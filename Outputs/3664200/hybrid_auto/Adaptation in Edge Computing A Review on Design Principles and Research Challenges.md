---
title: "Adaptation in Edge Computing: A Review on Design Principles and Research Challenges"
date: "2024-09-30"
year: "2024"
journal: "ACM Computing Surveys"
doi: "10.1145/3664200"
abstract: "Reviews adaptation mechanisms in edge computing, presenting a comprehensive"
abstract_cn: "综述边缘计算中的自适应机制，提出设计原则、使能技术和应用场景的综合分类法。解决资源受限边缘环境的挑战，包括有限计算能力、存储和能源供应。讨论软硬件协同设计方法、动态资源管理策略和边缘机器学习部署。分析三个维度的自适应技术：基础设施自适应、应用自适应和数据自适应。识别开放研究挑战，包括自适应边缘计算系统中的安全性、隐私和可持续性。"
keywords:
  - "[[Edge computing]]"
cite: "[1] Golpayegani F, Chen N X, Afraz N, et al. Adaptation in edge computing:"
aiSum: "边缘计算自适应综述：基础设施/应用/数据三维度自适应，软硬件协同设计，资源管理策略，47 次引用。"
confidence: "medium"
wiki_concepts:
  - "[[Edge computing]]"
authors:
  - "NANXI CHEN"
  - "Information Technology Chinese Academy of Sciences"
---

SURVEY

# Adaptation in Edge Computing: A Review on Design Principles and Research Challenges

FATEMEH GOLPAYEGANI, University College Dublin, Dublin, Leinster, Ireland

NANXI CHEN, Shanghai Institute of Microsystem and Information Technology Chinese Academy of Sciences, Shanghai, Shanghai, China

NIMA AFRAZ, University College Dublin, Dublin, Leinster, Ireland

ERIC GYAMFI, University College Dublin, Dublin, Leinster, Ireland

ABDOLLAH MALEKJAFARIAN, University College Dublin, Dublin, Leinster, Ireland

DOMINIK SCHÄFER

View all

Open Access Support provided by:

University College Dublin

Shanghai Institute of Microsystem and Information Technology

Chinese Academy of Sciences

University of Hohenheim

![](images/fee87f97694c97483b8f7fbeea6eba8cb1ed2970294dbf68736ec526f22bece1.jpg)

PDF Download

3664200.pdf

31 December 2025

Total Citations: 47

Total Downloads:

5148

Published: 30 September 2024

Online AM: 09 May 2024

Accepted: 23 April 2024

Revised: 29 February 2024

Received: 25 January 2023

Citation in BibTeX format

# Adaptation in Edge Computing: A Review on Design Principles and Research Challenges

FATENEH GOLPAYEGANI, School of Computer Science, University College Dublin, Dublin, Ireland NANXI CHEN, Shanghai Institute of Microsystem and Information Technology, Chinese Academy of Sciences, Shanghai, China and University of Chinese Academy of Sciences, Beijing, China NIMA AFRAZ and ERIC GYAMFI, School of Computer Science, University College Dublin, Dublin, Ireland

ABDOLLAH MALEKJAFARIAN, School of Civil Engineering, University College Dublin, Dublin, Ireland DOMINIK SCHÄFER, Syntax Systems GmbH & Co., Weinheim, Germany

CHRISTIAN KRUPITZER, Department of Food Informatics and Computational Science Lab, University of Hohenheim, Stutgart, Germany

Edge computing places the computational services and resources closer to the user proximity, to reduce latency, and ensure the quality of service and experience. Low latency, context awareness and mobility support are the major contributors to edge-enabled smart systems. Such systems require handling new situations and change on the fy and ensuring the quality of service while only having access to constrained computation and communication resources and operating in mobile, dynamic and ever-changing environments. Hence, adaptation and self-organisation are crucial for such systems to maintain their performance, and operability while accommodating new changes in their environment.

Tis article reviews the current literature in the feld of adaptive edge computing systems. We use a widely accepted taxonomy, which describes the important aspects of adaptive behaviour implementation in computing systems. Tis taxonomy discusses aspects such as adaptation reasons, the various levels an adaptation strategy can be implemented, the time of reaction to a change, categories of adaptation technique and control of the adaptive behaviour. In this article, we discuss how these aspects are addressed in the literature and identify the open research challenges and future direction in adaptive edge computing systems.

Te results of our analysis show that most of the identifed approaches target adaptation at the application level, and only a few focus on middleware, communication infrastructure and context. Adaptations that are required to address the changes in the context, changes caused by users or in the system itself are also less explored. Furthermore, most of the literature has opted for reactive adaptation, although proactive adaptation
