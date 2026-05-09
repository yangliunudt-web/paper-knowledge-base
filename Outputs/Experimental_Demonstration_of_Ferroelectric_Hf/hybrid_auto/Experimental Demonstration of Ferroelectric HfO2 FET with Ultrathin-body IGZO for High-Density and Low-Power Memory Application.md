---
title: "Experimental Demonstration of Ferroelectric HfO2 FET with Ultrathin-body IGZO for\\"
authors:
  - "Fei Mo"
  - "Yusaku Tagawa"
  - "Chengji Jin"
  - "MinJu Ahn"
  - "Takuya Saraya"
  - "Toshiro Hiramoto"
  - "Masaharu Kobayashi"
date: "2023-01-01"
year: "2023"
journal: "IEEE Electron Device Letters"
abstract: "We have experimentally demonstrated a ferroelectric HfO2 FET with memory operation by introducing ultrathin IGZO as a channel material. Ultrathin-body IGZO ferroelectric FET (FeFET) shows high mobility with deposited channel material, nearly ideal subthreshold slope, and controllable memory characteristics with the use of back-end compatible process. These results are attributed to the properties of IGZO channel: junctionless FET operation, nearly-zero low-k interfacial layer on metal-oxide channel and good capping effect for realizing ferroelectric phase formation with $\\mathrm { H f Z r O } _ { 2 } .$ . IGZO FeFET will open a new path for high-density memory application. Keywords: ferroelectric FET, HfO2, IGZO, memory."
abstract_cn: "我们通过引入超薄IGZO作为沟道材料，实验演示了具有存储操作的铁电HfO2 FET。超薄体IGZO铁电FET表现出沉积沟道材料的高迁移率、近乎理想的亚阈值斜率以及使用后端兼容工艺的可控存储特性。这些结果归因于IGZO沟道的特性：无结FET操作、金属氧化物沟道上近乎零的低k界面层以及实现HfZrO2铁电相形成的良好覆盖效应。IGZO\\"
keywords:
  - "[[FeFET]]"
  - "[[IGZO]]"
  - "[[HfO2]]"
  - "[[Memory application]]"
cite: "[1] Mo F, Tagawa Y, Jin C, et al. Experimental demonstration of ferroelectric HfO2\\"
aiSum: "超薄体IGZO FeFET实验演示：采用HfO2铁电层，实现高迁移率、理想亚阈值斜率、可控存储窗口，为高密度低功耗存储应用提供新方案。"
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
  - "[[HfO2]]"
  - "[[IGZO]]"
---

Fei Mo, Yusaku Tagawa, Chengji Jin, MinJu Ahn, Takuya Saraya, Toshiro Hiramoto and Masaharu Kobayashi Institute of Industrial Science, The University of Tokyo, Tokyo, Japan, email address: mofei@nano.iis.u-tokyo.ac.jp

# Abstract

We have experimentally demonstrated a ferroelectric HfO2 FET with memory operation by introducing ultrathin IGZO as a channel material. Ultrathin-body IGZO ferroelectric FET (FeFET) shows high mobility with deposited channel material, nearly ideal subthreshold slope, and controllable memory characteristics with the use of back-end compatible process. These results are attributed to the properties of IGZO channel: junctionless FET operation, nearly-zero low-k interfacial layer on metal-oxide channel and good capping effect for realizing ferroelectric phase formation with $\mathrm { H f Z r O } _ { 2 } .$ . IGZO FeFET will open a new path for high-density memory application.

Keywords: ferroelectric FET, HfO2, IGZO, memory.

# Introduction

In today’s highly information-oriented society, AI and IoT are driving new innovations, which are enabled by advanced semiconductor systems. To load and store more data, and implement sophisticated algorithms like machine learning under the constraint of energy consumption, higher density memories will be required with lower power consumption.

Ferroelectric HfO2 FET memories [1-3] have attracted much attention because of its CMOS compatibility and potential lowpower consumption by field-drive operation. A high-density ferroelectric FET (FeFET) architecture inspired by 3D vertical NAND structure has been recently proposed and successfully demonstrated [4]. The challenges for vertical FeFET from device perspectives are low mobility of very thin poly-Si channel, $V _ { \mathrm { t h } }$ compensation and degraded subthreshold slope (SS) by charge trapping, voltage loss by low-k interfacial layer on Si channel, and high thermal budget. IGZO is a promising channel material because of its high mobility as a deposited amorphous material [5-8], junctionless FET operation [9] without much surface conduction to avoid charge trapping, nearly zero low-k interfacial layer, and low thermal budget. Therefore, IGZO channel FeFET [10-12] (Fig. 1) can provide new opportunities for high density memory application by tackling the challenges described above (Fig. 2)

In this work, we propose and design a ferroelectric HfO2 FET with ultrathin-body IGZO channel for high density memory application. We develop device integration process and demonstrate its potential as a lower power memory device.

# Device operation and design

Since IGZO is an N-type material, IGZO FeFET operates as a junctionless FET (Fig. 3). In erase mode, negative $V _ { \mathrm { g } }$ induces high density of depletion charge. In program mode, positive $V _ { \mathrm { g } }$ induces accumulation charge. Spontaneous polarization can be flipped by electric field sustained by these charges. For high density memory application, channel thickness should be as thin as possible but without performance degradation. In our preliminary experiment of IGZO FET with $\mathrm { S i O } _ { 2 }$ gate insulator (Fig. 4), 5~10nm show high $V _ { \mathrm { t h } }$ and small SS (Fig. 5). 8nm is chosen for device design. Fig. 6 shows simulated $I _ { \mathrm { d } } { - } V _ { \mathrm { g } }$ and $I _ { \mathrm { g } ^ { - } }$ $V _ { \mathrm { g } }$ curves. Unlike floating body, IGZO FeFET shows memory window with substrate potential fixed by back gate because larger electric field can be effectively applied to FE-HfO layer especially in erase mode (seen as larger switching current in $I _ { \mathrm { g } } )$ .

# Device fabrication

We use a bottom-gate device structure for the proof-ofconcept in Fig. 7. $V _ { \mathrm { g } }$ is applied from the bottom gate. Fabrication process flow conducted in our university lab is shown in Fig. 8. First, 20nm-thick TiN is deposited as a bottom gate on cleaned $\mathrm { S i O } _ { 2 } / \mathrm { S i }$ substrate by RF sputtering. 15nm-thick Zr-doped HfO2 (HZO) is deposited as a gate insulator by ALD system at 250℃. 8nm-thick IGZO is deposited as a channel by RF sputtering and patterned by diluted HCl. 12nm-thick $\mathrm { S i O } _ { 2 }$ is deposited as a passivation by RF sputtering. RTA is done in $\Nu _ { 2 } / \Nu _ { 2 }$ ambient at 500℃ for 10sec. Al/Ti is deposited as an optional top gate to fix substrate potential by EB evaporation.

# Results and discussions

Fig.9 show the cross sectional TEM images. Each layer is uniformly formed. HZO is fully crystallized and IGZO layer remains amorphous. HZO and IGZO channel are free of low-k interfacial layer. Fig. 10 shows the XRD spectra of with and without IGZO cap on HZO layer. IGZO cap effectively helps to form ferroelectric phase of HZO layer. Fig. 11 shows P-V and I-V curves of Al/Ti/IGZO/HZO/TiN capacitor and clear ferroelectric property is confirmed.

By applying $V _ { \mathrm { g } }$ less than switching voltage, $I _ { \mathrm { d } } { - } V _ { \mathrm { g } }$ curve is measured and field effect mobility is extracted in Fig. 12 and Fig. 13, respectively. $I _ { \mathrm { d } } { - } V _ { \mathrm { g } }$ curve shows nearly ideal junctionless FET characteristics. The field effect mobility is consistent with Hall mobility ~10cm2 /V∙s and not significantly degraded by HZO gate insulator thanks to the bulk conduction in junctionless FET operation.

Fig.14 shows the measured $I _ { \mathrm { d } } { - } V _ { \mathrm { g } }$ after applying erase and program voltage from bottom-gate while top-gate potential is fixed. Erase and program occur, and memory window ~0.5V appears as expected from the simulation results. The extracted SS is shown in the inset. Nearly ideal SS is obtained for both erase and program state. Polarization switching can be observed in quasi-static $I _ { \mathrm { { g } } }$ measurement for large $V _ { \mathrm { g } }$ swing as shown in Fig. 15. Particularly, in positive $V _ { \mathrm { g } }$ sweep after erase, two $I _ { \mathrm { { g } } }$ peaks are observed. The first peak in lower $V _ { \mathrm { g } }$ corresponds to the current between bottom-gate and S/D pads, while the second peak in higher $V _ { \mathrm { g } }$ corresponds to the current between bottom-gate and the channel. Note that both peaks are overlapped in negative $V _ { \mathrm { g } }$ sweep after program. Write voltage dependence is examined in Fig. 16. IGZO FeFET shows controllable erase and program operation at less than 5V.

# Summary

We designed and fabricated ultrathin-body IGZO FeFET. The device shows high mobility as a deposited channel. In junctionless FET operation with nearly-zero interfacial layer, ideal subthreshold slope was obtained. IGZO works as a good capping layer for ferroelectric phase formation of HZO, which results in controllable memory operation. Ultrathin IGZO FeFET is a promising candidate for high-density memory application. Fast/reliable memory operation are to be done with device integration of top-gate structure in future work.

# Acknowledgement

This work was supported by JST PRESTO Grant Number JPMJPR1525, JSPS KAKENHI Grant Number JP18H01489 and Tokyo Electron Ltd.

![](images/5097492b3c663a325ae09a6717ccc7743c7b85b40dcd4463f0f50a47a567970d.jpg)  
Fig. 1 Schematic illustration of 3D vertical FeFETs of one pillar with FE-HfO gate insulator and ultrathin IGZO channel.

![](images/d497923be152b5f40c7a6661ec7656d443052ef1dcddfb1025e4d6758dda5216.jpg)  
Fig. 2 Schematic illustration of the difference between (upper) poly-Si channel and (lower) IGZO channel FeFET.

![](images/3cb19f44dc9cb04c794bd774d7c7f849ca34fdae272a13e7c2b0d8c5647b6d92.jpg)  
Fig. 3 Schematic illustration of an ultrathin-body IGZO channel FeFET in (upper) erase mode and (lower) program mode.

![](images/d8a8e943f5a71af97be30a4d0bec05033c413116368fc277a1c8424f412ab2c7.jpg)  
Fig. 4 Measured $I _ { \mathrm { d } } – V _ { \mathrm { g } } ^ { \overline { { \mathrm { g } } } }$ curves of IGZO FETs with normal SiO2 gate insulator for different thickness of IGZO channel. >5nm can be used.

![](images/34190562a81c0d1c2969b8bb0cde3d4fd64d952d4918549cb08f1bc3a5680903.jpg)

![](images/7e456f4fb2c637071f4195a4559772401a75b85b656e151b947d21dcbd51ccea.jpg)  
Fig. 5 Extracted Vth and SS from the measured $I _ { \mathrm { d } } { - } V _ { \mathrm { g } }$ curves in Fig. 4. 8nm is chosen for device design in terms of SS and $V _ { \mathrm { t h } } .$ .   
Fig. 6 Simulated $I _ { \mathrm { d } } { - } V _ { \mathrm { g } }$ and $I _ { \mathrm { g } ^ { - } } V _ { \mathrm { g } }$ curves of IGZO FeFET for (upper) floating body and (lower) fixed substrate potential by back-gate.

![](images/862c5b605588f41ecd1de71425c84e8a8b36c86eec8034744f3df7e88431f72c.jpg)  
Fig. 7 Schematic illustration of the device structure of ultrathinbody IGZO FeFET for proof-ofconcept. Bottom-gate structure is used with optional top gate.

![](images/a708c3df481e8a5c20d39ef047cd5355fd7c9744e782b8a37b74cc20dd584d17.jpg)  
${ \dot { \mathrm { F i g . } } }$ 8 Fabrication process flow of bottom-gate ultrathin-body IGZO FeFET. Max. process temperature is $5 0 0 \mathrm { { } ^ { \circ } C }$ in this work, but RTA condition can be tuned to ~400℃.

![](images/9e828d10c14cc76c1dc66daf036e40fed3c3c66ad7579ea1064ea0b2c2a2f5d4.jpg)  
Fig. 9 Cross sectional low-mag and high-mag TEM images of a fabricated SiO2/IGZO/HZO/TiN structure in the channel region. Each layer is formed uniformly.

![](images/039c05ce40892ac4188e0b09389be11b881c00f183edc9c345b0b6820fce8711.jpg)  
Fig. 10 Measured GIXRD spectra of HZO film (upper) with and (lower) without IGZO capping after crystallization anneal.

![](images/fc25a5e837412f817166af5c73722ae20f2f313767cab572c0a347890e7a4b4c.jpg)  
Fig. 11 Measured $\bar { P } { - } \bar { V }$ and transient $I { - } \bar { V }$ curve of a fabricated Al/Ti/ IGZO/HZO/TiN capacitor at 1kHz showing clean ferroelectric property.

![](images/82d9a78160500c3b5dcfc9d2f9230d21883d23c4dd99d8799226b404c076bfed.jpg)  
Fig. 12 Measured $I _ { \mathrm { d } } – V _ { \mathrm { g } } ^ { - }$ curves of 8nm-thick IGZO FET with 15nm HZO in a narrow $V _ { \mathrm { g } }$ sweep range where no erase/program occurs.

![](images/f7080e46dce316e9493248f135b742c5825ffbb9f427335b049540d2bb3f0ffa.jpg)  
Fig. 13 Measured field-effect mobility of 8nm-thick IGZO FET with $\mathrm { S i O } _ { 2 }$ and HZO gate insulator. Hall mobility is 10cm2/V∙s.

![](images/e4b8fd90d5e7b7853cecccf4e1c74a83f749fa03af4c3c7b1b53dbe17daf32cf.jpg)  
Fig. 14 Measured $I _ { \mathrm { d } } { - } V _ { \mathrm { g } }$ of IGZO FeFET after applying erase (-3V) / program (+2.5V) voltage. MW ~0.5V appears. The inset is SS.

![](images/11d9f2e55d9972eb42ae1469b7f56497595c9a1faf145f99a72bd9b1d3977d8a.jpg)  
Fig. 15 Measured $I _ { \mathrm { d } } { - } V _ { \mathrm { g } }$ and $I _ { \mathrm { g } ^ { - } } V _ { \mathrm { g } }$ of IGZO FeFET in a wide $V _ { \mathrm { g } }$ sweep range. Polarization switching on IGZO channel is observed in $I _ { \mathrm { g } } .$

Fig. 16 Measured write voltage dependence of IGZO FeFET for erase/program operation. Write operation is controllable at <5V.   
![](images/b42281a22c30fcfa9fb6e409097975881dccfe3c311e46dca4ae5b26f17fb78b.jpg)  
References [1] J. Muller et al., VLSI Symp. 2012, pp. 25-26, [2] S. Dunkel et al., IEDM 2017, p. 485-488, [3] K. Ni, VLSI Symp. 2018, pp. 131-132, [4] K. Florent, IEDM 2018, pp. 43-46, [5] K. Nomura et al., Nature, 432, 25, 488 (2004), [6] T. Kawamura et al., IEDM 2008, pp. 77-80, [7] S. Matsuda et al., VLSI Symp. 2015, pp. 216-217, [8] H. Sunamura et al., VLSI Symp. 2013, pp. 250-251, [9] H. –T. Lue et al., VLSI Symp 2010, pp.131-132. [10] G. –G. Lee, APL, 99, 012901 (2011), [11] B. –H. Kim, EDL 2011, [12] Y. Li, J. EDS, 5, 5, 378 (2017), [13] A. T. Voutsas, TED, 50, 6, 1494 (2003).