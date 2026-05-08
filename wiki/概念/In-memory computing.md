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
| [[Exploiting Hybrid Precision for Training and Inference of Deep Neural Networks|Exploiting Hybrid Precision for Training and ...]] | 2019 | FeFET 混合精度突触：2T1F 设计、易失电容 LSB+非易失 MSB、MNIST 97.3%、CIFAR-10 87%、佐治亚理工学院。 |
| [[Accurate deep neural network inference using computational phase-change memory|Accurate deep neural network inference using ...]] | 2020 | 本文提出训练ResNet型CNN映射到PCM器件的方法，利用批归一化补偿技术保持精度。在CIFAR-10上实现93.7%（软件）/93.5%（硬件）准确率... |
| [[Memory devices and applications for in‑memory computing|Memory devices and applications for in‑memory...]] | 2020 | 存内计算综述：涵盖基于电荷和基于电阻的存储设备、关键计算原语（向量‑矩阵乘法、逻辑运算、随机计算）及其在科学计算、机器学习等领域的应用，探讨器件与阵列层面... |
| [[Variation‑Resilient FeFET‑Based In‑Memory Computing Leveraging Probabilistic Deep Learning|Variation‑Resilient FeFET‑Based In‑Memory Com...]] | 2020 | 基于 FeFET 的变异鲁棒内存计算：通过贝叶斯神经网络融合器件变异特性，在 MNIST 上实现接近理想精度，CIFAR10 上 AlexNet 精度下降仅 |
| [[DNN+NeuroSim An End-to-End Benchmarking Framework for Compute-in-Memory Accelerators with Versatile Device Technologies|DNN+NeuroSim An End-to-End Benchmarking Frame...]] | 2021 | DNN+NeuroSim基准测试框架：支持SRAM/RRAM/PCM/FeFET/ECRAM等器件，评估存内计算加速器的芯片面积、延迟、能效、推理精度，开... |
| [[In-Memory Learning With Analog Resistive Switching Memory A Review and Perspective|In-Memory Learning With Analog Resistive Swit...]] | 2021 | 模拟电阻开关存储器存内学习综述：定义两层性能指标，分析器件特性、硬件算法、阵列映射、架构电路设计，评估现有器件性能，讨论从器件到系统的挑战与前景。 |
| [[Parallel convolutional processing using an integrated photonic tensor core|Parallel convolutional processing using an in...]] | 2021 | 集成光子张量核心：基于相变材料存储阵列和孤子微梳，实现每秒10^12次乘加运算，带宽>14 GHz，支持并行卷积处理，为自动驾驶、实时视频处理等数据密集型... |
| [[An Artificial Neural Network Implemented Using Parallel Dual-Gate Thin-Film Transistors|An Artificial Neural Network Implemented Usin...]] | 2022 | 双栅TFT人工神经网络：单片集成电容器阵列，4×6阵列实现俄罗斯方块分类，双栅结构放大弱信号、抑制强噪声，准静态电荷存储。 |
| [[Leveraging Ferroelectric Stochasticity and In-Memory Computing for DNN IP Obfuscation|Leveraging Ferroelectric Stochasticity and In...]] | 2022 | 提出基于 FeFET PUF 的 DNN 模型保护方案，利用铁电畴随机性在对抗攻击时破坏权重，保护图神经网络 IP 安全。 |
| [[1F-1T Array Current Limiting Transistor Cascoded FeFET Memory Array for Variation Tolerant Vector-Matrix Multiplication Operation|1F-1T Array Current Limiting Transistor Casco...]] | 2023 | 1F-1T 阵列：FeFET+电流限制晶体管级联，28 nm HKMG，减少 Id 变化，MNIST 97.6% 精度，60% 面积优势。 |
| [[Demonstration of Differential Mode FeFET-Array for multi-precision storage and IMC applications|Demonstration of Differential Mode FeFET-Arra...]] | 2023 | 差分模式FeFET阵列：12 Kbit容量、223Mb/mm²密度、VGG-8能效196 TOPS/W、1% BER下训练精度94%/推理精度88%。 |
| [[FeFET versus DRAM based PIM Architectures A Comparative Study|FeFET versus DRAM based PIM Architectures A C...]] | 2023 | 首次系统比较 FeFET-PIM 和 DRAM-PIM 架构：FeFET 具有高能效 MAC 操作（4.67 fJ/MAC @ 22nm）但容量受限（64... |

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
