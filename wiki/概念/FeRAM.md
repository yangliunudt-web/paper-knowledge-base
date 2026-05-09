---
title: FeRAM
type: concept
tags: [概念, 基础]
aliases: [FRAM, ferroelectric RAM, 铁电随机存储器, ferroelectric memory, 铁电存储器]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> FeRAM（Ferroelectric Random Access Memory）是利用铁电材料的极化翻转实现非易失存储的存储器技术，是最早商业化的铁电存储技术，涵盖 1T1C（类似 DRAM）、1T（FeFET）和 FTJ 等结构。

## 定义

传统 FeRAM 采用 1T1C 结构，铁电电容器（通常 PZT）与访问晶体管串联。写入时在位线和板线间施加电压极化铁电层；读取时检测位线电荷变化（破坏性读取，需回写）。

FeFET 基 FeRAM 将铁电栅介质直接集成到晶体管中，实现 1T 单元（无单独电容器），支持非破坏性读取。

## 关键特性

- **快速写入**：纳秒级极化翻转
- **低功耗**：电场驱动极化，无直流电流
- **非破坏性读取**（FeFET）：读取电流而非电荷
- **HfO₂ 基 FeRAM**：CMOS 兼容，可缩放到先进节点
- **vs DRAM**：非易失但密度低；**vs Flash**：更快但成本高
- **主要挑战**：疲劳导致的耐久性限制、存储窗口缩小、保持性退化

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[1T Non-Volatile Memory Design Using Sub-10nm Ferroelectric FETs\|1T Non-Volatile Memory Design Using Sub-...]] | 2018 | 提出基于 HfZrOx FeFET 的 1T Fe-NOR 非易失性存储器，利用超短沟道增强的漏极-沟道耦合动态调制存储窗口，实现亚 1V 编程/擦除电压和简化操作。 |
| [[Hafnium Oxide-Based Ferroelectric Memories Are We Ready for Application\|Hafnium Oxide-Based Ferroelectric Memori...]] | 2021 | HfO2 铁电存储综述：器件物理、材料工程、集成挑战、商业部署评估。 |
| [[Monolithic Integration of Oxide Semiconductor FET and Ferroelectric Capacitor for 3D Embedded RAM\|Monolithic Integration of Oxide Semicond...]] | 2021 | IGZTO FET+FeRAM 单片集成：>20 cm²/V·s 迁移率、400°C 低温工艺、~ns 操作、3D 嵌入式 RAM、东京大学。 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Device Applications\|Ferroelectric Transistors for Memory and...]] | 2022 | 综述HfO2基FeFET在存储和神经形态器件中的应用：涵盖器件物理、材料工程、多值存储和突触可塑性，展望大规模商业化前景。 |
| [[A 256 Kbit Hf0.5Zr0.5O2-based FeRAM Chip\|A 256 Kbit Hf0.5Zr0.5O2-based FeRAM Chip]] | 2023 | 256 Kbit HZO FeRAM 芯片：sub-8nm 技术，350°C BEOL，0.7 pJ/bit，>10^12 耐久性，O3 预结晶工程。 |
| [[A 2-Transistor-2-Capacitor Ferroelectric Edge Compute-in-Memory Scheme With Disturb-Free Inference and High Endurance\|A 2-Transistor-2-Capacitor Ferroelectric...]] | 2023 | C2FeRAM 2T2C方案：无干扰存内计算、高耐久性、CIFAR-10 VGG8推理>100倍时间且精度下降<1%、相比1T1C FeRAM缓存实现4倍能效/200倍速度/3.2e5倍生命周期提升。 |
| [[Fabrication of One-Transistor-Capacitor Structure of Nonvolatile TFT Ferroelectric RAM Devices Using Ba(Zr0.1Ti0.9)O3 Gated Oxide Film\|Fabrication of One-Transistor-Capacitor ...]] | 2007 | 制备Ba(Zr0.1Ti0.9)O3薄膜用于非晶硅TFT底栅1TC结构铁电RAM器件，优化RF沉积参数，实现4.5 uC/cm2剩余极化、80 kV/cm矫顽场，观察到逆时针电流回滞和存储窗口。器件具 |
| [[用于非破坏性读出铁电存储器的MFIS结构的机理研究\|用于非破坏性读出铁电存储器的MFIS结构的机理研究]] | 2007 | MFIS结构研究：存储窗口随ZrO2厚度变化现极大值、BFO厚度增大增窗口、界面效应与电压分配影响、实验验证理论吻合。 |
| [[Back-End CMOS Compatible and Flexible Ferroelectric Memories for Neuromorphic Computing and Adaptive Sensing\|Back-End CMOS Compatible and Flexible Fe...]] | 2021 | 综述掺杂 HfO2 和分子铁电体作为 CMOS BEOL 兼容和柔性可穿戴平台神经形态器件的潜力，讨论铁电存储器技术在边缘计算中的应用前景。 |
## 相关概念

- [[FeFET]]
- [[Ferroelectric]]
- [[HfO2]]
- [[In-memory computing]]
- [[Wiki 目录]]
