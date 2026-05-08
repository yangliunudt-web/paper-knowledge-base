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
| [[Unsupervised Domain Adaptation by Backpropagation|Unsupervised Domain Adaptation by Backpropaga...]] | 2015 | 提出 DANN 域对抗神经网络，通过梯度反转层实现域不变特征学习，在 MNIST→SVHN 等域适应任务上取得优异性能，开创深度域适应领域。 |
| [[Domain-Adversarial Training of Neural Networks|Domain-Adversarial Training of Neural Networks]] | 2016 | 领域对抗神经网络训练（DANN）：通过梯度反转层实现领域不变特征学习，处理同质/异质领域自适应，在标准基准上优于SOTA方法。 |
| [[Nonvolatile Memory Design Based on Ferroelectric FETs|Nonvolatile Memory Design Based on Ferroelect...]] | 2016 | 2T FeFET非易失存储器：利用三端结构实现分离读/写路径，非破坏性读取，相比FeRAM写入电压降低58.5%、能量降低67.7%，区分度10^6倍，能... |
| [[Context-modulation of hippocampal dynamics and deep convolutional networks|Context-modulation of hippocampal dynamics an...]] | 2017 | 受海马体 CA3 双通路（EC 直接投射和 EC→DG→CA3 间接投射）启发，提出上下文调制深度神经网络，通过上下文敏感偏置在 CIFAR-100 和 ... |
| [[Adaptive Batch Normalization for Practical Domain Adaptation|Adaptive Batch Normalization for Practical Do...]] | 2018 | AdaBN 域适应：调整 BN 统计量实现深度适应、无参数、无额外组件、可与现有方法互补。 |
| [[Ferroelectric FET Analog Synapse for Acceleration of Deep Neural Network Training|Ferroelectric FET Analog Synapse for Accelera...]] | 2018 | FeFET模拟突触：基于部分极化切换，实现5位对称增强/抑制特性，75ns更新脉冲，45倍电导可调范围，相比多态RRAM突触在线学习延迟加速10^3‑10... |
| [[Overcoming Catastrophic Forgetting with Hard Attention to the Task|Overcoming Catastrophic Forgetting with Hard ...]] | 2018 | 硬注意力任务机制：通过任务特定掩码保留旧任务信息，将灾难性遗忘率降低45‑80%，具备超参数鲁棒性和监控能力。 |
| [[Once for All Train One Network and Specialize it for Efficient Deployment|Once for All Train One Network and Specialize...]] | 2019 | OFA 通用网络：渐进收缩算法、支持 10^19 子网络、训练成本从 O(N) 降至 O(1)、比 NAS 快 14-1142 倍、多硬件平台部署。 |
| [[Accurate deep neural network inference using computational phase-change memory|Accurate deep neural network inference using ...]] | 2020 | 本文提出训练ResNet型CNN映射到PCM器件的方法，利用批归一化补偿技术保持精度。在CIFAR-10上实现93.7%（软件）/93.5%（硬件）准确率... |
| [[In-Memory Learning With Analog Resistive Switching Memory A Review and Perspective|In-Memory Learning With Analog Resistive Swit...]] | 2021 | 模拟电阻开关存储器存内学习综述：定义两层性能指标，分析器件特性、硬件算法、阵列映射、架构电路设计，评估现有器件性能，讨论从器件到系统的挑战与前景。 |
| [[2022 roadmap on neuromorphic computing and engineering|2022 roadmap on neuromorphic computing and en...]] | 2022 | 神经形态计算路线图综述：涵盖神经形态器件、电路架构、算法应用现状与挑战，展望类脑计算未来发展方向。 |
| [[Forget-free Continual Learning with Winning Subnetworks|Forget-free Continual Learning with Winning S...]] | 2022 | 获胜子网络持续学习方法：基于彩票假设，学习任务自适应二进制掩码，重用先前子网络权重，免疫灾难性遗忘，掩码霍夫曼编码实现容量亚线性增长。 |

## 相关概念

- [[Neuromorphic computing]]
- [[In-memory computing]]
- [[Reservoir computing]]
- [[crossbar]]
- [[Wiki 目录]]
