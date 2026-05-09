---
title: "Attention-in-Memory for Few-Shot Learning with Configurable Ferroelectric FET"
date: "2021-01-18"
year: "2021"
journal: "ACM Asia and South Pacific Design Automation Conference (ASPDAC)"
doi: "10.1145/3394885.3431526"
abstract: "Attention-in-Memory (AiM), a computing-in-memory (CiM) design, is introduced"
abstract_cn: "Attention-in-Memory (AiM) 是一种存内计算设计，用于实现记忆增强神经网络的注意力层。AiM 由基于铁电场效应晶体管的存储器阵列以及实现可配置功能的"
keywords:
  - "[[Ferroelectric]]"
  - "[[In-memory computing]]"
cite: "[1] Reis D, Laguna A F, Niemier M, et al. Attention‑in‑memory for few‑shot"
aiSum: "AiM 存内计算设计：可配置 FeFET 阵列，实现 MANN 注意力层，5-way 5-shot Omniglot 任务精度 95.14%，优于现有加速器。"
confidence: "medium"
wiki_concepts:
  - "[[FeFET]]"
  - "[[Ferroelectric]]"
  - "[[In-memory computing]]"
---

# Attention-in-Memory for [[Few-shot learning]] Attention-in-Memory for Few-Shot Learning

Dayane Reis

University of Notre Dame

Notre Dame, IN, USA

dreis@nd.edu

Michael Niemier

University of Notre Dame

Notre Dame, IN, USA

mniemier@nd.edu

Ann Franchesca Laguna

University of Notre Dame

Notre Dame, IN, USA

alaguna@nd.edu

Xiaobo Sharon Hu

University of Notre Dame

Notre Dame, IN, USA

shu@nd.edu

# ABSTRACT

Attention-in-Memory (AiM), a computing-in-memory (CiM) design, is introduced to implement the attentional layer of Memory Augmented Neural Networks (MANNs). AiM consists of a memory array based on [[ferroelectric]] FETs ([[FeFET]]) along with CMOS peripheral circuits implementing configurable functionalities, i.e., it can be dynamically changed from a ternary content-addressable memory (TCAM) to a general-purpose (GP) CiM. When compared to state-of-the art accelerators, AiM achieves comparable end-to-end speed-up and energy for MANNs, with better accuracy (95.14% v.s. 92.21%, and 95.14% v.s. 91.98%) at iso-memory size, for a 5-way 5-shot inference task with the Omniglot dataset.

# ACM Reference Format:

Dayane Reis, Ann Franchesca Laguna, Michael Niemier, and Xiaobo Sharon Hu. 2021. Attention-in-Memory for Few-Shot Learning with Configurable Ferroelectric FET Arrays. In 26th Asia and South Pacific Design Automation Conference (ASPDAC ’21), January 18–21, 2021, Tokyo, Japan. ACM, New York, NY, USA, 6 pages. https://doi.org/10.1145/3394885.3431526

# 1 INTRODUCTION

Memory augmented neural networks (MANNs) [1, 2] is a prevalent solution to few-shot learning. However, the attentional layer accounts for over 79% of the total execution time of MANNs [3], requiring a large volume of data transfers between processing units and the memory. To address this problem, hardware-friendly attentional layers for MANNs have been proposed in previous works [3–6]. Such accelerators often employ Compute-in-Memory (CiM) architectures, which reduce the amount of data transfers in a computer system by performing a subset of operations in memory. In this regard, either a Ternary Content Addressable Memory (TCAM) is used [4], or modifications are made to the memory cells/the circuits in the memory periphery in order to enable general-purpose (GP) logic/arithmetic [3, 5].

Configurable memories are memory arrays that have multiple operation modes, e.g., they can work as as regular random access memories (RAMs), TCAMs, general-purpose computing-inmemory (GP-CiM), [[crossbar]]s, etc. The operation mode can be dynamically configured. For instance, with the same piece of hardware,

one can perform searches in a TCAM mode, and then use the GP-CiM mode to perform additional computation on the result, e.g., bitwise logic, additions between memory words. Such configurable memories can be good candidates for accelerating MANNs.

In this work, we introduce Attention-in-Memory (AiM), a configurable CiM design based on FeFETs for hardware-friendly execution of the attentional layer of MANNs. AiM consists of a unified memory array based on ferroelectric field-effect transistor (FeFET) that employs 1T+1FeFET memory cells. The proposed array can have its functionality dynamically configured to a TCAM or a GP-CiM. Such configurable CiM design can support regular random-access memory (RAM), and TCAM and GP-CiM functions without requiring redundant storage of memory entries. Compared to existing design based on 2T+1FeFET memory cells (FeMAT [7]), our configurable CiM reduces the array area and associated parasitic components (resistance and capacitance), therefore enabling lower power consumption and shorter access times. In summary, our paper makes the following contributions:

• We propose AiM, an architecture for MANNs based on a configurable CiM array with dual TCAM/GP modes that employ 1T+1FeFET memory cells;   
• We design compact CiM peripheral circuits, which make use of supply gating techniques to reduce both the dynamic and stand-by power consumption;   
• We present and evaluate a real use case for configurable CiM arrays, i.e., in MANNs.

We evaluate the three different modes of AiM, i.e., when the array is configured to (i) work as a RAM, (ii) perform searches, or (iii) to compute GP bitwise logic and arithmetic operations between memory words. At the array level, we achieve 19.96× (1.33×) average improvements in the energy (delay) across all operations when compared to another FeFET-based configurable array (Fe-MAT [7]), with the same technology node (45nm) and array size (1024×64). The lower power of AiM come from its denser memory cells, less/smaller-sized peripheral circuitry, and the application of leakage reduction techniques (i.e., supply gating)1. At the application level, we compare the latency, energy and accuracy of AiM with previous accelerators for the attentional layer of MANNs [3, 6] at iso-memory size. When compared to [3], AiM achieves similar end-to-end delay, energy, and higher accuracy for MANNs with a $L _ { \infty } { + } L _ { 1 }$ distance metric (95.14% v.s. 91.98%). When compared to [6], AiM achieves better accuracy (95.14% v.s. 92.21%), with same end-to-end delay and energy.

![](images/405266993eea8b334f06c42904917059a980180b62c3a3ccdd522624d764626c.jpg)  
Figure 1: (a) An example of few-shot learning classification that uses MANNs. (b) The GPGPU run time distribution of MANNs during training and inference, for the Omniglot dataset [3].

# 2 BACKGROUND

In this section, we discuss the basic concepts on MANNs. We also introduce the FeFET device and review previous work.

# 2.1 Few-Shot Learning and Memory Augmented Neural Networks

Few-shot learning enables a NN to learn new classes from just a few examples without extensive re-training. In few-shot learning, a support set consists of ?? × ?? new images, i.e., ?? examples of images belonging to each one of the ?? classes in the support set. The support set is presented to a NN for training. Then, query images from among the ?? classes are presented. We call this classification a ??-way ??-shot. The concept of few-shot learning is illustrated by the example in Fig. 1(a). (Here, ??=4 and ??=1; the query is most similar to the second image of the support set.)

Memory Augmented Neural Networks (MANNs) are one of the most popular implementations for few-shot learning classification. A MANN is comprised of an attentional layer, i.e., a memory unit that stores the relevant features of a training set, which can be retrieved based on their similarity with a query vector. This process is illustrated in Fig. 1(a). During inference, a neural network is used to obtain the feature embedding of a query. Classification is enabled by two main operations in the memory unit: (i) the nearest-neighbor search and (ii) the memory updates.

To perform a nearest-neighbor search operation, a distance metric is required. The cosine distance is commonly used by GPGPU based implementations of MANNs. However, calculating a cosine distance requires a significant amount of computationally-expensive operations, $\mathrm { e . g . }$ , divisions and square roots, which has motivated the search for computationally efficient alternatives for distance metrics, e.g., the Manhattan $( \check { L _ { 1 } } )$ and the Chebyshev $\left( L _ { \infty } \right)$ metrics.

Memory updates ensure that representations of classes for a neural network are stored and replaced2 (if needed) in the memory unit [8, 10]. When the feature vectors of a ??-way ??-shot support set are presented to the attentional layer, the average between each example in the support set and the entries already present in the memory unit results in new class representations. These representations are written to the memory unit. Fig. 1(b) shows the breakdown of operations for MANNs during training and inference, for a 5-way 5-shot classification task with the Omniglot dataset.

![](images/54223086e5498740c5501ab8e77b30dcf20b81412d9f00921808aa76f59366bf.jpg)  
Figure 2: (a) Equivalent circuit and physical structure of an FeFET. (b) Applied gate waveform for FeFET characterization. (c) Experimentally measured and (d) simulated I-V characteristics of a FeFET device. Hysteresis shift by body biasing or gate metal work function engineering is possible (figure from [11]).

# 2.2 The FeFET device

A FeFET is an emerging device that can work as both a switch and storage element. A FeFET-based memory cell has virtually zero leakage power (due to device’s non-volatility), which makes FeFET-based memories competitive alternatives to conventional CMOS-based static RAMs (SRAMs). A FeFET is similar to a MOSFET with a layer of ferroelectric (FE) material (commonly, hafnium zirconium oxide (HZO)) added to the MOSFET’s gate stack. The equivalent circuit of a FeFET (Fig. 2(a)) shows the capacitances $C _ { F E }$ and $C _ { C M O S }$ , i.e., the FE layer and the CMOS capacitances, respectively. Hysteresis arises from the coupling between these two capacitances, making the FeFET a non-volatile (NV) device.

Storing a logic ’0’ or logic ’1’ in a FeFET device requires a voltage bias between gate and source terminals, which causes a polarization switch in the FE domains. Write voltages on the order of -4V/+4V are required when writing an FeFET [12]. On the other hand, the reading of an FeFET requires a smaller potential to be applied between the gate and source (on the order of 1V [12]). The pulses used to write and read the FeFET are depicted in Fig. 2(b). Note that rather than using a square pulse for reading, here a Measurement pulse is applied. This allows us to ramp up the read voltage within a certain interval -1V to +1V to observe the behavior of the drain current ???? (Figs. 2(c-d)).

# 2.3 Related work

2.3.1 CiM designs for MANNs. The authors of [4] propose the use of TCAM arrays as an alternative for accelerating the nearestneighbor search operations needed by the attentional layer of MANNs. However, the change of precision (from floating point to quantized fixed point), and the replacement of the cosine similarity by a CiM-friendly distance $\left( \bar { L _ { \infty } } \right)$ results in low classification accuracy. To address this issue, the paper proposes to use compound distance metrics, i.e., $L _ { \infty } { + } L _ { 1 }$ and $L _ { \infty } { + } L _ { 2 }$ , in which the computation of $L _ { 1 }$ and $L _ { 2 }$ distances is offloaded to the GPGPU. A fully in-memory approach employing GP-CiMs that implements the same distance metrics as [4] is proposed in [3]. A drawback of this approach is that in order to achieve good accuracies, [3] requires roughly twice as much memory (and energy) during memory updates as the memory entries have to be stored and maintained in separate memories.

In [6], a ?????? function hashes the real values of feature vectors to binary signatures that become the memory entries stored in the memory unit. During inference, the Hamming distances between

the binary signature of a query and the memory entries are measured and compared. Because regular TCAMs can perform only an exact match per search, an approximate TCAM is employed to detect the degree of mismatch (up to 6 bits). Following this method, the classification is performed based on the maximum similarity between a query and the memory entries. The use of ?????? enables comparable accuracies when compared to ??∞ [4]. However, the hashing part still needs to be done on the GPGPU.

2.3.2 Configurable CiM arrays. [13] proposes a configurable CiM array based on SRAM that supports TCAM, CAM, or regular memory operations. Logic operations like AND and NOR between memory words are also possible. However, unlike a conventional CAM (or TCAM), the configurable array in [13] needs to have words stored vertically, as the query is applied in the vertical direction (same direction as the sourcelines). When operating as a memory, the words are stored in a conventional manner (horizontally), which implies that the data would have to be rearranged when switching between the memory modes, triggering additional writes that could be disadvantageous from an application perspective.

A configurable CiM array based on 2T+1FeFET memory cells was proposed in [7]. The design can support GP-CiM, exact TCAM, and crossbar modes. Compared to this work, our design achieves higher memory density and lower power as it employs 1T+1FeFET memory cells and more energy efficient peripheral circuitry.

# 3 AIM DESIGN

# 3.1 Configurable CiM Array Components

Though FeFET-based RAMs, TCAMs and GP-CiM have been proposed in existing works [11, 14–16], straightforwardly combining these designs into a single array is not possible, as RAMs, TCAMs and GP-CiMs are often based on different array structures. For instance, the FeFET-based RAMs and GP-CiM in [11, 14, 16] leverage an AND-type array structure, i.e., with column-wise shared bitlines and sourcelines, and row-wise shared wordlines. In contrast, FeFET-based TCAMs [15] have row-wise shared sourcelines and matchlines. Row-wise shared matchlines imply that the drain nodes of the FeFETs in the same row are horizontally connected together.

The difference between the structures of the RAMs/ GP-CiMs and the TCAMs represent a challenge on building a combined hardware that encompass the RAM, TCAM and GP-CiM functionalities. The configurable CiM proposed in this work is based a non-conventional array structure that can be used for all operation modes, i.e., RAM, TCAM and GP-CiM modes. A high-level view of the proposed configurable CiM array is depicted in Fig. 3(a). In the figure, we show memory peripherals such as wordline drivers, sourceline drivers, bitline drivers, and sense amplifiers along with specialized CiM components (i.e., operation selectors and bit shifters).

Importantly, in our configurable CiM array (Fig. 3(a)), the matchlines (??????) and wordlines (?? ????) are row-wise (i.e., horizontally) connected, while sourcelines (????????), read bitlines (????????), and write/ read bitlines (?????? ????) are column-wise (i.e., vertically) connected. By setting enable signals accordingly, it is possible to either: (i) directly drive a row-wise connected ???? and sense the currents flowing through the column-wise connected ????????, or (ii) directly drive a column-wise connected ???????? and sense the currents flowing through the row-wise connected ??????. While (i) corresponds to the RAM/GP-CiM mode, (ii) supports to the TCAM mode. Below, we briefly discuss the elements of our CiM configurable array, as well as how they are used by the different operation modes (regular RAM, GP-CiM, and TCAM).

3.1.1 1T+1FeFET Memory Cells. The support of a certain type of memory cell by a CiM design directly impacts figures-of-merit such as density, energy consumption, and delay. Our configurable CiM array is based on 1T+1FeFET cells, which enable a compact/energy efficient array design with smaller parasitic resistance/capacitance when compared to 2T+1FeFET memory cells [7, 16] and 6T-SRAMs [17]. The compact memory cells also allow for more energy efficient design of peripheral circuits (i.e., with smaller-sized transistors).

The 1T+1FeFET memory cell and its write and read operations in our configurable CiM design are illustrated in Fig. 3(b). The access transistor (??2) is turned on during both writes and reads (by asserting $W L = V _ { D D } )$ . When writing, the write voltage $( \pm \ : V _ { W } )$ is applied to ?????? ??, while ????, ?????? are kept at 0?? . During reads, a read voltage $( V _ { R D } )$ is applied to ?????? ??, while $( V _ { D D } )$ is applied to the ????. ?????? is kept at 0?? . The current flow between ???? and ?????? is sensed by current-based SAs in our configurable CiM design. The value of the current depends on the value stored in the FeFET (??1).

3.1.2 Input drivers. The input drivers are indicated in Fig. 3(a) as Wordline Drivers, Write/Read Bitline Drivers, Matchline Drivers, and Sourceline Drivers. The drivers are voltage followers, which are used to input biases to the different lines of an array during writes, reads, compute, or searches. Matchline/sourceline drivers can be either activated or de-activated through selector circuits (see the lower right boxes in Figs. 3(c,d) for their schematics). When activated, matchline/sourceline drivers enable ??????/???????? to be directly driven by the corresponding biases. By de-activating a matchline/sourceline driver, its corresponding line (????/??????) is connected to a SA. The use of matchline/sourceline drivers in our configurable CiM design makes it possible for the array to dynamically reconfigure itself, i.e., our configurable CiM array can operate in different operation modes (i.e., RAM, GP-CiM, and TCAM) by activating (de-activating) the correct input buffers. Below, we list the circuits that need to be activated, and the signals applied to enable the different modes:

(1) RAM/GP-CiM (during writes): Matchline and sourceline drivers are activated. Voltage biases are applied to the ???? and ??????. The supply voltages of the GP-CiM and TCAM SAs are turned off to reduce static power;

(2) RAM/GP-CiM (during reads/compute): Matchline driver is activated, and sourceline driver is de-activated. A voltage bias is applied to the ????, and the currents between ???? and ?????? are sensed by the GP-CiM SAs. The supply voltages of the TCAM SAs and the sourceline drivers are turned off to reduce static power;

(3) TCAM: Matchline driver is de-activated, and sourceline driver is activated. A voltage bias is applied to the ????????, and the current (voltage drop) between ???????? and ???? is sensed by the TCAM SAs. The supply voltages of the GP-CiM SAs and the matchline drivers are turned off to reduce static power.

3.1.3 Memory and GP-CiM Sense Amplifiers. Our configurable CiM array employs a current-based sensing scheme for the RAM and CiM modes, as illustrated in Fig. 3(c). The circuit allows for regular reads in the RAM mode and Boolean logic between two memory words (in the GP-CiM mode). The sensing scheme consists of two current SAs in which we use two different references for OR (NOR) and AND (NAND) operations. By leveraging the results of OR and NAND operations/additional CMOS gates, we can achieve XOR and XNOR logic/arithmetic addition (similarly to [16, 18]).

3.1.4 TCAM Sense Amplifier. The TCAM SA of our configurable CiM, illustrated in Fig. 3(d), has a working mechanism similar to [15]. In the figure, the ???????? $S E N S E _ { E N }$ signal has to be asserted

![](images/ca8bf1386d3f2a171f31eaa87933f8abe61df14c79b2606f6876ca987c4a7418.jpg)

![](images/70ef3a2513e267ec9fd7cd085b47b49d14c83363df643a19b62779b4ab558866.jpg)  
(b)

![](images/f0ddc56bc78b0064bdabf49bfd0bffea79e776935a8b574849c73aff6857e737.jpg)

![](images/81e4dc609b593d74b712658054c6dab8558bede851d5c95911c299341eb29600.jpg)

![](images/28500a187ef0e67b9eceb7073685c156dd8b8aa06b5817a86afd8f4103166d8f.jpg)  
Figure 3: (a) Block diagram of AiM, which is based on (b) the 1T+1FeFET memory cell. (c) Two single-ended current SAs are used to perform GP-CiM logic and addition between memory words. (d) A voltage-based SA is used to perform searches in the TCAM mode. (e) A supply gating mechanism is employed to selectively turn on/off ?????? in different circuits.

to $V _ { D D }$ before the start of each search cycle. The signal ?????? is asserted to 0V to precharge the ????. When ?????? switches to $V _ { D D } ,$ the discharge of the ???? happens in the case of a mismatch between any bits of the contents of the memory and the query. Mismatches are detected by the buffer that generates the ?????????????? output.

3.1.5 Supply gating selectors. When switching between operation modes, our design employs a supply gating mechanism for all of its memory peripherals (see Fig. 3(e)). Such mechanism consists of demultiplexers that enable components of the configurable CiM to be selectively turned off when not being used by the active operation mode (i.e., RAM/ TCAM/ GP-CiM). The selection is enabled by a 2-bit “Op Code” that asserts the gated ?????? outputs (i.e., ???? ????????, ???? ????, ???? ?????? , and ?????? ?????? to either $\bar { V _ { D D } } ^ { - }$ or 0V. The correspondence between the “Op Codes” and the possible operation modes is shown in Fig. 3(e). Gated supply, along with the compact memory cells of our design, enable significant energy savings at both array and application levels (see Sec. 4 for an evaluation).

3.1.6 Other GP-CiM Components. The components labeled as “Operation Selectors" in Fig. 3(a) are multiplexers that are used in the GP-CiM mode to select among the several operations possible to be performed in one cycle, e.g., OR, AND, XOR, ADD, etc. Meanwhile, the “Bit Shifters" in Fig. 3(a) are barrel bit shifters [19] used to perform 1-bit left or right shifts in the output, enabling multiplications and divisions by powers-of-two (used in MANN memory updates).

# 3.2 RAM/GP-CiM Modes

Here, we describe the functionality of our configurable CiM array when working as a regular RAM and a GP-CiM.

3.2.1 RAM (Memory Writes). Per Fig. 3(a), in the configurable CiM array, the memory cells share ?? ???? (and ??????) horizontally, which means that the gate sides (and drains) of the FeFETs are connected to common ?? ???? (and ??????) in a row-wise fashion. Meanwhile, the ???????? are shared vertically, which means that the source terminals of the FeFETs share a common node along a memory column. During writes, the matchline and sourceline drivers (Fig. 3(c, d)) are activated. The write proceeds as described in Sec. 3.1.1. The write/read access transistors of the unselected FeFET memory cells

of the array should be turned off, i.e., by setting their $V _ { W L } = 0 V _ { ; }$ , to avoid write disturbances.

3.2.2 RAM (Memory Reads). The read operation for our configurable CiM array based on 1T+1FeFET memory cells has been described in previous work (see [14, 20] for more details). Note that reads and logic OR between memory words can use the same reference current in the SA.

3.2.3 GP-CiM. The GP-CiM mode enables bitwise logic, i.e., AND, NAND, OR, NOR, XOR, XNOR between two words stored in memory (which should be simultaneously selected by leveraging wordline drivers). The sensing scheme in the GP-CiM mode comprises two single-ended sense amplifiers that take as their inputs the sourceline current and compare it to two distinct reference currents (as described in Sec. 3.1.6). The peripherals for implementing the logic/arithmetic functions are similar to [16, 18] and the details are omitted here.

# 3.3 TCAM Mode

While in the TCAM mode, our configurable CiM array can perform exact matches with a voltage-based SA, which means that all the bits of the query must be equal to the bits of a memory entry to output a match result. The operation principle of TCAMs based on voltage-based SAs has been described in previous work [15] and is applicable to our configurable CiM array.

It is important to note that when implemented in configurable CiM arrays, 1 TCAM cell consists of 2 memory cells, as a TCAM needs to store complementary bits to perform binary ?????? as part of its search function. This implies that, when working as a TCAM, the array halves its density. However, this is not exclusive for our design. The same principle is also adopted in previous works [7, 17].

# 4 EVALUATION

In this section, we evaluate the delay and energy consumption of our configurable CiM array in AiM, which is based on the 1T+1FeFET memory cell design. At the array level, we compare our results with FeMAT [7], a configurable CiM design based on 2T+1FeFET memory cells. Furthermore, we analyze the performance, energy, and accuracy of AiM for the attentional memory of MANNs and

![](images/db5c610089389c93cd9499ae83c7d572f0b88ab64412fb9310641d3f30243d1e.jpg)

![](images/5fdda4c24b208aba4f6729696e5c439d28a5f3a9403bcf4996f134f12af93e38.jpg)  
  
Figure 4: Delay and energy of the different operations supported by our configurable CiM array, compared to FeMAT [7].

compare with the GPGPU-based implementation, as well as CiMbased accelerators proposed in [3, 6].

# 4.1 Array-Level Evaluation

4.1.1 Experimental setup. To evaluate the configurable array of AiM, we consider an array size of 1024x64 throughout our evaluation. We employ the Preisach model for FeFETs in [12] along with the CMOS Predictive Technology Model (PTM) from [21, 22] with a 45nm technology node in HSPICE simulations. Though more recent technology nodes (e.g., 22nm) could be used in the design of configurable CiM arrays, we use the 45nm technology node to enable a fair comparison with previous works [3, 6, 7].

Note that the FeFET model used in FeMAT (which we compare our work to) is a single domain model for ferroelectrics based on [23] (different from the Preisach model used in this work). Nevertheless, in our simulations we observe that since both FeFET models use underlying MOSFET transistors with same technology node, the read characteristics with both models are pretty similar. Using different models mostly affect the energy of the write operation, as well as GP-CiM operations that require writes, e.g. the subtraction. In this regard, while the $V _ { W }$ of FeFETs is on the order of ±4V in the Preisach model, the single domain model considers a much smaller $V _ { W }$ , i.e., on the order of ±0.5—1V. The higher $V _ { W }$ of Preisach model results in higher write energy.

4.1.2 Delay and energy analysis. The delays and energies of the various possible operations with our configurable CiM array and FeMAT [7] are shown in Fig. 4. The FeMAT datapoints are directly extracted from [7]. We observe that the average delay across all operations with our configurable CiM is 1.33× lower than FeMAT. The slightly faster operation with our configurable CiM design is due to its more compact memory cell design (1T+1FeFET instead of 2T+1FeFET), which leads to a small overall parasitic component (resistance/capacitance) in the array. For all the operations evaluated, only the search (with TCAMs) is slower in our design (0.45×) due to differences in the design of the TCAM SAs in this work and [7]. Note that [7] does not implement bit shifts in their CiM architecture, so this operation is excluded from our comparison.

In terms of energy consumption, our configurable CiM achieves average savings of 19.96× across all CiM operations. Our design is up to 51.46× more energy efficient for reads when compared to [7]. As mentioned in Sec. 1, the compact memory cell in our configurable CiM (i.e., the 1T+1FeFET), along with the sizing of peripheral circuits and gated supply implementations reduce the overall (static+dynamic) power of the design.

Table 1: Evaluation Setups for AiM   

<table><tr><td>Setup</td><td>Hardware Type</td><td>Distance Metric</td><td>Ref.</td></tr><tr><td>A</td><td>GPGPU+DRAM</td><td>Cosine</td><td>[6]</td></tr><tr><td>B</td><td>TCAM (approximate)</td><td>LSH</td><td>[6]</td></tr><tr><td>C</td><td>TCAM+GP-CiM (independent)</td><td>L∞+L1</td><td>[3]</td></tr><tr><td>D</td><td>TCAM/GP-CiM (configurable)</td><td>L∞+L1</td><td>[7]</td></tr><tr><td>E</td><td>TCAM/GP-CiM (configurable)</td><td>L∞+L1</td><td>AiM</td></tr></table>

Table 2: Accuracies of the MANN with Different Setups, for a 5-way 5-shot inference task with the Omniglot dataset   

<table><tr><td>Setup</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr><tr><td>Accuracy</td><td>99.70%</td><td>92.21%</td><td>91.98%</td><td>95.14%</td><td>95.14%</td></tr></table>

# 4.2 Application-level Evaluation

4.2.1 Experimental setup. We evaluate the energy consumption, latency and classification accuracy of AiM and compare them with a GPGPU baseline implementation, as well as with hardware accelerators proposed in previous works, i.e., [3] and [6]. Our GPGPU baseline implementation uses an Nvidia Titan GPGPU with 2688 CUDA cores and 288.4 GB/s memory bandwidth. Our MANN implementation is identical to the one used in [6] (i.e., with same neural network and 32-bit fixed-point precision).

Our five experimental setups are specified in Table 1. Setup A is the GPGPU-based version of MANN, which uses a cosine similarity distance metric. Setup B uses a ?????? scheme and a Hamming distance-based distance metric, which are implemented with an approximate TCAM. Setup C corresponds to the approach that uses separate TCAM and GP-CiM memories to implement a composed distance metric, i.e., $L _ { \infty } + L _ { 1 }$ . Finally, Setups D and E also employ a composed distance metric $\left( L _ { \infty } + L _ { 1 } \right)$ with FeMAT and AiM configurable designs, respectively. To enable a fair comparison between the works, we make the memory size the same for all configurations, which means that the total memory size (TCAM + GP-CiM) of [3] is equal to the size of the configurable CiM memories.

4.2.2 Delay, energy and accuracy analysis. Fig. 5 presents the results of our delay and energy comparison between the experimental setups in Table 1. In Fig. 5(a) and Fig. 5(b), we show improvements with respect to the GPGPU baseline (Setup ??) for the two main components of the attentional layer, i.e., the distance metric, and the memory updates, respectively.

For distance calculations (Fig. 5(a)), FeMAT and AiM (Setups ?? and ??) achieve 10× speed-up compared to the GPGPU implementation of a MANN (Setup A), as data transfers between memory and processing units are reduced by the CiM approach. Compared to Setup C, FeMAT and AiM can achieve a comparable (1.1×) speedup, as Setups C, D, and E all compute their distance metrics based on multiple TCAM searches, followed by GP-CiM additions and subtractions. Setup B, in turn, is 3× faster than FeMAT and AiM when performing distance calculations. In this regard, Setup B employs ?????? along with an approximate TCAM, which eliminates the need for multiple TCAM searches. When considering energy consumption, the most energy efficient setups for distance calculations are B and C. Setup B (C) enables 70× (6×) energy savings when compared to Setup A. AiM, in turn, still enables 3× energy savings, while FeMAT inccurs 40% energy (and 25× power) overheads when

![](images/be7e4c4d5ed29893d8463879a9f576d0aeff000b5f5b83ed04465f8f9f60d475.jpg)  
Figure 5: Delay and Energy improvements of the four evaluation setups (B through E in Table 1) with respect to Setup A. We present comparisons for (a) distance metric, (b) memory updates, (c) the attentional layer, and (d) end-to-end MANN, with respect to a GPGPU baseline.

compared to Setup A. This result reflects the array level figures reported in Sec. 4.1.2.

For memory updates (Fig. 5(b)), the latency and energy im provements of Setups ?? through ?? compared to Setup ?? are on the order of five to seven orders of magnitude, as writes in a DRAM+GPGPU MANN are expensive [4]. Compared to other CiM accelerators for the attentional layer of MANNs (Setups ?? and ??), the energy required for memory updates with our design (Setup E) is up to 700× smaller. Recall that memory updates require an average between each example in the support set and the entries already present in the memory unit, so new class representations are generated. While AiM performs the average with the adder and bit shifter integrated in its GP-CiM circuitry, Setups ?? and ?? have to outsource this operation to the GPGPU. Furthermore, memory updates with AiM do not need require redundant writes to separate TCAM and GP-CiM units (unlike Setup ??), further justifying the energy efficiency of AiM for memory updates.

We calculate the speedups and energy savings for the attentional layer (Fig. 5(c)) and the end-to-end MANN (Fig. 5(d)) using the Ahmdal’s law (Eq. 1).

$$
S = \frac {1}{\frac {p _ {1}}{s _ {1}} + \frac {p _ {2}}{s _ {2}} + \dots + \frac {p _ {n}}{s _ {n}}} \tag {1}
$$

Here, ?? is the total speed-up, $\scriptstyle { \mathcal { P } } n$ is the percentage of the $n ^ { t h }$ task runtime relative to that of the system, and $s _ { n }$ is the speedup achievable for the $n ^ { t h }$ task (obtained by the ratio between the old and the new execution times of a task). The Ahmdal’s law can be generalized to calculate energy savings [24]. Based on Fig. 1(b) and Eq. 1, assuming that distance calculation and memory updates are the tasks accelerated by CiM, the speed-up (and energy improvement) for the attentional layer is limited to 36.4×. Similarly, end-to-end MANN improvements are limited to 4.9×.

Note that hardware accelerators for the attentional layer of MANNs proposed in previous work (e.g., Setups B and C) already achieve end-to-end speedups and energy savings that are close to ideal (by the Amhdal’s law analysis above). That said, our work (Setup E) can achieve end-to-end speedups and energy savings that are comparable to these state-of-the-art CiM accelerators, with higher accuracies (see Table 2). Namely, AiM achieves 95.14% accuracy v.s. 92.21% (91.98%) accuracy with Setup B (C), for a 5-way 5-shot inference task with the Omniglot dataset. Improving accuracy poses significant challenges to MANNs, as more complicated neural networks, e.g., residual networks (ResNets) may be necessary. The use of complex neural networks for MANNs can turn out to be computationally expensive, as it may result in an increase in both the delay and energy consumption.

# 5 CONCLUSION

We propose AiM, a CiM accelerator for the attentional layer of MANNs. The proposed accelerator is based on a configurable CiM

array that can achieve TCAM and general purpose Boolean logic and arithmetic operations between memory words. When compared to previous work that employs separate TCAM and GP-CiMs, AiM achieves similar end-to-end delay and energy, with higher accuracy for MANNs 95.14% v.s. 91.98% (with a $L _ { \infty } { + } L _ { 1 }$ distance metric) at iso-memory size. When compared to an accelerator that uses a ?????? - based nearest neighbor approach, AiM achieves similar end-to-end delay and energy, also with better accuracy (95.14% v.s. 92.21%).

# ACKNOWLEDGMENTS

This work was supported in part by ASCENT, one of six centers in JUMP, a Semiconductor Research Corporation (SRC) program sponsored by DARPA.

# REFERENCES

[1] A. Graves, et al. Neural turing machines. CoRR, abs/1410.5401, 2014.   
[2] A. Santoro, et al. One-shot Learning with Memory-Augmented Neural Networks. CoRR, abs/1605.06065, 2016.   
[3] A. F. Laguna, et al. Ferroelectric FET Based In-Memory Computing for Few-Shot Learning. In GLSVLSI, page 373–378, New York, NY, USA, 2019. ACM.   
[4] A. F. Laguna, et al. Design of Hardware-Friendly Memory Enhanced Neural Networks. In DATE, pages 1583–1586, 2019.   
[5] A. Ranjan, et al. X-MANN: A Crossbar Based Architecture for Memory Augmented Neural Networks. In DAC, New York, NY, USA, 2019. ACM.   
[6] K. Ni, et al. Ferroelectric ternary content-addressable memory for one-shot learning. Nature Electronics, 2(11):521–529, 2019.   
[7] X. Zhang, et al. FeMAT: Exploring In-Memory Processing in Multifunctional FeFET-Based Memory Array. In ICCD, pages 541–549, 2019.   
[8] L. Kaiser, et al. Learning to remember rare events. CoRR, abs/1703.03129, 2017.   
[9] A. Graves, et al. Hybrid computing using a neural network with dynamic external memory. Nature, 538(7626):471–476, 2016.   
[10] A. Graves, et al. Neural turing machines. CoRR, abs/1410.5401, 2014.   
[11] D. Reis, et al. Design and Analysis of an Ultra-Dense, Low-Leakage, and Fast FeFET-Based Random Access Memory Array. IEEE JxCDC, 5(2):103–112, 2019.   
[12] K. Ni, et al. A circuit compatible accurate compact model for Ferroelectric FETs. In VLSI Symposium. IEEE, 2018.   
[13] S. Jeloka, et al. A 28 nm configurable memory (tcam/bcam/sram) using pushrule 6t bit cell enabling logic-in-memory. IEEE Journal of Solid-State Circuits, 51:1009–1021, 2016.   
[14] S. George, et al. Nonvolatile memory design based on ferroelectric FETs. In DAC, pages 1–6, 2016.   
[15] X. Yin, et al. An Ultra-dense 2FeFET TCAM Design based on a Multi-Domain FeFET Model. IEEE TCAS II: Express Briefs, pages 1–1, 2018.   
[16] D. Reis, et al. Computing in memory with FeFETs. In ISLPED, pages 1–6, 2018.   
[17] S. Jeloka, et al. A 28 nm Configurable Memory (TCAM/BCAM/SRAM) Using Push-Rule 6T Bit Cell Enabling Logic-in-Memory. JSSC, 51(4):1009–1021, 2016.   
[18] S. Jain, et al. Computing in Memory With Spin-Transfer Torque Magnetic RAM. TVLSI, PP(99):1–14, 2017.   
[19] M. R. Pillmeier, et al. Design alternatives for barrel shifters. In Advanced Signal Processing Algorithms, Architectures, and Implementations XII, volume 4791, pages 436–447. International Society for Optics and Photonics, 2002.   
[20] A. Sharma et al. 1T Non-Volatile Memory Design Using Sub-10nm Ferroelectric FETs. IEEE Electron Device L, 39(3):359–362, 2018.   
[21] R. Vattikonda, et al. Modeling and Minimization of PMOS NBTI Effect for Robust Nanometer Design. In DAC, 2006.   
[22] Y. Cao, et al. Predictive technology model. Internet: http://ptm. asu. edu, 2002.   
[23] A. Aziz, et al. Physics-based circuit-compatible spice model for ferroelectric transistors. IEEE Electron Device Lett., 37(6):805–808, 2016.   
[24] R. Ge et al. Generalizing Amdahl’s law for power and energy. IEEE Computer, 2012.