---
title: Transfer learning
type: concept
tags: [概念, 基础]
aliases: [transfer learning, 迁移学习, domain adaptation, 域适应, fine-tuning, 微调, parameter-efficient fine-tuning, PEFT, test-time adaptation]
created: 2026-05-10
updated: 2026-05-10
sources: []
confidence: medium
---

> 迁移学习是将在一个任务（源域）上学到的知识迁移到另一个相关任务（目标域）的机器学习范式。在深度学习时代，预训练-微调已成为标准实践：大规模预训练模型（如 ImageNet 分类器、LLM）通过微调适应下游任务。

## 定义

迁移学习涵盖多种子范式：标准微调（全参数更新）、参数高效微调（仅训练少量新增/选定参数）、域适应（减小源域-目标域分布差异）、零样本/少样本迁移、以及测试时适应（无源数据在线调整）。

## 关键特性

- **预训练-微调范式**：ImageNet 预训练 → 下游任务微调
- **参数高效微调（PEFT）**：LoRA、适配器、前缀微调等仅训练少量参数
- **域适应（DA）**：通过最小化分布差异（MMD、对抗训练）或自适应 BN（AdaBN）实现
- **测试时适应（TTA）**：无源数据、无标签，仅利用测试输入在线更新
- **边缘设备约束**：内存/算力限制驱动了对参数高效方法的需求

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Unsupervised Domain Adaptation by Backpropagation\|Unsupervised Domain Adaptation by Backpr...]] | 2015 | 提出 DANN 域对抗神经网络，通过梯度反转层实现域不变特征学习，在 MNIST→SVHN 等域适应任务上取得优异性能，开创深度域适应领域。 |
| [[Domain-Adversarial Training of Neural Networks\|Domain-Adversarial Training of Neural Ne...]] | 2016 | 领域对抗神经网络训练（DANN）：通过梯度反转层实现领域不变特征学习，处理同质/异质领域自适应，在标准基准上优于SOTA方法。 |
| [[Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks\|Model-Agnostic Meta-Learning for Fast Ad...]] | 2017 | 提出 MAML 模型无关元学习算法，通过二阶梯度优化初始参数，使模型在新任务上仅需 1-5 步梯度更新即可快速适应，在少样本分类、回归和强化学习上达到 |
| [[Adaptive Batch Normalization for Practical Domain Adaptation\|Adaptive Batch Normalization for Practic...]] | 2018 | AdaBN 域适应：调整 BN 统计量实现深度适应、无参数、无额外组件、可与现有方法互补。 |
| [[TinyTL Reduce Memory, Not Parameters for Efficient On-Device Learning\|TinyTL Reduce Memory, Not Parameters for...]] | 2020 | 提出 TinyTL 冻结权重仅学习偏置模块，引入轻量残差模块保持适应能力，实现内存节省高达 6.5 倍（对比全网络微调）或 7.3‑12.9 倍（结合特征提取器适配），准确率损失小。 |
| [[TENT Fully Test-Time Adaptation by Entropy Minimization\|TENT Fully Test-Time Adaptation by Entro...]] | 2021 | TENT 测试时适应：熵最小化、归一化统计+仿射变换、ImageNet-C SOTA、无需源数据/改变训练。 |
| [[LORA LOW-RANK ADAPTATION OF LARGE LANGUAGE MODELS\|LORA LOW-RANK ADAPTATION OF LARGE LANGUA...]] | 2021 | LoRA低秩适应：冻结预训练权重，注入可训练低秩矩阵，大幅减少可训练参数（GPT‑3 175B减少10,000倍），GPU内存需求降3倍，训练吞吐量高，无推理延迟，性能相当或优于全微调。 |
| [[Model Zoo A Growing “Brain” to Learn Continually\|Model Zoo A Growing “Brain” to Learn Con...]] | 2022 | Model Zoo：通过集成多个小模型实现持续学习，任务间协同可改善泛化误差，竞争则恶化，在多个基准上取得显著精度提升。 |
| [[Small Models are Valuable Plug-ins for Large Language Models\|Small Models are Valuable Plug-ins for L...]] | 2023 | 超上下文学习：将本地微调的小模型作为插件与大语言模型协同，提升监督任务性能，解决上下文学习不稳定性，增强小模型多语言与可解释能力。 |
## 相关概念

- [[Large language model]]
- [[Low-Rank Adaptation]]
- [[Test-time adaptation]]
- [[Continual learning]]
- [[Wiki 目录]]
