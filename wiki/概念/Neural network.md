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
| [[Accurate deep neural network inference using computational phase-change memory\|Accurate deep neural network inference u...]] | 2020 | Nature Communications |
| [[Neuromorphic computing hardware and neural architectures for robotics\|Neuromorphic computing hardware and neur...]] | 2022 | 综述神经形态计算硬件与神经架构在机器人中的应用：快速低功耗神经网络推理、受生物启发的算法设计、自主智能系统创新应用。 |
| [[Incorporating neuro-inspired adaptability for continual learning in artificial intelligence\|Incorporating neuro-inspired adaptabilit...]] | 2022 | 元可塑性+参数隔离方法，解决持续学习灾难性遗忘，多场景SOTA整体性能。 |
| [[Highly-scaled and fully-integrated 3-dimensional ferroelectric transistor array for hardware implementation of neural networks\|Highly-scaled and fully-integrated 3-dim...]] | 2023 | 提出基于 HfZrOx 铁电晶体管的三维 NAND 阵列 (3D FeNAND) 用于神经网络硬件实现，通过沟槽结构实现高密度集成，演示了向量矩阵乘法和模式分类，手写数字识别准确率 |
| [[First demonstration of in-memory computing crossbar using multi-level Cell FeFET\|First demonstration of in-memory computi...]] | 2023 | 首次利用多级 FeFET 实现存内计算交叉阵列宏，1FeFET-1R 单元支持多位 MAC 操作，手写识别 96.6% 准确率，能效 885.4 TOPS/W。 |
| [[Delocalized photonic deep learning on the internet's edge\|Delocalized photonic deep learning on th...]] | 2023 | 提出 Netcast 光子深度学习：云端智能收发器流式传输权重到边缘设备，实现 40 aJ/MAC 超低能耗推理，86 km 光纤现场试验验证。 |
| [[An index-free sparse neural network using two-dimensional semiconductor ferroelectric field-effect transistors\|An index-free sparse neural network usin...]] | 2024 | 2D FeFET存内稀疏性：稀疏信息嵌入存储单元，超高密度27M/mm²，超低能耗，替代索引稀疏方案。 |
| [[Stochastic Neuro-Fuzzy System Implemented in Memristor Crossbar Arrays\|Stochastic Neuro-Fuzzy System Implemente...]] | 2024 | 忆阻器神经模糊系统：TiN/TaOx/HfOx/TiN，64×128 阵列，变异性增强鲁棒性，6.6x 收敛加速，2.61 TOPS/W 能效。 |
| [[A hardware-adaptive learning algorithm for superlinear-capacity associative memory on memristor crossbars\|A hardware-adaptive learning algorithm f...]] | 2025 | 采用存算一体化架构，利用阻变存储器实现近数据计算。解决了传统冯氏架构中数据搬移的瓶颈问题，实现了高能效的神经网络推理。 |
| [[Memristor Spiking Neural Network for Shortest Path-Based Graph Learning\|Memristor Spiking Neural Network for Sho...]] | 2025 | 忆阻器 SNN 图学习：最短路径并行计算、脉冲传播替代算术、517.82 GTEPS/W、超越 FPGA 3-4 个数量级。 |
| [[Real-Time Signal Processing with Memristor-Based Fused Network\|Real-Time Signal Processing with Memrist...]] | 2025 | 忆阻器 SoC 融合网络：DFT+CNN、128×128 交叉阵列、33.49 dB PSNR、94.72% 分类准确率、~49 倍能效提升。 |
## 相关概念

- [[Neuromorphic computing]]
- [[In-memory computing]]
- [[Reservoir computing]]
- [[crossbar]]
- [[Wiki 目录]]
