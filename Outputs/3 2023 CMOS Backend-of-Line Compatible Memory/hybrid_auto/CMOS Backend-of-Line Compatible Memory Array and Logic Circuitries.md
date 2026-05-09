---
title: "CMOS Backend-of-Line Compatible Memory Array and Logic Circuitries"
authors:
  - "Wenhui Wang"
  - "Ke Li"
  - "Jun Lan"
  - "Mei Shen"
  - "Zhongrui Wang"
  - "Xuewei Feng"
  - "Hongyu Yu"
  - "Kai Chen"
  - "Jiamin Li"
  - "Feichi Zhou"
  - "Longyang Lin"
  - "Panpan Zhang"
  - "Yida Li"
date: "2023-09-28"
year: 2023
journal: "Nature Communications"
doi: "10.1038/s41467-023-41532-0"
abstract: "The development of high-performance oxide-based transistors is critical to enable very large-scale integration (VLSI) of monolithic 3-D integrated circuit (IC) in complementary metal oxide semiconductor (CMOS) backend-of-line (BEOL). Atomic layer deposition (ALD) deposited ZnO is an attractive candidate due to its excellent electrical properties, low processing temperature below copper interconnect thermal budget, and conformal sidewall deposition for novel 3D architecture. An optimized ALD deposited ZnO thin-film transistor achieving a record field-effect and intrinsic mobility (μFE/μo) of 85/140 cm²/V·s is presented here. The ZnO TFT was integrated with HfO2 RRAM in a 1 kbit (32×32) 1T1R array, demonstrating functionalities in RRAM switching. In order to co-design for future technology requiring high performance BEOL circuitries implementation, a spice-compatible model of the ZnO TFTs was developed. We then present designs of various ZnO TFT-based inverters, and 5-stage ring oscillators through simulations and experiments with working frequency exceeding 10's of MHz."
abstract_cn: "高性能氧化物晶体管的发展对于在CMOS后端工艺中实现单片三维集成电路的超大规模集成至关重要。原子层沉积ZnO因其优异的电学特性、低于铜互连热预算的低工艺温度、以及适用于新型3D架构的保形侧壁沉积而成为有吸引力的候选材料。本文展示了优化的ALD-ZnO薄膜晶体管，实现了85/140 cm²/V·s的记录场效应/本征迁移率。ZnO TFT与HfO2 RRAM集成在1 kbit（32×32）1T1R阵列中，展示了RRAM开关功能。为未来需要高性能BEOL电路实现的技术协同设计，开发了ZnO TFT的spice兼容模型。通过仿真和实验展示了各种基于ZnO TFT的反相器和5级环形振荡器，工作频率超过数十MHz。"
keywords:
  - "[[CMOS Backend-of-Line]]"
  - "[[ZnO TFT]]"
  - "[[RRAM]]"
  - "[[Monolithic 3D Integration]]"
  - "[[1T1R Array]]"
  - "[[CMOS后道集成]]"
  - "[[氧化物半导体]]"
cite: "[1] Wang W, Li K, Lan J, et al. CMOS backend-of-line compatible memory array and logic circuitries enabled by high performance atomic layer deposited ZnO thin-film transistor[J]. Nature Communications, 2023."
aiSum: "CMOS BEOL兼容ZnO TFT：ALD工艺、85/140 cm²/V·s迁移率、1 kbit 1T1R RRAM阵列、环形振荡器>10 MHz、spice模型。"
confidence: "high"
wiki_concepts:
  - "[[RRAM]]"
---

# CMOS backend-of-line compatible memory array and logic circuitries enabled by high performance atomic layer deposited ZnO thin-film transistor

Received: 24 May 2023

Accepted: 14 September 2023

Published online: 28 September 2023

Check for updates

Wenhui Wang $^{1,5}$ , Ke Li $^{1,5}$ , Jun Lan $^{1}$ , Mei Shen $^{1}$ , Zhongrui Wang $^{2}$ , Xuewei Feng $^{3}$ , Hongyu Yu $^{1}$ , Kai Chen $^{1}$ , Jiamin Li $^{1}$ , Feichi Zhou $^{1}$ , Longyang Lin $^{1}$ , Panpan Zhang $^{4}$ , & Yida Li $^{1}$

The development of high-performance oxide-based transistors is critical to enable very large-scale integration (VLSI) of monolithic 3-D integrated circuit (IC) in complementary metal oxide semiconductor (CMOS) backend-of-line (BEOL). Atomic layer deposition (ALD) deposited ZnO is an attractive candidate due to its excellent electrical properties, low processing temperature below copper interconnect thermal budget, and conformal sidewall deposition for novel 3D architecture. An optimized ALD deposited ZnO thin-film transistor achieving a record field-effect and intrinsic mobility $(\mu_{FE} / \mu_{o})$ of 85/140 $\mathrm{cm}^2/\mathrm{V}\cdot\mathrm{s}$ is presented here. The ZnO TFT was integrated with $\mathrm{HfO}_2$ [[RRAM]] in a 1 kbit $(32 \times 32)$ 1T1R array, demonstrating functionalities in RRAM switching. In order to co-design for future technology requiring high performance BEOL circuitries implementation, a spice-compatible model of the ZnO TFTs was developed. We then present designs of various ZnO TFT-based inverters, and 5-stage ring oscillators through simulations and experiments with working frequency exceeding 10's of MHz.

With the growing demand for data-driven applications such as the next-generation machine learning accelerators and the Internet of Things (IoT), the traditional von-Neumann architecture with disjoint memory and processing units suffers from huge memory latency and limited data bandwidth, which is further intensified by the scaling limits of silicon transistors. In order to surpass these bottlenecks, monolithic-three-dimensional (M3D) integration of fused logic and memory $^{1}$ , or [[in-memory computing]] $^{2,3}$ , with functional logic circuits has emerged as a potential solution. However, the utility of silicon (Si) technology for beyond BEOL integration is challenged by the low thermal budget ( $<400^{\circ}\mathrm{C}$ ) posed by the low-k dielectric and copper

interconnects, where subjected to higher temperatures results in reliability issues. Beyond-Si devices that can be co-integrated additively on Si-based complementary metal-oxide-semiconductor (CMOS) chips, include carbon nanotube (CNT) field-effect transistors (FETs) $^{4-6}$ , two-dimensional (2D) materials $^{7-10}$ , and oxide semiconductors $^{11,12}$ . Among them, oxide semiconductors, such as indium gallium zinc oxide ([[IGZO]]) $^{13-15}$ , indium oxide $(\mathrm{In}_2\mathrm{O}_3)$ ^{16}, and zinc oxide $(\mathrm{ZnO})^{17-22}$ , are well poised to be competitive n-channel materials beyond silicon due to their low thermal budget process, good transparency, process maturity for large scale deposition, and decent electrical properties, such as high carrier mobility, wide bandgap, low

$^{1}$ School of Microelectronics, Southern University of Science and Technology, 518055 Shenzhen, China. $^{2}$ Department of Electrical and Electronic Engineering, The University of Hong Kong, 999077 Hong Kong SAR, China. $^{3}$ Shanghai Jiao Tong University, 200240 Shanghai, China. $^{4}$ State Key Laboratory of Information Photonics and Optical Communications, Beijing University of Posts and Telecommunications, 100876 Beijing, China. $^{5}$ These authors contributed equally: Wenhui Wang, Ke Li. $^{e}$ -mail: linly@sustech.edu.cn; tanji ic@bupt.edu.cn; liyd3@sustech.edu.cn

gate leakage $^{23,24}$ . These merits make them suitable for backend-of-line (BEOL) integration as memory drivers in memory-centric computing cells or high-performance thin-film transistor (TFT)-based BEOL logic circuitries (Fig. 1a) $^{7,25}$ . With the increasing interest to realize new computing architecture with new functionalities and enhanced computing power, the development of high-performance oxide-based transistors to enable very large-scale integration (VLSI) of M3D integrated circuit (IC) in CMOS BEOL is timely.

Of these promising n-channel oxide candidates, polycrystalline $\mathrm{ZnO}$ exhibits one of the highest carrier mobility through proper crystallinity and oxygen vacancies $(V_{O})$ tuning[17,22]. In addition, its other advantageous properties, such as wide direct bandgap $(-3.3\mathrm{eV})$ and high thermal conductivity, make $\mathrm{ZnO}$ a strong competitor to complement the matured and conventional silicon. Moreover, $\mathrm{ZnO}$ has been reported to be grown by industry-accepted techniques such as magnetron sputtering[26], or atomic layer deposition (ALD)[17]. All these benefits offer $\mathrm{ZnO}$ as one of the best propositions in low-temperature channel material selection for CMOS-BEOL integration. While there have been reports on high-performance $\mathrm{ZnO}$ TFT[27], the reproducibility

of results is still challenging due to the difficult process control as well as ensuring the long-term stability of the ZnO layer due to its hygroscopic nature. Further, among the popular deposition techniques, the ALD approach is attractive for its low-temperature process (typically $<300^{\circ}\mathrm{C}$ ), accurate stoichiometry, thickness and uniformity control, and conformal sidewall deposition for M3D integration of vertically integrated architectures[28,29]. However, despite the promises, reports on high-performance ALD ZnO TFT, and a systematic guidance to implement it in BEOL-compatible logic circuit are still lacking, calling the need to further address these aspects.

High-performance oxide TFTs have been reported to be good selectors for emerging memories such as resistive random access memory (RRAM)<sup>7</sup>, and can be used to implement circuits such as basic logic gates<sup>30</sup>, amplifiers<sup>31</sup>, gate driver<sup>32</sup>, microprocessor<sup>33</sup>, etc. However, from logic circuit point of view, unipolar oxide TFTs-based circuit designs face huge challenges due to the lack of p-type oxide semiconductor FETs that match that of its n-type counterpart<sup>34</sup>. In order to overcome the challenges of designing for unipolar device-based circuits, pseudo-CMOS design style, including pseudo enhancement and

![](images/ca206771f1937f64a343def470fd13b017dab1d7481d420b10411518575811e2.jpg)  
a

![](images/605642559982cff428bd794edd04af24de9129e0a8e261c1751522de51e017c8.jpg)  
b

![](images/90d7b44f245133f3bca7be57bd65ff1aaf85b28a52ed60ecc6862620142e015a.jpg)  
C   
Fig. 1 | ZnO as CMOS-BEOL-compatible transistor material. a Schematic illustrating the use of low-temperature processable ZnO semiconductor, allowing for BEOL integration of logic circuits and memory array. b Schematic illustrating the   
fabrication process flow of the ZnO TFT. c Photo image of the fabricated sample containing the ZnO TFTs, 1T1R memory array, inverter, and ring oscillator.

![](images/3a4ea3de655dadbe953d65e3ee59cc4ceef024055f87f6ef6dc3acf0349f35e3.jpg)  
a

![](images/3cd777f630b712e2313bd5ee585738d4ee1fa7469145f05107afc5ac01072889.jpg)  
b

![](images/c1eb2ba93d5eafdef642df82c36fba18501e6e8da4e401c020755f3eb9f35a56.jpg)  
C

![](images/7d3cba1e521d654ecf12d9d73a1acc589c55b763abe90141f6746be5b803dd9c.jpg)  
d

![](images/74cc0f2eb060658ee1820834084af49828ef02c7d70c4f0795b908366387be09.jpg)  
e

![](images/85aadbd5fe65aae1a14d403b510c8a7558e7de9c21cb9d3e0c7073e41374fb2f.jpg)  
f   
Fig. 2 | Material characterizations of ZnO channel layer. a SEM image of the ZnO TFT channel and cross-section schematic. b TEM image of the ZnO TFT stack, with the different layers labeled. c, d GI-XRD scan, and average crystallite sizes (with error bar) calculated from the Scherrer's formula, respectively, of the three   
different temperatures deposited ZnO films. e, f OIs XPS spectra of the ZnO channel layers deposited at three temperatures as indicated, and plot showing the Zn-O, $V_{O}$ , and -OH atomic percentages (with error bar) as a function of the three different temperatures used[12,17,49-51].

pseudo depletion design, is a popular design method, which applies two-stage structures to achieve full $V_{DD}$ swing at the output voltage $(V_{OUT})^{25,35-37}$ . However, these efforts are currently lacking, and systematic investigation is necessary for future implementation.

In this work, we report on a stable, high-performance ZnO TFT that exhibits one of the highest reported field-effect mobility $(\mu_{FE})$ of $85\mathrm{cm}^2 /\mathrm{V}\cdot \mathrm{s}$ using ALD process with performance stability exceeding 90 days in an unpackaged form. This was achieved with an optimized ALD deposition temperature $(200^{\circ}\mathrm{C})$ , and with a 5-nm-thick $\mathrm{HfO}_2$ passivation layer. Excellent electrical properties, including low positive threshold voltage $(V_{TH},0.72\mathrm{V})$ , negligible hysteresis $(< 50\mathrm{mV})$ , and low $D_{it}$ $(2.45\times 10^{11}\mathrm{eV}^{-1}\mathrm{cm}^{-2})$ , were also achieved. Through careful X-ray photoelectron spectroscopy (XPS) and X-ray diffraction (XRD) characterizations, we correlate the electrical properties of the ZnO TFT with the amount of $V_{O}$ concentration and crystallites size, elucidating such effects on the performance for possible future large-scale implementation. To demonstrate the ZnO TFT as a capable memory driver, we co-integrated it with $\mathrm{HfO}_2$ RRAM into a functional $32\times 32$ 1T1R array; this shows its suitability for BEOL integration in analog computing. In order to co-design for unipolar TFT-based circuits, we first presented on the compact modeling of our fabricated ZnO TFT, followed by the Pseudo-CMOS design methodology to capture and accommodate the material and device limitations; these were all achieved by cross-validation of simulation and experimental results. Process variation-aware simulation framework was then implemented to evaluate the performance and robustness of ZnO TFTs-based circuits. Experimentally, the pseudo enhancement load inverter (PEL), linear enhancement load inverter (LEL) and conventional depletion load inverter (DL) based on unipolar ZnO TFTs were fabricated and characterized[35,38]. To further explore the merits of high-mobility ZnO

TFTs at the circuit level, the 5-stage ring oscillators (ROs) based on these three different types of inverters were designed and demonstrated. The results from this work are expected to provide guidance for future implementation of ZnO TFT-based circuitries at BEOL.

# Results

# Fabrication of TFT and circuits

Staggered, bottom-gate ZnO TFTs were investigated in this work. The bottom-gate electrode composed of Ti/Pt (the thickness is $5/23\mathrm{nm}$ ) was first deposited by e-beam evaporation (EBE) onto a $285\mathrm{nm}$ $\mathrm{SiO}_2$ layer on Si substrate. Following, $10\mathrm{nm}$ thick $\mathrm{HfO}_2$ layer was deposited as gate dielectric by ALD with $\mathrm{H}_2\mathrm{O}$ as the oxygen source at $250^{\circ}\mathrm{C}$ . $15\mathrm{nm}$ thick ZnO active channel layer was then deposited by ALD at 3 different temperatures $-150/200/250^{\circ}\mathrm{C}$ . The effect of the deposition temperatures on the TFT performance is discussed later. Both the gate dielectric and ZnO channel regions were defined via standard lithography followed by a buffered oxide etch (BOE). Then, the source/ drain electrodes $(\mathrm{Ti} / \mathrm{Pt} - 5/23\mathrm{nm})$ were deposited using EBE followed by a lift-off process. After that, a $5\mathrm{nm}$ thick $\mathrm{HfO}_2$ layer was deposited by ALD to passivate the channel region. Finally, the $\mathrm{HfO}_2$ layer on the contact pads was removed using standard lithography, followed by a BOE etch for electrical measurements. In this work, ZnO TFTs with channel widths $(W_{CH})$ of $10\mu \mathrm{m}$ , and channel lengths $(L_{CH})$ of $2/5/10\mu \mathrm{m}$ were fabricated. The detailed fabrication process flow as described is illustrated in Fig. 1b. Details of the process parameters are provided in "Methods".

To demonstrate the use of ZnO TFT as a RRAM selector in a 1T1R array, a 1kbit $(32 \times 32)$ 1T1R array was designed. An additional $5\mathrm{nm}$ thick $\mathrm{HfO}_2$ was deposited as the switching layer by ALD at $250^{\circ}\mathrm{C}$ after source/drain electrode deposition of TFT, followed by Ti/Pt top

![](images/b0903c81b5e2d18f643977d37f93225feaa4bca197729f39af4e66a9688ca1b2.jpg)  
a

![](images/713a9049f9d3d4a5627ef32003ba03cd42f47b73b60409ffa697c70eb223d088.jpg)  
b

![](images/488bd980bfc22e2e089b585120c6c6b00393c86a00336e7f5ddebcb5f261027b.jpg)  
C

![](images/7293affb48f6e29c08e31e4923aa3bea03ef9f34186685e359f0552567eb0b73.jpg)  
d   
Fig. 3 | ZnO TFT electrical performance. a Transfer curves $(I_{D} \cdot V_{GS})$ of the ZnO TFTs fabricated at the three different temperatures with $W_{CH}$ and $L_{CH}$ of $10\mu \mathrm{m}$ and $5\mu \mathrm{m}$ , respectively. b TLM measurements of the TFT with three different $L_{CH}$ (2, 5, $10\mu \mathrm{m}$ ), with a maximum standard deviation of $7\%$ . The $R_{\text{Contact}}$ is extracted via the vertical intercept as shown in the linear line fit equation; the $2R_{\text{contact-specific}}$ when normalized to the $W_{CH}$ of $10\mu \mathrm{m}$ is then obtained as $0.99\mathrm{k}\Omega \mu \mathrm{m}$ . c $I_{D} \cdot V_{GS}$ family of   
curves (dual sweep) measured over different $V_{DS}$ (0.2-2 V). A high current on-off ratio up to $-10^{8}$ is obtained with SS of $110 \mathrm{mV} / \mathrm{dec}$ and hysteresis $< 52 \mathrm{mV}$ . d Output $(I_{D} \cdot V_{DS})$ family of curves (dual sweep) measured over different $V_{GS}$ (0-3.5 V) of the same TFT. The zoomed-in region of the plots in (c, d) (circled) are shown in the inset, respectively, indicating the small hysteresis measured of our fabricated TFT.

electrode deposition. The size of the RRAM was $5\mu \mathrm{m}\times 5\mu \mathrm{m}$ . In the array, ZnO TFT with the $W_{CH}$ and $L_{CH}$ of $10\mu \mathrm{m}$ and $5\mu \mathrm{m}$ , respectively, was used as the select transistor. The microscopic image of the 1T1R array together with a zoom-in image of one single 1T1R cell and the process flow is shown in Supplementary Fig. S1. To demonstrate the functionality of the ZnO TFTs-based inverters and ring oscillators, we demonstrate the designs of three different kinds of inverters, namely, PEL, LEL, and DL inverters and their respective ring oscillators. In the fabrication, the process flow was basically the same as the ZnO TFT, with only the additional step of via hole opening before top electrode deposition for overlapping bottom and top interconnects. Figure 1c shows the photo image of the fabricated sample containing the ZnO TFTs, logic circuits, and 1T1R memory array. Details of measurements and characterizations of the devices and circuits are provided in "Methods".

# Materials characterization

Detailed material characterizations for ZnO TFT have been performed to analyze and optimize the TFT performance. Figure 2a shows the ZnO TFT-stacked structure and scanning electron microscope (SEM) image of the channel region with width $(10\mu \mathrm{m})$ and length $(5\mu \mathrm{m})$ as labeled. The cross-sectional transmission electron microscope (TEM) image shown in Fig. 2b confirms the layers thicknesses and good interface quality between the different layers. The energy dispersive spectroscopy (EDS) mapping of Ti, Pt, Hf, and Zn elements taken from the channel material stack shows clear distinction of the different

layers (Supplementary Fig. S2). Atomic force microscope (AFM) images of the $\mathrm{HfO_2}$ dielectric and $\mathrm{ZnO}$ channel are shown in Supplementary Fig. S3. Small root-mean-square roughness $(R_{q})$ of the $\mathrm{HfO_2}$ gate insulator $(0.289\mathrm{nm})$ and the $\mathrm{ZnO}$ channel $(0.342\mathrm{nm})$ are obtained, indicating the high quality of all the deposited layers, beneficial for reduced carrier scattering.

To analyze the crystallinity and the preferred orientation, grazing incidence X-ray diffraction (GI-XRD) scans were obtained for the ZnO thin films deposited at the three different temperatures, as shown in Fig. 2c. The XRD patterns show that all the ZnO films are polycrystalline with a hexagonal wurtzite structure, with the peaks identified as (100), (002), (101), (102), (110), (103), (112) phases[39,40]. The XRD patterns of all three films exhibit the enhanced intensities for the peaks corresponding to (002) plane, indicating preferential orientation along the c axis[40,41]. The $150^{\circ}\mathrm{C}$ deposited ZnO film shows the preferable (002) orientation with additional (100) and (101) peaks. However, the (100) and (101) peaks weaken significantly, and the (002) peak dominates as the deposition temperature of ZnO films increases. This can be attributed to the low surface energy of (002) plane, which is the most thermodynamically favorable[40,42,43]. When the deposition temperature of film is high, Zn and O atoms can obtain sufficient energy to transfer themselves into energetically favorable positions, which results in ZnO thin films transiting to the (002) preferred orientation at high deposition temperature[44-46]. Figure 2d shows the average crystallite sizes of the three different ZnO thin films, which were calculated using Scherrer's formula. The crystallite size calculations are conducted

based on the different diffraction peaks measured, and by assuming that the crystallite size is the same in all directions (see Supplementary Note S1 for details). The largest average crystallite size of $5.14\mathrm{nm}$ is obtained of the $200^{\circ}\mathrm{C}$ deposited ZnO film, which is favorable for high mobility due to reduced grain-boundary scattering $^{47}$ .

The details of the oxygen defects in the ZnO thin films are elucidated from the XPS O1s spectra of all the ZnO films, shown in Fig. 2e. The O1s peaks were typically deconvoluted into three energy level subpeaks, including a lower binding energy peak centered at $\sim 530.1\mathrm{eV}$ (magenta) corresponding to the lattice oxygen or metal oxide (Zn-O), a higher binding energy peak centered at $\sim 532.1\mathrm{eV}$ (green) corresponding to the loosely bound oxygen like hydroxyl groups $(-OH)$ , and the medium binding energy peak centered at $\sim 530.95\mathrm{eV}$ (blue) attributed to non-lattice oxygen and associated with $V_{O}^{12,17,48-50}$ . The extracted at% of the Zn-O, $V_{O}$ , and $-OH$ bonds are shown in Fig. 2f. It can be seen that the $200^{\circ}\mathrm{C}$ deposited ZnO film contains the largest amount of $V_{O}$ , which helps to improve the carrier density for better drive current $^{17,49}$ . At the same time, it also contains the lowest impurity concentration $(-OH)$ , leading to superior electrical performance, as presented in the following section $^{50}$ .

# ZnO TFT electrical characterization

Figure 3a shows the transfer curves $(I_{D} \cdot V_{GS})$ of the ZnO TFTs fabricated at the three different temperatures with $W_{CH}$ and $L_{CH}$ of $10\mu \mathrm{m}$ and $5\mu \mathrm{m}$ , respectively. The current-voltage $(I - V)$ curves in Fig. 3 are all normalized to the $W_{CH}$ . The $150^{\circ}\mathrm{C}$ deposited ZnO TFT exhibits the lowest drive current, lowest $\mu_{FE}(3.63\mathrm{cm}^2 /\mathrm{V}\cdot \mathrm{s})$ , and largest $V_{TH}(2.5\mathrm{V})$ as compared to the TFTs fabricated at higher temperatures. This suggests the detrimental effect of higher trap states, which allows unstable stray charges entering or leaving the traps, resulting in reduced $\mu_{FE}$ and overly positive shift in the $V_{TH}^{40,45,51}$ . On the other hand, the ZnO TFTs deposited at $220^{\circ}\mathrm{C}$ shows the emergence of a small hump in the subthreshold region of the transfer curve (Supplementary Fig. S4), while a distinct hump phenomenon appears in the $250^{\circ}\mathrm{C}$ deposited ZnO TFT that is accompanied by a negative shift of $V_{TH}$ , observable in all devices fabricated at this temperature. This phenomenon has been examined in several works, and can be attributed to the existence of dual conduction channels, i.e., a main channel and a parasitic channel that turn on a different voltage as a result of unoptimized growth

conditions[52-55]. The $200^{\circ}\mathrm{C}$ deposited ZnO TFT shows the best overall performance with the highest drive current and a low positive $V_{TH}$ , and is further discussed. Figure 3c shows the normalized transfer curves $(I_{D} - V_{GS})$ for $V_{DS}$ from 0.2 to $2\mathrm{V}$ $(V_{DS}$ step size of $0.2\mathrm{V}$ ), with corresponding gate leakage current $(I_{G})$ less than $10^{-12}\mathrm{A} / \mu \mathrm{m}$ (limit of measurement setup), which indicating good quality of $\mathrm{HfO_2}$ gate insulator. Figure 3d shows the normalized output curves $(I_{D} - V_{DS})$ at $V_{GS}$ from 0 to $3.5\mathrm{V}$ $(V_{GS}$ step size of $0.5\mathrm{V}$ ). The dual sweep $I - V$ characteristics for both transfer and output curves show negligible hysteresis of $47\mathrm{mV}$ at $V_{GS} = 0.5\mathrm{V}$ , as shown in the insets of Fig. 3c, d. The hysteresis is extracted as follows: At a selected $V_{GS}$ in the transfer curve, the voltage difference between the forward and backward sweep was obtained. The extracted hysteresis as a function of $V_{GS}$ at $V_{DS}$ of $1\mathrm{V}$ as shown in Supplementary Fig. S5, with the definition of the hysteresis extraction shown graphically in the inset. The hysteresis values vary with different $V_{GS}$ , and a maximum hysteresis value of $52\mathrm{mV}$ is obtained near the saturation voltage of $4.2\mathrm{V}$ . The small hysteresis value of our TFT further suggests the good interface quality with low interface traps. A high drive current of $64\mu \mathrm{A} / \mu \mathrm{m}$ , with a large $I_{ON/OFF}$ ratio $>10^8$ was obtained. Furthermore, the fabricated ZnO TFTs show good uniformity, as can be seen from the transfer curves of 20 devices randomly selected across entire sample with minor standard deviations, as shown in Supplementary Fig. S6.

The contact resistance $(R_{\text{Contact}})$ is an unwanted parasitic in transistors, where it degrades drive current required for high-speed operation of IC chips. This is especially so at advanced technology node where the $R_{\text{Contact}}$ can form a significant portion of the entire TFT's resistance. Here, we extracted the $R_{\text{Contact}}$ of the ZnO TFT via the transfer length method (TLM), by utilizing the different channel length $(L_{\text{CH}})$ TFTs measured and plotting the TFTs' resistance vs. $L_{\text{CH}}$ (three different channel lengths are utilized here), as shown in Fig. 3b. A total $R_{\text{Contact}}$ of $9.902\mathrm{k}\Omega$ was extracted at the fitting line's vertical intercept point, translating to a specific contact resistance $R_{\text{Contact-specific}}$ of $0.99\mathrm{k}\Omega\mu\mathrm{m}$ when normalized to the TFTs' $W_{\text{CH}}$ of $10\mu\mathrm{m}$ . Further optimization of the $R_{\text{Contact}}$ value can be achieved though source/drain contact engineering, such as plasma treatment for effect Schottky barrier height tuning[56].

Here, we present on the extraction of both $\mu_{o}$ and $\mu_{FE}$ of the fabricated ZnO TFTs. $\mu_{o}$ is defined as the true mobility of the ZnO TFT in

Table 1 | Benchmark of reported ALD ZnO TFT performance parameters   

<table><tr><td>References</td><td>Year</td><td>Temp. (°C)</td><td>ZnO thickness (nm)</td><td>Oxide/thickness (nm)</td><td>ION/IOFF ratio</td><td>SS (mV/dec)</td><td>VTH(V)</td><td>μFE (cm2/V·s)</td></tr><tr><td>45</td><td>2019</td><td>200</td><td>33</td><td>SiO2/30</td><td>2.8 × 109</td><td>127</td><td>4.00</td><td>7.8</td></tr><tr><td>60</td><td>2019</td><td>200</td><td>15</td><td>ZrO2/5</td><td>-107</td><td>69</td><td>0.10</td><td>36.8</td></tr><tr><td>17</td><td>2019</td><td>100</td><td>16</td><td>Al2O3/36</td><td>-107</td><td>320</td><td>1.23</td><td>38.4</td></tr><tr><td>46</td><td>2020</td><td>300</td><td>36</td><td>[[HfO2]]/30</td><td>1.9 × 107</td><td>175</td><td>1.10</td><td>11.8</td></tr><tr><td>61</td><td>2020</td><td>200</td><td>33</td><td>Al2O3/60</td><td>4.1 × 109</td><td>131</td><td>3.24</td><td>19.6</td></tr><tr><td>62</td><td>2020</td><td>300</td><td>30</td><td>Al2O3/40</td><td>-107</td><td>220</td><td>6.00</td><td>16.2</td></tr><tr><td>49</td><td>2020</td><td>150</td><td>14</td><td>Al2O3/40</td><td>-108</td><td>210</td><td>0.14</td><td>31.1</td></tr><tr><td>18</td><td>2021</td><td>350</td><td>11</td><td>SiO2/90</td><td>5.0 × 109</td><td>/</td><td>18.70</td><td>43.2</td></tr><tr><td>63</td><td>2021</td><td>100</td><td>25</td><td>Al2O3/30</td><td>3.0 × 107</td><td>210</td><td>/</td><td>14.3</td></tr><tr><td>64</td><td>2021</td><td>100</td><td>16</td><td>Al2O3/36</td><td>-108</td><td>170</td><td>1.05</td><td>31.2</td></tr><tr><td>50</td><td>2022</td><td>100</td><td>23</td><td>Al2O3/36</td><td>-108</td><td>170</td><td>1.00</td><td>32.1</td></tr><tr><td>19</td><td>2022</td><td>100</td><td>15</td><td>HfO2/30 + Al2O3/10</td><td>-107</td><td>110</td><td>-3.00</td><td>55.5</td></tr><tr><td>65</td><td>2022</td><td>400</td><td>20</td><td>Al2O3/30</td><td>-1010</td><td>225</td><td>3.23</td><td>17.9</td></tr><tr><td>40</td><td>2022</td><td>150</td><td>20</td><td>Al2O3/50</td><td>2.0 × 107</td><td>250</td><td>1.41</td><td>10.7</td></tr><tr><td>20</td><td>2022</td><td>100</td><td>20</td><td>Al2O3/40</td><td>4.3 × 109</td><td>243</td><td>1.13</td><td>45.3</td></tr><tr><td>21</td><td>2022</td><td>300</td><td>3</td><td>Al2O3/5</td><td>-108</td><td>94</td><td>/</td><td>84.0</td></tr><tr><td>66</td><td>2023</td><td>200</td><td>17</td><td>Al2O3/15</td><td>-1012</td><td>75</td><td>/</td><td>32.8</td></tr><tr><td>22</td><td>2023</td><td>200</td><td>20</td><td>Al2O3/20</td><td>-109</td><td>179</td><td>2.73</td><td>43.8</td></tr><tr><td>This work</td><td>2023</td><td>200</td><td>15</td><td>HfO2/10</td><td>-108</td><td>110</td><td>0.72</td><td>85.0</td></tr></table>

![](images/7ed97cf8f0401fd7838a87d8faf1371fef847c669694a88ccbbe2eb5669c88bd.jpg)  
a

![](images/724852c42066b3abd899b477658efd731bd13da4f93e694a09edf45daf92bcfd.jpg)  
b

![](images/e5f2afdc313583d9255104f3887149e16820494f8dcbf7ec01171155de5d9d80.jpg)  
C

![](images/68eeb5749d31facfe29b9a483f9b0e8ccb4c1a40ed2715ae035e126f3d5a9ecc.jpg)  
d   
Fig. 4 | ZnO TFT modeling and simulation. a, b Extracted statistical characteristics of threshold voltage and mobility from 21 fabricated ZnO TFTs, with the Gaussian fit curves. c, d Excellent agreement between the simulation and   
experimental results for transfer curves and output curves, with an inset in the plot showing the behavior of a fit for just one curve (both log scale and linear scale).

the absence of $R_{\text{Contact}}$ , while $\mu_{FE}$ represents the effective mobility exhibit by the ZnO TFT in the presence of $R_{\text{Contact}}$ . Details of the mobility extraction method is shown in Supplementary Note S2. A maximum $\mu_{FE}$ of $85 \, \text{cm}^2/\text{V} \cdot \text{s}$ and $\mu_o$ of $140 \, \text{cm}^2/\text{V} \cdot \text{s}$ of the ZnO TFT is achieved for $L_{\text{CH}} = 5 \, \mu \text{m}$ . The fabricated ZnO TFT with $\text{HfO}_2$ passivation layer was also observed to be much more stable over time as compared to the un-passivated one. For the passivated one, time stability over 90 days with negligible degradation was achieved. However, the un-passivated ZnO TFT degraded significantly over time, and ceased to work after one month (Supplementary Fig. S7).

Table 1 highlights the merits of the ALD ZnO TFT in this work with similar recently reported devices, including $I_{ON} / I_{OFF}$ , subthreshold swing (SS), $V_{TH}$ and $\mu_{FE}$ . A low SS for fast switching, high $I_{ON} / I_{OFF}$ and positive $V_{TH}$ for low leakage current and low-power circuits, and high mobility for large drive current are desired. Especially, the mobility of the ZnO TFT is of particular importance as it determines the amount of driving power it can provide to drive either memory cells for emerging memory-centric computing or functional logic circuits. The optimized ZnO TFT studied in this work exhibits the highest $\mu_{FE}$ as compared to other reported ALD-deposited ZnO TFT, while exhibiting excellent performance all round.

# Modeling and simulation

In this section, we describe a SPICE-compatible model that is further developed to capture the unique DC characteristics of polycrystalline ZnO TFTs. The main equations to implement the model are shown in Supplementary Table 1. The features of the model are as highlighted: (1) For the above-threshold region, the gate-bias dependent field-effect mobility model has been proposed to account for the grain-boundary induced trap states properly, where the exponent factor $m$ in Eq. (3) (Supplementary Table S1) serves as the field enhancement fitting

parameter for the mobility. An empirical function is also introduced to enable the smooth transition between the linear and saturation region; (2) For the subthreshold region, the current is dominated by the diffusion branch since most of the induced charge is trapped by the deep acceptor states (for n-type devices), with the subthreshold ideality factor $\eta$ indicating the property of gain-boundaries $^{57}$ . Furthermore, the expression for the SS can be reduced as Eq. (6) (Supplementary Table S1), from which the density of states for the interface traps $(D_{it})$ can be obtained. From Eq. (6) in Supplementary Table S1, the SS of the TFT is proportionate to the temperature $(T)$ and $D_{it}$ , and inversely proportionate to the oxide capacitance $(C_{ox})$ . In our measurements, the $D_{it}$ can be directly inferred from the SS extracted from the transfer curves of the ZnO TFTs while possessing knowledge on the $C_{ox}$ . The interface property between the ZnO channel and $\mathrm{HfO}_2$ dielectric is crucial for the transistor operation. It has been well-established that the existence of $V_{O}$ at the interface should be treated as the origin of interface states $^{58,59}$ . Charge transfer will occur between the channel carriers and interface states, which leads to degraded transport and poorer electrostatic control over the channel. Therefore, low $D_{it}$ is highly desired to enable a transistor with enhancement mode, hysteresis-free, high mobility, and suppressed SS characteristics.

As in the case of IGZO oxide semiconductor, the depletion-mode FET with significant charge-carrier density in the channel at $V_{GS} = 0$ V is undesirable for applications, since a negative gate-to-source voltage is required to turn off the transistor. However, different from IGZO which is amorphous in nature, the ZnO film studied in this work is polycrystalline, supported by XRD characterization in Fig. 2c, d. This results in improved mobility due to suppressed carrier scattering, indicating the potential of ZnO. In addition, our well-controlled ALD deposition process of ZnO film eliminates the interface dipoles and trap states, which reduces the mobile charges present in the channel significantly.

A nearly charge-neutral $\mathrm{ZnO - HfO_2}$ interface can thus be obtained to enable the desirable enhancement-mode characteristics. The $V_{TH}$ and $\mu_{FE}$ are extracted out of 21 fabricated ZnO TFTs, which generally show a gaussian distribution as illustrated in Fig. 4a, b with the mean value and standard deviation values provided. Figure 4c, d shows the excellent agreement between the simulation and experimental results for the transfer and output curves, respectively, after the extracted $\mu_{FE}$ , $V_{TH}$ , and geometrical parameters are fed into the model. The inset in Fig. 4c shows the behavior of a fit for just one curve (both log scale and linear scale).

# Demonstration of ZnO TFT as memory driver in a 1T1R array

The low processing temperature and high $\mu_{FE}$ make the ZnO TFT suitable to be M3D integrated as a select transistor for driving RRAM in CMOS-BEOL process for memory-centric computing. In this section, we discuss on the analog states tuning functionality and repeatability of the 1T1R memory cell. In the 1T1R array, the gate of the ZnO TFT served as the word line, while the top electrode of the RRAM served as the bit line. The RRAMs were characterized separately first. Figure 5a shows the DC switching characteristics of a single RRAM over 150 cycles (current compliance was set as $1\mathrm{mA}$ ), showing a functional single RRAM device. Multiple RRAMs DC characteristics and the cumulative probability plot of high-resistance state (HRS) and low resistance state (LRS) distribution are shown in Supplementary Fig. S8, demonstrating good uniformity of the fabricated devices. Following, DC switching characteristic of a 1T1R memory cell (applied $V_{GS} = 3\mathrm{V}$ ) displays good repeatability and a first-order lower reset current (Fig. 5b). The lower reset current compared to single RRAM is attributed to the impedance and current limited by the ZnO TFT. In the 1T1R measurement, no current compliance was used, and repeatable performance was obtained, albeit with a comparatively larger reset voltage due to the potential drop across the ZnO TFT. Figure 5c shows the cumulative probability plot of $V_{SET}$ and $V_{RESET}$ distribution for the 1T1R memory cell measured over 35 memory cells. The median values of $V_{SET}$ and $V_{RESET}$ are $0.9\mathrm{V}$ and $-1.5\mathrm{V}$ , respectively.

# Simulation and experimental demonstration of ZnO TFT-based inverter

Based on the calibrated model, three types of inverter configurations, i.e., the pseudo enhancement load (PEL), linear enhancement load (LEL), and depletion load (DL), are evaluated to compare the sensitivity and tolerance of the ZnO gate-level circuit to the device variabilities. The circuit diagrams and corresponding optical images are shown in Fig. 6a-c. The designed inverters are demonstrated experimentally. The voltage transfer curves (VTCs) of the inverters are designed by optimizing the design parameters of the load component (i.e., $W_{MI}$ ) to ensure a better noise margin for each construct. The $W_{CH}$ and $L_{CH}$ of

load transistors (MI) are $3\mu \mathrm{m}$ and $5\mu \mathrm{m}$ in PEL and LEL inverters, while $500\mu \mathrm{m}$ and $5\mu \mathrm{m}$ in DL inverter. The $W_{CH}$ and $L_{CH}$ of other TFTs in inverters are $10\mu \mathrm{m}$ and $5\mu \mathrm{m}$ , respectively. Figure 6d-f shows the simulated and experimental measured VTCs of the PEL, LEL, DL inverters, with excellent agreement. For the PEL and LEL inverters, the applied $V_{DD}$ is $1.5\mathrm{V}$ , while $V_{Bias}$ varies from 1.5 to $3\mathrm{V}$ with step size of $0.5\mathrm{V}$ . For the DL inverter, the applied $V_{DD}$ varies from $1\mathrm{V}$ to $3\mathrm{V}$ with step of $0.5\mathrm{V}$ . The voltage gain and noise margin (NM) with $V_{DD}$ of $1.5\mathrm{V}$ of the three different inverters are shown in Supplementary Fig. S9. Of the three different kinds of inverters, the PEL inverters can realize rail-to-rail operation, i.e., switching from $V_{DD}$ to $V_{SS}$ with low-noise margin $(NM_{L})$ and high noise margin $(NM_{H})$ of $0.26\mathrm{V}$ and $0.65\mathrm{V}$ , respectively. The VTC has a positive shift with the fixed $V_{DD}$ with increasing $V_{Bias}$ due to the increasing $V_{IM}$ , leading to impedance reduction of $M_{UN}$ . While the DL inverter can also achieve rail-to-rail operation, the designed transistor has to be excessively large to ensure a sufficiently low pseudo-load impedance and is thus less desired. On the other hand, the LEL inverter while functional, cannot realize rail-to-rail operation due to the finite pseudo-load impedance of the pull-up transistor. Further VTCs of the PEL and LEL inverters with different $V_{DD}$ are shown in Supplementary Fig. S10, while the square pulse responses for these three different inverters with input frequency of $1\mathrm{kHz}$ are shown in Supplementary Fig. S11. We provide a benchmark table of various critical parameters of the three different inverters summarized in Supplementary Table S2. The designed PEL inverter is shown to be the most robust configuration due to the two-stage structure.

# Simulation and experimental demonstration of ZnO TFT-based ring oscillator

To further explore the merits of high-mobility ZnO TFTs at the circuit level, the 5-stage ring oscillators (ROs) based on these three different types of inverters were designed. The 5-stage ROs were verified experimentally; the optical images of the fabricated ROs are shown in Supplementary Fig. S12. Figure 7a, b shows the as-measured and simulated output waveforms of the PEL inverter-based ROs, respectively. The measured frequency of the PEL inverter-based RO is at $369.1\mathrm{kHz}$ , while the simulated frequency is at $385\mathrm{kHz}$ . The measured frequency of the LEL inverter-based RO is the highest at $558.2\mathrm{kHz}$ , and the DL inverter-based RO at $10.3\mathrm{kHz}$ (Supplementary Fig. S13). The three different ROs performances, including measured frequency, peak-to-peak voltage, working current, and calculated delay time per stage under different applied voltage pairs, are summarized in Supplementary Tables S3-S5.

The measured frequencies of the fabricated ROs are observed to be smaller than that of the simulations because of parasitic resistance and capacitance of the large contact pads, wires, and the measurement setup. The parasitic resistance of the fabricated ROs is assumed

![](images/86844f35f2f11ff893fa7b86d1a571c34462201c006fb5464ced9c1d8077de10.jpg)  
a

![](images/b6a765f5f736a91188ed89c1ffce099dd5206a7bd608a904e98645b8d6ac2570.jpg)  
b

![](images/1ce689d258c03c43532ff6e13fd1961403262f87ce0dacccbaa944c64ac1d10f.jpg)  
C   
Fig. 5 | 1T1R electrical performance. a DC characteristic of a single $\mathrm{HfO}_2$ RRAM over 150 switching cycles. The blue line shows the average switching curve. b DC characteristics of a 1T1R memory cell over ten switching cycles ( $V_{GS} = 3\mathrm{V}$ ). The   
magenta line shows the average switching curve. c Cumulative probability plot of $V_{SET}$ and $V_{RESET}$ distribution for the 1TIR memory cell measured over 35 memory cells. The median values of $V_{SET}$ and $V_{RESET}$ are $0.9\mathrm{V}$ and $-1.5\mathrm{V}$ , respectively.

![](images/86e00f68f27b066d98bd4b47bcb1e7fe38f787b53684100f22f5d3dccd36903e.jpg)

![](images/d901657bfb6ed3ede2b7dd19a48a7aab359ea589cc681708570a617bf799284a.jpg)

![](images/10feb6b379a7ddae8a6d0f0b6b2b33a4b2829fd25837232db3ac5f22d87a52a6.jpg)

![](images/45346e48b05932a34b10429061dc3973c68788082022b14e009a9969574ed544.jpg)

![](images/95e2206a7c71b8fa8c4ef41aeb666c2dc779486d4d8d75d81ee742c5d1ca2bcc.jpg)

![](images/47d2545efd5bb3c478d3a6f382cf33b5abaab085ca06265e6ab24e7790e9bbc9.jpg)  
Fig. 6 | Simulated and experimental voltage transfer curves (VTCs) of inverters. a-c Circuit diagrams and optical images of the PEL, LEL, and DL inverters. Simulation and experimental measurements of (d, e) VTC of PEL and LEL inverters, with $V_{DD}$ of $1.5\mathrm{V}$ and $V_{Bias}$ varying from 1.5 to $3\mathrm{V}$ and f VTC of DL inverter with $V_{DD}$ varying from 1 to $3\mathrm{V}$ .

![](images/64fba2a59fd6dd41f25db8659d8e9b9b022ac86bfaebb1b7b7b888bc201ae6c1.jpg)

![](images/e36452f84dd61dee41ed334a7c3ea37fcb3f4889282f093ee5b5b0527796ac93.jpg)

![](images/eb1c2074ed19590b5911ee3b7345bb8f5923c591f261340a1eb3ceca72f7cbc9.jpg)  
Fig. 7 | Simulations and experiments of PEL inverter-based ring oscillator. a, b The as-measured and simulated output waveforms for the 5-stage PEL inverter-based ring oscillator. c Projected frequency (simulated) versus parasitic capacitance of the RO circuits.

to be negligible due to the size of the wires designed. However, the parasitic capacitances are non-trivial and should be accounted for. The total capacitance of PEL inverter-based RO is estimated to be $\sim 150\mathrm{pF}$ , with details provided in the methods section. With the inclusion of the parasitic capacitance in simulation, both frequencies of the ROs from simulation and experiment are matched as expected. In actual circuit design, the parasitic capacitances are usually minimized without unnecessary large contact pads and are typically less than $0.1\mathrm{pF}$ . With a typical parasitic capacitance of $0.1\mathrm{pF}$ , the frequency of the RO can easily reach $10\mathrm{s}$ of MHz as projected using simulation, owing to the high mobility achieved of the proposed ZnO TFT. Figure 7c shows the simulated frequency versus parasitic capacitance, where the frequency can reach up to $44.85\mathrm{MHz}$ with parasitic capacitance of $0.1\mathrm{pF}$ . Hence, it is evident that the designed ROs can perform equally well as

compared to the simulated results; the oscillating frequencies of the ROs can be remarkably improved by reducing wiring areas and upgrading the measurement systems. Our results, spanning from device process optimization, device compact modeling, system integration, and circuits designs (both simulations and experiments), demonstrate the potential and suitability of ZnO TFT to be implemented as circuit-level devices in CMOS BEOL.

In summary, we have reported on a CMOS-BEOL-compatible, temperature optimized, low-temperature $(200^{\circ}\mathrm{C})$ fabricated ALD ZnO TFT with excellent $\mu_{FE} / \mu_{o}$ of $85 / 140~\mathrm{cm^2 / V\cdot s}$ high $I_{ON / OFF} > 10^8$ low SS of $110\mathrm{mV / dec}$ $D_{it}$ of $2.45\times 10^{11}\mathrm{eV}^{-1}\mathrm{cm}^{-2}$ and negligible hysteresis $<  50\mathrm{mV}$ . In order to co-design for future M3D architecture requiring BEOL integration, we have further evaluated the implementation of our ZnO TFT in 1T1R memory array as well as functional logic

circuits and ROs. These were achieved using both novel compact/ space modeling and experimental verification. We have shown that a PEL type inverter configuration provides the most robust performance with excellent noise margin. Finally, a 5-stage PEL inverter-based RO design can achieve a working frequency reaching $369.1\mathrm{kHz}$ , and projected to reach 10's of MHz in the absence of undesired parasitic capacitance as verified from both simulations and experiments. Hence, our results pave the way for potential implementation of ZnO TFT-based circuits in future M3D computing systems.

# Methods

# Device fabrication

The fabrication process started with the standard cleaning steps with the SC-1 and SC-2. The bottom-gate electrode composed of Ti/Pt (the thickness is $5/23\mathrm{nm}$ ) was first deposited by e-beam evaporation (EBE) onto a $285\mathrm{nmSiO}_2$ layer on a Si substrate. The evaporation vacuum value of EBE was less than 5E-6 torr. The deposition rates for Ti and Pt are $4\AA/\mathrm{s}$ and $2\AA/\mathrm{s}$ , respectively. Then the 100 cycles $\mathrm{HfO}_2$ layer (10-nm thick, measured by ellipsometer) was deposited as gate dielectric by ALD using tetrakis (ethylmethylamido) hafnium (TEMAH) as precursor and $\mathrm{H}_2\mathrm{O}$ as reactant at $250^{\circ}\mathrm{C}$ , while the 100 cycles $\mathrm{ZnO}$ active channel layer (15 nm thick) was deposited by ALD using diethylzinc (DEZ) as precursor and $\mathrm{H}_2\mathrm{O}$ as reactant at three different temperatures-150/200/250°C for process optimization. In $\mathrm{HfO}_2$ ALD process, the pulse time and purge time for TEMAH are 1.6 s and 10 s, while for $\mathrm{H}_2\mathrm{O}$ are 0.1 s and 10 s, respectively. The carrier gas flows for TEMAH and $\mathrm{H}_2\mathrm{O}$ are 80 sccm and 100 sccm, respectively. In $\mathrm{ZnO}$ ALD process, the pulse time and purge time for DEZ are 0.1 s and 4 s, while for $\mathrm{H}_2\mathrm{O}$ are 0.2 s and 4 s, respectively. The carrier gas flows for DEZ and $\mathrm{H}_2\mathrm{O}$ are 150 sccm and 200 sccm, respectively. The TEMAH source bottle is heated to $120^{\circ}\mathrm{C}$ , while DEZ source is kept at room temperature during the deposition process. Both the gate dielectric and $\mathrm{ZnO}$ channel regions were defined via standard lithography followed by a buffered oxide etch (BOE). The BOE etching rates for $\mathrm{HfO}_2$ and $\mathrm{ZnO}$ layers are about $0.1\mathrm{nm/s}$ and $2\mathrm{nm/s}$ through calibration, respectively. Then, the source/drain electrodes (Ti/Pt - 5/23 nm) were deposited using EBE followed by a lift-off process (same as a bottom gate). After that, a 5-nm-thick $\mathrm{HfO}_2$ layer was deposited using ALD to passivate the $\mathrm{ZnO}$ TFT, and the deposition recipe is the same as before. Finally, open pad was conducted through standard lithography followed by BOE etching. $\mathrm{ZnO}$ TFTs with channel widths $(W_{CH})$ of $10\mu\mathrm{m}$ , and channel lengths $(L_{CH})$ of $2/5/10\mu\mathrm{m}$ were fabricated. In the standard lithography process, AZ5214 photoresist and RZX3038 developer are used to pattern. AZ5214 does not attack the $\mathrm{ZnO}$ film and protects the $\mathrm{ZnO}$ channel region during the developing process. The developer contains TMAH, $2.38\%$ . As TMAH can attack $\mathrm{ZnO}$ film, during the source/drain photolithography process, we finely and accurately control the developing time to alleviate the damage to $\mathrm{ZnO}$ . When the developing time is $38\mathrm{s}$ , the photoresist can be completely removed, while maintaining negligible damage to the $\mathrm{ZnO}$ film.

# Characterization and measurement

All film thicknesses were measured by ellipsometer TF-UVISEL. Scanning electron microscope (SEM) observations were performed with Hitachi SU8320. Transmission electron microscope (TEM) observations were performed with Hitachi HT7700 Exalens operating at $120\mathrm{kV}$ . Cross-sectional TEM specimen was prepared by focused ion beam (FIB) using Helios NanoLab 600i apparatus. Atomic force microscope (AFM) observations were performed with Dimension Edge. X-ray diffraction (XRD) measurements were performed with Rigaku Smartlab. X-ray photoelectron spectroscopy (XPS) measurements were performed with Thermo Fisher Escalab $\mathrm{Xi}^{+}$ . Current-voltage $(I - V)$ characteristics of $\mathrm{ZnO}$ TFTs, capacitance-voltage $(C - V)$ of $\mathrm{HfO}_2$ dielectric MIM capacitors, RRAM and voltage transfer characteristics (VTCs) of all inverters were measured with an Keithley 4200-SCS

semiconductor parameter analyzer under room temperature and ambient conditions. In both the transfer curve and output curve measurement, the sweep rate was 14 points per second. The square pulses were generated by Tektronix AFG1022. The oscillation waveforms of the ring oscillator were measured by Tektronix TBS1102B.

# Device and circuit simulation

The calibrated SPICE-compatible model is further used for the circuit design and simulation with the Specter simulator. For the inverter simulation, the geometry parameters $\mathrm{R} = (W / L)_{\mathrm{load}} / (W / L)_{\mathrm{driver}}$ , as well as the additional bias voltage sources, are elaborately designed and simulated iteratively to optimize the characteristics of VTCs for different configurations (PEL, LEL, and DL), which serves as guidelines for fabrication and eventually agrees well with measured results. Subsequently, 5-stage well-optimized inverters are further cascaded to implement the ROs, with distributed parasitic capacitances from the wires ( $C_{\mathrm{wire}} - 6$ pF per stage for the PEL type, $\sim 30$ pF for 5 stages), oscilloscope ( $C_{\mathrm{oscilloscope}} - 20$ pF), and measurement systems ( $C_{\mathrm{meas}} - 102$ pF) are introduced as the load at the output of each corresponding stage.

# Data availability

All data are available from the corresponding authors upon reasonable request.

# References

1. Shulaker, M. M. et al. Three-dimensional integration of nano-technologies for computing and data storage on a single chip. Nature 547, 74-78 (2017).   
2. Huo, Q. et al. A computing-in-memory macro based on three-dimensional resistive random-access memory. Nat. Electron. 5, 469-477 (2022).   
3. Ning, H. et al. An in-memory computing architecture based on a duplex two-dimensional material structure for in situ machine learning. Nat. Nanotechnol. https://doi.org/10.1038/s41565-023-01343-0 (2023).   
4. Lin, Y. M., Appenzeller, J., Knoch, J. & Avouris, P. High-performance carbon nanotube field-effect transistor with tunable polarities. IEEE Trans. Nanotechnol. 4, 481-489 (2005).   
5. Allen, B. L., Kichambare, P. D. & Star, A. Carbon nanotube field-effect-transistor-based biosensors. Adv. Mater. 19, 1439-1451 (2007).   
6. Liu, Y., Wang, S., Liu, H. & Peng, L. M. Carbon nanotube-based three-dimensional monolithic optoelectronic integrated system. Nat. Commun. 8, 15649 (2017).   
7. Sivan, M. et al. All WSe(2) 1T1R resistive RAM cell for future monolithic 3D embedded memory integration. Nat. Commun. 10, 5201 (2019).   
8. Kim, S. et al. High-mobility and low-power thin-film transistors based on multilayer $\mathrm{MoS}_2$ crystals. Nat. Commun. 3, 1011 (2012).   
9. Wang, M. et al. Robust memristors based on layered two-dimensional materials. Nat. Electron. 1, 130-136 (2018).   
10. Tang, B. et al. Wafer-scale solution-processed 2D material analog resistive memory array for memory-based computing. Nat. Commun. 13, 3037 (2022).   
11. Shi, J. et al. Wide bandgap oxide semiconductors: from materials physics to optoelectronic devices. Adv. Mater. 33, e2006230 (2021).   
12. Lan, J. et al. Improved performance of HfxZnyO-based RRAM and its switching characteristics down to 4 K temperature. Adv. Electron. Mater. 9 https://doi.org/10.1002/aelm.202201250 (2023).   
13. Chiu, C. J., Chang, S. P. & Chang, S. J. High-performance a-IGZO thin-film transistor using $\mathrm{Ta}_{2}\mathrm{O}_{5}$ gate dielectric. IEEE Electron Device Lett. https://doi.org/10.1109/led.2010.2066951 (2010).

14. Sheng, J. et al. Amorphous IGZO TFT with high mobility of approximately 70 cm(2)/(V s) via vertical dimension control using PEALD. ACS Appl. Mater. Interfaces 11, 40300-40309 (2019).   
15. Samanta, S. et al. Low subthreshold swing and high mobility amorphous indium-gallium-zinc-oxide thin-film transistor with thin $\mathrm{HfO}_2$ gate dielectric and excellent uniformity. IEEE Electron Device Lett. 41, 856-859 (2020).   
16. Si, M., Charnas, A., Lin, Z. & Ye, P. D. Enhancement-mode atomic-layer-deposited $\mathrm{In}_2\mathrm{O}_3$ transistors with maximum drain current of 2.2 A/mm at drain voltage of 0.7 V by low-temperature annealing and stability in hydrogen environment. IEEE Trans. Electron Devices 68, 1075-1080 (2021).   
17. Chen, X. et al. Transparent and flexible thin-film transistors with high performance prepared at ultralow temperatures by atomic layer deposition. Adv. Electron. Mater. 5 https://doi.org/10.1002/aelm.201800583 (2019).   
18. Wang, M. et al. Performance optimization of atomic layer deposited ZnO thin-film transistors by vacuum annealing. IEEE Electron Device Lett. 42, 716-719 (2021).   
19. Li, Q. et al. Back-end-of-line compatible InSnO/ZnO heterojunction thin-film transistors with high mobility and excellent stability. IEEE Electron Device Lett. 43, 1251-1254 (2022).   
20. Li, S. et al. Micron channel length ZnO thin film transistors using bilayer electrodes. J. Colloid Interface Sci. 622, 769-779 (2022).   
21. Chand, U. et al. in 2022 IEEE Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits) 326-327 (IEEE, 2022).   
22. Zhao, W. et al. Enhanced stability performance of transparent ozone ALD ZnO thin-film transistors with $\mathrm{SiAlO_X}$ dielectric. IEEE Trans. Electron Devices 70, 556-562 (2023).   
23. Fortunato, E., Barquinha, P. & Martins, R. Oxide semiconductor thin-film transistors: a review of recent advances. Adv. Mater. 24, 2945-2986 (2012).   
24. Wang, Z., Nayak, P. K., Caraveo-Frescas, J. A. & Alshareef, H. N. Recent developments in p-type oxide semiconductor materials and devices. Adv. Mater. 28, 3831-3892 (2016).   
25. Lei, T., Shi, R., Wang, Y., Xia, Z. & Wong, M. A comparative study on inverters built with dual-gate thin-film transistors based on depletion- or enhancement-mode technologies. IEEE Trans. Electron Devices 69, 3186-3191 (2022).   
26. Yin, X. et al. Low leakage current vertical thin-film transistors with InSnO-stabilized ZnO channel. IEEE Electron Device Lett. 41, 248-251 (2020).   
27. Shih, C. W. & Chin, A. Remarkably high mobility thin-film transistor on flexible substrate by novel passivation material. Sci. Rep. 7, 1147 (2017).   
28. Hwang, C.-S. et al. Vertical channel ZnO thin-film transistors using an atomic layer deposition method. IEEE Electron Device Lett. 35, 360-362 (2014).   
29. Kong, Q. et al. First demonstration of BEOL-compatible 3D Fin-gate oxide semiconductor Fe-FETs. in 2022 International Electron Devices Meeting (IEDM) 12.13.11-12.13.14 (IEEE, 2022).   
30. Shi, R., Wang, S., Xia, Z., Lu, L. & Wong, M. Fluorinated metal-oxide thin-film transistors for circuit implementation on a flexible substrate. IEEE J. Flex. Electron. 1, 58-63 (2022).   
31. Rahaman, A., Chen, Y., Hasan, M. M. & Jang, J. A high performance operational amplifier using coplanar dual gate a-IGZO TFTs. IEEE J. Electron Devices Soc. 7, 655-661 (2019).   
32. Kim, J.-H., Oh, J., Park, K. & Kim, Y.-S. IGZO TFT gate driver circuit with large threshold voltage margin. Displays 53, 1-7 (2018).   
33. Biggs, J. et al. A natively flexible 32-bit Arm microprocessor. Nature 595, 532-536 (2021).   
34. Shang, Z.-W., Hsu, H.-H., Zheng, Z.-W. & Cheng, C.-H. Progress and challenges in p-type oxide-based thin film transistors. Nanotechnol. Rev. 8, 422-443 (2019).

35. Huang, T.-C. et al. Pseudo-CMOS: a design style for low-cost and robust flexible electronics. IEEE Trans. Electron Devices 58, 141-150 (2011).   
36. Kimura, M. et al. Pseudo-CMOS circuits using amorphous In-Sn-ZnO thin-film transistors. SID Symp. Dig. Tech. Pap. 45, 960-963 (2014).   
37. Zhao, W. et al. High-gain transparent inverters based on deuterated ZnO TFTs fabricated by atomic layer deposition. IEEE Electron Device Lett. 41, 1508-1511 (2020).   
38. Shao, L. L. et al. Compact modeling of carbon nanotube thin film transistors for flexible circuit design. in 2018 Design, Automation & Test in Europe Conference & Exhibition (DATE) 491-496 (IEEE, 2018).   
39. Mridha, S. & Basak, D. Effect of thickness on the structural, electrical and optical properties of ZnO films. Mater. Res. Bull. 42, 875-882 (2007).   
40. Yang, J. et al. Characteristics of ALD-ZnO thin film transistor using $\mathsf{H}_2\mathsf{O}$ and $\mathsf{H}_2\mathsf{O}_2$ as oxygen sources. Adv. Mater. Interfaces 9 https://doi.org/10.1002/admi.202101953 (2022).   
41. Caglar, Y., Caglar, M., Ilican, S., Aksoy, S. & Yakuphanoglu, F. Effect of channel thickness on the field effect mobility of ZnO-TFT fabricated by sol gel process. J. Alloy. Compd. 621, 189-193 (2015).   
42. Fujimura, N., Nishihara, T., Goto, S., Xu, J. & Ito, T. Control of preferred orientation for ZnOx films: control of self-texture. J. Cryst. Growth 130, 269-279 (1993).   
43. Yuan, N. Y. et al. The influence of deposition temperature on growth mode, optical and mechanical properties of ZnO films prepared by the ALD method. J. Cryst. Growth 366, 43-46 (2013).   
44. Pung, S. Y., Choy, K. L., Hou, X. & Shan, C. X. Preferential growth of ZnO thin films by the atomic layer deposition technique. Nanotechnology 19 https://doi.org/10.1088/0957-4484/19/43/435609 (2008).   
45. Li, H. et al. High-performance ZnO thin-film transistors prepared by atomic layer deposition. IEEE Trans. Electron Devices 66, 2965-2970 (2019).   
46. Che, B. et al. Temperature gradient ZnO deposited via ALD for high-performance transistor applications. IEEE J. Electron Devices Soc. 8, 885-889 (2020).   
47. Kim, H., Wang, Z., Hedhili, M. N., Wehbe, N. & Alshareef, H. N. Oxidant-dependent thermoelectric properties of undoped ZnO films by atomic layer deposition. Chem. Mater. 29, 2794-2802 (2017).   
48. Hsieh, P. T., Chen, Y. C., Kao, K. S. & Wang, C. M. Luminescence mechanism of ZnO thin film investigated by XPS measurement. Appl. Phys. A 90, 317-321 (2007).   
49. Chen, X., Wan, J., Wu, H. & Liu, C. ZnO bilayer thin film transistors using $\mathsf{H}_2\mathsf{O}$ and $\mathsf{O}_3$ as oxidants by atomic layer deposition. Acta Mater. 185, 204-210 (2020).   
50. Chen, X., Wan, J., Gao, J., Wu, H. & Liu, C. Enhanced negative bias illumination stability of ZnO thin film transistors by using a two-step oxidation method. IEEE Trans. Electron Devices 69, 2404-2408 (2022).   
51. Zhang, L., Li, J., Zhang, X. W., Jiang, X. Y. & Zhang, Z. L. High performance ZnO-thin-film transistor with $\mathrm{Ta_2O_5}$ dielectrics fabricated at room temperature. Appl. Phys. Lett. 95 https://doi.org/10.1063/1.3206917 (2009).   
52. Yang, J. et al. Investigation of a hump phenomenon in back-channel-etched amorphous In-Ga-Zn-O thin-film transistors under negative bias stress. IEEE Electron Device Lett. 38, 592-595 (2017).   
53. Kim, W.-S. et al. Abnormal behavior with hump characteristics in current stressed a-InGaZnO thin film transistors. Solid State Electron 137, 22-28 (2017).   
54. Teng, T., Hu, C.-F., Qu, X.-P. & Wang, M. Investigation of the anomalous hump phenomenon in amorphous InGaZnO thin-film transistors. Solid State Electron 170 https://doi.org/10.1016/j.sse.2020.107814 (2020).

55. Li, Q. et al. Structural engineering effects on hump characteristics of ZnO/InSnO heterojunction thin-film transistors. Nanomaterials 12 https://doi.org/10.3390/nano12071167 (2022).   
56. Lu, J. et al. Contact resistance reduction of low temperature atomic layer deposition ZnO thin film transistor using Ar plasma surface treatment. IEEE Electron Device Lett. 43, 890-893 (2022).   
57. Jacunski, M. D. et al. A short-channel DC SPICE model for polysilicon thin-film transistors including temperature effects. IEEE Trans. Electron Devices 46, 1146-1158 (1999).   
58. Pentcheva, R. & Pickett, W. E. Charge localization or itineracy at LaAlO3/SrTiO3 interfaces: hole polarons, oxygen vacancies, and mobile electrons. Phys. Rev. B 74 https://doi.org/10.1103/PhysRevB.74.035112 (2006).   
59. Park, J. et al. Oxygen-vacancy-induced orbital reconstruction of Ti ions at the interface of $\mathrm{LaAlO_3 / SrTiO_3}$ heterostructures: a resonant soft-X-ray scattering study. Phys. Rev. Lett. 110 https://doi.org/10. 1103/PhysRevLett.110.017401 (2013).   
60. Yang, J. et al. High-performance 1-V ZnO thin-film transistors with ultrathin, ALD-processed $\mathrm{ZrO}_2$ gate dielectric. IEEE Trans. Electron Devices 66, 3382-3386 (2019).   
61. Li, H. et al. Enhanced performance of atomic layer deposited thin-film transistors with high-quality $\mathrm{ZnO / Al_2O_3}$ Interface. IEEE Trans. Electron Devices 67, 518-523 (2020).   
62. Tang, Q., Chen, X., Wan, J., Wu, H. & Liu, C. Influence of Ga doping on electrical performance and stability of ZnO thin-film transistors prepared by atomic layer deposition. IEEE Trans. Electron Devices 67, 3129-3134 (2020).   
63. Dong, J. et al. High-performance ZnO thin-film transistors on flexible PET substrates with a maximum process temperature of $100^{\circ}\mathrm{C}$ . IEEE J. Electron Devices Soc. 9, 10-13 (2021).   
64. Chen, X., Wan, J., Wu, H. & Liu, C. Effective encapsulation of ZnO thin film transistors controlled by thermal energy. Appl. Surf. Sci. 548 https://doi.org/10.1016/j.apsusc.2021.149253 (2021).   
65. Zhao, W. et al. Improvement in instability of transparent ALD ZnO TFTs under negative bias illumination stress with SiO/AlO bilayer dielectric. IEEE J. Electron Devices Soc. 10, 927-932 (2022).   
66. Lin, Z., Wang, Z., Zhao, J., Li, X. & Si, M. A low-leakage zinc oxide transistor by atomic layer deposition. IEEE Electron Device Lett. 44, 536-539 (2023).

# Acknowledgements

This work was supported by the National Natural Science Foundation of China (Grant No. 62174074—Y.L., 62274081—L.L., 52273246—F.Z.), Shenzhen Fundamental Research Program (Grant No. JCYJ20220530115014032—Y.L., JCYJ20220530115204009—F.Z.), Young Innovative Talent Project Research Program (Grant No. 2021KQNCX077—F.Z.), Zhujiang Young Talent Program (Grant No. 2021QN02X362—Y.L.), Guangdong Provincial Department of Education Innovation Team Program (2021KCXTD012—Y.L.), Special Funds for the Cultivation of Guangdong College Students' Scientific and Technological Innovation (Grant pdjh2022b0455—W.W., pdjh2023c11507—J.L.),

SUSTech SME-Pixelcore [[Neuromorphic]] In-sensor Computing Joint Lab and Guangdong Provincial Engineering Research Center of 3-D Integration. We would also like to acknowledge the Core Research Facilities (CRF) at SUSTech for the facilities used, and the technical support provided by the staff and engineers at the CRF.

# Author contributions

Y.L., P.Z., and L.L. conceived the concept, and designed the experiments. W.W. and J.L. fabricated the devices. W.W., J.L., and M.S. performed electrical and material characterizations. P.Z. and K.L. performed the compact modeling and simulation. Y.L., P.Z., L.L., and W.W. analyzed the results and co-wrote the manuscript. Z.W., X.F., M.S., H.Y., K.C., J.L., and F.Z. contributed toward data analysis and revision of the manuscript.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-023-41868-5.

Correspondence and requests for materials should be addressed to Longyang Lin, Panpan Zhang or Yida Li.

Peer review information Nature Communications thanks Neri Alves, Tokiyoshi Matsuda and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. A peer review file is available.

Reprints and permissions information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2023