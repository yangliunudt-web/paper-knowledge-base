---
title: "CMOS-Compatible Compute-in-Memory Accelerators Based on Integrated Ferroelectric Synaptic Arrays for Convolution Neural Networks"
authors:
  - "Min-Kyu Kim"
  - "Ik-Jyae Kim"
  - "Jang-Sik Lee"
  - "Min-Kyu Kim"
  - "Ik-Jyae Kim"
  - "Jang-Sik Lee"
date: "2022-04-08"
year: 2022
journal: "Science Advances"
doi: "10.1126/sciadv.abm8537"
abstract: "Convolutional neural networks (CNNs) require intensive multiply-and-accumulate (MAC) operations that strain conventional computing systems. This paper proposes a compute-in-memory (CIM) approach using integrated ferroelectric thin-film transistor (FeTFT) synaptic arrays. Three-terminal FeTFTs serve as both nonvolatile memory and access devices, overcoming leakage current and high-power issues of two-terminal crossbar-based CIM. FeTFTs enable efficient parallel programming and data processing through selective, accurate control of polarization in the ferroelectric (HfZrOx) layer. The integrated synaptic array performs convolution operations directly in memory, enabling high-accuracy image feature extraction for CNNs. The entire process is CMOS-compatible, making it suitable for practical semiconductor integration."
abstract_cn: "卷积神经网络（CNN）需要密集的乘累加操作，给传统计算系统带来巨大压力。本文提出了一种使用集成铁电薄膜晶体管（FeTFT）突触阵列的存内计算方法。三端FeTFT同时作为非易失性存储器和访问器件，克服了两端crossbar存内计算方案的漏电流和高功耗问题。FeTFT通过选择性、精确地控制铁电（HfZrOx）层极化实现高效的并行编程和数据处理。集成突触阵列直接在内存中执行卷积操作，实现高精度CNN图像特征提取。整个过程兼容CMOS工艺，适用于实际半导体集成。"
keywords:
  - "[[[[Compute-In-Memory]]]]"
  - "[[[[FeFET]]]]"
  - "[[[[Ferroelectric Synaptic Array]]]]"
  - "[[[[CNN]]]]"
  - "[[[[CMOS-Compatible]]]]"
  - "[[[[存内计算]]]]"
cite: "Kim M K, Kim I J, Lee J S. CMOS-Compatible Compute-in-Memory Accelerators Based on Integrated Ferroelectric Synaptic Arrays for Convolution Neural Networks[J]. Science Advances, 2022, 8(14): eabm8537. DOI: 10.1126/sciadv.abm8537"
aiSum: "补充材料：包含 HfZrOx 铁电特性表征、FeTFT 阵列制造工艺流程、器件 I-V 特性曲线等详细实验数据。"
confidence: "high"
parent:
  - "[[CMOS-compatible compute-in-memory accelerators based on integrated ferroelectric synaptic arrays for convolution neural networks]]"
---

MAAAS

# Supplementary Materials for

# CMOS-compatible compute-in-memory accelerators based on integrated ferroelectric synaptic arrays for convolution neural networks

Min-Kyu Kim, Ik-Jyae Kim, Jang-Sik Lee*

*Corresponding author. Email: jangsik@postech.ac.kr

Published 8 April 2022, Sci. Adv. 8, eabm8537 (2022)

DOI: 10.1126/sciadv.abm8537

This PDF file includes:

Figs. S1 to S10

![](images/dbcc0eebab1e715aca3586b942d7807475bf0aa5e3d9d7309bfd1366a3fa4c5a.jpg)  
Fig. S1. Ferroelectric characteristics of $\mathbf { H f Z r O _ { x } } .$ Polarization-voltage hysteresis curves of $\mathrm { H f Z r O _ { x } }$ with different ranges of voltage sweep (inset: schematic of a ferroelectric capacitor with a $\mathrm { M o / H f Z r O _ { \mathrm { X } } / W }$ structure). The ranges of voltage sweep increase from $\pm 2 \mathrm { ~ V ~ }$ to $\pm 6 \mathrm { V }$ in a step of 0.5 V.

![](images/29bd7666998fe3b16d07ace6f1f1f54210c5c637874c9582c0a05ef3149c5896.jpg)  
Fig. S2. Fabrication process of the ferroelectric synaptic transistor array. Optical images and schematic illustrations of fabrication process for the ferroelectric synaptic transistor array. Ferroelectric synaptic transistor array is composed of four $G L \mathbf { s } ,$ four $S L \mathbf { s } ,$ and nine DLs. ALD is used to deposit $\mathrm { H f Z r O _ { x } }$ and IZO layers. Array consists of 36 FeTFTs.

![](images/978f147640bee287583c956c1f45401f606ae7742d6254cc4434b129b1ee9c25.jpg)  
Fig. S3. $I _ { D L ^ { - } } V _ { G L }$ curves of the FeTFTs in the erased state and after program operations.

Before the measurements, FeTFTs are erased by applying an erase pulse (-5 V, 10 ms) to the $G L$ , while SL and DL are set to 0 V. After that, program pulses with a width of 10 ms are applied to the GL. The amplitudes of the program pulses increase from 2.5 to 5 V in increments of 0.25 V. The device states are confirmed by measuring IDL at $V _ { \mathrm { D L } }$ of 0.1 V, while sweeping $V _ { \mathrm { G L } }$ from 0 to -3.5 V.

![](images/72e500755f306a94e80f53d65b1ff49f8eba76eb74ebcb6ff3b3495a84688def.jpg)  
Fig. S4. Current changes of the FeTFTs according to pulse widths and amplitudes.

Before the measurements, FeTFTs are erased by applying an erase pulse (-5 V, 10 ms) to the $G L ,$ , while $S L$ and DL are set to 0 V. After that, program pulses are applied to the $G L .$ . Pulse widths of program pulses increase from 50 ns to 10 ms. The $I _ { \mathrm { D I } }$ of FeTFTs is measured by applying -2 V and 0.1 V to GL and DL, respectively.

![](images/44e819965de1964320e461c9b446f6731365c93dfdc333dd4af33cfccfdd4278.jpg)

![](images/f4f38bff3dc48d1348267601537a7b5455b40d1e07ba9af19285c186cdb394ce.jpg)

![](images/c1dc6a9dccdbaacf559f4e6a3ce5397f000e87961c962e0556d52c54aae6eca3.jpg)  
Fig. S5. Program-inhibit characteristics. (A) Equivalent circuits of ferroelectric synaptic transistor array with selected and unselected devices. (B) Program-inhibit operation method. Program pulses are applied to selected GL. Program-inhibit pulses are applied to selected SL and unselected DL. Amplitudes of the program and program-inhibit pulses are 4 and 2 V, respectively. The pulse widths of program and program-inhibit pulses are 10 and 30 ms, respectively. (C) Readout current of the unselected device for $1 0 ^ { 6 }$ program operation cycles.

![](images/05f355a2678b1460c76e111a709b37a58e3bdf2ca4982a4ea91525164759900f.jpg)

![](images/77646633b0ed25fc15ccacb206ff0da8b0d4df0adc2dcb417f58e44cfac6b594.jpg)  
Fig. S6. Row-wise parallel weight update characteristics of the ferroelectric synaptic transistor array. (A) Row-wise parallel weight update and read operation method. Two FeTFTs (C00, C20) in the same row are selected for row-wise parallel weight update operations. (B) Row-wise parallel weight update characteristics of FeTFTs in the array. First, $C _ { 0 0 }$ was selected for potentiation. After 32 pulse operations, $C _ { 0 0 }$ and $C _ { 2 0 }$ were both selected. At this stage, $C _ { 0 0 }$ and $C _ { 2 0 }$ had different states, so potentiation pulses with different amplitudes which could further update the states were used. After 64 pulse operations, C00 was unselected and $C _ { 2 0 }$ was selected until 96 pulse operations. After 96 pulse operations, C00 was selected for depression operation. After the 128 pulse operations, $C _ { 0 0 }$ and $C _ { 2 0 }$ were both selected. At this stage, $C _ { 0 0 }$ and $C _ { 2 0 }$ had also different states, so depression pulses for C00 and $C _ { 2 0 }$ had different amplitudes. After 160 pulse operations, the depression of C00 was finished and unselected. $C _ { 2 0 }$ was still selected for further depression to 192 pulse operations.

![](images/feffd4ee314f0e9d48bba9eeb87166052b94ec4dcb6c6955e17eaf3760b31fe0.jpg)

![](images/a7f5f04511b2f1f27bcf8217352fc37455bb9023b415a7c46bb725c2917bddcf.jpg)  
Fig. S7. Current-voltage behaviors of the FeTFT. (A) $I _ { \mathrm { D L } }  – V _ { \mathrm { D L } }$ curves of the FeTFTs in multiple states. Multiple states are induced by applying program pulses with different amplitudes and a fixed width of 10 ms. Before the measurements, the FeTFTs are erased by applying an erase pulse (-5 V, 10 ms) to the $G L ,$ while SL and DL are set to 0 V. The amplitudes of the program pulses increase from 2 to 5.5 V in increments of 0.25 V. $I _ { \mathrm { D L } }  – V _ { \mathrm { D I } }$ curves of the FeTFTs are measured at $V _ { \mathrm { G I } }$ of -2 V, while sweeping $V _ { \mathrm { D I } }$ from 0 to 0.1 V. (B) I-V linearity distribution of the FeTFTs in multiple states.

![](images/dbcfdd0f9cf8a6fd40d56a13c96739deb9f8a708095023a8d1bc13f55f35b069.jpg)  
A   
B

![](images/38a36529107e0dbeb4b62d34a59a0676fb160e6dbbdac276ad7e1dab3526870e.jpg)  
Fig. S8. Conductance map of the ferroelectric synaptic transistor array for the vertical kernel. (A) Vertical edge kernel. (B) Conductance map (unit of μS) of the ferroelectric synaptic transistor array for implementation of vertical edge kernel.

![](images/2fda7751b28a6a8350f6d74e4499ef4a970b9c5eab1548d2922e064841aa829b.jpg)  
A   
[Mean]

![](images/2732dc6ffa6e64e5f4268f6de880bd7359a4f9ef009cd8ee62c6370c143100ba.jpg)  
[Sharpen]

![](images/9e71512d0492627203f829bd4c128990dc87085958463f4a2308b78de850257b.jpg)  
Fig. S9. Conductance map of the ferroelectric synaptic transistor array for kernels for

image feature extraction. (A) Vertical edge, horizontal edge, mean, and sharpen kernels. These kernels are composed of 3 × 3-weight values, which are designed to extract the features of the image. (B) Conductance map (unit of μS) of the ferroelectric synaptic transistor array for vertical edge, horizontal edge, mean, and sharpen kernels.

![](images/d688b781136cd286bebe60d4f9020f91114c4de68d0d979794d31e6c0cf006d4.jpg)  
Fig. S10. Retention characteristics of FeTFTs for different conductance states of five devices.