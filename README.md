# ProjectSPVE

> 当前定位：角色驱动的 PVE 刷宝射击项目立项方案库。

🌐 **在线访问（GitHub Pages）：<https://archili2035.github.io/ProjectSPVE/>**

本仓库用于沉淀一个 PVE 刷宝射击游戏项目的早期方案、立项书、竞品研究、宣传片分析、阶段性决策和原始想法。

这里**不是实际游戏开发工程仓库**，不放置客户端、服务端、原型工程、资源包或可运行代码。当前目标是让方案讨论可以被持续修改、版本化、回溯和 diff。

## 1. 核心概念

一句话概念：

> 角色驱动的 PVE 刷宝射击。

展开表达：

> 以角色为核心商业化载体，以 TPS 刷宝射击为核心体验，以枪械、技能、遗物和词条为构筑材料，以高频 PVE 战斗、掉落循环和阶段性高难挑战为长期驱动的项目。

当前初步判断：

- 不优先选择 PVP 射击方向，避免直接进入流量、匹配、反外挂、竞技生态和头部厂商优势高度绑定的竞争区。
- PVE 刷宝构筑更适合承接角色商业化、长期养成、版本更新和构筑实验。
- 项目不应简单理解为“二次元版《遗迹2》”或“二次元版《流放之路》”，而应围绕“角色驱动 + 射击体验 + 刷宝构筑”重新组织设计。
- 艺术与产品口径倾向：风格化角色 + 暗黑微恐世界 + 复古朋克异常物件。

## 2. 当前目录结构

```text
ProjectSPVE/
├── README.md
├── 项目方向草案.md
├── 脑暴思路草稿.md
├── overview.md
├── ProjectLooterShooter.pptx
├── NZ_2025-08-23至2026-08-22 iPhone收入预估.csv
├── 00_raw/
│   └── 初始构想.txt
├── 01_discussion/
│   └── tps_pve_looter_build_vs_arpg.md
├── 02_references/
│   ├── 竞品研究_流放之路系列.md
│   └── 遗迹系列/
│       ├── 竞品研究_遗迹系列.md
│       ├── 遗迹2_资料索引.md
│       ├── 遗迹2_系统拆解.md
│       └── 遗迹2_装备与构筑.md
├── 03_decisions/
│   └── 宣传片评价框架.md
├── 04_exports/
│   ├── 脑暴思路草稿_游戏设计整理版.md
│   ├── pve_looter_competitor_data_20260823.md
│   ├── 立项书分页更新稿（overview_*.md / spve_*.md）
│   ├── pptx_extract/   # PPT 抽取文本
│   ├── 采集脚本（*.py）
│   ├── 宣传片原始数据（*_raw_sample.json）
│   └── 飞书思维笔记数据（mindnote_*.json）
├── 05_pic&videos/
│   ├── pics/   # 参考图、截图、Boss 概念图
│   └── videos/ # AI 生成的战斗演示视频
├── 06_techs/
│   └── tech_ref.md   # 技术参考链接
└── docs/             # GitHub Pages 静态页面
    ├── index.html
    ├── project_looter_shooter_proposal.html
    ├── spve_formal_project_proposal.html / .md
    ├── spve_project_proposal.html
    ├── trailer_analysis_index.html
    ├── trailer_quality_framework.html
    ├── assets/project_looter_shooter/   # 提案页图片资源
    └── *_trailer_report.html            # 各作品宣传片分析报告
```

## 3. 目录说明

| 路径 | 用途 |
| --- | --- |
| `README.md` | 仓库说明、目录说明、当前方案边界和维护方式。 |
| `项目方向草案.md` | 早期主方案文档，项目定位与关键设计问题的初稿。 |
| `脑暴思路草稿.md` | 世界观、玩法、买量测试等方向的原始脑暴记录。 |
| `overview.md` | 最近一次交付的更新概览。 |
| `ProjectLooterShooter.pptx` | Project Looter Shooter 立项书源文件（PPT）。 |
| `NZ_*.csv` | 竞品《逆战》iPhone 收入预估数据。 |
| `00_raw/` | 原始输入、未整理想法、访谈记录和临时材料。 |
| `01_discussion/` | 分主题讨论稿，例如战斗结构、角色系统、商业化、副玩法等。 |
| `02_references/` | 竞品、题材、美术、玩法、系统资料等参考研究。 |
| `03_decisions/` | 已形成阶段性结论的决策记录。 |
| `04_exports/` | 阶段性导出、采集脚本、原始数据、汇报材料。 |
| `05_pic&videos/` | 图片、视频等媒体素材。 |
| `06_techs/` | 技术参考链接与工程向调研。 |
| `docs/` | 静态 HTML 页面，用于 GitHub Pages 在线访问。 |

## 4. 当前已整理内容

### 4.1 立项书与主方案

- `docs/project_looter_shooter_proposal.html`
  - Project Looter Shooter 立项书网页版（由 `ProjectLooterShooter.pptx` 逐字转译）。
  - 方向论证、竞品数据、核心设计、团队范围与研发节奏。

- `docs/spve_formal_project_proposal.html` / `docs/spve_formal_project_proposal.md`
  - SPVE 项目立项书（正式整理版）。
  - 项目摘要、品类机会、平台判断、核心设计、商业化、风险与立项建议。

- `docs/spve_project_proposal.html`
  - SPVE 立项书早期版：风格化暗黑朋克刷宝射击。

- `项目方向草案.md`
  - 早期主方案：项目定位、三层分工、主控结构、内容结构、题材方向与验证问题。

- `脑暴思路草稿.md`
  - 世界观方向（苏联朋克 / 原子之心风格及延展）、玩法方向（类遗迹2，TPS / FPS 取舍）。

### 4.2 讨论稿

- `01_discussion/tps_pve_looter_build_vs_arpg.md`
  - TPS PVE 刷宝的核心战斗与 Build 相对 ARPG 的优劣势分析。

### 4.3 竞品研究

- `02_references/竞品研究_流放之路系列.md`
  - 关注 Build 野心、掉落循环、赛季机制、终局结构和新手门槛。

- `02_references/遗迹系列/竞品研究_遗迹系列.md`
  - 关注程序化冒险结构、机制型 Boss、横向构筑装备、隐藏收集和低门槛合作。

- `02_references/遗迹系列/遗迹2_资料索引.md`
  - 用于沉淀《遗迹2》的资料源、系统分类和后续拆解入口。

- `02_references/遗迹系列/遗迹2_系统拆解.md`
  - 《遗迹2》系统拆解，涵盖模式、世界生成、World Stone、战斗、职业、装备、成长缩放、Boss 奖励、多人、DLC、Boss Rush 与 Prism 系统。

- `02_references/遗迹系列/遗迹2_装备与构筑.md`
  - 关注《遗迹2》的职业、武器、模组、突变因子、戒指、项链、遗物、特性等构筑层级。

- `NZ_*.csv`
  - 竞品《逆战》iPhone 收入预估数据（2025-08-23 至 2026-08-22）。

### 4.4 决策与框架

- `03_decisions/宣传片评价框架.md`
  - 以“第一钩子、品质、美与实机”为核心的游戏宣传片评价标准。

### 4.5 宣传片分析（GitHub Pages 页面）

- `docs/trailer_quality_framework.html`
  - 宣传片评价框架的网页版。

- `docs/trailer_analysis_index.html`
  - 宣传片分析索引。

- 各作品宣传片分析报告（`docs/*_trailer_report.html`）：
  - 《原子之心2》
  - 《毁灭战士：黑暗时代》
  - 《诡影藏锋》
  - 《重返未来：1999》
  - 《逆向坍塌：F》
  - 《望月》

### 4.6 技术参考

- `06_techs/tech_ref.md`
  - GDC《三角洲行动》世界创建：跨平台开发美术管线和工具（腾讯游戏学堂）。

### 4.7 媒体素材

- `05_pic&videos/pics/`
  - 参考图、截图、Boss 概念图等。

- `05_pic&videos/videos/`
  - AI 生成的战斗演示视频（可灵、Seedance）。

## 5. 维护原则

1. **只讨论方案，不进入开发实现。**
   - 不在本仓库放置游戏工程、客户端代码、服务端代码或资源工程。

2. **原始材料与整理稿分离。**
   - 未整理输入放入 `00_raw/`。
   - 经过结构化整理的内容放入对应主题目录。

3. **主方案保持可 diff。**
   - 重大方向变化优先修改对应立项书或主方案文档。
   - 分主题展开可新增到 `01_discussion/`，形成结论后再回填主方案或写入 `03_decisions/`。

4. **参考资料保留来源边界。**
   - 竞品研究、资料索引和系统拆解放入 `02_references/`。
   - 尽量区分事实记录、资料摘录和设计转译。

5. **阶段性结论单独沉淀。**
   - 一旦某个方向被确认、推翻或暂缓，应在 `03_decisions/` 中记录原因、日期和影响范围。

6. **HTML 页面归入 `docs/`。**
   - 所有需要在线浏览的 HTML 页面放入 `docs/`，以便 GitHub Pages 部署。

7. **本地状态与敏感文件不入库。**
   - `.workbuddy/`、`.lark-auth/`、`.lark-slides/`、`.learnings/` 等本地状态与鉴权文件已通过 `.gitignore` 排除。

## 6. 建议的 Git 使用方式

查看修改：

```bash
git diff
```

提交修改：

```bash
git add .
git commit -m "Update project notes"
```

推送到 GitHub：

```bash
git push
```

## 7. GitHub Pages

- 在线访问入口：<https://archili2035.github.io/ProjectSPVE/>
- 部署目录：`docs/`
- 在仓库 Settings → Pages 中将 Source 设为 `Deploy from a branch`，分支选 `main`，目录选 `/docs`。

## 8. 待决策问题

以下问题建议后续逐步形成决策记录：

1. 主控结构：单主控 + 支援角色，还是多角色切换。
2. 角色与枪械关系：角色是否绑定专武，枪械是否参与抽取，武器是否主要通过刷宝获得。
3. 地图结构：传统副本、半开放战区、肉鸽地宫、枢纽 + 裂隙之间如何取舍。
4. 题材母题：异常都市、复古科技、移动据点、梦境废墟，哪一个作为主轴。
5. 联机权重：单人为主、合作为补充，还是多人合作为核心体验。
6. 副玩法边界：基地、档案、角色休整区是否足够，是否需要更重的都市/建造玩法。
7. 商业化边界：角色抽取、武器获取、皮肤、基地外观和战令之间的优先级。
