---
title: Monolithic 3D integration
type: concept
tags: [概念, 进阶]
aliases: [M3D, monolithic 3D integration, 单片三维集成, 3D monolithic integration, M3D integration, BEOL integration, 单片3D集成]
created: 2026-05-10
updated: 2026-05-10
sources: []
confidence: medium
---

> 单片三维集成（M3D）是将多层有源器件（逻辑、存储）在单一芯片上逐层垂直堆叠的制造技术，不同于基于 TSV 的芯片堆叠，M3D 实现纳米级层间互连密度，是突破存储墙的关键使能技术。

## 定义

M3D 在 BEOL（后端工艺）中以 <400°C 低温预算逐层沉积和加工有源器件。氧化物半导体（IGZO、ZnO、IWO）、2D 材料（MoS2）和铁电材料（HZO）是主要的 BEOL 兼容器件材料。典型的 M3D CIM 架构将存储阵列置于 BEOL、CMOS 逻辑置于 FEOL，利用面积折叠实现超高密度。

## 关键特性

- **热预算约束**：BEOL 工艺必须 <400°C 以保护铜互连和低-k 介质
- **面积折叠**：存储阵列堆叠在逻辑上方，有效 bit-cell 面积接近 4F² 理论极限
- **BEOL 晶体管**：IGZO/ZnO/IWO TFT 作为 BEOL 访问晶体管
- **BEOL 存储**：HZO FeFET/FeRAM、RRAM、PCM 均可 BEOL 集成
- **层间介质工程**：ILD 材料和工艺对下层器件性能影响显著

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Monolithic 3D integration of 2D transistors and vertical RRAMs in 1T–4R structure for high-densi\|Monolithic 3D integration of 2D transist...]] | 2023 | 本文实验演示了MoS2晶体管与三维垂直RRAM的单片3D集成方案，制造温度低于300°C。MoS2晶体管可驱动VRRAM到4个电阻状态，电路级建模证实比平面存储具有更小面积、更快传输和更低能耗。为高能 |
| [[CMOS Backend-of-Line Compatible Memory Array and Logic Circuitries\|CMOS Backend-of-Line Compatible Memory A...]] | 2023 | CMOS BEOL兼容ZnO TFT：ALD工艺、85/140 cm²/V·s迁移率、1 kbit 1T1R RRAM阵列、环形振荡器>10 MHz、spice模型。 |
| [[Monolithic 3D integration of back-end compatible 2D material FET on Si FinFET\|Monolithic 3D integration of back-end co...]] | 2025 | 单片3D集成：单层MoS2 n‑FET与Si p‑FinFET（鳍宽20 nm）垂直集成形成互补反相器，增益~38，采用CMP/e‑beam蒸发等工业成熟工艺，验证二维材料与硅基器件兼容性。 |
| [[A Compute‑in‑Memory Hardware Accelerator Design With Back‑End‑of‑Line (BEOL) Transistor Based Reconfigurable Interconnect\|A Compute‑in‑Memory Hardware Accelerator...]] | 2022 | Compute-in-memory (CIM) paradigm using ferroelectric field effect transistor (FeFET)\ |
## 相关概念

- [[crossbar]]
- [[IGZO]]
- [[FeFET]]
- [[RRAM]]
- [[In-memory computing]]
- [[Wiki 目录]]
