---
title: Test-Time Training
type: concept
tags: [概念, 进阶]
aliases: [TTT, test-time training, TTT-MIM, 测试时训练]
created: 2026-05-12
updated: 2026-05-12
sources: []
confidence: high
---

> 测试时训练（TTT）在推理阶段将测试样本转化为自监督学习任务，通过辅助任务在线更新模型参数。与 TTA 的熵最小化不同，TTT 依赖训练时预定义的辅助任务（旋转预测、掩码重建等），在测试时复用。

## 定义

TTT 训练时同时学习主任务和自监督辅助任务；测试时对每个样本先做一步自监督更新再进行主任务预测。代表性辅助任务：旋转预测、掩码图像建模（MIM）、对比学习。

## 关键特性

- **辅助任务设计**：MIM（TTT-MIM）优于旋转预测（原始 TTT）
- **评估协议**：需统一协议避免不公平比较（sTTT 规范）
- **3D 扩展**：MATE 将 TTT 引入 3D 点云，掩码自编码器测试时重建
- **低层视觉**：TTT-MIM 验证去噪等低层任务有效性

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Test-Time Training with Self-Supervision for Generalization under Distribution Shifts\|Test-Time Training with Self-Supervision...]] | 2020 | TTT开山之作：首次将自监督学习引入测试时自适应，将单样本转化为自监督任务在线更新模型。核心贡献是定义了Test-Time Training范式。来自UC Berkeley。 |
| [[Sketch3T Test-Time Training for Zero-Shot SBIR\|Sketch3T Test-Time Training for Zero-Sho...]] | 2022 | 将TTT拓展到草图检索：单张草图自适应的测试时训练+元学习分离主/辅任务更新。核心贡献是发现草图的测试时分布偏移问题并提出首个TTT解决方案。来自Surrey SketchX。 |
| [[Revisiting Realistic Test-Time Training Sequential Inference and Adaptation by Anchored Clustering\|Revisiting Realistic Test-Time Training ...]] | 2022 | TTT领域规范化工作：系统梳理TTT协议并提出sTTT+TTAC(锚定聚类匹配源-目标域聚类)。核心贡献是为TTT建立了清晰的评估协议，避免不公平比较。TTAC方法简单有效但主要价值在基准规范化。 |
| [[Test-Time Training with Masked Autoencoders\|Test-Time Training with Masked Autoencoders]] | 2022 | TTT+MAE：用掩码自编码器作为TTT的自监督任务，相比原始TTT(旋转预测)更有效。核心贡献是将MAE引入TTT框架并给出理论分析。来自UC Berkeley/Meta。 |
| [[NC-TTT A Noise Constrastive Approach for Test-Time Training\|NC-TTT A Noise Constrastive Approach for...]] | 2023 | 提出NC-TTT：将测试时训练重构为对比学习框架，用噪声对比估计区分原始/增广视图实现TTT。无需源数据或标签，在CIFAR-C和ImageNet-C上实现更稳定的自适应，性能优于熵最小化方法。 |
| [[ClusT3 Information Invariant Test-Time Training\|ClusT3 Information Invariant Test-Time T...]] | 2023 | 提出ClusT3：将聚类与信息不变性结合用于TTT，通过聚类伪标签实现自监督自适应，在保持信息论属性的同时防止灾难性遗忘。无需源数据访问，在多个域偏移基准上验证有效性。 |
| [[OST Improving Generalization of DeepFake Detection via One-Shot Test-Time Training\|OST Improving Generalization of DeepFake...]] | 2023 | 提出OST：首个将测试时训练引入深度伪造检测的工作。通过元学习实现单步梯度更新即可适应新伪造方法，解决跨生成方法泛化问题。在多个DeepFake基准上验证对未见伪造方法的泛化鲁棒性。 |
| [[MATE Masked Autoencoders are Online 3D Test-Time Learners\|MATE Masked Autoencoders are Online 3D T...]] | 2023 | 首个3D TTT方法：用掩码自编码器在测试时通过点云重建更新网络，仅需5% tokens即可自适应，极轻量。在ModelNet40-C/ShapeNet-C等多个3D基准上显著提升鲁棒性。 |
| [[ActMAD Activation Matching to Align Distributions for Test-Time-Training\|ActMAD Activation Matching to Align Dist...]] | 2023 | 提出ActMAD：通过多层激活统计对齐而非仅最终层实现TTT，建模网络中每层每个特征的分布。架构无关、任务无关，在分类(CIFAR-100C/ImageNet-C)和目标检测(KITTI-Fog)上均 |
| [[TTT-MIM Test-Time Training with Masked Image Modeling for Denoising Distribution Shifts\|TTT-MIM Test-Time Training with Masked I...]] | 2024 | 将TTT拓展到图像去噪：MIM作为自监督辅助任务+测试时微调适配单张图像。核心贡献是验证了TTT在低层视觉(去噪)任务上的有效性，突破了TTT主要应用于分类/分割的局限。 |
| [[On the Robustness of Open-World Test-Time Training Self-Training with Dynamic Prototype Expansion\|On the Robustness of Open-World Test-Tim...]] | 2024 | 开辟OWTTT(开放世界测试时训练)新方向：揭示现有TTT在强OOD污染下的脆弱性，提出自适应OOD剪枝+动态原型扩展+分布对齐三组件方案。核心贡献是将开放世界学习与TTA交叉，定义了新的评估场景和基 |
| [[MT3 Meta Test-Time Training for Self-Supervised Test-Time Adaption\|MT3 Meta Test-Time Training for Self-Sup...]] | 2020 | 早期TTA奠基工作：将元学习引入测试时训练，通过自监督损失使模型学会如何适应分布偏移。核心贡献是用元学习框架统一了自监督学习和测试时自适应，单样本即可适配。方法优雅但在更复杂基准上未经充分验证。 |
## 相关概念

- [[Test-time adaptation]]
- [[Self-Supervised Learning]]
- [[Entropy Minimization]]
- [[Distribution Shift]]
- [[Wiki 目录]]
