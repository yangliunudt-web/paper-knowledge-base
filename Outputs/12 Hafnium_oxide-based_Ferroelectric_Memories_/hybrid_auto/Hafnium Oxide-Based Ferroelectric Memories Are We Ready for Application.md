---
title: "Hafnium Oxide-Based Ferroelectric Memories: Are We Ready for Application"
date: "2021-01-01"
year: "2021"
journal: "IEEE VLSI-TSA"
abstract: "In this paper we discuss the current research status of ferroelectric memory solutions and reflect it with application requirements, showing potential of hafnium oxide based ferroelectrics for scaled non-volatile memory. In focus are mainly three promising emerging memory device technologies based on ferroelectric (FE) hafnium oxide: front-end of line (FEoL) implemented FeFET, and the two FE-capacitor based solutions FeRAM and 1T1C FeFET. These device technologies are discussed with respect to aspects like scaling opportunity, reliability, and maturity level, reflecting with current and future application requirements as well as conventional memory solutions."
abstract_cn: "本文讨论了HfO₂基铁电存储器的研究现状并与实际应用需求进行对比。综述聚焦于三类HfO₂基新型存储器技术：前道工序(FEoL)集成的FeFET，以及两种基于铁电电容的FeRAM和1T1C FeFET方案。从可扩展性、可靠性和成熟度等方面评估这些器件技术与当前及未来应用需求的匹配程度，并与传统存储器方案进行对比。"
cite: "[1] Seidel K, Lehninger D, Müller F, et al. Hafnium Oxide-Based Ferroelectric Memories: Are We Ready for Application?[C]. IEEE VLSI-TSA, 2021."
  - "[[FeFET]]"
  - "[[FeRAM]]"
  - "[[HfO2]]"
  - "[[1T1C]]"
  - "[[铁电存储器]]"
aiSum: "HfO2 铁电存储综述：器件物理、材料工程、集成挑战、商业部署评估。"
confidence: "high"
authors:
  - "Konrad Seidel"
  - "David Lehninger"
  - "Franz Müller"
  - "Yannick Raffel"
  - "Ayse Sünbül"
  - "Ricardo Revello"
  - "Raik Hoffmann"
  - "Sourav De"
  - "Thomas Kämpfe"
  - "Maximilian Lederer"
keywords:
  - "[[—ferroelectrics]]"
  - "[[non-volatile memory]]"
  - "[[FeFET]]"
  - "[[FeRAM]]"
wiki_concepts:
  - "[[FeFET]]"
  - "[[FeRAM]]"
---

# Hafnium oxide-based Ferroelectric Memories: Are we ready for Application?

Konrad Seidel, David Lehninger, Franz Müller, Yannick Raffel, Ayse Sünbül, Ricardo Revello, Raik Hoffmann, Sourav De, Thomas Kämpfe, and Maximilian Lederer

Fraunhofer IPMS, 01109 Dresden, Germany, e-mail konrad.seidel@ipms.fraunhofer.de

Abstract— In this paper we discuss the current research status of ferroelectric memory solutions and reflect it with application requirements. In focus are mainly three promising emerging memory device technologies based on ferroelectric (FE) hafnium oxide: front-end of line (FEoL) implemented FeFET, and the two FE-capacitor based solutions FeRAM and 1T1C FeFET. These device technologies are discussed with respect to aspects like scaling opportunity, reliability, and maturity level, reflecting with current and future application requirements as well as conventional memory solutions.

Keywords—ferroelectrics, non-volatile memory, FeFET, FeRAM

# I. INTRODUCTION

Ferroelectric memories based on perovskites are already known for many decades [1] and established as FRAM or FeRAM in several applications. This memory technology is an ideal choice for embedded or small capacity non-volatile memory (NVM) solutions in microcontrollers bringing along the advantage of low voltage operation, high reliability, and fast read and write speed. However, a wide range of applications also towards higher storage densities is limited because perovskites are not scalable due to the high dielectric constant and low coercive field. This results in thick FE films in the range of 50- 100 nm [2]. Thus, the possibility to shrink towards smaller technology nodes or even to take advantage of higher switched charges with 3D integration is missing. In addition, perovskite material integration and scaling is limited to the last BEoL layers due to the incompatibility of used materials in CMOS fabrication. The discovery of FE properties in confined hafnium oxide-based dielectrics [3] brought new momentum and options for further scaling and advanced CMOS integration. This is enabled by the usability of hafnium oxide together with dopants such as silicon or zirconium in the CMOS fabrication environment and by specific electrical properties such as a lower dielectric constant (~20) and higher coercive fields. Consequently, much thinner FE films in the range of about 5 to 10 nm are possible, switchable at about 2 to 4 V. It also results in reasonable switched charge density and 3D integration capability via atomic layer deposition (ALD). In the past decade research activities have brought up and demonstrated several device and integration concepts based on the newly discovered FE-films, like the front-end of line integrated ferroelectric FET (FeFET) which was co-integrated with low cost adder into existing CMOS front-end of line (FEoL) technology (Fig. 1) and has been demonstrated as scaled Mbit FeFET array capacity [4].

For FEoL process conditions, mainly the alloy hafnium silicon oxide (HSO) has proven good switching characteristics and thermal stability.

Revival and potential of FE storage device solutions based on hafnium oxide also for the back-end of line (BEoL) implementation were demonstrated for the FRAM concept [5, 6] and the gate coupled 1T1C FeFET or FeMFET [7, 8] solution which is applying mainly hafnium zirconium oxide (HZO) allowing crystallization with good FE properties at low thermal budget [9, 10]. In such BEoL implementation scalable metalferroelectric-metal (MFM) capacitors as storage elements offer good conditions for enhanced reliability.

This paper intends to summarize the research status and key parameters of the potential hafnium oxide based NVM concepts FeFET, FRAM, and FeMFET and reflects it with application requirements.

# II. SCALABILITY & VARIABILITY

Fig. 2 illustrates the microstructure, the crystallographic phase, and the grain size of HSO films embedded in MFIS structures and HZO films in MFM configuration. HSO films with bottom SiO2 interface (MFIS configuration) form dendritic grains with an average equivalent diameter of ~230 nm during the thermal treatment. In contrast, HZO films embedded between two TiN electrodes (MFM configuration) form much smaller grains of ~30 nm and columnar shape under identical annealing conditions. In both configurations, the majority of the grains crystallizes in the orthorhombic (ferroelectric) phase, as visualized by the blue (MFIS) and green color (MFM) of the respective TKD image. This results in different scaling opportunities for the different FE device concepts.

While the FEoL FeFET is particularly amenable to cointegration, the formation of current percolation paths (Fig. 3), forming in the transistor channel due to direct coupling of local polarization reversal must be given special consideration in cell design [11]. This offers tuning possibilities, while making scaling more challenging. As discussed earlier, the MFIS-stack configuration suffers from typically larger grain sizes. This is different for the FeMFET concept, where smaller grains are observed for MFM stack-configuration and the topic of current percolation paths is avoided due to the lower floating metal layer [14]. However, good scalability of FEoL FeFET was demonstrated in 28nm technology [4]. With the discussed smaller grain sizes for HZO even better scalability and MFM stacking capability is expected for BEoL concepts. Thin dielectric film of FE layer allow controlled aspect ratio (AR) of MFM stack patterning and thus low variability. Enhancement of sensing margin by increased switched charge also for scaled FRAM solutions can be achieved with 3D MFM capacitor integration [15]. Here, 3D MFM scalability for thin and high AR holes is achievable by demonstrated ALD processes with good step coverage. Since FeMFET concept is not based on switched charge, MFM cells can be optimized to smallest area and according to capacitance ratio between MFM and FET [16].

# III. ENDURANCE

Asymmetric stack parameters in MFIS FeFET lead to challenges in managing the electrostatic conditions between FE layer and the dielectric of the interfacial layer mainly causing higher field and also stress across interfacial layer (IL). This stress on the IL is detracting among other factors the endurance

behavior. Higher permittivity by IL nitridation [17] lowers the FE switching voltage by shifting field distribution from interface to FE layer. In addition, the reduced stress on IL results in significant improvement stable memory window (MW) to beyond 1e5 write cycles which is shown in Fig. 4(a). However, further engineering of electrostatics and trapping behavior in the stack is required for enhanced endurance beyond 1e6 cycles. Here, potential approach is additional fluourination of the interfacial layer [19].

More Symmetric stack configuration and no interfacial layer give good endurance opportunities for the MFM-based memory devices even for larger MFM areas, as shown in Fig. 5. Since FRAM concept implies destructive read operation with the need for a write back after each read operation relatively high cycling endurance levels beyond 1e12 cycles are required. Recent research projected demonstrated FRAM endurance levels in the range of 1e11 [5]. Reaching higher levels in near future can be expected. This combined target read/write endurance has to be evaluated for the different memory applications so that even higher generic endurance levels are specified for FRAM. The FeMFET concept does not require write back operation so that

endurance degradation is only driven by write operation. Further, the MFM cells in FeMFET can be optimized towards smaller area according to FET/MFM voltage divider so that high write endurance levels >1e10 cycles can be expected. The independent device area tuning between MFM and FET allows good control of the particular device stress level and hence optimized reliability behavior.

# IV. RETENTION

For FeFET devices retention behavior is influenced by depolarization field and trapping behavior of the FE layer [18, 21]. As shown in Fig. 4(b), depolarization field and socalled backswitching can be reduced by discussed interfacial layer with higher dielectric constant, such as SiN instead of SiO2. This electrostatic optimization also mitigates (de)trapping mechanisms which can be reduced by additional FE stack engineering. These measures carry potential for reaching 10 years retention targets with FeFET technology.

MFM-based stacks conceptionally do not suffer from depolarization effects. However, electrode and stack optimization is required in order to avoid trapping and degradation effects. Retention tests on MFM capacitors shown in Fig. 6 project a temperature-independent stable retention up to 10 years lifetime. This confirms good retention behavior for FRAM applicaton. For FeMFET memory concept, the underlying MFM cell concepts suggests similar performance. However, controlling the parasitic effects such as avoiding charge trapping of the floeating node between gate and MFM might be required.

# V. COSTS & COMPATIBILITY

Compared to other NVM technologies general FE-based memory implementation carries along relatively low cost for fabrication. This is mainly because of following reasons:

Compatibility for fabricating hafnium oxide-based FEmaterial in standard CMOS fabrication environment

When accessing existing NVM applications with FE memory technology it is of importance to consider different aspects of compatibility with existing solution and application space:

As application risks for FE memories can be considered specific functional or reliability effects, like wakeup and imprint behavior. Wakeup behavior is an intrinsic effect that describes an initial weak FE switching which has to be activated by several initialization cycles. This effect can be mitigated by interface and FE-stack engineering but needs to be considered in product testing phase. Especially in low thermal budget integration, like BEoL, careful consideration of FE crystallization has to be given. Imprint behavior describes the property of FE films to pin previously stored polarization which is accelerated by temperature stress. Again, FE stack optimization and understanding of underlying physical behavior help to mitigate such effects which can be identified by specific monitoring tests.

Besides existing applications for embedded but also standalone NVM solutions FE memories based on hafnium oxide can be utilized for analogue compute-in-memory architecures (CiM) [23] that have potential for high computing performance at low power consumption. Besides CiM, various computing architectures are in discussion. This is enabled firstly by the possibility to embed FE memory devices in computing architectures due low voltage operatability. Secondly, the analog switchability demonstrated for a FeMFET memory cell in Fig. 7 allows high computing efficiency.

# VI. SUMMARY & CONCLUSION

Table 1 summarizes and compares relevant properties of FE device concepts with conventional and other emerging memory technologies. We have shown based on analysis of different aspects that NVM solutions of FE hafnium oxide show good potential for future application. This is supported by scalability and performance parameters like switching speed and power consumption. Market readiness mainly depends on reliability requirements, cost as well as user-driven boundary conditions for particular applications. Based on present progress and physical understanding further research could enable such FE memory concepts even for automotive and space applications. Good analogue switching properties make FE devices suitable canditates for future in-memory computing architectures.

# ACKNOWLEDGMENT

This work has received funding from the ECSEL Joint Undertaking (JU) project StorAIge and ANDANTE under grant agreement No 101007321 and 783127, respectively. The JU receives support from the European Union’s Horizon 2020 research and innovation programme and France, Belgium, Czech Republic, Germany, Italy, Sweden, Switzerland, Turkey.

# REFERENCES
