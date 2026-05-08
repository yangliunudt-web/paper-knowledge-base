---
title: Memristor
type: concept
tags: [概念, 基础]
aliases: [忆阻器, memristive device, memristors, RRAM, memristive network, Memristive network, resistive memory, Resistive memory, 阻变存储器]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> 忆阻器（Memristor）是记忆电阻的简称，其电阻值随流经电荷的历史而改变，是第四种基本电路元件（继电阻、电容、电感之后），在非易失存储和神经形态计算中广泛用作突触器件。

## 定义

忆阻器理论由蔡少棠（Leon Chua）于 1971 年提出，2008 年 HP 实验室首次在 TiO₂ 器件中实现物理验证。其阻变机理包括：氧空位导电细丝（VCM）、金属离子导电细丝（ECM）、界面效应等。

在神经形态计算中，忆阻器的电导值代表突触权重，通过施加编程脉冲调节电导。

## 关键特性

- **非易失性存储**：电阻状态断电保持
- **多值/模拟存储**：部分阻变可实现多电导态（>4 bit）
- **纳秒级切换速度**
- **高密度集成**：crossbar 结构支持 4F² 单元面积
- **突触可塑性模拟**：渐进电导变化天然模拟 STDP、LTP/LTD
- **主要挑战**：cycle-to-cycle 和 device-to-device 变异、 stuck-at faults、耐久性 vs 保持性权衡

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Memory devices and applications for in‑memory computing\|Memory devices and applications for in‑m...]] | 2020 | 存内计算综述：涵盖基于电荷和基于电阻的存储设备、关键计算原语（向量‑矩阵乘法、逻辑运算、随机计算）及其在科学计算、机器学习等领域的应用，探讨器件与阵列层面的挑战与前景。 |
| [[Reservoir Computing System with Diverse Input Patterns in HfAlO-Based Ferroelectric Memristor\|Reservoir Computing System with Diverse ...]] | 2024 | 实现基于 Al 掺杂 HfO 铁电忆阻器的储备池计算系统，演示可处理多种输入脉冲类型的鲁棒储备池层，模拟生物突触短期可塑性，验证图像训练和巴甫洛夫实验等应用。 |
| [[Electrochemical ohmic memristors for Electrochemical oh\|Electrochemical ohmic memristors for Ele...]] | 2024 | 本文提出电化学欧姆忆阻器，利用电化学机制实现可靠阻变切换和欧姆行为，面向神经形态计算应用。 |
| [[A near-threshold memristive computing-inmemory engine for edge intelligence\|A near-threshold memristive computing-in...]] | 2025 | 近阈值忆阻存内计算引擎：亚阈值区crossbar操作，超低功耗边缘智能。 |
| [[Van der Waals Engineering of One-Transistor-One-Ferroelectric-Memristor Architecture for an Energy-Efficient Neuromorphic Array\|Van der Waals Engineering of One-Transis...]] | 2025 | 本文展示了全范德华组装的1T1M架构，CuCrP2S6/MoS2/h-BN堆叠。器件实现120 fA漏电流、10^6阻态可调性、12 fW功耗、<1V操作电压。神经形态阵列串扰降低2个数量级，256x |
| [[Large-scale crossbar arrays based on threeterminal MoS2 memtransistors\|Large-scale crossbar arrays based on thr...]] | 2025 | 大规模MoS2记忆晶体管交叉阵列：每阵列2048器件，良率>92%，写入能量~0.2 fJ，读取裕度10⁵，保持>3年，栅极调制解决推理模糊性，MNIST分类验证，性能优于其他2D材料架构。 |
| [[A memristor‑based unified PUF and TRNG chip with a concealable ability for advanced edge security\|A memristor‑based unified PUF and TRNG c...]] | 2025 | 基于 28 nm 嵌入式忆阻器的统一 PUF/TRNG 芯片：利用 FORMING 条件变异和读取电流变异作为熵源，设计紧凑熵提取器实现 41.7 Mbps 吞吐量，隐蔽方法防止数据泄露，认证吞吐量比 |
| [[Zn2+ Engineered Low-Barrier LiNbO3 Enables Visible-Light Programmable Ferroelectric Memristors for Noise-Immune Neuromorphic Vision\|Zn2+ Engineered Low-Barrier LiNbO3 Enabl...]] | 2026 | Zn2+掺杂LiNbO3降低铁电极化翻转能垒69%，实现可见光编程铁电忆阻器，10^8次循环耐久性，光学储备池计算在噪声MNIST上达98.6%识别率。 |
| [[Neuro-Inspired Computing With Emerging Nonvolatile Memory\|Neuro-Inspired Computing With Emerging N...]] | 2018 | 综述新兴非易失性存储器件在神经启发式计算中的应用：涵盖相变/阻变/铁电存储器等突触器件、交叉阵列架构、器件‑电路‑算法协同设计，展望定制化学习算法。 |
| [[Combinatorial optimization by weight annealing in memristive hopfeld networks\|Combinatorial optimization by weight ann...]] | 2021 | 本文提出权重退火方法用于忆阻器Hopfield网络的组合优化。初始权重为零使网络快速进入全局最小，逐渐引入权重保持基态。在TiO2 crossbar和eFlash阵列上实验验证了图划分和最大独立集问题 |
| [[In-Memory Learning With Analog Resistive Switching Memory A Review and Perspective\|In-Memory Learning With Analog Resistive...]] | 2021 | 模拟RRAM存内学习综述：器件特性、硬件算法、阵列映射和架构设计，从器件到系统的挑战。 |
| [[Enabling Energy-Efficient Deployment of Large Language Models on Memristor Crossbar A Synergy of Large and Small\|Enabling Energy-Efficient Deployment of ...]] | 2024 | 忆阻器交叉阵列大语言模型能效部署：提出新架构解决模型规模、非常权重稳态乘法、非线性操作三大挑战，BERT_Large测试精度损失可忽略，面积开销改善39倍，能耗改善18倍，面积-延迟积降低68倍。 |
## 相关概念

- [[RRAM]]
- [[ReRAM]]
- [[crossbar]]
- [[Neuromorphic computing]]
- [[In-memory computing]]
- [[selector]]
- [[Wiki 目录]]
