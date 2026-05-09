---
title: Combinatorial optimization
type: concept
tags: [概念, 进阶]
aliases: [组合优化, COP, 组合优化问题, Ising solver, QUBO, combinatorial optimization problem, discrete optimization]
created: 2026-05-09
updated: 2026-05-09
sources: []
confidence: medium
---

> 组合优化问题（COP）是在有限离散解空间中寻找使目标函数最优的解的数学问题，许多 COP 属于 NP-hard，可通过 Ising 模型/QUBO 框架映射到硬件求解器上进行加速。

## 定义

典型的组合优化问题包括：Max-Cut、图着色、旅行商问题（TSP）、顶点覆盖、最大团、最大独立集等。这些问题可被映射为 Ising 自旋模型或二次无约束二进制优化（QUBO）问题。模拟退火、量子退火和专用的硬件退火器（如 FeFET crossbar annealer）是主要求解方法。

## 关键特性

- **Ising/QUBO 映射**：将问题变量表示为自旋（±1），约束和相互作用表示为耦合矩阵
- **模拟退火**：通过逐步降低温度参数使系统跳出局部最优
- **FeFET 退火器**：利用 FeFET crossbar 阵列的并行 VMM 加速 QUBO 能量计算
- **忆阻器 Hopfield 网络**：将 COP 映射为网络能量函数，网络收敛到局部/全局最小解
- **权重退火**：在搜索过程中动态调整耦合权重，有助于避免局部最优

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Ferroelectric compute-in-memory annealer for combinatorial optimization problems\|Ferroelectric compute-in-memory annealer...]] | 2023 | FeFET交叉阵列退火器：组合优化→Ising/QUBO映射，硬件加速模拟退火，高能效COP求解。 |
| [[Combinatorial optimization by weight annealing in memristive hopfeld networks\|Combinatorial optimization by weight ann...]] | 2021 | 本文提出权重退火方法用于忆阻器Hopfield网络的组合优化。初始权重为零使网络快速进入全局最小，逐渐引入权重保持基态。在TiO2 crossbar和eFlash阵列上实验验证了图划分和最大独立集问题 |
| [[Solving the Traveling Telescope Problem with Mixed-integer Linear Programming\|Solving the Traveling Telescope Problem ...]] | 2024 | 混合整数线性规划求解旅行望远镜问题：10分钟内优化100次观测序列，转动开销降低5倍，适用于多普勒行星搜索等自动调度场景。 |
## 相关概念

- [[FeFET]]
- [[In-memory computing]]
- [[Memristor]]
- [[crossbar]]
- [[Wiki 目录]]
