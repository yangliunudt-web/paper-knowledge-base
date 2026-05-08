---
title: Edge computing
type: concept
tags: [概念, 基础]
aliases: [边缘计算, Edge AI, edge intelligence, 边缘智能, 边缘AI, TinyML]
created: 2026-05-08
updated: 2026-05-08
sources: []
confidence: high
---

> 边缘计算将计算和数据存储从云端推向数据源附近的网络边缘设备，减少延迟、带宽占用和隐私风险。存内计算和神经形态硬件是实现超低功耗边缘 AI 的核心使能技术。

## 定义

边缘计算的核心思想是"数据在哪里产生就在哪里处理"，规避将数据全部上传云端处理的延迟和带宽瓶颈。边缘 AI 进一步要求在资源极度受限的设备（MCU、传感器节点）上运行 ML 推理甚至在线学习。

## 关键特性

- **低延迟**：本地推理无需网络往返（<1 ms vs 云 100 ms+）
- **隐私保护**：数据不离开设备，降低隐私/安全风险
- **带宽节省**：仅上传处理结果而非原始数据
- **离线运行**：在无网络环境下自主运行
- **能效严格**：通常 <1 mW 功耗预算，需存内计算/SNN 等新型硬件
- **主要挑战**：模型压缩 vs 精度权衡、器件非理想性、在线学习可靠性、异构硬件适配

## 相关论文

| 论文 | 年份 | 核心发现 |
|------|------|----------|
| [[Edge Computing Vision and Challenges|Edge Computing Vision and Challenges]] | 2016 | 边缘计算综述：定义、案例（云卸载、智能家居/城市、协同边缘）、挑战与机遇（可编程性、命名、数据抽象、服务管理、隐私安全、优化指标）。 |
| [[Adaptive edge intelligence for rapid structural condition assessment using a wireless smart sensor network|Adaptive edge intelligence for rapid structur...]] | 2020 | 提出自适应边缘智能策略用于结构状态评估，集成无参考位移估计、高斯过程回归和随机过程控制，通过单节点独立计算和多节点协调处理有限资源，在铁路桥梁监测中验证有效性。 |
| [[MCUNet Tiny Deep Learning on IoT Devices|MCUNet Tiny Deep Learning on IoT Devices]] | 2020 | 提出 MCUNet 框架，联合设计 TinyNAS 神经架构搜索和 TinyEngine 轻量推理引擎，首次在商用 MCU 上实现 >70% ImageNet |
| [[TinyTL Reduce Memory, Not Parameters for Efficient On-Device Learning|TinyTL Reduce Memory, Not Parameters for Effi...]] | 2020 | 提出 TinyTL 冻结权重仅学习偏置模块，引入轻量残差模块保持适应能力，实现内存节省高达 6.5 倍（对比全网络微调）或 7.3‑12.9 倍（结合特征... |
| [[TinyOL TinyML with Online-Learning on Microcontrollers|TinyOL TinyML with Online-Learning on Microco...]] | 2021 | 微控制器在线学习 TinyOL：轻量级持续学习，特征提取+分类器更新，边缘设备自适应。 |
| [[On-Device Training Under 256KB Memory|On-Device Training Under 256KB Memory]] | 2022 | 算法-系统协同设计：QAS 稳定 8 位量化训练、稀疏更新减少内存占用、TTE 轻量引擎实现 256KB 内存训练，精度匹配云端，内存仅 PyTorch |
| [[A 2-Transistor-2-Capacitor Ferroelectric Edge Compute-in-Memory Scheme With Disturb-Free Inference and High Endurance|A 2-Transistor-2-Capacitor Ferroelectric Edge...]] | 2023 | C2FeRAM 2T2C方案：无干扰存内计算、高耐久性、CIFAR-10 VGG8推理>100倍时间且精度下降<1%、相比1T1C FeRAM缓存实现4倍... |
| [[Delocalized photonic deep learning on the internet's edge|Delocalized photonic deep learning on the int...]] | 2023 | 提出 Netcast 光子深度学习：云端智能收发器流式传输权重到边缘设备，实现 40 aJ/MAC 超低能耗推理，86 km 光纤现场试验验证。 |
| [[Adaptation in Edge Computing A Review on Design Principles and Research Challenges|Adaptation in Edge Computing A Review on Desi...]] | 2024 | 边缘计算自适应综述：基础设施/应用/数据三维度自适应，软硬件协同设计，资源管理策略，47 次引用。 |
| [[Benchmarking Test-Time DNN Adaptation at Edge with Compute-In-Memory|Benchmarking Test-Time DNN Adaptation at Edge...]] | 2024 | 本研究提出了一个基准测试框架，用于评估在配备CIM硬件的受限边缘设备上测试时DNN适应技术。研究发现：（1）部分网络适应往往优于全网络适应；（2）CIM设... |
| [[Deep Random Forest with Ferroelectric Analog Content Addressable Memory|Deep Random Forest with Ferroelectric Analog ...]] | 2024 | FeFET 模拟 CAM 深度随机森林：多级 V_TH 存储、1×16 阵列演示、边缘计算决策树。 |
| [[Deep random forest with ferroelectric analog content addressable memory|Deep random forest with ferroelectric analog ...]] | 2024 | 铁电模拟内容可寻址存储器实现深度随机森林加速：2FeFET单元实现分支分裂操作，相比CPU/ReRAM实现能耗降低106倍/10倍、延迟降低106倍/2.5倍。 |

## 相关概念

- [[In-memory computing]]
- [[Neuromorphic computing]]
- [[FeFET]]
- [[Wiki 目录]]
