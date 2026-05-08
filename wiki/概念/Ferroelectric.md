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
| [[Domain switching and spatial dependence of permittivity in ferroelectric thin films|Domain switching and spatial dependence of pe...]] | 1997 | 提出包含介电常数空间变化的铁电薄膜开关模型，描述 180° 和 90° 畴开关，揭示介电常数空间依赖性对矫顽场和磁滞回线形状的显著影响。 |
| [[Ferroelectric FET Based In-Memory Computing for Few-Shot Learning|Ferroelectric FET Based In-Memory Computing f...]] | 2019 | FeFET 小样本学习存内计算：模拟电导权重存储，原型网络硬件实现，边缘能效推理。 |
| [[Monte Carlo Simulation of Switching Dynamics in Polycrystalline Ferroelectric Capacitors|Monte Carlo Simulation of Switching Dynamics ...]] | 2019 | 蒙特卡洛模拟多晶铁电器件开关动力学：基于成核限制开关模型，使用HZO电容器数据提取晶粒统计分布，预测任意波形下动态响应，分析铁电-电介质双层结构动态特性及... |
| [[Ferroelectric Field Effect Transistors Progress and Perspective|Ferroelectric Field Effect Transistors Progre...]] | 2021 | 综述 HfO2 基 FeFET 的最新进展，包括器件物理、材料工程和集成挑战，展望大规模商业应用的未来研究方向。 |
| [[Hafnium Oxide-Based Ferroelectric Memories Are We Ready for Application|Hafnium Oxide-Based Ferroelectric Memories Ar...]] | 2021 | HfO2 铁电存储综述：器件物理、材料工程、集成挑战、商业部署评估。 |
| [[CMOS-compatible compute-in-memory accelerators based on integrated ferroelectric synaptic arrays for convolution neural networks|CMOS-compatible compute-in-memory accelerator...]] | 2022 | FeFET突触阵列CIM加速器：三端FeFET兼存储和访问，HfZrOx/IZO <400°C制备，MNIST验证CIM功能，展示高密度CNN加速潜力。 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Computing|Ferroelectric Transistors for Memory and Neur...]] | 2022 | HfO₂基FeFET综述：器件结构、工作原理、存储特性、神经形态计算应用及未来挑战。 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Device Applications|Ferroelectric Transistors for Memory and Neur...]] | 2022 | HfO₂基FeFET综述：器件结构、工作原理、存储特性及神经形态计算应用，覆盖最新研究进展。 |
| [[Monolithic 3D Integration of High Endurance Multi-bit Ferroelectric FET|Monolithic 3D Integration of High Endurance M...]] | 2022 | 单片 3D FeFET 集成：BEoL 铁电 MFM 器件，>10^10 耐久性，2 比特/单元，16kbit 阵列演示。 |
| [[A 256 Kbit Hf0.5Zr0.5O2-based FeRAM Chip|A 256 Kbit Hf0.5Zr0.5O2-based FeRAM Chip]] | 2023 | 256 Kbit HZO FeRAM 芯片：sub-8nm 技术，350°C BEOL，0.7 pJ/bit，>10^12 耐久性，O3 预结晶工程。 |
| [[Deep Random Forest with Ferroelectric Analog Content Addressable Memory|Deep Random Forest with Ferroelectric Analog ...]] | 2024 | FeFET 模拟 CAM 深度随机森林：多级 V_TH 存储、1×16 阵列演示、边缘计算决策树。 |
| [[Ferroelectric $mathbf { A l } _ { 0 . 8 5 } mathsf { S c } _ { 0 . 1 5 } mathsf { N }$ and $mathsf { H f } _ { 0 . 5 } mathsf { Z r } _ { 0 . 5 } mathsf { O } _ { 2 }$ Domain Switching Dynamics|Ferroelectric $mathbf { A l } _ { 0 . 8 5 } m...]] | 2024 | 本文比较了Al0.85Sc0.15N和Hf0.5Zr0.5O2两种铁电体系的畴切换动力学。AlScN受热激活蠕变畴壁运动主导，HfZrO2以独立成核畴为特... |

## 相关概念

- [[HfO2]]
- [[FeFET]]
- [[FeRAM]]
- [[ferroelectric polarization]]
- [[Wiki 目录]]
