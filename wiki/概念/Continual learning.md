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
| [[Incorporating neuro-inspired adaptability for continual learning in artificial intelligence\|Incorporating neuro-inspired adaptabilit...]] | 2022 | 元可塑性+参数隔离方法，解决持续学习灾难性遗忘，多场景SOTA整体性能。 |
| [[Hybrid neural networks for continual learning inspired by corticohippocampal circuits\|Hybrid neural networks for continual lea...]] | 2025 | CH-HNN混合神经网络模型，模拟皮质-海马回路的双重记忆表征。ANN+SNN混合架构，结合元可塑性机制动态调节学习率。在任务增量和类别增量学习场景中表现优异，SNN组件支持低功耗神经形态硬件部署。 |
| [[Piggyback Adapting a Single Network to Multiple Tasks by Learning to Mask Weights\|Piggyback Adapting a Single Network to M...]] | 2018 | Piggyback方法：通过可微分学习二进制掩码，固定骨干网络适应多任务，每参数1位开销，避免灾难性遗忘，任务顺序无关，性能与专用微调网络相当。 |
| [[Supermasks in Superposition\|Supermasks in Superposition]] | 2020 | 提出 SupSup 模型，利用固定随机权重网络上的超级掩码实现顺序学习数千任务而不遗忘，通过梯度优化推断任务标识，单步即可在 2500 任务中识别正确掩码。 |
| [[Isolation and Impartial Aggregation A Paradigm of Incremental Learning without Interference\|Isolation and Impartial Aggregation A Pa...]] | 2022 | 阶段隔离增量学习框架+能量自归一化策略，避免灾难性遗忘，四个基准数据集SOTA。 |
| [[Helpful or Harmful Inter-Task Association in Continual Learning\|Helpful or Harmful Inter-Task Associatio...]] | 2022 | 持续学习中的任务关联分析：通过模型搜索区分有益/有害旧任务知识，结合敏感性度量发现任务间协作关系，在任务/类增量场景中优于多种基线，缓解灾难性遗忘。 |
| [[Class-Incremental Learning A Survey\|Class-Incremental Learning A Survey]] | 2024 | 类增量学习综述：全面总结 CIL 方法，对 17 种方法进行基准评估，倡导基于内存预算的公平比较和内存无关的性能度量。 |
| [[Learning to Continually Learn\|Learning to Continually Learn]] | 2020 | 提出 ANML 神经调制元学习算法，通过元学习激活门控函数实现持续学习，可顺序学习多达 600 个类别而避免灾难性遗忘。 |
| [[A Model or 603 Exemplars Towards Memory-Efficient Exemplar-Free Continual Learning\|A Model or 603 Exemplars Towards Memory-...]] | 2022 | 无样本持续学习内存优化：单一模型替代样本存储，竞争性能+低内存占用。 |
## 相关概念

- [[Catastrophic forgetting]]
- [[Neural network]]
- [[Neuromorphic computing]]
- [[Wiki 目录]]
