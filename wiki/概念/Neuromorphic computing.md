---
title: Neuromorphic computing
type: concept
tags: [概念, 进阶]
aliases: [神经形态计算, neuromorphic, brain-inspired computing, 类脑计算]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> 神经形态计算是一种模仿生物神经系统计算原理的范式，采用脉冲驱动的存算一体架构，在能效和实时学习方面显著优于传统数字计算。

## 定义

神经形态计算从生物神经系统的两个关键特性获取灵感：(1) 突触可塑性——连接强度根据活动历史自适应调节；(2) 事件驱动——信息以稀疏脉冲（spike）形式传递和处理。硬件实现通常使用新兴存储器件（ReRAM, FeFET, PCM 等）模拟突触，用模拟电路模拟神经元。

## 关键特性

- **事件驱动**：无输入时为静态零功耗，天然稀疏
- **存算融合**：突触权重本地存储并原位更新，消除存储墙
- **模拟计算**：利用器件物理（欧姆定律、基尔霍夫定律）执行突触积分
- **脉冲编码**：信息以脉冲时序/频率编码，支持 STDP 等生物学习规则
- **主要应用**：边缘 AI、传感器内处理、实时自适应系统
- **主要挑战**：训练方法不成熟、器件非理想性（variation, stuck-at faults）、精度有限

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Ferroelectric Analog Synaptic Transistors\|Ferroelectric Analog Synaptic Transistors]] | 2019 | 本文展示了基于铁电材料和氧化物半导体的FeTFT器件的模拟电导调制行为。通过精确控制铁电层极化实现线性突触权重更新，器件展现了高线性度、多状态（32个状态）和低变异性的增强/抑制特性。基于实测参数的仿 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Device Applications\|Ferroelectric Transistors for Memory and...]] | 2022 | HfO₂基FeFET综述：器件结构、工作原理、存储特性及神经形态计算应用，覆盖最新研究进展。 |
| [[Neuromorphic computing hardware and neural architectures for robotics\|Neuromorphic computing hardware and neur...]] | 2022 | 综述神经形态计算硬件与神经架构在机器人中的应用：快速低功耗神经网络推理、受生物启发的算法设计、自主智能系统创新应用。 |
| [[Brain-inspired computing needs a master plan\|Brain-inspired computing needs a master ...]] | 2022 | 论述脑启发式计算需要总体规划：现代计算系统能耗过高，不适用于复杂 AI 应用，需要协调不同研究社区、提供资金和支持来开发新型脑启发计算技术。 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Computing\|Ferroelectric Transistors for Memory and...]] | 2022 | HfO₂基FeFET综述：器件结构、工作原理、存储特性、神经形态计算应用及未来挑战。 |
| [[Amorphous Indium Oxide Channel FeFETs with Write Voltage of 0.9V and Endurance 10^{12} for Refresh-free 1T-1FeFET embedded Memory\|Amorphous Indium Oxide Channel FeFETs wi...]] | 2023 | 首次BEOL兼容IWO FeFET：写入<0.9V，耐久性>10¹²循环，85°C保持>10⁴s，无需刷新1T-1FeFET存储器。 |
| [[Reservoir Computing System with Diverse Input Patterns in HfAlO-Based Ferroelectric Memristor\|Reservoir Computing System with Diverse ...]] | 2024 | 实现基于 Al 掺杂 HfO 铁电忆阻器的储备池计算系统，演示可处理多种输入脉冲类型的鲁棒储备池层，模拟生物突触短期可塑性，验证图像训练和巴甫洛夫实验等应用。 |
| [[In-sensor dynamic computing for intelligent machine vision\|In-sensor dynamic computing for intellig...]] | 2024 | 存内动态计算方法：使用多端混合维石墨烯-锗异质结构器件阵列，实现弱目标边缘特征的精确提取，在对比度变化的图像中实现高识别精度的目标跟踪，比传统光电卷积方法更鲁棒。解决了传统CMOS图像传感器无法直接提 |
| [[An index-free sparse neural network using two-dimensional semiconductor ferroelectric field-effect transistors\|An index-free sparse neural network usin...]] | 2024 | 2D FeFET存内稀疏性：稀疏信息嵌入存储单元，超高密度27M/mm²，超低能耗，替代索引稀疏方案。 |
| [[Ferroelectric-based neuromorphic memory devices for bio-inspired computing\|Ferroelectric-based neuromorphic memory ...]] | 2024 | 综述铁电神经形态器件与阵列：铪基和二维铁电材料模拟神经元/突触时间动态，低写入能耗，涵盖突触器件、神经元电路、阵列拓扑和传感器内计算应用。 |
| [[Sub-A Monolithic Ferroelectric-Ionic Duality for Stochastic-Neuromorphic Core Integration\|Sub-A Monolithic Ferroelectric-Ionic Dua...]] | 2024 | 本文是 Advanced Materials 论文的辅助材料，包含 FeFET 和 FIDFET 器件的结构分析、晶体相组成对比、氧空位分析、铁电特性测试、器件间变异性和耐久性特性等补充实验数据。 |
| [[Analog reservoir computing via ferroelectric mixed phase boundary transistors\|Analog reservoir computing via ferroelec...]] | 2024 | 利用 HfZrOx 混相边界材料的双栅 TFT 实现全集成模拟储备池计算系统，MPB TFT 作物理储备池和神经元，FeTFT 作突触，实现 5-bit |
## 相关概念

- [[In-memory computing]]
- [[Memristor]]
- [[Reservoir computing]]
- [[RRAM]]
- [[FeFET]]
- [[crossbar]]
- [[Wiki 目录]]
