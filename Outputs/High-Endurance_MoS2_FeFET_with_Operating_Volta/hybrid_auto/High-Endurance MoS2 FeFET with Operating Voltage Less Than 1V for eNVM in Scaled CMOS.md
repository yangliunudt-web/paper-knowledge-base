---
title: "High-Endurance FeFET with Operating Voltage Less Than 1V for eNVM in Scaled CMOS Technologies"
authors:
  - "Tsung-En Lee"
  - "Hung-Li Chiang"
  - "Chih-Yu Chang"
  - "Yuan-Chun Su"
  - "Shu-Jui Chang"
  - "Jui-Jen Wu"
  - "Bo-Jiun Lin"
  - "Jer-Fu Wang"
  - "Shu-Chih Haw"
  - "Shang-Jui Chiu"
  - "He-Liang Ching"
  - "Yan-Gu Lin"
  - "Wei-Sheng Yun"
  - "Chen-Feng Hsu"
  - "Hengyuan Lee"
  - "Tung-Ying Lee"
  - "Matthias Passlack"
  - "Chao-Ching Cheng"
  - "Chih-Sheng Chang"
  - "H.-S. Philip Wong"
  - "Wen-Hao Chang"
  - "Meng-Fan Chang"
  - "Yu-Ming Lin"
  - "Iuliana P. Radu"
date: "2025-01-01"
year: "2025"
journal: "Nature Electronics"
abstract: "For the first time, we demonstrate a transition metal dichalcogenide (TMD) Ferroelectric\\"
abstract_cn: "我们首次展示了过渡金属二硫属化物铁电场效应晶体管，具有超高耐久性（测量值>10^12）和超过10年的保持时间。该器件由原子层沉积的超薄Hf-Zr基铁电层组成，沉积在AlO_x\\"
keywords:
  - "[[FeFET]]"
  - "[[MoS₂]]"
  - "[[HfO₂]]"
  - "[[High endurance]]"
cite: "[1] Lee T E, Chiang H L, Chang C Y, et al. High‑endurance MoS2 FeFET with operating\\"
aiSum: "单层MoS₂ FeFET：超薄HZO（2.5nm）实现<1V工作电压、>10^12次耐久性、>10年保持时间，兼容CMOS后端工艺，适用于先进节点嵌入式存储。"
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
  - "[[HfO2]]"
---

# High-Endurance $\mathrm{MoS}_2$ FeFET with Operating Voltage Less Than 1V for eNVM in Scaled CMOS Technologies

Tsung-En Lee $^{1+*}$ , Hung-Li Chiang $^{1+}$ , Chih-Yu Chang $^{2+}$ , Yuan-Chun Su $^{1,3}$ , Shu-Jui Chang $^{1}$ , Jui-Jen Wu $^{1}$ , Bo-Jiun Lin $^{1}$ , Jer-Fu Wang $^{1}$ , Shu-Chih Haw $^{4}$ , Shang-Jui Chiu $^{4}$ , He-Liang Ching $^{4}$ , Yan-Gu Lin $^{4}$ , Wei-Sheng Yun $^{1}$ , Chen-Feng Hsu $^{1}$ , Hengyuan Lee $^{1}$ , Tung-Ying Lee $^{1}$ , Matthias Passlack $^{1}$ , Chao-Ching Cheng $^{1}$ , Chih-Sheng Chang $^{1}$ , H.-S. Philip Wong $^{1}$ , Wen-Hao Chang $^{3}$ , Meng-Fan Chang $^{1}$ , Yu-Ming Lin $^{2}$ , and Iuliana P. Radu $^{1*}$

<sup>1</sup>Corporate Research, Taiwan Semiconductor Manufacturing Company, Hsinchu, Taiwan *email: teleea@tsmc.com; iradu@tsmc.com

$^{2}$ Pathfinding, Taiwan Semiconductor Manufacturing Company, Hsinchu, Taiwan

$^{3}$ Department of Electrophysics, National Yang Ming Chiao Tung University, Hsinchu, Taiwan

$^{4}$ National Synchrotron Radiation Research Center, Hsinchu, Taiwan.

+These authors contributed equally.

Abstract - For the first time, we demonstrate a transition metal dichalcogenide (TMD) Ferroelectric Field-Effect Transistor (FeFET) with ultra-high endurance $(>10^{12}$ measured) and retention time exceeding 10 years. The devices consist of an ultrathin Hf-Zr-based (HZO) ferroelectric deposited by ALD on a stack of $\mathrm{AlO_x / MoS_2}$ with process temperature $< 250^{\circ}\mathrm{C}$ . By using a $2.5\mathrm{nm}$ HZO layer and a monolayer (1L) $\mathrm{MoS_2}$ , a record-low operating voltage $< 1\mathrm{V}$ is reported thanks to excellent gate control. The device fabrication is compatible with Back-End-of-Line (BEoL) processes in advanced CMOS technologies. Array-level projections show that a sufficient memory window is maintained at a supply voltage $(\mathrm{V_{DD}})$ of 1V. This device has promise for high-density memory embedded in scaled CMOS technology nodes.

# I. INTRODUCTION

Ferroelectric memories with HZO mixtures are promising candidates for non-volatile memories (NVM), due to their low operating power, fast write speed, scalability, and CMOS compatibility. Unlike the destructive read in Ferroelectric Random-Access Memory (FeRAM) [1] and the insufficient read current ( $\sim 1\mathrm{nA}$ ) in Ferroelectric Tunneling Junction (FTJ) [2], FeFET shows a high enough read current and excellent retention for an eNVM in CMOS technologies. However, FeFET faces challenges such as high switching voltage ( $>2\mathrm{V}$ ) limited by the degraded ferroelectricity at ultrathin HZO ( $<4\mathrm{nm}$ ) [3], and relatively low endurance ( $10^{6} \sim 10^{9}$ ) caused by trap generation in the interfacial layer (IL) under a high coercive electric field ( $\sim 1\mathrm{MV/cm}$ ) [3]. These issues make it difficult to integrate FeFET in advanced CMOS logics.

Previously, we demonstrated BEoL-compatible TMD transistors with nearly ideal subthreshold swing (S.S.) have been reported using an interlayer and an and HZO based dielectric [4]. The low S.S. stems from the negligible quantum capacitance in the monolayer $\mathrm{MoS}_2$ channel and relatively low $\mathrm{D}_{\mathrm{it}}$ between the IL and the self-terminated $\mathrm{MoS}_2$ in those devices. In this paper, we demonstrate an FeFET operation on the 1L-MoS $_2$ channel by using a conceptually similar stack but where the IL is PVD $\mathrm{AlO_x}$ and the ferroelectric layer is ALD HZO. The stoichiometry and the thickness for the HZO/ $\mathrm{AlO_x}$ stack are appropriately designed. The endurance is found to be higher than that in Si- based FeFETs. The mechanism for the improved endurance is not understood but several elements could play a role as discussed further down. Switching voltage reduction is achieved by decreasing the thickness of the ferroelectric layer to about $2.5\mathrm{nm}$ . The operating voltage promised to be compatible with embedded memory for multi-level caches in scaled CMOS logics (Fig. 1) [3, 5-10]. Array-level analysis is used to access the feasibility of building

64k-bit arrays in CMOS BEoL without cell transistors, resulting high array efficiency (AE), as sketched in Fig. 2.

# II. EXPERIMENT AND DEVICE CHARACTERISTICS

# A. Advantage of MoS $_2$ FeFET

The formation of ultra-thin ferroelectric HZO layers is limited by surface energy of IL in Metal/ Ferroelectric/ Insulator/ Semiconductor (MFIS) structures [11]. The poor endurance of Si FeFET is attributed to dielectric breakdown in $\mathrm{SiO_x}$ . In our dual-gate 1L-MoS $_2$ FeFET, an extremely flat IL $(\mathrm{AlO_x})$ with $\mathrm{k} > 6$ on 2D van der Waals (vdW) interface is proposed to stabilize the ferroelectricity of ultra-thin HZO and suppress the formation of dangling bonds at the IL/ $\mathrm{MoS}_2$ interface under stress (Fig.3).

# B. vdW interface and nanocrystalline phase

The extracted surface roughness of $1\mathrm{L - MoS}_2$ interface after the $\mathrm{AlO_x}$ deposition is comparable to that before the $\mathrm{AlO_x}$ deposition, validated by X-Ray Reflectometry (XRR) (Fig. 4). This implies the interaction between $\mathrm{AlO_x}$ and the $1\mathrm{L - MoS}_2$ channel is negligible. The HZO is then grown on $\mathrm{AlO_x}$ by Atomic Layer Deposition (ALD) at $250^{\circ}\mathrm{C}$ . No obvious signals from the bonds of Mo-O or S-O in spectra of Mo 3d and S 2p are observed by Xray Photoelectron Spectroscopy (XPS) (Fig. 5), indicating that $\mathrm{AlO_x}$ is a good buffer layer to resist the oxygen diffusion. A nearly S-terminated channel can be maintained after the gate-stack process and result in the robust endurance. The crystalline structures in HZO of $6\mathrm{nm}$ and $2.5\mathrm{nm}$ on $\mathrm{AlO_x / 1L - MoS_2}$ are analyzed by high-resolution Transmission Electron Microscope (TEM) (Fig. 6). We further evaluated the nanocrystalline phase of 6 and $2.5\mathrm{nm}$ HZO by X-ray Absorption Spectroscopy (XAS), as shown in Fig. 7. Though the polycrystal property reduces from $20\%$ to $1\%$ as the HZO is scaled to $2.5\mathrm{nm}$ , a considerable composition of o-phase and t-phase is remained still. In the nanocrystalline $2.5\mathrm{nm}$ HZO film, the crystal-field split of $\mathrm{e_g}$ and $\mathrm{t_{2g}}$ reveals the existence of o-phase and t-phase over the entire sample [12].

# C. Optimum operation voltage for power reduction

Under the same sweeping range of $\pm 1.5\mathrm{V}$ , the $\mathrm{V_{TH}}$ of low- $\mathrm{V_{TH}}$ state (LVTS) of FeFET with $2.5\mathrm{nm}$ HZO is positive, which enables lower off current $(\mathrm{I_{OFF}})$ at $\mathrm{V_{TG}} = 0\mathrm{V}$ (Fig. 8). Compared with $6\mathrm{nm}$ HZO, higher $\mathrm{V_{TH}}$ at high- $\mathrm{V_{TH}}$ state (HVTS) in $2.5\mathrm{nm}$ HZO is acquired and enlarge the memory window (MW). To separate the contribution of program and erase in MW, the program voltage $(\mathrm{V_{PRG}})$ is swept at fixed erase voltage $(\mathrm{V_{ERS}})$ and vice versa, as shown in Fig. 9(a). At read voltage $(\mathrm{V_{READ}}) = 0.4\mathrm{V}$ , the ratio of read current $(\mathrm{I_{READ}})$ at LVTS and that at HVTS is

improved by applying higher $\mathrm{V_{PRG}}$ and $\mathrm{V_{ERS}}$ , separately (Fig. 9(b)). This means our $\mathrm{1L - MoS_2}$ FeFET with low EOT enables an adequate hole density during erase operations, which is a concern in oxide semiconductor FeFETs [6]. In ultra-thin HZO $(<  4\mathrm{nm})$ MW is dominated by $\mathrm{V}_{\mathrm{C}}$ . An excessive MW needs higher $\mathrm{V_{WRITE}}$ and limits the $\mathrm{V_{DD}}$ scaling in advanced technologies. Thanks to the dual-gate structure, MW and $\mathrm{I_{off}}$ at LVTS can be also adjusted by varying the back-gate bias $(\mathrm{V_{BG}})$ , as shown in Fig. 10. $\mathrm{V_{TH}}$ at both HVTS and LVTS can be increased. With negative $\mathrm{V_{BG}}$ $\mathrm{I_{off}}$ is reduced by $0.2\times$ and consumes lower standby power as embedded in CMOS logics (Fig. 11).

# D. Fast writing speed, high endurance and long retention

The setup of measurements for P-V loops and fast I-V curves of FeFET is illustrated in Fig. 12. To reduce the RC delay from the parasitic resistance during the testing, positive $\mathrm{V_{BG}}$ is applied in the fast I-V testing. Here, the minimum pulse width of 30ns is studied, followed by read pulse for the MW extraction. The P-V loops of 1L-MoS $_2$ FeFETs at 1 MHz are shown in Fig. 13, which consist with the o/t phase observed in 2.5nm HZO (Fig. 4). Even annealing at temperature $>400^{\circ}\mathrm{C}$ is performed, the ferroelectricity in most FeFETs or MFIS capacitors still quenches as the HZO thickness is lower than 7nm, as shown in Fig. 14 [3,14,15,17]. Though some reported FeRAMs or FTJs show clear polarization at 4nm, our annealing-free 2.5nm HZO on $\mathrm{MoS}_2$ can still achieve a sufficient $2\mathrm{P_r}$ of $\sim 8\mu \mathrm{C} / \mathrm{cm}^2$ . To evaluate the sweeping speed of the dipoles in the proposed HZO layer, the fast I-V measurements with varying pulse time $(\mathrm{t_{pulse}})$ from 100 $\mu$ s to 30ns are then applied to the FeFET, as shown in Fig. 15. No degradation in MW is observed with faster program/ erase speed at $\mathrm{t_{pulse}} = 30$ ns. At $\mathrm{t_{pulse}} < 1\mu$ s, higher MW is extracted (Fig. 16), which may be resulted from the trap relaxation/ capture time higher than 1 $\mu$ s [3].

The endurance test is shown in Fig. 17. After applying the bipolar switching $10^{12}$ cycles at $\mathrm{V}_{\mathrm{WRITE}} = 1\mathrm{V}$ and $\mathrm{t}_{\mathrm{pulse}} = 100\mathrm{ns}$ , there is no significant degradation in MW up to $10^{12}$ cycles. To understand the failure mechanism from the cycling stress, S.S. (Fig. 18(a)) and $2\mathrm{Pr}$ (Fig. 18(b)) are extracted, respectively. S.S. dominated by the interface property maintains in $\sim 75\mathrm{mV / dec}$ at HVTS and $110\mathrm{mV / dec}$ at LVTS after the cycling stress. This implies that there is almost no stress-induced $\mathrm{D}_{\mathrm{it}}$ in the S-terminated $\mathrm{MoS}_2$ channel (Fig. 5). $2\mathrm{Pr}$ degradation is observed after the cycling stress, which means the endurance is dominated by the ferroelectricity fatigue in the HZO layer. Fortunately, the coercive voltage $(\mathrm{V_c})$ still sustains at the similar value. From the extrapolation to the point with $50\%$ $2\mathrm{Pr}$ remained, an endurance cycle $>10^{18}$ can be projected. Unlike the poor endurance $(< 10^{6})$ of FeFET or MFIS capacitors ascribed to the dielectric breakdown and/ or the ferroelectricity degradation [3] (Fig. 19), the combination of $\mathrm{AlO_x}$ with a higher dielectric constant and the near vdW interface of $\mathrm{MoS}_2$ channel boost the endurable stress time $(\mathrm{t}_{\mathrm{stress}})$ to $>10^{5}\mathrm{s}$ , without the recovery for the ferroelectricity at large bias [3]. Owing to the successful thickness reduction of HZO on $\mathrm{AlO_x}$ , the switching voltage can be reduced to $< 1\mathrm{V}$ . In addition, our MW can be retained up to 10 years from the extrapolation of HVTS and LVTS at $10^{4}\mathrm{s}$ (Fig. 20), proving the non-volatile characteristics.

# III. ARRAY-LEVEL ANALYSIS

# A. Considerations for write/read in FeFET-only array

The typical BEoL FeFETs with oxide semiconductor channels [6] have negative $\mathrm{V_{TH}}$ and high leakage current at zero gate bias. Either access transistors for 1T-1FeFET array (Fig. 21 (a)) or negative gate bias is needed to suppress the sneak current during

the read/ write operation and the standby power and consumes the footprint in FEoL. Our proposed FeFET of $\mathrm{MoS}_2$ channel with stable positive $\mathrm{V}_{\mathrm{TH}}$ exhibits low leakage current at $\mathrm{V_G} = 0$ , which enable an FeFET-only array without transistors, as shown in Fig. 21(b). Based on the device characteristics, the schemes for read/ write operations are shown in Table I. The $\mathrm{V}_{\mathrm{WRITE}} / 2$ write disturb inhibition scheme is applied to the FeFET-only array. To evaluate the write-disturb rate in the unselected cells bias at $\mathrm{V}_{\mathrm{WRITE}} / 2$ , DC I-V curves with gate bias from 0 to $0.5\mathrm{V} / -0.25\mathrm{V}$ repeated 20 times are examined. No $\mathrm{V}_{\mathrm{TH}}$ shift is observed as shown in Fig. 9 (a). Regarding the integration time (50ms) in the DC measurements and the write pulse time (30ns), the write-disturb rate should be $\ll 30$ ppb for both program operations and erase operations.

For read operations, $\mathrm{V}_{\mathrm{READ}}$ is designed at $0.4\mathrm{V}$ to ensure a read disturb rate lower than the write-disturb rate. The corresponding MW is $0.23\mathrm{V}$ and gives a sufficient read current $(\mathrm{I}_{\mathrm{READ}})$ difference $(\sim 10\times)$ between $\mathrm{I}_{\mathrm{READ}}$ at LVTS and that at HVTS, as shown in Fig. 9 (a). To ensure this satisfactory $\mathrm{I}_{\mathrm{READ}}$ ratio, the sneak current in the same bit line is further evaluated. With a difference of $>100\times$ between $\mathrm{I}_{\mathrm{READ}}$ at HVTS and the $\mathrm{I}_{\mathrm{OFF}}$ at LVTS, 64 word lines are allowed in a bank. A 64k-bit array consisting of four $64\times 256$ banks is adopted to the array-level evaluation.

# B. Read margin analysis and area benefit

To understand the benefits to the read margin from the proposed device in the array level, we investigate the impact from $\mathrm{V_{TH}}$ variability. The nanocrystalline HZO layer and the monolayer $\mathrm{MoS}_2$ with process temperature $< 250^{\circ}\mathrm{C}$ in BEoL still exhibits acceptable variations (e.g., ferroelectricity related to HZO granularity and write instability [13], work function affected by gate-metal granularity [18], trapping and de-trapping during cyclic operation [19]), as shown in Fig.22. From the statistical data, lower $\mathrm{V_{TH}}$ variability is observed in devices at HVTS. Regarding the MW of $0.23\mathrm{V}$ at $\mathrm{V_{PRG}} = 1.0\mathrm{V}$ , a difference of $\mathrm{I_{READ}}$ of $\sim 1\mu \mathrm{A}$ can be still obtained with a ppm-level bit-error rate, which is capable to be dealt by Error correction code (ECC) circuits. This current level also allows the dedicated sense amplifier (Fig. 23(a)) to differentiate $\mathrm{I_{READ}}$ at HVTS and that at LVTS with around 10ns, as shown in Fig. 23(b).

To further understand the macro-level benefits from the FeFET-only array enabled by our $\mathrm{MoS}_2$ FeFET, the comparison to a typical 1T-1FeFET array is shown in Fig. 24. By removing the access transistors in FEoL, the AE is improved from $57.2\%$ to $69.7\%$ at a cost of the limited word line number in a bank. The separated four sub-banks need additional bit-line drivers, sense amplifiers, and multiplexers, while the periphery can be implemented under the FeFET-only array. Although only 64 cells are allowed to share one bit line, an area reduction of $21.4\%$ can be still acquired in terms of the total macro size, including the cell area and the peripheral circuits.

# IV. CONCLUSION

We demonstrated here the first FeFET with a 1L-MoS $_2$ channel with deposited gate stack containing ultrathin HZO. This enables a switching voltage lower than 1.0V. The obtained memory window of 0.23V is compatible with the low supply voltage of scaled CMOS technologies. The gate stack and the interface quality enable high endurance of at least $10^{12}$ (projected endurance $>10^{18}$ ), satisfying the requirement for buffer memory in the cache hierarchy. Since the fabrication flow is BEoL-compatible and devices have positive $\mathrm{V_{TH}}$ , an FeFET-only array is proposed as a possible application in high-density eNVM to improve the power efficiency in advanced logics.

[1] K. Tahara et al., VLSI, 978 (2021). [2] H.-L. Chiang et al., VLSI, 361 (2022). [3] Z. Cai et al., VLSI, T5-2 (2023). [4] T.-E. Lee et al., IEDM, 154 (2022). [5] Y. Zhou et al., IEDM, 118 (2022). [6] Z. Lin et al., VLSI, 391 (2022). [7] C.-Y. Liao et al., VLSI, 393 (2022). [8] X. Wang et al., VLSI, T5_4 (2023). [9] C.-K. Chen et al., IEDM, 114 (2022). [10] Y.-R. Chen et al., VLSI, T5-3 (2023). [11] Y.-T. Tang et al., VLSI, 45 (2018). [12] S.S. Cheema et al., Nature, 604, 65 (2022). [13] F. Huang et al., VLSI, T7_3 (2023). [14] Y.-F. Chen et al., EDL, 43, 208 (2022). [15] J. Hwang et al., EDL, 41, 1193 (2020). [16] S. Dutta et al., IEDM (2021). [17] Z. Lin et al., IEDM (2021). [18] R. Brown et al., EDL, 31, 1199 (2010). [19] K. Toprasertpong et al., IEDM, 570 (2019).

![](images/6b2ff3be737ad6aa5ba9691376fa0158f8fe6f17f3e6a662b4452a87fa75f7ea.jpg)  
Fig. 1 Candidates of HZO-based FeFETs for eNVM in advanced CMOS. There was no solution to achieve endurance over $10^{12}$ cycles and $\mathrm{V_{DD}}$ below 1V.

![](images/3a9fccfc4e5c015e71e46b1c17f92f89455275aad12c339c0c051d615abc8404.jpg)  
Fig. 2 FeFET array in BEoL without cell transistors and negative bias for higher array efficiency. Devices with positive $\mathrm{V_{TH}}$ and $\mathrm{I_{Cell} / I_{Leak}} > 100\mathrm{x}$ is needed.   
Fig. 3 Device architecture of monolayer $\mathrm{MoS}_2$ FeFET with ultra-thin HZO layer $(<  4\mathrm{nm})$ and the process flow with highest temperature lower than $250^{\circ}\mathrm{C}$

![](images/15ca8968f9cad0bd718f2b67c7207eaded807dd83290ea54030a36551b84a119.jpg)  
Fig. 4 XRR analysis of $\mathrm{MoS}_2$ before and after the $\mathrm{AlO_x}$ deposition. There is no impact on $\mathrm{MoS}_2$ from the IL formation.

![](images/3c30e246758a204783249307e3ed2fbf5433b73ac36c583c2c2ba6573cf9bfee.jpg)  
Fig. 5 XPS analysis of Mo 3d spectra. An S-terminated $\mathrm{MoS}_2$ channel is maintained after the deposition of HZO/ $\mathrm{AlO_x}$

![](images/15395f56567ec63e14f2b8196a7e730ee86b5e75b231f8ca1c17f425f5c3341e.jpg)  
Fig. 6 High-resolution TEM images of (a) $6\mathrm{nm}$ HZO of polycrystal and (b) $2.5\mathrm{nm}$ HZO of nanocrystal on $\mathrm{AlO_x / 1L - }$ $\mathrm{MoS_2}$

![](images/05001717a501e65a33e411d64f0184680c73f668cb49606f340d951bbf20088f.jpg)  
Fig. 7 XAS spectra at the oxygen K edge for $6\mathrm{nm}/2.5\mathrm{nm}$ HZO on $\mathrm{AlO_x / 1L - }$ $\mathrm{MoS}_2$ stacks, suggesting the o/t-phase at the presented $2.5\mathrm{nm}$ HZO on $\mathrm{MoS}_2$ channel.

![](images/e84f7e1912993c301d94a1f949510d879b05fb856bd66d9345cdcc48e00f7dd0.jpg)  
Fig. 8 Transfer curves of $6\mathrm{nm}/2.5$ nm HZO. Scaling HZO thickness down to $2.5\mathrm{nm}$ is effective to reduce VWRITE.

![](images/9c8c40600f3d562f80074082c15aa493d9a7c282d8f21285322b1d596a46891f.jpg)  
Fig. 9 (a) Transfer curves of TiN/ $2.5\mathrm{nm}$ HZO/ $\mathrm{AlO_x / 1L - MoS_2}$ FeFETs at varying $\mathrm{V_{PRG}}$ and $\mathrm{V_{ERS}}$ . (b) $\mathrm{I_{on} / I_{off}}$ ratio at fixed $\mathrm{V_{PRG}}$ and $\mathrm{V_{ERS}}$ . This 1L-MoS $_2$ n-FeFET can provide sufficient electron and hole carrier density for both program and erase.

![](images/9f673c7abe6959058940a668e87521880a954ba6a152b12ead846a64649ae548.jpg)

![](images/7fd72967678f3f453ac88742122696ab3b09ed7a6d9ff6492623f6b7aeb9da96.jpg)  
Fig. 10 Transfer curves of $\mathrm{MoS}_2$ FeFETs at $\mathrm{V_{BG} / EOT}$ ranging from 1.5 to $-1.5\mathrm{MV / cm}$

![](images/e88d3fd242547ad020077e527cf5b41f04d57fa51696e042c416cbffc321c516.jpg)  
Fig. 11 Standby $\mathrm{I_{off}}$ of $\mathrm{MoS}_2$ FeFETs. $80\%$ $\mathrm{I_{off}}$ reduction at LVTS by applying $\mathrm{V_{BG}}$ for lower standby power reduction.

![](images/caec7e871778496a84b94841e281384011154cc849bb30e080bddd1f732a71e3.jpg)  
Fig. 12 Measurement setup of P-V and fast I-V for $\mathrm{MoS}_2$ FeFETs. S/D contacts are connected for P-V measurement. Pulse width of program and erase ranges from 100ns to 30ns. Positive $\mathrm{V_{BG}}$ is applied to reduce $\mathrm{R_{ch}}$ , $\mathrm{R_{spacer}}$ and $\mathrm{R_{csd}}$ for lowering the RC delay.

![](images/bd8e6a38abb5960c3aee0fc8d597ffb390474ee32f7ac447ad53f86ae5ae36c3.jpg)  
Fig. 13 P-V loops of $2.5\mathrm{nm}$ HZO on $1\mathrm{nm}$ $\mathrm{AlO_x / 1L - MoS_2}$ showing the signature of ferroelectricity consistent with the observed o/t phase in XAS (Fig. 4)

![](images/99af554e5b35debce56ab0fd7554797034db136173f09251b703a70bc21f2532.jpg)  
Fig. 14 Max process temperature vs. HZO thickness $(<  7\mathrm{nm})$ in FeFETs/ MFIS and FTJ/ FeRAM (in gray symbols) as reported here and from literature on several semiconductors.

![](images/58ff3b65b4335d83c327e76ba19f987238faeac547ba7897db19d03decf24943.jpg)  
Fig.15 IREAD by fast I-V measurements. With a sufficient carrier concentration by applying $\mathrm{V_{BG}}$ $(\mathrm{EOT} = 50\mathrm{nm})$ ,MW is comparable to MW extracted by DC measurements.

![](images/55160c0b3d5aaed1c2c3fa243de2775eba629a346c02a8dd1db46f0de2080a04.jpg)

![](images/92363c734809af018f1b776b7964dd74dfc98fd18046dfe9ea8d2da139300d50.jpg)  
Fig. 16 Normalized MW (difference in $\mathrm{V_{TH}}$ at HVTS/LVTS) at $\mathrm{V_{BG}} = 20\mathrm{V}$ as a function of $\mathrm{t_{pulse}}$ from $100\mu \mathrm{s}$ to 30ns. This allows to estimate the time constant of traps.   
Fig. 17 Endurance test for the proposed 1L-MoS $_2$ FeFETs with write pulse 100ns at 1V. No MW degradation is observed at least until 10 $^{12}$ cycles.

![](images/a6407278369b5c7e1f05a3b64f21d131ceb300338bc3a2ab3ffad333ccbb474b.jpg)

![](images/3a5cfe884974b3b158e14d6cd68d5041a3ee291c10a5d39c4eb1e5465432f0af.jpg)

![](images/18ffed12712989945b74c3b3d1496b8e650f18747d5f4a5262ef517dbace5846.jpg)

![](images/af88b090718723ee77c6a2f220c2ed003aaaaea892ded138ab5f0e313d641f4f.jpg)  
Fig. 19 Endurable $t_{\mathrm{stress}}$ at several HZO thickness on several semiconducting substrates in FeFETs/ MFIS and FTJ/ FeRAM (in gray symbols).   
Fig. 20 MW in $\mathrm{MoS}_2$ FeFETs as a function of retention time. MW $>$ 0.4V for 10 years from the extrapolation of the data at $10^{4}$ s.

![](images/b69df99a7d0adcd1a095145905a4605c5f16cd0ded755b24741218d01e568188.jpg)  
Fig. 18 Endurance properties of (a) S.S. and (b) $2\mathrm{Pr}$ with $\mathrm{V_c}$ in $\mathrm{MoS}_2$ FeFETs. S.S. after stress up to $10^{12}$ cycles is relatively well maintained at $\sim 75\mathrm{mV / dec}$ at HVTS and $110\mathrm{mV / dec}$ at LVTS. The extrapolation to $50\%$ degradation in $2\mathrm{Pr}$ is $>10^{18}$ cycles.

![](images/96510a7cba1023f729fa5630239733579282eb8f4b2dec78a84108daaaef353e.jpg)  
Fig. 21 (a) 1T-1FeFET with access transistors in FEoL and (b) FeFET-only with 1L-MoS $_2$ FeFET in BEoL only for higher AE.

Table. I Read/ write scheme for FeFET-only array with the proposed 1L-MoS2 FeFET.   

<table><tr><td colspan="2"></td><td>PRG</td><td>ERS</td><td>Read</td><td>Hold</td></tr><tr><td rowspan="3">Sel.</td><td>WL</td><td>1.0V</td><td>0</td><td>0.4V</td><td>0</td></tr><tr><td>BL</td><td>0</td><td>0.5V</td><td>0.1V</td><td>0</td></tr><tr><td>SL</td><td>0</td><td>0.5V</td><td>0</td><td>0</td></tr><tr><td rowspan="3">Unsel.</td><td>WL</td><td>0.5V</td><td>0.25V</td><td>0</td><td>0</td></tr><tr><td>BL</td><td>0.5V</td><td>0.25V</td><td>0</td><td>0</td></tr><tr><td>SL</td><td>0.5V</td><td>0.25V</td><td>0</td><td>0</td></tr></table>

![](images/70e938fb0415ca30ab1bc980f1a651f7dd575ec697739154bab2774895c24db5.jpg)  
Fig. 22 The distribution of $\mathrm{V_{TH}}$ at LVTS/HVTS data from FeFET to identify sigma of $\mathrm{V_{TH}}$ induced by the process variation.

![](images/99840b5eaf88aec0b0e674255f4867da51244fab34a564e9844b5d00144f0e97.jpg)

![](images/2f3d8b1bdf8597d8cd4e31b3c57484cc5e4f773a6435dd2e461c24208fc1fc95.jpg)

![](images/a218b118f3be0c4c7740c3720f31b1a9a4d391ad401741b330a4441a9c88e4b9.jpg)  
Fig. 24 Floorplans of (a) 1T-1FeFET array and (b) high- AE FeFET-only array.   
Table. II Benchmark table for comparison with reported FeFETs with FE thickness $< {10}\mathrm{\;{nm}}$ for low power eNVMs.   
Fig. 23 (a) Design of sense amplifier in $7\mathrm{nm}$ technology and (b) Timing breakdown of current sensing for the proposed 1L $\mathrm{MoS}_2$ FeFETs with the sense amplifier.

<table><tr><td colspan="2">This work</td><td>VLSI&#x27;23 [3]</td><td>VLSI&#x27;23 [10]</td><td>VLSI&#x27;22 [6]</td><td>VLSI&#x27;22 [7]</td><td>IEDM&#x27;21 [16]</td><td>IEDM&#x27;21 [17]</td></tr><tr><td>Architecture</td><td>Dual-gate</td><td>Front-gate Planar</td><td>Front-gate Nanosheet</td><td>Back-gate</td><td>Front-gate Nanosheet</td><td>Back-gate</td><td>Back-gate</td></tr><tr><td>Channel Material</td><td>\( {\mathrm{{MoS}}}_{2} \)</td><td>Si</td><td>\( {\mathrm{{Ge}}}_{0.38}{\mathrm{{Sn}}}_{0.02} \)</td><td>\( {\mathrm{{In}}}_{2}{\mathrm{O}}_{3} \)</td><td>Si</td><td>IWO</td><td>\( {\mathrm{{In}}}_{2}{\mathrm{O}}_{3} \)</td></tr><tr><td>FE thickness (nm)</td><td>2.5</td><td>4.6</td><td>7</td><td>8</td><td>9</td><td>5</td><td>8</td></tr><tr><td>\( 2{P}_{\mathrm{r}}\left( {\mu \mathrm{C}/{\mathrm{{cm}}}^{2}}\right) \)</td><td>7.1</td><td>20</td><td>NA</td><td>40</td><td>NA</td><td>NA</td><td>50</td></tr><tr><td>Endurance</td><td>\( &gt; {10}^{12} \)</td><td>\( \sim  {10}^{6} \)</td><td>\( &gt; {10}^{11} \)</td><td>\( &gt; {10}^{8} \)</td><td>\( &gt; {10}^{11} \)</td><td>\( &gt; {10}^{10} \)</td><td>\( \sim  {10}^{9} \)</td></tr><tr><td>\( {V}_{\text{PROGRAM }}/{V}_{\text{ERASE }}\left( \mathrm{V}\right) \)</td><td>1.0/-0.5</td><td>2.71/-1.71</td><td>2/-2</td><td>2.4/-2.4</td><td>3.5/-3.5</td><td>1.6/-1.6</td><td>2.2/-2.2</td></tr><tr><td>\( {\mathrm{t}}_{\mathrm{{WRIT}}} \)</td><td>30ns</td><td>1μs</td><td>100ns</td><td>50ns</td><td>5μs</td><td>20ns</td><td>500ns</td></tr><tr><td>MW/VWRITE (V)</td><td>0.27</td><td>0.11</td><td>0.45</td><td>0.42</td><td>0.19</td><td>0.22</td><td>0.50</td></tr><tr><td>LVTS \( {V}_{\mathrm{{TH}}}\left( \mathrm{V}\right) \)</td><td>0.1</td><td>0.1</td><td>-0.5</td><td>-3.2</td><td>-0.9</td><td>-0.4</td><td>-1.4</td></tr><tr><td>Back-gate bias for \( {P}_{\mathrm{{STB}}} \) reduction</td><td>Yes</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>BEOL Compatibility</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr></table>