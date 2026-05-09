---
title: "sub‑Scalable massively parallel computing using continuous‑time data representation"
authors:
  - "Scalable massively parallel computing using continuous-time data representation Cong Wang"
  - "Shi-Jun Liang"
  - "Chen-Yu Wang"
  - "Zai-Zheng Yang"
  - "Yingmeng Ge"
  - "Chen Pan"
  - "Xi Shen"
  - "Wei Wei"
  - "Yichen Zhao"
  - "Zaichen Zhang"
  - "Bin Cheng"
  - "Chuan Zhang"
  - "Feng Miao"
date: "2024‑01‑01"
year: 2024
journal: "Nature Communications"
doi: "10.1038/s41467‑024‑xxxxx"
abstract: "Supplementary information for the article 'Scalable massively parallel computing"
abstract_cn: "本文为《Scalable massively parallel computing using continuous‑time data"
cite: "Cong Wang, Shi‑Jun Liang, Chen‑Yu Wang, et al. sub‑Scalable massively parallel"
aiSum: "补充材料：包含补充图表和实验细节，支持主文中忆阻交叉阵列中连续时间数据表示和频率复用的大规模并行计算方案。"
confidence: "high"
---

# Supplementary information

# Scalable massively parallel computing using continuous-time data representation in nanoscale crossbar array

In the format provided by the authors and unedited

# Supplementary Information

Scalable massively parallel computing using continuous-time data representation Cong Wang1# , Shi-Jun Liang1# , Chen-Yu Wang1 , Zai-Zheng Yang1 , Yingmeng Ge2 , Chen Pan1 , Xi Shen1 , Wei Wei1 , Yichen Zhao1 , Zaichen Zhang2 , Bin Cheng1 , Chuan Zhang2 , Feng Miao1 *

1 Institute of brain-inspired intelligence, National Laboratory of Solid State Microstructures, School of Physics, Collaborative Innovation Center of Advanced Microstructures, Nanjing University, Nanjing, China.

2 National Mobile Communications Research Laboratory, Southeast University; Frontiers Science Center for Mobile Information Communication and Security, Southeast University; Purple Mountain Laboratories, Nanjing, China.

# C. Wang and S.J. Liang equally contributed to this work.

* Correspondence Email: miao@nju.edu.cn

![](images/2b3841d835c76f4eacbce285d76bbd3dd7e9967d7b65ec8c23dc6d4384389c9e.jpg)  
Supplementary Fig. 1 | Experimental results of FMC-based MMM operation implemented with the memristive crossbar array. The figure demonstrates the frequency spectrum of output currents from columns $( i . e . \ 1 , \ 2 , . . . 9 )$ of the memristor crossbar array, which represent the calculated results of one-shot MMM operation.

![](images/e0fe3a6d67412f0e6552c6346ebe3247c9dc49cc0d54d874f462f2d8969b3c13.jpg)  
Supplementary Fig. 2 | Experimental characterization of hardware. Error distribution of FMC using a 25×9 memristor crossbar array by applying random inputs that contain 16 frequencies. Error is defined as (Measured output - Expected output)/Expected output.

![](images/5fe0752d2e3f9be30bd145df997d369be922bf332b1a176bd787e46d0eb2aa66.jpg)

![](images/e1fe9aede9a9f32af9503e39f76501c652258229084fcb6bb3372c946982481d.jpg)

![](images/ca0f270dcdfef7c1d4b881af74291c4779a0a25258f6acc0a92f87927101e8b7.jpg)

![](images/9d5452e56a91134276e0efa6735e65a7171d5c41748facfbee383241c6881b61.jpg)

![](images/2868f671e7bb65e64bbfd1a89406ff48baf0acd0e27c2af356b002cfa2dd1e2a.jpg)

![](images/3b6fd9a95b62f8ae56aa6426faf7675c3ca5bf72f368194e5ceb44ae25e15580.jpg)  
Supplementary Fig. 3 | FMC modeling using memristive crossbar. a, Equivalent circuit modeling of memristor crossbar. Wire resistance R0 is estimated with copper wire with 200 nm thick, 1um width and 2 um length. b, The flow chart of the conductance compensation algorithm. By updating the device resistance, the algorithm can effectively enable the actual output behavior of memristor crossbar array (Reffective in the flow chart) to approach the target weight matrix $\mathrm { ( R _ { t a r g e t } }$ in the flow chart). The corresponding codes of the compensation algorithm are available at https://github.com/MiaoGroup/wire_resistance. c, Relationship between error distribution and Column of crossbars. d, Total error distribution of the crossbar. e, The relationship between the error parameters (standard deviation and mean) and crossbar size used for FMC. f, The relationship between the FMC error parameters (standard deviation and mean) and resistance range in 64×64 crossbar.

![](images/5585fa15ca71a1a85eb320fb0ef7d0beeeea190141e0d16fca889caaf2d1f43c.jpg)

![](images/d465768439aeed9ac63787707e60c1ba77fe6ea0e8cccf23c6d0f9a625ec4550.jpg)  
b   
Supplementary Fig. 4 | Comparison between von-Neumann-architecture-based parallel computing and the FMC-based scalable massively parallel computing. a, Traditional parallel architecture includes multiple processors and discrete memory, which communicate by shared memory bus. b, The FMC can be used to implement massively parallel processing of multiple computing tasks in a memristive crossbar array.

![](images/a90c80766093d0347c0ef7fd5d8406b906ad225b702379bab6e0b5f20054f33c.jpg)

![](images/fdbd97f5c6d3ac694840571daa4c3552cadfaad5f908ca663c867c14a20ef349.jpg)  
b   
Supplementary Fig. 5 | Handwritten digit recognition with the proposed FMC scheme. a, A group of 16 digit images are compressed and mapped into the crossbar array for data storage. The compressing procedure involves clipping and mean-pooling. The fully connected weights were transferred into the crossbar array for inference. b, Confusion matrix of our measured results for 1000 test images, an accuracy of 94.7% can be achieved. The test sets were generated from training set by adding 40% random Gaussian noise.

![](images/a4c47836bb693ddb0b92f2e536d8ec91404999c6e62167a2553806ca1407f0c8.jpg)  
a

![](images/a8af16d9019298eed742e8e30561a84c93a546d790686f44e9ecc78f1725f332.jpg)  
b

![](images/b7341eaabac6cdb91572149cbfbc151fdf27655daa8d4d8f09f86ea27a07b9e3.jpg)  
C   
Supplementary Fig. 6 | Demonstration of massively parallel identification of multiple frequencies based on a 32×32 memristive crossbar array. a, The timedomain signal to be input into each row of the crossbar array. b, The experimental conductance matrix mapped into the memristive crossbar array. The odd and even columns are used to identify the in-phase and quadrature components of the $\mathrm { n ^ { t h } }$ frequency channel, respectively. c, Experimental outputs identify the phase and amplitude of different frequencies.

![](images/d1c26183536d003ef6983046d9689549e96f57863adb45dcf5bd62a9c272f3ae.jpg)

![](images/ebb8dce6561af8bc75af28d4be3c0f50200bb73e60cb5266fc64bc0a766a348a.jpg)  
b   
Supplementary Fig. 7 | Demonstration of real-time wireless transmission and reception of recognition results by FMC system. a, The recognition results (represented by 16 frequency components) in the FMC system are transmitted by a RF module, which contains amplifiers, up-converter (with fLO as local oscillator frequency) and antenna, and received by a mobile phone over wireless channel. In the mobile phone, the received radio frequency signal is transformed into baseband signal through down-converter and converted to digital signal through analog-to-digital converter. b, Up-converter in RF module shown in (a) can be removed when carrier frequency band in FMC matches with that of wireless communication system.

![](images/805224902ce9a68ec051ed472309d56a465989b8b071b09f099e03aedea373ed.jpg)  
Supplementary Fig. 8 | The simulated channel capacity of a MIMO system as a function of the number of transmitting/receiving antennas for the number of subcarriers. The simulation indicates that transmission rate of the FMC system can be further improved with MIMO technology and the number of frequency components used in FMC system.

![](images/784ab1f97d044345abbbc89fe5ede5db0adfa98c7cfae9c347fbb272a062c9b0.jpg)

![](images/0d21bf964e712de2a3cf5e755e5055e07d26f14ea5a0314e6c4e326fc99f6925.jpg)

![](images/7dd47b119282c378048e91eefd9e2ac7d4a54590813648b9c7ff38f904313691.jpg)

![](images/762f2d4318721ec59fb5bffa59724b5a814c5547570cf3ecbdc1827019cbfe97.jpg)

![](images/8d611bbc5ba749af41604fed314a829f7003a84be593938dcdb5569272051cd8.jpg)

![](images/af3683589686aa8607edd11f7902f9620b1fb7a164e5403f3d77190ccceee1dd.jpg)

![](images/bc2f43eaceec8166ae61a3f50c7fc413a855e44d285023a6c3c34974ddfee949.jpg)

![](images/944239c6202c8a7a7aa20f2239c4bcc899d6bd57d8d4185b5139bfe51a7679ce.jpg)  
Supplementary Fig. 9 | Analysis of parallel reading error at different voltages. a, The measured output current vs conductance in memristive crossbar array for different U0 =1 mV to 100 mV. b-h, The parallel reading errors at different U0.

![](images/fbce705538ef97e9b092038b4195ccece45b801ed3ddd4d817c6384b66f9c11d.jpg)

![](images/2cb5517432053e4e7c6b421b6720674c4ef48f48de1b8c1dd6949b04069c166c.jpg)

![](images/5a251792812e342ebb7b32b5075984f877e0de58168e85d4b0001086e7ae6961.jpg)

![](images/ee075358f06fcfa1fe61b133dd1d8252cf52265781c0a880f5cf16e0be08db26.jpg)  
Supplementary Fig. 10 | Noise analysis at different operating voltages. a, Harmonic distortion is absent in output signal for low operating voltages, i.e. U0=1 mV. Further increasing the operating voltage results in the presence of harmonic distortion in output signals, as shown in the shaded areas of b and c. d, The harmonic distortion is attributed to the high operating voltage induced nonlinearity I-V characteristics. In addition to harmonic distortion, the high operating voltage also induces conductance variation.

![](images/6f81086b2ee44319fca2db763f8d4ef8b20d960e26c0b9d56aaad60fb45e05db.jpg)

![](images/0f387dc5a0e21762411a0addf9c046c63ff30a41a5df1cdfe3a7a62aa99823a2.jpg)  
Supplementary Fig. 11 | Comparison of measured and simulated S21. a, The measured S21 on a 0.16 μm2 memristor for different resistive states and the inset shows corresponding measurement circuit. b, An equivalent circuit model (inset) can be developed to simulate the experimentally measured S21 by modeling memristor as a variable resistor connected with a capacitor in parallel. Fitting the measured result with the simulation model gives rise to a capacitance of about 20 fF.

![](images/ebfd2f9fc2114d4e194f57caaa8f716f0aae4966dd6b5189ef09bedb71b03e2c.jpg)

![](images/389e361d823d59819bddc4a216b60c4f07d42f28dc32b0e6414f007a9a94a303.jpg)

![](images/e8d5ac305008acf8e941cc580b80c040cbf7c505facfab45ec617f32cdbbed5d.jpg)

![](images/9ce0b74615a9d108de705864ffe05fe7495ddbc8dc3d7e2827608debbc025673.jpg)  
Supplementary Fig. 12 | Performance of tiled crossbars. a, Experimental demonstration of FMC using 4-layer tiled crossbars. b, Experimental outputs show good agreement with the expected results. c, Error statistics versus crossbar array size. 4-layer tiled crossbars were used in the simulations. d, Error statistics versus number of tiled crossbars. 64×64 crossbar arrays were used in the simulations.

![](images/06feaf5912a129bffc3c36e8c942322ebe08aacc1c094be1d86ac4bb2a1d71be.jpg)

![](images/5d4f641a5ad84de38500d12e214f6d90459f4c14f172fe83313213498aa13062.jpg)

![](images/d8466ffb4c8e75d66c15019903720cd3c1f231aa516e28e57359d72966bb66ba.jpg)

![](images/bcd02d39c0a0deccc5a73119459d538e7ee4dbb50d9e9ff46acdebf795e9383a.jpg)  
Supplementary Fig. 13 | Performance of FMC based on memristors with high resistance values. a, The relative error is evaluated at various voltage amplitudes $\left( \operatorname { U } _ { 0 } \right)$ of the carrier signals. The resistance range in the experiment is from 3k to 500k Ω. b, Noise spectrum measured for the memristive device. The dashed red line is used to indicate the trend of noise suppression with increasing operating frequency. c, The simulated Scattering-parameter S21 of the memristive device. d, The calculated operating frequency of the FMC-based massively parallel computing based on memristors resistance ranging from 3k to 500k Ω.

![](images/d9358ca2d1f1e06c198ee318c29ceafb0f809dbaec6b8f46890d3318a0327baf.jpg)  
a

$$
R _ {\text {w i r e}} = \rho_ {\text {m e t a l}} L / W H = 2 \rho_ {\text {m e t a l}} / H
$$

![](images/2aa2fac8987de7ed1ac521f0896e5e337570dbb8fd9d080c1ff04f8a17dc3d9a.jpg)  
b   
Supplementary Fig. 14 | Resistance and capacitance associated with the wires in memristive crossbars. a, Wires resistance calculation based on $4 \mathrm { F } ^ { 2 }$ memristor cell. b, The complex impedanceac that determines the crosstalk of two wires adjacent is far larger than impedanceab, indicating a negligible crosstalk effect. Therefore, the accuracy of FMC is mainly dominated by the parasitic effect of the memristive devices.

![](images/62d2749cc861cbfb3b980b2e80b7b7d54c7c20978599bea054862b661969b51a.jpg)  
a

![](images/304af2c4b32444b2a7bb1e46b209bfc207fa2f82075c1f2e7e4d4f7b898b0ab5.jpg)  
b

![](images/869c7d52aa06bf7edf0394b33f7cafffe8ab12970ce288aabf35d228a57ae4c5.jpg)  
Supplementary Fig. 15 | Error statistics for different memristor device feature sizes by simulation. a, Scaling down memristor can dramatically decrease parasitic capacitance in memristor1-3 . b, Error statistics (standard deviation and mean) vs. operating frequency for different memristor device feature sizes.

![](images/bd9e3a6a74e23d1b85c7bfad53298e55fd8cf11af41f67ad0bb8dcd71a769642.jpg)  
a

![](images/68afc8aa9093ba98e7c6f09ef7666614b2505a9769ad3e634323acd4b1010577.jpg)  
b

![](images/6810e0d3653c042494909f5c4ba10568a155ff8b353f160930906dbb03cddb1b.jpg)  
Supplementary Fig. 16 | Error statistics vs. operating frequency of FMC by simulation. a, The circuit diagram using the differential scheme. Via this scheme, we can eliminate the undesired current components from the parasitic capacitors, and significantly increase the cut-off operating frequency of FMC without losing computing accuracy. b, The mean and standard deviation of error vs. the operating frequency of FMC, with and without adopting the differential scheme. The simulation was carried out based on the measured 20 fF memristor capacitance with 5% capacitance fluctuation.

![](images/4a5a795b3583492db4730f42f4c783455f6319ee4fbd295bbfc4939de15c063b.jpg)  
Supplementary Fig. 17 | Alternating inputs over different time frames in memristive crossbars.

![](images/14a1d614b978ab44a203ab826bb4d6d9c9be70fed8492e77acb6e41ff17a8880.jpg)  
Supplementary Fig. 18 | Peripheral circuitry of the proposed FMC. The circuits in the dashed box are involved when the FMC is used as MAC accelerator.

Supplementary Table 1 | Comparison between photonic WDM and electrical FMC   

<table><tr><td></td><td>Photonic WDM (from the literature4)</td><td>Electrical FMC (in this work)</td></tr><tr><td>Computing hardware</td><td>Interconnected waveguides coupled with phase-change materials</td><td>Memristor crossbar array</td></tr><tr><td>Limitation in scaling-down</td><td>~μm (limited by optical diffraction limit)</td><td>~nm (limited by filament size in memristor)</td></tr><tr><td>Size of integrated array</td><td>small</td><td>large</td></tr><tr><td>Parallelization approach</td><td>Wavelength division multiplexing</td><td>Frequency division multiplexing</td></tr><tr><td>Multiplexing and demultiplexing hardware</td><td>Fiber-based wavelength division multiplexers and wavelengths de-multiplexers</td><td>Memristor crossbar array and CMOS circuits</td></tr><tr><td>Modulation and demodulation hardware</td><td>Electro-optic modulators and photodetectors</td><td>Memristor crossbar array and CMOS circuits</td></tr><tr><td>Mechanism for multiplication</td><td>Employing tunable transmission through phase-change materials</td><td>Using Ohm&#x27;s law in the memristor</td></tr><tr><td>Mechanism for accumulation</td><td>Accumulating light intensity at photodetectors</td><td>Accumulating current at crossbar electrodes</td></tr><tr><td>Limitation in operational bandwidth</td><td>Range of frequency comb</td><td>Parasitic effect in memristor</td></tr><tr><td>Modulation speed</td><td>~20 GHz</td><td>~1 GHz</td></tr><tr><td>Number of parallel MVM operations in a single time step (for multiplexed wavelengths/frequencies)</td><td>Number of multiplexed wavelengths rows number of input waveguides</td><td>Number of multiplexed frequencies</td></tr><tr><td>Whether the approach supports cascading architectures?</td><td>No</td><td>Yes</td></tr></table>

Supplementary Table 2 | Comparison between anticipated capabilities of photonic WDM and electrical FMC   

<table><tr><td></td><td>Photonic WDM (literature4)</td><td>Electrical FMC (our work)</td></tr><tr><td>Array size</td><td>50×50</td><td>512 × 512 [a]</td></tr><tr><td>Cell area</td><td>30 μm×30 μm</td><td>Below 2 μm×1.5 μm [a] (minimum 12 nm × 12 nm [b])</td></tr><tr><td>Modulation speed</td><td>50 GHz</td><td>1 GHz [c]</td></tr><tr><td>Operational bandwidth</td><td>~ 20 THz</td><td>50 GHz [d]</td></tr><tr><td>Number of multiplexed wavelengths/frequencies</td><td>400</td><td>50</td></tr><tr><td>Number of parallel MVM operations in a single time step</td><td>400 / 50 = 8</td><td>50</td></tr><tr><td>Multiply-accumulate (MAC) operations per second</td><td>50 G × 8 × 50 × 50 = 1 POPs</td><td>1G × 50 × 512 × 512 = 13 POPs</td></tr></table>

[a] 512 × 512 crossbar array has been integrated on a 6 mm2 chip with cell area below 2 μm×1.5 μm, reported in the literature5 .   
[b] The literature6 reports minimum memristor crossbar arrays with 12-nm pitch and 2- nm feature dimension of the individual device (cell area: 12 nm × 12 nm).   
[c] The speed of modulator and demodulator based on CMOS technology can be beyond tens of $\mathrm { G H z } ^ { 7 } .$ . In our work, the modulation is realized by using the memristive crossbar arrays, as shown in the Supplementary Fig. 17. Note that alternating speed of different symbols over time frames is determined by switching speed of the transistors. Therefore, we conservatively list 1 GHz modulation speed limit adopted for FMC.   
[d] The operational bandwidth is fundamentally limited by parasitic capacitance of unit device. The literature reports fabrication of memristors with minimum 0.44 fF capacitance3 , which allows 200 GHz maximum operable bandwidth in FMC. In practice, here we list 50 GHz considering a cell of 126 nm × 126 nm with ~ 2 fF capacitance.

Supplementary Table 3 | Components of circuitry   

<table><tr><td></td><td>Circuit diagram</td><td>Layout drawing</td><td>Area (μm2)</td><td>Power consumption (μW)</td><td>CMOS technology node (nm)</td></tr><tr><td>Carrier sources</td><td></td><td></td><td>22×34</td><td>0.6</td><td>65</td></tr><tr><td>Transimpedance amplifiers</td><td></td><td></td><td>46×20</td><td>61</td><td>65</td></tr><tr><td>Demodulator</td><td></td><td></td><td>23×38</td><td>250</td><td>65</td></tr><tr><td>Memristor crossbar array*</td><td></td><td></td><td>320×320</td><td>328</td><td>-</td></tr><tr><td>Analog-to-Digital converter8</td><td>NOT AVAILABLE</td><td></td><td>22×70</td><td>3100</td><td>32</td></tr></table>

*demonstrated in this work

# Reference

1 Pi, S. et al. Nanoscale memristive radiofrequency switches. Nat. Commun. 6, 7519 (2015).   
2 A. C. Torrezan et al. Sub-nanosecond switching of a tantalum oxide memristor Nanotechnology 22 485203 (2011)   
3 Kim, M. et al. Analogue switches made from boron nitride monolayers for application in 5G and terahertz communication systems. Nat. Electron. 3, 479– 485 (2020).   
4 Feldmann, J. et al. Parallel convolutional processing using an integrated photonic tensor core. Nature 589, 52–58 (2021).   
5 Xue, CX. et al. A CMOS-integrated compute-in-memory macro based on resistive random-access memory for AI edge devices. Nat Electron 4, 81–90 (2021).   
6 Pi, S., Li, C., Jiang, H. et al. Memristor crossbar arrays with 6-nm half-pitch and 2-nm critical dimension. Nat Nanotech 14, 35–39 (2019).   
7 M. Elkhouly, et. al, A 245 GHz ASK modulator and demodulator with 40 Gbits/sec data rate in 0.13 μm SiGe BiCMOS technology 2013 IEEE MTT-S International Microwave Symposium Digest, 1-3 (2013)   
8 Kull, L. et al. A 3.1 mW 8b 1.2 GS/s single-channel asynchronous SAR ADC with alternate comparators for enhanced speed in 32 nm digital SOI CMOS. IEEE J. Solid-State Circuits 48, 3049–3058 (2013).