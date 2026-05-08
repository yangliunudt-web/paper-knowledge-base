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
| [[Scaling-up Resistive Synaptic Arrays for Neuro-inspired Architecture Challenges and Prospect|Scaling-up Resistive Synaptic Arrays for Neur...]] | 2016 | 讨论阻变突触器件交叉阵列规模扩展的挑战（器件非线性、有限精度、器件变异、IR 压降），提出差分读出消除关态电流、多单元平均减少变异、放宽线宽降低 IR |
| [[Neuro-Inspired Computing With Emerging Nonvolatile Memory|Neuro-Inspired Computing With Emerging Nonvol...]] | 2018 | 综述新兴非易失性存储器件在神经启发式计算中的应用：涵盖相变/阻变/铁电存储器等突触器件、交叉阵列架构、器件‑电路‑算法协同设计，展望定制化学习算法。 |
| [[NeuroSim A Circuit-Level Macro Model for Benchmarking Neuro-Inspired Architectures in Online Learning|NeuroSim A Circuit-Level Macro Model for Benc...]] | 2018 | 开发 NeuroSim 电路级宏模型，估算神经启发架构的面积、延迟、能耗，支持 SRAM、数字和模拟 eNVM 架构设计空间探索和基准测试。 |
| [[Ferroelectric Analog Synaptic Transistors|Ferroelectric Analog Synaptic Transistors]] | 2019 | 本文展示了基于铁电材料和氧化物半导体的FeTFT器件的模拟电导调制行为。通过精确控制铁电层极化实现线性突触权重更新，器件展现了高线性度、多状态（32个状态... |
| [[Back-End CMOS Compatible and Flexible Ferroelectric Memories for Neuromorphic Computing and Adaptive Sensing|Back-End CMOS Compatible and Flexible Ferroel...]] | 2021 | 综述掺杂 HfO2 和分子铁电体作为 CMOS BEOL 兼容和柔性可穿戴平台神经形态器件的潜力，讨论铁电存储器技术在边缘计算中的应用前景。 |
| [[2022 roadmap on neuromorphic computing and engineering|2022 roadmap on neuromorphic computing and en...]] | 2022 | 神经形态计算路线图综述：涵盖神经形态器件、电路架构、算法应用现状与挑战，展望类脑计算未来发展方向。 |
| [[Brain-inspired computing needs a master plan|Brain-inspired computing needs a master plan]] | 2022 | 论述脑启发式计算需要总体规划：现代计算系统能耗过高，不适用于复杂 AI 应用，需要协调不同研究社区、提供资金和支持来开发新型脑启发计算技术。 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Computing|Ferroelectric Transistors for Memory and Neur...]] | 2022 | HfO₂基FeFET综述：器件结构、工作原理、存储特性、神经形态计算应用及未来挑战。 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Device Applications|Ferroelectric Transistors for Memory and Neur...]] | 2022 | HfO₂基FeFET综述：器件结构、工作原理、存储特性及神经形态计算应用，覆盖最新研究进展。 |
| [[Neuromorphic computing hardware and neural architectures for robotics|Neuromorphic computing hardware and neural ar...]] | 2022 | 综述神经形态计算硬件与神经架构在机器人中的应用：快速低功耗神经网络推理、受生物启发的算法设计、自主智能系统创新应用。 |
| [[Amorphous Indium Oxide Channel FeFETs with Write Voltage of 0.9V and Endurance 10^{12} for Refresh-free 1T-1FeFET embedded Memory|Amorphous Indium Oxide Channel FeFETs with Wr...]] | 2023 | 首次BEOL兼容IWO FeFET：写入<0.9V，耐久性>10¹²循环，85°C保持>10⁴s，无需刷新1T-1FeFET存储器。 |
| [[An index-free sparse neural network using two-dimensional semiconductor ferroelectric field-effect transistors|An index-free sparse neural network using two...]] | 2024 | 2D FeFET存内稀疏性：稀疏信息嵌入存储单元，超高密度27M/mm²，超低能耗，替代索引稀疏方案。 |

## 相关概念

- [[In-memory computing]]
- [[Memristor]]
- [[Reservoir computing]]
- [[RRAM]]
- [[FeFET]]
- [[crossbar]]
- [[Wiki 目录]]
