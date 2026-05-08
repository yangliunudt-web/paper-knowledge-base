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
| [[Zn2+ Engineered Low-Barrier LiNbO3 Enables Visible-Light Programmable Ferroelectric Memristors for Noise-Immune Neuromorphic Vision\|Zn2+ Engineered Low-Barrier LiNbO3 Enabl...]] | 2025 | Lithium niobate (LiNbO ), owing to its unique [[ferroelectric polarization]] and\ |
## 相关概念

- [[In-memory computing]]
- [[Memristor]]
- [[Reservoir computing]]
- [[RRAM]]
- [[FeFET]]
- [[crossbar]]
- [[Wiki 目录]]
