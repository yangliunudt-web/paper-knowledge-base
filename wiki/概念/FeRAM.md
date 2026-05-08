---
title: FeRAM
type: concept
tags: [概念, 基础]
aliases: [FRAM, ferroelectric RAM, 铁电随机存储器, ferroelectric memory, 铁电存储器]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> FeRAM（Ferroelectric Random Access Memory）是利用铁电材料的极化翻转实现非易失存储的存储器技术，是最早商业化的铁电存储技术，涵盖 1T1C（类似 DRAM）、1T（FeFET）和 FTJ 等结构。

## 定义

传统 FeRAM 采用 1T1C 结构，铁电电容器（通常 PZT）与访问晶体管串联。写入时在位线和板线间施加电压极化铁电层；读取时检测位线电荷变化（破坏性读取，需回写）。

FeFET 基 FeRAM 将铁电栅介质直接集成到晶体管中，实现 1T 单元（无单独电容器），支持非破坏性读取。

## 关键特性

- **快速写入**：纳秒级极化翻转
- **低功耗**：电场驱动极化，无直流电流
- **非破坏性读取**（FeFET）：读取电流而非电荷
- **HfO₂ 基 FeRAM**：CMOS 兼容，可缩放到先进节点
- **vs DRAM**：非易失但密度低；**vs Flash**：更快但成本高
- **主要挑战**：疲劳导致的耐久性限制、存储窗口缩小、保持性退化

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| | | |

## 相关概念

- [[FeFET]]
- [[Ferroelectric]]
- [[HfO2]]
- [[In-memory computing]]
- [[Wiki 目录]]
