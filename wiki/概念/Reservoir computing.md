---
title: Reservoir computing
type: concept
tags: [概念, 进阶]
aliases: [RC, 储备池计算, echo state network, ESN, liquid state machine]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> 储备池计算（RC）是一种适合硬件实现的递归神经网络范式，将输入映射到高维动态空间后仅训练读出层，避免了对隐藏层权重的梯度传播，极大降低训练复杂度。

## 定义

RC 的核心思想：(1) 输入信号驱动一个固定/随机的动力学系统（储备池/reservoir），产生丰富的高维暂态响应；(2) 仅训练线性读出层（readout layer）完成分类/预测。因为储备池权重不需要训练，可使用物理器件（忆阻器、FeFET、光子器件等）的动态特性直接实现。

## 关键特性

- **简化训练**：仅读出层权重需训练（线性回归），无 BPTT
- **硬件友好**：物理器件的内在动态（memristor 衰减、spintronic 振荡）可直接作为储备池
- **适合边缘计算**：低功耗、低延迟实时信号处理
- **时间序列专长**：天然适合语音、ECG、混沌预测等时序任务
- **主要挑战**：
  - 储备池质量对性能影响大但难以定量设计
  - 多任务适应性不如端到端训练的 RNN
  - 物理储备池的噪声和稳定性

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| | | |

## 相关概念

- [[Neuromorphic computing]]
- [[Memristor]]
- [[In-memory computing]]
- [[Wiki 目录]]
