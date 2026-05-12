---
title: Test-Time Prompt Tuning
type: concept
tags: [概念, 进阶]
aliases: [TPT, test-time prompt tuning, 测试时提示微调, prompt tuning, prompt adaptation]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: high
---

> 测试时提示微调（TPT）是 VLM 时代的 TTA 新范式：不修改模型参数，而是在线优化文本/视觉提示（prompt），通过熵最小化或分布对齐引导提示学习。TPT（NeurIPS 2022）开创了这一范式。

## 定义

VLM（如 CLIP）用文本提示实现零样本分类。TPT 在测试时不调模型权重，而是将提示参数化为可微向量，用测试样本的熵最小化在线优化提示。后续工作扩展到双模态提示、持续提示、扩散增强提示等。

## 关键特性

- **零温度边缘化**：ZERO（NeurIPS 2024）超越所有复杂提示微调方法，10x 加速
- **双模态扩展**：DART 同时优化文本+视觉提示，知识保留机制利用历史
- **校准**：C-TPT 发现文本特征分散度与校准误差负相关
- **分布对齐**：PromptAlign 显式对齐 OOD 样本与源分布统计量
- **持续在线**：HisTPT 三类知识库记忆历史防止性能退化

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Test-Time Prompt Tuning for Zero-Shot Generalization in Vision-Language Models\|Test-Time Prompt Tuning for Zero-Shot Ge...]] | 2022 | 开创TPT(测试时提示微调)研究方向：单样本+熵最小化+置信度选择在线学习提示。TPT是VLM TTA领域的奠基之作，启发后续PromptAlign/C-TPT/HisTPT/SwapPrompt等大 |
| [[Align Your Prompts Test-Time Prompting with Distribution Alignment for Zero-Shot Generalization\|Align Your Prompts Test-Time Prompting w...]] | 2023 | 提出PromptAlign：首次在测试时提示微调中显式对齐OOD样本与源数据的分布统计量（均值+方差），扩展TPT从单模态文本提示到多模态提示(MaPLe)，同时优化分布对齐损失和熵最小化。核心洞察： |
| [[Historical Test-time Prompt Tuning for Vision Foundation Models\|Historical Test-time Prompt Tuning for V...]] | 2024 | 解决TPT在持续数据流中性能退化问题：通过三类知识库(局部/困难样本/全局)记忆历史测试样本知识，自适应检索机制正则化当前预测。核心贡献是将持续学习中的记忆回放思想引入TPT，在连续域变化场景下保持稳 |
| [[Diverse Data Augmentation with Diffusions for Effective Test-time Prompt Tuning\|Diverse Data Augmentation with Diffusion...]] | 2024 | 提出DiffTPT：用扩散模型替代传统数据增强为TPT生成多样化增强视图，解决增强多样性不足问题；余弦相似度过滤保证生成数据的预测保真度。5.13%的平均提升显著。核心洞察：扩散模型的生成能力可弥补传 |
| [[C-TPT Calibrated Test-Time Prompt Tuning for Vision-Language Models via Text Feature Dispersion\|C-TPT Calibrated Test-Time Prompt Tuning...]] | 2024 | 首次将校准(calibration)引入测试时提示微调：发现文本特征分散度与校准误差强负相关，提出ATFD度量和C-TPT方法在TPT中联合优化准确率+校准。核心贡献是揭示CLIP内部属性与校准的关系 |
| [[Robust Test-Time Adaptation for Zero-Shot Prompt Tuning\|Robust Test-Time Adaptation for Zero-Sho...]] | 2024 | 系统分析CLIP TPT中的双偏差(Data Bias + Model Bias)问题，提出ADAPROMPT集成+动态微调+置信缓冲三组件。核心贡献是首次将偏差分析框架引入TPT，方法鲁棒性显著(几 |
## 相关概念

- [[Test-time adaptation]]
- [[CLIP]]
- [[Entropy Minimization]]
- [[Diffusion Models]]
- [[Wiki 目录]]
