---
title: ferroelectric polarization
type: concept
tags: [概念, 基础]
aliases: [铁电极化, remnant polarization, P_r, 剩余极化, spontaneous polarization, P_s, 自发极化, coercive field, E_c, 矫顽场]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> 铁电极化是描述铁电材料性能的核心物理量，P-E（极化-电场）回线的关键参数——剩余极化（P_r）、饱和极化（P_s）、矫顽场（E_c）——直接决定 FeFET 和 FeRAM 的存储窗口、写入电压和可靠性。

## 定义

- **剩余极化（P_r）**：电场归零后材料保持的极化值，决定存储窗口大小
- **饱和极化（P_s）**：足够大电场下的最大极化值
- **矫顽场（E_c）**：使 P = 0 所需的反向电场，决定写入电压
- **印记（imprint）**：P-E 回线沿电场轴偏移，表明内建电场
- **唤醒（wake-up）**：初始循环中 P_r 逐渐增大，与氧空位再分布有关
- **疲劳（fatigue）**：反复翻转后 P_r 衰减，决定器件耐久性

## 关键特性

- **温度依赖性**：居里温度 T_c 以上铁电性消失（顺电相）
- **频率依赖性**：高频下畴翻转不完全，P_r 降低
- **厚度缩放**：HfO₂ 基铁电体在 <5 nm 仍维持铁电性
- **与 FeFET 性能的直接关系**：存储窗口 ∝ 2E_c × t_FE，取决于极化匹配

## 相关论文

| 论文                                                                                                                                                                                   | 年份   | 核心发现                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | --------------------- |
| [[Zn2+ Engineered Low-Barrier LiNbO3 Enables Visible-Light Programmable Ferroelectric Memristors for Noise-Immune Neuromorphic Vision\|Zn2+ Engineered Low-Barrier LiNbO3 Enabl...]] | 2025 | Nature Communications |
## 相关概念

- [[Ferroelectric]]
- [[HfO2]]
- [[FeFET]]
- [[FeRAM]]
- [[Wiki 目录]]
