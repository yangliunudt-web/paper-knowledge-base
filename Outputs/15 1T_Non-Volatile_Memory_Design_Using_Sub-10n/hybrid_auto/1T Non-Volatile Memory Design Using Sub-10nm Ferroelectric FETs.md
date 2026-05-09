---
title: "1T Non-Volatile Memory Design Using Sub-10nm [[ferroelectric]] FETs"
authors:
  - "Ankit Sharma"
  - "Kaushik Roy"
date: "2018-01-25"
year: "2018"
journal: "IEEE Electron Device Letters"
doi: "10.1109/LED.2018.2797887"
abstract: "In this letter, we propose one-transistor ferroelectric NOR type (Fe-NOR) non-volatile\\"
abstract_cn: "本文提出基于 HfZrOx 铁电场效应晶体管的单晶体管铁电 NOR 型 (Fe-NOR) 非易失性存储器。利用超短沟道 FeFET 中增强的漏极-沟道耦合来动态调制存储单元的存储窗口，简化擦除、编程和读取操作。仿真分析预测所提\\"
keywords:
  - "[[FeFET]]"
  - "[[Non-volatile memory]]"
  - "[[Fe-NOR]]"
  - "[[HfZrOx]]"
cite: "[1] Sharma A, Roy K. 1T Non-Volatile Memory Design Using Sub-10nm Ferroelectric FETs[J].\\"
aiSum: "提出基于 HfZrOx FeFET 的 1T Fe-NOR 非易失性存储器，利用超短沟道增强的漏极-沟道耦合动态调制存储窗口，实现亚 1V 编程/擦除电压和简化操作。"
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
---

# 1T Non-Volatile Memory Design Using Sub-10nm [[ferroelectric]] FETs

Ankit Sharma and Kaushik Roy, Fellow, IEEE

Abstract—In this letter， we propose one-transistor ferroelectric NOR type (Fe-NOR) non-volatile memory based on HfZrOx ferroelectric FETs ([[FeFET]]s). The enhanced drainchannel coupling in ultra-short channel FeFETs is utilized to dynamically modulate the memory window of storage cells, thereby resulting in simple erase-, program-, and read-operations. The simulation analysis predicts sub-1V program/erase voltages in the proposed Fe-NOR memory array and, therefore, presents a significantly lower power alternative to conventional [[FeRAM]] and NOR flash memories.

Index Terms-Ferroelectric FET (FeFET)， negativecapacitance FET (NCFET), NOR-flash, FinFETs.

# I. INTRODUCTION

FERROELECTRIC FETs (FeFETs), consisting of ferro- electric in the gate-stack of conventional MOSFET, have attracted considerable attention for future ultra low-power nonvolatile memory applications [1]–[3]. They show excellent features such as nonvolatility, better scalability and energyefficient switching with non-destructive read-out. Furthermore, their high distinguishability between two states compared to spin-based memories [4], and high endurance compared to resistive RAMs [5], phase change memories [6] and flash memories make them outstanding candidates for future non-volatile memory applications.

Traditionally, ferroelectrics like PZT and BTO have been used in ferroelectric capacitor memories (FeRAMs) [7]. However, their incompatibility with semiconductor technology, poor scalability and destructive read operation has posed serious limitation compared to several competing memories [8]. Recent discovery of ferroelectricity in hafniumoxide [9]–[12] has overcome shortcomings of FeRAMs and revived interest in scalable ferroelectric-gate type memories. Fast progress has been made in this segment whereby FeFETs with fast switching (∼10ns), retention of ∼10 years [13] and endurance of ${ \sim } 1 0 ^ { \circ }$ [13] cycles have been demonstrated.

Previously, George et al. [14] reported 2T FeFET memory with low read/write energy and superior characteristics

Manuscript received January 4, 2018; accepted January 22, 2018. Date of publication January 25, 2018; date of current version February 22, 2018. The review of this letter was arranged by Editor B. S. Doyle. (Corresponding author:Ankit Sharma.)

The authors are with the School of Electrical and Computer Engineering, Purdue University, West Lafayette, IN 47907-1285 USA (e-mail: sharm142@purdue.edu).

Color versions of one or more of the figures in this letter are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/LED.2018.2797887

![](images/51b854028223a929623900582ff3631679a67192d367d000f35a8d05be95e80c.jpg)  
Fig. 1. A 2 × 3 FeFET memory array with 2T per cell [14].

compared to 1T FeRAMs, albeit a slight area penalty due to 2T design. The design, reproduced in Fig. 1(a), consists of a FeFET and a conventional MOSFET as an access transistor. In this letter, we propose 1T Fe-NOR memory by getting rid of the access transistor. This is made possible by dynamically modulating the memory window (MW) of FeFETs. We utilize ultra-scaled 5nm gate-length FinFET to design FeFET as a memory element which achieves sub-1V write/erase voltages whilst greatly simplifying the program/read operations compared to existing Fe-NAND realizations [15].

The rest of the letter is organized as follows. Section II lays the background about origin of hysteresis in FeFETs. In Section III, we propose 5nm gate-length FeFET as a 1T memory element, describe the device simulation methodology and explain the operating principle. In Section IV, we utilize the proposed FeFET in a prototype 3 × 3 FeFET array and describe the voltage conditions for program, erase and read operations. The impact of gate-length and ferroelectric material variations is discussed in Section V. Finally, we summarize our findings in Section VI.

# II. BACKGROUND - HYSTERESIS IN FEFETS

In the past, several works have focused on the design of hysteresis-free negative capacitance FETs (NCFETs) for low-power logic applications. In our previous work, it was shown that the FinFET configuration greatly benefits the NCFET performance due to their undoped body and improved great control, which enables better capacitance matching with the ferroelectric [16]. A hysteresis-free NC-FinFET operating down to 0.25V was predicted using 3nm FE-HZO. A higher ferroelectric thickness induces hysteresis in the transfer characteristics due to presence of two valleys in the net-free

![](images/e18c36fbff3e103d00fc7a1c27c11ed609535b780a89d9e654f5cad7699a7d9c.jpg)

![](images/8a136b51e787f4babffe4c1e4a5b35998bcf853262ea1e1e6eea4144ddb54a22.jpg)

![](images/6446ace758f705fe8a020cddca7b827a2784209dfed671c2c6b17c71f27718aa.jpg)  
Fig. 2. (a) FE, MOS and $U _ { T O T A L }$ vs. charge en $U _ { S U P P L Y } = 0$ U U UThe total energy of the system shows two minima, i.e. two U .stable polarization states A and B. (b) Band-diagram from gate to channel for polarization states A and B.

![](images/deffcea877557afea5d34f5b4f39c16ff20a4b004632f5401569ede4dce811c5.jpg)

![](images/335e895e515f20951a41d7ecba7bc555aa4b859e987f38b22975742396dc246f.jpg)  
Fig. 3. (a) Schematic of 5nm FeFET. (b) Charge-internal voltage $( V _ { g s } )$ Vgscharacteristics of FinFET for low and high drain bias. An equivalent capacitance network of FeFET shown in the inset highlights the nomenclature of node voltages in the FeFET.

energy-charge curve of the system. This can be explained by writing the total free-energy of the system, UTOTAL as:

$$
U _ {T O T A L} = U _ {F E} + U _ {M O S} + U _ {S U P P L Y} \tag {1}
$$

where UFE, UMOS and USUPPLY are the free energies of the ferroelectric, the underlying MOSFET (dielectric and semiconductor channel) and the external supply, respectively. Fig. 2(a) plots these individual components w.r.t charge for an arbitrary ferroelectric-MOSFET combination designed in the hysteretic regime, assuming the supply is grounded $( { \mathrm { i . e . } } U _ { S U P P L Y } = - Q . V _ { D D } = 0 )$ . The net free energy of the system exhibits two stable minimas, labeled as A and B, separated by an unstable negative capacitance region - ∂2 UTOTAL −1 < 0. $\left( \frac { \hat { \sigma } ^ { 2 } ~ U _ { T O T A L } } { \hat { \sigma } O ^ { 2 } } \right) ^ { - 1 } < 0$ ∂ Q2 Fig. 2(b) shows the band-diagram from gate-to-substrate in both cases of stable polarization. A -ve ferroelectric polarization piles up holes in the channel leading to extremely low OFF-current through the transistor. On the other hand, a +ve polarization of the ferroelectric leads to strong inversion in the channel which represents the ON-state of the transistor. The polarization state can be switched from A to B and vice-versa via application of appropriate positive and negative gate-voltage respectively. The wide difference between the sense currents corresponding to the two polarization states greatly simplifies the read operation leading to simple sense and control circuitry. In the following sections, we introduce 5nm gate-length FeFETs and describe their operation in a 1T memory array.

# III. FEFET DESIGN AND SIMULATION METHODOLOGY

Fig. 3(a) shows the schematic of intrinsic-channel silicon FeFET with drawn gate length of 5nm and fin-thickness of 3nm. An interfacial dielectric $( { \mathrm { S i O } } _ { x } )$ thickness of 0.7nm is assumed while 9nm HfZrOx ferroelectric (FE-HZO), with

![](images/134d6c7803c7118264ee7f5ef6be61efddaaba90a5f88edcc74da4cfd2335c46.jpg)

![](images/d07ab3a8bf4aa50e35d0113ebb5ed456b32e646db6e7706a88b426e5cd3751bd.jpg)  
Fig. 4. (a) MOS vs charge for low and high drain bias. (b) TOTAL Uvs charge for low and high drain bias at ${ V _ { G S } } = 0 V$ U(dashed curves). V VAlso, shown is the curve for state transition from A to B (attained at $V _ { G S } = 0 . 3 V )$ , for low drain bias.

$P _ { R } = 3 \mu C / c m ^ { - 2 }$ and $E _ { C } = 1 . 4 ~ M V / c m ,$ is used [16]. The source/drain doping is set to 1 × 1020cm−3. $1 \times 1 0 ^ { 2 0 } c m ^ { - 3 }$

A physics-based device simulation is necessary at sub-10nm scale to capture quantum mechanical effects that manifest at such scales. To simulate the underlying FinFET in the FeFET structure, we use quantum physics-based NEMO5 simulator [17]. The device simulation involves self-consistently solving the ballistic 2-D nonequilibrium Greens function equations of transport in the Si fin by using an atomistic $s p ^ { 3 } \bar { d } ^ { 5 } s ^ { * }$ tight-binding basis together with the 2-D Poisson equation for electrostatics in the fin cross-section. The energy stored in the FinFET, $U _ { M O S } ,$ , is obtained by $\begin{array} { r } { \int _ { 0 } ^ { Q } V _ { g s } d Q . } \end{array}$ , where $V _ { g s }$ is the internal voltage at ferroelectric-dielectric interface (see inset in Fig.3(b)). $U _ { F E }$ is dictated by L-K theory of ferroelectrics [18] and is given by, $U _ { F E } = \alpha \dot { Q ^ { 2 } } + \beta Q ^ { 4 } + \stackrel { . } { \gamma } Q ^ { 6 }$ , where $\alpha , \beta ,$ and γ are the Landau parameters for the ferroelectric [16]. Eqn.1 is then used to calculate net-free energy of the FeFET. The charge corresponding to the energy minimas gives the current through the FeFET at a given external gate-bias, $V _ { G S } .$

Fig. 3(b) compares $Q - V _ { g s }$ characteristics of the underlying FinFET structure for low and high drain-bias. A high drainbias of 1V depletes the channel of free carriers, thereby significantly lowering the net charge available in the channel. Hence, for a given amount of channel charge, a higher gate bias needs to be applied when the drain bias is high. As a result, a higher energy is stored in the underlying FinFET as shown in Fig.4(a). Fig.4(b) shows the net energy of the FeFET $( U _ { T O T A L } )$ , at different bias conditions. At a lower drain bias, the net energy of the system is lower, hence a higher gatevoltage is needed to switch the polarization from A to B. In the structure described above, it is observed that $| V _ { G S } |$ of 0.2V is needed to switch the polarization when $V _ { D S } = 1 . 0 V$ , while a higher $| V _ { G S } | = 0 . 3 V$ is required to switch the polarization when $V _ { D S } = 0 . 1 V$ . It is worthwhile noting that the dynamic control of the switching voltage, via drain bias, is facilitated by enhanced drain-channel coupling due to ultra-short gatelength. Higher gate-lengths would lead to convergence of the switching voltages w.r.t drain bias and render 1T memory design difficult, as described later in Section V.

Fig.5 compares the transfer characteristics for the FeFET at two different drain bias. A higher drain bias results in a narrower memory window (MW), defined as the difference between the threshold voltages for the two different polarization values, thereby making switching feasible at a lower $V _ { G S }$ . We utilize this property to design a 1T FeFET based memory

![](images/39ec5bf5a7641eb07ac61f3d1847c4e98bb8a81410aa638493ff7310815edaf9.jpg)

![](images/d43d1c5416d8783122b5796b0fa523a1ee67be64b60e5d462b0d7f435ef212e8.jpg)  
Fig. 5. (a) $I _ { D } - V _ { G S }$ characteristics of FeFET at $V _ { D S } = 0 . 1 V$ . (b) $I _ { D } - V _ { G S }$ ID Vcharacteristics of FeFET at $V _ { D S } = 1 V$

![](images/7abbd015828d445c8d644177d92cf8a4c09729af4af058db42d50f977b51a0b8.jpg)

![](images/d3b774a2ef5e0519ff1e52f59062e076fd1009cf7e9f6d0f988e6830be26bb78.jpg)  
Fig. 6. (a) Voltage conditions for write operation on the central column. (b) Voltage conditions for read operation on the central row.

array in the NOR configuration, as described in the following section.

# IV. 1T FEFET MEMORY

We consider a prototype $3 \times 3$ NOR-type array consisting of proposed FeFETs to illustrate Program, Erase and Read operations. Fig.6(a) shows the voltage conditions for writing into the central column of the array. The bitline for the column to be programmed is set to high $V _ { D S }$ , which lowers the threshold voltage to write to the FeFETs, as described in the previous section. The wordlines are subsequently set to +ve or −ve voltages satisfying $0 . 2 V < | V _ { G S } | < 0 . 3 V$ to erase $( V _ { T } < 0 V )$ or program $( V _ { T } > 0 V )$ the cells respectively while the unselected columns are inhibited by setting their bitlines to ground. To estimate the write pulse-width requirements, a careful experimental measurement is necessary to account for capacitances and switching-time of the ferroelectric, which cannot be accurately deduced from the simulations due to abrupt switching behavior.

For reading the contents of the memory array, the bitlines are precharged to a voltage, $V _ { R E A D } \mathrm { ~  ~ { ~ < ~ } ~ } 0 . 2 V$ , while the wordlines are set to 0V. The source line of the selected row is set to ground as shown in Fig.6(b). This results in a $V _ { G S } = 0 V$ across the selected cells. The erased cells $( V _ { T } ~ < ~ 0 V )$ , with much higher drive current compared to programmed cells $( V _ { T } ~ > ~ 0 )$ , consequently discharge the bitlines which can be easily read through the sense amplifier. On the other hand, the unselected rows are inhibited by floating their source lines. If any of the cells in an unselected row is conductive (i.e. $\begin{array} { r l r } { V _ { T } } & { { } < } & { 0 ) } \end{array}$ , it will charge the corresponding source line to VREAD. Any read-disturb on the unselected cells is averted by ensuring $V _ { R E A D } < 0 . 2 V$ (i.e. lower of the two threshold voltages, $V _ { T H , M I N } ;$ , of the FeFETs). This would keep $| V _ { G S } | < 0 . 2 V$ for the unselected cells and prevent their unwanted switching. Similarly, if all the unselected cells were

![](images/05057368fc0988fa1c2c9fa05a6dce039c31a2a6e5a70646541d0488f6ef7346.jpg)

![](images/830b701bb47e0b38464336737082d1f6bcf77b92e64553a057a1c243bfed34a3.jpg)  
Fig. 7. (a) Variation of 0 → 1 switching threshold vs. gate-length for low and high-drain bias. (b) histogram for $0  1$ switching threshold considering variations in $P _ { R }$ VTand $E _ { C }$ of HZO in a 5nm FeFET.

non-conductive $( V _ { T } > 0 )$ , and if the floating source line rises beyond 0.2V, the bitline acts as a source, hence $| V _ { G S } | < 0 . 2$ still holds true, which prevents accidental switching of the unselected FeFET cells.

# V. VARIATION ANALYSIS

In this section, we study the sensitivity of the switching characteristics of FeFETs to the variations in gate-length and ferroelectric material properties. Fig.7(a) shows the variation of $0 \to 1$ switching threshold w.r.t gate-length at low and high drain bias. As expected, the drain control over the channel charge reduces at longer gate-lengths, thereby leaving a narrower margin to perform disturb-free write operation. To evaluate the impact of variations in ferroelectric properties, namely $P _ { R }$ and $E _ { C } ,$ , on switching characteristics, we consider 10000 samples of normally distributed $P _ { R }$ and $E _ { C }$ values each having three-sigma (3-σ ) variation of 3% [19]. Fig.7(b) shows the resulting distribution of switching threshold, under combined variation in $P _ { R }$ and $E _ { C } .$ , for 0→1 transition at low and high drain bias. A normal distribution with 3-σ variation of 8% in switching threshold is observed for both low and high drain bias. A clear separation between the two switching threshold levels is observed, which permits successful writing into the FeFET cell using the methodology described in Section IV. However, it can be shown that this variation increases to 25%, if the variations in ferroelectric material properties is assumed to be 10%. This would necessitate the employment of appropriate error correction schemes to address write-errors arising from cells lying in the overlapping region of switching voltage distributions. Further, a relaxed placement of memory cells might be beneficial to minimize read-disturb arising due to capacitive coupling between neighboring cells.

# VI. CONCLUSION

To conclude, this work describes a realizable possibility of next generation 1T Ferroelectric-NOR type memory using 5nm FeFETs with HfZrOx ferroelectric. The dynamic modulation of memory window of FeFETs using drain bias facilitates 1T NOR configuration while also greatly simplifying the erase, program and read operations associated with Fe-NAND configuration [15]. Our simulation based analysis shows that memory array can operate with sub-1V program/erase voltages and is therefore a promising candidate for ultra-low power memory achieving ultra-high density while maintaining non-volatility. The proposed 1T ferroelectric memory is expected to expedite further research and technical developments in the memory business.

# REFERENCES

[1] S. Sakai and R. Ilangovan, “Metal-ferroelectric-insulator-semiconductor memory FET with long retention and high endurance,” IEEE Electron Device Lett., vol. 25, no. 6, pp. 369–371, Jun. 2004, doi: 10.1109/ LED.2004.828992.   
[2] L. Van Hai, M. Takahashi, and S. Sakai, “Downsizing of ferroelectricgate field-effect-transistors for ferroelectric-NAND flash memory cells,” in Proc. 3rd IEEE Int. Memory Workshop (IMW), May 2011, pp. 1–4, doi: 10.1109/IMW.2011.5873239.   
[3] U. Schroeder, S. Mueller, J. Mueller, E. Yurchuk, D. Martin, C. Adelmann, T. Schloesser, R. van Bentum, and T. Mikolajick, “[[Hafnium oxide]] based CMOS compatible ferroelectric materials,” ECS J. Solid State Sci. Technol., vol. 2, no. 4, pp. N69–N72, 2013, doi: 10.1149/2.010304jss.   
[4] K. L. Wang, J. G. Alzate, and P. K. Amiri, “Low-power nonvolatile spintronic memory: STT-RAM and beyond,” J. Phys. D, Appl. Phys., vol. 46, no. 7, p. 074003, 2013, doi: 10.1088/0022-3727/46/7/ 074003.   
[5] M.-F. Chang, A. Lee, P.-C. Chen, C. J. Lin, Y.-C. King, S.-S. Sheu, and T.-K. Ku, “Challenges and circuit techniques for energy-efficient onchip nonvolatile memory using memristive devices,” IEEE J. Emerg. Sel. Topics Circuits Syst., vol. 5, no. 2, pp. 183–193, Jun. 2015, doi: 10.1109/JETCAS.2015.2426531.   
[6] A. Chen, “Emerging nonvolatile memory (NVM) technologies,” in Proc. 45th Eur. Solid State Device Res. Conf. (ESSDERC), Sep. 2015, pp. 109–113, doi: 10.1109/ESSDERC.2015.7324725.   
[7] D. Bondurant, “Ferroelectronic ram memory family for critical data storage,” Ferroelectrics, vol. 112, no. 1, pp. 273–282, 1990, doi: 10.1080/ 00150199008008233.   
[8] A. Sheikholeslami and P. G. Gulak, “A survey of circuit innovations in ferroelectric random-access memories,” Proc. IEEE, vol. 88, no. 5, pp. 667–689, May 2000, doi: 10.1109/5.849164.   
[9] M. H. Park, H. J. Kim, Y. J. Kim, W. Lee, T. Moon, K. D. Kim, and C. S. Hwang, “Study on the degradation mechanism of the ferroelectric properties of thin $\mathrm { H f } _ { 0 . 5 } \mathrm { Z r } _ { 0 . 5 } \mathrm { O } _ { 2 }$ films on TiN and Ir electrodes,” Appl. Phys. Lett., vol. 105, no. 7, p. 072902, 2014, doi: 10.1063/1.4893376.   
[10] J. Müller, T. S. Böscke, U. Schröder, S. Mueller, D. Bräuhaus, U. Böttger, L. Frey, and T. Mikolajick, “Ferroelectricity in simple binary ZrO2 and [[HfO2]],” Nano Lett., vol. 12, no. 8, pp. 4318–4323, 2012, doi: 10.1021/nl302049k.

[11] T. Shimizu, T. Yokouchi, T. Shiraishi, T. Oikawa, P. S. R. R. Krishnan, and H. Funakubo, “Study on the effect of heat treatment conditions on metalorganic-chemical-vapor-deposited ferroelectric $\mathrm { H f } _ { 0 . 5 } \mathrm { Z r } _ { 0 . 5 } 0 _ { 2 }$ thin film on Ir electrode,” Jpn. J. Appl. Phys., vol. 53, no. 9S, p. 09PA04, 2014, doi: 10.7567/JJAP.53.09PA04.   
[12] M. H. Lee, S.-T. Fan, C.-H. Tang, P.-G. Chen, Y.-C. Chou, H.-H. Chen, J.-Y. Kuo, M.-J. Xie, S.-N. Liu, M.-H. Liao, C.-A. Jong, K.-S. Li, M.-C. Chen, and C. W. Liu, “Physical thickness 1.x nm ferroelectric HfZrOx negative capacitance FETs,” in IEDM Tech. Dig., Dec. 2016, pp. 1–12, doi: 10.1109/IEDM.2016.7838400.   
[13] J. Müller, E. Yurchuk, T. Schlösser, J. Paul, R. Hoffmann, S. Müller, D. Martin, S. Slesazeck, P. Polakowski, J. Sundqvist, M. Czernohorsky, K. Seidel, P. Kücher, R. Boschke, M. Trentzsch, K. Gebauer, U. Schröder, and T. Mikolajick, “Ferroelectricity in HfO2 enables nonvolatile data storage in 28 nm HKMG,” in Proc. Symp. VLSI Technol. (VLSIT), 2012, pp. 25–26, doi: 10.1109/VLSIT.2012.6242443.   
[14] S. George, K. Ma, A. Aziz, X. Li, A. Khan, S. Salahuddin, M.-F. Chang, S. Datta, J. Sampson, S. Gupta, and V. Narayanan, “Nonvolatile memory design based on ferroelectric FETs,” in Proc. 53rd Annu. Design Autom. Conf., 2016, pp. 1–6, doi: 10.1145/2897937.2898050.   
[15] X. Zhang, M. Takahashi, K. Takeuchi, and S. Sakai, “64 kbit ferroelectric-gate-transistor-integrated NAND flash memory with 7.5 v program and long data retention,” Jpn. J. Appl. Phys., vol. 51, no. 4S, p. 04DD01, 2012, doi: 10.1143/JJAP.51.04DD01.   
[16] A. Sharma and K. Roy, “Design space exploration of hysteresisfree HfZrOx -based negative capacitance FETs,” IEEE Electron Device Lett., vol. 38, no. 8, pp. 1165–1167, Aug. 2017, doi: 10.1109/LED. 2017.2714659.   
[17] J. E. Fonseca, T. Kubis, M. Povolotskyi, B. Novakovic, A. Ajoy, G. Hegde, H. Ilatikhameneh, Z. Jiang, P. Sengupta, Y. Tan, and G. Klimeck, “Efficient and realistic device modeling from atomic detail to the nanoscale,” J. Comput. Electron., vol. 12, no. 4, pp. 592–600, 2013, doi: 10.1007/s10825-013-0509-0.   
[18] A. S. Starkov and I. Starkov, “Asymptotic description of the time and temperature hysteresis in the framework of Landau–Khalatnikov equation,” Ferroelectrics, vol. 461, no. 1, pp. 50–60, 2014, doi: 10.1080/ 00150193.2014.889544.   
[19] C.-I. Lin, A. I. Khan, S. Salahuddin, and C. Hu, “Effects of the variation of ferroelectric properties on negative capacitance FET characteristics,” IEEE Trans. Electron Devices, vol. 63, no. 5, pp. 2197–2199, May 2016, doi: 10.1109/TED.2016.2514783.