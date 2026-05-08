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
| [[Fusion of Memristor and Digital Compute-In-Memory Processing Units\|Fusion of Memristor and Digital Compute-...]] | 2023 | 忆阻器-SRAM CIM 融合：77.64 TOPS/W、392μs 唤醒、<0.5% 精度损失、TSMC 22nm、自适应本地训练。 |
| [[Electrochemical ohmic memristors\|Electrochemical ohmic memristors]] | 2024 | 本文提出电化学欧姆忆阻器，利用电化学机制实现可靠阻变切换和欧姆行为，面向神经形态计算应用。 |
| [[Zn2+ Engineered Low-Barrier LiNbO3 Enables Visible-Light Programmable Ferroelectric Memristors for Noise-Immune Neuromorphic Vision\|Zn2+ Engineered Low-Barrier LiNbO3 Enabl...]] | 2025 | Lithium niobate (LiNbO ), owing to its unique [[ferroelectric polarization]] and\ |
| [[Scaling-up Resistive Synaptic Arrays for Neuro-inspired Architecture Challenges and Prospect\|Scaling-up Resistive Synaptic Arrays for...]] | 2016 | 讨论阻变突触器件交叉阵列规模扩展的挑战（器件非线性、有限精度、器件变异、IR 压降），提出差分读出消除关态电流、多单元平均减少变异、放宽线宽降低 IR |
| [[Neuro-Inspired Computing With Emerging Nonvolatile Memory\|Neuro-Inspired Computing With Emerging N...]] | 2018 | 综述新兴非易失性存储器件在神经启发式计算中的应用：涵盖相变/阻变/铁电存储器等突触器件、交叉阵列架构、器件‑电路‑算法协同设计，展望定制化学习算法。 |
| [[In-Memory Learning With Analog Resistive Switching Memory A Review and Perspective\|In-Memory Learning With Analog Resistive...]] | 2021 | 模拟电阻开关存储器存内学习综述：定义两层性能指标，分析器件特性、硬件算法、阵列映射、架构电路设计，评估现有器件性能，讨论从器件到系统的挑战与前景。 |
## 相关概念

- [[RRAM]]
- [[ReRAM]]
- [[crossbar]]
- [[Neuromorphic computing]]
- [[In-memory computing]]
- [[selector]]
- [[Wiki 目录]]
