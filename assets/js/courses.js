/* ============================================================
   星宙 · 科技航向 —— 阶段化课程目录（TECH 000 → 107）
   编排参考：北大 CSDIY《CS 学习规划》
   结构：阶段（Stage）→ 主题（Topic）→ 多校可选课程（Options）
   ============================================================ */

(function () {
  'use strict';

  /* 每个 option：s=学校/出处 c=课号 t=课程名 n=一句话说明 u=链接 tag=元信息 */
  var STAGES = [
    {
      num: '000', name: '启航 · 工具箱', en: 'BOOTCAMP',
      desc: '磨刀不误砍柴工。在正式学任何一门课之前，先花两周把工具备齐：一台能命令行驱动的电脑、一个 GitHub 账号、一套提问与检索的方法论。这些在大学课表里没有学分，却是之后所有学习的杠杆。',
      goal: '用命令行脚本自动化一件日常琐事；建一个 GitHub 仓库管理你的全部学习笔记。',
      topics: [
        {
          id: 'panorama', name: '计算机全景图', why: '先见森林，再见树木。Computers are not magic!',
          options: [
            { s: 'Crash Course', c: 'Computer Science', t: '计算机科学速成课', u: 'https://www.youtube.com/playlist?list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo', n: '8 小时动画科普：从继电器到人工智能的全貌，零基础第一站。', tag: ['视频', '零基础', 'B站有中字'] },
            { s: 'Harvard', c: 'CS50x', t: 'This is CS50', u: 'https://cs50.harvard.edu/x/', n: '全球最知名的 CS 导论课，从 C 讲到 Web，Project 成就感拉满。', tag: ['100h', '零基础', '推荐'] }
          ]
        },
        {
          id: 'toolchain', name: '工具链一课', why: '大学里缺失、工作中天天用的那些工具。',
          options: [
            { s: 'MIT', c: 'Missing Semester', t: '计算机教育中缺失的一课', u: 'https://missing.csail.mit.edu/', n: 'Shell、Vim、Git、调试、自动化、安全——一门课补齐工具链。CSDIY 强烈推荐给小白。', tag: ['20h', '推荐', '有中文版'] },
            { s: '开源社区', c: '命令行的艺术', t: 'The Art of Command Line', u: 'https://github.com/jlevy/the-art-of-command-line', n: 'GitHub 十万 stars 的顶流教程，被译成十几种语言，值得反复通读。', tag: ['文档', '速查'] }
          ]
        },
        {
          id: 'ask', name: '学会提问与检索', why: '提问是开源社区的第一项生存技能。',
          options: [
            { s: 'Eric S. Raymond', c: '提问的智慧', t: 'How To Ask Questions The Smart Way', u: 'https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way', n: ' hacker 文化的提问圣经：如何用简洁的文字让别人瞬间理解你的处境与目的。', tag: ['文档', '必读'] },
            { s: '方法论', c: '自主排查', t: '文档 → 搜索 → 最小复现', u: 'https://missing.csail.mit.edu/', n: '遇到问题先查文档与报错，再搜索，最后才提问——这个周期本身就是最好的练习。', tag: ['习惯'] }
          ]
        },
        {
          id: 'git', name: 'Git 与 GitHub', why: '代码版本控制 + 全球最大开源社区。',
          options: [
            { s: '官方', c: 'Pro Git', t: 'Git 权威指南（免费电子书）', u: 'https://git-scm.com/book/zh/v2', n: '出自 Linux 之父之手的 Git 是必掌握的神器，前五章就够日常使用。', tag: ['书', '免费'] },
            { s: 'GitHub', c: 'Skills', t: '交互式官方教程', u: 'https://skills.github.com/', n: '在真实仓库里边做边学：提交、分支、PR、Actions。', tag: ['交互', '零基础'] }
          ]
        },
        {
          id: 'editor', name: '编辑器与排版', why: '写代码的地方，值得认真对待。',
          options: [
            { s: 'VS Code / Vim', c: '二选一再双修', t: '现代编辑器与上古神器', u: 'https://code.visualstudio.com/', n: 'VS Code 插件生态即开即用；Vim 学习曲线陡峭但终生受益（几乎所有 IDE 都有 Vim 插件）。', tag: ['工具'] },
            { s: 'LaTeX', c: 'lshort', t: '一份（不太）简短的 LaTeX 介绍', u: 'https://www.overleaf.com/learn', n: '论文与数学笔记的排版标准。配合 Overleaf 在线使用，零配置。', tag: ['排版', '免费'] }
          ]
        }
      ]
    },

    {
      num: '101', name: '数学地基', en: 'MATHEMATICS',
      desc: '学好微积分和线代，和写代码至少同等重要。数学不是考完就忘的考题，而是理解 AI、信号、控制乃至世界运行方式的语言。学本质，不背公式。',
      goal: '用 LaTeX 写一份数学笔记，把一个定理推导到底并配一张可视化图。',
      topics: [
        {
          id: 'calculus', name: '微积分', why: '变化率与累积——一切连续现象的母语。',
          options: [
            { s: 'MIT', c: '18.01SC / 18.02SC', t: '单变量与多变量微积分', u: 'https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/', n: 'OCW 完整开放，notes 浅显生动、直抓本质，不再疲于做题。', tag: ['OCW', '推荐'] },
            { s: '3Blue1Brown', c: '微积分的本质', t: 'Essence of Calculus', u: 'https://www.3blue1brown.com/topics/calculus', n: '用动画直抵微积分的几何直觉，配合 MIT 课程食用更佳。', tag: ['视频', '直觉'] }
          ]
        },
        {
          id: 'linalg', name: '线性代数', why: '矩阵、向量空间、特征分解——神经网络与数据科学的基础。',
          options: [
            { s: 'MIT', c: '18.06', t: 'Linear Algebra（Gilbert Strang）', u: 'https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/', n: '数学大牛 Strang 的经典课，教材已被清华采用。', tag: ['OCW', '推荐'] },
            { s: '3Blue1Brown', c: '线性代数的本质', t: 'Essence of Linear Algebra', u: 'https://www.3blue1brown.com/topics/linear-algebra', n: '把「矩阵即变换」刻进直觉，看完再看任何一门课都会轻松很多。', tag: ['视频', '直觉'] }
          ]
        },
        {
          id: 'prob', name: '离散数学与概率论', why: '算法推导与证明的工具，高阶课程的先修。',
          options: [
            { s: 'UC Berkeley', c: 'CS70', t: 'Discrete Math and Probability Theory', u: 'https://www.eecs70.org/', n: '每个模块都配算法实例：逻辑→稳定匹配、数论→RSA、概率→哈希与负载均衡。', tag: ['60h', '推荐'] },
            { s: 'MIT', c: '6.042J', t: 'Mathematics for Computer Science', u: 'https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/', n: '面向 CS 的离散数学，教材《Mathematics for CS》免费开源。', tag: ['OCW', '开源教材'] },
            { s: 'UC Berkeley', c: 'CS126', t: 'Probability Theory（进阶）', u: 'https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E8%BF%9B%E9%98%B6/CS126/', n: '随机过程与深入理论，大量 Python 作业让你用代码验证概率。', tag: ['进阶'] }
          ]
        },
        {
          id: 'info', name: '信息论入门', why: '编码、压缩、信息熵——AI 时代理解数据本质的核心。',
          options: [
            { s: 'MIT', c: '6.050J', t: 'Information Theory and Entropy', u: 'https://ocw.mit.edu/courses/6-050j-information-and-entropy-spring-2008/', n: '专为大一新生设计，几乎零先修：编码、压缩、通信、信息熵，非常有趣。', tag: ['零基础', '推荐'] }
          ]
        },
        {
          id: 'numerical', name: '数值分析（选修）', why: '用离散的计算机逼近连续的数学——计算思维。',
          options: [
            { s: 'MIT', c: 'Computational Thinking', t: '计算思维入门（Julia）', u: 'https://computationalthinking.mit.edu/', n: '全部开源：图像处理、社科数据、气候建模三个主题里体验计算与科学的结合。', tag: ['Julia', '零基础'] },
            { s: 'MIT', c: '18.330', t: 'Introduction to Numerical Analysis', u: 'https://github.com/mitmath/18330', n: '浮点编码、求根、线性系统、微分方程；配套开源教材与 Julia 实例。', tag: ['进阶'] }
          ]
        },
        {
          id: 'diffeq', name: '微分方程（选修）', why: '用方程刻画世间万物的运动，换一个视角看世界。',
          options: [
            { s: 'MIT', c: '18.03SC', t: 'Differential Equations', u: 'https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/', n: '常微分方程的求解与直觉，OCW 完整开放。', tag: ['OCW'] }
          ]
        },
        {
          id: 'mathadv', name: '数学高阶（按需自取）', why: '面向科研与高阶工程，兴趣驱动。',
          options: [
            { s: 'Stanford', c: 'EE364A', t: 'Convex Optimization 凸优化', u: 'https://web.stanford.edu/class/ee364a/', n: '机器学习的数学地基。Boyd 主讲，教材《Convex Optimization》免费开源。', tag: ['★★★★'] },
            { s: 'MIT', c: '18.650', t: 'Statistics for Applications 应用统计', u: 'https://ocw.mit.edu/courses/18-650-statistics-for-applications-fall-2016/', n: '面向应用的统计学研究生课，讲义完整开放。', tag: ['★★★★'] },
            { s: 'Stanford', c: 'CS255', t: 'Cryptography 密码学', u: 'https://www.coursera.org/learn/crypto', n: 'Dan Boneh 的密码学课，Coursera 版本免费开放。', tag: ['★★★★'] }
          ]
        }
      ]
    },

    {
      num: '102', name: '编程入门', en: 'FIRST LANGUAGES',
      desc: '语言是工具，没有完美的语言，只有合适的工具。选定一门主语言学透（推荐 Python 或 C），其余按需涉猎。本阶段每个主题都给出多所学校的选择——选一门跟到底，别全收藏。',
      goal: '完成 CS61A 或 CS50 的全部 Project，放进你的 GitHub。',
      topics: [
        {
          id: 'clang', name: 'C 语言', why: '离机器最近的高级语言，理解内存与指针的必修课。',
          options: [
            { s: 'Harvard', c: 'CS50x', t: 'This is CS50', u: 'https://cs50.harvard.edu/x/', n: '以 C 为主线的导论课：内存、指针、数据结构一次打穿，再平滑过渡到 Python。', tag: ['100h', '推荐'] },
            { s: '浙江大学', c: '翁恺 · C 语言程序设计', t: '中国大学 MOOC', u: 'https://www.icourse163.org/course/ZJU-9001', n: '中文世界最受欢迎的 C 入门课，讲解细致，配套 PTA 在线评测。', tag: ['中文', '零基础'] },
            { s: 'K&R', c: '《C 程序设计语言》', t: 'The C Programming Language', u: 'https://csdiy.wiki/%E5%A5%BD%E4%B9%A6%E6%8E%A8%E8%8D%90/', n: 'C 之父写的薄书，学完一门课后通读一遍，常有顿悟。', tag: ['书', '进阶'] }
          ]
        },
        {
          id: 'python', name: 'Python', why: 'AI 时代的第一语言，语法温和、生态无敌。',
          options: [
            { s: 'Harvard', c: 'CS50P', t: 'Introduction to Programming with Python', u: 'https://cs50.harvard.edu/python/', n: '10 周系统掌握 Python：函数、库、单测、正则、OOP。比 CS61A 温和。', tag: ['60h', '零基础'] },
            { s: 'UC Berkeley', c: 'CS61A', t: 'SICP（Python 版）', u: 'https://cs61a.org/', n: '不只是语言课：数据抽象、函数式、OOP，最后用 Python 写一个 Scheme 解释器。', tag: ['50h', '推荐'] },
            { s: 'MIT', c: '6.100L', t: 'Intro to CS and Programming using Python', u: 'https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/', n: 'MIT 官方 Python 入门，OCW 完整开放。', tag: ['OCW'] }
          ]
        },
        {
          id: 'cpp', name: 'C++', why: '系统课（CS144、15-445）与图形学的入场券。',
          options: [
            { s: 'Stanford', c: 'CS106B/X', t: 'Programming Abstractions', u: 'https://web.stanford.edu/class/cs106b/', n: '以 C++ 描述的抽象与数据结构入门，递归讲得极好。', tag: ['推荐'] },
            { s: 'Stanford', c: 'CS106L', t: 'Standard C++ Programming', u: 'https://web.stanford.edu/class/cs106l/', n: '现代 C++ 标准库速通：STL、流、模板，为系统课铺路。', tag: ['速通'] }
          ]
        },
        {
          id: 'java', name: 'Java', why: 'CS61B 与软件工程课的教学语言。',
          options: [
            { s: 'MIT', c: '6.092', t: 'Introduction to Programming in Java', u: 'https://ocw.mit.edu/courses/6-092-introduction-to-programming-in-java-january-iap-2010/', n: 'IAP 短课，快速掌握 Java 语法与 OOP 基础。', tag: ['短课'] }
          ]
        },
        {
          id: 'rust', name: 'Rust（选修）', why: '内存安全的新系统语言，未来基础设施的宠儿。',
          options: [
            { s: 'Stanford', c: 'CS110L', t: 'Safety in Systems Programming', u: 'https://web.stanford.edu/class/cs110l/', n: '用 Rust 重新思考系统编程中的安全性。', tag: ['进阶'] }
          ]
        },
        {
          id: 'ocaml', name: 'OCaml（选修）', why: '函数式编程的美学，编译器与形式化方向的入口。',
          options: [
            { s: 'Cornell', c: 'CS3110', t: 'OCaml Programming: Correct + Efficient + Beautiful', u: 'https://cs3110.github.io/textbook/cover.html', n: '教材完全开源，函数式思维会反过来改善你所有的代码。', tag: ['开源教材'] }
          ]
        }
      ]
    },

    {
      num: '103', name: '系统核心', en: 'SYSTEMS CORE',
      desc: '没有什么能比自己写个内核、写个 TCP 栈、写个数据库更能加深理解。这一层是 CS 的任督二脉：数据结构与算法 → 体系结构 → 操作系统 → 网络 → 数据库 → 编译器。每一门都配重实践。',
      goal: '迷你操作系统（xv6 扩展）/ 迷你 TCP 协议栈 / 迷你数据库，任选其一。',
      topics: [
        {
          id: 'dsa', name: '数据结构与算法', why: 'CS 的核心，几乎一切专业课的基础。',
          options: [
            { s: 'UC Berkeley', c: 'CS61B', t: 'Data Structures and Algorithms', u: 'https://sp24.datastructur.es/', n: '14 Lab 亲手实现数据结构，3 个上千行 Project（简易谷歌地图、二维 Minecraft），autograder 开源。', tag: ['Java', '60h', '推荐'] },
            { s: 'Princeton', c: 'Algorithms I & II', t: 'Coursera 算法专项', u: 'https://www.coursera.org/learn/algorithms-part1', n: 'Sedgewick 的经典课，深入浅出，配套 algs4 网站与评测。', tag: ['Java', 'Coursera'] },
            { s: 'MIT', c: '6.006', t: 'Introduction to Algorithms', u: 'https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/', n: '偏好 Python 的算法入门之选。', tag: ['Python', 'OCW'] },
            { s: 'Stanford', c: 'CS106B/X', t: 'Programming Abstractions', u: 'https://web.stanford.edu/class/cs106b/', n: '想走 C/C++ 路线的数据结构与基础算法课。', tag: ['C++'] },
            { s: 'UC Berkeley / MIT', c: 'CS170 / 6.046', t: '高阶算法与 NP（进阶）', u: 'https://cs170.org/', n: '算法设计与分析，以及 NP 问题的艺术。', tag: ['进阶'] }
          ]
        },
        {
          id: 'arch', name: '体系结构', why: '从与非门到 CPU——计算机的世界真是 01 构成的。',
          options: [
            { s: 'Nand2Tetris', c: 'I & II', t: '从零造一台计算机', u: 'https://www.nand2tetris.org/', n: 'Coursera 满分神课：逻辑门 → CPU → 编译器 → OS，最后在自己造的机器上跑俄罗斯方块。零门槛。', tag: ['40h', '零基础', '推荐'] },
            { s: 'UC Berkeley', c: 'CS61C', t: 'Great Ideas in Computer Architecture', u: 'https://cs61c.org/', n: 'RISC-V 发源地的正统课：手写汇编构造神经网络，从零搭 CPU。', tag: ['C/RISC-V', '120h'] },
            { s: 'MIT', c: '6.004', t: 'Computation Structures', u: 'https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/', n: '把数字逻辑 → 体系结构串成一条线，Project 在仿真器中搭完整 CPU。', tag: ['OCW'] }
          ]
        },
        {
          id: 'sysintro', name: '系统入门', why: '先建立对整个系统的鸟瞰图，再深入细分领域。',
          options: [
            { s: 'CMU', c: '15-213', t: 'CSAPP 深入理解计算机系统', u: 'https://csapp.cs.cmu.edu/', n: 'CMU 镇系神课。Data/Bomb/Attack/Malloc Lab 是自学者的试金石，教材中译版《深入理解计算机系统》。', tag: ['C', '150h', '推荐'] },
            { s: 'MIT', c: '6.033', t: 'System Engineering', u: 'https://ocw.mit.edu/courses/6-033-computer-system-engineering-spring-2018/', n: '操作系统、网络、分布式与安全的概念全景，配套教材写得极好。', tag: ['概念'] },
            { s: 'Stanford', c: 'CS110', t: 'Principles of Computer Systems', u: 'https://web.stanford.edu/class/cs110/', n: '大型系统的设计与权衡、跨机器软件与并行计算，作业配完整测试框架。', tag: ['进阶'] }
          ]
        },
        {
          id: 'os', name: '操作系统', why: '没有什么能比自己写个内核更能加深对 OS 的理解。',
          options: [
            { s: 'MIT', c: '6.1810', t: 'Operating System Engineering（原 6.S081）', u: 'https://pdos.csail.mit.edu/6.1810/', n: 'PDOS 实验室出品：在优雅的 xv6 上累加 11 个 Lab 的功能模块。', tag: ['C/RISC-V', '150h', '推荐'] },
            { s: '南京大学', c: '蒋炎岩 OS', t: '操作系统：设计与实现', u: 'https://jyywiki.cn/OS/2024/', n: '全程中文，独到系统视角 + 丰富代码示例，对国内自学者极其友好。', tag: ['中文', '推荐'] },
            { s: 'UC Berkeley', c: 'CS162', t: 'Operating Systems（Pintos）', u: 'https://cs162.org/', n: '在万行教学 OS 上实现线程调度、系统调用、虚拟内存、文件系统。难度六星。', tag: ['★★★★★★'] },
            { s: '哈工大', c: '李治军 OS', t: '基于 Linux 0.11 源码', u: 'https://github.com/hoverwinter/HIT-OSLab', n: '中文授课，站在学生视角把 OS 来龙去脉娓娓道来，配套实验楼在线实验。', tag: ['中文'] }
          ]
        },
        {
          id: 'net', name: '计算机网络', why: '没有什么能比自己写个 TCP/IP 协议栈更能加深理解。',
          options: [
            { s: 'Stanford', c: 'CS144', t: 'Computer Network', u: 'https://cs144.github.io/', n: '8 个 Checkpoint 用 C++ 搭出整个 TCP/IP 协议栈，也是最好的现代 C++ 实践课。', tag: ['C++', '100h', '推荐'] },
            { s: 'UC Berkeley', c: 'CS168', t: '网络理论向', u: 'https://textbook.cs168.io/', n: '只想在理论上了解网络，读这门课的配套教材即可。', tag: ['理论'] }
          ]
        },
        {
          id: 'db', name: '数据库系统', why: '没有什么能比自己写个关系型数据库更能加深理解。',
          options: [
            { s: 'CMU', c: '15-445', t: 'Introduction to Database Systems', u: 'https://15445.courses.cs.cmu.edu/', n: 'Andy Pavlo 主讲。4 个 Project 为 bustub 实现缓冲池、B+ 树、查询执行与并发控制。', tag: ['C++', '100h', '推荐'] },
            { s: 'UC Berkeley', c: 'CS186', t: 'Introduction to Database Systems', u: 'https://cs186berkeley.net/', n: 'Postgres 发源地的课：用 Java 实现支持 SQL 并发与故障恢复的数据库。', tag: ['Java'] }
          ]
        },
        {
          id: 'compiler', name: '编译原理', why: '没有什么能比自己写个编译器更能加深理解。',
          options: [
            { s: '北京大学', c: '编译实践', t: '类 C 语言 → RISC-V 编译器', u: 'https://pku-minic.github.io/online-doc/', n: '循序渐进的在线文档带你实现一个真正的编译器，全部开源。', tag: ['中文', '推荐'] },
            { s: 'Stanford', c: 'CS143', t: 'Compilers', u: 'https://web.stanford.edu/class/cs143/', n: '为 COOL 语言实现编译器，理论按龙书顺序覆盖词法到代码优化。', tag: ['150h'] }
          ]
        },
        {
          id: 'parallel', name: '并行与分布式', why: '摩尔定律终结之后，算力来自并行与集群。',
          options: [
            { s: 'CMU / Stanford', c: '15-418 / CS149', t: 'Parallel Computing', u: 'https://gfxcourses.stanford.edu/cs149/fall21/', n: '用 CUDA、MPI、OpenMP 写高性能并行程序，5 个作业层层递进。', tag: ['C++', '150h'] },
            { s: 'MIT', c: '6.5840', t: 'Distributed Systems（原 6.824）', u: 'https://pdos.csail.mit.edu/6.824/', n: '每周精读一篇经典论文；5 个 Lab 实现基于 Raft 的 KV-store，难度闻名遐迩。', tag: ['Go', '进阶'] }
          ]
        }
      ]
    },

    {
      num: '104', name: '硬件与物理世界', en: 'HARDWARE & SIGNALS',
      desc: 'CS 教你与抽象打交道，EE 教你与物理打交道。从传感器收集数据、到信号处理、再到反馈控制，这条链路是机器人、自动驾驶与具身智能的地基，也是通用型 AI 人才的稀缺视野。',
      goal: '做一个能「感知世界」的小装置：传感器 → 信号 → 反馈控制。',
      topics: [
        {
          id: 'circuits', name: '电路基础', why: '模拟世界的入口：从电阻网络到运算放大器。',
          options: [
            { s: 'UC Berkeley', c: 'EE16A & EE16B', t: 'Designing Information Devices and Systems', u: 'https://eecs16a.org/', n: '伯克利 EE 大一入门：16A 从环境收集与分析数据，16B 引入反馈与控制。Lab 全部有远程在线版。', tag: ['150h', '推荐'] },
            { s: 'MIT', c: '6.002', t: 'Circuits and Electronics', u: 'https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/', n: 'KVL/KCL、运放、频率响应、半导体基础，OCW 完整录像。', tag: ['OCW'] }
          ]
        },
        {
          id: 'signals', name: '信号与系统', why: '傅里叶变换给你一个看待世界的全新视角。',
          options: [
            { s: 'UC Berkeley', c: 'EE120', t: 'Signals and Systems', u: 'https://inst.eecs.berkeley.edu/~ee120/fa19/', n: '6 个超有趣的 Python 作业：手写 FFT 比拼 Numpy、从手指影像推断心率、给哈勃照片降噪。', tag: ['Python', '100h', '推荐'] },
            { s: 'MIT', c: '6.003', t: 'Signals and Systems', u: 'https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/', n: '全部课程录影 + 书面作业及答案开放。', tag: ['OCW'] }
          ]
        },
        {
          id: 'control', name: '控制论', why: '系统如何被反馈塑造——AI 智能体的理论前身。',
          options: [
            { s: 'UC Berkeley', c: 'EE16B', t: '反馈与控制入门', u: 'https://eecs16b.org/', n: '控制论的第一课，与 EE16A 衔接。', tag: ['入门'] },
            { s: 'Stanford', c: 'EE263', t: 'Introduction to Linear Dynamical Systems', u: 'https://web.stanford.edu/class/ee263/', n: '状态空间、稳定性、可控可观性——走向机器人与自动驾驶的必修。', tag: ['进阶'] }
          ]
        }
      ]
    },

    {
      num: '105', name: '安全', en: 'SECURITY',
      desc: '多少人当年是因为一个中二的黑客梦选择了计算机。成为黑客道阻且长：先学理论，再在 CTF 与靶场里融会贯通。',
      goal: '打一次 CTF 比赛，或完成 SEED Labs 的全部实验。',
      topics: [
        {
          id: 'sectheory', name: '安全理论', why: '内存安全、密码学、Web 与网络安全的设计原则。',
          options: [
            { s: 'UC Berkeley', c: 'CS161', t: 'Computer Security', u: 'https://cs161.org/', n: '栈攻击、密码学、Web 安全、网络安全五大模块；Project 用 Go 实现安全文件分享系统。', tag: ['C/Go', '150h', '推荐'] },
            { s: '雪城大学', c: 'SEED Labs', t: '网络安全动手实验体系', u: 'https://seedsecuritylabs.org/', n: 'NSF 资助，全球 1050 家机构使用：40+ 实验覆盖软件/网络/Web/系统安全，开箱即用的攻防环境。', tag: ['实践', '推荐'] }
          ]
        },
        {
          id: 'ctf', name: 'CTF 实战', why: '夺旗赛——把各领域的知识融会贯通地考出来。',
          options: [
            { s: 'pwn.college', c: 'Dojo', t: '系统安全教学平台', u: 'https://pwn.college/', n: '亚利桑那州立大学的安全教学道场，从入门到 pwn 的完整关卡。', tag: ['免费', '关卡制'] },
            { s: 'CTF Wiki', c: '中文知识库', t: 'CTF 竞赛百科', u: 'https://ctf-wiki.org/', n: '中文世界最完整的 CTF 知识库：Crypto、Web、Pwn、Reverse 全覆盖。', tag: ['中文', '速查'] },
            { s: 'Hacker101', c: 'Web 安全入门', t: 'HackerOne 官方教程', u: 'https://www.hacker101.com/', n: '面向 Web 漏洞赏金的免费课程，配 CTF 靶场练手。', tag: ['Web'] }
          ]
        }
      ]
    },

    {
      num: '106', name: '智能与数据', en: 'AI & DATA',
      desc: '不满足于听媒体报道 AI 的进展，就亲手一探究竟。路径：AI 导论 → 机器学习 → 深度学习 → 按兴趣选 CV / NLP / RL / 系统。数学功底决定你能走多远。',
      goal: '从零训练并部署一个小模型：微调一个 LLM，或实现 Needle 类自动微分库。',
      topics: [
        {
          id: 'aiintro', name: '人工智能导论', why: '搜索、博弈、强化学习、贝叶斯——AI 的经典版图。',
          options: [
            { s: 'Harvard', c: 'CS50 AI', t: 'Introduction to AI with Python', u: 'https://cs50.harvard.edu/ai/', n: '短小精悍的入门课，配丰富有趣的 Python 练习。', tag: ['零基础'] },
            { s: 'UC Berkeley', c: 'CS188', t: 'Introduction to Artificial Intelligence', u: 'https://ai.berkeley.edu/', n: '本科生难度的系统课：Project 用 AI 算法玩吃豆人，notes 质量极高。', tag: ['Python', '推荐'] }
          ]
        },
        {
          id: 'ml', name: '机器学习', why: '先建立宏观直觉，再深入数学原理。',
          options: [
            { s: 'Stanford / Coursera', c: 'Machine Learning', t: '吴恩达机器学习', u: 'https://www.coursera.org/specializations/machine-learning-introduction', n: '无人不晓的入门神课，作业保姆级框架，快速建立全景。', tag: ['Python', '推荐'] },
            { s: 'Stanford', c: 'CS229', t: 'Machine Learning（数学向）', u: 'https://cs229.stanford.edu/', n: '同样是吴恩达，但研究生难度：notes 写得极其专业，给不满足于调包的人。', tag: ['进阶'] },
            { s: 'UC Berkeley', c: 'CS189', t: 'Introduction to Machine Learning', u: 'https://eecs189.org/', n: '伯克利版本的数学向机器学习。', tag: ['进阶'] }
          ]
        },
        {
          id: 'dl', name: '深度学习', why: '神经网络是近十年最重要的技术浪潮。',
          options: [
            { s: 'CMU', c: '11-785', t: 'Introduction to Deep Learning', u: 'https://deeplearning.cs.cmu.edu/', n: '风格扎实、内容不水：从神经网络基础到 Transformer，作业真正锻炼训练与调参能力。', tag: ['120h', '推荐'] },
            { s: '台大', c: '李宏毅 ML', t: '机器学习（实为深度学习大全）', u: 'https://speech.ee.ntu.edu.tw/~hylee/', n: '中文授课，覆盖 DL 几乎所有方向，老师金句频出，适合宏观了解全领域。', tag: ['中文', '推荐'] },
            { s: 'Coursera', c: 'Deep Learning', t: '吴恩达深度学习专项', u: 'https://www.coursera.org/specializations/deep-learning', n: 'Coursera 满分专项，快速入门首选。', tag: ['入门'] },
            { s: 'MIT', c: '6.7960', t: 'Deep Learning', u: 'https://phillipi.github.io/6.7960/', n: '覆盖面广：LLM 主线之外兼顾 CV，作业对自学者友好。', tag: ['进阶'] },
            { s: 'NYU', c: 'DLSP21', t: 'Deep Learning（Yann LeCun）', u: 'https://atcold.github.io/NYU-DLSP21/', n: '图灵奖得主亲自授课的公开课，机会难得。', tag: ['大师课'] }
          ]
        },
        {
          id: 'cvnlp', name: 'CV / NLP / RL（按兴趣选）', why: '深度学习的三大应用分支。',
          options: [
            { s: 'Stanford', c: 'CS231n', t: 'CNN for Visual Recognition', u: 'https://cs231n.stanford.edu/', n: 'CV 入门首选：3 个作业从零实现全连接网络到 CNN。', tag: ['CV'] },
            { s: 'Stanford', c: 'CS224n', t: 'Natural Language Processing', u: 'https://web.stanford.edu/class/cs224n/', n: 'NLP 经典课，从词向量到 Transformer。', tag: ['NLP'] },
            { s: 'UC Berkeley', c: 'CS285', t: 'Deep Reinforcement Learning', u: 'https://rail.eecs.berkeley.edu/deeprlcourse/', n: '深度强化学习的系统课程。', tag: ['RL'] }
          ]
        },
        {
          id: 'datasci', name: '数据科学', why: '从海量数据中提取结果、预测行为。',
          options: [
            { s: 'UC Berkeley', c: 'Data100', t: 'Principles and Techniques of Data Science', u: 'https://ds100.org/', n: '丰富编程练习中掌握数据分析工具与算法。', tag: ['Python', '推荐'] },
            { s: 'Stanford', c: 'CS246', t: 'Mining Massive Data Sets', u: 'https://web.stanford.edu/class/cs246/', n: '工业级大数据挖掘技术的进阶课。', tag: ['进阶'] }
          ]
        },
        {
          id: 'dlsys', name: '深度学习系统', why: '模型越来越大，底层系统优化越来越值钱。',
          options: [
            { s: 'CMU', c: '10-414/714', t: 'Deep Learning Systems', u: 'https://dlsyscourse.org/', n: '从自动微分原理到 GPU 加速：5 个作业从零实现深度学习库 Needle。拒绝当调包侠。', tag: ['Python/C++', '推荐'] },
            { s: 'MIT', c: '6.5940', t: 'TinyML & Efficient Deep Learning', u: 'https://hanlab.mit.edu/courses/2023-fall-65940', n: '韩松主讲：剪枝、量化、蒸馏、NAS 与 LLM 系统优化，让模型跑在边缘设备上。', tag: ['前沿'] }
          ]
        }
      ]
    },

    {
      num: '107', name: '创造与拓展', en: 'BUILD & CRAFT',
      desc: '知识最终要变成作品。这一层没有固定路径：学会写高质量的工程代码，做出能给别人用的东西——一个网站、一个渲染器、一个开源项目。',
      goal: '上线一个你自己的 Web 作品，或完成一个软光栅化渲染器。',
      topics: [
        {
          id: 'sweng', name: '软件工程', why: '「能跑」的代码和工业级代码有本质区别。',
          options: [
            { s: 'MIT', c: '6.031（原 6.005）', t: 'Software Construction', u: 'https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/', n: '如何写不易出 bug、简明易懂、易于维护的代码——强烈建议低年级就学。', tag: ['Java', '推荐'] },
            { s: 'UC Berkeley', c: 'CS169', t: 'Software Engineering（Agile + SaaS）', u: 'https://www.saasbook.info/', n: '小团队敏捷开发与云服务模式，配套教材免费在线。', tag: ['进阶'] }
          ]
        },
        {
          id: 'web', name: 'Web 开发', why: '搭个人主页、给项目做展示、成为独立开发者。',
          options: [
            { s: 'MIT', c: 'Web Lab', t: 'Web 开发两周速成', u: 'https://webdev.mit.edu/', n: 'IAP 短课，快速掌握前后端全栈开发。', tag: ['速成'] },
            { s: 'Stanford', c: 'CS142', t: 'Web Applications', u: 'https://web.stanford.edu/class/cs142/', n: '想系统学习 Web 应用的正经选择。', tag: ['系统'] },
            { s: '赫尔辛基大学', c: 'Full Stack Open', t: '现代全栈开发', u: 'https://fullstackopen.com/zh/', n: 'React + Node 的免费开源课程，有官方中文版。', tag: ['中文', '免费'] }
          ]
        },
        {
          id: 'graphics', name: '计算机图形学', why: '用代码创造视觉的世界。',
          options: [
            { s: 'GAMES', c: '101', t: '现代计算机图形学入门（闫令琪）', u: 'https://sites.cs.ucsb.edu/~lingqi/teaching/games101.html', n: '公认最好的图形学入门：7 次作业实现一个软光栅化渲染器，中文授课。', tag: ['中文', 'C++', '推荐'] },
            { s: 'GAMES', c: '103 / 202', t: '物理仿真 / 实时渲染（进阶）', u: 'https://games-cn.org/', n: 'GAMES 系列的进阶课：基于物理的动画与高质量实时渲染。', tag: ['进阶'] },
            { s: 'Stanford', c: 'CS148', t: 'Introduction to Computer Graphics', u: 'https://web.stanford.edu/class/cs148/', n: '斯坦福的图形学导论，英文路线之选。', tag: ['英文'] }
          ]
        }
      ]
    }
  ];

  /* ================= 渲染 ================= */

  var root = document.getElementById('stage-root');
  if (!root) return;
  var rail = document.getElementById('stage-rail');
  var empty = document.getElementById('atlas-empty');
  var search = document.getElementById('atlas-search');

  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  function optHtml(o) {
    var tags = (o.tag || []).map(function (t) { return '<span>' + esc(t) + '</span>'; }).join('');
    var link = o.u
      ? '<a href="' + esc(o.u) + '" target="_blank" rel="noopener">课程入口 ↗</a>'
      : '';
    return '<div class="opt">'
      + '<p class="opt-school">' + esc(o.s) + '</p>'
      + '<h4>' + esc(o.c) + (o.t ? '<em>' + esc(o.t) + '</em>' : '') + '</h4>'
      + '<p class="opt-note">' + esc(o.n) + '</p>'
      + '<div class="opt-foot"><span class="opt-tags">' + tags + '</span>' + link + '</div>'
      + '</div>';
  }

  function topicHtml(t, si, ti) {
    var opts = t.options.map(optHtml).join('');
    return '<div class="topic" data-id="' + si + '-' + ti + '">'
      + '<button class="topic-head" aria-expanded="false">'
      + '<span class="topic-arrow">▸</span>'
      + '<span class="topic-name">' + esc(t.name) + '</span>'
      + '<span class="topic-why">' + esc(t.why) + '</span>'
      + '<span class="topic-n">' + t.options.length + ' 门可选</span>'
      + '</button>'
      + '<div class="topic-body"><div class="opts">' + opts + '</div></div>'
      + '</div>';
  }

  function stageHtml(s, si) {
    var topics = s.topics.map(function (t, ti) { return topicHtml(t, si, ti); }).join('');
    return '<section class="tstage reveal" id="stage-' + s.num + '" data-num="' + s.num + '">'
      + '<div class="tstage-head">'
      + '<span class="tstage-num">TECH<br/>' + esc(s.num) + '</span>'
      + '<div class="tstage-info">'
      + '<h2>' + esc(s.name) + '<em>' + esc(s.en) + '</em></h2>'
      + '<p class="tstage-desc">' + esc(s.desc) + '</p>'
      + '<p class="tstage-goal"><b>过关项目</b>' + esc(s.goal) + '</p>'
      + '</div>'
      + '</div>'
      + '<div class="topics">' + topics + '</div>'
      + '</section>';
  }

  function railHtml() {
    return STAGES.map(function (s) {
      return '<a class="rail-chip" href="#stage-' + s.num + '" data-num="' + s.num + '">'
        + '<b>' + esc(s.num) + '</b><span>' + esc(s.name.split(' ')[0]) + '</span></a>';
    }).join('');
  }

  root.innerHTML = STAGES.map(stageHtml).join('');
  if (rail) rail.insertAdjacentHTML('afterbegin', railHtml());

  /* 动态注入的 .reveal 元素需要自行挂观察器（main.js 只处理静态元素） */
  if ('IntersectionObserver' in window) {
    var rio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add('in');
          rio.unobserve(en.target);
        }
      });
    }, { threshold: 0.08 });
    Array.prototype.forEach.call(root.querySelectorAll('.reveal'), function (el) { rio.observe(el); });
  } else {
    Array.prototype.forEach.call(root.querySelectorAll('.reveal'), function (el) { el.classList.add('in'); });
  }

  /* 手风琴 */
  root.addEventListener('click', function (e) {
    var head = e.target.closest('.topic-head');
    if (!head) return;
    var topic = head.parentElement;
    var open = topic.classList.toggle('open');
    head.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  /* 搜索：命中主题展开，无命中阶段隐藏；忽略空格与大小写（「C语言」≈「C 语言」） */
  function norm(s) { return String(s).toLowerCase().replace(/\s+/g, ''); }
  if (search) {
    search.addEventListener('input', function () {
      var q = norm(search.value.trim());
      var anyVisible = false;
      STAGES.forEach(function (s, si) {
        var stageEl = root.children[si];
        var stageVisible = false;
        s.topics.forEach(function (t, ti) {
          var topicEl = stageEl.querySelector('[data-id="' + si + '-' + ti + '"]');
          var hit = !q || norm(t.name + ' ' + t.why + ' ' + t.options.map(function (o) {
            return o.s + ' ' + o.c + ' ' + (o.t || '') + ' ' + o.n;
          }).join(' ')).indexOf(q) !== -1;
          topicEl.style.display = hit ? '' : 'none';
          if (hit) {
            stageVisible = true;
            if (q) {
              topicEl.classList.add('open');
              topicEl.querySelector('.topic-head').setAttribute('aria-expanded', 'true');
            }
          }
        });
        stageEl.style.display = stageVisible ? '' : 'none';
        if (stageVisible) anyVisible = true;
      });
      if (empty) empty.style.display = anyVisible ? 'none' : 'block';
    });
  }

  /* 滚动时高亮当前阶段的导航 */
  if (rail && 'IntersectionObserver' in window) {
    var chips = rail.querySelectorAll('.rail-chip');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var num = en.target.getAttribute('data-num');
        chips.forEach(function (c) {
          c.classList.toggle('on', c.getAttribute('data-num') === num);
        });
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    Array.prototype.forEach.call(root.querySelectorAll('.tstage'), function (el) { io.observe(el); });
  }
})();
