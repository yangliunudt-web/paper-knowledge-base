---
title: Batch Normalization
type: concept
tags: [概念, 基础]
aliases: [BN, batch normalization, 批归一化, batch norm, Test-Time Batch Normalization, AdaBN]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: high
---

> 批归一化（BN）通过小批次统计量对层激活进行归一化，是深度学习的基础组件。在测试时自适应（TTA）中，BN 统计量的重估计和仿射参数的微调成为最轻量、最高效的自适应策略。

## 定义

BN 在训练时使用小批次均值/方差进行归一化，同时维护全局运行统计量用于推理。当测试数据分布偏移时，用目标域数据重估计 BN 统计量（AdaBN）或微调仿射参数（TENT）可显著提升鲁棒性，仅修改 <1% 模型参数。

## 关键特性

- **统计量重估计**：用目标域数据替代训练 running stats，一行代码即可实现
- **仿射参数微调**：TENT 仅优化 γ 和 β，参数效率极高
- **小批次敏感性**：小批次下统计量估计不可靠，类别多样性（非批次大小）是关键因素
- **层间差异**：不同 BN 层对域偏移敏感度不同，深层更敏感
- **退化风险**：纯目标统计量可能破坏判别结构，α-BN 源-目标混合可缓解

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Evaluating Prediction-Time Batch Normalization for Robustness under Covariate Shift\|Evaluating Prediction-Time Batch Normali...]] | 2020 | 提出TTA领域最简单有效的基线：预测时用目标域小批量数据重算BN统计量。一行代码即可显著提升协变量偏移下的性能。核心贡献是揭示BN统计量适配在TTA中的重要性，为后续TTA方法(如TENT)奠定基础。 |
| [[MixNorm Test-Time Adaptation Through Online Normalization Estimation\|MixNorm Test-Time Adaptation Through Onl...]] | 2021 | 提出MixNorm解决TTA两大不切实际假设：突破了对大批次和单分布的依赖，用混合策略仅需单样本即可估计可靠BN统计量。同时提出了更贴近实际的评估协议(任意批次+多分布)。早期TTA重要工作，来自US |
| [[Tent Fully Test-Time Adaptation by Entropy Minimization\|Tent Fully Test-Time Adaptation by Entro...]] | 2021 | TTA领域开山之作：提出测试时熵最小化(TENT)仅优化BN层的仿射参数，仅需一轮测试时优化。核心贡献是定义了Fully Test-Time Adaptation范式并证明其简单有效。奠定了后续所有T |
| [[Test-time Batch Normalization\|Test-time Batch Normalization]] | 2022 | 分析BN训练与测试的不一致性，提出GpreBN保持训练时梯度形式+数据集级统计量。核心贡献是揭示了BN在TTA中的深层机制并提供了统一优化框架。来自MSRA。 |
| [[Test-time Batch Statistics Calibration for Covariate Shift\|Test-time Batch Statistics Calibration f...]] | 2022 | α-BN：源-目标统计量混合校准，兼顾域自适应和判别结构保持。Core框架进行成对类别相关优化。核心贡献是揭示TBN(纯目标统计量)的潜在危害并提出简单有效的混合策略。 |
| [[NOTE Robust Continual Test-time Adaptation Against Temporal Correlation\|NOTE Robust Continual Test-time Adaptati...]] | 2022 | 首次揭示并解决TTA中的时间相关性问题：IABN(实例级BN纠正) + PBRS(预测平衡蓄水池采样模拟i.i.d.)。核心贡献是发现non-i.i.d.数据流是TTA的关键失败模式，提供完整的理论分 |
| [[SITA Single Image Test-time Adaptation\|SITA Single Image Test-time Adaptation]] | 2022 | 将TTA推向极致：单样本+无反向传播。AugBN用标签保持变换估计测试BN统计量，极简极快。核心贡献是定义了SITA(单图像TTA)这个实用场景并给出了完全可行的解决方案。来自Stanford/Goo |
| [[The Norm Must Go On Dynamic Unsupervised Domain Adaptation by Normalization\|The Norm Must Go On Dynamic Unsupervised...]] | 2022 | 极简持续自适应：DUA仅持续更新BN统计量，<1%目标数据即可有效适配。核心贡献是展示了BN统计量持续更新在数据稀缺场景下的惊人有效性。来自TU Graz。 |
| [[DomainAdaptor A Novel Approach to Test-time Adaptation\|DomainAdaptor A Novel Approach to Test-t...]] | 2023 | 提出DomainAdaptor：AdaMixBN动态融合训练/测试BN统计量+GEM广义熵最小化损失。统一框架在少数据未见域场景下表现突出，4个基准上一致超越Tent/T3A等SOTA方法。 |
| [[TTN A Domain-Shift Aware Batch Normalization in Test-Time Adaptation\|TTN A Domain-Shift Aware Batch Normaliza...]] | 2023 | CBN与TBN的智能插值：根据BN层对域偏移的敏感度动态调整混合比例。核心贡献是揭示不同BN层对域偏移敏感度不同这一关键发现，并据此设计了层自适应的归一化策略。来自Qualcomm\ |
| [[Test-Time Domain Adaptation by Learning Domain-Aware Batch Normalization\|Test-Time Domain Adaptation by Learning ...]] | 2023 | 揭示BN层中标签/域信息分离的关键发现：仅更新BN仿射参数即可有效域自适应。辅助SSL分支+元学习双层优化对齐目标，推理时可丢弃。设计精巧且实用。来自北京交通大学。 |
| [[Towards Stable Test-Time Adaptation in Dynamic Wild World\|Towards Stable Test-Time Adaptation in D...]] | 2023 | 揭示BN是TTA不稳定的根源，提出SAR用锐度感知优化+噪声过滤实现稳定TTA。核心贡献是首次系统分析TTA不稳定的原因并给出通用解决方案。来自华南理工和腾讯。 |
## 相关概念

- [[Test-time adaptation]]
- [[Distribution Shift]]
- [[Entropy Minimization]]
- [[Wiki 目录]]
