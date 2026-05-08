---
title: Continual learning
type: concept
tags: [概念, 进阶]
aliases: [持续学习, lifelong learning, incremental learning, 增量学习, continual learning, Continual Learning, class-incremental learning]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> 持续学习（Continual/Lifelong Learning）是机器学习中使模型在不遗忘已学知识的前提下持续学习新任务的研究方向，核心挑战是灾难性遗忘（catastrophic forgetting）。

## 定义

传统 DNN 在顺序学习多个任务时，新任务的梯度更新会覆盖旧任务的重要权重，导致旧任务性能急剧下降——即灾难性遗忘。持续学习方法通过正则化、记忆回放、动态架构等手段缓解此问题。

## 关键特性

- **正则化方法**：EWC、SI、MAS 等通过约束重要参数的变化来保护旧知识
- **记忆回放**：存储旧任务样本或生成伪样本（generative replay）进行联合训练
- **动态架构**：为新任务分配新参数（progressive networks），避免干扰已有参数
- **硬件实现**：FeFET/ReRAM 的多值存储天然支持多任务权重共存
- **主要挑战**：稳定性-可塑性困境、存储开销、任务边界检测

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Hybrid neural networks for continual learning inspired by corticohippocampal circuits\|Hybrid neural networks for continual lea...]] | 2025 | Nature Communications |
| [[A Comprehensive Survey of Continual Learning Theory, Method and Application\|A Comprehensive Survey of Continual Lear...]] | 2024 | Nature Communications |
| [[A Comprehensive Survey of Continual Learning Theory, Method and Application\|A Comprehensive Survey of Continual Lear...]] | 2024 | Nature Communications |
## 相关概念

- [[Catastrophic forgetting]]
- [[Neural network]]
- [[Neuromorphic computing]]
- [[Wiki 目录]]
