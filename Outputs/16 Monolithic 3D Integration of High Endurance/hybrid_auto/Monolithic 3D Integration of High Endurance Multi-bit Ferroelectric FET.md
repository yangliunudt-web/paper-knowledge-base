---
title: "Monolithic 3D Integration of High Endurance Multi-bit Ferroelectric FET"
authors:
  - "T. Francois"
  - "J. Coignus"
  - "A. Makosiej"
  - "B. Giraud"
date: "2022-06-12"
year: 2022
journal: "IEEE VLSI Symposium"
doi: "10.1109/VLSITechnologyandCir46769.2022.9830141"
abstract: "Demonstrates monolithic 3D integration of ferroelectric FETs with multi-bit storage\
  \ capability and high endurance. The 1T-1C FeFET concept features ferroelectric\
  \ MFM device in interconnect layer, enabling BEoL integration with CMOS. Achieves\
  \ >10^10 endurance cycles and 2-bit per cell operation."
abstract_cn: "展示具有多比特存储能力和高耐久性的单片 3D 集成铁电 FET。1T-1C FeFET 概念在互连层中集成铁电 MFM 器件，实现与 CMOS 的后端集成。实现\
  \ >10^10 耐久循环和每单元 2 比特操作。"
cite: "[1] Francois C M G Monolithic 3D Integration of High Endurance Multi-bit Ferroelectric\
  \ FET[C]. IEEE VLSI Symposium, 2022. DOI: 10.1109/VLSITechnologyandCir46769.2022.9830141."
aiSum: "单片 3D FeFET 集成：BEoL 铁电 MFM 器件，>10^10 耐久性，2 比特/单元，16kbit 阵列演示。"
confidence: high
---

1 University of Notre Dame, Notre Dame, IN 46556, USA; 2 Georgia Institute of Technology, Atlanta, GA, USA

*Equal contribution; Email: sdutta4@nd.edu

Abstract: We demonstrate, for the first time, monolithic 3D (M3D) integration of back-end-of-line (BEOL) compatible Hf0.5Zr0.5O2 (HZO) ferroelectric FET (FeFET) with front-endof-line (FEOL) high-k/metal gate (HKMG) Si-NMOS. We use low thermal budget $( { < } 4 0 0 ^ { 0 } \mathrm { C } )$ processing to integrate HZO with 1% Tungsten (W)-doped amorphous In2O3 (IWO) semiconducting oxide channel and demonstrate high remnant polarization charge density $2 P _ { R , }$ of $4 0 \mu C / c m ^ { 2 }$ with reliable switching characteristics. We report (a) read memory window of 0.45V in ultra-scaled 20nm channel length IWO FeFET, (b) write speed of 100ns, and (c) write endurance ${ > } 1 0 ^ { 8 }$ cycle. We further demonstrate a 2bit/cell synaptic weight cell with well separated conductance states. System-level analysis of compute-in-memory (CIM) accelerators for performing inference on CIFAR-10 image dataset using VGG-8 model shows that 22nm BEOL FeFET achieves 3× higher energyefficiency than 7nm SRAM while occupying a smaller memory array area due to area folding enabled by M3D architecture.

# I. Introduction

Billions of connected edge devices produce zettabytes of data per year that need to be transformed into actionable information. This has created an unprecedented demand for data-centric computing. With on-chip memory limited by SRAM size, there is an extraordinary volume of data traffic between processor and off-chip memory that adds to energy and latency. Compute-in-memory (CIM) is a promising approach to overcome memory bottleneck where compute is moved closer to the data residing in the memory. Embedded non-volatile memory (eNVM) technologies such as FeFET [1], RRAM [2] and STT-MRAM [3] are candidates for storing the weight matrix on-chip and for performing vector-matrixmultiplication (VMM) in-situ to accelerate deep neural network (DNN) inference. Conventional CIM architecture colocates eNVM and access transistors in the FEOL along with CMOS logic and periphery like MUX, analog-to-digital converter (ADC) in the FEOL. M3D CIM architecture targets placement of the memory array in the BEOL with CMOS periphery under the array (CUA) (Fig. 1(a)). Such M3D CIM accelerator provides significant area, energy and latency advantage [4]. Here, we demonstrate a BEOL compatible FeFET that is monolithically integrated on top of FEOL silicon NMOS to realize high-density 3D synaptic array (Fig. 1(b)). While 1T-1RRAM and 1T-1MRAM require large FEOL access transistors resulting in $3 0 { - } 6 0 \mathrm { F } ^ { 2 }$ bit cell area [2-3], M3D 1T-1FeFET bit cell occupies only $1 5 \mathrm { F } ^ { 2 }$ , providing a huge density advantage. Additionally, the low write and read energy of BEOL FeFET provides an energy-efficiency benefit when compared to SRAM and other eNVM technologies (Fig. 1(c)). In this work, we demonstrate BEOL compatible low thermal

budget processing and integration of HZO with amorphous oxide semiconductor (AOS) channel. IWO is preferred as the AOS channel material for FeFET owing to its high field-effect electron-mobility [5,6] under low thermal budget processing compared to poly-Si, absence of unwanted low-k interfacial layer formed between the Si interface and the HZO. Recently HZO has been integrated with BEOL compatible IGZO channel [7], however, IWO offers better improved $\mathrm { V } _ { \mathrm { T } }$ stability due to higher oxygen-bond dissociation energy of W that acts as both stabilizer and electron donor [8]. We experimentally demonstrate 2bit/cell synaptic characteristics of IWO FeFET with well separated conductance states and scalability down to 20nm for providing performance boost for CIM accelerators.

# II. Fabrication Process

The key fabricat