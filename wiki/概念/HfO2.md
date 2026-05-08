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
| [[Write Disturb in Ferroelectric FETs and Its Implication for 1T-FeFET AND Memory Arrays|Write Disturb in Ferroelectric FETs and Its I...]] | 2018 | 研究 HZO FeFET AND 阵列写入干扰：分析 VW/2 和 VW/3 抑制方案，发现低 VTH 态漏电流和高 VTH 态读电流增加是限制阵列尺寸的... |
| [[Monte Carlo Simulation of Switching Dynamics in Polycrystalline Ferroelectric Capacitors|Monte Carlo Simulation of Switching Dynamics ...]] | 2019 | 蒙特卡洛模拟多晶铁电器件开关动力学：基于成核限制开关模型，使用HZO电容器数据提取晶粒统计分布，预测任意波形下动态响应，分析铁电-电介质双层结构动态特性及... |
| [[Back-End CMOS Compatible and Flexible Ferroelectric Memories for Neuromorphic Computing and Adaptive Sensing|Back-End CMOS Compatible and Flexible Ferroel...]] | 2021 | 综述掺杂 HfO2 和分子铁电体作为 CMOS BEOL 兼容和柔性可穿戴平台神经形态器件的潜力，讨论铁电存储器技术在边缘计算中的应用前景。 |
| [[Ferroelectric Field Effect Transistors Progress and Perspective|Ferroelectric Field Effect Transistors Progre...]] | 2021 | 综述 HfO2 基 FeFET 的最新进展，包括器件物理、材料工程和集成挑战，展望大规模商业应用的未来研究方向。 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Computing|Ferroelectric Transistors for Memory and Neur...]] | 2022 | HfO₂基FeFET综述：器件结构、工作原理、存储特性、神经形态计算应用及未来挑战。 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Device Applications|Ferroelectric Transistors for Memory and Neur...]] | 2022 | HfO₂基FeFET综述：器件结构、工作原理、存储特性及神经形态计算应用，覆盖最新研究进展。 |
| [[A novel reconfigurable RF switch based on ferroelectric hafnium oxide FeFET fabricated in 22 nm FDSOI technology|A novel reconfigurable RF switch based on fer...]] | 2023 | 一句话总结：本文针对铁电存储器领域，提出了创新的解决方案，实验验证了方法的有效性。 |
| [[Application and Benefits of Target Programming Algorithms for Ferroelectric HfO₂ Transistors|Application and Benefits of Target Programmin...]] | 2023 | 目标编程算法改善 FeFET 耐久性能和变异特性：可将阈值电压设定为任意值，适用于多级单元和模拟存内计算，通过 GinestraTM 仿真提取 HfO₂ ... |
| [[CMOS Backend-of-Line Compatible Memory Array for In-Memory Computing|CMOS Backend-of-Line Compatible Memory Array ...]] | 2023 | CMOS BEOL 兼容存储阵列：ZnO TFT，<400°C，单片 3D 集成存内计算。 |
| [[Experimental Demonstration of Ferroelectric HfO2 FET with Ultrathin-body IGZO for High-Density and Low-Power Memory Application|Experimental Demonstration of Ferroelectric H...]] | 2023 | 超薄体IGZO FeFET实验演示：采用HfO2铁电层，实现高迁移率、理想亚阈值斜率、可控存储窗口，为高密度低功耗存储应用提供新方案。 |
| [[Metal-Induced Oxygen Vacancy Control in InGaZnOHf0.5Zr0.5O2 Ferroelectric Field-Effect Transistor Arrays for Simultaneous Improvement of Memory Window and Electrical Stability|Metal-Induced Oxygen Vacancy Control in InGaZ...]] | 2023 | W/IGZO覆盖层调控氧空位分布，协同优化HZO铁电开关与IGZO半导体性能，FeFET实现4.13 V存储窗口、70 mV·dec−1亚阈值摆幅、107... |
| [[Reconfigurable ferroelectric hafnium oxide FeFET fabricated in 28 nm CMOS technology for mmWave applications|Reconfigurable ferroelectric hafnium oxide Fe...]] | 2023 | 28 nm CMOS工艺制造的可重构HfO₂ FeFET，存储窗口>1 V，f_T/f_MAX分别达113/230 GHz，适用于毫米波射频电路。 |

## 相关概念

- [[FeFET]]
- [[Ferroelectric]]
- [[FeRAM]]
- [[IGZO]]
- [[Wiki 目录]]
