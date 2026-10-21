/* ============================================================
   星宙 · 科技航向 —— 课程星图数据与渲染
   数据来源：原 AstroVerseDAO 课程库（对标北大 CSDIY + EE 特色补充）
   ============================================================ */

(function () {
  'use strict';

  var COURSES = [
    /* ---------- 数学 ---------- */
    { id: 'calculus', name: 'MIT 18.01 / 18.02：Calculus 微积分', cat: '数学基础', group: 'math', school: 'MIT', prereq: '英语', lang: '无', diff: '★★', hours: '因人而异',
      desc: '由 MIT 18.01（单变量微积分）与 18.02（多变量微积分）组成。课程 notes 写得浅显生动且抓住本质，让你不再疲于做题，而是真正窥见微积分的魅力。配合 3Blue1Brown《微积分的本质》系列食用更佳。',
      res: ['课程网站：MIT OCW 18.01 / 18.02（open courseware）', '课程视频：参见课程网站', '课程教材：参见课程 notes', '课程作业：书面作业及答案参见课程网站'] },
    { id: 'linalg', name: 'MIT 18.06：Linear Algebra 线性代数', cat: '数学基础', group: 'math', school: 'MIT', prereq: '英语', lang: '无', diff: '★★★', hours: '因人而异',
      desc: '数学大牛 Gilbert Strang 的经典课程，教材《Introduction to Linear Algebra》已被清华采用为官方教材。矩阵、向量空间、特征分解是理解神经网络与数据科学的基础。配合 3Blue1Brown《线性代数的本质》系列食用更佳。',
      res: ['课程网站：MIT OCW 18.06（fall2011 视频完整开放）', '课程视频：参见课程网站', '课程教材：Introduction to Linear Algebra, Gilbert Strang', '课程作业：参见课程网站'] },
    { id: 'cs70', name: 'UCB CS70：Discrete Math and Probability 离散数学与概率论', cat: '数学基础', group: 'math', school: 'UC Berkeley', prereq: '无', lang: '无', diff: '★★★', hours: '60 小时',
      desc: '伯克利离散数学入门课。最大亮点是每个模块都结合理论在实际算法中的运用：逻辑证明→稳定匹配算法、图论→网络拓扑设计、数论→RSA、多项式环→纠错码、概率论→哈希表与负载均衡。',
      res: ['课程网站：eecs70.org', '课程教材：参见课程 notes', '课程作业：参见课程 Schedule'] },
    { id: 'numerical', name: 'MIT 18.330 / Computational Thinking：数值分析', cat: '数学进阶', group: 'math', school: 'MIT', prereq: '微积分、线性代数', lang: 'Julia', diff: '★★★', hours: '80 小时',
      desc: '用 Julia 把艰深的数学理论用直观的代码展示出来。先上 Computational Thinking 体验课（图像处理、社科数据、气候建模），再深入 18.330（浮点编码、求根、线性系统、微分方程）。',
      res: ['课程网站：MIT OCW（ComputationalThinking / 18.330）', '课程教材：Fundamentals of Numerical Computation（开源）', '课程作业：Julia 编程作业'] },
    { id: 'convex', name: 'Stanford EE364A：Convex Optimization 凸优化', cat: '数学进阶', group: 'math', school: 'Stanford', prereq: '线性代数、微积分', lang: 'MATLAB / Python', diff: '★★★★', hours: '100 小时',
      desc: '凸优化是机器学习的数学地基：SVM、LASSO、矩阵分解的背后都是它。Boyd 教授主讲的全球最经典凸优化课，讲义公开，配套教材《Convex Optimization》免费开源。',
      res: ['课程网站：Stanford EE364A 官网', '课程教材：Convex Optimization（Boyd，开源 PDF）', '课程作业：参见课程网站'] },

    /* ---------- 编程与软件 ---------- */
    { id: 'missing', name: 'MIT Missing-Semester：计算机教育中缺失的一课', cat: '编程入门', group: 'prog', school: 'MIT', prereq: '编程基础', lang: 'Shell / 工具链', diff: '★★★', hours: '20 小时',
      desc: '大学计算机课从不教你那些真正重要的工具：命令行、编辑器、版本控制、调试、自动化。一门课补齐：Shell、Vim、Git、调试器、元编程、安全与密码。它是从「会写代码」到「会用代码」的分水岭。',
      res: ['课程网站：missing.csail.mit.edu', '课程视频：课程网站 + B 站搬运', '课程作业：每讲配套练习'] },
    { id: 'cs50', name: 'Harvard CS50x：This is CS50 计算机科学导论', cat: '编程入门', group: 'prog', school: 'Harvard', prereq: '无', lang: 'C, Python', diff: '★★★', hours: '100 小时',
      desc: '哈佛最著名的入门课，面向零基础。从 C 语言讲起，覆盖算法、数据结构、内存、Web、安全，最后用 Python 收尾。授课极其生动，Project 成就感拉满，全世界数百万人在学。',
      res: ['课程网站：cs50.harvard.edu/x/', '课程视频：课程网站 + B 站（带中文字幕）', '课程作业：10 个 Problem Set + 最终 Project'] },
    { id: 'cs61a', name: 'UCB CS61A：Structure and Interpretation of Computer Programs', cat: '编程入门', group: 'prog', school: 'UC Berkeley', prereq: '无（零基础可学，略有挑战）', lang: 'Python, Scheme, SQL', diff: '★★★', hours: '50 小时',
      desc: '伯克利 CS61 系列第一门。不只是编程语言课，而是深入程序构造与运行的原理：函数式编程、数据抽象、面向对象，最后用 Python 实现一个 Scheme 解释器。',
      res: ['课程网站：cs61a.org（各学期均有存档）', '课程教材：Composing Programs（开源）', '课程作业：14 个 Lab + 4 个 Project（含 Scheme 解释器）'] },
    { id: 'cs50p', name: 'Harvard CS50P：Introduction to Programming with Python', cat: '编程入门', group: 'prog', school: 'Harvard', prereq: '无', lang: 'Python', diff: '★★★', hours: '60 小时',
      desc: 'CS50 系列的 Python 专项课，用 10 周系统掌握 Python：函数、库、单元测试、正则、文件 I/O、面向对象。比 CS61A 更温和，适合先扎实 Python 基础。',
      res: ['课程网站：cs50.harvard.edu/python/', '课程视频：课程网站 + B 站', '课程作业：每周 Problem Set + 期末项目'] },
    { id: 'cs61b', name: 'UCB CS61B：Data Structures and Algorithms 数据结构与算法', cat: '数据结构与算法', group: 'prog', school: 'UC Berkeley', prereq: 'CS61A', lang: 'Java', diff: '★★★', hours: '60 小时',
      desc: '数据结构与算法经典课。14 个 Lab 亲手实现绝大多数数据结构，3 个 Project 接触上千行工程代码（简易谷歌地图、二维 Minecraft）。autograder 开源，可通过 Gradescope 免费测评。',
      res: ['课程网站：sp24.datastructur.es', '课程视频：课程网站 + B 站中文翻译', '课程作业：14 Lab + 10 HW + 3 Project（Gradescope 免费测评）'] },
    { id: 'se', name: 'MIT 6.031：Software Construction 软件构造', cat: '软件工程', group: 'prog', school: 'MIT', prereq: 'Java 编程基础', lang: 'Java', diff: '★★★★', hours: '100 小时',
      desc: '一份「能跑」的代码和一份工业级代码有本质区别。6.031 传授如何编写不易出 bug、简明易懂、易于维护的高质量代码：从宏观数据结构设计到如何写注释。',
      res: ['课程网站：MIT 6.031 课程主页', '课程教材：课程阅读材料', '课程作业：编程练习与阅读作业'] },
    { id: 'webdev', name: 'Web 开发（MIT Web Development / Stanford CS142）', cat: 'Web 开发', group: 'prog', school: 'MIT / Stanford', prereq: '编程基础（Python 或 JS）', lang: 'HTML/CSS/JS, React', diff: '★★★', hours: '60 小时',
      desc: '前后端开发很少被大学培养方案重视，但掌握它好处多多：搭建个人主页、给项目做展示网页、成为独立开发者。想两周速成选 MIT Web Development；想系统学习选 Stanford CS142，再进阶 Full Stack Open。',
      res: ['课程网站：MIT Web Development / Stanford CS142 / Full Stack Open', '课程视频：参见各课程网站', '课程作业：参见各课程网站'] },

    /* ---------- EE 硬件 ---------- */
    { id: 'ee16', name: 'UCB EE16A&B：Designing Information Devices and Systems', cat: '电子基础', group: 'ee', school: 'UC Berkeley', prereq: '无', lang: 'Python', diff: '★★★', hours: '150 小时',
      desc: '伯克利电子系大一入门课，通过电路基础配合动手实操 Lab，体验「从环境收集信息 → 分析 → 预测和反馈」的完整链路。所有 Lab 都有远程在线版，非常适合自学。EE16B 引入反馈与控制，是控制论的入门。',
      res: ['课程网站：EE16A / EE16B 课程主页', '课程视频：B 站搜索', '课程教材：参见课程 notes', '课程作业：参见课程主页'] },
    { id: 'circuits', name: '电路与模拟电子（MIT 6.002 为核心）', cat: '电子基础', group: 'ee', school: 'MIT / 自建路径', prereq: '微积分、线性代数', lang: '无（电路仿真）', diff: '★★★★', hours: '100 小时',
      desc: '模拟世界的入口：KVL/KCL、电阻网络、运算放大器、频率响应、半导体基础。核心课 MIT 6.002 完整开放。进阶可读 Razavi《Microelectronics》——模拟电路是信号链路的根基，也是芯片设计的第一课。',
      res: ['课程网站：MIT OCW 6.002 Circuits and Electronics', '课程视频：OCW 完整课程录像', '课程教材：Agarwal & Lang, Foundations of Analog and Digital Electronic Circuits', '说明：星宙 EE 特色课（自建路径）'] },
    { id: 'signals', name: '信号与系统（UCB EE120 / MIT 6.003）', cat: '信号与系统', group: 'ee', school: 'UC Berkeley / MIT', prereq: 'CS61A, CS70，微积分，线性代数', lang: 'Python', diff: '★★★★★', hours: '100 小时',
      desc: '傅里叶变换给了我们一个全新的视角看待世界。EE120 最精华的是 6 个超有趣的 Python 编程作业：实现 FFT 并和 Numpy 比性能、通过手指影像推断心率、给哈勃望远镜照片降噪、构造反馈系统平衡细杆。',
      res: ['课程网站：inst.eecs.berkeley.edu/~ee120/fa19/', '课程视频：MIT 6.003 全部课程录影', '课程作业：EE120 为 5 书面 + 6 编程作业'] },
    { id: 'infotheory', name: '信息论（MIT 6.050J → 6.441）', cat: '信息论', group: 'ee', school: 'MIT / 自建路径', prereq: '入门无需先修；进阶需概率论', lang: '无', diff: '★★★★', hours: '60–120 小时',
      desc: '信息论是 AI 时代理解数据本质的核心：编码、压缩、通信、信息熵、信道容量。入门选 6.050J（专为大一设计，零先修），进阶选 6.441（信源编码、信道容量、率失真理论）。',
      res: ['课程网站：MIT OCW 6.050J / 6.441', '课程教材：Elements of Information Theory (Cover & Thomas)', '课程作业：参见 OCW', '说明：星宙 EE 特色课（自建路径）'] },
    { id: 'control', name: '控制论（EE16B → EE263 → 6.241）', cat: '控制论', group: 'ee', school: 'UC Berkeley / Stanford / MIT', prereq: '线性代数、信号与系统', lang: 'MATLAB / Python', diff: '★★★★★', hours: '120 小时',
      desc: '控制论是关于「系统如何被反馈塑造」的科学，也是 AI 智能体的理论前身：状态空间、稳定性、可控性、可观性。从 EE16B 到 Stanford EE263（线性动力系统）再到 MIT 6.241（PID、频域设计、鲁棒性）。想走向机器人、自动驾驶、具身智能的必修。',
      res: ['课程网站：Stanford EE263 官网 / MIT OCW 6.241', '课程教材：EE263 Lecture Notes（Boyd）', '课程作业：参见课程网站', '说明：星宙 EE 特色课（自建路径）'] },
    { id: 'digital', name: '数字电路与计算结构（MIT 6.004 为核心）', cat: '体系结构', group: 'ee', school: 'MIT / 自建路径', prereq: '编程入门、电路基础', lang: 'Verilog / 数字逻辑', diff: '★★★★', hours: '120 小时',
      desc: '从布尔代数、时序电路到流水线与 RISC-V 处理器的完整链路。核心课 MIT 6.004 Computation Structures：把数字逻辑 → 体系结构串起来，Project 在仿真器中搭建完整 CPU。配合 Nand2Tetris 与 CS61C 效果最佳。',
      res: ['课程网站：MIT OCW 6.004 Computation Structures', '课程视频：OCW 完整课程录像', '课程作业：Labs + Design Projects（OCW）', '说明：星宙 EE 特色课（自建路径）'] },

    /* ---------- 系统 ---------- */
    { id: 'csapp', name: 'CMU 15-213：CSAPP 深入理解计算机系统', cat: '计算机系统基础', group: 'sys', school: 'CMU', prereq: 'CS61A, CS61B', lang: 'C', diff: '★★★★★', hours: '150 小时',
      desc: 'CMU 镇系神课，以内容庞杂、Project 巨难而闻名。覆盖汇编、体系结构、操作系统、编译链接、并行、网络。11 个 Project（Data/Bomb/Attack/Cache/Malloc/Proxy Lab）是自学者的试金石。',
      res: ['课程网站：csapp.cs.cmu.edu', '课程视频：B 站全程录像', '课程教材：Computer Systems: A Programmer’s Perspective, 3/E', '中文讲解：B 站 UP 主九曲阑干'] },
    { id: 'cs110', name: 'Stanford CS110：Principles of Computer Systems', cat: '计算机系统基础', group: 'sys', school: 'Stanford', prereq: '编程基础、Unix、GDB、Valgrind', lang: 'C / C++', diff: '★★★★★', hours: '150 小时',
      desc: '在 CS107 基础上深入研究计算机系统和程序构建：程序如何映射到系统组件、大型系统的设计与权衡、跨机器的软件与并行计算。每周实验为项目增加新功能，作业配有完整测试框架。',
      res: ['课程网站：winter20 课程主页', '课程视频：spring19', '课程教材：Computer Systems: A Programmer’s Perspective', '课程作业：7 labs + 8 assignments'] },
    { id: 'cs61c', name: 'UCB CS61C：Great Ideas in Computer Architecture 体系结构', cat: '体系结构', group: 'sys', school: 'UC Berkeley', prereq: 'CS61A, CS61B', lang: 'C, RISC-V', diff: '★★★★★', hours: '120 小时',
      desc: 'RISC-V 发源地的正统体系结构课。注重实践：手写汇编构造神经网络、用 Logisim 从零搭建 CPU、实现 RISC-V 处理器。让你深入理解高级语言如何一步步变成机器可执行的 01 串。',
      res: ['课程网站：CS61C 课程主页（各学期存档）', '课程视频：课程网站 + B 站', '课程作业：Labs + Projects（含 CPU 实现）'] },
    { id: 'n2t', name: 'Nand2Tetris：从零造一台计算机', cat: '体系结构', group: 'sys', school: '希伯来大学 / Coursera', prereq: '无', lang: '任选一门编程语言', diff: '★★★', hours: '40 小时',
      desc: 'Coursera 上被数万人评为满分，全球四百多所高校采用。从与非门开始，构造逻辑电路、搭建 CPU、编译高级语言、开发简易 OS，最后在你自己造的计算机上运行俄罗斯方块。',
      res: ['课程网站：Nand2Tetris I / II（Coursera）', '课程教材：《计算机系统要素：从零开始构建现代计算机》', '课程作业：10 个 Project 造台计算机'] },
    { id: '6s081', name: 'MIT 6.1810（原 6.S081）：Operating System Engineering 操作系统', cat: '操作系统', group: 'sys', school: 'MIT', prereq: '体系结构 + 扎实 C 语言 + RISC-V 汇编', lang: 'C, RISC-V', diff: '★★★★★', hours: '150 小时',
      desc: 'MIT PDOS 实验室出品。基于 RISC-V 教学操作系统 xv6，每周一个 Lab（共 11 个），在 xv6 上增加新机制与特性。做系统不是靠 PPT 念出来的，是几万行代码一点点累起来的。',
      res: ['课程网站：pdos.csail.mit.edu/6.1810/', '课程视频：YouTube + 中文翻译文档（gitbook）', '课程教材：xv6 book（riscv-rev2 pdf）', '课程作业：11 个 Lab，测试框架完善'] },
    { id: 'cs162', name: 'UCB CS162：Operating Systems and Systems Programming 操作系统', cat: '操作系统', group: 'sys', school: 'UC Berkeley', prereq: 'CS61A/B/C，扎实 C 语言与 GDB 调试', lang: 'C, x86 汇编', diff: '★★★★★★', hours: '200 小时+',
      desc: 'Pintos 注重系统的 Design and Implementation：4 个 Project 在仅万行的教学 OS 上实现线程调度、系统调用、虚拟内存、文件系统。Stanford、Berkeley、JHU 等名校均采用 Pintos。',
      res: ['课程网站：CS162 当前学期 / 2022Spring 视频最适合自学', '课程教材：Operating Systems: Principles and Practice (2nd Edition)', '课程作业：3 Project + 6 Homework（含 Shell、HTTP 服务器、MapReduce）'] },
    { id: 'njuos', name: 'NJU 操作系统（蒋炎岩）', cat: '操作系统', group: 'sys', school: '南京大学', prereq: 'C 语言、体系结构', lang: 'C', diff: '★★★★★', hours: '120 小时',
      desc: '蒋炎岩老师的中文操作系统课，独到的系统视角结合丰富的代码示例，将众多 OS 概念讲得深入浅出。全程中文，非常适合国内自学者。实验围绕教学 OS 展开，从零理解中断、进程、虚拟内存、文件系统。',
      res: ['课程网站：南京大学操作系统课程主页', '课程视频：B 站完整课程', '课程作业：系列实验（含 OS 实验）'] },
    { id: 'cs149', name: 'CMU 15-418 / Stanford CS149：Parallel Computing 并行计算', cat: '并行与分布式', group: 'sys', school: 'CMU & Stanford', prereq: '计算机体系结构，熟悉 C++', lang: 'C++', diff: '★★★★★', hours: '150 小时',
      desc: '深入理解现代并行计算架构的设计原则与必要权衡，用 CUDA、MPI、OpenMP 等框架编写高性能并行程序。5 个编程作业从并行瓶颈分析到 CUDA、OpenMP、Spark，真正理论与实践结合。',
      res: ['课程网站：CMU15418 / CS149', '课程视频：CMU15418 / CS149', '课程作业：5 个编程作业（gfxcourses.stanford.edu/cs149/fall21）'] },
    { id: 'cs144', name: 'Stanford CS144：Computer Network 计算机网络', cat: '计算机网络', group: 'sys', school: 'Stanford', prereq: '一定的计算机系统基础，CS106L', lang: 'C++', diff: '★★★★★', hours: '100 小时',
      desc: '主讲人之一是网络巨擘 Nick McKeown 教授。8 个 Checkpoint 带你用 C++ 循序渐进搭建整个 TCP/IP 协议栈：可靠字节流、TCP、ARP、IP Router。与其说是网络课，更是一堂最好的现代 C++ 实践课。',
      res: ['课程网站：cs144.github.io', '课程视频：YouTube 官方合集', '课程作业：8 个 Project（checkpoint0-7）', '通关指南：@xzhseh 的 CS144 通关指北'] },
    { id: '15445', name: 'CMU 15-445：Introduction to Database Systems 数据库系统', cat: '数据库系统', group: 'sys', school: 'CMU', prereq: 'C++, 数据结构与算法, CSAPP', lang: 'C++', diff: '★★★★', hours: '100 小时',
      desc: '数据库大牛 Andy Pavlo 讲授。CMU Database Group 将课程基础设施完全开源，并开发了教学数据库 bustub——4 个 Project 实现缓冲池管理、B+ 树索引、查询执行器与优化器、并发控制，正反馈极强。',
      res: ['课程网站：Fall 2019–2022 / Spring 2023 版本', '课程视频：Fall 2022 YouTube 全开源 Lectures', '课程教材：Database System Concepts', '通关指南：@xzhseh 的 15-445 通关指北'] },
    { id: 'cs143', name: 'Stanford CS143：Compilers 编译原理', cat: '编译原理', group: 'sys', school: 'Stanford', prereq: '计算机体系结构', lang: 'Java 或 C++', diff: '★★★★★', hours: '150 小时',
      desc: '为 COOL 语言实现一个编译器，编译为 MIPS 汇编并在 Spim 模拟器上执行。理论按龙书顺序覆盖词法/语法/语义分析、运行时环境、寄存器分配、代码优化与生成；实践分四阶段循序渐进。',
      res: ['课程网站：web.stanford.edu/class/cs143/', '课程视频：B 站搬运', '课程教材：龙书', '课程作业：5 书面 + 5 编程作业实现一个编译器'] },

    /* ---------- 安全 ---------- */
    { id: 'cs161', name: 'UCB CS161：Computer Security 计算机安全', cat: '系统安全', group: 'sec', school: 'UC Berkeley', prereq: 'CS61A, CS61B, CS61C', lang: 'C, Go', diff: '★★★★★', hours: '150 小时',
      desc: '伯克利系统安全课，内容分 5 部分：安全设计原则、内存安全（缓冲区溢出）、密码学（对称/非对称、MAC、数字签名）、Web 安全（SQL 注入、XSS、XSRF）、网络安全。Project2 用 Go 设计实现一个安全文件分享系统（3000+ 行代码）。',
      res: ['课程网站：su20.cs161.org', '课程教材：textbook.cs161.org', '课程作业：7 在线 HW + 3 Lab + 3 Project'] },
    { id: 'seed', name: 'SU SEED Labs：网络安全动手实验', cat: '系统安全', group: 'sec', school: '雪城大学', prereq: '无（建议先学系统基础）', lang: 'C, 汇编', diff: '★★★★', hours: '150 小时',
      desc: 'NSF 资助开发的网安实践体系，全球 1050 家研究机构使用。四十多个动手实验覆盖软件安全、网络安全、Web 安全、操作系统安全和移动应用安全，配有开源讲义、视频教程与开箱即用的虚拟机和 Docker 攻防环境。',
      res: ['课程网站：seedsecuritylabs.org', '课程视频：handsonsecurity.net/video.html', '课程教材：handsonsecurity.net', '课程作业：四十多个 Lab（定制虚拟机/Docker 快速搭建）'] },

    /* ---------- AI · 图形 ---------- */
    { id: 'cs188', name: 'UCB CS188：Introduction to Artificial Intelligence 人工智能导论', cat: '人工智能', group: 'ai', school: 'UC Berkeley', prereq: 'CS70', lang: 'Python', diff: '★★★', hours: '50 小时',
      desc: '伯克利 AI 入门课（notes 足够，基本不需要看视频）。覆盖搜索剪枝、约束满足、马尔可夫决策、强化学习、贝叶斯网络以及基础机器学习。6 个 Project 质量爆炸：用 AI 算法让吃豆人在迷宫里穿梭。',
      res: ['课程网站：Spring 2024（视频资料完整，开放旁听 Gradescope）', '课程教材：Artificial Intelligence: A Modern Approach', '课程作业：在线测评书面作业 + 6 个 Project'] },
    { id: 'mlintro', name: 'Coursera：Machine Learning 机器学习（吴恩达）', cat: '机器学习', group: 'ai', school: 'Stanford / Coursera', prereq: 'AI 入门 + 熟练使用 Python', lang: 'Python', diff: '★★★', hours: '100 小时',
      desc: '吴恩达的成名作，机器学习入门神课。线性回归、逻辑回归、SVM、无监督学习、降维、异常检测、推荐系统。作业保姆级代码框架。想深究数学理论可继续 CS229。',
      res: ['课程网站：coursera.org/specializations/machine-learning-introduction', '课程视频：参见课程网站', '课程作业：参见课程网站'] },
    { id: 'cs229', name: 'Stanford CS229：Machine Learning 机器学习', cat: '机器学习', group: 'ai', school: 'Stanford', prereq: '高数、概率论、Python，需较深厚数学功底', lang: '无', diff: '★★★★', hours: '100 小时',
      desc: '同样是吴恩达讲授，但为研究生课程，更偏重数学理论。适合不满足于调包、想深入理解算法本质的学习者。课程 notes 写得非常专业且理论。',
      res: ['课程网站：cs229.stanford.edu', '课程视频：B 站搬运', '课程教材：课程 notes 写得非常好', '课程作业：不对公众开放'] },
    { id: 'dl', name: 'CMU 11-785：Introduction to Deep Learning 深度学习', cat: '深度学习', group: 'ai', school: 'CMU', prereq: '线性代数、概率论、Python、机器学习基础', lang: 'Python', diff: '★★★★★', hours: '120 小时',
      desc: '非常硬核的深度学习核心课，风格扎实、节奏快。从神经网络基础到 CNN、RNN、Attention/Transformer、优化与泛化。作业要求理解模型行为与实验设计，而非套模板跑通。投入产出比很高。',
      res: ['课程网站：deeplearning.cs.cmu.edu', '课程视频：课程网站提供 Lecture 录像', '课程教材：Lecture Notes / Slides + 论文阅读', '课程作业：多个编程作业 + 课程项目'] },
    { id: 'cs231n', name: 'Stanford CS231n：CNN for Visual Recognition 计算机视觉', cat: '深度学习', group: 'ai', school: 'Stanford', prereq: '机器学习基础', lang: 'Python', diff: '★★★★', hours: '80 小时',
      desc: 'Stanford CV 入门课，李飞飞院士领衔（ImageNet 团队）。内容基础友好：图像分类、CNN、训练技巧、迁移学习、目标检测。3 个编程作业从零实现全连接网络到 CNN。',
      res: ['课程网站：cs231n.stanford.edu', '课程视频：spring 2017 B 站 / spring 2025 YouTube', '课程作业：3 个编程作业（cs231n.stanford.edu/schedule.html）'] },
    { id: 'dlsys', name: 'CMU 10-414/714：Deep Learning Systems 深度学习系统', cat: '深度学习系统', group: 'ai', school: 'CMU', prereq: '系统入门（15-213）、深度学习入门、基础数学', lang: 'Python, C++', diff: '★★★', hours: '100 小时',
      desc: 'Zico Kolter 和 Tianqi Chen 主讲。覆盖深度学习系统「全栈」：框架顶层设计、自动微分原理与实现、硬件加速与生产部署。5 个作业从零实现深度学习库 Needle。拒绝当调包侠。',
      res: ['课程网站：dlsyscourse.org', '课程视频：YouTube 课程录像', '课程作业：dlsyscourse.org/assignments/'] },
    { id: 'tinyml', name: 'MIT 6.5940：TinyML and Efficient Deep Learning Computing', cat: '深度学习系统', group: 'ai', school: 'MIT', prereq: '深度学习基础、系统基础', lang: 'Python', diff: '★★★★', hours: '80 小时',
      desc: 'Song Han（韩松）老师的课程，学习让神经网络轻量化的关键技术：剪枝、量化、蒸馏、网络架构搜索（NAS），以及大语言模型相关的系统优化。想让模型跑在手机与边缘设备上的必修课。',
      res: ['课程网站：MIT 6.5940 课程主页', '课程视频：参见课程网站', '课程作业：Lab（TinyML 实战）'] },
    { id: 'games101', name: 'GAMES101：现代计算机图形学入门', cat: '计算机图形学', group: 'ai', school: 'GAMES（国内开源课程）', prereq: '线性代数、C++ 基础', lang: 'C++', diff: '★★★★', hours: '80 小时',
      desc: '闫令琪老师的中文图形学入门课，被公认为最好的图形学入门资源。从光栅化到光线追踪到几何处理与动画，7 次作业一步步实现一个软光栅化渲染器。中文授课，对自学者极其友好。',
      res: ['课程网站：GAMES101 课程主页', '课程视频：B 站完整课程', '课程作业：7 次作业实现软光栅化渲染器'] }
  ];

  var grid = document.getElementById('atlas-grid');
  if (!grid) return;
  var empty = document.getElementById('atlas-empty');
  var search = document.getElementById('atlas-search');
  var chips = Array.prototype.slice.call(document.querySelectorAll('.chip'));
  var modal = document.getElementById('course-modal');
  var state = { group: 'all', q: '' };

  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  function match(c) {
    if (state.group !== 'all' && c.group !== state.group) return false;
    if (state.q) {
      var hay = (c.name + ' ' + c.school + ' ' + c.cat + ' ' + c.desc).toLowerCase();
      if (hay.indexOf(state.q.toLowerCase()) === -1) return false;
    }
    return true;
  }

  function render() {
    var shown = COURSES.filter(match);
    grid.innerHTML = shown.map(function (c) {
      return '<article class="course" data-id="' + c.id + '" tabindex="0" role="button">'
        + '<span class="course-cat">' + esc(c.cat) + '</span>'
        + '<h3>' + esc(c.name) + '</h3>'
        + '<p class="course-school">' + esc(c.school) + '</p>'
        + '<div class="course-meta"><span class="stars">' + esc(c.diff) + '</span><span>' + esc(c.hours) + '</span><span>' + esc(c.lang) + '</span></div>'
        + '</article>';
    }).join('');
    empty.style.display = shown.length ? 'none' : 'block';

    // 更新计数
    chips.forEach(function (chip) {
      var g = chip.getAttribute('data-group');
      var n = g === 'all' ? COURSES.length : COURSES.filter(function (c) { return c.group === g; }).length;
      var base = chip.textContent.replace(/\s*\d+$/, '');
      chip.innerHTML = esc(base) + '<span class="n">' + n + '</span>';
    });
  }

  function openModal(c) {
    document.getElementById('modal-cat').textContent = c.cat + ' · ' + c.group.toUpperCase();
    document.getElementById('modal-title').textContent = c.name;
    document.getElementById('modal-meta').innerHTML =
      '<div><b>所属大学</b>' + esc(c.school) + '</div>'
      + '<div><b>先修要求</b>' + esc(c.prereq) + '</div>'
      + '<div><b>编程语言</b>' + esc(c.lang) + '</div>'
      + '<div><b>课程难度</b><span class="stars">' + esc(c.diff) + '</span>　<span style="font-family:var(--mono);font-size:11px">' + esc(c.hours) + '</span></div>';
    document.getElementById('modal-desc').textContent = c.desc;
    document.getElementById('modal-res').innerHTML = c.res.map(function (r) { return '<li>' + esc(r) + '</li>'; }).join('');
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    modal.classList.remove('open');
    document.body.style.overflow = '';
  }

  chips.forEach(function (chip) {
    chip.addEventListener('click', function () {
      chips.forEach(function (x) { x.classList.remove('on'); });
      chip.classList.add('on');
      state.group = chip.getAttribute('data-group');
      render();
    });
  });

  if (search) {
    search.addEventListener('input', function () {
      state.q = search.value.trim();
      // 搜索时自动跳出当前分类筛选，避免「搜不到」的错觉
      if (state.q && state.group !== 'all') {
        state.group = 'all';
        chips.forEach(function (x) { x.classList.toggle('on', x.getAttribute('data-group') === 'all'); });
      }
      render();
    });
  }

  grid.addEventListener('click', function (e) {
    var card = e.target.closest('.course');
    if (!card) return;
    var c = COURSES.find(function (x) { return x.id === card.getAttribute('data-id'); });
    if (c) openModal(c);
  });
  grid.addEventListener('keydown', function (e) {
    if (e.key !== 'Enter') return;
    var card = e.target.closest('.course');
    if (!card) return;
    var c = COURSES.find(function (x) { return x.id === card.getAttribute('data-id'); });
    if (c) openModal(c);
  });

  document.getElementById('modal-close').addEventListener('click', closeModal);
  document.getElementById('modal-backdrop').addEventListener('click', closeModal);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && modal.classList.contains('open')) closeModal();
  });

  render();
})();
