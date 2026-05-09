---
title: "Overview of memristor-SRAM CIM-fusion processor"
authors:
  - "Tai-Hao Wen"
  - "Je-Min Hung"
  - "Wei-Hsing Huang"
  - "Chuan-Jia Jhang"
  - "Yun-Chen Lo"
  - "Hung-Hsi Hsu"
  - "Zhao-En Ke"
  - "Yu-Chiao Chen"
  - "Yu-Hsiang Chin"
  - "Chin-I Su"
  - "Win-San Khwa"
  - "Chung-Chuan Lo"
  - "Ren-Shuo Liu"
  - "Chih-Cheng Hsieh"
  - "Kea-Tiong Tang"
  - "Mon-Shu Ho"
  - "Chung-Cheng Chou"
  - "Yu-Der Chih"
  - "Tsung-Yung Jonathan Chang"
  - "Meng-Fan Chang"
date: "2023-08-01"
year: "2023"
journal: "Science"
doi: "10.1126/science.adf5538"
keywords:
  - "[[Memristor]]"
  - "[[In-memory computing]]"
cite: "[1] Wen et al. Overview of memristor-SRAM CIM-fusion processor[J]. Science, 2023."
aiSum: "忆阻器-SRAM CIM 融合：77.64 TOPS/W、392μs 唤醒、<0.5% 精度损失、TSMC 22nm、自适应本地训练。"
confidence: "high"
wiki_concepts:
  - "[[In-memory computing]]"
  - "[[Memristor]]"
---

Artificial intelligence (AI) edge devices prefer employing high-capacity nonvolatile compute-in-memory (CIM) to achieve high energy efficiency and rapid wakeup-to-response with sufficient accuracy. Most previous works are based on either memristor-based CIMs, which suffer from accuracy loss and do not support training as a result of limited endurance, or digital static random-access memory (SRAM)–based CIMs, which suffer from large area requirements and volatile storage. We report an AI edge processor that uses a memristor-SRAM CIM-fusion scheme to simultaneously exploit the high accuracy of the digital SRAM CIM and the high energy-efficiency and storage density of the resistive random-access memory memristor CIM. This also enables adaptive local training to accommodate personalized characterization and user environment. The fusion processor achieved high CIM capacity, short wakeup-to-response latency (392 microseconds), high peak energy efficiency (77.64 teraoperations per second per watt), and robust accuracy (<0.5% accuracy loss). This work demonstrates that memristor technology has moved beyond in-lab development stages and now has manufacturability for AI edge processors.

n the realm of sensing and control, sending data directly to a large, central computational resource can be slow and energy intensive compared with processing signals near the sensors with small, distributed processors (edge computing). This approach places a premium on energy consumption of processors as these devices are often powered by batteries and must also transmit information to a central source (for example, Internet of Things devices such as environmental and motion sensors in a home for climate control and security). Artificial intelligence (AI) processors that use machine learning can provide a low-power alternative for these repetitive computational tasks to conventional (von Neumann) computing architectures. Such AI processors require high-capacity on-chip nonvolatile memory (for storing whole neural network parameters when power is off), high bit precision (for inference accuracy), high energy efficiency (for long battery life), fast wakeup from power off states, and short computation latency (the time between the start and end of the computation cycle for rapid inference response), and high tolerance for process variations (for ease and cost of manufacturability). Such processors should also allow for

1 Taiwan Semiconductor Manufacturing Company Limited (TSMC), No. 8, Li-Hsin Rd. 6, Hsinchu Science Park, Hsinchu 300, Taiwan, R.O.C. 2 Department of Electrical Engineering, National Tsing Hua University (NTHU), No. 101, Sec. 2, Guangfu Rd., East Dist., Hsinchu City, Hsinchu 300, Taiwan, R.O.C. 3 Department of Life Science, National Tsing Hua University (NTHU), No. 101, Sec. 2, Guangfu Rd., East Dist., Hsinchu City, Hsinchu 300, Taiwan, R.O.C. 4 Department of Physics, National Chung Hsing University (NCHU), No. 145, Xingda Rd., South Dist., Taichung City 402, Taiwan, R.O.C. *Corresponding author. Email: mfchangf@tsmc.com (M.-F.C.) †These authors contributed equally to this work.

on-chip adaptive local training (ALT) to tune the parameters of neural network models in accordance with personalized characterization and user environment.

Conventional computations are limited in terms of energy efficiency and computing latency because of the frequent movement of neural network parameters and intermediate computing data between processing cores and memory, a problem referred to as the memory wall (1–3). Compute-in-memory (CIM), which refers to a memory block with built-in computing functions, can largely overcome this bottleneck by performing multiple dot-product operations within the memory cell array. Most of the CIM-based AI processors use either digital static random-access memory CIM (SRAM-CIM) or memristor-CIM. The digital SRAM-CIM offers low density volatile storage with lossless computation and low memory write overhead whereas the memristor-CIM offers high density nonvolatile storage and highly parallel and efficient computing.

Digital SRAM-CIM (4–8) has become mainstream in recent years as it provides robust computing accuracy against process variation. However, the volatile nature of SRAM memory cells in SRAM-CIM hinders its integration in AI edge processors for fast wakeup-and-response operations because of the need to transfer weight from off-chip memory to on-chip SRAM-CIM during each inference. Also, SRAM-CIM imposes large area overhead for SRAM bit cells (~3 times larger than a memristor memory cell in 22-nm node technology) and digital circuitry for dot-product operations (~50% of total digital SRAM-CIM units).

Memristor-CIM (9–37) provides large memory capacity, high storage density, and high

energy efficiency. However, these devices suffer computing accuracy degradation due to process variation during mass production, particularly in devices that use multilevel cells (MLCs) that can store more than one bit of data. A memristor-CIM core with in-lab 32-level cell and multiple discrete components on a printed circuit board (9) has been demonstrated to classify images from the Modified National Institute of Standards and Technology database (MNIST) and the Canadian Institute for Advanced Research (CIFAR-10). However, in-lab memristor devices suffer from poor scalability and incompatibility with advanced complementary metal-oxidesemiconductor (CMOS) technology. We reported a single-level cell (SLC)–MLC multimode memristor–CIM processor (10) that used foundry-provided (“off the shelf”) memristor technology to classify images from CIFAR-100 and ImageNet. However, those devices are ill-suited to on-chip training as a result of limited memristor endurance (~10,000 cycles) (38). In general, prior CIM-based AI processors that use a single-type device (either SRAM or memristor) are poorly suited for rapid development in future AI edge devices.

# Overview of memristor-SRAM CIM-fusion processor

We present a fully CMOS-integrated memristor-SRAM CIM-fusion AI edge processor that combines the high accuracy of the digital SRAM-CIM and the high energy efficiency and high nonvolatile storage density of the resistive random-access memory (RRAM) memristor-CIM. This processor overcomes individual challenges related to functionality, performance, and manufacturability by also incorporating software-hardware co-optimization and onchip ALT. As shown in Table 1, this work, by integrating a memristor-SRAM CIM-fusion scheme along with ALT and the proposed schemes at the macro level, achieves 1.14 times greater energy efficiency while limiting the degradation in inference accuracy to only 0.49 times compared with our previous work (10) with ResNet-20 and CIFAR-100.

The proposed processor achieves various trade-offs between inference accuracy and energy efficiency across a variety of neural network models and datasets. The proposed memristor-SRAM CIM-fusion AI edge processor (Fig. 1A) comprises a CIM-fusion system controller (Fig. 1B), four CIM-fusion units, ALT circuitry (Fig. 1C), and other functional modules for inference and training operations (Fig. 1D). The CIM-fusion processor employs foundryprovided 22-nm RRAM memristors and SRAMbit cell to facilitate manufacturability while enabling integer dot-product operations with binary to 8-bit (8b) precision.

The features of the proposed processor are summarized as follows: The CIM-fusion mode

Table 1. Comparison of current work (version 2.0) versus previous work (version 1.0) (10).   

<table><tr><td></td><td>Category</td><td>This work (version 2.0)</td><td>Previous work (version 1.0) (10)</td></tr><tr><td rowspan="2">Processor-level feature</td><td>CIM mode controller</td><td>Memristor-SRAM CIM-fusion(SRAM-CIM ` mixed-device-CIM ` memristor-CIM)</td><td>Multimode memristor-CIM(IMC-NMC hybrid-mode)</td></tr><tr><td>On-chip training</td><td>ALT</td><td>No</td></tr><tr><td rowspan="3">Macro-level feature</td><td>SRAM-CIM feature</td><td>MUX-based local compute cell</td><td>No SRAM-CIM</td></tr><tr><td>Input feature</td><td>Fusion-aware activation distributor(with dynamic accumulation and in-memory cell array current quantization)</td><td>Dynamic accumulation with in-memory cell array current quantitization</td></tr><tr><td>Weight feature</td><td>Weight shift with compensate</td><td>No</td></tr><tr><td>Energy efficiency</td><td></td><td>1.16x</td><td>1x</td></tr><tr><td>Inference accuracy degradation</td><td></td><td>0.49x</td><td>1x</td></tr></table>

controller manages CIM-fusion units using different operating modes (four memristor-CIM modes across SLC and MLC, one mixed-device CIM mode, and one SRAM-CIM mode) for multiple neural network layers with the aim of striking a balance between memory capacity, energy efficiency, and inference accuracy. Note that the SLC-MLC hybrid memristor-CIM structure facilitates the manufacturability of onchip MLC cells.

The CIM-fusion unit (memristor-CIM, SRAM-CIM, and fusion bridge) enables a variety of operating modes to support dot product operations with high energy efficiency and high accuracy. The fusion bridge includes a digital circuit that incorporates the CIM-fusion mechanism between memristor-CIM and SRAM-CIM. In the fusion bridge, dynamic accumulation shortens computing latency without compromising accuracy. In memristor-CIM we also developed an in-memory-cell array current quantization scheme and weight shifting with compensation scheme to stabilize the bitline (BL) current and reduce energy consumption. In SRAM-CIM, we developed a compute cell. Note that the multiplexer (MUX)-based local compute cells comprise a 2-to-4 MUX-based local compute cell that utilizes the pre-computed result to reduce the adder tree power and area.

Our CIM-fusion-based ALT allows system customization and personalized characterization of user environment and relaxes the limited endurance of memristor devices. The proposed ALT scheme enhances system-level inference accuracy during the inference stage by suppressing the effects of process variation on memristors and transistors.

# Fusion-CIM mode controller

The fusion-CIM mode controller features three operating modes—memristor-CIM, mixed-device CIM, and SRAM-CIM—across different neural network layers (Fig. 2A). Memristor-CIM modes are suitable for layers that are less sensitive to readout accuracy degradation but require a

massive number of dot product operations, thereby necessitating high energy efficiency and high computing throughput. As shown in Fig. 2B, we sought to achieve a suitable balance between readout accuracy, energy efficiency, and storage density by storing the 8b weights of the neural network in memristor-CIM mode (MM), mixed-device CIM mode (MDM), or SRAM-CIM mode (SM) using various memorycell configurations. The memristor-CIM mode includes one SLC mode (MM-S), two MLC-SLC hybrid modes (MM-1 and MM-2), and an MLC mode (MM-M).

These different modes present operational trade-offs. The memristor-CIM MLC mode (MM-M) provides the highest energy efficiency. However, it suffers the most computing accuracy degradation because of process variation and a data-retention time among the memristor-CIM mode (MM) modes. The mixeddevice CIM mode (MDM) is suitable for layers that depend on high computing accuracy as well as dot product operations with high energy efficiency and computing throughput. Note that the 8b weights are split into two parts {most significant bits (MSB) (W[7:4]) and least significant bits (LBS) (W[3:0])} and stored in memristor-CIM and SRAM-CIM, respectively, through a weight distributor in the fusion bridge. The pure SM mode is suitable for layers that require dot product operations of ultrahigh accuracy, such as fully connected layers.

# Adaptive local training

Most AI edge devices use a pretrained neural network model and parameters provided by device vendors. However, even slight variations in customer environment or personalized characterization can undermine inference accuracy. Therefore, it is desirable to have hardware that can customize neural networks to accommodate customers with different user environments, as well as accommodate variation in individual chips for inference accuracy.

Process variation during manufacturing can affect the cell conductance of memristor devices, which can considerably affect the accuracy of dot-product operations (up to 10%), particularly for memristors featuring multilevel cell storage, where precise cell conductance is essential for accurate computing. Figure 3A presents the measured RRAM memory cell conductance distribution in four memristive states. Note that computing errors generated by memristor-CIM can be transmitted and amplified across neural network layers and so the severity of the effects can be enhanced in a deep neural network, as shown in Fig. 3B. Moreover, the limited endurance and long set and reset latency of memristors discourage their use for on-chip training operations, which involve a large number of write operations.

We developed an on-chip CIM-fusion based a ALT strategy to address these issues. Essentially, ALT is a process of fine-tuning accuracyoriented weights stored in the SM mode and mixed-device CIM mode (MDM) with the aim of allowing the neural network to accommodate personalized characterization or user environments as well as fluctuations in the cell conductance of memristors caused by process variation during manufacturing. Note that in MDM, the MSBs stored in the memristor-CIM are transferred to SRAM-CIM through the weight transfer circuit in the fusion bridge (weight transfer flow is shown in fig. S7). By eliminating the need to adjust the weights stored in memristor-CIM, our ALT system avoids excessive use of memristor devices, which have limited endurance. In contrast, SRAM faces no such endurance limitations. Following the completion of ALT, the trained weights are redistributed to memristor-CIM and SRAM-CIM by means of the weight distributor in the fusion bridge. The proposed ALT relaxes the endurance of memristor devices and suppresses training latency by only fine-tuning accuracy-oriented weights and taking advantage of SRAM-CIM, which features short read, write, and computing

![](images/fb297241a35047487928a7e609f1eba74fd55aa4badfd9baf25674c534f460e9.jpg)  
A

![](images/a8e3d9d765234742eed5d3d57aac59f1c80db5876cba787163297e3c276c732d.jpg)  
B

![](images/b33df4525eb7db733641400c612e699bdaace8661aeb77674b383f1da31b59d4.jpg)

![](images/84f1667916887c53f4fcabd9a3e045572467afecfeefb24eefd3c496ec99df1b.jpg)  
D   
Fig. 1. Overview of proposed CMOS-integrated nonvolatile AI edge processor based on a memristor-SRAM CIM-fusion structure. (A) Die photo of CMOS-integrated memristor-SRAM CIM-fusion AI edge processor. (B) CIMfusion controller to manage CIM-fusion units in different operating modes for multiple neural network layers. (C) ALT is proposed to accommodate personal characterization or user environment, relax the endurance of memristor devices   
during the training stage, and suppress the inference accuracy degradation during the inference stage. (D) The fully CMOS-integrated memristor-SRAM CIM-fusion AI edge processor comprises one CIM-fusion system controller, system input and output (IO), four CIM-fusion units, one 512 KB activation SRAM buffer, circuitry for ALT, and other modules for inference and training operations. Note that this design does not require a weight SRAM buffer as all weights are stored in the RRAM memristor array.

latency and robust computing accuracy during training (detailed implementation is shown in fig. S8). Figure 3C shows that ALT reduces inference accuracy degradation from 53.7 to 48.4% when applying the ResNet-20 to the CIFAR-10 and CIFAR-100 datasets.

# CIM-fusion unit

As shown in Fig. 4A, the CIM-Fusion unit comprises three major units, including a memristor-

CIM, fusion bridge, and digital SRAM-CIM. The fusion bridge comprises a fusion-aware activation (input) distributor for the dynamic accumulation operations used in CIMs, a weight distributor for distributing weight data (W[7:0]) to the appropriate physical memory locations in memristor-CIM and SRAM-CIM, and a global dot product integrator for combining the massive partial dot product results generated by memristor-CIM and SRAM-CIM macros.

Figure 4B presents a simplified illustration of the memristor-CIM structure, which comprises a memory cell array for storing weight data, BL voltage $( \mathtt { V } _ { \mathtt { B L } } )$ regulators for controlling $\mathrm { V _ { B L } }$ during dot product operations, 5-bit resolution analog-to-digital converters (ADCs) (10) for converting analog-domain partial dot products on BLs into the digital domain, and a configurable digital adder for combining partial dot products (5-bit) to generate 24-bit

![](images/6b80019db35d7d9c4f9c3f8b856ef32b0b10310c7514ed8fd4d8a38b64616cca.jpg)  
A

![](images/acacf24fc921ff5e12cfd6341f70637e82eb619b0f40fe190e1800dd5bde3736.jpg)  
B

<table><tr><td rowspan="2">CIM-Fusion
Mode
controller</td><td colspan="8">Weights [7:0] (W[7:0])</td></tr><tr><td>W[7]
(MSB)</td><td>W[6]</td><td>W[5]</td><td>W[4]</td><td>W[3]</td><td>W[2]</td><td>W[1]</td><td>W[0]
(LSB)</td></tr><tr><td>MM-M</td><td colspan="2">MLC</td><td colspan="2">MLC</td><td colspan="2">MLC</td><td colspan="2">MLC</td></tr><tr><td>MM-2</td><td>SLC</td><td>SLC</td><td colspan="2">MLC</td><td colspan="2">MLC</td><td colspan="2">MLC</td></tr><tr><td>MM-1</td><td>SLC</td><td>SLC</td><td>SLC</td><td>SLC</td><td colspan="2">MLC</td><td colspan="2">MLC</td></tr><tr><td>MM-S</td><td>SLC</td><td>SLC</td><td>SLC</td><td>SLC</td><td>SLC</td><td>SLC</td><td>SLC</td><td>SLC</td></tr><tr><td>MDM</td><td>DIG</td><td>DIG</td><td>DIG</td><td>DIG</td><td>SLC</td><td>SLC</td><td>SLC</td><td>SLC</td></tr><tr><td>SM</td><td>DIG</td><td>DIG</td><td>DIG</td><td>DIG</td><td>DIG</td><td>DIG</td><td>DIG</td><td>DIG</td></tr></table>

![](images/20b7504fbd62126686afd07828264899413134c0ed0fff344f52d8c0d7e1b6c5.jpg)  
Fig. 2. Overview of proposed CIM-fusion mode controller and ALT. (A) CIM-fusion mode controller selects different modes across various neural network layers. (B) Memristor-SRAM CIM-fusion processor includes memristor-CIM modes (MM-M, MM-2, MM-1, and MM-S), mixed-device CIM mode (MDM), and SRAM-CIM mode (SM).   
A

<table><tr><td colspan="2">Characteristics of Memristor</td></tr><tr><td>Set / Reset voltages (MLC states &amp; forming)</td><td>1.2V ~ 3.6V</td></tr><tr><td>Read voltage</td><td>&lt; 0.3V</td></tr><tr><td>Cell size</td><td>53F²</td></tr></table>

![](images/547b1c6ae603369657d91bba39d3c89eb3c31d0fa0bb3cfc030b6ec833e77e74.jpg)  
B

![](images/73ec2c6692432409d9b1bf3332a06edd1d392402c8ab2c9518b4781aa3ca0513.jpg)  
  
Fig. 3. Overview of proposed fusion CIM mode controller and ALT.

(A) Memory cell-conductance distribution of MLC memristor (properties shown on the right) in four memristive states (left). (B) ALT tasked with adjusting weight data stored in SRAM-CIM mode (SM) and mixed-device CIM mode (MDM) with the aim of accommodating various operating conditions (such as

personalized characterization and user environments) and fluctuations in memristor cell-conductance caused by process variation. (C) Measured accuracy degradation shows that ALT reduced inference accuracy degradation by 53.7 to 48.4% when applying the ResNet-20 to the CIFAR-10 and CIFAR-100 datasets.

dot products per output channel (under 8b input/weight precision). 8b-weight data are stored on the same row but across a different number of columns in 2’s-complement format to indicate the sign of the number. In MM-S mode, 8b-weight data are stored in eight memory cells across eight columns in SLC mode. In MM-1 mode, 8b-weight data are stored in four SLC cells and two MLC cells across six columns. In MM-2 mode, 8b-weight data are stored in two SLC cells and three MLC cells across five columns. In MM-M mode, 8b-

weight data are stored in four MLC cells across four columns.

In each SLC cell, data “1” are encoded as low resistance state (LRS) $( \mathrm { R } _ { \mathrm { L R S } } ) ,$ , whereas data $^ { 6 } 0 ^ { 3 }$ are encoded as high resistance state (HRS) $( \mathrm { R } _ { \mathrm { H R S } } ) .$ . In each MLC cell, $^ { * } \mathrm { 1 1 } ^ { * } , \ ^ { * } \mathrm { 1 0 } ^ { * } , \ ^ { * } 0 \mathrm { 1 } ^ { * } ,$ , and $^ { 6 6 } 0 0 ^ { 9 }$ are encoded as $\mathrm { R } _ { \mathrm { L R S } } , 4 / 3 { \times } \mathrm { R } _ { \mathrm { L R S } } , 2 { \times } \mathrm { R } _ { \mathrm { L R S } } ,$ and $4 \times \mathrm { R _ { L R S } } ,$ respectively. Thus, when a given clamping voltage is applied to the BL during a dot product operation, the memory cell current can be regulated to ILRS, ¾ILRS, ½×ILRS, and $\mathrm { { \% } \times I _ { I R S } }$ for the 4 MLC cell-resistance states.

During a dot product operation, the inputs are sent to memristor-CIM for dot product computation by means of the wordline (WL). Each memristor cell multiplies a given input by a weight stored in the memory cell. A BL then accumulates the multiplication result from activated memory cells in the same column to generate analog BL current $( \mathrm { I _ { B L } } ) .$ . Each $\mathrm { I _ { B L } }$ is read out by an ADC with 5-bit resolution to generate the partial dot-product result. A configurable adder is then used to combine partial dot products with respective

![](images/41b7cb356cc827c9c6732c5e1733e9929f34fbd290dbba071a7b6b460ccd838c.jpg)

![](images/1b0116ca89aa4e051bc058be10fc7458fd638a3c1f9777f83d107f5fd3df7689.jpg)  
C

![](images/04f09039e885a3643f1e94bdbf28e464fcc7c160b78606d57c4154bc536fdae6.jpg)  
B   
Fig. 4. Overview of CIM-Fusion unit, including fusion bridge, digital SRAM-CIM, and SLC-MLC hybrid memristor-CIM. (A) The fusion bridge comprises a fusionaware activation (input) distributor, a dynamic accumulation circuit, a fusion-aware weight distributor, a global dot product integrator, and a weight transfer circuit. (B) Structure   
of memristor-CIM at the circuit level, comprising a memory cell array, BL voltage regulators, 5-bit resolution analog-to-digital converters, and a configurable adder for 24-bit dot product results. (C) Structure of digital SRAM-CIM, comprising 64 subarrays, 64 MUX-based local compute cells for multiplication, and one configurable adder.

place values from the MSB readout channel to the LSB readout channel to generate a 24- bit dot product result for 8b-input and 8bweight.

Figure 4C and fig. S8 illustrates the structure of digital SRAM-CIM at the circuit level, which comprises 64 subarrays (8 rows and 25 columns) for storing weight data, 64 MUX-based local compute cells for 2-input multiplication, and one configurable local adder for accumulating 64 multiplication results (8b-input and 8b-weight with 128 accumulations). Every eight memory rows share a MUX-based local compute cell for dot-product operation. Each memory row stores two 8-bit weights (W0[7:0] and W1[7:0]) and one post-addition value (W0[7:0] + W1[7:0]). During a dot product operation with 8b-input and 8b-weight with 128 accumulations, 64 rows are activated and the data stored in the memory cells are loaded into the 64 MUX-based local compute cells. Note that the MUX-based local compute cells comprise a 2-to-4 MUX,

which inserts a dot-product between 2 bitwise inputs and 2 word-wise weights where the output is among 0, W0[7:0], W1[7:0], and W0[7:0] + W1[7:0], as selected by IN0[x] and IN1[x]. If IN0[x] and IN1[x] are both 0s, both 1s, 1 and 0, 0 and 1, such that the output of the MUX is 0, W0[7:0] + W1[7:0], W1[7:0], W0[7:0], respectively. Note that each 8-bit input $( \mathrm { I N } _ { 0 - \mathrm { N } } [ 7 ; 0 ] )$ ) is split into 8 input cycles and the configurable adder accumulates the partial dot-products across eight cycles to obtain the final dot product result.

# Dynamic accumulation by the fusion bridge

Figure 5A illustrates the operational flow of the proposed dynamic accumulation (DA) scheme, which leverages software-hardware co-optimization to increase the accumulation number $( \mathrm { N _ { A C C U } } ) ,$ the number of WLs that are turned on in a single cycle, with the aim of maximizing computing throughput for a single operational cycle in memristor-CIM and SRAM-

CIM. The dynamic accumulation slices 8-bit wordwise inputs into bitwise inputs and reorganizes them into eight bitwise groups according to their bitwise place values (W[7] group, W[6] group, …, and W[0] group). The dynamic accumulation provides four optional accumulation numbers for each group: 16, 32, 64, and 128. Bitwise inputs with higher place values involve fewer accumulations to maintain high-accuracy dot product operations whereas bitwise inputs with lower place values involve more accumulations to boost throughput. Consider an example dot product operation with 512 accumulations (Fig. 3B), where the MSBs (W[7]) of 512 8b-inputs form 32 MSB groups (each group has 16 MSBs) when $\mathrm { N _ { A C C U } } = 1 6 .$ . The LSBs (W[0]) of 512 8b-inputs form 4 LSB groups (each group has 128 LSBs) when $\mathrm { { N _ { A C C U } } = }$ 128. Each CIM macro requires 16 cycles to finish the dot product operation for all 512 MSB input bits whereas only 4 cycles are required to finish the dot product operation for all 512 LSB

![](images/6594c48174d77dff9bdc9218749a118c48b6d7680372b409796dac88ba81504b.jpg)

![](images/9bdb7ba6114b5e1d2ed47af6451f7ac8f403c93ba915721a65b2d5b6d8f1d770.jpg)

<table><tr><td>NACCU</td><td>VBL</td><td>Icell</td><td>IBL</td><td>Readout precision</td></tr><tr><td>16</td><td>VBL-16</td><td>Icell</td><td>16 x IHRS ~ 16 x I LRS</td><td>4b (Full Precision)</td></tr><tr><td>32</td><td>1/2 x VBL-16</td><td>1/2 x Icell</td><td>32 x (1/2) IHRS ~ 32 x (1/2) I LRS</td><td>5b (Full Precision)</td></tr><tr><td>64</td><td>1/4 x VBL-16</td><td>1/4 x Icell</td><td>64 x (1/4) IHRS ~ 64 x (1/4) I LRS</td><td>5b (Quantize 1b)</td></tr><tr><td>128</td><td>1/8 x VBL-16</td><td>1/8 x Icell</td><td>128 x (1/8) IHRS ~ 128 x (1/8) I LRS</td><td>5b (Quantize 2b)</td></tr></table>

IBLisstabilized at 16 $\times I _ { H R S } \sim 1 6 \times I _ { L R S }$ →Lowerenergyconsumptionandcurrentfluctuation

![](images/c419f6ecbe36fa2953248d1112bbbd0155d02ed98480975cd70207dc0025f8e2.jpg)

![](images/54cc8a1e5502d66ad4d7383c0b21bfb15ced2b2c97b9f206533a0993f9856a0a.jpg)

![](images/d056ed65867a9da2a4e77a03d785f52e8736ebbe8ea9db562fb8337310db1c3d.jpg)  
Fig. 5. Dynamic accumulation and proposed memristor-CIM schemes. (A) DA for the control of accumulation number during dot-product operations based on the place value of the bitwise input. (B) IMCACQ aimed at regulating BL voltage based on the accumulation number. (C) Proposed WSwC scheme aimed at increasing the number of HRS cells during computation and restoring the dot-product value through a digital compensation circuit.

input bits. Note that the accumulation number for each bitwise input group can be configured by the user according to the desired trade-off between computing throughput and system-level accuracy (detailed implementation is shown in fig. S11).

# In-memory cell array current quantization in memristor-CIM

The wide range of accumulation numbers supported by the dynamic accumulation can induce notable current fluctuations on BLs in memristor-CIM macros. Thus, we developed an in-memory cell array current quantization (IMCACQ) scheme to stabilize the maximum BL current $\left( \operatorname { I } _ { \mathrm { B L M A X } } \right)$ through the dynamic regulation of $\mathrm { V _ { B L } }$ according to the accumulation number associated with each dot product operation.

Figure 5B illustrates a memristor array operating with in-memory cell array current quantization in four quantization modes. When performing a dot product operation with 16 accumulations per output channel, each BL is biased at ${ \mathrm { V } } _ { \mathrm { B L - 1 6 } } ,$ which results in an IBL-MAX

equal to the summed memory cell current $\mathrm { ( I _ { L R S } ) }$ of reading 16 LRS cells $( \mathrm { I _ { B L - M A X } } = 1 6 \times \mathrm { I _ { L R S } } ) .$ When performing a dot product operation with 32 accumulations, $\mathrm { \Delta V _ { B I } }$ is biased at $0 . 5 \times \mathrm { V } _ { \mathrm { B L } = 1 6 } ,$ resulting in $\mathrm { I _ { B L , M A X } } = 1 6 \times \mathrm { I _ { L R S } } ~ ( = 3 2 \times 0 . 5 ~ \times$ $\mathrm { I _ { L R S } ) } .$ . Generally, $\mathrm { \Delta V _ { B L } ~ = ~ \Delta V _ { B L - 1 6 } / ( a c c u m u l a t i o n }$ number/16) in order to stabilize the maximum $\mathrm { I _ { B L } a t 1 6 \times I _ { L R S } } .$ .

Using an ADC with 5-bit resolution to read out the BL current, the BL current is linearly quantized to 5-bit when using 64 or 128 accumulations. Note that 16- and 32-accumulation modes both provide full-precision readout; however, the signal margin in the 16-accumulation mode is larger than that in the 32-accumulation mode, leading to higher readout accuracy.

# Weight shifting with compensation in memristor-CIM

We developed a weight shifting with compensation (WSwC) scheme in Fig. 5C with the aim of suppressing the overall amplitude of memory cell current consumed in memristor-CIM by increasing the number of HRS cells stored in

the memristor cell array during dot product computation. Weight shifting with compensation was implemented in three stages: (i) weight shifting to increase the number of HRS cells in the cell array; (ii) dot-product computing based on shifted weight data; and (iii) compensation for dot-product results in accordance with the weight shifting value. When storing the weight data of a neural network into the memristor-CIM, each 8-bit weight (W[7:0]) value is shifted by adding a positive bias $( \mathrm { B } _ { \mathrm { S h i f f } } ; \mathrm { e . g . } , 1 6 )$ by an on-chip shifting circuit. Note that in typical neural network models, small positive and negative weight values account for the largest proportion of the weights. When using the 2’s complement format, the bitwise ones lying in small negative value are the majority and the bitwise zeros lying in small positive value are the majority. Thus, weight shifting increases the bitwise sparsity of weight data, which increases the number of HRS cells in the memristor cell array.

In the dot-product computing stage, the dotproduct operation is conducted using post-

shifted weights with smaller current amplitude to generate auxiliary dot-product values. In the compensation stage, the final dot product value is obtained by subtracting auxiliary dot-product values from the auxiliary shifted value, which is generated by accumulating the values obtained by multiplying $\mathrm { B } _ { \mathrm { S h i f t } }$ with the inputs (the trade-off of selecting $\mathrm { B } _ { \mathrm { S h i f t } }$ is shown in fig. S12). The equation for compensation can be expressed as follows:

$$
\begin{array}{l} \left(\mathrm {W} _ {0} + \mathrm {B} _ {\text {S h i f t}}\right) + \dots + \mathrm {I N} _ {\mathrm {n}} \times \left(\mathrm {W} _ {\mathrm {n}} + \mathrm {B} _ {\text {S h i f t}}\right) \\ \begin{array}{r l} & = \mathrm {I N} _ {0} \times \mathrm {W} _ {0} + \mathrm {I N} _ {0} \times \mathrm {B} _ {\text {S h i f t}} + \dots + \mathrm {I N} _ {\mathrm {n}} \times \mathrm {W} _ {\mathrm {n}} + \\ & \mathrm {I N} _ {\mathrm {n}} \times \mathrm {B} _ {\text {S h i f t}} \end{array} \\ \begin{array}{l} = (\mathrm {I N} _ {0} \times \mathrm {W} _ {0} + \ldots + \mathrm {I N} _ {\mathrm {n}} \times \mathrm {W} _ {\mathrm {n}}) + (\mathrm {I N} _ {0} \times \\ \mathrm {B} _ {\mathrm {S h i f t}} + \ldots + \mathrm {I N} _ {\mathrm {n}} \times \mathrm {B} _ {\mathrm {S h i f t}}) \end{array} \\ \end{array}
$$

# Measurement results and demonstration of AI edge application

The flexibility of our memristor-SRAM CIMfusion AI edge processor was assessed through implementation in keyword spotting, gesture recognition, and image classification (the application to which modern edge devices are most commonly applied). Keyword spotting and gesture recognition are also fundamental applications applicable to augmented and virtual reality. Figure 6, A and B, presents the inference accuracy degradation and energy effi-

ciency, respectively, across various neural network models and datasets. Those measurement results included all AI tasks performed endto-end on-chip under power supply voltage = 0.8V, frequency = 200 MHz, and 8b precision (detailed specifications are summarized in tables S1 and S2).

The experiment on image classification was conducted using MobileNet-V2 (scalable), and ResNet-20 models. The inference accuracy was 0.14 to 0.51% below the software baseline, when applied to datasets of various complexity (MNIST, CIFAR-10, CIFAR-100, and ImageNet). Chip-level energy efficiency ranged from 34.24 TOPS/W to 77.64 TOPS/W. The experiment on gesture recognition was conducted using a parallel-CNN model to classify 14 gestures in a dynamic hand gesture dataset. The inference accuracy was 0.19% below the software baseline and the measured energy efficiency was 62.21 TOPS/W. The experiment on keyword spotting was conducted using a DS-CNN model to classify 12 speech commands in the Google Speech Commands V1 dataset. The inference accuracy was 0.21% below the software baseline and the measured energy efficiency was 64.17 TOPS/W.

Figure 6C illustrates the ratios of CIM-fusion modes operation used by the proposed AI edge processor in various experiments. When dealing with simpler classification tasks, neural

network layers may use more memristor-CIM modes (MM) to achieve ultrahigh energy efficiency while preserving inference accuracy. When dealing with complex classification tasks, neural networks use more SM and MDM modes to maintain sufficient inference accuracy and high energy efficiency. These ratios are optimized (assignment flow is shown in fig. S5) to achieve a balance between accuracy and energy efficiency. The weight mapping strategy used in a given neural network can be adjusted to prioritize either accuracy or energy efficiency in accordance with the requirements of the intended application.

Figure 6D presents the measured wakeupto-response latency of the proposed memristor-SRAM CIM-fusion processor when using the ResNet-20 model trained for the CIFAR-100 dataset. The overall latency for one-shot inference was 392.5 ms.

# Conclusions and outlook

This paper presents an AI edge processor based on commercial RRAM memristor technology with a memristor-SRAM CIM-fusion structure and on-chip ALT. In experiments, the proposed chip achieved reliable computation, sufficient inference accuracy, high energy efficiency, short wakeup-to-response latency, compact area, and high manufacturability. The CIM-fusion structure simultaneously obtains

![](images/65cd50f118fa29ca1789abfde8910c215ce82445dba61fa8f67aeaa56515a13c.jpg)  
A   
B

<table><tr><td></td><td>M</td><td>Dataset</td></tr><tr><td>Testset-1</td><td>DS-CNN</td><td>Google Speech Commands</td></tr><tr><td>Testset-2</td><td>Parallel-CNN</td><td>Dynamic hand gesture dataset</td></tr><tr><td>Testset-3</td><td>ResNet-20</td><td>MNIST</td></tr><tr><td>Testset-4</td><td>ResNet-20</td><td>CIFAR-10</td></tr><tr><td>Testset-5</td><td>ResNet-20</td><td>CIFAR-100</td></tr><tr><td>Testset-6</td><td>MobileNet-V2</td><td>CIFAR-100</td></tr><tr><td>Testset-7</td><td>MobileNet-V2</td><td>ImageNet</td></tr></table>

![](images/a68c6cc3a39b806453adf11903ed908cf67113accd0fa0823508234de6cd2d42.jpg)  
C

![](images/3f54e7fe0fb0438aa00e27f4f6a65066b9cb45d30c9851efc05310f8e6c78636.jpg)  
D   
Fig. 6. Measurement results and demonstration of AI edge applications. (A) Inference accuracy degradation and energy efficiency when memristor-SRAM CIM-fusion AI edge processor was applied to various inference tasks. (B) Table of test sets applied in the experiments. (C) Ratios of CIM-fusion modes used by the proposed AI edge processor across test sets in the experiment. (D) Measured waveform of wakeup-to-compute latency using the ResNet-20 model trained for the CIFAR-100 dataset.

the high accuracy of the digital SRAM-CIM and the high energy efficiency and storage density of the memristor-CIM, and also enables support for on-chip ALT despite limited device endurance. The SLC-MLC hybrid structure and ALT alleviates the effects of process variation in the mass production of memristor cells, thereby enabling the implementation of CIM using commercial memristors for integration with large-scale logic chips. This work takes memristor technology beyond the in-lab development stages by demonstrating its functionality and manufacturability for large-scale CMOS AI edge processors.

# REFERENCES AND NOTES

1. K. Prabhu et al., IEEE J. Solid-State Circuits 57, 1013–1026 (2022).   
2. D. Rossi et al., “4.4 A 1.3TOPS/W @ 32GOPS Fully Integrated 10-Core SoC for IoT End-Nodes with 1.7mW Cognitive Wake-Up From MRAM-Based State-Retentive Sleep Mode,” 2021 IEEE International Solid- State Circuits Conference (ISSCC, 2021), pp. 60–62.   
3. V. Jain et al., “TinyVers: A 0.8-17 TOPS/W, 1.7 mW-20 mW, Tiny Versatile System-on-chip with State-Retentive eMRAM for Machine Learning Inference at the Extreme Edge,” 2022 IEEE Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits, 2022), pp. 20–21.   
4. P.-C. Wu et al., IEEE J. Solid-State Circuits 59, 196–207 (2024).   
5. H. Mori et al., “A 4nm 6163-TOPS/W/b 4790-TOPS/mm2/b SRAM Based Digital-Computing-in-Memory Macro Supporting Bit-Width Flexibility and Simultaneous MAC and Weight Update,” IEEE International Solid-State Circuits Conference (ISSCC, 2023), pp. 132–134.   
6. Y.-D. Chih et al., 6.4 An 89TOPS/W and 16.3TOPS/mm2 All-Digital SRAM-Based Full-Precision Compute-In Memory Macro in 22nm for Machine-Learning Edge Applications (ISSCC, 2021), pp. 252–254.   
7. H. Fujiwara et al., “A 5-nm 254-TOPS/W 221-TOPS/mm2 Fully-Digital Computing-in-Memory Macro Supporting Wide-Range Dynamic-Voltage-Frequency Scaling and Simultaneous MAC and Write Operations,” 2022 IEEE International Solid- State Circuits Conference (ISSCC, 2022), pp. 1–3.   
8. C.-F. Lee et al., “A 12nm 121-TOPS/W 41.6-TOPS/mm2 All Digital Full Precision SRAM-based Compute-in-Memory with Configurable Bit-width For AI Edge Applications,” 2022 IEEE Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits, 2022), pp. 24–25.   
9. P. Yao et al., Nature 577, 641–646 (2020).   
10. H.-H. Hsu et al., IEEE J. Solid-State Circuits 59, 116–127 (2024).   
11. M. Chang et al., “A 40nm 60.64TOPS/W ECC-Capable Compute-in-Memory/Digital 2.25MB/768KB RRAM/SRAM System with Embedded Cortex M3 Microprocessor for

Edge Recommendation Systems,” 2022 IEEE International Solid-State Circuits Conference (ISSCC, 2022), pp. 1–3.   
12. S. Jung et al., Nature 601, 211–216 (2022).   
13. W. Wan et al., Nature 608, 504–512 (2022).   
14. J. M. Hung et al., Nat. Electron. 4, 921–930 (2021).   
15. W.-S. Khwa et al., “A 40-nm, 2M-Cell, 8b-Precision, Hybrid SLC-MLC PCM Computing-in-Memory Macro with 20.5 - 65.0TOPS/W for Tiny-Al Edge Devices,” 2022 IEEE International Solid-State Circuits Conference (ISSCC, 2022), pp. 1–3.   
16. J.-M. Hung et al., 8-b Precision 8-Mb ReRAM Compute-in-Memory Macro Using Direct-Current-Free Time-Domain Readout Scheme for AI Edge DevicesIEEE Journal of Solid-State Circuits, 58, 303–315 (2023).   
17. Y.-C. Chiu et al., “A 22nm 4Mb STT-MRAM Data-Encrypted Near-Memory Computation Macro with a 192GB/s Read and-Decryption Bandwidth and 25.1-55.1TOPS/W 8b MAC for AI Operations,” 2022 IEEE International Solid-State Circuits Conference (ISSCC, 2022), pp. 178–180.   
18. S. D. Spetalnick et al., “A 40nm 64kb 26.56TOPS/W 2.37Mb/mm2 RRAM Binary/Compute-in-Memory Macro with 4.23x Improvement in Density and >75% Use of Sensing Dynamic Range,” 2022 IEEE International Solid-State Circuits Conference (ISSCC, 2022), pp. 1–3.   
19. T -H. Wen et al., “A 28nm Nonvolatile AI Edge Processor using 4Mb Analog-Based Near-Memory-Compute ReRAM with 27.2 TOPS/W for Tiny AI Edge Devices,” 2023 IEEE Symposium on VLSI Technology and Circuits (VLSI, 2023), pp. 1–2   
20. J.-H. Yoon et al., “A 40nm 100Kb 118.44TOPS/W Ternary-weight Computein-Memory RRAM Macro with Voltage-sensing Read and Write Verification for reliable multi-bit RRAM operation,” 2021 IEEE Custom Integrated Circuits Conference (CICC, 2021), pp. 1–2.   
21. W. S. Khwa et al., “MLC PCM Techniques to Improve Nerual Network Inference Retention Time by 105X and Reduce Accuracy Degradation by 10.8X,” 2021 Symposium on VLSI Technology (VLSI, 2021), pp. 1–2.   
22. C.-X. Xue et al., 2020 IEEE International Solid-State Circuits Conference (ISSCC, 2020), pp. 244–246.   
23. C.-X. Xue et al., 2019 IEEE International Solid- State Circuits Conference (ISSCC, 2019), pp. 388–390.   
24. C.-X. Xue et al., Nat. Electron. 4, 81–90 (2020).   
25. W.-H. Chen et al., 2018 IEEE International Solid - State Circuits Conference (ISSCC, 2018), pp. 494–496.   
26. W. H. Chen et al., Nat. Electron. 2, 420–428 (2019).   
27. R. Mochida et al., “A 4M Synapses integrated Analog ReRAM based 66.5 TOPS/W Neural-Network Processor with Cell Current Controlled Writing and Flexible Network Architecture,” 2018 IEEE Symposium on VLSI Technology (VLSI, 2018), pp. 175–176.   
28. W. Wan et al., 2020 IEEE International Solid-State Circuits Conference (ISSCC, 2020), pp. 498–500.   
29. Q. Liu et al., 2020 IEEE International Solid-State Circuits Conference (ISSCC, 2020), pp. 500–502.   
30. F. Cai et al., Nat. Electron. 2, 290–299 (2019).   
31. C. Li et al., Nat. Electron. 1, 52–59 (2018).   
32. S. Ambrogio et al., Nature 558, 60–67 (2018).

33. D. Ielmini, H. S. P. Wong, Nat. Electron. 1, 333–343 (2018).   
34. C.-C. Chou et al., “A 22nm 96KX144 RRAM Macro with a Self-Tracking Reference and a Low Ripple Charge Pump to Achieve a Configurable Read Window and a Wide Operating Voltage Range,” 2020 IEEE Symposium on VLSI Circuits (VLSI, 2020), pp. 1–2.   
35. I. Boybat et al., Nat. Commun. 9, 2514 (2018).   
36. M. Le Gallo et al., Nat. Electron. 1, 246–253 (2018).   
37. A. Ankit et al., IEEE Trans. Comput. 69, 1128–1142 (2020)   
38. Y.-D. Chih et al., “Design Challenges and Solutions of Emerging Nonvolatile Memory for Embedded Applications,” 2021 IEEE International Electron Devices Meeting (IEDM, 2021), pp. 2.4.1–2.4.4.

# ACKNOWLEDGMENTS

The authors express their appreciation for support from National Tsing Hua University (NTHU), TSMC Corporate Research (TSMC-CR), TSMC Design Technology Platform (TSMC-DTP), TSMC-NTHU Joint Developed Project (JDP), and Nationa Science and Technology Council (NSTC) of Taiwan. We also acknowledge contributions from TSMC colleagues, H.-S. Philip Wong, H. Chuang, W. T. Chu, and K. C. Huang. Funding: Funded internally by the TSMC company. Author contributions: T.-H.W., W.-H.H., and H.-H.H. designed the Memristor-SRAM CIM-Fusion Processor and test-chip. T.-H.W., W.-H.H., H.-H.H., Y.-C.L., C.-J.J., Z.-E.K., Y.-C.C., H.-H.H., Y.-H.C., Y.-H.C. K.-T.T., C.-C.L., R.-S.L., C.-C.H., M.-S.H., and M.-F.C. contributed ideas. T.-H.W., W.-H.H., H.-H.H., Y.-C.L., C.-J.J., W.-S.K., and C.-I.S. built the test measurement system and testing flow for the Memristor-SRAM CIM-Fusion Processor. T.-H.W., W.-H.H., Y.-C.L., and C.-J.J. built the demonstration system. T.-H.W., W.-H.H., Y.-C.L., and C.-J.J. performed analysis and measurements of the Memristor-SRAM CIM-Fusion Processor. C.-C.C., Y.-D.C., T.-Y. C., and M.-F.C. managed the project. Competing interests: The authors declare no competing interests. The patent application titled “MEMORY SYSTEM AND OPERATING METHOD OF THE SAME” is currently pending. Data and materials availability: All data needed to evaluate the conclusions in the paper are included in the paper and/or Supplementary Materials. License information: Copyright © 2024 the authors, some rights reserved; exclusive licensee American Association for the Advancement of Science. No claim to original US government works. https://www.science.org/ about/science-licenses-journal-article-reuse

# SUPPLEMENTARY MATERIALS

science.org/doi/10.1126/science.adf5538

Materials and Methods

Supplementary Text

Figs. S1 to S14

Tables S1 and S2

Submitted 3 December 2022; resubmitted 17 October 2023

Accepted 19 March 2024

10.1126/science.adf5538