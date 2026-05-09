---
title: "Reconfigurable Ferroelectric Devices for Neuromorphic Computing"
authors:
  - "Tae Hyun Yoon"
  - "Jin Yong An"
  - "Yeon Ho Kim"
  - "Woong Huh"
  - "Jaeho Lee"
  - "Sungmin Park"
  - "Bong Gi Lim"
  - "Donghui Kang"
  - "Sangcheon Park"
  - "Chul-Ho Lee"
date: "2026-01-01"
year: 2026
journal: "Advanced Materials"
abstract: "Reviews reconfigurable ferroelectric devices for neuromorphic computing"
abstract_cn: "综述用于神经形态计算应用的可重构铁电器件。讨论用于突触可塑性的铁电极化切换、多功能器件设计和硬件实现策略。"
keywords:
  - "[[2D ferroelectric semiconductor]]"
  - "[[neuromorphic vision sensor]]"
  - "[[schottky photodiode]]"
cite: "Yoon, Author. Reconfigurable Ferroelectric Devices for Neuromorphic Computing[J]."
aiSum: "可重构铁电器件综述：极化切换突触可塑性、多功能设计、硬件实现策略。"
confidence: "high"
---

# RESEARCH ARTICLE

# Reconfigurable Vertical [[schottky photodiode]]s Based on Ferroelectric 2D Semiconductors for Perceptual-Precision, Context-Aware Neuromorphic Vision

Tae Hyun Yoon1,2 Jin Yong An2,3 Yeon Ho Kim1,2 Woong Huh3 Jaeho Lee1,2 Sungmin Park1,2 Bong Gi Lim1 Donghui Kang1 Sangcheon Park1 Chul-Ho Lee1,2

1 Department of Electrical and Computer Engineering, Seoul National University, Seoul, Republic of Korea 2Inter-University Semiconductor Research Center (ISRC), Seoul National University, Seoul, Republic of Korea 3KU-KIST Graduate School of Converging Science & Technology Korea University, Seoul, Republic of Korea

Correspondence: Chul-Ho Lee (chulholee@snu.ac.kr)

Received: 27 October 2%2& Revised: & January 2%26 Accepted: 1& January 2%26

Keywords: [[2D ferroelectric semiconductor]] | [[neuromorphic vision sensor]] | [[schottky photodiode]]

# ABSTRACT

To realize in-memory sensing and computing platforms, it is essential to integrate sensing, computation, and memory functionalities within a single device, enabling energy- and time-efficient vision systems with high perceptual precision. However, achieving such multi-functional processing capability within a compact device structure remains a major challenge. Here, a reconfigurable vertical photodiode based on α-In Se is presented, a ferroelectric 2D semiconductor. Gradual and reversible modulation of built-in electric fields at the top and bottom Schottky junctions is achieved through partial out-ofplane polarization switching of α-In Se , enabling multi-level, non-volatile, and polarity-tunable photoresponsivity. This allows analog programmability with a high degree of freedom in processing within a two-terminal metal-ferroelectric semiconductormetal (MFsM) structure, effectively resolving trade-off between structural compactness and computing versatility. Leveraging these intrinsic characteristics, we demonstrate a versatile sensor-level perceptual processing framework using a reconfigurable photodiode crossbar array. By exploiting the high-density spatial integration capability, the system adaptively configures its spatial support to prioritize either suppressing environmental noise for robust feature extraction or preserving fine-grained details for precise classification, depending on the task requirements. These results lay the foundation for highly scalable and energy-efficient neuromorphic vision system with high perceptual precision.

# 1 Introduction

With the rapid growth of the Internet of Things (IoT) and edge computing, efficient visual perception has become a core requirement for numerous data-driven, latency-sensitive applications such as autonomous driving, robotics, and edge artificial intelligence [1–&]. The human visual system, composed of the

retina and visual cortex, has long served as a model for such efficiency due to its seamless integration of sensing, memory, and computation within a highly parallel neural networks [&–(]. Within this functionally integrated architecture, neurons communicate through synapses whose weights modulate and store input–output relationships, enabling the retina to capture optical stimuli and, in coordination with the visual cortex, perform early

Tae Hyun Yoon and Jin Yong An contributed equally to this work.

© 2%26 Wiley-VCH GmbH

![](images/5bcd29832e695e3db58d8f2dce0a126ddabb76f9fb7aacddb6c1e3a55847d007.jpg)  
a

![](images/f89854d037552eb2d36d0219d92d00963867c0f68b2f14923f9c170301d96e80.jpg)  
b

![](images/d6be9d5ecbc5087b0be12179cd9f40ddc89ca09450febe84dba881483bea36e1.jpg)  
C   
FIGURE 1 Bio-inspired in-memory sensing and processing enabled by reconfigurable MFsM photodiodes based on [[2D ferroelectric semiconductor]]s. (a) Human visual system consisting of the retina and visual cortex. (b) Comparison of conventional vision systems and neuromorphic vision systems. Conventional systems separate sensing, memory, and processing units, requiring fixed R determined by a fixed built-in field. In contrast, neuromorphic systems embed memory and processing within the sensor, where ferroelectric 2D semiconductors provide visible-light responsivity, stable ferroelectric phase, and switchable polarization. (c) Schematic of a vertical MFsM photodiode. The built-in field is electrically reconfigurable via polarization switching, enabling programmable photoresponsivity and tunable optical output (right panel).

-stage cognitive tasks such as feature extraction and classification (Figure 1a). In contrast, conventional vision systems based on photodiode arrays consist of physically separated sensors, memory, and processor units. This separation requires frequent data conversion and transfer, resulting in substantial inefficiencies in terms of energy consumption, processing speed, and area

overhead [1–), 1%–1&]. To overcome these limitations, biologically inspired [[neuromorphic vision sensor]]s have been proposed that directly embed memory and processing functions within frontend sensors [16–26]. This implementation enables sensory nodes to function as active computational elements within neural network architectures [2, (, 27–3&].

At the sensor level, optical-to-electrical conversion can be modeled as a multiplication of the optical input power and the photoresponsivity, generating an electrical output signal [1– 3]. Thus, tunable photoresponsivity both in magnitude and polarity along with non-volatile characteristic is essential to emulate synaptic weights in neural networks. Recent efforts have pursued this through devices with nonlinear response characteristics for tasks such as noise suppression and edge enhancement [1, 2, 3%, 31]. While useful, many of these approaches are often limited to fixed functions without dynamic reconfigurability.

Atomically thin 2D semiconductors have emerged as a compelling platform for reconfigurable optical sensors owing to their strong light-matter interaction and effective electrostatic band control [36–)2]. Reconfigurable photodiodes based on dual-gate geometries, in which the channel can be electrostatically doped, have been reported. In these devices, locally gated regions can be tuned into either p- or n-type conduction, allowing modulation of the magnitude and direction of built-in electric fields for enhanced computational functionality in visual perception tasks [)3–)6]. More advanced designs, such as split-gate 2D transistors incorporating floating or ferroelectric gates, have introduced non-volatile programmability, holding promise for compact and energy-efficient vision systems [), )3–)6]. However, these approaches typically rely on separated programming and readout terminals, which increase structural complexity and device footprint. Under the stringent area and power constraints of IoT and on-device AI platforms, such designs face integration challenges and reduced pixel density, ultimately degrading visual fidelity [1%, )7, )8].

In this context, we report a vertical two-terminal (2-T) reconfigurable photodiode based on metal/ferroelectric semiconductor/metal (MFsM) architecture, where the programming and readout terminals are unified. By electrically switching the out-ofplane polarization of the 2D semiconductor α-In Se , we achieve gradual and reversible modulation of the built-in field at both the top and bottom Schottky junctions. This yields non-volatile, polarity-switchable, analog photocurrents without the need for external bias during readout, offering highly tunable device characteristics in a compact form factor. Crucially, the use of a high-work-function metal (Pt) as the contact electrode is found to be essential for preserving polarization-induced interfacial band bending while suppressing undesired bulk-polarization screening, thereby enabling a robust photovoltaic response. Building on these device characteristics, we further demonstrate highlevel visual information processing, including image feature extraction and classification, using MFsM photodiode arrays configured as reconfigurable convolutional kernels. Owing to the compact vertical architecture and its compatibility with high-density integration, the proposed platform enables contextdependent regulation of spatial-frequency components in visual data. In particular, noise-dominated high-frequency components can be effectively suppressed to stabilize feature extraction under noisy conditions, resulting in an improvement in signal-to-noise ratio from 6.3 to 13.( dB for Gaussian-noise-corrupted images. Conversely, when high-resolution recognition is prioritized, finegrained spatial details can be preserved, achieving classification accuracies of up to (2%.

# 2 Results and Discussion

Conventional vision systems face fundamental inefficiencies due to the physical separation of sensing, memory, and processing units. In such architecture, the sensor operates in the analog domain, necessitating analog-to-digital conversion and repeated data transfer to off-chip memories and processors. These operations result in large latency, power consumption, and memory overhead. To address this, we developed a vertical 2-T ferroelectric semiconductor photodiode as a compact in-memory sensing and processing platform, leveraging the intrinsic advantages of the [[2D ferroelectric semiconductor]] α- $\mathbf { \cdot I n } _ { 2 } \mathbf { S e } _ { 3 }$ (Figure 1b). It possesses an appropriate bandgap (∼1.3( eV) for visible-light detection (Figure S1a). Owing to broken inversion symmetry in its crystal structure (Figure S1b), ${ \alpha } { \mathrm { - } } \operatorname { I n } _ { 2 } \mathbf { S } { \mathbf { e } } _ { 3 }$ exhibits robust ferroelectric polarization that remains stable up to &%% K [)(, &%], making it well-suited for non-volatile memory applications. Moreover, its rich domain configurations, including head-to-head and tailto-tail alignment [&1], facilitate partial polarization switching, enabling analog programmability essential for neuromorphic vision systems.

Notably, ${ \alpha } { \mathrm { - } } \operatorname { I n } _ { 2 } \mathbf { S } { \mathbf { e } } _ { 3 }$ exhibits out-of-plane spontaneous polarization, allowing for 2-T vertical structure in which programming and readout are performed through the same terminals. This configuration enables compact integration while supporting nonvolatile and reconfigurable response characteristics [3, 33, &2]. By electrically modulating the polarization direction, the builtin electric field across the back-to-back Schottky junctions is gradually tuned, effectively switching band alignment between $n { - } p$ (upward polarization) to p–n (downward polarization) configurations. This results in polarity-switchable photocurrents with tunable magnitude (Figure 1c).

The vertical 2-T ferroelectric photodiode comprises the photoactive $\boldsymbol { \alpha } { \cdot } \boldsymbol { \mathrm { I n } } _ { 2 } \boldsymbol { \mathrm { S e } } _ { 3 }$ layers sandwiched between top and bottom Pt electrodes forming back-to-back Schottky junctions (Figure 2a). The top contact is a semi-transparent Pt layer (∼6 nm) to allow optical access. This ultrathin Pt electrode forms a laterally continuous and thickness-uniform film, as verified by optical/dark-field imaging and AFM topography (Figure S2). Prior to top-electrode deposition, the $\alpha { \mathrm { - I n } } _ { 2 } \mathrm { S e } _ { 3 }$ surface was treated with an $\mathrm { O } _ { 2 } / \mathrm { A r }$ plasma to prevent complete screening of ferroelectric polarization by charged surface residues [&3]. X-ray photoelectron spectroscopy (XPS) measurement results confirm that this process does not induce the formation of an InO interfacial layer (Figure S3). Taken together, these fabrication and interfacial characterizations confirm successful realization of the vertical MFsM device structure that supports polarization-controlled junction modulation while maintaining efficient optical coupling. This vertical geometry also enables the same terminals to be used for both programming and readout, minimizing structural complexity (device fabrication details are provided in the Experimental Section, Figure S)).

The out-of-plane ferroelectric polarization of ${ \alpha } { \mathrm { - } } \operatorname { I n } _ { 2 } \operatorname { S } { \mathrm { e } } _ { 3 }$ was confirmed using the contact-resonance piezo response force microscopy (CR-PFM, Figure S&). A +1% V bias was applied to an outer rectangular region and a −1% V bias to an inner region, reversing the pre-written domain orientation. Finally, with no

![](images/5190cb5c0856ad7577567685cbbc5b0fe235741e387599b871e6d7fd068e095f.jpg)  
a

![](images/48d906cdd74da79cfce8e92f8782586bf6be99829f5125bc59982eb92e005b11.jpg)

![](images/09b6c8a9934de64c78001713308501abf5cc0acb043e0195f406af1a2b43b84d.jpg)  
Polarization   
$\mathsf { P } _ { \mathsf { d o w n } }$ Pdown

![](images/9fc03ff2f45bbb35b6dbba186e48cbdfb4029e587c6c7981188fbf5871879350.jpg)  
$\mathsf { P } _ { \mathsf { u p } }$ Pu

![](images/ffdd8cbb8dbbddf72f118caf9079686791e54a294a6917772e292e317ff5a786.jpg)  
b

![](images/193f1322f25bda89a1293a8fa1841d0314879eed6c117335889c68f736827239.jpg)  
C

![](images/9fb260b6419e99ec6f353204f6049577a1d09c0f49adaf0620f636c05e34f74b.jpg)

![](images/25af8403a2fff5af116d5d43177d877ccd61fa65dd3bf180bb142338286891cd.jpg)  
d

![](images/132685c5a1ff0d5008951cbd4714cffb485bd9cc5de39730a254fd378f894305.jpg)  
e

![](images/795cb916ff2bf85c4fd8f9cdd3239db9829a02023120c1cafd983ff38deef7ae.jpg)

![](images/695bf294030ec6c420444d5b97dc347402abfda8a4f10ea8a8c7182edde862e6.jpg)

![](images/9b039dc657d159faaed0f2f24a2b5199bff56424510f4437033f9554b15b443a.jpg)  
FIGURE 2 Polarity-switchable MFsM photodiode based on ferroelectric ${ \alpha } \mathrm { - I n } _ { 2 } \mathrm { S e } _ { 3 }$ . (a) Schematic illustration and optical microscope image of MFsM device array. Scale bar, $4 \mu \mathrm { m }$ . (b) Out-of-plane PFM phase image after sequential domain writing (+1% V applied to the outer box and −1% V to the inner box). $\mathbf { A } \sim 1 8 0 ^ { \circ }$ phase contrast confirms switchable polarization. Scale bar, 2 µm. (c) PFM phase (left) and amplitude (right) hysteresis loop of 2)-nm-thick ${ \alpha } \mathrm { - I n } _ { 2 } \mathrm { S e } _ { 3 }$ layer on Pt substrate, demonstrating stable and reversible polarization switching. (d) J–V characteristics showing polarizationdependent diode behavior in the dark (upper panel) and under light illumination (lower panel). (e) Energy band diagram and time-resolved photocurrent density corresponding to the $P _ { \mathrm { u p } }$ (upper) and $P _ { \mathrm { d o w n } }$ (lower) polarization states, illustrating sign-tunable photocurrent response.

bias, conductive probe scanned the whole area in the pursuit of visualizing manipulated PFM phases. The resulting PFM phase map (Figure 2b) shows a clear ∼18%◦ phase contrast between the two regions, confirming electrically switchable polarization. Amplitude and phase hysteresis loops (Figure 2c) further indicate stable and reversible switching with well-defined coercive voltages, ensuring controllable modulation of the built-in electric field.

Having established the device architecture and verified the outof-plane ferroelectric switching capability of $\mathrm { \dot { \alpha } } _ { \mathrm { - } } \mathrm { I n } _ { 2 } \mathrm { S e } _ { 3 }$ via PFM, we next examined how polarization control translates into the operational behavior of the vertical MFsM photodiode. In particular, we focused on how the interplay between ferroelectric polarization and metal contacts determines the diode rectification and photocurrent polarity. This investigation not only elucidates the fundamental operation principle of our device but also provides design guidelines for optimizing contact engineering in polarization-driven reconfigurable photodiodes.

The core functionality of our device lies in its polarization dependent switchable photodiode characteristics, where ferroelectric polarization in α-In Se modulates the built-in electric fields, inducing opposite changes in the barrier height and depletion width at the top and bottom Schottky junctions. This configuration effectively controls both the rectification behavior and the polarity of the photocurrent. To investigate this, devices were programmed via voltage sweeps beyond the coercive field, followed by optoelectrical characterization under both dark and illuminated conditions. A positive sweep $( 0 \to + 5 \mathrm { ~ V ~ } \to \mathrm { ~ 0 ~ V ) ~ }$ switches the polarization downward. In this state, negative bound charges at the top interface cause electron depletion for screening, leading to upward band bending and an increased Schottky barrier height (SBH). Simultaneously, positive bound charges at the bottom interface induce electron accumulation, resulting in downward band bending and a reduced SBH. This asymmetric modulation produces a p–n junction-like (from top to bottom) diode configuration in the dark (Figure 2d, upper panel, red curve). Conversely, a negative sweep (% −& V % V) reverses the polarization, inducing the opposite band bending configuration and the resultant n–p junction-like (from top to bottom) diode behavior in the dark (Figure 2d, upper panel, blue curve). No such switching behavior is observed when the sweep voltage is below the coercive voltage, confirming that the effect originates from ferroelectric polarization reversal (Figure S6).

Kelvin probe force microscopy (KPFM) measurements further reveal a surface potential difference of ∼%.3 eV between antiparallel polarization domains, directly evidencing polarizationinduced modulation of the electronic boundary conditions at the Schottky interface (Figure S7). In addition, temperaturedependent J–V measurements yield SBHs of %.61 and %.6) eV for the $P _ { \mathrm { u p } }$ and $P _ { \mathrm { d o w n } }$ states, respectively, confirming that polarization reversal selectively changes which junction (top or bottom) dominates carrier transport (Figure S8).

This asymmetric control over the dominant transport junction directly accounts for the observed polarity reversal in the shortcircuit photocurrent density $J _ { \mathrm { s c } }$ (Figure 2d, lower panel). For the $P _ { \mathrm { d o w n } }$ state upon positive voltage sweep, the built-in field

$( E _ { \mathrm { b i } } )$ at the top junction is enhanced by carrier depletion, while that at the bottom junction is reduced, causing photocarrier separation to be dominated by the top junction and yielding negative $J _ { \mathrm { s c } } \ 0 \mathrm { f } - 1 5 \mathrm { m A } / \mathrm { c m } ^ { 2 }$ . In contrast, the $P _ { \mathrm { u p } }$ state enhances $E _ { \mathrm { b i } }$ at the bottom junction, reversing the photocurrent polarity to 12 mA/cm2 (Figure 2d, lower panel). Time-resolved photocurrent measurements (Figure 2e) further confirm stable and reversible photocurrent polarity switching via ferroelectric polarization control.

Given that the photovoltaic response depends critically on the built-in field asymmetry, the choice of contact metal becomes an important design factor. We therefore examined how contact work function and the resulting interface capacitance influence device performance. The equivalent capacitance of our device can be modeled as the series of the interface capacitance (C ) and the bulk capacitance $( C _ { \mathrm { { b } } } ) _ { \mathrm { { i } } }$ , where $C _ { \mathrm { i } }$ is reduced by depletion effects arising from the electrode–semiconductor contact potential. At this time, $C _ { \mathrm { i } }$ is inversely proportional to the built-in potential $( V _ { \mathrm { b i } } )$ because $\begin{array} { r } { \dot { \mathbf { C } } _ { \mathrm { i } } = \frac { \mathbb { q } \varepsilon _ { \mathrm { s } } \mathrm { N _ { D } } } { 2 \mathrm { V _ { b i } } } } \end{array}$ , where q is a unit charge, $\varepsilon _ { s }$ is semiconduc-2V bitor’s dielectric constant, and $N _ { \mathrm { D } }$ is carrier density. Thus, when contacted with Au (work function ∼&.% eV, smaller than Pt at ∼&.) eV, Figure S(), $V _ { \mathrm { b i } }$ decreases, and $C _ { \mathrm { i } }$ increases compared to Pt. Upon polarization switching, this larger $C _ { \mathrm { i } }$ in Au-contacted devices drives stronger bulk polarization, which generates an opposing field that cancels the depolarization field at the interface, effectively suppressing both rectification and photovoltaic effects [&)]. Consequently, Au-contacted devices fail to exhibit the polarization-dependent diode and photocurrent characteristics observed with Pt (Figure S1%). By contrast, Pt-contacted devices with their smaller $C _ { \mathrm { i } }$ preserve the asymmetric band profile necessary for strong photovoltaic response. J–V measurements under dark and illuminated conditions (Figures S11 and S12) confirm that only Pt-contacted devices deliver robust, polarity-tunable photocurrents consistent with the polarization-controlled band modulation mechanism.

Building on the polarization-dependent diode characteristics, we next evaluate the suitability of our device for emulating synaptic weight in neural network. The photodiode was first programmed into six distinct states using voltage pulses, and the corresponding J–V curves were measured under different illumination conditions (8(, 2%&, 317 mW cm2) (Figure 3a). ${ \cal J } _ { \mathrm { s c } } ,$ represented by the y-intercept of the J–V curves, is gradually modulated from negative to positive values as the junction band alignment evolved, confirming analog tunability of the device states.

This tunability is further demonstrated through long-term potentiation (LTP) and long-term depression (LTD) measurements (Figure 3b). During the writing process, negative $V _ { \mathrm { { D } } }$ pulses (– ) V, 1 µs) progressively increased the photoresponsivity (R), while successive positive $V _ { \mathrm { { D } } }$ pulses (+) V, 1 µs) decreased it. Between each pulse, the device was optically read at zero bias, demonstrating self-powered operation without the need for an external read voltage. Negative $V _ { \mathrm { { D } } }$ pulses gradually switch the polarization from up to down, converting R from negative to positive, whereas positive pulses reverse the process. To further assess stability, multiple states were initially programmed by voltage pulses and read out every 1% s. All states remain stable for over 1%%% s, demonstrating robust retention of polarization-driven

![](images/19a11d4f77f79a6f092a70724c0cdc3c9c1852c79b9f70412999944178fb855e.jpg)  
a

![](images/47be5fccf31a3418b0b3abccc2d7573e959b1c52c42bb38583c51fe2e4e42d65.jpg)  
h

![](images/c5062eecf305777e06161e634a45dabcd4b3fe188bab28ecd45c5098df0c5180.jpg)  
C

![](images/32d8ea7bdc1467ca94d18bac92abc3338f87eebacb7e58d26c70ba8ae7b86304.jpg)  
d   
FIGURE 3 Synaptic photoresponsivity characteristics of vertical MFsM photodiodes. (a) J–V curves measured at six programmed states under varying illumination power. (b) LTP and LTD characteristics showing multi-level, non-volatile modulation of R by sequential voltage pulses. (c) Retention characteristics of multiple programmed states over 1%%% s with optical readout at zero bias. (d) Linear dependence of photocurrent density on incident optical power across six distinct states, confirming optical-power-independent response.

analog photoresponsivity (Figure 3c). For retention evaluation, five representative programmed states were selected, comprising one OFF state, two positive-weight states, and two negativeweight states. In addition, beyond photoresponsivity modulation, the device conductance under dark conditions is also modulated in an analog and non-volatile manner through polarization switching, confirming its potential operation as an electrical synaptic element independent of optical input (Figure S13).

In addition to analog-like tunability and retention, the opticalpower-independent response characteristic is a key requirement for implementing reliable synaptic weights in neural networks. To evaluate this, the device was programmed into six representative states, including three positive $\left( \mathbf { U } _ { 1 } , \mathbf { U } _ { 2 } , \mathbf { U } _ { 3 } \right)$ and the three negative values $( \mathrm { D } _ { 1 } , \mathrm { D } _ { 2 } , \mathrm { D } _ { 3 } )$ , and corresponding $J _ { \mathrm { s c } }$ was measured under varying light intensities ()8, 8(, 2%&, 317 mW/cm2). In all cases, $J _ { \mathrm { s c } }$ scales linearly with incident light intensity, as confirmed by fitting parameters (α = %.83, %.88, 1.%1 for $\mathrm { U } _ { 1 } , \mathrm { \Delta U } _ { 2 } , \mathrm { \Delta U } _ { 3 }$ and %.(6, %.8), %.81 for $\mathrm { D } _ { 1 } , \mathrm { D } _ { 2 } , \mathrm { D } _ { 3 }$ respectively) (Figure 3d). These results highlight excellent linearity between optical input and electrical output across multiple programmed states, indicating power-independent photoresponse characteristics.

Overall, our device satisfies key performance requirements for neuromorphic vision networks by combining non-volatile multilevel programmability, optical-power-independent operation, self-driven optical readout, fast write capability, and stable operation under visible-light illumination. A comparative assessment of the present vertical MFsM device with previously reported ferroelectric-based in-memory sensing and computing platforms, focusing on device architecture and vision-relevant performance metrics, is provided in Table S1.

Based on the reconfigurable photoresponsivity of our vertical MFsM photodiodes, diverse visual features can be selectively extracted at the sensor level through programmable spatial filtering. Basic filtering functions, including background extraction and edge detection, can be directly implemented by programming the polarity and magnitude of responsivity values derived from experimental measurements (Figure S1)). For instance, background extraction is achieved by suppressing illuminated foreground regions using negative responsivity values, whereas edge-detection filters combining positive and negative weights enable selective extraction of left and right edges in MNIST digit images.

More fundamentally, these filtering operations reflect a broader capability of the proposed platform to regulate visual information according to its spatial-frequency content. Visual information can be broadly decomposed into low-frequency components, which capture global features such as shape and contours through gradual intensity variations, and high-frequency components, which arise from abrupt brightness changes and encode fine structural details. By programming the spatial weight distribution within the same device, the sensor can emphasize either low- or highfrequency components of an input image, thereby generating feature representations with distinct perceptual characteristics (Figure )a).

Low-frequency-oriented filtering, implemented using box and Gaussian kernels, aggregates neighboring pixel responses using positive weights, effectively suppressing rapid local fluctuations while preserving global structures such as object shape and background illumination. In contrast, high-frequency-oriented filtering is realized using directional Sobel kernels along the horizontal and vertical axes. Unlike low-frequency filters, these kernels employ both positive and negative weights, enabling selective responses to abrupt intensity transitions while cancelling out slowly varying background components. As a result, local structural cues such as edges and fine contours are highlighted, which is critical for precise shape discrimination. Through this reconfigurable filtering capability, our device can generate multiple, complementary feature maps from the same visual input, enabling selective extraction of visual information depending on the task requirements and visual context.

Having established device-level reconfigurability and functionality, we next examine how the compact integration enabled by our device architecture manifests at the system level under different visual contexts and task objectives. A central challenge in visual information processing lies in regulating relative contributions of different spatial-frequency components depending on visual conditions and the task context. In particular, high-frequency components warrant careful consideration, as their functional role is highly context-dependent: high-frequency information can act as target-irrelevant noise under background-noise-dominated conditions, while serving as a critical structural cue in tasks that require discriminating subtle shape differences. Accordingly, for robust perceptual precision computing across diverse conditions, a vision system should be capable of selectively emphasizing or suppressing high-frequency components depending on the visual context.

To investigate how area-efficient spatial integration enables such selective regulation of high-frequency information and consequently impacts system-level behavior, we considered two representative visual processing scenarios under an area-normalized modeling framework. In this framework, the vertical MFsM architecture and planar split-gate-based photodiode arrays were assumed to occupy the same total footprint but differ in effective unit-cell area, namely $4 \mathrm { F } ^ { 2 }$ and $1 6 \mathrm { F } ^ { 2 }$ , respectively. Based on this area correspondence, differences in achievable spatial integration density were translated into differences in effective spatial support at the sensor and system levels. Accordingly, larger spatial kernels and higher-resolution image (e.g., ) × ) kernels and 2% × 2% pixels) are associated with the $4 \mathrm { F } ^ { 2 }$ configuration, while smaller kernels and reduced input resolutions (e.g., 2 × 2 kernels

and 1% × 1% pixels) correspond to the $1 6 \mathrm { F } ^ { 2 }$ configuration. These settings provide a consistent basis for comparing how devicelevel density constraints propagate to feature extraction and downstream neural network performance.

Figure )b demonstrates noise-robust feature extraction enabled by high-density spatial filtering using the vertical MFsM photodiodes, in a scenario where high-frequency components coexist in both the target and the background. The input image contains a circular target with spatially correlated high-frequency features, such as continuous edges and coherent contours, namely, structured high-frequency component. By contrast, the background is corrupted by unstructured noise introduced by Gaussian noise $( \sigma = 0 . 0 8 )$ , generating spatially random and incoherent highfrequency intensity fluctuations. Although both components occupy a similar high-frequency spatial range, their responses to spatial integration differ substantially due to their distinct spatial coherence. To selectively extract structured frequency component, horizontal and vertical gradients are computed independently and combined into a local edge-magnitude map. When $\mathrm { ~ a ~ 4 ~ } \times \mathrm { ~ 4 ~ }$ spatial kernel is implemented using the highdensity integration enabled by the compact vertical architecture (Figure )b, left panel), spatial averaging effectively suppresses incoherent background fluctuations while preserving the continuity of the target contour, resulting in a clear feature map with an enhanced signal-to-noise ratio (SNR ∼13.( dB). In contrast, a 2 × 2 kernel with limited spatial support (Figure )b, right panel) directly transmits background-induced fluctuations into the edge response, leading to fragmented, noise-dominated features and a reduced SNR of approximately 6.3 dB. These results highlight that larger spatial kernels, made possible by compact device integration, are critical for suppressing target-irrelevant highfrequency noise and extracting structurally stable features under noisy conditions.

Figure )c evaluates system-level scenarios in which highfrequency visual information plays a constructive and decisive role in recognition accuracy, highlighting the advantage of compact, high-density sensing enabled by the vertical MFsM architecture. In the Fashion MNIST dataset, visually ambiguous classes such as T-shirt, shirt, and pullover share similar global shapes, and classification critically depends on resolving subtle local features (e.g. sleeve edges, collar regions, and fine texture cues). Under an area-normalized modeling framework, the $4 \mathrm { F } ^ { 2 }$ unit-cell supports higher spatial sampling resolution $( 2 0 \times 2 0$ pixels, left panel of Figure )c), whereas the $1 6 \mathrm { F } ^ { 2 }$ is constrained to lower-resolution inputs (1% × 1% pixels, right panel of Figure )c). Consequently, the high-density configuration preserves discriminative high-frequency details essential for class separation, while reduced-resolution sensing leads to blurred contours, increased feature overlap, and degraded recognition performance.

These resolution-dependent effects are quantitatively summarized in the confusion matrices shown in Figure )d. The 2% × 2% ()F2) case exhibits strong diagonal dominance, yielding a high classification accuracy of (2%, indicative of effective utilization of high-frequency discriminative cues. In contrast, the $1 0 \times 1 0$ $( 1 6 \mathrm { F } ^ { 2 } )$ case exhibits pronounced off-diagonal confusion among similar classes, resulting in a substantially reduced accuracy of 7)%, consistent with the insufficient representation of fine-scale features at reduced resolution.

![](images/0ff0dc8b291b571120464c44b0a0816077f9e9204eb2bd285d9a7091bc6562b4.jpg)  
a   
Visual input

![](images/964c85a38862d22dc4a3387573cb9e0a78e927944ce815e373da1c50379d528b.jpg)  
Vision sensor   
3x3filter

![](images/718fea0b6f0d2e178d6137b35385c7d89db8b788b27b4be565573539459b49b4.jpg)  
Feature extraction   
Low pass filter   
Box

![](images/3b550509872667a9d0be8ad419fa54db25e2cb071d50e9958d002463561ea571.jpg)

![](images/da3d9f0b3b53b92153affc3dc5b1b5769b43c1d4c6b6474a02daf0ea89c345d0.jpg)  
Gaussian

![](images/c7d42de1002197b83098a1eec454a5380958b8d3e0630116c567b8e7d84f4ea2.jpg)

![](images/20fb0f0a02c25a6ff43c2b393335d1411537510d37a6c493239636547e014da5.jpg)  
Sobel X Sobel X   
High pass filter

![](images/9cce72af30d8fee366fd212c91394e40c227bd50a6b4614d7cb63ee269f240f4.jpg)

![](images/bc01c79483f2dc7002d95295aa23719bf560bb355d2f4acaa817ce24c8e1f999.jpg)

![](images/c42f04db7833088a5d1f336195ddd22c9a9dbfcbcdb364b559112001745fa059.jpg)  
Sobel Y

![](images/80dc3a8615093169f286ab589a9a8705c421af6f8355a03f8b0f48fa60a575ed.jpg)  
b   
Robust feature extraction under noise-dominated conditions   
C   
High-precision classification under high-resolution sensing

![](images/560ea8f0dc6781e7e484db02181780e4966de6f57ccc1e247147af90a96fcaa2.jpg)  
High resolution (4F², 20 x 20)

![](images/0c6fae00620326a90fd986743822a99ca340ef7b69dc60c04ed7ed07840632aa.jpg)  
Visually ambiguous classes   
Pullover

![](images/dbb11266243e8e79d3a34f285ac744d635d218eb4ad1973044091729f3a3b3f2.jpg)

![](images/6597675b2cb800a81c13b9e51535b6b4df2b989f3779067521302494293ef460.jpg)

![](images/913d694f611be4eb3cd662e33366061ae1d52d0ed68d8a0fde8bb70d87088566.jpg)  
Neural network

![](images/4e5928e11a261bd6f09ecbee72f7e7969c8c7101404efbce764b2cb22bf2b256.jpg)  
Low resolution (16F²,10 × 10)

![](images/618902a7e9fe031fa5bb0c20995bc6fd68ced41b78698ec7b3f32e65b65ad59b.jpg)  
Neural network

![](images/5f2627c77894a125416d39d89487e91b556f8dff741b2b2421664c46cf43437c.jpg)  
d   
High resolution (4F²,20 x 20)

![](images/89fe1d93375734bfe5b29b3a5502eca4857914efac9e952d1d6e1bc328e7c8f6.jpg)  
Low resolution (16F²,10 ×10)

![](images/752f0323b1762a34fa0122d128f3e929da58233b6a21f4a579444b0731367925.jpg)  
Classification results   
FIGURE 4 Context-dependent visual processing enabled by compact vertical MFsM photodiode integration. (a) Reconfigurable feature extraction using programable photoresponsivity characteristics of MFsM photodiodes. By tunning the polarity and magnitude of synaptic weights within ${ \mathrm { ~ a ~ } } 3 \times 3$ kernel, the same device platform can perform different image filtering operations. Low-pass filters (box and Gaussian) suppress high-frequency noise and extract coarse intensity variations, whereas high-pass Sobel filters enhance local intensity gradients associated with fine image details. The box filter applies uniform weighting across the kernel, while the Gaussian filter emphasizes central pixels to preserve coarse structural features with reduced spatial distortion. (b) Noise-robust feature extraction via extended spatial support under area-normalized conditions. Owing to the compact vertical MFsM architecture (unit-cell area of $4 \mathrm { F } ^ { 2 } )$ supports a larger effective spatial kernel $( 4 \times 4 )$ , suppressing noise-induced high-frequency fluctuations while preserving target contour continuity, resulting in an enhanced signal-to-noise ratio (SNR ≈ 13.8 dB). In contrast, a planar split-gate-based configuration (unit-cell area of $1 6 \mathrm { F } ^ { 2 } )$ is limited to a smaller kernel $( 2 \times 2 ) ,$ yielding a lower SNR (≈ 6.3 dB). (c) High-precision classification enabled by highresolution sensing. For visually ambiguous Fashion-MNIST classes (T-shirt, shirt, and pullover), higher input resolution supported by the compact MFsM architecture (2% × 2% pixels, )F2) preserves fine local details critical for discrimination, whereas reduced resolution in the split-gate configuration (1% × 1% pixels, $1 6 \mathrm { F } ^ { 2 } )$ leads to loss of discriminative details and increased feature overlap. (d) Confusion matrices and classification accuracy summarizing improved class separability and higher recognition accuracy achieved by effectively retaining high-frequency details through compact, high-resolution sensing.

Altogether, these results demonstrate that the compact, highdensity integration enabled by the vertical MFsM photodiode architecture allows high-frequency information to be selectively exploited when it is beneficial, enhancing fine-grained discrimination, while complementing the noise-robust spatial integration discussed above. This context-dependent regulation of highfrequency visual information enables both improved robustness and superior recognition accuracy in neuromorphic vision tasks.

Building on these system-level capabilities, our vertical MFsM photodiodes provide a potential pathway toward hierarchically integrated neuromorphic vision hardware. In addition to operating optically as an element for in-memory sensing and computing platform, the same device structure can also function electrically as an in-memory computing element (Figure S1&). This dualmode functionality within a unified device architecture suggests the feasibility of constructing multilayer neuromorphic systems while reducing hardware complexity. Such an approach could support hierarchical information processing across multiple network layers, which is essential for complex vision tasks such as object localization and segmentation (Figure S1&). From a broader perspective, leveraging a single compact vertical device for both in-memory sensing and computing and in-memory computing offers a scalable hardware framework for neuromorphic vision systems with increased functional depth and improved architectural efficiency.

# 3 Conclusions

In summary, we demonstrated a compact and reconfigurable [[neuromorphic vision sensor]] based on a vertical MFsM photodiode. By electrically switching the ferroelectric polarization of α-In Se , the built-in field at the top and bottom Schottky junctions can be precisely modulated, enabling polarity tunable, non-volatile, analog photoresponsivity in a simple 2-T device design. This vertical configuration supports ultra-high-density integration within a fixed footprint, which directly translates into system-level advantages. In particular, the increased pixel density enables spatial integration to be adaptively regulated according to visual context: suppressing noise-dominated highfrequency components under noisy conditions while preserving fine-grained details required for accurate classification. Together, these results establish the vertical MFsM photodiode as a compact yet versatile building block, demonstrating how device-level reconfigurability and high-density integration can be leveraged to achieve context-aware visual information processing. This work highlights the potential of vertical ferroelectric photodiodes as a scalable neuromorphic hardware platform for next-generation neuromorphic vision systems.

# 4 Methods

# 4.1 Device Fabrication

α-In Se active layers (typical thickness, 2%−3% nm) were mechanically exfoliated onto Si substrates with thermally grown 28&-nm-thick SiO . The exfoliated α-In Se flakes were picked up using a polypropylene carbonate (PPC)/polydimethylsiloxane (PDMS) stamp and transferred onto prepatterned Pt bottom

electrodes (3% nm) deposited by an e-beam evaporator. The flakes were released from the PDMS by heating to 7%◦C and residual PPC was removed in acetone. Subsequently, e-beam lithography was performed to define the top-electrode pattern. To remove polymer residues and improve interfacial contact, an O /Ar plasma treatment (1%%/1) sccm) was performed at 2%% W for 1 min. Finally, semitransparent Pt top electrodes (∼6 nm) were deposited using an e-beam evaporator at a slow rate (<%.1 nm s−1 ) on the patterned regions to allow optical access. The overall fabrication processes are schematically illustrated in Figure S).

# 4.2 Optoelectrical Characterizations

Electrical transport and photoresponse measurements were carried out using a custom setup consisting of a voltage source (Yokogawa GS2%%), a pulse generator (Keysight 8111%A), a current preamplifier (DL Instrument 1211), and a digital multimeter (Keysight 3))%1A). Photocurrent measurements, including longterm potentiation and depression (LTD and LTD), were performed under &32 nm laser illumination focused through a &%× objective on an optical microscopy equipped with a motorized stage. Optical excitation was modulated by a mechanical chopper to produce a periodic on/off profile, enabling time-domain photocurrent and retention measurements. The temporal responses were monitored with a digital oscilloscope (Siglent SDS3%)CFL). All measurements were conducted under ambient conditions at room temperature.

# 4.3 Contact-Resonance PFM Measurement

Contact-resonance piezoresponse force microscopy (CR-PFM) was used to evaluate the ferroelectric properties of α-In Se . Measurements were conducted on an AFM (Park Systems NX1%) equipped with a high-frequency excitation module (NOST) and a conductive Cr/Pt-coated cantilever (ElectriMulti7&-G; tip radius ≈ 2& nm). A high-frequency AC bias (>1%% kHz) was applied to the AFM tip to drive oscillation near the contact-resonance frequency, and the cantilever’s vertical deflection was monitored by a laser–photodiode detector. The response signal was demodulated with a lock-in amplifier (Zurich Instruments HF2LI) to extract both amplitude and phase components. Additional measurement details and schematics were provided in Figure S2.

# 4.4 KPFM Measurement

KPFM measurements were performed to investigate surface potential variations. The potential maps were acquired in noncontact mode by applying an AC voltage to the conductive tip to determine the contact potential difference (CPD).

# 4.5 XPS Analysis

To investigate the composition changes in α-In Se induced by plasma treatment, X-ray photoelectron spectroscopy (XPS) was performed using a ULVAC-PHI X-Tool system equipped with a monochromatic Al Kα X-ray source (1)(%.& eV). The

measurements were conducted under a high vacuum of $7 . 0 \times$ $1 0 ^ { - 7 }$ Pa, with a photoemission current exceeding &.% µA at & kV.

# 4.6 Optical Characterization

Raman and photoluminescence (PL) spectra were acquired to estimate the optical bandgap and verify ferroelectric-related structural characteristics of α-In Se . A &32 nm laser was used as an excitation source, and the emitted signals were collected using a monochromator (Andor SOLIS 3%3). For PL measurements, a 3%%-groove mm−1 grating was used to capture a broad emission spectrum; for Raman, a high-resolution grating of 18%% groove mm−1 grating was employed to resolve characteristic vibrational modes.

# 4.7 Weight Update for Pattern Recognition

Pattern recognition consisted of two main stages: inference and training. During the inference stage, the neural network generates output signals based on given inputs, whereas the training stage focuses on optimizing synaptic weights to learn the input–output relationship for accurate pattern classification. In the inference phase, the pixel values of the input image (P) are fed into the neural network, where they are multiplied and summed with the photoresponsivity values (R) that serve as synaptic weights. To introduce nonlinearity required for classification, the weighted sum passes through a sigmoid activation function $f ,$ as expressed by $o = f ( \sum P \mathrm { x } R )$ . In the subsequent training phase, the error (δ) was calculated as the difference between the target output (t) and the actual output (o): $\delta = t { - } o$ . Depending on the sign of $\delta ,$ the synaptic weights are updated in the opposite manner: a positive error $( \delta > 0 )$ induces the potentiation phase in which the weights are increased, while a negative error $( \delta < 0 )$ induces the depression phase in which the weights are decreased. The weight update in each phase follows the delta rule and can be described by the following equations:

$$
\Delta R p = a _ {\mathrm {p}} + b _ {\mathrm {p}} \mathrm {e} ^ {- c _ {\mathrm {p}} \frac {\mathrm {R} _ {\mathrm {n}} - \mathrm {R} _ {\mathrm {m i n}}}{\mathrm {R} _ {\mathrm {m a x}} - \mathrm {R} _ {\mathrm {m i n}}}} (\delta > 0, \text {P o t e n t i a t i o n p h a s e})
$$

$$
\Delta R d = a _ {\mathrm {d}} + b _ {\mathrm {d}} \mathrm {e} ^ {- c _ {\mathrm {d}} \frac {\mathrm {R} _ {\max } - \mathrm {R} _ {\mathrm {n}}}{\mathrm {R} _ {\max } - \mathrm {R} _ {\min }}} (\delta <   0, \text {D e p r e s s i o n p h a s e})
$$

Here, $\varDelta R _ { \mathrm { p } }$ and $\varDelta R _ { \mathrm { d } }$ corresponds to weight change during longterm potentiation (LTP) and long-term depression (LTD), respectively, where $a _ { \mathrm { p } } , \ : a _ { \mathrm { d } } , \ : b _ { \mathrm { p } } , \ : b _ { \mathrm { d } } \ : \ : c _ { \mathrm { p } } ,$ and $c _ { \mathrm { d } , }$ are fitting parameters obtained from experimental LTP/LTD curves. The weight value is constrained between $R _ { \operatorname* { m i n } } , \ R _ { \operatorname* { m a x } }$ to ensure stable, bounded learning dynamics.

# Acknowledgements

This research was supported by the National Research Foundation (NRF) of Korea grant funded by the Korean government (MSIT) (RS-2%21- NR%6%%87, RS-2%23-NR%77272) and by the Creative Allied Project of the National Research Council of Science & Technology (NST) funded by the Ministry of Science and ICT of Korea (CAP2&%31-%%%). C.-H.L. acknowledges support from the BK21 FOUR Program of the Education and Research Program for Future ICT Pioneers, Seoul National University

(SNU) in 2%2&, Creative-Pioneering Researchers Program through SNU, and SNU Electrical Power Research Institute (SEPRI), the Interdisciplinary Program in Artificial Intelligence, and the New Faculty Startup Fund at Seoul National University.

# Conflicts of Interest

The authors declare no conflicts of interest.

# Data Availability Statement

The data that support the findings of this study are available from the corresponding author upon reasonable request.

# References

1. F. Zhou and Y. Chai, “Near-Sensor and In-Sensor Computing,” Nature Electronics 3 (2%2%): 66)–671.   
2. T. Wan, B. Shao, S. Ma, Y. Zhou, Q. Li, and Y. Chai, “In-Sensor Computing: Materials, Devices, and Integration Technologies,” Advanced Materials 3& (2%23): 22%383%.   
3. Z. Wang, T. Wan, S. Ma, and Y. Chai, “Multidimensional Vision Sensors for Information Processing,” Nature Nanotechnology 1( (2%2)): (1(–(3%.   
). G. Wu, X. Zhang, G. Feng, et al., “Ferroelectric-Defined Reconfigurable Homojunctions for In-Memory Sensing and Computing,” Nature Materials 22 (2%23): 1)((–1&%6.   
&. Y. Yang, C. Pan, Y. Li, et al., “In-Sensor Dynamic Computing for Intelligent Machine Vision,” Nature Electronics 7 (2%2)): 22&–233.   
6. D. Lee, M. Park, Y. Baek, B. Bae, J. Heo, and K. Lee, “In-Sensor Image Memorization and Encoding via Optical Neurons for Bio-Stimulus Domain Reduction Toward Visual Cognitive Processing,” Nature Communications 13 (2%22): &223.   
7. H. Kolb, “How the Retina Works,” American Scientist (1 (2%%3): 28–3&.   
8. C. D. Gilbert and W. Li, “Top-Down Influences on Visual Processing,” Nature Reviews Neuroscience 1) (2%13): 3&%–363.   
(. C. D. Schuman, S. R. Kulkarni, M. Parsa, J. P. Mitchell, P. Date, and B. Kay, “Opportunities for Neuromorphic Computing Algorithms and Applications,” Nature Computational Science 2 (2%22): 1%–1(.   
1%. K. Kyuma, E. Lange, J. Ohta, A. Hermanns, B. Banish, and M. Oita, “Artificial Retinas — Fast, Versatile Image Processors,” Nature 372 (1(()): 1(7–1(8.   
11. Y. Liu, R. Fan, J. Guo, H. Ni, and M. U. M. Bhutta, “In-Sensor Visual Perception and Inference,” Intelligent Computing 2 (2%23): %%)3.   
12. S. Wang, X. Pan, L. Lyu, et al., “Nonvolatile van der Waals Heterostructure Phototransistor for Encrypted Optoelectronic Logic Circuit,” ACS Nano 16 (2%22): )&28–)&3&.   
13. F. Zhou, J. Chen, X. Tao, X. Wang, and Y. Chai, “2D Materials Based Optoelectronic Memory: Convergence of Electronic Memory and Optical Sensor,” Research 2%1( (2%1(): ()(%)13.   
1). R. Wang, S. Wang, K. Liang, et al., “Bio-Inspired In-Sensor Compression and Computing Based on Phototransistors,” Small 18 (2%22): 22%1111.   
1&. G.-X. Zhang, Z.-C. Zhang, X.-D. Chen, et al., “Broadband Sensory Networks With Locally Stored Responsivities for Neuromorphic Machine Vision,” Science Advances ( (2%23): adi&1%).   
16. S. Chen, Z. Lou, D. Chen, and G. Shen, “An Artificial Flexible Visual Memory System Based on an UV-Motivated Memristor,” Advanced Materials 3% (2%18): 17%&)%%.   
17. B. Cui, Z. Fan, W. Li, et al., “Ferroelectric Photosensor Network: An Advanced Hardware Solution to Real-Time Machine Vision,” Nature Communications 13 (2%22): 17%7.

18. L. Sun, Z. Wang, J. Jiang, et al., “In-Sensor Reservoir Computing for Language Learning via Two-Dimensional Memristors,” Science Advances 7 (2%21): abg1)&&.   
1(. F. Zhou, Z. Zhou, J. Chen, et al., “Optoelectronic Resistive Random Access Memory for [[neuromorphic vision sensor]]s,” Nature Nanotechnology 1) (2%1(): 776–782.   
2%. T. Ahmed, S. Kuriakose, E. L. H. Mayes, et al., “Optically Stimulated Artificial Synapse Based on Layered Black Phosphorus,” Small 1& (2%1(): 1(%%(66.   
21. X. Fu, T. Li, B. Cai, et al., “Graphene/MoS2−xOx/graphene Photomemristor With Tunable Non-Volatile Responsivities for Neuromorphic Vision Processing,” Light: Science & Applications 12 (2%23): 3(.   
22. S. Lee, R. Peng, C. Wu, and M. Li, “Programmable Black Phosphorus Image Sensor for Broadband Optoelectronic Edge Computing,” Nature Communications 13 (2%22): 1)8&.   
23. K. Liu, T. Zhang, B. Dang, et al., “An Optoelectronic Synapse Based on α-In Se With Controllable Temporal Dynamics for Multimode and Multiscale Reservoir Computing,” Nature Electronics & (2%22): 761–773.   
2). L. Pi, P. Wang, S.-J. Liang, et al., “Broadband Convolutional Processing using Band-Alignment-Tunable Heterostructures,” Nature Electronics & (2%22): 2)8–2&).   
2&. C.-Y. Wang, S.-J. Liang, S. Wang, et al., “Molecular Collapse States in Graphene/WSe Heterostructure,” Science Advances 8 (2%22): abq8616.   
26. Z. Zhang, S. Wang, C. Liu, R. Xie, W. Hu, and P. Zhou, “All-in-One Two-Dimensional Retinomorphic Hardware Device for Motion Detection and Recognition,” Nature Nanotechnology 17 (2%22): 27–32.   
27. T. Y. Wang, J. L. Meng, Q. X. Li, et al., “Reconfigurable Optoelectronic Memristor for In-Sensor Computing Applications,” Nano Energy 8( (2%21): 1%62(1.   
28. Y. Chai, “In-Sensor Computing for Machine Vision,” Nature &7( (2%2%): 32–33.   
2(. H. Huang, X. Liang, Y. Wang, et al., “Fully Integrated Multi-Mode Optoelectronic Memristor Array for Diversified In-Sensor Computing,” Nature Nanotechnology 2% (2%2&): (3–1%3.   
3%. Y. Gong, R. Duan, Y. Hu, et al., “Reconfigurable and Nonvolatile Ferroelectric Bulk Photovoltaics based on 3R-WS for Machine Vision,” Nature Communications 16 (2%2&): 23%.   
31. H. L. Park, H. Kim, D. Lim, et al., “Retina-Inspired Carbon Nitride-Based Photonic Synapses for Selective Detection of UV Light,” Advanced Materials 32 (2%2%): 1(%68((.   
32. H. Wang, Q. Zhao, Z. Ni, et al., “A Ferroelectric/Electrochemical Modulated Organic Synapse for Ultraflexible, Artificial Visual-Perception System,” Advanced Materials 3% (2%18): 18%3(61.   
33. W. Huh, D. Lee, S. Jang, et al., “Heterosynaptic MoS Memtransistors Emulating Biological Neuromodulation for Energy-Efficient Neuromorphic Electronics,” Advanced Materials 3& (2%23): 2211&2&.   
3). F. Liao, Z. Zhou, B. J. Kim, et al., “Bioinspired in-Sensor Visual Adaptation for Accurate Perception,” Nature Electronics & (2%22): 8)–(1.   
3&. B. Ouyang, J. Wang, G. Zeng, et al., “Bioinspired In-Sensor Spectral Adaptation for Perceiving Spectrally Distinctive Features,” Nature Electronics 7 (2%2)): 7%&–713.   
36. C. H. Lee, G. H. Lee, A. M. van der Zande, et al., “Atomically thin p–n Junctions With van der Waals heterointerfaces,” Nature Nanotechnology ( (2%1)): 676–681.   
37. H. Chen, X. Xue, C. Liu, et al., “Logic Gates Based on Neuristors made From Two-Dimensional Materials,” Nature Electronics ) (2%21): 3((–)%).   
38. C. Liu, H. Chen, S. Wang, et al., “Two-Dimensional Materials for Next-Generation Computing Technologies,” Nature Nanotechnology 1& (2%2%): &)&–&&7.

3(. C. Pan, C. Y. Wang, S. J. Liang, et al., “Reconfigurable Logic and Neuromorphic Circuits based on Electrically Tunable Two-Dimensional Homojunctions,” Nature Electronics 3 (2%2%): 383–3(%.   
)%. F. H. L. Koppens, T. Mueller, P. Avouris, A. C. Ferrari, M. S. Vitiello, and M. Polini, “Photodetectors Based on Graphene, Other Two-Dimensional Materials and Hybrid Systems,” Nature Nanotechnology ( (2%1)): 78%–7(3.   
)1. C. Zhou, Y. Zhao, S. Raju, et al., “Carrier Type Control of WSe Field-Effect Transistors by Thickness Modulation and MoO3 Layer Doping,” Advanced Functional Materials 26 (2%16): )223–)23%.   
)2. P. Chen, T. L. Atallah, Z. Lin, et al., “Approaching the Intrinsic Exciton Physics Limit in Two-Dimensional Semiconductor Diodes,” Nature &(( (2%21): )%)–)1%.   
)3. L. Mennel, J. Symonowicz, S. Wachter, D. K. Polyushkin, A. J. Molina-Mendoza, and T. Mueller, “Ultrafast Machine Vision With 2D Material Neural Network Image Sensors,” Nature &7( (2%2%): 62–66.   
)). H. Jang, H. Hinton, W. B. Jung, et al., “In-Sensor Optoelectronic Computing using Electrostatically Doped Silicon,” Nature Electronics & (2%22): &1(–&2&.   
)&. Y. Zhou, Y. Wang, F. Zhuge, et al., “A Reconfigurable Two-WSe -Transistor Synaptic Cell for Reinforcement Learning,” Advanced Materials 3) (2%22): 21%77&).   
)6. Y. Zhou, J. Fu, Z. Chen, et al., “Computational Event-Driven Vision Sensors for In-Sensor Spiking Neural Networks,” Nature Electronics 6 (2%23): 87%–878.   
)7. D. Chen, D. A. Stow, and P. Gong, “Examining the Effect of Spatial Resolution and Texture Window Size on Classification Accuracy: An Urban Environment Case,” International Journal of Remote Sensing 2& (2%%)): 2177–21(2.   
)8. S. P. Kannojia and G. Jaiswal, “Effects of Varying Resolution on Performance of CNN based Image Classification An Experimental Study,” International Journal of Computational Science and Engineering 6 (2%18): )&1–)&6.   
)(. M. Si, A. K. Saha, S. Gao, et al., “A Ferroelectric Semiconductor Field-Effect Transistor,” Nature Electronics 2 (2%1(): &8%–&86.   
&%. G. F. Nataf, M. Guennou, J. M. Gregg, et al., “Domain-Wall Engineering and Topological Defects in Ferroelectric and Ferroelastic Materials,” Nature Reviews Physics 2 (2%2%): 63)–6)8.   
&1. Y. Zhou, D. Wu, Y. Zhu, et al., “Out-of-Plane Piezoelectricity and Ferroelectricity in Layered α-In Se Nanoflakes,” Nano Letters 17 (2%17): &&%8–&&13.   
&2. T. A. Anusudha, “A Novel Memristor Model for the Nonlinear Memristor Devices,” Transactions on Electrical and Electronic Materials 2) (2%23): (1–1%1.   
&3. F. Xue, X. He, Y. Ma, et al., “Unraveling the Origin of Ferroelectric Resistance Switching Through the Interfacial Engineering of Layered Ferroelectric-Metal Junctions,” Nature Communications 12 (2%21): 72(1.   
&). P. Lopez-Varo, L. Bertoluzzi, J. Bisquert, et al., “Physical Aspects of Ferroelectric Semiconductors for Photovoltaic Solar Energy Conversion,” Physics Reports 6&3 (2%16): 1–)%.

# Supporting Information

Additional supporting information can be found online in the Supporting Information section.

Supporting File: adma72232-sup-%%%1-SuppMat.docx.