---
title: "Understanding correlation between memory window closure, leakage and read delay effects\"
authors:
  - "Priyankka Ravikumar"
  - "Andrea Padovani"
  - "Prasanna Venkatesan"
  - "Chinsung Park"
  - "Nashrah Afroze"
  - "Mengkun Tian"
  - "Suman Datta"
  - "Shimeng Yu"
  - "Luca Larcher"
  - "Gaurav Thareja"
  - "Asif Khan"
date: "2024-01-01"
year: "2024"
journal: "IEEE Transactions on Electron Devices"
abstract: "Memory window (MW) closure, read delay, and gate leakage are three key reliability\"
abstract_cn: "存储窗口闭合、读取延迟和栅极泄漏是铁电场效应晶体管可靠性面临的三个关键挑战，传统上通常被单独分析。本文通过专门实验和器件模拟，详细研究了具有 10 nm 铁电 HZO\"
keywords:
  - "[[Ferroelectric FET]]"
  - "[[Memory window closure]]"
  - "[[Read delay]]"
  - "[[Gate leakage]]"
  - "[[Reliability]]"
cite: "[1] Ravikumar P, Padovani A, Venkatesan P, et al. Understanding correlation between\"
aiSum: "铁电场效应晶体管的存储窗口闭合、读取延迟和栅极泄漏三大可靠性挑战相互关联：极化翻转加速界面层慢陷阱产生，导致存储窗口恢复减少和闭合；界面层严重退化后触发 HZO\"
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
  - "[[Read delay]]"
---

Priyankka Ravikumar1,∧,Andrea Padovani2, Prasanna Venkatesan 1, Chinsung Park1, Nashrah Afroze1, Mengkun Tian3, Suman Datta1,4, Shimeng Yu1, Luca Larcher5, Gaurav Thareja5, Asif Khan1,4,$

1School of Electrical and Computer Engineering, Georgia Institute of Technology, GA, USA;

2 Engineering Department “Enzo Ferrari”, UNIMORE, Italy; 3Institute of Materials, GA, USA;

4School of Material Science and Engineering, Georgia Institute of Technology, GA, USA; 5Applied Materials

{∧pravikumar30, $akhan40}@gatech.edu

Abstract—Memory window (MW) closure, [[Read delay]], and [[Gate leakage]] are three key reliability challenges in ferroelectric (FE) field-effect transistors (FEFETs), all of which have traditionally been analyzed separately. In this work, we exploit dedicated experiments and device simulations to present a detailed study of these three mechanisms in Si-FEFETs with a 10nm layer of FE HZO. The results reveal critical insights into the interplay between trap generation and polarization switching (PS), and the correlation between MW closure, [[Read delay]], and leakage current. First, we show that trap generation is accelerated by PS and initially (up to 5x104 cycles) occurs mainly in the interfacial layer (IL). These PS induced traps are slow traps and are found to be responsible for both reduction in MW recovery with [[Read delay]] and MW closure, demonstrating a strong correlation between the two mechanisms. Finally, we show that leakage current increase is controlled by the generation of HZO traps, which is triggered by internal field redistribution once IL is highly degraded (after MW closure). The engineering of FEFETs to minimize the formation of slow (de)trapping defects in the IL is essential to improve overall reliability of the FEFET device.

Keywords [[- FEFET]], [[Endurance]], [[Read delay]], [[Gate leakage]], [[GinestraT M ]].

# I. INTRODUCTION

Ferroelectric field effect transistors (FEFETs) are emerging as a highly promising technology for next-generation data storage, combining high speed, energy efficiency, low power consumption, and fast switching, making them ideal for applications in edge computing, artificial intelligence, and cloud-based enterprise systems [1,2]. However, challenges such as memory window (MW) degradation, which limits write [[Endurance]], [[Read delay]], which limits operating speed, and [[Gate leakage]] remain critical obstacles to their broader adoption.

FEFETs have a ferroelectric layer that has polarization pointing towards the channel or away from the channel. When the polarization points towards the channel, the channel sees the positive polarization charges, making inversion in the n-channel FEFET easier, thus leading to the low $V _ { T }$ state. When the polarization points away from

the channel, the channel sees negative polarization charges, leading to the high VT state. Repeated read and write operations are emulated by applying bipolar voltage pulses. This cycling leads to the high $V _ { T }$ state reducing and the low $V _ { T }$ state increasing, eventually leading to full memory window closure. This effect has been associated to both polarization fatigue and to trap generation in the interfacial layer screening the polarization charges [3-12]. One of the other major challenges is the read-after-write delay effect. Once the device has been written to one state,either to the high $V _ { T }$ or low $V _ { T }$ state, a certain delay is required to see the full memory window. This effect is commonly observed in n-FEFETs [12,13].

Although these issues have typically been analyzed separately [3-11], they are highly correlated and their root causes can all be traced to trap generation in both the interfacial layer (IL) and the ferroelectric (FE) HZO layer (Fig 1).

![](images/6c5e8d274acd113f38593aea46a6d8462c780135a07f63f52d68179f40a65fdf.jpg)  
Fig. 1. Schematic of the key reliability challenges in ferroelectric field effect transistors : memory window (MW) closure, read-after-write delay and [[Gate leakage]]. These three mechanisms are correlated, and their root cause can be traced back to the trap generation in the $\mathrm { S i O _ { 2 } }$ layer and the HZO layer.

In this work, we demonstrate that: (1) MW closure results

![](images/21100498f7b84695c3532f496a54eb84a10796ac626e8dba7542d62c28f17e7d.jpg)  
Fig. 2. a) Schematic of the 10nm HZO n-channel FEFET. b) Process flow and c) STEM image of ferroelectric HZO FET. Diffraction patterns confirm the crystallinity of FEFET.

from electron traps in the IL, (2) [[Read delay]] arises from the slow (de)trapping of electrons from these traps, and (3) stress-induced [[Gate leakage]] is controlled by trap generation in the HZO layer.

# II. EXPERIMENTS

n-channel Si-FEFETs with an 10nm layer of FE-HZO were fabricated according to the process flow shown in Fig 2b. Fig.2c shows the Transmission Electron Microscopy (TEM) image and diffraction pattern of the device confirming the crystallinity and thickness of the HZO layer.

Electrical measurements were performed with a Keysight B1500. In order to understand the mechanism behind the degradation of FEFETs, we perform read-after-write delay ([[Read delay]]), leakage and threshold voltage measurements as the device is being cycled. To further de-convolute the effects arising specifically from polarization switching under bipolar stress and simple voltage stress, both bipolar and unipolar stress tests were performed. Specifically, the FEFETs were subjected to three different stress conditions: $( 1 ) \pm 3 . 5 \mathrm { V }$

![](images/05292d55fdfddbec94723743f7506a068e58e98715e13fb379fda31f013b4dfd.jpg)

![](images/4f55aa115f9158d914a9fa3d13af531bbbe2c2fe22b60975aeb6f505f9380e4b.jpg)

![](images/e2d048f009f52aaf0a61437a630491b99e64d9041c3303611f94d704b1bb36da.jpg)  
Fig. 3. a) Read-after-write delay measurement scheme. A delay is provided after a write operation that partially recovers MW. b) MW vs voltage and c) DC Id-Vg for the FEFET

bipolar (2) +3.5V positive unipolar, and (3) -3.5V negative unipolar, see Fig. 4(a). Pristine devices are cycled up to $1 0 ^ { 6 }$ cycles. Pulsed Id-Vg measurements are intermittently collected during the cycling process to monitor the threshold voltage $( V _ { T } )$ shifts of both the high $V _ { T }$ and low $V _ { T }$ states. These measurements are performed with [[Read delay]]s varying from 100 $\mu s$ to 10 s, as illustrated in Fig. 3(a). In addition to the pulsed measurements, DC Ig-Vg measurements are carried out at various stages of the stress cycling to observe changes in the leakage current over the period of stress cycling.

# III. MEMORY WINDOW CLOSURE

Memory window closure is indicated by an increase in the low $V _ { T }$ state and a decrease in the high $V _ { T }$ state under stress cycling. In the low $V _ { T }$ state, the polarization is pointing towards the channel and trapped electrons partially screen the polarization. In the high $V _ { T }$ state, the polarization points away from the channel and is partially screened by trapped holes (see Fig. 10(a,b)). Fig. 4 shows the evolution of the measured $\boldsymbol { \mathrm { I } } _ { d } { - } \boldsymbol { \mathrm { V } } _ { g }$ curves under the different stress conditions after (from top to bottom) 1, $1 0 ^ { 4 }$ and $1 0 ^ { 5 }$ cycles. The low $V _ { T }$ state increases significantly with bipolar stress while the decrease in the high $V _ { T }$ state is minimal. This indicates that a significant portion of the MW closure is due to electron trap generation, while the number of hole traps generated with bipolar cycles is minimal. Further, this drastic increase in the low $V _ { T }$ is absent under unipolar stress (Fig.4f), implying that polarization switching (PS) during bipolar stress accelerates electron trap generation.

# IV. [[Read delay]]

The $\mathrm { I } _ { d } \mathrm { - } \mathrm { V } _ { g }$ curves in Fig 4(b,c,d) show the recovery of memory window with sufficient [[Read delay]] at different stages of cycling. Fig 4(e) shows the negative shift in low $V _ { T }$ (MW recovery) as the [[Read delay]] $( t _ { D } )$ is increased. This is a result of the de-trapping of trapped electrons, which partially ‘unscreen’ the polarization (Fig.10(a)). The low $V _ { T }$ exhibits a significant increase after $1 0 ^ { 4 }$ cycles, (Fig. 4(e,f)), with minimal MW recovery with increasing $t _ { D }$ . This suggests that the new traps generated with bipolar cycling are slow and unable to de-trap within the 10s [[Read delay]] provided during the measurement. It is important to note that the unipolar stress also leads to a negative shift in low $V _ { T }$ with increasing [[Read delay]], but this does not change with cycling. This implies that the electron traps leading to MW closure under bipolar stress, are also the ones inhibiting MW recovery with [[Read delay]] post cycling.

The [[Read delay]] effect seen in the initial low $V _ { T }$ state under both unipolar and bipolar cases are is likely due to the first switch effect[14]. To further understand these trends, in particular the correlation between MW recovery and [[Read delay]], we perform $\mathrm { I } _ { g } - \mathrm { V } _ { g }$ measurements and simulations to shed light on stress-induced trap generation in IL and HZO. Simulations

![](images/6bd3f0319b0fd875dd4c181fa8671cacbe2770f6e19a73504ba43b03bba2e220.jpg)  
(a)

![](images/3cbfbddd86c561f72d67062fd465c12bc861c6b86a91dd4e6694ace96fe34083.jpg)  
(

![](images/e99c933107e0aee40dbe97dacd9e2672471b8866285c272a47a78f4739d45817.jpg)

![](images/2cc5b81a01f74afbff90afdaa8824134028562abbe0a1ae5f068c38f21e92abb.jpg)

![](images/2d478589582a13ab8899ecff1945152c8e4af0fe6c8e496a7856f2a308cc737c.jpg)

![](images/f615e1922dfc049ad0793d776e95b3851d2db6289923cd52355892ce81f60eac.jpg)

![](images/7bfa7364cdefefd2af5e1dc2c1e544b6651b61227bae4cfc97a41a3be5981a0e.jpg)

![](images/53b434ede9cc4f989772df5af703796a8cdb8d19d1a560de69a2b12669bc11ff.jpg)  
（

![](images/183e652625d7401d02eae73fef2bc1b9f0be868efbab9573ce096bd134d4a348.jpg)

![](images/81af2d0f5d3293276b8bcdccc75f376ee34fc9a3213858d6810de528115fcbd3.jpg)

![](images/6970c8b359fa6f3969e44c81608a5e50b3f2e6544b9e786145b38d8dc2cf52ad.jpg)  
(

![](images/a4f0764012fc120f27bfea46dd4ad7a6e260fdcf47f33b859a97f0fb27ffa9b3.jpg)

![](images/f8c51c79721e72d1234b862a5c8748398755e8640b5fe2ca5739582e14349c70.jpg)

![](images/04b49a66840e186e5cfbfc35a980ba07a39144aceeb75cfb59aa1d4bbda2df65.jpg)

![](images/782a885d08ebcc55ce14fcc077bd3d6acbe488455c5bf5678e3c14b2aad872de.jpg)

![](images/9766c056aa17c9c9390aa4e398c529cb1ec7da9ca73d936ee4c5eb67ff7a1728.jpg)  
Fig. 4. a) Schematic of the pulsed $\mathrm { I } _ { d } . \mathrm { V } _ { g }$ and stress schemes b-d) $\mathrm { I } _ { d } { - } \mathrm { V } _ { g }$ curves for the different stress cases at each stage of cycling e) Shift in Low VT as Read-after-write delay (RWD) is increased at different stages of cycling. Under bipolar stress, increasing RWD leads to a lesser negative shift in Low VT as more stress is applied. f) The shift in the Low VT with stress cycles. Under bipolar stress, the Low $\bar { \bf V } _ { T }$ shifts significantly while the under unipolar stress the shift is minimal.

![](images/75f1f33d89101bf35be850cb004ba430cb5c5d69bca79e736a56bdeb0264fb22.jpg)  
Fig. 5. a)Band diagrams for different simulated conditions, high IL traps and high HZO traps.

are performed with the [[GinestraT M ]]platform [15], which selfconsistently describes tunneling, trap-assisted charge transport, and trapping mechanisms. The simulations also account for ferroelectric effects and mechanisms.

# V. LEAKAGE

Figure 6(a) shows $\mathrm { I } _ { g } - \mathrm { V } _ { g }$ leakage measurements on FEFETs subjected to the three stresses in Fig.4(a), at different stress stages. Plotting the leakage current at -2.25V as a function of

![](images/a34acbda61945a35e38ce4a6a5e34c7e39a83832e23a2475fafd25e8dc2d2f19.jpg)  
Fig. 6. a-c) $\mathrm { I } _ { g } { - } \mathrm { V } _ { g }$ leakage curves at different stages of cycling under unipolar and bipolar voltage stress.

![](images/c64bbc8099e34eef521cf3fdb41c3f9e44a9561367d48a474ad2a9c9e58d8ea9.jpg)  
Fig. 7. IG taken at -2.25V vs stress cycles for all three stress cases. The leakage under bipolar stress stays under 1 $\mu \mathrm { A } / \mathrm { c m } ^ { 2 }$ until $1 0 ^ { 4 }$ cycles, then shoots up to 10 $\dot { \mu } \mathrm { A / c m ^ { 2 } }$ with subsequent cycling.

stress cycles, Fig. 7, shows a minimal change in the leakage current for the unipolar stresses, whereas a steep leakage increase is observed under bipolar stress, but only after MW closure (at $5 \mathrm { x } 1 0 ^ { 4 }$ cycles). This suggests a correlation between the two phenomena, as shown in Fig. 5. Leakage current simulations in Fig. 8 show that increasing the trap density in the IL does not affect the leakage current, while an increase in trap density in the HZO layer leads to higher leakage. This reveals that leakage is driven predominantly by HZO traps and that traps generated during cycling are predominantly located in the IL where they do not contribute to the trap-assisted tunneling leakage current. The results in Figs. 4, 7 and 9 unveil the existence of a correlation (and interplay) between MW closure, [[Read delay]] and leakage current phenomena, which is summarized in Fig. 5(a-c). Under bipolar cycling, PS accelerates traps generation, which occurs primarily in the IL, Fig. 6(b). Electron trapping into generated IL traps leads to MW closure, Fig. 5(b), and explains the reduced MW recovery with [[Read delay]], which is due to slow traps. Once the IL is highly degraded $( \ 5 \mathrm { x l 0 ^ { 4 } }$ cycles), trap generation shifts in the HZO, explaining the large leakage increase, Fig. 5(c), which is driven predominantly by HZO traps.

![](images/151812ee827da8756bb6f43230953f963346ce7ac0edaa1d223d2b3d3326265c.jpg)

![](images/de5586733a42059d02b1a9e72bc91f7f75134502c1122a404ef1df7d09a2273d.jpg)  
Fig. 8. a) Leakage simulations performed using [[GinestraT M ]]software. Increasing the trap density in IL leads to minimal change in leakage current while increased trap density in the HZO leads to increase leakage current enabled by TAT.

![](images/aebc7e4041d826e4ffe2323927b8e33c174a7e7df6aa2588a75a38748284685a.jpg)

![](images/584930e41694ffc9ba0fd23a07b4e977778c78b022979e671166233b021ad86d.jpg)  
Fig. 9. a), b) the correlated degradation of MW, [[Gate leakage]] and MW recovery with [[Read delay]] under bipolar stress.

# VI. CONCLUSION

We have analyzed the correlation between memory window degradation, [[Read delay]] and [[Gate leakage]] in FEFETs (Fig 10). We show that MW degradation and [[Read delay]] are highly correlated. Traps leading to MW closure are primarily electron traps as evidenced by the significant change in the low $V _ { T }$ state and minimal change in the high $V _ { T }$ state under bipolar stress. The evolution of MW recovery with bipolar cycling indicates that these traps are slow electron traps which eventually lead to the MW not being recoverable even with large [[Read delay]]. Further, by comparing unipolar and bipolar cycling, we show that the slow electron trap generation is induced by polarization switching under bipolar stress. The [[Gate leakage]] does not change significantly until MW closure, indicating that these traps are localized mainly near the IL. This is confirmed by GinestraTM simulations that show the [[Gate leakage]] is driven by the traps in the FE layer and not the IL. Our results highlight the importance of IL engineering and minimizing the formation of slow (de)trapping defects in the IL to improve FEFET reliability.

![](images/5e5894c84c0ce8834f7e9af3631272fdfbb93f48a452854a3ae655df217172a3.jpg)  
Fig. 10. a,b) Schematic illustrating read-after-write delay and MW closure with bipolar cycling. With cycling, the MW degrades and the MW recovery with RWD also reduces

# ACKNOWLEDGEMENT

This work was supported by SUPREME, one of the seven SRC-DARPA JUMP2.0 centers. Fab was done at the IEN, supported by the NSF-NNCI program (ECCS- 1542174).

Andrea Padovani acknowledges the FAR 2023-2024 project of the “Enzo Ferrari” Engineering Department of the University of Modena and Reggio Emilia, Italy, for financial support.

# REFERENCES

[1] Asif Khan, Ali Keshavarzi, and Suman Datta. ”The future of ferroelectric field-effect transistor technology.” Nature Electronics 3, no. 10 (2020): 588-597.   
[2] Muller, J., T. S. B¨ oscke, S. M¨ uller, E. Yurchuk, P. Polakowski, J. Paul,¨ D. Martin et al. ”Ferroelectric hafnium oxide: A CMOS-compatible and highly scalable approach to future ferroelectric memories.” In 2013 IEEE International Electron Devices Meeting, pp. 10-8. IEEE, 2013.   
[3] Gong, Nanbo, and Tso-Ping Ma. ”A study of [[Endurance]] issues in HfO 2-based ferroelectric field effect transistors: Charge trapping and trap generation.” IEEE Electron Device Letters 39, no. 1 (2017): 15-18.   
[4] Cai, Zuocheng, Kasidit Toprasertpong, Mitsuru Takenaka, and Shinichi Takagi. ”HZO scaling and fatigue recovery in FeFET with low voltage operation: Evidence of transition from interface degradation to ferroelectric fatigue.” In 2023 IEEE Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits), pp. 1-2. IEEE, 2023.   
[5] Pesic, Milan, Franz PG Fengler, Stefan Slesazeck, Uwe Schroeder, Thomas Mikolajick, Luca Larcher, and Andrea Padovani. ”Root cause of degradation in novel HfO 2-based ferroelectric memories.” In 2016 IEEE International Reliability Physics Symposium (IRPS), pp. MY-3. IEEE, 2016.   
[6] Cai, Puyang, Tianxiang Zhu, Jiahui Duan, Zixuan Sun, Hao Li, Yongkang Xue, Zhiwei Liu et al. ”Deep understanding of reliability in Hf-based FeFET during bipolar pulse cycling: trap profiling for readafter-write delay and memory window degradation.” In 2022 International Electron Devices Meeting (IEDM), pp. 32-2. IEEE, 2022.   
[7] Passlack, Matthias, Nujhat Tasneem, Zheng Wang, Khandker A. Aabrar, Jae Hur, Hang Chen, Vincent D-H. Hou et al. ”Direct Quantitative Extraction of Internal Variables from Measured PUND Characteristics Providing New Key Insights into Physics and Performance of Silicon and Oxide Channel Ferroelectric FETs.” In 2022 International Electron Devices Meeting (IEDM), pp. 32-4. IEEE, 2022.   
[8] Kleimaier, Dominik, Halid Mulaosmanovic, Stefan Dunkel, Sven Beyer, ¨ Steven Soss, Stefan Slesazeck, and Thomas Mikolajick. ”Demonstration of a p-type ferroelectric FET with immediate read-after-write capability.” IEEE Electron Device Letters 42, no. 12 (2021): 1774-1777.   
[9] Gong, Nanbo, and Tso-Ping Ma. ”A study of [[Endurance]] issues in HfO2- based ferroelectric field effect transistors: Charge trapping and trap generation.” IEEE Electron Device Letters39.1 (2017): 15-18.   
[10] Pesic, Milan, Franz PG Fengler, Stefan Slesazeck, Uwe Schroeder, Thomas Mikolajick, Luca Larcher, and Andrea Padovani. ”Root cause of degradation in novel HfO 2-based ferroelectric memories.” In 2016 IEEE International Reliability Physics Symposium (IRPS), pp. MY-3. IEEE, 2016.   
[11] Yurchuk, Ekaterina, Johannes Muller, Stefan M ¨ uller, Jan Paul, Milan ¨ Pesiˇ c, Ralf van Bentum, Uwe Schroeder, and Thomas Mikolajick. ´ ”Charge-trapping phenomena in HfO 2-based FeFET-type nonvolatile memories.” IEEE Transactions on Electron Devices 63, no. 9 (2016): 3501-3507.   
[12] Tasneem, Nujhat, Zheng Wang, Hang Chen, Shimeng Yu, Winston Chern, and Asif Khan. ”Immediate read-after-write capability in ptype ferroelectric field-effect transistors and its evolution with fatigue cycling.” IEEE Transactions on Device and Materials Reliability 23, no. 1 (2023): 142-146.   
[13] Toprasertpong, Kasidit, Mitsuru Takenaka, and Shinichi Takagi. ”On the strong coupling of polarization and charge trapping in HfO2/Sibased ferroelectric field-effect transistors: overview of device operation and reliability.” Applied Physics A 128, no. 12 (2022): 1114.   
[14] Ravikumar, Priyankka, Park, Chinsung, Venkatesan, Prasanna, Afroze, Nashrah et al. ”First write pulse-induced interface damage in ferroelectric field-effect transistors” IEEE IIRW 2024.   
[15] [[GinestraT M ]]https://www.appliedmaterials.com/sg/en/semiconductor/ ginestra-software.html