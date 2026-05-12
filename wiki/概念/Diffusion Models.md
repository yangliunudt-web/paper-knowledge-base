---
title: Diffusion Models
type: concept
tags: [概念, 进阶]
aliases: [diffusion models, DDPM, diffusion-based, 扩散模型, LDM, stable diffusion]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: high
---

> 扩散模型通过逐步加噪/去噪过程学习数据分布，在图像生成领域达到 SOTA。在测试时自适应中，扩散模型被用于样本级修复（将损坏图像投影回源域）和生成多样化增强视图。

## 定义

扩散模型包含前向扩散过程（逐步加噪）和逆向去噪过程（学习恢复）。在 TTA 中，利用预训练扩散模型在测试时不修改分类器参数，而是通过扩散过程修复输入样本或生成增强数据。

## 关键特性

- **输入自适应**：DDA 用扩散将损坏图像投影回源域，避免模型参数更新
- **效率优化**：Efficient Diffusion Editor 用 LDM + 蒸馏加速 100 倍
- **风格泛化**：GDA 引入风格/内容保持损失，突破像素损坏局限
- **多样性增强**：DiffTPT 用扩散生成多样化增强视图提升提示微调
- **医学应用**：染色自适应，填补扩散 TTA 在医学领域的空白

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[A-STAR Test-time Attention Segregation and Retention for Text-to-image Synthesis\|A-STAR Test-time Attention Segregation a...]] | 2023 | 提出A-STAR：两个测试时注意力损失函数（分离损失+保持损失），分析交叉注意力图发现概念重叠和信息丢失是扩散模型多概念生成失败的根本原因，无需重新训练即可在测试时优化并大幅提升语义准确性。方法简洁有 |
| [[Back to the Source Diffusion-Driven Test-Time Adaptation\|Back to the Source Diffusion-Driven Test...]] | 2023 | 提出DDA：将TTA从模型参数更新范式转变为输入数据更新范式。用扩散模型在测试时将损坏图像投影回源域，避免逐域重训练。核心发现：在数据受限场景（小批量/顺序相关/混合损坏）下输入自适应比模型自适应更鲁 |
| [[Diverse Data Augmentation with Diffusions for Effective Test-time Prompt Tuning\|Diverse Data Augmentation with Diffusion...]] | 2024 | 提出DiffTPT：用扩散模型替代传统数据增强为TPT生成多样化增强视图，解决增强多样性不足问题；余弦相似度过滤保证生成数据的预测保真度。5.13%的平均提升显著。核心洞察：扩散模型的生成能力可弥补传 |
| [[Diffusion-TTA Test-time Adaptation of Discriminative Models via Generative Feedback\|Diffusion-TTA Test-time Adaptation of Di...]] | 2024 | 提出Diffusion-TTA：用扩散模型的生成反馈(而非传统熵最小化)来引导判别模型进行TTA。核心创新是将生成模型作为测试时适配器，通过最大化图像似然来适应分布偏移。在分类、分割、深度预测等多任务 |
| [[GDA Generalized Diffusion for Robust Test-time Adaptation\|GDA Generalized Diffusion for Robust Tes...]] | 2024 | 将扩散TTA从像素损坏扩展到多样化OOD类型：引入风格+内容保持损失与熵最小化联合引导扩散过程。核心贡献是突破了DDA仅限于像素损坏的局限，使扩散TTA能应对风格化、素描等更广泛分布偏移。方法在损失设 |
| [[Test-Time Stain Adaptation with Diffusion Models for Histopathology Image Classification\|Test-Time Stain Adaptation with Diffusio...]] | 2024 | 将扩散TTA应用于医学图像染色自适应：首次探索测试时扩散模型解决染色偏移这一病理学核心问题。将TTA拓展到医学图像域，填补了扩散TTA在医学应用中的空白。来自台湾中研院。 |
| [[Efficient Diffusion-Driven Corruption Editor for Test-Time Adaptation\|Efficient Diffusion-Driven Corruption Ed...]] | 2024 | 解决DDA扩散TTA方法的效率瓶颈：用LDM替代像素空间DDPM + 损坏建模 + 蒸馏加速(4 NFE)。使图像级TTA从不可用变为可用(快100倍)。核心贡献是工程优化使扩散TTA实用化，但方法本 |
| [[Improved Test-Time Adaptation for Domain Generalization\|Improved Test-Time Adaptation for Domain...]] | 2023 | - |
## 相关概念

- [[Test-time adaptation]]
- [[Test-Time Prompt Tuning]]
- [[Distribution Shift]]
- [[Wiki 目录]]
