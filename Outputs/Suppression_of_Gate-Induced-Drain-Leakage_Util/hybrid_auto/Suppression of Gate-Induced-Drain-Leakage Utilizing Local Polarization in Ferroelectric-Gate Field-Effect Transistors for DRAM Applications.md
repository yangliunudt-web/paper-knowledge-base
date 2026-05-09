---
title: "Suppression of Gate-Induced-Drain-Leakage Utilizing Local Polarization in Ferroelectric-Gate Field-Effect Transistors for DRAM Applications"
authors:
  - "Been Kwak"
  - "Kitae Lee"
  - "Sihyun Kim"
  - "Daewoong Kwon"
date: "2024-01-01"
year: "2024"
journal: "IEEE Electron Device Letters"
doi: "10.1109/LED.2024.3371234"
abstract: "This study proposed a novel approach to enhance the retention characteristics in dynamic random access memory (DRAM) by employing a unique local polarization method, attempting to increase the threshold voltage $( V _ { \\mathrm { t h } } )$ to reduce subthreshold leakage current while alleviating gate-induced drain leakage (GIDL) current in a ferroelectric gate-field effect transistor with a recessed circular channel. Through the optimization of the position-dependent polarization control along the channel, it is revealed that the polarizations on the source/drain sides can be independently adjusted without interference, resulting in an impressive 80% reduction in GIDL current accompanied by an increase in $V _ { \\mathrm { { f h } } }$ by localized polarizations. Moreover, robustness measurements against temperature variations and read stress confirmed the stable maintenance of locally polarized states, underscoring an effective approach to addressing the performance and reliability limitations of DRAM cell transistors. Index Terms— FeFET, dynamic random access memory, recessed channel, gate-induced drain leakage, local polarization."
abstract_cn: "本研究提出一种利用局部极化工程增强DRAM保持特性的新方法，通过在铁电场效应晶体管（FeFET）中独立控制源侧和漏侧极化，有效抑制栅致漏极泄漏电流（GIDL），实现保持特性的改善。"
keywords:
  - "[[FeFET]]"
  - "[[DRAM]]"
  - "[[Gate-induced drain leakage]]"
  - "[[Local polarization]]"
  - "[[Recessed channel]]"
cite: "[1] Kwak et al. Suppression of Gate-Induced-Drain-Leakage Utilizing Local Polarization in Ferroelectric-Gate Field-Effect Transistors for DRAM Applications[J]. IEEE Electron Device Letters, 2024."
aiSum: "局部极化工程抑制FeFET的GIDL：独立控制源/漏侧极化，改善DRAM保持特性，实现无泄漏高性能存储单元。"
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
---

Been Kwak , Kitae Lee , Sihyun Kim , Member, IEEE, and Daewoong Kwon

Abstract— This study proposed a novel approach to enhance the retention characteristics in dynamic random access memory (DRAM) by employing a unique local polarization method, attempting to increase the threshold voltage $( V _ { \mathrm { t h } } )$ to reduce subthreshold leakage current while alleviating gate-induced drain leakage (GIDL) current in a ferroelectric gate-field effect transistor with a recessed circular channel. Through the optimization of the position-dependent polarization control along the channel, it is revealed that the polarizations on the source/drain sides can be independently adjusted without interference, resulting in an impressive 80% reduction in GIDL current accompanied by an increase in $V _ { \mathrm { { f h } } }$ by localized polarizations. Moreover, robustness measurements against temperature variations and read stress confirmed the stable maintenance of locally polarized states, underscoring an effective approach to addressing the performance and reliability limitations of DRAM cell transistors.

Index Terms— FeFET, dynamic random access memory, recessed channel, gate-induced drain leakage, local polarization.

# I. INTRODUCTION

HERE are numerous obstacles in terms of fabrication processes and electrical properties for further scaling

Manuscript received 30 November 2023; revised 9 February 2024; accepted 19 February 2024. Date of publication 27 February 2024; date of current version 26 April 2024. This work was supported in part by the National Research Foundation of Korea (NRF) grant funded by the Korea Government Ministry of Science and ICT (MSIT) under Grant RS-2023-00260527; in part by the National Research and Development Program through the NRF funded by MSIT under Grant RS-2023- 00257003; in part by the MSIT, Korea, under the ITRC (Information Technology Research Center) support Program the IITP (Institute for Information and Communications Technology Planning and Evaluation under Grant IITP-2024-RS-2023-00260091; in part by the National Research and Development Program through the NRF funded by MSIT under Grant 2021M3H2A1038042; and in part by Samsung Electronics Company Ltd., under Grant 202370026.02. The review of this letter was arranged by Editor M. Kobayashi. (Been Kwak and Kitae Lee contributed equally to this work.) (Corresponding authors: Sihyun Kim; Daewoong Kwon.)

Been Kwak and Daewoong Kwon are with the Department of Electronic Engineering, Hanyang University, Seoul 04763, South Korea (e-mail: dw79kwon@hanyang.ac.kr).

Kitae Lee is with the Department of Electrical and Computer Engineering and the Inter-University Semiconductor Research Center, Seoul National University, Seoul 08826, South Korea.

Sihyun Kim is with the Department of Electronic Engineering, Sogang University, Seoul 04107, South Korea (e-mail: skim@sogang.ac.kr).

Color versions of one or more figures in this letter are available at https://doi.org/10.1109/LED.2024.3370592.

Digital Object Identifier 10.1109/LED.2024.3370592

down of dynamic random-access memories (DRAM) beyond the nanoscale node [1], [2], [3]. Off-state leakage current in a DRAM cell transistor, which degrades the retention characteristics during holding operation by reducing the stored charge in a capacitor, is one of the critical problems because the loss of the stored charge can seriously deteriorate the sensing margin. Typically, the leakage current of a DRAM cell transistor originates from subthreshold leakage, the generation of electron–hole pairs in the depletion region of the junction, punch-through, and gate-induced drain leakage (GIDL) [4], [5], [6], [7].

To suppress the leakage current, saddle-structured cell transistors with a recessed channel have been studied because the recessed channel extends the channel length, and the saddle-shaped channel enhances gate controllability while maintaining the same footprint, effectively mitigating the off-state leakage current caused by short channel effects (SCE) [8], [9], [10], [11], [12], [13]. However, despite the suppressed SCEs, the GIDL generated by band-to-band tunneling in the gate-to-drain overlap region cannot be controlled. Recently, dual work-function metal (WFM) gate technology has been introduced to DRAM cell transistors to increase the source-side threshold voltage $( V _ { \mathrm { t h } } )$ for the reduction of subthreshold leakage and to decrease drain-side $V _ { \mathrm { t h } }$ for GIDL mitigation simultaneously [14], [15]. Nonetheless, an additional GIDL suppression method is required to scale down the capacitor.

This study demonstrated a ferroelectric-gate field-effect transistor with a recessed channel and single WFM gate (R-FeFET) as a DRAM cell transistor. In the R-FeFET, a novel method for the reduction of both the subthreshold leakage and GIDL was proposed without complicated dual WFM gate processes by independently adjusting the source-side $V _ { \mathrm { t h } }$ (increasing $V _ { \mathrm { t h } } )$ and drain-side $V _ { \mathrm { t h } }$ (decreasing $V _ { \mathrm { t h } } )$ utilizing the local polarization properties of the polycrystalline ferroelectric material [15], [16]. To verify the feasibility of the proposed local polarization, the independent modulation of $V _ { \mathrm { t h } }$ and GIDL was realized in the fabricated R-FeFET. Furthermore, the robustness of the stored locally polarized states against temperature and repetitive read pulses was rigorously investigated to ensure stable DRAM write-and-read operations.

# II. FABRICATION OF R-FEFET

The process flow of an R-FeFET is illustrated in Figs. 1(a) and (b). The source/drain/body implantation and

![](images/34df296f813c1dc401a209c7ed8db9b1f1cb8dca04d4fe89af5d8c6adf079c98.jpg)  
(a)

![](images/724d879e1fa978e623710dbd2569e53592cf133f05fa56dae5fe6fa1eb376b65.jpg)  
(b)

![](images/a9421ad5097a18b0081ba64e0e609d3404e20511fb2e51244fe500dde6f506d2.jpg)  
Fig. 1. (a) Process flow of R-FeFET. (b) illustrations of its key processes. Cross-sectional transmission electron microscopy (TEM) images of (c) fabricated R-FeFET with channel radius of $7 \dot { 5 }$ nm and (d) zoomed-in view of same.

activation were performed on a bulk Si substrate. After the active isolation process, a SiN spacer was formed through hard-mask patterning to set $L _ { \mathrm { o p e n } }$ to approximately 70 nm [(i) in Figs. 1(b)]. Moreover, to achieve a recessed channel, isotropic dry etching with ${ \mathrm { S F } } _ { 6 }$ gas was performed [(ii) in Fig. 1(b)]. Following sequential SC-1 and HF cleaning to eliminate etching-induced damage in the channel regions, a gate stack, comprising a SiO2 interlayer (IL) of 1.5 nm, an HZO ferroelectric layer (FE) of 5.5 nm, and a TiN gate metal, was deposited sequentially via atomic layer deposition. Post-metal annealing was performed to facilitate ferroelectric crystallization at $5 0 0 ~ ^ { \circ } \mathrm { C }$ for 30 s under ${ \Nu } _ { 2 }$ ambient [17]. Subsequently, alloying was performed [(iii) in Fig. 1(b)]. Figs. 1(c) and (d) present TEM images of the fabricated R-FeFET, verifying that the recessed channel with a radius (r) of 75 nm is completely covered by a thin IL/FE gate stack [18].

Unlike FeFETs with a planar structure (P-FeFET), where the electric field (e-field) distribution remains constant across the FE/IL, in the R-FeFET, the e-field increases towards the center of the gate metal [Fig. 3(a)] according to Gauss’s law, which enhances the memory performance by increasing the e-field across the FE and simultaneously improves the reliability by mitigating the e-field over the IL [19], [20].

# III. RESULT AND DISCUSSION

The memory characteristics of the fabricated R-FeFETs were evaluated using the square-pulsed program/erase (erase voltage: $\begin{array} { r c l } { V _ { \mathrm { E R S } } } & { = } & { - 4 \ – ( - 6 ) } \end{array}$ V and program voltage: $V _ { \mathrm { P G M } } = 4 { - } 6 \ \mathrm { V } ,$ pulse width = 50 ns–100 us) and DC read (nondisruptive range of read voltage: $V _ { \mathrm { R E A D } }$ from 0 to 1.5 V). Figs. 2(a) and (b) demonstrate the $V _ { \mathrm { t h } }$ change with respect to various $V _ { \mathrm { P G M S } } / V _ { \mathrm { E R S } } \mathrm { s }$ and PGM/ERS times (tPGM/tERS), respectively. All the $V _ { \mathrm { t h } } \mathrm { s }$ were extracted at $I _ { \mathrm { D } } = 1 0 ^ { - 8 } \mathrm { ~ A ~ }$ , and the memory window (MW) was calculated as a $V _ { \mathrm { t h } }$ difference between PGM and ERS states. Figs. 2(c) and (d) illustrate the drain current (ID)–gate voltage $( V _ { \mathrm { G } } )$ curves of the R-FeFETs (transfer curves) for 4.5 V VPGM and −6 V $V _ { \mathrm { E R S } }$ according to the pulse width. The MW of ${ \sim } 0 . 9$ V was observed by full polarization $( V _ { \mathrm { P G M } }$ of 4.5 V/ $t _ { \mathrm { P G M } }$ of 100 $\mu \mathrm { s }$ , VERS of −6 V/ tERS of $1 0 0 ~ \mu \mathrm { s } )$ . Note that the measured MW of the R-FeFET is slightly far from the theoretical maximum

![](images/57ef4cb396f6d0ea95d50d99b5f2b53464b9103a44c5d9f8cb0ef59c9772b17b.jpg)

![](images/ac9325024d6bd553524473b4f7d4c00ab1d66f5675823412aa3aaaa1dfa54549.jpg)

![](images/c8d5a601e26794ed3903852ba5525bbc92b60d00a9bfbe74e09a5b1e18b09cf2.jpg)

![](images/d8d3dbd7fac3b318c6dc056b8b028d62fa4951a07b1ec00de9d5571dc34bd8a6.jpg)  
Fig. 2. Threshold voltage change with respect to various (a) $V _ { \mathsf { P G M } } { \mathsf { s } } /$ (b) $V _ { E \mathsf { R S } } \mathsf { s }$ and pulse widths. Change of transfer curves in R-FeFET by (c) (4.5 V) and (d) ERS (−6V) with various pulse widths (from 50 ns to 100 us).

![](images/db680d767f556e419e7f48e6b153fc59f581f4fba68518bad17e7e8d547f9cda.jpg)  
@ Conventional DRAM Tr.

![](images/266b22555736ef1d89e254aaf6993381d414a9d455d62d2b7c6923a2339fd841.jpg)

![](images/fbc47602b2157c87323b7ed54ffb2d808fead87656fde361d5cf5c304083b2c8.jpg)

![](images/49c979f4154863bf3517ad2b9b549faf1c5b443628324ccc581def90295898c2.jpg)  
Fig. 3. (a) Conventional DRAM transistor utilizing dual work-function metals for high $V _ { \mathrm { { f h } } }$ and low GIDL current. (b) Transfer curves (solid) of R-FeFET with suppressed $I _ { \mathsf { G I D l } }$ L by drain side local polarization at $V _ { \mathsf { D } } =$ 1 V, and the projected curves (dot) with decreased junction leakage currents $( I _ { \mathsf { J L S } } ) .$ . Schematic images indicating a change of polarization state along the channel by (c) VERS and (d) subsequent $V _ { \mathsf { G I D L } }$ .

because of charge trapping at the interface trap states between the recessed Si channel and the IL, which is generated by the etching damage during the channel recess dry etching process although sufficient cleaning processes were performed to remove the damaged regions.

In conventional DRAM cell transistors, dual WFM gate technology has been introduced to increase $V _ { \mathrm { t h } }$ on the source side for the reduction of subthreshold leakage by overlapping

![](images/6bd405d514fb803cbecfefe7445085cbf6bd0903d1ffc115b67fae5caa65ca82.jpg)

![](images/3e0808b098f90652b4ab53cc62b88cbfbec7d06c8b9ed57c2b2b4cd80e89f90d.jpg)  
Fig. 4. Retention characteristics for $I _ { 0 \mathsf { n } }$ and suppressed $I _ { \mathsf { G I D L } }$ at (a) ${ } ^ { 3 0 ^ { \circ } \mathsf { C } }$ and (b) $8 5 ^ { \circ } \mathsf { C }$ .

sources with a high WFM (M2) and to lower the drain-side $V _ { \mathrm { t h } }$ for the suppression of the GIDL current (IGIDL) by overlapping the drain with a low WFM (M1) [Fig. 3(a)]. However, utilizing the local polarization switching properties of R-FeFETs, high $V _ { \mathrm { t h } }$ and low $I _ { \mathrm { G I D L } }$ can be implemented simultaneously with a single WFM gate, as illustrated in Figs. 3(c) and (d). The operation sequence for local polarization can be performed as follows: 1) To achieve a full ERS state, $\mathrm { ~ a ~ } - 6 \mathrm { ~ V ~ } \ V _ { \mathrm { E R S } }$ is applied for 10 µs to the gate with a grounded source/drain (S/D). 2) To locally polarize the drain side, the gate and source were then biased with a $V _ { \mathrm { P G M } }$ pulse of 4.5 V for 10 $\mu \mathrm { s }$ with a grounded drain (this bias condition is defined as VGIDL). Hence, only the drain side polarization was driven up by $V _ { \mathrm { G I D L } }$ , whereas the negative polarization was maintained on the source side because the potential difference between the gate and source was approximately zero [Figs. 3(c) and (d)]. Therefore, Fig. 3(b) demonstrates that increasing $V _ { \mathrm { t h } }$ and corresponding on-current $( I _ { \mathrm { o n } } )$ remain unchanged with an 80% reduction in IGIDL (measured at drain voltage of 1 V) after applying VGIDL because only the drain-side $V _ { \mathrm { t h } }$ becomes locally decreased.

Here, it should be noted that the GIDL reduction was underestimated due to the large junction leakage current $( I _ { \mathrm { J L } } )$ , which might be originated from the process-induced channel damage. The dotted lines of Fig 2 (b) represent the projected transfer curves with decreased $I _ { \mathrm { J L } } s ,$ , exhibiting that the GIDL could be suppressed down to 90% by the proposed scheme when the $I _ { \mathrm { J L } }$ was controlled to $1 0 ^ { - 1 3 } \mathrm { \ A / / } \dot { \mu } \mathrm { m }$ , which is the typical $I _ { \mathrm { o f f } }$ range of industrial buried cell transistors.

To verify the thermal stability of the source/drain side polarized states, which should be sustained once established, retention characteristics were evaluated at $3 0 ~ ^ { \circ } \mathrm { C }$ and $8 5 ~ ^ { \circ } \mathrm { C }$ . IGIDL and $I _ { \mathrm { o n } }$ were monitored at $V _ { \mathrm { G } } ~ = ~ 0 ~ \mathrm { V }$ and $V _ { \mathrm { G } } ~ =$ 1.5 V as a function of time. Fig. 4(a) and (b) demonstrates that the changes in IGIDL and $I _ { \mathrm { o n } }$ are negligible over $1 0 ^ { 3 }$ s (robust thermal stability) after VERS and subsequent $V _ { \mathrm { G I D L } }$ , indicating that increasing $V _ { \mathrm { t h } }$ and reducing $I _ { \mathrm { G I D L } }$ can be stably maintained against thermal variations. Notably, the mitigated GIDL by local polarization was stably retained even at $8 5 ^ { \circ } \mathrm { C }$ although the higher off-current was observed due to the increasing thermally generated electron-hole pairs (EHP).

Changes in $I _ { \mathrm { G I D I } }$ and $I _ { \mathrm { o n } }$ due to repetitive read operations (i.e., read disturbance) were investigated. After the formation of the source/drain-side localized polarization states by the sequential application of $V _ { \mathrm { E R S } }$ and $V _ { \mathrm { G I D L } }$ pulses, read pulses

![](images/ea0e97fb1826d1048e55f3037ce611bb870a6eb5cf78b166e7e6b2e784a84c49.jpg)  
(a)Read disturbance condition

![](images/104173231f19eb4d3426f90edd4fb80ff415affc8ee364b9d5602e558f0bb575.jpg)  
Fig. 5. (a) Voltage and timing diagram of read stress. $( \mathrm { b } ) \mathrm { - } ( \mathrm { d } )$ Change of Ion and $I _ { \mathsf { G I D L } }$ with respect to the number of read cycling, where various $V _ { \sf r e a d } \bar { \sf s }$ (from 2 to 3 V) were repeatedly applied with various $t _ { \mathrm { r e a d } } s$ (from 30 to 50 ns).

with various amplitudes $( V _ { \mathrm { r e a d } } \colon 2 { - } 3 \mathrm { ~ V } )$ and widths of 30–50 ns (read time: $t _ { \mathrm { r e a d } } )$ were repeatedly applied, as depicted in Fig. 5(a). Subsequently, IGIDL (at $V _ { \mathrm { G } } = 0 ~ \mathrm { V } )$ and $I _ { \mathrm { o n } }$ (at $V _ { \mathrm { G } } = 1 . 5 ~ \mathrm { V } )$ were measured with respect to the number of read cycles. Note that $V _ { \mathrm { r e a d } }$ and $t _ { \mathrm { r e a d } }$ for read cycling were determined by considering the voltage and time applied to the gate of a cell transistor during DRAM write/read operations. A relatively large $V _ { \mathrm { r e a d } }$ was applied during the longer $t _ { \mathrm { r e a d } }$ as a stress compared to those of practical DRAM write/read operations to accelerate the read stress. Figs. 5(b)–(d) demonstrate that the improvement in $I _ { \mathrm { G I D L } }$ was maintained stably even after the read stress. Furthermore, $I _ { \mathrm { o n } }$ remained unchanged while suppressing IGIDL for up to $1 0 ^ { 4 }$ cycles, demonstrating the feasibility of single WFM R-FeFETs with locally polarized states on the source/drain side as a DRAM cell transistor with low leakage currents.

# IV. CONCLUSION

To improve the retention characteristics of DRAM, a novel local polarization method to increase $V _ { \mathrm { t h } }$ for reducing the subthreshold leakage current and simultaneously mitigating the GIDL current was proposed in an R-FeFET with a single WFM gate. Sequential $V _ { \mathrm { E R S } }$ and $V _ { \mathrm { G I D L } }$ pulses were applied to implement local polarization on the source/drain side. As a result, it was found that source/drain side polarizations were independently controllable without interference, resulting in an 80% reduction in $I _ { \mathrm { G I D I } }$ L with increasing $V _ { \mathrm { t h } }$ by the localized polarizations.

Furthermore, robustness measurements against temperature and read stress confirmed that the locally polarized states could be stably maintained once established, highlighting their potential feasibility for a DRAM cell transistor. Our verification of simultaneously high $V _ { \mathrm { t h } }$ and mitigated $I _ { \mathrm { G I D L } }$ in the proposed R-FeFET suggests an efficient guideline for overcoming DRAM’s performance and reliability limitations.

# REFERENCES

[1] W. Mueller, G. Aichmayr, W. Bergner, E. Erben, T. Hecht, C. Kapteyn, A. Kersch, S. Kudelka, F. Lau, J. Luetzen, A. Orth, J. Nuetzel, T. Schloesser, A. Scholz, U. Schroeder, A. Sieck, A. Spitzer, M. Strasser, P.-F. Wang, S. Wege, and R. Weis, “Challenges for the DRAM cell scaling to 40nm,” in IEDM Tech. Dig., Washington, DC, USA, Dec. 2005, p. 4, doi: 10.1109/IEDM.2005.1609344.   
[2] J. A. Mandelman, R. H. Dennard, G. B. Bronner, J. K. DeBrosse, R. Divakaruni, Y. Li, and C. J. Radens, “Challenges and future directions for the scaling of dynamic random-access memory (DRAM),” IBM J. Res. Develop., vol. 46, no. 2.3, pp. 187–212, Mar. 2002, doi: 10.1147/RD.462.0187.   
[3] J. M. Park, Y. S. Hwang, S.-W. Kim, S. Y. Han, J. S. Park, J. Kim, J. W. Seo, B. S. Kim, S. H. Shin, C. H. Cho, S. W. Nam, H. S. Hong, K. P. Lee, G. Y. Jin, and E. S. Jung, “20 nm DRAM: A new beginning of another revolution,” in IEDM Tech. Dig., Washington, DC, USA, Dec. 2015, pp. 26.5.1–26.5.4, doi: 10.1109/IEDM.2015.7409774.   
[4] K. C. Chun, Y.-G. Chu, J.-S. Heo, T.-S. Kim, S. Kim, H.-K. Yang, M.-J. Kim, C.-K. Lee, J. Kim, H. Yoon, C.-H. Shin, S. Cha, H.-J. Kim, Y.-S. Kim, K. Kim, Y.-J. Kim, W. Choi, D.-S. Yim, I. Moon, Y.-J. Kim, J. Lee, Y. Choi, Y. Kwon, S.-W. Choi, J.-W. Kim, Y.-S. Park, W. Kang, J. Chung, S. Kim, Y. Ryu, S.-J. Cho, H. Shin, H. Jung, S. Kwon, K. Kang, J. Lee, Y. Song, Y.-J. Kim, E.-A. Kim, K.-S. Ha, K.-H. Kim, S.-H. Hyun, S. Ko, J.-H. Choi, Y.-S. Sohn, K.-I. Park, and S.-J. Jang, “A 16 Gb LPDDR4X SDRAM with an NBTI-tolerant circuit solution, an SWD PMOS GIDL reduction technique, an adaptive gear-down scheme and a metastable-free DQS aligner in a 10 nm class DRAM process,” in IEEE Int. Solid-State Circuits Conf. (ISSCC) Dig. Tech. Papers, San Francisco, CA, USA, Feb. 2018, pp. 206–208, doi: 10.1109/ISSCC.2018.8310256.   
[5] M. Chang, J. Lin, S. N. Shih, T.-C. Wu, B. Huang, J. Yang, and P.-I. Lee, “Impact of gate-induced drain leakage on retention time distribution of 256 Mbit DRAM with negative wordline bias,” IEEE Trans. Electron Devices, vol. 50, no. 4, pp. 1036–1041, Apr. 2003, doi: 10.1109/TED.2003.812498.   
[6] K.-H. Park, K.-R. Han, Y. M. Kim, and J.-H. Lee, “Simulation study of high-performance modified saddle MOSFET for sub-50-nm DRAM cell transistors,” IEEE Electron Device Lett., vol. 27, no. 9, pp. 759–761, Sep. 2006, doi: 10.1109/LED.2006.880833.   
[7] M. H. Cho, N. Jeon, T. Y. Kim, M. Jeong, S. Lee, J. S. Hong, H. S. Hong, and S. Yamada, “An innovative indicator to evaluate DRAM cell transistor leakage current distribution,” IEEE J. Electron Devices Soc., vol. 6, pp. 494–499, 2018, doi: 10.1109/JEDS.2017.2758026.   
[8] S.-W. Park, S.-J. Hong, J.-W. Kim, J.-G. Jeong, K.-D. Yoo, S.-C. Moon, H.-C. Sohn, N.-J. Kwak, Y.-S. Cho, S.-J. Baek, H.-S. Park, H. G. Yoon, B.-H. Lee, J.-S. Kim, S.-H. Hwang, L.-H. Lee, H.-J. Cho, S. Y. Cho, C.-O. Chung, K.-O. Kim, M.-S. Yoo, S.-A. Jang, S.-D. Lee, and S.-W. Chung, “Highly scalable saddle-fin (S-Fin) transistor for sub-50 nm DRAM technology,” in Proc. Symp. VLSI Technol., Honolulu, HI, USA, Jun. 2006, pp. 32–33, doi: 10.1109/VLSIT.2006.1705202.   
[9] S. K. Gautam, S. K. Manhas, A. Kumar, M. Pakala, and E. Yieh, “Row hammering mitigation using metal nanowire in saddle fin DRAM,” IEEE Trans. Electron Devices, vol. 66, no. 10, pp. 4170–4175, Oct. 2019, doi: 10.1109/TED.2019.2931347.   
[10] J.-W. Han, J. Kim, D.-I. Moon, J.-S. Lee, and M. Meyyappan, “Soft error in saddle fin based DRAM,” IEEE Electron Device Lett., vol. 40, no. 4, pp. 494–497, Apr. 2019, doi: 10.1109/LED.2019.2897685.

[11] J. Y. Kim, H. J. Oh, D. S. Woo, Y. S. Lee, D. H. Kim, S. E. Kim, G. W. Ha, H. J. Kim, N. J. Kang, J. M. Park, Y. S. Hwang, D. I. Kim, B. J. Park, M. Huh, B. H. Lee, S. B. Kim, M. H. Cho, M. Y. Jung, Y. I. Kim, C. Jin, D. W. Shin, M. S. Shim, C. S. Lee, W. S. Lee, J. C. Park, G. Y. Jin, Y. J. Park, and K. Kim, “S-RCAT (sphere-shapedrecess-channel-array transistor) technology for 70 nm DRAM feature size and beyond,” in Proc. Symp. VLSI Technol., Kyoto, Japan, Jun. 2005, pp. 34–35, doi: 10.1109/.2005.1469201.   
[12] J. Y. Kim, C. S. Lee, S. E. Kim, I. B. Chung, Y. M. Choi, B. J. Park, J. W. Lee, D. I. Kim, Y. S. Hwang, D. S. Hwang, H. K. Hwang, J. M. Park, D. H. Kim, N. J. Kang, M. H. Cho, M. Y. Jeong, H. J. Kim, J. N. Han, S. Y. Kim, B. Y. Nam, H. S. Park, S. H. Chung, J. H. Lee, J. S. Park, H. S. Kim, Y. J. Park, and K. Kim, “The breakthrough in data retention time of DRAM using recess-channel-array transistor(RCAT) for 88 nm feature size and beyond,” in Proc. Symp. VLSI Technol., Kyoto, Japan, Jun. 2003, pp. 11–12, doi: 10.1109/VLSIT.2003.1221061.   
[13] J. Y. Kim, D. S. Woo, H. J. Oh, H. J. Kim, S. E. Kim, B. J. Park, J. M. Kwon, M. S. Shim, G. W. Ha, J. W. Song, N. J. Kang, J. M. Park, H. K. Hwang, S. S. Song, Y. S. Hwang, D. I. Kim, D. H. Kim, M. Huh, D. H. Han, C. S. Lee, S. J. Park, Y. R. Kim, Y. S. Lee, M. Y. Jung, Y. I. Kim, B. H. Lee, M. H. Cho, W. T. Choi, H. S. Kim, G. Y. Jin, Y. J. Park, and K. Kim, “The excellent scalability of the RCAT (recess-channel-array-transistor) technology for sub-70 nm DRAM feature size and beyond,” in Proc. IEEE VLSI-TSA Int. Symp. VLSI Technol., Hsinchu, Taiwan, Apr. 2005, pp. 33–34, doi: 10.1109/VTSA.2005.1497071.   
[14] S. K. Gautam, S. Maheshwaram, S. K. Manhas, A. Kumar, S. Sherman, and S. H. Jo, “Reduction of GIDL using dual work-function metal gate in DRAM,” in Proc. IEEE 8th Int. Memory Workshop (IMW), Paris, France, May 2016, pp. 1–4, doi: 10.1109/IMW.2016. 7495287.   
[15] H. Kim, B. Kwak, J. H. Kim, and D. Kwon, “Frequency doubler based on ferroelectric tunnel field-effect transistor,” IEEE Trans. Electron Devices, vol. 69, no. 7, pp. 4046–4049, Jul. 2022, doi: 10.1109/TED.2022.3173245.   
[16] B. Kwak, K. Lee, N.-H. Park, S. J. Jeon, H. Kim, and D. Kwon, “Recessed channel ferroelectric-gate field-effect transistor memory with ferroelectric layer between dual metal gates,” IEEE Trans. Electron Devices, vol. 69, no. 3, pp. 1054–1057, Mar. 2022, doi: 10.1109/TED.2022.3144621.   
[17] C. Han, S. J. Kwon, J. Yim, J. Kim, S. Kim, S. Jeong, E. C. Park, J. W. You, R. Choi, and D. Kwon, “Effects of RTA rising time on ferroelectric characteristics of HfZrO2,” IEEE Trans. Electron Devices, vol. 69, no. 6, pp. 3499–3502, Jun. 2022, doi: 10.1109/TED.2022.3168237.   
[18] K. Lee, B. Kwak, S. Kim, and D. Kwon, “Demonstration of ferroelectric-gate field-effect transistors with recessed channels,” IEEE Electron Device Lett., vol. 45, no. 2, pp. 180–183, Feb. 2024, doi: 10.1109/LED.2023.3340254.   
[19] K. Lee, J.-H. Bae, S. Kim, J.-H. Lee, B.-G. Park, and D. Kwon, “Ferroelectric-gate field-effect transistor memory with recessed channel,” IEEE Electron Device Lett., vol. 41, no. 8, pp. 1201–1204, Aug. 2020, doi: 10.1109/LED.2020.3001129.   
[20] K. Lee, S. Kim, J.-H. Lee, B.-G. Park, and D. Kwon, “Ferroelectricmetal field-effect transistor with recessed channel for 1T-DRAM application,” IEEE J. Electron Devices Soc., vol. 10, pp. 13–18, 2022, doi: 10.1109/JEDS.2021.3127955.