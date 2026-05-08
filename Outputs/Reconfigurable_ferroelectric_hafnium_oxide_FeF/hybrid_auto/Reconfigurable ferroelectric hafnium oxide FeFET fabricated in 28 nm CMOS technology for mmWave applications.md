---
title: "Reconfigurable ferroelectric hafnium oxide FeFET fabricated in 28 nm CMOS technology\\"
authors:
  - "Sukhrob Abdulazhanov"
  - "Quang Huy Le"
  - "Dang Khoa Huynh"
  - "Maximilian Lederer"
  - "Yannick Raffel"
  - "Kai Ni"
  - "Xunzhao Yin"
  - "Thomas Kämpfe"
  - "Gerald Gerlach"
date: "2023-01-01"
year: "2023"
journal: "IEEE Electron Device Letters"
abstract: "In this work we introduce reconfigurable multifinger ferroelectric field effect transistors\\"
abstract_cn: "本工作介绍了采用28 nm CMOS技术制造的可重构多指铁电场效应晶体管。通过切换阈值电压，FeFET可用作射频电路的可重构器件，在V_GS = 0下工作，从而降低操作中的能量损耗。器件以共源极配置实现，表现出超过1\\"
keywords:
  - "[[FeFET]]"
  - "[[HfO₂]]"
  - "[[CMOS technology]]"
  - "[[mmWave]]"
cite: "[1] Abdulazhanov S, Le Q H, Huynh D K, et al. Reconfigurable ferroelectric hafnium\\"
aiSum: "28 nm CMOS工艺制造的可重构HfO₂ FeFET，存储窗口>1 V，f_T/f_MAX分别达113/230 GHz，适用于毫米波射频电路。"
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
  - "[[HfO2]]"
---

# Reconfigurable ferroelectric hafnium oxide FeFET fabricated in 28 nm CMOS technology for mmWave applications
  - "[[FeFET]]"

Sukhrob Abdulazhanov∗, Quang Huy Le∗, Dang Khoa Huynh∗, Maximilian Lederer∗, Yannick Raffel ∗, Kai Ni†, Xunzhao Yin ‡ Thomas Kampfe ¨ ∗ and Gerald Gerlach§ ∗Fraunhofer IPMS, Dresden, Germany, E-mail: sukhrob.abdulazhanov@imps.fraunhofer.de †Rochester Institute of Technology, Rochester, USA ‡Zhejiang University, Zhejiang, China

§Dresden University of Technology, Dresden, Germany, E-mail: gerald.gerlach@tu-dresden.de

Abstract—In this work we introduce reconfigurable multifinger ferroelectric field effect transistors (FeFETs) which were fabricated using 28 nm CMOS technology. By switching the threshold voltage, the FeFETs can be utilized as reconfigurable devices for RF circuits, functioning at $\mathbf { V _ { G S } } = \mathbf { 0 } ,$ thereby reducing energy losses during operation. The devices were realized in the common-source configuration and demonstrated a memory window of more than 1 V along with an exceptional performance at mmWave frequencies. For a 32×1 µm device with 80 nm gate length, the transit frequency $\bf ( f _ { T } )$ and maximum oscillation frequency $\bf ( f _ { M A X } )$ were calculated to be 113 GHz and 230 GHz, respectively. These $\mathbf { f } _ { \mathbf { T } } / \mathbf { f } _ { \mathbf { M A X } }$ values are the highest among reconfigurable RF FeFETs.

Index Terms—ferroelectric, $\mathbf { H f } \mathbf { O } _ { 2 } ,$ FeFET, memory window, HVT, LVT, LTP, LTD, load-pull

# I. INTRODUCTION

The growing need for high-speed and energy-efficient data exchange in modern technologies such as 5G, 6G, and IoT has resulted in a demand for transistors that can meet these requirements. As a result, researchers are exploring the use of materials and heterostructures with switchable properties, such as MEMS, phase-change materials, and ferroelectrics. Ferroelectric field-effect transistors (FeFETs) have emerged as a prominent research field in this regard, as they utilize the ferroelectric properties of certain materials to achieve low-power and fast switching. Ongoing research in this area is focused on identifying new ferroelectric materials and device architectures that can further improve the performance of FeFETs. Ferroelectric hafnium oxide $\left( \mathrm { H f O } _ { 2 } \right)$ is one of the most promising materials for FeFETs and has garnered significant attention from multiple research groups since its discovery [1]. Its compatibility with the CMOS fabrication process has made it an ideal candidate for large-scale integration of non-volatile memory devices [2] and neuromorphic networks [3]–[7]. Although ferroelectric $\mathrm { H f O } _ { 2 }$ devices were initially designed to operate at low frequencies, recent developments have seen the proposal and demonstration of ferroelectric HfO varactors for RF [8]–[10] and mmWave [11], [12] implementations up to 110 GHz [13]. However, no $\mathrm { H f O } _ { 2 }$ -based FeFETs

![](images/998ad758b11995328eb2cdb1b830e3eadfd376c0f939d8453c2970a2381d5455.jpg)  
(a)

![](images/e204124e42f5e4c6cd3b0ca9935e87916de7ab0aa2f7d5c2f1c9bfa073cf1a41.jpg)  
(c)

![](images/0f37ef5f6284711f8bd558b5496a7270eb7dd937e0eb4129d3744ed8ca96a2df.jpg)  
(b)

![](images/f5d0ba2533c4c01386923b15552121bc31362a328d81bb1814332a40e327c5aa.jpg)  
(d)   
Fig. 1: TEM image (a) and cross-section schematics (b) of a multifinger FeFET in common-source configuration (c) based on Si-doped $\mathrm { H f O } _ { 2 } .$ . The on-wafer measurements were done using OPEN-SHORT de-embedding technique with DUT reference plane in a vicinity of the FeFET (d).

with a Si channel that operate at mmWave frequencies have been demonstrated to date. While most reported RF active switchable devices are high electron mobility transistors (HEMTs) [14] based on III-V semiconductors with integrated ferroelectrics for threshold voltage $\left( \mathrm { V } _ { \mathrm { t } } \right)$ tuning. Unlike HEMTs, Si-channel FeFETs exhibit a symmetric hysteretic behavior around $\mathrm { V _ { G S } = 0 } .$ , making them well-suited for low-power switches. Additionally, the thick gate oxide of FeFETs can provide further advantages in high-power applications.

Possible system implementations stretch from frequency-multiplexed computing (FMC) [15], [16] - a cutting-edge technique in neuromorphic design, to low-power switching matrices for reconfigurable circuits and systems. Furthermore, a post-fabrication adaptation for mismatch control is possible by long-term depression and retention of the stored $\mathrm { V _ { T } }$ state of the FeFET, as

previously shown for double-gate devices in fully-depleted silicon-on-insulator.

In this paper, we present a first realization of Si-channel RF FeFETs, based on $\mathrm { H f O } _ { 2 }$ fabricated in 28 nm CMOS technology in the common-source configuration.

# II. FABRICATION AND EXPERIMENTAL SETUP

The FeFETs were designed and fabricated in 28 nm CMOS. The standard gate oxide is substituted with ferroelectric $\mathrm { H f O } _ { 2 }$ as illustrated in Figure 1(a). The multifinger architecture [Fig.1(b)] was chosen similarly to conventional RF FETs to decrease the channel resistance and transmission losses. The FeFETs were realized in a common-source configuration [Fig.1(c)]. The test structures used in this work consist of 80 nm gate-length FeFETs with 16 and 32 fingers. The gate widths available for the study are 1 µm and 3 µm.

Multi-bias two-port S-parameters were measured from 10 MHz to 67 GHz for the high-frequency characterization of the FeFETs upon gate voltage sweep between -5 V and 5 V. The measured S-parameters were deembedded to M1 plane using Open-Short technique [17]. DC and RF measurements were carried out using a Keysight N5247B PNA-X vector network analyzer. Ground-Signal-Ground Infinity probes with a pitch of 50 µm were used for the measurement, while an SMU B2902A and a bias tee were employed to apply DC bias to the DUT. A vector-receiver load-pull measurement system was utilized for the non-50-Ohm large-signal characterization [18]. The system consists mainly of a Keysight PNA-X N5247B vector network analyzer (VNA) and Maury MT985AL impedances tuners. In addition, nonlinear VNA measurement (NVNA) was applied to extract the harmonic components.

# III. RESULTS AND DISCUSSION

In Fig.2(a) the transfer characteristics are presented. When comparing the memory window (MW) of the different device configurations, similar values (≈1V) are observed. Larger devices exhibit higher drain currents. In all cases, the threshold voltage $( \mathrm { V _ { T } } )$ of the program (PG) state is found to be below $0 \ \mathrm { V } ,$ while the erase (ER) state is situated near 0 V. Fig.2(b) depicts the source-drain conductance, which reveals that it rises with both the gate width and the number of fingers.

Comparing the cycle endurance [Fig.3(a)], a pronounced walk-out of both states towards higher $\mathrm { V _ { T } }$ states is observed for the device with 16 fingers, whereas in the case of the device with 32 fingers, a walk-out towards higher $\mathrm { V _ { T } }$ is only observed for the ER state after $1 0 ^ { 4 }$ cycles. However, an increase in MW is observed initially, which could be related to the wake-up effect in hafnium oxide based ferroelectrics. Retention results [Fig.3(b)] indicate a stable memory window. In case of the 16-finger device, minor de-trapping is initially observable and $\mathrm { V _ { T } }$ states do not shift afterwards over the measured time period. In case of the 32-finger device, continuous shifting to higher $\mathrm { V _ { T } }$ values is

observed, but stable state separation is preserved. This hints to a de-trapping of holes, or trapping of electrons over time. As this is a major difference to the 16 finger device, the physical origin is most likely related to the device layout.

![](images/e7456bd3c6d507bd4c8eb03cbc0922ac8c87d0ec7fd60ce5f5ebde834f29bc70.jpg)

![](images/a7432f3a4cd6681ee91f232f14cdddf4dec4730847a4a864fc6462cb66a4a4a0.jpg)  
Fig. 2: Transfer characteristics conductance (b) of FeFETs configurations.   
(a) and source-drain with different finger

![](images/fa71c9fabf0a6ac5fbda9471e869f1f0b2666bfff14577e08c9917126b9a5e4b.jpg)

![](images/1abaf5e11c20004a75a83b9da47d4c757709ae74b3d165eed7207d5edf49e142.jpg)

![](images/60ea9fcee766519d23b9e0f96445358ee90df313edb7ae24d71d8f5fb303d64a.jpg)

![](images/aa2564d389772075587ccc2762e6831b8a036d1b5a5a5172906f4ee0d00de343.jpg)

![](images/46f1b4d7c91504d7b4e8aeb276a7c549241874a3f4bea06ca0a7cbfe947b47a7.jpg)  
Fig. 3: Endurance (a), retention (b), and long-term potentiation (LTP) and depression (LTD) (c) of 16×1 µm and 32×3 µm FeFETs with 80 nm channel length.

For the application as synaptic device in neuromorphic circuits, long-term potentiation (LTP) and depression (LTD) characteristics were explored [Fig.3(c)]. Here linear behavior is observed for both device configurations. Comparing the two, it becomes apparent that the potentiation curve for the 32-finger device deviates from linear behavior initially and saturates for higher number of pulses. Hereby, potentiation

![](images/1e52e5e2b5ef4319225335825bdcbab19f938a902627bb53f4c06c5ea2ad4e93.jpg)

![](images/c2b0b705c597247957330bbf22c65fbb2c8dccd21d14c7167c65837f7073d66b.jpg)

![](images/c2fe1cd6e330ffeac3b9655643c25306a60f0a4e1713d03beb3aa58c1591c78a.jpg)

![](images/539de9129c0476d4014ed2cec7ce4309d61c0cfe5e1e5be20de6bcbc0eed0871.jpg)  
Fig. 4: Transit frequency (fT) and maximum oscillation frequency $\operatorname { \left( f _ { M A X } \right) }$ of 16-finger (a) and 32-finger (b) devices, respectively, with 1 µm and 3 µm gate widths; the 16×1 µm device has demonstrated stable broadband variation of $\mathbf { S } _ { 2 1 }$ upon long-term potentiation (LTP) (c) and depression (LTD) (d).

can address less separated states than depression. The S-parameters measured during RF characterization were used to calculate the transit frequency $\left( \mathrm { f _ { T } } \right)$ and the maximum oscillation frequency $\operatorname { \left( f _ { M A X } \right) }$ , as outlined in [19]. The $\mathrm { f _ { T } }$ [Fig.4(a)] of 32-finger devices shows higher values than of the 16-finger ones, with a maximum of 113 GHz. The same trend is observed for $\mathrm { f _ { M A X } }$ [Fig.4(b)] that reaches the maximum value of 230 GHz for 32-finger device with 1 µm gate width. Similarly to Fig.3(c), the LTP [Fig.4(c)] and LTD [Fig.4(d)] measurements were performed on the 16-finger device with w=1 µm. Instead of measuring current, the analysis focused on the variation of the $\mathbf { S } _ { 2 1 }$ parameter at different $\mathrm { v _ { G S } }$ values. The results demonstrated a consistent shift across the entire frequency range, indicating the essential stability required for multilevel programming.

In Fig.5, the results of a large-signal FeFET performance, evaluated through vector-receiver load-pull measurement, are demonstrated, where the output impedance was optimized for a maximum power output [Fig.5(d) inset]. Devices with 16×1 µm and 32×3 µm dimensions, with pre-programmed HVT and LVT states, were analyzed at VGS = 0 V, 0.5 V and 1 V. In Fig.5(a),(b), the power sweep measurement results are presented, where the output power $\mathrm { ( P _ { o u t } ) }$ increases significantly (> 15 dBm) upon the transition from HVT [Fig.5(a)] to LVT [Fig.5(b)] state. We have furthermore investigated the harmonic distortion characteristics of the device. We extracted the load-pull power sweep up to $4 ^ { \mathrm { t h } }$ harmonic at the reference frequency of 10 GHz [Fig.6]. We observe a decrease in linearity from HVT to LVT at constant zero read bias $\mathrm { V } _ { \mathrm { G S } } = 0 \mathrm { V } ,$ as expected. Nevertheless, the higher-order harmonics are still separated from fundamental in LVT by more than 20 dBm

![](images/0e2e182e78134082f76a9bdc3708beb1feeeb4d8ecef5d489ab1f6f7a3b3b38a.jpg)

![](images/115adbe26cbd33d78c9c5de56fb909d187ee5b08fbc1b21978e85d57b83b6c4a.jpg)

![](images/c464b2b9b5290e32377eb9c8d4ff82bfadbd6f2c6ecd1c7375fd926fdf34d4cd.jpg)

![](images/e5a9f14304f853aae09322a5e049d3f88f3395d7ef717815b54b0fe13a0e5d92.jpg)  
Fig. 5: Power sweep measurement at 10 GHz for 16×1 µm (a),(b) and 32×3 µm (c),(d) devices with 80 nm channel length at HVT(a),(c) and LVT (b),(d) states, respectively, extracted during load-pull analysis at optimal impedance (see inset) at $\mathrm { V _ { G S } = 0 }$ V, 0.5 V, and 1 V.

![](images/38fd52017c39ebdf2e929c3bd7345fa4be7d1cefa5bce04e1c4ee3ddc11141ac.jpg)

![](images/4a4314bed372083497b75ce787cb6ad97696bcbb57e88539fb0c2343ea79e236.jpg)

![](images/ea1e64232aad24310ea1ebc3d693e84ec19efaf8893fc34fe9742a57d4afbfbc.jpg)

![](images/9ac6e04a23f4225feb0b59f0f63dc40661f5e304cec38c2fdbd3f6058a4714c5.jpg)  
Fig. 6: Power-sweep measurement of higher harmonics at 10 GHz, $\mathrm { V _ { G S } = 0 ~ V , }$ for 16×1 µm (a),(b) and 32×3 µm (c),(d) devices at HVT (a),(c) and LVT (b),(d) states, respectively.

[Fig.6(b)] and 16 dBm [Fig.6(d)] at 0 dBm input power for 16×1 µm and 32×3 µm devices, respectively.

In Fig.7, the plot illustrates the relationship between transducer gain and input power. Upon HVT to LVT switching at the input power $( \mathrm { P _ { i n } } )$ range between -30 dBm—15 dBm, the 16-finger device shows transducer gain variation (∆Gt) of 17 dB and 22 dB at $\mathrm { V _ { G S } = 0 V }$ and $\mathrm { V } _ { \mathrm { G S } } { = } 0 . 5 \mathrm { V } ,$ respectively [Fig.7(a)]. For 32-finger device its maximum variation is 16 dB at $\mathrm { V _ { g } } = 0 \mathrm { ~ V ~ }$ [Fig.7(b)]. At $\mathrm { P _ { i n } } { > } { - } 1 5$ dBm, transducer gain variation decreases. The

![](images/f5ea4c1337d43586226fe8d0b52337a92e556f8e7543fe226e9af647ea5dd971.jpg)  
Fig. 7: Transducer gain variation upon different $\mathrm { v _ { G S } }$ during the transition between HVT and LVT states at 10 GHz for 16×1 µm (a) and 32×3 µm (b) devices with 80 nm channel length.

32-finger device has the gain of 7 dB at $\mathrm { V _ { G S } = 0 }$ V, which can be implementented to compensate losses in future reconfigurable systems.

# IV. CONCLUSION

In this paper we introduced a new type of reconfigurable multifinger silicon-channel ferroelectric field-effect transistors (FeFETs) that utilize ferroelectric HfO2 and are optimized for mmWave applications. The FeFETs come in different finger numbers and dimensions and are fabricated using the 28 nm CMOS technology. The devices demonstrate excellent RF capabilities with highest reported $\mathrm { f _ { T } / f _ { M A X } }$ of 113 GHz/230 GHz and non-volatile transducer gain modulation of $\Delta \mathrm { G } _ { \mathrm { t } } = 2 2 ~ \mathrm { d B }$ at $\mathrm { V } _ { \mathrm { G S } } { = } 0 . 5 \mathrm { V } .$ The results presented here showcase FeFETs based on ferroelectric $\mathrm { H f O } _ { 2 }$ as new types of transistors with the potential to improve device architectures by eliminating traditional boundaries between memory, logic, and communication devices.

# V. ACKNOWLEDGMENT

This work has received funding from the ECSEL Joint Undertaking (JU) under grant agreement No 783127. The JU receives support from the European Union’s Horizon 2020 research and innovation programme and France, Germany, Austria, Poland, Portugal, Spain.

# REFERENCES

[1] T. S. Boscke, J. M ¨ uller, D. Br ¨ auhaus, U. Schr ¨ oder, and U. B ¨ ottger, ¨ “Ferroelectricity in hafnium oxide thin films,” Applied Physics Letters, vol. 99, no. 10, p. 102903, 2011.   
[2] J. Muller, P. Polakowski, S. Mueller, and T. Mikolajick, “Ferroelectric¨ Hafnium Oxide Based Materials and Devices: Assessment of Current Status and Future Prospects,” ECS Journal of Solid State Science and Technology, vol. 4, no. 5, pp. N30–N35, 2015.   
[3] M. Jerry, P.-Y. Chen, J. Zhang, P. Sharma, K. Ni, S. Yu, and S. Datta, “Ferroelectric FET analog synapse for acceleration of deep neural network training,” in 2017 IEEE International Electron Devices Meeting (IEDM). IEEE, 2017, pp. 6.2.1–6.2.4.

[4] M. Lederer, T. Kampfe, T. Ali, F. M ¨ uller, R. Olivo, R. Hoffmann, ¨ N. Laleni, and K. Seidel, “Ferroelectric Field Effect Transistors as a Synapse for Neuromorphic Application,” IEEE Transactions on Electron Devices, vol. 68, no. 5, pp. 2295–2300, 2021.   
[5] S. De, F. Muller, S. Thunder, S. Abdulazhanov, N. Laleni, M. Lederer, ¨ T. Ali, Y. Raffel, S. Dunkel, S. Mojumder, A. Vardar, S. Beyer, K. Seidel, and T. Kampfe, “28 nm HKMG-Based Current Limited FeFET Crossbar-Array for Inference Application,” IEEE Transactions on Electron Devices, pp. 1–5, 2022.   
[6] S. De, F. Muller, N. Laleni, M. Lederer, Y. Raffel, S. Mojumder,¨ A. Vardar, S. Abdulazhanov, T. Ali, S. Dunkel, S. Beyer, K. Seidel, and T. Kampfe, “Demonstration of Multiply-Accumulate Operation with 28 nm FeFET Crossbar Array,” IEEE Electron Device Letters, p. 1, 2022.   
[7] S. De, M. A. Baig, B.-H. Qiu, F. Muller, H.-H. Le, M. Lederer,¨ T. Kampfe, T. Ali, P.-J. Sung, C.-J. Su, Y.-J. Lee, and D. D. ¨ Lu, “Random and Systematic Variation in Nanoscale Hf0.5Zr0.5O2 Ferroelectric FinFETs: Physical Origin and Neuromorphic Circuit Implications,” Frontiers in Nanotechnology, vol. 3, 2022.   
[8] M. Dragoman, M. Aldrigo, M. Modreanu, and D. Dragoman, “Extraordinary tunability of high-frequency devices using Hf0.3Zr0.7O2 ferroelectric at very low applied voltages,” Appl. Phys. Lett., vol. 110, no. 10, p. 103104, 2017.   
[9] M. Dragoman, M. Modreanu, I. Povey, S. Iordanescu, M. Aldrigo, A. Dinescu, D. Vasilache, and C. Romanitan, “2.55 GHz miniaturised phased antenna array based on 7 nm-thick HfxZr1-xO2 ferroelectrics,” Electron. Lett., vol. 54, no. 8, pp. 469–470, 2018.   
[10] S. Abdulazhanov, Q. H. Le, D. K. Huynh, D. Wang, M. Lederer, R. Olivo, K. Mertens, J. Emara, T. Kampfe, and G. Gerlach, ¨ “RF-Characterization of HZO Thin Film Varactors,” Crystals, vol. 11, no. 8, p. 980, 2021.   
[11] S. Abdulazhanov, D. K. Huynh, Q. H. Le, D. Lehninger, T. Kampfe, and G. Gerlach, “BEoL integrated hafnium zirconium oxide varactors for tunable mmWave applications,” in ESSDERC 2022 - IEEE 52nd European Solid-State Device Research Conference (ESSDERC). IEEE, 2022, pp. 253–256.   
[12] S. Abdulazhanov, Q. H. Le, D. K. Huynh, D. Wang, D. Lehninger, T. Kampfe, and G. Gerlach, “THz Thin Film Varactor Based on ¨ Integrated Ferroelectric HfZrO2,” ACS Applied Electronic Materials, 2022.   
[13] S. Abdulazhanov, D. K. Huynh, Q. H. Le, D. Lehninger, T. Kampfe, and G. Gedach, “Investigation of BEoL integrated ferroelectric thin-film HfO 2 for mmWave varactor applications,” in 2022 IEEE International Symposium on Radio-Frequency Integration Technology (RFIT). IEEE, 2022, pp. 131–133.   
[14] J. Y. Yang, M. J. Yeom, J. Lee, K. Lee, C. Park, J. Heo, and G. Yoo, “Reconfigurable Radio–Frequency High–Electron Mobility Transistors via Ferroelectric–Based Gallium Nitride Heterostructure,” Advanced Electronic Materials, vol. 8, no. 9, p. 2101406, 2022.   
[15] J. Feldmann, N. Youngblood, M. Karpov, H. Gehring, X. Li, M. Stappers, M. Le Gallo, X. Fu, A. Lukashchuk, A. S. Raja, J. Liu, C. D. Wright, A. Sebastian, T. J. Kippenberg, W. H. P. Pernice, and H. Bhaskaran, “Parallel convolutional processing using an integrated photonic tensor core,” Nature, vol. 589, no. 7840, pp. 52–58, 2021.   
[16] C. Wang, S.-J. Liang, C.-Y. Wang, Z.-Z. Yang, Y. Ge, C. Pan, X. Shen, W. Wei, Y. Zhao, Z. Zhang, B. Cheng, C. Zhang, and F. Miao, “Scalable massively parallel computing using continuous-time data representation in nanoscale crossbar array,” Nature nanotechnology, vol. 16, no. 10, pp. 1079–1085, 2021.   
[17] E. Lourandakis, On-wafer microwave measurements and de-embedding, ser. Microwave design. Boston and London: Artech House, 2016.   
[18] Q. H. Le, D. K. Huynh, D. Wang, T. Kampfe, Z. Zhao, and S. Lehmann, “Assessment of a Thick-Oxide Transistor from the 22FDX Platform for 5G NR sub-6 GHz FEMs,” in 2019 IEEE 2nd 5G World Forum (5GWF). IEEE, 2019, pp. 7–10.   
[19] I. J. Bahl, Fundamentals of RF and microwave transistor amplifiers. Oxford: Wiley, 2009.