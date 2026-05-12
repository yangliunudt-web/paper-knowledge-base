---
title: Low-Rank Adaptation
type: concept
tags: [概念, 进阶]
aliases: [LoRA, Low-Rank Adaptation, 低秩适配, low rank adaptation, lora, 低秩适应]
created: 2026-05-10
updated: 2026-05-10
sources: []
confidence: high
---

> LoRA（Low-Rank Adaptation）是一种参数高效的大模型微调方法，通过冻结预训练权重并注入可训练的低秩分解矩阵（A·B），将可训练参数量减少数千倍而保持与全微调相当的性能，是实现 LLM 边缘适配的关键技术。

## 定义

LoRA 基于一个关键假设：模型适应过程中的权重更新具有低"本征秩"。对于预训练的权重矩阵 W₀ ∈ R^{d×k}，LoRA 将其更新限制为低秩分解 ΔW = BA，其中 B ∈ R^{d×r}，A ∈ R^{r×k}，秩 r ≪ min(d,k)。推理时 W = W₀ + BA，无额外延迟。

## 关键特性

- **参数量**：r=1~16 时比全微调减少 100-10,000 倍
- **无推理延迟**：BA 可与 W₀ 合并，推理时零开销
- **多任务切换**：不同任务只需切换不同的 LoRA 权重（插件式）
- **隐私保护**：LoRA 权重可在本地训练，无需上传数据
- **适用范围**：不仅限于 LLM，已扩展至 ViT、扩散模型等
- **变体**：QLoRA（量化+LoRA）、DoRA（权重分解 LoRA）、LoRA+（优化学习率）

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[A Survey on LoRA of Large Language Models\|A Survey on LoRA of Large Language Models]] | 2024 | LoRA 综述：下游适配改进（打破低秩瓶颈、动态秩分配）、跨任务泛化（混合 LoRA 模块）、计算效率提升（减少单模块成本、加速多模块服务）、联邦学习隐私保护、应用场景梳理。 |
| [[LORA LOW-RANK ADAPTATION OF LARGE LANGUAGE MODELS\|LORA LOW-RANK ADAPTATION OF LARGE LANGUA...]] | 2021 | LoRA低秩适应：冻结预训练权重，注入可训练低秩矩阵，大幅减少可训练参数（GPT‑3 175B减少10,000倍），GPU内存需求降3倍，训练吞吐量高，无推理延迟，性能相当或优于全微调。 |
## 相关概念

- [[Large language model]]
- [[Transfer learning]]
- [[Continual learning]]
- [[Wiki 目录]]
