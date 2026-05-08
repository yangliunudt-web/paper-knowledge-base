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
| [[Exploiting Hybrid Precision for Training and Inference of Deep Neural Networks\|Exploiting Hybrid Precision for Training...]] | 2019 | FeFET 混合精度突触：2T1F 设计、易失电容 LSB+非易失 MSB、MNIST 97.3%、CIFAR-10 87%、佐治亚理工学院。 |
| [[Accurate deep neural network inference using computational phase-change memory\|Accurate deep neural network inference u...]] | 2020 | Nature Communications |
| [[Variation‑Resilient FeFET‑Based In‑Memory Computing Leveraging Probabilistic Deep Learning\|Variation‑Resilient FeFET‑Based In‑Memor...]] | 2020 | 基于 FeFET 的变异鲁棒内存计算：通过贝叶斯神经网络融合器件变异特性，在 MNIST 上实现接近理想精度，CIFAR10 上 AlexNet 精度下降仅 |
| [[Memory devices and applications for in‑memory computing\|Memory devices and applications for in‑m...]] | 2020 | 存内计算综述：涵盖基于电荷和基于电阻的存储设备、关键计算原语（向量‑矩阵乘法、逻辑运算、随机计算）及其在科学计算、机器学习等领域的应用，探讨器件与阵列层面的挑战与前景。 |
| [[Parallel convolutional processing using an integrated photonic tensor core\|Parallel convolutional processing using ...]] | 2021 | 集成光子张量核心：基于相变材料存储阵列和孤子微梳，实现每秒10^12次乘加运算，带宽>14 GHz，支持并行卷积处理，为自动驾驶、实时视频处理等数据密集型AI应用提供高速低功耗硬件方案。 |
| [[An Artificial Neural Network Implemented Using Parallel Dual-Gate Thin-Film Transistors\|An Artificial Neural Network Implemented...]] | 2022 | 双栅TFT人工神经网络：单片集成电容器阵列，4×6阵列实现俄罗斯方块分类，双栅结构放大弱信号、抑制强噪声，准静态电荷存储。 |
| [[Highly-scaled and fully-integrated 3-dimensional ferroelectric transistor array for hardware implementation of neural networks\|Highly-scaled and fully-integrated 3-dim...]] | 2023 | 提出基于 HfZrOx 铁电晶体管的三维 NAND 阵列 (3D FeNAND) 用于神经网络硬件实现，通过沟槽结构实现高密度集成，演示了向量矩阵乘法和模式分类，手写数字识别准确率 |
| [[First demonstration of in-memory computing crossbar using multi-level Cell FeFET\|First demonstration of in-memory computi...]] | 2023 | 首次利用多级 FeFET 实现存内计算交叉阵列宏，1FeFET-1R 单元支持多位 MAC 操作，手写识别 96.6% 准确率，能效 885.4 TOPS/W。 |
| [[Demonstration of Differential Mode FeFET-Array for multi-precision storage and IMC applications\|Demonstration of Differential Mode FeFET...]] | 2023 | 差分模式FeFET阵列：12 Kbit容量、223Mb/mm²密度、VGG-8能效196 TOPS/W、1% BER下训练精度94%/推理精度88%。 |
| [[Ferroelectric compute-in-memory annealer for combinatorial optimization problems\|Ferroelectric compute-in-memory annealer...]] | 2023 | FeFET交叉阵列退火器：组合优化→Ising/QUBO映射，硬件加速模拟退火，高能效COP求解。 |
| [[An index-free sparse neural network using two-dimensional semiconductor ferroelectric field-effect transistors\|An index-free sparse neural network usin...]] | 2024 | 2D FeFET存内稀疏性：稀疏信息嵌入存储单元，超高密度27M/mm²，超低能耗，替代索引稀疏方案。 |
| [[Two-dimensional fully ferroelectric-gated hybrid computing-in-memory hardware for high-precision and energy-efficient dynamic tracking\|Two-dimensional fully ferroelectric-gate...]] | 2024 | 2D FeFET 混合 CIM：布尔逻辑+多级单元、96.36% 良率、>10^12 耐久性、用于动态跟踪。 |
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
