---
title: FeFET 研究
type: topic
tags: [深度, 基础]
aliases: [铁电场效应晶体管研究, Ferroelectric FET Research]
domain_keywords: [FeFET, ferroelectric FET, ferroelectric transistor, FeRAM, HfO2, HZO, IGZO, ferroelectric polarization, switching kinetics, 铁电]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> FeFET 是知识库核心研究领域，涵盖 68 篇论文。以 HfO₂ 基铁电栅介质为主流方向，研究重点从基础器件物理扩展到存内计算、神经形态计算和 3D 集成。

## 研究子方向

- **基础器件物理**：铁电正交相稳定化、唤醒/疲劳机制、界面工程
- **材料体系**：HZO（Hf₀.₅Zr₀.₅O₂）、Si 掺杂 HfO₂、IGZO 沟道 FeFET
- **器件优化**：高耐久性（>10¹² cycles）、大存储窗口、多值存储
- **存内计算应用**：FeFET crossbar MVM、模拟 IMC、内容可寻址存储器
- **3D 集成**：BEOL 兼容、单片 3D 集成、2T1C 结构
- **可靠性**：写入串扰（write disturb）、保持性退化、温度稳定性

## 关键论文

| 论文 | 年份 | 期刊 | 核心贡献 |
|------|------|------|----------|
| [[Monolithic 3D Integration of High Endurance Multi-bit Ferroelectric FET\|3D 高耐久多值 FeFET]] | 2023 | IEEE VLSI | 单片 3D FeFET 全集成 |
| [[Amorphous Indium Oxide Channel FeFETs with Write Voltage of 0.9V and Endurance 10^{12} for Refresh-free 1T-1FeFET embedded Memory\|0.9V 写入 In₂O₃ FeFET]] | 2025 | IEEE T-ED | 0.9V 超低写入电压，10¹² 耐久性 |
| [[Back-End-of-Line Compatible 2T1C Memory Cell With InGaZnO Thin-Film Transistors and Hf0.5Zr0.5O2-Based Ferroelectric Capacitors\|BEOL 兼容 2T1C IGZO FeFET]] | 2025 | IEEE T-ED | 首次 IGZO TFT + HZO FeCap 全集成 |
| [[First demonstration of in-memory computing crossbar using multi-level Cell FeFET\|首个 FeFET IMC Crossbar]] | 2021 | Nature Comms | 首次 FeFET crossbar IMC 演示 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Device Applications\|FeFET 综述]] | 2023 | Adv. Materials | 铁电晶体管综述 |
| [[Experimental Demonstration of Ferroelectric HfO2 FET with Ultrathin-body IGZO for High-Density and Low-Power Memory Application\|IGZO FeFET 高密度存储]] | 2023 | IEEE EDL | 超薄 IGZO 沟道 FeFET |
| [[Comparative Analysis and Energy-Efficient Write Scheme of Ferroelectric FET-Based Memory Cells\|FeFET 写方案对比]] | 2022 | IEEE Access | FeFET 存储单元节能写方案 |
| [[Nonvolatile Memory Design Based on Ferroelectric FETs\|FeFET 非易失存储设计]] | 2020 | ACM/IEEE DAC | FeFET 非易失存储设计方法 |

## 关键指标进展

| 指标 | 最佳值 | 对应论文 | 说明 |
|------|------|------|------|
| 写入电压 | 0.9 V | [[Amorphous Indium Oxide Channel FeFETs with Write Voltage of 0.9V and Endurance 10^{12} for Refresh-free 1T-1FeFET embedded Memory\|In₂O₃ FeFET]] | BEOL 兼容 |
| 耐久性 | >10¹² cycles | [[Amorphous Indium Oxide Channel FeFETs with Write Voltage of 0.9V and Endurance 10^{12} for Refresh-free 1T-1FeFET embedded Memory\|In₂O₃ FeFET]] | 刷新 free |
| 存储窗口 | >3 V | - | 多值存储基础 |
| 保持时间 | >10⁵ s | [[Back-End-of-Line Compatible 2T1C Memory Cell With InGaZnO Thin-Film Transistors and Hf0.5Zr0.5O2-Based Ferroelectric Capacitors\|2T1C IGZO FeFET]] | 85°C |

## 研究趋势

1. **从 HZO 到多元掺杂**：Si, Al, Gd, La 掺杂调控铁电/反铁电特性
2. **IGZO 沟道成为主流**：BEOL 兼容 + 超低漏电 + 与 HZO 界面优化
3. **耐久性突破**：从 10⁶ → 10¹²，接近 DRAM 级别
4. **写入串扰成为关键瓶颈**：crossbar 集成中的选择器需求
5. **从器件到系统**：FeFET-based IMC 架构、编译器协同设计

## 相关概念

- [[FeFET]]
- [[HfO2]]
- [[Ferroelectric]]
- [[IGZO]]
- [[In-memory computing]]
- [[FeRAM]]
- [[Wiki 目录]]
