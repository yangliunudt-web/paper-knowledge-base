---
title: CLIP
type: concept
tags: [概念, 基础]
aliases: [CLIP, Contrastive Language-Image Pre-training, vision-language models, VLM, VLMs]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: high
---

> CLIP（Contrastive Language-Image Pre-training）通过对比学习对齐图像和文本表征，是视觉-语言基础模型的核心范式。在测试时自适应中，CLIP 的零样本能力和可提示特性催生了提示词优化（TPT）等 TTA 新范式。

## 定义

CLIP 用双塔架构（图像编码器+文本编码器）在大规模图文对上通过 InfoNCE 对比损失训练，使匹配的图文对嵌入接近、不匹配的远离。推理时通过文本提示完成零样本分类，避免了固定类别头的限制。

## 关键特性

- **零样本泛化**：无需训练即可泛化到新类别，是 VL-TTA 的基础
- **提示词可调**：文本提示是可优化的连续向量，催生 TPT 范式
- **多模态对齐**：图文嵌入空间对齐使 TTA 可同时操作视觉和文本模态
- **点积推理偏差**：CLIP 点积推理存在信息损失，测试时分布归一化可缓解
- **温度参数关键**：温度缩放对校准至关重要，零温度边缘化（ZERO）简单有效

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Test-Time Prompt Tuning for Zero-Shot Generalization in Vision-Language Models]] | 2022 | 开创 TPT 范式，熵最小化在线优化提示词 |

## 相关概念

- [[Test-time adaptation]]
- [[Test-Time Prompt Tuning]]
- [[Entropy Minimization]]
- [[Zero-Shot Learning]]
- [[Wiki 目录]]
