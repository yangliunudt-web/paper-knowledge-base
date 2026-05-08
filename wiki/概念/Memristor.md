---
title: Memristor
type: concept
tags: [概念, 基础]
aliases: [忆阻器, memristive device, memristors, RRAM, memristive network, Memristive network, resistive memory, Resistive memory, 阻变存储器]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> 忆阻器（Memristor）是记忆电阻的简称，其电阻值随流经电荷的历史而改变，是第四种基本电路元件（继电阻、电容、电感之后），在非易失存储和神经形态计算中广泛用作突触器件。

## 定义

忆阻器理论由蔡少棠（Leon Chua）于 1971 年提出，2008 年 HP 实验室首次在 TiO₂ 器件中实现物理验证。其阻变机理包括：氧空位导电细丝（VCM）、金属离子导电细丝（ECM）、界面效应等。

在神经形态计算中，忆阻器的电导值代表突触权重，通过施加编程脉冲调节电导。

## 关键特性

- **非易失性存储**：电阻状态断电保持
- **多值/模拟存储**：部分阻变可实现多电导态（>4 bit）
- **纳秒级切换速度**
- **高密度集成**：crossbar 结构支持 4F² 单元面积
- **突触可塑性模拟**：渐进电导变化天然模拟 STDP、LTP/LTD
- **主要挑战**：cycle-to-cycle 和 device-to-device 变异、 stuck-at faults、耐久性 vs 保持性权衡

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Scaling-up Resistive Synaptic Arrays for Neuro-inspired Architecture Challenges and Prospect|Scaling-up Resistive Synaptic Arrays for Neur...]] | 2016 | 讨论阻变突触器件交叉阵列规模扩展的挑战（器件非线性、有限精度、器件变异、IR 压降），提出差分读出消除关态电流、多单元平均减少变异、放宽线宽降低 IR |
| [[Neuro-Inspired Computing With Emerging Nonvolatile Memory|Neuro-Inspired Computing With Emerging Nonvol...]] | 2018 | 综述新兴非易失性存储器件在神经启发式计算中的应用：涵盖相变/阻变/铁电存储器等突触器件、交叉阵列架构、器件‑电路‑算法协同设计，展望定制化学习算法。 |
| [[Memory devices and applications for in‑memory computing|Memory devices and applications for in‑memory...]] | 2020 | 存内计算综述：涵盖基于电荷和基于电阻的存储设备、关键计算原语（向量‑矩阵乘法、逻辑运算、随机计算）及其在科学计算、机器学习等领域的应用，探讨器件与阵列层面... |
| [[sub-Combinatorial Optimization by Weight Annealing in Memristive Hopfield Networks Supplementary Materials|sub-Combinatorial Optimization by Weight Anne...]] | 2020 | 忆阻器 Hopfield 网络权重退火组合优化论文补充材料：Hopfield 网络与退火技术、优化问题公式、图划分示例及仿真结果。 |
| [[sub-Combinatorial Optimization by Weight Annealing in Memristive Hopfield Networks Supplementary Materials (Copy 1)|sub-Combinatorial Optimization by Weight Anne...]] | 2020 | 忆阻器 Hopfield 网络权重退火组合优化论文补充材料：Hopfield 网络与退火技术、优化问题公式、图划分示例及仿真结果。 |
| [[sub-Combinatorial Optimization by Weight Annealing in Memristive Hopfield Networks Supplementary Materials (Copy)|sub-Combinatorial Optimization by Weight Anne...]] | 2020 | 忆阻器 Hopfield 网络权重退火组合优化论文补充材料：Hopfield 网络与退火技术、优化问题公式、图划分示例及仿真结果。 |
| [[Combinatorial optimization by weight annealing in memristive hopfeld networks|Combinatorial optimization by weight annealin...]] | 2021 | 本文提出权重退火方法用于忆阻器Hopfield网络的组合优化。初始权重为零使网络快速进入全局最小，逐渐引入权重保持基态。在TiO2 crossbar和eF... |
| [[In-Memory Learning With Analog Resistive Switching Memory A Review and Perspective|In-Memory Learning With Analog Resistive Swit...]] | 2021 | 模拟电阻开关存储器存内学习综述：定义两层性能指标，分析器件特性、硬件算法、阵列映射、架构电路设计，评估现有器件性能，讨论从器件到系统的挑战与前景。 |
| [[Fusion of Memristor and Digital Compute-In-Memory Processing Units|Fusion of Memristor and Digital Compute-In-Me...]] | 2023 | 忆阻器-SRAM CIM 融合：77.64 TOPS/W、392μs 唤醒、<0.5% 精度损失、TSMC 22nm、自适应本地训练。 |
| [[sub-Supplementary Materials for Edge Learning Using Neuro-Inspired Memristor Chip|sub-Supplementary Materials for Edge Learning...]] | 2023 | STELLAR 边缘学习芯片补充材料：器件制备、STDP 规则、35x 能耗降低。 |
| [[Electrochemical ohmic memristors|Electrochemical ohmic memristors]] | 2024 | 本文提出电化学欧姆忆阻器，利用电化学机制实现可靠阻变切换和欧姆行为，面向神经形态计算应用。 |
| [[Electrochemical ohmic memristors for Electrochemical oh|Electrochemical ohmic memristors for Electroc...]] | 2024 | 本文提出电化学欧姆忆阻器，利用电化学机制实现可靠阻变切换和欧姆行为，面向神经形态计算应用。 |

## 相关概念

- [[RRAM]]
- [[ReRAM]]
- [[crossbar]]
- [[Neuromorphic computing]]
- [[In-memory computing]]
- [[selector]]
- [[Wiki 目录]]
