---
title: Contrastive Learning
type: concept
tags: [概念, 进阶]
aliases: [contrastive learning, 对比学习, InfoNCE, contrastive loss, NC-TTT]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: high
---

> 对比学习通过拉近正样本对、推远负样本对来学习判别性表征。在 TTA 中，对比学习被用于替代熵最小化（SwapPrompt）、重构 TTT 优化目标（NC-TTT）、以及特征对齐（CAFA），提供了熵最小化之外的优化信号。

## 定义

对比学习核心是 InfoNCE 损失：对每个锚点样本，拉近其正样本（增广/同类），推远负样本（其他样本），学习嵌入空间中的判别结构。CLIP 的训练也是对比学习。

## 关键特性

- **交换预测**：SwapPrompt 用双提示+双增强视图对比学习替代熵最小化
- **噪声对比 TTT**：NC-TTT 将 TTT 重构为对比学习框架
- **特征对齐**：CAFA 类感知特征对齐结合伪标签和对比学习
- **激活匹配**：ActMAD 多层激活统计对齐

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[NC-TTT A Noise Constrastive Approach for Test-Time Training\|NC-TTT A Noise Constrastive Approach for...]] | 2023 | 提出NC-TTT：将测试时训练重构为对比学习框架，用噪声对比估计区分原始/增广视图实现TTT。无需源数据或标签，在CIFAR-C和ImageNet-C上实现更稳定的自适应，性能优于熵最小化方法。 |
| [[Guiding Pseudo-labels with Uncertainty Estimation for Test-Time Adaptation\|Guiding Pseudo-labels with Uncertainty E...]] | 2023 | 提出基于不确定性估计的SF-UDA方法：通过伪标签可靠性重加权+近邻知识聚合+对比正则化对抗伪标签噪声。负样本排除策略防止同类样本误作负对。VisDA-C/DomainNet/PACS均建立新SOTA |
| [[SwapPrompt Test-Time Prompt Adaptation for Vision-Language Models\|SwapPrompt Test-Time Prompt Adaptation f...]] | 2024 | 将自监督对比学习引入TPT：交换预测机制(Swap Prediction)利用双提示+双增强视图的对比学习增强在线提示。核心贡献是用对比学习替代熵最小化作为TPT优化目标，性能大幅提升逼近有监督CoO |
| [[Test-Time Distribution Normalization for Contrastively Learned Vision-language Models\|Test-Time Distribution Normalization for...]] | 2024 | 揭示CLIP点积推理的信息损失问题：DN用批次均值近似负样本使测试时操作与InfoNCE训练目标对齐。核心洞察深刻——测试过程应与训练目标一致，简单高效的即插即用方法。 |
## 相关概念

- [[Test-time adaptation]]
- [[Self-Supervised Learning]]
- [[CLIP]]
- [[Entropy Minimization]]
- [[Wiki 目录]]
