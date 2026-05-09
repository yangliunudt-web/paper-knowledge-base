---
title: "Demonstration of Differential Mode FeFET-Array for multi-precision storage"
authors:
  - "Vivek Parmar"
  - "Franz Müller"
  - "Jing-Hua Hsuen"
  - "Sandeep Kaur Kingra"
  - "Yannick Raffel"
  - "Maximillian Lederer"
  - "Tarek Ali"
  - "Stefan Dünkel"
  - "Konrad Seidel"
  - "Sven Beyer"
  - "Tian-Li Wu"
  - "Thomas Kämpfe"
  - "Sourav De"
  - "Manan Suri"
date: "2023-12-01"
year: "2023"
journal: "IEEE International Electron Devices Meeting (IEDM)"
abstract: "Harnessing multibit precision in non-volatile memory (NVM) based synaptic"
abstract_cn: "利用基于非易失性存储器的突触核心的多比特精度可以加速深度神经网络的乘加运算。然而，基于NVM的突触核心在比特密度和性能之间存在权衡。随着缩放带来的性能下降、有限的比特精度以及与权重更新相关的不对称性，成为实现高密度突触核心的严重瓶颈。本工作展示了：(i)"
keywords:
  - "[[FeFET]]"
  - "[[In-memory computing]]"
cite: "[1] Parmar V, Müller F, Hsuen J H, et al. Demonstration of differential mode"
aiSum: "差分模式FeFET阵列：12 Kbit容量、223Mb/mm²密度、VGG-8能效196 TOPS/W、1% BER下训练精度94%/推理精度88%。"
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
  - "[[In-memory computing]]"
---

# Demonstration of Differential Mode [[FeFET]]-Array for multi-precision storage and IMC applications

Vivek Parmar1, Franz Müller2, Jing-Hua Hsuen3, Sandeep Kaur Kingra1, Yannick Raffel2, Maximillian Lederer2, Tarek Ali5, Stefan Dünkel5, Konrad Seidel2, Sven Beyer5, Tian-Li Wu3,4, Thomas Kämpfe2, Sourav De2, Manan Suri1

1 Indian Institute of Technology Delhi, New Delhi, India 2 Fraunhofer IPMS-CNT, Dresden, Germany 3 Institute of Pioneer Semiconductor Innovation, National Yang Ming Chiao Tung University, Taiwan 4 International College of Semiconductor Technology, National Yang Ming Chiao Tung University, Taiwan, 5 GlobalFoundries’, Dresden, Germany. E-mail: manansuri@ee.iitd.ac.in, tlwu@nycu.edu.tw, sourav.de@ipms.fraunhofer.de

Abstract— Harnessing multibit precision in non-volatile memory (NVM) based synaptic core can accelerate multiply and accumulate (MAC) operation of deep neural network (DNN). However, NVM-based synaptic cores suffer from the trade-off between bit density and performance. The undesired performance degradation with scaling, limited bit precision, and asymmetry associated with weight update poses a severe bottleneck in realizing a high-density synaptic core. In this work, we demonstrate: (i) implementation of novel differential mode [[ferroelectric]] field effect transistor (FeFET) (DM-FeFET) based multibit [[crossbar]] array of 12 Kbit size. (ii) bit density of 223Mb/mm2, which is ~2x improvement compared to conventional FeFET array; (iii) 196 TOPS/W energy efficiency for VGG-8 network and (iv) superior bit error rate (BER) resilience showing ~94% training and 88% inference accuracy with 1% BER.

# I. INTRODUCTION

Recent progress in the research of [[hafnium oxide]] ([[HfO2]]) based ferroelectric (Fe) memories has manifested its potential as next-generation non-volatile memory (eNVM). Compatibility with standard CMOS technology, superior endurance, and data retention enabled very-large-scale integration (VLSI) of FeFET-based macro [1,2]. However, the major drawback lies in the device-to-device variation $( \Delta I ^ { \dot { D } 2 D } d d )$ in the drain current of the FeFET cells, especially for low threshold voltage (LVT) state [1-3], which hinders high precision arithmetic operations. Although the scientific community has spent significant effort in improving this from the process and device point of view, most demonstrations are limited to standalone devices [4,5]. A previous report on 1F-1R devices shows mitigation of ∆ID2Dd in FeFET however it is limited to 1 bit/cell operation [6]. In this work, we focus on implementing a DM-FeFET array macro for performing multi-level MAC operations. Fig. 1(a) compares the proposed synaptic cell with other state-of-art memory cells at the array level. The proposed structure can be easily mapped to a standard FeFET crossbar with only periphery-level changes. For the current study, a DM-FeFET-based 12 Kbit memory array was fabricated along with peripheral circuits and analogto-digital converters (ADCs) using 28nm HKMG technology (shown in Fig. 1(b)). Program-erase operations conducted on 60 devices across a 300 mm wafer showing D2D variations as mentioned above are shown in Fig, 1(c). Schematic of the inmemory-computing (IMC) array is shown in Fig. 1(d)). The IBL from each column of a crossbar is connected to the input of 3-bit current-mode ADCs. Experimentally obtained results from the MAC-unit were statistically modelled for convolutional neural network (CNN) simulations which achieved inference accuracies >88% for varying bit-precision on the CIFAR-10 dataset.

# II. DM-FEFET IMC ARRAY

Proposed Bitcell: Encoding of state for multiple precision using the bitcell is shown in Fig. 2(a). Fig. 2(b) shows the realization of the DM-FeFET cell over a fabricated FeFET crossbar through mapping by sharing the cells across a column. Current-limiter (CL) transistors were used at the end of each column to reduce the impact of $\Delta I ^ { D 2 D } d$ in BL-current (IBL). The impact of improvement in sensing margin at a constant $V _ { r e a d }$ using the proposed scheme is shown in Fig. 2(ce) for program-based MLC and Fig. 2(e-f) for erase-based MLC. The resulting 2-bit states from the DM-FeFET configuration show a well-separable sense margin. Next, we evaluated BER/error probabilities for proposed DM-FeFET bit cells for 2b states using both program and erase (Fig. 3(a)). We can observe BER improvement of the order of 3x compared to the conventional scheme. As an application demonstration, simulated programming of 32x32 crossbar arrays to represent an image using conventional MLC states and DM-FeFET was performed. This further validates the BER improvement (see Fig. 3(b)) with the proposed scheme showing BER<1%.

CNN Simulations: Using weight-mapping strategy described in Fig. 2(b) NN simulations were performed for 3 precisions (binary, ternary, 3-bit). Since applied inputs are intended to be constant voltage pulses, inputs and outputs are both assumed to be binary for MAC operation. For application validation, VGG-8-based CNN (see Fig. 4 (a)) was trained over the CIFAR-10 dataset after binarizing input using thermometric encoding. Three network schemes are described based on the precision of weight and activation as XWBA, where X is B: binary, T: ternary, and Q: 3-bit. Evolution of training accuracy is shown in Fig. 4(b). Next, we evaluated the impact of device programming variability on the accuracy of binary MAC operations using different weight precisions. Finally, we evaluated the impact of BER on network accuracy (Fig. 4(c)). Cut-off BER=1% is achieved across all weight precisions.

# III. CONCLUSION

28nm HKMG technology-based [[CIM]]-macro with FeFETbased IMC core has been demonstrated. The differential mode of operation in the FeFET-based crossbar array shows an improvement in current-based sensing and MLC-MAC operation. AI Application workload (CNN) was used to benchmark the performance of the DM-FeFET crossbar array over multiple precision, yielding the highest training accuracy of 94% over the CIFAR-10 dataset. DM-FeFET shows improvement in BER performance in MAC operations by up to 3x for 2b storage. The current implementation achieves a very high energy efficiency, storage density, and comparable accuracy on CIFAR-10 compared to other implementations in literature.

<table><tr><td>(a)</td><td>1T1R [7]</td><td>2FeFET+1T [8]</td><td>1T-FeFET [9]</td><td>2T1C[10]</td><td>2FeFET[This Work]</td></tr><tr><td>Cell Structure</td><td>R</td><td>MLP
SLS
MLS</td><td></td><td></td><td>SL
BL</td></tr><tr><td>Tech. Node</td><td>22 nm</td><td>28 nm</td><td>22 nm</td><td>28 nm</td><td>28 nm</td></tr><tr><td>Bit Density</td><td>2 bit/cell</td><td>2 bit/cell</td><td>2 bit/cell</td><td>2 bit/cell</td><td>3 bit/cell</td></tr><tr><td>Mb/mm2</td><td>1.43</td><td>31.79</td><td>131.36</td><td>28.05</td><td>223.52</td></tr></table>

![](images/527d5d7ee96081a139337bb83be1f8e724eec177f7084dafbad2c84642d786c2.jpg)

![](images/a2301a1c1085cfde3befa65a9744d5a662a0571c7c72714ce2ebc23f5bcf960b.jpg)

![](images/224380bcdd82db1cf11d34286ddf2f67733b04a7f2577e54f82696c0b5f09427.jpg)

![](images/040a1a43efb40fb0893eedecc37f9842c545bfe0d83f150fa1628197d9b1cc5d.jpg)  
Fig. 1. (a) Comparison of this work with state-of-the-art synaptic arrays. 3 bits/cell operation with 2-FeFETs working in differential mode improves the bit density. (b) 3D illustration of fabricated IMC array. (c) Characterization of program-erase operations for sixty standalone devices shows D2D variations over 300mm wafer. The FeFETs were programmed and erased with 500ns pulses. (d) Schematic of fabricated FeFET array.

![](images/b5ceeebc254199ca4584e05258fa1883809c4c32bb6fa68db8f9ddb4c4138886.jpg)

<table><tr><td colspan="3">Conventional MLC scheme</td></tr><tr><td>State</td><td>VPGM(V)</td><td>VERS(V)</td></tr><tr><td>S1</td><td>1.5</td><td>-5.1</td></tr><tr><td>S2</td><td>3.1</td><td>-4.1</td></tr><tr><td>S3</td><td>3.7</td><td>-3.5</td></tr><tr><td>S4</td><td>5.5</td><td>-2.1</td></tr></table>

DM-FeFET Scheme   

<table><tr><td>Data</td><td>D1</td><td>D2</td></tr><tr><td>-2</td><td>S1</td><td>S4</td></tr><tr><td>-1</td><td>S1</td><td>S3</td></tr><tr><td>0</td><td>S1</td><td>S1</td></tr><tr><td>1</td><td>S3</td><td>S1</td></tr></table>

![](images/48531971a635f50610ab79e90a68799d31e9edea9bbcc83d22c72a0e3207e44f.jpg)  
Fig.2. (a) Encoding schemes for multi-precision weights using DM-FeFET. (b) Schematic representation of DM-FeFET crossbar array demonstrates the operation of IMC bitcell. Statistical distribution of $\mathrm { { I } } _ { \mathrm { { r e a d } } }$ for weight encoding schemes: (c,e) Conventional MLC; (d,f) Differential MLC. Inset on top left for conventional schemes shows overlap in $\mathrm { { I } } _ { \mathrm { { r e a d } } }$ distributions for the lower MLC states (S1-S3)

![](images/17d6b2722229899a55a26532af7793565c453228606722dd30424559540f8fbc.jpg)

![](images/aea1a7eba27d206449167a9f406ae7ed70ff419aeeeeb1aeb2695a8a87c82473.jpg)  
Fig. 3. (a) Error probability calibrated over 1000 samples with conventional and DM-FeFET programming schemes, showing improvement in BER in program-erase operation achieved by DM operation. (b) 2-bit image of “SuperMario” written over a 32x32 matrix proves this fact.

![](images/1fc1fcee3898bf634f5cac5978f9d8e778af463bf811bb44b666c8c41ca5362a.jpg)  
(a)   
Fig 4. (a) CNN architecture used for the study (VGG-8). (b) Training accuracy evolution over 30 epochs for CIFAR-10 dataset. (c) Impact of binary MAC output BER on accuracy performance shows BER tolerance of upto 1%.

Acknowledgement: This work was supported in part by PSA-Prn.SA/Nanoelectronics/2017, IIT-Delhi, German Bundesministerium für Wirtschaft (BMWI) and by the State of Saxony in the frame of the “Important Project of Common European Interest (IPCEI) and European Union's ECSEL Joint Undertaking under grant agreement no. 876925 - project ANDANTE

# REFERENCES

[1] S. De et al., VLSI, 2021, pp. 1-2. [2] S. De et al.,2022 Frontiers in Nanotechnology. [3] S. De et al.,VLSI-TSA, 2022, pp. 1-2. [4] S. De et al., ACS Applied Electronic Materials, 2021 [5] M. Lederer, et al., IEEE TED 2021. [6] T. Soliman et al., IEDM, 2020 [7] D. Saito et al., VLSI, 2021, pp. 1-2. [8] C. Li et al., IEDM, 2020, pp. 29.3.1- 29.3.4. [9] S. Dutta et al., IEDM, 2020, pp. 36.4.1-36.4.4. [10] D. Saito et al., TED 2020, vol. 67, no. 11, pp. 4616-4620.