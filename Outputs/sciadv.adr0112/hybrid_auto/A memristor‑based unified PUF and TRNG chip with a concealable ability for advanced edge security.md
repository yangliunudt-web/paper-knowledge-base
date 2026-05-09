---
title: "A memristor‑based unified PUF and TRNG chip with a concealable ability for advanced\"
authors:
  - "Xueqi Li"
  - "Bohan Lin"
  - "Bin Gao"
  - "Yuyao Lu"
  - "Siyao Yang"
  - "Zhiqiang Su"
  - "Ting‑Ying Shen"
  - "Jianshi Tang"
  - "He Qian"
  - "Huaqiang Wu"
date: "2025-01-01"
year: "2025"
journal: "Science Advances"
doi: "10.1126/sciadv.adr0112"
abstract: "Security primitives ensure Internet of Things (IoT) security by generating stable\"
abstract_cn: "安全原语通过物理不可克隆函数生成稳定密钥和真随机数发生器生成不可预测比特流来确保物联网安全。考虑到物联网节点资源受限，一个有望的设计趋势是通过共享同一熵源和复用熵提取器来统一\"
keywords:
  - "[[Memristor]]"
  - "[[PUF]]"
  - "[[TRNG]]"
  - "[[IoT security]]"
  - "[[Entropy extractor]]"
cite: "[1] Li X, Lin B, Gao B, et al. A memristor‑based unified PUF and TRNG chip with a\"
aiSum: "基于 28 nm 嵌入式忆阻器的统一 PUF/TRNG 芯片：利用 FORMING 条件变异和读取电流变异作为熵源，设计紧凑熵提取器实现 41.7 Mbps 吞吐量，隐蔽方法防止数据泄露，认证吞吐量比\"
confidence: "high"
wiki_concepts:
  - "[[Memristor]]"
---

# A memristor-based unified PUF and TRNG chip with a concealable ability for advanced edge security

Xueqi Li1 , Bohan Lin1 , Bin Gao1 *, Yuyao Lu1 , Siyao Yang1 , Zhiqiang Su1,2 , Ting-Ying Shen3 , Jianshi Tang1 , He Qian1 , Huaqiang Wu1,4 *

Security primitives ensure Internet of Things (IoT) security by generating stable keys from physically unclonable functions (PUFs) and unpredictable bitstreams from true random number generators (TRNGs). Considering the restricted resources on IoT motes, a promising design trend is to unify PUF and TRNG by sharing the same entropy source and multiplexing entropy extractor. Here, we report a unified PUF and TRNG chip based on a 28-nanometer embedded memristor with concealable ability. We use the memristor intrinsic FORMING condition variation and read current variation as entropy sources and design a compact on-chip entropy extractor that achieves a high throughput of 41.7 megabits per second with minimal area overhead of 0.291 MF2 . To prevent PUF data leakage, we developed a concealment method, protecting data when idle and enabling recovery upon demand. Comprehensive testing shows the chip has excellent performance in randomness, reliability, lifetime, and stability, achieving a 3.82-fold throughput improvement over complementary metal-oxide semiconductor–based designs in authentication tasks.

Copyright © 2025 The

Authors, some rights

reserved; exclusive

licensee American

Association for the

Advancement of

Science. No claim to

original U.S.

Government Works.

Distributed under a

Creative Commons

Attribution

NonCommercial

License 4.0 (CC BY-­NC ).

# INTRODUCTION

The rapid growth of the Internet of Things (IoT) industry has led to the widespread use of billions of electronic devices in our daily life, which, along with its benefits, raises notable security concerns. Issues such as identity cloning, unauthorized remote access, and data theft have become commonplace (1, 2). More seriously, the high interconnectivity between IoT devices further intensifies the security problem, as an attacked device can serve as a gateway to attack other devices within the network, thus exacerbating the overall vulnerability of the IoT ecosystem. Therefore, there is an increasing demand for hardware-level security for IoT devices. A physically unclonable function (PUF) (3–5) and true random number generator (TRNG) (6) are the fundamental security primitives. They are the root of trust in infrastructure such as digital signatures, identity authentication, and cryptographic processes. PUFs use the inherent physical unpredictability of hardware, such as device-to-device variation or intra/interdie process variation, to generate a unique and unpredictable “fingerprint” (7–11). This “fingerprint” varies across device but remains stable throughout the lifetime of the same device, hence the term static entropy. PUF is usually applied in device authentication and cryptographic key generation (12–14). In contrast, TRNG uses unpredictable physical processes such as thermal noise to generate true random bitstreams. These bitstreams are device independent and time varying, hence the term dynamic entropy. In security protocols, these bitstreams can be used as nonce, initialization vectors, random salts, etc.

In the IoT ecosystem, edge devices are operating under limited area constraints and power budgets, so area and energy efficiency are crucial for implementing hardware security primitives. In this context, a unified PUF and TRNG design is considered as a promising

solution to maximize on-chip resource utilization, avoid excessive logic overhead, and save notable area (15–21). Both PUF and TRNG designs consist of an entropy source and an entropy extraction circuit, where the entropy source generates static and dynamic randomness, respectively, and the entropy extraction circuit extracts the randomness and outputs 0/1 bitstreams. In a unified chip, the PUF and TRNG designs share the same entropy source and multiplex the entropy extraction circuits, which can be flexibly configured in TRNG or PUF mode. Ideally, the TRNG and PUF output should exhibit balanced performance (e.g., throughput), enabling their joint participation in security tasks such as authentication or encryption and decryption (Fig. 1A).

However, implementing such a unified PUF and TRNG is challenging. Such a unified design requires the entropy source to have at least two independent, uncorrelated, and noninteracting random properties and requires the design of lightweight, reusable entropy extraction circuits. In recent years, several complementary metaloxide semiconductor (CMOS)–based unified PUF and TRNG designs have been proposed (15–20). However, CMOS circuits exhibit limited variety and relatively weak stochastic properties (e.g., thermal noise and transistor mismatches) and face the problems of temperature and voltage sensitivity, strong correlation between entropy sources, and circuit aging degradation. Thus, the CMOS-based unified designs often perform poorly in either PUF, TRNG, or both aspects. Moreover, the entropy extraction circuit of CMOS unified designs can rarely be fully reused, and it often requires the usage of error correction and postprocessing circuits to enhance the quality of PUF and TRNG, which further diminishes the area and power advantage of unified designs. Memristors are an emerging type of memory that exhibits rich and notable random characteristics, making them a highly promising entropy source. Many research studies have proposed different methods to implement memristorbased PUF or TRNG (10, 12). However, research for unified PUF and TRNG is still very preliminary, limited to array testing and simulation, and the performance is inferior to that of CMOS designs (21). In summary, it is challenging for traditional technology to generate high-quality, high-throughput PUF and TRNG bitstream to

![](images/99dd252e9c1b2a2ca59bb779133cd76121b7d93459607fd19fdb24fe2f8af00f.jpg)  
A

![](images/2198c2d20b9d340076a8eaeecbb911db9ca7fb40ef21c9f7716cb7c109a2ee40.jpg)

![](images/db6fd34a62feb9c5b79719c241e459b25ba2853ceedea91a2c2c0aafe17a1e69.jpg)  
C   
D

![](images/7ba1c09ec57fd9f23f3c83eb772166969207ba56d449394d63c532f8e91ad24b.jpg)  
Fig. 1. Unified PUF and TRNG chip based on memristor. (A) The unified chip can generate a TRNG and PUF response for multiple applications, such as privacy-preserving mutual authentication protocol, data encryption and decryption, etc. (B) The “conceal” operation makes the original 0/1 PUF bit into all 1 or all 0. At this point, the PUF value obtained by an attacker through physical attack is incorrect, which ensures the security of the PUF. (C) Overall structure of the memristor-based unified PUF and TRNG chip. (D) Photography of the hardware test platform, the optical microscopy image of the chip with an on-chip memristor entropy source array and unified entropy extractor, and the transmission electron microscopy (TE M) image of 28-nm memristor devices. PCB, printed circuit board; FPGA, field-programmable gate array; ES, entropy source.

meet the lightweight and high-performance demands for the IoT edge end.

Another security challenge for nowadays PUF design is the threat of various attacks. Although PUF has unique and unclonable properties, PUF data are inherently represented by detectable and immutable circuit traits that are physically accessible, posing a potential security risk. Through advanced microprobe attacks and sophisticated analysis methods, confidential PUF data can be stolen. Therefore, to enhance the security of PUFs, it is crucial to implement PUF circuits that are resistant to physical attacks. A possible solution is to implement a process that “conceals” PUF data when idle and “recovers” it upon demand (22). In this way, an attacker cannot physically access dormant PUF data, thus enhancing the security of the PUF (Fig. 1B).

Here, we report a unified PUF and TRNG chip based on a 28-nm embedded memristor with a concealable ability (Fig. 1C). The unified chip consists of a 16–kilobit (kb) memristor entropy source array, a unified entropy extractor, and a two-to-one multiplexer to generate PUF and TRNG bits end to end (Fig. 1D). The generated PUFs are weak PUFs, and the chip is capable of producing a total of 512 128-bit challenge-response pairs (CRPs). The memristor intrinsic FORMING condition variation serves as the static entropy source, while the memristor read current variation serves as the dynamic entropy source. These two entropy sources are independent and uncorrelated. The proposed chip avoids the need for large-area and power-consuming circuit components such as analog-to-digital converters and postprocessing circuits and reaches a minimal area

overhead of 0.291 ${ \mathrm { M F } } ^ { 2 }$ for the unified entropy extractor. In addition, to address the side-channel leakage for PUF, we demonstrate a chiplevel implementation of PUF concealment and recovery, achieving a hiding rate up to 40% and a recovery error rate as low as 0.46%. Last, we test the quality of the PUF and TRNG, including randomness, reliability, uniqueness, etc. We also test the performance of the chip, including throughput, lifetime, and robustness over a wide temperature range and supply voltage variations. Compared to previous works, our proposed memristor-based unified PUF and TRNG chip demonstrates excellent and balanced PUF and TRNG performance, achieving a 3.82× throughput improvement in authentication security tasks.

# RESULTS

# Unified PUF and TRNG design

In our paper, the static entropy for PUF comes from the FORMING speed and FORMING voltage variation between the memristor device (fig. S1). The FORMING process of the memristor involves the generation, migration, and aggregation of oxygen vacancies $\mathrm { ( V _ { o } ) }$ to form conductive filaments (23, 24). The microscopic process of $\mathrm { V _ { o } }$ formation or migration essentially involves the oxygen ions surmounting the energy barrier with the help of random fluctuating thermal kinetic energy. Thus, even for two devices with identical configuration and identical FORMING condition, the time and position of the initial $\mathrm { V _ { o } }$ formation or migration event could be different. Furthermore, in the FORMING pulse sequence, the different

$\mathrm { V _ { o } }$ distributions resulting from the previous pulse can cause a divergent interdevice local electric field and temperature distribution during the next forming pulse, further amplifying the divergence of the filament growth process (25–27). Dynamic entropy for TRNG comes from the relatively large read current variation of the memristor device (fig. S2), which is caused by random telegraph noise, thermal noise, etc., with the amplitude of the random telegraph noise being usually the largest (28). The defects or impurities in the device materials create energy wells where electrons can become temporarily trapped. The random electron transitions between trapped and detrapped states lead to discrete changes in the resistance state of the memristor, which appears as read current variation between cycles (29, 30).

The overall architecture of the unified chip is shown in Fig. 2A, which is consisted of a 16-kb, 28-nm two-transistor-two-resistor (2T2R) memristor crossbar array with 256 rows and 64 columns as the entropy source, a unified entropy extractor, bit line (BL)/source line (SL)/word line (WL) drivers, and logic controllers. The details of the memristor device are shown in the “Memristor device” section. The memristor array is divided into the top part and the bottom part, with the two 1T1R parts of the 2T2R cell positioned

symmetrically to minimize the impact of process variations and routing mismatches on the performance of the PUF. The unified entropy extractor is directly connected to the 2T2R cell and digitizes the randomness in the entropy source to output PUF or TRNG bitstreams. The drivers and controllers can be configured for 2T2R PUF/TRNG mode or can be configured to perform FORMING, SET, and RESET operations separately for each 1T1R part in the 2T2R cell (fig. S3A).

The design of the unified entropy extraction circuit is important for the performance of the chip, as shown in Fig. 2B. The unified entropy extraction circuit consists of a capacitor, a dynamic comparator, a delay buffer, a third-order ring oscillator, a D-flip-flop, and a multiplexer. In PUF mode, a competing FORMING method is adopted to generate PUF bits. In the competing FORMING method, stepped FORMING voltage is simultaneously applied to the paired memristor in the 2T2R cell until one of them is successfully formed, remaining the other one unformed. The voltage condition is shown in the “Operation condition details” section. Because of the high variability of FORMING conditions, combined with the fact that the first successfully formed device in the 2T2R cell draws more current and therefore hinders the FORMING of the other device,

![](images/fc7ffd2981c5a88bf1c4dd887b076fd0d87a23214dd144ac0a97d46d12b3a7a2.jpg)  
A

![](images/570acb341c985635b63a5dc5f79ab6dbba7188c0be7dd88b14baf2670a2981bf.jpg)

![](images/0383fe6d14b2aa19fac49d57390c4b50e44f718bec5eaa3c2f8274fae0a2f6ff.jpg)  
C

![](images/150b35cd9c66929c0f068a1c849a8e107239c519b8ab71140ac43c73e3413ca1.jpg)

![](images/40d0aa6a5b332391bfde814ccc846ca97a3846491c384130675c9bab51406207.jpg)  
D

![](images/453b3a6485c7bc0581b91edc1def749ef94ddad8ad82f9c61031b8fc22a0b6e2.jpg)  
E

![](images/8538b25f314d4751fa9f10d2a374b5541bccda62025186e7a6148dd3bc503ffa.jpg)  
F

![](images/947d77e0b6968f43935d8b824a569112cf8302711cbcdb5298fe68f72febe11e.jpg)  
n overflow of the chip. (A) Overview of the architecture of the chip. (B) Schematic of unified entropy extractor. The thresholds of the dynamic comparator and k2 ⋅ $V _ { R E A D }$ for PUF and TRNG mode, respectively. (C) Working principle and measured waveform of PUF and TRNG, taking the PUF and TRNG output bit “1” e. (D) Chip layout where the unified extractor and entropy source array are labeled. The unlabeled portion are the drivers and control circuits. (E) Flowchart and recovering PUF bits. (F) Working principle and measured waveform of concealing and recovering PUF bit. The initial PUF bit is “1.” (G) Measurement initial PUF, concealed PUF, recovered PUF, and error bits of recovered PUF, with BER reaching 0.46%. (H) Measured BER of concealed and recovered PUF bits

the probability of both devices being simultaneously formed can be controlled to be as low as <0.1%. The PUF output is determined to be 0/1 by comparing the resistance of the paired memristor (fig. S4A). To extract this static randomness, read voltage $( V _ { \mathrm { R E A D } } )$ is applied to the top memristor $R _ { 1 } ,$ and the bottom memristor $R _ { 2 }$ is connected to the ground. The PUF bit is derived by comparing the voltage divided by the paired resistance with a $k _ { 1 } \cdot V _ { \mathrm { R E A D } }$ threshold via the dynamic comparator. The PUF value is defined as follows

$$
O _ {\mathrm {P U F}} = \left\{ \begin{array}{l l} 0 & k _ {1} R _ {1} > (1 - k _ {1}) R _ {2} \\ 1 & k _ {1} R _ {1} <   (1 - k _ {1}) R _ {2} \end{array} \right.
$$

In TRNG mode, the read current of the memristor device is emphasized by charging the loaded capacitance Cap through the 2T2R cell (fig. S4B). In this case, the threshold of the dynamic comparator is $k _ { 2 } \cdot V _ { \mathrm { R E A D } } .$ The two memristor cells are both connected to $V _ { \mathrm { R E A D } } ,$ and the read current variation leads to a variation in charging time $T _ { \mathrm { C } }$

$$
T _ {\mathrm {C}} = \left(R _ {1} + R _ {2}\right) \cdot \mathrm {C a p} \cdot \ln \left(\frac {1}{1 - k _ {2}}\right)
$$

The three-invertor ring oscillator with period $T _ { \mathrm { R O } }$ is used to digitize $T _ { \mathrm { { C } } } .$ Once the charging process is completed, the ring oscillator is disabled, and its current state is latched, sampled, and output as a TRNG bit

$$
T _ {\mathrm {C}} = N \cdot T _ {\mathrm {R O}} + \delta , N \text {i s a n i n t e g e r}
$$

$$
O _ {\mathrm {T R N G}} = \left\{ \begin{array}{l l} 0 & \delta <   0. 5 T _ {\mathrm {R O}} \\ 1 & \delta > 0. 5 T _ {\mathrm {R O}} \end{array} \right.
$$

The measured waveforms of TRNG and PUF are shown in Fig. 2C. Both TRNG and PUF can obtain correct outputs within 100 ns, which means that a single entropy extractor can achieve above 10–megabits per second (Mbps) throughput. Besides, with highly multiplexing design and several layout and circuit optimization techniques, such as a low-power dynamic comparator, currentstarved structure ring oscillator, etc. (“Entropy extractor design details” section and fig. S3, B to G), the extractor generates PUF and TRNG bits at a minimum 291,000 F2 area overhead, as shown in Fig. 2D. No additional postprocessing circuits are needed. Overall, the memristor-based unified PUF and TRNG chip is designed with high area efficiency and high throughput, making it particularly suitable for IoT applications.

# Concealable ability

The resistive switching characteristic of the memristor is based on the conductive filaments. When the device is initially fabricated, the conductive filaments do not exist, leading to high resistance. After a FORMING operation, the conductive filaments are formed, and the device resistance can then be continuously modulated. A RESET operation ruptures the filaments by applying a reverse voltage pulse, increasing the resistance. Conversely, a SET operation reconnects the filaments by applying a positive voltage pulse, decreasing the resistance. In our design, the PUF value is determined by the different formed/unformed states of the top and bottom devices in the 2T2R cell. For a formed device, the conductive filaments and the device resistance will be modulated by SET/RESET; however, for an

unformed device where filaments do not exist, its resistance is not affected by SET/RESET operation, always remaining high. Leveraging this physical property of the memristor, we design a PUF concealment and recovery method and implement it on the unified chip.

The operation principle of concealing and recovering PUF bits is shown in Fig. 2 (E and F). At the very beginning, the paired memristor cell with $R _ { 1 }$ in a low-resistance state (~10 kilohm) and $R _ { 2 }$ in an unformed state (~1 megohm) will output PUF = 1 through the comparator. To conceal the PUF bit, we perform RESET operation on the whole array; the operation condition is shown in the “Operation condition details” section. The memristor cell $R _ { \mathrm { 1 } } ,$ which is originally in a low-resistance state, switches to a high-resistance state (~300 kilohm), and the memristor cell $R _ { 2 } ,$ which is originally in an unformed state, remains high. In this way, the resistor difference between the two paired devices becomes smaller. By setting an appropriate reference voltage $k _ { 1 } \cdot V _ { \mathrm { R E A D } }$ (typical value $\dot { k _ { 1 } } = 0 . 8 \dot { ) }$ , the PUF output fetched by the comparator of the whole chip will be $^ { \alpha } 0 . ^ { \gamma }$ This is the working principle of concealing the PUF bits. Similarly, to recover the PUF bits, we perform SET operation on the whole array; the operation condition is shown in the “Operation condition details” section. The memristor cell, which is RESET to a high-resistance state, returns to low, while the memristor cell, which is originally in an unformed state, remains high, because the SET operation condition is much weaker than the FORMING operation condition. In this way, the resistor difference between the two paired devices becomes larger and can be read out by the comparator.

We implement the concealment method on the unified PUF and TRNG chip. Figure 2F shows the measured waveforms of concealed PUF and recovered PUF, confirming the effectiveness of this method. The measurement results of the 8000-bit PUF data for half of the chip are depicted in Fig. 2G. The bitmaps indicate that the PUF value can be well concealed and correctly recovered with only a minimal number of errors bits. Figure 2H illustrates the bit error rates (BERs) of PUF data over 100 cycles of concealment and recovery. The BER of concealed PUF exceeds 40.51% (the ideal value is 50%), and the BER of recovered PUF is less than 0.46% (the ideal value is 0%). These results indicate that the chip can effectively execute the concealment function.

# PUF and TRNG performance

In our design, the PUF and TRNG performance is influenced by the reference voltage $k \cdot V _ { \mathrm { R E A D } } .$ . For TRNG, a higher k value leads to lower throughput but better randomness, and for PUF, higher k results in a better concealment effect but worsens the recovered BER. Therefore, we develop a dynamically adjustable reference circuit (Fig. 3A) that optimizes the performance of PUF and TRNG by automatically adjusting to the best k value. In this circuit, the 0/1 accumulator counts the output of PUF or TRNG over a specific period and compares it with the expected value to dynamically finetune the digital-to-analog converter output. With the abovementioned technique, the overall performance of PUF and TRNG is improved. Furthermore, this technique also helps to mitigate the offset and mismatch issues between dynamic comparators across different chips. By fine-tuning the digital-to-analog converter output on the basis of real-time performance feedback, it ensures optimal reference voltage for each comparator, ensuring consistent performance across chips and environmental conditions.

For the PUF performance evaluation, 200 by 256–bit PUF data are generated across 10 random selected chips at 25°C under 0.9-V

![](images/6cbc83c814f087cac59c3f8058bd9bfb1537b1e0f09e5e7934fbe3617b19e3eb.jpg)  
A

![](images/6e5ec98b528f9865d32918e83afc79aedfe2f728392ce11e7d72b966588f2cb0.jpg)  
B

![](images/94d2dd034ab2ab9f7a39ce90968b088d2794c9f9744f2e4cad78f4fd36980113.jpg)  
C

![](images/d0df6775d4576059485e2fb61b036a625fccd7f6b92ace1fe1b2c1aa7871b3e2.jpg)  
D

![](images/f6e3fa68a28c33ec7b7d1272d7964ea50fd2594ef4c309e49ac3e70ebe98b3ea.jpg)  
E

![](images/bea5b6e4af7a09d099cf0e418f963de90f1fc541f08c8b5472c41e21daaba35b.jpg)  
F

![](images/754ade4e050ed76045c22475bd0f97e40ccc528d61691885a5c7932a18fa7dfb.jpg)  
G

![](images/4768e64acbf5fdb778a112277490d3c3e6d31e0858526b265083d58961db2216.jpg)  
H

![](images/6ac966307b137257ae9d000104aa0065cffe5833b2f975d060912edc5e85fecd.jpg)  
1

![](images/cd6d8b4f7bae790f305132407ae6a0fbc3827215710eb1e62db9344033d26a4e.jpg)  
Fig. 3. Performance of PUF and TRNG. (A) Architecture of dynamic adjustable reference. (B) NI ST SP800-22 test results of PUF and TRNG. (C to F) Uniformity, diffuseness, autocorrelation function (ACF), uniqueness, and reliability of PUF bits. a.u., arbitrary units. (G to I) Uniformity, min-entropy, and autocorrelation function of TRNG bits. (J) “Yield” test of TRNG entropy sources. Randomly selected 1000/16,000 TRNG entropy sources on one chip are tested.

VDD, where VDD refers to the power supply voltage. The evaluation metrics include randomness, uniformity, diffuseness, uniqueness, and reliability (specific definitional formulas are shown in the “PUF and TRNG performance definition” section). Uniformity, assessed by Hamming weight, is defined as the proportion of “1”s in the PUF responses, ideally 50%. The average value of Hamming weight of 256-bit fingerprint data generated by different chips is $5 0 . { \overset { \circ } { 0 } } 9 \pm 0 . 2 5 \%$ (Fig. 3C). Diffuseness measures the difference in responses of the same PUF to different challenges and is mainly used to assess whether there is a correlation between different CRPs of the same PUF, with an ideal value of 50%. The average value of Hamming distance between 256-bit fingerprint data generated by the same chip is $4 9 . 9 1 \pm 6 . 7 1 \%$ . Uniqueness, evaluated by inter-chip Hamming distance, measures the difference in responses between two distinct PUFs under the same challenges, also ideally 50%. The average value of interchip Hamming distance of our chip is $5 0 . 0 6 \pm 6 . 4 5 \%$ (Fig. 3F). Reliability refers to the ability of a PUF to reproduce the same response multiple times under the same challenges. This attribute is primarily evaluated using the intrachip Hamming distance or BER,

with an ideal value of 0%. The average value of intrachip Hamming distance of our chip is 0.00%, with no bit error (Fig. 3F). For randomness, Fig. 3E shows the results of the autocorrelation test; the 95% confidence interval is ±0.0079 (Fig. 3E). Besides, we conducted NIST SP800-22 randomness tests on the PUF data (31). The lowest pass rate for the 62 by 1024–bit fingerprint data in the various NIST SP800-22 test items was 96.77% (fig. S5), with an average P value of 0.5678 (accept value >0.1) (Fig. 3B). These NIST test results demonstrate that the PUF has excellent statistical randomness.

For TRNG performance evaluation, 200 entropy sources from 10 random selected chips are tested at 25°C under 0.9-V VDD, and 100-kb true random numbers are generated using those entropy sources. We measured the uniformity, minimum entropy, and randomness of TRNG, which are the basic evaluation metrics (specific definitional formulas are shown in the “PUF and TRNG performance definition” section). Figure 3G shows that the average value of the proportion of “1”s generated by 20 entropy sources is $4 9 . 9 9 \pm 0 . 1 0 \%$ (ideal value 50%). The cryptographic meaning of minimum entropy is the amount of information contained in each bit of data, and the

ideal value is 1. Figure 3H shows the results of the minimum entropy calculation of 200 by 100–kb true random numbers, with the mean value of 0.9893, a variance of 0.0082, and a minimum value of 0.9652. For randomness, Fig. 3I shows the autocorrelation test results of the above true random numbers, with the 95% confidence interval of ±0.000378. Besides, we conducted NIST SP800-22 and SP800-90B randomness tests on the TRNG bits (fig. S5). The lowest pass rate for the 28 by 1–Mb fingerprint data in the various NIST SP800-22 test items was 96.43%, with an average P value of 0.4734 (accept value >0.1) (Fig. 3B). Also, the 1-Mb true random number passes the NIST SP800-90B (32) test, and the minimum entropy is as high as 0.9961. These NIST randomness test results prove that the TRNG has excellent statistical randomness (Fig. 3B). Furthermore, there are 16,000 entropy sources in a chip; to evaluate the “yield” of the entropy sources, we randomly selected 1000 entropy sources and generated 1-kb true random numbers independently from each entropy source for the NIST randomness test. The heatmap shows that 95.4% of the entropy sources can pass the NIST SP800-22 test, indicating that the entropy sources have a high “yield” (Fig. 3J).

# Chip robustness and applications

To validate the practical capabilities of the chip, we evaluate the performance of the chip under thermal extremes, voltage variations, endurance cycling, and high-temperature burn-in tests. The evaluation metrics include the BER and throughput of the PUF, as well as the min-entropy, randomness, and throughput of the TRNG under various conditions. In the power supply voltage tests (Fig. 4A), the chip exhibited maximum throughput when the VDD is 1.0 V, achieving a PUF throughput of 67.6 Mbps with 0% BER and a TRNG throughput of 41.7 Mbps with the min-entropy of NIST SP800-90B test reaching 0.99, less than 1% below optimal. As VDD decreased, the throughput deteriorated. When VDD dropped below 0.9 V, the throughput of PUF and TRNG became very low to keep the PUF BER and TRNG randomness stable; when VDD dropped below 0.8 V, the unified entropy extraction circuit failed to function properly. In the thermal extreme tests (Fig. 4C), the environmental temperature varied from −40° to 125°C. Throughout the entire temperature range, the output PUF data of the chip have no bit error, and the min-entropy of the output true random numbers reaches 0.998, less

![](images/03bf79d7a93d7d5e528c09e25811340deaa2db8e44f81cccbdba74bd00d3ab59.jpg)  
A

![](images/45b1f3c219a2a21f52b410ed48efa42dc95150302bfe7984f09abe744204d823.jpg)  
B

![](images/e2b19462f233b540813e4b66eceb5e0d24c6005b7541b107b7f9d07797ac37a0.jpg)  
C

![](images/3a57252d67e9144a1eff2cffb35916b88ffcb1b7c974e7d5f89af8ba094ea19b.jpg)  
D

![](images/782b7a57fca6fdfebf8841282957299f336ed18dcfe5d2b443fee6142fa9f768.jpg)  
E

![](images/64bd1e2d00c27c7d6c02174570e0fe69f96a22559cc1725294975232d9841ede.jpg)  
F

![](images/6e89d47114a6523f1cbf0587c374df2b9b99e26013b856ab44f757d4c721bcc4.jpg)  
G   
Fig. 4. Chip robustness and applications. (A and C) Throughput and BER of PUF and throughput and min-entropy from the NI ST SP800-90B test of TRNG under voltage variation and temperature variation. (B and D) BER of PUF and min-entropy and average P value of NI ST SP800-22 of TRNG in endurance and burn-in test. (E) Process of basic lightweight authentication protocol. (F) Comparison of PUF performance and TRNG performance for representative work and this work, including PUF-only/TRNGonly design and unified design. (G) Comparison of throughput for this work and digital unified design in the authentication protocol.

than 0.2% below optimal, demonstrating the excellent temperature stability of the chip. In the endurance test (Fig. 4B), the PUF reproduces three types of fingerprint data ${ 1 0 } ^ { 9 }$ times: The worst BERs for concealed, recovered, and no concealment PUF data are 42.27, 0.58, and 0%, showing degradations of 0.54, 0.12, and 0% from the initial operation, respectively. The TRNG uses the same entropy source to generate random numbers over $1 0 ^ { 1 1 }$ cycles, with a minimum entropy exceeding 0.998, and also passed the NIST SP800-22 randomness test. This indicates that the chip demonstrates good endurance performance. In the burn-in test (Fig. 4D), the chips are baked for 30 hours at 125°C. During the baking process, the worst BERs for concealed, recovered, and no concealment PUF data are 40.00, 3.09, and $0 \% ,$ showing degradations of 3.44, 2.63, and 0%, respectively. The randomness of the TRNG is unaffected, with its min-entropy still exceeding 0.998, and it passes the NIST test. In conclusion, our chip works well under varying voltages and a wide temperature range, has a long lifespan, and can endure notable stress. We further analyze the factors affecting the chip robustness, including the circuits and memristor devices, as detailed in the “Performance constraint analysis” section and figs. S8 and S9.

To illustrate the performance of our unified chip in solving real security problems, we present a demonstration showcasing its use in identity authentication. In a basic authentication process, the server sends a “challenge” and the IoT mote replies with a “response,” and then the server checks whether the “response” is correct. To prevent the leakage of CRPs during transmission, which could lead to impersonation, it is necessary to obscure the CRPs transmitted on the channel. Traditional approaches, such as weak PUF  +  encryption and strong PUF schemes, face the problems such as high computational overhead, high storage overhead, and vulnerability to machine learning attacks. A weak PUF + TRNG scheme is a promising solution, whose basic principle is to hide the “responses” of weak PUFs with random numbers generated by TRNG (33, 34), and its protocol is shown in Fig. 4E. The server picks a challenge ci and sends it to the IOT mote, and the IOT mote generates a corresponding response ri. Next, the IOT mote generates a random number xi and sends it to the server. Both the IOT mote and server use a one-way function (such as hash function) to apply the random number xi to ri and get the outcome a and ${ \boldsymbol { a } } ^ { \prime } ,$ respectively. Then, the IOT mote sends outcome a to the server, which verifies the correctness of the result. In the whole process, the IOT mote uses the unified PUF and TRNG to generate random number xi and response ri, which meets the lightweight requirements of the IoT mote.

Several CMOS-based unified PUF and TRNG chips have been proposed (15–20); however, they often exhibit bias in the performance of either the PUF or TRNG, as shown in Fig. 4F (“Chip performance comparison” section). Because of the inherently limited randomness within CMOS circuits, most CMOS-based unified designs are modified by extracting another kind of randomness from classical PUF-only designs or classical TRNG-only designs. This leaves these CMOS-based unified designs with excellent PUF or TRNG performance in one aspect, comparable to PUF-only (35–38)/TRNG-only (39–42) circuits, but notably weaker performance in the other aspect. However, in practical applications, the actual performance of such unified designs will be limited by their weaknesses, making them difficult to achieve optimal results. Our proposed unified chip exploits the intrinsic randomness of memristor devices with comparable PUF and TRNG capabilities, which can achieve superior performance in practical applications. Figure 4G shows the performance comparison

of the abovementioned authentication process using our memristorbased unified chip and other CMOS-based unified chips (“Chip application in authentication protocol” section), indicating that our memristor chip achieves a 3.82× throughput improvement. Compared to our previous work (21), this study introduces a competing FORMING technique to enhance PUF reliability, removes the perturbation operation in TRNG generation, and eliminates the analogto-digital converter component in the design, thus achieving notable improvements in area, throughput, and energy consumption. Unlike previous work that conducted experiments on the basis of array testing and simulation, this study realizes a unified PUF and TRNG chip that can generate stable PUF data and random bitstream end to end. The overall comparison is summarized in fig. S6.

# DISCUSSION

We have reported a memristor-based unified PUF and TRNG chip that can generate stable PUF bits and random bitstream end to end. By exploiting the memristor device intrinsic physical randomness as an entropy source and combining it with the well-designed entropy extractor, the unified chip can achieve a 41.7-Mbps throughput with a minimum area overhead of 0.291 $\mathrm { M F } ^ { 2 }$ for the entropy extractor. In addition, we propose a PUF concealment and recovery method and implement it on the chip to prevent the PUF data from leakage through physical attacks. The chip can achieve a hiding rate up to 40% and a recovery error rate as low as 0.46%. Our chip shows excellent PUF $( < 1 0 ^ { - 5 }$ native BER without postprocessing) and TRNG performance (min-entropy of 0.9961), stable operation voltage (0.9 to 1.0 V), wide temperature range (−40 to $1 2 5 ^ { \circ } \mathrm { \bar { C } } )$ , good cycling ability (more than ${ 1 0 } ^ { 9 } )$ , and long lifetime. Compared to other CMOSbased unified chips, our work shows balanced and compatible PUF and TRNG performance and can achieve a 3.82× throughput improvement in authentication task. In summary, the proposed memristor unified chip can realize lightweight, high-security, and high-performance hardware security primitives and is a practical and feasible solution for IoT security problems.

# MATERIALS AND METHODS

# Memristor device

The unified chip including the memristor device is fabricated using a standard 28-nm Si CMOS process by foundry. The memristor device uses a material stack of TiN/OGL/MO/HfOx/TiN and is integrated between metal 1 and metal 2. The metal oxidation layers MO/HfOx are fabricated using the atomic layer deposition technique. The bottom electrode TiN and the top electrode TiN/OGL are fabricated using the physical vapor deposition technique. The size of the memristor device is 180 nm by 145 nm, and the size of the 1T1R cell is 0.11 μm by 0.11 μm.

# Operation condition details

The voltage amplitudes and pulse widths applied to the memristor array for PUF concealing, PUF recovery, PUF generation, and PUF and TRNG reading are as follows. The port where the voltage is applied on the 2T2R cell is shown in fig. S7. PUF generation requires competing FORMING operations on the 2T2R cells. During this process, we adopt the standard incremental step pulse programming method, as shown in fig. S1. $V _ { \mathrm { B L } } = V _ { \mathrm { F O R M } }$ is from 2.0 to 3.3 V, with a step of 0.05 V; $V _ { \mathrm { W L } }$ is from 0.4 to 0.8 V, with a step of 0.05 V;

SL is grounded; and the pulse width is 10 μs, and the pulses number is concentrated between 100 and 200. Since the chip contains a total of 16,000 2T2R memristor cells, the total time required for the PUF generation process of the whole chip is estimated to be 1 $. 0 \mu \mathrm { s } \times 1 5 0 \times 1 6 , 0 0 0 = 2 4 \mathrm { ~ s ~ }$ . For PUF concealing and recovery, the entire array has to be SET/RESET. In the PUF concealing operation, $V _ { \mathrm { B L } } = V _ { \mathrm { S E T } } = 2 . 7 \mathrm { V } , V _ { \mathrm { W L } } = 0 . 9 \mathrm { V } ,$ the SL is grounded, and the pulse width is 4 μs. In the PUF recovery operation, $V _ { \mathrm { S L } } = V _ { \mathrm { R E S E T } } = 3 ~ \mathrm { V } ,$ $V _ { \mathrm { W L } } = 1 . 8 ~ \mathrm { V } ,$ the BL is grounded, and the pulse width is 4 μs. The total time required for PUF concealing and recovery across the chip is $4 \mu \mathrm { s } \times 1 6 , 0 0 0 = 6 4$ ms. For PUF and TRNG reading operations (Fig. 2, B and C), $V _ { \mathrm { R E A D } } = 0 . 2 \ : \mathrm { V } , \ : V _ { \mathrm { W L } } = 0 . 9 \ : \mathrm { V } ,$ and the SL is grounded. The reading speed is determined by the delay of the unified entropy extractor circuit. As discussed in the main text, at VDD = 1 V, the PUF throughput can reach 67.6 Mbps, while the TRNG throughput can reach 41.7 Mbps.

# Entropy extractor design details

The proposed entropy extractor optimizes the area and power consumption as follows

1) Use a low-power dynamic comparator with a p-type metaloxide semiconductor as an input transistor for low-voltage comparisons (fig. S2C). EN is the enable signal, and $V _ { \mathrm { b i a s } }$ is the bias voltage, which determines the circuit’s current consumption (power consumption). When $V _ { \mathrm { b i a s } }$ is set at 0.45 V, the dynamic comparator is in the normal operating state, and if the $V _ { - }$ terminal inputs 0.1-V fixed voltage and the V+ terminal inputs a 0.2-V square wave signal, the circuit’s delay is 3.80 ns (simulated); when $V _ { \mathrm { b i a s } }$ is set at 0.05 V, the dynamic comparator is in the subthreshold operating state, and under the same input signal, the circuit’s delay extends to 353.84 ns.   
2) Use a third-order ring oscillator circuit to replace the traditional complex clock signal generation circuit, reaching a minimum area of 3.10 μm by 9.12 μm. Besides, the ring oscillator circuit adopts a current-starved structure (fig. S3D), where $V _ { \mathrm { b p } }$ and $V _ { \mathrm { b n } }$ are the bias voltages of the p-channel metal-oxide semiconductor and ntype metal-oxide semiconductor in the oscillator circuit. Decreasing $V _ { \mathrm { b n } }$ and increasing $V _ { \mathrm { b p } }$ reduce the power consumption of the circuit but also decrease the oscillation frequency, as shown in fig. S3E. The maximum oscillation frequency of the circuit is 7.74 GHz, and the oscillation frequency of the circuit drops to 0.83 GHz with $V _ { \mathrm { b p } }$ and $V _ { \mathrm { b n } }$ of 0.45 V. The oscillation frequency of the ring oscillator circuit is closely related to the randomness of the TRNG, so the optimal value of the circuit’s bias voltage needs to be determined experimentally.   
3) Connect the output of the ring oscillator circuit to the input of the D-flip-flop instead of a single-bit counter. The circuit is modified to operate with fewer logic gate flips, resulting in lower dynamic power consumption.

# PUF and TRNG performance definition

Uniformity is quantified using the Hamming weights, and the definition of the Hamming weight is

$$
\mathrm{HW}(\%) = 100\times \frac{1}{N_{\text{challenges}}}\sum_{c = 1}^{N_{\text{challenges}}}r_{c}
$$

where $N _ { \mathrm { c h a l l e n g e s } }$ refers to the number of bits included in each response, and $r _ { \mathrm { c } }$ is the value of the cth bit in the response.

Reliability is evaluated using intra-Hamming distance/BER, whose definition is

$$
\text {Intra} - \mathrm {HD} / \mathrm {BER} (\%) = 1 0 0 - 1 0 0 \times \frac {2}{N _ {\text {cycles}} \left(N _ {\text {cycles}} - 1\right)} \sum_ {i = 1} ^ {N _ {\text {cycles}} - 1} \sum_ {j = i + 1} ^ {N _ {\text {cycles}}} r _ {i} \bigoplus r _ {j}
$$

where $N _ { \mathrm { c y c l e s } }$ s refers to the number of times the response is measured by applying a challenge, and $r _ { i }$ and $r _ { j }$ refer to the response obtained from the ith and jth measurements, respectively, under the same challenge. Therefore, the Intra-HD/BER of a reliable PUF should not increase notably with the number of tests.

Uniqueness is evaluated using inter-Hamming distance, whose definition is

$$
\text{Inter - HD} (\%) = 100 \times \frac{2}{N_{\text{chips}}\left(N_{\text{chips}} - 1\right)}\sum_{i = 1}^{N_{\text{chips}} - 1}\sum_{j = i + 1}^{N_{\text{chips}}}r_{i}\bigoplus r_{j}
$$

where $N _ { \mathrm { c h i p s } }$ refers to the number of measured PUFs, and $r _ { i }$ and $r _ { j }$ refer to the response of the ith and jth chip under the same challenge, respectively.

The definition of diffuseness is

$$
\text {D i f f u s e n e s s} (\%) = 1 0 0 \times \frac {2}{N _ {\text {ch a l l e n g e s}} \left(N _ {\text {ch a l l e n g e s}} - 1\right)} \sum_ {i = 1} ^ {N _ {\text {ch a l l e n g e s}} - 1} \sum_ {j = i + 1} ^ {N _ {\text {ch a l l e n g e s}}} r _ {i} \bigoplus r _ {j}
$$

where $N _ { \mathrm { c h a l l e n g e s } }$ refers to the number of times the response is applied, and $r _ { i }$ and $r _ { j }$ refer to the responses obtained by applying different excitations for the ith and jth times, respectively.

The definition of minimum entropy of TRNG is

$$
\text {M i n i m u m e n t r o p y} = - \log_ {2} \max  \left(p _ {0}, p _ {1}\right)
$$

where $\pmb { \mathit { p } } _ { 0 }$ is the probability o $\because 0 ^ { \dag }$ occurring, and ${ \boldsymbol { p } } _ { 1 }$ is the probability ${ \mathrm { o f } } ^ { \alpha } { 1 } ^ { \gamma }$ occurring in the data. Minimum entropy has a cryptographic meaning, i.e., the amount of information contained in each bit of data. For example, the 128-bit true random number has $p _ { 0 } = 0 . 2$ and $\begin{array} { r } { p _ { 1 } = 0 . 8 , } \end{array}$ and the corresponding minimum entropy is 0.323. Assuming that a hacker wants to crack this string of true random numbers, he has a probability of guessing correctly of at most $0 . 5 ^ { 1 2 8 } \times 0 . 3 2 2 = 3 . 9 \dot { 2 } \times 1 0 ^ { - 1 3 } ;$ ; if the minimum entropy of the 128-bit true random number is raised to 0.999, the probability of hacking correctly will be markedly reduced to $3 . 2 1 \times \dot { 1 } 0 ^ { - 3 9 }$ .

# Performance constraint analysis

Here, we analyze the factors that affect the chip robustness, including the circuit designs and memristor devices. In terms of circuits, the performance of the two most critical modules in the entropy extractor, the ring oscillator and the dynamic comparator, is simulated under different process, voltage, and temperature corers. The simulation results are shown in fig. S8. For the ring oscillator, the oscillation frequency notably affects the randomness and throughput of the TRNG. For the dynamic comparator, its conversion time affects the throughput of both the PUF and TRNG. The simulation results show that the oscillation frequency of the ring oscillator decreases when $\mathrm { V D D } \leq 0 . 8 \mathrm { V } ,$ , which is the main reason for the reduction in throughput and randomness of the TRNG at $\mathrm { V D D } \leq 0 . 8 \mathrm { V } .$ The delay of the dynamic comparator increases as the temperature decreases and is relatively long when $\mathrm { V D D } = 0 . 7$ to 0.8 V. This is the factor that contributes to the reduced throughput of the PUF and TRNG under low-temperature and low-voltage conditions.

In terms of memristor devices, the endurance and retention characteristics of the memristor also affect the performance of the chip. During the 125°C burn-in test, as the baking time increases, both the high- and low-resistance states drift toward a higherresistance direction, leading to an increase in the recovered PUF error rates, as shown in fig. S9A. During the $1 0 ^ { 4 }$ SET-RESET cycles, the high- and low-resistance window of the device remains stable, as shown in fig. S9B. However, under continuous SET pulses, unformed devices can be unintentionally formed, causing PUF bit errors, which limits the conceal-recover endurance of our chip to the order of a hundred times. By optimizing the material stack, the required FORMING voltage can be increased, reducing the occurrence of unintended FORMING and further improving the conceal-recover endurance of the chip.

# Chip performance comparison

In the chip design, area, energy consumption, and performance are the three most critical metrics that collectively determine the overall efficiency and practicality of a chip. Area metrics reflect the cost and integration capability, energy consumption affects the standby time and energy usage, and performance determines the speed and efficiency of task processing. Circuits based on the same design methodology and technology node are limited to trade-offs between these three factors and cannot achieve simultaneous performance enhancements. Thus, we define the TRNG performance as

$$
\text {T R N G p e r f o r m a n c e} = \frac {\text {T h r o u g h p u t}}{\text {A r e a} \times \text {E n e r g y}} \left(\frac {\text {M b p s}}{\text {M F} ^ {2} \times \text {p J / b i t}}\right)
$$

where to eliminate the influence of the fabrication process, the unit of chip area is $\mathrm { M F } ^ { 2 } \left( 1 0 ^ { 6 } \times \mathrm { F } ^ { 2 } \right)$ ), where F represents the feature size of the process.

For PUF, BER is an important metric. In security tasks such as authentication, an error PUF bit will lead to authentication failure, necessitating reauthentication. If the BER of a PUF is x (x is very small <0.001), for an N-bit authentication, its authentication error rate is roughly estimated to be N × x, demonstrating a linear relationship. We here add the BER factor to the PUF performance, defining it as

$$
\text {P U F} = \frac {\text {T h r o u g h p u t}}{\text {A r e a} \times \text {E n e r g y} \times \text {B E R}} \left(\frac {\text {M b p s}}{\text {M F} ^ {2} \times \text {p J / b i t}}\right)
$$

# Chip application in authentication protocol

As mentioned in the “PUF and TRNG performance definition” section, in authentication, an error PUF bit will lead to authentication failure, necessitating reauthentication. For an N-bit authentication, the relationship between the authentication error rate and PUF BER is

$$
\mathrm {A E R} = 1 - (1 - \mathrm {B E R}) ^ {N}
$$

From this formula, we can see that the authentication error rate will amplify the BER by at least N times, so nowadays, PUF still needs some postprocessing method to reduce the BER to meet the needs of practical application. The temporal majority voter (TMV) and error-correcting code (ECC) are the most commonly used methods. To make a fair comparison, we apply TMV3 and 1-bit ECC error correction to all the unified chips to reduce their BER and then calculate their authentication error rate. With TMV3, the BER can be reduced to

$$
\mathrm {B E R} _ {\mathrm {T M V} 3} = 1 - (1 - \mathrm {B E R}) ^ {3} - 3 \times \mathrm {B E R} \times (1 - \mathrm {B E R}) ^ {2}
$$

Then, with 1-bit ECC, the authentication error rate can be further reduced to

$$
\mathrm {A E R} _ {\mathrm {T M V 3 E C C}} = 1 - \left(1 - \mathrm {B E R} _ {\mathrm {T M V 3}}\right) ^ {N} - C _ {N} ^ {2} \times \mathrm {B E R} _ {\mathrm {T M V 3}} \times \left(1 - \mathrm {B E R} _ {\mathrm {T M V 3}}\right) ^ {N - 1}
$$

The impact of TMV3 and 1-bit ECC methods on authentication error rate is shown in fig. S10. For a unified PUF and TRNG chip, the maximum throughput rate that can be achieved per unit area when performing the N-bit authentication task is

Norm. throughput =

$$
\frac {\operatorname* {m i n} \left(\text {T h r o u g h p u t} _ {\mathrm {P U F}} , \text {T h r o u g h p u t} _ {\mathrm {T R N G}}\right) \times \left(1 - \mathrm {A E R} _ {\mathrm {T M V} 3 \mathrm {E C C}}\right)}{\text {A r e a} \times N} \left(\frac {\mathrm {M b p s}}{\mathrm {M F} ^ {2}}\right)
$$

where Throughpu $\mathrm { t _ { P U F } }$ and Throughput $\mathrm { T R N G }$ are the PUF and TRNG throughput, respectively.

# Supplementary Materials

The PDF file includes:

Figs. S1 to S10

Legend for movie S1

Other Supplementary Material for this manuscript includes the following: Movie S1

# REFERENCES AND NOTES

1. J. Deogirikar, A. Vidhate, “Security attacks in IoT: A survey,” in 2017 International Conference on I-SMAC (IoT in Social, Mobile, Analytics and Cloud) (I-SMAC) (IEEE , 2017), pp. 32–37.   
2. S. Hameed, F. I. Khan, B. Hameed, Understanding security requirements and challenges in Internet of Things (IoT): A review. J. Comput. Netw. Commun. 2019, 9629381 (2019).   
3. R. Pappu, B. Recht, J. Taylor, N. Gershenfeld, Physical one-way functions. Science 297, 2026–2030 (2002).   
4. Y. Gao, S. F. Al-Sarawi, D. Abbott, Physical unclonable functions. Nat. Electron. 3, 81–91 (2020).   
5. C . Herder, M.-­D. Yu, F. Koushanfar, S. Devadas, Physical unclonable functions and applications: A tutorial. Proc. IEEE 102, 1126–1141 (2014).   
6. C . Tokunaga, D. Blaauw, T. Mudge, True random number generator with a metastabilitybased quality control. IEEE J. Solid State Circuits 43, 78–85 (2008).   
7. Z. Wang, H. Wu, G. W. Burr, C. S. Hwang, K. L. Wang, Q. Xia, J. J. Yang, Resistive switching materials for information processing. Nat. Rev. Mater. 5, 173–195 (2020).   
8. R. Arppe, T. J. Sørensen, Physical unclonable functions generated through chemical methods for anti-counterfeiting. Nat. Rev. Chem. 1, 0031 (2017).   
9. J. Feng, W. Wen, X. Wei, X. Jiang, M. Cao, X. Wang, X. Zhang, L. Jiang, Y. Wu, Random organic nanolaser arrays for cryptographic primitives. Adv. Mater. 31, 1807880 (2019).   
10. H . Nili, G. C. Adam, B. Hoskins, M. Prezioso, J. Kim, M. R. Mahmoodi, F. M. Bayat, O. Kavehei, D. B. Strukov, Hardware-intrinsic security primitives enabled by analogue state and nonlinear conductance variations in integrated memristors. Nat. Electron. 1, 197–202 (2018).   
11. A. Dodda, S. S. Radhakrishnan, T. F. Schranghamer, D. Buzzell, P. Sengupta, S. Das, Graphene-based physically unclonable functions that are reconfigurable and resilient to machine learning attacks. Nat. Electron. 4, 364–374 (2021).   
12. H . Jiang, C. Li, R. Zhang, P. Yan, P. Lin, Y. Li, J. J. Yang, D. Holcomb, Q. Xia, A provable key destruction scheme based on memristive crossbar arrays. Nat. Electron. 1, 548–554 (2018).   
13. Y.-­C. Chiu, W.-S. Khwa, C.-S. Yang, S.-­H. Teng, H.-Y. Huang, F.-­C. Chang, Y. Wu, Y.-A. Chien, F.-L. Hsieh, C.-Y. Li, A CMOS-integrated spintronic compute-in-memory macro for secure AI edge devices. Nat. Electron. 6, 534–543 (2023).   
14. D . Zhong, J. Liu, M. Xiao, Y. Xie, H. Shi, L. Liu, C. Zhao, L. Ding, L.-M. Peng, Z. Zhang, Twin physically unclonable functions based on aligned carbon nanotube arrays. Nat. Electron. 5, 424–432 (2022).   
15. S. Taneja, V. K. Rajanna, M. Alioto, In-memory unified TRNG and multi-bit PUF for ubiquitous hardware security. IEEE J. Solid State Circuits. 57, 153–166 (2021).   
16. S. Taneja, V. K. Rajanna, M. Alioto, “36.1 Unified in-memory dynamic TRNG and multi-bit static PUF entropy generation for ubiquitous hardware security,” in 2021 IEEE International Solid-State Circuits Conference (ISSCC) (IEEE , 2021), vol. 64, pp. 498–500.

17. S. Satpathy, S. Mathew, V. Suresh, M. Anders, H. Kaul, A. Agarwal, S. Hsu, R. Krishnamurthy, V. De, “An all-digital unified static/dynamic entropy generator featuring self-calibrating hierarchical Von Neumann extraction for secure privacy-preserving mutual authentication in IoT mote platforms,” in 2018 IEEE Symposium on VLSI Circuits (IEEE , 2018), pp. 169–170.   
18. S. Larimian, M. Mahmoodi, D. Strukov, Lightweight integrated design of PUF and TRNG security primitives based on eFlash memory in 55-nm CMOS. IEEE Trans. Electron Devices 67, 1586–1592 (2020).   
19. Y. Cao, W. Liu, Y. Zheng, S. Chen, J. Ye, L. Qian, C.-­H. Chang, A new reconfigurable true random number generator and physical unclonable function unified chip with on-chip auto-calibration. IEEE Trans. Circuits Syst. I Regul. Pap. 70, 4900–4913 (2023).   
20. M. Danesh, A. B. Venkatasubramaniyan, G. Kapoor, N. Ramesh, S. Sadasivuni, S. T. Chandrasekaran, A. Sanyal, Unified analog PUF and TRNG based on current-steering DAC and VC O. IEEE Trans. Very Large Scale Integr. VLSI Syst. 28, 2280–2289 (2020).   
21. B. Gao, B. Lin, X. Li, J. Tang, H. Qian, H. Wu, A unified PUF and TRNG design based on 40-nm RRAM with high entropy and robustness for IoT security. IEEE Trans. Electron Devices 69, 536–542 (2022).   
22. B. Gao, B. Lin, Y. Pang, F. Xu, Y. Lu, Y.-­C. Chiu, Z. Liu, J. Tang, M.-F. Chang, H. Qian, Concealable physically unclonable function chip with a memristor array. Sci. Adv. 8, eabn7753 (2022).   
23. R. Dittmann, S. Menzel, R. Waser, Nanoionic memristive phenomena in metal oxides: The valence change mechanism. Adv. Phys. 70, 155–349 (2021).   
24. S. Yang, B. Gao, F. Xu, Q. Hu, J. Tang, J. Chen, H. Qian, “Oxygen vacancy formation accompanied by Hf oligomer in amorphous-­HfOx-based RRAM: A first principles study,” in 2021 5th IEEE Electron Devices Technology & Manufacturing Conference (EDTM) (IEEE , 2021), pp. 1–3.   
25. Y.-F. Kao, W. C. Zhuang, C.-J. Lin, Y.-­C. King, A study of the variability in contact resistive random access memory by stochastic vacancy model. Nanoscale Res. Lett. 13, 213 (2018).   
26. J. H. Q. Palhares, Y. Beilliard, F. Alibart, E. Bonturim, D. Z. de Florio, F. C. Fonseca, D. Drouin, A. S. Ferlauto, Oxygen vacancy engineering of TaOx-based resistive memories by Zr doping for improved variability and synaptic behavior. Nanotechnology 32, 405202 (2021).   
27. D . Maldonado, F. Gómez-­Campos, M. González, A. Roldán, F. Jiménez-Molinos, F. Campabadal, J. Roldán, Comprehensive study on unipolar RRAM charge conduction and stochastic features: A simulation approach. J. Phys. D Appl. Phys. 55, 155104 (2022).   
28. S. Ambrogio, S. Balatti, A. Cubeta, A. Calderoni, N. Ramaswamy, D. Ielmini, Statistical fluctuations in HfOx resistive-switching memory: Part II —Random telegraph noise. IEEE Transac. Electron Devices 61, 2920–2927 (2014).   
29. D . Veksler, G. Bersuker, B. Chakrabarti, E. Vogel, S. Deora, K. Matthews, D. Gilmer, H.-F. Li, S. Gausepohl, P. Kirsch, “Methodology for the statistical evaluation of the effect of random telegraph noise (RTN ) on RRAM characteristics,” in 2012 International Electron Devices Meeting (IEEE , 2012), pp. 9.6.1–9.6.4.   
30. D . Ielmini, F. Nardi, C. Cagli, Resistance-dependent amplitude of random telegraph-signal noise in resistive switching memories. Appl. Phys. Lett. 96, 053503 (2010).   
31. A. Rukhin, J. Soto, J. Nechvatal, M. Smid, E. Barker, S. Leigh, M. Levenson, M. Vangel, D. Banks, A. Heckert, A Statistical Test Suite for Random and Pseudorandom Number Generators for Cryptographic Applications (National Institute of Standards and Technology, 2001), vol. 22.   
32. M. S. Turan, E. Barker, J. Kelsey, K. A. McKay, M. L. Baish, M. Boyle, Recommendation for the Entropy Sources Used for Random Bit Generation (National Institute of Standards and Technology, 2018).

33. J. Delvaux, R. Peeters, D. Gu, I. Verbauwhede, A survey on lightweight entity authentication with strong PUFs. ACM Comput. Surv. 48, 1–42 (2015).   
34. A. Aysu, E. Gulcan, D. Moriyama, P. Schaumont, M. Yung, “End-to-end design of a PUF-based privacy preserving authentication protocol,” in Cryptographic Hardware and Embedded Systems--CHES 2015: 17th International Workshop, Saint-Malo, France, September 13–16, 2015, Proceedings 17 (Springer, 2015), pp. 556–576.   
35. Y. Choi, B. Karpinskyy, K.-M. Ahn, Y. Kim, S. Kwon, J. Park, Y. Lee, M. Noh, “Physically unclonable function in 28nm fdsoi technology achieving high reliability for aec-q 100 grade 1 and iso 26262 asil-b,” in 2020 IEEE International Solid-State Circuits Conference (ISSCC) (IEEE , 2020), pp. 426–428.   
36. D . Li, K. Yang, “25.1 A 562F2 physically unclonable function with a zero-overhead stabilization scheme,” in 2019 IEEE International Solid-State Circuits Conference (ISSCC) (IEEE , 2019), pp. 400–402.   
37. J. Li, T. Yang, M. Yang, P. R. Kinget, M. Seok, An area-efficient microprocessor-based SoC with an instruction-cache transformable to an ambient temperature sensor and a physically unclonable function. IEEE J. Solid State Circuits 53, 728–737 (2018).   
38. K. Liu, X. Chen, H. Pu, H. Shinohara, A 0.5-­V hybrid SRAM physically unclonable function using hot carrier injection burn-in for stability reinforcement. IEEE J. Solid State Circuits 56, 2193–2204 (2020).   
39. M. Kim, U. Ha, K. J. Lee, Y. Lee, H.-J. Yoo, A 82-nW chaotic map true random number generator based on a sub-ranging SAR ADC . IEEE J. Solid State Circuits 52, 1953–1965 (2017).   
40. E . Kim, M. Lee, J.-J. Kim, “8.2 8Mb/s 28Mb/mJ robust true-random-number generator in 65nm CMOS based on differential ring oscillator with feedback resistors,” in 2017 IEEE International Solid-State Circuits Conference (ISSCC) (IEEE , 2017), pp. 144–145.   
41. S. Taneja, M. Alioto, Fully synthesizable unified true random number generator and cryptographic core. IEEE J. Solid State Circuits 56, 3049–3061 (2021).   
42. R. Zhang, X. Wang, K. Liu, H. Shinohara, A 0.186-pJ per bit latch-based true random number generator featuring mismatch compensation and random noise enhancement. IEEE J. Solid State Circuits 57, 2498–2508 (2022).

# Acknowledgments

Funding: This work was supported by the following: STI 2030-Major Projects 2021ZD0201200 (to H.W.), National Natural Science Foundation of China 62025111 (to H.W.), National Natural Science Foundation of China 624B200167 (to X.L.), IoT Intelligent Microsystem Center of Tsinghua University-­China Mobile Communications Group Co., Ltd. Joint Institute, Shanghai Municipal Science and Technology Major Project, Beijing Advanced Innovation Center for Integrated Circuits, and Tsinghua ID G/McGovern “Brain+X” Seed Grant Doctoral and Postdoctoral Program. Author contributions: Experiment design: X.L. and B.L. Manuscript writing: X.L. and B.L. Test board design: B.L. Memristor fabrication process development: B.G., T.-Y.S., Z.S., J.T., H.Q., and H.W. Chip fabrication: T.-Y.S. and H.Q. Device mechanism analysis: Y.L. Memristor read noise and endurance data: S.Y. Supervision: B.G. and H.W. Manuscript review: all authors. Competing interests: The authors declare that they have no competing interests. Data and materials availability: All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. The codes that support the findings of this study are available at Zenodo https://zenodo.org/records/11515040.

Submitted 11 June 2024

Accepted 21 February 2025

Published 26 March 2025

10.1126/sciadv.adr0112