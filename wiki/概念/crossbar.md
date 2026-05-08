---
title: crossbar
type: concept
tags: [概念, 基础]
aliases: [交叉阵列, crossbar array, Crossbar array, cross-point array, 交叉点阵列, memristor crossbar, crossbar array]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> Crossbar 阵列是存内计算的核心拓扑结构，由横向字线（word line）和纵向位线（bit line）交叉构成，每个交叉点放置一个存储/计算单元，利用物理定律完成矩阵向量乘法（MVM）。

## 定义

在 N×M crossbar 中，每行施加输入电压 V_i，每个交叉点电导 G_ij 代表权重，每列输出的电流 I_j = Σ V_i × G_ij（基尔霍夫定律 + 欧姆定律）天然实现 MVM。

## 关键特性

- **O(1) 复杂度 MVM**：模拟域一次并行完成 N×M MAC 运算
- **高密度**：4F² 单元面积，支持 3D 堆叠
- **非易失**：使用 FeFET/ReRAM 权重器件，断电保持
- **主要挑战**：
  - Sneak path：未选中单元的漏电流干扰输出精度
  - IR drop：互连线寄生电阻导致电压降
  - 写串扰：编程一个单元时影响相邻单元
  - 器件变异：权重精度受限于器件非理想性
- **解决方案**：1S1R（selector + RRAM）、1T1R、1FeFET1R 等接入结构

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[In-memory ferroelectric differentiator\|In-memory ferroelectric differentiator]] | 2024 | Nature Communications |
## 相关概念

- [[In-memory computing]]
- [[Memristor]]
- [[RRAM]]
- [[selector]]
- [[FeFET]]
- [[Neuromorphic computing]]
- [[Wiki 目录]]
