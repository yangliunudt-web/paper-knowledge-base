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
| [[Ferroelectric Transistors for Memory and Neuromorphic Device Applications\|Ferroelectric Transistors for Memory and...]] | 2022 | 综述HfO2基FeFET在存储和神经形态器件中的应用：涵盖器件物理、材料工程、多值存储和突触可塑性，展望大规模商业化前景。 |
| [[Neuromorphic computing hardware and neural architectures for robotics\|Neuromorphic computing hardware and neur...]] | 2022 | 综述神经形态计算硬件与神经架构在机器人中的应用：快速低功耗神经网络推理、受生物启发的算法设计、自主智能系统创新应用。 |
| [[Brain-inspired computing needs a master plan\|Brain-inspired computing needs a master ...]] | 2022 | 论述脑启发式计算需要总体规划：现代计算系统能耗过高，不适用于复杂 AI 应用，需要协调不同研究社区、提供资金和支持来开发新型脑启发计算技术。 |
| [[Amorphous Indium Oxide Channel FeFETs with Write Voltage of 0.9V and Endurance 10^{12} for Refresh-free 1T-1FeFET embedded Memory\|Amorphous Indium Oxide Channel FeFETs wi...]] | 2023 | 首次BEOL兼容IWO FeFET：写入<0.9V，耐久性>10¹²循环，85°C保持>10⁴s，无需刷新1T-1FeFET存储器。 |
| [[In-sensor dynamic computing for intelligent machine vision\|In-sensor dynamic computing for intellig...]] | 2024 | 存内动态计算方法：使用多端混合维石墨烯-锗异质结构器件阵列，实现弱目标边缘特征的精确提取，在对比度变化的图像中实现高识别精度的目标跟踪，比传统光电卷积方法更鲁棒。解决了传统CMOS图像传感器无法直接提 |
| [[Physical reservoir computing with emerging electronics\|Physical reservoir computing with emergi...]] | 2024 | 综述新兴电子器件在物理储备计算中的应用：涵盖电子、光学、机械器件等物理系统，讨论架构、节点、输入输出层、性能基准和竞争力，展望技术挑战与未来方向。 |
| [[Electrochemical ohmic memristors for Electrochemical oh\|Electrochemical ohmic memristors for Ele...]] | 2024 | 本文提出电化学欧姆忆阻器，利用电化学机制实现可靠阻变切换和欧姆行为，面向神经形态计算应用。 |
| [[Neuromorphic computing at scale\|Neuromorphic computing at scale]] | 2025 | 神经形态计算规模化：综述大脑启发硬件/算法设计、可扩展架构关键特征、潜在应用与挑战、生态系统需求，为大规模神经形态系统发展提供路线图。 |
| [[A Monolithic Ferroelectric‑Ionic Duality for Stochastic‑Neuromorphic Core Integration\|A Monolithic Ferroelectric‑Ionic Duality...]] | 2026 | 提出铪基铁电‑离子双重性器件，利用氧空位作为功能性离子组分实现电压可调随机性和突触行为增强，在单一器件中集成随机编码与突触记忆，具备 CMOS 兼容性和 |
| [[Neuro-Inspired Computing With Emerging Nonvolatile Memory\|Neuro-Inspired Computing With Emerging N...]] | 2018 | 综述新兴非易失性存储器件在神经启发式计算中的应用：涵盖相变/阻变/铁电存储器等突触器件、交叉阵列架构、器件‑电路‑算法协同设计，展望定制化学习算法。 |
| [[NeuroSim A Circuit-Level Macro Model for Benchmarking Neuro-Inspired Architectures in Online Learning\|NeuroSim A Circuit-Level Macro Model for...]] | 2018 | 开发 NeuroSim 电路级宏模型，估算神经启发架构的面积、延迟、能耗，支持 SRAM、数字和模拟 eNVM 架构设计空间探索和基准测试。 |
## 相关概念

- [[In-memory computing]]
- [[Memristor]]
- [[Reservoir computing]]
- [[RRAM]]
- [[FeFET]]
- [[crossbar]]
- [[Wiki 目录]]
