---
title: Test-time adaptation
type: concept
tags: [概念, 进阶]
aliases: [TTA, test-time adaptation, 测试时适应, fully test-time adaptation, online adaptation, 测试时自适应]
created: 2026-05-10
updated: 2026-05-10
sources: []
confidence: medium
---

> 测试时适应（TTA）是机器学习中的一种适应范式，模型在推理阶段仅利用输入测试数据（无需源数据或标签）在线调整自身参数以应对数据分布偏移，是边缘设备持续鲁棒推理的关键使能技术。

## 定义

与域适应（DA）需要目标域（部分）标注数据不同，TTA 在完全无监督的测试阶段进行。主要方法包括：熵最小化（TENT）、批归一化统计量自适应（AdaBN）、伪标签自训练、以及基于记忆库的对比学习。TTA 允许边缘设备在部署后持续适应环境变化。

## 关键特性

- **熵最小化**：通过最小化模型输出熵来增强预测置信度
- **BN 自适应**：仅调整 BN 层统计量（均值/方差）而不改变权重，参数效率极高
- **内存效率**：TTA 通常仅需少量额外内存（存储 BN 统计量或轻量级优化器状态）
- **与 CIM 的关系**：存内计算硬件能效高但存在器件非理想性（噪声/漂移），TTA 可补偿这些非理想性
- **持续学习连接**：TTA 可被视为单任务持续学习的一种特殊形式

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[TENT Fully Test-Time Adaptation by Entropy Minimization\|TENT Fully Test-Time Adaptation by Entro...]] | 2021 | TENT 测试时适应：熵最小化、归一化统计+仿射变换、ImageNet-C SOTA、无需源数据/改变训练。 |
| [[Benchmarking Test-Time DNN Adaptation at Edge with Compute-In-Memory\|Benchmarking Test-Time DNN Adaptation at...]] | 2024 | 本研究提出了一个基准测试框架，用于评估在配备CIM硬件的受限边缘设备上测试时DNN适应技术。研究发现：（1）部分网络适应往往优于全网络适应；（2）CIM设备能效高但存在非理想性；（3）适应技术能有效处 |
| [[Beyond Model Adaptation at Test Time: A Survey\|Beyond Model Adaptation at Test Time: A ...]] | 2024 | 本文对测试时适应（Test-time Adaptation, TTA）进行了全面的综述，涵盖了400多篇近期论文。研究问题：机器学习模型在训练和测试数据分布不同时性能下降的问题。方法：将现有TTA方法 |
## 相关概念

- [[Edge computing]]
- [[In-memory computing]]
- [[Continual learning]]
- [[Transfer learning]]
- [[Wiki 目录]]
