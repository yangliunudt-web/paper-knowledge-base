---

title: "28nm HKMG 1F-1R² Multilevel Memory for Inference Engine Application"
authors:
  - "Sourav De"
  - "Franz Müller"
  - "Maximilian Lederer"
  - "Yannick Raffel"
  - "Tarek Ali"
  - "Luca Pirro"
  - "Stefan Dünkel"
  - "Sven Beyer"
  - "Konrad Seidel"
  - "Thomas Kämpfe"
date: "2022-07-01"
year: 2022
journal: "IEEE Journal of Electron Devices Society"
doi: "10.1109/JEDS.2022.3195119"
abstract: "This article reports 28 nm high-k-metal-gate (HKMG) based 3bits/cell memory with one ferroelectric (Fe) field effect transistor (FeFET) and one reconfigurable resistor (R^2). R^2, connected with the select line (SL) and the drain terminal of the FeFET, can be reconfigured via the SL terminal. R^2 can be implemented by using a standard metal-oxide-semiconductor field effect transistor (MOSFET) as voltage controlled resistor or any two terminal programmable resistors. The 1F-1R^2 cells demonstrate current-based 3bits/cell operation over a 300mm wafer and stable retention characteristics at 85°C for all eight current levels."
abstract_cn: "本文报道了基于28 nm高K金属栅的3比特/单元存储器，采用一个铁电场效应晶体管和一个可重构电阻器。可重构电阻器连接选择线和FeFET的漏极，可通过选择线终端重新配置。该电阻器可使用标准金属氧化物半导体场效应晶体管作为压控电阻或任何两端可编程电阻器实现。1F-1R²单元在300mm晶圆上展示了基于电流的3比特/单元操作，并在85°C下对所有八个电流水平表现出稳定的保持特性。"
cite: "[1] De S, Müller F, Lederer M, et al. 28nm HKMG 1F-1R² multilevel memory for"
aiSum: "28 nm HKMG 1F-1R²存储器：3比特/单元操作，300mm晶圆，85°C稳定保持，适用于推理引擎应用。"
confidence: medium
wiki_concepts:
  - "[[FeFET]]"
keywords:
  - "[[FeFET]]"
---

# 28nm HKMG 1F-1R² Multilevel Memory for Inference Engine Application

Sourav De $^{1}$ , Franz Müller $^{1}$ , Maximilian Lederer $^{1}$ , Yannick Raffel $^{1}$ , Tarek Ali $^{2}$ , Luca Pirro $^{2}$ , Stefan Dülkel $^{2}$ , Sven Beyer $^{2}$ , Konrad Seidel $^{1}$ and Thomas Kämpfe $^{1}$

<sup>1</sup> Fraunhofer-Institut für Photonische Mikrosysteme IPMS - Center Nanoelectronic Technologies, Dresden, Germany

2GlobalFoundries', Dresden, Germany

E-mail: sourav.de@ipms.fraunhofer.de, yannick.raffel@ipms.fraunhofer.de

Abstract—This article reports 28 nm high-k-metal-gate (HKMG) based 3bits/cell memory with one [[ferroelectric]] (Fe) field effect transistor ([[FeFET]]) and one reconfigurable resistor $(\mathbb{R}^2)$ . $\mathbb{R}^2$ , connected with the select line (SL) and the drain terminal of the FeFET, can be reconfigured via the SL terminal. $\mathbb{R}^2$ can be implemented by using a standard metal-oxide-semiconductor field effect transistor (MOSFET) as voltage controlled resistor or any two terminal programmable resistors. The detailed discussion about $\mathbb{R}^2$ is beyond the scope of this paper. The 1F-1R $^2$ cells demonstrate current-based 3bits/cell operation over a 300mm wafer and stable retention characteristics at $85^{\circ}\mathrm{C}$ for all eight current levels.

# I. INTRODUCTION

The scientific community is very interested in $\mathrm{HfO_2}$ -based Fe memories, among many other possible possibilities, such as resistive random access memory ([[RRAM]]), magnetic random access memory (MRAM), and phase change memories (PCMs) [1-3]. This characteristic can be linked to $\mathrm{HfO_2}$ 's CMOS compatibility and scalability, which enable Fe memories to be integrated on a very large scale (VLSI) with the sophisticated CMOS technology. The system-level integration of ferroelectric memories has been hastened by their compatibility with 28-nm HKMG, FinFET, and thin-film technologies [2,3].

The scaling up of variability, however, is the main problem with ferroelectric memory system integration. In extensively scaled ferroelectric field-effect transistors, a serious problem is caused by the poly-crystalline structure of $\mathrm{HfO_2}$ and inherent defect sites that serve as charge-trapping sites (FeFETs) [4,5,6]. In our earlier work, we showed how a 1F-1R structure might be used to efficiently perform the one-bit-precision multiply and accumulation operation while reducing device variance [2]. However, the 1F-1R architecture only allows for one bit per cell because of a lower saturation current. As a result, we tried shunting a reconfigurable resistor to the FeFET's drain terminal. Word lines (WL) were used to program the FeFET devices, while select lines were used to vary the resistance of the reconfigurable resistor (SL). The 1F-1R² structure achieves 3bits/cell operation over all process corners in 300mm wafers.

# II. EXPERIMENTS

The tested devices were fabricated at GlobalFoundries' using $28\mathrm{nm}$ HKMG technology on $300\mathrm{mm}$ wafers. The FeFETs were created by combining an interfacial layer of silicon dioxide $(\mathrm{SiO}_2)$ and an $8\mathrm{nm}$ silicon doped [[hafnium oxide]] $(\mathrm{HfO}_2)$ ferroelectric layer in the gate stack of a typical metal oxide semiconductor field-effect transistor (MOSFET). The reconfigurable resistors were externally embedded to the FeFET devices. However, it is

completely possible to integrate them on same wafer. Fig.1 shows the schematic representation of possible $1\mathrm{F - 1R}^2$ memory cells and the transmission electron microscopic (TEM) image. Using 500-ns pulses at the gate terminal, the 1F of $1\mathrm{F - 1R}^2$ devices was programmed (WRITE) and reconfiguration of resistance was conducted via SL. 50 consecutive wake-up pulses were cycled through the FeFETs before performing READ-WRITE operations. A 4.5-V pulse is followed by a 500-ns, 5-V pulse to create a wake-up pulse. During the WRITE operation, the source, drain, and bulk terminals were biased at $0\mathrm{V}$ . The READ operation is performed via reading the current $(I_{BL})$ through the bit line (BL) of the device.

In order to evaluate the effectiveness of the 1F-1R $^2$ devices in multi-layer perceptron (MLP) based NNs as synaptic cores, we performed a system-level simulation of hand-written digit recognition using the data set of "Modified National Institute of Standards and Technology (MNIST)". Models have been developed for NN simulation to account for $I_{BL}$ retention deterioration and device-to-device variance gained from experimental testing. The neural network architecture is shown in Fig. 3(a).

# III. RESULTS AND DISCUSSION

Fig. 2(a) shows the transfer characteristics of $1\mathrm{F - 1R}^2$ with 8-different current levels. Fig. 2(b) displays the cumulative distribution of the sixty numbers of $1\mathrm{F - 1R}^2$ cells distributed across all process corners of $300\mathrm{mm}$ wafers. The data retention characteristics, shown in Fig. 2(c), measured at $85^{\circ}\mathrm{C}$ shows stable retention characteristics over $10^{4}$ seconds for all current levels.

The NN received offline training to fulfill the 1F-1R $^2$ devices' endurance requirements. Following the offline training of the NN, the inference operation was carried out. In essence, online training or retraining of the NN places an unreasonable energy demand on the hardware. As a result, the capacity to retain data is crucial for performing inference operations without often retraining. The accuracy of the inference for MNIST datasets using MLP NN was evaluated using the data retention measured up to $10^{4}$ s at $85^{\circ}\mathrm{C}$ . The MLP-based NN initially achieves inference accuracy of over $97\%$ and keeps it over $95\%$ for $10^{4}$ s without having to be retrained Fig. 3(b). Finally, the device was benchmarked with other state-of-art ferroelectric devices.

# IV. CONCLUSION

This article reports 3bits/cell 1F-1R2 memory. The FeFET devices were fabricated at GlobalFoundries on $300\mathrm{mm}$ wafers using $28\mathrm{nm}$ HKMG process. The retention characteristics measured at $85^{\circ}\mathrm{C}$ shows stable retention characteristics for $10^{4}\mathrm{s}$ . Finally, the [[neuromorphic]] simulations corroborates the feasibility of this devices in system-level applications.

![](images/237ccebc86f8c2e18e08504601804f24c43027f36c16c0ca5b9d312b347728de.jpg)

![](images/dc76cfa03f06a2fb4304373eca32f8d6c0666cc08a9c4db36dbe517240fb6a81.jpg)

![](images/30b8496573c81eee074c05021aeda51d88366dc40d9b55cd67b6c9a29591a668.jpg)

![](images/aba7b6fb8d7ba057ab0d6c0addf4c2e57b111a180ea5089523199c9b940e1848.jpg)  
Figure.1. Schematic representation of $1\mathrm{F - 1R}^2$ memory array with (a) MOSFET as voltage controlled resistor, (b) and two terminal reconfigurable resistive element attached to the drain terminal of the FeFET. (c) TEM image of $28\mathrm{nm}$ FeFET [2].

![](images/b2a61698c774ce79a5021ff173466bafc9814fd80bf80cac989ccdecff9b3aa9.jpg)

![](images/9511403f9e6e379f51dd16a41446586228a30afbffc07784de849a7419d32db5.jpg)

![](images/82f60d50d265ac986bcab156940b630acbdd2b26ee315564552da2a70965d67c.jpg)  
Figure.2. (a) Transfer characteristics demonstrates 8-levels of current from the bit line of the memory cell. (b) The cumulative distribution shows 3bits/cell operation among sixty devices in $300\mathrm{mm}$ wafers. (c) Data retention characteristics demonstrate stable data retention up to $10^{4}$ seconds at elevated temperature. The excellent retention makes $1\mathrm{F - 1R}^2$ devices suitable for inference applications.   
Figure.3. (a) Schematic representation of the memory array with $1\mathrm{F - 1R}^2$ synaptic devices. (b) Inference accuracy demonstrate minimal accuracy degradation due to retention loss.

Table I: Benchmarking [3]   
References   

<table><tr><td>Attributes</td><td>This Work</td><td>IEDM 20</td><td>IEDM 19</td><td>IEDM 20</td><td>IEDM 20</td></tr><tr><td>Material</td><td>Si:[[HfO2]]</td><td>Si:HfO2</td><td>Si:HfO2</td><td>HfO2</td><td>Si:HfO2</td></tr><tr><td>MLC Level</td><td>3 bits/cell</td><td>3 bits/cell</td><td>3 bits/cell</td><td>1 bits/cell</td><td>2 bits/cell</td></tr><tr><td>Max Voltage</td><td>±5V</td><td>±16V</td><td>±10V</td><td>±1.8 V</td><td>±4 V</td></tr><tr><td>TFE (nm)</td><td>8</td><td>20</td><td>20</td><td>6.5</td><td>9</td></tr><tr><td>Technology</td><td>28nm</td><td>~180nm</td><td>~180nm</td><td>NA</td><td>~28 nm</td></tr><tr><td>Retention</td><td>104s, 85C</td><td>104s, 85C</td><td>104s, 85C</td><td>NA</td><td>104s, 85C</td></tr><tr><td>Endurance</td><td>~105</td><td>~105</td><td>~104</td><td>~1012</td><td>~104</td></tr></table>

[1] S. De et al., in IEEE JEDS, vol. 10, pp. 637-641, 2022, DOI: 10.1109/JEDS.2022.3195119   
[2] S. De et al., in IEEE Trans. Electron Devices, pp. 1-5, 2022, DOI: 10.1109/TED.2022.3216973   
[3] S. De et al., in 2021 Symposium on VLSI Technology, 2021, pp. 1-2   
[4] Y. Raffel et al., in ACS Appl. Electron. Mater., vol. 4, no. 11, pp. 5292-5300, 2022, DOI: 10.1021/acsaelm.2c00771   
[5] Y. Raffel et al., in 2022 IEEE International Memory Workshop (IMW), 2022, pp. 1-4, DOI: 10.1109/IMW52921.2022.9779277   
[6] M. Lederer., in 2021 Silicon Nanoelectronics Workshop (SNW), 2021, DOI: 10.1109/SNW51795.2021.00033

Acknowledgement: The research leading to these results has received funding in part from the ECSEL Joint Undertaking under Grant Agreement No. 826655—Project TEMPO and Project ANDANTE under Grant No. 876925.