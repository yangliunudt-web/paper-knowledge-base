---
title: In-memory computing
type: concept
tags: [概念, 基础]
aliases: [IMC, 存内计算, compute-in-memory, Compute-in-memory, CIM, processing-in-memory, PIM, in-memory processing, In‑memory computing, near-memory computing, 近存计算, 存算一体]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> 存内计算（IMC）是一种消除存储墙瓶颈的计算范式，在存储阵列内部直接执行计算操作，避免数据在处理器和存储器之间的频繁搬运。

## 定义

传统冯·诺依曼架构中，数据在 CPU 和存储器之间搬运消耗了大部分能耗和延迟（即存储墙）。IMC 利用存储阵列（如 crossbar）的物理定律（欧姆定律 + 基尔霍夫定律）原地完成矩阵向量乘法（MVM），大幅降低数据搬运开销。

## 关键特性

- **消除存储墙**：计算在存储单元内部完成，无数据搬运
- **高并行度**：crossbar 阵列天然支持大规模并行 MVM
- **模拟计算**：利用模拟域电流求和，一个周期完成 MAC 运算
- **非易失 IMC**：基于 FeFET/ReRAM/MRAM 可实现非易失存内计算，支持 instant-on
- **主要挑战**：模拟计算精度有限、器件变异、ADC/DAC 开销、耐久性

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Accurate deep neural network inference using computational phase-change memory\|Accurate deep neural network inference u...]] | 2020 | 将ResNet CNN映射到PCM器件进行存内推理：批归一化补偿保持精度，CIFAR-10达到93.5%硬件准确率。 |
| [[Memory devices and applications for in‑memory computing\|Memory devices and applications for in‑m...]] | 2020 | 存内计算综述：涵盖基于电荷和基于电阻的存储设备、关键计算原语（向量‑矩阵乘法、逻辑运算、随机计算）及其在科学计算、机器学习等领域的应用，探讨器件与阵列层面的挑战与前景。 |
| [[Parallel convolutional processing using an integrated photonic tensor core\|Parallel convolutional processing using ...]] | 2021 | 集成光子张量核心：基于相变材料存储阵列和孤子微梳，实现每秒10^12次乘加运算，带宽>14 GHz，支持并行卷积处理，为自动驾驶、实时视频处理等数据密集型AI应用提供高速低功耗硬件方案。 |
| [[An Artificial Neural Network Implemented Using Parallel Dual-Gate Thin-Film Transistors\|An Artificial Neural Network Implemented...]] | 2022 | 双栅TFT人工神经网络：单片集成电容器阵列，4×6阵列实现俄罗斯方块分类，双栅结构放大弱信号、抑制强噪声，准静态电荷存储。 |
| [[Highly-scaled and fully-integrated 3-dimensional ferroelectric transistor array for hardware implementation of neural networks\|Highly-scaled and fully-integrated 3-dim...]] | 2023 | 提出基于 HfZrOx 铁电晶体管的三维 NAND 阵列 (3D FeNAND) 用于神经网络硬件实现，通过沟槽结构实现高密度集成，演示了向量矩阵乘法和模式分类，手写数字识别准确率 |
| [[First demonstration of in-memory computing crossbar using multi-level Cell FeFET\|First demonstration of in-memory computi...]] | 2023 | 首次展示基于多级FeFET的存内计算crossbar：1FeFET-1R结构，手写识别96.6%准确率，885.4 TOPS/W能效。 |
| [[Demonstration of Differential Mode FeFET-Array for multi-precision storage and IMC applications\|Demonstration of Differential Mode FeFET...]] | 2023 | 差分模式FeFET阵列：12 Kbit容量、223Mb/mm²密度、VGG-8能效196 TOPS/W、1% BER下训练精度94%/推理精度88%。 |
| [[Ferroelectric compute-in-memory annealer for combinatorial optimization problems\|Ferroelectric compute-in-memory annealer...]] | 2023 | FeFET交叉阵列退火器：组合优化→Ising/QUBO映射，硬件加速模拟退火，高能效COP求解。 |
| [[An in-memory computing architecture based on a duplex two-dimensional material structure for in situ learning\|An in-memory computing architecture base...]] | 2024 | FeFET+单层MoS2双功能器件：突触+神经峰功能，原位学习，高能效片上学习方案。 |
| [[In-memory ferroelectric differentiator\|In-memory ferroelectric differentiator]] | 2025 | 存内铁电微分器：利用铁电电容器本征微分响应，0.24 fJ/次、1 MHz、98.9%准确率。 |
| [[Highly-reliable ferroelectric thin-film transistors array for hardware implementation of image classification\|Highly-reliable ferroelectric thin-film ...]] | 2025 | 研究问题：FeTFT在存内计算中面临弱擦除问题和界面缺陷导致的可靠性下降，限制了其在神经网络硬件实现中的应用。研究方法：提出平面集成MFMIS-FeTFT结构，通过浮栅抑制弱擦除效应，简化工艺减少界面 |
| [[A hardware-adaptive learning algorithm for superlinear-capacity associative memory on memristor crossbars\|A hardware-adaptive learning algorithm f...]] | 2025 | 采用存算一体化架构，利用阻变存储器实现近数据计算。解决了传统冯氏架构中数据搬移的瓶颈问题，实现了高能效的神经网络推理。 |
## 相关概念

- [[FeFET]]
- [[crossbar]]
- [[Memristor]]
- [[RRAM]]
- [[ReRAM]]
- [[Neuromorphic computing]]
- [[Reservoir computing]]
- [[存内计算]]
- [[Wiki 目录]]
