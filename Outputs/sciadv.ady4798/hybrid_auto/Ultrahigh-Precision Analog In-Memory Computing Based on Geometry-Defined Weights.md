---
title: "Ultrahigh-Precision Analog In-Memory Computing Based on Geometry-Defined Weights"
authors:
  - "Analog The"
  - "We Enhanced"
  - "This"
date: "2025-01-01"
year: "2025"
journal: "Science Advances"
doi: "10.1126/sciadv.ady4798"
abstract: "Analog computing has gained increasing attention for its potential in artificial"
abstract_cn: "模拟计算因其在人工智能硬件中的潜力而受到越来越多的关注。传统模拟系统中的计算依赖于固有物理量（如电阻），这些量容易因环境变化或重复编程而产生波动，导致精度受损。本文将存储器件对固有物理量的依赖转移到晶体管的几何比例，实现超高精度模拟计算。展示了一种基于标准"
keywords:
  - "[[In-memory computing]]"
cite: "Zhezhi He, Jing Guo, Zihan Wang, et al. Ultrahigh-Precision Analog In-Memory"
aiSum: "模拟存内计算芯片：几何比例权重、CMOS 工艺、0.101% RMSE、-78.5°C~180°C 温度稳定。"
confidence: "high"
wiki_concepts:
  - "[[In-memory computing]]"
---

Analog computing has gained increasing attention for its potential in artificial intelligence hardware. The computation in traditional analog systems relies on use of intrinsic physical quantities (e.g., resistance), which are prone to fluctuations due to environmental changes or repeated programming, leading to compromised precision. Here, we shift the reliance on intrinsic physical quantity of memory devices to geometric ratio of transistors, enabling ultrahigh-precision analog computation. We demonstrate an analog in-memory computing chip based on a standard complementary metal-oxide semiconductor process, achieving the highest precision reported to date. Enhanced by the proposed weight remapping technique, the chip realizes ultrahigh computing accuracy with a root mean square error of only 0.101% across multiple parallel vector-by-matrix multiplication operations. Moreover, our analog in-memory computing chip maintains high precision, with an error of 0.155 and 0.130% under environmental temperatures of −78.5° and 180°C, respectively. This work pushes the boundaries of analog computing precision by leveraging stable geometry feature of devices.

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

Analog computing holds promise for accelerating artificial intelligence (AI) tasks while improving energy efficiency (1, 2). In analog systems, computations are naturally executed as signals propagate through programmable analog devices (3–10). A common approach in analog computing is the use of crossbar-structured circuits to efficiently perform vector-by-matrix multiplications (VMMs) in parallel (11–31). By programming the analog devices, the signal transformation behavior of the system can be controlled to execute various computational tasks (32– 47). This highly efficient computing paradigm has gained widespread attention, spurring rapid advancements in analog computing (48–66). However, low precision remains a major challenge in realizing practical analog computing systems. Traditional analog systems rely on the intrinsic parameters of devices, such as resistance, to perform computations. These parameters exhibit variability across multiple programming cycles, leading to inconsistencies in output even when targeting the same device state and input (67–72). This variability results in pronounced low-precision issues, which are further exacerbated by environmental factors, especially temperature. As a consequence, the inherent uncertainty in conventional analog systems not only results in low precision but also complicates efforts to improve accuracy through calibration or compensation methods (73, 74).

Here, we propose an analog computing approach that shifts the computation reliance from device parameters to the device geometry. Since geometry is a highly stable factor that does not change once fabricated, the proposed approach enhances the precision of analog computing. Here, as a proof of concept, we demonstrate an analog computing chip using complementary metal-oxide semiconductor

(CMOS) process. The weights of the analog computing chip depend solely on geometric ratio of transistors, enabling the chip to perform dot products with extremely high precision. Experimental results of random VMM operations show that all measured values are nearly identical to the ideal values, with a root mean square error (RMSE) as low as 0.101%, achieving the lowest error level among published analog computing works. Moreover, we find that the proposed analog computing chip can maintain computational precision even under extreme environments. The computational scheme proposed in this work brings a promising approach to highly precise analog computing systems.

# RESULTS

# Highly precise analog computing architecture

Figure 1A schematically illustrates the geometry-based precise analog computing approach, in which the computing process is fundamentally governed by the geometric ratio of two analog devices (e.g., ratio between channel widths of two transistors, m/n). By modifying the effective geometric ratio of two devices (from m/n to m′/n), we can control the analog signal propagation and reconfigure the computing operation (functional relationship from input x to output y). Notably, this functional relationship benefits from inherent stability, as the device geometry remains fixed once the chip is fabricated. Therefore, our approach leverages this geometric stability to enable high-precision analog computing (conceptually presented in Fig. 1B), in contrast to traditional methods that rely on parameters prone to fluctuation.

We leveraged the abovementioned concept to design a geometrybased analog computing architecture for highly precise VMM operations. In our chip, the input current x undergoes two-stage analog computing (Fig. 1C). In the first stage, the local memory storing the binary weight B controls the effective geometric ratio; the second stage is a transistor pair with fixed dimensions, offering a gain of 2i−3 to further amplify the effective geometric ratio of the first computing stage. Overall signal paths for analog computing are governed by the effective geometric ratios of transistors, providing a programmable

![](images/3a9389be0b2a86c96d3e39854e5198948dc5a307978782c493777fddfa030c6a.jpg)  
A

![](images/ba4d3470dac40906371391218c8b1bacf9bb38c8d40e42193841995b982e665c.jpg)  
B

![](images/d79323b47c048418dba232c6c9ceb58b9d28af93f2966b121794b5fa5dde4a1d.jpg)  
C

![](images/19525b80ba73f67e44dfc46b2724f23d59b7d245cf728365c6f89b7b02eb1efa.jpg)  
D   
Fig. 1. Geometry-based precise analog computing approach and architecture. (A) The approach leverages device geometric ratios for computation. $m , m ^ { \prime } ,$ , and n represent the channel width of transistors. G, gate; D, drain; S, source of the transistor. (B) Conceptual illustration showing that the geometric stability enables highprecision analog computing, in contrast to conventional methods that rely on resistance prone to fluctuation. (C) The memory cell, switch, and slave transistor are physically integrated. In our demonstrated chip, the memory cell is a static random-access memory (SRAM) with 6-­T structure, and the switch is realized by an NMOS transistor. The local memory storing the weight data controls the effective geometric ratio of the first computing stage. In the second stage, transistor pairs with fixed dimensions offer the gains o $: 2 ^ { n }$ to further amplify the effective geometric ratio of the first computing stage. Overall signal paths for analog computing are governed by the effective geometric ratios of transistors, providing programmable weights from 0 to 31.875 (0 to 255 code). VDD , the positive supply voltage. (D) Schematic of geometry-based computing architecture. The architecture integrates a 34 × 32 array of geometry-based computation cells, performing parallel VMM operations in the current domain.

weight from 8-bit levels. By combining the two amplifying stages and eight memory bits in an analog in-memory computing (AIMC) cell, the output current y contributed by the input current x is $\sum _ { i = 0 } 2 ^ { i - 3 } \times B _ { i } \times x$ i=0 . In both two stages, the stability of transistor dimensions contributes to ensure the high computational precision.

As shown in the diagram of Fig. 1D, the architecture integrates an array of geometry-based computation cells. All cells in same row share a common gate voltage $V _ { \mathrm { G } i } ,$ which is generated by the master transistor in response to the input current (xi). The output currents from computing cells in the same column are summed according to Kirchhoff ’s current law and then weighted by a set of current scalers to produce the final output current (yi). Thus, this geometrybased configuration enables fully parallel VMM in analog domain, $y _ { j } = \sum _ { i = 1 } ^ { 3 4 } w _ { i , j } \times x _ { i }$ , serving as the core computational engine for analog

signal processing. A detailed flow of geometry-based VMM in current domain is provided in note S1.

The choice of memory type does not affect the precision of the proposed architecture. Therefore, our scheme is compatible with a variety of memory technologies [e.g., static random-access memory (SRAM), dynamic random-access memory (DRAM), flash memory, and resistive random-access memory (RRAM)]. The schematics using different memory technologies are provided in fig. S1, in which the local memory controls the switch of the effective geometric ratio and the weight data do not require to be moved during VMM operations.

# Highly precise VMM operations

As a proof of concept, we use the standard CMOS process to fabricate an AIMC chip (details are provided in Materials and Methods) based on the geometry-based analog computing architecture. The analog computing chip has 34 input channels and 32 output channels,

implementing linear signal transformation from the input current vector to output current vector. Figure 2A shows the photograph of the chip in which six-transistor SRAM is used for memory cell and the switch is realized by an N-type metal-oxide-semiconductor (NMOS) transistor (refer to fig. S1 for details). The memory cell, switch, and slave transistor are closely integrated and laid out in a tight structure.

Since the computation results rely only on the stable geometric ratio, our analog computing chips achieve the highest reported precision for fully parallel VMM operations, even without requiring any postprocessing or output calibration. To evaluate the precision performance, we carried out extensive VMM operations. A customized test system, as illustrated in Fig. 2A, was developed to facilitate the VMM experiment. Its schematic is shown in Fig. 2B. The test system

includes digital-to-analog converters (DACs) and voltage-to-current (V-I) converters that generate 64 channels of currents as input signals for our analog computing chip. The output currents are converted to voltage using current-to-voltage (I-V) converters and subtracted by an analog subtractor to implement signed weight. The output of the subtractor is subsequently measured by analog-to-digital converters (ADCs). A microcontroller unit (MCU) orchestrates the overall operation by controlling DACs, acquiring data from ADCs, and managing the analog computing chip. More details about the test system are provided in Materials and Methods.

The geometry-based approach allows us to use a weight remapping technique to mitigate the mismatch errors and further enhance the accuracy of parallel VMM results. Because of the precision limitation in the fabrication process, the resulting random variations in

![](images/40fad556b307c6f660d46b0d44cb9f148742dc748216f28016a6933bd6838c6b.jpg)  
A   
B

![](images/369f033d1411e5db0837d005fabc473ee762c163dfdb411cc281d02acf6ed817.jpg)

![](images/d4187b11775d3b941bdedd325980e432c3c829f3535cc546d5afeef4e704d7cd.jpg)  
C

![](images/741b0527a4082cbd0d529ba404af3ff5e57fe5cf74eab724d1666cc8e67f82f0.jpg)  
D

![](images/8cd58b54457cabf0f9b20b8774ad7be8ae6dd6163cf3e69fcc6cf9dbc4869bec.jpg)  
E

![](images/6e13231c7b5e1ae355d6b7a061563982ba1adea35d856a12953131c759e9d626.jpg)  
F   
Fig. 2. Ultrahigh precision in parallel analog VMM tests. (A) Photograph of the chip and the VMM precision test system. (B) The schematic of the VMM precision test system. The MCU configures the chip and controls the DACs to generate random input vectors in parallel. Analog VMM results are sampled by the ADC s. (C) The weight remapping process for mitigating mismatch-induced errors. By programming W into the analog computing chip, the chip is able to more precisely implement the intended computation Y = ŴX. (D) Precision performance of the chip across 48,000 measured data points. Results obtained by executing 1500 VMM operations using 64 × 32 matrices with signed weights. (E) Histogram of computational errors (measured results minus expected results). The RMSE is as low as 0.101%, demonstrating extremely high precision. (F) Comparison of computational precision with state-of-the-art analog computing works.

transistor geometry can lead to deviations from ideal behavior, thereby affecting computational accuracy (see note S2 for more details). Fortunately, these geometry variations remain constant after fabrication, allowing them to be effectively calibrated through weight remapping. As a result, their impact on the chip’s computational precision can be negligible. Figure 2C shows this weight remapping process. To implement the target computation Y = ŴX (Ŵ, the expected weight matrix), we deliver a remapped matrix W (W, the matrix actually programmed into the chip) from Ŵ through the proposed weight remapping technique (details of this technique are presented in the note S3). By programming W into the analog computing chip, the chip is able to more precisely implement the intended computation Y = ŴX.

We evaluated the precision performance of the analog computing chip with 48,000 dot product experiments. These 48,000 dot products were obtained by executing 1500 parallel VMMs using 64 × 32 matrices with signed weights, implemented by a 2 × 2 chip array. In experiment, we used uniformly distributed random matrices as target weights, and the uniformly distributed input currents were fed into the analog computing chip. The measured outputs, shown in Fig. 2D, form a thin and straight line, demonstrating an exceptional agreement between the measured and expected computing results. The histogram of dot product errors, normalized by the output range (details are provided in Materials and Methods), is presented in Fig. 2E, with an RMSE of only 0.101%. Notably, some previously reported approaches often adopt sequential operations to enhance the precision performance of VMM calculation (38, 73, 74), which reduces the level of computational parallelism and increases latency. In contrast, our chip achieved this high level of precision without any postprocessing or output calibration, thereby avoiding additional system complexity and energy consumption. To further assess the precision, we compared the precision performance of parallel analog VMM operations in our work and the state-of-the-art analog hardware (12, 33, 42, 45). Our precision evaluation was extended to larger scales through simulations (details are provided in Materials and Methods). These precision results, along with those from previous works, are collectively plotted in Fig. 2F. The comparison demonstrates that our scheme not only achieves the highest reported computational precision to date but also maintains superior precision as the matrix size scales up. More comparisons are provided in table S1. In addition, the precision of AIMC array can be further improved after addressing the missing code issue by combining the circuit design with the weight remapping technique (fig. S6).

# Application demonstrations based on high-precision AIMC chips

The ultrahigh dot product precision enhances the performance of our chips in both neural network inference and scientific computing scenarios. Figure 3A shows the dataset and neural network architecture used to evaluate the chip’s performance on AI tasks, in which all the matrix multiplications are implemented by our AIMC chips. As shown in Fig. 3B, our chips achieve a recognition accuracy of 97.97% on the modified national institute of standards and technology (MNIST) test set. We compare our chip’s results with those implemented by software. As shown in Fig. 3C, our chip achieves an accuracy comparable to the software baseline, with a difference of less than 0.5%. In addition, we compare the chip’s results with the same computations implemented by a simulated AIMC array model, which is built according to a reasonable VMM error of 1.37% (fig. S7), similar to that of the AIMC hardware reported in (33, 42, 45). As shown

in Fig. 3C, our chips achieve 3.8% higher inference accuracy than the simulated AIMC array model with 1.37% VMM error, highlighting the importance of high-precision analog computing in AI tasks.

Moreover, to further emphasize the advantages of high precision, we evaluated our chip in a scientific computing scenario: solving the Navier-Stokes (N-S) equations (refer notes S4 and S5 for details), which are highly sensitive to numerical accuracy due to the accumulation of small errors during iterative calculations. Specifically, we selected a scientific computing application that studies the fluid flow behaviors around a central pillar under diagonally applied force. Figure 3D shows the prediction results of fluid flow behaviors, which are calculated by our AIMC chips. Figure 3E presents the corresponding results obtained by software calculations that use 64-bit floatingpoint precision, exhibiting strong agreement with the measured results from our AIMC platform. For comparison, we also simulated the same scenario using an AIMC array model with a VMM error of 1.37%, which would deliver severe errors, as shown in Fig. 3F.

Furthermore, the analog-input nature makes the proposed chip perfect for direct integration with current-output sensors without ADC/DAC, as demonstrated in note S6 in detail.

# Precision validation under extreme environments

In addition to its record-breaking precision performance, the geometrybased approach also enables the analog computing chips to realize robustness against environmental variations. Changes under environmental conditions often pose substantial challenges for achieving precise analog computing. This is because these environmental fluctuations alter key parameters, including charge carrier mobility, threshold voltage, and resistance, which introduce computation errors and degrade overall precision of analog computing (75–80).

To rigorously evaluate the environmental robustness of our analog computing chip, we selected a random matrix as target weights and programmed it into our chip using the weight remapping technique at room temperature. We then exposed the chip to environmental conditions of low/high temperatures and examined the precision using the same VMM operations. The measured VMM results demonstrate that our chip maintained high computational precision (Fig. 4, A and B), with RMSE values of 0.155 and 0.130% under environmental temperatures of −78.5° and 180°C, respectively. The details of measurements are provided in fig. S10 and Materials and Methods.

To further investigate this robust performance against the temperature changes, we examined the single analog computing cell in the chip and monitored the transistors in our chip over a wide temperature range (Fig. 4C), from 100 to 560 K (fig. S11 and Materials and Methods). As shown in fig. S12, temperature variation considerably affects analog signal transformation characteristics (e.g., transfer characteristics). However, the experimental results show that the output current deviates by no more than 1.47% compared to its value at room temperature (Fig. 4, D to F). This is because temperature variations do not alter the geometric ratios of the transistors, which are fundamental to the accuracy of our computation scheme. Additional discussion on this mechanism is provided in fig. S13.

As shown in Fig. 4G, we also evaluated the single analog computing cell under a strong magnetic field of up to 10 T (fig. S14 and Materials and Methods). As shown in fig. S15, intense magnetic fields affect electron motion and further influence the signal transformation behavior of analog devices. However, our approach remains unaffected by magnetic fields. The experimental results show that

![](images/195b63d4cbcee780a8683e6bb2cfeef267982f7ab4bbeacaacb05996d6244e69.jpg)  
A

![](images/b3f7828777126baede9242f5d23126b31d034925b3dac2263606e8d528a85713.jpg)  
B

![](images/3d250a37e5b90b41f0fe1fda711d7a438fd35fcdbda23bb8c47d7f8e2bd06d2d.jpg)  
C

![](images/75c8f8f91cd42225debccb36cc6a4de2a5abd3a15db65945fddbd9dd379d08ac.jpg)  
D

![](images/d2a4a740ba22c26b540cf9eeb6dd4edc6e876a46ada121478c7e7050493447f1.jpg)  
E

![](images/b608cf9b512318f7ae7bb75423aa2a77785fc94f9d42c1b774dda135db77851b.jpg)  
  
Fig. 3. Application demonstrations based on high-precision AIMC chips. (A) The dataset and neural network architecture used to evaluate our chip’s performance on AI tasks, in which all matrix computations are implemented by our AIMC chips. ReLU, rectified linear unit. (B) The measured confusion matrix on MNI ST test set. (C) Recognition accuracy comparison among: (i) software baseline without computing error, (ii) the results measured by our chips, and (iii) the results simulated with an AIMC array model with 1.37% VMM error. (D) Fluid dynamics results of solving the Navier-Stokes (N-S) equations, which are measured from our AIMC chip. (E) Corresponding results obtained using software to execute the same computations with precision of 64-bit floating point. (F) Simulated results using an AIMC array model with 1.37% VMM error.

the output current fluctuates slightly by no more than 0.21% (Fig. 4, H to J), effectively preserving computational precision. This is also because the computation in our system is determined by the geometric ratios of transistors, rather than their individual electrical characteristics.

# DISCUSSION

We propose an approach that leverages the stability of device geometries to implement highly precise analog computation. To demonstrate this concept, we designed and fabricated an analog computing chip capable of implementing fully parallel VMM operation in analog domain. Across 48,000 measured data in VMM experiments, the RMSE between the expected and measured results was as low as 0.101%, achieving the highest precision reported to date. The application demonstrations of neural network inference and scientific computing highlight the precision performance of our chips. Furthermore, we validated that the geometry-based approach can maintain computational precision in extreme environments. The measured results show that our AIMC chip maintains high precision with RMSE values of 0.155 and 0.130% under environmental conditions

of −78.5° and 180°C, respectively. The work paves the way for development of highly precise and reliable analog computing systems.

# MATERIALS AND METHODS

Analog computing chip design, fabrication, and packaging

Proposed analog computing chip is fabricated using 180-nm technology. The circuit design and layout are conducted in Cadence Virtuoso design environment. After the layout is completed, the layout design files are exported as graphic design system files and sent to the foundry for manufacturing. After the foundry delivers the chip, the wire bonding technique is used to route the signal to the designed printed circuit board (PCB). Then, the chip can interface with peripheral circuits through the PCB and proceed with subsequent experiments.

# The circuit for dot product precision experiment

To conduct the dot product precision experiment, we designed a customized VMM precision test system. The system is assembled on PCBs. The PCBs primarily include DACs, V-I converters, analog computing chips, I-V converters, ADCs, and an MCU. The DACs used

![](images/463d5a9e1d09835b2f216f00b9c4a8539686369a48cc1f36435c2255877a8a2e.jpg)  
A

![](images/40e8ed16af0dd70472db109859baee29f75d43a56ce422045e4103e78935ebb3.jpg)  
B

![](images/17ca8ba467d807203c2e04a03339caa89fb42b6543605d779a5724061c2f6dda.jpg)  
C

![](images/f4f3e70af509237b8ff686d69c9de4af8f534c289f1b8d37dcd298e8bec36330.jpg)  
D

![](images/8da100c5da22d65737379fdd559814a2feccecd9bd6c99b53ec22634a01e6675.jpg)  
G

![](images/d4a976bb0188abe9d7d3524c753e46e3292ff4140806bf7debea3bfc86096547.jpg)  
H

![](images/30fbfc8a20343fca49e944e9a3908c3108bd7dedabdd103b6891f34fed4bde94.jpg)

![](images/b9cd743a2fc95dc9bf69de399d3907dd1823b986e0128b5d312ec3f5979f2e54.jpg)  
E

![](images/d6a86a7bdcc556812d1a00038a0f1e6853075e0d692a6ecdeb260eea58bb0ae5.jpg)

![](images/fd23f6eee61035742108afd84522828d90ceb8dc44696234309f93c25d51cd18.jpg)

![](images/6a77bfee0b8bdd4994221b30b7ff6d001789c19e8d9bc1dedd5c9d7c425a924b.jpg)  
F

![](images/6d55e722e3fc1be18400e0f26878c8cdc560873635fbc4cdc67f699b08ee4456.jpg)  
J   
Fig. 4. Precision validation under extreme environments. (A) Our chip is programmed with a random target matrix using the weight remapping technique at room temperature and then undergoes the same VMM tests under environmental conditions of low/high temperatures. The chip maintained high precision with an RMSE of 0.155% at the environmental temperature of −78.5°C. (B) The chip maintained high computational precision, with an RMSE of 0.130% under the environmental temperature of 180°C. (C) An AIMC cell is tested over a wider temperature range from 100 to 560 K. (D to F) The variation of computing results compared to the output at 300 K, with respect to different input currents (100 nA, 1 μA, and 10 μA). (G) An AIMC cell is tested over a variable magnetic field from 0 to 10 T. The magnetic field direction is perpendicular to the chip. (H to J) The variation of computing results compared to the output at 0 T, when input current is 100 nA, 1 μA, and 10 μA, respectively.

are DAC7678SRGET from Texas Instruments (TI), the V-I and I-V converters are realized by TP5552-VR from 3PEAK, and the ADCs used are ADS131M08IRSN from TI. The MCU used is ST-M32F407ZGT6 from STMicroelectronics.

# Normalized RMSE

Since the outputs of the proposed chip are current signals, the raw data are measured in current, with values typically on the order of $1 0 ^ { - 4 }$ . To ensure a fair comparison with other analog computing approaches, the dot product errors need to be normalized. The

normalized dot product errors in Fig. 2E are obtained by subtracting the ideal value from the actual value and then normalizing it by the range of expected values. The normalized RMSE is the root mean square of the calculated normalized dot product errors. The range of expected values is defined as the difference between their maximum and minimum.

# Precision simulations of the chip at larger scales

The simulation was conducted using foundry-provided process design kit in the Cadence Virtuoso design environment. First, the

postsimulation model was used to determine the resistance of interconnect lines between cells. These resistances were then incorporated into the schematic for connections between cells in different rows within the same column. The number of rows was scaled up to 128, 256, and 512, respectively, and multiple dot product simulations were performed for each scale using randomly generated input and weight vectors. Following the same method used in Fig. 2E, the VMM RMSE is calculated for each scale. Last, these RMSEs were plotted in Fig. 2F.

# Cell-level computational precision measurement under different temperatures

The computational precision of the single master-slave cell under varying temperatures was measured using the Lake Shore CRX-VF probe station. Because of the limited number of probes available in the station, a customized PCB substrate was used to facilitate signal measurement. Signals from the computing core were wire bonded to the PCB, and probes were used to contact the PCB for testing. Nodes with the same potential, such as ground and power supply, were connected by the PCB to minimize the number of probes required. In addition, the PCB was designed with large pads to effectively address the issue of probe slippage during continuous temperature changes. The current input of the master transistor in the computing core and the voltage measurement at the input port, as well as the current measurement at the output port of the slave transistor and the bias voltage applied to the output port, were performed by two source and measure units (SMUs) of the Keithley 2636B. The temperature is controlled by a Lake Shore Model 336 temperature controller. During the experiment, the temperature was set to the target value. After the temperature display stabilized, one SMU was used to input current to the master transistor and measure the voltage at the input port, while the other SMU applied bias voltage to the slave transistor and measured its output current. This procedure was repeated for temperatures ranging from 100 to 560 K. At each temperature, data were collected five times to account for and mitigate occasional measurement errors.

# Array-level computational precision measurement under high and low temperatures

The computational precision of the array-level VMM under high and low temperatures was evaluated using the custom temperaturecontrolled setup shown in fig. S10. First, a total of 50 VMM computations were performed using a remapping technique at room temperature. The weights were signed 34 × 16 matrices. The input vector, target weights, and remapped weights were recorded for highand low-temperature experiments. The input vector and target weights were used to calculate the expected VMM results, and remapped weights were directly written to the chip during high and low temperatures. For high-temperature experiment, a positive temperature coefficient heater with a rated temperature of 180°C was attached to the package substrate using thermal gap filler pads, and then power was supplied to the heaters. Once the heater current had stabilized and the temperature readings from both the thermocoupleconnected digital multimeter and the thermal camera became steady, the same VMM computations performed at room temperature were repeated. The VMM results are shown in Fig. 4B. For low-temperature experiment, dry ice was used to cool the chip. Once the temperature readings from the thermocouple-connected digital multimeter became steady, the same VMM computations were repeated. The VMM results are shown in Fig. 4A.

# Computational precision measurement under different magnetic fields

The computational precision of the single master-slave cell under different magnetic fields was measured using the Oxford TeslatronPT superconducting magnet system. The computing core was mounted on the sample holder, which was inserted into the center of the magnet by a sample rod. The signal from the computing core was routed to the sample holder through wire bonding, and the signal of the sample holder was connected to the outside by the sample rod. The sample holder used is CSB02039T from Spectrum Semiconductor. The current input of the master transistor in the computing core and the voltage measurement at the input port, as well as the current measurement at the output port of the slave transistor and the bias voltage applied to the output port, were performed by two SMUs of the Keithley 2636B. Each measurement involves multiple voltage and current samplings, and the average of the last 100 stable readings is taken as the final result. The magnetic field strength is controlled by the Oxford MercuryiPS magnet controller.

# Supplementary Materials

This PDF file includes:

Notes S1 to S6

Figs. S1 to S15

Table S1

# REFERENCES AND NOTES

1. A. Momeni, B. Rahmani, M. Malléjac, P. del Hougne, R. Fleury, Backpropagation-free training of deep physical neural networks. Science 382, 1297–1303 (2023).   
2. L . G. Wright, T. Onodera, M. M. Stein, T. Wang, D. T. Schachter, Z. Hu, P. L. McMahon, Deep physical neural networks trained with backpropagation. Nature 601, 549–555 (2022).   
3. G. Milano, G. Pedretti, K. Montano, S. Ricci, S. Hashemkhani, L. Boarino, D. Ielmini, C. Ricciardi, In materia reservoir computing with a fully memristive architecture based on self-organizing nanowire networks. Nat. Mater. 21, 195–202 (2022).   
4. Z. Sun, G. Pedretti, E. Ambrosi, A. Bricalli, W. Wang, D. Ielmini, Solving matrix equations in one step with cross-point resistive arrays. Proc. Natl. Acad. Sci. U.S.A. 116, 4123–4128 (2019).   
5. S. Oh, Y. Shi, J. del Valle, P. Salev, Y. Lu, Z. Huang, Y. Kalcheim, I. K. Schuller, D. Kuzum, Energy-efficient Mott activation neuron for full-hardware implementation of neural networks. Nat. Nanotechnol. 16, 680–687 (2021).   
6. L . Sun, Z. Wang, J. Jiang, Y. Kim, B. Joo, S. Zheng, S. Lee, W. J. Yu, B.-S. Kong, H. Yang, In-sensor reser voir computing for language learning via two-dimensional memristors. Sci. Adv. 7, eabg1455 (2021).   
7. W. A. Borders, A. Z. Pervaiz, S. Fukami, K. Y. Camsari, H. Ohno, S. Datta, Integer factorization using stochastic magnetic tunnel junctions. Nature 573, 390–393 (2019).   
8. F. Kiani, J. Yin, Z. Wang, J. J. Yang, Q. Xia, A fully hardware-based memristive multilayer neural network. Sci. Adv. 7, eabj4801 (2021).   
9. Y. Chen, M. Nazhamaiti, H. Xu, Y. Meng, T. Zhou, G. Li, J. Fan, Q. Wei, J. Wu, F. Qiao, L. Fang, Q. Dai, All-analog photoelectronic chip for high-speed vision tasks. Nature 623, 48–57 (2023).   
10. R. Zhu, S. Lilak, A. Loeffler, J. Lizier, A. Stieg, J. Gimzewski, Z. Kuncic, Online dynamical learning and sequence memory with neuromorphic nanowire networks. Nat. Commun. 14, 6697 (2023).   
11. J. J. Yang, D. B. Strukov, D. R. Stewart, Memristive devices for computing. Nat. Nanotechnol. 8, 13–24 (2013).   
12. C . Li, M. Hu, Y. Li, H. Jiang, N. Ge, E. Montgomery, J. Zhang, W. Song, N. Dávila, C. E. Graves, Z. Li, J. P. Strachan, P. Lin, Z. Wang, M. Barnell, Q. Wu, R. S. Williams, J. J. Yang, Q. Xia, Analogue signal and image processing with large memristor crossbars. Nat. Electron. 1, 52–59 (2018).   
13. Z. Wang, C. Li, P. Lin, M. Rao, Y. Nie, W. Song, Q. Qiu, Y. Li, P. Yan, J. P. Strachan, N. Ge, N. McDonald, Q. Wu, M. Hu, H. Wu, R. S. Williams, Q. Xia, J. J. Yang, In situ training of feed-forward and recurrent convolutional memristor networks. Nat. Mach. Intell. 1, 434–442 (2019).   
14. S. D. Spetalnick, M. Chang, B. Crafton, W. S. Khwa, Y. D. Chih, M. F. Chang, A. Raychowdhury, in 2022 IEEE International Solid-State Circuits Conference (ISSCC) (IEEE , 2022), vol. 65, pp. 1–3.

15. M. Prezioso, F. Merrikh-Bayat, B. D. Hoskins, G. C. Adam, K. K. Likharev, D. B. Strukov, Training and operation of an integrated neuromorphic network based on metal-oxide memristors. Nature 521, 61–64 (2015).   
16. Y. Yuan, Y. Yang, X. Wang, X. Li, C. Ma, Q. Chen, M. Tang, X. Wei, Z. Hou, J. Zhu, H. Wu, Q. Ren, G. Xing, P. I. Mak, F. Zhang, in 2024 IEEE International Solid-State Circuits Conference (ISSCC) (IEEE , 2024), vol. 67, pp. 576–578.   
17. D . Ielmini, H. S. P. Wong, In-memory computing with resistive switching devices. Nat. Electron. 1, 333–343 (2018).   
18. Z. Wang, C. Li, W. Song, M. Rao, D. Belkin, Y. Li, P. Yan, H. Jiang, P. Lin, M. Hu, J. P. Strachan, N. Ge, M. Barnell, Q. Wu, A. G. Barto, Q. Qiu, R. S. Williams, Q. Xia, J. J. Yang, Reinforcement learning with analogue memristor arrays. Nat. Electron. 2, 115–124 (2019).   
19. S. Xie, C. Ni, A. Sayal, P. Jain, F. Hamzaoglu, J. P. Kulkarni, in 2021 IEEE International Solid-State Circuits Conference (ISSCC) (IEEE , 2021), vol. 64, pp. 248–250.   
20. M. Hu, C. E. Graves, C. Li, Y. Li, N. Ge, E. Montgomery, N. Davila, H. Jiang, R. S. Williams, J. J. Yang, Q. Xia, J. P. Strachan, Memristor-based analog computation and neural network classification with a dot product engine. Adv. Mater. 30, 1705914 (2018).   
21. K.-U. Demasius, A. Kirschen, S. Parkin, Energy-efficient memcapacitor devices for neuromorphic computing. Nat. Electron. 4, 748–756 (2021).   
22. M. Hu, J. P. Strachan, Z. Li, E. M. Grafals, N. Davila, C. Graves, S. Lam, N. Ge, J. J. Yang, R. S. Williams, in Proceedings of the 53rd Annual Design Automation Conference (ACM, 2016), pp. Article 19.   
23. L . Wang, W. Li, Z. Zhou, H. Gao, Z. Li, W. Ye, H. Hu, J. Liu, J. Yue, J. Yang, Q. Luo, C. Dou, Q. Liu, M. Liu, in 2024 IEEE International Solid-State Circuits Conference (ISSCC) (IEEE , 2024), vol. 67, pp. 582–584.   
24. H . Jia, M. Ozatay, Y. Tang, H. Valavi, R. Pathak, J. Lee, N. Verma, in 2021 IEEE International Solid-State Circuits Conference (ISSCC) (IEEE , 2021), vol. 64, pp. 236–238.   
25. R. Berdan, T. Marukame, K. Ota, M. Yamaguchi, M. Saitoh, S. Fujii, J. Deguchi, Y. Nishi, Low-power linear computation using nonlinear ferroelectric tunnel junction memristors. Nat. Electron. 3, 259–266 (2020).   
26. S. Jung, H. Lee, S. Myung, H. Kim, S. K. Yoon, S.-W. Kwon, Y. Ju, M. Kim, W. Yi, S. Han, B. Kwon, B. Seo, K. Lee, G.-­H. Koh, K. Lee, Y. Song, C. Choi, D. Ham, S. J. Kim, A crossbar array of magnetoresistive memory devices for in-memory computing. Nature 601, 211–216 (2022).   
27. W. Wang, L. Danial, Y. Li, E. Herbelin, E. Pikhay, Y. Roizin, B. Hoffer, Z. Wang, S. Kvatinsky, A memristive deep belief neural network based on silicon synapses. Nat. Electron. 5, 870–880 (2022).   
28. S. Yu, Neuro-inspired computing with emerging nonvolatile memorys. Proc. IEEE 106, 260–285 (2018).   
29. T . C. Kao, M. J. Huang, Y. R. Liu, Y. K. Wang, J. C. Guo, S. S. Chung, in 2024 IEEE Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits) (IEEE , 2024), pp. 1–2.   
30. B. Wang, C. Xue, Z. Feng, Z. Zhang, H. Liu, L. Ren, X. Li, A. Yin, T. Xiong, Y. Xue, S. He, Y. Kong, Y. Zhou, A. Guo, X. Si, J. Yang, in 2023 IEEE International Solid-State Circuits Conference (ISSCC) (IEEE , 2023), pp. 134–136.   
31. Z. Chen, X. Chen, J. Gu, in 2021 IEEE International Solid-State Circuits Conference (ISSCC) (IEEE , 2021), vol. 64, pp. 240–242.   
32. J. Langenegger, G. Karunaratne, M. Hersche, L. Benini, A. Sebastian, A. Rahimi, In-memory factorization of holographic perceptual representations. Nat. Nanotechnol. 18, 479–485 (2023).   
33. M. Le Gallo, R. Khaddam-Aljameh, M. Stanisavljevic, A. Vasilopoulos, B. Kersting, M. Dazzi, G. Karunaratne, M. Brändli, A. Singh, S. M. Müller, J. Büchel, X. Timoneda, V. Joshi, M. J. Rasch, U. Egger, A. Garofalo, A. Petropoulos, T. Antonakopoulos, K. Brew, S. Choi, I. Ok, T. Philip, V. Chan, C. Silvestre, I. Ahsan, N. Saulnier, V. Narayanan, P. A. Francese, E. Eleftheriou, A. Sebastian, A 64-core mixed-signal in-memory compute chip based on phase-change memory for deep neural network inference. Nat. Electron. 6, 680–693 (2023).   
34. W. Yue, T. Zhang, Z. Jing, K. Wu, Y. Yang, Z. Yang, Y. Wu, W. Bu, K. Zheng, J. Kang, Y. Lin, Y. Tao, B. Yan, R. Huang, Y. Yang, A scalable universal Ising machine based on interactioncentric storage and compute-in-memory. Nat. Electron. 7, 904–913 (2024).   
35. S. Wang, Y. Li, D. Wang, W. Zhang, X. Chen, D. Dong, S. Wang, X. Zhang, P. Lin, C. Gallicchio, X. Xu, Q. Liu, K.-­T. Cheng, Z. Wang, D. Shang, M. Liu, Echo state graph neural networks with analogue random resistive memory arrays. Nat. Mach. Intell. 5, 104–113 (2023).   
36. C . Wang, G.-J. Ruan, Z.-Z. Yang, X.-J. Yangdong, Y. Li, L. Wu, Y. Ge, Y. Zhao, C. Pan, W. Wei, L.-B. Wang, B. Cheng, Z. Zhang, C. Zhang, S.-J. Liang, F. Miao, Parallel in-memory wireless computing. Nat. Electron. 6, 381–389 (2023).   
37. C . Wang, S.-J. Liang, C.-Y. Wang, Z.-Z. Yang, Y. Ge, C. Pan, X. Shen, W. Wei, Y. Zhao, Z. Zhang, B. Cheng, C. Zhang, F. Miao, Scalable massively parallel computing using continuous-time data representation in nanoscale crossbar array. Nat. Nanotechnol. 16, 1079–1085 (2021).   
38. P. Yao, H. Wu, B. Gao, J. Tang, Q. Zhang, W. Zhang, J. J. Yang, H. Qian, Fully hardwareimplemented memristor convolutional neural network. Nature 577, 641–646 (2020).   
39. G. Pedretti, C. E. Graves, S. Serebryakov, R. Mao, X. Sheng, M. Foltin, C. Li, J. P. Strachan, Tree-based machine learning performed in-memory with memristive analog CAM. Nat. Commun. 12, 5806 (2021).

40. F. Cai, S. Kumar, T. Van Vaerenbergh, X. Sheng, R. Liu, C. Li, Z. Liu, M. Foltin, S. Yu, Q. Xia, J. J. Yang, R. Beausoleil, W. D. Lu, J. P. Strachan, Power-efficient combinatorial optimization using intrinsic noise in memristor Hopfield neural networks. Nat. Electron. 3, 409–418 (2020).   
41. K. Yoshioka, in 2024 IEEE International Solid-State Circuits Conference (ISSCC) (IEEE , 2024), vol. 67, pp. 574–576.   
42. W. Wan, R. Kubendran, C. Schaefer, S. B. Eryilmaz, W. Zhang, D. Wu, S. Deiss, P. Raina, H. Qian, B. Gao, S. Joshi, H. Wu, H. S. P. Wong, G. Cauwenberghs, A compute-in-memory chip based on resistive random-access memory. Nature 608, 504–512 (2022).   
43. K. Yang, Q. Duan, Y. Wang, T. Zhang, Y. Yang, R. Huang, Transiently chaotic simulated annealing based on intrinsic nonlinearity of memristors for efficient solution of optimization problems. Sci. Adv. 6, eaba9901 (2020).   
44. Y. Lu, X. Li, L. Yan, T. Zhang, Y. Yang, Z. Song, R. Huang, in 2020 IEEE International Electron Devices Meeting (IEDM) (IEEE , 2020), pp. 36.33.31–36.33.34.   
45. S. Ambrogio, P. Narayanan, A. Okazaki, A. Fasoli, C. Mackin, K. Hosokawa, A. Nomura, T. Yasuda, A. Chen, A. Friz, M. Ishii, J. Luquin, Y. Kohda, N. Saulnier, K. Brew, S. Choi, I. Ok, T. Philip, V. Chan, C. Silvestre, I. Ahsan, V. Narayanan, H. Tsai, G. W. Burr, An analog-AI chip for energy-efficient speech recognition and transcription. Nature 620, 768–775 (2023).   
46. Z. Yue, Y. Wang, H. Wang, Y. Wang, R. Guo, L. Tang, L. Liu, S. Wei, Y. Hu, S. Yin, in 2023 IEEE International Solid-State Circuits Conference (ISSCC) (IEEE , 2023), pp. 1–3.   
47. F. Cai, J. M. Correll, S. H. Lee, Y. Lim, V. Bothra, Z. Zhang, M. P. Flynn, W. D. Lu, A fully integrated reprogrammable memristor–CMOS system for efficient multiply–accumulate operations. Nat. Electron. 2, 290–299 (2019).   
48. Y. Li, W. Song, Z. Wang, H. Jiang, P. Yan, P. Lin, C. Li, M. Rao, M. Barnell, Q. Wu, S. Ganguli, A. K. Roy, Q. Xia, J. J. Yang, Memristive field-programmable analog arrays for analog computing. Adv. Mater. 35, e2206648 (2023).   
49. G. Migliato Marega, H. G. Ji, Z. Wang, G. Pasquale, M. Tripathi, A. Radenovic, A. Kis, A large-scale integrated vector–matrix multiplication processor based on monolayer molybdenum disulfide memories. Nat. Electron. 6, 991–998 (2023).   
50. H . Hong, X. Chen, W. Cho, H. Y. Yoo, J. Oh, M. Kim, G. Hwang, Y. Yang, L. Sun, Z. Wang, H. Yang, Dynamic convolutional neural networks based on adaptive 2D memristors. Adv. Funct. Mater. 35, 2422321 (2025).   
51. S. Hong, W. Jo, S. Kim, S. Kim, K. Sohn, H. J. Yoo, in 2024 IEEE Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits) (IEEE , 2024), pp. 1–2.   
52. Z. Liu, J. Mei, J. Tang, M. Xu, B. Gao, K. Wang, S. Ding, Q. Liu, Q. Qin, W. Chen, Y. Xi, Y. Li, P. Yao, H. Zhao, N. Wong, H. Qian, B. Hong, T.-P. Jung, D. Ming, H. Wu, A memristor-based adaptive neuromorphic decoder for brain–computer interfaces. Nat. Electron. 8, 362–372 (2025).   
53. T . Soliman, S. Chatterjee, N. Laleni, F. Müller, T. Kirchner, N. Wehn, T. Kämpfe, Y. S. Chauhan, H. Amrouch, First demonstration of in-memory computing crossbar using multi-level cell FeFET . Nat. Commun. 14, 6348 (2023).   
54. C . Choi, H. Kim, J.-­H. Kang, M.-K. Song, H. Yeon, C. S. Chang, J. M. Suh, J. Shin, K. Lu, B.-­I. Park, Y. Kim, H. E. Lee, D. Lee, J. Lee, I. Jang, S. Pang, K. Ryu, S.-­H. Bae, Y. Nie, H. S. Kum, M.-­C. Park, S. Lee, H.-J. Kim, H. Wu, P. Lin, J. Kim, Reconfigurable heterogeneous integration using stackable chips with embedded artificial intelligence. Nat. Electron. 5, 386–393 (2022).   
55. X. Chen, S. Li, Z. Zhang, W. Zheng, X. Tan, Y. Tang, Y. Shi, L. Ren, Y. Mai, F. Liu, J. Chen, Z. Zhang, A. Guo, T. Xiong, B. Wang, X. Liu, W. Shan, B. Liu, H. Cai, J. Yang, X. Si, in 2025 IEEE International Solid-State Circuits Conference (ISSCC) (IEEE , 2025), vol. 68, pp. 260–262.   
56. C . Li, X. Chen, Z. Zhang, X. Wu, T. Yu, R. Bie, D. Yang, Y. Yao, Z. Wang, L. Sun, Chargeselective 2D heterointerface-driven multifunctional floating gate memory for in situ sensing-memory-computing. Nano Lett. 24, 15025–15034 (2024).   
57. D .-­H. Lim, S. Wu, R. Zhao, J.-­H. Lee, H. Jeong, L. Shi, Spontaneous sparse learning for PCM-based memristor neural networks. Nat. Commun. 12, 319 (2021).   
58. J. Pei, L. Deng, S. Song, M. Zhao, Y. Zhang, S. Wu, G. Wang, Z. Zou, Z. Wu, W. He, F. Chen, N. Deng, S. Wu, Y. Wang, Y. Wu, Z. Yang, C. Ma, G. Li, W. Han, H. Li, H. Wu, R. Zhao, Y. Xie, L. Shi, Towards artificial general intelligence with hybrid Tianjic chip architecture. Nature 572, 106–111 (2019).   
59. K. Zhu, S. Pazos, F. Aguirre, Y. Shen, Y. Yuan, W. Zheng, O. Alharbi, M. A. Villena, B. Fang, X. Li, A. Milozzi, M. Farronato, M. Muñoz-Rojo, T. Wang, R. Li, H. Fariborzi, J. B. Roldan, G. Benstetter, X. Zhang, H. N. Alshareef, T. Grasser, H. Wu, D. Ielmini, M. Lanza, Hybrid 2D– CMOS microchips for memristive applications. Nature 618, 57–62 (2023).   
60. W. Ye, L. Wang, Z. Zhou, J. An, W. Li, H. Gao, Z. Li, J. Yue, H. Hu, X. Xu, J. Yang, J. Liu, D. Shang, F. Zhang, J. Tian, C. Dou, Q. Liu, M. Liu, A 28-nm RRAM computing-in-memory macro using weighted hybrid 2T1R cell array and reference subtracting sense amplifier for AI edge inference. IEEE J. Solid-State Circuit 58, 2839–2850 (2023).   
61. X. Huang, C. Liu, Z. Tang, S. Zeng, S. Wang, P. Zhou, An ultrafast bipolar flash memory for self-activated in-memory computing. Nat. Nanotechnol. 18, 486–492 (2023).   
62. J. Cui, F. An, J. Qian, Y. Wu, L. L. Sloan, S. Pidaparthy, J.-M. Zuo, Q. Cao, CMOS-compatible electrochemical synaptic transistor arrays for deep learning accelerators. Nat. Electron. 6, 292–300 (2023).

63. S. Yoo, S. Chae, T. Chiang, M. Webb, T. Ma, H. Paik, Y. Park, L. Williams, K. Nomoto, H. G. Xing, S. Trolier-McKinstry, E. Kioupakis, J. T. Heron, W. D. Lu, Efficient data processing using tunable entropy-stabilized oxide memristors. Nat. Electron. 7, 466–474 (2024).   
64. Y. Wang, H. Tang, Y. Xie, X. Chen, S. Ma, Z. Sun, Q. Sun, L. Chen, H. Zhu, J. Wan, Z. Xu, D. W. Zhang, P. Zhou, W. Bao, An in-memory computing architecture based on two-dimensional semiconductors for multiply-accumulate operations. Nat. Commun. 12, 3347 (2021).   
65. H . Ning, Z. Yu, Q. Zhang, H. Wen, B. Gao, Y. Mao, Y. Li, Y. Zhou, Y. Zhou, J. Chen, L. Liu, W. Wang, T. Li, Y. Li, W. Meng, W. Li, Y. Li, H. Qiu, Y. Shi, Y. Chai, H. Wu, X. Wang, An in-memory computing architecture based on a duplex two-dimensional material structure for in situ machine learning. Nat. Nanotechnol. 18, 493–500 (2023).   
66. J. Yue, X. Feng, Y. He, Y. Huang, Y. Wang, Z. Yuan, M. Zhan, J. Liu, J. W. Su, Y. L. Chung, P. C. Wu, L. Y. Hung, M. F. Chang, N. Sun, X. Li, H. Yang, Y. Liu, in 2021 IEEE International Solid-State Circuits Conference (ISSCC) (IEEE , 2021), vol. 64, pp. 238–240.   
67. R. Mao, B. Wen, A. Kazemi, Y. Zhao, A. F. Laguna, R. Lin, N. Wong, M. Niemier, X. S. Hu, X. Sheng, C. E. Graves, J. P. Strachan, C. Li, Experimentally validated memristive memory augmented neural network with efficient hashing and similarity search. Nat. Commun. 13, 6284 (2022).   
68. Q. Huo, Y. Yang, Y. Wang, D. Lei, X. Fu, Q. Ren, X. Xu, Q. Luo, G. Xing, C. Chen, X. Si, H. Wu, Y. Yuan, Q. Li, X. Li, X. Wang, M.-F. Chang, F. Zhang, M. Liu, A computing-in-memory macro based on three-dimensional resistive random-access memory. Nat. Electron 5, 469–477 (2022).   
69. Y. Feng, Y. Zhang, Z. Zhou, P. Huang, L. Liu, X. Liu, J. Kang, Memristor-based storage system with convolutional autoencoder-based image compression network. Nat. Commun. 15, 1132 (2024).   
70. J.-M. Hung, C.-X. Xue, H.-Y. Kao, Y.-­H. Huang, F.-­C. Chang, S.-P. Huang, T.-W. Liu, C.-J. Jhang, C.-­I. Su, W.-S. Khwa, C.-­C. Lo, R.-S. Liu, C.-­C. Hsieh, K.-­T. Tang, M.-S. Ho, C.-­C. Chou, Y.-­D. Chih, T.-Y. J. Chang, M.-F. Chang, A four-megabit compute-in-memory macro with eight-bit precision based on CMOS and resistive random-access memory for AI edge devices. Nat. Electron. 4, 921–930 (2021).   
71. W.-­H. Chen, C. Dou, K.-X. Li, W.-Y. Lin, P.-Y. Li, J.-­H. Huang, J.-­H. Wang, W.-­C. Wei, C.-X. Xue, Y.-­C. Chiu, Y.-­C. King, C.-J. Lin, R.-S. Liu, C.-­C. Hsieh, K.-­T. Tang, J. J. Yang, M.-S. Ho, M.-F. Chang, CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors. Nat. Electron. 2, 420–428 (2019).   
72. R. Wang, T. Shi, X. Zhang, J. Wei, J. Lu, J. Zhu, Z. Wu, Q. Liu, M. Liu, Implementing in-situ self-organizing maps with memristor crossbar arrays for data mining and optimization. Nat. Commun. 13, 2289 (2022).   
73. M. Le Gallo, A. Sebastian, R. Mathis, M. Manica, H. Giefers, T. Tuma, C. Bekas, A. Curioni, E. Eleftheriou, Mixed-precision in-memory computing. Nat. Electron. 1, 246–253 (2018).   
74. W. Song, M. Rao, Y. Li, C. Li, Y. Zhuo, F. Cai, M. Wu, W. Yin, Z. Li, Q. Wei, S. Lee, H. Zhu, L. Gong, M. Barnell, Q. Wu, P. A. Beerel, M. S.-W. Chen, N. Ge, M. Hu, Q. Xia, J. J. Yang,

Programming memristor arrays with arbitrarily high precision for analog computing. Science 383, 903–910 (2024).   
75. I . Boybat, B. Kersting, S. G. Sarwat, X. Timoneda, R. L. Bruce, M. BrightSky, M. L. Gallo, A. Sebastian, in 2021 IEEE International Electron Devices Meeting (IEDM) (IEEE , 2021), pp. 28.23.21–28.23.24.   
76. X. Guo, F. M. Bayat, M. Prezioso, Y. Chen, B. Nguyen, N. Do, D. B. Strukov, in 2017 IEEE Custom Integrated Circuits Conference (CICC) (IEEE , 2017), pp. 1–4.   
77. Y. Huang, R. Hopkins, D. Janosky, Y. C. Chen, Y. F. Chang, J. C. Lee, Effect of temperature on analog memristor in neuromorphic computing. IEEE Trans. Electron Devices 69, 6102–6105 (2022).   
78. A. Ma, B. Gao, P. Yao, J. Tang, H. Qian, H. Wu, Thermal analysis and evaluation of memristor-based compute-in-memory chips. Chips 4, 9 (2025).   
79. Y. Ling, Z. Wang, Z. Yu, S. Bao, Y. Yang, L. Bao, Y. Sun, Y. Cai, R. Huang, Temperaturedependent accuracy analysis and resistance temperature correction in RRAM-based in-memory computing. IEEE Trans. Electron Devices 71, 294–300 (2024).   
80. J. Meng, W. Shim, L. Yang, I. Yeo, D. Fan, S. Yu, J. s. Seo, Temperature-resilient RRAM-based in-memory computing for DNN inference. IEEE Micro 42, 89–98 (2022).

# Acknowledgments

Funding: This work was supported in part by the National Key R&D Program of China under grant 2023YFF1203600 (S.-J.L.), the National Natural Science Foundation of China [62034004 (F.M.), 62305155 (C.W.), and 62375131 (W.Y.)], the Leading-edge Technology Program of Jiangsu Natural Science Foundation [BK20232004 (F.M.) and BK20220947 (W.Y.)], the Natural Science Foundation of Jiangsu Province [BK20233001 (F.M.)], the AI & AI for Science Project of Nanjing University [14380241 (C.W.), 14380240 (S.-J.L.), and 14380242 (F.M.)]. F.M. and S.-J.L. would like to acknowledge support from AIQ Foundation and the e-Science Center of Collaborative Innovation Center of Advanced Microstructures. C.W. would like to acknowledge support from the Jiangsu Funding Program for Excellent Postdoctoral Talent (2023ZB079) and Xiaomi Young Scholar Foundation. Author contributions: Conceptualization: X.-J.Y. and C.W. Data curation: X.-J.Y. and C.W. Methodology: X.-J.Y., C.W., Y.Z., Z.L., W.Y., S.W., and W.W. Formal analysis: X.-J.Y. and C.W. Investigation: X.-J.Y. and C.W. Visualization: X.-J.Y., C.W., Z.-­C.W., and Z.Y. Funding acquisition: F.M., S.-J.L., C.W., and C.P. Project administration: F.M., S.-J.L., and C.W. Software: Y.Z., Z.-­C.W., Z.Y., Z.Z., Y.S., D.K., S.D., and X.W. Resources: F.M. and S.-J.L. Supervision: F.M., S.-J.L., and C.W. Writing—original draft: X.-J.Y. and C.W. Writing—review and editing: F.M., S.-J.L., X.-J.Y., C.W., Z.-­C.W., and Z.Y. Competing interests: The authors declare that they have no competing interests. Data and materials availability: All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials.

Submitted 24 April 2025

Accepted 13 August 2025

Published 12 September 2025

10.1126/sciadv.ady4798