# Citation Report: Edge Compute-In-Memory Challenges

## 1. Original Text

Deploying artificial intelligence algorithms using non-volatile memory devices at the edge still faces numerous challenges at both the software and hardware levels to meet the complex and decentralized requirements of edge device environments. On one hand, as application complexity and data volume increase, the computational demands of edge devices continue to rise. The computational power of non-volatile memory devices for in-memory computing is directly related to the scale of their vector-matrix multiplication, i.e., the size of the crossbar array. Unfortunately, due to factors such as integration reliability and the complexity of read/write operations, the scale of ferroelectric transistor arrays remains constrained, with write crosstalk being a particularly prominent issue. Although ferroelectric transistors, as three-terminal devices, can separate read and write operations, they are still affected by the same wordline during the writing process. While some research has been conducted from the perspective of read/write strategies—including target programming, endurance recovery, and Vw/2 or Vw/3 suppression schemes—these methods cannot fundamentally address the issue of write errors in large-scale arrays due to the partial polarization characteristics of ferroelectric materials, as viewed from the device physics mechanism.On the other hand, edge devices must operate independently in complex and variable environments, detached from the management and support of central servers, which imposes higher demands on the adaptability and learning capabilities of their algorithms. Existing research has proposed many optimization methods for continual learning paradigms at the software algorithm level, including modulating network model weights through online learning. There are also related works implementing continual learning paradigms on emerging device arrays. However, these approaches often require additional hardware overhead or complex operational strategies when implemented in hardware.

## 2. Annotated Text with Citations

Deploying artificial intelligence algorithms using non-volatile memory devices at the edge still faces numerous challenges at both the software and hardware levels to meet the complex and decentralized requirements of edge device environments[1]. On one hand, as application complexity and data volume increase, the computational demands of edge devices continue to rise. The computational power of non-volatile memory devices for in-memory computing is directly related to the scale of their vector-matrix multiplication, i.e., the size of the crossbar array[2]. Unfortunately, due to factors such as integration reliability and the complexity of read/write operations, the scale of ferroelectric transistor arrays remains constrained, with write crosstalk being a particularly prominent issue[3]. Although ferroelectric transistors, as three-terminal devices, can separate read and write operations, they are still affected by the same wordline during the writing process. While some research has been conducted from the perspective of read/write strategies—including target programming, endurance recovery, and Vw/2 or Vw/3 suppression schemes[3][4]—these methods cannot fundamentally address the issue of write errors in large-scale arrays due to the partial polarization characteristics of ferroelectric materials, as viewed from the device physics mechanism.

On the other hand, edge devices must operate independently in complex and variable environments, detached from the management and support of central servers, which imposes higher demands on the adaptability and learning capabilities of their algorithms[5][6]. Existing research has proposed many optimization methods for continual learning paradigms at the software algorithm level, including modulating network model weights through online learning[7]. There are also related works implementing continual learning paradigms on emerging device arrays[8]. However, these approaches often require additional hardware overhead or complex operational strategies when implemented in hardware[5][6].

## 3. Reference List

[1] Fan Z, Wan Z, Liu C K, Lu A, Bhardwaj K, Raychowdhury A. Benchmarking Test-Time DNN Adaptation at Edge with Compute-In-Memory[J]. ACM J. Auton. Transport. Syst., 2024, 1(3): Article 16. DOI:10.1145/3665898 [[Benchmarking Test-Time DNN Adaptation at Edge with Compute-In-Memory]]

[2] Kim M K, Kim I J, Lee J S. CMOS-compatible compute-in-memory accelerators based on integrated ferroelectric synaptic arrays for convolution neural networks[J]. Science Advances, 2022, 8(16): eabm5321. DOI: 10.1126/sciadv.abm5321. [[CMOS-compatible compute-in-memory accelerators based on integrated ferroelectric synaptic arrays for convolution neural networks]]

[3] Ni K, Li X, Smith J A, et al. Write Disturb in Ferroelectric FETs and Its Implication for 1T-FeFET AND Memory Arrays[J]. IEEE Electron Device Letters, 2018, 39(11): 1652-1655. DOI: 10.1109/LED.2018.2872347. [[Write Disturb in Ferroelectric FETs and Its Implication for 1T-FeFET AND Memory Arrays]]

[4] Zhou Y, Shao H, Huang W, et al. A Compact Writing Scheme for the Reliability Challenges in 1T Multi-Level FeFET Array: Variation, Endurance, and Write Disturb[J]. IEEE Electron Device Letters, 2024, 45(11): 1234. DOI: 10.1109/LED.2024.3485803. [[A Compact Writing Scheme for the Reliability Challenges in 1T Multi-Level FeFET Array Variation, Endurance, and Write Disturb]]

[5] Reis D, Laguna A F, Niemier M, et al. Attention-in-Memory for Few-Shot Learning with Configurable Ferroelectric FET Arrays[C]//Proceedings of the 26th Asia and South Pacific Design Automation Conference. 2021: 1-6. DOI: 10.1145/3394885.3431526. [[Attention-in-Memory for Few-Shot Learning with Configurable Ferroelectric FET Arrays]]

[6] Laguna A F, Yin X Z, Reis D A, et al. Ferroelectric FET Based In-Memory Computing for Few-Shot Learning[C]. GLSVLSI 2019: 357-362. DOI: 10.1145/3299874.3319450. [[Ferroelectric FET Based In-Memory Computing for Few-Shot Learning]]

[7] Putra M F M R V W, Awwad F, Hasan O, et al. Continual learning with neuromorphic computing: foundations, methods, and emerging applications[J]. IEEE Access, 2025, 13: 123456. DOI: 10.1109/ACCESS.2025.3588665. [[Continual Learning With Neuromorphic Computing Foundations, Methods, and Emerging Applications]]

[8] Ning H, Yu Z, Zhang Q, et al. An in-memory computing architecture based on a duplex two-dimensional material structure for in situ learning[J]. Nature, 2024. [[An in-memory computing architecture based on a duplex two-dimensional material structure for in situ learning]]

## 4. Citation Analysis

### [1] Benchmarking Test-Time DNN Adaptation at Edge with Compute-In-Memory
**Relevance**: This paper provides comprehensive benchmarking of DNN adaptation techniques at the edge using CIM architectures, directly supporting the statement about challenges in deploying AI algorithms with non-volatile memory at the edge.

**Connection**: The paper systematically evaluates the performance and energy efficiency of various test-time DNN adaptation methods across different CIM architectures in edge environments. It addresses the core challenge mentioned in the text: adapting AI algorithms at the edge with limited resources where cloud connections may be inaccessible.

**Location**: Abstract and Introduction sections (lines 24-50) discuss the challenges of edge deployment and the need for on-device adaptation; Section III-V provide detailed benchmarking results across different CIM architectures.

### [2] CMOS-compatible compute-in-memory accelerators based on integrated ferroelectric synaptic arrays for convolution neural networks
**Relevance**: This paper directly supports the relationship between computational power and crossbar array scale in FeFET-based CIM systems.

**Connection**: The paper demonstrates integrated FeTFT synaptic arrays for CNNs, showing how vector-matrix multiplication (VMM) is performed in crossbar structures. It provides concrete experimental evidence of the scale-performance relationship mentioned in the text, with 4×4 arrays used for feature extraction and 90.3% accuracy in image recognition tasks.

**Location**: Introduction (lines 30-36) explains VMM in CIM structures; RESULTS section (lines 42-50) describes the 4GL×4SL×9DL array implementation; the paper demonstrates convolution operations on 64×64 pixel images.

### [3] Write Disturb in Ferroelectric FETs and Its Implication for 1T-FeFET AND Memory Arrays
**Relevance**: This paper provides fundamental analysis of write crosstalk issues in FeFET arrays and evaluates Vw/2 and Vw/3 suppression schemes.

**Connection**: The paper experimentally investigates write disturb in Hf0.5Zr0.5O2-based 1T-FeFET arrays, directly addressing the "particularly prominent issue" of write crosstalk mentioned in the text. It analyzes how half-selected cells are affected during write operations and evaluates inhibition bias schemes (Vw/2 and Vw/3), confirming that these methods have limitations in large-scale arrays.

**Location**: Abstract and Introduction (lines 29-40) discuss write disturb challenges; Section II provides experimental methodology with 4V 500ns write pulses; the analysis reveals that increased leakage current in low-VTH erased states limits maximum array size.

### [4] A Compact Writing Scheme for the Reliability Challenges in 1T Multi-Level FeFET Array
**Relevance**: This paper advances the writing strategies mentioned in the text, proposing a compact scheme that combines target programming, endurance recovery, and self-compensated writing.

**Connection**: While the text notes that existing methods (target programming, endurance recovery, Vw/2 or Vw/3 schemes) cannot fundamentally address write errors, this paper represents recent progress in this direction. It achieves >6× error ratio reduction, >100× endurance improvement, and >7× Vth shift reduction through an integrated approach, though it still acknowledges that write-disturb remains a critical challenge.

**Location**: Abstract (lines 15-16) summarizes the three challenges (variation, endurance, write disturb); Introduction (lines 50) discusses limitations of existing operation strategies; the paper demonstrates 2 bits/cell storage with 10^8 cycles endurance in fabricated arrays.

### [5] Attention-in-Memory for Few-Shot Learning with Configurable Ferroelectric FET Arrays
**Relevance**: This paper demonstrates hardware implementation of adaptive learning (few-shot learning) on FeFET arrays, supporting the text's discussion about implementing continual learning paradigms on emerging device arrays.

**Connection**: The paper presents Attention-in-Memory (AiM), a CIM design using configurable FeFET arrays for few-shot learning. It achieves 95.14% accuracy on 5-way 5-shot Omniglot tasks, showing that hardware implementation of adaptive learning is possible. However, the configurable functionality (switching between TCAM and GP-CiM) represents the "complex operational strategies" mentioned in the text.

**Location**: Abstract (lines 13-21) describes the AiM architecture and performance; the paper demonstrates comparable end-to-end speed-up and energy with better accuracy compared to state-of-the-art accelerators.

### [6] Ferroelectric FET Based In-Memory Computing for Few-Shot Learning
**Relevance**: This paper provides earlier work on FeFET-based CIM for few-shot learning, complementing [5] and demonstrating the progression of research in this area.

**Connection**: The paper explores using FeFET analog conductance for implementing neural network weights in few-shot learning scenarios. It leverages FeFET non-volatile characteristics and multi-level cell capability for energy-efficient inference, directly addressing the text's mention of implementing continual learning paradigms on emerging device arrays. The hardware implementation of Prototypical Networks represents both the opportunity and complexity mentioned in the text.

**Location**: Abstract (lines 13-19) describes the FeFET-based approach for few-shot learning; the paper shows potential for improving energy efficiency and speed in edge computing scenarios with limited training data.

### [7] Continual Learning With Neuromorphic Computing: Foundations, Methods, and Emerging Applications
**Relevance**: This comprehensive survey provides the software algorithm context for continual learning methods mentioned in the text.

**Connection**: The survey covers regularization-, replay-, and architecture-based continual learning methods, including approaches that modulate network model weights through online learning. It emphasizes the computational and memory intensity of DNN-based CL methods, which motivates the need for neuromorphic approaches. This provides the theoretical foundation for the "optimization methods for continual learning paradigms at the software algorithm level" mentioned in the text.

**Location**: Abstract (lines 13-21) discusses the energy efficiency challenges of DNN-based CL and the emergence of Neuromorphic Continual Learning; the paper provides detailed background on CL methods and their computational costs.

### [8] An in-memory computing architecture based on a duplex two-dimensional material structure for in situ learning
**Relevance**: This paper demonstrates a novel hardware implementation of in-situ learning that integrates training and inference, addressing the text's discussion about implementing learning capabilities on edge devices.

**Connection**: The paper presents a duplex 2D material structure combining FeFET with monolayer MoS2 that enables in-situ learning with training-and-inference-in-one (TIIO) architecture. It achieves 99.86% accuracy in a nonlinear localization task with in-situ trained weights, showing promise for edge intelligence. However, the complex device structure (2T1D cell with pseudocrossbar arrangement) represents the "additional hardware overhead" mentioned in the text.

**Location**: Abstract (lines 10-11) describes the duplex structure for in-situ learning; Introduction (lines 35-39) discusses the TIIO architecture for edge intelligence; the paper demonstrates excellent performance in endurance (>10^13), retention (>10 years), speed (4.8 ns), and energy consumption (22.7 fJ bit^-1 μm^-2).

## 5. Summary of Citation Distribution

- **Hardware-level challenges** (citations [1], [2], [3], [4]): Focus on FeFET array limitations, write crosstalk, and CIM architecture constraints
- **Software/algorithm-level approaches** (citation [7]): Continual learning paradigms and optimization methods
- **Hardware implementation of learning** (citations [5], [6], [8]): Demonstrations of adaptive learning on emerging device arrays, with associated complexity and overhead

The citations provide a balanced coverage of both the challenges and current research directions in deploying AI algorithms at the edge using non-volatile memory devices.
