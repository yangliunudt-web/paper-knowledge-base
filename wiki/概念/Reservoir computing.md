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
| [[Analog reservoir computing via ferroelectric mixed phase boundary transistors|Analog reservoir computing via ferroelectric ...]] | 2024 | 利用 HfZrOx 混相边界材料的双栅 TFT 实现全集成模拟储备池计算系统，MPB TFT 作物理储备池和神经元，FeTFT 作突触，实现 5-bit |
| [[Physical reservoir computing with emerging electronics|Physical reservoir computing with emerging el...]] | 2024 | 综述新兴电子器件在物理储备计算中的应用：涵盖电子、光学、机械器件等物理系统，讨论架构、节点、输入输出层、性能基准和竞争力，展望技术挑战与未来方向。 |
| [[Reservoir Computing System with Diverse Input Patterns in HfAlO-Based Ferroelectric Memristor|Reservoir Computing System with Diverse Input...]] | 2024 | 实现基于 Al 掺杂 HfO 铁电忆阻器的储备池计算系统，演示可处理多种输入脉冲类型的鲁棒储备池层，模拟生物突触短期可塑性，验证图像训练和巴甫洛夫实验等应用。 |
| [[Reservoir Computing Utilizing a Complementary Combination of n- and p-Channel FeFETs|Reservoir Computing Utilizing a Complementary...]] | 2024 | n‑p FeFET互补组合实现储备池计算，利用器件互补特性提升非线性变换能力，结合反转数字输入可进一步优化性能。 |
| [[Zn2+ Engineered Low-Barrier LiNbO3 Enables Visible-Light Programmable Ferroelectric Memristors for Noise-Immune Neuromorphic Vision|Zn2+ Engineered Low-Barrier LiNbO3 Enables Vi...]] | 2025 | | |
| [[Ultralow‑power reservoir computing based on bidirectionally operable ferroelectric capacitors with tunable time constants|Ultralow‑power reservoir computing based on b...]] | 2026 | 铁电电容器‑线性电容器串联器件实现超低功耗储备计算，具备双向操作和可调时间常数，在波形分类、多模态数字识别和 Mackey‑Glass 时间序列预测中表现优异。 |

## 相关概念

- [[Neuromorphic computing]]
- [[Memristor]]
- [[In-memory computing]]
- [[Wiki 目录]]
