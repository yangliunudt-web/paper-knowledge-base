---
title: "Reservoir Computing System with Diverse Input Patterns in HfAlO-Based Ferroelectric Memristor"
authors:
  - "Dongyeol Ju"
  - "Minseo Noh"
  - "Gimun Kim"
  - "Yongjin Park"
  - "Sejoon Lee"
  - "Sungjun Kim"
date: "2024-11-19"
year: "2024"
journal: "ACS Applied Materials & Interfaces"
doi: "10.1021/acsami.4c11513"
abstract: "Ferroelectric memristors, particularly those based on hafnia, are gaining"
abstract_cn: "铁电忆阻器，特别是基于铪的那些，作为神经形态计算的潜在候选者正受到关注。这些器件由于结构简单、与 CMOS 技术兼容以及低功耗特性，相比钙钛矿基铁电忆阻器具有优势。本研究实现了利用基于"
keywords:
  - "[[reservoir computing]]"
  - "[[artificial synapse]]"
  - "[[memristor]]"
  - "[[ferroelectric memories]]"
  - "[[$H f O _ { 2 }$]]"
cite: "[1] Ju D, Noh M, Kim G, et al. Reservoir computing system with diverse input"
aiSum: "实现基于 Al 掺杂 HfO 铁电忆阻器的储备池计算系统，演示可处理多种输入脉冲类型的鲁棒储备池层，模拟生物突触短期可塑性，验证图像训练和巴甫洛夫实验等应用。"
confidence: "high"
wiki_concepts:
  - "[[Memristor]]"
  - "[[Reservoir computing]]"
---

www.acsami.org

Research Article

# Reservoir Computing System with Diverse Input Patterns in HfAlO-Based Ferroelectric Memristor

Dongyeol Ju,§ Minseo Noh,§ Gimun Kim,§ Yongjin Park, Sejoon Lee,* and Sungjun Kim*

![](images/18d33f599f07522c321158ca527da32bedcf975da6bdfa871699502a7bc0c217.jpg)

Cite This: ACS Appl. Mater. Interfaces 2024, 16, 66250−66261

![](images/f74b1feb263bf60e3adb9bbcaa78b59d5d74b6c402af5ff4dbe62dd592e50a48.jpg)

Read Online

ACCESS

![](images/e9121e5fe9b73f1c7b7a9259d076d3b15619f452d8736b4a8b5ddd046e056a88.jpg)

Metrics & More

![](images/e90f956e3137704858ddb2b71e929bbe32ff17e2fc9061a6fe6670db542ddfc9.jpg)

Article Recommendations

![](images/68ff5ba451196baaf362a4e20dec73af38a22e20fc3e44f062c037a070376c2d.jpg)

Supporting Information

ABSTRACT: Ferroelectric memristors, particularly those based on hafnia, are gaining attention as potential candidates for neuromorphic computing. These devices offer advantages over perovskite-based ferroelectric memristors owing to their simpler structures, compatibility with complementary metal-oxide semiconductor technology, and low-power consumption characteristics. Additionally, improvements in ferroelectric memristor’s performance, such as enhancing tunneling electro resistance (TER) and polarization retention, can be achieved using methods like aluminum doping and insulating film deposition. In this study, we implement a physical reservoir computing (RC) system utilizing the metal-ferroelectric-insulator−semiconductor-structured ferroelectric memristor based on Al-doped HfO as an artificial synapse. Specifically, we ensure the universality and diversity of the

system by experimentally demonstrating a robust reservoir layer capable of handling various types of input pulses. To utilize the ferroelectric memristor in the reservoir layer of the RC system, we employ partial polarization switching of ferroelectric materials. We measure the retention loss characteristics of the device for pulse amplitude, interval, and width, and quantify the time constant values by fitting them to a stretched exponential function. Additionally, we validate the suitability of the fabricated device as an artificial synapse by mimicking various short-term plasticity functions of biological synapses. Furthermore, we experimentally demonstrate various applications related to learning and memory of the brain, such as image training and Pavlov’s experiment, utilizing the shortterm memory characteristics of the fabricated device. Lastly, we evaluate the robustness of the RC system under various input conditions by employing the fabricated device as a reservoir layer.

KEYWORDS: reservoir computing, artificial synapse, memristor, ferroelectric memories, $H f O _ { 2 }$

![](images/690247f5735e8ab598ff74f5b42e3aca3fbc68e61223636a3e77eed2996f60ba.jpg)  
Image memorization

![](images/9364047f7002e3a9ea8102d3c047689ae194e97be2b368e637747530049f851d.jpg)

![](images/f48adcf175484ee7af3717a999580a01df044b6db5d4a45b9945f2aa1178f09d.jpg)

# INTRODUCTION

Currently, there is considerable emphasis on computing systems for energy-efficient data processing, aiming to surpass the limitations of existing technologies. 3 The elaborate structure of the human brain includes interconnected neurons and synapses that transmit and receive action potentials. The abundance of neurons and synapses enables our brain to perform parallel data processing efficiently at high speeds.4,5 The action potential generated in this process induces changes in synaptic weight, a phenomenon known as synaptic plasticity.6 This plasticity regulates the formation of memories, categorizing it into two types based on the time required for observing synaptic plasticity facilitation.7 Short-term memory (STM), characterized by its volatile nature, undergoes rapid degradation of synaptic plasticity within milliseconds. In contrast, long-term memory (LTM) arises from nonvolatile synaptic plasticity that persists for extended periods, ranging from hours to days.7,8 By replicating these synaptic and neural functions using electronic devices, neuromorphic computing can be effectively implemented.

Ferroelectric memristors have gained prominence as promising candidates for emulating synapse functions owing to their straightforward metal-ferroelectric-semiconductor structure, compatibility with complementary metal-oxide semiconductor technology, nondestructive reading processes, and low power consumption.9−13 While previous studies highlighted perovskite materials such as $\mathrm { P b T i O } _ { 3 } , \mathrm { B a T i O } _ { 3 } ,$ and $\mathrm { S r B i } _ { 2 } \mathrm { \bar { T a } } _ { 2 } \mathrm { O } _ { 9 }$ in the ferroelectric layer, their incompatibility with modern very-large-scale integration technology and scaling issues have prompted the exploration of new hafnium oxidebased ferroelectric layers.16−2 1 Recent research suggests that enhancing the electrical properties of the ferroelectric layer is achievable through doping and additional insulating film deposition, leading to the integration of the metal-ferro-

Received: September 2, 2024

Revised: November 7, 2024

Accepted: November 13, 2024

Published: November 19, 2024

![](images/51370d5f7a976668f9831a87935a69888b43d50076c806cd78ce7d9c617e7b49.jpg)

electric-insulator−semiconductor (MFIS) structure.22−24 Doping with elements like Zr, Y, Si, and (especially) Al has proven effective in inducing ferroelectric phase transitions.25−30 Al doping induces spontaneous mechanical stress during cooling, thus resulting in the orthorhombic (o-phase) formation, thereby reducing the switching voltage, and increasing the polarization.31−33 Furthermore, ferroelectric devices based on an Al-doped HfO2 (HAO) offer advantages, such as a high on/ off ratio, low-energy consumption, rapid operation, long-term stability, and suitability as memory devices.34,35 Enhancing ferroelectric memristor properties is also achievable by employing the MFIS structure, involving the deposition of an additional insulating layer between the ferroelectric layer and the semiconductor. Applying a bias across the ferroelectric layer alters its polarization direction, influencing the electron tunneling probability through the material. The magnitude and direction of the applied voltage determine the degree of polarization reversal that affects the electron tunneling current. Compared with the metal-ferroelectric-semiconductor (MFS) structure, the MFIS structure�with additional insulating films like $\mathrm { H f O } _ { 2 } , \mathrm { Z r O } _ { 2 } , \mathrm { S i O } _ { 2 } ,$ and $\mathrm { { A l } } _ { 2 } \mathrm { { O } } _ { 3 } \mathrm { { - } }$ �offers a reduced leakage current and an improved TER ratio, thus enabling multiple conductance states conducive to achieving synaptic features.36,37 Therefore, doping Al into the ferroelectric film and applying insulating films enhance device performance, thus facilitating a closer mimicry of synapse functions.14,15,79

Neuromorphic computing is a technology that enables parallel, energy-efficient computation and autonomous learning. Designing innovative devices that emulate the core functions of synapses is crucial for implementing neuromorphic computing in hardware.38

The core of neuromorphic computing lies in the precise replication of the complex signal-processing processes and learning models between synapses and neurons observed in the biological brain. For example, in human brains, the smooth transition between STM and LTM relies on a process known as “rehearsal”.7 Without rehearsal, synaptic plasticity facilitation occurs, thus causing LTM to shift gradually to STM. Conversely, the repeated rehearsal enhances synaptic plasticity, transforming STM into LTM. This neural behavior can be mimicked in synaptic devices by regulating the intensity of electrical pulse stimuli. Intense electrical stress leads to a gradual decline in the excitatory postsynaptic current (EPSC), representing LTM, while weaker stress causes a rapid EPSC decrease, indicative of STM.39− 41 Recently, numerous research findings have been published regarding the utility of various synaptic devices exhibiting STM characteristics.42−45 Particularly noteworthy is the significant importance of incorporating memristor devices with STM characteristics in the implementation of artificial neural networks (ANN). Prior investigations underscored the significance of deploying volatile memory devices in reservoir computing (RC) to tackle cost and efficiency issues encountered in recurrent neural networks.46 49 RC consists of three sequential layers�input, hidden, and output�where time-dependent input signals undergo high-dimensional mapping within the reservoir layer. This process enables the system to handle adeptly complex tasks such as time-series analysis, speech recognition, and pattern generation. 48,50 Two aspects essential for the implementation of volatile devices in RC are the volatile memory property and nonlinearity.51−53 The output from the readout layer should exclusively depend on current data within the reservoir layer, necessitating gradual information facili-

tation. Furthermore, the high-dimensional mapping within the reservoir layer must be nonlinear to induce the necessary complexity required for addressing diverse problems. Reservoir computing leverages the dynamic reservoir of neurons to capture temporal dependencies and transform temporal inputs into a high-dimensional space, enabling efficient temporal data processing with low training costs. Physical reservoir computing inspired by the brain, utilizing neuromorphic devices, exhibits rich nonlinearity, further enhancing the efficiency of temporal signal processing.50

In this study, we utilize the MFIS-structured ferroelectric memristor based on HAO as an artificial synapse to implement a physical RC system. Specifically, we ensure the universality and versatility of the system by implementing a resilient reservoir layer capable of handling various types of input pulses, thus paving the way for improved energy efficiency in future hardware implementations. First, we evaluate the ferroelectricity and fundamental electrical properties of the fabricated device, thus ensuring stable operation. By leveraging the current facilitation functionalities of the MFIS device based on depolarization effect, we induce the STM characteristics of the memristor. We measure the retention loss tendencies of the device under various input pulse conditions (amplitude, interval, width) and quantify the time constant values by fitting them to the stretched exponential model. Furthermore, we demonstrate the suitability of the fabricated artificial synapse by mimicking the short-term potentiation (STP) functions of biological synapses, such as potentiation/depression, pairedpulse facilitation (PPF), post-tetanic potentiation (PTP), and spike-rate dependent plasticity (SRDP). Additionally, we experimentally demonstrate various applications related to learning and memory of the brain, such as image training and Pavlov’s experiment, by utilizing the STM characteristics of the fabricated device. Lastly, we evaluate the robustness of the RC system under various input conditions by utilizing the fabricated device as a reservoir layer.

# EXPERIMENTAL PROCEDURE

The MFIS-structured TiN/HAO/ZrO /n+ -Si device was fabricated based on the following process. Initially, the heavily doped $\mathrm { n ^ { + } { - } S i }$ substrate underwent a cleaning process using a concentrated sulfuric acid $\left( \mathrm { H } _ { 2 } S \mathrm { O } _ { 4 } \right)$ and hydrogen peroxide $\left( \mathrm { H } _ { 2 } \mathrm { O } _ { 2 } \right)$ mixture (known as the sulfuric acid-peroxide mixture) to eliminate significant organic contaminants from the wafer’s surface. Subsequently, the native oxide layer and any metallic impurities on the cleaned $\mathrm { n ^ { + } { - } S i }$ substrate were removed using a diluted hydrofluoric acid solution consisting of deionized water (100 parts) to hydrofluoric acid (HF) (1 part). On the cleaned n+ -Si substrate, the insulating layer of zirconium dioxide $\left( \mathrm { Z r O } _ { 2 } \right)$ was applied using atomic layer deposition (ALD) at $2 5 0 ~ ^ { \circ } \mathrm { C }$ at a deposition pressure of 0.1 Torr. The process utilized tetrakis-(ethylmethylamido) zirconium(IV) (TEMAZr) as the precursor and $_ { \mathrm { H } _ { 2 } \mathrm { O } }$ as the oxidant for the deposition process. The HAO ferroelectric layer was subsequently deposited onto the $\mathrm { Z r O } _ { 2 }$ insulating layer using thermal ALD (CN1 atomic premium) at a stage temperature of 350 $^ \circ \mathbf { C } .$ . For the HfO2 and ${ \mathrm { A l } } _ { 2 } { \mathrm { O } } _ { 3 }$ precursors, tetrakis(ethylmethylamino) hafnium (TEMAHf) and trimethyl aluminum (TMA) were utilized. Ozone $\left( \mathbf { O } _ { 3 } \right)$ served as the oxidant for all the dielectric layers deposited via ALD. The Hf and Al were combined in a process with a cycle ratio of 25:1 (Al 3%). By repeating this sequence, the HAO ferroelectric film was fabricated. Subsequently, the top electrode TiN was deposited by direct current (DC) sputtering (Endura 5500, AMAT) at a stage temperature of 200 °C by utilizing a Ti target (99.99% purity). The gases of Ar and $\Nu _ { 2 }$ were used with a DC voltage power of 5 kW applied to the target in the main chamber at a pressure of 3 mtorr. Subsequently, a rapid thermal annealing (RTA, KVT-

![](images/ccf32a299646e737dfa1669c59cf8d3f9c5b44ebfc17ec8f6cd0dd9b10cdb5ed.jpg)  
  
(b)

![](images/42546825aa8b0b2b8ebee647841c2018f39d8b7bfa8d312f4f606586aa7056b0.jpg)

![](images/f8b3885016ff1e688eaa41efd1d35eab6ab4c63a44a1d768e9613cfe87494012.jpg)  
(c)

![](images/93e485cfb217a73bf5412b8726e57efe190abc719e669b11d12795b6f86365e0.jpg)  
(d)

![](images/0040c3578c8b3e474b299a72db91716df6ce0ae13eee2764aee6150e3d1702da.jpg)  
(e)

![](images/19e90e4d789da466f11e8d94034d840fff642989e1e2d735f0d19afc4cd60dd6.jpg)  
Figure 1. (a)Schematic of the $\mathrm { T i N / H A O / Z r O _ { 2 } / n ^ { + } { - } S i }$ MFIS device. (b) Cross-sectional TEM image and $( \mathrm { c } )$ EDS color mapping of the fabricated device. (d) EDS line scan analysis. (e) GIXRD patterns of the HAO film after phase transition annealing.

![](images/6d86cd5125f609f46aa6b2aa9061e3202f316b7f6e05b4c892323eab46252bff.jpg)

![](images/83a5b84c8dfc82ec5166b54d119f1c97448ac60c76f30682f3bea1cac5537461.jpg)

![](images/ac227c519386a3912dd20083735b5e14a1c17d4bd125b1eccb89b69815b0c7bc.jpg)

![](images/7e37cbf9024ad89bcc00ae3703c779edef18a5ec1e1166a940720fbde9acd87a.jpg)  
Figure 2. (a) I−V history curve with a rectifying ratio of >132. (b) P−V curves after $1 0 ^ { 2 }$ wake-up cycles. (b) Polarization endurance test at various pulse amplitudes (from 4 to 6.5 V). (c) Multilevel cell operation through set voltage variation. (d) On/off ratio at a read voltage of 1.5 V depending on sweep voltage range. (e) Increasing on/off ratio depending on the sweep voltage range.

3006T) process was applied to the fabricated device in a vacuum atmosphere for $2 0 \mathrm { ~ \ s ~ \ ~ a t ~ \ } 8 0 0 \mathrm { ~ \ } ^ { \circ } \mathrm { C } .$ Temperature changes caused expansion or contraction, creating tensile stress in the HAO layer due to the distinct thermal expansion coefficients of TiN, $\mathrm { H A O } , \mathrm { Z r O } _ { 2 } ,$ and Si. Finally, using a mask with a pattern diameter of $1 0 0 \ \mu \mathrm { m } ,$ , the top electrode was patterned and etched. Electrical assessments involved the application of DC bias and pulses to the top electrode (TiN) while keeping the bottom electrode $\left( \mathrm { n } ^ { + }  – \mathrm { S i } \right)$ grounded; these evaluations were achieved by using a semiconductor parameter analyzer (Keithley 4200-SCS) and the pulse measurement module (Keithley 4225-PMU). Furthermore, the structure of the manufactured MFIS device was examined using a cross-sectional transmission electron microscopy (TEM) image, thus illustrating the thickness of individual layers with an energy-dispersive spectrometer (EDS) confirming the presence of each element within the fabricated device.

# RESULTS AND DISCUSSION

Figure 1a illustrates a schematic of the $\mathrm { T i N / H A O / Z r O _ { 2 } / n ^ { + } { - } S i }$ MFIS device. The cross-sectional TEM image of the fabricated device is depicted in Figure 1b, showing each layer of TiN, ${ \mathrm { H A O } } ,$ and $\mathrm { Z r O } _ { 2 }$ on the $\mathrm { n ^ { + } { . } S i }$ bottom electrode. The TiN top electrode has a thickness of 80 nm, while the ferroelectric layer measures 9 nm, and the insulating layer is only 1 nm thick. In Figure $^ { 1 \mathrm { c } , \mathrm { d } , }$ an EDS color map and the elemental weight distribution derived from EDS line scan measurements illustrates the presence of Ti, $\mathrm { N } ,$ Hf, $\mathbf { A l } , \mathbf { Z r } ,$ and O elements within the MFIS device. Grazing-angle incidence X-ray diffraction (GIXRD) was used to examine the diffraction patterns of a ferroelectric film (Figure 1e). Various crystalline

![](images/320639ede2256f9c600e696d7c977dbbb0ee51a171f7a54bd1d6dab7ff1f7d8d.jpg)

![](images/88545f9ebd9b77bf61d649bd55f19f53d83e423dede091a9420656dd13fbedae.jpg)

![](images/707335567bc36a434af0851a7e7c7be2e1a9a667d2cdf373ddd9a3c642487afa.jpg)

![](images/9ff226643f90feca9741ee52d9c092ff2de899d5a9409898d18550a9e2acef39.jpg)

![](images/a9452e01d829a427d08afde3c7d7c317242e57e934810f7e50ae3be220e0670f.jpg)  
Figure 3. (a) EPSC gain measured at various pulse widths. (b) Potentiation/depression characteristics measured using the pulse scheme in the inset. (c) Decay characteristics of the device according to the control variables of the input pulse (number, interval, width). (d) Fitted results of the currents over time to the stretched exponential model. (e) Schematic illustration of the duration for each sensory, short, and long-term memory.

phases of the ferroelectric films were explored; these revealed peaks corresponding to the m (−111), o (111)/t (011), m (111), and o (200) phases of MFIS. Specifically, the presence of the orthorhombic phase (o-phase) was identified (peak of 30.7°), thus indicating the robust maintenance of ferroelectricity in the HAO layer.54

Figure 2 illustrates the ferroelectric characteristics of the MFIS device. Figure 2a depicts the I−V curve of the fabricated MFIS device, demonstrating typical behavior measured in dual-sweep mode across a voltage range of −3.8−5.2 V. The excellent uniformity of the fabricated devices can be observed from the I−V curves of randomly selected cells in Figure S1a in the Supporting Information. As shown in Figure S1b in the Supporting Information, the average on/off ratio across the 10 cells is approximately 4.7. At a bias of 5.2 V, the device transitions from a high-resistance state (HRS) to a lowresistance state (LRS), exhibiting a high-rectification ratio of 132, which is advantageous for array architectures. Figure 2b presents the P−V curve obtained using the positive-up negative-down (PUND) method. With a pulse amplitude of 6.5 V applied at 5 kHz, a remnant polarization (P ) of 20.59 $\mu \mathrm { C } / \mathrm { c m } ^ { 2 }$ was observed. To assess the reliability of the MFIS device, an endurance test was conducted at various voltages (from 4 to 6.5 V) in incremental steps of 0.5 V. The $\mathrm { P _ { r } }$ endurance was determined using the PUND method at a frequency of 5 kHz, as illustrated in Figure 2c. The results exhibit three distinct stages: wake-up, stability, and fatigue, observed during continuous cycling. In the wake-up stage, the crystalline phase in the bulk region shifts to the o-phase owing to oxygen vacancy redistribution, thus leading to an increase in $\mathrm { P _ { r } }$ with more pulse cycles. The stabilization stage shows saturation of the $\mathrm { P _ { r } }$ value. In contrast, the fatigue stage r indicates a decrease in $\mathrm { P _ { r } } { } ^ { 5 5 - 5 9 }$ Potential causes of fatigue include charge trapping, dipole fixing of oxygen vacancies and ions, and an increase in the bulk defect density, thus resulting in a higher leakage current.59,60 At the voltage values of 4 and 4.5 V, fatigue occurred after $1 0 ^ { 6 }$ cycles. At 5.5, $^ { 6 , }$ and 6.5 ${ \mathrm { V } } ,$ larger P values were obtained, but breakdown occurred at $1 0 ^ { 4 }$ cycles. At a 5 V bias, the breakdown occurred at cycle numbers ${ < } 1 0 ^ { 5 }$ . Figure 2d displays the multilevel cell properties, showcasing eight distinguishable LRS states achieved by incrementing the set voltage (from 4.8 to 5.5 at 0.1 V intervals). Figure 2e displays the $I _ { \mathrm { o n } } / I _ { \mathrm { o f f } }$ ratio at a read voltage

of 1.5 V and shows that the ratio increases exponentially as the sweep voltage range increases. This means increased electron tunneling probability owing to stronger bias. Based on the measured results and established theory of the ferroelectric memristor,59,60 the conduction mechanism of the MFIS device is depicted in Figures S1c and d in the Supporting Information (details on conduction mechanisms based on resistance states and bias regions).

Neuromorphic computing utilizes the plasticity of synapses in the neural network of the human brain for learning and information processing.61 Each synapse is composed of a narrow gap between pre neurons and post neurons, known as the synaptic cleft (Figure 3a).62 Synapses are crucial components for functional connections between neurons, where the conductivity (synaptic weight) of the synapse is controlled based on the concentration of neurotransmitters. Consequently, depending on the incoming spikes toward the synapse change in conductivity is resulted, triggering EPSC.7 This process, known as synaptic plasticity, plays a vital role in information transmission in the human neural network.63 Biological synapses exhibit diverse response characteristics based on the intensity of incoming spikes. The developed MFIS device can mimic these characteristics. Figure 3a shows the observed EPSC (response) as a function of the number of pulses measured, with the pulse width used as a variable. The magnitude of the applied voltage is 5.5 ${ \mathrm { V } } ,$ while the read voltage is 4 V. Here, the 5.5 V set pulse represents the incoming spike pattern directed toward the synapse, simulating the behavior of a memristor, and triggering a change in conductance. The 4 V pulse is employed as a read pulse to monitor the conductance change of the device, facilitating the realization of an artificial synapse. The EPSC gain in Figure 3a was determined using the following eq 1: 64

$$
\text {EPSC} \quad \text {gain} (\%) = \frac {A _ {\mathrm {n}}}{A _ {1}} \times 100 \tag{1}
$$

where $A _ { \mathfrak { n } }$ and $A _ { 1 }$ respectively refer to the responses of EPSC after the last and first pulse. Varying the pulse width resulted in various EPSC gains, demonstrating a linear relationship between width and response. Additionally, our MFIS device exhibited a correlation between the number of applied pulses and EPSC gain. These findings highlight the importance of stimulus strength in the MFIS device, enabling the generation

![](images/258f38ea6b28efac5ca7843dbd0d2d810b3c836dc3cc96f87e4f7a6e2f4931c8.jpg)

![](images/4cc245597fa967f9771d12af7997db05f0fa13b88c8d3841eb6eb177bf77332d.jpg)

![](images/06d26a3e4740a3a6ef4af65922b9a2494b5520fa33b206c340fa1814fd75b1ab.jpg)

![](images/2658f43208aa7df5dce45c07885a4a99a0adc80412e1fc25c44c1d77dd032a5a.jpg)

![](images/9134981aea36363b2994fa20c693508d752bba54a29864c683b5c9e4b8f9c73e.jpg)  
Figure 4. (a) Illustration of the biological synapse (top) and partial polarization behavior of the MFIS device according to the shapes of the applied input pulses (bottom). (b) Response characteristics of the device measured after the application of a pair of stimulus pulses with varying pulse intervals. (c) PPF index fitted using the double exponential decay function. (d) Spike-rate dependent plasticity characteristics according to various pulse intervals. (e) Relative current change during the application of 10 pulses for pulse trains with different pulse intervals. The rectangular boxes indicate PPF and post-tetanic potentiation behavior. Herein, ΔI was calculated using the equation $\Delta I = [ ( \dot { I } _ { n } { - } I _ { 0 } ) / I _ { n } ]$ .

of diverse responses that effectively mimic neural network functionality. One of the types of synaptic plasticity, known as long-term potentiation/depression (LTP/LTD), is associated with human brain learning and memory. 63 This synaptic plasticity is associated with lasting changes in synaptic efficacy65 MFIS device, as shown in Figure 3b, we verified the LTP/LTD characteristics by applying 50 consecutive set pulses and reset pulses, following the pulse scheme in the inset of Figure 3b. The LTP/LTD characteristics measured over 100 repetitions are shown in Figure S3a in the Supporting Information; these demonstrate highly uniform characteristics with a maximum coefficient of variation of 1.09%. Our MFIS device imposes significant limitations in neuromorphic applications owing to the abrupt conductance changes observed during the depression, while exhibiting a gradual and relatively linear conductance change (weight update) during potentiation. Particularly, as the artificial synapse device for ANNs such as the multilayer perceptron or convolution neural network that require excellent weight retention characteristics, it appears unsuitable.66,67 However, in RC systems where a highly unique component with STM characteristics is essential, the retentionloss property of these memory devices can be utilized.68 By utilizing the current facilitation functions of the MFIS device and applying short pulses, it becomes feasible to induce STM features. This is evident because the decay of current can be observed under the retention of on-state current in a 4 V bias for 1000 s after the set process of 5.2 V application Figure S2a in the Supporting Informatio n. 69−71 We have induced these STM characteristics by applying various types of input pulses. Figure 3c illustrates the device’s current decay characteristics according to the input pulse’s control variables (number, interval, width). The pulse schemes applied for each

experimental condition are depicted in Figures S3b−d in the Supporting Information. From the measured results, the response characteristics of the device can be divided into STM and LTM based on specific reference currents. For example, when the control variable is the number, the transition to LTM occurs with more than 10 pulse inputs; when the control variable is the interval, the transition occurs with pulse intervals <0.1 ms; and when the control variable is the width, the transition occurs with pulse widths >20 ms. Under the conditions depicted, the frequency of polarization reversal increases notably when encountering stronger pulses. Consequently, during the read process at 4 V, a larger current response is observed compared to weaker incoming pulses. Moreover, due to this increased current response, the process of returning the current toward the device’s original state (3 μA) takes a longer duration. These functionalities mimic the LTM function of the biological brain, where longer periods are required for synaptic plasticity facilitation under significant changes. Conversely, under weak pulse application, an immediate decrease in current is evident, which corresponds to the STM function of the biological brain, where rapid facilitation of synaptic plasticity occurs.7 We adopted the stretched exponential (SE) model to evaluate quantitatively the retention loss characteristics of the device. When describing electrical or structural relaxation in disordered materials like glass, polymers, or dielectrics, the SE model is frequently employed.72−74 Specifically, this model is frequently applied to the modeling of $\mathrm { V _ { T } }$ shifts caused by charge trapping or trap formation in the gate dielectric of semiconductor devices like FETs and TFTs.75,76 Therefore, we consider the SE model suitable for describing the spontaneous retention loss characteristics of our device. The following equation defines the SE model

![](images/9688e501cc819f6480423e90a32f61e69b3e88f79871866e8ee13fc8d6042b3b.jpg)  
(a)   
Image memorization 5×5synapse array

![](images/abd96708cbd840234de227b40a6368e607dc7aa3c6c17aed3b6173277f95875e.jpg)

![](images/6bee38ee7cfb6ba9d0648e66869dc07a635f2cf0f367c794c59c5fde4ebf0413.jpg)

![](images/e739e53206cf96ab0b1b61a7d28f472760b6dfec9236855c78c1a9e7fc132b6b.jpg)

![](images/46ad39cd3577ca3361325dd987f711e098e4ec6160a5e3258becc8b2b0884720.jpg)

![](images/3ef63cb6d508cb2935e6f4dd11ef1d667ec73caebeb92a110b10db07256a6a03.jpg)  
(d)

![](images/2d0c6a20db436ebca22ad20c6c2df466dfd96f242f4f3c38b3b3a7385e07b4dc.jpg)

![](images/3b6170982c3ecd9e05900f0da8e00dca98d00fb903ef2683dbb4487825b3d928.jpg)  
(e

![](images/30378b399ae201b9e186cf4fb737b009ad27d18a599a2e2706eda8a974fb6835.jpg)

![](images/27a6eb26e9e455a1e8f632edac04553fa77384f35712fc61d8358abd97cac03e.jpg)

![](images/be3cc4195dbbea274a49181d21ef2db773b0cef4dd933b923397764ee5c58cfc.jpg)  
Figure 5. (a) Input image used for memorization of the letter $^ { \alpha } { \cal S } ^ { \gamma }$ using ${ \mathrm { ~ a ~ } } 5 \times { \mathrm { ~ 5 ~ } }$ artificial synaptic array. (b) Pulse scheme used for image training experiments. (c) Image mapping of current response according to the pulse number (three and six). (d) Pulse scheme applied to the device for Pavlov’s experiment on classical conditioning. Herein, the input voltage pulses corresponding to 4 V bell (conditioned stimulus (CS)), 5.5 V food (unconditional stimulus (US)), bell + food $\zeta \mathsf { C } S + \mathsf { U } S )$ , and bell (CS) were sequentially applied. (e) Current device responses to the various input pulses. Herein, salivation was the unconditional response (UR), and the learned response to the CS was the conditioned response (CR).

$$
I (t) = I _ {0} \exp [ - (t / \tau) ^ {\beta} ] \tag {2}
$$

where $I _ { 0 }$ is the equilibrium shift of the conductance at $t = + \infty ,$ , τ is the characteristic relaxation time constant, and $\beta$ is the stretched exponent (which takes values between zero and one). Figure 3d illustrates the fitting results for the control variables of pulse number (20), interval (10 μs), and width (20 ms), thus indicating that the current changes closely adhere to the SE model under these three conditions. The extracted time constants from the fitted results of the three control variables are 0.07, 0.23, and 4.6 s. Here, we note the deliberate controllability of the time dependence of these STM characteristics based on the conditions of the input pulses. In other words, they can be controlled on the time scales of 0.01, 0.1, and 1 s. According to the multistore memory model

of the human brain,77 information is detected by the sensing organs and enters the sensory memory, which stores a fleeting impression of sensory stimuli. If this information enters the STM and if the information is assigned to meaning (repeated rehearsal) it is passed on to the LTM. As shown in Figure 3e, the three separate memory stores have their unique durations defined.78 Therefore, securing time constant values of various scales in STM devices has the advantage of being able to implement each memory storage with a single device. Furthermore, when utilizing our device as the reservoir layer of an RC system, it can increase the design flexibility by considering factors such as speed, accuracy, and energy efficiency of the system.

Typically, the implementation of STM using memristors exploits the dynamic characteristics of short-term components. These characteristics denote the ability of the device to return spontaneously to its initial state after the electrical stimulus is removed. Figure 4a illustrates the partial polarization due to the principle of dynamic domain switching in ferroelectric memristors. Small or short electrical fields are not sufficient to flip completely the domains; at this point, reversible domain wall motion predominates.69 Therefore, the nonideal screening resulting from the inability of polarization charges in ferroelectric materials to be completely blocked by the electrodes induces a depolarization field opposing the polarization, ultimately reflected in the finite time scale of polarization retention under certain conditions.69 In Figure S2b in the Supporting Information, the impact of depolarization on the retention characteristics of domain switching is demonstrated. Following the methodology referenced from prior studies, two positive triangular pulses were administered to the memristor with varying time intervals between them to analyze the time-dependent switching current. These intervals were categorized into six conditions: immediately after the first set, after 1 ms, 10, 100 ms, 2 s, and 2 min27 When the interval is brief, such as immediately after the set, no further switching took place as the domain vectors were already aligned. This resulted in an ideal scenario with only nonswitching current being present. However, as the time intervals between pulses increased, the switching current gradually reverted to the initial set state. With time, a significant rise was noticeable as the once-aligned domain polarization vectors became random again, prompting localized switching. This highlights the impact of the depolarization field on the retention loss of our ferroelectric memristor. We have utilized the STM characteristics of these ferroelectric memristors to implement various synaptic functionalities. In particular, by evaluating the PPF phenomenon, wherein the potential response to the second input signal is enhanced compared with the first input signal when delivered within a short time interval, we can explore the short-term facilitation characteristics of synaptic plasticity and the volatile nature of the device. Figure 4b demonstrates the measured response of the device after applying a pair of stimulus pulses with the pulse interval as a variable. The response to the second pulse demonstrated a significant increase compared with that of the first pulse, and the extent of this increase can be adjusted by varying the time interval between the two pulses. Additionally, a decrease in current was observed during the pause between consecutive pulses attributed to the volatile nature of the device. As illustrated in Figure 4c, we varied the time interval (from 100 μs to 100 ms) between the two pulses (5.5 V, 5 ms) to evaluate quantitatively the rate of change in the device’s reaction to PPF. The following equation was used to determine the PPF index80

$$
\text{PPF} \quad \text{index} (\%) = \frac {I _ {2} - I _ {1}}{I _ {1}} \times 100 (\%) \tag{3}
$$

where the terms $I _ { 1 }$ and $I _ { 2 }$ refer to the current response after the second and first pulse application. The measured results were fitted using a double exponential decay equation, and the reliability of the measurements was confirmed by verifying that the R-squared value for the exponential fit was 1, as shown in Figure 4c, where Δt represents the pulse interval time, and $\tau _ { 1 }$ and $\tau _ { 2 }$ represent the characteristic relaxation times of the respective phases, each of them corresponding to a fast and

slow decaying process.81 The fitted values of $\tau _ { 1 }$ and $\tau _ { 2 }$ were extracted to be 5 and 61 ms, respectively; these correspond to the relaxation time scales of biological synapses.82,83 Additionally, we validated the utility of our device as an artificial synapse by emulating the SRDP, a form of the Hebbian learning rule.84 Figure 4d shows the measured results of the device’s current after the application of 10 consecutive set pulses with the pulse interval as a variable. The pulse scheme applied for the experiment is illustrated in Figure S4 in the Supporting Information. From the SRDP experiments, it can be inferred that the connection strength (current level) of the artificial synapse device is modulated by the neuronal activity rate. In other words, the strength of the synapse is determined by the frequency or firing rate of the neuron triggering that synapse. If the neuron fires more frequently, the synaptic strength increases and decreases if the firing is less frequent. This reflects the Hebbian principle that neurons that fire together wire together.85 Moreover, as shown in Figure 4e, in contrast to PPF, PTP is observed through consecutive pulse application. When stimulated at a high frequency for a short duration, referring to rapid firing of incoming spikes, the synaptic efficiency increases, and the intensity of signal transmission is enhanced. This represents long-term changes in synapses that play a crucial role in longer retention and memory of information.

Our device, which possesses controllable STM characteristics depending on the form of the input pulses, can be applied to various applications related to learning and memorizing. First, we can conduct image training by assigning specific pixel patterns to the memristor. Figure 5a depicts a 5 × 5 synaptic array used to represent the character “S.” The decay time of EPSC can be adjusted depending on the type of stimulus. Moreover, we utilized the number of pulses as a control variable, as shown in Figure 5b. As the number of pulses increases, the amplitude and decay time of EPSC after pulse removal increase. Herein, the number of pulses is analogous to the number of learning iterations, and the EPSC decay level represents the memory level (current level). Figure 5c visualizes the current level of each cell corresponding to each pixel at a specific time after training. When three pulses are applied, the image disappears after 200 ms, but when six pulses are applied, the image $^ { \ast } S ^ { \prime }$ remains visible even after 200 ms. Our experimental findings not only closely resemble the multistore memory model of the human brain but also suggest the potential utilization of our device as a synaptic device for implementing the human visual system. Second, we demonstrated that Pavlov’s experiment can be mimicked using our device. Pavlov’s experiment is crucial as it forms the basis of classical conditioning theory.86 It serves as a typical example of a conditioned reflex, demonstrating that a bell, acting as a conditioned stimulus (CS), when paired with an unconditional stimulus (US), can elicit a conditioned response (CR) from mammalian species. As shown in the inset of Figure 5d, the bell ringing (CS) and food (US) in Pavlov’s dog experiment correspond to voltage pulses of 4 and 5.5 V, respectively. The salivation response induced by the US is referred to as the unconditional response (UR). In Figure 5e, the responses to each stimulus were matched with the current responses. Before training, the dog shows no salivation response (threshold current below 30 μA) to the CS but yields a positive salivation response to the US. During the training process, the dog is exposed to both the CS and US simultaneously. After 10 training sessions, an association between the US and CS is

![](images/1a9c186ddc725ec14bf52e6c41b1cc9f16b292d9ed15c5f9bcdc63c6bcbff272.jpg)

![](images/5f37bbdba9d119cbc791e6a16ea7814fa7e2383019edecc31286d1da2a0aa34d.jpg)

![](images/d121f24af77e93a8d91838309cb5e7fd5b5742ff86a403ee76cc1445ce240e5e.jpg)  
(c)

![](images/0a6b4ac8cc397aea2356f85e51efa1ad45e9ac1841e246e62bd7aa3d70f1139e.jpg)  
(d)

![](images/f2e3e3c597eef6f7a4ad7a14d9ee98b1890f2155c20d472ccd7f57a068e1c34c.jpg)  
(e)

![](images/126ec2c4c9d9871974cc25329ee911a2d37e404c53da8f9300b48e2363a5e0cd.jpg)  
(f)   
Figure 6. (a) Preprocessing of MNIST data for reservoir computing (RC) system simulations and schematic of the RC system. The final current response of the device to 16 different 4 bit input pulse trains with pulse widths of (b) 5 ms, (c) 20 ms, and (d) 40 ms. (e) Accuracy of the RC system according to pulse width. (f) Confusion matrix for a pulse width of 40 ms.

established, and the CR (similar to the UR) (threshold current exceeding 30 $\mu \mathrm { A } )$ is induced by the CS alone. Therefore, the experimental results in Figure $\mathrm { j } _ { \mathrm { d , e } }$ show that our device can effectively emulate Pavlov’s principles of associative learning. Furthermore, in Figure S5a in the Supporting Information, the decline in response when only the CS is applied is demonstrated, indicating the weakening of the established synaptic connection in the absence of the US. Figure S5b in the Supporting Information illustrates the replicable training function akin to Pavlov’s experiment, where the consistent behavior of associative learning from our MFIS devices is evident.

RC systems are a type of ANNs that maintain a part of the network in a dynamic and random state. In the RC system, input data are injected into a fixed neural network structure called the reservoir. The reservoir maintains internal states that vary over time and is used to process input data. Owing to its simplicity and efficiency, flexibility, high-dimensional data processing capability, ease of learning, and robustness to temporal changes, the RC system can be effectively utilized in various applications such as speech recognition, time series prediction, control systems, and signal processing.87,88 We validated the suitability of our device based on HAO for robust RC systems capable of handling various input patterns. Herein, we evaluated an RC system according to pulse width, one of the control variables of STM experimentally investigated in Figure 3c. Figure 6a illustrates the data preprocessing steps for simulation and schematic diagrams of the RC system. The preprocessing steps for Modified National Institute of Standards and Technology (MNIST) database classification

are as follows: first, pixel binarization is employed to simplify handwritten digit images consisting of 784 pixels $( 2 8 \times 2 8 )$ with grayscale information (0−255). Pixels with values between 0 and 127 are assigned a value of zero, while pixels with values between 128 and 255 are assigned a value of one. Subsequently, the binarized pixels are grouped into sets of four pixels each. Consequently, 196 subimages composed of 7 × 28 pixels are generated. Each pixel group is represented by a 4 bit pulse train and applied to the input layer of the RC system, which are transferred toward array of 196 MFIS devices. The pulse train with an amplitude of 5 V and an interval of 1 μs was used, and the pulse width was varied at 5, 20, and 40 ms. The readout layer was a typical multilayer perceptron consisting of 196 input neurons (for the 196 subimages), 100 hidden neurons, and 10 output neurons (for the numbers zero to nine). For training and testing the pattern recognition system, we employed 50,000 training images and 10,000 testing images to evaluate its accuracy. Both the hidden and output layers employed the rectified linear unit (ReLU) and SoftMax as activation functions, with cross-entropy serving as the loss function. Figure 6b−d show the final responses of our reservoir to 16 different 4 bit temporal inputs with pulse widths of 5, 20, and 40 ms, respectively. Detailed information regarding the input pulse scheme is summarized in Figure S6 (Supporting Information), and all current responses for each input train as a function of pulse width are shown in Figure S7 in the Supporting Information. Herein, even if pulse trains containing the same number of $^ { \ast } 1 ^ { \ast }$ inputs are applied, they exhibit different final responses. This is because the pulse sequence, i.e., the number and order of ${ } ^ { \omega } 0 ^ { \it { p } }$ inputs in the pulse train,

exposes the reservoir to various decay situations, thus making temporal changes in current responses highly suitable for the RC system. From the measurements in Figure 6b−d, we recognize that not all 16 reservoir states are distinctly distinguishable. Particularly, for inputs with a pulse width of 5 ms, most of the 16 reservoir states appear with very similar current levels to each other owing to the limits of the dynamic range (on/off ratio). Additionally, in cases of similar current levels at inputs such as 0000 and 1000, the reservoir state may be reversed owing to the conductance variation of the device. However, such nonideal characteristics can be partially mitigated through training via the readout network. Additionally, note that the objective is to design a diversified range of input pulse types within an acceptable accuracy range. Figure 6e shows that after 20 training epochs, the accuracy of the RC system for inputs with pulse widths of 5, 20, and 40 ms reached 93.7%, 95.23%, and 95.83%, respectively. For a more detailed analysis, Figure 6f shows the confusion matrix of the simulation results for the pulse width of 40 ms, which exhibits the highest recognition rate. The confusion matrices for 5 and 20 ms are summarized in Figure S8. This matrix illustrates the recognition rate of each digit compared with all other digits and itself. Each row of the matrix represents an actual digit class, and each column corresponds to a predicted digit class. As shown in Figure 6f, the recognition rate for digit 9, which had the lowest recognition rate, is 94.84%. To enhance accuracy assessment, we implemented both the handwritten digit-based MNIST and the Fashion MNIST data sets. While the original MNIST data set comprises images of handwritten digits from 0 to 9, the Fashion MNIST data set includes images of various apparel items such as clothing, shoes, and bags. Each image is sized 28 × 28 pixels, featuring more complex visual characteristics than the MNIST digit data set. This complexity allows for a more realistic evaluation of model performance (Figure S9a in the Supporting Information). We conducted Fashion MNIST classification across different pulse widths, observing notably high accuracy at 20 and 40 ms, as illustrated in Figure S9b in the Supporting Information. Additionally, the confusion matrix for classification results on the Fashion MNIST data set, based on reservoir computing data, is presented in Figure S9c in the Supporting Information. Additionally, to demonstrate how the pattern recognition accuracy of the RC system varies across different devices, 4 bit reservoir computing data was collected from three distinct devices using a 10 ms pulse width pattern, as illustrated in Figures S10a-c in the Supporting Information. The accuracy results obtained from these devices are presented in Figure S10d in the Supporting Information, where all devices achieved an accuracy of over 94%, despite minor discrepancies in the reservoir state. The results indicate that all three devices consistently achieved a reliable 4 bit reservoir state representation with high accuracy. This consistency across multiple devices highlights the robustness of our memristor in reservoir computing applications, suggesting that the device can reliably maintain complex state representations required for such computational tasks. Consequently, the distinct characteristics of our memristor, particularly its pronounced nonlinearity and volatile behavior, render it highly suitable for reservoir computing applications. The nonlinear I−V characteristics are critical for facilitating complex signal transformations. This nonlinearity enhances the differentiation of input signals within high-dimensional spaces, which is essential for effective reservoir computing. Furthermore, the volatile

nature of our device enables it to exhibit short-term memory, making it particularly adept at processing dynamic temporal patterns encountered in tasks such as time-series prediction and speech recognition. The inherent decay of volatile devices over time prevents the saturation of states, thereby allowing for continuous adaptability and responsiveness to novel input patterns. Overall, these attributes position our memristor as a significant advancement for a broad spectrum of reservoir computing tasks, especially those that necessitate rapid adaptation and real-time processing capabilities. By capitalizing on its nonlinear and volatile characteristics, the device demonstrates superior performance in applications requiring complex and transient dynamics. These features highlight the potential of the MFIS device in neuromorphic computing, with performance comparisons to previously reported studies provided in Table S1 in the Supporting Information. This study emphasizes the integration of multiple functionalities within a single device, making it a promising candidate for neuromorphic computing applications. The ability of our ferroelectric memristor to emulate complex synaptic behaviors not only enhances its performance in reservoir computing tasks but also paves the way for advancements in artificial intelligence and machine learning systems. Furthermore, the scalability of our device allows for potential applications in large-scale neural networks, highlighting its relevance in future computing paradigms.

# ■ CONCLUSION

We fabricated TiN/HAO/ZrO /n+ -Si structured MFIS devices and implemented the RC system with the fabricated devices as the reservoir layers. The STM characteristic of the fabricated device was controllable according to the amplitude, interval, and width of the applied pulse, and the extracted time constants (controlled within the range of 0.01−10 s) were fitted using the SE function. Various STP features of biological synapses such as potentiation/depression, PPF, PTP, and SRDP were successfully mimicked. Furthermore, the experimental implementation of image training related to learning and memorizing the human brain was conducted by adjusting the pulse number, and the CS and US of the classical conditioning theory were matched to the voltage amplitude applied to the device, inducing a CR after training. Finally, we evaluated the RC system by diversifying the width of input pulses, and achieved accuracy values of up to 93.7%, even in the worst-case scenario.

# ASSOCIATED CONTENT

# *sı Supporting Information

The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acsami.4c14910.

Cell-to-cell variability of the device measured form 10 independent cells, The conduction mechanism of the FTJ device in HRS and LRS; Retention loss of LRS current acquired at read bias of 4 V, I−V response of domain switching measured at six different time intervals after the initial set pulse, LTP/LTD characteristics measured over 100 repetitions, Pulse schemes used to evaluate STM/LTM characteristics based on pulse amplitude, interval, and width; Pulse scheme used in SRDP experiments, Weakening of synaptic connection in Pavlov’s experiment under continuous CS application, Rehearsal of the training process through the application

of CS and US 5 times, Pulse schemes utilized in reservoir computing; All current responses of the device to input pulses with pulse widths of 5, 20, and 40 ms; Confusion matrix for the classification results of the MNIST data set using input pulses, 4 bit RC acquired from 3 different devices, Accuracy of the RC system acquired from 3 different devices, Comparison of the MFIS memristor in comparison to the previous two terminal ferroelectric device (PDF)

# ■ AUTHOR INFORMATION

# Corresponding Authors

Sejoon Lee − Department of Semiconductor Science, Quantum-functional Semiconductor Research Center, Dongguk University−Seoul, Seoul 04620, Republic of Korea; orcid.org/0000-0002-4548-7436; Email: sejoon@ dongguk.edu   
Sungjun Kim − Division of Electronics and Electrical Engineering, Dongguk University, Seoul 04620, Republic of Korea; orcid.org/0000-0002-9873-2474; Email: sungjun@dongguk.edu

# Authors

Dongyeol Ju − Division of Electronics and Electrical Engineering, Dongguk University, Seoul 04620, Republic of Korea   
Minseo Noh − Division of Electronics and Electrical Engineering, Dongguk University, Seoul 04620, Republic of Korea; orcid.org/0009-0006-2241-1654   
Gimun Kim − Division of Electronics and Electrical Engineering, Dongguk University, Seoul 04620, Republic of Korea   
Yongjin Park − Division of Electronics and Electrical Engineering, Dongguk University, Seoul 04620, Republic of Korea

Complete contact information is available at:

https://pubs.acs.org/10.1021/acsami.4c14910

# Author Contributions

§ D.J., M.N. and J.K. authors contributed equally.

# Notes

The authors declare no competing financial interest.

# ACKNOWLEDGMENTS

This work was supported in part by the National Research Foundation of Korea (NRF) grant funded by the Ministry of Science and ICT (2023R1A2C1005421) and (RS-2023- 00217673).

# REFERENCES

(1) Zahoor, F.; Azni Zulkifli, T. Z.; Khanday, F. A. Resistive Random Access Memory (RRAM): An Overview of Materials, Switching Mechanism, Performance, Multilevel Cell (Mlc) Storage, Modeling, and Applications. Nanoscale Res. Lett. 2020, 15, 90.   
(2) Athle, R.; Persson, A. E. O.; Troian, A.; Borg, M. Top Electrode Engineering for Freedom in Design and Implementation of Ferroelectric Tunnel Junctions Based on $\mathrm { H f } _ { \mathrm { x } } \mathrm { Z r } _ { \mathrm { x } } \mathrm { O } _ { 2 } .$ ACS Appl. Electron. Mater. 2022, 4 (3), 1002−1009.   
(3) Yu, Y.; Jha, N. K. Energy-Efficient Monolithic Three-Dimensional On-Chip Memory Architectures. IEEE Trans. Nanotechnol. 2018, 17 (4), 620−633.

(4) Poon, C. S.; Zhou, K. Neuromorphic Silicon Neurons and Large-Scale Neural Networks: Challenges and Opportunities. Front. Neurosci. 2011, 5, 108.   
(5) Markovic,́ D.; Mizrahi, A.; Querlioz, D.; Grollier, J. Physics for Neuromorphic Computing. Nat. Rev. Phys. 2020, 2, 499−510.   
(6) Kirkwood, A.; Rioult, M. G.; Bear, M. F. Experience-Dependent Modification of Synaptic Plasticity in Visual Cortex. Nature 1996, 381, 526−528.   
(7) Yang, R.; Huang, H. M.; Guo, X. Memristive Synapses and Neurons for Bioinspired Computing. Adv. Electron. Mater. 2019, 5 (9), 1900287.   
(8) Raymond, C. R. LTP Forms 1, 2 and 3: Different Mechanisms for the “long” in Long-Term Potentiation. Trends Neurosci. 2007, 30, 167−175.   
(9) Goh, Y.; Jeon, S. The Effect of the Bottom Electrode on Ferroelectric Tunnel Junctions Based on CMOS-Compatible HfO2. Nanotechnology 2018, 29 (33), 335201.   
(10) Chen, L.; Wang, T. Y.; Dai, Y. W.; Cha, M. Y.; Zhu, H.; Sun, Q. Q.; Ding, S. J.; Zhou, P.; Chua, L.; Zhang, D. W. Ultra-Low Power Hf0.5Zr0.5O2 Based Ferroelectric Tunnel Junction Synapses for Hardware Neural Network Applications. Nanoscale 2018, 10 (33), 15826−15833.   
(11) Ambriz-Vargas, F.; Kolhatkar, G.; Broyer, M.; Hadj-Youssef, A.; Nouar, R.; Sarkissian, A.; Thomas, R.; Gomez-Yáñez, C.; Gauthier, M. A.; Ruediger, A. A Complementary Metal Oxide Semiconductor Process-Compatible Ferroelectric Tunnel Junction. ACS Appl. Mater. Interfaces 2017, 9 (15), 13262−13268.   
(12) Yoon, J.; Hong, S.; Song, Y. W.; Ahn, J. H.; Ahn, S. E. Understanding Tunneling Electroresistance Effect through Potential Profile in Pt/Hf0.5Zr0.5O2/TiN Ferroelectric Tunnel Junction Memory. Appl. Phys. Lett. 2019, 115 (15), 153502.   
(13) Berdan, R.; Marukame, T.; Ota, K.; Yamaguchi, M.; Saitoh, M.; Fujii, S.; Deguchi, J.; Nishi, Y. Low-Power Linear Computation Using Nonlinear Ferroelectric Tunnel Junction Memristors. Nat. Electron. 2020, 3 (5), 259−266.   
(14) Luo, Z.; Wang, Z.; Guan, Z.; Ma, C.; Zhao, L.; Liu, C.; Sun, H.; Wang, H.; Lin, Y.; Jin, X.; Yin, Y.; Li, X. High-Precision and Linear Weight Updates by Subnanosecond Pulses in Ferroelectric Tunnel Junction for Neuro-Inspired Computing. Nat. Commun. 2022, 13 (1), 699.   
(15) Shekhawat, A.; Walters, G.; Yang, N.; Guo, J.; Nishida, T.; Moghaddam, S. Data Retention and Low Voltage Operation of Al2O3/Hf0.5Zr0.5O2based Ferroelectric Tunnel Junctions. Nanotechnology 2020, 31 (39), 39LT01.   
(16) Tokumitsu, E.; Okamoto, K.; Ishiwara, H. Low Voltage Operation of Nonvolatile Metal-Ferroelectric-Metal-Insulator-Semiconductor (MFMIS)-Field-Effect-Transistors (FETs) Using Pt/ SrBi2Ta2O9/Pt/SrTa2O6/SiON/Si Structures. J. Appl. Phys. 2001, 40, 2917.   
(17) Shih, W. C.; Juan, P. C.; Lee, J. Y. M. Fabrication and Characterization of Metal-Ferroelectric (PbZr0.53Ti0.47O3) -Insulator (Y2O3) -Semiconductor Field Effect Transistors for Nonvolatile Memory Applications. J. Appl. Phys. 2008, 103 (9), 094110.   
(18) Chen, Y. Q.; Xu, X. B.; Lei, Z. F.; Liao, X. Y.; Wang, X.; Zeng, C.; En, Y. F.; Huang, Y. Effect of Temperature on the Electrical Properties of a Metal-Ferroelectric (SrBi2Ta2O9)-Insulator (HfTaO)-Silicon Capacitor. J. Phys. D Appl. Phys. 2015, 48 (3), 035109.   
(19) Zhou, J.; Zhou, Z.; Wang, X.; Wang, H.; Sun, C.; Han, K.; Kang, Y.; Gong, X. Demonstration of Ferroelectricity in Al-Doped HfO with a Low Thermal Budget of 500 °C. IEEE Electron Device Lett. 2020, 41 (7), 1130−1133.   
(20) Li, S.; Zheng, Y.; Jakoby, R.; Klein, A. Electrically Programmable Bistable Capacitor for High-Frequency Applications Based on Charge Storage at the (Ba,Sr)TiO 3/Al 2O 3 Interface. Adv. Funct. Mater. 2012, 22 (22), 4827−4832.   
(21) Park, J. Y.; Choe, D. H.; Lee, D. H.; Yu, G. T.; Yang, K.; Kim, S. H.; Park, G. H.; Nam, S. G.; Lee, H. J.; Jo, S.; Kuh, B. J.; Ha, D.; Kim, Y.; Heo, J.; Park, M. H. Revival of Ferroelectric Memories Based on

Emerging Fluorite-Structured Ferroelectrics. Adv. Mater. 2023, 35, 2204904.   
(22) Kim, J.; Kim, D.; Min, K. K.; Kraatz, M.; Han, T.; Kim, S. Effect of Al Concentration on Ferroelectric Properties in HfAlO -Based Ferroelectric Tunnel Junction Devices for Neuroinspired Applications. Adv. Intell. Syst. 2023, 5 (8), 1900287.   
(23) Park, Y.; Kim, J.; Kim, S.; Kim, D.; Shim, W.; Kim, S. Effect of interfacial SiO layer thickness on the memory performances in the HfAlO -based ferroelectric tunnel junction for a neuromorphic system. J. Mater. Chem. C 2023, 11 (40), 13886−13896.   
(24) Xiao, W.; Liu, C.; Peng, Y.; Zheng, S.; Feng, Q.; Zhang, C.; Zhang, J.; Hao, Y.; Liao, M.; Zhou, Y. Performance Improvement of Hf0.5Zr0.5O2-Based Ferroelectric-Field-Effect Transistors With ZrO2 Seed Layers. IEEE Electron Device Lett. 2019, 40 (5), 714−717.   
(25) Kim, J.; Kwon, O.; Lim, E.; Kim, D.; Kim, S. Impact of annealing temperature on the remanent polarization and tunneling electro-resistance of ferroelectric Al-doped HfO tunnel junction memory. Phys. Chem. Chem. Phys. 2023, 25 (6), 4588−4597.   
(26) Starschich, S.; Boettger, U. An Extensive Study of the Influence of Dopants on the Ferroelectric Properties of HfO2. J. Mater. Chem. C 2017, 5 (2), 333−338.   
(27) Böscke, T. S.; Teichert, S.; Bräuhaus, D.; Müller, J.; Schröder, U.; Böttger, U.; Mikolajick, T. Phase Transitions in Ferroelectric Silicon Doped Hafnium Oxide. Appl. Phys. Lett. 2011, 99 (11), 112904.   
(28) Müller, J.; Schröder, U.; Böscke, T. S.; Müller, I.; Böttger, U.; Wilde, L.; Sundqvist, J.; Lemberger, M.; Kücher, P.; Mikolajick, T.; Frey, L. Ferroelectricity in Yttrium-Doped Hafnium Oxide. J. Appl. Phys. 2011, 110 (11), 114113.   
(29) Lomenzo, P. D.; Takmeel, Q.; Moghaddam, S.; Nishida, T. Annealing Behavior of Ferroelectric Si-Doped HfO2 Thin Films. Thin Solid Films 2016, 615, 139−144.   
(30) Mueller, S.; Mueller, J.; Singh, A.; Riedel, S.; Sundqvist, J.; Schroeder, U.; Mikolajick, T. Incipient Ferroelectricity in Al-Doped HfO 2 Thin Films. Adv. Funct. Mater. 2012, 22 (11), 2412−2417.   
(31) Hwang, J.; Goh, Y.; Jeon, S. Effect of Forming Gas High-Pressure Annealing on Metal-Ferroelectric-Semiconductor Hafnia Ferroelectric Tunnel Junction. IEEE Electron Device Lett. 2020, 41 (8), 1193−1196.   
(32) Goh, Y.; Hwang, J.; Kim, M.; Lee, Y.; Jung, M.; Jeon, S. Selector-Less Ferroelectric Tunnel Junctions by Stress Engineering and an Imprinting Effect for High-Density Cross-Point Synapse Arrays. ACS Appl. Mater. Interfaces 2021, 13 (49), 59422−59430.   
(33) Goh, Y.; Hwang, J.; Jeon, S. Excellent Reliability and High-Speed Antiferroelectric HfZrO2Tunnel Junction by a High-Pressure Annealing Process and Built-In Bias Engineering. ACS Appl. Mater. Interfaces 2020, 12 (51), 57539−57546.   
(34) Shkuratov, S. I.; Lynch, C. S. A Review of Ferroelectric Materials for High Power Devices. J. Materiomics. 2022, 8 (4), 739− 752.   
(35) Ryu, H.; Xu, K.; Kim, J.; Kang, S.; Guo, J.; Zhu, W. Exploring New Metal Electrodes for Ferroelectric Aluminum-Doped Hafnium Oxide. IEEE Trans. Electron Devices 2019, 66 (5), 2359−2364.   
(36) Lee, S. J.; Kim, M. J.; Lee, T. Y.; Lee, T. I.; Bong, J. H.; Shin, S. W.; Kim, S. H.; Hwang, W. S.; Cho, B. J. Effect of ZrO2 Interfacial Layer on Forming Ferroelectric HfxZryOz on Si Substrate. AIP Adv. 2019, 9 (12), 125020.   
(37) Kim, Y.; Min, K. K.; Yu, J.; Kwon, D.; Park, B. G. Lamination Method for Improved Polarization-Leakage Current Relation in HfO2-Based Metal/Ferroelectric/Insulator/Semiconductor Structure. Semicond. Sci. Technol. 2022, 37 (4), 045001.   
(38) Zhang, Y.; Wang, D.; Wang, J.; Luo, C.; Li, M.; Li, Y.; Tao, R.; Chen, D.; Fan, Z.; Dai, J. Y.; Zhou, G.; Lu, X.; Liu, J. M. Growth of the Orthorhombic Phase and Inhibition of Charge Injection in Ferroelectric HfO2-Based MFIS Memory Devices with a High-Permittivity Dielectric Seed Layer. Sci. China Mater. 2023, 66 (1), 219−232.   
(39) Park, Y.; Kim, M. K.; Lee, J. S. Emerging Memory Devices for Artificial Synapses. J. Mater. Chem. C 2020, 8, 9163−9183.

(40) Sun, Y.; Li, J.; Li, S.; Jiang, Y.; Wan, E.; Zhang, J.; Shi, Y.; Pan, L. Advanced Synaptic Devices and Their Applications in Biomimetic Sensory Neural System. Chip 2023, 2 (1), 100031.   
(41) Li, J.; Ge, C.; Lu, H.; Guo, H.; Guo, E. J.; He, M.; Wang, C.; Yang, G.; Jin, K. Energy-Efficient Artificial Synapses Based on Oxide Tunnel Junctions. ACS Appl. Mater. Interfaces 2019, 11 (46), 43473− 43479.   
(42) Du, C.; Cai, F.; Zidan, M. A.; Ma, W.; Lee, S. H.; Lu, W. D. Reservoir computing using dynamic memristors for temporal information processing. Nat. Commun. 2017, 8 (1), 2204.   
(43) Midya, R.; Wang, Z.; Asapu, S.; Zhang, X.; Rao, M.; Song, W.; Zhuo, Y.; Upadhyay, N.; Xia, Q.; Yang, J. J. Reservoir computing using diffusive memristors. Adv. Intell. Syst. 2019, 1 (7), 1900084.   
(44) Armendarez, N. X.; Mohamed, A. S.; Dhungel, A.; Hossain, M. R.; Hasan, M. S.; Najem, J. S. Brain-Inspired Reservoir Computing Using Memristors with Tunable Dynamics and Short-Term Plasticity. ACS Appl. Mater. Interfaces 2024, 16 (5), 6176−6188.   
(45) Maraj, J. J.; Haughn, K. P.; Inman, D. J.; Sarles, S. A. Sensory adaptation in biomolecular memristors improves reservoir computing performance. Adv. Intell. Syst. 2023, 5 (8), 2300049.   
(46) Lukosevic ̌ ius, ̌ M.; Jaeger, H. Reservoir Computing Approaches to Recurrent Neural Network Training. Comput. Sci. Rev. 2009, 3 (3), 127−149.   
(47) Gauthier, D. J.; Bollt, E.; Griffith, A.; Barbosa, W. A. S. Next Generation Reservoir Computing. Nat. Commun. 2021, 12 (1), 5564.   
(48) Tanaka, G.; Yamane, T.; Héroux, J. B.; Nakane, R.; Kanazawa, N.; Takeda, S.; Numata, H.; Nakano, D.; Hirose, A. Recent Advances in Physical Reservoir Computing: A Review. Neural Networks 2019, 115, 100−123.   
(49) Shahi, S.; Fenton, F. H.; Cherry, E. M. Prediction of Chaotic Time Series Using Recurrent Neural Networks and Reservoir Computing Techniques: A Comparative Study. Mach. Learn. Appl. 2022, 8, 100300.   
(50) Pathak, J.; Hunt, B.; Girvan, M.; Lu, Z.; Ott, E. Model-Free Prediction of Large Spatiotemporally Chaotic Systems from Data: A Reservoir Computing Approach. Phys. Rev. Lett. 2018, 120, 024102.   
(51) Du, C.; Cai, F.; Zidan, M. A.; Ma, W.; Lee, S. H.; Lu, W. D. Reservoir Computing Using Dynamic Memristors for Temporal Information Processing. Nat. Commun. 2017, 8 (1), 2204.   
(52) Kim, D.; Shin, J.; Kim, S. Implementation of reservoir computing using volatile WO -based memristor. Appl. Surf. Sci. 2022, 599, 153876.   
(53) Li, R.; Yang, H.; Zhang, Y.; Tang, N.; Chen, R.; Zhou, Z.; Liu, L.; Kang, J.; Huang, P. Adjustable Short-Term Memory of SiOx:Ag-Based Memristor for Reservoir Computing. Nanotechnology 2023, 34 (50), 505207.   
(54) Park, M. H.; Lee, Y. H.; Kim, H. J.; Kim, Y. J.; Moon, T.; Do Kim, K.; Müller, J.; Kersch, A.; Schroeder, U.; Mikolajick, T.; Hwang, C. S. Ferroelectricity and Antiferroelectricity of Doped Thin HfO2- Based Films. Adv. Mater. 2015, 27, 1811−1831.   
(55) Yang, Y.; Wu, M.; Zheng, X.; Zheng, C.; Xu, J.; Xu, Z.; Li, X.; Lou, X.; Wu, D.; Liu, X.; Pennycook, S. J.; Wen, Z. Atomic-Scale Fatigue Mechanism of Ferroelectric Tunnel Junctions. Adv. Sci. 2021, 7, 2761.   
(56) Park, M. H.; Kim, H. J.; Kim, Y. J.; Lee, Y. H.; Moon, T.; Kim, K. D.; Hyun, S. D.; Fengler, F.; Schroeder, U.; Hwang, C. S. Effect of Zr Content on the Wake-Up Effect in Hf Zr O Films. ACS Appl. Mater. Interfaces 2016, 8 (24), 15466−15475.   
(57) Chen, J.; Jin, C.; Yu, X.; Jia, X.; Peng, Y.; Liu, Y.; Chen, B.; Cheng, R.; Han, G. Impact of Oxygen Vacancy on Ferroelectric Characteristics and Its Implication for Wake-Up and Fatigue of HfO - Based Thin Films. IEEE Trans. Electron Devices 2022, 69, 5297−5301.   
(58) Kim, H. J.; Park, M. H.; Kim, Y. J.; Lee, Y. H.; Moon, T.; Kim, K. D.; Hyun, S. D.; Hwang, C. S. A Study on the Wake-up Effect of Ferroelectric Hf0.5Zr0.5O2 Films by Pulse-Switching Measurement. Nanoscale 2016, 8 (3), 1383−1389.   
(59) Shin, W.; Min, K. K.; Bae, J. H.; Yim, J.; Kwon, D.; Kim, Y.; Yu, J.; Hwang, J.; Park, B. G.; Kwon, D.; Lee, J. H. Comprehensive and Accurate Analysis of the Working Principle in Ferroelectric Tunnel

Junctions Using Low-Frequency Noise Spectroscopy. Nanoscale 2022, 14 (6), 2177−2185.   
(60) Shin, W.; Min, K. K.; Bae, J. H.; Kim, J.; Koo, R. H.; Kwon, D.; Kim, J. J.; Kwon, D.; Lee, J. H. 1/f Noise in Synaptic Ferroelectric Tunnel Junction: Impact on Convolutional Neural Network. Adv. Intell. Syst. 2023, 5, 2200377.   
(61) Xia, X.; Huang, W.; Hang, P.; Guo, T.; Yan, Y.; Yang, J.; Yang, D.; Yu, X.; Li, X. 2D-Material-Based Volatile and Nonvolatile Memristive Devices for Neuromorphic Computing. ACS Mater. Lett. 2023, 5 (4), 1109−1135.   
(62) Pan, X.; Zheng, Y.; Shi, Y.; Chen, W. Surface Charge Transfer Doping Enabled Large Hysteresis in van Der Waals Heterostructures for Artificial Synapse. ACS Mater. Lett. 2021, 3 (2), 235−242.   
(63) Huang, W.; Xia, X.; Zhu, C.; Steichen, P.; Quan, W.; Mao, W.; Yang, J.; Chu, L.; Li, X. Memristive Artificial Synapses for Neuromorphic Computing. Nano-Micro Lett. 2021, 13, 85.   
(64) Ismail, M.; Rasheed, M.; Mahata, C.; Kang, M.; Kim, S. Mimicking Biological Synapses with A-HfSiOx-Based Memristor: Implications for Artificial Intelligence and Memory Applications. Nano Convergence 2023, 10 (1), 33.   
(65) Kerr, D. S.; Huggett, A. M.; Abraham, W. C. Modulation of Hippocampal Long-Term Potentiation and Long-Term Depression by Corticosteroid Receptor Activation. Psychobiology 1994, 22, 123− 133.   
(66) Park, J.; Song, M. S.; Youn, S.; Kim, T. H.; Kim, S.; Hong, K.; Kim, H. Intrinsic Variation Effect in Memristive Neural Network with Weight Quantization. Nanotechnology 2022, 33 (37), 375203.   
(67) Shin, W.; Im, J.; Koo, R. H.; Kim, J.; Kwon, K. R.; Kwon, D.; Kim, J. J.; Lee, J. H.; Kwon, D. Self-Curable Synaptic Ferroelectric FET Arrays for Neuromorphic Convolutional Neural Network. Adv. Sci. 2023, 10 (15), 2207661.   
(68) Yang, J.; Cho, H.; Ryu, H.; Ismail, M.; Mahata, C.; Kim, S. Tunable Synaptic Characteristics of a Ti/TiO2/Si Memory Device for Reservoir Computing. ACS Appl. Mater. Interfaces 2021, 13 (28), 33244−33252.   
(69) Majumdar, S. Ultrafast Switching and Linear Conductance Modulation in Ferroelectric Tunnel Junctions: Via P(VDF-TrFE) Morphology Control. Nanoscale 2021, 13 (25), 11270−11278.   
(70) Li, C.; Zhang, X.; Chen, P.; Zhou, K.; Yu, J.; Wu, G.; Xiang, D.; Jiang, H.; Wang, M.; Liu, Q. Short-Term Synaptic Plasticity in Emerging Devices for Neuromorphic Computing. iScience 2023, 26, 106315.   
(71) Dutta, S.; Saha, A.; Chakraborty, W.; Gomez, J.; Khanna, A.; Gupta, S.; Roy, K.; Datta, S. Biologically Plausible Ferroelectric Quasi-Leaky Integrate and Fire Neuron. In 2019 Symposium on VLSI Technology; IEEE, 2019, pp T140−T141..   
(72) Ediger, M. D.; Angell, C. A.; Nagel, S. R. Supercooled Liquids and Glasses. J. Chem. Phys. 1996, 100, 13200−13212.   
(73) Potuzak, M.; Welch, R. C.; Mauro, J. C. Topological Origin of Stretched Exponential Relaxation in Glass. J. Chem. Phys. 2011, 135 (21), 214502.   
(74) Kakalios, J.; Street, R. A.; Jackson, W. B. Stretched-Exponential Relaxation Arising from Dispersive Diffusion of Hydrogen in Amorphous Silicon. Rev. Lett. 1987, 59, 1037−1040.   
(75) Lee, J. K.; Chung, H. J.; Heo, J.; Seo, S.; Cho, I. H.; Kwon, H. I.; Lee, J. H. Reliability of Bottom-Gate Graphene Field-Effect Transistors Prepared by Using Inductively Coupled Plasma-Chemical Vapor Deposition. Appl. Phys. Lett. 2011, 98 (19), 193504.   
(76) Lee, J. M.; Cho, I. T.; Lee, J. H.; Kwon, H. I. Bias-Stress-Induced Stretched-Exponential Time Dependence of Threshold Voltage Shift in InGaZnO Thin Film Transistors. Appl. Phys. Lett. 2008, 93 (9), 093504.   
(77) Subramanian Periyal, S.; Jagadeeswararao, M.; Ng, S. E.; John, R. A.; Mathews, N. Halide Perovskite Quantum Dots Photosensitized-Amorphous Oxide Transistors for Multimodal Synapses. Adv. Mater. Technol. 2020, 5 (11), 2000514.   
(78) Chen, H.; Liu, C.; Wu, Z.; He, Y.; Wang, Z.; Zhang, H.; Wan, Q.; Hu, W.; Zhang, D. W.; Liu, M.; Liu, Q.; Zhou, P. Time-Tailoring

van Der Waals Heterostructures for Human Memory System Programming. Adv. Sci. 2019, 6 (20), 1901072.   
(79) Guo, R.; Lin, W.; Yan, X.; Venkatesan, T.; Chen, J. Ferroic tunnel junctions and their application in neuromorphic networks. Appl. Phys. Rev. 2020, 7, 011304.   
(80) Han, C.; Han, X.; Han, J.; He, M.; Peng, S.; Zhang, C.; Liu, X.; Gou, J.; Wang, J. Light-Stimulated Synaptic Transistor with High PPF Feature for Artificial Visual Perception System Application. Adv. Funct. Mater. 2022, 32 (22), 2113053.   
(81) Zhang, Y.; Liu, L.; Tu, B.; Cui, B.; Guo, J.; Zhao, X.; Wang, J.; Yan, Y. An Artificial Synapse Based on Molecular Junctions. Nat. Commun. 2023, 14 (1), 247.   
(82) Shin, S.; Kang, D. C.; Kim, K.; Jeong, Y.; Kim, J.; Lee, S.; Kwak, J. Y.; Park, J.; Hwang, G. W.; Lee, K. S.; Park, J. K.; Li, J.; Kim, I. Emulating the Short-Term Plasticity of a Biological Synapse with a Ruthenium Complex-Based Organic Mixed Ionic-Electronic Conductor. Mater. Adv. 2022, 3 (6), 2827−2837.   
(83) Zucker, R. S.; Regehr, W. G. Short-Term Synaptic Plasticity. Annu. Rev. Physiol. 2002, 64, 355−405.   
(84) Munakata, Y.; Pfaffly, J. Hebbian Learning and Development. Dev. Sci. 2004, 7, 141−148.   
(85) Pershin, Y. V.; Di Ventra, M. Experimental Demonstration of Associative Memory with Memristive Neural Networks. Neural Networks 2010, 23 (7), 881−886.   
(86) Jena, A. K.; Sahu, M. C.; Mohanan, K. U.; Mallik, S. K.; Sahoo, S.; Pradhan, G. K.; Sahoo, S. Bipolar Resistive Switching in TiO2Artificial Synapse Mimicking Pavlov’s Associative Learning. ACS Appl. Mater. Interfaces 2023, 15 (2), 3574−3585.   
(87) Matsukatova, A. N.; Prudnikov, N. V.; Kulagin, V. A.; Battistoni, S.; Minnekhanov, A. A.; Trofimov, A. D.; Nesmelov, A. A.; Zavyalov, S. A.; Malakhova, Y. N.; Parmeggiani, M.; Ballesio, A.; Marasso, S. L.; Chvalun, S. N.; Demin, V. A.; Emelyanov, A. V.; Erokhin, V. Combination of Organic-Based Reservoir Computing and Spiking Neuromorphic Systems for a Robust and Efficient Pattern Classification. Adv. Intell. Syst. 2023, 5 (6), 2200407.   
(88) Cao, J.; Zhang, X.; Cheng, H.; Qiu, J.; Liu, X.; Wang, M.; Liu, Q. Emerging Dynamic Memristors for Neuromorphic Reservoir Computing. Nanoscale 2022, 14, 289−298.