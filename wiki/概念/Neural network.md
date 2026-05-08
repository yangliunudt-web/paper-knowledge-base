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
| [[Accurate deep neural network inference using computational phase-change memory\|Accurate deep neural network inference u...]] | 2020 | 本文提出训练ResNet型CNN映射到PCM器件的方法，利用批归一化补偿技术保持精度。在CIFAR-10上实现93.7%（软件）/93.5%（硬件）准确率，ImageNet\ |
| [[Electrochemical ohmic memristors\|Electrochemical ohmic memristors]] | 2024 | 本文提出电化学欧姆忆阻器，利用电化学机制实现可靠阻变切换和欧姆行为，面向神经形态计算应用。 |
| [[In-memory ferroelectric differentiator\|In-memory ferroelectric differentiator]] | 2025 | 开发40x40 P(VDF-TrFE)铁电电容crossbar存内差分器。0.24 fJ/次、1 MHz、98.9%准确率、4.17 POPS/W（比V100高10000倍）。演示一阶/二阶导数、运动 |
| [[Zn2+ Engineered Low-Barrier LiNbO3 Enables Visible-Light Programmable Ferroelectric Memristors for Noise-Immune Neuromorphic Vision\|Zn2+ Engineered Low-Barrier LiNbO3 Enabl...]] | 2025 | Lithium niobate (LiNbO ), owing to its unique [[ferroelectric polarization]] and\ |
## 相关概念

- [[Neuromorphic computing]]
- [[In-memory computing]]
- [[Reservoir computing]]
- [[crossbar]]
- [[Wiki 目录]]
