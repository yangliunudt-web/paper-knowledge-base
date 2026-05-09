---
title: Memristor
type: concept
tags: [概念, 基础]
aliases: [忆阻器, memristive device, memristors, RRAM, memristive network, Memristive network, resistive memory, Resistive memory, 阻变存储器]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> 忆阻器（Memristor）是记忆电阻的简称，其电阻值随流经电荷的历史而改变，是第四种基本电路元件（继电阻、电容、电感之后），在非易失存储和神经形态计算中广泛用作突触器件。

## 定义

忆阻器理论由蔡少棠（Leon Chua）于 1971 年提出，2008 年 HP 实验室首次在 TiO₂ 器件中实现物理验证。其阻变机理包括：氧空位导电细丝（VCM）、金属离子导电细丝（ECM）、界面效应等。

在神经形态计算中，忆阻器的电导值代表突触权重，通过施加编程脉冲调节电导。

## 关键特性

- **非易失性存储**：电阻状态断电保持
- **多值/模拟存储**：部分阻变可实现多电导态（>4 bit）
- **纳秒级切换速度**
- **高密度集成**：crossbar 结构支持 4F² 单元面积
- **突触可塑性模拟**：渐进电导变化天然模拟 STDP、LTP/LTD
- **主要挑战**：cycle-to-cycle 和 device-to-device 变异、 stuck-at faults、耐久性 vs 保持性权衡

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Memory devices and applications for in‑memory computing\|Memory devices and applications for in‑m...]] | 2020 | 存内计算综述：涵盖基于电荷和基于电阻的存储设备、关键计算原语（向量‑矩阵乘法、逻辑运算、随机计算）及其在科学计算、机器学习等领域的应用，探讨器件与阵列层面的挑战与前景。 |
| [[Fusion of Memristor and Digital Compute-In-Memory Processing Units\|Fusion of Memristor and Digital Compute-...]] | 2023 | 忆阻器-SRAM CIM 融合：77.64 TOPS/W、392μs 唤醒、<0.5% 精度损失、TSMC 22nm、自适应本地训练。 |
| [[Reservoir Computing System with Diverse Input Patterns in HfAlO-Based Ferroelectric Memristor\|Reservoir Computing System with Diverse ...]] | 2024 | 实现基于 Al 掺杂 HfO 铁电忆阻器的储备池计算系统，演示可处理多种输入脉冲类型的鲁棒储备池层，模拟生物突触短期可塑性，验证图像训练和巴甫洛夫实验等应用。 |
| [[Stochastic Neuro-Fuzzy System Implemented in Memristor Crossbar Arrays\|Stochastic Neuro-Fuzzy System Implemente...]] | 2024 | 忆阻器神经模糊系统：TiN/TaOx/HfOx/TiN，64×128 阵列，变异性增强鲁棒性，6.6x 收敛加速，2.61 TOPS/W 能效。 |
| [[Electrochemical ohmic memristors for Electrochemical oh\|Electrochemical ohmic memristors for Ele...]] | 2024 | 本文提出电化学欧姆忆阻器，利用电化学机制实现可靠阻变切换和欧姆行为，面向神经形态计算应用。 |
| [[A hardware-adaptive learning algorithm for superlinear-capacity associative memory on memristor crossbars\|A hardware-adaptive learning algorithm f...]] | 2025 | 采用存算一体化架构，利用阻变存储器实现近数据计算。解决了传统冯氏架构中数据搬移的瓶颈问题，实现了高能效的神经网络推理。 |
| [[Memristor Spiking Neural Network for Shortest Path-Based Graph Learning\|Memristor Spiking Neural Network for Sho...]] | 2025 | 忆阻器 SNN 图学习：最短路径并行计算、脉冲传播替代算术、517.82 GTEPS/W、超越 FPGA 3-4 个数量级。 |
| [[Memristor‑based adaptive analog‑to‑digital conversion for efficient and accurate compute‑in‑memory\|Memristor‑based adaptive analog‑to‑digit...]] | 2025 | 提出基于忆阻器的自适应模数转换器，利用可编程重叠边界的模拟 CAM 单元实现优化量化阈值，在 CIFAR‑10 上达到 89.55% 准确率，能效提升 15.1 倍，面积减少 12.9 倍，集成到 C |
| [[Real-Time Signal Processing with Memristor-Based Fused Network\|Real-Time Signal Processing with Memrist...]] | 2025 | 忆阻器 SoC 融合网络：DFT+CNN、128×128 交叉阵列、33.49 dB PSNR、94.72% 分类准确率、~49 倍能效提升。 |
| [[A near-threshold memristive computing-inmemory engine for edge intelligence\|A near-threshold memristive computing-in...]] | 2025 | 近阈值忆阻存内计算引擎：亚阈值区crossbar操作，超低功耗边缘智能。 |
| [[Van der Waals Engineering of One-Transistor-One-Ferroelectric-Memristor Architecture for an Energy-Efficient Neuromorphic Array\|Van der Waals Engineering of One-Transis...]] | 2025 | 提出基于范德华工程的CuCrP2S6/MoS2/h-BN全二维材料1T1M架构，利用CuCrP2S6的铁电极化反转实现非易失阻变，电阻可调性达10^6，潜行电流低至120 fA，静态功耗仅12 fW。 |
| [[Large-scale crossbar arrays based on threeterminal MoS2 memtransistors\|Large-scale crossbar arrays based on thr...]] | 2025 | 大规模MoS2记忆晶体管交叉阵列：每阵列2048器件，良率>92%，写入能量~0.2 fJ，读取裕度10⁵，保持>3年，栅极调制解决推理模糊性，MNIST分类验证，性能优于其他2D材料架构。 |
## 相关概念

- [[RRAM]]
- [[ReRAM]]
- [[crossbar]]
- [[Neuromorphic computing]]
- [[In-memory computing]]
- [[selector]]
- [[Wiki 目录]]
