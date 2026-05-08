---
title: Ferroelectric
type: concept
tags: [概念, 基础]
aliases: [铁电, ferroelectricity, 铁电性, ferroelectric material, ferroelectric polarization]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> 铁电性是指某些介电材料在没有外加电场时仍能保持自发极化，且极化方向可被外加电场翻转的物理性质。铁电材料是 FeFET、FeRAM 和 FTJ 等非易失存储器件的基础。

## 定义

铁电材料具有两个及以上稳定的极化态，由晶体结构中的离子位移产生电偶极矩。极化-电场（P-E）关系呈现特征性的电滞回线（hysteresis loop）。关键参数包括：剩余极化（P_r）、矫顽场（E_c）、饱和极化（P_s）。

## 关键特性

- **可翻转极化**：极化方向可被外部电场翻转，形成双稳存储
- **非易失**：断电后极化保持
- **快速切换**：极化翻转可在亚纳秒级完成
- **疲劳**：反复翻转后极化衰减，影响器件耐久性
- **铁电/反铁电**：反铁电体中相邻偶极子反平行排列，P-E 呈双回线
- **传统材料**：PZT（钙钛矿）、SBT → **新兴**：HfO₂ 基（CMOS 兼容）

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Ferroelectric Transistors for Memory and Neuromorphic Device Applications\|Ferroelectric Transistors for Memory and...]] | 2022 | HfO₂基FeFET综述：器件结构、工作原理、存储特性及神经形态计算应用，覆盖最新研究进展。 |
| [[Ferroelectric Transistors for Memory and Neuromorphic Computing\|Ferroelectric Transistors for Memory and...]] | 2022 | HfO₂基FeFET综述：器件结构、工作原理、存储特性、神经形态计算应用及未来挑战。 |
| [[In-memory ferroelectric differentiator\|In-memory ferroelectric differentiator]] | 2025 | 开发40x40 P(VDF-TrFE)铁电电容crossbar存内差分器。0.24 fJ/次、1 MHz、98.9%准确率、4.17 POPS/W（比V100高10000倍）。演示一阶/二阶导数、运动 |
| [[Highly-reliable ferroelectric thin-film transistors array for hardware implementation of image classification\|Highly-reliable ferroelectric thin-film ...]] | 2025 | 研究问题：FeTFT在存内计算中面临弱擦除问题和界面缺陷导致的可靠性下降，限制了其在神经网络硬件实现中的应用。研究方法：提出平面集成MFMIS-FeTFT结构，通过浮栅抑制弱擦除效应，简化工艺减少界面 |
| [[Ferroelectric Optoelectronic Sensor for Intelligent Flame Detection and In‑Sensor Motion Perception\|Ferroelectric Optoelectronic Sensor for ...]] | 2026 | Ga2O3/In2Se3铁电-光电传感器阵列：255 nm紫外探测率4.91x10^17 Jones，NB-IoT实时报警，CNN 96.47%火焰运动识别，ANN\ |
## 相关概念

- [[HfO2]]
- [[FeFET]]
- [[FeRAM]]
- [[ferroelectric polarization]]
- [[Wiki 目录]]
