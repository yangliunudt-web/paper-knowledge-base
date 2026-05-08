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
| [[In-memory ferroelectric differentiator\|In-memory ferroelectric differentiator]] | 2024 | Nature Communications |
| [[Unsupervised local learning based on voltagedependent synaptic plasticity for resistive and ferroelectric synapses\|Unsupervised local learning based on vol...]] | 2024 | Communications Materials |
| [[Ferroelectric Optoelectronic Sensor for Intelligent Flame Detection and In‑Sensor Motion Perception\|Ferroelectric Optoelectronic Sensor for ...]] | 2026 | Nano-Micro Letters |
## 相关概念

- [[HfO2]]
- [[Ferroelectric]]
- [[In-memory computing]]
- [[FeRAM]]
- [[IGZO]]
- [[Wiki 目录]]
