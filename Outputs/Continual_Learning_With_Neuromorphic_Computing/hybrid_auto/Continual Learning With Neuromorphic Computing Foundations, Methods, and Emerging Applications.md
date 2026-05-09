---
title: "Continual Learning With Neuromorphic Computing: Foundations, Methods, and Emerging Applications"
authors:
  - "Mishal Fatima Minhas Rachmad Vidya Wicaksana Putra"
  - "Falah Awwad"
  - "Osman Hasan"
  - "Muhammad Shafique"
date: "2025-07-15"
year: "2025"
journal: "IEEE Access"
doi: "10.1109/ACCESS.2025.3588665"
abstract: "The challenging deployment of compute- and memory-intensive methods from"
abstract_cn: "基于深度神经网络的持续学习方法对计算和内存的高需求，突显了向更高效方法范式转变的迫切性。神经形态持续学习作为一种新兴解决方案，通过利用脉冲神经网络的原理及其固有优势（例如稀疏脉冲驱动操作和生物可塑性学习规则）来提高能效和性能，从而实现在资源受限计算系统的动态变化环境中执行高效的持续学习算法（例如无监督学习方法）。"
keywords:
  - "[[Continual learning]]"
  - "[[Neuromorphic computing]]"
cite: "[1] Putra M F M R V W, Awwad F, Hasan O, et al. Continual learning with neuromorphic"
aiSum: "神经形态持续学习综述：涵盖SNN原理、持续学习方法分类（正则化、回放、架构等）、优化技术、应用案例（自适应机器人、自动驾驶），以及能效与性能权衡分析。"
confidence: "medium"
wiki_concepts:
  - "[[Continual learning]]"
  - "[[Neuromorphic computing]]"
---

# TOPICAL REVIEW

# Continual Learning With Neuromorphic Computing: Foundations, Methods, and Emerging Applications

MISHAL FATIMA MINHAS RACHMAD VIDYA WICAKSANA PUTRA 2, (Member, IEEE), FALAH AWWAD 1 , (Senior Member, IEEE), OSMAN HASAN3, (Senior Member, IEEE), AND MUHAMMAD SHAFIQUE 2, (Senior Member, IEEE)

1Electrical and Communication Engineering Department, United Arab Emirates University (UAEU), Al Ain, United Arab Emirates   
2eBRAIN Laboratory, New York University (NYU) Abu Dhabi, Abu Dhabi, United Arab Emirates   
3School of Electrical Engineering and Computer Science (SEECS), National University of Sciences and Technology (NUST), Islamabad 44000, Pakistan

Corresponding author: Falah Awwad (f_awwad@uaeu.ac.ae)

This work was supported in part by United Arab Emirates University (UPAR) under Grant 12N169; and in part by the New York University Abu Dhabi (NYUAD) Center for Artificial Intelligence and Robotics (CAIR), funded by Tamkeen under NYUAD Research Institute under Award CG010.

ABSTRACT The challenging deployment of compute- and memory-intensive methods from Deep Neural Network (DNN)-based Continual Learning (CL), underscores the critical need for a paradigm shift towards more efficient approaches. Neuromorphic Continual Learning (NCL) appears as an emerging solution, by leveraging the principles of Spiking Neural Networks (SNNs) and their inherent advantages (e.g., sparse spike-driven operations and bio-plausible learning rules) for improving energy efficiency and performance, thereby enabling efficient CL algorithms (e.g., unsupervised learning approach) executed in dynamically-changed environments with resource-constrained computing systems. Though in its early stages, NCL is already a major research field with an increasing interest in novel SNN-based techniques for different CL methods (e.g., regularization-, replay-, and architecture-based). Motivated by the need for a holistic study of NCL, in this survey, we first provide a detailed background on CL, encompassing the desiderata, settings, metrics, scenario taxonomy, Online Continual Learning (OCL) paradigm, recent DNN-based methods proposed in the literature to address catastrophic forgetting (CF). Then, we analyze these methods based on their achieved CL desiderata, computational and memory costs, as well as network complexity, hence emphasizing the need for energy-efficient CL. After introducing the CL background and the energy efficiency challenges, we provide an extensive background of low-power neuromorphic computing systems including encoding techniques, neuronal dynamics, network architectures, learning rules, neuromorphic hardware processors, software and hardware frameworks, neuromorphic datasets, benchmarks, and evaluation metrics. Then, this survey comprehensively reviews and analyzes state-ofthe-art works in the NCL field. The key ideas, implementation frameworks, and performance assessments (including CL, OCL, neuromorphic hardware compatibility aspects) are provided. This survey also covers several hybrid approaches that combine supervised and unsupervised learning paradigms and categorizes them into three main classes. It also covers optimization techniques including SNN operations reduction, weight quantization, and knowledge distillation. Then, this survey covers the progress of real-world NCL applications categorized into adaptive robots and autonomous vehicles with a wide range of use-cases i.e., object recognition, robotic arm control, cars and road lane detection, Simultaneous Localization and Mapping

The associate editor coordinating the review of this manuscript and D approving it for publication was Wei Wei

(SLAM), people detection and robotic navigation and provides their specific case-studies with empirical results. Finally, this paper provides a future perspective on the open research challenges for NCL, since the purpose of this study is to be useful for the wider neuromorphic AI research community and to inspire future research in bioplausible OCL.

INDEX TERMS Continual learning (CL), neuromorphic computing, spiking neural networks (SNNs), neuromorphic continual learning (NCL), event-based processing, energy efficiency, online continual learning (OCL), catastrophic forgetting (CF), deep neural networks (DNNs), artificial intelligence (AI), embedded AI systems.

# I. INTRODUCTION

The inherent cognitive flexibility of the human brain allows continuous learning from environmental interactions throughout life, exhibiting a remarkable ability to simultaneously acquire and retain multiple skills [1]. For instance, a person fluent in English can also develop proficiency in Spanish and French, each with unique grammatical structures and vocabulary, without losing proficiency in their native language. This ability is rooted in the brains’ delicate balance between plasticity and stability [2], [3]. Plasticity allows for the acquisition of new skills, while stability ensures that existing knowledge is preserved. Naturally, we expect Artificial Intelligence (AI) systems [4], [5], [6], wielding Neural Network (NN) algorithms [7], to develop a similar learning capability to effectively operate and adapt in real-world scenarios. While state-of-the-art AI systems excel in single task-based static environments, such as image recognition [8], face identification [9], and speech recognition [10], they often struggle in dynamic environments where data or tasks may change in structure, distribution, or characteristics over time. For instance, when a new task is encountered after a resource-intensive training, NNs are often retrained from scratch despite the high computational costs [11]. Therefore, robustness to multiple tasks and sequential experiences, remains a significant research challenge for AI systems. When faced with incremental learning of different tasks, most NNs underperform due to suffering from rapid performance degradation, a phenomenon known as Catastrophic Forgetting (CF) or interference [12], [13], [14].

In recent years, Continual Learning (CL) [15], [16], [17] emerges as a conceptual solution for addressing CF in AI systems. CL aims to balance the system’s ability to learn new tasks without forgetting the previous knowledge, known as the stability-plasticity dilemma [18], [19] (Fig. 1). It also seeks to achieve generalizability across tasks. In addition to avoiding CF, the primary objectives of CL also include ensuring scalability of NNs, minimizing reliance on old data, realizing controlled forgetting, and enabling rapid adaptation and recovery, which will be further discussed in Section II-B.

Numerous CL methods have been proposed to address CF in the conventional Artificial/Deep Neural Network (ANN/DNN) domain, which showed notable performance improvements [21], [22], [23], [24], [25], [26], [27]. However, most methods are resource-intensive, demanding

additional memory and computational power. Therefore, ANN-based CL methods often fail to account for storage usage during incremental training, necessitating a significant addition of memory for parameters [28]. These conditions are not suitable for embedded AI systems, that use portable-battery and need quick adaptation to new data within limited resources. However, designing resourceand energy-efficient systems with CL capabilities (i.e., CL systems) is still a major challenge.

Recently, the brain-inspired Neuromorphic Computing (NC) paradigm [29], [30], [31], [32], [33], [34] has emerged as a promising field for enabling efficient and low-power information processing and decision-making, i.e., by emulating the architecture and functionality of brains with Spiking Neural Network (SNN) algorithms [35], [36], [37], [38], [39], [40]. The event-driven nature of SNNs supports energy-efficient learning of both static and non-static data streams [35], [36], [37], [38], [39], [40]. Furthermore, SNNs can perform unsupervised learning due to their bio-plausible learning rules (e.g., Spike-Timing-Dependent Plasticity (STDP) [41]), thus enabling continuous adaptation to dynamically changing environments and efficiently learning spatio-temporal data online without labels [42], [43]. In this manner, NC aligns seamlessly with the desired characteristics (desiderata) of CL, called Neuromorphic Continual Learning (NCL).

# A. SURVEYS ON CL AND NCL

To fully understand the foundations and recent advancements in CL and NCL, a comprehensive survey is imperative, unlike other surveys that focus on a single area (either CL, NCL, bioplausible learning rules, or applications). Table 1 compares surveys studying multiple aspects of CL, NCL or SNNs, like our work. Most of the existing CL surveys [11], [16], [17], [44], [45], [46], [47], [48], [49], [50], [51], [52], [54] have particularly focused on addressing CF in DNNs. For instance, studies in [16] provided an up-to-date CL survey in DNNs. Meanwhile, other surveys focused on categorizing CL methods [44], [47], [49], [54], studying the challenges of forgetting in DNNs [11], [45], [52], reviewing computational requirements of CL (e.g., regularization) [11], discussing the benefits of forgetting in CL [52], providing experimental comparisons of 11 CL methods [45], discussing Online Continual Learning (OCL) paradigm [51], and discussing

TABLE 1. Qualitative comparison of our survey and the existing ones. Note: ’’✓’’, ’’≈’’, and ’’×’’ mean full, partial, and no consideration, respectively.   

<table><tr><td>Survey</td><td>Year</td><td>Pages (ref)</td><td>References (ref)</td><td>Scope</td><td>Taxonomy</td><td>FW/Platforms</td><td>SW Frameworks</td><td>Architectures</td><td>Benchmarks</td><td>Datasets</td><td>Metrics</td><td>Challenges</td><td>Quant. Analysis</td><td>Case Studies</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>CL</td><td>NCL</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[17]</td><td>2019</td><td>21*</td><td>207</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>[44]</td><td>2021</td><td>25</td><td>344</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>✓</td><td>✓</td></tr><tr><td>[45]</td><td>2021</td><td>18</td><td>102</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>[46]</td><td>2022</td><td>18</td><td>159</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>≈</td><td>✓</td><td>✓</td><td>≈</td><td>✓</td><td>✓</td></tr><tr><td>[47]</td><td>2022</td><td>18</td><td>124</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>✓</td><td>×</td><td>✓</td><td>✓</td><td>×</td><td>✓</td><td>✓</td></tr><tr><td>[48]</td><td>2022</td><td>32*</td><td>249</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>[49]</td><td>2022</td><td>7</td><td>113</td><td>✓</td><td>×</td><td>≈</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td></tr><tr><td>[50]</td><td>2022</td><td>6</td><td>78</td><td>×</td><td>SNNs</td><td>×</td><td>✓</td><td>✓</td><td>≈</td><td>×</td><td>≈</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>[51]</td><td>2022</td><td>30</td><td>79</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>✓</td></tr><tr><td>[52]</td><td>2023</td><td>15</td><td>281</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>≈</td></tr><tr><td>[35]</td><td>2023</td><td>11</td><td>83</td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>≈</td><td>≈</td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>✓</td></tr><tr><td>[53]</td><td>2023</td><td>18</td><td>173</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>✓</td><td>✓</td><td>×</td></tr><tr><td>[54]</td><td>2024</td><td>16</td><td>289</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>✓</td><td>✓</td></tr><tr><td>[11]</td><td>2024</td><td>13</td><td>177</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>[16]</td><td>2024</td><td>20</td><td>527</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>≈</td><td>×</td><td>✓</td><td>×</td><td>✓</td></tr><tr><td>[55]</td><td>2024</td><td>28*</td><td>66</td><td>≈</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>≈</td><td>×</td><td>✓</td><td>×</td><td>✓</td></tr><tr><td>[56]</td><td>2024</td><td>25*</td><td>304</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>[57]</td><td>2024</td><td>7</td><td>80</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>✓</td><td>≈</td><td>✓</td><td>✓</td><td>×</td></tr><tr><td>[58]</td><td>2024</td><td>17</td><td>167</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>≈</td><td>≈</td><td>✓</td><td>✓</td><td>×</td><td>✓</td><td>✓</td><td>×</td></tr><tr><td>[59]</td><td>2024</td><td>14</td><td>144</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>[60]</td><td>2025</td><td>27</td><td>233</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>This work</td><td>2025</td><td>39</td><td>413</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr></table>

* Single-column pages.

![](images/cc655769ebdd6b63938c692b2cf01c4a5a4737aa9999e2faaca5e822d06f9019.jpg)  
FIGURE 1. The key challenge of performing sequential task learning in NNs is balancing stability and plasticity of the weights. Failing to maintain this balance results in CF, leading to a significant performance decline on earlier tasks. It is illustrated by the sharp drop in accuracy on the previous ‘‘cat’’ task as the network learns a new task, such as recognizing ‘‘dog’’; adapted from studies in [20].

the importance of adopting brain-inspired data representations [53]. A more recent line of surveys have also explored CL in large pre-trained models, focusing on paradigms such as prompt tuning, adapters, and distillation for mitigating forgetting in large language models (LLMs) [56], [57], [58], [59], [60]. While these methods offer solutions for foundation models, they are fundamentally different from resource-constrained, biologically-inspired approaches like NCL for enabling energy-efficient CL and OCL, which remain underexplored in existing surveys. In particular, our survey differs from the study [16] in the following ways (see overview in Table 1 and an in-depth comparison in Table 2).

• Focus: Survey [16] focused on categorizing DNN-based CL methods, and provided theoretical concepts of stability-plasticity trade-offs, generalizability in CL, and application domains. Our survey builds on that foundation to highlight the limitations of DNN-based CL methods, i.e., computational and memory overhead for resource-constrained systems. Motivated by these challenges, it provides a specialized perspective on state-ofthe-art NCL methods, categorizing the existing literature into: 1) enhancements on unsupervised STDP learning, 2) predictive coding, 3) active dendrites, 4) bayesian continual learning, 5) architecture, 6) replay, 7) regularization and 8) hebbian learning based methods, along with optimization techniques proposed by these works, and SNN-specific application use-cases for enabling energy-efficient CL and OCL in embedded AI systems.

• Comparative Quantitative Analysis: Our survey distinguishes itself from [16] by providing a comparative quantitative analysis considering design factors (i.e., network complexity) and evaluation metrics (i.e., accuracy, memory footprint, latency, power/energy usage) of the reviewed NCL methods with relevant DNN-based CL methods. It also provides a detailed quantitative trade-off analysis (accuracy vs. efficiency) for various NCL methods. Additionally, it provides a comparison of prominent neuromorphic datasets and a comparative analysis of NCL frameworks with standard DNN-based CL frameworks, which are not provided in [16].

• Application Domains: Our survey systematically analyzes the current progress of NCL in real-world

TABLE 2. Comparison of our survey with study [16]. Note: ’’✓’’, ’’≈’’, and ’’×’’ mean full, partial, and no consideration, respectively.   

<table><tr><td>Aspect</td><td>This Work</td><td>[16]</td></tr><tr><td>Taxonomy &amp; categorization</td><td>NCL methods &amp; their real-world use-cases</td><td>CL methods</td></tr><tr><td>Neuromorphic datasets &amp; SNN-based evaluation metrics</td><td>✓</td><td>×</td></tr><tr><td>SNN-based CL, OCL capability, &amp; hardware compatibility</td><td>✓</td><td>×</td></tr><tr><td>Hardware deployment constraints</td><td>✓</td><td>≈</td></tr><tr><td>Quantitative trade-off analysis</td><td>✓</td><td>×</td></tr><tr><td>Comparative analysis of NCL frameworks with standard DNN-based CL frameworks</td><td>✓</td><td>×</td></tr><tr><td>Comparative quantitative analysis of NCL methods with DNN-based CL methods</td><td>✓</td><td>×</td></tr></table>

applications by categorizing existing works into: 1) adaptive robots, and 2) autonomous vehicles/agents. It provides specific case studies with empirical results (latency, power/energy, accuracy), and OCL capability assessment, to demonstrate the real-world feasibility of NCL in embedded AI systems. Furthermore, it reports the datasets, learning rules, software/hardware platforms, and discusses hardware deployment challenges. These aspects are not covered by [16] survey, as it mainly focuses on the scenario complexity and task-specific challenges.

The remarkable CL capability of humans has sparked interest in the emerging of NCL paradigm, i.e., investigation on how SNN architectures and learning rules can be utilized to develop efficient CL systems. For instance, studies in [35] explored biological mechanisms for NCL and emphasized the importance of CL, but did not provide a comparative quantitative analysis of the reviewed NCL methods with relevant DNN-based CL methods. It also did not provide details of neuromorphic datasets or a taxonomy that categorizes the recent literature on NCL methods and SNN-specific real-world application use-cases. The other survey [55] provided the background theories on sparse and predictive coding and their relation to Hebbian and bio-plausible learning, hence it only focused on learning rules and application aspect of NCL. It did not cover the aspects such as OCL capability, software and hardware frameworks, hardware compatibility, neuromorphic datasets & benchmarks, performance and computational efficiency trade-offs of existing NCL works. Therefore, a unified survey that covers the foundations of CL, recent advances in both the DNN and SNN domains, provides a comparative and application-driven view of NCL with detailed NCL design and optimization aspects, assessing suitability for OCL and neuromorphic hardware compatibility, has not been provided.

# B. SCOPE AND CONTRIBUTION

# Our survey addresses the following key questions.

Q1: What are the CL desiderata, settings, evaluation metrics, and taxonomy of scenarios?

Q2: What are the different categories of existing CL methods in the ANN/DNN domain, how they overcome CF, and their achieved desiderata?   
Q3: What are the deployment challenges of these CL methods (i.e., computational/memory overhead) that necessitate energy-efficient approaches?   
Q4: What is the technical background of low-power neuromorphic systems, current software and hardware frameworks/platforms, datasets, benchmarks and evaluation metrics?   
Q5: How do neuromorphic frameworks compare with standard deep learning (DL) and CL frameworks?   
Q6: What methods do the state-of-the-art propose to enable energy-efficient CL with SNNs (i.e., NCL), their OCL capability, and which efficiency enhancement techniques they propose?   
Q7: What is the compatibility of reviewed methods with neuromorphic hardware platforms, and their on-chip learning capabilities?   
Q8: Is there a standardized evaluation framework or metrics for benchmarking NCL and what additional metrics can be used for evaluating NCL methods?   
Q9: What are the hardware deployment challenges of NCL methods considering accuracy-efficiency trade-offs?   
Q10: What are the specific use-cases in adaptive robots and autonomous vehicles that benefit from NCL, their OCL capability, and quantitative performance analysis?   
Q11: What are the identified open challenges and proposed future research directions?

By addressing the above key questions, our paper covers all the key aspects discussed above and makes the following contributions (see overview in Fig. 2):

1) We provide the preliminaries of CL including formulation, desiderata, settings, taxonomy of learning scenarios, evaluation metrics, and OCL paradigm. We discuss how different categories of existing CL methods which are pre-dominantly from ANN/DNN domain overcome CF, and which of the desiderata they achieve. Furthermore, we emphasize their challenges (computational/memory overhead) for practical applications in resource-constrained systems, outlining the need for energy-efficient approaches.   
2) We discuss the technical background of low-power neuromorphic computing systems covering the key aspects (i.e., encoding schemes, neuronal dynamics, learning rules, software/hardware frameworks, neuromorphic processor architectures, an elaborate description of neuromorphic datasets, benchmarks & metrics), suggesting the need for standardized NCL benchmarks and additional metrics. We provide a comparative analysis of NCL frameworks with conventional DNN-based CL frameworks. Then, we provide a comprehensive review of state-of-the-art works for NCL, categorizing them into: 1) enhancements on unsupervised STDP learning, 2) predictive coding,

![](images/3171fc89c34b42f00f5c7d4d6e7572a324db88df5af2748a1ffbf396c66acad3.jpg)  
FIGURE 2. Overview of our survey: CL in ANNs/DNNs and SNNs (i.e., NCL). ANNs/DNNs rely on global learning, supervised training, and computationally intensive processing on conventional hardware, thus making them less suitable for OCL. SNNs leverage event-based processing, local learning rules, and low-power neuromorphic hardware which enable energy-efficient CL, thus making them suitable for OCL.

3) active dendrites, 4) bayesian continual learning, 5) architecture, 6) replay, 7) regularization and 8) hebbian learning based methods, assessing their CL performance, OCL capabilities, and neuromorphic hardware compatibility. We discuss hybrid approaches that combine supervised and unsupervised learning paradigms to address CF and improve CL performance. We categorize these approaches into three main classes: 1) self-supervised pre-training hybrids, 2) STDP + supervised learning hybrids, and 3) generative-discriminative hybrid models. We discuss efficiency enhancement techniques for NCL proposed by state-of-the-art including SNN operations reduction, quantization, and knowledge distillation. Moreover, we discuss the performance and computational efficiency trade-offs of NCL considering hardware implementation constraints and provide a comparative quantitative analysis considering design factors and evaluation metrics of the reviewed NCL with relevant DNN-based CL methods.

3) We categorize the current progress of NCL in real-world applications into: 1) adaptive robots, and 2) autonomous vehicles/agents, studying a range of emerging use-cases including object recognition, robotic arm control, cars and road lane detection, Simultaneous Localization and Mapping (SLAM), people detection and robotic navigation, and report their specific case-studies with empirical results, implementation frameworks, and OCL capabilities to assess real-world feasibility. Toward the end, we discuss the identified open research challenges

and provide a perspective on future research directions.

Table 3 summarizes the abbreviations used throughout the paper for clarity and consistency.

# C. PAPER STRUCTURE

The rest of this survey paper is organized as shown in Fig. 3. Section II delves into the CL background. Section III provides detailed technical background of neuromorphic computing systems across multiple aspects and comprehensively reviews state-of-the-art NCL methods, with comparative quantitative and trade-off analysis. In Section IV, several application use-cases of NCL are provided and analyzed. Then, Section V discusses open challenges for meeting the CL desiderata with SNNs and proposes future research directions for each challenge. Finally, Section VI presents the conclusion.

# II. CONTINUAL LEARNING

In recent years, ANNs have revolutionized the field of AI [8], [51], [61], due to their effective training technique (i.e., gradient descent-based backpropagation), while assuming the training data are independently and identically distributed (i.i.d) [62], [63]. However, a critical question arises: how can we integrate new data into existing models? One approach is to retrain with new data, while using current parameters as the initial state [63]. However, successive training tends to cause NNs to suffer from CF [13], [14]. Although retraining from scratch effectively tackles CF issues, but it is inefficient and almost impossible in some cases, such as real-time learning scenarios where the model must update and adapt

![](images/659ae49d339ec9d28d1fc663c43c25639230f3cc0a54ae1fa945d7b2ecb1ecdd.jpg)  
Paper Organization

![](images/9e2a9efb0ee19a6c18b78badb4d2478a361dbbb33f9fa08af51fabf9009be302.jpg)  
FIGURE 3. Organization of our survey paper.

to continuous data streams instantly with limited resources (e.g., developmental learning for autonomous agents [64]).

CL (also known as incremental learning or lifelong learning) addresses CF by accumulating knowledge from a continuous data stream throughout their lifetime [1]. As stability-plasticity dilemma requires trade-off between preserving past knowledge (stability) and adapting to new experiences (plasticity) [65], researchers have developed several CL methods to provide the same capability [66], [67], [68]. While many CL methods focused on the offline learning with supervised task-based incremental learning, which operates under the assumption of i.i.d. data and constant task identification, these assumptions often diverge from realworld scenarios. In practical applications, input data streams are typically not i.i.d. and task identity may not be available. It highlights the complexity of CL problems, showing the importance of understanding the CL foundations. Therefore, in this section, we delve into the basic formulation and desiderata of $\mathrm { C L , }$ and explore various learning scenarios, methods, settings, and evaluation metrics.

# A. BASIC FORMULATION

A CL algorithm must adapt to new tasks without full access to previous training data while maintaining performance on respective test sets. Formally, defined by parameters $\theta \ =$

$\cup _ { t = 1 } ^ { \mathcal { T } } \theta ^ { ( t ) }$ , where $\theta ^ { ( t ) } ~ = ~ \{ e ^ { ( t ) } , \psi \} , ~ e ^ { ( t ) }$ is the task-specific parameters and ψ is the task-sharing parameters for a task t. A batch of training samples for a task t is denoted as $ \mathcal { D } _ { t , b } ~ = \{ \mathcal { X } _ { t , b } , \mathcal { Y } _ { t , b } \}$ where $\mathcal { X } _ { t , b }$ represents input data, $\mathcal { V } _ { t , b }$ denotes data labels, and $t \in \mathcal T = \{ 1 , \cdots , T \}$ signifies the task identity, with $b \in \textit { B } _ { t }$ as the batch index $( \mathcal { T }$ and $B _ { t }$ indicate their respective spaces). Task t is defined by its training samples $\mathcal { D } _ { t } .$ , with distribution $\mathbb { D } _ { t } : = p ( \mathcal { X } _ { t } , \mathcal { Y } _ { t } ) , \mathcal { D } _ { t }$ encompasses the entire training set, omitting the batch index and assuming no distribution discrepancy between training and test sets. However, in practical scenarios, data labels Y and task identity (Task ID) t may not always be available. CL accommodates varying batch sizes for each task’s training samples (i.e., $\{ \{ \mathcal { D } _ { t , b } \} _ { b \in \mathcal { B } _ { t } } \} _ { t \in \mathcal { T } } )$ or simultaneous arrival (i.e., $\{ \mathcal { D } _ { t } \} _ { t \in \mathcal { T } } ) \left[ 1 6 \right]$ .

# B. DESIDERATA OF CL

In this sub-section, we address the key question Q1 by explaining the desired characteristics (desiderata) of a CL algorithm, and show an overview of key requirements to achieve CL capability using a robotic arm as an example in Fig. 4.

# 1) SCALABILITY

A CL algorithm should effectively train on a large or potentially unlimited number of tasks without expanding

![](images/8ce061fd3a48cdf34dd3940923dc3c32dc41dd9c0c8e30854da9b65252dc5b8b.jpg)  
(a) Continual Learning

![](images/d9be638ab3ff1a724bf8b86765ffb75055124eebf64b3a40e3605ba1e1e50ded.jpg)  
(b) Key Desiderata   
FIGURE 4. (a) A robotic arm being trained to perform a variety of tasks sequentially, and is subsequently able to select from its repertoire of learned skills to apply in different situations. (b) Key desiderata for CL; adapted from studies in [1].

NNs excessively. The increasing of NN capacity and computational costs have to be minimal or sub-linear, thereby ensuring the scalability of a CL algorithm [53]. To achieve high scalability, the major challenges include scalability of network model size [16], [69] and scalability of regularization terms (e.g., weight regularization [70]).

# 2) NO/MINIMAL USAGE OF OLD DATA

Minimizing or eliminating the reliance on data from previous tasks is crucial for a CL algorithm, because of storage constraints and privacy concerns. Recent research has made progress to achieve this goal [71], [72], [73], [74], [75], [76]. For instance, previous studies used mutual information maximization and compressed gradients to minimize the reliance on old data [71], [72], [73], and employed representative subsets to preserve knowledge [74].

# 3) TASK AGNOSTIC (TA)

A CL algorithm should function independently from pre-defined task boundaries during the training and inference phases, known as Task Agnostic (TA). For instance, a robot in an ever-changing environment should adapt to new tasks, such as picking up different objects or navigating new terrains without explicit information of task identity. It has to learn from environment and experiences, and dynamically adjust to new tasks. State-of-the-art attempted to achieve TA using methods studied in [77], [78], [79], [80], [81], [82], [83], and [84].

# 4) POSITIVE FORWARD TRANSFER (FWT)

A CL algorithm should leverage previous knowledge to enhance performance on new tasks, known as Positive Forward Transfer (FWT). Formally, $\mathrm { F W T } _ { k }$ evaluates the average influence of all old tasks on the current k-th task, and can be stated as:

$$
\mathrm {F W T} _ {k} = \frac {1}{k - 1} \sum_ {j = 2} ^ {k} \left(a _ {j - 1, j} - \tilde {a} _ {j}\right) \tag {1}
$$

where, $\tilde { a } _ { j }$ is the accuracy of a randomly-initialized model trained with data $\mathcal { D } _ { j }$ for the j-th task [16]. The parameter $a _ { j - 1 , j }$ denotes accuracy on task j after learning task $j - 1$ , but before task $j$ and $\tilde { a } _ { j }$ denotes baseline performance on task j without prior learning. High FWT indicates that the model generalizes well to unseen tasks by reusing learned knowledge. Recent research explored different methods to enable FWT, including studies in [53], [85], [86], [87], [88], [89], [90], [91], [92], [93], and [94].

# 5) POSITIVE BACKWARD TRANSFER (BWT)

A CL algorithm should transfer knowledge from later tasks to past tasks for improving performance on the past tasks, known as Positive Backward Transfer (BWT). Negative BWT reflects CF and zero BWT suggests zero forgetting [53]. Formally, $\mathrm { B W T } _ { k }$ evaluates the average influence of learning

TABLE 3. List of abbreviations.   

<table><tr><td>Abbreviation</td><td>Full Form</td></tr><tr><td>CL</td><td>Continual Learning</td></tr><tr><td>DL</td><td>Deep Learning</td></tr><tr><td>ANN</td><td>Artificial Neural Network</td></tr><tr><td>DNN</td><td>Deep Neural Network</td></tr><tr><td>CNN</td><td>Convolutional Neural Network</td></tr><tr><td>NNs</td><td>Neural Networks</td></tr><tr><td>CF</td><td>Catastrophic Forgetting</td></tr><tr><td>NCL</td><td>Neuromorphic Continual Learning</td></tr><tr><td>SNN</td><td>Spiking Neural Network</td></tr><tr><td>CSNN</td><td>Convolutional SNN</td></tr><tr><td>OCL</td><td>Online Continual Learning</td></tr><tr><td>TA</td><td>Task Agnostic</td></tr><tr><td>FWT</td><td>Positive Forward Transfer</td></tr><tr><td>BWT</td><td>Positive Backward Transfer</td></tr><tr><td>RL</td><td>Reinforcement Learning</td></tr><tr><td>STDP</td><td>Spike-Timing-Dependent Plasticity</td></tr><tr><td>SLAM</td><td>Simultaneous Localization and Mapping</td></tr><tr><td>Task-IL</td><td>Task-Incremental Learning</td></tr><tr><td>Domain-IL</td><td>Domain-Incremental Learning</td></tr><tr><td>Class-IL</td><td>Class-Incremental Learning</td></tr><tr><td>DTA</td><td>Discrete Task Agnostic</td></tr><tr><td>CTA</td><td>Continuous Task Agnostic</td></tr><tr><td>OWTA</td><td>Open-World Task Agnostic</td></tr><tr><td>SSL</td><td>Self-Supervised Learning</td></tr><tr><td>CPT</td><td>Continual Pre-Training</td></tr><tr><td>BP</td><td>Backpropagation</td></tr><tr><td>EWC</td><td>Elastic Weight Consolidation</td></tr><tr><td>FIM</td><td>Fisher Information Matrix</td></tr><tr><td>SI</td><td>Synaptic Intelligence</td></tr><tr><td>GEM</td><td>Gradient Episodic Memory</td></tr><tr><td>GPM</td><td>Gradient Projection Memory</td></tr><tr><td>MAS</td><td>Memory Aware Synapses</td></tr><tr><td>RWalk</td><td>Riemannian Walk</td></tr><tr><td>MLP</td><td>Multi-layer Perceptron</td></tr><tr><td>FC</td><td>Fully-Connected</td></tr><tr><td>CFN</td><td>Controlled Forgetting Network</td></tr><tr><td>ASP</td><td>Adaptive Synaptic Plasticity</td></tr><tr><td>ViT</td><td>Vision Transformer</td></tr><tr><td>KD</td><td>Knowledge Distillation</td></tr><tr><td>ER</td><td>Experience Replay</td></tr><tr><td>HW</td><td>Hardware</td></tr><tr><td>SW</td><td>Software</td></tr><tr><td>TTFS</td><td>Time-to-first Spike</td></tr><tr><td>HH</td><td>Hodgkin-Huxley</td></tr><tr><td>IF</td><td>Integrate-and-Fire</td></tr><tr><td>LIF</td><td>Leaky IF</td></tr><tr><td>AdExIF</td><td>Adaptive Exponential IF</td></tr><tr><td>SDSP</td><td>Spike-Driven Synaptic Plasticity</td></tr><tr><td>R-STDP</td><td>Reward-Modulated STDP</td></tr><tr><td>PES</td><td>Prescribed Error Sensitivity</td></tr><tr><td>BPTT</td><td>Backpropagation Through Time</td></tr><tr><td>SG</td><td>Surrogate Gradient</td></tr><tr><td>STBP</td><td>Spatio-Temporal Backpropagation</td></tr><tr><td>DECOLLE</td><td>Deep Continuous Local Learning</td></tr><tr><td>ST-LRA</td><td>Spike-Triggered Local Representation Alignment</td></tr><tr><td>BrainCog</td><td>Brain-inspired Cognitive Intelligence Engine</td></tr><tr><td>CPU</td><td>Central Processing Unit</td></tr><tr><td>GPU</td><td>Graphic Processing Unit</td></tr><tr><td>MCU</td><td>Microcontroller Unit</td></tr><tr><td>TPU</td><td>Tensor Processing Unit</td></tr><tr><td>CMOS</td><td>Complementary Metal-Oxide-Semiconductor</td></tr><tr><td>FPGA</td><td>Field-Programmable Gate Array</td></tr><tr><td>ASIC</td><td>Application-Specific Integrated Circuit</td></tr><tr><td>ROLLS</td><td>Reconfigurable On-line Learning Spiking</td></tr><tr><td></td><td>Neuromorphic Processor</td></tr><tr><td>PIM</td><td>Processing-In-Memory</td></tr><tr><td>CIM</td><td>Compute-In-Memory</td></tr><tr><td>NVM</td><td>Non-Volatile Memory</td></tr><tr><td>RRAM</td><td>Resistive Random Access Memory</td></tr><tr><td>MRAM</td><td>Magnetic RAM</td></tr><tr><td>PCM</td><td>Phase Change Memory</td></tr></table>

TABLE 3. (Continued.) List of abbreviations.   

<table><tr><td>Abbreviation</td><td>Full Form</td></tr><tr><td>DVS</td><td>Dynamic Vision Sensor</td></tr><tr><td>ATIS</td><td>Asynchronous Time-based Image Sensor</td></tr><tr><td>DAS</td><td>Dynamic Audio Sensor</td></tr><tr><td>NVS</td><td>Neuromorphic Vision Sensor</td></tr><tr><td>BAE</td><td>Biologically Plausible Auditory Encoding</td></tr><tr><td>mAP</td><td>Mean Average Precision</td></tr><tr><td>MAE</td><td>Mean Absolute Error</td></tr><tr><td>MAEL</td><td>MAE for Localisation</td></tr><tr><td>MAEM</td><td>MAE for Mapping</td></tr><tr><td>MSE</td><td>Mean Square Error</td></tr><tr><td>RMSE</td><td>Root Mean Square Error</td></tr><tr><td>AOC</td><td>Average of top-1 accuracy over classes</td></tr><tr><td>ITAE</td><td>Integral of Time-weighted Absolute Error</td></tr><tr><td>SNR</td><td>Signal-to-Noise Ratio</td></tr><tr><td>SpNCN</td><td>Spiking Neural Coding Network</td></tr><tr><td>DSD-SNN</td><td>Dynamic Structure Development of SNN</td></tr><tr><td>SOR-SNN</td><td>Self-Organized Regulation SNN</td></tr><tr><td>LR</td><td>Latent Representation/Replay</td></tr><tr><td>HLOP</td><td>Hebbian Learning-based Orthogonal Projection</td></tr><tr><td>NEF</td><td>Neural Engineering Framework</td></tr><tr><td>NSM</td><td>Neural State Machine</td></tr><tr><td>IK</td><td>Inverse Kinematics</td></tr><tr><td>PID</td><td>Proportional Integral Derivative</td></tr><tr><td>PES</td><td>Prescribed Error Sensitivity</td></tr><tr><td>WCE</td><td>Weighted Binary Cross Entropy</td></tr><tr><td>IoU</td><td>Intersection over Union</td></tr><tr><td>FMCW</td><td>Frequency Modulated Continuous Wave</td></tr><tr><td>HNN</td><td>Hybrid Neural Network (SNN-ANN)</td></tr><tr><td>FPS/W</td><td>Frames Per Second per Watt</td></tr><tr><td>DoF</td><td>Degrees of Freedom</td></tr><tr><td>FID</td><td>Fréchet distance</td></tr></table>

the k-th task on all old tasks, and can be stated as:

$$
\mathrm {B W T} _ {k} = \frac {1}{k - 1} \sum_ {j = 1} ^ {k - 1} \left(a _ {k, j} - a _ {j, j}\right) \tag {2}
$$

where, $a _ { k , j }$ is the accuracy of a model at j-th task after incremental learning of the k-th task [16]. The parameter $a _ { j , j }$ denotes accuracy of task j when it was first learned.

# 6) CONTROLLED FORGETTING

A CL algorithm should forget old yet insignificant knowledge to make room for learning new information, known as controlled forgetting. Although humans do not experience sudden memory loss, a gradual decrease in memory (forgetting) over time is natural, hence controlled forgetting is beneficial for managing memory retention [95]. Related methods include [96], [97], [98] for ANNs and [42], [43], [99], [100] for SNNs.

# 7) FAST ADAPTATION AND RECOVERY

A CL algorithm should quickly learn new tasks while minimizing the loss of previous knowledge (fast adaptation), and regain previous performance after encountering new tasks that cause degradation in learned knowledge (recovery). Related methods include regularization [70] and gradientbased meta-learning or fast optimization [101].

# C. CL SETTINGS

In this sub-section, we address the key question Q1 by introducing the definition of learning settings in which the CL methods operate, based on how the data label and information are utilized for learning process, including the supervised, unsupervised, and reinforcement learning settings.

# 1) SUPERVISED LEARNING

It is an ML setting that trains models with labeled datasets. Therefore, in the Supervised CL setting, the goal is to train a model on a sequential data stream. Its challenge is to efficiently perform the training, since the supervised-based learning typically requires huge memory and energy requirements. Moreover, obtaining a large labeled dataset can be time consuming and expensive.

# 2) UNSUPERVISED LEARNING

It is an ML setting that trains models with unlabeled data (e.g., identifying patterns, structures, or relationships) [102]. Therefore, in the Unsupervised CL setting, the goal is to develop a model that can discover similarity in samples that arrive sequentially [102]. Its challenge is to extract meaningful features without explicit labels. This setting is particularly useful for tasks where data labeling is impractical or expensive.

# 3) REINFORCEMENT LEARNING (RL)

It is an ML setting that trains models to make sequential decisions based on the feedback (i.e., rewards or penalties) [103], [104]. Through trials and errors, the model learns to associate actions with outcomes, aiming to discover the optimal strategy or policy to achieve its objectives over time. Its challenge is to efficiently perform the training, as RL typically requires high memory and energy requirements. Moreover, the nature of trials and errors can also be time-consuming and expensive.

# D. EVALUATION METRICS

To evaluate the performance of an efficient CL system, metrics are essential. This sub-section addresses the key question Q1 for evaluation metrics. To assess the overall performance of a CL algorithm, average accuracy (AA) [89], [105], average incremental accuracy (AIA) [106], [107] and forgetting (F) are often used, where F is the average maximum drop in classification accuracy over time, with lower values indicating better retention. BWT and FWT are also used to quantify memory stability and learning plasticity, respectively, in CL. Model size is used to measure the memory size for storing the model parameters [108], while sample storage size (SSS) is used to measure the storage size for storing data samples. To evaluate the computational resources required for the training and inference phases, metrics such as the number of floating-point operationsper-second (FLOPS) and time complexity are often used.

Meanwhile, power/energy efficiency measures the efficiency gains of a CL system during its operational life-time.

# E. SCENARIOS IN CL

In this sub-section, we address key question Q1 regarding the CL scenarios by presenting their definitions, taxonomy (shown in Fig. 5), and formal comparison in Table 4. The initially-identified scenarios are Task-Incremental Learning (Task-IL), Domain-Incremental Learning (Domain-IL), and Class-Incremental Learning (Class-IL). While these scenarios cover some desiderata of CL, they fail to meet the requirement of TA [53]; see Fig. 6. They assume that tasks have clear and well-defined boundaries during training. Therefore, recent studies proposed expanding the CL scenarios by introducing Discrete TA (DTA) [77], Continuous TA (CTA) [77], and Open-World TA (OWTA) [53].

![](images/98c56fa30c6318404e695eb2632842de5db8b2471e5fe30275ea64a0969e5a36.jpg)  
FIGURE 5. Taxonomy of the CL scenarios based on the nature of training and inference setups considering the task identity (Task ID); adapted from studies in [53].

# 1) TASK-INCREMENTAL LEARNING (TASK-IL)

In Task-IL, a model sequentially learns to solve a number of distinct tasks [109], [110], [111]. Each task has disjoint output spaces $\{ \mathcal { V } _ { t - 1 } ~ \neq ~ \mathcal { V } _ { t } \}$ and Task IDs are known in training and testing phases. Typically, Task-IL employs multi-headed model (i.e., an output head for each task). An NN model equipped with a multi-headed output layer can accommodate various tasks, making $p ( \mathcal { V } _ { t - 1 } ) \neq p ( \mathcal { V } _ { t } )$ and $p ( \mathcal { X } _ { t - 1 } ) \neq p ( \mathcal { X } _ { t } )$ true (Table 4).

# 2) DOMAIN-INCREMENTAL LEARNING (DOMAIN-IL)

In Domain-IL, a model learns to solve the same problem in different tasks [109], [110], [111]. Tasks have the same data label space $\{ \mathcal { V } _ { t - 1 } ~ = ~ \mathcal { V } _ { t } \}$ but different input distributions $p ( \mathcal { X } _ { t - 1 } ) \neq p ( \mathcal { X } _ { t } )$ . The model does not require Task IDs in the inference phase, as each task has the same possible outputs (e.g., same classes in each task). The use of a single-headed model (i.e., same output head for every task) ensures that the output space remains consistent. An example of Task-IL

TABLE 4. The CL scenarios based on the difference between $\mathcal { D } _ { t - 1 }$ and $\mathbf { \delta } _ { \mathcal { D } _ { t } , }$ , (adapted from [46]). p(X ) is the input data distribution; p(Y) is the target label distribution; $\{ \mathcal { V } _ { t - 1 } \neq \mathcal { V } _ { t } \}$ denotes that output space are from a disjoint space which is separated by task identity (Task ID).   

<table><tr><td rowspan="2">CL Scenario</td><td colspan="3">Difference between Dt-1 and Dt</td><td colspan="2">Task ID</td><td rowspan="2">Online Learning</td></tr><tr><td>p(Xt-1) ≠ p(Xt)</td><td>p(Yt-1) ≠ p(Yt)</td><td>{Yt-1}</td><td>Train</td><td>Test</td></tr><tr><td>Task-IL</td><td>✓</td><td>✓</td><td>✓</td><td>Known</td><td>Known</td><td>No</td></tr><tr><td>Domain-IL</td><td>✓</td><td>×</td><td>×</td><td>Known</td><td>Not required</td><td>Optional</td></tr><tr><td>Class-IL</td><td>✓</td><td>✓</td><td>×</td><td>Known</td><td>To be inferred</td><td>Optional</td></tr><tr><td>DTA</td><td>✓</td><td>×</td><td>×</td><td>Not required</td><td>Not required</td><td>Yes</td></tr><tr><td>OWTA</td><td>✓</td><td>✓</td><td>×</td><td>To be inferred</td><td>To be inferred</td><td>Yes</td></tr><tr><td>CTA</td><td>×</td><td>×</td><td>×</td><td>Unknown</td><td>Unknown</td><td>Yes</td></tr></table>

![](images/3ba864cb34f8a12e3d91ac224f332035b9704dd2b8be9582d04e863bf9bd92f9.jpg)  
(a)

FIGURE 6. Split MNIST according to Task-IL, Domain-IL, and Class-ID.(a) Split MNIST is obtained by splitting the original MNIST into five contexts/tasks, each having two classes. (b) Overview of what is expected of the model at test time for each scenario.   

<table><tr><td></td><td>Input (at test time)</td><td>Expected Output</td><td>Intuitive Description</td></tr><tr><td>Task-Incremental Learning (Task-IL)</td><td>Image + context label</td><td>Within-context label*</td><td>Choice between two digits of same context (e.g. 0 or 1)</td></tr><tr><td>Domain-Incremental Learning (Domain-IL)</td><td>Image</td><td>Within-context label</td><td>Is the digit odd or even?</td></tr><tr><td>Class-Incremental Learning (Class-IL)</td><td>Image</td><td>Global label</td><td>Choice between all ten digits</td></tr></table>

is incrementally learning to recognize objects midst varying lighting conditions (e.g., indoor and outdoor) [112].

# 3) CLASS-INCREMENTAL LEARNING (CLASS-IL)

In Class-IL, a model must distinguish the global labels (classes) [109], [110], [111]. Here, Task IDs are only provided in the training phase, as they will be inferred in the inference phase. Due to the multi-class property, $p ( \mathcal { V } _ { t - 1 } ) \neq p ( \mathcal { V } _ { t } )$ is a natural consequence, thereby posing more challenges as compared to Task-IL and Domain-IL.

# 4) DISCRETE TASK AGNOSTIC (DTA)

In DTA, a model learns from a sequence of distinct tasks, but without the need for inferring the Task ID during training and inference phases [53], [77]. The input distributions differ between tasks, making $p ( \mathcal { X } _ { t - 1 } ) \ \neq \ p ( \mathcal { X } _ { t } )$ true. Meanwhile, the target label across tasks have the same distributions, and the output space is the same across tasks, making $p ( \mathcal { V } _ { t - 1 } ) \neq$ $p ( \mathcal { V } _ { t } )$ and $\{ \mathcal { V } _ { t - 1 } \neq \mathcal { V } _ { t } \}$ false.

# 5) OPEN-WORLD TASK AGNOSTIC (OWTA)

In OWTA, a model learns from a sequence of distinct tasks, but needs to infer the Task ID during training and inference phases [53], [77]. It requires the CL algorithm to handle an open set of tasks and classes, potentially facing unknown categories that are not encountered during initial training. This makes the OWTA as one of the most challenging scenarios.

# 6) CONTINUOUS TASK AGNOSTIC (CTA)

In CTA, data stream is represented as a continuous function over time without explicit task boundaries [53], [77], which makes CTA as the most challenging scenario. Here, a CL algorithm must learn from evolving distribution without any task-specific guidance, as neither task boundaries are clear nor Task ID is known during the training phase [53], making $p ( \mathcal { X } _ { t - 1 } ) \neq p ( \mathcal { X } _ { t } ) , p ( \mathcal { Y } _ { t - 1 } ) \neq p ( \mathcal { Y } _ { t } )$ and $\{ \mathcal { V } _ { t - 1 } \neq \mathcal { V } _ { t } \}$ false.

# F. ONLINE CONTINUAL LEARNING (OCL)

In OCL, a model learns from a continuous data stream, so that each input sample during inference is used as training data for updating the models’ knowledge [46], [113], [114]. As a new sample arrives, it is immediately used for inference, and for updating the model on-the-fly. This capability is highly desired for systems that face highly dynamic environments (e.g., autonomous mobile agents), where new data is encountered in real-time and immediate updates to the model are required. Its challenges include integrating new knowledge and retaining previous information, while considering limited memory and power/energy budgets. In this survey, we emphasize that OCL is the expected capability for embedded AI systems.

# G. CL METHODS

In this sub-section, we address the key question $\mathbf { Q } 2 ,$ , by providing an overview of the existing methods that address

CF in various CL scenarios, and the desiderata they fulfill; summarized in Table 5. These methods are categorized into five approaches based on representation, regularization, rehearsal/replay, optimization, and architecture [16], as follows.

# 1) REPRESENTATION-BASED APPROACH

This approach is characterized by exploiting the strengths of data representations [16]; see Fig. 7. The related methods are as follows.

![](images/a27809fc603712104596814a3580d57e2672708fb8f020167cfb24ae9a0fece5.jpg)

![](images/0b04851c627837ac7cce3ea9cd971bde505f9b014411653ab3bd94e97aa56aad.jpg)  
FIGURE 7. An illustration of the taxonomy of (a) representation-based approach and (b) its respective methods; adapted from studies in [16].

1) Self-Supervised Learning (SSL): It makes the model learn to generate useful data representations without relying on explicit labels, by creating supervisory signals from the input data to uncover the underlying structure of the data [115], [116]. Related studies are discussed in [117], [118], [119], [120], [121], [122], and [123].   
2) Pre-training for Downstream CL: It is the initial phase of model training on a large diverse dataset to learn general-purpose representations, which can be fine-tuned for specific downstream tasks, hence having strong knowledge transfer [86], [124], [125], [126]. To maintain generalizability for future tasks, several strategies have been developed, such as Pretrained Representations [91], [127], [128], [129], [130], Task-adaptive Prompts [131], [132], [133], [134], [135], [136], Saving Prototypes and Enhancing Classifiers [137], [138], [139], and Optimizing an Updatable Backbone [86], [140], [141], [142], [143].   
3) Continual Pre-Training (CPT): It includes techniques studied in [144], [145], [146], [147], [148], [149], and [150].

# 2) REGULARIZATION-BASED APPROACH

This approach is characterized by adding explicit regularization terms to balance the old and new tasks [16], which usually requires storing a frozen copy of the old model for reference; see Fig. 8. The related methods are as follows.

![](images/3616ad344bf7437f99d20c629341fc494aa857a6d2a659ee55f6d750cc9ecbce.jpg)

![](images/19b11cb12eff4c3bc4bf9ce58b8e9db3700c445047acecf859602b2c2fa72e9c.jpg)  
FIGURE 8. An illustration of the taxonomy of (a) regularization-based approach and (b) its respective methods; adapted from studies in [16].

1) Weight Regularization: It includes techniques such as Elastic Weight Consolidation (EWC) [70], Synaptic Intelligenc (SI) [66], Memory Aware Synapses (MAS) [151], Riemannian Walk (RWalk) [105]. Meanwhile, other techniques are categorized into Expansion-Renormalization [90], [98], [152], [153], Quadratic Penalty Refinement [154], [155], [156], and Online Variational Inference [96], [157], [158], [159], [160], [161], [162].   
2) Function Regularization: It regulates the variations in models’ function $f _ { \theta }$ over time, and applies constraints directly to the function. A generalized form of function regularization can be expressed as:

$$
\begin{array}{l} \theta_ {t} = \arg \min  _ {\theta} \\ \times \left(\frac {1}{N _ {t}} \sum_ {i = 1} ^ {N _ {t}} \mathcal {L} _ {t} \left(f _ {\theta} \left(\mathbf {x} _ {i}\right), y _ {i}\right) + \lambda \mathcal {R} _ {f} \left(f _ {\theta}, \mathcal {D} _ {1: t - 1}\right)\right) \tag {3} \\ \end{array}
$$

where, $\theta \in \mathbb { R } ^ { d }$ denotes the model parameters (weights) after learning task t. The term 1N PNti=1 Lt (fθ (xi), yi) $\begin{array} { r } { \frac { \hat { 1 } } { N _ { t } } \sum _ { i = 1 } ^ { N _ { t } } \mathcal { L } _ { t } ( f _ { \theta } ( \mathbf { x } _ { i } ) , y _ { i } ) } \end{array}$ calculates the average loss on the current task t, where $N _ { t }$ is the number of samples in task $t , \mathbf { x } _ { i } \in \mathbb { R } ^ { n }$ is the input feature vector for the $i ^ { \mathrm { { t h } } }$ training sample for task $t , y _ { i }$ is the corresponding ground truth label for $\mathbf { x } _ { i } , f _ { \theta } ( \mathbf { x } _ { i } )$ is the model’s prediction for input $\mathbf { x } _ { i }$ using parameters $\theta$ and $\mathcal { L } _ { t }$ is the task-specific loss function (e.g.,

cross-entropy for classification). $\mathscr { R } _ { f } ( f _ { \theta } , \mathscr { D } _ { 1 : t - 1 } )$ is the function regularization term that penalizes changes in the models’ function $f _ { \theta }$ based on its performance on previous data $\mathcal { D } _ { 1 : t - 1 }$ from tasks 1 to t − 1 and λ is a hyperparameter controlling the strength of the regularization i.e., the balance between stability and plasticity. The goal is to find the set of weights $\theta _ { t }$ that minimize both the loss on the current task and the deviation from prior knowledge.

3) Knowledge Distillation (KD): It utilizes the previouslytrained model as the teacher and the currently-trained model as the student [16]. It includes techniques studied in [106], [163], [164], [165], and [166].   
4) Besides the above prominent methods, several alternatives have also been proposed: Sequential Bayesian Inference over Function Space [167], [168], [169] and Conditional Generation [170], [171], [172].

![](images/c6e5366c2463972c624c19760fbddcde88151101431e58146a10022897df2d24.jpg)  
(a)

![](images/f2cc49f6a18d8015a70f1b7789005c868ae4d198a08a7ef726a52aa266604aa0.jpg)  
(b)   
FIGURE 9. An illustration of the taxonomy of (a) replay-based approach and (b) its respective methods; adapted from studies in [16].

# 3) REHEARSAL/REPLAY-BASED APPROACH

This approach is characterized by approximating and recovering old data distributions [16]; see Fig. 9. The related methods are discussed in the following.

1) Experience Replay (ER): It stores a few old training samples in a small memory buffer. It includes several strategies such as Sample Selection (SS) [88], [89], [106], [173], Gradient/Optimization-based Techniques [113], [174], [175], [176], [177], [178], Storage Efficiency [68], [177], [179], [180], [181], [182], Integration of ER with KD [106], [183], Mitigation of Data Imbalance [107], [122], [171], [184], [185], [186], [187], [188], [189], [190], Learning Plasticity

Enhancement [191], [192], and Overfitting Alleviation [193], [194], [195], [196], [197].

2) Generative Replay: It uses an additional generative model such as Generative Adversarial Networks (GANs) [198] or Variational Autoencoders (VAEs) [199] to replay the previously-learned data [21]. There are several GANs-based techniques as studied in [67], [129], [170], [200], and [201]. However, they usually suffer from label inconsistency [67]. Toward this, other techniques employ autoencoderbased strategies [21], [202], [203].   
3) Feature Replay: It includes techniques studied in [22], [23], [204], [205], [206], [207], [208], and [209].

# 4) OPTIMIZATION-BASED APPROACH

This approach is characterized by explicitly designing and manipulating the optimization programs [16]; see Fig. 10. It includes the following methods.

![](images/e69b78a5749094e32d36f08fa8f8e5f0597119f8bef32d19b294a29722984abd.jpg)  
(a)

![](images/beb6f8c8a1bcb2b3435b33a1192227f13e8766a9432aeabd3b88bc0801f5e707.jpg)  
  
FIGURE 10. An illustration of the taxonomy of (a) optimization-based approach and (b) its respective methods; adapted from studies in [16].

1) Gradient Projection: It includes techniques studied in [210], [211], [212], [213], [214], [215], [216], [217], [218], and [219] and the ones with Replay-based Strategies [88], [89], [220], [221].   
2) Loss Landscape: The related techniques are studied in [222], [223], and [224].   
3) Meta-Learning: It is also known as learning-to-learn for CL, which attempts to obtain a data-driven inductive bias for various scenarios, rather than designing it manually [15]. It includes techniques studied in [87], [88], [225], [226], [227], [228], [229], [230], [231], [232], and [233].

# 5) ARCHITECTURE-BASED APPROACH

This approach is characterized by constructing task-specific parameters, that can explicitly resolve the inter-task interference caused by incremental task learning with shared

parameters [16]; see Fig. 11. It encompasses the following methods.

![](images/029f4db81f4ae49abe43e2e808cbd75643bb9b843d2a54b96fa944faf7d8897a.jpg)  
FIGURE 11. An illustration of the taxonomy of (a) architecture-based approach and (b) its respective methods; adapted from studies in [16].

1) Parameter Allocation: It isolates parameter subspace, which is dedicated to each task throughout the model, where the architecture can be fixed or dynamic in size. It includes strategies like Fixed Architecture [69], [96], [97], [162], [234], [235], [236], [237] and Dynamic Architecture [238], [239].   
2) Modular Network: It leverages parallel sub-networks to learn new tasks one-by-one, without pre-defined task-sharing or task-specific components. The related techniques are studied in [92], [93], [240], [241], [242], [243], [244], [245], and [246].   
3) Model Decomposition: It separates a model into the task-sharing and task-specific components [16] (Fig. 12). The relate techniques are studied in [247], [248], [249], [250], [251], [252], [253], and [254].

![](images/379188c7df451fc1a700479b8c7f2b46b97f29caef11f60d46c04a68aa233b24.jpg)  
FIGURE 12. An illustration of the model decomposition method exhibiting two types; corresponding to parameters (i.e., low-rank factorization) and representations (i.e., masks of intermediate features); adapted from studies in [16].

# H. LIMITATIONS OF EXISTING CL METHODS

The CL desiderata fulfilled by the existing CL methods (discussed in Section II-G) are presented in Table 5. This table shows that, different CL methods feature different advantages and disadvantages. Furthermore, the limitations of existing CL methods in DNNs and the challenges that impede their direct application to SNNs are discussed as follows, answering key question Q3. A summary of these limitations is provided in Table 6. For example, weight regularization with methods like EWC [70] and SI [66] requires estimating and storing importance measures (e.g., FIM calculations) for every synapse, adding a quadratic penalty term for each learned task, which is resource-intensive in high-dimensional, event-driven SNNs, therefore has a linearly increasing computational cost [44]. Moreover, such importance scores assume a static activation landscape, which is unstable in SNNs due to variable spiking activity and dynamic thresholds. Replay-based methods (e.g., iCaRL [106], DGR [200], GEM [89]) require storing and reprocessing raw input samples or features. This is not well suited for neuromorphic hardware, which operates under strict memory and power constraints and lacks the infrastructure to store dense data or continuously replay high-dimensional inputs efficiently. Many CL methods in DNNs rely on precise gradient computations through differentiable activation functions. In contrast, SNNs involve discontinuous spike events and temporal dynamics, making conventional BP infeasible or biologically implausible. Although SG methods exist, they are computationally expensive. Moreover, spike-based learning involves temporally extended input encoding. Mapping gradient-based loss functions from DNN-CL to temporally sparse spike trains introduces ambiguity in assigning credit across time, which is non-trivial and often requires costly unrolling (e.g., through BPTT). Most DNN-based CL methods assume synchronous, frame-based computation. SNNs operate asynchronously, responding to sparse events. This fundamental mismatch makes it difficult to translate CL mechanisms designed for batch updates and full forward/backward passes into the SNN regime without re-engineering their entire workflow.

These limitations in adapting conventional CL strategies to SNNs underscore the critical need for a paradigm shift towards neuromorphic-specific CL algorithms that can achieve higher performance while minimizing energy consumption. This is especially important for deployments in embedded AI systems (e.g., mobile robots/agents and IoT-Edge) where compute and memory budgets are limited, highlighting the reasons why the energy-efficient CL algorithms are crucial for resource-constrained embedded AI systems posed by the key question Q3.

Motivated by the limitations of existing CL methods, NCL concept has emerged as a potential solution as it has characteristics that align with the desiderata of CL. Specifically, NCL leverages SNN computation models which has eventdriven operations, thus enabling energy-efficient learning.

Furthermore, SNNs can perform unsupervised learning due to their bio-plausible learning rules. Details of NCL concept and review of NCL methods that are explicitly designed to operate under the constraints of event-driven computation, limited memory, and hardware variability inherent to neuromorphic systems will be discussed in Section III.

# III. NEUROMORPHIC COMPUTING

# A. OVERVIEW OF SNNs

A neuromorphic computing system encompasses SNN processing (including spike-based operations and training) in the software part, and a neuromorphic processor in the hardware part. The overview of the system is illustrated in Fig. 13, and described in the following, answering key question Q4.

![](images/b0db48df89b14556f3b93f6703436cd85e329023b77d786a13034863e1f89e76.jpg)  
FIGURE 13. An overview of a neuromorphic system, encompassing hardware (HW) and software (SW) parts.

# 1) SNN MODELS AND OPERATIONS

SNNs mimic the brains’ functionality through the utilization of spikes for transmitting information [38], [264], [265]. Therefore, SNNs encode information into discrete spike trains. Popular encoding techniques include rate coding [266] (e.g., spike count, spike density, population activity [267]), and temporal coding (e.g., burst [268], time-to-first spike (TTFS) [269], phase [270], and rank-order [271]). Each spiking neuron processes the input spikes, and its internal behavior (i.e., neuronal dynamics) depends on the spiking neuron model, such as Hodgkin–Huxley (HH) [272], Leaky Integrate and Fire (LIF) [273], Izhikevich Model [274], and Adaptive Exponential Integrate-and-Fire (AdExIF) [275]. Neuron model selection typically considers the expected neuronal dynamics and computational complexity [276], [277]. The illustration of neuronal dynamics and computational complexity trade-off for different neuron models is shown in Fig. 14. The output spikes are generated only when neurons’ membrane potential reaches the threshold, and transmitted through synapses, enabling ultra-low power/energy consumption [50], [278], [279], [280], [281].

Note, spike-based operations can also be applied to emerging network models like Transformers, i.e., so-called Spikebased Transformers, by employing spike data representation and spiking neuron model in Transformer network architectures, as demonstrated in recent research works [282], [283], [284], [285], [286]. These works show that Spike-based Transformers have comparable scalability and performance over the conventional Transformers, while enabling higher

energy efficiency when executed on neuromorphic hardware due to their sparse spike-based operations.

![](images/3b9938246b7af1fb9d01561a0f28ad9acc5f524debe4f0d38c8c9f1c1d5a7552.jpg)  
FIGURE 14. Trade-off between bio-plausibility and computation complexity for different neuron models; adapted from studies in [274].

# 2) SNN TRAINING

The training process can be performed using bioplausible or analytical learning rules. The bio-plausible ones are typically characterized by local learning mechanism, like Hebbian [287], Spike-Timing-Dependent Plasticity (STDP) [288], Spike-Driven Synaptic Plasticity (SDSP) [289], [290], and Reward-Modulated STDP (R-STDP) [291], [292]. Meanwhile, the analytical ones encompass DNN-to-SNN conversion [293], Surrogate Gradient Learning [294], [295], [296] (e.g., Backpropagation Through Time (BPTT) [294], [297], [298], Spatio-Temporal Backpropagation (STBP) [299], and Deep Continuous Local Learning (DECOLLE) [300]), Spike-Triggered Local Representation Alignment (ST-LRA) [301], and Bayesian Learning [302]. To facilitate SNN training, software frameworks play a vital role. Some notable ones include SpikingJelly [303], BindsNet [304], SNNtorch [305], TinySpiking [306], Norse [307], SpyTorch [308], SINABS [309], Spyke-Torch [310], Brian [311], Lava [312], BrainCog [313], PySNN [314], and PyNCS [315]. These frameworks are still evolving to support CL features. Meanwhile, standard DL frameworks such as Tensorflow [316] and PyTorch [317], and CL frameworks such as PyCIL [318], FACIL [47] and Avalanche [319] stand out for their user-friendly interfaces, flexibility, and support for complex applications. Table 7 addresses the key question Q5 by comparing neuromorphic, DL and CL frameworks, outlining that the SNN frameworks with local STDP learning and neuromorphic hardware are more computationally efficient.

# 3) NEUROMORPHIC HARDWARE

SNN processing demands a suitable computing hardware to maximize its potentials in accuracy, latency, and power/energy efficiency. Conventional von-Neumann architecture-based hardware platforms (e.g., CPU and GPUs) have been widely used to perform Python-based SNN processing using generic arithmetic units [303], [304], [320],

TABLE 5. Representation-, Regularization-, Rehearsal/Replay- and Architecture-based CL methods that potentially fulfill ‘‘+’’ or have fulfilled ‘‘✓’’ the desiderata of CL.   

<table><tr><td rowspan="2">Approach</td><td rowspan="2">Methods</td><td rowspan="2">Work,(Year)</td><td colspan="7">Desiderata of CL</td></tr><tr><td>Scalability</td><td>No/Minimal Old Data Use</td><td>Task Agnostic</td><td>Positive FWT</td><td>Positive BWT</td><td>Controlled Forgetting</td><td>Fast Adaptation</td></tr><tr><td rowspan="12">Representation</td><td rowspan="5">Pre-training for Downstream Tasks</td><td>[72],(2023)</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[255],(2023)</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[76],(2024)</td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>[256],(2024)</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MAML [101],(2017)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>✓</td></tr><tr><td>Self-Supervised Learning</td><td>[73],(2023)</td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="6">Continual Pre-training</td><td>[257],(2019)</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td></tr><tr><td>[82],(2022)</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td></tr><tr><td>TADIL [84],(2023)</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td></tr><tr><td>[258],(2022)</td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td></td></tr><tr><td>AFEC [90],(2021)</td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td></td></tr><tr><td>CFN [99],(2020)</td><td></td><td></td><td></td><td></td><td></td><td>✓</td><td></td></tr><tr><td rowspan="13">Regularization</td><td></td><td>GPM [213],(2021)</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>[71],(2022)</td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>[259],(2022)</td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>[77],(2018)</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="6">Weight Regularization</td><td>[260],(2023)</td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>OGD [211],(2020)</td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TRGP [215],(2022)</td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td></td></tr><tr><td>OWM [210],(2019)</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASP [100],(2017)</td><td></td><td></td><td></td><td></td><td></td><td>✓</td><td></td></tr><tr><td>UCL [96],(2019)</td><td></td><td></td><td></td><td></td><td></td><td>✓</td><td></td></tr><tr><td rowspan="2">Function Regularization</td><td>HCL [80],(2021)</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td></tr><tr><td>SGP [261],(2023)</td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Distillation</td><td>[262],(2023)</td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="5">Replay</td><td rowspan="4">Experience Replay</td><td>[85],(2022)</td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td></td></tr><tr><td>[263],(2019)</td><td></td><td></td><td>+</td><td>✓</td><td>✓</td><td></td><td></td></tr><tr><td>MER [88],(2019)</td><td></td><td></td><td>+</td><td>✓</td><td>✓</td><td></td><td></td></tr><tr><td>GEM [89],(2017)</td><td></td><td></td><td></td><td>✓</td><td>✓</td><td></td><td></td></tr><tr><td>Generative</td><td>TAME [81],(2024)</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="5">Architecture</td><td rowspan="4">Model Decomposition</td><td>CN-DPM [79],(2020)</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td></tr><tr><td>DSSAE [83],(2023)</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td></tr><tr><td>P&amp;C [98],(2018)</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td>✓</td><td></td></tr><tr><td>CLNP [97],(2019)</td><td></td><td></td><td></td><td></td><td></td><td>✓</td><td></td></tr><tr><td>Allocation</td><td>AFAF [94],(2022)</td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td></td></tr></table>

[321], thereby leading to sub-optimal efficiency gains. To address this, CMOS-based neuromorphic hardware accelerators facilitate efficient spike transmission and computation [322], allowing their implementation in the Field-Programmable Gate Array (FPGA) or Application-Specific Integrated Circuit (ASIC). Popular accelerators include Neurogrid [323], ROLLS [324], TrueNorth [325], Loihi [326], DYNAP [327], and Akida [328], [329]. Their typical hardware architecture is shown in Fig. 15(a). Beyond CMOS-based technologies, the processing-in-memory (PIM) or compute-in-memory (CIM) paradigm has been explored to further reduce latency and energy in data transfer between memory and compute units [330], [331] by leveraging nonvolatile memory (NVM) technologies, such as Resistive Random Access Memory (RRAM), Magnetic RAM (MRAM), and Phase Change Memory (PCM) [332]. Their typical hardware architecture is shown in Fig. 15(b).

![](images/198b8d75be53b3c98aadf8dd01a253e333e5c7862f90b48ab0419c30c7e46f7d.jpg)

![](images/32af56b9437d2cb2f1e4ef9b433b93db4eb1e2a4380788b5fcabebf07e40a4b3.jpg)  
  
FIGURE 15. Neuromorphic processors: (a) CMOS-based HW architecture, and (b) NVM-based HW architecture; adapted from studies in [321].

# B. FRAMEWORK, DATASETS, BENCHMARKS, AND EVALUATION METRICS

The discussion in this section addresses the key questions Q4 and Q8.

# 1) FRAMEWORK

Recently, the SNN community has been building a framework for benchmarking neuromorphic algorithms and systems, so-called NeuroBench [333], encompassing datasets and metrics. Its algorithm-level metrics include correctness (e.g., mean average precision (mAP)) and complexity (e.g., memory footprint, synaptic operations, as well as model and activation sparsity). Meanwhile, its system-level metrics include task-specific correctness, timing, and efficiency. Despite these advancements, NeuroBench framework is

still under continuous development, and has not provided comprehensive benchmarks for NCL considering different CL settings and scenarios (see Section II-C and Section II-E). Therefore, a standardized framework for comprehensively benchmarking NCL is still missing, and requires extensive developments. Toward this, we propose to consider the following additional datasets, benchmarks, and evaluation metrics.

# 2) DATASETS & BENCHMARKS

Neuromorphic datasets play a crucial role in advancing the NC field, particularly in the training and evaluation of SNN models. These datasets are derived or generated to leverage the unique characteristics of event-based data. Some datasets are obtained using neuromorphic sensors, and some others are derived from existing conventional datasets. Neuromorphic datasets can be divided into three categories based on their acquisition methods, as the following.

1) Real-World Scene Datasets: They are collected directly from real-world environments using event-based sensors, such as Dynamic Vision Sensor (DVS) cameras. Consequently, these datasets are unlabeled until the labeling process is performed. For instance, the DVS-128 Gesture dataset [334] for gesture recognition is obtained using a DVS camera.   
2) Transformation Datasets: They are obtained by transforming the existing (labeled) datasets from the ANN domain through recordings with event-based sensors. An example for this category is the CIFAR10-DVS dataset [335]. These datasets are expected to leverage event-based data characteristics for SNNs, while having direct counterparts in the ANN domain for comparison, thereby making them popular for SNN evaluation.   
3) Algorithmically Generated Datasets: They are synthesized using algorithms that emulate the behavior of event-based sensors. They convert existing labeled image, video, or speech data into neuromorphic datasets using difference-based algorithms. An example for this category is the Spike-TIDIGITS [336].

Table 8 provides an elaborate comparison of the prominent neuromorphic datasets, including their publication year, characteristics, and tasks. Currently, they also serve as benchmarks for evaluating and comparing SNN models, including the NCL methods. However, these datasets are mainly for classification tasks, which limit the applicability of neuromorphic systems. Therefore, more diverse datasets are required including the types of tasks (e.g., regression and generative), diversity in conditions during data collection (e.g., weather, lighting, fog, etc.), and even diversity of application use-cases (e.g., vision, sound, tactile, and olfactory datasets). Moreover, benchmarks for NCL should also consider different possible CL settings (e.g., supervised, unsupervised, and RL) and scenarios (e.g., task-IL, domain-IL, and class-IL).

TABLE 6. Summary of ANN-based CL methods, outlining their computational/memory overhead.   

<table><tr><td>Approach</td><td>CL Method</td><td>Network/Model</td><td>Limitations</td></tr><tr><td rowspan="5">Regularization-based</td><td rowspan="5">EWC [70], SI [66], MAS [151], RWalk [105], R-EWC [154], XK-FAC [155], ALASSO [156], GD [166]</td><td>MLP, CNN</td><td>- Linearly increasing computations with the number of parameters and tasks due to Fisher Information Matrix (FIM) calculations.</td></tr><tr><td>LeNet, VGG-16</td><td>- High computations due to factorized rotation of the parameter space to diagonalize the FIM.</td></tr><tr><td>ResNet-18</td><td>- High computations due to the complexity of handling batch normalization.</td></tr><tr><td>ResNet-50</td><td>- High computations due to more accurate quadratic approximation of the loss function for improving performance.</td></tr><tr><td>ResNet-18</td><td>- High computations due to large-scale distillation over unlabeled data.</td></tr><tr><td rowspan="4">Replay-based</td><td rowspan="4">GEM [89], A-GEM [220], DGR [200], RAR [181], DGM [67], L-VAEGAN [21], EEC [203]</td><td>MLP, ResNet-18</td><td>- High computations and memory overhead during training due to the requirement for backward passes.</td></tr><tr><td>GAN, MLP, ResNet-18</td><td>- High computations due to adversarial training, high memory for storing and generating past data.</td></tr><tr><td>DCGAN, ResNet-18, VAE-GAN, DCGAN, ResNet-18</td><td>- High computations due to adversarial training with sparse attention masks.</td></tr><tr><td>- High computations due to combination of VAEs with GANs.</td><td>- High computations and memory overhead due to encoding and decoding of entire past episodes.</td></tr><tr><td rowspan="7">Representation-based</td><td rowspan="7">Co2L [122], DualNet [117] TwF [91], GAN-Memory [129], CODA-Prompt [132], S-Prompts [134], Barlow Twins + EWC [144]</td><td rowspan="7">ResNet-18, Two parallel CNNs ResNet-18, GAN, Vision Transformer (ViT), Transformer-based ResNet-50</td><td>- High computations due to contrastive learning.</td></tr><tr><td>- Memory overhead due to maintaining two networks.</td></tr><tr><td>- Memory overhead due to parallel networks.</td></tr><tr><td>- High computations due to generative modeling.</td></tr><tr><td>- High computations due to attention calculations of ViTs leading to quadratic complexity in terms of input size.</td></tr><tr><td>- High memory overhead as prompts grow with tasks.</td></tr><tr><td>- High computations due to quadratic penalty in EWC.</td></tr><tr><td rowspan="3">Architecture-based</td><td rowspan="3">PNN [92], PathNet [93], Model Zoo [244]</td><td rowspan="3">MLP, CNN CNN, Wide-Resnet</td><td>- Exponential memory increase due to new sub-networks added for new tasks.</td></tr><tr><td>- High computations due to multiple parallel networks.</td></tr><tr><td>- Linearly increasing memory due to a separate sub-network storage for each task, and ensemble of all sub-networks.</td></tr></table>

# 3) EVALUATION METRICS

Section II-D highlights the standard evaluation metrics including average accuracy, BWT and FWT, forgetting measure, model size, sample size, compute resources (e.g., FLOPS and time complexity), and power/energy efficiency. Therefore, they cover limited metrics for evaluating the functionality of different CL tasks. Moreover, the conventional metrics serve as indicators of a model’s ability to retain prior knowledge while learning new tasks sequentially. However, when applied to neuromorphic systems, these metrics must be reinterpreted and complemented due to the distinct computational paradigms inherent in such architectures, such as event-driven computation, quantized activations, low-precision operations, and temporal spikebased encoding. To address this, we reference works that propose complementary performance indicators and suggest new metrics as follows.

• Performance: In spike-based systems, processing time often relies on the neural coding (e.g., rate, TTFS, etc.). Therefore, latency (measured in time steps until a decision is made) and throughput becomes a critical indicator of performance of low-power or real-time applications [337].   
• Efficiency: Power and energy consumption during CL training and inference are important to indicate the energy efficiency of NCL. For estimation, spike count and membrane potential dynamics may also provide crucial insights into the energy efficiency [42]. Further-

more, utilization of memory bandwidth and compute module, as well as synaptic operation rates (SOPS) are also relevant for indicating efficiency when running networks on neuromorphic chips. NCL systems that maintain accuracy with high efficiency are preferred for embedded AI deployments.

• Robustness: Neuromorphic systems may exhibit variability due to low-bit precision, noisy spikes, and device-level process variations. Therefore, robustness (defined as accuracy maintained under noise, perturbations, or quantization) emerges as a meaningful metric besides accuracy.   
• Task-specific functionality metrics: They depend on the type of task. For instance, mean absolute error (MAE) and mean square error (MSE) can be used for regressionbased tasks.   
• Memory ratio: It represents how much memory overhead compared to the original model size, that is needed to execute the implemented CL method.   
• Adaptability scores: They represent how effective is the implemented CL method over time considering different CL scenarios i.e., task-IL, class-IL, domain-IL, TA etc.

# C. NEUROMORPHIC CONTINUAL LEARNING (NCL)

The integration of CL with neuromorphic computing (i.e., NCL) is the central focus of the paper. Specifically, how NCL facilitates continual adaptation in diverse operational environments by leveraging key characteristics of neuromorphic

TABLE 7. Comparison of neuromorphic, standard DL and CL frameworks.   

<table><tr><td rowspan="2">Frameworks</td><td colspan="3">Learning Mechanism</td><td rowspan="2">CL Support</td><td rowspan="2">Hardware Support</td><td rowspan="2">Flexibility and Usability</td><td rowspan="2">PyTorch-based</td><td rowspan="2">Computational Efficiency</td></tr><tr><td>Unsupervised</td><td>Supervised</td><td>Hybrid</td></tr><tr><td colspan="9">Neuromorphic Frameworks</td></tr><tr><td>SpikingJelly [303]</td><td>STDP, Hebbian Learning</td><td>BPTT, SG</td><td>RL</td><td>✓</td><td>CPU, GPU, Neuromorphic chips</td><td>High</td><td>✓</td><td>High</td></tr><tr><td>BindsNet [304]</td><td>STDP, Hebbian Learning</td><td>×</td><td>RL</td><td>×</td><td>CPU, GPU</td><td>Medium</td><td>✓</td><td>Moderate</td></tr><tr><td>SNNtorch [305]</td><td>STDP</td><td>BPTT, SG</td><td>×</td><td>×</td><td>CPU, GPU</td><td>High</td><td>✓</td><td>High</td></tr><tr><td>TinySpiking [306]</td><td>STDP</td><td>×</td><td>×</td><td>×</td><td>CPU, MCU</td><td>High</td><td>Python-Based</td><td>High</td></tr><tr><td>Norse [307]</td><td>STDP, Hebbian Learning</td><td>BPTT, SG</td><td>RL</td><td>×</td><td>CPU, GPU</td><td>High</td><td>✓</td><td>High</td></tr><tr><td>SpyTorch [308]</td><td>STDP</td><td>×</td><td>×</td><td>×</td><td>CPU, GPU</td><td>Medium</td><td>✓</td><td>Moderate</td></tr><tr><td>SINABS [309]</td><td>STDP</td><td>BP</td><td>×</td><td>×</td><td>Neuromorphic chips</td><td>Medium</td><td>✓</td><td>High</td></tr><tr><td>SpykeTorch [310]</td><td>STDP, R-STDP</td><td>×</td><td>×</td><td>×</td><td>CPU, GPU</td><td>Medium</td><td>Python-Based</td><td>Moderate</td></tr><tr><td>Brian [311]</td><td>STDP, Hebbian Learning</td><td>×</td><td>×</td><td>×</td><td>CPU</td><td>Medium</td><td>Python-Based</td><td>Moderate</td></tr><tr><td>Lava [312]</td><td>STDP, Hebbian Learning</td><td>×</td><td>RL</td><td>×</td><td>Neuromorphic chips</td><td>Medium</td><td>Python-Based</td><td>High</td></tr><tr><td>BrainCog [313]</td><td>STDP, Hebbian Learning</td><td>BPTT, SG</td><td>RL</td><td>✓</td><td>CPU, GPU, Neuromorphic chips</td><td>High</td><td>✓</td><td>High</td></tr><tr><td>PySNN [314]</td><td>STDP</td><td>SG</td><td>×</td><td>×</td><td>CPU, GPU</td><td>Medium</td><td>✓</td><td>High</td></tr><tr><td>PyNCS [315]</td><td>STDP, Hebbian Learning</td><td>×</td><td>×</td><td>×</td><td>Neuromorphic chips</td><td>Medium</td><td>Python-Based</td><td>Moderate</td></tr><tr><td colspan="9">Standard DL Frameworks</td></tr><tr><td>TensorFlow [316]</td><td>×</td><td>BP</td><td>RL</td><td>✓</td><td>CPU, GPU, TPU</td><td>Very High</td><td>Python-Based</td><td>Relatively low</td></tr><tr><td>PyTorch [317]</td><td>×</td><td>BP</td><td>RL</td><td>✓</td><td>CPU, GPU</td><td>Very High</td><td>✓</td><td>Relatively low</td></tr><tr><td colspan="9">CL Frameworks</td></tr><tr><td>PyCIL [318]</td><td>×</td><td>BP</td><td>RL</td><td>✓</td><td>CPU, GPU</td><td>High</td><td>✓</td><td>Relatively low</td></tr><tr><td>FACIL [47]</td><td>×</td><td>BP, SG</td><td>×</td><td>✓</td><td>CPU, GPU</td><td>High</td><td>✓</td><td>Relatively low</td></tr><tr><td>Avalanche [319]</td><td>×</td><td>BP</td><td>RL</td><td>✓</td><td>CPU, GPU</td><td>High</td><td>✓</td><td>Relatively low</td></tr></table>

systems that align with CL requirements, as highlighted in the following.

• Neural plasticity: It is established using bio-plausible learning rules, such as Hebbian rule and Spike-Timing Dependent Plasticity (STDP), which enable SNNs to flexibly learn new information while preserving prior knowledge (e.g., through weight potentiation and depression), which is useful for addressing CF problem.   
• Localized learning in each synapse: Bio-plausible learning rules in SNNs can leverage spiking activities for updating weight locally in each synapse. It is useful for learning information without explicit labels, which is required for enabling online training in updating systems’ knowledge and adapting to dynamic environments.

• Event-based processing: The event-driven operations in SNNs consider both spatial and temporal information in the event-based data streams, which aligns with the nature of dynamic data streams in CL. This potentially streamlines the execution of CL algorithms.   
• Energy-efficient computation: The event-driven operations in SNNs and neuromorphic hardware enable ultralow power/energy computation, which is required for enabling CL execution in tightly-constrained systems.

# D. NCL METHODS

In this sub-section, we provide an in-depth review of stateof-the-art NCL methods, including their key ideas and techniques, whose details are summarized in Table 9. Fig. 16 presents the taxonomy that systematically categorizes these methods based on their specific techniques. This discussion also addresses the key question Q6.

TABLE 8. Comparison of widely used neuromorphic datasets for SNNs with their publication year, description, key features and tasks.   

<table><tr><td>Dataset</td><td>Year</td><td>Description</td><td>Key Features</td><td>Tasks</td></tr><tr><td>N-MNIST [338]</td><td>2015</td><td>An event-based version of the MNIST dataset captured using Asynchronous Time-based Image Sensor (ATIS) with each digit recorded over 300 ms</td><td>Classes: 10 Resolution: 28x28 Training Samples: 60,000 Testing Samples: 10,000</td><td>Digit Classification</td></tr><tr><td>DVS-128 Gesture [334]</td><td>2017</td><td>An event-driven data of hand and arm gestures captured using DVS128 cameras, focusing on dynamic movement with 6s/sample duration</td><td>Classes: 11 Subjects: 29 Illumination conditions: 3 Resolution: 128x128</td><td>Gesture Recognition</td></tr><tr><td>CIFAR10-DVS [335]</td><td>2017</td><td>An event-based version of CIFAR-10 dataset with 300ms/sample duration</td><td>Classes: 10 &amp; Event streams: 10,000 Resolution: 128x128</td><td>Image Classification</td></tr><tr><td>N-Caltech101 [338]</td><td>2015</td><td>A spiking version of the original frame-based Caltech101 dataset with 300-500ms/sample duration</td><td>Samples: 8709 Classes: 100 objects, and a background class</td><td>Object Recognition</td></tr><tr><td>N-CARS [339]</td><td>2018</td><td>A large real-world event-based dataset captured using ATIS camera with 100ms/sample duration</td><td>Classes: 2 Samples of Car: 12,336 &amp; Background: 11,693 Training Samples: 7940 (car), 7482 (bg) Testing Samples: 4396 (car), 4211 (bg)</td><td>Car &amp; Background Recognition</td></tr><tr><td>N-Omniglot [340]</td><td>2022</td><td>A large-scale neuromorphic dataset of handwritten characters, representing 50 different languages captured by DVS</td><td>Classes: 1,623 Samples per class: 20 Samples: 32,460</td><td>Few-Shot Learning in SNNs</td></tr><tr><td>Spiking Heidelberg Digits (SHD) [341]</td><td>2022</td><td>An audio-based dataset of 10k high-quality recordings of spoken digits ranging from zero to nine in English and German</td><td>Classes: 10 Digit Count: 10,420 Speakers: 12</td><td>Speech Classification and Keyword Spotting</td></tr><tr><td>ES-ImageNet [342]</td><td>2021</td><td>A large-scale event-stream dataset converted from the ImageNet dataset [343] using a software-based event generation Omnidirectional Discrete Gradient (ODG) algorithm with 29.47ms/sample duration</td><td>Classes: 1000 Training Samples: 1,257,035 Testing Samples: 49,881 Total Samples: 1.3 M Resolution: 224x224*</td><td>Image Classification</td></tr><tr><td>SpikeBALL [344]</td><td>2023</td><td>A neuromorphic dataset capturing 10 different trajectories of a ball in a table football game</td><td>Class: 1 Events: 80,000 to 100,000 per trajectory</td><td>Object Tracking</td></tr><tr><td>NE15-MNIST [345]</td><td>2016</td><td>A spiking version of MNIST dataset with four sub-datasets encoded using: Poissonian, Rank-Order, DVS recorded flashing and DVS recorded moving</td><td>Classes: 10 Training Samples: 60,000 Testing Samples: 10,000</td><td>Visual Recognition</td></tr><tr><td>ASL-DVS [346]</td><td>2019</td><td>Event-driven data of 24 letters (A-Y, excl. J) from American sign language recorded using DAVIS240c NVS camera with 100ms/sample duration</td><td>Classes: 24 Samples: 100,800 / Samples per-class: 4,200 Training Samples: 80,640 Testing Samples: 20,160</td><td>Sign Language Recognition</td></tr><tr><td>N-TIDIGITS18 [347]</td><td>2018</td><td>The spike recordings from a Dynamic Audio Sensor (DAS) in response to the TIDIGITS audio dataset</td><td>Classes: 11 Training Samples: 8,623 Testing Samples: 8,700</td><td>Spoken Digit Recognition [348]</td></tr><tr><td>Spike-TIDIGITS [336]</td><td>2020</td><td>A Spike-based version of TIDIGITS dataset created using the Biologically Plausible Auditory Encoding (BAE) algorithm</td><td>Classes: 11 Training Samples: 2464 Testing Samples: 2486</td><td>Speech Recognition</td></tr><tr><td>Spike-TIMIT [336]</td><td>2020</td><td>An event-based version of TIMIT dataset [349]</td><td>Training Samples: 4621 Testing Samples: 1679</td><td>Audio Classification</td></tr><tr><td>DVS Lane Extraction (DET) [350]</td><td>2019</td><td>A high-resolution event-based dataset of complex traffic scenes and various lane types annotated with multi-class segmentation captured by CeleX-V DVS</td><td>Classes: 5, (0 for bg and 1,2,3,4 for four lane types) Images: 5,424 Resolution: 1280x800</td><td>Lane Extraction</td></tr><tr><td>KUL-UAVSAFE [351]</td><td>2021</td><td>A joint DVS and RGB dataset in an indoor environment with one walking human</td><td>Subjects: 6 &amp; Variations: Clothes color, shape &amp; walking style</td><td>People Detection</td></tr></table>

*Eventsaregeeiitleul motion; bg: background.

1) ENHANCEMENTS ON UNSUPERVISED STDP LEARNING While conventional STDP enables efficient online unsupervised learning, employing STDP alone may still suffer from

CF [42], [43]. To address these challenges, several techniques have been proposed in the literature, as discussed in the following.

![](images/b3212ae41d29a84fa0bff1c7e715437fc7b3e5aa6162d4c17bfd357d80cff1b9.jpg)  
FIGURE 16. A state-of-the-art taxonomy of NCL methods covered in this survey. We have highlighted the main categories (blue blocks), with each of their works shown (red blocks).

# a: WEIGHT DECAY

It prevents overfitting in NNs by penalizing large weight values by adding a regularization term, which encourages the model to keep the weights small. For instance, Adaptive Synaptic Plasticity (ASP) [100], SpikeDyn [42] and lpSpikeCon [43] leak the weights to gradually remove old and insignificant information and ensure the weights do not grow too large.

# b: ADAPTIVE THRESHOLD POTENTIAL

It refers to the dynamic adjustment of the neurons’ threshold based on its spiking activity. It allows neurons to adapt their sensitivity to incoming spikes, making the network more flexible/robust in processing information. A neuron typically fires when its membrane potential exceeds a pre-defined threshold. However, in an adaptive threshold model (as employed by SpikeDyn [42] and lpSpike-Con [43]), the threshold changes based on the neurons’ recent activity, thus helping the neuron provide the following features.

1) Regulating the firing rates to prevent excessive firing and maintain a stable firing rate over time to avoid overactive neurons (homeostasis) [264], [266].   
2) Leveraging the temporal information to improve the neurons’ capability to respond to varying input patterns.   
3) Improving the signal-to-noise ratio (SNR), by separating the significant input patterns from the noise.

# c: ADAPTIVE LEARNING RATE

It dynamically adjusts the learning rate in training to improve convergence. The learning rate controls how much the models’ weights are updated. ASP [100], SpikeDyn [42] and lpSpikeCon [43] employ adaptive learning rates to determine the potentiation and depression factors in the STDP-based learning based on the spiking activities. By prioritizing the adjustment of highly active synapses, it enhances learning efficiency and reduces unnecessary energy expenditure on less active connections. This selective learning process mimics biological synaptic behavior.

These techniques are often employed together in NCL methods as discussed below.

# d: ADAPTIVE SYNAPTIC PLASTICITY (ASP) [100]

It integrates weight decay with the STDP-based weight updates to balance forgetting and learning, while leveraging time-dependent learning rate. ASP uses a two-phase weight update process (i.e., recovery and decay), allowing weight updates based on spiking activities and gradually leak toward a baseline value; see Fig. 17. The SNN was implemented in Brian [311], (a lightweight SNN simulator for rapid prototyping and experimentation with a flexible Python interface), to perform dynamic digit recognition with the MNIST dataset. The digit categories ’0’ to ’9’ were presented sequentially, without intermixing at any point during the training phase (i.e., no data reinforcement). For a 6400 neuron SNN, ASP achieved avg. accuracy of 94.2% outperforming the standard STDP. A summary is presented in Table 9 and the empirical results are shown in Table 11 and Table 12, providing a comparative analysis in terms of network architecture, size and key performance metrics such as accuracy, memory footprint, and power/energy consumption of the reviewed works. Despite its strengths, ASP requires larger quantities of input samples from earlier distributions than later ones, hence requiring the knowledge of task changes [99], making it unsuitable for OCL scenario.

![](images/9ea600ea011be4aae83ffab3c5012f9aaece406f67f4f0413398f38d5cc520e3.jpg)

![](images/46576f1d893eb1148ec47031c5a5eebf0d19916e707b9c27dba3932e41f37444.jpg)  
FIGURE 17. Weight update process of ASP; adapted from studies in [100]. More frequent input spikes represent common features between old and new input patterns, and will experience a greater weight update compared to less frequent spikes, that correspond to unique features of a specific input.

# e: CONTROLLED FORGETTING NETWORK (CFN) [99]

It is an SNN architecture that exploits dopaminergic neurons to modulate the synaptic plasticity. Its idea is to temporarily

make the weights of some neurons more plastic (easier to change) and keep the weights of other neurons. The modulation is triggered by dopaminergic neurons, which fire when there are no or only a small number of incoming inhibitory spikes (indicating that new information is encountered), and then stimulate a temporary boost of learning rate for other neurons (Fig. 18). For a 6,400 neuron CFN, the evaluations on MNIST dataset in a fully disjoint scenario, achieved on average 95.24% classification accuracy across all digits (see summary in Table 9 and the comparative empirical analysis in Table 11 and Table 12). Despite its benefits, CFN requires additional components (i.e., dopaminergic neurons and their connections) and considers a conventional CL scenario (i.e., temporally separated tasks), which makes it challenging for deployments in an environment of changing priorities, i.e., OCL scenario.

![](images/18d8f924bfe7a0dd9ae51966c2c2faa92d5a5dcd51bea0e5e5ee564108bcf11e.jpg)  
FIGURE 18. Single-layer CFN architecture; adapted from studies in [99]. The dopaminergic neuron activates when other neurons in its layer are inactive, indicating new information in the input. This activation temporarily enhances plasticity in other neurons. Dopaminergic signals are weighted to provide targeted stimulation.

# f: SPIKEDYN [42]

It focuses on enhancing STDP for enabling unsupervised CL while minimizing energy consumption in both training and inference phases (Fig. 19). Its key ideas include: reduction of neuronal operations by substituting the inhibitory neurons with direct lateral inhibitions to reduce memory and energy requirements; enhancing unsupervised CL algorithm by employing adaptive learning rates, weight decay, adaptive threshold potential, and reduction of spurious weight updates; and SNN model size search by leveraging analytical models to estimate the memory and energy requirements, and selecting a Pareto-optimal model that meets the resource constraints. The SNN was implemented using Bindsnet, a ML-oriented SNN library in Python [304]. Evaluations on MNIST dataset in a dynamic environment (where tasks are fed sequentially, without re-feeding earlier ones, and each task contains an equal number of samples), for a 200 neuron SNN, showed avg. 23% and 4% improved accuracy than ASP [100] when learning a new task and when retaining the old task, respectively. It also reduced energy consumption by up to

avg. 57% and 51% for training and inference, respectively (see summary in Table 9 and the comparative empirical analysis in Table 11 and Table 12). SpikeDyn demonstrated that optimization techniques can be exploited to minimize memory and energy requirements of CL systems, but they should be supported with an enhanced unsupervised CL algorithm to maintain the performance.

![](images/3aee811e1934ded986b780c06fd76e3178d0f882fc7dcc1933acd608e25dcf2d.jpg)  
FIGURE 19. SpikeDyn framework for adaptive and energy-efficient unsupervised CL for SNNs; adapted from studies in [42].

# g: LPSPIKECON [43]

It extends the studies in SpikeDyn [42], by enabling STDPbased unsupervised CL under low-precision settings for embedded AI systems (e.g., robots). lpSpikeCon employs weight quantization and compensates the loss of information by identifying and adjusting SNN parameters that significantly impact accuracy (Fig. 20). The SNN was implemented using Bindsnet [304], see Table 7. It performed a case study in a dynamic CL scenario using the MNIST dataset. The network was trained sequentially on digit classes from 0 to 9, receiving one class at a time. After each training phase, the model was evaluated on the test samples of all classes learned so far, simulating a real-time CL process. The 4- bit weight quantized SNN with key parameter adjustments showed no accuracy loss in the inference while reducing the weight memory by 8x compared to 32-bit non-quantized SNN (see summary in Table 9 and comparative empirical analysis in Table 11 and Table 12). This study found that the key SNN parameters to adjust include the adaptive threshold potential and weight decay rate. This study demonstrated that low-precision settings can be exploited for substantially reducing memory and energy requirements, and adjustments of other parameters are crucial to maintain the performance. Despite their promising results, SpikeDyn and lpSpikeCon have so far focused on the MNIST dataset and conventional CL scenario. Expanding these methods to more complex scenarios for OCL is a potential future research direction.

# 2) PREDICTIVE CODING

This method is used by the Spiking Neural Coding Network (SpNCN) [301] to predict incoming data and then correct the prediction based on the actual inputs [352], [353]; see

![](images/bdff027e0b7a4675818e12aab26cf70efc8c82156784a7dc71d7c9793acfc397.jpg)  
FIGURE 20. Key steps of lpSpikeCon methodology for low-precision unsupervised CL for SNNs; adapted from studies in [43].

![](images/4224633ad023522a926b1dc326f205b1def3434a1aaa4c93b405e60ff599d14d.jpg)  
Fig. 21. This iterative process of ‘‘guess-and-check’’ allows the network to adjust its weights continually and learn from data streams without repeated exposure to same data. Key ideas of SpNCN are as follows.   
FIGURE 21. A 2-layer SpNCN with error units (blue diamonds) that measure the difference between predictions $( z _ { \mu } ^ { 0 } , z _ { \mu } ^ { 1 } )$ and target signals $( z ^ { 0 } ( t ) , z ^ { 1 } ( t ) )$ . Variables $s ^ { 0 } ( t ) , s ^ { 1 } ( t )$ are the binary spike outputs of neuron groups at time t. Black dash-dotted arrows show the repeated transmission of the last known values. Mismatch signals, shown by green dashed arcs, adjust the spiking neuron’s action potentials through synapses. Solid black lines show predictive synapses, and black dotted lines show direct information transfer; adapted from studies in [301].

• Prediction of neuron activity and error correction using local synaptic updates.   
• Weight adaptation using a coordinated ST-LRA, which adjusts weights based on the mismatch between predictions and actual activity. It is also combined with STDP as regularizer.   
• A memory module and task/context-modulated lateral inhibition to enhance memory retention across tasks.

A case study was conducted using adapted versions of standard CL benchmarks, i.e., Split MNIST, Split NotM-NIST, and Split Fashion MNIST (FMNIST), in a spike-train continuous-time setting. Each dataset was partitioned into five sequential tasks, where each task involved classifying two object categories (e.g., digit pairs in Split MNIST, letters A–J in NotMNIST, or clothing types in FMNIST). The tasks were presented in a fixed sequence, simulating a dynamic CL scenario where the learner must adapt to new tasks while retaining prior knowledge, despite changes in the label distribution that create cross-task interference. Experimental results showed normalized accuracy of 0.9653 on MNIST, 0.9120 on Not-MNIST and 0.9995 on FMNIST (see summary in Table 9 and comparative empirical analysis in Table 11 and Table 12). This study showed that combination of learning rules is potential for enabling CL. However,

this complex combination of multiple learning rules make it challenging for deployments under OCL scenario.

# 3) ACTIVE DENDRITES

Studies in [354] proposed an SNN model leveraging active dendrites [355] to facilitate task-specific sub-network formation (Fig. 22). The spike time $t _ { j }$ of a neuron is modulated by a function of the selected dendritic segment $u _ { j n }$ for the current task. The dendritic activation function f (u) modulates the spike time dynamically, allowing the model to adapt its behavior based on the task context. It also leverages TTFS encoding to introduce a gating mechanism, that enables selection of sub-networks for various tasks. Experimental results on the Split MNIST dataset for sequential CL tasks demonstrated an end-of-training accuracy of 88.3%. Moreover, the FPGA implementation matched the quantized software model with an average inference time of 37.3ms and an accuracy of 80.0%, highlighting the potential for applications in resource-constrained environments (see summary in Table 9 and comparative empirical analysis in Table 11 and Table 12). However, this method requires labeled data or supervisory signals, hence making it challenging for deployments under the OCL scenario.

![](images/4bbbb5bf1d7fb88902ed6611603b53277adbaf3da4be57b229f94986d046e7ec.jpg)  
FIGURE 22. Neuron model and network architecture with active dendrites; adapted from studies in [354]. (a) Linear integration of synaptic strength ${ \pmb w } _ { i j }$ following a pre-synaptic spike at $\mathbf { \Delta } _ { t _ { j } } \mathbf { : }$ Top figure shows the ij imodulation of spike timing by dendritic processes. (b) Illustration of a pyramidal neuron. (c) Selection of different sub-networks for various tasks based on dendritic segment activity. (d) Proposed neuron model and dendritic activation function.

# 4) BAYESIAN CONTINUAL LEARNING

This method represents weights with parameters that quantify the epistemic uncertainty based on prior knowledge and observed data, and employs Bayesian methods for handling uncertainty over time by determining which knowledge to retain and which to forget [302] (Fig. 23). For real-valued synapses, it uses a Gaussian variational distribution to adjust the values; while for binary synapses, it uses a Bernoulli variational distribution with Gumbel-softmax [356]. The work was implemented using Intel’s Lava platform [312],

enabling Bayesian CL in SNNs, see Table 7. Experimental results achieved avg. test accuracy of $8 5 . 4 4 \pm 0 . 1 6 \%$ with 5× memory reduction on Split-MNIST and 74% for MNIST-DVS (see summary in Table 9 and comparative empirical analysis in Table 11 and Table 12). Although, this method provides better-calibrated decisions and better detection compared to conventional frequentist approaches [357], the uncertainty quantification incurs high computational complexity, thereby making it challenging for deployments in OCL scenario.

![](images/51640dcd2727c30455316c3f146f968b8c56f306a198ca487660f52f6f0240c8.jpg)  
FIGURE 23. In the Bayesian continual learning, the system is sequentially presented with similar yet distinct tasks; adapted from studies in [302].

# 5) ARCHITECTURE-BASED APPROACH

Dynamic Structure Development of Spiking Neural Networks (DSD-SNN) enhances the SNN structure by growing new neurons for new tasks and pruning redundant neurons [358] (Fig. 24). It employs a deep SNN architecture comprising of multiple convolutional (CONV) and fullyconnected (FC) layers, which is equipped with random growth, adaptive pruning, and freezing of neuron mechanisms. This SNN was implemented using the Brain-inspired Cognitive intelligence engine (BrainCog) [313], see Table 7 for details. Experimental results on the MNIST dataset in Task-IL scenario, demonstrated an accuracy of $9 7 . 3 0 \ \pm $ 0.09% with a network parameter compression rate of 34.38%, outperforming the EWC, GEM and DEN DNN-based CL methods. Furthermore, an accuracy of $9 6 . 9 4 \pm 0 . 0 5 \%$ was reported for the N-MNIST and $7 7 . 9 2 \% \pm 0 . 2 9$ in Task-IL and 60.47% (10 steps) in Class-IL scenario for the CIFAR100 dataset (see summary in Table 9 and comparative empirical analysis in Table 11 and Table 12). This study advanced multi-task learning while enhancing memory capacity and efficiency. However, the development of dynamic structure adds complexity to SNN implementation, which is challenging for OCL scenario.

Self-Organized Regulation SNN (SOR-SNN) employs a pathway search module to adaptively activate task-specific sparse neural pathways based on fundamental weights Wt [359] (Fig. 25). Each synapse has two states (i.e., active and inactive), and is determined by learnable synaptic selection parameters. The model decides whether to activate or inhibit each weight by comparing the learnable parameter $A _ { s }$ with the threshold ${ \tilde { A } } _ { s } ,$ where activation is preferred if $A _ { s } > \tilde { A } _ { s }$ . The experimental results on the CIFAR100 dataset in Class-IL scenario demonstrated an average accuracy of

![](images/2531419fc7626dfb6981732821bdb6a47ebf6943e16cad153c235b9aa0dd7a3b.jpg)  
FIGURE 24. Deep SNN architecture with dynamic structure development; adapted from studies in [358].

$8 6 . 6 5 \% \pm \ : 0 . 2 0$ for 20 steps, where each task contains 5 classes and an accuracy improvement of 2.20% compared to the DSD-SNN. Moreover, on the Mini-ImageNet dataset, it reported > 55% accuracy, higher than the existing studies (see summary in Table 9 and comparative empirical analysis in Table 11 and Table 12). This study showed that SOR-SNN enables adaptive reorganization, BWT, and selfrepair capabilities. Despite its benefits, this method requires complex dynamic connectivity capabilities, hence making it challenging for deployments under OCL scenario.

![](images/579ab962011e4c60c2d4f4cab1e9b4f8150ac818655d7527fe430297ef15cc22.jpg)  
FIGURE 25. The process of SOR-SNN model; adapted from the studies in [359]. Each SNN block includes a self-organizing regulation network which selectively activates task-specific sparse pathways. For instance, the purple connections represent the pathway for Task 1. The numerous combinations of connections enable the limited SNN to incrementally learn a larger number of tasks.

# 6) REHEARSAL/REPLAY-BASED APPROACH

A memory replay approach using ER method has been developed, where a CSNN is trained to learn in Class-IL and TA scenarios [360]. For resource-constrained devices, the memory-efficient Latent Replay (LR)-based method has been developed, which stores compressed data representations [297]. The Latent Replay training involves a pre-training phase, where SNN is divided into two parts i.e., frozen and learning layers. The network stores latent replays for memory, and only trains the learning layers on new data. Here, the main challenges are related to the efficient store-load mechanisms for replay data under OCL

scenario. The implementations are based on the Python framework. Experimental results on SHD dataset showcased a Top-1 accuracy of 92% in the CLass-IL scenario and a memory-accuracy trade-off with only 4% accuracy drop due to compression. Unlike prior method [297] that rely on long timesteps and compression-decompression for accuracy, Replay4NCL [361] advances NCL for embedded AI systems by significantly reducing latency and energy consumption. It compressed latent data and replayed it with fewer timesteps during NCL training. Parameter adjustments (e.g., neuron thresholds, learning rate) compensated for reduced spikes. The SNN (Fig. 26) was implemented in Python in a Class-IL scenario with 19 tasks for pre-training and a 20th task for CL. Evaluations on the SHD dataset demonstrated 90.43% accuracy compared to 86.22% of the baseline [297] at layer 3, with 4.88× speed-up, 20% latent memory saving, and 36.43% energy savings (see summary in Table 9 and comparative empirical analysis in Table 11 and Table 12).

![](images/8397dfa788e8d79c9ec15d72b75e30118fddf57d5e9debd430c230765efe0090.jpg)  
FIGURE 26. (a) SNN architecture with recurrent neurons and latent replay (LR) and (b) configuration of current activation data and LR data [361].

# 7) REGULARIZATION-BASED APPROACH

This approach employs regularization terms to balance the old and new tasks, such as Noise Regularization [362], Freezing Large Weights, and Stochastic Langevin Dynamics [292]. For instance, Langevin Dynamics exploit the fact that each weight $w _ { i }$ can vary without impacting the accuracy in the domain $D _ { i }$ if constrained to a specific space when learning new tasks; see Fig. 27. The SNN was implemented in SpykeTorch [310], an open-source PyTorch-based framework supporting non-leaky IF neurons and local learning rules like STDP and R-STDP, see Table 7. The experiments were performed in a Task-IL scenario using the MNIST dataset (i.e., Task1) for initial training in a layer-by-layer training approach, where layer-S1 and layer-S2 were trained using STDP, while the final layer-S3 was trained with R-STDP. The Extended MNIST (EMNIST) dataset containing both

letters and digits was then used for subsequent training (i.e., Task 2), assuming MNIST data is not available. The classification accuracy for digits reached $9 2 . 0 ~ \pm ~ 0 . 1 \%$ and for letters it reached $7 9 . 7 \pm 0 . 5 \%$ (see summary in Table 9 and comparative empirical analysis in Table 11 and Table 12). This study highlighted that Langevin dynamics can exhibit very similar performance as the replay-based methods while being less memory-intensive. However, its compute requirements are relatively high, thus requiring further studies for OCL scenario.

![](images/0f6805d210d106388f261369a43a6217424612309b479c8ce651566b7b0e17fa.jpg)  
FIGURE 27. The effective potential force field (U∗) created by the R-STDP mechanism, which prevents the Brownian motion (represented by the dashed line) from leaving the optimal weight domain D; adapted from studies in [292].

# 8) HEBBIAN LEARNING

Hebbian Learning-based Orthogonal Projection (HLOP) method leverages lateral connections and Hebbian learning to achieve CL [363]. It employs orthogonal gradient projection to modify pre-synaptic activity traces (Fig. 28) to ensure that weight updates for new tasks do not interfere with the weights associated with the old tasks. Hebbian learning is useful to extract the principal subspace of neural activities, and updates synaptic weights based on the correlation between pre- and post-synaptic neuron activities, while the activity traces are updated using lateral signals. The implementations are based on the PyTorch framework [317]. Experimental results on various datasets and scenarios, including Permuted MNIST (PMNIST), CIFAR-100, and a combination of datasets like CIFAR-10, MNIST, SVHN, Fashion MNIST, and notM NIST, demonstrated higher accuracy such as 95.15% for PMNIST and lower forgetting (i.e., BWT) across different training methods like Dynamic Spike Representation (DSR), BPTT with SG, and Online Training Through Time (OTTT). HLOP also showcased superior performance compared to DNN-based methods such as EWC, HAT, and GPM highlighting its potential for robust NCL (see summary in Table 9 and comparative empirical analysis in Table 11 and Table 12).

# E. HYBRID LEARNING PARADIGMS

The scalability of most NCL methods to complicated problems with many tasks or complex inputs is challenging.

![](images/58051c93a7018222e7bf792f2b7635f63032dad83c6d3521944e981c699454f2.jpg)  
FIGURE 28. An illustration of the HLOP; adapted from studies in [363]. (a) Overview of the method. (b) Skew-symmetric connection weights in lateral circuits. (c) Construction of new subspaces for new tasks with Hebbian learning in lateral circuits. (d) Recurrent lateral connections based orthogonal projection.

In this section, we explore hybrid approaches that combine supervised and unsupervised learning paradigms to address CF and improve CL performance. We categorize these approaches into three main classes: 1) self-supervised pretraining hybrids, 2) STDP + supervised learning hybrids, and 3) generative-discriminative hybrid models; see Fig. 29.

![](images/9e870eee2da7356dcd70bc6b65860f5fecd897beb37e3b434cf04792c02ee9d2.jpg)  
FIGURE 29. A taxonomy of hybrid approaches combining supervised and unsupervised learning paradigms. We have highlighted the main categories (blue blocks), with their works shown (red blocks).

# 1) SELF-SUPERVISED PRE-TRAINING HYBRID

Cortico-Hippocampal Hybrid Networks (CH-HNN) [372] integrated ANNs for generalization and SNNs for specific memory encoding, inspired by dual-memory corticohippocampal circuits. It employed ANN-guided episode inference and metaplasticity with SG training to dynamically regulate synaptic plasticity. CH-HNN was validated in two robotic case studies: a Unitree GO1 robot performed real-time MNIST digit recognition using ANN-SNN inference, and a Unitree Z1 arm achieved 82±7.25% accuracy in sCIFAR-100 object grasping using YOLO. Across benchmarks like split MNIST, pMNIST, sCIFAR-100, sTiny-ImageNet (70.72% accuracy), and DVS Gesture, CH-HNN outperformed EWC, SI, XdG, iCaRL, and FOS-TER in stability-plasticity balance, disparity, and efficiency. For neuromorphic deployment, int8 quantization incurred minimal loss, with SNNs yielding 60.82% power savings over ANNs. Although CH-HNN supports various spiking neuron models, their selection involves trade-offs between

computational cost, biological fidelity, and deployment efficiency.

# 2) STDP + SUPERVISED LEARNING

The study in [373] integrated ANN-to-SNN conversion with STDB to converge to optimal accuracy in fewer epochs compared to training from scratch. Evaluations on image classification tasks using CIFAR-10, CIFAR-100, and ImageNet for VGG and ResNet architectures showed that SNNs trained with the hybrid method required significantly fewer time steps (10 × −25× fewer) to achieve competitive accuracy compared to purely converted SNNs. For instance, the model achieved a top-1 accuracy of 65.19% on the ImageNet dataset using only 250 time steps. Although, the study showed promise, the inherent challenges of converting SNNs, such as their non-differentiable nature, still pose difficulties that may affect broader applicability.

# 3) GENERATIVE-DISCRIMINATIVE HYBRID MODELS

SpikeGAN [374] is a hybrid generative model that combined an SNN generator with an ANN discriminator to learn and generate temporal spiking data distributions. The SNN generator captured spatio-temporal patterns, while the ANN discriminator enabled adversarial training akin to standard GANs. Bayesian learning was applied to the generator’s weights, and a continual meta-learning framework supported adaptation to multiple real-world distributions. Evaluated on handwritten digit generation, SpikeGAN outperformed ANN classifier accuracy by 20% and enabled SNN classifiers trained on synthetic data to match the performance of those trained on real rate-encoded inputs. The model leveraged the complementary strengths of ANNs and SNNs; however, it may suffer from sample space coverage issues, as indicated by Train-on-Synthetic-Test-on-Real (TSTR) errors, pointing to potential limitations in robustness when generalizing to unseen real data.

Dynamic Lifelong learning with Spiking Generative Networks (DL-SGN) [375] is a hybrid SNN-ANN lifelong learning framework designed to enable energy-efficient image generation and classification on edge devices while addressing CF. It integrated ANN-based dynamic expert modules that grow through Dynamic Knowledge Adversarial Fusion (DKAF), an SNN-based student module combining a VAE and classifier, and an ANN-based assistant discriminator trained adversarially to support generalization. Implemented in PyTorch, DL-SGN achieved substantial improvements in FID scores e.g., MNIST (56.26 vs. 95.26) and CIFAR10 (92.46 vs. 192.2) and surpassed ANN-based replay methods such as LTS and LGM in classification accuracy across complex benchmarks like SVHN-CIFAR10- ImageNet10 task (average: 52.43%). In semi-supervised lifelong learning, it reduces MNIST classification error to 2.47%, significantly outperforming DGR (7.27%). However, the framework incurs notable computational overhead due to expert module expansion and adversarial training. Future

directions include optimizing expansion strategies, developing SNN-native generative models, and unifying supervised and unsupervised objectives for improved adaptability in dynamic environments.

Our analysis reveals that hybrid architectures consistently outperform single-paradigm approaches by leveraging complementary strengths of different learning mechanisms. Key observations include the effectiveness of biologically-inspired designs CH-HNN, the scalability advantages of generative replay methods, and the computational efficiency gains from hybrid training protocols. These approaches demonstrate significant improvements in both Task-IL and Class-IL scenarios across standard benchmarks including MNIST, CIFAR-100, and ImageNet variants.

# F. EFFICIENCY ENHANCEMENT METHODS FOR NCL

To further reduce the memory footprint and energy consumption of NCL methods, several optimization methods proposed in literature are discussed below, addressing key question Q6.

# 1) REDUCTION OF SNN OPERATIONS

Real-time resource-constrained applications require fast and efficient processing SNNs. Their operations can be reduced through several network optimizations by:

• Leveraging sparse neurons and sparse synapses to reduce the number of neuron operations and connections/weights, respectively.   
• Utilizing temporal encoding uses timing of spikes to encode information in a way that can reduce computational complexity compared to rate encoding.   
• Employing simple neuron models like LIF instead of complex models to reduce the computational complexity required per neuron.

SpikeDyn [42] replaced the inhibitory neurons with the direct lateral inhibitions in the SNN model used in ASP [100], which consisted of input, excitatory, and inhibitory layers (Fig. 30), thereby eliminating the operations in the inhibitory layer.

![](images/4dc03331e6d6265dda8213baee470e99cb95d61251b88cb70fe9d51097aca34f.jpg)  
FIGURE 30. Replacement of the inhibitory neurons with direct lateral inhibitions; adapted from studies in [42].

# 2) WEIGHT QUANTIZATION

This method enhances SNNs efficiency by representing network weights with lower precision instead of using fullprecision floating-point numbers [279], [280], [281], [376],

[377], [378], [379]. Weights can be quantized to a smaller number of selected discrete levels such as 8-bit, 4-bit, or even binary, using uniform or non-uniform quantization [380]. For instance, lpSpikeCon [43] reduced SNN weights using uniform quantization with truncation [380], [381]. Similarly, to reduce the required on-chip memory, the synaptic weights and dendritic delays are quantized in [355]. Thus, keeping the user-defined number of bits and removing the remaining bits from the fractional part, reduces the storage size, speeds up the training and inference processes, and enables more efficient hardware implementations [264].

# 3) KNOWLEDGE DISTILLATION

To enhance the efficiency of SNNs in resource-constrained environments, knowledge distillation has been widely explored as an optimization technique [382], [383], [384], [385]. In particular, teacher-student knowledge distillation enables smaller models to retain the performance of larger models while reducing memory and computational overhead. Shaw et al. [386] demonstrated the successful application of teacher-student knowledge distillation for radar perception on embedded accelerators, optimizing neural networks for efficient real-time processing. Similar techniques could be leveraged in NCL to improve computational efficiency and reduce model complexity for neuromorphic edge applications.

# G. COMPATIBILITY WITH NEUROMORPHIC HARDWARE

The requirements for implementing a CL method on neuromorphic hardware include: (1) computational units/modules that can execute the CL algorithm, and (2) sufficient size of computational and memory resources. Specifically, the neuromorphic hardware should have compute units that can execute the given CL algorithm on-chip. For instance, if the CL algorithm employs a bio-plausible STDP learning rule, then the neuromorphic hardware should have a learning unit that can execute it. Meanwhile, the size of computational and memory modules from the neuromorphic hardware defines how much workload can be executed at one time, thereby computational and memory constraints will affect the performance in terms of processing latency, throughput, and energy efficiency.

The compatibility of reviewed methods on the existing neuromorphic hardware can be analyzed based on the capability of the hardware to perform on-chip learning. The summary of existing neuromorphic hardware and their on-chip learning capabilities is provided in Table 10. This table shows that, most of neuromorphic hardware platforms do not support on-chip learning, or only support specific on-chip learning mechanisms (e.g., bio-plausible STDP). Therefore, most of reviewed methods may not be executed on the existing neuromorphic hardware, rather they can be executed on the host processing unit (CPU/GPU), which is capable of executing more types of operations, addressing the key question Q7.

TABLE 9. Summary of the state-of-the-art works for energy-efficient CL employing bio-plausible SNNs (i.e., NCL).   

<table><tr><td>Work, Year</td><td>CL Scenario</td><td>Learning Setting</td><td>Neuron Model</td><td>Neural Coding</td><td>Learning Rule</td><td>Learning Rate</td><td>Optimization Technique</td><td>Dataset</td><td>Software</td></tr><tr><td>ASP [100], (2017)</td><td>Class-IL</td><td>Unsupervised</td><td>LIF</td><td>Rate</td><td>STDP</td><td>Adaptive</td><td>Weight Decay</td><td>MNIST</td><td>Brian [311]</td></tr><tr><td>SpikeDyn [42], (2021)</td><td>Class-IL</td><td>Unsupervised</td><td>LIF</td><td>Rate</td><td>STDP</td><td>Adaptive</td><td>Weight Decay</td><td>MNIST</td><td>Bindsnet [304]</td></tr><tr><td>pSpikeCon [43], (2022)</td><td>Class-IL</td><td>Unsupervised</td><td>LIF</td><td>Rate</td><td>STDP</td><td>Adaptive</td><td>Weight Quantization</td><td>MNIST</td><td>Bindsnet [304]</td></tr><tr><td>CFN [99], (2020)</td><td>Class-IL</td><td>Unsupervised</td><td>LIF</td><td>Rate</td><td>STDP</td><td>Adaptive</td><td>-</td><td>MNIST</td><td>-</td></tr><tr><td>SpNCN [301], (2023)</td><td>Task-IL</td><td>Supervised</td><td>LIF</td><td>Rate</td><td>ST-LRA, ST-LRA+ STDP</td><td>-</td><td>-</td><td>MNIST [364] FMNIST [365] Not-MNIST [366]</td><td>-</td></tr><tr><td>[354], (2024)</td><td>Task-IL</td><td>Supervised</td><td>Enhanced model of [367]</td><td>TTFS</td><td>Back-Propagation</td><td>Fixed</td><td>Weight and Delay Quantization</td><td>Split-MNIST</td><td>FPGA, Python</td></tr><tr><td>[302], (2022)</td><td>Class-IL</td><td>Supervised</td><td>SRM</td><td>Rate</td><td>Bayesian Learning</td><td>-</td><td>-</td><td>Split-MNIST, MNIST-DVS [368]</td><td>Intel&#x27;s Lava [312]</td></tr><tr><td>DSD-SNN [358], (2023)</td><td>Task-IL, Class-IL</td><td>Supervised</td><td>LIF</td><td>-</td><td>Back-Propagation</td><td>-</td><td>-</td><td>MNIST N-MNIST [338], Split-CIFAR100</td><td>BrainCog [313]</td></tr><tr><td>SOR-SNN [359], (2023)</td><td>Class-IL</td><td>Supervised</td><td>LIF</td><td>-</td><td>Back-Propagation</td><td>Adaptive</td><td>-</td><td>CIFAR100 [369], ImageNet [370]</td><td>-</td></tr><tr><td>[360], (2023)</td><td>Class-IL, TA</td><td>Supervised</td><td>LIF</td><td>-</td><td>BPTT</td><td>Fixed Fixed</td><td>-</td><td>MNIST</td><td>PyTorch [317]</td></tr><tr><td>[297], (2023)</td><td>Sample-IL, Class-IL</td><td>Supervised</td><td>LIF</td><td>-</td><td>BPTT</td><td>-</td><td>Time Compression</td><td>SHD [341]</td><td>Python</td></tr><tr><td>Replay4NCL [361], (2025)</td><td>Class-IL</td><td>Supervised</td><td>LIF</td><td>-</td><td>BPTT</td><td>Adaptive</td><td>Timestep Reduction</td><td>SHD [341]</td><td>Python</td></tr><tr><td>[292], (2022)</td><td>Task-IL</td><td>Unsupervised</td><td>IF</td><td>Rank-Order</td><td>STDP, R-STDP</td><td>a+&lt;0.15, a-&gt;−0.1125</td><td>-</td><td>MNIST, EMNIST [371]</td><td>SpykeTorch [310]</td></tr><tr><td>HLOP-SNN [363], (2024)</td><td>Task-IL, DIL</td><td>Supervised</td><td>LIF</td><td>Rate</td><td>Hebbian</td><td>Fixed</td><td>-</td><td>PMNIST [364], CIFAR100</td><td>Python</td></tr></table>

TABLE 10. Summary of the existing neuromorphic hardware platforms with their on-chip learning capabilities.   

<table><tr><td>Neuromorphic Processor</td><td>On-chip Learning</td><td>On-chip Learning Mechanism</td></tr><tr><td>NeuroGrid [323]</td><td>No</td><td>-</td></tr><tr><td>ROLLS [325]</td><td>Yes</td><td>SDSP</td></tr><tr><td>TrueNorth [325]</td><td>No</td><td>-</td></tr><tr><td>SpiNNaker [387]</td><td>Yes</td><td>STDP</td></tr><tr><td>BrainscaleS-2 [388]</td><td>Yes</td><td>STDP, R-STDP, SG</td></tr><tr><td>Loihi [326]</td><td>Yes</td><td>STDP, Surrogate Gradient Learning</td></tr><tr><td>Tianjic [389]</td><td>No</td><td>-</td></tr><tr><td>MorphIC [390]</td><td>Yes</td><td>SDSP</td></tr><tr><td>DYNAP [327]</td><td>No</td><td>-</td></tr><tr><td>Akida [328]</td><td>Yes</td><td>Last-layer Learning</td></tr><tr><td>PAIBoard [391]</td><td>No</td><td>-</td></tr><tr><td>PAICORE [392]</td><td>Yes</td><td>STDP</td></tr></table>

# H. TRADE-OFF ANALYSIS

The discussion in this section addresses the key question Q9. Hardware implementation of NCL typically aims at improving performance (speed-up) and computational efficiency (e.g., in terms of power/energy consumption), while offering high accuracy. However, achieving high accuracy with high speed-up and high efficiency in NCL is a challenging task due to the conflicting nature of their requirements. For instance, in order to achieve high accuracy, the network model typically requires more resources (e.g., more neurons and weights) to provide more memory for continually storing new knowledge from learning new tasks without forgetting, thus significantly increasing the model size.

# 1) ENERGY-ACCURACY TRADE-OFFS

SpikeDyn [42] demonstrated substantial energy savings with 51% reduction in training energy and 37% in inference energy for 400 neuron network, (see Table 12), while achieving 21% accuracy improvement over baseline method [100] for new tasks and 8% improvement for previously learned tasks. For smaller 200 neuron network, the trade-offs were even more favorable, showing 57% training and 51% inference energy reductions with 23% accuracy improvements. These results indicate that careful architectural optimizations can yield significant energy benefits without accuracy losses.

# 2) MEMORY-ACCURACY TRADE-OFFS

Compressed latent replay methods [297], [361] demonstrated memory-accuracy trade-offs, achieving 140× memory reduction (from 22.4 MB to 160 KB) with only 4% accuracy degradation in Sample-IL scenario [297]. In Class-IL scenario, this method achieved ≈86% accuracy on layer 3 in case of a 1:5 ratio with 320 kB memory usage, compared to naive rehearsal (without compression) requiring 22.4 MB for 89.55% accuracy, representing a 7× memory efficiency improvement with ≈3% accuracy drop [297]. Replay4NCL [361] revealed that storing compressed latent replays at layer 3 and replaying them with fewer timesteps (i.e., 40 instead of 100) with critical parameters adjustment achieved 90.43% accuracy compared to 86.22% of the baseline [297], with 4.88x speed-

up, 20% latent memory saving, and 36.43% energy saving. lpSpikeCon [43] showed that lowering weight precision from 32-bit to 4-bit degrades task-specific accuracy due to information loss, while achieving 8× memory reduction.

# 3) HARDWARE PLATFORM ENERGY-LATENCY TRADE-OFFS

Platform-specific performance showed significant latency variations in [42]: 1.71s per inference on Jetson Nano (10W) versus 0.2s on RTX 2080 Ti (250W), indicating that energy-constrained platforms require 8.5× longer processing time but consume 25× less power, providing clear energylatency trade-off quantification for different deployment scenarios.

Moreover, maintaining high accuracy often requires the model to employ high precision data format, which may not be supported in commodity neuromorphic hardware [328], thereby making it even more difficult to reduce the network size. On the other hand, neuromorphic hardware platforms typically have limited compute and memory resources, which constrains how the network model will be implemented (i.e., mapped and executed) on the hardware fabric. Therefore, a larger model usually requires longer processing latency, and hence higher power/energy consumption. The DSD-SNN model achieved an efficient trade-off between network compactness and CL by dynamically adapting its structure [358]. On CIFAR100, it stabilized at 37.48% of the full network size while maintaining superior accuracy than the nonpruned variant, which rapidly exhausted memory, leading to performance collapse after six tasks. This highlights the effectiveness of pruning in reducing overhead without compromising learning performance. In some cases, a very large model may even need to be split into several parts (e.g., layer-based partition), so that each part can be mapped and executed on the hardware fabric. Consequently, this condition leads to higher processing latency (lower speed-up) and higher power/energy consumption (lower efficiency).

To address this, trade-off analysis is required. This analysis aims at identifying the appropriate network model candidates considering the given hardware constraints (e.g., compute and memory budgets), and then guides the selection on the most suitable one [42]. For instance, if we can accept a slight accuracy degradation for a targeted application, we may be able to decrease the model size significantly through some optimization techniques (such as quantization and pruning), and hence reducing processing latency (higher speed-up) and power/energy consumption (higher efficiency) [43], [264].

# I. SUMMARY OF NCL

The state-of-the-art methods have performed initial studies for enabling NCL (Table 9). We provide a comparative quantitative analysis (i.e., numerical results) considering design factors (i.e., network complexity) and key evaluation metrics (accuracy, memory footprint, latency, power/energy usage) of the reviewed NCL methods with relevant stateof-the-art DNN-based CL methods (from Section II-G), see Table 11. The table is designed to align according to evaluated

TABLE 11. Comparative quantitative analysis of the surveyed NCL methods evaluated on P-MNIST, Split CIFAR-100, Split MNIST, and ImageNet datasets with relevant state-of-the-art DNN-based CL methods addressing energy-efficiency problem with various settings and scenarios.   

<table><tr><td colspan="8">P-MNIST</td></tr><tr><td>Methods</td><td>Network/Model</td><td>Accuracy</td><td>CL Setting</td><td>CL Scenario</td><td>Memory</td><td>Latency</td><td>Energy</td></tr><tr><td>GPM [213]</td><td>FC</td><td>93.91% ± 0.16</td><td>Supervised</td><td>Task-IL, Class-IL</td><td>n/a</td><td>245s (train)</td><td>n/a</td></tr><tr><td>[221]</td><td>FC</td><td>84.3% ± 0.3</td><td>Supervised</td><td>Task-IL</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td>A-GEM [220]</td><td>FC</td><td>≈ 90%</td><td>Supervised</td><td>Task-IL</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td>GSS [113]</td><td>MLP</td><td>77.3% ± 0.5</td><td>Supervised</td><td>Task-IL</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td>HLOP-SNN [363]</td><td>FC</td><td>95.15%</td><td>Supervised</td><td>Task-IL, Domain-IL</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td colspan="8">CIFAR-100</td></tr><tr><td>GPM [213]</td><td>5-layer AlexNet</td><td>72.48% ± 0.40 (10-split)</td><td>Supervised</td><td>Task-IL, Class-IL</td><td>5.84M parameters</td><td>770s (train)</td><td>n/a</td></tr><tr><td>Adam-NSCL [216]</td><td>ResNet-18</td><td>75.95% (20-split)</td><td>Supervised</td><td>Class-IL</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td>[221]</td><td>ResNet18</td><td>71.0% ± 0.3</td><td>Supervised</td><td>Task-IL</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td>GDumb [196]</td><td>ResNet32</td><td>60.3% ± 0.85</td><td>OCL</td><td>Task-IL</td><td>11051</td><td>60s (train)</td><td>n/a</td></tr><tr><td>CoPE [190]</td><td>Resnet18</td><td>21.62%±0.69</td><td>Supervised</td><td>-</td><td>50001</td><td></td><td></td></tr><tr><td>X-DER [197]</td><td>ResNet18</td><td>49.93%</td><td>Supervised</td><td>Class-IL</td><td>≈ 50MB</td><td>5× more runtime than DER++</td><td>n/a</td></tr><tr><td>ACAE-REMIND [208]</td><td>Resnet-18 &amp; Resnet-32</td><td>62.30% AOC (50 steps)</td><td>OCL</td><td>Class-IL, TA</td><td>12.8 MB</td><td>n/a</td><td>n/a</td></tr><tr><td>A-GEM [220]</td><td>ResNet18</td><td>≈ 62%</td><td>Supervised</td><td>Task-IL</td><td>10 times lower than EWC</td><td>100 times faster than EWC</td><td>n/a</td></tr><tr><td>DVC [393]</td><td>Resnet18</td><td>24.1% ± 0.8</td><td>OCL</td><td>Class-IL</td><td>50001</td><td>n/a</td><td>n/a</td></tr><tr><td>SDAF [394]</td><td>ResNet18 &amp; MLP</td><td>39.0% ± 0.3</td><td>OCL</td><td>Class-IL</td><td>50001</td><td>n/a</td><td>n/a</td></tr><tr><td>SCR [191]</td><td>ResNet18 &amp; MLP</td><td>37.8% ± 0.3</td><td>Supervised</td><td>Class-IL</td><td>50001</td><td>≈ 250s</td><td>n/a</td></tr><tr><td>DSD-SNN [358]</td><td>Multi-CONV &amp; 1 FC layers</td><td>77.92% ± 0.29, 60.47% (10 steps)</td><td>Supervised</td><td>Task-IL, Class-IL</td><td>37.48% network compression</td><td>n/a</td><td>n/a</td></tr><tr><td>SOR-SNN [359]</td><td>ResNet-18</td><td>86.65% ± 0.20 (20 steps)</td><td>Supervised</td><td>Class-IL</td><td>0.32M parameters</td><td>n/a</td><td>n/a</td></tr><tr><td>HLOP-SNN [363]</td><td>ResNet-18</td><td>78.58%</td><td>Supervised</td><td>Task-IL, Domain-IL</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td colspan="8">MNIST</td></tr><tr><td>DER++ [195]</td><td>FC</td><td>92.77% ± 1.05</td><td>Supervised</td><td>Domain-IL</td><td>5001</td><td>n/a</td><td>n/a</td></tr><tr><td>EEC [203]</td><td>3-layer CONV autoencoder</td><td>97.83% (10 classes)</td><td>Supervised</td><td>Class-IL</td><td>0.2MB disk space</td><td>n/a</td><td>n/a</td></tr><tr><td>CoPE [190]</td><td>MLP</td><td>93.94% ± 0.20</td><td>Supervised</td><td>-</td><td>20001</td><td>n/a</td><td>n/a</td></tr><tr><td>GDumb [196]</td><td>MLP</td><td>88.9% ± 0.6</td><td>OCL</td><td>Class-IL</td><td>3001</td><td>60s (train)</td><td>n/a</td></tr><tr><td>[292]</td><td>3 CONV layers</td><td>92.0% ± 0.1</td><td>Unsupervised</td><td>Task-IL</td><td>n/a</td><td>2.5min2</td><td>n/a</td></tr><tr><td>DSD-SNN [358]</td><td>Multi-CONV</td><td>97.30% ± 0.09</td><td>Supervised</td><td>Task-IL</td><td>34.38% network compression</td><td>n/a</td><td>n/a</td></tr><tr><td>Bayesian CL [302]</td><td>Multi-FC layers</td><td>85.44% ± 0.16</td><td>Supervised</td><td>Class-IL</td><td>5× reduction</td><td>n/a</td><td>n/a</td></tr><tr><td>SpNCN [301]</td><td>4 FC layers</td><td>96.50%</td><td>Supervised</td><td>Task-IL</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td>ASP [100]</td><td>2 FC layers</td><td>94.20%</td><td>Unsupervised</td><td>Class-IL</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td>SpikeDyn [42]</td><td>2 FC layers</td><td>Improved 23% (new task), 4% (old task) than ASP</td><td>Unsupervised</td><td>Class-IL</td><td>&lt;3000kB</td><td>0.2s3</td><td>57% (train), 51%(in-ference) lower than ASP</td></tr></table>

TABLE 11. (Continued.) Comparative quantitative analysis of the surveyed NCL methods evaluated on P-MNIST, Split CIFAR-100, Split MNIST, and ImageNet datasets with relevant state-of-the-art DNN-based CL methods addressing energy-efficiency problem with various settings and scenarios.   

<table><tr><td>lpspikecon [43]</td><td>2 FC layers</td><td>68% (6-bit quantized weights)</td><td>Unsupervised</td><td>Class-IL</td><td>8x weight memory reduction with 4-bit than 32-bit</td><td>n/a</td><td>n/a</td></tr><tr><td>[354]</td><td>4 FC layers</td><td>80.0% on FPGA</td><td>Supervised</td><td>Task-IL</td><td>35.3% flip-flops, 29.3% BRAMs</td><td>n/a</td><td>n/a</td></tr><tr><td colspan="8">ImageNet</td></tr><tr><td>X-DER [188]</td><td>EfficientNet-B2</td><td>28.19%</td><td>Supervised</td><td>Class-IL</td><td>20001</td><td>n/a</td><td>n/a</td></tr><tr><td>SDAF [394]</td><td>ResNet18 &amp; MLP</td><td>33.2% ± 0.5</td><td>OCL</td><td>Class-IL</td><td>50001</td><td>n/a</td><td>n/a</td></tr><tr><td>DVC [393]</td><td>Resnet18</td><td>19.1% ± 0.9</td><td>OCL</td><td>Class-IL</td><td>50001</td><td>n/a</td><td>n/a</td></tr><tr><td>[221]</td><td>ResNet18</td><td>39.5% ± 0.3</td><td>Supervised</td><td>Task-IL</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td>SCR [191]</td><td>ResNet18 &amp; MLP</td><td>35.4% ± 0.5</td><td>OCL</td><td>Class-IL</td><td>50001</td><td>n/a</td><td>n/a</td></tr><tr><td>SOR-SNN [359]</td><td>ResNet-18</td><td>&gt;55%</td><td>Supervised</td><td>Class-IL</td><td>0.32M parameters</td><td>n/a</td><td>n/a</td></tr></table>

1 Memorybufersize;²Aproximatetimeoetrainngepochtoofor24ktrainingpatts;Inferece timeofanimage;Note:Rows with indicate NCL methods andindicate DNN-based CL methods.

datasets (i.e., P-MNIST, Split CIFAR-100, Split-MNIST, and ImageNet) and includes the performance metrics (as reported in the respective studies of each method). Several reviewed NCL methods like SpNCN [301], SOR-SNN [359] and DSD-SNN [358] explicitly compare their method with established DNN-CL baselines, such as EWC [70], SI [66], MAS [151]. For more detailed comparisons, we refer to the respective studies of the NCL methods.

We observe that while optimization-based CL methods in DNNs (i.e., GPM [213], [221], A-GEM [220] and GSS [113]) report high accuracy on standard benchmarks such as P-MNIST, the NCL method HLOP-SNN [363] achieves superior accuracy (95.15%) with the same CL setting and scenario. Moreover, the NCL method SOR-SNN [359] achieves competitive accuracy (86.65%) on CIFAR-100 with significantly lower memory (0.32M params) than DNN-based CL methods, highlighting the energy-efficient scalability of spiking architectures. On the MNIST, NCL methods such as DSD-SNN [358] and SpikeDyn [42] report comparable or better accuracy with drastic reductions in latency, memory, and energy (e.g., 0.2s, <3000KB), demonstrating the suitability of NCL for lightweight and resource-constrained applications. While accuracy remains lower for both domains on ImageNet, NCL methods like SOR-SNN [359] show promising results in parameter efficiency and deployment feasibility. Furthermore, the NCL methods with bio-plausible learning rules (e.g., STDP) facilitate unsupervised learning, which is suitable for OCL scenario. These works mainly employ FC SNN architectures (see Table 12), consisting of input layer and a pair of excitatory-inhibitory layer. As the input data grows in complexity, FC SNNs struggle to capture the important hierarchical features without increasing

the network size. Larger architectures often lead to better accuracy but require larger storage sizes, which may exceed resource constraints. This limits the deployable networks on practical hardware platforms, and makes their performance limited to simple datasets (e.g., MNIST) with simple CL scenarios (e.g., Split-MNIST). Meanwhile, NCL methods that employ supervised-based learning rules (e.g., SG-based BP) can achieve acceptable performance on complex datasets (e.g., CIFAR-100 and ImageNet).

However, they are not suitable for OCL scenario, as they require costly labeled data and power-hungry training. Therefore, alternative methods are required especially for enabling energy-efficient SNNs with OCL capabilities, which are beneficial for many real-world application use-cases. Although, we provide the comparison (Table 11), we acknowledge that perfect fairness remains a challenge due to differences in CL scenarios, hyperparameters, underlying model architectures, training paradigms, hardware assumptions, encoding schemes, evaluation protocols, and CL settings (i.e., OCL, supervised or unsupervised). We have emphasized these limitations in our discussion (Section-V). Meanwhile, we ensured that our comparisons are as meaningful and aligned, as possible under current benchmarking constraints. Thus, providing a contextual foundation for assessing the relative strengths and limitations of approaches and the reliability of results.

Replay-based CL in SNNs differs from its ANN counterparts in terms of operation as the ANN-based replay methods like iCaRL [106], DGR [200] rely on storing raw inputs or latent vectors and updating weights using full gradient feedback. In contrast, SNN-based replay must preserve temporally precise spike trains under event-driven

constraints, making it dependent on local or SG learning and limited by encoding complexity and latency alignment. While ANN replay offers high gradient precision and plasticity, SNN replay often relies on approximations like compressed or spike-rate encoded replay to conserve power and memory, which may reduce accuracy. Nonetheless, SNN replay methods such as latent replay or STDP-based approaches are significantly more energy-efficient and wellsuited for OCL in low-power environments. Additionally, spike noise from stochastic firing and temporal jitter, along with hardware-induced variability such as component mismatch and drift, introduces instability in synaptic updates and membrane dynamics. These factors hinder reproducibility and memory consolidation in SNNs, necessitating robustness-aware learning rules like homeostatic STDP or meta-plasticity, such challenges are absent in conventional hardware.

# IV. REAL-WORLD APPLICATION USE-CASES

In this section, we discuss the real-world application usecases that will benefit from bio-plausible SNNs with OCL capabilities, taxonomy shown in Fig. 31. Additionally, we also highlight the current state-of-the-art for emerging application use-cases, and hence addressing the key question Q10. A summary of real-world application use-cases that will benefit from SNNs with OCL, is presented in Table 13. Quantitative analysis (i.e., numerical results) of the case studies covered by these works are reported in Table 14.

# A. ADAPTIVE ROBOTS

# 1) OBJECT RECOGNITION FOR HUMANOID ROBOTS

Adaptive Robots need to identify, classify, and locate objects within an image/video. For this, Neural Engineering Framework (NEF) is explored for developing Neural State Machine (NSM) framework leveraging SNNs, managing the allocation of new neurons (Fig. 32), where data may be collected on-the-fly without any labels [395]. A case study on the interactive continual object learning of the iCub robot was presented in [395]; see Table 13. Experiments in the Gazebo robotic simulator [396] mimicking event-based camera conditions, and implementations on Intel’s Loihi neuromorphic chip [326], demonstrated 96.55±2.02% accuracy in learning object representations within three epochs, adapting efficiently to new objects [395]; see Table 14. CL assessments showed rare confusions (< 20%) after the first epoch. The model allocated neurons dynamically based on object complexity, optimizing resource use. The continual classifier was benchmarked against conventional online classifiers on a CPU, showing up to 300× better energy efficiency for learning and 150× for inference [395]. These findings highlight SNNs’ potential for real-world deployment in embedded AI systems, with future extensions to physical robotic platforms. However, it relies on supervised settings which require costly labeled data, power-hungry training, and

long training time to update its knowledge, thus it is not suitable for OCL scenario.

# 2) ROBOTIC CONTROL SYSTEMS

The study [397] explored NEF for developing neuromorphic algorithms for Inverse Kinematics (IK) and Proportional-Integral-Derivative (PID) control systems, supporting online learning of control signals, using Prescribed Error Sensitivity (PES). Fig. 33(a) shows the model schematic for neuromorphic IK with online learning, whose target is to efficiently compute the joint angles required to place the robots’ endeffector at the desired position. Meanwhile, the PID controller aims to ensure that the robots’ actuators accurately follow a desired trajectory. Hence, it needs to continuously adjust the actuators to minimize the error in position, ensuring accurate motion control. To achieve this, the PID controller has been implemented using spiking neurons to represent the error signals and components; see Fig. 33(b). This work presented a case study on the control of a 6-degrees of freedom robotic arm; see Table 13. The implementation was based on Nengo [398], [399] a Python based neural compiler, that translates high-level descriptions to low-level neural models and Intel Loihi neuromorphic chip [326], offering high performing and energy-efficient neuromorphic control; see Table 14. However, it relies on supervised settings which require costly labeled data, power-hungry training, and long training time to update its knowledge and thus is not suitable for the OCL scenario. Similarly, a recent work in [400] used NEF within the Nengo simulator and MATLAB R2022b to implement a SNN-based PID controller for robotic arm trajectory tracking. The controller was evaluated on a case study of simulated 3-DoF robotic arm; see Table 13. It reported achieving a 6% improvement in the Integral of Time-weighted Absolute Error (ITAE) and a 30% reduction in Root Mean Square Error (RMSE) compared to the conventional PID and fuzzy controllers; see Table 14.

# B. AUTONOMOUS VEHICLES AND MOBILE AGENTS

CL in autonomous vehicles and mobile agents is crucial to enable continuous adaptation to the changes in environments (e.g., road and weather) and personalize the preferences. Hence, they are typically equipped with sensors and cameras for continuous data collection during operation. Moreover, they usually rely on limited battery, and often face unlabeled data and constrained resources. Therefore, their use-cases can benefit from SNNs with OCL capabilities.

# 1) CARS DETECTION

Several works have been developed for low-power autonomous vehicles using SNNs, including studies of cars detection in CarSNN [401], SNN4Agents [379], Fast-Spiker [402], [403] and [404]. CarSNN and SNN4Agents used an attention window mechanism (i.e., focusing on regions with the highest event density) to process event-based input samples from the N-CARS dataset [339]; see Fig. 34.

odel size, perfo architec NCL in te   

<table><tr><td>Work</td><td>SNN Architecture</td><td>Model Size</td><td>Performance</td><td>Memory Footprint</td><td>Power/Energy Consumption</td></tr><tr><td>ASP [100]</td><td>Hierarchical SNN</td><td>6400 excitatory neurons</td><td>Achieved avg. accuracy of 94.2% outperforming standard STDP</td><td>n/a</td><td>n/a</td></tr><tr><td>SpikeDyn [42]</td><td>2 FC layers (1 input &amp; 1 excit. layers)</td><td>200 and 400 excit. neurons</td><td>Improved accuracy by 23% for the new task &amp; 4% for old tasks than ASP for 200-neuron SNN</td><td>&lt;3000 KB</td><td>Avg. reduction of 57% (training) and 51% (inference) than ASP</td></tr><tr><td>IpSpikeCon [43]</td><td>2 FC layers (1 input &amp; 1 excit. layers)</td><td>200 and 400 excit. neurons</td><td>No accuracy loss in inference compared to the 32-bit weights baseline (SpikeDyn)</td><td>8x reduction from SpikeDyn</td><td>n/a</td></tr><tr><td>CFN [99]</td><td>Multi-FC layers (1 excit., 1 inhib., &amp; 1 dopaminergic layers)</td><td>400-6400 excit. neurons</td><td>Achieved 95.24% avg. accuracy across MNIST digits in Class-IL for 6400-neuron CFN</td><td>n/a</td><td>n/a</td></tr><tr><td>SpNCN [301]</td><td>4 FC layers</td><td>3000 neurons-per-layer</td><td>Normalized accuracy of 0.9653 (MNIST), 0.9120 (Not-MNIST), and 0.9995 (FMNIST)</td><td>n/a</td><td>n/a</td></tr><tr><td>[354]</td><td>4 FC layers</td><td>784-403-403-2784-400-400-2</td><td>Achieved avg. inference time of 37.3ms &amp; test accuracy of 80.0% on FPGA</td><td>35.3% flip-flops, 29.3% BRAMs</td><td>n/a</td></tr><tr><td>[302]</td><td>Multi-FC layers</td><td>2048, 4096, 40962048, 1024 neurons/layer</td><td>Achieved avg. test accuracy of 85.44±0.16% for Split-MNIST and 74% for MNIST-DVS</td><td>5× reduction</td><td>n/a</td></tr><tr><td>DSD-SNN [358]</td><td>Multi-CONV &amp; 1 FC layers</td><td>100 &amp; 500 neurons</td><td>Achieved 97.30%±0.09% accuracy (34.38% compression rate) for MNIST in Task-IL, 96.94%±0.05% accuracy for N-MNIST, 60.47% (10 steps) for CIFAR100 in Class-IL</td><td>n/a</td><td>n/a</td></tr><tr><td>SOR-SNN [359]</td><td>ResNet18</td><td>96 hidden layer neurons</td><td>Achieved 86.65%±0.20 accuracy, &amp; improved accuracy by 2.20% from DSD-SNN (CIFAR100)</td><td>n/a</td><td>0.32M parameters (9.35% of DSD-SNN)</td></tr><tr><td>[360]</td><td>2 CONV layers</td><td>n/a</td><td>Achieved 51% avg. accuracy (40 batches-per-task) in Class-IL &amp; 36% accuracy with memory replay (100 batches-per-task) in Task-Free scenario</td><td>n/a</td><td>n/a</td></tr><tr><td>[297]</td><td>4 Recurrent-FC layers</td><td>200-100-50-20 neurons</td><td>Achieved Top-1 accuracy of 92.5% and 92% in Sample and Class-IL scenarios, respectively and 78.4% in multi Class-IL scenario</td><td>Two orders of magnitude reduction from naive rehearsal (max. 4% acc. drop)</td><td>n/a</td></tr><tr><td>Replay4NCL [361]</td><td>4 Recurrent-FC layers</td><td>200-100-50-20 neurons</td><td>Achieved Top-1 accuracy of 90.43% on old knowledge, outperforming the state-of-the-art</td><td>20% reduction in latent memory usage</td><td>4.88x latency improvement and 36.43% energy reduction than [297]</td></tr><tr><td>[292]</td><td>3 CONV layers</td><td>30-250-200 neurons</td><td>Achieved 92.0 ± 0.1% accuracy for digits in joint training, &amp; 79.7±0.5% accuracy for letters</td><td>n/a</td><td>n/a</td></tr><tr><td>HLOP-SNN [363]</td><td>FC, ResNet-18, &amp; 3 CONV layer architectures</td><td>784-800-10 neurons for FC SNN</td><td>Achieved 95.15% accuracy (PMNIST), 78.58% (CIFAR-100), 63.40% (miniImageNet), &amp; 88.65% (5-Datasets)</td><td>n/a</td><td>n/a</td></tr></table>

For the cars vs. background classification the SNN model was implemented on the Intel Loihi neuromorphic chip [326] (see Table 13). The neuromorphic hardware implementation had maximum 0.72 ms of latency for every sample, and consumed only 310 mW power with an accuracy of 83% [401] (see Table 14). However, the state-of-the-art [379], [401] require a long training time [402]. Therefore, FastSpiker proposed a methodology to accelerate SNN training while maintaining accuracy through learning rate enhancements [402]. However, these works considered supervised settings which require costly labeled data, power-hungry training, and long training time to update its knowledge, hence they are not suitable for OCL scenario..

# 2) ROAD LANE DETECTION

Other SNN works for low-power autonomous vehicles include the road line detection. For instance, LaneSNN [405] addressed the imbalance between lane and background classes by employing a novel loss function combining Weighted Binary Cross Entropy (WCE) and MSE; see Fig. 35. For detecting the lanes marked on the streets using the event-based camera input, the SNNs training and implementation was based on PyTorch library [317] and the Intel Loihi neuromorphic chip [326]; see Table 13. Evaluations demonstrated maximum latency of less than 8 ms, power consumption of about 1 W during the classification of a single image, and online IoU equal to 0.623, thereby making it superior to the state-of-the-art techniques like LaneNet and RefineNet in terms of performance and power efficiency; see Table 14. However, it still considered supervised settings which require costly labeled data, power-hungry training, and long training time to update its knowledge, hence it is not suitable for OCL scenario.

# 3) SIMULTANEOUS LOCALIZATION AND MAPPING (SLAM)

SLAM is important for an autonomous vehicle/agent for constructing a map while simultaneously keeping track of its location in an unknown environment. The DVS-Radar Fusion SLAM [406] is the first SNN-based method for enabling CL-based SLAM using drones (Fig. 36), integrating DVS and a Frequency Modulated Continuous Wave (FMCW) radar to encode sensory data on-the-fly into feature descriptors. To provide drones’ velocity information and aid in obstacle detection, a radar-gyroscope odometry method is used for accurate navigation and mapping. SNN output is utilized as feature descriptors for loop closure detection that are fed to a RatSLAM back-end. This process helps in identifying when the drone revisits a previously mapped area. The obstacle modelling is achieved using radar data by detecting objects and integrating this information into its SLAM framework. DVS-Radar fusion setup outperformed RGB-based methods achieving lower $M A E _ { L }$ and $M A E _ { M }$ values of 0.51 & 0.17 for drone flight sequence 1, and 0.81 & 0.45 for sequence 2; see Table 13 and 14. This work showed

the potential of implementing OCL on SNN-based mobile agents.

# 4) PEOPLE DETECTION

A CL-based people detection framework has been developed in [407]; see Fig. 37. It employs attention maps to enable network adaptation on walking-people detection in dynamic environments, thus avoiding collision. To create attention maps from DVS data, the network is integrated with a readout mechanism. It also generalizes the unsupervised STDP from [410] to a semi-supervised learning case with teacher signals (TSs). To control overfitting, an anti-Hebbian rule (i.e., negative STDP) is applied when person is absent, while positive STDP is used when a person is detected. The empirical results indicated that this SNN-STDP system achieved a peak $F _ { 1 }$ score 19% higher than a comparable same-size CNN processing DVS frames, demonstrating its effectiveness in dynamic human detection task; see Table 13 and 14. Future works include: a) investigating multi-object contexts with multiple walking people instead of a single person, b) implementing proposed system on neuromorphic hardware ReckOn chip [408], which supports local learning, multilayer learning, and SNN ensembles with non-spiking readouts, making it suitable for this SNN-STDPreadout approach. This work further showed the potential of implementing OCL on SNN-based systems.

# 5) ROBOTIC NAVIGATION

Recent study [391] demonstrated the use of PAIBoard neuromorphic computing platform in a quadruped robot [409] performing real-world navigation tasks such as tracking (i.e., via UWB and visual fusion) and obstacle avoidance (i.e., via depth perception) based on vision-based NN processing, as shown in Fig. 38. The system leveraged SNNs for adaptive, low-power control, underscoring the viability of hybrid SNN-ANN (HNN) platforms in autonomous sensorimotor tasks. PAIBoard achieved 90.2% accuracy on CIFAR-10 using fewer neurons and cores than TrueNorth and Tianjic, highlighting efficient resource usage. It also demonstrated 791FPS/W energy efficiency for image classification and consumed 12.8 W during robot tracking and obstacle avoidance task; see Table 13 and 14. The platform is designed to handle such complex tasks, implies a potential for OCL.

# V. OPEN RESEARCH CHALLENGES

Due to the huge potentials and benefits of energy-efficient SNNs with OCL capabilities, continuous advancements in the NCL field are expected in the future. In this section, we identify open research challenges in NCL, highlight the gaps between current research efforts, and propose future research directions; see the summary presented in Table 15. This discussion also addresses the key question Q11.

# A. ADAPTIVE KNOWLEDGE RETENTION AND TRANSFER

Recent NCL methods mitigate CF through adaptive learning rates and weight decay coupled with STDP [42], parameter

![](images/7ea3c8104b3c29ac5dc72601da1d0b34a88f694db9ae2d3571f69f5fc794cb8f.jpg)  
FIGURE 31. A taxonomy of real-world application use-cases covered in this survey, that will benefit from bio-plausible SNNs with OCL capabilities. We have highlighted the main categories (blue blocks), with sub-categories (red blocks), and each of their works shown (green blocks).

TABLE 13. Summary of recent progress in real-world NCL application use-cases that will benefit from SNNs with OCL capabilities, with their implementation details and case studies.   

<table><tr><td>Application Domains</td><td>Use-cases</td><td>Work (Year)</td><td>Case Study</td><td>CL Setting</td><td>Dataset</td><td>CL Approach</td><td>Learning Rule</td><td>Neuron Model</td><td>HW</td></tr><tr><td rowspan="2">Adaptive Robots</td><td>Object Recognition</td><td>[395] (2022)</td><td>Interactive continual object learning in iCub robot</td><td>Supervised</td><td>Custom DVS dataset</td><td>Representation-based</td><td>Modified Hebbian</td><td>LIF</td><td>Loihi</td></tr><tr><td>Robotic Arm Control</td><td>[397] (2021) [400] (2024)</td><td>Control of 6-DoF, 3-DoF trajectory tracking</td><td>Supervised</td><td>Custom dataset from robotic arms&#x27; operations</td><td>Representation-based</td><td>PES</td><td>LIF</td><td>Loihi</td></tr><tr><td rowspan="7">Autonomous Vehicles/ Agents</td><td rowspan="3">Cars Detection</td><td rowspan="3">[401] (2021) [403] (2022) [379] (2024)</td><td rowspan="3">Cars vs. background classification</td><td rowspan="3">Supervised</td><td rowspan="3">N-CARS</td><td>STBP</td><td>SG</td><td>LIF</td><td>Loihi</td></tr><tr><td>-</td><td>STBP</td><td>LIF</td><td>GPU</td></tr><tr><td>STBP</td><td>-</td><td>LIF</td><td>GPU</td></tr><tr><td>Road Lane Detection</td><td>[405] (2022)</td><td>Detection of lanes marked on the streets</td><td>Supervised</td><td>DET [350]</td><td>-</td><td>STBP</td><td>LIF</td><td>Loihi</td></tr><tr><td>SLAM</td><td>[406] (2023)</td><td>CL SLAM fusing DVS &amp; radar on drone</td><td>Unsupervised</td><td>Real-time data from sensors</td><td>Representation-based</td><td>STDP</td><td>LIF</td><td>n/a</td></tr><tr><td>People Detection</td><td>[407] (2024)</td><td>CL of people detection from event-camera mounted on drone</td><td>Semi-supervised</td><td>KUL-UAVSAFE [351]</td><td>Representation-based</td><td>STDP</td><td>LIF</td><td>ReckOn chip* [408]</td></tr><tr><td>Robotic Navigation</td><td>[391] (2024)</td><td>Tracking &amp; obstacle avoidance in robot dog [409]</td><td>Hybrid</td><td>CIFAR-10, self-built dataset</td><td>-</td><td>-</td><td>LIF</td><td>PAIBoard</td></tr></table>

* Potential future work.

adjustments with weight potentiation and depression [43], error-corrected predictions, multi-layer architectures for maintaining distinct task representations [301], dendriticdependent spike time delays and context-dependent gating system [354], as well as compressed LR of learned data [297]. Moreover, Hebbian learning and lateral connections, to project neuronal activity into an orthogonal subspace [363] have been utilized to preserve previous knowledge. Despite these advancements, we identify the existing research gaps and potential future directions, as follows.

1) Exploration of task-similarity-based BWT is limited, thus the challenge of interference in overlapping

classes with high feature similarity remains open. To address this, improving task-similarity-based BWT by exploring advanced feature extraction techniques to enhance class separability and reduce interference.

2) In replay-based methods, increasing number of classes may result in substantial growth in storage. Meanwhile, lossy compression techniques can cause information loss that degrade the performance on previously learned task. Toward this, advanced compression techniques that preserve temporal information with efficient memory-augmentation methods may preserve synaptic connections, thus enhancing performance.

TABLE 14. Quantitative analysis of case studies covered by the reviewed works in Section IV.   

<table><tr><td>Work</td><td>Performance</td><td>OCL 
Capability</td><td>Latency</td><td>Memory 
Footprint</td><td>Power/Energy 
Savings</td></tr><tr><td>[395]</td><td>96.55±2.02% new object accuracy within three epochs, &lt;20% confusions after first epoch</td><td>×</td><td>n/a</td><td>n/a</td><td>300× better for training &amp; 150× for inference</td></tr><tr><td>[397]</td><td>Loihi accuracy outperformed the simulation across different learning rates</td><td>×</td><td>Loihi implementation converged faster to the target than the simulated model</td><td>n/a</td><td>Improved</td></tr><tr><td>[400]</td><td>6% improvement in ITAE and 30% reduction in RMSE compared to traditional PID controller</td><td>×</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td>[401]</td><td>83% accuracy</td><td>×</td><td>0.72 ms</td><td>n/a</td><td>310 mW</td></tr><tr><td>[405]</td><td>online IoU 0.623</td><td>×</td><td>8 ms</td><td>n/a</td><td>1W1</td></tr><tr><td>[406]</td><td>MAEL of 0.51 &amp; MAEM of 0.17 for drone flight sequence 1, MAEL of 0.81 &amp; MAEM of 0.45 for sequence 2</td><td>✓</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td>[407]</td><td>Peak F1 score 19% higher compared to same-size CNN</td><td>✓</td><td>n/a</td><td>514 kB</td><td>n/a</td></tr><tr><td>[391]</td><td>90.2% accuracy</td><td>✓</td><td>n/a</td><td>n/a</td><td>energy2 791FPS/W, power3 12.8W</td></tr></table>

1 For single image classification; ² For image clasification tasks; 3 For tracking and obstacle avoidance task.

![](images/a78ff9c954d6dc7a0640a7ac567497ee8c4804c07a8214aa4b2999bd54d29ccb.jpg)  
FIGURE 32. The NSM framework: Subsampling layer (SS), S1 and C1 perform the visual feature extraction, S2 is the plastic layer (dark blue neurons) that stores visual patterns, Error (Err) and label neurons (Lb) control inference decision of output neurons (Out); adapted from studies in [395].

![](images/1dcee86cdb9aa7d6bd80d5e5b5e0bf0ebf0f77ddeb0f761ee3e7b8c20a5172b4.jpg)

![](images/d988fe33d286b26be89f4c81cfb8e25ce49b421e861fc360a3ff4256c8f091ee.jpg)  
FIGURE 33. (a) A model for neuromorphic IK with online learning, and (b) Neuromorphic PID controller in action; adapted from studies in [397].

3) To avoid overfitting, dendritic segments can be dynamically allocated.   
4) Finally, developing adaptive algorithms to determine subspace neuron numbers based on task complexity and optimizing computational efficiency through code

![](images/01f463abb7b0a59e69979eea3331ed5b5b6a3bd98da12a3070f4c44689cef6f9.jpg)  
FIGURE 34. Setup and tool-flow of CarSNN; adapted from studies in [401].

![](images/e622e18043e91dcffbd8078cdf481942e7344e07eb5d874311371bebf0ab0502.jpg)  
FIGURE 35. Setup and tool-flow of LaneSNNs; adapted from studies in [405].

enhancements or asynchronous parallel neuromorphic hardware could enable real-time adaptability for OCL.

# B. ADAPTATION OF EXISTING CL METHODS IN SNNDOMAIN AND HYBRID SNN-DNN APPROACHES

Exploring how existing ANN-based CL methods can be adapted to the SNN domain, to leverage the strengths

TABLE 15. Summary of open research challenges with their brief description, identified research gaps, and future directions in NCL.   

<table><tr><td>Challenge</td><td>Description</td><td>Identified Research Gaps</td><td>Future Directions</td></tr><tr><td>Adaptive knowledge retention and transfer</td><td>Includes issues like overlapping neural representations, retaining task-specific knowledge with memory efficiency.</td><td>- Insufficient exploration of NCL methods considering task-similarity for BWT. - Limited exploration of advanced compression techniques in replay-based NCL methods.</td><td>- Developing methods with enhanced BWT leveraging similarities between tasks, while avoiding interference. - Exploring efficient memory-augmented techniques for SNNs that preserve important synapses. - Exploring dynamic allocation of dendritic segments only when needed to avoid overfitting. - Designing adaptive algorithms that automatically determine the number of subspace neurons based on task complexity.</td></tr><tr><td>Adaptation of DNN-based CL methods in SNN domain (i.e., NCL) and Hybrid SNN-DNN Approaches</td><td>The adaption of current DNN-based CL methods in SNN domain for NCL developments may lead to effective solutions. - The integration of hybrid SNN-DNN models, leveraging the strengths of both architectures to improve CL performance.</td><td>- Limited adaptation of different CL-based methods (e.g., regularization) in SNNs, particularly for OCL scenarios. - Limited exploration of hybrid SNN-DNN models for CL. - Limited exploration of knowledge distillation techniques like teacher-student in SNN-based CL models.</td><td>- Exploring adaptations of CL-based methods (e.g., regularization) and their impact on SNNs trained with local learning rules in dynamic environments. - Investigating the optimal memory size for replay-based methods in SNNs. - Hybrid approaches where DNNs handle feature extraction while SNNs process temporal or event-driven information could enhance CL in real-world applications. - Exploring knowledge distillation to transfer knowledge from deep networks to SNNs, enabling efficient CL while preserving performance.</td></tr><tr><td>Adaptation to dynamic input patterns</td><td>Changes in input patterns may occur during run time, thereby requiring OCL capabilities to handle dynamic variability of input.</td><td>- SNN learning quality in OCL scenarios is still a developing area. - Limited development of adaptive learning rates that are responsive to temporal correlations in spiking patterns.</td><td>- Investigating SNN architectures that effectively perform weight updates to maintain performance (e.g., accuracy). - Investigating adaptive learning and weight decay rate strategies to improve the flexibility of neuron dynamics. - Developing methods for efficient clustering and representation learning. - Developing adaptive algorithms to explore various configurations of dendritic segments to optimize task-specific adaptation.</td></tr><tr><td>Balancing CL desiderata</td><td>To meet multiple, often conflicting, requirements of CL.</td><td>Balancing CL desiderata remains a key optimization goal for NCL al-orphisms.</td><td>Developing methods that balance and prioritize CL desiderata trade-offs based on the specific application needs.</td></tr><tr><td>Input noise robustness</td><td>Real-world input data is of- ten noisy, with more com- plex, non-linear patterns than AWGN.</td><td>Limited exploration of diverse noise types and intensities for ensuring robustness of NCL methods against noise for OCL scenarios.</td><td>- Expanding the scope of evaluation to include diverse noise types and intensities. - Designing algorithms that automatically filter irrelevant information while emphasizing critical features, thus improving overall performance.</td></tr><tr><td>Data representation</td><td>Most of the current NCL methods use a single encoding technique, i.e., rate coding, which neglects the temporal structure of spike trains, limiting their ability to fully exploit temporal information.</td><td>- Limited exploration of NCL methods using temporal encoding with high information density. - Lack of studies for exploring encoding methods that utilize the strengths of multiple encoding methods.</td><td>- Incorporating time-encoded signals into SNNs to enhance their learning from temporal data (e.g., TTFS encoding) to improve the network&#x27;s ability to handle time-dependent patterns. - Developing SNNs that integrate hybrid encoding techniques for optimization of task performance, latency and energy efficiency.</td></tr><tr><td>Scalability</td><td>Current CL methods incur significant memory and power/energy overheads when the networks get bigger, thereby posing scalability issue.</td><td>- Limited studies for realizing dynamic allocation of neurons without significant computational and memory overheads. - Lack of effective and biologically inspired synaptic reorganization (pruning and growing) mechanisms for SNNs.</td><td>- Investigating the integration of more complex neuron models (e.g., Hodgkin-Huxley model), allowing for a richer representation of neuronal activity and potentially improving the model&#x27;s predictive capabilities and scalability. - Exploring techniques to dynamically allocate neurons for new tasks while pruning redundant ones from previous tasks. - Investigating hierarchical or modular approaches for SNN design to enable scalable architectures for CL. - Investigating techniques for dynamic structural plasticity, in-spiried by the brain&#x27;s ability to reorganize neural connections.</td></tr><tr><td>Learning rule developments</td><td>The existing CL methods of- ten rely on non-local learning rules and primarily use a single learning paradigm, either supervised or unsupervised, limiting performance and adaptability.</td><td>- Enhancements of bio-plausible learning rules (e.g., STDP) for OCL scenarios remain under-explored. - Limited studies in combining supervised and unsupervised settings for NCL.</td><td>Developing advanced local learning rules, such as adaptive variations of STDP, can help SNN models achieve NCL capabilities, especially in OCL scenarios. - Developing hybrid approaches for NCL that combine different learning paradigms for training SNNs (i.e., supervised and unsupervised settings), considering OCL scenarios.</td></tr></table>

of both architectures. For instance, adapting the regularization methods and how it impacts the performance of SNNs trained with local learning rules under dynamic

environments can be explored. Furthermore, the optimal memory size for replay-based method in SNNs that balances desiderata effectively under dynamic environments, can

TABLE 15. (Continued.) Summary of open research challenges with their brief description, identified research gaps, and future directions in NCL.   

<table><tr><td>Challenge</td><td>Description</td><td>Identified Research Gaps</td><td>Future Directions</td></tr><tr><td>Generalization capability</td><td>Current methods are limited in their adaptability to drastically changing environments or task-specific nuances.</td><td>Ensuring NCL methods function effectively across diverse operational settings and tasks is a developing area.</td><td>- Developing adaptive NCL methods that can dynamically adjust to diverse tasks and environmental context, such as adapting to changes from indoor to outdoor conditions. 
- Expanding the evaluation of NCL methods to diverse datasets like DVS Gesture to improve generalization for complex tasks.</td></tr><tr><td>Evaluation datasets and benchmarks</td><td>Datasets should be derived or generated to leverage unique characteristics of event-based data, which properly represent the original data.</td><td>- Research on neuromorphic datasets for benchmarking NCL methods is still developing. 
- Inconsistent data pre-processing (e.g., time resolution), making it difficult to compare results fairly. 
- Data transformation may fail to capture temporal information, thus limiting SNN capabilities. 
- Current datasets are mostly small-scale and narrowly focused, limiting the generalizability and benchmarking for SNNs.</td><td>- Developing standardized pre-processing rules to ensure fairness and consistency in dataset comparisons. 
- Measuring and optimizing energy savings for showing the NC potential in practical applications. 
- Constructing datasets emphasizing temporal dynamics, leveraging event-driven and spike-based data generation. 
- Creating larger-scale, spatial-temporal event-based datasets for diverse tasks to enhance benchmarking and real-world applicability. 
- Task-specific performance metrics are suggested, such as accuracy for classification, MAE for regression, memory ratio and power/energy overhead for scalability, and adaptability scores for functionality.</td></tr><tr><td>Hardware deployments</td><td>- Implementing NCL methods on neuromorphic processors can maximize the efficiency benefits via massively-parallel processing and inherent low-power. 
- NCL methods involve frequently updating parameters, like neuron thresholds and decay rates along with the adjustments of membrane potentials and synaptic weights.</td><td>- The transition from algorithmic level to practical implementation on hardware remains under-explored. 
- Limited exploration of in-memory computing paradigms for handling frequent updates efficiently. 
- Cross-integration of diverse paradigms (e.g., DNNs and SNNs) on neuromorphic chips remains under-explored.</td><td>- Developing more efficient hardware designs and leverage SNN mapping for supporting NCL methods. 
- Introducing approximations in neuron parameters and synaptic weights to meet hardware constraints. 
- Exploring the potential of beyond-CMOS technologies (e.g., NVM) for more energy-efficient implementation. 
- Developing CIM systems with high-performance interfaces to support quick and frequent updates, minimizing latency and energy overheads. 
- Developing processors for supporting the combination of unsupervised local learning with supervised global learning (e.g., combining different conventional &amp; neuromorphic chips).</td></tr></table>

also be explored. Additionally, integration of hybrid SNN-DNN models, leveraging the strengths of both architectures, where DNNs handle feature extraction while SNNs process temporal or event-driven information to enhance CL performance in real-world applications can be explored. Moreover, knowledge distillation techniques like teacher-student to transfer knowledge from deep networks to SNNs, for efficient CL can be explored.

# C. ADAPTATION TO DYNAMIC INPUT PATTERNS

In dynamic environments, input data change unpredictably. Recent advancements leveraging STDP and active dendrites offer promising solutions. STDP adjusts synaptic strength based on spike timing, enabling efficient unsupervised learning and real-time adaptation without labeled data [42], [43]. Meanwhile, active dendrites enhance adaptability by dynamically selecting task-specific sub-networks via a gating mechanism [355], [411]. Despite these advancements, we identify that the existing techniques have not exploited temporal correlations in spiking patterns in inputs, hence hindering the network from achieving higher performance. To overcome this, there are several potential solutions, such as (1) adaptive learning with effective weight decay and weight updates, to improve the flexibility of neuron dynamics for adapting to input spikes; (2) clustering and representation learning based on the input patterns; and (3) adaptive algorithms to explore various configurations of

dendritic segments in active dendrite techniques to optimize task-specific adaptation.

# D. BALANCING CL DESIDERATA

To meet multiple, often conflicting, requirements of CL is extremely challenging, requiring trade-offs to satisfy all CL desiderata (i.e., scalability, no/minimal usage of old data, task-agnostic, positive forward and backward transfer, controlled forgetting, and fast adaptation/recovery). For example, improving learning quality for past tasks while minimizing the use of old data is non-trivial. Therefore, it is important to prioritize the desired characteristics based on the applications and balance them during the operational lifetime within acceptable performance.

# E. INPUT NOISE ROBUSTNESS

Noise in input data, such as low contrast, background interference, or additive white Gaussian noise (AWGN), can obscure important features and significantly impair learning efficiency, particularly in dynamic environments where noise patterns vary unpredictably. A recent study addressed this issue by implementing a selective attention mechanism that focuses on task-relevant features, leading to enhanced performance in noisy conditions [100]. However, its reliance on specific noise types, such as AWGN, limits its generalizability to more complex, non-linear noise patterns. To overcome this, future research should consider various

![](images/d73ea15635b6b0875db6c9ff219c8829917940a43f6b9a0c749de6941753f604.jpg)  
FIGURE 36. a) Setup on a drone in a UWB-equipped warehouse for ground truth localization, b) Event and radar data are processed by an STDP-trained SNN for loop closure detection in SLAM, with radar also modeling obstacles (black dots), and c) DVS-Radar Fusion for SNN-STDP based CL SLAM system [406].

![](images/f42ced6c7de46c8f432a98a5e195127e57df43552427a8b758c17b31b9675d64.jpg)  
FIGURE 37. Attention maps based CL system for people detection; adapted from studies in $[ 4 0 7 ] _ { * } ( \mathsf { a } )$ The DVS produces a stream of spikes over time and space. (b) A spike is emitted when the change in light intensity $\ ! L _ { i j }$ at pixel $( i , j )$ exceeds a certain threshold. The spike is positive if the change $\Delta L _ { j j } > 0$ and negative otherwise.(c) The SNN-STDP followed by a readout of neural activity is used to investigate the continuous development of attention-based perception.

noise types and intensities, ensuring robustness in realworld scenarios. Adaptive algorithms capable of real-time adjustments to varying noise conditions may also enhance

![](images/7c878e10680f75cce696268da837ab14098d5ae2de7a17b7c6c751cc36914151.jpg)  
FIGURE 38. Deployment of PAIBoard in a quadruped robot for autonomous navigation, where sensor fusion (UWB + vision) and hybrid SNNs enable robust real-time tracking and obstacle avoidance [391].

resilience. Furthermore, efficient pre-processing techniques and integration of high-resolution event-based sensors (e.g., DVS cameras) with conventional sensors (e.g., RGB camera) can also improve input data quality and robustness.

# F. DATA REPRESENTATION

Current NCL methods predominantly use rate coding to represent data, which is effective in some scenarios, but overlooks the temporal structure of spike trains. This limits the advantages of temporal information. Furthermore, studies on NCL methods with temporal coding is also underexplored. To address these challenges, future research may focus on incorporating temporal coding techniques with high information density (e.g., TTFS). Additionally, advancing hybrid encoding techniques that combine multiple encoding approaches may also improve performance, while optimizing latency and energy efficiency.

# G. SCALABILITY

Current CL methods incur significant memory and power/energy overheads when the networks get bigger, hence posing scalability issue. However, studies for realizing dynamic allocation of neurons without significant computational and memory overheads, as well as biologically inspired synaptic reorganization mechanisms are limited. To address these challenges, several actions can be taken, as follows.

1) Investigating the integration of more complex neuron models (e.g., Hodgkin-Huxley model) to enable richer representation of neuronal activity, thus potentially improving performance with good scalability.   
2) Exploring techniques to dynamically allocate neurons for new tasks while pruning redundant ones from previous tasks.   
3) Employing hierarchical or modular SNN design to enable scalable network architectures for CL.   
4) Investigating techniques for dynamic structural plasticity to enable reorganization of neural connections.

# H. LEARNING RULE DEVELOPMENTS

Current NCL methods often rely on non-local learning rules. While variations and enhancements of STDP for OCL

scenarios have shown promise, they remain under-explored. Additionally, current approaches primarily focus on a single learning paradigm, either supervised or unsupervised, which restricts the adaptability and overall performance of NCL methods. To address these limitations, future advancements should focus on developing advanced localized learning rules, such as adaptive variations of STDP, that enable SNNs to better retain past information while achieving quick learning convergence for new data in dynamic environments. Furthermore, hybrid learning approaches that integrate supervised and unsupervised paradigms could significantly enhance the training of SNNs, improving performance and adaptability in complex, real-world scenarios.

# I. GENERALIZATION CAPABILITY

Ensuring that NCL methods can function effectively across diverse tasks and operational settings remains an open challenge. To address this, future advancements should focus on developing adaptive NCL methods capable of dynamically adjusting to varied environmental contexts, such as transitions from indoor to outdoor conditions. For this, expanding the evaluation of NCL methods to diverse datasets is important to improve generalization for complex tasks, thereby enhancing their robustness and versatility in realworld applications.

# J. STANDARDIZED FRAMEWORK, EVALUATION DATASETS, AND BENCHMARKS

Research on neuromorphic datasets for benchmarking NCL is still in its early stage, and the existing datasets still have limitations, such as:

1) Inconsistent data pre-processing practices, e.g., varying time resolutions and image compression techniques, which impede fair comparisons across methods.   
2) Current datasets are predominantly small-scale and narrowly focused, limiting their generalizability and applicability to real-world tasks.   
3) Data transformation from conventional to event-based data (spikes) may fail to capture temporal information, thus limiting SNN capabilities.   
4) Most works do not specify the quantitative measurements of power/energy savings, latency and memory footprint for showing the NCL potential in practical real-world applications.

To address these limitations, following actions can be taken.

1) Developing standardized pre-processing protocols to ensure fairness and consistency in dataset comparisons.   
2) Creating large-scale, spatial-temporal event-based datasets tailored for diverse tasks, apart from the classification task, would improve benchmarking and enable the broader application of NCL methods.   
3) Constructing datasets emphasizing temporal dynamics, leveraging spike-based data generation.

4) Task-specific performance metrics, such as accuracy for classification, MAE for regression, memory ratio and power/energy overhead for scalability, adaptability scores for functionality and robustness under noise perturbations or quantization.   
5) Reporting and optimizing quantitative power/energy savings, latency and memory for showing the NCL potential in practical real-world applications.

# K. HARDWARE DEPLOYMENTS

Deployments of NCL methods should leverage the inherent low-power and massively-parallel processing strengths of the neuromorphic chips, thus maximizing the efficiency benefits. For instance, algorithm mapping policies on the given hardware accelerators hold an important role in determining the processing latency and efficiency. Additionally, the frequently updating parameters such as neuron thresholds, decay rates, membrane potentials, and synaptic weights, align well with the capabilities of neuromorphic hardware. However, the hardware deployments remains under-explored. Therefore, future research should focus on the following direction.

1) Developing more efficient hardware designs that fully utilize SNN unique properties.   
2) Incorporating approximations in SNN parameters and weights can also help meet hardware constraints.   
3) Exploration of beyond-CMOS technologies (e.g., NVMs like RRAM, PCM, and MRAM) for energyefficient hardware implementations is another promising direction.   
4) Developing CIM systems with high-performance interfaces to support quick and frequent updates, minimizing latency and energy overheads.   
5) Developing processors for supporting the combination of unsupervised local learning with supervised global learning (e.g., combining different conventional & neuromorphic chips).

To better align research focus with practical needs, we prioritize these challenges based on their relevance to real-world application domains such as robotics and autonomous vehicles/agents. Immediate ones include adaptive knowledge retention and transfer, input noise robustness, balancing CL desiderata and hardware-constrained deployments, each of which directly impacts system reliability and performance in dynamic environments. Medium-priority challenges such as dynamic input adaptation, scalability, hybrid SNN-DNN approaches, and the development of energy-efficient learning rules will enable broader applicability. Finally, long-term ones such as generalization capability, improved data representations, adaptation of DNN-based CL methods, and standardized benchmarking frameworks, will be essential for building robust neuromorphic intelligence. A structured roadmap prioritizing NCL challenges in relation to real-world deployment is illustrated in Fig. 39.

![](images/7003e1a179cfb12cd5a96815649147b4f65a0cab15e8c6ee43423f17422af8b6.jpg)  
FIGURE 39. Prioritized roadmap for NCL challenges in relation to real-world deployment.

# VI. CONCLUSION

This paper presented a comprehensive survey of CL, reviewing the state-of-the-art works in both DNN and SNNbased methods. Regarding the DNN-based methods, the survey focused on the hardware deployment challenges and discussed the need for energy-efficient CL approaches. Then, it provided an extensive technical background of low-power neuromorphic systems covering its key aspects. Regarding the SNN-based CL methods (i.e., NCL), the survey categorized them and provided their comparison with relevant DNN-based CL methods, discussed and categorized hybrid approaches and focused on efficiency enhancement techniques currently used in literature. Moreover, it included the current progress of real-world NCL applications in adaptive robots and autonomous vehicles covering a wide range of use-cases, and provided quantitative analysis. Furthermore, it reported prominent neuromorphic datasets, metrics and benchmarks, emphasizing the need for standardized benchmarks and evaluation protocols, and suggested additional metrics for NCL. Among the reviewed methods, architecture-based like DSD-SNN and SOR-SNN achieved high accuracy on image classification benchmarks like MNIST, CIFAR100 and ImageNet. Methods incorporating compressed latent replay like Replay4NCL exhibited better performance in Class-IL scenario with significant latency and energy savings in speech classification. Similarly, more biologically inspired methods such as SpikeDyn and lpSpikeCon offered significant gains in memory efficiency and inference cost for low-power embedded systems. Additionally, hybrid SNN-ANN approaches are emerging as promising directions for enabling scalable and efficient CL. Despite the notable progress in the NCL field, there is still a pressing need for ongoing and significant innovation to fully realize the potential of low-power neuromorphic systems in the design of energy-efficient CL systems. The open challenges were discussed along with future directions at the end of the survey. Notably, CL strategies developed for DNNs, such as EWC, GEM, and ER are not directly transferable to SNNs due to differences in training dynamics, data encoding, and the lack of differentiability. Addressing this gap requires the design of SNN-compatible learning rules that preserve

long-term knowledge while enabling online plasticity. Moreover, effective deployment of NCL methods on neuromorphic hardware remains constrained by architectural limitations, energy budgets, and on-chip learning capabilities for OCL. Future research should prioritize hardware-aware learning algorithms and standardized benchmarks to enable fair, reproducible evaluations across both domains.

# ACKNOWLEDGMENT

(Mishal Fatima Minhas and Rachmad Vidya Wicaksana Putra contributed equally to this work.)

# REFERENCES

[1] D. Kudithipudi et al., ‘‘Biological underpinnings for lifelong learning machines,’’ Nature Mach. Intell., vol. 4, no. 3, pp. 196–210, Mar. 2022.   
[2] M. Mermillod, A. Bugaiska, and P. Bonin, ‘‘The stability-plasticity dilemma: Investigating the continuum from catastrophic forgetting to age-limited learning effects,’’ Frontiers Psychol., vol. 4, May 2013, Art. no. 54654.   
[3] A. E. Takesian and T. K. Hensch, ‘‘Balancing plasticity/stability across brain development,’’ Prog. Brain Res., vol. 207, pp. 3–34, Jan. 2013.   
[4] S. J. Russell and P. Norvig, Artificial Intelligence: A Modern Approach. U.K.: Pearson Education, 2016.   
[5] D. Hassabis, D. Kumaran, C. Summerfield, and M. Botvinick, ‘‘Neuroscience-inspired artificial intelligence,’’ Neuron, vol. 95, no. 2, pp. 245–258, Jul. 2017.   
[6] B. M. Lake, T. D. Ullman, J. B. Tenenbaum, and S. J. Gershman, ‘‘Building machines that learn and think like people,’’ Behav. Brain Sci., vol. 40, Jun. 2017, Art. no. e253.   
[7] Y. LeCun, Y. Bengio, and G. Hinton, ‘‘Deep learning,’’ Nature, vol. 521, no. 7553, pp. 436–444, 2015.   
[8] A. Krizhevsky, I. Sutskever, and G. E. Hinton, ‘‘ImageNet classification with deep convolutional neural networks,’’ Commun. ACM, vol. 60, no. 6, pp. 84–90, May 2017.   
[9] E. Zangeneh, M. Rahmati, and Y. Mohsenzadeh, ‘‘Low resolution face recognition using a two-branch deep convolutional neural network architecture,’’ Expert Syst. Appl., vol. 139, Jan. 2020, Art. no. 112854.   
[10] G. E. Hinton, L. Deng, D. Yu, G. E. Dahl, A. Mohamed, N. Jaitly, A. Senior, V. Vanhoucke, P. Nguyen, T. N. Sainath, and B. Kingsbury, ‘‘Deep neural networks for acoustic modeling in speech recognition,’’ IEEE Signal Process. Mag., vol. 29, no. 6, pp. 82–97, Nov. 2012.   
[11] G. M. van de Ven, N. Soures, and D. Kudithipudi, ‘‘Continual learning and catastrophic forgetting,’’ 2024, arXiv:2403.05175.   
[12] R. French, ‘‘Catastrophic forgetting in connectionist networks,’’ Trends Cognit. Sci., vol. 3, no. 4, pp. 128–135, Apr. 1999.   
[13] M. McCloskey and N. J. Cohen, ‘‘Catastrophic interference in connectionist networks: The sequential learning problem,’’ Psychol. Learn. Motivat., vol. 24, pp. 109–165, Apr. 1989.

[14] R. Ratcliff, ‘‘Connectionist models of recognition memory: Constraints imposed by learning and forgetting functions,’’ Psychol. Rev., vol. 97, no. 2, pp. 285–308, 1990.   
[15] R. Hadsell, D. Rao, A. A. Rusu, and R. Pascanu, ‘‘Embracing change: Continual learning in deep neural networks,’’ Trends Cognit. Sci., vol. 24, no. 12, pp. 1028–1040, Dec. 2020.   
[16] L. Wang, X. Zhang, H. Su, and J. Zhu, ‘‘A comprehensive survey of continual learning: Theory, method and application,’’ IEEE Trans. Pattern Anal. Mach. Intell., vol. 46, no. 8, pp. 5362–5383, Aug. 2024.   
[17] G. I. Parisi, R. Kemker, J. L. Part, C. Kanan, and S. Wermter, ‘‘Continual lifelong learning with neural networks: A review,’’ Neural Netw., vol. 113, pp. 54–71, May 2019.   
[18] D. Kim and B. Han, ‘‘On the stability-plasticity dilemma of classincremental learning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2023, pp. 20196–20204.   
[19] W. C. Abraham and A. Robins, ‘‘Memory retention—The synaptic stability versus plasticity dilemma,’’ Trends Neurosci., vol. 28, no. 2, pp. 73–78, Feb. 2005.   
[20] Y. Li, W. Zhang, X. Xu, Y. He, D. Dong, N. Jiang, F. Wang, Z. Guo, S. Wang, C. Dou, Y. Liu, Z. Wang, and D. Shang, ‘‘Mixed-precision continual learning based on computational resistance random access memory,’’ Adv. Intell. Syst., vol. 4, no. 8, Aug. 2022, Art. no. 2200026.   
[21] F. Ye and A. G. Borş, ‘‘Learning latent representations across multiple data domains using lifelong VAEGAN,’’ in Proc. 16th Eur. Conf. Comput. Vis. (ECCV), Glasgow, U.K. Cham, Switzerland: Springer, Jan. 2020, pp. 777–795.   
[22] X. Liu, C. Wu, M. Menta, L. Herranz, B. Raducanu, A. D. Bagdanov, S. Jui, and J. van de Weijer, ‘‘Generative feature replay for classincremental learning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. Workshops (CVPRW), Jun. 2020, pp. 915–924.   
[23] G. M. van de Ven, H. T. Siegelmann, and A. S. Tolias, ‘‘Brain-inspired replay for continual learning with artificial neural networks,’’ Nature Commun., vol. 11, no. 1, p. 4069, Aug. 2020.   
[24] H. Hu, A. Li, D. Calandriello, and D. Gorur, ‘‘One pass ImageNet,’’ 2021, arXiv:2111.01956.   
[25] Y. Min, K. Ahn, and N. Azizan, ‘‘One-pass learning via bridging orthogonal gradient descent and recursive least-squares,’’ in Proc. IEEE 61st Conf. Decis. Control (CDC), Dec. 2022, pp. 4720–4725.   
[26] J. Ye, Y. Fu, J. Song, X. Yang, S. Liu, X. Jin, M. Song, and X. Wang, ‘‘Learning with recoverable forgetting,’’ in Proc. Eur. Conf. Comput. Vis. Cham, Switzerland: Springer, Jan. 2022, pp. 87–103.   
[27] T. Shibata, G. Irie, D. Ikami, and Y. Mitsuzumi, ‘‘Learning with selective forgetting,’’ in Proc. 30th Int. Joint Conf. Artif. Intell., Aug. 2021, pp. 989–996.   
[28] M. Y. Harun, J. Gallardo, T. L. Hayes, and C. Kanan, ‘‘How efficient are today’s continual learning algorithms?’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., Jun. 2023, pp. 2430–2435.   
[29] K. Roy, A. Jaiswal, and P. Panda, ‘‘Towards spike-based machine intelligence with neuromorphic computing,’’ Nature, vol. 575, no. 7784, pp. 607–617, Nov. 2019.   
[30] C. D. Schuman, S. R. Kulkarni, M. Parsa, J. P. Mitchell, P. Date, and B. Kay, ‘‘Opportunities for neuromorphic computing algorithms and applications,’’ Nature Comput. Sci., vol. 2, no. 1, pp. 10–19, Jan. 2022.   
[31] A. Shrestha, H. Fang, Z. Mei, D. P. Rider, Q. Wu, and Q. Qiu, ‘‘A survey on neuromorphic computing: Models and hardware,’’ IEEE Circuits Syst. Mag., vol. 22, no. 2, pp. 6–35, 2nd Quart., 2022.   
[32] J. Zhu, T. Zhang, Y. Yang, and R. Huang, ‘‘A comprehensive review on emerging artificial neuromorphic devices,’’ Appl. Phys. Rev., vol. 7, no. 1, Mar. 2020, Art. no. 011312.   
[33] G. Lagani, R. Mazziotti, F. Falchi, C. Gennaro, G. M. Cicchini, T. Pizzorusso, F. Cremisi, and G. Amato, ‘‘Assessing pattern recognition performance of neuronal cultures through accurate simulation,’’ in Proc. 10th Int. IEEE/EMBS Conf. Neural Eng. (NER), May 2021, pp. 726–729.   
[34] R. V. W. Putra, P. Wickramasinghe, and M. Shafique, ‘‘Enabling efficient processing of spiking neural networks with on-chip learning on commodity neuromorphic processors for edge AI systems,’’ 2025, arXiv:2504.00957.   
[35] R. Mishra and M. Suri, ‘‘A survey and perspective on neuromorphic continual learning systems,’’ Frontiers Neurosci., vol. 17, May 2023, Art. no. 1149410.   
[36] J. D. Nunes, M. Carvalho, D. Carneiro, and J. S. Cardoso, ‘‘Spiking neural networks: A survey,’’ IEEE Access, vol. 10, pp. 60738–60764, 2022.

[37] W. Gerstner and W. M. Kistler, Spiking Neuron Models: Single Neurons, Populations, Plasticity. U.K.: Cambridge Univ. Press, 2002.   
[38] W. Maass, ‘‘Networks of spiking neurons: The third generation of neural network models,’’ Neural Netw., vol. 10, no. 9, pp. 1659–1671, Dec. 1997.   
[39] M. Pfeiffer and T. Pfeil, ‘‘Deep learning with spiking neurons: Opportunities and challenges,’’ Frontiers Neurosci., vol. 12, Oct. 2018, Art. no. 409662.   
[40] A. Tavanaei, M. Ghodrati, S. R. Kheradpisheh, T. Masquelier, and A. Maida, ‘‘Deep learning in spiking neural networks,’’ Neural Netw., vol. 111, pp. 47–63, Mar. 2019.   
[41] S. Song, K. D. Miller, and L. F. Abbott, ‘‘Competitive Hebbian learning through spike-timing-dependent synaptic plasticity,’’ Nature Neurosci., vol. 3, no. 9, pp. 919–926, Sep. 2000.   
[42] R. V. W. Putra and M. Shafique, ‘‘SpikeDyn: A framework for energyefficient spiking neural networks with continual and unsupervised learning capabilities in dynamic environments,’’ in Proc. 58th ACM/IEEE Design Autom. Conf. (DAC), Dec. 2021, pp. 1057–1062.   
[43] R. V. W. Putra and M. Shafique, ‘‘LpSpikeCon: Enabling low-precision spiking neural network processing for efficient unsupervised continual learning on autonomous agents,’’ in Proc. Int. Joint Conf. Neural Netw. (IJCNN), Jul. 2022, pp. 1–8.   
[44] H. Qu, H. Rahmani, L. Xu, B. Williams, and J. Liu, ‘‘Recent advances of continual learning in computer vision: An overview,’’ 2021, arXiv:2109.11369.   
[45] M. De Lange, R. Aljundi, M. Masana, S. Parisot, X. Jia, A. Leonardis, G. Slabaugh, and T. Tuytelaars, ‘‘A continual learning survey: Defying forgetting in classification tasks,’’ IEEE Trans. Pattern Anal. Mach. Intell., vol. 44, no. 7, pp. 3366–3385, Jul. 2022.   
[46] Z. Mai, R. Li, J. Jeong, D. Quispe, H. Kim, and S. Sanner, ‘‘Online continual learning in image classification: An empirical survey,’’ Neurocomputing, vol. 469, pp. 28–51, Jan. 2022.   
[47] M. Masana, X. Liu, B. Twardowski, M. Menta, A. D. Bagdanov, and J. van de Weijer, ‘‘Class-incremental learning: Survey and performance evaluation on image classification,’’ IEEE Trans. Pattern Anal. Mach. Intell., vol. 45, no. 5, pp. 5513–5533, May 2023.   
[48] J. A. Mendez and E. Eaton, ‘‘How to reuse and compose knowledge for a lifetime of tasks: A survey on continual learning and functional composition,’’ 2022, arXiv:2207.07730.   
[49] Z. Ke and B. Liu, ‘‘Continual learning of natural language processing tasks: A survey,’’ 2022, arXiv:2211.12701.   
[50] D. Zhang, S. Jia, and Q. Wang, ‘‘Recent advances and new frontiers in spiking neural networks,’’ 2022, arXiv:2204.07050.   
[51] K. Shaheen, M. A. Hanif, O. Hasan, and M. Shafique, ‘‘Continual learning for real-world autonomous systems: Algorithms, challenges and frameworks,’’ J. Intell. Robotic Syst., vol. 105, no. 1, p. 9, May 2022.   
[52] Z. Wang, E. Yang, L. Shen, and H. Huang, ‘‘A comprehensive survey of forgetting in deep learning beyond continual learning,’’ IEEE Trans. Pattern Anal. Mach. Intell., vol. 47, no. 3, pp. 1464–1483, Mar. 2025.   
[53] B. Wickramasinghe, G. Saha, and K. Roy, ‘‘Continual learning: A review of techniques, challenges, and future directions,’’ IEEE Trans. Artif. Intell., vol. 5, no. 6, pp. 2526–2546, Jun. 2024.   
[54] D.-W. Zhou, Q. Wang, Z. Qi, H.-J. Ye, D. Zhan, and Z. Liu, ‘‘Classincremental learning: A survey,’’ IEEE Trans. Pattern Anal. Mach. Intell., vol. 46, no. 12, pp. 9851–9873, Jul. 2024.   
[55] A. Safa, ‘‘Continual learning with Hebbian plasticity in sparse and predictive coding networks: A survey and perspective,’’ 2024, arXiv:2407.17305.   
[56] H. Shi, Z. Xu, H. Wang, W. Qin, W. Wang, Y. Wang, Z. Wang, S. Ebrahimi, and H. Wang, ‘‘Continual learning of large language models: A comprehensive survey,’’ Apr. 2024, arXiv:2404.16789.   
[57] D.-W. Zhou, H.-L. Sun, J. Ning, H.-J. Ye, and D.-C. Zhan, ‘‘Continual learning with pre-trained models: A survey,’’ 2024, arXiv:2401.16386.   
[58] S. Li, T. Su, X.-Y. Zhang, and Z. Wang, ‘‘Continual learning with knowledge distillation: A survey,’’ IEEE Trans. Neural Netw. Learn. Syst., vol. 36, no. 6, pp. 9798–9818, Jun. 2025.   
[59] D. Yu, X. Zhang, Y. Chen, A. Liu, Y. Zhang, P. S. Yu, and I. King, ‘‘Recent advances of multimodal continual learning: A comprehensive survey,’’ 2024, arXiv:2410.05352.   
[60] Y. Yang, J. Zhou, X. Ding, T. Huai, S. Liu, Q. Chen, Y. Xie, and L. He, ‘‘Recent advances of foundation language models-based continual learning: A survey,’’ ACM Comput. Surv., vol. 57, no. 5, pp. 1–38, May 2025.

[61] D. Silver, A. Huang, C. J. Maddison, A. Guez, L. Sifre, G. van den Driessche, J. Schrittwieser, I. Antonoglou, V. Panneershelvam, M. Lanctot, S. Dieleman, D. Grewe, J. Nham, N. Kalchbrenner, I. Sutskever, T. Lillicrap, M. Leach, K. Kavukcuoglu, T. Graepel, and D. Hassabis, ‘‘Mastering the game of go with deep neural networks and tree search,’’ Nature, vol. 529, no. 7587, pp. 484–489, Jan. 2016.   
[62] K. E. Nikolakakis, A. Karbasi, and D. Kalogerias, ‘‘Select without fear: Almost all mini-batch schedules generalize optimally,’’ 2023, arXiv:2305.02247.   
[63] H. Qi, F. Wang, and H. Wang, ‘‘Statistical analysis of fixed mini-batch gradient descent estimator,’’ J. Comput. Graph. Statist., vol. 32, no. 4, pp. 1348–1360, Oct. 2023.   
[64] A. Galdeano, A. Gonnot, C. Cottet, S. Hassas, M. Lefort, and A. Cordier, ‘‘Developmental learning for social robots in real-world interactions,’’ in Proc. 1st Workshop Social Robots Wild 13th Annu. ACM/IEEE Int. Conf. Hum.-Robot Interact. (HRI), Mar. 2018, p. 5.   
[65] G. Wu, S. Gong, and P. L. Queen, ‘‘Striking a balance between stability and plasticity for class-incremental learning,’’ in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2021, pp. 1104–1113.   
[66] F. Zenke, B. Poole, and S. Ganguli, ‘‘Continual learning through synaptic intelligence,’’ in Proc. Int. Conf. Mach. Learn., Jan. 2017, pp. 3987–3995.   
[67] O. Ostapenko, M. Puscas, T. Klein, P. Jähnichen, and M. Nabi, ‘‘Learning to remember: A synaptic plasticity driven framework for continual learning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2019, pp. 11313–11321.   
[68] L. Wang, X. Zhang, K. Yang, L. Yu, C. Li, L. Hong, S. Zhang, Z. Li, Y. Zhong, and J. Zhu, ‘‘Memory replay with data compression for continual learning,’’ 2022, arXiv:2202.06592.   
[69] J. Serra, D. Surís, M. Miron, and A. Karatzoglou, ‘‘Overcoming catastrophic forgetting with hard attention to the task,’’ in Proc. Int. Conf. Mach. Learn., Jan. 2018, pp. 4548–4557.   
[70] J. Kirkpatrick, R. Pascanu, N. C. Rabinowitz, J. Veness, G. Desjardins, A. A. Rusu, K. Milan, J. Quan, T. Ramalho, A. Grabska-Barwińska, D. Hassabis, C. Clopath, D. Kumaran, and R. Hadsell, ‘‘Overcoming catastrophic forgetting in neural networks,’’ Proc. Nat. Acad. Sci. USA, vol. 114, no. 13, pp. 3521–3526, Mar. 2017.   
[71] D. Paul, D. Sorokin, and J. Gaspers, ‘‘Class incremental learning for intent classification with limited or no old data,’’ in Proc. The 1st Workshop Ever Evolving NLP (EvoNLP), 2022, pp. 16–25.   
[72] N. Asadi, M. Davar, S. P. Mudur, R. Aljundi, and E. Belilovsky, ‘‘Prototype-sample relation distillation: Towards replay-free continual learning,’’ in Proc. Int. Conf. Mach. Learn., Jan. 2023, pp. 1093–1106.   
[73] X. Li, S. Wang, J. Sun, and Z. Xu, ‘‘Variational data-free knowledge distillation for continual learning,’’ IEEE Trans. Pattern Anal. Mach. Intell., vol. 45, no. 10, pp. 12618–12634, Oct. 2023.   
[74] Z. Wang, D. Li, and P. Li, ‘‘Latent coreset sampling based data-free continual learning,’’ in Proc. 31st ACM Int. Conf. Inf. Knowl. Manage., Oct. 2022, pp. 2077–2087.   
[75] Y. Yang, Z. Cui, J. Xu, C. Zhong, W.-S. Zheng, and R. Wang, ‘‘Continual learning with Bayesian model based on a fixed pre-trained feature extractor,’’ Vis. Intell., vol. 1, no. 1, p. 5, 2023.   
[76] D. Goswami, Y. Liu, B. Twardowski, and J. van de Weijer, ‘‘FeCAM: Exploiting the heterogeneity of class distributions in exemplar-free continual learning,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 36, Jan. 2023, pp. 6582–6595.   
[77] C. Zeno, I. Golan, E. Hoffer, and D. Soudry, ‘‘Task agnostic continual learning using online variational Bayes,’’ 2018, arXiv:1803.10123.   
[78] X. He, J. Sygnowski, A. Galashov, A. A. Rusu, Y. Whye Teh, and R. Pascanu, ‘‘Task agnostic continual learning via meta learning,’’ 2019, arXiv:1906.05201.   
[79] S. Lee, J. Ha, D. Zhang, and G. Kim, ‘‘A neural Dirichlet process mixture model for task-free continual learning,’’ 2020, arXiv:2001.00689.   
[80] P. Kirichenko, M. Farajtabar, D. Rao, B. Lakshminarayanan, N. Levine, A. Li, H. Hu, A. G. Wilson, and R. Pascanu, ‘‘Task-agnostic continual learning with hybrid probabilistic models,’’ 2021, arXiv:2106.12772.   
[81] H. Zhu, M. Majzoubi, A. Jain, and A. Choromanska, ‘‘TAME: Task agnostic continual learning using multiple experts,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. Workshops (CVPRW), Jun. 2024, pp. 4139–4148.   
[82] H. Hihn and D. A. Braun, ‘‘Hierarchically structured task-agnostic continual learning,’’ Mach. Learn., vol. 112, no. 2, pp. 655–686, Feb. 2023.

[83] F. Ye and A. G. Bors, ‘‘Dynamic scalable self-attention ensemble for task-free continual learning,’’ in Proc. ICASSP - IEEE Int. Conf. Acoust., Speech Signal Process. (ICASSP), Jun. 2023, pp. 1–5.   
[84] G. Bravo-Rocca, P. Liu, J. Guitart, A. Dholakia, and D. Ellison, ‘‘TADIL: Task-agnostic domain-incremental learning through task-ID inference using transformer nearest-centroid embeddings,’’ 2023, arXiv:2306.11955.   
[85] J. Chen, T. Nguyen, D. Gorur, and A. Chaudhry, ‘‘Is forgetting less a good inductive bias for forward transfer?’’ 2023, arXiv:2303.08207.   
[86] S. V. Mehta, D. Patil, S. Chandar, and E. Strubell, ‘‘An empirical investigation of the role of pre-training in lifelong learning,’’ J. Mach. Learn. Res., vol. 24, no. 214, pp. 1–50, Jan. 2021.   
[87] K. Javed and M. White, ‘‘Meta-learning representations for continual learning,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 32, Jan. 2019, pp. 1818–1828.   
[88] M. Riemer, I. Cases, R. Ajemian, M. Liu, I. Rish, Y. Tu, and G. Tesauro, ‘‘Learning to learn without forgetting by maximizing transfer and minimizing interference,’’ in Proc. Int. Conf. Learn. Represent., Jan. 2018, pp. 6470–6479.   
[89] D. López-Paz and M. Ranzato, ‘‘Gradient episodic memory for continual learning,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 30, Jan. 2017.   
[90] L. Wang, M. Zhang, Z. Jia, Q. Li, C. Bao, K. Ma, J. Zhu, and Y. Zhong, ‘‘AFEC: Active forgetting of negative transfer in continual learning,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 34, Jan. 2021, pp. 22379–22391.   
[91] M. Boschini, L. Bonicelli, A. Porrello, G. Bellitto, M. Pennisi, S. Palazzo, C. Spampinato, and S. Calderara, ‘‘Transfer without forgetting,’’ in Proc. Eur. Conf. Comput. Vis. Cham, Switzerland: Springer, Jan. 2022, pp. 692–709.   
[92] A. A. Rusu, N. C. Rabinowitz, G. Desjardins, H. Soyer, J. Kirkpatrick, K. Kavukcuoglu, R. Pascanu, and R. Hadsell, ‘‘Progressive neural networks,’’ 2016, arXiv:1606.04671.   
[93] C. Fernando, D. Banarse, C. Blundell, Y. Zwols, D. Ha, A. A. Rusu, A. Pritzel, and D. Wierstra, ‘‘PathNet: Evolution channels gradient descent in super neural networks,’’ 2017, arXiv:1701.08734.   
[94] G. Sokar, D. C. Mocanu, and M. Pechenizkiy, ‘‘Avoiding forgetting and allowing forward transfer in continual learning via sparse networks,’’ in Proc. Joint Eur. Conf. Mach. Learn. Knowl. Discovery Databases. Cham, Switzerland: Springer, Jan. 2023, pp. 85–101.   
[95] L. Gravitz, ‘‘The forgotten part of memory,’’ Nature, vol. 571, no. 7766, pp. S12–S14, Jul. 2019.   
[96] H. Ahn, S. Cha, D.-G. Lee, and T. Moon, ‘‘Uncertainty-based continual learning with adaptive regularization,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 33, Jan. 2019, pp. 4392–4402.   
[97] S. Golkar, M. Kagan, and K. Cho, ‘‘Continual learning via neural pruning,’’ 2019, arXiv:1903.04476.   
[98] J. Schwarz, W. M. Czarnecki, J. Luketina, A. Grabska-Barwińska, Y. W. Teh, R. Pascanu, and R. Hadsell, ‘‘Progress & compress: A scalable framework for continual learning,’’ in Proc. Int. Conf. Mach. Learn., Jul. 2018, pp. 4528–4537.   
[99] J. M. Allred and K. Roy, ‘‘Controlled forgetting: Targeted stimulation and dopaminergic plasticity modulation for unsupervised lifelong learning in spiking neural networks,’’ Frontiers Neurosci., vol. 14, p. 7, Jan. 2020.   
[100] P. Panda, J. M. Allred, S. Ramanathan, and K. Roy, ‘‘ASP: Learning to forget with adaptive synaptic plasticity in spiking neural networks,’’ IEEE J. Emerg. Sel. Topics Circuits Syst., vol. 8, no. 1, pp. 51–64, Mar. 2018.   
[101] C. Finn, P. Abbeel, and S. Levine, ‘‘Model-agnostic meta-learning for fast adaptation of deep networks,’’ in Proc. Int. Conf. Mach. Learn., Jan. 2017, pp. 1126–1135.   
[102] R. Pandey, S. K. Khatri, N. K. Singh, and P. Verma, Artificial Intelligence and Machine Learning for Edge Computing. U.K.: Academic, 2022.   
[103] J. Xu and Z. Zhu, ‘‘Reinforced continual learning,’’ in Proc. Adv. Neural Inf. Process. Syst. (NeurIPS), vol. 31, 2018, pp. 899–908.   
[104] R. S. Sutton and A. G. Barto, Reinforcement Learning: An Introduction. London, U.K.: The MIT Press, 2018.   
[105] A. Chaudhry, P. K. Dokania, T. Ajanthan, and P. H. S. Torr, ‘‘Riemannian walk for incremental learning: Understanding forgetting and intransigence,’’ in Proc. Eur. Conf. Comput. Vis. (ECCV), Jan. 2018, pp. 556–572.   
[106] S.-A. Rebuffi, A. Kolesnikov, G. Sperl, and C. H. Lampert, ‘‘ICaRL: Incremental classifier and representation learning,’’ in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Jul. 2017, pp. 5533–5542.   
[107] S. Hou, X. Pan, C. C. Loy, Z. Wang, and D. Lin, ‘‘Learning a unified classifier incrementally via rebalancing,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2019, pp. 831–839.

[108] Q. Liu, T. Zhang, M. Hemmatpour, H. Qiu, D. Zhang, C. S. Chen, M. Mellia, and A. Aghasaryan, ‘‘Operationalizing AI in future networks: A bird’s eye view from the system perspective,’’ 2023, arXiv:2303.04073.   
[109] Y.-C. Hsu, Y.-C. Liu, A. Ramasamy, and Z. Kira, ‘‘Re-evaluating continual learning scenarios: A categorization and case for strong baselines,’’ 2018, arXiv:1810.12488.   
[110] G. M. van de Ven and A. S. Tolias, ‘‘Three scenarios for continual learning,’’ 2019, arXiv:1904.07734.   
[111] G. M. van de Ven, T. Tuytelaars, and A. S. Tolias, ‘‘Three types of incremental learning,’’ Nature Mach. Intell., vol. 4, no. 12, pp. 1185–1197, Dec. 2022.   
[112] V. Lomonaco and D. Maltoni, ‘‘CORe50: A new dataset and benchmark for continuous object recognition,’’ in Proc. Conf. Robot. Learn., Oct. 2017, pp. 17–26.   
[113] R. Aljundi, M. Lin, B. Goujaud, and Y. Bengio, ‘‘Gradient based sample selection for online continual learning,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 32, 2019, pp. 11817–11826.   
[114] R. Aljundi, E. Belilovsky, T. Tuytelaars, L. Charlin, M. Caccia, M. Lin, and L. Page-Caccia, ‘‘Online continual learning with maximal interfered retrieval,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 32, Jan. 2019, pp. 11849–11860.   
[115] L. Jing and Y. Tian, ‘‘Self-supervised visual feature learning with deep neural networks: A survey,’’ IEEE Trans. Pattern Anal. Mach. Intell., vol. 43, no. 11, pp. 4037–4058, Nov. 2021.   
[116] T. Chen, S. Kornblith, M. Norouzi, and G. E. Hinton, ‘‘A simple framework for contrastive learning of visual representations,’’ in Proc. Int. Conf. Mach. Learn., Jan. 2020, pp. 1597–1607.   
[117] Q. Pham, L. Chenghao, and S. C. H. Hoi, ‘‘DualNet: Continual learning, fast and slow,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 34, Jan. 2021, pp. 16131–16144.   
[118] D. Madaan, J. Yoon, Y. Li, Y. Liu, and S. J. Hwang, ‘‘Representational continuity for unsupervised continual learning,’’ 2021, arXiv:2110.06976.   
[119] J. Gallardo, T. L. Hayes, and C. Kanan, ‘‘Self-supervised training enhances online continual learning,’’ 2021, arXiv:2103.14010.   
[120] S. Purushwalkam, P. Morgado, and A. Gupta, ‘‘The challenges of continuous self-supervised learning,’’ in Proc. Eur. Conf. Comput. Vis. Cham, Switzerland: Springer, Jan. 2022, pp. 702–721.   
[121] E. Fini, V. G. T. Da Costa, X. Alameda-Pineda, E. Ricci, K. Alahari, and J. Mairal, ‘‘Self-supervised models are continual learners,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2022, pp. 9611–9620.   
[122] H. Cha, J. Lee, and J. Shin, ‘‘Co2L: Contrastive continual learning,’’ in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2021, pp. 9496–9505.   
[123] N. Vödisch, D. Cattaneo, W. Burgard, and A. Valada, ‘‘Continual SLAM: Beyond lifelong simultaneous localization and mapping through continual learning,’’ in Proc. Int. Symp. Robot. Res. Cham, Switzerland: Springer, Jan. 2023, pp. 19–35.   
[124] V. V. Ramasesh, A. Lewkowycz, and E. Dyer, ‘‘Effect of scale on catastrophic forgetting in neural networks,’’ in Proc. Int. Conf. Learn. Represent., 2021.   
[125] O. Ostapenko, T. Lesort, P. Rodríguez, M. R. Arefin, A. Douillard, I. Rish, and L. Charlin, ‘‘Continual learning with foundation models: An empirical study of latent replay,’’ in Proc. Conf. Lifelong Learn. Agents, Jan. 2022, pp. 60–91.   
[126] M. Davari, N. Asadi, S. Mudur, R. Aljundi, and E. Belilovsky, ‘‘Probing representation forgetting in supervised and unsupervised continual learning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2022, pp. 16691–16700.   
[127] J. O. Zhang, A. F. Sax, A. Zamir, L. Guibas, and J. Malik, ‘‘Side-tuning: A baseline for network adaptation via additive side networks,’’ in Proc. 16th Eur. Conf. Comput. Vis. (ECCV), Glasgow, U.K. Cham, Switzerland: Springer, Aug. 2020, pp. 698–714.   
[128] H. Shon, J. Lee, S. H. Kim, and J. Kim, ‘‘DLCFT: Deep linear continual fine-tuning for general incremental learning,’’ in Proc. Eur. Conf. Comput. Vis., Jan. 2022, pp. 513–529.   
[129] Y. Cong, M. Zhao, J. Li, S. Wang, and L. Carin, ‘‘GAN memory with no forgetting,’’ in Proc. Adv. Neural Inf. Process. Syst., Jan. 2020, pp. 16481–16494.   
[130] B. Ermis, G. Zappella, M. Wistuba, and C. Archambeau, ‘‘Memory efficient continual learning with transformers,’’ in Proc. Adv. Neural Inf. Process. Syst., Jan. 2022, pp. 10629–10642.

[131] Z. Wang, Z. Zhang, C.-Y. Lee, H. Zhang, R. Sun, X. Ren, G. Su, V. Perot, J. Dy, and T. Pfister, ‘‘Learning to prompt for continual learning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2022, pp. 139–149.   
[132] J. S. Smith, L. Karlinsky, V. Gutta, P. Cascante-Bonilla, D. Kim, A. Arbelle, R. Panda, R. Feris, and Z. Kira, ‘‘CODA-prompt: Continual decomposed attention-based prompting for rehearsal-free continual learning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2023, pp. 11909–11919.   
[133] Z. Wang, Z. Zhang, S. Ebrahimi, R. Sun, H. Zhang, C.-Y. Lee, X. Ren, G. Su, V. Pérot, J. Dy, and T. Pfister, ‘‘DualPrompt: Complementary prompting for rehearsal-free continual learning,’’ in Proc. Eur. Conf. Comput. Vis., Jan. 2022, pp. 631–648.   
[134] Y. Wang, Z. Huang, and X. Hong, ‘‘S-prompts learning with pre-trained transformers: An occam’s Razor for domain incremental learning,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 35, 2022, pp. 5682–5695.   
[135] A. Razdaibiedina, Y. Mao, R. Hou, M. Khabsa, M. Lewis, and A. Almahairi, ‘‘Progressive prompts: Continual learning for language models,’’ 2023, arXiv:2301.12314.   
[136] L. Wang, J. Xie, X. Zhang, H. Su, and J. Zhu, ‘‘HiDe-PET: Continual learning via hierarchical decomposition of parameter-efficient tuning,’’ 2024, arXiv:2407.05229.   
[137] P. Janson, W. Zhang, R. Aljundi, and M. Elhoseiny, ‘‘A simple baseline that questions the use of pretrained-models in continual learning,’’ 2022, arXiv:2210.04428.   
[138] F. Pelosin, ‘‘Simpler is better: Off-the-shelf continual learning through pretrained backbones,’’ 2022, arXiv:2205.01586.   
[139] A. Panos, Y. Kobe, D. O. Reino, R. Aljundi, and R. E. Turner, ‘‘First session adaptation: A strong replay-free baseline for class-incremental learning,’’ in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2023, pp. 18774–18784.   
[140] G. Shi, J. Chen, W. Zhang, L.-M. Zhan, and X.-M. Wu, ‘‘Overcoming catastrophic forgetting in incremental few-shot learning by finding flat minima,’’ in Proc. Adv. Neural Inf. Process. Syst., Jan. 2021, pp. 6747–6761.   
[141] Y. Shi, K. Zhou, J. Liang, Z. Jiang, J. Feng, P. Torr, S. Bai, and V. Y. F. Tan, ‘‘Mimicking the oracle: An initial phase decorrelation approach for class incremental learning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2022, pp. 16701–16710.   
[142] P. Foret, A. Kleiner, H. Mobahi, and B. Neyshabur, ‘‘Sharpnessaware minimization for efficiently improving generalization,’’ 2020, arXiv:2010.01412.   
[143] G. Zhang, L. Wang, G. Kang, L. Chen, and Y. Wei, ‘‘SLCA: Slow learner with classifier alignment for continual learning on a pre-trained model,’’ in Proc. IEEE/CVF Int. Conf. Comput. Vis., Jul. 2023, pp. 19148–19158.   
[144] V. Marsocci and S. Scardapane, ‘‘Continual barlow twins: Continual self-supervised learning for remote sensing semantic segmentation,’’ IEEE J. Sel. Topics Appl. Earth Observ. Remote Sens., vol. 16, pp. 5049–5060, 2023.   
[145] S. Yan, L. Hong, H. Xu, J. Han, T. Tuytelaars, Z. Li, and X. He, ‘‘Generative negative text replay for continual vision-language pretraining,’’ in Proc. Eur. Conf. Comput. Vis. Cham, Switzerland: Springer, Jan. 2022, pp. 22–38.   
[146] Q. Liu, O. Majumder, A. Achille, A. Ravichandran, R. Bhotika, and S. Soatto, ‘‘Incremental few-shot meta-learning via indirect discriminant alignment,’’ in Proc. 16th Eur. Conf. Comput. Vis. (ECCV), Glasgow, U.K. Cham, Switzerland: Springer, Jan. 2020, pp. 685–701.   
[147] Z. Wang, L. Shen, L. Fang, Q. Suo, D. Zhan, T. Duan, and M. Gao, ‘‘Meta-learning with less forgetting on large-scale non-stationary task distributions,’’ in Proc. Eur. Conf. Comput. Vis. Cham, Switzerland: Springer, Jan. 2022, pp. 221–238.   
[148] K. Chen and C.-G. Lee, ‘‘Incremental few-shot learning via vector quantization in deep embedded space,’’ in Proc. Int. Conf. Learn. Represent., May 2021.   
[149] Y. Toda, K. Ozasa, and T. Matsuno, ‘‘Growing neural gas based navigation system in unknown terrain environment for an autonomous mobile robot,’’ Artif. Life Robot., vol. 28, no. 1, pp. 76–88, Feb. 2023.   
[150] A. Cossu, A. Carta, L. Passaro, V. Lomonaco, T. Tuytelaars, and D. Bacciu, ‘‘Continual pre-training mitigates forgetting in language and vision,’’ Neural Netw., vol. 179, Nov. 2024, Art. no. 106492.   
[151] R. Aljundi, F. Babiloni, M. Elhoseiny, M. Rohrbach, and T. Tuytelaars, ‘‘Memory aware synapses: Learning what (not) to forget,’’ in Proc. Eur. Conf. Comput. Vis. (ECCV), Nov. 2017, pp. 139–154.

[152] S.-W. Lee, J.-H. Kim, J.-H. Jun, J.-W. Ha, and B. Zhang, ‘‘Overcoming catastrophic forgetting by incremental moment matching,’’ in Proc. Adv. Neural Inf. Process. Syst., Jan. 2017, pp. 4655–4665.   
[153] J. Lee, D. Joo, H. G. Hong, and J. Kim, ‘‘Residual continual learning,’’ in Proc. AAAI Conf. Artif. Intell., Apr. 2020, vol. 34, no. 4, pp. 4553–4560.   
[154] X. Liu, M. Masana, L. Herranz, J. Van de Weijer, A. M. López, and A. D. Bagdanov, ‘‘Rotate your networks: Better weight consolidation and less catastrophic forgetting,’’ in Proc. 24th Int. Conf. Pattern Recognit. (ICPR), Aug. 2018, pp. 2262–2268.   
[155] J. Lee, H. G. Hong, D. Joo, and J. Kim, ‘‘Continual learning with extended kronecker-factored approximate curvature,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2020, pp. 8998–9007.   
[156] D. Park, S. Hong, B. Han, and K. M. Lee, ‘‘Continual learning by asymmetric loss approximation with single-side overestimation,’’ in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2019, pp. 3334–3343.   
[157] C. V. Nguyen, Y. Li, T. D. Bui, and R. E. Turner, ‘‘Variational continual learning,’’ 2017, arXiv:1710.10628.   
[158] T. Adel, H. Zhao, and R. E. Turner, ‘‘Continual learning with adaptive weights (CLAW),’’ 2019, arXiv:1911.09514.   
[159] N. Loo, S. Swaroop, and R. E. Turner, ‘‘Generalized variational continual learning,’’ 2020, arXiv:2011.12328.   
[160] S. Kapoor, T. Karaletsos, and T. D. Bui, ‘‘Variational auto-regressive Gaussian processes for continual learning,’’ in Proc. Int. Conf. Mach. Learn., Jan. 2020, pp. 5290–5300.   
[161] I. Paik, S. Oh, T.-Y. Kwak, and I. Kim, ‘‘Overcoming catastrophic forgetting by neuron-level plasticity control,’’ in Proc. AAAI Conf. Artif. Intell., Jan. 2020, vol. 34, no. 4, pp. 5339–5346.   
[162] S. Jung, H. Ahn, S. Cha, and T. Moon, ‘‘Continual learning with nodeimportance based adaptive group sparse regularization,’’ in Proc. Adv. Neural Inf. Process. Syst., Jan. 2020, pp. 3647–3658.   
[163] Z. Li and D. Hoiem, ‘‘Learning without forgetting,’’ IEEE Trans. Pattern Anal. Mach. Intell., vol. 40, no. 12, pp. 2935–2947, Dec. 2018.   
[164] P. Dhar, R. V. Singh, K.-C. Peng, Z. Wu, and R. Chellappa, ‘‘Learning without memorizing,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2019, pp. 5133–5141.   
[165] A. Rannen, R. Aljundi, M. B. Blaschko, and T. Tuytelaars, ‘‘Encoder based lifelong learning,’’ in Proc. IEEE Int. Conf. Comput. Vis. (ICCV), Oct. 2017, pp. 1329–1337.   
[166] K. Lee, K. Lee, J. Shin, and H. Lee, ‘‘Overcoming catastrophic forgetting with unlabeled data in the wild,’’ in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2019, pp. 312–321.   
[167] M. K. Titsias, J. Schwarz, A. G. de G. Matthews, R. Pascanu, and Y. W. Teh, ‘‘Functional regularisation for continual learning with Gaussian processes,’’ 2019, arXiv:1901.11356.   
[168] P. Pan, S. Swaroop, A. Immer, R. Eschenhagen, R. E. Turner, and M. E. Khan, ‘‘Continual deep learning by functional regularisation of memorable past,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 33, Jan. 2020, pp. 4453–4464.   
[169] T. G. J. Rudner, F. B. Smith, Q. Feng, Y. W. Teh, and Y. Gal, ‘‘Continual learning via sequential function-space variational inference,’’ in Proc. Int. Conf. Mach. Learn., Jan. 2023, pp. 18871–18887.   
[170] C. Wu, L. Herranz, X. Liu, Y. Wang, J. Van De Weijer, and B. Raducanu, ‘‘Memory replay GANs: Learning to generate new categories without forgetting,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 31, Jan. 2018, pp. 5962–5972.   
[171] Z. Wang, L. Liu, Y. Duan, and D. Tao, ‘‘Continual learning through retrieval and imagination,’’ in Proc. AAAI Conf. Artif. Intell., 2022, vol. 36, no. 8, pp. 8594–8602.   
[172] M. Zhai, L. Chen, F. Tung, J. He, M. Nawhal, and G. Mori, ‘‘Lifelong GAN: Continual learning for conditional image generation,’’ in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2019, pp. 2759–2768.   
[173] A. Chaudhry, M. Rohrbach, M. Elhoseiny, T. Ajanthan, P. K. Dokania, P. H. S. Torr, and M. Ranzato, ‘‘On tiny episodic memories in continual learning,’’ 2019, arXiv:1902.10486.   
[174] Z. Borsos, M. Mutný, and A. Krause, ‘‘Coresets via bilevel optimization for continual learning and streaming,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 33, Jan. 2020, pp. 14879–14890.   
[175] J. Yoon, D. Madaan, E. Yang, and S. J. Hwang, ‘‘Online coreset selection for rehearsal-based continual learning,’’ 2021, arXiv:2106.01085.   
[176] D. Shim, Z. Mai, J. Jeong, S. Sanner, H. Kim, and J. Jang, ‘‘Online classincremental continual learning with adversarial Shapley value,’’ in Proc. AAAI Conf. Artif. Intell., May 2021, vol. 35, no. 11, pp. 9630–9638.

[177] J. Bang, H. Kim, Y. Yoo, J.-W. Ha, and J. Choi, ‘‘Rainbow memory: Continual learning with a memory of diverse samples,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., Jun. 2021, pp. 8214–8223.   
[178] R. Tiwari, K. Killamsetty, R. Iyer, and P. Shenoy, ‘‘GCR: Gradient coreset based replay buffer selection for continual learning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2022, pp. 99–108.   
[179] L. Caccia, E. Belilovsky, M. Caccia, and J. Pineau, ‘‘Online learned continual compression with adaptive quantization modules,’’ in Proc. Int. Conf. Mach. Learn., vol. 1, Jul. 2020, pp. 1240–1250.   
[180] A. Van Den Oord and O. Vinyals, ‘‘Neural discrete representation learning,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 30, 2017, pp. 6309–6318.   
[181] L. Kumari, S. Wang, T. Zhou, and J. A. Bilmes, ‘‘Retrospective adversarial replay for continual learning,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 35, 2022, pp. 28530–28544.   
[182] W. Xie, J. Li, J. Li, and X. Wang, ‘‘An isvm algorithm based on high-dimensional distance and forgetting characteristics,’’ Sci. Program., vol. 2022, no. 1, May 2022, Art. no. 4872230.   
[183] F. M. Castro, M. J. Marín-Jiménez, N. Guil, C. Schmid, and K. Alahari, ‘‘End-to-end incremental learning,’’ in Proc. Eur. Conf. Comput. Vis. (ECCV), Oct. 2018, pp. 233–248.   
[184] Y. Wu, Y. Chen, L. Wang, Y. Ye, Z. Liu, Y. Guo, and Y. Fu, ‘‘Large scale incremental learning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2019, pp. 374–382.   
[185] H. Ahn, J. Kwak, S. Lim, H. Bang, H. Kim, and T. Moon, ‘‘SS-IL: Separated softmax for incremental learning,’’ in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2021, pp. 824–833.   
[186] A. Douillard, M. Cord, C. Ollion, T. Robert, and E. Valle, ‘‘PODNet: Pooled outputs distillation for small-tasks incremental learning,’’ in Proc. 16th Eur. Conf. Comput. Vis. (ECCV), Glasgow, U.K. Cham, Switzerland: Springer, Jan. 2020, pp. 86–102.   
[187] K. J. Joseph, S. Khan, F. S. Khan, R. M. Anwer, and V. N. Balasubramanian, ‘‘Energy-based latent aligner for incremental learning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2022, pp. 7442–7451.   
[188] X. Hu, K. Tang, C. Miao, X.-S. Hua, and H. Zhang, ‘‘Distilling causal effect of data in class-incremental learning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2021, pp. 3956–3965.   
[189] A. Ashok, K. J. Joseph, and V. N. Balasubramanian, ‘‘Class-incremental learning with cross-space clustering and controlled transfer,’’ in Proc. Eur. Conf. Comput. Vis. Cham, Switzerland: Springer, Jan. 2022, pp. 105–122.   
[190] M. De Lange and T. Tuytelaars, ‘‘Continual prototype evolution: Learning online from non-stationary data streams,’’ in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2021, pp. 8230–8239.   
[191] Z. Mai, R. Li, H. Kim, and S. Sanner, ‘‘Supervised contrastive replay: Revisiting the nearest class mean classifier in online class-incremental continual learning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. Workshops (CVPRW), Jun. 2021, pp. 3584–3594.   
[192] F.-Y. Wang, D.-W. Zhou, H.-J. Ye, and D. Zhan, ‘‘FOSTER: Feature boosting and compression for class-incremental learning,’’ in Proc. Eur. Conf. Comput. Vis. Cham, Switzerland: Springer, Jan. 2022, pp. 398–414.   
[193] L. Bonicelli, M. Boschini, A. Porrello, C. Spampinato, and S. Calderara, ‘‘On the effectiveness of lipschitz-driven rehearsal in continual learning,’ in Proc. Adv. Neural Inf. Process. Syst., vol. 35, 2022, pp. 31886–31901.   
[194] L. Yu, T. Hu, L. Hong, Z. Liu, A. Weller, and W. Liu, ‘‘Continual learning by modeling intra-class variation,’’ 2022, arXiv:2210.05398.   
[195] P. Buzzega, M. Boschini, A. Porrello, D. Abati, and S. Calderara, ‘‘Dark experience for general continual learning: A strong, simple baseline,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 33, Jan. 2020, pp. 15920–15930.   
[196] A. Prabhu, P. H. S. Torr, and P. K. Dokania, ‘‘GDumb: A simple approach that questions our progress in continual learning,’’ in Proc. 16th Eur. Conf. Comput. Vis. (ECCV), Glasgow, U.K. Cham, Switzerland: Springer, Jan. 2020, pp. 524–540.   
[197] M. Boschini, L. Bonicelli, P. Buzzega, A. Porrello, and S. Calderara, ‘‘Class-incremental continual learning into the eXtended DER-verse,’’ IEEE Trans. Pattern Anal. Mach. Intell., vol. 45, no. 5, pp. 5497–5512, May 2023.   
[198] A. Creswell, T. White, V. Dumoulin, K. Arulkumaran, B. Sengupta, and A. A. Bharath, ‘‘Generative adversarial networks: An overview,’’ IEEE Signal Process. Mag., vol. 35, no. 1, pp. 53–65, Jan. 2018.   
[199] D. P. Kingma and M. Welling, ‘‘Auto-encoding variational Bayes,’’ 2013, arXiv:1312.6114.

[200] H. Shin, J. K. Lee, J. Kim, and J. Kim, ‘‘Continual learning with deep generative replay,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 30, 2017, pp. 2990–2999.   
[201] Y. Xiang, Y. Fu, P. Ji, and H. Huang, ‘‘Incremental learning using conditional adversarial networks,’’ in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2019, pp. 6618–6627.   
[202] M. Riemer, T. Klinger, D. Bouneffouf, and M. Franceschini, ‘‘Scalable recollections for continual lifelong learning,’’ in Proc. AAAI Conf. Artif. Intell., Jul. 2019, vol. 33, no. 1, pp. 1352–1359.   
[203] A. Ayub and A. R. Wagner, ‘‘EEC: Learning to encode and regenerate images for continual learning,’’ 2021, arXiv:2101.04904.   
[204] A. İcscen, J. Zhang, S. Lazebnik, and C. Schmid, ‘‘Memory-efficient incremental learning through feature adaptation,’’ in Proc. 16th Eur. Conf. Comput. Vis. (ECCV), Glasgow, U.K. Cham, Switzerland: Springer, Jan. 2020, pp. 699–715.   
[205] K. Zhu, W. Zhai, Y. Cao, J. Luo, and Z.-J. Zha, ‘‘Self-sustaining representation expansion for non-exemplar class-incremental learning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2022, pp. 9286–9295.   
[206] E. Belouadah and A. Popescu, ‘‘IL2M: Class incremental learning with dual memory,’’ in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2019, pp. 583–592.   
[207] M. Toldo and M. Ozay, ‘‘Bring evanescent representations to life in lifelong class incremental learning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2022, pp. 16711–16720.   
[208] K. Wang, J. van de Weijer, and L. Herranz, ‘‘ACAE-REMIND for online continual learning with compressed feature replay,’’ Pattern Recognit. Lett., vol. 150, pp. 122–129, Oct. 2021.   
[209] G. Petit, A. Popescu, H. Schindler, D. Picard, and B. Delezoide, ‘‘FeTrIL: Feature translation for exemplar-free class-incremental learning,’’ in Proc. IEEE/CVF Winter Conf. Appl. Comput. Vis. (WACV), Jan. 2023, pp. 3911–3920.   
[210] G. Zeng, Y. Chen, B. Cui, and S. Yu, ‘‘Continual learning of contextdependent processing in neural networks,’’ Nature Mach. Intell., vol. 1, no. 8, pp. 364–372, Aug. 2019.   
[211] M. Farajtabar, N. Azizan, A. Mott, and A. Li, ‘‘Orthogonal gradient descent for continual learning,’’ in Proc. Int. Conf. Artif. Intell. Statist., Dec. 2020, pp. 3762–3773.   
[212] A. Chaudhry, N. Khan, P. K. Dokania, and P. H. S. Torr, ‘‘Continual learning in low-rank orthogonal subspaces,’’ in Proc. Adv. Neural Inf. Process. Syst., Jan. 2020, pp. 9900–9911.   
[213] G. Saha, I. Garg, and K. Roy, ‘‘Gradient projection memory for continual learning,’’ 2021, arXiv:2103.09762.   
[214] D. Deng, G. Chen, J. Hao, Q. Wang, and P.-A. Heng, ‘‘Flattening sharpness for dynamic gradient projection memory benefits continual learning,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 34, Jan. 2021, pp. 18710–18721.   
[215] S. Lin, L. Yang, D. Fan, and J. Zhang, ‘‘TRGP: Trust region gradient projection for continual learning,’’ 2022, arXiv:2202.02931.   
[216] S. Wang, X. Li, J. Sun, and Z. Xu, ‘‘Training networks in null space of feature covariance for continual learning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2021, pp. 184–193.   
[217] Y. Kong, L. Liu, Z. Wang, and D. Tao, ‘‘Balancing stability and plasticity through advanced null space in continual learning,’’ in Proc. Eur. Conf. Comput. Vis. Cham, Switzerland: Springer, Jan. 2022, pp. 219–236.   
[218] T.-C. Kao, K. T. Jensen, G. van de Ven, A. Bernacchia, and G. Hennequin, ‘‘Natural continual learning: Success is a journey, not (just) a destination,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 34, Jan. 2021, pp. 28067–28079.   
[219] H. Liu and H. Liu, ‘‘Continual learning with recursive gradient optimization,’’ 2022, arXiv:2201.12522.   
[220] A. Chaudhry, M. Ranzato, M. Rohrbach, and M. Elhoseiny, ‘‘Efficient lifelong learning with A-GEM,’’ 2018, arXiv:1812.00420.   
[221] S. Tang, D. Chen, J. Zhu, S. Yu, and W. Ouyang, ‘‘Layerwise optimization by gradient decomposition for continual learning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2021, pp. 9629–9638.   
[222] S. I. Mirzadeh, M. Farajtabar, R. Pascanu, and H. Ghasemzadeh, ‘‘Understanding the role of training regimes in continual learning,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 33, Jan. 2020, pp. 7308–7320.   
[223] S. I. Mirzadeh, M. Farajtabar, D. Gorur, R. Pascanu, and H. Ghasemzadeh, ‘‘Linear mode connectivity in multitask and continual learning,’’ 2020, arXiv:2010.04495.

[224] G. Lin, H. Chu, and H. Lai, ‘‘Towards better plasticity-stability trade-off in incremental learning: A simple linear connector,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2022, pp. 89–98.   
[225] S. Beaulieu, L. Frati, T. Miconi, J. Lehman, K. O. Stanley, J. Clune, and N. Cheney, ‘‘Learning to continually learn,’’ in Proc. ECAI, Jan. 2020, pp. 992–1001.   
[226] E. Lee, C.-H. Huang, and C.-Y. Lee, ‘‘Few-shot and continual learning with attentive independent mechanisms,’’ in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2021, pp. 9435–9444.   
[227] J. Rajasegaran, S. Khan, M. Hayat, F. S. Khan, and M. Shah, ‘‘ITAML: An incremental task-agnostic meta-learning approach,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2020, pp. 13585–13594.   
[228] G. Gupta, K. Yadav, and L. Paull, ‘‘Look-ahead meta learning for continual learning,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 33, Dec. 2020, pp. 11588–11598.   
[229] M. Caccia, P. Rodríguez, O. Ostapenko, F. Normandin, M. Lin, L. Page-Caccia, I. Laradji, I. Rish, A. Lacoste, D. Vázquez, and L. Charlin, ‘‘Online fast adaptation and knowledge accumulation (OSAKA): A new approach to continual learning,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 33, Jan. 2020, pp. 16532–16545.   
[230] K. J. Joseph and V. N. Balasubramanian, ‘‘Meta-consolidation for continual learning,’’ in Proc. Adv. Neural Inf. Process. Syst., Jan. 2020, pp. 14374–14386.   
[231] C. Henning, M. R. Cervera, F. D’Angelo, J. V. Oswald, R. Traber, B. Ehret, S. Kobayashi, B. F. Grewe, and J. Sacramento, ‘‘Posterior metareplay for continual learning,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 34, Jan. 2021, pp. 14135–14149.   
[232] J. Hurtado, A. Raymond-Sáez, and Á. Soto, ‘‘Optimizing reusable knowledge for continual learning via metalearning,’’ in Proc. Adv. Neural Inf. Process. Syst., Jan. 2021, pp. 14150–14162.   
[233] R. Wang, Y. Bao, B. Zhang, J. Liu, W. Zhu, and G. Guo, ‘‘Anti-retroactive interference for lifelong learning,’’ in Proc. Eur. Conf. Comput. Vis. Cham, Switzerland: Springer, Jan. 2022, pp. 163–178.   
[234] A. Mallya, D. Davis, and S. Lazebnik, ‘‘Piggyback: Adapting a single network to multiple tasks by learning to mask weights,’’ in Proc. Eur. Conf. Comput. Vis. (ECCV), Jun. 2018, pp. 67–82.   
[235] H. Kang, R. J. L. Mina, S. R. H. Madjid, J. Yoon, M. Hasegawa-Johnson, S. J. Hwang, and C. D. Yoo, ‘‘Forget-free continual learning with winning subnetworks,’’ in Proc. Int. Conf. Mach. Learn., 2022, pp. 10734–10750.   
[236] H. Jin and E. Kim, ‘‘Helpful or harmful: Inter-task association in continual learning,’’ in Proc. Eur. Conf. Comput. Vis. Cham, Switzerland: Springer, Jan. 2022, pp. 519–535.   
[237] A. Mallya and S. Lazebnik, ‘‘PackNet: Adding multiple tasks to a single network by iterative pruning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., Jun. 2018, pp. 7765–7773.   
[238] J. Yoon, E. Yang, J. Lee, and S. J. Hwang, ‘‘Lifelong learning with dynamically expandable networks,’’ 2017, arXiv:1708.01547.   
[239] S. C. Y. Hung, C.-H. Tu, C. Wu, C. Chen, Y.-M. Chan, and C.- S. Chen, ‘‘Compacting, picking and growing for unforgetting continual learning,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 32, Jan. 2019, pp. 13677–13687.   
[240] R. Aljundi, P. Chakravarty, and T. Tuytelaars, ‘‘Expert gate: Lifelong learning with a network of experts,’’ in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Jul. 2017, pp. 3366–3375.   
[241] J. Rajasegaran, M. Hayat, S. Khan, F. S. Khan, and L. Shao, ‘‘Random path selection for continual learning,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 32, Jan. 2019, pp. 12648–12658.   
[242] T. Veniat, L. Denoyer, and M. Ranzato, ‘‘Efficient continual learning with modular networks and task-driven priors,’’ 2020, arXiv:2012.12631.   
[243] O. Ostapenko, P. Rodríguez, M. Caccia, and L. Charlin, ‘‘Continual learning via local module composition,’’ in Proc. Adv. Neural Inf. Process. Syst., Jan. 2021, pp. 30298–30312.   
[244] R. Ramesh and P. Chaudhari, ‘‘Model zoo: A growing ‘Brain’ that learns continually,’’ 2021, arXiv:2106.03027.   
[245] L. Wang, X. Zhang, Q. Li, J. Zhu, and Y. Zhong, ‘‘CoSCL: Cooperation of small continual learners is stronger than a big one,’’ in Proc. Eur. Conf. Comput. Vis. Cham, Switzerland: Springer, Jan. 2022, pp. 254–271.   
[246] L. Wang, X. Zhang, Q. Li, M. Zhang, H. Su, J. Zhu, and Y. Zhong, ‘‘Incorporating neuro-inspired adaptability for continual learning in artificial intelligence,’’ Nature Mach. Intell., vol. 5, no. 12, pp. 1356–1368, Nov. 2023.

[247] Z. Wu, C. Baek, C. You, and Y. Ma, ‘‘Incremental learning via rate reduction,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2021, pp. 1125–1133.   
[248] A. Douillard, A. Ramé, G. Couairon, and M. Cord, ‘‘DyTox: Transformers for continual learning with dynamic token expansion,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2022, pp. 9275–9285.   
[249] P. Singh, V. K. Verma, P. Mazumder, L. Carin, and P. Rai, ‘‘Calibrating CNNs for lifelong learning,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 33, Jan. 2020, pp. 15579–15590.   
[250] J. Yoon, S. Kim, E. Yang, and S. Ju Hwang, ‘‘Scalable and orderrobust continual learning with additive parameter decomposition,’’ 2019, arXiv:1902.09432.   
[251] M. Kanakis, D. Brüggemann, S. Saha, S. Georgoulis, A. Obukhov, and L. Van Gool, ‘‘Reparameterizing convolutions for incremental multi-task learning without task interference,’’ in Proc. 16th Eur. Conf. Comput. Vis. (ECCV), Glasgow, U.K. Cham, Switzerland: Springer, Jul. 2020, pp. 689–707.   
[252] Z. Miao, Z. Wang, W. Chen, and Q. Qiu, ‘‘Continual learning with filter atom swapping,’’ in Proc. Int. Conf. Learn. Represent., Aug. 2021.   
[253] N. Mehta, K. J. Liang, V. K. Verma, and L. Carin, ‘‘Continual learning using a Bayesian nonparametric dictionary of weight factors,’’ in Proc. Int. Conf. Artif. Intell. Statist., Jan. 2020, pp. 100–108.   
[254] R. Hyder, K. Shao, B.-Y. Hou, P. P. Markopoulos, A. Prater-Bennette, and M. S. Asif, ‘‘Incremental task learning with incremental rank updates,’’ in Proc. Eur. Conf. Comput. Vis. Cham, Switzerland: Springer, Jan. 2022, pp. 566–582.   
[255] Z. Li, L. Zhao, Z. Zhang, H. Zhang, D. Liu, T. Liu, and D. N. Metaxas, ‘‘Steering prototypes with prompt-tuning for rehearsal-free continual learning,’’ in Proc. IEEE/CVF Winter Conf. Appl. Comput. Vis. (WACV), Jan. 2024, pp. 2511–2521.   
[256] H. Kasaei and S. Xiong, ‘‘Lifelong ensemble learning based on multiple representations for few-shot object recognition,’’ Robot. Auto. Syst., vol. 174, Apr. 2024, Art. no. 104615.   
[257] D. Rao, F. Visin, A. Rusu, R. Pascanu, Y. W. Teh, and R. Hadsell, ‘‘Continual unsupervised representation learning,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 32, 2019, pp. 1–11.   
[258] D. Benavides-Prado and P. Riddle, ‘‘A theory for knowledge transfer in continual learning,’’ in Proc. Conf. Lifelong Learn. Agents, Jan. 2022, pp. 647–660.   
[259] M. Wołczyk, K. J. Piczak, B. Wójcik, Ł. Pustelnik, P. Morawiecki, J. Tabor, T. P. Trzcinski, and P. Spurek, ‘‘Continual learning with guarantees via weight interval constraints,’’ in Proc. Int. Conf. Mach. Learn., Jan. 2022, pp. 23897–23911.   
[260] J. S. Smith, J. Tian, S. Halbe, Y.-C. Hsu, and Z. Kira, ‘‘A closer look at rehearsal-free continual learning,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. Workshops (CVPRW), Jun. 2023, pp. 2410–2420.   
[261] G. Saha and K. Roy, ‘‘Continual learning with scaled gradient projection,’’ in Proc. AAAI Conf. Artif. Intell., Jun. 2023, vol. 37, no. 8, pp. 9677–9685.   
[262] X. Li, S. Wang, J. Sun, and Z. Xu, ‘‘Memory efficient data-free distillation for continual learning,’’ Pattern Recognit., vol. 144, Dec. 2023, Art. no. 109875.   
[263] A. Chaudhry, M. Rohrbach, M. Elhoseiny, T. Ajanthan, P. Dokania, P. Torr, and M. Ranzato, ‘‘Continual learning with tiny episodic memories,’’ in Proc. Workshop Multi-Task Lifelong Reinforcement Learn., Jan. 2019.   
[264] R. V. W. Putra and M. Shafique, ‘‘FSpiNN: An optimization framework for memory-efficient and energy-efficient spiking neural networks,’’ IEEE Trans. Comput.-Aided Design Integr. Circuits Syst., vol. 39, no. 11, pp. 3601–3613, Nov. 2020.   
[265] R. V. W. Putra and M. Shafique, A Design Methodology for Energy-Efficient Embedded Spiking Neural Networks. Cham, Switzerland: Springer, 2024, pp. 15–35, doi: 10.1007/978-3-031-39932-9_2.   
[266] P. U. Diehl and M. Cook, ‘‘Unsupervised learning of digit recognition using spike-timing-dependent plasticity,’’ Frontiers Comput. Neurosci., vol. 9, p. 99, Aug. 2015. [Online]. Available: https://www.frontiersin.org/article/10.3389/fncom.2015.00099   
[267] S. A. E. Sayed, ‘‘Fault tolerance in hardware spiking neural networks,’’ Ph.D. thesis, Dept. Micro Nanotechnologies/Microelectron., Sorbonne Université, Paris, France, 2021. [Online]. Available: https://theses.hal.science/tel-03681910

[268] S. Park, S. Kim, H. Choe, and S. Yoon, ‘‘Fast and efficient information transmission with burst spikes in deep spiking neural networks,’’ in Proc. 56th ACM/IEEE Design Autom. Conf. (DAC), Jun. 2019, pp. 1–6.   
[269] S. Park, S. Kim, B. Na, and S. Yoon, ‘‘T2FSNN: Deep spiking neural networks with time-to-first-spike coding,’’ in Proc. 57th ACM/IEEE Design Autom. Conf. (DAC), Jul. 2020, pp. 1–6.   
[270] W. Guo, M. E. Fouda, A. M. Eltawil, and K. N. Salama, ‘‘Neural coding in spiking neural networks: A comparative study for robust neuromorphic systems,’’ Frontiers Neurosci., vol. 15, Mar. 2021, Art. no. 638474.   
[271] S. Thorpe and J. Gautrais, ‘‘Rank order coding,’’ in Computational Neuroscience: Trends in Research. New York, NY, USA: Plenum Press, 1998, pp. 113–118.   
[272] A. L. Hodgkin and A. F. Huxley, ‘‘A quantitative description of membrane current and its application to conduction and excitation in nerve,’’ J. Physiol., vol. 117, no. 4, p. 500, 1952.   
[273] P. Falez, ‘‘Improving spiking neural networks trained with spike timing dependent plasticity for image recognition,’’ Doctoral thesis, Dept. Comput. Sci., Université de Lille, Lille, France, 2019. [Online]. Available: https://hal.science/tel-02429539   
[274] E. M. Izhikevich, ‘‘Which model to use for cortical spiking neurons?’’ IEEE Trans. Neural Netw., vol. 15, no. 5, pp. 1063–1070, Sep. 2004.   
[275] R. Brette and W. Gerstner, ‘‘Adaptive exponential integrate-and-fire model as an effective description of neuronal activity,’’ J. Neurophysiology, vol. 94, no. 5, pp. 3637–3642, Nov. 2005.   
[276] W. Gerstner, W. M. Kistler, R. Naud, and L. Paninski, Neuronal Dynamics: From Single Neurons To Networks and Models of Cognition. U.K.: Cambridge Univ. Press, 2014.   
[277] K. Yamazaki, V.-K. Vo-Ho, D. Bulsara, and N. Le, ‘‘Spiking neural networks and their applications: A review,’’ Brain Sci., vol. 12, no. 7, p. 863, Jun. 2022.   
[278] S. Koppula, L. Orosa, A. G. Yaglikçi, R. Azizi, T. Shahroodi, K. Kanellopoulos, O. Mutlu, ‘‘Eden: Enabling energy-efficient, highperformance deep neural network inference using approximate dram,’’ in Proc. 52nd Annu. IEEE/ACM Int. Symp. Microarchitecture (MICRO), Aug. 2019, pp. 166–181.   
[279] R. V. W. Putra, M. A. Hanif, and M. Shafique, ‘‘ReSpawn: Energyefficient fault-tolerance for spiking neural networks considering unreliable memories,’’ in Proc. IEEE/ACM Int. Conf. Comput. Aided Design (ICCAD), Nov. 2021, pp. 1–9.   
[280] R. V. W. Putra, M. A. Hanif, and M. Shafique, ‘‘SparkXD: A framework for resilient and energy-efficient spiking neural network inference using approximate DRAM,’’ in Proc. 58th ACM/IEEE Design Autom. Conf. (DAC), Dec. 2021, pp. 379–384.   
[281] R. V. W. Putra, M. A. Hanif, and M. Shafique, ‘‘EnforceSNN: Enabling resilient and energy-efficient spiking neural network inference considering approximate DRAMs for embedded systems,’’ Frontiers Neurosci., vol. 16, Aug. 2022, Art. no. 937782.   
[282] J. Zhang, B. Dong, H. Zhang, J. Ding, F. Heide, B. Yin, and X. Yang, ‘‘Spiking transformers for event-based single object tracking,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2022, pp. 8791–8800.   
[283] Z. Zhou, Y. Zhu, C. He, Y. Wang, S. Yan, Y. Tian, and L. Yuan, ‘‘Spikformer: When spiking neural network meets transformer,’’ 2022, arXiv:2209.15425.   
[284] M. Yao, J. Hu, Z. Zhou, Y. Li, Y. Tian, B. Xu, and G. Li, ‘‘Spike-driven transformer,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 36, Jan. 2023, pp. 64043–64058.   
[285] M. Yao, J. Hu, T. Hu, Y. Xu, Z. Zhou, Y. Tian, B. Xu, and G. Li, ‘‘Spike-driven transformer v2: Meta spiking neural network architecture inspiring the design of next-generation neuromorphic chips,’’ 2024, arXiv:2404.03663.   
[286] R. V. W. Putra, S. Iftikhar, and M. Shafique, ‘‘QSViT: A methodology for quantizing spiking vision transformers,’’ 2025, arXiv:2504.00948.   
[287] B. Ruf and M. Schmitt, ‘‘Hebbian learning in networks of spiking neurons using temporal coding,’’ in Proc. Int. Work-Conf. Artif. Natural Neural Netw. (IWANN), Jan. 1997, pp. 380–389.   
[288] G.-Q. Bi and M.-M. Poo, ‘‘Synaptic modifications in cultured hippocampal neurons: Dependence on spike timing, synaptic strength, and postsynaptic cell type,’’ J. Neurosci., vol. 18, no. 24, pp. 10464–10472, Dec. 1998.   
[289] S. Fusi, M. Annunziato, D. Badoni, A. Salamon, and D. J. Amit, ‘‘Spike-driven synaptic plasticity: Theory, simulation, VLSI implementation,’’ Neural Comput., vol. 12, no. 10, pp. 2227–2258, Oct. 2000.

[290] J. M. Brader, W. Senn, and S. Fusi, ‘‘Learning real-world stimuli in a neural network with spike-driven synaptic dynamics,’’ Neural Comput., vol. 19, no. 11, pp. 2881–2912, Nov. 2007.   
[291] M. Mozafari, M. Ganjtabesh, A. Nowzari-Dalini, S. J. Thorpe, and T. Masquelier, ‘‘Bio-inspired digit recognition using reward-modulated spike-timing-dependent plasticity in deep convolutional networks,’’ Pattern Recognit., vol. 94, pp. 87–95, Oct. 2019.   
[292] D. I. Antonov, K. V. Sviatov, and S. Sukhov, ‘‘Continuous learning of spiking networks trained with local rules,’’ Neural Netw., vol. 155, pp. 512–522, Nov. 2022.   
[293] B. Rueckauer, I.-A. Lungu, Y. Hu, M. Pfeiffer, and S.-C. Liu, ‘‘Conversion of continuous-valued deep networks to efficient eventdriven networks for image classification,’’ Frontiers Neurosci., vol. 11, Dec. 2017, Art. no. 682.   
[294] E. O. Neftci, H. Mostafa, and F. Zenke, ‘‘Surrogate gradient learning in spiking neural networks: Bringing the power of gradient-based optimization to spiking neural networks,’’ IEEE Signal Process. Mag., vol. 36, no. 6, pp. 51–63, Nov. 2019.   
[295] R. V. W. Putra and M. Shafique, ‘‘SpiKernel: A kernel size exploration methodology for improving accuracy of the embedded spiking neural network systems,’’ IEEE Embedded Syst. Lett., vol. 17, no. 3, pp. 151–155, Jun. 2025.   
[296] R. V. W. Putra and M. Shafique, ‘‘SpikeNAS: A fast memory-aware neural architecture search framework for spiking neural network-based embedded AI systems,’’ 2024, arXiv:2402.11322.   
[297] A. Dequino, A. Carpegna, D. Nadalini, A. Savino, L. Benini, S. Di Carlo, and F. Conti, ‘‘Compressed latent replays for lightweight continual learning on spiking neural networks,’’ 2024, arXiv:2407.03111.   
[298] S. B. Shrestha and G. Orchard, ‘‘SLAYER: Spike layer error reassignment in time,’’ in Proc. Adv. Neural Inf. Process. Syst. (NeurIPS), vol. 31, S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi, and R. Garnett, Eds., 2018, pp. 1419–1428.   
[299] Y. Wu, L. Deng, G. Li, J. Zhu, and L. Shi, ‘‘Spatio-temporal backpropagation for training high-performance spiking neural networks,’’ Frontiers Neurosci., vol. 12, May 2018, Art. no. 331   
[300] J. Kaiser, H. Mostafa, and E. Neftci, ‘‘Synaptic plasticity dynamics for deep continuous local learning (DECOLLE),’’ Frontiers Neurosci., vol. 14, May 2020, Art. no. 424.   
[301] A. Ororbia, ‘‘Spiking neural predictive coding for continually learning from data streams,’’ Neurocomputing, vol. 544, Aug. 2023, Art. no. 126292.   
[302] N. Skatchkovsky, H. Jang, and O. Simeone, ‘‘Bayesian continual learning via spiking neural networks,’’ Frontiers Comput. Neurosci., vol. 16, Nov. 2022, Art. no. 1037976.   
[303] W. Fang, Y. Chen, J. Ding, Z. Yu, T. Masquelier, D. Chen, L. Huang, H. Zhou, G. Li, and Y. Tian, ‘‘SpikingJelly: An open-source machine learning infrastructure platform for spike-based intelligence,’’ Sci. Adv., vol. 9, no. 40, p. 1480, Oct. 2023.   
[304] H. Hazan, D. J. Saunders, H. Khan, D. Patel, D. T. Sanghavi, H. T. Siegelmann, and R. Kozma, ‘‘BindsNET: A machine learningoriented spiking neural networks library in Python,’’ Frontiers Neuroinform., vol. 12, p. 89, Dec. 2018.   
[305] J. K. Eshraghian, M. Ward, E. O. Neftci, X. Wang, G. Lenz, G. Dwivedi, M. Bennamoun, D. S. Jeong, and W. D. Lu, ‘‘Training spiking neural networks using lessons from deep learning,’’ Proc. IEEE, vol. 111, no. 9, pp. 1016–1054, Sep. 2023.   
[306] X. Liu, L. Mo, and M. Tang, ‘‘TinySpiking: A lightweight and efficient Python framework for unsupervised learning spiking neural networks,’’ Eng. Res. Exp., vol. 7, no. 1, Mar. 2025, Art. no. 015217.   
[307] C.-G. Pehle and J. Egholm Pedersen, ‘‘Norse-a deep learning library for spiking neural networks,’’ Zenodo, Geneva, Switzerland, Tech. Rep., 2021, doi: 10.5281/zenodo.4422025.   
[308] F. Zenke. (2021). SPyTorch: A PyTorch-based Framework for Spiking Neural Networks. [Online]. Available: https://github.com/fzenke/spytorch   
[309] S. Sheik, G. Lenz, F. Bauer, and N. Kuepelioglu. (2024). SINABS: A Simple PyTorch Based SNN Library Specialised for Speck. [Online]. Available: https://github.com/synsense/sinabs   
[310] M. Mozafari, M. Ganjtabesh, A. Nowzari-Dalini, and T. Masquelier, ‘‘SpykeTorch: Efficient simulation of convolutional spiking neural networks with at most one spike per neuron,’’ Frontiers Neurosci., vol. 13, p. 625, Jul. 2019.   
[311] D. F. Goodman and R. Brette, ‘‘Brian: A simulator for spiking neural networks in Python,’’ Frontiers Neuroinform., vol. 2, p. 350, Jul. 2008.

[312] Intel Corp. (2021). Lava Software Framework. [Online]. Available: https://lava-nc.org/   
[313] Y. Zeng, D. Zhao, F. Zhao, G. Shen, Y. Dong, E. Lu, Q. Zhang, Y. Sun, Q. Liang, Y. Zhao, Z. Zhao, H. Fang, Y. Wang, Y. Li, X. Liu, C. Du, Q. Kong, Z. Ruan, and W. Bi, ‘‘BrainCog: A spiking neural network based, brain-inspired cognitive intelligence engine for brain-inspired AI and brain simulation,’’ Patterns, vol. 4, no. 8, Aug. 2023, Art. no. 100789.   
[314] B. Buller. (2021). Pysnn: A Python Framework for Spiking Neural Networks. [Online]. Available: https://github.com/BasBuller/PySNN   
[315] F. Stefanini, E. O. Neftci, S. Sheik, and G. Indiveri, ‘‘PyNCS: A microkernel for high-level definition and configuration of neuromorphic electronic systems,’’ Frontiers Neuroinform., vol. 8, p. 73, Aug. 2014.   
[316] M. Abadi, P. Barham, J. Chen, Z. Chen, A. Davis, J. Dean, M. Devin, S. Ghemawat, G. Irving, and M. Isard, ‘‘TensorFlow: A system for largescale machine learning,’’ in Proc. 12th USENIX Symp. Operating Syst. Design Implement. (OSDI 16), Apr. 2016, pp. 265–283.   
[317] A. Paszke et al., ‘‘PyTorch: An imperative style, high-performance deep learning library,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 32, Jan. 2019, pp. 8026–8037.   
[318] D.-W. Zhou, F.-Y. Wang, H.-J. Ye, and D.-C. Zhan, ‘‘PyCIL: A Python toolbox for class-incremental learning,’’ Sci. China Inf. Sci., vol. 66, no. 9, Sep. 2023, Art. no. 197101.   
[319] A. Carta, L. Pellegrini, A. Cossu, H. Hemati, and V. Lomonaco, ‘‘Avalanche: A PyTorch library for deep continual learning,’’ J. Mach. Learn. Res., vol. 24, no. 363, pp. 1–6, 2023. [Online]. Available: http://jmlr.org/papers/v24/23-0130.html   
[320] M. Stimberg, R. Brette, and D. F. Goodman, ‘‘Brian 2, an intuitive and efficient neural simulator,’’ eLife, vol. 8, Aug. 2019, Art. no. e47314.   
[321] R. V. W. Putra, A. Marchisio, F. Zayer, J. Dias, and M. Shafique, ‘‘Embodied neuromorphic artificial intelligence for robotics: Perspectives, challenges, and research development stack,’’ in Proc. 18th Int. Conf. Control, Autom., Robot. Vis. (ICARCV), Dec. 2024, pp. 612–619.   
[322] A. Basu, L. Deng, C. Frenkel, and X. Zhang, ‘‘Spiking neural network integrated circuits: A review of trends and future directions,’’ in Proc. IEEE Custom Integr. Circuits Conf. (CICC), Apr. 2022, pp. 1–8.   
[323] B. V. Benjamin, P. Gao, E. McQuinn, S. Choudhary, A. R. Chandrasekaran, J.-M. Bussat, R. Alvarez-Icaza, J. V. Arthur, P. A. Merolla, and K. Boahen, ‘‘Neurogrid: A mixed-analog-digital multichip system for large-scale neural simulations,’’ Proc. IEEE, vol. 102, no. 5, pp. 699–716, May 2014.   
[324] N. Qiao, H. Mostafa, F. Corradi, M. Osswald, F. Stefanini, D. Sumislawska, and G. Indiveri, ‘‘A reconfigurable on-line learning spiking neuromorphic processor comprising 256 neurons and 128K synapses,’’ Frontiers Neurosci., vol. 9, p. 141, Apr. 2015.   
[325] F. Akopyan, J. Sawada, A. Cassidy, R. Alvarez-Icaza, J. Arthur, P. Merolla, N. Imam, Y. Nakamura, P. Datta, G.-J. Nam, B. Taba, M. Beakes, B. Brezzo, J. B. Kuang, R. Manohar, W. P. Risk, B. Jackson, and D. S. Modha, ‘‘TrueNorth: Design and tool flow of a 65mw 1 million neuron programmable neurosynaptic chip,’’ IEEE Trans. Comput.-Aided Design for Integr. Circuits Syst., vol. 34, no. 10, pp. 1537–1557, Oct. 2015.   
[326] M. Davies, N. Srinivasa, T.-H. Lin, G. Chinya, Y. Cao, S. H. Choday, ‘‘Loihi: A neuromorphic manycore processor with on-chip learning,’ IEEE Micro, vol. 38, no. 1, pp. 82–99, Jan. 2018.   
[327] SynSense. Dynap-CNN: The World’s First Fully Scalable, Event-driven Neuromorphic Processor With up to 1m Configurable Spiking Neurons and Direct Interface with External DVS. Accessed: Jun. 1, 2025. [Online]. Available: https://www.synsense.ai/products/dynap-cnn/   
[328] BrainChip. Akida Neural Processor SoC. [Online]. Available: https://brainchip.com/akida-neural-processor-soc/   
[329] B. M. Posey, ‘‘What is the akida event domain neural processor?’’ BrainChip, Laguna Hills, CA, USA, Tech. Rep., 2022.   
[330] A. Moitra, A. Bhattacharjee, R. Kuang, G. Krishnan, Y. Cao, and P. Panda, ‘‘SpikeSim: An end-to-end compute-in-memory hardware evaluation tool for benchmarking spiking neural networks,’’ IEEE Trans. Comput.-Aided Design Integr. Circuits Syst., vol. 42, no. 11, pp. 3815–3828, Nov. 2023.   
[331] R. V. W. Putra and M. Shafique, ‘‘NeuroNAS: Enhancing efficiency of neuromorphic in-memory computing for intelligent mobile agents through hardware-aware spiking neural architecture search,’’ 2024, arXiv:2407.00641.   
[332] K. Asifuzzaman, N. R. Miniskar, A. R. Young, F. Liu, and J. S. Vetter, ‘‘A survey on processing-in-memory techniques: Advances and challenges,’’ Memories-Mater., Devices, Circuits Syst., vol. 4, Jul. 2023, Art. no. 100022.

[333] J. Yik et al., ‘‘The neurobench framework for benchmarking neuromorphic computing algorithms and systems,’’ Nature Commun., vol. 16, no. 1, p. 1545, Feb. 2025.   
[334] A. Amir, B. Taba, D. Berg, T. Melano, J. McKinstry, C. Di Nolfo, T. Nayak, A. Andreopoulos, G. Garreau, M. Mendoza, J. Kusnitz, M. Debole, S. Esser, T. Delbruck, M. Flickner, and D. Modha, ‘‘A low power, fully event-based gesture recognition system,’’ in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Jul. 2017, pp. 7388–7397.   
[335] H. Li, H. Liu, X. Ji, G. Li, and L. Shi, ‘‘CIFAR10-DVS: An event-stream dataset for object classification,’’ Frontiers Neurosci., vol. 11, p. 309, May 2017.   
[336] Z. Pan, Y. Chua, J. Wu, M. Zhang, H. Li, and E. Ambikairajah, ‘‘An efficient and perceptually motivated auditory neural encoding and decoding algorithm for spiking neural networks,’’ Frontiers Neurosci., vol. 13, p. 1420, Jan. 2020.   
[337] J. Göltz, L. Kriener, A. Baumbach, S. Billaudelle, O. Breitwieser, B. Cramer, D. Dold, A. F. Kungl, W. Senn, J. Schemmel, K. Meier, and M. A. Petrovici, ‘‘Fast and energy-efficient neuromorphic deep learning with first-spike times,’’ Nature Mach. Intell., vol. 3, no. 9, pp. 823–835, Sep. 2021.   
[338] G. Orchard, A. Jayawant, G. Cohen, and N. V. Thakor, ‘‘Converting static image datasets to spiking neuromorphic datasets using saccades,’’ Frontiers Neurosci., vol. 9, p. 437, Nov. 2015.   
[339] A. Sironi, M. Brambilla, N. Bourdis, X. Lagorce, and R. Benosman, ‘‘HATS: Histograms of averaged time surfaces for robust event-based object classification,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., Jun. 2018, pp. 1731–1740.   
[340] Y. Li, Y. Dong, D. Zhao, and Y. Zeng, ‘‘N-omniglot, a large-scale neuromorphic dataset for spatio-temporal sparse few-shot learning,’’ Scientific Data, vol. 9, no. 1, p. 746, Dec. 2022.   
[341] B. Cramer, Y. Stradmann, J. Schemmel, and F. Zenke, ‘‘The Heidelberg spiking data sets for the systematic evaluation of spiking neural networks,’’ IEEE Trans. Neural Netw. Learn. Syst., vol. 33, no. 7, pp. 2744–2757, Jul. 2022.   
[342] Y. Lin, W. Ding, S. Qiang, L. Deng, and G. Li, ‘‘ES-ImageNet: A million event-stream classification dataset for spiking neural networks,’’ Frontiers Neurosci., vol. 15, Nov. 2021, Art. no. 726582.   
[343] O. Russakovsky, J. Deng, H. Su, J. Krause, S. Satheesh, S. Ma, Z. Huang, A. Karpathy, A. Khosla, M. Bernstein, A. C. Berg, and L. Fei-Fei, ‘‘ImageNet large scale visual recognition challenge,’’ Int. J. Comput. Vis., vol. 115, no. 3, pp. 211–252, Dec. 2015.   
[344] M. P. Guerrero-Lebrero, F. M. Quintana, and E. Guerrero, ‘‘SpikeBALL: Neuromorphic dataset for object tracking,’’ in Proc. Int. Work-Conf. Artif. Neural Netw. Cham, Switzerland: Springer, Jan. 2023, pp. 641–652.   
[345] Q. Liu, G. Pineda-García, E. Stromatias, T. Serrano-Gotarredona, and S. B. Furber, ‘‘Benchmarking spike-based visual recognition: A dataset and evaluation,’’ Frontiers Neurosci., vol. 10, p. 496, Nov. 2016.   
[346] Y. Bi, A. Chadha, A. Abbas, E. Bourtsoulatze, and Y. Andreopoulos, ‘‘Graph-based object classification for neuromorphic vision sensing,’’ in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2019, pp. 491–501.   
[347] J. Anumula, D. Neil, T. Delbruck, and S.-C. Liu, ‘‘Feature representations for neuromorphic audio spike streams,’’ Frontiers Neurosci., vol. 12, p. 23, Feb. 2018.   
[348] S. S. Park and Y.-S. Choi, ‘‘Advancing temporal spike encoding for efficient speech recognition,’’ in Proc. IEEE Int. Conf. Consum. Electron.-Asia (ICCE-Asia), Oct. 2023, pp. 1–3.   
[349] J. S. Garofolo, L. F. Lamel, W. M. Fisher, D. S. Pallett, N. L. Dahlgren, V. Zue, and J. G. Fiscus, ‘‘Timit acoustic-phonetic continuous speech corpus,’’ Nat. Inst. Standards Technol. (NIST), Gaithersburg, MD, USA, Tech. Rep. NISTIR 4930, 1993.   
[350] W. Cheng, H. Luo, W. Yang, L. Yu, S. Chen, and W. Li, ‘‘DET: A high-resolution DVS dataset for lane extraction,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. Workshops (CVPRW), Jun. 2019, pp. 1666–1675.   
[351] A. Safa, T. Verbelen, I. Ocket, A. Bourdoux, F. Catthoor, and G. G. E. Gielen, ‘‘Fail-safe human detection for drones using a multimodal curriculum learning approach,’’ IEEE Robot. Autom. Lett., vol. 7, no. 1, pp. 303–310, Jan. 2022.   
[352] K. Friston and S. Kiebel, ‘‘Predictive coding under the free-energy principle,’’ Phil. Trans. Roy. Soc. B, Biol. Sci., vol. 364, no. 1521, pp. 1211–1221, May 2009.   
[353] B. Millidge, A. Seth, and C. L. Buckley, ‘‘Predictive coding: A theoretical and experimental review,’’ 2021, arXiv:2107.12979.

[354] L. Pes, R. Luiken, F. Corradi, and C. Frenkel, ‘‘Active dendrites enable efficient continual learning in time-to-first-spike neural networks,’’ 2024, arXiv:2404.19419.   
[355] A. Iyer, K. Grewal, A. Velu, L. O. Souza, J. Forest, and S. Ahmad, ‘‘Avoiding catastrophe: Active dendrites enable multi-task learning in dynamic environments,’’ Frontiers Neurorobotics, vol. 16, Apr. 2022, Art. no. 846219.   
[356] E. Jang, S. Gu, and B. Poole, ‘‘Categorical reparameterization with gumbel-softmax,’’ 2016, arXiv:1611.01144.   
[357] E. Kreutzer, M. A. Petrovici, and W. Senn, ‘‘Natural gradient learning for spiking neurons,’’ in Proc. Neuro-inspired Comput. Elements Workshop, Mar. 2020, pp. 1–3.   
[358] B. Han, F. Zhao, Y. Zeng, W. Pan, and G. Shen, ‘‘Enhancing efficient continual learning with dynamic structure development of spiking neural networks,’’ 2023, arXiv:2308.04749.   
[359] B. Han, F. Zhao, W. Pan, Z. Zhao, X. Li, Q. Kong, and Y. Zeng, ‘‘Adaptive reorganization of neural pathways for continual learning with spiking neural networks,’’ 2023, arXiv:2309.09550.   
[360] M. Proietti, A. Ragno, and R. Capobianco, ‘‘Memory replay for continual learning with spiking neural networks,’’ in Proc. IEEE 33rd Int. Workshop Mach. Learn. Signal Process. (MLSP), Sep. 2023, pp. 1–6.   
[361] M. F. Minhas, R. V. W. Putra, F. Awwad, O. Hasan, and M. Shafique, ‘‘Replay4NCL: An efficient memory replay-based methodology for neuromorphic continual learning in embedded AI systems,’’ 2025, arXiv:2503.17061.   
[362] N. Srivastava, G. E. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhutdinov, ‘‘Dropout: A simple way to prevent neural networks from overfitting,’’ J. Mach. Learn. Res., vol. 15, no. 1, pp. 1929–1958, Jan. 2014.   
[363] M. Xiao, Q. Meng, Z. Zhang, D. He, and Z. Lin, ‘‘Hebbian learning based orthogonal projection for continual learning of spiking neural networks,’’ 2024, arXiv:2402.11984.   
[364] Y. Lecun, L. Bottou, Y. Bengio, and P. Haffner, ‘‘Gradient-based learning applied to document recognition,’’ Proc. IEEE, vol. 86, no. 11, pp. 2278–2324, Nov. 1998.   
[365] H. Xiao, K. Rasul, and R. Vollgraf, ‘‘Fashion-MNIST: A novel image dataset for benchmarking machine learning algorithms,’’ 2017, arXiv:1708.07747.   
[366] Y. Bulatov. (2011). Notmnist Dataset. [Online]. Available: http://yaroslavvb.blogspot.com/2011/09/notmnist-dataset.html   
[367] M. Zhang, J. Wang, J. Wu, A. Belatreche, B. Amornpaisannon, Z. Zhang, V. P. K. Miriyala, H. Qu, Y. Chua, T. E. Carlson, and H. Li, ‘‘Rectified linear postsynaptic potential function for backpropagation in deep spiking neural networks,’’ IEEE Trans. Neural Netw. Learn. Syst., vol. 33, no. 5, pp. 1947–1958, May 2022.   
[368] T. Serrano-Gotarredona and B. Linares-Barranco, ‘‘Poker-DVS and MNIST-DVS. Their history, how they were made, and other details,’’ Frontiers Neurosci., vol. 9, p. 481, Dec. 2015.   
[369] A. Krizhevsky and G. Hinton, ‘‘Learning multiple layers of features from tiny images,’’ Univ. Toronto, Toronto, ON, Canada, Tech. Rep., 2009.   
[370] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei, ‘‘ImageNet: A large-scale hierarchical image database,’’ in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., Jun. 2009, pp. 248–255.   
[371] G. Cohen, S. Afshar, J. Tapson, and A. Van Schaik, ‘‘EMNIST: Extending MNIST to handwritten letters,’’ in Proc. Int. Joint Conf. Neural Netw. (IJCNN), May 2017, pp. 2921–2926.   
[372] Q. Shi, F. Liu, H. Li, G. Li, L. Shi, and R. Zhao, ‘‘Hybrid neural networks for continual learning inspired by corticohippocampal circuits,’’ Nature Commun., vol. 16, no. 1, p. 1272, Feb. 2025.   
[373] N. Rathi, G. Srinivasan, P. Panda, and K. Roy, ‘‘Enabling deep spiking neural networks with hybrid conversion and spike timing dependent backpropagation,’’ 2020, arXiv:2005.01807.   
[374] B. Rosenfeld, O. Simeone, and B. Rajendran, ‘‘Spiking generative adversarial networks with a neural network discriminator: Local training, Bayesian models, and continual meta-learning,’’ IEEE Trans. Comput., vol. 71, no. 11, pp. 2778–2791, Nov. 2022.   
[375] J. Zhang, W. Fan, and X. Liu, ‘‘Spiking generative networks empowered by multiple dynamic experts for lifelong learning,’’ Expert Syst. Appl., vol. 238, Mar. 2024, Art. no. 121845.   
[376] R. V. W. Putra and M. Shafique, ‘‘Q-SpiNN: A framework for quantizing spiking neural networks,’’ in Proc. Int. Joint Conf. Neural Netw. (IJCNN), Jul. 2021, pp. 1–8.   
[377] R. V. W. Putra, M. A. Hanif, and M. Shafique, ‘‘RescueSNN: Enabling reliable executions on spiking neural network accelerators under permanent faults,’’ Frontiers Neurosci., vol. 17, Apr. 2023, Art. no. 1159440.

[378] R. V. W. Putra, M. A. Hanif, and M. Shafique, ‘‘SoftSNN: Low-cost fault tolerance for spiking neural network accelerators under soft errors,’’ in Proc. 59th ACM/IEEE Design Autom. Conf. New York, NY, USA: ACM, Jul. 2022, pp. 151–156, doi: 10.1145/3489517.3530657.   
[379] R. V. W. Putra, A. Marchisio, and M. Shafique, ‘‘SNN4Agents: A framework for developing energy-efficient embodied spiking neural networks for autonomous agents,’’ Frontiers Robot. AI (FROBT), vol. 11, Jul. 2024, Art. no. 1401677. [Online]. Available: https:// www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt. 2024.1401677   
[380] R. Krishnamoorthi, ‘‘Quantizing deep convolutional networks for efficient inference: A whitepaper,’’ 2018, arXiv:1806.08342.   
[381] M. Hopkins, M. Mikaitis, D. R. Lester, and S. Furber, ‘‘Stochastic rounding and reduced-precision fixed-point arithmetic for solving neural ordinary differential equations,’’ Phil. Trans. Roy. Soc. A, Math., Phys. Eng. Sci., vol. 378, no. 2166, Mar. 2020, Art. no. 20190052.   
[382] D. Lee, S. Park, J. Kim, W. Doh, and S. Yoon, ‘‘Energy-efficient knowledge distillation for spiking neural networks,’’ 2021, arXiv:2106. 07172.   
[383] D. Hong, J. Shen, Y. Qi, and Y. Wang, ‘‘LaSNN: Layer-wise ANN-to-SNN distillation for effective and efficient training in deep spiking neural networks,’’ 2023, arXiv:2304.09101.   
[384] Q. Xu, Y. Li, J. Shen, J. K. Liu, H. Tang, and G. Pan, ‘‘Constructing deep spiking neural networks from artificial neural networks with knowledge distillation,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2023, pp. 7886–7895.   
[385] H. Qiu, M. Ning, Z. Song, W. Fang, Y. Chen, T. Sun, Z. Ma, L. Yuan, and Y. Tian, ‘‘Self-architectural knowledge distillation for spiking neural networks,’’ Neural Netw., vol. 178, Oct. 2024, Art. no. 106475.   
[386] S. Shaw, K. Tyagi, and S. Zhang, ‘‘Teacher-student knowledge distillation for radar perception on embedded accelerators,’’ in Proc. 57th Asilomar Conf. Signals, Syst., Comput., Oct. 2023, pp. 1035–1038.   
[387] S. B. Furber, F. Galluppi, S. Temple, and L. A. Plana, ‘‘The spinnaker project,’’ Proc. IEEE, vol. 102, no. 5, pp. 652–665, May 2014.   
[388] C. Pehle, S. Billaudelle, B. Cramer, J. Kaiser, K. Schreiber, Y. Stradmann, J. Weis, A. Leibfried, E. Müller, and J. Schemmel, ‘‘The BrainScaleS-2 accelerated neuromorphic system with hybrid plasticity,’’ Frontiers Neurosci., vol. 16, Feb. 2022, Art. no. 795876.   
[389] J. Pei et al., ‘‘Towards artificial general intelligence with hybrid Tianjic chip architecture,’’ Nature, vol. 572, no. 7767, pp. 106–111, 2019.   
[390] C. Frenkel, J.-D. Legat, and D. Bol, ‘‘MorphIC: A 65-nm 738ksynapse/mm2 quad-core binary-weight digital neuromorphic processor with stochastic spike-driven online learning,’’ IEEE Trans. Biomed. Circuits Syst., vol. 13, no. 5, pp. 999–1010, Oct. 2019.   
[391] G. Chen, J. Cao, C. Zou, S. Feng, Y. Zhong, X. Zhang, and Y. Wang, ‘‘PAIBoard: A neuromorphic computing platform for hybrid neural networks in robot dog application,’’ Electronics, vol. 13, no. 18, p. 3619, Sep. 2024.   
[392] Y. Zhong, Y. Kuang, K. Liu, Z. Wang, S. Feng, G. Chen, Y. Yang, X. Cui, Q. Wang, J. Cao, S. Jia, Y. Liang, G. Sun, X. Cui, R. Huang, and Y. Wang, ‘‘PAICORE: A 1.9-million-neuron 5.181-TSOPS/W digital neuromorphic processor with unified SNN-ANN and on-chip learning paradigm,’’ IEEE J. Solid-State Circuits, vol. 60, no. 2, pp. 651–671, Feb. 2025.   
[393] Y. Gu, X. Yang, K. Wei, and C. Deng, ‘‘Not just selection, but exploration: Online class-incremental continual learning via dual view consistency,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2022, pp. 7432–7441.   
[394] S.-F. Yu and W.-C. Chiu, ‘‘Mitigating forgetting in online continual learning via contrasting semantically distinct augmentations,’’ 2022, arXiv:2211.05347.   
[395] E. Hajizada, P. Berggold, M. Iacono, A. Glover, and Y. Sandamirskaya, ‘‘Interactive continual learning for robots: A neuromorphic approach,’’ in Proc. Int. Conf. Neuromorphic Syst., Jul. 2022, pp. 1–10.   
[396] V. Tikhanoff, A. Cangelosi, P. Fitzpatrick, G. Metta, L. Natale, and F. Nori, ‘‘An open-source simulator for cognitive robotics research: The prototype of the iCub humanoid robot simulator,’’ in Proc. 8th Workshop Perform. Metrics Intell. Syst., Aug. 2008, pp. 57–61.   
[397] Y. Zaidel, A. Shalumov, A. Volinski, L. Supic, and E. E. Tsur, ‘‘Neuromorphic NEF-based inverse kinematics and PID control,’’ Frontiers Neurorobotics, vol. 15, Feb. 2021, Art. no. 631159.   
[398] T. Bekolay, J. Bergstra, E. Hunsberger, T. DeWolf, T. C. Stewart, D. Rasmussen, X. Choo, A. R. Voelker, and C. Eliasmith, ‘‘Nengo: A Python tool for building large-scale functional brain models,’’ Frontiers Neuroinform., vol. 7, p. 48, May 2014.

[399] C.-K. Lin, A. Wild, G. N. Chinya, Y. Cao, M. Davies, D. M. Lavery, and H. Wang, ‘‘Programming spiking neural networks on Intel’s loihi,’’ Computer, vol. 51, no. 3, pp. 52–61, Mar. 2018.   
[400] D. Marrero, J. Kern, and C. Urrea, ‘‘A novel robotic controller using neural engineering framework-based spiking neural networks,’’ Sensors, vol. 24, no. 2, p. 491, Jan. 2024.   
[401] A. Viale, A. Marchisio, M. Martina, G. Masera, and M. Shafique, ‘‘CarSNN: An efficient spiking neural network for event-based autonomous cars on the loihi neuromorphic research processor,’’ in Proc. Int. Joint Conf. Neural Netw. (IJCNN), Jul. 2021, pp. 1–10.   
[402] I. Bano, R. V. W. Putra, A. Marchisio, and M. Shafique, ‘‘FastSpiker: Enabling fast training for spiking neural networks on event-based data through learning rate enhancements for autonomous embedded systems,’’ 2024, arXiv:2407.05262.   
[403] L. Cordone, B. Miramond, and P. Thierion, ‘‘Object detection with spiking neural networks on automotive event data,’’ in Proc. Int. Joint Conf. Neural Netw. (IJCNN), Jul. 2022, pp. 1–8.   
[404] I. Bano, R. V. W. Putra, A. Marchisio, and M. Shafique, ‘‘A methodology to study the impact of spiking neural network parameters considering event-based automotive data,’’ 2024, arXiv:2404.03493.   
[405] A. Viale, A. Marchisio, M. Martina, G. Masera, and M. Shafique, ‘‘LaneSNNs: Spiking neural networks for lane detection on the loihi neuromorphic processor,’’ in Proc. IEEE/RSJ Int. Conf. Intell. Robots Syst. (IROS), Oct. 2022, pp. 79–86.   
[406] A. Safa, T. Verbelen, I. Ocket, A. Bourdoux, H. Sahli, F. Catthoor, and G. Gielen, ‘‘Fusing event-based camera and radar for SLAM using spiking neural networks with continual STDP learning,’’ in Proc. IEEE Int. Conf. Robot. Autom. (ICRA), May 2023, pp. 2782–2788.   
[407] A. Safa, I. Ocket, A. Bourdoux, H. Sahli, F. Catthoor, and G. G. E. Gielen, ‘‘STDP-driven development of attention-based people detection in spiking neural networks,’’ IEEE Trans. Cognit. Develop. Syst., vol. 16, no. 1, pp. 380–387, Jan. 2022.   
[408] C. Frenkel and G. Indiveri, ‘‘ReckOn: A 28nm sub-mm2 task-agnostic spiking recurrent neural network processor enabling on-chip learning over second-long timescales,’’ in IEEE Int. Solid-State Circuits Conf. (ISSCC) Dig. Tech. Papers, vol. 65, Feb. 2022, pp. 1–3.   
[409] Unitree Robot. Unitree Aliengo. [Online]. Available: https://www.unitree.com/aliengo   
[410] A. Safa, I. Ocket, A. Bourdoux, H. Sahli, F. Catthoor, and G. Gielen, ‘‘A new look at spike-timing-dependent plasticity networks for spatiotemporal feature learning,’’ 2021, arXiv:2111.00791.   
[411] A. Devkota, R. V. W. Putra, and M. Shafique, ‘‘MTSpark: Enabling multitask learning with spiking neural networks for generalist agents,’’ 2024, arXiv:2412.04847.

![](images/9065f52f69139fc8a244cde0a1e5a42742bca2afff8d31dd3fbb3353abf677a5.jpg)

MISHAL FATIMA MINHAS received the B.Sc. degree (Hons.) in computer systems engineering from Mirpur University of Science and Technology (MUST), Pakistan, and the M.Sc. degree in electrical engineering with specialization in digital systems and signal processing (DSSP) from the School of Electrical Engineering and Computer Science (SEECS), National University of Sciences and Technology (NUST), Islamabad, Pakistan. She is currently pursuing the Ph.D. degree in

electrical engineering with the Department of Electrical and Communication Engineering, United Arab Emirates University (UAEU), Al Ain, United Arab Emirates. Her research interests include continual learning, brain-inspired AI, machine learning, energy-efficient design, neuromorphic computing, digital signal processing, digital system design, and formal verification.

![](images/8e2b0d863665a57a64f3ea8b22785ec5dbe9ef984603115df793ec3d46ae31c7.jpg)

RACHMAD VIDYA WICAKSANA PUTRA (Member, IEEE) received the B.Sc. degree in electrical engineering and the M.Sc. degree in electronics engineering from Bandung Institute of Technology (ITB), Indonesia, and the Ph.D. degree in computer science from Technische Universität Wien (TU Wien), Vienna, Austria.

In academia, he was a Teaching Assistant with the Electrical Engineering, ITB, a Research Assistant with the Microelectronics Center, ITB,

and a Project Research Assistant with the Institute of Computer Engineering, TU Wien. Meanwhile, in industry, he also experienced working as an FPGA Engineer at PT. Fusi Global Teknologi, Indonesia, and TriLite Technologies GmbH, Austria. He is currently the Research Team Leader, eBrain Laboratory, New York University (NYU) Abu Dhabi, Abu Dhabi, United Arab Emirates. His research interests include neuromorphic and cognitive computing, computer architecture, integrated circuits and VLSI, system-on-chip design, emerging device technologies, robust and energyefficient computing, embedded AI, and electronic design automation. He received multiple HiPEAC paper awards and an ACM Showcase for his first-authored articles during the Ph.D. degree, and the Best Paper Nomination in ICARCV 2024.

![](images/a63ef3a0ace730a7facaee7caeb12982fc04b7af1c101b34c07731db253bf400.jpg)

FALAH AWWAD (Senior Member, IEEE) received the M.Sc. and Ph.D. degrees in electrical and computer engineering from Concordia University, Montreal, Canada, in 2002 and 2006, respectively. He is currently a Professor with the Department of Electrical and Communication Engineering, College of Engineering, United Arab Emirates University (UAEU), Al Ain, United Arab Emirates, where he is also the Coordinator of the M.Sc. Electrical Engineering Program. He has

co-authored one book and two book chapters and has published over 120 papers in journals and international conferences. His work has appeared in IEEE journals, Biosensors and Bioelectronics, Scientific Reports, and other reputable publications. He holds two U.S. patents. He has secured over 23 research grants, serving as the principal investigator on 17 of them. His service contributions include his roles as a consultant and a committee member at various universities and research institutions in United Arab Emirates. He has played a key role in developing and enhancing curricula for undergraduate and graduate programs in electrical engineering, computer engineering, and cybersecurity. He continues to advance his field through ongoing projects in the IoT security, energy-efficient computing, and advanced semiconductor devices. His research interests include VLSI circuits and systems, including hardware security, sensors, and biomedical applications.

![](images/0235769fbac1718696df23391cb1c074b3ef8c555151d2923f013b8935aad86f.jpg)

OSMAN HASAN (Senior Member, IEEE) received the B.Eng. degree (Hons.) from the University of Engineering and Technology Peshawar, Pakistan, in 1997, and the M.Eng. and Ph.D. degrees from Concordia University, Montreal, Canada, in 2001 and 2008, respectively.

He was an ASIC Design Engineer with LSI Logic Corporation, Ottawa, Canada, from 2001 to 2003, and a Research Associate with Concordia University, for 18 months after the Ph.D. degree.

He joined the School of Electrical Engineering and Computer Science (SEECS), NUST, as an Assistant Professor, in September 2009. He was promoted to a Tenured Associate Professor and a Tenured Professor ranks in May 2015 and August 2019, respectively. He was the Head of the Department of Research, from 2015 to 2018, the Senior Head of the Department of Electrical Engineering, from 2018 to 2020, and the Principal and the Dean of SEECS, NUST, from 2020 to 2021. He is currently the Pro Rector (Academics) of NUST. He is the Founder and the Director of the System Analysis and Verification (SAVe) Laboratory, SEECS, and his research

interests include embedded system design, formal methods, and e-health. He has been able to acquire over Rs. 120 million of research grants from various national and international agencies and has published over 250 research articles, including six manuscripts, one patent, 20 book chapters, over 100 impact factor journal articles, and over 150 conference proceeding papers.

Dr. Hasan is a member of ACM, the Association for Automated Reasoning (AAR), and Pakistan Engineering Council. He received the Quaid-e-Azam Award, Ministry of Education, Pakistan (1998), the Best University Teacher Award 2010 from HEC, Pakistan, the Ideal ICT Excellence Award 2012 from Ideal Distributions, Pakistan, the Excellence in IT Education Award 2013 from Teradata Pakistan, the Best Young Research Scholar Award from HEC, Pakistan (2011), the Excellence in IT Research and Development Award 2014 from Teradata Pakistan, the President’s Gold Medal for the Best Teacher of the University (2015) from NUST, the Best University Researcher Award (2015 and 2019), and the Research Productivity Award (2016) from Pakistan Council for Science and Technology. For his continued services in higher education, he was awarded the prestigious National Award of Tamgh-e-Imtiaz by the President of Pakistan in 2022.

![](images/23751a34a00210b4b6de1fd962ba1963d7bd9b964d01738663fed01c6f6548be.jpg)

MUHAMMAD SHAFIQUE (Senior Member, IEEE) received the Ph.D. degree in computer science from Karlsruhe Institute of Technology (KIT), Karlsruhe, Germany, in 2011.

He established and led a highly recognized research group at KIT for several years and conducted impactful collaborative research and development activities across the globe. In 2016, he joined as a Full Professor of computer architecture and robust, energy-efficient technologies with

the Faculty of Informatics, Institute of Computer Engineering, Technische Universität Wien (TU Wien), Vienna, Austria. Since 2020, he has been with New York University (NYU) Abu Dhabi, Abu Dhabi, United Arab Emirates, where he is currently a Full Professor and the Director of eBrain Laboratory. He is a Global Network Professor with the Tandon School of Engineering, NYU, New York, NY, USA. He is also a Co-PI/Investigator with multiple NYUAD centers, including the Center of Artificial Intelligence and Robotics (CAIR), the Center of Cyber Security (CCS), the Center for InTeractIng urban nEtworkS (CITIES), and the Center for Quantum and Topological Systems (CQTS). He holds one U.S. patent and has (co-)authored six books, more than ten book chapters, more than 350 papers in premier journals and conferences, and more than 100 archive articles. His research interests include AI and machine learning hardware and systemlevel design, brain-inspired computing, quantum machine learning, cognitive autonomous systems, wearable healthcare, energy-efficient systems, robust computing, hardware security, emerging technologies, FPGAs, MPSoCs, and embedded systems. His research has a special focus on cross-layer analysis, modeling, design, and optimization of computing and memory systems. The researched technologies and tools are deployed in application use cases from the Internet-of-Things (IoT), smart cyber–physical systems (CPSs), and ICT for development (ICT4D) domains.

Dr. Shafique is a Senior Member of the IEEE Signal Processing Society (SPS) and a member of ACM, SIGARCH, SIGDA, SIGBED, and HIPEAC. He has given several keynotes, invited talks, and tutorials, and organized many special sessions at premier venues. He served as the PC chair, the general chair, the track chair, and a PC member for several prestigious IEEE/ACM conferences. He received the 2015 ACM/SIGDA Outstanding New Faculty Award, the AI 2000 Chip Technology Most Influential Scholar Award in 2020, 2022, and 2023, the ASPIRE AARE Research Excellence Award in 2021, six gold medals, and several best paper awards and nominations at prestigious conferences.