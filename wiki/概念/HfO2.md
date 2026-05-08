---
title: HfO2
type: concept
tags: [概念, 基础]
aliases: [hafnium oxide, 氧化铪, HfO₂, HfO2, hafnium dioxide, HZO, Hf0.5Zr0.5O2, Hf0.5Zr0.5O₂, hafnia]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> 氧化铪（HfO₂）基铁电材料是当前 FeFET 和铁电存储器的核心栅介质材料，2011 年首次被发现具有铁电性，因其 CMOS 兼容性和优异的缩放特性成为铁电器件主流选择。

## 定义

HfO₂ 在室温下稳定相为单斜相（无铁电性），通过掺杂（Si, Al, Gd, Zr, Y 等）、应力工程或氧空位调控可获得正交相（Pca2₁），该相具有稳定铁电性。Hf₀.₅Zr₀.₅O₂（HZO）是最常见的铁电组分。

## 关键特性

- **CMOS 兼容**：已在先进逻辑工艺中作为 high-k 栅介质使用
- **厚度缩放**：铁电性可在 <10 nm 厚度下保持，优于传统钙钛矿铁电体
- **掺杂调控**：通过掺杂元素和浓度调控铁电/反铁电特性
- **唤醒效应**：初始循环中铁电极化逐渐增强（wake-up），可能与氧空位再分布有关
- **疲劳**：长循环后极化衰减（fatigue），是器件耐久性的主要限制因素
- **主要挑战**：唤醒效应的不确定性、疲劳机制、与 IGZO/Si 沟道的界面质量

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Write Disturb in Ferroelectric FETs and Its Implication for 1T-FeFET AND Memory Arrays\|Write Disturb in Ferroelectric FETs and ...]] | 2018 | 研究 HZO FeFET AND 阵列写入干扰：分析 VW/2 和 VW/3 抑制方案，发现低 VTH 态漏电流和高 VTH 态读电流增加是限制阵列尺寸的关键因素，为阵列优化提供指导。 |
| [[Monte Carlo Simulation of Switching Dynamics in Polycrystalline Ferroelectric Capacitors\|Monte Carlo Simulation of Switching Dyna...]] | 2019 | 蒙特卡洛模拟多晶铁电器件开关动力学：基于成核限制开关模型，使用HZO电容器数据提取晶粒统计分布，预测任意波形下动态响应，分析铁电-电介质双层结构动态特性及器件变异导致的存储窗口缩减。 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Device Applications\|Ferroelectric Transistors for Memory and...]] | 2022 | 综述HfO2基FeFET在存储和神经形态器件中的应用：涵盖器件物理、材料工程、多值存储和突触可塑性，展望大规模商业化前景。 |
| [[Write Bias Scheme Optimization of Ferroelectric Field-Effect-Transistor (FeFET) Synapse for Accurate On-chip Training\|Write Bias Scheme Optimization of Ferroe...]] | 2023 | 通过TCAD仿真优化FeFET突触片上训练的写入偏置方案，实现4位突触操作和高对称性/线性度的增强抑制特性，即使在工艺变异下仍保持良好性能。 |
| [[Experimental Demonstration of Ferroelectric HfO2 FET with Ultrathin-body IGZO for High-Density and Low-Power Memory Application\|Experimental Demonstration of Ferroelect...]] | 2023 | 超薄体IGZO FeFET实验演示：采用HfO2铁电层，实现高迁移率、理想亚阈值斜率、可控存储窗口，为高密度低功耗存储应用提供新方案。 |
| [[Reconfigurable ferroelectric hafnium oxide FeFET fabricated in 28 nm CMOS technology for mmWave applications\|Reconfigurable ferroelectric hafnium oxi...]] | 2023 | 28 nm CMOS工艺制造的可重构HfO₂ FeFET，存储窗口>1 V，f_T/f_MAX分别达113/230 GHz，适用于毫米波射频电路。 |
| [[Application and Benefits of Target Programming Algorithms for Ferroelectric HfO₂ Transistors\|Application and Benefits of Target Progr...]] | 2023 | 目标编程算法改善 FeFET 耐久性能和变异特性：可将阈值电压设定为任意值，适用于多级单元和模拟存内计算，通过 GinestraTM 仿真提取 HfO₂ 陷阱分布并提出退化机制模型。 |
| [[Sub-Vertical Ferroelectric $ mathrm { H f O } _ { 2 }$ FET based on 3-D NAND Architecture Towards Dense Low-Power Memory\|Sub-Vertical Ferroelectric $ mathrm { H ...]] | 2024 | 垂直HfO₂ FET 3-D NAND架构：高密度低功耗非易失存储，良好存储窗口和可靠性。 |
| [[High-Endurance MoS2 FeFET with Operating Voltage Less Than 1V for eNVM in Scaled CMOS\|High-Endurance MoS2 FeFET with Operating...]] | 2025 | 单层MoS₂ FeFET：超薄HZO（2.5nm）实现<1V工作电压、>10^12次耐久性、>10年保持时间，兼容CMOS后端工艺，适用于先进节点嵌入式存储。 |
| [[Coupled ferroelectric-anisotropic optoelectronic synapse for polarization-sensitive neuromorphic vision\|Coupled ferroelectric-anisotropic optoel...]] | 2026 | 偏振分辨光电突触，ReS2/HZO MFMIS FeFET结构。ANN 97.33%虹膜识别，3x3 FeFET CNN蝴蝶分类，2.0 fJ/事件能效。铁电-各向异性平台实现偏振敏感神经形态视觉。 |
| [[Homogeneous integration of two-dimensional material-based optoelectronic neurons and ferroelectric synapses for neuromorphic vision\|Homogeneous integration of two-dimension...]] | 2026 | 实现 MoS2 光电 LIF 神经元与铁电突触的均匀集成：多光谱传感、无电容积分、阈值触发脉冲，SNN 系统颜色识别 91.7%、目标检测 93.5% |
| [[Ferroelectric Field Effect Transistors Progress and Perspective\|Ferroelectric Field Effect Transistors P...]] | 2021 | 综述 HfO2 基 FeFET 的最新进展，包括器件物理、材料工程和集成挑战，展望大规模商业应用的未来研究方向。 |
## 相关概念

- [[FeFET]]
- [[Ferroelectric]]
- [[FeRAM]]
- [[IGZO]]
- [[Wiki 目录]]
