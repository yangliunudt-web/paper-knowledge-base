---
title: Unsupervised Domain Adaptation
type: concept
tags: [概念, 进阶]
aliases: [UDA, unsupervised domain adaptation, 无监督域自适应, domain adaptation, DA]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: high
---

> 无监督域自适应（UDA）将源域训练模型适配到无标签的目标域。与 TTA 不同，UDA 通常假设可同时访问源域数据，而 TTA 在测试时仅有无标签目标数据。TTA 可视为 UDA 在测试阶段的特化形态。

## 定义

UDA 场景：有标注源域 + 无标注目标域，学习域不变特征或映射以弥合域差距。主要方法：对抗域自适应（DANN）、矩匹配（MMD）、自训练（伪标签）、图像翻译（CycleGAN）。TTA 是 UDA 在"无源数据、仅目标域、在线推理"约束下的特化。

## 关键特性

- **与 TTA 的关系**：TTA ⊂ UDA，多了"无源数据"和"在线推理"约束
- **测试时 UDA**：在医学影像中测试时逐受试者 UDA 是早期 TTA 应用
- **域感知 BN**：揭示 BN 中标签/域信息可分离，仅更新域相关部分
- **不确定性重加权**：Guiding Pseudo-labels 用不确定性估计减少伪标签噪声

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[The Norm Must Go On Dynamic Unsupervised Domain Adaptation by Normalization\|The Norm Must Go On Dynamic Unsupervised...]] | 2022 | 极简持续自适应：DUA仅持续更新BN统计量，<1%目标数据即可有效适配。核心贡献是展示了BN统计量持续更新在数据稀缺场景下的惊人有效性。来自TU Graz。 |
| [[Test-time Unsupervised Domain Adaptation\|Test-time Unsupervised Domain Adaptation]] | 2020 | 早期TTA医学影像应用：论证测试时逐受试者UDA优于传统UDA。核心贡献是将测试时自适应的概念引入医学影像领域。来自KCL/UCL。 |
| [[Test-time_Unsupervised_Domain_Adaptation\|Test-time_Unsupervised_Domain_Adaptation]] | 2020 | 早期TTA医学影像应用：逐受试者测试时UDA。来自KCL/UCL。 |
## 相关概念

- [[Test-time adaptation]]
- [[Domain Generalization]]
- [[Distribution Shift]]
- [[Pseudo-Labeling]]
- [[Wiki 目录]]
