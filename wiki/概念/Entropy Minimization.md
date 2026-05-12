---
title: Entropy Minimization
type: concept
tags: [概念, 基础]
aliases: [entropy minimization, Shannon entropy, 熵最小化, prediction entropy, marginal entropy, entropy optimization]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: high
---

> 熵最小化是 TTA 的核心优化目标：通过最小化模型预测输出的 Shannon 熵，迫使模型对测试样本产生更自信的预测，隐式地适应目标域分布。TENT（ICLR 2021）首次将其确立为 Fully TTA 的标准范式。

## 定义

对于测试样本 x，模型输出 p(y|x)，Shannon 熵 H(p) = -Σ p(y|x) log p(y|x)。熵最小化通过梯度下降优化 H(p)，使预测更确定，间接对齐目标域数据分布。

## 关键特性

- **TTA 开山范式**：TENT 仅优化 BN 仿射参数（<1% 参数），一轮测试时优化
- **局限性**：无法解耦内容/风格因子偏移；可能盲目自信
- **替代方案**：熵匹配（无偏移不退化）、CLIP reward、交换预测、对比学习
- **开放集**：统一熵优化（熵最小化 ID + 熵最大化 OOD）
- **单样本**：MEMO 增广视图边际熵最小化

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Tent Fully Test-Time Adaptation by Entropy Minimization\|Tent Fully Test-Time Adaptation by Entro...]] | 2021 | TTA领域开山之作：提出测试时熵最小化(TENT)仅优化BN层的仿射参数，仅需一轮测试时优化。核心贡献是定义了Fully Test-Time Adaptation范式并证明其简单有效。奠定了后续所有T |
| [[Test-time Batch Normalization\|Test-time Batch Normalization]] | 2022 | 分析BN训练与测试的不一致性，提出GpreBN保持训练时梯度形式+数据集级统计量。核心贡献是揭示了BN在TTA中的深层机制并提供了统一优化框架。来自MSRA。 |
| [[MEMO Test Time Robustness via Adaptation and Augmentation\|MEMO Test Time Robustness via Adaptation...]] | 2022 | 提出MEMO：仅用单测试点原始+增广视图的边际熵最小化适配全模型参数。无需假设训练过程，即插即用。单点TTA范式奠基性工作，ImageNet-C/R/A达SOTA。 |
| [[Test-Time Prompt Tuning for Zero-Shot Generalization in Vision-Language Models\|Test-Time Prompt Tuning for Zero-Shot Ge...]] | 2022 | 开创TPT(测试时提示微调)研究方向：单样本+熵最小化+置信度选择在线学习提示。TPT是VLM TTA领域的奠基之作，启发后续PromptAlign/C-TPT/HisTPT/SwapPrompt等大 |
| [[If your data distribution shifts, use self-learning\|If your data distribution shifts, use se...]] | 2022 | 系统验证自学习(熵最小化+伪标签)在域偏移下的有效性：跨架构、预训练方式、偏移类型一致改善。实践价值高：无需源数据、超参数鲁棒、仅需少量epoch。提出ImageNet-D新基准，多个基准上达SOTA |
| [[DomainAdaptor A Novel Approach to Test-time Adaptation\|DomainAdaptor A Novel Approach to Test-t...]] | 2023 | 提出DomainAdaptor：AdaMixBN动态融合训练/测试BN统计量+GEM广义熵最小化损失。统一框架在少数据未见域场景下表现突出，4个基准上一致超越Tent/T3A等SOTA方法。 |
| [[STAMP Outlier-Aware Test-Time Adaptation with Stable Memory Replay\|STAMP Outlier-Aware Test-Time Adaptation...]] | 2024 | 将TTA从封闭世界推向开放世界：首次关注outlier(未知类别)存在下的TTA。稳定记忆库替代风险小批次 + 自加权熵最小化。核心贡献是定义了outlier-aware\ |
| [[Unified Entropy Optimization for Open-Set Test-Time Adaptation\|Unified Entropy Optimization for Open-Se...]] | 2024 | 开放集TTA：用熵最小化(ID)+熵最大化(OOD)统一处理协变量和语义偏移。核心贡献是将OOD检测集成到TTA优化框架中统一优化。来自中科院自动化所。 |
| [[Entropy is not Enough for Test-Time Adaptation From the Perspective of Disentangled Factors\|Entropy is not Enough for Test-Time Adap...]] | 2024 | 指出熵最小化TTA的局限性：无法解耦域偏移中的内容/风格因子。提出因子解耦TTA方法，分离处理内容和风格偏移，在多种分布偏移下实现更鲁棒的自适应，在DomainNet/ImageNet-C上验证。 |
| [[Domain-Specific Block Selection and Paired-View Pseudo-Labeling for Online Test-Time Adaptation\|Domain-Specific Block Selection and Pair...]] | 2024 | 提出DPLOT：域特定模块选择+翻转成对视图伪标签生成，解决TTA中伪标签质量退化问题。仅用翻转增广避免强增广的域偏移，在CIFAR-C和ImageNet-C上以简单设计超越复杂TTA方法。 |
| [[Towards Open-Set Test-Time Adaptation Utilizing the Wisdom of Crowds in Entropy Minimization\|Towards Open-Set Test-Time Adaptation Ut...]] | 2023 | 提出群体智慧样本选择方法解决开放集TTA：关键发现——噪声样本在熵最小化下置信度反而下降，基于此设计样本选择机制过滤错误和开集预测。简单有效，解决TTA中错误累积问题。 |
## 相关概念

- [[Test-time adaptation]]
- [[Batch Normalization]]
- [[Test-Time Prompt Tuning]]
- [[Self-Training]]
- [[Wiki 目录]]
