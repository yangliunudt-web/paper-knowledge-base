---
title: Zero-Shot Learning
type: concept
tags: [概念, 进阶]
aliases: [zero-shot learning, ZSL, 零样本学习, zero-shot generalization, 零样本泛化, zero-shot]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: high
---

> 零样本学习（ZSL）使模型能识别训练中未见过的类别。在 VLM 时代，CLIP 通过图文对比学习实现了强大的零样本泛化能力，成为 VL-TTA（如 TPT）的基础能力。

## 定义

ZSL 目标：训练时见过类别集合 S，测试时识别未见类别集合 U。CLIP 通过大规模图文对比预训练使文本描述可替代视觉样本，实现开放词汇的零样本分类。

## 关键特性

- **CLIP 零样本**：通过文本提示实现任意类别分类，无需微调
- **与 TTA 的关系**：零样本能力是 VL-TTA 的基础，TPT 在零样本基础上进一步用测试样本优化提示
- **泛化评估**：ImageNet-V2, ImageNet-R, ImageNet-Sketch 等 OOD 基准
- **边缘化**：ZERO 零温度边缘化在零样本 CLIP 上超越复杂提示方法

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Test-Time Prompt Tuning for Zero-Shot Generalization in Vision-Language Models\|Test-Time Prompt Tuning for Zero-Shot Ge...]] | 2022 | 开创TPT(测试时提示微调)研究方向：单样本+熵最小化+置信度选择在线学习提示。TPT是VLM TTA领域的奠基之作，启发后续PromptAlign/C-TPT/HisTPT/SwapPrompt等大 |
| [[Sketch3T Test-Time Training for Zero-Shot SBIR\|Sketch3T Test-Time Training for Zero-Sho...]] | 2022 | 将TTT拓展到草图检索：单张草图自适应的测试时训练+元学习分离主/辅任务更新。核心贡献是发现草图的测试时分布偏移问题并提出首个TTT解决方案。来自Surrey SketchX。 |
| [[Align Your Prompts Test-Time Prompting with Distribution Alignment for Zero-Shot Generalization\|Align Your Prompts Test-Time Prompting w...]] | 2023 | 提出PromptAlign：首次在测试时提示微调中显式对齐OOD样本与源数据的分布统计量（均值+方差），扩展TPT从单模态文本提示到多模态提示(MaPLe)，同时优化分布对齐损失和熵最小化。核心洞察： |
| [[Test-Time Adaptation with CLIP Reward for Zero-Shot Generalization in Vision-Language Models\|Test-Time Adaptation with CLIP Reward fo...]] | 2024 | 将RL引入VLM的TTA：用CLIP作为奖励模型替代熵最小化，防止模型盲目自信。核心创新是用CLIP reward替代entropy作为TTA优化目标，框架灵活可扩展至多任务。在TPT和SwapPro |
| [[Diverse Data Augmentation with Diffusions for Effective Test-time Prompt Tuning\|Diverse Data Augmentation with Diffusion...]] | 2024 | 提出DiffTPT：用扩散模型替代传统数据增强为TPT生成多样化增强视图，解决增强多样性不足问题；余弦相似度过滤保证生成数据的预测保真度。5.13%的平均提升显著。核心洞察：扩散模型的生成能力可弥补传 |
| [[Robust Test-Time Adaptation for Zero-Shot Prompt Tuning\|Robust Test-Time Adaptation for Zero-Sho...]] | 2024 | 系统分析CLIP TPT中的双偏差(Data Bias + Model Bias)问题，提出ADAPROMPT集成+动态微调+置信缓冲三组件。核心贡献是首次将偏差分析框架引入TPT，方法鲁棒性显著(几 |
## 相关概念

- [[CLIP]]
- [[Test-Time Prompt Tuning]]
- [[Test-time adaptation]]
- [[Domain Generalization]]
- [[Wiki 目录]]
