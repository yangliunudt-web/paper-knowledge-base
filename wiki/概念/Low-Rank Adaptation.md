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
| [[LORA LOW-RANK ADAPTATION OF LARGE LANGUAGE MODELS]] | 2021 | 原始 LoRA, GPT-3 175B 参数减少 10,000× |
| [[A Survey on LoRA of Large Language Models]] | 2024 | LoRA 综述 |

## 相关概念

- [[Large language model]]
- [[Transfer learning]]
- [[Continual learning]]
- [[Wiki 目录]]
