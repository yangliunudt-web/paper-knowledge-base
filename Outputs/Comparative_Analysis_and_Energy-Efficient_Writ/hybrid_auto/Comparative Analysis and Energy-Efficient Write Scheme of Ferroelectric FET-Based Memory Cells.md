---
title: "Comparative Analysis and Energy-Efficient Write Scheme of Ferroelectric FET-Based"
authors:
  - "Dong-Hyun Ko"
  - "Tae-Woong Oh"
  - "Seong-Ook Lim"
  - "Jong-Hyun Ko"
  - "Se-Hyeon Kang"
date: "2021-09-10"
year: "2021"
journal: "IEEE Access"
doi: "10.1109/ACCESS.2021.3111913"
abstract: "The ferroelectric field-effect transistor (FeFET) is one of the most promising candidates for emerging nonvolatile memory devices owing to its low write energy and high ION/IOFF ratio. For FeFET applications as nonvolatile memory devices, 1FeFET, 1T-1FeFET, 2T-1FeFET, and 3T-1FeFET cells have been proposed. The 1FeFET cell exhibits the highest density but suffers from write disturbance. Although the 1T-1FeFET and 2T-1FeFET cells resolve the write disturbance, they use a write scheme with a negative write voltage (VW), which requires voltage swings of many control signals, leading to significantly high write energy consumption. The 3T-1FeFET cell uses a write scheme without a negative VW but exhibits the largest area overhead. In this paper, to significantly reduce the write energy consumption, we propose a less control signal swing (LCSS) write scheme without using a negative VW. Simulation results indicate that the worst, average, and best cases of the proposed LCSS write scheme can achieve 35%, 66%, and 96% lower write energy consumption, respectively, than the write scheme with a negative VW in the 1T-1FeFET cell. We also identify the available sensing schemes for each FeFET cell in the read operation according to the FeFET threshold voltage distribution."
abstract_cn: "铁电场效应晶体管因其低写入能量和高ION/IOFF比而成为新兴非易失性存储器件中最有希望的候选者之一。对于FeFET作为非易失性存储器件的应用，已提出了1FeFET、1T-1FeFET、2T-1FeFET和3T-1FeFET单元。1FeFET单元具有最高密度但受到写入干扰的影响。虽然1T-1FeFET和2T-1FeFET单元解决了写入干扰问题，但它们使用带有负写入电压的写入方案，这需要许多控制信号的电压摆动，导致极高的写入能量消耗。3T-1FeFET单元使用无负写入电压的写入方案，但具有最大的面积开销。虽然1T-1FeFET单元以较小的面积开销解决了写入干扰问题，但由于使用负写入电压，其写入能量消耗较高。本文为了显著降低写入能量消耗，提出了一种无负写入电压的低控制信号摆动写入方案。仿真结果表明，所提出的低控制信号摆动写入方案在最坏、平均和最好情况下，相比1T-1FeFET单元中使用负写入电压的写入方案，可分别实现35%、66%和96%的写入能量降低。我们还根据FeFET阈值电压分布确定了每种FeFET单元在读取操作中可用的传感方案。"
keywords:
  - "[[FeFET]]"
cite: "[1] Ko D H, Oh T W, Lim S, et al. Comparative analysis and energy‑efficient"
aiSum: "FeFET存储单元比较与低控制信号摆动写入方案：分析1FeFET/1T-1FeFET/2T-1FeFET/3T-1FeFET单元特性，提出LCSS写入方案，在最坏/平均/最好情况下分别降低35%/66%/96%写入能量。"
confidence: "medium"
wiki_concepts:
  - "[[FeFET]]"
---

Received August 2, 2021, accepted September 8, 2021, date of publication September 10, 2021, date of current version September 21, 2021.

Digital Object Identifier 10.1109/ACCESS.2021.3111913

# Comparative Analysis and Energy-Efficient Write Scheme of Ferroelectric FET-Based Memory Cells

DONG HAN KO , (Graduate Student Member, IEEE), TAE WOO OH , (Graduate Student Member, IEEE), SEHEE LIM , (Graduate Student Member, IEEE), SE KEON KIM 9 (Graduate Student Member, IEEE), AND SEONG-OOK JUNG , (Senior Member, IEEE)

School of Electrical and Electronic Engineering, Yonsei University, Seoul 03722, South Korea

Corresponding author: Seong-Ook Jung (sjung@yonsei.ac.kr)

This work was supported by the Research Foundation of Korea (NRF) under Grant 2020M3F3A2A01081918.

ABSTRACT The ferroelectric field-effect transistor (FeFET) is one of the most promising candidates for emerging nonvolatile memory devices owing to its low write energy and high ION/IOFF ratio. For FeFET applications as nonvolatile memory devices, 1FeFET, 1T-1FeFET, 2T-1FeFET, and 3T-1FeFET cells have been proposed. The 1FeFET cell exhibits the highest density but suffers from write disturbance. Although the 1T-1FeFET and 2T-1FeFET cells resolve the write disturbance, they use a write scheme with a negative write voltage (VW), which requires voltage swings of many control signals, leading to a significantly high write energy consumption. The 3T-1FeFET cell uses a write scheme without a negative VW; however, it exhibits the largest area overhead. Although the 1T-1FeFET cell resolves the write disturbance with a small area overhead; however, it exhibits high write energy consumption because of the use of a negative VW. In this paper, to significantly reduce the write energy consumption, we propose a less control signal swing (LCSS) write scheme without using a negative VW. Simulation results indicate that the worst, average, and best cases of the proposed LCSS write scheme can achieve 35%, 66%, and 96% lower write energy consumption, respectively, than the write scheme with a negative VW in the 1T-1FeFET cell. We also identify the available sensing schemes for each FeFET cell in the read operation according to the FeFET threshold voltage distribution.   
INDEX TERMS Control signal swing, ferroelectric field-effect transistor, hysteresis, nonvolatile memory, write disturbance.

# I. INTRODUCTION

In the past decades, static and dynamic random-access memory (SRAM and DRAM, respectively) have been conventionally used as cache and main memory, respectively. The technology has been scaled down to satisfy the demand for a high memory density, a high speed, and low power dissipation [1], [2]. However, process variation makes technology scaling difficult [3]–[9]. Moreover, technology scaling causes a high leakage power in SRAM and DRAM [10], [11].

To overcome these limitations, researchers have developed emerging nonvolatile memory devices that have zero-leakage power, high-density, and high-scalability characteristics. Because of these characteristics, emerging

The associate editor coordinating the review of this manuscript and D approving it for publication was Muhammad Zakarya

nonvolatile devices are suitable for use as Internet of Things devices and in data-intensive applications such as edge computing and artificial-intelligence hardware devices.

In this context, nonvolatile memory devices such as phase-change memory (PCM), spin-transfer torque magnetic random-access memory (STT-RAM), and resistive randomaccess memory (ReRAM) have been studied. However, these memory devices face the following challenges. Because they use a current-based write scheme, a high write current flows during the write operation, which causes high write energy consumption [12]. Additionally, they have a low ION/IOFF ratio, which causes a low read sensing margin [13]–[15]. The ferroelectric field-effect transistor (FeFET), which is a promising emerging nonvolatile memory device, can overcome these challenges. First, because the ferroelectric (FE) layer polarization is switched by the gate-to-source

voltage $( V _ { \mathrm { G S } } )$ , a write current rarely flows during the write operation [16]. Most of the write energy is consumed by charge trapping and capacitor charging [17], [18]. Moreover, the FE layer in an FeFET has a fast switching time [19]. Therefore, the FeFET exhibits a low write energy consumption. Second, the FeFET has a high ION/IOFF ratio [19], [20], leading to a high read-sensing margin.

To use the FeFET as a nonvolatile memory device, various FeFET cell structures have been proposed: 1FeFET [21], 1T-1FeFET [22], 2T-1FeFET [23], and 3T-1FeFET [24]. Each structure has advantages and limitations. The 1FeFET cell exhibits the highest density. However, it suffers from write disturbance in the array structure owing to the absence of an access transistor. To alleviate the write disturbance, the write voltage (VW)/2 and VW/3 inhibition bias (IB) schemes were proposed in [21], [25]; however, they still have the probability of write disturbance. In the 1T-1FeFET cell, one access transistor is added to the gate of the FeFET. This transistor allows selected and unselected rows to be distinguished; thus, the write disturbance problem can be solved. In the 2T-1FeFET cell, an additional access transistor is added at the drain of the FeFET. Thus, the 2T-1FeFET cell can read by selecting bits during the read operation. Moreover, the 1T-1FeFET and 2T-1FeFET cells use a write scheme with a negative write voltage $( V _ { \mathrm { { W } } } )$ . This causes increased control signal swing to prevent write disturbance in unselected rows. Thus, this write scheme exhibits a higher write energy consumption than the write scheme without a negative $V _ { \mathrm { { W } } }$ . Additionally, in the 1FeFET, 1T-1FeFET, and 2T-1FeFET cells, the available sensing scheme varies according to the FeFET threshold voltage $( V _ { \mathrm { T H } } )$ distribution because there is no access transistor at the FeFET source to block the sneakcurrent path. In the 3T-1FeFET cell, an additional access transistor is added at the source of the FeFET. Because the 3T-1FeFET cell uses a write scheme without a negative $V _ { \mathrm { { W } } }$ , it exhibits a lower write energy consumption. Furthermore, both current- and voltage-based sensing schemes can be used regardless of the $V _ { \mathrm { T H } }$ distribution. However, because three access transistors are used, the 3T-1FeFET cell exhibits the largest area overhead.

In this study, we comprehensively analyzed previous FeFET memory cells in terms of area, write scheme, and sensing scheme. Among these, the analyzed 1T-1FeFET cell not only solves the write disturbance problem but also exhibits a small area overhead. However, it also exhibits a high write energy consumption because it uses a negative $V _ { \mathrm { { W } } }$ . To reduce the write energy consumption of the 1T-1FeFET cell, we propose a less control signal swing (LCSS) write scheme without using a negative VW. Additionally, we analyzed the available sensing schemes in array structures according to $V _ { \mathrm { T H } }$ distribution in the FeFET.

The remainder of this paper is organized as follows. The FeFET device characteristics, write and sensing schemes, and simulation model are introduced in Section II. Previous FeFET memory cells are reviewed in Section III. The characteristics and operation of the proposed LCSS write scheme

![](images/1574a6ea70ae3c15c8dd1f7520c546731c63f0f221e1109e1c030aab43935aab.jpg)  
(a)

![](images/4a87cc9f9c8555249750b2dc515c71581ea7a9727eab20ca0a871b6dd73673ed.jpg)  
(b)   
FIGURE 1. FeFET (a) structure and (b) equivalent circuit.

are presented in Section IV, along with an analysis of the available sensing schemes based on the $V _ { \mathrm { T H } }$ distribution in the FeFET. Previous FeFET memory cells are comprehensively analyzed in Section ${ \mathrm { V } } ;$ additionally, in this section, the proposed LCSS write scheme is compared with previous write schemes. Finally, Section VI concludes the paper.

# II. BACKGROUND

# A. FeFET STRUCTURE AND CHARACTERISTICS

The FeFET structure is similar to that of a metal–oxide– semiconductor field-effect transistor (MOSFET). The difference is that in an FeFET, an FE layer is added between the gate metal and dielectric layer, as shown in Fig. 1(a). Additionally, the FeFET equivalent circuit structure has an FE-layer capacitance $( C _ { \mathrm { F E } } )$ coupled with a MOSFET capacitance (CMOS), as illustrated in Fig. 1(b). Because of the coupled capacitance (C and C ), an FeFET can be used as a nonvolatile memory device that exhibits hysteresis behavior based on the $V _ { \mathrm { G S } }$ with a sufficient FE-layer thickness [20], [26]–[28]. The FeFET $V _ { \mathrm { T H } }$ depends on its polarization state, which can be either the high $V _ { \mathrm { T H } }$ (HVT) state corresponding to logic $\cdot \circ '$ or the low V (LVT) state corresponding to logic ‘‘1.’’ When a positive $V _ { \mathrm { G S } }$ is applied to the FeFET, the polarization direction points to the channel. This causes electrons in the substrate to form a channel, which reduces the $V _ { \mathrm { T H } }$ . Conversely, when a negative $V _ { \mathrm { G S } }$ is applied to the FeFET, the polarization direction points to the gate metal. This prohibits the electrons in the substrate from forming a channel, which increases the $V _ { \mathrm { T H } }$ .

# B. FeFET WRITE AND SENSING SCHEMES

Based on the use of a negative voltage source, the FeFET write scheme can be divided into write schemes with and without a negative $V _ { \mathrm { { W } } }$ [20], [24]. In the write scheme with a negative $V _ { \mathrm { { W } } }$ , the source of the FeFET is driven to ground (GND), and its gate is driven to a positive or negative $V _ { \mathrm { { W } } } ,$ as shown in Fig. 2(a). In the write scheme without a negative $V _ { \mathrm { { W } } }$ , the write data ‘‘1’’ operation is the same as that for the write scheme with a negative $V _ { \mathrm { { W } } }$ . When writing the data $\cdot \circ '$ the source of the FeFET is driven to the positive $V _ { \mathrm { { W } } }$ , and the gate is driven to GND to apply a negative $V _ { \mathrm { G S } }$ without a negative $V _ { \mathrm { { W } } } .$ , as shown in Fig. 2(b).

The FeFET sensing schemes are illustrated in Fig. 3. The gate of the FeFET is driven to the gate read voltage (VGREAD).

![](images/8d45178f01ed290cc2b596723131d2c3661f370bdd1d849afb1d3119653d2b42.jpg)

![](images/677b15321b82afd8d9c4ab8ea64ca46138f1a9fa28855d2ded769a4300dafc97.jpg)  
FIGURE 2. FeFET write schemes (a) with and (b) without a negative $v _ { w }$ [20], [24].

![](images/9ec3dc764a70cd28a5b41bb69716b12b91539f5038189af82b0daca2844c7a1f.jpg)  
FIGURE 3. (a) Voltage- and (b) current-based FeFET sensing schemes.

$V _ { \mathrm { G R E A D } }$ has a value within the memory window and is used for distinguishing the LVT and HVT states. When the drain of the FeFET is driven to the drain read voltage (VDREAD), the I /I current flows according to the stored data in the FeFET. This $I _ { \mathrm { O N } } / I _ { \mathrm { O F F } }$ current can be sensed by the voltage- or current-based sensing scheme. When the source of the FeFET is floated to GND, the voltage of the source is altered by the ION/IOFF current, and this is sensed by the voltage-based sensing circuit. When the source of the FeFET is driven to GND, the ION/IOFF current is sensed by the current-based sensing circuit.

Previous FeFET memory cell structures use various write and sensing schemes. In Section III, we examine the advantages and disadvantages of these write and sensing schemes at the array level.

# C. FeFET MODELING FOR SIMULATION

The $V _ { \mathrm { T H } }$ of the FeFET can be shifted through body biasing or gate metal engineering [19], [28], [29]. Fig. 4 presents the drain–source current $\left( I _ { \mathrm { D S } } \right)$ versus $V _ { \mathrm { G S } }$ curves of FeFETs with different $V _ { \mathrm { T H } }$ distributions [30], [31]. In this study, we divide FeFETs into two types according to the $V _ { \mathrm { T H } }$ distribution: type-I has a negative LVT, whereas type-II has a positive LVT. These two FeFET types use 0 V and a voltage higher than 0 V as V , respectively. Additionally, the available

![](images/19fe9d94bc6318d7656c7ab9432b107e8d8a103d6fd7352979bec3cf1c0646f2.jpg)

![](images/305085ae8aaae2243ed479ea1bdde950182f7e6a6ce52abb0dfa9a8a14c6b3c8.jpg)  
FIGURE 4. $\pmb { I _ { \mathrm { D S } } }$ versus $\pmb { v _ { \odot s } }$ characteristics of the FeFET: (a) $\pmb { I _ { \bigtriangledown S } } - \pmb { V _ { \bigtriangledown S } }$ curve of a type-I FeFET: experimentally measured data for a fabricated FeFET [30]; (b) $\pmb { I _ { \mathrm { D S } } } \mathrm { - } \dot { \pmb { V _ { \mathrm { G S } } } }$ curve of a type-II FeFET: experimentally measured data for a fabricated FeFET [31].

![](images/1b9d6a8a80b539dd3cd0511a7f87b32b6ebccf5f49a8d3352e912dffdde393ee.jpg)

![](images/aa01de3811be99d5e706bba6146d01a9b1acb53338707349c47ad2afaf34fb6b.jpg)  
FIGURE 5. (a) Polarization versus electric field (P–E) hysteresis curve of a fabricated FeFET [31]. (b) Fitted $\pmb { I _ { \mathrm { D S } } } - \pmb { V _ { \mathrm { G S } } }$ curves of a type-II FeFET (black dotted lines). The fitting was based on experimentally measured data for the fabricated FeFET (represented by red and blue solid lines) [31].

sensing scheme is determined by the $V _ { \mathrm { T H } }$ distribution. When the FeFET has a positive LVT (type-II), both sensing schemes (current- and voltage based) can be used in all FeFET cells. This is discussed in detail in Section III.

In this study, we performed HSPICE simulations based on industry-compatible 28 nm complementary metal–oxide– semiconductor (CMOS) technology. The FeFET model used for the simulations is based on the type-II FeFET. Figs. 5(a) and (b), respectively, present the measured polarization versus electric field (P-E) hysteresis and $I _ { \mathrm { D S } }  – V _ { \mathrm { G S } }$ curves (red and blue solid lines) of a fabricated FeFET device with a 10 nm-thick $\mathrm { S i } { : } \mathrm { H f } { \mathrm { O } } _ { 2 }$ [31]. The FeFET model used in this study was fitted using a predictive technology model (PTM) [32] to mimic the measured $I _ { \mathrm { D S } }  – V _ { \mathrm { G S } }$ curves (red and blue solid lines) in Fig. 5(b). The fitting was performed by adjusting the PTM parameters values related to $I _ { \mathrm { O N } } / I _ { \mathrm { O F F } } ,$ , $V _ { \mathrm { T H } }$ , and the subthreshold slope. The black dotted lines in Fig. 5(b) represent the fitted $I _ { \mathrm { D S } }  – V _ { \mathrm { G S } }$ curves obtained using the FeFET model. According to the constant-current criteria (800 nA), the $V _ { \mathrm { T H } }$ values for the LVT and HVT states in the fitted FeFET model are 0.67 and 1.58 V, respectively. Because $V _ { \mathrm { G R E A D } }$ is 1 V in the read simulation, the $I _ { \mathrm { O N } }$ value was adjusted when $V _ { \mathrm { G S } }$ in the fabricated FeFET device is 1 V. The $V _ { \mathrm { T H } }$ and ION/IOFF values obtained with the fitted FeFET model are within a 3% error range of those obtained in [31].

TABLE 1. Control signal information for the 1FeFET, 1T-1FeFET, 2T-1FeFET and 3T-1FeFET cells.   

<table><tr><td>Cell</td><td colspan="4">1FeFET</td><td colspan="3">1T-1FeFET</td><td colspan="3">2T-1FeFET</td><td colspan="3">3T-1FeFET</td></tr><tr><td>Operation</td><td>Hold</td><td>Write Phase 1</td><td>Write Phase 2</td><td>Read</td><td>Hold</td><td>Write</td><td>Read</td><td>Hold</td><td>Write</td><td>Read</td><td>Hold</td><td>Write</td><td>Read</td></tr><tr><td>WL (selected)</td><td rowspan="2">0</td><td>-Vw(-Vw)</td><td>VW(VW)</td><td>VGREAD</td><td rowspan="2">0</td><td>VW</td><td>VDD</td><td rowspan="2">0</td><td>VW</td><td>VDD</td><td rowspan="2">0</td><td>VW</td><td>VDD</td></tr><tr><td>WL (unselected)</td><td>-Vw/2(-Vw/3)</td><td>VW/2(VW/3)</td><td>0</td><td>-VW</td><td>0</td><td>-VW</td><td>0</td><td>0</td><td>0</td></tr><tr><td>BL (write &#x27;1&#x27;)</td><td rowspan="2">0</td><td>-Vw/2(-2Vw/3)</td><td>0</td><td rowspan="2">VDREAD</td><td rowspan="2">0</td><td>VW</td><td rowspan="2">VGREAD</td><td rowspan="2">0</td><td>VW</td><td rowspan="2">VGREAD</td><td rowspan="2">0</td><td>VW</td><td rowspan="2">VGREAD</td></tr><tr><td>BL (write &#x27;0&#x27;)</td><td>0</td><td>VW/2(2Vw/3)</td><td>-VW</td><td>-VW</td><td>0</td></tr><tr><td>SL (write &#x27;1&#x27;)</td><td rowspan="2">0</td><td>-Vw/2(-2Vw/3)</td><td>0</td><td rowspan="2">0</td><td rowspan="2">0</td><td rowspan="2">0</td><td rowspan="2">0</td><td rowspan="2">0</td><td rowspan="2">0</td><td rowspan="2">0</td><td rowspan="2">0</td><td>VW</td><td>VDD</td></tr><tr><td>SL (write &#x27;0&#x27;)</td><td>0</td><td>VW/2(2Vw/3)</td><td>0</td><td>0</td></tr><tr><td>RL (selected)</td><td rowspan="2" colspan="4">-</td><td rowspan="2">0</td><td rowspan="2">0</td><td>VDREAD</td><td rowspan="2">0</td><td rowspan="2">0</td><td>VDREAD</td><td rowspan="2">0</td><td rowspan="2">0</td><td>VDREAD</td></tr><tr><td>RL (unselected)</td><td>0</td><td>0</td><td>0</td></tr><tr><td>DL</td><td colspan="4">-</td><td colspan="3">-</td><td>0</td><td>0</td><td>VDD</td><td>0</td><td>0</td><td>VDD</td></tr><tr><td>SSL (selected)</td><td rowspan="2" colspan="4">-</td><td rowspan="2" colspan="3">-</td><td rowspan="2" colspan="3">-</td><td rowspan="2">0</td><td>VW</td><td>VDD</td></tr><tr><td>SSL (unselected)</td><td>0</td><td>0</td></tr></table>

$^ { \mathsf { a } } V _ { \mathsf { W } } / 2$ IB scheme.   
$^ \mathrm { { b } } V _ { \mathrm { { W } } } / 3$ IB scheme.

# III. PREVIOUS FeFET MEMORY CELLS

The 1FeFET, 1T-1FeFET, 2T-1FeFET, and 3T-1FeFET memory cells were proposed in [21]–[23], and [24], respectively. Each cell uses its own write and sensing schemes according to the access transistor position. In this section, we review the structure and operation of these FeFET memory cells. The FeFET memory cells are in hold operation when they are neither in write nor read operation. In hold operation, the FeFET memory cell needs to maintain the stored data. This can be achieved by setting all control signals to 0 to make the FeFET $V _ { \mathrm { G S } } \mathrm { s }$ in all memory cells 0. The control signal information for all FeFET memory cells is presented in Table 1.

# A. 1FeFET CELL

The 1FeFET cell has the highest density; however, it suffers from write disturbance owing to the absence of an access transistor. To alleviate the write disturbance, the $V _ { \mathrm { W } } / 2$ and $V _ { \mathrm { W } } / 3$ IB schemes were proposed in [21], [25]; however, they still have the probability of write disturbance.

The write operation of the 1FeFET cell is presented in Figs. 6(a) and (b). The write operation occurs in two phases. In phase 1, the data $\mathbf { \ddot { \rho } } _ { 0 } , \mathbf { \vec { \rho } } _ { 0 }$ are written to the cells in which data $\cdot \circ '$ are intended to be written, and in phase 2, the data ‘‘1’’ are written to the cells in which data $" 1 >$ are intended to be written. Phase 1, which begins as the word line (WL) in the selected row, is set $\mathrm { t o } - V _ { \mathrm { W } }$ and the unselected WLs are set $\mathrm { t o } - V \mathrm { w } / 2 \left( - V \mathrm { w } / 3 \right)$ . The bit and sense lines (BLs and ${ \mathrm { S L s } } ,$ respectively) in unselected cells are set to $- V _ { \mathrm { W } } / 2 \left( - 2 V _ { \mathrm { W } } / 3 \right)$ in the $V _ { \mathrm { W } } / 2 ( V _ { \mathrm { W } } / 3 )$ IB scheme.

![](images/f17a9ee869001e5af0b7bfde33782123086fa3a7f4b6c9f2ce4457535d465584.jpg)  
(a)

![](images/9e5aaecc9ef3fc190727db5607abe921d0a2af715d2f5937f692376c9d4b17e8.jpg)

![](images/b8c27b7100414fb9a7f97bd742cd8fa1bac14b700eba3959b8f5feb424206e78.jpg)  
Voltage-based: 0 (float) Current-based : 0 (driving)   
(c)

![](images/71c1f18adbba31b31ef0d8637b4bf2790915d0480b111b9570ccdf212754c610.jpg)  
Voltage-based : 0 (float) Current-based:0 (driving)   
(d)   
FIGURE 6. Array structure $( 2 \times 2 )$ of the 1FeFET cell: (a) write phase 1 and (b) write phase 2 $( ^ { a } V _ { \mathbf { W } } / 2$ IB and $\mathbf { b } _ { \pmb { v } _ { \mathbf { w } } / \mathbf { 3 } }$ IB schemes). Read operation of (c) type-I and (d) type-II FeFETs.

In phase 2, the selected WL is set to $V _ { \mathrm { { W } } }$ , and the unselected WLs are set to $V _ { \mathrm { W } } / 2 \left( V _ { \mathrm { W } } / 3 \right)$ . The BLs and SLs in unselected cells are set to $V _ { \mathrm { W } } / 2 \left( 2 V _ { \mathrm { W } } / 3 \right)$ in the $V _ { \mathrm { W } } / 2 \left( V _ { \mathrm { W } } / 3 \right)$ IB scheme.

Although both schemes were proposed to reduce the write disturbance, they are unable to completely solve the problem.

In the $V _ { \mathrm { W } } / 2$ IB scheme, the disturbance voltage $V _ { \mathrm { W } } / 2$ is applied to the half-selected cells, where either the WL or the BL and SL are selected. In the $V _ { \mathrm { W } } / 3$ IB scheme, the disturbance voltage $V _ { \mathrm { W } } / 3$ is applied to all cells except the selected cells. Although a low-level disturbance voltage occurs in the $V _ { \mathrm { W } } / 3$ IB scheme, the number of disturbed cells and the routing cost increase owing to the large number of required voltage sources, such as $\pm V _ { \mathrm { W } } / 3 , \pm 2 V _ { \mathrm { W } } / 3$ , and $\pm V _ { \mathrm { W } }$ . Additionally, the swing of all BLs, SLs, and WLs occurs during the write operation, leading to high write energy consumption.

The available sensing scheme depends on the type of FeFET. The read operation of the 1FeFET cell is presented in Figs. 6(c) and (d). In the type-I FeFET, all BLs are set to VDREAD, and the selected WL is set to $V _ { \mathrm { G R E A D } } ~ ( = 0 )$ . Thereafter, the SL is floated to GND in a voltage-based sensing scheme or driven to GND in a current-based sensing scheme during the read operation. Because the LVT of the type-I FeFET is negative and the unselected WLs are set to GND during the read operation, the FeFETs in the LVT state in unselected rows are turned on. Thus, the read current flows from the unselected rows to the SL of the selected cell. Furthermore, in the 1FeFET cell, there is no access transistor at the source of the FeFET that can prevent the current path. Therefore, it is impossible to read the data in the selected row under both the voltage- and current-based sensing schemes. In the type-II FeFET, the selected WL is set to $V _ { \mathrm { G R E A D } }$ (a positive value), and the other control signals are assigned similar values to those in the type-I FeFET. Because the gate of the FeFET in the unselected rows is set to GND, the FeFETs in the unselected rows are completely turned off. Therefore, the read current does not flow to unselected rows, and both sensing schemes can be used in the type-II 1FeFET cell.

# B. 1T-1FeFET CELL

The 1T-1FeFET cell has an access transistor at the gate of the FeFET, which can address the write disturbance problem by distinguishing between the selected and unselected rows.

The write operation of the 1T-1FeFET cell is presented in Fig. 7(a). The 1T-1FeFET cell uses a write scheme with a negative $V _ { \mathrm { { W } } }$ . The write operation begins as the selected WL is set to $V _ { \mathrm { { W } } }$ , and the unselected WLs are set to $- V _ { \mathrm { W } }$ . Thereafter, BLs that write data $^ { 6 6 } 1 ^ { , 9 }$ and $\cdots _ { 0 } , \boldsymbol { \cdot } ,$ are set to $V _ { \mathrm { { W } } }$ and $- V _ { \mathrm { W } }$ , respectively. In the write scheme with a negative $V _ { \mathrm { { W } } } .$ , the unselected WLs must be set $\mathrm { t o } - V _ { \mathrm { W } }$ to prevent write disturbance to cells in unselected rows. Additionally, the swing of all BLs occurs during the write operation, leading to high write energy consumption.

The available sensing scheme also depends on the type of FeFET for the 1T-1FeFET cell. The current- and voltagebased sensing scheme operation in the 1T-1FeFET cell is presented in Figs. 7(b), (c), and (d). In the type-I FeFET, the selected WL is set to $V _ { \mathrm { D D } }$ , and the selected read line (RL) is set to $V _ { \mathrm { D R E A D } }$ . Thereafter, all BLs are set to VGREAD. The operation of the SL is identical to that in the 1FeFET cell. In the current-based sensing scheme, no sneak current flows

![](images/bbbce4c5f66f147f91603fcb7226fc78fe8437e6bbd021ac94f9cdc59ac1d622.jpg)  
(a)

![](images/1fe4125631e2096afc6f709e0f0a8dd56d59e3e8a00e2901a7cd814e9a8f6dcb.jpg)

![](images/57a2a7f2fa04c4a2c34194611bbcaa823fadd95b6dba43290494c83f0377957f.jpg)  
(c)

![](images/ec7481e1acabe01e8eb993e72817c0e9baa808cf414e1cef68e8c7c03aae58d7.jpg)  
  
FIGURE 7. Array structure $( 2 \times 2 )$ of the 1T-1FeFET cell. (a) Write operation. (b) Current sensing scheme operation. (c) Voltage sensing scheme operation at type-I FeFET. (d) Voltage sensing scheme operation at type-II FeFET.

from the SL to the unselected RLs because the SL and the unselected RLs are driven to GND. Thus, a current-based sensing scheme can be used for the type-I FeFET. Conversely, in a voltage-based sensing scheme, the SL is floated to GND, and the SL voltage increases when the data $^ { 6 6 } 1 ^ { , 9 }$ are read. Because the FeFETs in the LVT state in the unselected rows are turned on and there is no access transistor at the source of the FeFET in the 1T-1FeFET cell, sneak current can flow from the SL to unselected rows. Subsequently, the SL voltage decreases to GND; thus, it is impossible to read data $" 1 > "$ . Therefore, the voltage-based sensing scheme cannot be used for the type-I 1T-1FeFET cell. In the type-II FeFET, no sneak current flows from the SL to unselected rows because the FeFETs in the LVT state in unselected rows are completely turned off. Thus, both sensing schemes can be used for the type-II 1T-1FeFET cell.

# C. 2T-1FeFET CELL

The 2T-1FeFET cell has two access transistors connected to the gate and drain of the FeFET. It can control the read current path, which flows from the drain to the source of the FeFET owing to the access transistor at the drain of the FeFET. This allows the 2T-1FeFET cell to read the cell by selecting bits.

The write operation of the 2T-1FeFET cell is presented in Fig. 8(a). The 2T-1FeFET cell uses a write scheme with a negative $V _ { \mathrm { { W } } }$ , and its write operation is the same as that of the 1T-1FeFET cell. Thus, all BLs and WLs swing during the write operation, leading to high write energy consumption.

The current- and voltage-based sensing scheme operation in the 2T-1FeFET cell is presented in Figs. 8(b), (c), and (d).

![](images/9bf1d35bc042a9727c3378c1558514a9557ba000465c68cc76c4724d4c69b917.jpg)  
(a)

![](images/a0cd9623d1675b61acb0d39d07855445fad2e7704507990d8147cd4eeba0c24f.jpg)  
(b)

![](images/2d465a59e718fec947af587b85e83377f31d365ecb05b7dcf538b562427e4596.jpg)  
(c)

![](images/4711d89088612fc9cb78e4e182ee88bd2a2f68a1f474c416adbd5b019b990d8b.jpg)  
(d)   
FIGURE 8. Array structure (2 × 2) of the 2T-1FeFET cell. (a) Write operation. (b) Current sensing scheme operation. (c) Voltage sensing scheme operation at type-I FeFET. (d) Voltage sensing scheme operation at type-II FeFET.

The 2T-1FeFET cell has no access transistor at the source of the FeFET. Thus, the current-based sensing scheme can be used for both types of FeFETs, and the voltage-based sensing scheme can only be used for the type-II FeFET, as with the 1T-1FeFET cell. The read operation begins as the selected WL and all data lines (DLs) are set to VDD. The operation of the BL, RL, SL, and unselected WLs is identical to those for the 1T-1FeFET cell.

# D. 3T-1FeFET CELL

In the 3T-1FeFET cell, an access transistor is connected to each of the three terminals of the FeFET. The access transistor at the source of the FeFET can prevent the sneak current path. Thus, a current- or voltage-based sensing scheme can be used regardless of the type of FeFET. However, the 3T-1FeFET cell has the largest area overhead.

The write operation of the 3T-1FeFET cell is presented in Fig. 9(a). This cell uses a write scheme without a negative VW. The write operation begins with the WL and sense selected line (SSL) in the selected row being set to VW. Thereafter, the BLs that write the data ‘‘1’’ are set to V and the SLs that write the data ‘‘0’’ are set to V . In the write scheme without a negative VW, the swing of the unselected WLs can be eliminated. Thus, the 3T-1FeFET cell exhibits low write energy consumption.

Because of the access transistor at the source of the FeFET, both sensing schemes can be used regardless of the type of FeFET in the 3T-1FeFET cell. The read operation of the 3T-1FeFET cell is presented in Fig. 9(b), which begins as the

![](images/f5e19d59d232702e6d0a88f128911dbf66b7783eca43cc516f605307121dfb03.jpg)

![](images/b6a8cca9e3934a324cdbb9c72a2df93fb1b379cfbb8ace63dd9949cfc63a040e.jpg)  
(a)   
(b)   
FIGURE 9. Array structure (2 × 2) of the 3T-1FeFET cell. (a) Write operation. (b) Read operation.

TABLE 2. Parameter values of the FeFET model.   

<table><tr><td>Parameter</td><td>Description</td><td>FeFET LVT</td><td>FeFET HVT</td></tr><tr><td>\(V_{\text{TH}}\)</td><td>Threshold voltage</td><td>0.67 V</td><td>1.58 V</td></tr><tr><td>\({}^{a}_{\text{ON}}\)</td><td>On-current</td><td>9.43 μA</td><td>0.05 nA</td></tr><tr><td>nfactor</td><td>Sub-threshold swing factor</td><td>9</td><td>8.5</td></tr><tr><td>\(E_{\text{ta0}}\)</td><td>\({}^{b}\text{DIBL}\) coefficient</td><td>0.004</td><td>0.006</td></tr><tr><td>μ0</td><td>Low field mobility</td><td>32 cm2/V·S</td><td>200 cm2/V·S</td></tr><tr><td>\(V_{\text{SAT}}\)</td><td>Saturation velocity</td><td>15000 m/s</td><td>25000 m/s</td></tr></table>

a/oN ismeasured at $\mathsf { V } _ { \mathsf { G S } } = 1 \mathsf { V }$   
bDIBL:Drain-induced barrier lowering

selected WL, the selected SSL, and all DLs are set to VDD. Thereafter, all BLs are set to V , and the selected RL is set to $V _ { \mathrm { D R E A D } }$ . The SL operation is identical to that in the 1T-1FeFET cell.

# E. SENSING SCHEME ANALYSIS

As described in the preceding section, the available sensing scheme for the FeFET in an array structure depends on the type of FeFET. Table 3 presents the available sensing schemes for each type of FeFET memory cell. For the type-I FeFET, the 1FeFET cell cannot read data in the selected row because the data in the selected and unselected rows

![](images/0a284488f06ca4cf326f6df0c2247646a5564b802ca305001db2e88319293d61.jpg)  
(a)

![](images/c9b8508937fddb1c4e475a0f074c8ef06c5df25b8b2f2a17de9a1f6a0ca8fb77.jpg)  
(b)

![](images/98e9a33d597ae84c40f2faf95b29f6aad4fcf7c9279b56131558ef1abc977d99.jpg)  
(c)   
FIGURE 10. Operation of the proposed LCSS write scheme: (a) hold; (b) write phase 1: write data $\mathbf { \mu } ^ { \prime \prime } \mathbf { 0 } ^ { \prime \prime } ;$ (c) write phase 2: write data ‘‘1.’’

TABLE 3. Available sensing schemes for each type of FeFET memory cell.   

<table><tr><td>Type of FeFET</td><td>1FeFET</td><td>1T-1FeFET</td><td>2T-1FeFET</td><td>3T-1FeFET</td></tr><tr><td>type-I</td><td>Not available</td><td>Current-based</td><td>Current-based</td><td>All</td></tr><tr><td>type-II</td><td>Alla</td><td>All</td><td>All</td><td>All</td></tr></table>

aAll: both (current and voltage based) sensing schemes.

cannot be distinguished owing to the read current flowing from the FeFETs in the LVT state in the unselected rows to the SL in the selected cell. The 1T-1FeFET and 2T-1FeFET cells can use only the current-based sensing scheme because the data $^ { 6 6 } 1 ^ { , 9 }$ cannot be read under the voltage-based sensing scheme owing to the sneak current flowing from the SL of the selected cell to unselected rows. The 3T-1FeFET cell can use both sensing schemes owing to the access transistor at the source of the FeFET. In contrast, in type-II FeFET, there is no sneak current because the FeFETs in the LVT state in the unselected rows are completely turned off. Thus, when the FeFET memory cell design is based on the type-II FeFET, both sensing schemes can be used for all FeFET memory cells.

# IV. PROPOSED FeFET WRITE SCHEME

Previous FeFET memory cells have the following advantages and disadvantages. The 1FeFET cell exhibits the highest density but suffers from write disturbance. The 1T-1FeFET and 2T-1FeFET cells can address the write disturbance problem due to the presence of an access transistor at the gate of the FeFET. However, they use a write scheme with a negative $V _ { \mathrm { { W } } }$ , which suffers from high write energy consumption because of the voltage swings of the many control signals. The 3T-1FeFET cell uses a write scheme without a negative $V _ { \mathrm { { W } } }$ , which incurs low write energy consumption. However, it exhibits the largest area overhead. Although the 1T-1FeFET cell can address the write disturbance and has a small area overhead, it exhibits high write energy consumption due to

the use of a negative $V _ { \mathrm { { W } } }$ . Thus, to reduce the write energy consumption of the 1T-1FeFET cell, we propose an LCSS write scheme without using a negative $V _ { \mathrm { { W } } }$ .

To significantly reduce the energy consumption without using a negative $V _ { \mathrm { { W } } }$ during the write operation, the proposed LCSS write scheme consists of two phases. Furthermore, the row-wise RL acts as the source of the FeFET.

Fig. 10 illustrates the operation of the proposed LCSS write scheme. Write phase 1 begins as the selected WL is set to $V _ { \mathrm { { W } } }$ to turn on the access transistor at the gate of the FeFET. Next, the selected RL is set to $V _ { \mathrm { { W } } }$ to apply a negative $V _ { \mathrm { G S } }$ to all cells in the selected row. Thus, the data $\mathbf { \ddot { \rho } } _ { 0 } , \mathbf { \vec { \rho } } _ { 0 }$ are written to all cells in the selected row. Write phase 2 begins as the selected RL falls to 0. Subsequently, the BLs that write the data $^ { 6 6 } 1 ^ { , 9 }$ are set to $V _ { \mathrm { { W } } }$ , and the data $" 1 > "$ are written to the cells in which the data $" 1 >$ are intended to be written.

The proposed LCSS write scheme can eliminate the swing of unselected rows owing to the absence of a negative $V _ { \mathrm { { W } } }$ . Additionally, because the data ‘‘0’’ are written owing to the swing of the selected RL, the swing of the BLs that write data $\mathbf { \ddot { \rho } } _ { 0 } , \mathbf { \vec { \rho } } _ { 0 }$ is also reduced. Therefore, the write energy consumption is significantly lower in the proposed write scheme than in the write scheme with a negative $V _ { \mathrm { { W } } }$ at the expense of the overhead in write time.

# V. PERFORMANCE ANALYSIS

In this section, we compare previous FeFET memory cells in terms of write energy, read time, read energy, and layout area. HSPICE simulations were performed using an industrycompatible 28 nm model for CMOS technology, and the FeFET model was fitted using the PTM [32], as described in Section II-C. The V and write time were set to 4 V and 10 ns, respectively [33], [34]. The $V _ { \mathrm { G R E A D } }$ and $V _ { \mathrm { D R E A D } }$ were set to 1 V, which is the value within a memory window. A metal capacitance of 0.21 fF/µm was considered for evaluating the delay and energy [35]. In this simulation, $1 3 2 \times 3 2$ memory array was assumed. Table 4 presents the characteristics and performance of the FeFET memory cells.

TABLE 4. Characteristics and performance of the analyzed FeFET memory cells.   

<table><tr><td></td><td colspan="2">1FeFET cell [21]</td><td colspan="2">2T-1FeFET cell [23]</td><td colspan="2">3T-1FeFET cell [24]</td><td colspan="2">1T-1FeFET cell [22]</td></tr><tr><td>Layout area (μm2)</td><td colspan="2">0.099</td><td colspan="2">0.292</td><td colspan="2">0.392</td><td colspan="2">0.14</td></tr><tr><td>Write scheme</td><td>Vw/2 IB</td><td>Vw/3 IB</td><td colspan="2">with a negative Vw</td><td colspan="2">without a negative Vw</td><td>with a negative Vw</td><td>proposed LCSS</td></tr><tr><td>Negative Vw</td><td colspan="2">yes</td><td colspan="2">yes</td><td colspan="2">no</td><td>yes</td><td>no</td></tr><tr><td>Write disturbance</td><td colspan="2">yes</td><td colspan="2">no</td><td colspan="2">no</td><td>no</td><td>no</td></tr><tr><td>Write time</td><td colspan="2">two-phase</td><td colspan="2">one-phase</td><td colspan="2">one-phase</td><td>one-phase</td><td>two-phase</td></tr><tr><td rowspan="3">Write energy (pJ)</td><td rowspan="3">2.27</td><td rowspan="3">2.84</td><td rowspan="3" colspan="2">3.7</td><td rowspan="3" colspan="2">2.83</td><td rowspan="3">3.16</td><td>worst 2.06</td></tr><tr><td>average 1.09</td></tr><tr><td>best 0.13</td></tr><tr><td>Type of FeFET</td><td>type-I</td><td>type-II</td><td>type-I</td><td>type-II</td><td>type-I</td><td>type-II</td><td>type-I</td><td>type-II</td></tr><tr><td>Available read scheme</td><td>not available</td><td>alla</td><td>current-based</td><td>all</td><td colspan="2">all</td><td>current-based</td><td>all</td></tr><tr><td>Read time (ns)b</td><td>-</td><td>0.279</td><td>-</td><td>0.326</td><td colspan="2">0.510</td><td>-</td><td>0.289</td></tr><tr><td>Read energy (pJ)b</td><td>-</td><td>0.03</td><td>-</td><td>0.107</td><td colspan="2">0.128</td><td>-</td><td>0.036</td></tr></table>

aAll: both (current- and voltage-based) sensing schemes.   
bRead time and energy are measured under the voltage-based sensing scheme.

# A. WRITE ENERGY

The write energy of the FeFET can be divided into two portions: one is consumed by the switching current in the FE layer, and the other is consumed by the voltage swings of the control signals. Because the switching current in the FE layer occurs only in the selected row and is small [16], the energy consumed by it in the FE layer constitutes a small portion of the entire write energy. Conversely, because the swing of the control signals occurs in all lines, most of the write energy is consumed by the swing of the control signals. Thus, we evaluated the write energy consumed by the voltage swings of the control signals.

Fig. 11 presents the write energy for the previous FeFET memory cells and the proposed LCSS write scheme. In the proposed LCSS write scheme, because the data ‘‘0’’ are written into all cells connected to the selected row in write phase 1, the write energy consumption depends on the data portions that are $\cdot \circ '$ and $" 1 >$ in the selected row. Thus, the write energy consumption is divided into three cases according to the data portions: the worst case is to write only ‘‘1’’, the average case is to write an equal number of ‘‘0’’s and ${ } ^ { 6 6 } 1 { } ^ { 5 } \mathrm { s } ,$ , and the best case is to write only ‘‘0’’.

In the write scheme with a negative VW of the 1T-1FeFET and 2T-1FeFET cells, the swing of all WLs and BLs occurs during the write operation, whereas there is no swing of the unselected WLs and BLs for writing data ‘‘0’’ in the proposed LCSS write scheme. Thus, the 1T-1FeFET and

![](images/45f226f366108243a8b6e565dbbdebaccbbe8a7d8535fc6991b2237ac87f1e61.jpg)  
FIGURE 11. Write energy comparison.

2T-1FeFET cells consume 56% and 83% higher write energy, respectively, than the worst case of the proposed LCSS write scheme in the 1T-1FeFET cell.

In the VW/2 and VW/3 IB schemes of the 1FeFET cell, the swing of all WLs, BLs, and SLs occurs during the write operation. Thus, these schemes consume 12% and 40% higher write energy, respectively, than the worst case of the proposed LCSS write scheme in the 1T-1FeFET cell. Because the $V _ { \mathrm { W } } / 3$ IB scheme in the 1FeFET cell uses a higher disturbance voltage $( 2 V _ { \mathrm { W } } / 3 )$ in the BLs and SLs, it incurs in higher

![](images/e3592732d54cbc2dbab0e1848ee75922a5ffdbd58215a89d691fdca89c21d2af.jpg)  
(a)

![](images/8a77d9e627b3d15c0ac532ee22715f257fd5af76bf7dcfdf3aca1ae513516871.jpg)  
(b)   
FIGURE 12. Read performance of FeFET memory cells based on the voltage-based sensing scheme: (a) Read time; (b) Read energy.

write energy consumption than the $V _ { \mathrm { W } } / 2$ IB scheme in the 1FeFET cell.

The 3T-1FeFET cell uses a write scheme without a negative $V _ { \mathrm { { W } } }$ , which can eliminate the swing of unselected rows. Thus, it results in lower write energy consumption than the write scheme with a negative $V _ { \mathrm { { W } } }$ in the 1T-1FeFET and 2T-1FeFET cells. However, the 3T-1FeFET cell has a higher metal capacitance than the other FeFET memory cells. Thus, it consumes 40% higher write energy than the worst case of the proposed LCSS write scheme in the 1T-1FeFET cell.

The proposed LCSS write scheme can eliminate the swing of unselected WLs because it does not use a negative $V _ { \mathrm { { W } } }$ . Additionally, it can eliminate the swing of BLs for writing $\cdot \circ '$ because the data ‘‘0’’ are written through the swing of the selected RL. Thus, the proposed LCSS write scheme can reduce the write energy consumption by 35%, 66%, and 96% in the worst, average, and best cases, respectively, relative to the write scheme with a negative $V _ { \mathrm { { W } } }$ in the 1T-1FeFET cell. Moreover, even in the worst case, the proposed LCSS scheme consumes the lowest write energy compared to the other FeFET memory cells.

# B. READ TIME AND ENERGY

As described in Section IV-B, type-I 1T-1FeFET and 2T-1FeFET cells can only use the current-based sensing scheme. In contrast, type-II FeFET memory cells can use both the current- and voltage-based sensing schemes in all FeFET memory cells. In the read simulation, we evaluated the read performance of type-II FeFET memory cells under the voltage-based sensing scheme.

Fig. 12(a) presents the read times of the FeFET memory cells. The read time of the 1T-1FeFET cell was 11% and 43.3% faster than that of the 2T-1FeFET and 3T-1FeFET cells, respectively, because its read path consists of an FeFET without an access transistor, and it has a low parasitic capacitance. The 1T-1FeFET cell exhibited a similar read time as the 1FeFET cell because both cells have the same read path.

Fig. 12(b) presents the read energy results for the FeFET memory cells. When the data in the selected row are read, the swing of the row-wise control signals (WL, RL, SSL) only occurs in the selected row. Conversely, the swing of the column-wise control signals (BL, SL, DL) occurs in all columns. Thus, the swing of the column-wise control signals

![](images/bff243721f83dce92a497abe274fe453da97407b70a14e823d3c8a5bf31c30f5.jpg)  
(a)

![](images/7f95ed0afc654ddcd9f6a4579c5df37718147245ea601436cfd6ec1d51e5e8eb.jpg)  
(b)

![](images/371e7679224c7d7fbfae5e210b7ea555521c60590f50310287e51752eae30a91.jpg)  
(c)

![](images/136743d9adf8938325fc8372081c260d0581acb918da49a9c60fcf0278e9e360.jpg)  
  
FIGURE 13. Layouts of 2 × 2 FeFET memory cells: (a) 1FeFET cell; (b) 1T-1FeFET cell; (c) 2T-1FeFET cell; (d) 3T-1FeFET cell.

dominates the read energy consumption. The 1T-1FeFET cell consumes 66% and 71.9% lower read energy than the 2T-1FeFET and 3T-1FeFET cells, respectively, because it has a small number of column-wise control signals and low parasitic capacitance. However, the 1T-1FeFET cell consumes 20% higher read energy than the 1FeFET cell because the 1T-1FeFET cell has an additional row-wise control signal (RL).

# C. LAYOUT AREA

Fig. 13 presents the layouts of the 2 × 2 FeFET memory cells based on the industry-compatible 28 nm CMOS technology. The area of the 1T-1FeFET cell is 52% and 64% smaller than that of the 2T-1FeFET and 3T-1FeFET cells, respectively, because it has a small number of access transistors and simple metal routing. Although the area of the 1T-1FeFET cell is 41% larger than that of the 1FeFET cell owing to the access transistor at the gate of the FeFET, the 1T-1FeFET cell has the advantage that there is no write disturbance.

# VI. CONCLUSION

Previous FeFET memory cells have advantages and limitations. The 1FeFET cell exhibits the highest density but suffers from write disturbance. Furthermore, the type-I 1FeFET cell cannot read data in the selected row. The 1T-1FeFET cell can address the write disturbance; however, it uses a write scheme with a negative $V _ { \mathrm { { W } } }$ , which incurs high write energy consumption. The 2T-1FeFET cell can control the read current during the read operation; however, it also uses a write scheme with a negative $V _ { \mathrm { { W } } }$ . Moreover, the type-I 1T-1FeFET and 2T-1FeFET cells can use only a current-based sensing scheme during the read operation. The 3T-1FeFET cell uses a write scheme without a negative $V _ { \mathrm { { W } } }$ , which consumes a low amount of write energy, and can use both currentand voltage-based sensing schemes regardless of the type of FeFET; however, it exhibits the largest area overhead.

Compared with the other FeFET memory cells, under the proposed LCSS write scheme, the 1T-1FeFET cell addresses the write disturbance, has a smaller area overhead and the lowest write energy consumption by eliminating the negative VW. Additionally, the available sensing scheme for each FeFET memory cell was identified according to the FeFET $V _ { \mathrm { T H } }$ distribution. The analysis results indicated that when the FeFET memory cell is designed on the basis of the type-II FeFET, both sensing schemes can be used in all FeFET memory cells.

# APPENDIX

The parameter values of the FeFET model are presented in table 2.

# ACKNOWLEDGMENT

The EDA tool is supported by the Integrated Circuit (IC) Design Education Center.

# REFERENCES

[1] H. Iwai, ‘‘CMOS technology-year 2010 and beyond,’’ IEEE J. Solid-State Circuits, vol. 34, no. 3, pp. 357–366, Mar. 1999.   
[2] R. Gonzalez, B. M. Gordon, and M. A. Horowitz, ‘‘Supply and threshold voltage scaling for low power CMOS,’’ IEEE J. Solid-State Circuits, vol. 32, no. 8, pp. 1210–1216, Aug. 1997.   
[3] H. Li and Y. Chen, ‘‘Emerging non-volatile memory technologies: From materials, to device, circuit, and architecture,’’ in Proc. 53rd IEEE Int. Midwest Symp. Circuits Syst., Seattle, WA, USA, Aug. 2010, pp. 1–4.   
[4] M. Soltani, M. Kamal, A. Afzali-Kusha, and M. Pedram, ‘‘RandShift: An energy-efficient fault-tolerant method in secure nonvolatile main memory,’’ IEEE Trans. Very Large Scale Integr. (VLSI) Syst., vol. 28, no. 1, pp. 287–291, Jan. 2020.   
[5] T. W. Oh, H. Jeong, J. Park, and S.-O. Jung, ‘‘Pre-charged local bit-line sharing SRAM architecture for near-threshold operation,’’ IEEE Trans. Circuits Syst. I, Reg. Papers, vol. 64, no. 10, pp. 2737–2747, Oct. 2017.   
[6] K. Cho, J. Park, T. W. Oh, and S. Jung, ‘‘One-sided schmitt-trigger-based 9T SRAM cell for near-threshold operation,’’ IEEE Trans. Circuits Syst. I, Reg. Papers, vol. 67, no. 5, pp. 1551–1561, May 2020.   
[7] S. M. Kim, B. Song, and S.-O. Jung, ‘‘Sensing margin enhancement technique utilizing boosted reference voltage for low-voltage and high-density DRAM,’’ IEEE Trans. Very Large Scale Integr. (VLSI) Syst., vol. 27, no. 10, pp. 2413–2422, Oct. 2019.   
[8] A. Yan, C. Lai, Y. Zhang, J. Cui, Z. Huang, J. Song, J. Guo, and X. Wen, ‘‘Novel low cost, double-and-triple-node-upset-tolerant latch designs for nano-scale CMOS,’’ IEEE Trans. Emerg. Topics Comput., vol. 9, no. 1, pp. 520–533, Jan. 2021.

[9] A. Yan, Y. Chen, Y. Hu, J. Zhou, T. Ni, J. Cui, P. Girard, and X. Wen, ‘‘Novel speed-and-power-optimized SRAM cell designs with enhanced self-recoverability from Single- and double-node upsets,’’ IEEE Trans. Circuits Syst. I, Reg. Papers, vol. 67, no. 12, pp. 4684–4695, Dec. 2020.   
[10] J. Samandari-Rad and R. Hughey, ‘‘Power/energy minimization techniques for variability-aware high-performance 16-nm 6T-SRAM,’’ IEEE Access, vol. 4, pp. 594–614, Jan. 2016.   
[11] O. Mutlu, ‘‘The RowHammer problem and other issues we may face as memory becomes denser,’’ in Proc. Design, Automat. Test Eur. Conf. Exhib. (DATE), Lausanne, Switzerland, Mar. 2017, pp. 1116–1121.   
[12] S.-S. Sheu, K.-H. Cheng, M.-F. Chang, P.-C. Chiang, W.-P. Lin, H.-Y. Lee, P.-S. Chen, Y.-S. Chen, T.-Y. Wu, F. T. Chen, K.-L. Su, M.-J. Kao, and M.-J. Tsai, ‘‘Fast-write resistive RAM (RRAM) for embedded applications,’’ IEEE Des. Test. Comput., vol. 28, no. 1, pp. 64–71, Jan. 2011.   
[13] H. Y. Cheng, W. C. Chien, M. BrightSky, Y. H. Ho, Y. Zhu, A. Ray, R. Bruce, W. Kim, C. W. Yeh, H. L. Lung, and C. Lam, ‘‘Novel fast-switching and high-data retention phase-change memory based on new Ga-Sb-Ge material,’’ in IEDM Tech. Dig., Washington, DC, USA, Dec. 2015, pp. 3.5.1–3.5.4.   
[14] T. Endoh, H. Honjo, K. Nishioka, and S. Ikeda, ‘‘Recent progresses in STT-MRAM and SOT-MRAM for next generation MRAM,’’ in Proc. IEEE Symp. VLSI Technol., Jun. 2020, pp. 1–2.   
[15] F. Zahoor, T. Z. A. Zulkifli, and F. A. Khanday, ‘‘Resistive random access memory (RRAM): An overview of materials, switching mechanism, performance, multilevel cell (MLC) storage, modeling, and applications,’ Nanosc. Res. Lett., vol. 15, no. 1, pp. 1–26, Apr. 2020.   
[16] M. Halter, L. Bégon-Lours, V. Bragaglia, M. Sousa, B. J. Offrein, S. Abel, M. Luisier, and J. Fompeyrine, ‘‘Back-end, CMOS-compatible ferroelectric field-effect transistor for synaptic weights,’’ ACS Appl. Mater. Interfaces, vol. 12, no. 15, pp. 17725–17732, Mar. 2020.   
[17] X. Li, J. Sampson, A. Khan, K. Ma, S. George, A. Aziz, S. K. Gupta, S. Salahuddin, M.-F. Chang, S. Datta, and V. Narayanan, ‘‘Enabling energy-efficient nonvolatile computing with negative capacitance FET,’’ IEEE Trans. Electron Devices, vol. 64, no. 8, pp. 3452–3458, Aug. 2017.   
[18] X. Li, S. George, Y. Liang, K. Ma, K. Ni, A. Aziz, S. K. Gupta, J. Sampson, M.-F. Chang, Y. Liu, H. Yang, S. Datta, and V. Narayanan, ‘‘Lowering area overheads for FeFET-based energy-efficient nonvolatile flip-flops,’’ IEEE Trans. Electron Devices, vol. 65, no. 6, pp. 2670–2674, Jun. 2018.   
[19] D. Reis, S. Datta, M. T. Niemier, X. S. Hu, K. Ni, W. Chakraborty, X. Yin, M. Trentzsch, S. Dunkel, T. Melde, J. Muller, and S. Beyer, ‘‘Design and analysis of an ultra-dense, low-leakage, and fast FeFET-based random access memory array,’’ IEEE J. Explor. Solid-State Comput. Devices Circuits, vol. 5, no. 2, pp. 103–112, Dec. 2019.   
[20] X. Yin, X. Chen, M. Niemier, and X. S. Hu, ‘‘Ferroelectric FETs-based nonvolatile logic-in-memory circuits,’’ IEEE Trans. Very Large Scale Integr. (VLSI) Syst., vol. 27, no. 1, pp. 159–172, Jan. 2019.   
[21] K. Ni, X. Li, J. A. Smith, M. Jerry, and S. Datta, ‘‘Write disturb in ferroelectric FETs and its implication for 1T-FeFET and memory arrays,’’ IEEE Electron Device Lett., vol. 39, no. 11, pp. 1656–1659, Nov. 2018.   
[22] S. George, K. Ma, A. Aziz, X. Li, A. Khan, S. Salahuddin, M.-F. Chang, S. Datta, J. Sampson, S. Gupta, and V. Narayanan, ‘‘Nonvolatile memory design based on ferroelectric FETs,’’ in Proc. 53rd ACME/EDAC/IEEE Design Automat. Conf. (DAC), Jun. 2016, pp. 1–6.   
[23] X. Zhang, X. Chen, and Y. Han, ‘‘FeMAT: Exploring in-memory processing in multifunctional FeFET-based memory array,’’ in Proc. IEEE 37th Int. Conf. Comput. Design (ICCD), Nov. 2019, pp. 541–549.   
[24] S. George, X. Li, M. J. Liao, K. Ma, S. Srinivasa, K. Mohan, A. Aziz, J. Sampson, S. K. Gupta, and V. Narayanan, ‘‘Symmetric 2-D-memory access to multidimensional data,’’ IEEE Trans. Very Large Scale Integr. (VLSI) Syst., vol. 26, no. 6, pp. 1040–1050, Jun. 2018.   
[25] S.-J. Ham, H.-S. Mo, and K.-S. Min, ‘‘Low-power VDD/3 write scheme with inversion coding circuit for complementary memristor array,’’ IEEE Trans. Nanotechnol., vol. 12, no. 5, pp. 851–857, Sep. 2013.   
[26] A. Aziz, E. T. Breyer, A. Chen, X. Chen, S. Datta, S. K. Gupta, M. Hoffmann, X. S. Hu, A. Ionescu, M. Jerry, T. Mikolajick, H. Mulaosmanovic, K. Ni, M. Niemier, I. O’Connor, A. Saha, S. Slesazeck, S. K. Thirumala, and X. Yin, ‘‘Computing with ferroelectric FETs: Devices, models, systems, and applications,’’ in Proc. Design, Automat. Test Eur. Conf. Exhib. (DATE), Dresden, Germany, Mar. 2018, pp. 1289–1298.   
[27] S. K. Kim, T. W. Oh, S. Lim, D. H. Ko, and S.-O. Jung, ‘‘High-performance and area-efficient ferroelectric FET-based nonvolatile flip-flops,’’ IEEE Access, vol. 9, pp. 35549–35561, Apr. 2021.

[28] X. Yin, K. Ni, D. Reis, S. Datta, M. Niemier, and X. S. Hu, ‘‘An ultradense 2FeFET TCAM design based on a multi-domain FeFET model,’’ IEEE Trans. Circuits Syst. II, Exp. Briefs, vol. 66, no. 9, pp. 1577–1581, Sep. 2019.   
[29] E. T. Breyer, H. Mulaosmanovic, T. Mikolajick, and S. Slesazeck, ‘‘Reconfigurable NAND/NOR logic gates in 28 nm HKMG and 22 nm FD-SOI FeFET technology,’’ in IEDM Tech. Dig., Dec. 2017, pp. 25–28.   
[30] M. Trentzsch, S. Flachowsky, R. Richter, J. Paul, B. Reimer, D. Utess, S. Jansen, H. Mulaosmanovic, S. Muller, S. Slesazeck, J. Ocker, M. Noack, J. Muller, P. Polakowski, J. Schreiter, S. Beyer, T. Mikolajick, and B. Rice, ‘‘A 28 nm HKMG super low power embedded NVM technology based on ferroelectric FETs,’’ in IEDM Tech. Dig., San Francisco, CA, USA, Dec. 2016, pp. 11–15.   
[31] T. Ali, P. Polakowski, S. Riedel, T. Büttner, T. Kämpfe, M. Rudolph, B. Pätzold, K. Seidel, D. Löhr, R. Hoffmann, M. Czernohorsky, K. Kühnel, P. Steinke, J. Calvo, K. Zimmermann, and J. Müller, ‘‘High endurance ferroelectric hafnium oxide-based FeFET memory without retention penalty,’’ IEEE Trans. Electron Devices, vol. 65, no. 9, pp. 3769–3774, Sep. 2018.   
[32] Predictive Technology Model (PTM). Accessed: Jun. 2011. [Online]. Available: http://ptm.asu.edu/   
[33] H. Mulaomanovic, E. T. Breyer, T. Mikolajick, and S. Slesazeck, ‘‘Ferroelectric FETs with 20-nm-thick HfO2 layer for large memory window and high performance,’’ IEEE Trans. Electron Devices, vol. 66, no. 9, pp. 3828–3833, Sep. 2019.   
[34] S. Dunkel et al., ‘‘A FeFET based super-low-power ultra-fast embedded NVM technology for 22 nm FDSOI and beyond,’’ in IEDM Tech. Dig., Dec. 2017, pp. 17–19.   
[35] Y. Xu, F. Bai, W. Liu, and C. Xie, ‘‘An effective capacitance model for 28-nm and beyond copper interconnect,’’ IEEE Trans. Electron Devices, vol. 60, no. 6, pp. 1867–1871, Jun. 2013.

![](images/6ecfd2d4bf041f23ca332f4d458415c52a512eeeeae2522cddc82c5e75d4c137.jpg)

SEHEE LIM (Graduate Student Member, IEEE) was born in Seoul, South Korea, in 1994. She received the B.S. degree in systems biology and electrical and electronic engineering from Yonsei University, Seoul, in 2018, where she is currently pursuing the Ph.D. degree. Her current research interests include physically unclonable function design and ferroelectric FET-based logic IP design.

![](images/76f4d9925d563e1b4fd3e936b87b34a64bdd82f1e616251d0a911593fc2de685.jpg)

SE KEON KIM (Graduate Student Member, IEEE) was born in Seoul, South Korea, in 1996. He received the B.S. degree in electrical and electronic engineering from Yonsei University, Seoul, in 2021, where he is currently pursuing the Ph.D. degree in electrical and electronic engineering. His current research interest includes ferroelectric FET-based nonvolatile circuit design.

![](images/bbe629a3c7aca1170e114207eb08b2086be1e34416389297b8f4e9fb6bf09e2d.jpg)  
DONG HAN KO (Graduate Student Member, IEEE) was born in Seoul, South Korea, in 1995. He received the B.S. degree in electrical and electronic engineering from Yonsei University, Seoul, in 2021, where he is currently pursuing the Ph.D. degree in electrical and electronic engineering. His current research interest includes ferroelectric FET-based nonvolatile circuit design.

![](images/40eae2bd176cab15932cdd6283f4978f3354afd6336a4bc57fc43e5cc49f6ab5.jpg)  
TAE WOO OH (Graduate Student Member, IEEE) was born in Seoul, South Korea, in 1992. He received the B.S. degree in electrical and electronic engineering from Yonsei University, Seoul, in 2015, where he is currently pursuing the Ph.D. degree in electrical and electronic engineering. His current research interests include ferroelectric FET-based nonvolatile circuit design, nextgeneration semiconductor devices, low-power and high-speed SRAM, and processing-in-memory.

![](images/9d9764e225a917ce971cb2ef9db796d2f7f8a67c9d5cae358159a9ef220caf74.jpg)  
SEONG-OOK JUNG (Senior Member, IEEE) received the B.S. and M.S. degrees in electrical and electronic engineering from Yonsei University, Seoul, South Korea, in 1987 and 1989, respectively, and the Ph.D. degree in electrical engineering from the University of Illinois at Urbana–Champaign, Urbana, IL, USA, in 2002. From 1989 to 1998, he was affiliated with Samsung Electronics Company, Ltd., Hwaseong, South Korea, where he was involved in specialty memo-

ries, such as video, graphic, and window RAM, and merged memory logic. From 2001 to 2003, he was affiliated with T-RAM Inc., Mountain View, CA, USA, where he was the Leader of the Thyristor-Based Memory Circuit Design Team. From 2003 to 2006, he was affiliated with Qualcomm Inc., San Diego, CA, USA, where he was involved in high-performance lowpower embedded memories, process variation-tolerant circuit design, and low-power circuit techniques. Since 2006, he has been a Professor with Yonsei University. His current research interests include process variationtolerant, low-power, mixed-mode circuit design, and next-generation memory and technology.