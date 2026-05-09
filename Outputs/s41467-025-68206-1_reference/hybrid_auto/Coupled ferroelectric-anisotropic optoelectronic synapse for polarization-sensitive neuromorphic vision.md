---

title: "Coupled Ferroelectric-Anisotropic Optoelectronic Synapse for Polarization-Sensitive\\"
authors:
  - "Jiali Huo"
  - "Jinpeng Huo"
  - "Jing Gao"
  - "Lingqi Li"
  - "Thaw Tint Te Tun"
  - "Jin Peng"
  - "Haofei Zheng"
  - "Yufei Shi"
  - "Kah-Wee Ang"
date: "2026-01-08"
year: "2026"
journal: "Nature Communications"
abstract: "This paper presents a polarization-resolved optoelectronic synapse integrating polarization-sensitive\\"
abstract_cn: "本文提出了一种偏振分辨光电突触，在单个器件中集成偏振敏感光电检测和非易失性存储。采用2D ReS2沟道结合Hf0.5Zr0.5O2栅介质构成MFMIS FeFET。铁电极化与光生载流子捕获的协同调控实现高响应度和长期光电保持。ANN在非偏振光下实现97.33%虹膜识别，3x3\\"
keywords:
  - "[[Optoelectronic Synapse]]"
  - "[[Ferroelectric]]"
  - "[[ReS2]]"
  - "[[HZO]]"
  - "[[Polarization]]"
  - "[[Neuromorphic Vision]]"
  - "[[光电突触]]"
  - "[[神经形态视觉]]"
cite: "Huo J, Huo J, Gao J, Li L, Tun T T T, Peng J, Zheng H, Shi Y, Ang K W. Coupled Ferroelectric-Anisotropic\\"
aiSum: "偏振分辨光电突触，ReS2/HZO MFMIS FeFET结构。ANN 97.33%虹膜识别，3x3 FeFET CNN蝴蝶分类，2.0 fJ/事件能效。铁电-各向异性平台实现偏振敏感神经形态视觉。"
confidence: "high"
wiki_concepts:
  - "[[Ferroelectric]]"
  - "[[HfO2]]"
---

# Coupled ferroelectric-anisotropic optoelectronic synapse for polarization-sensitive neuromorphic vision

Received: 21 April 2025

Accepted: 19 December 2025

Cite this article as: Huo, J., Huo, J., Gao, J. et al. Coupled ferroelectricanisotropic optoelectronic synapse for polarization-sensitive neuromorphic vision. NatCommun (2025). https://doi.org/10.1038/ s41467-025-68206-1

Jiali Huo, Jinpeng Huo, Jing Gao, Lingqi Li, Thaw Tint Te Tun, Jin Peng, Haofei Zheng, Yufei Shi & Kah-Wee Ang

We are providing an unedited version of this manuscript to give early access to its findings. Before final publication, the manuscript will undergo further editing. Please note there may be errors present which affect the content, and all legal disclaimers apply.

If this paper is publishing under a Transparent Peer Review model then Peer Review reports will publish with the final article.

# Coupled Ferroelectric-Anisotropic Optoelectronic Synapse for Polarization-Sensitive Neuromorphic Vision

Jiali Huo1, Jinpeng Huo2, Jing Gao1, Lingqi Li1, Thaw Tint Te Tun1, Jin Peng2, Haofei Zheng1, Yufei Shi1, Kah-Wee Ang1, *

1 Department of Electrical and Computer Engineering, National University of Singapore, 4 Engineering Drive 3, Singapore, 117583 Singapore.   
2 State Key Laboratory of Clean and Efficient Turbomachinery Power Equipment, Department of Mechanical Engineering, Tsinghua University, Beijing, 100084, China.

*Email: eleakw@nus.edu.sg

Polarization-sensitive photodetection and non-volatile memory are both vital for neuromorphic vision hardware but are rarely integrated within a single device. This challenge arises from interfacial instabilities and depolarization fields at the 2D/ferroelectric junctions that degrade remanent polarization and long-term retention. Here, we demonstrate a polarization-resolved optoelectronic synapse based on a $2 \mathbf { D } \mathbf { R e } \mathbf { S } _ { 2 }$ channel and a ferroelectric $\mathbf { H f _ { 0 . 5 } Z r _ { 0 . 5 } O _ { 2 } }$ (HZO) gate dielectric in a metal-ferroelectric-metal-insulatorsemiconductor (MFMIS) ferroelectric field-effect transistor (FeFET). Co-modulation of ferroelectric polarization and photoexcited carrier trapping enables high responsivity, strong detectivity, and long-term optoelectronic retention. Coupling between the polarization anisotropy of $\mathbf { R e S } _ { 2 }$ and ferroelectric memristive states enables gate-tunable polarization ratios and polarization-resolved learning. Furthermore, the optoelectronic synapse exhibits linear and energy-efficient optical–electrical modulation with 2.0 fJ per event. An ANN built from these synapses achieves 97.33% accuracy in iris recognition under unpolarized light, while a 3×3 FeFET-based CNN performs butterfly classification under polarized illumination through polarization-resolved feature extraction. This work establishes a unified ferroelectric-anisotropic platform for energy-efficient, polarizationresolved neuromorphic vision.

The rapid advancement of artificial intelligence (AI) and machine vision has intensified the demand for energy-efficient and compact computing hardware. Traditional vision systems based

on the von Neumann architecture are constrained by frequent data transfers between physically separated sensing, memory, and computing units, leading to limited energy efficiency and increased system latency1. To overcome these limitations, in-sensor computing, bio-inspired by the retina, has emerged as a promising paradigm by directly integrating these functions within a single platform2. This approach significantly reduces redundant data transfer and enables lowlatency, low-power visual perception3-5. Central to this architecture are optoelectronic synaptic devices, which bridge photodetection and neuromorphic processing by simultaneously sensing, storing, and processing optical inputs6-10. Beyond basic functionalities, neuromorphic vision hardware should also exhibit feature-selective detection to distinguish complex visual patterns.

Achieving efficient in-sensor computing for complex visual tasks requires optoelectronic synaptic devices that combine high responsivity, fast carrier dynamics, non-volatile storage, and polarization sensitivity. Various approaches have been pursued to meet these criteria. Polarizationsensitive operation has been developed using external polarization optical components or materials with intrinsic anisotropy11-13. However, these methods often involve complex architectures and additional structural designs that hinder scalability and reproducibility. Non-volatile optical memory has also been demonstrated through charge-trapping, conductive filament formation, or ferroelectric polarization14-16, yet stability and scalability remain limited. Consequently, realizing compact, energy-efficient, and CMOS-compatible optoelectronic synapses that simultaneously offer polarization sensitivity and non-volatile operation remains challenging.

Ferroelectric field-effect transistors (FeFETs) are promising candidates for optoelectronic memory owing to their non-volatile polarization with superior retention, ultra-fast switching, and tunable memory states17-19. FeFETs have been implemented using various ferroelectric materials, including organic polymers (P(VDF-TrFE)), 2D ferroelectrics like CuInP2S6, and doped HfO2- based dielectrics20-23. Among these, Hf0.5Zr0.5O2 (HZO) offers superior environmental stability and CMOS compatibility, making it ideal for scalable FeFETs in integrated optoelectronic systems24, 25. Integrating HZO-based FeFETs with anisotropic 2D materials such as BP, GeSe, or ReS2 can offer intrinsic anisotropy for polarization sensitivity as well as high detectivity and fast carrier dynamics26-28. Nevertheless, two key challenges remain: mitigating interface effects between the 2D channel and the ferroelectric gate dielectric to improve interfacial stability, and suppressing depolarization fields within the gate stack to maintain stable remanent polarization and long-term data retention.

In this work, we address the challenges of interfacial instability and depolarization by developing a metal-ferroelectric-metal-insulator-semiconductor (MFMIS) FeFET structure that integrates a photosensitive 2D ${ \mathrm { R e S } } _ { 2 }$ channel with a ferroelectric HZO gate dielectric. The floatinggate design effectively decouples the ferroelectric and semiconductor layers, mitigating interfacial coupling and depolarization effects while enabling cooperative modulation of ferroelectric switching and photocarrier trapping. This coupling results in stable memory states, long-term optoelectronic retention, an ultra-low dark current (~100 fA), and high photoresponsivity up to 4 $\times \ 1 0 ^ { 5 } \mathrm { A / W }$ even at zero gate bias. Coupling between the polarization anisotropy of $\mathrm { R e S } _ { 2 }$ and the ferroelectric memristive states allows gate-tunable polarization selectivity and polarizationresolved imaging capable of distinguishing underwater features near the Brewster angle. In addition, dual-mode modulation through electrical gating and optical illumination enables preciseS synaptic weight tuning with ultralow energy consumption of 2.0 fJ per event. An optoelectronic artificial neural network (ANN) achieves 97.33% accuracy in iris recognition under unpolarized R illumination, while a 3×3 FeFET array, coupled with a convolutional neural network (CNN),P performs polarization-resolved butterfly recognition. These results demonstrate ferroelectric–N optical-polarization coupling in optoelectronic synapses and scalable array-level operation, establishing a foundation for large-scale neuromorphic vision hardware. E

# Results

# Polarization-Sensitive Ferroelectric Optoelectronic Synapse for Neuromorphic Vision

The human visual system processes complex optical information through a hierarchical network, where photoreceptors, synapses, and neurons cooperatively extract, encode, and relay visual features to the brain for perception and cognition. Inspired by this biological architecture, we developed a ReS2-based MFMIS FeFET optoelectronic synapse that integrates sensing, memory, and computing within a single device platform. This biomimetic FeFET emulates the early stages of visual perception by directly coupling optical sensing with in-memory computing, thereby enabling efficient feature extraction and adaptive learning. Furthermore, when multiple devices are interconnected into an array, higher-level visual processing becomes possible, laying the foundation for neuromorphic vision hardware.

As illustrated in Fig. 1a, human visual perception of polarized light typically requires external polarization filters such as polarizing glasses, which selectively transmit light oscillations along specific directions. Drawing inspiration from this biological principle, the $\mathrm { R e S } _ { 2 }$ MFMIS FeFET optoelectronic synapse exploits the intrinsic in-plane anisotropy of layered ${ \mathrm { R e S } } _ { 2 }$ to distinguish different polarization orientations without the need for additional optical components. The anisotropic crystal structure enables differential optical absorption along the crystallographic $a \mathrm { - }$ and $b { \mathrm { - a x e s } }$ , allowing the polarization ratio to be dynamically tuned by varying gate voltages or illumination conditions. This intrinsic anisotropy enables polarization-resolved photoresponse, functioning as an integrated input stage for polarization-sensitive visual processing.

Beyond polarization selectivity, the device also emulates the adaptive response of the human retina under different lighting environments. In biological vision, rod cells enhance sensitivity under dim conditions, while cone cells operate in bright conditions to prevent oversaturation. Similarly, in the $\mathrm { R e S } _ { 2 }$ MFMIS FeFET, the ferroelectric polarization of the HZO layer modulates carrier density within the $\mathrm { R e S } _ { 2 }$ channel, enabling light-intensity adaptation. Under positive gate bias, upward polarization induces electron accumulation, enhancing channel conductance and mimicking cone-like photopic operation. Conversely, negative bias drives downward polarization, depleting carriers and amplifying response under weak illumination, resembling rod-like scotopic

adaptation. This ferroelectric-mediated modulation enables the device to sustain a stable and wellbalanced photoresponse across a broad range of illumination intensities.

By integrating the photosensitive ${ \mathrm { R e S } } _ { 2 }$ channel, ferroelectric HZO layer, and floating-gate stack within a single architecture, the device simultaneously achieves optical sensing, nonvolatile memory, and in-situ computing. Upon illumination, photocarriers generated in the ${ \mathrm { R e S } } _ { 2 }$ channel are trapped in the floating gate to enable optical programming, while ferroelectric polarization reversal electrically erases the stored states. This dual-control mechanism allows programmable and nonvolatile modulation of channel conductance, translating optical stimuli such as brightness, polarization, and pulse duration into distinct and nonvolatile conductance states.

Furthermore, as shown in Fig. 1b, when individual FeFET synaptic units are interconnected into a 3×3 array, the incident light passing through a polarizer and a half-wave plate can beS processed directly on-chip. The projected optical signals form an image matrix $I _ { \mathrm { i j } } ,$ which is convolved with programmable kernels to produce output feature maps R $M _ { \mathrm { i j } } .$ . This in-sensor convolution enables the direct extraction of key visual features such as edges and textures at theP hardware level, thereby reducing the computational load on external processors. The intrinsic in-N plane anisotropy of $\mathrm { R e S } _ { 2 }$ provides polarization-resolved optical sensing, while the coupling between ferroelectric and floating-gate ensures nonvolatile retention of the synaptic weights.E Together, these coupled mechanisms enable adaptive and reconfigurable image processing.C Extending this architecture to large-scale arrays paves the way for hardware-implemented visualI recognition systems, showcasing the synergistic interplay among optical input, ferroelectricR plasticity, and neuromorphic computation for energy A -efficient, polarization-resolved vision.

![](images/ce13e08c3ac1874b2f63250ab9b59497036a6f9e824c617fb93e479306ca4135.jpg)  
a

![](images/43f9474c1c363b0ea3e2ff49b87d79b1d221deb357f26a1e2083d9c9303a7ebe.jpg)  
b   
Fig. 1 | Bio-inspired $\mathbf { R e S } _ { 2 }$ MFMIS FeFET optoelectronic synapse integrating sensing, memory, and computing for polarization-resolved neuromorphic vision. a. Bio-inspired polarization-sensitive and light-adaptive mechanism of $\mathrm { R e S } _ { 2 }$ MFMIS FeFET synapse. The intrinsic anisotropy of ${ \mathrm { R e S } } _ { 2 }$ enables polarization-resolved optical sensing analogous to retinal polarized vision, while ferroelectric polarization states modulate the channel response under different illumination levels. Upward and downward polarizations correspond to cone-like

(photopic) and rod-like (scotopic) responses, emulating adaptive visual behavior. Coupled ferroelectric and floating-gate layers enable optical programming and electrical erasing, integrating sensing, memory, and computing for neuromorphic vision. b. The $3 { \times } 3 \ \mathrm { R e S } _ { 2 }$ MFMIS FeFET optoelectronic synapse array for convolutional image preprocessing. Input light patterns are convolved with kernels to extract object features through polarization-sensitive and nonvolatile synaptic modulation.

# Robust Memory Performance of MFMIS ReS2 FeFET

FeFETs have attracted considerable interest due to their inherent nonvolatility, low power consumption, fast switching speed, and non-destructive readout29-32. The non-volatile memory effect in FeFETs arises from the remanent polarization (Pr) of the ferroelectric layer, which is stable and electrically switchable. This polarization modulates the charge carrier concentration in the semiconductor channel, functioning similarly to dynamic doping, thereby altering the channel resistance and enabling bi-stable resistance states essential for memory operations. Additionally, ferroelectric polarization suppresses dark current over extended durations, thereby enhancing the detectivity of optoelectronic devices. Details of the device fabrication process are provided in Supplementary Note 1 and Supplementary Figures 1 to 3. To investigate these properties, we first evaluate the FeFET’s memory behavior under dark conditions.

First, the ferroelectric functionality of the HZO layer was verified using W/HZO/W capacitors, which exhibited stable polarization switching and low leakage, confirming the suitability of the 18 nm HZO film for FeFET integration (Supplementary Figure 4). Building on the confirmed robust ferroelectricity of the HZO layer, a FeFET with an MFMIS structure was fabricated, in which the FG design effectively controlled the area ratio between the ferroelectric and dielectric layers, thereby enhancing the memory window (MW) and extending retention. The FeFET’s electrical performance was systematically assessed under dark conditions to verify its non-volatile memory and synaptic behavior. The $I _ { \mathrm { D S } ^ { - } } V _ { \mathrm { G S } }$ transfer characteristics (Fig. 2a) exhibit a counterclockwise hysteresis loop, consistent with reversible polarization switching. The device maintains a high switching ratio $( > 1 0 ^ { 6 } )$ and a wide MW (~10.5 V) over 100 consecutive cycles at $V _ { \mathrm { D S } } { = } 0 . 1 ~ \mathrm { V } _ { \mathrm { ~ i ~ } }$ , indicating excellent endurance and stability. The large MW enables distinct high and low resistance states, which are crucial for memory state differentiation. The corresponding gate

leakage current over 100 cycles (Supplementary Figure 5) confirms robust gate insulation during repeated switching. Furthermore, the device maintains stable switching across drain biases from 50 mV to 0.5 V (Fig. 2b), indicating robust operation. Retention measurements (Fig. 2c), performed by applying gate voltages of ±7.0 V (100 ms) and tracking IDS over $1 0 ^ { 4 }$ s, demonstrate two well-separated and stable polarization states with negligible degradation, highlighting strong data retention. The enhanced MW provided by the FG structure improves resistance state separation and suppresses disturbance, thereby supporting long-term retention essential for nonvolatile memory applications.

The FeFET’s operational mechanism is illustrated in Fig. 2d and 2e. During programming (Fig. 2d), a positive gate voltage(+VGS) exceeding the coercive voltage (+VC) of the ferroelectric HZO layer switches the polarization upward, leading to electrons accumulating in the ReS2 channel and inducing downward band bending. This reduces the potential barrier and switches the device ON. During erasing (Fig. 2e), a negative gate voltage $( - V _ { \mathrm { G S } } )$ reverses the polarization, depleting electrons and inducing upward band bending, thus increasing the barrier height and turning the device OFF. This reversible modulation of the band profile by ferroelectric switching enables bistable resistance states that can be retained after gate bias removal, ensuring non-volatile storage. Such electric-field-controlled polarization provides a scalable and CMOS-compatible route to high-performance non-volatile memory.

To investigate the mechanisms underlying the enhanced memory window stability in MFMIS FeFETs, we conducted a comparative study with MFIS counterparts fabricated under similar conditions. As detailed in Supplementary Note 2 and Supplementary Figures 6 to 9, key differences arise from voltage distribution, the depolarization field $\left( E \mathrm { d e p } \right)$ , and charge trapping (CT) behavior. In MFIS devices (Supplementary Figure 6), the limited voltage drop across the ferroelectric layer (COX<CFE, AOX/AFE1) and the resulting strong $E _ { \mathrm { d e p } }$ (Supplementary Figure 8a) destabilize the polarization switching, while interface CT further suppresses polarization, leading to the degradation from ferroelectric- to trap-dominated behavior (Supplementary Figure 7). In contrast, the MFMIS structure introduces an FG that decouples the ferroelectric and semiconducting layers, leading to an enlarged AOX/AFE>1, an enhanced voltage drop across the ferroelectric, and reduced $E _ { \mathrm { d e p } }$ (Supplementary Figure 8b)32, thereby enabling sustained and stable switching (Supplementary Figure 9). A concise summary of these structural and operational differences is provided in Supplementary Table 1, while Supplementary Table 2

compares our device with prior Si-based MFS/MFIS FeFETs and ReS2-based optoelectronic devices, highlighting its advantages in both memory and optical performance33-36. Furthermore, the electrical reliability and statistical uniformity of the MFMIS FeFETs were confirmed through cycle-to-cycle (C2C) and device-to-device (D2D) analyses, as presented in Supplementary Note 3 and Supplementary Figures 10 to 13. Consistent counterclockwise hysteresis and minimal parameter variation across repeated cycles and multiple devices demonstrate robust and reproducible switching behavior, which is critical for practical non-volatile memory applications.

Beyond memory storage, the FeFET also demonstrates synaptic behaviors critical to emulating biological neural processes. The excitatory postsynaptic current (EPSC) responses (Fig. 2f) show sustained output across input pulse widths ranging from 100 μs to 100 ms under a fixed VGS of 7.0 V, demonstrating extended temporal retention. Long-term potentiation (LTP), induced by identical +5 V gate pulses with varying pulse widths $( 5 0 \mu \mathrm { s }$ to 1 ms), reveals gradual conductance modulation with reasonably linear trends under shorter pulses (50‒200 μs), as shown in Fig. 2g. However, under longer pulse widths (500 μs and 1 ms), the linearity of conductance updates deteriorates. This degradation is likely due to accelerated charge accumulation or partial saturation of trap states in the FG, which reduces the incremental conductance change per pulse. Despite this nonlinearity at longer durations, the overall conductance evolution remains monotonic and stable, enabling controllable synaptic weight tuning for neuromorphic learning applications. The corresponding fitted results are provided in Supplementary Figure 14. Long-term depression (LTD), triggered by negative pulses of different widths (Fig. 2h), similarly exhibits improved linearity with pulse width adjustment, further supporting the device’s potential for energy-efficient neuromorphic computing. In addition, endurance tests under ±7.0 V, 500 µs pulses over $1 0 ^ { 5 }$ cycles (Fig. 2i) show negligible degradation, confirming excellent long-term reliability. These results highlight the FeFET’s multifunctionality and lay the groundwork for investigating its photoresponsive behavior.

![](images/4070a660d3c9831b72384cf13445f49a4c5a1fde6f17a0f58135bf115ef1fecc.jpg)

![](images/f3131b83541846d448998bddb89b12deed5a2d3c3021899481f84792c1b9956b.jpg)

![](images/df72410fbbe125a6461fa4eba644ee6d2d2d8239aef256b7cd2cd28fe2a253eb.jpg)

![](images/c272b9d0ad45905f46cfe8b1cffb635ff5897e7e72d584aa6895ed69754746a8.jpg)

![](images/7b2b276ed72a3a1967e8ff82739783738060c8b3df70d9f3e0ae09834e21b2c2.jpg)

![](images/898704eceee4a557b79cb3c419d59358309736766cb4ed6d22c37ff82db5af75.jpg)

![](images/48b4d052d8bac44fd35cd07bba921ac761ecfcf7f68415b2f9a205f336ee9e99.jpg)

![](images/2860fda8904b74bb7e937781fff600d72ea0aef39d94264cb99168beccad33df.jpg)

![](images/7ee41e6ed37737cb51978d5e866d67fa9ef4531b880b41d58d5cf597eb1f8722.jpg)  
Fig. 2 | The electrical memory performance of the $\mathbf { R e S } _ { 2 } .$ -based MFMIS FeFET. a. $I _ { \mathrm { D S } ^ { - } } V _ { \mathrm { G S } }$ characteristics exhibit stable counterclockwise hysteresis with a 10.5 V memory window (MW) over 100 cycles at $V _ { \mathrm { D S } } { = } 0 . 1 \mathrm { ~ V }$ . b. $I _ { \mathrm { D S } ^ { - } } V _ { \mathrm { G S } }$ curves at $V _ { \mathrm { D S } }$ from 50 mV to 0.5 V. c. Retention behavior under dark conditions over $1 0 ^ { 4 }$ s. d. Electrical programming $( + V _ { \mathrm { G S } } )$ results in upward polarization and the ON state. e. Electrical erasing $( - V _ { \mathrm { G S } } )$ leads to downward polarization and the OFF state. f. EPSC response under a single gate pulse $( V _ { \mathrm { G S } } { = } 7 . 0 \ : \mathrm { V } )$ with varying pulse widths, showing current retention. $\mathbf { g } .$ LTP behavior under a series of identical $V _ { \mathrm { G S } }$ pulses (5.0 V) with pulse widths of 50 μs to 1 ms. h. LTP is achieved with a +5 V, 100 μs pulse, while LTD is induced by -7 V pulses ranging from 50 to 200 μs. i. Endurance performance under ±7.0 V, 500 μs pulses over $1 0 ^ { 5 }$ cycles.

# High-Performance $\mathbf { R e S } _ { 2 }$ FeFET Photodetector

Photodetectors based on 2D materials often suffer from high dark current and low detectivity, limiting their practical application. A common strategy is to apply a continuous gate voltage, but this increases both power consumption and device complexity. To overcome this limitation, we propose an MFMIS FeFET incorporating a ferroelectric HZO high-κ gate dielectric. The remnant polarization of the ferroelectric layer generates a strong internal electric field, effectively modulating carrier concentration in the 2D ${ \mathrm { R e S } } _ { 2 }$ channel. This built-in field allows dynamic tuning of photoresponse under varying illumination, achieving high sensitivity in the weak-light regime and stable suppression under strong illumination. This enables low-power operation at $V _ { \mathrm { G S } } { = } 0$ , significantly suppressing dark current and enhancing sensitivity without requiring continuous gate bias.

As illustrated in Fig. 3a, the device is designed to operate under 658 nm illumination. Upon exposure, the ${ \mathrm { R e S } } _ { 2 }$ channel absorbs the incident photons and generates electron-hole pairs. These photoexcited carriers are efficiently separated by the external electric field applied between the source and drain, resulting in a measurable photocurrent. The $I _ { \mathrm { D S } ^ { - } } V _ { \mathrm { G S } }$ characteristics of the device under varying light intensities (Fig. 3b, $V _ { \mathrm { D S } } { = } 0 . 1 \ \mathrm { V } )$ reveal a clear modulation of channel conductance with increasing illumination, confirming effective photodetection performance. From the transfer curves, key photodetector metrics, including $I _ { \mathrm { l i g h t } } / I _ { \mathrm { d a r k } }$ and responsivity (R), were extracted (Fig. 3c) at an incident optical power of 63.6 pW. The responsivity is defined $\mathrm { a s } ^ { 3 8 }$ :

$$
R = \frac {I _ {\mathrm {p h}}}{P _ {\mathrm {i n}}} = \frac {I _ {\mathrm {l i g h t}} - I _ {\mathrm {d a r k}}}{p A _ {\mathrm {d}}} \tag {1}
$$

Where $I _ { \mathrm { p h } }$ is the photocurrent $\left( I _ { \mathrm { l i g h t } } – I _ { \mathrm { d a r k } } \right)$ in amperes (A), $P _ { \mathrm { i n } }$ is the incident optical power in watts (W), $p$ is the optical power density $( \mathrm { W } / \mathrm { c m } ^ { 2 } )$ , $A _ { \mathrm { d } }$ is the effective device area $( \mathrm { c m } ^ { 2 } )$ . Notably, the remanent polarization of the ferroelectric layer sustains an internal electric field that maintains carriers in the channel, enabling high responsivity at $V _ { \mathrm { G S } } { = } 0 \mathrm { V }$ without the need for continuous gate voltages, confirming the strong ferroelectric–photoelectric coupling in the device.

To further evaluate the responsivity and detectivity, IDS-VDS measurements were performed (Fig. 3d) after programming the ferroelectric polarization downward to establish the OFF state. Measurements were taken under dark and illuminated conditions at $V _ { \mathrm { G S } } { = } 0 \mathrm { ~ V ~ } ,$ allowing the extraction of $I _ { \mathrm { d a r k } }$ and corresponding $I _ { \mathrm { p h } }$ . The results confirm a strong photoresponse and validate

the device’s capability of gate-free operation. Fig. 3e and 3f depict the programmed statedependent optoelectronic performance of the device, extracted from the IDS-VDS curves after each VGS pulse was applied and subsequently removed. As the magnitude of the programming VGS pulse increases, the responsivity exhibits a consistent improvement, as shown in Fig. 3e, attributed to ferroelectric polarization-induced modulation of the ${ \mathrm { R e S } } _ { 2 }$ channel state. The remnant HZO polarization reduces the depletion and promotes carrier accumulation in the channel, enhancing the separation and collection efficiency of photogenerated carriers.

Another important photodetector metric is detectivity (D*), which evaluates the ability to distinguish weak optical signals from noise. It is commonly calculated by accounting for multiple noise sources, including shot noise, thermal noise, and 1/f noise. The specific detectivity (D*) is defined $\mathrm { a s } ^ { 3 8 }$ :

$$
D ^ {*} = \frac {R \sqrt {A}}{\mathrm {P S D} _ {\text {o v e r a l l}}} = \frac {R \sqrt {A}}{\sqrt {\mathrm {P S D} _ {\text {s h o t}} ^ {2} + \mathrm {P S D} _ {\text {t h e r m a l}} ^ {2} + \mathrm {P S D} _ {1 / f} ^ {2}}} \tag {2}
$$

Where R is the responsivity (A/W), A is the active area (cm2), and $P S D _ { \mathrm { o v e r a l l } }$ is the total noise current density $\left( \mathbf { A \cdot H z } ^ { - 1 / 2 } \right)$ . $D ^ { * }$ is typically expressed in Jones $( \mathrm { c m { \cdot } H z ^ { - 1 / 2 } { \cdot } W ^ { - 1 } } )$ , with higher values indicating better weak-light sensitivity.

In our device, thermal noise is negligible under the operating conditions and was excluded from the calculation. As detailed in Supplementary Note 4 and shown in Supplementary Figures 15 to 19, only shot noise and 1/f noise were considered in $\mathrm { P S D } _ { \mathrm { o v e r a l l } }$ . The device exhibits consistently high responsivity and detectivity across various VGS values under low light intensity. As shown in Fig. 3f, detectivity increases with programming voltage due to enhanced photocurrent, peaking near the coercive voltage. Beyond this point, the accumulation of carriers raises Idark, reducing the signal-to-noise ratio and leading to a drop in $D ^ { * }$ . This nonlinear behavior highlights the importance of tuning ferroelectric polarization for optical detection performance.

To further evaluate the influence of light intensity and gate voltage, Fig. 3g and h present the responsivity and detectivity as functions of incident optical power under different gate voltages $( V _ { \mathrm { D S } } { = } 0 . 1 ~ \mathrm { V } )$ . Both metrics decrease with increasing light intensity, attributed to enhanced carrier recombination at higher photocarrier densities, which reduces lifetime and charge collection efficiency. Notably, as shown in Fig. 3g, after reaching the ferroelectric polarization switching point, the responsivity remains relatively high across the entire power range, with a peak of $4 \times 1 0 ^ { 5 }$

A/W under the lowest incident power. This indicates that the polarization-modulated channel state remains favorable for carrier separation and transport. In contrast, Fig. 3h shows that the detectivity declines after polarization switching. While $D ^ { * }$ initially increases due to enhanced photocurrent, it peaks at $1 . 9 \times 1 0 ^ { 1 4 }$ Jones and then decreases due to increased dark current. These results highlight the FeFET’s strong potential for weak-light detection.

The dependence of responsivity and detectivity on both illumination intensity and gate bias highlights the coupled interplay between photocarrier dynamics and ferroelectric polarization in the ReS2 MFMIS FeFET. Under weak illumination, the device exhibits high responsivity and detectivity, reflecting a rod-like, high-sensitivity regime analogous to scotopic vision. In contrast, under strong illumination, enhanced photocarrier recombination shortens carrier lifetime and reduces optical gain, giving rise to a cone-like, low-sensitivity regime. These light-dependent behaviors are further modulated by gate voltage. A negative $V _ { \mathrm { G } }$ (downward polarization) depletes channel carriers, enhancing sensitivity in weak-light conditions, whereas a positive $V _ { \mathrm { G } }$ (upward polarization) increases carrier density, improving conductance but diminishing gain under intense illumination. The ferroelectric-controlled modulation of the channel state closely emulates the adaptive transition between rod and cone cells in biological vision, enabling dynamic sensitivity adjustment across varying optical environments.

Fig. 3i compares the FeFET’s responsivity and detectivity with other 2D materialsferroelectric photodetectors39-48, demonstrating its superior performance. Detailed comparisons in Supplementary Table 3 further highlight the device’s advantages, including lower dark current and reduced operating voltage, affirming its potential for low-power operation. The transient photoresponse of the FeFET was also characterized (Supplementary Figure 20). Under low optical power, the device exhibits a rapid rise time of 200 $\mu \mathrm { s }$ and a fall time of 1 ms, indicating rapid switching between ON and OFF states in response to optical stimuli. The rapid response is enabled by the efficient photocarrier generation and separation in the $\mathrm { R e S } _ { 2 }$ channel under polarization-induced fields, with minimal trapping, ensuring high-speed operation. These attributes make the FeFET ideal for real-time optical signal processing in energy-efficient applications.

![](images/4455921d0f0fdf713dacd96b3e2e652540600415ffbe2df0ca7e33f782e299a9.jpg)  
a   
b

![](images/f4d336c07887de37776d524975a9432ef8708f188c50dd1561f75de0514bae28.jpg)

![](images/e99e8ab7c848982e5f606327b1396e6ac0d996a3a446cd35f7a56c93d14f10eb.jpg)

![](images/092c36bee0ee52449c1fb5b50d5ef35aa3dd153dcfc71cc4b9f71071353da784.jpg)

![](images/d8a5cffcc9a8a69c4d5cf0e879d72e4645b5c4127cb0d3aea0c700d7f4438bde.jpg)

![](images/10e8b206ab3b240a8ef0f2f6e4675a0b0aceb88fed82d84b569c423bc238cfd7.jpg)

![](images/37dca765b03bb39718e57da79ff8277850d3325f90bd907c85f4f265d6f9bb72.jpg)

![](images/83d4f5c68f68423dc4acd661097cd556e7a8fc076dedbdd3d2ebc3d337cc1c2c.jpg)  
h   
：

![](images/e34917d5fcac172be3a51e81afb6ac5eb1116bddbc8df3baa18e36c41fc2193d.jpg)  
Fig. 3 | Optical detection performance of the FeFETs. a. Schematic illustration of the FeFET under 658 nm illumination. b. $I _ { \mathrm { D S } ^ { - } } V _ { \mathrm { G S } }$ characteristics under varying light intensities. c. Extracted $I _ { \mathrm { l i g h t } } / I _ { \mathrm { d a r k } }$ and responsivity at $6 3 . 6 \mathrm { p W } .$ . d. $I _ { \mathrm { D S } ^ { - } } V _ { \mathrm { D S } }$ curves under different light intensities. e. Responsivity extracted from $I _ { \mathrm { D S } ^ { - } } V _ { \mathrm { D S } }$ curves after applying and removing $V _ { \mathrm { G S } }$ pulses. f. Detectivity extracted from $I _ { \mathrm { D S } ^ { - } } V _ { \mathrm { D S } }$ curves after applying and removing VGS pulses. g. Responsivity under different optical powers and gate voltages at $V _ { \mathrm { D S } } { = } 0 . 1$ V. h. Detectivity under different optical powers and gate voltages at $V _ { \mathrm { D S } } { = } 0 . 1 \ \mathrm { V } .$ i. Comparison with reported 2D materials-based ferroelectric phototransistors39-48.

# Polarization-Sensitive Dual-Mode Programmable Optoelectronic Synapse

Beyond its photodetection capability, the ReS2 MFMIS FeFET functions as a nonvolatile optoelectronic synapse, enabled by ferroelectric polarization–assisted trapping of photocarriers within the floating gate. This coupling mechanism allows optical programming and long-term memory formation, extending device functionality beyond transient photodetection. Furthermore, the intrinsic in-plane anisotropy of layered ReS2 further enables polarization sensitivity, enabling direction-selective encoding of optical inputs. By leveraging the multiple ferroelectric polarization states, the synaptic weights can be precisely modulated, achieving dual-mode programmable plasticity by both optical and electrical stimuli. These synergistic properties establish the ReS2 FeFET as a versatile platform for energy-efficient, polarization-resolved neuromorphic vision systems.

To elucidate these synaptic characteristics, we first examine the device response under optical and electrical stimulation. As illustrated in Fig. 4a, both optical and electrical inputs serve as presynaptic stimuli, while the resulting drain current represents the postsynaptic response. The transition from short-term memory (STM) to long-term memory (LTM) is demonstrated in Fig. 4b, where increasing the number of light pulses from 8 to 128 enhances the excitatory postsynaptic current (EPSC) and prolongs its decay, indicating LTM formation. Analogous to biological vision, the ReS2 FeFET synapse exhibits power-dependent optoelectronic plasticity. As shown in Fig. 4c, higher light intensity leads to larger and more stable EPSC, confirming nonvolatile optical memory. Learning and forgetting behavior is further illustrated in Fig. 4d, where EPSC increases during illumination and partially decays after stimulus removal, followed by rapid recovery upon retraining, mimicking biological relearning and memory consolidation. Frequency-dependent responses (Supplementary Figures 21 and 22) reveal stronger EPSC at higher frequencies due to charge accumulation. This nonvolatile behavior originates from ferroelectric polarization–assisted photocarrier trapping in the floating gate, which stabilizes the channel conductance after light removal and enables optical programming with long-term retention.

Beyond individual optical or electrical modulation, synergistic optoelectronic co-modulation was explored to achieve more precise weight control. As illustrated in Fig. 4e (and schematically in Supplementary Figures 23 and 24), optical pulses induce LTP, while a negative gate bias triggers LTD, enabling linear and reversible conductance modulation through optical

programming and electrical erasing. The energy consumption per synaptic event arises from these two processes. As shown in Supplementary Figure 25, the photoresponse was measured under varying light power (6.36−636.9 pW) and pulse widths $( 2 0 0 \mu \mathrm { s } - 1 \ s )$ . Based on the measured photocurrent and input power, the optical programming energy was estimated to be ⁓1.3 fJ (6.39 pW, 200 µs), while electrical erasing consumed ⁓0.7 fJ, yielding a total of ⁓2.0 fJ per synaptic operation. Detailed calculations are provided in Supplementary Note ${ \pmb 5 } ^ { 4 9 }$ . This ultralow energy compared to previously reported devices (Supplementary Table $4 ) ^ { 5 0 - 5 7 }$ , highlighting the energy efficiency of our design. The device exhibits excellent endurance (Fig. 4f), maintaining a stable memory window and high conductance contrast over $1 0 ^ { 5 }$ optical–electrical program–erase cycles, confirming robust optoelectronic synaptic operation for nonvolatile memory applications.

Beyond dual-mode optoelectronic programmability, the intrinsic in-plane anisotropy of $\mathrm { R e S } _ { 2 }$ introduces an additional degree of freedom for polarization-sensitive learning. The coupling between crystallographic orientation and optical absorption enables direction-dependent modulation of synaptic conductance, extending FeFET functionality from conventional lightinduced memory to polarization-resolved information processing. As shown in Supplementary Figures 26 to 28, only ${ \mathrm { R e S } } _ { 2 }$ , unlike isotropic TMDCs such as $\mathbf { M o S } _ { 2 }$ and $\mathrm { W } \mathbf { S } _ { 2 } ,$ exhibits pronounced anisotropy arising from its distorted 1T' Re-chain structure, which breaks in-plane symmetry and leads to strong angular dependence in the optoelectronic response. Fig. 4g shows that pulsed illumination along the crystallographic a- and b-axes produces a much stronger photocurrent along the b-axis, confirming the anisotropic behavior. This direction selectivity enables encoding of polarization-dependent optical stimuli into synaptic weights, providing a neuromorphic basis for polarization-resolved learning. Fig. 4h further demonstrates coupled modulation by polarization angle and pulse duration, where longer pulses enhance the overall current amplitude, while the polarization angle dictates its periodic variation with a maximum response along the b-axis.

Furthermore, Fig. 4i shows that the polarization-resolved photoresponse of the $\mathrm { R e S } _ { 2 }$ FeFET, revealing the synergistic interplay between the intrinsic anisotropy of ${ \mathrm { R e S } } _ { 2 }$ and the stabilization provided by ferroelectric gating. The polarization ratio (PR, defined as $I _ { \mathrm { m a x } } / I _ { \mathrm { m i n } } )$ plotted as a function of $V _ { \mathrm { G S } }$ shows a wide tunability from approximately 1 to 12, and pronounced enhancement near the ferroelectric-polarized operating points, confirming that ferroelectric gating enhances polarization selectivity. The corresponding polar plot of normalized photocurrent as a function of

polarization angle ( ) exhibits a two-lobed pattern aligned with the crystalline axes, which becomes increasingly asymmetric under ferroelectric modulation, consistent with the observed PR enhancement. The angular data are normalized to highlight relative selectivity rather than absolute current magnitude. This enhancement originates from the remanent polarization of the ferroelectric HZO layer, which establishes a stable electrostatic field that modulates the Fermi level and carrier concentration within the ReS2 channel. Owing to the intrinsic anisotropy of 2D materials such as $\mathrm { R e S } _ { 2 } { } ^ { 5 8 }$ , black phosphorus59, and ${ \mathrm { W T e } } _ { 2 } { } ^ { 6 0 } .$ , the ferroelectric-induced Fermi-level shift affects the $a \mathrm { - }$ and b-axes unequally. As a result, the optical transitions along these directions experience asymmetric filling and screening, leading to differential absorption strength that amplifies the dichroic ratio and maximizes the polarized response along the b-axis. Additionally, the floating gate within the MFMIS stack further stabilizes photocarriers and suppresses dark current, ensuring that the intrinsic anisotropy of ${ \mathrm { R e S } } _ { 2 }$ is more effectively reflected in device-level performance61.

Inspired by the polarization vision of insects, we further simulated a polarization-resolved optical sensing task in a realistic environment. As illustrated in Fig. 4j, the ReS2 FeFET reproduces insect-like polarization vision, where bees and other insects use polarized light for navigation. When light transitions between two media, such as air and water, partial reflection and refraction occur. At a specific angle known as the Brewster angle, the reflected light becomes fully polarized, containing only the polarization component parallel to the incident plane. To emulate this phenomenon, we incorporated a temporal integration step (T, 100 μs–25.6 ms) corresponding to the experimentally measured polarization-resolved learning in Fig. 4h. Electrical output frames were generated under linearly polarized illumination oriented at $0 ^ { \circ }$ and $9 0 ^ { \circ }$ relative to the ReS2 baxis. The $9 0 ^ { \circ }$ channel effectively suppresses surface reflections to enhance underwater contours, while the $0 ^ { \circ }$ channel captures sky patterns and glare. The contrast between these polarization channels enables direction-selective feature recognition, analogous to polarization-based visual processing in biological systems. As the integration time T increases, the image contrast gradually improves, reflecting the cumulative conductance modulation of the ferroelectric ${ \mathrm { R e S } } _ { 2 }$ FeFET. The cooperative interaction between the remanent polarization of HZO and trapped photocarriers in the floating gate stabilizes the channel potential, ensuring long-term plasticity and retention of optical information even after stimulus removal. This temporal integration transforms transient optical inputs into persistent synaptic weights, effectively mimicking biological learning and adaptive perception. Collectively, these results demonstrate that the $\mathrm { R e S } _ { 2 }$ FeFET synapse enables

low-power, polarization-aware computation for bio-inspired imaging and neuromorphic vision systems.

![](images/f30095edbdf9c130de96dd3af903e663820a6ce81a9ee78fd8b497d8b4d1d0a0.jpg)

![](images/ea4735c2840282f7bcef7956f7b4dbd32d6288bf1f85758a9cbca93a4e08e150.jpg)

![](images/ee14486c39ebefaccf4c2be92a0c6d4222e8fc34a780100d90c5512a0d1c3637.jpg)

![](images/f22bf85b993bcabb7f3ef793109137518ffbc46d3fdba36fef681fd1b724f80d.jpg)

![](images/f4fd23a90e1edb9a5b939dfdcf72ae8bf693a22f6239374ed34e227b459b7445.jpg)

![](images/540775ba049e54c88ae27e7be5182359dd8bf9a4adf6e002c0775106999db2de.jpg)

![](images/4b33b54893f34c9f25e8c4f9e226077f58c64485a3aec59e77ddbb761e67b5e1.jpg)

![](images/edbecd5acc255f5b7062ec761d3e1ca30da3407c258a1595321246776c6bae62.jpg)

![](images/5d5385d706ff9ccb269408a4a34f2a38a91f117393b57700d379bdd03fa5fa27.jpg)

![](images/e7fade57a4e64287972449c154bea7fefd7939f311d02390f5ca46165e4918ac.jpg)

![](images/d8a9e461509462635b4929053cd5733700ad1510bf987311b4ea51808236d93b.jpg)  
Repeated Learning   
Time Step   
Fig. 4 | Optoelectronic synaptic and polarization-sensitive behaviors of the FeFET. a. Schematic of an artificial synapse, with gate voltage and light as presynaptic stimuli and the drain current as the postsynaptic response. b. Transition from STM to LTM with increasing number of light pulses (658 nm, 0.5 s, 636.9

pW). c. STM to LTM transition under varying incident optical power. d. Stable photo-induced conductance over repeated light on/off cycles at different intensities. e. Optical LTP and electrical LTD. f. Endurance of repeated optical programming and electrical erasing over $1 0 ^ { 5 }$ cycles. g. Photocurrent evolution under optical programming along the crystallographic a- and b-axes of ${ \mathrm { R e S } } _ { 2 } .$ A significantly higher response is observed along the b-axis, reflecting its intrinsic in-plane anisotropy. The inset shows the $\operatorname { R e S } _ { 2 }$ crystal structure. h. 3D surface plot showing the optically induced channel current enhancement as a function of polarization angle and light pulse width. i. Polarization ratio under varying $V _ { \mathrm { G S } , }$ showing tunability from ~1 to 12. The inset shows the polarization ratio as a function of analyzer angle $( 0 ^ { \circ } - 3 6 0 ^ { \circ } )$ . j. Schematic of polarization-sensitive imaging to distinguish surface reflection and subsurface objects. Time-sequenced images under linear polarization at $0 ^ { \circ }$ (top) and $9 0 ^ { \circ }$ (bottom) relative to the $\operatorname { R e S } _ { 2 }$ b-axis clearly distinguish surface and underwater features.

# Unique Polarization-Sensitive Applications

Having established the ferroelectric-optoelectronic characteristics of the ReS2 FeFETs, we next explore their potential for bio-inspired vision applications. Fig. 5a schematically illustrates the optical signals relevant to natural polarization vision, highlighting the contrast between unpolarized illumination from flowers such as irises and the polarized light used by butterflies for conspecific recognition. In biological vision systems, both unpolarized and polarized light function as complementary optical channels that enhance visual perception. Unpolarized light primarily provides color and intensity contrasts that facilitate floral localization and recognition, whereas polarized light contributes directional cues that enable orientation and species identification, as observed in insect navigation and communication. These natural paradigms motivate the integration of both unpolarized and polarization-sensitive functionalities into our hardware demonstrations, bridging device-level ferroelectric properties with system-level neuromorphic vision capabilities. Inspired by these paradigms, we evaluate two representative scenarios, including unpolarized-light-driven recognition tasks implemented using an ANN and polarizationresolved recognition tasks realized via a CNN based on a 3×3 ReS2 FeFET array.

Fig. 5b illustrates the system architecture and array characterization. Each FeFET synaptic unit functions as an adaptive weight element within the neuromorphic framework, dynamically modulating connection strength in response to optical and electrical stimuli to emulate biological synaptic plasticity. A 3×3 FeFET array (D1–D9) was fabricated, with the fabrication details provided in Supplementary Figure 29. The IDS–VGS characteristics of all nine devices exhibit reproducible switching, confirming excellent uniformity across the array. A comprehensive statistical analysis of key electrical parameters (Vth, ION/IOFF, and MW), presented in Supplementary Figure 30, further demonstrates narrow parameter distributions and high deviceto-device reproducibility. In addition, the optical LTP and electrical LTD measurements over five consecutive cycles demonstrate linear and symmetric conductance modulation. This bidirectional and stable tunability highlights the robustness of the FeFET synapse and its suitability for arraylevel neuromorphic computation.

Based on this architecture, the FeFET synapse was implemented in an optoelectronic ANN for iris species classification under unpolarized light (Fig. 5c). Leveraging the FeFET’s efficient optoelectronic modulation, the ANN consisted of three layers comprising four input neurons, six

hidden neurons, and three output neurons. The network was trained on the standard iris dataset (150 samples evenly divided among Iris setosa, Iris versicolor, and Iris virginica), where four morphological features (sepal length, sepal width, petal length, and petal width) were mapped to the input neurons, and species labels were encoded by the output neurons. Synaptic weights were iteratively updated using the backpropagation algorithm, leading to an increase in classification accuracy from 36.95% to 97.15% within 30 epochs, demonstrating strong learning capability. To establish the correlation between FeFET conductance and ANN synaptic weights, the optical LTP characteristics under different light intensities were normalized and discretized to emulate programmable weight levels. Six representative test cases were further evaluated, each programmed by a distinct light intensity, and achieved an accuracy of approximately 97%, closely matching the software-trained ANN across all cases. The optoelectronic synapse exhibited a minimum effective programming time of ~100 μs, corresponding to the intrinsic ferroelectric– optoelectronic response limit. These results confirm that synaptic weights can be directly encoded through optoelectronic modulation under unpolarized light, thereby enabling high classification accuracy and robust neuromorphic performance.

Furthermore, under polarized illumination, a CNN was implemented using the 3×3 ReS2 FeFET array for polarization-resolved image processing (Fig. 5d). The responsivity–state function R(s,θ), calibrated from experimental measurements of responsivity versus VG_preset and polarization angle, was integrated into a CNN pipeline adapted from prior in-sensor convolution work. Using polarization-resolved butterfly images as input62, the array reproduced orientation-selective feature extraction (vertical, horizontal, and sharpening) and supported polarization-aware kernels through programmable tuning of R for different filters. The optical convolution operation was performed with pulse widths as short as ~200 μs, corresponding to the ferroelectric-gated photoresponse time of the ReS2 channel, which is well matched to biological visual timescales and suitable for polarization-resolved image processing. These results demonstrate that a compact, programmable 3×3 ferroelectric–optoelectronic array can directly implement CNN primitives at the sensory front end, leveraging floating-gate nonvolatility for low-overhead, polarization-resolved neuromorphic vision. The observed orientation-selective recognition behavior mimics the polarization-based visual perception in butterflies, underscoring the potential of this integrated platform for bioinspired, energy-efficient vision hardware that unifies sensing, memory, and computing within a single device framework.

![](images/56f59e8ff16126be897aef975f258f6f7b2a63e72966caa68ef28b0df89ee423.jpg)  
a

![](images/f1f5ee7bb9b6eca10b708185d5d7447c8eae3dbd940c9be624d00f49a61cb971.jpg)  
b

![](images/775b2217a895906aed828589e0b8acd3b4972ad44272c7d596c6ba50ed52eae4.jpg)

![](images/e4c097bd6bdefa318928831110cf1d98ba9261ad96491e963b95656b50d277aa.jpg)

![](images/a5f0e346f7461c2eb4c3f178e799351b61e190ff4418a9a6774392b75832c756.jpg)  
C

![](images/fc35b16010bd5332af91aca77d6ea162a3e74006bbf6955fc9ea6123761ffabf.jpg)

![](images/2dff5ab19976ebf80a8188ad3fd07b3725906c0c28b6e94e51c77d627d166593.jpg)

![](images/b56cbc2c5980e6da7309998c70f799d5c269a9fdcd76afc5d69674f5141bd341.jpg)  
d

![](images/b9cdc93f2a47318afa88134462997310784bb7571731d0259c0dd9492e6766de.jpg)

![](images/63f3e141c8f7fb5007575438b65c602c198490a8cdd1921931a5cad4f6d55b2c.jpg)

![](images/102206809e8cac3112340cca7257c4a079557304b1fb932b32326ef4ef2099ee.jpg)

![](images/e6e457d80af7caafbd0f1d5fe71521e5caf0af41132ea413d935650a144938a8.jpg)  
Fig. 5 | Neuromorphic vision demonstrations based on $\mathbf { R e S } _ { 2 }$ MFMIS FeFETs. a. Schematic of optical stimuli in nature, showing unpolarized light for floral recognition (iris) and polarized light utilized by butterflies for conspecific recognition. The two butterfly polarization images on the right side are reproduced with permission from Springer ${ \mathrm { N a t u r e } } ^ { 6 2 }$ . b. Hardware architecture and array characterization. The left panel shows the schematic of the FeFET array and system wiring layout. The middle panel presents the $3 { \times } 3 \mathrm { R e S } _ { 2 }$ MFMIS FeFET array demonstration, where all nine devices exhibit uniform $I _ { \mathrm { D S } } { - } V _ { \mathrm { G S } }$ characteristics and stable switching behavior. The right panel displays the optical LTP and electrical LTD

synaptic plasticity of the system over successive cycles., c. Under unpolarized illumination, the optoelectronic FeFET-based three-layer ANN for iris classification demonstrates a training accuracy of ~97%, derived from optically programmed synaptic weights. d. Under polarized illumination, a CNN based on the 3×3 ReS2 MFMIS FeFET array performs polarization-resolved convolution on butterfly images across two polarization channels (0° and 90°) using different types of kernels (vertical, horizontal, and sharpen), yielding orientation-selective recognition results and thereby mimicking the polarization-based visual perception behavior of butterflies.

# Discussion

In summary, we demonstrate a high-performance optoelectronic synapse based on a ReS2- based MFMIF FeFET architecture that seamlessly integrates sensing, memory, and computing within a single device platform. Incorporation of a floating-gate structure effectively decouples ferroelectric polarization from the 2D ReS2 channel, yielding a highly stable operation with significantly suppressed dark current, reduced charge scattering, and enhanced photodetection performance. This design supports nonvolatile photo-induced conductance modulation, enabling low-power optoelectronic control of synaptic dynamics. Through the synergistic coupling between ferroelectric polarization and the intrinsic anisotropic optical response of ${ \mathrm { R e S } } _ { 2 }$ , the device exhibits synergistic modulation of polarization selectivity, enabling polarization-resolved imaging. Under unpolarized illumination, a three-layer ANN implemented on this platform achieves 97.33% accuracy for iris recognition. Under polarized illumination, a CNN simulation using a 3×3 FeFET array enables polarization-resolved butterfly recognition, demonstrating hardware-level implementation of polarization-aware perception. Together, these results highlight a scalable and energy-efficient pathway toward large-scale integration of multifunctional ferroelectric– optoelectronic hardware. The ReS2 MFMIS FeFET thus represents a key advance toward realizing bio-inspired, all-in-one neuromorphic vision systems capable of simultaneous sensing, learning, and computation.

# Methods

# HZO MFM Capacitor Fabrication

The 18 nm HZO films were deposited using thermal ALD onto a sputtered 30 nm W bottom electrode. Hf[N- $( \mathrm { C } _ { 2 } \mathrm { H } _ { 5 } ) \mathrm { C H } _ { 3 } ] _ { 4 }$ and $\mathrm { Z r [ N \mathrm { - } ( C _ { 2 } H _ { 5 } ) C H _ { 3 } ] _ { 4 } }$ were used as the metal precursors for hafnium and zirconium, respectively, with nitrogen (N2) as the carrier gas at a flow rate of 250 sccm. Ozone served as the oxygen precursor, delivered with an $\Nu _ { 2 }$ carrier gas at 100 sccm. To induce the ferroelectric phase in the HZO film, a 40 nm W layer was deposited on top of the HZO, followed by rapid thermal annealing at $4 0 0 ^ { \circ } \mathrm { C }$ for 60 seconds. Photolithography and wet etching were then employed to pattern the top W electrode into a $1 0 0 \times 1 0 0 ~ \mu \mathrm { m } ^ { 2 }$ area, completing the formation of the MFM capacitor structure.

# MFMIS FeFET and Array Fabrication

The proposed ReS2-based MFMIS FeFETs were fabricated on $_ { \mathrm { S i O 2 / p - t y p e } }$ Si (100) substrates. The process began with the deposition of a 30 nm W layer via sputtering to serve as the global back gate. An 18 nm HZO film was then deposited on the W back gate layer using the ALD process at $2 8 0 ^ { \circ } \mathrm { C }$ , with the details described above. A 50 nm W layer was subsequently deposited over the HZO and subjected to rapid thermal annealing (RTA) at $4 0 0 ^ { \circ } \mathrm { C }$ for 60 seconds in a nitrogen environment to induce the ferroelectric phase. The W layer was then patterned into an FG using photolithography, followed by wet etching. A 6 nm $\mathrm { H f O } _ { 2 }$ layer was deposited using ALD at $1 5 0 ^ { \circ } \mathrm { C }$ . Few-layer $\mathrm { R e S } _ { 2 }$ flakes were mechanically exfoliated in a glove box and transferred onto the $\mathrm { H f O } _ { 2 }$ surface to prevent oxidation.

For the single FeFET device, after the transfer of the exfoliated $\mathrm { R e S } _ { 2 }$ flake onto the prepatterned substrate, electron-beam lithography (EBL) was employed to define the source and drain regions. Subsequently, a 30/20 nm Ni/Au thin film was deposited by thermal electron-beam evaporation to form the source and drain electrodes. Finally, the PMMA resist was removed using acetone and ethanol, completing the fabrication of the MFMIS FeFET.

For the 3×3 FeFET array, a large-area ${ \mathrm { R e S } } _ { 2 }$ flake was first transferred onto the substrate. EBL was then used to define the active channel regions, followed by reactive ion etching to pattern the ${ \mathrm { R e S } } _ { 2 }$ into individual device islands. Afterward, a second EBL step was performed to define the source and drain electrodes, which were formed by electron-beam evaporation of 30/20 nm Ni/Au,

followed by a lift-off process in acetone. The array fabrication was completed after resist removal and cleaning.

# Electrical and Optical Characteristics

The ferroelectric properties of the HZO-based MFM capacitors were characterized using an aixACCT TF3000 analyzer, which enabled the acquisition of the provided P-V, I-V, and C-V characteristics of the HZO layer. The electrical performance of both the MFM capacitors and FeFET devices, including DC I-V and pulsed I-V measurements, was evaluated using a Keysight B1500A semiconductor analyzer at room temperature. The voltage waveform for pulse I-V measurements was generated by the Keysight B1530, with an integrated waveform generator and fast measurement unit (WGFMU). The optical performance of the device was measured using a Keysight B1500A semiconductor analyzer and a 658 nm laser. The laser supports both internal and external modulation, with the B1500A providing an external trigger to precisely control the optical pulses.

# ANN Simulation Method

The ANN employed in this study features a three-layer architecture comprising four input neurons, six hidden neurons, and three output neurons. The training was performed using the iris dataset, comprising 150 samples evenly distributed across three species: Iris setosa, Iris versicolor, and Iris virginica. Each sample is characterized by four attributes: sepal length, sepal width, petal length, and petal width, corresponding to the input layer of the neural network. The classification task involves mapping the three iris species to the output neurons. Synaptic weights were iteratively adjusted using the backpropagation algorithm, enabling the network to progressively refine its classification accuracy. In the simulation, weight updates were guided by the experimentally observed linearity of optical LTP and electrical LTD characteristics.

# Convolution Image Processing with FeFET

The constant wave (CW) laser in this task expresses the input data (butterfly images) while the gate voltages independently preset the resistance states in the channel. Each cell integrates floating-gate‒stabilized ferroelectric states with the intrinsic polarization sensitivity of anisotropic ReS2, thereby providing both non-volatile weight storage (via preset gate programming) and polarization-dependent responsivity during optical readout. In this scheme, the polarized optical

input encodes local image patches (two polarization channels at $0 ^ { \circ } / 9 0 ^ { \circ } )$ , while the ferroelectric preset voltage $( V _ { \mathrm { G } \_ p r e s e t } )$ defines a responsivity matrix $R { = } \{ R _ { \mathrm { i j } } \}$ that emulates the kernel of the CNN. Once programmed, the array operates without further electrical bias during convolution, relying only on small VDS readout.

For a 3×3 patch with local optical power $P { = } \{ P _ { i j } ( \theta ) \}$ (: polarization angle), the photocurrent response of each device can be expressed as $I _ { i j } { \approx } R _ { i j } ( s _ { i j } , \theta ) { \times } P _ { i j } ( \theta )$ , where $S i j$ denotes the ferroelectric state set by $V _ { \mathrm { G } \_ p r e s e t . }$ . By Kirchhoff’s law, the column current is just the sum of all device currents in that column, $I _ { \mathrm { c o l } } { = } \Sigma _ { j } I _ { i j } { , }$ this realizes the multiply and accumulate (MAC) operation in CNNs. Signed convolutional kernels, such as those used in edge detection, are realized by programming complementary responsivity matrices and subtracting their outputs to represent positive and negative weights. Sliding the 3×3 kernel across an N×N image generates an (N–2)×(N–2) current map corresponding to the feature map of the convolution layer.

# Data Availability

All data supporting the findings of this study are provided in the main text and the Supplementary Information. Source data are provided with this paper.

# Code Availability

The iris flower dataset used for ANN training and evaluation is publicly available and was accessed via scikit-learn63. All codes used for simulations in this study are available from the corresponding authors upon request.

# References

1. Liu, C. et al. Small footprint transistor architecture for photoswitching logic and in situ memory. Nat. Nanotechnol. 14, 662–667 (2019).   
2. Wang, Z., Wan, T., Ma, S. & Chai, Y. Multidimensional vision sensors for information processing. Nat. Nanotechnol. 19, 919–930 (2024).   
3. Zhu, Q.-B. et al. A flexible ultrasensitive optoelectronic sensor array for neuromorphic vision systems. Nat. Commun. 12, 1798 (2021).

4. Tong, L. et al. 2D materials-based homogeneous transistor-memory architecture for neuromorphic hardware. Science 373, 1353–1358 (2021).   
5. Lee, S., Peng, R., Wu, C. & Li, M. Programmable black phosphorus image sensor for broadband optoelectronic edge computing. Nat. Commun. 13, 1485 (2022).   
6. Li, Z. et al. MoS2/ZnO-heterostructured optoelectronic synapse for multiwavelength optical information-based sensing, memory, and processing. Nano Energy 127, 109733 (2024).   
7. Jain, S. et al. Heterogeneous integration of 2D memristor arrays and silicon selectors for compute-in-memory hardware in convolutional neural networks. Nat. Commun. 16, 2719 (2025).   
8. Duong, N. T. et al. Coupled Ferroelectric-Photonic Memory in a Retinomorphic Hardware for In-Sensor Computing. Adv. Sci. 11, 2303447 (2024).   
9. Long, M., Wang, P., Fang, H. & Hu, W. Progress, Challenges, and Opportunities for 2D Material Based Photodetectors. Adv. Funct. Mater. 29, 1803807 (2019).   
10. Ouyang, B. et al. Bioinspired in-sensor spectral adaptation for perceiving spectrally distinctive features. Nat. Electron. 7, 705–713 (2024).   
11. Atalar, O., Van Laer, R., Safavi-Naeini, A. H. & Arbabian, A. Longitudinal piezoelectric resonant photoelastic modulator for efficient intensity modulation at megahertz frequencies. Nat. Commun. 13, 1526 (2022).   
12. Yang, D. et al. High-speed readout for direct light orbital angular momentum photodetector via photoelastic modulation. Adv. Photon. 7, (2025).   
13. Li, X. et al. Review of Anisotropic 2D Materials: Controlled Growth, Optical Anisotropy Modulation, and Photonic Applications. Laser Photonics Rev. 15, (2021).   
14. Sun, Z., Li, J., Liu, C., Yang, S. & Yan, F. Trap-Assisted Charge Storage in Titania Nanocrystals toward Optoelectronic Nonvolatile Memory. Nano Lett. 21, 723–730 (2021).   
15. Wang, Y. et al. MXene-ZnO Memristor for Multimodal In-Sensor Computing. Adv. Funct. Mater. 31, 2100144 (2021).   
16. Wang, P. et al. Integrated In-Memory Sensor and Computing of Artificial Vision Based on Full-vdW Optoelectronic Ferroelectric Field-Effect Transistor. Adv. Sci. 11, 2305679 (2024).   
17. Kim, J. Y., Choi, M.-J. & Jang, H. W. Ferroelectric field effect transistors: Progress and perspective. APL Mater. 9, 021102 (2021).

18. Zhang, Z. et al. A Polarization-Switching, Charge-Trapping, Modulated Arithmetic Logic Unit for In-Memory Computing Based on Ferroelectric Fin Field-Effect Transistors. ACS Appl. Mater. Interfaces 14, 6967–6976 (2022).   
19. Kim, I.-J. & Lee, J.-S. Unlocking large memory windows and 16-level data per cell memory operations in hafnia-based ferroelectric transistors. Sci. Adv. 10, eadn1345 (2024).   
20. Zhao, D., Katsouras, I., Asadi, K., Blom, P. W. M. & De Leeuw, D. M. Switching dynamics in ferroelectric P(VDF-TrFE) thin films. Phys. Rev. B 92, 214115 (2015).   
21. Liu, F. et al. Room-temperature ferroelectricity in CuInP2S6 ultrathin flakes. Nat. Commun. 7, 12357 (2016).   
22. Böscke, T. S., Müller, J., Bräuhaus, D., Schröder, U. & Böttger, U. Ferroelectricity in hafnium oxide thin films. Appl. Phys. Lett. 99, 102903 (2011).   
23. Park, M. H. et al. Ferroelectricity and Antiferroelectricity of Doped Thin HfO2-Based Films. Adv. Mater. 27, 1811–1831 (2015).   
24. Kim, S. J., Mohan, J., Summerfelt, S. R. & Kim, J. Ferroelectric Hf0 $. 5 Z \mathrm { r } 0 . 5 \mathrm { O } 2$ Thin Films: A Review of Recent Advances. JOM 71, 246–255 (2019).   
25. Cheema, S. S. et al. Ultrathin ferroic HfO2–ZrO2 superlattice gate stack for advanced transistors. Nature 604, 65–71 (2022).   
26. Yuan, H. et al. Polarization-sensitive broadband photodetector using a black phosphorus vertical p–n junction. Nat. Nanotechnol. 10, 707–713 (2015).   
27. He, K. et al. Polarization Signal Amplification of 2D GeSe-Based Polarization-Sensitive Photodetectors. Adv. Mater. 37, 2509066 (2025).   
28. Hu, Y. et al. High Performance Balanced Linear Polarization Photodetector Based on 2D ReS2. Laser Photonics Rev. 18, 2400661 (2024).   
29. Kim, J. Y., Choi, M.-J. & Jang, H. W. Ferroelectric field effect transistors: Progress and perspective. APL Mater. 9, 021102 (2021).   
30. Wang, X. et al. Van der Waals engineering of ferroelectric heterostructures for long-retention memory. Nat. Commun. 12, 1109 (2021).   
31. Ning, H. et al. An in-memory computing architecture based on a duplex two-dimensional material structure for in situ machine learning. Nat. Nanotechnol. 18, 493–500 (2023).

32. Xiang, H. et al. Enhancing Memory Window Efficiency of Ferroelectric Transistor for Neuromorphic Computing via Two-Dimensional Materials Integration. Adv. Funct. Mater. 33, 2304657 (2023).   
33. Lee, H. J. et al. Laminated Ferroelectric FET With Large Memory Window and High Reliability. IEEE Trans. Electron Devices 71, 2411–2416 (2024).   
34. Cai, Z., Toprasertpong, K., Liu, Z., Takenaka, M. & Takagi, S. Understanding HZO Thickness Scaling in Si FeFETs: Low Operating Voltage, Fast Wake-Up, and Suppressed Charge Trapping. IEEE Trans. Electron Devices 71, 3633–3639 (2024).   
35. Li, W. et al. The Nonvolatile Memory and Neuromorphic Simulation of ReS2/h-BN/Graphene Floating Gate Devices Under Photoelectrical Hybrid Modulations. Small 20, 2311630 (2024).   
36. Chen, Y. et al. Wrinkled Rhenium Disulfide for Anisotropic Nonvolatile Memory and Multiple Artificial Neuromorphic Synapses. ACS Nano 18, 30871–30883 (2024).   
37. Duan, J. et al. Variation Tolerant and Energy-Efficient Charge Domain Compute-in-Memory Array with Binary and Multi-Level Cell Ferroelectric FET. IEEE Int. Electron Devices Meet. 1–4 (2024).   
38. Wang, F., Zhang, T., Xie, R., Wang, Z. & Hu, W. How to characterize figures of merit of two-dimensional photodetectors. Nat. Commun. 14, 2224 (2023).   
39. Tai, X. et al. High-performance ReS2 photodetectors enhanced by a ferroelectric field and strain field. RSC Adv. 12, 4939–4945 (2022).   
40. Wang, X. et al. Ultrasensitive and Broadband MoS2 Photodetector Driven by Ferroelectrics. Adv. Mater. 27, 6575–6581 (2015).   
41. Wang, X. et al. Multimechanism Synergistic Photodetectors with Ultrabroad Spectrum Response from 375 nm to 10 µm. Adv. Sci. 6, 1901050 (2019).   
42. Wu, G. et al. MoTe2 p-n Homojunctions Defined by Ferroelectric Polarization. Adv. Mater. 32, 1907937 (2020).   
43. Chen, Y. et al. Ferroelectric-tuned van der Waals heterojunction with band alignment evolution. Nat. Commun. 12, 4030 (2021).   
44. Zhang, S. et al. Highly Sensitive InSb Nanosheets Infrared Photodetector Passivated by Ferroelectric Polymer. Adv. Funct. Mater. 30, 2006156 (2020).   
45. Tu, L. et al. Ultrasensitive negative capacitance phototransistors. Nat. Commun. 11, 101 (2020).

46. Meng, G. et al. Polarizable Nonvolatile Ferroelectric Gating in Monolayer MoS2 Phototransistors. ACS Appl. Mater. Interfaces 16, 10316–10324 (2024).   
47. Tan, C., Wu, H., Lin, Z., Yang, L. & Wang, Z. 2D Reconfigurable Memtransistor for High-Performance Dual-Mode Memory and Broadband Photodetection. Adv. Funct. Mater. 35, 2415360 (2025).   
48. Chen, X. et al. Ideal Photodetector Based on WS2/CuInP2S6 Heterostructure by Combining Band Engineering and Ferroelectric Modulation. ACS Appl. Mater. Interfaces 16, 13927– 13937 (2024).   
49. Zhu, C. et al. Optical synaptic devices with ultra-low power consumption for neuromorphic computing. Light: Sci. Appl. 11, 337 (2022).   
50. Bai, J. et al. Full van der Waals Ambipolar Ferroelectric Configurable Optical Hetero-Synapses for In-Sensor Computing. Adv. Mater. 36, 2401060 (2024).   
51. Luo, Z. et al. Artificial Optoelectronic Synapses Based on Ferroelectric Field-Effect Enabled 2D Transition Metal Dichalcogenide Memristive Transistors. ACS Nano 14, 746–754 (2020).   
52. Gao, J. et al. Intrinsic polarization coupling in 2D α-In2Se3 toward artificial synapse with multimode operations. SmartMat 2, 88–98 (2021).   
53. Shang, Z. et al. Ferroelectric Polarization Enhanced Optoelectronic Synaptic Response of a CuInP2S6 Transistor Structure. ACS Nano 18, 30530–30539 (2024).   
54. Dang, Z. et al. Ferroelectric Modulation of ReS2-Based Multifunctional Optoelectronic Neuromorphic Devices for Wavelength-Selective Artificial Visual System. Adv. Funct. Mater. 34, 2400105 (2024).   
55. Zhou, Y. et al. A Reconfigurable Two-WSe2-Transistor Synaptic Cell for Reinforcement Learning. Adv. Mater. 34, 2107754 (2022).   
56. Wang, S. et al. Two-dimensional ferroelectric channel transistors integrating ultra-fast memory and neural computing. Nat. Commun. 12, 53 (2021).   
57. Yan, M. et al. Ferroelectric Synaptic Transistor Network for Associative Memory. Adv. Electron. Mater. 7, 2001276 (2021).   
58. Jiang, J. et al. Chirality-transferred epitaxy of circular polarization-sensitive ReS2 monolayer single crystals. Nat. Commun. 16, 7119 (2025).

59. Xie, L. et al. Nonvolatile Photoelectric Memory Induced by Interfacial Charge at a Ferroelectric PZT-Gated Black Phosphorus Transistor. Adv. Electron. Mater. 5, 1900458 (2019).   
60. Zhou, W. et al. Anomalous and Polarization-Sensitive Photoresponse of Td-WTe2 from Visible to Infrared Light. Adv. Mater. 31, 1804629 (2019).   
61. Wang, J. et al. Electrically Tunable Second Harmonic Generation in Atomically Thin ReS2. ACS Nano 16, 6404–6413 (2022).   
62. Sweeney, A., Jiggins, C. & Johnsen, S. Polarized light as a butterfly mating signal. Nature 423, 31–32 (2003).   
63. Pedregosa, F. et al. Scikit-learn: Machine Learning in Python. J. Mach. Learn. Res. 12, 2825– 2830 (2011).

# Acknowledgments

This work is supported by the National Research Foundation, Prime Minister’s Office, Singapore, under its Competitive Research Program (NRF-CRP24-2020-0002, K.-W.A; NRF-F-CRP-2024-0006, K.-W.A.).

# Author Contributions

J. L. H., J. P. H., and K.-W. A. conceived and designed the experiments. K.-W. A. supervised the project. Device fabrication was carried out by J. L. H., L. Q. L., J. G., T. T. T. T., H. F. Z. and Y. F.S.. J. L. H., J. P. H. and J. P. performed the measurements and simulations. The manuscript was written with contributions from all authors. All authors have reviewed and approved the final version of the manuscript.

# Competing Interests

The authors declare no competing financial or non-financial interests.

# Editor’s Summary

Neuromorphic vision hardware calls for all-in-one integration of photodetection and computing. Huo et al. report an optoelectronic synapse based on a ReS2 channel integrated to a metal– ferroelectric–metal–insulator–semiconductor architecture, showing ultra-low dark current and high photoresponsivity.

Peer review information: Nature Communications thanks Byoung Hun Lee and the other anonymous reviewer(s) for their contribution to the peer review of this work. A peer review file is available.