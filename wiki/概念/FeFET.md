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
| [[Fabrication of One-Transistor-Capacitor Structure of Nonvolatile TFT Ferroelectric RAM Devices Using Ba(Zr0.1Ti0.9)O3 Gated Oxide Film|Fabrication of One-Transistor-Capacitor Struc...]] | 2007 | 制备 Ba(Zr0.1Ti0.9)O3 薄膜并用于非晶硅 TFT 底栅 1TC 铁电 RAM 器件，优化 RF 沉积参数，实现 4.5 uC/cm2 剩余... |
| [[Nonvolatile Memory Design Based on Ferroelectric FETs|Nonvolatile Memory Design Based on Ferroelect...]] | 2016 | 2T FeFET非易失存储器：利用三端结构实现分离读/写路径，非破坏性读取，相比FeRAM写入电压降低58.5%、能量降低67.7%，区分度10^6倍，能... |
| [[1T Non-Volatile Memory Design Using Sub-10nm Ferroelectric FETs|1T Non-Volatile Memory Design Using Sub-10nm ...]] | 2018 | 提出基于 HfZrOx FeFET 的 1T Fe-NOR 非易失性存储器，利用超短沟道增强的漏极-沟道耦合动态调制存储窗口，实现亚 1V 编程/擦除电压... |
| [[Ferroelectric FET Analog Synapse for Acceleration of Deep Neural Network Training|Ferroelectric FET Analog Synapse for Accelera...]] | 2018 | FeFET模拟突触：基于部分极化切换，实现5位对称增强/抑制特性，75ns更新脉冲，45倍电导可调范围，相比多态RRAM突触在线学习延迟加速10^3‑10... |
| [[Symmetric 2-D-Memory Access to Multidimensional Data|Symmetric 2-D-Memory Access to Multidimension...]] | 2018 | 基于铁电晶体管的新型二维存储器架构实现单周期行/列访问，在256×256矩阵操作中减少86%行缓冲事务，能耗降低5%~93%，延迟减少11%~95%。 |
| [[Write Disturb in Ferroelectric FETs and Its Implication for 1T-FeFET AND Memory Arrays|Write Disturb in Ferroelectric FETs and Its I...]] | 2018 | 研究 HZO FeFET AND 阵列写入干扰：分析 VW/2 和 VW/3 抑制方案，发现低 VTH 态漏电流和高 VTH 态读电流增加是限制阵列尺寸的... |
| [[Atomic-scale characterization of defects generation during fatigue in ferroelectric Hf0.5Zr0.5O2 films vacancy generation and lattice dislocation|Atomic-scale characterization of defects gene...]] | 2019 | 采用铁电存储器器件，研究其在神经形态计算中的应用。分析了器件的工作原理和性能特性，为下一代内存计算提供了解决方案。 |
| [[Exploiting Hybrid Precision for Training and Inference of Deep Neural Networks|Exploiting Hybrid Precision for Training and ...]] | 2019 | FeFET 混合精度突触：2T1F 设计、易失电容 LSB+非易失 MSB、MNIST 97.3%、CIFAR-10 87%、佐治亚理工学院。 |
| [[Ferroelectric FET Based In-Memory Computing for Few-Shot Learning|Ferroelectric FET Based In-Memory Computing f...]] | 2019 | FeFET 小样本学习存内计算：模拟电导权重存储，原型网络硬件实现，边缘能效推理。 |
| [[Variation‑Resilient FeFET‑Based In‑Memory Computing Leveraging Probabilistic Deep Learning|Variation‑Resilient FeFET‑Based In‑Memory Com...]] | 2020 | 基于 FeFET 的变异鲁棒内存计算：通过贝叶斯神经网络融合器件变异特性，在 MNIST 上实现接近理想精度，CIFAR10 上 AlexNet 精度下降仅 |
| [[Attention-in-Memory for Few-Shot Learning with Configurable Ferroelectric FET Arrays|Attention-in-Memory for Few-Shot Learning wit...]] | 2021 | AiM 存内计算设计：可配置 FeFET 阵列，实现 MANN 注意力层，5-way 5-shot Omniglot 任务精度 95.14%，优于现有加速器。 |
| [[Back-End CMOS Compatible and Flexible Ferroelectric Memories for Neuromorphic Computing and Adaptive Sensing|Back-End CMOS Compatible and Flexible Ferroel...]] | 2021 | 综述掺杂 HfO2 和分子铁电体作为 CMOS BEOL 兼容和柔性可穿戴平台神经形态器件的潜力，讨论铁电存储器技术在边缘计算中的应用前景。 |

## 相关概念

- [[HfO2]]
- [[Ferroelectric]]
- [[In-memory computing]]
- [[FeRAM]]
- [[IGZO]]
- [[Wiki 目录]]
