# 观星书院 · Open Cosmos

星宙 AstroVerseDAO 的官方站点 —— 面向 AI 时代的开源通识学院。

我们不授予学位，我们提供一条完整的自学路径。

## 站点结构

| 页面 | 内容 |
| --- | --- |
| `index.html` | 首页：观星台首屏 · 修习机制摘要 · 入院 |
| `manifesto.html` | 壹 · 宣言 + 贰 · 信条 |
| `directions.html` | 叁 · 五大航向（五行星座图 + 航向列表） |
| `politics.html` | 第壹航向 · 政治（金 · 权力与秩序） |
| `economy.html` | 第贰航向 · 经济（土 · 金钱与时间） |
| `tech.html` | 第叁航向 · 科技（火 · 工具与创造）：TECH 000 · 101–107 阶段总览，点击进入阶段页 |
| `tech/<num>.html` | 每个阶段一页（`000, 101 … 107`）：主题 → 多校可选课程卡片 |
| `tech/course/<slug>.html` | 每门课程一页：所属大学 / 先修要求 / 编程语言 / 课程难度 / 预计学时 + 课程简介、评价与资源链接（对标北大 CSDIY） |
| `history.html` | 第肆航向 · 历史（木 · 记忆与智慧） |
| `cosmos.html` | 第伍航向 · 宇宙（水 · 星海与未知） |
| `path.html` | 修习机制：Piscine → 核心路径 → 谜题环 → 远征 → 毕业课题 |
| `join.html` | 入院：为什么加入 · 如何开始 · 社区准则 |

## 科技课程库 · TECH 000 → 107

科技航向是一条从零基础到深度学习系统的完整路径，共 **101 个静态页面**：

- `tech.html` —— 8 个阶段的总览（每个阶段一个编号、一个词：启航 / 数学 / 编程 / 系统 / 硬件 / 安全 / 智能 / 创造）；
- `tech/<num>.html` —— 每个阶段单独一页：阶段导读、过关项目、阶段导航、主题区块；
- `tech/course/<slug>.html` —— 每门课程单独一页：CSDIY 风格元信息（所属大学 / 先修要求 / 编程语言 / 课程难度 / 预计学时）+ 课程简介 + 评价 + 课程资源 + 同主题其他选择。

课程数据（92 门唯一课程、40 个主题、8 个阶段）与页面模板统一收敛在仓库根目录的 `build_tech.py` 中。修改课程只需改脚本里的 `STAGES` 数据，然后重新生成：

```bash
python build_tech.py    # 输出 tech.html + tech/*.html + tech/course/*.html（101 页）
```

生成结果全部是普通静态 HTML，运行时不需要构建工具。

## 技术

纯手写静态站，零构建、零依赖：HTML + CSS + 原生 JS（Canvas 星野 / IntersectionObserver / SVG 星座图）。唯一的"构建"是科技课程库的页面生成脚本 `build_tech.py`（仅改课程时运行，产物直接提交）。

## 部署

GitHub Pages：`main` 分支根目录直接发布。

线上地址：<https://astroversedao.github.io/>

## 参与

欢迎 Issue 与 Pull Request。社区准则：尊重每一个人 · 诚实与开放 · 分享即学习。
