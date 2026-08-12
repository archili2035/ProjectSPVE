import urllib.request
import json
import gzip
import zlib
import html
import xml.etree.ElementTree as ET
import datetime
import os
import collections

bvid = "BV1muTQ6CExQ"
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
out = "E:/WorkBuddyRepo/ProjectSPVE/04_exports/guiguang_raw_sample.json"


def fetch_bytes(url):
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Referer": "https://www.bilibili.com/video/" + bvid + "/"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
        enc = r.headers.get("Content-Encoding", "")
        if enc == "gzip":
            data = gzip.decompress(data)
        elif enc == "deflate":
            try:
                data = zlib.decompress(data)
            except zlib.error:
                data = zlib.decompress(data, -zlib.MAX_WBITS)
        return data


def fetch_json(url):
    return json.loads(fetch_bytes(url).decode("utf-8", "ignore"))


meta = fetch_json(f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}")["data"]
aid = meta["aid"]
comments = []
seen = set()


def add_reply(r, source, root=None):
    if not r or r.get("rpid") in seen:
        return
    seen.add(r.get("rpid"))
    ctime = r.get("ctime")
    comments.append({
        "source": source,
        "root": root,
        "rpid": r.get("rpid"),
        "ctime": ctime,
        "time": datetime.datetime.fromtimestamp(ctime).strftime("%Y-%m-%d %H:%M:%S") if ctime else "",
        "like": r.get("like", 0),
        "uname": r.get("member", {}).get("uname", ""),
        "message": r.get("content", {}).get("message", "").replace("\n", " "),
        "reply_count": r.get("rcount", 0) or r.get("count", 0) or 0,
    })


# 热门评论多翻几页；最新评论抓一页做即时补充。公开接口可能只返回可见样本，不视为全量。
for mode in [3, 2]:
    nexts = [0, 1, 2, 3, 4, 5] if mode == 3 else [0]
    for nx in nexts:
        try:
            data = fetch_json(f"https://api.bilibili.com/x/v2/reply/main?type=1&oid={aid}&mode={mode}&next={nx}&ps=20")
            for r in data.get("data", {}).get("replies") or []:
                add_reply(r, "热门评论" if mode == 3 else "最新评论")
                for rr in (r.get("replies") or [])[:5]:
                    add_reply(rr, "楼中楼", root=r.get("rpid"))
        except Exception as e:
            print("comment fetch err", mode, nx, e)

barrages = []
for page in meta["pages"]:
    cid = page["cid"]
    part = page["part"]
    try:
        data = fetch_bytes(f"https://comment.bilibili.com/{cid}.xml")
        text = data.decode("utf-8", "ignore")
        root = ET.fromstring(text)
        for d in root.findall("d"):
            p = d.attrib.get("p", "").split(",")
            sec = float(p[0]) if p and p[0] else 0
            barrages.append({
                "part": part,
                "sec": sec,
                "timecode": f"{int(sec // 60):02d}:{int(sec % 60):02d}",
                "text": html.unescape(d.text or ""),
            })
    except Exception as e:
        print("dm fetch err", cid, e)

keywords = ["中式", "志怪", "搜打撤", "第一人称", "冷兵器", "画风", "美术", "实机", "玩法", "道士", "道教", "怪", "鬼", "诡", "武器", "近战", "fps", "塔科夫", "燕云", "影之刃", "怪猎", "pve", "pvp", "单机", "多人", "优化", "氪金", "手游", "端游", "买断", "抽卡", "预约", "期待", "喜欢", "怕", "晕", "眩晕", "抄", "缝"]
counter = collections.Counter()
for item in comments:
    msg = item["message"].lower()
    for k in keywords:
        if k.lower() in msg:
            counter[k] += 1
for item in barrages:
    msg = item["text"].lower()
    for k in keywords:
        if k.lower() in msg:
            counter[k] += 1

bucket = collections.Counter()
for dm in barrages:
    bucket[int(dm["sec"] // 10) * 10] += 1

sample = {
    "collected_at": "2026-07-28 10:55 GMT+8",
    "url": "https://www.bilibili.com/video/" + bvid + "/",
    "meta": meta,
    "comments": comments,
    "danmaku": barrages,
    "keyword_counts": counter.most_common(),
    "danmaku_buckets": bucket.most_common(),
}
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w", encoding="utf-8") as f:
    json.dump(sample, f, ensure_ascii=False, indent=2)

print("saved", out)
print("comments", len(comments), "danmaku", len(barrages))
print("top keywords", counter.most_common(30))
print("top comments:")
for c in sorted(comments, key=lambda x: x["like"], reverse=True)[:30]:
    print(f"[{c['source']}] like={c['like']} rc={c['reply_count']} {c['message'][:120]}")
print("top danmaku buckets", bucket.most_common(10))
