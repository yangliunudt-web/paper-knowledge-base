---
title: FeFET
type: concept
tags: [概念, 基础]
aliases: [ferroelectric FET, 铁电场效应晶体管, ferroelectric field-effect transistor, FeFETs]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> 铁电场效应晶体管（FeFET）是一种以铁电材料作为栅介质的三端存储/计算器件，通过铁电极化翻转调控沟道电导，实现非易失性状态存储。

## 定义

FeFET 利用铁电材料的可编程极化状态调制晶体管阈值电压，从而实现非易失性存储。栅极电压脉冲翻转铁电畴极化方向，改变沟道载流子浓度，形成可区分的低/高阈值电压态，对应逻辑 0/1。

核心指标包括：存储窗口（memory window）、耐久性（endurance）、保持时间（retention）、写入/读取速度。

## 关键特性

- **非易失性**：断电后极化状态保持，实现 instant-on 操作
- **低功耗**：写入能量可低至 ~10 fJ/bit 量级
- **CMOS 兼容**：HfO₂ 基铁电材料与 BEOL 工艺兼容
- **多值存储**：部分极化翻转可实现多比特/状态存储
- **存内计算**：利用同一器件同时完成存储和逻辑运算
- **主要挑战**：耐久性有限（~10⁶-10¹⁰ cycles）、写入串扰（write disturb）、保持性 vs 耐久性权衡

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Organic Ferroelectric-Based 1T1T Random Access Memory Cell Employing a Common Dielectric Layer Overcoming the Half-Selection Problem\|Organic Ferroelectric-Based 1T1T Random ...]] | 2017 | 研究问题：基于有机铁电材料的非易失性存储器在制造过程中面临半选问题，即在对目标存储晶体管进行写操作时，会导致相邻存储晶体管被轻微编程。研究方法：提出了一种新型的1T1T FeRAM单元结构，由一个选择 |
| [[1T Non-Volatile Memory Design Using Sub-10nm Ferroelectric FETs\|1T Non-Volatile Memory Design Using Sub-...]] | 2018 | 提出基于 HfZrOx FeFET 的 1T Fe-NOR 非易失性存储器，利用超短沟道增强的漏极-沟道耦合动态调制存储窗口，实现亚 1V 编程/擦除电压和简化操作。 |
| [[Write Disturb in Ferroelectric FETs and Its Implication for 1T-FeFET AND Memory Arrays\|Write Disturb in Ferroelectric FETs and ...]] | 2018 | 研究 HZO FeFET AND 阵列写入干扰：分析 VW/2 和 VW/3 抑制方案，发现低 VTH 态漏电流和高 VTH 态读电流增加是限制阵列尺寸的关键因素，为阵列优化提供指导。 |
| [[Ferroelectric FET Analog Synapse for Acceleration of Deep Neural Network Training\|Ferroelectric FET Analog Synapse for Acc...]] | 2018 | FeFET模拟突触：基于部分极化切换，实现5位对称增强/抑制特性，75ns更新脉冲，45倍电导可调范围，相比多态RRAM突触在线学习延迟加速10^3‑10^6倍。 |
| [[Exploiting Hybrid Precision for Training and Inference of Deep Neural Networks\|Exploiting Hybrid Precision for Training...]] | 2019 | FeFET 混合精度突触：2T1F 设计、易失电容 LSB+非易失 MSB、MNIST 97.3%、CIFAR-10 87%、佐治亚理工学院。 |
| [[Variation‑Resilient FeFET‑Based In‑Memory Computing Leveraging Probabilistic Deep Learning\|Variation‑Resilient FeFET‑Based In‑Memor...]] | 2020 | 基于 FeFET 的变异鲁棒内存计算：通过贝叶斯神经网络融合器件变异特性，在 MNIST 上实现接近理想精度，CIFAR10 上 AlexNet 精度下降仅 |
| [[Hafnium Oxide-Based Ferroelectric Memories Are We Ready for Application\|Hafnium Oxide-Based Ferroelectric Memori...]] | 2021 | HfO2 铁电存储综述：器件物理、材料工程、集成挑战、商业部署评估。 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Device Applications\|Ferroelectric Transistors for Memory and...]] | 2022 | 综述HfO2基FeFET在存储和神经形态器件中的应用：涵盖器件物理、材料工程、多值存储和突触可塑性，展望大规模商业化前景。 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Computing\|Ferroelectric Transistors for Memory and...]] | 2022 | 综述HfO2基FeFET在存储和神经形态计算中的应用：器件结构、工作原理、存储特性和突触应用。 |
| [[Vertical ferroelectric thin-film transistor array with a 10-nm gate length for high-density three-dimensional memory applications\|Vertical ferroelectric thin-film transis...]] | 2022 | 展示 10 nm 栅长垂直 FeTFT 阵列，有效器件尺寸 0.005 μm²，操作速度 <100 ns，耐久性 10⁸ 次循环，演示串级 NAND 操作，仿真确认 200 层 3D 铁电 NAND  |
| [[CMOS-compatible compute-in-memory accelerators based on integrated ferroelectric synaptic arrays for convolution neural networks\|CMOS-compatible compute-in-memory accele...]] | 2022 | FeFET突触阵列CIM加速器：三端FeFET兼存储和访问，HfZrOx/IZO <400°C制备，MNIST验证CIM功能，展示高密度CNN加速潜力。 |
| [[Sub-CMOS-compatible compute-in-memory accelerators based on integrated ferroelectric synaptic arrays for convolution neural networks\|Sub-CMOS-compatible compute-in-memory ac...]] | 2022 | 补充材料：包含 HfZrOx 铁电特性表征、FeTFT 阵列制造工艺流程、器件 I-V 特性曲线等详细实验数据。 |
## 相关概念

- [[HfO2]]
- [[Ferroelectric]]
- [[In-memory computing]]
- [[FeRAM]]
- [[IGZO]]
- [[Wiki 目录]]
