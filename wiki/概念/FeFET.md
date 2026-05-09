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
| [[1T Non-Volatile Memory Design Using Sub-10nm Ferroelectric FETs\|1T Non-Volatile Memory Design Using Sub-...]] | 2018 | 提出基于 HfZrOx FeFET 的 1T Fe-NOR 非易失性存储器，利用超短沟道增强的漏极-沟道耦合动态调制存储窗口，实现亚 1V 编程/擦除电压和简化操作。 |
| [[Write Disturb in Ferroelectric FETs and Its Implication for 1T-FeFET AND Memory Arrays\|Write Disturb in Ferroelectric FETs and ...]] | 2018 | 研究 HZO FeFET AND 阵列写入干扰：分析 VW/2 和 VW/3 抑制方案，发现低 VTH 态漏电流和高 VTH 态读电流增加是限制阵列尺寸的关键因素，为阵列优化提供指导。 |
| [[Ferroelectric FET Analog Synapse for Acceleration of Deep Neural Network Training\|Ferroelectric FET Analog Synapse for Acc...]] | 2018 | FeFET模拟突触：基于部分极化切换，实现5位对称增强/抑制特性，75ns更新脉冲，45倍电导可调范围，相比多态RRAM突触在线学习延迟加速10^3‑10^6倍。 |
| [[Variation‑Resilient FeFET‑Based In‑Memory Computing Leveraging Probabilistic Deep Learning\|Variation‑Resilient FeFET‑Based In‑Memor...]] | 2020 | 基于 FeFET 的变异鲁棒内存计算：通过贝叶斯神经网络融合器件变异特性，在 MNIST 上实现接近理想精度，CIFAR10 上 AlexNet 精度下降仅 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Device Applications\|Ferroelectric Transistors for Memory and...]] | 2022 | 综述HfO2基FeFET在存储和神经形态器件中的应用：涵盖器件物理、材料工程、多值存储和突触可塑性，展望大规模商业化前景。 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Computing\|Ferroelectric Transistors for Memory and...]] | 2022 | 综述HfO2基FeFET在存储和神经形态计算中的应用：器件结构、工作原理、存储特性和突触应用。 |
| [[CMOS-compatible compute-in-memory accelerators based on integrated ferroelectric synaptic arrays for convolution neural networks\|CMOS-compatible compute-in-memory accele...]] | 2022 | FeFET突触阵列CIM加速器：三端FeFET兼存储和访问，HfZrOx/IZO <400°C制备，MNIST验证CIM功能，展示高密度CNN加速潜力。 |
| [[Highly-scaled and fully-integrated 3-dimensional ferroelectric transistor array for hardware implementation of neural networks\|Highly-scaled and fully-integrated 3-dim...]] | 2023 | 提出基于 HfZrOx 铁电晶体管的三维 NAND 阵列 (3D FeNAND) 用于神经网络硬件实现，通过沟槽结构实现高密度集成，演示了向量矩阵乘法和模式分类，手写数字识别准确率 |
| [[Amorphous Indium Oxide Channel FeFETs with Write Voltage of 0.9V and Endurance 10^{12} for Refresh-free 1T-1FeFET embedded Memory\|Amorphous Indium Oxide Channel FeFETs wi...]] | 2023 | 首次BEOL兼容IWO FeFET：写入<0.9V，耐久性>10¹²循环，85°C保持>10⁴s，无需刷新1T-1FeFET存储器。 |
| [[First demonstration of in-memory computing crossbar using multi-level Cell FeFET\|First demonstration of in-memory computi...]] | 2023 | 首次展示基于多级FeFET的存内计算crossbar：1FeFET-1R结构，手写识别96.6%准确率，885.4 TOPS/W能效。 |
| [[Write Bias Scheme Optimization of Ferroelectric Field-Effect-Transistor (FeFET) Synapse for Accurate On-chip Training\|Write Bias Scheme Optimization of Ferroe...]] | 2023 | 通过TCAD仿真优化FeFET突触片上训练的写入偏置方案，实现4位突触操作和高对称性/线性度的增强抑制特性，即使在工艺变异下仍保持良好性能。 |
| [[Novel Complementary FeFET- based Lookup Table and Routing Switch Design and their Applications in EnergyArea-Efficient FPGA\|Novel Complementary FeFET- based Lookup ...]] | 2023 | 互补FeFET构建现场可编程门阵列查找表与路由开关：p‑FeFET与n‑FeFET堆叠实现1位存储与2‑1多路复用器，无短路电流，漏电流低，功耗-性能-面积优于静态随机存取存储器/电流模式FeFET设 |
## 相关概念

- [[HfO2]]
- [[Ferroelectric]]
- [[In-memory computing]]
- [[FeRAM]]
- [[IGZO]]
- [[Wiki 目录]]
