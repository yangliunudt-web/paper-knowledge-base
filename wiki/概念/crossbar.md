---
title: crossbar
type: concept
tags: [概念, 基础]
aliases: [交叉阵列, crossbar array, Crossbar array, cross-point array, 交叉点阵列, memristor crossbar, crossbar array]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> Crossbar 阵列是存内计算的核心拓扑结构，由横向字线（word line）和纵向位线（bit line）交叉构成，每个交叉点放置一个存储/计算单元，利用物理定律完成矩阵向量乘法（MVM）。

## 定义

在 N×M crossbar 中，每行施加输入电压 V_i，每个交叉点电导 G_ij 代表权重，每列输出的电流 I_j = Σ V_i × G_ij（基尔霍夫定律 + 欧姆定律）天然实现 MVM。

## 关键特性

- **O(1) 复杂度 MVM**：模拟域一次并行完成 N×M MAC 运算
- **高密度**：4F² 单元面积，支持 3D 堆叠
- **非易失**：使用 FeFET/ReRAM 权重器件，断电保持
- **主要挑战**：
  - Sneak path：未选中单元的漏电流干扰输出精度
  - IR drop：互连线寄生电阻导致电压降
  - 写串扰：编程一个单元时影响相邻单元
  - 器件变异：权重精度受限于器件非理想性
- **解决方案**：1S1R（selector + RRAM）、1T1R、1FeFET1R 等接入结构

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[First demonstration of in-memory computing crossbar using multi-level Cell FeFET\|First demonstration of in-memory computi...]] | 2023 | 首次利用多级 FeFET 实现存内计算交叉阵列宏，1FeFET-1R 单元支持多位 MAC 操作，手写识别 96.6% 准确率，能效 885.4 TOPS/W。 |
| [[Ferroelectric compute-in-memory annealer for combinatorial optimization problems\|Ferroelectric compute-in-memory annealer...]] | 2023 | FeFET交叉阵列退火器：组合优化→Ising/QUBO映射，硬件加速模拟退火，高能效COP求解。 |
| [[In-memory ferroelectric differentiator\|In-memory ferroelectric differentiator]] | 2025 | 开发40x40 P(VDF-TrFE)铁电电容crossbar存内差分器。0.24 fJ/次、1 MHz、98.9%准确率、4.17 POPS/W（比V100高10000倍）。演示一阶/二阶导数、运动 |
| [[Large-scale crossbar arrays based on threeterminal MoS2 memtransistors\|Large-scale crossbar arrays based on thr...]] | 2025 | 大规模MoS2记忆晶体管交叉阵列：每阵列2048器件，良率>92%，写入能量~0.2 fJ，读取裕度10⁵，保持>3年，栅极调制解决推理模糊性，MNIST分类验证，性能优于其他2D材料架构。 |
| [[Scaling-up Resistive Synaptic Arrays for Neuro-inspired Architecture Challenges and Prospect\|Scaling-up Resistive Synaptic Arrays for...]] | 2016 | 讨论阻变突触器件交叉阵列规模扩展的挑战（器件非线性、有限精度、器件变异、IR 压降），提出差分读出消除关态电流、多单元平均减少变异、放宽线宽降低 IR |
| [[Neuro-Inspired Computing With Emerging Nonvolatile Memory\|Neuro-Inspired Computing With Emerging N...]] | 2018 | 综述新兴非易失性存储器件在神经启发式计算中的应用：涵盖相变/阻变/铁电存储器等突触器件、交叉阵列架构、器件‑电路‑算法协同设计，展望定制化学习算法。 |
| [[CODEX Stochastic Encoding Method to Relax Resistive Crossbar Accelerator Design Requirements\|CODEX Stochastic Encoding Method to Rela...]] | 2022 | 提出随机输入编码方案 CODEX，通过伯努利统计编码将位线电流分布压缩为窄高斯分布，降低 ADC 输入范围，实现 ADC 功耗降低 68.5%、面积降低 35.5%、原位训练周期数降低 25.8%。 |
## 相关概念

- [[In-memory computing]]
- [[Memristor]]
- [[RRAM]]
- [[selector]]
- [[FeFET]]
- [[Neuromorphic computing]]
- [[Wiki 目录]]
