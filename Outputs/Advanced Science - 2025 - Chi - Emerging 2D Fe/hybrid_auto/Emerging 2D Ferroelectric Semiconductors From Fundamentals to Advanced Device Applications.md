---
title: "Emerging 2D Ferroelectric Semiconductors: From Fundamentals to Advanced Device Applications"
authors:
  - "Mengshuang Chi"
  - "Xiang Zhang"
  - "JiTao Liu"
  - "YiFan Wang"
  - "Aifang Yu"
  - "Di Guo"
  - "Junyi Zhai"
date: "2025-01-01"
year: "2025"
journal: "Advanced Science"
doi: "10.1002/advs.202514185"
abstract: "Two-dimensional (2D) ferroelectric semiconductors, as an emerging class of functional materials, attract considerable interest in nanoelectronics, spintronics, and optoelectronics, owing to their unique ability to combine ferroelectricity and semiconducting properties at the ultimate thickness limit. This review provides a comprehensive overview of the development, fundamental mechanisms, and recent advances of 2D ferroelectric semiconductors. The origins and unique characteristics of 2D ferroelectricity are discussed, and representative intrinsic 2D ferroelectric semiconductors as well as extrinsic systems are summarized. The potential applications of these materials in electronics, optoelectronics, spintronics, and valleytronics are discussed in detail. Finally, the key challenges facing the field are outlined, and perspectives on future directions are offered. This review aims to provide a systematic reference for both fundamental studies and technological development, fostering the advancement of 2D ferroelectric semiconductors toward high-performance and multifunctional device applications."
abstract_cn: "二维铁电半导体作为一类新兴的功能材料，因其在极限厚度下结合铁电性和半导体特性的独特能力，在纳米电子学、自旋电子学和光电子学领域引起了广泛关注。本综述全面概述了二维铁电半导体的发展、基本机制和最新进展。讨论了二维铁电性的起源和独特特征，总结了代表性的本征二维铁电半导体以及外延系统。详细探讨了这些材料在电子学、光电子学、自旋电子学和能谷电子学中的潜在应用。最后，概述了该领域面临的关键挑战，并对未来发展方向提出了展望。本综述旨在为基础研究和技术开发提供系统参考，促进二维铁电半导体向高性能和多功能器件应用的发展。"
keywords:
  - "[[2D ferroelectric semiconductors]]"
  - "[[Ferroelectricity]]"
  - "[[Review]]"
  - "[[Advanced Science]]"
cite: "[1] Chi et al. Emerging 2D Ferroelectric Semiconductors: From Fundamentals to Advanced Device Applications[J]. Advanced Science, 2025."
aiSum: "二维铁电半导体综述：涵盖发展历程、基本机制（软模理论、滑动铁电性）、本征/外延材料体系、在FeS-FET、FTJ、光电探测器、自旋器件等应用，挑战与未来方向。"
confidence: "high"
wiki_concepts:
  - "[[Ferroelectric]]"
---

# Emerging 2D Ferroelectric Semiconductors: From Fundamentals to Advanced Device Applications

Mengshuang Chi, Xiang Zhang, JiTao Liu, YiFan Wang, Aifang Yu, Di Guo,* and Junyi Zhai*

Two-dimensional (2D) ferroelectric semiconductors, as an emerging class of functional materials, attract considerable interest in nanoelectronics, spintronics, and optoelectronics, owing to their unique ability to combine ferroelectricity and semiconducting properties at the ultimate thickness limit. This review provides a comprehensive overview of the development, fundamental mechanisms, and recent advances of 2D ferroelectric semiconductors. The origins and unique characteristics of 2D ferroelectricity are discussed, and representative intrinsic 2D ferroelectric semiconductors as well as extrinsic systems are summarized. The potential applications of these materials in electronics, optoelectronics, spintronics, and valleytronics are discussed in detail. Finally, the key challenges facing the field are outlined, and perspectives on future directions are offered. This review aims to provide a systematic reference for both fundamental studies and technological development, fostering the advancement of 2D ferroelectric semiconductors toward high-performance and multifunctional device applications.

# 1. Introduction

Ferroelectricity, defined as the presence of a spontaneous and reversible electric polarization, was first discovered in 1920 by Joseph Valasek in Rochelle salt (potassium sodium tartrate).[1] Below a characteristic Curie temperature (Tc), these materials

M. Chi, X. Zhang, J. Liu, Y. Wang, A. Yu, D. Guo, J. Zhai Beijing Key Laboratory of Micro-Nano Energy and Sensor Center for High-Entropy Energy and Systems Beijing Institute of Nanoenergy and Nanosystems Chinese Academy of Sciences Beijing 101400, P. R. China E-mail: guodi@binn.cas.cn; jyzhai@binn.cas.cn M. Chi, X. Zhang, J. Liu, Y. Wang, A. Yu, D. Guo, J. Zhai School of Nanoscience and Engineering University of Chinese Academy of Sciences Beijing 100049, P. R. China M. Chi, J. Liu, J. Zhai Beijing Huairou Laboratory Beijing 100049, P. R. China

The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/advs.202514185 © 2025 The Author(s). Advanced Science published by Wiley-VCH GmbH. This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited. DOI: 10.1002/advs.202514185

exhibit a non-zero polarization that can be reversed by applying an external electric field, leading to a hysteretic polarization– field loop. This reversible polarization makes ferroelectrics direct analogs of ferromagnets (hence the prefix “ferro-”), with analogous features such as remnant polarization and coercive fields. After Valasek’s pioneering work, other early ferroelectrics were identified: for example, KDP $\mathrm { ( K H } _ { 2 } \mathrm { P O } _ { 4 } )$ was found in the 1930s to become ferroelectric below ≈122 K.[2] However, these compounds were characterized by hydrogen-bonded crystal structures, high water solubility, and poor mechanical stability, limiting practical use. Consequently, ferroelectricity was initially considered a niche phenomenon, with limited utility and theoretical interest during its formative decades. The field took a major turn with the discovery of

robust, room-temperature ferroelectricity in inorganic oxides. In particular, $\mathrm { B a T i O } _ { 3 }$ was found in the mid-1940s to undergo a ferroelectric transition near $1 2 0 \ ^ { \circ } \mathrm { C } . ^ { [ 3 ] }$ This stable perovskite oxide, characterized by a very high dielectric constant, enabled the development of the first ferroelectric devices, including ultrasound transducers and, subsequently, non-volatile memory systems. Subsequent work in the 1950s–1960s expanded this family: lead zirconate titanate $( \mathrm { P b } ( \mathrm { Z r } , \mathrm { T i } ) \mathrm { O } _ { 3 } , \mathrm { o r } \mathrm { P Z T } )$ ) and related solid solutions became the workhorses for piezoelectric and ferroelectric applications. The simple perovskite structure of ${ \mathrm { B a T i O } } _ { 3 }$ and its derivatives also made them ideal for developing the phenomenological Landau–Devonshire theory of ferroelectricity (double-well potential models), which remains a cornerstone for understanding ferroelectric phase transitions and polarization switching.

Throughout the late 20th century, ferroelectric research focused on improving material properties (higher $T _ { c } ,$ larger polarization, fatigue resistance) and device integration. Despite these advances, a fundamental limitation emerged: when ferroelectric films are thinned toward the nanometer scale, the depolarization field (arising from incomplete screening of surface charges) suppresses polarization. Theoretical studies predicted that below a critical thickness (often only a few unit cells), a conventional ferroelectric will lose its polar order.[4,5] Experimentally, ferroelectricity in perovskite thin films typically vanishes below a few nanometers unless elaborate interface engineering is used to compensate for the depolarizing field.[6,7] These scaling limits,

together with the complex fabrication of oxide films, have driven the search for novel atomically thin ferroelectrics.

A breakthrough came with the discovery that layered twodimensional (2D) semiconductors can host intrinsic ferroelectricity. In contrast to oxide films, 2D layered materials have no dangling surface bonds, allowing clean, trap-free interfaces and robust polar order down to a single layer. Early studies in the 1960s–1970s identified bulk ferroelectricity in IV– VI monochalcogenides[8] (SnS, SnSe, GeS, and GeSe) and in transition-metal phosphorus trisulfides[9] (MPX compounds), but only recently have ultrathin 2D forms been explored. Firstprinciples calculations in 2016–2017 predicted that monolayers of certain van der Waals (vdW) materials (e.g., SnSe,[10] GeTe,[11] $\mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 } ^ { \ [ 1 2 ] } )$ possess spontaneous polarization arising from inplane (IP) ionic displacement or interlayer sliding. A key advance was achieved in 2016, when room-temperature switchable spontaneous polarization was experimentally demonstrated in ultrathin 4 nm $\mathrm { C u I n P } _ { 2 } \mathrm { S } _ { 6 }$ (CIPS),[13] challenging the long-held view that depolarization fields would suppress ferroelectricity at the nanoscale. Since then, a wide variety of 2D vdW ferroelectrics have been identified. These include $\mathrm { \dot { N i I } _ { 2 } } , \mathrm { [ 1 4 ] }  \alpha { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 } , \mathrm { [ } ^ { 1 5 } \mathrm { ] }$ $\mathrm { C u C r P } _ { 2 } \mathrm { S } _ { 6 } , ^ { [ 1 6 ] }$ the family of group-IV monochalcogenides[17–19] (GeS, GeSe, SnS, SnSe, etc.), and layered transition-metal dichalcogenides[20] (e.g., MoTe2, $\mathrm { W T e } _ { 2 } )$ . Very recently, layered bismuth oxychalcogenides[21] (e.g., ${ \tt B i } _ { 2 } { \sf O } _ { 2 } { \sf S e } )$ and niobium oxyhalides[22] (e.g., NbOI ) have been proposed as 2D ferroelectric semiconductors, where subtle lattice distortions break inversion symmetry. In addition to these intrinsic materials, researchers have used strain, charge doping, surface functionalization, and engineered defects to induce ferroelectricity in nominally non-ferroelectric 2D crystals. The field is also moving toward “multiphysics” ferroelectrics: for example, heterostructures like $\mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 } / \mathrm { C r I } _ { 3 } [ 2 3 ]$ ] couple ferroelectric and magnetic or valley degrees of freedom, opening new device possibilities.

A key advantage of many 2D ferroelectrics is that they are semiconductors with moderate band gaps. This means a single 2D crystal can simultaneously host a switchable polarization and support electronic conduction. In practice, 2D ferroelectric semiconductors overcome the scaling limits of conventional ferroelectrics: for example, $\boldsymbol { \alpha } { \cdot } \boldsymbol { \mathrm { I n } } _ { 2 } \boldsymbol { \mathrm { S e } } _ { 3 }$ maintains robust polarization down to a few atomic layers. Moreover, the clean vdW surfaces allow easy stacking and gating without the dielectric fatigue problems of oxide devices. These properties enable novel device concepts. First, a 2D ferroelectric can serve simultaneously as an active transistor channel and a nonvolatile memory element. For example, $\alpha { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ has been used as the channel in fieldeffect transistors whose conductance state is set by the ferroelectric polarization. Because the channel polarization does not rely on a separate gate dielectric, these devices intrinsically combine logic and memory functions, with the transistor state being nonvolatile. Such devices have been demonstrated to operate with fast switching (tens of nanoseconds) and tunable neural-network dynamics, pointing toward in-memory and neuromorphic computing applications.[24] Second, nonvolatile gating is now possible: a ferroelectric layer in a 2D heterostructure can gate an adjacent semiconductor layer without continuous power, enabling ultra-low-energy memory and logic. Third, the polar order in a semiconductor enables optoelectronic enhancements. For instance, broken inversion symmetry gives a bulk photovoltaic ef-

fect, where light absorption can generate photovoltages above the bandgap. It was recently shown that 2D CIPS exhibits a bulk photovoltaic response two orders of magnitude larger than classic oxide ferroelectrics.[25] Similarly, $\alpha { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ exhibits a strong pyroelectric response in conjunction with its intrinsic polarization, giving rise to a pyro-photovoltaic effect that enables it to function simultaneously as a self-powered photodetector and a memory element.[26]

Over the past few years, the development of 2D ferroelectric semiconductor devices has undergone rapid and diverse evolution, marked by breakthroughs in architecture, mechanism, and functionality, as illustrated in  . In 2019, the ferro-Figure 1electric semiconductor field effect transistor (FeS-FET) was first demonstrated using $\alpha { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ to embed ferroelectricity within the channel, enabling direct carrier modulation without conventional gate stacks.[27] This was followed in 2020 by enhanced tunneling electroresistance in CIPS-based 2D ferroelectric tunnel junctions (FTJs), advancing logic-in-memory integration.[28] In 2021, the adoption of MFMIS architectures improved retention and endurance by mitigating depolarization effects.[29] From 2022 to 2023, novel mechanisms were uncovered, including spontaneous ferroelectricity in untwisted $\mathrm { M o S } _ { 2 } / \mathrm { W S } .$ heterostructures, tunable polarization in $\mathrm { W S e } _ { 2 } / \mathrm { M o S } _ { 2 }$ trilayers, and hybrid negative-capacitance tunneling devices achieving sub-60 mV dec−1 switching.[30,31] In 2024, a shear-induced sliding ferroelectric transistor based on $3 \mathrm { R } { \cdot } \mathrm { M o S } _ { 2 }$ offered rewritable, highspeed memory functionality.[32] By 2025, the field expanded into optoelectronics, with demonstrations of ferroelectric bulk photovoltaic effects in $3 \mathrm { R - W S } _ { 2 } ^ { [ 3 3 ] }$ and strong terahertz emission and synaptic plasticity in $\mathrm { N b O I } _ { 2 } [ 3 4 ]$ heterostructures. Collectively, these advancements mark a transition from fundamental material exploration to multifunctional, device-integrated platforms. 2D ferroelectric semiconductors are now emerging as key building blocks for next-generation electronic, optoelectronic, and neuromorphic systems.

2D ferroelectric semiconductors form an emerging class of materials that combine spontaneous polarization with semiconducting behavior at atomic thickness. Materials such as $\alpha { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ and CIPS exhibit stable room-temperature ferroelectricity even in ultrathin films, offering promising opportunities for applications in electronics and optoelectronics. In this review, we first outline the historical context of ferroelectricity and the advent of 2D ferroelectrics, emphasizing the unique mechanisms that stabilize polarization at the nanoscale. It then discusses the fundamental principles that govern ferroelectricity in low-dimensional systems, with a focus on their distinct physical properties compared to bulk ferroelectrics. Next, we outline the main classes of 2D ferroelectric semiconductors, including intrinsic materials and extrinsically engineered systems. Their structural features, polarization mechanisms, and representative examples are summarized in detail. In addition, applications in various device platforms are also discussed, including ferroelectric transistors, tunneling junctions, photodetectors, and spin-related devices. The review concludes with an analysis of current challenges in the field, such as maintaining polarization stability at the nanoscale, integrating with existing semiconductor processes, and optimizing material performance. Future directions in materials discovery, theoretical modeling, and quantum ferroelectric effects are also considered. This review is intended to

![](images/9ba99b8b295650b73a34c9e402ca2dac6bffe16d143f15a38ee1a4cda004611a.jpg)  
Figure 1. Timeline of milestones in 2D ferroelectric semiconductors. Reproduced with permission.[27–35,36] Copyright 2019, Springer Nature; Copyright 2020, Springer Nature; Copyright 2021, Springer Nature; Copyright 2022, The American Association for the Advancement of Science. Copyright 2022, Springer Nature; Copyright 2023, Springer Nature; Copyright 2024, Springer Nature; Copyright 2025, Springer Nature; Copyright 2025, Springer Nature; Copyright 2025, John Wiley and Sons.

![](images/9e919ca2ae060804e83aeab9d2a7a907f0fbe45ae4ca79b233cb00b9e6bf20f5.jpg)  
Figure 2. Progress in 2D ferroelectric semiconductors: structures, mechanisms, devices, and functional applications. The central circle highlights representative mechanisms of 2D ferroelectricity, including displacive ferroelectricity and sliding ferroelectricity,[37] Copyright 2025, The Authors, published by Springer Nature. order–disorder ferroelectricity,[13] Copyright 2016, The Authors, published by Springer Nature. improper ferroelectricity,[38] electronic ferroelectricity,[39] and domain-wall topology ferroelectricity.[40] The outer ring depicts potential applications in electronics,[27,41,42] optoelectronics,[25,43,44] references25,44, Copyright 2021, The Authors, published by Springer Nature. and spintronics.[45–47] Reproduced with permission.[27,38–42,43,45–47] Copyright 2024, American Chemical Society; Copyright 2012, American Physical Society; Copyright 2024, American Chemical Society; Copyright 2019, Springer Nature; Copyright 2022, Springer Nature; Copyright 2017, John Wiley and Sons; Copyright 2023, John Wiley and Sons; Copyright 2021, Springer Nature; Copyright 2024, American Physical Society; Copyright 2024, American Chemical Society.

support researchers in advancing the development and application of 2D ferroelectric semiconductors. presents a Figure 2schematic overview of the review structure, which helps to understand the overall organization and content arrangement of the article.

# 2. Fundamentals of 2D Ferroelectric Semiconductors

Understanding the fundamental physics of 2D ferroelectric semiconductors requires revisiting the core principles of ferroelec-

tric ordering, which arises from the spontaneous alignment of electric dipoles within a crystal lattice. In conventional bulk and thin-film systems, spontaneous dipole alignment is destabilized in ultrathin regimes due to enhanced depolarization fields and weakened Coulomb interactions, often leading to the disappearance of ferroelectricity below a few nanometers. In contrast, van der Waals layered materials present a fundamentally different platform. Their intrinsic 2D nature, with strong IP covalent bonding and weak out-of-plane (OOP) van der Waals coupling, offers structural stability down to the monolayer limit without the need for epitaxial constraint or chemical passivation. This anisotropic bonding environment suppresses detrimental interfacial effects and enables the retention of spontaneous polarization even in atomic-scale systems. Beyond classical ferroelectric behavior, these 2D materials exhibit coupling between polarization and symmetry-breaking electronic properties such as Rashba spin-splitting, valley polarization, and direction-dependent transport, making them ideal for exploring new regimes of ferroic order and correlated phenomena in reduced dimensions.

The microscopic mechanism of ferroelectric polarization is complex, as it typically involves competing interactions. Fundamentally, ferroelectricity originates from spontaneous symmetry breaking in the crystal structure under certain conditions, leading to spontaneous polarization. According to the soft mode theory,[48,49] ferroelectric phase transitions are generally driven by the softening of a specific optical phonon mode, whose frequency approaches zero, thereby inducing stable atomic displacements and forming a polar structure. This softening arises mainly from the competition between short-range repulsive forces, which favor high-symmetry nonpolar Jahn–Teller effect. Calculations of projector structures and long-range Coulomb interactions, which stabilize low-symmetry polar phases. In addition, the driving forces behind atomic displacements are often closely linked to electronic structure effects, including orbital hybridization,[50] the projected density of states,[50] interatomic force constants,[51] and Born effective charges.[52] These factors further clarify how changes in electronic structure drive lattice distortions and ultimately lead to ferroelectricity.

# 2.1. Origin of Ferroelectricity in 2D Materials

In intrinsic 2D ferroelectrics, polarization arises from the combined contributions of both electronic and ionic components. Based on symmetry-breaking modes, the polarization mechanisms of 2D ferroelectric materials can be roughly classified into six types, as illustrated in and . Most Figure 3 Table 12D ferroelectrics exhibit multiple polarization mechanisms simultaneously. For instance, the ??-phase $\mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ displays multiple coexisting ferroelectric mechanisms. In In Se , the displacive ferroelectricity involves IP polarization induced by the lateral displacement of In and Se atoms, as well as OOP polarization arising from the vertical displacement of the central Se layer.[12,15] These two polarization directions coexist, leading to biaxial ferroelectricity.[53] Some studies suggest that order– disorder-like behavior may also be present during the phase transition from the high-temperature ??-phase to the low-temperature ??-phase, although the dominant mechanism remains ionic displacement. In multilayer $\mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ , sliding ferroelectricity arises

from changes in stacking symmetry due to interlayer translation, allowing reversible switching between ferroelectric and antiferroelectric states.[54]

# 2.1.1. Displacive Ferroelectricity

Displacive ferroelectricity is one of the most common mechanisms underlying the emergence of ferroelectricity in materials, in which polarization originates from the displacement of ions or atoms away from their centrosymmetric positions within the crystal lattice. When the crystal structure undergoes a phase transition from a high-symmetry (non-polar) phase to a lowsymmetry (polar) phase, the central ions or atoms in the unit cell shift from their equilibrium positions. These displacements break the symmetry of the system and result in spontaneous polarization, where the positive and negative charges are separated, giving rise to a dipole moment at the atomic scale. The critical feature is that the polarization is directly related to the degree of ion displacement. In 2D materials like In2Se3, [12] SnTe,[18] and GeTe,[8,55] this mechanism is observed. In monolayer SnTe, spontaneous IP polarization arises from the relative displacement between Sn and Te atoms in its puckered lattice (Figure 3a, top). The FE stems of ??-In $\phantom { } _ { 2 } \mathrm { S e } _ { 3 }$ from the vertical displacement of Se atoms in the center (Figure 3a, down). In monolayer GeTe, displacive ferroelectricity arises from a relative lateral displacement between Ge and Te atoms, which breaks the inversion symmetry of the lattice and induces strong IP spontaneous polarization. In its paraelectric phase, Ge and Te atoms are symmetrically arranged within a hexagonal lattice. Upon transitioning to the ferroelectric phase, Ge atoms shift off-center relative to Te atoms, forming a polar structure. This distortion is driven by the softening of transverse optical phonon modes, a signature of displacive ferroelectricity, and leads to a characteristic double-well potential energy surface. First-principles calculations reveal that this displacement is stabilized by the competition between short-range repulsion and long-range Coulomb interactions, as well as the hybridization between Ge 4s and Te 5p orbitals, which contributes to the energy gain in the polar structure. Monolayer GeTe exhibits robust IP polarization (≈2–4 μC cm−2) and a high Curie temperature exceeding 500 ${ \mathrm { K } } ^ { [ 1 1 ] }$

# 2.1.2. Sliding Ferroelectricity

Sliding ferroelectricity emerges in vdW layered materials, where relative sliding between adjacent atomic layers breaks inversion symmetry and generates spontaneous polarization. Unlike displacive ferroelectricity, where polarization originates from intralayer ionic displacements, sliding ferroelectricity is interlayer in nature, driven by the stacking arrangement and lateral translation of atomic planes. This mechanism is governed by weak interlayer vdW interactions, which allow for low-energy sliding between layers. The polarization is often OOP and strongly dependent on the stacking configuration (e.g., AA, AB, BA). Sliding ferroelectricity is switchable via lateral electric fields or mechanical shear strain, which can shift one layer relative to another. The energy barrier for switching is often low due to the weak interlayer bonding, making this type of ferroelectricity promis-

![](images/207309b3baedd910b2d881b22e053838fe553717ff5d756c5afb0650919e0e5d.jpg)  
a

![](images/c3468813e3eeb161e9c193d604ea898976cb0bff87b2f5ef74d56351380f9ee1.jpg)

![](images/58de9163ec31608cf250af777eb9b0c31c67dbf0f011808f35b7d81a5ca3c4dd.jpg)  
d   
Conventional ferroelectrics

![](images/1e43ca4d72e57678000b3b5d2b33dc4dbe3d9f03dc02b72a2337c5cef7f1414c.jpg)

![](images/44e557ce81df363b6be425a28c97a995ecb366d40bc9be9c7b7c7d77a41791c8.jpg)  
e

![](images/8449cf0e1fc5c7d23d185a1315ec37954dc0cb2897ec92f3eba9fae0e5cc5565.jpg)

![](images/83f452a854680d5654a0330832ed4c0e1ab3c88776968559fcc4bb954f2b3709.jpg)  
Figure 3. Representative mechanisms of 2D ferroelectricity. a) Displacive ferroelectricity in monolayer SnTe. The ferroelectricity originates from relative lateral displacements of Ge and Te atoms (top). Reproduced with permission.[18] Copyright 2016, The American Association for the Advancement of Science. In $\mathsf { I n } _ { 2 } \mathsf { S e } _ { 3 } ,$ the vertical displacement of Se atoms relative to In atoms breaks the inversion symmetry and induces spontaneous polarization 2 3(down).[12] Copyright 2017, The Authors, published by Springer Nature. b) Sliding ferroelectricity in layered SnSe. Relative sliding between atomic layers (AA, AB, and different R stacking configurations) breaks centrosymmetry and induces polarization $\mathsf { \Gamma } ( \mathsf { t o p } ) . \mathsf { I } ^ { 3 7 ] }$ Copyright 2015, The Authors, published by Springer Nature. In bilayer TMDs, H-stacking with antiparallel layers restores inversion symmetry and gives zero net polarization, while r-stacking with parallel MX or XM alignment induces ${ \mathsf { O O P } }$ polarization (−P or +P) due to vertical atomic asymmetry (down). Reproduced with permission.[60] Copyright 2022, Springer Nature. c) Improper ferroelectricity in ${ \mathsf { T I } } _ { 2 } { \mathsf { S } } .$ . Interlayer twisting stabilizes ferroelectricity by coupling structural instabilities with polar distortions, leading to ${ \mathsf { P } } \neq 0 .$ . Reproduced with permission $. [ 3 8 ]$ Copyright 2024, American Chemical Society. d) Electronic ferroelectricity in TTF-CA. Polarization arises mainly from electronic charge redistribution, as revealed by the opposite direction of ionic and electronic contributions. Reproduced with permission $\cdot ^ { [ 3 9 ] }$ Copyright 2012, American Physical Society. e) Order–disorder ferroelectricity in CIPS. ${ \mathsf { C u } } ^ { + }$ ions switch between off-center sites, resulting in a double-well potential and ferroelectric ordering upon cooling. Reproduced with permission $\cdot ^ { [ 7 1 ] }$ Copyright 2023, John Wiley and Sons. f) Domain-wall and flexoelectric-induced ferroelectricity in CIPS. Flexoelectric control enables artificial stripe domains with local ferroelectricity, confirmed via piezoresponse force microscopy phase imaging. Reproduced with permission.[73] Copyright 2022, American Chemical Society.

Table 1. Summary of Ferroelectric Mechanisms and Parameters in 2D ferroelectric semiconductors.   

<table><tr><td>Mechanisms</td><td>Materials</td><td>Polarization direction</td><td>Tc[K]</td><td>Ec</td><td>P</td><td>Refs.</td></tr><tr><td rowspan="5">Displacive</td><td>α-In2Se3</td><td>OOP + IP</td><td>473</td><td>0.1–0.4 V nm-1</td><td>7–8 μC cm-2</td><td>[27]</td></tr><tr><td>SnTe</td><td>IP</td><td>270</td><td>-</td><td>-</td><td>[18]</td></tr><tr><td>GeTe</td><td>IP</td><td>570</td><td>-</td><td>-</td><td>[55]</td></tr><tr><td>CuInP2S6</td><td>OOP</td><td>320</td><td>25–30 kV cm-1</td><td>3–5 μC cm-2</td><td>[77–79]</td></tr><tr><td>SnS</td><td>IP</td><td>&gt;300</td><td>-</td><td>1.8-4.8 C m-1</td><td>[11,17]</td></tr><tr><td rowspan="10">Sliding</td><td>WTe2</td><td>OOP</td><td>350</td><td>-</td><td>0.051 μC cm-2</td><td>[56,80]</td></tr><tr><td>BN</td><td>OOP</td><td>620</td><td>0.3 V nm-1</td><td>0.68 μC cm-2</td><td>[58,81]</td></tr><tr><td>β-InSe</td><td>OOP</td><td>&gt;300</td><td>0.15 V nm-1</td><td>0.375 μC cm-2</td><td>[59,80]</td></tr><tr><td rowspan="4">MX2(M = Mo,W; X = S,Se)</td><td rowspan="4">OOP</td><td rowspan="4">-</td><td rowspan="4">-</td><td>0.77 pC m-1</td><td rowspan="4">[82]</td></tr><tr><td>0.59 pC m-1</td></tr><tr><td>0.69 pC m-1</td></tr><tr><td>0.73 pC m-1</td></tr><tr><td>3R-MoS2</td><td>OOP</td><td>&gt;650</td><td>0.1–0.19 V nm-1</td><td>-</td><td>[83]</td></tr><tr><td>SeSn</td><td>OOP</td><td></td><td></td><td></td><td>[37]</td></tr><tr><td>GaSe</td><td>OOP</td><td></td><td></td><td>6.19 pC m-1</td><td>[84]</td></tr><tr><td rowspan="6">Improper</td><td>TI2S</td><td>OOP</td><td>-</td><td>-</td><td>-</td><td>[38]</td></tr><tr><td>MoTe2</td><td>OOP/IP</td><td>&gt;300</td><td>-</td><td>-</td><td>[85]</td></tr><tr><td>Twisted/Moiré h-BN</td><td>OOP</td><td>&gt;300</td><td>0.1 V nm-1</td><td>0.68 μC cm-2</td><td>[58]</td></tr><tr><td>Bi2O2Se</td><td>OOP</td><td>508</td><td>-</td><td>4.4 pm V-1</td><td>[21,43]</td></tr><tr><td>d1T-MoS2</td><td>OOP</td><td>-</td><td>-</td><td>-</td><td>[86]</td></tr><tr><td>Hf2VC2F2</td><td>c-axis</td><td>&gt;300</td><td>-</td><td>0.27 μC cm-2</td><td>[87]</td></tr><tr><td rowspan="3">Electronic</td><td>TTF-CA</td><td>a/c-axis</td><td>71</td><td>-</td><td>6.3 μC cm-2</td><td>[39]</td></tr><tr><td>Sc2CO2</td><td>OOP</td><td>300–600</td><td>2.5 V nm-1</td><td>1.6 μC cm-2</td><td>[88,89]</td></tr><tr><td>1T&#x27;-WTe2</td><td>IP</td><td>350</td><td>-</td><td>0.2–0.4 μC cm-2</td><td>[56]</td></tr><tr><td rowspan="3">Order-disorder</td><td>CuInP2S6</td><td>OOP</td><td>333 K</td><td>200 kV cm-1</td><td>3–4 μC cm-2</td><td>[71]</td></tr><tr><td>CuCrP2S6</td><td>OOP</td><td>305–320</td><td>-</td><td>14.97 μC cm-2</td><td>[16]</td></tr><tr><td>CuBiP2Se6</td><td>OOP</td><td>-</td><td>-</td><td>-</td><td>[90]</td></tr><tr><td rowspan="3">Domain-wall</td><td>WTe2</td><td>OOP</td><td>350</td><td>1–10 GV m-1</td><td>0.3–0.5 μC cm-2</td><td>[56,91]</td></tr><tr><td>Twisted/Moiré h-BN</td><td>OOP</td><td>&gt;300</td><td>0.1 V nm-1</td><td>0.68 μC cm-2</td><td>[58]</td></tr><tr><td>SnSe</td><td>400</td><td>&gt;300</td><td>-</td><td>-</td><td>[92]</td></tr></table>

ing for low-power applications. In 2018, Fei et al. experimentally demonstrated sliding ferroelectricity for the first time in fewlayer $\mathbb { W } \mathrm { T e } _ { 2 } . ^ { [ 5 6 ] }$ Subsequently, in 2019, Sharma et al. further confirmed the presence of OOP ferroelectricity in bulk $\mathrm { W T e } _ { 2 }$ using piezoresponse force microscopy $( \mathrm { P F M } ) . ^ { [ 5 7 ] }$ In 2020, Yasuda et al. designed a dual-gated van der Waals heterostructure device, in which monolayer graphene was used as a detector to quantitatively probe the polarization of bilayer BN.[58] Sliding ferroelectricity has also been observed in semiconducting van der Waals layers. For instance, Hu et al. detected clear amplitude butterfly loops and phase hysteresis in ≈7 nm-thick ??-InSe via PFM, revealing reversible OOP polarization switching.[59] In 2021, Wang et al. identified sliding ferroelectricity in bilayers of a series of transition metal dichalcogenides (TMDs), including MoS , WS , MoSe , and $\mathrm { W S e } _ { 2 } . \mathrm { } ^ { [ 6 0 ] }$ By introducing AA stacking and interlayer sliding in SnSe, Chen et al. induced polarization and uncovered the coupling between OOP and IP polarization in ${ \mathrm { S e S n } } , ^ { [ 3 7 ] }$ as shown in Figure 3b. Therefore, in van der Waals materials with centrosymmetric lattice structures, ferroelectricity can be achieved through interlayer sliding, exploiting the slip-induced polarization mechanism.

# 2.1.3. Moiré/Twistronic Ferroelectricity

Beyond sliding ferroelectricity, recent studies on moiré and twistronic systems have unveiled novel ferroelectric phenomena that greatly enrich the physical picture of 2D polarization. The socalled moiré or twistronic ferroelectricity arises from long-range moiré superlattice potential modulations induced by small twist angles (typically <2°) or lattice-constant mismatches between adjacent layers.[58,61,62] Such periodic potential wells lead to spatial modulation of both electronic states and atomic configurations, resulting in the emergence of polarized domains, soliton lattices, and domain-wall network structures in local regions.[63] When the twist angle approaches a critical small value (<1°), pronounced atomic reconstruction occurs, breaking the original crystalline symmetry and inducing spontaneous polarization in 2D van der Waals bilayers.[64] A typical example is the twisted bilayer hexagonal boron nitride (tBL BN), where slight misalignment and reconstruction of local ionic dipoles between boron and nitrogen atoms under small twist angles induce O polarization and distinct ferroelectric hysteresis behavior. $[ 5 8 , 6 5 , 6 6 ]$ In TMD semiconductors, such as twisted bilayer $\mathsf { W S e } _ { 2 } , \mathsf { M o S e } _ { 2 } , \mathsf { W S } _ { 2 } ,$ and

${ \mathrm { M o S } } _ { 2 } ,$ small-angle twisting generates triangular moiré domain patterns composed of MX and XM stacking regions, separated by domain walls carrying fractionalized polarization charges.[60] Polarization reversal typically proceeds through the motion of domain walls and collective rearrangement of the soliton network, with the associated energy barriers being tunable via twist angle,[67] stacking configuration,[60] and external electric field.[64] Compared with sliding ferroelectricity, moiré ferroelectricity features a fundamentally distinct energy landscape and switching mechanism. The former is dominated by interlayer translation with low energy cost, while the latter involves cooperative reconstruction of soliton domains and domain-wall networks, exhibiting enhanced tunability and strong responsiveness to external fields. This unique programmable polarization behavior offers a new platform for the design of reconfigurable electronic devices, nonvolatile optoelectronic modulators, and quantum information units based on polar solitons.

# 2.1.4. Improper Ferroelectricity

In improper ferroelectrics, polarization is not the primary order parameter but instead emerges as a secondary effect induced by a nonpolar structural distortion, such as rotational, tilt, or lattice modulation modes.[68] This is fundamentally different from proper ferroelectricity, where spontaneous polarization arises directly from a polar instability (e.g., a soft optical phonon mode). In improper ferroelectrics, the polar distortion is driven or stabilized by other nonpolar distortions through anharmonic coupling, typically in the form of trilinear or higher-order coupling terms in the free energy. Improper ferroelectricity is typically found in hybrid improper ferroelectrics, multiferroics, and layered perovskites. Gui et al., based on first-principles calculations, revealed an improper, electronically driven ferroelectric mechanism in $\mathrm { T l } _ { 2 } \mathrm { S }$ induced by structural instability. This improper ferroelectricity originates from an unstable phonon mode $( \mathrm { K } _ { 2 } \mathsf { a } )$ at the Brillouin zone boundary K point $( 1 / 3 , 1 / 3 , 0 )$ , which nonlinearly couples with the intrinsic polar mode $( \Gamma _ { 2 - } )$ to induce OOP polarization[38] (Figure 3c). Unlike conventional iondisplacement-driven ferroelectricity, the resulting polarization arises primarily from electronic redistribution, exhibiting characteristic features of electronic improper ferroelectricity. CIPS is commonly classified as a proper ferroelectric, with its ferroelectricity primarily originating from the displacement of $\mathrm { C u ^ { + } }$ ions along the OOP direction. While this mechanism is characteristic of proper ferroelectricity, recent studies have explored the complex interplay of structural distortions in CIPS. For instance, the coexistence of ferrielectric states and non-piezoelectric surface phases has been observed, suggesting that under certain conditions,[69] polarization in CIPS may be influenced by secondary structural modes, hinting at improper ferroelectric behavior.

# 2.1.5. Electronic Ferroelectricity

Electronic ferroelectricity is characterized by spontaneous polarization that arises predominantly from the redistribution of electronic charge, rather than from ionic displacements. In such

systems, a shift in the electronic charge center relative to the ionic lattice generates a net electric dipole, even when atomic positions remain essentially unchanged. This mechanism is distinct from conventional displacive ferroelectricity, where polarization results from symmetry-breaking ionic movements. The origin of polarization in electronic ferroelectrics typically lies in changes to the electronic band structure, charge density rearrangement, or orbital hybridization. Due to the ultrafast response of electronic degrees of freedom, this type of ferroelectricity holds promise for high-speed electronic and optoelectronic devices. Electronic ferroelectricity is an intrinsic polarization mechanism driven by electronic behavior itself and is commonly found in conjugated organic molecules or certain 2D resonant systems. TTF-CA (tetrathiafulvalene–p-chloranil), despite being 1D, is one of the earliest and most representative materials experimentally confirmed to exhibit electronic ferroelectricity. Kobayashi et al., using Berry phase theory, demonstrated that the polarization direction is opposite to that of ionic displacement, with the ionic contribution being negative and the electronic part dominating the total polarization,[39] as shown in Figure 3d. This confirms that TTF-CA is a prototypical electronic ferroelectric. Monolayer $\mathrm { W T e } _ { 2 }$ is a representative example of this behavior in 2D systems. WTe exhibits switchable IP polarization driven by an asymmetric distribution of electron density across the layer. This asymmetry arises from the material’s intrinsic lack of inversion symmetry and strong spin–orbit interaction. Experimental and theoretical studies have shown that the polarization can be reversed by an applied IP electric field,[56,70] with negligible ionic displacement involved. This confirms the electronic origin of the polarization.

# 2.1.6. Order–Disorder Ferroelectricity

Order–disorder ferroelectricity arises from the thermally driven reorientation of local dipoles associated with discrete atomic configurations. In the paraelectric phase, these dipoles are dynamically disordered due to thermal fluctuations, leading to a vanishing net polarization. Upon cooling, the system undergoes a phase transition in which the dipoles align in a preferred orientation, resulting in spontaneous polarization. This mechanism contrasts with displacive ferroelectricity, where polarization emerges from continuous ionic displacements. A representative example in 2D van der Waals materials is CIPS.[71] In this compound, ferroelectricity originates from the off-center displacement of $\mathrm { C u ^ { + } }$ ions within sulfur octahedra (Figure 3e). At high temperatures, $\mathrm { C u ^ { + } }$ ions reside at centrosymmetric sites, and the system becomes nonpolar. As temperature decreases, the ions shift into energetically favorable off-center sites, leading to an ordered arrangement of local dipoles and a net polarization. Experimental techniques such as piezoresponse force microscopy and second-harmonic generation, along with first-principles calculations, have confirmed the order–disorder nature of this ferroelectric transition.

# 2.1.7. Domain-Wall/Topological Ferroelectricity

Domain-wall ferroelectricity and topological ferroelectricity differ from the intrinsic polarization mechanisms discussed above, as they do not arise from the material’s bulk structural polarity. Instead, the polarization in these cases is localized and

# Extrinsic 2D ferroelectric semiconductors

![](images/92541b5bd7d26bbede472b87f8cf64b87f8429cfc1a1e3773aa04f74f8010c15.jpg)

![](images/92754f4d7853d80471845078fe648d5c363436e9255e45712a4fdf97503b4e97.jpg)

![](images/71976c9cfaf306c6c3e8562cbe2b489fe3e88fa5390441e4160fd012cb62ecbe.jpg)

![](images/91c21ee69342d36f315671076f513f1bb1d029e3eb504a6bbbf8b4b6d8d8bafe.jpg)

![](images/4b2715200aa5bcbdf5aa2ee2e8ad64e15a52f47bb74d2e22719d2f168beae7ea.jpg)

![](images/9682cce27c13b1d76d824e06aedcd0d71babde30e66e62ad05396a5a9c60ee09.jpg)

![](images/ec04fd5c6eae4176c1302cd39bbc5a63f650baab977c0a8b6b1f9638c532475c.jpg)  
Rigid twist

![](images/b7409a62cba06297cb3d7847d016f9b027173b5e147d808dc8d63f5e04ca8791.jpg)  
Twisted WSe2 bilayers

![](images/3ab1eebbaaca8d1186adf448b8e5164a56ca0fe20727a1b7478517016be0ece4.jpg)

![](images/06ed9b08061a852b3518381f31af09ea1a2145090026a9767020dd7dfad28d2a.jpg)

![](images/3298b32f72acca3382ad1e9635536dfb89ba7f36cdd5ee211ccd6d2faa24b0fe.jpg)

![](images/af2eace7ca04ad642e3a7b7c785d79b42b4ebeacc6fcf29dbf69ea8743f3021e.jpg)  
Figure 4. Extrinsic 2D ferroelectric semiconductors. a) Strain-induced ferroelectric behavior. Reproduced with permission.[120–122] Copyright 2020, John Wiley and Sons; Copyright 2023, John Wiley and Sons; Copyright 2023, Springer Nature. b) Electric field-driven polarization switching. Reproduced with permission.[83] Copyright 2022, Springer Nature. c) Doping and interface engineering. Reproduced with permission.[123] Copyright 2018, American Physical Society. d) Twisting-induced ferroelectricity. Reproduced with permission.[124,125] Copyright 2021, The American Association for the Advancement of Science. Copyright 2024, John Wiley and Sons. e) Magnetic-field-driven spin texture-induced ferroelectricity. Reproduced with permission.[14] Copyright 2022, Springer Nature. f) Domain engineering for local polarization control. Reproduced with permission.[126] Copyright 2019, American Chemical Society.

![](images/caf6a77141a2d67fb4370457f7c34bea320f72530c29ab4ba48f2a4b4cdfb93c.jpg)  
a   
Ferroelectric insulator

![](images/542ddd9b9297c72f0d87d5c81b66194b66d62db7b82a6f21a8ff3394466248dc.jpg)  
Ferroelectric semiconductor

![](images/37fd59ba99cd297c7415d53611f3cfb20a1234b6325c8a06aeb4ea3142d17c14.jpg)

![](images/616a4f511ec77d0db9b909b54c3138e328be1664be4dbc887f050535c05d3ed5.jpg)

![](images/ae70849dda372032c37df3835a08a6487d73765cc9f450a17623a50fe9ff52fe.jpg)  
C

![](images/7e6cd76be712b7661e53a407429bd6c663d8571488f52272455dcbb5e178ebae.jpg)  
a

![](images/39a377d2e4bdb587907cbc04e34438e27ac874b0befb7e877055ef18465a29e5.jpg)  
e

# In2Se3

# SnSe

![](images/1e5d13fc06393369b2c0ce27ceb30d97071770ce6e15e491da03c5b1bd112daf.jpg)  
f

![](images/c6da964495c46cb36c7e3ef445249b24eb27828bd046bfe5b039a0ef6e57b188.jpg)  
g

![](images/7a1a4f0d1ba100d86b1ff9dd45f0d53d00c60925b7885b6b9d3d2c5eb06de7b6.jpg)

![](images/829ec150a6a69024e3a76c171da6127b484494c7d1e9a059d9fcf4f5d9ac348e.jpg)  
h

![](images/4ea24057f9b7b921aebab09902108c289a8aa28f4f9895bb7a031f10adff5785.jpg)

![](images/76acd8e24f017e8136f0ae7266e2e8f93eed0fb9934313bf79eac8899cbe8995.jpg)  
j

![](images/7c08490f361a2ab60f0ade763d3ce5b2baa13b1acc7ee030ad38862c0d0c190f.jpg)

![](images/aa3e15c9d8e3ef3e6d58628036fcdfae8dccf839e74b86fc0c122b603da7b5a3.jpg)  
k

![](images/6af2ad3e5bcd6bdff2824cc49ab0cb5c9387f3e05653b74f48e502a62fad8617.jpg)  
一

![](images/19e817173504c609937724a8f3821e8830d639b43f23f388240d2d705444c578.jpg)  
m

![](images/1aff69c134325cbc5e848a43d28a2435d19c529c6ba7eb8ce697239fa3d224c7.jpg)

![](images/f655f758c1a89c1236b35d4c83f4549ab2b42739cabf0a1e21bddfcceb9d8066.jpg)  
0

![](images/4eaaad9f00d2eb06e21155381f1ec70884a01e5f4a650685988cb627627b1774.jpg)  
p

![](images/7d795d1113b294229aa3a271cb043e23765f9a3e941c3b827690a9d146dc2dd2.jpg)  
q   
Figure 5. Applications of ferroelectric semiconductors in electronics. a) Schematic diagrams of ferroelectric transistors and ferroelectric semiconductor transistors. b) Lattice structures of $\mathsf { I n } _ { 2 } \mathsf { S e } _ { 3 }$ with different polarization orientations. c) $I _ { \mathsf { D } } { - } V _ { \mathsf { D } \mathsf { S } }$ characteristics at room temperature of a typical $\alpha \cdot | \mathsf { n } _ { 2 } \mathsf { S e } _ { 3 }$ FeS-FET with 90 nm SiO gate dielectric and ALD passivation, featuring a 1 μm channel length and 52.2 nm thickness. Reproduced with permission.[27] Copyright 2019, Springer Nature. d) ??-In $\phantom { } _ { 2 } S e _ { 3 }$ electronic synapse schematic. e) Long-term potentiation by 50 pulses (2 V, 100 ms) and long-term depression by 50 pulses $( - 2 \lor , \ 7 0$ ms), with $\mathsf { a } - 0 . 1$ V bias for state readout. Reproduced with permission.[42] Copyright 2022, Springer Nature. f) Top view of monolayer group-IV monochalcogenide structure (left). Schematic side views of two distorted degenerate polar structures (B and B′) (right). Reproduced with permission.[11] Copyright 2016, American Physical Society. g) Schematic of the Au/SnSe/NSTO memristor structure and 2D SnSe. h) Current of the SnSe device in ON and OFF states under low bias. i) The device current stabilizes after an 800 ns pulse with a ΔI of ≈1.47 μA. Reproduced with permission.[144] Copyright 2020, RCS Pub. j) Layered crystal structure of $_ { \mathsf { B i } _ { 2 } \mathsf { O } _ { 2 } \mathsf { S e } }$ and its lattice structure under strain. Reproduced with 2 2permission.[21,146] Copyright 2019, American Chemical Society; Copyright 2017, American Chemical Society. k) Back-gate FETs based on ${ \tt B i } _ { 2 } { \sf O } _ { 2 } { \sf S e }$ thin films. l) PFM phase images of ${ \tt B i } _ { 2 } { \tt O } _ { 2 }$ 2 2Se after Panda pattern writing with ±10 V DC voltage. Reproduced with permission.[147] Copyright 2024, John Wiley 2 2and Sons. m) Normalized conductance states of the ${ \tt B i } _ { 2 } { \tt O } _ { 2 }$ Se memristor versus the number of applied pulses. Reproduced with permission.[148] Copyright 2017, American Chemical Society. n) CIPS crystal structure.[13] Copyright 2016, The Authors, published by Springer Nature. o) Schematic of the ClPS resistive switching device on $\mathrm { S i O } _ { 2 } / \mathrm { S i }$ i substrate. p) Typical I–V curves of the Ag/ClPS/Au device under different constant current conditions. Reproduced 2               with permission.[135] Copyright 2023, Springer Nature. q) I–V characteristics of the ON and OFF states for bilayer graphene/CIPS/Cr heterostructures. Reproduced with permission.[28] Copyright 2020, Springer Nature.

Table 2. Representative 2D ferroelectric devices and their key performance metrics.   

<table><tr><td>Device type</td><td>Material system</td><td>On/off ratio</td><td>Memory window</td><td>Operating voltage</td><td>Retention</td><td>Endurance</td><td>Refs.</td></tr><tr><td rowspan="5">FeS-FET</td><td>α-In2Se3</td><td>≈108</td><td>≈4 V</td><td>±6 V</td><td>-</td><td>-</td><td>[27]</td></tr><tr><td>α-In2Se3</td><td>≈105</td><td>≈13 V</td><td>±10 V</td><td>-</td><td>&gt;102 cycles</td><td>[127]</td></tr><tr><td>α-In2Se3</td><td>≈105</td><td>≈5 V</td><td>±8 V</td><td>&gt;102s</td><td>&gt;102 cycles</td><td>[24]</td></tr><tr><td>α-In2Se3</td><td>≈105</td><td>≈3 V</td><td>±5 V</td><td>&gt;103s</td><td>&gt;103 cycles</td><td>[128]</td></tr><tr><td>Bi2O2Se</td><td>≈104</td><td>20 V</td><td>±50 V</td><td>-</td><td>-</td><td>[129]</td></tr><tr><td rowspan="2">FeFET</td><td>CIPS</td><td>107</td><td>≈120 V</td><td>±80 V</td><td>104s</td><td>300 cycles</td><td>[130]</td></tr><tr><td>CIPS</td><td>106</td><td>≈15 V</td><td>±10 V</td><td>104s</td><td>104 cycles</td><td>[131]</td></tr><tr><td rowspan="2">FSJ</td><td>α-In2Se3</td><td>&gt;104</td><td>-</td><td>-</td><td>&gt;104s</td><td>&gt;106 cycles</td><td>[132]</td></tr><tr><td>SnS</td><td>&gt;20</td><td>-</td><td>-</td><td>≈103s</td><td>104 cycles</td><td>[133]</td></tr><tr><td>FTJ</td><td>CIPS</td><td>TER≈106</td><td>-</td><td>-</td><td>&gt;104s</td><td>&gt;104 cycles</td><td>[28]</td></tr><tr><td rowspan="2">Memristor</td><td>Bi2O2Se</td><td>1010</td><td>-</td><td>-</td><td>104s</td><td>&gt;102 cycles</td><td>[134]</td></tr><tr><td>CIPS</td><td>103</td><td>-</td><td>-</td><td>104s</td><td>&gt;102 cycles</td><td>[135]</td></tr><tr><td rowspan="3">FeFET</td><td>P(VDF-TrFE)</td><td>104</td><td>≈2 V</td><td>±6 V</td><td>104s</td><td>102 cycles</td><td>[136]</td></tr><tr><td>HZO</td><td>105</td><td>-</td><td>±1.5 V</td><td>108s</td><td>104 cycles</td><td>[137]</td></tr><tr><td>PZT</td><td>107</td><td>≈2 V</td><td>±3.5 V</td><td>&gt;104s</td><td>&gt;102 cycles</td><td>[138]</td></tr><tr><td rowspan="2">FeS</td><td>Advantage</td><td></td><td colspan="5">High retention and low charge trapping</td></tr><tr><td>Disadvantage</td><td></td><td colspan="5">Low polarization and low industrial applicability</td></tr><tr><td rowspan="2">Traditional Fe</td><td>Advantage</td><td></td><td colspan="5">high polarization and high industrial applicability</td></tr><tr><td>Disadvantage</td><td></td><td colspan="5">Bulk scale layer and environmental issues</td></tr></table>

non-intrinsic. In certain 2D materials that are globally nonferroelectric or weakly ferroelectric, local symmetry breaking at domain walls can induce spontaneous polarization, resulting in localized ferroelectric behavior. Strain is an effective approach to induce ferroelectricity at domain walls. In $\mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 } ,$ local polarization can be generated through bending or localized stress, resulting in ferroelectric domains of varying sizes.[72] In 2D CIPS, large-scale stripe-like ferroelectric domains can be formed via the flexoelectric effect, enabling mechanical control of polarization,[73] as shown in Figure 3f. In bilayer $\mathrm { M o T e } _ { 2 } [ 7 4 ]$ and $\mathrm { W T e } _ { 2 } , ^ { [ 5 6 ] }$ the polarization direction can be modulated by the position of domain walls. Topological ferroelectricity refers to the formation of ferroelectric domain configurations with topological features, such as vortices, skyrmions, or loop structures. These topological polar structures often exhibit enhanced stability and tunability, and are typically observed in hexagonal ferroelectrics or systems with strong domain coupling. Monolayer $\mathrm { W T e } _ { 2 }$ is regarded as a representative 2D material exhibiting topological ferroelectricity.[56] Its ferroelectricity arises from the reconstruction of orbital electronic states following lattice symmetry breaking, even in the absence of significant ionic displacement. The spontaneous polarization originates from anomalous orbital currents and Berry curvature, indicating an electronic topological origin of the ferroelectric behavior.[75,76]

# 2.2. Unique Properties of 2D Ferroelectric Semiconductor

# 2.2.1. Coexistence of Ferroelectricity and Semiconducting Behavior

2D ferroelectric semiconductors exhibit unique physical properties not found in conventional ferroelectric materials, particularly the coexistence of spontaneous polarization and semicon-

ducting behavior. While traditional ferroelectrics such as $\mathrm { B a T i O } _ { 3 }$ and ${ \mathrm { P b T i O } } _ { 3 }$ are typically wide-bandgap insulators with limited charge transport capabilities, 2D materials like $\mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ , SnTe, $\mathrm { S n S } , \mathrm { 1 T \cdot M o T e } _ { 2 }$ , and ${ \mathrm { B i } } _ { 2 } { \mathrm { O } } _ { 2 }$ Se combine robust ferroelectricity with moderate,[93] tunable band gaps in the range of approximately one to two electronvolts. In these systems, polarization can directly modulate carrier distribution and band alignment via the internal electric field, enabling control over conduction type and allowing for self-powered device operation without external gate voltages. Their atomic-scale thickness and clean surfaces minimize leakage current, a major limitation in bulk ferroelectric oxides. This intrinsic coupling between polarization and semiconducting properties provides a versatile platform for multifunctional, low-power, high-density electronic and optoelectronic devices. Additionally, ferroelectric states in these materials can be effectively tuned through external strain,[15,94–96] offering further opportunities for precise control over their electronic and optical functionalities.

# 2.2.2. Low Switching Barrier and Single-Layer Ferroelectric Scalability

In 3D ferroelectrics, OOP polarization is typically suppressed due to depolarization effects, which limit the stability of ferroelectricity at ultrathin dimensions. For instance, in ${ \mathrm { B a T i O } } _ { 3 }$ thin films, ferroelectric polarization vanishes when the thickness falls below six unit cells.[97] Although some conventional ferroelectrics can maintain polarization at reduced thicknesses, such as 2.4 nm for $\mathrm { B a T i O } _ { 3 } , ^ { \overline { { { [ 9 7 ] } } } }$ 1.2 nm for $\mathrm { P b T i O } _ { 3 } , { } ^ { [ 9 8 ] }$ one unit cell for $\mathrm { B i F e O } _ { 3 } , { } ^ { [ 9 9 ] }$ and 1.5 unit cells for $\mathrm { P b } { \mathrm { Z r } } _ { 0 \cdot 2 } \mathrm { T i } _ { 0 \cdot 8 } { \mathrm { O } } _ { 3 } , { \mathrm { } } ^ { [ 1 0 0 ] }$ this typically requires carefully engineered ferroelectric–electrode interfaces with sufficient carrier densities to screen depolarizing

fields or the application of compressive strain from the substrate to stabilize stripe domain structures. In contrast, 2D vdW materials can be exfoliated down to the monolayer limit without dangling bonds, effectively overcoming thickness-related limitations. According to Li et al., monolayer SnTe exhibits stable IP ferroelectricity with a transition temperature of 270 K, attributed to enhanced quantum confinement and increased in-plane lattice distortion.[18] Biswas et al. reported that ultrathin $_ { \mathrm { B i _ { 2 } O _ { 2 } S e } }$ nanoflakes exhibit robust OOP ferroelectricity at room temperature, driven by broken inversion symmetry caused by orthorhombic distortion.[101] Yuan et al. found that monolayer $\mathrm { 1 T } { \cdot } \mathrm { M o T e } _ { 2 }$ displays OOP ferroelectricity at room temperature, with a transition temperature exceeding $3 \dot { 3 } 0 \mathrm { K } . ^ { [ 2 0 ] }$ ] Moreover, at atomic-scale thickness, the energy barrier for polarization switching is reduced, enabling polarization control under low voltages using vertical or lateral electric fields. The thermal stability, hysteresis behavior, and switching speed of the polarization state in 2D structures can also be tuned through layer number, strain, or interfacial engineering.

# 2.2.3. Negative Piezoelectric Coefficients

The negative piezoelectric coefficient, especially the negative longitudinal piezoelectric effect (NLPE), describes an atypical electromechanical behavior where polarization increases under compressive strain along the polarization axis. This contrasts with the conventional effect, where polarization typically decreases. NLPE is frequently observed in 2D vdW layered materials due to their structural anisotropy and unique interlayer interactions. The piezoelectric response includes two components: the clampedion term, reflecting polarization change with fixed atomic positions, and the internal-strain term, arising from atomic relaxations. A dominant negative contribution from either term results in a negative overall response. In $\mathsf { S } \mathsf { b } _ { 2 } \mathsf { T e S e } _ { 2 } , \mathsf { \Omega } ^ { [ 1 0 2 ] }$ both terms are strongly negative, yielding a longitudinal piezoelectric coefficient of $\stackrel { \cdot } { \approx } - 3 2 . 6 6 6 ~ \mathrm { p C } ~ \mathrm { N } ^ { - 1 }$ , among the highest known in 2D materials. In multilayer vdW ferroelectrics with OOP polarization, polarization is mainly confined within atomic layers, while interlayer forces are governed by vdW interactions. When an electric field enhances intralayer dipoles, interlayer dipole–dipole repulsion increases, causing vdW gaps to contract. This contraction can outweigh in-plane lattice expansion, reducing the lattice constant along the polarization direction. In CIPS,[103–105] highly mobile Cu ions migrate within layers and across vdW gaps, forming a quadruple-well potential along the z-axis with two energy minima per polarization direction. Intralayer migration corresponds to a low-polarization state $( \pm 4 . 9 3 \mu \mathrm { C } \mathrm { c m } ^ { - 2 } )$ that is strainsensitive, leading to a negative longitudinal piezoelectric coefficient. Migration into vdW gaps yields a high-polarization state $( \pm 1 1 . 2 6 \mu \mathrm { C } \mathrm { c m } ^ { - 2 } )$ with a positive response.

# 3. Classes of 2D Ferroelectric Semiconductors

2D ferroelectric semiconductors have garnered increasing attention due to their unique integration of switchable polarization and semiconducting behavior, enabling novel functionalities in logic, memory, sensing, and optoelectronic applications. A variety of 2D ferroelectric materials have been reported, and although

the origin of ferroelectricity in some cases remains under debate, numerous theoretical studies have offered compelling explanations. Based on the origin of their ferroelectric properties, these materials can be broadly categorized into intrinsic and extrinsic types. Intrinsic 2D ferroelectric semiconductors exhibit spontaneous polarization as a direct consequence of their crystal symmetry and atomic configuration, even down to the monolayer limit. In contrast, extrinsic 2D ferroelectric semiconductors acquire ferroelectricity through external modifications such as interfacial coupling in layered heterostructures, strain engineering, surface functionalization, or defect engineering. This section provides an overview of both classes, with a focus on representative materials and the fundamental mechanisms underlying their ferroelectric behavior.

# 3.1. Intrinsic 2D Ferroelectric Semiconductors

Intrinsic 2D ferroelectric semiconductors exhibit spontaneous polarization arising directly from their low-symmetry crystal structures and specific atomic arrangements, without the need for external stimuli, and they retain ferroelectric properties even at the monolayer limit. In TMDs, numerous ferroelectric semiconductors and ferroelectric metals have been identified, with semiconducting behavior typically associated with the 2H phase (e.g., MoS , WS , MoSe , and WSe ) and metallic or semimetallic behavior more common in the 1T and 1T’ phases (e.g., 1T-MoS , 1T $- \mathrm { { W T e } } _ { 2 } )$ . Bismuth oxychalcogenides such as $\mathrm { B i } _ { 2 } \mathrm { O } _ { 2 } \mathrm { S e } , \mathrm { B i } _ { 2 } \mathrm { O } _ { 2 }$ Te, and $\mathrm { B i } _ { 2 } \mathrm { O } _ { 2 } \mathrm { S }$ represent another class of 2D van der Waals ferroelectric semiconductors that combine high carrier mobility with intrinsic ferroelectricity. Group-IV monochalcogenides, including SnS, SnSe, GeS, GeSe, SiS, and SiSe, have also been reported to exhibit ferroelectricity in their monolayer forms, with some studies indicating potential multiferroic behavior.

Among 2D ferroelectric semiconductor materials, In Se is a prototypical ferroelectric semiconductor, exhibiting both IP and OOP ferroelectricity due to selenium atom displacement relative to the indium sublattice; its monolayer ??-phase breaks inversion symmetry and allows for electrically switchable polarization. Another well-known material is SnTe, a group-IV elemental material with a buckled lattice structure, which shows strong in-plane ferroelectricity driven by spontaneous lattice distortion, and its dipole moment can be reversibly switched under applied bias. CIPS, a wide-bandgap semiconductor (2.6– $3 \mathrm { e V } )$ , displays ferroelectricity due to the relative displacement of cations and anions within its ionic framework, leading to vertical polarization. These intrinsic ferroelectric semiconductors not only provide model systems for exploring polarization switching mechanisms at the atomic scale but also offer significant potential for integration into low-power, non-volatile electronic devices.

# 3.2. Extrinsic 2D Ferroelectric Semiconductors

Engineered 2D ferroelectric semiconductors refer to 2D semiconductors that acquire ferroelectric properties through external modulation strategies such as interfacial engineering, strain, electric fields, twist angles, doping, or magnetic ordering. These

materials are not intrinsically ferroelectric, but their symmetry and electronic structure are engineered to break inversion symmetry and induce a stable polarization.

In ferroelectric–semiconductor heterostructures, the electronic properties of the semiconductor layer can be directly modulated by altering the interfacial polarization charges via altering the polarization state of the ferroelectric layer, thereby enabling non-volatile ferroelectric functionality within the semiconductor layer. A series of ferroelectric–semiconductor coupled systems,[79,94,106,107] such as $\mathrm { P M N . P T } / \mathrm { M o S } _ { 2 } , \mathrm { C I P S } / \mathrm { M o S } _ { 2 } ,$ , and $\mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 } / \mathrm { M o S } _ { 2 }$ , have been developed, in which the coexistence of semiconductor and ferroelectric properties and a strong coupling between semiconductor and ferroelectricity are observed. Moreover, the interfacial interaction between ${ \mathrm { M o S } } _ { 2 }$ and various substrates can also generate a vertical electric field at the interface, whose magnitude can be further tuned optically.[108] In a related study, Weston et al. realized interfacial ferroelectricity in slightly twisted bilayer MoS by forming distinct stacking configurations (e.g., MotSb and StMob), where interlayer charge transfer induces spontaneous polarization.[61] In stacked vdW devices, aligning all polarization directions requires substantial energy to bend and merge adjacent domain walls. Studies have demonstrated that near-field infrared nanoimaging and nanophotocurrent techniques can visualize moiré ferroelectricity in graphene/twisted-WSe heterostructures, enabling its investigation at the native length scale.[65]

The Janus structure provides an effective approach for constructing ferroelectric-like materials, in which polarization originates from the chemical asymmetry of the crystal lattice. Owing to the different anions on the top and bottom layers (e.g., the electronegativity difference between S and Se in MoSSe), the electron density becomes unevenly distributed along the OOP direction, resulting in a permanent dipole moment.[109] This dipole is fixed within the crystal lattice and cannot be reversed by an external electric field, thereby corresponding to a non-intrinsic polarization rather than genuine ferroelectricity. Under an applied vertical electric field, however, the electronic charge distribution can be modulated, leading to a so-called pseudo-polarization switching. In addition, applying tensile or compressive strain can modify the Mo─X bond length and interlayer spacing, making the two polarization states nearly degenerate. For example, in Janus MoSSe, the vertical dipole moment increases from ≈360 e μm at – 4% strain to 400 e μm at +4% strain.[110] When Janus monolayers are integrated with other layered materials to form heterostructures, interfacial polarization reversal may occur, giving rise to ferroelectric-like coupling behavior.[111] It should be emphasized that these modulation processes do not represent genuine ferroelectric switching, but rather correspond to field-induced redistribution of dipoles. Moreover, bilayer Janus-type TMDs can combine with sliding or twistronic ferroelectricity.[112] Theoretical calculations suggest that interlayer sliding in bilayer MoSSe induces an asymmetric charge redistribution between the upper and lower layers, enabling switchable polarization components both IP and OOP.

Ferroelectricity can also be induced in semiconductors through the employed approach of strain engineering. When a semiconductor is subjected to non-uniform strain or stress, a flexoelectric polarization field may emerge due to the flexoelectric effect,[113–115] allowing for ferroelectric behavior in intrinsi-

cally non-ferroelectric materials.[116,117] For instance, Guo et al. applied non-uniform strain to Complementary Metal–Oxide– Semiconductor (CMOS) technology-compatible silicon devices and successfully induced a polarization field via flexoelectric engineering.[113,118] In suspended ${ \mathrm { M o S } } _ { 2 }$ structures, a highly localized polarization field was generated by introducing a strain gradient using the tip of an atomic force microscope to create nonlinear bending deformations.[119] Similarly, uniform strain applied to PbXs (X = S, Se, and Te),[120] $\mathsf { B i } _ { 2 } \mathsf { O } _ { 2 } \mathsf { S e } , ^ { [ 1 2 1 ] }$ and $3 \mathrm { R } { \cdot } \mathrm { M o S } _ { 2 } [ 1 \bar { 2 } \bar { 2 } ]$ has been shown to effectively induce ferroelectricity in these semiconductors ( a).

Figure 4Electric field modulation represents another effective approach. For example, applying a vertical electric field to multilayer (more than bilayer) 3R ${ \mathrm { M o S } } _ { 2 }$ can drive interlayer sliding, thereby breaking inversion symmetry and inducing polarization[83] (Figure 4b). Doping is also capable of inducing ferroelectric polarization in semiconductors. In monolayer $\mathrm { C r B r } _ { 3 }$ , electron doping breaks orbital degeneracy and results in IP polarization through charge and orbital ordering[123] (Figure 4c). Twist engineering, achieved by adjusting the interlayer twist angle or lateral displacement, offers a similar mechanism[124] (Figure 4d). In bilayer WSe , spontaneous ferroelectric polarization emerges at low temperatures when the twist angle is small.[125] In type-II multiferroic systems, spin textures driven by magnetic fields can give rise to ferroelectric polarization via magnetoelectric coupling. For example, in monolayer ${ \mathrm { N i I } } _ { 2 } ,$ a spin-helix order with inherent chirality breaks spatial inversion symmetry, thereby inducing a finite polarization[14] (Figure 4e). Finally, domain engineering provides a pathway for localized control of polarization. By applying an electrical bias using a conductive scanning probe, local polarization switching has been demonstrated in MoS2/ferroelectric oxide heterostructures[126] (Figure 4f).

# 4. Device Applications

In recent years, the rapid progress of 2D ferroelectric semiconductors has given rise to novel device architectures distinct from conventional ferroelectric insulator structures, as shown in a. summarizes the key parameters of represen-Figure 5 Table 2tative 2D ferroelectric semiconductor devices and traditional ferroelectric devices. In conventional ferroelectric devices such as ferroelectric field-effect transistors (FeFETs), a ferroelectric insulator is used as the gate dielectric to modulate the carrier density in the semiconductor channel. This approach often suffers from issues such as depolarization fields, charge trapping, interface defects, and gate leakage, which limit device performance and reliability. In contrast, 2D ferroelectric semiconductors combine ferroelectricity and semiconducting properties in a single material, enabling their direct use as the channel. Polarization switching takes place within the channel itself, not in the gate dielectric. Mobile carriers in the channel can screen depolarization fields, improving polarization stability. The clean, danglingbond-free surfaces of 2D materials help reduce interface defects. This structure also allows for high on/off ratios and lower power consumption. These characteristics make 2D ferroelectric semiconductors a promising platform for next-generation, highly integrated electronic systems. This section highlights recent advances in related devices, including applications in electronics, optoelectronics, and spintronics.

# 4.1. Electronics

2D ferroelectric semiconductors integrate spontaneous polarization with intrinsic semiconducting behavior, providing an ideal material platform for developing nonvolatile memories, logic transistors, and neuromorphic devices. Their atomic-scale thickness allows efficient electrostatic coupling and facile polarization modulation in vdW heterostructures. Representative 2D FeSCs, including $\boldsymbol { \alpha } { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ , group-IV monochalcogenides (MX, M = Ge, Sn; ${ \mathrm { X } } = { \mathrm { S } } , { \mathrm { S e } } ,$ , and Te), $_ { \mathrm { B i _ { 2 } O _ { 2 } S e } }$ , and CIPS, have demonstrated remarkable ferroelectricity and device functionalities.

# 4.1.1. ??-In Se -Based Devices

$\mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ is a prototypical 2D van der Waals ferroelectric semiconductor, with its monolayer structure composed of a Se─In─Se─In─Se atomic stacking sequence (Figure 5b). Among its five phases $( \alpha , \beta , \gamma , \delta ,$ and ??), the ?? phase is the most stable and exhibits coupledIP and OOP polarization in both 2H and 3R stacking configurations. In 2019, Si et al. developed an $\alpha { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ -based FeS-FET exhibiting an on/off ratio over $1 0 ^ { 8 }$ , an on-state current of 862 $\mu \mathrm { A } \mu ^ { - 1 } \mathrm { ~ m } ^ { - 1 }$ , low operating voltage, and a wide memory window, demonstrating its potential for lowpower non-volatile memory,[27] as shown in Figure 5c. Beyond logic functions, $\alpha { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ has shown promising neuromorphic capabilities. Under electrical stimulation, it exhibits controllable temporal dynamics (Figure 5d). As shown in Figure 5e, synaptic devices based on $\alpha { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ are capable of long-term conductance modulation, including long-term potentiation (LTP) and long-term depression (LTD), achieved by applying multiple identical voltage pulses that induce gradual ferroelectric polarization switching.[42] These properties highlight the potential of ??-In Se -based synaptic devices for brain-inspired computing. In FTJs architectures, ??-In Se also serves as an efficient ferroelectric barrier layer. Si et al. (2021) introduced $\alpha { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ with asymmetric electrodes, achieving an ultrahigh tunneling electroresistance (TER) exceeding $1 0 ^ { 8 } . ^ { [ 1 3 2 ] }$ More recently, a $\mathrm { M o S } _ { 2 } / \alpha { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 } / \mathrm { T i }$ FTJ device exhibited simultaneous room-temperature negative differential resistance and a high TER over 104, further validating its potential for miniaturized multifunctional electronics.[139]

# 4.1.2. Group-IV Monochalcogenides-Based Devices

Monolayer group-IV monochalcogenides (MX, $\mathbf { M } = \mathbf { G e } ,$ Sn; ${ \mathrm { X } } = { \mathrm { S } } ,$ , Se, and Te) were theoretically predicted in 2016 to exhibit large IP spontaneous polarization.[11] Monolayer MX adopts two energetically stable, inversion-related structures, as illustrated in Figure 5f. The discovery of robust IP ferroelectricity in few-layer SnTe by Chang et al. $( 2 0 1 6 ) ^ { [ 1 8 ] }$ initiated intensive experimental efforts on this material family. Subsequent works demonstrated pronounced room-temperature ferroelectricity in $\mathrm { S n S } , ^ { [ 1 4 0 ] }$ SnSe,[92] GeS,[141] GeSe,[142] and ${ \sf G e T e } , ^ { \left[ 1 4 3 \right] }$ confirmed through techniques such as second harmonic generation, PFM, and scanning tunneling microscopy. These monolayers exhibit controllable domain wall motion, domain nucleation, and reversible switching, enabling excellent ferroelectric performance

at the atomic scale. The outstanding IP polarization stability and scalability make MX monolayers promising for ultrathin nonvolatile memories and neuromorphic devices. For example, Wang et al. fabricated ≈28 nm thick SnSe ferroelectric films via pulsed laser deposition and developed $\mathrm { A u / S n S e / N S T O }$ memristors with synapse-like structures (Figure $\dot { 5 } \mathrm { g } ) . \dot { } ^ { [ 1 4 4 \dot { } ] }$ ] The devices exhibit clear bipolar resistive switching (Figure 5h) and emulate synaptic functions through pulse modulation (Figure 5i), achieving current saturation with 800 ns pulses and a minimum energy consumption of 66 fJ.

# 4.1.3. Bi O Se -Based Devices

${ \mathrm { B i } } _ { 2 } { \mathrm { O } } _ { 2 }$ Se is an emerging 2D ferroelectric semiconductor that has attracted attention due to its tunable structure and properties, as well as its potential in electronics, optoelectronics, and energy devices.[145] It is an intrinsic n-type quasi-2D semiconductor with a layered body-centered tetragonal structure $( a = b = 3 . 8 8 7 \mathrm { ~ \AA } _ { \mathrm { { } } }$ , $c = 1 2 . 1 6 4 \mathring { \mathrm { A } } )$ , belonging to the I4/mmm space group (Figure 5j). Although the pristine $_ { \mathrm { B i _ { 2 } O _ { 2 } S e } }$ structure is centrosymmetric, strain can induce piezoelectric or ferroelectric behavior. As shown in Figure 5j (right), in-plane biaxial strain distorts the lattice, causing $\mathrm { S e / O }$ and Bi atoms to shift in opposite directions, resulting in a net polarization along the diagonal. Polarization appears when strain exceeds 1.7% and increases with further strain, reaching 56.1 $\mu \mathrm { C } \mathrm { c m } ^ { - 2 }$ at 4.1%.[146] Since the theoretical prediction of ferroelectricity in ${ \mathrm { B i } } _ { 2 } { \mathrm { O } } _ { 2 }$ Se in 2017, experimental investigations have progressively followed. In 2019, Ghosh et al. fabricated free-standing ${ \mathrm { B i } } _ { 2 } { \mathrm { O } } _ { 2 }$ Se nanosheets with a thickness of $2 \ \mathrm { n m } . ^ { [ 2 1 ] }$ Ferroelectricity was confirmed by hysteresis behavior observed through PFM and local structural distortions revealed by atomicresolution STEM. In 2023, Wang et al. developed $\mathrm {  ~ \Omega ~ } _ { 1 } \mathrm { \ B i } _ { 2 } \dot { 0 } _ { 2 } \mathrm { \ S e }$ FET with an on/off ratio of 104 and a 47% memory window.[43] Wu et al. observed typical butterfly amplitude curves and 180° phase switching in PFM under a 700 nN tip load,[121] with a switching ratio of ${ \approx } 1 0 ^ { 6 }$ . In 2024, Khan et al. used CVD to synthesize 6 nm thick ${ \mathrm { B i } } _ { 2 } { \mathrm { O } } _ { 2 }$ Se flakes and built a FET with a 47.7 μm channel length (Figure 5k),[147] showing a high on/off ratio of $1 0 ^ { 8 }$ and a mobility of ≈131 $\dot { \mathrm { c m } } ^ { 2 } \mathrm { V } ^ { - 1 } \mathrm { \bf S } ^ { - 1 }$ . PFM patterning showed clear 180° phase contrast (Figure 5l), confirming good ferroelectric switching. In 2025, Wan et al. demonstrated a planar ${ \mathrm { B i } } _ { 2 } { \mathrm { O } } _ { 2 }$ Se memristor with over 28 000 switching cycles, fast 400 μs switching, and nearly linear LTP and LTD behavior (Figure 5m),[148] making it promising for energy-efficient computing and memory applications.

# 4.1.4. CuInP S -Based Devices

CIPS is also a typical 2D ferroelectric semiconductor, where OOP polarization arises from the asymmetric vertical displacement of Cu and In ions. This relative displacement induces spontaneous polarization perpendicular to the basal plane. As a wide-bandgap semiconductor with insulating electrical characteristics, CIPS is suitable for use as a gate dielectric or tunneling/barrier layer in ferroelectric devices. CIPS has been widely applied in ferroelectric memristors, ferroelectric diodes (FDs), FTJs, and FeFETs. For example, Ag/CIPS/Au-based memristors (Figure 5o,p) exhibit excellent non-volatile memory behavior, with an on/off ratio of 103

and data retention exceeding $1 0 ^ { 4 } \ \mathbf { s } , ^ { [ 1 3 5 ] }$ enabling both selection and memory functions.

In a CIPS/Si heterostructure FD, Liu et al. demonstrated an $\mathrm { { \ o n / o f f } }$ ratio of ${ \approx } 1 0 0 , ^ { \left[ 1 3 \right] }$ comparable to oxide-based devices, with resistive switching clearly observed at 1.3 V due to polarization reversal in the CIPS layer. Similar switching performance was also observed in Au/CIPS/Cr and Au/CIPS/Ni metal– ferroelectric–metal structures, with on/off ratios up to $1 0 ^ { 3 } . ^ { [ 1 4 9 ] }$ In FTJs, CIPS as a ferroelectric barrier layer, combined with asymmetric graphene/Cr electrodes, enabled tunneling resistance ratios exceeding $1 0 ^ { 7 } , ^ { [ 2 8 ] }$ as shown in Figure 5q. Further enhancement was achieved by inserting monolayer ${ \mathrm { M o S } } _ { 2 }$ or ${ \tt W S e } _ { 2 }$ at the CIPS/graphene interface, yielding van der Waals FTJs with TER ratios above $1 0 ^ { 1 0 } , ^ { [ 1 5 0 ] }$ significantly surpassing that of conventional FTJs. In FeFETs, replacing conventional ferroelectrics with CIPS improves interface quality and integration density. A $\mathrm { M o S } _ { 2 } / \mathrm { C I P S }$ van der Waals FeFET showed a subthreshold swing (SS) below the Boltzmann limit across seven decades of drain current, with a minimum SS of 28 mV $\mathsf { d e c } ^ { - 1 } , \mathsf { l } ^ { 1 5 1 } ]$ indicative of negative capacitance behavior. Furthermore, when ${ \mathrm { M o S } } _ { 2 }$ is replaced by the ferroelectric semiconductor $\mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 } , ^ { [ 1 3 1 ] }$ the interfacial dipole coupling between CIPS and $\mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ leads to enhanced electrical performance. The resulting $\mathrm { C I P S } / \alpha { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ heterostructure device exhibits a wide memory window, an on/off current ratio exceeding 106, stable data retention over $1 0 ^ { 4 } { \bf s } ,$ and endurance over $1 0 ^ { 4 }$ switching cycles.

# 4.2. Optoelectronics

2D ferroelectric semiconductors switchable polarization fields can modulate band alignment, carrier dynamics, and light– matter interactions, enabling reconfigurable photodetection, optical memory, and neuromorphic computation. Compared with conventional bulk ferroelectrics, 2D FeSCs offer tunable band gaps across the visible–infrared range, strong light–polarization coupling, and intrinsic multifunctionality, allowing them to simultaneously serve as the light absorber, ferroelectric layer, and conductive channel in a single device.

# 4.2.1. Electro–Optical Coupling in $\alpha \cdot I n _ { 2 } S e _ { 3 }$

A prototypical example is $\alpha { \mathrm { - I n } } _ { 2 } { \mathrm { S e } } _ { 3 }$ , which exhibits robust roomtemperature ferroelectricity and a moderate bandgap (1.3– 1.5 eV).[12] Its coupled ferroelectric and semiconducting nature allows simultaneous optical and electrical modulation within one material. In photodetectors, $\alpha { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ delivers a photoresponsivity as high as $2 . 8 6 \times 1 0 ^ { 6 } \mathrm { A W ^ { - 1 } }$ and detection sensitivity down to ≈20 photons, owing to the synergistic effect of ferroelectric and photovoltaic responses.[152] It also demonstrates long data retention (>10 years), high on/off ratio $( \approx 2 . 9 \times 1 0 ^ { 5 } )$ , and endurance beyond $1 0 ^ { 6 }$ cycles, suitable for nonvolatile optoelectronic memory.

Liu et al.[42] developed a photonic synaptic device based on ??- In Se ( a), achieving for the first time electro–optical dual Figure 6modulation of synaptic plasticity. As shown in Figure 6b, increasing the light intensity from 0 to 1.29 mW $\mathrm { c m } ^ { - 2 }$ leads to a significant increase in the current levels during both set and reset pro-

cesses, due to the injection of photogenerated carriers. In addition, the inhibitory postsynaptic current (PSC), triggered by electrical pulses under varying light intensities, gradually diminishes with increasing light intensity, which is attributed to shortened relaxation times and reduced accumulative effects (Figure 6c). Figure 6e further confirms a negative correlation between relaxation time and light intensity, indicating that stronger illumination can effectively accelerate the dynamic recovery of the device. The temporal interplay between optical and electrical pulses is illustrated in Figure 6d. When a light pulse precedes an electrical pulse (Figure 6d,f), optical memory can be completely erased by subsequent electrical input, highlighting the reversibility of photoinduced states. These results enabled a multimodal neuromorphic system capable of sensory fusion and temporal learning (Figure 6g). In addition, Uzhansky et al. utilized the bulk photovoltaic effect (BPVE) of $\alpha { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ to realize a self-powered, nonvolatile photovoltaic memory operating without external bias.[26]

# 4.2.2. Polarization-Enhanced Photodetection in MX

Group-III/IV monochalcogenides such as InSe, SnSe, and GeSe combine ferroelectricity with excellent charge transport, making them promising for polarization-tunable photodetection.

A pure InSe photodetector achieved a responsivity of 2300 A $\mathbb { W } ^ { - 1 }$ at 1 V bias and 90 mA $\mathbb { W } ^ { - 1 }$ even at zero bias, with a 56 ms response time and detectivity of $2 . 8 ~ \times ~ 1 0$ Jones.[153] Ferroelectric gating further enhances performance: in a ??-InSe/graphene heterostructure, Li et al. (2023) reported a sixfold detectivity enhancement under negative polarization relative to the unpolarized state.[154] More recently, Wang et al. (2024) introduced sliding-induced ferroelectricity into ??-InSe, achieving a picosecond-scale bulk photovoltaic response in a vertical graphene/??-InSe/graphene heterostructure under near-infrared illumination, further confirming the significant potential of ferroelectric polarization in boosting photodetector performance.[155] Moreover, several studies have explored heterostructures composed of MX materials and conventional ferroelectrics, utilizing ferroelectric polarization to modulate their photoresponse. For instance, Weng et al. reported a $\mathrm { C u C r P } _ { 2 } \mathrm { S } _ { 6 } /$ InSe heterostructure that achieved a responsivity of 1839 A $\cdot \mathbb { W } ^ { - 1 }$ and a detectivity of $1 . 9 \times 1 0 ^ { - 2 }$ Jones at a wavelength of 300 nm, with a responsivity contrast of up to 20.7 times between different polarization states.[156]

# 4.2.3. Polarization-Enhanced Photodetection in $B i _ { 2 } O _ { 2 } S e$

$\mathrm { B i } _ { 2 } \mathrm { O } _ { 2 } \mathrm { S e }$ is another 2D ferroelectric semiconductor with a small indirect bandgap (≈0.8 eV) and high electron mobility, suitable for broadband optoelectronics. However, its narrow gap often causes large dark currents, which can be mitigated via heterojunction or interface engineering. Tao et al. combined $_ { \mathrm { B i _ { 2 } O _ { 2 } S e } }$ with $\mathsf { M o S e } _ { 2 }$ to form a type-II junction that reduced dark current through interlayer charge separation;[157] Huang et al. fabricated a $\mathrm { B i } _ { 2 } \mathrm { O } _ { 2 } \mathrm { S e } / \mathrm { S i }$ photodetector with low dark current $( 2 2 . 3 \mathrm { n A c m } ^ { - 2 } )$ , high on/off ratio $( 8 \times 1 0 ^ { 6 } )$ , and responsivity of $2 3 \mathrm { ~ A ~ } \mathbb { W } ^ { - 1 } ;  { [ 1 5 8 ] }$ and asymmetric electrodes have been shown to further suppress leakage.[159] Additionally, ${ \sf B i } _ { 2 } { \sf O } _ { 2 } { \sf S e } ^ { \prime } { \sf s }$ ferroelectricity can be

![](images/52fca353890d07246f379ba28d932b2550739e63de35585824e6ca868e218059.jpg)  
a

![](images/3a18bd5d455a2e3bccfa883afed9b747919afa1635f4d4216b6284e4743e6919.jpg)

![](images/7f21271a92d5cb300e7762b7c274c4a483f1d8f013570f2b80e297c70b118b38.jpg)  
C

![](images/3700af9b9dd98d33993778fd0a0322546a597220a3c0de3106f825a4f0aa38a3.jpg)  
d

![](images/ecfc26a65e1aba8c6d3555b46312f0a7833a615ee60f1330312a4281622ea7b7.jpg)  
e

![](images/d0a133e743d0288cdb8cf41200741f48f5f301ec021f69c6d3b5ee4a72663855.jpg)  
f   
g

![](images/65e1d492640ca950c8dc9c61758cf678af28856822db9db3bfbe25aabc0a0864.jpg)

![](images/37a047c61b61953587eb0e9b6ed6fe46397402eb09903536de7be661923b7224.jpg)

![](images/46233bd1cfb495d650f2617cac3b7dce97da3a769d0dfdd070f4cf37cf0d58e5.jpg)

![](images/21072e17be46bc63097580d7f32fd8ca1346bf62c1f1f635bed7c2adf2333864.jpg)  
h

![](images/02987d307b8fd55b3f82b7bf0431863f846d6a38a37d46b25305eb1307a1cb95.jpg)

![](images/b9fa2815c15b5b272c623cc56361e05e20e99480a69014a71688c4a5e3329955.jpg)

![](images/43bde918d19cd65ff7978c14fc78fa70622757ac2f59acd77dbc39ca4cd1386c.jpg)

![](images/e69059b39f562afc6dbace587e92b17a5183f762a640529346e8f2d2de29b077.jpg)  
k   
m

![](images/f6841b4216e1aaa543f6502c6ddb363af30ea897efa2094b779c72f277b4f501.jpg)

![](images/c45d832bbd487f52634ad792da9b0ec3c5b2dd2bc165ddc4426ddc7c5c300a1a.jpg)

![](images/22cf5294c61c8d695b14a730522685705989811b8a6e5e36f69e8ce241b08464.jpg)  
Figure 6. Applications of ferroelectric semiconductors in optoelectronics. a) Modulation of the third terminal of the ??-In2Se3 bipolar electric synapse by constant illumination/back-gate voltage. b) Relationship between ferroelectric memristor switching and light intensity. c) Inhibitory PSC induced by electrical pulses (−1 V, 100 ms, 6.7 Hz) decreases under constant illumination $( 0 { - } 1 . 2 9 \ m \ ) \times ( - m ^ { - 2 } )$ due to shorter relaxation time and reduced accumulation. d) Timing interaction between electrical (−2 V, 50 ms) and optical (1.29 mW cm−2, 50 ms) pulses at −0.1 V bias, with $\Delta t = t _ { \mathrm { | i g h t } } - t _ { \mathrm { e | e c t r i c a l } } .$ . e) Relaxation time decreases with increasing light intensity under varying electrical stimuli. f) Weight changes at different intervals between electrical and optical pulses. g) $\alpha { \cdot } | \mathsf { n } _ { 2 } \mathsf { S } { \mathsf { e } } _ { 3 }$ synapse for multimodal signal processing. Reproduced with permission.[42] Copyright 2022, Springer Nature. h) Schematic of the $\dot { \mathsf { B i } } _ { 2 } \mathsf { O } _ { 2 } \mathsf { S e }$ photodetector. i) FeS-PD photoresponse under 405 nm, 1.1184 mW $\mathsf { c m } ^ { - 2 }$ illumination after withdrawal of different gate pulses. j) Band diagrams of FeS-PD in HRS, intermediate states $\begin{array}{c} 1 /  { \vert { \vert { \vert } } , { \vert { \vert { \vert { \vert { \vert { \vert { \vert { \vert } } } } } } } } \end{array} }$ and LRS after gate pulse withdrawal, showing enhanced electron–hole separation under 405 nm light due to remanent polarization. Reproduced with permission $[ \breve { 4 3 } ]$ ] Copyright 2023, John Wiley and Sons. k) Schematic of the experimental setup for measuring the suspended CIPS. l) Structural schematic of CIPS under bending deformation. m) Short-circuit photocurrent mapping collected by graphene electrodes on suspended and substrate-supported regions. n) Single-point I–V curves measured at the white and black markers in (m), corresponding to the suspended region (red) and the substrate-supported region (blue), respectively. Reproduced with permission.[40] Copyright 2024, American Chemical Society.

used to tune device performance. Wang et al.[43] demonstrated polarization-controlled photodetection in $\mathrm { B i } _ { 2 } \mathrm { O } _ { 2 } \mathrm { S e }$ , where ferroelectric switching modulates both photocurrent and dark current. Figure 6h presents a schematic of the photodetector (FeS-PD) based on ${ \tt B i } _ { 2 } { \sf O } _ { 2 } { \sf S e }$ , which can switch between different optical response states using gate pulses. The influence of polarization on the photodetection performance was studied by switching between different optical response states with gate pulses. Figure 6i illustrates the time-dependent optical response at various polarization levels. The photodetector operates by switching ferro-

electric polarization, creating an internal electric field that enhances residual polarization. Applying gate pulses bends the energy bands, altering channel resistance, and adjusting both photocurrent and dark current. Positive gate pulses set the channel to HRS, while negative pulses decrease resistance, increasing photocurrent and dark current. Figure 6e shows the band diagram of the FeS-PD under residual polarization. Gate pulse adjustment allows precise control of photonic responses by switching between bistable resistance states (HRS, State I, State II, LRS). This photodetector offers highly tunable performance, a simpli-

fied structure, and potential for integrating high-performance optoelectronic devices.

# 4.2.4. Bulk Photovoltaic Effect and Flexoelectric Enhancement

The BPVE—the generation of a steady photocurrent in a non-centrosymmetric crystal without external bias—is a hallmark of ferroelectrics, originating from shift current and asymmetrical excitation processes. Initially observed in ferroelectric oxides, BPVE has since been extensively explored in emerging materials such as Weyl semimetals.[160] vdW nanomaterials,[122] oxide superlattices,[161] halide perovskites,[162] organic compounds,[163] and bulk Rashba semiconductors.[164] In 2D FeSCs, BPVE has been experimentally confirmed and can be amplified through strain or flexoelectric coupling. CIPS serves as a representative case. Li et al.[25] used CIPS as a photoferroelectric layer sandwiched by graphene electrodes, observing a two-orders-of-magnitude photocurrent enhancement compared with bulk ferroelectrics. Building on this, Yu et al. enhanced the BPVE in CIPS via the flexoelectric effect and demonstrated its mechanical tunability.[40] By transferring CIPS onto a perforated substrate and applying local strain using a PFM tip (Figure 6k), they broke the crystal symmetry (Figure 6l), driving $\mathrm { C u ^ { + } }$ ions toward polarized lattice sites and inducing uniform polarization. The short-circuit current mapping under 405 nm laser illumination (Figure 6m) showed a peak current of 1.43 nA at the suspended region (Point 1), while the supported region (Point 2) exhibited only – 65.9 pA (Figure 6n), confirming that flexoelectric strain effectively boosts the BPVE in CIPS. Similarly, Dong et al.[122] reported strain-enhanced photocurrents in non-centrosymmetric ${ \mathrm { M o S } } _ { 2 } ,$ and Wang et al.[165] demonstrated polarization-switchable BPVE in $\alpha { \cdot } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ . Peng et al. achieved highly sensitive polarizationresolved photodetection in a trilayer hybrid perovskite ferroelectric, (allyammonium) (ethylammonium) $\underline { { \boldsymbol { \mathrm { P } } } } \mathsf { b } _ { 3 } \mathsf { B r } _ { 1 0 }$ , exhibiting a near-bandgap open-circuit voltage of ${ \approx } 2 . 5 ~ \mathrm { V } ,$ an on/off ratio of 104, and a polarization ratio up to $1 5 . ^ { [ 1 6 6 ] }$

# 4.3. Spintronics and Valleytronics

The spin and valley degrees of freedom introduce new dimensions for tuning device performance. In 2D materials, where reduced symmetry and strong spin–orbit coupling (SOC) prevail, these internal degrees of freedom can be sensitively tuned by structural or electrical perturbations. Ferroelectric semiconductors, with their switchable spontaneous polarization and intrinsic coupling among charge, lattice, orbital, and spin, naturally provide a powerful platform for manipulating spin and valley states via electric fields. Such coupling not only enables efficient spin and valley control without magnetic fields but also promotes the integration of multiple information modalities— charge, spin, and valley—within a single architecture.

# 4.3.1. Ferroelectric Control of Spin and Magnetism

In spintronics, ferroelectric polarization–induced Rashba spin splitting introduces spin-dependent band dispersion, enabling

electrical control over spin degrees of freedom. This is crucial for devices like spin field-effect transistors. Compared with conventional spintronic devices relying on magnetic field manipulation, electric control offers low power consumption and better integration. Moreover, the coupling between ferroelectricity and SOC allows reversible spin polarization switching, supporting non-volatile spin storage and logic. Some 2D van der Waals ferroelectrics exhibit large Rashba effects, with Rashba parameters surpassing those from conventional surface or interface effects. For example, Bruyer et al.[167] found that trilayer ${ \mathrm { M o S } } _ { 2 } ,$ , with d2 metal ions, retains switchable Rashba spin textures even at the monolayer limit.

Building on this concept, ferroelectric Rashba semiconductors have emerged as a key materials class that combines semiconducting transport, strong SOC, and ferroelectric nonvolatility. In Fe/GeTe heterostructures, Varotto et al.[45] reported that spin-to-charge conversion efficiency can be reversibly tuned by flipping ferroelectric polarization, thereby demonstrating nonvolatile spin manipulation purely through electric means. These findings highlight a unifying principle across diverse systems: the electrostatic field associated with ferroelectric polarization directly modifies the local potential gradient and, consequently, the spin texture and spin current response—an effect central to scalable spintronic logic and memory design.

# 4.3.2. Multiferroic Coupling and 2D Magnetic–Ferroelectric Integration

Beyond Rashba-type effects, intrinsic 2D multiferroics offer direct coupling between electric and magnetic order parameters, enabling cross-control of magnetism and ferroelectricity. Although achieving room-temperature stability remains challenging, recent experimental breakthroughs have verified genuine 2D multiferroicity. Wu et al.[168] identified the coexistence of ferroelectricity and antiferromagnetism in layered ${ \mathrm { N i I } } _ { 2 } ,$ establishing it as a single-phase van der Waals multiferroic through optical, electrical, and magnetic characterizations. In their study, trilayer $\mathrm { N i I } _ { 2 }$ devices encapsulated with graphene and hBN ( a) Figure 7showed a rhombohedral stacking structure with triangular Ni–I lattices (Figure 7b). ADF-STEM imaging confirmed the stacking order and an interlayer spacing of ≈1.9 Å (Figure 7c), while circularly polarized Raman spectra identified the $\mathsf { A } _ { 1 } \mathsf { g }$ and interlayer shear modes characteristic of trilayer geometry (Figure 7d). Magnetic circular dichroism (MCD) and reflective MCD spectra revealed field-dependent magnetic signals and bimeron-like topological domains (Figure 7e), and frequency-dependent P–E and I–E loops confirmed the coexistence of ferroelectric and antiferromagnetic order. The magnetoelectric coefficient reached ≈7% under 7 T at 24.5 Hz (Figure 7f), signifying a prototypical type-II multiferroic coupling. The systematic modulation of ferroelectric switching by external magnetic fields provides compelling evidence of the dynamic interplay between spin and polarization in van der Waals materials.

A complementary strategy to engineer spin–electric coupling is the assembly of ferroelectric/ferromagnetic van der Waals heterostructures, where interfacial polarization fields mediate magnetism across atomic layers. Yang et al.[23] realized such a system by integrating bilayer $\mathrm { C r I } _ { 3 }$ with monolayer $\mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ (Figure 7h).

![](images/33f62e4823475035c656fe59169da6bbe9d04b9b60260a1dfa894f42246b1202.jpg)  
a

![](images/524a51fcf4a3b2d78eb524c24565e52367f90a75b086a509a689fd9c11f365d9.jpg)  
b

![](images/c6f720632043316b8421e69508c53b7bc6c28a159715ea7794df5aec2424be32.jpg)

![](images/d9b1adb60470fbe62b0dde4b618bf72007813829df3f9c5134ad443248f0f062.jpg)  
e

![](images/12167fdc44c4d8148f5a9c76c38b1c974220c5607f3b5660f05ef49b46596153.jpg)

![](images/3f59d8522d6dde98cedefa6abe4172d918e6609a8a823300abc1153c28590835.jpg)

![](images/58bf340a156209b4316b4b12b076e48bf70973856ec7e00c0bb463916884b10a.jpg)  
C

![](images/0213ee2a60b5833337af2ec1cde04e2473b2e492b9c84dc7daa5abf04548683e.jpg)  
d

![](images/6c7966a7847e516fc75db29186e437c9bd5e81199af44745a399e0df80759e8c.jpg)  
f

![](images/7c904f677931408b4bfe79e394523a09d358f83bd8bfaa277e49d66c162236a9.jpg)  
g

![](images/e8b5b49d0a291b09a98ca42728a032ce1063895ed0ba3a531870b9d41cfd9373.jpg)  
h

![](images/73232638e71d85810cf3406dc6d94b71647ffdfcb1f0230ef91227c3d3b1f0ab.jpg)

![](images/f1f68041ddd844582987b2ad2a7551f2001b5db1dc76aa3566f1d578dfbc140a.jpg)  
k

![](images/02f07ff9a88b80e2dc651bd3040d737d18ff2b00ccb08e9b78d0bba6a822f6f5.jpg)

![](images/22eb4198f039782b793008768ac93bdcdfb63214e095c7d2746d168e8803b4bb.jpg)

![](images/2687b71faad72b55c74da7954c0375abc871ac28aef7eeeb672347c353c73082.jpg)  
m

![](images/2d60984aa8087e033d66693b1ed1cc5a81c8792e2254db2db3fb1bedc73b5e4a.jpg)  
n

![](images/4908c3b7e78302a9c9382e3f7174ff6c41e7c664e8a37991b8f7087604bdfb20.jpg)  
0   
Figure 7. a) Schematic of trilayer ${ \sf N i l } _ { 2 }$ sandwiched between graphene and hBN, showing both IP and OOP atomic lattice structures. $\mathsf { N i } ^ { 2 + }$ ions are coordinated by I− octahedra, and the trilayer $\mathsf { N i l } _ { 2 }$ stacks in a staggered fashion along the c-axis. b) Atomic-resolution ADF-STEM image displaying the hexagonal pattern characteristic of rhombohedral stacking in few-layer NiI crystals; inset shows the corresponding FFT image. c) Circular polarizationresolved Raman spectra of the NiI2 device under 532 nm laser excitation, highlighting the interlayer shear mode (SM). d) MCD spectra of trilayer NiI2 measured under magnetic fields of +3 T, 0 T, and −3 T. e) Remanent polarization $( P _ { r } )$ as a function of OOP magnetic field at different frequencies. f) Phase diagram of the magnetic control ratio, $( P _ { \mathrm { r } } - P _ { \mathrm { r 0 } } ) / \bar { P } _ { \mathrm { r 0 } }$ , as a function of frequency and magnetic field, where $P _ { \mathrm { { r } } }$ and $P _ { \mathrm { r 0 } }$ represent the remanent r  r0 r0 r r0 polarization with and without a magnetic field, respectively. g) I–E curves measured under different magnetic fields.[168] Copyright 2024, The Authors, published by Springer Nature. h) Side view of ${ \mathsf { b i - C r l } } _ { 3 } / { \mathsf { I n } } _ { 2 } \mathsf { S e } _ { 3 } . \mathsf { i } )$ Switching path between the FM-P↑ and $\mathsf { A F M } . \mathsf { P } \downarrow$ states in the high-temperature phase of $\mathsf { \dot { b i } } { - } \mathsf C r | _ { 3 } / | \mathsf n _ { 2 } \mathsf { S e } _ { 3 }$ . Blue and green circles represent different magnetic states in the P↑ and P↓ configurations, respectively. When $\begin{array} { r } { \bar { P } = 0 , } \end{array}$ , the system is nonferroelectric. j,m) Schematic diagrams of orbital coupling between the interfacial I-1 and Se-1 p orbitals, and the virtual hopping path between the empty Cr-1 $e _ { \mathrm { g } }$ and occupied Cr-2 $t _ { 2 \mathrm { g } }$ orbitals. $^ { \mathsf { k } , \mathsf { n } ) }$ Orbital-projected band structures (spin-up channel). l,o) Projected density of states (PDOS). Reproduced with permission.[23] Copyright 2024, American Physical Society.

In this heterostructure, the polarization direction of $\mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ controls the interlayer magnetic alignment of ${ \mathrm { C r l } } _ { 3 } { \mathrm { : } }$ the upward polarization (P↑) and downward polarization (P↓) states correspond to ferromagnetic and antiferromagnetic configurations, respectively, separated by an energy barrier of 459 meV per Cr atom (Figure 7i). Unlike charge-transfer-based modulation, the interfacial coupling here is electrostatic and orbital in nature, preserving the semiconducting characteristics. PDOS analysis (Figure 7j,k)

shows that the P↑ induces a potential difference (ΔV) that stabilizes the ferromagnetic state (Figure 7l), whereas the P↓ enhances orbital hybridization (Figure 7m–o), reducing ΔV and favoring antiferromagnetism. This bidirectional electrical control of magnetism exemplifies a key physical insight across various systems: ferroelectric polarization acts as an internal gate that reshapes the magnetic exchange interactions through spin-dependent orbital overlap, offering a unified route to electrically tunable spin order.

![](images/3922e87eebd9fd7b5e630f5a812b2f08c1f1b4542af21d9232e7fc89b24943ce.jpg)  
Figure 8. Challenges of 2D ferroelectric semiconductors.

# 4.3.3. Ferroelectric Modulation of Valley Degrees of Freedom

In valleytronics, ferroelectric polarization breaks the degeneracy between K and K′ valleys, leading to valley polarization and enabling electrical and optical control over the valley degree of freedom. Moreover, polarization-induced Berry curvature reconstruction can give rise to the valley Hall effect, generating transverse valley currents in the absence of an external magnetic field— a promising mechanism for low-power information processing. Initial studies focused on 2D hexagonal lattice systems.[169] As research has progressed, intrinsic coupling between ferroelectric polarization and spontaneous valley polarization has been observed in group-IV monochalcogenides, such as SnS and GeSe. For instance, GeSe[170] exhibits two vertical polarization orientations, each corresponding to opposite valley polarization states. Owing to the synergy between ferroelectricity and valley polarity, the direction of valley polarization can be reversed through ferroelectric switching.

Beyond intrinsic coupling, heterostructure engineering, interlayer sliding, and ionic doping offer additional degrees of control. For example, in the MnPS /CIPS heterostructure,[171] ferroelectric polarization induced by proximity effects modulates the direction of valley polarization and the optical bandgap, enabling multidimensional tuning of electronic degrees of freedom.

# 5. Challenges and Future Perspectives

The continued advancement of 2D ferroelectric semiconductors for next-generation nanoelectronic and optoelectronic technolo-

gies hinges on overcoming several critical challenges, which span from fundamental scientific questions to practical engineering issues, as illustrated in  .

# 5.1. Challenges

# 5.1.1. Exploring Quantum Ferroelectric Phenomena at the Ultrathin Limit

When scaled to monolayer or few-layer thicknesses, 2D ferroelectric semiconductors may exhibit quantum phenomena that fundamentally alter their polarization behavior. Quantum fluctuations, tunneling-assisted polarization reversal, and proximity to quantum critical points could give rise to entirely new physics beyond classical ferroelectricity. Unraveling these effects and understanding their implications for applications in spintronics, quantum information devices, and correlated electron systems represent exciting frontiers for basic research.

# 5.1.2. Discovery and Rapid Screening of New Materials

The library of experimentally realized 2D ferroelectric semiconductors remains relatively narrow, largely limited to a few families such as IV–VI group compounds, Janus structures, and layered oxides like ${ \mathrm { B i } } _ { 2 } { \mathrm { O } } _ { 2 } { \mathrm { S e } }$ . Expanding this material space is crucial for diversifying functional properties and enabling new applications. High-throughput computational screening, accelerated

by machine learning and data-driven approaches, holds great promise for discovering novel 2D materials that combine robust polarization, wide-range bandgap tunability, and intrinsic stability under operational conditions.

# 5.1.3. Compatibility with Mainstream Semiconductor Technologies

For 2D ferroelectric semiconductors to make a meaningful impact in practical devices, their integration with existing CMOS technologies must be addressed. This involves not only the scalable growth of large-area, high-quality films with uniform properties and minimal defect density, but also the realization of lowresistance, stable interfaces with metal contacts and insulating layers. Furthermore, the ability to transfer or directly synthesize these materials on technologically relevant substrates, while preserving their ferroelectric and semiconducting functionalities, is essential for seamless incorporation into current fabrication processes.

# 5.1.4. Stability of Polarization over Time and with Scaling

As device dimensions are pushed into the sub-10 nm regime, the ferroelectric polarization in 2D semiconductors becomes increasingly vulnerable to thermal fluctuations, depolarization fields, and the presence of defects. These factors can lead to significant degradation of remanent polarization and switching reliability over time. Ensuring robust, switchable polarization at room temperature in the ultrathin limit, while maintaining long-term retention and fatigue endurance, remains a central challenge. This calls for innovative strategies in material design, defect passivation, and interface engineering to suppress depolarization and stabilize ferroelectric order at atomic thicknesses.

# 5.1.5. Balancing Ferroelectricity and Semiconducting Performance

Achieving a harmonious integration of strong ferroelectric properties with desirable semiconducting characteristics—such as appropriate band gaps, high carrier mobility, and low trap density— is inherently challenging. Strong spontaneous polarization often induces significant lattice distortions, which in turn can reduce carrier mobility and degrade charge transport. The development of 2D ferroelectric semiconductors thus requires careful tuning of composition, strain, and heterostructure configurations to reconcile these competing requirements. Alloy engineering, van der Waals stacking, and external-field control represent promising approaches to achieve this delicate balance.

# 5.1.6. Potential in Next-Generation Flexible and Wearable Electronics

The atomic thinness and mechanical flexibility of 2D ferroelectric semiconductors position them as promising candidates for flexible, wearable, and implantable electronic systems. However, maintaining stable ferroelectric polarization and reliable device operation under repeated bending, stretching, and other mechanical deformations remains a significant challenge. Progress

in scalable synthesis techniques, as well as the development of robust device architectures capable of withstanding mechanical stress, will be key to realizing their full potential in these emerging applications.

# 5.2. Future Directions

Looking ahead, several emerging research avenues are expected to further expand the scientific and technological potential of 2D ferroelectric semiconductors:

# 5.2.1. Strain Engineering for Polarization and Phase Control

The extreme mechanical flexibility of 2D materials provides a unique platform for strain engineering, enabling the precise modulation of polarization orientation, magnitude, and switching barrier. Dynamically tunable strain fields—achieved via substrate coupling, local gating, or piezoelectric actuators—may allow reversible control of ferroelectric domains, phase boundaries, and even emergent ferroelastic states, offering a pathway toward adaptive and reconfigurable devices.

# 5.2.2. Twist-Angle and Moiré Engineering

Twist-angle control in van der Waals bilayers offers another promising route to realize exotic ferroelectric phenomena, such as moiré-induced polarization, fractional domain-wall charges, and electrically switchable dipole textures. Systematic exploration of moiré ferroelectricity, including the interplay between twist angle, stacking configuration, and interlayer coupling, will be crucial for developing next-generation twistronic ferroelectric devices with programmable polarization landscapes.

# 5.2.3. Integration with Quantum and Correlated Materials

Coupling 2D ferroelectric semiconductors with quantum materials—such as topological insulators, superconductors, and magnetic van der Waals layers—could lead to novel quantum functionalities arising from ferroelectric control of topological phases, spin textures, or superconducting pairing. Such hybrid architectures are expected to open exciting opportunities in nonvolatile quantum logic, topological memory, and low-dissipation information processing.

# 5.2.4. Artificial Heterostructures and Neuromorphic Architectures

Designing artificial van der Waals heterostructures that combine ferroelectric, semiconducting, and magnetic components may enable multifunctional devices capable of performing sensing, memory, and computation simultaneously. Beyond conventional transistors, integrating 2D ferroelectric semiconductors into neuromorphic architectures could leverage their analog switching and nonvolatile polarization states for brain-inspired computing.

# 5.2.5. Toward Sustainable and Scalable Integration

Finally, developing environmentally friendly synthesis routes, wafer-scale integration strategies, and defect-tolerant architectures will be essential for bridging the gap between laboratory demonstrations and real-world applications. Future efforts should focus on the co-optimization of material quality, interface design, and device performance to establish 2D ferroelectric semiconductors as key enablers in next-generation low-power and multifunctional nanoelectronics.

# 6. Conclusion

2D ferroelectric semiconductors have emerged as a frontier in ferroelectric materials research, offering a compelling combination of atomic-scale thickness, spontaneous polarization, excellent semiconducting properties, and tunable band gaps. These unique features are driving a new wave of innovation in microand nanoelectronics as well as optoelectronics. This review has provided a systematic overview of the evolution of ferroelectricity, with a focus on the origin of intrinsic ferroelectricity in 2D materials, their distinctive properties compared with conventional 3D ferroelectrics, and recent advances in both intrinsic and extrinsically engineered 2D ferroelectric semiconductors.

In terms of device applications, 2D ferroelectric semiconductors exhibit significant potential in a broad range of technologies, including FeFETs, ferroelectric tunnel junctions, neuromorphic computing devices, piezotronic systems, ferroelectric photodetectors, bulk photovoltaic effect devices, piezophototronic structures, as well as spintronic and valleytronic applications. These emerging applications offer promising pathways toward the development of next-generation high-density, low-power, nonvolatile memory and logic devices, while also providing a new material foundation for flexible electronics, wearable technologies, and hardware for neural network computing.

Despite the remarkable progress, the development of 2D ferroelectric semiconductors continues to face critical challenges. Key issues include ensuring polarization stability at reduced dimensions and over extended operating lifetimes, achieving integration compatibility with existing silicon-based semiconductor processes, balancing strong ferroelectric properties with high carrier mobility and tunable electronic structures, and accelerating the discovery of new materials through high-throughput screening and machine learning approaches. Future research must not only advance material design, modulation, and scalable fabrication techniques, but also explore quantum ferroelectric phenomena at the ultimate thickness limit and their potential in flexible and wearable electronic systems.

In summary, as a new class of materials combining intrinsic ferroelectricity with outstanding semiconducting performance, 2D ferroelectric semiconductors are steadily advancing the frontiers of nanoelectronics, optoelectronics, and spintronics. Their application in next-generation information technologies warrants continued and intensive investigation.

# Acknowledgements

This work was supported by the National Natural Science Foundation of China (Grant nos. 52303307 and 52192611), Beijing Natural

Science Foundation (Z230024), China Postdoctoral Science Foundation (2023M743438), Postdoctoral Fellowship Program of China Postdoctoral Science Foundation (GZB20230730).

# Conflict of Interest

The authors declare no conflict of interest.

# Author Contributions

Conceptualization was done by M.C. and J.Z. Original Draft was written by M.C. M.C. and D.G. prepared the figures. M.C., X.Z., J.L., Y.W., and A.Y. were responsible for analysis and synthesis. Funding Acquisition was done by J.Z. and D.G. Supervision was done by J.Z. and D.G. All authors revised and approved the final version of the manuscript.

# Keywords

2D materials, electronics, ferroelectric semiconductors, optoelectronics, polarization mechanisms

Received: July 26, 2025

Revised: October 14, 2025

Published online: November 3, 2025

[1] J. Valasek, Phys. Rev. 1921, 17, 475.   
[2] G. Busch, P. Scherrer, Naturwissenschaften 1935, 23, 737.   
[3] S. Miyake, R. Ueda, J. Phys. Soc. Jpn. 1946, 1, 32.   
[4] R. R. Mehta, B. D. Silverman, J. T. Jacobs, J. Appl. Phys. 1973, 44, 3379.   
[5] M. D. Glinchuk, E. A. Eliseev, V. A. Stephanovich, Phys. B 2002, 322, 356.   
[6] P. Wurfel, I. P. Batra, Phys. Rev. B 1973, 8, 5126.   
[7] M. Dawber, P. Chandra, P. B. Littlewood, J. F. Scott, J. Phys.: Condens. Matter 2003, 15, L393.   
[8] G. S. Pawley, W. Cochran, R. A. Cowley, G. Dolling, Phys. Rev. Lett. 1966, 17, 753.   
[9] R. Brec, in Intercalation in Layered Materials, 1st ed., Vol. 148 (Ed: M. S. Dresselhaus), Springer, New York, NY, USA, 1986, 93.   
[10] M. Wu, X. C. Zeng, Nano Lett. 2016, 16, 3236.   
[11] R. Fei, W. Kang, L. Yang, Phys. Rev. Lett. 2016, 117, 097601.   
[12] W. Ding, J. Zhu, Z. Wang, Y. Gao, D. Xiao, Y. Gu, Z. Zhang, W. Zhu, Nat. Commun. 2017, 8, 14956.   
[13] F. Liu, L. You, K. L. Seyler, X. Li, P. Yu, J. Lin, X. Wang, J. Zhou, H. Wang, H. He, S. T. Pantelides, W. Zhou, P. Sharma, X. Xu, P. M. Ajayan, J. Wang, Z. Liu, Nat. Commun. 2016, 7, 12357.   
[14] Q. Song, C. A. Occhialini, E. Ergeçen, B. Ilyas, D. Amoroso, P. Barone, J. Kapeghian, K. Watanabe, T. Taniguchi, A. S. Botana, S. Picozzi, N. Gedik, R. Comin, Nature 2022, 602, 601.   
[15] Y. Zhou, D. Wu, Y. Zhu, Y. Cho, Q. He, X. Yang, K. Herrera, Z. Chu, Y. Han, M. C. Downer, H. Peng, K. Lai, Nano Lett. 2017, 17, 5508.   
[16] W. F. Io, S. Y. Pang, L. W. Wong, Y. Zhao, R. Ding, J. Mao, Y. Zhao, F. Guo, S. Yuan, J. Zhao, J. Yi, J. Hao, Nat. Commun. 2023, 14, 7304.   
[17] N. Higashitarumizu, H. Kawamoto, C.-J. Lee, B.-H. Lin, F.-H. Chu, I. Yonemori, T. Nishimura, K. Wakabayashi, W.-H. Chang, K. Nagashio, Nat. Commun. 2020, 11, 2428.   
[18] K. Chang, J. Liu, H. Lin, N. Wang, K. Zhao, A. Zhang, F. Jin, Y. Zhong, X. Hu, W. Duan, Q. Zhang, L. Fu, Q.-K. Xue, X. Chen, S.-H. Ji, Science 2016, 353, 274.   
[19] D. Kriegner, G. Springholz, C. Richter, N. Pilet, E. Müller, M. Capron, H. Berger, V. Holý, J. H. Dil, J. Krempaský, Crystals 2019, 9, 335.

[20] S. Yuan, X. Luo, H. L. Chan, C. Xiao, Y. Dai, M. Xie, J. Hao, Nat. Commun. 2019, 10, 1775.   
[21] T. Ghosh, M. Samanta, A. Vasdev, K. Dolui, J. Ghatak, T. Das, G. Sheet, K. Biswas, Nano Lett. 2019, 19, 5703.   
[22] I. Abdelwahab, B. Tilmann, Y. Wu, D. Giovanni, I. Verzhbitskiy, M. Zhu, R. Berté, F. Xuan, L. d. S. Menezes, G. Eda, T. C. Sum, S. Y. Quek, S. A. Maier, K. P. Loh, Nat. Photonics 2022, 16, 644.   
[23] B. Yang, B. Shao, J. Wang, Y. Li, C. Yam, S. Zhang, B. Huang, Phys. Rev. B 2021, 103, L201405.   
[24] S. Wang, L. Liu, L. Gan, H. Chen, X. Hou, Y. Ding, S. Ma, D. W. Zhang, P. Zhou, Nat. Commun. 2021, 12, 53.   
[25] Y. Li, J. Fu, X. Mao, C. Chen, H. Liu, M. Gong, H. Zeng, Nat. Commun. 2021, 12, 5896.   
[26] M. Uzhansky, A. Rakshit, Y. Kalcheim, E. Koren, npj 2D Mater. Appl. 2025, 9, 6.   
[27] M. Si, A. K. Saha, S. Gao, G. Qiu, J. Qin, Y. Duan, J. Jian, C. Niu, H. Wang, W. Wu, S. K. Gupta, P. D. Ye, Nat. Electron. 2019, 2, 580.   
[28] J. Wu, H.-Y. Chen, N. Yang, J. Cao, X. Yan, F. Liu, Q. Sun, X. Ling, J. Guo, H. Wang, Nat. Electron. 2020, 3, 466.   
[29] X. Wang, C. Zhu, Y. Deng, R. Duan, J. Chen, Q. Zeng, J. Zhou, Q. Fu, L. You, S. Liu, J. H. Edgar, P. Yu, Z. Liu, Nat. Commun. 2021, 12, 1109.   
[30] S. Deb, W. Cao, N. Raab, K. Watanabe, T. Taniguchi, M. Goldstein, L. Kronik, M. Urbakh, O. Hod, M. B. Shalom, Nature 2022, 612, 465.   
[31] S. Kamaei, X. Liu, A. Saeidi, Y. Wei, C. Gastaldi, J. Brugger, A. M. Ionescu, Nat. Electron. 2023, 6, 658.   
[32] T. H. Yang, B.-W. Liang, H.-C. Hu, F.-X. Chen, S.-Z. Ho, W.-H. Chang, L. Yang, H.-C. Lo, T.-H. Kuo, J.-H. Chen, P.-Y. Lin, K. B. Simbulan, Z.- F. Luo, A. C. Chang, Y.-H. Kuo, Y.-S. Ku, Y.-C. Chen, Y.-J. Huang, Y.-C. Chang, Y.-F. Chiang, T.-H. Lu, M.-H. Lee, K.-S. Li, M. Wu, Y.-C. Chen, C.-L. Lin, Y.-W. Lan, Nat. Electron. 2024, 7, 29.   
[33] Y. Gong, R. Duan, Y. Hu, Y. Wu, S. Zhu, X. Wang, Q. Wang, S. P. Lau, Z. Liu, B. K. Tay, Nat. Commun. 2025, 16, 230.   
[34] M. Wang, D. Ouyang, Y. Dai, D. Huo, W. He, B. Song, W. Hu, M. Wu, Y. Li, T. Zhai, Adv. Mater. 2025, 37, 2500049.   
[35] L. Rogée, L. Wang, Y. Zhang, S. Cai, P. Wang, M. Chhowalla, W. Ji, S. P. Lau, Science 2022, 376, 973.   
[36] T. Handa, C.-Y. Huang, Y. Li, N. Olsen, D. G. Chica, D. D. Xu, F. Sturm, J. W. McIver, X. Roy, X. Zhu, Nat. Mater. 2025, 24, 1203.   
[37] R. Chen, F. Meng, H. Zhang, Y. Liu, S. Yan, X. Xu, L. Zhu, J. Chen, T. Zhou, J. Zhou, F. Yang, P. Ci, X. Huang, X. Chen, T. Zhang, Y. Cai, K. Dong, Y. Liu, K. Watanabe, T. Taniguchi, C.-C. Lin, A. V. Penumatcha, I. Young, E. Chan, J. Wu, L. Yang, R. Ramesh, J. Yao, Nat. Commun. 2025, 16, 3648.   
[38] Z. Gui, W. Li, L. Huang, Nano Lett. 2024, 24, 3231.   
[39] K. Kobayashi, S. Horiuchi, R. Kumai, F. Kagawa, Y. Murakami, Y. Tokura, Phys. Rev. Lett. 2012, 108, 237601.   
[40] J. Yu, B. Huang, S. Yang, Y. Zhang, Y. Bai, C. Song, W. Ming, W. Liu, J. Wang, C. Li, Q. Wang, J. Li, Nano Lett. 2024, 24, 6337.   
[41] J.-H. Lee, J. Y. Park, E. B. Cho, T. Y. Kim, S. A. Han, T.-H. Kim, Y. Liu, S. K. Kim, C. J. Roh, H.-J. Yoon, H. Ryu, W. Seung, J. S. Lee, J. Lee, S.-W. Kim, Adv. Mater. 2017, 29, 1606667.   
[42] K. Liu, T. Zhang, B. Dang, L. Bao, L. Xu, C. Cheng, Z. Yang, R. Huang, Y. Yang, Nat. Electron. 2022, 5, 761.   
[43] W. Wang, Y. Meng, Y. Zhang, Z. Zhang, W. Wang, Z. Lai, P. Xie, D. Li, D. Chen, Q. Quan, D. Yin, C. Liu, Z. Yang, S. Yip, J. C. Ho, Adv. Mater. 2023, 35, 2210854.   
[44] W. Yan, H.-R. Fuh, Y. Lv, K.-Q. Chen, T.-Y. Tsai, Y.-R. Wu, T.-H. Shieh, K.-M. Hung, J. Li, D. Zhang, C. Ó Coileáin, S. K. Arora, Z. Wang, Z. Jiang, C.-R. Chang, H.-C. Wu, Nat. Commun. 2021, 12, 2018.   
[45] S. Varotto, L. Nessi, S. Cecchi, J. Sławinska, P. Noël, S. Petrò, F. ´ Fagiani, A. Novati, M. Cantoni, D. Petti, E. Albisetti, M. Costa, R. Calarco, M. Buongiorno Nardelli, M. Bibes, S. Picozzi, J.-P. Attané, L. Vila, R. Bertacco, C. Rinaldi, Nat. Electron. 2021, 4, 740.

[46] S. Fang, M. Wang, X. Yang, Z. Yang, Q. Li, Z. Luo, J. Lu, Phys. Rev. B 2024, 109, 195202.   
[47] X. Chen, X. Ding, G. Gou, X. C. Zeng, Nano Lett. 2024, 24, 3089.   
[48] W. Cochran, Phys. Rev. Lett. 1959, 3, 412.   
[49] A. A. Sirenko, C. Bernhard, A. Golnik, A. M. Clark, J. Hao, W. Si, X. X. Xi, Nature 2000, 404, 373.   
[50] B. Xu, H. Xiang, Y. Xia, K. Jiang, X. Wan, J. He, J. Yin, Z. Liu, Nanoscale 2017, 9, 8427.   
[51] K. Liu, J. Lu, S. Picozzi, L. Bellaiche, H. Xiang, Phys. Rev. Lett. 2018, 121, 027601.   
[52] J. Lu, G. Chen, W. Luo, J. Íñiguez, L. Bellaiche, H. Xiang, Phys. Rev. Lett. 2019, 122, 227601.   
[53] J. Xiao, H. Zhu, Y. Wang, W. Feng, Y. Hu, A. Dasgupta, Y. Han, Y. Wang, D. A. Muller, L. W. Martin, P. Hu, X. Zhang, Phys. Rev. Lett. 2018, 120, 227601.   
[54] X. Sun, Q. Xia, T. Cao, S. Yuan, Mater. Sci. Eng.: R: Rep. 2025, 163, 100927.   
[55] W. Wan, C. Liu, W. Xiao, Y. Yao, Appl. Phys. Lett. 2017, 111, 132904.   
[56] Z. Fei, W. Zhao, T. A. Palomaki, B. Sun, M. K. Miller, Z. Zhao, J. Yan, X. Xu, D. H. Cobden, Nature 2018, 560, 336.   
[57] P. Sharma, F.-X. Xiang, D.-F. Shao, D. Zhang, E. Y. Tsymbal, A. R. Hamilton, J. Seidel, Sci. Adv. 2019, 5, aax5080.   
[58] K. Yasuda, X. Wang, K. Watanabe, T. Taniguchi, P. Jarillo-Herrero, Science 2021, 372, 1458.   
[59] H. Hu, Y. Sun, M. Chai, D. Xie, J. Ma, H. Zhu, Appl. Phys. Lett. 2019, 114, 252903.   
[60] X. Wang, K. Yasuda, Y. Zhang, S. Liu, K. Watanabe, T. Taniguchi, J. Hone, L. Fu, P. Jarillo-Herrero, Nat. Nanotechnol. 2022, 17, 367.   
[61] A. Weston, E. G. Castanon, V. Enaldiev, F. Ferreira, S. Bhattacharjee, S. Xu, H. Corte-León, Z. Wu, N. Clark, A. Summerfield, T. Hashimoto, Y. Gao, W. Wang, M. Hamer, H. Read, L. Fumagalli, A. V. Kretinin, S. J. Haigh, O. Kazakova, A. K. Geim, V. I. Fal’ko, R. Gorbachev, Nat. Nanotechnol. 2022, 17, 390.   
[62] D. R. Klein, L.-Q. Xia, D. MacNeill, K. Watanabe, T. Taniguchi, P. Jarillo-Herrero, Nat. Nanotechnol. 2023, 18, 331.   
[63] D. Bennett, Phys. Rev. B 2022, 105, 235445.   
[64] D. Bennett, B. Remez, npj 2D Mater. Appl. 2022, 6, 7.   
[65] S. Zhang, Y. Liu, Z. Sun, X. Chen, B. Li, S. L. Moore, S. Liu, Z. Wang, S. E. Rossi, R. Jing, J. Fonseca, B. Yang, Y. Shao, C.-Y. Huang, T. Handa, L. Xiong, M. Fu, T.-C. Pan, D. Halbertal, X. Xu, W. Zheng, P. J. Schuck, A. N. Pasupathy, C. R. Dean, X. Zhu, D. H. Cobden, X. Xu, M. Liu, M. M. Fogler, J. C. Hone, et al., Nat. Commun. 2023, 14, 6200.   
[66] D. S. Kim, C. Xiao, R. C. Dominguez, Z. Liu, H. Abudayyeh, K. Lee, R. Mayorga-Luna, H. Kim, K. Watanabe, T. Taniguchi, C.-K. Shih, Y. Miyahara, W. Yao, X. Li, 2025, 11, adt7789.   
[67] Y. Li, Y. Wei, R. Guo, Y. Wang, H. Zhang, T. Taniguchi, K. Watanabe, Y. Shi, Y. Shi, C. Wang, Z. Fei, Nat. Commun. 2025, 16, 5451.   
[68] N. A. Benedek, C. J. Fennie, Phys. Rev. Lett. 2011, 106, 107204.   
[69] A. Belianinov, Q. He, A. Dziaugys, P. Maksymovych, E. Eliseev, A. Borisevich, A. Morozovska, J. Banys, Y. Vysochanskii, S. V. Kalinin, Nano Lett. 2015, 15, 3808.   
[70] A. A. Soluyanov, D. Gresch, Z. Wang, Q. Wu, M. Troyer, X. Dai, B. A. Bernevig, Nature 2015, 527, 495.   
[71] J. Zhou, A. Chen, Y. Zhang, D. Pu, B. Qiao, J. Hu, H. Li, S. Zhong, R. Zhao, F. Xue, Y. Xu, K. P. Loh, H. Wang, B. Yu, Adv. Mater. 2023, 35, 2302419.   
[72] D. Bai, Y. Nie, J. Shang, J. Liu, M. Liu, Y. Yang, H. Zhan, L. Kou, Y. Gu, Nano Lett. 2023, 23, 10922.   
[73] C. Chen, H. Liu, Q. Lai, X. Mao, J. Fu, Z. Fu, H. Zeng, Nano Lett. 2022, 22, 3275.   
[74] F.-T. Huang, S. J. Lim, S. Singh, J. Kim, L. Zhang, J.-W. Kim, M.-W. Chu, K. M. Rabe, D. Vanderbilt, S.-W. Cheong, Nat. Commun. 2019, 10, 4211.

[75] S.-Y. Xu, Q. Ma, H. Shen, V. Fatemi, S. Wu, T.-R. Chang, G. Chang, A. M. M. Valdivia, C.-K. Chan, Q. D. Gibson, J. Zhou, Z. Liu, K. Watanabe, T. Taniguchi, H. Lin, R. J. Cava, L. Fu, N. Gedik, P. Jarillo-Herrero, Nat. Phys. 2018, 14, 900.   
[76] Y. Zhang, Y. Sun, B. Yan, Phys. Rev. B 2018, 97, 041101.   
[77] S. Zhou, L. You, H. Zhou, Y. Pu, Z. Gui, J. Wang, Front. Phys. 2021, 16, 13301.   
[78] Z. Zhao, K. Xu, H. Ryu, W. Zhu, ACS Appl. Mater. Interfaces 2020, 12, 51820.   
[79] M. Chi, A. Li, X. Zhang, Z. Li, M. Jia, J. Wang, Z. L. Wang, J. Zhai, Nano Energy 2024, 126, 109640.   
[80] Q. Zhang, A. Fan, Y. Wang, F. Wu, L. Li, H. Meng, D. Geng, npj 2D Mater. Appl. 2025, 9, 76.   
[81] K. Yasuda, E. Zalys-Geller, X. Wang, D. Bennett, S. S. Cheema, K. Watanabe, T. Taniguchi, E. Kaxiras, P. Jarillo-Herrero, R. Ashoori, Science 2024, 385, 53.   
[82] H. Jafari, E. Barts, P. Przybysz, K. Tenzin, P. J. Kowalczyk, P. Dabrowski, J. Sławinska,´ Phys. Rev. Mater. 2024, 8, 024005.   
[83] P. Meng, Y. Wu, R. Bian, E. Pan, B. Dong, X. Zhao, J. Chen, L. Wu, Y. Sun, Q. Fu, Q. Liu, D. Shi, Q. Zhang, Y.-W. Zhang, Z. Liu, F. Liu, Nat. Commun. 2022, 13, 7696.   
[84] F. Sui, M. Jin, Y. Zhang, R. Qi, Y.-N. Wu, R. Huang, F. Yue, J. Chu, Nat. Commun. 2023, 14, 36.   
[85] W. Wang, Y. Meng, W. Wang, Y. Zhang, B. Li, Y. Yan, B. Gao, J. C. Ho, Mater. Today Electron. 2023, 6, 100080.   
[86] S. N. Shirodkar, U. V. Waghmare, Phys. Rev. Lett. 2014, 112, 157601.   
[87] J.-J. Zhang, L. Lin, Y. Zhang, M. Wu, B. I. Yakobson, S. Dong, J. Am. Chem. Soc. 2018, 140, 9768.   
[88] W. Ding, J. Lu, X. Tang, L. Kou, L. Liu, ACS Omega 2023, 8, 6164.   
[89] Y. Lu, R. Fei, X. Lu, L. Zhu, L. Wang, L. Yang, ACS Appl. Mater. Interfaces 2020, 12, 6243.   
[90] S. A. Tawfik, J. R. Reimers, C. Stampfl, M. J. Ford, J. Phys. Chem. C 2018, 122, 22675.   
[91] P. Tang, G. E. W. Bauer, Phys. Rev. Lett. 2023, 130, 176801.   
[92] K. Chang, F. Küster, B. J. Miller, J.-R. Ji, J.-L. Zhang, P. Sessi, S. Barraza-Lopez, S. S. P. Parkin, Nano Lett. 2020, 20, 6590.   
[93] J. Chu, Y. Wang, X. Wang, K. Hu, G. Rao, C. Gong, C. Wu, H. Hong, X. Wang, K. Liu, C. Gao, J. Xiong, Adv. Mater. 2021, 33, 2004469.   
[94] M. Chi, Y. Zhao, X. Zhang, M. Jia, A. Yu, Z. L. Wang, J. Zhai, Adv. Funct. Mater. 2023, 33, 2307901.   
[95] W. Li, M. Dai, Y. Hu, H. Chen, X. Zhu, Q. Yang, P. Hu, ACS Appl. Mater. Interfaces 2019, 11, 47098.   
[96] D. Guo, Y. Zhu, X. Xu, J. Zhai, H. N. Alshareef, J. Lou, MRS Bull. 2025, 50, 138.   
[97] J. Junquera, P. Ghosez, Nature 2003, 422, 506.   
[98] D. D. Fong, G. B. Stephenson, S. K. Streiffer, J. A. Eastman, O. Auciello, P. H. Fuoss, C. Thompson, Science 2004, 304, 1650.   
[99] H. Wang, Z. R. Liu, H. Y. Yoong, T. R. Paudel, J. X. Xiao, R. Guo, W. N. Lin, P. Yang, J. Wang, G. M. Chow, T. Venkatesan, E. Y. Tsymbal, H. Tian, J. S. Chen, Nat. Commun. 2018, 9, 3319.   
[100] P. Gao, Z. Zhang, M. Li, R. Ishikawa, B. Feng, H.-J. Liu, Y.-L. Huang, N. Shibata, X. Ma, S. Chen, J. Zhang, K. Liu, E.-G. Wang, D. Yu, L. Liao, Y.-H. Chu, Y. Ikuhara, Nat. Commun. 2017, 8, 15549.   
[101] S. Ghosh, A. M. Chizhik, G. Yang, N. Karedla, I. Gregor, D. Oron, S. Weiss, J. Enderlein, A. I. Chizhik, Nano Lett. 2019, 19, 1695.   
[102] X. Chen, Z. Wang, Z. Zhang, W. Wu, Y. Chai, G. Gou, Z. Yang, X. C. Zeng, Adv. Funct. Mater. 2024, 34, 2410675.   
[103] C. Wang, L. You, D. Cobden, J. Wang, Nat. Mater. 2023, 22, 542.   
[104] A. Dziaugys, K. Kelley, J. A. Brehm, L. Tao, A. Puretzky, T. Feng, A. O’Hara, S. Neumayer, M. Chyasnavichyus, E. A. Eliseev, J. Banys, Y. Vysochanskii, F. Ye, B. C. Chakoumakos, M. A. Susner, M. A. McGuire, S. V. Kalinin, P. Ganesh, N. Balke, S. T. Pantelides, A. N. Morozovska, P. Maksymovych, Nat. Commun. 2020, 11, 3623.

[105] S. Li, F. Wang, Y. Wang, J. Yang, X. Wang, X. Zhan, J. He, Z. Wang, Adv. Mater. 2024, 36, 2301472.   
[106] M. Peng, Y. Zhang, Y. Liu, M. Song, J. Zhai, Z. L. Wang, Adv. Mater. 2014, 26, 6767.   
[107] Y. Liu, J. Guo, A. Yu, Y. Zhang, J. Kou, K. Zhang, R. Wen, Y. Zhang, J. Zhai, Z. L. Wang, Adv. Mater. 2018, 30, 1704524.   
[108] K. Zhang, M. Peng, A. Yu, Y. Fan, J. Zhai, Z. L. Wang, Mater. Horiz. 2019, 6, 826.   
[109] A.-Y. Lu, H. Zhu, J. Xiao, C.-P. Chuu, Y. Han, M.-H. Chiu, C.-C. Cheng, C.-W. Yang, K.-H. Wei, Y. Yang, Y. Wang, D. Sokaras, D. Nordlund, P. Yang, D. A. Muller, M.-Y. Chou, X. Zhang, L.-J. Li, Nat. Nanotechnol. 2017, 12, 744.   
[110] S. Wang, B. Hu, T.-X. Qian, J. Zhou, Y. Ding, T. Cai, S. Ju, ACS Appl. Opt. Mater. 2025, 3, 102.   
[111] M. He, X. Li, X. Liu, L. Li, S. Wei, C. Xia, Phys. E 2022, 142, 115256.   
[112] L. Lin, X. Hu, R. Meng, X. Li, Y. Guo, H. Da, Y. Jiang, D. Wang, Y. Yang, X. Yan, Nanoscale 2024, 16, 4841.   
[113] D. Guo, P. Guo, L. Ren, Y. Yao, W. Wang, M. Jia, Y. Wang, L. Wang, Z. L. Wang, J. Zhai, Sci. Adv. 2023, 9, 3310.   
[114] P. Guo, M. Jia, D. Guo, Z. L. Wang, J. Zhai, Matter 2023, 6, 1.   
[115] C. Wang, Y. Zhang, B. Zhang, B. Wang, J. Zhang, L.-Q. Chen, Q. Zhang, Z. L. Wang, K. Ren, Adv. Sci. 2021, 8, 2004554.   
[116] L. Wang, S. Liu, X. Feng, C. Zhang, L. Zhu, J. Zhai, Y. Qin, Z. L. Wang, Nat. Nanotechnol. 2020, 15, 661.   
[117] P. Guo, M. Jia, D. Guo, T. Ren, Z. L. Wang, J. Zhai, SmartSys 2025, 1, 1.   
[118] D. Guo, P. Guo, Y. Yao, L. Ren, M. Jia, W. Wang, Y. Wang, Y. Zhang, A. Yu, J. Zhai, Nano Energy 2022, 100, 107508.   
[119] P. Guo, M. Jia, D. Guo, W. Wang, Y. Zhang, L. Ren, A. Yu, Z. L. Wang, J. Zhai, Adv. Funct. Mater. 2022, 32, 2202779.   
[120] T. Xu, X. Wang, J. Mai, J. Zhang, J. Wang, T.-Y. Zhang, Adv. Electron. Mater. 2020, 6, 1900932.   
[121] M. Wu, Z. Lou, C.-M. Dai, T. Wang, J. Wang, Z. Zhu, Z. Xu, T. Sun, W. Li, X. Zheng, X. Lin, Adv. Mater. 2023, 35, 2300450.   
[122] Y. Dong, M.-M. Yang, M. Yoshii, S. Matsuoka, S. Kitamura, T. Hasegawa, N. Ogawa, T. Morimoto, T. Ideue, Y. Iwasa, Nat. Nanotechnol. 2023, 18, 36.   
[123] C. Huang, Y. Du, H. Wu, H. Xiang, K. Deng, E. Kan, Phys. Rev. Lett. 2018, 120, 147601.   
[124] M. Vizner Stern, Y. Waschitz, W. Cao, I. Nevo, K. Watanabe, T. Taniguchi, E. Sela, M. Urbakh, O. Hod, M. B. Shalom, Science 2021, 372, 1462.   
[125] Y. Hassan, B. Singh, M. Joe, B.-M. Son, T. D. Ngo, Y. Jang, S. Sett, A. Singha, R. Biswas, M. Bhakar, K. Watanabe, T. Taniguchi, V. Raghunathan, G. Sheet, Z. Lee, W. J. Yoo, P. K. Srivastava, C. Lee, Adv. Mater. 2024, 36, 2406290.   
[126] A. Lipatov, T. Li, N. S. Vorobeva, A. Sinitskii, A. Gruverman, Nano Lett. 2019, 19, 3194.   
[127] L. Wang, X. Wang, Y. Zhang, R. Li, T. Ma, K. Leng, Z. Chen, I. Abdelwahab, K. P. Loh, Adv. Funct. Mater. 2020, 30, 2004609.   
[128] J. Wang, F. Wang, Z. Wang, W. Huang, Y. Yao, Y. Wang, J. Yang, N. Li, L. Yin, R. Cheng, X. Zhan, C. Shan, J. He, Sci. Bull. 2021, 66, 2288.   
[129] M. Gao, W. Wei, T. Han, B. Li, Z. Zeng, L. Luo, C. Zhu, ACS Appl. Mater. Interfaces 2022, 14, 15370.   
[130] W. Huang, F. Wang, L. Yin, R. Cheng, Z. Wang, M. G. Sendeku, J. Wang, N. Li, Y. Yao, J. He, Adv. Mater. 2020, 32, 1908040.   
[131] S. Baek, H. H. Yoo, J. H. Ju, P. Sriboriboon, P. Singh, J. Niu, J.-H. Park, C. Shin, Y. Kim, S. Lee, Adv. Sci. 2022, 9, 2200566.   
[132] M. Si, Z. Zhang, S.-C. Chang, N. Haratipour, D. Zheng, J. Li, U. E. Avci, P. D. Ye, ACS Nano 2021, 15, 5689.   
[133] K. C. Kwon, Y. Zhang, L. Wang, W. Yu, X. Wang, I.-H. Park, H. S. Choi, T. Ma, Z. Zhu, B. Tian, C. Su, K. P. Loh, ACS Nano 2020, 14, 7628.

[134] T. Guo, Z. Pan, Y. Shen, J. Yang, C. Chen, Y. Xiong, X. Chen, Y. Song, N. Huo, R. Xu, G. Zhu, G. Shen, X. Chen, S. Zhang, X. Song, H. Zeng, Nano Lett. 2025, 25, 8258.   
[135] Y. Liu, Y. Wu, B. Wang, H. Chen, D. Yi, K. Liu, C.-W. Nan, J. Ma, Nano Res. 2023, 16, 10191.   
[136] C. Ren, G. Zhong, Q. Xiao, C. Tan, M. Feng, X. Zhong, F. An, J. Wang, M. Zi, M. Tang, Y. Tang, T. Jia, J. Li, Adv. Funct. Mater. 2020, 30, 1906131.   
[137] W. Xiao, C. Liu, Y. Peng, S. Zheng, Q. Feng, C. Zhang, J. Zhang, Y. Hao, M. Liao, Y. Zhou, Nanoscale Res. Lett. 2019, 14, 254.   
[138] C. Ko, Y. Lee, Y. Chen, J. Suh, D. Fu, A. Suslu, S. Lee, J. D. Clarkson, H. S. Choe, S. Tongay, R. Ramesh, J. Wu, Adv. Mater. 2016, 28, 2923.   
[139] Y. Luo, J. Chen, A. Abbas, W. Li, Y. Sun, Y. Sun, J. Yi, X. Lin, G. Qiu, R. Wen, Y. Chai, Q. Liang, C. Zhou, Adv. Funct. Mater. 2024, 34, 2470195.   
[140] Y. Bao, P. Song, Y. Liu, Z. Chen, M. Zhu, I. Abdelwahab, J. Su, W. Fu, X. Chi, W. Yu, W. Liu, X. Zhao, Q.-H. Xu, M. Yang, K. P. Loh, Nano Lett. 2019, 19, 5109.   
[141] Y. Yan, Q. Deng, S. Li, T. Guo, X. Li, Y. Jiang, X. Song, W. Huang, J. Yang, C. Xia, Nanoscale 2021, 13, 16122.   
[142] F. Sui, Y. Yu, J. Chen, R. Qi, R. Ge, Y. Zheng, B. Liu, R. Jin, S. Gong, F. Yue, J. Chu, Nat. Commun. 2025, 16, 1810.   
[143] K. Jeong, H. Lee, C. Lee, L. H. Wook, H. Kim, E. Lee, M.-H. Cho, Appl. Mater. Today 2021, 24, 101122.   
[144] H. Wang, W. Lu, S. Hou, B. Yu, Z. Zhou, Y. Xue, R. Guo, S. Wang, K. Zeng, X. Yan, Nanoscale 2020, 12, 21913.   
[145] X. Ding, M. Li, P. Chen, Y. Zhao, M. Zhao, H. Leng, Y. Wang, S. Ali, F. Raziq, X. Wu, H. Xiao, X. Zu, Q. Wang, A. Vinu, J. Yi, L. Qiao, Matter 2022, 5, 4274.   
[146] M. Wu, X. C. Zeng, Nano Lett. 2017, 17, 6309.   
[147] U. Khan, R. Xu, A. Nairan, M. Han, X. Wang, L. Kong, J. Gao, L. Tang, Adv. Funct. Mater. 2024, 34, 2315522.   
[148] X. Wan, X. Wang, Y. Yu, T. Liu, M. Zhang, E. Chen, K. Chen, S. Wang, F. Shao, X. Gu, J. Xu, ACS Appl. Nano Mater. 2025, 8, 2260.   
[149] J. Yao, Y. Liu, S. Ding, Y. Zhu, Z. Mao, S. V. Kalinin, Y. Liu, Appl. Phys. Lett. 2023, 123, 142903.   
[150] Q. Wang, T. Xie, N. A. Blumenschein, Z. Song, J. C. Kotsakidis, A. T. Hanbicki, M. A. Susner, B. S. Conner, Q. Tan, S. H. Lee, Z. Mao, X. Ling, T. Low, J.-P. Wang, A. L. Friedman, C. Gong, Matter 2022, 5, p4425.   
[151] X. Wang, P. Yu, Z. Lei, C. Zhu, X. Cao, F. Liu, L. You, Q. Zeng, Y. Deng, C. Zhu, J. Zhou, Q. Fu, J. Wang, Y. Huang, Z. Liu, Nat. Commun. 2019, 10, 3037.   
[152] J. Yang, F. Wang, J. Guo, Y. Wang, C. Jiang, S. Li, Y. Cai, X. Zhan, X. Liu, Z. Cheng, J. He, Z. Wang, Adv. Funct. Mater. 2022, 32, 2205468.

[153] M. Wang, H. Nan, X. Gao, C. Wang, Y. Ding, Q. Wu, D. Wan, T. Zhou, L. L. Lin, Z. Cai, S. Xiao, X. Gu, ACS Appl. Nano Mater. 2024, 7, 27640.   
[154] J. Li, Y. Chen, Y. Li, H. Zhu, L. Li, Appl. Phys. Express 2023, 16, 021002.   
[155] Y. Wang, Z. Zeng, Z. Tian, C. Li, K. Braun, L. Huang, Y. Li, X. Luo, J. Yi, G. Wu, G. Liu, D. Li, Y. Zhou, M. Chen, X. Wang, A. Pan, Adv. Mater. 2024, 36, 2410696.   
[156] X. Weng, L. Qi, W. Tang, M. A. Iqbal, C. Kang, K. Wu, Y.-J. Zeng, RSC Adv. 2023, 13, 33588.   
[157] T. Yang, X. Li, L. Wang, Y. Liu, K. Chen, X. Yang, L. Liao, L. Dong, C.-X. Shan, J. Mater. Sci. 2019, 54, 14742.   
[158] T.-P. Hung, W.-H. Chen, Y.-J. Chen, Y.-H. Tu, Z.-H. Huang, Y.-L. Chueh, C.-H. Yeh, C.-W. Chen, Y.-Y. Jhang, Y.-H. Chu, C.-Y. Chen, ACS Appl. Mater. Interfaces 2025, 17, 26931.   
[159] J. Han, C. Fang, M. Yu, J. Cao, K. Huang, Adv. Electron. Mater. 2022, 8, 2100987.   
[160] G. B. Osterhoudt, L. K. Diebel, M. J. Gray, X. Yang, J. Stanco, X. Huang, B. Shen, N. Ni, P. J. W. Moll, Y. Ran, K. S. Burch, Nat. Mater. 2019, 18, 471.   
[161] S. Y. Yang, J. Seidel, S. J. Byrnes, P. Shafer, C. H. Yang, M. D. Rossell, P. Yu, Y. H. Chu, J. F. Scott, J. W. Ager, L. W. Martin, R. Ramesh, Nat. Nanotechnol. 2010, 5, 143.   
[162] I. Grinberg, D. V. West, M. Torres, G. Gou, D. M. Stein, L. Wu, G. Chen, E. M. Gallo, A. R. Akbashev, P. K. Davies, J. E. Spanier, A. M. Rappe, Nature 2013, 503, 509.   
[163] R. K. Vijayaraghavan, S. C. J. Meskers, M. Abdul Rahim, S. Das, Chem. Commun. 2014, 50, 6530.   
[164] T. Rangel, B. M. Fregoso, B. S. Mendoza, T. Morimoto, J. E. Moore, J. B. Neaton, Phys. Rev. Lett. 2017, 119, 067402.   
[165] H. Wang, S. Wu, Y. Chen, Q. Zhao, J. Zeng, R. Yin, Y. Zheng, C. Liu, S. Zhang, T. Lin, H. Shen, X. Meng, J. Ge, X. Wang, J. Chu, J. Wang, Sci. China Inf. Sci. 2024, 68, 122401.   
[166] Y. Peng, X. Liu, Z. Sun, C. Ji, L. Li, Z. Wu, S. Wang, Y. Yao, M. Hong, J. Luo, Angew. Chem., Int. Ed. 2020, 59, 3933.   
[167] E. Bruyer, D. Di Sante, P. Barone, A. Stroppa, M.-H. Whangbo, S. Picozzi, Phys. Rev. B 2016, 94, 195402.   
[168] Y. Wu, Z. Zeng, H. Lu, X. Han, C. Yang, N. Liu, X. Zhao, L. Qiao, W. Ji, R. Che, L. Deng, P. Yan, B. Peng, Nat. Commun. 2024, 15, 8616.   
[169] J. R. Schaibley, H. Yu, G. Clark, P. Rivera, J. S. Ross, K. L. Seyler, W. Yao, X. Xu, Nat. Rev. Mater. 2016, 1, 16055.   
[170] X.-W. Shen, W.-Y. Tong, S.-J. Gong, C.-G. Duan, 2D Mater. 2018, 5, 011001.   
[171] H. Hu, W.-Y. Tong, Y.-H. Shen, C.-G. Duan, J. Mater. Chem. C 2020, 8, 8098.

![](images/e4c9c16d269ca8481f776d6f9db8a42e12790ebf3183cdb38523a454b350a721.jpg)

Mengshuang Chi received her M.S. from Tianjin University in 2020 and Ph.D. from the Beijing Institute of Nanoenergy and Nanosystems, Chinese Academy of Sciences, in 2024. She is currently a postdoctoral fellow at the Beijing Institute of Nanoenergy and Nanosystems, Chinese Academy of Sciences. Her research focuses on multifunctional semiconductor devices based on two-dimensional materials, including piezoelectric, ferroelectric, and flexible devices.

![](images/e8ea78cb7ce3bbfba58d0a1af6a9994f0b8c6e6098ef8d3ee448a4c693c0ae9a.jpg)

Dr. Di Guo is currently an associate professor at the Beijing Institute of Nanoenergy and Nanosystems, Chinese Academy of Sciences. Her research interests mainly revolve around novel multifunctional electronics and optoelectronics devices, focusing on interface engineering by piezoelectric, flexoelectric, and ferroelectric polarizations in semiconductor devices, aiming to delve intensively into the interface science of force-electric-optical multi-field coupling, and develop innovative highperformance semiconductor devices and micro/nano-electromechanical systems.

![](images/3ef07947770ae1af93b68c256a6f10c5bf2ae496971e6342c022dbbd96b82a8f.jpg)

Junyi Zhai received his Ph.D. from Virginia Polytechnic Institute and State University in 2009. He currently serves as the Deputy Director of the Beijing Institute of Nanoenergy and Nanosystems, Chinese Academy of Sciences. His research focuses on the new effects of force-electricity-optical multi-field coupling in semiconductor devices, aiming to investigate in depth the carrier generation, separation, relaxation, and compounding processes in semiconductor heterojunctions and their correlation with the force-electricity-optical multi-field coupling, and to explore a new method of three-dimensional accurate local stress modulation. For further details, visit found at: https://www.x-mol.com/groups/zhai_junyi?lang=zh.