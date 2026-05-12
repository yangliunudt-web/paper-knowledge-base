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
| [[Test-Time Training with Self-Supervision for Generalization under Distribution Shifts\|Test-Time Training with Self-Supervision...]] | 2020 | TTT开山之作：首次将自监督学习引入测试时自适应，将单样本转化为自监督任务在线更新模型。核心贡献是定义了Test-Time Training范式。来自UC Berkeley。 |
| [[Evaluating Prediction-Time Batch Normalization for Robustness under Covariate Shift\|Evaluating Prediction-Time Batch Normali...]] | 2020 | 提出TTA领域最简单有效的基线：预测时用目标域小批量数据重算BN统计量。一行代码即可显著提升协变量偏移下的性能。核心贡献是揭示BN统计量适配在TTA中的重要性，为后续TTA方法(如TENT)奠定基础。 |
| [[MixNorm Test-Time Adaptation Through Online Normalization Estimation\|MixNorm Test-Time Adaptation Through Onl...]] | 2021 | 提出MixNorm解决TTA两大不切实际假设：突破了对大批次和单分布的依赖，用混合策略仅需单样本即可估计可靠BN统计量。同时提出了更贴近实际的评估协议(任意批次+多分布)。早期TTA重要工作，来自US |
| [[Adaptive Risk Minimization Learning to Adapt to Domain Shift\|Adaptive Risk Minimization Learning to A...]] | 2021 | 提出ARM框架：不同于学习不变特征，直接优化模型在训练域上学会自适应，测试时无需重新训练即可应对分布偏移。理论分析了自适应与不变性的权衡，在DomainNet/Wilds等多个基准上验证，为TTA方法 |
| [[Test-time Batch Normalization\|Test-time Batch Normalization]] | 2022 | 分析BN训练与测试的不一致性，提出GpreBN保持训练时梯度形式+数据集级统计量。核心贡献是揭示了BN在TTA中的深层机制并提供了统一优化框架。来自MSRA。 |
| [[Test-time Batch Statistics Calibration for Covariate Shift\|Test-time Batch Statistics Calibration f...]] | 2022 | α-BN：源-目标统计量混合校准，兼顾域自适应和判别结构保持。Core框架进行成对类别相关优化。核心贡献是揭示TBN(纯目标统计量)的潜在危害并提出简单有效的混合策略。 |
| [[If your data distribution shifts, use self-learning\|If your data distribution shifts, use se...]] | 2022 | 系统验证自学习(熵最小化+伪标签)在域偏移下的有效性：跨架构、预训练方式、偏移类型一致改善。实践价值高：无需源数据、超参数鲁棒、仅需少量epoch。提出ImageNet-D新基准，多个基准上达SOTA |
| [[Test-Time Training with Masked Autoencoders\|Test-Time Training with Masked Autoencoders]] | 2022 | TTT+MAE：用掩码自编码器作为TTT的自监督任务，相比原始TTT(旋转预测)更有效。核心贡献是将MAE引入TTT框架并给出理论分析。来自UC Berkeley/Meta。 |
| [[DomainAdaptor A Novel Approach to Test-time Adaptation\|DomainAdaptor A Novel Approach to Test-t...]] | 2023 | 提出DomainAdaptor：AdaMixBN动态融合训练/测试BN统计量+GEM广义熵最小化损失。统一框架在少数据未见域场景下表现突出，4个基准上一致超越Tent/T3A等SOTA方法。 |
| [[TTN A Domain-Shift Aware Batch Normalization in Test-Time Adaptation\|TTN A Domain-Shift Aware Batch Normaliza...]] | 2023 | CBN与TBN的智能插值：根据BN层对域偏移的敏感度动态调整混合比例。核心贡献是揭示不同BN层对域偏移敏感度不同这一关键发现，并据此设计了层自适应的归一化策略。来自Qualcomm\ |
| [[NC-TTT A Noise Constrastive Approach for Test-Time Training\|NC-TTT A Noise Constrastive Approach for...]] | 2023 | 提出NC-TTT：将测试时训练重构为对比学习框架，用噪声对比估计区分原始/增广视图实现TTT。无需源数据或标签，在CIFAR-C和ImageNet-C上实现更稳定的自适应，性能优于熵最小化方法。 |
| [[CAFA Class-Aware Feature Alignment for Test-Time Adaptation\|CAFA Class-Aware Feature Alignment for T...]] | 2023 | 提出CAFA：通过伪标签引导的类感知特征对齐，解决TTA中无法访问源数据标签导致的类判别性丢失问题。同时实现类判别目标表示和分布偏移缓解，无需额外超参数，6个数据集上一致超越Tent/EATA等基线。 |
## 相关概念

- [[Test-time adaptation]]
- [[Batch Normalization]]
- [[Domain Generalization]]
- [[Wiki 目录]]
