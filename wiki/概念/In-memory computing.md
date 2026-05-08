---
title: In-memory computing
type: concept
tags: [概念, 基础]
aliases: [IMC, 存内计算, compute-in-memory, Compute-in-memory, CIM, processing-in-memory, PIM, in-memory processing, In‑memory computing, near-memory computing, 近存计算, 存算一体]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> 存内计算（IMC）是一种消除存储墙瓶颈的计算范式，在存储阵列内部直接执行计算操作，避免数据在处理器和存储器之间的频繁搬运。

## 定义

传统冯·诺依曼架构中，数据在 CPU 和存储器之间搬运消耗了大部分能耗和延迟（即存储墙）。IMC 利用存储阵列（如 crossbar）的物理定律（欧姆定律 + 基尔霍夫定律）原地完成矩阵向量乘法（MVM），大幅降低数据搬运开销。

## 关键特性

- **消除存储墙**：计算在存储单元内部完成，无数据搬运
- **高并行度**：crossbar 阵列天然支持大规模并行 MVM
- **模拟计算**：利用模拟域电流求和，一个周期完成 MAC 运算
- **非易失 IMC**：基于 FeFET/ReRAM/MRAM 可实现非易失存内计算，支持 instant-on
- **主要挑战**：模拟计算精度有限、器件变异、ADC/DAC 开销、耐久性

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| | | |

## 相关概念

- [[FeFET]]
- [[crossbar]]
- [[Memristor]]
- [[RRAM]]
- [[ReRAM]]
- [[Neuromorphic computing]]
- [[Reservoir computing]]
- [[存内计算]]
- [[Wiki 目录]]
