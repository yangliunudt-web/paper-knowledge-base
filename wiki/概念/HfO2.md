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
| [[Ferroelectric Transistors for Memory and Neuromorphic Computing\|Ferroelectric Transistors for Memory and...]] | 2022 | 综述HfO2基FeFET在存储和神经形态计算中的应用：器件结构、工作原理、存储特性和突触应用。 |
| [[A novel reconfigurable RF switch based on ferroelectric hafnium oxide FeFET fabricated in 22 nm FDSOI technology\|A novel reconfigurable RF switch based o...]] | 2023 | 在22nm FDSOI工艺上制备基于HfO2铁电FeFET的多指结构可重构RF开关，利用非易失性阈值电压调节实现零栅压操作，融合无源/有源开关优势。16指器件fT=135GHz、fMAX=139GHz |
| [[A 256 Kbit Hf0.5Zr0.5O2-based FeRAM Chip\|A 256 Kbit Hf0.5Zr0.5O2-based FeRAM Chip]] | 2023 | 256 Kbit HZO FeRAM 芯片：sub-8nm 技术，350°C BEOL，0.7 pJ/bit，>10^12 耐久性，O3 预结晶工程。 |
| [[Write Bias Scheme Optimization of Ferroelectric Field-Effect-Transistor (FeFET) Synapse for Accurate On-chip Training\|Write Bias Scheme Optimization of Ferroe...]] | 2023 | 通过TCAD仿真优化FeFET突触片上训练的写入偏置方案，实现4位突触操作和高对称性/线性度的增强抑制特性，即使在工艺变异下仍保持良好性能。 |
| [[Experimental Demonstration of Ferroelectric HfO2 FET with Ultrathin-body IGZO for High-Density and Low-Power Memory Application\|Experimental Demonstration of Ferroelect...]] | 2023 | 超薄体IGZO FeFET实验演示：采用HfO2铁电层，实现高迁移率、理想亚阈值斜率、可控存储窗口，为高密度低功耗存储应用提供新方案。 |
| [[Reconfigurable ferroelectric hafnium oxide FeFET fabricated in 28 nm CMOS technology for mmWave applications\|Reconfigurable ferroelectric hafnium oxi...]] | 2023 | 28 nm CMOS工艺制造的可重构HfO₂ FeFET，存储窗口>1 V，f_T/f_MAX分别达113/230 GHz，适用于毫米波射频电路。 |
| [[Application and Benefits of Target Programming Algorithms for Ferroelectric HfO₂ Transistors\|Application and Benefits of Target Progr...]] | 2023 | 目标编程算法改善 FeFET 耐久性能和变异特性：可将阈值电压设定为任意值，适用于多级单元和模拟存内计算，通过 GinestraTM 仿真提取 HfO₂ 陷阱分布并提出退化机制模型。 |
| [[Reservoir Computing System with Diverse Input Patterns in HfAlO-Based Ferroelectric Memristor\|Reservoir Computing System with Diverse ...]] | 2024 | 实现基于 Al 掺杂 HfO 铁电忆阻器的储备池计算系统，演示可处理多种输入脉冲类型的鲁棒储备池层，模拟生物突触短期可塑性，验证图像训练和巴甫洛夫实验等应用。 |
| [[Unlocking Large Memory Windows and 16-Level Data per Cell Memory Operations in Hafnia-Based Ferroelectric Transistors\|Unlocking Large Memory Windows and 16-Le...]] | 2024 | HfAlOx FeTFT 16 级存储：MFMFS 栅极堆叠，10V 存储窗口，DCC 一次性编程，3D 兼容。 |
## 相关概念

- [[FeFET]]
- [[Ferroelectric]]
- [[FeRAM]]
- [[IGZO]]
- [[Wiki 目录]]
