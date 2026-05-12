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
| [[Test-Time Prompt Tuning for Zero-Shot Generalization in Vision-Language Models\|Test-Time Prompt Tuning for Zero-Shot Ge...]] | 2022 | 开创TPT(测试时提示微调)研究方向：单样本+熵最小化+置信度选择在线学习提示。TPT是VLM TTA领域的奠基之作，启发后续PromptAlign/C-TPT/HisTPT/SwapPrompt等大 |
| [[PODA Prompt-driven Zero-shot Domain Adaptation\|PODA Prompt-driven Zero-shot Domain Adap...]] | 2023 | 开创零样本域自适应新范式：仅需一段prompt文本描述目标域即可适配。PIN模块用CLIP引导源特征仿射变换，无需任何目标域图像。核心贡献是将域自适应从视觉范式转变为语言引导范式，极其实用且创新性高。 |
| [[Align Your Prompts Test-Time Prompting with Distribution Alignment for Zero-Shot Generalization\|Align Your Prompts Test-Time Prompting w...]] | 2023 | 提出PromptAlign：首次在测试时提示微调中显式对齐OOD样本与源数据的分布统计量（均值+方差），扩展TPT从单模态文本提示到多模态提示(MaPLe)，同时优化分布对齐损失和熵最小化。核心洞察： |
| [[SwapPrompt Test-Time Prompt Adaptation for Vision-Language Models\|SwapPrompt Test-Time Prompt Adaptation f...]] | 2024 | 将自监督对比学习引入TPT：交换预测机制(Swap Prediction)利用双提示+双增强视图的对比学习增强在线提示。核心贡献是用对比学习替代熵最小化作为TPT优化目标，性能大幅提升逼近有监督CoO |
| [[Frustratingly Easy Test-Time Adaptation of Vision-Language Models\|Frustratingly Easy Test-Time Adaptation ...]] | 2024 | 理论分析MEM-TPT发现零温度边缘化(ZERO)超越了所有复杂提示微调方法。核心贡献是从MEM方法中发掘被忽视的简单基线，10x加速13x省内存。创新在于揭示MEM中的温度参数是关键。局限：仅适用于 |
| [[Test-Time Distribution Normalization for Contrastively Learned Vision-language Models\|Test-Time Distribution Normalization for...]] | 2024 | 揭示CLIP点积推理的信息损失问题：DN用批次均值近似负样本使测试时操作与InfoNCE训练目标对齐。核心洞察深刻——测试过程应与训练目标一致，简单高效的即插即用方法。 |
| [[Test-Time Adaptation with CLIP Reward for Zero-Shot Generalization in Vision-Language Models\|Test-Time Adaptation with CLIP Reward fo...]] | 2024 | 将RL引入VLM的TTA：用CLIP作为奖励模型替代熵最小化，防止模型盲目自信。核心创新是用CLIP reward替代entropy作为TTA优化目标，框架灵活可扩展至多任务。在TPT和SwapPro |
| [[Diverse Data Augmentation with Diffusions for Effective Test-time Prompt Tuning\|Diverse Data Augmentation with Diffusion...]] | 2024 | 提出DiffTPT：用扩散模型替代传统数据增强为TPT生成多样化增强视图，解决增强多样性不足问题；余弦相似度过滤保证生成数据的预测保真度。5.13%的平均提升显著。核心洞察：扩散模型的生成能力可弥补传 |
| [[C-TPT Calibrated Test-Time Prompt Tuning for Vision-Language Models via Text Feature Dispersion\|C-TPT Calibrated Test-Time Prompt Tuning...]] | 2024 | 首次将校准(calibration)引入测试时提示微调：发现文本特征分散度与校准误差强负相关，提出ATFD度量和C-TPT方法在TPT中联合优化准确率+校准。核心贡献是揭示CLIP内部属性与校准的关系 |
| [[Contrastive Test-Time Adaptation\|Contrastive Test-Time Adaptation]] | 2024 | 提出PTA：用知识原型替代缓存实现高效TTA，根据零样本置信度自适应加权更新原型，消除缓存检索开销。在保持CLIP 92%推理速度的同时，跨域基准准确率从65.64%提升至69.38%，显著优于TDA |
| [[Efficient Test-Time Adaptation of Vision-Language Models\|Efficient Test-Time Adaptation of Vision...]] | 2024 | 提出TDA：免训练动态适配器，用轻量键值缓存+渐进伪标签精炼实现高效TTA，无需反向传播。创新负伪标签机制缓解伪标签噪声。在OOD和跨域基准上性能优于TPT等需训练方法，速度提升5-10倍。 |
| [[Robust Test-Time Adaptation for Zero-Shot Prompt Tuning\|Robust Test-Time Adaptation for Zero-Sho...]] | 2024 | 系统分析CLIP TPT中的双偏差(Data Bias + Model Bias)问题，提出ADAPROMPT集成+动态微调+置信缓冲三组件。核心贡献是首次将偏差分析框架引入TPT，方法鲁棒性显著(几 |
## 相关概念

- [[Test-time adaptation]]
- [[Test-Time Prompt Tuning]]
- [[Entropy Minimization]]
- [[Zero-Shot Learning]]
- [[Wiki 目录]]
