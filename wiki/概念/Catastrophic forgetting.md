---
title: Catastrophic forgetting
type: concept
tags: [概念, 进阶]
aliases: [灾难性遗忘, catastrophic interference, 灾难性干扰]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> 灾难性遗忘（Catastrophic Forgetting）是持续学习的核心挑战：神经网络在学习新任务时，先前学习任务的性能会急剧下降，因为新知识的梯度更新破坏了表示旧知识的权重配置。

## 定义

灾难性遗忘源于神经网络的"分布式表示"特性——同一组权重参与表示多个概念/任务，新任务的训练信号不可避免地干扰已有表示。缓解方案参见 [[Continual learning]]。

## 关键特性

- **程度衡量**：用 backward transfer（BWT）和 forward transfer（FWT）指标量化
- **与生物脑的对比**：生物脑也经历遗忘，但通过睡眠重放、互补学习系统（海马体+新皮层）机制显著缓解
- **硬件维度**：新兴存储器件（FeFET/ReRAM）的多电导态使参数空间更大，可能提供更好的抗遗忘能力
- **主要挑战**：在有限存储（不保存所有旧数据）和计算预算下达到可接受的遗忘率

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Incorporating neuro-inspired adaptability for continual learning in artificial intelligence\|Incorporating neuro-inspired adaptabilit...]] | 2022 | 元可塑性+参数隔离方法，解决持续学习灾难性遗忘，多场景SOTA整体性能。 |
| [[A Comprehensive Survey of Continual Learning Theory, Method and Application\|A Comprehensive Survey of Continual Lear...]] | 2024 | 持续学习综述：五类方法（正则化/回放/优化/表示/架构），系统性分析稳定性-可塑性权衡。 |
| [[Supermasks in Superposition\|Supermasks in Superposition]] | 2020 | 提出 SupSup 模型，利用固定随机权重网络上的超级掩码实现顺序学习数千任务而不遗忘，通过梯度优化推断任务标识，单步即可在 2500 任务中识别正确掩码。 |
| [[Isolation and Impartial Aggregation A Paradigm of Incremental Learning without Interference\|Isolation and Impartial Aggregation A Pa...]] | 2022 | 阶段隔离增量学习框架+能量自归一化策略，避免灾难性遗忘，四个基准数据集SOTA。 |
| [[Class-Incremental Learning A Survey\|Class-Incremental Learning A Survey]] | 2024 | 类增量学习综述：全面总结 CIL 方法，对 17 种方法进行基准评估，倡导基于内存预算的公平比较和内存无关的性能度量。 |
## 相关概念

- [[Continual learning]]
- [[Neural network]]
- [[Neuromorphic computing]]
- [[Wiki 目录]]
