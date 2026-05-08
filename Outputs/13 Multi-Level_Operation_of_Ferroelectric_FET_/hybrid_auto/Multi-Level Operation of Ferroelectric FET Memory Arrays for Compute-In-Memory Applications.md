---
title: "Multi-Level Operation of Ferroelectric FET Memory Arrays for Compute-In-Memory Applications"
authors:
  - "Franz Muller"
  - "Sourav De"
  - "Maximilian Lederer"
  - "Raik Hoffmann"
  - "Ricardo Olivo"
  - "Thomas Kampfe"
  - "Konrad Seidel"
  - "Tarek Ali"
  - "Halid Mulaosmanovic"
  - "Stefan Dunkel"
  - "Johannes Muller"
  - "Sven Beyer"
  - "Gerald Gerlach"
date: "2023-03-01"
year: 2023
journal: "IEEE Journal on Exploratory Solid-State Computational Devices and Circuits"
doi: "10.1109/JXCDC.2022.3227351"
abstract: "We report on the multi-level-cell (MLC) operation of AND-connected ferroelectric\\"
abstract_cn: "本文研究 AND 连接铁电场效应晶体管 (FeFET) 阵列的多级单元 (MLC) 操作及其在存内计算 (CiM) 应用中的适用性。研究了被动 AND 阵列测试结构中\\"
keywords:
  - "[[FeFET]]"
  - "[[Multi-level cell]]"
  - "[[Compute-in-memory]]"
  - "[[AND array]]"
  - "[[Neural network]]"
cite: "[1] Muller F, De S, Lederer M, et al. Multi-Level Operation of Ferroelectric FET\\"
aiSum: "研究 28nm FeFET AND 阵列的多级操作，提出写入验证方案和静态抑制方案实现 2-3 位/单元操作，BER 4%，CIFAR-10 LeNet 推理精度仅下降\\"
confidence: medium
---

Franz Muller, Sourav De, Maximilian ¨ Lederer, Raik Hoffmann, Ricardo Olivo, Thomas Kampfe, Konrad Seidel¨ Fraunhofer Institute for Photonic Microsystems Dresden, Germany franz.mueller@ipms.fraunhofer.de

Tarek Ali, Halid Mulaosmanovic, Stefan Dunkel, Johannes M ¨ uller, ¨ Sven Beyer GlobalFoundries Dresden, Germany sven.beyer@globalfoundries.com

Gerald Gerlach

Technische Universitat Dresden ¨ Dresden, Germany gerald.gerlach@tu-dresden.de

Abstract—We report on the multi-level-cell (MLC) operation of AND-connected ferroelectric FET (FeFET) arrays and their suitability for Compute-in-Memory (CiM) applications. The switching behavior and device variation of FeFETs in a passive AND array test-structure configuration is investigated. From this, we derive suitable write schemes and inhibit schemes capable of protecting any FeFET state. This enables the MLC operation of the AND arrays, yielding a performance suitable for CiM applications. We investigate the impact of the obtained bit-errorrate (BER) of 4% in inference-only operation, which shows only a 1% degradation from the floating-point (FP) accuracy for CIFAR-10 datasets with LeNET.

Index Terms—ferroelectric, memory, FeFET, array, multilevel, neural network

# I. INTRODUCTION

Since the discovery of ferroelectricity in $\mathrm { H f O _ { 2 } }$ [1] FeFETs have been a promising contender in the field of emerging non-volatile memories (eNVMs). HfO2 enables scalability to recent technology nodes and beyond. Coupled with cointegration capability, low-power operation, and competitive endurance and data retention, this explains the continuing research interest in this memory technology [2]. Besides pure storage applications, FeFETs are also researched in the field of neuromorphic and Compute-in-Memory (CiM) applications. The ability to gradually transition between the programmed and erased state is a key benefit of this technology. While single device characterization is sufficient for the understanding of device and process parameters, more authentic studies can be performed through the further progression towards array-level measurements for the verification of very large scale integration (VLSI) applications. Characterization on this level is limited to binary operation to date [2]–[6]. In this case, a FeFET (Fig. 1) is written by applying a positive or negative gate voltage, while keeping the source, drain and bulk terminals grounded. This results in a low threshold voltage (LVT) state and a high threshold voltage (HVT) state, respectively. The ferroelectric $\mathrm { H f O _ { 2 } }$ switches due to its field-driven

This work was funded in the framework Important Project of Common European Interest (IPCEI) by the Federal Ministry for Economics and Energy and by the State of Saxony, and in part from the ECSEL Joint Undertaking (JU) under grant agreement No 876925. The JU receives support from the European Union’s Horizon 2020 research and innovation programme and France, Belgium, Germany, Netherlands, Portugal, Spain, Switzerland.

polarization properties. A unit-cell-intrinsic isolation between domains [7] results in less coupling between neighboring domains and enables a gradual transition between LVT and HVT. This property enables multi-level-cell (MLC) operation. However, due to large grains [8] of the polycrystalline $\mathrm { H f O _ { 2 } }$ microstructure, with width and length scaling, the switching transition becomes less gradual [9] and device variation in regard to switching behavior becomes challenging [10].

![](images/b03d0144731fb780b49a6e5d77a94a81c5a431275b476cb72ca8f255228bbb56.jpg)

![](images/2c4dbd3c99ccda3904951cb10df8f06d868803cb337691182125eb4465dee730.jpg)  
Fig. 1. Illustration of the FeFETs devices arranges in an AND-connected array structure (a). Each FeFET can be gradually written as the transfer characteristics show (b).

In this work, we show that device-to-device (D2D) switching variation can be counteracted. Suitable writing schemes are investigated for this purpose. To protect the state of a FeFET once it is written to a target state, inhibit conditions suitable in AND arrays are screened. We show that even static conditions are suitable, reducing the overall implementation complexity. By combining the write- and inhibit-scheme, MLC operation on AND-connected FeFET memory arrays is enabled. Finally, the applicability of a CiM implementation is demonstrated.

# II. SWITCHING BEHAVIOR ON ARRAY LEVEL

The switching behavior of FeFETs is characterized by AND-connected arrays with direct access to wordlines (WL), sourcelines (SL) and bitlines (BL). With 9 WL and 7 SL/BL, 63 450×450 nm² FeFETs are available per array. The test structures, shown in Fig. 1a, were fabricated in GlobalFoundries 28 nm high-k-metal-gate (HKMG) technology node and feature metal-ferroelectric-isolator-silicon (MFIS) structured Fe-FETs. Individual Source-Measure-Units ensure parallel access for each contact. A linearly increasing gate voltage (VG) is applied to each WL in steps of 40 mV while keeping source

(VS) and drain (VD) contacts via SL and BL at 0 V. After a set pulse, a read-delay of 2 s is applied to avoid trappingrelated influences. The readout is done per WL in parallel with $V _ { G } = 0 . 1 \ : \mathrm { V }$ .. 1.5 V in steps of 0.1 V while keeping all BL at 1 V. A series of $V _ { G }$ read voltages and the corresponding $I _ { D }$ are acquired. By continuing the altering scheme of setpulses and readouts, a write-verify-scheme [11] is realized. As visualized in Fig. 1b, a set of $I _ { D } V _ { G }$ curves can be analyzed for VT state separation, as required in CAM applications [12], or for $I _ { o n } / I _ { o f f }$ , as in standard memory applications. The resulting switching trends for an array of 63 FeFETs in Fig. 2 result from gradual programming (a, b) or erasing (c). The comparison of VT transition for the program (a) and erase (c) show that an erase transition starts earlier and is more gradual. Therefore, array designs capable of utilizing negative write voltages would be beneficial. This is attributed to the underlying mechanism of current percolation paths that form in the transistor channel of MFIS-based FeFETs [10], [13]. Different operating points have an effect on the granularity of the switching transition, especially noticeable in Fig. 2b. The 2-bit MLC states achievable with the best read condition are extracted and shown in Fig. 2(d-f). It can be seen that a wide range of write voltages is necessary for a full transition from an erased to a programmed state and vice versa. While accumulative switching schemes have been demonstrated for FeFETs [14], a voltage-controlled write scheme mitigates the array-level variation in required pulse counts.

# III. INHIBIT CONDITION SCREENING

To protect FeFETs that have reached their target value and no longer need to change state, inhibit schemes must be used. By screening different operation conditions for these subsequently passive FeFETs, the voltage range for a disturbfree operation range is found. For an actively programmed FeFET, three different passive FeFETs are defined based on their relation to the target cell. Type 1 shares the active WL, type 2 shares the active SL and BL, and type 3 shares no active contact, as visualized in Fig. 3a. Based on Fig. 2, a maximum $V _ { W L } = 4 . 0 \mathrm { V } ~ ( V _ { D D } )$ is defined. The cells of one

![](images/ddba7970b39e1733f324f24d374a765e527864cd9a3a57b0396075a26f7c74fb.jpg)

![](images/8c20ef05a8fd7b9369aa5ad6a2b39b90a153221a3602250e605bf1bcd16ce27a.jpg)

![](images/c99f4a82c931d783bc0b04adece7d5c34408aad73e4bf1dc5971ccae95b45cd2.jpg)

![](images/84acc01ca73474f9c46bec3f655a4f51c72f78351a751c982af3c7f3ce93d948.jpg)

![](images/8239024be478aec5299776aaff9b65ede715c40dae47bebca2d7985a9e021e59.jpg)

![](images/62497373fa26bb141c4bd8f6a4d0c041e272942444b750b1f9488b907f6950f9.jpg)

![](images/0c449ab6f538d216d51f9cafdf3457fbaca16541dd3c8f84972efe361e3e14aa.jpg)

![](images/bc832027b2de75ac8ebc2ba619dc145997a9b5abce32921be7959f07a09ffce3.jpg)

![](images/7da9170c437e3c229f0574358e3e21369b914e65f4274c687aa854144f58112c.jpg)

![](images/4e9041477b5d740d98a1eae257e1521e4398e0d59db4cec244cd8c5637b016f9.jpg)  
Fig. 2. Comparison of amplitude-driven set-schemes at different operating points. Presented are the switching transitions for constant-current (a, c) and constant-voltage (b) reading. These are performed by programming (a, b) and erasing (c). The distributions show 2-bit/cell can be achieved for array-level operation for both VT and $I _ { D }$ -based operation (d, e, f).   
Fig. 3. AND-array shows the three types of unselected bits (a). Efficient inhibit operation plays a crucial role in implementing MLC on array level. Inhibit-screening after 50 pulses with constant program voltage of $V _ { W L } = 4 . 0 \mathrm { V } ,$ highlighting usable inhibit-voltage-range for disturb-free operation of neighbor type 1 (b), 2 (c) and 3 (d).

AND array are grouped into sets of active and three passive types. The array is initially entirely erased. Inhibit voltages are stepped in 400 mV over a range of 1.6 V to 3.2 V. Active FeFETs are pulsed 50 times with $V _ { W L m a x }$ at each set of inhibit voltages. After write, the whole array is read and the scheme is repeated with the next inhibit voltage set. Fig. 3b presents the results for the change in VT of the passive SL/BL FeFETs. With $V _ { W L m a x } = 4 . 0 \mathrm { V } ,$ disturbs start to be measurable from a passive $V _ { S L / B L } \leq 2 \mathrm { V } .$ This makes a $V _ { D D } / 2$ inhibitscheme marginal and advises using a $V _ { D D } / 3$ method [15]. Fig. 3c shows that passive $V _ { W L } > 2 \mathrm { V }$ starts inducing disturbs in type 2 FeFETs. Fig. 3d shows the resulting disturbance on type 3, which depends on the combination of inhibiting voltages chosen for type 1 and type 2. To give margin, inhibit voltages are set to $V _ { W L p } = 1 . 6 \mathrm { V } , \ V _ { S L / B L p } = 3 . 2 \mathrm { V } ,$ enabling disturb-free operation for program voltages up to 5.2 V even with static inhibit conditions.

# IV. MULTI-LEVEL-OPERATION ON ARRAY LEVEL

With the voltage-driven write-verify- and the voltage-fixed inhibit-scheme, the array is operated in multilevel mode. The write-verify-scheme is performed per WL in parallel on all

![](images/8ae6ab4c4b77193cc67b20f37fa81603facdfd7f3992c6658ed14e7c19803ffe.jpg)

![](images/269279d4c7ac3cff8b176c735057cbd8c178d5426174b7abc594afd56ed0c95b.jpg)

![](images/bd80624aacdd65b92df1fded97a16a484fef934319990ed481a6919c90f4f7aa.jpg)  
Fig. 4. Timing of the write-scheme to avoid write disturbs (a), the transition from actively written FeFETs to inhibit-condition (b) and their application in a continuous data pattern to verify the ability of each FeFET to reach each state (c).

FeFETs, as in section II. Fig. 4a visualizes the timing scheme for a program pulse cycle, ensuring that inhibit conditions are applied first, followed by the pulse. Once a FeFET along the WL reaches the target state, it is put on the inhibit condition of type 1 passive FeFETs, changing pulsing conditions as in Fig. 4b. While programming along one WL, FeFETs of other WLs are inhibited according to types 2 & 3. All FeFETs along the active WL are read in each write cycle, ensuring continuous state verification until the last FeFET has reached its target state. A walking-bit input dataset is suggested to fully explore the ability of each FeFET to reach each state and persistently withstand disturb-voltages. Each FeFET is set to each desired target once, having neighbors at deviating states. This worstcase exploration is tested on a 3-bit level, shown in 4c, with the primary source of the error caused by the hard-to-reach LVT state. The evolution of the VT state can be seen in Fig. 5, highlighting the transition of 7 FeFETs per WL for four different WLs from an HVT state to the desired target ranges. It should be noted that in the effective inhibit scheme, the VT state is not further shifted after a FeFET has reached the target.

![](images/0d4e046f4a7ecbe75fe28bae48f1d4c32186bc89adc4ef0347af29581285a70c.jpg)

![](images/b642f30da30a33e1bfbe24d01bd00061810de7de941d356469ae8610b20a8458.jpg)  
Fig. 5. Screening of the states of 7 FeFETs per WL, that are written to 4 distinct states, highlighting the respective target ranges. As seen, inhibit is effective and prevents disturbance until all FeFETs are set.

![](images/eb9cd55883abaa4527a7445d9e2ff9a237411903adb62e78e6d0cd976c198991.jpg)  
Fig. 6. Neural network (NN) architectures used to validate the neuromorphic capability of the AND arrays (a) and schematic representation of the memory array with 1F synaptic devices as analyzed in the simulation (b).

# V. IMPLICATIONS ON NEURAL NETWORKS
  - "[[FeFET]]"
  - "[[Neural network]]"

To quantify the aptness of the 28 nm-based FeFET arrays as synaptic-core, we have performed a system-level neuromorphic simulation [16] (Fig. 6). To calibrate the simulation framework a random pattern at 2-bit resolution with evenly distributed states is used. The read is voltage-based at $V _ { W L } = 1 . 4 \ : \mathrm { V }$ with $V _ { B L } = 1 { \bf V } . \mathrm { ~ A ~ }$ total of 25 arrays with 63 FeFETs each were written and the states verified. The resulting currents for the 4 target levels are shown in Fig. 7. Once an entire array is written, the states of all FeFETs are verified, obtaining a BER of 4%.

![](images/70f522901d5280072439a780be5ba6143cf7bd0bc88a0d6cd930048e245be148.jpg)  
Fig. 7. Writing an equally distributed data pattern to multiple AND-arrays, resulting in a total of 1.5k FeFETs. Shown are the resulting box plots for the written states over the targeted states.

We only consider two scenarios of offline training. The first is training a multilevel perceptron neural network (MLP-NN) with the MNIST data set, and the second is training the LeNET with CIFAR-10 datasets. The measured 4-level operations with experimentally calibrated D2D and cycle-to-cycle (C2C) variations (σD2D, σC2C) in $I _ { B L }$ distribution have been used during weight-update (WRITE) and inference (READ) in FeFET-based NN. The impact of D2D and C2C variation that arises from the inability to program the synaptic devices to the desired $I _ { D }$ state shows a mere 2% and 1% degradation in hardware-based NN for MNIST and CIFAR-10 datasets from the FP precision (Fig. 6). The 2-bits/cell synaptic core also outperforms the other bit-precision in energy efficiency and latency (Fig. 8).

# VI. CONCLUSIONS

We show how multilevel states can be written and maintained in AND-connected FeFET arrays with appropriate BER.

![](images/67500f6db949910b42abd3cbfa0ac6901559081d4b2e8622ba41e0aa26013537.jpg)

![](images/b51148b4ac4e067191742a1a74cc0c92f9b2b20a2c320df63dbc5a5498208a2d.jpg)  
Fig. 8. 2-bit precision showing good performance for energy consumption and latency (a), while obtaining the best inference accuracy for different datasets(b).

First, by writing the entire array stepwise, inhibit schemes can be avoided, and the holistic switching behavior can be investigated. This shows a controllable cell variability when using a voltage-controlled writing approach. The screening of inhibit conditions reveals that a static condition tailored to the highest write voltage sufficiently avoids write disturbances. By combining write and inhibit schemes, successful MLC operation is demonstrated. Finally, system-level validation through NN simulation confirms the importance of MLC for arraylevel operation, especially for inference operations. Table I compares this work with other state-of-the-art ferroelectric memory arrays.

TABLE I COMPARING THE WORK TO PRIOR ART.   

<table><tr><td></td><td>[3], [4]</td><td>[5]</td><td>[6]</td><td>This work</td></tr><tr><td rowspan="2">Bit Cell</td><td>1F1C</td><td>1F1C</td><td>1F1R</td><td>1F</td></tr><tr><td>FeRAM</td><td>FeRAM</td><td>FeFET</td><td>FeFET</td></tr><tr><td>Bit Precision</td><td>SLC</td><td>SLC</td><td>SLC</td><td>MLC</td></tr><tr><td>Technology</td><td>180 nm</td><td>130 nm</td><td>28 nm</td><td>28 nm</td></tr><tr><td>Parallel MAC</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Relative Area</td><td>45x</td><td>25x</td><td>4x</td><td>1x</td></tr><tr><td>Fe-Integration</td><td>MoL</td><td>BEoL</td><td>FEoL</td><td>FEoL</td></tr><tr><td>Sensing Mode</td><td>Voltage</td><td>Voltage</td><td>Current</td><td>Voltage or Current</td></tr></table>

# REFERENCES

[1] T. S. Boscke, J. M ¨ uller, D. Br ¨ auhaus, U. Schr ¨ oder, and U. B ¨ ottger, ¨ “Ferroelectricity in hafnium oxide thin films,” Applied Physics Letters, vol. 99, no. 10, p. 102903, 2011, doi: 10.1063/1.3634052.   
[2] S. Beyer, S. Dunkel, M. Trentzsch, J. Muller, A. Hellmich, D. Utess, J. Paul, D. Kleimaier, J. Pellerin, S. Muller, J. Ocker, A. Benoist, H. Zhou, M. Mennenga, M. Schuster, F. Tassan, M. Noack, A. Pourkeramati, F. Muller, M. Lederer, T. Ali, R. Hoffmann, T. Kampfe, K. Seidel, H. Mulaosmanovic, E. T. Breyer, T. Mikolajick, and S. Slesazeck, “Fe-FET: A versatile CMOS compatible device with game-changing potential,” in 2020 IEEE International Memory Workshop (IMW). Piscataway, NJ: IEEE, 2020, pp. 1–4, doi: 10.1109/IMW48823.2020.9108150.   
[3] J. Okuno, T. Kunihiro, K. Konishi, H. Maemura, Y. Shuto, F. Sugaya, M. Materano, T. Ali, M. Lederer, K. Kuehnel, K. Seidel, U. Schroeder, T. Mikolajick, M. Tsukamoto, and T. Umebayashi, “High-Endurance and Low-Voltage operation of 1T1C FeRAM Arrays for Nonvolatile Memory Application,” in 2021 IEEE International Memory Workshop (IMW). Piscataway, NJ: IEEE, 2021, pp. 1–3, doi: 10.1109/IMW51353.2021.9439595.   
[4] K. Seidel, D. Lehninger, R. Hoffmann, T. Ali, M. Lederer, R. Revello, K. Mertens, K. Biedermann, Y. Shen, D. Wang, M. Landwehr, A. Heinig, T. Kampfe, H. Mahne, K. Bernert, and S. Thiem, “Memory

Array Demonstration of fully integrated 1T-1C FeFET concept with separated ferroelectric MFM device in interconnect layer,” in 2022 IEEE Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits). IEEE, 6/12/2022 - 6/17/2022, pp. 355–356, doi: 10.1109/VLSITechnologyandCir46769.2022.9830141.   
[5] T. Francois, J. Coignus, A. Makosiej, B. Giraud, C. Carabasse, J. Barbot, S. Martin, N. Castellani, T. Magis, H. Grampeix, S. van Duijn, C. Mounet, P. Chiquet, U. Schroeder, S. Slesazeck, T. Mikolajick, E. Nowak, M. Bocquet, N. Barrett, F. Andrieu, and L. Grenouillet, “16kbit HfO2:Si-based 1T-1C FeRAM Arrays Demonstrating High Performance Operation and Solder Reflow Compatibility,” in 2021 IEEE International Electron Devices Meeting (IEDM). IEEE, 12/11/2021 - 12/16/2021, pp. 33.1.1–33.1.4, doi: 10.1109/IEDM19574.2021.9720640.   
[6] S. De, F. Muller, S. Thunder, S. Abdulazhanov, N. Laleni, M. Lederer, T. Ali, Y. Raffel, S. Dunkel, S. Mojumder, A. Vardar, S. Beyer, K. Seidel, and T. Kampfe, “28 nm HKMG-Based Current Limited FeFET Crossbar-Array for Inference Application,” IEEE Transactions on Electron Devices, pp. 1–5, 2022, doi: 10.1109/TED.2022.3216973.   
[7] H.-J. Lee, M. Lee, K. Lee, J. Jo, H. Yang, Y. Kim, S. C. Chae, U. Waghmare, and J. H. Lee, “Scale-free ferroelectricity induced by flat phonon bands in HfO2,” Science (New York, N.Y.), vol. 369, no. 6509, pp. 1343–1347, 2020, doi: 10.1126/science.aba0067.   
[8] M. Lederer, A. Reck, K. Mertens, R. Olivo, P. Bagul, A. Kia, B. Volkmann, T. Kampfe, K. Seidel, and L. M. Eng, “Impact of the SiO ¨ 2 interface layer on the crystallographic texture of ferroelectric hafnium oxide,” Applied Physics Letters, vol. 118, no. 1, p. 012901, 2021, doi: 10.1063/5.0029635.   
[9] H. Mulaosmanovic, S. Slesazeck, J. Ocker, M. Pesic, S. Muller, S. Flachowsky, J. Muller, P. Polakowski, J. Paul, S. Jansen, S. Kolodinski, C. Richter, S. Piontek, T. Schenk, A. Kersch, C. Kunneth, R. van Bentum, U. Schroder, and T. Mikolajick, “Evidence of single domain switching in hafnium oxide based FeFETs: Enabler for multi-level FeFET memory cells,” in 2015 IEEE International Electron Devices Meeting (IEDM), 2015, p. 26.8.1, doi: 10.1109/IEDM.2015.7409777.   
[10] F. Muller, M. Lederer, R. Olivo, T. Ali, R. Hoffmann, H. Mulaosmanovic, S. Beyer, S. Dunkel, J. Muller, S. Muller, K. Seidel, and G. Gerlach, “Current percolation path impacting switching behavior of ferroelectric FETs,” in 2021 International Symposium on VLSI Technology, Systems and Applications (VLSI-TSA). IEEE, 2021, pp. 1–2, doi: 10.1109/VLSI-TSA51926.2021.9440081.   
[11] H. Zhou, J. Ocker, A. Padovani, M. Pesic, M. Trentzsch, S. Dunkel, H. Mulaosmanovic, S. Slesazeck, L. Larcher, S. Beyer, S. Muller, and T. Mikolajick, “Application and Benefits of Target Programming Algorithms for Ferroelectric HfO2 Transistors,” in 2020 IEEE International Electron Devices Meeting (IEDM). IEEE, 12122020, pp. 18.6.1–18.6.4, doi: 10.1109/IEDM13553.2020.9371975.   
[12] C. Li, F. Muller, T. Ali, R. Olivo, M. Imani, S. Deng, C. Zhuo, T. Kampfe, X. Yin, and K. Ni, “A Scalable Design of Multi-Bit Ferroelectric Content Addressable Memory for Data-Centric Computing,” in 2020 IEEE International Electron Devices Meeting (IEDM). IEEE, 2020, doi: 10.1109/iedm13553.2020.9372119.   
[13] K. Ni, S. Thomann, O. Prakash, Z. Zhao, S. Deng, and H. Amrouch, “On the Channel Percolation in Ferroelectric FET Towards Proper Analog States Engineering,” in 2021 IEEE International Electron Devices Meeting (IEDM). IEEE, 12/11/2021 - 12/16/2021, pp. 15.3.1–15.3.4, doi: 10.1109/IEDM19574.2021.9720631.   
[14] H. Mulaosmanovic, S. Dunkel, M. Trentzsch, S. Beyer, E. T. Breyer, T. Mikolajick, and S. Slesazeck, “Investigation of Accumulative Switching in Ferroelectric FETs: Enabling Universal Modeling of the Switching Behavior,” IEEE Transactions on Electron Devices, vol. 67, no. 12, pp. 5804–5809, 2020, doi: 10.1109/TED.2020.3031249.   
[15] S. Mueller, J. Muller, R. Hoffmann, E. Yurchuk, T. Schlosser, R. Boschke, J. Paul, M. Goldbach, T. Herrmann, A. Zaka, U. Schroder, and T. Mikolajick, “From MFM Capacitors Toward Ferroelectric Transistors: Endurance and Disturb Characteristics of HfO2-Based FeFET Devices,” IEEE Transactions on Electron Devices, vol. 60, no. 12, pp. 4199–4205, 2013, doi: 10.1109/TED.2013.2283465.   
[16] S. De, D. D. Lu, H.-H. Le, S. Mazumder, Y.-J. Lee, W.-C. Tseng, B.- H. Qiu, M. A. Baig, P.-J. Sung, C.-J. Su, C.-T. Wu, W.-F. Wu, W.-K. Yeh, and Y.-H. Wang, “Ultra-Low Power Robust 3bit/cell Hf0.5Zr0.5O2 Ferroelectric FinFET with High Endurance for Advanced Computing-In-Memory Technology,” in 2021 Symposium on VLSI Technology, 2021, pp. 1–2.