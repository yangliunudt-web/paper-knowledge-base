---


title: "Ferroelectric Transistors: from Materials Innovation to Intelligent Electronic"
authors:
  - "Enlong Wunan"
  - "Yu Ruixue"
  - "Chunlai Hongmiao"
  - "Shuo Shuxin"
  - "Zhaoren Kaichen"
  - "Wenwu Junhao"
  - "Chu"
date: "2025-01-01"
year: 2025
journal: "Advanced Materials"
doi: "10.1002/adma.202515480"
abstract: "The explosive growth of artificial intelligence, big data, and the Internet"
abstract_cn: "人工智能、大数据和物联网的爆炸式增长推动了对计算能力和能效的前所未有的需求。然而，传统的冯·诺依曼架构在后摩尔时代日益受到晶体管缩放物理和经济极限的制约。铁电晶体管不仅仅是一种新型存储技术，更代表了一个革命性平台，将非易失性存储、存内计算和多模态传感无缝集成到单一高能效器件中，克服了传统计算架构的瓶颈。本综述全面概述了铁电材料，包括钙钛矿氧化物、铪基化合物、有机材料和新兴二维系统，强调了它们的极化起源机制和结构-性能关系。本研究重点关注三端铁电晶体管的器件物理和工程，特别关注铁电介质和基于半导体的设计的当前问题、优化策略和对比操作原理。最后，讨论了铁电晶体管在非易失性存储器、神经形态计算和人工智能硬件中从器件到系统集成的扩展应用，并展望了由铁电创新驱动的可扩展、低功耗和多功能电子学前景。"
cite: "[1] Li E, Wang W, Liu Y, et al. Ferroelectric transistors: from materials innovation"
aiSum: "铁电晶体管综述：涵盖钙钛矿/HfO₂/有机/二维铁电材料，讨论三端FeFET器件物理、优化策略，以及非易失存储、存内计算、神经形态计算等应用，展望后摩尔时代可扩展低功耗电子系统。"
confidence: "high"
keywords:
  - "[[Ferroelectric]]"
---

# Ferroelectric Transistors: from Materials Innovation to Intelligent Electronic Systems

Enlong Li, Wunan Wang, Yu Liu, Ruixue Wang, Chunlai Luo, Hongmiao Zhou, Shuo Chen, Shuxin Chen, Zhaoren Xie, Kaichen Zhu, Wenwu Li,* and Junhao Chu

The explosive growth of artificial intelligence, big data, and the Internet of Things is driving an unprecedented demand for computing power and energy efficiency. However, conventional von Neumann architectures are increasingly constrained by the physical and economic limits of transistor scaling in the post-Moore era. Ferroelectric transistors (FeFETs) are far more than a novel memory technology and instead represent a revolutionary platform that seamlessly integrates nonvolatile storage, in-memory computation, and multi-modal sensing into a single, energy-efficient device, overcoming the bottlenecks of traditional computing architectures. This review provides a comprehensive overview of ferroelectric materials, including perovskite oxides, hafnium-based compounds, organics, and emerging 2D systems, emphasizing their polarization original mechanisms and structureproperty relationships. This study focuses on the device physics and engineering of three terminal FeFETs, with particular attention to the current issues, optimization strategies, and contrasting operation principles of ferroelectric dielectric and semiconductor-based designs. Finally, the expanding applications of FeFETs in nonvolatile memory, neuromorphic computing, and artificial intelligence hardware from device to system integration is discussed, and an outlook toward scalable, low-power, and multifunctional electronics driven by ferroelectric innovation is presented.

# 1. Introduction

The proliferation of data-intensive technologies such as the Internet of Things (IoT), artificial intelligence (AI), and edge

E. Li, W. Wang, Y. Liu, R. Wang, C. Luo, H. Zhou, S. Chen, S. Chen, Z. Xie, K. Zhu, W. Li, J. Chu

Shanghai Frontiers Science Research Base of Intelligent Optoelectronics and Perception

Institute of Optoelectronics

College of Future Information Technology

Fudan University

Shanghai 200433, China

E-mail: liwenwu@fudan.edu.cn

E. Li, W. Wang, Y. Liu, H. Zhou, S. Chen, S. Chen, Z. Xie, W. Li, J. Chu

State Key Laboratory of Photovoltaic Science and Technology

College of Smart Materials and Future Energy

Fudan University

Shanghai 200433, China

E. Li

School of Microelectronics

Shanghai University

Jiading, Shanghai 201800, China

![](images/bb4be6f185c93ae4343a6313607038d448bcf55db4a548764709bafe15f76e11.jpg)

The ORCID identification number(s) for the author(s) of this article

can be found under https://doi.org/10.1002/adma.202515480

DOI: 10.1002/adma.202515480

computing has accelerated shift toward memory-centric computing architectures.[1,2] These applications demand high energy efficiency, computational density, and real-time data processing. However, conventional computing technologies and architectures face growing challenges in meeting these demands, leading to a widening gap between computational needs and the hardware capabilities of integrated circuits (ICs). The resulting computability divide will widen increasingly with the development of artificial intelligence. Therefore, it is of great necessity to further develop new computing technology.

As illustrated in , the histor-Figure 1ical improvements in computing performance were primarily driven by transistor scaling. For example, multi-core CPUs, GPUs, and near-memory computing have offered modest gains in recent.[3,4] However, further advancement is constrained by some limitations. The computability

demand for AI doubles every 6 to 8 months, while the miniaturization of transistors in ICs following Moore’s Law only doubles every 18 to 24 months. In addition, the power consumption of memory is high, and its speed cannot keep up with the operational speed of the central processing unit (CPU). The resulting data movement overhead, known as the “memory wall”, significantly degrades system performance and energy efficiency.[5–7] On the other hand, the von Neumann architecture is inefficient, which separates memory and computation. So, a significant amount of power consumption is wasted on data access and transportation. Note that the energy consumption of data infrastructure is rising sharply. The International Monetary Fund estimates that global power consumption by data centers and AI reached 400–500 TWh in 2023, with projections exceeding 1,500 TWh by 2030.[8] This energy performance imbalance underscores the need for new computing paradigms.

In order to address these limitations, we need to rethink the basic foundation of materials and device physics. In one word, it is better to find an idea material for memory and inmemory computing applications. Fortunately, ferroelectric materials, characterized by switchable spontaneous polarization in the absence of an external electric field, possess advantages such as ultra-fast switching, low operating voltage, non-volatility, and fatigue resistance. It enables ferroelectric materials can be used

![](images/2fb99238a5a8406e52913c64e0b45243d431d70fddb6dfea214f1cd404ce3cb9.jpg)  
Figure 1. The development of the computing system based on FeFETs. Owing to their non-volatile polarization, high sensitivity, fast switching capabilities, low power consumption, and high-density integration potential, the FeFETs have emerged as a promising alternative for the current in-memory computing and future neuromorphic computing systems. They hold significant potential in addressing both the “memory wall” challenge through non-volatile memory applications and in enabling in-memory computing architectures to overcome the limitations of the von Neumann architecture.

for ultra-fast operation, low power, exceptional endurance, and non-volatility ferroelectric memories.[9–12] Furthermore, ferroelectric field-effect transistors (FeFETs) as three-terminal devices that embed ferroelectric materials into the dielectric or semiconductor layer.[13–15] Their unique properties, including multi-level switching, high speed, low power consumption, and high integration density, position FeFETs as key enablers of non-volatile in-memory computing and neuromorphic architectures. Despite substantial progress in material physics, such as hafnium oxide, perovskites, and emerging 2D ferroelectrics, there remains a lack of comprehensive reviews dedicated to the systematic understanding of ferroelectric transistors in the context of future computing demands. Besides, existing works often emphasize either material science or device demonstrations, without establishing a holistic link between ferroelectric material properties, device architecture, performance optimization strategies, and their integration into novel computing frameworks.

In this review, we aim to bridge this gap by providing a systematic and critical overview of recent developments in threeterminal ferroelectric transistors. We begin by discussing the origin and classification of ferroelectricity, distinguishing between intrinsic and non-intrinsic mechanisms. We then examine various ferroelectric material systems, including inorganic, organic,

and organic–inorganic hybrid, highlighting their key properties and integration challenges. Subsequently, we explore the device engineering of FeFETs, elucidating their working principles, performance metrics, and optimization strategies. A comparative analysis is presented between FeFETs based on ferroelectric dielectrics and ferroelectric semiconductors. We then survey recent progress in FeFET-based non-volatile memories and their role in non-volatile memory, neuromorphic computing, and AI systems. Finally, we identify the current limitations and outline future research directions for achieving scalable, energy-efficient, and AI-compatible ferroelectric transistor technologies.

# 2. Ferroelectric Materials and the Origins of Ferroelectricity

# 2.1. Classification of Ferroelectric Materials

Driven by the rising demand for scalable, energy-efficient electronics, ferroelectric materials have become essential components in non-volatile memories, in-memory computing, and flexible electronics. This section reviews the structural classes and performance characteristics of key ferroelectric materials,

![](images/da5233a0a07439b466a55b5ed066c40fdc5de5157ae2de637ccd9f317c5766db.jpg)  
Inorganic

![](images/dd901717e2b5aa2bf678311e05e28a2b9942a7eece3da9ba35c52fa9429ba631.jpg)

![](images/06e95a97b3086cf86ca42cde46ec968b6a44bca226aa53d8eb7c7264185bed7d.jpg)

![](images/c3f2e8f7105b312b0f774424baea6081d9adea474866381b47be1ad69aa6f42c.jpg)  
Two-dimensional material: lonic displacement

![](images/9d76c021ea7fdf8dac3b0f50a540afa541b7d4736bb8320d256db20656bc9f7c.jpg)

![](images/a684b7beba821b91f3f64a2845915e434987be777b43699fd33abf6ed1ccdb2b.jpg)

![](images/6329106805fef41fff7a8159eebaa96a8fad38061eaa5d4718d540a1158f4121.jpg)  
Organic

![](images/e08a0f115f5ad347832aa42abccbc91cf2e49a3629314907a2a797b891d51299.jpg)

![](images/faa166078f6149bd0967d6a8a3943bb0ae187dde6f3fd069187087ae2366f9fa.jpg)  
Organic-inorganic hybrid

![](images/a1d0d362d3d1bcc923628b64beecbdad149b9950690aa0fe47d98addaf62c8ba.jpg)  
Figure 2. The materials structure and the development of typical inorganic,[153–155] organic,[156,157] and organic–inorganic hybrid ferroelectric materials.[129,158] The Ferroelectric materials have a wide range of materials, from 3D bulk materials to 2D layered materials. Different ferroelectrics possess different polarization and material properties and are suitable for different application scenarios. The radar plot compares fundamental ferroelectric properties of different materials. Reproduced with permission.[153] Copyright 2020, Springer Nature. Reproduced under the terms of the CC BY license.[154] Copyright 2024, Springer Nature. Reproduced with permission.[155] Copyright 2018, American Chemical Society. Reproduced with permission.[156] Copyright 2017, John Wiley and Sons. Reproduced under the terms of the CC BY license.[157] Copyright 2020, The American Association for the Advancement of Science. Reproduced with permission.[129] Copyright 2025, John Wiley and Sons. Reproduced with permission.[158] Copyright 2024, John Wiley and Sons. Reproduced with permission. Copyright 2023, Springer Nature. Reproduced with permission. Copyright 2017, American Chemical Society.

including inorganic, organic, and organic–inorganic hybrid systems with a particular emphasis on their intrinsic ferroelectric parameters, such as remnant polarization (Pr), coercive field (Ec), curie temperature (Tc), dielectric constant (k), and critical film thickness. shows the material structure diagrams of sev-Figure 2eral representative types of ferroelectric materials. More details about the materials’ physical and chemical properties will be discussed later.

# 2.1.1. Inorganic Ferroelectric Materials

Traditional perovskite oxides such as $\mathrm { P b } ( \mathrm { Z r _ { 1 - x } T i _ { x } ) O _ { 3 } \ ( P Z T ) }$ , BaTiO (BTO), and BiFeO (BFO) represent the most well-studied class of ferroelectric materials. These materials typically exhibit high remnant polarization (the Pr is $1 0 { - } 4 0 ~ \mu \mathrm { C } ~ \mathrm { c m } ^ { - 2 }$ for PZT), moderate coercive fields (the Ec is 50–200 kV cm−1), and wide operational temperature windows (the Tc is 120–800 °C).[16–18] Their dielectric constants are generally high (the k is 100–1000), provid-

ing strong electrostatic coupling but also raising issues in scaling and leakage.[19,20]

The ferroelectricity in these materials is highly thicknessdependent, with critical thicknesses typically above 10–30 nm for maintaining robust domain switching. PZT is considered to be a gold standard for thin-film ferroelectrics, with mature processing and strong polarization retention; however, lead toxicity and poor CMOS compatibility limit its commercial adoption. BFO, with its Tc exceeding 800 °C, is appealing for harsh environments but suffers from high leakage currents due to intrinsic oxygen vacancies.[21] BTO, although lead-free, shows rapid fatigue and relatively low Tc (≈120 °C), restricting its high-temperature applications.[22]

HfO -based ferroelectricity, particularly doped hafnium oxide systems such as $\mathrm { H f _ { 1 - x } Z r _ { x } O _ { 2 } }$ (HZO), have gained prominence due to their excellent CMOS process compatibility and robust performance in ultrathin regimes. Ferroelectricity in these materials can be stabilized in films as thin as 5 nm or below, enabling scaling beyond what is achievable with conventional

perovskites. Typical ferroelectric properties include Pr values of $\mathsf { \bar { 1 0 } } { - } 3 0 \ \mu \mathrm { C } \ \mathrm { c m } ^ { - 2 }$ , Ec in the range of $1 { - } 3 ~ \mathrm { M V ~ c m ^ { - 1 } }$ , and dielectric constants of 20–30. The Curie temperature of HZO is relatively low $( { \approx } 4 0 0 { - } 6 0 0 \ { \mathrm { ^ { o } C } } )$ and highly dependent on doping and annealing conditions. While HfO -based materials excel in highspeed operation (polarization switching times <1 ns) and high endurance $( > 1 0 ^ { 1 2 } \mathrm { c y c l e s } )$ , they are susceptible to phase degradation at high temperatures and suffer from charge trapping at oxide interfaces, especially at low operating voltages.[23,24]

2D ferroelectric materials such as $\mathrm { C u I n P } _ { 2 } \mathrm { S } _ { 6 }$ (CIPS) and ??- $\mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ exhibit unique characteristics arising from their atomicscale thickness and van der Waals bonding. Despite their ultrathin dimensions, these materials maintain stable out-of-plane polarization with Pr typically in the range of $1 { - } 5 ~ { \mu \mathrm { C } } ~ \mathrm { c m } ^ { - 2 }$ , and Ec around $0 . 5 { - } 1 ~ \mathrm { M V ~ c m ^ { - 1 } }$ . Their dielectric constants are relatively low (k≈10–20), reducing gate leakage and allowing fine control over electrostatic potential in ferroelectric transistors. 2D ferroelectrics often lack a well-defined Tc due to their phase instability in ambient conditions; however, for example, CIPS maintains ferroelectricity up to room temperature, while $\alpha { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ shows Tc around 200 ${ } ^ { \circ } \dot { \mathbf { C } } . { } ^ { [ 2 5 ] }$ Their critical thickness can approach the monolayer limit (≈1 nm), which makes them ideal for extreme scaling. Nonetheless, surface oxidation and degradation in air significantly impact polarization retention and reliability.

# 2.1.2. Organic Ferroelectric Materials

Polyvinylidene Fluoride (PVDF) and its copolymers (e.g., Poly(vinylidene fluoride-co-trifluoroethylene), P(VDF-TrFE)) represent the prototypical class of organic ferroelectrics. These polymers exhibit switchable polarization due to the alignment of molecular dipoles in the ??-phase, with typical Pr values ranging from $1 0 { - } 2 0 \mu \mathrm { C } \ \mathrm { c m } ^ { - 2 }$ and large Ec around $5 0 { - } 1 0 0 \ \mathrm { M V } \ \mathrm { m } ^ { - 1 }$ . Their dielectric constants are relatively low (k≈10), reducing capacitance loading and relatively high switching voltage. The ferroelectric-to-paraelectric transition occurs at low Tc (≈100– $1 3 0 ~ ^ { \circ } \mathrm { C } )$ , which limits their use in high-temperature environments but allows integration with flexible, thermally sensitive substrates such as polyethylene terephthalate.[26,27] Mechanical flexibility and compatibility with solution-based processing enable roll-to-roll manufacturing and direct printing of flexible Fe-FET arrays. However, these materials require film thicknesses typically larger than 100 nm to retain ferroelectricity, and performance rapidly degrades as thickness is reduced. Below 50 nm, polarization retention becomes unstable due to incomplete $\beta \mathrm { \cdot }$ phase crystallinity and depolarizing fields.[28]

Polyamide (nylon) is another well-known class of organic ferroelectric. Its ferroelectric property is derived from the intrinsic dipole moment of the amide bond (─CO─NH─) on its molecular chain. Among them, the stable crystal structure (such as ?? phase) of odd-odd nylons (such as nylon 11) naturally has a non-centrosymmetric polarity characteristic, which enables the dipoles within the molecule to spontaneously align in the same direction, realizing excellent out-of-plane ferroelectricity.[29] The prepared odd-number nylon films have a coercive field of up to $\bar { 1 } 2 5 \mathrm { M V } \mathrm { m } ^ { - 1 }$ and a residual polarization intensity of $4 . 5 \pm 0 . 5 \mu \mathrm { C }$ $\mathrm { c m } ^ { - 2 }$ at a thickness of 185 nanometers. Its powerful hydrogen bond network more effectively “locks” the polarization state, en-

dowing it with residual polarization stability far exceeding that of even-numbered nylon and even superior to that of PVDF-based polymers. Although the molecular chain spacing of this phase is relatively large and the hydrogen bond network is relatively disordered, allowing dipole orientation, its metastable property leads to poor ferroelectricity retention.[30] Therefore, compared with even-nylons, odd-nylons have been developed and applied in fields such as data storage devices due to their stable ferroelectricity. At present, organic ferroelectric materials universally face the challenge of high coercive fields, which elevate operating voltage and power consumption. This issue stems from pronounced size effects at nanometer-scale thicknesses, where interface states, defects, and depolarization fields degrade polarization and increase leakage, severely weakening ferroelectricity. Current research thus focuses on mitigating these effects through molecular design, interfacial engineering, and hybrid stacking to achieve stable, low-coercive-field ultrathin films suitable for lowpower, flexible electronics.

# 2.1.3. Organic–Inorganic Hybrid Ferroelectric Materials

Organic-inorganic hybrid ferroelectrics represent a structurally versatile class of materials that integrate polarizable organic components (e.g., amines, polymers) with ferroelectrically active inorganic frameworks (e.g., halide perovskites, metal oxides) through hydrogen bonding, ionic coordination, or van der Waals interactions. The resulting synergy enables dipole reorientation via molecular order-disorder transitions and displacement-induced polarization within the inorganic sublattice.[31] The ferroelectricity of organic-inorganic ferroelectric materials mainly stems from the ordering of organic cations and the displacement of inorganic skeletons. However, this mechanism also determines that its residual polarization is usually low, generally within the range of $1 - 1 0 \mu \mathrm { { C } } / \mathrm { { c m } } ^ { 2 } . ^ { [ 3 2 ] }$ Meanwhile, due to the order-disorder transformation of organic cations and the limitation of hydrogen bond strength, the Curie temperature of such materials is often below $1 0 0 ^ { \circ } \mathrm { C } .$ In addition, the presence of the organic layer hinders the movement of domain walls, thereby increasing the potential barrier for domain wall inversion and resulting in a relatively high coercive field, which can reach tens of $\mathrm { k V } \mathrm { c m } ^ { - 1 }$ .

A distinctive advantage of hybrid systems is their coexistence of semiconductor and ferroelectric characteristics. Many hybrid perovskites exhibit high carrier mobilities and low trap densities, which allow them to simultaneously support charge transport and polarization-based switching. Moreover, their compositionally tunable bandgaps and strong light absorption coefficients enable photoferroelectric effects, positioning them as promising candidates for ferroelectric photovoltaic and photodetection applications.[33] Materials such as methylammonium lead iodide $( \mathrm { M A P b I } _ { 3 } )$ , formamidinium tin iodide $( \mathrm { F A S n I } _ { 3 } )$ , and their lowdimensional derivatives have demonstrated light-tunable ferroelectric switching and photostimulated memory functionalities. In addition, the weak interlayer van der Waals interaction in layered hybrid systems imparts structural similarities to 2D ferroelectrics, allowing them to retain stable polarization states down to the nanometer scale. This opens opportunities for ultra-thin, flexible non-volatile memories and ferroelectric transistors.

Table 1. Ferroelectric Properties of the typical ferroelectric materials.   

<table><tr><td>Type</td><td>Materials</td><td>ferroelectric thickness</td><td>k</td><td>Tc[°C]</td><td>Pr[μCcm-2]</td><td>Ec[kVcm-1]</td><td>Refs.</td></tr><tr><td rowspan="15">Inorganic</td><td>BaTiO3</td><td>NA</td><td>1700</td><td>115</td><td>7.5</td><td>4</td><td>[159]</td></tr><tr><td>Na0.5Bi0.5TiO3</td><td>NA</td><td>NA</td><td>320</td><td>38</td><td>73</td><td>[160]</td></tr><tr><td>LiNbO3</td><td>270 nm</td><td>NA</td><td>NA</td><td>20</td><td>30</td><td>[161]</td></tr><tr><td>BiFeO3</td><td>120 nm</td><td>NA</td><td>827</td><td>90-100</td><td>26-30</td><td>[17]</td></tr><tr><td>Pb(Ti, Zr)O3</td><td>50 nm</td><td>130-400</td><td>400</td><td>10-40</td><td>50-70</td><td>[162]</td></tr><tr><td>PZT</td><td>NA</td><td>1300-3400</td><td>193-328</td><td>15-20</td><td>55</td><td>[16]</td></tr><tr><td>PLZT</td><td>NA</td><td>1300</td><td>145</td><td>26.9</td><td>6.7</td><td>[163]</td></tr><tr><td>SrBi2Ta2O9</td><td>NA</td><td>200</td><td>400</td><td>5-10</td><td>30-50</td><td>[164]</td></tr><tr><td>Hf0.5Zr0.5O2</td><td>5 nm</td><td>20-30</td><td>&gt;RT</td><td>16-17</td><td>1000</td><td>[165]</td></tr><tr><td>AlScN</td><td>20 nm</td><td>14-16</td><td>&gt;RT</td><td>80-115</td><td>2000-4500</td><td>[166]</td></tr><tr><td>CuInP2S6</td><td>≥2 layers</td><td>NA</td><td>42</td><td>2.55</td><td>700</td><td>[25]</td></tr><tr><td>(α, β&#x27;)-In2Se3</td><td>≥1 layer</td><td>17</td><td>427</td><td>0.92</td><td>200</td><td>[114]</td></tr><tr><td>γ-InSe</td><td>≥1 layer</td><td>、</td><td>&gt;RT</td><td>0.48</td><td>NA</td><td>[167]</td></tr><tr><td>SnS</td><td>≥1 layer</td><td>17.5</td><td>527-927</td><td>17.5</td><td>20</td><td>[115]</td></tr><tr><td>SnTe</td><td>≥1 layer</td><td>NA</td><td>-3</td><td>13-22</td><td>100</td><td>[168]</td></tr><tr><td rowspan="4">Organic</td><td>P(VDF-TrFE)</td><td>300 nm</td><td>8</td><td>100</td><td>10</td><td>330-400</td><td>[169]</td></tr><tr><td>Nylon-(6, 7, 11, 12)</td><td>NA</td><td>5</td><td>NA</td><td>1.8-8.6</td><td>500-790</td><td>[30]</td></tr><tr><td>PLA</td><td>113 nm</td><td>NA</td><td>&gt;RT</td><td>0.795</td><td>225</td><td>[170]</td></tr><tr><td>TGS</td><td>200 um</td><td>36</td><td>48</td><td>2.8</td><td>0.4</td><td>[171]</td></tr><tr><td rowspan="2">Organic-inorganic hybrid</td><td>HA2MA2Pb3Cl10</td><td>35 nm</td><td>NA</td><td>66-69</td><td>3000</td><td>6.5</td><td>[129]</td></tr><tr><td>(FA0.86Cs0.14)SnI3&amp;PEA2SnI4</td><td>38 nm</td><td>NA</td><td>&gt;RT</td><td>23.2</td><td>NA</td><td>[44]</td></tr></table>

PLZT: Lead lanthanum zirconium titanate, PLA: poly (lactic acid), TGS: (CHsNHsCOOH) H SO.

The high degree of molecular designability also enables the engineering of dipolar motifs, lattice flexibility, and defect tolerance. Functional groups and metal centers can be chemically tailored to modulate the Pr, Ec, Tc, and optoelectronic responses. Moreover, hybridization with 2D semiconductors (e.g., MoS , WS ) yields vdW heterostructures with controllable band alignment and interfacial dipole coupling, enabling multi-functional memory-logic-sensor integration in a single platform. This hybrid platform offers broad opportunities to harness the unique regulatory capabilities of ferroelectric materials. For instance, the incorporation of intrinsically ferroelectric perovskites enhances the photoresponse and carrier dynamics of TMDs via polarization-induced electric fields.[34] In addition, surface functionalization of TMDs with organic ferroelectric molecular layers provides a precise approach to modulate interfacial charge distribution and band alignment, further expanding the design flexibility and multifunctionality of ferroelectric systems.[35] Despite these advantages, several challenges remain for large-scale device implementation, such as material instability. Many hybrid halide perovskites are susceptible to degradation under heat, light, and moisture, with decomposition onset around 85 °C. Besides, the soft lattices, interfacial traps, and mobile ions often lead to the electrostatic shielding of gate regulation, which increases the leakage and reduces on/off ratios, cycle endurance, and memory retention of devices. Achieving uniform, pinholefree films over large areas also remains challenging due to

complex crystallization dynamics and solution-processed growth conditions.

summarizes the key ferroelectric parameters of rep-Table 1resentative material systems, including ferroelectric layer thickness, remnant polarization, coercive field, Curie temperature, and dielectric constant. These metrics reflect the intrinsic material responses under an electric field, which are critical for evaluating their integration suitability in the application of electronics, optoelectronics, and energy harvesting. As evident from the comparison of Table 1, perovskite oxides such as BTO and PZT typically exhibit high remanent polarization and Curie temperatures, making them well-suited for high-temperature operation and endurance-critical applications. However, their hightemperature processing and integration challenges limit their compatibility with modern CMOS technologies. HfO -based ferroelectrics, particularly doped HfO thin films, offer excellent scalability down to sub-10 nm thickness and full compatibility with CMOS processes. These properties make them ideal for embedded non-volatile memory and logic integration. Despite their moderate Pr, their scalability, reliability, and manufacturability position them as the most industry-relevant platform today. 2D ferroelectrics such as $\mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ and $\mathrm { C u I n P } _ { 2 } \mathrm { S } _ { 6 }$ exhibit intrinsic or sliding ferroelectricity with atomic-layer thickness, making them promising for ultra-scaled and flexible electronics. Their lack of dangling bonds and inherent crystallinity allows for defect-tolerant interfaces, although their Pr and

![](images/40fd2865f3a40c6676bd996ae3df5b0e42b629eac4d3e9847e55fa1e63e45a60.jpg)  
a   
lon displacement   
P down

![](images/89cefd315bda8250675c6c6afff7952535451873bff4458dd75c276eb0f6f386.jpg)

![](images/6eaae4bb67b0ee729242cdabdda3aef43859be0d4a65dd08f9595e16be84b2a9.jpg)

![](images/13a94d54f44a2e07b6f818658cfec2d6a4d5f9060cc52f3caf2f6980d46c7d37.jpg)  
Ferroelectricity

![](images/661a539c08a387ec17e3c30ce293519515cee06aeb7993776c14a4911afd38ec.jpg)  
  
Pdov   
Polar molecules   
Charge redistribution

![](images/2841c68772aaea2083ebac13a20c04144ea92e398c735d822485f2865b7b40b8.jpg)  
C   
AB

![](images/de9fc5a9bfb854d16cb6a3141dd334f631d448a64212afbde8492916504ce4ae.jpg)  
Sliding   
d

![](images/dfdac41c96e221efe4fd477ea8113831abdedc82c549482802c8ab9b24bc47d7.jpg)  
Figure 3. Origin of ferroelectricity. a) Schematic diagram of ion displacement-induced ferroelectricity. b) Schematic diagram of the polar molecular group induced ferroelectricity. c) Schematic diagram of charge redistribution induced ferroelectricity and switching of h-BN in antiparallel stacking, where −P and +P represent downward and upward polarizations, respectively.[172] d) Schematic diagram of the periodic moiré pattern of h-BN with small-angle twist.[47] c) Reproduced with permission.[172] Copyright 2021, The American Association for the Advancement of Science. d) Reproduced with permission.[47] Copyright 2021, The American Association for the Advancement of Science.

endurance still require improvement. Organic ferroelectric materials, such as P(VDF-TrFE), feature mechanical flexibility, lowtemperature processability, and biocompatibility, enabling applications in flexible, wearable, or implantable electronics. However, they often suffer from limited Pr and relatively poor environmental stability. Organic–inorganic hybrid ferroelectrics combine solution processability and photo-responsiveness with ferroelectric functionality, offering potential in optoelectronic memory and neuromorphic devices. Yet, challenges remain in phase stability, hysteresis control, and long-term reliability. Therefore, the selection of a suitable ferroelectric material system must be tailored to the specific application scenario, balancing trade-offs between switching performance, integration requirements, environmental stability, and processing compatibility, to fully exploit the functional potential of each material platform.

# 2.2. Origins of Ferroelectricity

Ferroelectricity refers to the presence of a spontaneous electric polarization that can be reversed by an external electric field. This fundamental property arises from a lack of inversion symmetry in the material’s crystal structure and plays a critical role in a wide range of applications. The field of ferroelectricity has expanded to include a broad spectrum of material systems with varying dimensional, bonding mechanisms, and switching be-

haviors. In this section, ferroelectricity is generally categorized into three types based on its physical origin: ion-displacement, polar atom/molecular group, and charge redistribution-induced ferroelectricity. The understanding of the origin of ferroelectricity is crucial for advancing applications in non-volatile memory, sensors, and actuators, as well as for exploring their broader potential.

# 2.2.1. Ion Displacement Induced Ferroelectricity

As shown in the schematic of a, ion-displacement in-Figure 3duced ferroelectrics exhibit spontaneous polarization originating from the asymmetric displacement of ions within a crystal lattice. This phenomenon is typically associated with structural instabilities that break inversion symmetry, leading to the emergence of a permanent electric dipole. Such polarization appears below the Curie temperature (Tc) and can be reversibly switched by an external electric field.

A classic example of ion displacement ferroelectrics is the perovskite oxides such as BTO and PZT, where ferroelectricity results from the off-center displacement of titanium ions within oxygen octahedra.[36] This phenomenon is explained by Cochran’s soft mode theory,[37] which suggests that softening specific lattice vibration modes induces structural distortions. In these perovskites, the movement of metal ions (like Ti4+) within

the oxygen octahedra separates the charge centers of cations and anions, creating an electric dipole moment.[38] This ionic migration is influenced by temperature changes and external electric fields, resulting in spontaneous polarization that can be reversed by applying an external field. Additionally, intrinsic ferroelectrics undergo a phase transition at the Tc. Above Tc, these materials exist in a high-symmetry cubic phase with no net polarization. As the temperature decreases below Tc, the symmetry is broken, leading to a non-centrosymmetric phase (such as tetragonal or orthorhombic) and the emergence of spontaneous polarization.

In contrast to conventional perovskite oxides, CIPS represents a layered van der Waals (vdW) compound that also exhibits iondisplacement induced ferroelectricity, albeit through a different lattice mechanism.[39] In CIPS, ferroelectricity arises from the vertical displacement of Cu+ ions within the van der Waals gaps of the layered lattice. Below Tc, these Cu+ ions shift asymmetrically along the out-of-plane direction, breaking the centrosymmetry and inducing spontaneous polarization.[25,40] This displacement is stabilized by the soft lattice environment and weak interlayer interactions characteristic of vdW materials, enabling ferroelectricity even in ultrathin and exfoliated flakes.

# 2.2.2. Polar Molecular Induced Ferroelectricity

Beyond traditional ion displacement mechanisms, ferroelectricity can also arise from the alignment and ordering of polar molecular groups. In such systems, spontaneous polarization originates from molecular dipoles or asymmetric molecular configurations, rather than from collective ion shifts within a rigid lattice. These materials exhibit switchable polarization due to the reorientation of dipolar units under an external electric field, often enabled by structural flexibility and weak intermolecular interactions. Moreover, as shown in Figure 3b, the centrosymmetric non-ferroelectric material can also induce symmetry breaking by doping with certain polar molecular materials, resulting in stable ferroelectricity.

A prominent example is the organic ferroelectrics P(VDF-TrFE), a widely studied ferroelectric polymer. Ferroelectricity in P(VDF-TrFE) stems from the strong electronegativity difference between fluorine and hydrogen atoms along the polymer backbone, creating permanent polar-molecular and dipole moments.[41] Upon electrical poling, the conformation of the polymer chains aligns the dipoles in a uniform direction, generating macroscopic polarization. Besides, this polarization is reversible, and the dipole moments remain after the removal of the electric field, endowing P(VDF-TrFE) with excellent ferroelectric memory properties, mechanical flexibility, and processability at low temperatures.

Organic–inorganic hybrid perovskite systems also demonstrate ferroelectricity driven by molecular dipoles and asymmetric structural units. In these systems, ferroelectricity primarily originates from the orientational ordering of polar organic molecular units such as imidazolium or methylammonium within a non-centrosymmetric or distorted inorganic lattice.[42,43] The spontaneous polarization arises through cooperative dipole alignment, often aided by hydrogen bonding and lattice asymmetry. This mechanism enables switchable ferroelectric behavior, offering low-voltage operation, solution process-

ability, and multifunctional properties ideal for flexible and optoelectronic applications. Recently, by doping polar-molecular, 2- methylbenzimidazole, Liu et al. successfully converted Sn-based perovskite semiconductor films (93.3 mol% $( \mathrm { F A } _ { 0 . 8 6 } \mathrm { C s } _ { 0 . 1 4 } ) \mathrm { S n I } _ { 3 }$ and 6.7 mol.% $\mathrm { P E A } _ { 2 } \mathrm { S n I } _ { 4 } )$ into ferroelectric semiconductors through molecular rearrangement. The doped film exhibited a high remanent polarization of $: 2 3 . 2 \mu \mathrm { C c m } ^ { - 2 }$ and clear 180° phase switching under an applied electric field, as evidenced by piezoelectric force microscopy. This ferroelectricity originates from enhanced hydrogen bonding and spatial asymmetry induced by the imidazole units, which disrupt charge center alignment and create switchable electric dipoles.[44]

# 2.2.3. Charge Redistribution Induced Ferroelectricity

Beyond conventional ferroelectricity driven by ion displacement or polar molecular orientation, recent discoveries have unveiled a novel class of ferroelectric phenomena arising from interlayer charge redistribution. Unlike traditional mechanisms, this type of ferroelectricity does not require structural symmetry breaking but instead stems from asymmetries in electronic charge distribution between layers, often modulated by subtle interlayer translations or twisting configurations (Figure 3c,d). This mechanism has been widely observed in vdW materials and is commonly referred to as sliding ferroelectricity.

The concept of sliding-induced ferroelectricity, understood as a manifestation of charge redistribution was first proposed theoretically in 2017 by Wu et al., who predicted that bilayer hexagonal boron nitride (h-BN) could exhibit spontaneous polarization due to AB or BA stacking configurations without layer rotation.[45] As shown in Figure 3c, the asymmetric stacking order between layers leads to an unequal charge distribution, giving rise to a net out-of-plane polarization. Sliding the layers reverses the stacking order, consequently reversing the direction of polarization via charge transfer, even in the absence of ionic displacement.[46] Similarly, by small-angle twisting, as shown in Figure 3d, Similar effects can be engineered via small-angle twists, which create periodic ferroelectric domains with alternating stacking arrangements (AB, BA, AA), separated by domain walls.[47]

Experimental evidence of charge redistribution-induced ferroelectricity was later reported in 2020 by Zheng et al., who demonstrated unconventional ferroelectric hysteresis in bilayer Bernal-stacked graphene encapsulated by h-BN. The interlayer charge transfer driven by molar flat bands in aligned bilayer graphene produced a polarization of 0.18 μCcm−2. [48] As shown in  a, after spatially aligning the bilayer graphene and the Figure 4top (bottom) h-BN, the molar superlattice potential was introduced into it. When an out-of-plane electric field was applied, the graphene resistor had a typical and robust hysteresis behavior.

Compared with graphene and h-BN, twisted homologous or heterogeneous layers of transition metal dichalcogenides (TMDs) may provide a wider diversity for electronics because they have suitable bandgaps. In 2022, Pablo et al.[49] and Roman et al.[50] simultaneously reported the sliding ferroelectricity of transition metal sulfides. By stacking two identical monolayer TMDs (MX2, M represents W and Mo, X represents S and Se) in parallel, an electrically switchable rhombohedral stacking configuration was obtained, and its out-of-plane polarization was

![](images/f894a70ab3638e817b520f71b09c48fc12ab8730a3523cc08315c3566342aef4.jpg)  
a   
Bernal bilayer graphene

![](images/d068af5a31ca59683cd96c84a8d63559648000373ac261e13e25b3a2560a8840.jpg)  
b   
Twisted homologous bilayer

![](images/5ea7fe33f6e3502cb91929cb531720eb74c698bf47b9640650aaa062ffd18573.jpg)

![](images/9565eb08700c6e36e16e1edbbde87ac698b0c114bee12a908b4e4662005b36e7.jpg)

![](images/0587baed0ea230c0221ed9ec8704c0dc8526b4e3109421d9816c1ae00353045a.jpg)

![](images/ba6a6d2226764a5a5d638f99a90c98e54650c5b753583801c8756152cf9ee61a.jpg)

![](images/ffc40722f103d7afdd3210c07a2d14dad93073732b8aae55ec86c53a02c36d39.jpg)

# Twisted heterojunction bilayer

![](images/deed5602ca048a75d327763cdd156d84a1e54dab155087913af730828231875b.jpg)  
C

![](images/10ed37315cea72540bedf224d20b04d7c17c045a0865ca968bdabab978a762cc.jpg)

![](images/27689691cc642edc4dcbd1ef3a0cc8460822f92f0d2eeb8ed6a73a2a23d53b17.jpg)  
d

![](images/815848e7854b16959e4e0fff5513b989bc7841f6bd1a2cae9bf8beda5e74699a.jpg)  
Figure 4. Sliding induced non-intrinsic ferroelectricity. a) Lattice structure of Bernard stacked bilayer graphene and four-probe resistance diagram for a hysteretic device.[48] b) Schematic diagram of different stacking orders of double-layer TMD. H stacking (antiparallel stacking) satisfies the spatial inversion symmetry, while R stacking (parallel stacking) breaks the spatial inversion symmetry.[49] c) SHG intensity comparison image and schematic diagram of 2H stacking and 3R stacking of $\mathsf { M o S } _ { 2 } / \mathsf { W S } _ { 2 } . \mathsf { I } ^ { 5 0 ] }$ d) Piezoelectric force microscopy phase and amplitude spectra of $\mathsf { M o S } _ { 2 } / \mathsf { W S } _ { 2 }$ before and after poling $\mathsf { M o S } _ { 2 } / \mathsf { W S } _ { 2 } . \mathsf { [ } 5 0 \mathsf { ] } _ { \mathrm { ~ } \mathfrak { a } } )$ 2 2 2 2  Reproduced with permission.[48] Copyright 2020, Springer Nature. b) Reproduced with permission.[49] Copyright 2022, Springer Nature. ${ \mathsf { c } } , { \mathsf { d } } )$ 2 Reproduced with permission.[50] Copyright 2022, The American Association for the Advancement of Science.

flipped by the in-plane sliding motion. As shown in Figure 4b, the sliding motion between parallel-stacked TMD monolayers generates out-of-plane polarization, while antiparallel stacking restores inversion symmetry and eliminates net polarization.[49] A significant advancement came when Rogée et al. demonstrated that heterostructures composed of ${ \mathrm { M o S } } _ { 2 }$ and ${ \mathbb { W } } S _ { 2 }$ could also exhibit charge redistribution-induced ferroelectricity without requiring twist angles. As shown in Figure 4c, zero-angle stacked $\mathrm { M o S } _ { 2 } / \mathrm { W S } _ { 2 }$ bilayers fabricated by CVD exhibited stable ferroelectric and piezoelectric responses. First-principles calculations revealed that spontaneous symmetry breaking arises from interlayer charge imbalance, and polarization switching occurs via lateral sliding of the layers.[50] The out-of-plane ferroelectricity and piezoelectricity of the heterojunction bilayer were tested by piezoelectric force microscopy in Figure 4d. The charge redistributioninduced ferroelectricity offers a distinct mechanism to achieve electrically switchable polarization in low-dimensional materials without relying on lattice distortion. This emerging mechanism allows for precise tuning of ferroelectric behavior through stacking sequence, interlayer spacing, and twist angle, offering unprecedented opportunities. To elucidate the intrinsic strength and application potential of sliding ferroelectricity, sys-Table 2tematically compares the Pr values reported for a broad range of material systems, including individual 2D crystals and their heterostructures based on both theoretical predictions and experimental measurements. This comparative analysis provides read-

ers with a clear quantitative understanding of sliding ferroelectric performance and facilitates the selection of appropriate material platforms for different device scenarios

# 3. Design, Mechanisms, and Optimization of Ferroelectric Transistors

Building upon the foundational understanding of ferroelectric origin mechanisms, the translation of these intrinsic or engineered polarization behaviors into device-level functionality has become a central focus in next-generation electronics. Among various implementations, FeFETs serve as a critical platform to exploit ferroelectricity within standard transistor configurations. By integrating ferroelectric materials into the gate dielectric or semiconductor channel, FeFETs enable nonvolatile modulation of channel conductance via switchable polarization states.[15] This embedded ferroelectricity offers distinct advantages over conventional MOSFETs: the strong local electric fields generated by remanent polarization can significantly lower the operating voltage and off-state leakage current, enhancing energy efficiency.[51] Furthermore, the strong coupling between ferroelectric polarization and the semiconductor channel facilitates localized electrostatic doping, thereby enabling reconfigurable control over carrier type and density.[52] This tunability not only enhances charge transport modulation but also introduces functionalities such as ambipolar switching,

Table 2. Comparison of polarization value across different sliding ferroelectric material systems.   

<table><tr><td>Materials System</td><td>Polarization</td><td>Refs.</td></tr><tr><td>BN bilayer</td><td>2.08 pC m-1</td><td>[45]</td></tr><tr><td>BP bilayer</td><td>1.075 pC m-1</td><td>[173]</td></tr><tr><td>ZnO bilayer</td><td>8.22 pC m-1</td><td>[45]</td></tr><tr><td>AlN bilayer</td><td>10.29 pC m-1</td><td>[45]</td></tr><tr><td>GaN bilayer</td><td>9.72 pC m-1</td><td>[45]</td></tr><tr><td>SiC bilayer</td><td>6.17 pC m-1</td><td>[45]</td></tr><tr><td>MoS2bilayer</td><td>0.97 pC m-1</td><td>[45]</td></tr><tr><td>InSe bilayer</td><td>0.24 pC m-1</td><td>[45]</td></tr><tr><td>GaSe bilayer</td><td>0.46 pC m-1</td><td>[45]</td></tr><tr><td>3R-MoSe2bilayer</td><td>0.651 pC m-1</td><td>[174]</td></tr><tr><td>3R-MoTe2bilayer</td><td>0.712 pC m-1</td><td>[174]</td></tr><tr><td>3R-WS2bilayer</td><td>0.680 pC m-1</td><td>[174]</td></tr><tr><td>3R-MoS2bulk</td><td>0.52 μC cm-2</td><td>[45]</td></tr><tr><td>3R-InSe bulk</td><td>0.08 μC cm-2</td><td>[45]</td></tr><tr><td>h-SnS2bulk</td><td>0.18 μC cm-2</td><td>[175]</td></tr><tr><td>h-CrI3bulk</td><td>0.06 μC cm-2</td><td>[176]</td></tr><tr><td>3R-WTe2bilayer</td><td>0.731 pC m-1</td><td>[174]</td></tr><tr><td>3R-WSe2bilayer</td><td>0.701 pC m-1</td><td>[174]</td></tr><tr><td>MnSe bilayer</td><td>2.7 pC m-1</td><td>[177]</td></tr><tr><td>WTe2bilayer</td><td>0.38 pC m-1</td><td>[178]</td></tr><tr><td>HgI bulk</td><td>1.16 μC cm-2</td><td>[179]</td></tr></table>

threshold voltage programmability, and dynamic logic reconfiguration. This section explores the structural configurations, working mechanisms, and performance engineering of FeFETs, highlighting how material-level ferroelectricity is harnessed at the device level to address emerging challenges in modern electronics.

# 3.1. Ferroelectric Dielectric Field Effect Transistors

# 3.1.1. Device Structure

While the integration of ferroelectric materials into the dielectric layer of transistors unlocks powerful functionalities, the practical realization of high-performance FeFETs necessitates careful structural design to overcome intrinsic and extrinsic limitations. Challenges such as depolarization fields, interfacial trap states, limited endurance, and the need for compatibility with advanced CMOS technology nodes have prompted the development of diverse architectural innovations. As illustrated in 5, these include classical Metal–Ferroelectric– FigureSemiconductor (MFS) structures, interface-engineered Metal– Ferroelectric–Insulator–Semiconductor (MFIS) designs, and Metal–Ferroelectric–Metal–Insulator–Semiconductor (MFMIS) stacks that decouple ferroelectric and dielectric domains. Moreover, dual-gate configurations allow independent control over logic and memory operations, while 3D device geometries such as FinFETs and Gate-All-Around (GAA) structures offer enhanced electrostatic control and scalability. The following section systematically reviews these device architectures, highlighting how structural engineering strategies address key materialdevice integration challenges.

Metal–Ferroelectric–Semiconductor: The MFS architecture represents a straightforward FeFET configuration, in which a ferroelectric layer is directly sandwiched between a metal gate and a semiconductor channel (Figure 5a). This intimate interface allows for strong electrostatic coupling and efficient modulation of channel conductance via ferroelectric polarization, enabling high-speed switching and compact integration. Moreover, when implemented with wide-bandgap oxide semiconductors (e.g., indium tin oxide, ITO; indium gallium zinc oxide, IGZO) and low-temperature-processed ferroelectrics, MFS structures can offer enhanced transparency, mechanical flexibility, and process compatibility with flexible electronics. However, the direct ferroelectric/semiconductor interface is highly susceptible to interfacial chemical reactions and defect formation, especially in silicon-based systems. For instance, the deposition of HfO -based ferroelectrics directly on Si often induces interfacial $\mathrm { S i O _ { x } }$ formation, which acts as a low-permittivity layer, introducing substantial depolarization fields and threshold voltage instability.[53,54] These effects degrade memory retention and scalability. Thus, while MFS FeFETs offer strong polarization channel coupling, their practical performance critically depends on careful interface engineering and material compatibility.

Metal–Ferroelectric–Insulator–Semiconductor: To enhance interface reliability and suppress defect formation, the MFIS architecture incorporates an insulating buffer layer such as ${ \mathrm { S i O } } _ { 2 } ,$ $\mathrm { H f O } _ { 2 }$ between the ferroelectric layer and semiconductor channel (Figure 5b). This additional insulator serves to chemically isolate the ferroelectric film from the underlying semiconductor, reducing interface state density and improving overall device endurance. Furthermore, MFIS configurations offer greater process tunability by enabling the independent optimization of ferroelectric and semiconductor interfaces. Nevertheless, the presence of an intermediate insulator introduces parasitic capacitance and voltage division, reducing the effective field across the ferroelectric and weakening polarization switching. This challenge is especially pronounced when low-k materials like $\mathrm { S i O } _ { 2 }$ are used, leading to reduced memory windows and increased susceptibility to charge trapping. To address these issues, high-k interfacial layers such as HfSiO and $\mathrm { S i N _ { x } }$ have been employed. For instance, Jia et al. demonstrated that $\mathrm { H f S i O _ { x } }$ interlayers significantly improved switching speed and retention, achieving endurance beyond $1 0 ^ { 1 0 }$ cycles.[55] Similarly, Hu et al. showed that $\mathrm { S i N _ { s } }$ -based MFIS devices enabled immediate read-after-write functionality by suppressing transient trap-related effects.[56]

Metal–Ferroelectric–Metal–Insulator–Semiconductor: The MFMIS structure introduces a metallic interlayer between the ferroelectric and insulating dielectrics, forming a ferroelectric capacitor in series with the transistor gate stack (Figure 5c). This design ensures a uniform lateral electric field distribution in the ferroelectric layer under negative bias, effectively resolving the weak erase issue commonly observed in conventional FeFETs. In the MFMIS configuration, the gate voltage is divided between the ferroelectric and dielectric layers according to their capacitances. By reducing the area or capacitance ratio $( \mathsf { A } _ { \mathrm { F E } } / \mathsf { A } _ { \mathrm { D E } } )$ , a larger portion of the gate voltage drops across the ferroelectric layer, thereby enhancing polarization switching, widening the memory window, and increasing the conductance dynamic range.[57,58] Simultaneously, the reduced voltage across the gate dielectric suppresses electron injection and mitigates interface

![](images/4cb3de5eba29c54876de51301ec27d780e74257b1cfc8ec8341985a0df5a55a7.jpg)  
a   
MFS

![](images/8949e46c81437c4b9f95001fa08fc547731e817f224ef2b81ade1f8d4c54b44b.jpg)  
b   
MFIS

![](images/36b3d927071601c260e880cf4046dfca14aa6b5799e6e452bd9608d9bd3dd32e.jpg)  
C   
MFMIS

![](images/7bfc78913e300735da3cfba0d6e5251a057ac6fdd03144c610256e28b0220d98.jpg)  
d   
DUAL gate

![](images/76484bf34559ab1eb3355c2c6aff1cf213007648c959c92ad879d4a4031b7c92.jpg)  
e   
Fin-FET

![](images/37c2b3d7011502d8f702a3326003bca5a1888d002042117de2292698c1cd965d.jpg)  
f   
GAA

![](images/6d18aa32ab15b6326fcc86973fbd13426fe7b611191ee09efe9317faffeee361.jpg)  
metal

![](images/1e1726ad4426958615a279990ce396e57f226757c4a08918b88b117c6c4c7e2f.jpg)  
semiconductorl

![](images/e02bfe23d3f36f1304a7d8f3c9c1152a535d4adeae6c2b3c8bf012d0278aef89.jpg)  
insulator   
ferroelectric

![](images/24d085949df9b58f7e6adea51c01f63a694da370c050c1bc7962c98ac9eac04d.jpg)  
substrate   
Figure 5. Schematic diagrams of FeFETs with different device structures. a) Metal-ferroelectric-semiconductor FET, where the ferroelectric region is in direct contact with the semiconductor. b) Metal-ferroelectric-insulator-semiconductor FET, where the performance of the FeFET can be improved by optimizing the insulating layer. c) Metal-ferroelectric-metal insulator-semiconductor FET, which can be viewed as a ferroelectric capacitor in series with a FET. The ferroelectric capacitor can be integrated with the FET or connected externally. d) Dual-gate FeFET utilizes two gates: a ferroelectric gate for memory functionality and a conventional gate for logic operations. e) Fin-FeFET, where the “fin” gate is the ferroelectric gate. f) Gate-all-around FeFET, where the semiconductor layer is surrounded by the ferroelectric and dielectric gate stacks.

degradation from repeated switching events. Furthermore, the structural decoupling of the ferroelectric and semiconductor interfaces alleviates charge trapping and reliability issues. The MFMIS architecture also offers greater design flexibility, allowing separate optimization of the ferroelectric capacitor and transistor channel, and supports BEOL-compatible integration for advanced logic-memory co-design.

Dual-Gated FeFETs: The dual-gated FeFETs typically integrate two gate electrodes at the top and bottom of the semiconductor layer, combining a ferroelectric gate for nonvolatile memory operations and a conventional gate for logic or read functions, enabling independent control of programming and sensing processes (Figure 5d). This structural decoupling enhances functional versatility and allows for simultaneous logic-in-memory and neuromorphic computing within a single-transistor footprint. Unlike traditional single-gate FeFETs, where logic gate implementation often requires cascading multiple devices or complex control sequences, resulting in increased area and latency, dual-gate architectures offer simplified and compact solutions for multifunctional in-memory computing.[59] By assigning program/erase operations to the ferroelectric gate and readout to the conventional gate, this structure effectively expands the memory window, mitigates read disturbance, and enhances operational reliability.[60] Moreover, modulation of the read-gate voltage can further accelerate programming speed and improve endurance, offering tunable performance across diverse computing tasks.

FinFETs and GAA FeFETs: With continued device scaling, 3D architectures such as FinFET and GAA FeFETs have become increasingly important for FeFETs (Figure 5e,f). In FinFETs, the gate wraps around the channel on three sides, providing improved electrostatic control and reduced short-channel effects.

GAA architectures further enhance these properties by fully enclosing the channel, offering near-ideal gate modulation and scalability. The superior channel control in these geometries stems from reduced interface state density and enhanced electrostatic integrity, which are critical for maintaining reliable ferroelectric switching at nanometer nodes.[61] HfO -based ferroelectric Fin-FETs have already been demonstrated at the 28 nm technology node, narrowing the integration gap between FeFETs and advanced CMOS logic processes.[62] Compared with planar FETs, FinFET structures exhibit stronger vertical electric fields, promoting faster polarization switching and improved program/erase efficiency. GAA FeFETs are regarded as the most scalable FeFET architecture for sub-5 nm nodes due to their excellent gate control, high current drive per footprint, and compatibility with vertically stacked integration schemes. In particular, vertical offer enhanced integration density by accommodating multilayer ferroelectric channels and ultra-short gate lengths, making them wellsuited for embedded nonvolatile memory and logic-in-memory applications.[63]

# 3.1.2. Challenges and Strategies for Enhancing FeFETs Performance and Reliability

Although ferroelectric materials and devices have made remarkable progress in recent years, ferroelectric transistors still face several critical reliability challenges that hinder their scalability, stability, and suitability for large-scale integration and commercial applications. Fatigue, induced by repeated polarization switching, progressively reduces the switchable polarization through defect generation, domain-wall pinning, and charge

injection into the ferroelectric or adjacent dielectrics, thereby narrowing the memory window and increasing write failure probability.[64] This degradation limits the number of reliable program/erase cycles and constrains array endurance and refresh strategies, especially in high-endurance applications such as byteaddressable nonvolatile memories and synaptic devices. Imprint effects, arising from asymmetric charge trapping, pinned domain configurations, or unequal electrode/ferroelectric interfaces, cause quasi-permanent hysteresis loop shifts that lead to voltage asymmetry, increased read/write disturbances, and drift in cell-to-cell performance.[65] Retention loss is primarily governed by depolarization-field-driven relaxation due to incomplete charge compensation and by charge trapping or leakage in the gate stack, both of which reduce the nonvolatile retention window and compromise the stability of stored information. Furthermore, device scaling involving reduced ferroelectric and semiconductor thickness and shorter gate lengths enhances electrostatic control and supports low-voltage operation but simultaneously amplifies depolarization fields, interface trap effects, and domain instability, making thinner ferroelectric films more prone to wake-up, imprint, and retention degradation.[66,67] In addition, device-to-device and cycle-to-cycle variability remains a major barrier for FeFET-based memory and in-memory computing systems, originating from stochastic domain nucleation, nonuniform trap distributions, and process fluctuations in thickness, composition, and grain structure, which together result in threshold voltage spread, retention dispersion, and endurance variation across arrays.

Overall, the performance and reliability of FeFETs are highly sensitive to material composition, interface quality, contact resistance, and post-fabrication treatment, and while substantial advances have been achieved in improving memory window, endurance, retention, and energy efficiency, further progress requires integrated optimization across materials, interface, and scaling dimensions. The following section systematically reviews recent strategies addressing these reliability challenges through ferroelectric material design, contact and interface engineering, post-deposition thermal treatments, and device scaling approaches.

Ferroelectric Material Optimization: Enhancing the intrinsic properties of ferroelectric materials is fundamental to improving FeFET functionality. Doping strategies such as the incorporation of Zr, Y, or other dopants into $\mathrm { H f O } _ { 2 }$ stabilize the noncentrosymmetric orthorhombic phase, critical for robust ferroelectricity. Yun et al. observed an out-of-plane polarization value of $5 0 ~ \mu \mathrm { C } \cdot \mathrm { c m } ^ { - 2 }$ in Y-doped HfO (111) epitaxial films and estimated the full intrinsic polarization to be 64 $\mu \mathrm { C } { \cdot } \mathrm { c m } ^ { - 2 }$ . The intrinsic value was derived by accounting for the crystallographic orientation, where the measured out-of-plane component corresponds to the projected portion of the spontaneous polarization along the (111) direction. They further demonstrated that the ferroelectric polarization increases with crystallinity, consistent with a structural constraint mechanism that stabilizes the orthorhombic phase.[68] In another approach, as shown in  a, lattice Figure 6expansion by inserting excess Hf(Zr) atoms into vacant sites has been shown to promote rhombohedral phase stabilization and improve both in-plane and out-of-plane polarization.[69]

In addition to chemical doping, defect engineering methods such as light ion bombardment have been employed to

enhance ferroelectric polarization via defect-state modulation (Figure 6b).[70] This process introduces a controlled increase in defect density within the HZO film, which in turn strengthens its ferroelectric response by facilitating domain switching and stabilizing the polar phase. Moreover, structural engineering strategies have further contributed to performance enhancement. Superlattice structures comprising alternating ferroelectric and dielectric layers leverage strain and interface effects to stabilize the ferroelectric phase, improve durability, and suppress leakage currents. Cheema et al. employed $\mathrm { H f } _ { 0 \cdot 5 } \mathrm { Z r } _ { 0 \cdot 5 } { \mathrm { O } } _ { 2 }$ superlattice heterostructures as gate stacks, stabilized by mixed ferroelectric–antiferroelectric ordering, which were directly integrated onto Si transistors and scaled down to approximately 20 $\check { \mathrm { A } } . { } ^ { [ 7 1 ] }$ Furthermore, the construction of $\mathrm { H Z O - Z r O _ { 2 } }$ ferroelectric superlattices enabled fast switching and minimized depolarization fields, thereby reducing both the duration and magnitude of charge injection during polarization switching, improving the endurance, fatigue recovery, and retention characteristics of devices (Figure 6c).

Contact Engineering for Efficient Carrier Injection: High contact resistance or severe Fermi-level pinning (FLP) at metal– semiconductor interfaces in FeFETs increases programming voltages, lowers energy efficiency, and accelerates degradation of the device. Minimizing contact resistance is essential for reducing power consumption and enhancing switching speed in FeFETs. Strategies such as van der Waals contacts, graphene interlayers, edge contact, and semimetallic electrodes reduce FLP and Schottky barriers, thereby lowering contact resistance and improving endurance in switching cycles. For example, indium contacts on WSe channels with HZO gate dielectrics enabled Schottky barrier heights as low as 29.9 meV, promoting efficient hole injection and ambipolar behavior, realizing a high on/off current ratio of 109. [72] Similarly, Song et al. systematically investigated the impact of Ti and In contacts on FeFET performance employing a ferroelectric $\mathrm { A l } _ { 0 \cdot _ { 6 8 } } \mathrm { S c } _ { 0 \cdot _ { 3 2 } } \mathrm { N }$ (AlScN) gate dielectric. Their study revealed that devices with indium contacts exhibited a contact resistance nearly three times lower than those with titanium, leading to a fivefold enhancement in memory ratio.[73] This improvement originates from the lower chemical reactivity of indium with the TMD channel and well-aligned work function. Moreover, the low evaporation temperature of indium minimizes damage to the TMD during metal deposition, effectively suppressing Fermilevel pinning and preserving interfacial integrity.

A raised source/drain structure can also be used to reduce contact resistance. Si et al. used a 10 nm thick raised source/drain structure with a 1 nm ultrathin Indium-Tin-Oxide channel. The device demonstrated a contact resistance as low as 0.15 Ω mm and a contact resistivity as low as $1 . 1 { \times } 1 0 ^ { - 7 } \ \Omega { \cdot } \mathrm { c m } ^ { 2 } . ^ { [ 7 4 ] }$ More advanced approaches exploit programmable Schottky junctions using ferroelectric doping at the contact region. As a typical example, Zhao et al. reported FeFETs capable of dynamic polarity reconfiguration, switching between n-type and p-type states via localized polarization modulation (Figure 6d).[75] These reconfigurable devices expand FeFET applicability beyond memory, enabling adaptive logic, and multifunctional computing paradigms.

Interface Engineering to Suppress Trap States: The interface between the ferroelectric gate and semiconductor channel is often the origin of reliability issues such as threshold voltage drift, endurance degradation, and hysteresis asymmetry.

![](images/e5640d20d286e6a7d66a9d464749cdb99d5395f60535952c1ca16b25e6e7aa51.jpg)  
a

![](images/0b4f20e773afd1566c87246d9bea0f05aa1e02fe65cd5688f58045a5cd97d53b.jpg)  
b   
C

![](images/613dd6029b94cda295db16e879a580ff5ff56eadc761b4d87b6640c3ed7a700d.jpg)

d   
![](images/d9526013195187f8a4ef5ce84e43e022d9a62a6750c7d221acc6d5f942e9163b.jpg)  
Electron doping Hole doping

![](images/a03f739bc8fcb4e505e4c28862fd8dadc4c0155725bee83bc06909dc5a3270a0.jpg)  
Contact Engineering

![](images/e7719aa4c58cb19aeefd37f3138b8440052e26828697ee1c4c54a390fa3ce680.jpg)  
  
Interface Engineering

![](images/e43d4e0ce67442e39d6e4e0f1827b6446f2ef3e88ec69710236e66376b40a23c.jpg)  
f   
Annealing

![](images/cdea740cf76a5ea11ba2d6cadb0234cc5cf063fc156e22a20f976e269210554f.jpg)  
  
Plasma   
Figure 6. Schematic diagram of methods to improve the performance of FeFETs. a) Doping excess Hf(Zr) atoms into vacancies to expand the lattice and improve ferroelectricity.[69] b) Light ion bombardment for precise modulation of HZO polarization.[70] c) Superlattice design to induce interfacial strain and stabilize the ferroelectric phase.[180] d) Band diagrams of ${ \bf \dot { M } o T e } _ { 2 }$ at equilibrium with channel electron-doped. The dashed line represents the Fermi level in the MoTe2.Red and green fill colors are used to represent electron doping and hole doping, respectively.[75] e) Flexible FeFET structure with ultrathin AlOx interlayer to improve semiconductor/ferroelectric interface.[76] f) Post-annealing under high-temperature and high-pressure gas to enhance crystallinity and polarization.[82] g) Schematic diagram of the plasma post-processing process of devices.[84] a) Reproduced with permission.[69] Copyright 2023, The American Association for the Advancement of Science. b) Reproduced with permission.[70] Copyright 2022, The American Association for the Advancement of Science. c) Reproduced with permission.[173] Copyright 2025, John Wiley and Sons. d) Reproduced with permission.[75] Copyright 2021, American Chemical Society. e) Reproduced with permission.[76] Copyright 2018, IEEE.

As mentioned before, the coupling between ferroelectric and semiconductor capacitance plays a key role in the performance of FeFET. Tailoring the dielectric stack and reducing the interface trapping sites can further enhance the stability and efficiency of devices. Incorporating a high-k interfacial layer has proven effective in reducing interface trap densities and improving electric field distribution, which suppresses leakage and enhances polarization coupling, enabling larger memory windows and lower switching voltages. For instance, ultrathin $\mathsf { A l O } _ { \mathrm { x } }$ interlayers in organic FeFETs enable both enhanced mobility and memory retention, making them suitable for flexible electronics (Figure 6e).[76] Similarly, Jeong et al. demonstrated that coating the surface of a ${ \bf B a } _ { 0 } . . _ { 7 } { \bf S r } _ { 0 } . . _ { 3 } \mathrm { T i O } _ { 3 }$ (BST) dielectric with a

5.5 nm poly(methyl methacrylate) (PMMA) brush effectively improved surface smoothness, enabling ultra-low-voltage operation of $\mathrm { ~ M o S } _ { 2 }$ FETs at 0.5 V.[77] Notably, Lin et al. showed that transferring freestanding HZO membranes onto molybdenum disulfide $( \mathrm { M o S } _ { 2 } )$ as high-k ferroelectric top-gate dielectrics enables effective suppression of interfacial trap states, attaining an interface state density $( \mathrm { D } _ { \mathrm { i t } } )$ of ${ \approx } 9 { \times } 1 0 ^ { 1 0 } \ \mathrm { c m } ^ { - 2 } \ \mathrm { e V } ^ { - 1 }$ , a value approaching CMOS technology standards.[78]

Improving the intrinsic quality of the interfacial layer also contributes to better endurance and stability. Scandium incorporation in the gate stack has also been shown to thin the interfacial $\mathrm { S i O _ { x } }$ layer while maintaining long-term endurance, as demonstrated in over $1 0 ^ { 1 0 }$ switching cycles.[79] In another

approach, decoupled plasma nitridation was employed to form a SiON interlayer. Compared to conventional $\mathrm { S i O } _ { \mathrm { x } } ,$ , the SiON interlayer exhibited a lower interface state density $( \mathrm { D } \_ { \mathrm { i t } } )$ at the $\mathrm { I L } / \mathrm { S i }$ interface, suppressed ion-induced degradation and subthreshold swing deterioration, and improved long-term device durability under equivalent electric fields.[80]

Post-Fabrication Treatments: Post-deposition treatments such as annealing and plasma exposure are critical for activating ferroelectricity and improving long-term reliability. These techniques can promote ferroelectric phase formation, passivate interface defects, and enhance overall electrostatic stability. Appropriate annealing processes facilitate the crystallization of ferroelectric phases and improve polarization characteristics. However, the thermal budget must be carefully managed, as excessive annealing temperatures may induce unwanted interfacial layer formation and increase interface state density, ultimately degrading device performance.[81]

Wake-up-free and highly durable HZO-based ferroelectric field-effect transistors (FeFETs) have been demonstrated through high-pressure annealing (HPA) on silicon-on-insulator substrates. After metal contact formation, annealing at $4 5 0 ~ ^ { \circ } \mathrm { C }$ under a forming gas (Ar 96%, H 4%) atmosphere at 20 atm for 30 min has been shown to eliminate wake-up effects and enhance polarization in HZO films without compromising BEOL compatibility (Figure $6 \mathrm { f } ) . ^ { [ 8 2 ] }$ High-pressure hydrogen annealing (HPHA) applied to HfO -based MFIS FeFETs effectively passivated trap sites near both the HfO /interfacial layer (IL) and $\mathrm { I L } / \mathrm { S i }$ interfaces, thereby improving IL quality and long-term reliability.[83] To minimize thermal budgets, microwave annealing offers a low-energy alternative for crystallization. Additionally, hydrogen-rich environments can passivate interface defects, improving subthreshold swing and extending data retention. Plasma-assisted surface treatment (Figure 6g) is also used to modulate oxygen vacancies and passivate trap states at the FE/semiconductor interface. For instance, $\mathrm { { A r / O } } _ { 2 }$ plasma treatment followed by thermal annealing effectively reduced interface state density in IGZO/HZObased FeTFTs, thereby enhancing memory window and endurance.[84]

Dimensional Scaling of Devices: In FeFETs, device performance is fundamentally governed by the capacitive coupling between the ferroelectric dielectric and the semiconductor channel. Consequently, the thicknesses of both the ferroelectric layer and the semiconductor channel play a decisive role in determining transistor characteristics. Reducing the channel thickness enhances the electrostatic coupling between the ferroelectric polarization and channel carriers, leading to a pronounced thresholdvoltage shift and an enlarged memory window.[85,62] Atomically thin channels further suppress bulk screening, thereby preserving the polarization field and improving retention. For instance, Si et al. (2020) systematically investigated indium tin oxide (ITO) transistors gated by HZO and demonstrated that reducing the channel thickness from 2 to 1 nm markedly improved mobility, gate control, and the memory window.[74] Owing to their atomically thin nature, 2D semiconductors such as $\mathrm { M o S } _ { 2 } , \mathrm { W S e } _ { 2 } ,$ and MoTe enable highly efficient ferroelectric–channel coupling, allowing the polarization field to strongly modulate carrier distribution across the entire channel depth. This ultimate scaling ensures nearly complete ferroelectric–semiconductor interaction,

yielding steep subthreshold swings, large memory windows, and precise conductance modulation essential for analog weight updates in neuromorphic applications.

At the same time, scaling the ferroelectric thickness further strengthens the internal electric field, enabling low-voltage (<1 V) polarization switching and ultralow-energy operation. The integration of few-nanometer-thick ferroelectric layers with monolayer semiconductors thus facilitates high-performance, lowpower switching suitable for embedded non-volatile memory.[86] Moreover, shortening the gate length enhances electrostatic control and reduces parasitic capacitance, enabling fast polarization dynamics and high integration density without severe shortchannel degradation, owing to the atomically sharp van der Waals interfaces that mitigate depolarization and interface-trap effects. Wang et.al demonstrated a sub-5 nm gate length device with a metallic carbon-nanotube gate terminal. The short-channel device exhibited an on/off ratio of $1 0 ^ { 5 }$ with a minimum SS of 6.1 mVdec−1, offering an energy-efficient path to sub-5 nm FeFET.[87] The drawback, however, is that the article offers no insight into the memory or retention characteristics of the device. While it is possible to selectively optimize specific performance indicators of FeFETs, achieving balanced enhancement across all key metrics remains challenging.

# 3.2. Ferroelectric Semiconductor Field Effect Transistors

Ferroelectric semiconductor materials uniquely combine ferroelectricity and semiconducting properties, offering great opportunities for the advancement of electronic devices. These materials exhibit not only spontaneous polarization characteristics, enabling the reversal of polarization direction under an applied electric field, but also possess tunable carrier transport properties. Unlike traditional structures based on semiconductor channels and ferroelectric dielectrics, ferroelectric semiconductor field-effect transistors (FsFETs) integrate ferroelectric semiconductors as channel materials with well-established dielectric gating technologies. By replacing the conventional ferroelectric dielectric/semiconductor interface with high-quality and wellengineered dielectric materials, charge trapping and leakage currents are significantly mitigated. In FsFETs, ferroelectric semiconductors typically serve as conductive channels, necessitating a balance between robust ferroelectric polarization and high carrier mobility.[88] Below, we classify ferroelectric semiconductor materials suitable for channel applications based on their dimensionality:

# 3.2.1. Device Structure

3D Ferroelectric Semiconductor Transistors: Traditional ferroelectric crystals, such as lithium niobate $\left( \mathrm { L i N b } \mathsf { O } _ { 3 } \right)$ and BTO, typically exhibit large bandgaps and low intrinsic carrier concentrations, making them unsuitable as conductive channels for field-effect transistors. However, through doping or the introduction of defects, perovskite crystals can simultaneously achieve ferroelectricity and high carrier mobility. In 2024, Li’s group transformed a tin-based perovskite semiconductor thin film into a ferroelectric semiconductor thin film by doping with

<table><tr><td colspan="3">Ferroelectric Semiconductor FETs</td></tr><tr><td>3D</td><td>2D</td><td>1D</td></tr><tr><td>a
HfO2
Pd-Si
G
VGS</td><td>b
Graphite Vtg
h-BN
d1
Graphite
3R-MoS2
d2
Graphite Vbg</td><td>c
Au/Ti
Gate H-BN
Au/Ti
Source
90 nm SiO2</td></tr><tr><td>104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
104
104
106
108
10</td><td></td><td></td></tr></table>

Figure 7. FsFETs with different dimensions of ferroelectric semiconductor as the channel. a) 3D ferroelectric semiconductor FET and its transfer curves.[44] b) 2D van der Waals ferroelectric semiconductor FET, realizing fatigue-resistant polarization reversal.[94] c) 1D ferroelectric Te nanowires semiconductor FET and its hysteresis loops.[95] a) Reproduced under the terms of the CC BY license.[44] Copyright 2025, Springer Nature. b) Reproduced with permission.[94] Copyright 2024, The American Association for the Advancement of Science. c) Reproduced with permission.[95] Copyright 2024, Springer Nature.

2-methylbenzimidazole. The reconfigured ferroelectric semiconductor exhibited a high Pr of 23.2 μCcm−2. Utilizing the ferroelectric perovskite as a semiconductor layer, a bottom-gate top-contact transistor was constructed, exhibiting a typical ptype transfer curve with ferroelectric clockwise hysteresis loops ( a).[44] Notably, transistors based on perovskite ferroelec-Figure 7tric semiconductors demonstrated a low subthreshold swing of 67 mVdec−1, further highlighting the advantages of incorporating ferroelectricity.

Although high-performance ferroelectric semiconductors have been successfully achieved through doping engineering, their miniaturization process remains severely constrained by the critical size effect.[89] When the thickness of 3D ferroelectric semiconductor crystals is reduced to the nanoscale, the material suffers from significant degradation in ferroelectric properties due to the enhanced depolarization field. This challenge makes overcoming the critical size effect in ferroelectric semiconductors an urgent technical bottleneck that must be addressed in current research.

2D Ferroelectric Semiconductor Transistors: The 2D materials exhibit atomic-scale thickness, with interlayers bonded via van der Waals interactions, enabling facile exfoliation into singlelayer structures. Recent studies have confirmed that multiple 2D materials retain intrinsic ferroelectricity even when their thickness is reduced below 10 nm, which effectively overcomes the critical size effect.

The room-temperature ferroelectricity in the 2D material ??- $\mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ was first predicted by Zhu’s group in $2 0 1 7 , ^ { [ 9 0 ] }$ and then experimental evidence confirmed that the layered 2D material ??- In Se indeed exhibits room-temperature ferroelectricity.[91] The origin of ferroelectricity lies in the significant difference in interlayer spacing between the central Se layer and the adjacent two In layers, which disrupts the central symmetry. Thanks to its excellent carrier mobility and the ability to maintain ferroelectricity even at a few atomic layers thick, ??-In Se is highly suitable to serve as a conductive channel for FETs. In 2019, the first ferroelectric field-effect transistor structure using $\alpha { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ as the channel was successfully realized.[92] The device demonstrates outstanding electrical characteristics, including a remarkably wide memory window, an exceptionally high maximum drain current of $6 7 1 \mu \mathrm { A } \mu \mathrm { m } ^ { - 1 }$ 1, and an impressive on/off ratio exceeding 108. Furthermore, it exhibits superior electron mobility, with field-effect mobility $( \mu _ { \mathrm { F E } } )$ reaching 312 cm2 V−1 s−1 in the forward sweep and an even higher value of 488 cm2 $\mathrm { V } ^ { - 1 } \thinspace \thinspace \mathbf { s } ^ { - 1 }$ in the reverse sweep, indicating excellent charge transport properties.

Although the thickness scaling limitation has been addressed, the retention characteristics of ferroelectric semiconductors are still plagued by fatigue effects arising from progressive defect aggregation. 2D sliding ferroelectric materials achieve ferroelectricity through interlayer sliding while retaining semiconducting properties. Unlike traditional ferroelectric materials that rely on lattice distortions, sliding ferroelectricity primarily originates

from the relative displacement of atomic layers in 2D materials. This provides a novel perspective for addressing the fatigue effects in ferroelectric semiconductors.

Liu’s group has conducted a series of progressive research in the field of sliding ferroelectricity in recent years. In 2022, Liu et al. fabricated dual-gate FETs using 3R ${ \mathrm { M o S } } _ { 2 }$ flakes of varying thicknesses to observe polarization switching in sliding ferroelectrics, discovering intermediate polarization states during the switching process.[93] This study revealed the critical role of layer number and interlayer dipole coupling in sliding ferroelectrics, providing new insights for designing novel sliding ferroelectric devices. Then in 2024, Liu’s team further proposed a ferroelectric memory device transistor based on sliding ferroelectricity, demonstrating excellent fatigue resistance with a stress time of up to $1 0 ^ { 5 }$ s (Figure 7b).[94] Theoretical calculations indicated that due to the ultra-low switching barrier and strong in-plane stiffness of $3 \mathrm { R - M o S } _ { 2 }$ , charge defects do not accumulate at domain walls during repeated polarization reversals under cyclic electric fields, resulting in fatigue-free behavior in bilayer 3R-MoS . The system exhibited exceptional endurance, maintaining stable operation over $1 0 ^ { 6 }$ program/erase cycles under ultrafast switching pulses as short as 53 ns without observable fatigue. This property provides crucial support for overcoming key challenges in the practical application of ferroelectric devices.

1D Semiconductor Transistors: Researchers have been striving to overcome the critical size effect in ferroelectric semiconductors, and the dimensional limitations of ferroelectric semiconductors have now been successfully pushed down to the 1D scale. In 2024, Jiang’s team reported the observation of roomtemperature ferroelectricity, piezoelectricity, and resistive switching behavior in single-element tellurium (Te) nanowires.[95] They discovered room-temperature vertical ferroelectricity in quasi-1D Te nanowires and at the edges of Te nanosheets. The vertical ferroelectricity is attributed to atomic displacements perpendicular to the atomic chains within the Te nanowires, a mechanism further validated by density functional theory (DFT) calculations. Additionally, the study utilized Te nanowires as ferroelectric semiconductor channels to construct self-gated FsFETs with h-BN as the gate dielectric (Figure 7c), realizing continuousvariable resistive states with fast response and high-density storage capabilities. Noted that the research on FsFETs remains in its infancy. To date, most reported studies have focused on 2D ferroelectric semiconductors, while investigations into their 3D and 1D counterparts are still scarce. This emerging field thus offers substantial opportunities for exploration and innovation.

# 3.2.2. Operating Principles

Ferroelectric dielectric transistors place the ferroelectric layer in the gate stack, modulating channel conductance via polarization fields, offering better CMOS compatibility. In contrast, ferroelectric semiconductor transistors integrate ferroelectric materials as the channel layer, combining conductivity and polarization to directly modulate carrier transport. The defining feature of ferroelectric semiconductors lies in the intrinsic correlation between their polarization and charge carrier transport characteristics. The spontaneous polarization of the material generates bound charges at the surface, which can effectively modulate the con-

centration and distribution of charge carriers in the semiconductor channel. When the polarization direction is altered, both the sign and magnitude of these surface-bound charges change accordingly, allowing for precise control over the channel conductivity.

Si et al[92] have experimentally elucidated the interaction between polarization and gate-controlled electric fields in ferroelectric semiconductors. Their research revealed that in ??-In Se ferroelectric semiconductor-based transistors, the electric field intensity modulated by gate dielectric equivalent oxide thickness (EOT) critically governs polarization switching dynamics. At high EOT regimes, the lateral electric field suffers from dielectric screening effects, confining ferroelectric domain reversal predominantly near the $\alpha { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ bottom region. When EOT decreases, enhanced vertical electric fields drive complete ferroelectric switching throughout the ??-In2Se3 channel. In this regime, the P-up state enables carrier accumulation at the top interface (LRS), while the P-down state corresponds to HRS, producing counterclockwise Id-Vg hysteresis. This EOT-dependent transport behavior inversion mechanism provides crucial insights for polarization engineering in ferroelectric transistors.

In 2023, Zhou’s group[96] elucidated the polarizationdependent conductivity mechanism in FsFETs. They revealed that the ferroelectric built-in electric field in ferroelectric semiconductor induces asymmetric conductive pathways via a hidden Stark effect, while also competing with potential redistribution caused by external gate electric fields ( a). When the Figure 8polarization is oriented upwards, the conductive path deviates from the bottom gating dielectric, causing the gate electric field to influence the potential along the conductive path less efficiently compared to the downwards polarization, resulting in the threshold voltage being right-shifted with downward polarization state (Figure 8c upward). Conversely, from the perspective of potential redistribution, the downward band bending in the polarization up state implies an earlier switching ‘on’ than that in the polarization down state when increasing the bottom gate voltage (Figure 8b). This indicates that the $\mathrm { V _ { t h } }$ in the upward polarization state is positioned to the left of that in the downward polarization state (Figure 8c below). By leveraging the underlying physical mechanism described in this work, the researchers achieved precise control over the conductivity threshold in ??-In Se -based FsFETs.

In summary, the ferroelectric dielectric FETs and ferroelectric semiconductor FETs differ fundamentally in their polarizationchannel coupling mechanisms, resulting in distinct performance characteristics. In ferroelectric dielectric FETs, the ferroelectric layer acts as a gate insulator, where polarization-bound charges at the dielectric/semiconductor interface electrostatically modulate the surface potential. This interface-controlled process can utilize the negative capacitance effect to achieve low subthreshold swing and low-power operation, but device performance is limited by interface quality, capacitance matching, and polarization retention. In contrast, ferroelectric semiconductor FETs employ semiconducting channels with intrinsic polarization, enabling direct modulation of band edges and carrier distribution through polarization reversal. This internal coupling enhances current controllability, switching speed, and scalability, while allowing both clockwise and counterclockwise hysteresis depending on band alignment.

# Ferroelectric Mechanism in 2D Ferroelectric Semiconductor FETs

![](images/01c3341ab84ab80dcc0f4e92dd931f08c769d09557c1a65ebd70bd84b4ae655a.jpg)  
a

![](images/21b8b123f7c1f109325e945213161974d31fb645c7cc829707e66b2c03ef407a.jpg)  
b

![](images/0f6c451a0f7198823baf1465f89f713d3971afb366876ad20a3efcd455b15468.jpg)  
C

![](images/e4687e979a11895096759d2715077bf28f26e87484867bda11cad9e9823fbcb3.jpg)  
Figure 8. Ferroelectric and charge transport mechanism of 2D ferroelectric semiconductor FETs. a) Transmission eigenstate of the ??-In $\phantom { } _ { 2 } \mathsf { S e } _ { 3 }$ transistor in the polarization up and down states. b) Average Hartree difference potential of the bottom-gated transistor in the polarization up and down states. c) Shift of the threshold voltage in the transfer characteristics.[96] a–c) Reproduced with permission.[96] Copyright 2023, Springer Nature.

# 4. Functional Applications of Ferroelectric Transistors

# 4.1. Non-Volatile Memory Applications

With the rapid rise of data-centric applications, a significant challenge faced by modern memory technologies is the efficient storage of the exponentially increasing volume of data. Embedded static random-access memory (SRAM), widely utilized in integrated circuits at the 28 nm process node, is a conventional memory solution.[97] However, SRAM is volatile and constrained by its relatively large cell size, limiting its ability to store large amounts of data. In contrast, dynamic random-access memory (DRAM) offers higher storage density but suffers from inherent volatility and substantial power consumption due to the need for periodic data refresh cycles. A cornerstone of non-volatile memory (NVM) technology is the embedded flash memory, which relies on floating-gate (FG) transistors. While FG-based flash memory has been a standard solution, its development has stagnated, particularly as process nodes scale down to 28 nm.[98] This slowdown is primarily attributed to technical limitations and performance bottlenecks. As the dimensions of the FG memory shrink, the ability of the gate to control the channel weakens, resulting in leakage of stored charge and a significant reduction in memory endurance (104 cycles). Furthermore, the necessity of a tunneling layer to facilitate charge storage in FG memory increases the operating voltage, often reaching as high as 12 $\mathrm { V . } ^ { [ 9 9 ] }$ These high voltages, coupled with poor endurance, make FG flash memory incompatible with logic processors, necessitating the inclusion of charge-pump circuits and complex caching techniques.

In recent years, ferroelectric transistors have emerged as a promising alternative for embedded non-volatile memory applications, driven by the non-volatile nature of ferroelectric ma-

terials, which retain their polarization state even after the removal of an applied electric field. To store information, the ferroelectric material generates upward and downward-polarized electric fields under different directions of applied voltage, resulting in the drift of the threshold voltage in the ferroelectric transistors, which enables the writing and erasing of information.

# 4.1.1. Inorganic Ferroelectric Transistor Memory

Perovskite Oxide-Based Ferroelectric Transistor Memory: With the advancement of ferroelectric materials over recent decades, ferroelectric transistor memories based on various material systems have exhibited distinct characteristics, offering diverse functionalities for memory applications. Resembling a conventional MOSFET with the dielectric replaced by a ferroelectric layer in 1973, Wu et al. developed a bismuth titanate as the ferroelectric component to fabricate a Si-based MFS memory.[100] This architecture initially showed promise for integration into nonvolatile memory technologies. However, significant limitations, such as poor interface quality and ion migration between the ferroelectric and semiconductor layers, resulted in limited endurance performance. In subsequent decades, considerable progress has been made in both device architecture and ferroelectric oxide material development, particularly in perovskite-based systems. Highperformance ferroelectric materials such as PZT and BFO, and $\mathrm { S r B i } _ { 2 } \mathrm { T a } _ { 2 } \mathrm { O } _ { 9 }$ (SBT) have been extensively explored.[17,18] In 2011, Tang et al. introduced a HfTaO buffer layer between SBT and the Si channel, enabling an MFIS FeFET to exhibit a memory window of $1 0 ^ { 7 }$ and endurance over $2 \times 1 0 ^ { 1 1 }$ cycles.[101] More recently, in 2021, Tripathi et al. demonstrated a $\mathrm { T i N } / \mathrm { B F O } / \mathrm { A l } _ { 2 } \mathrm { O } _ { 3 } / \mathrm { S i }$ structure incorporating a 100 nm plasma-enhanced atomic layer

# Inorganic Ferroelectric Transistor Memory

![](images/222cb1198fd40b35e35f4300e3e0179e122c0d9197f7d8d661e3696ce2bf3489.jpg)

![](images/24bcba64b3637694e922eb36bb881c076c7d2e80d284663ce339793a444f5b9c.jpg)

![](images/dd1cc6394ad56d8e17fad4d83393e8697fd969d8942c38b311311291b14543c7.jpg)

![](images/85158ee11e843a83307797238fdad2a0f9be27ddbfb58f633015ad2403f433e3.jpg)

![](images/4d67eebe67cf12a4dc1c1bf40f56eef897f9aa27b9b77a67de5a64a8c5d9ee46.jpg)

![](images/e486c5cbd9520ce5924b9c6f8072d911ceaa4201f89443ba809d701b3a2caf14.jpg)

![](images/f0f31c867398a417ae85419bc0f167445b47a738afe4d6320dc6634b20c28532.jpg)

![](images/83c35d283ba452668c40b389267163542433598b5bdc467bb69a954f10b68694.jpg)

![](images/834e06dbbbc5785e5b23b0189519f6ee8ad49057e10c6c1836e64dc7e08dc100.jpg)  
Figure 9. Applications of ferroelectric transistors in non-volatile memory based on inorganic ferroelectric material. a) Schematic of a SrTiO3 (STO)-based ferroelectric transistor. b,c) Cycle endurance and memory retention of STO-based memory device.[104] d) Schematic of an HZO-based MFMIS ferroelectric transistor memory. e) Memory window evolution over long-term testing. f) Cycle endurance with different pulse widths.[111] g) Device structure of 2D CIPS-based ferroelectric transistor. h) transfer curves of the 2D CIPS-based ferroelectric transistor. i) Demonstration of four-bit multi-level memory with a 100 ns pulse width.[118] (a–c) Reproduced with permission.[104] Copyright 2024, Springer Nature. d–f) Reproduced with permission.[111] Copyright 2024, The American Association for the Advancement of Science. g–i) Reproduced under the terms of the CC BY license.[118] Copyright 2021, Springer Nature.

deposited (PEALD) ${ \mathrm { A l } } _ { 2 } { \mathrm { O } } _ { 3 }$ interlayer, which effectively enhanced the memory window from 4.75 to 8.53 V and yielded outstanding fatigue resistance with negligible polarization degradation even after $1 0 ^ { 1 2 }$ write–erase cycles.[102] These findings highlight the efficacy of high-k buffer layers in mitigating charge injection and suppressing interfacial diffusion, thereby significantly improving endurance characteristics in perovskite-based FeFETs. Except for the insertion of a high-k buffer layer, in 2023, Ren. et al. develop a polarized tunneling transistor using a PZT-enabled ${ \mathrm { M o S } } _ { 2 }$ field-effect transistor, which achieves ultrafast nonvolatile memory performance without the need for a traditional tunnel or floating-gate layer. By leveraging the ferroelectric polarization of PZT and the surface traps for charge storage, the device exhibits a program/erase speed of $2 5 / 2 0$ ns and 10-year data retention.[103]

With advances in thin-film growth, exfoliation, and transfer techniques, freestanding perovskite ferroelectric films have garnered growing interest for applications in flexible electronics, neuromorphic memory, and quantum information technologies. As shown in a, Das et al. reported a multifunctional fer-Figure 9roelectric transistor composed of a freestanding incipient ferroelectric $\mathrm { S r T i O } _ { 3 }$ coupled with a MoS channel in 2024.[104] The device exhibited nonvolatile ferroelectric switching at cryogenic temperatures (below 100 K), achieving ultrafast switching speeds of 10 ns, endurance of $1 0 ^ { 4 }$ cycles, and 32 distinct multilevel states (Figure 9b,c). At room temperature, the incipient ferroelectricity transitioned to a volatile regime, enabling reservoir computing for pattern recognition. Despite the advantages of perovskite ferroelectrics, such as large remanent polarization, low leakage

current, and excellent endurance, several critical challenges remain. These include thermal instability under CMOS-compatible processing conditions, difficulty in achieving atomically sharp interfaces, and the necessity of thick (>100 nm) ferroelectric films to maintain polarization stability and suppress leakage currents, which hinders scalability in advanced technology nodes. Although recent studies have reported the realization of ultrathin (≈1 nm) ferroelectric bismuth oxide films via samarium doping, their viability in high-performance devices remains to be comprehensively evaluated.[105]

Hafnium-Based Ferroelectric Transistor Memory: The rapid development of integrated circuits has shortened the gate length in transistors to increase the integration (16 nm in 3 nm technology node). This requires that the transistor dielectric and semiconductor layers be thin enough to provide good gate control. Originally, due to the thickness of the perovskite and organic ferroelectric layers, ferroelectric transistors have been difficult to use in modern integration processes and can only be used in specific application scenarios. Fortunately, the emergence of Si-doped induced hafnium-based ferroelectric materials in 2011 has provided confidence in the research of ferroelectric transistor memories and started a second wave of intensive research.[106] As $\mathrm { H f O } _ { 2 }$ has been widely used in the semiconductor industry as a gate dielectric in high dielectric constant metal gate MOSFETs since Intel introduced it into the fabrication process in $2 0 0 7 , ^ { [ 1 0 7 ] }$ hafnium-based ferroelectrics are fully CMOS process compatible. In addition, hafnium-based ferroelectric materials can be deposited in a variety of ways, such as CVD, PLD, and ALD, and the materials have low dielectric constants, which means that in the ultrathin limit, their depolarization field is smaller and thus easier to maintain the polarization state providing the possibility of preparing large-scale homogeneous and ultrathin ferroelectric films.

Over the past decade, significant progress has been made in enhancing the performance of HfO -based ferroelectric transistor memories through strategies such as dopant engineering, strain modulation, structural design, and thermal processing. Doping with elements including Si, Zr, Y, Al, La, Gd, and Sr has been instrumental in stabilizing the orthorhombic ferroelectric phase. Among these, HZO is the most widely adopted system. Notably, in 2017, Karbasian et al. systematically demonstrated the effect of Zr doping, from 0% to 100%, and annealing temperature on ferroelectric/antiferroelectric behavior of $\mathrm { H f O } _ { 2 }$ film through phase engineering. The results indicate that 50% Zr-doping with high-temperature annealing $( 7 0 0 ~ ^ { \circ } \mathrm { C } )$ stabilizes the ferroelectric orthorhombic phase, while 70% Zr-doping induces tetragonal phase antiferroelectricity.[108] Building on this material’s foundation, high-performance FeFETs based on HZO have been demonstrated with full CMOS compatibility. For instance, Slesazeck et al. (2019) successfully fabricated HZO-based FeFETs using a 28 nm high-k metal gate process, achieving a memory window of 3 V, excellent high-temperature data retention $( 3 0 0 ~ ^ { \circ } \mathrm { C } )$ , and endurance of 105 cycles.[109] This poor cycle endurance can be ascribed to the ion diffusion and charge trapping in the ferroelectric-semiconductor interface.

The introduction of a suitable interfacial layer (e.g., SiO , $\mathrm { A l } _ { 2 } \mathrm { O } _ { 3 } ,$ or $\mathrm { L a } _ { 2 } \mathrm { O } _ { 3 } )$ between the ferroelectric film and the channel can further enhance interface quality, suppress charge trapping, and improve retention. In 2021, Zhou et al. demonstrated

that inserting a $\mathrm { Z r O } _ { 2 }$ seed layer between HZO and Si not only inhibits the formation of non-ferroelectric monoclinic phases but also reduces interface trap densities, thereby expanding the memory window from 0.8 to 1.4 V and significantly improving endurance by an order of magnitude.[110] Recently, by introducing a floating metal layer between the ferroelectric and insulating layers, the MFMIS design enables improved capacitance matching between the ferroelectric and semiconductor capacitors, thereby effectively stabilizing polarization and enhancing retention. Additionally, unlike conventional stacks, the areas of the MFM and MIS capacitors in MFMIS devices can be independently engineered, offering further design flexibility. Recent studies demonstrated that increasing the MIS/MFM capacitance ratio from 8 to 32 boosts the memory window from 1 to 2.8 V while preserving retention and endurance.[58] In a representative example, Ren et al. (2024) reported a high-performance FeFET with a TiN/ $\mathrm { H Z O / T i N / H f O } _ { 2 } / \mathrm { M o S } _ { 2 }$ device structure as shown in Figure 9d. [111] The HZO layer was activated via rapid thermal annealing at $5 0 0 ~ ^ { \circ } \mathrm { C } ,$ , followed by the deposition of a 15 nm high-k ${ \mathrm { H f O } } _ { 2 }$ dielectric. The ${ \mathrm { M o S } } _ { 2 }$ channel was solutionprocessed with precise thickness control to ensure uniformity and high yield. By tuning the MFM-to-MIS area ratio from 3.6 to 14.2, a memory window of up to $4 . 7 \mathrm { ~ V ~ }$ was maintained even after one year of testing (Figure 9e). The device achieved excellent electrical characteristics, including an on/off current ratio exceeding $1 0 ^ { 7 }$ , sub-30 ns switching speed, and endurance over $1 0 ^ { 1 2 }$ cycles (Figure 9f). The wafer-scale yield of 96.36% underscores the feasibility and reliability of the MFMIS structure for large-scale integration in computing-in-memory hardware. In addition to planar structures, HfO -based FeFETs have been successfully integrated into FinFET, vertical gate-all-around (GAA) architectures, and 3D integration processing, further enhancing memory density and integration capability.[63,112] However, key challenges remain, including wake-up and fatigue phenomena, retention degradation from charge trapping, limited memory window, and device variability driven by stochastic ferroelectric phase nucleation.[113] Addressing these challenges will require continued advances in grain boundary engineering, interface design, and a deeper understanding of defect-mediated switching mechanisms.

2D Ferroelectric Transistor Memory: Although HfO -based ferroelectrics can retain robust ferroelectricity at sub-10 nm thickness and are compatible with CMOS processes, they remain fundamentally bulk materials. As their thickness approaches the atomic scale, ferroelectricity becomes increasingly unstable due to the emergence of depolarization fields, interface-induced degradation, and polarization fatigue. In contrast, the emergence of intrinsic ferroelectricity in several 2D vdW materials, such as $\alpha { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 } , \mathrm { \Lambda } ^ { [ 8 8 , 1 1 4 ] } \mathrm { C I P S } , \mathrm { \dot { \mathrm { \Omega } } ^ { [ 2 5 ] } }$ and $\mathsf { S n S } ^ { [ 1 1 5 ] }$ down to the monolayer limit, offers a feasible pathway toward scaling ferroelectric devices to the ultimate thickness and integration density. The weak interlayer vdW interactions in these materials enable the retention of spontaneous polarization without requiring mechanical clamping or epitaxial strain, fundamentally overcoming the critical thickness limit faced by conventional ferroelectrics. In addition, the inherently weak electrostatic screening in 2D materials allows the ferroelectric polarization to exert a pronounced influence on carrier distribution in the adjacent semiconducting layers,

enabling efficient modulation of charge density, carrier type, and transport properties.

Despite rapid advances in the synthesis and integration of 2D ferroelectrics, their development remains in its infancy compared to conventional bulk ferroelectric materials. Only a limited number of 2D compounds exhibit robust ferroelectricity at room temperature, among which CIPS and $\mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ are the most widely studied. In $^ { 2 0 1 6 , }$ via utilizing the van der Waals layered structure to suppress the depolarization field, Liu et al. experimentally demonstrated stable room-temperature ferroelectricity in CIPS nanosheets with one unit cell thickness (1.6 nm),[25] overcoming the critical thickness issue existing in traditional ferroelectrics.[116] Subsequent studies confirmed that the out-ofplane polarization in CIPS can effectively modulate carrier density in adjacent semiconductor channels, thereby enabling nonvolatile data storage in FeFETs. In 2018, Si et al. reported a prototypical 2D/2D FeFET based on a CIPS/MoS van der Waals heterostructure, in which CIPS acts as a ferroelectric gate insulator atop the ${ \mathrm { M o S } } _ { 2 }$ channel.[117] The device exhibits a clear counterclockwise hysteresis loop in its transfer characteristics, confirming stable ferroelectric switching and reliable non-volatile memory behavior. Additionally, the device performance can be tuned via a back-gate bias, enhancing its on/off current ratio. To further enhance device performance, the MFMIS device structure has also been explored in 2D FeFETs. As shown in Figure 9g, in 2021, Zhou et al. demonstrated a high-performance ferroelectric memory cell featuring an all-van der Waals heterostructure composed of CIPS/graphene/h-BN/MoS , where the graphene layer functions as a floating gate. This architecture achieves a typical n-type anticlockwise hysteresis and excellent metrics, including a program/erase speed under 5 μs, endurance exceeding 104 cycles, and data retention beyond 10 years (Figure 9h). Impressively, the device supports multi-level cell operation (four-bit/cell) and sub-100 ns polarization switching enabled by the weak interlayer coupling and clean interfaces intrinsic to van der Waals engineering (Figure 9i).[118]

In recent years, the exploration of sliding ferroelectricity in 2D materials has opened new avenues for developing nonvolatile memories.[119] A representative example is the dual-gate fatigue-resistant ferroelectric transistor memory based on 3R-MoS as mentioned before, which demonstrated an impressive endurance of 106 cycles, albeit with a relatively narrow memory window.[94] In 2024, Zhang et al. employed a singlegate $3 \mathrm { R } { \cdot } \mathrm { M o S } _ { 2 }$ slide ferroelectric transistor, achieving a significantly larger memory window of 8 V and robust retention exceeding 10 years. The device exhibited a clockwise hysteresis loop, attributed to the sliding ferroelectric polarization in Rstacked bilayer ${ \mathrm { M o S } } _ { 2 } .$ , which modulates the channel carrier density through threshold voltage reconfiguration rather than conventional charge trapping.[120] Despite these advantages, current challenges for sliding ferroelectrics include their low polarization strength and the difficulty of scalable material synthesis.

# 4.1.2. Organic Ferroelectric Transistor Memory

The rapid evolution of AI and edge computing has imposed stringent requirements on memory technologies, particularly for applications necessitating low power consumption, mechanical

flexibility, and biocompatibility. Organic ferroelectric transistor memories (OFTMs), based on polymers such as (P(VDF-TrFE)), have emerged as promising candidates to meet these demands due to their intrinsic flexibility, low-temperature solution processability, and tunable electronic properties. These characteristics render OFTMs particularly attractive for next-generation wearable electronics, implantable devices, and flexible AI hardware, where lightweight and conformable memory systems are essential for continuous physiological monitoring and real-time data processing.[121,122] The groundbreaking OFTM was prepared by Naber et al. in 2005 using P (VDF-TrFE) as the ferroelectric insulating layer through spin coating.[123] The device exhibited a memory window of 104, switching speed of 50 μs, and retention exceeding $6 \times 1 0 ^ { 5 } \mathrm { ~ s ~ }$ . However, the thick ferroelectric film (≈850 nm) resulted in a high operating voltage (>75 V). Over the past decade, significant advances have been made in improving the performance and energy efficiency of OFTMs. These efforts include the development of low-coercive-field terpolymer ferroelectrics, such as P(VDF-TrFE-CTFE), as well as the introduction of passivation layers, interfacial engineering, and device scaling. In 2017, Wang et al. reported a flexible OFTM incorporating ultrathin AlO interfacial layers on both sides of a P(VDF-TrFE-CTFE) film with a minimum thickness of 40 nm. This design significantly suppressed gate leakage current and reduced the operating voltage to as low as 4 V, while maintaining robust memory performance under 7500 mechanical bending cycles at a bending radius of 5.5 mm.[124] Building on this work, the same group later demonstrated a two-bit organic non-volatile memory utilizing ultraviolet–ozone (UVO) treated P(VDF-TrFE-CTFE) gates. The UVO treatment enhanced carrier mobility and accelerated the program/erase (P/E) switching speed to 5 μs at an operating voltage of 15 V.[125]

Despite notable progress, organic ferroelectric memories still face limitations in terms of data retention (typically $1 0 ^ { 4 } – 1 0 ^ { 6 }$ s) and cycling endurance (on the order of 103), compared to their inorganic counterparts. Nonetheless, their superior mechanical compliance and integrability into unconventional substrates offer distinct advantages. In 2019, Kang et al. reported a fiber-shaped OFTM fabricated through a capillary-tube-assisted coating process that enabled the deposition of a surrounding P(VDF-TrFE) ferroelectric layer onto a silver wire gate electrode ( a).[126] Specifically, a concentric ferroelectric dielectric Figure 10film was uniformly coated around the silver wire using a capillary delivery system, followed by thermal evaporation of pentacene as the organic semiconductor and gold as the source and drain electrodes. The resulting memory device exhibited excellent electrical performance, operating at voltages below 5 V with robust data retention exceeding $1 0 ^ { \hat { 4 } } \mathrm { ~ s ~ }$ . Furthermore, the device maintained stable operation under 100% uniaxial strain, withstanding over 400 cycles of endurance and 2000 bending tests without significant degradation (Figure 10b,c). Benefiting from the intrinsic mechanical compliance of both the ferroelectric polymer and the metallic fiber electrodes, the OFTMs were directly integrated into a woven textile platform using conventional weaving techniques. In 2021, a 10×12 array of fiber-shaped memory transistors was successfully fabricated by the same group, forming a crossbar architecture capable of both non-volatile data storage and real-time physiological signal detection.[127] This work underscores the high application potential of OFTMs in wearable

# Organic Ferroelectric Transistor Memory

![](images/fd1edb196712da7172c6fa943ffedd013893164ddc90a6c7d64e9496b276a694.jpg)

![](images/c5774cf87060ea4a9e133ff3326aa793eddea853ff703098be9e254cad18bf24.jpg)

![](images/a4637d6de7d9265b3beecda26468c9c5a9ab8e2419a717fef49ac8d38c8b9932.jpg)

![](images/32e284d31d1b24e78e214c7f8b6ecae4fcf62c894df3c35bded464c4cf7a9d2c.jpg)

# Organic-Inorganic Ferroelectric Transistor Memory

![](images/57e5084d5aecbe0ddd25be08eccec929b4d3c41b11193343d89ea9a6104d5aed.jpg)

![](images/698b015ef38562f4c213b63c489e52fb2f270b78789038f04cf19fae1d1264c7.jpg)

![](images/f8217a54f0970888c428d407ece2610d7dcdcba86e48a11409db34eb9657d534.jpg)  
Figure 10. Applications of ferroelectric transistors in non-volatile memory based on organic and organic-inorganic-hybrid ferroelectric material. a) Structure of a flexible fiber-shaped organic ferroelectric transistor memory using PVDF-TrFE. b,c) Mechanical bending and cycling endurance performance of the OFTM.[126] (d) Device structure of organic-inorganic hybrid ferroelectric perovskite-based non-volatile memory. e) Double sweep transfer curves of the organic–inorganic hybrid ferroelectric transistor. f) Comparative summary of key memory metrics across different ferroelectric material systems.[129] a–c) Reproduced with permission.[126] Copyright 2019, American Chemical Society. d–f) Reproduced with permission.[129] Copyright 2025, John Wiley and Sons.

neuromorphic electronics and soft human–machine interfaces. Except for the memory performance of a single cell, the uniformity of the OFTM array is also the key point. In 2024, Hu. et.al introduced an organic non-volatile two-transistor memory cell that exploits a NOT-gate-like voltage-divider architecture to deliver binary-level output with self-enhanced noise tolerance. The device uses a ferroelectric polymer gate dielectric (P(VDF-TrFE)) in combination with solution-processed organic semiconductors, enabling complementary switching characteristics with low operating voltage and robust signal stability.[128] This complementary switching enlarges the effective memory-on/off ratio to >105, yields a noise-margin window of ±1 V during program/erase and −7 V during read. Furthermore, the authors demonstrated the scalability and array-level integration potential of this architecture, which can be extended toward wearable, flexible neuromorphic systems and in-memory computing circuits.

# 4.1.3. Organic–Inorganic Ferroelectric Transistor Memory

Organic–inorganic hybrid ferroelectric materials, particularly those based on low-dimensional perovskite structures, have

emerged as promising candidates for next-generation nonvolatile memory and neuromorphic computing applications. These materials combine the mechanical flexibility and tunable chemistry of organic compounds with the robust electronic properties of inorganic components, enabling unique functionalities such as room-temperature ferroelectricity, bandgap engineering, and interface design compatibility with vdW heterostructures. Despite their theoretical advantages, the application of organic–inorganic hybrid ferroelectrics in transistor devices is still in its infancy. Compared to conventional inorganic-based ferroelectrics or polymer ferroelectrics, reports on hybrid perovskite ferroelectrics in practical transistor architectures remain limited. This is largely due to challenges in the small polarization value, phase stability, and interface compatibility. Nevertheless, recent advances have shown that integrating organic–inorganic hybrid ferroelectric materials with atomically thin semiconductors can yield functional vdW heterostructures with ferroelectric modulation capability, paving the way for compact, flexible, and low-power memory devices. In 2024, Xu et.al. synthesized a series of 2D Ruddlesden–Popper hybrid perovskite ferroelectric materials with stable room temperature ferroelectricity.[129] The synthesized hybrid perovskite ferroelectric materials can be

easily exfoliated into monolayer or few-layer flakes and seamlessly integrated with other 2D semiconductors such as MoS to form vdW heterostructure ferroelectric transistors, as shown in Figure 10d. Leveraging the sub-millimeter-scale monolayer processability and tunable ferroelectric properties of the ferroelectric layer, the authors successfully demonstrate unique charge polarity modulation effects and outstanding non-volatile memory characteristics. As shown in Figure 10e, the device exhibited ultra-wide hysteresis windows up to 177 V, high on/off current ratios of 105, fast programming speeds, and robust long-term retention performance.

Benefiting from the semiconductor properties of organicinorganic hybrid ferroelectric perovskite, these materials have excellent photoelectric response and possess unique application potential in photodetection, ferroelectric photovoltaics, and insensor computing. In 2025, Guo et al. reported a 2D organicinorganic hybrid perovskite ferroelectric transistor exhibiting a gate-tunable circular photocurrent effect, which enables multistate, light-controllable nonvolatile memory operation.[130] The device was constructed using a 2D Ruddlesden-Popper ferroelectric perovskite layer as the gate dielectric and active photoresponsive medium, integrated onto a semiconductor channel. By exploiting the interfacial Rashba field that emerges from ferroelectric polarization, they achieve a helicity-dependent circular photocurrent whose magnitude and sign are nonvolatily programmed through ferroelectric domain switching. This intimate marriage of switchable electric dipoles, strong spin-orbit coupling, and broadband light harvesting yields six multilevel memory states, which provide a new paradigm for multi-functional ferroelectric transistors.

Similarly, in 2025, using an organic-inorganic hybrid perovskite (PMA) PbCl as the ferroelectric layer and an organic semiconductor (PDVT-10) as the channel, Guo et al. reported a switchable photodetection-synaptic ferroelectric transistor with color perception capabilities.[131] By coupling ferroelectric polarization modulation with light excitation, the transistor realized distinct positive/negative photocurrent responses to 310, 425, and 808 nm illumination. Furthermore, the ferroelectric transistor array acts as a color-selective neuromorphic retina, which preferentially amplifies the green or brown color channel in real time, enabling a low-power neural network to detect camouflaged objects with accuracy rising from 13% to 99% while cutting latency and energy by 56% and 91%, respectively, compared with a conventional architecture based on electrical synapses.

In ferroelectric transistors, the polarization behavior is often compromised by the shielding effect of defect-trapped charges, resulting in incomplete polarization reversal and unstable hysteresis characteristics. The intrinsic competition between ferroelectric polarization and charge trapping has long posed a fundamental challenge to achieving reliable and high-performance ferroelectric devices. Recently, Li et al. proposed a polarizationdependent modulation mechanism in 2D hybrid perovskite heterojunction ferroelectric transistors. By introducing electrontrapping sites into an organic–inorganic hybrid ferroelectric layer ((EATMP)PbBr ) and integrating TCAD simulations with firstprinciples calculations, they elucidated the competitive coupling between FE and CT and revealed a polarity-dependent reversible transition between the two mechanisms. In n-type MoS channels, the majority electrons enhance charge trapping, forming a

reverse depolarization field that suppresses ferroelectric switching, whereas in p-type BP channels, the hole-dominated transport weakens the trapping effect, allowing polarization reversal. This polarity-dependent control enables a heterogeneous synergy between ferroelectric and trapping dynamics, endowing a single device with both nonvolatile memory and volatile synaptic weight modulation functionalities. Device-informed simulations of transfer learning networks further demonstrate a recognition accuracy of 92.9% and a 20.7-fold enhancement in training efficiency, highlighting the great potential of such ferroelectric heterostructures for energy-efficient neuromorphic computing.[132]

To provide a comprehensive comparison of FeFETs based on diverse ferroelectric systems, we summarize key performance metrics, including memory window, ON/OFF current ratio, switching speed, endurance, and power consumption, in Figures 1,10 and  . Perovskite oxide-based FeFETs mem-Table 3ory exhibits superior retention and endurance due to their robust spontaneous polarization and well-established switching dynamics. However, their relatively thick films and complex crystallographic requirements impose significant challenges for aggressive device scaling and integration into advanced CMOS nodes. In contrast, hafnium-based ferroelectrics have emerged as a CMOS-compatible alternative. Their integration into Fe-FETs has enabled high-performance memory characteristics, yet the practical application is still limited by narrow memory windows and issues related to film uniformity, phase stabilization, and wake-up/fatigue behavior during cycling. Organic ferroelectric materials offer unique advantages for applications requiring mechanical compliance, such as flexible, stretchable, and bio-integrated electronics. Although they typically suffer from lower remanent polarization and reduced endurance compared to their inorganic counterparts. 2D ferroelectric materials represent an emerging class with the potential to achieve ultimate thickness scaling and ultra-low-power operation. Their atomically thin nature enables enhanced electrostatic control and fast polarization switching, making them particularly attractive for low-power, high-speed, and high-density memory applications. However, critical challenges remain in achieving wafer-scale synthesis with uniform ferroelectric properties, improving device-todevice variability, and integrating these materials into standard semiconductor manufacturing flows.

# 4.2. Ferroelectric Transistors for Neuromorphic Computing

While ferroelectric transistors were initially developed as nonvolatile memory elements leveraging the bistable polarization states of ferroelectric materials, their functionality extends far beyond binary storage. FeFETs offer distinct advantages over conventional memory devices, including ultralow switching energy, three-terminal read-write decoupling, and nonvolatile state retention. Moreover, the integration of multiphysics coupling mechanisms, such as electrical, mechanical, and optical responses, provides expanded design flexibility and multifunctional capability, paving the way for more compact, reconfigurable, and energyefficient computing units. More importantly, the rich polarization dynamics of FeFETs support the construction of neural hardware with enhanced mapping efficiency and generalization performance, critical for real-world deployment of AI systems. In the

Table 3. Comparison of key memory metrics across different ferroelectric material systems.   

<table><tr><td>Materials structure</td><td>Program/erase voltage</td><td>operation speed</td><td>Memory window</td><td>Endurance</td><td>Retention</td><td>Refs.</td></tr><tr><td>BiFeO3/HfO2/α-In2Se3</td><td>3V/-3V</td><td>10 μs</td><td>NA</td><td>103</td><td>103s</td><td>[181]</td></tr><tr><td>BiFeO3/Y2O3/Si</td><td>20V/-20V</td><td>0.5 μs</td><td>7.97V</td><td>2.8 × 1011</td><td>2.778 h</td><td>[182]</td></tr><tr><td>PZT/WSe2</td><td>2.5V/-2.5V</td><td>5 ms</td><td>NA</td><td>4 × 102</td><td>5.5 h</td><td>[183]</td></tr><tr><td>PZT/MoS2</td><td>2.5V/-2.5V</td><td>5 ms</td><td>NA</td><td>NA</td><td>10 days</td><td>[183]</td></tr><tr><td>P(VDF/TrFE)/MEH-PPV</td><td>77.5V/-77.5V</td><td>0.3 ms</td><td>NA</td><td>103</td><td>7 days</td><td>[123]</td></tr><tr><td>P(VDF/TrFE)/ReS2</td><td>25V/-25V</td><td>1 ms</td><td>30V</td><td>2 × 103</td><td>2000 s</td><td>[184]</td></tr><tr><td>P(VDF-TrFE-CTFE)</td><td>15V/-15V</td><td>5 μs</td><td>NA</td><td>103</td><td>2 × 104s</td><td>[125]</td></tr><tr><td>/C8-BTBT</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>BZT/ P(VDF-TrFE)/ Pentacene</td><td>10V/-10V</td><td>1 s</td><td>7V</td><td>40</td><td>104s</td><td>[185]</td></tr><tr><td>HZO/ITO</td><td>3.8V/-2V</td><td>NA</td><td>2.78V</td><td>2 × 107</td><td>10 years</td><td>[186]</td></tr><tr><td>HZO/TiN/HfOx/MoS2</td><td>4V/-4V</td><td>30 ns</td><td>4.7V</td><td>1012</td><td>10 years</td><td>[111]</td></tr><tr><td>HZO/SiO2/Si</td><td>4.8V/-4.8V</td><td>100 ns</td><td>0.7V</td><td>106</td><td>10 years</td><td>[187]</td></tr><tr><td>HZO/SiNx/Si</td><td>3V/-3V</td><td>10 ns</td><td>1V</td><td>1010</td><td>NA</td><td>[56]</td></tr><tr><td>SiO2/HfO2/HZO/SiO2/Si</td><td>15V/-11V</td><td>20 μs</td><td>12.2V</td><td>1.3 × 104</td><td>10 years</td><td>[188]</td></tr><tr><td>HZO/W:In2O3</td><td>0.9V/-0.9V</td><td>20 ns</td><td>1V</td><td>1012</td><td>104s</td><td>[189]</td></tr><tr><td>HZO/Al2O3/α-In2Se3</td><td>4V/-4V</td><td>10 ns</td><td>4.2V</td><td>104</td><td>104s</td><td>[190]</td></tr><tr><td>HfO2/SiO2/Si</td><td>4V/-4.3V</td><td>1.6 μs</td><td>1.6V</td><td>105</td><td>10 years</td><td>[191]</td></tr><tr><td>CIPS/h-BN/α-In2Se3</td><td>10V/-10V</td><td>1 s</td><td>14.47V</td><td>104</td><td>104s</td><td>[192]</td></tr><tr><td>CIPS/h-BN/InSe</td><td>5V/-5V</td><td>10 ms</td><td>4.6V</td><td>103</td><td>104s</td><td>[193]</td></tr><tr><td>CIPS/Graphene/h-BN/MoS2</td><td>10V/-10V</td><td>Sub-5 μs</td><td>3.8V</td><td>104</td><td>10 years</td><td>[118]</td></tr><tr><td>AlScN/WSe2</td><td>11V/-11V</td><td>40 ms</td><td>6V</td><td>5 × 103</td><td>104s</td><td>[194]</td></tr><tr><td>AlScN/MoS2</td><td>12V/-12V</td><td>40 ms</td><td>7.8V</td><td>104</td><td>10 years</td><td>[195]</td></tr><tr><td>h-BN/ MoS2</td><td>0.25V/-0.25V</td><td>53 ns</td><td>NA</td><td>106</td><td>103s</td><td>[94]</td></tr></table>

following section, we discuss the recent progress of ferroelectric transistor-based neuromorphic devices and their integration into various network architectures, including multi-layer perceptions (MLPs), convolutional neural networks (CNNs), recurrent neural networks (RNNs), and spiking neural networks (SNNs), highlighting their potential to bridge memory and computation at the device level.

# 4.2.1. Ferroelectric Transistors used for MLP

Multilayer perceptions (MLPs), as fundamental building blocks of feedforward artificial neural networks (ANNs), are widely employed in pattern recognition, regression, and feature extraction tasks. The primary computational operation in MLPs involves multiply-and-accumulate (MAC) processes, where synaptic weights are modulated and passed through nonlinear activation functions across multiple neuron layers, including input, hidden, and output layers.[133] Implementing MLPs efficiently in hardware requires synaptic devices that offer high precision, linearity, and endurance. However, many existing synaptic device platforms suffer from limited on/off ratios, poor retention, high variability, and nonlinear or asymmetric weight update behavior limit the performance of MLP neural networks

Ferroelectric transistors present a promising solution to these challenges by leveraging the electrically switchable spontaneous polarization of ferroelectric materials to modulate the conductance of the semiconductor channel. This enables fine-tuned and non-volatile control over synaptic weights with minimal energy

consumption. Notably, the gradual polarization switching in ferroelectric domains allows ferroelectric transistors to realize multiple stable conductance states with high linearity and symmetry during the potentiation and depression process.

In 2019, Kim et al. demonstrated FeFET-based artificial synapses comprising HZO ferroelectric layers and indium gallium zinc oxide channels for MLP implementation. The devices exhibited high synaptic performance, including linear weight updates with low nonlinearity $( \mathrm { A _ { p } } = - 0 . 8 0 2 8 , \mathrm { A _ { d } } = - 0 . 6 9 7 9 )$ , a conductance ratio (Gmax/Gmin>10), and 64 discrete conductance states. These characteristics enabled a high recognition accuracy of 91.1% on the Modified National Institute of Standards and Technology (MNIST) dataset. Additionally, the study systematically correlated neural network performance with key device metrics such as conductance states, conductance variation, and cycle-to-cycle endurance, providing guidance for designing high-performance neural network hardware. To further improve scalability and integration flexibility, in 2021, Li et al. reported an inkjet printing fabricated nanoscale channel-length organic FeFET synaptic array using PVDF-TrFE as the ferroelectric layer and PDVT-10 as the organic semiconductor, as shown in a.[134] Benefiting from the vertical device structure Figure 11design, the devices exhibited improved gate control ability and a large conductance modulation window (Gmax/Gmin = 16.9), realizing linear and symmetrical weight update (Figure 11b). As shown in Figure 11c, the MLPs consist of 400 input neurons corresponding to a 20×20-pixel MNIST image, 100 hidden neurons for feature extraction, and ten output neurons representing the digit classes (0-9). The synaptic weights, represented by the

![](images/bcbf1397309b735242cdf8dc1450e4a0026c3b83c053b8e7ab574c623310d55f.jpg)  
a

![](images/1229a1d56e342bb1312aa20ad4064a67bb1f70698a61ba2c4fcece85bea33eab.jpg)

![](images/f3bc952792677d6fab097365c29953f78d5b2586b072f9208d69c12e2abbb0c6.jpg)

![](images/cf37b11c160c96bf8898703cc699ca50e6841a29f787dcabbe5187eb69eee5bb.jpg)  
d

![](images/ae16d012c832f6168ada209c38e13ce6067e62ddaa2ea3d3b4334ec9d30c8bbb.jpg)  
  
CNN

![](images/306ddd9bc5c3b9c88b89b8c2aa7b1a0a5feb455734d33b17dbc6209d5c1e4e18.jpg)

![](images/361b6280f280dd43f47eaa9e45992137ea6698263c4f225466841c1b3ab7212e.jpg)  
g   
h

![](images/a8fed973b56a41c3b1b8b4eb86e6ad6fb0a19383a458d830cf4618ffe3a2c47b.jpg)

![](images/cd6e9870662eb5360a3e0f0cedc9192297b41d180f57fed32f15b8f4b2dcadab.jpg)

![](images/3cdcded88cefcf835992a3ed50db63b7be462ea1a7f4bc71928d4b43f0cd4b3a.jpg)  
Temporal integration

![](images/10eaebbaa5d76e87ffaa50187eaa9dfef51ca46a8837d22560b4bfec50cdf8ce.jpg)  
k

![](images/c559ed7596be4e7f435d5adc74ab9d70dd37c755fda8309befa7102412aa8bad.jpg)

![](images/a17d17ba36ad1f3b3a77a9672c51fe58760b3cd284608494dc96c4120eea3754.jpg)  
m RNN

![](images/887f74be1f4f48b2f5defb8647315a1a76297fdf61ee70940146486c27dd5988.jpg)

![](images/8afe5039d70400821aa266ba9d25d3f1958e42b774e74b9372978ba17470797b.jpg)

![](images/053d94018bd5bdf66e90cdd7ad0fdcbf52393de65abfe0267deec8782880b45e.jpg)  
Reservoir nodes

![](images/8cdf00082473048d698df9c287f093241b0c2be46e0cdb8da53eb15f455e6a6b.jpg)  
FClayer   
Figure 11. Applications of ferroelectric transistors in various neuromorphic computing architectures. a) Schematic illustration of an organic ferroelectric synaptic transistor array fabricated via inkjet printing. b) Synaptic weight update under potentiation and depression of an organic ferroelectric synaptic transistor. c) Schematic of a fully connected MLP neural network employing ferroelectric synapses. d) Recognition accuracy of the organic ferroelectric synaptic transistor in the MNIST handwriting dataset.[134] e) Schematic of a ferroelectric phototransistor enabling integrated visual sensing and in-memory computing. f) Linear, bidirectional modulation of photocurrent with incident light intensity, enabling analog photoresponse control. g) Illustration of vector-matrix multiplication for CNN. h) Demonstration of reconfigurable three-in-one optical kernels—right-edge detection, top-edge detection, and image sharpening—using a ferroelectric phototransistor array.[52] i) Device structure of a double-gate HZO-based FeFET operating near the morphotropic phase boundary for phase-dependent neuromorphic functions. j) Emulation of leaky integrate-and-fire (LIF) neuron dynamics using FeFETs in the paraelectric state. k) Schematic of an SNN employing FeFETs with ferroelectric-phase synapses and paraelectric-phase neurons. l) Classification accuracy on the MNIST dataset comparing SNN performance with and without spike-frequency adaptation enabled by ferroelectric transistors.[145] m) Structure of a CIPS-based FeFET incorporating SnS2 as the photosensitive semiconducting channel material. n) Demonstration of 16 discrete conductance states in the SnS /CIPS FeFET under different optical pulse sequences, used for encoding temporal information. o) Schematic 2of RNN consists of a ferroelectric FeFET-based reservoir layer and a fully connected readout layer, enabling spatiotemporal processing.[150] a–d) Reproduced with permission.[134] Copyright 2021, Elsevier. e–h) Reproduced with permission.[52] Copyright 2023, Springer Nature. i–l) Reproduced under the terms of the CC BY license.[145] Copyright 2024, John Wiley and Sons. m–o) Reproduced under the terms of the CC BY license.[150] Copyright 2024, John Wiley and Sons.

conductance states of organic ferroelectric transistors array, are updated through voltage pulses, enabling the network to achieve a high recognition accuracy of 91.38% after 125 training epochs (Figure 11d). In 2023, Wang et al. introduced van der Waals Fe-FETs based on single-crystalline $\mathrm { B i } _ { 4 } \mathrm { T i } _ { 3 } \mathrm { O } _ { 1 2 }$ nanoflakes and fewlayer ${ \mathrm { M o S } } _ { 2 } .$ The devices exhibited an ultra-large conductance ratio (Gmax/Gmin>120), highly linear weight updates, and ultralow power operation (10 fJ/spike). Leveraging these advantages, the device achieved a remarkable 97.6% recognition accuracy in handwritten digit recognition.[135] Collectively, these advances affirm the ferroelectric transistor as a promising platform for realizing MLP-based neuromorphic computing, combining analog programmability and excellent energy efficiency.

# 4.2.2. Ferroelectric Transistors used for CNN

Convolutional neural networks have emerged as the backbone of modern computer vision, excelling in image classification, object detection, and video analysis through hierarchical feature extraction enabled by convolutional and pooling layers. Their core operations, particularly convolution and activation, rely heavily on vector-matrix multiplication (VMM), rendering them ideal candidates for acceleration through analog in-memory computing.[136] Ferroelectric transistors, owing to their non-volatility, analog tunability, and linear modulation with applied voltages, are promising synaptic elements for CNN-based neuromorphic systems. The polarization-governed channel conductance in ferroelectric transistors offers precise, gradual tuning, enabling efficient analog VMM operations directly within memory arrays while mitigating the data shuttling bottlenecks of von Neumann architectures.[137]

Recent efforts have demonstrated the feasibility of FeFETbased synaptic arrays for CNN implementations. In 2022, Kim et al. developed a CMOS-compatible HZO-based FeFET synaptic array fabricated below $4 0 0 \ ^ { \circ } \mathrm { C } .$ The array exhibited excellent linearity in current voltage and conductance modulation characteristics, supporting column and row-wise parallel programming with program inhibit schemes to minimize write disturbances.[138] Convolution operations simulated on this array, applied within a VGG-8 architecture, achieved high recognition accuracy (90.3%) on the CIFAR-10 dataset, validating the potential of FeFET arrays for real-time image feature extraction.

Beyond electrical signal processing, in 2023, Wu et al. integrated visual sensing, weight storage, and computation in a single platform by designing a ferroelectric-defined MoTe phototransistor array gated with P(VDF-TrFE) (Figure 11e).[52] The device exhibited more than 51 linearly tunable conductance states with symmetric, reversible weight update behavior and long-term retention. As shown in Figure 11f, the device demonstrates bidirectional weight updates, linear light intensity dependence, and long-term stability. Therefore, the output photocurrent of the array corresponds to the weighted sum of the incident optical power and the conductance of each device, enabling in situ VMM through convolutional functionality directly at the sensor level, leveraging the principles of Kirchhoff’s law (Figure 11g). Utilizing ferroelectric-programmed multi-level photoresponsivity and high photodetection sensitivity, the array supports reconfigurable three-in-one optical kernels. As shown in Figure 11h, kernels for

right-edge detection, top-edge detection, and image sharpening are spatially distributed to allow simultaneous extraction of three image features via a single convolution step. This integrated approach enables direct image processing, pattern recognition, and real-time robotic control without external memory or processing units, highlighting its potential for compact neuromorphic vision systems.

To further enhance integration density and scalability, in 2023, Lee et al. introduced a 3D-stacked FeFET array based on vertical HZO/InZnO ferroelectric transistors.[139] The 3D NAND architecture enabled layer-specific parallelism, where each vertical layer performed discrete CNN operations, such as feature extraction and classification. The compact vertical stacking allowed high device density and parallel VMM execution, achieving 93.8% classification accuracy in color-mixed image recognition tasks. To enable prototype devices to shift focus from implementing the functionalities of individual neurons or synapses to important network-level properties such as neural reuse, in 2025, Chen et al. designed a refreshable transistor with a $\mathrm { M o S } _ { 2 } / \mathrm { C I P S } / \mathrm { M o S } _ { 2 }$ vertical structure configuration. Through dynamic allocation of the ferro-ionic phases, the proposed device enables the collaborative dual working modes driven by ferroelectric polarization and ion migration,[140] thereby supporting the entire neural reuse process, realizing a faster learning speed (accelerated by 2200%), superior accuracy (improved by 17%), and lower power consumption (reduced by 40%). Collectively, these advances underscore the promise of ferroelectric transistors in realizing compact, energy-efficient, and high-performance CNN accelerators, where sensing, memory, and computation are seamlessly integrated at the device level.

# 4.2.3. Ferroelectric Transistors used for SNN

SNNs are regarded as the third generation of neural networks, emulating the discrete, event-driven signaling of biological neurons, offering a paradigm shift from the continuous activation functions employed in conventional MLPs and CNNs. This biologically inspired computation mechanism enables ultra-low power consumption and superior temporal information processing, making SNNs highly suitable for energy-constrained, latency-sensitive applications such as edge AI, autonomous robotics, and real-time sensory systems.[141,142] The practical realization of SNN hardware, however, necessitates stringent performance metrics including sub-femtojoule spike energy, symmetric and linear spike-timing-dependent plasticity (STDP), longterm weight retention, and high endurance across repeated training cycles.

The analog programmability and ultra-low energy operation of ferroelectric transistors, rooted in the capacitive switching of ferroelectric domains, provide an ideal physical platform for implementing synaptic plasticity and dynamic neuronal behaviors. In 2019, Chen et al. introduced graphene/ferroelectric hybrid transistors employing P(VDF-TrFE) as the ferroelectric gate dielectric to realize continuously tunable, nonvolatile synaptic weights.[143] The devices emulate supervised STDP learning in compact SNN modules through remote supervision strategies, achieving accurate classification of 3×3 image patterns with rapid convergence. The combination of ferroelectric tunability and graphene’s

ambipolar conduction enables seamless integration with peripheral leaky integrate-and-fire (LIF) neurons and control circuitry. In 2022, Ni et al. demonstrated anti-FeFETs that intrinsically emulate leaky integrate-and-fire (LIF) neuron dynamics through reversible polarization switching in $\mathrm { H f } _ { 0 \cdot 5 } \mathrm { Z r } _ { 0 \cdot 5 } { \mathrm { O } } _ { 2 }$ -based gate stacks. The devices exhibit ultralow energy consumption (≈37 fJ per spike), high endurance exceeding $1 0 ^ { 1 2 }$ cycles, and uniform spiking behavior across large arrays. When integrated with FeFET synapses in a fully ferroelectric SNN, the system achieved 96.8% classification accuracy on the MNIST dataset, comparable to ideal neuron models.[144] More recently, in 2024, Kim et al. reported a fully ferroelectric SNN system integrating multilevel synaptic FeFETs with double-gate ferroelectric transistors as artificial LIF neurons (Figure 11i).[145] The neurons exploit the volatile polarization dynamics of HZO near its morphotropic phase boundary to mimic the integration, threshold firing, and self-resetting functionalities of biological neurons, eliminating the need for external capacitors and explicit reset circuits. As shown in Figure 11j, this architecture leverages spike-frequency adaptation and lateral inhibition, enabled by the double-gate configuration, realizing a typical LIF neuron performance. Figure 11k demonstrates the schematic of a fully-connected single-layer SNN architecture, consisting of non-volatile ferroelectric transistor-based synapses and double-gate ferroelectric transistor-based LIF neurons. The complete system achieved an improved classification accuracy up to 94.9% on the MNIST dataset, compared with the device without spike-frequency adaptation ability, affirming its applicability for real-time neuromorphic computing (Figure 11l).

To promote the practical application of ferroelectric transistors in SNN networks, in 2025, Wang et al. realized ferroelectric spiking neurons composed of a ferroelectric FinFET fabricated using CMOS-compatible processes. The ferroelectric FinFET, constructed with an 80 nm gate and 14 nm fin and employing PZT as the ferroelectric gate dielectric, harnesses hysteretic polarization switching to emulate integrate-and-fire behavior. These neurons exhibit abrupt switching in polarization voltage and current voltage characteristics, generating frequency-adaptive spike trains in response to varying input stimuli. Moreover, inhibitory modulation is readily achieved by superimposing negative input pulses, effectively suppressing spike emission under competing excitatory and inhibitory inputs. The compact design and intrinsic energy efficiency of these ferroelectric spiking neurons underscore their potential for scalable SNN systems capable of unsupervised learning and pattern clustering on raw, unlabeled data.

# 4.2.4. Ferroelectric Transistors used for RNN

RNNs are designed to process sequential data by incorporating feedback loops, allowing them to retain temporal context and capture time-dependent correlations. This memory-like property makes RNNs particularly powerful in applications such as speech recognition, natural language processing, and dynamic signal prediction. Among the RNN variants, reservoir computing (RC) has emerged as a streamlined and hardware-efficient paradigm. Unlike feedforward networks such as MLPs or CNNs, where static inputs are mapped to outputs that require iterative training of all weights, RC utilizes a fixed, randomly connected reservoir layer combined with a simple, trainable output

layer.[146] This structure significantly reduces training complexity while preserving the temporal processing capabilities of full RNNs.

RC benefits from transient nonlinear responses and fading memory dynamics, which can be effectively emulated using carefully engineered ferroelectric transistors. Recent studies have demonstrated that, through specific material or structural engineering such as Vdw ferroelectricity,[147] photo-induced ferroelectric polarization,[148] and ferroelectric–antiferroelectric phase modulation,[149] ferroelectric transistors can be endowed with a unique combination of nonlinear, volatile conductance dynamics and nonvolatile polarization states within a single device. These engineered properties allow the devices to simultaneously exhibit fading memory and nonlinear transformation capabilities required by physical reservoirs, while retaining programmable states for output projection. By leveraging these phenomena, a fully ferroelectric transistor-based reservoir computing system can be constructed, wherein temporal inputs are encoded through the device’s intrinsic nonlinear dynamics and short-term memory effects, while the ferroelectric polarization serves to stabilize the reservoir configuration or provide reconfigurability. As shown in Figure 11m, in 2023, Xu. et al demonstrated an all-2D FeFET based on the SnS2/h-BN/CIPS heterostructure, realizing outstanding nonvolatile memory and integrated perception-memory-computation functionality through photoinduced ferroelectric polarization switching.[150] Under electrical stimulation, the device exhibits robust ferroelectric memory behavior, achieving a high on/off current ratio of 105 and a large memory window of 18.4 V. Upon optical excitation, photogenerated carriers in SnS couple with the polarization charges in the ferroelectric CIPS layer, inducing nonlinear photo-responsive polarization switching. As shown in Figure 11n, this optically driven modulation yields 16 discrete, stable conductance states corresponding to encoded inputs from “0000” to “1111”, reflecting a gradual and nonlinear transition. Leveraging this nonlinear, volatile photo-response, an RC system is constructed, as illustrated in Figure 11o. The RC hardware comprises a reservoir layer of optically responsive FeFETs that perform high-dimensional, spatiotemporal nonlinear mapping, and a fully connected readout layer formed by FeFET synapses exhibiting long-term potentiation and depression under electrical control. This hybrid optical-electrical architecture enables efficient parallel processing and classification tasks. Upon training, the system achieves an MNIST image recognition accuracy of 93.6%, highlighting the potential of 2D Fe-FETs for low-power, hardware-efficient neuromorphic computing.

In 2024, Kim et al. further reported an all-ferroelectric RC system using dual-gate mixed-phase boundary IGZO ferroelectric transistors as reservoir nodes and FeFETs as nonvolatile readout synapses.[149] The device exploits the field-induced modulation between ferroelectric and antiferroelectric phases near the morphotropic phase boundary of $\mathrm { H f } _ { 0 . 3 } \mathrm { Z r } _ { 0 . 7 } \mathrm { O } _ { 2 }$ . Incoming voltage pulses dynamically alter the phase composition, inducing volatile, nonlinear conductance changes, mimicking the short-term memory and nonlinearity required in RC. Meanwhile, FeFETs in the readout layer store the trained weights via stable ferroelectric polarization states, enabling efficient classification. This fully integrated architecture successfully performed time-series tasks such as waveform recognition and

MNIST classification, achieving up to 90.2% accuracy and robust prediction with low error.

# 4.3. System-Level Integration of Ferroelectric Transistors for AI Applications

To unlock the full potential of ferroelectric transistors in AI applications, system-level integration that extends beyond isolated device characteristics is essential. Recent advances have demonstrated that ferroelectric transistors are not only promising as compact non-volatile memory and in-memory computing units but also serve as core elements in highly integrated intelligent hardware when coupled with peripheral circuits such as analog-to-digital and digital-to-analog converters (ADC/DAC), field-programmable gate arrays (FPGAs), weight modulation circuits, and parallel read/write controllers. Owing to their multilevel switching capability, low-power operation, CMOS compatibility, and analog programmability, FeFET-based architectures are increasingly deployed in domain-specific edge AI systems that demand real-time processing with high energy efficiency.

# 4.3.1. Integrated Ferroelectric Transistor Systems for In Situ Machine Learning

One representative system-level strategy for enabling efficient neuromorphic computing is the development of a dynamic inmemory computing architecture based on a duplex FeFET. As illustrated in a, the device integrates an MFMIS gate Figure 12stack with an atomically thin MoS channel, forming a duplex Fe-FET structure with a voltage-tunable electrostatic landscape.[57] By precisely engineering the capacitance ratio between the ferroelectric HZO layer and the dielectric $\mathrm { A l } _ { 2 } \mathrm { O } _ { 3 }$ layer, the device can switch between a ferroelectric-dominant state for synaptic weight training and a dielectric-dominant state for inference operations, allowing task-specific reconfiguration and improved energy efficiency. This duplex architecture exhibits outstanding device performance, including ultrahigh endurance exceeding $1 0 ^ { 1 3 }$ program/erase cycles, data retention beyond 10 years, fast switching speeds of 4.8 ns, and ultralow energy consumption per operation. As shown in Figure 12b, an artificial neural network comprising three layers (input, hidden, output) is experimentally realized using an 8×3 array of two-FeFETs-one-duplex cells to solve nonlinear spatial localization tasks. Each weight is implemented by combining two seven-bit FeFET cells, enabling both positive and negative weight representations to emulate excitatory and inhibitory neural behavior.

Further validation is conducted via a co-simulated hardware software architecture for high-level vision tasks. A 178-layer, 15- block U-Net model is mapped onto the duplex FeFET platform for monocular depth estimation in autonomous driving applications. In this framework, training synapses located in the encoder module leverage the stable, long-term polarization states, while inference synapses in the decoder facilitate real-time feature decoding from the learned data. As illustrated in Figure 12c, the system accurately captures depth and semantic features across various urban driving scenes. The inference accuracy reaches 96.85%, matching the convergence of conventional GPU systems

while significantly outperforming them in energy efficiency. Projected under a 22 nm node, the FeFET-based convolution architecture achieves a training energy efficiency of 1,151 teraoperations per second per watt (TOPS/W), surpassing the stateof-the-art GPU-based solutions.

# 4.3.2. Integrated Ferroelectric Transistor Systems for Low Power Pattern Recognition

Recently, Yang et al. proposed a planar-integrated MFMIS Fe-FET architecture designed to address scalability and process integration challenges in neuromorphic systems. As illustrated in Figure 12d, a floating gate was strategically inserted between the ferroelectric (HZO) and insulating layers, enabling lateral coupling of the ferroelectric capacitor to the floating gate of the transistor. This configuration resolves key limitations of vertically stacked FeFET, specifically, weak erase behavior caused by nonuniform electric field distribution and interface defect formation, by achieving more uniform polarization switching and improved interfacial quality.[151]

The planar MFMIS architecture is fully compatible with BEOL CMOS processes, facilitating monolithic 3D integration with conventional logic. Moreover, the simplified fabrication flow reduces lithography mask steps by three, further lowering process complexity and parasitic variability. As a result, the Fe-FET exhibits excellent synaptic device performance, including a wide memory window (4.3 V), high conductance dynamic range (Gmax/Gmin>1400), outstanding endurance $( 1 0 ^ { \dot { 1 } \dot { 2 } }$ cycles), and minimal variation (cycle-to-cycle: 2.5%, device-to-device: 3.5%). These metrics support precise analog behavior, enabling 256 stable programmable conductance states and ultralow energy consumption of 47.6 fJ/spike. To ensure reliable large-scale operation, a Vop/2 half-bias scheme was implemented in a 16×16 pseudo-crossbar array configuration. During programming, target word lines received full Vop pulses while unselected WLs and bit lines (BLs) were biased at Vop/2, suppressing unintended switching events and reducing write disturbance errors to below 5%. As shown in Figure 12e, the array was fully integrated on a custom test board incorporating pulse drivers, digital decoders, and transimpedance amplifiers for accurate current-tovoltage conversion, enabling complete hardware implementation of an MLP network. As shown in Figure 12f, the FeFETsbased MLP system achieved 95% classification accuracy on a four-symbol recognition task, with a measured power efficiency of 1.7 μW/class, nearly 193× lower than traditional CMOS systems (328.6 μW/class). While the planar layout incurs a modest area overhead (∼25%), its structural simplicity, BEOL compatibility, and robust analog behavior provide a compelling route toward energy-efficient, large-scale neuromorphic processors.

# 4.3.3. Integrated Ferroelectric Transistor Systems for High Accuracy Auto Driving

In the context of autonomous driving, real-time prediction of dynamically moving objects is critical for safe navigation and decision making. Conventional computing architectures relying on frequent access to external memory for temporal data retention

![](images/e75d61b3e9e3162dc40fb9717fe0dd19c84885965fcb63219c8435a5c28374d0.jpg)  
a

![](images/f956695889ce35ba676ae3e1d5b305031cf2edb7c0aaf411fa8d43fdd55b3e7f.jpg)  
In-situ learning system

![](images/acb835df1997c06d22000c73c0dace58f3b4622f04dbbd18c188248704e3559e.jpg)  
C

![](images/288cdfac4c383e0701e0c0e2370cdbfbc2cbe3e2ee50c351a29f4b22f4f7e777.jpg)  
d

![](images/1a9efb5f2eaa71b65ddf8274f9f25369c49b91dba45503caabbcb27408d3bb7e.jpg)  
Image recogniction system

![](images/1fc335b0fa21a1cb810696de91ddb0dac896798613627cf02f5d4fb1f8cce7c4.jpg)  
f

![](images/c1041913563edcaaf6ecdb77300abec33695ea0aa0298d60573f998992daa886.jpg)  
g

![](images/a1711de7c30d52371abe66e1907d68a7c8f84db096d4f79fededad1302eafb00.jpg)  
h

![](images/e08b2f9e1f80229b69a5f8f1375524fbc3142654f805b802e54c121da76b5dec.jpg)

![](images/18e76917c3b1369eb865b11f2f8e17091b43e55af3c992cd0c125b626c2e2356.jpg)  
jTrajectory prediction system   
1

![](images/eb28c80d4175df74c71aebc3749bd579d584dadb2b7bf2ee764dd48a81bff311.jpg)  
Figure 12. System-level integration of ferroelectric transistors for AI applications. a) Duplex FeFET with MFMIS stack and MoS2 channel enabling voltagetunable training/inference by adjusting ferroelectric/dielectric capacitance. b) Optical image of an 8×3 duplex FeFET array implementing a three-layer ANN for nonlinear localization. c) U-Net simulation for monocular depth estimation using duplex FeFETs, achieving 96.85% accuracy.[57] d) Planar MFMIS FeFET with an inserted floating gate to enhance erase performance and interface quality. e) Optical image 16×16 FeFET pseudo-crossbar array integrated on PCB with peripheral circuits for MLP execution. f) FeFET-based MLP achieving 95% classification accuracy and 1.7 μW/class energy efficiency.[151] g) Schematic of trajectory prediction with spike-frequency dependent temporal processing. h) Dual-mode hysteresis of CT-FeFET showing CT-dominant and ferroelectric switching behaviors. i) Frequency-dependent short-term depression via the CT effect enables real-time history integration. j) Optical image of1K CT-FeFET array integrated with ADC and LIF neurons for dynamic trajectory prediction. k) comparison of energy efficiency memory overhead between and CT-FeFET system and a ${ \mathsf { G P U . } } ^ { [ 1 5 2 ] } { \mathsf { a - c } } )$ Reproduced with permission.[57] Copyright 2023, Springer Nature. d–f) Reproduced with permission.[151] Copyright 2024, Elsevier. g–l) Reproduced with permission.[151] Copyright 2025, IEEE.

incur significant latency and energy overhead. To overcome these limitations, in 2024, Li et al. proposed a neuromorphic architecture based on a fused long short-term plasticity ferroelectric synaptic array, inspired by the dual adaptive dynamics of biological synapses.[152]

As shown in Figure 12g, the system integrates long-term synaptic memory via non-volatile ferroelectric polarization in the HZO layer, while transient short-term memory is realized through charge trapping (CT) at engineered shallow defect states within a SiO interfacial layer. Input spatial information, such as

the relative position of a target vehicle, is encoded as frequencymodulated spike trains, where higher input frequencies induce stronger short-term depression due to cumulative CT effects. Output spike frequencies are decoded by LIF neurons to predict future trajectories, allowing proactive motion planning. This mechanism enables in-situ processing of spatiotemporal dependencies without requiring external memory buffering.

The underlying device operation relies on decoupled hysteresis modes, as illustrated in Figure 12h, a clockwise loop emerges under low-voltage operation (<1.5 V) due to volatile CT, while anticlockwise loops dominate at higher voltages (>2.2 V), corresponding to stable ferroelectric switching. Moreover, as demonstrated in Figure 12i, the CT mechanism exhibits frequencydependent short-term depression, where increasing spike frequencies induce enhanced conductance suppression, following an exponential decay model, which is crucial for encoding and integrating temporal sequences in real time. The FeFET devices were further extended to a 1K CT-FeFET synaptic array using BEOL-compatible processes, achieving a four-bit analog resolution and small cycle-to-cycle and device-to-device variation (Figure 12j). Finally, a complete prediction system was constructed by integrating the CT-FeFET array with a custom dynamic in-memory computing board, a 16-bit ADC for parallel row-wise data acquisition, and an FPGA-based LIF neuron module for real-time signal processing (Figure 12k). Spike-coded positional data were applied to the synaptic array, where CT-induced depression encoded short-term dynamics. The row-wise outputs were digitized and processed by the LIF neurons, and the neuron with the highest firing rate represented the predicted location of the moving object. This architecture demonstrated over 1000× improvement in energy efficiency and a 4× reduction in memory overhead compared to GPU-based implementations, as shown in Figure 12l. These gains arise from the co-location of computation and memory within the CT-FeFET array, thereby eliminating data movement bottlenecks inherent in von Neumann architectures.

# 5. Summary and Outlook

This review provides a comprehensive overview of FeFETs, from the origin of ferroelectricity to their diverse functionalities in next-generation electronics. FeFETs are far more than a new type of memory but are a revolutionary platform that merges memory, computation, and sensing into a single, multifunctional transistor. Harnessing the intrinsic coupling of ferroelectric materials with electric, optical, and magnetic fields, FeFETs uniquely bridge the gap between traditional digital logic, non-volatile storage, and cutting-edge neuromorphic and in-sensor computing architectures. In logic circuits, the high dielectric constant and negative capacitance effect of ferroelectrics enable ultrafast, lowvoltage switching beyond the classical Boltzmann limit, achieving sub-60 mVdec−1 operation. As non-volatile memories, Fe-FETs exploit bistable polarization to store information without standby power, offering nanosecond-level write/erase speeds, retention exceeding a decade, and endurance approaching 1012 cycles, dramatically outperforming conventional flash in both energy efficiency and scalability. Beyond digital applications, Fe-FETs can emulate the analog behavior of biological synapses, enabling continuous, reversible conductance modulation for inmemory computing and neuromorphic learning. Their seamless

integration with sensors and CMOS peripherals allows memory, sensing, and computation to coexist within a single architecture, opening the door to intelligent, energy-efficient, edge AI systems. While the potential is enormous, realizing this vision requires overcoming key materials, device, and integration challenges.

# 5.1. Materials: Stabilizing Ferroelectric Phases and Microstructures

The integration of FeFETs into advanced nodes (10 nm and below) requires aggressive scaling of the ferroelectric layer from the current 5–10 nm down to 3 nm below to meet tight gate pitch constraints. While hafnia-based ferroelectrics maintain robust polarization at these thicknesses, scaling introduces a critical trade-off: thinner films enhance memory density, reduce write voltages to logic-compatible, but simultaneously amplify the depolarization field and leakage current, and increase sensitivity to both bulk and interface defects. Moreover, the ferroelectric layers are often polycrystalline, exhibiting inhomogeneous grain sizes, random orientations, and mixed-phase distributions. And the desired ferroelectric phase (e.g., orthorhombic in HZO) is typically metastable and sensitive to processing conditions, leading to phase degradation over time or under electrical stress. These microstructural variabilities result in significant device-todevice performance fluctuations and reduced reliability. To address these challenges, future material development should focus on promoting strong crystallographic texture or single crystal behavior with ultra-thin thickness through large-scale epitaxial growth or template-induced nucleation; Stabilizing ferroelectric phases via compositional doping and defect engineering; Exploring new classes of scalable ferroelectrics with high remanent polarization, such as AlScN or engineered superlattices, for enhanced scalability and CMOS compatibility.

# 5.2. Device Engineering: Enhancing Reliability, Density, and Endurance

While FeFETs offer exceptional speed and energy efficiency, their endurance still falls behind SRAM, primarily due to degradation at the ferroelectric interface. High trap densities lead to threshold voltage shifts and retention loss, while repeated highfield switching can induce hot carrier injection, accelerating interfacial and bulk defect formation. Addressing these reliability concerns requires meticulous gate stack engineering to enhance interface quality, increasing voltage drop across the ferroelectric layer, and reducing it across the interfacial oxide. Scaling down the ferroelectric thickness to enable low-voltage operation compatible with advanced logic nodes, thereby minimizing stress-induced degradation. Additionally, architectural strategies such as MFMIS stacking, dual-gate structures, and charge-trapassisted FeFETs provide architectural solutions for suppressing write disturbance, enhancing multibit storage, and improving write/erase symmetry. The multi-level cell programming, vertical 3D stacking, and analog weight modulation further enhance storage density and functionality, positioning FeFETs as both digital memories and analog neuromorphic units. Ultimately, Fe-FET design involves a careful trade-off across multiple metrics.

No single configuration is universally optimal, and the design space must be tailored to the specific requirements of each datacentric application, balancing performance and data persistence according to the target use case.

# 5.3. System-Level Integration: Toward AI-Enabled Intelligent Platforms

Looking ahead, realizing the full potential of FeFETs in intelligent systems will require a holistic, system-level co-design approach that unites device physics with algorithmic functionality. Future domain-specific architectures should harness the intrinsic strengths of FeFETs, such as analog weight tunability, multi-bit programmability, and non-volatility, to efficiently implement neural operations, including temporal encoding, spatial filtering, and adaptive learning. Scalable and manufacturable integration will hinge on monolithic 3D stacking of FeFETs with CMOS logic, enabling densely packed, vertically interconnected memory–compute hierarchies optimized for data-centric processing. This integration demands ultra-low thermal budget fabrication (<300 °C), defect-tolerant circuit designs, and adaptive control architectures to mitigate device variability, endurance degradation, and precision loss in large-scale arrays. Furthermore, advancing in situ and on-chip learning will require rethinking the conventional algorithm–hardware interface. The design of local training circuits, online weight update schemes, and error-correction mechanisms must be adapted to accommodate the analog, nonlinear, and history-dependent behavior of FeFETs.

In the long term, FeFET integration will evolve toward heterogeneous intelligent platforms where memory, sensing, logic, and learning are seamlessly co-localized within a unified hardware stack. This convergence will enable compact, low-power AI chips capable of autonomous perception and adaptive decisionmaking, advancing applications in robotics, real-time biomedical diagnostics, and neuromorphic computing. The next wave of semiconductor innovation will depend on how effectively hardware can support data-centric intelligence, and FeFET technology is poised to be a cornerstone in this evolution.

# Acknowledgements

E.L. and W.W. contributed equally to this work. This work was supported by National Natural Science Foundation of China (Grant Nos. U25A20482, 62374043 and 62304043), Shanghai Pilot Program for Basic Research-Fudan University 21TQ1400100 (25TQ001), Shanghai Oriental Talent Program Youth Project (2022), State Key Laboratory of Dynamic Measurement Technology, North University of China (2024-SYSJJ-06), National Key Laboratory of Integrated Circuit Materials (SKLJC-K2025-04), Shanghai Collaborative Innovation Center of Intelligent Perception Chip Technology, and China Postdoctoral Science Foundation (Grant Nos. 2022M720751 and 2023T160119).

# Conflict of Interest

The authors declare no conflict of interest.

# Keywords

ferroelectric materials, field effect transistor, ferroelectric semiconductor, non-volatile memory, neuromorphic computing

Received: August 9, 2025

Revised: December 2, 2025

Published online:

[1] M. A. Zidan, J. P. Strachan, W. D. Lu, Nat. Electron. 2018, 1, 22.   
[2] C. Chen, Y. Zhou, L. Tong, Y. Pang, J. Xu, Adv. Mater. 2024, 37, 2400332.   
[3] D. Gizopoulos, G. Papadimitriou, A. Chatzidimitriou, V. J. Reddi, B. Salami, O. S. Unsal, A. C. Kestelman, J. Leng, 2019 IEEE 25th International Symposium on On-Line Testing and Robust System Design (IOLTS), IEEE, Piscataway, NJ 2019, 129.   
[4] G. Singh, L. Chelini, S. Corda, A. J. Awan, S. Stuijk, R. Jordans, H. Corporaal, A.-J. Boonstra, Microprocess. Microsyst. 2019, 71, 102868.   
[5] K. Sun, J. Chen, X. Yan, Adv. Funct. Mater. 2021, 31, 2006773.   
[6] A. Gholami, Z. Yao, S. Kim, C. Hooper, M. W. Mahoney, K. Keutzer, AI, M. Wall, IEEE Micro 2024, 44, 33.   
[7] W. A. Wulf, S. A. McKee, ACM SIGARCH Comput. Architect. news 1995, 23, 20.   
[8] C. Bogmans, P. Gomez-Gonzalez, G. Ganpurev, G. Melina, A. Pescatori, S. Thube, P. Hungry, IMF Working Papers 2025, 081, 32.   
[9] K.-H. Kim, I. Karpov, R. H. Olsson, D. Jariwala, Nat. Nanotechnol. 2023, 18, 422.   
[10] U. Schroeder, M. H. Park, T. Mikolajick, C. S. Hwang, Nat. Rev. Mater. 2022, 7, 653.   
[11] T. Mikolajick, U. Schroeder, S. Slesazeck, IEEE Trans. Electron Devices 2020, 67, 1434.   
[12] T. Mikolajick, M. H. Park, L. Begon-Lours, S. Slesazeck, Adv. Mater. 2023, 35, 2206042.   
[13] I. J. Kim, J. S. Lee, Adv. Mater. 2023, 35, 2206864.   
[14] S. Majumdar, Adv. Intell. Syst 2022, 4, 2100175.   
[15] H. Jiao, X. Wang, S. Wu, Y. Chen, J. Chu, J. Wang, Appl. Phys. Rev. 2023, 10, 011310.   
[16] D. Chen, T. Murphy, J. Phillips, Thin Solid Films 2005, 491, 301.   
[17] K. Meng, W. Li, X.-G. Tang, Q.-X. Liu, Y.-P. Jiang, ACS Appl. Electron. Mater. 2021, 4, 2109.   
[18] V. Afanasjev, A. Petrov, I. Pronin, E. Tarakanov, E. J. Kaptelov, J. Graul, J. Phys.: Condens. Matter 2001, 13, 8755.   
[19] L. Pintilie, Phys. Rev. B 2007, 75, 104103.   
[20] W. Li, S.-L. Li, K. Komatsu, A. Aparecido-Ferreira, Y.-F. Lin, Y. Xu, M. Osada, T. Sasaki, K. Tsukagoshi, Appl. Phys. Lett. 2013, 103, 023113.   
[21] H. Chen, X. Zhou, L. Tang, Y. Chen, H. Luo, X. Yuan, C. R. Bowen, D. Zhang, Appl. Phys. Rev. 2022, 9, 011307.   
[22] K. Komatsu, I. Suzuki, T. Aoki, Y. Hamasaki, S. Yasui, M. Itoh, T. Taniyama, Appl. Phys. Lett. 2020, 117, 072902.   
[23] N. Wang, X. Luo, L. Han, Z. Zhang, R. Zhang, H. Olin, Y. Yang, Nano-Micro Lett. 2020, 12, 81.   
[24] A. Jain, Y. G. Wang, A. Kumar, N. Gupta, K. Kumar, A. K. Goyal, J. Alloys Compd. 2025, 1010, 177170.   
[25] F. Liu, L. You, K. L. Seyler, X. Li, P. Yu, J. Lin, X. Wang, J. Zhou, H. Wang, H. He, S. T. Pantelides, W. Zhou, P. Sharma, X. Xu, P. M. Ajayan, J. Wang, Z. Liu, Nat. Commun. 2016, 7, 12357.   
[26] X. Zhao, C. Li, R. Qi, H. Guo, G. Peng, Polymer 2022, 252, 124933.   
[27] S. Roy, A. Chowdhury, M. Joshi, S. W. Ali, ACS Appl. Electron. Mater. 2024   
[28] P. Saxena, P. Shukla, Adv. Compos. Hybrid Mater. 2021, 4, 8.   
[29] S. Anwar, D. Pinkal, W. Zajaczkowski, P. von Tiedemann, H. Sharifi Dehsari, M. Kumar, T. Lenz, U. Kemmer-Jonas, W. Pisula, M. Wagner, R. Graf, H. Frey, K. Asadi, Sci. Adv. 2019, 5, aav3489.   
[30] A. Yanaka, W. Sakai, K. Kinashi, N. Tsutsumi, J. Appl. Polym. Sci 2020, 137, 48438.   
[31] J.-C. Blancon, J. Even, C. C. Stoumpos, M. G. Kanatzidis, A. D. Mohite, Nat. Nanotechnol. 2020, 15, 969.

[32] W. Zheng, X. Wang, X. Zhang, B. Chen, H. Suo, Z. Xing, Y. Wang, H.-L. Wei, J. Chen, Y. Guo, F. Wang, Adv. Mater. 2023, 35, 2205410.   
[33] Y. Chen, C. Gao, T. Yang, W. Li, H. Xu, Z. Sun, Chin. J. Struct. Chem. 2022, 41, 2204001.   
[34] S. Duan, P. Chen, Y.-a. Xiong, F. Zhao, Z. Jing, G. Du, X. Wei, S. Xiang, J. Hong, Q. Shi, Y. You, J. Wu, Sci. Adv. 2024, 10, adr2886.   
[35] Y. Guo, L. Wu, J. Deng, L. Zhou, W. Jiang, S. Lu, D. Huo, J. Ji, Y. Bai, X. Lin, S. Zhang, H. Xu, W. Ji, C. Zhang, Nano Res. 2021, 15, 1276.   
[36] M. Acosta, N. Novak, V. Rojas, S. Patel, R. Vaish, J. Koruza, G. A. Rossetti, J. Rödel, Appl. Phys. Rev. 2017, 4, 041305.   
[37] W. Cochran, Adv. Phys. 1960, 9, 387.   
[38] S. Liu, I. Grinberg, A. M. Rappe, Nature 2016, 534, 360.   
[39] T.-X. Xu, X.-B. Guo, D. Zhang, Q.-J. Sun, Y.-P. Jiang, Q.-X. Liu, X.-G. Tang, J. Mater. Chem. A 2024, 12, 31028.   
[40] L. Liang, E. Pan, G. Cao, J. Chen, R. Wang, B. Dong, Q. Liu, X. Chen, X. Luo, Y. Kong, W. Li, F. Liu, Nat. Commun. 2025, 16, 4462.   
[41] W. J. Hu, D.-M. Juo, L. You, J. Wang, Y.-C. Chen, Y.-H. Chu, T. Wu, Sci. Rep. 2014, 4, 4772.   
[42] T. Zhang, K. Xu, J. Li, L. He, D.-W. Fu, Q. Ye, R.-G. Xiong, Natl. Sci. Rev. 2023, 10, nwac240.   
[43] W. He, Y. Yang, C. Li, W. P. D. Wong, F. Cimpoesu, A. M. Toader, Z. Wu, X. Wu, Z. Lin, Q.-h. Xu, K. Leng, A. Stroppa, K. P. Loh, J. Am. Chem. Soc. 2023, 145, 14044.   
[44] Y. Liu, S. Yang, L. Hua, X. Yang, E. Li, J. Wen, Y. Wu, L. Zhu, Y. Yang, Y. Zhao, Nat. Commun. 2025, 16, 365.   
[45] L. Li, M. Wu, ACS Nano 2017, 11, 6382.   
[46] E. Pan, Z. Li, F. Yang, K. Niu, R. Bian, Q. Liu, J. Chen, B. Dong, R. Wang, T. Zhou, A. Zhou, X. Luo, J. Chu, J. Lin, W. Li, F. Liu, Nat. Commun. 2025, 16, 3026.   
[47] E. Y. Tsymbal, Science 2021, 372, 1389.   
[48] Z. Zheng, Q. Ma, Z. Bi, S. de La Barrera, M.-H. Liu, N. Mao, Y. Zhang, N. Kiper, K. Watanabe, T. Taniguchi, Nature 2020, 588, 71.   
[49] X. Wang, K. Yasuda, Y. Zhang, S. Liu, K. Watanabe, T. Taniguchi, J. Hone, L. Fu, P. Jarillo-Herrero, Nat. Nanotechnol. 2022, 17, 367.   
[50] L. Rogée, L. Wang, Y. Zhang, S. Cai, P. Wang, M. Chhowalla, W. Ji, S. P. Lau, Science 2022, 376, 973.   
[51] S. Kamaei, X. Liu, A. Saeidi, Y. Wei, C. Gastaldi, J. Brugger, A. M. Ionescu, Nat. Electron. 2023, 6, 658.   
[52] G. Wu, X. Zhang, G. Feng, J. Wang, K. Zhou, J. Zeng, D. Dong, F. Zhu, C. Yang, X. Zhao, D. Gong, M. Zhang, B. Tian, C. Duan, Q. Liu, J. Wang, J. Chu, M. Liu, Nat. Mater. 2023, 22, 1499.   
[53] Y. Zang, D. Xie, Y. Xiao, Y. Ruan, T. Ren, L. Liu, Integr. Ferroelectr. 2008, 98, 90.   
[54] W. P. Li, Y. M. Liu, R. Zhang, J. Chen, P. Cheng, X. L. Yuan, Y. G. Zhou, B. Shen, R. L. Jiang, Z. G. Liu, Y. D. Zheng, Appl. Phys. A 2001, 72, 85.   
[55] S. W. Kim, W. Shin, M. Kim, K. R. Kwon, J. Yim, J. Kim, C. Han, S. Jeong, E. C. Park, J. W. You, H. Kim, R. Choi, D. Kwon, IEEE Electron Device Lett. 2023, 44, 1955.   
[56] M. Hoffmann, A. J. Tan, N. Shanker, Y. H. Liao, L. C. Wang, J. H. Bae, C. Hu, S. Salahuddin, IEEE Electron Device Lett. 2022, 43, 717.   
[57] H. Ning, Z. Yu, Q. Zhang, H. Wen, B. Gao, Y. Mao, Y. Li, Y. Zhou, Y. Zhou, J. Chen, L. Liu, W. Wang, T. Li, Y. Li, W. Meng, W. Li, Y. Li, H. Qiu, Y. Shi, Y. Chai, H. Wu, X. Wang, Nat. Nanotechnol. 2023, 18, 493.   
[58] S. J. Yoon, D. H. Min, S. E. Moon, K. S. Park, J. I. Won, S. M. Yoon, IEEE Trans. Electron Devices 2020, 67, 499.   
[59] Z.-D. Luo, S. Zhang, Y. Liu, D. Zhang, X. Gan, J. Seidel, Y. Liu, G. Han, M. Alexe, Y. Hao, ACS Nano 2022, 16, 3362.   
[60] K. Huang, M. Zhai, X. Liu, B. Sun, H. Chang, J. Liu, C. Feng, H. Liu, IEEE Electron Device Lett. 2020, 41, 1600.   
[61] Z. Zhang, G. Xu, Q. Zhang, Z. Hou, J. Li, Z. Kong, Y. Zhang, J. Xiang, Q. Xu, Z. Wu, H. Zhu, H. Yin, W. Wang, T. Ye, IEEE Electron Device Lett. 2019, 40, 367.

[62] E. Yurchuk, J. Muller, J. Paul, T. Schlosser, D. Martin, R. Hoffmann, S. Muller, S. Slesazeck, U. Schroeder, R. Boschke, R. Bentum, T. Mikolajick, IEEE Trans. Electron Devices 2014, 61, 3699.   
[63] W. Huang, H. Zhu, Y. Zhang, X. Yin, X. Ai, J. Li, C. Li, Y. Li, L. Xie, Y. Liu, J. Xiang, K. Jia, J. Li, T. C. Ye, IEEE Electron Device Lett. 2022, 43, 25.   
[64] M. Pesic, F. P. G. Fengler, L. Larcher, A. Padovani, T. Schenk, E. D. Grimley, X. H. Sang, J. M. LeBeau, S. Slesazeck, U. Schroeder, T. Mikolajick, Adv. Funct. Mater. 2016, 26, 4601.   
[65] H. J. Kim, M. H. Park, Y. J. Kim, Y. H. Lee, T. Moon, K. Do Kim, S. D. Hyun, C. S. Hwang, Nanoscale 2016, 8, 1383.   
[66] C.-C. Fan, H.-H. Chen, R.-Y. Liao, W.-C. Chou, C.-C. Huang, H.- H. Hsu, S.-T. Han, C.-H. Cheng, Thin Solid Films 2024, 799, 140400.   
[67] F. Li, B. Wang, X. Gao, D. Damjanovic, L.-Q. Chen, S. Zhang, Science 389, adn4926.   
[68] Y. Yun, P. Buragohain, M. Li, Z. Ahmadi, Y. Zhang, X. Li, H. Wang, J. Li, P. Lu, L. Tao, H. Wang, J. E. Shield, E. Y. Tsymbal, A. Gruverman, X. Xu, Nat. Mater 2022, 21, 903.   
[69] Y. Wang, L. Tao, R. Guzman, Q. Luo, W. Zhou, Y. Yang, Y. Wei, Y. Liu, P. Jiang, Y. Chen, S. Lv, Y. Ding, W. Wei, T. Gong, Y. Wang, Q. Liu, S. Du, M. Liu, Science 2023, 381, 558.   
[70] S. Kang, W.-S. Jang, A. N. Morozovska, O. Kwon, Y. Jin, Y.-H. Kim, H. Bae, C. Wang, S.-H. Yang, A. Belianinov, S. Randolph, E. A. Eliseev, L. Collins, Y. Park, S. Jo, M.-H. Jung, K.-J. Go, H. W. Cho, S.-Y. Choi, J. H. Jang, S. Kim, H. Y. Jeong, J. Lee, O. S. Ovchinnikova, J. Heo, S. V. Kalinin, Y.-M. Kim, Y. Kim, Science 2022, 376, 731.   
[71] S. S. Cheema, N. Shanker, L.-C. Wang, C.-H. Hsu, S.-L. Hsu, Y.-H. Liao, M. San Jose, J. Gomez, W. Chakraborty, W. Li, J.-H. Bae, S. K. Volkman, D. Kwon, Y. Rho, G. Pinelli, R. Rastogi, D. Pipitone, C. Stull, M. Cook, B. Tyrrell, V. A. Stoica, Z. Zhang, J. W. Freeland, C. J. Tassone, A. Mehta, G. Saheli, D. Thompson, D. I. Suh, W.-T. Koo, K.-J. Nam, et al., Nature 2022, 604, 65.   
[72] J. Dong, Z. Sheng, R. Yu, W. Hu, Y. Wang, H. Sun, D. W. Zhang, P. Zhou, Z. Zhang, Adv. Electron. Mater 2022, 8, 2100829.   
[73] S. Song, K.-H. Kim, R. Keneipp, M. Jung, N. Trainor, C. Chen, J. Zheng, J. M. Redwing, J. Kang, M. Drndi´c, R. H. Olsson Iii, D. Jariwala, ACS Nano 2025, 19, 8985.   
[74] M. Si, J. Andler, X. Lyu, C. Niu, S. Datta, R. Agrawal, P. D. Ye, ACS Nano 2020, 14, 11542.   
[75] Z. Zhao, S. Rakheja, W. Zhu, Nano Lett. 2021, 21, 9318.   
[76] M. Xu, S. Guo, L. Xiang, T. Xu, W. Xie, W. Wang, IEEE Trans. Electron Devices 2018, 65, 1113.   
[77] Y. Jeong, H.-J. Jin, J. H. Park, Y. Cho, M. Kim, S. Hong, W. Jo, Y. Yi, S. Im, Adv. Funct. Mater. 2020, 30, 1908210.   
[78] C.-Y. Lin, B.-C. Chen, Y.-C. Liu, S.-F. Kuo, H.-C. Tsai, Y.-M. Chang, C.-Y. Kuo, C.-F. Chang, J.-H. Chen, Y.-H. Chu, M. Yamamoto, C.-H. Shen, Y.-L. Chueh, P.-W. Chiu, Y.-C. Chen, J.-C. Yang, Y.-F. Lin, Nat. Electron. 2025, 8, 560.   
[79] B. H. Kim, S. H. Kuk, S. K. Kim, J. P. Kim, Y. J. Suh, J. Jeong, D. M. Geum, S. H. Baek, S. H. Kim, IEEE Trans. Electron Devices 2023, 70, 1996.   
[80] S. Dai, S. Li, S. Xu, F. Tian, J. Chai, J. Duan, W. Xiong, J. Xiang, Y. Wang, H. Xu, J. Zhang, X. Wang, W. Wang, IEEE Trans. Electron Devices 2024, 71, 5081.   
[81] P. Xu, P. Jiang, Y. Yang, T. Gong, W. Wei, Y. Wang, X. Long, J. Niu, Z. Wu, X. Peng, Z. Wu, Q. Luo, IEEE Electron Device Lett. 2024, 45, 2110.   
[82] M. C. Nguyen, S. Kim, K. Lee, J. Y. Yim, R. Choi, D. Kwon, IEEE Electron Device Lett. 2021, 42, 1295.   
[83] S. Oh, J. Song, I. K. Yoo, H. Hwang, IEEE Electron Device Lett. 2019, 40, 1092.   
[84] M. M. Hasan, Mohit, M. M. I, R. N. Bukke, E. Tokumitsu, H. Y. Chu, S. C. Kim, J. Jang, IEEE Electron Device Lett. 2022, 43, 725.

[85] S. Jindal, S. K. Manhas, S. K. Gautam, S. Balatti, A. Kumar, M. Pakala, IEEE Trans. Electron Devices 2021, 68, 1364.   
[86] K. Lee, J. Yim, W. Shin, S. Kim, D. Kwon, IEEE Electron Device Lett. 2024, 45, 805.   
[87] F. Wang, J. Liu, W. Huang, R. Cheng, L. Yin, J. Wang, M. G. Sendeku, Y. Zhang, X. Zhan, C. Shan, Z. Wang, J. He, Sci. Bull. 2020, 65, 1444.   
[88] S. Wang, L. Liu, L. Gan, H. Chen, X. Hou, Y. Ding, S. Ma, D. W. Zhang, P. Zhou, Nat. Commun. 2021, 12, 53.   
[89] J. Nordlander, G. De Luca, N. Strkalj, M. Fiebig, M. Trassin, Appl. Sci. 2018, 8, 570.   
[90] W. Ding, J. Zhu, Z. Wang, Y. Gao, D. Xiao, Y. Gu, Z. Zhang, W. Zhu, Nat. Commun. 2017, 8, 14956.   
[91] Y. Zhou, D. Wu, Y. Zhu, Y. Cho, Q. He, X. Yang, K. Herrera, Z. Chu, Y. Han, M. C. Downer, H. Peng, K. Lai, Nano Lett. 2017, 17, 5508.   
[92] M. Si, A. K. Saha, S. Gao, G. Qiu, J. Qin, Y. Duan, J. Jian, C. Niu, H. Wang, W. Wu, S. K. Gupta, P. D. Ye, Nat. Electron. 2019, 2, 580.   
[93] P. Meng, Y. Wu, R. Bian, E. Pan, B. Dong, X. Zhao, J. Chen, L. Wu, Y. Sun, Q. Fu, Q. Liu, D. Shi, Q. Zhang, Y.-W. Zhang, Z. Liu, F. Liu, Nat. Commun. 2022, 13, 7696.   
[94] R. Bian, R. He, E. Pan, Z. Li, G. Cao, P. Meng, J. Chen, Q. Liu, Z. Zhong, W. Li, F. Liu, Science 2024, 385, 57.   
[95] J. Zhang, J. Zhang, Y. Qi, S. Gong, H. Xu, Z. Liu, R. Zhang, M. A. Sadi, D. Sychev, R. Zhao, H. Yang, Z. Wu, D. Cui, L. Wang, C. Ma, X. Wu, J. Gao, Y. P. Chen, X. Wang, Y. Jiang, Nat. Commun. 2024, 15, 7648.   
[96] R. Quhe, Z. Di, J. Zhang, Y. Sun, L. Zhang, Y. Guo, S. Wang, P. Zhou, Nat. Nanotechnol. 2023, 19, 173.   
[97] J. Wang, X. Wang, C. Eckert, A. Subramaniyan, R. Das, D. Blaauw, D. Sylvester, IEEE J. Solid-State Circuits 2020, 55, 76.   
[98] S. Jourba, N. Bollon, C. Decobert, G. Festes, B. Bertello, F. Zhou, V. Markov, Y. Tkachev, J. Kim, P. Ghazav, X. Liu, N. Do, R. Richter, S. Dünkel, M. Trentzsch, A. Zaka, T. Herrmann, T. Melde, B. Müller, F. Mauersberger, B. Bayha, S. Wittek, M. Duggan, S. Beyer, 2020 IEEE International Memory Workshop (IMW), IEEE, Piscataway, NJ 2020, pp. 17-20.   
[99] Y. K. Kim, S. Park, J. Choi, H. Park, B. C. Jang, Adv. Funct. Mater. 2024, 34, 2405670.   
[100] W. Shu-Yau, IEEE Trans. Electron Device 1974, 21, 499.   
[101] M. Tang, X. Xu, Z. Ye, Y. Sugiyama, H. Ishiwara, IEEE Trans. Electron Device 2011, 58, 370.   
[102] P. N. Tripathi, S. K. Ojha, A. Nazarov, Appl. Phys. A 2021, 127, 58.   
[103] J. Chen, G. Dun, J. Hu, Z. Lin, Y. Wang, T. Lu, P. Li, T. Wei, J. Zhu, J. Wang, X. Li, X.-M. Wu, Y. Yang, T.-L. Ren, ACS Nano 2023, 17, 12374.   
[104] D. Sen, H. Ravichandran, M. Das, P. Venkatram, S. Choo, S. Varshney, Z. Zhang, Y. Sun, J. Shah, S. Subbulakshmi Radhakrishnan, A. Saha, S. Hazra, C. Chen, J. M. Redwing, K. A. Mkhoyan, V. Gopalan, Y. Yang, B. Jalan, S. Das, Nat. Commun. 2024, 15, 10739.   
[105] Q. Yang, J. Hu, Y.-W. Fang, Y. Jia, R. Yang, S. Deng, Y. Lu, O. Dieguez, L. Fan, D. Zheng, X. Zhang, Y. Dong, Z. Luo, Z. Wang, H. Wang, M. Sui, X. Xing, J. Chen, J. Tian, L. Zhang, Science 2023, 379, 1218.   
[106] T. S. Böscke, J. Müller, D. Bräuhaus, U. Schröder, U. Böttger, 2011 International Electron Devices Meeting, IEEE, Piscataway, NJ 2011, pp. 5–7.   
[107] K. Mistry, C. Allen, C. Auth, B. Beattie, D. Bergstrom, M. Bost, M. Brazier, M. Buehler, A. Cappellani, R. Chau, C. H. Choi, G. Ding, K. Fischer, T. Ghani, R. Grover, W. Han, D. Hanken, M. Hattendorf, J. He, J. Hicks, R. Huessner, D. Ingerly, P. Jain, R. James, L. Jong, S. Joshi, C. Kenyon, K. Kuhn, K. Lee, H. Liu, et al., 2007 IEEE International Electron Devices Meeting (IEDM), IEEE, Piscataway, NJ 2007, pp. 10–12 .   
[108] G. Karbasian, A. Tan, A. Yadav, E. M. H. Sorensen, C. R. Serrao, A. I. Khan, K. Chatterjee, K. Sangwan, H. Chenming, S. Salahuddin, 2017

International Symposium on VLSI Technology, Systems and Application (VLSI-TSA), IEEE, Piscataway, NJ 2017, pp. 24–27.   
[109] H. Mulaosmanovic, E. T. Breyer, T. Mikolajick, S. Slesazeck, IEEE Trans. Electron Devices 2019, 66, 3828.   
[110] W. Xiao, C. Liu, Y. Peng, S. Zheng, Q. Feng, C. Zhang, J. Zhang, Y. Hao, M. Liao, Y. Zhou, Nanoscale Res. Lett. 2019, 14, 254.   
[111] T. Lu, J. Xue, P. Shen, H. Liu, X. Gao, X. Li, J. Hao, D. Huang, R. Zhao, J. Yan, M. Yang, B. Yan, P. Gao, Z. Lin, Y. Yang, T.-L. Ren, Sci. Adv. 10, adp0174.   
[112] S. C. Yan, G. M. Lan, C. J. Sun, Y. H. Chen, C. H. Wu, H. K. Peng, Y. H. Lin, Y. H. Wu, Y. C. Wu, IEEE Electron Device Lett. 2021, 42, 1307.   
[113] Y. Fan, S. Zhang, Z. Xue, Y. Dong, D. Chen, J. Zhang, J. Liu, M. Si, C. Luo, W. Li, J. Chu, Y. Cao, Z. Wang, X. Li, Nat. Commun. 2025, 16, 4232.   
[114] J. R. Rodriguez, W. Murray, K. Fujisawa, S. H. Lee, A. L. Kotrick, Y. Chen, N. McKee, S. Lee, M. Terrones, S. Trolier-McKinstry, T. N. Jackson, Z. Mao, Z. Liu, Y. Liu, Appl. Phys. Lett. 2020, 117, 052901.   
[115] Y. Bao, P. Song, Y. Liu, Z. Chen, M. Zhu, I. Abdelwahab, J. Su, W. Fu, X. Chi, W. Yu, Nano Lett. 2019, 19, 5109.   
[116] J. Junquera, P. Ghosez, Nature 2003, 422, 506.   
[117] M. Si, P.-Y. Liao, G. Qiu, Y. Duan, P. D. Ye, ACS Nano 2018, 12, 6700.   
[118] X. Wang, C. Zhu, Y. Deng, R. Duan, J. Chen, Q. Zeng, J. Zhou, Q. Fu, L. You, S. Liu, J. H. Edgar, P. Yu, Z. Liu, Nat. Commun. 2021, 12, 1109.   
[119] R. Bian, G. Cao, E. Pan, Q. Liu, Z. Li, L. Liang, Q. Wu, L. K. Ang, W. Li, X. Zhao, F. Liu, Nano Lett. 2023, 23, 4595.   
[120] X. Li, B. Qin, Y. Wang, Y. Xi, Z. Huang, M. Zhao, Y. Peng, Z. Chen, Z. Pan, J. Zhu, C. Cui, R. Yang, W. Yang, S. Meng, D. Shi, X. Bai, C. Liu, N. Li, J. Tang, K. Liu, L. Du, G. Zhang, Nat. Commun. 2024, 15, 10921.   
[121] P. Zhang, X. Chen, W. Li, H. Ling, W. Wang, G. Zhang, M. Yi, L. Xie, W. Shi, N. Shi, W. Huang, Org. Electron. 2018, 57, 335.   
[122] Y. van de Burgt, A. Melianas, S. T. Keene, G. Malliaras, A. Salleo, Nat. Electron. 2018, 1, 386.   
[123] R. C. G. Naber, C. Tanase, P. W. M. Blom, G. H. Gelinck, A. W. Marsman, F. J. Touwslager, S. Setayesh, D. M. de Leeuw, Nat. Mater. 2005, 4, 243.   
[124] T. Xu, L. Xiang, M. Xu, W. Xie, W. Wang, Sci. Rep. 2017, 7, 8890.   
[125] Y. Ding, Q. Xu, H. Wei, J. Su, W. Wang, IEEE Electron Device Lett. 2024, 45, 240.   
[126] M. Kang, S.-A. Lee, S. Jang, S. Hwang, S.-K. Lee, S. Bae, J.-M. Hong, S. H. Lee, K.-U. Jeong, J. A. Lim, T.-W. Kim, ACS Appl. Mater. Interfaces 2019, 11, 22575.   
[127] S. Ham, M. Kang, S. Jang, J. Jang, S. Choi, T.-W. Kim, G. Wang, Sci. Adv. 6, aba1178.   
[128] Q. Zhao, H. Wang, Z. Ni, J. Liu, J. Li, F. Yang, L. Li, L. Jiang, Y. Zhen, H.Dong,W.Hu,Ady.Mgter 2024,36,24]2255.   
[129] H. Xu, F. Sun, E. Li, W. Guo, L. Hua, R. Wang, W. Li, J. Chu, W. Liu, J. Luo, Adv. Mater. 2025, 37, 2414339.   
[130] W. Guo, H. Xu, F. Sun, Y. Liu, Y. Ma, W. Liu, Y. Zhao, Z. Sun, J. Luo, Angew. Chem., Int. Ed. 2025, 64, 202421463.   
[131] P. Zhang, C. Xu, G. Chen, C. Liu, P. Yang, X. Shang, W. Li, H. Chen, Device 2025, 3, 100757.   
[132] E. Li, W. He, R. Wang, C. Zhang, H. Zhou, Y. Liu, Y. Yuan, K. P. Loh, J. Chu, W. Li, Nat. Commun. 2025, 16, 9382.   
[133] M. K. Kim, J. S. Lee, Nano Lett. 2019, 19, 2044.   
[134] E. Li, X. Wu, Q. Chen, S. Wu, L. He, R. Yu, Y. Hu, H. Chen, T. Guo, Nano Energy 2021, 85, 106010.   
[135] Z. Wang, X. Zhou, X. Liu, A. Qiu, C. Gao, Y. Yuan, Y. Jing, D. Zhang, W. Li, H. Luo, J. Chu, J. Sun, Chip 2023, 2, 100044.   
[136] L. Pi, P. Wang, S.-J. Liang, P. Luo, H. Wang, D. Li, Z. Li, P. Chen, X. Zhou, F. Miao, T. Zhai, Nat. Electron. 2022, 5, 248.   
[137] R. Yu, L. He, C. Gao, X. Zhang, E. Li, T. Guo, W. Li, H. Chen, Nat. Commun. 2022, 13, 7019.

[138] M.-K. Kim, I.-J. Kim, J.-S. Lee, Sci. Adv. 2022, 8, abm8537.   
[139] I.-J. Kim, M.-K. Kim, J.-S. Lee, Nat. Commun. 2023, 14, 504.   
[140] J. Chen, Z. Wen, F. Yang, R. Bian, Q. Zhang, E. Pan, Y. Zeng, X. Luo, Q. Liu, L.-J. Deng, F. Liu, Nat. Commun. 2025, 16, 702.   
[141] N. Zheng, P. Mazumder, IEEE Trans. Neural Netw. Learn. Syst. 2018, 29, 4287.   
[142] C. Gao, M. Liu, A. Aierken, X. Liu, D. Wang, Z. Wang, G. Wang, Y. Wu, G. Zhou, H. Chen, J. Bi, Adv. Funct. Mater. 2025, 17785.   
[143] Y. Chen, Y. Zhou, F. Zhuge, B. Tian, M. Yan, Y. Li, Y. He, X. S. Miao, npj 2D Mater. Appl. 2019, 3, 31.   
[144] R. Cao, X. Zhang, S. Liu, J. Lu, Y. Wang, H. Jiang, Y. Yang, Y. Sun, W. Wei, J. Wang, H. Xu, Q. Li, Q. Liu, Nat. Commun. 2022, 13, 7018.   
[145] J. Kim, E. C. Park, W. Shin, R. H. Koo, J. Im, C. H. Han, J. H. Lee, D. Kwon, Adv. Sci. 2024, 11, 2407870.   
[146] D. J. Gauthier, E. Bollt, A. Griffith, W. A. S. Barbosa, Nat. Commun. 2021, 12, 5564.   
[147] J. Zhou, A. Chen, Y. Zhang, X. Zhang, J. Chai, J. Hu, H. Li, Y. Xu, X. Liu, N. Tan, F. Xue, B. Yu, Nano Lett. 2024, 24, 14892.   
[148] J. Zha, S. Shi, A. Chaturvedi, H. Huang, P. Yang, Y. Yao, S. Li, Y. Xia, Z. Zhang, W. Wang, H. Wang, S. Wang, Z. Yuan, Z. Yang, Q. He, H. Tai, E. H. T. Teo, H. Yu, J. C. Ho, Z. Wang, H. Zhang, C. Tan, Adv. Mater. 2023, 35, 2211598.   
[149] J. Kim, E. C. Park, W. Shin, R.-H. Koo, C.-H. Han, H. Y. Kang, T. G. Yang, Y. Goh, K. Lee, D. Ha, S. S. Cheema, J. K. Jeong, D. Kwon, Nat. Commun. 2024, 15, 9147.   
[150] P. Wang, J. Li, W. Xue, W. Ci, F. Jiang, L. Shi, F. Zhou, P. Zhou, X. Xu, Adv. Sci. 2024, 11, 2305679.   
[151] P. Yang, P. Tong, H. Xu, S. Liu, C. Chen, Y. Zhang, S. Yu, W. Wang, R. Cao, H. Liu, L. Liao, Q. Li, J. Mater. Sci. Technol. 2025, 231, 20.   
[152] C. Li, J. Yu, X. Zhang, Z. Zhang, F. Zhu, S. Ouyang, P. Chen, L. Cheng, G. Xu, Q. Zhang, H. Yin, Q. Liu, M. Liu, 2024 IEEE International Electron Devices Meeting (IEDM), IEEE, Piscataway, NJ 2024, 1.   
[153] S. S. Cheema, D. Kwon, N. Shanker, R. dos Reis, S.-L. Hsu, J. Xiao, H. Zhang, R. Wagner, A. Datar, M. R. McCarter, C. R. Serrao, A. K. Yadav, G. Karbasian, C.-H. Hsu, A. J. Tan, L.-C. Wang, V. Thakare, X. Zhang, A. Mehta, E. Karapetrova, R. V. Chopdekar, P. Shafer, E. Arenholz, C. Hu, R. Proksch, R. Ramesh, J. Ciston, S. Salahuddin, Nature 2020, 580, 478.   
[154] T. Li, Y. Wu, G. Yu, S. Li, Y. Ren, Y. Liu, J. Liu, H. Feng, Y. Deng, M. Chen, Z. Zhang, T. Min, Nat. Commun. 2024, 15, 2653.   
[155] C. Cui, W.-J. Hu, X. Yan, C. Addiego, W. Gao, Y. Wang, Z. Wang, L. Li, Y. Cheng, P. Li, X. Zhang, H. N. Alshareef, T. Wu, W. Zhu, X. Pan, L.-J. Li, Nano Lett. 2018, 18, 1253.   
[156] X. Chen, X. Han, Q.-D. Shen, Adv. Electron. Mater 2017, 3, 1600460.   
[157] Y. S. Choi, S. K. Kim, M. Smith, F. Williams, M. E. Vickers, J. A. Elliott, S. Kar-Narayan, Sci. Adv. 6, aay5065.   
[158] J. Y. Park, W. Mihalyi-Koch, C. T. Triggs, C. R. Roy, K. M. Sanders, J. C. Wright, S. Jin, Adv. Mater. 2024, 36, 2314292.   
[159] H. Jaffe, J. Am. Ceram. Soc. 1958, 41, 494.   
[160] W. Li, W. Cao, D. Xu, W. Wang, W. Fei, J. Alloys Compd. 2014, 613, 181.   
[161] A. Simoes, M. Zaghete, B. Stojanovic, C. Riccardi, A. Ries, A. Gonzalez, J. A. Varela, Mater. Lett. 2003, 57, 2333.   
[162] D. Wang, J. Zheng, P. Musavigharavi, W. Zhu, A. C. Foucher, S. E. Trolier-McKinstry, E. A. Stach, R. H. Olsson, IEEE Electron Device Lett. 2020, 41, 1774.   
[163] Q. Jiang, L. Cross, J. Mater. Sci. 1993, 28, 4536.   
[164] C. A.-P. de Araujo, J. Cuchiaro, L. McMillan, M. Scott, J. Scott, Nature 1995, 374, 627.   
[165] J. Muller, T. S. Boscke, U. Schroder, S. Mueller, D. Brauhaus, U. Bottger, L. Frey, T. Mikolajick, Nano Lett. 2012, 12, 4318.

[166] X. Liu, J. Zheng, D. Wang, P. Musavigharavi, E. A. Stach, R. Olsson III, D. Jariwala, Appl. Phys. Lett. 2021, 118, 202901.   
[167] H. Hu, H. Wang, Y. Sun, J. Li, J. Wei, D. Xie, H. Zhu, Nanotechnology 2021, 32, 385202.   
[168] K. Chang, J. Liu, H. Lin, N. Wang, K. Zhao, A. Zhang, F. Jin, Y. Zhong, X. Hu, W. Duan, Science 2016, 353, 274.   
[169] T. Yamada, T. Ueda, T. Kitayama, J. Appl. Phys. 1981, 52, 948.   
[170] H. H. Jiang, X. J. Song, H. P. Lv, X. G. Chen, R. G. Xiong, H. Y. Zhang, Adv. Mater. 2024, 36, 2307936.   
[171] S. Hoshino, T. Mitsui, F. Jona, R. Pepinsky, Phy. Rev. 1957, 107, 1255.   
[172] K. Yasuda, X. Wang, K. Watanabe, T. Taniguchi, P. Jarillo-Herrero, Science 2021, 372, 1458.   
[173] Z. Wang, Z. Gui, L. Huang, Phys. Rev. B 2023, 107, 035426.   
[174] C. Zhang, Z. Zhang, Z. Wu, X. Li, Y. Wu, J. Kang, J. Phys. Chem. Lett. 2024, 15, 8049.   
[175] Z. Ma, Z. Yao, Y. Cheng, X. Zhang, B. Guo, Y. Lyu, P. Wang, Q. Li, H. Wang, A. Nie, A. Aspuru-Guzik, Nano Energy 2020, 67, 104276.   
[176] W. Chen, Z. Sun, Z. Wang, L. Gu, X. Xu, S. Wu, C. Gao, Science 2019, 366, 983.   
[177] K. Liu, X. Ma, S. Xu, Y. Li, M. Zhao, Npj Comput. Mater. 2023, 9, 16.   
[178] Q. Yang, M. Wu, J. Li, J. Phys. Chem. Lett. 2018, 9, 7160.   
[179] X. Chen, X. Ding, G. Gou, X. C. Zeng, Nano Lett. 2024, 24, 3089.   
[180] S. Jia, J. Liao, Q. Yang, R. Peng, J. Wang, F. Yan, S. Wen, Z. Wang, J. Huang, K. Bao, X. Liu, M. Liao, J. Jiang, Y. Zhou, Adv. Funct. Mater. 2025, 35, 2501470.   
[181] Y. Wang, Y. Cai, S. Li, X. Zhan, R. Cheng, Z. Wang, J. He, F. Wang, Small 2025, 21, 2409922.   
[182] K. P. Pandey, Ferroelectrics 2020, 558, 140.   
[183] C. Ko, Y. Lee, Y. Chen, J. Suh, D. Fu, A. Suslu, S. Lee, J. D. Clarkson, H. S. Choe, S. Tongay, R. Ramesh, J. Wu, Adv. Mater. 2016, 28, 2923.   
[184] L. Liu, H. Wang, Q. Wu, K. Wu, Y. Tian, H. Yang, C. M. Shen, L. Bao, Z. Qin, H.-J. Gao, Nano Res. 2022, 15, 5443.   
[185] K. J. Lee, T. Y. Yang, D. W. Chou, Y. H. Wang, IEEE Electron Device Lett. 2022, 43, 1463.   
[186] Q. Li, S. Wang, Z. Li, X. Hu, Y. Liu, J. Yu, Y. Yang, T. Wang, J. Meng, Q. Sun, D. W. Zhang, L. Chen, Nat. Commun. 2024, E15.   
[187] K. T. Chen, H. Y. Chen, C. Y. Liao, G. Y. Siang, C. Lo, M. H. Liao, K. S. Li, S. T. Chang, M. H. Lee, IEEE Electron Device Lett. 2019, 40, 399.   
[188] S. H. Kuk, B. H. Kim, Y. Park, K. Ko, H. S. Hwang, D. Lee, B. J. Cho, J. H. Han, S. H. Kim, 2024 IEEE International Electron Devices Meeting (IEDM), IEEE, Piscataway, NJ 2024, 7–11.   
[189] S. G. Kirtania, H. Park, O. Phadke, E. Sarkar, D. Chakraborty, F. G. Waqar, J. Shin, A. Khan, S. Yu, S. Datta, IEEE Trans. Electron Devices 2025, 72, 2691.   
[190] J. Huo, Z. Zhang, Y. Zhang, F. Zhang, G. Yan, G. Tian, H. Xu, G. Zhan, G. Xu, Q. Zhang, H. Yin, Z. Wu, IEEE Trans. Electron Devices 2023, 70, 3071.   
[191] H. Mulaosmanovic, S. Dünkel, D. Kleimaier, A. e. Kacimi, S. Beyer, E. T. Breyer, T. Mikolajick, S. Slesazeck, IEEE Trans. Electron Devices 2021, 68, 4773.   
[192] S. Baek, H. H. Yoo, J. H. Ju, P. Sriboriboon, P. Singh, J. Niu, J.-H. Park, C. Shin, Y. Kim, S. Lee, Adv. Sci. 2022, 9, 2200566.   
[193] P. Singh, S. Baek, H. H. Yoo, J. Niu, J.-H. Park, S. Lee, ACS Nano 2022, 16, 5418.   
[194] K.-H. Kim, S. Song, B. Kim, P. Musavigharavi, N. Trainor, K. Katti, C. Chen, S. Kumari, J. Zheng, J. M. Redwing, E. A. Stach, R. H. Olsson Iii, D. Jariwala, ACS Nano 2024, 18, 4180.   
[195] K.-H. Kim, S. Oh, M. M. A. Fiagbenu, J. Zheng, P. Musavigharavi, P. Kumar, N. Trainor, A. Aljarb, Y. Wan, H. M. Kim, K. Katti, S. Song, G. Kim, Z. Tang, J.-H. Fu, M. Hakami, V. Tung, J. M. Redwing, E. A. Stach, R. H. Olsson, D. Jariwala, Nat. Nanotechnol. 2023, 18, 1044.

![](images/0a52e2604f2faaf9f1af9f9519d23fe4dacb16a3a386d0a8463c4b132f18a65b.jpg)

Enlong Li received his Ph.D. degree from Fuzhou University, China in 2022 and then worked as a postdoctoral researcher at Fudan University from 2022–2025. He is currently an associate professor at the School of Microelectronics, Shanghai University. His research focuses on the development of advanced materials and device technologies for next-generation integrated circuits.

![](images/4e5da21389f34057ec8d68b91cbf4068aaa6cf7b52be503c201eb51da7e4534f.jpg)

Wunan Wang is a Ph.D. candidate in electronic science and technology at Fudan University since 2022. He received his B.S. and M.S. degrees from China Jiliang University. His research interests focus on novel oxide semiconductor materials and their integrated device applications.

![](images/b929b73ff4f4140129488705e96c704bfef4f5a0416c2fd5ada694bdc72dbc7e.jpg)

Wenwu Li received his Ph.D. degree in Microelectronics and Solid-State Electronics from East China Normal University in 2012. From 20122014, he worked as a postdoctoral researcher at the National Institute for Materials Science (Japan) and China Southern Power Grid Corporation. From 20142021, he worked as a full professor at East China Normal University. Since August 2021, he is serving as a full professor at Fudan University. His research field focuses on semiconductor electronic devices, ferroelectric materials and devices. For more information: (https://fit.fudan.edu.cn/Data/View/4889).

![](images/7608c337b7720f50613f4ba43024a33f03d71e6e3eef119d85537c1cb4add8e4.jpg)

Junhao Chu is an academician of the Chinese Academy of Sciences since 2005. He received his Ph.D. degree from the Shanghai Institute of Technical Physics, Chinese Academy of Sciences in 1984. From 1986 to 1988, he was a Humboldt Fellow at Technical University of Munich, Germany. From 1993 to 2003, he was Director of the National Laboratory for Infrared Physics. He is now serving as a distinguished professor at Fudan University, China. He is a world-famous semiconductor physics and device expert. His current research interests include semiconductor material physics and device technology.