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
| [[A Comprehensive Survey of Continual Learning Theory, Method and Application\|A Comprehensive Survey of Continual Lear...]] | 2024 | 持续学习综述：五类方法（正则化/回放/优化/表示/架构），系统性分析稳定性-可塑性权衡。 |
| [[Hybrid neural networks for continual learning inspired by corticohippocampal circuits\|Hybrid neural networks for continual lea...]] | 2025 | CH-HNN混合神经网络模型，模拟皮质-海马回路的双重记忆表征。ANN+SNN混合架构，结合元可塑性机制动态调节学习率。在任务增量和类别增量学习场景中表现优异，SNN组件支持低功耗神经形态硬件部署。 |
| [[PackNet Adding Multiple Tasks to a Single Network by Iterative Pruning\|PackNet Adding Multiple Tasks to a Singl...]] | 2018 | 提出 PackNet 通过迭代剪枝实现持续学习：先剪枝释放冗余参数，再用释放的参数学习新任务，每个任务只需存储二进制掩码，在 VGG-16 上成功添加 |
| [[Overcoming Catastrophic Forgetting with Hard Attention to the Task\|Overcoming Catastrophic Forgetting with ...]] | 2018 | 硬注意力任务机制：通过任务特定掩码保留旧任务信息，将灾难性遗忘率降低45‑80%，具备超参数鲁棒性和监控能力。 |
| [[Piggyback Adapting a Single Network to Multiple Tasks by Learning to Mask Weights\|Piggyback Adapting a Single Network to M...]] | 2018 | Piggyback方法：通过可微分学习二进制掩码，固定骨干网络适应多任务，每参数1位开销，避免灾难性遗忘，任务顺序无关，性能与专用微调网络相当。 |
| [[Overcoming Catastrophic Forgetting with Synaptic Intelligence\|Overcoming Catastrophic Forgetting with ...]] | 2018 | Progress & Compress 持续学习：知识库+主动列双网络、蒸馏保护、无架构增长、Atari 游戏验证。 |
| [[Supermasks in Superposition\|Supermasks in Superposition]] | 2020 | 提出 SupSup 模型，利用固定随机权重网络上的超级掩码实现顺序学习数千任务而不遗忘，通过梯度优化推断任务标识，单步即可在 2500 任务中识别正确掩码。 |
| [[Isolation and Impartial Aggregation A Paradigm of Incremental Learning without Interference\|Isolation and Impartial Aggregation A Pa...]] | 2022 | 阶段隔离增量学习框架+能量自归一化策略，避免灾难性遗忘，四个基准数据集SOTA。 |
| [[Meta-attention for ViT-backed Continual Learning\|Meta-attention for ViT-backed Continual ...]] | 2022 | 采用混合神经网络+元可塑性+参数隔离的方法，解决持续学习中的灾难性遗忘问题。在多个基准数据集上验证，性能优于现有方法。 |
| [[Forget-free Continual Learning with Winning Subnetworks\|Forget-free Continual Learning with Winn...]] | 2022 | 获胜子网络持续学习方法：基于彩票假设，学习任务自适应二进制掩码，重用先前子网络权重，免疫灾难性遗忘，掩码霍夫曼编码实现容量亚线性增长。 |
| [[Helpful or Harmful Inter-Task Association in Continual Learning\|Helpful or Harmful Inter-Task Associatio...]] | 2022 | 持续学习中的任务关联分析：通过模型搜索区分有益/有害旧任务知识，结合敏感性度量发现任务间协作关系，在任务/类增量场景中优于多种基线，缓解灾难性遗忘。 |
## 相关概念

- [[Catastrophic forgetting]]
- [[Neural network]]
- [[Neuromorphic computing]]
- [[Wiki 目录]]
