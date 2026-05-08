---
title: "Low-power Edge Detection Based on Ferroelectric Field-Effect Transistor"
date: "'2025-01-10'"
year: 2025
journal: "Nature Communications"
doi: "10.1038/s41467-024-00000-0"
abstract: "Edge detection is essential for computer vision applications including image"
abstract_cn: "边缘检测是计算机视觉的核心技术，广泛应用于图像分割、目标检测等领域。报道基于 HfO2 铁电场效应晶体管的低功耗边缘检测硬件系统。提出无需卷积操作的匹配单值段同化核"
cite: "'[1] Chen J J, Xu J C, Gu J N, et al. Low-power edge detection based on ferroelectric"
aiSum: "FeFET 边缘检测：MUSAN 方法无需卷积/ADC，4×4 NAND 阵列，~10 fJ/操作，无精度损失，适用于边缘计算。"
confidence: high
---

Received: 17 April 2024

Accepted: 3 December 2024

Published online: 10 January 2025

Check for updates

Jiajia Chen 1,2, Jiacheng Xu3 , Jiani Gu 3 , Bowen Chen3 , Hongrui Zhang1 , Haoji Qian1,2, Huan Liu1 , Rongzong Shen3 , Gaobo Lin3 , Xiao Yu1,2, Miaomiao Zhang1,2, Yi’an Ding1 , Yan Liu 1,2, Jianshi Tang 4 , Huaqiang Wu 4 , Chengji Jin 1,3 & Genquan Han1,2

Edge detection is one of the most essential research hotspots in computer vision and has a wide variety of applications, such as image segmentation, target detection, and other high-level image processing technologies. However, efficient edge detection is difficult in a resource-constrained environment, especially edge-computing hardware. Here, we report a low-power edge detection hardware system based on [[HfO2]]-based ferroelectric field-effect transistor, which is one of the most potential non-volatile memories for energy-efficient computing. Different from the conventional edge detectors requiring sophisticated hardware for the complex operation such as convolution and gradient, the proposed edge detector is analogue-to-digital converter free and loaded into a multi-bit content addressable memory, which only needs one 4 × 4 ferroelectric field-effect transistor NAND array. The experimental results show that the proposed hardware system is able to achieve efficient image edge detection at low power consumption (~10 fJ/per operation), realizing no-accuracy-loss, low-power and analogue-to-digitalconverter-free hardware system, providing a feasible solution for edge computing.

Edge intelligence refers to the processing and decision-making of data at the device or sensor level, without the need for data transmission to cloud or other remote data centers, thereby enabling more efficient, real-time, secure, and privacy-preserving applications1–5 . Image edge detection, as a key technology in edge intelligence, finds extensive applications in fields such as intelligent security, intelligent transportation, and intelligent manufacturing that require real-time and accurate identification of edge information in images to make intelligent decisions6,7 . Although the development of technologies in recent years such as event-based cameras has significantly reduced hardware power consumption8 . Low-power and high-speed edge detection is still a challenge due to the complex computational steps involved in conventional edge detectors, such as gradient and convolution

operations. In order to overcome this challenge, [[in-memory computing]] (IMC) with emerging non-volatile memories (eNVMs), such as resistive random-access memory ([[ReRAM]])8–11, ferroelectric field-effect transistor ([[FeFET]])12–16, etc. have been widely explored in edge detection. These eNVMs not only achieve on-chip storage with high density, but also show great potential in low-power and high-speed multiplyaccumulate computations, greatly accelerating the computing process and significantly reducing computational power consumption in edge detection.

The main computing core of most eNVMs-based edge detection lies in convolution operations, such as Prewitt, Soble and Laplacian detector as shown in Fig. 1a. By adjusting the conductance of eNVMs in a cross-bar array to represent the elements of the convolutional kernel

1 Hangzhou Institute of Technology, Xidian University, Hangzhou 311231, China. 2 Faculty of Integrated Circuits, Xidian University, Xi’an 710071, China. 3 Research Center for New Materials Computing, Zhejiang Lab, Hangzhou 311121, China. 4 School of Integrated Circuits, Beijing National Research Center for Information Science and Technology, Tsinghua University, Beijing 100084, China. e-mail: jiani_gu@zhejianglab.edu.cn; cjjin@ieee.org

![](images/0baac91f945f1bd2c3605f29017a65ed0dd92da6bd11a0d40022fc242d71d9b7.jpg)  
Fig. 1 | The comparison of the typical edge detectors and the proposed MUSAN edge detector. a Typical edge detectors: Prewitt, Sobel, Laplacian detectors, need convolution operations and ADC to readout. b The eNVMs-based hardware implementation of the typical edge detectors. c The corresponding scheme of   
eNVMs-based convolution operation. d The proposed MUSAN edge detector, combining USAN and feature matching, does not need convolution operations and ADC to readout. e The MCAM-based hardware implementation of the proposed edge detector. f The corresponding scheme of MUSAN operation.

(weights), and summing up the currents of each column through Kirchhoff’s current law with the voltage input related to the pixel value, the total current obtained is read out as the result of the convolution (Fig. 1b). Therefore, theoretically, the eNVMs-based edge detection hardware with convolution operation can achieve low-power and highspeed IMC. However, three kinds of basic challenges exist in hardware implementations of eNVMs-based convolution operations, making it difficult to widely promote eNVMs-based edge detection in practical applications. The first one is the poor robustness, which is due to the convolution operations with eNVMs-based array are of low tolerance for variation and read-out disturbance. The second one is high hardware cost for read-out. Typically, the results of analog convolution need be converted into digital read-out signals with additional analogto-digital converter (ADC), as shown in Fig. 1c, which increases power consuming and introduces additional latency. The last one is the accuracy loss due to the error accumulation of eNVMs-based convolution operations. The situation with low efficiency becomes even worse when floating-point-based approaches are used. Therefore, it is urgent to explore alternative approaches to realize the eNVMs-based edge detection which does not lie in convolution operations.

In this regard, a matching univalue segment assimilating nucleus (MUSAN) method without convolution operations is proposed in this work. The proposed MUSAN combines univalue segment assimilating nucleus (USAN) operator and feature matching method, as shown in Fig. 1d. The hardware system corresponding to MUSAN method is very simple and can be loaded into a multi-bit content addressable memory (MCAM) array as shown in Fig. 1e. Figure 1f shows the proposed MUSAN scheme. Different from the typical eNVMs-based edge detection hardware system in which each convolution operation exhibits power consuming and the analog outputs need to be converted into digital read-out by ADC, the proposed one only exhibits obvious power consuming when feature matching occurs and the match/mismatch

results can be readout by distinguishing high/low current with general purpose input/output (GPIO) instead of ADC. Moreover, the hardware system based on the proposed MUSAN method exhibits high tolerance of performance degradation caused by variation of eNVMs, which results in excellent robustness. The architecture and details of the MUSAN method are presented in this paper, and its high performance and low-power consumption are verified by the hardware implementation with MCAM array based on FeFET. The measurement results show that the proposed FeFET-based MUSAN edge detection is able to achieve image edge detection with low-power consumption (~10 fJ/per operation), ADC-free, and no-accuracy-loss at low hardware cost, providing a feasible solution for edge computing.

# Results

# The proposed MUSAN method

The basic idea of MUSAN is matching USAN feature. Here, USAN feature of pixels is defined as 0/1 for the neighboring pixel with dissimilar/ similar brightness. Figure 2a shows the proposed USAN feature extraction method. We use a cross mask consisting of 9 pixels including 4 vertical ones $\left( P _ { 1 } \sim P _ { 4 } \right)$ , 4 horizontal ones $( P _ { 5 } \sim P _ { 8 } )$ , and a central one $( P _ { 0 } )$ in finding USAN area. The vertical/horizontal USAN feature $( I _ { 1 } { \sim } I _ { 4 } / I _ { 5 } { \sim } I _ { 8 } )$ can be extracted by comparing the gray scale values of $P _ { 1 } { \sim } P _ { 4 } / P _ { 5 } { \sim } P _ { 8 }$ with the one of P0. Ii = 1 represents the similar brightness with central pixel, while Ii = 0 is considered as dissimilar brightness. Figure 2b summarizes the vertical/horizontal USAN feature (UF) of 5 typical image edge locations $( L _ { 2 } \sim L _ { 6 } )$ and 2 non-edge locations $( L _ { 1 } , L _ { 7 } )$ in Fig. 2a. Fig. S1 shows several MUSAN schemes with different matched edge feature (EF), and the corresponding simulation results of edge detection. Among them, 0011/1100 and 1110/0111 are the exact matching EF, while 00XX/XX00 is the fuzzy matching EF $\scriptstyle ( X = 0 / 1 )$ . Compared to 0011/1100, 00XX/XX00 can describe more conditions, i.e. 0011/1100, 0000, 0001/1000, showing better robustness. Here, we

![](images/3076ac3f77f075beefd127f9e7c8ba3c1441006760c73c33d01697148acf525a.jpg)  
a   
USAN feature extraction   
b   
The matched Edge features

Edge location:L2-6 Non-edge location:L1,7   

<table><tr><td>UF</td><td colspan="2">L1</td><td colspan="2">L2</td><td colspan="2">L3</td><td colspan="2">L4</td><td colspan="2">L5</td><td colspan="2">L6</td><td colspan="2">L7</td></tr><tr><td>I1/5</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>I2/6</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>I3/7</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>I4/8</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td></tr></table>

![](images/b5a7d96f935d63d1c978980c1a39de8e96a8d4c1214797950238e93b59632823.jpg)

![](images/1437e9aa0a8ba3ef3e8c55078796ecfc1eea07cc8b34afbfc19b8af4fec364f4.jpg)  
Edge feature 1

![](images/2e2e60dd6175f240782e1bed1925438cd16fc9f6e21dddc1a985bf703a6aebe8.jpg)  
Edge feature 2

![](images/4a47d1fdb476e34d95a6a9f7ffb797c674c6cecfdeb50daeccb4d331b36c2a2c.jpg)  
c   
Flowchart

![](images/2448cd2269efc5d1e53d15529655c53fcbdbdb574adfdc94186c78748b9bcab6.jpg)  
d   
L4 Feature matching

![](images/60cd8dfe624afc5c649ff4183a295b3a8669f4fe64e7fbddffc814ac26e6de1c.jpg)  
× Mismatch   
√ Match

![](images/ceb5af563550c6fd5d366763547b709f729c36a201e58cafbb12adab59867f73.jpg)  
L is edge location   
Fig. 2 | Scheme of the proposed MUSAN method. a USAN feature extraction. b The matched edge features. c The flowchart of the proposed edge detector. d Feature matching process using $L _ { 4 }$ as an example.

combine the fuzzy matching EF with 00XX/XX00 as the primary EF (EF1) and the exact matching EF with 0111/1110 as secondary EF (EF2). The primary EF means that one of vertical and horizontal UF satisfies 00XX/XX00, while secondary EF means that both vertical and horizontal UF satisfy 1110/0111. For example, the vertical or horizontal UF of $L _ { 2 } \sim L _ { 5 }$ satisfies 00XX or XX00, while both vertical and horizontal UF of $\yen 6$ satisfy 1110/0111. According to the analysis above, the flowchart of the proposed feature matching process can be described in Fig. 2c. The feature matching consists of two search-matching processes. The first $\left( 1 _ { \mathrm { s t } } \right)$ search-matching one is for vertical UF $\left( I _ { 1 } \sim I _ { 4 } \right)$ . If the input $I _ { 1 } \sim I _ { 4 }$ matches with $\mathrm { E F _ { 1 } , }$ then output the pixel location as the edge location. Otherwise, the second $( 2 _ { \mathrm { n d } } )$ search-matching one for horizontal UF $( I _ { 5 } \sim I _ { 8 } )$ is performed. If the input $I _ { 5 } \sim I _ { 8 }$ matches with EF1 in the $2 _ { \mathrm { n d } }$ search-matching process, then output the pixel location as the edge location. If the input $I _ { 1 } \sim I _ { 4 }$ matches with $\mathsf { E F } _ { 2 }$ in the ${ \bf 1 _ { s t } }$ search-matching process, and the input $I _ { 5 } \sim I _ { 8 }$ matches with $\mathsf { E F } _ { 2 }$ in the $2 _ { \mathrm { n d } }$ searchmatching one, then also output the pixel location as the edge location. We take $L _ { 4 }$ as an example shown in Fig. 2d. For the ${ \bf 1 _ { s t } }$ search-matching process, the input $I _ { 1 } \sim I _ { 4 }$ of $L _ { 4 }$ (1111) does not match with $\mathsf { E F } _ { 1 }$ (00XX/ XX00). Then, the $2 _ { \mathrm { n d } }$ search-matching process is needed. And the $2 _ { \mathrm { n d } }$ input $I _ { 5 } { \sim } I _ { 8 } \mathbf { o f } L _ { 4 }$ (1100) matches with $\mathsf { E F } _ { 1 }$ (00XX/XX00). Therefore, $L _ { 4 }$ is considered as the edge location. In summary, the proposed MUSAN

edge detection method includes UF extraction, feature matching, and processing of matching results.

To evaluate the performance of the proposed MUSAN method, we compare it with various classical ones, e.g. Prewitt, Sobel, Roberts, Laplacian of Gaussian and SUSAN (smallest USAN) detectors. The masks and schemes of these methods are described in Fig. S2. As mentioned earlier, these detectors are based on convolution operations. In this work, the BSDS500 dataset (200 images) is used to evaluate the ability of the proposed MUSAN detector. Note that the pixel resolution of all the images in BSDS500 dataset is 481 × 321. Here, the precision17, recall17, feature similarity (FSIM)18, and Pratt’s figure of merit (FOM)19 are used as indicators, and their detailed definitions are described in Supplementary. Table. S1 shows the average quality assessment of different edge detection methods for 200 images (BSDS500 dataset). Through these quality assessments, it can be observed that the ability of the proposed MUSAN detector is not inferior to convolution-based detectors. Moreover, in terms of subjective visual perception, the proposed MUSAN detector outperforms SUSAN detector in distinguishing some details (taking the comparison of simulation results in Fig. S3 as an example). Nonetheless, there are still some limitations of the proposed MUSAN detector, i.e. it does not perform as well on higher pixel images. For example, if we adjust the

![](images/da7413cff4265b438835871700f530ae6d5a71f85e0b809680f036a7237c16c9.jpg)

![](images/ac930a7ae6295233f80fc616f70e533c131622a2bcadf34611c348631baae654.jpg)

![](images/afc5273e76609ea17f0ae1ab3bde7e8ed7d059bb4f17d95aed2a29d2f4545a19.jpg)

![](images/58081f606302dd6d891f5aec6237b3dd56b0f9a6cc1bc4a509d3b67d2175418e.jpg)

![](images/3b6d97f1857da43432b17aa82a2416c6c8495c003fc88a19c70dbf1130c1a307.jpg)

![](images/b9b01975d553b2605d17d2f5022f671f944d5280b7604c91a95fb40b97015690.jpg)

![](images/89f525618d506d4fdf24ca26f60d8b8bf8006cdaeb3f098aa002969dac77e540.jpg)  
d

![](images/12dbcfaeef79ec0fbc92b4369d6068ad1096e61537e776aa10c982124d35fc7c.jpg)

![](images/689e50edf777ce4e08da2aa216dba025568740df5aaf386b46b79090cefaf94b.jpg)

![](images/fd58498132ea5811c9f1ea502da88ea7119b7ffaa3723a2aff365ed8adb9e7a7.jpg)

![](images/fc76fb78dac8a242ecaff06d67394882286c40f01e4a3dc02d4115e25e6ec012.jpg)

<table><tr><td rowspan="2">f
Cell
State</td><td colspan="5">Searching</td></tr><tr><td>00: 
VSL=V00 
VSL=VCC-V00</td><td>01: 
VSL=V01 
VSL=VCC-V01</td><td>10: 
VSL=V10 
VSL=VCC-V10</td><td>11: 
VSL=V11 
VSL=VCC-V11</td><td>XX: 
VSL=V00 
VSL=V00</td></tr><tr><td>00</td><td>Match</td><td>Mismatch</td><td>Mismatch</td><td>Mismatch</td><td>Match</td></tr><tr><td>01</td><td>Mismatch</td><td>Match</td><td>Mismatch</td><td>Mismatch</td><td>Match</td></tr><tr><td>10</td><td>Mismatch</td><td>Mismatch</td><td>Match</td><td>Mismatch</td><td>Match</td></tr><tr><td>11</td><td>Mismatch</td><td>Mismatch</td><td>Mismatch</td><td>Match</td><td>Match</td></tr><tr><td>XX</td><td>Match</td><td>Match</td><td>Match</td><td>Match</td><td>Match</td></tr></table>

![](images/54f59ade6cb156c6bb97952f625a94cfdf27f23b1eeaac50426d2a74b99a7876.jpg)  
Fig. 3 | Hardware implementation of edge detector: 4×4 FeFET NAND array. a Schematic illustration of a fabricated FeFET. b Cross-sectional TEM image of W/ TiN/HZO/SiO /Si gate-stack. c Operation mechanisms of MLC FeFET. d MCAM cell   
based on two FeFETs connected in series. e Operations Mechanisms of the multi-bit CAM cell. f The operation table of a MCAM cell. g The edge detector loaded in 4 × 4 FeFET NAND array.

input image pixels (481 × 321) in Fig. S3a into higher pixels (1924 × 1284), the results of the proposed MUSAN detector will lose some details compared to the ones of SUSAN detector. The simulation results of 6 kinds of edge detectors are shown in Fig. S4. This is due to that the cross mask of MUSAN detector consisting only 8 feature pixels, while the SUSAN detector’s mask has 37 pixels. Therefore, if we want to perform edge detection for high pixel images with higher accuracy, we need to expand the MUSAN detector to more feature pixels.

# Hardware implementation of MUSAN edge detector by FeFET NAND array

Next, we introduce hardware implementation of the proposed edge detector. As mentioned above, the proposed edge detector focuses on feature matching including fuzzy matching and exact matching, which can be realized by MCAM. In our design, the proposed edge detector is loaded into a 4 × 4 FeFET NAND array as MCAM. The MCAM functions

originate from the multiple states of ferroelectric by partial polarization switching, which results in multilevel cell (MLC) operations of FeFETs. Figure 3a schematically illustrates the structure of fabricated FeFETs. The details of the device fabrication are shown in Methods. Figure 3b shows the cross-sectional transmission electron microscope (TEM) image of the $\mathsf { W } / \mathsf { T i N } / \mathsf { H Z O } / \mathsf { S i O } _ { 2 } / \mathsf { S i }$ gate stack of a fabricated FeFET. The poly-crystalline nature of ferroelectric HZO is confirmed. Figure 3c illustrates operation mechanisms of MLC FeFET. Four polarization states (i.e., ‘S0’, ‘S1’, ‘S2’, and ‘S3’), and thus threshold voltages $( V _ { \mathrm { T H } } )$ can be tuned by different program pulse amplitudes or widths. The measured read drain current (I )- gate voltage $( V _ { \mathbf { g } } )$ after different write pulse and the corresponding write pulse schemes are shown in Methods and Supplementary. MLC operations are confirmed by the well separated 4 $V _ { \mathrm { T H } }$ states of a transistor.

Here, we designed a CAM cell consisting of two FeFETs connected in series (Fig. 3d), where T0 and T1 are upper and lower FeFETs with

threshold voltages $V _ { \mathrm { T H } 0 }$ and $V _ { \mathrm { T H 1 } } ,$ respectively. Comparing the complementary input with the stored state in a CAM cell through search lines (SLs), the match/mismatch results are sensed according to the current of each match line (ML). By utilizing MLC operations of FeFET, multi-bit CAM functions, including fuzzy matching (XX) and exact matching (00, 01, 10, and 11), can be realized. For fuzzy matching, both T0 and T1 are programed to the lowest $V _ { \mathrm { T H } }$ state (S3) shown in Fig. 3d. Whatever the input search data is, matching always occurs. For exact matching, T0 and T1 are programed to the different $V _ { \mathrm { T H } }$ states shown in Fig. 3d. The input search voltages of SL and SL $( V _ { \mathrm { S l } }$ and $\bar { \nu _ { \mathrm { s L } } } )$ in a cell are complementary, which satisfied $V _ { \mathrm { S L } } + \bar { V _ { \mathrm { S L } } } = V _ { \mathrm { C C } } .$ According to the above-mentioned algorithm and the definition of different states of a CAM cell (i.e., 00, 01, 10, and 11), ML current $( I _ { \mathrm { M L } } )$ - SL voltage $( V _ { \mathrm { S L } } )$ exhibits a current peak (Fig. 3e). The input $V _ { \mathrm { S L } }$ in search operation for each state is set as the corresponding $V _ { \mathrm { S L } }$ where current peak happens (i.e., V00, V01, $V _ { 1 0 } ,$ and $V _ { \mathrm { 1 1 } } )$ . When the input search data exactly matches the stored state of a CAM cell, there will be a high current response. Otherwise, the current response can be negligible. The operation table of the multi-bit CAM cell is summarized in Fig. 3f. The corresponding detailed write and search schemes are shown in Methods and Supplementary.

The proposed edge detector requires parallel fuzzy and exact matching of UF with 4-bits data. Therefore, we choose the 4 × 4 FeFET NAND array (Fig. 3g) for hardware implementation of the proposed algorithm. The stored EFs in 4 columns of FeFET array are 00XX, XX00, 0111, 1110, respectively. Each EF is stored in two FeFET-based MCAM cells in a NAND string. Only the input 4-bit UF fully match the two cells of one column, high current flows in the corresponding ML. Otherwise, these 4 columns will retain negligible current. The schematic diagram is shown in Fig. 3g. This is a key reason why the proposed edge detector hardware consumes low energy. Note that, the proposed MUSAN detector is applicable to various devices, including SRAM (static random-access memory)20, ReRAM21–28, FeFET29,30 and so on, as long as these devices can successfully implement CAM. The detailed comparison of MUSAN detectors based on different devices is given in Supplementary.

# Performance evaluation of MUSAN edge detection hardware system

Figure 4a, b demonstrate the low-power hardware system with $4 \times 4$ FeFET NAND array as the computing core. This system controlled by a field-programmable gate array (FPGA) implements the pre-processing operations based on the UF extraction scheme and realizes postprocessing operations and edge output. The 4 × 4 FeFET NAND array (Fig. 4b) is connected with PCB (Printed Circuit Board) through probe card, and stores the EF of 00XX/XX00/0111/1110. Due to the parasitic capacitance and resistance of devices such as probe card, there is a certain delay time in the hardware system. According to the current responses under different search voltage pulse width (1–100 μs) in Fig. S7, we choose pulse width of $1 0 \mu \mathrm { s }$ for the search operation. Note that, search operation with pulse width of $1 \mu \mathrm { s }$ can be also realized if stable current response is not strictly required. Fig. S8 gives the 2D mapping of measured $I _ { \mathrm { M L } }$ with all 16 kinds of search UF corresponding to 4 kinds of stored EF. In order to distinguish the match and mismatch $I _ { \mathrm { M L } }$ more intuitively, we plot the 3D bar chart corresponding to Fig. S8 in Fig. 4c. The measured minimum match $I _ { \mathrm { M L } }$ is 44.57 nA, and the maximum mismatch $I _ { \mathrm { M L } }$ is 6.62 nA. In this work, the match $I _ { \mathrm { M L } }$ and the mismatch $I _ { \mathrm { M L } }$ can be considered as effective signal and noise signal, respectively. Therefore, the maximum amplitude of the noise signal in search operations does not exceed 15% (6.62 nA/44.57 nA = 14.85%) of the effective signal amplitude, and the noise signal can be easily avoided at the hardware level. The detailed hardware design (Fig. S9) and noise analysis are given in Supplementary. Note that the hardware implementation in this work uses only a 4×4 FeFET array (16 devices), which is exactly suitable for storing the 8 feature pixels of the

proposed MUSAN detector. However, compared with SUSAN detector of 37 feature pixels, the fewer feature pixels lead to the proposed MUSAN detector not performing well on higher pixel images, as mentioned above. Expanding the MUSAN detector to images with higher pixel resolution requires FeFET array with larger size. The corresponding research will be carried out in our future work.

To further estimate the feasibility of the 4 × 4 FeFET NAND array as the computing core of proposed edge detector, the retention, the cycle-to-cycle variation and the endurance have been studied systematically. Figure 4d plots the retention of 4 kinds of stored EF (00XX/XX00/0111/1110). According to the retention characteristic of the match and mismatch currents, the functions of computing core can retain even after >10 years. Fig. S10 shows 10 times current responses under search pulse width of 10 μs with 4 kinds of stored EF and all the matched search UF, illustrating negligible variation of multiple search operations. Fig. S11 depicts the endurance of searchmatch operation with stored EF (00XX) and search UF (0011). After 107 cycles, the match current still can be distinguished well, indicating the excellent endurance of the proposed edge detection hardware system.

Here, we take one image with 481 × 321 pixels (from BSDS500 dataset) shown in Fig. 4e as an example. The pixel information of input image is supplied by the PC (personal computer) terminal. Here, we do not artificially introduce noise into the input images. Figure 4f, g depict the ideal results by software simulation and the experimental results using the proposed edge detection, respectively. Compared with software simulation, the proposed hardware system does not lose any accuracy. Moreover, 200 images (BSDS500 dataset) are input into the proposed hardware system with the FeFET-based MUSAN detector. By point to point pixel comparison, all the hardware outputs show 100% accuracy compared with the simulation results, indicating that the proposed FeFET-based hardware system is the no-accuracy-loss edge detection hardware system. However, the hardware outputs based on convolution operators cannot achieve such high accuracy16,31–33. One of the main reasons is that, for the proposed MUSAN detector, the hardware output of the edge position is 0 and the one of the non-edge position is 1, which is determined by feature matching or not, and is digital in a sense. This leads to higher accuracy, compared to the analog output of convolution operation with the need of ADC to read out.

The power analysis of the proposed FeFET-based MUSAN edge detector is provided in Methods. The power of the proposed FeFETbased MUSAN is relatively low due to two reasons. The first one is that in-memory computing with eNVMs exhibits lower power consumption compared to the computing core with storage-compute separation architecture. The other one is that different from the conventional eNVMs-based edge detectors, in which convolution operations are the computing core and each convolution operation outputs quantitative current, the 4 × 4 FeFET NAND array based on MUSAN only exhibit power consuming (10 fJ/per operation) when feature matching occurs. This means that the proposed hardware system consumes the most power at the edge pixels, resulting in lower power consumption than the conventional eNVMs-based edge detection hardware system.

The comparison between this work and previous eNVMs-based edge detection works is shown in Fig. 4h. To summarize, the hardware power consumption of computing core in this work is as low as 10 fJ/ per operation which is the lowest one reported so far. The power estimation method is described in Methods. Moreover, the hardware system of MUSAN is ADC-free, while the ones of other NVMs-based methods are not. The performance requirements (such as device-todevice variation) for NVMs of MUSAN is tolerant, while the ones of other NVMs-based methods are tough due to the exact values of readout current considered as the convolution results. This is also the reason that the hardware accuracy compared to simulation of NVMs-

![](images/56f1a40ad77934b4778e4846d512761e9ed2299b01fed46b500b57dc72c02601.jpg)  
a

![](images/86e4053cd5ad0244f4a9bb5f4f33323524c8fecdcf8fc03e8f83ad0659936588.jpg)  
c

![](images/871e91103ae95a227021ab2a45d9be8d0dd37faee1ecc6502956df58314e8418.jpg)  
d

![](images/16dbe6268cdbd497e537839f68715c27e497131cf0a2ef5fa8567e409a8da589.jpg)  
e

![](images/56fc4c006cac50d0621ba29c78b1d8b932af643c01442bd615fd2f7d2568e820.jpg)  
f

g

![](images/5a934c73b27fc05890801fa60d0902475ae15c0a9dc4fe9756625fd61c2f1807.jpg)  
Fig. 4 | Hardware implementation of the proposed MUSUN. a Image of the PCB connected with 4 × 4 FeFET NAND array through probe card. b The microscope image of a 4 × 4 FeFET NAND array. c The measured I with all 16 kinds of search UF corresponding to 4 kinds of stored EF. d The retention of 4 kinds of stored EF. Symbols are the experimental data, and the dotted lines are the extrapolation of   
these experimental data. e The input image with 481 × 321 pixels (from BSDS500 dataset). f The simulation results of the proposed MASUN detector corresponding to the input image in Fig. 4e. g The experimental output of the proposed hardware system corresponding to the input image in Fig. 4e. h Comparison of this work with other edge detection hardware.

h   

<table><tr><td>Benchmarks</td><td>Edge detector</td><td>convolution operation</td><td>ADC-free</td><td>Power (nJ)/ per operation</td><td>Power consuming of computing core for non-edge pixels</td><td>Performance requirements for eNVMs</td><td>Accuracy of eNVMs -based hardware</td></tr><tr><td>FeFET [16]</td><td>Sobel filter</td><td>Yes</td><td>No</td><td>~1.2×10-4</td><td>Yes</td><td>Tough</td><td>92%</td></tr><tr><td>ReRAM [31]</td><td>Prewitt filter</td><td>Yes</td><td>No</td><td>~3.3</td><td>Yes</td><td>Tough</td><td>98%</td></tr><tr><td>ReRAM [32]</td><td>Laplace filter</td><td>Yes</td><td>No</td><td>~5.0×10-4</td><td>Yes</td><td>Tough</td><td>92%</td></tr><tr><td>ReRAM [33]</td><td>Laplace filter</td><td>Yes</td><td>No</td><td>~8.0×10-2</td><td>Yes</td><td>Tough</td><td>98%</td></tr><tr><td>This work</td><td>MUSAN</td><td>No</td><td>Yes</td><td>~1.0×10-5</td><td>No</td><td>Tolerant</td><td>100%</td></tr></table>

based convolution methods cannot achieve 100%, while the one of MUSAN can.

# Discussion

We have reported a FeFET-based MUSAN method for edge detection, which combines USAN operator and feature matching method. Our IMC hardware system achieves low-power (10 fJ/per operation), which is much lower than the previous eNVMs-based edge detector with convolution operations. Due to the proposed feature matching

scheme, ADC-free and no-accuracy-loss edge detector hardware can also be realized. In summary, the proposed hardware system has higher robustness, stability and accuracy compared with conventional convolution-based schemes. Our proposed edge detector scheme is also applicable to hardware systems based on other emerging NVMs technologies, which is potentially useful for other AI edge computation that may suffer from stability issues of analog convolution operations. Future work will further study the more universal approach to transforming unstable analog

convolution operations into feature matching operations based on NVMs.

# Methods

# Fabrication of MCAM arrays based on FeFET in NAND configuration

Fabrication started from a lightly doped p-type silicon (Si) substrate. After active area (AA) patterning, shallow trench isolation (STI) was performed for electrical isolation. Then, a dummy gate was formed by thermal oxidation of Si and chemical vapor deposition (CVD) poly-Si. After the $\mathrm { S i } _ { 3 } \mathrm { N } _ { 4 }$ spacer and lightly doped drain (LDD) formation, arsenic ions with 40-keV energy and $4 \times 1 0 ^ { 1 5 } \mathrm { c m } ^ { - 2 }$ dose were implanted for source/drain (S/D). Dopant activation was performed by a spike annealing at 1050 °C. After dummy gate removal, SiO2 interfacial layer (IL) was grown by ozone oxidation for better interface property. Next, 10 nm $\mathsf { H f } _ { 0 . 5 } Z \mathsf { r } _ { 0 . 5 } \mathsf { O } _ { 2 } \left( \mathsf { H Z O } \right)$ was deposited by atomic layer deposition (ALD) using tetrakis (ethylmethylamido) hafnium (TEMAHf) and tetrakis (ethylmethylamino) zirconium (TEMAZr) as precursor, and water vapor $( \mathsf { H } _ { 2 } \boldsymbol { \mathrm { O } } )$ as oxidant. Subsequently, 20 nm TiN and 75 nm W were deposited by sputter and CVD, respectively. To crystallize HZO and induce ferroelectricity, rapid thermal annealing (RTA) was carried out in N ambient at $5 5 0 ^ { \circ } \mathrm { C }$ for 1 min. Finally, interconnects and contact pads are formed for electrical characterization. The gate width/length (W/L) of FeFET devices as well as MCAM arrays characterized in this study is 8μm/0.5μm.

# Operation mechanism of MCAM cells

In our design, MCAM functions originate from MLC operations of FeFET cells. Figure 3c illustrates operation mechanisms of MLC FeFET. Four polarization states (i.e., ‘S0’, ‘S1’, ‘S2’, and ‘S3’), and thus threshold voltages $( V _ { \mathrm { T H } } )$ can be tuned by different program pulse amplitudes or widths. Fig. S5a illustrated the optimized write schemes for four different states of fabricated FeFET cells. The corresponding read $I _ { \mathrm { d } } { \cdot } V _ { \mathrm { g } }$ curves for ten different FeFET cells are plotted in Fig. S5b, which shows tightly controlled four $V _ { \mathrm { T H } }$ states. Fig. S5c plots retention and endurance of a FeFET cell.

The designed MCAM cells with two FeFET connected in series and the defined operation rules are illustrated in Fig. S6a. The input voltages of SL and SL $( V _ { \mathrm { S L } }$ and $V _ { \bar { \mathrm { S L } } } )$ in a cell are complementary. In other words, the sum of $V _ { \mathrm { S L } }$ and $V _ { \bar { \mathrm { S } } \bar { \mathrm { L } } }$ is a fixed value $( V _ { \mathrm { C C } } )$ determined by $V _ { \mathrm { T H } }$ of two FeFETs and an overdrive voltage $( V _ { \mathrm { O V } } )$ . ML current versus SL voltage $( I _ { \mathrm { M L } } \cdot V _ { \mathrm { S L } } )$ exhibits a current peak at different $V _ { \mathrm { S L } }$ according to the stored states as defined in Fig. 3d. The input $V _ { \mathrm { S L } }$ in search operation for each state is set as the corresponding $V _ { \mathrm { S L } }$ where current peak happens (i.e., V00, V01, $V _ { 1 0 } ,$ and $V _ { \mathrm { 1 1 } } )$ . Only if the input search data fully match the stored state of a MCAM cell, both T0 and T1 are on, and high current flows through ML (match). Otherwise, at least one of FeFETs in a cell is off and negligible current flows through ML (mismatch). Figure S6b plots measured $I _ { \mathrm { M L } } \cdot V _ { \mathrm { S L } }$ for 5 different states of a MCAM cell. The search voltage of SL determined from Fig. S5b are 1.75, 1.3, 0.8 and 0.3 V for data 00, 01, 10 and 11, respectively. The search operations are further verified by transient measurement of a MCAM cell as shown in Fig. S6c. $I _ { \mathrm { M L } }$ shows behaviors exactly same as predicted by the operation table illustrated in Fig. 3f. Note that, the operating conditions are crucial for the NAND arrays34. Generally, to prevent program disturbance of the SL or word-line (WL) half selected cells, a program inhibition voltage is applied to the MLs or bit-lines (BLs) of unselected NAND strings. In this work, the program inhibition voltage is set as 3 V, which can ensure the program operations are disturb-free35.

# Hardware system set-up

The hardware system consists of three main parts:

• A power management system that supplies power to other modules.   
• A PCB with FeFETs NAND array and its peripheral circuits. FeFETs NAND array is connected to PCB with probe card. The peripheral

circuits including several sensitive amplifier circuits, row and column decoder circuits, write driver circuits, selective switching circuits and partial digital circuits are bonded and packaged in a stacked way, and they communicate with the outside through the PCB. Due to that the FeFETs NAND array is connected to peripheral circuits by probe cards, a relatively large RC delay is introduced, leading to a large read latency $( - 5 \mu \mathsf { s } )$ ). We estimate that the maximum throughput of the search task $\mathrm { i s } - 4 / ( 5 { \mu } { \mathsf s } ) = 3 . 2 { \mathsf { M b p s } } .$ . It is worth noting that the proposed hardware system is just a prototype system. Previous literatures have claimed that the read latency of on-chip FeFET arrays can be within $1 { \mathsf { n } } { \mathsf { s } } ^ { 3 6 }$ . This means that the corresponding throughput will be greatly improved if RC delay is reduced by avoiding probe card. Therefore, the throughput will be greatly increased if we encapsulate the FeFETs NAND array and peripheral circuits into a chip. The corresponding research will be carried out in our future work.

• An FPGA board with an embedded processor is responsible for data management between the FeFETs NAND array and the host computer as well as the control of the peripheral circuits for FeFETs NAND array.

# Power estimation

The hardware system of proposed MUSUN detector based on FeFETs NAND array is advantageous in energy consumption.

• Power analysis of FeFETs array.

Firstly, the power consumption per operation of the proposed FeFET-based MUSUN detector is very low. Fig. S12 gives the methods of power estimation per operation for this work and previous eNVMs-based edge detection works16,31–33. In this work, per operation means high current is captured on a certain ML in 4 × 4 FeFETs NAND array, i.e. feature matching condition. Therefore, the power consumption per operation can be represented as $E = V _ { \mathrm { M L } } \times I _ { \mathrm { M L } } \times t = - 0 . 2 \lor \times 5 0 \mathrm { n A } \times 1 \mu \mathrm { s } = \ – 1 0 \quad \mathrm { ~ f } \mathrm { J } ,$ where $I _ { \mathrm { M L } }$ is the current of ML for feature matching, $V _ { \mathrm { { M L } } }$ is the voltage of ML, and t is pulse width, respectively. For NVM-based convolutional detector, per operation means one single convolution operation. Taking FeFET-based convolution in Ref. 16 as an example, there are two convolution kernels (X-mask and Ymask). The power consumption per operation is defined as the energy of performing one convolution with these two convolution kernels in 9 × 4 FeFET array, and can be evaluated as ${ \cal E } = { V _ { \mathrm { B L } } } ^ { 2 } \times { \cal G } \times t \times n _ { \mathrm { N V M } } = ( 0 . 1 \mathrm { V } ) ^ { 2 } \times \cdot 1 \mathrm { \Delta } \mu \mathrm { S } \times 1 \mathrm { \Delta } \mu \mathrm { S } \times 1 2 = - 1 2 0 \mathrm { \Delta } \mathrm { f } \mathrm { \Delta } ( \mathrm { F i g . } \mathrm { S } 1 2 ) \mathrm { \Delta } \mu \mathrm { S } \times \mathrm { \Delta }$ . Here, $V _ { \mathrm { B L } }$ is the voltage of BL, G and $n _ { \mathrm { N V M } }$ is conductance and number of NVMs under high conductance state, respectively. And n depends on the number of non-zero elements in the mask. Note that, we uniformly adopt a pulse width of 1 μs to estimate the power consumption of this work and previous eNVMs-based edge detection works for fair. Secondly, the 4 × 1 FeFETs connected in series are conductive only when feature matching occurs. For example, for the image with 481 × 321 pixels in Fig. 4e, the feature matching occurs 27960 times, resulting in the total power consuming of $1 0 \uparrow \uparrow \times 2 7 9 6 0 = 0 . 2 8 \mathsf { n } \jmath$ . While the classical method based on convolution in Ref. 16 needs 481 × 321 = 154401 times convolution operations, resulting 120 fJ × 154401 = 18.5 nJ. Therefore, for one whole image, the proposed FeFET-based MUSAN detector exhibits more significant advantage in power consumption.

• Power analysis of peripheral circuits.

Different from the typical eNVMs-based edge detection hardware system where the analog outputs need to be converted into digital read-out by ADC, in the proposed one the outputs can be readout by distinguishing high/low current with general purpose input/output (GPIO) instead of ADC. This leads to both direct and indirect power savings can be achieved in the following circuits in actual application scenarios. Firstly,

the direct power savings. The power consumption of driving an ADC pin and peripheral circuits is about 150 mW which can be referred to the device handbook of FPGA (CYCLONE IV). However, the power consumption of driving a GPIO pin and its peripheral circuits can usually be controlled within 5 mW, much <150 mW. Therefore, at this point, more than 145 mW of power consumption can be saved. Secondly, the indirect power savings. For conventional DC-DC chips, the working efficiency is usually around 90%. The power consumption savings on the chip side can be further reflected indirectly in the power supplies at all levels. The 145 mW chip-side power consumption savings means about 15 mW or more of the power chip thermal power consumption savings.

# Data availability

The data supporting this study and the source data of all the plots of main manuscript and supplementary information are available via Zenodo at https://doi.org/10.5281/zenodo.13808606. The BSDS500 dataset37 used to evaluate the edge detection methods discussed in this study is publicly available and can be accessed at https://github. com/BIDS/BSDS500.

# Code availability

The codes for all the simulations supporting this study are available via Zenodo at https://doi.org/10.5281/zenodo.13808606.

# References

1. Soliman, T. et al. First demonstration of in-memory computing [[crossbar]] using multi-level cell FeFET. Nat. Commun. 14, 6348 (2023).   
2. Kazemi, A. et al. Achieving software-equivalent accuracy for hyperdimensional computing with ferroelectric-based in-memory computing. Sci. Rep. 12, 19201 (2022).   
3. Wu, G. et al. Ferroelectric-defined reconfigurable homojunctions for in-memory sensing and computing. Nat. Mater. 22, 1499–1506 (2023).   
4. Chiu, Y.-C. et al. A CMOS-integrated spintronic compute-inmemory macro for secure AI edge devices. Nat. Electron 6, 534–543 (2023).   
5. Ning, H. An in-memory computing architecture based on a duplex two-dimensional material structure for in situ machine learning. Nat. Nanotechnol. 18, 493–500 (2023).   
6. Sun, R. et al. Survey of image edge detection. Front. Signal Process. 2, 826967 (2022).   
7. Muntarina, K., Shorif, S. B. & Uddin, M. S. Notes on edge detection approaches. Evol. Syst. 13, 169–182 (2022).   
8. Gallego, G. et al. Event-based vision: a survey. IEEE Trans. Pattern Anal. Mach. Intell. 44, 154–180 (2022).   
9. Li, C. et al. Analogue signal and image processing with large memristor crossbars. Nat. Electron. 1, 52–59 (2017).   
10. Huo, Q. et al. A computing-in-memory macro based on threedimensional resistive random-access memory. Nat. Electron. 5, 469–477 (2022).   
11. Gong, T. et al. A 128 kb stochastic computing chip based on [[RRAM]] flicker noise with high noise density and nearly zero autocorrelation on 28 nm CMOS platform. In IEEE International Electron Devices Meeting (IEDM) 12.5.1-12.5.4 (IEEE, 2021).   
12. Lin, P. et al. Three-dimensional memristor circuits as complex neural networks. Nat. Electron. 3, 225–232 (2020).   
13. Behbahani, F., Jooq, M. K. Q., Moaiyeri, M. H. & Tamersit, K. Leveraging negative capacitance CNTFETs for image processing: an ultra-efficient ternary image edge detection hardware. IEEE Trans. Circuits Syst. I 68, 5108–5119 (2021).   
14. Eslahi, H., Hamilton, T. J. & Khandelwal, S. Energy-efficient ferroelectric field-effect transistor-based oscillators for [[neuromorphic]]

system design. IEEE J. Explor. Solid State Comput. Devices Circuits 6, 122–129 (2020).   
15. Yu, E. et al. Ferroelectric FET based coupled-oscillatory network for edge detection. IEEE Electron Device Lett. 42, 1670–1673 (2021).   
16. Kim, M. K., Kim, I. J. & Lee, J. S. CMOS-compatible compute-inmemory accelerators based on integrated ferroelectric synaptic arrays for convolution neural networks. Sci. Adv. 8, eabm8537 (2022).   
17. Tariq, N., Hamzah, R. A., Ng, T. F., Wang, S. L. & Ibrahim, H. Quality assessment methods to evaluate the performance of edge detection algorithms for digital image: a systematic literature review. IEEE Access 9, 87763–87776 (2021).   
18. Zhang, L., Zhang, L., Mou, X. & Zhang, D. FSIM: A feature similarity index for image quality assessment. IEEE Trans. Image Process. 20, 2378–2386 (2011).   
19. Yi, S., Labate, D., Easley, G. R. & Krim, H. A shearlet approach to edge analysis and detection. IEEE Trans. Image Process. 18, 929–941 (2009).   
20. Hayashi, I. et al. A 250 MHz 18 Mb full ternary CAM with low-voltage matchline sensing scheme in 65 nm CMOS. IEEE J. Solid-State Circuits 48, 2671–2680 (2013).   
21. Zheng, L. et al. RRAM-based TCAMs for pattern search. In 2016 IEEE International Symposium on Circuits and Systems (ISCAS) 1382–1385 (IEEE, Montreal, QC, Canada, 2016).   
22. Pan, K., Tosson, A. M. S., Wang, N., Zhou, N. Y. & Wei, L. A novel cascadable TCAM using RRAM and current race scheme for highspeed energy-efficient applications. IEEE Trans. Nanotechnol. 22, 214–221 (2023).   
23. Li, J., Montoye, R. K., Ishii, M. & Chang, L. 1 Mb 0.41 µm2 2T-2R cell nonvolatile TCAM with two-bit encoding and clocked selfreferenced sensing. IEEE J. Solid State Circuits 49, 896–907 (2014).   
24. Lin, C.-C. et al. 7.4 A 256b-wordlength ReRAM-based TCAM with 1 ns search-time and 14× improvement in wordlengthenergyefficiency-density product using 2.5T1R cell. In 2016 IEEE International Solid-State Circuits Conference (ISSCC) 136–137 (IEEE, San Francisco, CA, USA, 2016).   
25. Yin, X. et al. FeCAM: A universal compact digital and analog content addressable memory using ferroelectric. IEEE Trans. Electron Devices 67, 2785–2792 (2020).   
26. Bazzi, J., Sweidan, J., Fouda, M. E., Kanj, R. & Eltawil, A. M. Variabilityaware design of RRAM-based analog CAMs. IEEE Access 12, 55859–55873 (2024).   
27. Li, C. et al. Analog content-addressable memories with memristors. Nat. Commun. 11, 1638 (2020).   
28. Ni, K. et al. Ferroelectric ternary content-addressable memory for one-shot learning. Nat. Electron 2, 521–529 (2019).   
29. Das, D. et al. Experimental demonstration and modeling of a ferroelectric gate stack with a tunnel dielectric insert for NAND applications. In 2023 International Electron Devices Meeting (IEDM) 1–4 (IEEE, San Francisco, CA, USA, 2023).   
30. Kim, I.-J. & Lee, J.-S. Unlocking large memory windows and 16-level data per cell memory operations in hafnia-based ferroelectric transistors. Sci. Adv. 10, eadn1345 (2024).   
31. Oh, S. et al. Energy-efficient Mott activation neuron for fullhardware implementation of neural networks. Nat. Nanotechnol. 16, 680–687 (2021).   
32. Hong, E. et al. Convolutional kernel with PrCaMnOx-based resistive random-access memory for neuromorphic image processing. AIP Adv. 13, 015318 (2023).   
33. Jeon, S. et al. Hybrid precision in resistive memory-based convolutional kernel for fault-resilient neuromorphic systems. IEEE Trans. Electron Devices 70, 1659–1663 (2023).   
34. Kim, M.-K., Kim, I.-J. & Lee, J.-S. CMOS-compatible ferroelectric NAND flash memory for high-density, low-power, and high-speed three-dimensional memory. Sci. Adv. 7, eabe1341 (2021).

35. Jin, C. et al. Disturb-free operations of multilevel cell ferroelectric FETs for nand applications. IEEE Trans. Electron Devices 70, 1653–1658 (2023).   
36. Genssler, P. R., Van Santen, V. M., Henkel, J. & Amrouch, H. On the reliability of FeFET on-chip memory. IEEE Trans. Comput. 71, 947–958 (2022).   
37. Arbeláez, P., Maire, M., Fowlkes, C. & Malik, J. Contour detection and hierarchical image segmentation. IEEE Trans. Pattern Anal. Mach. Intell. 33, 898–916 (2011).

# Acknowledgements

This work was supported in part by the National Key R&D Program of China (No. 2023YFB4402303) and in part by the National Natural Science Foundation of China (No. 62204229, 62204228, 62204226, and 62025402).

# Author contributions

J.C., J.G. and C.J. proposed and implemented the project. J.X., B.C., H.Z., H.Q., H.L. R.S. G.L. X.Y. M.Z. and Y.D. designed the chip and performed the experimental verification of the proposed design. J.C. conducted MATLAB simulations and verification. Y.L., J.T., H.W. and G.H. helped with data analysis. All authors contributed to write up of the manuscript. G.H. organized and supervised the whole project implementation and provided the project financial support.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-024-55224-8.

Correspondence and requests for materials should be addressed to Jiani Gu or Chengji Jin.

Peer review information Nature Communications thanks the anonymous reviewers for their contribution to the peer review of this work. A peer review file is available.

Reprints and permissions information is available at http://www.nature.com/reprints

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http:// creativecommons.org/licenses/by-nc-nd/4.0/.

© The Author(s) 2025

# Terms and Conditions

Springer Nature journal content, brought to you courtesy of Springer Nature Customer Service Center GmbH (“Springer Nature”).

Springer Nature supports a reasonable amount of sharing of research papers by authors, subscribers and authorised users (“Users”), for smallscale personal, non-commercial use provided that all copyright, trade and service marks and other proprietary notices are maintained. By accessing, sharing, receiving or otherwise using the Springer Nature journal content you agree to these terms of use (“Terms”). For these purposes, Springer Nature considers academic use (by researchers and students) to be non-commercial.

These Terms are supplementary and will apply in addition to any applicable website terms and conditions, a relevant site licence or a personal subscription. These Terms will prevail over any conflict or ambiguity with regards to the relevant terms, a site licence or a personal subscription (to the extent of the conflict or ambiguity only). For Creative Commons-licensed articles, the terms of the Creative Commons license used will apply.

We collect and use personal data to provide access to the Springer Nature journal content. We may also use these personal data internally within ResearchGate and Springer Nature and as agreed share it, in an anonymised way, for purposes of tracking, analysis and reporting. We will not otherwise disclose your personal data outside the ResearchGate or the Springer Nature group of companies unless we have your permission as detailed in the Privacy Policy.

While Users may use the Springer Nature journal content for small scale, personal non-commercial use, it is important to note that Users may not:

1. use such content for the purpose of providing other users with access on a regular or large scale basis or as a means to circumvent access control;   
2. use such content where to do so would be considered a criminal or statutory offence in any jurisdiction, or gives rise to civil liability, or is otherwise unlawful;   
3. falsely or misleadingly imply or suggest endorsement, approval , sponsorship, or association unless explicitly agreed to by Springer Nature in writing;   
4. use bots or other automated methods to access the content or redirect messages   
5. override any security feature or exclusionary protocol; or   
6. share the content in order to create substitute for Springer Nature products or services or a systematic database of Springer Nature journal content.

In line with the restriction against commercial use, Springer Nature does not permit the creation of a product or service that creates revenue, royalties, rent or income from our content or its inclusion as part of a paid for service or for other commercial gain. Springer Nature journal content cannot be used for inter-library loans and librarians may not upload Springer Nature journal content on a large scale into their, or any other, institutional repository.

These terms of use are reviewed regularly and may be amended at any time. Springer Nature is not obligated to publish any information or content on this website and may remove it or features or functionality at our sole discretion, at any time with or without notice. Springer Nature may revoke this licence to you at any time and remove access to any copies of the Springer Nature journal content which have been saved.

To the fullest extent permitted by law, Springer Nature makes no warranties, representations or guarantees to Users, either express or implied with respect to the Springer nature journal content and all parties disclaim and waive any implied warranties or warranties imposed by law, including merchantability or fitness for any particular purpose.

Please note that these rights do not automatically extend to content, data or other material published by Springer Nature that may be licensed from third parties.

If you would like to use or distribute our Springer Nature journal content to a wider audience or on a regular basis or in any other manner not expressly permitted by these Terms, please contact Springer Nature at