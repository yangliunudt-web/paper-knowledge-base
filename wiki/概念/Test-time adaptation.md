---
title: Test-time adaptation
type: concept
tags: [概念, 进阶]
aliases: [TTA, test-time adaptation, 测试时适应, fully test-time adaptation, online adaptation, 测试时自适应, Test-Time Domain Adaptation, test-time domain adaptation]
created: 2026-05-10
updated: 2026-05-10
sources: []
confidence: medium
---

> 测试时适应（TTA）是机器学习中的一种适应范式，模型在推理阶段仅利用输入测试数据（无需源数据或标签）在线调整自身参数以应对数据分布偏移，是边缘设备持续鲁棒推理的关键使能技术。

## 定义

与域适应（DA）需要目标域（部分）标注数据不同，TTA 在完全无监督的测试阶段进行。主要方法包括：熵最小化（TENT）、批归一化统计量自适应（AdaBN）、伪标签自训练、以及基于记忆库的对比学习。TTA 允许边缘设备在部署后持续适应环境变化。

## 关键特性

- **熵最小化**：通过最小化模型输出熵来增强预测置信度
- **BN 自适应**：仅调整 BN 层统计量（均值/方差）而不改变权重，参数效率极高
- **内存效率**：TTA 通常仅需少量额外内存（存储 BN 统计量或轻量级优化器状态）
- **与 CIM 的关系**：存内计算硬件能效高但存在器件非理想性（噪声/漂移），TTA 可补偿这些非理想性
- **持续学习连接**：TTA 可被视为单任务持续学习的一种特殊形式

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Evaluating Prediction-Time Batch Normalization for Robustness under Covariate Shift\|Evaluating Prediction-Time Batch Normali...]] | 2020 | 提出TTA领域最简单有效的基线：预测时用目标域小批量数据重算BN统计量。一行代码即可显著提升协变量偏移下的性能。核心贡献是揭示BN统计量适配在TTA中的重要性，为后续TTA方法(如TENT)奠定基础。 |
| [[MixNorm Test-Time Adaptation Through Online Normalization Estimation\|MixNorm Test-Time Adaptation Through Onl...]] | 2021 | 提出MixNorm解决TTA两大不切实际假设：突破了对大批次和单分布的依赖，用混合策略仅需单样本即可估计可靠BN统计量。同时提出了更贴近实际的评估协议(任意批次+多分布)。早期TTA重要工作，来自US |
| [[Tent Fully Test-Time Adaptation by Entropy Minimization\|Tent Fully Test-Time Adaptation by Entro...]] | 2021 | TTA领域开山之作：提出测试时熵最小化(TENT)仅优化BN层的仿射参数，仅需一轮测试时优化。核心贡献是定义了Fully Test-Time Adaptation范式并证明其简单有效。奠定了后续所有T |
| [[Test-Time Classifier Adjustment Module for Model-Agnostic Domain Generalization\|Test-Time Classifier Adjustment Module f...]] | 2021 | 极简测试时DG：T3A无反向传播仅调整分类器原型，计算开销可忽略。核心贡献是证明测试时调整分类层原型即可有效应对域偏移，无需梯度优化。方法极简但为后续原型-based\ |
| [[Adaptive Risk Minimization Learning to Adapt to Domain Shift\|Adaptive Risk Minimization Learning to A...]] | 2021 | 提出ARM框架：不同于学习不变特征，直接优化模型在训练域上学会自适应，测试时无需重新训练即可应对分布偏移。理论分析了自适应与不变性的权衡，在DomainNet/Wilds等多个基准上验证，为TTA方法 |
| [[Improving Test-Time Adaptation via Shift-agnostic Weight Regularization and Nearest Source Prototypes\|Improving Test-Time Adaptation via Shift...]] | 2022 | 提出SWR：通过识别参数对分布偏移的敏感性来差异化更新幅度，使TTA能安全使用高学习率。+最近源原型辅助对齐。核心贡献是将参数敏感性分析引入TTA优化，实现更快更稳定的适配。来自工业界(Qualcom |
| [[Test-time Batch Normalization\|Test-time Batch Normalization]] | 2022 | 分析BN训练与测试的不一致性，提出GpreBN保持训练时梯度形式+数据集级统计量。核心贡献是揭示了BN在TTA中的深层机制并提供了统一优化框架。来自MSRA。 |
| [[Learning to Generalize across Domains on Single Test Samples\|Learning to Generalize across Domains on...]] | 2022 | 提出单样本测试时自适应框架：研究部分域泛化(PDG)场景，用元学习训练使模型仅需单个测试样本的一步梯度更新即可适应目标域。在部分标签空间的挑战性设置下验证有效性。 |
| [[Test-time Batch Statistics Calibration for Covariate Shift\|Test-time Batch Statistics Calibration f...]] | 2022 | α-BN：源-目标统计量混合校准，兼顾域自适应和判别结构保持。Core框架进行成对类别相关优化。核心贡献是揭示TBN(纯目标统计量)的潜在危害并提出简单有效的混合策略。 |
| [[MEMO Test Time Robustness via Adaptation and Augmentation\|MEMO Test Time Robustness via Adaptation...]] | 2022 | 提出MEMO：仅用单测试点原始+增广视图的边际熵最小化适配全模型参数。无需假设训练过程，即插即用。单点TTA范式奠基性工作，ImageNet-C/R/A达SOTA。 |
| [[SITA Single Image Test-time Adaptation\|SITA Single Image Test-time Adaptation]] | 2022 | 将TTA推向极致：单样本+无反向传播。AugBN用标签保持变换估计测试BN统计量，极简极快。核心贡献是定义了SITA(单图像TTA)这个实用场景并给出了完全可行的解决方案。来自Stanford/Goo |
| [[Extrapolative Continuous-time Bayesian Neural Network for Fast Training-free Test-time Adaptation\|Extrapolative Continuous-time Bayesian N...]] | 2022 | 从神经科学内部预测建模获得灵感，提出ECBNN将TTA形式化为连续时间贝叶斯滤波问题：用随机动力系统描述模型参数演化，外推参数分布实现真正的免训练TTA。核心创新是将TTA从优化范式转变为预测/外推范 |
## 相关概念

- [[Edge computing]]
- [[In-memory computing]]
- [[Continual learning]]
- [[Transfer learning]]
- [[Wiki 目录]]
