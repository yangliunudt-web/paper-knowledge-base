---
title: Multi-level cell
type: concept
tags: [概念, 进阶]
aliases: [MLC, 多级单元, 多位存储, multi-level storage, multi-bit cell, multilevel cell]
created: 2026-05-09
updated: 2026-05-09
sources: []
confidence: medium
---

> Multi-level cell (MLC) 是指在单个存储单元中存储多个比特（≥2 bits/cell）的技术，通过编程不同的电导/阈值电压/极化状态实现多值存储，是提升存储密度的关键技术路径。

## 定义

MLC 利用存储介质的模拟可调特性，在单个单元中编码多个离散状态。例如，2 bits/cell 需要 4 个可区分状态，3 bits/cell 需要 8 个状态。在 FeFET 中，通过控制铁电极化的部分翻转实现多级阈值电压；在 RRAM/PCM 中，通过控制编程电流/脉冲宽度实现多级电导状态。

## 关键特性

- **状态数 vs 可靠性权衡**：更多状态提升密度但缩小状态间距，增加读取错误率
- **FeFET MLC**：通过 gate pulse 幅度/宽度控制极化部分翻转，2-4 bits/cell 已有实验验证
- **RRAM MLC**：通过 compliance current 或多脉冲编程控制 filament 尺寸
- **PCM MLC**：利用非晶化比例在宽阻值范围内实现多级存储
- **写验证（write-verify）**：MLC 编程通常需要迭代写-读验证循环以保证状态精度
- **关键挑战**：器件变异、保持期间的 drift（PCM/RRAM）、读干扰、耐久性退化导致的窗口闭合

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[A Compact Writing Scheme for the Reliability Challenges in 1T Multi-Level FeFET Array Variation, Endurance, and Write Disturb]] | 2024 | | | [[Application and Benefits of Target Programming Algorithms for Ferroelectric HfO₂ Transistors]] | 2023 | | | [[Monolithic 3D Integration of High Endurance Multi-Bit Ferroelectric FET for Accelerating Compute-In-Memory]] | 2024 | | | [[Ferroelectric Analog Synaptic Transistors]] | 2019 | |

## 相关概念

- [[FeFET]]
- [[RRAM]]
- [[crossbar]]
- [[In-memory computing]]
- [[Wiki 目录]]
