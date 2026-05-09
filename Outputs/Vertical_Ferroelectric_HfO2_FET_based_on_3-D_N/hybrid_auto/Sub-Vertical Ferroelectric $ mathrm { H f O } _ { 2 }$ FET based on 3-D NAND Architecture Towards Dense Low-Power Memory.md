---
title: "Vertical Ferroelectric HfO2 FET based on 3-D NAND Architecture Towards Dense and\"
authors:
  - "K. Florent"
  - "M. Pesic"
  - "A. Subirats"
  - "K. Banerjee"
  - "S. Lavizzari"
  - "A. Arreghini"
  - "L. D. Piazza"
  - "M. C. C. J. M. Toledano"
  - "J. L. M. R. G. C. S. R. Y. Deng"
date: "2024-01-01"
year: "2024"
journal: "IEEE Transactions on Electron Devices"
abstract: "A vertical ferroelectric HfO2 field effect transistor based on 3-D macaroni NAND\"
abstract_cn: "本文展示了基于3-D NAND架构的垂直铁电HfO₂ FET，通过在位工艺实现高密度低功耗非易失性存储。器件展现出良好的存储窗口、耐久性和保持特性，为3-D堆叠存储应用提供了可行的器件方案。"
keywords:
  - "[[FeFET]]"
  - "[[HfO2]]"
  - "[[3-D NAND]]"
  - "[[Non-volatile memory]]"
  - "[[Vertical transistor]]"
cite: "Florent K, Pesic M, Subirats A, et al. Vertical ferroelectric HfO2 FET based on\"
aiSum: "垂直HfO₂ FET 3-D NAND架构：高密度低功耗非易失存储，良好存储窗口和可靠性。"
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
  - "[[HfO2]]"
---

# Vertical Ferroelectric $\mathrm { H f O } _ { 2 }$ FET based on 3-D NAND Architecture: Towards Dense Low-Power Memory

K. Florent1 , M. Pesic2 , A. Subirats, K. Banerjee, S. Lavizzari3 , A. Arreghini, L. Di Piazza, G. Potoms, F. Sebaai, S. R. C. McMitchell, M. Popovici, G. Groeseneken1 and J. Van Houdt1

imec, Leuven, Belgium, email : karine.florent@imec.be

1 also with ESAT- KU Leuven, Leuven, Belgium, 2 MDLSoft Inc, Santa Clara, CA, USA, 3 now with Prophesee, Paris, France

Abstract— A vertical ferroelectric HfO2 field effect transistor based on 3-D macaroni NAND architecture is reported for the first time. Up to 2 V memory window was obtained after the application of 100 ns program/erase pulses. Flash-like endurance of $1 0 ^ { 4 }$ cycles is reported and first reliability assessments were performed.

# I. INTRODUCTION

The memory market is currently in an era of tremendous growth: the big data explosion has yielded the need for more and more data storage. Although 3-D NAND memory is a high density and cost-effective technology, it still suffers from some drawbacks, i.e. speed, cell size and power consumption at system level due to required periphery (e.g. charge pumps). Addressing these issues while keeping the advantages of this technology would be very appealing.

Recent years have seen a growing interest in ferroelectric (FE) memory applications. The discovery in 2011 of FE hafnium oxide enabled the emergence of scaled FE devices [1]. Planar $\mathrm { H f O } _ { 2 } .$ -based FE capacitors and FeFET (Ferroelectric Field Effect Transistor) have received large interest either as a replacement for Dynamic Random-Access Memory (DRAM) or for embedded applications [2-3]. A vertical 3-D FE-capacitor (FeCap) has also been realized using silicon electrodes [4]. Implementation of doped $\mathrm { H f O } _ { 2 } .$ - based 3-D FeCaps confirmed the presence of FE properties with 10-year retention [4]. The fabrication of these vertical 3-D FeCaps, using a 3-D NAND architecture, was the first step towards Vertical FeFET (V-FeFET) [5]. Such device could potentially have several benefits over the conventional 3-D NAND memory, such as lower power, periphery reduction, improved endurance and faster operations, while maintaining full CMOS compatibility and high-density.

In this study, a vertical macaroni-type 3-D FeFET with three transistors in series is reported. This is the first demonstration of such device.

# II. DEVICE FABRICATION

Fig. 1a shows the process sequence for the test device, consisting in a vertical string of three transistors in series with a channel length $( \mathrm { L _ { c h } } )$ of 50 nm. The fabrication steps until FE deposition are same as previous work [4]. Here, silicon was used as dopant in HfO2 to form the FE material, deposited by atomic layer deposition (ALD). A thin a-Si layer was then deposited as gate stack protection from the subsequent etching of the bottom of the hole, required to allow the contact between

the source junction at the substrate and the channel. A HF clean followed by a TMAH etch are then performed to remove the remains of the protective layer. A 20 nm n-type amorphous silicon $( 4 \mathrm { x } 1 0 ^ { 1 9 } \mathrm { c m } ^ { - 3 } )$ is then deposited as a channel. To crystallize the channel and the FE layer, a 30 min anneal is performed at 900 °C in an ambient mixture of $\mathbf { \dot { N } } _ { 2 }$ and $\mathrm { O } _ { 2 } .$ In the next step, the hole was filled with oxide and then recessed (hence macaroni structure). Highly doped n-type silicon was deposited on top of the structure to form the drain and then annealed. Finally, the staircase was formed, followed by metal contacts. A cross-section schematic of the complete test vehicle is shown in Fig. 1b. HR-TEM cross-section of a 100 nm diameter hole can be seen in Fig. 2. A deep recess in the substrate is visible due to the TMAH etch.

In parallel of the macaroni-type FeFET device fabrication, highly-doped full-channel 3-D devices were also made to confirm the presence of ferroelectricity in this configuration and extract FE properties, as previously described [4].

# III. RESULTS AND DISCUSSIONS

# A. Ferroelectric Capacitor:Material screening

9.5 nm- and 15 nm-thick Si:HfO2 were deposited in the full-channel configuration and characterized using polarization-voltage (P-V) measurements. Cycling dependent P-V and corresponding current-voltage (I-V) characteristics are shown in Fig. 3. Both thicknesses under test exhibited FE behavior accompanied by a slight wake-up. Fig. 4 shows the endurance of these devices up to $1 0 ^ { 5 }$ cycles. An initial increase in remnant polarization was observed which was followed by a stable behavior. No fatigue was observed, as devices were no longer operational after $1 0 ^ { 5 }$ cycles. Both devices have comparable FE characteristics. Due to the presence of several etch steps during device fabrication, which could potentially damage the FE layer, a 15 nm-thick dielectric was preferred.

# B. V-FeFET:Standard Electrical Characterization

Before investigating V-FeFET memory performance, standard transistor measurements were carried out. A pass voltage of 3 V was applied to both the top and the bottom transistors, while the source was grounded. Output characteristics $\mathrm { ( I _ { D } - V _ { D } ) }$ were recorded (Fig. 5) for a hole diameter of 70 nm. Typically for scaled MOSFET devices, an increase in current was observed at large drain and gate voltages. The $\mathrm { I } _ { \mathrm { D } ^ { - } } \mathrm { V } _ { \mathrm { G } }$ characteristics are shown in Fig. 6 for multiple devices with 70 nm hole diameter. The gate had negligible leakage current, as shown in the inset. An ON-

current of ~1 ȝA was achieved, while maintaining an OFFcurrent of a few $\mathrm { p A } ,$ giving an excellent ON/OFF ratio $\mathrm { o f } \sim 6$ decades. The statistical distributions of the threshold voltage $( \mathrm { V _ { T } } )$ , extracted using a constant current (CC) criterion (10 nA), the ON-current ION, taken at $\mathrm { V } _ { \mathrm { T } } + 2 \mathrm { V }$ and the subthreshold swing STS are shown in Fig. 7 for various hole diameters. $\mathrm { V _ { T } }$ and STS distributions were broad, which suggested the presence of a defect-rich HfO2 / Poly-Si interface.

# C. V-FeFET:Memory Characterization

As charge trapping at the interface can effect proper cell read-out, DC and pulsed $\mathrm { { I } _ { D } \mathrm { { - } } V _ { G } }$ measurement methodologies were benchmarked. This first technique is relatively slow, as each measurement at a given voltage requires milliseconds. In the presence of traps, this can lead to a degradation of the characteristics and to a smaller FE memory window (MW). Pulsed I-V measurements, which are in the order of microseconds at every voltage, can reduce charge trapping. FE MW is shown here for a vertical macaroni-type FET with a hole diameter of 70 nm, a pass voltage of 3 V and ± 10 V program/erase (PRG/ERS) pulse with a width of 100 ns (Fig. 8). A MW of ~2 V was obtained with pulsed I-V. This was further utilized as the preferred method to characterize memory devices, as DC I-V resulted in an $\mathrm { { I } _ { D } \mathrm { { - } } V _ { G } }$ degradation (charge trapping) as well as a smaller MW: MW pulsed ~2 V vs MW DC ~0.5 V.

To investigate the optimal operation conditions for the device, ISPP and ISPE on a 70 nm-diameter device were performed and are shown in Fig. 9 and 10, respectively. A ± 10 V with 100 ns pulse length was used to program and erase before the measurements. The ISPP showed a gradual increase in the MW with pulse amplitude, while ISPE yielded a more sudden step. This could be due to the presence of a small number of domains because of the small size of the device. The gradual programming could be the result of some trapping interferences and/or different domain growth kinetics. At larger pulse widths and high voltages, charge trapping starts to dominate FE.

The evolution of $\mathrm { V _ { T } }$ with cycling is shown in Fig. 11. Closure of the MW was observed at $1 0 ^ { 4 }$ cycles. A slight wake up period of around 10 cycles was initially observed. This was followed by a decrease in the MW. While the ERS state decreased slightly with cycling, the PRG state was much more impacted by the endurance possibly due to trapping [6]. Fig. 12 shows the PRG and ERS density distributions after 10 cycles. The device-to-device variability may be caused by differences in defect distribution and charge injection as well as variable FE properties, that can be affected by a combination of factors such as film uniformity and mechanical stress. The ERS state was narrower than the PRG, confirming that one state was more stable than the other. Further integration improvements are required to enhance MW characteristics.

# D. V-FeFET: Reliability Consideration

High fields over the interface can generate defects and can also cause injection of charges into defects, resulting in charge trapping which causes a reliability issue for FeFET devices. A way to study the trapping mechanisms in high-k material is to

use single-pulse technique [7]. The shift between the rising and falling edges of the pulse $\left( \Delta \mathbf { V } _ { \mathrm { T 2 1 } } = \mathbf { V } _ { \mathrm { T 2 ^ { - } } } \mathbf { V } _ { \mathrm { T 1 } } \right)$ is proportional to the number of trapped charges, here electrons (Fig. 13 inset). The trapping process was studied on a transistor in PRG state by changing the pulse width and amplitude. A positive $\Delta \mathrm { V } _ { \mathrm { T 2 1 } }$ shift in $\mathrm { { I } _ { D } \mathrm { { - } } V _ { G } }$ confirmed the occurrence of electron trapping (Fig. 13a) which increased with both pulse width and amplitude, as shown in Fig. 13b.

Retention measurements were also carried out. Short-term retention at $2 5 ~ ^ { \circ } \mathrm { C }$ (related to FE relaxation) showed a stronger degradation of the PRG state compared to the ERS state (Fig. 14) nicely correlating to the broader $\mathrm { V _ { T } }$ distributions of the PRG state compared to the ERS equivalent. The latter one stays relatively steady, with degradation occurring at higher voltages. The same remark held true for the PRG state but with a more intense degradation as a possible result of charge trapping and depolarization. Longer retention tests at $8 5 ~ ^ { \circ } \mathrm { C }$ confirmed a larger degradation of the PRG pulse (Fig. 15). A clear separation of states was observed after 100h at $8 5 ~ ^ { \circ } \mathrm { C }$ .

# E. Path for improvements

The presence of high-k dielectric as the gate oxide results in charge trapping phenomenon, countering the ferroelectric behavior. This is a known issue for HfO2 FeFET [6], which needs to be addressed through process integration optimization. A thick oxide, without special treatment or film improvement, was used, leading to large PRG/ERS voltages. This could be seen as too high for FE, however this corresponds to an electric field $\mathrm { o f } \sim 6 . 5$ MV/cm and is in agreement with the P-V loop shown in Fig. 3. A thinner gate oxide would reduce the operation voltage and additionally improve the reliability, i.e. reduce trapping and enhance endurance. Detailed reliability studies are required for better understanding of the device behavior, i.e. impact of pass voltages. The potential of 3-D FeFET and its advantages compared to the prior state-of-the-art are presented in Table 1. This technology offers low power high-density memory that decreases the speed gap between the central processing unit (CPU) and storage.

# IV. CONCLUSIONS

A functional vertical macaroni-type 3-D FeFET with three gates was fabricated and characterized for the first time. Memory window up to 2 V was obtained with pulse width of 100 ns. Endurance of $1 0 ^ { 4 }$ cycles and reliability assessments are also reported. A decrease of the FE layer thickness could potentially decrease the operation voltage and increase the endurance and lifetime of these devices. This study paves the way for a high-density high-speed non-volatile memory that reduces the gap between CPU and storage.

# REFERENCES

[1] T. S. Böscke et al, APL, vol. 99, no. 10, pp. 102903-1–102903.3, 2011   
[2] S. Dunkel et al., 2017 IEEE IEDM, pp. 19.7.1–19.7.4   
[3] M. Pesic et al., 2016 IEEE IEDM, pp. 11.6.1-11.6.4.   
[4] K. Florent et al., 2017 Symp. on VLSI Technology, pp. T158-T159.   
[5] Patent US 2016/0181259 A1, 2016   
[6] E. Yurchuk et al., IEEE TED, vol. 63, no. 9, pp. 3501-3507, 2016.   
[7] D. Heh et al., 2006 IEEE IIRW, pp. 120-124   
[8] H. Tanakaet al., 2007 Symp. on VLSI Technology, pp. 14-15

![](images/74eb689b539ea09380400364038a5d5bd451d9c86b2c6c819e5c638a7883f509.jpg)  
Figure 1. (a) Process Flow description. (b) Schematic cross-section of the macaroni-type 3-D FeFET with three cells in series.

![](images/e4c0f7ab3795c60cb2c2526652be940929763f06650f81d1b0db7851f2faaa8b.jpg)  
Figure 2. TEM crosssection (Ø: 100nm)

![](images/a52c98e697250ef8caf19dcdce29bc7dbc89e44b2311a73af34d05b76e8cf849.jpg)  
Figure 3. Polarization - voltage (P-V) and corresponding current - voltage (I-V) characteristics for 3-D capacitors with (left) 9.5 nm- and (right) 15 nm-thick Si:HfO2.

![](images/7c869239e5be17829e958ab563a2c8ccf3951bb627d15bacdb4e436e7b396b93.jpg)  
Figure 4. (Top) Positive $\mathrm { P _ { r } ^ { + } }$ and negative $\mathrm { P _ { r } ^ { \mathrm { ~ - ~ } } }$ remnant polarization for 3-D capacitors. (Bottom) 2Pr endurance showing wake-up behavior.

![](images/0c85294d279a691e726c1a4902e397b209306c3c964e949829807a1887e97141.jpg)  
Figure 5. Output characteristics $\left( \mathrm { { I } _ { D } \mathrm { { - } } \mathrm { { V } _ { D } } } \right)$ of control gate with 3 V pass voltage, exhibiting typical behavior for scaled MOSFET devices. $( \mathrm { L } _ { \mathrm { c h } } { = } 5 0 \ \mathrm { n m } )$

![](images/4e599dea21205c2cb9e7cda3b5a3dd8bf56b9746d59d1cc1f55969f500f54d62.jpg)  
Figure 6. $\mathrm { I } _ { \mathrm { D } ^ { - } } \mathrm { V } _ { \mathrm { G } }$ of control gate transistors with $\mathrm { { V _ { D } } } = 1 \mathrm { { V } }$ and $\mathrm { V } _ { \mathrm { p a s s } } = 3 \mathrm { V }$ for top and bottom selectors. (inset) $\mathrm { I } _ { \mathrm { G } } { - } \mathrm { V } _ { \mathrm { G } }$ showing no leakage. $( \mathrm { L } _ { \mathrm { c h } } = 5 0 $ nm and Ø: 70 nm)

![](images/ed2def3a95c747705aa6718010f31606db98d552b389d188fb44aefd7598709c.jpg)

![](images/663c2822378a5bbe01a1c55bdff399aac618b1b12a9a08eea8b93ad9451fb99b.jpg)

![](images/e19d79d58833a12fc2191cd43cc459eed4ae3428e5987c85f79496c48b253524.jpg)  
Figure 7. Statistical distribution of (a) $\mathrm { V _ { T } }$ taken at CC criterion (10 nA), (b) $\mathrm { I _ { O N } }$ at $\mathrm { ~ V ~ + ~ } 2 \mathrm { V }$ , and (c) Subthreshold swing for various diameter holes. Broad distributions of $\mathbf { \ddot { V } } _ { \mathrm { T } }$ and STS could indicate the presence of traps at the ${ \mathrm { H f O } } _ { 2 } / { \mathrm { P o l y } } .$ - Si interface. $( \mathrm { L } _ { \mathrm { c h } } { = } 5 0 \ \mathrm { n m } )$

![](images/c51327d3a2938ee80d1e3a2b15a8d4cdf9ffe1232af6305b024fb0f3dfb9fb24.jpg)  
Figure 8. Comparison between DC ID- $. \mathrm { v _ { G } }$ and Pulsed $\mathrm { { I } _ { D } \mathrm { { - } } V _ { G } }$ after PRG and ERS (±10 V – 100 ns). A MW of ~2 V was measured

![](images/53371647833cc6aca6fb8f7b46dc3be7550b01fc8cbcf5054089aed9426ace47.jpg)  
Figure 9. ISPP after -10 V/100 ns erase pulse. A gradual increase is observed with pulse amplitude. Blue: no MW, Yellow: Max MW

![](images/a2de3a57688e4017a125b0b9ae8e28447f8c8e3e613c6f88dadc3b8cc0adba7c.jpg)  
Figure 10. ISPE after +10 V/100 ns program pulse. The MW increase is more sudden. Blue: no MW, Yellow: Max MW

![](images/1a5a25470bd84faf8e13bcf0c890e77be7a64054d8fcf85b3c25de89e8921423.jpg)  
Figure 11. $\mathrm { V _ { T } }$ evolution with cycling after PRG and ERS. A larger degradation of PRG is observed.

![](images/be1ca7add5c27e46b042d00454b7aacb3d6f79d1c7d704d276d88e7580ec1804.jpg)  
Figure 12. $\mathrm { V _ { T } }$ after 10 cycles (±10 V – 100 ns). ERS distribution is narrower than PRG distribution. (Ø: 70 nm)

![](images/842686611aea0ff1c381c08d144545dfcfd61b7a5c61f19fbdc17d994b305a88.jpg)  
Figure 13. (a) Single pulse ID- $\mathbf { \nabla \cdot V _ { G } }$ (obtained from rising/falling edge) after PRG for incrementing pulse width tTP, (b) $\Delta \mathrm { V } _ { \mathrm { T 2 1 } }$ vs tTP $( \Delta \mathrm { V } _ { \mathrm { T } }$ extracted at $\mathrm { I _ { D } } = 4 \mathrm { x } 1 0 ^ { 7 } \mathrm { \Delta A }$ , pulse width: 100 ȝs to 10 ms, pulse amplitude: 2 V to 3 V)

![](images/8cd380a07b3a71701ab68ee2a2a00f6f22140680ebcd291b0fd62a693271aaa2.jpg)  
Figure 14. Short retention at $2 5 ~ ^ { \circ } \mathrm { C }$ for (top) PRG and (bottom) ERS states, showing degradation of PRG state.

![](images/f51cf8e29be5b875b271e90e80a30f779fd8b48eacc21a3da1cafc3b0148621c.jpg)  
Figure 15. Retention at $8 5 ~ ^ { \circ } \mathrm { C }$ showing some retention loss of PRG after 100 h.

Table 1. Comparison with prior art   

<table><tr><td></td><td>Planar FeFET[2]</td><td>Flash NAND[8]</td><td>This work</td></tr><tr><td>Energy</td><td>&lt; 1fJ/bit</td><td>&lt; 1nJ/bit</td><td>&lt; 1fJ/bit</td></tr><tr><td>Endurance</td><td>105cycles</td><td>104cycles (MLC)</td><td>104cycles</td></tr><tr><td>PRG/ERS Speed</td><td>10 ns / 10 ns</td><td>100 us / 10 ms</td><td>100 ns/100 ns</td></tr><tr><td>Retention at 85 °C</td><td>10 years (expected)</td><td>10 years</td><td>10 years (expected)</td></tr><tr><td>Cell area</td><td>0.025 μm2</td><td>0.026 μm2per Nlayer*↑</td><td>0.026 μm2per Nlayer*</td></tr><tr><td>Multibit capability</td><td>NA</td><td>Yes</td><td>NA</td></tr></table>

* Stackable devices with pitch size of 160 nm   
† Assumed similar to this work