---
title: Domain Generalization
type: concept
tags: [概念, 进阶]
aliases: [domain generalization, DG, 域泛化, test-time domain generalization, out-of-distribution generalization]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: high
---

> 域泛化（DG）旨在从多个源域学习一个能泛化到未见目标域的模型。与域自适应（DA）不同，DG 在训练和测试阶段均不访问目标域数据。测试时域泛化（TTDG）进一步允许在推理时利用无标签测试样本进行在线适配。

## 定义

DG 假设训练时有多源域数据但测试时目标域完全未知。主要方法包括：域不变特征学习、元学习、数据增强、集成策略。TTDG 融合 DG 和 TTA 思想，在测试时用无标签数据微调模型以应对特定目标域偏移。

## 关键特性

- **无需目标域数据**：训练时不可见目标域，区别于 DA
- **多源域假设**：依赖源域多样性学习不变表征
- **与 TTA 的区别**：TTA 在测试时在线更新模型；DG 训练时就设计好泛化能力
- **TTDG 融合范式**：测试时域泛化结合在线自适应，取两者之长

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Adaptive Risk Minimization Learning to Adapt to Domain Shift]] | 2021 | ARM 元学习框架：测试时无需重训练即可自适应 |

## 相关概念

- [[Test-time adaptation]]
- [[Distribution Shift]]
- [[Meta-Learning]]
- [[Wiki 目录]]
