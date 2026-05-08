---
title: "DERMIS: End-to-End Design of a Fully Integrated Large-Area Grasp-State-Adaptive Tactile\\"
authors:
  - "Mark Daniel Alea"
  - "Maria Atalaia Rosa"
  - "Michael Kraft"
  - "Kris Myny"
  - "Georges Gielen"
date: "2025-10-01"
year: "2025"
journal: "IEEE Transactions on Biomedical Circuits and Systems"
abstract: "This paper presents the design of a high-resolution fully-integrated tactile sensor\\"
abstract_cn: "本文提出了一种高分辨率全集成触觉传感器系统DERMIS，采用柔性薄膜晶体管技术实现大面积电子皮肤。讨论了端到端设计策略——从传感器到读出电路再到片上特征提取——如何实现高效系统重配置，以首创性地实现受生物启发的抓握状态自适应触觉传感器。与现有仅检测滑动的触觉传感器相比，DERMIS系统还能测量关键接触线索，包括摩擦力、接触开始/结束、抬升开始/结束，这得益于一种新型差分电容传感器结构，能够独立感测剪切力和法向力，以及协同设计的模拟域前端直接提取这两个分量。此外，由于对这些抓握状态相关接触参数的模拟编码，系统避免了复杂的离线滑动提取算法。每个触觉像素的读出声称实现了最先进的72\\"
keywords:
  - "[[Tactile sensing]]"
  - "[[Electronic skins]]"
  - "[[Thin-film transistor]]"
  - "[[Neuromorphic computing]]"
cite: "[1] Alea M D, Rosa M A, Kraft M, et al. DERMIS: end‑to‑end design of a fully integrated\\"
aiSum: "DERMIS触觉传感器系统：基于a-IGZO TFT的柔性大面积电子皮肤，端到端设计，差分电容结构独立感测剪切/法向力，每个触觉像素72 µW功耗、0.36 mm²面积、2\\"
confidence: "medium"
wiki_concepts:
  - "[[Neuromorphic computing]]"
---

# DERMIS: End-to-End Design of a Fully Integrated Large-Area Grasp-State-Adaptive Tactile Sensor System on a-IGZO TFT

Mark Daniel Alea ID , Graduate Student Member, IEEE, Maria Atalaia Rosa ID , Michael Kraft ID , Member, IEEE, Kris Myny ID , Senior Member, IEEE, and Georges Gielen ID , Fellow, IEEE

Abstract—This paper presents the design of a high-resolution fully-integrated tactile sensor system, called DERMIS, implemented in a flexible thin-film transistor (TFT) technology for large-area electronic skins. It discusses how an end-to-end design strategy – from the sensor to the readout and to the on-chip feature extraction – enables efficient system reconfiguration to implement a first-of-its-kind and biologically-inspired grasp-stateadaptive tactile sensor. In contrast to existing tactile sensors that only detect slip, the DERMIS system also measures key contact cues, including friction, contact onset/offset, and lift-off onset/offset, enabled by a novel differential capacitive sensor structure that independently senses shear and normal forces and a co-designed front end that directly extracts both components at the analog domain. Furthermore, due to the analog-based encoding of these grasp-state-dependent contact parameters, the system avoids the use of complex offline slip-extraction algorithms. The per-taxel (tactile pixel) readout consumes a state-of-the-art 72 µW power consumption and occupies 0.36 mm2 area while achieving a human-like 2 mNRMS force resolution at 0.6 mm pitch. This work demonstrates our solution for the first time in a true largearea prototype of 9×4 mm2.

Index Terms—tactile sensing, electronic skins, slip detection, thin-film technology, neuromorphic, end-to-end design.

# I. INTRODUCTION
  - "[[Neuromorphic computing]]"

F INE grasp-state-dependent force sensing, as performed byhuman hands during dexterous object manipulation, is human hands during dexterous object manipulation, is likewise crucial for robotic and neuroprosthetic applications (Fig. 1). Depending on the current grasp state [1] (Fig. 1(b)), mechanoreceptors in the human hand sense a variety of contact parameters with high spatial resolution: (a) the onset/offset of contact (based on the normal force), (b) friction (extracted from the shear force), (c) onset of lift-off (based on the change in the shear force) and (d) slip (based on the normal and shear forces). When manipulating objects, the brain utilizes sensory predictions and tactile afferent signals to adapt its motor response across sequential action phases, monitoring contact events that trigger rapid corrective actions [1]. Therefore,

Manuscript created October, 2025.

Mark Daniel Alea and Georges Gielen are with ESAT-MICAS, KU Leuven, 3001 Leuven, Belgium (email: mark.alea@kuleuven.be; georges.gielen@kuleuven.be).

Maria Atalaia Rosa and Michael Kraft is with ESAT-MNS, KU Leuven, 3001 Leuven, Belgium (email:maria.rosa@kuleuven.be and michael.kraft@kuleuven.be).

Kris Myny is with ES&S, KU Leuven, 3590 Diepenbeek, Belgium (email: kris.myny@kuleuven.be).

![](images/2c9fa159f969f8d9c8ff8169406a326136d9f21ea1ec150dae7ff2e7d162be3e.jpg)

![](images/69e29f22d2d7358f0c17513310e09fb4a47352891b539c37b49bc0466ad4590a.jpg)  
Fig. 1: a) The high-spatial-resolution tactile sensor allows detecting localized slip, discriminating between incipient and gross slips. Object slips are typically characterized by an inner stick region (in green) where incipient (partial) slip happens, and an outer region (in red) where gross slip is seen. (b) Different grasp states during object manipulation. The illustrative image was generated with assistance from OpenAI’s ChatGPT image generation tool.

adding grasp-state-aware force-sensing capabilities into tactile sensors is crucial in real-world grasp applications.

Contrary to common electronic skin (e-skin) designs, where only the normal force is measured, grasp-state-aware sensing also requires shear and torsional force detection [2]. Meanwhile, those e-skin designs that can measure shear force are limited to slip detection, neglecting the detection of these other crucial contact parameters relevant to the different stages of grasping. Such requirement for complex force detection typically complicates the sensor and its readout, reducing the sensing spatial resolution and increasing the number of mechanically-moving parts (Fig. 2(a)).

Prior work [3] uses the commercial BioTac sensor, a liquidfilled biomimetic fingertip with an impedance electrode array, to estimate forces and classify slip. Slip is detected from the high-pressure signal, with a neural-network classifier distinguishing slip types. However, this fingertip sensor is bulky and expensive, making it unsuitable for large-area, high-resolution tactile arrays.

On the other hand, an approach completely devoid of complex force sensing is detecting slip through micro-vibrations, generated when a textured object slides across the sensor. Extracting slip from such sensor output is then done by applying envelope detection [4] or transforms [5] to the captured signal. Bulky, expensive shear sensors are avoided in [6] by using arrays of normal force sensors. Combined with computing the inter-frame cross-correlations, the lateral and torsional movement of the object in contact with the sensor array is then extracted to determine slip. Thus, in general, slip detection that relies on simpler sensors often demands more complex upstream algorithms [4], [5], [6].

Another approach to slip detection is a friction-based approach [7] by which the normal and tangential forces are acquired during incipient slip. This technique hinges on the fact that to prevent slip, the normal force, $f _ { n o r m }$ , applied by the grasp should be higher than $f _ { t a n } { \cdot } \mu _ { s }$ , where $f _ { t a n }$ is the tangential force at the contact and $\mu _ { s }$ is the static friction coefficient. While, in theory, simple algorithms would suffice to detect slip, this approach requires bulky and expensive multi-axial force/torque (F/T) sensors to detect the tangential forces. Thus, to fully leverage this approach, miniaturizing the multi-axial force sensors is essential, as demonstrated in the DERMIS design.

To match the human somatosensory system, the requirements for next-generation tactile sensors must be based on the low-latency capabilities of the human hands to detect slip with high spatial resolution and to detect the relevant contact parameters that depend on the current grasp state. Human skin, due to its mechanical compliance, is able to detect complex tensile, compressive, and torsional forces during object handling. The high density of receptors on the fingertips is then hypothesized [8] to encode the moving strain wave with a spatiotemporal spike pattern towards the nervous system.

Current tactile sensors (Fig. 2(a)&(b)), however, have low spatial resolution, hardware-expensive upstream slip detection algorithms and, as discussed above, cannot reconfigure dynamically depending on the grasp state. In this paper, which expands on our previous work [9], [10], we highlight our DERMIS end-to-end design approach [11], that takes advantage of the flexibility of a full-custom top-down approach – from the sensor to the readout and to the on-chip processing – to implement:

• a high-spatial-resolution shear- and normal-forceencoding capacitive tactile sensor, with a   
• pitch-matched spike-based readout in a large-area flexible technology (Fig. 2(c)), that implements   
• low-latency analog-based slip encoding and grasp-stateadaptive force sensing, and   
• embedded grasp-state-aware feature extraction and data compression.

This paper is organized as follows. Section II describes the use of a thin-film technology (TFT) to implement a large-area tactile sensor system design. Section III discusses the end-toend system design in the DERMIS e-skin approach. Section IV highlights the detailed circuit design of the DERMIS chip. Section V shows our experimental results, while Sections VI

provides further discussions and some future outlook. Section VII draws conclusions.

# II. TFT-BASED TACTILE SENSING SYSTEM

While a modern fully-integrated Si-CMOS-based highdensity e-skin system has been demonstrated in a prior work [12], the large-area sensing requirement for slip detection demands implementing the system on a different type of substrate. Previous large-area flexible e-skins are implemented on exotic substrates and, thus, lack the monolithic integration capabilities to implement the more complex embedded readout and processing discussed above [13]. To achieve the various requirements and capabilities required in next-generation integrated slip detection and grasp-state-adaptive tactile sensing systems, a thin-film transistor (TFT) technology-based approach is an attractive alternative (Fig. 2(c)).

![](images/e221cb529e19acd6573d30d1f7670375ff115ca7a129aa946a2a8f1aafb4d859.jpg)  
Fig. 2: a) Existing tactile sensing systems lack the level of integration to allow for power-efficient and low-latency slip detection. b) Hybrid approaches are limited in scalability. c) To match the high spatial resolution and the fast localized slip detection capability of human hands, next-generation slip detection systems can leverage the integration potential of large-area thin-film transistor (TFT) technology.

![](images/e448633c667c603af6ea1aaa0ac9a539d464b79474ee8bfedebf459dd8249e34.jpg)  
Fig. 3: Event-driven readout scales its signal sampling rate upon the instantaneous bandwidth of the tactile input signal, converting the continuous-time sensor signal into an asynchronous spike train.

In contrast to Si-CMOS-based designs, TFT-based solutions are larger in area and flexible, but they are constrained by the performance of the monolithic devices available. TFT transistors typically have lower carrier mobilities and higher threshold voltages [14], resulting in larger device sizes and supply voltages. Furthermore, a-IGZO-based designs today are unipolar (i.e., NMOS only). As a consequence, implementing complex digital computation, possible in Si-CMOS with its dense integration, becomes a challenge in TFT. TFT devices also suffer from larger flicker noise, large mismatch, and fabrication defects [15]. Therefore, large-area TFT-based designs

for embedded slip detection would benefit from largely analogbased algorithms with simple digital blocks, as proposed in this paper.

![](images/4c6462dfd097805ab9d934c9656a778b0a5e840359c22b36311b06bfa10978ad.jpg)  
Fig. 4: Top-level architecture of the proposed DERMIS e-skin system. Separate readouts for the shear sensors in both X and Y orientations allow the detection of the shear direction. An asynchronous Address Event Representation (AER) interface sends out an output spike train after sensor conversion. To extract a measure of the shear force, a ratiometric mode (in red) uses the output of a neighboring taxel’s analog frontend (AFE) unit as a reference for ADC quantization, essentially performing a division. The detailed per-taxel circuit architecture can be found in Fig. 11

Adaptive event-based signal acquisition [16] is beneficial as both fast slip sensing (<10 ms for safe grasping) and sparse spatiotemporal sampling (during periods of inactivity) are required (Fig. 3). A recent work [17] used event-driven detection of tactile signals, but relied on off-chip sensors measuring only normal force, limiting the scalability and having no friction/slip detection (Fig. 2(b)). Sensor-to-readout integration [12] addresses this with dense per-taxel connections, but is costly for large areas. TFT implementations offer a scalable alternative, though prior work [15] so far retained off-chip sensing limitations. Our DERMIS fully-integrated solution combines capacitive shear sensors with event-based, reconfigurable readout in a large-area TFT technology to enable high-resolution grasp-state-dependent force sensing, including slip detection.

Table I compares our proposed DERMIS solution to other existing slip-detecting tactile sensor systems. The detection mechanism is bioinspired: humans rely on prior knowledge of an object’s friction, formed through visual cues and past experience (i.e., its static friction coefficient), to adjust the normal force in response to changes in shear force and thereby detect emerging slip [1]. The proposed solution can measure slip directly in a non-compute-intensive manner, and therefore is a viable approach for integration on a digital-logicconstrained TFT process. This analog-domain-based acquisition of slip is in contrast to prior digital-heavy transform- [5]

or cross-correlation-based [6] methods. Our approach infers slip using a known static friction coefficient from measured normal and shear forces. However, extracting shear requires normalizing the differential capacitance by its common-mode value (Eq. (5)), which entails divider logic that is difficult to implement in the a-IGZO TFT technology used within the $0 . 6 { \times } 0 . 6 ~ \mathrm { m m ^ { 2 } }$ area budget (minimum inverter: $1 3 0 0 \ \mu \mathrm { { m } ^ { 2 } }$ vs. 10 $\mu \mathrm { { m } ^ { 2 } }$ in 40-nm CMOS).

# III. THE DERMIS APPROACH: END-TO-END DESIGN

Our proposed implementation focuses on a fully monolithic TFT design (Fig. 4). To allow grasp-state-dependent force sensing, the DERMIS system incorporates the following innovations: (a) miniaturized force sensors with both normal and shear force transductions, (b) a reconfigurable readout to encode the normal and shear forces, and (c) on-chip graspstate-aware data compression and feature extraction. We will now describe the system in greater detail.

# A. Sensors

Novel differential capacitive sensors allow for sensing both normal and shear forces in both X and Y directions $( e . g .$ , by rotating the sensor pattern perpendicularly), enabling graspstate-dependent measurements without the bulky form factor of traditional force/torque (F/T) sensors [2]. Shear and normal forces can be measured via simple arithmetic operations on the differential capacitance, as will be discussed in detail in Section III-B. The capacitive sensor structure used is shown in Fig. 5. The capacitive sensors are formed through the overlap of a floating top electrode (Al) and two bottom electrodes (TFT top metal, Al), forming two capacitances in series. The sensors are fabricated on a wafer carrier through a novel sacrificial molding layer approach [19]. The structure is then integrated on the TFT substrates through an alignment-based post-processing step after regular TFT chip fabrication.

![](images/9fdd9bc1f50e41ac74f090d6e34b1aca633a1dad24fc32174cd641aded24f590.jpg)  
Fig. 5: Differential capacitive sensor for both normal and shear force detection, designed to be integrated on top of a TFT substrate with integrated readout electronics. The bottom part gives the equations to extract the normal and shear forces.

The dynamic range of the capacitive sensor is modeled in Fig. 6, considering changes in both the shear and normal forces, which modulate $\Delta x$ and $\Delta z ,$ respectively.

TABLE I: Comparison of DERMIS with state-of-the-art slip-detecting tactile sensor systems   

<table><tr><td></td><td>[4]</td><td>[5]</td><td>[6]</td><td>[3]</td><td>[7], [18]</td><td>This work (DERMIS)</td></tr><tr><td>Sensor Type</td><td>Vibration</td><td>Vibration</td><td>Normal Force</td><td>Shear + Normal Force</td><td>Shear + Normal Force</td><td>Shear + Normal Force</td></tr><tr><td>Slip Detection Algorithm</td><td>Envelope Detection</td><td>Transforms</td><td>Inter-Frame Cross-Correlation</td><td>Classifier-Based</td><td>Friction Extraction (post-quantization)</td><td>Friction Extraction (pre-quantization)</td></tr><tr><td>Direct Slip Measurement?</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>TFT Hardware-Friendly?</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr></table>

![](images/242a572bcbae286ecec2a5e17906bcf04df52a916d0cbe954d5a8857d18d4012.jpg)  
Fig. 6: Modeled capacitive dynamic range of the integrated multiaxial tactile sensors with 600-µm pitch.

# B. Readout

The proposed readout (Fig. 7) takes advantage of the versatile nature of the differential capacitive sensors, inherently allowing the extraction of both shear and normal forces through simple reconfiguration of the phases of the capacitor stimulation voltages. The normal force can be extracted by applying out-of-phase stimulation waveforms on $C s p$ and Csn, resulting in a voltage output that is proportional to the sum of the two capacitances after demodulation and filtering (Fig. 7(a), MODE:F N ). A ratiometric mode (Fig. 7(b)&(c), MODE:F S) allows to extract the shear force by using the output of a neighboring taxel as the reference for the quantization step of the ADC (essentially performing a division). The readout assumes that the spatial resolution is sufficiently high such that the normal force measured by the neighboring taxel is approximately the same as that of the main taxel. A low-power mode (MODE:IDLE) allows the chopping mechanism to be turned off, permitting a reduced bandwidth and consequently reduced power requirements for the frontend OTA.

The AFE output expressions across different grasp states are summarized in eq. 2 to 6, where $V _ { T X }$ is the peak-to-peak voltage of the square-wave input applied to the equivalent sensors top plate $( e . g . ,$ , by simplifying two series capacitors into a single capacitor on one side of the differential sensor), V OCM is the output common-mode voltage (set by the common-mode feedback), and Cf the feedback capacitance. The feedback capacitance can be configured in two ways: via tha $G A I N _ { H I }$ setting and by operating in ratiometric mode (M ODE : F S). As shown in Fig. 7(c), spikes are generated whenever the main taxel AFE output exceeds the neighboring taxel AFE output (i.e., ratiometric). To guarantee that spikes are generated, the neighbor taxel AFE output waveform is intentionally attenuated by a factor $K = 1 / 4 ,$ , as shown in eq. 7, by increasing the feedback capacitance 4× from 40 fF to 160 fF in normal gain setting $( G A I N _ { H I } { = } ^ { \prime } 0 ^ { \prime } )$ and 10 fF

![](images/65fedc704025ac6077e3b5e51393d75e0f47236886a3ff773bd14cad6af1b3d4.jpg)

![](images/8d20863d65fbb3ca261c71edd48dbe38aa6d3e51f3a84bed98a98f7b1698526c.jpg)

![](images/ecf17e9b1843d3039f7e0b26bd396530046102506beda14b7fc20c3a26b6b437.jpg)  
  
(c)   
Fig. 7: Extracting the normal and shear forces via the proposed DERMIS readout: (a) this configuration measures the normal force, while (b) this ratiometric configuration measures the shear force, as depicted in (c).

to 40fF in high gain setting $( G A I N _ { H I } { = } ^ { \prime } 1 ^ { \prime } )$ . The AFE output swing considering the input differential capacitance range is shown in Fig. 8.

In MODE:F N, the non-linear term in the AFE output (eq. 3) is reduced because the sensor exhibits small capacitance values throughout its dynamic range (Fig. 9).

$$
\begin{array}{l} V _ {\mathrm {O U T}} (\mathrm {r a w}) = \frac {2 V _ {\mathrm {T X}} \left(\beta_ {2} - \beta_ {1}\right)}{\beta_ {1} + \beta_ {2}} + \frac {2 V _ {\mathrm {O C M}} \left(\beta_ {1} - \beta_ {2}\right)}{\beta_ {1} + \beta_ {2}} (1) \\ = \frac {V _ {\mathrm {T X}} \left(C _ {s p} - C _ {s n}\right)}{C _ {s p} + C _ {s n} + 2 C _ {f}} \quad \propto \text {r a w d i f f . c a p . v a l u e} (2) \\ \end{array}
$$

$$
\begin{array}{l} \because V _ {\mathrm {O C M}} = \frac {V _ {\mathrm {T X}}}{2} \\ \because \beta_ {1} = \frac {C _ {f}}{C _ {s p} + C _ {f}} \quad \beta_ {2} = \frac {C _ {f}}{C _ {s n} + C _ {f}} \\ \end{array}
$$

![](images/943e1a0a31838e5961f49c568706362f7235a65122270b4a608962ae93d680de.jpg)  
Fig. 8: Modeled voltage swing for MODE : raw considering the input differential capacitance range in Fig. 6. Inset showing the range wherein SNR<0dB.

$$
V _ {\mathrm {O U T}} (\mathrm {F N}) = \frac {V _ {\mathrm {T X}} \left[ 2 C _ {s p} C _ {s n} + C _ {f} \left(C _ {s p} + C _ {s n}\right) \right]}{C _ {f} \left(C _ {s p} + C _ {s n} + 2 C _ {f}\right)} \tag {3}
$$

$$
V _ {\mathrm {O U T}} (\mathrm {F N}) \approx \frac {V _ {\mathrm {T X}} \left(C _ {s p} + C _ {s n}\right)}{C _ {s p} + C _ {s n} + 2 C _ {f}} \quad \propto F _ {\mathrm {n o r m a l}} \tag {4}
$$

$$
\begin{array}{l} V _ {\text {O U T}} (\mathrm {F S}) = \frac {V _ {\text {O U T}} (\text {r a w})}{K V _ {\text {O U T}} (\mathrm {F N})} \propto \frac {C _ {s p} - C _ {s n}}{C _ {s p} + C _ {s n}} \rightarrow \propto F _ {\text {s h e a r}} (5) \\ V _ {\mathrm {O U T}} (\mathrm {i d l e}) = \frac {2 V _ {\mathrm {O C M}} \left(C _ {s n} - C _ {s p}\right)}{C _ {s p} + C _ {s n} + 2 C _ {f}} (6) \\ \because C _ {f} ^ {\prime} = 4 C _ {f} \Rightarrow K = \frac {1}{4} (7) \\ \end{array}
$$

![](images/02358d629b6915b2e77a8f51e39ef6446a67ade6d086699c539b17c536ca7ede.jpg)

![](images/f644d6752d4c3efc209594aeb0fe1b6b8bed8f6fae41b1d7a7b2ce1e8532bd97.jpg)  
Fig. 9: The nonlinear term in the derived AFE output voltage contributes a small error term (eq. 3). AFE output versus the normal force (as expressed by Csp+Csn) for (a) Cf=10 fF and (b) Cf=100 fF. Inset plots show the error (%) due to this nonlinear term at the maximum Csp+Csn, denoted by the vertical dashed line.

![](images/ee06124a81065a5d9ca9d39d4c7ae5c761d628a0e93ea8733d2b9048e516bb41.jpg)  
Fig. 10: State diagram during the evolution of grasping movements. Similar to humans, grasp manipulation involves planning the next action depending on the extracted feature at the current state.

TABLE II: Force features extracted for different grasp states.   

<table><tr><td>STATE</td><td>FORCE MEASURED</td><td>FEATURE EXTRACTED (DOUT=&#x27;1&#x27;)</td></tr><tr><td>IDLE</td><td>Normal Force</td><td>Onset of contact</td></tr><tr><td>LIFTOFF</td><td>Shear Force</td><td>Lift-off</td></tr><tr><td>MANIPULATION</td><td>Normal &amp; Shear Force</td><td>Slip</td></tr></table>

# C. Embedded Grasp-State-Based Feature Extraction

The human somatosensory system relies on fast feature extraction in navigating the various stages of grasping (e.g., fast object slip detection to adjust the grip force). Inspired by this, the DERMIS prototype system performs grasp-stateaware feature extraction while effectively performing on-chip data compression locally to reduce the detection latency. As discussed in Section I, dexterous object manipulation consists of different grasp states, which involve planning the next action depending on the extracted features at the current grasp state. This evolution is depicted in Fig. 10. Table II summarizes the relevant feature extracted per state. The path highlighted in green depicts the actions performed before active object manipulation (i.e., picking an object from a table), while the path in red depicts post-manipulation movements (i.e., placing the object on a table).

# IV. DETAILED CIRCUIT DESIGN

# A. System Architecture

The DERMIS readout chip prototype includes a 2x8 taxel array with per-taxel readout, implemented in a unipolar 0.6 µm a-IGZO technology. Each per-taxel readout combines a capacitive frontend and an event-based level-crossing (LC) data converter (Fig. 11). The frontend comprises a fully differential capacitively-coupled amplifier, with the differential capacitive

sensor directly used as the input capacitance, eliminating the need for extra charge amplifiers [20]. The LC converter [21] asynchronously detects signal changes, using window comparators to generate bipolar spikes encoded as addresses by an on-chip AER interface [22]. Per-taxel digital blocks, implemented with differential logic for reducing the static power [23], latch the LC events, which are then arbitrated and transmitted off-chip by the AER interface. The interface, which arbitrates outputs from multiple taxels, uses pseudo-CMOS logic for a good noise margin, trading off increased static power [23].

![](images/090326420a5d1a54b8204d6d7a4160fb56cb6aa51c824ab6a1143f60473b60c8.jpg)  
Fig. 11: Schematic of the per-taxel readout (2x8 taxels on-chip) showing the fully-differential AFE and the event-driven LC-ADC. The comparator inputs use of neighboring taxel AFE outputs during the ratiometric mode.

# B. AFE OTA

Despite its tight $0 . 0 4 ~ \mathrm { m m ^ { 2 } }$ area budget, the fully differential amplifier (Fig. 12) achieves an open-loop gain of 30 dB using a “pseudo-PMOS” load implemented with a positive feedback network [24]. The positive feedback effectively keeps the $V _ { G S }$ of the NMOS load constant, eliminating its transconductance contribution to the small-signal gain, keeping only the higher intrinsic output impedance. The common-mode feedback (CMFB) amplifier is implemented with an NMOS diode-load OTA.

# C. Autozeroed Comparator

Two continuous-time (CT) comparators detect the residue voltage’s level crossings (±1 LSB), each using a 3-stage openloop amplifier: a dual-differential input pre-amplifier and two resistive-load common-source (CS) stages (Fig. 13). The preamplifier’s dual-differential input rejects common-mode noise, including switching artifacts, and allows comparison with a neighboring taxel’s differential output in the ratiometric mode. The comparator is auto-zeroed (AZ) after each level crossing (i.e., under non-uniform sampling), which reduces flicker noise, but typically introduces noise folding and elevates the overall noise floor [25]. Because non-uniform sampling is inherently aliasing-free [26], this issue is however effectively

![](images/a381630d2196ee2ee5930d2ed41c0df1d57c9138e3d26ff374521d63e47d9867.jpg)  
Fig. 12: Schematic of the fully-differential AFE OTA, highlighting the pseudo-PMOS load (through positive feedback) to boost the gain.

mitigated. The proposed non-uniform AZ technique has been modeled and simulated. Fig. 14(a) shows the flicker noise attenuation without noise folding as compared to a uniform AZ, while Fig. 14(b) compares the SNR, SNDR, and SFDR, highlighting the benefits of the non-uniform AZ. The increased SFDR can be attributed to the signal-dependent timing of level crossings and autozero updates in the LC operation, which can produce input-correlated error and harmonic distortion. In contrast, uniform-sampling AZ uses clock-timed updates, making the error less input-correlated and thus reducing the distortion.

An added advantage of the high-pass LC conversion is that it decouples the first CS stage’s biasing from the preamplifier’s DC output (set by the NMOS load VGS), thereby maximizing the gain of the next stage. Large resistive loads bias the CS stages, reducing the power consumption by leveraging the high-resistivity devices available in TFT technology.

![](images/ac54d21a32390264dd0d74406ab505508cd462f6542d86a5a537f3c1c1a938c5.jpg)  
Fig. 13: Schematic of the non-uniform-sampling autozeroed comparator.

# D. Per-Taxel Grasp-State-Based Control Logic

The DERMIS per-taxel readout (Fig. 11) can be reconfigured to detect grasp-state-dependent forces, as summarized in Table III. This happens by adjusting the phases of the $V _ { T X }$ switches $( \phi _ { t x p / n } )$ on the capacitive sensors Csp and Csn, driven to be either $V _ { T X } \ ( 3 \mathrm { V } )$ or 0V. The $V _ { T X }$ switches are driven with a 6-V gate drive via a level shifter. The chopper demodulation switch gate logic can also be reconfigured $\left( \phi _ { r x p / n } \right)$ , and is permanently asserted during the IDLE mode (non-switching mode). The cmp signal is useful during ratiometric modes, where it decides whether to take the local

![](images/5da21c22daab557363d19790a10601ff73b2b970e701a331dc45584d83b7bc0c.jpg)

![](images/f62fe7e875ed063a4311942b29631855e9e32dcb846568d4dadedb2eefb1c75b.jpg)  
Fig. 14: (a) Simulated PSD comparing the effect of non-uniform sampling versus a conventional uniform sampling autozeroing. Raw PSD with flicker noise added for reference. (b) Achieved SNDR, SNR and SFDR across the following: LC-ADC (no autozero), LC-ADC (autozero), and uniform-sampling autozero.

TABLE III: Truth table to reconfigure the readout depending on the grasp state (F N , F S(X), F S(Y ), raw, or IDLE modes)   

<table><tr><td colspan="4">TAXEL X</td><td colspan="4">TAXEL Y</td><td>IDLE</td><td>Signal</td></tr><tr><td>FN</td><td>FS(Y)</td><td>FS(X)</td><td>raw</td><td>FN</td><td>FS(X)</td><td>FS(Y)</td><td>raw</td><td></td><td></td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>X</td><td>TX_CLK</td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>φtxp</td></tr><tr><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>φtxn</td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>φrx</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>cmp</td></tr></table>

AFE outputs or the neighboring taxel’s AFE outputs as inputs to its comparator. The on-chip grasp-state-based control logic is implemented with differential logic for reduced static power consumption.

# V. EXPERIMENTAL RESULTS

# A. Sensor Measurements

To test the sensor fabrication methods and validate the sensing principles, a protoype capacitive sensor with larger top metal dimensions and thicker PDMS has been used. The larger dimensions allow easier handling and alignment of the sensor with the test PCB backplane. The capacitive sensor has been characterized using a commercial readout board (EVAL-AD7746EBZ, Analog Devices Inc.). Fig. 15(a) shows the measurement setup where a metal tip attached to a force indenter (MTS Criterion) is slid over the sensor (oriented parallel to the tip) to demonstrate the lateral force application. Fig. 15(b) shows the capacitive readout readings, including the

extracted values of the normal and shear forces, following the equations in Fig. 5. The measured sensor responses (Fig. 16) from multiple sensor samples reflect the spatial variation that one would observe in an array. All samples were fabricated on the same wafer, so this captures the inherent withinwafer variations across devices and thus closely emulates the behavior of an arrayed sensor.

![](images/7e2b1b2502bf1b3e34e8873738f6c3201a0d4d4d18652bbf7120f8d1abbfdf9d.jpg)  
(@)

![](images/4b6928109e093ae26a52dcf6589dc4481e0263779c69f82055cfad9ed7e70e18.jpg)  
  
Fig. 15: Measurement setup and capacitive readout readings (using a commercial readout for demonstration) used to detect slip. The bottom curves indicate the measured normal and shear forces.

![](images/e6cc9f252f6b941266abefb68cecc178cd87588a0307fbda31b7a27f184ad5d0.jpg)

![](images/6dd0ef15e044288cb5c9335d687dcc796bad700d0e594cf26583b199bc868307.jpg)  
Fig. 16: Capacitance versus pressure measurements for multiple sensor samples.

# B. Chip Measurements

The DERMIS design has been prototyped in an NMOSonly 0.6 µm a-IGZO TFT process. The chip measurement setup is shown in Fig. 17, while the chip micrograph is shown in Fig. 18. For the electrical characterization, the analog frontend (capacitance-to-voltage) output has been measured using external digitally-controlled capacitors as input (Fig. 19. Off-chip attenuation capacitances can be used to perform sensor calibration. The off-chip capacitors can then be

![](images/cbda56d6a601248a54d3068bf1d45fe8f3cd641297e30202119990d35ad7ac46.jpg)  
Fig. 17: Chip measurement setup. The frontend characterization input signal is applied via a commercial difference amplifier that combines both a DC offset and an AC input signal (from Rigol DG3061A). The replica frontend output and input, and the on-chip temperature sensor output are acquired by a Keysight MXR058A. The chip’s current consumption is measured by a Keysight B2061A SMU and Keysight E36312A power supplies. The output spikes during the experiments are recorded off-chip via an ARM Cortex M7 $\mu C$ (600MHz clock) with a software-based AER interface communicating with the chip’s AER interface.

integrated into future designs. Adding capacitors to the AC ground does increase the amplifier’s noise gain. However, in the intended on-chip implementation this effect is negligible because $C _ { f } \gg C _ { \mathrm { a t t } }$ and $C _ { \mathrm { s e n s o r } }$ .

The inherent chopping mechanism (Fig. 7) attenuates the flicker noise (Fig. 20), resulting in a force-referred input resolution of 2 mNRMS (0.61 $\mathrm { f F } _ { R M S }$ for 0.3 pF/N sensor sensitivity), which outperforms human skins [27]. Each pertaxel readout has a power consumption of $7 2 ~ \mu \mathrm { W }$ and occupies an area of 0.36 mm2 (Fig. 18(b)). The per-taxel power consumption is dominated by the static power consumption of the digital logic. Meaningful measurement of the featureextraction block was not possible because the large off-chip capacitors used to test the prototype chip make the AFE’s nonlinear term dominant (Fig. 9), preventing realistic normalforce emulation.

The per-taxel level-crossing ADC achieves a peak ENOB of 6.16 bits (Fig. 21(a)), resulting in a Walden FOM of 1 nJ/c · s. Fig. 21(b) shows the SNDR versus frequency. It is noted that the SNDR degrades with increasing input frequency, which will be explained further in Section VI. It is, however, important to note that the target SNDR is still achieved across the target bandwidth. Prior work [12] shows that a low spikeencoding precision (3 to 5 bits) is not only sufficient, but also prevents overfitting and therefore maximizing the classification accuracy. This overfitting prevention is likely due to the low spike rates of the low-precision conversion.

Comparisons with state-of-the-art work in TFTimplemented AFEs and ADCs are shown in Tables IV and V, revealing superior chip area (400× lower for the

![](images/9fa92f4387ebd95a417b7a037451d250a4f66ef16bcdcdb8ee2d236582be6ba1.jpg)  
(a)

![](images/fe6f3a4dc631599dfb71f827484bde404f3fecdb9ed15f5592a8a0b325698a54.jpg)  
  
Fig. 18: Chip micrograph: (a) The DERMIS prototype is shown, highlighting the $2 \times 8$ taxel array, the AER inteface, the feature extraction logic, and replica blocks for characterization. The chip’s taxels are wirebonded for off-chip sensor tests. (b) The per-taxel readout floorplan, pitch-matched to the 0.6mm shear sensing spatial resolution

AFE; 17× lower for the ADC), power consumption (60× lower), with comparable input-referred noise and Walden FOM. Our design attains similar noise levels at much lower power, because the noise is primarily set by the DC bias current, whereas prior solutions rely on high supply voltages that unnecessarily inflate power consumption for the same bias level. Table VI compares our proposed fully-integrated solution to prior state of the art tactile readout systems, highlighting the beyond state of the art 0.6-mm shear sensing resolution, while being the first to implement a large-area and flexible readout system with grasp-state-adaptive force sensing and embedded data compression. Despite being implemented in a coarse-lithography, transistor-performanceconstrained TFT process (relative to prior Si-CMOS work), the presented work achieves a per-taxel readout area and power consumption comparable to state-of-the-art designs. Compared to the state of the art in slip-sensing tactile

![](images/a2e8b06a11ea5353652599248f92f1fa32e902bf2455d740cd35cdb987123b39.jpg)  
Fig. 19: Input capacitance range of two taxel capacitance-to-voltage frontends (X0 and Y0) at $C _ { s p } ^ { } + C _ { s n } ^ { } = 2 9 . 4 ~ \mathrm { p F } ,$ , resulting in a $C _ { s p } -$ $C _ { s n }$ range of around $\pm \nobreakspace 1 6 \nobreakspace$ pF before the output saturates. Note that despite the large absolute values of $C _ { s p }$ and $C _ { s n }$ compared to the integrated sensors, the inherent normalization of the AFE output by the common-mode capacitance $C _ { s p } + C _ { s n }$ prevents saturation. The non-linearity at large $\bar { C } _ { s p } - C _ { s n }$ values is due to the relatively small open-loop gain (32 dB).

![](images/c99d323cddb3a66dad72023a69137a06f8da2080e075160c0f6f64230089134d.jpg)  
Fig. 20: Capacitance-referred PSD: compared with the chopping on (5 kHz) and off.

sensor systems, this work achieves the lowest readout power consumption (36× lower for the taxel array) and the best shear force sensing pitch (3.33× lower) (Fig. 22).

# VI. DISCUSSIONS

In this section, the effect of a correlated noise source to the ADC output SNDR and the dominant sources of the chip’s power consumption are discussed.

As explained in the previous section, the non-uniform sampling autozeroed readout reduces the effect of the flicker noise on the output spectrum. However, another correlated noise source has been identified as the main culprit to the observed SNDR degradation towards higher input frequencies. Levelcrossing ADCs inherently exceed the theoretical limit set by the amplitude quantizer resolution N due to its oversampling properties [33]:

$$
\mathrm {S N D R} = 6. 0 2 \cdot N + 1. 7 6 \tag {8}
$$

![](images/d49653c053294733aa1d8ac7d3efcdb8457952397c7dc0c30a99d3019f8e756a.jpg)

![](images/a9b54b6c371438598c2ebec3a0946b5b4ae7ddeeff29e3e22eb27d9b5ee55746.jpg)  
Fig. 21: (a) Measured LC-ADC Power Spectral Density (PSD). The input is 1 Hz sine wave, 6 Vpp (differential). The differential nature of the conversion inherently attenuates even-order harmonics.(b) Measured SNDR and SFDR across the input frequency. Throughout the desired bandwidth range, the target precision is achieved.

TABLE IV: Performance comparison with prior-art TFT-based readout systems.   

<table><tr><td></td><td>[28] ISSCC&#x27;16</td><td>[29] JSSC&#x27;23</td><td>[15] ISSCC&#x27;19</td><td>This work</td></tr><tr><td>Application</td><td>EEG</td><td>EMG</td><td>Tactile</td><td>Tactile</td></tr><tr><td>TFT Technology</td><td>a-Si</td><td>a-IGZO</td><td>ZnO</td><td>a-IGZO</td></tr><tr><td>BW [kHz]</td><td>0.2</td><td>30</td><td>N/A**</td><td>0.3</td></tr><tr><td>Vnoise,in (μVRMS)</td><td>5.14</td><td>94.7</td><td>N/A**</td><td>6.1***</td></tr><tr><td>Area (mm2)</td><td>50</td><td>16</td><td>60</td><td>0.04</td></tr><tr><td>Power / ch. (mW)</td><td>11</td><td>0.037</td><td>N/A**</td><td>0.0006</td></tr><tr><td>VDD(V)</td><td>55</td><td>26</td><td>N/A**</td><td>3</td></tr><tr><td>Readout Strategy</td><td>Hybrid*</td><td>Hybrid*</td><td>Hybrid*</td><td>TFT-only</td></tr></table>

∗Si-CMOS + TFT; ∗∗readout in CMOS; ∗∗∗input-referred, noise gain = (Cf + Cs)/Cf

Therefore, its SNDR is rather determined by timing errors associated with the samples and the precision of the synchronous re-timing interface [33] needed to reconstruct the input:

$$
\mathrm {S N D R} = - 2 0 \log_ {1 0} \left(\delta \times f _ {\mathrm {I N P U T}}\right) - 1 1. 2 \tag {9}
$$

where δ is the timing error and $f _ { I N P U T }$ is the signal input frequncy. These timing errors, beyond those intrinsic to the ADC itself, can be compounded by errors introduced during the asynchronous transmission of level-crossing times-

TABLE V: Performance comparison with prior-art TFT-based ADC implementations   

<table><tr><td></td><td>[30] ISSCC&#x27;17</td><td>[31] VLSI&#x27;25</td><td>[10] VLSI&#x27;25</td><td>This work</td></tr><tr><td>TFT Technology</td><td>a-IGZO</td><td>a-IGZO</td><td>a-IGZO</td><td>a-IGZO</td></tr><tr><td>μ [cm2/Vs] / Lmin [μm]</td><td>14 /15</td><td>10/0.6</td><td>10/0.6</td><td>10/0.6</td></tr><tr><td>ADC Architecture</td><td>ADSM</td><td>SAR</td><td>LC-ADC</td><td>LC-ADC</td></tr><tr><td>Peak ENOB [bits]</td><td>6.35</td><td>7.02</td><td>4.12</td><td>6.16*</td></tr><tr><td>BW [Hz]</td><td>300</td><td>32000</td><td>50</td><td>500</td></tr><tr><td>Area (mm2)</td><td>27.9</td><td>1.9</td><td>0.11</td><td>0.11</td></tr><tr><td>Power (mW)</td><td>2</td><td>1.7</td><td>0.007</td><td>0.072</td></tr><tr><td>Walden FOM [nJ/c.s.]</td><td>39</td><td>0.41</td><td>4</td><td>1</td></tr></table>

$^ { \ast } V _ { p p } = 6 V$ (full-scale differential), 1Hz, 1µs re-timing precision

TABLE VI: Performance comparison with recent tactile readout systems.   

<table><tr><td></td><td>[17]JSSC&#x27;24</td><td>[12]VLSI&#x27;23</td><td>[32]ISSCC&#x27;24</td><td>This work</td></tr><tr><td>Technology</td><td>55nmCMOS</td><td>0.18μmCMOS</td><td>0.18μmCMOS</td><td>0.6μma-IGZO TFT</td></tr><tr><td>Sensors</td><td>Capacitive</td><td>Piezoelectric</td><td>Capacitive</td><td>Capacitive</td></tr><tr><td>Shear sensing resolution</td><td>N/A*</td><td>N/A*</td><td>N/A*</td><td>0.6 mm</td></tr><tr><td>Readout Method</td><td>Event-Driven**</td><td>Event-Driven</td><td>Frame</td><td>Event-Driven</td></tr><tr><td>Readout Area (mm2)***</td><td>0.016</td><td>0.04</td><td>0.192†</td><td>0.33</td></tr><tr><td>Power (μW)***</td><td>1.6/7.2</td><td>0.012</td><td>0.75</td><td>72</td></tr><tr><td>Pitch-Matched to Sensors</td><td>NO</td><td>YES</td><td>NO</td><td>YES</td></tr><tr><td>Large-Area</td><td>NO</td><td>NO</td><td>NO††</td><td>YES</td></tr><tr><td>Flexible</td><td>NO</td><td>NO</td><td>NO</td><td>YES</td></tr><tr><td>Grasp-State-Adaptive Data Compression</td><td>NO</td><td>NO</td><td>NO</td><td>YES</td></tr></table>

∗normal force only; ∗∗post-acquisition; ∗∗∗per-taxel;   
†estimated; ††wireless network;

tamps. Prior LC-ADC implementations [33], [21] are predominantly single-channel prototypes and therefore rely on low-overhead digital logic to transmit samples. In contrast, to support real-life applications, this work transmits spikes from multiple channels while maintaining compatibility with neuromorphic processing hardware via an address-event representation (AER) interface. Intermittent stalls were observed in the AER interface, occasionally disrupting spike transmission and marginally affecting reconstruction accuracy. While the cause is not yet fully understood, modeling indicates that the behavior introduces event-rate-dependent colored noise, explaining the observed SNDR degradation (Fig. 23).

As shown in Fig. 22(a), the chip power consumption is orders of magnitude smaller than prior work, if only the taxel readout array is considered. Thus, the chip’s system power is dominated by the digital logic in both the AER and the data compression logic. This is due to the large static power consumption observed in the pseudo-CMOS logic cells used in this TFT technology. As discussed in the low-power per-taxel digital block, differential logic has a significantly lower static power consumption at the expense of a larger area. In this work, the relative maturity and low area of the

![](images/d39b1a182788f690023051bdd6a9d2c20106c0cf91fb813ea04d36334c240017.jpg)

![](images/671495479025354d18ad12ba9f796a048edf8ab51589017efea8ff45c4c35142.jpg)  
(a)   
(b)   
Fig. 22: Comparison with existing slip-detecting tactile sensors: (a) Readout power consumption (estimated based on available datasheets) versus the raw throughput, (b) shear sensing spatial resolution comparison.

![](images/0221df830ccde968789526157aa7dc873bef0babc5c501b9422bf6375c69e613.jpg)

![](images/d789ad57c6d3c01451109baa6f1e22704153dfe2cb821acf3dc5d9095e1ee009.jpg)  
Fig. 23: The modeled SNDR across the input frequency with random AER stalls closely resembles that of the measured SNDR.

available pseudo-CMOS cells is prioritized over the static power consumption advantage of differential logic cells. The power consumption due to the AER, however, scales only by approximately $l o g _ { 2 } ( M )$ where M is the number of taxels.

This work demonstrates a scalable strategy for realizing electronic skins that emulate the high-resolution, energyefficient tactile sensing of human skin. Although implemented here using thin-film technology, the relative simplicity of the front-end and readout circuitry bodes well for portability and adaptation to other, more exotic, large-area flexible sub-

strates [13]. The minimalist sensor architecture also enables integrated, high-spatial-resolution shear sensing. The device comprises only a polymer (PDMS) and a metal layer, both of which can be deposited and processed in standard clean-room environments. Consequently, future designs could integrate the sensor during the thin-film transistor (TFT) fabrication step, yielding well-controlled, high-volume, fully integrated tactilesensor systems.

# VII. CONCLUSIONS

This paper has presented a pathway toward realizing a low-latency, high-resolution tactile slip sensor system through a fully-integrated end-to-end design in a large-area flexible thin-film technology. Experimental results of this DERMIS prototype have shown state-of-the-art performance in terms of force resolution, readout area, and power consumption, while integrating biologically-inspired grasp-state-based force sensing and data compression. Leveraging the intrinsic shear- and normal-force detection capabilities of the tactile sensors, the readout system reconfigures based on the current grasp state, achieving the same grasp-state-adaptive force measurements performed in the human somatosensory system. The design brings e-skins closer to human tactile capabilities.

# ACKNOWLEDGMENTS

This work has received funding from the KU Leuven C3 Project DERMIS and the European Union’s Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No 861166 (INTUITIVE). The authors would like to thank M. Dandekar, Y. Nowicki, Sara Farfalha, and Jonas Pelgrims of KU Leuven, and H. Jorntell of ¨ Lund University for their support throughout this work.

# REFERENCES

[1] R. Johansson and J. Flanagan, “Coding and use of tactile signals from the fingertips in object manipulation tasks,” Nature reviews. Neuroscience, vol. 10, pp. 345–59, 05 2009.   
[2] R. Romeo and L. Zollo, “Methods and sensors for slip detection in robotics: A survey,” IEEE Access, vol. PP, pp. 1–1, 04 2020.   
[3] Z. Su, K. Hausman, Y. Chebotar, A. Molchanov, G. E. Loeb, G. S. Sukhatme, and S. Schaal, “Force estimation and slip detection/classification for grip control using a biomimetic tactile sensor,” in 2015 IEEE-RAS 15th International Conference on Humanoid Robots (Humanoids), 2015, pp. 297–303.   
[4] R. A. Romeo, C. M. Oddo, M. C. Carrozza, E. Guglielmelli, and L. Zollo, “Slippage detection with piezoresistive tactile sensors,” Sensors, vol. 17, no. 8, 2017.   
[5] R. Fernandez, I. Payo, A. S. Vazquez, and J. Becedas, “Micro-vibrationbased slip detection in tactile force sensors,” Sensors, vol. 14, no. 1, pp. 709–730, 2014.   
[6] Y. Cheng, C. Su, Y. Jia, and N. Xi, “Data correlation approach for slippage detection in robotic manipulations using tactile sensor array,” in 2015 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2015, pp. 2717–2722.   
[7] M. Tremblay and M. Cutkosky, “Estimating friction using incipient slip sensing during a manipulation task,” in [1993] Proceedings IEEE International Conference on Robotics and Automation, 1993, pp. 429– 434 vol.1.   
[8] H. A. Khamis, S. J. Redmond, V. G. Macefield, and I. Birznieks, “Tactile afferents encode grip safety before slip for different frictions,” in 2014 36th Annual International Conference of the IEEE Engineering in Medicine and Biology Society, 2014, pp. 4123–4126.

[9] M. D. Alea, M. A. Rosa, S. Farfalha, K. Myny, and G. Gielen, “Dermis: Toward a fully-integrated large-area high-resolution tactile slip sensing solution,” in 2025 IEEE International Symposium on Circuits and Systems (ISCAS), 2025, pp. 1–5.   
[10] M. D. Alea, M. A. Rosa, Y. Nowicki, M. Dandekar, K. Myny, and G. Gielen, “Dermis: A flexible fully-integrated 600µm-resolution pertaxel slip-to-spikes tactile sensor readout on a-igzo tft for large-area high-density electronic skins,” in 2025 Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits), 2025, pp. 1–3.   
[11] J. Van Assche, M. F. Carlino, M. D. Alea, S. Massaioli, and G. Gielen, “From sensor to inference: end-to-end chip design for wearable and implantable biomedical applications,” in 2023 IEEE Biomedical Circuits and Systems Conference (BioCAS), 2023, pp. 1–5.   
[12] M. D. Alea, A. Safa, F. Giacomozzi, A. Adami, I. R. Temel, M. A. Rosa, L. Lorenzelli, and G. Gielen, “A fingertip-mimicking 12×16 200 µmresolution e-skin taxel readout chip with per-taxel spiking readout and embedded receptive field processing,” IEEE Transactions on Biomedical Circuits and Systems, vol. 18, no. 6, pp. 1308–1320, 2024.   
[13] Y. Kim, A. Chortos, W. Xu, Y. Liu, J. Oh, D. Son, J. Kang, A. Foudeh, C. Zhu, Y. Lee, S. Niu, J. Liu, R. Pfattner, Z. Bao, and T. Lee, “A bioinspired flexible organic artificial afferent nerve,” Science, vol. 360, no. 6392, pp. 998–1003, Jun. 2018.   
[14] M. Zulqarnain and E. Cantatore, “Analog and mixed signal circuit design techniques in flexible unipolar a-igzo tft technology: Challenges and recent trends,” IEEE Open Journal of Circuits and Systems, vol. 2, pp. 743–756, 2021.   
[15] L. E. Aygun, P. Kumar, Z. Zheng, T.-S. Chen, S. Wagner, J. C. Sturm, and N. Verma, “17.3 hybrid system for efficient lae-cmos interfacing in large-scale tactile-sensing skins via tft-based compressed sensing,” in 2019 IEEE International Solid-State Circuits Conference - (ISSCC), 2019, pp. 280–282.   
[16] M. D. Alea, A. Safa, J. V. Assche, and G. G. E. Gielen, “Power-efficient and accurate texture sensing using spiking readouts for high-density e-skins,” in 2022 IEEE Biomedical Circuits and Systems Conference (BioCAS), 2022, pp. 359–363.   
[17] Y. Chen, T. Cai, Y. Kuang, J. Dong, Z. Cheng, B. Zhao, and Y. Luo, “A fully dynamic event-driven capacitive sensor interface circuits based on self-reconfigurable sar capacitance-to-digital conversion for high-density robotic tactile sensing,” IEEE Journal of Solid-State Circuits, vol. 59, no. 8, pp. 2618–2629, 2024.   
[18] O. Leslie, D. Cordova Bulens, and S. J. Redmond, “Design, fabrication, ´ and characterization of a novel optical six-axis distributed force and displacement tactile sensor for dexterous robotic manipulation,” Sensors, vol. 23, no. 24, 2023.   
[19] M. B. A. Rosa and M. Kraft, “Microengineered flexible pressure sensors with sacrificial molding layer: A novel fabrication approach for improved performance,” Proceedings, vol. 97, no. 1, 2024.   
[20] J.-E. Park, J. Park, Y.-H. Hwang, J. Oh, and D.-K. Jeong, “A noiseimmunity-enhanced analog front-end for 36 × 64 touch-screen controllers with 20- Vpp noise tolerance at 100 khz,” IEEE Journal of Solid-State Circuits, vol. 54, no. 5, pp. 1497–1510, 2019.   
[21] J. Van Assche and G. Gielen, “Analysis and design of a 10.4-enob 0.92–5.38-w event-driven level-crossing adc with adaptive clocking for time-sparse edge applications,” IEEE Journal of Solid-State Circuits, vol. 59, no. 9, pp. 2858–2869, 2024.   
[22] K. Boahen, “Point-to-point connectivity between neuromorphic chips using address events,” IEEE Transactions on Circuits and Systems II: Analog and Digital Signal Processing, vol. 47, no. 5, pp. 416–434, 2000.   
[23] H. C¸ eliker, F. De Roose, M. Willegems, S. Smout, W. Dehaene, and K. Myny, “Analysis and comparison of logic architectures for digital circuits in a-igzo thin-film transistor technologies,” IEEE Journal of Solid-State Circuits, vol. 59, no. 6, pp. 1858–1870, 2024.   
[24] M. Dandekar, K. Myny, and W. Dehaene, “Positive-feedback-based design technique for inherently stable active load toward high-gain amplifiers with unipolar a-igzo tft devices,” IEEE Solid-State Circuits Letters, vol. 5, pp. 37–40, 2022.   
[25] T. Rooijers, J. H. Huijsing, and K. A. A. Makinwa, “An auto-zerostabilized voltage buffer with a quiet chopping scheme and constant sub-pa input current,” IEEE Journal of Solid-State Circuits, vol. 57, no. 8, pp. 2438–2448, 2022.   
[26] Y. Tsividis, “Event-driven data acquisition and continuous-time digital signal processing,” in IEEE Custom Integrated Circuits Conference 2010, 2010, pp. 1–8.   
[27] L. Bai, B. Lehnert, J. Liu, N. Neubarth, T. Dickendesher, P. Nwe, C. Cassidy, C. Woodbury, and D. Ginty, “Genetic identification of an expansive mechanoreceptor sensitive to skin stroking,” Cell, vol. 163, 12 2015.

[28] T. Moy, L. Huang, W. Rieutort-Louis, S. Wagner, J. C. Sturm, and N. Verma, “16.4 a flexible eeg acquisition and biomarker extraction system based on thin-film electronics,” in 2016 IEEE International Solid-State Circuits Conference (ISSCC), 2016, pp. 294–295.   
[29] E. Genco, C. Garripoli, J.-L. P. J. v. der Steen, G. H. Gelinck, S. Abdinia, P. Harpe, and E. Cantatore, “An emg interface comprising a flexible aigzo active electrode matrix and a 65-nm cmos ic,” IEEE Journal of Solid-State Circuits, vol. 58, no. 11, pp. 3138–3149, 2023.   
[30] C. Garripoli, J.-L. P. J. van der Steen, E. Smits, G. H. Gelinck, A. H. M. Van Roermund, and E. Cantatore, “15.3 an a-igzo asynchronous deltasigma modulator on foil achieving up to 43db snr and 40db sndr in 300hz bandwidth,” in 2017 IEEE International Solid-State Circuits Conference (ISSCC), 2017, pp. 260–261.   
[31] M. Dandekar and K. Myny, “An n-type-only a-igzo thin-film-transistor based nyquist-rate 8-bit cdac+sar adc consuming 1.7mw at 32ksps and achieving 44db sndr,” in 2025 Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits), 2025, pp. 1–3.   
[32] H. Hao, A. G. Richardson, Y. Ding, L. Du, M. G. Allen, J. V. d. Spiegel, and F. Aflatouni, “17.10 a 0.4v, 750nw, individually accessible wireless capacitive sensor interface ic for a tactile sensing network,” in 2024 IEEE International Solid-State Circuits Conference (ISSCC), vol. 67, 2024, pp. 332–334.   
[33] M. Timmermans, K. van Oosterhout, M. Fattori, P. Harpe, Y.-H. Liu, and E. Cantatore, “A 1.8–65 fj/conv.-step 64-db sndr continuous- time level crossing adc exploiting dynamic self-biasing comparators,” IEEE Journal of Solid-State Circuits, vol. 59, no. 4, pp. 1194–1203, 2024.

![](images/477bf38b0ad00510abab562662fe082885c9eca340141c7d26c063c0bc4b533c.jpg)

Kris Myny (Senior Member, IEEE) received the Ph.D. degree in electrical engineering from KU Leuven, Leuven, Belgium, in 2013. He is currently an Associate Professor with the Emerging Technologies, Systems Security Group, COSIC, Electrical Engineering Department (ESAT), KU Leuven. He is a Scientist with imec, Leuven, for topics related to thin-film electronics. His work has been published in numerous international journals and conferences, including Nature Electronics and several ISSCC contributions. Dr. Myny is a member of the Young

Academy of Belgium from 2019 to 2024. He was listed as one of Belgium’s top tech pioneers by the business newspaper De Tijd. He received European Young Researcher Award for design on thin-film electronics in 2018. He also received the prestigious ERC Starting Grant from European Commission in 2016 to enable breakthrough research in thin-film transistor circuits. He also serves as the Track Chair for the IEEE FLEPs Conference and acts in the Editorial Board of the new IEEE Journal on Flexible Electronics.

![](images/cb1b759f8f38eadc8086c1e35a652f5d131c645b6bb644d503ed93be3865dc7d.jpg)

Georges Gielen (Fellow, IEEE) received the M.Sc. and Ph.D. degrees in electrical engineering from Katholieke Universiteit Leuven (KU Leuven), Leuven, Belgium, in 1986 and 1990, respectively. After a Postdoc at UC Berkeley, since 1991 he has been with the MICAS research group at the Department of Electrical Engineering (ESAT), KU Leuven, where he is currently a Full Professor. His current research interests include the design of analog and mixedsignal integrated circuits, such as sensor interfaces and data converters, as well as analog and mixed-

signal CAD tools and design automation.

![](images/0203cf2eddc380de8b24a2d9998a9b03402f9b50145683b26ec6b21f8d3e0dc3.jpg)

Mark Daniel Alea (Graduate Student Member, IEEE) obtained his B.S. in computer engineering and M.S. in electrical engineering from the University of the Philippines Diliman in 2014 and 2019, respectively. Currently pursuing a Ph.D. at the MICAS Group of KU Leuven in Belgium, he focuses on developing neuromorphic high-density tactile sensor readout chips with integrated sensors for electronic skins. Prior to joining KU Leuven, he was an Analog IC Design Engineer at Analog Devices Philippines until 2020, and was a Science Research Specialist

on the SmartWire Chip project under the Philippine Department of Science and Technology (DOST). His research interests include event-driven sensor interfaces, as well as neuromorphic circuits.

![](images/6e706a221d1e22eb39c41af35ea167085189f8474d4b4590ab1831340031b789.jpg)

Maria Atalaia Rosa received the B.Sc. and M.Sc. degrees in Micro and Nanotechnology Engineering from NOVA School of Science and Technology in 2018 and 2020, respectively. Since 2020, she has been working as a Research Assistant in the MNS group under the guidance of Prof. Michael Kraft in order to receive the Ph.D. degree in Electrical Engineering. Her work focuses on the fabrication and functionalization of microstructured flexible sensors.

![](images/d88680bdc242e951ba8b71b0bcec58ed57695cacd1939c7a51dc1ef2cf63d838.jpg)

Michael Kraft (Member, IEEE) joined KU Leuven-MICAS Group, Leuven, Belgium, as a Full Professor of microsystems and nanosystems, in October 2017. He brings along 20 years of experience in the design, fabrication, and characterization of a wide range of microsystems and nanosystems, and MEMS sensors and devices. He has worked on inertial sensors, intelligent interface circuits and control systems for microdevices, atom and ion chips, and biomedical and biochemical sensors and devices. These topics will also form the framework of his future research,

with a strong focus on biomedical sensors and systems. He has taken over the lead of the clean room and MEMS activities in Leuven Nanocentre from Prof. Puers.