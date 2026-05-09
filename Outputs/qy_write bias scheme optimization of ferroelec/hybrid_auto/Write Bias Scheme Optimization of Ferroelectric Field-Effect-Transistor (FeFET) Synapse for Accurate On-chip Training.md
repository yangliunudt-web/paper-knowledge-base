---
title: "Write Bias Scheme Optimization of Ferroelectric Field-Effect-Transistor (FeFET) Synapse for Accurate On-chip Training"
authors:
  - "Seungmin Kang"
  - "Sangwan Kim"
date: "2023-09-01"
year: "2023"
journal: "IEEE Electron Device Letters"
abstract: "Through technology computer-aided-design (TCAD) simulation and FeFET capacitor measurement, we optimized the write bias scheme in on-chip training of HfO2-based FeFET synapse to improve training accuracy. With the optimized write bias scheme secured in this work, 4-bit synaptic operation was confirmed even in the presence of D2D variations in remanent polarization (Pr) and coercive field (Ec) induced by the FeFET film process and the wake-up procedure."
abstract_cn: "通过TCAD仿真和FeFET电容测量，我们优化了HfO2基FeFET突触片上训练的写入偏置方案以提高训练精度。采用优化的写入偏置方案，即使在FeFET薄膜工艺和唤醒过程引起的剩余极化和矫顽场的器件间差异存在的情况下，仍确认了4位突触操作。通过系统优化读写电压，实现了增强和抑制特性的高对称性和线性度。"
keywords:
  - "[[FeFET]]"
  - "[[Synapse]]"
  - "[[On-Chip Training]]"
  - "[[Write Bias Scheme]]"
  - "[[HfO2]]"
  - "[[铁电晶体管]]"
  - "[[片上训练]]"
cite: "[1] Kang et al. Write Bias Scheme Optimization of Ferroelectric Field-Effect-Transistor (FeFET) Synapse for Accurate On-chip Training[J]. IEEE Electron Device Letters, 2023."
aiSum: "通过TCAD仿真优化FeFET突触片上训练的写入偏置方案，实现4位突触操作和高对称性/线性度的增强抑制特性，即使在工艺变异下仍保持良好性能。"
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
  - "[[HfO2]]"
---

# Write Bias Scheme Optimization of Ferroelectric Field-Effect-Transistor (FeFET) Synapse for Accurate On-chip Training

Seungmin Kang, Sangwan Kim, and Sihyun Kim Department of Electronic Engineering, Sogang University, 04107, South Korea Email: skim@sogang.ac.kr

Abstract— Through technology computer-aided- design (TCAD) simulation and [[FeFET]] capacitor measurement, we optimized the write bias scheme in [[On-chip training]] of HfO2- based [[FeFET]] field-effect-transistor ([[FeFET]]) [[Synapse]] to improve training accuracy. With the optimized write bias scheme secured in this work, 4-bit synaptic operation was confirmed even in the presence of D2D variations in remanent polarization (Pr) and coercive field $( E \mathrm { c } )$ induced by the [[FeFET]] film process and the wake-up procedure.

Keywords; [[FeFET]], [[Synapse]], [[FeFET]], [[Device-to-device variation]], [[On-chip training]]

# I. INTRODUCTION

HfO2-based [[FeFET]] field-effect-transistors ([[FeFET]]s) have recently attracted an exceptional attention as artificial intelligence (AI) semiconductor devices, owing to the lowvoltage/fast switching and excellent data retention as well as their fine weight control. However, [[FeFET]]s suffer from weight accuracy decrement due to the variation of threshold voltage $( V _ { \mathrm { t h } } )$ caused by the deviation of [[FeFET]] properties, namely the remanent polarization (Pr) and the coercive field (Ec) [1]. These variations occur from random domain changes in [[FeFET]] films during wake-up process [2]. Therefore, an optimal write bias scheme for linear drainto-source conductance (Gds) mapping is highly required [3]. In this work, we develop an optimized write bias scheme for [[FeFET]] [[Synapse]], considering the device-to-device (D2D) variation through metal-[[FeFET]]-metal (MFM) capacitor measurements and SentaurusTM technology computer-aideddesign (TCAD) simulation.

# II. METAL-[[FeFET]]-METAL CAPACITOR FABRICATION AND MODELING

The [[FeFET]] film undergoes a wake-up process from the pristine state, during which the $P _ { \mathrm { ~ r ~ } }$ increases with the growth of the orthorhombic phase (o-phase). In this process, the boundary of the [[FeFET]] domain changes, leading to D2D variations in $P _ { \mathrm { ~ r ~ } }$ and $E _ { \mathrm { { c } } } .$ To determine how these variations affect the accuracy of [[On-chip training]], the MFM capacitors were fabricated and measured to model [[FeFET]] parameters $( P _ { \mathrm { r } }$ and $E _ { \mathrm { c } } )$ and variations through TCAD simulation.

# A. Fabrication

![](images/1e13d59dbe6052f62a7a36a1c2a3e1daa2797a0f0fc2cdf1a835092e422501be.jpg)  
(a)

![](images/04c375d3a5cf1ad94f1da91e687e84adaca4408430aff1b8f506cb6728c96691.jpg)  
(b)

![](images/4c95f13ecd26b9021c7ee81032bce9661168a96a53da02112d24d115e19b717b.jpg)  
(c)

![](images/ac8b98a5463aef7a57d329f0ad799d8eb6a4d41d916142eee76ddc627223ed21.jpg)  
(d)   
Figure 1. (a) Schematic image of fabricated MFM capacitor, (b) P-E curves of 100 MFM capacitor samples. Distribution and Gussaion fitting of (c) P and (d) $E _ { \mathrm { c } }$ variations extracted from the measurements.

To extract the [[FeFET]] parameters and variations, MFM capacitors were fabricated in the following order. The bottom electrode (TiN, 100 nm) was deposited by RF sputtering on a bare Si wafer. Consecutively, [[FeFET]] (Hf0.5Zr0.5O2 (HZO), 7 nm) was deposited using thermal atomic layer deposition (ALD). Following, the top electrode (TiN, 100 nm) was deposited by the same process as the bottom electrode, and then the top electrode patterning, rapid thermal annealing (RTA) was conducted at 700℃ for 30 sec to facilitate o-phase crystallization [Fig. 1(a)].

# B. D2D Variation Modeling

To model the [[FeFET]] parameters and variations in TCAD simulation, the polarization (P)–electric field (E) curves of 100 MFM capacitor samples within the 3000×600 μm2 local area were measured using the positive-up-negativedown (PUND) technique with the Keysight B1500A WGFMU module [Fig. 1(b)]. From the measured $P { - } E$ curves, [[FeFET]] parameters were extracted based on their average values $( P _ { \mathrm { r } } = \stackrel { \cdot } { ( } P _ { \mathrm { r ^ { + } } } { + } P _ { \mathrm { r } } ) / 2$ and $E _ { \mathrm { c } } = ( E _ { \mathrm { c } + } { + } E _ { \mathrm { c } - } ) / 2 )$ . The mean and deviation of $P _ { \mathrm { ~ r ~ } }$ and $E _ { \mathrm { c } }$ were determined through Gaussian fitting, yielding values of μPr = 16.7 μC/cm2, $\sigma _ { \mathrm { P r } } = 0 . 4 3$ , μEc = 2.44 MV/cm, and $\sigma _ { \mathrm { E c } } = 0 . 1 7$ [Figs. 1(c) and (d)].

![](images/0447290222cb1e03e52b8b8c12a1f8be17f69d6c35358ecefee660390bde855d.jpg)  
(a)

![](images/04ad7e1d34f4549ee5d38109106906bc5f4a8f9c7048a049cd6b2fe910f56bf6.jpg)  
(b)   
Figure 2. (a) Schematic of incremental step pulse program/erase method. (b) [ Drain currentG $( I _ { \mathrm { d } } ) \cdot$ -gate voltage $( V _ { \mathrm { g } } )$ curves with varying $V _ { \mathrm { P G M S } } .$ .

![](images/7ca8b847f52a0da7334636a8f28acfb14ee54eec539cb7fc4a99b848704416cc.jpg)  
Figure 3. $G _ { \mathrm { d s } }$ with training scheme (a) $V _ { \mathrm { a d d } } = 0 . 0 6 \mathrm { \ V } , ( \mathbf { b } ) \ V _ { \mathrm { a d d } } = 0 . 0 8 \mathrm { \ V } ,$ (c) $V _ { \mathrm { a d d } } = 0 . 1 0 \mathrm { V } , ( \mathrm { d } ) \ V _ { \mathrm { a d d } } = 0 . 1 2 \mathrm { V }$ and (e) GPOT/GDEP.

# III. TRAINING SCHEME OPTIMIZATION OF [[FeFET]]S

# A. TCAD Simulation Setup

Prior to applying the n $P _ { \mathrm { ~ r ~ } }$ and $E _ { \mathrm { c } }$ variations, the training scheme, namely, the write bias scheme of [[FeFET]], was optimized to ensure the linear $G _ { \mathrm { d s } }$ mapping. The [[FeFET]] simulation was conducted by implementing the measured mean values $( P _ { \mathrm { r } } = 1 6 . 7 ~ \mu \mathrm { C } / \mathrm { c m } ^ { \bar { 2 } }$ and $E _ { \mathrm { c } } = 2$ .44 MV/cm) into the Preisach [[FeFET]] model. The training scheme wasC optimized by adjusting the add voltage $( V _ { \mathrm { a d d } } )$ of incremental step pulse program/erase method [Fig. 2(a)] and the device operation voltage (when the drain current $( \bar { I _ { \mathrm { d } } } ) > 1 0 ^ { - 7 } ~ \mathrm { A / \mu m } ) .$ , namely the read voltage $( V _ { \mathrm { r e a d } } )$ [Fig. 2(b)]. Here, the $V _ { \mathrm { a d d } }$ ranged from 0.06 to 0.12 V and the $V _ { \mathrm { r e a d } }$ ranged from 0.3 to 0.8 V. At each training scheme, 32 cycles of potentiation and depression (P/D) pulses were simulated [Figs. 3(a)-(d)].

# B. Symmetry and Linearity Optimization

To demonstrate symmetry, the $G _ { \mathrm { d s } }$ ranges $( G _ { \mathrm { m a x } } \ - \ G _ { \mathrm { m i n } } )$ during potentiation $( G _ { \mathrm { { P O T } } } = G _ { \mathrm { { m a x } } } \cdot G _ { \mathrm { { m i n } } }$ @ potentiation) and depression $\left( G _ { \mathrm { D E P } } = G _ { \mathrm { m a x } } - G _ { \mathrm { m i n } } \ @ \right.$ depression) were calculated. The GPOT/GDEP plot [Fig. 3(e)] reveals that high symmetry $( \mathrm { i . e . , }$ GPOT/GDEP close to 1) was achieved at $V _ { \mathrm { r e a d } } \geq 0 . 6$ V when $V _ { \mathrm { a d d } } = 0 . 1 0 ~ \mathrm { V }$ , and at $V _ { \mathrm { r e a d } } \geq 0 . 5 ~ \mathrm { V }$ when $V _ { \mathrm { a d d } } = 0 . 1 2 \mathrm { V } .$ . Then, the linearity was evaluated by a non-linearity factor $\left( { \mathfrak { a } } _ { \mathfrak { p } , \mathrm { d } } \right)$ in both P/D circumstances through non-linear fitting [3]. The non-linear fitting of $G _ { \mathrm { d s } }$ mapping with the symmetry was performed as shown in Figs. 4(a) and (b). The highest linearities $( \alpha _ { \mathrm { p } } = 0 . 4 2$ and $\alpha _ { \mathrm { d } } = 0 . 8 4 )$ were observed when $V _ { \mathrm { a d d } }$ $= 0 . 1 0 \mathrm { ~ V ~ }$ and $V _ { \mathrm { r e a d } } = 0 . 7 ~ \mathrm { V }$ , resulting in the most optimized training scheme regarding both symmetry and linearity P/D.

![](images/59b720418387cae0385bcf0e1bff72ef47d07e3b78fd722833f0e74f71ce7a1e.jpg)

![](images/58594a391e16dbcaa0146d725279307e19d1f844b6fc259935301e342194c408.jpg)  
  
Figure 4. Non-linear fitting and non-linearity factor $\alpha _ { \mathrm { p , d } }$ at (a) $V _ { \mathrm { r e a d } } \geq 0 . 6 ~ \mathrm { V }$ when $V _ { \mathrm { a d d } } = 0 . 1 0 \ : \mathrm { V }$ and (b) $\bar { V _ { \mathrm { r e a d } } } \geq 0 . 5 \ : \mathrm { V }$ when $\dot { V } _ { \mathrm { a d d } } = 0 . 1 \dot { 2 } \ : \mathrm { V } .$ (c) $G _ { \mathrm { d s } }$ change w/ D2D variations and (d) enlarged box chart.

# C. Optimization w/ D2D Variation

To reflect the D2D variation of [[FeFET]] HZO into the [[FeFET]] [[Synapse]], the Gaussian distributions modeled Figs. 1(c) and (d) were applied to TCAD simulation with the optimized training scheme $( V _ { \mathrm { a d d } } = 0 . 1 0 ~ \mathrm { V }$ and $V _ { \mathrm { r e a d } } = 0 . 7 ~ \mathrm { V } )$ . Fig. 4(c) illustrates the P/D characteristics with the D2D variations applied, which confirms that the box chart, even with the $P _ { \mathrm { ~ r ~ } }$ and $E _ { \mathrm { c } }$ variations, does not overlap within 16 states (4-bit) [Fig. 4(d)], implying the training accuracy of over 90% [3].P u l s e N u m b e r

# IV. CONCLUSION

In this work, the training scheme of [[FeFET]] was optimized by adjusting the $V _ { \mathrm { a d d } }$ and $V _ { \mathrm { r e a d } }$ for [[On-chip training]] accuracy enhancement. We verified that the optimized training scheme enabled up to 4-bit synaptic operation even in the presence of D2D variations, which were measured from the fabricated MFM capacitors. Accordingly, with the optimized training scheme, [[FeFET]] [[Synapse]] can provide highly reliable and lowpower [[On-chip training]] operations with over 90% accuracy.

# REFERENCES

[1] Sujan K. Gonigondla et al, “A Variation-Tolerant In-Memory Machine Learning Classifer via [[On-chip training]]”, IEEE Journal of Solid-State Circuits, vol. 53, no. 11, pp.3163-3173, November 2018.   
[2] Yunzhe Zheng et al, “Atomic-scale characterization of defects generation during fatigue in [[FeFET]] $\mathrm { H f } _ { 0 . 5 } \mathrm { Z r } _ { 0 . 5 } \mathrm { O }$ 2 films: vacancy generation and lattice dislocation”, IEEE International Electron Devices Meeting (IEDM), San Francisco, CA, USA, pp. 33.5.1-33.5.4, December 2021.   
[3] Matthew Jerry et al, “[[FeFET]] FET Analog [[Synapse]] for Acceleration of Deep Neural Network Training”, IEEE International Electron Devices Meeting (IEDM), San Francisco, CA, USA, pp. 6.2.1- 6.2.4, December 2017.