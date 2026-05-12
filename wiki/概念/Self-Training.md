---
title: Self-Training
type: concept
tags: [概念, 基础]
aliases: [self-training, 自训练, iterative self-training]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: medium
---

> 自训练（Self-Training）是半监督学习的经典方法：用模型对无标签数据的预测作为监督信号迭代训练自身。在 TTA 中，自训练是熵最小化的延伸——高置信度预测转为伪标签驱动在线自适应。

## 定义

自训练循环：模型预测 → 高置信度样本选中 → 作为伪标签 → 更新模型 → 重复。TTA 中通常只做一轮（one-epoch），避免错误累积。关键设计：伪标签质量过滤、更新范围控制（仅 BN 参数/全参数/选择性）、温度缩放。

## 关键特性

- **TENT 本质**：熵最小化可视为软自训练的一种形式
- **伪标签质量**：是自训练成功的关键，从简单的置信度阈值到图消息传递
- **Tri-net 架构**：TRIBE 三网络+锚定损失将 TTA 推向真实综合场景
- **无源数据**：自训练使 TTA 无需访问源域数据即可适配

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Test-Time Adaptation via Self-Training with Nearest Neighbor Information\|Test-Time Adaptation via Self-Training w...]] | 2023 | 用最近邻替代分类器预测生成伪标签：核心洞察是嵌入空间的最近邻比softmax输出更可靠。多随机初始化模块集成提升鲁棒性。方法简洁有效，解决了TTA中伪标签不可靠这一核心问题。来自KAIST。 |
| [[PROGRAM PROtotype GRAph Model based Pseudo-Label Learning for Test-Time Adaptation\|PROGRAM PROtotype GRAph Model based Pseu...]] | 2024 | 解决TTA伪标签不可靠问题：PGM(原型图消息传递)生成高质量伪标签 + RST(一致性正则化+伪标签)鲁棒自训练。核心贡献是用图结构建模原型和样本关系来提升伪标签质量。方法可插拔集成到现有TTA基线 |
| [[Towards Real-World Test-Time Adaptation Tri-net Self-Training with Balanced Normalization\|Towards Real-World Test-Time Adaptation ...]] | 2024 | 最全面的真实TTA场景：同时处理non-i.i.d.+持续域偏移+类别不平衡。平衡BN+TRIBE三网络架构+锚定损失。核心贡献是将TTA推向更真实的综合场景。来自华南理工(I2R/CUHK-SZ)。 |
| [[On the Robustness of Open-World Test-Time Training Self-Training with Dynamic Prototype Expansion\|On the Robustness of Open-World Test-Tim...]] | 2024 | 开辟OWTTT(开放世界测试时训练)新方向：揭示现有TTT在强OOD污染下的脆弱性，提出自适应OOD剪枝+动态原型扩展+分布对齐三组件方案。核心贡献是将开放世界学习与TTA交叉，定义了新的评估场景和基 |
## 相关概念

- [[Test-time adaptation]]
- [[Pseudo-Labeling]]
- [[Entropy Minimization]]
- [[Wiki 目录]]
