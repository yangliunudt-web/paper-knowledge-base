---
title: "NVM-CIM-TTA 文献分类索引"
date: 2026-04-29
tags: [文献索引, NVM, CIM, TTA, RRAM, PCM, FeFET, 存内计算]
source: "Benchmarking Test-Time DNN Adaptation at Edge with CIM — Section 2.3 & 3.3"
aliases: ["TTA文献索引", "NVM-TTA文献地图"]
---

# NVM-CIM-TTA 文献分类索引

> 来源：Fan et al., *Benchmarking Test-Time DNN Adaptation at Edge with Compute-In-Memory*, ACM J. Auton. Transport. Syst., 2024.
> 共 23 篇已下载 PDF，按**器件**和**架构**双维度分类。

---

## 一、按器件分类

### 1.1 RRAM (Resistive RAM) — 7 篇

#### 器件基础

| 论文                                                                   | 年份   | 期刊/会议      | PDF                                      |
| -------------------------------------------------------------------- | ---- | ---------- | ---------------------------------------- |
| Wong et al. — Metal-Oxide RRAM (综述)                                  | 2012 | Proc. IEEE | [[RRAM/Wong_2012_RRAM_ProcIEEE.pdf]]     |
| Ielmini — Universal Set/Reset Characteristics of Bipolar RRAM (物理模型) | 2011 | IEEE TED   | [[RRAM/Ielmini_2011_RRAM_Model_TED.pdf]] |
| Jiang et al. — Compact Model for Metal-Oxide RRAM (紧凑模型)             | 2016 | IEEE TED   | [[RRAM/Jiang_2016_RRAM_Compact_TED.pdf]] |

#### CIM 宏单元与系统

| 论文                                                                              | 年份   | 会议           | PDF                                         |
| ------------------------------------------------------------------------------- | ---- | ------------ | ------------------------------------------- |
| Spetalnick et al. — 40nm 64Kb RRAM Binary CIM Macro (Paper 16.2)                | 2022 | ISSCC        | [[RRAM/Spetalnick_2022_RRAM_CIM_ISSCC.pdf]] |
| Chang et al. — 40nm 60.64TOPS/W ECC RRAM/SRAM CIM System (Paper 16.3)           | 2022 | ISSCC        | [[RRAM/Chang_2022_RRAM_SRAM_CIM_ISSCC.pdf]] |
| Chang et al. — Heterogeneous RRAM In-Memory & SRAM Near-Memory SoC              | 2023 | ISSCC        | [[RRAM/Chang_2023_RRAM_SoC_ISSCC.pdf]]      |
| Sebastian et al. — Memory Devices and Applications for In-Memory Computing (综述) | 2020 | Nature Nano. | [[RRAM/Sebastian_2020_NatureNano.pdf]]      |

> 缺失：Wan et al. 2022 RRAM-ECC (NVMW Workshop，无正式出版)

### 1.2 FeFET (Ferroelectric FET) — 3 篇

| 论文 | 年份 | 会议 | PDF |
|------|------|------|-----|
| Shou et al. — SEE-MCAM: Scalable Multi-bit FeFET CAM | 2023 | ICCAD | [[FeFET/Shou_2023_SEE_MCAM_ICCAD.pdf]] |
| Liu et al. — COSIME: FeFET Associative Memory for Cosine Similarity Search | 2022 | ICCAD | [[FeFET/Liu_2022_COSIME_FeFET_ICCAD.pdf]] |
| Barkam et al. — HDGIM: Hyperdimensional Genome Matching on Unreliable FeFET | 2023 | DATE | [[FeFET/Barkam_2023_HDGIM_FeFET_DATE.pdf]] |

### 1.3 PCM (Phase-Change Memory) — 4 篇

| 论文 | 年份 | 期刊/会议 | PDF |
|------|------|----------|-----|
| Le Gallo & Sebastian — PCM Device Physics Overview (综述) | 2020 | J. Phys. D | [[PCM/LeGallo_2020_PCM_Overview.pdf]] |
| Ielmini & Zhang — Subthreshold Conduction & Threshold Switching in Chalcogenide Memory (物理模型) | 2007 | J. Appl. Phys. | [[PCM/Ielmini_2007_PCM_Model_JAP.pdf]] |
| Bertuletti et al. — Multilayer Neural Accelerator with Binary Activations Based on PCM | 2023 | IEEE TED | [[PCM/Bertuletti_2023_PCM_TED.pdf]] |
| Antolini et al. — Combined HW/SW Drift & Variability Mitigation for PCM Analog IMC | 2023 | IEEE JETCAS | [[PCM/Antolini_2023_PCM_JETCAS.pdf]] |

---

## 二、按架构/方法论分类

### 2.1 CIM 基准测试框架 — 7 篇

| 论文                                                                              | 年份   | 期刊/会议      | 关键贡献            | PDF                                                        |
| ------------------------------------------------------------------------------- | ---- | ---------- | --------------- | ---------------------------------------------------------- |
| Chen et al. — NeuroSim+: Device-to-Algorithm Benchmarking                       | 2017 | IEDM       | 突触器件与阵列架构基准测试   | [[CIM_Benchmarking/Chen_2017_NeuroSim_IEDM.pdf]]           |
| Peng et al. — DNN+NeuroSim: CIM Accelerators with Versatile Device Technologies | 2019 | IEDM       | 多器件技术 CIM 加速器框架 | [[CIM_Benchmarking/Peng_2019_DNN_NeuroSim_IEDM.pdf]]       |
| Peng et al. — DNN+NeuroSim V2.0: On-Chip Training                               | 2020 | IEEE TCAD  | 片上训练 CIM 端到端框架  | [[CIM_Benchmarking/Peng_2020_DNN_NeuroSim_TCAD.pdf]]       |
| Lu et al. — NeuroSim Validation with 40nm RRAM CIM Macro                        | 2021 | AICAS      | 40nm RRAM 芯片验证  | [[CIM_Benchmarking/Lu_2021_NeuroSim_Validation_AICAS.pdf]] |
| Pentecost et al. — NVMExplorer: Cross-Stack NVM Comparisons                     | 2021 | arXiv/HPCA | NVM 跨栈比较框架      | [[CIM_Benchmarking/Pentecost_2021_NVMExplorer.pdf]]        |
| Reis et al. — CIM Design Space Exploration                                      | 2020 | GLSVLSI    | CIM 建模与设计空间探索   | [[CIM_Benchmarking/Reis_2020_CIM_Benchmark_GLSVLSI.pdf]]   |
| He et al. — Design Space and Memory Tech Co-Exploration for CIM ML Accelerators | 2022 | ICCAD      | 存储技术联合设计空间探索    | [[CIM_Benchmarking/He_2022_DesignSpace_ICCAD.pdf]]         |

### 2.2 CIM 加速器架构 — 2 篇

| 论文                                                                                  | 年份   | 期刊/会议 | 关键贡献                               | PDF                                                     |
| ----------------------------------------------------------------------------------- | ---- | ----- | ---------------------------------- | ------------------------------------------------------- |
| Shafiee et al. — ISAAC: CNN Accelerator with In-Situ Analog Arithmetic in Crossbars | 2016 | ISCA  | 流水线化 ReRAM crossbar 架构，14.8× 吞吐量提升 | [[CIM_Benchmarking/Shafiee_2016_ISAAC_ISCA.pdf]]        |
| Peng et al. — Optimizing Weight Mapping & Data Flow for CNN on RRAM PIM             | 2019 | ISCAS | 权重映射与数据流优化，65% 延迟/能耗节省             | [[CIM_Benchmarking/Peng_2019_Weight_Mapping_ISCAS.pdf]] |

### 2.3 FeFET 关联存储与加速 — 2 篇

| 论文 | 年份 | 会议 | 关键贡献 | PDF |
|------|------|------|---------|-----|
| Shou et al. — SEE-MCAM: Multi-bit FeFET CAM | 2023 | ICCAD | 可扩展 FeFET 内容可寻址存储器 | [[FeFET/Shou_2023_SEE_MCAM_ICCAD.pdf]] |
| Liu et al. — COSIME: FeFET Cosine Similarity Search | 2022 | ICCAD | FeFET 关联存储用于余弦相似度检索 | [[FeFET/Liu_2022_COSIME_FeFET_ICCAD.pdf]] |

### 2.4 混合存储 CIM 系统 — 2 篇

| 论文 | 年份 | 会议 | 关键贡献 | PDF |
|------|------|------|---------|-----|
| Chang et al. — ECC RRAM/SRAM CIM + Cortex M3 | 2022 | ISSCC | 60.64TOPS/W 混合存储推荐系统 | [[RRAM/Chang_2022_RRAM_SRAM_CIM_ISSCC.pdf]] |
| Chang et al. — Heterogeneous RRAM In-Memory + SRAM Near-Memory SoC | 2023 | ISSCC | 73.53TOPS/W 异构目标跟踪 | [[RRAM/Chang_2023_RRAM_SoC_ISSCC.pdf]] |

### 2.5 NVM 器件建模与物理 — 4 篇

| 论文 | 年份 | 期刊 | 器件 | PDF |
|------|------|------|------|-----|
| Wong et al. — Metal-Oxide RRAM | 2012 | Proc. IEEE | RRAM | [[RRAM/Wong_2012_RRAM_ProcIEEE.pdf]] |
| Ielmini — Bipolar RRAM Model | 2011 | IEEE TED | RRAM | [[RRAM/Ielmini_2011_RRAM_Model_TED.pdf]] |
| Jiang et al. — Compact RRAM Model | 2016 | IEEE TED | RRAM | [[RRAM/Jiang_2016_RRAM_Compact_TED.pdf]] |
| Le Gallo & Sebastian — PCM Device Physics | 2020 | J. Phys. D | PCM | [[PCM/LeGallo_2020_PCM_Overview.pdf]] |
| Ielmini & Zhang — Chalcogenide Threshold Switching | 2007 | J. Appl. Phys. | PCM | [[PCM/Ielmini_2007_PCM_Model_JAP.pdf]] |

---

## 三、TTA 方法论分类（Fan et al. 2024 提出的三维度）

| 方法维度              | 核心思想                                                        | 相关文献                                                          |
| ----------------- | ----------------------------------------------------------- | ------------------------------------------------------------- |
| **全部/局部微调**       | 仅调整部分 block，冻结其余参数；浅层适应输入偏移，深层适应输出偏移                        | 本文提出，NeuroSim 框架验证                                            |
| **混合架构组合**        | 可适应层 → SRAM（快写），冻结层 → RRAM（密度高、快读）；cell type 成为逐层设计变量       | Chang ISSCC 2022/2023, Spetalnick ISSCC 2022                  |
| **流水线化 + 非理想性适应** | 局部微调实现 batch 间流水线（CPI≈2 vs. 全微调 CPI=6）；TTA 同时修复环境偏移和 NVM 噪声 | Shafiee ISCA 2016 (ISAAC 流水线), Antolini JETCAS 2023 (PCM 变异性) |

---

## 四、文献关系图

```
器件层         架构层               应用层
─────────────────────────────────────────────
RRAM ──────┬─ NeuroSim 框架 ────── TTA Benchmarking
           ├─ ISAAC 加速器
           ├─ 混合 SRAM/RRAM CIM
           └─ RRAM 紧凑模型

FeFET ─────── FeFET CAM ────────── 关联搜索/基因组匹配
           └─ COSIME 余弦相似度

PCM  ─────── PCM 神经加速器 ───── TTA 漂移/变异性缓解
           └─ PCM 器件物理
```

> 不可下载：Wan et al. 2022 RRAM-ECC (NVMW Workshop)、Ielmini & Wong 2018 (书籍章节)
