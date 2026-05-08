---
title: RRAM
type: concept
tags: [概念, 基础]
aliases: [ReRAM, 阻变存储器, resistive RAM, resistive switching memory, memristive memory]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> RRAM（Resistive Random Access Memory）是一种基于电阻切换的非易失存储器，利用材料在不同电阻态之间可逆切换存储信息，是存内计算和神经形态计算的核心器件之一。

## 定义

RRAM 通常是金属-绝缘体-金属（MIM）结构，在上下电极间施加电压使绝缘层发生可逆阻变。主流机理包括：价态变化记忆（VCM，氧空位迁移）、电化学金属化记忆（ECM/CBRAM，金属离子迁移）、热化学记忆（单极开关）。

## 关键特性

- **结构简单**：MIM 结构，单元面积小（4F² crossbar）
- **高速**：<1 ns 切换速度
- **低功耗**：fJ 级切换能量
- **多值能力**：通过 compliance current 控制细丝尺寸实现 >2 bit/cell
- **3D 集成**：1S1R（selector + RRAM）垂直堆叠
- **主要挑战**：cycle-to-cycle 变异、数据保持性（尤其是中间态）、forming 过程的高电压需求、sneak path 问题

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Monolithic 3D integration of 2D transistors and vertical RRAMs in 1T–4R structure for high-densi\|Monolithic 3D integration of 2D transist...]] | 2023 | 本文实验演示了MoS2晶体管与三维垂直RRAM的单片3D集成方案，制造温度低于300°C。MoS2晶体管可驱动VRRAM到4个电阻状态，电路级建模证实比平面存储具有更小面积、更快传输和更低能耗。为高能 |
| [[Few-Shot Graph Learning with Robust and Energy-Efficient Memory-Augmented GNN\|Few-Shot Graph Learning with Robust and ...]] | 2022 | 少样本图学习 MAGNN：256 Kb 1T1R RRAM、CORA 78% 准确率、70 倍延迟降低、60 倍能耗降低、中科院+香港大学。 |
## 相关概念

- [[Memristor]]
- [[ReRAM]]
- [[crossbar]]
- [[selector]]
- [[In-memory computing]]
- [[Neuromorphic computing]]
- [[Wiki 目录]]
