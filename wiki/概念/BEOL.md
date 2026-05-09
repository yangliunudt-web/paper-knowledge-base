---
title: BEOL
type: concept
tags: [概念, 基础]
aliases: [back-end-of-line, BEOL, 后端工艺, backend-of-line, back end of line, CMOS BEOL, BEOL compatible]
created: 2026-05-10
updated: 2026-05-10
sources: []
confidence: medium
---

> BEOL（Back-End-of-Line，后端工艺）是 CMOS 制造流程中在晶体管（FEOL）完成后进行金属互连层加工的工艺阶段。BEOL 兼容性指材料和器件可在 <400°C 低温下制造，不破坏已完成的铜互连和低-k 介质层。

## 定义

BEOL 工艺温度上限由铜互连的热稳定性（~400°C）决定。传统 Si 晶体管需要 >800°C 的激活退火，因此只能放在 FEOL。BEOL 兼容器件使用氧化物半导体、2D 材料或铁电材料，在低温下实现高性能，可直接堆叠在互连层之上或之间。

## 关键特性

- **温度上限**：<400°C（铜互连热预算）
- **BEOL 晶体管**：IGZO、ZnO、IWO、MoS2 FET
- **BEOL 存储器**：HZO FeFET/FeRAM、RRAM、PCM
- **面积优势**：BEOL 存储不占用 FEOL Si 面积
- **3D 堆叠**：多层 BEOL 器件垂直堆叠实现超高密度

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Amorphous Indium Oxide Channel FeFETs with Write Voltage of 0.9V and Endurance 10^{12} for Refresh-free 1T-1FeFET embedded Memory\|Amorphous Indium Oxide Channel FeFETs wi...]] | 2023 | 首次BEOL兼容IWO FeFET：写入<0.9V，耐久性>10¹²循环，85°C保持>10⁴s，无需刷新1T-1FeFET存储器。 |
| [[A 256 Kbit Hf0.5Zr0.5O2-based FeRAM Chip\|A 256 Kbit Hf0.5Zr0.5O2-based FeRAM Chip]] | 2023 | 256 Kbit HZO FeRAM 芯片：sub-8nm 技术，350°C BEOL，0.7 pJ/bit，>10^12 耐久性，O3 预结晶工程。 |
| [[Back-End-of-Line Compatible 2T1C Memory Cell With InGaZnO Thin-Film Transistors and Hf0.5Zr0.5O2-Based Ferroelectric Capacitors\|Back-End-of-Line Compatible 2T1C Memory ...]] | 2025 | BEOL兼容2T1C存储单元：首次实现InGaZnO TFT与HZO铁电电容器全集成，面积比1:8时写入2V/读取2.5V，保持时间≥10^5秒，耐久性≥10^7次循环。 |
| [[High-Endurance MoS2 FeFET with Operating Voltage Less Than 1V for eNVM in Scaled CMOS\|High-Endurance MoS2 FeFET with Operating...]] | 2025 | 单层MoS₂ FeFET：超薄HZO（2.5nm）实现<1V工作电压、>10^12次耐久性、>10年保持时间，兼容CMOS后端工艺，适用于先进节点嵌入式存储。 |
| [[Back-End CMOS Compatible and Flexible Ferroelectric Memories for Neuromorphic Computing and Adaptive Sensing\|Back-End CMOS Compatible and Flexible Fe...]] | 2021 | 综述掺杂 HfO2 和分子铁电体作为 CMOS BEOL 兼容和柔性可穿戴平台神经形态器件的潜力，讨论铁电存储器技术在边缘计算中的应用前景。 |
## 相关概念

- [[Monolithic 3D integration]]
- [[FeFET]]
- [[RRAM]]
- [[IGZO]]
- [[Wiki 目录]]
