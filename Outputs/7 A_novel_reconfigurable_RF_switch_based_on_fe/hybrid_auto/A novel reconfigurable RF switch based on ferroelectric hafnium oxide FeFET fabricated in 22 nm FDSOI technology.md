---


title: "A novel reconfigurable RF switch based on ferroelectric hafnium oxide FeFET"
authors:
  - "Sukhrob Dang"
  - "Khoa Quang"
  - "Huy Thomas"
  - "Gerald"
date: "2023-01-01"
year: 2023
journal: "Neuromorphic Computing and Engineering"
abstract: "— This paper presents a novel type of ferroelectric field effect transistor"
abstract_cn: "本文针对铁电器件等领域展开研究，提出了创新的解决方案，通过实验验证了方法的有效性，为相关领域的发展提供了新的思路。"
cite: "[1] Sukhrob A., Dang K.H., Quang H.L., 等. A novel reconfigurable RF switch"
aiSum: "一句话总结：本文针对铁电存储器领域，提出了创新的解决方案，实验验证了方法的有效性。"
confidence: medium
wiki_concepts:
  - "[[FeFET]]"
  - "[[HfO2]]"
keywords:
  - "[[— ferroelectric]]"
  - "[[HfO₂]]"
  - "[[FeFET]]"
  - "[[memory window]]"
  - "[[FDSOI]]"
---

Sukhrob Abdulazhanov1 , Dang Khoa Huynh1 , Quang Huy Le1 , Thomas Kämpfe1 , Gerald Gerlach2

1 Fraunhofer IPMS, Germany

2 TU Dresden, Germany

sukhrob.abdulazhanov@ipms.fraunhofer.de, gerald.gerlach@tu-dresden.de

Abstract — This paper presents a novel type of ferroelectric field effect transistor ([[FeFET]]) - based RF switch with multiple finger structure fabricated in 22 nm [[FDSOI]] technology. The ability to adjust the threshold voltage non-volatile allows for a novel switch concept. The [[FeFET]] can operate at $\mathbf { V _ { G S } } = \mathbf { 0 } ,$ which reduces the necessity of bias-tee configurations in the signal path. It combines the advantages of passive and active RF switches with low loss and low distortion. The devices were implemented in the common-source configuration and demonstrate a large [[memory window]] exceeding 2 V, as well as exceptional performance at mmWave frequencies. We determined a transit frequency (fT) and maximum oscillation frequency (fMAX) of 135 GHz and 139 GHz, respectively for a device with 16 fingers, 20 nm gate length, and 1 µm gate width.

Keywords [[— ferroelectric]], [[HfO₂]], [[FeFET]], [[memory window]], HVT, LVT, [[FDSOI]]

# I. INTRODUCTION

Nowadays, due to the increasing amount and speed of data exchange, there is a high demand to find energy-efficient and fast switching transistors, that can be adapted to advanced technologies such as 5G, 6G or the Internet of Things (IoT). In this regard, scientists are constantly trying to make use of materials and heterostructures with switchable properties, like MEMS, phase-change materials, or ferroelectrics. As an example of the latter, ferroelectric field effect transistors ([[FeFET]]s) have become a well-established research field. One of the best representatives of materials for [[FeFET]]s, is ferroelectric hafnium oxide ([[HfO₂]]), which from the day of its discovery [1] remains steadily in the spotlight of multiple research groups. Due to its perfect compatibility to the CMOS fabrication standards, it leads the way towards large scale integration of non-volatile memory devices [2] and [[neuromorphic]] networks [3]–[7]. Initially, the devices based on ferroelectric [[HfO₂]] were designed to operate predominantly at DC or at low frequencies of several kHz. More recently, devices based on ferroelectric HfO varactors for the RF [8]–[10] and mmWave [11], [12] implementations up to 110 GHz [13] were proposed and demonstrated. However, no $_ { \mathrm { H f O } _ { 2 } - \mathrm { b a s e d } }$ [[FeFET]]s with a Si channel, operating at mmWave frequencies have been demonstrated so far. The majority of reported RF active non-volatile ferroelectric switches are based on high electron mobility transistors (HEMTs) [14], [21] with on III-V channels. However, these

![](images/1ccc5d31ccf3692294df0eb7291730ae7aec9444c00d6c8355ca8f7a66a9f5c8.jpg)  
(a)

![](images/37727db5ed99353efed1eeb9bbda1f7bb73c46db2fea870ac85d62a52b166c72.jpg)  
(b)

![](images/8cdd67e251bc6ee0f6fc9cd63b68f0a3b969e7ff424f45a0e428cce2582339e5.jpg)  
(c)

![](images/4bdbc711a0ba107739dd90ecc40e2a168ea4f65322d4950d2eabce1db4c10091.jpg)  
(d)   
Fig. 1. Cross-section schematics of a single gate (a) and multiple gates (b), the layout (c) and the microscopy image (d) of the multifinger [[FeFET]] in common-source configuration including OPEN and SHORT de-embedding structures.

realizations show very low threshold voltages with small hysteresis. Possible application of such non-volatile mmWave switches are low-power reconfigurable RF/mmWave circuits as frequency-multiplexed computing (FMC) [15], [16] which is one of the latest approaches in neuromorphic architectures.

In this paper we demonstrate the first realization of a multifinger [[FeFET]] for mmWave applications, fabricated in 22 nm [[FDSOI]] technology platform with a large [[memory window]] and centered threshold voltage levels.

# II. FABRICATION AND EXPERIMENTAL SETUP

The general fabrication procedure is a replacement of the standard gate oxide with 10 nm $\mathrm { H f O } _ { 2 } ,$ see Fig. 1(a). To decrease channel resistance and transmission losses, a multifinger architecture [Fig.1(b)] was used, with 16 fingers and a gate width of 1 µm. The gate length was varied between 20 nm, 80 nm, and 200 nm. The test structures, which included OPEN and SHORT de-embedding structures [17] [Fig.1(d)], were designed in a common-source configuration [Fig.1(b),(c)], and the reference plane was brought to the 1st metal layer. DC and RF measurements were conducted using

a Keysight N5247B PNA-X vector network analyzer with N5293A extender heads, applying a signal in the frequency range between 1 GHz and 110 GHz. The pads were contacted using 50 µm pitch Ground-Signal-Ground Infinity probes and the DC bias was applied to the RF signal using an SMU B2902A and a bias tee integrated into the extenders.

Ferroelectric switching is indicated by the shift of threshold voltage $\mathrm { ( V _ { t } ) }$ between high- $\mathbf { \nabla } \cdot \mathrm { V _ { t } }$ (HVT) and low- $\mathbf { - V _ { t } }$ (LVT) or erase (ERS) and program (PRG) states. The switching was accomplished by gradually sweeping $\mathrm { v _ { G S } }$ between -4 V and 4 V while $\mathrm { \Delta V _ { D S } }$ was varied between 0 and 1.2 V.

# III. RESULTS AND DISCUSSION

Fig. 2 shows the transfer characteristics $\left( \mathrm { I } _ { \mathrm { D S } } \mathrm { - } \mathrm { V } _ { \mathrm { G S } } \right)$ at different $\mathrm { \Delta V _ { D S } }$ for devices with varying channel lengths. The IDS-VGS characteristics exhibit a clear counter-clockwise hysteresis behavior with the [[memory window]] (MW) defined as the difference between threshold voltages at HVT and LVT states. The $\mathrm { V _ { t } }$ is defined at $\mathrm { I _ { D S } = 2 0 \mu A }$ . As seen, the device with a gate length of 20 nm exhibits the highest MW of 2.25 V. The threshold voltages of both HVT and LVT states shift towards higher values with an increase in the gate length. The $\mathrm { V _ { t } }$ of HVT is below 0 V in all cases, while in LVT, the $\mathrm { V _ { t } }$ is close to 0 V for $1 = 2 0$ nm and is higher than 0 V for 80 nm and 200 nm devices. The $\mathrm { I _ { O N } / I _ { O F F } }$ ratio at $\mathrm { V _ { G S } } { = } 0 \ \mathrm { V }$ and $\mathrm { V _ { D S } } = 1 . 2 \ : \mathrm { V }$ is 50, 500, and 800 for $1 = 2 0$ nm, 80 nm, and 200 nm, respectively. In all cases, the bending of subthreshold characteristics is visible. This could be attributed to the re-switching of ferroelectric domains during the gradual voltage sweep.

![](images/cd1361785925dd1c174f79fcfa9ae98c1492fb53d725aa5218d20e2d83c920c1.jpg)  
Fig. 2. Transfer characteristics of multifinger [[FeFET]]s with 20 nm (a), 80 nm (b) and 200 nm (c) finger length, respectively.

Fig. 3 displays the output curves $\left( \mathrm { { I } _ { D S } - V _ { D S } } \right)$ of the devices, which were measured while sweeping the gate voltage $\mathrm { v _ { G S } }$ from -2 V to 4 V with a 1 V step. Both high- $\cdot \mathrm { V _ { t } }$ (HVT) and low-V (LVT) states are plotted to demonstrate the mismatch of I due to switching. As expected, the saturation current decreases with increasing gate length due to an increase in channel resistance. Notably, at $\mathrm { V } _ { \mathrm { G S } } = 4 \ \mathrm { V } ,$ the device with a gate length of 20 nm exhibits channel modulation [Fig.3(a)], which is evidenced by an increase in the slope in saturation.

The S-parameter data was used to calculate the maximum available gain (MAG), the transit frequency (fT), and the maximum oscillation frequency $\operatorname { \left( f _ { M A X } \right) }$ [18]. The MAG is plotted as a function of frequency in Fig. 4. From the plots, it is evident that MAG is decreasing with an increase in the gate

![](images/da3e3ab54c66862d281eb90d5c270b4d86e2f2e72cb7ac39c78158a6b346848f.jpg)  
Fig. 3. The output curves of multifinger [[FeFET]]s with 20 nm (a), 80 nm (b), and 200 nm (c) finger length, respectively.

length. The overall frequency response of the MAG is similar to conventional [[FDSOI]] devices [19], [20].

![](images/5a8bd78594313ab718dfe880719c71fa0dc54190a6b4fcad4799d8f115cf1f6a.jpg)  
Fig. 4. Maximum available gain (MAG) vs. frequency (log. scale) of the [[FeFET]]s with 20 nm , 80 nm and 200 nm gate lengths, respectively.

The $\mathrm { f _ { T } }$ plot vs. $\mathrm { v _ { G S } }$ [Fig.5] shows a hysteretic behavior, which confirms the device switchability. The maximum $\mathrm { f _ { T } }$ reaches 135 GHz, 74 GHz and 31 GHz for 20 nm, 80 nm and 200 nm devices, respectively.

![](images/6072587048d729a8625cda942676c2b861043bbd29534201ec0edc5d11dee85a.jpg)  
Fig. 5. Transit frequency vs. VGS of the [[FeFET]]s with 20 nm (a), 80 nm (b) and 200 nm (c) gate lengths, respectively measured at different $\mathrm { \Delta V _ { D S } }$ .

Maximum oscillation frequency similarly shows the hysteretic behavior, reaching maximum values of 139 GHz, 126 GHz and 70 GHz for 20 nm, 80 nm and 200 nm devices, respectively.

In Fig.7 the performance of the devices is compared to the state-of-the-art HEMTs [14], [21]–[24]. In Fig.7(a) the

![](images/b6db882e885e9f4be3068d4c292c1ec65f9bd9640e2ee5062a79958ad1030f69.jpg)  
Fig. 6. Maximum oscillation frequency vs. $\mathrm { v _ { G S } }$ of the [[FeFET]]s with 20 nm (a), 80 nm (b) and 200 nm (c) gate lengths, respectively measured at different $\mathrm { \Delta V _ { D S } }$ .

maximum channel current, normalized to the gate width is plotted versus gate length. As can be seen, because of the multi-finger structure, the total gate current is much higher than that of conventional HEMTs. In Fig.7(b) the $\mathrm { f _ { M A X } }$ is plotted versus $\mathrm { f _ { T } }$ . When compared with the state-of-the-art devices, the $\mathrm { H f O } _ { 2 }$ [[FeFET]] with 20 nm gate length shows the highest $\mathrm { f _ { M A X } \times f _ { T } }$ product.

![](images/16b6dac02450304929b6dc2171ab79544cb9fec8543b21fcab0d8205748a729c.jpg)

![](images/21ee4fe3e66b3ca910b7879761d66f24d332a072837da1e7a02fd10899eebca8.jpg)  
Fig. 7. Maximum I vs. gate length (a) and $\operatorname { f } _ { \mathrm { M A X } }$ vs. f (b) of the [[FeFET]]s compared to the state-of-the-art devices.

# IV. CONCLUSION

In this paper we have demonstrated reconfigurable multifinger [[FeFET]]s with various gate lengths for mmWave implementations, fabricated in 22 nm [[FDSOI]] technology. The device with 20 nm gate length has demonstrated a broad [[memory window]] of 2.3 V, maximum drain current of 12 A/mm, which is higher than state-of-the-art HEMTs. The [[FeFET]]s have also shown an outstanding mmWave performance, manifested in $\mathrm { f _ { T } / f _ { M A X } }$ of 139/135 GHz, 126/74 GHz and 70/31 GHz, respectively. All devices have shown good broadband switching at $\mathrm { v _ { G S } } = 0 .$ , which makes them available for low-power performance. Given the exceptional RF properties, the [[FeFET]]s are the perfect candidates for emerging frequency-multiplexed neuromorphic applications and switchable RF devices.

# ACKNOWLEDGMENT

This work has received funding from the ECSEL Joint Undertaking (JU) under grant agreement No 783127. The JU receives support from the European Union’s Horizon 2020 research and innovation programme and France, Germany, Austria, Poland, Portugal, Spain.

# REFERENCES

[1] T. S. Böscke, J. Müller, D. Bräuhaus, U. Schröder, and U. Böttger, “Ferroelectricity in hafnium oxide thin films,” Applied Physics Letters, vol. 99, no. 10, p. 102903, 2011.   
[2] J. Müller, P. Polakowski, S. Mueller, and T. Mikolajick, “Ferroelectric Hafnium Oxide Based Materials and Devices: Assessment of Current Status and Future Prospects,” ECS Journal of Solid State Science and Technology, vol. 4, no. 5, pp. N30–N35, 2015.   
[3] M. Jerry, P.-Y. Chen, J. Zhang, P. Sharma, K. Ni, S. Yu, and S. Datta, “Ferroelectric FET analog synapse for acceleration of deep neural network training,” in 2017 IEEE International Electron Devices Meeting (IEDM). IEEE, 2017, pp. 6.2.1–6.2.4.   
[4] M. Lederer, T. Kämpfe, T. Ali, F. Müller, R. Olivo, R. Hoffmann, N. Laleni, and K. Seidel, “Ferroelectric Field Effect Transistors as a Synapse for Neuromorphic Application,” IEEE Transactions on Electron Devices, vol. 68, no. 5, pp. 2295–2300, 2021.   
[5] S. De, F. Müller, S. Thunder, S. Abdulazhanov, N. Laleni, M. Lederer, T. Ali, Y. Raffel, S. Dunkel, S. Mojumder, A. Vardar, S. Beyer, K. Seidel, and T. Kampfe, “28 nm HKMG-Based Current Limited [[FeFET]] [[crossbar]]-Array for Inference Application,” IEEE Transactions on Electron Devices, pp. 1–5, 2022.   
[6] S. De, F. Müller, N. Laleni, M. Lederer, Y. Raffel, S. Mojumder, A. Vardar, S. Abdulazhanov, T. Ali, S. Dunkel, S. Beyer, K. Seidel, and T. Kampfe, “Demonstration of Multiply-Accumulate Operation with 28 nm [[FeFET]] Crossbar Array,” IEEE Electron Device Letters, p. 1, 2022.   
[7] S. De, M. A. Baig, B.-H. Qiu, F. Müller, H.-H. Le, M. Lederer, T. Kämpfe, T. Ali, P.-J. Sung, C.-J. Su, Y.-J. Lee, and D. D. Lu, “Random and Systematic Variation in Nanoscale $\mathrm { H f } _ { 0 . 5 } \mathrm { Z r } _ { 0 . 5 } 0 _ { 2 }$ Ferroelectric FinFETs: Physical Origin and Neuromorphic Circuit Implications,” Frontiers in Nanotechnology, vol. 3, 2022.   
[8] M. Dragoman, M. Aldrigo, M. Modreanu, and D. Dragoman, “Extraordinary tunability of high-frequency devices using Hf0.3Zr0.7O2 ferroelectric at very low applied voltages,” Appl. Phys. Lett., vol. 110, no. 10, p. 103104, 2017.   
[9] M. Dragoman, M. Modreanu, I. Povey, S. Iordanescu, M. Aldrigo, A. Dinescu, D. Vasilache, and C. Romanitan, “2.55 GHz miniaturised phased antenna array based on 7 nm-thick $\mathrm { H f _ { x } } Z \mathbf { r } _ { 1 - \mathrm { x } } \mathbf { O } _ { 2 }$ ferroelectrics,” Electron. Lett., vol. 54, no. 8, pp. 469–470, 2018.   
[10] S. Abdulazhanov, Q. H. Le, D. K. Huynh, D. Wang, M. Lederer, R. Olivo, K. Mertens, J. Emara, T. Kämpfe, and G. Gerlach, “RF-Characterization of HZO Thin Film Varactors,” Crystals, vol. 11, no. 8, p. 980, 2021.   
[11] S. Abdulazhanov, D. K. Huynh, Q. H. Le, D. Lehninger, T. Kampfe, and G. Gerlach, “BEoL integrated hafnium zirconium oxide varactors for tunable mmWave applications,” in ESSDERC 2022 - IEEE 52nd European Solid-State Device Research Conference (ESSDERC). IEEE, 2022, pp. 253–256.   
[12] S. Abdulazhanov, Q. H. Le, D. K. Huynh, D. Wang, D. Lehninger, T. Kämpfe, and G. Gerlach, “THz Thin Film Varactor Based on Integrated Ferroelectric HfZrO2,” ACS Applied Electronic Materials, 2022.   
[13] S. Abdulazhanov, D. K. Huynh, Q. H. Le, D. Lehninger, T. Kampfe, and G. Gedach, “Investigation of BEoL integrated ferroelectric thin-film HfO 2 for mmWave varactor applications,” in 2022 IEEE International Symposium on Radio-Frequency Integration Technology (RFIT). IEEE, 2022, pp. 131–133.   
[14] J. Y. Yang, M. J. Yeom, J. Lee, K. Lee, C. Park, J. Heo, and G. Yoo, “Reconfigurable Radio–Frequency High–Electron Mobility Transistors via Ferroelectric–Based Gallium Nitride Heterostructure,” Advanced Electronic Materials, vol. 8, no. 9, p. 2101406, 2022.   
[15] J. Feldmann, N. Youngblood, M. Karpov, H. Gehring, X. Li, M. Stappers, M. Le Gallo, X. Fu, A. Lukashchuk, A. S. Raja, J. Liu, C. D. Wright, A. Sebastian, T. J. Kippenberg, W. H. P. Pernice, and H. Bhaskaran, “Parallel convolutional processing using an integrated photonic tensor core,” Nature, vol. 589, no. 7840, pp. 52–58, 2021.

[16] C. Wang, S.-J. Liang, C.-Y. Wang, Z.-Z. Yang, Y. Ge, C. Pan, X. Shen, W. Wei, Y. Zhao, Z. Zhang, B. Cheng, C. Zhang, and F. Miao, “Scalable massively parallel computing using continuous-time data representation in nanoscale crossbar array,” Nature nanotechnology, vol. 16, no. 10, pp. 1079–1085, 2021.   
[17] E. Lourandakis, On-wafer microwave measurements and de-embedding, ser. Microwave design. Boston and London: Artech House, 2016.   
[18] I. J. Bahl, Fundamentals of RF and microwave transistor amplifiers. Oxford: Wiley, 2009.   
[19] Q. H. Le, D. K. Huynh, D. Wang, T. Kampfe, Z. Zhao, and S. Lehmann, “Assessment of a Thick-Oxide Transistor from the 22FDX Platform for 5G NR sub-6 GHz FEMs,” in 2019 IEEE 2nd 5G World Forum (5GWF). IEEE, 2019, pp. 7–10.   
[20] M. Sadegh Dadash, S. Bonen, U. Alakusu, D. Harame, and S. P. Voinigescu, “DC-170 GHz Characterization of 22nm [[FDSOI]] Technology for Radar Sensor Applications,” in 2018 13th European Microwave Integrated Circuits Conference (EuMIC). IEEE, 2018, pp. 158–161.   
[21] J. Casamento, K. Nomoto, T. S. Nguyen, H. Lee, C. Savant, L. Li, A. Hickman, T. Maeda, Encomendero, V. Gund, A. Lal, J. C. M. Hwang H. G. Xing, and D. Jena, Ed., FerroHEMTs: High-Current and High-Speed All-Epitaxial AlScN/GaN Ferroelectric Transistors, 2022.   
[22] J. Cheng, M. W. Rahman, A. Xie, H. Xue, S. H. Sohel, E. Beam, C. Lee, H. Yang, C. Wang, Y. Cao, S. Rajan, and W. Lu, “Breakdown Voltage Enhancement in ScAlN/GaN High-Electron-Mobility Transistors by High- k Bismuth Zinc Niobate Oxide,” IEEE Transactions on Electron Devices, vol. 68, no. 7, pp. 3333–3338, 2021.   
[23] A. J. Green, J. K. Gillespie, R. C. Fitch, D. E. Walker, M. Lindquist, A. Crespo, D. Brooks, E. Beam, A. Xie, V. Kumar, J. Jimenez, C. Lee, Y. Cao, K. D. Chabak, and G. H. Jessen, “ScAlN/GaN High-Electron-Mobility Transistors With 2.4-A/mm Current Density and 0.67-S/mm Transconductance,” IEEE Electron Device Letters, vol. 40, no. 7, pp. 1056–1059, 2019.   
[24] T. E. Kazior, E. M. Chumbes, B. Schultz, J. Logan, D. J. Meyer, and M. T. Hardy, “High Power Density ScAlN-Based Heterostructure FETs for mm-Wave Applications,” pp. 1136–1139.