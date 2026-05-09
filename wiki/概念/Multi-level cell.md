---
title: Multi-level cell
type: concept
tags: [概念, 进阶]
aliases: [MLC, 多级单元, 多位存储, multi-level storage, multi-bit cell, multilevel cell]
created: 2026-05-09
updated: 2026-05-09
sources: []
confidence: medium
---

> Multi-level cell (MLC) 是指在单个存储单元中存储多个比特（≥2 bits/cell）的技术，通过编程不同的电导/阈值电压/极化状态实现多值存储，是提升存储密度的关键技术路径。

## 定义

MLC 利用存储介质的模拟可调特性，在单个单元中编码多个离散状态。例如，2 bits/cell 需要 4 个可区分状态，3 bits/cell 需要 8 个状态。在 FeFET 中，通过控制铁电极化的部分翻转实现多级阈值电压；在 RRAM/PCM 中，通过控制编程电流/脉冲宽度实现多级电导状态。

## 关键特性

- **状态数 vs 可靠性权衡**：更多状态提升密度但缩小状态间距，增加读取错误率
- **FeFET MLC**：通过 gate pulse 幅度/宽度控制极化部分翻转，2-4 bits/cell 已有实验验证
- **RRAM MLC**：通过 compliance current 或多脉冲编程控制 filament 尺寸
- **PCM MLC**：利用非晶化比例在宽阻值范围内实现多级存储
- **写验证（write-verify）**：MLC 编程通常需要迭代写-读验证循环以保证状态精度
- **关键挑战**：器件变异、保持期间的 drift（PCM/RRAM）、读干扰、耐久性退化导致的窗口闭合

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Amorphous Indium Oxide Channel FeFETs with Write Voltage of 0.9V and Endurance 10^{12} for Refresh-free 1T-1FeFET embedded Memory\|Amorphous Indium Oxide Channel FeFETs wi...]] | 2023 | 首次BEOL兼容IWO FeFET：写入<0.9V，耐久性>10¹²循环，85°C保持>10⁴s，无需刷新1T-1FeFET存储器。 |
| [[First demonstration of in-memory computing crossbar using multi-level Cell FeFET\|First demonstration of in-memory computi...]] | 2023 | 首次展示基于多级FeFET的存内计算crossbar：1FeFET-1R结构，手写识别96.6%准确率，885.4 TOPS/W能效。 |
| [[Disturb-Free Operations of Multilevel Cell Ferroelectric FETs for Nand Applications\|Disturb-Free Operations of Multilevel Ce...]] | 2023 | MLC FeFET NAND阵列无干扰操作：实验研究编程/读取干扰，提出稳定多级写入/读取方案，确定抑制电压与通过电压容限。 |
| [[Unlocking Large Memory Windows and 16-Level Data per Cell Memory Operations in Hafnia-Based Ferroelectric Transistors\|Unlocking Large Memory Windows and 16-Le...]] | 2024 | HfAlOx FeTFT 16 级存储：MFMFS 栅极堆叠，10V 存储窗口，DCC 一次性编程，3D 兼容。 |
| [[Ultra-Low Power Robust 3bit cell $ mathrm{Hf}_{0.5} mathrm{Zr}_{0.5} mathrm{O}_2$ Ferroelectric FinFET with High Endurance for Advanced Computing-In-Memory Technology\|Ultra-Low Power Robust 3bit cell $ mathr...]] | 2024 | 通过后鳍形成表面工程去除Si表面线边缘粗糙度和Br杂质，改善HZO-Si界面质量，实现10nm HZO FinFET的3bit/单元操作、ION/IOFF>10^6、10^11次耐久性、85°C下10 |
| [[A Compact Writing Scheme for the Reliability Challenges in 1T Multi-Level FeFET Array Variation, Endurance, and Write Disturb\|A Compact Writing Scheme for the Reliabi...]] | 2024 | 紧凑写入方案：错误率降低>6倍、耐久性提升>100倍、Vth漂移减少>7倍，1T FeFET阵列实现2比特/单元存储、10^8周期耐久性、写入干扰免疫。 |
| [[Multi-Level Operation of Ferroelectric FET Memory Arrays for Compute-In-Memory Applications\|Multi-Level Operation of Ferroelectric F...]] | 2023 | 报道AND连接FeFET阵列的MLC操作及其在存内计算中的适用性：研究被动AND阵列中FeFET的切换行为和器件变异，设计合适的写入和抑制方案保护任意FeFET状态，实现AND阵列MLC操作，CIFA |
| [[One-Pulse-Programmable Multi-Level PCMSelector Cross-Point Memory for 20 nm Half Pitch and Beyond\|One-Pulse-Programmable Multi-Level PCMSe...]] | 2024 | 首次实现无需初始化和迭代验证的PCM/选通管多级存储单元，通过TE厚度优化控制热耗散、PCM组分垂直设计（上层富Te提高熔点）形成稳定的晶态-非晶态共存的中间电阻态（MRS），单脉冲编程、>10^7次 |
## 相关概念

- [[FeFET]]
- [[RRAM]]
- [[crossbar]]
- [[In-memory computing]]
- [[Wiki 目录]]
