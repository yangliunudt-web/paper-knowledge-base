---
title: "Deep Random Forest with Ferroelectric Analog Content Addressable Memory"
date: "2024-01-01"
year: 2024
journal: "Science Advances"
doi: "10.1126/sciadv.adk8471"
abstract: "[Summarized - Supplementary Materials] Demonstrates deep random forest"
abstract_cn: "使用铁电模拟内容寻址存储器实现深度随机森林算法用于边缘计算。利用 FeFET 模拟状态存储决策树节点和基于相似性的路由。实验设置包括 NI"
cite: "Yin X, Zhuo C, Kämpfe T, et al. Deep random forest with ferroelectric analog"
aiSum: "FeFET 模拟 CAM 深度随机森林：多级 V_TH 存储、1×16 阵列演示、边缘计算决策树。"
confidence: "high"
---

Sci. Adv. 10, eadk8471 (2024)

DOI: 10.1126/sciadv.adk8471

# This PDF file includes:

Figs. S1 to S19

Table S1

References

# Supplementary Materials

# Experimental Setup

Fig.S1 shows the experimental setup used in this work for the demonstration of FeFET analog CAM cell and array for the decision tree and deep random forest.

![](images/b738729057bd52d6c0d697b7e45fad6d6fd92c42bd227d3a4c2479229088d16d.jpg)

![](images/01134190ed1be6676350837a7fc74a38784809db30f12b39ff6555a04449b744.jpg)  
PXl-System

![](images/33e45b56f5fc22ae8b7aa58d7c19388bb65555129e16995126767e31b54e65f4.jpg)  
Switch-Matrix

![](images/81c5693ac159f4ddb0d2b0dfd0846e8286bf49cae5ec6d8fe2710614e96cde89.jpg)  
Probe Station

![](images/d7a60242ef122d00486d0b7c224e27711abc3821d65aa7df21451c0c72b485eb.jpg)  
Probe Card&Wafer   
Figure S1: The setup with the NI PXI system with PPMU and SMU modules (1), the switch matrix board (2), the 300mm wafer probe station (3) and the probe card connecting the wafer with the array structure (4).

![](images/baf4fdda07c0d177765c63ae2c8a97b921ca614cf60069bfd1d1f968b7cfba97.jpg)

![](images/e9533814a6e696e53f5a003b109260e8b00643c572b232951be657c6da80f646.jpg)

![](images/677e2914163345ae2de68454beab94d30840d5af9fed8d690eff585e472d1d1c.jpg)

![](images/09f1199c31c745dbf1d97a8d823f55c1e4759bc8c2674d93b2fc692ce7b9990d.jpg)  
Figure S2: Multiple states in FeFET [23]. (a) Switching dynamics in FeFET showing the memory window as a function of write pulse width at different write pulse amplitudes. FeFET is initialized with +4V, 1µs write pulse before each measurement. The write pulse amplitudes changed from -1V to -3.8V with a step of -0.1V. Intermediate $V _ { T H }$ states are observed. (b) $I _ { D ^ { - } } V _ { G }$ characteristics for four different states in 60 different FeFET devices. (c)/(d) The $V _ { T H }$ distributions for 4/8 levels, respectively [23]. Different levels are written through a write pulse with different amplitudes. Tight $V _ { T H }$ distribution is obtained given the present unoptimized FeFET devices.

# Measurement On An 1×16 CAM Array: Other Cells In State 4

![](images/642b1c9190bdb6c6a2b0fa26470088b7a6ee95b1169faa4bea0f14c3af5b2456.jpg)  
15 cells are in state 4, $\mathsf { V } _ { \mathsf { T H } } \mathsf { = } 1 . 1 \mathsf { V }$

![](images/22c3ae945a88429cb510426bf5d2c0e3e675cc026351eb0a6d205e278f79c573.jpg)

![](images/72a2941a4a6635cbf1105538c96185f56e3e6d27ac1e30d197ee0525ad155379.jpg)

![](images/9b500848854609e062dbd3b937c8a2a77d2f5ae3b90aae7d4ef1886942f0d058.jpg)

![](images/69c64f1b0ac5a1a14a4f2d53532bd94cdcb87c38701aeffd8e233d0c941933ad.jpg)

![](images/a8401b10f8426e91fdae9f2a3723e36b9bd732b1f02298953000a387f7547757.jpg)

![](images/dcdb8d50aa1003ee355f0371d58547491ead3ee4424f9819076770dffc29244f.jpg)

![](images/d0220d1d2b3ccbb38f81241027a9e275aac056396720842621da0caa07203b67.jpg)

![](images/489dd272b766db17d20d8fd097fe9133d0cb81ec0148c0adab6bb7fcbf59b689.jpg)

![](images/d9b79a4644215d2b256f01cb4aba2fdfa7d87a017482de35dd0b01db3cce529c.jpg)

![](images/27d439b4d13fccd88af3dd6931d808a12223cf9e0cad6a25950182ab6596347f.jpg)

![](images/c3f27a9cc16a5a2507aa02d9d7f202afc22c72c84418fd2d2e7e3ff381109b01.jpg)

![](images/de3a40ae6bfb70dd2164373c747468ba18f25432de84a6c3630039a1dc991d14.jpg)

![](images/7145f9dccba71b68e8de2eb7dffaa2ac42c26da728199925c66adec212f10550.jpg)

![](images/7f9871a8cf5b75a1ae0486818515810bcf5e3528e106d683d352faca8bb2bec3.jpg)

![](images/8fe46471878546e867a655dc8491a309a65e45baf42601c1dce70e3abe6e03be.jpg)  
Figure S3: Measurement on a 1×16 analog CAM array. During testing, all $F _ { 1 }$ transistors in the array are set to be $h i g h – V _ { T H }$ states, fixing the 