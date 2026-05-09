---
title: "A Monolithic Ferroelectric-Ionic Duality for Stochastic-Neuromorphic Core Integration"
authors:
  - "Changhyeon Han"
  - "Ryun-Han Koo"
  - "Minsuk Song"
  - "Youngchan Cho"
  - "Min Wook Kang"
  - "Jangsaeng Kim"
  - "Jong-Ho Lee"
  - "Wonjun Shin"
  - "Daewoong Kwon"
date: "2026-01-01"
year: "2026"
journal: "Advanced Materials"
doi: "10.1002/adma.2026xxxxx"
abstract: "Learning under uncertainty has become increasingly critical in data‑intensive"
abstract_cn: "在数据密集型人工智能应用中，不确定性下的学习变得日益关键，需要能够统一确定性和概率性功能的计算系统。结合稳定存储和可调随机性的硬件对此类系统至关重要，但由于精确存储保持与可控随机变异之间的内在冲突，在微型架构中实现这种集成仍然极具挑战性。本文展示了一种基于铪基的铁电‑离子双重性，可在单一器件中集成随机编码和突触记忆。通过精心设计铁电界面以重新利用氧空位（传统上被视为降低铪基铁电可靠性的缺陷），我们将这些空位用作动态调制器件行为的功能性离子组分。由此产生的铁电‑离子双模切换引入了电压可调随机性，并在单一器件架构中增强了突触行为。重要的是，这种铁电‑离子双重性表现出完全的互补金属氧化物半导体兼容性和向超大规模集成的可扩展性，这得益于基于晶圆级原子层沉积的铪生长。这些结果确立了一种新的器件范式，将存储、随机性和学习能力统一在单一铁电平台中。"
keywords:
  - "[[hafnia ferroelectrics]]"
  - "[[oxygen vacancy]]"
  - "[[neuromorphic computing]]"
  - "[[stochastic computing]]"
  - "[[low-frequency noise]]"
cite: "[1] Han C, Koo R‑H, Song M, et al. A monolithic ferroelectric‑ionic duality"
aiSum: "提出铪基铁电‑离子双重性器件，利用氧空位作为功能性离子组分实现电压可调随机性和突触行为增强，在单一器件中集成随机编码与突触记忆，具备 CMOS 兼容性和"
confidence: "high"
wiki_concepts:
  - "[[Neuromorphic computing]]"
---

# RESEARCH ARTICLE

# A Monolithic Ferroelectric-Ionic Duality for Stochastic-Neuromorphic Core Integration

Changhyeon Han1 Ryun-Han Koo2 Minsuk Song1 Youngchan Cho3 Min Wook Kang4 Jangsaeng Kim5 Jong-Ho Lee2 Wonjun Shin3 Daewoong Kwon1

1 Department of Electrical Engineering, Hanyang University, Seoul, Republic of Korea 2Department of Electrical and Computer Engineering and Inter-university Semiconductor Research Center, Seoul National University, Seoul, Republic of Korea 3Department of Semiconductor Convergence Engineering, Sungkyunkwan University, Suwon, Republic of Korea 4School of Electronic and Electrical Engineering, Sungkyunkwan University, Suwon, Republic of Korea 5Department of Electronic Engineering, Sogang University, Seoul, Republic of Korea
  - "[[Neuromorphic computing]]"

Correspondence: Wonjun Shin (swj0107@skku.edu) Daewoong Kwon (dw79kwon@hanyang.ac.kr)

Received: 5 September 2025 Revised: 26 November 2025 Accepted: 17 December 2025

Keywords: hafnia ferroelectrics | oxygen vacancy | neuromorphic computing | stochastic computing | low-frequency noise

# ABSTRACT

Learning under uncertainty has become increasingly critical in data-intensive artificial intelligence applications, requiring computing systems that unify deterministic and probabilistic functions. Hardware that combines stable memory with tunable stochasticity is essential for such systems, but achieving this integration within a miniaturized architecture remains significantly challenging due to intrinsic conflicts between precise memory retention and controllable stochastic variability. Here we demonstrate a hafnia-based ferroelectric-ionic duality that integrates stochastic encoding and synaptic memory within a single device. By deliberately engineering the ferroelectric interface to repurpose oxygen vacancies—traditionally regarded as defects that degrade reliability in hafnia ferroelectrics—we exploit these vacancies as functional ionic components that dynamically modulate device behavior. The resulting ferroelectric-ionic dual-mode switching introduces voltage-tunable stochasticity and enhances synaptic behavior within a single device architecture. Crucially, this ferroelectric-ionic duality exhibits full complementary metaloxide-semiconductor (CMOS) compatibility and scalability to very-large scale integration (VLSI) system, enabled by wafer-scale atomic layer deposition-based growth of hafnia. These results establish a novel device paradigm that unifies memory, randomness, and learning capabilities within a single ferroelectric platform.

# 1 Introduction

The explosive growth of artificial intelligence (AI) and dataintensive computing is rapidly increasing global energy consumption, pushing conventional semiconductor technologies toward their physical and energetic limits. Addressing this emerging energy crisis demands a fundamental shift toward computing architectures inspired by biological brains, which excel at parallel processing of information with remarkable energy efficiency.

Neuromorphic computing paradigms aim to replicate these biological features by leveraging analog synaptic functions to achieve highly energy-efficient information processing and adaptive learning capabilities [1–4]. However, neuromorphic systems alone are insufficient for handling the growing complexity and unpredictability inherent in modern AI applications. As AI technologies increasingly permeate complex and uncertain environments, efficiently managing and learning from uncertaintyrich data becomes essential. Probabilistic computing, which

Changhyeon Han, Ryun-Han Koo, and Minsuk Song contributed equally to this work.

© 2026 Wiley-VCH GmbH

inherently incorporates stochasticity, has emerged as a crucial methodology for robust inference and decision-making under ambiguous or incomplete information. Ideally, future computing platforms should seamlessly combine deterministic synaptic memory and intrinsic stochastic behavior within a single device architecture, enabling direct and energy-efficient probabilistic inference.

To realize such multifunctional hardware, the materials employed need to be carefully engineered to simultaneously provide deterministic analog memory states and tunable stochastic characteristics. However, integrating these dual functionalities at the nanoscale remains challenging, primarily due to inherent conflicts between precise analog memory retention, device reproducibility, and the controlled introduction of stochastic variability. Moreover, for practical deployment in large-scale AI systems, it is essential that these materials are fully compatible with complementary metal-oxide-semiconductor (CMOS) fabrication processes and scalable to very-large-scale integration (VLSI). Although several candidate materials— including 2D van der Waals (vdW) materials, perovskite oxides, and organic semiconductors [5–14]—have been explored, each exhibits fundamental limitations that hinder simultaneous achievement of analog programmability, stochastic tunability, CMOS compatibility, and VLSI scalability [15–19]. Thus, a fundamentally new approach is required, employing materials uniquely capable of addressing these comprehensive demands.

In this study, we propose a monolithic hafnia-based ferroelectricionic duality field-effect transistor (FIDFET) that integrates stochastic encoding and neuromorphic functionalities at the nanoscale, while ensuring compatibility with wafer-scale integration to address these challenges fundamentally. The core of our approach lies in deliberately engineering the ionic component, oxygen vacancies $\mathbf { ( V _ { 0 } s ) }$ , traditionally viewed as detrimental defects in hafnia-based ferroelectric materials. We propose that the coexistence and coupling of ferroelectric and ionic enabled by ${ \mathrm { V } } _ { 0 } { \mathrm { s } }$ can be intentionally harnessed as new design knobs. By precisely controlling $\mathrm { v _ { o } }$ dynamics alongside intrinsic ferroelectric polarization switching, a dual-functional computing element that provides both enhanced deterministic synaptic behavior and tunable stochastic characteristics is achieved. Furthermore, the proposed hafnia-based ferroelectric device leverages waferscale atomic layer deposition (ALD), ensuring compatibility with CMOS processes and scalability to VLSI systems, thus representing a practical and transformative approach for future AI hardware.

# 2 Results and Discussion

# 2.1 Device Structure of FIDFET

We introduce a novel interface-engineered device structure: an HZO-TiO -integrated ferroelectric field-effect transistor (FeFET) referred to as a FIDFET. This structure is systematically compared with a control FeFET incorporating a conventional gate stack without the TiO oxygen-absorbing interlayer. Both devices with $\mathrm { S i O } _ { 2 } / \mathrm { H Z O }$ and $\mathrm { S i O } _ { 2 } / \mathrm { T i O } _ { 2 } / \mathrm { H Z O }$ gate stacks were fabricated on silicon-on-insulator (SOI) substrates via a gate-first process, based on a 6-inch wafer-scale CMOS-compatible process, with

potential scalability to 8- and 12-inch platforms (Figure 1A; Figure S1, Supporting Information). HZO was adopted as the ferroelectric layer owing to its CMOS compatibility and scalable ferroelectricity (Note S1, Supporting Information). Figure 1B shows the simplified schematic of the fabricated devices. The elemental composition of the gate stacks was confirmed through energy-dispersive X-ray spectroscopy (Figure S2 and Methods, Supporting Information).

To verify the ferroelectric-switching characteristics of the HZO layer, atomic-scale imaging was conducted using integrated differential phase contrast (iDPC) scanning TEM (STEM) (Figure 1C). The observed periodic lattice fringes correspond to the polar orthorhombic phase (Pbc2 ), which is responsible for the ferroelectric behavior. The enlarged image highlights the atomic columns of Hf(Zr) and $^ { \mathrm { ~ O ~ } , }$ where the asymmetric displacement of oxygen atoms along the vertical direction indicates polarization [20, 21]. To further verify the crystallinity of the HZO layer, grazing-incidence X-ray diffraction (GIXRD) and fast Fourier transform (FFT) analyses were also performed, both of which confirmed the presence of the orthorhombic phase in HZO (Figure S3 and Note S2, Supporting Information).

To verify the ion-switching components, we conducted analytical experiments with a focus on the role of ${ \mathrm { V } } _ { 0 } { \bf s } ,$ , which are known to be critical defects in hafnia-based ferroelectrics (Note S3, Supporting Information) [22, 23]. These analyses were performed using electron energy loss spectroscopy (EELS) and X-ray photoelectron spectroscopy (XPS) to examine the distribution and behavior of ${ \mathrm { V } } _ { 0 } { \mathrm { s } }$ in the gate stacks (Notes S4 and S5, Supporting Information). In the $\mathrm { T i O } _ { 2 }$ -inserted FIDFET, EELS analysis reveals a reduced ${ p _ { 1 } / p _ { 2 } }$ intensity ratio near the ${ \mathrm { H Z O / I L } } ,$ indicating an increase in local $\mathrm { v _ { o } }$ concentration (Figure $\mathrm { 1 D ; }$ Figures S4 and S5, Supporting Information) [24]. XPS depth profiling further supports this result, showing a higher $\mathrm { v _ { o } }$ and sub-oxide concentration throughout the HZO layer in the FIDFET compared to the control FeFET (Figure S6, Supporting Information). These observations collectively imply that $\mathrm { T i O } _ { 2 }$ acts as an oxygenscavenging interlayer, facilitating directional oxygen migration and modifying the interfacial defect landscape. Building on the demonstrated ferroelectric-ionic coexistence, we focus on codesigning device operation and system-level architectures that exploit dual-mode switching by harnessing fast dipole reorientation for analog memory and tunable vacancy-induced defect dynamics for stochastic encoding (Figure 1E). Detailed analysis of the $\mathrm { T i O } _ { 2 }$ interlayer selection and thickness optimization is provided in supporting information (Figure S7, Note S6 and S7, Supporting Information).

# 2.2 Hybrid Ferroelectric-Ionic Switching

Figure 2 shows the switching behaviors of the fabricated FeFET and FIDFET. In the case of FeFET, typical ferroelectric hysteresis behavior is observed. As the program voltage $\left( V _ { \mathrm { P G M } } \right)$ increases from 3 V to $4 \ \mathrm { V } ,$ the memory window (MW) expands due to the enhanced switching of ferroelectric domains, ferroelectric switching program (FE-PGM) (Figure 2A). However, at 5 V, the MW begins to shrink, accompanied by a sharp rise in gate current $\left( { { I _ { \mathrm { G } } } } \right)$ at the $\mathrm { S i O } _ { 2 } / \mathrm { H Z O }$ interface, which screens the internal field and suppresses further polarization switching (Figure 2B). In

![](images/29c38759aa48d5c38157c635942115880edaa2761e6f3058a2b1a6ca5b8407c3.jpg)  
A

![](images/991cf428cf8a148a300e33548635edfd398db96761ae90a0cfa9611bf540ed6a.jpg)

![](images/aa08beaa2f10187cb6e9be9d32b51515be43cf9862e687a33300dbaa0025e1c7.jpg)

![](images/f8ab795044653dab140c605c8ca548041f9ad66e3cdc807d0ea76f042277111e.jpg)  
C

![](images/ebf68d0001cce1390b3df27f5d93aa4bf6fea8ba2c2cce1ee93e0e5dae05eef6.jpg)  
B   
D

![](images/f3b96a2711d8721a4ccf358eef29d2eb4906b5831577923bf120d862bed4e1c9.jpg)

![](images/f343fe81eb3f755741da9112b5edf3ff27c308da0876131a3a6222135721a9bf.jpg)

![](images/14998918e8c2ad7c21ed2206e62c005d5bc25729ca2ca83bffe37da2006a423a.jpg)

![](images/d5c644bf69a8eb08c4dd63984e6100f9c41b6220da70a25ce1829ea8c07bc3b7.jpg)  
E

![](images/a7f49eccad149ced10b4a28207f17cac6685b69f5cb92c8ca1417e93dabf6e0e.jpg)  
FIGURE 1 Wafer-scale integration of ferroelectric-ionic duality. (A) Fabricated 6-inch wafer and enlarged SEM images of the AND-type memory array, fully fabricated using CMOS-compatible processes. (B) Schematic of the FIDFET with the $\mathrm { T i O } _ { 2 }$ interlayer. (C) Cross-sectional TEM and EDS mapping images and high-resolution STEM-iDPC images of the HZO film showing polarization directions consistent with the orthorhombic Pbc21 phase. (D) EELS analysis of the FIDFET gate stack: oxygen mapping highlights oxygen-rich regions (red pixels), while O K-edge spectra recorded across the HZO and TiO layers. The ${ p _ { 1 } / p _ { 2 } }$ peak ratio analysis indicates increased $\mathrm { v _ { 0 } }$ concentration at the ${ \mathrm { H Z O - T i O } } _ { 2 }$ interface, as schematically illustrated by interfacial oxygen absorption. (E) Schematic illustration of the conduction mechanism between ferroelectric switching (C) and ionic migration enhanced by high $\mathrm { v _ { 0 } }$ concentration (D) in the FIDFET.

contrast, FIDFET shows continued MW expansion at 5 V, despite a similar rise in $I _ { \mathrm { G } }$ (Figure 2C,D). While both devices increase $I _ { \mathrm { G } }$ at high $V _ { \mathrm { P G M } }$ , the underlying mechanisms differ: in FeFET, it results in performance degradation, whereas in FIDFET, it represents a synergistic coupling between ferroelectric and ionic switching. This $\mathrm { v _ { o } }$ -mediated modulation, enabled by the $\mathrm { T i O } _ { 2 }$ interlayer, resembles resistive switching behavior in oxide-based resistive random-access memory (RRAM), but here it functions synergistically with ferroelectric switching to extend the MW.

To validate the origin of switching behaviors and decouple the intrinsic ferroelectric response, polarization switching dynamics were analyzed via positive-up and negative-down (PUND) measurements (Figure S8, Supporting Information). Both FeFET and

FIDFET exhibit excellent ferroelectric switching dynamics with comparable double remnant polarization (2P ) values, indicating that the intrinsic ferroelectricity of HZO is maintained regardless of $\mathrm { T i O } _ { 2 }$ insertion (Figure 2E,G). Some differences were noted, particularly in leakage current behavior. FIDFET demonstrates lower leakage current than FeFET, resulting in closed P-V loops indicative of stable ferroelectric switching with minimal leakage current contribution [25]. The additional $\mathrm { T i O } _ { 2 }$ layer in FIDFET suppresses leakage, and its stability is retained even after repeated cycling, confirming improved reliability.

While intrinsic ferroelectric switching with negligible ionic involvement is dominant in FeFET, FIDFET exhibits hybrid switching: ferroelectric switching at low voltages and field-driven

![](images/5fdb163ae7508444298069338b50d5243408d140d30ac5e155ac802cfc7ed511.jpg)  
FeFET

![](images/807076f1d1fdaba9519cd8e9b480b49734bf3743d8418b2c3640fd155abfb9ea.jpg)

![](images/02f55887762e03e65f827c91406b06ee0521cfb5cb702c127314efd1774b61c7.jpg)

![](images/5986050b0a9e71c5a50927c05f2278d8b7d32f375c215b06a070f48963866b67.jpg)  
FIDFET

![](images/6031a3aeb969ac23c6764fa7f9cda981606d2b575c05836fb560b8ad0a0c4723.jpg)

![](images/9398b4f5ab43f9d5fba84af5c0b0dd8142fe6902bf97a80e569aa3ceab64a4cb.jpg)

![](images/5ccd4a8c522137fef80e0bba929534196d4c9f6f3311400eb7031909f69c2a12.jpg)

![](images/575c7c6d16d862f99c321d1e8d2b7e2502a4c64b62f9eae61921233a97af8026.jpg)

![](images/1a8efab2ad9b0d917712e2ca1414e2f07a6ec9d1759a587e4ca682e0521254f8.jpg)

![](images/61a51580a01f94e94f0c65170e8d1665b25cef2cf7174f2e44f602c4a792b2f0.jpg)

![](images/62c34ec5cfbbff77deff54f810b1dba5f1af08739d8f9726f619c2a74823a875.jpg)  
Pulse width (s)

![](images/103630a622a44c23b881d732edb7aafca669d25f8552480956961ceea226011a.jpg)  
FIGURE 2 Ferroelectric-Ionic switching in FIDFET. A–D) Transfer characteristics of the transistors without $\mathrm { T i O } _ { 2 }$ (FeFET) and with $\mathrm { T i O } _ { 2 }$ (FIDFET). $\left( \mathrm { A } , \mathrm { C } \right) I _ { \mathrm { D } ^ { - } } V _ { \mathrm { G S } }$ curves and $\left( \mathrm { B } , \mathrm { D } \right) I _ { \mathrm { G } } – V _ { \mathrm { G S } }$ curves measured under DC double-swept conditions under various positive voltages. In the FeFET, the MW initially expands but eventually decreases at higher voltages (5 V) due to increased gate leakage current and electron trapping. In contrast, for the FIDFET with a higher $\mathrm { v _ { 0 } }$ concentration, the MW dramatically expands at higher voltages, driven by ionic migration-induced $\mathrm { v _ { 0 } }$ movement. (E,G) Extracted $P { - } V$ curves using PUND results, demonstrating comparable ferroelectric switching behavior for FeFET and FIDFET. (F,H) Schematic representations of the voltage-dependent conduction mechanisms in the FeFET and FIDFET. (I,J) $V _ { \mathrm { t h } }$ changes with varying $V _ { \mathrm { P G M } }$ as well as pulse width. While the FeFET exhibits saturation behavior under 100 ns pulses, the FIDFET shows additional expansion of $V _ { \mathrm { t h } }$ under high $V _ { \mathrm { P G M } } \mathrm { s }$ or extended pulse widths, attributed to additional ionic migration effects. (K,L) Retention characteristics of the transistors, demonstrating excellent long-term stability and reliability in the FIDFET.

ionic migration at higher voltages (Figure 2F,H). Note that the dual-mode switching is consistently reproduced across multiple devices (Figure S9, Supporting Information). This additional ionic contribution modifies the channel potential and enables further MW expansion beyond the FE-only FeFET. Furthermore, to quantitatively distinguish the contributions of ferroelectric and ionic switching to memory modulation, we analyzed the $V _ { \mathrm { t h } }$ evolution under varying $V _ { \mathrm { P G M } }$ and pulse widths (Figure 2I,J). For FeFET, the MW saturates at 100 ns due to the limit of fast and intrinsic dipole switching, while FIDFET shows further MW expansion beyond this limit via ionic migration (Note S8, Supporting Information). The dual switching behavior is further reflected in the retention performance, resulting in a stable MW for up to 10 years for FIDFET (Figure 2K,L). This enhanced retention is attributed to the synergistic interplay between fast ferroelectric dipole switching and persistent ionic migration (Note S9, Supporting Information). The endurance behavior of both FeFET and FIDFET was evaluated under repeated PGM/ERS operations up to $1 0 ^ { 6 }$ cycles. (Figure S10, Supporting Information) Together, these mechanisms enable voltage- and time-dependent control of memory characteristics, capabilities not attainable in conventional FeFETs. Furthermore, we investigated the temperature- and time-dependence of MW in FIDFET. These thermal and temporal dependences of $\mathrm { V } _ { 0 } -$ driven modulation are reflected in the MW evolution trends (Figures S11 and S12, Supporting Information), where higher temperatures and longer holding times progressively expand the MW at reduced $V _ { \mathrm { P G M } } .$ , consistent with enhanced $\mathrm { v _ { o } }$ mobility (Methods; Note S10, Supporting Information). [22, 26, 27]

# 2.3 Stochastic Behavior and its Application to Spike Encoding

We adopted low-frequency noise (LFN) analysis as a nondestructive probe of trap dynamics and carrier transport to reveal how the intrinsic stochastic fluctuations of the FIDFET can serve as a native noise source for analog computing. By measuring $I _ { \mathrm { G } }$ (Figure 3A–D) and drain current $\left( I _ { \mathrm { D } } \right)$ (Figure 3E–H) noise under varied program (PGM)/erase (ERS) conditions (Methods; Figure S13, Note S11, Supporting Information), we decouple dipole and vacancy-driven contributions, revealing their combined influence on switching and stochastic behaviors [28–30]. Under varied $V _ { \mathrm { P G M } } \mathbf { s } ,$ 1/f noise behavior of FIDFET exhibits two distinct trends reflecting its dual switching modes (Figure 3B; Figure S14 and Note S11, Supporting Information). At lower $V _ { \mathrm { P G M } } \mathbf { s }$ (under 4.4 V), ferroelectric polarization reduces the net HZO field and drives up Poole-Frenkel (P-F)-emission–related noise, while above this threshold, $\mathrm { v _ { o } }$ migration forms conductive paths that instead suppress $1 / f$ noise as $V _ { \mathrm { P G M } }$ increases (Figure 3C; Note S11, Figures S15 and S16, Supporting Information) [28]. This in situ LFN analysis reveals the coexistence of dipole-driven ferroelectric switching and vacancy-driven ionic switching within the HZO film [31]. Furthermore, we performed LFN measurements under different operating temperatures. LFN measurements between 20 and $8 0 ^ { \circ } \mathrm { C }$ demonstrate a reduction in the voltage threshold for noise suppression and an increased steepness of the decay with rising temperature, indicative of thermally activated $\mathrm { v _ { o } }$ migration (Figure 3D; Note S12, Figures S17 and S18, Supporting Information). These temperature-dependent observations robustly delineate low-voltage ferroelectric polarization switch-

ing from high-voltage vacancy-mediated conduction within the same hafnia film.

We next analyze the $I _ { \mathrm { D } }$ noise of FIDFET to gain insight into stochastic behavior at the channel side (Figure 3E). In the FIDFET, both the noise magnitude and PSD shape evolve with $V _ { \mathrm { G S } }$ shifting from a $1 / f$ noise behavior whose magnitude decreases with bias at lower $V _ { \mathrm { G S } }$ to a mixed $1 / f { - } 1 / f ^ { 2 }$ noise behavior with rising corner frequency at high voltages (Figure 3F,G)— behavior that contrasts with the monotonic $1 / f$ noise decrease in FeFETs (Figure S19, Supporting Information) [32–34]. In conventional $\mathrm { F E T s } , I _ { \mathrm { D } }$ noise arises primarily from carrier number fluctuation (CNF). This phenomenon occurs when the number of free carriers in the channel fluctuates due to trapping and detrapping events at gate dielectric defects and channel interface traps, which explain the LFN behavior of the FeFETs (Figure S20 and Note S13, Supporting Information). This demonstrates that the switching and the conduction of FeFETs are not governed by the ${ \mathrm { V } } _ { 0 } { \mathrm { s } }$ . In the FIDFET, LFN at low $I _ { \mathrm { D } }$ values follows the CNF model; however, as the $I _ { \mathrm { D } }$ increases, $\mathrm { v _ { o } }$ dynamics alter the carrier transport mechanism, producing excess noise (Figure 3H; Figure S21, Supporting Information). To further confirm the $\mathrm { v _ { o } }$ origin of this RTN, we additionally analyzed the voltage dependence of the RTN dwell-time statistics and extracted the physical depth of the dominant trap from the ratio of high- and low-state dwell times (Figures S22 and S23, Supporting Information). The extracted trap position ( 2.65 nm inside the HZO layer) coincides with the $\mathrm { v _ { o } }$ -enriched region near the $\mathrm { T i O } _ { 2 } / \mathrm { H Z O }$ interface, providing quantitative evidence that the fluctuation responsible for the RTN is a $\mathrm { v _ { o } }$ -induced defect.

Based on the LFN analysis, we propose the use of this vacancy-driven high-current regime as a noise source suitable for analog stochastic encoding. We leverage the stochastic trapping–detrapping dynamics of ${ \mathrm { V } } _ { 0 } { \mathrm { { s } } }$ near the channel interface (Figure 4A,B) [30]. The microscopic noise-generation mechanism occurring during ferro-ionic switching is as follows: At low $V _ { \mathrm { G S } } ,$ , positively charged $\mathrm { v _ { o } }$ sites (white circles) remain distant from the channel, resulting in conventional CNF-induced $1 / f$ noise. When $V _ { \mathrm { G S } }$ increases, $\mathrm { v _ { o } }$ ions drift toward the interface and intermittently interact with channel electrons (blue circles), causing capture-and-emission events observable as random telegraph noise (RTN). At low $V _ { \mathrm { G S } } ,$ , no RTN is detected, confirming that $\mathrm { v _ { o } }$ sites remain distant to affect the channel charge fluctuation (Figure 3B,C). At intermediate $V _ { \mathrm { G S } } ,$ , the signal exhibits discrete two-level fluctuations with long capture and emission times $( \tau _ { \mathrm { e } }$ and $\tau _ { \mathrm { c } } ) _ { \cdot }$ , producing a pronounced $1 / f ^ { \mathrm { ~ 2 ~ } }$ trends in the PSD (Figure 3G). Increasing $V _ { \mathrm { G S } }$ further shortens both $\tau _ { \mathrm { e } }$ and $\tau _ { \mathrm { c } } ,$ causing the current to toggle more rapidly and shifting the corner frequency $( f _ { \mathrm { c o r n e r } } )$ to higher values, consistent with frequencydomain trends [35–37].

We translated this RTN into a hardware-friendly Poisson rate code by using a simple analog front-end. As shown in Figure 4C, the RTN current generated by the FIDFET is first converted into a voltage by a transimpedance stage, and this voltage is then passed through a single RC differentiator that produces sharp transient pulses at each capture–emission transition. These pulses are subsequently fed into a comparator, which outputs a digital spike whenever the differentiated voltage exceeds a fixed threshold, so that the inter-spike intervals inherit the

![](images/3d70653c801855fcb231d8daf9bc162ab71fc7f0bf245b95a43587effd42e80d.jpg)  
A

![](images/7d7f33b36b2582e1b0daaf9c3f6c663c4e8c8d42bd03a12ba5d63089eba70ebe.jpg)  
B

![](images/7528ee58abf8e92f155ef371952812eb10d777bf07d9184e746c26bf2f0c658b.jpg)  
C

![](images/44e208f0dd714e2a1cf896b0f7cef9069b94dad02348675930cd53ac4651ac91.jpg)  
D

![](images/7d3b4a0fdb45f98664ef438da4d11cb85f5d0f4c5f7cdab05fa91ad543d478a2.jpg)  
E   
F

![](images/6ce6314f425d58a71447e0e7a78ba0cc07c0f66321e7547c6e00d39b4e762897.jpg)

![](images/2457fec17d816d158aa4de93b6fc11bba3a342195a71c2a476de2e6c9b318094.jpg)  
G

![](images/bea78d222fc6483738635df68485eed32284fc71d1e767b2478fe2c50b4577ef.jpg)  
H   
FIGURE 3 $I _ { \mathrm { G } }$ and $I _ { \mathrm { D } }$ LFN measurement of FIDFET. (A) Schematic cross section and measurement configuration of $I _ { \mathrm { G } }$ noise in FIDFET. $\left( \mathrm { B } \right) I _ { \mathrm { G } }$ normalized noise PSD sampled at a 1000 Hz with varying $V _ { \mathrm { P G M } }$ revealing two regimes—increase in $1 / f$ noise below 4.4 V due to PF emission under reduced HZO field and decrease above 4.4 V as oxygen-vacancy migration forms conductive paths. $\left( \mathrm { C } \right) I _ { \mathrm { G } }$ normalized PSD versus $V _ { \mathrm { P G M } }$ highlighting the dual switching threshold. (D) Temperature dependence $( 2 0 ^ { \circ } \mathrm { C } \mathrm { t o } 8 0 ^ { \circ } \mathrm { C } )$ showing a reduced noise-suppression threshold and steeper decay indicative of thermally activated vacancy migration. (E) Schematic cross section and measurement configuration of $I _ { \mathrm { D } }$ noise in FIDFET. (F) $\boldsymbol { I _ { \mathrm { D } } }$ normalized PSD evolution with $V _ { \mathrm { G S } }$ shifting from a monotonic 1/f behavior at low bias to a mixed $1 / f \mathrm { - } 1 / f ^ { 2 }$ spectra with rising corner frequency at $V _ { \mathrm { G S } }$ bias. $( \mathrm { G } ) f _ { \mathrm { c o r n e r } }$ increase with $V _ { \mathrm { G S } } ;$ and H) noise magnitude versus $I _ { \mathrm { D } }$ illustrating a transition from CNF-dominated noise at low $I _ { \mathrm { D } }$ to excess vacancy-driven noise at high $I _ { \mathrm { D } } .$ .

exponential dwell-time statistics of the underlying RTN and realize a Poisson spike train whose mean rate is controlled by $V _ { \mathrm { G S } }$ (Figure S24, Supporting Information). Unlike conventional deterministic rate encoding—where each pixel fires at perfectly periodic intervals—Poisson encoding preserves only the average spike rate, allowing each inter-spike interval to jitter randomly. This controlled randomness mitigates synchronization artifacts and enhances inference robustness when temporal noise or misalignment corrupts the input stream [38, 39]. Implementing a true Poisson spike generator at the single-device level in conventional Si CMOS is challenging, since it typically relies on area-intensive pseudo-random number generators—such as linear-feedback shift registers—that demand substantial logic resources to achieve sufficient randomness and period [40, 41]. FIDFET circumvents this overhead: its RTN time constants $( \tau _ { \mathrm { c } }$ and $\tau _ { \mathrm { e } } )$ contract exponentially with $V _ { \mathrm { G S } }$ (Figure S24, Supporting Information) allowing a single RC differentiator followed by a comparator to digitize each capture–emission transition. By adjusting $V _ { \mathrm { G S } }$ values, the mean inter-spike interval can be tuned over nearly three orders of magnitude without altering the circuit topology. Note that Table S1 compares our energy efficiency, device area, and randomness quality against state-of-the-art reports [42–48]. To evaluate whether the vacancy-related RTN remains stable under extended operation, we further examined the dwell-time behavior of the two-level RTN signal under prolonged read bias conditions (Figures S25–S28, Supporting

Information). The extracted high- and low-state dwell times show no measurable drift across multiple observation windows and gate-bias conditions, indicating that no additional traps are generated and that the RTN fluctuation remains stable during long-term read operation.

To demonstrate system-level utility, we benchmarked the encoder on the DVS-Gesture dataset, an event-based camera recording hand motions with microsecond precision—ideal for evaluating time-domain coding schemes (Figure 4D; Note S14, Supporting Information). Deterministic DVS events from each active pixel pass through the FIDFET encoder; the resulting spike train maintains the original mean rate, but each interval now follows Poisson distribution, achieving stochastic encoding without additional random-number hardware. Because $\tau _ { \mathrm { c } } / \tau _ { \mathrm { e } }$ scale with $V _ { \mathrm { G S } } ,$ the spike rate can be voltage-programmed in realtime, enabling per-pixel adaptation. Figure 4E compares raw DVS spikes with FIDFET-encoded Poisson spikes for representative pixels in the hand clapping and left throw classes. Although the overall spike density is conserved, intervals fluctuate around the mean, confirming successful stochastic encoding. This simple, voltage-controlled approach eliminates bulky peripheral blocks and delivers randomness previously attainable only with 2D devices or numerical generators, offering a scalable route toward noise-resilient, event-driven vision hardware.

![](images/56bcbd8bf523ff0649ecd13cb5c3178150a125f1df0ff7eccb655e2b8b322440.jpg)

![](images/af1433f7f9d63853abd06e91e7396629929a0d7c6223624c1fbaf8c29e5e9971.jpg)

![](images/d76915ed3e19136af5d1d7eb466659cb52f5c4f1889c19b684393ac3d70a5962.jpg)  
B

![](images/50617cfdd8a753639e799974790393dc1b7c3be2dced8bb9a938be9a5acf39ab.jpg)

![](images/01706661f84afab9399a3001f2ab9c0f79b717b94fbdc75a2a1a20eb6e9e2079.jpg)

![](images/adfd29f58e0bc7754a94211086bf98cd7ed9e70465d219246e5b2bd810b394b2.jpg)

![](images/42541f0f9c4cd4ff397bc0af91af159b58c09523dd13942c7c544990fa50cec7.jpg)  
C

![](images/2e49e616b04968494fe1abfa4989242513a78b6a0644e2f6f6027193f7a552ca.jpg)

![](images/e1077000083982e53c79808d817a59d3a4cf76176e808e7585fb16e4ca49df71.jpg)

![](images/de75803b4acd6e5c3530f060ee8c0df752066f57f3f3a906a46fb967d3995c49.jpg)  
DVS Gesture Dataset   
D

![](images/d1e84835e719cb84eda1f5ab0fb9406fb62d645be6e023c156455ea91d90e24d.jpg)

![](images/ec82ce6ec0fa23db251b40462934376abe0a2135fd52bb0806af47c0808a0e71.jpg)

![](images/1a0ace0e5087636c6831ccf7e1c5fc6549a1ca828244dfb89e2562111d2f89c4.jpg)

![](images/b7400fb09ff4e5336aa53e2b2f9e2e00e85609116265cb0147040933de0ce1eb.jpg)

![](images/9706dd0e2247de8215ae4ea023c366536027a36ecaa81ad5a41dded66b7b8b54.jpg)  
E

![](images/d3027fd64fb700856adb7d082c97428efee4d02a40e4b133f6f99c59e03ee9ab.jpg)  
FIGURE 4 RTN-driven stochastic Poisson spike encoding using FIDFET and its application to event-driven vision. (A) Schematic of ferro-ionic switching in FIDFET under ferroelectric PGM (left) and Hybrid-PGM (right), with insets showing $\mathrm { v _ { 0 } }$ capture/emission near the channel at low and high $V _ { \mathrm { G S } } .$ (B) Measured drain-current traces at three $V _ { \mathrm { G S } }$ regimes: no RTN (teal), slow two-level RTN with long $\tau _ { \mathrm { c } } / \tau _ { \mathrm { e } }$ (blue), and fast two-level RTN with short $\tau _ { \mathrm { c } } / \tau _ { \mathrm { e } }$ (navy). (C) RTN-to-spike conversion: raw RTN signals (left) are passed through a single RC differentiator and comparator (center) to yield Poisson-distributed spike trains (right), with spike rate exponentially tunable by $V _ { \mathrm { G S } }$ modulation. (D) t-SNE projections of network activations for five classes of the DVS-Gesture dataset under deterministic (top row) versus RTN-driven Poisson (bottom row) encoding, showing improved class separability with stochastic encoding. E) Example spike rasters for “hand clapping” (green) and “left throw” (purple) events: deterministic DVS input versus FIDFET Poisson encoding, preserving mean rate while introducing interval jitter.

# 2.4 Integration of Stochastic Spike Encoding and VMM Neuromorphic Readout

To further demonstrate the effectiveness of RTN-based stochastic encoding in event-driven neuromorphic systems, we performed classification simulations using the DVS Gesture dataset (Figure 5A) [49]. Event streams from the DVS Gesture dataset are first converted into Poisson spike trains by directly exploiting the RTN characteristics of FIDFET. These RTN-driven spikes feed into a convolutional SNN, whose architecture comprises multiple convolutional layers followed by fully connected layers (Methods). An AND-type 24 × 12 crossbar array was fabricated and employed as a synaptic array in the SNN (Figure 5B and Methods). The dual use of FIDFET for both the signal encoding and synaptic stages enables a more compact and hardware-efficient neuromorphic system.

First, the fabricated FIDFETs were experimentally validated for their suitability as synaptic elements. Compared to conventional FeFETs, FIDFETs exhibit improved synaptic performance: their conductance modulation is both more linear and more uniform across devices (Figure 5C, Methods; Figures S29 and S30 and Note S15, Supporting Information) [50, 51]. This enhanced linearity simplifies weight programming and yields more reliable analog weight storage in neuromorphic hardware [52]. Based on the conductance modulation characteristics, spiking convolutional neural network (CNN)-based on-chip learning simulations were conducted to evaluate the suitability of FeFETs and FIDFETs as synaptic devices for neuromorphic computing (Figure S29 and Note S16, Supporting Information). FIDFET-based synapses outperform FeFET-only implementations in a spiking CNN trained on the Fashion modified National Institute of Standards and Technology (MNIST) dataset, delivering higher and more stable classification accuracy with reduced device-to-device variability (Figure S29, Supporting Information). Second, we performed array-level validation using a 24 × 12 FIDFET AND-type array to demonstrate selective programming, inhibition, and accurate vector-matrix multiplication (VMM). Individual cells within the FIDFET array can be selectively programmed and inhibited as intended (Figure 5D; Figure S31, Supporting Information). Figures S32 and S33 further present the $\mathrm { v _ { o } }$ crosstalk measurement and array-level device yield, confirming that all cells in the FIDFET array operate properly without defective devices.

Hardware-based neuromorphic computing was implemented through VMM via current summation. The accumulated current from the source lines can be read out along the column direction in AND type array. Uniform I-V behavior across FIDFET arrays results in summing these in a single VMM operation yields 52.3 nA, with under 1% deviation from the ideal sum, confirming precise array-level VMM accuracy (Figure 5E; Figure S34, Supporting Information). Figure 5F shows the VMM results from the FIDFET array under three different states: hybrid region, ferroelectric region, and erase state. To evaluate the impact of device-to-device variation on VMM operations, measurements were performed across various input cases and BLs (Methods). In the hybrid region, a wider MW and higher on/off ratio are observed, leading to a significantly larger current increase as the number of ‘on’ cells increases. We also confirmed that only the targeted cell is updated during both PGM modes, while inhibit cells remain unchanged, ensuring negligible crosstalk

during high-bias operation (Figure S35, Supporting Information). Furthermore, the statistical distribution of $V _ { \mathrm { t h } }$ extracted from the crossbar array shows the device-to-device variability in both FeFET and FIDFET (Figure S36, Supporting Information).

Finally, we integrated the RTN-based Poisson spike encoding with the deterministic VMM synaptic core into a unified stochastic neuromorphic processor and evaluated its performance on the DVS Gesture dataset. Note that, to our knowledge, integrating a voltage-tunable RTN stochastic encoder with an analog synapse in a single device has not been previously demonstrated (Table S4, Supporting Information) [53–58]. Figure 5G compares four hardware/algorithm co-design scenarios applied to the DVS-Gesture task. The two axes of variation are: (i) the spiking encoder— either a static FeFET encoder that emits perfectly periodic spikes or a dynamic FIDFET encoder whose RTN produces Poissondistributed intervals—and (ii) the spiking CNN core, where VMM and weight updates are executed using either FeFET arrays or FIDFET arrays. In all four cases, accuracy increases monotonically with training. However, the FIDFET-based spiking CNN consistently achieves the highest final accuracy, as its larger on/off ratio and more linear conductance-update curves minimize accumulation errors during gradient descent. Figure 5H shows inference robustness after training completion (epoch 40). Temporal noise was injected into the inter-event intervals of the DVS stream while keeping weight matrices fixed. The resulting accuracy curves demonstrate that overall resilience is governed principally by the choice of encoder rather than by the memory array: networks utilizing the dynamic FIDFET encoder retain high accuracy even under severe perturbation of interval variance, whereas those driven by the static FeFET encoder degrade rapidly. This behavior confirms that intrinsic Poisson jitter in FIDFET encoders provides a built-in regularization effect during training, resulting in networks naturally tolerant of timing noise. Coupled with the superior linearity of FIDFET VMM arrays, this approach delivers both higher peak accuracy and greater robustness compared to FeFET-only implementations. To further assess the generality of our stochastic encoder beyond DVS-based gesture recognition, we evaluated its behavior under controlled class ambiguity using blended Fashion-MNIST inputs (Figure S37, Supporting Information). In this ambiguous setting, the Poisson-encoded network exhibited consistently lower entropy and Brier scores than the deterministic baseline, demonstrating improved uncertainty calibration (Figure S38, Supporting Information). We additionally confirmed that this benefit arises from controlled sampling variability at the spike-input level while preserving the mean activation, as shown by the trial-to-trial spike-sum analysis (Figure S39, Supporting Information). Finally, to clarify, these advantages—including stochastic encoding and overall benefits of the proposed FIDFET—are summarized in Note S17.

# 3 Conclusion

In summary, we have introduced a monolithically integrated hafnia-based FIDFET that unites analog memory and tunable stochasticity within a single, CMOS-compatible platform. By deliberately engineering $\mathrm { v _ { o } }$ dynamics alongside ferroelectric polarization switching, the FIDFET achieves dual-mode operation: voltage-programmed RTN for Poisson-rate spike encoding

![](images/7240911e012d171b7bcc944b6480e86366bcc7073828792a935101428dd986a5.jpg)  
A

![](images/23c5bb3d160da918ab94bebe8a0128723e23194431bca048fe7fb85dd3bbb65f.jpg)  
B

![](images/299005f8c64a5432aa9e969e4ac1d0671bc5180bef904ff1e7edd665af921744.jpg)  
C

![](images/7ea2b55b8f8da8fd21a7d1418078d03726bf507a2d6b034fb95338510884c2a3.jpg)

![](images/2848f7cfda9654b8dc5f09b14b7b0664ef0ac0527e28db07bd02802bb9546724.jpg)  
E

![](images/02b64074f44de0843f0bc794f10e6f1dac47caf801760d8f1f19325dbcf046a2.jpg)  
F

![](images/5a54d01c91af31d5ebd44bb9810453eaa5bb8cf0e4e52bb31f4cc50bdf5f5408.jpg)  
G

![](images/58af038e8ffc7e7e7181af8ad960e5edb91b427e3779933c0fe289abfbb8f060.jpg)  
H   
FIGURE 5 Co-designed RTN-encoded spiking CNN and FIDFET synapses for DVS-Gesture classification. (A) System-level architecture: event streams from a DVS-Gesture sensor are converted into Poisson spike trains by exploiting FIDFET RTN, then fed into a convolutional SNN with an ANDtype 24 × 12 FIDFET crossbar synaptic array. (B) Schematic of synaptic array of FIDFET. (C) Measured conductance modulation of FeFET versus FIDFET synapses over successive programming pulse. (D) Array-level validation in a 24 × 12 FIDFET crossbar: selective programming/inhibition of individual cells. (E) VMM accuracy: summed column currents as a function of the number of “on” cells under $V _ { \mathrm { G S } } = 1 \mathrm { V } , V _ { \mathrm { D S } } = 0 . 1$ V, showing 52.3 nA ideal sum with <1% deviation. (F) VMM results from the 24 × 12 FIDFET array under three operating states—hybrid-ferroelectric (grey), ferroelectric (cyan), and erase (purple). The FIDFET exhibits a wider MW and higher on/off ratio, yielding a steeper current increase with rising on-cell count. (G) Training accuracy on DVS-Gesture for four hardware/algorithm co-design scenarios: static FeFET encoder + FeFET synapses (black), static encoder + FIDFET synapses (teal), RTN FIDFET encoder + FeFET synapses (purple), and fully FIDFET-based system (blue). (H) Inference robustness to injected temporal jitter after epoch 40: networks with RTN FIDFET encoding maintain high accuracy under severe interval variance, whereas static FeFET-encoded systems degrade rapidly.

and precise, linear conductance modulation for synaptic weight storage, while also exhibiting an expanded and bias-tunable MW, improved linearity, and enhanced operation stability enabled by the $\mathrm { T i O } _ { 2 }$ interlayer. This intrinsic device duality obviates bulky peripheral circuits—realizing both event-driven stochastic encoding and compact VMM in a crossbar array—and delivers robust gesture classification on the DVS-Gesture benchmark with high accuracy, low latency and exceptional resilience to temporal noise. Moving forward, the FIDFET paradigm paves the way for fully integrated neuromorphic-probabilistic cores, where devicelevel randomness is exploited as a computational resource rather than treated as a reliability concern. Scaling to larger arrays and deeper network architectures will benefit from the wafer-scale ALD process demonstrated in this work, while co-optimization of device materials and circuit topologies promises further gains in energy efficiency and functional density. More broadly, our approach suggests a new materials-centric design principle for AI hardware: transform intrinsic defects into programmable functions, thereby unifying memory, computation and stochastic inference in a single, scalable platform.

# 4 Methods

# 4.1 Fabrication of Devices

Transistors were fabricated on a silicon-on-insulator (SOI) substrate with a 100 nm-thick. The process began with active region definition through photolithography and dry etching, followed by a series of cleaning steps including piranha solution (SPM) treatment, standard clean-1 (SC-1), and standard clean-$2 \ ( \mathrm { S C } \cdot 2 )$ . Subsequently, gate stacks of $\mathrm { S i O } _ { 2 } / \mathrm { H Z O }$ (FeFET) and $\mathrm { S i O _ { 2 } / T i O _ { 2 } / H Z O ( F I D F E T ) }$ were deposited at 330◦C using BDEAS, TDMAT, TEMA-Hf, TEMA-Zr, and $\mathrm { O } _ { 3 }$ as the respective precursors and oxygen source. The HZO composition was precisely tuned by adjusting the cycle ratio of $\mathrm { H f O } _ { 2 }$ and $\mathrm { Z r O } _ { 2 } ,$ , employing two cycles of HfO followed by one cycle of $Z \mathrm { r } { \bf O } _ { 2 } .$ . The deposited stack included a 1.3 nm $\mathrm { S i O } _ { 2 }$ interlayer and a 6.4 nm HZO ferroelectric layer. For the FIDFET, a 0.5 nm $\mathrm { T i O } _ { 2 }$ layer was inserted between the $\mathrm { S i O } _ { 2 }$ and HZO. TiN was sputtered as the gate electrode and patterned through photolithography and dry etching. Source and drain regions were formed via self-aligned phosphorus ion implantation at a dose of $1 0 ^ { 1 5 }$ cm−2 with an acceleration energy of 20 keV. Post-metallization annealing (PMA) was conducted at $6 5 0 ^ { \circ } \mathrm { C }$ for 30 s in a nitrogen atmosphere to activate phosphorus dopant and to crystallize ferroelectric HZO layer. A 300 nm $\mathrm { S i O } _ { 2 }$ passivation layer was subsequently deposited using plasma-enhanced chemical vapor deposition (PECVD). Finally, Ti/TiN/Al/TiN metal stacks were deposited by sputtering to form contact pads, following the opening of the contact vias using reactive ion etching (RIE). The fabricated device structures were characterized by cross-sectional transmission electron microscopy (TEM) and energy-dispersive X-ray spectroscopy (EDS) mapping (Figure S2, Supporting Information).

# 4.2 GIXRD Measurement

Grazing-incidence X-ray diffraction (GIXRD) measurements were conducted using a high-resolution X-ray diffractometer (X’pert Pro) with an incident angle set at $0 . 5 ^ { \circ }$ to improve surface

sensitivity and accurately probe the crystallinity of the thin films. The acquired GIXRD patterns were analyzed to identify the distinct crystalline phases—orthorhombic, tetragonal, and monoclinic—and to quantify their relative phase fractions, providing critical insights into the ferroelectric behavior of the HZO layers.

# 4.3 PUND Measurement

The ferroelectric characteristics of the ferroelectric devices were evaluated using a parameter analyzer (Keithley 4200-SCS) integrated with a current-voltage module (4225-PMU). Polarizationvoltage (P–V) hysteresis curves were measured through the PUND technique to selectively capture only the polarization switching currents. In this method, the ferroelectric switching component was extracted by calculating the difference between the positive-up and negative-down pulses, as the positive and negative pulses contain both switching (polarization) and nonswitching (displacement and leakage) contributions, whereas the up and down pulses represent solely nonswitching behavior. A triangular waveform with a frequency of 10 kHz was applied during the PUND measurements.

# 4.4 EELS Measurement

STEM-EELS spectra were collected using a ThermoFisher Spectra Ultra microscope equipped with double-Cs correctors (image and probe), operated at 300 kV. Both low-loss and core-loss spectra were acquired with 0.25 eV energy dispersion. Quantitative oxygen mapping and ELNES analysis of the O-K edge were performed using Gatan Microscopy Suite (GMS 3), following Verbeeck and Van Aert [59]. Power-law background subtraction and Hartree-Slater cross-section modeling were used to extract oxygen content. The ${ p _ { 1 } / p _ { 2 } }$ peak intensity ratio of the O Kedge ELNES was analyzed to assess local variations in $\mathrm { v _ { o } }$ concentration across the HZO films.

# 4.5 XPS Measurement

X-ray photoelectron spectroscopy (XPS) measurements were carried out using a ThermoFisher Scientific NEXSA system to analyze the $\mathrm { v _ { o } }$ concentration in the fabricated devices. Depthprofile XPS analysis was employed to investigate the spatial distribution of oxygen vacancies, with particular focus on their correlation with the presence of the $\mathrm { T i O } _ { 2 }$ interlayer.

# 4.6 Temperature- and Time-Dependent Measurement

To evaluate the influence of thermal and temporal stress on ${ \mathrm { V } } _ { 0 } -$ driven modulation, we conducted a series of temperature- and holding-time- dependent I-V measurements. $\mathrm { V } _ { \mathrm { P G M } } \mathbf { s }$ ranging from 3.5 to 4.5 V were applied at four different temperatures: 20, 40, 60, and $8 0 ^ { \circ } \mathrm { C } .$ For each test condition, the $V _ { \mathrm { G S } }$ was applied from negative to positive, and the holding time was applied at the onset of the positive sweep, corresponding to the starting point of the $V _ { \mathrm { G S } }$ . Holding times of 0, 2, 5, 10, and 20 s were used before

continuing the sweep to complete the I-V measurement. This measurement scheme allowed for systematic observation of MW evolution under controlled thermal and temporal stress, revealing the dynamics of $\mathrm { v _ { o } }$ -mediated switching.

# 4.7 LFN Measurement

Low-frequency noise (LFN) measurements were conducted using a semiconductor parameter analyzer (Keysight B1500A) to apply specific $V _ { \mathrm { G S } }$ to the top gate terminal of the devices and $V _ { \mathrm { D S } }$ to the drain contact. The source terminal of the devices was grounded through a signal amplifier (Stanford Research Systems SR570). The resulting current fluctuations were converted into voltage signals and amplified by a low-pass filter embedded within the amplifier. Subsequently, these amplified voltage fluctuations were transformed into power spectral density (PSD) data in the frequency domain using a dynamic signal analyzer (Keysight 35670A). Measurements were systematically repeated under varying $V _ { \mathrm { G S } }$ to explore different operating regimes of the devices. Additionally, temperature-dependent measurements were performed to evaluate the thermal behavior of the noise characteristics.

# 4.8 Electrical Measurement Setup

The overall experimental setup for the device measurements is shown in Figure S40 (Supporting Information). The ferroelectric properties of the fabricated HZO, TiO -based FIDFETs were investigated using a probe station and Keithley 4200-SCS semiconductor parameter analyzer (Keithley 4200-SCS). DC $I _ { \mathrm { D } } { \displaystyle - V _ { \mathrm { G S } } }$ characteristics were conducted using a Keysight B1500A semiconductor parameter analyzer equipped with a source measurement unit (SMU). RTN and VMM operation were measured using B1500A equipped with a waveform generator/fast measurement unit (B1530A, WGFMU) module and a high-voltage semiconductor pulse generator unit (B1525A, SPGU) were used for the pulse and speed measurements. To characterize the fabricated array, we connected a B1500A to a Keysight E5250A switching matrix and acquired the array’s electrical characteristics using a custommade probe card. To control the array, each input is routed to multiple output channels of the switching matrix and controlled via a customized LabVIEW program and Keysight Easy Expert.

# 4.9 Stochastic Spike Encoding Circuit Setup

To validate the operation of the stochastic spike-encoding circuit, PSPICE circuit simulation was performed. Figure S24A shows the full schematic: the device’s current is first converted to a voltage compatible with the transimpedance amplifier (LM741, $V _ { \mathrm { D D } } = 1 0 ~ \mathrm { V } )$ via a variable resistor that adapts to the device’s current. The amplified voltage is then passed through an RC differentiator $( R = 1 0 ~ \mathrm { k } \Omega , C = 0 . 1 ~ \mu \mathrm { F } )$ to generate spikes at the rising and falling edges of the RTN signal. The characteristics were confirmed by adjusting the R and C values to optimize the RC conditions. Figure S41 shows the results of the output voltage of the RC circuit according to the R and C values. For small RC values, the circuit behaves as a differentiator and generates spikes (Figure S41A, Supporting Information); for large RC values, it

functions as a coupling capacitor that blocks DC components (Figure S41B, Supporting Information). Figure S24C (Supporting Information) plots the node voltage after differentiation, showing an exponential increase in spike frequency as the RTN dwell time decreases. Finally, a comparator converts these pulses into digital spikes $( \mathrm { o u t p u t } = V _ { \mathrm { D D } }$ when $V _ { \mathrm { i n } } > \mathrm { G N D } )$ , and Figure S24D (Supporting Information) quantifies the spike rate, confirming that shorter dwell times (S1→S4) yield dramatically higher firing frequencies [60].

# 4.10 VMM Operation in AND Type FIDFET Array

VMM operations were performed using the fabricated $2 4 \times 1 2$ FIDFET array by varying the number of cells. The accumulated current along the shared SL was measured to assess the linearity and scalability of array-level computation. In the pristine state, VMM was repeated with 1000 random binary input patterns to evaluate the impact of device variation, where the same input pattern can result in different output currents due to inherent variability in device characteristics. A 1 V pulse was applied to selected WLs, while unselected WLs were grounded. For the programmed states, two operation regions inherent to FIDFET, FE (5 V, 1 µs) and hybrid (5 V, 100 µs), were used to perform VMM across 50 BLs. In both regions, the output SL current increased linearly with the number of contributing cells, confirming reliable summation behavior.

# 4.11 Pulse Conditions for Potentiation and Depression

The potentiation and depression conditions were extracted to capture device-specific weight update behavior and incorporated into the on-chip learning simulations for realistic modeling. To evaluate conductance modulation, identical pulses were applied to selected cells within the array. For FeFETs, potentiation was achieved by applying a pulse of 3.5 V (1 µs) to the WL of the selected cell, while grounding both the BL and SL. To prevent unintended disturbance in unselected cells, an inhibit voltage of 2 V was applied to their BL and SL. For depression, a pulse of 3.8 V (200 ns) was applied to the BL and SL of the selected cell while grounding its WL, and 2.5 V was applied to the WLs of unselected cells to suppress disturbance. In contrast, for FIDFET devices, potentiation was performed by applying a 5 V (50 µs) pulse to the WL of the selected cell with grounded BL and SL, while a 2.5 V inhibit voltage was applied to the BL and SL of unselected cells. Depression was achieved by applying a 3 V (10 µs) pulse to the BL and SL while grounding the WL of the selected cell and applying 2.5 V to the WLs of unselected cells to prevent state change. Figure S29B,C shows the conductance modulation characteristics of 30 devices within the fabricated AND-type array, confirming that only the selected cells exhibited conductance changes, while unselected cells remained unaffected.

# 4.12 Software Algorithm

The network architecture employed for image classification using the DVS Gesture dataset is detailed below. To evaluate

classification performance, simulations were performed using five classes from the DVS Gesture dataset: hand clapping, right wave, left wave, right CW, and left CW. The network architecture consists of two convolutional layers followed by ReLU activations and max pooling operations. The input to the network is a 2- channel 128 × 128 image. The first convolutional layer maps the input to 16 channels using a 3 × 3 kernel with padding of 1, followed by a ReLU activation and a 2 × 2 max pooling. The second convolutional layer increases the depth to 32 channels using the same kernel and padding configuration, again followed by ReLU and 2 × 2 max pooling. The resulting feature maps are flattened and passed through a fully connected layer that reduces the dimensionality. A Leaky-Spiking activation function with a decay factor β = 0.9 is applied, followed by a final fully connected layer mapping to the output class space. The model was trained using cross-entropy loss and Adam optimizer for 200 epochs. The conductance response of the FIDFET device was learned and utilized for weight updates. The trained weights of the ANN were directly transferred to the SNN, and its performance was evaluated using both deterministic and Poisson spike encoding schemes. In all experiments, temporal DVS or RTNdriven spike trains are first accumulated into frame-based rate (spike-count) maps, and the subsequent convolutional network operates on these rate maps rather than propagating individual spikes through all layers. The spiking CNN itself consists of conventional convolution, ReLU, pooling, and fully connected layers trained by backpropagation, and we do not explicitly simulate membrane-potential dynamics inside the hidden layers. In this sense, only the input encoding is spike-based, whereas the core network functions as a frame-based spiking CNN with Poisson-rate encoded inputs.

# Acknowledgements

This work was supported by the Institute of Information & Communications Technology Planning & Evaluation (IITP) under the Artificial Intelligence Semiconductor Support Program to Nurture the Best Talents (IITP-2025-RS-2023-00253914), by Samsung Electronics Co., Ltd. (Grant No. IO240514-09972-01), and by the National Research Foundation of Korea (NRF) grant funded by the Korean Government (MSIT) (RS-2024- 00336845).

# Conflicts of Interest

The authors declare no conflict of interest.

# Data Availability Statement

The authors declare that the data supporting the findings of this study are available within the paper and its supplementary information files.

# References

1. K. Roy, A. Jaiswal, and P. Panda, “Towards Spike-Based Machine Intelligence With Neuromorphic Computing,” Nature 575 (2019): 607.   
2. K. U. Demasius, A. Kirschen, and S. Parkin, “Energy-Efficient Memcapacitor Devices for Neuromorphic Computing,” Nature Electronics 4 (2021): 748.   
3. I. Boybat, M. L. Gallo, S. R. Nandakumar, et al., “Neuromorphic Computing With Multi-Memristive Synapses,” Nature Communications 9 (2018): 2514.

4. D. Marković, A. Mizrahi, D. Querlioz, and J. Grollier, “Physics for Neuromorphic Computing,” Nature Reviews Physics 2 (2020): 499.   
5. P. Ajayan, P. Kim, and K. Banerjee, “Two-Dimensional van der Waals Materials,” Physics Today 69 (2016): 38.   
6. Y. Hu, H. Lu, S. B. Masood, et al., “A 2D Hybrid Perovskite Ferroelectric With Switchable Polarization and Photoelectric Robustness Down to Monolayer,” Nature Communications 16 (2025): 3028.   
7. J. Kim, E. C. Park, W. Shin, et al., “Analog Reservoir Computing Via Ferroelectric Mixed Phase Boundary Transistors,” Nature Communications 15 (2024): 9147.   
8. D. Jayachandran, R. Pendurthi, M. U. K. Sadaf, et al., “Three-Dimensional Integration of Two-Dimensional Field-Effect Transistors,” Nature 625 (2024): 276.   
9. M. U. K. Sadaf, Z. Chen, S. Subbulakshmi Radhakrishnan, et al., “Enabling Static Random-Access Memory Cell Scaling With Monolithic 3D Integration of 2D Field-Effect Transistors,” Nature Communications 16 (2025): 4879.   
10. Y. Shen, K. Zhu, Y. Xiao, et al., “Two-Dimensional-Materials-Based Transistors Using Hexagonal Boron Nitride Dielectrics and Metal Gate Electrodes With High Cohesive Energy,” Nature Electronics 7 (2024): 856.   
11. S. Husain, I. Harris, G. Gao, et al., “Low-Temperature Grapho-Epitaxial La-Substituted BiFeO3 on Metallic Perovskite,” Nature Communications 15 (2024): 479.   
12. P. Behera, A. M. Ross, N. Shanker, et al., “Anisotropic Ferroelectricity in Polar Vortices,” Advanced Materials 37 (2025): 2410149.   
13. T. Park, M. Kim, E. K. Lee, J. Hur, and H. Yoo, “Overcoming Downscaling Limitations in Organic Semiconductors: Strategies and Progress,” Small 20 (2024): 2306468.   
14. J. Choi, C. Lee, C. Lee, et al., “Vertically Stacked, Low-Voltage Organic Ternary Logic Circuits Including Nonvolatile Floating-Gate Memory Transistors,” Nature Communications 13 (2022): 2305.   
15. C. Lee, C. Lee, S. Lee, J. Choi, H. Yoo, and S. G. Im, “A Reconfigurable Binary/Ternary Logic Conversion-In-Memory Based on Drain-Aligned Floating-Gate Heterojunction Transistors,” Nature Communications 14 (2023): 3757.   
16. I. J. Kim and J. S. Lee, “Ferroelectric Transistors for Memory and Neuromorphic Device Applications,” Advanced Materials 35 (2023): 2206864.   
17. I. J. Kim, M. K. Kim, and J. S. Lee, “Highly-Scaled and Fully-Integrated 3-Dimensional Ferroelectric Transistor Array for Hardware Implementation of Neural Networks,” Nature Communications 14 (2023): 504.   
18. M. K. Park, J. Hwang, S. Kim, et al., “Charge-Trap Synaptic Device With Polycrystalline Silicon Channel for Low Power In-Memory Computing,” Scientific Reports 14 (2024): 29089.   
19. S. W. Kim, W. Shin, R. Koo, et al., “A New Back-End-Of-Line Ferroelectric Field-Effect Transistor Platform via Laser Processing,” Small 21 (2024): 2406376.   
20. Y. Cheng, Z. Gao, K. H. Ye, et al., “Reversible Transition Between the Polar and Antipolar Phases and its Implications for Wake-Up and Fatigue in HfO2-Based Ferroelectric Thin Film,” Nature Communications 13 (2022): 645.   
21. Q. Luo, Y. Cheng, J. Yang, et al., “A Highly CMOS Compatible Hafnia-Based Ferroelectric Diode,” Nature Communications 11 (2020): 1391.   
22. J. Lee, K. Yang, J. Y. Kwon, et al., “Role of Oxygen Vacancies in Ferroelectric or Resistive Switching Hafnium Oxide,” Nano Convergence 10 (2023): 55.   
23. K. Takagi and T. Ono, “First-Principles Study on Leakage Current Caused by Oxygen Vacancies at HfO 2 /SiO 2 /Si Interface,” Japanese Journal of Applied Physics 57 (2018): 066501.   
24. J. Lee, M. S. Song, W. S. Jang, et al., “Modulating the Ferroelectricity of Hafnium Zirconium Oxide Ultrathin Films via Interface Engineering to

Control the Oxygen Vacancy Distribution,” Advanced Materials Interfaces 9 (2022): 2101647.   
25. Y. Peng, G. Han, F. Liu, et al., “Ferroelectric-Like Behavior Originating From Oxygen Vacancy Dipoles in Amorphous Film for Non-volatile Memory,” Nanoscale Research Letters 15 (2020): 134.   
26. R. Meyer, R. Liedtke, and R. Waser, “Oxygen Vacancy Migration and Time-Dependent Leakage Current Behavior of Ba0.3Sr0.7TiO3 Thin Films,” Applied Physics Letters 86 (2005): 112904.   
27. J. Hanzig, M. Zschornak, E. Mehner, et al., “The Anisotropy of Oxygen Vacancy Migration in SrTiO 3,” Journal of Physics: Condensed Matter 28 (2016): 225001.   
28. R. H. Koo, W. Shin, K. K. Min, et al., “Optimizing Post-Metal Annealing Temperature Considering Different Resistive Switching Mechanisms in Ferroelectric Tunnel Junction,” IEEE Electron Device Letters 44 (2023): 935.   
29. W. Shin, R. H. Koo, K. K. Min, et al., “Effects of Temperature and DC Cycling Stress on Resistive Switching Mechanisms in Hafnia-Based Ferroelectric Tunnel Junction,” Applied Physics Letters 122 (2023): 152901.   
30. R. H. Koo, W. Shin, K. K. Min, et al., “Effect of Carrier Transport Process on Tunneling Electroresistance in Ferroelectric Tunnel Junction,” IEEE Electron Device Letters 44 (2023): 164.   
31. V. Mikheev, A. Chouprik, Y. Lebedinskii, et al., “Memristor With a Ferroelectric HfO 2 Layer: In Which Case it is a Ferroelectric Tunnel Junction,” Nanotechnology 31 (2020): 215205.   
32. R. H. Koo, W. Shin, J. Kim, et al., “Polarization Pruning: Reliability Enhancement of Hafnia-Based Ferroelectric Devices for Memory and Neuromorphic Computing,” Advanced Science 11 (2024): 2407729.   
33. W. Shin, R. H. Koo, S. Kim, et al., “Robust 1/ f Noise Unaffected by Program/Erase Cycling-Induced Damage in Ferroelectric Schottky Barrier FETs,” IEEE Electron Device Letters 45 (2024): 1645.   
34. R. H. Koo, W. Shin, S. Kim, et al., “Low-Frequency Noise Spectroscopy for Navigating Geometrically Varying Strain Effects in HfO 2 Ferroelectric FETs,” Advanced Science 12 (2025): 2501367.   
35. M. Banaszeski Da Silva, H. P. Tuinhout, A. Zegers-Van Duijnhoven, G. I. Wirth, and A. J. Scholten, “A Physics-Based Statistical RTN Model for the Low Frequency Noise in MOSFETs,” IEEE Transactions on Electron Devices 63 (2016): 3683.   
36. H. J. Cho, S. Lee, B. G. Park, and H. Shin, “Extraction of Trap Energy and Location From Random Telegraph Noise in Gate Leakage Current (Ig RTN) of Metal–Oxide Semiconductor Field Effect Transistor (MOSFET),” Solid-State Electronics 54 (2010): 362.   
37. R. H. Koo, W. Shin, S. T. Lee, D. Kwon, and J. H. Lee, “Stochastic Behavior of Random Telegraph Noise in Ferroelectric Devices: Impact of Downscaling and Mitigation Strategies for Neuromorphic Applications,” Chaos, Solitons & Fractals 191 (2025): 115856.   
38. C. E. Rullán Buxó and J. W. Pillow, “Poisson Balanced Spiking Networks,” PLoS Computational Biology 16 (2020): 1008261.   
39. J. Gao, Y. C. Chien, J. Huo, et al., “Reconfigurable Neuromorphic Functions in Antiferroelectric Transistors Through Coupled Polarization Switching and Charge Trapping Dynamics,” Nature Communications 16 (2025): 4368.   
40. M. Karamimanesh, E. Abiri, M. Shahsavari, K. Hassanli, A. van Schaik, and J. Eshraghian, “Spiking Neural Networks on FPGA: A Survey of Methodologies and Recent Advancements,” Neural Networks 186 (2025): 107256.   
41. F. J. Rubio-Barbero, F. de los Santos-Prieto, R. Castro-Lopez, E. Roca, and F. V. Fernandez, “Harvesting Random Telegraph Noise for True Random Number Generation,” AEU—International Journal of Electronics and Communications 196 (2025): 155801.   
42. J. Daniel, Z. Sun, X. Zhang, et al., “Experimental Demonstration of an On-Chip p-bit Core Based on Stochastic Magnetic Tunnel Junctions and 2D MoS2 Transistors,” Nature Communications 15 (2024): 4098.

43. Y.-C. Chiu, W.-S. Khwa, C.-S. Yang, et al., “A CMOS-Integrated Spintronic Compute-In-Memory Macro for Secure AI Edge Devices,” Nature Electronics 6 (2023): 534.   
44. W. A. Borders, A. Z. Pervaiz, S. Fukami, K. Y. Camsari, H. Ohno, and S. Datta, “Integer Factorization Using Stochastic Magnetic Tunnel Junctions,” Nature 573 (2019): 390.   
45. R. Carboni and D. Ielmini, “Stochastic Memory Devices for Security and Computing,” Advanced Electronic Materials 5 (2019): 1900198.   
46. R. Carboni, W. Chen, M. Siddik, et al., “Random Number Generation by Differential Read of Stochastic Switching in Spin-Transfer Torque Memory,” IEEE Electron Device Letters 39 (2018): 951.   
47. T. Tuma, A. Pantazi, M. L. Gallo, A. Sebastian, and E. Eleftheriou, “Stochastic Phase-Change Neurons,” Nature Nanotechnology 11 (2016): 693.   
48. S. Balatti, S. Ambrogio, R. Carboni, V. Milo, Z. Wang, and A. Calderoni, “Physical Unbiased Generation of Random Numbers With Coupled Resistive Switching Devices,” IEEE Transactions on Electron Devices 63 (2016): 2029.   
49. A. Amir, B. Taba, and D. Berg, Proceedings –30th IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2017 (IEEE, 2017), 7243.   
50. P. Y. Chen, B. Lin, and I. T. Wang, 2015 IEEE/ACM International Conference on Computer-Aided Design, ICCAD 2015 (IEEE, 2015), 194.   
51. G. H. Lee, T. H. Kim, S. Youn, J. Park, S. Kim, and H. Kim, “Low-Fluctuation Nonlinear Model Using Incremental Step Pulse Programming With Memristive Devices,” Chaos, Solitons & Fractals 170 (2023): 113359.   
52. S. T. Yang, X. Y. Li, T. L. Yu, et al., “High-Performance Neuromorphic Computing Based on Ferroelectric Synapses With Excellent Conductance Linearity and Symmetry,” Advanced Functional Materials 32 (2022): 2202366.   
53. J. Park, H. Kim, and H. Kim, “Bias-Independent True Random Number Generator Circuit using Memristor Noise Signals as Entropy Source,” Advanced Intelligent Systems 7 (2025): 2400648.   
54. C. Wen, X. Li, W. Zheng, et al., “Advanced Data Encryption Using 2D Materials,” Advanced Materials 33 (2021): 2100185.   
55. B. Gao, B. Lin, X. Li, J. Tang, and H. Qian, “A Unified PUF and TRNG Design Based on 40-nm RRAM With High Entropy and Robustness for IoT Security,” IEEE Transactions on Electron Devices 69 (2022): 536.   
56. X. Li, B. Lin, B. Gao, et al., “A Memristor-Based Unified PUF and TRNG Chip With A Concealable Ability for Advanced Edge Security,” Science Advances 11 (2025): ad01112.   
57. H. Ravichandran, T. Knobloch, S. S. Radhakrishnan, et al., “A Stochastic Encoder Using Point Defects In Two-Dimensional Materials,” Nature Communications 15 (2024): 10562.   
58. B. Ray and A. Milenković, “True Random Number Generation Using Read Noise of Flash Memory Cells,” IEEE Transactions on Electron Devices 65 (2018): 963.   
59. J. Verbeeck and S. Van Aert, “Model Based Quantification of EELS Spectra,” Ultramicroscopy 101 (2004): 207.   
60. H. Ravichandran, T. Knobloch, S. Subbulakshmi, et al., “A Stochastic Encoder Using Point Defects in Two-Dimensional Materials,” Nature Communications 15 (2024): 10562.

# Supporting Information

Additional supporting information can be found online in the Supporting Information section.

Supporting file: adma71965-sup-0001-SuppMat.docx.