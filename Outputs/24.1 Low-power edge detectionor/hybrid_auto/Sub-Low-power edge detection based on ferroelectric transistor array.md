---
title: "Sub-Low-power edge detection based on ferroelectric transistor array"
authors:
  - "Author"
date: "2023-01-01"
year: 2023
journal: "IEEE TED"
abstract: "Supplementary materials for low-power edge detection using ferroelectric transistor arrays. Contains additional experimental data and analysis."
abstract_cn: "使用铁电晶体管阵列的低功耗边缘检测补充材料。包含额外实验数据和分析。"
keywords:
  - "[[[[Edge Detection]]]]"
  - "[[[[FeFET]]]]"
  - "[[[[Ferroelectric Transistor]]]]"
  - "[[[[Low-Power]]]]"
  - "[[[[边缘检测]]]]"
cite: "Author. Low-power edge detection based on ferroelectric transistor array[J]. IEEE TED, 2023."
aiSum: "边缘检测补充材料：器件特性、阵列配置、处理结果。"
confidence: "medium"
parent:
  - "[[Low-power edge detection based on ferroelectric field-effect transistor]]"
---

# Low-power Edge Detection Based on Ferroelectric Field-Effect Transistor

Jiajia Chen1,2, Jiacheng Xu3, Jiani Gu3,*, Bowen Chen3, Hongrui Zhang1, Haoji Qian1,2, Huan Liu1, Rongzong Shen3, Gaobo Lin3, Xiao Yu1,2, Miaomiao Zhang1,2, Yi’an Ding1, Yan Liu1,2, Jianshi Tang4, Huaqiang Wu4, Chengji Jin1,3,*, and Genquan Han1,2

1Hangzhou Institute of Technology, Xidian University, Hangzhou 311231, China.

2Faculty of Integrated Circuits, Xidian University, Xi’an 710071, China.

3Research Center for New Materials Computing, Zhejiang Lab, Hangzhou 311121, China.

4School of Integrated Circuits, Beijing National Research Center for Information Science and Technology, Tsinghua University, Beijing 100084, China.

*Email: jiani_gu@zhejianglab.edu.cn, cjjin@ieee.org

# 1. MUSAN schemes with different matched edge feature

![](images/4892fb83b166613ab4940aca9873581439548b5241e7c292ff628049387cb8ef.jpg)  
Fig. S1 The simulated results comparison of MUSAN with different matched edge feature.

# 2. The comparison of MUSAN with classical edge detectors

The precision17 is defined as:

$$
\text {P r e c i s i o n} = \frac {\mathrm {T P}}{\mathrm {T P} + \mathrm {F P}}, \tag {1}
$$

and the recall17 is defined as:

$$
\text {R e c a l l} = \frac {\mathrm {T P}}{\mathrm {T P} + \mathrm {F N}}, \tag {2}
$$

where TP, FN and FP are the number of true positive, false negative, and false positive, respectively.

FOM 19 is defined as:

$$
F O M = \frac {1}{\max \left(N _ {E} , N _ {G}\right)} \sum_ {k = 1} ^ {N _ {E}} \frac {1}{1 + \alpha d ^ {2} (k)}, \tag {3}
$$

where $N _ { G }$ is the number of the actual edges, $N _ { E }$ is the number of the detected edges by the algorithm, α is the scaling constant, and $d ( k )$ is the displacement of the detected edge from the actual edge.

$\mathrm { F S I M ^ { 1 8 } }$ is defined as:

$$
\mathrm {F S I M} = \frac {\sum_ {x \in \Omega} S _ {L} (x) \cdot \mathrm {P C} _ {\mathrm {m}} (x)}{\sum_ {x \in \Omega} \mathrm {P C} _ {\mathrm {m}} (x)}, \tag {4}
$$

where $S _ { L } ( x )$ is the similarity of location x. $\mathrm { P C } _ { \mathrm { m } }$ represents the importance of $S _ { L } ( x )$ in the overall similarity between the compared two images. Ω means the whole image spatial domain.

![](images/353ffb2a8442a71fb9ceb3879b2c85c73cd886fc860b4abbb707c7d4e34d3db2.jpg)  
Fig. S2 The schemes of the classical and the proposed MUSAN edge detection methods.

![](images/21f9662e3469844a4cfe19b2c2c8685be9bf49ec84a94f5f4f2a2812b6ca5d59.jpg)

![](images/3a7e5130fb9de73653a262d70653d16b36dcd90db1558b67b0bbc983f318ce30.jpg)  
Fig. S3 The simulated results comparison of classical edge detection methods with the proposed MUSAN. a. The input image (481×321) is from BSDS500 dataset. b. The comparison of the simulated results for these edge detection methods.

Table S1 The average quality assessment of different edge detection methods for 200 images (BSDS500 dataset).   

<table><tr><td>Edge detector</td><td>Precision</td><td>Recall</td><td>FSIM</td><td>FOM</td></tr><tr><td>Laplacian of Gaussian</td><td>0.32</td><td>0.59</td><td>0.71</td><td>0.31</td></tr><tr><td>Sobel</td><td>0.44</td><td>0.36</td><td>0.82</td><td>0.29</td></tr><tr><td>Prewitt</td><td>0.45</td><td>0.36</td><td>0.82</td><td>0.29</td></tr><tr><td>Roberts</td><td>0.47</td><td>0.29</td><td>0.84</td><td>0.27</td></tr><tr><td>SUSAN</td><td>0.37</td><td>0.87</td><td>0.43</td><td>0.19</td></tr><tr><td>MUSAN (This work)</td><td>0.38</td><td>0.84</td><td>0.66</td><td>0.21</td></tr></table>

![](images/5fba4ad4840159553ea1a84cafa4e04cf41ebeae9dce449f490ae14d12bc8026.jpg)  
Fig. S4 Comparison of the simulated results for classical edge detection and the proposed MUSAN methods. The input image is with higher pixels (1924×1284).

# 3. Fundamentals of the proposed MUSAN detector based on the FeFETs

The measured read drain current (Id)- gate voltage $( V _ { \mathrm { g } } )$ after different write pulse and the corresponding write pulse schemes are shown in Fig. S5. MLC operations are confirmed by the well separated 4 $V _ { \mathrm { T H } }$ states of a transistor.

Note that, two main characteristics of FeFETs affect the performance of MCAM cells and the proposed MUSAN hardware system. The first one is the memory window (MW) of FeFETs. As shown in Fig. 3d, the proposed MCAM cell consists of two FeFETs connected in series. The MCAM functions originate from the multiple states of ferroelectric by partial polarization switching, which results in MLC operations of FeFETs (Fig. 3c). In this work, four polarization states $( \mathrm { i . e . , \ ^ { . } S 0 ^ { , } , \ ^ { . } S 1 ^ { , } , \ ^ { . } S 2 } ^ { \mathrm { , } } ,$ , and ‘S3’) are chosen to design 5-state CAM. Fig. S6b shows the measured $I _ { \mathrm { M L } } - V _ { \mathrm { S I } }$ L for the 5 states of a MCAM cell. Therefore, more states of a MCAM cell can be designed if the MW increases. The other one is the subthreshold swing (SS) of FeFETs. In this work, the match $I _ { \mathrm { M L } }$ and the mismatch $I _ { \mathrm { M L } }$ can be considered as effective signal and noise signal, respectively. If the SS of FeFETs decreases, the ratio of match ${ \cal I } _ { \mathrm { M L } }$ and mismatch $I _ { \mathrm { M L } }$ will increase. This results in a higher signal-to-noise ratio, enhancing noise resistant capability of the system.

![](images/5fb905dee4c204162423e662294af74cdd36286d325fe01191a293eb1c0fcd00.jpg)

![](images/44c87a0f5345b7e9c5eaf481cb16b0ab06f5ef4d1c13d522e8e879d0232dcf8c.jpg)

![](images/bd8ec6a450665c898a01ab006161055d6f09c9efef5599cba4f0a5889b0b2c7b.jpg)

![](images/9a902037ee40070dd203e69dbcbaad1dbf268be2fbc367fa36b537b357343bc0.jpg)  
Fig. S5 MLC operations of FeFET cell. a. Write schemes for FeFET cells with 2bits/cell. b. The measured read $I _ { \mathrm { d } } { - } V _ { \mathrm { g } }$ after write for ten different FeFET cells. c. Endurance and d. retention characteristics of a fabricated FeFET cell.

![](images/93051a8632ee57c18057df813a7a8d5f96ceb4879c1edfbf049a86e2007b7a83.jpg)

![](images/5b13c88a3fffa8a9deebe65035493344be376904bc58478225b7cc811d9dbc7d.jpg)

![](images/0066c2ae841880dc49312586bb954c9391e1d9afc932c7b03d9eed3144153af2.jpg)  
Fig. S6 The MCAM cell with 5 states. a. Operation mechanisms of the proposed MCAM cell based on 2 FeFETs connected in series. b. Measured IML-VSL for different states of a MCAM cell. The inset shows the microscopic image of a fabricated MCAM cell. c. Experimental demonstration of search operations by transient measurement on a MCAM cell.

# 4. The comparison of MUSAN detectors based on different devices

In this work, the proposed MUSAN combines USAN operator and feature matching method, as shown in Fig. 1d. The feature matching method is loaded into a multi-bit content addressable memory (MCAM) array based on FeFET array as shown in Fig. 1e. Theoretically, as long as the devices can successfully implement CAM function, MUSAN with 100% accuracy can be achieved. MOSFET20 and $\mathrm { R e R A M } ^ { 2 1 }$ can also be used to design CAM in previous literatures. Note that the traditional MOSFET-based CAM is usually based on static random-access memory (SRAM). Therefore, 100% accuracy of MUSAN can be achieved by MOSFET and ReRAM.

However, it is quite difficult to estimate the energy consumption for the proposed MUSAN detectors based on different kinds of devices. Because the implement methods and operation methods of the CAM for different kinds of devices will have great impacts on energy consumption. Here, we ignore the differences in implement and operation methods and only compare the power consumption of the CAM that have been reported, as shown in Table S2.

Table S2 The comparison of CAM systems based on different devices.   

<table><tr><td>Devices</td><td>Search energy (fJ/bit/search)</td><td>Cell structure</td><td>TCAM/MCAM</td></tr><tr><td>MOSFET [20]</td><td>1.98</td><td>16T</td><td>TCAM</td></tr><tr><td>ReRAM [21]</td><td>3.0</td><td>5T-2ReRAM</td><td>TCAM</td></tr><tr><td>FeFET(This work)</td><td>2.5</td><td>2FeFET</td><td>MCAM</td></tr></table>

In addition, several challenges persist with CAM based on MOSFET. (1) High standby power because of the high transistor leakage in advanced CMOS technology node. (2) Low integration density. One binary CAM (BCAM) cell need ten transistors (10T), and one ternary CAM (TCAM) need sixteen transistors (16T). (3) Low design flexibility and thus limited functionality. Compared to SRAM-based CAM, ReRAM-based CAM has solved the above challenges to a certain extent. However, the proposed FeFET-based CAM still performs better than ReRAM-based CAM in several aspects. For example, ReRAM-based CAM is usually designed as digital ternary CAM (TCAM), i.e. 3 states/cell3,4, while the FeFET-based MCAM proposed in this work exhibit more states, i.e. 5 states/cell. The structure of ReRAM-based digital TCAM cell (such as 2.5T-1ReRAM, 2T-2ReRAM) is more complex, compared to the one of FeFET-based MCAM cell (2FeFET) in this work. Although ReRAMbased analog CAM can achieve higher CAM density, it also introduces higher overhead and design complexity 6,7. For example, the design in [8] employs six transistors and two ReRAMs (6T-2ReRAM) for just one analog CAM cell, consuming a significant area overhead.

Note that the proposed MCAM cell is based on two series connected FeFETs. On the one hand, compared to MCAM cell with two parallel FeFETs9, it can achieve lower power consuming. On the other hand, the proposed MCAM cell can be integrated in a form of 3D vertical FeFET NAND10. This will enable high density and energy efficiency at low area overhead. Moreover, the proposed FeFET-based MCAM cell with higher bits/cell can be realized by the proposed method, if FeFETs with quad-level cell (QLC) can be achieved. And recent researches demonstrated the QLC characteristics of FeFETs through gate stack engineering and optimized operation methods11.

# 5. Performance evaluation of MUSAN edge detection hardware system

![](images/ecdc0ed85e56f8573e97d952b3ffe6825edd33cfaa7c9eaee6ab45f7d6d19386.jpg)  
Fig. S7 Current responses under different search voltage pulse width (1-100 μs) with stored EF:00XX and search UF:0011.

![](images/bda33e94cec2742fde1b8fc919bcbd4ca183f0f5f6d4249dd18a73b47f726f2b.jpg)  
Fig. S8 The 2D mapping of measured $\mathrm { I _ { M L } }$ with all 16 kinds of search UF corresponding to 4 kinds of stored EF.

![](images/2899a917e3d2315687fb0a5bd17aa59da0996b12762ab295712355f1811f23c1.jpg)  
Fig. S9 The designed sense amplifier adopts a current-type readout structure.

As shown in the Fig. S9, the sense amplifier we designed adopts a current-type readout structure. First, the voltage regulator is used to clamp the ML voltage, and then the current of the selected unit is read, amplified N times by the current mirror, and the sampling voltage is obtained by the sampling resistor. It is compared with a reference voltage $V _ { \mathrm { r e f } }$ through a comparison amplifier to obtain the final output. By setting $V _ { \mathrm { r e f } }$ and the amplification factor N, the high- and low-level threshold voltages

can be accurately controlled to about 90% of the required minimum trigger current value, so that the noise current with an amplitude of only 15% of the trigger current cannot trigger a high-level signal.

![](images/e2329af7c8212f0b155bebd5bcf5ca11ac155253249dea04206ed300ac684d07.jpg)

![](images/92bcdec14711e60b6ae62023ca539ded4634b5114ef2d5256a8b0bd9f1e40d7b.jpg)

![](images/e2d259bc620d6431ef946164e50aaca7f64880f14aa971ed6fe2ee9645c41066.jpg)

![](images/af4f3cc471db2adb70a2989d17abbabc961dd1381ce5bb97d74855027c56925b.jpg)  
Fig. S10 Current responses under search pulse width of 10 μs with 4 kinds of stored EF and all the matched search UF

![](images/d9e02cdaf44ee7f0ad1ee1487bdec75464c4545bc810bb37bdc0425f6c0e2881.jpg)  
Fig. S11 The endurance of search-matching operation with stored EF:00XX and search UF:0011.

![](images/8e8877c4b67342609ff9e142f9f772bc22cbb738c0e41b4208d9d372d7f2bb50.jpg)

![](images/c7524417df771ba0a6d85ecc15b7ad8c7a0693546253f90f0b98b55d8716fc72.jpg)

![](images/4d29b55ff0af31dab6fc0bbe7991d6fb8903fea6759d05dc8c94f91ef394b621.jpg)

![](images/44f34f76a0a9f5132521cbe5c712ca0731725de9e265c1c0cdc2ff0d1460c65f.jpg)

![](images/a38a11ee730533a72b62221f6ed096ff30165857513dd47560d1ca93ee57fffb.jpg)  
For NVM-based convolution, $\mathsf { n } _ { \mathsf { N V M } }$ depends on the strategies for the weight of the kernels   
Fig. S12 The methods of power estimation per operation for this work and previous works with eNVMs-based edge detection.

# 6. The impact of variation in device and circuit behavior

The proposed 5-state MCAM cell is based on two MLC FeFETs with 4 different states (S0, S1, S2, S3), as shown in Figs.

3c and d. Even though certain device-to-device variation exists for FeFETs in an array, the system performs without any loss in accuracy as long as MCAM functions can be successfully implemented. In this work, MLC operations with 4 different states can be confirmed by applying the different write pulse schemes (Fig. S4a). And Fig. S4b plots read drain current versus gate voltage $\mathrm { ( I _ { d } \mathrm { - V _ { g } ) } }$ of 4 states (S0, S1, S2, S3) for 10 FeFETs. The well separated 4 $\mathrm { V } _ { \mathrm { T H } }$ states for these 10 FeFETs guarantee MCAM functions can be successfully implemented. In this way, device-to-device variation demonstrated in this wrok will not affect the accuracy of detection.

In our peripheral circuits, operational amplifiers and bipolar junction transistors in the readout circuits are prone to introduce the noise, which would incur variation in circuit behavior. The noise of the operational amplifiers in this work is within 1nV, which is much lower than the voltage amplitude of the effective signal (0.5V-1V) and will not cause significant impact. The bipolar junction transistors in this work are low noise with NF (Noise Figure) <5dB. Note that, the noise caused by the FeFET array is up to 15% (<-16dB), which has been discussed in detail in the above. For the input noise of -16dB, the output noise of bipolar junction transistors is <-11dB, which will not cause significant impacts. In summary, the circuit behavior noise involved will not cause significant interference to the implementation of the proposed edge detection.