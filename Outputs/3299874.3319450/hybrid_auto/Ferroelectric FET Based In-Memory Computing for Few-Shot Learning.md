---
title: "Ferroelectric FET Based In-Memory Computing for Few-Shot Learning"
authors:
  - "University Notre"
  - "Notre United"
  - "States"
date: "2019-05-09"
year: "2019"
journal: "GLSVLSI 2019"
doi: "10.1145/3299874.3319450"
abstract: "Explores ferroelectric FET (FeFET) based in-memory computing for few-shot"
abstract_cn: "探索基于铁电 FET (FeFET) 的存内计算用于小样本学习应用。提出使用 FeFET 模拟电导实现神经网络权重存储和存储器内乘法运算。利用"
keywords:
  - "[[Ferroelectric]]"
  - "[[In-memory computing]]"
cite: "[1] Laguna A F, Yin X Z, Reis D A, et al. Ferroelectric FET based in-memory"
aiSum: "FeFET 小样本学习存内计算：模拟电导权重存储，原型网络硬件实现，边缘能效推理。"
confidence: "high"
wiki_concepts:
  - "[[Ferroelectric]]"
  - "[[In-memory computing]]"
---

# Ferroelectric FET Based In-Memory Computing for Few-Shot Learning

ANN FRANCHESCA LAGUNA, University of Notre Dame, Notre Dame, IN, United States

XUNZHAO YIN, University of Notre Dame, Notre Dame, IN, United States

DAYANE ALFENAS REIS, University of Notre Dame, Notre Dame, IN, United States

MICHAEL THADDEUS NIEMIER, University of Notre Dame, Notre Dame, IN, United States

XIAOBO SHARON HU, University of Notre Dame, Notre Dame, IN, United States

Open Access Support provided by:

University of Notre Dame

![](images/e4706e50eed692cd364fb4720538ac68a600053ec0c0acf0205fe53a45d5cb37.jpg)

PDF Download

3299874.3319450.pdf

04 February 2026

Total Citations: 32

Total Downloads: 1109

Published: 13 May 2019

Citation in BibTeX format

GLSVLSI '19: Great Lakes Symposium on VLSI 2019

May 9 - 11, 2019

VA, Tysons Corner, USA

Conference Sponsors: SIGDA

# Ferroelectric FET based In-Memory Computing for Few-Shot Learning

Ann Franchesca Laguna

alaguna@nd.edu

University of Notre Dame

Indiana, USA

Xunzhao Yin

xyin1@nd.edu

University of Notre Dame

Indiana, USA

Dayane Reis

dreis@nd.edu

University of Notre Dame

Indiana, USA

Michael Niemier

mniemier@nd.edu

University of Notre Dame

Indiana, USA

X. Sharon Hu

shu@nd.edu

University of Notre Dame

Indiana, USA

# ABSTRACT

As CMOS technology advances, the performance gap between the CPU and main memory has not improved. Furthermore, the hardware deployed for Internet of Things (IoT) applications need to process ever growing volumes of data, which can further exacerbate the “memory wall”. Computing-in-memory (CiM) architectures, where logic and arithmetic operations are performed in memory, can signicantly reduce energy and latency overheads associated with data transfer, and potentially alleviate processor-memory bottlenecks. In this paper, we consider the utility of ternary content addressable memory (TCAM) arrays and CiM arrays based on ferroelectric eld e
ect transistors (FeFETs) to support emerging machine learning models that can learn new classes of data with signicantly less training overhead – highly desirable in IoT applications. Architecturally, we use TCAM and CiM arrays to implement the external memory module in a memory enhanced neural network (MENN) – which can be used to minimize catastrophic forgetting – a major problem in applications such as lifelong and few-shot learning. As a representative example, we achieve 95.14% accuracy for a few-shot learning task with the Omniglot data set by using a combined L∞ and $L _ { 1 }$ distance metric computed via a TCAM-CiM cascaded architecture (as opposed to 99.06% accuracy assuming a GPU backed by DRAM). While there is a slight drop in accuracy, the TCAM-CiM approach is 4.34X faster and 4.18X more energy e
cient than a CMOS implementation for the same task. The ability of an FeFET to serve as both a compact logic and storage element helps to enable dense CiM and TCAM structures that drive the aforementioned improvements to application-level gures of merit (FOMs).

# CCS CONCEPTS

• Computing methodologies → Online learning settings; Neural networks; • Hardware → Non-volatile memory; Arithmetic and datapath circuits.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for prot or commercial advantage and that copies bear this notice and the full citation on the rst page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specic permission and/or a fe