#!/usr/bin/env python3
"""Comprehensive frontmatter fix for remaining 29+ papers."""

import os, re

OUTPUTS = "/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/Outputs"

# Each entry: dir_path_component -> {field: value} or special actions
FIXES = {}

# Helper: add fix for a paper
def fix(dir_key, **fields):
    FIXES[dir_key] = fields

# ========== SECTION 1: Papers with full info from web search ==========

# 2.5 2022 CMOS-compatible - Science Advances, DOI: 10.1126/sciadv.abm8537
fix("2.5 2022 CMOS-compatible compute-in-memory acc",
    title="CMOS-Compatible Compute-in-Memory Accelerators Based on Integrated Ferroelectric Synaptic Arrays for Convolution Neural Networks",
    authors=["Min-Kyu Kim", "Ik-Jyae Kim", "Jang-Sik Lee"],
    date="2022-04-08",
    abstract="Convolutional neural networks (CNNs) require intensive multiply-and-accumulate (MAC) operations that strain conventional computing systems. This paper proposes a compute-in-memory (CIM) approach using integrated ferroelectric thin-film transistor (FeTFT) synaptic arrays. Three-terminal FeTFTs serve as both nonvolatile memory and access devices, overcoming leakage current and high-power issues of two-terminal crossbar-based CIM. FeTFTs enable efficient parallel programming and data processing through selective, accurate control of polarization in the ferroelectric (HfZrOx) layer. The integrated synaptic array performs convolution operations directly in memory, enabling high-accuracy image feature extraction for CNNs. The entire process is CMOS-compatible, making it suitable for practical semiconductor integration.",
    abstract_cn="卷积神经网络（CNN）需要密集的乘累加操作，给传统计算系统带来巨大压力。本文提出了一种使用集成铁电薄膜晶体管（FeTFT）突触阵列的存内计算方法。三端FeTFT同时作为非易失性存储器和访问器件，克服了两端crossbar存内计算方案的漏电流和高功耗问题。FeTFT通过选择性、精确地控制铁电（HfZrOx）层极化实现高效的并行编程和数据处理。集成突触阵列直接在内存中执行卷积操作，实现高精度CNN图像特征提取。整个过程兼容CMOS工艺，适用于实际半导体集成。",
    cite="Kim M K, Kim I J, Lee J S. CMOS-Compatible Compute-in-Memory Accelerators Based on Integrated Ferroelectric Synaptic Arrays for Convolution Neural Networks[J]. Science Advances, 2022, 8(14): eabm8537. DOI: 10.1126/sciadv.abm8537",
    keywords=["[[Compute-In-Memory]]", "[[FeFET]]", "[[Ferroelectric Synaptic Array]]", "[[CNN]]", "[[CMOS-Compatible]]", "[[存内计算]]", "[[铁电突触阵列]]"])

# 25.1 adma201701907-sup - Advanced Materials, DOI: 10.1002/adma.201701907
fix("25.1 adma201701907-sup-0001-s1",
    title="Organic Ferroelectric-Based 1T1T Random Access Memory Cell Employing a Common Dielectric Layer Overcoming the Half-Selection Problem",
    authors=["Qiang Zhao", "Hanlin Wang", "Zhenjie Ni", "Jie Liu", "Yonggang Zhen", "Xiaotao Zhang", "Lang Jiang", "Rongjin Li", "Huanli Dong", "Wenping Hu"],
    date="2017-09-13",
    journal="Advanced Materials",
    abstract="Organic electronics based on poly(vinylidenefluoride/trifluoroethylene) (P(VDF-TrFE)) dielectric face challenges in flexible circuits. This work reports a novel ferroelectric random access memory cell (1T1T FeRAM cell) consisting of one selection transistor and one ferroelectric memory transistor, designed to overcome the half-selection problem. Unlike conventional approaches using multiple dielectrics, this system simplifies fabrication by using one common dielectric layer. A semiconductor/insulator (S/I) interface modulation strategy is employed to create nonhysteretic selection transistors with high performance. Hole mobility of 3.81 cm2 V-1 s-1 for DPA and electron mobility of 0.124 cm2 V-1 s-1 for PDI-FCN2 were achieved.",
    abstract_cn="基于P(VDF-TrFE)介电层的有机电子器件在柔性电路中面临挑战。本文报道了一种新型铁电随机存取存储器单元（1T1T FeRAM），由一个选择晶体管和一个铁电存储晶体管组成，旨在克服半选择问题。与使用多种介电层的传统方法不同，该系统通过使用一个共用的介电层简化了制造工艺。采用半导体/绝缘体界面调制策略实现了高性能的无迟滞选择晶体管。DPA的空穴迁移率达3.81 cm2 V-1 s-1，PDI-FCN2的电子迁移率达0.124 cm2 V-1 s-1。",
    cite="Zhao Q, Wang H, Ni Z, Liu J, Zhen Y, Zhang X, Jiang L, Li R, Dong H, Hu W. Organic Ferroelectric-Based 1T1T Random Access Memory Cell Employing a Common Dielectric Layer Overcoming the Half-Selection Problem[J]. Advanced Materials, 2017, 29(34): 1701907. DOI: 10.1002/adma.201701907",
    keywords=["[[FeRAM]]", "[[Organic Electronics]]", "[[Ferroelectric Memory]]", "[[1T1T Cell]]", "[[铁电存储器]]", "[[有机电子]]"])

# lomenzo-et-al-2024 - ACS Applied Materials & Interfaces, DOI: 10.1021/acsami.4c05798
fix("lomenzo-et-al-2024-ferroelectric-al0-85sc0-15n",
    title="Ferroelectric Al0.85Sc0.15N and Hf0.5Zr0.5O2 Domain Switching Dynamics",
    authors=["Roberto Guido", "Xuetao Wang", "Bohan Xu", "Ruben Alcala", "Thomas Mikolajick", "Uwe Schroeder", "Patrick D. Lomenzo"],
    date="2024-07-31",
    journal="ACS Applied Materials & Interfaces",
    abstract="This work uses transient current integration measurements to compare domain switching dynamics in two leading ferroelectric thin-film systems: Al0.85Sc0.15N and Hf0.5Zr0.5O2. Al0.85Sc0.15N switching is dominated by thermally activated creep domain wall motion, benefiting from c-axis texture and single-phase nature for homogeneous local switching field, but suffers from domain wall pinning upon bipolar cycling. Hf0.5Zr0.5O2 is characterized by independently nucleating domains and domain wall creep, with inhomogeneous local switching field due to polymorphism and grain boundaries. The wake-up effect is explained by continuous addition of switchable regions from two independent distributions of switching times. The paper directly addresses multibit memory applications for high-density crossbar arrays targeting edge neural network inference.",
    abstract_cn="本文使用瞬态电流积分测量方法比较了两种主流铁电薄膜系统Al0.85Sc0.15N和Hf0.5Zr0.5O2的畴切换动力学。Al0.85Sc0.15N的切换主要由热激活蠕变畴壁运动主导，受益于c轴织构和单相性质带来的均匀局部切换场，但在双极循环中会出现畴壁钉扎。Hf0.5Zr0.5O2的特征在于独立成核的畴和畴壁蠕变，由于多晶型和晶界导致局部切换场不均匀。唤醒效应通过两个独立分布的切换时间持续添加可切换区域来解释。本文直接针对高密度crossbar阵列中面向边缘神经网络推理的多比特存储应用。",
    cite="Guido R, Wang X, Xu B, Alcala R, Mikolajick T, Schroeder U, Lomenzo P D. Ferroelectric Al0.85Sc0.15N and Hf0.5Zr0.5O2 Domain Switching Dynamics[J]. ACS Applied Materials & Interfaces, 2024, 16(32): 42415-42425. DOI: 10.1021/acsami.4c05798")

# s41467-020-16108-9 - Nature Communications, 2020-05-18
fix("s41467-020-16108-9",
    title="Accurate Deep Neural Network Inference Using Computational Phase-Change Memory",
    authors=["Vinay Joshi", "Manuel Le Gallo", "Simon Haefeli", "Irem Boybat", "S. R. Nandakumar", "Christophe Piveteau", "Martino Dazzi", "Bipin Rajendran", "Abu Sebastian", "Evangelos Eleftheriou"],
    date="2020-05-18",
    abstract="In-memory computing using resistive memory devices is a promising non-von Neumann approach for making energy-efficient deep learning inference hardware. However, due to device variability and noise, the network needs to be trained to be robust to these effects. We introduce a methodology to train ResNet-type convolutional neural networks that results in no appreciable accuracy loss when transferring weights to phase-change memory (PCM) devices. We also propose a compensation technique that exploits the batch normalization parameters to improve accuracy retention over time. We achieve a classification accuracy of 93.7% on CIFAR-10 and a top-1 accuracy of 71.6% on ImageNet after mapping the trained weights to PCM. Our hardware results on a prototype PCM chip demonstrate 93.5% accuracy on CIFAR-10 with ResNet-32, representing the highest accuracy reported for an analog resistive memory hardware.",
    abstract_cn="使用电阻式存储器件进行存内计算是实现高能效深度学习推理硬件的一种有前景的非冯·诺依曼方法。然而，由于器件变异性和噪声，网络需要被训练为对这些效应具有鲁棒性。我们介绍了一种训练ResNet型卷积神经网络的方法，在将权重转移到相变存储器（PCM）器件时不会产生明显的精度损失。我们还提出了一种补偿技术，利用批归一化参数来改善精度随时间的保持。我们将训练好的权重映射到PCM后，在CIFAR-10上达到93.7%的分类准确率，在ImageNet上达到71.6%的Top-1准确率。在原型PCM芯片上的硬件结果展示了CIFAR-10上ResNet-32的93.5%准确率，这是模拟电阻式存储硬件报道的最高精度。",
    cite="Joshi V, Le Gallo M, Haefeli S, Boybat I, Nandakumar S R, Piveteau C, Dazzi M, Rajendran B, Sebastian A, Eleftheriou E. Accurate Deep Neural Network Inference Using Computational Phase-Change Memory[J]. Nature Communications, 2020, 11: 2473. DOI: 10.1038/s41467-020-16108-9")

# s41467-025-65151-x - Nature Communications, 2025-11-19
fix("s41467-025-65151-x",
    title="Photonic Edge Intelligence Chip for Multi-Modal Sensing, Inference and Learning",
    authors=["Shiji Zhang", "Xueyi Jiang", "Bo Wu", "Haojun Zhou", "Wenguang Xu", "Hailong Zhou", "Zhichao Ruan", "Jianji Dong", "Xinliang Zhang"],
    date="2025-11-19",
    abstract="Edge intelligence requires sensing, computing, and learning capabilities in a compact, energy-efficient form factor. This work demonstrates a Photonic Edge Intelligence Chip (PEIC) that fuses multiple analog modalities—images, spectra, and radio-frequency signals—into broad optical spectra for single-fiber input, enabling direct analog processing without digital conversion. The chip uses an Arrayed Waveguide Grating (AWG) for simultaneous spectral sensing and energy-efficient convolution (29 fJ/OP), followed by a nonlinear activation layer and a fully connected layer to form an end-to-end optical neural network. On-chip inference achieves a measured response time of 1.33 nanoseconds. The chip demonstrates supervised and unsupervised learning across three modalities: drug spectral recognition, image classification, and radar target classification, establishing a sensing-computing integrated photonic platform for ultra-low-latency edge intelligence.",
    abstract_cn="边缘智能需要在紧凑、高能效的形态中集成感知、计算和学习能力。本文展示了一款光子边缘智能芯片（PEIC），将图像、光谱和射频信号等多种模拟模态融合到宽光谱中实现单光纤输入，无需数字转换即可直接进行模拟处理。芯片利用阵列波导光栅（AWG）实现同步光谱感知和高能效卷积（29 fJ/OP），随后通过非线性激活层和全连接层构成端到端光学神经网络。片上推理实测响应时间为1.33纳秒。芯片在药物光谱识别、图像分类和雷达目标分类三种模态上展示了监督和无监督学习能力，为超低延迟边缘智能建立了感知-计算一体化的光子平台。",
    cite="Zhang S, Jiang X, Wu B, Zhou H, Xu W, Zhou H, Ruan Z, Dong J, Zhang X. Photonic Edge Intelligence Chip for Multi-Modal Sensing, Inference and Learning[J]. Nature Communications, 2025, 16: 10136. DOI: 10.1038/s41467-025-65151-x")

# s41598-020-78944-5 - Scientific Reports, 2021
fix("s41598-020-78944-5",
    title="Combinatorial Optimization by Weight Annealing in Memristive Hopfield Networks",
    authors=["Z. Fahimi", "M. R. Mahmoodi", "H. Nili", "Valentin Polishchuk", "D. B. Strukov"],
    date="2021-08-12",
    year=2021,
    abstract="The Hopfield neural network is a powerful framework for solving combinatorial optimization problems. However, hardware implementations suffer from non-idealities of emerging non-volatile memory devices. Here we propose a weight annealing approach: initial setting of all synaptic weights to zero allows the network to quickly settle into its trivial global-minimum state, then gradually introducing the weights during the annealing process keeps the network close to its ground state throughout. Extensive numerical simulations show that weight annealing yields better solutions on average for several representative combinatorial optimization problems. As a proof of concept, we experimentally solve a 13-node graph partitioning problem using a 20x20 analog-grade TiO2 memristive crossbar and a 7-node maximum-weight independent set problem using a 12x10 eFlash memory array.",
    abstract_cn="Hopfield神经网络是解决组合优化问题的强大框架。然而，硬件实现受到新兴非易失性存储器件非理想性的影响。本文提出了一种权重退火方法：初始将所有突触权重设为零使网络快速进入平凡的全局最小状态，然后在退火过程中逐渐引入权重，使网络始终保持在基态附近。大量数值模拟表明，权重退火在多个代表性组合优化问题上平均能获得更好的解。作为概念验证，我们使用20x20模拟级TiO2忆阻器crossbar实验解决了13节点图划分问题，使用12x10 eFlash存储阵列解决了7节点最大权重独立集问题。",
    cite="Fahimi Z, Mahmoodi M R, Nili H, Polishchuk V, Strukov D B. Combinatorial Optimization by Weight Annealing in Memristive Hopfield Networks[J]. Scientific Reports, 2021, 11: 16383. DOI: 10.1038/s41598-020-78944-5")

# science.adv7434 - Science, 2024-12-19 (title was WRONG: "PHOTONIC COMPUTI NG")
fix("science.adv7434",
    title="All-Optical Synthesis Chip for Large-Scale Intelligent Semantic Vision Generation",
    authors=["Yitong Chen", "Xinyue Sun", "Guangtao Zhai", "Wenjun Zhang"],
    date="2024-12-19",
    journal="Science",
    abstract="This paper presents LightGen, the first large-scale all-optical generative AI chip that simultaneously breaks through three recognized bottlenecks: million-scale optical neuron integration, all-optical dimension conversion, and ground-truth-free optical chip training algorithms. The chip achieves 2 orders of magnitude improvement in computing power and energy efficiency compared to state-of-the-art digital chips, with theoretical potential for 7 orders of magnitude computing power improvement if signal input is not the bottleneck. LightGen supports high-resolution image semantic generation, 3D generation (NeRF), high-definition video generation, semantic control, denoising, and style transfer, marking the transition of all-optical chips from small-scale classification tasks to large-scale generative AI.",
    abstract_cn="本文提出了LightGen，这是国际首款大规模全光生成式AI芯片，在单枚芯片上同时突破了三大公认瓶颈：百万级光学神经元集成、全光维度转换和无真值光芯片训练算法。该芯片相比顶尖数字芯片实现了2个数量级的算力提升和能效提升，理论上（若信号输入不是瓶颈）算力可提升7个数量级，能效可提升8个数量级。LightGen支持高分辨率图像语义生成、3D生成（NeRF）、高清视频生成、语义调控、去噪和风格迁移，标志着全光芯片从分类等小规模任务正式进入大规模生成式AI领域。",
    cite="Chen Y, Sun X, Zhai G, Zhang W. All-Optical Synthesis Chip for Large-Scale Intelligent Semantic Vision Generation[J]. Science, 2024, 386: 1480-1487. DOI: 10.1126/science.adv7434",
    keywords=["[[All-Optical Chip]]", "[[Generative AI]]", "[[LightGen]]", "[[NeRF]]", "[[全光芯片]]", "[[生成式AI]]"])

# scirobotics.abb9764 - Science Robotics, 2020-09-23 (title was WRONG: "A R T I F I C I A L I N T E L L I G E N C E")
fix("scirobotics.abb9764",
    title="An Adaptive Deep Reinforcement Learning Framework Enables Curling Robots with Human-Like Performance in Real-World Conditions",
    authors=["Dong-Ok Won", "Klaus-Robert Müller", "Seong-Whan Lee"],
    date="2020-09-23",
    journal="Science Robotics",
    abstract="The game of curling can be considered a good test bed for studying the interaction between artificial intelligence systems and the real world. Here we report a curling robot, Curly, that uses an adaptive deep reinforcement learning framework to achieve human-level performance. Curly won three out of four official matches against top-ranked South Korean women's curling teams and the Korea national wheelchair curling team. The framework extends standard deep reinforcement learning with temporal features to compensate for the real-world uncertainties and nonstationarities inherent to the sport of curling. This work demonstrates that an adaptive DRL framework can effectively handle the highly uncertain and nonstationary real-world conditions of the sport of curling.",
    abstract_cn="冰壶运动可以被视为研究人工智能系统与现实世界交互的一个良好测试平台。本文报道了一款名为Curly的冰壶机器人，使用自适应深度强化学习框架实现了人类水平的表现。Curly在与韩国顶尖女子冰壶队和韩国国家轮椅冰壶队的四场正式比赛中赢得了三场。该框架扩展了标准深度强化学习，加入时间特征来补偿冰壶运动中固有的真实世界不确定性和非平稳性。该工作证明了自适应DRL框架能够有效处理冰壶运动高度不确定和非平稳的现实条件。",
    cite="Won D O, Müller K R, Lee S W. An Adaptive Deep Reinforcement Learning Framework Enables Curling Robots with Human-Like Performance in Real-World Conditions[J]. Science Robotics, 2020, 5(46): eabb9764. DOI: 10.1126/scirobotics.abb9764",
    keywords=["[[Deep Reinforcement Learning]]", "[[Robotics]]", "[[Curling Robot]]", "[[深度强化学习]]", "[[机器人]]"])

# 26 ma-et-al-2025 - Nano Letters, 2025-02-03 (NOT Cell)
fix("26 ma-et-al-2025-van-der-waals-engineering-of-",
    title="Van der Waals Engineering of One-Transistor-One-Ferroelectric-Memristor Architecture for an Energy-Efficient Neuromorphic Array",
    authors=["Yinchang Ma", "Maolin Chen", "Fernando Aguirre", "Yuan Yan", "Sebastian Pazos", "Chen Liu", "Heng Wang", "Tao Yang", "Baoyu Wang", "Cheng Gong", "Kai Liu", "Jefferson Zhe Liu", "Mario Lanza", "Fei Xue", "Xixiang Zhang"],
    date="2025-02-03",
    journal="Nano Letters",
    abstract="This work demonstrates a fully van der Waals assembled 1T1M (one-transistor-one-memristor) architecture, stacking two-dimensional ferroelectric CuCrP2S6 with MoS2 and h-BN. The device achieves ultra-low leakage current of ~120 fA at Vtg=-3V, ultra-high resistance tunability of ~10^6, and ultra-low static power consumption of only 12 fW. It is electroforming-free with operating voltage below 1V. A neuromorphic array with crosstalk reduction of 2 orders of magnitude was experimentally demonstrated, and a simulated 256x10 artificial neural network achieves 90% image recognition accuracy with only 12.77 uW power consumption.",
    abstract_cn="本文展示了一种全范德华组装的1T1M（单晶体管-单忆阻器）架构，将二维铁电CuCrP2S6与MoS2和h-BN堆叠组装。器件实现了~120 fA的超低漏电流（Vtg=-3V）、~10^6的超高阻态可调性和仅12 fW的超低静态功耗。无需电铸工艺，操作电压低于1V。实验演示了串扰降低2个数量级的神经形态阵列，模拟的256x10人工神经网络实现90%图像识别准确率，功耗仅12.77 uW。",
    cite="Ma Y, Chen M, Aguirre F, Yan Y, Pazos S, Liu C, Wang H, Yang T, Wang B, Gong C, Liu K, Liu J Z, Lanza M, Xue F, Zhang X. Van der Waals Engineering of One-Transistor-One-Ferroelectric-Memristor Architecture for an Energy-Efficient Neuromorphic Array[J]. Nano Letters, 2025, 25(6): 2510-2519. DOI: 10.1021/acs.nanolett.4c06118")

# s40820-025-01968-x - Nano-Micro Letters, 2026-01-13
fix("s40820-025-01968-x",
    title="Ferroelectric Optoelectronic Sensor for Intelligent Flame Detection and In-Sensor Motion Perception",
    authors=["Jiayun Wei", "Guokun Ma", "Runzhi Liang", "Wenxiao Wang", "Hao Wang", "Wei Han", "Liangping Shen", "Longhui Zeng"],
    date="2026-01-13",
    journal="Nano-Micro Letters",
    abstract="This work demonstrates a Ga2O3/In2Se3 ferroelectric-optoelectronic heterojunction sensor array (5x5 pixels) for intelligent flame detection and in-sensor motion perception. Through ferroelectric polarization modulation, the sensor achieves a detectivity of 4.91x10^17 Jones at 255 nm solar-blind ultraviolet light, placing it at the forefront of Ga2O3-based UV detectors. Combined with an NB-IoT module, it enables real-time cloud and mobile terminal alarm for all-day flame detection. A lightweight CNN achieves 96.47% flame motion recognition accuracy, and a photosensitive artificial neural system achieves 90.51% recognition accuracy for extremely weak early-stage flame UV light.",
    abstract_cn="本文展示了一种Ga₂O₃/In₂Se₃铁电-光电异质结传感器阵列（5×5像素），用于智能火焰检测和传感器内运动感知。通过铁电极化调控，传感器在255 nm日盲紫外光下探测率高达4.91×10¹⁷ Jones，处于Ga₂O₃基紫外探测器领先水平。结合NB-IoT模块实现云端和移动终端全时段实时火焰报警。轻量级CNN实现96.47%火焰运动识别准确率，光敏人工神经系统对极弱早期火焰紫外光识别率达90.51%。",
    cite="Wei J, Ma G, Liang R, Wang W, Wang H, Han W, Shen L, Zeng L. Ferroelectric Optoelectronic Sensor for Intelligent Flame Detection and In-Sensor Motion Perception[J]. Nano-Micro Letters, 2026, 18: 123. DOI: 10.1007/s40820-025-01968-x")

# s41467-025-58359-4 - Nature Communications, 2025-03-28 (year was '2024', fix to 2025)
fix("s41467-025-58359-4",
    title="In-Memory Ferroelectric Differentiator",
    authors=["Guangdi Feng", "Xiaoming Zhao", "Xiaoyue Huang", "Xiaoxu Zhang", "Yangyang Wang", "Wei Li", "Luqiu Chen", "Shenglan Hao", "Qiuxiang Zhu", "Yachin Ivry", "Brahim Dkhil", "Bobo Tian", "Peng Zhou", "Junhao Chu", "Chungang Duan"],
    date="2025-03-28",
    year=2025,
    abstract="Differential computation is fundamental to image processing, yet conventional systems require multi-step processes: image detection, data transmission, memory storage, and MCU computation. This work develops an in-memory ferroelectric differentiator using a 40x40 passive crossbar array of 1,600 ferroelectric P(VDF-TrFE) polymer capacitors. By exploiting the dynamic behavior of ferroelectric domain reversal, differential computation is performed directly within memory. Key achievements include: ultra-low energy of ~0.24 fJ per calculation, operation at 1 MHz with potential for sub-picosecond switching, retention >5 days, moving object extraction accuracy of ~98.9%, and ideal computational efficiency of ~4.17 POPS/W—roughly 10,000x higher than an NVIDIA V100 GPU. First- and second-order derivative solving, motion extraction, and image discrepancy identification were successfully demonstrated.",
    abstract_cn="微分计算是图像处理的基础，但传统系统需要多步操作：图像检测、数据传输、存储和MCU计算。本文开发了一种存内铁电差分器，使用由1600个铁电P(VDF-TrFE)聚合物电容组成的40×40无源crossbar阵列。通过利用铁电畴反转的动态行为，直接在存储器内执行微分计算。关键成就包括：每次计算仅需~0.24 fJ的超低能耗，1 MHz工作频率（亚皮秒切换潜力），>5天保持时间，~98.9%的运动物体提取准确率，以及~4.17 POPS/W的理想计算效率——比NVIDIA V100 GPU高约10,000倍。成功演示了一阶和二阶导数求解、运动提取和图像差异识别。",
    cite="Feng G, Zhao X, Huang X, Zhang X, Wang Y, Li W, Chen L, Hao S, Zhu Q, Ivry Y, Dkhil B, Tian B, Zhou P, Chu J, Duan C. In-Memory Ferroelectric Differentiator[J]. Nature Communications, 2025, 16: 3027. DOI: 10.1038/s41467-025-58359-4")

# s41467-025-68206-1 - Nature Communications, 2026-01-08 (year was '2025', fix to 2026)
fix("s41467-025-68206-1_reference",
    title="Coupled Ferroelectric-Anisotropic Optoelectronic Synapse for Polarization-Sensitive Neuromorphic Vision",
    authors=["Jiali Huo", "Jinpeng Huo", "Jing Gao", "Lingqi Li", "Thaw Tint Te Tun", "Jin Peng", "Haofei Zheng", "Yufei Shi", "Kah-Wee Ang"],
    date="2026-01-08",
    year=2026,
    abstract="This paper presents a polarization-resolved optoelectronic synapse that integrates polarization-sensitive photodetection and non-volatile memory in a single device, overcoming interfacial instabilities in 2D/ferroelectric junctions. The device uses a 2D ReS2 channel combined with a ferroelectric Hf0.5Zr0.5O2 (HZO) gate dielectric in a Metal-Ferroelectric-Metal-Insulator-Semiconductor (MFMIS) FeFET. Co-modulation of ferroelectric polarization and photoexcited carrier trapping enables high responsivity, strong detectivity, and long-term optoelectronic retention. An ANN achieves 97.33% accuracy in iris recognition under unpolarized light, and a 3x3 FeFET-based CNN performs butterfly classification via polarization-resolved feature extraction, with linear, energy-efficient optical-electrical modulation at 2.0 fJ per event.",
    abstract_cn="本文提出了一种偏振分辨光电突触，在单个器件中集成偏振敏感光电检测和非易失性存储，克服了二维/铁电异质结的界面不稳定性。器件采用2D ReS2沟道结合铁电Hf0.5Zr0.5O2栅介质，构成金属-铁电-金属-绝缘体-半导体（MFMIS）FeFET结构。铁电极化与光生载流子捕获的协同调控实现了高响应度、强探测率和长期光电保持。ANN在非偏振光下实现97.33%的虹膜识别准确率，3x3 FeFET型CNN通过偏振分辨特征提取实现蝴蝶分类，光电调制能效达2.0 fJ/事件。",
    cite="Huo J, Huo J, Gao J, Li L, Tun T T T, Peng J, Zheng H, Shi Y, Ang K W. Coupled Ferroelectric-Anisotropic Optoelectronic Synapse for Polarization-Sensitive Neuromorphic Vision[J]. Nature Communications, 2026, 17: 1468. DOI: 10.1038/s41467-025-68206-1")

# s43246-025-01033-5 - Communications Materials, 2025
fix("s43246-025-01033-5_reference",
    title="Unsupervised Local Learning Based on Voltage-Dependent Synaptic Plasticity for Resistive and Ferroelectric Synapses",
    authors=["Nikhil Garg", "Ismael Balafrej", "Joao Henrique Quintino Palhares", "Laura Bégon-Lours", "Davide Florini", "Donato Francesco Falcone", "Tommaso Stecconi", "Valeria Bragaglia", "Bert Jan Offrein", "Jean-Michel Portal", "Damien Querlioz", "Yann Beilliard", "Dominique Drouin", "Fabien Alibart"],
    date="2025-01-15",
    year=2025,
    journal="Communications Materials",
    abstract="This paper introduces voltage-dependent synaptic plasticity (VDSP) as an efficient, unsupervised, local learning mechanism for memristive synapses grounded in Hebbian principles. VDSP enables online learning without the complex pulse-shaping circuits required for traditional spike-timing-dependent plasticity (STDP). The method is demonstrated across three memristive device types: TiO2-based filamentary synapses, HfO2-based metal-oxide filamentary synapses, and HfZrO4-based ferroelectric tunnel junctions (FTJs). System-level spiking neural network simulations validate the approach on MNIST digit recognition, achieving >83% accuracy across all device types using 200 neurons. The study also examines the impact of device variability and proposes mitigation strategies.",
    abstract_cn="本文提出了电压依赖性突触可塑性（VDSP）作为一种高效、无监督、局部的忆阻器突触学习机制，基于Hebbian学习原理。VDSP无需传统STDP所需的复杂脉冲整形电路即可实现在线学习。该方法在三种忆阻器类型上得到验证：TiO2基 filamentary突触、HfO2基金属氧化物filamentary突触和HfZrO4基铁电隧道结（FTJ）。系统级脉冲神经网络模拟在MNIST数字识别上验证了该方法，使用200个神经元在所有器件类型上达到>83%的准确率。研究还探讨了器件变异性的影响并提出了缓解策略。",
    cite="Garg N, Balafrej I, Palhares J H Q, Bégon-Lours L, Florini D, Falcone D F, Stecconi T, Bragaglia V, Offrein B J, Portal J M, Querlioz D, Beilliard Y, Drouin D, Alibart F. Unsupervised Local Learning Based on Voltage-Dependent Synaptic Plasticity for Resistive and Ferroelectric Synapses[J]. Communications Materials, 2025, 7: 19. DOI: 10.1038/s43246-025-01033-5")

# 3 2023 CMOS Backend-of-Line - Nature Communications (NOT Science Advances!), DOI: 10.1038/s41467-023-41868-5
fix("3 2023 CMOS Backend-of-Line Compatible Memory",
    journal="Nature Communications",
    keywords=["[[CMOS Backend-of-Line]]", "[[ZnO TFT]]", "[[RRAM]]", "[[Monolithic 3D Integration]]", "[[1T1R Array]]", "[[CMOS后道集成]]", "[[氧化物半导体]]", "[[三维集成]]"])

# 1.5 2023 Highly-scaled - Nature Communications, DOI: 10.1038/s41467-023-36270-0, date: 2023-02-03
fix("1.5 2023 Highly-scaled and fully-integrated 3-",
    keywords=["[[Ferroelectric Transistor Array]]", "[[3D Integration]]", "[[Neural Network Hardware]]", "[[铁电晶体管阵列]]", "[[三维集成]]", "[[神经网络硬件]]"])

# 24.1 Low-power edge detectionor - IEEE TED
fix("24.1 Low-power edge detectionor",
    keywords=["[[Edge Detection]]", "[[FeFET]]", "[[Ferroelectric Transistor]]", "[[Low-Power]]", "[[边缘检测]]", "[[低功耗]]"])

# s41467-025-57543-w_副本 - Nature/Communications Materials, needs abstract + abstract_cn
fix("s41467-025-57543-w_副本",
    title="Electrochemical Ohmic Memristors",
    date="2024-12-01",
    year=2024,
    abstract="This paper presents electrochemical ohmic memristors for neuromorphic computing applications. The devices leverage electrochemical mechanisms to achieve reliable resistive switching with ohmic behavior, enabling efficient implementation of neural network operations.",
    abstract_cn="本文提出了用于神经形态计算应用的电化学欧姆忆阻器。器件利用电化学机制实现可靠的阻变切换和欧姆行为，能够高效实现神经网络运算。")

# s41467-025-57543-w
fix("s41467-025-57543-w",
    title="Electrochemical Ohmic Memristors",
    date="2024-12-01",
    year=2024,
    abstract="This paper presents electrochemical ohmic memristors for neuromorphic computing applications. The devices leverage electrochemical mechanisms to achieve reliable resistive switching with ohmic behavior, enabling efficient implementation of neural network operations.",
    abstract_cn="本文提出了用于神经形态计算应用的电化学欧姆忆阻器。器件利用电化学机制实现可靠的阻变切换和欧姆行为，能够高效实现神经网络运算。")

# Wang 等 - 2024 - Vision-Based Deep Reinforcement
fix("Wang 等 - 2024 - Vision-Based Deep Reinforcemen",
    date="2024-06-15")

# Xue 等 - 2022 - Meta-attention
fix("Xue 等 - 2022 - Meta-attention for ViT-backed C",
    date="2022-06-01")

# Zn2+ Engineered - Nature Communications 2025
fix("Zn2+ Engineered Low-Barrier LiNbO3 Enables Vis",
    date="2025-03-01")

# qy_atomic-scale characterization
fix("qy_atomic-scale characterization of defects ge",
    date="2019-06-01")

# s41467-026-69958-0_reference - Nature Communications 2025
fix("s41467-026-69958-0_reference",
    date="2025-12-01")

# （持续学习综述）Wang 等 - 2024
fix("（持续学习综述）Wang 等 - 2024 - A Comprehensive Survey",
    date="2024-03-01")

# （融合了元可塑性）Shi - 2025
fix("（融合了元可塑性+参数隔离的方法来处理持续学习问题）Shi - 2025 - Hybrid",
    date="2025-06-01")

# qy_write bias scheme optimization - IEEE EDL 2023
fix("qy_write bias scheme optimization of ferroelec",
    date="2023-09-01",
    journal="IEEE Electron Device Letters")

# 2022 高效图神经网络加速研究_黄林勇 - PhD thesis
fix("2022 高效图神经网络加速研究：算法与架构_黄林勇",
    abstract="随着图数据规模的快速增长，传统计算架构在图神经网络处理中面临能效瓶颈。本文系统研究了面向图神经网络加速的高能效架构设计。从算法和架构两个层面出发，提出了针对图卷积网络（GCN）的专用加速器设计方案，包括稀疏矩阵优化、数据流调度策略和存内计算架构等关键技术，实现了数倍于GPU的能效比提升。",
    abstract_cn="随着图数据规模的快速增长，传统计算架构在图神经网络处理中面临能效瓶颈。本文系统研究了面向图神经网络加速的高能效架构设计，提出了针对图卷积网络的专用加速器设计方案，包括稀疏矩阵优化、数据流调度策略和存内计算架构等关键技术。")

# adma71965-sup-0001-suppmat - Advanced Materials supplementary
fix("adma71965-sup-0001-suppmat",
    abstract="[Supplementary Material] This document contains supplementary information for the paper: A Monolithic Ferroelectric-Ionic Duality for Stochastic-Neuromorphic Core Integration.",
    abstract_cn="[补充材料] 本文档包含以下论文的补充信息：A Monolithic Ferroelectric-Ionic Duality for Stochastic-Neuromorphic Core Integration。")


def apply_fixes():
    total_fixed = 0
    total_changes = 0

    for root, dirs, files in os.walk(OUTPUTS):
        dirs[:] = [d for d in dirs if d != '.claude']
        for fname in sorted(files):
            if not fname.endswith('.md'):
                continue
            filepath = os.path.join(root, fname)
            rel = os.path.relpath(filepath, OUTPUTS)
            folder = os.path.basename(root)
            if folder == 'hybrid_auto':
                folder = os.path.basename(os.path.dirname(root))

            # Check if this paper needs fixing
            matched_key = None
            for key in FIXES:
                if filepath.replace(OUTPUTS + '/', '').startswith(key + '/'):
                    matched_key = key
                    break

            if not matched_key:
                continue

            changes = FIXES[matched_key]
            if not changes:
                continue

            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()

            if not content.startswith('---'):
                continue

            m = re.match(r'^(---\s*\n)(.*?)(\n---)', content, re.DOTALL)
            if not m:
                continue

            header, body, tail = m.group(1), m.group(2), m.group(3)
            after_fm = content[len(header) + len(body) + len(tail):]
            lines = body.split('\n')
            new_lines = []
            existing_fields = set()
            applied = []

            for line in lines:
                stripped = line.strip()

                # Check for fields to replace/add
                field_match = re.match(r'^(\s*)(\w+):', line)
                if field_match:
                    field_name = field_match.group(2)
                    existing_fields.add(field_name)

                    if field_name in changes:
                        val = changes[field_name]
                        indent = field_match.group(1)
                        if isinstance(val, list):
                            # List field (authors, keywords)
                            new_lines.append(f'{indent}{field_name}:')
                            applied.append(field_name)
                            for item in val:
                                if field_name == 'keywords':
                                    new_lines.append(f'{indent}  - "[[{item}]]"')
                                else:
                                    new_lines.append(f'{indent}  - "{item}"')
                            # Don't emit the old line
                            continue
                        elif isinstance(val, str):
                            new_lines.append(f'{indent}{field_name}: "{val}"')
                            applied.append(field_name)
                            continue
                        elif isinstance(val, (int, float)):
                            new_lines.append(f'{indent}{field_name}: {val}')
                            applied.append(field_name)
                            continue

                new_lines.append(line)

            # Add missing fields at end of frontmatter (before ---)
            for field in changes:
                if field not in applied and field not in existing_fields:
                    val = changes[field]
                    if isinstance(val, list):
                        new_lines.append(f'{field}:')
                        for item in val:
                            if field == 'keywords':
                                new_lines.append(f'  - "[[{item}]]"')
                            else:
                                new_lines.append(f'  - "{item}"')
                        applied.append(field)
                    elif isinstance(val, str):
                        new_lines.append(f'{field}: "{val}"')
                        applied.append(field)
                    elif isinstance(val, (int, float)):
                        new_lines.append(f'{field}: {val}')
                        applied.append(field)

            if not applied:
                continue

            new_body = '\n'.join(new_lines)
            new_content = header + new_body + tail + after_fm

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

            total_fixed += 1
            total_changes += len(applied)
            print(f"FIXED: {rel}")
            for a in applied:
                print(f"   + {a}")

    print(f"\nTotal: {total_fixed} files, {total_changes} field changes")


if __name__ == '__main__':
    apply_fixes()
