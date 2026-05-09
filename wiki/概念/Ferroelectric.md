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
| [[Monte Carlo Simulation of Switching Dynamics in Polycrystalline Ferroelectric Capacitors\|Monte Carlo Simulation of Switching Dyna...]] | 2019 | 蒙特卡洛模拟多晶铁电器件开关动力学：基于成核限制开关模型，使用HZO电容器数据提取晶粒统计分布，预测任意波形下动态响应，分析铁电-电介质双层结构动态特性及器件变异导致的存储窗口缩减。 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Device Applications\|Ferroelectric Transistors for Memory and...]] | 2022 | 综述HfO2基FeFET在存储和神经形态器件中的应用：涵盖器件物理、材料工程、多值存储和突触可塑性，展望大规模商业化前景。 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Computing\|Ferroelectric Transistors for Memory and...]] | 2022 | 综述HfO2基FeFET在存储和神经形态计算中的应用：器件结构、工作原理、存储特性和突触应用。 |
| [[CMOS-compatible compute-in-memory accelerators based on integrated ferroelectric synaptic arrays for convolution neural networks\|CMOS-compatible compute-in-memory accele...]] | 2022 | FeFET突触阵列CIM加速器：三端FeFET兼存储和访问，HfZrOx/IZO <400°C制备，MNIST验证CIM功能，展示高密度CNN加速潜力。 |
| [[Highly-scaled and fully-integrated 3-dimensional ferroelectric transistor array for hardware implementation of neural networks\|Highly-scaled and fully-integrated 3-dim...]] | 2023 | 提出基于 HfZrOx 铁电晶体管的三维 NAND 阵列 (3D FeNAND) 用于神经网络硬件实现，通过沟槽结构实现高密度集成，演示了向量矩阵乘法和模式分类，手写数字识别准确率 |
| [[An index-free sparse neural network using two-dimensional semiconductor ferroelectric field-effect transistors\|An index-free sparse neural network usin...]] | 2024 | 二维FeFET实现无索引稀疏神经网络，高能效边缘AI处理。 |
| [[Analog reservoir computing via ferroelectric mixed phase boundary transistors\|Analog reservoir computing via ferroelec...]] | 2024 | 铁电MPB晶体管实现全集成模拟储备池计算：5-bit储备池状态，物理储备池+读出神经元一体化。 |
| [[In-memory ferroelectric differentiator\|In-memory ferroelectric differentiator]] | 2025 | 存内铁电微分器：利用铁电电容器本征微分响应，0.24 fJ/次、1 MHz、98.9%准确率。 |
| [[Highly-reliable ferroelectric thin-film transistors array for hardware implementation of image classification\|Highly-reliable ferroelectric thin-film ...]] | 2025 | 研究问题：FeTFT在存内计算中面临弱擦除问题和界面缺陷导致的可靠性下降，限制了其在神经网络硬件实现中的应用。研究方法：提出平面集成MFMIS-FeTFT结构，通过浮栅抑制弱擦除效应，简化工艺减少界面 |
| [[Emerging 2D Ferroelectric Semiconductors From Fundamentals to Advanced Device Applications\|Emerging 2D Ferroelectric Semiconductors...]] | 2025 | 二维铁电半导体综述：涵盖发展历程、基本机制（软模理论、滑动铁电性）、本征/外延材料体系、在FeS-FET、FTJ、光电探测器、自旋器件等应用，挑战与未来方向。 |
| [[Coupled ferroelectric-anisotropic optoelectronic synapse for polarization-sensitive neuromorphic vision\|Coupled ferroelectric-anisotropic optoel...]] | 2026 | 偏振分辨光电突触，ReS2/HZO MFMIS FeFET结构。ANN 97.33%虹膜识别，3x3 FeFET CNN蝴蝶分类，2.0 fJ/事件能效。铁电-各向异性平台实现偏振敏感神经形态视觉。 |
## 相关概念

- [[HfO2]]
- [[FeFET]]
- [[FeRAM]]
- [[ferroelectric polarization]]
- [[Wiki 目录]]
