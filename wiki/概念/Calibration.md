---
title: Calibration
type: concept
tags: [概念, 进阶]
aliases: [calibration, 校准, confidence calibration, ECE, expected calibration error, calibrated]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: medium
---

> 校准（Calibration）衡量模型预测置信度与实际准确率的一致性。在 TTA 中，熵最小化可能导致过度自信（overconfidence），校准成为重要评估维度。C-TPT 首次将校准显式引入 TPT 优化。

## 定义

完美校准：置信度 p 的预测中恰好有 p 比例的样本是正确的。Expected Calibration Error (ECE) 是常用校准度量。温度缩放（temperature scaling）是最简单有效的校准方法。

## 关键特性

- **文本特征分散度**：C-TPT 发现文本特征分散度与校准误差负相关
- **零温度边缘化**：ZERO 方法揭示温度参数是校准关键
- **能量模型视角**：TEA 将分类器转化为 EBM 同时解决泛化和校准
- **AETTA**：dropout 推断预测分歧估计模型在目标域性能，可检测 TTA 失败

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Evaluating Prediction-Time Batch Normalization for Robustness under Covariate Shift\|Evaluating Prediction-Time Batch Normali...]] | 2020 | 提出TTA领域最简单有效的基线：预测时用目标域小批量数据重算BN统计量。一行代码即可显著提升协变量偏移下的性能。核心贡献是揭示BN统计量适配在TTA中的重要性，为后续TTA方法(如TENT)奠定基础。 |
| [[C-TPT Calibrated Test-Time Prompt Tuning for Vision-Language Models via Text Feature Dispersion\|C-TPT Calibrated Test-Time Prompt Tuning...]] | 2024 | 首次将校准(calibration)引入测试时提示微调：发现文本特征分散度与校准误差强负相关，提出ATFD度量和C-TPT方法在TPT中联合优化准确率+校准。核心贡献是揭示CLIP内部属性与校准的关系 |
| [[TEA Test-time Energy Adaptation\|TEA Test-time Energy Adaptation]] | 2024 | 从能量模型视角重新解释TTA：将分类器转化为EBM，对齐模型分布与测试分布。核心贡献是为TTA建立了能量模型理论基础，同时解决泛化和校准两个维度。与Xiao等人的能量样本适配互补(一个适配模型，一个适 |
## 相关概念

- [[Test-time adaptation]]
- [[Test-Time Prompt Tuning]]
- [[Entropy Minimization]]
- [[CLIP]]
- [[Wiki 目录]]
