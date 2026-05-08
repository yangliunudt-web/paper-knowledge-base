---
title: "Unveiling pyroelectricity in ferroelectric planar capacitors with area‑selective"
date: "2024-08-28"
year: 2024
journal: "Journal of Physics: Energy"
doi: "10.1088/2515-7655/ad..."
abstract: "In this work, a systematic approach aimed at investigating and validating"
abstract_cn: "本文提出一种系统性的方法，旨在研究和验证实现热电收集的新途径。通过在基于高阻硅的平面叉指电容器中嵌入厚度小于 7 nm 的铁电锆掺杂氧化铪纳米薄膜，利用温度梯度产生直流信号，这是一种新颖、简单、有效且可重复的解决方案。首先通过高级从头计算模拟"
keywords:
  - "[[hafnium zirconium oxide ferroelectrics]]"
  - "[[planar capacitors]]"
  - "[[area-selective wet etching]]"
  - "[[ab initio and multiphysics simulations]]"
  - "[[pyroelectric harvesting]]"
cite: "[1] Aldrigo M, et al. Unveiling pyroelectricity in ferroelectric planar capacitors"
aiSum: "区域选择性湿法刻蚀 HZO 平面电容器实现热电收集：通过从头计算和多物理场模拟预测最大开路电压 900 mV，实验验证输出电流随温度梯度增大而显著提升。"
confidence: "medium"
---

# Unveiling pyroelectricity in ferroelectric planar capacitors with area-selective wet etched hafnium zirconium oxide: from ab initio and multiphysics simulations to experiments

10 October 2024

# ACCEPTED FOR PUBLICATION

24 October 2024

# PUBLISHED

1 November 2024

Original content from this work may be used under the terms of the Creative Commons Attribution 4.0 licence.

Any further distribution of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI.

![](images/0e6f6d083f9e76e3f74d35895b9a93f09e132f231b35b221f96ce41891f55888.jpg)

# PAPER

# Unveiling pyroelectricity in ferroelectric planar capacitors with area-selective wet etched hafnium zirconium oxide: from ab initio and multiphysics simulations to experiments

Martino Aldrigo1,∗, Gian Marco Zampa2, Mircea Dragoman1, Livia Alexandra Dinu1,

Florin Nastase1, Cosmin Romanitan1, Catalin Parvulescu1, Oana Brincoveanu 1,

Sergiu Iordanescu1, Silviu Vulpe1, Emiliano Laudadio3, Elaheh Mohebbi3 and Eleonora Pavoni3,∗ 

1 National Institute for Research and Development in Microtechnologies, IMT-Bucharest, 126A Erou Iancu Nicolae Street, 077190 Voluntari, Ilfov, Romania   
2 Information Engineering Department, Marche Polytechnic University, Via Brecce Bianche, 60131 Ancona, Italy   
3 Department of Matter, Environmental Sciences, and Urban Planning, Marche Polytechnic University, Via Brecce Bianche, 60131 Ancona, Italy   
∗ Authors to whom any correspondence should be addressed.

E-mail: martino.aldrigo@imt.ro and e.pavoni@staff.univpm.it

Keywords: hafnium zirconium oxide ferroelectrics, planar capacitors, area-selective wet etching, ab initio and multiphysics simulations, pyroelectric harvesting

# Abstract

In this work, a systematic approach aimed at investigating and validating a novel way of realizing pyroelectric harvesting is presented. Generating a direct-current (dc) signal through a temperature gradient within a less than 7 nm-thick ferroelectric zirconium-doped hafnium oxide (HZO) nano-film, embedded in planar interdigitated capacitors on high-resistivity silicon, is a new, simple, effective, and reproducible solution. Temperature-related structural modifications in HZO are first simulated using advanced ab initio calculations. Then, rigorous multiphysics simulations of the final devices provide insight into the expected performance of the pyroelectric harvester, as a function of temperature, contact area, and crystal orientation, showing a maximum open-circuit voltage of up to 900 mV. The fabrication of the harvesters involves the area-selective wet etching of the HZO layer to retain it exclusively in between the fingers of each capacitor. This choice maximizes the pyroelectric effect (which strongly depends on the area) and represents a new paradigm in the development of HZO-based electronics, which are conventionally built on ferroelectric continuous films. Experimental validation at both low frequencies and microwaves confirms the pyroelectric effect, exhibiting a significant increase in the output current for higher temperature gradients, and a generated dc voltage of several hundred millivolts.

# 1. Introduction

In an era of increased energy demands and in need of sustainable power sources, energy harvesting techniques can offer an efficient way to collect energy already available in the environment and that would otherwise be lost [1, 2]. In this context, many solutions have been presented in the literature to recover energy from solar and electromagnetic radiation [3], mechanical vibrations [4], or thermal differentials [5]. The latter ones can be obtained from various physical mechanisms that can convert heat differentials into usable electrical energy, such as the thermoelectric, thermophotovoltaic, or pyroelectric effects. In particular, pyroelectricity—the ability of certain materials to generate a spontaneous polarization in response to temperature variations—presents great potential for powering low-consumption electronic devices [6].

In this direction, the investigation and discovery of new pyroelectric materials are crucial to achieve efficient energy harvesters [7–9]. Hafnium-based oxides have been gaining momentum in the last decade, thanks to their remarkable properties and versatile applications across various scientific and technological domains. These oxides, particularly undoped hafnium oxide (HfO2) and zirconium-doped hafnium oxide

(HZO), have received significant attention for their unique combination of high dielectric constant, thermal stability, and compatibility with complementary metal-oxide-semiconductor (CMOS) technology [10, 11]. One of the key driving forces behind the increasing interest in hafnium-based oxides is their potential in advancing semiconductor device technology. As electronic devices shrink in size and the demand for higher performance increases, traditional silicon dioxide $\left( \mathrm { S i O } _ { 2 } \right)$ as a gate dielectric material faces challenges, such as gate leakage and reliability issues [12], that can be circumvented by adopting high-k (where k is the dielectric constant) hafnium-based oxides, which offer superior electrical properties.

The discovery of a stable ferroelectric crystalline structure in hafnium-based oxides with a pyroelectric behavior [13–15] has sparked a significant interest in the scientific community, opening up avenues for novel applications in energy harvesting [16], non-volatile memory devices [17], and sensors [18, 19]. In fact, these materials can substitute commonly used pyroelectrics containing lead, particularly ceramics based on lead-zirconate-titanate (PZT). Moreover, hafnium-based oxides have been demonstrated to keep their ferroelectric phase even at very low thicknesses of just a few nanometers [14, 20]. Moreover, HZO can be directly deposited on silicon and it is possible to pattern its shape through area-selective wet etching (ASWE), which is a reliable, low-cost, and repeatable technique as recently demonstrated [21].

In this paper, we propose an innovative, yet simple coplanar pyroelectric harvester based on HZO and whose structure relies on metallic interdigitated capacitors (IDTs). The ferroelectric ultra-thin film (less than 7 nm thick) was deposited via atomic layer deposition (ALD) directly on high-resistivity silicon (HRSi). It was then configured using ASWE to retain the HZO exclusively in between the fingers of each IDT. In this way, we could enhance the pyroelectric effect as it strongly depends on the capacitive behavior of the device under test (DUT). In this respect, it was of utmost importance to confine the electric field inside the HZO used as the insulating layer between the ‘plates’ of each capacitor by limiting the field penetration inside the substrate underneath (i.e. HRSi). This was accomplished through an ASWE process and it represents a major novelty with respect to the actual state of the art, wherein continuous thin films of HZO are typically used, thus posing intrinsic constraints to its full integration in high-frequency electronics. By selectively patterning the HZO, we can overcome these limitations, thus enabling enhanced performance and seamless integration into microwave circuits. Another reason for this choice was to provide a component easy to embed into any microwave circuit: in fact, each IDT lets the signal pass through almost non-attenuated, but it can be used as a pyroelectric harvester on demand by applying the proper temperature gradient. The multiphysics simulations of the proposed HZO-based pyroelectric harvesters show an impressive maximum open-circuit voltage, up to 900 mV, from a single IDT. Additionally, the experimental validation was carried out at both low and high frequencies, the latter one involving an original setup to induce the pyroelectric effect by heating the HZO while exciting each IDT with a microwave signal. These experiments confirmed the initial hypothesis, with a strong increase of the output current for increasing temperatures and a generated dc voltage of several hundred millivolts when using the high-frequency system.

The paper is organized as follows: first, we provide details about the atomistic and ab initio molecular dynamics (AIMD) simulations used to analyze the deformations of the electron density as a function of temperature, which results in a change of the dielectric permittivity. After that, we present the fabrication of the pyroelectric harvesters and characterization of the HZO ultra-thin films. Then, we discuss the simulated results, using both ab initio simulation tools and the finite-element method software COMSOL Multiphysics, to assess the pyroelectric effect in the proposed HZO-based IDTs. In the last section, we offer a detailed description of the low-frequency and microwave characterization of the manufactured IDTs, followed by some general conclusions.

# 2. Methods and fabrication

# 2.1. Atomistic modeling and AIMD simulations

The atomistic simulations have been performed on the orthorhombic $P c a 2 _ { I }$ polymorph of $\mathrm { H f O } _ { 2 }$ doped with Zr, where the Zr atoms replace 30% of the total amount of Hf $( \mathrm { H f } _ { 0 . 7 } \mathrm { Z r } _ { 0 . 3 } \mathrm { O } _ { 2 } )$ . In particular, the atomistic modeling platform Quantum ATK has been used to model the systems and to carry out the simulations [22]. In detail, the geometrical optimization of the Zr-doped $\mathrm { H f O } _ { 2 }$ system, the electron density, and the permittivity have been performed using the density functional theory (DFT) method. AIMD has been, then, used to accommodate the HZO as a function of the increasing temperature; different trajectory structures, in the temperature range between $2 5 ~ ^ { \circ } \mathrm { C }$ and $4 0 ~ ^ { \circ } \mathrm { C } ,$ , have been extrapolated to evaluate the electron density and to calculate the relative permittivity. About the DFT approach, the linear combination of the atomic orbital (LCAO) method has been used for Hf, Zr, and O [23]. To optimize the geometry of the system the Perdew–Burke–Ernzerhof associated with generalized gradient approximation (GGA-PBE) density functional has been used for the electron exchange energy [24–26]. The ionic cores of the atoms have been simulated making use of the norm-conserving (NC) PseudoDojo (PDj) pseudopotentials [27]. To overcome

the problems related to the finite size of the model and to maintain a high accuracy of the simulation, the periodic boundary conditions (PBCs) have been used along all axes [25, 26]. To estimate the electron density $( \mathbb { A } ^ { - 3 } )$ and the relative permittivity values, the plane wave method, with 100 Hartree as wave function cut-off, has been associated with GGA-PBE functional and plane augmented wave (PAW) pseudopotentials. The iso-surfaces have been considered with an iso-value of 0.6 to plot the electron density.

The energy cut-off has been fixed at 1200 eV and the Brillouin-zone integration has been performed over a $. 1 5 \times 1 5 \times 1 5$ k-points grid, thus the total energy convergence was $5 . 0 \times 1 0 ^ { - 6 }$ eV atom−1, the maximum stress of $2 . 0 \times 1 0 ^ { - 2 }$ GPa, and the maximum displacement of $5 . 0 \times 1 0 ^ { - 4 } \mathrm { \AA } .$

Molecular dynamics simulations have been employed as implemented in Q-ATK. At each time step, the instantaneous Kohn–Sham electronic ground state has been obtained following the previously described DFT approach for the geometry optimization, with a total energy convergence criterion of $1 0 ^ { - 6 }$ eV. Once the instantaneous electronic ground state was known, the forces were calculated from the Hellmann–Feynman theorem [28]. The calculated forces have been then used to integrate the Newtonian equations of motion for the ionic degrees of freedom via the Verlet algorithm [29]. The canonical thermodynamic ensemble maintaining atoms (N), volume (V), and energy (E) (NVE) has been used for the AIMD simulations, and a simulation running time equal to 100 ps has been considered to reach the maximum simulation temperature of $4 0 ~ ^ { \circ } \mathrm { C }$ gradually.

# 2.2. Multiphysics simulations

The electrostatic potential in the structure can be computed by solving the Poisson equation. The terminals are assumed to be perfect metals, which is a reasonable approximation since the hafnium-zirconium oxide is a good insulator, and, therefore, the leakage current is negligible. The heating has been simulated with an external source that models an ultraviolet lamp which will be used in the measurement setup to heat the device. The coupling is defined by equation (1):

$$
P _ {e} = p _ {e} \left(T - T _ {0}\right), \tag {1}
$$

where $P _ { e }$ is the pyroelectric induced polarization, T is the temperature variation, $T _ { 0 }$ is the temperature at which the induced polarization is null, and $\mathit { p _ { e } }$ is the pyroelectric coefficient [30]. The $P _ { e }$ term in equation (2) generates a thermal-induced polarization and, thus, an electric potential in the material. The pyroelectric coefficient can be defined under a constant stress (σ) and electric field (E) as in:

$$
p _ {e} = \left. \frac {\partial P _ {e}}{\partial T} \right| _ {\sigma , E}. \tag {2}
$$

The pyroelectric coefficient for HZO can be found in the literature [14, 31] and it is assumed to be between −48 and −254 $\mu \mathrm { C } \mathrm { m } ^ { - 2 } \mathrm { K } ^ { - 1 }$ . We stress here that all the HZO-based pyroelectric harvesters reported so far are vertical structures [7, 32, 33] of the metal-ferroelectric-metal (MFM) type, hence parallel-plate capacitors. In our work, the planar configuration does not allow the straightforward extraction of $\dot { p } _ { e }$ , which is in any case an intrinsic property of the material.

# 2.3. Fabrication of the pyroelectric harvesters and characterization of the HZO ultra-thin films

The fabrication of the IDTs followed the technological flow depicted in figure 1 and it started from HRSi wafers with the following specifications: orientation ${ < } 1 0 0 >$ , resistivity (Ohm·cm) 10 000–99 999, and thickness in the range 515–535 µm. The silicon wafers were thoroughly cleaned, dried, and then dehydrated under thermal treatment $( 1 6 0 ^ { \circ } \mathrm { C } )$ to achieve optimal adhesion of the photoresist (PR) layer to their surface. The subsequent three main fabrication steps were gold IDT configuration, ALD deposition of the HZO ultra-thin film, and configuration of the oxide layers, as described below.

1) Gold IDT configuration: during the configuration stage of the IDT structures in coplanar waveguide (CPW) technology, a double-layer resist was deposited for sacrificial purposes, facilitating metal configuration using a lift-off process. After PR deposition and exposure through the first photolithographic mask (M1), the development process was achieved, followed by metal deposition (Cr/Au; 20/200 nm, the thin Cr serving as adhesion layer for the Au metallization) using an electron beam evaporation system EVD-500A, Neva, Tokyo, Japan. To finalize the IDT configuration, the lift-off technique involved immersing the wafers in DMSO at $8 0 ~ ^ { \circ } \mathrm { C }$ for 10 min. For each IDT, the signal line of the CPW has a width of 100 µm, whereas the gap with the lateral ground planes is equal to 60 µm. The fingers have a width of 10 µm, a length of 200 $\mu \mathrm { m } ,$ , and an interspacing of 5 µm.   
2) Deposition of the ultra-thin HZO film by ALD: the ferroelectric HZO thin film was synthesized utilizing ALD in an OpAl ALD reactor (Oxford Instruments Plasma Technology). This process was carried out

![](images/e240fa5dba12b6f32b500aba3a3409ba3535791608ab45950f0878c15cdf0f20.jpg)  
Figure 1. The technological flow of the pyroelectric harvester fabrication.

directly on top of pre-patterned gold IDTs to ensure precise material integration and uniform film coverage. Prior to initiating the ALD process, the silicon wafers underwent a surface preparation step, consisting of a UV-ozone cleaning procedure at $7 5 ^ { \circ } \mathrm { C }$ for a duration of 15 min. This step, performed using a UV-ozone cleaning apparatus (Novascan Technologies, USA), was critical to remove organic contaminants and improve surface hydrophilicity, thereby promoting better adhesion and ensuring the high-quality deposition of the HZO film.

3) Configuration of the oxide layer: in the second stage, the oxide layer was selectively patterned between the fingers of the IDT structures. Positive PR AZ1518 was deposited by centrifugation at 4000 rpm, resulting in a 1.8 µm-thick layer, followed by a pre-bake step at $9 5 ^ { \circ } \mathrm { C } .$ . Subsequently, the PR layer was exposed through photolithographic mask M2, to configure the oxide, using UV irradiation at 405 nm for 2.8 s. Development in AZ 726 MIF developer solution for 30 s was followed by thorough rinsing and drying. Lastly, a thermal treatment on a hot plate at $1 1 0 ^ { \circ } \mathrm { C }$ for 1 min was applied to enhance the PR layer’s resistance to chemical solutions.

To etch the 6–7 nm-thick layer of HZO, a 1% HF etchant solution was used. This solution was prepared by diluting HF in water and stored safely when not in use. All wet oxide etching processes were carried out in a cleanroom, maintaining constant humidity levels (below 55%) and temperature $( 2 2 . 0 ^ { \circ } \mathrm { C } \pm 0 . 9 ^ { \circ } \mathrm { C } )$ , using an etch rate of 0.37 $\textrm { \AA } s ^ { - 1 }$ . The full protocol for the wet etching method was described by the group in a previous paper [21]. The optical and SEM (Nova NanoSEM 630 Scanning Electron Microscope from FEI Company, Hillsboro, OR, USA) images of one type of fabricated pyroelectric harvesters are presented in figures 2(a) and (b), respectively. For the final DUTs, we selected a total number of fingers of 23 (small IDT), 30 (intermediate IDT), and 38 (large IDT), i.e. the maximum number of fingers of one of the two electrodes constituting the plates of each IDT. Furthermore, SEM images of two details with the HZO layer in between the fingers are provided in figures 2(c) and (d), respectively. The photolithographic mask, M2, used for etching the ultra-thin oxide layer was designed to slightly overlap by 0.5 µm onto the edges of the gold

![](images/36ffc5e1734b633567063268eb1bcaf64203c2cbad306f1e97172f1cdae7d1ba.jpg)

![](images/c6ff90c2979d56e11a3bbf96b05f302cd40c72b23c6735e189bddb81c878f2fd.jpg)

![](images/d1c11ec69f673948952f36413582a43fc16bc6c9fb1be2ab339d105241b5a0a5.jpg)

![](images/2bb7bf1d9a02694fa16429f08a667cd66fdbe4b0ed2fefde86c297799627ae93.jpg)  
Figure 2. (a) Optical and (b) SEM images of an IDT structure; (c) and (d): SEM images of two details with the HZO layer in between the fingers.

![](images/ef47193699092dd6daa8514069c9911acf40898caa13ee1b75fb5e50eb0315fd.jpg)

![](images/13a5402b8d4298f0786ccbedf8487f0d78cf5dbf1da1c440fce9404ef285b720.jpg)  
Figure 3. (a) XRD spectrum of the HZO ultra-thin film; (b) XRR spectra of the HZO unetched and etched areas.

fingers, as depicted in figure 2(c). This design choice was made to ensure precise etching and prevent potential damage or misalignment during the photolithographic process. By overlapping onto the edges, the mask provides a buffer zone, thus safeguarding the integrity of the oxide layer and maintaining the functionality of the pyroelectric harvester. The final dimensions of the devices are 1.31  2 mm2.

# 2.4. Structural and electrical assessment of the ferroelectric HZO thin film

Figure 3(a) shows the x-ray diffraction (XRD) pattern of HZO acquired with a Rigaku SmartLab diffraction system, before and after the wet etching process. In the first case, one can observe the characteristic diffraction pattern of an HZO ultra-thin film, visible as broad diffraction features centered at ${ \sim } 3 2 ^ { \circ }$ and 53◦. According to the card no. 040-1173 of the International Centre for Diffraction Data (ICDD) database, the broad diffraction features encompass overlapped reflections, namely (101), (012), (111), (103), (113), and (203). After the etching process, only a sharp diffraction peak from Si substrate can be seen, without any diffraction features associated with HZO. The XRD results are further supported by x-ray reflectivity (XRR) spectra, as shown in figure 3(b). Before the etching processes, the XRR pattern presents periodic interference fringes, known as Kiessig fringes, resulting from the interference between the reflected x-ray beam from the surface and the one from the interface to the substrate [34]. Based on the simulation of the experimental pattern using the GlobalFit software developed by Rigaku Corp. (USA), the calculated thickness is ∼6.8 nm.

![](images/ff0276f2f2605324513036822a189462cd47a30e136eda43732f019631172454.jpg)

![](images/4c18e4b5e54f527b506786f538b938b7344d86672f9a1dcbe20957e8d4667dee.jpg)

![](images/70a50fb122ae237cf1a7dda4d2c82b91e3a9fbb62a2a3463425b79fc950ea8ea.jpg)  
Figure 4. Experimental (a) P E and (b) I E loop of the HZO ultra-thin film; (c) PFM phase of the 7 nm-thick HZO film.

A similar value was also obtained from the extended Fast-Fourier transform (FFT) algorithm—shown in the inset of figure 3(b). After etching, no interference fringes can be observed in the XRR pattern. According to the formula relating the critical angle to the sample density, the XRR pattern indicates the presence of bare-Si with a density of 2.33 g cm−3 [35]. Thus, both XRD and XRR investigations prove the complete removal of HZO after the etching process.

Figure 4(a) presents the measured polarization-electric field (P E) loop obtained using the Sawyer-Tower method [36, 37]. The as-deposited HZO demonstrates superior performance compared to the actual state of the art values, with a coercive field $E _ { \mathrm { c } } = 1 . 0 9 \ : \mathrm { M V \ c m ^ { - 1 } }$ and a remanent polarization $P _ { \mathrm { r } } = 4 9 . 1 9 \mu \mathrm { C } \mathrm { c m } ^ { - 2 }$ . Additionally, the spontaneous polarization $P _ { s }$ is $6 5 . 5 6 \mu \mathrm { C } \mathrm { c m } ^ { - 2 }$ , showing excellent stability up to $1 4 0 ^ { \circ } \mathrm { C }$ and a strong endurance over time. The stabilization of the ferroelectric phase by oxygen vacancy engineering during the ALD process, along with the elimination of a wake-up thermal treatment (as required in the TiN/HZO/TiN approach), allow significant flexibility for electronic devices and components operating at microwaves and millimeter-waves. Figure 4(b) displays the measured current-electric field (I−E) loop, with the complete reversal of ferroelectric domains not occurring instantaneously once the coercive field is reached. Ferroelectric materials may exhibit inertia in the domain reorientation process and, even after the coercive field is exceeded, some domains may not immediately reorient, so that rapid changes in polarization—which generate current—can persist even beyond the coercive field threshold. This ‘delay’ effect in the domain response may result in the current peaking after the coercive field has been surpassed. Furthermore, defects or inhomogeneities in the ferroelectric material can delay domain reversal in specific regions. This implies that even if a portion of the domains has reoriented at the coercive field, other domains will continue to reorient at higher fields, leading to a maximum current after the coercive field is exceeded. The occurrence of a current maximum after surpassing the coercive field is associated with the delayed dynamics of ferroelectric domain reversal, influenced by factors such as domain reorientation inertia, material defects, electric field frequency, and relaxation processes. This behavior is not uncommon in ferroelectric material. Piezo-response force microscopy (PFM) measurements were also conducted on the HZO thin film to further demonstrate its ferroelectricity (figure 4(c)). During the manipulation of the ferroelectric domains, the atomic force microscopy (AFM, NtegraScanning Probe Microscope, NT_MDT Spectrum Instruments, USA) tip was held at 0 V, while a dc bias voltage between 10 V and 10 V was applied to the substrate during scanning. The local mechanical response was determined by applying an alternating current (AC) bias to the AFM tip, while the substrate was held at 0 V. figure 4(c) provides the corresponding phase image (top) and phase variation versus distance, showing the phase shift between the response and the excitation. The PFM measurements demonstrate that the HZO film

exhibits easy polarization switching along the poling direction, with clear boundaries between upward and downward domains. The phase shift differs by approximately 180◦ between the successively written areas, confirming that the fabricated HZO thin film is indeed ferroelectric [38].

# 3. Results and discussion

# 3.1. Ab initio simulations

The atomistic simulations were first conducted to optimize the geometry of the Zr-doped $\mathrm { H f O } _ { 2 }$ in its orthorhombic polymorph, as displayed in figure 5, and then to perform AIMD to mimic the effect of a temperature variation (ranging between $2 5 ~ ^ { \circ } \mathrm { C }$ and $4 0 ~ ^ { \circ } \mathrm { C } )$ on the optimized molecular structures. Lastly, the DFT simulations were used to evaluate the electron density in both the room temperature and the heated bulk systems, as well as to calculate the relative permittivity.

The molecular structural changes at different temperatures are strongly connected to the pyroelectric behavior [39], thus the HZO system has been evaluated by increasing the temperature from $2 5 ~ ^ { \circ } \mathrm { C }$ to $4 0 ~ ^ { \circ } \mathrm { C }$ . As expected, the molecular arrangements underwent structural changes in terms of both bond lengths and bond angles. In particular, after optimizing the geometry at $2 5 ^ { \circ } \mathrm { C } .$ , the HZO is characterized by lattice vectors a = 5.22 Å, b = 5.00 Å, and $c = 5 . 0 5 \mathrm { \AA } .$ , in good agreement with the literature [26, 40]. The bond lengths between $\mathrm { Z r } { - } \mathrm { O }$ and Hf–O are on the order of 2.12–2.14 Å, with shorter sizes of about 2.04 Å, while the angles within O–Hf–O are about $1 0 8 ^ { \circ }$ , with a minimum of 81◦, and the angles between Zr–O–Hf are $1 0 6 ^ { \circ }$ . As a consequence of the molecular dynamics, when the system reaches $4 0 \ ^ { \circ } \mathrm { C } ,$ , lattice vectors slightly change to a = 5.24 Å, $b = 5 . 0 2 \mathrm { { \AA } } ,$ , and $c = 5 . 0 8 \mathrm { \AA } .$ . The bond lengths between $_ { Z \mathrm { r } - \mathrm { O } }$ underwent major changes, with a general increase up to $2 . 3 0 { - } 2 . 3 3 .$ , while the bond enclosed between Hf and O became approximately 2.20–2.25 Å, with a minimum of about 2.10 Å. On the other hand, the angles between O–Hf–O showed minor variation compared to the room temperature systems, while the angles between Zr–O–Hf increased to $1 1 4 ^ { \circ }$ . Following the heating up, structural changes have been detected and these modifications are directly responsible for the differences found in the electron density distribution. This latter parameter represents the probability of an electron being present at an infinitesimal element of space surrounding any given point. Furthermore, the electron density is concentrated near the nucleus, showing peaks at the electron density maxima at atomic positions [41]. Thus, the electron density distribution and its changes with the temperature can be understood in terms of the change of dipole arrangement, which leads to the spontaneous polarization underlying the pyroelectric phenomena stemming from temperature fluctuations [42, 43]. To highlight the structural and electronic rearrangements, the most evident changes are denoted with yellow circles in figure 5. The systems obtained from first-principles calculations and the electron density distribution at the two terminal temperatures strongly support the pyroelectric nature of the material. This is not surprising, since the pyroelectricity of pure and doped $\mathrm { H f O } _ { 2 }$ was already observed by other authors in the orthorhombic and tetragonal crystal polymorphs [13, 43].

The analysis of the structural properties as well as the electronic peculiarities of HZO by combining the AIMD approach, for structure evolution, and first-principles DFT, could be even more informative [44]. We have evaluated the effect of the temperature on the relative permittivity (ε) calculated at different temperatures, i.e. on the crystalline structure at $2 5 ^ { \circ } \mathrm { C } , 3 0 ^ { \circ } \mathrm { C } , 3 5 ^ { \circ } \mathrm { C } ,$ , and $4 0 \ { } ^ { \circ } \mathrm { C } ,$ as reported in table 1. Along with the rearrangement of the atoms and the change of the electron density distribution in the bulk HZO, even the relative permittivity changes from a value of 16.62 at $2 5 ~ ^ { \circ } \mathrm { C }$ to 18.78 at $4 0 \ ^ { \circ } \mathrm { C } ,$ , with a total increase of about 13%.

# 3.2. Multiphysics simulations

The final design of the pyroelectric harvester is shown in figure 6. The terminals (T1, T2) feature an interdigitated geometry, in CPW technology, to increase the contact area between the electrodes and, hence, to enhance the pyroelectric effect. The HZO, approximately 7 nm thick, is patterned so that it is only between the fingers. The terminals are connected to coplanar lines, as the device is designed for RF applications. The metals are modeled as 0.5 µm of gold and are deposited on a silicon substrate of 525 µm. We chose to use 0.5 µm of metal as this is the maximum thickness that guarantees a homogeneous, low-roughness surface during the metal deposition process previously described. From a practical point of view, the low-frequency and microwave performance are not affected when using a thinner metallization for the electrodes.

Simulations of the pyroelectric harvester were performed in the time domain using the software COMSOL Multiphysics and applying the finite element method. To investigate the pyroelectric behavior of the structure, a uniform and constant heat source was assumed to operate on the external surface of the device. This source generates a linear increase in temperature until the device reaches thermal equilibrium.

![](images/4bf71ff3a746ab87fa6adfad12fa4297ef651a06d7e72f70661922921dd53a84.jpg)

![](images/d99086105f6412befa91d58870ef787bef8914ad974f799f31477db249e34fea.jpg)

![](images/889f60cdde21f8238460b499e706870374f1ced0c3c886a803922cc359e2771e.jpg)

![](images/6e3ae2a8906be9803d8a8ef4ebc541c9bb9b1c325c6f6d34ae0c48a7d2c41996.jpg)

![](images/f0e6754a4edecde2a522d59db8d95c47fb79b9ff95048fe87dcab08769bc8512.jpg)  
Figure 5. (a) Molecular representation of the orthorhombic polymorph of HZO $( \mathrm { H f } _ { 0 . 7 } \mathrm { Z r } _ { 0 . 3 } \mathrm { O } _ { 2 } )$ , and $( \mathrm { b } ) \mathrm { - } ( \mathrm { e } )$ electron density distribution of the system from two different points of view. The electron density distribution has been evaluated before and after the molecular dynamics, at $2 5 ^ { \circ } \mathrm { C } \left( \mathrm { b } \right)$ and (c) and at 40 ◦C (d) and (e). For the electron density $( \mathring { \mathrm { A } } ^ { - 3 } ) ,$ , the iso-surfaces were considered with an iso-value of 0.6. The atoms composing the molecular structure are O in red, Hf in light blue, and Zr in turquoise green; the major changes at the two edge temperatures are evidenced by yellow or circles.

Table 1. Evolution of the relative permittivity value at different temperatures, i.e. on the crystalline structure at 25 ◦C, 30 ◦C, 35 ${ } ^ { \circ } \mathrm { C } ,$ and $4 0 ~ ^ { \circ } \mathrm { C }$ .   

<table><tr><td>Temperature (°C)</td><td>25</td><td>30</td><td>35</td><td>40</td></tr><tr><td>Relative permittivity</td><td>16.62</td><td>17.35</td><td>17.96</td><td>18.78</td></tr></table>

Under this assumption, the harvester was simulated with different finger numbers (i.e. the maximum number of fingers of one of the two electrodes constituting the plates of each IDT) during a time interval in which the temperature increase is linear. As shown in figure 6(c), the pyroelectric potential between the terminals, terminated as an open circuit, increases proportionally with time and temperature. Devices with larger areas are shown to present higher open circuit voltages $( V _ { \mathrm { O C } } )$ , as expected. This evidence suggests that it is possible to increase the harvested power by increasing the number of fingers. In figure 6(d), the maximum $V _ { \mathrm { O C } }$ is plotted as a function of the number of fingers. From both figures 6(c) and (d) one can observe that the maximum $V _ { \mathrm { O C } }$ reaches almost 900 mV, which is sufficient to charge a supercapacitor using a high-efficiency step-up dc/dc converter that can operate from input voltages as low as a few hundred mV.

Since the pyroelectric effect is highly anisotropic due to crystal asymmetries, it is interesting to study the behavior of the harvester assuming different dipole orientations inside the HZO ultra-thin film. Three limit cases have been studied, assuming the maximum pyroelectric response of the crystal oriented in the x-, y-, and z-directions, respectively, according to the reference system in figure 6(a). In detail, the x- and y-axis are in plane with the IDT but perpendicular to, respectively parallel with, the fingers, whereas the z-axis is

![](images/854f87a5d14032d244cdab199f037097173bd1b9443d1fc83c65a5ab9ea6ef1e.jpg)  
a   
b

![](images/acb2683623b244ece9890c7f5286df7bf00db5a2af49ea9fbcfb6cc59eef5c4e.jpg)

![](images/8e847296023993948834bd6a0904c756d7862bdb60a749e4699a5abd1c345c70.jpg)  
C

![](images/d8b340331859783824059c2e8ab0c815aa9f91ed19d7574e320f7426c4c08bc8.jpg)  
d

![](images/6e444953a962968aee90525f463f78b61a842d3367532c1a23b7282c341811b0.jpg)  
Figure 6. (a) 3D design of the pyroelectric harvester with 40 fingers; (b) top view of the harvester; the HZO is patterned in the region between the fingers; (c) open circuit voltage between T1 and T2 assuming different finger numbers; (d) maximum open circuit voltage reached as a function of the number of fingers; (e) increment of the pyroelectric voltage with temperature (time), assuming the maximum pyroelectric response of the crystal along the x-, y- and z-axis.

perpendicular to the plane of the IDT. As shown in figure 6(e), the higher $V _ { \mathrm { O C } }$ is achieved with a crystal oriented along the y-axis. This happens since the dipole orientation is parallel to the fingers and orthogonal to the terminal, which enhances the in-plane polarization in the direction of the pyroelectric current flow. The worst case is obtained with an orientation along the z-axis due to the polarization increase in the out-of-plane direction. In the real device, the response of the pyroelectric is expected to be a combination of the responses along the different axes.

# 3.3. Low-frequency and microwave characterization

For the low-frequency and microwave characterization of the fabricated pyroelectric harvesters, we prepared two different setups.

# 3.3.1. Low-frequency measurements

The temperature-dependent measurements of the current-voltage (I–V) loops for all three types of IDT were performed using the Radiant Technologies Precision LC II Ferroelectric Tester. The sample temperature was finely controlled with the ThorLabs TC200 Heater Controller in the voltage range between $- 6 \mathrm { V }$ and 6 V, with a maximum electric field of $1 2  { \mathrm { k V } }  { \mathrm { c m } } ^ { - 1 }$ , and a current loop period of 0.1 ms. The temperature was slowly increased from 24 $^ \circ \mathrm { C }$ (room temperature) up to 66 $^ \circ \mathrm { C }$ in steps of 6 $^ \circ \mathrm { C }$ after stabilizing the target value in the controller. The expressions of the pyroelectric current $i _ { \mathrm { p } } ( t )$ and of the current in a capacitor $i _ { \mathrm { C } } ( t )$ are reported in equations (3) and (4), respectively:

$$
i _ {\mathrm {p}} (t) = p _ {e} A \frac {\partial T}{\partial t}, \tag {3}
$$

$$
i _ {\mathrm {C}} (t) = C (\nu) \frac {\partial \nu}{\partial t}, \tag {4}
$$

![](images/a5314d20a3995025a583cbc37a2fdbf51d6d174ae3de675b2627d7742d80ccd8.jpg)

![](images/504feedf2a30e1954abcad09307bfc6445efa356b4df18fc2cb67788cca0ab24.jpg)

![](images/54a3c4de6807c8be0447ce3fb95ade23c5c099fd015c696f8bf798f9aaf6ff91.jpg)

![](images/414f0bfc1491f2e5bb74917e2f7b3210c3b4474e3b90d9f7aa1485f9bc34b365.jpg)

![](images/e821c30c441ee3f9bd4fb2e964dbc83a7e058556a987fc5324dad8da6e817468.jpg)

![](images/673ae40be2c4610fb73c62eaacc8d6664e117a4b82853912f0ef55a2dd0a8ef6.jpg)  
Figure 7. Measured I–V loops at 10 kHz (a), (b), and (c), and current-time curves (d), (e), (f) of the fabricated pyroelectric harvesters as a function of the applied temperature, from $2 4 ~ ^ { \circ } \mathrm { C }$ up to 66 $^ \circ \mathrm { C }$ in steps of ${ \bf \dot { 6 } } ^ { \circ } { \bf C } ,$ for the IDTs with (a) and (d) 23 fingers, (b) and (e) 30 fingers, and (c) and (f) 38 fingers.

where A is the contact area of the DUT, ∂T/∂t is the time derivative of the temperature T, C is the static capacitance, and v is the voltage. From analytical calculations and electromagnetic (static) simulations carried out using CST Studio Suite 2023, C  0.7, 0.95, and 1.2 pF for the structures with 23, 30, and 38 fingers (small, intermediate, and large IDT, as defined previously), respectively. From equation (4), it is evident that the current flowing through a conventional capacitor does not depend on temperature: this was confirmed by measuring the same three types of IDT without the HZO layer in between the fingers, where the only variations in the (much lower and without hysteresis) current values were ascribed to changes in the total capacitance of each IDT. On the other hand, figure 7 is directly associated with the already described ab initio simulations and with equation (3). In detail, figure 7 shows the I–V loops and the current-time curves, respectively, for the small, intermediate, and large IDT. It is apparent that there is a significant increase in the current when increasing the number of fingers: for example, at 6 V and 66 $^ { \circ } \mathrm { C } ,$ the maximum current is about 143 $\mu \mathrm { A }$ for the small IDT, 189 $\mu \mathrm { A }$ for the intermediate IDT (32% more), and 222 $\mu \mathrm { A }$ for the large IDT (55% more with respect to the small IDT and 18% more with respect to the intermediate IDT). If we consider the variation of the current with temperature, the rise exhibits a monotonic behavior in all cases: at 6 V, the current increases from 32 $\mu \mathrm { A }$ to 143 $\mu \mathrm { A }$ for the small IDT (447% more), from 42 $\mu \mathrm { A }$ to 189 $\mu \mathrm { A }$ for the intermediate IDT (450% more), and from 51 $\mu \mathrm { A }$ to 222 $\mu \mathrm { A }$ for the large IDT (435% more). These results are repeatable in time and terms of different DUTs on the same wafer, which proves the reliability of the fabrication process. Most importantly, they give proof of the pyroelectric effect inside the HZO ultra-thin film, i.e. the strong dependence of the current on both the contact area and the temperature variation. Figure 7(a) through figure 7(f) unequivocally demonstrate the ferroelectric nature of HZO: the hysteretic behavior of the current flowing through each IDT for any considered temperature (attributed to the storage of charges inside HZO) is evident. There is an asymmetry that favors the negative values of the applied voltage in terms of both the width of the hysteresis window and the current level. The shape of the I–V loops indicates a strong frequency dependence on the polarization switching measurements performed on the fabricated DUTs, which suggests the existence of a time delay between the voltage peak and the current peak at the selected frequency (i.e. 10 kHz) [45]. The latter frequency was chosen to emphasize the ferroelectric effect. Considering that the IDTs with HZO configured through ASWE represent an unconventional type of structures for pyroelectric harvesters, their electrical characterization requires special precautions and settings.

![](images/390b4fd93f5da3fe18c7a1d476febea43a8af219159d9b3e06e4933f8879d9bd.jpg)  
a

![](images/b76ab6c5e1594dcb5028e7f3ef524112f1478184cdb68b809c5f8a53f80d5a61.jpg)  
b

![](images/ca48913925db24c37ede1fa37c78dc5d80755fd1e7ea93809e3a2c1e621678b6.jpg)  
C

![](images/a3d6f4c36caca1220ac40f3eb96e147dc5fd1cf5ad3332bd69df9ba5208680de.jpg)  
  
Figure 8. (a) Measured transmission coefficients in the 0.1–8 GHz band for the IDTs with 23 (solid black line), 30 (solid red line), and 38 (solid blue line) fingers; (b) schematic representation of the microwave setup; (c) typical current-voltage (i–v) curve of a Schottky diode and illustration of the effect of the pyroelectric voltage $V _ { \mathrm { p y r o } } ;$ (d) output dc voltage $V _ { \mathrm { d c } }$ read on the oscilloscope without and with UV illumination.

# 3.3.2. Microwave measurements

As stated in the Introduction, we chose to develop planar pyroelectric harvesters, where HZO is selectively etched to remain exclusively in between the fingers of the IDTs. This choice was motivated by their straightforward integration with other microwave components using CMOS-compatible processes. In fact, the capacitance value of each IDT allows the microwave signal to pass through, almost non-attenuated, while enabling activation of the pyroelectric harvester on demand by applying the appropriate temperature gradient. This can be verified by inspecting figure 8, where the transmission coefficient between the two ports of each DUT $\left( \left| \mathsf { S } _ { 2 1 } \right| \mathrm { o r } \left| \mathsf { S } _ { 1 2 } \right| \right)$ , expressed in dB) is depicted for the three IDTs in the 100 MHz–8 GHz band. In detail, between 1.58 GHz and 8 GHz, the transmission is always better than 5 dB. The high-frequency measurements were performed by using a vector network analyzer (VNA, Anritsu 37397D). After this preliminary assessment of the miniaturized IDTs, we resumed to a novel setup to verify their pyroelectric behavior (figure 8(b)): a microwave generator (Agilent E8257D) was connected via coplanar probe tips (pitch of 150 µm) to one port of an IDT placed on the chuck of a SUSS MicroTec probe station. ¨ The other port of the IDT was connected to an oscilloscope (Tektronix DPO2024) via a 75VA50 microwave detector (Anritsu low-barrier Schottky diode, negative polarity). Then, we used an UV LED source (wavelength λ = 396 nm, output power $P _ { 0 } = 2 2 5 { - } 2 2 8 \mathrm { m W }$ at a distance d = 10–20 mm) to heat the IDT up with an approximately constant rate $\partial T / \partial t = 0 . 2 5 ^ { \circ } \mathrm { C } s ^ { - 1 }$ from room temperature up to $4 0 { } ^ { \circ } \mathrm { C } \mathrm { - } 4 1 { } ^ { \circ } \mathrm { C }$ (this temperature representing the maximum value allowed by the UV LED source to avoid overheating). The aim was to extract indirectly the dc voltage generated by the pyroelectric harvester, as follows: the detector works as a rectifier for the signal injected by the microwave generator (we chose an amplitude-modulated 2.45 GHz signal with frequency modulation of 1 kHz and power level of −3 dBm). This means that the output from the detector is a dc current, which is then transformed into an output dc voltage $V _ { \mathrm { d c } }$ in the oscilloscope (with input port impedance equal to 1 MΩ in parallel with 11.7 pF). The initial hypothesis is illustrated in figure 8(c): a pyroelectric harvester generating an output dc voltage $V _ { \mathrm { p y r o } }$ of a few hundred millivolts can bias the diode inside the detector, thus moving its operating point beyond the threshold voltage $V _ { \gamma }$ and very close to the linear regime of the current i (which diminishes diode’s rectifying capabilities). Since $V _ { \gamma }$ attains values between 0.15 and 0.46 V for a typical Schottky diode, it means that $V _ { \mathrm { p y r o } }$ must be much greater, in agreement

with the multiphysics simulations shown in section 3.2. The overall effect observable from the microwave characterization will be a decrease in the output dc voltage $V _ { \mathrm { d c } }$ read on the oscilloscope when illuminating each IDT with the UV LED source. The final results are depicted in figure 8(d), which presents the oscilloscope output dc voltage $V _ { \mathrm { d c } }$ as a function of time for all three IDT types. Following figure 8(a), it can be observed that the large IDT exhibits the highest transmission value at 2.45 GHz, followed by the intermediate and small IDTs. This means that the large IDT enables the maximum power transfer to the detector. The latter fact translates into a higher rectified voltage. Figure 8(d) is a direct proof of this fact, considering that the detector works for negative polarities, hence the more negative the value of $V _ { \mathrm { d c } } ,$ the higher the voltage rectified by the Schottky diode. The horizontal dotted lines refer to the cases without UV illumination, with $V _ { \mathrm { d c } }$ falling between about −61 mV (small IDT) and about −75 mV (large IDT). When heating each IDT up with the UV source, the voltage drop ranges from approximately 7 mV (small IDT) to about 9 mV (large IDT). From these experimental measurements, it is possible to provide an estimation of the power generated from the harvester. Since the oscilloscope used to measure the DC voltage presents an input port resistance of 1 MΩ, the dissipated power in this configuration can be obtained from $P = V \times I = V ^ { 2 } / R$ . This power is also the power generated from the harvester since the parallel capacitance can be assumed as an open circuit at dc regime. According to the measured voltages, the corresponding power outputs will be between 49 nW (small IDT) and 81 nW (large IDT). Certainly, this represents just a rough estimation since the load is not designed to optimize the power transfer. At low frequencies, the maximum power generated in our experiments varies between $8 4 0 ~ \mu \mathrm { W }$ (small IDT) and 1.32 mW (large IDT). This result was expected, as the capacitive effect of the IDT is much more pronounced at low frequencies (see figure 8(a)). However, these outcomes are still remarkable and they can be further increased. Moreover, the modularity of the proposed approach allows putting in parallel many capacitors, hence tailoring the output power to the specific application. This voltage drop is proportional to the finger number, as expected. This relationship arises because the larger the contact area of the pyroelectric harvester, the greater the value of $V _ { \mathrm { p y r o } ; }$ , which in turn brings the diode closer to its linear regime, hence reducing the rectified voltage and, consequently, $V _ { \mathrm { d c } }$ . These results prove the pyroelectricity of the ultra-thin HZO-based planar IDTs and encourage further investigations, also resorting to other types of dopants (like yttrium or aluminum). Furthermore, the multiplication of such structures to increase the pyroelectric current is straightforward thanks to their CPW configuration and miniaturized dimensions, which allows us to arrange them in parallel in a large number and, thus, to increase the overall capacitance.

We stress here that we also performed measurements on the same IDTs without HZO to assess the outcome of directly illuminating the HRSi substrate with the UV LED source, knowing that a small photoelectric effect can occur when using a 396 nm UV radiation. In this case, the output dc voltage $V _ { \mathrm { d c } }$ exhibits just small, constant (i.e. irrespective of the contact area) changes around 2 mV. However, due to the strong absorption inside the HZO, the presence of the ferroelectric layer highly reduces the photoelectric effect, which becomes negligible.

# 4. Conclusion

In summary, this work proposes a novel strategy for fabricating easy-to-integrate planar pyroelectric harvesters based on ultra-thin films (less than 7 nm thick) of zirconium-doped hafnium oxide (HZO), selectively etched in between the fingers of interdigitated capacitors directly configured on a high-resistivity silicon wafer. Unlike traditional approaches relying on vertical structures of the metal-ferroelectric-metal type with continuous ferroelectric layers, the presented technological solution is simple yet effective and reliable. Starting from ab initio and multiphysics simulations, we first investigated the effects of temperature variation on the mechanical and electrical properties within the HZO crystalline structure, as well as on the output dc pyroelectric voltage of the final harvesters. Each capacitor is able to generate an impressive maximum open-circuit voltage up to 900 mV, which is sufficient to charge a supercapacitor using a high-efficiency step-up dc/dc converter. Then, the fabricated devices have been characterized at both low frequencies and microwaves: in the first case, a temperature variation induces an increase in the current intensity of maximum 450%, whereas the original microwave setup, specifically developed for this type of structure, confirmed the generation of a pyroelectric voltage of several hundred millivolts. This work provides a pioneering approach for developing efficient and CMOS-compatible pyroelectric harvesters based on nanometer-scale ferroelectrics.

# Data availability statement

The data cannot be made publicly available upon publication because no suitable repository exists for hosting data in this field of study. The data that support the findings of this study are available upon reasonable request from the authors.

# Acknowledgment

Martino Aldrigo and Gian Marco Zampa contributed equally to this work.

This work was supported by the Romanian Ministry of Research, Innovation and Digitization: in part by CCCDI—UEFISCDI within PNCDI III under Project PN-III-P4-PCE-2021-0223, and in part by the Core Program within the National Research Development and Innovation Plan 2022–2027, under Project PN 2307 ‘µNanoEl’ (Contract No. 8N/03.01.2023, Sub-Projects PN 23070101 and PN 23070201).

# Conflict of interest

The authors declare no conflict of interest.

# ORCID iDs

Martino Aldrigo  https://orcid.org/0000-0003-2257-1966 Gian Marco Zampa  https://orcid.org/0000-0002-9957-8691 Mircea Dragoman  https://orcid.org/0000-0001-6886-5295 Livia Alexandra Dinu  https://orcid.org/0000-0002-3264-2548 Florin Nastase  https://orcid.org/0000-0002-6764-0403 Cosmin Romanitan  https://orcid.org/0000-0002-5615-6624 Catalin Parvulescu  https://orcid.org/0000-0001-8570-0089 Oana Brincoveanu  https://orcid.org/0000-0002-4860-2591 Sergiu Iordanescu  https://orcid.org/0000-0001-9471-6306 Silviu Vulpe  https://orcid.org/0000-0002-3269-1382 Emiliano Laudadio  https://orcid.org/0000-0002-8053-6539 Elaheh Mohebbi  https://orcid.org/0000-0002-5866-7911 Eleonora Pavoni  https://orcid.org/0000-0002-0711-0021

# References

[1] Wang Z L 2020 On the first principle theory of nanogenerators from Maxwell’s equations Nano Energy 68 104272   
[2] Sheng X L, Li Y, Pu S and Wang Q 2022 Lorentz transformation in Maxwell equations for slowly moving media Symmetry 14 1641   
[3] Dragoman M, Aldrigo M, Dinescu A, Vasilache D, Iordanescu S and Dragoman D 2023 Nanomaterials and devices for harvesting ambient electromagnetic waves Nanomaterials 13 595–602   
[4] Kim H S, Kim J H and Kim J 2011 A review of piezoelectric energy harvesting based on vibration Int. J. Precis. Eng. Manuf. 12 1129–41   
[5] Lingam D, Parikh A R, Huang J, Jain A and Minary-Jolandan M 2013 Nano/microscale pyroelectric energy harvesting: challenges and opportunities Int. J. Smart Nano Mater. 4 229–45   
[6] Yang Y, Zhou Y, Wu J M and Wang Z L 2012 Single micro/nanowire pyroelectric nanogenerators as self-powered temperature sensors ACS Nano 6 8456–61   
[7] Mondal R, Hasan M A M, Baik J M and Yang Y 2023 Advanced pyroelectric materials for energy harvesting and sensing applications Mater. Today 66 273–301   
[8] He H, Lu X, Hanc E, Chen C, Zhang H and Lu L 2020 Advances in lead-free pyroelectric materials: a comprehensive review J. Mater. Chem. C 8 1494–516   
[9] Zhang D, Wu H, Bowen C R, Yang Y, Zhang D, Wu H, Yang Y and Bowen C R 2021 Recent advances in pyroelectric materials and applications Small 17 2103960   
[10] Ambriz-Vargas F, Kolhatkar G, Broyer M, Hadj-Youssef A, Nouar R, Sarkissian A, Thomas R, Gomez-Yánez C, Gauthier M A and ˜ Ruediger A 2017 A complementary metal oxide semiconductor process-compatible ferroelectric tunnel junction ACS Appl. Mater. Interfaces 9 13262–8   
[11] Hyuk Park M, Joon Kim H, Jin Kim Y, Lee W, Kyeom Kim H and Seong Hwang C 2013 Effect of forming gas annealing on the ferroelectric properties of Hf0.5Zr0.5O2 thin films with and without Pt electrodes Appl. Phys. Lett. 102 112914   
[12] Sun Z 2023 Comparison and analysis of gate dielectrics for SiC MOSFET Appl. Comput. Eng. 23 223–9   
[13] Böscke T S, Müller J, Bräuhaus D, Schröder U and Böttger U 2011 Ferroelectricity in hafnium oxide thin films Appl. Phys. Lett. 99 102903   
[14] Smith S W, Kitahara A R, Rodriguez M A, Henry M D, Brumbach M T and Ihlefeld J F 2017 Pyroelectric response in crystalline hafnium zirconium oxide (Hf1-xZrxO2) thin films Appl. Phys. Lett. 110 72901   
[15] Neuber M, Lederer M W, Mertens K, Kämpfe T, Czernohorsky M and Seidel K 2022 Pyroelectric and ferroelectric properties of hafnium oxide doped with Si via plasma enhanced ALD Crystals 12 1115

[16] Mart C et al 2020 Energy harvesting in the back-end of line with CMOS compatible ferroelectric hafnium oxide Technical Digest—Int. Electron Devices Meeting, IEDM pp 26.3.1–4   
[17] Müller J et al 2012 Ferroelectricity in HfO2 enables nonvolatile data storage in 28 nm HKMG Digest of Technical Papers—Symp. on VLSI Technology pp 25–26   
[18] Mart C, Kühnel K, Kämpfe T, Zybell S and Weinreich W 2019 Ferroelectric and pyroelectric properties of polycrystalline La-doped HfO2 thin films Appl. Phys. Lett. 114 102903   
[19] Mart C, Weinreich W, Czernohorsky M, Riedel S, Zybell S and Kuhnel K 2018 CMOS compatible pyroelectric applications enabled by doped HfO2 films on deep-trench structures European Solid-State Device Research Conf. pp 130–3   
[20] Peˇsi´c M, Schroeder U and Mikolajick T 2019 Ferroelectric One Transistor/one Capacitor Memory Cell (Elsevier)   
[21] Dinu L A et al 2023 Investigation of wet etching technique for selective patterning of ferroelectric zirconium-doped hafnium oxide thin films for high-frequency electronic applications Mater. Des. 233 112194   
[22] Smidstrup S et al 2019 QuantumATK: an integrated platform of electronic and atomic-scale modelling tools J. Phys.: Condens. Matter 32 015901   
[23] Soler J M, Artacho E, Gale J D, García A, Junquera J, Ordejón P and Sánchez-Portal D 2002 The SIESTA method for ab initio order-N materials simulation vol 14   
[24] Perdew J P, Burke K and Ernzerhof M 1996 Generalized gradient approximation made simple Phys. Rev. Lett. 77 3865–8   
[25] Pavoni E, Mohebbi E, Mencarelli D, Stipa P, Laudadio E and Pierantoni L 2022 The effect of Y doping on monoclinic, orthorhombic, and cubic polymorphs of HfO : a first principles study Nanomaterials 12 1–12   
[26] Pavoni E, Mohebbi E, Stipa P, Mencarelli D, Pierantoni L and Laudadio E 2022 The role of Zr on monoclinic and orthorhombic Hfx Zry O2 systems: a first-principles study Materials 15 4175–88   
[27] van Setten M J, Giantomassi M, Bousquet E, Verstraete M J, Hamann D R, Gonze X and Rignanese G M 2018 The PSEUDODOJO: training and grading a 85 element optimized norm-conserving pseudopotential table Comput. Phys. Commun. 226 39–54   
[28] Feynman R P 1939 Forces in molecules Phys. Rev. 56 340   
[29] Grubmüller H, Heller H, Windemuth A and Schulten K 1991 Generalized verlet algorithm for efficient molecular dynamics simulations with long-range interactions Mol. Simul. 6 121–42   
[30] Newham R E 2005 Properties of Materials Anisotropy, Symmetry, Structure (Oxford University Press)   
[31] Park M H, Kim H J, Kim Y J, Moon T, Do Kim K and Hwang C S 2015 Toward a multifunctional monolithic device based on pyroelectricity and the electrocaloric effect of thin antiferroelectric HfxZr1 xO2 films Nano Energy 12 131–40   
[32] Zhou Y and W H G 2023 Pyroelectric heat harvesting, what’s next? Next Energy 1 100026   
[33] Priya K S, Pal S, Mohan M and Murugavel P 2023 High performance near-room-temperature pyroelectric energy harvesting characteristics of ferroelectric-semiconductor composites ACS Appl. Electron. Mater. 5 3790–7   
[34] Daillant J and Gibaud A 1999 X-ray and Neuron Reflectivity: Principles and Applications (Springer)   
[35] Birkholz M 2006 Thin Film Analysis by X-ray Scattering (Wiley)   
[36] Dragoman M, Aldrigo M, Dragoman D, Iordanescu S, Dinescu A, Vulpe S and Modreanu M 2023 Ferroelectrics at the nanoscale: materials and devices—a critical review Crit. Rev. Solid State Mater. Sci. 48 561–79   
[37] Sawyer C B and Tower C H 1930 Rochelle salt as a dielectric Phys. Rev. 35 269   
[38] Aldrigo M, Dragoman M, Iordanescu S, Nastase F and Vulpe S 2020 Tunable microwave filters using $\mathrm { H f O } _ { 2 } .$ -based ferroelectrics Nanomaterials 10 2057   
[39] Li T, Zou Y and Liu Z 2023 Magnetic-thermal external field activate the pyro-magnetic effect of pyroelectric crystal (NaNbO3) to build a promising multi-field coupling-assisted photoelectrochemical water splitting system Appl. Catal. B 328 122486   
[40] Sang X, Grimley E D, Schenk T, Schroeder U and Lebeau J M 2015 On the structural origins of ferroelectricity in HfO thin films Appl. Phys. Lett. 106 162905   
[41] Gupta V P 2015 Principles and Applications of Quantum Chemistry (Elsevier)   
[42] Yu Z, Gong H, Gao Y, Li L, Xue F, Zeng Y, Li M, Liu X and Tang D 2022 Integrated photothermal-pyroelectric biosensor for rapid and point-of-care diagnosis of acute myocardial infarction: a convergence of theoretical research and commercialization Small 18 2202564   
[43] Liu J, Liu S, Liu L H, Hanrahan B and Pantelides S T 2019 Origin of pyroelectricity in ferroelectric HfO2 Phys. Rev. Appl. 12 034032   
[44] Wang Y, Zahid F, Wang J and Guo H 2012 Structure and dielectric properties of amorphous high-κ oxides: hfO , ZrO , and their alloys Phys. Rev. B 85 224110   
[45] Gao Z, Lyu S and Lyu H 2022 Frequency dependence on polarization switching measurement in ferroelectric capacitors J. Semicond. 43 014102