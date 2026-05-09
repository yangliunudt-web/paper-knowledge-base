---
title: "A Compact Writing Scheme for the Reliability Challenges in 1T Multi-Level [[FeFET]] Array: Variation, Endurance, and Write Disturb"
authors:
  - "Yuejia Zhou"
  - "Hanyong Shao"
  - "Weiqin Huang"
  - "Runteng Zhu"
  - "Yihan Zhang"
  - "Ru Huang"
  - "Kechao Tang"
date: "2024-10-24"
year: "2024"
journal: "IEEE Electron Device Letters"
doi: "10.1109/LED.2024.3485803"
abstract: "Multi-level cell (MLC) [[ferroelectric]] FETs (FeFETs) face critical reliability challenges including variation, endurance and write disturb. In this work, we proposed an innovative solution to tackle all the three challenges within a compact writing scheme. Combining error correction, endurance recovery, and self-compensated writing, the proposed scheme achieves a > 6× reduction in error ratio (ER), a > 100 improvement in endurance, and $\\mathsf { a } > 7 \\mathsf { x }$ reduction in Vth shift. Reliable 2 bits/cell storage with high endurance of 108cycles and write-disturb immunity is experimentally demonstrated in the fabricated 1T FeFET array. This writing scheme is realized within a single work flow, and can be readily implemented in the operation circuits. Index Terms— Multi-level cell (MLC) FeFET, writing scheme, variation, endurance recovery, write disturb."
keywords:
  - "[[FeFET]]"
  - "[[Multi-level cell]]"
  - "[[Writing scheme]]"
  - "[[Reliability]]"
abstract_cn: "多级单元铁电FET面临关键可靠性挑战，包括变异性、耐久性和写入干扰。本文提出了一种创新方案，在紧凑的写入流程中同时解决这三个挑战。结合纠错、耐久性恢复和自补偿写入，该方案实现了错误率降低>6倍、耐久性提升>100倍、Vth漂移减少>7倍。在所制造的1T FeFET阵列中实验验证了具有10⁸次循环高耐久性和写入干扰免疫的可靠2比特/单元存储。该写入方案在单一工作流程内实现，可方便地部署于操作电路中。"
cite: "[1] Zhou et al. A Compact Writing Scheme for the Reliability Challenges in 1T Multi-Level [[FeFET]] Array: Variation, Endurance, and Write Disturb[J]. IEEE Electron Device Letters, 2024."
aiSum: "紧凑写入方案：错误率降低>6倍、耐久性提升>100倍、Vth漂移减少>7倍，1T FeFET阵列实现2比特/单元存储、10^8周期耐久性、写入干扰免疫。"
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
---

# A Compact Writing Scheme for the Reliability Challenges in 1T Multi-Level [[FeFET]] Array: Variation, Endurance, and Write Disturb

Yuejia Zhou , Graduate Student Member, IEEE, Hanyong Shao , Graduate Student Member, IEEE, Weiqin Huang, Runteng Zhu, Yihan Zhang , Member, IEEE, Ru Huang, Fellow, IEEE, and Kechao Tang , Member, IEEE

Abstract— Multi-level cell (MLC) [[ferroelectric]] FETs (FeFETs) face critical reliability challenges including variation, endurance and write disturb. In this work, we proposed an innovative solution to tackle all the three challenges within a compact writing scheme. Combining error correction, endurance recovery, and self-compensated writing, the proposed scheme achieves a > 6× reduction in error ratio (ER), a > 100 improvement in endurance, and $\mathsf { a } > 7 \mathsf { x }$ reduction in Vth shift. Reliable 2 bits/cell storage with high endurance of 108cycles and write-disturb immunity is experimentally demonstrated in the fabricated 1T FeFET array. This writing scheme is realized within a single work flow, and can be readily implemented in the operation circuits.

Index Terms— Multi-level cell (MLC) FeFET, writing scheme, variation, endurance recovery, write disturb.

# I. INTRODUCTION

fO2-BASED ferroelectric field effect transistor (FeFET) is a promising candidate for future non-volatile memory (NVM) due to its ultra-low power consumption, high speed, good scalability, and the ability for multi-level cell (MLC) storage [1], [2]. However, FeFET still faces reliability challenges, including device-to-device (D2D) and cycle-to-cycle (C2C) variation [3], poor endurance $( < 1 0 ^ { 6 }$ cycles [4]), and severe write disturb in the 1T FeFET array [5], which are especially

Received 7 October 2024; accepted 21 October 2024. Date of publication 24 October 2024; date of current version 26 November 2024. This work was supported in part by the National Key Research and Development Program of China under Grant 2022YFB4400300; in part by NSFC under Grant 62274003, Grant 61927901, and Grant 92164203; in part by the 111 Project under Grant B18001; and in part by the National Micro/Nano Fabrication Laboratory of Peking University. The review of this letter was arranged by Editor M. H. Park. (Corresponding author: Kechao Tang.)

Yuejia Zhou, Hanyong Shao, Weiqin Huang, and Runteng Zhu are with the School of Integrated Circuits, Peking University, Beijing 100871, China.

Yihan Zhang is with the Department of Electronic and Computer Engineering, Hong Kong University of Science and Technology, Hong Kong 999077, China.

Ru Huang and Kechao Tang are with the School of Integrated Circuits, Peking University, Beijing 100871, China, and also with Beijing Advanced Innovation Center for Integrated Circuits, Beijing 100871, China (e-mail: tkch@pku.edu.cn).

Color versions of one or more figures in this letter are available at https://doi.org/10.1109/LED.2024.3485803.

Digital Object Identifier 10.1109/LED.2024.3485803

critical for MLC devices. These challenges should all be addressed in the final memory macro, as any unresolved issue becomes the reliability bottleneck for applications. While most works focus on device process improvement to solve the reliability issues [6], [7], [8], recent years have witnessed a growing interest in the perspective of operation strategies, including target program [9], [10], endurance recovery [11], and $\mathrm { v } _ { \mathrm { w } } / 2$ or $\mathrm { V } _ { \mathrm { w } } / 3$ inhibit scheme [12]. However, in-depth study of array operation is still lacking and the reliability performance needs further improvement, especially for the write-disturb issue. In addition, existing works are limited in addressing each problem separately, while merging the proposed operation methods in a compact and mutually-compatible pattern is indispensable for practical implementation.

This work highlighted a compact writing scheme that addresses all the three reliability challenges simultaneously. A novel self-compensated writing scheme was proposed to effectively prevent the write disturb. In addition, we designed an auto-trigger rule that merges our proposed error correction and endurance recovery method within the writing work flow. This compact writing scheme demonstrates an overall reliability improvement, and can be readily implemented by a corresponding circuit design.

# II. PROPOSED WRITING SCHEME

The proposed writing scheme for 1T MLC FeFET array is described in Fig. 1. In the conventional writing approach, the entire array is first erased to 00 state and then programmed with an incremental pulse sequence row by row [13]. In our proposed scheme, the array is first set to middle state, followed by an alternative sequence of positive and negative pulses for writing. This setup results in alternating disturb bias stresses on unselected cells with opposite signs and similar magnitude. The impact of disturb stresses is thus self-compensating rather than accumulating, which effectively mitigates writedisturb (Fig. 1 (b)). In addition, error correction and endurance recovery approaches are also merged in the proposed writing scheme, as shown in Fig. 1 (a). A read-verify process is performed after writing a state, where the cells deviated from target states are corrected by incremental pulse attempts until the pass condition is met. Furthermore, if the pass condition

![](images/581c6b5082c3c7a0dd42392d092da6dfe237fcb5ed5e27c0d42cd6e133107e52.jpg)  
Fig. 1. (a) Proposed writing scheme for 1T MLC FeFET array, simultaneously addressing three key reliability issues. (b) Comparison of traditional writing scheme and the proposed writing scheme.

![](images/b3e966717c61f374a11b60873b55fb7494fe97704f99cccf089ac87744c53ef1.jpg)

![](images/eac3355672fc91af5e3cb50a4b6f15da2bc8c3c5dec8346ce41d353189b1177d.jpg)

![](images/c7b6460892037ee94d523d22feb1c9dc5f7e2bf192d9634da28960a9cc6364b3.jpg)  
Fig. 2. (a) SEM image of the fabricated $6 \times 6$ FeFET array. (b) Schematic, (c) cross-sectional HRTEM image and (d) the process flow of FeFET. (e) Statistical Id- $\cdot \vee _ { 9 }$ curves of the FeFET array.

cannot be met by the set number of attempts, it indicates the device is fatigued and automatically activates the endurance recovery treatment. This compact scheme solves the long standing “when to recover” problem, and guarantees MLC operation with low error rate for extended writing cycles.

# III. RESULTS AND DISCUSSION

# A. Fabrication and Basic Results of the FeFET Array

The 1T AND-type FeFET array and devices were prepared by gate-first process, as described in Fig. 2 (d). After active area patterning and native oxide removal, $\mathrm { H f } _ { 0 . 5 } \mathrm { Z r } _ { 0 . 5 } \mathrm { O } _ { 2 }$ (HZO) and $\mathbf { A l } _ { 2 } \mathbf { O } _ { 3 }$ layer is grown by atomic layer deposition (ALD) as FE and interlayer (IL), respectively. Fig. 2 (a) shows the SEM image of the fabricated $6 \times 6$ 1T AND FeFET array. FeFETs with gate length of 2 µm and width of 20 µm were fabricated in the array. The schematic and cross-sectional HRTEM image of the FeFET cell are shown in Fig. 2 (b) and (c), with clear interface and expected thickness of the gate structure.

The statistical memory property of the FeFET array is shown in Fig. 2 (e), where the individual and averaged $\mathrm { I _ { d } \mathrm { - } V _ { g } }$ curves for the four states of 36 devices are plotted. The threshold voltage $( \mathrm { V _ { t h } } )$ of each state is extracted at $\mathrm { I _ { d } } = 1 \ \mu \mathrm { A }$ , and a memory window (MW) of 0.85V is obtained.

# B. Error Correction and Endurance Recovery

The error correction process is depicted in Fig. 3 (a). Each write pulse is followed by a read-verify process. To reduce the read after write delay (RAWD) [9], a detrapping pulse of -2V and 1ms is applied, which could be potentially eliminated or shortened by device optimization [14]. Once the read $\mathrm { V _ { t h } }$ exceeds the set threshold, the error correction process is initiated. Incremental (decremental) correction pulse sequence with step of +0.1 V (-0.1 V) is applied for $\mathrm { V _ { t h } }$ higher (lower) than threshold, which shifts the $\mathrm { V _ { t h } }$ towards

![](images/dec6adda238b4684e676ed42735e7c84293e00957e203b659d0249382ac6462f.jpg)

![](images/86404fff084463cd802dbade61426ff9764db2eccff0dcbbb177eb3163db0fe0.jpg)  
Fig. 3. Error correction procedures. (a) Incremental or decremental pulse trains for correction. (b) Examples of error correction in different cases.

![](images/10347df45c4a01946c5cbab8b157ae496d0da7d483477c3bf114841982975183.jpg)

![](images/ab4a5007ac09c96f1b63fd61e45fe1f7531e2ec7232dc43976eb3208cc25eab9.jpg)

![](images/97d5ab08acdde05af6c3e4e9c106dab5edf3dd58ba417335cfb5794ba210fb41.jpg)

![](images/859a6140ac3b49e1cfbf96aabd563e1d786b5983464b7beff8fcb86cf15784a9.jpg)

![](images/92ce4c2dfef66eb3be6e290132baa8a7318e6804e44c0fd1ef2d36e7d5e5f87f.jpg)  
Fig. 4. Results of error correction on 10 FeFETs × 10 times of writing. States distribution for the (a) pristine device and (b) after $1 0 ^ { 3 }$ cycles. (c) ER with and without correction during cycling. (d) Average $\mathsf { V } _ { \mathsf { f h } }$ and σ during cycling. (e) ${ \mathsf { I } } _ { \mathsf { d } } { \mathsf { - } } { \mathsf { V } } _ { \mathsf { g } }$ curves for the four states after $\mathsf { 1 0 ^ { 6 } }$ cycles.

the correct range (Fig. 3 (b)) [15]. Note that the upper limit of the correction pulse number is set to 10, beyond which the correction is decided as failed and recovery is activated. This maximum pulse number is determined by considering the device performance, accuracy requirement, and time cost.

The statisic and fitted Gaussian distribution for the four $\mathrm { V _ { t h } }$ states from 10 devices × 10 times of writing is plot in Fig. 4 (a) and (b) to show the effectiveness of correction. The standard deviation (σ ) of $\mathrm { V _ { t h } }$ is comparable to previous work [10], and the error ratio (ER) is calculated from the area of the overlapped region of neighboring $\mathrm { V _ { t h } }$ distributions divided by the total area. The ER is reduced from 0.725% to 0.02% for pristine devices, and from 2.1% to 0.5% for those after $1 0 ^ { 3 }$ writing cycles. Note that the raw ER increases with cycling due to gradual device degradation, and reaches 6% after $1 0 ^ { 6 }$ cycles. With error correction, the ER is maintained $< 1 \%$ , signifying a 6× reduction, with $< 2 \times$ overhead in writing time (Fig. 4 (c)). The evolution of the average $\mathrm { V _ { t h } }$ and σ of each state with cycling are shown in Fig. 4 (d), where the $\mathrm { V _ { t h } }$ of the 11 state shifts significantly to positive while the σ of each state increases slightly. The positive $\mathrm { V _ { t h } }$ shift after cycling is considered the result of charge trapping, where the gradually accumulating trapped elelctrons screen the FE polarization [16]. This $\mathrm { V _ { t h } }$ shift combined with the increased σ may cause failure of error correction after $1 0 ^ { 6 }$ cycles, as shown in Fig. 4 (e).

![](images/1fdb46ef0d8c9cb07a3e4db44bca50961eeb5de05258ceadcc47b41a465487ca.jpg)

![](images/deecbb3fed8a3d72dc1428d24d0f0e2ffa8eae6c497807bda392bdb4d0e818f4.jpg)

![](images/522d542f05c88144a6ca2c000ce2698105425fbf59a5fc4bf31d1c5a42373bdc.jpg)

![](images/1ef564062e0b03c0008f5c611adaca87fa2ba58115bba02b4d41fee822c2fd4a.jpg)

![](images/d5b26edf33746d591bddb11881d25263be005f29f17fbf258115c0a1cc44a7e4.jpg)  
Fig. 5. (a) Waveform and (b) sustainable effect of endurance recovery. $( \mathsf { c } ) \mathsf { l } _ { \mathsf { d } } – \mathsf { V } _ { \mathsf { g } }$ curves at four states after cycling and recovery. (d) and (e) Accumulated endurance test showing a small ER over $1 0 ^ { 8 }$ cycles. (f) Measured stable retention up to 3000s and extrapolated to 10 years.

Endurance recovery is activated once error correction fails, as shown in Fig. 5 (a), and a single pulse of -9 V, 100 $\mu \mathrm { s }$ is used for recovery. Fig. 5 (b) shows the nearly identical cycling process before and after recovery, demonstrating full recovery effect of FeFET. The $\mathrm { I _ { d } \mathrm { - } V _ { g } }$ results in Fig. 5 (c) indicate that the 11 state shifts back to the pristine position after recovery. This is likely to originate from the electron detrapping by the negative recovery pulse. To further demonstrate the recovery effect, the accumulated endurance was measured with each $1 0 ^ { 6 }$ endurance cycles plus one recovery pulse as a recovery round, and the results are shown in Fig. 5 (d) and (e). After 100 recovery rounds (i.e., $1 0 ^ { 8 }$ cycles), the $\mathrm { V _ { t h } }$ of the four states shows no significant degradation. The ER is reduced from 6% to 0.8% after recovery, and further to 0.4% after error correction. This enables a reliable MLC operation with low ER over $1 0 ^ { 8 }$ cycles. It is also interesting that σ remains large after recovery, suggesting that the variation is not coupled with the endurance recovery dynamic. Fig. 5 (f) shows the measured stable retention of 3000 s and extrapolated to 10 years.

# C. Write Disturb Inhibit and Circuit Design

Fig. 6 (a) illustrates the detailed procedures of the proposed self-compensated writing scheme. In contrast to the conventional approach, the array is initialized to middle state, with $\mathrm { V _ { t h } }$ between 01 and 10 states. After that, self-compensated pulse trains are used to sequentially write the corresponding cells of the selected row, with $\mathrm { V } _ { \mathrm { w } } / 2$ applied on unselected bit lines (BLs) and word lines (WLs) as a general disturb inhibit scheme. Note that the cells with the same state in a row are simultaneously written, and our proposed correction-recovery method can be adopted in each write operation. After finishing writing one row, the next row is written in the same way until the entire array is completed. For a direct comparison, the two schemes were used to experimentally write a randomly generated state map into the same fabricated $6 \times 6$ FeFET array. After completely writing the entire array, the states of the first row are tested again to check the disturb, as shown in Fig. 6 (b). The conventional writing scheme

![](images/c18af5411b235985fdbd9a2ee3f926e03887530de28ae294224fc3e0415f4793.jpg)

![](images/2cd23eb89f2f0d40a22b40af8c08c6dc59743112b2aa07d6b4319508e381985a.jpg)

![](images/3b1aecf1ec45c11a05150528ce5dc2791ac7c00fa325f121a76ea6ee98561722.jpg)

![](images/de9c532fff57815ac30c4ea359b8ddc8e7d8d6a0032839febcef4c6c83d4e3aa.jpg)  
Fig. 6. (a) Schematic of the self-compensated and conventional writing scheme. (b) The random state map to experimentally write in the array. (c) Measured ${ \sf I _ { d } } \mathrm { - } { \sf V } _ { 9 }$ curves of the first row before and after array disturb.

![](images/8f1994dd8e2194a92814e9bc8501eeec3f5200d3a19105298bd3954a567f6b4a.jpg)  
Fig. 7. (a) Circuit design for the proposed writing scheme. (b) Comparison of the proposed writing scheme with current solutions.

<table><tr><td rowspan="4">(b)</td><td>Challenges</td><td>Current solutions</td><td>Proposed scheme</td><td>Performance</td></tr><tr><td>D2D/C2C variation</td><td>Target program[9]: Large time cost</td><td>Error correction: Small time cost</td><td>1.Error ratio reduced by &gt;6×2.Time cost &lt;2×</td></tr><tr><td>Poor endurance</td><td>Recovery[11]: Single bit</td><td>Recovery: 1. Multi bit 2. Combined with variation</td><td>1. 2 bits/cell 2. Improved from 108to &gt;108cycles</td></tr><tr><td>Write disturb</td><td>Vw/2 or Vw/3[12]: Accumulative disturb</td><td>Self-compensated scheme: Write disturb inhibit</td><td>Vth shift reduced from 0.15V to &lt;0.02V</td></tr></table>

results in severe $\mathrm { V _ { t h } }$ shift, especially for the 00 states due to the disturb by accumulating positive pulses. In contrast, our proposed scheme exhibits nearly no $\mathrm { V _ { t h } }$ shift, showing an unprecedented disturb-free performance, consistent with the self-compensation between alternating pulses (Fig. 6 (c)).

For future implementation, a corresponding circuit is designed with self-tracking and self-activating operation module, as illustrated in Fig. 7 (a). The $\mathrm { V _ { t h } }$ states output through a 2-bit ADC to a comparator, which initiates error correction when deviation is detected. The endurance recovery is auto-triggered when the counter of correction number reaches the set limit. These circuits are connected with the WL control module, to merge correction and recovery operation with the self-compensating writing scheme. Finally, the comparison of the proposed writing scheme with current solutions is summarized in Fig. 7 (b). The proposed scheme demonstrates significant improvement in all aspects of reliability.

# IV. CONCLUSION

In this work, we proposed a novel and compact writing scheme for 1T MLC FeFET array to address the reliability challenges of variation, endurance and write disturb simultaneously. The developed writing scheme enhances all these reliability metrics, enabling MLC operation with low ER, high endurance of $> 1 0 ^ { 8 }$ cycles, and immunity to write disturb. Supported with a corresponding circuit design, this work sets basis for the development of a highly reliable FeFET macro for practical memory applications.

# REFERENCES

[1] T. Ali, P. Polakowski, K. Kühnel, M. Czernohorsky, T. Kämpfe, M. Rudolph, B. Pätzold, D. Lehninger, F. Müller, R. Olivo, M. Lederer, R. Hoffmann, P. Steinke, K. Zimmermann, U. Mühle, K. Seidel, and J. Müller, “A multilevel FeFET memory device based on laminated HSO and HZO ferroelectric layers for high-density storage,” in IEDM Tech. Dig., Dec. 2019, pp. 28.7.1–28.7.4, doi: 10.1109/IEDM19573.2019.8993642.   
[2] K. Ni, J. Smith, H. Ye, B. Grisafe, G. B. Rayner, A. Kummel, and S. Datta, “A novel ferroelectric superlattice based multi-level cell nonvolatile memory,” in IEDM Tech. Dig., Dec. 2019, pp. 28.8.1–28.8.4, doi: 10.1109/IEDM19573.2019.8993670.   
[3] K. Ni, W. Chakraborty, J. Smith, B. Grisafe, and S. Datta, “Fundamental understanding and control of device-to-device variation in deeply scaled ferroelectric FETs,” in Proc. Symp. VLSI Technol., Jun. 2019, pp. T40–T41, doi: 10.23919/VLSIT.2019.8776497.   
[4] Y. Zhou, Z. Liang, W. Luo, M. Yu, R. Zhu, X. Lv, J. Li, Q. Huang, F. Liu, K. Tang, and R. Huang, “Ferroelectric and interlayer co-optimization with in-depth analysis for high endurance FeFET,” in IEDM Tech. Dig., Dec. 2022, pp. 6.2.1–6.2.4, doi: 10.1109/IEDM45625.2022.10019465.   
[5] Z. Jiang, Z. Zhao, S. Deng, Y. Xiao, Y. Xu, H. Mulaosmanovic, S. Duenkel, S. Beyer, S. Meninger, M. Mohamed, R. Joshi, X. Gong, S. Kurinec, V. Narayanan, and K. Ni, “On the feasibility of 1T ferroelectric FET memory array,” IEEE Trans. Electron Devices, vol. 69, no. 12, pp. 6722–6730, Dec. 2022, doi: 10.1109/TED.2022.3216819.   
[6] C.-Y. Liao, Z.-F. Lou, C.-Y. Lin, A. Senapati, R. Karmakar, K.-Y. Hsiang, Z.-X. Li, W.-C. Ray, J.-Y. Lee, P.-H. Chen, F.-S. Chang, H.-H. Tseng, C.-C. Wang, J.-H. Tsai, Y.-T. Tang, S. T. Chang, C. W. Liu, S. Maikap, and M. H. Lee, “Superlattice [[HfO2]]-ZrO2 based ferro-stack HfZrO2 FeFETs: Homogeneous-domain merits ultra-low error, low programming voltage 4 V and robust endurance 109 cycles for multibit NVM,” in IEDM Tech. Dig., Dec. 2022, pp. 36.6.1–36.6.4, doi: 10.1109/IEDM45625.2022.10019369.   
[7] M. Hoffmann, A. J. Tan, N. Shanker, Y.-H. Liao, L.-C. Wang, J.-H. Bae, C. Hu, and S. Salahuddin, “Write disturb-free ferroelectric FETs with non-accumulative switching dynamics,” IEEE Electron Device Lett., vol. 43, no. 12, pp. 2097–2100, Dec. 2022, doi: 10.1109/LED.2022.3212330.   
[8] M.-C. Nguyen, S. Kim, K. Lee, J.-Y. Yim, R. Choi, and D. Kwon, “Wakeup-free and endurance-robust ferroelectric fieldeffect transistor memory using high pressure annealing,” IEEE Electron Device Lett., vol. 42, no. 9, pp. 1295–1298, Sep. 2021, doi: 10.1109/LED.2021.3096248.

[9] H. Zhou, J. Ocker, A. Padovani, M. Pesic, M. Trentzsch, S. Dünkel, H. Mulaosmanovic, S. Slesazeck, L. Larcher, S. Beyer, S. Müller, and T. Mikolajick, “Application and benefits of target programming algorithms for ferroelectric HfO2 transistors,” in IEDM Tech. Dig., Dec. 2020, pp. 18.6.1–18.6.4, doi: 10.1109/IEDM13553. 2020.9371975.   
[10] T. Soliman, S. Chatterjee, N. Laleni, F. Müller, T. Kirchner, N. Wehn, T. Kämpfe, Y. S. Chauhan, and H. Amrouch, “First demonstration of [[in-memory computing]] [[crossbar]] using multi-level cell FeFET,” Nature Commun., vol. 14, no. 1, p. 6348, Oct. 2023, doi: 10.1038/s41467-023- 42110-y.   
[11] C.-H. Wu, J. Liu, X.-T. Zheng, Y.-M. Tseng, M. Kobayashi, V. P.-H. Hu, and C.-J. Su, “Robust recovery scheme for MFIS-FeFETs at optimal timing with prolonged endurance: Fast-unipolar pulsing (100 ns), nearly zero memory window loss (0.02 %), and self-tracking circuit design,” in IEDM Tech. Dig., Dec. 2023, pp. 1–4, doi: 10.1109/IEDM45741.2023.10413819.   
[12] K. Ni, X. Li, J. A. Smith, M. Jerry, and S. Datta, “Write disturb in ferroelectric FETs and its implication for 1T-FeFET AND memory arrays,” IEEE Electron Device Lett., vol. 39, no. 11, pp. 1656–1659, Nov. 2018, doi: 10.1109/LED. 2018.2872347.   
[13] M. Trentzsch, S. Flachowsky, R. Richter, J. Paul, B. Reimer, D. Utess, S. Jansen, H. Mulaosmanovic, S. Müller, S. Slesazeck, J. Ocker, M. Noack, J. Müller, P. Polakowski, J. Schreiter, S. Beyer, T. Mikolajick, and B. Rice, “A 28 nm HKMG super low power embedded NVM technology based on ferroelectric FETs,” in IEDM Tech. Dig., Dec. 2016, pp. 11.5.1–11.5.4, doi: 10.1109/IEDM.2016. 7838397.   
[14] M. Hoffmann, A. J. Tan, N. Shanker, Y.-H. Liao, L.-C. Wang, J.-H. Bae, C. Hu, and S. Salahuddin, “Fast read-after-write and depolarization fields in high endurance n-type ferroelectric FETs,” IEEE Electron Device Lett., vol. 43, no. 5, pp. 717–720, May 2022.   
[15] Y. Zhou, H. Shao, R. Zhu, W. Luo, W. Huang, L. Shan, R. Huang, and K. Tang, “Hybrid-FE-Layer FeFET with high linearity and endurance toward on-chip [[CIM]] by array demonstration,” IEEE Electron Device Lett., vol. 45, no. 2, pp. 276–279, Feb. 2024, doi: 10.1109/LED.2023.3346030.   
[16] E. Yurchuk, J. Müller, S. Müller, J. Paul, M. Pešic, R. van Bentum, ´ U. Schroeder, and T. Mikolajick, “Charge-trapping phenomena in HfO2-based FeFET-type nonvolatile memories,” IEEE Trans. Electron Devices, vol. 63, no. 9, pp. 3501–3507, Sep. 2016, doi: 10.1109/TED.2016.2588439.