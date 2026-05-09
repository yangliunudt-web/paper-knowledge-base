---
title: Ferroelectric
type: concept
tags: [概念, 基础]
aliases: [铁电, ferroelectricity, 铁电性, ferroelectric material, ferroelectric polarization]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> 铁电性是指某些介电材料在没有外加电场时仍能保持自发极化，且极化方向可被外加电场翻转的物理性质。铁电材料是 FeFET、FeRAM 和 FTJ 等非易失存储器件的基础。

## 定义

铁电材料具有两个及以上稳定的极化态，由晶体结构中的离子位移产生电偶极矩。极化-电场（P-E）关系呈现特征性的电滞回线（hysteresis loop）。关键参数包括：剩余极化（P_r）、矫顽场（E_c）、饱和极化（P_s）。

## 关键特性

- **可翻转极化**：极化方向可被外部电场翻转，形成双稳存储
- **非易失**：断电后极化保持
- **快速切换**：极化翻转可在亚纳秒级完成
- **疲劳**：反复翻转后极化衰减，影响器件耐久性
- **铁电/反铁电**：反铁电体中相邻偶极子反平行排列，P-E 呈双回线
- **传统材料**：PZT（钙钛矿）、SBT → **新兴**：HfO₂ 基（CMOS 兼容）

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Domain switching and spatial dependence of permittivity in ferroelectric thin films\|Domain switching and spatial dependence ...]] | 1997 | 提出包含介电常数空间变化的铁电薄膜开关模型，描述 180° 和 90° 畴开关，揭示介电常数空间依赖性对矫顽场和磁滞回线形状的显著影响。 |
| [[Ferroelectric FET Based In-Memory Computing for Few-Shot Learning\|Ferroelectric FET Based In-Memory Comput...]] | 2019 | FeFET 小样本学习存内计算：模拟电导权重存储，原型网络硬件实现，边缘能效推理。 |
| [[Monte Carlo Simulation of Switching Dynamics in Polycrystalline Ferroelectric Capacitors\|Monte Carlo Simulation of Switching Dyna...]] | 2019 | 蒙特卡洛模拟多晶铁电器件开关动力学：基于成核限制开关模型，使用HZO电容器数据提取晶粒统计分布，预测任意波形下动态响应，分析铁电-电介质双层结构动态特性及器件变异导致的存储窗口缩减。 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Device Applications\|Ferroelectric Transistors for Memory and...]] | 2022 | 综述HfO2基FeFET在存储和神经形态器件中的应用：涵盖器件物理、材料工程、多值存储和突触可塑性，展望大规模商业化前景。 |
| [[Monolithic 3D Integration of High Endurance Multi-bit Ferroelectric FET\|Monolithic 3D Integration of High Endura...]] | 2022 | 单片 3D FeFET 集成：BEoL 铁电 MFM 器件，>10^10 耐久性，2 比特/单元，16kbit 阵列演示。 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Computing\|Ferroelectric Transistors for Memory and...]] | 2022 | 综述HfO2基FeFET在存储和神经形态计算中的应用：器件结构、工作原理、存储特性和突触应用。 |
| [[CMOS-compatible compute-in-memory accelerators based on integrated ferroelectric synaptic arrays for convolution neural networks\|CMOS-compatible compute-in-memory accele...]] | 2022 | FeFET突触阵列CIM加速器：三端FeFET兼存储和访问，HfZrOx/IZO <400°C制备，MNIST验证CIM功能，展示高密度CNN加速潜力。 |
| [[Highly-scaled and fully-integrated 3-dimensional ferroelectric transistor array for hardware implementation of neural networks\|Highly-scaled and fully-integrated 3-dim...]] | 2023 | 提出基于 HfZrOx 铁电晶体管的三维 NAND 阵列 (3D FeNAND) 用于神经网络硬件实现，通过沟槽结构实现高密度集成，演示了向量矩阵乘法和模式分类，手写数字识别准确率 |
| [[An index-free sparse neural network using two-dimensional semiconductor ferroelectric field-effect transistors\|An index-free sparse neural network usin...]] | 2024 | 二维FeFET实现无索引稀疏神经网络，高能效边缘AI处理。 |
| [[Two-dimensional fully ferroelectric-gated hybrid computing-in-memory hardware for high-precision and energy-efficient dynamic tracking\|Two-dimensional fully ferroelectric-gate...]] | 2024 | 2D FeFET 混合 CIM：布尔逻辑+多级单元、96.36% 良率、>10^12 耐久性、用于动态跟踪。 |
| [[Sub-A Monolithic Ferroelectric-Ionic Duality for Stochastic-Neuromorphic Core Integration\|Sub-A Monolithic Ferroelectric-Ionic Dua...]] | 2024 | 本文是 Advanced Materials 论文的辅助材料，包含 FeFET 和 FIDFET 器件的结构分析、晶体相组成对比、氧空位分析、铁电特性测试、器件间变异性和耐久性特性等补充实验数据。 |
| [[Analog reservoir computing via ferroelectric mixed phase boundary transistors\|Analog reservoir computing via ferroelec...]] | 2024 | 铁电MPB晶体管实现全集成模拟储备池计算：5-bit储备池状态，物理储备池+读出神经元一体化。 |
## 相关概念

- [[HfO2]]
- [[FeFET]]
- [[FeRAM]]
- [[ferroelectric polarization]]
- [[Wiki 目录]]
