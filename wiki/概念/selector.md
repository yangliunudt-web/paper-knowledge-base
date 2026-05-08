---
title: selector
type: concept
tags: [概念, 进阶]
aliases: [选通管, select device, 选择器, access device, 1S1R]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> Selector 是交叉阵列中串联在每个存储单元上的选通器件，提供强烈的非线性 I-V 特性，抑制未选中单元的 sneak path 漏电流，是实现高密度 3D 存储/存内计算的关键元件。

## 定义

在 crossbar 中，未选中半选单元的漏电流（sneak path）会导致读取错误和额外功耗。Selector 提供类二极管的开关特性：低电压高阻/关断态 → 超过阈值电压后极低电阻/导通态。主流类型包括：OTS（Ovonic Threshold Switching）、MIT（Metal-Insulator Transition）、FA（Fast Access）selector、隧道结。

## 关键特性

- **高非线性比**：导通/关断电流比 > 10⁴
- **高速切换**：纳秒级
- **双向导通**（多数方案）：支持 bipolar RRAM 操作
- **高导通电流密度**：足够驱动 RRAM 的 SET/RESET
- **可缩放**：垂直堆叠实现 3D 集成
- **主要挑战****：导通电流密度 vs 非线性比的权衡、循环稳定性、与 RRAM 的 V 窗口匹配、forming 电压兼容

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[One-Pulse-Programmable Multi-Level PCMSelector Cross-Point Memory for 20 nm Half Pitch and Beyond\|One-Pulse-Programmable Multi-Level PCMSe...]] | 2024 | Nature Electronics |
## 相关概念

- [[RRAM]]
- [[crossbar]]
- [[Memristor]]
- [[In-memory computing]]
- [[Wiki 目录]]
