---
title: "Homogeneous integration of two-dimensional material-based optoelectronic neurons"
date: "2026-01-19"
year: "2026"
journal: "Nature Communications"
doi: "10.1038/s41467-026-68905-3"
abstract: "Dynamic vision processing at the edge requires in-sensor spiking neural"
abstract_cn: "边缘动态视觉处理需要传感器内脉冲神经网络以实现高能效和快速处理。我们展示了基于 MoS2 光电晶体管的光电 LIF 神经元，能够重现关键神经元特性，包括多光谱传感、无电容积分和阈值触发脉冲。此外，我们在单个基底上实现了这些神经元与"
keywords:
  - "[[MoS2]]"
  - "[[HZO]]"
  - "[[optoelectronic leaky integrate-and-fire neuron]]"
  - "[[spiking neural networks]]"
  - "[[in-sensor computing]]"
cite: "[1] Wang J, Liu K, Tiw P J, et al. Homogeneous integration of two-dimensional"
aiSum: "实现 MoS2 光电 LIF 神经元与铁电突触的均匀集成：多光谱传感、无电容积分、阈值触发脉冲，SNN 系统颜色识别 91.7%、目标检测 93.5%"
confidence: "high"
wiki_concepts:
  - "[[HfO2]]"
---

# Homogeneous integration of two-dimensional material-based optoelectronic neurons and ferroelectric synapses for neuromorphic vision

Received: 18 September 2025

Accepted: 19 January 2026

![](images/4db78b77532e9d5033ecf0f35782c1e598e5995298f37b8e326b9e7bd32e5abd.jpg)

Cite this article as: Wang, J., Liu, K., Tiw, P.J. et al. Homogeneous integration of two-dimensional material-based optoelectronic neurons and ferroelectric synapses for neuromorphic vision. Nat Commun (2026). https://doi.org/ 10.1038/s41467-026-68905-3

Jiarong Wang, Keqin Liu, Pek Jun Tiw, Dawei He, Lianfeng Yu, Bowen Wang, Jinxuan Bai, Teng Zhang, Xin Shan, Yang Yang, Yuzhe Wang, Yongsheng Wang, Yaoyu Tao, Xiaoxian Zhang & Yuchao Yang

We are providing an unedited version of this manuscript to give early access to its findings. Before final publication, the manuscript will undergo further editing. Please note there may be errors present which affect the content, and all legal disclaimers apply.

If this paper is publishing under a Transparent Peer Review model then Peer Review reports will publish with the final article.

# Homogeneous integration of two-dimensional material-based optoelectronic neurons and ferroelectric synapses for neuromorphic vision

Jiarong Wang1,2,#, Keqin Liu1,#, Pek Jun Tiw1,#, Dawei He2, Lianfeng Yu1, Bowen Wang1, Jinxuan Bai2, Teng Zhang1, Xin Shan3, Yang Yang1, Yuzhe Wang1, Yongsheng Wang2*, Yaoyu Tao1,4*, Xiaoxian Zhang2*, Yuchao Yang1,3,4,5*

1New Cornerstone Science Laboratory, Beijing Advanced Innovation Center for Integrated Circuits, School of Integrated Circuits, Peking University, Beijing 100871, China   
2Key Laboratory of Luminescence and Optical Information, Ministry of Education, Institute of Optoelectronic Technology, Beijing Jiaotong University, Beijing 100044, China   
3Center for Brain Inspired Intelligence, Chinese Institute for Brain Research (CIBR), Beijing, Beijing 102206, China   
4Center for Brain Inspired Chips, Institute for Artificial Intelligence, Peking University, Beijing 100871, China   
5New Cornerstone Science Laboratory, Guangdong Provincial Key Laboratory of In-Memory Computing Chips, School of Electronic and Computer Engineering, Shenzhen Graduate School, Peking University, Shenzhen 518055, China   
#These authors contributed equally

Corresponding author. E-mail: yuchaoyang@pku.edu.cn; zhxiaoxian@bjtu.edu.cn; taoyaoyutyy@pku.edu.cn; yshwang@bjtu.edu.cn

# Abstract

Dynamic vision processing at the edge requires in-sensor spiking neural networks (SNNs) to achieve high energy efficiency and rapid processing. Although optoelectronic leaky integrate-andfire (LIF) neurons are essential for optical sensing and sparse coding, their practical utility has been hindered by incomplete emulation of biological behaviors and integration difficulties with synaptic devices. Here, we show an optoelectronic LIF neuron based on a MoS2 phototransistor that reproduces key neuronal features, including multispectral sensing, capacitor-less integration, and threshold-triggered spiking. This neuron supports complementary rate and time-to-first-spike coding, enabling versatile visual information processing at the hardware level. Furthermore, we achieve the homogeneous integration of these neurons with MoS2 ferroelectric synapses on a single substrate, unifying volatile optical encoding with non-volatile weight storage. The integrated SNN system attains recognition accuracies of 91.7% for color recognition and 93.5% for object detection, indicating its potential for scalable, high-performance next-generation neuromorphic vision systems.

Keywords: MoS2, HZO, optoelectronic leaky integrate-and-fire neuron, spiking neural networks, in-sensor computing

# Introduction

As the demand for intelligent perception and edge computing continues rise, conventional vision systems based on CMOS sensors are encounter bottlenecks in processing efficiency and energy consumption1, 2, 3, 4. The physical separation of sensing, storage, and computing units requires additional modules, increasing hardware complexity, latency, and power consumption. 5, 6.

To address these limitations, in-sensor neuromorphic computing architectures integrate sensing and preliminary processing functionalities at the sensor level to enable local, real-time preprocessing of input data such as images6, 7, 8, 9. These systems are often tightly coupled with machine learning algorithms to perform tasks like image feature extraction and object recognition at the perception stage, thereby improving system efficiency4, 9, 10, 11. Within this framework, spiking neural networks (SNNs) encode and process image information as spikes, supporting lowenergy time-series information processing12, 13, 14. Two complementary coding strategies, rate coding15, 16, 17, 18 and time-to-first-spike (TTFS) coding12, 19, 20, are commonly adopted, balancing robustness and rapid responsiveness for high-density, efficient information processing.

Structurally, SNNs comprise interconnected neurons and synapses21, 22, 23, among which leaky integrate-and-fire (LIF) neurons stand out for their simplicity, hardware compatibility, and ability to support flexible, sparse, event-driven spike coding 24, 25. In this model, the membrane potential integrates incoming signals and, upon reaching a predefined threshold, triggers an action potential (spike) before resetting to its resting state. Despite their promise, current optoelectronic implementations face technical challenges. Constrained by device architecture, material limitations, or reliance on complex peripheral circuitry, most demonstrations are restricted to basic photocurrent integration21, 22, 23, 26 or oscillation13, 27, 28. Even recent attempts to realize

optoelectronic LIF dynamics remain limited in frequency tunability29, underscoring the challenge of realizing full optoelectronic LIF functionality at the hardware level. In contrast, artificial synapse devices are typically designed to emphasize long-term plasticity30, 31, which conflicts with the short-term dynamic behaviors required for neuronal emulation24, 32, 33. Thus, integrating volatile optical sensing with non-volatile weight storage remains a critical challenge for neuromorphic architectures, as conventional heterogeneous approaches are constrained by material and process incompatibilities, increasing integration complexity and fabrication costs.

MoS2, as a two-dimensional (2D) material, exhibits a pronounced optoelectronic response across the ultraviolet to visible spectrum34, 35, and its optoelectronic synaptic FET features capacitive-free photocurrent accumulation21, 36, which simplifies analog circuit design. Meanwhile, hafnium-zirconium oxide (HZO) retains ferroelectricity even at thickness limits37, 38, 39, offering potential for non-volatile memory. With advances in fabrication techniques, MoS2 demonstrates scalable integration potential40, supporting ferroelectric plasticity in ferroelectric field-effect transistors  (FeFETs) for non-volatile modulation41, 42. Compared with silicon-based materials, MoS2 provides favorable homogeneous integration compatibility, enabling simultaneous optical sensing and ferroelectric storage on a single platform, thereby simplifying device fabrication and reducing complexity and cost.

In this study, we design an optoelectronic LIF neuron based on a MoS2 phototransistor (PT). By introducing a photogenerated charge trapping-detrapping mechanism and a short-circuit discharge pathway, the device emulates key neuronal features: multispectral optical sensing, capacitor-less membrane potential integration, threshold-triggered spiking with automatic reset, and intrinsic stochasticity. In parallel, we develop MoS2 FeFETs as artificial synapses, featuring a tunable memory window and reliable multilevel storage. Building on this, we propose a

homogeneous integration scheme, enabling seamless co-integration of optoelectronic neurons and ferroelectric synapses on a single substrate and streamlining the fabrication process. The resulting SNN system with a complementary coding strategy achieves 91.7% and 93.5% accuracies in color recognition and object detection, respectively, offering an innovative design paradigm for in-sensor neuromorphic computing.

# Results

# Homogeneous integration for neuromorphic computing

To overcome the fundamental bottleneck of conventional architectures in visual information processing, we propose an in-sensor neuromorphic computing architecture, which integrates optical sensing, spike encoding, weight storage, and computation within a homogeneous platform (Figure 1a). In this system, incident light patterns are transformed into spike trains by photoelectronic neurons, which are subsequently processed by synaptic arrays to perform parallel multiply-accumulate (MAC) operations for color recognition and object detection.

We realize this concept through an optoelectronic SNN built on a homogeneously integrated MoS2 platform, consisting of a 1×4 array of PTs and 4×4 FeFETs (Figure 1b). Each PT, coupled with a neuron circuit to reproduce the full dynamics of an optoelectronic LIF neuron, captures and preprocesses multispectral optical signals, converting them into discrete voltage spikes.  Two complementary coding schemes are employed: rate coding and TTFS coding. In rate coding, spike frequency (F) reflects the stimulus intensity, with stronger illumination producing higher spike rates, allowing robust extraction of fine image details. In TTFS coding, stimulus intensity is encoded by the latency of the first spike $( T _ { \mathrm { t r i g g e r } } )$ , with brighter stimuli triggering earlier spike events, allowing faster, energy-efficient detection of sudden or hazardous inputs. Combining these strategies provides a hierarchical balance between fast responsiveness and high-precision recognition within the in-sensor neuromorphic computing architectures.

In parallel, FeFETs act as artificial synaptic units, where gate-controlled polarization switching in the ferroelectric layer allows non-volatile weight storage and plasticity modulation.

Receiving spikes from the optoelectronic neuron, these synapses execute weighted accumulation, supporting in-sensor learning and recognition.

Unlike prior demonstrations that rely on heterogeneous integration, which exhibit material and process incompatibilities that increase complexity and fabrication cost, our framework enables a platform from raw optical input to spike-based neuromorphic computing on a homogeneous material system.

# Optoelectronic neurons using molybdenum disulfide transistor

Figure 2a presents a bio-inspired optoelectronic LIF neuron that emulates the signal processing behavior of the retinal layer. It employs a hybrid architecture consisting of a few-layer MoS2 PT and a neuron circuit, which together convert optical stimuli into spike sequences through a two-stage process of integration and firing to emulate LIF dynamics. During the integration phase, successive light pulses induce a photogating effect that cumulatively increases the channel conductance of the MoS2 PT without requiring a capacitor. The resulting photocurrent $( I _ { \mathrm { p h } } )$ is converted into a rising voltage $( V _ { \mathrm { { m e m b r a n e } } } )$ across a load resistor $( R _ { \mathrm { l } } ) ,$ with a slope correlated with light intensity, thereby mimicking the cumulative response of biological neurons to external stimuli. Once the voltage reaches the predefined threshold of the comparator $\left( V _ { \mathrm { r e f e r e n c e } } \right)$ , the circuit enters the firing phase. The comparator outputs voltage spike while simultaneously triggering two coordinated responses: (1) release of trapped photocarriers to reset the MoS2 PT conductance, simulating the leakage process, and (2) activation of an NMOS transistor to momentarily ground the circuit node, preventing sustained output. A selected high-delay comparator (pulse ${ \mathrm { w i d t h } } > 2 0 0 ~ { \mu \mathrm { s } } )$ facilitates the reset process, enabling stable spike encoding across illumination wavelengths and power levels.

Reliable responsiveness of the PT to diverse optical stimuli is essential for realizing the optoelectronic LIF neuron functionality. It adopts a back-gate configuration and on the same substrate as the FeFET (Supplementary Figure 1), where $\mathrm { { A l } } _ { 2 } \mathrm { { O } } _ { 3 }$ serves as the insulating layer, and Ti/Au electrodes serve as source and drain contacts to reduce contact resistance. Raman spectroscopy reveals the characteristic vibrational modes $( E _ { 2 \mathrm { g } } ^ { 1 }$ and $A _ { 1 \mathrm { g } } )$ of few-layer ${ \mathrm { M o S } } _ { 2 }$ , confirming the layer number and crystalline quality (Supplementary Figure 2a). Photoluminescence (PL) spectroscopy exhibits emission peaks near the direct bandgap transition,

indicating optical quality (Supplementary Figure 2b). Atomic force microscopy (AFM) characterizes the flake thickness and surface morphology, verifying few-layer coverage with minimal roughness (Supplementary Figure 3a). Cross-sectional transmission electron microscopy (TEM) images further elucidate the layered structure and interfaces between MoS2 and the underlying $\mathrm { A l } _ { 2 } \mathrm { O } _ { 3 }$ dielectric, as well as the well-defined multilayer stack of the device architecture (Supplementary Figure 3b).

Additionally, we investigate the optical absorption and photoresponse of few-layer MoS2 PTs to assess their stability for multispectral optical sensing and encoding. Figure 2b shows the optical absorption spectrum of few-layer MoS2, revealing absorption capabilities for red, green, and blue (RGB) light. The inset presents the transfer characteristics of the few-layer MoS2 PT under identical incident power density for RGB illumination (2.0 mW mm-2), confirming its multispectral photoresponse capability. Figure 2c presents the transfer characteristics of the $\mathbf { M o S } _ { 2 }$ PT under 450 nm laser illumination at $V _ { \mathrm { d s } } = 0 . 5 \ : \mathrm { V }$ , showing a negative shift in the threshold voltage as the incident power density rises from 1.0 to 2.0 mW mm-2. This trend, which remains consistent across different wavelengths (Supplementary Figure  4), indicates that stronger illumination enhances the carrier concentration in the MoS2 channel, enabling optical intensity encoding in neuromorphic systems.

Following the characterization of the PT’s photoresponse, Figure 2d demonstrates the dynamic behavior of the optoelectronic LIF neuron system, with the experimental setup shown in Supplementary Figure 5. The dark purple curve illustrates the increase in channel current of the $\mathbf { M o S } _ { 2 }$ PT under periodic optical pulse stimulation, indicating light-induced persistent conductance. The red curve denotes the input voltage to the comparator, analogous to the membrane potential of a biological neuron. As the optical stimulation continues, the membrane potential accumulates

and, upon reaching the predefined threshold voltage $( V _ { \mathrm { r e f e r e n c e } } { = } 0 . 4 5 \mathrm { V } )$ , triggers a neuronal spike output $( V _ { \mathrm { o u t } } )$ . The inset presents a spike with a 6 V amplitude and ~20 μs pulse width. After the spike, the system automatically resets the PT conductance and clears the membrane potential, initiating the next integration cycle. The 6 V pulse amplitude returns the neuron to its baseline state after each spike. The threshold voltage determines the membrane potential at which the neuron fires; a lower threshold results in higher spiking frequency and shorter triggering latency, as shown in Supplementary Figure 6.

Figure 2e presents an energy band diagram illustrating the physical mechanism underlying the persistent photoresponse and conductance reset of the MoS2 PT. When MoS2 is illuminated with light of energy exceeding its bandgap, electrons in the valence band are excited to the conduction band, generating electron-hole pairs. Some of the photogenerated holes are trapped by defect states at the $\mathrm { M o S } _ { 2 } / \mathrm { A l } _ { 2 } \mathrm { O } _ { 3 }$ interface, forming stable positive charges. The trapped charges induce an effective local electrostatic potential near the channel, acting as an additional gate voltage known as the photogating effect. This potential facilitates the accumulation of free electrons and results in a sustained increase in channel conductance, reflecting the persistent photoresponse of the device. Upon applying a positive gate voltage pulse, the external electric field assists in releasing the trapped holes, neutralizing the interface charges and eliminating the photogating effect, restoring the device to its initial state.

Building on the device mechanism and neuron-like spiking behavior, we demonstrate that the optoelectronic LIF neuron encodes multispectral optical signals through two distinct operational regimes: (1) illumination with different wavelengths (450 nm, 520 nm, and 650 nm) at a fixed optical power, and (2) monochromatic illumination at 450 nm with varied optical power.

As shown in Figure 2f, the neuron exhibits distinct characteristics under illumination at 450 nm, 520 nm, and 650 nm wavelengths. Owing to the differences in MoS2 absorption efficiencies at these wavelengths, the effective incident light intensities on the MoS2 PT differ correspondingly, with power densities of 1.6, 3.5, and 2.7 mW mm-2, respectively. Figure 2g presents the corresponding rate and TTFS encoding results, achieving selective encoding and recognition of RGB optical stimuli.

Furthermore, to investigate the neuron’s dynamic behavior under light intensity modulation, we evaluated the rate and TTFS encoding behaviors under 450 nm monochromatic illumination, increasing the laser power density from 0.8 to 1.8 mW mm-2 (Figure 2h). The neuron exhibits evolution of  F and $T _ { \mathrm { t r i g g e r } }$ with increasing optical power, indicating that its spiking behavior varies by light intensity (Figure 2i). Unlike oscillatory neurons, which are limited in coding flexibility and energy efficiency, LIF neurons enable temporal integration and sparse spike coding, suitable for optoelectronic implementations.

Critically, both spike frequency and triggering latency are primarily determined by the photocurrent levels of the MoS2 PT. The ability to distinguish these photocurrent levels across the two encoding regimes is essential. As shown in Supplementary Figure  7, the device exhibits distinct photocurrent levels under these conditions. In addition, Supplementary Figure 8 shows the temporal evolution of the membrane potential under RGB color stimuli and varying 450 nm light intensities, confirming the neuron's multispectral responsiveness and optical intensity modulation capability. Notably, the fluctuation of the charge trapping and detrapping during accumulation and reset processes provides inherent stochasticity, which mimics the stochastic firing in biological neurons.

# Synaptic ferroelectric field effect transistors

Synaptic plasticity, the activity-dependent modulation of synaptic strength, underlies learning and memory in the brain and is essential for artificial neuromorphic systems. Here, we present a FeFET with a layered metal-ferroelectric-metal-insulator-semiconductor (MFMIS) structure composed of TiN, HZO, ${ \bf A l } _ { 2 } { \bf O } _ { 3 }$ , and MoS2 (Figure 3a) to emulate synaptic behavior. The bottom TiN layer serves as the control gate, which, together with the HZO layer and the intermediate TiN floating gate, forms a ferroelectric capacitor structure that decouples the ferroelectric layer from the insulating layer. The $\mathrm { A l } _ { 2 } \mathrm { O } _ { 3 }$ layer functions as an insulating buffer, facilitating stable modulation of channel conductance. Ti/Au electrodes provide work function alignment with MoS2, reducing contact resistance. Input spikes are applied to the drain, while the source outputs the corresponding current spikes, mimicking pre-synaptic stimulation and post-synaptic responses.

Figure 3b presents the cross-sectional TEM image of the FeFET, revealing a multilayer structure. The accompanying energy-dispersive spectroscopy (EDS) elemental mapping confirms the spatial distribution of constituent elements, validating the structural integrity. The highresolution transmission electron microscopy (HRTEM) image of the HZO ferroelectric layer, shown in Figure 3c, reveals its polycrystalline nature. Further elemental composition analysis (Supplementary Figure 9 and Supplementary Table 1) indicates a Zr:Hf ratio of approximately 0.56:0.44. The polarization-voltage (P-V) curve (Supplementary Figure 10) exhibits ferroelectric behavior, with a coercive voltage (??c) of ~2.1 V and a remnant polarization (??r) of ~14.9 μC cm-2, confirming robust polarization switching.

The MFMIS structure offers an additional advantage through tunable voltage distribution between the ferroelectric and insulating layers. In this architecture, the bottom metal-ferroelectricmetal (MFM) stack and the top metal-insulator-semiconductor (MIS) stack act as two series

capacitors, enabling precise modulation of the voltage drop across the ferroelectric layer by adjusting the area ratio between the MIS and MFM regions. Both vertically stacked43, 44 and nonvertically stacked24, 42 FeFETs with MFMIS structures demonstrates robust storage performance. The non-vertical stacking is selected due to its flexibility in device design, facilitating control over the area ratio between the MIS and MFM regions. As shown in the fabricated structures with AFE/ADE ratios varying from 1.5 to 0.2 (Supplementary Figure 11), the memory window broadens with a decreasing ratio (Figure 3d), owing to the amplified voltage across the ferroelectric layer that promotes efficient polarization switching.

Moreover, the high-quality insulator/semiconductor interface suppresses polarization screening effects induced by interface traps. The counterclockwise hysteresis observed in the transfer curve verifies the ferroelectric modulation characteristics of the device (Figure 3d). For comparison, devices based on conventional metal-ferroelectric-semiconductor (MFS) and metalferroelectric-insulator-semiconductor  (MFIS) structures exhibit clockwise hysteresis loops (Supplementary Figures 12 and 13), consistent with the analysis in Supplementary Note 1, which shows that interface traps and suboptimal voltage distribution can suppress ferroelectric behavior.

The broadened memory window and right-shifted threshold voltage facilitate lower channel conductance under zero bias, which decreases the device current and energy consumption during MAC operations. The output curves measured across different conductance states (Figure 3e) show a near-linear I-V relationship within a low bias range (0 to 1 V), indicating that the device functions as a tunable resistor. This enables FeFETs to serve as MAC units in SNNs, encoding synaptic weights as conductance values while input signals are summed via Ohmic conduction.

The operational mechanism of the FeFET is illustrated in Figure 3d and 3f from the bandstructure perspective. Under a positive gate bias, polarization in the HZO layer aligns toward the

channel, and the resulting charges, transmitted through the TiN floating gate, modulate the Al2O3/MoS2 interface to induce electron accumulation. This accumulation bends the MoS2 bands downward, shifting the conduction band edge closer to the Fermi level, and increasing carrier density, attaining a high-conductance state. Conversely, a negative gate bias reverses the polarization toward the gate electrode, forming a depletion region at the Al2O3/MoS2 interface. The MoS2 bands then bend upward, moving the conduction band edge away from the Fermi level, and reducing carrier density, switching the device to a low-conductance state. Due to the nonvolatile nature of ferroelectric polarization, both the polarization and the corresponding conductance state persist after the removal of the gate voltage, enabling nonvolatile data storage.

Notably, polycrystalline HZO consists of multiple ferroelectric domains whose domain wall motion requires a finite voltage threshold and exhibits statistical variability, resulting in multi-level polarization switching. As a result, the device operates beyond binary 0 and 1 state: intermediate gate biases between the coercive and saturation voltages partially switch domains, generating multiple polarization states and corresponding conductance levels, emulating synaptic plasticity.

Due to the non-uniformity of the ferroelectric polarization switching process45, programming strategies relying solely on fixed amplitudes or extended pulse widths lead to non-linear conductance updates (Supplementary Figure 14). Figure 3h demonstrates that FeFET conductance varies in response to pulse amplitude modulation, leading to relatively linear long-term potentiation (LTP) and long-term depression (LTD) behaviors, with the detailed programming conditions presented in Supplementary Figure 15. The device operates across 50 discrete conductance states, with a dynamic range of ~8× between the highest and lowest conductance values. Retention measurements (Figure 3i) confirm maintenance of states for over 100 s under zero bias, and endurance tests (Figure 3j) show conductance modulation over 5000 pulses across

50 full LTP/LTD cycles. The cycle-to-cycle (C2C) variation, ranges from 0.34% to 2.1%

(Supplementary Figure 16), supporting its use for synaptic emulation in neuromorphic systems.

# Molybdenum disulfide neuron and synapse array

After validating the functions and operating mechanisms of the MoS2-based optoelectronic LIF neuron and ferroelectric synapse, we demonstrate homogeneous integration of the hybrid 2D array. By incorporating a neuron circuit implemented on a printed circuit board (PCB), we constructed a neuron-synapse integrated architecture for optoelectronic SNNs. In Figure 4a, external optical pulses are first detected by the PT array and subsequently converted into encoded spike signals via the neuron circuit. To match the operating range of the FeFETs, a resistive voltage divider is used at the output stage of the neuron circuit to regulate the pulse voltage (Supplementary Figure 17). These encoded spikes are then fed into the ferroelectric synapse array to perform MAC operations, thereby enabling in-sensor neuromorphic computing.

Figure 4b details the layout of the optoelectronic LIF neurons and ferroelectric synapses, showing the interconnection scheme between the PTs and FeFETs. Optical microscopy images of the fabricated 1×4 MoS2 PT array and 4×4 FeFET array are shown in Figure 4c, demonstrating the practicable high-density homogeneous integration within a single material platform. Figure 4d presents the electrical performance of representative devices within the arrays, showing device-todevice (D2D) variations in $V _ { \mathrm { t h } }$ of ~7.7% for the 16 FeFETs and ~12.7% for the 4 PTs (Supplementary Figure 18).

Furthermore, the MAC functionality of the ferroelectric synapse array is demonstrated to assess its neuromorphic computing potential. As depicted in Figure 4e, four input spike trains are applied to a column of the synapse array, with each synapse programmed to a weight to perform the accumulation operation described by:

$$
I _ {\mathrm {n}} = \sum_ {\mathrm {m} = 1} ^ {4} V _ {\mathrm {m}} G _ {\mathrm {m n}} \tag {1}
$$

, where $I _ { \mathrm { n } }$ is the MAC output, $V _ { m }$ is the input voltage (0.5 V), and $G _ { m n }$ represents the synaptic weight (conductance). The spike trains are temporally superimposed and integrated to produce output sequences, preserving both the temporal dynamics of the inputs and the weighted accumulation outcomes.

In rate coding, information is conveyed through the firing frequency of spikes, with higher frequencies corresponding to denser spike trains. The MAC operation performs weighted accumulation of these spikes, producing output sequences that reflect the integrated effect of input signals. In TTFS coding, information is represented by the triggering timing of spikes. During the MAC operation, TTFS-encoded spike trains are accumulated according to their arrival times, generating output spike sequences while preserving temporal order.

Overall, the MAC operation outputs a spatially weighted spike sequence, which is then fed into the postsynaptic neuron. The neuron performs membrane potential integration temporally, completing computation that incorporates both TTFS and rate-coded information. Since the MAC operation conducts weighted summation of the spikes, the resulting output sequence encapsulates the integrated effect of input signals. By modulating the spike frequency and synaptic weights, the aggregated input information is encoded (Supplementary Figure 19).

Additionally, statistical analysis of the 4×4 FeFET array conductance distribution is presented via the cumulative distribution function (CDF) in Supplementary Figure 20. All 16 devices operate between $0 . 2 \mu \mathrm { S }$ and 1.3 μS, achieving 16 conductance levels. This demonstrates the multilevel tunability of the synaptic array, providing robust hardware support for precise weight mapping in neuromorphic systems. Compared with prior works (Supplementary Table 2 and Supplementary Note 2), we not only fully implemented the complete functionality of optoelectronic LIF neurons, but also proposed a homogeneous integration strategy for neurons and synapses.

Given current hardware limitations, we validate the system’s capability for spike-based RGB color classification via simulation (Figure 4g, Methods). Unlike conventional SNN models, our system features device-level spectral selectivity, enabling independent encoding of RGB signals via the wavelength-dependent response of optoelectronic LIF neurons. This approach offers a hardware pathway for in-situ color image processing within SNNs. During simulation, RGB patterns are input into the optoelectronic LIF neuron array for spike encoding, and then transmitted through a fully connected (FC) layer based on our ferroelectric synapse array for MAC operations. The summed currents serve as input signals to the output layer of the SNN. Ultimately, the system achieves a classification accuracy of 91.7% for RGB color patterns (Figure 4h) and demonstrates the ability to distinguish multiple wavelengths, particularly the RGB colors (Supplementary Figure 21). These results demonstrate our integrated neuron-synapse platform for hardware-level color recognition.

Furthermore, extending this approach to the infrared spectral range enables broader-band visual perception and higher-dimensional scene understanding. 2D material systems such as InSe, black phosphorus, narrow-bandgap chalcogenides (e.g., Bi2Te3-Sb2Te3), and MoTe2/WSe2 heterostructures exhibit broadband photoresponse performance across the visible to mid-infrared range46, 47. Compared with silicon-based materials, these narrow-bandgap or heterojunction 2D materials offer efficient light absorption and charge separation. Therefore, replacing the MoS2 channel used in this study with such materials broadens broaden the spectral coverage and enhances the dimensionality of optical sensing and neural encoding.

# Optoelectronic neural networks for object detection

Beyond color detection, the integrated MoS2 system is deployed for tasks of higher complexity, such as machine vision in assisted driving, where differentiating between multiple road hazards in complex and noisy backgrounds is essential for decision-making. In such a system, acquired road scene images are encoded into spikes by the bio-inspired optoelectronic LIF neurons and processed by the ferroelectric synaptic array using MAC operations. We demonstrate the potential of the system by performing object detection within road scenes using the Karlsruhe object detection dataset48 (Methods). As shown in Figure 5a, the optoelectronic LIF neuron encodes grayscale pixel values, which correspond to light intensity ?? ranging from 1 mW mm2 to 1.8 mW:

$$
T _ {\text {t r i g g e r}} = a _ {0} \ln \left(\frac {P}{P - b _ {0}}\right) \tag {2}
$$

$$
F = a _ {1} (P - b _ {1}) ^ {2} + c _ {1} \tag {3}
$$

, where $\mathtt { a } _ { 0 }$ , $\mathsf { b } _ { 0 } ,$ $\mathsf { a } _ { 1 }$ , $\mathsf { b } _ { 1 }$ , and $c _ { 1 }$ are constant parameters. TTFS coding enables computation at short latencies and is crucial for quick system response to road conditions, while rate coding enables robustness to noise. Subsequently, the spike-encoded images are processed by a spike-elementwise (SEW) ResNet18 modle49 modified to accommodate our road scene object detection task (Figure 5b). Each convolution (Conv) layer is followed by an integrate-and-fire layer serving as the nonlinear activation. Details regarding the network and its training are provided in the Methods section.

Figure 5c illustrates the evolution of selected 7×7 Conv kernel weights over training epochs. After 411 epochs, the weights stabilize, revealing distinct edge-detection patterns (horizontal, vertical, and so forth), indicating that the network extracts directional features from spike-encoded

inputs to enhance recognition. Figure 5d presents the 2×2 confusion matrices for vehicle and pedestrian recognition, where the horizontal and vertical axes represent the actual and predicted labels, respectively. The matrices show classification performance with high accuracy. Figure 5e shows the accuracy and loss evolution during training, with the model achieving an accuracy of 93.5% on the test set. The training can be found in Supplementary Figure 22, which provides the accuracy performance on the training set. Figure 5f shows representative detection results in road scenes, including identification of individual vehicles, co-occurring vehicles and people, and people alone, validating the system’s efficient multi-object detection capability.

We quantitatively compare the neuron-synapse array with commercial neuromorphic chips and representative neuromorphic systems (Supplementary Tables 3 and  4). Relative to these mature platforms, this architecture offers advantages in optoelectronic fusion and circuit simplification, though system scale and energy efficiency remain areas for improvement. Supplementary Note 3 and Supplementary Discussion provide analyses regarding the potential and limitations of 2D material-based neuromorphic devices.

Overall, these results demonstrate the integration of bio-inspired spike encoding using optoelectronic LIF neurons with the MAC operations of the ferroelectric synapse array. This integration enables real-time visual perception and processing, establishing a foundation for neuromorphic vision systems.

# Discussion

In conclusion, we introduce a bio-inspired optoelectronic LIF neuron based on a MoS2 PT that reproduces neuronal behaviors, such as multispectral optical sensing, capacitor-less membrane potential integration, threshold-triggered spiking with automatic reset, and intrinsic stochasticity. We further construct artificial synapses based on $\mathbf { M o S } _ { 2 }$ FeFET that support energy-efficient MAC operations. Through a homogeneous integration strategy combining PTs and FeFETs, we realize a scalable neuron-synapse array for optoelectronic SNNs. The integrated system supports complementary coding and achieves recognition accuracies of 91.7% and 93.5% in color recognition and object detection tasks, respectively, establishing a versatile platform for advanced neuromorphic vision systems.

# Methods

# Fabrication of devices and array

Device fabrication began with the sputtering and patterning of a 30 nm TiN layer on a $\mathrm { S i } / \mathrm { S i O } _ { 2 }$ substrate to serve as the bottom electrode. An 18 nm HZO film was subsequently deposited by atomic layer deposition (ALD) at $2 5 0 ^ { \circ } \mathrm { C }$ . A second 30 nm TiN layer was then sputtered and patterned, followed by rapid thermal annealing at $5 5 0 ~ ^ { \circ } \mathrm { C }$ for 60 s to crystallize the film. On this layer, a 30 nm Ti/Au electrode was defined by photolithography and deposited by electron-beam evaporation to serve as the gate electrode of the PT. A 10 nm $\mathrm { { A l } } _ { 2 } \mathrm { { O } } _ { 3 }$ insulating layer was subsequently grown by ALD at $1 5 0 ^ { \circ } \mathrm { C }$ . Selected regions of the $\mathrm { A l } _ { 2 } \mathrm { O } _ { 3 }$ and HZO films were removed by photolithography and inductively coupled plasma (ICP) etching, thereby exposing the underlying TiN and Ti/Au electrodes. Few-layer $\mathbf { M o S } _ { 2 }$ flakes, mechanically exfoliated from bulk crystals, were transferred onto the substrate. Finally, source and drain electrodes were patterned by electron-beam lithography, followed by the deposition of a 90 nm Ti/Au layer and a standard lift-off process.

For FeFET array fabrication, minor modifications were introduced to prevent short-circuiting between source and drain electrodes. Following ICP etching, a 30 nm Ti/Au electrode layer was patterned and deposited adjacent to the array. An 8 nm $\mathrm { H f O } _ { 2 }$ layer was then patterned and deposited by ALD to electrically isolate the source and drain lines. Thereafter, $\mathbf { M o S } _ { 2 }$ flakes were exfoliated and transferred, followed by the deposition of contact electrodes and lift-off.

# Device characterization

Electrical measurements were conducted on a Signatone probe station equipped with an Agilent B1500A semiconductor parameter analyzer. Optoelectronic measurements were carried

out on the same platform using lasers at 450, 520, and 650 nm, with signals recorded on a Keysight DSOS404A digital storage oscilloscope.

# Material characterization

Raman and PL spectra of exfoliated MoS2 flakes on $\mathrm { S i O } _ { 2 }$ substrates were acquired using a LabRAM HR800 system (Horiba Jobin Yvon) with a 532 nm excitation laser. Absorption spectra were measured using an Excipolar Trion absorption spectrometer with a white light source. TEM images and EDS elemental maps of MoS2 devices were obtained using a dual-beam focused ion beam (FIB) system (FEI Helios NanoLab 600i) equipped with an Oxford X-MaxN 80 EDS detector. Cross-sectional TEM samples were prepared by FIB, and high-resolution imaging was conducted using an ex situ TEM (Talos F200e, Thermo-fisher) operated at 200 kV. Surface morphology was characterized using AFM (Bruker Dimension Icon) in PeakForce Tapping mode with a ScanAsyst-Air probe.

# Color recognition

The 4×4 patterns of the digits 0, 1, 4, and 7 were generated using red, green, and blue colors, forming a dataset has a size of 12. After color-sensitive spike encoding, the corresponding spike trains were fed into a 16×3 feed-forward SNN. For the detection of multiple combinations of RGB colors (red, green, blue, yellow, cyan, magenta, white), the dataset has a size of 28 and the network has a size of 48×7.The SNN was implemented using PyTorch and SpikingJelly50. To train the network, an inverse tangent surrogate function (Equation 4) was employed for back-propagation through time51, where LTP corresponded to weight increases induced by positive gradients of the loss, while LTD corresponded to weight decreases induced by negative gradients.

$$
f (x) = \frac {1}{\pi^ {2}} \arctan (\pi x) \tag {4}
$$

The output neuron with the highest spiking frequency was taken as the classification result. Thus, the loss function was defined by the mean square error between the output spiking frequency and the target spiking frequency of each output neuron.

# Object detection

The dataset A of the Karlsruhe Dataset : Labeled Objects (Cars and Pedestrians)48 was used, which contained 775 positive images with either cars, pedestrians, or both, and 1, 155 negative images with no objects. The images were resized to 344×100. The dataset was randomly split into a train subset and a test subset of sizes 1, 575 and 355, respectively. During training, image augmentation techniques including random rotation, horizontal flip, brightness adjustments, contrast adjustments, and MixUp were applied on-the-fly. In addition, after spike encoding of the image, spike time jitter was applied to further enhance the robustness of the system.

The SEW ResNet18 was also implemented using PyTorch and SpikingJelly50. To accommodate our task demonstration, the input Conv layer was modified to accept a singlechannel grayscale image, and the size of the output FC layer was set to 2. A dropout layer was added before the final FC layer. Pre-trained weights were not loaded and the network was trained from scratch. The inverse tangent surrogate function (Equation  4) was also used for backpropagation51. To enable the simultaneous detection of objects from multiple classes per input sample, binary cross-entropy losses were calculated for each output class. The total accuracy represented the average performance over all input samples. To obtain the final performance, all weights were quantized and mapped into differential 4-bit conductances supported by our

ferroelectric synapse (Figure 4f). The mapping scale layer was determined by the maximum absolute value within each layer.

# Data availability

The Source Data generated in this study have been deposited in the figshare database under accession code (https://doi.org/10.6084/m9.figshare.31037746).

# Code availability

All the codes used for the simulations are publicly available on GitHub at https://github.com/pekjuntiw/mos2-neuromorphic-vision.

# References

1. Dodda A, Trainor N, Redwing JM, Das S. All-in-one, bio-inspired, and low-power crypto engines for near-sensor security based on two-dimensional memtransistors. Nat. Commun.13, 3587 (2022).   
2. Merolla PA, et al. A million spiking-neuron integrated circuit with a scalable communication network and interface. Science 345, 668-673 (2014).   
3. Sebastian A, Le Gallo M, Khaddam-Aljameh R, Eleftheriou E. Memory devices and applications for in-memory computing. Nat. Nanotechnol. 15, 529-544 (2020).   
4. Seo S, et al. Artificial optic-neural synapse for colored and color-mixed pattern recognition. Nat. Commun. 9, 5106 (2018).   
5. Zhou F, Chai Y. Near-sensor and in-sensor computing. Nat. Electron. 3, 664-671 (2020).   
6. Mennel L, Symonowicz J, Wachter S, Polyushkin DK, Molina-Mendoza AJ, Mueller T. Ultrafast machine vision with 2D material neural network image sensors. Nature 579, 62- 66 (2020).   
7. Kyuma K, Lange E, Ohta J, Hermanns A, Banish B, Oita M. Artificial retinas  — fast, versatile image processors. Nature 372, 197-198 (1994).   
8. Zhou F, et al. Optoelectronic resistive random access memory for neuromorphic vision sensors. Nat. Nanotechnol. 14, 776-782 (2019).   
9. Yang Y, et al. In-sensor dynamic computing for intelligent machine vision. Nat. Electron. 7, 225-233 (2024).   
10. Zhang Z, Wang S, Liu C, Xie R, Hu W, Zhou P. All-in-one two-dimensional retinomorphic hardware device for motion detection and recognition. Nat. Nanotechnol. 17, 27-32 (2022).   
11. Pi L, et al. Broadband convolutional processing using band-alignment-tunable heterostructures. Nat. Electron. 5, 248-254 (2022).   
12. Li F, et al. An artificial visual neuron with multiplexed rate and time-to-first-spike coding. Nat. Commun. 15, 3689 (2024).

13. Dang B, Zhang T, Wu X, Liu K, Huang R, Yang Y. Reconfigurable in-sensor processing based on a multi-phototransistor–one-memristor array. Nat. Electron. 7, 991-1003 (2024).   
14. Zhou Y, et al. Computational event-driven vision sensors for in-sensor spiking neural networks. Nat. Electron. 6, 870-878 (2023).   
15. Wu Q, et al. Spike Encoding with Optic Sensory Neurons Enable a Pulse Coupled Neural Network for Ultraviolet Image Segmentation. Nano Lett. 20, 8015-8023 (2020).   
16. Li F, et al. A Skin-Inspired Artificial Mechanoreceptor for Tactile Enhancement and Integration. ACS Nano 15, 16422-16431 (2021).   
17. Wang R, et al. 1-Phototransistor-1-Threshold Switching Optoelectronic Neuron for In-Sensor Compression via Spiking Neuron Network. In: 2023 International Electron Devices Meeting (IEDM)) (2023).   
18. Zhang X, et al. Experimental Demonstration of Conversion-Based SNNs with 1T1R Mott Neurons for Neuromorphic Inference. In: 2019 IEEE International Electron Devices Meeting (IEDM)) (2019).   
19. Subbulakshmi Radhakrishnan S, et al. A Sparse and Spike-Timing-Based Adaptive Photoencoder for Augmenting Machine Vision for Spiking Neural Networks. Adv. Mater. 34, 2202535 (2022).   
20. Su X, et al. Integrating Image Perception and Time-to-First-Spike Coding in MoS2 Phototransistors for Spiking Neural Network. Adv. Funct. Mater. 34, 2315323 (2024).   
21. Chen J, et al. Optoelectronic graded neurons for bioinspired in-sensor motion perception. Nat. Nanotechnol. 18, 882-888 (2023).   
22. Cao R, et al. Compact artificial neuron based on anti-ferroelectric transistor. Nat. Commun.13, 7018 (2022).   
23. Sun C, et al. Novel a-IGZO Anti-Ferroelectric FET LIF Neuron with Co-Integrated Ferroelectric FET Synapse for Spiking Neural Networks. In: 2022 International Electron Devices Meeting (IEDM)) (2022).

24. Gao J, et al. Reconfigurable neuromorphic functions in antiferroelectric transistors through coupled polarization switching and charge trapping dynamics. Nat. Commun.16, 4368 (2025).   
25. Yuan R, et al. A neuromorphic physiological signal processing system based on VO2 memristor for next-generation human-machine interface. Nat. Commun. 14, 3695 (2023).   
26. Luo X, et al. The Optical-Electronic Integrated Spiking Neurons Based on Antiferroelectric Thin-Film Transistors. IEEE Trans. Electron Devices 71, 6442-6447 (2024).   
27. Wang X, et al. Vertically integrated spiking cone photoreceptor arrays for color perception. Nat. Commun. 14, 3444 (2023).   
28. Nath SK, et al. Optically Tunable Electrical Oscillations in Oxide-Based Memristors for Neuromorphic Computing. Adv. Mater. 36, 2400904 (2024).   
29. Xu J, et al. High-order dynamics in an ultra-adaptive neuromorphic vision device. Nat. Nanotechnol. 20, 1419–1430 (2025).   
30. Won UY, et al. Multi-neuron connection using multi-terminal floating–gate memristor for unsupervised learning. Nat. Commun. 14, 3070 (2023).   
31. Liu K, et al. An optoelectronic synapse based on α-In2Se3 with controllable temporal dynamics for multimode and multiscale reservoir computing. Nat. Electron. 5, 761-773 (2022).   
32. Syed GS, Zhou Y, Warner J, Bhaskaran H. Atomically thin optomemristive feedback neurons. Nat. Nanotechnol. 18, 1036-1043 (2023).   
33. Wang Y, et al. A biologically inspired artificial neuron with intrinsic plasticity based on monolayer molybdenum disulfide. Nat. Electron. 8, 680–688 (2025).   
34. Lopez-Sanchez O, Lembke D, Kayci M, Radenovic A, Kis A. Ultrasensitive photodetectors based on monolayer MoS2. Nat. Nanotechnol. 8, 497-501 (2013).   
35. Yoon HH, et al. Miniaturized spectrometers with a tunable van der Waals junction. Science 378, 296-299 (2022).

36. Liao F, et al. Bioinspired in-sensor visual adaptation for accurate perception. Nat. Electron. 5, 84-91 (2022).   
37. Müller J, et al. Ferroelectricity in Simple Binary ZrO2 and HfO2. Nano Lett. 12, 4318-4323 (2012).   
38. Cheema SS, et al. Enhanced ferroelectricity in ultrathin films grown directly on silicon. Nature 580, 478-482 (2020).   
39. Cheema SS, et al. Emergent ferroelectricity in subnanometer binary oxide films on silicon. Science 376, 648-652 (2022).   
40. Jayachandran D, et al. Three-dimensional integration of two-dimensional field-effect transistors. Nature 625, 276-281 (2024).   
41. Si M, et al. Steep-slope hysteresis-free negative capacitance MoS2 transistors. Nat. Nanotechnol. 13, 24-28 (2018).   
42. Ning H, et al. An in-memory computing architecture based on a duplex two-dimensional material structure for in situ machine learning. Nat. Nanotechnol. 18, 493-500 (2023).   
43. Zhao R, et al. Reconfigurable aJ-Level Ferroelectric Transistor-Based Boolean Logic for Logic-in-Memory. Nano Lett. 24, 10957-10963 (2024).   
44. Lu T, et al. Two-dimensional fully ferroelectric-gated hybrid computing-in-memory hardware for high-precision and energy-efficient dynamic tracking. Sci. Adv. 10, eadp0174.   
45. Jerry M, et al. Ferroelectric FET analog synapse for acceleration of deep neural network training. In: 2017 IEEE International Electron Devices Meeting (IEDM)) (2017).   
46. Wang H, et al. Superlattice Engineering on 2D Bi2Te3-Sb2Te3 Chalcogenides. Adv. Sci. 12, 2503492 (2025).   
47. Gou G, et al. Broadband Visual Information Processing with 2D Materials. Small. 2504001 (2025).   
48. Geiger A, Wojek C, Urtasun R. Joint 3D Estimation of Objects and Scene Layout. In Advances in Neural Information Processing Systems vol. 24 (Curran Associates, Inc., 2011).

49. Fang W, yu Z, Chen Y, Huang T, Masquelier T, Tian Y. Deep Residual Learning in Spiking Neural Networks. In Advances in Neural Information Processing Systems vol. 34 21056– 21069 (Curran Associates, Inc., 2021).   
50. Fang W, et al. SpikingJelly: An open-source machine learning infrastructure platform for spike-based intelligence. Sci. Adv. 9, eadi1480.   
51. Neftci EO, Mostafa H, Zenke F. Surrogate Gradient Learning in Spiking Neural Networks: Bringing the Power of Gradient-Based Optimization to Spiking Neural Networks. IEEE Signal Process. Mag. 36, 51-63 (2019).

# Acknowledgments

This work has been supported by the National Key R&D Program of China (2023YFB4502200), Guangdong Provincial Key Laboratory of In-Memory Computing Chips (2024B1212020002), Shenzhen Science and Technology Program (JCYJ20241202125907011), Beijing Natural Science Foundation (L234026, L257010), National Natural Science Foundation of China (62374014, 92164302), and Financial Support for Outstanding scientific and technological innovation Talents Training Fund in Shenzhen. This work has been supported by the New Cornerstone Science Foundation. We acknowledge BioRender.com for helping us to create Figures. 2a, 3a.

# Author Contributions Statement

J. W., K. L., and P. T. contributed equally to this work. J. W., K. L., and P. J. T. designed the entire concept and experiment. Y. W., Y. T., X. Z., and Y.C. Y. supervised the whole project. J. W. fabricated the MoS2-based devices and array. J. W., L. Y., and B. W. designed and built neuron circuits. J. W., J. B., X. S., Y. Y., Y. W., and T. Z. performed electrical measurements and related data analyses. J. W. and P. T. performed the software simulations. J. W., D. H., Y. W., X. Z., Y. T., and Y.C. Y. contributed to the discussion and data analysis. J. W., X. Z., and Y.C. Y. prepared the manuscript with input from all authors. All authors analyzed the results and implications and commented on the manuscript at all stages.

# Competing Interests Statement

The authors declare no competing interests.

# Figure Captions

Fig. 1 MoS2-based in-sensor neuromorphic computing architecture. (a) Schematic of the insensor neuromorphic computing architecture with integrated optical sensing (red–green–blue, RGB), spike encoding, weight storage, and computation. $I _ { \mathrm { n } , }$ output current the MAC operation; $V _ { \mathrm { m } } .$ , input voltage; $G _ { \mathrm { m n } }$ , programmed conductance. (b) Integrated MoS2-based spiking neural network (SNN) hardware comprising a 2D array of phototransistors (PTs) and ferroelectric field-effect transistors (FeFETs). PTs are coupled with neuron circuits to emulate optoelectronic leaky integrate-and-fire (LIF) neurons, while FeFETs act as artificial synapses with non-volatile weight storage and plasticity. $V ,$ membrane potential; $G ,$ programmed conductance; $T ,$ time.

# Fig. 2 Neuromorphic optical sensing and spike encoding in a $\mathbf { M _ { 0 } S _ { 2 } } – \mathbf { b _ { \lambda } } \mathbf { a s e d }$ optoelectronic LIF

neuron. (a) Schematic of a bio-inspired optoelectronic LIF neuron mimicking retinal signal processing. The system integrates a few-layer MoS2 PT and a neuron circuit to convert light stimuli into voltage spikes via a two-stage integration and firing process. $V _ { \mathrm { d d } } .$ supply voltage of the $\mathrm { P T } ;$ ; $\boldsymbol { I _ { \mathrm { o u t } } }$ , output current of $\mathrm { P T } ;$ ;  Vreference, predefined threshold voltage of comparator (CMP); $V _ { \mathrm { s u p p l y } }$ , supply voltage of CMP; $V _ { \mathrm { o u t } }$ , output voltage of CMP. (b) Broadband optical absorption of fewlayer MoS2 with RGB transfer curves (inset). ${ \cal I } _ { \mathrm { d s , } }$ channel current of PT; $V _ { \mathrm { g } } ,$ gate voltage of PT. (c) Transfer curves of the $\mathbf { M o S } _ { 2 }$ PT under 450 nm illumination at increasing power densities $( P )$ , showing a negative threshold voltage shift. (d) Dynamic behavior of the optoelectronic LIF neuron under optical pulse input. The $\mathbf { M o S } _ { 2 }$ channel current and membrane potential (Vmembrane) increase until the threshold is reached, triggering a voltage spike (Inset: 6 V amplitude, ${ \sim } 2 0 \mu \mathrm { s }$ pulse width). (e) Energy band diagram of the photogating effect. Illumination generates trapped holes at the $\mathrm { M o S } _ { 2 } / \mathrm { A l } _ { 2 } \mathrm { O } _ { 3 }$ interface, inducing a persistent increase in channel conductance. $E _ { \mathrm { c , } }$ conduction band minimum; $E _ { \mathrm { v } } ,$ , valence band maximum; $E _ { \mathrm { f } } ,$ Fermi level. (f) Spike response under RGB illumination (450, 520, 650 nm). (g) Rate and TTFS encoding results for RGB light, showing wavelengthdependent encoding. (h) Spike response under increasing 450 nm light power density. (i) Spike frequency (F) and the latency of the first spike $( T _ { \mathrm { t r i g g e r } } )$ as a function of power density, showing tunable spiking behavior. The retinal illustration in Figure 2a was created in BioRender. Wang, J. (2026) https://BioRender.com/52jtpav.

Fig. 3 MoS2 FeFET with synaptic plasticity based on an MFMIS architecture. (a) Schematic of the FeFET with an MFMIS structure, illustrating the tunable ferroelectric-to-dielectric area ratio and its emulation of synaptic plasticity, pre-synaptic stimulation, and post-synaptic responses. (b) Cross-sectional TEM image and corresponding EDS elemental mapping of the device, showing uniform layer stacking and well-defined interfaces. Scale bar, 20nm. (c) HRTEM image of the polycrystalline HZO ferroelectric layer. Scale bar, 3nm. (d) Transfer curve of the FeFET with varying AFE/ADE ratios, showing enhanced memory window and counterclockwise hysteresis loop. $I _ { \mathrm { d s } , }$ channel current of FeFET; $V _ { \mathrm { g } } ,$ gate voltage of FeFET; ADE, area of MIS stack; $A _ { \mathrm { F E } , }$ area of MFM stack. (e) Output curve at different conductance states, indicating near-linear I-V behavior suitable for multiply-accumulate (MAC) operations. $V _ { \mathrm { d s } } ,$ , drain-source voltage of FeFET. (f) and (g) Energy band diagrams illustrating band modulation under opposite polarization states. Positive gate bias induces electron accumulation and downward band bending, while negative bias induces depletion and upward band bending. $E _ { \mathrm { c , } }$ conduction band minimum; $E _ { \mathrm { v _ { \mathrm { i } } } }$ , valence band maximum; $E _ { \mathrm { f } } ,$ Fermi level. (h) LTP/LTD behaviors programmed by varying pulse amplitudes, demonstrating 50 discrete conductance states.  Gmax,  maximum programmed conductance; $G _ { \mathrm { m i n . } }$ , minimum programmed conductance. (i) Retention performance of the FeFET, showing stable maintenance of 50 discrete conductance states over 100 s under zero-bias conditions. (j) Endurance performance of the FeFET over 5,000 consecutive pulses, demonstrating stable and repeatable LTP/LTD cycles for synaptic emulation. $C _ { \mathrm { v } }$ _max, maximum coefficient of variation; $C _ { \mathrm { v } }$ _min, minimum coefficient of variation. The synapse illustration in Figure  3a was created in BioRender. Wang, J. (2026) https://BioRender.com/6o0xxu3.

Fig. 4 Co-integrated MoS2-based neuron-synapse array for optoelectronic spiking neural networks (SNNs). (a) Schematic of the neuron-synapse integrated system, comprising a MoS2 phototransistors (PTs) array, a printed circuit board (PCB)-based neuron circuit, and a ferroelectric field-effect transistors (FeFETs) array. (b) Structural layout and interconnection scheme of the 1×4 PT array and $4 { \times } 4$ ferroelectric FeFET array. SL, source line; DL, drain line. (c) Optical microscopy images of the fabricated 1×4 PT array and the 4×4 FeFET array. Scale bars, 50 μm (left) and 20 μm (right panels). (d) D2D variation, showing ~12.7% and ~7.7% variations in threshold voltage (Vth) for the 4 PTs and the 16 FeFETs, respectively. $I _ { \mathrm { d s } , }$ channel current; $V _ { \mathrm { g } , }$ gate voltage. (e) MAC operation in the ferroelectric synapse array with rate and TTFS Coding. $I _ { \mathrm { n } , }$ , output current; $V _ { \mathrm { m } } .$ , input voltage; $G _ { \mathrm { m n } }$ , programmed conductance;  T, time. (f) Schematic of red-green-blue (RGB) image classification using RGB-resolved spike encoding and MAC in the system. (g) Classification accuracy of 91.7% for RGB patterns via simulation using the hardware-defined SNN framework.

Fig. 5 Object  detection in  assisted  driving  scenarios  using optoelectronic SNN. (a) Spike encoding strategies, time-to-first-spike (TTFS) and rate coding are based on the response of our device to optical power density (P). F, spike frequency; Ttrigger, the latency of the first spike; a0, b0, a1, b1, and c1 are constant parameters. (b) Schematic of the spike-element-wise (SEW) ResNet1849 used for road scene objects. The input images are first encoded into spike trains and then fed into the SEW ResNet18 model. Residual connections are employed between the convolutional (conv) layers. Subsequently, the features are passed through an average pooling (Avg pool) layer before entering the fully connected (FC) layer, which utilizes a sigmoid activation function for classification. (c) Evolution of selected 7×7 Conv kernel weights for edge detection after 411 epochs. (d) $2 \times 2$ confusion matrices for vehicle and person recognition. Tneg, target negative; Tpos, target positive; $P _ { \mathrm { n e g , } }$ prediction negative; $P _ { \mathrm { p o s } , }$ prediction positive. (e) Accuracy and loss evolution during training, achieving 93.5% accuracy on the test set. (f) Representative detection results in road scenes, including individual vehicles, co-occurring vehicles and people, and people alone. The original road scene images in Figure 5a and 5f are Sourced from the Karlsruhe Object Detection Dataset48, used under CC BY-NC-SA 3.0 (https://creativecommons.org/licenses/by-ncsa/3.0/). No changes were made to the original images.

# Editor’s summary:

Integrating volatile optical sensing with non-volatile memory is crucial for neuromorphic vision applications. Wang et al. propose a homogeneous integration scheme that combines optoelectronic neurons and ferroelectric synapses on a single substrate for color recognition and object detection tasks.

Peer review information: Nature Communications thanks Qingjiang Li and the other anonymous reviewer(s) for their contribution to the peer review of this work. A peer review file is available.

![](images/3f05666ec494f8a17a3ed685a8d954905b205948ee3c486efa5401e5c1117d6a.jpg)  
a

![](images/c35e6b7300115f51bc642ffdb4c944798f51c0df4995fc77c286bf9b213f839e.jpg)

![](images/a36a9f5e7cf0c6211f69eaf63ae922a34a05f6e371b5fdf9f90060cdb8e75d8a.jpg)  
PT neuron

![](images/cb6a6d8d93525d31d881e65f4845c6d8ec2298d2767884716e96f51df761dbfe.jpg)  
Full LIF neuronal dynamics emulation & spike encoding

![](images/69d8fdd69ff63359e2cd3fd0ac13eaad9169c4b0f2b672c4456885c52572bb9c.jpg)  
FeFET synapse

![](images/3d7d5b88aeaaf355319dc7bac2c4b69e292f95ac35b86eb0bc59fc0777bfd319.jpg)  
Optoelectronic SNN   
In-sensor In-se nsor ning & recognitionnin g reco gnitio n

![](images/8bbc26bbab5eb63ca7f03e639d8a76c56e825b2b2c305ef91d66362952310e30.jpg)  
a

![](images/bd9190ef3da7975224243ec0236967c348db4a6e7cc14fac7c81816d1a487d11.jpg)

![](images/ffe5d4a42c45be99b790a820c97e3064ae7bd02c283114ebfc3f788b1c716d1c.jpg)

![](images/0c05455def8e1c31bc8e3c03283073b6bb7fea53c494a08a3e504546eccdde14.jpg)

![](images/c3a0ebac1174ab59f8e6b6db127bdb5d54a9395578d3fb910f3fb86922496f15.jpg)  
d

![](images/3b9702868612f0c24257bf829e211fe185b64bb0cdf59e0c9776becb434942f9.jpg)

![](images/13232fd57115a240cd58ef111f5045a4ea1f0ae1d5c75d45b135b4c79c5c979c.jpg)  
f

![](images/49a413c6baf43cf135738995a66569301397402524bf372820a23946a3c7ba7f.jpg)  
g

![](images/092f7d297c2896ba2a0afd383a29e95c2a963d4132f129266c18261c20195da2.jpg)  
h

![](images/209fbbc4e96d5364d0ecaa235ea0833d21249139c3bd75bebf68da4a0a349b96.jpg)  
i

![](images/323351373cf2569c40a3ffd77a626173fca4d92c040d7e9b443c0584f75697a9.jpg)

![](images/b3df2735aa58e16fa53badf8b07a97e30867905a9695934675711073b5818662.jpg)

![](images/00580277eca41c4a8c9d1d90b5231a84b959420537903aebd4c24f5824875e03.jpg)

![](images/664be1dc09a26e207826cb1aa3c0af110f0ccd02ed3dd53b53469a78de66ffd1.jpg)

![](images/cf06500cf80e61279a34dac86708ac06261bd5efb4d2040161ba1459459c6855.jpg)

![](images/3fc6afa78c4b6cf1ae8400248c4e64648b5ca290a586de7178de808eb748dc69.jpg)

![](images/f0e9db96e58f4492e857be01c360b328e0f214bf379977f19d6cb0ac092032d0.jpg)

![](images/eae3569fb75c20a2bdc66d02eb3b9b67255f9de22c1f4fc3f6aa63dc209973da.jpg)

![](images/f8a2604341cad90448df8eb9cfc7eed675bd1c99e3ffaabba204672f5bb4734e.jpg)

![](images/be5e95e5aea74501da56083f5c781f519105113c3b0ad1cdeabc3da301a2947c.jpg)

![](images/3ee1d50d3c8d23ba740900bfac2f30fd7022976efb7df40786e38ffd0daeba95.jpg)  
a   
b

![](images/4a9257620a47d0613478225ecd9673f3269d060a7d770d49ef3f92e443c83520.jpg)

![](images/1bc99d05722b90185d8ad3157eb1824f5e3212f23dd9999aa0281d730e58ca34.jpg)  
c

![](images/0a64389cde512d5a5f2f09c9441f468e85cf615a86ae9be49c4f68ddfd2570f9.jpg)  
d

![](images/7d4b89d3f7b868f56ad3290d160b3553dd59cb7f06f733a958157e1e83b84a68.jpg)

![](images/f2de5efc683102e639ba0ab513360eccc991785b951c6e73bbd3e991f00809b4.jpg)

![](images/aa05e4f546316095d3c9ecb31ff22e7a4a6eb7795f677eec821940c661b5d868.jpg)  
f

![](images/fca72d31b776ebba402b33aefe1a5199472362f4f2383029ef7db313144018af.jpg)  
g

![](images/c9e20a71d468b0f1f18f15639f78416c2671f9182cd8431cbf2c0890efac7168.jpg)

![](images/30d7624f3d66cced9786452640f323b010fbdaec377188953047593df7ba863a.jpg)

![](images/0742fd2317afebfa4127566bd6b15bc9f623055ff28a0eece53be930e39c38de.jpg)

![](images/e347ab17d77b79a25183c54c1d9d777f13ad20571649a6352aacf35650615eb8.jpg)  
Image input   
b   
7×7 conv   
64 filters

![](images/5b32eb2fe84c03c60a974e8de4367c280dc56ec05ea8466f3b1ee38949f11cdb.jpg)  
f   
c

![](images/0a2e8c0f3a79ab811b392fac42b956cd5c7e3db350d5fc9706854786791a98ae.jpg)

![](images/fb62bef0ba2a9c29bfbbd5bc0c2b0922480bd7e9967fb33b29fa6ccb2cbc9404.jpg)

![](images/4a9ded5b5e170f4631e8df0b349267f7cae41afad69862b4197e96035cbedc8f.jpg)

![](images/1c9c62c9215832269c3ffa5459565b7aad1c90b5f6752a11828a7a5e7310b8c4.jpg)

![](images/066dbe37c7f07545524796701112b679567997e7cd6a44706f438aa6a545d5f2.jpg)

![](images/8c01406ba0370495a31ef0d7ce42787fd7d527898dbe327b7122644b5a9cbc9b.jpg)

![](images/a8ff9318723b945da2b66d8dd6600e9f13ad0730b0b4012bfdd5d35bc8558c1d.jpg)

![](images/e06e75109bc89d6291f3a263a153420ffb96de155e7956acda2fa1e37f1cc5bc.jpg)