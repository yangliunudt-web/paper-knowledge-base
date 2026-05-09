---
title: Large language model
type: concept
tags: [概念, 进阶]
aliases: [LLM, large language model, 大语言模型, 大模型, LLMs, GPT, language model, foundation model]
created: 2026-05-10
updated: 2026-05-10
sources: []
confidence: medium
---

> 大语言模型（LLM）是参数规模达到数十亿到数千亿的自然语言处理模型，通过大规模预训练获取通用语言能力，再通过微调或提示适应下游任务。其训练和推理的巨大计算需求推动了高效微调（如 LoRA）和边缘推理优化技术的发展。

## 定义

LLM 基于 Transformer 架构，通过自监督预训练（如 GPT 系列的因果语言建模、BERT 系列的掩码语言建模）在海量文本数据上学习。主要研究方向包括参数高效微调（PEFT）、模型压缩（量化/剪枝）、推理加速（KV-cache 优化）、以及多模态扩展。

## 关键特性

- **参数高效微调（PEFT）**：LoRA（低秩适配）、适配器、前缀微调等方法仅训练少量参数
- **上下文学习（ICL）**：无需梯度更新，通过提示中的少量示例引导模型行为
- **持续学习挑战**：LLM 在持续获取新知识时面临灾难性遗忘
- **边缘部署**：量化（INT8/INT4）、蒸馏、投机解码等技术使 LLM 能在边缘设备运行
- **小模型协同**：SuperICL 等方法将本地微调的小模型作为 LLM 插件

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[A Survey on LoRA of Large Language Models\|A Survey on LoRA of Large Language Models]] | 2024 | LoRA 综述：下游适配改进（打破低秩瓶颈、动态秩分配）、跨任务泛化（混合 LoRA 模块）、计算效率提升（减少单模块成本、加速多模块服务）、联邦学习隐私保护、应用场景梳理。 |
| [[An Edge-Cloud Collaboration Framework for Generative AI Service Provision With Synergetic Big Cloud Model and Small Edge Models\|An Edge-Cloud Collaboration Framework fo...]] | 2024 | 边缘-云端协作生成式AI服务框架：自底向上BAIM架构、分布式训练、任务导向部署，通过图像生成用例验证，降低云端负担、提升边缘个性化服务能力。 |
| [[Enabling Energy-Efficient Deployment of Large Language Models on Memristor Crossbar A Synergy of Large and Small\|Enabling Energy-Efficient Deployment of ...]] | 2024 | 忆阻器交叉阵列大语言模型能效部署：提出新架构解决模型规模、非常权重稳态乘法、非线性操作三大挑战，BERT_Large测试精度损失可忽略，面积开销改善39倍，能耗改善18倍，面积-延迟积降低68倍。 |
| [[LORA LOW-RANK ADAPTATION OF LARGE LANGUAGE MODELS\|LORA LOW-RANK ADAPTATION OF LARGE LANGUA...]] | 2021 | LoRA低秩适应：冻结预训练权重，注入可训练低秩矩阵，大幅减少可训练参数（GPT‑3 175B减少10,000倍），GPU内存需求降3倍，训练吞吐量高，无推理延迟，性能相当或优于全微调。 |
| [[Small Models are Valuable Plug-ins for Large Language Models\|Small Models are Valuable Plug-ins for L...]] | 2023 | 超上下文学习：将本地微调的小模型作为插件与大语言模型协同，提升监督任务性能，解决上下文学习不稳定性，增强小模型多语言与可解释能力。 |
## 相关概念

- [[Continual learning]]
- [[Low-Rank Adaptation]]
- [[Wiki 目录]]
