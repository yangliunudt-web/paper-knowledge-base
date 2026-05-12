---
title: Continual Test-Time Adaptation
type: concept
tags: [概念, 进阶]
aliases: [continual TTA, CTTA, online TTA, continual test-time adaptation, 持续测试时自适应, continual online adaptation]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: high
---

> 持续测试时自适应（CTTA）将 TTA 从单批次扩展到持续变化的在线数据流：模型在非平稳环境中连续接收测试样本并自适应，同时需防止灾难性遗忘和错误累积。

## 定义

与标准 TTA（固定目标域、单轮自适应）不同，CTTA 面对持续变化的分布（天气渐变、昼夜交替、传感器老化）。核心挑战：如何在持续自适应中保持稳定性，不遗忘之前学到的适应能力。

## 关键特性

- **灾难性遗忘**：模型持续更新会覆盖先前的适应，EcoTTA 用自蒸馏+元网络缓解
- **内存效率**：EcoTTA ResNet-50 省 86% 内存；CoTTA 教师-学生框架
- **卡尔曼滤波**：CMF 用卡尔曼滤波对 SGD 参数去噪，滤波+集成精炼
- **贝叶斯视角**：SLWI 贝叶斯滤波推理 OTTA 权重，识别非稳态权重
- **输入自适应范式**：Decorate the Newcomers 视觉域提示重构输入替代模型更新

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[NOTE Robust Continual Test-time Adaptation Against Temporal Correlation\|NOTE Robust Continual Test-time Adaptati...]] | 2022 | 首次揭示并解决TTA中的时间相关性问题：IABN(实例级BN纠正) + PBRS(预测平衡蓄水池采样模拟i.i.d.)。核心贡献是发现non-i.i.d.数据流是TTA的关键失败模式，提供完整的理论分 |
| [[EcoTTA Memory-Efficient Continual Test-time Adaptation via Self-distilled Regularization\|EcoTTA Memory-Efficient Continual Test-t...]] | 2023 | 提出EcoTTA：轻量元网络+自蒸馏正则化，大幅降低持续TTA内存消耗（ResNet-50省86%），同时解决灾难性遗忘和误差累积。在分类和语义分割上超越CoTTA等SOTA。 |
| [[Decorate the Newcomers Visual Domain Prompt for Continual Test Time Adaptation\|Decorate the Newcomers Visual Domain Pro...]] | 2024 | 将CTTA从模型自适应范式转变为输入自适应范式：冻结模型+学习视觉域提示(Domain-specific + Domain-agnostic)来重构输入，稳态策略抑制域敏感参数。核心贡献是从根本上绕过 |
## 相关概念

- [[Test-time adaptation]]
- [[Continual learning]]
- [[Catastrophic forgetting]]
- [[Distribution Shift]]
- [[Wiki 目录]]
