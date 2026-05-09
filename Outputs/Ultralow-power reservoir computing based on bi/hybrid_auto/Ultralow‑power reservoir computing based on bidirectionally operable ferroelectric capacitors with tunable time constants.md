---

title: "Ultralow‑power reservoir computing based on bidirectionally operable ferroelectric\\"
authors:
  - "Linyuan Mo"
  - "Zhen Fan"
  - "Jiali Ou"
  - "Zhiwei Chen"
  - "Haipeng Lin"
  - "Wenjie Hu"
  - "Wenjie Li"
  - "Meixia Li"
  - "Boyuan Cui"
  - "Hua Fan"
  - "Ruiqiang Tao"
  - "Guo Tian"
  - "Minghui Qin"
  - "Xubing Lu"
  - "Guofu Zhou"
  - "Xingsen Gao"
  - "Jun‑Ming Liu"
date: "2026-01-01"
year: "2026"
journal: "Reports on Progress in Physics"
doi: "10.1088/1361‑6633/ae3984"
abstract: "Physical reservoir computing (RC) systems have emerged as a prominent research frontier\\"
abstract_cn: "物理储备计算系统因其在时序信息处理中的卓越效率而成为前沿研究热点。然而，现有主要基于电阻器件的实现方案在能效和动态丰富性方面面临挑战。本文提出一种用于储备计算的铁电电容器‑线性电容器串联器件。通过利用非线性极化翻转和回弹翻转，该串联器件实现了储备计算的两个关键特性：非线性和衰减记忆。此外，该器件具有超低功耗特性，结合其直接电压读出能力，标志着相对于电阻储备器件的重大进展。同时，该器件支持双向操作和宽范围可调的时间常数，从而增强了储备空间维度和状态丰富性。基于这些\\"
keywords:
  - "[[Reservoir computing]]"
  - "[[Ferroelectric capacitors]]"
  - "[[Polarization switching]]"
  - "[[Time‑series prediction]]"
cite: "[1] Mo L, Fan Z, Ou J, et al. Ultralow‑power reservoir computing based on bidirectionally\\"
aiSum: "铁电电容器‑线性电容器串联器件实现超低功耗储备计算，具备双向操作和可调时间常数，在波形分类、多模态数字识别和 Mackey‑Glass 时间序列预测中表现优异。"
confidence: "medium"
wiki_concepts:
  - "[[Reservoir computing]]"
---

# Ultralow-power reservoir computing based on bidirectionally operable ferroelectric capacitors with tunable time constants

Linyuan Mo1, Zhen Fan1*, Jiali Ou1, Zhiwei Chen1, Haipeng Lin1, Wenjie Hu1, Wenjie Li1, Meixia Li1, Boyuan Cui1, Hua Fan1, Ruiqiang Tao1, Guo Tian1, Minghui Qin1, Xubing Lu1, Guofu Zhou2, Xingsen Gao1 and Jun-Ming Liu 1,3

1 Institute for Advanced Materials and Guangdong Provincial Key Laboratory of Optical Information Materials and Technology, South China Academy of Advanced Optoelectronics, South China Normal University, 510006 Guangzhou, China.   
2 National Center for International Research on Green Optoelectronics, South China Normal University,u 510006 Guangzhou, China.   
3 Laboratory of Solid State Microstructures and Innovation Center of Advanced Microstructures, Nanjing University, 210093 Nanjing, China.

*Author to whom any correspondence should be addressed.

E-mail: fanzhen@m.scnu.edu.cn

Received xxxxxx

Accepted for publication xxxxxx

Published xxxxxx

# Abstract

Physical reservoir computing (RC) systems have emerged as a prominent research frontier due to their exceptional efficiency in temporal information processing. However, existingd implementations, predominantly utilizing resistive devices, face challenges pertaining to power efficiency and dynamic richness. Here, we propose a ferroelectric capacitor-linear capacitor (FC-LC) series device for RC implementation. By leveraging nonlinear polarization switching and back-switching, the FC-LC series device realizes two essential reservoire properties: nonlinearity and fading memory. In addition, the device exhibits an ultralow power consumption, which, along with its direct voltage readout capability, marks a t significant advance over resistive reservoir devices. Moreover, the device features bidirectional operation and widely tunable time constants, thereby enhancing reservoir space dimensionality and state richness. Building upon these FC-LC series devices, a ferroelectric p capacitive RC system is developed, which demonstrates superior performance in various benchmark tasks. By exploiting the bidirectional operation of the device, the RC system not only delivers enhanced performance in waveform classification but also enables highaccuracy multimodal digit recognition. Through strategically hybridizing the FC-LC series devices with varying time constants, the RC system achieves remarkable performance in c Mackey-Glass time-series prediction. Our study paves the way for power-efficient, dynamicrich RC systems capable of handling diverse temporal tasks.

Keywords: reservoir computing, ferroelectric capacitors, polarization switching, back-switching, time-series prediction

# 1. Introduction

Recurrent neural networks (RNNs), in which neurons generate outputs depending on both current inputs and stored memory, demonstrate remarkable capabilities in temporal data processing. Nevertheless, training RNNs remains notoriously challenging and computationally expensive, primarily due to the issues of exploding and vanishing gradients [1]. To address these issues, reservoir computing (RC) has emerged as a pivotal solution [2]. An RC system processes temporal inputs by nonlinearly mapping them into a high-dimensional feature space via a reservoir, generating linearly separable reservoir states that are subsequently analyzed by a readout layer (Figure 1(a)). Training the RC system necessitates only the training of the readout layer while the reservoir’s internal connections remain fixed. Moreover, the reservoir network can be significantly simplified into a single physical node with a time-delayed feedback loop using a time-multiplexing (or masking) approach [3–7]. By adjusting the delay time, the reservoir dynamics can be tailored to meet task-specific timescale requirements. [5] These advancements render the RC system an efficient and low-training-cost framework well suited for handling temporal tasks, such as speech recognition [1, 8, 9], chaotic system forecasting [1, 9, 10], pattern classification [11, 12], and other [13–15].

Recently, increasing attention has been paid to the hardware implementation of RC systems for boosted computational speed and energy efficiency [16]. Various emerging devices with intrinsic nonlinearity and fading memory, such as dynamic memristors [1, 9, 17–21], ferroelectric devices [15, 22–32], nanomagnetic systems [33– 37], and electrochemical transistors [14, 38–40], have been used to construct physical reservoirs. Notably, most of these devices are resistive devices whose conductance states arep harnessed as reservoir states (Figure 1(b)) [1, 2, 9, 13, 17–19,i 41–43]. Such devices typically operate by applying a write pulse to modulate the conductance state, followed by a read pulse for reading out the conductance state. During these operations, relatively high conduction currents are often generated, inevitably causing excessive power dissipation [44].c In addition, the resistive devices typically require current-tovoltage conversions to transfer the reservoir states to the readout layer [9, 22, 45], thereby increasing hardwares overhead and introducing extra energy consumption. Also noteworthy is that most resistive devices exhibit unidirectional relaxation behavior [1, 2, 8–12, 15–19, 23, 27, 41, 46–51], characterized by spontaneous current decay exclusively following unipolar pulse stimulation. This confines the device to unidirectional operation, thereby limiting the dimensionality of reservoir space and compromising the RC performance [52]. Besides, it is difficult to tailor the intrinsic

![](images/0e4828d2e428ed1a0d7c2f42bad1be5b0a205cbb3d7752b662370fde573e4e52.jpg)

![](images/efdcd7affb811b86d0611b65e6cb3210187bd131aec8e9b4f99e964caefb6276.jpg)

![](images/ce9cd7a06d4de858587e2315a2f67f3359c3e7641b7fc3a956ded41a17fc0c48.jpg)

![](images/624be32dbf8edd0da3510ad7e57c2b2c26416f68051dfaa0d5805999463e3f30.jpg)

![](images/e0d9b62d71af91b7a9088307f26ae153cf9abb3f7bda08366282459493d049b7.jpg)  
Figure 1. Implementation of RC using FCs. (a) Schematic diagram of an RC system for temporal data processing. The inputs are nonlinearly transformed into a high-dimensional feature space by a reservoir, whereupon a readout layer performs subsequent analysis. Only the weights in the readout layer, i.e., Wout, undergo training. Devices used for physical implementation of reservoirs: (b) resistive and (c) capacitivec devices. Proposed FC-LC series device as a reservoir device, where (d) polarization switching and (e) back-switching causes gradual increase

and decay in $V _ { \mathrm { o u t } } ,$ respectively. The electric fields inducing the polarization switching and back-switching are indicated in the bottoms of (d) and (e), respectively, where d is the thickness of the ferroelectric layer. In addition, “TE”, “FE” and “BE” represent the top electrode, ferroelectric layer, and bottom electrode, respectively.

dynamics of resistive devices once fabricated [53–56], resulting in limited tunability in relaxation time constant. This limitation constrains the richness of reservoir states and ultimately hinders the system’s efficacy in processing temporal information of multiple timescales. Therefore, existing hardware RC systems, primarily implemented with resistive devices, are challenged by limitations in power efficiency and dynamic richness.

To address these challenges, capacitive devices have emerged as promising alternatives for constructing physical reservoirs [44, 57]. The capacitive devices operate through charge accumulation and relaxation (Figure 1(c)), where displacement currents rather than conduction currents are generated. This mechanism enables two key advantages: direct voltage readout and theoretically zero static power dissipation. In addition, a specific class of capacitive devices known as ferroelectric capacitors, can exhibit nonlinear polarization switching in presence of an electric field and depolarization in its absence. These device characteristics align with the two essential features of a reservoir: nonlinearity and fading memory. Moreover, the ferroelectric capacitors offer unique opportunities for realizing bidirectional operation as well as tunable time constants. The bidirectional operation can expand the dimensionality of reservoir space, while the tunable time constants are crucial for enhancing the reservoir’s capability to extract multitimescale features. Therefore, utilizing bidirectionallyoperable ferroelectric capacitors with tunable dynamics as reservoir devices holds great promise for the development of power-efficient, dynamic-rich RC systems, a concept that has yet to be realized in practice.

Here, we propose a ferroelectric capacitor-based reservoir device encompassing all the above-mentioned advantages for implementing efficient RC. This device consists of a ferroelectric capacitor (FC) connected in series with a linear capacitor (LC), an innovative design that has not been reported hitherto. When an input voltage $( V _ { \mathrm { i n } } )$ is applied to the FC-LCe series device, polarization switching occurs in the FC, inducing charges on the LC (Figure 1(d)). The voltage acrosst the LC, denoted as $V _ { \mathrm { o u t } } ,$ , is directly read out and regarded as the reservoir state. By leveraging the inherent nonlinearity of polarization switching, the FC-LC series device achieves ap nonlinear dependence of Vout on $V _ { \mathrm { i n } } ^ { \prime } .$ In addition, fading memory, manifested as spontaneous decay of $V _ { \mathrm { o u t } }$ upon removal of $V _ { \mathrm { i n } } ,$ is realized by utilizing the polarization backswitching (i.e., depolarization) induced by $V _ { \mathrm { o u t } }$ feedback to the FC (Figure 1(e)). The bidirectionality of both the polarization switching and back-switching enables the FC-LC series device to operate under bipolar pulses. Besides, the time constant of the device is shown to be easily adjustable byc varying the capacitance of the LC. More importantly, the

device exhibits an ultralow power consumption (~1.3 μW per input), which is lower than those reported for most reservoir devices [1, 9, 10, 17–19, 46–51, 58–61].

A ferroelectric capacitive RC system based on these FC-LC series devices is further constructed, which delivers strong performance in benchmark tasks including arrhythmic p heartbeat detection and Hénon map prediction. By exploiting the bidirectional operation of the FC-LC series devices, the RC system not only achieves enhanced performance in waveform classification [normalized root mean square error r (NRMSE): 0.04] but also enables multimodal digit recognition with an accuracy of 97.6%. In addition, by intentionally hybridizing the FC-LC series devices with varying time constants, the RC system achieves superior performance in Mackey-Glass time-series predictions (NRMSE: 0.045). Our results indicate the great potential of ferroelectric capacitive devices in developing power-efficient, dynamic-rich RC systems capable of tackling diverseu temporal tasks.

# 2. Results and Discussionn

# 2.1. Ferroelectric properties of Pt/PZT/SRO FC

As a proof of concept, an FC with a two-terminal vertical structure, consisting of an ~120 nm $\mathrm { P b } ( Z \mathrm { r } _ { 0 . 2 } \mathrm { T i } _ { 0 . 8 } ) \mathrm { O } _ { 3 }$ (PZT) epitaxial film sandwiched between a SrRuO3 (SRO) bottom electrode and a Pt top electrode (diameter: ~100 μm) , is fabricated, as schematically shown in the left panel of Figure 2(a). The PZT epitaxial film is chosen as the ferroelectric layer of the FC for its excellent ferroelectric properties (to be demonstrated later). The high-quality epitaxial growth of the PZT film is confirmed by the X-ray diffraction (XRD) results (Figure S1). The high quality of the PZT film is also reflected by its flat surface with a root-mean-square roughness of ~440 pm, as shown in Figure S2(a). The ferroelectricity of the PZT film is investigated by using piezoelectric force microscopy (PFM). Figure 2(b) shows the PFM phase image after writing a box-in-box pattern (outer: +5 V; inner: −5 V) on the PZT film. The sharp 180o phase contrast between the +5 V and −5 V written areas validates the ferroelectricity of the PZT film. Additional evidence for the ferroelectricity lies in the observed butterfly-shaped amplitude loop and square phase loop with 180o switching (Figure S2(b)).

To further assess the ferroelectric properties, polarizationvoltage (P-V) hysteresis loops are measured for the Pt/PZT/SRO FC. Figure 2(c) presents a typical P-V loop, showing a well-defined square shape and a high remnant polarization (Pr) of ~90 μC/cm2. Such a high Pr is beneficial for creating a large reservoir space, highlighting a key advantage of our epitaxial PZT-based FC over other FCs [32,

62, 63] for RC applications. In addition, our FC exhibits a polarization retention time as long as 24 h in absence of an external field (Figure S3(a)). This retention time can be shortened by introducing a depolarization effect associated with $V _ { \mathrm { o u t } }$ (to be demonstrated later), enabling the fading memory as required by a reservoir. Moreover, our FC sustains polarization switching over $1 0 ^ { 9 }$ cycles (Figure S3(b)), showcasing a high endurance that is crucial for reliable reservoir operation. These excellent ferroelectric properties make the Pt/PZT/SRO FC a favorable candidate to implement the proposed FC-based reservoir.

# 2.2. Nonlinearity and fading memory in FC-LC series device

Next, the Pt/PZT/SRO FC is connected in series with an LC (capacitance: 330 pF) to form a reservoir device, as illustrated in the right panel of Figure 2(a). A switch $\mathrm { S } _ { 0 } ,$ parallel to the LC, is used to short-circuit the LC when necessary. The input voltage pulse $V _ { \mathrm { i n } }$ is applied to Node 1 (corresponding to the top electrode of the FC), while Node 3 is grounded. Thep voltage across the LC, denoted as $V _ { \mathrm { o u t } } ,$ is monitored and used as the reservoir state. This direct voltage readout can greatly reduce the power consumption and latency compared with the conventional current readout, as current-to-voltage conversionr is bypassed entirely.

![](images/b50a544b0c08e6f52ef835ea36d780de9642416dae38dd463c683be75f01138e.jpg)  
(a)

![](images/5f91be0a71c8956e2f3054b403eb060b4d56c29a4dd8436a20389140e23ae51b.jpg)

![](images/ff5c8f0e52b7df36b48c7b7f2bdf26489913dc69320ea61d420697c943eb9412.jpg)  
(c)

![](images/48c4eda12546e19df28b150928494f1326a6b73c6ac8badc53e266550bb05305.jpg)  
(d)

![](images/d5a888113877b42c27cc4eb0fb234197e9b9fe8a53c035c2dc56c96ddf766cba.jpg)  
(e)

![](images/b2aae918643d54bc6c1956bc471ae09a21a443a6cdf49dff2965c342720eec90.jpg)  
(f)

![](images/1784a0ce48905b0db0ca64ac60a3315123da799ac86f5920076637836ceda07d.jpg)  
(g）  
Figure 2. Device characteristics of FC and FC-LC series device. (a) Schematic structures of Pt/PZT/SRO FC (left panel) and FC-LC series device (right panel). (b) PFM phase image of PZT film after writing a box-in-box pattern (outer: +5 V; inner: −5 V). (c) Typical P-V loop of FC measured using the inset setup. Whene $\mathrm { \Delta S _ { 0 } }$ is turned on, the LC is short-circuited and $V _ { \mathrm { i n } }$ is completely applied to the FC. (d) $V _ { \mathrm { o u t } } { - } V _ { \mathrm { i n } }$ characteristics of FC-LC series device measured using the inset setup. When S0 is turned off, Vin is shared between the FC and LC. (e) Switched polarization in the FC (PFC) versus its partitioned voltage (VFC) calculated from the results in (d). (f) Typical $V _ { \mathrm { o u t } }$ response of FC-LC series device to a Vin pulse of +3 V. (g) Vout responses monitored while applying pairs of +3 V and –3 V pulses with different delay periodsc (tdelay). The upper panel shows the schematics of the applied pulses, which are slightly shifted along the vertical axis for visual clarity. Following the $\widetilde { t _ { \mathrm { d e l a y ; } } }$ , S0 is turned on to short-circuit the LC. The insets in the lower panel schematically show the polarization configurations in the FC and charges on the LC in different states. States I and IV refer to the states right after tdelay, and more polarization is back-switchedc in State IV due to a longer tdelay. Upon short-circuiting the LC, State I (IV) transitions to State II (V), where the $V _ { \mathrm { o u t } }$ becomes zero while the

polarization configuration remains unchanged. Subsequently, State II (V) changes to State III (VI) following the application of $\mathbf { a } - 3 \mathrm { ~ V ~ }$ pulse to switch the polarization and induce $V _ { \mathrm { o u t } } .$ The less polarization available for switching in State V results in a smaller magnitude of $V _ { \mathrm { o u t } }$ in State VI.

We first measure the $V _ { \mathrm { o u t } } – V _ { \mathrm { i n } }$ characteristics of the FC-LC series device. Prior to this measurement, the FC is preset by applying a sufficiently high $V _ { \mathrm { i n } }$ while turning on S0 to shortcircuit the LC (the same preset approach will be used hereafter unless otherwise specified). Subsequently, a triangular waveform $V _ { \mathrm { i n } }$ is applied with $\mathrm { S } _ { 0 }$ turned off, while simultaneously measuring $V _ { \mathrm { o u t } } .$ The resultant $V _ { \mathrm { o u t } } – V _ { \mathrm { i n } }$ characteristics are shown in Figure $2 ( \mathrm { d } )$ , displaying nonlinear and hysteretic behavior. This behavior is attributed to the polarization switching in the $\mathrm { F C } ,$ , since $V _ { \mathrm { o u t } }$ can directly reflect the switched polarization in the $\mathrm { F C - L C }$ series configuration. In contrast, when the FC is replaced by an LC, forming an $\mathrm { L C _ { - } }$ LC series configuration, purely linear $V _ { \mathrm { o u t } } – V _ { \mathrm { i n } }$ characteristics without any hysteresis are observed (Figure S4). These results unambiguously demonstrate that the polarization switching in the FC plays an essential role in achieving the nonlinear and hysteretic $V _ { \mathrm { o u t } } { - } V _ { \mathrm { i n } }$ characteristics of the FC-LC series device.

To more explicitly show the polarization switching in the $\mathrm { F C } ,$ Figure 2(d) is replotted as Figure 2(e), presenting the switched polarization $( P _ { \mathrm { F C } } = C _ { \mathrm { L C } } V _ { \mathrm { o u t } } / A _ { \mathrm { F C } } )$ versus the voltage across the FC $( V _ { \mathrm { F C } } = V _ { \mathrm { i n } } - V _ { \mathrm { o u t } } )$ , where $C _ { \mathrm { L C } }$ is the capacitance of the $\mathrm { L C } , C _ { \mathrm { L C } } V _ { \mathrm { o u t } }$ is the charge that is the same for the LC and FC due to their series connection, and AFC is the electrode area of the FC. It is clearly seen that the $\mathrm { F C }$ exhibits typical subloops, indicating that only partial of the polarization is switched (see the comparison of polarization values between Figure $2 ( \mathrm { c } , \mathrm { e } ) )$ . This partial switching behavior arises because the $V _ { \mathrm { F C } } \mathrm { ~ - ~ }$ the driving force for polarization switching ⎯ is relatively low due to the voltage partitioning caused by the LC. Note that our FC in the FC-LC series configuration is intentionally designed to operate in the partial switching regime. This design enables the FC to exhibit multiple intermediate states without rapid saturation under repeated pulse stimulation, which is critical for achieving high reservoir state richness.

Having demonstrated the $V _ { \mathrm { o u t } } – V _ { \mathrm { i n } }$ nonlinearity of the FC-LC series device and identified its origin as the partial polarizatione switching in the $\mathrm { F C } ,$ our study now shifts focus to investigate the fading memory of the device and its underlying t mechanism. We begin with presetting the FC using the previously described approach, and then monitor the $V _ { \mathrm { o u t } }$ response of the device while applying a square pulsep $V _ { \mathrm { i n } }$ to it. Figure 2(f) depicts the Vout response to a $V _ { \mathrm { i n } }$ pulse of +3 V, accompanied by a longer-term measurement in Figure S5. During the application of the Vin pulse, $\bar { \bar { \rho } } _ { \mathrm { o u t } }$ first rises rapidly and then increases gradually. The increase in $V _ { \mathrm { o u t } }$ comes from two major contributions: linear dielectric response and polarization switching. When the $V _ { \mathrm { i n } }$ pulse is withdrawn, $V _ { \mathrm { o u t } }$ undergoes a sudden drop followed by a gradual decay. The sudden drop of $V _ { \mathrm { o u t } }$ is attributed to the rapid decline in linear dielectric contribution, leaving the residual $V _ { \mathrm { o u t } }$ dominated by

the polarization of the FC. The subsequent gradual decay of $V _ { \mathrm { o u t } }$ signifies the fading memory effect, which, in conjunction with the above-demonstrated nonlinearity, establishes the FC-t LC series device as a capable candidate for reservoir implementation.

To elucidate the mechanism underlying the fading memoryp behavior of the FC-LC series device, we conduct the following experiment. First, a pulse with $V _ { \mathrm { i n } } = + 3$ V is applied, followed by a delay period $\left( t _ { \mathrm { d e l a y } } \right)$ during which $V _ { \mathrm { o u t } }$ is allowed to relax. Then, the switch S0 is turned on to short-circuit ther $\mathrm { L C } ,$ forcing $V _ { \mathrm { o u t } }$ to be zero. Afterward, another pulse with $V _ { \mathrm { i n } } = - 3 \mathrm { ~ V ~ }$ is applied while turning off $\mathrm { S } _ { 0 } . \big | \overline { { V _ { \mathrm { o u t } } } }$ is monitored throughout the whole experiment. Figure 2(g) shows that as $t _ { \mathrm { d e l a y } }$ increases, the magnitude of the residual $V _ { \mathrm { o u t } }$ after the +3 V pulse decreases (see comparison between States I and IV in Figures $2 ( \mathrm { g } ) )$ . This finding indicates that polarization back-switching $( \mathrm { i . e . } ,$ , depolarization) occurs during $t _ { \mathrm { d e l a y } }$ . As $V _ { \mathrm { i n } } = 0$ during $t _ { \mathrm { d e l a y } } ,$ some polarization initially aligned by the +3 V pulse mayu undergo back-switching under the effect of $V _ { \mathrm { o u t } }$ feedback to the FC. A prolonged $\scriptstyle t _ { \mathrm { d e l a y } }$ allows more polarization to be backswitched. Consequently, less polarization is available forn switching by the subsequent $- 3 \mathrm { ~ V ~ }$ pulse, resulting in smaller magnitude of the residual $V _ { \mathrm { o u t } }$ after this pulse (see comparison between States III and VI in Figurea $2 ( \mathrm { g } ) )$ ).

Note that the gradual $V _ { \mathrm { o u t } }$ decay during $\scriptstyle t _ { \mathrm { d e l a y } }$ cannot be attributed to charge leakage; otherwise, the residual $V _ { \mathrm { o u t } }$ t after the $- 3 ~ \mathrm { ~ V ~ }$ –3 pulse would be the same regardless of $t _ { \mathrm { d e l a y } } ,$ , inconsistent with the findings presented in Figure 2(g). In addition, the $V _ { \mathrm { o u t } }$ decay is not associated with the depolarization in certain stand-alone $\mathrm { F C s , }$ as our FC under stand-alone conditions exhibits negligible depolarization (Figure S6). Besides, when the FC is replaced by an LC, only a sudden drop of $V _ { \mathrm { o u t } }$ to zero is observed after the $V _ { \mathrm { i n } }$ pulse, with no sign of residual $V _ { \mathrm { o u t } }$ and its gradual decay (Figure S7). A combination of these results evidence that the gradual $V _ { \mathrm { o u t } }$ t decay, a manifestation of fading memory, is caused by the Vout-induced polarization back-switching in the FC.

Given that the fading memory is achieved through the $V _ { \mathrm { o u t } } \mathrm { - }$ induced polarization back-switching, concerns on device endurance may arise, as this “switching” mechanism may impose a heavier burden on the device than the “passive relaxation” typically observed in conventional reservoir devices. Nevertheless, the FC-LC series device demonstrates endurance of at least $1 0 ^ { 7 }$ cycles under cyclic +3 V/−3 V pulses (pulse width: 0.15 ms) (Figure S8), which is comparable to or even superior to that of previously reported reservoir devices [22, 64–66]. This can be attributed to the following factors. First, as mentioned earlier, the FC in the FC-LC architecture experiences only moderate voltages and is indeed partially switched, meaning its operation conditions are not as harsh as initially assumed. Additionally, our FC is based on a high-

quality epitaxial ferroelectric PZT film and an SRO bottom electrode, a structure widely recognized for its high endurance [67]. Together, these factors contribute to the high endurance of our FC-LC series device.

# 2.3. Key advantages of FC-LC series device

With the above-demonstrated nonlinearity and fading memory, the FC-LC series device can readily be used as a reservoir device. In comparison to conventional reservoir devices, the FC-LC series device possesses several key advantages. The first advantage is its bidirectional operation capability. Conventional reservoir devices typically exhibit unidirectional relaxation behavior and thus only support unidirectional operation [1, 2, 8–12, 15–19, 23, 27, 41, 46–51]. This limits the dimensionality of reservoir space and ultimately the RC performance.

Unlike these devices, the FC-LC series device can operate under bipolar pulses. This can be evidenced by Figure 3(a, b), showing that both positive and negative $V _ { \mathrm { i n } }$ pulses induce Vout enhancement (i.e., memory forming) followed by post-pulse $V _ { \mathrm { o u t } }$ decay (i.e., memory fading). The residual $V _ { \mathrm { o u t } }$ after the $V _ { \mathrm { i n } }$ pulse increases with pulse amplitude or width, and this trend holds true for both pulse polarities. In addition, Figure $3 ( \mathrm { c } , \mathrm { d } )$ show that the residual $V _ { \mathrm { o u t } }$ nonlinearly increases with successive short-interval pulses (interval: 0.15 ms), while it decreases as the pulse interval becomes longer (interval: 1.05 ms). Such pulse interval-dependent memory accumulation and decay behavior is preserved for both pulse polarities. These results demonstrate the capability of the FC-LC series device to operate under bipolar pulses, significantly expanding the dimensionality of reservoir space. Moreover, this capability paves the way for multimodal signal processing (to be demonstrated later).

The bidirectional operation of the FC-LC series device is facilitated by the bidirectionality of both polarization switching and back-switching. Specifically, the polarization can be bidirectionally switched depending on the polarity of the $V _ { \mathrm { i n } }$ pulse. In absence of the $V _ { \mathrm { i n } } / \mathsf { p u l s e }$ , bidirectional polarization back-switching can occur according to thee polarity of the residual $V _ { \mathrm { o u t } } .$ Therefore, the memory forming and fading can be realized under both positive and negativet pulses. The increase in the residual $\boldsymbol { V _ { \mathrm { o u t } } }$ with pulse amplitude or width can be explained by the fact that more polarization is switched by a large or wider pulse. In addition, as the pulse interval is shortened (elongated), less (more) polarization is allowed to be back-switched, thereby leading to a higher (lower) residual $V _ { \mathrm { o u t } } .$ . Thanks to the bidirectionality of bothe polarization switching and back-switching, the pulse amplitude-, width-, and interval-dependent memory evolution trends remain consistent across both pulse polarities.

The second advantage of the FC-LC series device is its tunability in time constant. Most existing reservoir devices typically exhibit fixed temporal dynamics once they are

fabricated, making it difficult to tailor their time constants [53–56]. This limitation restricts the richness of reservoir states and impairs the reservoir’s capability to extract multitimescale features. To address these issues, one commonly used approach is to leverage device-to-device variations to achieve different time constants [1, 27, 46, 50, 51, 54]. Nevertheless, the range of the time constants obtained from this approach is uncontrollable. Other approaches involve various input encoding schemes, such as pulse-widthp encoding [41] and masking [2, 9]. However, these approachesi necessitate the use of additional circuitry for input encoding, increasing hardware overhead and power consumption. To overcome the limitations — without aiming to fully replace these approaches, given their effectiveness in processing complex tasks [3–5] — it is crucial to develop reservoir c devices with controllably tunable dynamics. This can be easily realized in our FC-LC series devices by manipulating the capacitance of the $\operatorname { L C } { \mathrm { ( i . e . , } } C _ { \mathrm { L C } } { \mathrm { ) } } .$ As shown in Figure 3(e), the FC-LC series device exhibits distinct temporal responses to identical input pulses $( V _ { \mathrm { i n } } = 4 3 ~ \mathrm { V } )$ as $C _ { \mathrm { L C } }$ varies from 100 pF to 2.2 nF. Through fitting, the time constants related to the gradual $V _ { \mathrm { o u t } } ~ \mathrm { d e c a y }$ are extracted (Figure S9). Figure 3(f) reveals a positive correlation between the time constant and $C _ { \mathrm { L C } }$ . Moreover, as CLC increases from 1 pF to 33 nF, a broad range of tunable time constants from ~0.01 to ~3 ms is obtained.

The tunable time constant in our FC-LC series device arises from two synergistic mechanisms. First, adjusting $C _ { \mathrm { L C } }$ directly modulates the RC time constant, which has been reported in some previous works [56, 68–70]. Besides, our device exhibits an indirect effect mediated by the FC. Specifically, varying CLC alters the voltage partitioned by the FC. Since the capacitance of the FC (CFC) is voltage-dependent, this in turn modifies $C _ { \mathrm { F C } } .$ . The resulting change in CFC amplifies the time constant tuning effect caused by the $C _ { \mathrm { L C } }$ variation, thus distinguishing our device from previously reported devices with tunable time constants [56, 68–70].

These results demonstrate that the FC-LC series device can exhibit tunable time constants by adjusting $C _ { \mathrm { L C } } .$ Such tunability allows diverse mappings of inputs across different timescales, creating a high-dimensional space with rich reservoir states. Consequently, the reservoir gains enhanced capability to extract multi-timescale features, thereby improving the performance of the RC system in processing tasks with complex temporal dynamics. In addition to the time constant, the nonlinearity, characterized by the nonlinear relationship between the residual $V _ { \mathrm { o u t } }$ and $V _ { \mathrm { i n } } ,$ can also be tuned by varying CLC (Figure S10).

The third advantage of the FC-LC series device is its ultralow power consumption. The power consumption of the device under typical operation conditions is estimated to be ~1.3 μW per input using Eq. (S3) in Supplementary Note 1. This total power consumption comprises contributions from

![](images/c5c577754b102a0547430ec0ec099e7deb20decfa3f319c46df9a5a51f0b3acf.jpg)

![](images/6180530f7431113b38eb43429c2d44487af2c9d18352489b39d266c4f0b0d454.jpg)

![](images/44845cb90d82ddb65ad8ea3f71bd18903620ad67d82c6c92600b2b50d9dbb799.jpg)

![](images/89a0e3b3fd98acc1137168df8b59d8c1cefafb753199a638f5cb2aa747bb71b3.jpg)

![](images/6bee00a0c98ddd8e3973fed5d7bc4077e3a2350f1202133266061608eb7ae047.jpg)

![](images/a0d93e7c572fced8ab8661ccb34aebcc6927616a6e862908e9844397de33038c.jpg)

![](images/6132fd1ffe2f6747a16f1025be5cf2ad8b87dd2202c54d7caf53be9882fcd48f.jpg)  
Figure 3. Bidirectional operation and tunable time constants of FC-LC series device. $V _ { \mathrm { o u t } }$ responses to $V _ { \mathrm { i n } }$ pulses with varying (a) amplitudes (width fixed at 0.15 ms) and (b) widths (amplitude fixed at ±3 V). $V _ { \mathrm { o u t } } ^ { \bar { } }$ responses to 4 successive (c) +3 V and (d) –3 V pulses. In the left panels of (c) and (d), the interval between each pulse is 0.15 ms, while in the right panels, the interval between the third and fourth pulse is extended to 1.05 ms. The star symbol indicates the residual Vout value measured 24 μs after each pulse. (e)d $V _ { \mathrm { o u t } }$ responses to identical +3 V/0.15 ms pulses for FC-LC series devices with different CLCs. $^ { * * } \mathrm { L C _ { 1 0 0 } } ^ { , * } , \ ^ { * } \mathrm { L C _ { 2 0 0 } } ^ { , * } , \ ^ { * } \mathrm { L C _ { 3 3 0 } } ^ { , * } , \ ^ { * } \mathrm { L C _ { 8 2 0 } } ^ { , * } ,$ and “LC2200” denote the linear capacitances of 100, 200, 330, 820, and 2200 pF, respectively. (f) Relaxation time constant as a function of CLC. (g) Performance comparison between our FC-LC series device and other reservoir devices. max/min denotes the ratio of the upper bound to the lower bound of the tunable time constant range. Red symbols indicate the devices with bidirectional operation capability.e

both dynamic (related to hysteretic polarization switching) and static (associated with leakage current) powert consumptions. However, some previous studies reported very low power consumptions considering only the static component (i.e., $V _ { \mathrm { i n } } \ \times \ I _ { \mathrm { l e a k a g e } } ) .$ For example, Ref. [44]p reported a static power consumption of 0.9 nW per input for a Zr-doped HfO2-based memcapacitor. For our FC-LC series device, based on its leakage current characteristics (Figure S11), the estimated static power consumption is 0.096 nW, which is 10× lower than the previously reported value. Nevertheless, for a fair comparison with other devices, we will focus on the total power consumption of the FC-LC series device (~1.3 μW) in the following discussion.c

Figure 3(g) highlights the advantages of our FC-LC series device when compared to other reservoir devices. The FC-LC series device stands out as one of the few devices capable of bidirectional operation. Moreover, it boasts the widest range of tunable time constants and the lowest power consumption. These notable advantages establish the FC-LC series device as a highly promising platform for RC applications, as we will demonstrate in the following sections.

# 2.4. Ferroelectric capacitive RC system based on FC-LC series devices

The FC-LC series devices are used to construct a ferroelectric capacitive RC system. As schematically shown in Figure 4(a), the reservoir of this system is always physically implemented by using multiple FC-LC series devices. The LC capacitances are kept constant $( C _ { \mathrm { L C } } = 3 3 0$ pF) for all subsequent tasks unless otherwise specified. The readout layer is physically implemented with adjustable resistors only for an arrhythmic heartbeat detection task, while being simulated for all other tasks. Depending on the specific task, input signals are converted into voltage pulses either directly or through masking [32, 71–73], which are subsequently applied to the reservoir. The resulting reservoir state, represented by the collective $V _ { \mathrm { o u t } }$ values of all the FC-LC series devices, is sent into the readout layer for processing through a linearly weighted summation in order to generate a predicted outcome.

We first evaluate the temporal signal processing performance of the ferroelectric capacitive RC system by using two benchmark tasks: arrhythmic heartbeat detection and Hénon map prediction. The arrhythmic heartbeat detection task is carried out with the MIT-BIH heart arrhythmia database [74], which comprises 30-min electrocardiogram recordings from 48 subjects. An original electrocardiogram waveform is re-sampled at a frequency of 72 Hz and chopped into heartbeat segments lasting 208 ms (i.e., 15 time steps). This results in a total of 200 heartbeat segments, with each labelled as healthy or arrhythmic. Out of them 100 heartbeat segments (50% healthy, 50% arrhythmic) are randomly selected for training, with the rest for test (see examples in Figure 4(b) and all the samples in Figure S12). Each heartbeat segment is further chopped into 5 subsections, with each subsection converted to a 3- timeframe pulse train (see illustration in Figure 4(c)). The pulse amplitude is linearly mapped from the amplitude of the heartbeat signal, while the pulse width is fixed at 0.15 ms. The 5 pulse trains are applied to the reservoir consisting of 5d FC-LC series devices, with each device receiving one of the pulse trains. The residual $V _ { \mathrm { o u t } }$ is recorded 24 μs after the last pulse for each device. This timing ensures the exclusion of the linear dielectric response while maintaining a high signalto-noise ratio. The $V _ { \mathrm { o u t } }$ values of the 5 devices constitute the reservoir state. These $V _ { \mathrm { o u t } }$ values are subsequently sent to a 5 × 1 readout layer physically implemented with adjustable resistors to perform the linearly weighted summation. The summed current is then fed into a sigmoid activation functionp to generate the final neuronal output, where the values of 0 and 1 represent arrhythmic and healthy, respectively.e Training of the readout layer is accomplished through regularized logistic regression.

Figure S13 shows the photography and circuit diagram of c the hardware RC system based on FC-LC series devices and adjustable resistors for the arrhythmic heartbeat detection task. Figure 4(d) displays the reservoir states generated byc

the 5 FC-LC series devices when processing 8 typical heartbeat segments from the test set. The reservoir states exhibit distinct patterns for healthy versus arrhythmic heartbeats, demonstrating the reservoir’s capability to produce distinguishable responses to different temporal inputs. The reservoir states are subsequently processed by the readout layer, generating summed currents as displayed in Figure 4(e) and Video 1. It is seen that the summed currents corresponding to the healthy heartbeats are positive, whilep those corresponding to the arrhythmic heartbeats arei negative. The summed currents are further converted to neuronal outputs after passing through the sigmoid activation function. Figure S14 illustrates that the neuronal outputs of all the test samples agree well with their labels, achieving 100% classification accuracy.

In addition to arrhythmic heartbeat detection, Hénon map prediction is employed as another benchmark task for evaluating the performance of the ferroelectric capacitive RC system. The Hénon map is one of the most studied dynamic systems exhibiting chaotic behavior. It transforms a point (x(n), y(n)) in the 2D plane into a new point (x(n + 1), y(n + 1)) through the equations below:

$$
x (n + 1) = y (n) - 1. 4 x (n) ^ {2}. \tag {1}
$$

$$
y (n + 1) = 0. 3 x (n) + w (n). \tag {2}
$$

where n is the time step, and w(n) is a Gaussian noise with a mean of 0 and a standard deviation of 0.05. Substituting Eq.a (2) into (1), the equation is simplified to involve only x, thereby turning the task to the prediction of x(n + 1) based on the known values up to x(n).

We create a dataset comprising an x(n) series with a length of 500, where the first 300 data points are designated for training while the rest are reserved for test. Before being sent to the reservoir, the input x(n) undergoes pre-processing via a mask technique [75, 76]. The mask is a 1D vector composed of randomly assigned binary values of 1 and –1. Each data point in x(n) is multiplied by N masks, each of length M, and then converted to N M-timeframe pulse trains (pulse amplitude: linearly mapped from the masked input; width: 0.15 ms). These pulse trains are applied to a reservoir composed of N FC-LC series devices, with each device receiving one pulse train. The residual $V _ { \mathrm { o u t } }$ (24 μs after each pulse) is recorded as a virtual-node state, yielding a total of N × M virtual-node states from all the devices. These virtualnode states are fed into a $( N \times \ M + 1 ) \times \ M$ readout layer (including a bias) to output a predicted x(n + 1) value. The readout layer is trained via linear regression.

Figure S15 shows that the prediction performance of the ferroelectric capacitive RC system is influenced by the parameters N and M. When M is fixed at 4, the NRMSE decreases with increasing N due to the expanded reservoir size (Figure S15a). When M × N is fixed at 24, the NRMSE first decreases and then increases with increasing M, attaining its minimum value at M = 4 (Figure S15b). This

phenomenon may be attributed to the following factors. A mask that is too short results in a very limited number of

![](images/9b398444a5cc75bb198f2c4d08b167ad3ca248f408049ba7b3fa081a8c831f13.jpg)

![](images/b9dbb93399c19de9c1d5d9e766c8d85656411911a3979b2291264f21f3c838b3.jpg)

![](images/c45778d2bfdb174f7fb5e8f04a3dda0a84c000d0da6aaacb86187dcece2f46ae.jpg)

![](images/1c1efbb970a4ad25da03f4de5adff4b9cb42dc87f982e1a15c51d3df0fd86014.jpg)

![](images/5b21dab75bff4519a11c2b80663ec6ca60c70cd4cb7bd06619d98142e41ca965.jpg)

![](images/c2f2369efa183aeef72a91452b2e993661bb3edbfdf1ab2613b620b15cd46603.jpg)  
Figure 4. Performance of ferroelectric capacitive RC system in benchmark tasks. (a) Schematic of a ferroelectric capacitive RC system whose reservoir layer is implemented with FC-LC series devices. (b) Examples of arrhythmic and healthy heartbeat segments. (c) Schematicd illustration of encoding a heartbeat segment into pulse trains. (d) Reservoir states measured from 5 FC-LC series devices under stimulation by 8 typical heartbeat segments from the test set. (e) Summed currents produced by the readout layer during the presentation of 8 typical heartbeat segments. (f) Predicted Hénon map time series versus its ground truth on the test set. (g) 2D plot of the results in (f)

distinct mask sequences. This reduces the richness of reservoir states, leading to a high NRMSE. Conversely, if the mask length M is too long, the device’s Vout response may become excessively high or low during the pulse train application [9]. This weakens the feedback strength of the reservoir, thereby elevating NRMSE. Therefore, the lowest NRMSE is achievedp at an intermediate M that may best match the timescale of reservoir response.

When employing the optimized values (N = 6 and M = 4), the RC system predicts an x(n) series closely aligning with its ground truth during the test (Figure 4(f)). This high level of c consistency is further confirmed by a 2D visualization of the results (Figure 4(g)). The resulting NRMSE value is

calculated as 0.025, which is close to the previously reported state-of-the-art values [9, 22, 32].

For comparison, a control RC system is established by replacing the FCs in the reservoir with LCs. This control RC system achieves 84% accuracy in the arrhythmic heartbeat detection and 1.01 NRMSE in the Hénon map prediction (Figure S16). Such performance is notably inferior to that of the ferroelectric capacitive RC system, demonstrating that the FC’s nonlinearity and fading memory are critical to achieving superior RC performance.

Besides these benchmark results, our ferroelectric capacitive RC system presents distinctive prospects for achieving enhanced performance by taking advantage of the bidirectional operation and tunable time constants of the FC-

LC series device. We first demonstrate the benefits of the bidirectional operation by using a waveform classification task. In this task, the input sequence consists of randomly generated sine and square waveforms (see Figure 5(a)), while the target output is a binary sequence of −1 and +1, corresponding to the sine and square waveforms, respectively (see black curve in Figure 5(b)). The input sequence is preprocessed through the aforementioned mask technique with the mask parameters M = 4 and N = 12. The masked inputs are then converted into pulse trains via two pulse schemes. The first (second) scheme contains unipolar (bipolar) pulses, with the pulse amplitude linearly mapped from the masked input into a range of [0, 6 V] ([−3, 3 V]) and the pulse width fixed at 0.15 ms, as depicted in Figure 5(c). After applying the pulse trains to a reservoir with 12 FC-LC series devices, 48 virtualnode states are produced and subsequently fed into a 49 × 1 readout layer (trained via linear regression) to generate an output.

As illustrated by Figure 5(b), the ferroelectric capacitive RC system exhibits significantly superior waveform classification performance when utilizing the bipolar pulse scheme compared to the unipolar pulse scheme (NRMSE: 0.04 versus 0.12). This superiority in performance achieved with the bipolar pulse scheme remains robust across varying mask parameters (Figure 5(d)). The enhanced performance is attributed to the FC-LC series device’s capability to effectively function under bipolar pulses, which can expand the effective reservoir size (see quantitative evidence in Figure S17). Besides, a qualitative analysis reveals that the bipolar operation can enhance the reservoir’s feedback strength and state richness (Figure S18). Note that such bidirectional operation capability is typically absent in resistive devices [1, 9, 10, 17–19, 46–51]. As a result, the NRMSE of 0.04 achieved by our ferroelectric capacitive RC system is lower than those reported for most resistive RC systems [9, 15, 22].

In addition to enhanced temporal signal processing d performance, the bidirectional operation also facilitates multimodal signal processing as signals of different modes can be encoded into pulses of different polarities [52]. To demonstrate this, we design a ferroelectric capacitive RC e system for digit recognition, integrating both image and speech inputs. The reservoir in this system consists of two groups of FC-LC series devices: one group for processing image information encoded as positive pulses, while the other for processing speech information encoded as negative pulses.p The extracted features from these two modalities are subsequently fused and analyzed by a readout layer.e

In data preparation, we randomly select 500 handwritten digit images (28 × 28 pixels) from the Modified National Institute of Standards and Technology (MNIST) database, and 500c audio waveforms of spoken digits from the NIST TI-46 database [77]. Each digit image is randomly paired with an audio waveform of the same digit, forming an input sample.c

These 500 input samples are used for a 10-fold crossvalidation (90% training, 10% validation) to evaluate system performance, following the pre-processing steps as follows. First, each image is binarized while preserving its key features (see transformation from Figure 5(e) to 5(f)). On the other hand, each audio waveform is transformed into a cochleagram with 49 frequency channels and 22 time steps using the Lyon’s passive ear model (see transformation from Figure 5(h) to 5(i)) [77]. Then, the cochleagram is cropped to 49 channels × 12p time steps by using a sliding window method [77], followedi by a binarization (see transformation from Figure 5(i) to 5(j)). Next, the pre-processed images and cochleagrams are converted to pulse trains with different polarities: positive pulse trains for images and negative pulse trains for cochleagrams (see Figure 5(g, k)). Each pulse train comprisesc 4 timeframes, with each timeframe containing a +3 V (−3 V) pulse if the corresponding pixel in the image (cochleagram) is valued at 1 or a 0 V pulse otherwise. As a result, each images (cochleagram) is converted into a total of 196 (147) pulse trains. The pulse trains corresponding to the image (cochleagram) are applied to 7 (7) FC-LC series devices in the reservoir, with each device receiving 28 (21) pulse trains. The residual Vout is measured 24 μs after each pulse, but only that after the last pulse is used to constitute the reservoir state.

Figure 5(l, m) show the evolutions of the residual Vout of two typical FC-LC series devices in response to different positive and negative pulse trains, respectively. The final residual Vout values are clearly separated for both pulse polarities, with the degree of separation surpassing most reported values (Figure S19). Such superior separation performance under both pulse polarities is attributed to the device’s nonlinearity, fading memory, and bidirectional operation capability. In addition, similar separation capabilities are evident in other devices in the reservoir, as displayed in Figure S20. These results therefore suggest the great potential of the FC-LC series device-based reservoir to extract both image and speech features.

The reservoir states corresponding to the image and speech inputs are subsequently fed to a (196 + 147 + 1) × 10 readout layer for recognition. Figure 5(n) shows that this multimodal RC system achieves an average recognition accuracy as high as 97.6% during the 10-fold cross-validation. In contrast, control RC systems which use image or speech information alone as inputs achieve apparently lower accuracies of only 87.6% and 86.0%, respectively. These comparative results underscore the efficacy of our FC-LC series devices in multimodal RC, which is facilitated by their bidirectional operation capability.

Besides bidirectional operation, the FC-LC series devices also possess tunable time constants, which can enhance temporal signal processing performance, particularly for tasks involving multiple timescales. We demonstrate this with a Mackey-Glass time-series prediction task. The Mackey-Glass

time series is described by a nonlinear time-delayed differential equation as follows:

![](images/e404579a9c9e5a15e94b0a4e6eee303d38daa4bd3181ee25f87a144393ffd81d.jpg)

![](images/e25700fa2bf42983054d2d422cba7a5d6475f6d953b433b96132e4d9dd4ccfbd.jpg)

![](images/eedef807af9604053b01646f301183808de5121d18d2dd725a8260415b5edd32.jpg)

![](images/57ab339c19ed3f83529e5c656563b0545e8b74756ef2bdcd7d1d4d7aec512311.jpg)

![](images/bf82a64c62c5a9ec17d9cff72e3b913530e48306db2bc34a05e67c358e8b3984.jpg)

![](images/b8735c35a0cb6aecc04d6a4196317d77b1ab96c9d6963d9361766d07470f992e.jpg)

![](images/507f152a2ea3bc27201be1e7cc26c146983c607d2ce1e7465a96fff4cd3071bb.jpg)  
Figure 5. Waveform classification and multimodal digit recognition using bidirectionally operable FC-LC series devices. (a) Input sequence consisting of sine and square waveforms. (b) Comparative waveform classification results: unipolar versus bipolar pulse schemes with ground truth reference. (c) Schematics illustrating the conversions of masked inputs into unipolar and bipolar pulses. (d) NRMSEs obtained with unipolar and bipolar pulse schemes at different mask parameters. (e) Typical handwritten digit image of digit “5” and (f) its corresponding d binarized image. (g) Schematics illustrating the encoding of pre-processed images into positive pulse trains. (h) Typical audio waveform of digit “5”. (i) Original cochleagram corresponding to the audio waveform in (h) and (j) its cropped and binarized version. (k) Schematics illustrating the encoding of pre-processed cochleagrams into negative pulse trains. Residual $V _ { \mathrm { o u t } }$ evolutions of two typical FC-LC series devices in response to (l) positive and (m) negative pulse trains, respectively. (n) Performance comparison between multimodal RC system e and control RC systems using only images or speeches as inputs.

$$
\frac {d y}{d t} = \beta \frac {y (t - \tau)}{1 + y (t - \tau) ^ {n}} - \gamma y (t). \tag {3}
$$

where the system parameters are set to the widely used values of $y ( 0 ) = 1 . 2 , \gamma = 0 . 1 , \beta = 0 . 2 , n = 1 0 .$ , and τ = 17 [49]. As the system becomes chaotic for τ > 16.8, a chaotic y(n) series containing multi-timescale features (Figure S21(a)) is thuse generated. The total length of this series is 1000 time steps, with the first 500 time steps allocated for training and the remaining for test. The objective is to to perform one-stepc ahead prediction, i.e., to predict y(n + 1) based on the known values up to y(n).

To achieve the best prediction, we construct a RC system whose reservoir comprises 5 different FC-LC series devices. The $C _ { \mathrm { L C S } }$ of these devices span from 100 pF to 200 pF, 330 pF, 820 pF, and 2.2 nF, providing the reservoir with a wide range of time constants (Figure 3(f)) for extracting multitimescale features. When the RC system performs the prediction, each input y(n) is first linearly transformed into a pulse voltage in the range of 1 to 3 V (pulse width: 0.15 ms), which is then applied to each FC-LC series device in the reservoir. The residual $V _ { \mathrm { o u t } }$ values (24 μs after the pulse) of the 5 devices at the time steps $n - 5 , n - 4 , . . . ,$ and n (totaling 30 virtual nodes), combined with a bias, are fed into a $3 1 \times 1$ readout layer to predict y(n + 1). As illustrated in Figure 6(a,

b), the predicted y(n) series matches well with its corresponding ground truth during the test, resulting in a small NRMSE of only 0.045.

![](images/0bb0b5d108943e5cf45f7d57ebaf58507880f9a85e223da93a3ae2e671a88b75.jpg)

![](images/9476e3c523951e1ca878cbddcf3d6c17085a8b0b98d3050a5acfe89d47fb3856.jpg)

![](images/57e21fcb2290fe605f0fc4f12e01b3622f8a0762225497ebf85d798a7933ffb3.jpg)

![](images/2728254c3a113b5d68f417d0ad979d9d8977e4f525ad3185771bb5144fad29e3.jpg)  
Figure 6. Mackey-Glass time-series prediction using FC-LC series devices with varying time constants. (a, c, e) Predicted Mackey-Glass time series versus its ground truth obtained from RC systems with different device configurations: (a) 5 different devices with $C _ { \mathrm { { L C S } } }$ of 100 pF, 200 pF, 330 pF, 820 pF, and 2.2 nF, (c) 5 nominally identical devices with $C _ { \mathrm { L C } }$ of 100 pF, and (e) 5 nominally identical devices with $C _ { \mathrm { L C } }$ of 2.2 nF. (b, d, f) 2D plots of the results in (a), (c), and (e), respectively. (g) Performance comparison between the hybrid-device system and d control systems with nominally identical devices. (h) Normalized standard deviations of the major FFT spectral peaks for reservoir states of the hybrid-device system and control systems with nominally identical devices.

Conversely, replacing the hybrid devices in the reservoir by nominally identical devices leads to noticeable deviations e between the predicted $y ( n )$ series and the ground truth, accompanied by a larger NRMSE, as shown in Figure 6(c-f)t and Figure S22. To elucidate the reason behind the performance enhancement with the hybrid-device system, fast Fourier transformation (FFT) is utilized to analyze the reservoir states (see Figure S23). It is revealed from Figure 6(h) that the RC system with hybrid devices exhibits the largest deviations in the major peaks of the FFT spectra. This e indicates that the hybrid-device system is particularly adept at capturing diverse temporal dynamics across different timescales, accounting for its superior performance in the Mackey-Glass time-series prediction.

Notably, the performance of the hybrid-device system canc be further enhanced through external timescale tailoring. As

demonstrated in Figure S24, the NRMSE is reduced by introducing appropriate input and output delays. Therefore, combining the hybrid-device system with time-multiplexing approaches [3–5] to achieve optimal performance is a promising direction for future investigation.

# 3. Conclusion

In summary, this study demonstrates the FC-LC series device as an advanced reservoir device for implementing RC. This device operates through charge accumulation and relaxation, which are associated with nonlinear polarization switching and back-switching in the FC, respectively. This unique mechanism equips the device with nonlinearity and fading memory, essential properties of a reservoir, as well as direct voltage readout. Moreover, the device boasts bidirectional operation capability, widely tunable time

constants (from ~0.01 to ~3 ms), and ultralow power consumption (~1.3 μW per input). The combination of these advantages makes the FC-LC series device stand out from existing reservoir devices (Figure 3(g)).

Building upon these FC-LC series devices, a ferroelectric capacitive RC system is developed, which demonstrates exceptional performance in benchmark tasks including arrhythmic heartbeat detection and Hénon map prediction. Furthermore, by exploiting the bidirectional operation of the FC-LC series devices, the RC system not only achieves enhanced performance in waveform classification (NRMSE = 0.04) but also accomplishes multimodal digit recognition with 97.6% accuracy. Through strategically hybridizing the FC-LC series devices with varying time constants, the RC system achieves outstanding performance in Mackey-Glass timeseries prediction (NRMSE = 0.045). These results showcase the great promise of ferroelectric capacitive devices for constructing power-efficient, dynamic-rich RC systems capable of handling diverse temporal tasks.

It is worth noting that the FC-LC series device has remarkable potential for compact implementation by leveraging established ferroelectric memory fabrication technologies. Specifically, the PZT-based FC has already been available at the 130 nm node [78], while the switch S0 and the LC (Figure 2(a)) can be realized by using a transistor and a SiO2 (or alternative dielectrics)-based capacitor, respectively. Therefore, large-scale on-chip integration of FC-LC series devices for constructing a compact RC system is quite promising. We also emphasize that the device concept demonstrated in this work can be extended to other ferroelectrics. For example, HfO2-based ferroelectrics, which feature high CMOS compatibility and scalability, can be utilized to develop the FCs. This will likely inspire ongoing research efforts to further develop ferroelectric capacitive devices for practical RC applications.

# 4. Experimental Section

Device fabrication: PZT epitaxial thin films (~120 nm) buffered by SRO bottom electrode layers (~40 nm) were e epitaxially grown on (001)-oriented SrTiO3 (STO) singlecrystalline substrates via pulsed laser deposition (PLD) using t a KrF excimer laser source (λ = 248 nm). The laser energy fluences for depositing PZT and SRO films were 0.90 and 0.97 J/cm2, respectively, while maintaining a consistent repetition p rate of 5 Hz. The SRO films were first deposited at a substrate temperature of 680 °C under an oxygen pressure of 15 Pa. The PZT films were subsequently deposited at a lower temperaturee of 620 °C, while keeping the oxygen pressure unchanged. After deposition, the PZT/SRO films were cooled at a rate of 10 °C/min to room temperature in an oxygen atmosphere of c 1000 Pa. Then, circular Pt top electrodes (diameter: ~100 m) were ex situ deposited on the films through a shadow mask by sputtering under vacuum, resulting in the formation of

Pt/PZT/SRO FCs. Each FC was connected in series with an LC (commercial 0805 surface-mount capacitor) to function as a reservoir device.

Structural, morphological, and domain characterizations: The phases and crystalline structures of the PZT films were investigated by X-ray diffraction (XRD) -2 scan and reciprocal space mapping, utilizing a PANalytical X’Pert PRO diffractometer. The morphologies and domains were characterized by atomic force microscopy (AFM) and p piezoresponse force microscopy (PFM), respectively, i performed on an Asylum Research Cypher scanning probe microscope equipped with Pt-coated silicon tips (Nanoworld EFM Arrow). The PFM images and hysteresis loops were obtained by applying an AC driving voltage of 0.8 V in the dual a.c. resonance tracking (DART) mode.c

Electrical measurements: The P–V hysteresis loops of the FCs were measured using a ferroelectric tester (Radiant Precision Multiferroic). The leakage currents were measured with a Keithley 6430 SourceMeter. Electrical measurements on the FC-LC series devices were conducted utilizing a customized test board with circuit connections as illustrated in Figure 2(a). The switch S0 within the circuit was implemented using a TMUX6119DCNR analog switch. Pulses applied to the FC-LC series devices were supplied by multi-channel 16- bit digital-to-analog converters (DACs) controlled by a STM32 microcontroller unit (MCU) in communication with a personal computer (PC). The resulting Vouts were recorded using either a LeCory 64Xi-A oscilloscope or multi-channel 16-bit analog-to-digital converters (ADCs). In the arrhythmic heartbeat detection task, the readout layer was physically implemented using adjustable resistors, while in all other tasks, the readout layers were implemented by simulation.

Simulations: For the arrhythmic heartbeat detection task, the reservoir state generated by the FC-LC series devices was applied to the readout layer consisting of adjustable resistors, producing a summed current. This current was converted into the final neuronal output via a sigmoid activation function as expressed by

$$
\hat {y} _ {i} = \operatorname {s i g m o i d} \left(x _ {i}\right) = \frac {1}{1 + e ^ {- x _ {i}}}. \tag {4}
$$

where x is the neuronal input scaled from the summed current I:

$$
x = \alpha (I - \beta). \tag {5}
$$

where α is a scaling factor and β is an offset. The readout layer was trained using regularized logistic regression, with the cost function (J) defined as

$$
J = \frac {1}{m} \sum_ {i = 1} ^ {m} \left[ - y _ {i} \log \left(\hat {y} _ {i}\right) - \left(1 - y _ {i}\right) \log \left(1 - \hat {y} _ {i}\right) \right] + \lambda \sum_ {j = 1} ^ {n} \left| w _ {j} \right|. \tag {6}
$$

where m is the number of samples, yi is the desired target, wj is the weight, n represents the number of weights, and λ is the regularization parameter. The logistic regression was used

because this task is a binary classification task (healthy vs. arrhythmic).

For the multimodal digit recognition task, the original outputs of the readout layer were fed into a softmax function to obtain categorical probabilities, as expressed as:

$$
\hat {y} _ {i} = \operatorname {s o f t m a x} \left(z _ {i}\right) = \frac {e ^ {z _ {i}}}{\sum_ {j = 1} ^ {N} e ^ {z _ {j}}}. \tag {7}
$$

where $z _ { i }$ is the original output of the i-th output neuron, $\hat { y } _ { i }$ is the probability corresponding to $z _ { i } ,$ and N is the total number of output neurons (or categories). The readout layer was trained via softmax regression using the categorical crossentropy cost function (L) given by

$$
L = - \sum_ {i = 1} ^ {m} y _ {i} \log \left(\hat {y} _ {i}\right), \tag {8}
$$

For the Hénon map prediction, waveform classification, and Mackey-Glass time-series prediction tasks, linear regression was employed to train the readout layer. Following this method, the weight matrix of the readout layer W was directly calculated as

$$
\mathbf {W} = \left(\mathbf {X} ^ {\mathrm {T}} \mathbf {Y}\right) ^ {- 1} \mathbf {X} ^ {\mathrm {T}} \mathbf {Y}, \tag {9}
$$

where X is the input matrix, and Y is the target matrix.

Prediction performance was evaluated by using the NRMSE as the primary metric, which is defined as:

$$
\mathrm {N R M S E} = \sqrt {\frac {\frac {1}{m} \sum_ {i = 1} ^ {m} \left(y _ {i} - \hat {y} _ {i}\right) ^ {2}}{\sigma_ {y} ^ {2}}} \tag {10}
$$

where yi and ŷi are the target and predicted outputs at time step $i ,$ m is the number of samples considered, ${ \sigma _ { y } } ^ { 2 }$ is the variance of the target outputs.

# Acknowledgements

The authors would like to thank the National Key Researchd and Development Programs of China (Grant No. 2022YFB3807603), National Natural Science Foundation of China (Grant Nos. 92163210 and 52172143), Science and e Technology Projects in Guangzhou (Grant Nos. 202201000008 and 2022A04J00031), Guangdong Natural t Science Funds for Distinguished Young Scholar (Grant No. 2024B1515020053), and Guangdong Provincial Key Laboratory of Optical Information Materials and Technology (Grant No. 2023B1212060065).

# ORCID iDs

Linyuan Mo https://orcid.org/0009-0007-7692-1227 Zhen Fan https://orcid.org/0000-0002-1756-641Xc

# Data availability statement

The data that support the findings of this study are available upon reasonable request from the authors.

# References

[1] Moon J, Ma W, and Shin J H 2019 Temporal data classification and forecasting using a memristor-based reservoir computing system Nat. Electron. 2 480–7   
[2] Lukoševičius M and Jaeger H 2009 Reservoir computing approaches to recurrent neural network training Comput. Sci.p Rev. 3 127–49   
[3] Dong H, Jaurigue L and Lüdge K 2025 Time‐Multiplexedi Reservoir Computing with Quantum‐Dot Lasers: Impact of Charge‐Carrier Scattering Timescale Phys. Status Solidi RRL– Rapid Res. Lett. 19 2400433   
[4] Jaurigue L and Lüdge K 2024 Reducing reservoir computer hyperparameter dependence by external timescale tailoring Neuromorphic Comput. Eng. 4 014001   
[5] Kuriki Y, Nakayama J, and Takano K A 2018 Impact of input mask signals on delay-based photonic reservoir computing with semiconductor lasers Opt. Express 26 5777–88s   
[6] Appeltant L, Soriano M C, and Van der Sande G 2011 Information processing using a single dynamical node as complex system Nat. Commun. 2 468u   
[7] Dion G, Mejaouri S and Sylvestre J 2018 Reservoir computing with a single delay-coupled non-linear mechanical oscillator J. Appl. Phys. 124 152132   
[8] Usami Y, van de Ven B, and Mathew D G 2021 In‐materion reservoir computing in a sulfonated polyaniline network Adv. Mater. 33 2102688   
[9] Zhong Y, Tang J, and Li X 2021 Dynamic memristor-based a reservoir computing for high-efficiency temporal signal processing Nat. Commun. 12 408   
[10] Milano G, Pedretti G, and Montano K 2022 In materia reservoir computing with a fully memristive architecture based on self-organizing nanowire networks Nat. Mater. 21 195–202   
[11] Tanaka G, Yamane T, and Héroux J B 2019 Recent advances in physical reservoir computing: A review Neural Netw. 115 100–23   
[12] Tang J, Yuan F, and Shen X 2019 Bridging Biological and Artificial Neural Networks with Emerging Neuromorphic Devices: Fundamentals, Progress, and Challenges Adv. Mater. 31 1902761   
[13] Zhang H-T, Park T J, and Islam A N 2022 Reconfigurable perovskite nickelate electronics for artificial intelligence Science 375 533–9   
[14] Cucchi M, Gruener C, and Petrauskas L 2021 Reservoir computing with biocompatible organic electrochemical networks for brain-inspired biosignal classification Sci. Adv. 7 eabh0693   
[15] Liu K, Dang B, and Zhang T 2022 Multilayer Reservoir Computing Based on Ferroelectric α‐In2Se3 for Hierarchical Information Processing Adv. Mater. 34 2108826   
[16] Liang X, Tang J, and Zhong Y 2024 Physical reservoir computing with emerging electronics Nat. Electron. 7 193– 206   
[17] Midya R, Wang Z, and Asapu S 2019 Reservoir Computing Using Diffusive Memristors Adv. Intell. Syst. 1 1900084   
[18] Wlaźlak E, Zawal P and Szaciłowski K 2020 Neuromorphic Applications of a Multivalued [SnI4{(C6H5)2SO}2] Memristor Incorporated in the Echo State Machine ACS Appl. Electron. Mater. 2 329–38

[19] Sun L, Wang Z, and Jiang J 2021 In-sensor reservoir computing for language learning via two-dimensional memristors Sci. Adv. 7 eabg1455   
[20] Cao J, Zhang X, and Cheng H 2022 Emerging dynamic memristors for neuromorphic reservoir computing Nanoscale 14 289–98   
[21] Hu W, Fan Z, and Mo L 2025 Volatile Resistive Switching and Short-Term Synaptic Plasticity in a Ferroelectric-Modulated SrFeOx Memristor ACS Appl. Mater. Interfaces 17 9595–605   
[22] Chen Z, Li W, and Fan Z 2023 All-ferroelectric implementation of reservoir computing Nat. Commun. 14 3585   
[23] Toprasertpong K, Nako E, and Wang Z 2022 Reservoir computing on a silicon platform with a ferroelectric fieldeffect transistor Commun. Eng. 1 21   
[24] Li L, Xiang H, and Zheng H 2024 Physical reservoirs based on MoS2–HZO integrated ferroelectric field-effect transistors for reservoir computing systems Nanoscale Horiz. 9 752–63   
[25] Lee S, Kim D and Kim S 2024 Volatile memory characteristics of CMOS-compatible HZO ferroelectric layer for reservoir computing Ceram. Int. 50 36495–502   
[26] Kim D, Kim J, and Yun S 2023 Ferroelectric synaptic devices based on CMOS-compatible HfAlOx for neuromorphic and reservoir computing applications Nanoscale 15 8366–76   
[27] Ju D, Noh M, and Kim G 2024 Reservoir Computing System with Diverse Input Patterns in HfAlO-Based Ferroelectric Memristor ACS Appl. Mater. Interfaces 16 66250–61   
[28] Everschor-Sitte K, Majumdar A, and Wolk K 2024 Topological magnetic and ferroelectric systems for reservoir computing Nat. Rev. Phys. 6 455–62   
[29] Duong N T, Chien Y-C, and Xiang H 2023 Dynamic Ferroelectric Transistor‐Based Reservoir Computing for Spatiotemporal Information Processing Adv. Intell. Syst. 5 2300009   
[30] Meier D and Selbach S M 2022 Ferroelectric domain walls for nanotechnology Nat. Rev. Mater. 7 157–73   
[31] Covi E, Mulaosmanovic H, and Max B 2022 Ferroelectricbased synapses and neurons for neuromorphic computing Neuromorphic Comput. Eng. 2 012002   
[32] Kim J, Park E C, and Shin W 2024 Analog reservoir computing via ferroelectric mixed phase boundary transistors Nat. Commun. 15 9147   
[33] Allwood D A, Ellis M O, and Griffin D 2023 A perspective d on physical reservoir computing with nanomagnetic devices Appl. Phys. Lett. 122   
[34] Dawidek R W, Hayward T J, and Vidamour I T 2021 Dynamically driven emergence in a nanomagnetic system Adv. Funct. Mater. 31 2008389   
[35] Gartside J C, Stenning K D, and Vanstone A 2022 Reconfigurable training and reservoir computing in ant artificial spin-vortex ice via spin-wave fingerprinting Nat. Nanotechnol. 17 460–9   
[36] Nakane R, Tanaka G and Hirose A 2018 Reservoir computing with spin waves excited in a garnet film IEEE Access 6 4462–p 9   
[37] Torrejon J, Riou M, and Araujo F A 2017 Neuromorphic computing with nanoscale spintronic oscillators Nature 547 428–31   
[38] Kan S, Nakajima K, and Asai T 2022 Physical Implementation of Reservoir Computing throughc Electrochemical Reaction Adv. Sci. 9 2104076   
[39] Yin Y, Wang S, and Weng R 2025 A Dual‐Modal Memory Organic Electrochemical Transistor Implementation forc Reservoir Computing Small Sci. 5 2400415

[40] Wang S, Chen X, and Zhao C 2023 An organic electrochemical transistor for multi-modal sensing, memory and processing Nat. Electron. 6 281–91   
[41] Du C, Cai F, and Zidan M A 2017 Reservoir computing using dynamic memristors for temporal information processing Nat. Commun. 8 2204   
[42] Zhu X, Wang Q and Lu W D 2020 Memristor networks for real-time neural activity analysis Nat. Commun. 11 2439   
[43] Jiang W, Chen L, and Zhou K 2019 Physical reservoir computing using magnetic skyrmion memristor and spin torque nano-oscillator Appl. Phys. Lett. 115   
[44] Pei M, Zhu Y, and Liu S 2023 Power‐Efficient Multisensory i Reservoir Computing Based on Zr‐Doped HfO2 Memcapacitive Synapse Arrays Adv. Mater. 35 2305609   
[45] Zhong Y, Tang J, and Li X 2022 A memristor-based analoguer reservoir computing system for real-time and power-efficient signal processing Nat. Electron. 5 672–81   
[46] Lee J-K, Kwon O, and Jeon B 2023 Reservoir Computing for c Temporal Data Processing Using Resistive Switching Memory Devices Based on ITO Treated With O2 Plasma IEEE Trans. Electron Devices 70 5651–6s   
[47] Park S-O, Jeong H, and Park J 2022 Experimental demonstration of highly reliable dynamic memristor for artificial neuron and neuromorphic computing Nat. Commun. 13 2888   
[48] Tang M, Zhan X, and Wu S 2022 A compact fully ferroelectric-FETs reservoir computing network with sub-100 ns operating speed IEEE Electron Device Lett. 43 1555–8n   
[49] Ma Z, Yi H, and Zheng Z 2025 Versatile and Robust Reservoir Computing with PWM‐Driven Heterogenous R-C Circuits Adv. Sci. 12 e16413   
[50] Hosoda N, Komatsu H and Ikuno T 2025 Synaptic behavior a in dye-sensitized solar cell-based optoelectronic artificial synaptic devices towards self-powered physical reservoir computing Jpn. J. Appl. Phys. 64 017001   
[51] Komatsu H, Hosoda N, and Kounoue T 2024 Disposable and Flexible Paper-Based Optoelectronic Synaptic Devices for Physical Reservoir Computing Adv. Electron. Mater. 10 2300749   
[52] Nie F, Fang H, and Wang J 2025 An Adaptive Solid‐State Synapse with Bi‐Directional Relaxation for Multimodal Recognition and Spatio‐Temporal Learning Adv. Mater. 37 2412006   
[53] Liu K, Zhang T, and Dang B 2022 An optoelectronic synapse based on α-In2Se3 with controllable temporal dynamics for multimode and multiscale reservoir computing Nat. Electron. 5 761–73   
[54] Armendarez N X, Mohamed A S, and Dhungel A 2024 Brain-Inspired Reservoir Computing Using Memristors with Tunable Dynamics and Short-Term Plasticity ACS Appl. Mater. Interfaces 16 6176–88   
[55] Chen R, Yang H, and Li R 2024 Thin-film transistor for temporal self-adaptive reservoir computing with closed-loop architecture Sci. Adv. 10 eadl1299   
[56] Jang Y H, Kim W, and Kim J 2021 Time-varying data processing with nonvolatile memristor-based temporal kernel Nat. Commun. 12 5727   
[57] Demasius K-U, Kirschen A and Parkin S 2021 Energyefficient memcapacitor devices for neuromorphic computing Nat. Electron. 4 748–56   
[58] Singh A, Choi S, and Wang G 2025 Analysis and fully memristor-based reservoir computing for temporal data classification Neural Netw. 182 106925

[59] Ghenzi N, Park T W, and Kim S S 2024 Heterogeneous reservoir computing in second-order Ta2O5/HfO2 memristors Nanoscale Horiz. 9 427–37   
[60] Choi S, Shin J, and Park G 2024 3D-integrated multilayered physical reservoir array for learning and forecasting timeseries information Nat. Commun. 15 2044   
[61] Yu J, Li Y, and Sun W 2021 Energy efficient and robust reservoir computing system using ultrathin (3.5 nm) ferroelectric tunneling junctions for temporal data learning 2021 Symposium on VLSI Technology (IEEE) pp. 1–2   
[62] Zhang P, Ma X, and Dong Y 2023 An energy efficient reservoir computing system based on HZO memcapacitive devices Appl. Phys. Lett. 123   
[63] Takagi S, Toprasertpong K, and Nako E 2023 Reservoir computing utilizing ferroelectric-gate-insulator FETs and capacitors 2023 International Conference on IC Design and Technology (ICICDT) (IEEE) pp. 25–8   
[64] Park S-O, Jeong H, and Park J 2022 Experimental demonstration of highly reliable dynamic memristor for artificial neuron and neuromorphic computing Nat. Commun. 13 2888   
[65] Ryu D, Park S, and Kim S 2025 Physical reservoir computing system fully implemented using a single flash memory device via tailored decay pulse modulation Nano Energy 146 111525   
[66] Duong N T, Chien Y-C, and Xiang H 2023 Dynamic Ferroelectric Transistor‐Based Reservoir Computing for Spatiotemporal Information Processing Adv. Intell. Syst. 5 2300009   
[67] Eom C B, Van Dover R B, and Phillips J M 1993 Fabrication and properties of epitaxial ferroelectric heterostructures with (SrRuO3) isotropic metallic oxide electrodes Appl. Phys. Lett. 63 2570–2   
[68] Shim S K, Jang Y H, and Han J 2024 2Memristor‐1Capacitor Integrated Temporal Kernel for High‐Dimensional Data Mapping Small 20 2306585   
[69] Shim S K, Lee K, and Han J 2024 Thresholding Computing with Heterogeneous Integration of Memristive Kernel with Metal‐Oxide‐Semiconductor Capacitor for Temporal Data Analysis Adv. Mater. 36 2410432   
[70] Shim S K, Han J-K, and Han J 2025 Advanced Time Series Data Processing Using Various Memristor‐Integrated Devices Adv. Mater. Technol. e00838   
[71] Sun W, Zhang W, and Yu J 2022 3D reservoir computing d with high area efficiency (5.12 tops/mm2) implemented by 3D dynamic memristor array for temporal signal processing 2022 IEEE Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits) (IEEE) pp. 222–3   
[72] Li Z and Yu X 2024 Exploring non-steady-state charge transport dynamics in information processing: insights from reservoir computing Neuromorphic Comput. Eng. 4 024014t   
[73] Liu Z, Zhang Q, and Xie D 2023 Interface-type tunable oxygen ion dynamics for physical reservoir computing Nat. Commun. 14 7176   
[74] Moody G B and Mark R G 2001 The impact of the MIT-BIH p Arrhythmia Database IEEE Eng. Med. Biol. Mag. 20 45–50   
[75] Kuriki Y, Nakayama J, and Takano K 2018 Impact of input mask signals on delay-based photonic reservoir computing with semiconductor lasers Opt. Express 26 5777–88   
[76] Appeltant L, Van der Sande G, and Danckaert J 2014 Constructing optimized binary masks for reservoir computingc with delay systems Sci. Rep. 4 3629   
[77] Rabiner L and Juang B-H 1993 Fundamentals of speech recognition (Prentice-Hall, Inc.)c

[78] McAdams H P, Acklin R, and Blake T 2004 A 64-Mb embedded FRAM utilizing a 130-nm 5LM Cu/FSG logic process IEEE J. Solid-State Circuits 39 667–77