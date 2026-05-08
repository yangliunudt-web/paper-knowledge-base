---
title: "Monolithic Integration of Oxide Semiconductor FET and Ferroelectric Capacitor for\\"
authors:
  - "Jixuan Wu"
  - "Fei Mo"
  - "Takuya Saraya"
  - "Toshiro Hiramoto"
  - "Mototaka Ochi"
  - "Hiroshi Goto"
  - "Masaharu Kobayashi"
date: "2021-12-01"
year: 2021
journal: "IEEE Transactions on Electron Devices"
doi: "10.1109/TED.2021.3111145"
abstract: "We have developed and integrated a mobility-enhanced FET and a wakeup-free ferroelectric\\"
abstract_cn: "开发了使用 Sn 掺杂 InGaZnO (IGZTO) 的迁移率增强型 FET 和无唤醒铁电 (FE) 电容，并演示了用于 3D 嵌入式 RAM 应用的 1T1C\\"
keywords:
  - "[[IGZTO]]"
  - "[[Ferroelectric capacitor]]"
  - "[[3D integration]]"
  - "[[FeRAM]]"
cite: "Wu J, Mo F, Saraya T, et al. Monolithic integration of oxide semiconductor FET and\\"
aiSum: "IGZTO FET+FeRAM 单片集成：>20 cm²/V·s 迁移率、400°C 低温工艺、~ns 操作、3D 嵌入式 RAM、东京大学。"
confidence: high
---

Index Terms-Ferroelectric (FE) memory, monolithic 3-D integration, oxide semiconductor FET.

# I. INTRODUCTION

HE proximity of a high-density memory to a processor core has become more and more important for the last level cache in the conventional architecture and machine learning accelerator in AI chips [1], [2]. Near-memory computing with an embedded memory has been one of the
  - "[[FeRAM]]"

Manuscript received July 29, 2021; revised September 1, 2021; accepted September 3, 2021. Date of publication September 16, 2021; date of current version December 1, 2021. This work was supported in part by Japan Science and Technology Agency (JST) CREST under Grant 16815651 and in part by Japan Society for the Promotion of Science (JSPS) KAKENHI under Grant JP18H01489. The review of this article was arranged by Editor S. Yu. (Corresponding author: Jixuan Wu.) Jixuan Wu, Fei Mo, Takuya Saraya, and Toshiro Hiramoto are with the Institute of Industrial Science, The University of Tokyo, Tokyo 153-0041, Japan (e-mail: jixuanwu@nano.iis.u-tokyo.ac.jp).

Mototaka Ochi is with Kobe Steel, Ltd., Kobe, Hyogo 651-8585, Japan. Hiroshi Goto is with Kobelco Research Institute, Inc., Kobe, Hyogo 651-2271, Japan.

Masaharu Kobayashi is with the Institute of Industrial Science, The University of Tokyo, Tokyo 153-0041, Japan, and also with the System Design Research Center (d.lab), Department of Engineering, The University of Tokyo, Tokyo 153-0041, Japan (e-mail: masa-kobayashi@ nano.iis.u-tokyo.ac.jp).

Color versions of one or more figures in this article are available at https://doi.org/10.1109/TED.2021.3111145.

Digital Object Identifier 10.1109/TED.2021.3111145

most attractive solutions to overcome the Von Neumann bottleneck [3], [4]. 3-D monolithic integration of a processor core and an embedded memory will enable high-density and energy-efficient computing. Currently, there are several options of the embedded memory such as eDRAM [5], MRAM [6], and PCRAM [7] in the market, and research and development. Those memory cells typically consist of a memory element and an access transistor which is usually a Si-MOSFET. Thus, an extra area is needed in a chip to place the access transistor in the front-end-of-line (FEOL) layer [8], [9].

High-density and energy-efficient embedded memory systems can be achieved by integrating both access transistor and memory elements in the back-end-of-line (BEOL) layers. Recently, oxide semiconductor such as InGaZnO (IGZO) [10]–[12] has been attracting attention because transistors can be placed in BEOL layers, thanks to its low-temperature process. IGZO has been widely used in flat panel display (FPD) products such as thin-film transistor backplanes. The first practical device was reported in 2004 with amorphous IGZO as a channel material with high mobility, transparent, and flexible TFT fabricated at room temperature (RT) and then commercialized in 2012 [10], [13]. In addition, ferroelectric (FE)-[[HfO2]] has been attracting attention for its CMOS compatibility, scalability, and lowtemperature process [14]–[17]. FE properties in fluorite structure oxides such as hafnia and zirconia were first reported in 2011 by Böscke et al. Since then, FE-HfO2 has attracted much interest in the field of FE and for nonvolatile memory applications [18]. Integration of oxide semiconductor FET and FE-HfO2 capacitor can be a feasible approach for 3-D embedded RAM applications such as eDRAM and FeRAM (see Fig. 1).

Previously, we have reported 1T1R cell operation of an IGZO transistor and an [[RRAM]] cell for monolithic 3-D integration [19], where we emphasized the importance of mobility enhancement and high reliability of oxide semiconductor FET. Sn-doped IGZO (IGZTO) has been developed for FPD purposes by coauthors [20], where high mobility was reported. Fig. 2 shows the PBTI characteristics of IGZO and IGZTO FETs made by the baseline process, which shows significant

![](images/2d1f76b886c9a7fbe87598fde8d7941fa00ca4817bd7e0efeea40be79504063e.jpg)

![](images/86cc36933de47bfd7c3db82e4d327f471b0cc28756de265128b0d14145d8b9c1.jpg)  
Fig. 1. Proposed concept of monolithic 3-D integration of oxide semiconductor FET and FE-HfO2 capacitor for 1T1C embedded RAM application such as eDRAM and FeRAM.   
Fig. 2. Measured PBTI characteristics of IGZO and IGZTO FETs made by the baseline process. IGZTO FET shows significant improvement.

improvement in IGZTO FETs. This is a large advantage of IGZTO over IGZO in terms of reliability.

Therefore, in this work, we introduce Sn-doped IGZO (IGZTO), develop and integrate FETs and FE capacitors, and demonstrate 1T1C operation. The characteristics of IGZO FET and IGZTO FET are compared in this work. The physical mechanism of mobility enhancement with Sn dopant is systematically studied with the temperature dependence measurement and ab initio simulation. We also discuss the impact of IGZTO FET on 1T1C cells from the aspects of gate voltage dependence and FE capacitor size dependence. To project the real performance of the 1T1C memory cell with small-size device, we also perform a SPICE simulation.

# II. DESIGN SPACE EXPLORATION

It is critical to understand whether the mobility of oxide semiconductors is sufficient to drive FE capacitor. We consider the design space of 1T1C cell using oxide semiconductor FET and FE capacitor. Fig. 3(a) shows the contour plot of switching time $( \boldsymbol { t } _ { \mathrm { s w } } )$ of the FE capacitor calculated by FET current $( I _ { \mathrm { F E T } } )$ [21] and polarization charge density of $1 0 \ \mu \mathrm { C } / \mathrm { c m } ^ { 2 }$ , as a function of mobility and capacitor area. Polarization switching peak current $( I _ { \mathrm { p o l } } )$ is finite and can potentially limit $t _ { \mathrm { s w } }$ . Fig. 3(b) illustrates the definition of $I _ { \mathrm { F E T } } , \ I _ { \mathrm { p o l } } .$ , and $I _ { \mathrm { c e l l } }$ .

![](images/28a9f7b7a5f2601b23a5550feed88df90e0d2e68c137d74db25f700fc684ac53.jpg)

![](images/398ebec5d53c6fc84950ea2f6a7a50d333d0ec739c7c475187bac2e4370ac775.jpg)  
Fig. 3. (a) Contour plot of switching time $( \mathrm { \Delta } t _ { \mathsf { S W } } )$ of 1T1C cell calculated by FET current (IFET) and polarization charge [21]. (b) Definition of IFET, Ipol,and lcell. (c) pol with different rise/falltimesof voltage pulse.

![](images/a4993f86749a6d31bb98c48deb359e6993d2b47fb18cac1878a338ba77c12d5f.jpg)

![](images/50f38ce4365bd3744185deeee9f66649d0dffc1e4e83ba183b58a7b3ce704f7d.jpg)  
Fig. 4. (a) Fabrication process flow. IGZTO FET is formed by a bottom-gate structure with ultrathin 8-nm IGZTO. FE capacitor is formed in the stack of TiN/HZO/IGZTO/TiN. (b) Schematic of the device structure. (c) Top-down microscope image. IGZTO FET and FE capacitor are integrated into the same device.

$I _ { \mathrm { p o l } }$ was estimated by extrapolating the measured peak current with different pulse rise/fall times as shown in Fig. 3(c). Since the measured $I _ { \mathrm { p o l } }$ can be limited by RC delay of the sample and measurement system, those data were fit to extract $I _ { \mathrm { p o l } }$ . On the other hand, ideal $I _ { \mathrm { p o l } }$ without RC delay may be determined by linearly extrapolating the measured $I _ { \mathrm { p o l } }$ data. These two extracted currents set the boundary drawn in Fig. 3(a). The boundary determines which of $I _ { \mathrm { F E T } }$ or $I _ { \mathrm { p o l } }$ is the 1T1C cell peak current $\left( I _ { \mathrm { c e l l } } \right)$ . There is a design space where $1 0 { - } 1 0 0 \ \mathrm { c m } ^ { 2 } / \mathrm { V } \cdot \mathrm { s }$ mobility oxide semiconductor can switch FE capacitor around 1–10 ns, which is applicable to embedded memory applications.

# III. DEVICE STRUCTURE AND FABRICATION

Fig. 4 shows (a) the device fabrication flow for the proofof-concept and (b) the schematic of the device structure of the 1T1C cell. Starting from the Si-substrate which was cleaned by RCA wet clean, $\mathrm { S i O } _ { 2 }$ was deposited by radio frequency (RF) reactive sputtering. FE capacitor was formed in the stack of TiN/IGZTO/HfZrOx(HZO)/TiN. The bottom electrode of the capacitor was formed by depositing TiN by RF sputtering and patterning. The 9-nm HZO was deposited by atomic layer deposition (ALD) as an FE layer at $2 5 0 ~ ^ { \circ } \mathrm { C } .$

![](images/e14ea29a9834aefd27a1228ecb8d48fe38f54b4f9b5bfd659e67e93e09f558d6.jpg)

![](images/d2193fc616069045073f13cb2a706a2b9f6a7b833ceec4050abe3d202060126e.jpg)  
Fig. 5. Cross-sectional STEM images of (a) IGZTO FET and (b) FE capacitor. Each layer is uniformly formed. With IGZTO capping, the HZO layer is crystallized after RTA.

The Zr/Hf ratio is 1/1. 8-nm IGZTO was deposited by RF sputtering from a compound target and patterned by diluted HCl solution. RTA was done in $\Nu _ { 2 }$ ambient for crystallization. An IGZTO FET was formed by a bottom-gate structure with $\mathrm { H f O } _ { 2 }$ gate insulator and ultrathin 8-nm IGZTO. $\mathrm { H f O } _ { 2 }$ was deposited by ALD for gate insulator with 5.5-nm thickness for FET performance evaluation and 10 nm for access transistor demonstration. The 8-nm IGZTO is deposited by RF sputtering as a channel material and patterned by diluted HCl solution. The W /L of the FET is 100 μm/10 μm, and the diameter of the FE capacitor is 34–90 μm. Fig. 4(c) shows a top-down microscope image of an IGZTO FET and an FE capacitor integrated into the same device as a 1T1C cell. The FET and FE capacitor in the 1T1C cell can be individually tested using the extra pad. Fig. 5(a) and (b) shows the cross-sectional TEM images of IGZTO FET and FE capacitor. Each layer was uniformly formed. With IGZTO capping, the HZO layer was fully crystallized after RTA, while the $\mathrm { H f O } _ { 2 }$ gate insulator and IGZTO layers were kept amorphous. Fig. 6 shows the elemental mapping of an FE capacitor by EDX. IGZTO and HZO show the sharp interface. Note that we confirm that Ga signal in HZO is not from Ga itself but from Hf because Ga-Kα and Hf-Lβ have close peak positions in the EDX spectrum.

# IV. RESULTS AND DISCUSSION

# A. FET Characteristics and Physics of Mobility Enhancement

We characterized the IGZTO FET and compared it with the IGZO FET. Fig. 7(a) and (b) shows the $I _ { \mathrm { d } } { - } V _ { \mathrm { g } }$ curves of the IGZO and IGZTO FETs. Normally off operation, nearly ideal subthreshold slope [the insets of Fig. 7(a) and (b)], and high drive current were obtained. Fig. 7(c) shows the $I _ { \mathrm { d } } { - } V _ { \mathrm { d } }$ curves of the IGZTO and IGZO FETs, where 2× higher drive current was obtained in the IGZTO FET than in the IGZO FET. We extracted the effective mobility for both IGZO and IGZTO FETs in Fig. 7(d). The IGZTO FET can achieve >20 cm2/V · s mobility with the ultrathin channel, which is also 2× higher than the IGZO FET.

To investigate the origin of high mobility in IGZTO FET, we measured the temperature dependence of mobility in Fig. 8(a). Temperature dependence is smaller in the IGZTO FET than in the IGZO FET. According to the percolation transport theory as illustrated in Fig. 8(b), mobility is an exponential function of the average barrier height from the Fermi

![](images/317c6133fd9fcb9737fc6ef5adca0bcff77bf7dd54a16602c6c8dde572bb2442.jpg)

![](images/e1ba010d29a9181ec0a343ecc7c4ea8433f8461a4df95a54740b5404288d6bc6.jpg)

![](images/4a56d9da076f71d6e75d6967f6a428a3df4402ac09398dcc128a98ce7c5017ca.jpg)

![](images/1fb5c7cd0f2d6e55e537057186c1beeb8f08d1cbd1d305f492733740d2773896.jpg)

![](images/060a43c58ffb750bf406601d428f9ff2746fcda5507ef46b51b7d9e2084a8f4f.jpg)

![](images/943d1e1efc609872825d38a145c2656558b3923c2e3b6cd00776c943bbd31db8.jpg)

![](images/833439f22e9499dbf1ddcafd8659748ea64b0a46d44d421d0b14ddc9ce74709d.jpg)

![](images/b936fcb78a2d9e447b9a4ab8fe038aed618d4d7918d9e77c494c47531c94a694.jpg)

![](images/8829c0abdd91b15b1ac41366eeeef74bd394a14a3e4a6cb4ae430de764cf751e.jpg)  
Fig. 6. Elemental mapping of an FE capacitor measured by EDX.

![](images/8f14dd4b039232a008ffbabff387d2cac5594214ad7720ec37eef5fb73070d40.jpg)

![](images/f8a89f8231c383a8b70f6ec9e611eec029e63054f40b3450c56a20652c04df1a.jpg)

![](images/373bce742b0246f1d459b210a55c601c9e32a61a4687f42e942641ef97141748.jpg)

![](images/43ac33b20919a95e61ea34e546aca7885a45c62dd7b017f057c44dbfd87dc9cc.jpg)  
Fig. 7. (a) Six measured $I _ { \mathsf { d } } \mathrm { - } V _ { \mathsf { g } }$ curves IGZO FET. The inset shows SS versus $I _ { \mathsf { d } } .$ This is a reference device from [20]. (b) Measured $I _ { \mathsf { d } } - V _ { \mathsf { g } }$ curves of IGZTO FET. The inset shows SS versus Id. Sharp cut-off characteristics are obtained. (c) Measured $I _ { \mathsf { d } } - V _ { \mathsf { d } }$ curves of IGZTO and IGZO FETs. IGZTO shows 2× higher $I _ { \mathrm { o n } } .$ . (d) Measured effective mobility. IGZTO shows 2× higher mobility than IGZO.

level. The lower temperature dependence of the IGZTO FET indicates that the average potential barrier height is smaller in IGZTO FET [22]. The potential barrier height is attributed to the band edge fluctuation in an amorphous structure. Thus, the band edge fluctuation in IGZTO is expected to be lower than in IGZO.

To support the discussion above, we used ab initio simulation. As a starting point, an IGZO crystal structure with superlattice including 84 atoms is built for the simulation as shown in Fig. 9(a). One Sn atom is introduced as a substitute atom (Sn substitute Ga atom— $- S \mathrm { { n } _ { G a } , }$ , Sn substitute In $\mathrm { { a t o m } - \mathrm { { S n _ { I n } } , } }$ Sn substitute $\mathrm { Z n a t o m { \mathrm { - } } S n _ { Z n } ) }$ or interstitial atom $( \mathrm { { S n } _ { i } ) }$ .

![](images/d3c734a9c4508f218b2680a3ca638c3a880e1d09efae05ad4df5c5eb0257d817.jpg)  
Fig. 8. (a) Temperature dependence of mobility and extracted average barrier height at different biases. (b) Mobility model based on percolation theory [22]. IGZTO has a lower potential barrier height, which leads to higher mobility.

![](images/da3fa5f52516e5b0f78bf6182f0e5b8866e891e83fe8e88e7bb590741e0e0bf3.jpg)

![](images/e65e0860863b1df432442177120914d5b0f5372c14907f92c7f146d864f77c3f.jpg)  
Fig. 9. (a) Crystal IGZO atomic supercell structure. (b) Formation energy of Sn-doped defect in crystal IGZO.

Generalized gradient approximation (GGA)-Perdew–Burke– Ernzerhof (PBE) is used as the pseudo-potential for DFT simulation with $5 \times 5 \times 5 k$ -point sampling. The energy cutoff is set to 125 Har. The formation energies of the Sn substitutes and interstice are shown in Fig. 9(b). The Sn substitutes have relatively lower formation energy than the interstice, which means that there could be a higher probability that Sn dopant exists as substitutes rather than interstice. From now on, we only focus on the substitutes. For further analysis of the effect of Sn dopant on the electronic conduction and mobility, we also analyzed the wave function of the conduction band minimum (CBM) as shown in Fig. 10. It shows that the wave function is more localized around the atoms without Sn dopant and extended with Sn dopant, which consequently results in a higher probability of an electron crossing the system [23].

Since IGZO is formed as amorphous layer for the FET channel, we also built the amorphous IGZO (a-IGZO) structure using molecular dynamics (MD). The initial models of a-IGZO were first built with classical MD simulations by melt and quench method from the initial crystalline structure model containing 84 atoms. The parameters used for classical potential are referred to [24]. Then, the MD-relaxed a-IGZO models were further relaxed by the DFT structure relaxation calculations. One example of the a-IGZTO supercell is shown in Fig. 11(a). Pseudo-band structures of a-IGZO without and with Sn substitute are shown for ten samples in Fig. 11(b). It shows that the CBM variation in 10 a-IGZO samples is suppressed with Sn doping. The small band edge fluctuation in a-IGZTO indicates the mobility enhancement in the percolation transport theory [25]. The contour plots of the projected

![](images/33dd2148384cfaa318f05886bf320f22518024bf2f5666d28b9effebd6b454a2.jpg)  
Fig. 10. Plots of the projected self-consistent Hamiltonian eigenstates of (a) pure IGZO and (b)–(d) Sn-doped IGZO along the middle plane. The results are shown for states at the CBM. The electronic state is extended with Sn dopant consequently resulting in a higher probability of an electron crossing the system.

![](images/9bb6600d92b21d596cc44715efdbc0ba487dbd6f10e71f5bcc7174b3afe0ea9b.jpg)  
Fig. 11. (a) Atomic structure of amorphous IGZO. (b) Calculated pseudo-band structures of a-IGZO and IGZTO. Ten samples are shown for each.

self-consistent Hamiltonian wave functions of pure a-IGZO (a)–(c) and a-IGZTO (d)–(f) on (100), (010), and (001) plane are shown in Fig. 12. The results are shown for the states at the CBM. Similar to the crystal IGZO case, the electronic state of CBM is extended by Sn dopant consequently resulting in a higher probability of an electron crossing the system.

# B. FE Capacitor Characteristics

FE capacitors with IGZTO capping were characterized. Fig. 13(a) and (b) shows the P–V curves of the FE capacitors fabricated by $5 0 0 ~ ^ { \circ } \mathrm { C }$ and $4 0 0 ~ ^ { \circ } \mathrm { C }$ RTA. The $5 0 0 ~ ^ { \circ } \mathrm { C }$ FE capacitor has large $P _ { \mathrm { r } } \sim 2 0 \ \mu \mathrm { C } / \mathrm { c m } ^ { 2 }$ , while the $4 0 0 ~ ^ { \circ } \mathrm { C }$ FE capacitor also shows $P _ { \mathrm { r } } \sim 1 0 ~ \mu \mathrm { C } / \mathrm { c m } ^ { 2 }$ with sharp switching. This low-temperature process at $4 0 0 ~ ^ { \circ } \mathrm { C }$ is preferable for BEOL compatibility. IGZTO can realize large ferroelectricity even at low temperature because IGZTO has a relatively small thermal expansion coefficient similar to IGZO and induces large strain for FE phase formation [26].

Fig. 13(c) shows the endurance characteristics of the FE capacitor with IGZTO capping and with IGZO capping for reference. They show similar endurance characteristics. Fig. 13(e) shows the corresponding P–V curves. The pulse cycling with $1 - \mu \mathrm { s }$ pulsewidth is used for endurance measurement. The 2Pr is $> 1 5 ~ \ \mu$ after $1 0 ^ { 7 }$ cycling pulses without breakdown. More importantly, there is no wakeup phenomenon, which is the large advantage with IGZTO capping as reported with IGZO [26]. The wakeup phenomenon is mainly caused by defect redistribution during the stress cycles as reported [27], [28]. Thanks to the oxide–oxide interface between FE-HZO and IGZTO, the oxygen vacancy

![](images/0f59339425975cffd89cb5685d32563e65e5dc5dc1c8a1b53a053c790a4b4604.jpg)

![](images/d6bcf3f57c6e6962a51c9bacd1a36f0668fe49ac5367eaf8b70e6133e3b8897a.jpg)

![](images/d4f4e7985c7d874e76a57b1fd871a8bfdc6072c1e988bb7a37e7c41757b452d4.jpg)  
Fig. 12. Contour plots of the projected self-consistent Hamiltonian eigenstates of (a)–(c) pure a-IGZO and (d)–(f) Sn-doped a-IGZO on (100), (010), and (001) plane. The results are shown for the states at CBM. The electronic state is extended with Sn dopant consequently resulting in a higher probability of an electron crossing the system.

![](images/7b4863fd45773c5a3294e3e896cb96896506c671b3e9f702f4fdfde8ccf7bb97.jpg)

![](images/f8a45fedd5913b46ff8783e2d238ed389ce1f227457a063bac9a40a2e209038d.jpg)

![](images/73f241fa3c3d94a611f6b66b4fb93be05c8ba3840b4a7db89186914e1fef6351.jpg)

![](images/7dc77705cb6b9134dba018255fa92a2b6e2bdd1d50739d9662f0b6cc0473ccbc.jpg)

![](images/2e8950a5f27818070fef4757deee0f1d0b3cf7843c4fe7847ca49c4a2009102e.jpg)

![](images/152c9907df1805957f19e05e26600bdeb97ee24d1ea625e520fefb7cbd02c915.jpg)

![](images/4ede1b8d5e51bdc4c6502709364726618956fdd7c450be0cbd190b45ddfc36fb.jpg)

![](images/d9d10dde72e8021b22fd01829b45e27dd7b384f90613c62f75897cc83237763e.jpg)

![](images/68fe14852771459f34179ed8309007f1bf674d1de09fa521f3b1ed8ee4971700.jpg)

![](images/808810dcd50cac69cfc4a6e63bd35f5c6f8f84ce0090679cbc74398895d4b550.jpg)  
Fig. 14. (a) Measurement setup and typically measured waveform of 1T1C cell. (b) Measured waveform of 1T1C cell current with different $V _ { 9 }$ and 1C devices. (c) Measured waveform of 1T1C cell current with different FE capacitor sizes and 1C device. (d) SPICE simulation with $0 . 1 \mathrm { - } \mu \mathsf { m } ^ { 2 }$ capacitor shows ns operation of 1T1C cell. The inset shows FET calibration.

Fig. 13. (a) Measured P–V curve of IGZTO-capped HZO FE capacitor with 500 ◦C RTA. (b) Measured P–V curve of IGZTO-capped HZO FE capacitor with 400 ◦C RTA. (c) Measured endurance characteristics that show no wakeup phenomenon. (d) Measured retention characteristics. (e) P–V curves of endurance measurement. (f) P–V curves of retention measurement.

formation is suppressed. Thus, defect redistribution does not occur during the stress cycles and the wakeup-free operation can be achieved. Fig. 13(d) shows the retention characteristics

at RT without much degradation after 12-h retention. Ten years retention is expected from extrapolation. Fig. 13(f) shows the corresponding P–V curves of the retention measurement. The imprint effect during retention at the positive polarization state (at +V) is relatively smaller than that at the negative polarization state (at −V). This can be explained by the impact of electron injection from TiN electron with a midgap workfunction being small due to the high barrier height [26].

#

We demonstrated the write/read operation of the 1T1C cell using the measurement scheme in Fig. 14(a). In the write operation, a positive voltage pulse is applied from the FET side and the current is sensed at the FE cap side. On the other hand, in the read operation, a positive voltage pulse is applied from the FE capacitor side and the current is sensed at the FET side. 1T1C cell current is extracted by subtracting the non-switching current from the switching current. $V _ { \mathrm { g } }$ dependence is shown in Fig. 14(b) for write and read operations. Write operation can be slower than read operation due to the source-follower mode of FET. $I _ { \mathrm { c e l l } }$ is limited by $I _ { \mathrm { F E T } }$ and gets closer to $I _ { \mathrm { p o l } }$ as $V _ { \mathrm { g } }$ increases, which effectively corresponds to moving to the upper direction in Fig. 3(a). The read operation can be fast, especially if the bitline ground sensing is used [29]. $I _ { \mathrm { c e l l } }$ reaches $I _ { \mathrm { p o l } }$ as $V _ { \mathrm { g } }$ increases. FE capacitor size dependence is shown in Fig. 14(c). In the write and read operations, as the FE capacitor size decreases, $t _ { \mathrm { s w } }$ becomes shorter, which corresponds to moving to the left direction in Fig. 3(a). $I _ { \mathrm { c e l l } }$ reaches $I _ { \mathrm { p o l } }$ for the smaller FE capacitor in the read operation.

To project the real performance of the 1T1C memory cell with small-size device, we also performed a SPICE simulation. Fig. 14(d) shows the SPICE simulation result of a $0 . 1 \mathrm { - } \mu \mathrm { m } ^ { 2 }$ FE capacitor and a scaled FET. The Preisach model [30]

is used with a single voltage-dependent switching time constant associated with nucleation-limited switching coefficient 0.1 ps and activation field 10 MV/cm. These parameters are extracted by fitting to experiment [31]. The SPICE model of the IGZTO FET is calibrated by the measurement result. The result shows ns operation and about 100 fJ write/read energy of 1T1C memory cell, which is applicable to embedded memory. Note that with a small-area FE capacitor, it is known that FE switching occurs in sub ns [32]. The drive current with a mobility of 20 $\mathrm { c m } ^ { 2 } / \mathrm { V } { \cdot } \mathrm { s }$ is almost comparable to the polarization switching current. Therefore, drive current dependence can be weaker but a high drive current is still helpful for faster write operation.

# V. CONCLUSION

We developed BEOL-compatible monolithic integration of FET and FE capacitor using IGZTO and demonstrated 1T1C FeRAM operation toward the design target. The IGZTO FET with high mobility and high driving current was achieved. The physical mechanism of mobility enhancement with Sn dopant was systematically studied. Sn substitute increases the probability of an electron crossing by extending the electron wave function. Thus, potential fluctuation is suppressed and higher mobility is obtained. With IGZTO capping, the HZO FE capacitor shows high endurance and wakeup-free characteristics. $V _ { \mathrm { g } }$ dependence and FE capacitor size dependence are characterized by 1T1C cell for write/read operation. SPICE simulation indicates that the memory cell can be operated in ns. The proposed 3-D embedded memory enables high-density and energy-efficient computing.

# ACKNOWLEDGMENT

The authors would like to thank Dr. Toshifumi Irisawa (National Institute of Advanced Industrial Science and Technology (AIST), Tokyo, Japan) for technical support.

# REFERENCES

[1] F. K. Hsueh et al., “First demonstration of ultrafast laser annealed monolithic 3D gate-all-around CMOS logic and [[FeFET]] memory with near-memory-computing macro,” in IEDM Tech. Dig., Dec. 2020, pp. 40.4.1–40.4.4.   
[2] F. Schuiki, M. Schaffner, F. K. Gürkaynak, and L. Benini, “A scalable near-memory architecture for training deep neural networks on large in-memory datasets,” IEEE Trans. Comput., vol. 68, no. 4, pp. 484–497, Apr. 2018.   
[3] M. Sivan et al., “All WSe2 1T1R resistive RAM cell for future monolithic 3D embedded memory integration,” Nature Commun., vol. 10, no. 1, pp. 1–12, Dec. 2019.   
[4] S. S. Iyer, “The evolution of dense embedded memory in high performance logic technologies,” in IEDM Tech. Dig., Dec. 2012, pp. 33.1.1–33.1.4.   
[5] C. H. Lin et al., “High performance 14 nm SOI FinFET CMOS technology with 0.0174 μm2 embedded DRAM and 15 levels of Cu metallization,” in IEDM Tech. Dig., Dec. 2014, pp. 3–8.   
[6] S. H. Han et al., “28-nm 0.08 mm2/Mb embedded MRAM for frame buffer memory,” in IEDM Tech. Dig., Dec. 2020, pp. 11.2.1–11.2.4.   
[7] F. Arnaud et al., “High density embedded PCM cell in 28 nm FDSOI technology for automotive micro-controller applications,” in IEDM Tech. Dig., Dec. 2020, pp. 24.2.1–24.2.4.   
[8] C.-C. Cheng et al., “Monolithic heterogeneous integration of BEOL power gating transistors of carbon nanotube networks with FEOL Si ring oscillator circuits,” in IEDM Tech. Dig., Dec. 2019, pp. 19.2.1–19.2.4.   
[9] S. Dutta et al., “Monolithic 3D integration of high endurance multi-bit ferroelectric FET for accelerating compute-in-memory,” in IEDM Tech. Dig., Dec. 2020, pp. 36.4.1–36.4.4.

[10] K. Nomura, H. Ohta, A. Takagi, T. Kamiya, M. Hirano, and H. Hosono, “Room-temperature fabrication of transparent flexible thin-film transistors using amorphous oxide semiconductors,” Nature, vol. 432, no. 4016, pp. 488–492, Nov. 2004.   
[11] M. Oota et al., “3D-stacked CAAC-In-Ga-Zn oxide FETs with gate length of 72 nm,” in IEDM Tech. Dig., Dec. 2019, pp. 3.2.1–3.2.4.   
[12] C.-C. Chang, P.-T. Liu, C.-Y. Chien, and Y.-S. Fan, “Solving the integration problem of one transistor one memristor architecture with a bi-layer IGZO film through synchronous process,” Appl. Phys. Lett., vol. 112, no. 17, Apr. 2018, Art. no. 172101.   
[13] K. Ide, K. Nomura, H. Hosono, and T. Kamiya, “Electronic defects in amorphous oxide semiconductors: A review,” Phys. Status Solidi A, vol. 216, no. 5, Mar. 2019, Art. no. 1800372.   
[14] S. C. Chang et al., “Anti-ferroelectric $\mathrm { H f } _ { X } \mathrm { Z r } _ { 1 - X } \mathrm { O } _ { 2 }$ capacitors for high-density 3-D embedded-DRAM,” in IEDM Tech. Dig., Dec. 2020, pp. 28.1.1–28.1.4.   
[15] J. Okuno et al., “SoC compatible 1T1C FeRAM memory array based on ferroelectric $\mathrm { H f } _ { 0 . 5 } \mathrm { Z r } _ { 0 . 5 } \mathrm { O } _ { 2 } , ^ { \prime \prime }$ in Proc. IEEE Symp. VLSI Technol., Jun. 2020, pp. 1–2.   
[16] L. Grenouillet et al., “Nanosecond laser anneal (NLA) for Si-implanted HfO2 ferroelectric memories integrated in back-end of line (BEOL),” in Proc. IEEE Symp. VLSI Technol., Jun. 2020, pp. 1–2.   
[17] Y. D. Lin et al., “3D scalable, wake-up free, and highly reliable FRAM technology with stress-engineered HfZrOX ,” in IEDM Tech. Dig., Dec. 2019, pp. 15.3.1–15.3.4.   
[18] M. H. Park, Y. H. Lee, T. Mikolajick, U. Schroeder, and C. S. Hwang, “Review and perspective on ferroelectric HfO2-based thin films for memory applications,” MRS Commun., vol. 8, no. 3, pp. 795–808, Aug. 2018.   
[19] J. Wu, F. Mo, T. Saraya, T. Hiramoto, and M. Kobayashi, “A monolithic 3D integration of RRAM array with oxide semiconductor FET for [[in-memory computing]] in quantized neural network AI applications,” in Proc. IEEE Symp. VLSI Technol., Jun. 2020, pp. 1–2.   
[20] M. Ochi, K. Nishiyama, Y. Teramae, H. Goto, and T. Kugimiya, “High stress stability imparted by Sn addition effect in high mobility amorphous IGZTO TFTs,” in Proc. IDW, 2018, p. 308.   
[21] International Technology Roadmap for Semiconductors (ITRS), Semicond. Ind. Assoc., 2015.   
[22] S. Lee et al., “Trap-limited and percolation conduction mechanisms in amorphous oxide semiconductor thin film transistors,” Appl. Phys. Lett., vol. 98, no. 20, May 2011, Art. no. 203508.   
[23] G. R. Berdiyorov and M. E.-A. Madjet, “First-principles study of electronic transport and optical properties of penta-graphene, penta-SiC2 and penta-CN2,” RSC Adv., vol. 6, no. 56, pp. 50867–50873, 2016.   
[24] M. Orita, H. Tanji, M. Mizuno, H. Adachi, and I. Tanaka, “Mechanism of electrical conductivity of transparent InGaZnO4,” Phys. Rev. B, Condens. Matter, vol. 61, no. 3, p. 1811, 2000.   
[25] I. I. Fishchuk et al., “Interplay between hopping and band transport in high-mobility disordered semiconductors at large carrier concentrations: The case of the amorphous oxide InGaZnO,” Phys. Rev. B, Condens. Matter, vol. 93, no. 19, May 2016, Art. no. 195204.   
[26] F. Mo, T. Saraya, T. Hiramoto, and M. Kobayashi, “Reliability characteristics of metal/ferroelectric-HfO2 /IGZO/metal capacitor for non-volatile memory application,” Appl. Phys. Exp., vol. 13, no. 7, Jul. 2020, Art. no. 074005.   
[27] M. Peši´c et al., “Physical mechanisms behind the field-cycling behavior of HfO2-based ferroelectric capacitors,” Adv. Funct. Mater., vol. 26, no. 25, pp. 4601–4612, Jul. 2016.   
[28] S. Starschich, S. Menzel, and U. Böttger, “Evidence for oxygen vacancies movement during wake-up in ferroelectric [[hafnium oxide]],” Appl. Phys. Lett., vol. 108, no. 3, Jan. 2016, Art. no. 032903.   
[29] S. Kawashima et al., “Bitline GND sensing technique for low-voltage operation FeRAM,” IEEE J. Solid-State Circuits, vol. 37, no. 5, pp. 592–598, May 2002.   
[30] K. Ni, M. Jerry, J. A. Smith, and S. Datta, “A circuit compatible accurate compact model for ferroelectric-FETs,” in Proc. IEEE Symp. VLSI Technol., Jun. 2018, pp. 131–132.   
[31] N. Gong, X. Sun, H. Jiang, K. S. Chang-Liao, Q. Xia, and T. P. Ma, “Nucleation limited switching (NLS) model for HfO2-based metal-ferroelectric-metal (MFM) capacitors: Switching kinetics and retention characteristics,” Appl. Phys. Lett., vol. 112, no. 26, Jun. 2018, Art. no. 262903.   
[32] X. Lyu, M. Si, P. R. Shrestha, K. P. Cheung, and P. D. Ye, “First direct measurement of sub-nanosecond polarization switching in ferroelectric hafnium zirconium oxide,” in IEDM Tech. Dig., Dec. 2019, pp. 15.2.1–15.2.4.