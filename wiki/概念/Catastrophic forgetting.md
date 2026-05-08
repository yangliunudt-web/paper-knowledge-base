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
| [[Electrochemical ohmic memristors\|Electrochemical ohmic memristors]] | 2024 | 本文提出电化学欧姆忆阻器，利用电化学机制实现可靠阻变切换和欧姆行为，面向神经形态计算应用。 |
| [[Hybrid neural networks for continual learning inspired by corticohippocampal circuits\|Hybrid neural networks for continual lea...]] | 2025 | CH-HNN混合神经网络模型，模拟皮质-海马回路的双重记忆表征。ANN+SNN混合架构，结合元可塑性机制动态调节学习率。在任务增量和类别增量学习场景中表现优异，SNN组件支持低功耗神经形态硬件部署。 |
| [[Overcoming Catastrophic Forgetting with Hard Attention to the Task\|Overcoming Catastrophic Forgetting with ...]] | 2018 | 硬注意力任务机制：通过任务特定掩码保留旧任务信息，将灾难性遗忘率降低45‑80%，具备超参数鲁棒性和监控能力。 |
| [[Isolation and Impartial Aggregation A Paradigm of Incremental Learning without Interference\|Isolation and Impartial Aggregation A Pa...]] | 2022 | 阶段隔离增量学习框架+能量自归一化策略，避免灾难性遗忘，四个基准数据集SOTA。 |
| [[Meta-attention for ViT-backed Continual Learning\|Meta-attention for ViT-backed Continual ...]] | 2022 | 采用混合神经网络+元可塑性+参数隔离的方法，解决持续学习中的灾难性遗忘问题。在多个基准数据集上验证，性能优于现有方法。 |
| [[Forget-free Continual Learning with Winning Subnetworks\|Forget-free Continual Learning with Winn...]] | 2022 | 获胜子网络持续学习方法：基于彩票假设，学习任务自适应二进制掩码，重用先前子网络权重，免疫灾难性遗忘，掩码霍夫曼编码实现容量亚线性增长。 |
| [[A Comprehensive Survey of Continual Learning Theory, Method and Application\|A Comprehensive Survey of Continual Lear...]] | 2024 | 全面综述持续学习的理论、方法和应用。定义核心目标为稳定性-可塑性权衡和跨任务泛化能力。提出五类方法分类：正则化、回放、优化、表示和架构方法。系统性分析各类方法的优缺点和适用场景。 |
## 相关概念

- [[Continual learning]]
- [[Neural network]]
- [[Neuromorphic computing]]
- [[Wiki 目录]]
