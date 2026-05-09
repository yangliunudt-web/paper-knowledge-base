---
title: "Application and Benefits of Target Programming Algorithms for Ferroelectric HfO₂ Transistors"
authors:
  - "H. Zhou"
  - "J. Ocker"
  - "A. Padovani"
  - "M. Pesic"
  - "M. Trentzsch"
  - "S. Dünkel"
  - "H. Mulaosmanovic"
  - "S. Slesazeck"
  - "Luca Larcher"
  - "S. Beyer"
  - "S. Müller"
  - "T. Mikolajick"
date: "2023-01-01"
year: "2023"
journal: "IEEE Transactions on Electron Devices"
doi: "10.1109/TED.2023.xxxxxxx"
abstract: "The ferroelectric HfO2 based field effect transistor (FeFET) has been under research for many years and shows unique properties for applications in the field of emerging memories and in-memory computing. This work for the first time demonstrates how a target programming algorithm can improve the FeFET device characteristics with respect to endurance performance and variability for small device geometries. With this technique the threshold voltage Vt of the memory cell can be targeted to any desired value, which is essential for multilevel cells and analog in-memory computing as used in AI accelerators. The switching, trapping and detrapping characteristics of the cell and their influence on the target programming algorithm are presented. The trapping and leakage characteristics are modelled using the GinestraTM simulation software to extract the trap distribution in ferroelectric HfO2. Finally, a model for the underlying mechanism of the endurance degradation is proposed."
abstract_cn: "铁电HfO2基场效应晶体管（FeFET）经过多年研究，在新兴存储器和存内计算领域展现出独特性能。本文首次展示了目标编程算法如何改善FeFET器件在小尺寸几何结构下的耐久性性能和variability。通过该技术，存储单元的阈值电压Vt可被编程到任意目标值，这对多级单元和AI加速器中的模拟存内计算至关重要。介绍了单元的切换、俘获和去俘获特性及其对目标编程算法的影响，使用GinestraTM仿真软件对HfO2中的陷阱分布进行了建模，最后提出了耐久性退化的底层机理模型。"
  - "[[FeFET]]"
  - "[[Target programming]]"
  - "[[Endurance]]"
  - "[[Multi-level cell]]"
  - "[[HfO2]]"
  - "[[铁电晶体管]]"
keywords:
  - "[[FeFET]]"
  - "[[Target programming]]"
  - "[[Endurance]]"
  - "[[Variability]]"
  - "[[HfO₂]]"
cite: "[1] Zhou et al. Application and Benefits of Target Programming Algorithms for Ferroelectric HfO₂ Transistors[J]. IEEE Transactions on Electron Devices, 2023."
aiSum: "目标编程算法改善 FeFET 耐久性能和变异特性：可将阈值电压设定为任意值，适用于多级单元和模拟存内计算，通过 GinestraTM 仿真提取 HfO₂ 陷阱分布并提出退化机制模型。"
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
  - "[[HfO2]]"
---

# Application and Benefits of Target Programming Algorithms for Ferroelectric HfO₂ Transistors

H. Zhou1, J. Ocker1, A. Padovani2, M. Pesic2, M. Trentzsch3, S. Dünkel3, H. Mulaosmanovic4, S. Slesazeck4, Luca Larcher2, S. Beyer3, S. Müller1 and T. Mikolajick4,5

1Ferroelectric Memory GmbH, Dresden Germany, email: haidi.zhou@ferroelectric-memory.com

2Applied Materials, Inc, Santa Clara, CA, USA

3GLOBALFOUNDRIES Dresden Module One LLC & Co. KG, Dresden Germany

4NaMLab gGmbH, Dresden, Germany 5Institute of Semiconductors and Microsystems, TU Dresden, Dresden Germany

Abstract—The ferroelectric HfO2 based field effect transistor (FeFET) has been under research for many years and shows unique properties for applications in the field of emerging memories and in-memory computing. This work for the first time demonstrates how a target programming algorithm can improve the FeFET device characteristics with respect to endurance performance and variability for small device geometries. With this technique the threshold voltage Vt of the memory cell can be targeted to any desired value, which is essential for multilevel cells and analog in-memory computing as used in AI accelerators. The switching, trapping and detrapping characteristics of the cell and their influence on the target programming algorithm are presented. The trapping and leakage characteristics are modelled using the GinestraTM simulation software to extract the trap distribution in ferroelectric HfO2. Finally, a model for the underlying mechanism of the endurance degradation is proposed.

# I. INTRODUCTION

Ferroelectric HfO2 transistors have made huge improvements during the last years due to intensive research and development. However, some issues still need to be overcome, among them is the endurance degradation. Numerous research studies [1]–[5] have been published to explain the mechanism for this endurance degradation. The conclusion is that the degradation is mainly related to the deterioration of the gate stack rather than the fatigue of the ferroelectric layer. The degradation of the gate stack is attributed to charge trapping and trap generation which occurs during program and erase operation.

In this work a deeper analysis is performed on the trapping and switching characteristics by designing comprehensive tests, then model the device using the GinestraTM simulation platform [6] and fit the measured data. Upon understanding the potential trapping mechanism of the FeFET a target programming algorithm is applied to the ferroelectric HfO2 transistor, aiming at a better endurance performance and smaller device variability. Preliminary results about the improvement on the device variability with the target programming scheme can be found in a recently published study[7]. In addition, a previous study[8] has shown that the threshold voltage $V _ { t }$ of the FeFET can be set at any point between the low Vt (LVT) and the high Vt (HVT), by adjusting the program and erase conditions. With this target programming algorithm, we could change the FeFET

$V _ { t }$ to any desired value, which is extremely valuable for multilevel cells and analog in-memory computing applications.

# II. TRAPPING AND DETRAPPING CHARACTERISTICS

The FeFET device used in this paper is manufactured on a GLOBALFOUNDRIES 28 nm high-k metal gate (HKMG) super low power (SLP) technology platform with a 9 nm thick ferroelectric HfO2 (Fig. 1). Switching, trapping, detrapping, endurance, multilevel cell and variability experiments have been performed on single N-type FeFETs with either a gate length and width of 450 nm or 180 nm correspondingly. Gate leakage measurements have been performed on N-type FeFET multi- structures with a gate length and width of 2700 nm.

Fig. 2 shows the HVT and LVT short term retention directly after the write pulse which reveals the electron and hole detrapping behavior. The LVT electron detrapping requires 400 ms to settle whereas the HVT state can be read out directly after the write pulse. To apply a target programming scheme to such a cell in a real memory architecture one would have to wait 40- 400 ms for every programming cycle to fully detrap. Hence, the origin of the strong trapping behavior was investigated by means of trapping experiments and multiscale simulation with GinestraTM. Afterwards detrapping pulse schemes were investigated to increase the read speed.

Fig. 3 shows the trapping behavior measured directly at the falling edge of the LVT programming pulse in dependence of pulse amplitude and width. A maximum threshold voltage shift due to electron trapping of 4V can be noticed which is even higher than observed in the short-term retention measurements. To investigate the origin of this difference, the pure trapping response was measured by reading out the $V _ { t }$ after the pulse using a dedicated $V _ { t }$ sweep as shown in Fig. 4. The different $V _ { t }$ levels between single-pulse and dedicated $V _ { t }$ sweep reveals that there is an even faster detrapping process not captured by the short-term retention measurement. Subsequently, both trapping experiments and temperature-dependent gate leakage currents (Fig. 5) were fed into the Ginestra simulation tool to extract the trap distribution in the ferroelectric gate stack after setting the polarization state using Ginestras’ ferroelectric module (comprising multidomain time-dependent Ginzburg-Landau model) [9]. A reasonable trap density of 1020 cm-3, comparable with HfO2-based gate dielectrics was extracted and the trap parameters are shown in Table I. From the simulated band diagram and extracted defect map for +3V/10us in Fig. 5b) one

can conclude that charge is trapped not only in the $\mathrm { S i O } _ { 2 }$ and the $_ { \mathrm { S i O } _ { 2 } / \mathrm { F E - H f O } _ { 2 } }$ interface region, but also deep inside the bulk FE-HfO2.

To investigate the $V _ { t }$ shift without any wait time the readout sweep was performed directly after the write pulse with different amplitudes for both LVT and HVT programming (Fig. 6a) and the results are shown in Fig. 6b). The LVT programming without wait time keeps the $V _ { t }$ close to the HVT state and only a small dip to lower threshold voltages is found when polarization switching occurs at about 2.5V. On the other hand, the HVT programming shows for low amplitudes, where $V _ { t }$ is still in a LVT state, a detrapping behavior. Once the LVT detrapping reaches its lowest point the device starts to switch to HVT that can be read without the need for any additional delay time. To find the optimal LVT program and detrapping voltage a shmoo plot over both voltages for 10us pulse width was generated in Fig. 6d). As can be seen the best detrapping voltage of about -2.3V is almost independent of the LVT write voltage. In order to choose the optimal write voltage and detrapping voltage for every cell a target programming algorithm is developed as presented in the next chapter.

# III. TARGET PROGRAMMING ALGORITHM

As it is shown in section II, the FeFETs currently experience large amount of electron trapping. This trapping counteracts the polarization reversal and causes on the one hand a smaller memory window after switching, while on the other hand it accelerates the endurance degradation by inducing more traps in the gate stack. Thus, a target programming scheme is developed. The corresponding pulse train is shown in Fig. 7. For the target erase operation, a consecutive series of negative pulses with increasing amplitude is applied to the cell with a point read after every target HVT pulse (Fig. 7a) until the drain current reaches below a certain threshold value (in this case 1uA). In our test system this is accomplished by connecting the gate of the FeFET to ground utilizing a FPGA controlled multiplexer (Fig. 8). For the target program operation, a similar series of positive pulses with increasing amplitude is applied to the cell followed by a series of detrapping pulses with increasing amplitude, a point read is done after each detrapping pulse (Fig. 7b) until the drain current reaches above a certain threshold value (in this case 1uA). Although previous detrapping shmoo plot shows a steady best detrapping voltage independent of the LVT write voltage, there is cell to cell as well as cycle to cycle variations across the wafer in terms of optimal detrapping voltage as can be seen in Fig. 10e).

# A. Multi-Level-Cell capability

The pulse train for this test is shown in Fig. 9a). Initially the cell is set to the lowest $V _ { t }$ by applying a reference pulse, then 3 target erase pulses with increasing target $V _ { t }$ are applied to the cell, followed by an $\mathrm { I _ { D } \mathrm { - V _ { G } } }$ read after each operation. This procedure is repeated for 100 times to verify the cycle to cycle variation. In addition, 20 random dies are chosen across the wafer to capture the die to die variation. The ID-VGs and cumulative plots of the extracted $V _ { t }$ of 20 dies are illustrated in Fig. 9b) and Fig. 9c) respectively. Obviously, in this case a separation of four $V _ { t }$ states can be achieved.

# B. Improved endurance performance

Endurance pulse trains with standard +/-4V/10us condition and the target programming algorithm are depicted in Fig. 10a) and Fig. 10b). Corresponding results are shown in Fig. 10c) and Fig. 10d). It can be clearly seen that with standard condition both $V _ { t }$ states shift up dramatically, making a complex adaptive reference scheme necessary to read out the state, In contrast, by using the target programming algorithm we could achieve a flat endurance behavior up to 10k cycles. To further understand the cycle to cycle variation, all write voltages and detrapping voltages are plotted out in Fig. 10e). An increase of the required programming voltage can be seen with increasing cycle count. This compensates the upshift of the transistor $V _ { t }$ while at the same time the erase voltage and detrapping voltage show no obvious pattern.

# C. Lower device variablity

Fig. 11 shows the $V _ { t }$ variability for small devices (180 nm x 180 nm) for the standard and the target programming algorithm. From Fig. 11b) and Fig. 11e) it can be seen that with the target programming algorithm the $V _ { t }$ variation can be lowered. This leads to a $^ { 5 }$ orders of magnitude reduction of the extrapolated bit error rate (BER). The BER is calculated based on the standard deviation and median value of both $V _ { t }$ states, by assuming a Gaussian distribution. The improvements due to the target programming algorithm can also be seen when comparing the wafermaps of the memory window in Fig. 11c) and Fig. 11f).

# IV. CONCLUSION

This paper demonstrated the capability of enhancing the endurance performance and lowering variabilities for small device geometries by a target programming algorithm and also the possibility for Multi-Level-Cell operation, which is essential for building higher-density FeFET memories and analog in-memory computing tasks. A comprehensive study with test and simulation results regarding to the trapping, switching and detrapping is presented, thus, providing in depth insight into to the endurance degradation mechanism of our FeFET devices.

# ACKNOWLEDGMENT

This work has been supported by funding from the EC through H2020-NMBP-TO-IND project GA n. 814487 (INTERSECT).

# REFERENCES

[1] E. Yurchuk et al., IEEE Trans. Electron Devices, pp. 3501-3507, Sept. 2016.   
[2] N. Gong et al., IEEE Electron Device Lett., pp. 15-18, Jan. 2018.   
[3] M. Pešić et al., Adv. Funct. Mater., pp. 4601-4612, July 2016.   
[4] K. Ni et al., IEEE Trans. Electron Devices, pp. 2461-2469, 2018   
[5] E. Yurchuk et al., IEEE IRPS, pp. 2E.5.1-2E.5.5, 2014.   
[6] Applied Materials GinestraTM,   
http://www.appliedmaterials.com/products/applied-mdlx-ginestrasimulation-software.   
[7] H. Zhou et al., IMW, pp. 1-4, 2020.   
H. Mulaosmanovic et al., IEEE EDTM, pp. 1-4, 2020.   
[9] M. Pesic et al., IEEE IEDM, pp. 25.1.1-25.1.4, 2018.

![](images/37a1e249adb1f72900945eac4c6397b93eec0f3e9edd3a485fa7bc25085a4d0d.jpg)

![](images/abd0b7c44b39af98ca87c48de77dc01e01eec1b1963c34f3f761fa23c8ad7293.jpg)  
  
Fig. 1. The gate stack schematic of a FeFET device with the MFIS structure is depicted in a). Thickness of each layer is not to scale with respect to a real device. b) shows the TEM graph of the cross section of a FeFET device fabricated on a GLOBALFOUNDRIES 28 nm SLP technology platform, a longer channel version (450 nm) of this FeFET is utilized for obtaining the experimental results in this paper

# Short Term Retention

![](images/7fa9ce53a943305a30366353094bbdb174e1ec3a7cf8d7ce1fb7bdb8c850d6b3.jpg)  
a)

![](images/f1c5f2224053c26675f0fc8534be1eb1d779303047a902525a1f0483477c4bf4.jpg)  
b   
Fig. 2. Pulse train is shown in a), a reference pulse is always given before every write operation, after various delay time an $\mathrm { I _ { D } \mathrm { - } V _ { G } }$ read is performed and its results are illustrated in b).

# Trapping Characteristics

Table Ⅰ. Parameters for the modeling of the fast trapping test   

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td colspan="2">HfO2</td></tr><tr><td>Trap Density
NT(cm-3)</td><td>1x1020</td></tr><tr><td>Trap Energy
from Conduction Band
ET(eV)</td><td>1.5</td></tr><tr><td>Relaxation Energy
REL(eV)</td><td>1.8</td></tr><tr><td>Capture Cross Section
σT(cm2)</td><td>1x10-14</td></tr><tr><td colspan="2">SiO2</td></tr><tr><td>Trap Density
NT(cm-3)</td><td>2x1019</td></tr><tr><td>Trap Energy
from Conduction Band
ET(eV)</td><td>2.66</td></tr></table>

![](images/bea1c14298537cfbb93e53e68a2cf54489e67fdee364e49aec7db0340c40d7bf.jpg)  
a

![](images/e71a9275bb7e0bb935975cbb87776cf1637d8ab42c7921f08ad3684845499180.jpg)  
  
Fig. 3. Pulse train is depicted in a). The cell is set to the LVT state and waited 40 ms for detrapping before each fast trapping test with various pulse width and pulse amplitude. The threshold voltage is extracted on both the rising edge and the falling edge as indicated in yellow. Their difference $\Delta \mathrm { V } _ { \mathrm { t } }$ is illustrated in b). Circles are measured data while solid lines are simulation results.

![](images/cd69730308569b4f8f0ab247fd402976c6c8638a46067fe0f6bd714b98b5a22a.jpg)  
a)

![](images/07ae0e6d98dd4343972fa3b9877f1b98049f99318d481f41fba972ee502315d9.jpg)  
b)   
Fig. 4. Pulse train for the trapping test is shown in a).After switching the cell to LVT with 40 ms wait time another pulse in the same polarity with various amplitude is applied, subsequently the Vt read out is performed and the result is illustrated in b). Circles are measured data while solid lines are simulation results.

# Temperature-dependent Gate Leakage

![](images/5f9cb997de774ca7fe68349cbb82357dba980fce50fbc54026ede2308815b7bb.jpg)

![](images/6467267b1023f21e59ade86f1e271abf4417f59932957178235f03692e219026.jpg)  
Fig. 5. Temperature dependent gate leakage vs gate voltage results are illustrated in a). Circles are measured data while solid lines are simulation results. Trapped charges in the gate stack after a gate voltage pulse of 3V/10 us are simulated and depicted in the band diagram shown in b).

# Switching, Trapping and Detrapping Characteristics

![](images/e6a903bee00f23571c5d3685c0dd299b84659e3a493e590fd7ddfc1a7039a88f.jpg)  
a)

![](images/36cd80baf07ac125b1596e7abdde5d481c0757eea3a2534f3ee5698b3c59bb5f.jpg)  
b)

![](images/2a4886969541a008125f64ce917082c3618734e51303d75a408af1c8bf2d908c.jpg)  
c)

![](images/5a9658662369a292340f4bb178aa7b2f51a74cd3788a04a6c5384ef9ace39364.jpg)  
  
Fig. 6. The pulse trains for the trapping and switching and detrapping test are shown in a) and c). For a) an $\mathrm { I _ { D } { - } V _ { G } }$ read is performed directly after a LVT or a HVT programming pulse with various amplitude, while for c) a detrapping pulse with various amplitude directly after the program pulse is applied, thereafter an $\mathrm { I _ { D } { - } V _ { G } }$ read is performed, results are illustrated in b) and d). Red represents lower $V _ { t }$ value and blue represents higher Vt values in d) while blue stands for LVT to HVT switching and orange for HVT to LVT switching.

# Target Programming Algorithm Pulse Train

![](images/70a0e63f4624b77e460e3337d229dc785b40008862a8c9f4b1aa96e8d1b9e2d3.jpg)

![](images/a47061aafb1733ca71ad1cf58deb783ecfbffe996195a4b395301b839e6337a7.jpg)  
Fig. 7. Pulse trains for target erase operation and target program operation are depicted in a) and b) respectively. For target erase a series of negative pulses starting from small voltages to large voltages with small steps is applied and a point read at the target HVT value is performed after each pulse. For target program a series of similar pulses is applied, but in positive direction, after each program, a series of detrapping pulses with increasing amplitudes is applied and a point read at the target LVT value is performed after each detrapping pulse.

![](images/648f91d54748c7d8ea2c7231f68e742d380f46429df33ba176d68b00686d17da.jpg)  
PXI Setup   
Fig. 8. The block diagram for the test system setup. Using the FPGA, the output voltage to the gate is controlled, which is essential for the target programming algorithm.

![](images/81277f098a7750b748ea157e82ce7542735d5e44883b121f5efa8c923361b627.jpg)  
Multi-Level Cell

![](images/0080af214fc47ccef92cb943dabf99d91a8c5db8f9ffb3a42d9942624cefb5b2.jpg)

![](images/dfc6b2b07929859f2877efa021c65a5b591fe8c4d0f6e4d1793b8e4bedf4097f.jpg)  
Fig. 9. Pulse train for the Multi-Level-Cell application is depicted in a). First of all, the cell is set to the lowest Vt, then we use the target erase to bring the $V _ { t } \mathbf { s }$ to the other three higher values and repeat this procedure 100 times on the same cell. $\mathrm { I _ { D } \mathrm { - V _ { G } \mathrm { s } } }$ and cumulative plots of 20 dies across the wafer are shown in b) and c). For each state there are in total 2000 $\mathrm { \underline { { I _ { D } } } \mathrm { - V _ { G } } }$ readouts.

![](images/565dffcffa30ff1850e03ef2b9c0b128e44d1f81ed818a29d7b92c20aabe95de.jpg)  
Endurance Degradation

![](images/82f33837647cdfb220efd1688188bdaa3ca757399ffc791ef0d3ada8a57744ce.jpg)

![](images/d63110c6c2c73488b1b922c9bdee062de7616e2c9f52bde22bb76d0e63af9c62.jpg)

![](images/1cbf61895cc00cf8c882e4879de8a30fdfd15e8243d6e3452e6465e75ce316e9.jpg)

![](images/f30bef733d8cae1412a2e14727dff6e0d679e3054763718c04bda3fae0e3cbbc.jpg)  
Fig. 10. Pulse trains for the endurance test with +/-4V/10us and with the target programming algorithm are depicted in a) and b) correspondingly. The $\mathrm { I _ { D } { - } V _ { G } }$ plot in c) shows that both Vt upshifts by cycling under standard condition as the arrow shows while the $\mathrm { I _ { D } { - } } \bar { \mathrm { V _ { G } } }$ in d) shows a stable Vt behavior up to 10k cycles using the target programming algorithm. The gray line in both $\mathrm { I _ { D } \mathrm { - V _ { G } } }$ plots indicates the current criteria for Vt extraction. In addition, the cycle to cycle programming(red), erase(blue) and detrapping voltages(gray) are captured in e).

![](images/885f6716e9654b950738100766755399e991553d11ff2a3167437ae780b42e0d.jpg)  
Variability

![](images/940283478f90882ccd05adebe0cd03468116ba05fd85f5a24aa51c1ec07088cb.jpg)

![](images/c9c2d11a29d50ac87c7ff5d3d0dc1cf863ffb306a872f0754569dbff2fc76615.jpg)

![](images/843fb2bab334f2b52ca60dffc6bdf2a844d05d1eef7129b00de08a06234f7d70.jpg)

![](images/baef4069854b3745be8f5c4dba56b58f5ea18edb31635534bbc2ba303408f7f2.jpg)  
Fig. 11. Pulse trains for the device variability test under standard condition with +/-4V/10us and with the target programming algorithm are depicted in a) and d) correspondingly. 10 cycles with bipolar pulses are applied first, then the device is set to HVT and read out, followed by the opposite direction. The $\mathrm { I _ { D } { - } V _ { G } }$ reads of 64 dies across the wafer are illustrated in b) and e) correspondingly. Blue stands for HVT while red stands for LVT, the legend shows the memory window and extrapolated BER. c) and f) illustrates the memory window wafermap of 64 dies.