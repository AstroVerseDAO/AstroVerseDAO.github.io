# -*- coding: utf-8 -*-
"""
星宙 · 科技航向页面生成器
从统一数据源生成：
  tech.html                    阶段总览（TECH 000 → 107，两字命名）
  tech/<num>.html              每个阶段的独立页面（主题 → 课程列表）
  tech/course/<slug>.html      每门课程的详情页（简介 + 评价 + 资源链接）
运行：python build_tech.py   （ROOT 取脚本所在目录，可在任意目录运行）
"""

import os
import html

# ============================================================
# 数据
#   stage  字段：num  name  en  desc  goal  prereq  topics
#   option 字段：slug  s（学校/出处） c（课号/课程代码） t（课程名） u（链接）
#                intro  review  tags  links
#                + lang（编程语言） diff（难度 1-5） hours（预计学时）
#                + 可选 prereq（覆盖阶段级先修兜底）
#   注意：同一课程可出现在多个阶段（如 cs50x / cs106b），课程详情页取
#         unique_courses() 里的首次出现；两处 occurrence 都必须带完整元数据。
# ============================================================

STAGES = [
    {
        "num": "000", "name": "启航", "en": "BOOTCAMP",
        "desc": "磨刀不误砍柴工。在正式学任何一门课之前，先花两周把工具备齐：一台能命令行驱动的电脑、一个 GitHub 账号、一套提问与检索的方法论。这些在大学课表里没有学分，却是之后所有学习的杠杆。",
        "goal": "用命令行脚本自动化一件日常琐事；建一个 GitHub 仓库管理你的全部学习笔记。",
        "prereq": "无（零基础可入；一台能上网的电脑即可）",
        "topics": [
            {
                "id": "panorama", "name": "计算机全景图", "why": "先见森林，再见树木。Computers are not magic!",
                "options": [
                    dict(slug="crashcourse-cs", lang="无代码", diff=1, hours=8, s="Crash Course", c="Computer Science", t="计算机科学速成课",
                         u="https://www.youtube.com/playlist?list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo",
                         intro="8 小时动画科普：从继电器到人工智能的全貌，零基础第一站。",
                         review="每集十分钟出头，动画制作精良，把抽象概念讲得极具画面感。它不教你写代码，而是给你一张「地图」——之后学任何一门课，你都知道自己站在地图的哪个位置。B 站有全套中文字幕，通勤路上就能刷完。",
                         tags=["视频", "零基础", "B站有中字"],
                         links=[("B 站中字全集", "https://www.bilibili.com/video/BV1EW411u7th/")]),
                    dict(slug="cs50x", lang="C / Python", diff=3, hours=100, s="Harvard", c="CS50x", t="This is CS50",
                         u="https://cs50.harvard.edu/x/",
                         intro="全球最知名的 CS 导论课，从 C 讲到 Web，Project 成就感拉满。",
                         review="Harvard 的镇校之宝，教授 David Malan 的课堂感染力无人能及。以 C 语言为主线打穿内存与指针，再平滑过渡到 Python、SQL 与 Web。作业是真正的项目而非习题，每年更新、全部免费。唯一的「缺点」是体量偏大，但值得。",
                         tags=["100h", "零基础", "推荐"],
                         links=[("edX 免费修读入口", "https://www.edx.org/learn/computer-science/harvard-university-cs50-s-introduction-to-computer-science")]),
                ],
            },
            {
                "id": "toolchain", "name": "工具链一课", "why": "大学里缺失、工作中天天用的那些工具。",
                "options": [
                    dict(slug="missing-semester", lang="Shell", diff=2, hours=20, s="MIT", c="Missing Semester", t="计算机教育中缺失的一课",
                         u="https://missing.csail.mit.edu/",
                         intro="Shell、Vim、Git、调试、自动化、安全——一门课补齐工具链。CSDIY 强烈推荐给小白。",
                         review="MIT 的三位助教发现：学校教你算法，却没人教你用工具。于是有了这门课。11 讲覆盖 Shell 脚本、Vim、Git 进阶、调试与性能分析、元编程、安全，每一讲都配练习。学完它的回报率，可能是整个目录里最高的。有热心社区维护的中文版。",
                         tags=["20h", "推荐", "有中文版"],
                         links=[("中文翻译版", "https://missing-semester-cn.github.io/")]),
                    dict(slug="art-of-command-line", lang="Shell", diff=2, hours=8, s="开源社区", c="命令行的艺术", t="The Art of Command Line",
                         u="https://github.com/jlevy/the-art-of-command-line",
                         intro="GitHub 十万 stars 的顶流教程，被译成十几种语言，值得反复通读。",
                         review="一页文档，浓缩了作者几十年的命令行功力。不求一次全记住，先通读留印象，遇到问题时回来速查——这正是它的设计用法。中文版翻译质量很高。",
                         tags=["文档", "速查"], links=[]),
                ],
            },
            {
                "id": "ask", "name": "学会提问与检索", "why": "提问是开源社区的第一项生存技能。",
                "options": [
                    dict(slug="how-to-ask", lang="无代码", diff=1, hours=2, s="Eric S. Raymond", c="提问的智慧", t="How To Ask Questions The Smart Way",
                         u="https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way",
                         intro="hacker 文化的提问圣经：如何用简洁的文字让别人瞬间理解你的处境与目的。",
                         review="写于 2001 年，至今仍是开源社区的通行礼仪。它教你：先做什么功课、如何描述最小复现、在哪里提问、如何追问。读完你再提的问题，被回答的概率会完全不同。",
                         tags=["文档", "必读"], links=[]),
                    dict(slug="self-debug", lang="无代码", diff=1, hours=2, s="方法论", c="自主排查", t="文档 → 搜索 → 最小复现",
                         u="https://missing.csail.mit.edu/",
                         intro="遇到问题先查文档与报错，再搜索，最后才提问——这个周期本身就是最好的练习。",
                         review="这不是一门课，而是一条纪律：报错信息读三遍，官方文档搜一遍，搜索引擎问一遍，最小复现做一遍——80% 的问题活不到提问那一步。把它贴在桌前。",
                         tags=["习惯"], links=[]),
                ],
            },
            {
                "id": "git", "name": "Git 与 GitHub", "why": "代码版本控制 + 全球最大开源社区。",
                "options": [
                    dict(slug="pro-git", lang="Shell / Git", diff=2, hours=15, s="官方", c="Pro Git", t="Git 权威指南（免费电子书）",
                         u="https://git-scm.com/book/zh/v2",
                         intro="出自 Linux 之父之手的 Git 是必掌握的神器，前五章就够日常使用。",
                         review="Git 官方唯一指定书籍，免费开源、官方中译。前五章覆盖 95% 的日常场景；后面的「Git 内部原理」章节强烈建议读——理解了对象模型，Git 再也不是玄学。",
                         tags=["书", "免费"], links=[]),
                    dict(slug="github-skills", lang="Git / GitHub", diff=1, hours=6, s="GitHub", c="Skills", t="交互式官方教程",
                         u="https://skills.github.com/",
                         intro="在真实仓库里边做边学：提交、分支、PR、Actions。",
                         review="GitHub 官方出品的交互式教程：每门课都是一个真实仓库，机器人 Reviewer 陪你一步步完成提交、分支、合并与 PR。一个下午就能上手，零安装零配置。",
                         tags=["交互", "零基础"], links=[]),
                ],
            },
            {
                "id": "editor", "name": "编辑器与排版", "why": "写代码的地方，值得认真对待。",
                "options": [
                    dict(slug="vscode-vim", lang="无代码（工具）", diff=2, hours=15, s="VS Code / Vim", c="二选一再双修", t="现代编辑器与上古神器",
                         u="https://code.visualstudio.com/",
                         intro="VS Code 插件生态即开即用；Vim 学习曲线陡峭但终生受益（几乎所有 IDE 都有 Vim 插件）。",
                         review="先用 VS Code 解决「现在就要干活」，再花两周在 VS Code 里装 Vim 插件练 modal editing。前者是这个时代的默认答案，后者是一笔五十年后仍有利息的投资。",
                         tags=["工具"],
                         links=[("Vim 官方交互教程（终端输入 vimtutor）", "https://vimhelp.org/")]),
                    dict(slug="latex-lshort", lang="LaTeX", diff=2, hours=15, s="LaTeX", c="lshort", t="一份（不太）简短的 LaTeX 介绍",
                         u="https://www.overleaf.com/learn",
                         intro="论文与数学笔记的排版标准。配合 Overleaf 在线使用，零配置。",
                         review="lshort 是全球 LaTeX 学习者的共同起点，有高质量中译本。不必本地装环境——注册 Overleaf 直接在线写。等你需要交论文或写数学笔记时，会感谢现在花掉的这两天。",
                         tags=["排版", "免费"],
                         links=[("lshort 中文版 PDF", "https://ctan.org/pkg/lshort-zh-cn")]),
                ],
            },
        ],
    },

    {
        "num": "101", "name": "数学", "en": "MATHEMATICS",
        "desc": "学好微积分和线代，和写代码至少同等重要。数学不是考完就忘的考题，而是理解 AI、信号、控制乃至世界运行方式的语言。学本质，不背公式。",
        "goal": "用 LaTeX 写一份数学笔记，把一个定理推导到底并配一张可视化图。",
        "prereq": "高中数学（函数、三角、极限基础）",
        "topics": [
            {
                "id": "calculus", "name": "微积分", "why": "变化率与累积——一切连续现象的母语。",
                "options": [
                    dict(slug="mit-1801sc", lang="数学", diff=4, hours=180, s="MIT", c="18.01SC / 18.02SC", t="单变量与多变量微积分",
                         u="https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/",
                         intro="OCW 完整开放，notes 浅显生动、直抓本质，不再疲于做题。",
                         review="SC 后缀代表 Scholar 版本：专为自学者打包，讲义、习题、答案、考试一应俱全。讲法直奔几何与物理直觉，而非刷题套路。18.02SC 把多元微积分同样处理，两门连读效果最好。",
                         tags=["OCW", "推荐"],
                         links=[("18.02SC 多变量微积分", "https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/")]),
                    dict(slug="essence-of-calculus", lang="无代码", diff=2, hours=10, s="3Blue1Brown", c="微积分的本质", t="Essence of Calculus",
                         u="https://www.3blue1brown.com/topics/calculus",
                         intro="用动画直抵微积分的几何直觉，配合 MIT 课程食用更佳。",
                         review="Grant Sanderson 的动画让「导数」和「积分」变成你能看见的东西。建议在学 MIT 课程之前先刷一遍建立直觉，学完后再刷一遍串联理解——两遍感受完全不同。",
                         tags=["视频", "直觉"],
                         links=[("B 站官方中字", "https://space.bilibili.com/88461692")]),
                ],
            },
            {
                "id": "linalg", "name": "线性代数", "why": "矩阵、向量空间、特征分解——神经网络与数据科学的基础。",
                "options": [
                    dict(slug="mit-1806", lang="数学", diff=3, hours=100, s="MIT", c="18.06", t="Linear Algebra（Gilbert Strang）",
                         u="https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/",
                         intro="数学大牛 Strang 的经典课，教材已被清华采用。",
                         review="Strang 老爷子是线性代数教学的活传奇：不讲行列式开头的天书，从 Ax=b 的列图像讲起，直指四个基本子空间。这门课录像拍摄于他退休前，是一代人的共同记忆。OCW 全开放。",
                         tags=["OCW", "推荐"], links=[]),
                    dict(slug="essence-of-linalg", lang="无代码", diff=2, hours=8, s="3Blue1Brown", c="线性代数的本质", t="Essence of Linear Algebra",
                         u="https://www.3blue1brown.com/topics/linear-algebra",
                         intro="把「矩阵即变换」刻进直觉，看完再看任何一门课都会轻松很多。",
                         review="整个 3Blue1Brown 频道的成名系列。「矩阵是对空间的变换」这一个视角，能串起你之后会遇到的特征值、行列式、SVD 乃至神经网络。必看，且值得反复看。",
                         tags=["视频", "直觉"],
                         links=[("B 站官方中字", "https://space.bilibili.com/88461692")]),
                ],
            },
            {
                "id": "prob", "name": "离散数学与概率论", "why": "算法推导与证明的工具，高阶课程的先修。",
                "options": [
                    dict(slug="cs70", lang="数学", diff=4, hours=60, s="UC Berkeley", c="CS70", t="Discrete Math and Probability Theory",
                         u="https://www.eecs70.org/",
                         intro="每个模块都配算法实例：逻辑→稳定匹配、数论→RSA、概率→哈希与负载均衡。",
                         review="伯克利把离散数学和概率论缝合成一门课，且每个概念都立刻给出 CS 应用——数论讲完就上 RSA，图论讲完就上稳定匹配。notes 完全公开，写作质量堪称教科书级别。",
                         tags=["60h", "推荐"], links=[]),
                    dict(slug="mit-6042", lang="数学", diff=3, hours=80, s="MIT", c="6.042J", t="Mathematics for Computer Science",
                         u="https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/",
                         intro="面向 CS 的离散数学，教材《Mathematics for CS》免费开源。",
                         review="MIT 版本的 CS 数学课，教材全文免费且写得异常清晰，证明范式讲得尤其扎实。如果你想要一本能反复查阅的案头教材，选它。",
                         tags=["OCW", "开源教材"], links=[]),
                    dict(slug="cs126", lang="Python / 数学", diff=4, hours=100, prereq="CS70 或 6.042J（离散数学与概率）", s="UC Berkeley", c="CS126", t="Probability Theory（进阶）",
                         u="https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E8%BF%9B%E9%98%B6/CS126/",
                         intro="随机过程与深入理论，大量 Python 作业让你用代码验证概率。",
                         review="CS70 的进阶续集：随机过程、马尔可夫链、大数定律的深入处理。特色是大量用 Python 模拟验证定理的作业——概率论第一次变得「看得见」。适合打算走 AI/数据方向的人。",
                         tags=["进阶"], links=[]),
                ],
            },
            {
                "id": "info", "name": "信息论入门", "why": "编码、压缩、信息熵——AI 时代理解数据本质的核心。",
                "options": [
                    dict(slug="mit-6050", lang="数学", diff=2, hours=40, s="MIT", c="6.050J", t="Information Theory and Entropy",
                         u="https://ocw.mit.edu/courses/6-050j-information-and-entropy-spring-2008/",
                         intro="专为大一新生设计，几乎零先修：编码、压缩、通信、信息熵，非常有趣。",
                         review="一门为新生设计的宝藏小课：从「如何给信息称重」讲起，一路讲到压缩、信道与熵。它会在你心里种下「信息是一种物理量」的直觉——这在 AI 时代越来越值钱。",
                         tags=["零基础", "推荐"], links=[]),
                ],
            },
            {
                "id": "numerical", "name": "数值分析（选修）", "why": "用离散的计算机逼近连续的数学——计算思维。",
                "options": [
                    dict(slug="mit-ct-julia", lang="Julia", diff=2, hours=40, s="MIT", c="Computational Thinking", t="计算思维入门（Julia）",
                         u="https://computationalthinking.mit.edu/",
                         intro="全部开源：图像处理、社科数据、气候建模三个主题里体验计算与科学的结合。",
                         intro2=None,
                         review="MIT 在疫情期间火出圈的直播课：用 Julia 的 Pluto 交互笔记本，边改代码边看图像、气候模型实时变化。它教的不是语法，而是「用计算理解世界」的思维方式。零基础可入。",
                         tags=["Julia", "零基础"], links=[]),
                    dict(slug="mit-18330", lang="Julia / 数学", diff=4, hours=100, prereq="微积分 + 线性代数", s="MIT", c="18.330", t="Introduction to Numerical Analysis",
                         u="https://github.com/mitmath/18330",
                         intro="浮点编码、求根、线性系统、微分方程；配套开源教材与 Julia 实例。",
                         review="数值分析的正经入门：浮点误差、迭代求根、最小二乘、微分方程数值解。仓库里教材与 Julia 代码全部开源。想认真搞科学计算或 ML 系统的人绕不开它。",
                         tags=["进阶"], links=[]),
                ],
            },
            {
                "id": "diffeq", "name": "微分方程（选修）", "why": "用方程刻画世间万物的运动，换一个视角看世界。",
                "options": [
                    dict(slug="mit-1803sc", lang="数学", diff=3, hours=80, prereq="单变量微积分", s="MIT", c="18.03SC", t="Differential Equations",
                         u="https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/",
                         intro="常微分方程的求解与直觉，OCW 完整开放。",
                         review="OCW Scholar 版本自学者友好：从指数增长到振动与共振，把「方程描述运动」的感觉讲透了。学完它再去看控制论与动力系统，会顺畅很多。",
                         tags=["OCW"], links=[]),
                ],
            },
            {
                "id": "mathadv", "name": "数学高阶（按需自取）", "why": "面向科研与高阶工程，兴趣驱动。",
                "options": [
                    dict(slug="ee364a", lang="数学 / Python", diff=5, hours=120, prereq="线性代数、微积分、概率论", s="Stanford", c="EE364A", t="Convex Optimization 凸优化",
                         u="https://web.stanford.edu/class/ee364a/",
                         intro="机器学习的数学地基。Boyd 主讲，教材《Convex Optimization》免费开源。",
                         review="Stephen Boyd 是凸优化领域的化身。这门课+那本免费开源的大部头教材，是 ML 理论方向的入场券。难度不低，需要扎实的线代与微积分，但学完看论文的眼光会彻底不同。",
                         tags=["★★★★"],
                         links=[("教材官方免费 PDF", "https://web.stanford.edu/~boyd/cvxbook/")]),
                    dict(slug="mit-18650", lang="数学 / R", diff=5, hours=100, prereq="概率论、线性代数", s="MIT", c="18.650", t="Statistics for Applications 应用统计",
                         u="https://ocw.mit.edu/courses/18-650-statistics-for-applications-fall-2016/",
                         intro="面向应用的统计学研究生课，讲义完整开放。",
                         review="从估计、假设检验到回归与贝叶斯视角，数学严谨但始终面向应用。讲义质量极高，适合想在 ML 之外补上统计学内功的人。",
                         tags=["★★★★"], links=[]),
                    dict(slug="cs255", lang="数学", diff=4, hours=80, prereq="离散数学、概率论", s="Stanford", c="CS255", t="Cryptography 密码学",
                         u="https://www.coursera.org/learn/crypto",
                         intro="Dan Boneh 的密码学课，Coursera 版本免费开放。",
                         review="Dan Boneh 是应用密码学的旗帜人物。从流密码、分组密码到公钥体系，推导严谨、节奏紧凑。对安全航向（TECH 105）和区块链方向都是硬通货。",
                         tags=["★★★★"], links=[]),
                ],
            },
        ],
    },

    {
        "num": "102", "name": "编程", "en": "FIRST LANGUAGES",
        "desc": "语言是工具，没有完美的语言，只有合适的工具。选定一门主语言学透（推荐 Python 或 C），其余按需涉猎。本阶段每个主题都给出多所学校的选择——选一门跟到底，别全收藏。",
        "goal": "完成 CS61A 或 CS50 的全部 Project，放进你的 GitHub。",
        "prereq": "000 启航（命令行、Git、编辑器）",
        "topics": [
            {
                "id": "clang", "name": "C 语言", "why": "离机器最近的高级语言，理解内存与指针的必修课。",
                "options": [
                    dict(slug="cs50x", lang="C / Python", diff=3, hours=100, s="Harvard", c="CS50x", t="This is CS50",
                         u="https://cs50.harvard.edu/x/",
                         intro="以 C 为主线的导论课：内存、指针、数据结构一次打穿，再平滑过渡到 Python。",
                         review="见 TECH 000 的完整评价——用 CS50 学 C 的好处是：你在写真正有趣的程序（图像滤镜、拼写检查器）的过程中被迫驯服指针与内存，痛苦但深刻。",
                         tags=["100h", "推荐"], links=[]),
                    dict(slug="zju-wengkai-c", lang="C", diff=2, hours=60, s="浙江大学", c="翁恺 · C 语言程序设计", t="中国大学 MOOC",
                         u="https://www.icourse163.org/course/ZJU-9001",
                         intro="中文世界最受欢迎的 C 入门课，讲解细致，配套 PTA 在线评测。",
                         review="翁恺老师的课是无数中国学生的 C 语言启蒙：语速平缓、示例生活化，把指针这种拦路虎讲得像唠家常。配套 PTA 平台在线判题，作业即写即评。中文零基础首选。",
                         tags=["中文", "零基础"], links=[]),
                    dict(slug="kr-c", lang="C", diff=3, hours=20, prereq="先跟完一门 C 语言课", s="K&R", c="《C 程序设计语言》", t="The C Programming Language",
                         u="https://csdiy.wiki/%E5%A5%BD%E4%B9%A6%E6%8E%A8%E8%8D%90/",
                         intro="C 之父写的薄书，学完一门课后通读一遍，常有顿悟。",
                         review="Kernighan 与 Ritchie——C 语言的作者亲自写的书，不到 300 页却字字珠玑。不建议零基础直接啃，建议跟着一门课学完后通读：每一章都会让你发出「原来如此」的感叹。",
                         tags=["书", "进阶"], links=[]),
                ],
            },
            {
                "id": "python", "name": "Python", "why": "AI 时代的第一语言，语法温和、生态无敌。",
                "options": [
                    dict(slug="cs50p", lang="Python", diff=2, hours=60, s="Harvard", c="CS50P", t="Introduction to Programming with Python",
                         u="https://cs50.harvard.edu/python/",
                         intro="10 周系统掌握 Python：函数、库、单测、正则、OOP。比 CS61A 温和。",
                         review="CS50 家族的 Python 专项，保持了同样的制作水准与作业质量。10 周从变量讲到面向对象，每周一个真实的编程作业。想要温和而完整的入门体验，选它。",
                         tags=["60h", "零基础"], links=[]),
                    dict(slug="cs61a", lang="Python", diff=4, hours=50, s="UC Berkeley", c="CS61A", t="SICP（Python 版）",
                         u="https://cs61a.org/",
                         intro="不只是语言课：数据抽象、函数式、OOP，最后用 Python 写一个 Scheme 解释器。",
                         review="伯克利 CS 第一课，精神续作自 MIT 神书 SICP。它表面教 Python，实际教「程序设计的方法」：高阶函数、递归、数据抽象、解释器。期末项目是用 Python 写一个 Scheme 解释器——写完你就不再是初学者。配套在线教材 Composing Programs 免费。",
                         tags=["50h", "推荐"],
                         links=[("配套教材 Composing Programs", "https://www.composingprograms.com/")]),
                    dict(slug="mit-6100l", lang="Python", diff=3, hours=80, s="MIT", c="6.100L", t="Intro to CS and Programming using Python",
                         u="https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/",
                         intro="MIT 官方 Python 入门，OCW 完整开放。",
                         review="经典 6.0001 的新版：节奏平稳、讲义齐全，附带完整的习题与解答。风格比 CS61A 保守，适合喜欢「教科书式」循序渐进的人。",
                         tags=["OCW"], links=[]),
                ],
            },
            {
                "id": "cpp", "name": "C++", "why": "系统课（CS144、15-445）与图形学的入场券。",
                "options": [
                    dict(slug="cs106b", lang="C++", diff=4, hours=100, prereq="编程基础（函数、循环、递归）", s="Stanford", c="CS106B/X", t="Programming Abstractions",
                         u="https://web.stanford.edu/class/cs106b/",
                         intro="以 C++ 描述的抽象与数据结构入门，递归讲得极好。",
                         review="斯坦福 CS 第二课，用 C++ 讲抽象与递归——递归部分的教学被公认为全世界最好的之一。 assignments 从热身小游戏一路做到真实的算法问题。它也是 TECH 103 数据结构的 C++ 路线之选。",
                         tags=["推荐"], links=[]),
                    dict(slug="cs106l", lang="C++", diff=3, hours=30, prereq="CS106B 或 C++ 基础", s="Stanford", c="CS106L", t="Standard C++ Programming",
                         u="https://web.stanford.edu/class/cs106l/",
                         intro="现代 C++ 标准库速通：STL、流、模板，为系统课铺路。",
                         review="一门「C++ 标准库使用手册」式的短课：容器、迭代器、lambda、模板与 RAII，直奔现代 C++ 的正确用法。CS106B 之后、CS144 之前的完美衔接。",
                         tags=["速通"], links=[]),
                ],
            },
            {
                "id": "java", "name": "Java", "why": "CS61B 与软件工程课的教学语言。",
                "options": [
                    dict(slug="mit-6092", lang="Java", diff=2, hours=20, s="MIT", c="6.092", t="Introduction to Programming in Java",
                         u="https://ocw.mit.edu/courses/6-092-introduction-to-programming-in-java-january-iap-2010/",
                         intro="IAP 短课，快速掌握 Java 语法与 OOP 基础。",
                         review="MIT 一月短学期课，几天时间覆盖 Java 语法与面向对象基础。目标不是精通，而是让你拿到「Java 读写能力」，好去接 CS61B 这样的大课。",
                         tags=["短课"], links=[]),
                ],
            },
            {
                "id": "rust", "name": "Rust（选修）", "why": "内存安全的新系统语言，未来基础设施的宠儿。",
                "options": [
                    dict(slug="cs110l", lang="Rust", diff=4, hours=60, prereq="C/C++ 与系统编程基础", s="Stanford", c="CS110L", t="Safety in Systems Programming",
                         u="https://web.stanford.edu/class/cs110l/",
                         intro="用 Rust 重新思考系统编程中的安全性。",
                         review="斯坦福系统课 CS110 的 Rust 侧翼：所有权与借用检查器放在系统编程语境里讲，比单纯学语法深刻得多。建议有了 C/C++ 与系统的底子再来。",
                         tags=["进阶"], links=[]),
                ],
            },
            {
                "id": "ocaml", "name": "OCaml（选修）", "why": "函数式编程的美学，编译器与形式化方向的入口。",
                "options": [
                    dict(slug="cs3110", lang="OCaml", diff=4, hours=80, s="Cornell", c="CS3110", t="OCaml Programming: Correct + Efficient + Beautiful",
                         u="https://cs3110.github.io/textbook/cover.html",
                         intro="教材完全开源，函数式思维会反过来改善你所有的代码。",
                         review="康奈尔的函数式编程课，标题即纲领：正确、高效、优雅。即使你以后一行 OCaml 都不写，模式匹配与不可变数据的思维也会渗透进你写的每一行 Python 和 C++。",
                         tags=["开源教材"], links=[]),
                ],
            },
        ],
    },
]

STAGES += [
    {
        "num": "103", "name": "系统", "en": "SYSTEMS CORE",
        "desc": "没有什么能比自己写个内核、写个 TCP 栈、写个数据库更能加深理解。这一层是 CS 的任督二脉：数据结构与算法 → 体系结构 → 操作系统 → 网络 → 数据库 → 编译器。每一门都配重实践。",
        "goal": "迷你操作系统（xv6 扩展）/ 迷你 TCP 协议栈 / 迷你数据库，任选其一。",
        "prereq": "102 编程（至少一门主语言）+ 101 数学基础",
        "topics": [
            {
                "id": "dsa", "name": "数据结构与算法", "why": "CS 的核心，几乎一切专业课的基础。",
                "options": [
                    dict(slug="cs61b", lang="Java", diff=4, hours=60, s="UC Berkeley", c="CS61B", t="Data Structures and Algorithms",
                         u="https://sp24.datastructur.es/",
                         intro="14 Lab 亲手实现数据结构，3 个上千行 Project（简易谷歌地图、二维 Minecraft），autograder 开源。",
                         review="伯克利数据结构课，自学者口碑第一梯队：每个数据结构都亲手实现，三个大项目有完整的自动评分器，做完简历上能写两行。课程网站历学期全部公开，Josh Hug 的 lecture 生动有趣。需要一点 Java 基础。",
                         tags=["Java", "60h", "推荐"], links=[]),
                    dict(slug="princeton-algs", lang="Java", diff=4, hours=100, s="Princeton", c="Algorithms I & II", t="Coursera 算法专项",
                         u="https://www.coursera.org/learn/algorithms-part1",
                         intro="Sedgewick 的经典课，深入浅出，配套 algs4 网站与评测。",
                         review="Sedgewick 是算法教材的活化石（Knuth 的学生）。课程不教证明、专注实现与应用，作业自动评分且设计精巧（如用并查集做渗透模拟）。配套 algs4 网站是极好的速查手册。",
                         tags=["Java", "Coursera"],
                         links=[("配套网站 algs4", "https://algs4.cs.princeton.edu/")]),
                    dict(slug="mit-6006", lang="Python", diff=4, hours=90, s="MIT", c="6.006", t="Introduction to Algorithms",
                         u="https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/",
                         intro="偏好 Python 的算法入门之选。",
                         review="MIT 的算法入门，理论深度高于 CS61B、Princeton，讲义与习题完整开放。如果你打算读 CLRS 或走理论方向，这门课的节奏与你合拍。",
                         tags=["Python", "OCW"], links=[]),
                    dict(slug="cs106b", lang="C++", diff=4, hours=100, prereq="编程基础（函数、循环、递归）", s="Stanford", c="CS106B/X", t="Programming Abstractions",
                         u="https://web.stanford.edu/class/cs106b/",
                         intro="想走 C/C++ 路线的数据结构与基础算法课。",
                         review="见 TECH 102 的完整评价——在数据结构语境下，它是 C++ 路线的最佳起点：从容器抽象讲到链表、树、图的经典实现。",
                         tags=["C++"], links=[]),
                    dict(slug="cs170", lang="数学 / Python", diff=5, hours=100, prereq="数据结构与算法", s="UC Berkeley / MIT", c="CS170 / 6.046", t="高阶算法与 NP（进阶）",
                         u="https://cs170.org/",
                         intro="算法设计与分析，以及 NP 问题的艺术。",
                         review="分治、动态规划、线性规划、NP 完全性的系统训练。CS170 的讨论课材料与历年题完全公开，是算法进阶与面试高阶题的共同源头。学完它，你看算法的眼神会变。",
                         tags=["进阶"],
                         links=[("MIT 6.046 版本", "https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/")]),
                ],
            },
            {
                "id": "arch", "name": "体系结构", "why": "从与非门到 CPU——计算机的世界真是 01 构成的。",
                "options": [
                    dict(slug="nand2tetris", lang="HDL / 汇编", diff=3, hours=40, s="Nand2Tetris", c="I & II", t="从零造一台计算机",
                         u="https://www.nand2tetris.org/",
                         intro="Coursera 满分神课：逻辑门 → CPU → 编译器 → OS，最后在自己造的机器上跑俄罗斯方块。零门槛。",
                         review="可能是全世界好评率最高的 CS 课：从一颗与非门出发，十二周造出一台能跑俄罗斯方块的完整计算机。每个项目规模恰到好处，零先修要求。学完后，「计算机是黑箱」这件事将永远从你的世界里消失。",
                         tags=["40h", "零基础", "推荐"],
                         links=[("Coursera 课程页", "https://www.coursera.org/learn/build-a-computer")]),
                    dict(slug="cs61c", lang="C / RISC-V 汇编", diff=4, hours=120, s="UC Berkeley", c="CS61C", t="Great Ideas in Computer Architecture",
                         u="https://cs61c.org/",
                         intro="RISC-V 发源地的正统课：手写汇编构造神经网络，从零搭 CPU。",
                         review="在 RISC-V 的发源地学习体系结构：C、汇编、缓存、流水线、并行，期末用 Logisim 从零搭一颗能跑程序的 CPU。项目强度大，但做完是真正的脱胎换骨。",
                         tags=["C/RISC-V", "120h"], links=[]),
                    dict(slug="mit-6004", lang="Verilog / 汇编", diff=4, hours=100, s="MIT", c="6.004", t="Computation Structures",
                         u="https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/",
                         intro="把数字逻辑 → 体系结构串成一条线，Project 在仿真器中搭完整 CPU。",
                         review="MIT 版本的体系结构课：从晶体管讲到 32 位 RISC 处理器，再讲到操作系统接口。仿真器实验设计精良，讲义兼具深度与可读性。",
                         tags=["OCW"], links=[]),
                ],
            },
            {
                "id": "sysintro", "name": "系统入门", "why": "先建立对整个系统的鸟瞰图，再深入细分领域。",
                "options": [
                    dict(slug="cmu-15213", lang="C", diff=5, hours=150, prereq="C 语言、汇编与计算机组成基础", s="CMU", c="15-213", t="CSAPP 深入理解计算机系统",
                         u="https://csapp.cs.cmu.edu/",
                         intro="CMU 镇系神课。Data/Bomb/Attack/Malloc Lab 是自学者的试金石，教材中译版《深入理解计算机系统》。",
                         review="如果整个目录只能选一门课，很多人会选它。Bomb Lab、Attack Lab、Malloc Lab 每个都是精心设计的关卡游戏，逼你真正理解机器级表示、内存层次与链接装载。教材 CSAPP 中译本是国内 CS 学生的共同圣经。学完它，「系统」二字对你不再神秘。",
                         tags=["C", "150h", "推荐"],
                         links=[("课程录像（B 站中字）", "https://www.bilibili.com/video/BV1iW411d7hd/")]),
                    dict(slug="mit-6033", lang="无代码（概念）", diff=3, hours=60, s="MIT", c="6.033", t="System Engineering",
                         u="https://ocw.mit.edu/courses/6-033-computer-system-engineering-spring-2018/",
                         intro="操作系统、网络、分布式与安全的概念全景，配套教材写得极好。",
                         review="不谈实现细节，专讲系统设计的基本原则：模块化、命名、容错、一致性。教材《Principles of Computer System Design》免费开放，是系统设计的思想内功。",
                         tags=["概念"],
                         links=[("配套教材（开放获取）", "https://ocw.mit.edu/resources/res-6-001-principles-of-computer-system-design-an-introduction-spring-2009/")]),
                    dict(slug="cs110", lang="C", diff=4, hours=100, prereq="系统编程基础", s="Stanford", c="CS110", t="Principles of Computer Systems",
                         u="https://web.stanford.edu/class/cs110/",
                         intro="大型系统的设计与权衡、跨机器软件与并行计算，作业配完整测试框架。",
                         review="斯坦福的系统原理课：进程、线程、并发、网络编程一网打尽，作业是大型的真实系统组件（如多线程代理服务器）。难度与收获成正比。",
                         tags=["进阶"], links=[]),
                ],
            },
            {
                "id": "os", "name": "操作系统", "why": "没有什么能比自己写个内核更能加深对 OS 的理解。",
                "options": [
                    dict(slug="mit-6s081", lang="C / RISC-V 汇编", diff=5, hours=150, prereq="C 语言、操作系统概念", s="MIT", c="6.1810", t="Operating System Engineering（原 6.S081）",
                         u="https://pdos.csail.mit.edu/6.1810/",
                         intro="PDOS 实验室出品：在优雅的 xv6 上累加 11 个 Lab 的功能模块。",
                         review="近年最火的 OS 课：在只有一万行的教学内核 xv6 上，亲手实现系统调用、页表、中断、锁、文件系统、mmap。11 个 Lab 难度曲线设计极佳， Frans Kaashoek 与 Robert Morris（Unix 传奇）亲自授课。自学者口碑爆棚。",
                         tags=["C/RISC-V", "150h", "推荐"], links=[]),
                    dict(slug="jyy-os", lang="C", diff=5, hours=100, s="南京大学", c="蒋炎岩 OS", t="操作系统：设计与实现",
                         u="https://jyywiki.cn/OS/2024/",
                         intro="全程中文，独到系统视角 + 丰富代码示例，对国内自学者极其友好。",
                         review="蒋炎岩老师的课是国内 OS 教学的一面旗帜：从「状态机」的独特视角统一进程、并发与持久化，课堂上现场写代码演示。全程中文 + B 站录像，配合丰富的迷你实验，对国内自学者极其友好。",
                         tags=["中文", "推荐"],
                         links=[("B 站课程录像", "https://www.bilibili.com/video/BV1Cm4y1d7Ur/")]),
                    dict(slug="cs162", lang="C", diff=5, hours=180, prereq="操作系统概念、C 语言", s="UC Berkeley", c="CS162", t="Operating Systems（Pintos）",
                         u="https://cs162.org/",
                         intro="在万行教学 OS 上实现线程调度、系统调用、虚拟内存、文件系统。难度六星。",
                         review="伯克利的硬核 OS 课：在 Pintos 上组队实现线程调度、用户程序、虚拟内存与文件系统。体量远大于 xv6，难度六星——但完成后你对 OS 的理解将无人能撼动。",
                         tags=["★★★★★★"], links=[]),
                    dict(slug="hit-os", lang="C", diff=4, hours=80, s="哈工大", c="李治军 OS", t="基于 Linux 0.11 源码",
                         u="https://github.com/hoverwinter/HIT-OSLab",
                         intro="中文授课，站在学生视角把 OS 来龙去脉娓娓道来，配套实验楼在线实验。",
                         review="李治军老师基于 Linux 0.11 源码逐层讲解 OS 的启动、进程、内存与文件系统，中文授课、视角亲民。配套的 8 个实验直接改动真实内核代码，理论到实践的闭环完整。",
                         tags=["中文"],
                         links=[("实验楼在线实验环境", "https://www.lanqiao.cn/courses/115")]),
                ],
            },
            {
                "id": "net", "name": "计算机网络", "why": "没有什么能比自己写个 TCP/IP 协议栈更能加深理解。",
                "options": [
                    dict(slug="cs144", lang="C++", diff=5, hours=100, s="Stanford", c="CS144", t="Computer Network",
                         u="https://cs144.github.io/",
                         intro="8 个 Checkpoint 用 C++ 搭出整个 TCP/IP 协议栈，也是最好的现代 C++ 实践课。",
                         review="斯坦福的新版网络课：从字节流、TCP 收发器、IP 路由一路写到网络接口，最终组成一个能与真实互联网通信的协议栈。Lab 用现代 C++ 编写，测试框架完善。学完后 TCP 的三次握手对你不再是背诵题。",
                         tags=["C++", "100h", "推荐"], links=[]),
                    dict(slug="cs168", lang="无代码（理论）", diff=3, hours=40, s="UC Berkeley", c="CS168", t="网络理论向",
                         u="https://textbook.cs168.io/",
                         intro="只想在理论上了解网络，读这门课的配套教材即可。",
                         review="伯克利网络课的在线教材，采用「自底向上」的现代顺序（从应用层往下讲），数学化地讨论拥塞控制与路由。不想写协议栈、只想建立理论框架的话，读它就够了。",
                         tags=["理论"], links=[]),
                ],
            },
            {
                "id": "db", "name": "数据库系统", "why": "没有什么能比自己写个关系型数据库更能加深理解。",
                "options": [
                    dict(slug="cmu-15445", lang="C++", diff=5, hours=100, s="CMU", c="15-445", t="Introduction to Database Systems",
                         u="https://15445.courses.cs.cmu.edu/",
                         intro="Andy Pavlo 主讲。4 个 Project 为 bustub 实现缓冲池、B+ 树、查询执行与并发控制。",
                         review="数据库领域最著名的公开课：Andy Pavlo 讲课如脱口秀，四个 Project 在 CMU 的教学数据库 bustub 上实现缓冲池、B+ 树索引、查询执行器与并发控制。Gradescope 评分对自学者开放。数据库方向的必修课。",
                         tags=["C++", "100h", "推荐"], links=[]),
                    dict(slug="cs186", lang="Java", diff=4, hours=100, s="UC Berkeley", c="CS186", t="Introduction to Database Systems",
                         u="https://cs186berkeley.net/",
                         intro="Postgres 发源地的课：用 Java 实现支持 SQL 并发与故障恢复的数据库。",
                         review="PostgreSQL 诞生地的数据库课：RookieDB 项目用 Java 实现查询、并发控制与恢复。相比 15-445 节奏稍缓，notes 写作质量高。",
                         tags=["Java"], links=[]),
                ],
            },
            {
                "id": "compiler", "name": "编译原理", "why": "没有什么能比自己写个编译器更能加深理解。",
                "options": [
                    dict(slug="pku-compiler", lang="C++ / RISC-V", diff=4, hours=80, s="北京大学", c="编译实践", t="类 C 语言 → RISC-V 编译器",
                         u="https://pku-minic.github.io/online-doc/",
                         intro="循序渐进的在线文档带你实现一个真正的编译器，全部开源。",
                         review="北大为本科生打造的编译实践：从词法分析到寄存器分配，在线文档手把手带你把类 C 语言编译到 RISC-V 汇编。中文编写、全程开源——中文世界最好的编译器实践入口。",
                         tags=["中文", "推荐"], links=[]),
                    dict(slug="cs143", lang="C++", diff=4, hours=150, s="Stanford", c="CS143", t="Compilers",
                         u="https://web.stanford.edu/class/cs143/",
                         intro="为 COOL 语言实现编译器，理论按龙书顺序覆盖词法到代码优化。",
                         review="斯坦福的经典编译课：为教学语言 COOL 实现完整的词法、语法、语义分析与代码生成。理论覆盖与龙书同步，想要正统编译训练的选它。",
                         tags=["150h"],
                         links=[("Coursera 版本", "https://www.coursera.org/learn/compilers")]),
                ],
            },
            {
                "id": "parallel", "name": "并行与分布式", "why": "摩尔定律终结之后，算力来自并行与集群。",
                "options": [
                    dict(slug="cmu-15418", lang="C++ / CUDA", diff=5, hours=150, s="CMU / Stanford", c="15-418 / CS149", t="Parallel Computing",
                         u="https://gfxcourses.stanford.edu/cs149/fall21/",
                         intro="用 CUDA、MPI、OpenMP 写高性能并行程序，5 个作业层层递进。",
                         review="并行计算的旗舰课（CMU 与斯坦福同源）：从多线程、SIMD 到 CUDA 与 MPI，五个大作业让你真切体验「性能调优」这门手艺。想进 AI Infra 或高性能计算方向，这是必修课。",
                         tags=["C++", "150h"], links=[]),
                    dict(slug="mit-6824", lang="Go", diff=5, hours=120, s="MIT", c="6.5840", t="Distributed Systems（原 6.824）",
                         u="https://pdos.csail.mit.edu/6.824/",
                         intro="每周精读一篇经典论文；5 个 Lab 实现基于 Raft 的 KV-store，难度闻名遐迩。",
                         review="分布式系统的殿堂级课程：每周精读 MapReduce、GFS、Raft 等经典论文，五个 Lab 用 Go 从零实现基于 Raft 共识的容错 KV 存储。难度闻名遐迩，工业界认可度同样闻名遐迩。",
                         tags=["Go", "进阶"], links=[]),
                ],
            },
        ],
    },

    {
        "num": "104", "name": "硬件", "en": "HARDWARE & SIGNALS",
        "desc": "CS 教你与抽象打交道，EE 教你与物理打交道。从传感器收集数据、到信号处理、再到反馈控制，这条链路是机器人、自动驾驶与具身智能的地基，也是通用型 AI 人才的稀缺视野。",
        "goal": "做一个能「感知世界」的小装置：传感器 → 信号 → 反馈控制。",
        "prereq": "101 数学（微积分、线性代数）",
        "topics": [
            {
                "id": "circuits", "name": "电路基础", "why": "模拟世界的入口：从电阻网络到运算放大器。",
                "options": [
                    dict(slug="ee16ab", lang="Python / MATLAB", diff=3, hours=150, s="UC Berkeley", c="EE16A & EE16B", t="Designing Information Devices and Systems",
                         u="https://eecs16a.org/",
                         intro="伯克利 EE 大一入门：16A 从环境收集与分析数据，16B 引入反馈与控制。Lab 全部有远程在线版。",
                         review="伯克利重新设计的 EE 入门双子星：不讲枯燥的电路分析套路，而是从「设计信息设备」出发——16A 做成像与定位，16B 做自平衡小车式的控制。全部 Lab 有远程版本，对自学者极其友好。",
                         tags=["150h", "推荐"],
                         links=[("EE16B 课程网站", "https://eecs16b.org/")]),
                    dict(slug="mit-6002", lang="无代码（电路）", diff=3, hours=80, s="MIT", c="6.002", t="Circuits and Electronics",
                         u="https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/",
                         intro="KVL/KCL、运放、频率响应、半导体基础，OCW 完整录像。",
                         review="MIT 经典电路课：Anant Agarwal 的 lecture 激情四射，从 KVL/KCL 讲到运放与半导体。想要扎实的传统电路功底，选它。",
                         tags=["OCW"], links=[]),
                ],
            },
            {
                "id": "signals", "name": "信号与系统", "why": "傅里叶变换给你一个看待世界的全新视角。",
                "options": [
                    dict(slug="ee120", lang="Python", diff=4, hours=100, s="UC Berkeley", c="EE120", t="Signals and Systems",
                         u="https://inst.eecs.berkeley.edu/~ee120/fa19/",
                         intro="6 个超有趣的 Python 作业：手写 FFT 比拼 Numpy、从手指影像推断心率、给哈勃照片降噪。",
                         review="把「信号与系统」从数学苦役变成游乐场的一门课：手写 FFT、用手机视频测心率、给哈勃望远镜的照片降噪。六个 Python 作业每个都让人上瘾。需要先修微积分与线代。",
                         tags=["Python", "100h", "推荐"], links=[]),
                    dict(slug="mit-6003", lang="Python / 数学", diff=4, hours=90, s="MIT", c="6.003", t="Signals and Systems",
                         u="https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/",
                         intro="全部课程录影 + 书面作业及答案开放。",
                         review="MIT 版本的信号与系统：更偏理论框架，CT/DT 变换体系讲得严密完整。与 EE120 的实践风格互补，喜欢先立理论框架的人从这里开始。",
                         tags=["OCW"], links=[]),
                ],
            },
            {
                "id": "control", "name": "控制论", "why": "系统如何被反馈塑造——AI 智能体的理论前身。",
                "options": [
                    dict(slug="ee16b", lang="Python", diff=3, hours=70, s="UC Berkeley", c="EE16B", t="反馈与控制入门",
                         u="https://eecs16b.org/",
                         intro="控制论的第一课，与 EE16A 衔接。",
                         review="从状态空间模型讲到可控性、稳定性与反馈控制，最后亲手让一个小车立起来走直线。作为控制论的第一课，它的坡度设计得恰到好处。",
                         tags=["入门"], links=[]),
                    dict(slug="ee263", lang="MATLAB / 数学", diff=4, hours=90, s="Stanford", c="EE263", t="Introduction to Linear Dynamical Systems",
                         u="https://web.stanford.edu/class/ee263/",
                         intro="状态空间、稳定性、可控可观性——走向机器人与自动驾驶的必修。",
                         review="斯坦福的线性动力系统课：把线性代数作为语言，系统讲透状态空间、最小二乘、稳定性与估计（Kalman 滤波的门槛）。讲义免费公开，机器人与自动驾驶方向的标配内功。",
                         tags=["进阶"],
                         links=[("课程讲义 PDF", "https://stanford.edu/~boyd/ee263/")]),
                ],
            },
        ],
    },

    {
        "num": "105", "name": "安全", "en": "SECURITY",
        "desc": "多少人当年是因为一个中二的黑客梦选择了计算机。成为黑客道阻且长：先学理论，再在 CTF 与靶场里融会贯通。",
        "goal": "打一次 CTF 比赛，或完成 SEED Labs 的全部实验。",
        "prereq": "103 系统（汇编、操作系统、网络基础）",
        "topics": [
            {
                "id": "sectheory", "name": "安全理论", "why": "内存安全、密码学、Web 与网络安全的设计原则。",
                "options": [
                    dict(slug="cs161", lang="C / Go", diff=4, hours=150, s="UC Berkeley", c="CS161", t="Computer Security",
                         u="https://cs161.org/",
                         intro="栈攻击、密码学、Web 安全、网络安全五大模块；Project 用 Go 实现安全文件分享系统。",
                         review="伯克利安全课：内存攻击、密码学、Web 安全、网络安全五块版图全覆盖，教材式的讲义全公开。三个 Project 实战性强——包括用 Go 实现一个端到端安全的文件分享系统。先修 CS61C 级别的系统知识。",
                         tags=["C/Go", "150h", "推荐"],
                         links=[("配套讲义 textbook", "https://textbook.cs161.org/")]),
                    dict(slug="seed-labs", lang="C / Python", diff=3, hours=80, s="雪城大学", c="SEED Labs", t="网络安全动手实验体系",
                         u="https://seedsecuritylabs.org/",
                         intro="NSF 资助，全球 1050 家机构使用：40+ 实验覆盖软件/网络/Web/系统安全，开箱即用的攻防环境。",
                         review="杜文亮教授 20 年打磨的实验体系：40 多个实验从缓冲区溢出到 DNS 投毒，全部提供预配置的虚拟机环境，下载即做。不想听课只想动手？这里是天堂。",
                         tags=["实践", "推荐"], links=[]),
                ],
            },
            {
                "id": "ctf", "name": "CTF 实战", "why": "夺旗赛——把各领域的知识融会贯通地考出来。",
                "options": [
                    dict(slug="pwn-college", lang="汇编 / C", diff=5, hours=120, s="pwn.college", c="Dojo", t="系统安全教学平台",
                         u="https://pwn.college/",
                         intro="亚利桑那州立大学的安全教学道场，从入门到 pwn 的完整关卡。",
                         review="ASU 把整套系统安全课程做成了闯关游戏：从 Linux 基础一路打到二进制利用（pwn），每个关卡都有配套讲解视频。关卡制 + 排行榜的反馈循环，学起来像打游戏。",
                         tags=["免费", "关卡制"], links=[]),
                    dict(slug="ctf-wiki", lang="无代码（速查）", diff=3, hours=20, s="CTF Wiki", c="中文知识库", t="CTF 竞赛百科",
                         u="https://ctf-wiki.org/",
                         intro="中文世界最完整的 CTF 知识库：Crypto、Web、Pwn、Reverse 全覆盖。",
                         review="中文 CTF 社区的集体智慧结晶：五大方向的知识体系、历年真题解析、工具清单。它更适合作为案头参考而非教材——遇到不会的赛题类型，先查这里。",
                         tags=["中文", "速查"], links=[]),
                    dict(slug="hacker101", lang="Web / JS", diff=2, hours=30, s="Hacker101", c="Web 安全入门", t="HackerOne 官方教程",
                         u="https://www.hacker101.com/",
                         intro="面向 Web 漏洞赏金的免费课程，配 CTF 靶场练手。",
                         review="漏洞赏金平台 HackerOne 的官方教程：视频课 + 配套靶场，学完直接在真实平台上挖洞赚赏金。Web 安全方向最短的上手路径。",
                         tags=["Web"], links=[]),
                ],
            },
        ],
    },
]

STAGES += [
    {
        "num": "106", "name": "智能", "en": "AI & DATA",
        "desc": "不满足于听媒体报道 AI 的进展，就亲手一探究竟。路径：AI 导论 → 机器学习 → 深度学习 → 按兴趣选 CV / NLP / RL / 系统。数学功底决定你能走多远。",
        "goal": "从零训练并部署一个小模型：微调一个 LLM，或实现 Needle 类自动微分库。",
        "prereq": "101 数学（线性代数和概率）+ 102 编程（Python）",
        "topics": [
            {
                "id": "aiintro", "name": "人工智能导论", "why": "搜索、博弈、强化学习、贝叶斯——AI 的经典版图。",
                "options": [
                    dict(slug="cs50-ai", lang="Python", diff=3, hours=60, s="Harvard", c="CS50 AI", t="Introduction to AI with Python",
                         u="https://cs50.harvard.edu/ai/",
                         intro="短小精悍的入门课，配丰富有趣的 Python 练习。",
                         review="CS50 家族的 AI 分支：七周覆盖搜索、知识、优化、学习、神经网络与 NLP，每周一个有趣的小项目（扫雷 AI、填字游戏、交通标志识别）。想快速建立 AI 全景，这是最轻快的一扇门。",
                         tags=["零基础"], links=[]),
                    dict(slug="cs188", lang="Python", diff=4, hours=100, s="UC Berkeley", c="CS188", t="Introduction to Artificial Intelligence",
                         u="https://ai.berkeley.edu/",
                         intro="本科生难度的系统课：Project 用 AI 算法玩吃豆人，notes 质量极高。",
                         review="伯克利 AI 导论：搜索、博弈、MDP、强化学习、贝叶斯网络的经典版图，Project 全部围绕吃豆人展开——让 AI 吃豆、躲鬼、学策略。讲义质量极高，是「经典 AI」体系的最佳入口。",
                         tags=["Python", "推荐"], links=[]),
                ],
            },
            {
                "id": "ml", "name": "机器学习", "why": "先建立宏观直觉，再深入数学原理。",
                "options": [
                    dict(slug="ng-ml", lang="Python", diff=2, hours=60, s="Stanford / Coursera", c="Machine Learning", t="吴恩达机器学习",
                         u="https://www.coursera.org/specializations/machine-learning-introduction",
                         intro="无人不晓的入门神课，作业保姆级框架，快速建立全景。",
                         review="全球数百万人学习 ML 的第一课。新版（2022 专项）用 Python 重写了全部作业，门槛极低、反馈极好。它的定位是「全景地图」：快速建立直觉，数学推导留给后面的课。",
                         tags=["Python", "推荐"], links=[]),
                    dict(slug="cs229", lang="Python / 数学", diff=5, hours=120, prereq="线性代数、概率统计、微积分", s="Stanford", c="CS229", t="Machine Learning（数学向）",
                         u="https://cs229.stanford.edu/",
                         intro="同样是吴恩达，但研究生难度：notes 写得极其专业，给不满足于调包的人。",
                         review="CS229 是吴恩达在斯坦福校园里的原版课：从最大似然到 EM、从核方法到 VC 维，数学严谨。notes 被公认为 ML 理论的最佳自学材料之一。线代与概率的功底在这里接受检验。",
                         tags=["进阶"], links=[]),
                    dict(slug="cs189", lang="Python / 数学", diff=4, hours=100, s="UC Berkeley", c="CS189", t="Introduction to Machine Learning",
                         u="https://eecs189.org/",
                         intro="伯克利版本的数学向机器学习。",
                         review="伯克利版本的数学向 ML：从优化视角统一回归、分类、神经网络与核方法，讲义由浅入深。与 CS229 风格略异，可按口味二选一。",
                         tags=["进阶"], links=[]),
                ],
            },
            {
                "id": "dl", "name": "深度学习", "why": "神经网络是近十年最重要的技术浪潮。",
                "options": [
                    dict(slug="cmu-11785", lang="Python / PyTorch", diff=5, hours=120, s="CMU", c="11-785", t="Introduction to Deep Learning",
                         u="https://deeplearning.cs.cmu.edu/",
                         intro="风格扎实、内容不水：从神经网络基础到 Transformer，作业真正锻炼训练与调参能力。",
                         review="CMU 的深度学习旗舰：从 MLP 手写到 CNN/RNN/Attention/Transformer，作业要求从零实现关键组件并在真实任务上调参。想获得「工业级炼丹能力」，这门课的强度刚刚好。",
                         tags=["120h", "推荐"], links=[]),
                    dict(slug="lihongyi-ml", lang="Python", diff=3, hours=80, s="台大", c="李宏毅 ML", t="机器学习（实为深度学习大全）",
                         u="https://speech.ee.ntu.edu.tw/~hylee/",
                         intro="中文授课，覆盖 DL 几乎所有方向，老师金句频出，适合宏观了解全领域。",
                         review="中文世界最受欢迎的 DL 课：李宏毅老师用动漫梗讲 Transformer，每年随领域更新（LLM、Diffusion 全覆盖）。适合作为宏观地图反复回看；作业配 Kaggle 式评测。",
                         tags=["中文", "推荐"],
                         links=[("B 站搬运合集", "https://www.bilibili.com/video/BV1Wv411h7kN/")]),
                    dict(slug="ng-dl", lang="Python / TensorFlow", diff=3, hours=80, s="Coursera", c="Deep Learning", t="吴恩达深度学习专项",
                         u="https://www.coursera.org/specializations/deep-learning",
                         intro="Coursera 满分专项，快速入门首选。",
                         review="五门小课组成的深度学习专项：从网络基础到 CNN 与序列模型，作业保姆级。强度低于 CMU 11-785，适合想在一个月内快速上岗的人。",
                         tags=["入门"], links=[]),
                    dict(slug="mit-67960", lang="Python / PyTorch", diff=5, hours=120, s="MIT", c="6.7960", t="Deep Learning",
                         u="https://phillipi.github.io/6.7960/",
                         intro="覆盖面广：LLM 主线之外兼顾 CV，作业对自学者友好。",
                         review="MIT 的新版深度学习课：以 LLM 为主线但不偏废 CV 与生成模型，作业设计对自学者友好（公开 notebook）。Phillip Isola 的讲授兼具直觉与严谨。",
                         tags=["进阶"], links=[]),
                    dict(slug="nyu-dl", lang="Python / PyTorch", diff=5, hours=100, s="NYU", c="DLSP21", t="Deep Learning（Yann LeCun）",
                         u="https://atcold.github.io/NYU-DLSP21/",
                         intro="图灵奖得主亲自授课的公开课，机会难得。",
                         review="Yann LeCun 亲自授课的 NYU 深度学习课：能量视角的统一框架、自监督学习的哲学——这是别处听不到的「祖师爷视角」。材料全开放，含配套练习。",
                         tags=["大师课"], links=[]),
                ],
            },
            {
                "id": "cvnlp", "name": "CV / NLP / RL（按兴趣选）", "why": "深度学习的三大应用分支。",
                "options": [
                    dict(slug="cs231n", lang="Python / PyTorch", diff=4, hours=100, s="Stanford", c="CS231n", t="CNN for Visual Recognition",
                         u="https://cs231n.stanford.edu/",
                         intro="CV 入门首选：3 个作业从零实现全连接网络到 CNN。",
                         review="计算机视觉的国民级课程：三个作业让你从零写出全连接网络、CNN 与图像应用。虽然如今视觉已进入 ViT 时代，但这里打的工程与直觉底子依然无可替代。",
                         tags=["CV"], links=[]),
                    dict(slug="cs224n", lang="Python / PyTorch", diff=4, hours=100, s="Stanford", c="CS224n", t="Natural Language Processing",
                         u="https://web.stanford.edu/class/cs224n/",
                         intro="NLP 经典课，从词向量到 Transformer。",
                         review="NLP 的国民级课程：从词向量一路讲到 Transformer 与预训练模型。想理解 LLM 的技术脉络，这是最正的一门课。作业用 PyTorch 从零实现核心组件。",
                         tags=["NLP"], links=[]),
                    dict(slug="cs285", lang="Python / PyTorch", diff=5, hours=120, s="UC Berkeley", c="CS285", t="Deep Reinforcement Learning",
                         u="https://rail.eecs.berkeley.edu/deeprlcourse/",
                         intro="深度强化学习的系统课程。",
                         review="Sergey Levine 主讲的深度强化学习系统课：从策略梯度、Q 学习到基于模型的 RL 与离线 RL。RL 是 LLM 对齐（RLHF）的底座，这门课的理论密度值得一啃。",
                         tags=["RL"], links=[]),
                ],
            },
            {
                "id": "datasci", "name": "数据科学", "why": "从海量数据中提取结果、预测行为。",
                "options": [
                    dict(slug="data100", lang="Python / SQL", diff=3, hours=80, s="UC Berkeley", c="Data100", t="Principles and Techniques of Data Science",
                         u="https://ds100.org/",
                         intro="丰富编程练习中掌握数据分析工具与算法。",
                         review="伯克利数据科学课：pandas、SQL、可视化、统计推断到机器学习入门，一条线串起数据分析全流程。练习密度高，教材开源。想拿数据当技能而非专业的人，从这里开始。",
                         tags=["Python", "推荐"],
                         links=[("开源教材 Learning Data Science", "https://learningds.org/")]),
                    dict(slug="cs246", lang="Python / C++", diff=4, hours=80, s="Stanford", c="CS246", t="Mining Massive Data Sets",
                         u="https://web.stanford.edu/class/cs246/",
                         intro="工业级大数据挖掘技术的进阶课。",
                         review="基于 Jure Leskovec 那本著名的免费教材：MapReduce/Spark、频繁项集、推荐系统、图挖掘。是「数据工程与挖掘」方向的正统进阶课。",
                         tags=["进阶"],
                         links=[("配套教材（免费）", "https://www.mmds.org/")]),
                ],
            },
            {
                "id": "dlsys", "name": "深度学习系统", "why": "模型越来越大，底层系统优化越来越值钱。",
                "options": [
                    dict(slug="cmu-10414", lang="Python / C++", diff=5, hours=150, s="CMU", c="10-414/714", t="Deep Learning Systems",
                         u="https://dlsyscourse.org/",
                         intro="从自动微分原理到 GPU 加速：5 个作业从零实现深度学习库 Needle。拒绝当调包侠。",
                         review="这门课让你亲手造一个 PyTorch：五个作业从零实现自动微分框架 Needle——计算图、反向传播、卷积加速、GPU 后端。完成后，你对深度学习的理解将从「调用者」跃升为「建造者」。AI Infra 方向的头牌课。",
                         tags=["Python/C++", "推荐"], links=[]),
                    dict(slug="mit-65940", lang="Python / PyTorch", diff=4, hours=80, s="MIT", c="6.5940", t="TinyML & Efficient Deep Learning",
                         u="https://hanlab.mit.edu/courses/2023-fall-65940",
                         intro="韩松主讲：剪枝、量化、蒸馏、NAS 与 LLM 系统优化，让模型跑在边缘设备上。",
                         review="韩松（MIT HAN Lab）的高效深度学习课：剪枝、量化、蒸馏、神经架构搜索，以及最新的 LLM 推理与训练系统优化。讲的全是工业界正在抢人的手艺。",
                         tags=["前沿"], links=[]),
                ],
            },
        ],
    },

    {
        "num": "107", "name": "创造", "en": "BUILD & CRAFT",
        "desc": "知识最终要变成作品。这一层没有固定路径：学会写高质量的工程代码，做出能给别人用的东西——一个网站、一个渲染器、一个开源项目。",
        "goal": "上线一个你自己的 Web 作品，或完成一个软光栅化渲染器。",
        "prereq": "102 编程（一门主语言）+ 103 系统（部分方向）",
        "topics": [
            {
                "id": "sweng", "name": "软件工程", "why": "「能跑」的代码和工业级代码有本质区别。",
                "options": [
                    dict(slug="mit-6031", lang="Java", diff=3, hours=80, s="MIT", c="6.031（原 6.005）", t="Software Construction",
                         u="https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/",
                         intro="如何写不易出 bug、简明易懂、易于维护的代码——强烈建议低年级就学。",
                         review="软件构建的方法论课：测试先行、规约、抽象数据类型、并发安全。它教的不是语言特性，而是让代码「经得起时间」的思维习惯。讲义质量极高，强烈建议早学。",
                         tags=["Java", "推荐"], links=[]),
                    dict(slug="cs169", lang="Ruby / JS", diff=3, hours=80, s="UC Berkeley", c="CS169", t="Software Engineering（Agile + SaaS）",
                         u="https://www.saasbook.info/",
                         intro="小团队敏捷开发与云服务模式，配套教材免费在线。",
                         review="敏捷开发与 SaaS 的实战课：用户故事、TDD/BDD、持续集成、部署上云。配套教材《Engineering Software as a Service》免费在线，适合组队实践。",
                         tags=["进阶"], links=[]),
                ],
            },
            {
                "id": "web", "name": "Web 开发", "why": "搭个人主页、给项目做展示、成为独立开发者。",
                "options": [
                    dict(slug="mit-weblab", lang="JS / Node", diff=2, hours=40, s="MIT", c="Web Lab", t="Web 开发两周速成",
                         u="https://webdev.mit.edu/",
                         intro="IAP 短课，快速掌握前后端全栈开发。",
                         review="MIT 一月短学期的全栈速成：HTML/CSS/JS、React、Node、MongoDB 两周打通，最终交一个完整网站。想快速获得「能做出东西」的手感，这门课的节奏很爽。",
                         tags=["速成"], links=[]),
                    dict(slug="cs142", lang="JS / React / Node", diff=3, hours=100, s="Stanford", c="CS142", t="Web Applications",
                         u="https://web.stanford.edu/class/cs142/",
                         intro="想系统学习 Web 应用的正经选择。",
                         review="斯坦福的 Web 应用课：前后端架构、React、Node、数据库与安全的系统讲授。比速成课扎实，适合想把 Web 作为主战场的人。",
                         tags=["系统"], links=[]),
                    dict(slug="fullstackopen", lang="JS / TypeScript", diff=3, hours=150, s="赫尔辛基大学", c="Full Stack Open", t="现代全栈开发",
                         u="https://fullstackopen.com/zh/",
                         intro="React + Node 的免费开源课程，有官方中文版。",
                         review="赫尔辛基大学出品、全球口碑极佳的全栈课：React、Redux、Node、Express、MongoDB、GraphQL、TypeScript 一条龙，每章配循序渐进的练习。官方中文翻译，完全免费——这可能是世界上性价比最高的 Web 课。",
                         tags=["中文", "免费"], links=[]),
                ],
            },
            {
                "id": "graphics", "name": "计算机图形学", "why": "用代码创造视觉的世界。",
                "options": [
                    dict(slug="games101", lang="C++", diff=4, hours=100, s="GAMES", c="101", t="现代计算机图形学入门（闫令琪）",
                         u="https://sites.cs.ucsb.edu/~lingqi/teaching/games101.html",
                         intro="公认最好的图形学入门：7 次作业实现一个软光栅化渲染器，中文授课。",
                         review="闫令琪老师的 GAMES101 是中文技术课程的标杆：光栅化、几何、光线追踪、动画仿真四大块，七次 C++ 作业最终汇成一个软光栅化渲染器。B 站录像百万播放，口碑封神。",
                         tags=["中文", "C++", "推荐"],
                         links=[("B 站课程录像", "https://www.bilibili.com/video/BV1X7411F744/")]),
                    dict(slug="games103-202", lang="C++ / CUDA", diff=5, hours=120, s="GAMES", c="103 / 202", t="物理仿真 / 实时渲染（进阶）",
                         u="https://games-cn.org/",
                         intro="GAMES 系列的进阶课：基于物理的动画与高质量实时渲染。",
                         review="GAMES101 之后的进阶双雄：103 讲基于物理的动画与仿真（布料、流体、刚体），202 讲高质量实时渲染。图形学深入方向的正统路径。",
                         tags=["进阶"], links=[]),
                    dict(slug="cs148", lang="JS / WebGL", diff=3, hours=100, s="Stanford", c="CS148", t="Introduction to Computer Graphics",
                         u="https://web.stanford.edu/class/cs148/",
                         intro="斯坦福的图形学导论，英文路线之选。",
                         review="斯坦福的图形学导论：从成像原理到光栅化、光线追踪与动画。英文授课路线的稳健选择，作业在浏览器里完成（WebGL），环境零配置。",
                         tags=["英文"], links=[]),
                ],
            },
        ],
    },
]

# ============================================================
# 模板与生成
# ============================================================

ROOT = os.path.dirname(os.path.abspath(__file__))

def esc(s):
    return html.escape(str(s), quote=True)

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com" />\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n'
         '<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;900'
         '&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=IBM+Plex+Mono:wght@400;500'
         '&display=swap" rel="stylesheet" />')

NAV = [("manifesto.html", "宣言", ""), ("directions.html", "航向", "active"),
       ("path.html", "机制", ""), ("join.html", "入院", "nav-cta")]

def chrome(title, desc, depth, body, extra_head=""):
    """depth: ''=根目录, '../'=tech/, '../../'=tech/course/"""
    nav = "\n".join(
        '    <a href="%s%s"%s>%s</a>' % (depth, href, (' class="%s"' % cls) if cls else "", label)
        for href, label, cls in NAV)
    return """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>%s</title>
<meta name="description" content="%s" />
%s
<link rel="stylesheet" href="%sassets/css/style.css" />
%s
</head>
<body class="dimmer">

<canvas id="sky" aria-hidden="true"></canvas>
<div class="grain" aria-hidden="true"></div>

<header class="topbar">
  <a class="brand" href="%sindex.html">
    <svg class="brand-mark" viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="16" r="3.2" fill="currentColor"/>
      <ellipse cx="16" cy="16" rx="14" ry="5.4" fill="none" stroke="currentColor" stroke-width="1"/>
      <ellipse cx="16" cy="16" rx="14" ry="5.4" fill="none" stroke="currentColor" stroke-width="0.7" transform="rotate(56 16 16)"/>
    </svg>
    <span class="brand-word">星宙<em>AstroVerseDAO</em></span>
  </a>
  <nav class="topnav">
%s
  </nav>
</header>

%s

<footer class="footer">
  <span>星宙 AstroVerseDAO · 观星书院</span>
  <span class="footer-dim">开源 · 免费 · 面向每一位求知者 — MMXXVI</span>
</footer>

<script src="%sassets/js/main.js"></script>
</body>
</html>
""" % (esc(title), esc(desc), FONTS, depth, extra_head, depth, nav, body, depth)


def tags_html(tags):
    return "".join("<span>%s</span>" % esc(t) for t in tags)


def unique_courses():
    """按首次出现顺序返回 (stage, topic, option)；同一 slug 只取第一次出现的课程位。"""
    seen, out = set(), []
    for st in STAGES:
        for tp in st["topics"]:
            for op in tp["options"]:
                if op["slug"] not in seen:
                    seen.add(op["slug"])
                    out.append((st, tp, op))
    return out


def stars(diff):
    """diff 个实心星 + (5-diff) 个空心星。"""
    d = int(diff)
    d = 1 if d < 1 else (5 if d > 5 else d)
    return "★" * d + "☆" * (5 - d)


CN_NUM = ["壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌"]
FIRE_HEAD = '<style>body { --accent: var(--fire); }</style>'


# ---------- 总览页 ----------
def overview_page():
    cards = []
    for st in STAGES:
        n_topics = len(st["topics"])
        n_courses = sum(len(t["options"]) for t in st["topics"])
        first = st["desc"].split("。")[0] + "。"
        cards.append("""      <a class="tcard reveal" href="tech/{num}.html">
        <span class="tcard-num">TECH<br/>{num}</span>
        <span class="tcard-body">
          <h3>{name}<em>{en}</em></h3>
          <p>{first}</p>
          <span class="tcard-meta">{nt} 个主题 · {nc} 门可选课程</span>
        </span>
        <span class="tcard-go">→</span>
      </a>""".format(num=st["num"], name=esc(st["name"]), en=esc(st["en"]),
                     first=esc(first), nt=n_topics, nc=n_courses))
    pathline = " → ".join(
        "<b>{num}</b><span>{name}</span>".format(num=s["num"], name=esc(s["name"]))
        for s in STAGES)
    body = """<main>

  <section class="page-hero wrap">
    <p class="page-kicker reveal">第叁航向 · FIRE · 火</p>
    <h1 class="page-title reveal">科技</h1>
    <p class="page-lens reveal">火 · 工具与创造</p>
    <p class="page-why reveal"><strong>为什么学：</strong>科技是五大航向中唯一以工程为核心的方向，但它不是「程序员速成班」。目标是三件事：理解世界如何运转——从晶体管的物理到神经网络的学习；掌握创造的双手——不只是会用工具，而是能造出工具；为 AI 时代做好准备——扎实的数学与系统功底 + 硬件视野 + 前沿的 AI 能力。</p>
    <div class="page-pathline reveal">{pathline}</div>
  </section>

  <section class="wrap">
    <p class="sec-index">课程目录 · TECH 000 → 107</p>
    <p class="reveal" style="color:var(--dim);font-size:15px;max-width:680px;margin-bottom:30px">
      编排参考 <a href="https://csdiy.wiki/CS%E5%AD%A6%E4%B9%A0%E8%A7%84%E5%88%92/" target="_blank" rel="noopener" style="color:var(--green-bright);border-bottom:1px solid var(--line-strong)">北大 CSDIY《CS 学习规划》</a>，并按阶段重新组织：<strong style="color:var(--text)">每个阶段一个编号、一个词，点开阶段看主题，点开课程看评价与资源。</strong>除「启航」与「数学」外，阶段之间没有绝对次序——满足先修即可自由选择。每个主题从列出的学校里选一门跟到底。
    </p>
    <div class="tcard-grid">
{cards}
    </div>
  </section>

  <div class="wrap">
    <div class="tip-block reveal">
      <b>怎么走完这条路径</b>
      <ol>
        <li><strong>不要跳过 000 与 101。</strong> 工具是所有学习的杠杆，数学是 AI 的地基——EE 的翅膀也建立在数学之上。</li>
        <li><strong>103 与 104 可以并行。</strong> CS 主干（系统、网络）与 EE 主干（信号、控制）是两条互补的线。</li>
        <li><strong>每个主题选一门课学透，而不是全部收藏。</strong> 列表里的多校选项是给你「选」的，不是给你「囤」的。</li>
        <li><strong>每学一个理论，配一个实践。</strong> 学了信号与系统就写个音频滤波器，学了控制论就做一个自平衡小车。</li>
        <li><strong>用输出倒逼输入。</strong> 笔记、Project、复盘都发到 GitHub——你会学得更快。</li>
      </ol>
    </div>

    <section class="cross reveal" style="margin-top:50px">
      <p class="sec-index">航向联动</p>
      <div class="cross-list">
        <a href="politics.html" style="--c:#e3d9b8"><b>科技 × 政治</b>数字治理、平台权力</a>
        <a href="history.html" style="--c:#7fb069"><b>科技 × 历史</b>技术变革的社会后果</a>
        <a href="cosmos.html" style="--c:#7a9bb8"><b>科技 × 宇宙</b>航天工程、AI 的物理基础</a>
      </div>
    </section>

    <p class="manifesto-note reveal" style="margin-bottom:70px">课程信息与资源整理自公开免费资源，致谢北大 CSDIY 与所有开源课程的老师们。<strong>会写代码只是开始——看得懂世界，造得出工具，才是终点。</strong></p>
  </div>

  <nav class="cycle" aria-label="航向循环导航">
    <a href="economy.html" style="--c:#cfa85c">
      <span class="cyc-label">← 上一航向 · 土</span>
      <div class="cyc-name">经济 · 金钱与时间</div>
    </a>
    <a href="history.html" style="--c:#7fb069">
      <span class="cyc-label">下一航向 · 木 →</span>
      <div class="cyc-name">历史 · 记忆与智慧</div>
    </a>
  </nav>

</main>""".format(pathline=pathline, cards="\n".join(cards))
    return chrome(
        "科技 · 工具与创造 — 星宙 AstroVerseDAO",
        "科技航向：TECH 000–107 阶段化课程目录。编排参考北大 CSDIY，每门课附评价与资源链接，从零基础到深度学习系统。",
        "", body, FIRE_HEAD)


# ---------- 阶段页 ----------
def stage_page(idx, st):
    rail = "\n".join(
        '    <a class="rail-chip{on}" href="{num}.html"><b>{num}</b><span>{name}</span></a>'.format(
            on=" on" if s["num"] == st["num"] else "", num=s["num"], name=esc(s["name"]))
        for s in STAGES)

    topic_blocks = []
    for ti, tp in enumerate(st["topics"], 1):
        opts = []
        for op in tp["options"]:
            opts.append("""        <a class="opt" href="course/{slug}.html">
          <span class="opt-school">{school}</span>
          <h4>{code}<em>{title}</em></h4>
          <p class="opt-note">{intro}</p>
          <span class="opt-foot">
            <span class="opt-tags">{tags}</span>
            <span class="opt-go">查看评价 →</span>
          </span>
        </a>""".format(slug=op["slug"], school=esc(op["s"]), code=esc(op["c"]),
                        title=esc(op.get("t") or ""), intro=esc(op["intro"]),
                        tags=tags_html(op["tags"])))
        topic_blocks.append("""    <section class="stopic reveal">
      <div class="stopic-head">
        <span class="stopic-code">{code:02d}</span>
        <div class="stopic-title"><h2>{name}</h2><p class="stopic-why">{why}</p></div>
      </div>
      <div class="opts">
{opts}
      </div>
    </section>""".format(code=ti, name=esc(tp["name"]), why=esc(tp["why"]),
                         opts="\n".join(opts)))

    prev_s = STAGES[(idx - 1) % len(STAGES)]
    next_s = STAGES[(idx + 1) % len(STAGES)]
    body = """<main>
  <section class="page-hero wrap">
    <p class="crumb reveal"><a href="../tech.html">科技</a><i>/</i>TECH {num} {name}</p>
    <p class="page-kicker reveal">第叁航向 · FIRE · 火 — 第{cn}阶段</p>
    <h1 class="page-title reveal"><span class="tech-code">TECH {num}</span>{name}</h1>
    <p class="page-lens reveal">{en}</p>
    <p class="page-why reveal">{desc}</p>
    <div class="stage-goalbar reveal"><b>过关项目</b>{goal}</div>
  </section>

  <div class="stage-rail wrap reveal">
{rail}
  </div>

  <div class="stages-topics wrap">
{topics}
  </div>

  <nav class="cycle" aria-label="阶段循环导航">
    <a href="{pnum}.html" style="--c:var(--fire)"><span class="cyc-label">← 上一阶段 · TECH {pnum}</span><div class="cyc-name">{pname}</div></a>
    <a href="{nnum}.html" style="--c:var(--fire)"><span class="cyc-label">下一阶段 · TECH {nnum} →</span><div class="cyc-name">{nname}</div></a>
  </nav>
</main>""".format(
        num=st["num"], name=esc(st["name"]), cn=CN_NUM[idx], en=esc(st["en"]),
        desc=esc(st["desc"]), goal=esc(st["goal"]), rail=rail,
        topics="\n".join(topic_blocks),
        pnum=prev_s["num"], pname=esc(prev_s["name"]),
        nnum=next_s["num"], nname=esc(next_s["name"]))
    return chrome(
        "科技 · TECH %s %s — 星宙 AstroVerseDAO" % (st["num"], st["name"]),
        "TECH %s %s（%s）：%s" % (st["num"], st["name"], st["en"], st["desc"]),
        "../", body, FIRE_HEAD)


# ---------- 课程详情页 ----------
def course_page(st, tp, op):
    siblings = [o for o in tp["options"] if o["slug"] != op["slug"]]
    if siblings:
        sib_html = "\n".join(
            '      <li><a href="{slug}.html"><b>{school} · {code}</b><span>{intro}</span></a></li>'.format(
                slug=o["slug"], school=esc(o["s"]), code=esc(o["c"]), intro=esc(o["intro"]))
            for o in siblings)
    else:
        sib_html = ('      <li><a href="../{num}.html"><b>该主题暂无其他选择</b>'
                    '<span>回到 TECH {num} · {name} 看看其他主题的课程。</span></a></li>'.format(
                        num=st["num"], name=esc(st["name"])))

    links = [("课程官网 ↗", op["u"])] + list(op.get("links") or [])
    res_html = "\n".join(
        '      <li><a href="{url}" target="_blank" rel="noopener">{label}</a></li>'.format(
            url=esc(u), label=esc(label))
        for label, u in links)

    prereq = op.get("prereq") or st.get("prereq") or "无"
    cmeta = "\n".join([
        "      <div><b>所属大学</b>%s</div>" % esc(op["s"]),
        "      <div><b>先修要求</b>%s</div>" % esc(prereq),
        "      <div><b>编程语言</b>%s</div>" % esc(op.get("lang") or "无代码"),
        '      <div><b>课程难度</b><span class="stars">%s</span></div>' % stars(op.get("diff", 3)),
        "      <div><b>预计学时</b>%d 小时</div>" % int(op.get("hours") or 0),
    ])

    body = """<main>
  <section class="page-hero wrap">
    <p class="crumb reveal"><a href="../../tech.html">科技</a><i>/</i><a href="../{num}.html">TECH {num} {sname}</a><i>/</i>{title}</p>
    <p class="page-kicker reveal">{school} · {code}</p>
    <h1 class="page-title course-h reveal">{code}<em>{title}</em></h1>
    <div class="cmeta reveal">
{cmeta}
    </div>
  </section>

  <div class="wrap course-body">
    <section class="cpanel reveal">
      <p class="sec-index">课程简介</p>
      <p class="cpanel-text">{intro}</p>
    </section>
    <section class="cpanel reveal">
      <p class="sec-index">课程评价</p>
      <p class="cpanel-text">{review}</p>
    </section>
    <section class="cpanel reveal">
      <p class="sec-index">课程资源</p>
      <ul class="reslink-list">
{res}
      </ul>
    </section>
    <section class="cpanel reveal">
      <p class="sec-index">同一主题的其他选择</p>
      <ul class="sib-list">
{sib}
      </ul>
    </section>
    <p class="course-back reveal"><a href="../{num}.html">← 返回 TECH {num} {sname}</a></p>
  </div>
</main>""".format(
        num=st["num"], sname=esc(st["name"]), title=esc(op.get("t") or op["c"]),
        school=esc(op["s"]), code=esc(op["c"]), cmeta=cmeta,
        intro=esc(op["intro"]), review=esc(op["review"]),
        res=res_html, sib=sib_html)
    return chrome(
        "%s · %s · TECH %s %s — 星宙 AstroVerseDAO" % (
            op["c"], op.get("t") or tp["name"], st["num"], st["name"]),
        "TECH %s %s · %s · %s：%s" % (
            st["num"], st["name"], op["s"], op["c"], op["intro"]),
        "../../", body, FIRE_HEAD)


def write(rel, content):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", rel)


def main():
    write("tech.html", overview_page())
    for i, st in enumerate(STAGES):
        write("tech/%s.html" % st["num"], stage_page(i, st))
    for st, tp, op in unique_courses():
        write("tech/course/%s.html" % op["slug"], course_page(st, tp, op))
    total = 1 + len(STAGES) + len(unique_courses())
    print("done: %d pages (%d course pages)" % (total, len(unique_courses())))


if __name__ == "__main__":
    main()
