---
title: "Van der Waals Engineering of One-Transistor-One-Ferroelectric-Memristor Architecture for an Energy-Efficient Neuromorphic Array"
authors:
  - "Yinchang Ma"
  - "Maolin Chen"
  - "Fernando Aguirre"
  - "Yuan Yan"
  - "Sebastian Pazos"
  - "Chen Liu"
  - "Heng Wang"
  - "Tao Yang"
  - "Baoyu Wang"
  - "Cheng Gong"
  - "Kai Liu"
  - "Jefferson Zhe Liu"
  - "Mario Lanza"
  - "Fei Xue"
  - "Xixiang Zhang"
date: "2025-02-03"
year: "2025"
journal: "Nano Letters"
keywords:
  - "[[Van der Waals]]"
  - "[[FeFET]]"
  - "[[Memristor]]"
  - "[[Neuromorphic Array]]"
  - "[[CuCrP2S6]]"
  - "[[1T1M]]"
  - "[[范德华]]"
  - "[[神经形态阵列]]"
abstract: "Two-dimensional-material-based memristor arrays hold promise for data-centric applications such as artificial intelligence and big data. However, accessing individual memristor cells and effectively controlling sneak current paths remain challenging. Here, we propose a van der Waals engineering approach to create one-transistor-one-memristor (1T1M) cells by assembling the emerging two-dimensional ferroelectric CuCrP2S6 with MoS2 and h-BN. The memory cell exhibits high resistance tunability (~10^6), low sneak current (120 fA), and low static power (12 fW). A neuromorphic array with greatly reduced crosstalk is experimentally demonstrated. The nonvolatile resistance switching is driven by electric-field-induced ferroelectric polarization reversal. This van der Waals engineering approach offers a universal solution for creating compact and energy-efficient 2D in-memory computation systems for next-generation artificial neural networks."
abstract_cn: "基于二维材料的忆阻器阵列在人工智能和大数据等以数据为中心的应用中具有广阔前景。然而，访问单个忆阻器单元并有效控制潜行电流路径仍然具有挑战性。本文提出了一种范德华工程方法，通过将新兴二维铁电材料CuCrP2S6与MoS2和h-BN组装，构建了一晶体管一忆阻器（1T1M）单元。该存储单元具有高电阻可调性（~10^6）、低潜行电流（120 fA）和低静态功耗（12 fW）。实验演示了串扰大幅降低的神经形态阵列，非易失性电阻切换由电场诱导的铁电极化反转驱动。该范德华工程方法为下一代人工神经网络创建紧凑且高能效的二维存内计算系统提供了通用解决方案。"
aiSum: "提出基于范德华工程的CuCrP2S6/MoS2/h-BN全二维材料1T1M架构，利用CuCrP2S6的铁电极化反转实现非易失阻变，电阻可调性达10^6，潜行电流低至120 fA，静态功耗仅12 fW。实验验证2×3阵列中串扰降低2个数量级，模拟256×10 ANN在MNIST上达到~90%识别精度。为高能效二维存内计算提供通用方案。"
cite: "[1] Ma et al. Van der Waals Engineering of One-Transistor-One-Ferroelectric-Memristor Architecture for an Energy-Efficient Neuromorphic Array[J]. Nano Letters, 2025."
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
  - "[[Memristor]]"
---

pubs.acs.org/NanoLett

Letter

# Van der Waals Engineering of One-Transistor-One-Ferroelectric-Memristor Architecture for an Energy-Efficient Neuromorphic Array

Yinchang Ma, Maolin Chen, Fernando Aguirre, Yuan Yan, Sebastian Pazos, Chen Liu, Heng Wang, Tao Yang, Baoyu Wang, Cheng Gong, Kai Liu, Jefferson Zhe Liu, Mario Lanza, Fei Xue,* and Xixiang Zhang*

![](images/7ed5474057068103db02a9041d80d45062e98c069733367cec86ac1d60e6831e.jpg)

Cite This: Nano Lett. 2025, 25, 2528−2537

![](images/5a2537e71f5656ff4f7732626ee7229342b4da758c6b22f12179a38c626fe37e.jpg)

Read Online

ACCESS

![](images/ac81655d13b1d6c25dbab7a20081cb25eb8d14a180fca25dd92206378e99d7e6.jpg)

Metrics & More

![](images/45553eecc3f687239b66b681632c090f7b1b7e42eea8cb195ba792398c23c8eb.jpg)

Article Recommendations

![](images/d435de34971c320faa2c26f55330d354baa079d1caec585f29b8acef2d7a5a30.jpg)

Supporting Information

![](images/bf9240d2c95b7dde568badb2c3c2ac5ea3aaf49ea33459a7df81761e297512a9.jpg)

![](images/2d581f46651ff0fd8cf1fc1c64b77cd7f9f989fd1f69cdf3ed4b3b050545be39.jpg)

![](images/381f6b7e79bdcaf490125eea63ef2a1de08bf81455b3fbdecd95d6433bad0ec5.jpg)

ABSTRACT: Two-dimensional-material-based memristor arrays hold promise for data-centric applications such as artificial intelligence and big data. However, accessing individual memristor cells and effectively controlling sneak current paths remain challenging. Here, we propose a van der Waals engineering approach to create [[one-transistor-one-memristor]] (1T1M) cells by assembling the emerging two-dimensional ferroelectric $\mathrm { C u C r P } _ { 2 } S _ { 6 }$ with $\mathbf { M o S } _ { 2 }$ and h-BN. The memory cell exhibits high resistance tunability $\mathsf { \tilde { ( 1 0 ^ { 6 } ) } }$ , low sneak current (120 fA), and low static power (12 fW). A neuromorphic array with greatly reduced crosstalk is experimentally demonstrated. The nonvolatile resistance switching is driven by electric-field-induced ferroelectric polarization reversal. This van der Waals engineering approach offers a universal solution for creating compact and energy-efficient 2D inmemory computation systems for next-generation artificial neural networks.

[[KEYWORDS: 2D ferroelectric crystals]], [[one-transistor-one-memristor]], [[van der Waals assembling]], [[gate-tunable synaptic behaviors]]

n the current era of big data, the emergence of artificial intelligence and machine learning demands high-throughput data storage and processing. Memristors have emerged as promising candidates for high-density integrated memory and neuromorphic computing.1 Recent advancements have enabled artificial neural networks (ANNs) with synapse-like memristor cells, achieving exceptional performance in data storage and computation for data-centric applications.2− 4 Among these technologies, two-dimensional (2D) material-based memristors are gaining attention in the semiconductor industry for their scalability, low power operation, and compatibility with existing technologies.5 Two-dimensional ferroelectric (FE) memory devices are particularly promising.6 These devices exploit polarization and metal/semiconductor interface effects for nonvolatile resistance switching7 and offer ultrafast switching time and ultralow power consumption,8,9 making them ideal for parallel sensing−storing−computing applications.10−13 However, the exploration of ferroelectric-driven device arrays for executing high-volume tasks remains limited.

Building neural networks with memristor arrays faces two major challenges. The first is the leakage current: when the memristor is configured to an “OFF” state, leakage currents still exist due to material imperfections or defects, causing additional static power consumption and impacting the stability of the stored data.14−17 The second is the sneak current path: when reading or writing a specific memristor, the current may pass through other parallel cells, forming a “sneaky” pathway and resulting in considerable read−write errors.16,18 Fortunately, combining memristors with field-effect transistors can help alleviate these issues,19 thereby avoiding crosstalk problems and improving computational effi-

Received: December 3, 2024

Revised: January 21, 2025

Accepted: January 24, 2025

Published: February 3, 2025

![](images/1bfbb08e6cfa6a923a2068dd69598fe6520338e030cd8e276f36793acf21f359.jpg)

![](images/983637f8a293402845ed67669f009d1989afdac0b513f2910081d7ba6ee25de8.jpg)

![](images/b5e214d683f601bf400fbb42c87841c88e8b4af554b0d81b63ad75c0c291b14c.jpg)

![](images/66ddbbc035b8930681807d65f7fd3c74d74276752bf8b8cda514c4c30d7c2455.jpg)

![](images/30f6437664dfc4b27db2a6c4f61578b3d4152c67e93f345c990ed6c6d5aa0ce0.jpg)

![](images/ce0b3131c47abcfd61e7ca337ae91f5d7742450a5524e6f25a64f9ee7af9c774.jpg)

![](images/a2cc3562d83984e9c9b9a8c60905c49a7d2a89b99f72f68dc7cff3509f9f4d81.jpg)

![](images/69dcbb3c5b24d6c7795d423b5527119365999ad515b8404b0692a3677a651529.jpg)  
Figure 1. Characterization of ${ \mathrm { C u C r P } } _ { 2 } S _ { 6 }$ polar properties. (a) Crystal structures of ${ \mathrm { C u C r P } } _ { 2 } S _ { 6 }$ in FE, AFE, and intermediate states indicated by the locations of $\mathrm { C u } ^ { \mathrm { I I } }$ atoms along the c-axis. (b) Electrostatic potential distribution along the c-axis of FE ${ \mathrm { C u C r P } } _ { 2 } S _ { 6 }$ overlaid with its crystal structure. (c) PFM-patterned phase images at room temperature and $2 5 0 ^ { \circ } \mathrm { C } . \left( \mathbf { d } \right)$ Ten continuous cycles of PFM butterfly hysteresis loops observed at room temperature. (e) Temperature-dependent phase hysteresis loops. The phase switching vanishes at temperatures of $2 2 0 ^ { \circ } \mathrm { C }$ or higher. (f) Schematic of optical SHG measurements. (g) Thickness dependence of SHG intensity. Inset: Polar plot of the SHG intensity when the polarization of the linearly polarized laser is swept from 0 to 360°.

ciency. 20−23 $^ { 2 0 - 2 3 } \mathrm { Y e t } ,$ the hybridization of memristors and transistors via all-2D assembly is scarcely studied.

Herein, we demonstrate a novel one-transistor-one-ferroelectric-memristor (1T1M) device24 by assembling ${ \mathrm { C u C r P } } _ { 2 } { \mathrm { S } } _ { 6 } ,$ hexagonal boron nitride (h-BN), and $\mathbf { M o S } _ { 2 } .$ . Different from previous studies,25,26 our 1T1M device exhibits gate-tunable nonvolatile resistance switching due to electric-field-driven FE transition in $\mathrm { C u C r P } _ { 2 } \mathrm { S } _ { 6 } . 1 3 , 2 7 , 2 8$ The 1T1M architecture is entirely composed of 2D van der Waals (vdW) crystals, leveraging their atomic-scale thickness and sharp interfaces. The active memristive material ${ \mathrm { C u C r P } } _ { 2 } { \mathrm { S } } _ { 6 }$ belongs to the emerging family of transition-metal phosphosulfides but has not received considerable attention. The vdW-engineered ${ \mathrm { C u C r P } } _ { 2 } { \mathrm { S } } _ { 6 }$ -based 1T1M exhibits ultralow sneak current $( { \sim } 1 2 0 \ \mathrm { f A } ) _ { \it \Omega }$ , colossal tunability (106 ) of resistance states, and low operation voltages (<1 V). Our 1T1M memory array

suppresses crosstalk by 2 orders of magnitude in experiments and achieves 90% image-recognition accuracy with low energy consumption $( 1 2 . 7 7 \ : \mu \mathrm { \bar { W } } )$ in a simulated $2 5 6 \times 1 0 ~ \mathrm { A N N }$ . This study highlights the potential of 2D FE materials for advanced memory architectures.

As discovered by recent studies,27,29 CuCrP2S6 crystals, despite being antiferroelectric in bulk, exhibit polarization in thin layers under external electric fields through ferroelectric phase transitions. In its structure (Figure 1a), $\mathrm { \dot { C } u ^ { I } }$ atoms are fixed on one side of the monolayer, while $\mathrm { \dot { C } } \mathbf { u } ^ { \mathrm { I I } }$ atoms shift vertically when sufficient energy is acquired from external stimuli, such as vertical electric fields. This shift enables different phases with distinct symmetries. When ${ \mathrm { C u } } ^ { \mathrm { I } }$ and $\mathrm { C u } ^ { \mathrm { I I } }$ are located on the same side, the crystal produces upward or downward polarization at the macroscopic level, i.e., an FE state. Conversely, when CuI and ${ \mathrm { C u } } ^ { \mathrm { I I } }$ appear on opposite sides,

![](images/90f5b45e21ae8508a55b13c97b6f2e69efdf99a5d476859f7c4909e0687c0025.jpg)  
a

![](images/994fbc0801aad7dee785f697df0275e9a81b31c4a9930c6cefdf02883f59cbd7.jpg)  
b

![](images/fb54312c508077f7131b2574cfc2787c4c9476771e9993d370ce09729dbe0bdc.jpg)  
C

![](images/6743d4dc802985f18f85be41544fdd329ee670c993194b3166978638216b736e.jpg)  
d

![](images/2bcdba3ed7988ac98ec0b7839747862ad026f369ae9e9cb7ae24895d7847dbdb.jpg)  
e

![](images/59addfbbaedcf39fcc092867f9f1567eefa0b6b25cf9af8a3b0c236f8420a77d.jpg)  
f

![](images/e949cc7e62721e61edfb19ea83106de3fb54cdbd57860ee6c4e5574e57282478.jpg)  
g

![](images/582886797a86528468081ae108f5122919fa3f5758ebed406960347f1485fba8.jpg)

![](images/503e382d59e0e439c663897c88c804a242cd15fd336c85216f37dc8a0ba911f8.jpg)  
  
Figure 2. Design of the 1T1M architecture and device characterization. (a) Cross-sectional schematic of the 1T1M device structure. The currents were acquired by applying biases onto $V _ { \mathrm { d } }$ and the forward current pathway is marked by arrows. Ti is used for contact. (b) 3D schematic illustration of the device structure. (c) Cross-sectional transmission electron microscope images of 1T and 1M sections. Scale bar: 10 nm. (d) Scanning electron microscope image of the as-fabricated 1T1M device presented in false color. Scale bar: 15 μm. (e) Top-gate-tunable memristor: Hysteretic I−V curves for the 1T1M with $V _ { \mathrm { t g } }$ varied from −3 to 3 V. (f) Top-gate transfer characteristics of the 1T1M device. The nonhysteretic transfer curve shows that the $\mathrm { { } ^ { \mathfrak { \omega } } O N } ^ { \mathfrak { \omega } }$ and ${ } ^ { \omega } \mathrm { O F F } ^ { \mathfrak { n } }$ states of the transistor can enable and disable resistance switching, respectively. $V _ { \mathrm { d } } = 1 ~ \mathrm { V } . ~ ( \mathbf { g } )$ Retention tests after a pulse of $V _ { \mathrm { d } } = \pm 1 ~ \mathrm { V } / 1 0$ s with $V _ { \mathrm { t g } }$ set as 3 V and −3 V. The read voltage is 0.1 V. (h) Potentiation and depression of the device with $V _ { \mathrm { t g } } = 3 \mathrm { V } \left( \mathrm { O N } \right.$ state) and $V _ { \mathrm { t g } } = - 3 \mathrm { ~ V } \left( \mathrm { O F F } \ \mathrm { s t a t e } \right)$ , using pulses of (1 V, 300 ms) for potentiation and (−0.2 V, 300 ms) for depression. Read voltages $V _ { \mathrm { d } } = 0 . 1 ~ \mathrm { V . ~ ( i ) }$ 100-cyle I−V sweeping test.

their dipole moments cancel each other out, resulting in a state with no macroscopic net polarization, i.e., an antiferroelectric (AFE) state. Band structure calculations confirm monolayer ${ \mathrm { C u C r P } } _ { 2 } { \mathrm { S } } _ { 6 }$ as a direct bandgap semiconductor with 1.04 and 1.18 eV for AFE and FE states, respectively (Figure S1). Asymmetric electrostatic potential distribution along the c-axis (Figure 1b) with $\Phi _ { 0 } \ = \ 3 . 1 5$ eV provides evidence of the polarization.

High-quality plate-like ${ \mathrm { C u C r P } } _ { 2 } { \mathrm { S } } _ { 6 }$ crystals were synthesized using the chemical vapor transport method. Scanning electron microscopy shows plate-like crystals with clear $1 2 0 ^ { \circ }$ edges (Figure S2a and b), consistent with their hexagonal structure. Energy-dispersive X-ray spectroscopy confirms the uniform distribution of $\mathrm { { C u , C r , \dot { P } , } }$ and S elements (Figure S2c, top) and validates the stoichiometric composition (Figure S2c, bottom). Raman spectroscopy (Figure S2d, top) identifies phonon modes: peak A at 204 cm−1 (anion rotation), peak B at 266 $\mathrm { c m } ^ { - 1 }$ (anion translation), and peaks C and D (stretching of $[ \mathrm { P } _ { 2 } \mathrm { S } _ { 6 } ] ^ { 4 - } )$ , aligning with previous reports.30

Electric field-induced polarization behaviors were probed using piezoresponse force microscopy (PFM). The box-in-box pattern was written by applying ±10 V DC biases along the out-of-plane direction, showing clear domain reversal (Figure 1c, top). The phase−voltage and amplitude−voltage curves show hysteresis loops and typical “butterfly” shapes, respectively, indicating the existence of out-of-plane polarization (Figure 1d). The multidomain structure disappears at $2 5 0 ~ ^ { \circ } \mathrm { C }$ (Figure 1c, bottom), and the hysteresis of phase loops is pronounced with 180° reversal even up to 160 °C but vanishes at $2 2 0 ~ ^ { \circ } \mathrm { C }$ and above (Figure 1e), both of which indicate polar-to-nonpolar phase transitions.

Second harmonic generation (SHG) probes the noncentrosymmetry, a prerequisite of polarization.31 SHG has advantages over PFM in the aspect of being noncontact, nondestructive, and highly efficient. We utilized SHG measurements as an efficient method to screen CuCrP S flakes across the whole wafer. SHG emission (Figure 1f and g) exhibits a six-petal polar plot, consistent with hexagonal crystal symmetry. The SHG signal increases with the increasing thickness of the sample (Figure 1g), indicating SHG is a bulk property arising from the inherent non-centrosymmetry of the crystal, rather than a surface-induced symmetry breaking phenomenon.

Seamless integration of memory and logic functions in 1T1M configuration requires several considerations to minimize mismatch issues and ensure collaborative operations:32 (1) interference between the transistor and memristor;33 (2) matching of the working current range and operating voltages;34 and (3) contact problems.35 Failing to meet matching conditions may limit the full expression of the memory effect and programmable functions. For example, filamentary memristors often require large forming current to establish conductive paths,6 which many transistors cannot provide; the nonlinear output characteristics caused by the transistor contacts will hinder the realization of linear multilevel resistance states.35 Meanwhile, the stray fields, parasitic capacitance, and defect charging in transistors may bring a negative impact to the high-frequency operation of memristors.36 Among the vast library of materials, we found that the recently discovered ferroelectric ${ \mathrm { C u C r P } } _ { 2 } { \mathrm { S } } _ { 6 } ,$ when integrated with the MoS transistor, has immense potential in addressing these critical challenges. Its unique properties such as low switching energy barrier,37 strong polarization,28,37−39

minimal stray field,29 $\mathrm { { f i e l d } } , ^ { 2 9 }$ and low degradation rate, make it a perfect choice for collaborative operation with $\mathbf { M o S } _ { 2 }$ FETs. Furthermore, the multidomain nature of $\mathrm { C u C r P } _ { 2 } \mathrm { S } _ { 6 } ^ { 4 0 }$ collaborates well with the linear output and high current tolerance of MoS FETs, ensuring the comprehensive exploitation of synaptic properties of memristors.

Our design features a planar-transistor-vertical-memristor cascaded layout, enabling the compact and reliable integration of logic and memory functions with reduced interference. Atomic-thick MoS is used as the transistor channel due to its high mobility for fast switching; h-BN with a wide bandgap serves as both top-gate dielectrics and isolation layers. For the 1T1M configuration, the planar transistor component is assembled by vdW stacking of $\mathbf { M o S } _ { 2 }$ and h-BN, while the ${ \mathrm { C u C r P } } _ { 2 } { \mathrm { S } } _ { 6 }$ flake in the vertical memristor is assembled on top of the electrode $\left( \mathrm { T } _ { 2 } \right)$ via vdW forces. The device schematics are displayed in Figure 2a and b. The fabricated device is shown in the scanning electron microscopy image (Figure 2d). The thicknesses of ${ \bf M o S } _ { 2 } ,$ h-BN, and ${ \mathrm { C u C r P } } _ { 2 } { \mathrm { S } } _ { 6 }$ are 10, 20, and 18 nm, respectively (Figure S3a). The metals for the electrode are Ti (10 nm) and Au (60 nm). The left side of the device, marked by dashed lines and noted as $^ { \omega } 1 \mathrm { T } ^ { \dprime } .$ , serves as a transistor. To mitigate the generation of parasitic capacitance, the gate electrode needs to be patterned in a position that does not overlap with the source $\left( \mathbf { \bar { T } } _ { 2 } \right)$ and drain $\left( \mathrm { T } _ { 1 } \right)$ electrodes. The cross-sectional transmission electron microscope images and energy-dispersive X-ray spectroscopy confirm the layered structure and sharp interfaces (Figures 2c and S4).

Electrical characterization (Figure 2e) shows hysteretic I−V curves in the $\mathrm { ^ { \alpha } O N ^ { \mathrm { { \it { \infty } } } } }$ state $\left( V _ { \mathrm { t g } } = 3 ~ \mathrm { V } \right.$ with a floating back gate). The temperature-dependent memristive behavior is illustrated in Figure S5. The positive $V _ { \mathrm { t g } }$ increases the carrier concentration, allowing current flow between $\mathrm { T } _ { 1 }$ and $\mathrm { T } _ { 2 } .$ This causes a significant potential drop across the memristor, generating an electric field strong enough to induce FE polarization reversal. Conversely, when a negative top-gate voltage $\left( V _ { \mathrm { t g } } = - 3 ~ \mathrm { V } \right)$ is applied, the current sharply decreases and the resistance switching window disappears. The negative $V _ { \mathrm { t g } }$ suppresses channel conductivity, leading to a major potential drop across the channel rather than the memristor, which makes the electric field inadequate to induce or reverse the polarization.

Figure 2f depicts the transfer characteristics of the 1T1M cell at $\bar { V _ { \mathrm { d } } } = 1 ~ \mathrm { V } ,$ which shows a low subthreshold-swing value of around 125 mV/dec. While a maximum ON/OFF ratio up to $1 0 ^ { 6 }$ at $V _ { \mathrm { d } } = 1 ~ \mathrm { V }$ has been achieved by top-gating, the gate leakage current remains below 1 pA. Furthermore, the backgating has a similar effect to the top-gating (Figure S6). This design effectively integrates the functions of the memristor and transistor, leading to a well-functioning 1T1M cell. The good performance of the 1T1M cell can be ascribed to the following features of the device: (a) the relatively small LRS and HRS currents that can be effectively controlled by gating; (b) being free from the electroforming process, ensuring the current stays within the tolerable threshold of the transistor; (c) good ohmic contacts (Figure S7) ensuring a large potential difference across the memristor to trigger resistance switching.

The 1T1M device exhibits synaptic dynamics, including potentiation and depression. In the “ON” state (with positive $V _ { \mathrm { t g } } )$ , the device shows a stepwise conductivity increase with excellent linearity due to ferroelectric domain expansion41,42 (Figure 2h). Using positive voltage pulses, 100 distinguishable resistance states are achieved. Following the depression process

![](images/cd73941414e54a8ce59e46d884b8e05931a20bed39f96961af581298ec095628.jpg)  
a

![](images/05fabbc6a63b68c33ed6ef6a1577568da38ae2b214bb4bb388015db66d291f75.jpg)  
b

![](images/a676a87ce0533feaa44825caf5f880df325e72cee79eb53c5c8302362bf4f256.jpg)  
C

![](images/8797b66b5137d7aa139383a171d43bfb212112aec5e678bcc466edf82b1a79a5.jpg)  
d

![](images/65956530b4e6bd43155b43b4529be72c6acdc67aed1c9093888fa7593416c290.jpg)

![](images/f0b135ac1018ffe1cf7f1a4a99828ebe3be7c1e35efc576521540f06fa60e543.jpg)  
f

![](images/aa77e3a8dc156690d387d08f8514a1da0d37384d6ae04afd9ec978419ac1dccd.jpg)  
g

![](images/84f872b36af0019caa2d0f7eaf68578e113bba34479b206cd981eb6874236390.jpg)  
h   
Figure 3. Working principle and performance merits of our design. (a−f) Energy band diagrams of 1T1M under thermal equilibrium $\left( V _ { \mathrm { d } } = 0 ~ \mathrm { V } \right)$ with different $V _ { \mathrm { t g } } \mathrm { \overline { { \Omega } } }$ dependent Fermi levels and $V _ { \mathrm { d } } .$ -dependent polarization directions. (a,d) and (b,c,e,f) depict devices in their initial states and under operation, respectively. ${ } ^ { \mathrm { 4 } } V _ { \mathrm { d } } = 0 \ \mathrm { V }$ after $1 / { - 1 } \bar { \mathrm { ~ V ~ } } ^ { \dag }$ denotes the operations where $V _ { \mathrm { d } }$ is set to $1 / { - } 1 \mathrm { ~ V ~ }$ to reverse the polarization, followed by resetting $V _ { \mathrm { d } }$ to 0 V. $\bar { ( \mathbf { g } ) }$ Mapping of top-gate and back-gate voltage dependence of the resistance switching ratio and LRS current. (h) Comparison between ${ \mathrm { C u C r P } } _ { 2 } S _ { 6 }$ 1T1M cells and gate-tunable resistance switching devices in previous reports.

under negative voltage pulses, the current decreases to 20 $\mathrm { p A } .$ . With a $V _ { \mathrm { t g } }$ of −3 V, the current is further suppressed to $2 \ \mathrm { p A } ,$ , regardless of whether the device undergoes a depression or potentiation. Gating not only activates/quenches the synaptic function but also modulates synaptic response linearity (Figure S8).

Figure S9 presents other key synaptic characteristics, including excitatory postsynaptic current (EPSC), pairedpulse facilitation (PPF), and spike-timing-dependent plasticity (STDP). The EPSC increased with higher voltage pulses (Figure S9a). Paired-pulse tests show enhanced current response at shorter pulse intervals (Figures S9b and c). STDP tests demonstrate the correlation between the timing of pre- and postsynaptic spikes and the corresponding synaptic weight change (Figure S9d), resembling the temporal learning rules in biological systems. The stability of the device is examined over 60 cycles of potentiation and depression (Figure S10), demonstrating minimal variations.

The retention tests (Figure 2g) show the resistance states can persist for more than 20,000 s after a pulse of $V _ { \mathrm { d } } = \pm 1 ~ \mathrm { V } / $ 10 s. After a fast relaxation process of 1000 ${ \bf s } ,$ the current tends to stabilize, exhibiting nonvolatile LRS and HRS. At $V _ { \mathrm { t g } } = - 3$ ${ \mathrm { V } } ,$ the current is suppressed below 120 fA. This shows $V _ { \mathrm { t g } }$ provides complete ON−OFF switching for the memristor with the gate tunability of $1 0 ^ { 4 }$ for LRS and $\overline { { 1 0 ^ { 3 } } }$ for HRS. The static power consumption of the standby cell $( P _ { \mathrm { s t a t i c } } = I _ { \mathrm { O F F } } \times V _ { \mathrm { R e a d } } ,$ where $I _ { \mathrm { O F F } }$ is leakage current in the “OFF” state, $V _ { \mathrm { R e a d } }$ is the

read voltage14,17) is as low as 12 fW, nearly three orders lower than the 1M configuration (300 pW). Cycling I−V tests demonstrate endurance over 100 consecutive cycles with small cycle-to-cycle variability (Figure 2i). Figure S11 shows stable resistance switching over 3000 cycles.

The band diagrams for understanding the working principles of the 1T1M memory cell are presented in Figure 3. In the initial state (Figure 3a and d), the intrinsic dipoles inside the ${ \mathrm { C u C r P } } _ { 2 } { \mathrm { S } } _ { 6 }$ exhibit macroscopically antiparallel alignment, i.e., the AFE state. The resistance state of the device is solely dependent on the gate voltages. Figure 3b,c,e,f depict scenarios where the 1T and 1M are working in coordination. With a positive $V _ { \mathrm { t g } } ,$ the history of applied $V _ { \mathrm { d } }$ determines the polarization direction, modulating the potential barrier and defining the HRS or LRS state. Applying a negative $V _ { \mathrm { t g } }$ lowers the Fermi level, disabling the device and setting it to the “OFF” state. These band diagrams effectively explain the observed experimental results.

A broader modulation range can be achieved through the collaborative utilization of the back gate and top gate. A positive back-gate voltage $( V _ { \mathrm { b g } } )$ combined with manipulations of $V _ { \mathrm { t g } }$ can yield a larger resistance switching ratio (Figure 3g, left). Meanwhile, a negative $V _ { \mathrm { b g } }$ in combination with a varying $V _ { \mathrm { t g } }$ can further suppress the sneak current (Figure 3g, right). With the application of a slightly negative $V _ { \mathrm { t g } } \ ( { \bf e . g . } , - 1 \ \mathrm { V } ) .$ , smoother modulations can be achieved by the back-gating.

![](images/9fd609b7a106e2a17cd9ace7f492c15a2990bfabdb098401b34871f6af761d3c.jpg)  
a   
b

![](images/6f2a8768a35350c0be51d8c606201a04cb8a4358eeadc43c798f2f1f553078e4.jpg)

![](images/3354276cf8e0016ef32c9d91a01fb68ef1ff7c4c823104fd0f9e748c7dec0a6c.jpg)  
C

![](images/e995e9ed82455d2879a1c10b35e067034e6b83804517fb9eb752d62a405a4f3d.jpg)  
d

![](images/475eb140f5ec016d954ce87484047ce84c33805ebbf14b5cb46259e0b7b26646.jpg)  
e

![](images/0ee45ffa628dbdc692b604ad21bb17c7f57f6fd2eab2a66bddfc722694c9dfa8.jpg)  
f

![](images/e41f4cc97be943776db5b6793d6c0a6b059d55bb92fe5376d605bc430a7a4a48.jpg)  
g

![](images/bddc96614a21cb79fe7574b38e454cea5192be7258cf056f01eb4cfcb9566718.jpg)  
h   
Figure 4. Experimental demonstration of a neuromorphic array with no obvious crosstalk. (a) Conceptual schematic of the 1T1M array. Inset: the 2 × 3 miniarray corresponding to the actual fabricated array shown in (b). (b) False-colored scanning electron microscope image of the miniarray schematically shown in the inset of (a). Scale bar: 5 μm. (c) Hysteresis I−V curves for all cells in the 2 × 3 array. (d) Potentiation and depression curves for all cells in the array. (e) Bar plot of individual cell currents for HRS, LRS (both read at 0.1 V), and maximum value during switching (read at 1 V), extracted from (c). (f) Conductance of each cell in the 1T1M array when $V _ { \mathrm { G \mathrm { - } O F F } } = - 3$ V was applied on the second column. Conductance values (read at 0.1 V) are represented by the color filling the circles (nodes). (g) Conductance of cells in a 1M (without 1T) array compared to the 1T1M array in (f). The absence of 1T causes undesired sneak paths. (h) Comparison of individual cell conductance between the 1T1M array (with reduced crosstalk issues) and the 1M array (suffering crosstalk issues). The conductance measured after the occurrence of crosstalk is noted as “2nd read”.

This dual-gating design provides a higher degree of freedom in reconfiguring memristors.

Our 1T1M device potentially addresses the sneak current issue, an unsolved problem in many memtransistor-based designs. While previous reports have achieved gate-tunable resistance switching behaviors in memtransistors,43−46 few studies concurrently achieve several desirable features�lowvoltage drive, sneak current suppression, and complete quenching of the resistance switching behavior�all within a single unit.21,47 Figure 3h demonstrates these features in our 1T1M. Compared to multiterminal memtransistors based on

vdW materials like $\mathrm { W S e } _ { 2 } , \quad \mathrm { S n O } _ { 2 } , ^ { 4 8 }$ and polycrystalline $\mathrm { M o S } _ { 2 } , ^ { 4 4 , 4 9 }$ our device is operational at smaller gate voltage with significantly reduced sneak current. These substantial improvements mitigate the power consumption challenges for scaled-down applications.

The developed 1T1M architecture is used to construct neuromorphic arrays (Figure 4a). In this design, the bit line (BL) and source line (SL) are connected to the two terminals $( \mathrm { T } _ { 1 }$ and $\mathrm { T } _ { 3 } ,$ respectively) of the 1T1M memory cell for read and write operations, whereas the word line (WL) is connected to the gate and is used for targeting specific memristors (Figure

![](images/cea6dbaf84f6b22cf044b729a575cbe933932d03da9781bcc9848f7539a9b0d1.jpg)

![](images/dc2a5fb4b27f6afcb9b118794e802803c964b7ecf296190cd72a3b93703c252d.jpg)

![](images/1d6114ed5e526dfa05e8690b046326999d8bb1076fb5f5cff7a97821fd3239d2.jpg)

![](images/9c6195b7934b5e31218ce95a93418473dc460af4b9bf6d3bcd08456ddf31eeb2.jpg)  
Figure 5. Construction of artificial neural networks. (a) Simplified equivalent circuit schematic for 1T1M array-based neural networks. The array is partitioned into left and right sectors, assigned to process positive and negative synaptic weights, respectively. (b) Simulated accuracy rate as a function of line resistance for different sizes of neural networks. (c) Simulated power consumption as a function of line resistance. (d) Confusion matrix of MNIST recognition performance. The rows in the matrix denote the labels of input patterns, the columns represent the output recognition results, and the depth of color represents the recognition accuracy.

4b). The thicknesses of the materials are listed in Figure S3b. Low cell-to-cell variability is observed in I−V curves and synaptic features (Figure 4c,d,e). The devices 1−1, 1−2, and 1−3 are made from the same flake, while the devices 2−1, 2− 2, and 2−3 are fabricated from another. The 1T1M configuration efficiently eliminates the undesired sneak paths (Figure 4f and 4g) (the in-plane conductivity of ${ \mathrm { C u C r P } } _ { 2 } { \mathrm { S } } _ { 6 }$ is negligible). $V _ { \mathrm { G - O F F } }$ suppresses conductance in unselected devices (∼1 pS, Figure 4f), significantly reducing sneak current compared to uncontrolled “leaking” states (1 to 100 nS) in arrays without the 1T section (Figure 4g). The sneak current disturbs cell conductance during “writing” operations on adjacent cells, causing crosstalk-induced data loss. Crosstalk impact was analyzed by measuring the cell conductance before and after “write” operations on adjacent cells. For the 1M array (Figure S12), huge conductance discrepancies are observed. In contrast, 1T1M arrays show mitigated fluctuations as the unselected cells are effectively isolated by gating $\left( V _ { \mathrm { G \mathrm { - } O F F } } = - 3 \right.$ V). The comparative assessment (Figure 4h) shows conductance variability (defined as $\Delta G = \left( G _ { 1 } - G _ { 0 } \right) / G _ { 0 } ,$ where $G _ { 0 }$ and $G _ { 1 }$ are conductance before and after crosstalk, respectively) reduced from 800% in 1M arrays to 3% in 1T1M arrays. This demonstrates the important role of the 1T1M design in mitigating crosstalk and enhancing the array performance.

To justify the advantage of this work, Table S1 compares various types of sneak-controlling 2D devices with different

assembly approaches, including one-transistor-four-resistor (1T4R),50 one-selector-one-resistor (1S1R),51 one-diode-oneselector (1D1S),52 and self-selective memtransistor.49 These devices are based on different resistance switching mechanisms (charge trapping,53 filament,54 etc.). These devices demonstrate multiple strategies for cell selection in an array. Unlike others, our work uniquely integrates ferroelectric mechanisms with all-vdW engineering. While semiconductor transistors are known to have low off-state current,55,56 the collaborative operation of vdW-engineered transistors and memristors remains a promising area for achieving scalable memory systems. Figure S13 shows current progress toward lower gate voltages and reduced sneak currents. Future research will focus on the scalable material growth and its monolithic integration.57,58

Circuit-level simulations were performed with SPICE simulators for ${ \mathrm { C u C r P } } _ { 2 } { \mathrm { S } } _ { 6 }$ 1T1M crossbar arrays based on experimentally measured I−V characteristics and weight updates. The arrays came in three different sizes (64 × 10, 128 × 10, and 256 × 10) and were implemented in single-layer perceptron (SLP) neural networks to perform handwritten digit recognition using the MNIST training data set (Figure 5a). The recognition accuracy remains high (∼90%) across all array sizes when the line resistance varies between 1 and 100 Ω (Figure 5b). There is a trade-off between pattern recognition accuracy and energy efficiency. Power consumption decreases dramatically as the line resistance exceeds 1 Ω (Figure 5c) due

to its effect on the total current. By optimizing the layout of 1T1M memory units in large-scale arrays, power efficiency can be improved without major accuracy loss. Based on 64 × 10 arrays and 1 Ω resistance, the recognition performance for each input class is shown in the confusion matrix (Figure 5d).

In summary, we used vdW engineering to develop a novel all-2D-material-based 1T1M architecture using $\bar { \mathrm { C u C r P } _ { 2 } S _ { 6 } }$ ferroelectric polarization, achieving high resistance tunability (106 ), ultralow minimum sneak current (120 fA), and an ultralow static power (12 fW). This work presents significant progress in all-2D 1T1M arrays with precise cell access and over 2 orders of magnitude suppression in conductance variations. This 1T1M configuration offers universal strategies for energy-efficient and precision-oriented neural networks.

# ASSOCIATED CONTENT

# Data Availability Statement

All data are presented in the main text or Supporting Information.

# *sı Supporting Information

The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.nanolett.4c06118.

Calculated band structures; scanning electron microscope images and energy-dispersive X-ray spectroscopy mapping images; temperature dependence of resistance switching; gate-tunable synaptic behavior tests; EPSC, PPD/PPF, and STDP tests; endurance test; comparison with various multiterminal memory devices; experimental methods (PDF)

# AUTHOR INFORMATION

# Corresponding Authors

Fei Xue − Center for Quantum Matter, School of Physics, Zhejiang University, Hangzhou 311215, China; ZJU-Hangzhou Global Scientific and Technological Innovation Center, Zhejiang University, Hangzhou 311215, China; Email: xuef@zju.edu.cn   
Xixiang Zhang − Physical Science and Engineering Division, King Abdullah University of Science and Technology, Thuwal 23955-6900, Saudi Arabia; orcid.org/0000-0002-3478- 6414; Email: xixiang.zhang@kaust.edu.sa

# Authors

Yinchang Ma − Physical Science and Engineering Division, King Abdullah University of Science and Technology, Thuwal 23955-6900, Saudi Arabia; orcid.org/0000-0002-5201- 6448   
Maolin Chen − Physical Science and Engineering Division, King Abdullah University of Science and Technology, Thuwal 23955-6900, Saudi Arabia   
Fernando Aguirre − Intrinsic Semiconductor Technologies, Ltd., Buckinghamshire HP18 9SU, United Kingdom   
Yuan Yan − Department of Mechanical Engineering, The University of Melbourne, Parkville, VIC 3010, Australia   
Sebastian Pazos − Physical Science and Engineering Division, King Abdullah University of Science and Technology, Thuwal 23955-6900, Saudi Arabia   
Chen Liu − Physical Science and Engineering Division, King Abdullah University of Science and Technology, Thuwal 23955-6900, Saudi Arabia

Heng Wang − Electrical and Computer Engineering, King Abdullah University of Science and Technology, Thuwal 23955-6900, Saudi Arabia   
Tao Yang − Physical Science and Engineering Division, King Abdullah University of Science and Technology, Thuwal 23955-6900, Saudi Arabia   
Baoyu Wang − ZJU-Hangzhou Global Scientific and Technological Innovation Center, Zhejiang University, Hangzhou 311215, China   
Cheng Gong − Department of Electrical and Computer Engineering and Quantum Technology Center, University of Maryland, College Park, Maryland 20742, United States; orcid.org/0000-0001-7714-6380   
Kai Liu − Physics Department, Georgetown University, Washington, D.C. 20057, United States; orcid.org/0000- 0001-9413-6782   
Jefferson Zhe Liu − Department of Mechanical Engineering, The University of Melbourne, Parkville, VIC 3010, Australia; orcid.org/0000-0002-5282-7945   
Mario Lanza − Department of Materials Science and Engineering, National University of Singapore, Singapore 117575, Singapore; Singapore Institute for Functional Intelligent Materials, National University of Singapore, Singapore 117544, Singapore

Complete contact information is available at: https://pubs.acs.org/10.1021/acs.nanolett.4c06118

# Notes

The authors declare no competing financial interest.

# ACKNOWLEDGMENTS

This work was supported by King Abdullah University of Science and Technology (KAUST) Office of Sponsored Research (OSR) under Award Nos. ORA-CRG10-2021-4665 and ORA-CRG11-2022-5031. F.X. acknowledges the Zhejiang Provincial Natural Science Foundation of China (grant no. LDT23F04013F04) and the startup funding (02170000- K02013012) of the ZJU-Hangzhou Global Scientific and Technological Innovation Center. This research was undertaken with the resources from the Supercomputing Laboratory at KAUST and the National Computational Infrastructure (NCI) in Australia.

# REFERENCES

(1) Xia, Q.; Robinett, W.; Cumbie, M. W.; Banerjee, N.; Cardinali, T. J.; Yang, J. J.; Wu, W.; Li, X.; Tong, W. M.; Strukov, D. B.; Snider, G. S. Memristor−CMOS hybrid integrated circuits for reconfigurable logic. Nano Lett. 2009, 9, 3640−3645.   
(2) Prezioso, M.; Merrikh-Bayat, F.; Hoskins, B. D.; Adam, G. C.; Likharev, K. K.; Strukov, D. B. Training and operation of an integrated neuromorphic network based on metal-oxide memristors. Nature 2015, 521, 61−64.   
(3) Li, C.; Hu, M.; Li, Y.; Jiang, H.; Ge, N.; Montgomery, E.; Zhang, J.; Song, W.; Dávila, N.; Graves, C. E.; Li, Z.; Strachan, J. P.; Lin, P.; Wang, Z.; Barnell, M.; Wu, Q.; Williams, R. S.; Yang, J. J.; Xia, Q. Analogue signal and image processing with large memristor crossbars. Nat. Electron. 2018, 1, 52−59.   
(4) Sheridan, P. M.; Cai, F.; Du, C.; Ma, W.; Zhang, Z.; Lu, W. D. Sparse coding with memristor networks. Nat. Nanotechnol. 2017, 12, 784−789.   
(5) Sun, L.; Wang, W.; Yang, H. Recent progress in synaptic devices based on 2D materials. Adv. Intell. Syst. 2020, 2, 1900167.   
(6) Ge, R.; Wu, X.; Liang, L.; Hus, S. M.; Gu, Y.; Okogbue, E.; Chou, H.; Shi, J.; Zhang, Y.; Banerjee, S. K.; Jung, Y.; Lee, J. C.;

Akinwande, D. A library of atomically thin 2D materials featuring the conductive-point resistive switching phenomenon. Adv. Mater. 2021, 33, No. e2007792.   
(7) Wang, S.; Liu, L.; Gan, L.; Chen, H.; Hou, X.; Ding, Y.; Ma, S.; Zhang, D. W.; Zhou, P. Two-dimensional ferroelectric channel transistors integrating ultra-fast memory and neural computing. Nat. Commun. 2021, 12, 53.   
(8) He, X.; Ma, Y.; Zhang, C.; Fu, A.; Hu, W.; Xu, Y.; Yu, B.; Liu, K.; Wang, H.; Zhang, X.; Xue, F. Proton-mediated reversible switching of metastable ferroelectric phases with low operation voltages. Sci. Adv. 2023, 9, No. eadg4561.   
(9) Choi, S.; Choi, J.-W.; Kim, J. C.; Jeong, H. Y.; Shin, J.; Jang, S.; Ham, S.; Kim, N. D.; Wang, G. Energy-efficient three-terminal SiOx memristor crossbar array enabled by vertical Si/graphene heterojunction barristor. Nano Energy 2021, 84, 105947.   
(10) Kim, D. J.; Lu, H.; Ryu, S.; Bark, C. W.; Eom, C. B.; Tsymbal, E. Y.; Gruverman, A. Ferroelectric tunnel memristor. Nano Lett. 2012, 12, 5697−5702.   
(11) Chaudhary, P.; Lu, H.; Lipatov, A.; Ahmadi, Z.; McConville, J. P. V.; Sokolov, A.; Shield, J. E.; Sinitskii, A.; Gregg, J. M.; Gruverman, A. Low-voltage domain-wall LiNbO memristors. Nano Lett. 2020, 20, 5873−5878.   
(12) Xue, F.; He, X.; Ma, Y.; Zheng, D.; Zhang, C.; Li, L.-J.; He, J.- H.; Yu, B.; Zhang, X. Unraveling the origin of ferroelectric resistance switching through the interfacial engineering of layered ferroelectricmetal junctions. Nat. Commun. 2021, 12, 7291.   
(13) Xue, F.; Ma, Y.; Wang, H.; Luo, L.; Xu, Y.; Anthopoulos, T. D.; Lanza, M.; Yu, B.; Zhang, X. Two-dimensional ferroelectricity and antiferroelectricity for next-generation computing paradigms. Matter 2022, 5, 1999−2014.   
(14) Ahmed, T.; Kuriakose, S.; Tawfik, S. A.; Mayes, E. L. H.; Mazumder, A.; Balendhran, S.; Spencer, M. J. S.; Akinwande, D.; Bhaskaran, M.; Sriram, S.; Walia, S. Mixed ionic-electronic charge transport in layered black-phosphorus for low-power memory. Adv. Funct. Mater. 2022, 32, 2107068.   
(15) Zidan, M. A.; Fahmy, H. A. H.; Hussain, M. M.; Salama, K. N. Memristor-based memory: The sneak paths problem and solutions. Microelectron. J. 2013, 44, 176−183.   
(16) Sun, L.; Zhang, Y.; Han, G.; Hwang, G.; Jiang, J.; Joo, B.; Watanabe, K.; Taniguchi, T.; Kim, Y. M.; Yu, W. J.; Kong, B. S.; Zhao, R.; Yang, H. Self-selective van der Waals heterostructures for large scale memory array. Nat. Commun. 2019, 10, 3161.   
(17) Feng, X.; Li, Y.; Wang, L.; Chen, S.; Yu, Z. G.; Tan, W. C.; Macadam, N.; Hu, G.; Huang, L.; Chen, L.; Gong, X.; Chi, D.; Hasan, T.; Thean, A. V. Y.; Zhang, Y. W.; Ang, K. W. A fully printed flexible MoS2 memristive artificial synapse with femtojoule switching energy. Adv. Electron. Mater. 2019, 5, 1900740.   
(18) Yang, R.; Li, H.; Smithe, K. K. H.; Kim, T. R.; Okabe, K.; Pop, E.; Fan, J. A.; Wong, H. S. P. Ternary content-addressable memory with MoS transistors for massively parallel data search. Nat. Electron. 2019, 2, 108−114.   
(19) Zhu, K.; Pazos, S.; Aguirre, F.; Shen, Y.; Yuan, Y.; Zheng, W.; Alharbi, O.; Villena, M. A.; Fang, B.; Li, X.; Milozzi, A.; Farronato, M.; Munoz-Rojo, M.; Wang, T.; Li, R.; Fariborzi, H.; Roldan, J. B.; Benstetter, G.; Zhang, X.; Alshareef, H. N.; Grasser, T.; Wu, H.; Ielmini, D.; Lanza, M. Hybrid 2D-CMOS microchips for memristive applications. Nature 2023, 618, 57−62.   
(20) Ding, G.; Yang, B.; Chen, R. S.; Mo, W. A.; Zhou, K.; Liu, Y.; Shang, G.; Zhai, Y.; Han, S. T.; Zhou, Y. Reconfigurable 2D WSe - based memtransistor for mimicking homosynaptic and heterosynaptic plasticity. Small 2021, 17, No. e2103175.   
(21) Nam, J. H.; Oh, S.; Jang, H. Y.; Kwon, O.; Park, H.; Park, W.; Kwon, J. D.; Kim, Y.; Cho, B. Low power MoS2/Nb2O5 Memtransistor device with highly reliable heterosynaptic plasticity. Adv. Funct. Mater. 2021, 31, 2104174.   
(22) Sivan, M.; Li, Y.; Veluri, H.; Zhao, Y.; Tang, B.; Wang, X.; Zamburg, E.; Leong, J. F.; Niu, J. X.; Chand, U.; Thean, A. V. All WSe 1T1R resistive RAM cell for future monolithic 3D embedded memory integration. Nat. Commun. 2019, 10, 5201.

(23) Won, U. Y.; An Vu, Q.; Park, S. B.; Park, M. H.; Dam Do, V.; Park, H. J.; Yang, H.; Lee, Y. H.; Yu, W. J. Multi-neuron connection using multi-terminal floating-gate memristor for unsupervised learning. Nat. Commun. 2023, 14, 3070.   
(24) Rao, M.; Tang, H.; Wu, J.; Song, W.; Zhang, M.; Yin, W.; Zhuo, Y.; Kiani, F.; Chen, B.; Jiang, X.; Liu, H.; Chen, H. Y.; Midya, R.; Ye, F.; Jiang, H.; Wang, Z.; Wu, M.; Hu, M.; Wang, H.; Xia, Q.; Ge, N.; Li, J.; Yang, J. J. Thousands of conductance levels in memristors integrated on CMOS. Nature 2023, 615, 823−829.   
(25) Upadhyay, N. K.; Sun, W.; Lin, P.; Joshi, S.; Midya, R.; Zhang, X.; Wang, Z.; Jiang, H.; Yoon, J. H.; Rao, M.; Chi, M.; Xia, Q.; Yang, J. J. A Memristor with low switching current and voltage for 1S1R integration and array operation. Adv. Electron. Mater. 2020, 6, 1901411.   
(26) Zhou, Y. X.; Li, Y.; Duan, N.; Wang, Z. R.; Lu, K.; Jin, M. M.; Cheng, L.; Hu, S. Y.; Chang, T. C.; Sun, H. J.; Xue, K. H.; Miao, X. S. Boolean and sequential logic in a one-memristor-one-resistor (1M1R) structure for in-memory computing. Adv. Electron. Mater. 2018, 4, 1800229.   
(27) Lai, Y.; Song, Z.; Wan, Y.; Xue, M.; Wang, C.; Ye, Y.; Dai, L.; Zhang, Z.; Yang, W.; Du, H.; Yang, J. Two-dimensional ferromagnetism and driven ferroelectricity in van der Waals CuCrP S . Nanoscale 2019, 11, 5163−5170.   
(28) Ma, Y.; Yan, Y.; Luo, L.; Pazos, S.; Zhang, C.; Lv, X.; Chen, M.; Liu, C.; Wang, Y.; Chen, A.; Li, Y.; Zheng, D.; Lin, R.; Algaidi, H.; Sun, M.; Liu, J. Z.; Tu, S.; Alshareef, H. N.; Gong, C.; Lanza, M.; Xue, F.; Zhang, X. High-performance van der Waals antiferroelectric CuCrP S -based memristors. Nat. Commun. 2023, 14, 7891.   
(29) Hu, Q.; Huang, Y.; Wang, Y.; Ding, S.; Zhang, M.; Hua, C.; Li, L.; Xu, X.; Yang, J.; Yuan, S.; Watanabe, K.; Taniguchi, T.; Lu, Y.; Jin, C.; Wang, D.; Zheng, Y. Ferrielectricity controlled widely-tunable magnetoelectric coupling in van der Waals multiferroics. Nat. Commun. 2024, 15, 3029.   
(30) Susner, M. A.; Rao, R.; Pelton, A. T.; McLeod, M. V.; Maruyama, B. Temperature-dependent Raman scattering and x-ray diffraction study of phase transitions in layered multiferroic CuCrP S . Phys. Rev. Mater. 2020, 4, 104003.   
(31) Chen, B.; Gauquelin, N.; Strkalj, N.; Huang, S.; Halisdemir, U.; Nguyen, M. D.; Jannis, D.; Sarott, M. F.; Eltes, F.; Abel, S.; Spreitzer, M.; Fiebig, M.; Trassin, M.; Fompeyrine, J.; Verbeeck, J.; Huijben, M.; Rijnders, G.; Koster, G. Signatures of enhanced out-of-plane polarization in asymmetric BaTiO superlattices integrated on silicon. Nat. Commun. 2022, 13, 265.   
(32) Sivan, M.; Leong, J. F.; Ghosh, J.; Tang, B.; Pan, J.; Zamburg, E.; Thean, A. V. Physical insights into vacancy-based memtransistors: toward power efficiency, reliable operation, and scalability. ACS Nano 2022, 16, 14308−14322.   
(33) Shi, L.; Zheng, G.; Tian, B.; Dkhil, B.; Duan, C. Research progress on solutions to the sneak path issue in memristor crossbar arrays. Nanoscale Adv. 2020, 2, 1811−1827.   
(34) Yan, X.; Qian, J. H.; Sangwan, V. K.; Hersam, M. C. Progress and challenges for memtransistors in neuromorphic circuits and systems. Adv. Mater. 2022, 34, No. e2108025.   
(35) Liu, B.; Lyu, F.; Tang, B.; Li, X.; Liao, J.; Chen, Q. Contact properties of two-dimensional ferroelectric α-In2Se3. ACS Appl. Electron. Mater. 2021, 3, 4604−4610.   
(36) Teja Nibhanupudi, S. S.; Roy, A.; Veksler, D.; Coupin, M.; Matthews, K. C.; Disiena, M.; Ansh; Singh, J. V.; Gearba-Dolocan, I. R.; Warner, J.; Kulkarni, J. P.; Bersuker, G.; Banerjee, S. K. Ultra-fast switching memristors based on two-dimensional materials. Nat. Commun. 2024, 15, 2334.   
(37) Yu, G.; Pan, A.; Chen, M. Interface engineering of ferroelectricity in thin films of thiophosphate ABP2X6 (A = Cu, Ag; B = In, Bi, Cr, V; X = S, Se). Phys. Rev. B 104, (2021). DOI: 10.1103/ PhysRevB.104.224102   
(38) Aoki, S.; Dong, Y.; Wang, Z.; Huang, X. S. W.; Itahashi, Y. M.; Ogawa, N.; Ideue, T.; Iwasa, Y. Giant modulation of the second harmonic generation by magnetoelectricity in two-dimensional multiferroic CuCrP S . Adv. Mater. 2024, 36, No. e2312781.

(39) Hong, M.; Dai, L.; Hu, H.; Li, C. Structural, ferroelectric, and electronic transitions in the van der Waals multiferroic material CuCrP S under high temperature and high pressure. Phys. Rev. B 2024, 110, 144103.   
(40) Ma, R. R.; Xu, D. D.; Zhong, Q. L.; Zhong, C. R.; Huang, R.; Xiang, P. H.; Zhong, N.; Duan, C. G. Nanoscale mapping of Cu-ion transport in van der Waals layered CuCrP S . Adv. Mater. Interfaces 9, (2022). DOI: 10.1002/admi.202101769   
(41) Kim, D.; Jeon, Y. R.; Ku, B.; Chung, C.; Kim, T. H.; Yang, S.; Won, U.; Jeong, T.; Choi, C. Analog synaptic transistor with Al-doped HfO2 ferroelectric thin film. ACS Appl. Mater. Interfaces 2021, 13, 52743.   
(42) Boyn, S.; Grollier, J.; Lecerf, G.; Xu, B.; Locatelli, N.; Fusil, S.; Girod, S.; Carretero, C.; Garcia, K.; Xavier, S.; Tomas, J.; Bellaiche, L.; Bibes, M.; Barthelemy, A.; Saighi, S.; Garcia, V. Learning through ferroelectric domain dynamics in solid-state synapses. Nat. Commun. 2017, 8, 14736.   
(43) Li, W.; Guo, Y.; Luo, Z.; Wu, S.; Han, B.; Hu, W.; You, L.; Watanabe, K.; Taniguchi, T.; Alava, T.; et al. A gate programmable van der Waals metal-ferroelectric-semiconductor vertical heterojunction memory. Adv. Mater. 2023, 35, 2208266.   
(44) Sangwan, V. K.; Lee, H. S.; Bergeron, H.; Balla, I.; Beck, M. E.; Chen, K. S.; Hersam, M. C. Multi-terminal memtransistors from polycrystalline monolayer molybdenum disulfide. Nature 2018, 554, 500−504.   
(45) Zhai, Y.; Xie, P.; Hu, J.; Chen, X.; Feng, Z.; Lv, Z.; Ding, G.; Zhou, K.; Zhou, Y.; Han, S.-T. Reconfigurable 2D-ferroelectric platform for neuromorphic computing. Appl. Phys. Rev. 2023, 10, 011408.   
(46) Xue, F.; He, X.; Retamal, J. R. D.; Han, A.; Zhang, J.; Liu, Z.; Huang, J. K.; Hu, W.; Tung, V.; He, J. H.; Li, L. J.; Zhang, X. Gatetunable and multidirection-switchable memristive phenomena in a van der Waals ferroelectric. Adv. Mater. 2019, 31, No. e1901300.   
(47) Jadwiszczak, J.; Keane, D.; Maguire, P.; Cullen, C. P.; Zhou, Y.; Song, H.; Downing, C.; Fox, D.; McEvoy, N.; Zhu, R.; Xu, J.; Duesberg, G. S.; Liao, Z. M.; Boland, J. J.; Zhang, H. MoS2 memtransistors fabricated by localized helium ion beam irradiation. ACS Nano 2019, 13, 14262−14273.   
(48) Huang, C. H.; Chang, H.; Yang, T. Y.; Wang, Y. C.; Chueh, Y. L.; Nomura, K. Artificial synapse based on a 2D-SnO memtransistor with dynamically tunable analog switching for neuromorphic computing. ACS Appl. Mater. Interfaces 2021, 13, 52822−52832.   
(49) Feng, X.; Li, S.; Wong, S. L.; Tong, S.; Chen, L.; Zhang, P.; Wang, L.; Fong, X.; Chi, D.; Ang, K. W. Self-selective multi-terminal memtransistor crossbar array for in-memory computing. ACS Nano 2021, 15, 1764−1774.   
(50) Xie, M.; Jia, Y.; Nie, C.; Liu, Z.; Tang, A.; Fan, S.; Liang, X.; Jiang, L.; He, Z.; Yang, R. Monolithic 3D integration of 2D transistors and vertical RRAMs in 1T-4R structure for high-density memory. Nat. Commun. 2023, 14, 5952.   
(51) Shen, M.; Shen, S.; Jia, Y.; Liu, Y.; Zhang, P.; Xie, M.; Wei, J.; Yang, R. One-selector-one-resistor integrated memory cells based on two-dimensional heterojunction memory selectors. ACS Nano 2024, 18, 28292−28300.   
(52) Wang, X.; Qiao, R.; Lu, H.; He, W.; Liu, Y.; Zhou, T.; Wan, D.; Wang, Q.; Liu, Y.; Guo, W. 2D memory selectors with giant nonlinearity enabled by van der Waals heterostructures. Small 2024, 20, No. e2310158.   
(53) Fu, S.; Park, J. H.; Gao, H.; Zhang, T.; Ji, X.; Fu, T.; Sun, L.; Kong, J.; Yao, J. Two-terminal MoS memristor and the homogeneous integration with a MoS transistor for neural networks. Nano Lett. 2023, 23, 5869−5876.   
(54) Kim, K. T.; Kim, T.; Jeong, Y.; Park, S.; Kim, J.; Cho, H.; Cha, S. K.; Kim, Y. S.; Bae, H.; Yi, Y.; Im, S. Self-assembled TaO /2H-TaS as a van der Waals platform of a multilevel memristor circuit integrated with a beta- ${ \bf \cdot G a } _ { 2 } { \bf O } _ { 3 }$ transistor. ACS Nano 2023, 17, 3666− 3675.   
(55) Huang, W. C.; Zheng, H. X.; Chen, P. H.; Chang, T. C.; Tan, Y. F.; Lin, S. K.; Zhang, Y. C.; Jin, F. Y.; Wu, C. W.; Yeh, Y. H.; Chou, S.

Y.; Huang, H. C.; Chen, Y. W.; Sze, S. M. Incorporation of resistive random access memory into low-temperature polysilicon transistor with fin-like structure as 1T1R device. Adv. Electron. Mater. 6, (2020). DOI: 10.1002/aelm.202000066   
(56) Wang, W.; Li, K.; Lan, J.; Shen, M.; Wang, Z.; Feng, X.; Yu, H.; Chen, K.; Li, J.; Zhou, F.; Lin, L.; Zhang, P.; Li, Y. CMOS backendof-line compatible memory array and logic circuitries enabled by high performance atomic layer deposited ZnO thin-film transistor. Nat. Commun. 2023, 14, 6079.   
(57) Zhou, X.; Zhao, L.; Yan, C.; Zhen, W.; Lin, Y.; Li, L.; Du, G.; Lu, L.; Zhang, S. T.; Lu, Z.; Li, D. Thermally stable threshold selector based on CuAg alloy for energy-efficient memory and neuromorphic computing applications. Nat. Commun. 2023, 14, 3285.   
(58) Lin, H.; Wu, Z.; Liu, L.; Wang, D.; Zhao, X.; Cheng, L.; Lin, Y.; Wang, Z.; Xu, X.; Xu, H.; Liu, Q.; Xing, G. Implementation of highly reliable and energy efficient in-memory hamming distance computations in 1 kb 1-transistor-1-memristor arrays. Adv. Mater. Technol. 6, (2021). DOI: 10.1002/admt.202100745