---
title: Meta-Learning
type: concept
tags: [概念, 进阶]
aliases: [meta-learning, learning to learn, 元学习, MAML, meta-training]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: high
---

> 元学习（Meta-Learning）通过学习"如何学习"，使模型具备快速适应新任务/域的能力。在 TTA 中，元学习赋予模型测试时仅需少量样本或几步梯度即可适应的泛化能力，ARM 和 MT³ 是代表性融合工作。

## 定义

元训练阶段模拟域偏移场景，优化模型初始化参数或自适应策略；元测试阶段面对新域时能快速适应。代表性方法：MAML（模型无关元学习）、原型网络、元学习自适应损失函数。

## 关键特性

- **学习如何适应**：训练时模拟域偏移，内化适应能力
- **少样本快速适应**：仅需 1-5 步梯度即可适应新域
- **与 TTA 融合**：MT³ 元学习统一自监督和 TTA；ARM 元学习域自适应策略
- **计算前置**：元训练开销大但测试时适应极快

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Adaptive Risk Minimization Learning to Adapt to Domain Shift\|Adaptive Risk Minimization Learning to A...]] | 2021 | 提出ARM框架：不同于学习不变特征，直接优化模型在训练域上学会自适应，测试时无需重新训练即可应对分布偏移。理论分析了自适应与不变性的权衡，在DomainNet/Wilds等多个基准上验证，为TTA方法 |
| [[Learning to Generalize across Domains on Single Test Samples\|Learning to Generalize across Domains on...]] | 2022 | 提出单样本测试时自适应框架：研究部分域泛化(PDG)场景，用元学习训练使模型仅需单个测试样本的一步梯度更新即可适应目标域。在部分标签空间的挑战性设置下验证有效性。 |
| [[Sketch3T Test-Time Training for Zero-Shot SBIR\|Sketch3T Test-Time Training for Zero-Sho...]] | 2022 | 将TTT拓展到草图检索：单张草图自适应的测试时训练+元学习分离主/辅任务更新。核心贡献是发现草图的测试时分布偏移问题并提出首个TTT解决方案。来自Surrey SketchX。 |
| [[Test-Time Domain Adaptation by Learning Domain-Aware Batch Normalization\|Test-Time Domain Adaptation by Learning ...]] | 2023 | 揭示BN层中标签/域信息分离的关键发现：仅更新BN仿射参数即可有效域自适应。辅助SSL分支+元学习双层优化对齐目标，推理时可丢弃。设计精巧且实用。来自北京交通大学。 |
| [[Probabilistic Test-Time Generalization by Variational Neighbor-Labeling\|Probabilistic Test-Time Generalization b...]] | 2023 | 将变分推理引入测试时域泛化：伪标签→伪标签分布(考虑不确定性)，邻居标签→变分邻居标签(融合邻近样本信息)，+元泛化阶段模拟泛化过程。核心贡献是为测试时域泛化建立了概率框架，理论优雅。来自AIM\ |
| [[OST Improving Generalization of DeepFake Detection via One-Shot Test-Time Training\|OST Improving Generalization of DeepFake...]] | 2023 | 提出OST：首个将测试时训练引入深度伪造检测的工作。通过元学习实现单步梯度更新即可适应新伪造方法，解决跨生成方法泛化问题。在多个DeepFake基准上验证对未见伪造方法的泛化鲁棒性。 |
| [[Test-Time Personalization with Meta Prompt for Gaze Estimation\|Test-Time Personalization with Meta Prom...]] | 2024 | 将TTA/meta prompt应用于视线估计个性化：元学习确保无监督提示更新与任务目标对齐。核心贡献是将NLP提示学习和元学习结合用于细粒度回归任务的个性化TTA。来自华为。 |
| [[Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks\|Model-Agnostic Meta-Learning for Fast Ad...]] | 2017 | 提出 MAML 模型无关元学习算法，通过二阶梯度优化初始参数，使模型在新任务上仅需 1-5 步梯度更新即可快速适应，在少样本分类、回归和强化学习上达到 |
| [[MT3 Meta Test-Time Training for Self-Supervised Test-Time Adaption\|MT3 Meta Test-Time Training for Self-Sup...]] | 2020 | 早期TTA奠基工作：将元学习引入测试时训练，通过自监督损失使模型学会如何适应分布偏移。核心贡献是用元学习框架统一了自监督学习和测试时自适应，单样本即可适配。方法优雅但在更复杂基准上未经充分验证。 |
| [[Dynamic Domain Generalization\|Dynamic Domain Generalization]] | 2022 | 提出DDG：通过元调节器根据输入数据动态扭曲网络参数，静态模型学习域共享特征，元调节器学习域特定特征，DomainMix模拟多域数据。实现免训练的测试时模型调整，即插即用，在多个DG基准上验证有效性。 |
## 相关概念

- [[Test-time adaptation]]
- [[Domain Generalization]]
- [[Self-Supervised Learning]]
- [[Wiki 目录]]
