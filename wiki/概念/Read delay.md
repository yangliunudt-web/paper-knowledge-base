---
title: Read delay
type: concept
tags: [概念, 进阶]
aliases: [读取延迟, read latency, 读取延时, sense delay, 读出时间]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: medium
---

> Read delay 是存储器从施加读取信号到输出稳定数据的时间间隔，在存内计算中是决定推理延迟和系统吞吐量的关键时序参数。

## 定义

读取延迟由多个因素贡献：字线/位线 RC 延迟、sense amplifier 建立时间、ADC 转换时间（模拟 IMC 中）、地址解码时间。在 FeFET/RRAM 等新兴存储器中，读取延迟与读取电压（read voltage）存在权衡——更高电压加快读取但可能引起 read disturb。

## 关键特性

- **影响因素**：阵列规模（IR drop）、selector 的导通速度、互连线 RC、sense margin
- **FeFET**：栅极读取，本质上比电荷型读取（DRAM/FeRAM 1T1C）快
- **Crossbar IMC**：一次 MVM 在一个读取周期内完成，延迟优势显著
- **Read disturb 制约**：读取电压不能无限增大，否则会在非目标单元引起意外极化翻转（FeFET）或阻变（RRAM）
- **vs Write delay**：读取通常远快于写入（ns 级 vs µs 级）

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| | | |

## 相关概念

- [[In-memory computing]]
- [[crossbar]]
- [[FeFET]]
- [[RRAM]]
- [[Wiki 目录]]
