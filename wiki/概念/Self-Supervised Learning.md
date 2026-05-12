---
title: Self-Supervised Learning
type: concept
tags: [概念, 基础]
aliases: [self-supervised learning, SSL, 自监督学习, self-supervision]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: high
---

> 自监督学习（SSL）从数据本身构造监督信号，无需人工标注。在 TTA 中，SSL 是 Test-Time Training 的核心——将测试样本转化为自监督任务（旋转预测、掩码重建、对比学习）以在线更新模型。

## 定义

SSL 通过预置任务（pretext task）从无标签数据中学习表征。预置任务包括：旋转预测、拼图、掩码图像建模（MIM）、对比学习。TTT 的核心创新在于训练时定义的 SSL 任务可在测试时直接复用以适应分布偏移。

## 关键特性

- **MIM 优于旋转**：MAE/TTT-MIM 验证 MIM 是当前最强 TTT 辅助任务
- **与 TTA 互补**：TTA 用熵最小化（无训练时准备）；TTT 用 SSL（需训练时设计辅助任务）
- **元学习统一**：MT³ 用元学习学习最优自监督损失，统一 SSL 和 TTA

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Test-Time Training with Self-Supervision for Generalization under Distribution Shifts\|Test-Time Training with Self-Supervision...]] | 2020 | TTT开山之作：首次将自监督学习引入测试时自适应，将单样本转化为自监督任务在线更新模型。核心贡献是定义了Test-Time Training范式。来自UC Berkeley。 |
| [[Test-Time Training with Masked Autoencoders\|Test-Time Training with Masked Autoencoders]] | 2022 | TTT+MAE：用掩码自编码器作为TTT的自监督任务，相比原始TTT(旋转预测)更有效。核心贡献是将MAE引入TTT框架并给出理论分析。来自UC Berkeley/Meta。 |
| [[Test-Time Domain Adaptation by Learning Domain-Aware Batch Normalization\|Test-Time Domain Adaptation by Learning ...]] | 2023 | 揭示BN层中标签/域信息分离的关键发现：仅更新BN仿射参数即可有效域自适应。辅助SSL分支+元学习双层优化对齐目标，推理时可丢弃。设计精巧且实用。来自北京交通大学。 |
| [[ClusT3 Information Invariant Test-Time Training\|ClusT3 Information Invariant Test-Time T...]] | 2023 | 提出ClusT3：将聚类与信息不变性结合用于TTT，通过聚类伪标签实现自监督自适应，在保持信息论属性的同时防止灾难性遗忘。无需源数据访问，在多个域偏移基准上验证有效性。 |
| [[Test-Time Personalization with a Transformer for Human Pose Estimation\|Test-Time Personalization with a Transfo...]] | 2023 | 将TTA拓展到姿态估计：Transformer桥接自监督与有监督关键点，测试时自监督微调实现个性化。核心贡献是将TTA从分类扩展到结构化预测任务，巧妙利用自监督信号。 |
| [[MT3 Meta Test-Time Training for Self-Supervised Test-Time Adaption\|MT3 Meta Test-Time Training for Self-Sup...]] | 2020 | 早期TTA奠基工作：将元学习引入测试时训练，通过自监督损失使模型学会如何适应分布偏移。核心贡献是用元学习框架统一了自监督学习和测试时自适应，单样本即可适配。方法优雅但在更复杂基准上未经充分验证。 |
## 相关概念

- [[Test-Time Training]]
- [[Test-time adaptation]]
- [[Contrastive Learning]]
- [[Meta-Learning]]
- [[Wiki 目录]]
