---
title: Distribution Shift
type: concept
tags: [概念, 基础]
aliases: [distribution shift, domain shift, covariate shift, 分布偏移, 协变量偏移, 域偏移, label shift, 标签偏移]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: high
---

> 分布偏移指训练数据与测试数据分布不一致的现象，是机器学习模型部署后性能下降的根本原因。测试时自适应（TTA）的核心目标就是在线应对各类分布偏移。

## 定义

分布偏移主要包括：协变量偏移（输入分布 P(x) 变化）、标签偏移（P(y) 变化）、概念偏移（P(y|x) 变化）。TTA 主要应对协变量偏移，如自然损坏（ImageNet-C）、风格变化、域迁移等。新近研究开始关注混合偏移（协变量+标签偏移同时发生）和开集偏移（含未知类别）。

## 关键特性

- **协变量偏移**：最常见，输入数据分布变化但条件分布不变
- **标签偏移**：类别先验变化，需与协变量偏移解耦处理
- **时间相关性**：non-i.i.d. 数据流中标签时间相关性是 TTA 关键失败模式
- **混合偏移**：真实场景中多种偏移同时发生，需综合应对
- **评估基准**：ImageNet-C（损坏）、ImageNet-R（风格）、DomainNet（域迁移）

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[TENT Fully Test-Time Adaptation by Entropy Minimization]] | 2021 | 定义 Fully TTA 应对协变量偏移，熵最小化 |

## 相关概念

- [[Test-time adaptation]]
- [[Batch Normalization]]
- [[Domain Generalization]]
- [[Wiki 目录]]
