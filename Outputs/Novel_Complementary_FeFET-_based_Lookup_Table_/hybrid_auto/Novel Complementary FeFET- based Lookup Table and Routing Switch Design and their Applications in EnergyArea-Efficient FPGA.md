---
title: "Novel Complementary FeFET- based Lookup Table and Routing Switch Design and their\"
authors:
  - "Yuan-Yu Huang"
  - "Po-Tsang Huang"
  - "Po-Yi Lee"
  - "Pin Su"
date: "2023-01-01"
year: "2023"
journal: "IEEE Transactions on Electron Devices"
abstract: "This work explores the potential of voltage-mode complementary ferroelectric FET\"
abstract_cn: "本研究探索了电压模式互补铁电场效应晶体管在实现面向存储密集型和计算密集型应用的高能效/面积效率非易失逻辑的潜力。互补铁电场效应晶体管可以通过p型铁电场效应晶体管堆叠在n型铁电场效应晶体管上构建，仅占用一个晶体管的面积。每个互补铁电场效应晶体管可用作1位存储单元和2选1多路复用器，且无任何短路电流。此外，由于未选中的n型铁电场效应晶体管或p型铁电场效应晶体管的较高阈值电压，漏电流进一步降低。另外，我们进一步展示了使用互补铁电场效应晶体管的现场可编程门阵列构建模块。仿真结果表明，与使用静态随机存取存储器或电流模式铁电场效应晶体管实现的相同设计相比，互补铁电场效应晶体管可以实现更优的功耗-性能-面积。"
keywords:
  - "[[FeFET]]"
  - "[[Complementary FeFET]]"
  - "[[Lookup table]]"
  - "[[FPGA]]"
cite: "[1] Huang Y Y, Huang P T, Lee P Y, et al. Novel complementary FeFET‑based lookup\"
aiSum: "互补FeFET构建现场可编程门阵列查找表与路由开关：p‑FeFET与n‑FeFET堆叠实现1位存储与2‑1多路复用器，无短路电流，漏电流低，功耗-性能-面积优于静态随机存取存储器/电流模式FeFET设计。"
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
---

# Novel Complementary FeFET- based Lookup Table and Routing Switch Design and their Applications in Energy/Area-Efficient FPGA

Yuan-Yu Huang1, Po-Tsang Huang2, Po-Yi Lee1 and Pin Su1

1Institute of Electronics, National Yang Ming Chiao Tung University, Taiwan

2International College of Semiconductor Technology, National Yang Ming Chiao Tung University, Taiwan

Email: kevinhyyhyy.ee09@nycu.edu.tw, bughuang@nycu.edu.tw, pinsu@nycu.edu.tw

# Abstract

This work explores the potential of voltage-mode complementary ferroelectric FET (CFeFET) to realize energy/area-efficient nonvolatile logics for both memory-intensive and computation-intensive applications. CFeFET can be constructed by a p-type FeFET stacking on a n-type FeFET with only one transistor’s footprint. Each single CFeFET can be utilized as a 1-bit storage element and a 2-to-1 multiplexer without any short currents. Moreover, leakage current is further reduced due to higher $\mathrm { V _ { t h } }$ of unselected n-FeFET or p-FeFET. Additionally, we further demonstrate FPGA building blocks using the CFeFET. Our simulation results show that the CFeFET can achieve superior Power-Performance-Area (PPA) when compared to the same designs implemented by SRAM or current-mode FeFET. Keywords - FeFET, CFET, Routing switch, Lookup table, FPGA

# I. Introduction

Emerging embedded nonvolatile devices have been crucial to augmenting CMOS devices by integrating logic and memory functions to improve energy and area efficiency [1, 2]. Among several emerging nonvolatile devices, FeFETs have gained great attention for both memory-intensive and computation-intensive circuits due to their CMOS compatibility, fast writing speed, low power consumption, and high $\mathrm { R _ { o f f } } / \mathrm { R _ { o n } }$ ratio [3, 4]. However, the FeFET-based memories and logics [5-8] have mainly been studied based on n-type FeFETs. These FeFET-based logics have been realized by sensing on/off currents of FeFETs which limits the implementation of logic styles. Moreover, the overall energy efficiency would be further degraded if considering loading effects, full-swing signals, clock loading of dynamic circuits, and the overhead of sensing circuits.

To overcome the design constraints of currentmode FeFET-based logics, in this work we propose a voltage-mode CFeFET by stacking a p-FeFET and a n-FeFET vertically with common gate and common drain terminal as shown in Fig. 1 [11]. Each CFeFET can be adopted as both a nonvolatile SRAM-like memory cell and a 2-to-1 multiplexer (MUX) based on the complementary configuration of p-FeFET and

![](images/4ca6d377be3bd3cfc35f1121681c2f8c1adf56825229c98412103593c23379e2.jpg)

![](images/7b561b199e594b2472206a699dce3f9a9b75ecc87c6889d4b33bbe3a1157b788.jpg)  
Fig. 1. A voltage-mode CFeFET stacking by a p-FeFET and a n-FeFET with a common gate and a common drain by the views of 45-degree, a crosssection of gate and a cross section of S/D.

n-FeFET. These two complementary FeFETs are configured as $\mathrm { \ h i g h - V _ { t h } }$ and $\mathrm { 1 o w \mathrm { - V _ { t h } } }$ devices with large $\mathrm { R _ { o n } / R _ { o f f } }$ ratio, respectively. Therefore, the proposed CFeFET can realize low-power and area-efficient nonvolatile memories and logics with full-swing outputs. To further explore the feasibility and benefits of CFeFET-based memories and logics, the building blocks of FPGA utilizing CFeFET are also demonstrated.

# II. Simulation Methodology and CFeFET Characteristics

An in-house SPICE model is utilized to simulate CFeFET, and the ferroelectric layers surrounding the MOSFETs are described by the Monte-Carlo NLS model [9]. This model regards the ferroelectric layers as polycrystalline with multiple grains that switch independently. Additionally, the electrical characteristics of the surrounded MOSFETs as shown in Fig. 1 have been calibrated with TCAD using a BSIM-CMG compatible model based on [10]. Fig. 2 presents the $\mathrm { I _ { D } \mathrm { - V _ { G } } }$ curves of both n-FeFET and p-FeFET under two binary states. Due to the hysteric behavior of the ferroelectric layers, after applying a positive writing voltage (Vw), a red solid $\mathrm { { I } _ { D } \mathrm { { - } } V _ { G } }$ curve for n-FeFET $( \mathrm { l o w \mathrm { - } V _ { t h } }$ state) and a red dashed $\mathrm { I _ { D } - V _ { G } }$ curve for p-FeFET $\mathrm { ( h i g h - V _ { t h } }$ state) can be obtained for state-0. Likewise, the electrical characteristics of state-1 are based on the black solid $\mathrm { I _ { D } - V _ { G } }$ curve for n-FeFET $\mathrm { ( h i g h - V _ { t h } }$ state) and a black dashed one for p-FeFET $( \mathrm { l o w \mathrm { - } V _ { t h } }$ state) after applying a negative $\mathrm { V } _ { \mathrm { w } } .$ .

![](images/fcd75f187348929a36a0b0724faa55c82dd2c1d5c38feef71e182daf697f43ae.jpg)

![](images/be78b98c460f064295bac3daea3546bf26c6b6435ecf54a6a1cb2a0b9ed2db3a.jpg)  
Fig. 2. $\mathrm { I _ { D } \mathrm { - V _ { G } } }$ curves of both n-FeFET and $\mathsf { p - }$ FeFET under two binary states.   
Fig. 3. Building blocks of a FPGA, including CLBs (which is composed of multiple basic logic elements), CBs and SBs.

The memory windows (high $- \mathrm { V } _ { \mathrm { t h } } \ - \ \mathrm { l o w { - } V _ { \mathrm { t h } } ) }$ of n-FeFET and p-FeFET are 0.95 V with the writing voltage $( \mathrm { V _ { w } } ) \pm 3 \mathrm { V }$ under $| \mathrm { V } _ { \mathrm { D S } } | = 0 . 0 5 \ : \mathrm { V } .$ Hence, the CFeFET can be adopted as a nonvolatile SRAM-like memory cell or a logic element and their mechanisms are explained in the next section.

# III. CFeFET-based FPGA Design

FPGAs are built up by configure logic blocks (CLBs), connection blocks (CBs), and switching blocks (SBs) as shown in Fig. 3. These tiled blocks adopt great amounts of lookup tables (LUTs) and multiplexers for reconfigurable functions and signal routing. Unfortunately, the implementation of LUTs and configurable routing switches are both areahungry and power-hungry when using SRAM. Thus, 1T-FeFET had been suggested as a promising candidate for LUTs and routing circuits in FPGAs [6]. To prevent sneak currents of static FeFET logics, a voltage-mode CFeFET-based LUT is designed by CFeFET as memory cells. Furthermore, CFeFET is also adopted for routing switches in CBs and SBs.

# A. Nonvolatile 2-to1 MUX based on CFeFET

The proposed CFeFET can be performed as a

![](images/12869a9e3ac173ab958a1d59c683e5daf0668e6fa632e793ca2976c012993b16.jpg)  
(a)

![](images/29eee145f2a4577833633451a3c5da24fca2e65fb52ab6c2fbafecfef73e8745.jpg)

![](images/19d83415e4989c4b5353593a67b78b291b0ebc48e18eba0060374c9b8bd773bc.jpg)  
Fig. 4. (a) Circuit and (b) schematic of CFeFET as a 2-to-1 MUX.   
（a)

![](images/a74960862d459cd802eea9ea111fb3ddd65e74bdf89f543c460ed1ad0c5f2c78.jpg)  
  
Fig. 5. Waveforms of the CFeFET-based 2-to-1 MUX after (a) negative $\mathrm { V _ { w } }$ and (b) positive $\mathrm { V } _ { \mathrm { w } } .$

voltage-mode nonvolatile 2-to-1 MUX while $\mathrm { V _ { g } { = } 0 V }$ as shown in Fig. 4. After applying a negative $\mathrm { V _ { w } }$ to the common gate, n-FeFET will be operated as an enhancement-mode transistor (high resistive when $\mathrm { V _ { g } { = } 0 V ) }$ and p-FeFET will be operated as a depletionmode transistor (low resistive when $\mathrm { V _ { g } { = } 0 V ) }$ . On the contrary, n-FeFET and p-FeFET will be low resistive and high resistive after applying a positive $\mathrm { V } _ { \mathrm { w } } ,$ , respectively. Thus, by applying the inputs at the sources of CFeFET to build up a pass transistor logic (Fig. 4), the output swing of the CFeFET-based MUX will not be degraded by a $\mathrm { V _ { t h } }$ drop as a full-swing signal. The polarization state (P) in Fig. 4 determines which input can pass through to the output. Fig. 5 shows the simulated waveforms of the CFeFETbased MUX demonstrating the functionality.

Routing switches among SBs and CBs consume lots of area in FPGAs and can be easily implemented by CFeFET-based MUXs by integrating the function of memories and switches as shown in Fig. 6. Compared to FeFET-based routing switches in [5], the programming time and corresponding peripheral circuits of CFeFET-based switches can be decreased in half by the common gate, and double n-FeFETs in [5] have to be written by complementary signals independently. Moreover, only one transistor will be turned on due to the natural property of CFeFET after

![](images/0025bce0ea7b6ca3ee05091318164a7a05b01a1f151494d2f23b848e1fa2036b.jpg)  
Fig. 6. Schematic and waveforms of the CFeFETbased routing switch.

![](images/2b5e4da37f40d9fa616ba43b15fb58b8aea4f77923e791f73ca79073663a3a02.jpg)  
Fig. 7. A conceptual schematic of a CFeFETbased CLB and the corresponding waveforms.

a single programming process. In view of these, CFeFET is more suitable to be adopted as routing switches in CLB.

# B. CFeFET-based Lookup Table

A conceptual schematic of CLB consists of a 2-input LUT and a routing switch as shown in Fig. 7 is realized by CFeFETs for both memory cells and a routing switch. The write pass transistors are added to prevent write disturbance [12]. During write operations, a two-phase write scheme is adopted to write all 0 and all 1 by applying +3V and -3V as $\mathrm { V } _ { \mathrm { w } } ,$ respectively. Thus, the write wordline (WWL) of selected cells and write bitline (WBL) are $\mathrm { V _ { p a s s } }$ and $\mathrm { V _ { w } }$ while read source lines for n-FeFET (RSLn) and p-FeFET $\mathrm { ( R S L _ { p } ) }$ have to be biased at GND. After write operations, the ${ \mathrm { R S L } } _ { \mathfrak { p } }$ will be biased to $\mathrm { \Delta V _ { D D } , }$ and $\mathrm { R S L _ { n } }$ remains grounded. Fig. 7 also presents the waveforms of an XOR gate built up by the 2-input LUT with 4 memory cells. A positive $\mathrm { V _ { w } }$ and a negative $\mathrm { V _ { w } }$ are applied for (A,D) and (B,C) cells in sequence. All CFeFET memory cells are accessed simultaneously, and all the outputs are connected to $\mathrm { R S L _ { n } }$ or ${ \mathrm { R S L } } _ { \mathfrak { p } }$ as full-swing signals. Thus, the delay

of this LUT is determined by a pass-transistor network (PT-network) and level-restored inverters. Table I compares the performance of a 4-input LUT implemented by CFeFET, 1T-FeFET, and SRAM, respectively. The simulation results show that the proposed CFeFET can achieve the smallest delay, power consumption, and area. Both the delay and power consumption of the 1T-FeFET-based LUT are large due to the short current. Additionally, the 1T-FeFET-based static logics are ratioed circuits and sensitive to process variations.

Table I. Comparison of 4-input lookup tables implemented by CFeFET, 1T-FeFET and SRAM.   

<table><tr><td></td><td>Delay (ps)</td><td>Static Power (nW)</td><td>Active Power (nW)</td><td>Device count</td></tr><tr><td>CFeFET</td><td>26.8</td><td>0.66</td><td>2.5</td><td>16 CFeFETs (16 n-FeFETs and 16 p-FeFETs) + 58 MOSFETs</td></tr><tr><td>1T-FeFET</td><td>126</td><td>184</td><td>207</td><td>16 FeFETs + 61 MOSFETs</td></tr><tr><td>SRAM</td><td>39</td><td>2.73</td><td>6.42</td><td>170 MOSFETs</td></tr></table>

# IV. Conclusion

A novel nonvolatile CFeFET device is presented in this paper by stacking a n-FeFET and a p-FeFET vertically, to realize embedded nonvolatile memories and logics. A large $\mathrm { { I _ { o n } / I _ { o f f } } }$ ratio can be achieved since one of n-FeFET or p-FeFET is operated in the enhancement mode and the other one is operated in the depletion mode. The utilization of CFeFET-based memories and logics can reduce area, delay, and power significantly. The building blocks of FPGAs using CFeFET have been demonstrated for achieving better PPA. These advantages render CFeFET a promising candidate for future low-power, small-area, and high-performance embedded nonvolatile devices.

# Acknowledgments

This work was supported in part by the National Science and Technology Council, Taiwan, under Grants 111-2218-E-A49- 016-MBK, 111-2634-F-A49-008 and 110-2221-E-A49-136- MY2, and in part by the “Center for Semiconductor Technology Research” from the Featured Areas Research Center Program within the framework of the Higher Education Sprout Project by the Ministry of Education, Taiwan.

# References

[1] J. Cong, et al. TVLSI, pp 864-877, 2013. [2] D. Suzuki, et al. VLSI Circuits, 2009. [3] T. Mikolajick, et al. IEDM, pp. 15.5.1- 15.5.4, Oct. 2019. [4] S. Dünkel, et al. IEDM, pp. 19.7.1-19.7.4, Dec. 2017. [5] X. Chen, et al. TCAS-I, 66.5, pp.1 780-1793, 2018. [6] X. Chen, et al. ISCAS, 2018. [7] E.T. Breyer, et al. JEDS, p. 748-756, 2020. [8] W.-X. You, et al. TED, 69.1, pp. 444-446, 2021. [9] C. Alessandri, et al. TED, pp. 3527-3534, 2019. [10] L.T. Clark, et al. Microelectronics Journal, 53, pp. 105-115, 2016. [11] Subramanian, S., et al. IEEE Symposium on VLSI Technology, 2020. p. 1-2. [12] Huang, Bo-Kai, et al. VLSI-TSA. IEEE, 2021.