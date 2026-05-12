---
title: Pseudo-Labeling
type: concept
tags: [概念, 基础]
aliases: [pseudo-labeling, pseudo labels, 伪标签, self-training, pseudo-label, PL]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: high
---

> 伪标签是半监督学习的核心技术：用模型对无标签数据的预测作为"伪标签"进行自我训练。在 TTA 中，伪标签是熵最小化的自然延伸——高置信度预测转为硬/软标签，驱动进一步的自适应。

## 定义

模型对测试样本预测 class probabilities，取 argmax 或 top-k 经阈值过滤后作为伪标签，再用于监督式更新模型参数。核心挑战是伪标签噪声和确认偏误（confirmation bias）。

## 关键特性

- **最近邻伪标签**：嵌入空间最近邻比 softmax 更可靠（NINFO）
- **原型图消息传递**：PROGRAM 用图结构消息传递提升伪标签质量
- **不确定性估计**：变分邻居标签（VPN）将伪标签扩展为伪标签分布
- **统一框架**：TeSLA 互信息驱动自学习损失可学习对抗增强
- **源数据替代**：伪标签使 TTA 无需源数据即可自监督学习

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[If your data distribution shifts, use self-learning\|If your data distribution shifts, use se...]] | 2022 | 系统验证自学习(熵最小化+伪标签)在域偏移下的有效性：跨架构、预训练方式、偏移类型一致改善。实践价值高：无需源数据、超参数鲁棒、仅需少量epoch。提出ImageNet-D新基准，多个基准上达SOTA |
| [[Test-Time Adaptation via Self-Training with Nearest Neighbor Information\|Test-Time Adaptation via Self-Training w...]] | 2023 | 用最近邻替代分类器预测生成伪标签：核心洞察是嵌入空间的最近邻比softmax输出更可靠。多随机初始化模块集成提升鲁棒性。方法简洁有效，解决了TTA中伪标签不可靠这一核心问题。来自KAIST。 |
| [[SODA Robust Training of Test-Time Data Adaptors\|SODA Robust Training of Test-Time Data A...]] | 2023 | 黑盒TTA新范式：用ZOO训练数据适配器修改输入而非修改模型参数。核心贡献是将TTA从白盒扩展到黑盒场景，解决了隐私/知识产权约束下的分布偏移问题。数据适配器思路与DDA/GDA互补。 |
| [[Probabilistic Test-Time Generalization by Variational Neighbor-Labeling\|Probabilistic Test-Time Generalization b...]] | 2023 | 将变分推理引入测试时域泛化：伪标签→伪标签分布(考虑不确定性)，邻居标签→变分邻居标签(融合邻近样本信息)，+元泛化阶段模拟泛化过程。核心贡献是为测试时域泛化建立了概率框架，理论优雅。来自AIM\ |
| [[Guiding Pseudo-labels with Uncertainty Estimation for Test-Time Adaptation\|Guiding Pseudo-labels with Uncertainty E...]] | 2023 | 提出基于不确定性估计的SF-UDA方法：通过伪标签可靠性重加权+近邻知识聚合+对比正则化对抗伪标签噪声。负样本排除策略防止同类样本误作负对。VisDA-C/DomainNet/PACS均建立新SOTA |
| [[Visual Prompt Tuning for Test-time Domain Adaptation\|Visual Prompt Tuning for Test-time Domai...]] | 2023 | 将视觉提示微调引入TTA：DePT仅微调少量prompt参数+记忆库伪标签+分层自监督。核心贡献是参数高效TTA范式，数据效率极高(1%数据达全量性能)。来自AWS。 |
| [[PROGRAM PROtotype GRAph Model based Pseudo-Label Learning for Test-Time Adaptation\|PROGRAM PROtotype GRAph Model based Pseu...]] | 2024 | 解决TTA伪标签不可靠问题：PGM(原型图消息传递)生成高质量伪标签 + RST(一致性正则化+伪标签)鲁棒自训练。核心贡献是用图结构建模原型和样本关系来提升伪标签质量。方法可插拔集成到现有TTA基线 |
| [[Domain-Specific Block Selection and Paired-View Pseudo-Labeling for Online Test-Time Adaptation\|Domain-Specific Block Selection and Pair...]] | 2024 | 提出DPLOT：域特定模块选择+翻转成对视图伪标签生成，解决TTA中伪标签质量退化问题。仅用翻转增广避免强增广的域偏移，在CIFAR-C和ImageNet-C上以简单设计超越复杂TTA方法。 |
## 相关概念

- [[Test-time adaptation]]
- [[Entropy Minimization]]
- [[Self-Training]]
- [[Contrastive Learning]]
- [[Wiki 目录]]
