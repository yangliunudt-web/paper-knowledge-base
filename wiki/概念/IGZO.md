---
title: IGZO
type: concept
tags: [概念, 基础]
aliases: [InGaZnO, indium gallium zinc oxide, 铟镓锌氧化物, IGZO TFT, a-IGZO, amorphous IGZO]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> IGZO（铟镓锌氧化物）是一种非晶氧化物半导体，广泛用作 BEOL 兼容薄膜晶体管（TFT）的沟道材料，在 FeFET 和 3D 集成中扮演关键角色。

## 定义

IGZO 是通过 In₂O₃、Ga₂O₃、ZnO 共溅射形成的非晶氧化物半导体。非晶结构使其在大面积上保持均匀性，同时保留了氧化物半导体的高迁移率（~10-50 cm²/V·s），远超 a-Si:H（~1 cm²/V·s）。

## 关键特性

- **BEOL 兼容**：低温沉积（<400°C），可在金属互连层上制造
- **超低漏电流**：宽禁带（~3 eV）→ 极低关态电流（<10⁻²² A/µm）→ 适合低功耗/存储应用
- **高开态电流**：10-100 µA/µm
- **透明柔性**：可见光透明，可用于柔性电子
- **与 FeFET 结合**：IGZO 沟道 + HZO 栅介质的 FeFET 可实现超高耐久性（>10¹² cycles）
- **主要挑战****：偏压/光照不稳定性、p 型掺杂困难、与 HfO₂ 界面态优化

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Experimental Demonstration of Ferroelectric HfO2 FET with Ultrathin-body IGZO for High-Density and Low-Power Memory Application\|Experimental Demonstration of Ferroelect...]] | 2023 | 超薄体IGZO FeFET实验演示：采用HfO2铁电层，实现高迁移率、理想亚阈值斜率、可控存储窗口，为高密度低功耗存储应用提供新方案。 |
| [[Inter-Layer Dielectric Engineering for Monolithic Stacking $4 mathrm { F } ^ { 2 }$ -2T0C DRAM with Channel-All-Around (CAA) IGZO FET to Achieve Good Reliability $( 1 0 ^ { 4 } mathrm { s }$ Bias Stre\|Inter-Layer Dielectric Engineering for M...]] | 2023 | CAA-IGZO FET层间介质工程：优化PEALD工艺改善H穿透问题，实现>10⁴s保持特性和2T0C DRAM堆叠可行性。 |
## 相关概念

- [[FeFET]]
- [[HfO2]]
- [[In-memory computing]]
- [[Wiki 目录]]
