---
title: MoS₂
type: concept
tags: [概念, 进阶]
aliases: [MoS2, molybdenum disulfide, 二硫化钼, 2D semiconductor, transition metal dichalcogenide, TMDC, 二维材料, 2D materials, monolayer MoS2]
created: 2026-05-10
updated: 2026-05-10
sources: []
confidence: medium
---

> 二硫化钼（MoS₂）是最具代表性的过渡金属二硫族化物（TMDC）二维半导体材料，单层 MoS₂ 具有直接带隙（~1.8 eV）、高开关比和原子级厚度，是 BEOL 兼容晶体管和存内计算器件的理想沟道材料。

## 定义

单层 MoS₂ 由 S-Mo-S 三层原子组成，通过范德华力层间结合。MOCVD 可生长晶圆级单层 MoS₂，实现大规模器件阵列。MoS₂ 的高表面积-体积比使其对电荷变化极为敏感，适合电荷俘获型存储器和传感器应用。

## 关键特性

- **直接带隙**：单层 ~1.8 eV，体材料 ~1.2 eV（间接带隙）
- **高开关比**：>10⁶ 的 Ion/Ioff 比
- **低温工艺**：MOCVD 生长或机械剥离可在 <400°C 完成
- **BEOL 兼容**：可转移或直接在 BEOL 互连层上生长
- **存储应用**：MoS₂ 通道 + 电荷俘获栅堆叠（Al₂O₃/HfO₂/Al₂O₃）实现非易失性存储
- **突触器件**：三端 memtransistor 支持栅极调制的异突触可塑性
- **异构集成**：与 FeFET、RRAM 等可单片 3D 集成

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Monolithic 3D integration of 2D transistors and vertical RRAMs in 1T–4R structure for high-densi\|Monolithic 3D integration of 2D transist...]] | 2023 | 本文实验演示了MoS2晶体管与三维垂直RRAM的单片3D集成方案，制造温度低于300°C。MoS2晶体管可驱动VRRAM到4个电阻状态，电路级建模证实比平面存储具有更小面积、更快传输和更低能耗。为高能 |
| [[An index-free sparse neural network using two-dimensional semiconductor ferroelectric field-effect transistors\|An index-free sparse neural network usin...]] | 2024 | 二维FeFET实现无索引稀疏神经网络，高能效边缘AI处理。 |
| [[An in-memory computing architecture based on a duplex two-dimensional material structure for in situ learning\|An in-memory computing architecture base...]] | 2024 | FeFET+单层MoS2双功能器件：突触+神经峰功能，原位学习，高能效片上学习方案。 |
| [[Monolithic 3D integration of back-end compatible 2D material FET on Si FinFET\|Monolithic 3D integration of back-end co...]] | 2025 | 单片3D集成：单层MoS2 n‑FET与Si p‑FinFET（鳍宽20 nm）垂直集成形成互补反相器，增益~38，采用CMP/e‑beam蒸发等工业成熟工艺，验证二维材料与硅基器件兼容性。 |
| [[High-Endurance MoS2 FeFET with Operating Voltage Less Than 1V for eNVM in Scaled CMOS\|High-Endurance MoS2 FeFET with Operating...]] | 2025 | 单层MoS₂ FeFET：超薄HZO（2.5nm）实现<1V工作电压、>10^12次耐久性、>10年保持时间，兼容CMOS后端工艺，适用于先进节点嵌入式存储。 |
| [[Homogeneous integration of two-dimensional material-based optoelectronic neurons and ferroelectric synapses for neuromorphic vision\|Homogeneous integration of two-dimension...]] | 2026 | 实现 MoS2 光电 LIF 神经元与铁电突触的均匀集成：多光谱传感、无电容积分、阈值触发脉冲，SNN 系统颜色识别 91.7%、目标检测 93.5% |
## 相关概念

- [[Monolithic 3D integration]]
- [[BEOL]]
- [[In-memory computing]]
- [[FeFET]]
- [[Wiki 目录]]
