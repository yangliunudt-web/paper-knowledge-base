---
title: "Monolithic 3D integration of back-end compatible 2D material FET on Si FinFET"
authors:
  - "Shi-Xian Guan"
  - "Tilo H. Yang"
  - "Chih-Hao Yang"
  - "Chuan-Jie Hong"
  - "Bor-Wei Liang"
  - "Kristan Bryan Simbulan"
  - "Jyun-Hong Chen"
  - "Chun-Jung Su"
  - "Kai-Shin Li"
  - "Yuan-Liang Zhong"
  - "Lain-Jong Li"
  - "Yann-Wen Lan"
date: "2025-01-01"
year: 2025
journal: "Nature Electronics"
abstract: "The performance enhancement of integrated circuits relying on dimension scaling (i.e., following Moore’s Law) is more and more challenging owing to the physical limit of Si materials. Monolithic three-dimensional (M3D) integration has been considered as a powerful scheme to further boost up the system performance. Two-dimensional (2D) materials such as MoS2 are potential building blocks for constructing upper-tier transistors owing to their high mobility, atomic thickness, and back-end-of-line (BEOL) compatible processes. The concept to integrate 2D material-based devices with Si field-effect transistor (FET) is technologically important but the compatibility is yet to be experimentally demonstrated. Here, we successfully integrated an n-type monolayer MoS2 FET on a p-type Si fin-shaped FET with 20 nm fin width via an M3D integration technique to form a complementary inverter. The integration was enabled by deliberately adopting industrially matured techniques, such as chemical mechanical planarization and e-beam evaporation, to ensure its compatibility with the existing 3D integrated circuit process and the semiconductor industry in general. The 2D FET is fabricated using low-temperature sequential processes to avoid the degradation of lower-tier Si devices. The MoS2 n-FETs and Si p-FinFETs display symmetrical transfer characteristics and the resulting 3D complementary metal-oxide-semiconductor inverter show a voltage transfer characteristic with a maximum gain of ~38. This work clearly proves the integration compatibility of 2D materials with Si-based devices, encouraging the further development of monolithic 3D integrated circuits."
abstract_cn: "依靠尺寸缩放（即遵循摩尔定律）的集成电路性能提升由于硅材料的物理极限而变得越来越具有挑战性。单片三维集成被认为是进一步提升系统性能的强大方案。二维材料如MoS2由于其高迁移率、原子厚度和与后端工艺兼容的工艺，成为构建上层晶体管的有潜力的构建模块。将基于二维材料的器件与硅场效应晶体管集成的概念在技术上很重要，但兼容性尚未得到实验证明。本文通过M3D集成技术成功将n型单层MoS2 FET集成在p型硅鳍式FET（鳍宽20 nm）上，形成互补反相器。集成通过有意采用工业成熟技术（如化学机械抛光和电子束蒸发）实现，以确保其与现有3D集成电路工艺和整个半导体行业的兼容性。二维FET采用低温顺序工艺制造，以避免下层硅器件的性能退化。MoS2 n-FET和Si p-FinFET显示出对称的转移特性，所得3D互补金属氧化物半导体反相器的电压传输特性显示最大增益约为38。这项工作明确证明了二维材料与硅基器件的集成兼容性，鼓励了单片3D集成电路的进一步发展。"
keywords:
  - "[[Monolithic 3D integration]]"
  - "[[2D materials]]"
  - "[[FinFET]]"
  - "[[Back-end compatibility]]"
cite: "[1] Guan S X, Yang T H, Yang C H, et al. Monolithic 3D integration of back‑end compatible 2D material FET on Si FinFET[J]. Nature Electronics, 2025, 8(4): 312‑325."
aiSum: "单片3D集成：单层MoS2 n‑FET与Si p‑FinFET（鳍宽20 nm）垂直集成形成互补反相器，增益~38，采用CMP/e‑beam蒸发等工业成熟工艺，验证二维材料与硅基器件兼容性。"
confidence: "high"
---

ARTICLE OPEN

? Check for updates

# Monolithic 3D integration of back-end compatible 2D material FET on Si FinFET

Shi-Xian Guan1,8, Tilo H. Yang 2,8, Chih-Hao Yang1 , Chuan-Jie Hong1 , Bor-Wei Liang3 , Kristan Bryan Simbulan2,4, Jyun-Hong Chen5 , Chun-Jung Su5 , Kai-Shin Li5✉, Yuan-Liang Zhong 1✉, Lain-Jong Li6✉ and Yann-Wen Lan 2,7✉

The performance enhancement of integrated circuits relying on dimension scaling (i.e., following Moore’s Law) is more and more challenging owing to the physical limit of Si materials. Monolithic three-dimensional (M3D) integration has been considered as a powerful scheme to further boost up the system performance. Two-dimensional (2D) materials such as MoS2 are potential building blocks for constructing upper-tier transistors owing to their high mobility, atomic thickness, and back-end-of-line (BEOL) compatible processes. The concept to integrate 2D material-based devices with Si field-effect transistor (FET) is technologically important but the compatibility is yet to be experimentally demonstrated. Here, we successfully integrated an n-type monolayer MoS2 FET on a p-type Si fin-shaped FET with 20 nm fin width via an M3D integration technique to form a complementary inverter. The integration was enabled by deliberately adopting industrially matured techniques, such as chemical mechanical planarization and e-beam evaporation, to ensure its compatibility with the existing 3D integrated circuit process and the semiconductor industry in general. The 2D FET is fabricated using low-temperature sequential processes to avoid the degradation of lower-tier Si devices. The MoS2 n-FETs and Si p-FinFETs display symmetrical transfer characteristics and the resulting 3D complementary metal-oxidesemiconductor inverter show a voltage transfer characteristic with a maximum gain of ~38. This work clearly proves the integration compatibility of 2D materials with Si-based devices, encouraging the further development of monolithic 3D integrated circuits.

npj 2D Materials and Applications (2023) 7:9 ; https://doi.org/10.1038/s41699-023-00371-7

# INTRODUCTION

The recent trend in the development of electronic devices is directed toward miniaturization, portability, and high performance, well agreed with the prediction of Moore’s Law. However, the imminent end of Moore’s Law has already been expected over the last few years. To continue to keep up with the miniaturization requirements, shortening the device channel is a traditional solution, although the challenge with this approach is the rise of leakage current due to short-channel effects. For this reason, modified device structures, such as the fin field-effect transistors (FinFETs), were introduced. In FinFET, the transistor channel is constructed into a fin-like shape forming a wrap-around gate structure. This three-dimensional (3D) design enables control over the on/off states of FinFETs from both sides of the circuit, thereby offering better control due to more effective leakage current suppression. Aside from improving the device design, many efforts have also been made to explore new materials that can replace silicon for shorter FET channel implementations. Atomically thin two-dimensional (2D) layered materials like semiconducting transition metal dichalcogenides (TMDs) represent the ultimate limit of miniaturization in the vertical direction, holding great potential for advanced nanoelectronics1,2 . Attention has been paid mainly to molybdenum disulfide (MoS ), owing to its large bandgap (~1.9 eV), high carrier mobility, significant on/off current ratio, and relatively small subthreshold swing3–7 . However, MoS2 exhibits only n-type behavior in most previous studies, hampering its use in complementary metal-oxide-semiconductors

(CMOS). To solve this, one feasible strategy is to integrate MoS2 with other p-type transistors. For instance, a 2D CMOS inverter was constructed by integrating an n-type MoS2 FET and a p-type WSe2 FET into a planar heterostructure8 . A flexible CMOS inverter was designed by fabricating a p-type Si nanomembrane FET and an n-type MoS2 FET on the same organic substrate9 . Recently, we also realized a polarity-controllable MoS transistor in a single device for logic inverter application10.

In addition to the above efforts and achievements, advanced integration techniques, particularly 3D integration schemes, have also been presented to ensure the more rapid growth of transistors per chip. 3D integrated circuits (3D ICs)11,12 consist of vertically stacked and interconnected active chips, carrying components like transistors and sensors. 3D ICs promise a smaller form factor, higher integration density, lower power consumption, better signal integrity, and heterogeneous integration compared to conventional 2D ICs. Utilizing both a 2D TMD channel and the finFET design into 3D ICs can combine their respective advantages11,13,14; however, the intuitive question is whether 2D materials-based devices and their fabrication are compatible with existing Si-based semiconductor technology. This question has yet to be examined, although 2D materials and related devices have been broadly studied in academia. In general, stacking schemes in 3D ICs include wafer-to-wafer, die-to-wafer, and die-to-die using aligning, thinning, bonding, and through-silicon-via (TSV) technique for constructing 3D interconnected circuits15–18. However, these manufacturing methods tend to be accompanied by some

![](images/486531e85079a37542fafa32920c7b6d71d14b8692c2d4b7c6d7f8fcde8a7056.jpg)

![](images/9d55b5f2f02307e468768d305e27ca868e287c50aac36cc0b7a14aed2e4bbda9.jpg)

![](images/ccbe09113bb69d0271470358ab35b165530cd051c190d864284d84d1d9a5b5a1.jpg)

![](images/b1af1df818ed1114df5bc7965d7298eb38e983ef7a59cd59852031da8b9376eb.jpg)

![](images/07e87ac4e1524779cbf3a3ddccf100e9aab76881cb5d3c4e412f267e6cf4b8d1.jpg)

![](images/abbd2c6750d405a2d861ee0702ddea5fbca8b0c6ce1548221362c87554365e83.jpg)

![](images/6ee6cfee5f486d62a999d7f8527afa1be8b8391594061a92e5a831b45b042f62.jpg)

![](images/16954dcb4f880d4e0a2c2c218b9647cb9156181063f7fc27c234be644af53f9f.jpg)

![](images/d91809736ff074a646edd17bbb3f1fe729773472141b7bbfa79f69ba8bdd5e2e.jpg)

![](images/0da1bdf5420315259ac8eee9b711e82f6cd93343b7ff2f8177e16b950661944d.jpg)  
Schematic and process flow of the 3D Si-MoS CMOS inverter. a Completed Si FinFET on $\mathrm { S i O } _ { 2 } / \mathrm { S i }$ substrate. b Deposition of $\mathsf { S i O } _ { 2 }$ via Fig. 1  PECVD to create an intermediate layer on the FinFET for passivation, followed by chemical mechanical polishing for the thinning and flattening of the $\mathrm { S i O } _ { 2 }$ layer. c Building the monolithic intertier vias (MIVs) by employing contact hole etching and e-beam vapor deposition. d Transferring the monolayer ${ \mathsf { M o S } } _ { 2 }$ triangles on the $\mathrm { S i O } _ { 2 }$ layer. e Fabrication of source/drain electrodes connected to ${ \mathsf { M o S } } _ { 2 }$ using e-beam lithography and e-beam vapor deposition. f E-beam vapor deposition of ${ \sf A l } _ { 2 } { \sf O } _ { 3 }$ dielectric as the top-gate on MoS . g Schematic of a CMOS inverter fabricated by vertically integrating a p-channel Si FinFET and an n-channel monolayer $M O S _ { 2 }$ transistor. The inset shows the crosssectional structure of the Si FinFET. h SEM image of the Si FinFET. Scale bar: 100 μm. i TEM image showing the cross-section of Si FinFET. Scale bar: 25 nm. j Optical image showing the top view of the fabricated 3D CMOS inverter. Scale bar: 100 μm. k Zoom-in image showing the MoS2 FET in k. Scale bar: 10 μm.

concerns, including sizeable parasitic capacitance and enormous residual thermal/mechanical stress in chip substrates. Therefore, incorporating 2D materials into 3D ICs is considered difficult by using conventional TSV-based 3D integration. Auspiciously, monolithic 3D ICs (M3D ICs), enabled by sequential integration of device tiers on the same wafer by deposition or recrystallization, is a relatively feasible strategy for incorporating 2D materials in 3D $| \mathsf { C s } ^ { 1 1 , 1 3 , 1 7 }$ . The high process temperature used during the sequential processes should, nevertheless, be prevented to reduce the thermal budget and to avoid affecting the performance of the lower layer active devices.

This work demonstrates a prototype monolithic 3D CMOS inverter with a vertical-stacking configuration of an upper-tier nchannel ${ \mathsf { M o S } } _ { 2 }$ transistor and a lower-tier p-channel Si FinFET with

20 nm fin width. We utilize the contact hole etching (CHE) technique to fabricate monolithic intertier vias (MIVs) to interconnect the top and bottom transistors, employ chemical mechanical planarization (CMP) to thin down the passivation layer, and perform wet-transfer method towards building the MoS2 FET on the upper-tier. While the lower-tier Si FinFET exhibits very minimal gate leakage current as expected, the upper-tier ${ \mathsf { M o S } } _ { 2 }$ FET also demonstrated negligible leakage. The whole process is kept at a low temperature to comply with the thermal budget needed to avoid the degradation of the lower-tier devices during subsequent fabrication of the upper-tier components. Symmetrical characteristic curves have been observed between the MoS FET and the Si FinFET after changing the MoS FET’s control structure from back-gated to top-gated, which is an

important consideration prior to integrating the devices into a CMOS structure. Consequently, as made apparent by a smoother interface between the e-beam vapor deposition (e-beam VD) grown ${ \sf A l } _ { 2 } { \sf O } _ { 3 }$ top-gate and the ${ \sf M o S } _ { 2 }$ flake, the MoS2 FET’s performance was proven unaffected by the low-temperature dielectric deposition process. The fabricated Si FinFETs display an averaged on/off current ratio of ${ 1 0 ^ { 6 } }$ and an on-current of $1 0 ^ { - 5 } \mathsf { A } ,$ , while ${ \sf M o S } _ { 2 }$ FETs show an on/off current ratio of ${ 1 0 ^ { 6 } }$ and an oncurrent near $1 0 ^ { - 6 } \mathsf { A }$ —implying further a consistent performance between the two unique structured devices as needed for CMOS implementation. The Si FinFET on the bottom tier maintains good electrical properties after subsequent ${ \mathsf { M o S } } _ { 2 }$ FET fabrication, proving that our low-temperature monolithic-like integration method can indeed allow successful integration of 2D materialsbased devices with Si-based devices. The resulting CMOS inverter exhibits inversion signals with a maximum gain value of ~38. It is worth noting that the integration was enabled by deliberately adopting industrially matured techniques, such as CMP and e-beam evaporation, to ensure its compatibility to the existing 3D IC process and to the semiconductor industry in general. Hence, this work demonstrates a feasible manufacturing process to integrate 2D materials into 3D ICs for back-end circuit applications.

# RESULTS AND DISCUSSION

# Manufacturing of M3D CMOS inverter

Figure 1a–g illustrates the step-by-step process of fabricating the proposed monolithic 3D CMOS inverter, in which a top-gated MoS FET was built on top of a Si FinFET. First, a fin-shaped Si channel was fabricated on a $\mathsf { S i O } _ { 2 }$ substrate before a $H \mathsf { f } \mathsf { O } _ { 2 }$ dielectric, wrapped around the channel, was deposited. A TaN/ TiN electrode was then placed on the dielectric sheet to complete the p-type Si FinFET on ${ \mathsf { S i O } } _ { 2 }$ substrate (Fig. 1a). A passivation/ supporting layer that separates the lower-tier Si FinFET from the upper-tier is needed to avoid leakage current or coupling effects between the vertically adjacent devices. Hence, a 750 nm tetraethyl orthosilicate (TEOS) layer was deposited on Si FinFET to serve as the precursor for synthesizing SiO2 via a plasmaenhanced chemical vapor deposition (PECVD) process19. The intermediate $\mathsf { S i O } _ { 2 }$ layer was then thinned down to 250 nm using CMP (Fig. 1b). Vertical holes were then made through the $\mathsf { S i O } _ { 2 }$ layer via the CHE method and then filled with the Al/Cu metals by e-beam evaporation method to connect the Si FinFET to the upper surface of the ${ \mathsf { S i O } } _ { 2 }$ layer (Fig. 1c).

It should be mentioned that the CMP treatment for surface planarization and the CHE method have been commonly used in 3D ICs and adopted here to evaluate process compatibility. Meanwhile, to build the n-type ${ \mathsf { M o S } } _ { 2 }$ FET on the surface of intermediate $\mathsf { S i O } _ { 2 }$ layer, monolayer ${ \mathsf { M o S } } _ { 2 }$ triangles were synthesized on a c-plane sapphire or $\mathsf { S i O } _ { 2 } / \mathsf { S i }$ substrate using CVD and transferred onto the $\mathsf { S i O } _ { 2 }$ surface by wet-transfer technique (Fig. 1d). The size of ${ \mathsf { M o S } } _ { 2 }$ crystals selected for FET fabrication was 10–20 μm. To anchor ${ \sf M o S } _ { 2 }$ samples on the $\mathsf { S i O } _ { 2 }$ intermediate layer, we placed the substrate on a hot plate with a tilt angle of about 60°, and then baked the chip at $1 1 0 ^ { \circ } \mathsf { C }$ for 30 min under ambient conditions. The detailed procedure of wet-transfer has been thoroughly depicted in our previous study20. Ti (10 nm)/Ni (50 nm) source/drain electrodes were subsequently deposited onto the MoS2 sheet (Fig. 1e). To form the high-k/metal gate, a 20 nm ${ \sf A l } _ { 2 } { \sf O } _ { 3 }$ dielectric layer was placed on the ${ \mathsf { M o S } } _ { 2 }$ flake using e-beam VD between the source and drain electrodes (Fig. 1f), followed by a Ti (10 nm)/Ni (50 nm) top-gate electrode to form the ${ \mathsf { M o S } } _ { 2 }$ FET. Finally, another Ti (10 nm)/Ni (50 nm) electrodes were made to connect the upper-tier MoS2 FET and the lower-tier Si FinFET (Fig. 1g) to complete the monolithic 3D CMOS inverter. It is noteworthy that, from PECVD $\mathsf { S i O } _ { 2 }$ process to ${ \sf M o S } _ { 2 }$ FET fabrication, the fabrication processes were conducted at the temperature lower than $2 0 0 ^ { \circ } \mathsf C ,$ which complied with the low thermal budget required by BEOL processes21. Figure 1h–k show the photographs and TEM images of the fabricated 3D CMOS inverter comprising a p-Si FinFET and an $\mathsf { n } { \mathsf { - } } M \mathsf { o } { \mathsf { S } } _ { 2 }$ FET. More details about the fabrication processes are available in the Experimental section.

# Characterizations of Si FinFETs and back-gated MoS2 FETs

The electrical properties and structures of individual FETs were first evaluated before the integration stage. Figure 2a shows the transfer characteristic curves (drain current vs. gate voltage, $I _ { \mathrm { D S } } \mathrm { - } V _ { \mathrm { G S } } )$ of the 12 isolated Si FinFETs with 20 nm fin width on the same wafer. The $I _ { \mathrm { D S } }$ of the Si FinFETs were measured between the source and drain electrodes of the respective devices by sweeping the gate voltage $( V _ { \mathsf { G S } } )$ from –2.0 V to 1.0 V at a drain voltage $V _ { \sf D S } = - 1 \sf V .$ Negative $V _ { \mathsf { G S } }$ enhances the $I _ { \mathsf { D S } } ,$ , confirming that the transistor channels are p-type. The $I _ { \mathrm { D S } } / _ { \mathrm { G S } }$ graph also displays that the on/off current states changed at around $V _ { \mathsf { G S } } = 0 \mathsf { V } ,$ which corresponds to the threshold voltage $( V _ { \mathrm { t h } } )$ of the transistors. Specifically, the $V _ { \mathrm { t h } }$ value is obtained from the linear region of the transfer curve based on the linear extrapolation method, as shown in the inset of Fig. 2a. The output characteristic $( I _ { \mathrm { D } S } - V _ { \mathrm { D } S } )$ curves of

![](images/564a43cd1e70e07a59db7c26319af3366c423a6aff2b7c81771a377a6c36b2c1.jpg)

![](images/19842aac455482332b2523a556c7113067ed585bc9e3f7eb2238494fe101f6d2.jpg)  
Electrical characteristics of the Si FinFET. a Measured transfer characteristics of the 12 Si FinFETs spread on the same wafer $( \bar { V } _ { \mathsf { D } \mathsf { S } } = - 1 \mathsf { V } )$ . The inset shows a linear fitting line to the transfer characteristic to estimate the threshold voltage $( V _ { \mathrm { t h } } ) .$ b Measured output characteristic of a FinFET at applied $V _ { \mathsf { G S } } = 0 . \mathsf { 1 } \lor \mathsf { t o } - 2 \mathsf { V } .$

![](images/0f336946d1836dbd63eac4e4dc716452aca4733f664a6d39fd92d163345667ab.jpg)  
a

![](images/7f92daf3dc0eeb0c01ce45bc45d9f495a2942a702173d2ed3e700748de864233.jpg)  
b

![](images/05f9bfe337605a169636e99f0eecf81440b548c0097eb11bfca4d49a65c3b7b2.jpg)  
C

![](images/5e28b155260f15f3ea83e0e127dfd16437baeb03e22bff7d71594d0a5cc42ae8.jpg)  
d

![](images/5ddbb1aa937229f487301102b5b90bf543c848641ddfbabdae59a15df8862bde.jpg)  
e

![](images/991a509797ba225717bca3b95b4eb76d460537afce779fe94f724ee69f7fd367.jpg)

![](images/10e3b306e3181fc379b4f0a1ac6e78f20808d1891afdb1ebb4de53c3f13d97a2.jpg)  
Material characterization and electrical performance of back-gated $M o S _ { 2 }$ FET on $\mathsf { S i O } _ { 2 } / \mathsf { S i } .$ . a Photoluminescence (PL) spectrum of ${ \mathsf { M o S } } _ { 2 } .$ The inset shows a representative CVD-grown ${ \mathsf { M o S } } _ { 2 }$ flake used in this work. Scale bar, $5 \mu \mathrm { m } .$ . b Raman spectra showing $\mathsf { A } _ { 1 \mathsf { g } }$ and $\mathsf { E } _ { 2 \mathsf { g } } ^ { 1 }$ characteristic peaks of MoS2 before and after wet-transfer. c PL mapping for A exciton peak intensity at 1.85 eV and Raman mapping for the $\mathsf { A } _ { 1 \mathsf { g } }$ and $\mathsf { E } _ { 2 \mathsf { q } } ^ { 1 }$ peaks, all of which are obtained from the MoS2 triangle shown in the inset of a. d Measured transfer characteristics of 23 back-gate ${ \mathsf { M o S } } _ { 2 }$ FETs fabricated in different process batches $( V _ { \mathsf { D S } } = 1 \mathsf { V } )$ . Scale bar, 5 μm. e Measured output characteristics of a back-gated ${ \mathsf { M o S } } _ { 2 }$ FET at $V _ { \mathsf { G S } } = - 1 5 \mathsf { V }$ to 25 V in 5 V steps.

the representative Si FinFET (Fig. 2b) displays that the $I _ { \mathsf { D } \mathsf { S } }$ is near zero and the channel is off when $V _ { \mathsf { G S } }$ is higher than 0.1 V, reaffirming its p-type role in the CMOS circuit. The $I _ { \mathsf { D } \mathsf { S } }$ reaches up to about $3 5 \mu \mathsf { A }$ at $V _ { \mathsf { G S } } = - 2 . 0 \mathsf { V } .$ .

Spectroscopic and electrical properties of the ${ \mathsf { M o S } } _ { 2 }$ films were first characterized before they get employed for monolithic integration with Si-FETs. The optical properties of the MoS2 flakes used in the ${ \sf M o S } _ { 2 }$ FET fabrication were recorded before and after the wet-transfer process. The PL spectrum (Fig. 3a) of a representative ${ \mathsf { M o S } } _ { 2 }$ flake under 532 nm laser excitation shows an A exciton peak at 672 nm, indicating a semiconductor bandgap g  light condition, s $E _ { \mathrm { q } } \sim 1 . 8 5 \mathrm { e V } ^ { 9 , \dot { 2 } 2 , 2 3 }$ . Its Raman spectrum (Fig. 3b), under the same fference (Δ) between the $\mathsf { A } _ { 1 \mathsf { g } }$ and $\mathsf { E } _ { 2 \mathsf { q } } ^ { 1 }$ $1 7 . 8 \mathsf { c m } ^ { - 1 }$ monolayer ${ \sf M o S } _ { 2 }$ reported in most studies22–24. In addition, the shift of the $\mathsf { E } _ { 2 \mathsf { g } } ^ { 1 }$ vibration mode is an indication of defect concentration in 2D TMD material $\mathsf { S } ^ { 2 5 , 2 6 }$ . There was no noticeable change in the $\mathsf { E } _ { 2 \mathsf { g } } ^ { 1 }$ peak position found after wet-transfer, revealing that the quality of ${ \sf M o S } _ { 2 }$ was not seriously affected by the wettransfer process. The PL/Raman mapping (Fig. 3c) with respect to the A exciton/Raman peak intensity shows consistency all throughout the sample. Based on these spectroscopic analyses, the CVD-grown ${ \sf M o S } _ { 2 }$ samples were identified to be monolayers with high uniformity.

Initially, back-gated ${ \mathsf { M o S } } _ { 2 }$ FETs on ${ \mathsf { S i O } } _ { 2 }$ layer were built and the electrical characteristic curves (Fig. 3d), performed using the same measuring parameters as those used in the Si FinFET, displayed consistent and steady n-FET performances among different

devices, where the N-Methyl-2-Pyrrolidone (NMP) wet cleaning process played a critical role as discussed in our previous ${ \mathsf { w o r k } } ^ { 2 7 }$ The on-current level of these 23 back-gated MoS FETs was able to be tuned from $1 0 ^ { - 7 }$ to $1 0 ^ { - 5 } { \mathsf { A } }$ depending on the channel length (from 3 to 0.16 μm), which served as a tuning nobe for optimizing the on-current and the on/off ratio to match with the Si FinFET. In addition, Fig. 3e displays the $I _ { \mathrm { D S } } \mathrm { - } V _ { \mathrm { D S } }$ characteristic curves of a representative device at different gate voltages showing that the $I _ { \mathsf { D } \mathsf { S } }$ becomes zero when $V _ { \mathsf { G S } }$ is lower than $- 1 5 \mathsf V ,$ confirming its function as an n-type device for the CMOS circuit. The maximum $I _ { \mathsf { D } \mathsf { S } }$ reached around $4 0 \mu \mathsf { A }$ at $V _ { \mathsf { G S } } = 5 \mathsf { V } .$ Evidently, however, the $V _ { \mathrm { t h } }$ of the back-gated ${ \mathsf { M o S } } _ { 2 }$ FETs are too far from the Si FinFET’s, consequently indicating an asymmetric relationship with the Si FinFET for CMOS application.

# Performance of top-gated $M O S _ { 2 }$ FET on upper-tier

The prominent performance of top-gated FET structures compared to their back-gated counterparts28–30, and the known advantages of ${ \sf A l } _ { 2 } { \sf O } _ { 3 }$ dielectrics, such as high dielectric constant, excellent stability, and a reported induced positive $V _ { \mathrm { t h } }$ shifting when used as a substrate replacing $\mathsf { S i O } _ { 2 } ^ { 3 1 }$ , have motivated the fabrication of top-gated $\mathsf { A l } _ { 2 } \bar { \mathsf { O } } _ { 3 } / \mathsf { M o } \bar { \mathsf { S } } _ { 2 }$ FET structures $^ { 1 0 , 3 2 }$ as the upper-tier device for this work. Apparently, the $V _ { \mathrm { t h } }$ of the developed top-gated ${ \mathsf { M o S } } _ { 2 }$ FETs, in which the result of a representative device is shown in Fig. 4a, has gotten closer and more symmetrical with that of the corresponding Si FinFET (Fig. 4b). The shifting of the $V _ { \mathrm { t h } }$ to a lower negative (near zero) value may arise from several possible factors, which include reduced

![](images/73715432724e268bfcbdd6059d5dddb6129bb7bd26c77fad8eee34be6b8a6d32.jpg)

![](images/6c01ff9828a8af19c900afb572a113b5b2d7cb4a313d7786ae186a74e1b3eb68.jpg)

![](images/a670700c32b6a3d755d6b82b66aeaa364d51674c8dc891b98af914bedd19fc7e.jpg)  
Electrical characteristics of top-gated MoS2 FET on upper-tier and lower-tier Si FinFET. Measured transfer characteristics of a a top-Fig. 4gate MoS2 FET on intermediate SiO2 layer and b a Si FinFET on Si/SiO2 $( V _ { \mathsf { D } 5 } = 0 . 0 5 \mathsf { V }$ and 1.00 V). For the Si FinFET, the measurement was conducted before and after the MoS2 FET fabrication. In a and b, the gate current $( I _ { \mathsf { G S } } )$ was measured to acquire the level of the leakage current in the fabricated transistors. c Schematic of the top-gated MoS2 FET. The TEM image shows the cross-section of the top-gated ${ \mathsf { M o } } { \bar { \mathsf { S } } } _ { 2 }$ FET. Scale bar, 10 nm.

<table><tr><td colspan="9">Table 1. Transistor parameters of the p-type Si FinFET and n-type MoS2 FET combined in CMOS inverter.</td></tr><tr><td>Device</td><td>Dielectric thickness (nm)</td><td>Dielectric constant37</td><td>Length (μm)</td><td>Width (μm)</td><td>C (Fm-2)</td><td>μ (cm2V-1s-1)</td><td>SS (mV/dec)</td><td>Conductance (S)</td></tr><tr><td>MoS2 FET</td><td>20</td><td>Al2O3: 9.8</td><td>~1</td><td>~7</td><td>~3.98 × 10-3</td><td>~0.2</td><td>~130</td><td>~1.12 × 10-7</td></tr><tr><td>Si FinFET</td><td>2.5</td><td>HfO2: 25</td><td>~7.0 × 10-2</td><td>~2.0 × 10-2</td><td>~4.96 × 10-2</td><td>2.51</td><td>~80</td><td>~3.08 × 10-5</td></tr></table>

fixed charges in the ${ \sf A l } _ { 2 } { \sf O } _ { 3 }$ and a lower trap density at the ${ M O S } _ { 2 } / { }$ ${ \sf A l } _ { 2 } { \sf O } _ { 3 }$ interface as governed by the numerical simulation in the previous $\mathsf { r e p o r t } ^ { 3 3 } .$ Concurrently, a more systematic investigation of this positive shifting of the $V _ { \mathrm { t h } }$ is in progress. The gate leakage current $( I _ { \mathsf { G S } } )$ in the top-gated device is also very minimal, which is the same order $( \sim 1 0 ^ { - 1 2 } \mathsf { A } )$ as in the back-gated operation. The smooth interface between the ${ \sf A l } _ { 2 } { \sf O } _ { 3 }$ and ${ \mathsf { M o S } } _ { 2 }$ layers, as shown in the TEM image in Fig. $^ { 4 \ C , }$ implies that the $A l _ { 2 } O _ { 3 }$ deposition by e-beam has not caused pronounced damage to the MoS flake, in contrast to the atomic layer deposition (ALD) technique that could degrade the device performance. Looking closer to the characteristic curve of the top-gated MoS2 FET in Fig. 4a, the $I _ { \mathrm { D S } }$ has reached ${ \sim } 1 0 ^ { - 6 } \mathsf { A }$ and the $V _ { \mathrm { t h } } = - 1 . 3 \vee .$ The on/off current ratios are approximately $1 0 ^ { 4 }$ and $1 0 ^ { 5 }$ at $V _ { \mathrm { D S } } = 0 . 0 5 \ : \forall$ and 1.00 V, respectively. The subthreshold swing (SS) of the device can be obtained according to its definition, $S S = \partial V _ { \odot 5 } / \partial \log _ { 1 0 } I _ { \mathsf { D S } }$ , and has a value of 129.5 mV/dec at $V _ { \sf D S } = 1 \sf V ,$ which becomes smaller compared with the back-gated ${ M o S } _ { 2 }$ FETs. Lastly, the field-effect electron mobility (μ) was calculated based on μ ¼ LW C V ∂IDS∂V  $\begin{array} { r } { \mu = \frac { L } { W \cdot C \cdot V _ { \mathrm { D S } } } \biggl ( \frac { \partial I _ { \mathrm { D S } } } { \partial V _ { \mathrm { G S } } } \biggr ) } \end{array}$ where L stands for the channel length, W the channel width, C the capacitance of the top-gate $( \mathsf { A l } _ { 2 } \mathsf { O } _ { 3 } )$ , and $\partial I _ { \mathrm { D S } } / \partial V _ { \mathsf { G S } }$ the slope of the transfer curve. The calculated μ value is $0 . 2 \mathsf { c m } ^ { 2 } \mathsf { V } ^ { - 1 } \mathsf { s } ^ { - 1 }$ .

The transfer characteristic of the Si FinFET with fin width of 20 nm was again measured in order to ensure good and unaffected electrical performance after the ${ \sf M o S } _ { 2 }$ FET fabrication. As shown in Fig. 4b, the measured transfer curves of the the Si FinFET at drain voltages $V _ { \mathrm { D S } } = 0 . 0 5 \ : \forall$ and 1.00 V were found almost the same before and after the MoS FET fabrication, indicating that the subsequent MoS2 FET process had not damaged the electrical characteristic of the Si FinFET. This may strongly be attributed to the low-temperature processes used in building the upper-tier components. The SS of the Si FinFET can be estimated to 80.6 mV/dec at $V _ { \mathsf { D S } } = 1 \mathsf { V } .$ . The on-current value is increased to approximately $1 0 ^ { - 5 } \mathsf { A }$ at its maximum, and a negligible level of $I _ { \mathsf { G S } }$ with four orders of magnitude lower than the $I _ { \mathrm { D S } }$ is observed. For comparison purposes, the on/off current ratio of the Si FinFET and the MoS FET has the same order of magnitude, whereas the on-current of the former is an order of magnitude larger than that of the latter. The acceptable

similarities of the electric current properties of the two unique structured devices imply a compatible performance between them, which is needed for CMOS implementation. Such matched electrical results have also been reliably obtained in other fabricated devices. Table 1 summarizes the measured parameters and electrical characteristics of the Si FinFET and the ${ \mathsf { M o S } } _ { 2 }$ FET that we deliberately used for the demonstration of our CMOS inverters. The size of the MoS2 FET is more significant than that of the Si FinFET by one order of magnitude. Likewise, the mobility of the former is one order of magnitude lower than that of the latter. Both FETs have almost similar SS values. The dimension of the MoS FET can be scaled to match with Si FinFET with the further improvement of the contact resistance and field-effect mobility. For this, utilizing Bi/Au as the contact metal is a promising strategy recently reported realizing a high on-current level for ultrashort channel 2D FETs2 . The relevant experiments are needed to further improve our 3D CMOS device architectures.

# Demonstration of M3D CMOS inverter and benchmarks

After being verified with good electrical performance, the p-type Si FinFET and the n-type top-gated MoS2 FET were interconnected to form a 3D CMOS inverter. Figure 5a shows the inverter’s voltage transfer characteristics $( V _ { \mathrm { { O U T } } } \lor 5 . \ V _ { \_ N } )$ by varying the power supply voltage $V _ { \mathsf { D D } }$ from 0.1 V to 2.1 V in 0.5 V steps. An evident signal inversion was observed with high $V _ { \mathrm { O U T } }$ at low $V _ { \mathsf { I N } _ { r } }$ , and vice versa, and the corresponding gain $( \partial V _ { \mathrm { O U T } } / \partial V _ { \mathrm { I N } } )$ was successively obtained. The maximum gain in this CMOS is approximately 30.8 at $V _ { \sf D D } = 2 . 1 \sf V .$ This inverter displays 5 μW power consumption in the static states. For the evaluation of its noise margin, Fig. 5b shows the forward and reverse curves of the inverter’s logic voltage level, where the logic low output voltage $( V _ { \circ { \mathsf { I } } } = 0 . 0 6 3 \ : \mathsf { V } ) ,$ , logic low input voltage $( V _ { \mathrm { i l } } = 1 . 0 0 6 \ : \forall ) ,$ , logic high input voltage $( V _ { \mathrm { i h } } = 1 . 2 6 1 \ : \mathrm { V } )$ , and logic high output voltage $( V _ { \mathrm { o h } } = 2 . 0 3 7 \ : \forall )$ are shown. When the inverter is applied with a low input voltage, the noise margin low $( N M _ { \mathrm { L } } = V _ { \mathrm { o l } } - V _ { \mathrm { i l } } )$ was 0.449 $V _ { \mathsf { D D } }$ at $V _ { \mathsf { D D } } { = } 2 . 1 \lor . \mathsf { A }$ high input voltage has a noise margin high $( N M _ { \mathsf { H } } = V _ { \mathsf { i h } } - V _ { \mathsf { o h } } )$ of 0.370 VDD at $V _ { \mathrm { D D } } = 2 . 1 \ : \mathrm { V } .$ . Supplementary Fig. 1 shows the electrical characteristics of other inverters, where good signal inversion is also evident, and deviations among different devices are barely

![](images/ce55ded20be74d00d71cd6b89adfed655eba56b9bcd7ebf38e5c11d7cadf9c3f.jpg)

![](images/5672fcd84129bdc79a35445512c5d04a8fc9b7f2e89370254c0d34858f19e331.jpg)  
Output characteristics of 3D $S i - M o S _ { 2 }$ complementary inverter. a Voltage transfer characteristics of the 3D CMOS inverter for power Fig. 5supply voltage $( V _ { \mathsf { D D } } )$ from 0.1 V to 2.1 V in 0.5 V steps. Peaks in the red curves indicate the corresponding voltage gain at different $V _ { \mathsf { D D } } .$ . b Noise margin of a CMOS inverter. When the inverter was applied with a low input voltage, the noise margin low (NML) is 0.449 VDD $( V _ { \mathsf { D D } } = 2 . 1 \mathsf { V } )$ . When applied with a high input voltage, the inverter has a noise margin high $( N M _ { \sf H } )$ of $0 . 3 7 0 ~ V _ { \mathrm { D D } } ~ ( \breve { V } _ { \mathrm { D D } } = 2 . 1 \check { \vee } )$ .

Comparison of the inverter performance in this work and other researchers’ works.   

<table><tr><td>Refs.</td><td>Channel P-type N-type</td><td>Substrate</td><td>Max.-Min. voltage</td><td>Max. gain</td><td>Transition voltage</td><td>Power consumption</td></tr><tr><td rowspan="2">Our work</td><td>p-type Si</td><td rowspan="2">Si</td><td>VIN= -2 V-2 V</td><td rowspan="2">38</td><td rowspan="2">0.6 V</td><td rowspan="2">~5 μW</td></tr><tr><td>n-type MoS2</td><td>VDD= 0.1 V-2.1 V</td></tr><tr><td rowspan="2">9</td><td>p-type Si nanomembranes</td><td rowspan="2">PET</td><td>VIN= -2 V-5 V</td><td rowspan="2">16</td><td rowspan="2">2.3 V</td><td rowspan="2">14 nW</td></tr><tr><td>n-type MoS2</td><td>VDD= 5 V</td></tr><tr><td rowspan="2">38</td><td>p-type Si FinFET</td><td rowspan="2">N/A</td><td>VIN= 0 V-0.3 V</td><td rowspan="2">N/A</td><td rowspan="2">0.15 V</td><td rowspan="2">N/A</td></tr><tr><td>n-type Si FinFET</td><td>VDD= 0.3 V</td></tr><tr><td rowspan="2">39</td><td>p-type Si FinFET</td><td rowspan="2">N/A</td><td>VIN= -1 V-1 V</td><td rowspan="2">N/A</td><td rowspan="2">N/A</td><td rowspan="2">5.2 μW</td></tr><tr><td>n-type Si FinFET</td><td>VDD= Not report</td></tr><tr><td rowspan="2">40</td><td>p-type Si FinFET</td><td rowspan="2">Si</td><td>VIN= -1 V-1 V</td><td rowspan="2">15</td><td rowspan="2">0.5 V</td><td rowspan="2">N/A</td></tr><tr><td>n-type Si FinFET</td><td>VDD= 0.1 V-2.1 V</td></tr><tr><td rowspan="2">41</td><td>p-type Ge FinFETs</td><td rowspan="2">SOI</td><td>VIN= 0 V-1.2 V</td><td rowspan="2">50</td><td rowspan="2">0.6 V</td><td rowspan="2">N/A</td></tr><tr><td>n-type Ge FinFETs</td><td>VDD= 0.2 V-1.2 V</td></tr></table>

observed. Also therein, a maximum voltage gain of ~38 was recorded. The comparison between our work and other reported works in terms of channel type and performance is summarized in Table 2. Our inverter presents a similar level in voltage gain, transition voltage, power consumption, and $V _ { \mathsf { I N } }$ and $V _ { \mathsf { D D } }$ range compared to current FinFET inverters. All these results imply that high-quality $S i { \mathrm { - } } M \circ S _ { 2 }$ hybrid CMOS inverters with stable and reproducible device performance were achieved by the proposed manufacturing process.

# Critical considerations concerning future M3D CMOS devices with 2D materials

In the proposed 3D inverter, additional layout electrodes were fabricated to interconnect two FETs after the device-to-device variability in 2D MoS2 FETs and Si FinFETs had been checked. However, these layouts required extra area for interconnection, which would cause a limitation to IC density in future heterointegration. To increase integration density, common gate electrodes and vertically stacked heterostructures with back-gated 2D FET are promising solutions. In this regard, large-scale, singlecrystalline 2D materials growth and reliable transfer method have been demonstrated34,35, which are crucially important to boost the integration efficiency. The proposed process is expected to be

utilized in future M3D heterostructures with large-scale 2D materials.

It should also be noted that 3D self-aligned device architectures with vertically stacked n- and $\mathsf { p \mathrm { - } F E T s , }$ recently achieved in semiconductor nanoribbon transistor stacks36, will be a potential next step for the proposed M3D heterointegration with 2D material transistors. In such kind of device, the gate-all-around (GAA) architecture promises improved electrostatic control of the channel, enhanced current per area, and further device scaling. The GAA multichannel transistor stacks via vertically stacking nand p-FETs provide a promising way toward 3D CMOS heterointegrations with high integration density. Accordingly, 2D materials feature uniform and clean surfaces states that avoid strong scattering of the charge carriers, which makes 2D FET exhibit excellent electronic properties to the ultimate limit of miniaturization in the vertical direction. Therefore, 2D materials can be a basic material for multichannel stacked transistors or GAA structure36 in future advanced electronics13. Furthermore, 2D materials device via transfer methods can be fabricated with a low-temperature process, which may mitigate the thermal budget issue in 3D ICs BEOL process.

In summary, a monolithic 3D CMOS inverter was fabricated by vertically integrating a p-type Si FinFET with 20 nm fin width and an n-type ${ \mathsf { M o S } } _ { 2 }$ FET. To fabricate the ${ \sf M o S } _ { 2 }$ FET upon the Si FinFET

while effectively maintaining the device performance of the Si FinFET, we chose to utilize a series of low-temperature processes, including spin coating, CMP, CHE, e-beam lithography, wettransfer, and e-beam VD. Exclusively, to prevent damaging the ${ \mathsf { M o S } } _ { 2 }$ layer and tuning $V _ { \mathrm { t h } }$ voltage, e-beam VD was utilized in depositing the ${ \sf A l } _ { 2 } { \sf O } _ { 3 }$ top-gate dielectric instead of ALD. Consequently, symmetrical characteristic curves have been observed between the MoS2 FET and the Si FinFET after changing the MoS2 FET’s control structure from back-gated to top-gated. Moreover, the on/off current ratio and the on-current of both transistors show similar levels, which imply a compatible performance between the two unique structured devices as needed for CMOS implementation. The fabricated 3D inverter exhibits evident signal inversion with a maximum voltage gain of ~38. This work not only proves that 2D material-based and Si-based transistors can be integrated compatibly to form a CMOS inverter, despite their intrinsically distinct band structures, but demonstrates a feasible manufacturing method to integrate 2D materials into 3D ICs.

# METHODS

# Other details concerning the device fabrication

Atomic Layer Deposition (ALD) process was used to grow the HfO2 layer around the fin-shaped Si channel. The tetraethyl orthosilicate (TEOS) passivation layer was applied via spin-coating. Al/Cu and Ni/ Ti metal electrodes were deposited using a sequence of processes, namely the e-beam lithography, e-beam vapor deposition, and photoresist lift-off in such order. Likewise, a sequence of processes was used to perform the contact hole etching step, consisting of e-beam lithography, etching, and e-beam vapor deposition.

# Electrical measurements on the FET devices

Electrical characterizations were performed via three-terminal I-V measurement using a semiconductor analyzer (Keithley model 2636B). The measurements were conducted at room temperature and under ambient atmosphere.

# Optical characterization of the monolayer MoS2

Raman and photoluminescence (PL) measurements were conducted via an integrated confocal optical microscope system with a spectrometer (Kymera 328i, Andor). The light source is a 532 nm continuous wave laser operated at 14.5 mW for Raman and 150 μW for PL measurements (with 100×, N.A. = 0.9 objective lens), respectively. All measurements were conducted at room temperature.

# DATA AVAILABILITY

The data that support the findings of this study are available from the corresponding author upon reasonable request.

Received: 27 December 2021; Accepted: 11 July 2022;

Published online: O7 February 2023

# REFERENCES

1. Radisavljevic, B., Whitwick, M. B. & Kis, A. Integrated circuits and logic operations based on single-layer MoS . ACS Nano 5, 9934–9938 (2011).   
2. Shen, P. C. et al. Ultralow contact resistance between semimetal and monolayer semiconductors. Nature 593, 211–217 (2021).   
3. Akinwande, D., Petrone, N. & Hone, J. Two-dimensional flexible nanoelectronics. Nat. Commun. 5, 5678 (2014).   
4. Liu, Y. et al. Valleytronics in transition metal dichalcogenides materials. Nano Res. 12, 2695–2711 (2019).   
5. Radisavljevic, B., Radenovic, A., Brivio, J., Giacometti, V. & Kis, A. Single-layer MoS transistors. Nat. Nanotechnol. 6, 147–150 (2011).   
6. Wang, H. et al. Integrated circuits based on bilayer MoS2 transistors. Nano Lett. 12, 4674–4680 (2012).

7. Yu, H., Liu, G. B., Gong, P., Xu, X. & Yao, W. Dirac cones and Dirac saddle points of bright excitons in monolayer transition metal dichalcogenides. Nat. Commun. 5, 3876 (2014).   
8. Liu, S. et al. Hysteresis-free hexagonal boron nitride encapsulated 2D semiconductor transistors, NMOS and CMOS inverters. Adv. Electron. Mater. 5, 1800419 (2019).   
9. Das, T. et al. Highly flexible hybrid CMOS inverter based on Si nanomembrane and molybdenum disulfide. Small 12, 5720–5727 (2016).   
10. Lin, C. Y. et al. Polarity-controllable MoS2 transistor for adjustable complementary logic inverter applications. Nanoscale Horiz. 5, 163–170 (2020).   
11. Jiang, J., Parto, K., Cao, W. & Banerjee, K. Ultimate monolithic-3D integration With 2D materials: rationale, prospects, and challenges. IEEE J. Electron Devices Soc. 7, 878–887 (2019).   
12. Ko, C. T. & Chen, K. N. Reliability of key technologies in 3D integration. Microelectron. Reliab. 53, 7–16 (2013).   
13. Liu, Y. et al. Promises and prospects of two-dimensional transistors. Nature 591, 43–53 (2021).   
14. Su, C. J. et al. 3D integration of vertical-stacking of MoS2 and Si CMOS featuring embedded 2T1R configuration demonstrated on full wafers. In: 2020 IEEE International Electron Devices Meeting (IEDM) 12.2.1–12.2.4 (IEEE, 2020).   
15. Hsueh, F. K. et al. TSV-free FinFET-based monolithic 3D+-IC with computing-inmemory SRAM cell for intelligent IoT devices. In: 2017 IEEE International Electron Devices Meeting (IEDM). 12.16.1–12.16.4 (IEEE, 2017).   
16. Papanikolaou, A., Soudris, D. & Radojcic, R. Three Dimensional System Integration. (Springer, 2011).   
17. Sachid, A. B. et al. Monolithic 3D CMOS using layered semiconductors. Adv. Mater. 28, 2547–2554 (2016).   
18. Samal, S. K., Nayak, D., Ichihashi, M., Banna, S. & Lim, S. K. Monolithic 3D IC vs. TSVbased 3D IC in 14 nm FinFET technology. In: 2016 IEEE SOI-3D-Subthreshold Microelectronics Technology Unified Conference (S3S) 1–2 (IEEE, 2016).   
19. Mahajan, A. M., Patil, L. S., Bange, J. P. & Gautam, D. K. TEOS-PECVD system for high growth rate deposition of SiO2 films. Vacuum 79, 194–202 (2005).   
20. Simbulan, K. B. C., Chen, P. C., Lin, Y. Y. & Lan, Y. W. A Standard and reliable method to fabricate two-dimensional nanoelectronics. JoVE 138, e57885 (2018).   
21. Fenouillet-Beranger, C. et al. Guidelines for intermediate back end of line (BEOL) for 3D sequential integration. In: 2017 47th European Solid-State Device Research Conference (ESSDERC) 252–255 (IEEE, 2017).   
22. Splendiani, A. et al. Emerging photoluminescence in monolayer MoS2. Nano Lett. 10, 1271–1275 (2010).   
23. Sun, L. et al. Plasma modified MoS2 nanoflakes for surface enhanced raman scattering. Small 10, 1090–1095 (2014).   
24. Simbulan, K. B. et al. Selective photoexcitation of finite-momentum excitons in monolayer MoS by twisted light. ACS Nano 15, 3481–3489 (2021).   
25. Kou, Z., Hashemi, A., Puska, M. J., Krasheninnikov, A. V. & Komsa, H. P. Simulating Raman spectra by combining first-principles and empirical potential approaches with application to defective MoS . NPJ Comput. Mater. 6, 1–7 (2020).   
26. Parkin, W. M. et al. Raman shifts in electron-irradiated monolayer MoS . ACS Nano 10, 4134–4142 (2016).   
27. Chen, P. C. et al. Effective N-methyl-2-pyrrolidone wet cleaning for fabricating high-performance monolayer MoS transistors. Nano Res. 12, 303–308 (2018).   
28. Sanne, A. et al. Top-gated chemical vapor deposited MoS2 field-effect transistors on Si3N4 substrates. Appl. Phys. Lett. 106, 062101 (2015).   
29. Radisavljevic, B. & Kis, A. Mobility engineering and a metal-insulator transition in monolayer MoS2. Nat. Mater. 12, 815–820 (2013).   
30. Yu, Z. et al. Analyzing the carrier mobility in transition-metal dichalcogenide MoS field-effect transistors. Adv. Funct. Mater. 27, 1604093 (2017).   
31. Li, T., Wan, B., Du, G., Zhang, B. & Zeng, Z. Electrical performance of multilayer MoS2 transistors on high-κ Al2O3 coated Si substrates. AIP Adv. 5, 057102 (2015).   
32. Lan, Y. W. et al. Scalable fabrication of a complementary logic inverter based on MoS fin-shaped field effect transistors. Nanoscale Horiz. 4, 683–688 (2019).   
33. Matsuura, K. et al. Sputter-deposited-MoS2 nMISFETs with top-gate and Al2O3 passivation under low thermal budget for large area integration. IEEE J. Electron Devices Soc. 6, 1246–1252 (2018).   
34. Li, T. et al. Epitaxial growth of wafer-scale molybdenum disulfide semiconductor single crystals on sapphire. Nat. Nanotechnol. 16, 1201–1207 (2021).   
35. Shen, Y. C. et al. Rational design on wrinkle‐less transfer of transition metal dichalcogenide monolayer by adjustable wettability‐assisted transfer method. Adv. Funct. Mater. 31, 2104978 (2021).   
36. Huang, C. Y. et al. 3-D Self-aligned stacked NMOS-on-PMOS nanoribbon transistors for continued Moore’s Law Scaling. In: 2020 IEEE International Electron Devices Meeting (IEDM) 20.6.1–20.6.4 (IEEE, 2020).   
37. Robertson, J. High dielectric constant oxides. EPJ Appl. Phys. 28, 265–291 (2004).   
38. Rendón, M. et al. Performance benchmarking of TFET and FinFET digital circuits from a synthesis-based perspective. Electronics 11, 632 (2022).   
39. Sathe, M. & Sarwade, N. Performance comparison of CMOS and Finfet based circuits At 45nm technology using SPICE. Int. J. Eng. Res. Appl. 4, 39–43 (2014).

40. Zaman, S. S., Kumar, P., Sarma, M. P., Ray, A. & Trivedi, G. Design and Simulation of SF-FinFET and SD-FinFET and Their Performance in Analog, RF and Digital Applications. In: 2017 IEEE International Symposium on Nanoelectronic and Information Systems (iNIS) 200–205 (IEEE, 2017).   
41. Yeh, M. S. et al. Ge FinFET CMOS inverters with improved channel surface roughness by using in-situ ALD digital O3 treatment. IEEE J. Electron Devices Soc. 6, 1227–1232 (2018).

# ACKNOWLEDGEMENTS

This work was supported by the Ministry of Science and Technology of Taiwan through grant MOST 108-2112-M-033-006, MOST 111-2119-M-008-003-MBK, MOST 111-2628-M-003-002-MY3 and 108-2112-M-003-010-MY3. This work was also, in part, supported by National Taiwan Semiconductor Research Institute. L.J.L. thanks the support from the Jockey Club Hong Kong to the JC STEM lab of 3DIC, and the Research Grant of Council of Hong Kong (CRS_PolyU502/22), and the National Key R&D Project of China (2022YFB4044100).

# AUTHOR CONTRIBUTIONS

S.X.G., C.H.Y., and C.J.H. synthesized MoS2 samples. S.X.G., C.J.H., J.H.C., and C.J.S. fabricated the devices. S.X.G., T.H.Y, C.H.Y., J.H.C., B.W.L. and C.J.S. performed the electrical measurement and data analysis. T.H.Y. and K.B.S. performed Raman and photoluminescence spectroscopy and data analysis. S.X.G., T.H.Y., B.W.L. and K.B.S. wrote the manuscript. K.S.L., Y.L.Z., L.J.L., and Y.W.L. supervised this work. Y.L.Z., L.J.L., and Y.W.L. reviewed and edited the manuscript.

# COMPETING INTERESTS

The authors declare no competing interests.

# ADDITIONAL INFORMATION

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41699-023-00371-7.

Correspondence and requests for materials should be addressed to Kai-Shin Li, Yuan-Liang Zhong, Lain-Jong Li or Yann-Wen Lan.

Reprints and permission information is available at http://www.nature.com/ reprints

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/4e1a5a59702a98ded4ac92c95a686f9c5601bb241aff8c77eff0c94153db6e75.jpg)

Open Access This article is licensed under a Creative Commons

Attribution 4.0 International License, which permits use, sharing, tribution and reproduction in any medium or format, as long as you give dit to the original author(s) and the source, provide a link to the Creative se, and indicate if changes were made. The images or other third party article are included in the article’s Creative Commons license, unless wise in a credit line to the material. If material is not included in the Commons license and your intended use is not permitted by statutory xceeds the permitted use, you will need to obtain permission directly pyright holder. To view a copy of this license, visit http:// ns.org/licenses/by/4.0/.

© The Author(s) 2023