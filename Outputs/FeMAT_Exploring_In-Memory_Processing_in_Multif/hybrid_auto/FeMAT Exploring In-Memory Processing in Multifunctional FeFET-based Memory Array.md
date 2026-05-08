---
title: "FeMAT: Exploring In-Memory Processing in Multifunctional FeFET-based Memory Array"
authors:
  - "Xiaoyu Zhang"
  - "Xiaoming Chen"
  - "Yinhe Han"
date: "2023-01-01"
year: 2023
journal: "IEEE Transactions on Computers"
abstract: "The performance gap between the processors and the main memory is continuously widening,\\"
abstract_cn: "处理器与主内存之间的性能差距持续扩大，称为内存墙瓶颈。新兴非易失性器件具有存内处理能力，因此有潜力部分缓解内存墙瓶颈。人们已采用非易失性器件构建针对不同问题和应用的各种加速器。本工作中，我们采用新兴非易失性器件之一的铁电场效应晶体管，构建了一个多功能存内处理单元，命名为FeMAT。从结构角度看，FeMAT是一个由基于3T单元组成的FeFET存储阵列。从功能角度看，FeMAT不仅是一个非易失性存储器，还可以在内存中执行一些逻辑操作（即存内处理模式）、二值卷积（即二值卷积神经网络加速模式）和内容搜索（即三元内容可寻址存储器模式）。这些功能无缝融合到FeFET存储阵列中，并且可以在不改变电路结构的情况下在线配置。我们的实验以及与基于电阻随机存取存储器的等效设计、以及基于互补金属氧化物半导体器件的TCAM和BCNN加速器的比较，证明了其卓越的能效。"
keywords:
  - "[[FeFET]]"
  - "[[In-memory processing]]"
  - "[[Ternary content-addressable memory]]"
  - "[[Binary convolutional neural network]]"
cite: "[1] Zhang X, Chen X, Han Y. FeMAT: exploring in‑memory processing in multifunctional\\"
aiSum: "FeMAT多功能FeFET存储阵列：基于3T单元，支持存内处理、二值卷积神经网络加速、三元内容可寻址存储器三种模式，能效优于ReRAM等效设计及CMOS基TCAM/BCNN加速器。"
confidence: medium
---

# FeMAT: Exploring In-Memory Processing in Multifunctional FeFET-based Memory Array

Xiaoyu Zhang $^{1,2}$ , Xiaoming Chen $^{1*}$ , Yinhe Han $^{1}$ $^{1}$ State Key Laboratory of Computer Architecture, Institute of Computing Technology, Chinese Academy of Sciences $^{2}$ School of Computer Science and Technology, University of Chinese Academy of Sciences  
*Corresponding author (e-mail: chenxiaoming@ict.ac.cn)

Abstract—The performance gap between the processors and the main memory is continuously widening, known as the memory wall bottleneck. Emerging nonvolatile devices have the ability of in-memory processing, and thus, have the potential to partially alleviate the memory wall bottleneck. People have adopted nonvolatile devices to build various accelerators that are targeted at different problems and applications. In this work, we adopt one of the emerging nonvolatile devices, the ferroelectric field-effect transistor (FeFET), to build a multifunctional in-memory processing unit, which is named FeMAT. From a structural point of view, FeMAT is an FeFET-based memory array composed of 3T-based cells. From a functional point of view, FeMAT not only is a nonvolatile memory, but also can perform some logic operations (i.e., the processing-in-memory (PIM) mode), binary convolutions (i.e., the binary convolutional neural network (BCNN) acceleration mode) and content searching (i.e., the ternary content-addressable memory (TCAM) mode) in the memory. These functions are seamlessly fused into the FeFET-based memory array and can be configured online without changing the circuit structure. Superior energy efficiency is demonstrated by our experiments and comparisons with a resistive random-access memory (ReRAM) based equivalence, as well as a TCAM and a BCNN accelerator based on complementary metal-oxide-semiconductor (CMOS) devices.

Index Terms—Ferroelectric field-effect transistor, in-memory processing, ternary content-addressable memory, binary convolutional neural network

# I. INTRODUCTION

In the past decades, the performance gap between processors and memories has been continuously widened [1], which is known as the memory wall bottleneck. Due to the separated processors and memories, a large amount of data need to be transferred between processors and memories through the narrow off-chip memory bus, which becomes the bottleneck of computing systems. It is reported that a data access from a dynamic random-access memory (DRAM) consumes three orders of magnitude higher energy than a simple arithmetic operation [2]. As a result, the energy consumption of data movement can be over $60\%$ and up to over $90\%$ of the total

This work was supported in part by the National Key Research and Development Project under Grant 2018YFA0701502, in part by the Innovative Project of Institute of Computing Technology, Chinese Academy of Sciences (CAS), under Grant 5120186140, in part by the 0-to-1 Innovative Project of the CAS Fundamental Frontier Scientific Research Program under Grant ZDBS-LY-JSC012, in part by National Natural Science Foundation of China under Grant 61804155, in part by the Youth Innovation Promotion Association CAS, and in part by the Young Elite Scientists Sponsorship Program by CAST under Grant 2018QNRC001.

energy consumption for big-data applications [3]. Instead of moving data between the main memory and the processing units, in-memory processing performs computations inside the memory, and thus, both the performance and the energy efficiency of computing systems can be improved due to the reduced data movement. In-memory processing is considered as one of the promising solutions to alleviate the memory wall bottleneck.

In recent years, there emerge many nonvolatile devices that support in-memory processing, and thus, have the potential to partially alleviate the memory wall bottleneck. Popular nonvolatile devices include resistive random-access memories (ReRAMs), magnetic tunnel junctions (MTJs), ferroelectric field-effect transistors (FeFETs), phase-change memories (PCMs), etc. Among all the emerging nonvolatile devices, FeFETs have a unique feature that they are three-terminal devices so they are compatible with conventional metal-oxide-semiconductor field-effect transistors (MOSFETs) [4]. As a three-terminal transistor, an FeFET can function as both a nonvolatile storage element and a controllable switch. The three-terminal structure results in separated read and write paths and allows for easy control of both write and read power. This is a unique advantage compared with other two-terminal devices (e.g., ReRAMs, MTJs and PCMs).

The advantages of FeFETs have been experimentally investigated [5]–[7] and demonstrated in various circuits with comparisons with complementary metal-oxide-semiconductor (CMOS) based volatile circuits [8]. The targeted applications include memories [9]–[11], ternary content-addressable memories (TCAMs) [12], [13], lookup tables [14], field-programmable gate arrays [15], binary convolutional neural networks (BCNNs) [16], processing-in-memory (PIM) logics [11], logic gates [13], flip-flops [17], linear algebra [18], etc. Though these circuits or accelerators offer higher performance and/or energy efficiency than CMOS-based circuits, these designs are quite application specific. In other words, different applications need different circuits, architectures, and design methodologies. We found that some accelerators can be merged into a memory array by exploring the structural similarities, so that we can perform various functions just in a memory array instead of employing dedicated circuits or accelerators. As a result, the cost can be significantly reduced. Such a fused system is especially suitable for the cases requiring low power and high energy efficiency.

In this paper, we investigate how to fuse some special functions into an FeFET-based nonvolatile memory array. The common structural features of different FeFET-based circuits are extracted. Based on a common 3T cell design, we propose an FeFET-based multifunctional in-memory processing unit named FeMAT, standing for FeFET-based unit for computational memory, BCNN acceleration and TCAM. FeMAT is an FeFET-based memory array with each cell composed of an FeFET and two access transistors. FeMAT can function as not only a conventional memory, but also a computational memory, a BCNN accelerator or a TCAM array without changing the circuit structure. The contributions of this paper are summarized as follows.

- A unified FeFET-based 3T cell is proposed to support PIM operations, BCNN acceleration and TCAM, by exploring the structural similarities of the existing cell designs for each individual function.   
- Based on the elaborated memory cell design, we propose FeMAT, an in-memory processing unit that can act as either a conventional memory or specialized in-memory functions including PIM operations, BCNN acceleration and TCAM. As far as we know, this is the first time that an FeFET-based multifunctional memory array is proposed.   
- FeMAT is compared with a ReRAM-based equivalence as well as a TCAM and a BCNN accelerator based on CMOS devices. The results reveal the advantages of FeFETs. FeFETs have much lower programming power than ReRAMs, while FeMAT consumes lower energy than the ReRAM-based equivalence and the CMOS-based circuits in the TCAM and BCNN acceleration modes.

The rest of this paper is organized as follows. In Section II, we introduce some preliminaries of this work. The proposed FeMAT design is presented in detail in Section III. The proposed design is evaluated in Section IV. Finally Section V concludes the paper.

# II. PRELIMINARIES

In this section, we introduce some preliminaries including FeFETs, BCNNs and TCAMs as the background of this work. We first list the abbreviations of the line names used in the following contents in Table I.

# A. Ferroelectric Field-Effect Transistor

The structure of an FeFET is shown in Fig. 1a. FeFETs are compatible with conventional MOSFETs [4]. An FeFET
  - "[[FeFET]]"

TABLE I: Abbreviations and their full spellings.   

<table><tr><td>Abbreviation</td><td>Full spelling</td></tr><tr><td>BL</td><td>Bit line</td></tr><tr><td>DL</td><td>Data line</td></tr><tr><td>ML</td><td>Match line</td></tr><tr><td>RSL</td><td>Read select line</td></tr><tr><td>SL</td><td>Sense line</td></tr><tr><td>WL</td><td>Word line</td></tr><tr><td>WSL</td><td>Write select line</td></tr></table>

![](images/343ce3b308e669b252d709e5b07668f370a706c5074d6a80e3b743af9da1d0f0.jpg)  
(a)

![](images/b8c500d78ad9ce590f4897fcd8a59df427a8d7e86bf8dda4aa54bb27b2783f3e.jpg)  
(b)   
Fig. 1: FeFET background. (a) FeFET structure. (b) Simulated hysteresis curve.

is similar to a conventional MOSFET with a major difference of a ferroelectric material layer integrated in the gate stack of the underlying MOSFET. The behavior of an FeFET strongly depends on the ferroelectric layer material and its thickness. By properly selecting the thickness of the ferroelectric layer, a hysteresis loop in the $I_{\mathrm{DS}} - V_{\mathrm{G}}$ curve can be obtained [19] so as to introduce nonvolatility into the device.

A SPICE-compatible FeFET simulation model has been developed and calibrated based on fabricated devices [20]. Fig. 1b shows a simulated hysteresis curve using the SPICE model with a $5.4\mathrm{nm}$ ferroelectric layer thickness. The existence of the hysteresis curve reveals that the state of an FeFET can be read out by setting a proper $V_{\mathrm{G}}$ (e.g., $V_{\mathrm{G}} = 0\mathrm{V}$ in the case of Fig. 1b) and a fixed nonzero $V_{\mathrm{D}}$ . In this case, we can obtain two possible values of $I_{\mathrm{DS}}$ , i.e., $I_{\mathrm{ON}}$ or $I_{\mathrm{OFF}}$ , depending on the state of the FeFET (i.e., ON or OFF), which in turn, depends on the polarization of the ferroelectric layer.

To change the polarization of the ferroelectric layer which determines the state of an FeFET, we need to supply a positive or negative $V_{\mathrm{G}}$ pulse with a proper magnitude (e.g., 0.4V according to Fig. 1b) to the gate terminal. The applied $V_{\mathrm{G}}$ pulse produces a positive or negative electric field on the ferroelectric material, and changes its polarization accordingly. FeFETs are nonvolatile, meaning that the polarization of the ferroelectric layer maintains when powered off.

# B. FeFET-based Memory

An FeFET can store one bit so FeFETs can naturally construct nonvolatile memories. Compared with conventional static random-access memories (SRAMs), FeFETs not only save area but also offer the nonvolatility. Different FeFET-based nonvolatile memories have been proposed [9]–[11], as shown in Fig. 2. The 1T cell based memory design is denser but suffers from the sneak path problem, while the 2T and 3T cells based memory designs consume more area but do not have the sneak path problem. The 2T cell and 3T cell based memory designs both use an access transistor for each FeFET to select the programming row and also to maintain the polarization during read, while the latter uses one more access transistor in each cell for read selection.

![](images/26934669e9b91265280a88de3a5ace71e12cea14a61dd0b3d83805dbd9f9190c.jpg)  
Fig. 2: Existing FeFET-based memory designs $(2 \times 2$ examples). (a) 1T cell [9]. (b) 2T cell [10]. (c) 3T cell [11].

# C. FeFET-based BCNN Accelerator

BCNNs are proposed to reduce the energy consumption and also to improve the performance for neural networks. In BCNNs, both inputs and weights are binarized to $\pm 1$ [21], [22]. The output of an convolution operation is the binarized result of the inner product between a weight vector and an input vector. If $-1$ is mapped to 0, then a multiplication on the field of $\{1, -1\}$ is equivalent to an XNOR operation on the field of $\{0,1\}$ . As a result, a convolution operation can be converted to a series of XNOR operations followed by an accumulation (i.e., bit-counting) operation [21], [22]. The resulting integer is further binarized to be used for the next convolutional layer.

Fig. 3 shows an existing FeFET-based BCNN accelerator [16]. It is a crossbar structure where each cell is an FeFET-based XNOR gate which is composed of four transistors. The two FeFETs in an XNOR gate store complementary bits

![](images/f8482949c2725795568184786bc7bd01383b61e3e0c1922a418c428aee35bb3a.jpg)  
Fig. 3: Existing FeFET-based BCNN accelerator [16].

representing a weight parameter. Each XNOR gate in the crossbar performs an XNOR operation between the stored weight parameter and the input activation. The outputs are sensed from the SLs. Each column computes a convolution operation (i.e., an inner product operation).

# D. FeFET-based TCAM

A TCAM array performs parallel searches for a given piece of data against all the stored data, and returns information as to whether one or more matches occur. TCAMs have obvious utility in networking hardware and other applications, e.g., in routers, database search applications, and associative memories [23].

![](images/f2193e7e1d26097727ef8ded50b3facfb9d6c6853c06268cafb5ab770b87fd0e.jpg)  
Fig. 4: Existing FeFET-based TCAM cell [13].

An FeFET-based 6T TCAM cell has been proposed in [13], as shown in Fig. 4. The two FeFETs store complementary bits representing one bit for matching or two "0" bits representing the don't-care state. The input word for matching is applied on the DLs and their inverses. A TCAM array works in a dynamic circuit style. A clock cycle is partitioned into a precharge phase and an evaluation phase. In the precharge phase, the MLs are charged to high. In the evaluation phase, if at least one bit is mismatched, the mismatched cells pull down the ML voltage. If all bits are matched, the ML voltage keeps high. It is easy to understand that a TCAM cell actually performs an XNOR operation when the two FeFETs store complementary bits. When they both store "0" (representing the don't-care state), the cell always outputs a match. All TCAM rows perform the search operation in parallel so the latency is almost independent with the number of TCAM rows.

# III. FEMAT ARRAY

In this section, we present the proposed FeMAT in detail. We first give an overview of the cell and array designs, then we describe the four modes in detail.

# A. Cell Design

The aim of FeMAT is to integrate some special functions, including PIM operations, BCNN acceleration and TCAM, into an FeFET-based memory array, to construct a multifunctional nonvolatile memory. Thereby, when designing the basic cell, the features of the memory cell (Fig. 2b or 2c), the TCAM cell (Fig. 4) and the BCNN accelerator cell (Fig. 3) should be taken into account. They have a common feature on programming — an access transistor together with a WL (or WSL) and a BL is used for programming. But the read schemes are quite different. In this work, we unify the read schemes of the three

![](images/95cc5e274202f8ec136572214352c1a2d54c52d3954c8cee6761960ad0799b1c.jpg)  
Fig. 5: Basic cell design of FeMAT (2×2 example).

functions and propose a unified cell structure to support the desired functions in a unified memory array.

Fig. 5 shows the proposed basic cell of FeMAT. A memory cell is composed of three transistors. In order to make the cell compatible to the special functions other than memory, the 3T-based memory cell is different from all the existing memory cell designs (Fig. 2). The basic cells for TCAM and BCNN acceleration are both composed of two basic memory cells. In Fig. 5, the horizontal dashed box represents a TCAM cell consisting of two memory cells that store one bit and its inverse to represent one bit for TCAM matching. Since TCAM can operate on the don't-care state, in this case, "0" is stored in both memory cells. The vertical dotted box indicates a BCNN accelerator cell. When FeMAT is used as a BCNN accelerator, the basic cell in the vertical dotted box stores one bit and its inverse to represent a weight parameter.

The basic cells can be combined to form an array of any size, but a memory array still needs peripheral circuits and control signals to complete different functions and function switch, which are described below.

# B. Array Overview

Based on the proposed basic cells, we design the FeMAT array structure, as illustrated in Fig. 6. The core component is the FeFET-based memory array. The peripheral circuits include the read and write address decoders, the BL driver, the DL driver, the WL driver, the RSL driver, the SAs for the memory, PIM operations and BCNN acceleration, and the SAs for TCAM. In order to realize function switch, some transmission gates are also required to control the connections for the signals. In addition to the transmission gates explicitly shown in Fig. 6, there are also other transmission gates and multiplexers in the driver circuits used to select the correct signals in different operation modes. In a certain mode, unused components can be power gated to save power. For example, in the TCAM mode, the SAs used for the memory and BCNN modes can be power gated.

Note that Fig. 6 is a single memory array. In practice, multiple arrays together with some global address decoders, data buffers, etc. can form a complete memory. Different memory arrays may operate in different modes. In this paper

![](images/55d17927ec1084a67563a7d3dc73badb70ed3c433dc8f0ea34389cba6ef2b0ae.jpg)  
Fig. 6: Array design of FeMAT.

we stick on a single array instead of a complete memory architecture not only because the latter is neither the focus nor the main contribution of this work, but also because the conventional memory architecture is well known. In the following subsections, we will describe the four operation modes of FeMAT in detail.

# C. Memory and Computational Memory Modes

In the memory mode, FeMAT supports row-wise (i.e., wordwise) read and write (an additional column decoder/multiplexer can be added to support bit-wise read and write). In the computational memory mode, FeMAT supports some bit-wise operations and an addition operation between two rows. The two modes share the same datapath and SAs so we introduce them together. In the memory and computational memory modes, by controlling the $C_{\mathrm{TCAM}}$ signal (see Fig. 6), the TCAM SAs are disconnected and the voltage followers are connected.

For convenience, we show a memory cell in Fig. 7a. Each cell is composed of an FeFET, an access transistor for write (ATW) and an access transistor for read (ATR). The read and write operations are controlled by the two access transistors together with the corresponding lines (BL, WL, DL and RSL).

![](images/34f4da0a62831340a8e9b246b312a08007f2447f38bcf3eae44dcc13c81def50.jpg)

![](images/8658c7493e39b11920e6fcc269832aa1a6a7f5f0b13eb9ec25b39e74c3d79615.jpg)

![](images/d47ea5222eefc4de7166d04a4c380212d28a8b99c18aa8c764e268f921097f35.jpg)  
Fig. 7: Memory mode. (a) Memory cell of FeMAT. (b) Memory write. (c) Memory read.

1) Memory Write: As mentioned in Section II-A, programming an FeFET needs a positive or negative voltage pulse on the gate terminal. The data which need to be written into a row are given by the BLs. The WLs are used to select the programming row and only one WL can be activated by the write address decoder. The data specified by the BLs are written into the selected row in one step. The unselected rows are not affected since their WLs are "0" and the corresponding ATWs are turned off. The DLs are set to "0" during programming, which turn off the ATRs so there are no currents flowing through the FeFETs. Fig. 7b illustrates how programming is performed. The separated read and write paths and the programming mechanism significantly lower the programming power and the advantage of FeFETs in programming will be demonstrated by our experiments.

It is worth noting that programming is for not only the memory mode, but also the TCAM and BCNN acceleration modes. In the TCAM mode, we write data into the memory array for TCAM matching. In the BCNN acceleration mode, we write the weight parameters into the memory array.

2) Memory Read and PIM Operations: For anytime the memory is not being programmed, the FeFETs should maintain their states. To achieve this goal, the WLs are set to "1" and the BLs are set to "0". Such a setting for maintaining the FeFETs' states is for not only memory read, but also the TCAM and BCNN acceleration modes. For memory read operations, we activate one RSL, while for PIM operations, we activate two RSLs. A read voltage $V_{\mathrm{R}}$ is set to the activated RSL(s). In the TCAM mode, the RSLs act as MLs and they need to be disconnected from the RSL driver. Hence, switches are required between the RSLs (i.e., MLs) and the RSL driver. Transmission gates can realize this goal. However, transmission gates cause RSL voltage drop in the memory mode. To avoid this problem, we instead use a voltage follower for each RSL, as shown in Fig. 6. The DLs are set to "1" so that the ATRs are turned on. If an FeFET in an activated row stores "1", it contributes a current to the corresponding column SL. Fig. 7c illustrates a memory read operation. The SAs which connect to the SLs convert the currents to voltage outputs. If two rows are activated in the computational memory mode, they both contribute currents to the SLs so that we are able to read out the PIM operation results by the SAs.

Fig. 8 shows the SA design for both memory read and PIM operations. The operational amplifier (OpAmp) connected to the SL converts the SL current to voltage. This current-to-voltage converter also clamps the SL voltage to 0. The

![](images/d5a699f291e1a825bd20c4ce3ee099f3714bd9bf9d8582cb5035dbfba76aff71.jpg)  
Fig. 8: SA for memory read and PIM operations.

converted voltage is fed into two voltage comparators with different reference voltages ( $V_{\mathrm{OR}}$ and $V_{\mathrm{AND}}$ ). One comparator is for memory read and the two comparators together are for PIM operations. As shown in Fig. 8, our SA design supports bit-wise AND, NAND, OR, NOR, XOR and XNOR operations between two memory rows. In addition, with a few additional logic gates, we can also perform a word-wise addition operation between two rows. Such a PIM mode eliminates the data movement between processors and memories if the desired operations are supported by the PIM mode.

# D. BCNN Acceleration Mode

In BCNNs, we have only two values: 1 and -1 [21], [22]. As mentioned in Section II-C, a multiplication on the field of $\{-1,1\}$ can be mapped to an XNOR operation on the field of $\{0,1\}$ . That is, $-1$ is represented by 0. Such XNOR operations can be easily implemented by BCNN accelerator cells.

When FeMAT works as a BCNN accelerator, all WLs are set to "1" and all BLs are set to "0" to maintain the FeFETs' states. All DLs are set to "1" to turn on the ATRs. A BCNN accelerator cell is composed of two adjacent memory cells in the same column, as shown in Fig. 9. The two FeFETs in a BCNN accelerator cell store complementary bits to represent one weight parameter. The input activations are provided by the RSLs. Different from the memory mode where only one or two RSLs are activated, here all RSLs are activated. One bit of the input activations and its inverse are applied to two neighboring RSLs which correspond to the same BCNN accelerator cell. A BCNN accelerator cell of FeMAT implements an XNOR operation between the input activation and the stored weight parameter. As marked in Fig. 9, if the two FeFETs respectively store $w_{i}$ and $\overline{w_{i}}$ , and the two RSLs respectively provide $x_{i}$ and $\overline{x_{i}}$ , then this cell computes $x_{i} \odot w_{i}$ . Similar to

![](images/609e30e01c6da98744cd7381374585d490a4a1e3355ee4b68d3819fa5a1c3d3c.jpg)  
Fig. 9: Equivalent circuit in BCNN acceleration mode (for one column).

the memory mode, the XNOR result contributes a current to the column SL.

Considering a column, it corresponds to a kernel filter in a convolutional neural network and the SL current is the analog result of a convolution operation, namely, the inner product between the input activation vector and the weight vector stored in the column (i.e., $\sum x_{i} \odot w_{i}$ in Fig. 9). Different columns store the weight parameters of different kernel filters but share the same input activations. For an $M \times N$ memory array, we can compute at most $N$ convolution operations at a time while the number of input activations can be up to $\frac{M}{2}$ . To obtain the binarized results which are the input activations for the next convolutional layer, we use SAs which are almost identical to the memory read SAs, as shown in Fig. 9. An SA is composed of two OpAmps where one is a current-to-voltage converter and the other is a voltage comparator. The operation process in the BCNN acceleration mode is similar to that of reading data when FeMAT works in the memory mode. The major difference is the number of activated rows. In addition, in the SAs, the resistance for current-voltage conversion and the reference voltage for comparisons are also different.

Since the two memory cells in a BCNN accelerator cell are in different rows, programming a weight parameter requires two clock cycles. Considering that weights are fixed after training and do not change during inferences, the programming operation in the BCNN acceleration mode is just a one-time work so the programming latency would not be a performance bottleneck.

![](images/67a4116afd0b03a9b9de7a05733d7b2351c915fd67ba8b25822f956356ea1180.jpg)  
E. TCAM Mode   
Fig. 10: Equivalent circuit in TCAM mode (for one row).

In the TCAM mode, by controlling the $C_{\mathrm{TCAM}}$ signal (see Fig. 6), the MLs are connected to the TCAM SAs and the voltage followers are disconnected to the array and power gated, so that the MLs can reflect the TCAM results. All WLs are set to "1" and all BLs are set to "0" so that all FeFETs maintain their states. The SLs are grounded. Remember that a TCAM cell is composed of two adjacent memory cells along the horizontal direction, as shown in Fig. 5. We show the equivalent circuit of a row operating in the TCAM mode in Fig. 10, where only one TCAM cell is shown and others are omitted. The two memory cells in a TCAM cell store complementary bits representing one bit for matching or both "0" representing the don't-care state. The input word for matching is given through the DLs. Since the DLs are vertical

lines, the input word is compared in parallel with all rows of data stored in the array. The matching result of each row is read from the SA output which reflects the ML voltage.

We design a dynamic logic style SA for the TCAM mode, meaning that a clock cycle has two phases: precharge (CLK = 0) and evaluation (CLK = 1). During a precharge phase, the MLs are precharged to $V_{\mathrm{DD}}$ though the $\mathrm{M_C}$ transistor. During an evaluation phase, the input word given by the DLs are compared with the words stored in the array. Each TCAM cell implements an XNOR function, if the two FeFETs in the TCAM cell store complementary bits. For example, as marked in Fig. 10, if $s_i$ is "0" and $s_i'$ is "1", indicating that the TCAM cell stores "0". If $y_i$ is "1", then the right-side path in the TCAM cell is ON, indicating a mismatch. There will be an ML-to-ground path in the corresponding TCAM cell if a mismatch happens. Any ML-to-ground path pulls down the ML voltage to ground. If the two FeFETs in one TCAM cell both store "0", indicating the don't-care state, then the two paths are always OFF regardless of the input data, so the TCAM cell always produces a match. If no TCAM cell in a row outputs a mismatch, the ML keeps high, indicating a match. Without loss of generality, if a TCAM cell performs a boolean function of match $(y_i, s_i, s_i')$ , then an ML performs a boolean function of $\prod \text{match}(y_i, s_i, s_i')$ . The transistor $M_U$ (with a minimum width) and the feedback inverter form a level restorer which is used for maintain the ML voltage for a match. The latch in the TCAM SA is used to maintain the output during the precharge phases, as the ML voltage during the precharge phases does not reflect the correct matching result.

If we force the two FeFETs in a TCAM cell to store complementary bits, then it is the content-addressable memory (CAM) mode. The only difference between CAM and TCAM is that the former cannot handle the don't-care state. More interestingly, the TCAM mode can also be used as a column-memory mode that supports column-wise memory read. If we activate only one DL and set all the other DLs to "0", and the TCAM SAs work in the same way as in the TCAM mode, then the SA outputs are the bits stored in the activated column. This is an auxiliary function of FeMAT. Hence, FeMAT supports both row-wise read and column-wise read.

# F. Summary

FeMAT is an FeFET-based memory array which can not only act as a nonvolatile memory, but also perform some in-memory functions including PIM operations, BCNN accelerations and TCAM-based searching. We have described the circuit structure and all functions of FeMAT in detail. Table II summarizes the voltage setups of the lines in all modes. Multiplexers and/or transmission gates are needed to select the proper signals according to the operation mode. The function of FeMAT can be configured online by controlling the multiplexers and/or the transmission gates. The circuitries to realize this goal are quite trivial so we do not show them here. The simulation results shown in the next section include the impact of these peripheral circuits.

TABLE II: Voltage setups of all signals in all modes.   

<table><tr><td></td><td>Write</td><td>Read/PIM</td><td>BCNN mode</td><td>TCAM mode</td></tr><tr><td>BL</td><td>Data (±VDD)</td><td>0</td><td>0</td><td>0</td></tr><tr><td>DL</td><td>0</td><td>VDD</td><td>VDD</td><td>Data (VDD/0)</td></tr><tr><td>ML/RSL</td><td>0</td><td>VRa/0b</td><td>Data (VR/0)</td><td>For sensing</td></tr><tr><td>SL</td><td>0</td><td>0 (for sensing)</td><td>0 (for sensing)</td><td>0</td></tr><tr><td>WL</td><td>VDDa/-VDDb</td><td>VDD</td><td>VDD</td><td>VDD</td></tr></table>

a For selected row(s).   
b For unselected rows.

![](images/f60b6ff1b85b179e986c3baf6f412aa3b663e72e29f6f154466f7d0e9ce1431d.jpg)  
Fig. 11: Basic cells of ReMAT (2×2 example).

# IV. SIMULATION RESULTS

We have implemented and evaluated FeMAT including all the peripheral circuits with HSPICE. We use the $45\mathrm{nm}$ predictive technology model [24] as the MOSFET model and the FeFET model proposed in [20]. The memory array size is $1024\times 64$ . $V_{\mathrm{DD}} = 1\mathrm{V}$ and $V_{\mathrm{R}} = 0.1\mathrm{V}$ . We use a ReRAM-based equivalence as the baseline for comparisons. Similar to FeMAT, the ReRAM-based equivalence can perform the same functions as FeMAT and is named ReMAT. The basic cells of ReMAT are shown in Fig. 11. Each cell is composed of a ReRAM and an access transistor. Although a ReRAM-based cell has one less device than an FeFET-based cell, access transistors for ReRAMs must be wider to provide a large programming current (typically $\geq 50 - 100\mu \mathrm{A}$ ) [25]. For $45\mathrm{nm}$ , the W/L ratio of access transistors for ReRAM should be 3 [26]. Different from ReRAMs which are programmed by current, FeFETs are programmed by voltage, so that the width of access transistors for FeFETs can be the minimum. In our experiments, the W/L ratios of the access transistors for FeFETs and ReRAMs are 1 and 3, respectively. We use a 2V programming voltage for ReRAMs [25].

Since the resistance of ReRAMs can be arbitrarily selected in a reasonable range and the power consumption of ReMAT strongly depends on the resistance of ReRAMs, it will bring high power consumption if the ON-state resistance is low. To make fair comparisons between FeMAT and ReMAT and also to demonstrate the essential advantages of FeFETs in a multifunctional memory array, the ON-state resistance of ReRAMs is selected such that the read current of a ReRAM is identical to that of an FeFET. This produces $5.2\mathrm{K}\Omega$ for the ON-state resistance. The OFF-state resistance is $200\times$ of

![](images/8f45d6a3c64c21feff380b8efe13e2ce4827cf6b3997d28be7fc0670fd241157.jpg)  
(a)

![](images/920b4a2d1da5b0602eab12305677679811c8f43395a296545486c554e22405d3.jpg)  
(b)   
Fig. 12: CMOS-based basic cells. (a) BCNN accelerator cell. (b) TCAM cell.

the ON-state resistance. This range (i.e., $5.2\mathrm{K}\Omega$ to $1.04\mathrm{M}\Omega$ ) conforms to the measured ReRAM resistance range [27]. Different from ReRAMs, FeFETs offer a much higher OFF-state resistance to ON-state resistance ratio and the ratio can be $10^{6}$ [5], [7]. The advantages of the small access transistors and the high OFF-state resistance to ON-state resistance ratio of FeFETs will be demonstrated by our experiments.

For the TCAM and BCNN acceleration modes, we also compare FeMAT with a CMOS-based TCAM and a CMOS-based BCNN accelerator, respectively. The CMOS-based BCNN accelerator cell and TCAM cell are shown in Fig. 12. We will show the power consumption of two cases which are with and without the peripheral circuits, respectively, where the peripheral circuits include the address decoders, the drivers and the SAs in Fig. 6. Remember that unused components of FeMAT and ReMAT are power gated (e.g., the TCAM SAs are power gated when FeMAT is not in the TCAM mode) to reduce the power consumption.

# A. Memory and Computational Memory Modes

![](images/148917cb3aa9fe5473b4b3ceccd2882a7c4e2ba39205894a56f21aa56d62fbf1.jpg)  
Fig. 13: Programming power comparison.

Fig. 13 compares the programming power when one memory row is being programmed (but the power values are for the entire array with or without the peripheral circuits, instead of the single programming row). For both FeMAT and ReMAT, the power consumed by the peripheral circuits is ignorable in programming. ReMAT consumes an order of magnitude higher programming power than FeMAT. This is mainly due to the different programming mechanisms. ReRAMs are programmed by the large currents flowing through them while FeFETs are programmed by their gate voltages. The programming power of an FeFET is mainly consumed by charging the ferroelectric layer of the FeFET which is very low.

![](images/ecd75074cf58a294de2dec132f6352bc3b5f7be01645269558cad8060c52dc10.jpg)  
Fig. 14: Read power and PIM power comparisons.

![](images/3b995d1a603214c1372b41b1c5f0d3eef1b7aa6160766f7ec465a651cc7a54d0.jpg)  
Fig. 15: Read latency and PIM latency comparisons.

Considering that the programming latency of FeFETs and ReRAMs are both at the magnitude of 10ns while ReRAMs have a $2 - 3\times$ shorter programming latency than FeFETs [7], [28], [29], the programming energy of FeMAT is about $3 - 5\times$ lower than that of ReMAT.

Fig. 14 compares the memory read power and the PIM operation power. Different from programming, for memory reads and PIM operations, the peripheral circuits including the SAs, the address decoders and the drivers consume most of the power. In any case, the power consumption of FeMAT and ReMAT are almost identical. The tiny power difference is due to the different OFF-state resistance to ON-state resistance ratios of FeFETs and ReRAMs. Fig. 15 compares the memory read latency and the PIM operation latency. The read latency of FeMAT and ReMAT are also almost identical, while FeMAT has slightly longer $(< 3\%)$ latency than ReMAT. Note that all the peripheral circuits have been taken into account when evaluating the latency.

# B. BCNN Acceleration Mode

Table III compares the power, latency and energy in the BCNN acceleration mode. Since the 0/1 distributions of the inputs and weights can affect the latency and the power consumption, we randomly generate a number of sets of

TABLE III: Power, latency and energy comparisons in BCNN acceleration mode.   

<table><tr><td></td><td>Power (mW) 
w/ periph. ckt</td><td>Power (mW) 
w/o periph. ckt</td><td>Latency (ns)</td><td>Energy (pJ)</td></tr><tr><td>FeMAT</td><td>31.546</td><td>25.188</td><td>1.63</td><td>51.42</td></tr><tr><td>ReMAT</td><td>31.656</td><td>25.320</td><td>1.70</td><td>53.82 (1.05×)</td></tr><tr><td>CMOS Accelerator</td><td>63.742</td><td>57.958</td><td>1.43</td><td>91.15 (1.77×)</td></tr></table>

TABLE IV: Power, latency and energy comparisons in TCAM mode.   

<table><tr><td></td><td>Power (mW) 
w/ periph. ckt</td><td>Power (mW) 
w/o periph. ckt</td><td>Latency (ps)</td><td>Energy (fJ)</td></tr><tr><td>FeMAT</td><td>4.656</td><td>1.180</td><td>81</td><td>377.14</td></tr><tr><td>ReMAT</td><td>9.206</td><td>2.437</td><td>86</td><td>791.72 (2.10×)</td></tr><tr><td>CMOS TCAM</td><td>6.393</td><td>3.278</td><td>74</td><td>473.08 (1.25×)</td></tr></table>

inputs and weights and show the average results. The power consumptions of FeMAT and ReMAT are almost identical, while ReMAT consumes slightly higher power than FeMAT, due to the low OFF-state resistance to ON-state resistance ratio of ReRAMs. The latency of ReMAT is a little longer than that of FeMAT, which in turn, makes the energy consumption of ReMAT $5\%$ higher.

Different from ReMAT, the CMOS-based BCNN accelerator consumes much higher power. The high power consumption is mainly due to the static power of the SRAMs, which does not exist in ReMAT and FeMAT. The CMOS-based BCNN accelerator has the shortest latency. However, if we compare the energy consumption, the CMOS-based BCNN accelerator consumes $1.77 \times$ higher energy than FeMAT.

# C. TCAM Mode

Table IV compares FeMAT with ReMAT in the TCAM mode. These numbers are also the average results of a number of runs on randomly generated data. Different from the BCNN acceleration mode, FeMAT shows about $2 \times$ lower power consumption and $2.1 \times$ lower energy consumption in the TCAM mode. The high improvements come from the small width of the access transistors used in FeMAT. The large access transistors used in ReMAT lead to large parasitic capacitance. Since the parasitic capacitance affects the MLs' parasitic capacitance in the TCAM mode, the power consumption and the latency of ReMAT are both increased.

The CMOS-based TCAM consumes about $3 \times$ higher array power mainly due to the static power of the SRAMs. The total power of the CMOS-based TCAM is $37\%$ higher. The latency of the CMOS-based TCAM is the shortest among the three TCAMs. When comparing the energy consumption, FeMAT still has the lowest energy consumption.

# V. CONCLUSIONS

In this work, we propose a unified FeFET-based memory cell structure such that PIM operations, BCNN operations and TCAM can be seamlessly fused into the unified cell structure. Based on that, we propose FeMAT, an FeFET-based multifunctional nonvolatile memory array which can support the aforementioned functions inside the memory. HSPICE simulations with a calibrated FeFET model demonstrate the advantages of FeFETs including the much lower programming than ReRAMs and the lower energy consumption in the BCNN acceleration and TCAM modes compared with ReRAM- and CMOS-based circuits.

# REFERENCES

[1] D. Patterson, T. Anderson, N. Cardwell, R. Fromm, K. Keeton, C. Kozyrakis, R. Thomas, and K. Yelick, "A case for intelligent RAM," IEEE Micro, vol. 17, no. 2, pp. 34-44, March 1997.   
[2] S. Han, X. Liu, H. Mao, J. Pu, A. Pedram, M. A. Horowitz, and W. J. Dally, "EIE: Efficient Inference Engine on Compressed Deep Neural Network," in 2016 ACM/IEEE 43rd Annual International Symposium on Computer Architecture (ISCA), June 2016, pp. 243-254.   
[3] H.-W. Tseng, Y. Liu, M. Gahagan, J. Li, Y. Jing, and S. Swanson, "Gullfoss: Accelerating and Simplifying Data Movement among Heterogeneous Computing and Storage Resources," Department of Computer Science and Engineering, University of California, San Diego, Tech. Rep. CS2015-1015, 2015. [Online]. Available: http://csetechrep.ucsd.edu/Dienst/UI/2.0/Describe/ncstrl.ucsd_cse/CS2015-1015   
[4] M. Trentzsch, S. Flachowsky, R. Richter, J. Paul, B. Reimer, D. Utess, S. Jansen, H. Mulaosmanovic, S. Miller, S. Slesazeck, J. Ocker, M. Noack, J. Miller, P. Polakowski, J. Schreiter, S. Beyer, T. Mikolajick, and B. Rice, "A 28nm HKMG super low power embedded NVM technology based on ferroelectric FETs," in 2016 IEEE International Electron Devices Meeting (IEDM), Dec 2016, pp. 11.5.1-11.5.4.   
[5] P. Sharma, K. Tapily, A. K. Saha, J. Zhang, A. Shaughnessy, A. Aziz, G. L. Snider, S. Gupta, R. D. Clark, and S. Datta, "Impact of total and partial dipole switching on the switching slope of gate-last negative capacitance FETs with ferroelectric hafnium zirconium oxide gate stack," in 2017 Symposium on VLSI Technology, June 2017, pp. T154–T155.   
[6] K. Ni, P. Sharma, J. Zhang, M. Jerry, J. A. Smith, K. Tapily, R. Clark, S. Mahapatra, and S. Datta, "Critical Role of Interlayer in Hf0.5Zr0.5O2Ferroelectric FET Nonvolatile Memory Performance," IEEE Transactions on Electron Devices, vol. 65, no. 6, pp. 2461-2469, June 2018.   
[7] J. Müller, T. S. Boscke, S. Müller, E. Yurchuk, P. Polakowski, J. Paul, D. Martin, T. Schenk, K. Khullar, A. Kersch, W. Weinreich, S. Riedel, K. Seidel, A. Kumar, T. M. Arruda, S. V. Kalinin, T. Schlosser, R. Boschke, R. van Bentum, U. Schröder, and T. Mikolajick, "Ferroelectric hafnium oxide: A CMOS-compatible and highly scalable approach to future ferroelectric memories," in 2013 IEEE International Electron Devices Meeting, Dec 2013, pp. 10.8.1-10.8.4.   
[8] A. Aziz, E. T. Breyer, A. Chen, X. Chen, S. Datta, S. K. Gupta, M. Hoffmann, X. S. Hu, A. Ionescu, M. Jerry, T. Mikolajick, H. Mulaosmanovic, K. Ni, M. Niemier, I. O'Connor, A. Saha, S. Slesazeck, S. K. Thirumala, and X. Yin, "Computing with ferroelectric FETs: Devices, models, systems, and applications," in 2018 Design, Automation Test in Europe Conference Exhibition (DATE), March 2018, pp. 1289-1298.   
[9] A. Sharma and K. Roy, "1T Non-Volatile Memory Design Using Sub-10nm Ferroelectric FETs," IEEE Electron Device Letters, vol. 39, no. 3, pp. 359-362, March 2018.   
[10] S. George, K. Ma, A. Aziz, X. Li, A. Khan, S. Salahuddin, M. Chang, S. Datta, J. Sampson, S. Gupta, and V. Narayanan, "Nonvolatile memory design based on ferroelectric FETs," in 2016 53nd ACM/EDAC/IEEE Design Automation Conference (DAC), June 2016, pp. 1-6.   
[11] D. Reis, M. Niermie, and X. S. Hu, "Computing in Memory with FeFETs," in International Symposium on Low Power Electronics and Design, ser. ISLPED '18, 2018, pp. 24:1-24:6.   
[12] X. Yin, K. Ni, D. Reis, S. Datta, M. Niemier, and X. S. Hu, "An Ultradense 2FeFET TCAM Design based on a Multi-Domain FeFET Model," IEEE Transactions on Circuits and Systems II: Express Briefs, pp. 1-1, 2018.   
[13] X. Yin, X. Chen, M. Niemier, and X. S. Hu, "Ferroelectric FETs-Based Nonvolatile Logic-in-Memory Circuits," IEEE Transactions on Very Large Scale Integration (VLSI) Systems, vol. 27, no. 1, pp. 159-172, Jan 2019.   
[14] X. Chen, M. Niemier, and X. S. Hu, "Nonvolatile Lookup Table Design Based on Ferroelectric Field-Effect Transistors," in 2018 IEEE International Symposium on Circuits and Systems (ISCAS), May 2018, pp. 1-5.   
[15] X. Chen, K. Ni, M. T. Niemier, Y. Han, S. Datta, and X. S. Hu, "Power and Area Efficient FPGA Building Blocks Based on Ferroelectric FETs," IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 66, no. 5, pp. 1780-1793, May 2019.   
[16] X. Chen, X. Yin, M. Niemier, and X. S. Hu, "Design and optimization of FeFET-based crossbars for binary convolution neural networks," in

2018 Design, Automation Test in Europe Conference Exhibition (DATE), March 2018, pp. 1205-1210.   
[17] D. Wang, S. George, A. Aziz, S. Datta, V. Narayanan, and S. K. Gupta, "Ferroelectric Transistor Based Non-Volatile Flip-Flop," in Proceedings of the 2016 International Symposium on Low Power Electronics and Design, 2016, pp. 10-15.   
[18] I. Yoon, M. Chang, K. Ni, M. Jerry, S. Gangopadhyay, G. Smith, T. Hamam, V. Narayanan, J. Romberg, S. Lu, S. Datta, and A. Raychowdhury, "A FeFET Based Processing-In-Memory Architecture for Solving Distributed Least-Square Optimizations," in 2018 76th Device Research Conference (DRC), June 2018, pp. 1-2.   
[19] S. George, A. Aziz, X. Li, J. Sampson, S. Datta, S. Gupta, and V. Narayanan, "Ncfet based logic for energy harvesting systems," in SRC TECHCON, 2015.   
[20] A. Aziz, S. Ghosh, S. Datta, and S. K. Gupta, "Physics-Based Circuit-Compatible SPICE Model for Ferroelectric Transistors," IEEE Electron Device Letters, vol. 37, no. 6, pp. 805-808, June 2016.   
[21] M. Courbariaux, I. Hubara et al., "Binarized Neural Networks: Training Deep Neural Networks with Weights and Activations Constrained to +1 or -1," arXiv preprint arXiv:1602.02830, 2016.   
[22] M. Rastegari et al., "XNOR-Net: ImageNet Classification Using Binary Convolutional Neural Networks," in ECCV, 2016, pp. 525-542.   
[23] R. Karam, R. Puri, S. Ghosh, and S. Bhunia, “Emerging Trends in Design and Applications of Memory-Based Computing and Content-Addressable Memories,” Proceedings of the IEEE, vol. 103, no. 8, pp. 1311–1330, Aug 2015.   
[24] ASU, “Predictive Technology Model,” 2011. [Online]. Available: http://ptm.asu.edu/   
[25] C. Xu, X. Dong, N. P. Jouppi, and Y. Xie, “Design implications of memristor-based RRAM cross-point structures,” in 2011 Design, Automation Test in Europe, March 2011, pp. 1-6.   
[26] S. Yu, Resistive Random Access Memory (RRAM): From Devices to Array Architectures. San Rafael, California, 2016.   
[27] H. Chang, H. Li, C. W. Liu, F. Chen, and M. Tsai, "Physical mechanism of HfO2-based bipolar resistive random access memory," in Proceedings of 2011 International Symposium on VLSI Technology, Systems and Applications, April 2011, pp. 1-2.   
[28] J. Müller, E. Yurchuk, T. Schlosser, J. Paul, R. Hoffmann, S. Miller, D. Martin, S. Slesazeck, P. Polakowski, J. Sundqvist, M. Czernohorsky, K. Seidel, P. Kcher, R. Boschke, M. Trentzsch, K. Gebauer, U. Schröder, and T. Mikolajick, "Ferroelectricity in HfO2enables nonvolatile data storage in 28 nm HKMG," in 2012 Symposium on VLSI Technology (VLSIT), June 2012, pp. 25-26.   
[29] S. Sheu, M. Chang, K. Lin, C. Wu, Y. Chen, P. Chiu, C. Kuo, Y. Yang, P. Chiang, W. Lin, C. Lin, H. Lee, P. Gu, S. Wang, F. T. Chen, K. Su, C. Lien, K. Cheng, H. Wu, T. Ku, M. Kao, and M. Tsai, "A 4Mb embedded SLC resistive-RAM macro with 7.2ns read-write random-access time and 160ns MLC-access capability," in 2011 IEEE International Solid-State Circuits Conference, Feb 2011, pp. 200-202.