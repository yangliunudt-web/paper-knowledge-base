---

title: "Amorphous Indium Oxide Channel FeFETs with Write Voltage of 0.9V and Endurance >10¹²\\"
authors:
  - "Sharadindu Gopal Kirtania"
  - "Omkar Phadke"
  - "Eknath Sarker"
  - "Khandker Akif Aabr"
  - "Dyutimoy Chakraborty"
  - "Faaiq Waqar"
  - "Shin Jaewon"
  - "Sourav Dutta"
  - "Asif Khan"
  - "Shimeng Yu"
  - "Suman Datta"
date: "2023-01-01"
year: "2023"
journal: "IEEE Transactions on Electron Devices"
abstract: "For the first time, we demonstrate a back end of the line (BEOL) compatible amorphous\\"
abstract_cn: "首次展示了后端工艺兼容的非晶氧化铟钨（IWO）铁电场效应晶体管（FeFET），写入电压低于0.9V，耐久性超过10¹²次循环，85°C下保持特性超过10⁴秒，实现了无需刷新且嵌入式1T-1FeFET存储器的演示。"
keywords:
  - "[[FeFET]]"
  - "[[IWO]]"
  - "[[BEOL compatible]]"
  - "[[Multi-level cell]]"
  - "[[Neuromorphic]]"
cite: "待补充. Amorphous Indium Oxide Channel FeFETs with Write Voltage of 0.9V and Endurance\\"
aiSum: "首次BEOL兼容IWO FeFET：写入<0.9V，耐久性>10¹²循环，85°C保持>10⁴s，无需刷新1T-1FeFET存储器。"
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
  - "[[Neuromorphic computing]]"
---

# Amorphous Indium Oxide Channel FeFETs with Write Voltage of 0.9V and Endurance $>10^{12}$ for Refresh-free 1T-1FeFET embedded Memory

Sharadindu Gopal Kirtania<sup>1</sup>, Omkar Phadke<sup>1</sup>, Eknath Sarker<sup>1</sup>, Khandker Akif Aabr<sup>1</sup>, Dyutimoy Chakraborty<sup>1</sup>, Faaiq Waqar<sup>1</sup>, Shin Jaewon<sup>1</sup>, T.H. Pantha<sup>2</sup>, Sourav Dutta<sup>2</sup>, Asif Khan<sup>1</sup>, Shimeng Yu<sup>1</sup>, Suman Datta<sup>1</sup>

<sup>1</sup>Georgia Institute of Technology, Atlanta, GA, USA, <sup>2</sup>University of Texas Dallas, Richardson, TX 75080, USA. email: skirtania3@gatech.edu

Abstract—For the first time, we demonstrate a back end of the line (BEOL) compatible amorphous oxide semiconductor (AOS) FeFET with a record-low operating voltage $< 0.9\mathrm{V}$ and write-speed of 20ns while maintaining a current window $(\mathrm{I}_{\mathrm{LVT}} / \mathrm{I}_{\mathrm{HVT}}) > 10^{3}$ . We also demonstrate a) bipolar write endurance reaching $10^{12}$ cycles (measured), b) fast read speed of 50 ns, c) read endurance greater than $10^{12}$ cycles, and d) retention time exceeding $10^{4}$ seconds at $85^{\circ}\mathrm{C}$ . Array level analysis of AOS 1T-1FeFET offers 100x less standby power than 2T eDRAM and 1,000x lower refresh power than eMRAM due to non-destructive read and comparable write speed due to faster switching. AOS channel FeFETs a potential candidate for high density embedded memory in scaled CMOS technology nodes.

# I. INTRODUCTION

In recent years, the rise of artificial intelligence (AI) has driven a significant increase in the development of domain-specific accelerators tailored for tasks such as graphics, deep learning, autonomous systems, natural language processing, and edge computing [1-15]. These advancements have amplified the demand for high-density, high-performance non-volatile memory solutions with low standby power, presenting a compelling alternative. As these accelerators continue to evolve, the integration of non-volatile on-chip memory becomes increasingly essential to meet the stringent performance and power requirements of modern applications [15]. FeFETs have potential to facilitate scalable and CMOS-compatible embedded non-volatile memory (eNVM), aligning with the scaling requirements of advanced logic technologies [16]. However, FeFETs encounter challenges including high switching voltages exceeding 2V, relatively low endurance, ranging from cycles $10^{7}$ to $10^{9}$ , trap generation in the interfacial layer (IL) under high electric field, degraded ferroelectric properties in ultrathin HZO layers [12]. These issues pose significant hurdles for the integration of FeFETs into advanced CMOS logic circuits. To address these challenges, AOS channel FeFETs are emerging as promising candidates for integration into high density novel memory technologies within advanced CMOS logic, thanks to their superior fabrication compatibility and exceptional scaling properties with BEOL compatibility. In this work, we introduce a BEOL compatible W-doped Indium Oxide $(\mathrm{In}_2\mathrm{O}_3)$ FeFETs in an 1T-1FeFET eDRAM which can enable refresh free high density on-chip memory for last-level cache (LLC) with a record-low operating voltage of less than 0.9V, achieving a switching speed of 20 ns and an on/off ratio exceeding $10^{3}$ . The device demonstrates

write endurance over $10^{12}$ cycles and retention beyond $10^{4}$ seconds at $85^{\circ}\mathrm{C}$ . Additionally, we have conducted read speed measurements and confirmed read endurance surpassing $10^{12}$ cycles, indicating excellent persistence performance. Furthermore, we also incorporate a 1T-1FeFET array level analysis in TCAD mixed mode simulation for program, read, erase and disturb operation to ensure the impact of floating node of gate of unselected cells is minimized.

# II. FABRICATION PROCESS

Fig. 4(a) and Fig. 5(a) illustrate the schematics of the fabricated BEOL IWO FeFET and MOSFET, respectively. Both devices feature a $5\mathrm{nm}$ layer deposited using PEALD: HZO for the FeFET and $\mathrm{HfO_2}$ for the MOSFET, at $250^{\circ}\mathrm{C}$ . For the FeFET, a W sacrificial capping layer (SCL) is added to stabilize ferroelectricity, followed by rapid thermal annealing at $400^{\circ}\mathrm{C}$ for 300s in $\mathrm{N}_2$ and subsequent etching. Both devices have $4.5\mathrm{nm}$ of $1\%$ W-doped Indium Oxide (IWO) sputtered in $0.02\mathrm{Pa}$ excess $\mathrm{O}_2$ at room temperature. Pd source and drain electrodes are patterned, with a post-metal anneal at $150^{\circ}\mathrm{C}$ in $\mathrm{N}_2$ , keeping the entire process within $400^{\circ}\mathrm{C}$ for BEOL compatibility. Fig. 4(c) shows a false-colored cross-sectional STEM image and Fig. 4(d) provides EDS mapping of the IWO FeFET, confirming element locations. Fig. 5(b) presents the DC transfer characteristics of the BEOL IWO MOSFET with an on/off ratio $>10^{11}$ at $\mathrm{V_{DS}} = 1\mathrm{V}$ .

# III. ELECTRICAL CHARACTERIZATION RESULTS AND DISCUSSION

The MFM (W/HZO/W) and MFIM (W/HZO/IWO/Pd) devices, both incorporating a $5\mathrm{nm}$ HZO layer, were characterized to assess their polarization response and endurance (Fig. 6 and Fig.7). Both devices demonstrated robust high endurance under $50\%$ switching stress conditions, withstanding up to $10^{11}$ cycles without any breakdown, and exhibited reasonable effective $2\mathrm{Pr}$ . Dual DC transfer characteristics of IWO FeFET have been shown in Fig. 8(a) for different $\mathrm{V_{PRG}}$ and $\mathrm{V_{ERS}}$ . A steep switching is observed in the transfer curves during polarization switching from the PRG to ERS state (reverse sweep). A physics-based model, validated against a TCAD simulation, indicates that this steep switching is primarily influenced by the inner-fringing field near the source and drain regions in the absence of holes in the IWO channel. Fig. 8(b) shows the MW of $\sim 1\mathrm{V}$ and $\mathrm{I_{LVT}}/\mathrm{I_{HVT}} = \mathrm{Current~Window~(CW)} > 10^{6}$ for $\mathrm{V_{PRG}}$ and $\mathrm{V_{ERS}}$ from $\pm 2\mathrm{V}$ to $\pm 0.9\mathrm{V}$ . Variation of CW and MW for different gate length has been illustrated in the box plots of Fig.8(c) and 8(d). The

higher MW and CW of the scaled devices can be attributed to the amplified influence of the fringing field in shorter channel devices, leading to a greater portion of negative polarization being switched during the program to erase operation. Measured $\mathrm{I_D - V_G}$ using a single program and erase pulse of $\pm 2\mathrm{V}$ , 20 ns showing a 1V MW.

Next, we characterized the fast write and read operations of the IWO FeFET using a one-shot measurement scheme with rapid read-out. As shown in Fig. 9(a), a CW of approximately $10^{3}$ was achieved with voltages as low as $\pm 0.9\mathrm{V}$ and a pulse width of 20ns. This measurement was repeated for 85 devices across the die to determine the lowest operating voltage condition. We observed that nearly $33\%$ of the devices could be switched with $< 1\mathrm{V}$ and a 20ns pulse width. This can be attributed to the classical nucleation switching theory model, which suggests that polarization switching in FeFETs is limited by domain nucleation within the range of $\sim$ ps. Fig.9(c) shows a full transient measurement demonstrating the absence of read latency, using a continuous $\mathrm{V_{DS}}$ and a fixed current compliance of $10\mu \mathrm{A}$ , which increases the noise floor and limits the minimum measurable current compared to DC characteristics. Multiple transient measurements exhibit high-speed, low-voltage operation with $\pm 1\mathrm{V}$ and 20ns pulses. Measured instantaneous read-after-write latency of less than 100ns was observed in Fig. 9(d), a significant improvement over conventional Si FeFETs.

After that, we conducted a bipolar write endurance experiment on our BEOL IWO FeFETs under $\pm 1\mathrm{V}$ , 20ns stress pulses with a 100ns delay between pulses (Fig. 10(a)). Stress cycling increased the subthreshold swing (SS) and reduced the current window (CW) at a fixed $\mathrm{V}_{\mathrm{Read}}$ (Fig. 10(a) and (b)). This degradation is attributed to the generation of interface trap density $(\mathrm{N}_{\mathrm{it}})$ at the HZO/IWO interface due to repeated polarization switching. The retention characteristics of the IWO FeFET exhibit a stable read current margin for both program and erase states at room temperature and $85^{\circ}\mathrm{C}$ for up to $10^{4}$ seconds (Fig. 10(c)). Fast read speed characterization was performed off-chip with a 50ns read measurement, featuring rise and fall times of 10ns showing stable read operation without any degradation. The inset shows the measurement setup, utilizing a signal generator and oscilloscope to accurately capture the read speed performance (Fig.10(d)). After this measurement, we have performed the read endurance of our device (repeated reading). The IWO FeFET shows almost no degradation up to $10^{12}$ cycles for a -0.2V, 50ns read stress with a 100ns delay between the pulses. Read disturb was measured using a straightforward measurement technique referring Fig.10(c). IWO FeFET demonstrated stable performance across -0.5V to 0.9V, with disturbances in the HVT state starting after 1 second at 0.9V (Fig.10(d)).

# IV. IWO 1T-1FEFET ARRAY OPERATION

An all-positive voltage scheme can be used to program, erase, and read the memory in a 1T-1FeFET array. For programming (Fig.12 (a)), apply $\mathrm{V_P}$ (1V) to the FeFET gate while grounding the S-D terminals. For erasing (Fig.12(c)), ground the gate and apply $\mathrm{V_E}$ (0.6V to 0.9V) to the S-D terminals to ensure a negative $\mathrm{V_{GS}}$ and flip the polarization. Mixed Mode Simulations in Sentaurus TCAD, shown in Fig.

13, help assess the required biases to ensure proper gate charging during programming and minimize the impact of floating gates of unselected cells during erasing. In the 1T-1FeFET array, cells in the same row share the same WWL (connected to the access transistor gate) and RWL, while cells in the same column share the same WBL and RBL, allowing for row-wise program/erase and column-wise read operations.

Program Operation: The WWL is raised to $\mathrm{V_B}$ (1.4V) to turn on the access transistor, and WBL is set to $\mathrm{V_P}$ (Fig.13(b)). This charges the FeFET gate in the target cell to 1V, with RWL and RBL at 0V, resulting in a positive net gate potential, thus programming the target cell. After programming, WBL is set to 0V, and the access transistor is turned off by returning WWL to 0V. For unselected cells in the same row, WBL is set to 0V to ensure no write-disturb, as their gate-source-drain potential remains 0V.

Erase Operation: (Fig.13(b)) All RWL and RBL are raised to $\mathrm{V_E}$ . For the target cell, the access transistor is turned on by raising WWL to $\mathrm{V_B}$ and WBL to 0V, achieving a net negative bias at the FeFET gate, leading to an erase operation. For unselected cells in the same row, WBL is set to $\mathrm{V_E} / 2$ to give a write disturbance of $-\mathrm{V_E} / 2$ . To prevent unwanted erases in unselected cells in different rows, a pre-charge operation is performed to set their gate potential to $\mathrm{V_E} / 2$ before the erase operation.

Read Operation: (Fig.13(b)) An entire column is read simultaneously by raising RBL of the target column to 0.1V, setting RWL to 0V, all WWL to $\mathrm{V_B}$ , and applying $\mathrm{V_R}$ (0.2V) to WBL. The current through each RWL is then measured to identify stored data. For unselected columns, RBL and RWL are kept at 0V and WBL is set to 0V to prevent leakage current.

# V. CONCLUSION

We demonstrate BEOL-compatible IWO 1T-1FeFET which can enable refresh free high density on-chip memory for last-level cache (LLC) with a record-low operating voltage of less than $0.9\mathrm{V}$ , achieving a switching speed of 20 ns and an on/off ratio exceeding $10^{3}$ with $>10^{12}$ write and read endurance along with $>10^{4}$ sec retention at $85^{\circ}\mathrm{C}$ . We also simulate a 1T-1FeFET array with an accurate program, erase, and read scheme using Mixed Mode Simulations in Sentaurus TCAD, ensuring reliable operation and performance optimization.

# REFERENCES

[1] T. -E. Lee et al., IEDM 2023 [2] F. -X. Liang et al., IEEE TED, 2024 [3] Z. Cai, K et al., VLSI 2023 [4] Dahan et al., Nano Letters 2023 [5] Y. Zhou et al., IEDM 2022 [6] Lin et al., VLSI 2022 [7] C. -Y. Liao et al., IEDM 2022 [8] X. Wang et al., VLSI 2023 [9] C. -K. Chen et al., IEDM 2022 [10] Y. -R. Chen et al., VLSI 2023 [11] C. -Y. Liao et al., VLSI 2022 [12] S. Dutta et al., IEEE EDL 2022 [13] Z. Lin et al., IEDM 2021 [14] S. Dunkel et al., IEDM 2017 [15] H. Ye et al., IEDM 20 [16] M. I. Popovici et al., IEDM 2022 [17] D. Edelstein et al., IEDM 2022 [18] K. C. Chun et al., IEEE JSSC 2012.

# ACKNOWLEDGEMENTS

Acknowledgment: This research is sponsored from EMD Performance Materials and SRC/DARPA sponsored PRISM center,

# High Performance BEOL Compatible AOS FeFET for 1T-1FeFET eDRAM with Peripheral CMOS Under Array

![](images/eb50b437bc7d047ca275006a47a45fa89c5934d6043a6510517fee9fe88f4a13.jpg)

![](images/be4cff874640591bc9f78ab5db9979752e8cacb12ddbcb9652eaff9757451fab.jpg)  
Required FeFET as Read Transistor Properties:

- Low Operating Voltage (<1.2V)
- Fast Write and Read Operation.
- High Endurance ( $>10^{10}$ ) and

$\checkmark$ High retention $\checkmark$ Low leakage Current

![](images/cf58a686cb3ec7d15efd163edc63d896cdee68bae3b4ad7a5282a99cac11822c.jpg)  
Fig.1. (a) 1T-1FeFET eDRAM can enable refresh free high density on-chip memory for last-level cache (LLC). BEOL compatible AOS FeFET allows non-volatile high memory density, high retention time, faster access time. Fig.2. Comparison of embedded storage technologies' timing and standby power performance.

# Fabrication of BEOL IWO FeFET

![](images/1a0ac89b3975c7af4edbf22e27750ffdb062f1a48c59de7df73d1c0f490af2ab.jpg)  
(a) Back Gate(BG)

Rapid thermal annealing

Source drain patterning

RF Sputter of IWO channel

Deposit Sacrificial W Layer

Crystallization anneal

PEALD HZO

DC Sputter W back gate

![](images/37da08b9d1ef36473ddd061cf2f46c86386ff131adc96c0eac1146a0b2b45e95.jpg)  
Fig. 4. a) Schematic device structure and process flow of BEOL IWO FeFET. (b) Measured DC transfer characteristics of IWO FeFET with $\mathrm{LG} = 50\mathrm{nm}$

![](images/6ae58a352e1da55ebc3ad359a187572b8e837d48378afb878a2632b4ae22ad14.jpg)

![](images/87b37a4c893f7a8891c1589c9b7ad7af5470e71cc98a714ab715fe3d3bceae43.jpg)

![](images/743828d5fdab2035ba46e3a47287ffb12c682c3108a2ae0f7c6b8feb16ea46da.jpg)

![](images/6a36fc601da6ae8da60e896a77bef60df8df8abb6a4c91a1d6ab39693815bdcd.jpg)

![](images/f13a66b0b1cd98571ff9162d4c54817027aed27801c29a612766fd23496c02f9.jpg)

![](images/1cdd031afedc408c9c3736d0b9eed7aac5cecf3a8e1a5a9c641f80208b07187e.jpg)

# Key highlights of this

# work

Low Energy Consumption: Record low (0.9V) program/erase voltage with $>10^{3}$ current window.

# High Speed:

Ultra fast switching at 20 ns  
Fast read $< 50$ ns

# Write Endurance:

Ultra-high measured write endurance $>10^{12}$

# Refresh-free:

Read endurance $>10^{12}$ Superior retention $>10^{4}$ sec at $85^{\circ}\mathrm{C}$

![](images/4145739119e30b95730beb2c0d60b962eeaf65e1e4b3ea408300fd135215732c.jpg)

![](images/42ef75534ae41785ae2def46bbeefe3ee827d9384b6da4a59444306136867b71.jpg)  
Fig.3. Benchmarking: (a) IWO FeFET achieves highest $\mathrm{I_{on} / I_{off}}$ ratio (in pulsed mode) with record low write voltage of 0.9V with fast switching speed of 20ns. (b) It exhibits write endurance $>10^{12}$ cycles. This makes IWO FeFET a contender for high-density, low-power, fast, refresh-free embedded memory, compatible with CMOS.

# Fabrication of BEOL IWO MOSFET

![](images/7626e656cb435f8627dcec994fba7dda7ef74bc7e2db3775f98deb475f36bf50.jpg)  
Back Gate(BG) IWO MOSFET  
(a)

![](images/92f2f629fb77d65ae7479e315158ac6b60f211359152a5658a9170e41f5ec476.jpg)

Annealing

S/D patterning

Sputter IWO at 25C

PEALD HfO2at 2500

Sputter W back gate

Fig. 5. a) Schematic device structure and process flow of BEOL IWO MOSFET. b) Measured DC transfer characteristics of IWO BG MOSFET with $\mathrm{L}_{\mathrm{G}} = 50\mathrm{nm}$

# MFM and MFIM Characterization

![](images/5e0edeff403ef1eb02746e94b87c8811fe0370fff431c64d6dc9cbfbe37e6a3e.jpg)  
Fig. 4. c) Cross sectional STEM image of IWO FeFET d) EDS mapping of the cross section of the IWO FeFET confirming all the elements' location.

![](images/43987ee5775840c3d95736b83b35eb5033822ebe45a3762d739119cc83e98b5c.jpg)

Fig. 6. a) PV response of $5\mathrm{nm}$ HZO MFM shows $2\mathrm{P}_{\mathrm{r}}$ of $45~\mu \mathrm{C} / \mathrm{cm}^2$ b) For bipolar stress of $50\%$ switched polarization conditions, $5\mathrm{nm}$ HZO MFM shows endurance $>10^{11}$ cycles (No breakdown).

![](images/1f4feba8b3b2dfcc4501af95bf90c936efc06f48580013fb14b087207260cdc8.jpg)  
(a)

![](images/6dd5a445a51a6142d63f0c4cba9b2a2e7dae9a3a9839220e0a029beaecc4a3a8.jpg)

Fig. 7. a) PV response of $5\mathrm{nm}$ HZO/IWO MFIM shows $2\mathrm{P}_{\mathrm{r}}$ of $22~\mu \mathrm{C} / \mathrm{cm}^2$ b) For bipolar stress of $50\%$ switched polarization conditions, no breakdown observed till $>10^{11}$ cycles.

# Electrical Characterization of BEOL Compatible IWO FeFET

![](images/34fc026faba41fa787218ceedb5a59b3a960c8bbcbf382f8843acc6f7014ae07.jpg)

![](images/46ac30e2e90043195a5076ca8270b9d0d143d888534187c8653f8897d409dcbb.jpg)

![](images/2e53235340a8ffb85ac79e2d9bf1a1bf02bbce4e49050386dffe3294c53a84c4.jpg)

![](images/107f8b90efab3bb60f020f901913409878f935f7a111326c21feff546612a718.jpg)

![](images/aa89ca1272608990f1c4850b2a2a9db107f6f6a2edb213cfc9d5ffcd0a9afad2.jpg)  
Fig. 8. (a)DC Transfer Characteristics of IWO FeFETs at varying $\mathrm{V_{PRG}}$ and $\mathrm{V_{ERS}}$ for $\mathrm{L_G = 50nm}$ showing HVT - LVT = Memory Window (MW) of 1V and $\mathrm{I_{LVT}} / \mathrm{I_{HVT}} =$ Current Window (CW) $>10^{6}$ . (b) Program and erage voltage dependence of $\mathrm{I_{LVT}}$ and $\mathrm{I_{HVT}}$ for IWO FeFETs, demonstrating a stable MW up to $\mathrm{V_{PRG}} = 0.9\mathrm{V}$ with 1V MW at $\mathrm{V_{read}} = -0.25\mathrm{V}$ . (c) Variation of drain current at fixed $\mathrm{V}_{\mathrm{GS}}$ for different $\mathrm{L}_{\mathrm{G}}$ devices show higher drain current for scaled FeFETs. (d) Dependence of MW on $\mathrm{L}_{\mathrm{G}}$ also shows similar trend. (e) Pulsed $\mathrm{I_d - V_g}$ characteristics for IWO FeFETs showcase MW and CW with pulses of 20ns duration.

# Ultra-fast operation of BEOL Compatible IWO FeFET

![](images/8c17f1d6b496858a35d1d493a4f8505582a7a3411de7fde35aed6356496d9a13.jpg)

![](images/b649b52468b6f99d77be621081338c30423f81e068f78ce615631ffe8e57e491.jpg)

![](images/27cfaad4d096478ad8979df3bd02fe901548b57647eaf1231cd53419f4d1c952.jpg)

![](images/b2797fa811f120ecc69b9fd87f07083b8ab87d14a315b204df255c9422629c94.jpg)  
Fig. 9. (a) Ultra-fast switching characteristics of the IWO FeFET using program and erase pulses. At 20ns, above 0.9V, FeFET shows maximum current window (limited by current compliance and higher noise floor) (b) Histogram showing the distribution of the lowest operating voltage required to achieve a current window $(CW > 10^{3})$ for 85 devices with a 20ns pulse width which can be attributed to process variations and inherent multi-grain, multi-phase nature of ferroelectric HZO.   
Fig. 9. (c) Transient measurements show program and erase operation with $\pm 1\mathrm{V}$ and 20ns pulses, and nearly instantaneous read-after-write operation.   
Fig. 9. (d) Measured read after delay for IWO FeFET shows read latency of 100ns without any degradation which is orders of magnitude improvement over conventional Silicon FeFET

# Endurance, Retention and Read Speed Characteristics of IWO FeFET

![](images/cf0cab91187b19477b34a9c3841c3a97e7e1e45a4b7537e1a2aad4f2dddddf91.jpg)

![](images/08a9eb26cd6560fe6e67ef451e7ab89e585c28a9ba031acdd528982f615a826a.jpg)

![](images/984eae6aec328f77708cd9102b890728d4c28222ab91d27abf2b6ee70e9e8cd1.jpg)

![](images/baa2732d353a7defae059a659d5a3984a3be8cd4923eb48a532f68d1dbdf9e27.jpg)  
Fig. 10. Bipolar write endurance of IWO FeFET showing (a) stable transfer characteristics and (b) adequate read current window up to $10^{12}$ cycles. The stress pulse used for the test is the switching condition $\pm 1\mathrm{V}$ , 20ns. (c) Retention characteristics of IWO FeFET shows stable read current margin for program and erase states at room temperature and $85^{\circ}\mathrm{C}$ upto $>10^{4}$ sec. (d) Fast read speed characterization setup (off-chip) with a 50ns read measurement, featuring rise and fall times of 10ns. The inset shows the measurement setup using a signal generator and oscilloscope to accurately capture the read speed performance.

# Read Endurance and Read Disturb Characterization

![](images/3e08ec168aa10f9b8d74c1eee9bbd3e409b54090237fbee562f90e9c140801df.jpg)

![](images/5530cac72868836f8868084f40f85ec1610342115b358027e59fd3447db02819.jpg)

![](images/7a54078472fec130b6eb25938d5676a3a2bceca266ed6267a159ef6d23fbccdf.jpg)

![](images/456af67d69c83def1753c5ec8dcc3e1723ad71f93dacc038c42fa66e803f656a.jpg)  
Fig. 11. (a) Read endurance measurement of IWO FeFET with read stress of -0.2V, 50ns. DC transfer characteristics were measured after each decade of pulses. (b) There is no noticeable degradation observed for repeated reading of the devices which can be attributed to good interface of FeFETs. (c) Read disturb measurement setup involved applying the full range of read voltages from -0.5V to 0.9V for durations between 1 $\mu$ s and $10^{3}$ seconds after program/erase cycles, followed by a state check. (e) Read disturb measurements demonstrated stable performance across -0.5V to 0.9V, with disturbances in the HVT state starting after 1 second at 0.9V.

# Array Level Characteristics: Program and Erase Scheme for 1T-1FeFET Array

![](images/175ce88899d72d3104c00b2c7da273a36ea5bdf1353baf0890bab2fe346eccf4.jpg)

![](images/d82d0f034ec6da73fc0b89eb89b8d1866b1f74dac69c539393474c8e9e71f3b0.jpg)

![](images/78c6fe2c49d04c9663deaa2573cf802ff9fbe0ef45a53f4030331373bb4c7283.jpg)  
Fig.12: Program, Erase, Read scheme for 1T-1FeFET array, where the FeFET is the storage element, and its drain current is used for a memory read-out. (a) The Program scheme with negligible disturb on the selected cells in the same as well as different rows (b) Erase scheme with a pre-charge scheme to minimize disturb on the unselected cells, with $-\mathrm{V}_{\mathrm{E} / 2}$ disturb on the unselected cells in the same row and $\mathrm{V}_{\mathrm{E} / 2}$ in different row. (c) Parallel read-out, where an entire column can be read simultaneously without disturb on the unselected columns.

# BEOL AOS 1T-1FeFET Cell Operation

![](images/e94f7c1d8b0d27c8b6ff00f0480e32568ae5b4ecfee687872ab501b6d0011d20.jpg)

![](images/c46aa1e59b0bbdac0641416d31d3a3660f237a07434f3274f12a502fc58fe611.jpg)

![](images/27ba535f7678acc777e5d0b53fa77ce6645c5368e60bb3bf7e6069cfefecaeae.jpg)  
Fig. 13: (a) 3D Schematic of BEOL AOS 1T-1FeFET Cell. b) Timing diagram of program, erase, read on target cells, and erase disturb on the unselected cells. i) Write: WWL is raised to $V_{\mathrm{B}}$ to turn ON the transistor and WBL is raised to $V_{\mathrm{P}}$ . Gate of FeFET charges up to $V_{\mathrm{P}}$ , leading to program operation. WBL is lowered back to $0V$ to prevent unwanted stress and WWL is lowered back to $0V$ , turning OFF the access transistor. (ii) Read: An entire column is read simultaneously. Access transistor of each cell is turned ON and gate of FeFET is charged to $V_{\mathrm{READ}}$ in target cell and $0V$ for unselected cells. In the same column, RBL is raised to $V_{\mathrm{D}}$ and current coming out of RWL is measured. WBL is then lowered back to $0V$ , discharging the gate of FeFET followed by turning OFF the access transistor. (iii) Erase: Access transistor of target cell is turned ON and Gate is charged to $0V$ . RWL, RBL is raised to $V_{\mathrm{E}}$ achieving a net negative gate bias. Target cell turns OFF and RWL, RBL is lowered back to $0V$ , followed by turning OFF the access transistor. (iv) Erase Disturb: unselected cell in the different row: In the unselected row, the gate of FeFET is a floating node and hence can be at any potential. Hence, a precharge operation is introduced prior to Erase operation, where the gate is charged to $V_{\mathrm{E2}}$ , followed by erase operation on the target cell. (v) Erase Disturb: unselected cell in the same row: The access transistor is ON. Hence, the gate is charged to $V_{\mathrm{E2}}$ while RWL, RBL is raised to $V_{\mathrm{E}}$ , achieving a disturbance of $-V_{\mathrm{E2}}$ . (c) Comparison of different on chip memory options demonstrating AOS 1T-1FeFET to exhibit desired characteristics of refresh free high density on-chip memory for last-level cache (LLC).

<table><tr><td>Parameter</td><td>eMRAM[17]</td><td>eDRAM[18]</td><td>AOS 1T-1FeFET(this work)</td></tr><tr><td>Access Time</td><td>5-20ns</td><td>1.5 ns</td><td>20 ns</td></tr><tr><td>Retention Time</td><td>1s-60s</td><td>100-1000us</td><td>&gt;104s</td></tr><tr><td>Write Energy/bit</td><td>300-600fJ</td><td>3-5 fJ</td><td>6.7 fJ</td></tr><tr><td>Write Voltage</td><td>0.6V-1.5V</td><td>0.7-1.2V</td><td>&lt;1V</td></tr><tr><td>BEOL Compatibility</td><td>Partially</td><td>No</td><td>Yes</td></tr></table>