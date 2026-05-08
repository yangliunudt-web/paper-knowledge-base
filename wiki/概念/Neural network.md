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
| [[Ferroelectric FET Analog Synapse for Acceleration of Deep Neural Network Training\|Ferroelectric FET Analog Synapse for Acc...]] | 2018 | FeFET模拟突触：基于部分极化切换，实现5位对称增强/抑制特性，75ns更新脉冲，45倍电导可调范围，相比多态RRAM突触在线学习延迟加速10^3‑10^6倍。 |
| [[Accurate deep neural network inference using computational phase-change memory\|Accurate deep neural network inference u...]] | 2020 | 将ResNet CNN映射到PCM器件进行存内推理：批归一化补偿保持精度，CIFAR-10达到93.5%硬件准确率。 |
| [[Neuromorphic computing hardware and neural architectures for robotics\|Neuromorphic computing hardware and neur...]] | 2022 | 综述神经形态计算硬件与神经架构在机器人中的应用：快速低功耗神经网络推理、受生物启发的算法设计、自主智能系统创新应用。 |
| [[Incorporating neuro-inspired adaptability for continual learning in artificial intelligence\|Incorporating neuro-inspired adaptabilit...]] | 2022 | 元可塑性+参数隔离方法，解决持续学习灾难性遗忘，多场景SOTA整体性能。 |
| [[Delocalized photonic deep learning on the internet's edge\|Delocalized photonic deep learning on th...]] | 2023 | 提出 Netcast 光子深度学习：云端智能收发器流式传输权重到边缘设备，实现 40 aJ/MAC 超低能耗推理，86 km 光纤现场试验验证。 |
| [[An index-free sparse neural network using two-dimensional semiconductor ferroelectric field-effect transistors\|An index-free sparse neural network usin...]] | 2024 | 二维FeFET实现无索引稀疏神经网络，高能效边缘AI处理。 |
| [[A Comprehensive Survey of Continual Learning Theory, Method and Application\|A Comprehensive Survey of Continual Lear...]] | 2024 | 持续学习综述：五类方法（正则化/回放/优化/表示/架构），系统性分析稳定性-可塑性权衡。 |
| [[Hybrid neural networks for continual learning inspired by corticohippocampal circuits\|Hybrid neural networks for continual lea...]] | 2025 | CH-HNN混合神经网络模型，模拟皮质-海马回路的双重记忆表征。ANN+SNN混合架构，结合元可塑性机制动态调节学习率。在任务增量和类别增量学习场景中表现优异，SNN组件支持低功耗神经形态硬件部署。 |
| [[Neuromorphic computing at scale\|Neuromorphic computing at scale]] | 2025 | 神经形态计算规模化：综述大脑启发硬件/算法设计、可扩展架构关键特征、潜在应用与挑战、生态系统需求，为大规模神经形态系统发展提供路线图。 |
| [[Unsupervised Domain Adaptation by Backpropagation\|Unsupervised Domain Adaptation by Backpr...]] | 2015 | 提出 DANN 域对抗神经网络，通过梯度反转层实现域不变特征学习，在 MNIST→SVHN 等域适应任务上取得优异性能，开创深度域适应领域。 |
| [[Domain-Adversarial Training of Neural Networks\|Domain-Adversarial Training of Neural Ne...]] | 2016 | 领域对抗神经网络训练（DANN）：通过梯度反转层实现领域不变特征学习，处理同质/异质领域自适应，在标准基准上优于SOTA方法。 |
| [[2022 roadmap on neuromorphic computing and engineering\|2022 roadmap on neuromorphic computing a...]] | 2022 | 神经形态计算路线图综述：涵盖神经形态器件、电路架构、算法应用现状与挑战，展望类脑计算未来发展方向。 |
## 相关概念

- [[Neuromorphic computing]]
- [[In-memory computing]]
- [[Reservoir computing]]
- [[crossbar]]
- [[Wiki 目录]]
