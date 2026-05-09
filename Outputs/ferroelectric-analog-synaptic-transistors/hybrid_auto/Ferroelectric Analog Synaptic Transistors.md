---
title: "ASSOCIATED CONTENT"
authors:
  - "Min-Kyu Kim"
  - "Jang-Sik Lee"
date: "2019-01-30"
year: "2019"
journal: "Nano Letters"
abstract: "Neuromorphic computing is a promising alternative to conventional computing systems\\"
abstract_cn: "神经形态计算是传统计算系统的一种有前景的替代方案，因为它可以实现并行计算和自适应学习过程。然而，高能效神经形态硬件系统的发展受到了模拟突触器件性能有限的制约。本文展示了具有纳米级铁电材料和氧化物半导体的铁电薄膜晶体管（FeTFT）中的模拟电导调制行为。通过精确控制纳米级铁电层中的极化变化来诱导电导调制，展示了FeTFT的线性增强和抑制特性。我们的器件展示了高线性度、多状态和小周期/器件间差异的增强和抑制性能。在使用测量特性的仿真中，基于FeTFT的神经形态系统实现了91.1%的手写数字识别准确率。该工作为实现使用FeTFT作为突触器件的神经形态硬件系统提供了一条途径。"
keywords:
  - "[[Ferroelectric Materials]]"
  - "[[Thin-Film Transistors]]"
  - "[[Multilevel Data Storage]]"
  - "[[Artificial Synapses]]"
  - "[[Neuromorphic Computing]]"
  - "[[Analog Conductance Modulation]]"
  - "[[铁电材料]]"
  - "[[薄膜晶体管]]"
  - "[[人工突触]]"
  - "[[神经形态计算]]"
cite: "Kim M K, Lee J S. Ferroelectric Analog Synaptic Transistors[J]. Nano Letters, 2019,\\"
aiSum: "本文展示了基于铁电材料和氧化物半导体的FeTFT器件的模拟电导调制行为。通过精确控制铁电层极化实现线性突触权重更新，器件展现了高线性度、多状态（32个状态）和低变异性的增强/抑制特性。基于实测参数的仿真中，神经形态系统达到91.1%的MNIST手写数字识别准确率。该工作为神经形态硬件中突触器件的实现提供了可行方案。"
confidence: "high"
wiki_concepts:
  - "[[Neuromorphic computing]]"
---

Min-Kyu Kim and Jang-Sik Lee*

Department of Materials Science and Engineering, Pohang University of Science and Technology (POSTECH), Pohang 37673, Korea

S Supporting Information

![](images/89b1a57ab68c0b5a5fe167c8959ff39c225aaaf782be910354d28a40b0a32474.jpg)

ABSTRACT: [[neuromorphic computing]] is a promising alternative to conventional computing systems as it could enable parallel computation and adaptive learning process. However, the development of energy efficient neuromorphic hardware systems has been hindered by the limited performance of analog synaptic devices. Here, we demonstrate the analog conductance modulation behavior in the ferroelectric [[thin-film transistors]] (FeTFT) that have the nanoscale ferroelectric material and oxide semiconductors. Accurate control of polarization changes in the nanoscale ferroelectric layer induces conductance modulation to demonstrate linear potentiation and depression characteristics of FeTFTs. Our devices show potentiation and depression properties, including high linearity, multiple states, and small cycle-to-cycle/device-to-device variations. In simulations with measured properties, a neuromorphic system with FeTFT achieves 91.1% recognition accuracy of handwritten digits. This work may provide a way to realize the neuromorphic hardware systems that use FeTFTs as the synaptic devices.

[[KEYWORDS: Ferroelectric materials]], [[thin-film transistors]], [[multilevel data storage]], [[artificial synapses]], [[neuromorphic computing]], [[analog conductance modulations]]

D evelopment of an efficient computing system may be a way to overcome the scaling limits of complementary metal-oxide-semiconductor (CMOS) devices.1−3 Conventional von Neumann computing systems separate memory from logic; the communication between these components increases the power consumption and heat generation in conventional computing systems.4 New computing paradigms such as [[neuromorphic computing]] can overcome this problem. [[neuromorphic computing]] replicates the structure of the human brain and may enable highly efficient computing by parallel computation and adaptive learning.5,6 Efficient [[neuromorphic computing]] systems require synaptic devices that can achieve analog updates of synaptic weights. Various devices have been successfully demonstrated as synaptic devices to realize [[neuromorphic computing]] hardware 7−19 but some of them have suffered from a small on/off ratio, undesirable variations, poor data retention, and nonlinear weight-update properties. High accuracy in neuromorphic systems requires development of devices that have ideal synaptic properties.20−22

Ferroelectric materials have a great potential to meet these requirements.23,24 Ferroelectric materials have spontaneous

polarization states that can be maintained even without an external electric field. Delicate control of polarization is possible because domains in ferroelectric materials can be controlled by an applied electric field.25,26 Each polarization state of the ferroelectric layer can be confirmed by changes in channel conductance; to exploit this characteristic, ferroelectric materials have been evaluated as the dielectric layer in transistors.27−29 The conductance of channel material in ferroelectric transistor can be gradually controlled by the polarization of ferroelectric materials.23,30 These characteristics can be the solution to solve some problems in current synapse devices, such as a small on/off ratio, nonlinear weight updates, and variations in electric properties. So, ferroelectric transistors constitute promising candidates for memory and synaptic devices.24,25,31,32 However, ferroelectric materials have been reported to show some issues, for example, complex compositions, high annealing temperatures, and difficulty in scaling. 33−35 These problems can also be critical in ferroelectric

Received: January 15, 2019

Published: January 30, 2019

![](images/0621b3f5421eb81cddecf8b0f5c36055ee1e43eac863a62d55fd46af77164e98.jpg)  
(a)

![](images/0d463c3cf68f13c6fdd9e3a94e3f07277a04a967576a35edc6fd6f297ce5a0d7.jpg)  
(b)

![](images/eb22741789d3ed82ea14fc101476c345eca88b7982620bcbfffd87b0ed8eda95.jpg)  
（c)  
Figure 1. (a) Schematic structure of ferroelectric thin-film transistor (FeTFT). (b) Polarization−voltage (P−V) hysteresis curve (inset: schematic of MFS structure with $\mathrm { A l / I G Z O / H f Z r O _ { \it x } / T i N ) }$ . (c) Capacitance−voltage (C−V) characteristic of the $\mathrm { A l / I G Z O / H f Z r O } _ { x } / \mathrm { T i N }$ structure.

![](images/e14b576a6e66d86a3251521699dc162da984ac81f5ba775c68c354613fa6af9e.jpg)

![](images/81b770980e6937611b8366d2a020e5cb60a35087a674f754c0cba5fd8eec8aeb.jpg)  
(b)   
Figure 2. (a) Transfer curve of ferroelectric thin-film transistor. (b) ac operation characteristics of ferroelectric thin-film transistor with programming pulses (6 V, 30 ms) and erasing pulses $\left( - 6 \mathrm { ~ V } , 3 0 \mathrm { ~ m s } \right)$ .

synaptic devices. Additionally, ferroelectric transistors based on Si cause formation of interfacial layers when ferroelectric materials are deposited directly on the Si substrate due to high annealing temperature and volatile elements such as Pb in the ferroelectric layer. Interfacial layers can cause high operation voltage, poor retention, and small memory windows.36,37 To overcome these limitations, ferroelectric materials based on nanoscale hafnium oxide $\left( \mathrm { H f O } _ { x } \right)$ have been suggested. Ferroelectric materials based on $\mathrm { H f O } _ { x }$ have various advantages, such as CMOS compatibility, low process temperature, and process scalability. $3 8 - \dot { 4 } 4$ Use of oxide semiconductors and low temperature HfO -based ferroelectric layers can minimize the formation of interfacial layers, so these materials are desirable as channel materials and ferroelectric layers in ferroelectric transistors. Therefore, a ferroelectric transistor based on nanoscale HfO and an oxide semiconductor could be useful in fabricating synaptic devices with CMOS compatibility, process scalability, and desirable synaptic characteristics.

In this study, we fabricate ferroelectric thin-film transistor (FeTFT) based on nanoscale ferroelectric material and oxide semiconductor to investigate the feasibility of FeTFTs as synaptic devices. The FeTFT shows the ferroelectric hysteresis in its transfer curve, [[multilevel data storage]] capability, and data retention property. We demonstrate analog potentiation and depression characteristics of FeTFTs. This paper shows the feasibility of FeTFT as the synaptic device for the neuromorphic hardware systems.

Results and Discussion. FeTFTs with metal−ferroelectric−semiconductor (MFS) structure were fabricated

(Figure 1a). Prior to the fabrication of MFS structure, the basic ferroelectric characteristics of metal−ferroelectric−metal (MFM) capacitors (TiN/zirconium-doped hafnium oxide $\left( \mathrm { H f Z r O } _ { x } \right) / \bar { \mathrm { T i N } } )$ were measured (Figure S1). Ferroelectric polarization hysteresis curves with different sweep voltages are shown in Figure S1a. The capacitors had the typical capacitance−voltage (C−V) curve of ferroelectric materials. $\mathrm { H f Z r O } _ { x }$ was used as the ferroelectric layer in the FeTFTs (Figure S1b). Stable ferroelectric polarization−voltage (P−V) characteristics were also observed from $\mathrm { T i N / H f \bar { Z } r O } _ { x } / \mathrm { T i N }$ structure with different device sizes (Figure S2). In addition, we confirmed that it is possible to operate the ferroelectric capacitors with a size of $1 \times 1 ~ \mu \mathrm { m } ^ { 2 }$ by measurement using electrostatic force microscopy. To enable use of a ferroelectric material based on $\mathrm { H f Z r O } _ { x }$ as dielectric layer, the FeTFTs were fabricated with a bottom-gate structure. This structure is suitable because induction of ferroelectric properties in $\mathrm { H f Z r O } _ { x }$ layer requires an appropriate bottom layer. 45,46 To fabricate MFS structure, $\mathrm { H f Z r O } _ { x }$ was transformed to the ferroelectric phase by thermal annealing on the TiN gate electrode. Then a layer of indium gallium zinc oxide (IGZO) was deposited as the channel layer on the $\mathrm { { H f Z r O } } _ { x }$ layer. To investigate the ferroelectric properties in MFS structure, P−V measurements were performed by applying voltage to the TiN bottom electrode with the Al top electrode grounded (Figure 1b). The hysteresis loop indicated that positive remnant polarization $\dot { \left( \right)} + P _ { \mathrm { r } }  = 5 . 3 \ \dot { \mu } \mathrm { C } / \mathrm { c m } ^ { 2 }$ and $- P _ { \mathrm { r } } = - 5 . 9 ~ \mu \mathrm { C } / \mathrm { c m } ^ { 2 }$ . In addition, to estimate the reliability of MFS structure, the endurance properties of $\mathrm { A l / I G Z O / H f Z r O } _ { x } / \mathrm { T i N }$ structure

![](images/e4a077ee4644ca123bf114dd3daef7161a69d46dece3000f4d71a71c8daa2639.jpg)

![](images/03e7e8c541081905f35f001419060871eef0190e513f90e8e3a1ee0c97322cf9.jpg)  
Figure 3. (a) The multiple levels of the ferroelectric thin-film transistor. (b) Schematic illustrations of suggested mechanism of [[multilevel data storage]]. The direction and size of arrow represent the direction and value of polarization in HfZrOx layer, respectively.

were tested by applying pulses $\left( \pm 7 \ \mathrm { V } , \ 1 0 \ \mu s \right)$ . Ferroelectric properties of MFS structure was retained without degradation for 105 cycles (Figure S3). The C−V curve revealed the charge responses of MFS structure according to the applied voltages (Figure 1c). A butterfly shaped curve was observed, which is a result of the ferroelectric nature of $\mathrm { H f Z r O } _ { x } .$ Capacitance decreased when negative bias was applied to TiN bottom electrode, but capacitance increased when this bias was positive; these results indicate that electrons are accumulated and depleted at the interface between the ferroelectric layer and IGZO layer, depending on the direction of the polarization in HfZrOx layer.47,48 The accumulation and depletion states in the IGZO layer were maintained without the applied voltage.30 These results confirm the ferroelectric characteristics of HfZrO in the MFS structure.

The electrical characteristics of FeTFT were investigated by applying a gate voltage $\left( V _ { \mathrm { G } } \right)$ sweep to the TiN bottom electrode, while a source-drain voltage $( V _ { \mathrm { D S } } )$ of 1 V was applied. The FeTFT with ferroelectric $\mathrm { H f Z r O } _ { x }$ had n-type transfer characteristics. Forward and reverse transfer-curve sweep evoked typical anticlockwise hysteresis, which arose from ferroelectric polarization switching of the HfZrO (Figure 2a). The hysteresis curve was saturated when $V _ { \mathrm { G } } > 5 ~ \mathrm { V }$ was applied. Conductance modulation under ac operation was also investigated by applying voltage pulses (Figure 2b). Programming pulses (30 ms, 6 V) and erasing pulses (30 ms, −6 V) were applied to the gate electrode, and read voltages $( V _ { \mathrm { G } } , - 1$ V; ${ \tilde { V _ { \mathrm { D S } } } } , { \bar { 1 } } \ \mathrm { V } )$ were used to read its state. The programming pulse increased the conductance G of the channel but the erasing pulse reduced G. The ratio of maximum conductance $G _ { \mathrm { m a x } }$ to minimum conductance $G _ { \mathrm { m i n } }$ of channel was over >40. The origin of G modulation in a FeTFT is polarization switching in the ferroelectric layer. G of the channel can be controlled by the polarization state of the ferroelectric layer.37,49 Therefore, [[multilevel data storage]] can be achieved by inducing continuous ferroelectric domain switching in the HfZrO layer.23,50

The gradual change in polarization state of $\mathrm { H f Z r O } _ { x }$ layer can be possible by controlling the applied voltage (Figure S1a). When a voltage is applied to a ferroelectric layer, the fraction of switched polarization might depend on amplitude of the applied voltage.25,26 The partially switched state can be realized by applying a bias pulse with suitable amplitude. Therefore, the use of an appropriate bias pulse is expected to enable gradual control of the G of the channel, because G is closely related to

the polarization state in ferroelectric layer.25,26,30 To investigate [[multilevel data storage]] properties in FeTFTs, the partial switching of ferroelectric domain was induced by applying different programming voltage pulses and the resulting G of the channel was measured (Figure 3a). First, the erased state was set up by applying a negative bias pulse $\left( 3 0 ~ \mathrm { \ m s } , ~ - 6 ~ \mathrm { \ V } \right)$ to the gate electrode. In this state, the polarization of the $\mathrm { \Pi ~ H f Z r O } _ { x } ^ { \mathrm { \tiny ~ \cdot } }$ layer pointed downward (toward TiN gate electrode), and the channel had low G because electrons were depleted from the interface between the channel and ferroelectric layer by the downward polarization.30 With applying the positive bias pulse to the gate electrode, the polarization began to switch to the upward direction (toward IGZO channel). As the amplitude of positive bias pulse increased, the polarization in the ferroelectric layer changed sequentially from downward to upward. When upward polarization increased, G of the channel increased because electrons could accumulate at the interface region with the upward polarization (Figure 3b).37 Therefore, G of the channel could be delicately modulated by the changing the amplitude of applied bias pulses. Here, four data levels were shown, but it is possible to control levels much more since the polarization reversal can be controlled almost linearly by changing applied bias amplitudes and/or widths.25,37

The retention properties were evaluated by measuring four channel G levels at read voltage $\left( V _ { \mathrm { G } } = - 1 ~ \mathrm { V } \right.$ and ${ \bar { V } } _ { \mathrm { D S } } = { \bar { 1 } } \mathrm { { V } } )$ . FeTFTs based on the ferroelectric $\mathrm { H f Z r O } _ { x }$ and oxide semiconductor showed the stable data storage properties of four channel conductance levels for 104 s (Figure S4). These stable retention characteristics are very promising because previously reported devices, such as organic and inorganic FeTFTs have suffered from poor data retention properties $\left( < 1 0 ^ { 3 } \ s \right)$ due to the depolarization field.39,51,52 The origins of stable retention properties seem to be the MFS structure without interfacial layer and the low permittivity of ${ \mathrm { H f Z r O } } _ { x } . { } ^ { 4 1 , 5 3 }$ These results indicate that the conductance of IGZO channel can be controlled by ferroelectric polarization and that each G level can be maintained stably. These multilevel and retention characteristics imply the suitability of FeTFT as the synaptic device for [[neuromorphic computing]].

For efficient neural network systems utilizing on-chip storage, an artificial synaptic device with analog memory properties is essential. In these neuromorphic systems, artificial synaptic device must have properties, such as linear conductance modulation, $G _ { \mathrm { m a x } } / G _ { \mathrm { m i n } }$ ratio of >10, data levels

![](images/8dea54ebb6b09abe4d904db04c4e5fa62634800d4d01726e5c1cf48674c1990e.jpg)

![](images/5e499aafbc39286fe49ce98ce6e2b18b8d05f72e9239d69d99d44be91b94e0ea.jpg)

![](images/3410ccb19e8c3bff351b8f2facea7703f8612642bc939ff590f041206067979b.jpg)

![](images/f9af7b94ac58d464572d71f6181a3cdebfc152b326475e9c480c181c7ca8591e.jpg)  
Figure 4. (a) Potentiation and depression properties of ferroelectric thin-film transistor with incremental pulse scheme. (b) Schematic illustration of two-layer multilayer perceptron neural network. (c) Simulated pattern recognition accuracy of the two-layer multilayer perceptron neural network based on the ferroelectric [[thin-film transistors]] compared to an ideal neuromorphic device.

![](images/0098ac2f92b6ce0eb7556e75f3f197fddc75cabc1019dd67e8bd07b33b826945.jpg)

![](images/24f37a50e8bd250f178eafdd8818736b83743840e26500b38143e30c7514aa88.jpg)  
Figure 5. (a) Endurance properties of FeTFT. Cycle-to-cycle variations of (b) potentiation and (c) depression operations for 100 cycles.

>32, and low cycle-to-cycle/device-to-device variations.20,21,54 The conductance modulation properties of FeTFTs give them potential as ideal synaptic devices. To investigate the analog conductance modulation properties of FeTFT, multiple bias pulses with incremental amplitude (potentiation, 2.7 to 4.3 V with 25 mV step; depression, −2 to −3.6 V with 25 mV step) and 10 ms width were applied to the gate. After applying each bias pulse, the conductance of device was measured at $V _ { \mathrm { G } }$ of $- 1 \hat { \mathrm { ~ V ~ } }$ and $V _ { \mathrm { D S } }$ of 1 V (Figure S5). The FeTFT exhibits the good potentiation and depression properties, such as 64 level conductance states, good linearity $\left( \tilde { \left( A _ { \mathrm { p } } , - 0 . 8 0 2 8 ; A _ { \mathrm { d } } , - 0 . 6 9 7 9 \right) } \right)$ , and $G _ { \mathrm { m a x } } / G _ { \mathrm { m i n } }$ ratio >10 (Figure 4a). To evaluate linearity of potentiation and depression, the change in G with number of pulses is described $\stackrel { \star } { \operatorname { a s } } ^ { 2 1 , 2 4 }$

$$
G _ {\mathrm {p}} = B \left(1 - e ^ {- P / A _ {\mathrm {p}}}\right) + G _ {\min }
$$

$$
G _ {\mathrm {d}} = - B \left(1 - e ^ {\left(P - P _ {\max }\right) / A _ {\mathrm {d}}}\right) + G _ {\max }
$$

$$
B = \frac {\left(G _ {\max } - G _ {\min }\right)}{\left(1 - e ^ {- P _ {\max } / A _ {\mathrm {p} , \mathrm {d}}}\right)}
$$

where $G _ { \mathfrak { p } }$ is the conductance of potentiation, $G _ { \mathrm { d } }$ is the conductance of depression, $P _ { \mathrm { m a x } }$ is the maximum number of

pulses, and A is the parameter that represents the linearity of potentiation and depression.

An artificial neural network (ANN) was simulated to perform supervised learning on the Modified National Institute of Standard and Technology (MNIST) database.2 For simulation, a two-layer multilayer perceptron (MLP) neural network with 400 input neurons, 100 hidden neurons, and 10 output neurons was utilized (Figure 4b).2,20,24 The MLP algorithm with analog weight update was used in a simulation based on FeTFT conductance modulation properties, such as number of conductance states, linearity, $\hat { G } _ { \mathrm { m a x } } / \hat { G } _ { \mathrm { m i n } } ,$ cycle-tocycle variation, and device-to-device variation. The 400 input neurons correspond to a 20 × 20 MNIST data, and the 10 output neurons correspond to 10 classes of digits (0−9). At each epoch, the ANN was trained on 8000 patterns that had been randomly selected from 60 000 images in a training data set, and the recognition accuracy was tested on a separate set of 10 000 images from the testing data $\mathsf { s e t . } ^ { 2 }$ In the simulations, the NN based on FeTFT was achieved 91.1% accuracy after 125 training epochs, which is comparable to the recognition accuracy of 94.1% obtained by the ideal synapse NN. The high-recognition accuracy is achieved because of the 64-level conductance states, good linearity $\left( A _ { \mathrm { p } } , - 0 . 8 0 2 8 ; A _ { \mathrm { d } } , - 0 . 6 9 7 9 \right)$ , and reasonable $G _ { \mathrm { m a x } } / G _ { \mathrm { m i n } }$ ratio (>10). In addition, the good variation properties of FeTFT would contribute to the high

![](images/39e1aa0dc9c40fc627ebe91e0d54befccff3da88d053efb9d37f75832345df92.jpg)

![](images/186435e376b0e52b1c67a81d99fcdd3c49f61c56edbbe5298462a046525877b4.jpg)

![](images/feb24942a4a8eb981138466cb71211c1343deab51b425d2169a401ec4b825dce.jpg)  
Figure 6. Effects of potentiation and depression characteristics on recognition accuracy. (a) Conductance levels, (b) $G _ { \mathrm { m a x } } / G _ { \mathrm { m i n } }$ ratio, and (c) cycleto-cycle variation.

recognition accuracy. Endurance property was measured up to 100 cycles (12 800 pulse operation) (Figure 5a). During repeated pulse operation, degradation was not serious. Small cycle-to-cycle variation of 2.36% $\left( n = 1 0 0 \mathrm { c y c l e s } \right)$ and deviceto-device variation of 3.93% (n = 40 devices) were obtained (Figures 5b,c, and S6). These parameters affected recognition accuracy (Figure 6). A comparison between previous synaptic devices and FeTFTs is made (Table S1).7,9,13,24 FeTFTs are promising candidates for synaptic devices due to high $G _ { \mathrm { m a x } } /$ $G _ { \mathrm { m i n } }$ ratio, small variation properties, and the number of conductance levels. In particular, FeTFT exhibits good variation properties compared to previously reported synaptic devices based on the resistive switching behavior.7,9,24 When cycle-to-cycle variation of synaptic devices is >3%, the recognition accuracy may be seriously degraded because variation can overwhelm the amount of conductance modulation.21 Neuromorphic devices based on FeTFT have advantages in variation properties because the origin of conductance modulation in FeTFT is obtained by controlling partial polarization switching in ferroelectric layer.24 Thus, the controllability of channel conductance presents opportunities for developing neuromorphic hardware based on ferroelectric analog synaptic transistors.

Conclusions. In summary, we fabricated and demonstrated an analog synaptic device that used the nanoscale ferroelectric material and oxide semiconductor. The conductance of channel was controlled by the polarization of the ferroelectric layer. The potentiation and depression properties in FeTFTs were measured by applying incremental bias pulses. The FeTFT had good weight-update properties, including good linearity, multiple data states, a high $G _ { \mathrm { m a x } } / G _ { \mathrm { m i n } } ,$ and small device variation properties. An artificial neural network simulation using those measured properties showed 91.1% recognition accuracy in recognizing handwritten digits. These results may facilitate the development of the neuromorphic hardware systems based on FeTFTs.

Experimental Section. Fabrication of Devices. In this study, the proposed FeTFT devices have MFS structure with $\mathrm { T i N / H f Z r 0 } _ { x } / \mathrm { \bar { I } G Z O }$ structure (Figure 1a). First, TiN layer was deposited on the $\mathrm { S i O } _ { 2 } / \mathrm { S i }$ substrates using dc sputtering. $\mathrm { H f Z r O } _ { x }$ films were deposited on sputtered $\mathrm { T i N } / \mathrm { S i O } _ { 2 } / \mathrm { S i }$ substrate using atomic layer deposition (ALD) at $2 8 0 ~ ^ { \circ } \mathrm { C } .$ $\mathrm { H f } \big [ \mathrm { N } \big ( \mathrm { C } _ { 2 } \mathrm { H } _ { 5 } \big ) \mathrm { C H } _ { 3 } \big ] .$ 4 (TEMAH), $\mathrm { Z r } \big [ \mathrm { N } \big ( \mathrm { C } _ { 2 } \mathrm { H } _ { 5 } \big ) \mathrm { C H } _ { 3 } \big ] _ { 4 }$ (TEMAZ), and ozone were used as Hf precursor, Zr precursor, and oxygen source, respectively. HfZrO with thickness of about 24 nm was deposited using $\mathrm { H f O } _ { 2 } / \mathrm { Z r O } _ { 2 }$ ALD cycle ratio 1:1. TiN layer was deposited on $\mathrm { H f Z r O } _ { x }$ films as a capping layer, then the device was thermally annealed for 1 min at 400

$^ \circ \mathrm { C }$ under $\Nu _ { 2 }$ gas. TiN capping layer was removed by wet etching. This etching process did not increase the surface roughness (Figure S7). A layer of 10 nm IGZO film was deposited by radio frequency (RF) sputtering using a sputtering target with In/Ga/Zn = 1:1:1 atomic ratio at room temperature. During the sputtering, the RF power was 150 W and working pressure in the chamber was 5 mTorr. Al source/drain electrodes were deposited by e-beam evaporation. The channel width and length were 50 and 300 μm, respectively. Samples were then annealed at 100 °C for 1 h. TiN/HfZrO /TiN and $\mathrm { A l / I G Z O / H f Z r O } _ { x } / \mathrm { T i N }$ device with the capacitor structure were fabricated in the same way and the top electrodes of TiN/HfZrO /TiN and Al/IGZO/HfZrO / TiN device were 350 μm in diameter.

Characterizations. All characteristics of FeTFT were measured under ambient conditions and room temperature. The electrical characteristics were obtained using a semiconductor parameter analyzer (4200a-SCS, KEITHLEY). The thickness of HfZrO was measured by spectroscopic ellipsometer (M-2000, J.A. Woollam). The surface roughness of HfZrOx layer was measured by atomic force microscopy (AFM) (Dimension 3100, VEECO) operated in tapping mode with Si-tip at scan rate of 0.6 Hz. The thickness of IGZO layer was measured by AFM (Dimension 3100, VEECO) operated in tapping mode with Si-tip at scan rate of 0.5 Hz. The polarization−voltage and capacitance−voltage curves were measured using a pulse measurement unit (4225-PMU, KEITHLEY) and an impedance analyzer (4194A, HP), respectively. All simulations were performed in Linux system with GCC, GNU make, CNU C libraries by using $\mathrm { C } { \mathrm { + } } { \mathrm { + } } \mathrm { c o d e } . ^ { 2 0 }$ The simulated MLP neural network consisted of 400 input neurons, 100 hidden neurons, and 10 output neurons. The 400 input neurons corresponded to the 20 × 20 MNIST image, and the 10 output neurons corresponded to 10 classes of digits. $G _ { \mathrm { m a x } } / G _ { \mathrm { m i n } } ,$ linearity, and cycle-to-cycle/device-to-device variations of the FeTFTs were considered as synaptic device characteristics in these simulations. For simulation of an ideal synapse neural network, ideal synaptic properties including perfectly linear conductance modulation with $G _ { \mathrm { m a x } } / G _ { \mathrm { m i n } }$ ratio = 50, and 64 conductance states were used.

# ASSOCIATED CONTENT

# *S Supporting Information

The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acs.nanolett.9b00180.

Polarization−voltage hysteresis and capacitance−voltage characteristic of the $\mathrm { T i N / H f Z r O } _ { x } / \mathrm { T i N }$ structure; polar-

ization−voltage hysteresis of TiN/HfZrO /TiN structure with different device size and remnant polarization of TiN/HfZrO /TiN structure with different device size; the endurance properties of $\mathrm { A l / I G Z O / H f Z r O _ { \it x } / T i N }$ structure over $1 \hat { 0 } ^ { 5 }$ cycles and remnant polarization of $\mathrm { A l / I G Z O / H f Z r O } _ { x } / \mathrm { T i N }$ structure over 105 cycles; retention properties of the ferroelectric thin-film transistor for multilevel state; potentiation and depression pulse schemes applied to gate electrode; device-todevice variation of potentiation and depression operation of 40 different devices; topography image measured by atomic force microscope for HfZrO film before TiN deposition and after TiN etching process (PDF)

# AUTHOR INFORMATION

# Corresponding Author

*E-mail: jangsik@postech.ac.kr (J.-S.L).

# ORCID

Jang-Sik Lee: 0000-0002-1096-1783

# Author Contributions

J.S.L. conceived and directed the research. J.S.L. and M.K.K. designed and planned the experiment. M.K.K. performed the experiment and acquired the data. M.K.K. and J.S.L. wrote the manuscript.

# Notes

The authors declare no competing financial interest.

# ACKNOWLEDGMENTS

This work was supported by the National Research Foundation of Korea (NRF-2016M3D1A1027663 and 2018R1D1A1B07043368). In addition, this work was partially supported by the Brain Korea 21 PLUS project (Center for Creative Industrial Materials).

# REFERENCES

(1) Wang, Z.; Joshi, S.; Savel’ev, S. E.; Jiang, H.; Midya, R.; Lin, P.; Hu, M.; Ge, N.; Strachan, J. P.; Li, Z.; Wu, Q.; Barnell, M.; Li, G.-L.; Xin, H. L.; Williams, R. S.; Xia, Q.; Yang, J. Nat. Mater. 2017, 16, 101−108.   
(2) Choi, S.; Tan, S. H.; Li, Z.; Kim, Y.; Choi, C.; Chen, P.-Y.; Yeon, H.; Yu, S.; Kim, J. Nat. Mater. 2018, 17, 335−340.   
(3) Prezioso, M.; Merrikh-Bayat, F.; Hoskins, B. D.; Adam, G. C.; Likharev, K. K.; Strukov, D. B. Nature 2015, 521, 61−64.   
(4) Liu, C.; Yan, X.; Song, X.; Ding, S.; Zhang, D. W.; Zhou, P. Nat. Nanotechnol. 2018, 13, 404−410.   
(5) Jain, A. K.; Jianchang, M.; Mohiuddin, K. M. Computer 1996, 29, 31−44.   
(6) Hu, M.; Li, H.; Chen, Y.; Wu, Q.; Rose, G. S.; Linderman, R. W. IEEE Transactions on Neural Networks and Learning Systems 2014, 25, 1864−1878.   
(7) Jo, S. H.; Chang, T.; Ebong, I.; Bhadviya, B. B.; Mazumder, P.; Lu, W. Nano Lett. 2010, 10, 1297−1301.   
(8) van de Burgt, Y.; Lubberman, E.; Fuller, E. J.; Keene, S. T.; Faria, G. C.; Agarwal, S.; Marinella, M. J.; Alec Talin, A.; Salleo, A. Nat. Mater. 2017, 16, 414−418.   
(9) Woo, J.; Moon, K.; Song, J.; Lee, S.; Kwak, M.; Park, J.; Hwang, H. IEEE Electron Device Lett. 2016, 37, 994−997.   
(10) Pan, F.; Gao, S.; Chen, C.; Song, C.; Zeng, F. Mater. Sci. Eng., R 2014, 83, 1−59.   
(11) Burr, G. W.; Shelby, R. M.; Sidler, S.; Nolfo, C. d.; Jang, J.; Boybat, I.; Shenoy, R. S.; Narayanan, P.; Virwani, K.; Giacometti, E. U.; Kurdi, B. N.; Hwang, H. IEEE Trans. Electron Devices 2015, 62, 3498−3507.

(12) Fuller, E. J.; Gabaly, F. E.; Leonard, F.; Agarwal, S.; Plimpton,́ S. J.; Jacobs-Gedrim, R. B.; James, C. D.; Marinella, M. J.; Talin, A. A. Adv. Mater. 2017, 29, 1604310.   
(13) Sanchez Esqueda, I.; Yan, X.; Rutherglen, C.; Kane, A.; Cain, T.; Marsh, P.; Liu, Q.; Galatsis, K.; Wang, H.; Zhou, C. ACS Nano 2018, 12, 7352−7361.   
(14) Suri, M.; Bichler, O.; Querlioz, D.; Cueto, O.; Perniola, L.; Sousa, V.; Vuillaume, D.; Gamrat, C.; DeSalvo, B. 2011 IEEE International Electron Devices Meeting (IEDM), Washington, DC, USA, December 5−7, 2011; IEEE: Piscataway, NJ, USA, 2011; pp 4.4.1− 4.4.4.   
(15) Kim, S.; Ishii, M.; Lewis, S.; Perri, T.; BrightSky, M.; Kim, W.; Jordan, R.; Burr, G. W.; Sosa, N.; Ray, A.; Han, J.; Miller, C.; Hosokawa, K.; Lam, C. 2015 IEEE International Electron Devices Meeting (IEDM), Washington, DC, USA, December 7−9, 2015; IEEE: Piscataway, NJ, USA, 2015; pp 17.1.1−17.1.4.   
(16) Sharbati, M. T.; Du, Y.; Torres, J.; Ardolino, N. D.; Yun, M.; Xiong, F. Adv. Mater. 2018, 30, 1802353.   
(17) Yan, X.; Zhao, J.; Liu, S.; Zhou, Z.; Liu, Q.; Chen, J.; Liu, X. Y. Adv. Funct. Mater. 2018, 28, 1705320.   
(18) Yin, J.; Zeng, F.; Wan, Q.; Li, F.; Sun, Y.; Hu, Y.; Liu, J.; Li, G.; Pan, F. Adv. Funct. Mater. 2018, 28, 1706927.   
(19) Wang, I. T.; Chang, C.-C.; Chiu, L.-W.; Chou, T.; Hou, T.-H. Nanotechnology 2016, 27, 365204.   
(20) Chen, P.; Peng, X.; Yu, S. 2017 IEEE International Electron Devices Meeting (IEDM), San Francisco, CA, USA, December 2−6, 2017; IEEE: Piscataway, NJ, USA, 2017; pp 6.1.1−6.1.4.   
(21) Chen, P.-Y.; Peng, X.; Yu, S. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems 2018, 37, 3067−3080.   
(22) Yu, S.; Chen, P.-Y.; Cao, Y.; Xia, L.; Wang, Y.; Wu, H. 2015 IEEE International Electron Devices Meeting (IEDM), Washington, DC, USA, December 7−9, 2015; IEEE: Piscataway, NJ, USA, 2015; pp 17.3. 1−17.3. 4.   
(23) Oh, S.; Kim, T.; Kwak, M.; Song, J.; Woo, J.; Jeon, S.; Yoo, I. K.; Hwang, H. IEEE Electron Device Lett. 2017, 38, 732−735.   
(24) Jerry, M.; Chen, P.; Zhang, J.; Sharma, P.; Ni, K.; Yu, S.; Datta, S. 2017 IEEE International Electron Devices Meeting (IEDM), San Francisco, CA, USA, December 2−6, 2017; IEEE: Piscataway, NJ, USA, 2017; pp 6.2.1−6.2.4.   
(25) Nishitani, Y.; Kaneko, Y.; Ueda, M.; Morie, T.; Fujii, E. J. Appl. Phys. 2012, 111, 124108.   
(26) Nishitani, Y.; et al. Jpn. J. Appl. Phys. 2013, 52, 04CE06.   
(27) Lee, K. H.; Lee, G.; Lee, K.; Oh, M. S.; Im, S.; Yoon, S. M. Adv. Mater. 2009, 21, 4287−4291.   
(28) Hoffman, J.; Pan, X.; Reiner, J. W.; Walker, F. J.; Han, J. P.; Ahn, C. H.; Ma, T. P. Adv. Mater. 2010, 22, 2957−2961.   
(29) Hwang, S. K.; Bae, I.; Kim, R. H.; Park, C. Adv. Mater. 2012, 24, 5910−5914.   
(30) Kaneko, Y., In Ferroelectric-Gate Field Effect Transistor Memories: Device Physics and Applications; Park, B.-E., Ishiwara, H., Okuyama, M., Sakai, S., Yoon, S.-M., Eds.; Springer Netherlands: Dordrecht, 2016; pp 89−109.   
(31) Lee, G. G.; Tokumitsu, E.; Yoon, S. M.; Fujisaki, Y.; Yoon, J. W.; Ishiwara, H. Appl. Phys. Lett. 2011, 99, 012901.   
(32) Ishiwara, H. Jpn. J. Appl. Phys. 1993, 32, 442.   
(33) Horiuchi, T.; et al. Semicond. Sci. Technol. 2009, 24, 105026.   
(34) Fukushima, T.; et al. Jpn. J. Appl. Phys. 2008, 47, 8874.   
(35) McAdams, H. P.; Acklin, R.; Blake, T.; Xiao-Hong, D.; Eliason, J.; Fong, J.; Kraus, W. F.; Liu, D.; Madan, S.; Moise, T.; Natarajan, S.; Ning, Q.; Yunchen, Q.; Remack, K. A.; Rodriguez, J.; Roscher, J.; Seshadri, A.; Summerfelt, S. R. IEEE J. Solid-State Circuits 2004, 39, 667−677.   
(36) Ni, K.; Sharma, P.; Zhang, J.; Jerry, M.; Smith, J. A.; Tapily, K.; Clark, R.; Mahapatra, S.; Datta, S. IEEE Trans. Electron Devices 2018, 65, 2461−2469.   
(37) Kaneko, Y.; Nishitani, Y.; Tanaka, H.; Ueda, M.; Kato, Y.; Tokumitsu, E.; Fujii, E. J. Appl. Phys. 2011, 110, 084106.   
(38) Müller, J.; Yurchuk, E.; Schlösser, T.; Paul, J.; Hoffmann, R.; Müller, S.; Martin, D.; Slesazeck, S.; Polakowski, P.; Sundqvist, J.;

Czernohorsky, M.; Seidel, K.; Kücher, P.; Boschke, R.; Trentzsch, M.; Gebauer, K.; Schröder, U.; Mikolajick, T. 2012 Symposium on VLSI Technology (VLSIT), Honolulu, HI, USA; June 12−14, 2012; IEEE: Piscataway, NJ, USA, 2012; pp 25−26.   
(39) Cheng, C.; Chin, A. IEEE Electron Device Lett. 2014, 35, 138− 140.   
(40) Boescke, T. S.; Muller, J.; Brauhaus, D.; Schroder, U.; Bottger, U. Appl. Phys. Lett. 2011, 99, 102903.   
(41) Mikolajick, T.; Slesazeck, S.; Park, M. H.; Schroeder, U. MRS Bull. 2018, 43, 340−346.   
(42) Kim, S. J.; Mohan, J.; Lee, J.; Lee, J. S.; Lucero, A. T.; Young, C. D.; Colombo, L.; Summerfelt, S. R.; San, T.; Kim, J. Appl. Phys. Lett. 2018, 112, 172902.   
(43) Kim, S. J.; Mohan, J.; Young, C. D.; Colombo, L.; Kim, J.; Summerfelt, S. R.; San, T. 2018 IEEE International Memory Workshop (IMW), Kyoto, Japan; May 13−16, 2018; IEEE: Piscataway, NJ, USA, 2018; pp 1−4.   
(44) Kim, S. J.; Narayan, D.; Lee, J.-G.; Mohan, J.; Lee, J. S.; Lee, J.; Kim, H. S.; Byun, Y.-C.; Lucero, A. T.; Young, C. D.; Summerfelt, S. R.; San, T.; Colombo, L.; Kim, J. Appl. Phys. Lett. 2017, 111, 242901.   
(45) Shiraishi, T.; Katayama, K.; Yokouchi, T.; Shimizu, T.; Oikawa, T.; Sakata, O.; Uchida, H.; Imai, Y.; Kiguchi, T.; Konno, T. J.; Funakubo, H. Appl. Phys. Lett. 2016, 108, 262904.   
(46) Park, M. H.; Kim, H. J.; Kim, Y. J.; Moon, T.; Hwang, C. S. Appl. Phys. Lett. 2014, 104, 072901.   
(47) Choi, W.; Kim, S.; Jin, Y. W.; Lee, S. Y.; Sands, T. D. Appl. Phys. Lett. 2011, 98, 102901.   
(48) Kato, Y.; et al. Jpn. J. Appl. Phys. 2008, 47, 2719.   
(49) Mathews, S.; Ramesh, R.; Venkatesan, T.; Benedetto, J. Science 1997, 276, 238−240.   
(50) Furukawa, T.; Nakajima, T.; Takahashi, Y. IEEE Trans. Dielectr. Electr. Insul. 2006, 13, 1120−1131.   
(51) Yoon, S.-M.; et al. Jpn. J. Appl. Phys. 2010, 49, 04DJ06.   
(52) Yoon, S. M.; Yang, S.; Byun, C.; Park, S. H. K.; Cho, D. H.; Jung, S. W.; Kwon, O. S.; Hwang, C. S. Adv. Funct. Mater. 2010, 20, 921−926.   
(53) Ishiwara, H. Curr. Appl. Phys. 2009, 9, S2−S6.   
(54) Yu, S. Proc. IEEE 2018, 106, 260−285.