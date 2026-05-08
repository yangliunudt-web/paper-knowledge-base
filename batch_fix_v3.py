#!/usr/bin/env python3
"""v3: Complete frontmatter rewrite for problematic papers."""

import os, re

OUTPUTS = "/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/Outputs"

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def build_frontmatter(fields):
    """Build YAML frontmatter from field dict."""
    lines = ['---']
    for key, val in fields.items():
        if val is None:
            continue
        if isinstance(val, list):
            lines.append(f'{key}:')
            for item in val:
                lines.append(f'  - "{item}"')
        elif isinstance(val, str):
            # Escape double quotes in content
            escaped = val.replace('\\', '\\\\').replace('"', '\\"')
            lines.append(f'{key}: "{escaped}"')
        elif isinstance(val, (int, float)):
            lines.append(f'{key}: {val}')
        elif isinstance(val, bool):
            lines.append(f'{key}: {"true" if val else "false"}')
    lines.append('---')
    return '\n'.join(lines) + '\n'


# ===== Paper 1: 2022 高效图神经网络加速研究 =====
fix_file1 = os.path.join(OUTPUTS, "2022 高效图神经网络加速研究：算法与架构_黄林勇/hybrid_auto/高效图神经网络加速研究：算法与架构.md")
if os.path.exists(fix_file1):
    content = read_file(fix_file1)
    body = content.split('\n---\n', 1)[1] if '\n---\n' in content else ''
    # Remove old frontmatter
    body = body.split('\n---\n', 1)[-1] if body.startswith('---') else body
    fm = build_frontmatter({
        'title': '高效图神经网络加速研究：算法与架构',
        'authors': ['黄林勇'],
        'date': '2022-06-01',
        'year': 2022,
        'journal': '博士学位论文',
        'type': 'thesis',
        'keywords': ['[[图神经网络]]', '[[加速器]]', '[[存内计算]]', '[[稀疏矩阵]]', '[[Graph Neural Network]]', '[[Accelerator]]'],
        'abstract': '随着图数据规模的快速增长，传统计算架构在图神经网络处理中面临能效瓶颈。本文系统研究了面向图神经网络加速的高能效架构设计，从算法和架构两个层面出发，提出了针对图卷积网络（GCN）的专用加速器设计方案，包括稀疏矩阵优化、数据流调度策略和存内计算架构等关键技术，实现了数倍于GPU的能效比提升。',
        'abstract_cn': '随着图数据规模的快速增长，传统计算架构在图神经网络处理中面临能效瓶颈。本文系统研究了面向图神经网络加速的高能效架构设计，从算法和架构两个层面出发，提出了针对图卷积网络（GCN）的专用加速器设计方案，包括稀疏矩阵优化、数据流调度策略和存内计算架构等关键技术，实现了数倍于GPU的能效比提升。',
        'cite': '黄林勇. 高效图神经网络加速研究：算法与架构[D]. 博士学位论文, 2022.',
        'aiSum': '本文系统研究了面向图神经网络加速的高能效架构设计，提出了针对GCN的专用加速器方案，包括稀疏矩阵优化、数据流调度和存内计算等关键技术。',
    })
    new_content = fm + '\n' + body.lstrip('\n')
    write_file(fix_file1, new_content)
    print(f"FIXED: 2022 高效图神经网络加速研究")

# ===== Paper 2: 26 ma-et-al-2025 =====
fix_file2 = os.path.join(OUTPUTS, "26 ma-et-al-2025-van-der-waals-engineering-of-/hybrid_auto/Van der Waals Engineering of One-Transistor-One-Ferroelectric-Memristor Architecture for an Energy-Efficient Neuromorphic Array.md")
if os.path.exists(fix_file2):
    content = read_file(fix_file2)
    body_parts = content.split('\n---\n', 2)
    body = body_parts[-1] if len(body_parts) > 1 else ''
    fm = build_frontmatter({
        'title': 'Van der Waals Engineering of One-Transistor-One-Ferroelectric-Memristor Architecture for an Energy-Efficient Neuromorphic Array',
        'authors': ['Yinchang Ma', 'Maolin Chen', 'Fernando Aguirre', 'Yuan Yan', 'Sebastian Pazos', 'Chen Liu', 'Heng Wang', 'Tao Yang', 'Baoyu Wang', 'Cheng Gong', 'Kai Liu', 'Jefferson Zhe Liu', 'Mario Lanza', 'Fei Xue', 'Xixiang Zhang'],
        'date': '2025-02-03',
        'year': 2025,
        'journal': 'Nano Letters',
        'keywords': ['[[Van der Waals]]', '[[FeFET]]', '[[Memristor]]', '[[Neuromorphic Array]]', '[[CuCrP2S6]]', '[[1T1M]]', '[[范德华]]', '[[神经形态阵列]]'],
        'abstract': 'This work demonstrates a fully van der Waals assembled 1T1M (one-transistor-one-memristor) architecture, stacking two-dimensional ferroelectric CuCrP2S6 with MoS2 and h-BN. The device achieves ultra-low leakage current of ~120 fA at Vtg=-3V, ultra-high resistance tunability of ~10^6, and ultra-low static power consumption of only 12 fW. It is electroforming-free with operating voltage below 1V. A neuromorphic array with crosstalk reduction of 2 orders of magnitude was demonstrated, and a simulated 256x10 ANN achieves 90% image recognition accuracy with only 12.77 uW power consumption.',
        'abstract_cn': '本文展示了一种全范德华组装的1T1M架构，将二维铁电CuCrP2S6与MoS2和h-BN堆叠组装。器件实现~120 fA超低漏电流、~10^6超高阻态可调性和仅12 fW的超低静态功耗。无需电铸工艺，操作电压低于1V。实验演示了串扰降低2个数量级的神经形态阵列，模拟的256x10人工神经网络实现90%图像识别准确率，功耗仅12.77 uW。',
        'cite': 'Ma Y, Chen M, Aguirre F, Yan Y, Pazos S, Liu C, Wang H, Yang T, Wang B, Gong C, Liu K, Liu J Z, Lanza M, Xue F, Zhang X. Van der Waals Engineering of One-Transistor-One-Ferroelectric-Memristor Architecture for an Energy-Efficient Neuromorphic Array[J]. Nano Letters, 2025, 25(6): 2510-2519. DOI: 10.1021/acs.nanolett.4c06118',
        'aiSum': '本文展示了全范德华组装的1T1M架构，CuCrP2S6/MoS2/h-BN堆叠。器件实现120 fA漏电流、10^6阻态可调性、12 fW功耗、<1V操作电压。神经形态阵列串扰降低2个数量级，256x10 ANN图像识别准确率90%，功耗12.77 uW。',
    })
    new_content = fm + '\n' + body.lstrip('\n')
    write_file(fix_file2, new_content)
    print(f"FIXED: 26 ma-et-al-2025")

# ===== Paper 3: lomenzo-et-al-2024 =====
fix_file3 = os.path.join(OUTPUTS, "lomenzo-et-al-2024-ferroelectric-al0-85sc0-15n/hybrid_auto/Ferroelectric $mathbf { A l } _ { 0 . 8 5 } mathsf { S c } _ { 0 . 1 5 } mathsf { N }$ and $mathsf { H f } _ { 0 . 5 } mathsf { Z r } _ { 0 . 5 } mathsf { O } _ { 2 }$ Domain Switching Dynamics.md")
if os.path.exists(fix_file3):
    content = read_file(fix_file3)
    body_parts = content.split('\n---\n', 2)
    body = body_parts[-1] if len(body_parts) > 1 else ''
    fm = build_frontmatter({
        'title': 'Ferroelectric Al0.85Sc0.15N and Hf0.5Zr0.5O2 Domain Switching Dynamics',
        'authors': ['Roberto Guido', 'Xuetao Wang', 'Bohan Xu', 'Ruben Alcala', 'Thomas Mikolajick', 'Uwe Schroeder', 'Patrick D. Lomenzo'],
        'date': '2024-07-31',
        'year': 2024,
        'journal': 'ACS Applied Materials & Interfaces',
        'keywords': ['[[Ferroelectric]]', '[[Domain Switching]]', '[[AlScN]]', '[[HfZrO2]]', '[[FeFET]]', '[[铁电材料]]', '[[畴切换动力学]]'],
        'abstract': 'This work uses transient current integration measurements to compare domain switching dynamics in two leading ferroelectric thin-film systems: Al0.85Sc0.15N and Hf0.5Zr0.5O2. Al0.85Sc0.15N switching is dominated by thermally activated creep domain wall motion, benefiting from c-axis texture for homogeneous local switching field, but suffers from domain wall pinning upon bipolar cycling. Hf0.5Zr0.5O2 is characterized by independently nucleating domains and domain wall creep, with inhomogeneous local switching field due to polymorphism and grain boundaries. The paper addresses multibit memory applications for high-density crossbar arrays targeting edge neural network inference.',
        'abstract_cn': '本文使用瞬态电流积分测量方法比较了Al0.85Sc0.15N和Hf0.5Zr0.5O2两种主流铁电薄膜系统的畴切换动力学。Al0.85Sc0.15N的切换主要由热激活蠕变畴壁运动主导，受益于c轴织构，但在双极循环中会出现畴壁钉扎。Hf0.5Zr0.5O2的特征在于独立成核的畴和畴壁蠕变，由于多晶型和晶界导致局部切换场不均匀。本文直接针对高密度crossbar阵列的多比特存储应用。',
        'cite': 'Guido R, Wang X, Xu B, Alcala R, Mikolajick T, Schroeder U, Lomenzo P D. Ferroelectric Al0.85Sc0.15N and Hf0.5Zr0.5O2 Domain Switching Dynamics[J]. ACS Applied Materials & Interfaces, 2024, 16(32): 42415-42425. DOI: 10.1021/acsami.4c05798',
        'aiSum': '本文比较了Al0.85Sc0.15N和Hf0.5Zr0.5O2两种铁电体系的畴切换动力学。AlScN受热激活蠕变畴壁运动主导，HfZrO2以独立成核畴为特征。研究针对高密度crossbar阵列中面向边缘神经网络推理的多比特存储应用。',
    })
    new_content = fm + '\n' + body.lstrip('\n')
    write_file(fix_file3, new_content)
    print(f"FIXED: lomenzo-et-al-2024")

# ===== Papers 4-14: fix with full rewrites =====
papers = [
    ("s41467-020-16108-9/hybrid_auto/Accurate deep neural network inference using computational phase-change memory.md", {
        'title': 'Accurate Deep Neural Network Inference Using Computational Phase-Change Memory',
        'authors': ['Vinay Joshi', 'Manuel Le Gallo', 'Simon Haefeli', 'Irem Boybat', 'S. R. Nandakumar', 'Christophe Piveteau', 'Martino Dazzi', 'Bipin Rajendran', 'Abu Sebastian', 'Evangelos Eleftheriou'],
        'date': '2020-05-18', 'year': 2020, 'journal': 'Nature Communications',
        'keywords': ['[[In-Memory Computing]]', '[[Phase-Change Memory]]', '[[Deep Learning]]', '[[CIFAR-10]]', '[[ImageNet]]', '[[存内计算]]', '[[相变存储器]]'],
        'abstract': 'In-memory computing using resistive memory devices is a promising non-von Neumann approach for making energy-efficient deep learning inference hardware. We introduce a methodology to train ResNet-type CNNs that results in no appreciable accuracy loss when transferring weights to phase-change memory (PCM) devices. We also propose a compensation technique exploiting batch normalization parameters to improve accuracy retention over time. We achieve 93.7% accuracy on CIFAR-10 and 71.6% top-1 accuracy on ImageNet after mapping trained weights to PCM. Hardware results demonstrate 93.5% accuracy on CIFAR-10 with ResNet-32, the highest reported for analog resistive memory hardware.',
        'abstract_cn': '使用电阻式存储器件进行存内计算是实现高能效深度学习推理硬件的一种有前景的非冯·诺依曼方法。我们提出了一种训练ResNet型CNN的方法，将权重转移到相变存储器时不会产生精度损失，并提出利用批归一化参数改善精度保持的补偿技术。在CIFAR-10上达到93.7%准确率，ImageNet上71.6%的Top-1准确率。硬件结果展示93.5% CIFAR-10准确率，为模拟电阻式存储硬件最高。',
        'cite': 'Joshi V, Le Gallo M, Haefeli S, Boybat I, Nandakumar S R, Piveteau C, Dazzi M, Rajendran B, Sebastian A, Eleftheriou E. Accurate Deep Neural Network Inference Using Computational Phase-Change Memory[J]. Nature Communications, 2020, 11: 2473. DOI: 10.1038/s41467-020-16108-9',
        'aiSum': '本文提出训练ResNet型CNN映射到PCM器件的方法，利用批归一化补偿技术保持精度。在CIFAR-10上实现93.7%（软件）/93.5%（硬件）准确率，ImageNet Top-1达71.6%，为模拟电阻式存储硬件最高精度。',
    }),
    ("s41467-025-65151-x/hybrid_auto/Photonic edge intelligence chip for multimodal sensing, inference and learning.md", {
        'title': 'Photonic Edge Intelligence Chip for Multi-Modal Sensing, Inference and Learning',
        'authors': ['Shiji Zhang', 'Xueyi Jiang', 'Bo Wu', 'Haojun Zhou', 'Wenguang Xu', 'Hailong Zhou', 'Zhichao Ruan', 'Jianji Dong', 'Xinliang Zhang'],
        'date': '2025-11-19', 'year': 2025, 'journal': 'Nature Communications',
        'keywords': ['[[Photonic Chip]]', '[[Edge Intelligence]]', '[[AWG]]', '[[Multi-Modal]]', '[[光子芯片]]', '[[边缘智能]]', '[[多模态]]'],
        'abstract': 'This work demonstrates a Photonic Edge Intelligence Chip (PEIC) that fuses multiple analog modalities—images, spectra, and RF signals—into broad optical spectra for single-fiber input, enabling direct analog processing. The chip uses an Arrayed Waveguide Grating for simultaneous spectral sensing and energy-efficient convolution (29 fJ/OP), followed by a nonlinear activation and fully connected layer forming an end-to-end optical neural network. On-chip inference achieves 1.33 ns response time across three modalities: drug spectral recognition, image classification, and radar target classification.',
        'abstract_cn': '本文展示了一款光子边缘智能芯片，将图像、光谱和射频信号等多种模拟模态融合到宽光谱中实现单光纤输入，无需数字转换即可直接进行模拟处理。芯片利用阵列波导光栅实现同步光谱感知和高能效卷积（29 fJ/OP），构成端到端光学神经网络。片上推理实测响应时间为1.33纳秒，在药物光谱识别、图像分类和雷达目标分类三种模态上进行了验证。',
        'cite': 'Zhang S, Jiang X, Wu B, Zhou H, Xu W, Zhou H, Ruan Z, Dong J, Zhang X. Photonic Edge Intelligence Chip for Multi-Modal Sensing, Inference and Learning[J]. Nature Communications, 2025, 16: 10136. DOI: 10.1038/s41467-025-65151-x',
        'aiSum': '本文展示光子边缘智能芯片PEIC，融合图像/光谱/RF多模态，AWG实现29 fJ/OP卷积，1.33 ns推理延迟。在药物识别、图像分类和雷达分类三种任务上的感知-计算一体化验证。',
    }),
    ("s41598-020-78944-5/hybrid_auto/Combinatorial optimization by weight annealing in memristive hopfeld networks.md", {
        'title': 'Combinatorial Optimization by Weight Annealing in Memristive Hopfield Networks',
        'authors': ['Z. Fahimi', 'M. R. Mahmoodi', 'H. Nili', 'Valentin Polishchuk', 'D. B. Strukov'],
        'date': '2021-08-12', 'year': 2021, 'journal': 'Scientific Reports',
        'keywords': ['[[Hopfield Network]]', '[[Memristor]]', '[[Combinatorial Optimization]]', '[[Weight Annealing]]', '[[忆阻器]]', '[[组合优化]]'],
        'abstract': 'The Hopfield neural network is a powerful framework for solving combinatorial optimization problems. We propose a weight annealing approach: initially setting all synaptic weights to zero allows the network to quickly settle into its trivial global-minimum state, then gradually introducing the weights keeps the network close to its ground state. Extensive simulations show weight annealing yields better solutions on average for several representative combinatorial optimization problems. As proof of concept, we experimentally solve a 13-node graph partitioning problem using a 20x20 TiO2 memristive crossbar and a 7-node maximum-weight independent set problem using a 12x10 eFlash memory array.',
        'abstract_cn': 'Hopfield神经网络是解决组合优化问题的强大框架。我们提出了一种权重退火方法：初始将所有突触权重设为零使网络快速进入全局最小状态，然后逐渐引入权重使网络保持在基态附近。大量模拟表明权重退火在多个组合优化问题上平均能获得更好的解。作为概念验证，使用20x20 TiO2忆阻器crossbar实验解决了13节点图划分问题，使用12x10 eFlash阵列解决了7节点最大权重独立集问题。',
        'cite': 'Fahimi Z, Mahmoodi M R, Nili H, Polishchuk V, Strukov D B. Combinatorial Optimization by Weight Annealing in Memristive Hopfield Networks[J]. Scientific Reports, 2021, 11: 16383. DOI: 10.1038/s41598-020-78944-5',
        'aiSum': '本文提出权重退火方法用于忆阻器Hopfield网络的组合优化。初始权重为零使网络快速进入全局最小，逐渐引入权重保持基态。在TiO2 crossbar和eFlash阵列上实验验证了图划分和最大独立集问题。',
    }),
    ("science.adv7434/hybrid_auto/PHOTONIC COMPUTI NG.md", {
        'title': 'All-Optical Synthesis Chip for Large-Scale Intelligent Semantic Vision Generation',
        'authors': ['Yitong Chen', 'Xinyue Sun', 'Guangtao Zhai', 'Wenjun Zhang'],
        'date': '2024-12-19', 'year': 2024, 'journal': 'Science',
        'keywords': ['[[All-Optical Chip]]', '[[Generative AI]]', '[[LightGen]]', '[[NeRF]]', '[[全光芯片]]', '[[生成式AI]]'],
        'abstract': 'This paper presents LightGen, the first large-scale all-optical generative AI chip simultaneously breaking through three bottlenecks: million-scale optical neuron integration, all-optical dimension conversion, and ground-truth-free optical chip training. The chip achieves 2 orders of magnitude improvement in computing power and energy efficiency versus state-of-the-art digital chips, with theoretical potential for 7 orders of magnitude if signal input is not the bottleneck. LightGen supports high-resolution image semantic generation, 3D NeRF generation, HD video generation, semantic control, denoising, and style transfer.',
        'abstract_cn': '本文提出了LightGen，首款大规模全光生成式AI芯片，同时突破百万级光学神经元集成、全光维度转换和无真值光芯片训练三大瓶颈。相比顶尖数字芯片实现2个数量级的算力和能效提升，理论上可达7个数量级。支持高分辨率图像语义生成、3D NeRF、高清视频生成、语义调控、去噪和风格迁移。',
        'cite': 'Chen Y, Sun X, Zhai G, Zhang W. All-Optical Synthesis Chip for Large-Scale Intelligent Semantic Vision Generation[J]. Science, 2024, 386: 1480-1487. DOI: 10.1126/science.adv7434',
        'aiSum': 'LightGen全光生成式AI芯片，突破百万级光学神经元集成、全光维度转换、无真值训练三大瓶颈。算力提升2个数量级（理论7个），支持NeRF、视频生成、风格迁移等任务。',
    }),
    ("scirobotics.abb9764/hybrid_auto/A R T I F I C I A L I N T E L L I G E N C E.md", {
        'title': 'An Adaptive Deep Reinforcement Learning Framework Enables Curling Robots with Human-Like Performance in Real-World Conditions',
        'authors': ['Dong-Ok Won', 'Klaus-Robert Müller', 'Seong-Whan Lee'],
        'date': '2020-09-23', 'year': 2020, 'journal': 'Science Robotics',
        'keywords': ['[[Deep Reinforcement Learning]]', '[[Robotics]]', '[[Curling]]', '[[深度强化学习]]', '[[机器人]]'],
        'abstract': 'The game of curling can be considered a good test bed for studying AI-real world interaction. We report a curling robot, Curly, that uses an adaptive deep reinforcement learning framework to achieve human-level performance. Curly won three out of four official matches against top-ranked South Korean women\'s curling teams and the Korea national wheelchair curling team. The framework extends standard DRL with temporal features to compensate for real-world uncertainties and nonstationarities inherent to the sport.',
        'abstract_cn': '冰壶运动是研究AI与现实世界交互的良好测试平台。我们报道了Curly冰壶机器人，使用自适应深度强化学习框架实现人类水平的表现。Curly在与韩国顶尖女子冰壶队和轮椅冰壶队的四场正式比赛中赢得三场。该框架扩展了标准DRL，加入时间特征补偿冰壶运动的不确定性和非平稳性。',
        'cite': 'Won D O, Müller K R, Lee S W. An Adaptive Deep Reinforcement Learning Framework Enables Curling Robots with Human-Like Performance in Real-World Conditions[J]. Science Robotics, 2020, 5(46): eabb9764. DOI: 10.1126/scirobotics.abb9764',
        'aiSum': 'Curly冰壶机器人使用自适应DRL框架，加入时间特征补偿现实不确定性。在与韩国顶尖队伍的四场正式比赛中三胜，展示了DRL在高度不确定现实条件下的有效性。',
    }),
    ("s40820-025-01968-x/hybrid_auto/Ferroelectric Optoelectronic Sensor for Intelligent Flame Detection and In-Sensor Motion Perception.md", {
        'title': 'Ferroelectric Optoelectronic Sensor for Intelligent Flame Detection and In-Sensor Motion Perception',
        'authors': ['Jiayun Wei', 'Guokun Ma', 'Runzhi Liang', 'Wenxiao Wang', 'Hao Wang', 'Wei Han', 'Liangping Shen', 'Longhui Zeng'],
        'date': '2026-01-13', 'year': 2026, 'journal': 'Nano-Micro Letters',
        'keywords': ['[[Optoelectronic Sensor]]', '[[Ferroelectric]]', '[[Ga2O3]]', '[[Flame Detection]]', '[[In-Sensor Computing]]', '[[光电传感器]]', '[[火焰检测]]'],
        'abstract': 'This work demonstrates a Ga2O3/In2Se3 ferroelectric-optoelectronic heterojunction sensor array (5x5 pixels) for intelligent flame detection and in-sensor motion perception. Through ferroelectric polarization modulation, the sensor achieves a detectivity of 4.91x10^17 Jones at 255 nm solar-blind UV light, at the forefront of Ga2O3-based UV detectors. Combined with NB-IoT for real-time cloud and mobile alarm, a lightweight CNN achieves 96.47% flame motion recognition, and a photosensitive ANN achieves 90.51% recognition for extremely weak early-stage flame UV light.',
        'abstract_cn': '本文展示了一种Ga₂O₃/In₂Se₃铁电-光电异质结传感器阵列（5x5像素），用于智能火焰检测和传感器内运动感知。通过铁电极化调控，传感器在255 nm日盲紫外光下探测率达4.91×10¹⁷ Jones。结合NB-IoT模块实现实时报警，轻量级CNN实现96.47%火焰运动识别，光敏ANN对极弱早期火焰紫外光识别率达90.51%。',
        'cite': 'Wei J, Ma G, Liang R, Wang W, Wang H, Han W, Shen L, Zeng L. Ferroelectric Optoelectronic Sensor for Intelligent Flame Detection and In-Sensor Motion Perception[J]. Nano-Micro Letters, 2026, 18: 123. DOI: 10.1007/s40820-025-01968-x',
        'aiSum': 'Ga₂O₃/In₂Se₃铁电-光电传感器阵列，255 nm紫外探测率4.91×10¹⁷ Jones。NB-IoT云端报警+CNN 96.47%火焰运动识别+ANN 90.51%极弱光火焰识别，实现全时段智能火焰检测。',
    }),
    ("s41467-025-58359-4/hybrid_auto/In-memory ferroelectric differentiator.md", {
        'title': 'In-Memory Ferroelectric Differentiator',
        'authors': ['Guangdi Feng', 'Xiaoming Zhao', 'Xiaoyue Huang', 'Xiaoxu Zhang', 'Yangyang Wang', 'Wei Li', 'Luqiu Chen', 'Shenglan Hao', 'Qiuxiang Zhu', 'Yachin Ivry', 'Brahim Dkhil', 'Bobo Tian', 'Peng Zhou', 'Junhao Chu', 'Chungang Duan'],
        'date': '2025-03-28', 'year': 2025, 'journal': 'Nature Communications',
        'keywords': ['[[Ferroelectric]]', '[[Differentiator]]', '[[In-Memory Computing]]', '[[Crossbar Array]]', '[[P(VDF-TrFE)]]', '[[铁电材料]]', '[[存内计算]]'],
        'abstract': 'This work develops an in-memory ferroelectric differentiator using a 40x40 passive crossbar array of 1,600 ferroelectric P(VDF-TrFE) polymer capacitors. By exploiting ferroelectric domain reversal dynamics, differential computation is performed directly within memory. Key achievements: 0.24 fJ per calculation, 1 MHz operation, >5 day retention, 98.9% moving object extraction accuracy, and 4.17 POPS/W ideal computational efficiency (10,000x higher than NVIDIA V100 GPU). First- and second-order derivatives, motion extraction, and image discrepancy identification were demonstrated.',
        'abstract_cn': '本文开发了一种存内铁电差分器，使用由1600个P(VDF-TrFE)铁电聚合物电容组成的40×40无源crossbar阵列。利用铁电畴反转动态行为直接在存储器内执行微分计算。关键指标：0.24 fJ/次计算，1 MHz工作，>5天保持，98.9%运动提取准确率，4.17 POPS/W理想计算效率（比V100 GPU高10,000倍）。成功演示了一阶和二阶导数求解、运动提取和图像差异识别。',
        'cite': 'Feng G, Zhao X, Huang X, Zhang X, Wang Y, Li W, Chen L, Hao S, Zhu Q, Ivry Y, Dkhil B, Tian B, Zhou P, Chu J, Duan C. In-Memory Ferroelectric Differentiator[J]. Nature Communications, 2025, 16: 3027. DOI: 10.1038/s41467-025-58359-4',
        'aiSum': '开发40x40 P(VDF-TrFE)铁电电容crossbar存内差分器。0.24 fJ/次、1 MHz、98.9%准确率、4.17 POPS/W（比V100高10000倍）。演示一阶/二阶导数、运动提取和图像差异识别。',
    }),
    ("s41467-025-68206-1_reference/hybrid_auto/Coupled ferroelectric-anisotropic optoelectronic synapse for polarization-sensitive neuromorphic vision.md", {
        'title': 'Coupled Ferroelectric-Anisotropic Optoelectronic Synapse for Polarization-Sensitive Neuromorphic Vision',
        'authors': ['Jiali Huo', 'Jinpeng Huo', 'Jing Gao', 'Lingqi Li', 'Thaw Tint Te Tun', 'Jin Peng', 'Haofei Zheng', 'Yufei Shi', 'Kah-Wee Ang'],
        'date': '2026-01-08', 'year': 2026, 'journal': 'Nature Communications',
        'keywords': ['[[Optoelectronic Synapse]]', '[[Ferroelectric]]', '[[ReS2]]', '[[HZO]]', '[[Polarization]]', '[[Neuromorphic Vision]]', '[[光电突触]]', '[[神经形态视觉]]'],
        'abstract': 'This paper presents a polarization-resolved optoelectronic synapse integrating polarization-sensitive photodetection and non-volatile memory in a single device. A 2D ReS2 channel combined with Hf0.5Zr0.5O2 gate dielectric forms an MFMIS FeFET. Co-modulation of ferroelectric polarization and photoexcited carrier trapping enables high responsivity and long-term optoelectronic retention. An ANN achieves 97.33% iris recognition accuracy under unpolarized light, and a 3x3 FeFET-based CNN performs butterfly classification via polarization-resolved feature extraction, with 2.0 fJ per event energy efficiency.',
        'abstract_cn': '本文提出了一种偏振分辨光电突触，在单个器件中集成偏振敏感光电检测和非易失性存储。采用2D ReS2沟道结合Hf0.5Zr0.5O2栅介质构成MFMIS FeFET。铁电极化与光生载流子捕获的协同调控实现高响应度和长期光电保持。ANN在非偏振光下实现97.33%虹膜识别，3x3 FeFET CNN通过偏振分辨特征提取实现蝴蝶分类，能效达2.0 fJ/事件。',
        'cite': 'Huo J, Huo J, Gao J, Li L, Tun T T T, Peng J, Zheng H, Shi Y, Ang K W. Coupled Ferroelectric-Anisotropic Optoelectronic Synapse for Polarization-Sensitive Neuromorphic Vision[J]. Nature Communications, 2026, 17: 1468. DOI: 10.1038/s41467-025-68206-1',
        'aiSum': '偏振分辨光电突触，ReS2/HZO MFMIS FeFET结构。ANN 97.33%虹膜识别，3x3 FeFET CNN蝴蝶分类，2.0 fJ/事件能效。铁电-各向异性平台实现偏振敏感神经形态视觉。',
    }),
    ("s43246-025-01033-5_reference/hybrid_auto/Unsupervised local learning based on voltagedependent synaptic plasticity for resistive and ferroelectric synapses.md", {
        'title': 'Unsupervised Local Learning Based on Voltage-Dependent Synaptic Plasticity for Resistive and Ferroelectric Synapses',
        'authors': ['Nikhil Garg', 'Ismael Balafrej', 'Joao Henrique Quintino Palhares', 'Laura Begon-Lours', 'Davide Florini', 'Donato Francesco Falcone', 'Tommaso Stecconi', 'Valeria Bragaglia', 'Bert Jan Offrein', 'Jean-Michel Portal', 'Damien Querlioz', 'Yann Beilliard', 'Dominique Drouin', 'Fabien Alibart'],
        'date': '2025-01-15', 'year': 2025, 'journal': 'Communications Materials',
        'keywords': ['[[Synaptic Plasticity]]', '[[Memristor]]', '[[Ferroelectric Tunnel Junction]]', '[[Unsupervised Learning]]', '[[Spiking Neural Network]]', '[[突触可塑性]]', '[[无监督学习]]'],
        'abstract': 'This paper introduces voltage-dependent synaptic plasticity (VDSP) as an efficient, unsupervised, local learning mechanism for memristive synapses grounded in Hebbian principles. VDSP enables online learning without complex pulse-shaping circuits required for STDP. Demonstrated across three memristive device types: TiO2 filamentary, HfO2 filamentary, and HfZrO4 ferroelectric tunnel junctions. SNN simulations on MNIST achieve >83% accuracy across all device types using 200 neurons. Device variability impact and mitigation strategies are examined.',
        'abstract_cn': '本文提出了电压依赖性突触可塑性（VDSP）作为一种高效、无监督、局部的忆阻器突触学习机制，基于Hebbian学习原理。VDSP无需传统STDP的复杂脉冲整形电路即可实现在线学习。在三种忆阻器类型上验证：TiO2 filamentary、HfO2 filamentary和HfZrO4铁电隧道结。SNN在MNIST上使用200个神经元在所有器件类型上达到>83%准确率。研究了器件变异性影响和缓解策略。',
        'cite': 'Garg N, Balafrej I, Palhares J H Q, Begon-Lours L, Florini D, Falcone D F, Stecconi T, Bragaglia V, Offrein B J, Portal J M, Querlioz D, Beilliard Y, Drouin D, Alibart F. Unsupervised Local Learning Based on Voltage-Dependent Synaptic Plasticity for Resistive and Ferroelectric Synapses[J]. Communications Materials, 2025, 7: 19. DOI: 10.1038/s43246-025-01033-5',
        'aiSum': '提出VDSP无监督局部学习机制，基于Hebbian原理。在TiO2、HfO2 filamentary和HfZrO4 FTJ三种器件上验证，MNIST SNN准确率>83%。无需复杂STDP脉冲电路，支持在线学习。',
    }),
    ("s41467-025-57543-w/hybrid_auto/Electrochemical ohmic memristors.md", {
        'title': 'Electrochemical Ohmic Memristors',
        'authors': ['Shaochuan Chen'],
        'date': '2024-12-01', 'year': 2024, 'journal': 'Nature Communications',
        'keywords': ['[[Memristor]]', '[[Electrochemical]]', '[[Ohmic]]', '[[Neuromorphic Computing]]', '[[忆阻器]]', '[[电化学]]'],
        'abstract': 'This paper presents electrochemical ohmic memristors for neuromorphic computing applications. The devices leverage electrochemical mechanisms to achieve reliable resistive switching with ohmic behavior, enabling efficient implementation of neural network operations.',
        'abstract_cn': '本文提出了用于神经形态计算应用的电化学欧姆忆阻器。器件利用电化学机制实现可靠的阻变切换和欧姆行为，能够高效实现神经网络运算。',
        'cite': 'Chen S et al. Electrochemical Ohmic Memristors[J]. Nature Communications, 2024. DOI: 10.1038/s41467-025-57543-w',
        'aiSum': '本文提出电化学欧姆忆阻器，利用电化学机制实现可靠阻变切换和欧姆行为，面向神经形态计算应用。',
    }),
    ("s41467-025-57543-w_副本/hybrid_auto/Electrochemical ohmic memristors for Electrochemical oh.md", {
        'title': 'Electrochemical Ohmic Memristors',
        'authors': ['Shaochuan Chen'],
        'date': '2024-12-01', 'year': 2024, 'journal': 'Nature Communications',
        'keywords': ['[[Memristor]]', '[[Electrochemical]]', '[[Ohmic]]', '[[Neuromorphic Computing]]', '[[忆阻器]]', '[[电化学]]'],
        'abstract': 'This paper presents electrochemical ohmic memristors for neuromorphic computing applications. The devices leverage electrochemical mechanisms to achieve reliable resistive switching with ohmic behavior, enabling efficient implementation of neural network operations.',
        'abstract_cn': '本文提出了用于神经形态计算应用的电化学欧姆忆阻器。器件利用电化学机制实现可靠的阻变切换和欧姆行为，能够高效实现神经网络运算。',
        'cite': 'Chen S et al. Electrochemical Ohmic Memristors[J]. Nature Communications, 2024. DOI: 10.1038/s41467-025-57543-w',
        'aiSum': '本文提出电化学欧姆忆阻器，利用电化学机制实现可靠阻变切换和欧姆行为，面向神经形态计算应用。',
    }),
]

for rel_path, fields in papers:
    filepath = os.path.join(OUTPUTS, rel_path)
    if not os.path.exists(filepath):
        print(f"NOT FOUND: {rel_path}")
        continue
    content = read_file(filepath)
    body_parts = content.split('\n---\n', 2)
    body = body_parts[-1] if len(body_parts) > 1 else ''
    fm = build_frontmatter(fields)
    new_content = fm + '\n' + body.lstrip('\n')
    write_file(filepath, new_content)
    print(f"FIXED: {os.path.basename(rel_path)}")

print("\nDone!")
