---
title: Neural network
type: concept
tags: [概念, 基础]
aliases: [神经网络, neural networks, Neural networks, Neural Networks, NN, ANN, DNN, deep neural network, SNN, spiking neural network, deep learning, Deep learning]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> 神经网络是受生物神经系统启发的计算模型，由多层相互连接的人工神经元组成，通过调节连接权重（突触）学习和执行模式识别、分类、预测等任务。在硬件实现中，神经元和突触分别由模拟电路和新兴存储器件实现。

## 定义

神经网络的基本计算单元是人工神经元：y = f(Σ w_i x_i + b)，其中权重 w_i 代表突触连接强度，x_i 是输入，f 是非线性激活函数。深度学习（DNN）通过多层堆叠实现层次化特征提取。

硬件实现的关键是将 MVM（矩阵向量乘法 Σ w_i x_i）映射到物理阵列（如 crossbar）上。

## 关键特性

- **DNN（深度神经网络）**：多层前馈网络，通过反向传播训练
- **CNN（卷积神经网络）**：权重共享的卷积核，适合视觉任务
- **SNN（脉冲神经网络）**：事件驱动的时序编码，更适合神经形态硬件
- **GNN（图神经网络）**：处理图结构数据，适合分子/社交/引用网络
- **训练 vs 推理**：训练需要高精度（FP16/32）和权重更新，推理可容忍低精度（INT4/8）
- **硬件适配**：器件非理想性（variation, stuck-at faults）对推理精度影响小于训练

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[In-memory ferroelectric differentiator\|In-memory ferroelectric differentiator]] | 2024 | Nature Communications |
| [[Electrochemical ohmic memristors\|Electrochemical ohmic memristors]] | 2024 | Nature Communications |
| [[Hybrid neural networks for continual learning inspired by corticohippocampal circuits\|Hybrid neural networks for continual lea...]] | 2025 | Nature Communications |
| [[Photonic edge intelligence chip for multimodal sensing, inference and learning\|Photonic edge intelligence chip for mult...]] | 2025 | Nature Communications |
| [[Accurate deep neural network inference using computational phase-change memory\|Accurate deep neural network inference u...]] | Unknown Year | Nature Communications |
| [[Accurate deep neural network inference using computational phase-change memory\|Accurate deep neural network inference u...]] | Unknown Year | Nature Communications |
| [[Unsupervised local learning based on voltagedependent synaptic plasticity for resistive and ferroelectric synapses\|Unsupervised local learning based on vol...]] | 2024 | Communications Materials |
| [[Ferroelectric Optoelectronic Sensor for Intelligent Flame Detection and In‑Sensor Motion Perception\|Ferroelectric Optoelectronic Sensor for ...]] | 2026 | Nano-Micro Letters |
| [[Combinatorial optimization by weight annealing in memristive hopfeld networks\|Combinatorial optimization by weight ann...]] | Unknown Year | Scientific Reports |
## 相关概念

- [[Neuromorphic computing]]
- [[In-memory computing]]
- [[Reservoir computing]]
- [[crossbar]]
- [[Wiki 目录]]
