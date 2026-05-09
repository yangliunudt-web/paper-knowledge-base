---
title: "Proposal of P-Channel FE NAND with High Drain Current and Feasible Disturbance"
authors:
  - "Bong Ho"
  - "Junpyo"
date: "2023-01-01"
year: 2023
journal: "IEEE International Electron Devices Meeting (IEDM)"
abstract: "Recently the demand for higher drain current and scalable gate stack thickness"
abstract_cn: "最近，由于单元物理极限和超过1000层的堆叠层数，下一代3D NAND闪存对更高漏极电流和可扩展栅极堆叠厚度的需求日益增长。虽然N沟道铁电场效应晶体管已被研究以克服这一限制，但由于编程和读取过程中寄生电子俘获带来的关键可靠性问题，会降低保持性能、耐久性并引起干扰和单元失效。我们展示了2位多级单元p沟道铁电场效应晶体管用于（嵌入式）NAND闪存应用的可行性。p沟道铁电场效应晶体管本质上比n沟道铁电场效应晶体管具有更高的导通电流。这是由于空穴俘获的缺失，导致沟道处铁电电荷增强。其他特性（保持性能、干扰等）也表明，当针对NAND闪存时，p沟道铁电场效应晶体管具有显著改善的电学特性，而不是n沟道铁电场效应晶体管。最后，我们提出了p沟道铁电NAND器件的工程策略。"
keywords:
  - "[[—Ferroelectric NAND flash]]"
  - "[[p-channel FEFET]]"
  - "[[charge trapping]]"
  - "[[reliability]]"
cite: "[1] Kuk S H, Han J H, Kim B H, et al. Proposal of p‑channel FE NAND with high"
aiSum: "p沟道FeFET NAND提案：利用无空穴俘获特性实现高漏极电流和铁电电荷增强，相比n‑FeFET具有更高导通电流、更佳保持与干扰特性，适用于下一代3D"
confidence: "high"
---

# Proposal of P-Channel FE NAND with High Drain Current and Feasible Disturbance for Next Generation 3D NAND

Song-Hyeon Kuk1, Jae-Hoon Han2, Bong Ho Kim1, Junpyo Kim1, and Sang-Hyeon Kim1*

1Department of Electrical Engineering, Korea Advanced Institute of Science and Technology, 34141 Daejeon, Republic of Korea. 2Center for Opto-electronic Materials and Devices, Korea Institute of Science and Technology, 02792 Seoul, Republic of Korea

*e-mail: shkim.ee@kaist.ac.kr

Abstract— Recently the demand for higher drain current and scalable gate stack thickness arises for next-generation 3D NAND flash, due to the physical limit of cells and stacked layers over 1,000. While the N-channel ferroelectric field-effect-transistor (n-FEFET) has been studied to overcome the limit, it brings the critical [[reliability]] issue due to parasitic electron trapping during the program and read, which degrades retention, endurance and induces disturbance and cell failure. We show the feasibility of 2- bit multi-level-cell (MLC) [[p-channel FEFET]] (p-FEFET) for (embedded) NAND flash memory application. P-FEFET intrinsically has higher on-current than n-FEFET. It is due to the absence of hole trapping, which leads to ferroelectric charge boosting at the channel. Other properties (retention, disturbance, etc) also show that p-FEFET has remarkably improved electrical characteristics when it is targeted for NAND flash, rather than n-FEFET. Finally, we propose a strategy for engineering the p-FENAND device.

Keywords[[—Ferroelectric NAND flash]], [[p-channel FEFET]], [[charge trapping]], [[reliability]].

# I. INTRODUCTION

The paradigm shift from 2D to 3D NAND flash with CTF devices has led to high-density low-cost non-volatile memory in last decade. The strategy of 3D NAND is to keep word line (WL) stacking [1]. Until now it has worked well with tremendous engineering and optimization such as channel hole etch, ONO (oxide-nitride-oxide) stack engineering, and peri-under-cell (or cell-on-peri). However, realizing 1000-layered NAND would be more challenging—a thousand layers will increase the length of the string, resulting in a low drain current [1]. This imposes that further scaling of the unit cell is required to guarantee a certain drain current. Nonetheless, the physical limit of scaling almost reached, considering cell-to-cell interference and thicknesses of ONO layers and spacer oxide. This arises a demand for a new paradigm of 3D NAND flash for the future generation.

Metal-ferroelectric-insulator-semiconductor (MFIS) FEFET has been broadly studied for memory-targeted applications due to its highly-scalable property, fast write speed, and 10-year retention [2]. Most importantly, the HfO2-based FEFET fabrication process is CMOS-compatible and highly-scalable, which is beneficial compared to other non-volatile memories. This potentially reduces the cost per a bit and manufacturing time, in the industry.

Most studies have focused on n-FEFET and demonstrated various systems such as compute-in-memory and NAND flash [3, 4]. However, at the same time, many studies have shown that n-FEFET intrinsically has severe electron trapping during the program operation because of the ferroelectric-insulatorsemiconductor interface nature [5, 6]. Unstable electron trapping/de-trapping dynamics makes fast read challenging, and the write endurance is limited by screening trapped electron [7, 8]. Especially for NAND flash application, parasitic electron trapping leads to significant disturbance in unselected cells,

which hinders the successful operation of n-FEFET for NAND flash [9, 10]. Hence, suprressing electron trapping by interface engineering or using materials having a higher coercive field (Ec) has been suggested [11, 12].

On the other hand, the absence of hole trapping in p-FEFET has been recently reported [13]. Stable retention and high ION and ION/IOFF in p-FEFET were attributed to suppressed hole trapping, which might be attributed to the heavy effective mass of the hole. However, the feasibility of p-FEFET for NAND flash devices has not been yet studied. This is most likely due to the negative prejudices toward the hole channel: (1) generally, the hole has lower mobility than an electron; (2) the hole might induce negative-bias-temperature-instability (NBTI); (3) pchannel poly-Si in NAND flash might have instability and [[reliability]] issue.

We investigate the properties of 2-bit MLC p-FEFET and show that p-FEFET is rather more appropriate (than n-FEFET) for the flash device. We show: (1) p-FEFET has higher $I _ { \mathrm { O N } }$ and lower subthreshold swing (SS) than n-FEFET; (2) it has extremely stable MLC retention from 100 μs to 10 years; (3) negligible read and write disturb until 106 cycles; (4) 5×104 program and erase cycles at 25°C; (5) negligible negative-biastemperature-instability (NBTI) and rather critical electrontrapping-induced instability (that is, positive-bias-temperatureinstability) at 85°C.

By studying the above properties, we propose [[p-channel FEFET]] NAND flash (p-FENAND) for a new paradigm of 3D NAND flash. P-FENAND would provide the possibility of further oxide and cell scaling, increased drain current, and overcoming the drawbacks of n-FEFET. We also suggest a strategy for p-FENAND engineering and optimization.

# II. SUPERIORITY OF P-FEFET OVER N-FEFET AND CTF

For fabricating n- and p-FEFET, HfZrOx 10×14 cycles (nanolaminate, ZH…ZH) was deposited by atomic layer deposition (ALD) on the bulk silicon wafer. A Tungsten gate was used, and post-metallization annealing was carried out at a relatively low temperature of 400°C, to reduce the interface $\mathrm { ( H f Z r O _ { x } { \mathrm { - } } S i O _ { x } ) }$ trap [14]. Devices with W/L = 28/5 μm were examined in this paper.

Fig. 1 describes the structures of [[charge trapping]] flash (CTF) and the proposed p-channel FE device. Table. 1 summarizes the advantages of the p-FENAND device. Taking the advantage of CMOS compatibility of HfZrOx, p-FENAND flash does not need an additional process or additional photomask compared to n-FEFET and CTF devices. Critical figure-of-merits for over-1000-layered NAND such as scalability, write speed, and oncurrent $( I _ { \mathrm { o n } } )$ could be mitigated by adopting p-FENAND. Especially $I _ { \mathrm { o n } } ,$ it must be significantly enhanced from that of CTF devices, although this paper does not show the results of CTF devices. It is because the equivalent oxide thickness (EOT) of FEFET is lower than that of CTF. Typically EOT in MFIS

![](images/730823f8769c1bcc4a16513e5dca7311b3843bf7096a867bf5a3d97643a99189.jpg)  
Fig. 1. A schematic of stacked 3D NAND CTF device and proposed p-channel ferroelectric NAND flash.

TABLE I. ADVANTAGES OF P-FEFET FOR (EMBEDDED) 3D NAND FLASH APPLICATION.   

<table><tr><td>Requirements</td><td>CTF (NMOS)</td><td>n-FEFET NAND</td><td>p-FENAND (This work)</td></tr><tr><td>Scalability</td><td>-</td><td>High</td><td>High</td></tr><tr><td>Read-after-write delay</td><td>&gt;0.1 s</td><td>&gt;0.1 s</td><td>&lt;40 ns</td></tr><tr><td rowspan="2">Cell write speed</td><td>tPRG ~ 100 μs</td><td>tPRG &lt; 1 μs</td><td>tPRG &lt; 20 μs</td></tr><tr><td>tERS ~ 1 ms</td><td>tERS &lt; 1 μs</td><td>tERS &gt; 100 μs</td></tr><tr><td>Retention</td><td>10 years</td><td>10 years</td><td>10 years</td></tr><tr><td>Endurance</td><td>~ 103</td><td>~ 104[15]</td><td>4×104</td></tr><tr><td>Write/Read Disturb</td><td>-</td><td>Bad (parasitic [[charge trapping]])</td><td>Good (Absence of parasitic hole trapping)</td></tr><tr><td>Erase mode (related to SS)</td><td>Hole injection</td><td>Hole injection</td><td>Electron injection</td></tr><tr><td>Subthreshold Swing</td><td>Bad</td><td>Bad</td><td>Good (by FE charge boosting)</td></tr><tr><td>Drain Current</td><td>Low</td><td>Low</td><td>High (Ns &gt; 2×1013cm-2by FE charge boosting)</td></tr><tr><td>Temperature Instability</td><td>Good</td><td>Bad</td><td>Feasible</td></tr></table>

![](images/cd651e1ed7d6160d7fdfaae84c02c19fcdcb5a1a0439d2f433e2997ffc77480a.jpg)  
Fig. 2. (a) DC $I _ { \mathrm { D } } { \cdot } V _ { \mathrm { G } }$ of our n- and p-FEFET, showing higher $I _ { \mathrm { o n } }$ in pFEFET due to less-hole-trapping-induced FE charge boosting. (b) $\mathrm { \hat { \vert } { \cal V } _ { G } } – { \cal V } _ { \mathrm { t h } }$ versus $I _ { \mathrm { D } }$ after program. (c) ID versus SS, showing lower SS in pFEFET.

(HfZrOx 14 nm / SiOx 1 nm) would be $< 3$ nm, while EOT in CTF (TANOS, Al2O3 5 nm / Si3N4 4 nm $/ \mathrm { S i O } _ { 2 } .$ 4 nm) is approximately 8.2 nm. The only disadvantage of p-FENAND in this work is low write endurance, but it was already comparable to

![](images/ff439a3f55b9463bd7c350d08b63dba4026162ec76fc5059f734f0c5a06edeb2.jpg)  
Fig. 3. Schematic of high ID and stable data retention in p-FEFET. The absence of screening holes could result in very high Ns $( { > } 2 { \times } 1 0 ^ { 1 3 } \thinspace \mathrm { c m } ^ { - 2 } ) .$ Thus, higher ID and lower SS can be easily achieved with holes. This might be helpful for 3D NAND flash stacks suffering from low drain currents.

the CTF device and would be able to be enhanced by further device optimization and engineering.

Fig. 2(a) experimentally shows transfer characteristics of nand p-FEFET. P-FEFET clearly shows a much higher drain current (ID) than n-FEFET. $I _ { \mathrm { D } }$ considering threshold voltage $( V _ { \mathrm { t h } } )$ at backward sweeps (namely, after programming the cell) are compared in Fig. 2(b), showing 2.5× higher $I _ { \mathrm { D } }$ in p-FEFET than in n-FEFET. This ID must be higher than that of CTF considering EOT as mentioned above. Furthermore, enhanced SS is also achieved in p-FEFET. Fig. 2(c) shows extracted SS from Fig. 2(b). The improved SS is most likely due to the less (or absent) hole trapping in the MFIS stack.

Fig. 3 describes the mechanism of higher $I _ { \mathrm { O N } }$ in p-FEFET. Surprisingly, p-FEFET shows higher $I _ { \mathrm { O N } }$ although typically electron has much higher effective mobility than the hole in Si. According to a previous study, the reason for this uncommon phenomenon is the unexpectedly high sheet carrier density [16]. Typically, a CMOS device has a saturated sheet charge density of approximately $1 0 ^ { 1 3 } \mathrm { c m } ^ { - 2 }$ . However, the ferroelectric-boosted sheet density of the inversion hole has been reported a $\mathbf { s } > 2 \times 1 0 ^ { 1 3 }$ $\mathrm { c m } ^ { - 2 }$ by Hall measurement [16]. This indicates that most of the channel holes are induced by ferroelectric polarity than by applied gate voltage. This would mitigate the challenge of the driving current for the next-generation 3D NAND flash.

From Fig. 4, the properties of 2-bit MLC p-FEFET are investigated. Fig. 4(a) shows program time and biases with $V _ { \mathrm { t h } }$ shifts. While ferroelectric switching below 800 ps has been reported [17], our devices have limited speeds due to their large size (long channel) and measurement equipment limits. In this study, triangular $2 0 \mu \mathrm { s }$ pulses were adopted. Fig. 4(b) shows erase time and biases with $V _ { \mathrm { t h } }$ shifts. Erase is slower than the program, which might be owing to electron-trapping-limited ferroelectric switching [18]. This is a critical disadvantage if the device is targeted for dynamic random-access-memory (DRAM) cells. On the other hand, the basic unit of erase in NAND flash is a block (not a page), and typically erase takes a few milliseconds in NAND flash. Hence, the slow speed is thought to be tolerated if p-FEFET is adopted to NAND flash memory.

Fig. 5(a) shows p-FEFET data retention of 2-bit states from 100 μs to $\mathrm { \dot { 1 } 0 ^ { 5 } s }$ . We note that it shows extremely stable retention from a very short time to $1 0 ^ { 5 } \mathrm { s } .$ 10-year 2-bit MLC retention is

![](images/1c75c5a02c615b3a5d1d5b78105202896b5aa630a092f60b1c8e356a148ff8be.jpg)  
Fig. 4. (a) Program and (b) erase at different triangular pulse times and biases of MLC p-FEFET. Erase requires a longer pulse time, but it is satisfying for NAND flash because the basic unit of erase is a block, not a page.

![](images/8bd8785e4811fbf4dc9ffc7feb49c314fe7b56b7f622aa54c9fa93dc76549098.jpg)

![](images/d67da86f10ff78d47f90d1ac91bdbc4978b2f29f628621f7c7b1f9b0c15487b6.jpg)  
Fig. 5. (a) p-FEFET 2-bit $V _ { \mathrm { t h } }$ retention, projected to 10 years and (b) Iread at $V _ { \mathrm { G } } =$ $- \mathrm { 1 . 2 V }$ and $V _ { \mathrm { D S } } = - 0 . 5 \ : \mathrm { V }$ in p-FEFET (at 25°C). (c) n-FEFET 2-bit $V _ { \parallel }$ retention and (d) Iread at $V _ { \mathrm { G } } = 1 . 3$ V and $V _ { \mathrm { D S } } = 0 . { \dot { 5 } } ^ { \cdot }$ V in n-FEFET (at 25°C). In n-FEFET, erase was carried out by −3.3 V / 20 μs triangle pulses.

projected. Fig. 5(b) shows read current when the read bias is fixed as $V _ { \mathrm { G } } = - 1 . 2 \ : \mathrm { V } .$ . 10-year retention is projected as well. Fig. 5(c) shows data retention of 2-bit n-FEFET from 100 μs to $1 0 ^ { 5 }$ s. Compared to p-FEFET, it has much more unstable charge dynamics due to unstable electron trapping/de-trapping which is induced by ferroelectric current displacement and depolarization field. While a larger MW was observed in p-FEFET, it is not commented here because n-FEFET also can achieve higher MW by further engineering as our previous study and other papers [19, 20].

More importantly, Figs. 5(b) and 5(d) show that the read current $\left( I _ { \mathrm { r e a d } } \right)$ in p-FEFET is 4 times higher than $I _ { \mathrm { r e a d } }$ in nFEFET. The device metrics and $V _ { \mathrm { D S } }$ are equal but p-FEFET has about 4 times higher $I _ { \mathrm { r e a d } }$ than n-FEFET. Wider $I _ { \mathrm { r e a d } }$ range guarantees not only a higher number of stacked cells but also a larger device variation gap margin in p-FEFET than n-FEFET when it is adopted to NAND flash memory. Moreover, a wider $I _ { \mathrm { r e a d } }$ range shows that triple-level-cell (TLC) and quad-level-cell (QLC) would be more feasible in p-FEFET than in n-FEFET.

In summary, p-FEFET takes the advantage of high ${ \cal I } _ { \mathrm { D } } ,$ a desirable property for next-generation 3D NAND flash over

![](images/cfd3533fbb9c31b08703ceec3f3e462a21ef68421e5446a7e9a37a560943f8e2.jpg)  
Fig. 6. (a) Proposed scheme of program operation and (b) read operation in a unit NAND flash block of MLC p-FEFET. Vinhibit and $V _ { \mathrm { p a s s } }$ was defined as $- 2 . 5 \mathrm { V }$ and $- 1 . 5 \mathrm { ~ V } .$ Program and erase triangular pulses were adopted from Fig. 4(a) and 4(b).

![](images/f8a3fb7fded0e71bb2f0d877be143e9d4926a6f1e91e2c173a6bd5a8cdbaf350.jpg)

![](images/abf44229faf5ebb8d8254a923c9428a2e3f2eaf8557ffc0c12d1a2165a4e41b0.jpg)

![](images/5620ab5f8c7d7beb2beece473318a3e49c1ff49c767530b1da4bb51c6cacfc00.jpg)  
Fig. 7. (a) Disturbance test in p-FEFET from Fig. 6. Program, pass, and read disturbs were examined. (00) cell equals −3.5V-programmed cell, and (11) cell is the erased cell. (b) Disturbance test in n-FEFET. (00) cell is equivalent to a 3.9 V-programmed cell, and (11) cell is the erased cell.

![](images/395a2175d399cdf79056cfa664f35cdd52960362c1c866b637c7b1032ea7f5cd.jpg)

![](images/52d6bade577875a292123bc58be32271c86e7693985999872aab299045730351.jpg)  
Fig. 8. (a) Cycling test of 2-bit MLC p-FEFET at 25°C. (b) Cycling test of p-FEFET at 85°C to investigate the impact of hole-induced defect generation, namely, negative-bias-temperature-instability (NBTI). (c) Cycling test of n-FEFET at $8 5 ^ { \circ } \mathrm { C }$ to compare with (b).

1,000-stacked layers. The extremely stable 2-bit data retention also shows that p-FEFET has more advantages for NAND flash memory.

# III. DISTURBANCE AND ENDURANCE

As mentioned above, [[reliability]] issue, especially disturbance, occurs due to parasitic electron trapping in n-

FEFET. Thus, the disturbance is tested in the p-FEFET array scheme as Fig. 6(a) and 6(b). Proper biases for program-inhibit voltage $( V _ { \mathrm { i n h i b i t } } )$ and pass voltage $\hat { ( }  { V _ { \mathrm { p a s s } } } )$ were adopted. Fig. 6(a) shows program/pass disturbance in unselected cells during the program, and Fig. 6(b) shows read/pass disturbance in unselected cells. Fig. 7(a) shows the disturbance test of erased (11) cells and −3.5V-programmed (00) cells in p-FEFET. The harshest bias conditions (for pass disturbance, $- 1 . 5 \mathrm { V } / 2 0 \mu \mathrm { s } .$ , and for program disturbance, −3.5V/20 μs with $V _ { \mathrm { i n h i b i t } } )$ were adopted. (00) and (11) cells are most vulnerable to disturbance because (11) cells are not programmed and (00) cells have high remnant polarization $( P _ { \mathrm { r } } )$ in the ferroelectric layer, which is most likely to cause parasitic carrier trapping.

In Fig. $^ { 7 ( \mathrm { a ) , } }$ , (00) cells show no disturbance at all, but (11) cells show $V _ { \mathrm { t h } }$ shifts from $1 0 ^ { 4 }$ cycles. However, only 0.1 V was shifted by $1 0 ^ { 6 }$ cycles, which did not reach failure. On the other hand, in Fig. 7(b), (00) cell reached failure at 106 cycles because its $V _ { \mathrm { t h } }$ overlaps (01) cell (3.6V-programmed cell). Compared to n-FEFET (Fig. 7(b)), p-FEFET shows the feasible disturbance characteristics to NAND flash. The negligible disturbance in p-FEFET is remarkably promising, compared to previous papers on n-FEFET as well [9].

The endurance test of p-FEFET was carried out as Fig. 8(a) at $2 5 ^ { \circ } \mathrm { C } .$ . Failure of 2-bit operation was observed after $5 { \times } 1 0 ^ { 4 }$ cycles of the program (−3.5 V/20 μs) and erase (4 V/500 μs) pulses. Especially, programmed cells are vulnerable, which must be attributed to the gradual increase of hole trapping, like negative-bias-temperature-instability (NBTI) in p-MOSFET.

Hence, we also tested endurance at $8 5 ^ { \circ } \mathrm { C }$ as Fig. 8(b). However, rather erased cells became more vulnerable, contrary to at 25°C [7]. This is most likely due to the slow erase speed compared to the program speed. Namely, repeated 500μstriangular-pulses at $8 5 ^ { \circ } \mathrm { C }$ might more degrade the interface. To further investigate the phenomenon, we also examined n-FEFET at 85°C (Fig. 8(c)). The program/erase in n-FEFET was carried out by $3 . 9 \mathrm { ~ V ~ } / 2 0$ μs and −3.3 V / 20 μs. The program and erase times were the same, and Fig. 8(c) shows that the programmed cell has more $V _ { \mathrm { t h } }$ shifts, which is likely to be originated from electron trapping. This indicates that electron trapping is rather more critical to [[reliability]] than hole trapping in the FEFET structure, contrary to conventional MOSFET. Another study also shows that NBTI in p-FEFET is suppressed compared to conventional p-MOSFET [21]. Therefore, p-FEFET has the potential for high [[reliability]].

Finally, we propose a strategy for higher memory window (MW), higher endurance, and realizing triple-level-cell (TLC) p-FENAND. The most key property is to design proper E-field in the MFIS stack. Low-temperature annealing and excellent ALD recipe are critical for reducing hole/electron trap and for E-field optimization, and further engineering of IL and device structure would increase MW. Adopting high Ec $( \mathrm { o r } > 5 $ nm HfZrOx) and high $P _ { \mathrm { ~ r ~ } }$ FE material, interface engineering (e.g. high-k material such as SiON), and optimizing channel doping concentration and thicknesses of IL/FE will be required [11].

# IV. CONCLUSION

In conclusion, we propose the concept of p-FEFET (p-FENAND) for next-generation 3D NAND flash. High scalability, high drain current and stable retention are the key advantages of p-FENAND for the next-generation 3D NAND flash. Wider range of read current in p-FEFET would increase bit-per-cell. Feasible disturbance, endurance and temperature instability with 2-bit MLC operation were studied as well. We use 14 nm-HZO here, but the thickness would be shrinked for the scalability. P-FENAND might be the key enabler for 3D NAND of the future generation.

# ACKNOWLEDGMENT

This work was supported by NRF of Korea grant (No. 2020M3F3A2A01110575, 2022R1C1C1007333, RS-2023- 00215860), BrainKore-a21 FOUR, KAIST (N11220038), IDEC, and KIST Institutional Program (2E32242).

# REFERENCES

[1] A. Goda, IEEE Transactions on Electron Devices, vol. 67, no. 4, pp. 1373 1381, 2020.   
[2] A. I. Khan, A. Keshavarzi, and S. Datta, Nature Electronics, vol. 3, no. 10, pp. 588-597, 2020.   
[3] S. Yoon et al., 2022 IEEE International Memory Workshop (IMW), 2022: IEEE, pp. 1-4.   
[4] S. Dutta et al., 2020 IEEE International Electron Devices Meeting (IEDM), 2020: IEEE, pp. 36.4. 1-36.4. 4.   
[5] S.-H. Kuk, S.-M. Han, B. H. Kim, S.-H. Baek, J.-H. Han, and S.-H. Kim, IEEE Transactions on Electron Devices, 2022.   
[6] R. Ichihara et al., 2021 IEEE International Electron Devices Meeting (IEDM), 2021: IEEE, pp. 6.3. 1-6.3. 4.   
[7] M. Hoffmann et al., IEEE Electron Device Letters, vol. 43, no. 5, pp. 717- 720, 2022.   
[8] A. J. Tan et al., IEEE Electron Device Letters, vol. 42, no. 7, pp. 994-997, 2021.   
[9] K. Ni, X. Li, J. A. Smith, M. Jerry, and S. Datta, IEEE Electron Device Letters, vol. 39, no. 11, pp. 1656-1659, 2018.   
[10] M. M. Dahan, E. T. Breyer, S. Slesazeck, T. Mikolajick, and S. Kvatinsky, IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 69, no. 4, pp. 1595-1605, 2022.   
[11] M. Pešić et al., 2022 IEEE International Memory Workshop (IMW), 2022: IEEE, pp. 1-4.   
[12] B. H. Kim et al., Nanoscale Advances, vol. 4, no. 19, pp. 4114-4121, 2022.   
[13] D. Kleimaier et al., IEEE Electron Device Letters, vol. 42, no. 12, pp. 1774-1777, 2021.   
[14] K. Toprasertpong et al., IEEE Electron Device Letters, vol. 41, no. 10, pp. 1588-1591, 2020.   
[15] K. Florent et al., 2018 IEEE International Electron Devices Meeting (IEDM), 2018: IEEE, pp. 2.5. 1-2.5. 4.   
[16] K. Toprasertpong, Z. Lin, T. Lee, M. Takenaka, and S. Takagi, in 2020 IEEE Symposium on VLSI Technology, 2020: IEEE, pp. 1-2.   
[17] H. Bae et al., 2020 IEEE International Electron Devices Meeting (IEDM), 2020: IEEE, pp. 31.3. 1-31.3. 4.   
[18] S.-H. Kuk, S.-M. Han, B.-H. Kim, S.-H. Baek, J.-H. Han, and S.-h. Kim, 2021 IEEE International Electron Devices Meeting (IEDM), 2021: IEEE, pp. 33.6. 1-33.6. 4.   
[19] S.-H. Kuk et al., IEEE Electron Device Letters, vol. 44, no. 1, pp. 36-39, 2022.   
[20] H.-K. Peng, C.-Y. Chan, K.-Y. Chen, and Y.-H. Wu, Applied Physics Letters, vol. 118, no. 10, p. 103503, 2021.   
[21] L. Zhou et al., 2020 IEEE International [[reliability]] Physics Symposium (IRPS), 2020: IEEE, pp. 1-6.