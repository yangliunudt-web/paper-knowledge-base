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
| [[Ferroelectric Analog Synaptic Transistors\|Ferroelectric Analog Synaptic Transistors]] | 2019 | 本文展示了基于铁电材料和氧化物半导体的FeTFT器件的模拟电导调制行为。通过精确控制铁电层极化实现线性突触权重更新，器件展现了高线性度、多状态（32个状态）和低变异性的增强/抑制特性。基于实测参数的仿 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Device Applications\|Ferroelectric Transistors for Memory and...]] | 2022 | 综述HfO2基FeFET在存储和神经形态器件中的应用：涵盖器件物理、材料工程、多值存储和突触可塑性，展望大规模商业化前景。 |
| [[Monolithic 3D Integration of High Endurance Multi-bit Ferroelectric FET\|Monolithic 3D Integration of High Endura...]] | 2022 | 单片 3D FeFET 集成：BEoL 铁电 MFM 器件，>10^10 耐久性，2 比特/单元，16kbit 阵列演示。 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Computing\|Ferroelectric Transistors for Memory and...]] | 2022 | 综述HfO2基FeFET在存储和神经形态计算中的应用：器件结构、工作原理、存储特性和突触应用。 |
| [[CMOS-compatible compute-in-memory accelerators based on integrated ferroelectric synaptic arrays for convolution neural networks\|CMOS-compatible compute-in-memory accele...]] | 2022 | FeFET突触阵列CIM加速器：三端FeFET兼存储和访问，HfZrOx/IZO <400°C制备，MNIST验证CIM功能，展示高密度CNN加速潜力。 |
| [[Highly-scaled and fully-integrated 3-dimensional ferroelectric transistor array for hardware implementation of neural networks\|Highly-scaled and fully-integrated 3-dim...]] | 2023 | 提出基于 HfZrOx 铁电晶体管的三维 NAND 阵列 (3D FeNAND) 用于神经网络硬件实现，通过沟槽结构实现高密度集成，演示了向量矩阵乘法和模式分类，手写数字识别准确率 |
| [[A novel reconfigurable RF switch based on ferroelectric hafnium oxide FeFET fabricated in 22 nm FDSOI technology\|A novel reconfigurable RF switch based o...]] | 2023 | 在22nm FDSOI工艺上制备基于HfO2铁电FeFET的多指结构可重构RF开关，利用非易失性阈值电压调节实现零栅压操作，融合无源/有源开关优势。16指器件fT=135GHz、fMAX=139GHz |
| [[A 2-Transistor-2-Capacitor Ferroelectric Edge Compute-in-Memory Scheme With Disturb-Free Inference and High Endurance\|A 2-Transistor-2-Capacitor Ferroelectric...]] | 2023 | C2FeRAM 2T2C方案：无干扰存内计算、高耐久性、CIFAR-10 VGG8推理>100倍时间且精度下降<1%、相比1T1C FeRAM缓存实现4倍能效/200倍速度/3.2e5倍生命周期提升。 |
| [[Proposal of P-Channel FE NAND with High Drain Current and Feasible Disturbance for Next Generation 3D NAND\|Proposal of P-Channel FE NAND with High ...]] | 2023 | p沟道FeFET NAND提案：利用无空穴俘获特性实现高漏极电流和铁电电荷增强，相比n‑FeFET具有更高导通电流、更佳保持与干扰特性，适用于下一代3D |
## 相关概念

- [[HfO2]]
- [[FeFET]]
- [[FeRAM]]
- [[ferroelectric polarization]]
- [[Wiki 目录]]
