---
title: "Monolithic 3D Integration of High Endurance Multi-Bit Ferroelectric FET for Accelerating Compute-In-Memory"
authors:
  - "S. Dutta"
  - "H. Ye"
  - "W. Chakraborty"
  - "Y.-C. Luo"
  - "M. San Jose"
  - "B. Grisafe"
  - "A. Khanna"
  - "I. Lightcap"
  - "S. Shinde"
  - "S. Yu"
  - "S. Datta"
date: "2024-01-01"
year: "2024"
journal: "Nature Electronics"
abstract: "We demonstrate, for the first time, monolithic 3D (M3D) integration of back-end-of-line (BEOL) compatible Hf0.5Zr0.5O2 (HZO) ferroelectric FET (FeFET) with front-endof-line (FEOL) high-k/metal gate (HKMG) Si-NMOS. We use low thermal budget $( { < } 4 0 0 ^ { 0 } \\mathrm { C } )$ processing to integrate HZO with 1% Tungsten (W)-doped amorphous In2O3 (IWO) semiconducting oxide channel and demonstrate high remnant polarization charge density $2 P _ { R , }$ of $4 0 \\mu C / c m ^ { 2 }$ with reliable switching characteristics. We report (a) read memory window of 0.45V in ultra-scaled 20nm channel length IWO FeFET, (b) write speed of 100ns, and (c) write endurance ${ > } 1 0 ^ { 8 }$ cycle. We further demonstrate a 2bit/cell synaptic weight cell with well separated conductance states. System-level analysis of compute-in-memory (CIM) accelerators for performing inference on CIFAR-10 image dataset using VGG-8 model shows that 22nm BEOL FeFET achieves 3× higher energyefficiency than 7nm SRAM while occupying a smaller memory array area due to area folding enabled by M3D architecture."
keywords:
  - "[[FeFET]]"
  - "[[In-memory computing]]"
  - "[[3D NAND]]"
  - "[[Monolithic 3D integration]]"
cite: "[1] Dutta et al. Monolithic 3D Integration of High Endurance Multi-Bit Ferroelectric FET for Accelerating Compute-In-Memory[J]. Nature Electronics, 2024."
aiSum: "We demonstrate, for the first time, monolithic 3D (M3D) integration of back-end-of-line (BEOL) compatible Hf0.5Zr0.5O2 (HZO) ferroelectric FET (FeFET) with front-endof-line (FEOL) high-k/metal gate (H..."
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
  - "[[In-memory computing]]"
---

# Monolithic 3D Integration of High Endurance Multi-Bit Ferroelectric FET for Accelerating Compute-In-Memory

S. Dutta1* , H. Ye1* , W. Chakraborty1 , Y.-C. Luo2 , M. San Jose1 , B. Grisafe1 , A. Khanna1 , I. Lightcap1 , S. Shinde1 , S. Yu2 and S. Datta1

1 University of Notre Dame, Notre Dame, IN 46556, USA; 2 Georgia Institute of Technology, Atlanta, GA, USA

*Equal contribution; Email: sdutta4@nd.edu

Abstract: We demonstrate, for the first time, monolithic 3D (M3D) integration of back-end-of-line (BEOL) compatible Hf0.5Zr0.5O2 (HZO) ferroelectric FET (FeFET) with front-endof-line (FEOL) high-k/metal gate (HKMG) Si-NMOS. We use low thermal budget $( { < } 4 0 0 ^ { 0 } \mathrm { C } )$ processing to integrate HZO with 1% Tungsten (W)-doped amorphous In2O3 (IWO) semiconducting oxide channel and demonstrate high remnant polarization charge density $2 P _ { R , }$ of $4 0 \mu C / c m ^ { 2 }$ with reliable switching characteristics. We report (a) read memory window of 0.45V in ultra-scaled 20nm channel length IWO FeFET, (b) write speed of 100ns, and (c) write endurance ${ > } 1 0 ^ { 8 }$ cycle. We further demonstrate a 2bit/cell synaptic weight cell with well separated conductance states. System-level analysis of compute-in-memory (CIM) accelerators for performing inference on CIFAR-10 image dataset using VGG-8 model shows that 22nm BEOL FeFET achieves 3× higher energyefficiency than 7nm SRAM while occupying a smaller memory array area due to area folding enabled by M3D architecture.

# I. Introduction

Billions of connected edge devices produce zettabytes of data per year that need to be transformed into actionable information. This has created an unprecedented demand for data-centric computing. With on-chip memory limited by SRAM size, there is an extraordinary volume of data traffic between processor and off-chip memory that adds to energy and latency. Compute-in-memory (CIM) is a promising approach to overcome memory bottleneck where compute is moved closer to the data residing in the memory. Embedded non-volatile memory (eNVM) technologies such as FeFET [1], RRAM [2] and STT-MRAM [3] are candidates for storing the weight matrix on-chip and for performing vector-matrixmultiplication (VMM) in-situ to accelerate deep neural network (DNN) inference. Conventional CIM architecture colocates eNVM and access transistors in the FEOL along with CMOS logic and periphery like MUX, analog-to-digital converter (ADC) in the FEOL. M3D CIM architecture targets placement of the memory array in the BEOL with CMOS periphery under the array (CUA) (Fig. 1(a)). Such M3D CIM accelerator provides significant area, energy and latency advantage [4]. Here, we demonstrate a BEOL compatible FeFET that is monolithically integrated on top of FEOL silicon NMOS to realize high-density 3D synaptic array (Fig. 1(b)). While 1T-1RRAM and 1T-1MRAM require large FEOL access transistors resulting in $3 0 { - } 6 0 \mathrm { F } ^ { 2 }$ bit cell area [2-3], M3D 1T-1FeFET bit cell occupies only $1 5 \mathrm { F } ^ { 2 }$ , providing a huge density advantage. Additionally, the low write and read energy of BEOL FeFET provides an energy-efficiency benefit when compared to SRAM and other eNVM technologies (Fig. 1(c)). In this work, we demonstrate BEOL compatible low thermal

budget processing and integration of HZO with amorphous oxide semiconductor (AOS) channel. IWO is preferred as the AOS channel material for FeFET owing to its high field-effect electron-mobility [5,6] under low thermal budget processing compared to poly-Si, absence of unwanted low-k interfacial layer formed between the Si interface and the HZO. Recently HZO has been integrated with BEOL compatible IGZO channel [7], however, IWO offers better improved $\mathrm { V } _ { \mathrm { T } }$ stability due to higher oxygen-bond dissociation energy of W that acts as both stabilizer and electron donor [8]. We experimentally demonstrate 2bit/cell synaptic characteristics of IWO FeFET with well separated conductance states and scalability down to 20nm for providing performance boost for CIM accelerators.

# II. Fabrication Process

The key fabrication steps for monolithic integration of BEOL FeFET with FEOL Si-NMOS are shown in Fig. 2(a). FEOL Si-NMOS fabrication comprises source/drain (S/D) ion implantation, junction activation, thermal ALD of 5nm HfO2 followed by 20nm thick W deposition as patterned gate metal. 100nm thick PECVD SiO2 is deposited to serve as interlayer dielectric (ILD). Following via pattern and etch, Ti/Al contact metallization and anneal completes the FEOL process. BEOL processing of FeFET starts with patterned W back gate formation and plasma enhanced ALD (PEALD) of 10nm thick HZO at $2 5 0 ^ { 0 } \mathrm { C } .$ For strain-induced stabilization of ferroelectric orthorhombic phase in HZO, W sacrificial capping layer (SCL) is sputter-deposited followed by 3500 C anneal for 300s in N2 and subsequent W removal. Next, 1% by weight W-doped amorphous In2O3 (IWO) channel of 3nm thickness was sputtered in the presence of 0.02Pa excess $\mathrm { O } _ { 2 }$ at room temperature, followed by liftoff. 30 nm thick Pd was patterned as S/D electrodes, followed by a $1 5 0 ^ { 0 } \mathrm { C }$ N2 anneal for contact resistance improvement. Next, 5nm thick HfO2 was deposited using thermal ALD as top-gate dielectric at $1 2 0 ^ { 0 } \mathrm { C } _ { ; }$ , followed by patterning Pd top electrode. The top gate ensures effective application of electric field across HZO compared to floatingbody scenario [7]. Fig. 2(b) shows the top view false-colored SEM image of the FEOL Si-NMOS and the BEOL HZO FeFET. Cross-sectional STEM of the highlighted region is shown in Fig. 2(c) showing the fully processed 2-tier M3D integrated structure. Fig. 2(d) shows the STEM image and EDS elemental mapping of the 500nm LG FEOL Si-NMOS. Similar STEM image and EDS elemental mapping of the 20nm LG BEOL FeFET is shown in Fig. 2(e). The impact of the 3D stacking and the associated process temperature on the bottom Si-NMOS is characterized by comparing the ID-VG characteristics pre and post 3D integration (Fig.2(f)) showing matched transfer characteristics.

# III. Low Thermal Budget Processing of HZO

Conventional processing of Zr-doped ferroelectric HfO2 involves crystallization anneal with thermal budget larger than

5000 C. Here, we report on optimization of BEOL compatible low thermal budget processing of HZO. Large area (80!%´80!%) W/HZO/W metal-ferroelectric-metal (MFM) capacitors were fabricated using plasma ALD, followed by annealing at various temperatures ranging from 3000 C to 4000 C and different anneal durations of 30s and 300s. Fig. 3(a) shows the remnant polarization (PR) measured using DC sweep P-E loop measurements for various anneal conditions. While lower thermal budget leads to lowering of $\mathrm { P _ { R } , }$ higher ferroelectricity with $\mathrm { P _ { R } } { = } 2 0 \mu C / c m ^ { 2 }$ is still achievable at 3500 C with 300s anneal which is comparable with our baseline process of $5 0 0 \mathrm { { } ^ { 0 } C }$ anneal for 30s. Fig. 3(b) shows representative P-E loops measured for 3500 C anneal for 30s and 300s and compared with the baseline 5000 C 30s anneal. We also analyzed the evolution of the ferroelectric orthorhombic phase for low thermal budget processing by performing Grazing-Incidence $\mathrm { X } { \mathrm { - R a y } }$ Diffraction (GI-XRD) as shown in Fig. 3(c). The appearance of o(111) peak around $3 0 . 5 ^ { 0 }$ and o(200) peak around $3 5 . 5 ^ { 0 }$ confirms stabilized ferroelectric phase in BEOL compatible HZO. We measured the switching speed of the MFM capacitor using squared-shaped program and erase pulses. Fig. 3(d) shows excellent switching capability with partial polarization switching occurring within 50ns - suitable for multi-bit weight cell. The low thermal budget MFM capacitors showed ${ \mathrm { > } } 1 0 ^ { 7 }$ endurance cycle and retention ${ > } 1 0 ^ { 3 }$ seconds, similar to that of baseline processing as shown in Fig. 3(e) and (f), respectively.

# IV. Low Thermal Budget Processing of IWO FeFET

To enable BEOL compatible FeFET, we integrate HZO with IWO as AOS channel material. Fig. 4(a) highlights a key fabrication step of introducing an additional W SCL during annealing to stabilize ferroelectricity in HZO. This is confirmed by P-E loop measurements performed on 80!%×80!% W/HZO/IWO/W capacitors exhibiting higher PR with SCL compared to that without SCL (Fig. 4(b)). The switching speed of the two samples with and without SCL is shown in Fig. 4(c, d) showing partial polarization switching within 50ns in the integrated structure with SCL.

# V. Characterization of IWO FeFET

We characterize the weight cell operation of IWO FeFET using pulsed ID-VG and single pulse program and erase measurements on a long channel $\operatorname { ( L G = 1 } \mu \mathrm { m ) }$ device. For all measurements, gate voltage was applied to the bottom gate while the top gate was kept grounded to ensure effective application of electric field across HZO [7]. Fig. 5(a) shows a large memory window (MW) of 1.2V measured from pulsed ID-VG using a wide VG sweep from -2V to +5V. We also measured a MW of 0.45V using a single program and erase pulse of ±5V and 100!s (Fig. 5(b)). Similar measurements are reported in Fig. 6(a, b) for ultra-scaled FeFET of LG=20nm showing MW of 0.45V and 0.2V measured using pulsed ID-VG measurement with -2V to +5V VG sweep and using program/erase pulse of ±5V and 100!s. The dependence of the MW on the program pulse amplitude and pulse width is shown in Fig. 7(a). Fast write speed of 100ns is achieved while maintaining a MW of 0.3V. Note that the write speed of the fabricated IWO FeFET is limited by the parasitic capacitances

and with optimized device structure sub-10ns switching is possible. High endurance $( > 1 0 ^ { 8 }$ cycle) of the IWO FeFET with 3-orders of magnitude improvement over conventional Si-FeFET [1] is shown in Fig. 7(b) which can be attributed to the absence of low-k interfacial layer between IWO channel and HZO ferroelectric. A memory retention ${ > } 1 0 ^ { 3 }$ seconds is shown in Fig. 7(c). We demonstrate the multi-bit program capability of IWO FeFET using partial polarization switching. Fig. 8(a, b) shows four tightly distributed distinct ID levels (corresponding to 2bit per cell) achieved by tuning the programming pulses. For writing bits ‘00’, ‘01’, ‘10’ and ‘11’, program/erase pulses of -5V, +3V, +4V and +5V were applied with pulse widths of 1!s. The distribution in ID due to cycleto-cycle variation was measured for 100 program/erase cycles.

# VI. BEOL FeFET CIM Accelerator Benchmark

We benchmark the BEOL IWO FeFET with SRAM and other eNVM devices (FEOL FeFET[1], 2-bit RRAM [2], STT-MRAM[3]) for 8-bit inferencing VGG-8 model on CIFAR-10 dataset using DNN+NeuroSim framework [9] (Fig. 9(a)), which is a widely used benchmark simulator developed for evaluating the CIM accelerators that include all the necessary peripheral logic. We developed the cell structure of the 1T-1BEOL FeFET in a pseudo-crossbar array (Fig. 9(b, c)) to realize key operations such as VMM. The FEOL 1T serves as selection transistor to avoid disturb in the write operations in pseudo-crossbar array [10]. Thanks to the small current needed to write/read BEOL FeFET, a compact BEOL FeFET cell area of $1 5 \mathrm { F } ^ { 2 }$ assuming minimum W/L. On the other hand, 1T1R cell area is generally in the range of $3 0 \mathrm { F } ^ { 2 } – 6 0 \mathrm { F } ^ { 2 }$ due to RRAM/STT-MRAM’s large write current. The SRAM based accelerators are evaluated at both 7nm and 22nm node, and the other eNVM based accelerators were evaluated at 22nm node. Fig. 9(d) summarizes the benchmarking results. BEOL FeFET CIM array occupies smallest memory array area due to minimum size FEOL access transistor under the BEOL FeFET in M3D. BEOL FeFET also achieves more than 3× improvement in energy-efficiency than 7nm SRAM due to the large RON (4(Ω) of BEOL FeFET limiting the read dynamic energy.

# VII. Conclusion

We demonstrated monolithic 3D integration of BEOL compatible FeFET with FEOL Si-NMOS. We show low thermal budget $( { < } 4 0 0 ^ { 0 } \mathrm { C } )$ processing and integration of HZO with W doped In2O3 amorphous oxide semiconductor. We report 0.45V memory window in 20nm channel length IWO FeFET with fast write speed of 100ns, ${ > } 1 0 ^ { 8 }$ cycle write endurance and ${ > } 1 0 ^ { 3 }$ seconds memory retention. We also demonstrate 2bit/cell synaptic weight cell that provides 3× improvement in energy-efficiency than 7nm SRAM and density advantage due to compact cell area of 15F2 when benchmarked against other eNVM technologies for CIM accelerators.

# References

[1] K. Ni, et al, IEDM 2018. [2] P. Jain, et al, ISSCC 2019. [3] Y. Kim et al, VLSI 2011. [4] S. Datta et al, IEEE Micro 2019. [5] K. Nomura et al, Nature 2004. [6] W. Chakraborty, et al, VLSI 2020. [7] F. Mo et al, VLSI 2019. [8] H. Li. et al, EDL 2013. [9] X. Peng et al, IEDM 2019. [10] K. Ni. et al, EDL 2018.   
Acknowledgements:This work was supported by ASCENT, one of six centres in JUMP, sponsored by DARPA and the Semiconductor Research Corporation (SRC), and IMPACT center in nCORE, sponsored by SRC.

# Motivation:AcceleratingCompute-In-Memorywith BEOLCompatibleMulti-BitpercellFeFET

![](images/fa55108e99b0a00472aaff955bb6cf14173b85b88e8f798df1074a2305b0b1fe.jpg)

![](images/04be50ccfd00c31915639d8f57e133c32baa4439f7f3fb5cd1ecc316830ee9c7.jpg)

![](images/4f9875ee36ecd2c14166016bc7fa97d4df6ebebb52655379b67e728b6722385e.jpg)

![](images/d08822226612384fe09fecb3e1f1f8082416846880fdb42a1d3d98176fc17aab.jpg)  
Fig.1(a)ComparedtooventionalCarchitecturemonoithic3D3D)Cprovidesareaenergandlatencyadvantagebyplacinghigh densityembededn-volatilmemorinOLitperipralCOunderearrayCUA))SchematicofMDFeFElthicaly integratedontoofFEOLSiNtoaliegensityDsynapticaray(c)EstimatedareaandefincydvantageofF

# Monolithic3DIntegrationofBEOLIWOFeFETwithFEOLSi-NMOS

![](images/02f6fe44ecff1ca3da1ea62fc372f4bfed1a873013df51673ccfaa630983055a.jpg)

![](images/41e012f67a2f00e91cd31868b93e06360c17884dfc46418aca7b52c479dc1c88.jpg)

![](images/88cd2834814fc086790738ee2bbfe188979258f25c3847c42d6f1da06fec84f2.jpg)  
Fig.2(a)KeyfabricationstepsinM3DintegrationofBEOLFFETontopofFEOLSi-NMOShighlightinglowthermalbudget.(b)Towview false-coloredSEMoftheM3Dintegratedstructure.(c)STEMshowingcross-sectionoffulyprocessed2-tierM3Dintegratedstructure withBEOLFeFET(topdevicelayer)andFEOLSi-NMSbotomdevicelayer).(d，e)STEMandEDSelementalmapof50nmLFEOL Si-NMOS and 20nm $\mathsf { L } _ { \mathsf { G } }$ BEOL FeFET,respectively. (f) Measured $\mathsf { I } _ { \mathsf { D } } \mathsf { - } \mathsf { V } _ { \mathsf { G } }$ of FEOL Si-NMOS pre and post 3D stacking showing matched transfercharacteristics.Thepost3DstackingSi-OScharacteristicswasmeasuredaftersubjectingtofulBEOLprocessingofFFET.

# BEOL CompatibleLowThermal BudgetProcessing of Ferroelectric Hfo.5Zro.5O2

![](images/93f1fe043e64c3172a8ce3a711d79c26c559f540ec4eeab65c06c8adb711a670.jpg)

![](images/a8d76aac08697e08e8b2b7ed25f16639830b7e6a1d365903068d476d3537a864.jpg)

![](images/d72da880918fbc7af9f8079c57491547caef8d31e8538a634a5fb4f158132cae.jpg)

![](images/9599c2cc8d3380b3efe83fb924e0ea2f4ba72ced6e465d1ae914510cfed1b51f.jpg)

![](images/52b4c02df302c706c169ef4d335f86e308ac44066fa358245b92ff5f1e578906.jpg)

![](images/14455e35170b2b3878fd70835060f5291927baf8a6c5b2dfb8ca9ff7e7b807dd.jpg)

![](images/e26659015de925dc861bf5d38a234c160670df82e746dcaa7e8dd2c8998f6960.jpg)  
Fig.3(a)Measuredpoarzationand(b)P-Eloopsin8Oμmx8Oumcapacitorsforlowtemperatureannealconditions.(c）GIXRDshowsthe appearanceoffrroelectrictoombicpaeforlowthealbdgetprocessing.dMeasuredswiingspdfor5030sanealsowing partiaporzatiositingitinns.(e)Endurancece>nd(figretentiomeasuedfo5scompardtoaseis.

![](images/6886f9324111db8c65fc13a859320021aaec0b8112ec68002e010ee45676418f.jpg)  
LowThermalBudgetIntegrationofFeroelectricHf.Z5OwithAmorphousOxideSemconductor(dium-Tungsten-Oxide)

![](images/97bd740eb2518964bc6d54e58bf14d552256308b9d581f9eb46ccab372be6f82.jpg)

![](images/8afa3c394d2bedb5363e4f70930ab99b19084322e116224b41b5a48c301821f9.jpg)

![](images/5651e284f3966688032d2208f6b855b390d1a6dfaadac480cdc647ea8ccf2a53.jpg)  
Fig.4(a)HZOisanealedusing Wsacrificialcappinglayer (SCL)tostablizehgherpercentageoforthorhombicphase.(b)MeasuredP-E loop in 80μmx80μm capacitors showing higher $\mathsf { P } _ { \mathsf { R } }$ with SCL. (c,d) Switching speed measured in two structures.

![](images/3a31b6274e36ed68c351713fb12e48487222f4308f1e2f076083a0a04ed83b87.jpg)  
CharacterizationofIWOFeFET

![](images/671d8716f4906aeabf9e5cc84334aa34d572ca4851ed2ec38d39f79f684b8415.jpg)  
Fig. 5(a) Measured pulsed $\mathsf { I } _ { \mathsf { D } } { \mathsf { - } } \mathsf { V } _ { \mathsf { G } }$ of FeFET for-2V to $+ 5 \mathsf { V V } _ { \mathsf { G } }$ sweep showing largeMW of1.2V.(b)Measured $\mathsf { I } _ { \mathsf { D } } { \mathsf { - } } \mathsf { V } _ { \mathsf { G } }$ using a single program and erase pulse of ±5V,100us showing 0.45V MW.

![](images/8a48a74802d0ad74ed38fd5d3f428f71b6d855f2d0eb42472ff862a3066f19a6.jpg)  
Demonstrationof UItra-Scaled20nmLGIWOFeFET

![](images/616c762ff2dacdf3da45faee41c4174c189e82cacd9a2f79afe55613b49a39e0.jpg)  
Fig.6(a) Measured pulsed $\mathsf { I } _ { \mathsf { D } } \mathsf { - } \mathsf { V } _ { \mathsf { G } }$ of ultra-scaled FeFET of Lg=20nm for-2V $\mathfrak { t o } + 5 \vee \vee \mathfrak { s }$ sweep showing MW of 0.45V. (b) Using a single program and erase pulse of $\pm 5 \mathsf { V } , 1 0 0 \mu \mathsf { s } ,$ ,MW of 0.2V was obtained.

![](images/f493f0b81a712dc473bc37a52d9f01ea0c658bd964e119e8b78364aefc31cb8f.jpg)  
Speed,EnduranceandRetentionofIWOFeFET

![](images/71cba22500c9fc0def2a1cd8306f465d38ef3967d75869a4edce8d4ad0b41294.jpg)

![](images/5d5b55bdf5907156ba17a51acc479f7742de8a2fd09eac4e657a4338b2b1e4bc.jpg)  
Fig. 7(a) Dependence of MW on program pulse amplitude and pulse width highlighting the switching speed of FeFET.Write operation with ±5V,1μs is achieved.(b） High endurance $\tt { > } 1 0 ^ { 8 }$ cycles and (c) high retention with no degradation in memory window measured in IWO FeFET at 25C.

![](images/3bfe80c265a7ef56609dd7c7692951b5c5d992fa2b9217393533d9dd7b6ef1b3.jpg)  
Multi-BitFeFETSynapticWeightCell   
Fig.8(a) Demonstration of multi-bit program capability of iWO FeFET.4 tightly distributed distinct $1 0$ levelsachieved using different programming schemes,(b) Distribution of well separated 4 conductancesmeasured for100 cycles.

![](images/94c80a8763765bddb19f811b003d6904ba513cedb3644c8fa97167ef525ee1df.jpg)  
Compute-ln-MemoryBenchmarking

![](images/0bc6113abf66fd40bbc8719d94d89bebf08e68e52b9ffb204f32edc13da6293a.jpg)

![](images/133dd9c1f5a19672b6d313e6148d73ed4c577378512250b98b2c539635adec8f.jpg)  
Fig.9(a)Webenchmark M3D BEOLFeFET with SRAM,RRAM,STT-MRAMand conventional FeFET for8-bit inferencing VGG-8 modelon CIFAR-10 dataset using DNN+NeuroSim framework.(b,c) Schematicof cellstructureof 1T-1BEOL FeFETinapseudo-crossbararray.(d)Benchmarking resultsshow BEOLFeFETproviding highestdensitydue to15F²cell areaand more than 3×improvement in energy-effciency than 7nm SRAMdue to reduced read dynamic energy.

<table><tr><td>(d)</td><td>Device</td><td>SRAM</td><td>SRAM</td><td>RRAM (Intel)</td><td>STT-MRAM (Samsung)</td><td>Conv. FeFET (Global Foundry)</td><td>BEOL FeFET (Notre Dame)</td></tr><tr><td>Technology node (LSTP)</td><td>7nm</td><td colspan="6">22nm</td></tr><tr><td>Bit/Cell</td><td>1</td><td>1</td><td>2</td><td>1</td><td>2</td><td>2</td><td>2</td></tr><tr><td>Ron (Ω)</td><td colspan="2">/</td><td>6k</td><td>14k</td><td>67k</td><td>4M</td><td></td></tr><tr><td>On/Off Ratio</td><td colspan="2">/</td><td>17</td><td>2</td><td>100</td><td>4</td><td></td></tr><tr><td>Cell Area (F2)</td><td>600</td><td>200</td><td>60</td><td>30</td><td>26</td><td>15</td><td></td></tr><tr><td>Inference Accuracy</td><td colspan="7">91%</td></tr><tr><td>L-by-L Dynamic Energy (μJ)</td><td>46.28</td><td>75.65</td><td>47.5</td><td>93.9</td><td>21.3</td><td>17.2</td><td></td></tr><tr><td>Energy Efficiency (TOPS/W)</td><td>25.4</td><td>15.77</td><td>25.80</td><td>13.04</td><td>57.49</td><td>71.04</td><td></td></tr><tr><td>Throughput (FPS)</td><td>771.96</td><td>607.25</td><td>792.35</td><td>617.83</td><td>1059.90</td><td>1066.25</td><td></td></tr><tr><td>ADC Read Dynamic Energy (μJ)</td><td>39.83</td><td>52.17</td><td>34.91</td><td>71.63</td><td>10.45</td><td>6.47</td><td></td></tr><tr><td>CIM array on chip (%)</td><td>29.17</td><td>20.06</td><td>5.81</td><td>3.67</td><td>3.57</td><td>2.15</td><td></td></tr><tr><td>Single CIM array Area (μm2)</td><td>481.69</td><td>1585.97</td><td>475.791</td><td>237.896</td><td>206.176</td><td>118.948</td><td></td></tr></table>

Subarray size=128*128; SAR ADC precision=5 bits.   
F=7nm or 22nm for normalizing cellarea, doesn't indicate physical feature size.