---
title: Batch Normalization
type: concept
tags: [概念, 基础]
aliases: [BN, batch normalization, 批归一化, batch norm, Test-Time Batch Normalization, AdaBN]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: high
---

> 批归一化（BN）通过小批次统计量对层激活进行归一化，是深度学习的基础组件。在测试时自适应（TTA）中，BN 统计量的重估计和仿射参数的微调成为最轻量、最高效的自适应策略。

## 定义

BN 在训练时使用小批次均值/方差进行归一化，同时维护全局运行统计量用于推理。当测试数据分布偏移时，用目标域数据重估计 BN 统计量（AdaBN）或微调仿射参数（TENT）可显著提升鲁棒性，仅修改 <1% 模型参数。

## 关键特性

- **统计量重估计**：用目标域数据替代训练 running stats，一行代码即可实现
- **仿射参数微调**：TENT 仅优化 γ 和 β，参数效率极高
- **小批次敏感性**：小批次下统计量估计不可靠，类别多样性（非批次大小）是关键因素
- **层间差异**：不同 BN 层对域偏移敏感度不同，深层更敏感
- **退化风险**：纯目标统计量可能破坏判别结构，α-BN 源-目标混合可缓解

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[TENT Fully Test-Time Adaptation by Entropy Minimization]] | 2021 | TENT 开创 BN 仿射参数在线优化范式，仅优化 <1% 参数 |
| [[DELTA Degradation-free Fully Test-time Adaptation]] | 2023 | BN 校准+特征对齐实现无退化 TTA |

## 相关概念

- [[Test-time adaptation]]
- [[Distribution Shift]]
- [[Entropy Minimization]]
- [[Wiki 目录]]
