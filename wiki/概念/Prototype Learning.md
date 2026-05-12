---
title: Prototype Learning
type: concept
tags: [概念, 进阶]
aliases: [prototype learning, prototype-based, 原型学习, class prototype, feature prototype]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: medium
---

> 原型学习用类中心（prototype）代表每个类别在特征空间的表征。在 TTA 中，原型方法不需要梯度更新——仅调整分类器原型即可应对域偏移（T3A），或通过测试样本动态演化原型（DPE）。

## 定义

每个类别用一个特征向量（原型，通常为类内样本特征均值）表示。分类时用最近原型的距离/相似度决定类别。TTA 中可在线调整目标域原型而无需求导。

## 关键特性

- **免梯度 TTA**：T3A 仅调整分类器原型，计算开销可忽略
- **动态原型进化**：DPE 双原型进化无需反向传播通过文本编码器，速度 5-10x
- **图消息传递**：PROGRAM 原型图消息传播提升伪标签质量
- **最近邻原型**：嵌入空间最近邻比 softmax 分类器更鲁棒

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Test-Time Classifier Adjustment Module for Model-Agnostic Domain Generalization\|Test-Time Classifier Adjustment Module f...]] | 2021 | 极简测试时DG：T3A无反向传播仅调整分类器原型，计算开销可忽略。核心贡献是证明测试时调整分类层原型即可有效应对域偏移，无需梯度优化。方法极简但为后续原型-based\ |
| [[Improving Test-Time Adaptation via Shift-agnostic Weight Regularization and Nearest Source Prototypes\|Improving Test-Time Adaptation via Shift...]] | 2022 | 提出SWR：通过识别参数对分布偏移的敏感性来差异化更新幅度，使TTA能安全使用高学习率。+最近源原型辅助对齐。核心贡献是将参数敏感性分析引入TTA优化，实现更快更稳定的适配。来自工业界(Qualcom |
| [[Contrastive Test-Time Adaptation\|Contrastive Test-Time Adaptation]] | 2024 | 提出PTA：用知识原型替代缓存实现高效TTA，根据零样本置信度自适应加权更新原型，消除缓存检索开销。在保持CLIP 92%推理速度的同时，跨域基准准确率从65.64%提升至69.38%，显著优于TDA |
| [[On the Robustness of Open-World Test-Time Training Self-Training with Dynamic Prototype Expansion\|On the Robustness of Open-World Test-Tim...]] | 2024 | 开辟OWTTT(开放世界测试时训练)新方向：揭示现有TTT在强OOD污染下的脆弱性，提出自适应OOD剪枝+动态原型扩展+分布对齐三组件方案。核心贡献是将开放世界学习与TTA交叉，定义了新的评估场景和基 |
| [[Dual Prototype Evolving for Test-Time Generalization of Vision-Language Models\|Dual Prototype Evolving for Test-Time Ge...]] | 2024 | 提出DPE：双原型进化方法，在测试时从文本和视觉双模态创建并进化原型，通过累积平均和优先队列策略在线更新，引入可学习残差对齐跨模态特征。仅优化嵌入空间中的原型，无需反向传播通过文本编码器，速度比TPT |
## 相关概念

- [[Test-time adaptation]]
- [[Pseudo-Labeling]]
- [[Domain Generalization]]
- [[Wiki 目录]]
