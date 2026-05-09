---
title: Hippocampus
type: concept
tags: [概念, 基础]
aliases: [hippocampus, 海马体, 海马, hippocampal, CA1, CA3, dentate gyrus, 齿状回, 海马区]
created: 2026-05-10
updated: 2026-05-10
sources: []
confidence: medium
---

> 海马体是大脑中负责记忆形成、空间导航和模式分离的关键结构，其独特的解剖组织和突触可塑性机制为人工神经网络设计（特别是持续学习和吸引子网络）提供了重要启发。

## 定义

海马体包含 DG（齿状回）、CA3、CA1 等子区域，形成经典的三突触回路：内嗅皮层 → DG → CA3 → CA1。CA3 的循环连接实现模式完成（pattern completion），DG 的稀疏编码实现模式分离（pattern separation），这些机制启发了人工神经网络中的记忆巩固和持续学习架构。

## 关键特性

- **模式分离（DG）**：将相似输入映射为不重叠的表示
- **模式完成（CA3）**：从部分线索恢复完整记忆
- **BTSP 突触可塑性**：行为时间尺度突触可塑性，支持吸引子动力学
- **神经发生**：成年 DG 中持续产生新神经元，为持续学习提供生物学基础
- **双重通路**：EC→CA3 的直接和间接通路提供上下文门控机制

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Operation and plasticity of hippocampal CA3 circuits implications for memory encoding\|Operation and plasticity of hippocampal ...]] | 2022 | 海马CA3记忆印记：突触传递增强+内在兴奋性增加、NMDA受体激活必需、CREB基因表达维持、支持记忆编码与检索。 |
| [[Mechanisms of memory-supporting neuronal dynamics in hippocampal area CA3\|Mechanisms of memory-supporting neuronal...]] | 2024 | 通过膜电位记录和光遗传操作揭示 CA3 位置野活动由循环突触上的对称性 BTSP 产生，内嗅皮层输入负责更新位置细胞活动，计算模型实现吸引子动力学，理论分析表明网络具有优越的记忆存储容量。 |
| [[Resolving New Memories A Critical Look at the Dentate Gyrus, Adult Neurogenesis, and Pattern Separation\|Resolving New Memories A Critical Look a...]] | 2011 | 观点文章，提出记忆分辨率假说整合计算、电生理和行为视角，解释成年神经发生中海马齿状回新生神经元在模式分离中的功能，区分年轻神经元的广泛调谐与成熟神经元的高度特异性。 |
| [[Context-modulation of hippocampal dynamics and deep convolutional networks\|Context-modulation of hippocampal dynami...]] | 2017 | Complex architectures of biological neural circuits, such as parallel processing\ |
## 相关概念

- [[Continual learning]]
- [[Neural network]]
- [[Neuromorphic computing]]
- [[Wiki 目录]]
