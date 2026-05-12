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
| [[Test-Time Training with Self-Supervision for Generalization under Distribution Shifts\|Test-Time Training with Self-Supervision...]] | 2020 | TTT开山之作：首次将自监督学习引入测试时自适应，将单样本转化为自监督任务在线更新模型。核心贡献是定义了Test-Time Training范式。来自UC Berkeley。 |
| [[Test-Time Classifier Adjustment Module for Model-Agnostic Domain Generalization\|Test-Time Classifier Adjustment Module f...]] | 2021 | 极简测试时DG：T3A无反向传播仅调整分类器原型，计算开销可忽略。核心贡献是证明测试时调整分类层原型即可有效应对域偏移，无需梯度优化。方法极简但为后续原型-based\ |
| [[Adaptive Risk Minimization Learning to Adapt to Domain Shift\|Adaptive Risk Minimization Learning to A...]] | 2021 | 提出ARM框架：不同于学习不变特征，直接优化模型在训练域上学会自适应，测试时无需重新训练即可应对分布偏移。理论分析了自适应与不变性的权衡，在DomainNet/Wilds等多个基准上验证，为TTA方法 |
| [[Improving Test-Time Adaptation via Shift-agnostic Weight Regularization and Nearest Source Prototypes\|Improving Test-Time Adaptation via Shift...]] | 2022 | 提出SWR：通过识别参数对分布偏移的敏感性来差异化更新幅度，使TTA能安全使用高学习率。+最近源原型辅助对齐。核心贡献是将参数敏感性分析引入TTA优化，实现更快更稳定的适配。来自工业界(Qualcom |
| [[Learning to Generalize across Domains on Single Test Samples\|Learning to Generalize across Domains on...]] | 2022 | 提出单样本测试时自适应框架：研究部分域泛化(PDG)场景，用元学习训练使模型仅需单个测试样本的一步梯度更新即可适应目标域。在部分标签空间的挑战性设置下验证有效性。 |
| [[Revisiting Realistic Test-Time Training Sequential Inference and Adaptation by Anchored Clustering\|Revisiting Realistic Test-Time Training ...]] | 2022 | TTT领域规范化工作：系统梳理TTT协议并提出sTTT+TTAC(锚定聚类匹配源-目标域聚类)。核心贡献是为TTT建立了清晰的评估协议，避免不公平比较。TTAC方法简单有效但主要价值在基准规范化。 |
| [[Probabilistic Test-Time Generalization by Variational Neighbor-Labeling\|Probabilistic Test-Time Generalization b...]] | 2023 | 将变分推理引入测试时域泛化：伪标签→伪标签分布(考虑不确定性)，邻居标签→变分邻居标签(融合邻近样本信息)，+元泛化阶段模拟泛化过程。核心贡献是为测试时域泛化建立了概率框架，理论优雅。来自AIM\ |
| [[Align Your Prompts Test-Time Prompting with Distribution Alignment for Zero-Shot Generalization\|Align Your Prompts Test-Time Prompting w...]] | 2023 | 提出PromptAlign：首次在测试时提示微调中显式对齐OOD样本与源数据的分布统计量（均值+方差），扩展TPT从单模态文本提示到多模态提示(MaPLe)，同时优化分布对齐损失和熵最小化。核心洞察： |
| [[Test-Time Style Shifting Handling Arbitrary Styles in Domain Generalization\|Test-Time Style Shifting Handling Arbitr...]] | 2023 | 测试时风格偏移将目标样本风格映射到最近源域风格，无需模型更新。核心贡献是风格层面的输入适配+风格平衡，简洁有效。来自KAIST。 |
| [[Energy-Based Test Sample Adaptation for Domain Generalization\|Energy-Based Test Sample Adaptation for ...]] | 2023 | 提出能量模型驱动的测试样本适配：用能量函数+Langevin动力学将目标样本迭代适配到源分布，而非修改模型。类别潜变量保持适配过程中的语义信息。核心贡献是将DG从模型适配范式转变为样本适配范式，与前一 |
| [[OST Improving Generalization of DeepFake Detection via One-Shot Test-Time Training\|OST Improving Generalization of DeepFake...]] | 2023 | 提出OST：首个将测试时训练引入深度伪造检测的工作。通过元学习实现单步梯度更新即可适应新伪造方法，解决跨生成方法泛化问题。在多个DeepFake基准上验证对未见伪造方法的泛化鲁棒性。 |
| [[Continual Test-Time Domain Adaptation\|Continual Test-Time Domain Adaptation]] | 2025 | 定义OCTTA新场景（持续域偏移+未知类），提出DOCO：动态ID/OOD分割+域补偿提示+结构正则化闭环框架，同时解决域自适应和OOD检测。首次将开集识别引入持续TTA，在多个基准上建立SOTA。 |
## 相关概念

- [[Test-time adaptation]]
- [[Distribution Shift]]
- [[Meta-Learning]]
- [[Wiki 目录]]
