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

| 论文                                                                                                                                                                     | 年份   | 核心发现                                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ---------------------------------------------------------------------------------------------------- |
| [[A near-threshold memristive computing-inmemory engine for edge intelligence\|A near-threshold memristive computing-in...]]                                           | 2025 | 研究问题：边缘AI硬件需要在严格的功耗约束下实现高能效和高并行性，但忆阻器存内计算和近阈值计算都面临工艺变化的挑战，限制了其可扩展性。主要方法：1）设计近阈值2T1R单元阵列，通过额外的核心晶体管放大 |
| [[Photonic edge intelligence chip for multimodal sensing, inference and learning\|Photonic edge intelligence chip for mult...]]                                        | 2025 | 本文展示光子边缘智能芯片PEIC，融合图像/光谱/RF多模态，AWG实现29 fJ/OP卷积，1.33 ns推理延迟。在药物识别、图像分类和雷达分类三种任务上的感知-计算一体化验证。          |
| [[Spectral convolutional neural network chip for in-sensor edge computing of incoherent natural light\|Spectral convolutional neural network ch...]]                   | 2025 | 研究问题：现有光学神经网络需要相干光源，限制了片上集成规模且无法直接处理自然光，导致能效较低。方法：提出光谱卷积神经网络（SCNN），通过在CMOS图像传感器上集成大规模像素对齐的光谱滤波器实现光学卷 |
| [[Deep random forest with ferroelectric analog content addressable memory\|Deep random forest with ferroelectric an...]]                                               | 2024 | 铁电模拟内容可寻址存储器实现深度随机森林加速：2FeFET单元实现分支分裂操作，相比CPU/ReRAM实现能耗降低106倍/10倍、延迟降低106倍/2.5倍。                     |
| [[Benchmarking Test-Time DNN Adaptation at Edge with Compute-In-Memory\|Benchmarking Test-Time DNN Adaptation at...]]                                                  | 2024 | ACM J. Auton. Transport. Syst.                                                                       |
| [[Adaptation in Edge Computing A Review on Design Principles and Research Challenges\|Adaptation in Edge Computing A Review on...]]                                    | 2024 | 边缘计算自适应综述：基础设施/应用/数据三维度自适应，软硬件协同设计，资源管理策略，47 次引用。                                                    |
| [[Split Federated Learning Empowered Vehicular Edge Intelligence Concept, Adaptive Design, and Future Directions\|Split Federated Learning Empowered Vehic...]]        | 2024 | 自适应分裂联邦学习赋能车辆边缘智能：动态分裂层选择、并行优化通信与计算效率，提升非独立同分布数据下模型性能，展望未来研究方向。                                      |
| [[Sub-Thermal Expansion-Engineered Ferroelectric Transistor Arrays for Scalable Edge AI Computing\|Sub-Thermal Expansion-Engineered Ferroel...]]                       | 2024 | MFMIS-FeFET阵列热膨胀工程：室温下<1pJ/跳功耗，MNIST>97%精度，验证边缘AI计算可行性。                                              |
| [[Delocalized photonic deep learning on the internet's edge\|Delocalized photonic deep learning on th...]]                                                             | 2023 | 提出 Netcast 光子深度学习：云端智能收发器流式传输权重到边缘设备，实现 40 aJ/MAC 超低能耗推理，86 km 光纤现场试验验证。                             |
| [[A 2-Transistor-2-Capacitor Ferroelectric Edge Compute-in-Memory Scheme With Disturb-Free Inference and High Endurance\|A 2-Transistor-2-Capacitor Ferroelectric...]] | 2023 | C2FeRAM 2T2C方案：无干扰存内计算、高耐久性、CIFAR-10 VGG8推理>100倍时间且精度下降<1%、相比1T1C FeRAM缓存实现4倍能效/200倍速度/3.2e5倍生命周期提升。 |
## 相关概念

- [[In-memory computing]]
- [[Neuromorphic computing]]
- [[FeFET]]
- [[Wiki 目录]]
