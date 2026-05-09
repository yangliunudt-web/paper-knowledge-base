---

title: "An Artificial Neural Network Implemented Using Parallel Dual-Gate Thin-Film Transistors"
authors:
  - "Yushen Hu"
  - "Tengteng Lei"
  - "Yuqi Wang"
  - "Fei Wang"
  - "Man Wong"
date: "2022-09-05"
year: "2022"
journal: "IEEE Transactions on Electron Devices"
doi: "10.1109/TED.2022.3201836"
abstract: "Implementing in-memory computation, an artificial neural network (ANN) consisting\\"
abstract_cn: "实现存内计算，构建了一种人工神经网络，该网络由薄膜晶体管组成，单片集成在电容器阵列的每个单元中。同时采用了单栅和并行双栅薄膜晶体管。电容器和双栅晶体管分别作为存储和计算元件。双栅晶体管能够放大弱相关输入信号并抑制强无关输入信号跨越突触间隙，并且由于基于金属氧化物半导体的寻址晶体管具有极低的关态漏电流，电容器上的电荷存储是准静态的。使用一个4×6阵列对特定一组俄罗斯方块图案进行分类，证明了该人工神经网络的可行性。"
keywords:
  - "[[Artificial neural network]]"
  - "[[Dual-gate TFT]]"
  - "[[In-memory computing]]"
  - "[[Thin-film transistor]]"
cite: "[1] Hu Y, Lei T, Wang Y, et al. An artificial neural network implemented using parallel\\"
aiSum: "双栅TFT人工神经网络：单片集成电容器阵列，4×6阵列实现俄罗斯方块分类，双栅结构放大弱信号、抑制强噪声，准静态电荷存储。"
confidence: "high"
wiki_concepts:
  - "[[In-memory computing]]"
---

# An Artificial Neural Network Implemented Using Parallel Dual-Gate Thin-Film Transistors

Yushen Hu , Tengteng Lei , Yuqi Wang , Fei Wang , Senior Member, IEEE, and Man Wong , Senior Member, IEEE

Abstract-Implementing in-memory computation,an artificial neural network (ANN) consisting of thin-film transistors (TFTs) monolithically integrated in each unit of an array of capacitors is constructed. Both single-gate and parallel, dual-gate (DG) TFTs are deployed. The capacitors and the DG TFTs serve as the respective memory and computational elements. The DG TFT offers the capability of amplifying a weak but relevant input signal and suppressing a strong but irrelevant input signal across a synaptic gap, and the storage of charge on the capacitor is pseudostatic because of the exceptionally low OFF-state leakage current of the accompanying address TFT built on a metal–oxide semiconductor. The feasibility of such an ANN is demonstrated using a $4 \times 6$ array for classifying a specific set of Tetris patterns.

Index Terms—Artificial neural network (ANN), dual gate (DG), metal–oxide semiconductor, synapse, thin-film transistor (TFT).

# I. INTRODUCTION

A N ARTIFICIAL neural network (ANN) is a computationscheme for data processing and pattern classification by scheme for data processing and pattern classification by mimicking the interconnectivity and the in-memory computation of a mammalian brain consisting of massively connected neurons with local weight-adjusted passage of signals across synaptic gaps. However, software implementations of ANNs are often executed on computers based on the von Neumann architecture requiring the passage of data between separate memory and instruction execution units. The inherent difference in computing architectures results in a rapid decrease

Manuscript received 3 May 2022; revised 19 July 2022 and 16 August 2022; accepted 22 August 2022. Date of publication 5 September 2022; date of current version 22 September 2022. This work was supported in part by the Innovation and Technology Fund under Grant GHP/013/19SZ, in part by the Science and Technology Program of Shenzhen under Grant SGDX20190918105001787, and in part by the Science and Technology Program of Shenzhen under Grant JCYJ20200109140601691. The review of this article was arranged by Editor D. Triyoso. (Corresponding author: Yushen Hu.)

Yushen Hu and Fei Wang are with the Department of Electronic and Computer Engineering, The Hong Kong University of Science and Technology, Hong Kong, China, and also with the School of Microelectronics, Southern University of Science and Technology, Shenzhen 518055, China (e-mail: yhuaz@connect.ust.hk).

Tengteng Lei and Yuqi Wang are with the Department of Electronic and Computer Engineering, The Hong Kong University of Science and Technology, Hong Kong, China.

Man Wong is with the Department of Electronic and Computer Engineering and the Shenzhen Research Institute, The Hong Kong University of Science and Technology (HKUST), Hong Kong, China (e-mail: eemwong@ust.hk).

Color versions of one or more figures in this article are available at https://doi.org/10.1109/TED.2022.3201836.

Digital Object Identifier 10.1109/TED.2022.3201836

![](images/028f571896a76b9e2061e59354976220ffc55d1b56a6344b8e32fefeb6dca53b.jpg)

![](images/5fd7fb724cc01fa09fedd03e68c7adc931283a0fce160b2463163644bbffe4a0.jpg)  
Fig. 1. Schematic hardware implementations of an ANN based on (a) resistive memory elements and (b) float-gate FETs.

in computational efficiency and an increase in power consumption with increasing size of an ANN [1], [2]. Significant effort has been spent on developing biomimetic hardware implementations of ANNs that more closely replicate the computation architecture of a mammalian brain, thus also emulating its adaptability and noise tolerance.

A range of hardware implementations of ANNs have been investigated. These include one consisting of resistive memory elements [see Fig. 1(a)] monolithically integrated with active-matrix addressing and computation circuits built using conventional complementary MOSFET technologies [3], [4]. While a variable synaptic weight can be readily emulated by the adjustable resistance of a memory element, the element presents its own technical challenges, such as local heating, parameter drift, and inadequate durability. Substituting the resistive memory elements by the technologically more mature floating-gate memory FETs [see Fig. 1(b)] also provides higher device stability and lower power consumption [5]. However, weight update by charge carrier injection into the floating gate of a memory FET [6] typically requires a high-voltage operation that demands a dedicated peripheral circuit. The speed of the updating process is often limited by a relatively low injection current.

The two- or three-port memory elements used in these implementations limit the selection of device terminals for the input signals. Consider the case of the relatively more versatile three-port floating-gate FET: the weight signal is typically loaded on the gate terminal to modulate the resistance of the channel, thus leaving only one of the source/drain (S/D) terminals for the coupling of the input signal. The relatively low impedance associated with such a terminal could result in the attenuation and distortion of the input signal. The same is true for ANN implementations based on two-port memory elements.

![](images/48160aba475c6213c06f0a00011fe1d33fe2b3518e62e11a7e0499685cedc373.jpg)

![](images/d0b16502ca6d09b77e0aa50b8febb1cebc76a484969946a2948ab1410783fe32.jpg)  
Fig. 2. (a) Schematic hardware implementations of an ANN based on serially connected DG FETs. Schematics of DG FETs with gate electrodes arranged in (b) series and (c) parallel.

The issue of low impedance has been addressed with the deployment of a dual-gate (DG) FET with serially connected gate electrodes [7]. While such a four-port FET [see Fig. 2(a)] is effective in providing a high direct-current (dc) impedance to a signal source that supplies the input or weight signals, its serial configuration of the gate electrodes limits the amplification of weak but relevant input signals because the total channel resistance consists of the sum of the serially connected input- and weight-signal modulated channel resistance [see Fig. 2(b)]. This drawback has been addressed with the deployment of a DG FET with parallelly connected gate electrodes [see Fig. 2(c)] [8].

At least a portion of the channel of a parallel, DG FET is sandwiched between two gate electrodes with high dc impedance. When the input and weight signals are separately applied on the electrodes, the potential of the channel is simultaneously modulated. Such modulation is best understood as the modulation by the weight signal of the apparent threshold voltage $V _ { \mathrm { t h } }$ “seen” by the input signal [9], thus capable of accommodating both the amplification of a weak but relevant input signal and the suppression of a strong but irrelevant input signal by, respectively, lowering and raising the apparent threshold voltage. Such thin-film transistors (TFTs) have recently been applied to the realization of [[neuromorphic]] logic gates [10]. Their deployment in the construction of an ANN is presently described.

The organization of the manuscript is as follows. The fabrication and characterization of the component TFTs making up an ANN are described in Section II. The design, operation, and application of an ANN are described in Section III. Finally, a conclusion is given in Section IV.

# II. DEVICE FABRICATION AND CHARACTERIZATION

Device fabrication [8], [10] starts on a wafer of n-type silicon covered with a 200-nm-thick thermally grown silicon oxide $( { \mathrm { S i O } } _ { x } )$ buffer layer [see Fig. 3(a)], and a layer of 100-nm-thick molybdenum (Mo) is sputter-deposited and patterned photolighographically to form the bottom gate electrodes of the TFTs and the bottom electrodes of the capacitors [see Fig. 3(b)]. A stacked insulator layer consisting of 50-nm-thick silicon nitride $( \mathrm { S i N } _ { y } )$ under a layer of 75-nm-thick $\mathrm { S i O } _ { x }$ is subsequently formed using plasmaenhanced chemical vapor deposition (PECVD) [see Fig. 3(c)].

![](images/5aeca1567d12e707f880fa76c8b1c085b7d9dedcc96a28791b36421b9472bd71.jpg)  
Fig. 3. Process flow of DG (left) and single-gate (center) TFTs, and a storage capacitor (right). (a) Growth of $\mathsf { S i O } _ { x }$ buffer layer, (b) patterning of Mo bottom gate electrodes, (c) deposition of $\mathsf { S i N } _ { y } \dot { } \mathsf { S i O } _ { x }$ bottom gate dielectrics, (d) deposition and pattering of [[IGZO]] active layer, (e) formation of the $\mathsf { S i O } _ { x }$ top gate dielectrics, (f) patterning of ITO top gate electrode, (g) deposition o $\mathsf { \bar { s s } } _ { \mathsf { i O } _ { x } }$ passivation layer, (h) opening of contact holes, and (i) patterning of Al on Mo interconnects.

This is followed by the sputter-deposition and patterning of a 20-nm-thick layer of indium–gallium–zinc oxide (IGZO), a metal–oxide semiconductor, to form the active layers of the TFTs and the counterelectrode of a capacitor [see Fig. 3(d)].

A second layer of 50-nm-thick PECVD $\mathrm { S i O } _ { x }$ is subsequently deposited and combined with the existing 50-nmthick layer of SiOx to form a 100-nm thick top-gate insulator [see Fig. 3(e)]. A 40-nm-thick layer of indium–tin oxide (ITO) is then sputter-deposited and patterned to form the top-gate electrode [see Fig. 3(f)] of a DG TFT. A third 200-nmthick layer of PECVD SiOx passivation layer is deposited [see Fig. 3(g)] before the opening of the contact holes [see Fig. 3(h)]. Electrical interconnects composed of 50-nm-thick layer of Mo under a 300-nm-thick layer of aluminum (Al) is

![](images/4842c281332f49f7d75aababd2b5a58228e6cfcc4ba00b893086ff987ec10006.jpg)

![](images/66a4849848769f37462a52655fd234a2e9efc5eb841bedadc6be67c779c513c9.jpg)

![](images/bdfebfe33c05650689554763a46706a5ab567fa8f186b8b049cf3669c3be502e.jpg)

![](images/6d7c364721ff0040cc9ac502beb6ef406ba7a9cbc49a0e89156c253ef36a1ec4.jpg)  
Fig. 4. Transfer characteristics of (a) single and (b) DG TFTs. Output characteristics of (c) single and (d) DG TFTs.

sputter-deposited and patterned [see Fig. 3(i)]. A final thermal treatment for 180 min in oxygen at $4 0 0 \mathbf { n } \ ^ { \circ } \mathbf { C }$ is performed to activate by reducing the resistivity of the S/D regions of the TFTs and the counterelectrode of the capacitor.

The drain current $I _ { D }$ versus bottom-gate voltage $V _ { G }$ transfer characteristics of a single-gate and a parallel DG TFTs, both with channel length L and width W of 20 μm, are shown, respectively, in Fig. 4(a) and (b). The respective $I _ { D }$ versus drain voltage $V _ { D }$ output characteristics are shown in Fig. 4(c) and (d). Due to the limitation of the measurement setup, the actual leakage current in the OFF-state of a TFT is much smaller [11] than that displayed. More importantly, it can be seen [see Fig. 4(b)] that the characteristics of the DG TFT can be parallelly shifted by an applied top-gate bias $V _ { \mathrm { T G } }$ . With the resulting $V _ { \mathrm { t h } }$ “seen” by the bottom-gate spanning both positive and negative values. It is for this reason that a parallel DG TFT can amplify a weak but relevant and suppress a strong but irrelevant input signal applied on the bottom gate, a feat that would be difficult to accomplish using a serially connected DG TFT.

The voltage-transfer characteristics of an inverter emulating a nonlinear, threshold-based, activation function (AF) controlling the firing of a neuron are displayed in Fig. 5(a), showing how the transition threshold $V _ { M }$ (i.e., the input voltage $V _ { \mathrm { { I n } } }$ at output voltage $V _ { \mathrm { O u t } } = 2 . 5 \ \mathrm { V } )$ can be modulated between 3 and 8 V by changing VTG applied on the top gate of the pull-down DG TFT from −13 to −8 V [see Fig. 5(b)]. It has already been reported that the storage of charge on the capacitor is pseudostatic because of the low OFF-state leakage current $( < 1 0 ^ { - 1 8 } \mathrm { ~ A ~ }$ per μm of channel width) of the accompanying address TFT built on IGZO [11].

# III. DESIGN AND OPERATION OF AN ANN

Shown in Fig. 6 is the schematic of an ANN with n inputs and m outputs. The ANN consists of (1) an $m \ \times \ n$ array of “units” that emulates the comprehensive connectivity and the in-memory threshold-based computation of a mammalian brain and (2) an $m \ \times \ 1$ column of inverters

![](images/7de485fee8b6d6b6a622b91c657f7cd4736ed619e3ca6ead5b5d2c88bfae3fa8.jpg)

![](images/287a1ff7c37c86e343582f2b803e72a94e0d4d44ff1df46fabd8cd5f7d42ea1e.jpg)  
Fig. 5. (a) Voltage-transfer characteristics of an inverter emulating a threshold-based firing AF. (b) Dependence of $V _ { M }$ on $V _ { \mathsf { T G } }$ .

![](images/ad62f0dc5b6b33c4aec2d4a25f157c0b5f7e88cf9f8a921613c781f791f5960b.jpg)  
Fig. 6. Schematic of an m × n ANN.

executing a threshold-based $\mathbf { \ddot { s } } _ { \mathbf { A F } } , \mathbf { \vec { \mathbf { \pi } } }$ that emulates the “firing” of neurons [12]. With α and $\beta$ indexing, respectively, one of the m rows and one of the n columns of the array, each unit $\mathrm { P } ( \alpha , \beta )$ consists of a single-gate TFT $M _ { \alpha \beta }$ for accessing a storage capacitor $C _ { \alpha \beta }$ , on which a weight signal $V _ { W a \beta }$ is stored and a DG TFT $D _ { \alpha \beta }$ for computing an output that contains the product of the weight and the input signals.

During a weight-writing operation involving a specific column $\beta ~ = ~ \beta _ { s }$ , the voltage $V _ {  { \mathrm { S c a n } }  { \beta _ { s } } }$ on line Scanβs and the voltage on the remaining scan lines $\beta \ \ne \ \beta _ { s }$ are set, respectively, above and below the threshold voltage of the TFTs $M _ { \alpha \beta }$ . Consequently, TFTs $M _ { \alpha \beta _ { s } }$ are turned on, and the respective weight signals $V _ { W \alpha \beta _ { s } }$ on lines $\mathrm { W t } _ { \alpha }$ are stored on capacitors $C _ { \alpha \beta _ { s } }$ . Since TFTs $M _ { \alpha \beta }$ for $\beta \neq \beta _ { s }$ are turned off, these signals are not stored on capacitors $C _ { \alpha \beta }$ for $\beta \neq \beta _ { s }$ . This operation is repeated for all $\beta$ from 1 to n to store the respective $V _ { W \alpha \beta }$ on all of $C _ { \alpha \beta }$ .

The channel impedance of each DG TFT $D _ { \alpha \beta }$ operating in the saturation regime is simultaneously controlled by $V _ { W \alpha \beta }$ and the input signal $V _ { \mathrm { I n } \beta }$ and depends in part on the product of the two. The $D _ { \alpha \beta }$ TFTs in row α tied to the source of pull-up TFT $U _ { \alpha }$ behave as resistors connected in parallel, thus emulating an accumulation (summation) operation. The “weighted sum” of this node is the input of the inverter $\operatorname { A F } _ { \alpha }$ performing a

![](images/f8331010fd09a089066a234e278612a276ee7bf97369dfcd7fc3cadddf284d43.jpg)  
Fig. 7. Schematic of the peripheral circuit driving an $m \times n \mathsf { A N N }$

threshold-based, neuron-firing AF. The output signal $V _ { \mathrm { O u t } a }$ of $\operatorname { A F } _ { a }$ appears in line Outα.

The peripheral circuit for driving the ANN is schematically shown in Fig. 7. The digital-to-analog converter (DAC) ports from a microcontroller unit (MCU, STM32F407ZGT6) supply the input and weight signals. These analog signals are written into the ANN using the respective demultiplexers DeMUX-I and DeMUX-W. A relatively large 10-pF capacitor is provided at each output of the DeMUXs to minimize signal attenuation due to capacitive loading. The output signals of the ANN are fed into the analog-to-digital converter (ADC) port of the MCU using a multiplexer MUX. Other digital ports, such as Ctrl1, Ctrl2, and Ctrl3, are used to control the operation of the DeMUXs and the MUX; Scan1 and Scan2 are used for controlling the weight-writing operations. The dc power supplies BiasU, BiasA, VDD, VCOM, and GND are used to bias the ANN.

As a demonstration, a 4 × 6 ANN is fabricated for the recognition of a set of four designated Tetris patterns. Each pattern is obtained by placing four solid shapes of $ [ \mathbf { \overline { { \mathbf { \overline { { \Pi } } } \mathbf { \overline { { \Pi } } } } } } ]  \mathbf { \overline { { \mathbf { \Pi } } } }  ,$ in a $3 ~ \times ~ 2$ array of possible locations. The six locations are labeled $L _ { 1 } , L _ { 2 } , . . . ,$ to $L _ { 6 } ,$ with each assigned a logic value of 0 or 1 depending, respectively, on the absence or presence of a shape at each location. A code word for a pattern, such as (0 0 1 1 1 1) for Pattern #1 in Fig. 8(a), is obtained by arranging the assigned values in a row. The code words for all four designated patterns are shown in Fig. 8(b). When fed as inputs to the ANN, the 0s and 1s of a code word are represented, respectively, by 0 V and a “high” voltage of $V _ { H }$ in a six-component input vector $[ V _ { \mathrm { I n } \beta } ]$ .

Consisting of $[ V _ { \mathrm { I n } \beta } ]$ , a $4 \times 6$ weight matrix $\left[ V _ { W \alpha \beta } \right]$ , and an output vector $\left[ V _ { \mathrm { O u t } a } \right]$ , the data structure associated with the ANN is schematically shown in Fig. 9.

Employing the gradient descent technique [13], [14], the ANN is trained using a training set $\{ [ V _ { \mathrm { I n } \beta } ] \}$ consisting of the

![](images/59c19475a407ba8852a87950b065355f309218a7e22f9f41fb150289f9b23221.jpg)

![](images/2cd5d8a54be700ef7897055b5887f3b68c0866028d72db097b0d7ed75623d39b.jpg)  
Fig. 8. Generation of (a) code word of a Tetris pattern and (b) those of all four designated patterns.   
Fig. 9. Data structure of $\approx 4 \times 6 \mathsf { A N N } .$

TABLE I DESIGNATED PATTERNS AND THEIR CORRESPONDING $[ \hat { V } _ { \mathrm { O U T } \alpha } ]$   

<table><tr><td>Input code word</td><td>[ˆVOutα]</td></tr><tr><td>#1</td><td>(VH,0,0,0)</td></tr><tr><td>#2</td><td>(0, VH,0,0)</td></tr><tr><td>#3</td><td>(0,0, VH,0)</td></tr><tr><td>#4</td><td>(0,0,0, VH)</td></tr></table>

four designated patterns shown in Fig. 8(b). Summarized in Table I is the desired $\left[ V _ { \mathrm { O u t } a } \right]$ (denoted by $[ \hat { V } _ { \mathrm { O u t } \alpha } ] )$ when the designated patterns are properly classified by a trained ANN.

Denoted by vector in traithe measured $[ V _ { W a \beta } ^ { \{ p \} } ]$ ight matrix and  In general, the from those o $\dot { [ } V _ { \mathrm { O u t } a } ^ { \{ p \} }$ he outputonents oflisted in $p .$ $[ V _ { \mathrm { O u t } \alpha } ^  \mp p \} ]$ $[ \hat { V } _ { \mathrm { O u t } a } ]$ Outα  Table I. One computes a “cost function” $J ^ { \{ p \} } ( [ V _ { W \alpha \beta } ^ { \{ p \} } ] )$ for Epoch p

$$
J ^ {\{p \}} \left(\left[ V _ {W \alpha \beta} ^ {\{p \}} \right]\right) \equiv \sum_ {\alpha = 1} ^ {4} J _ {\alpha} ^ {\{p \}} \tag {1}
$$

where J { p} α ≡  [VInβ ] ( $\begin{array} { r } { J _ { \alpha } ^ { \{ p \} } \equiv \sum _ { [ V _ { \mathrm { I n } \beta } ] } ( V _ { \mathrm { O u t } \alpha } ^ { \{ p \} } - \hat { V } _ { \mathrm { O u t } \alpha } ) ^ { 2 } } \end{array}$ V { p} is the sum of the squares of the “errors” with an initial guess of s of is u $\{ [ V _ { \mathrm { I n } \beta } ] \}$ $[ V _ { W \alpha \beta } ^ { \{ 0 \} } ] , [ V _ { W \alpha \beta } ^ { \{ p \} } ]$ gradient descent technique until $J ^ { \{ p \} }$ is minimized. The $" a \beta "$ component of the gradient of $J ^ { \{ p \} }$ is estimated by

$$
\frac {\partial J ^ {\{p \}}}{\partial V _ {W \alpha \beta} ^ {\{p \}}} \approx \frac {J ^ {\{p \}} \left(\Delta V _ {W}\right) - J ^ {\{p \}}}{\Delta V _ {W}} \tag {2}
$$

TABLE II PARAMETER VALUES OF THE ANN   

<table><tr><td>V_H</td><td>5 V</td></tr><tr><td>K</td><td>10</td></tr><tr><td>ΔVw</td><td>0.2 V</td></tr><tr><td>BiasU</td><td>2 V</td></tr><tr><td>BiasA</td><td>-8 V</td></tr><tr><td>VDD</td><td>5 V</td></tr><tr><td>VCOM</td><td>2 V</td></tr><tr><td>GND</td><td>0 V</td></tr></table>

$J ^ { \{ p \} } ( \Delta V _ { W } )$ is the computeince changes in function after does not affe $\Delta V _ { W }$ $V _ { W \alpha \beta } ^ { \{ p \} }$ $V _ { W \alpha \beta } ^ { \{ p \} }$ $V _ { \mathrm { O u t } \alpha ^ { \prime } } ^ { \{ p \} }$ $\alpha \neq \alpha ^ { \prime }$ $\Delta \dot { V } _ { W }$ of $[ \dot { V } _ { W \alpha \beta } ^ { \{ p \} } ]$ to obtain

$$
\frac {\partial J ^ {\{p \}}}{\partial V _ {W \alpha \beta} ^ {\{p \}}} \approx \frac {J ^ {\{p \}} \left(\Delta V _ {W}\right) - J ^ {\{p \}}}{\Delta V _ {W}} = \frac {J _ {\alpha} ^ {\{p \}} \left(\Delta V _ {W}\right) - J _ {\alpha} ^ {\{p \}}}{\Delta V _ {W}}. \tag {3}
$$

Consequently, the updated weight signal $V _ { W \alpha \beta } ^ { \{ p + 1 \} }$ f or the next epoch can be computed

$$
V _ {W \alpha \beta} ^ {\{p + 1 \}} = V _ {W \alpha \beta} ^ {\{p \}} - K \frac {J _ {\alpha} ^ {\{p \}} \left(\Delta V _ {W}\right) - J _ {\alpha} ^ {\{p \}}}{\Delta V _ {W}} \tag {4}
$$

where K denotes a learning rate. The settings of the parameters used in the present implementation are summarized in Table II.

Two different initial weight matrices $[ V _ { W a \beta } ^ { \{ 0 \} } ] _ { 1 }$ and $[ V _ { W \alpha \beta } ^ { \{ 0 \} }$ are investigated: $[ V _ { W a \beta } ^ { \{ 0 \} } ] _ { 1 } = ( 0 )$ with all elements set to logic value 0 and $[ V _ { W a \beta } ^ { \{ 0 \} } ] _ { 2 }$ Wαβ  with the elements set to logic values of

$$
\left[ V _ {W \alpha \beta} ^ {\{0 \}} \right] _ {2} = \left( \begin{array}{c c c c c c} 0 & 0 & 1 & 1 & 1 & 1 \\ 1 & 0 & 1 & 1 & 0 & 1 \\ 1 & 1 & 1 & 0 & 1 & 0 \\ 1 & 0 & 1 & 1 & 1 & 0 \end{array} \right). \tag {5}
$$

Note that each row of $[ V _ { W a \beta } ^ { \{ 0 \} } ] _ { 2 }$ simply corresponds to one corresponding to logic value $" 1 "$ is set at $V _ { \mathrm { C O M } } = 2 \mathrm { ~ V ~ } [ 1 5 ]$ . $J ^ { \{ p \} }$ wn in Fig. 10 is tcorresponding to $[ V _ { W a \beta } ^ { \{ 0 \} } ] _ { 1 }$ ured and $[ V _ { W a \beta } ^ { \{ 0 \} } ] _ { 2 }$ nce trends of. Clearly, the convergence is slower (∼17 epochs) using $[ V _ { W a \beta } ^ { \{ 0 \} } ] _ { 1 }$ than that (∼10 epochs) using $[ V _ { W a \beta } ^ { \{ 0 \} } ] _ { 2 }$ .

The training is repeated 50× for each of the two proposed initial guesses, and the values of the 24 components of the final $\left[ V _ { W a \beta } \right]$ are recorded. As an illustration, histograms of $V _ { W 3 1 }$ r unit P(3, 1) are shown in Fig. 1and Fig. 11(b) for initial guess initial guess. The same $[ V _ { W a \beta } ^ { \{ 0 \} } ] _ { 1 }$ $[ V _ { W \alpha \beta } ^ { \{ 0 \} } ] _ { 2 }$ statistical analysis has been performed for all 24 components, and the resulting average values and standard deviations of $V _ { W \alpha \beta }$ are shown in Fig. 11(c). The standard deviation is on the order of 0.5 V, largely independent of the average values. From the similarity between the final gray-scale maps of the weight signals shown in Fig. 10 and the distribution of the weight signals shown in Fig. 11(c), it is evident that the values

![](images/f362163ad8582027f9f822bd0db6990054b88bf9bfa6065237b606a88afed882.jpg)  
Fig. 10. Cost function versus training epochs with two different initial weight matrices. Shown also are the gray-scale maps of the initial and final weight signals.

![](images/3b6931d2eb1a19ab61a7db94997771f54c521e8c419af1e152f815bb85b4ea18.jpg)  
(a)

![](images/04ee4e01065af228c8c62ba8a0452b184da1c253496d04a66153575bcad58328.jpg)  
(b)

![](images/730d8ecb4bf9cc3c20f9902e8c79a4191e0e901f4c33c88ea72fcaf0242e600a.jpg)  
(c)   
10 12 14 16 18 20 22 24 Weight ID   
50 training runs starting with (a) Fig. 11. Relative frequency of the weight signals of unit P(3, 1) from $[ V _ { W \alpha \beta } ^ { \{ 0 \} } ] \cdot$ and $( \mathsf { b } ) [ V _ { W \alpha \beta } ^ { \{ 0 \} } ]$ 2 (o Disrution from 50 training runs starting with of the average values and the standard deviations of all 24 weight signals $[ V _ { W \alpha \beta } ^ { \{ 0 \} } ] _ { 1 }$ $[ V _ { W \alpha \beta } ^ { \{ 0 \} } ] _ { z }$ 2：

of $\left[ V _ { W a \beta } \right]$ after convergence are relatively independent of the choice of the two $[ V _ { W \alpha \beta } ^ { \{ 0 \} } ] \mathrm { s }$ .

The ANN trained using the set of four designated patterns is deployed to infer the classification of elements of an inference set containing all possible patterns consisting of three or four shapes. A percentage figure-of-merit $\eta _ { \alpha }$ is computed for each row α of the output according to

$$
\eta_ {\alpha} \equiv \frac {V _ {\mathrm {O u t} \alpha}}{V _ {H}} \times 100 \% \tag{6}
$$

![](images/0c4c209b06d72cbc93426f92af67b8f590e56d95ae9d83fd4649efb2e3b3a059.jpg)  
Fig. 12. Gray-scale map showing the inference outcome of all patterns containing three or four solid shapes. The four designated patterns are labeled.

and displayed in Fig. 12 in the form of a gray-scale map. Clearly, the ANN is capable of distinguishing the four designated elements (see Fig. 8) from the other elements of the inference set.

# IV. CONCLUSION

A low-temperature technology capped by a peak processing temperature of 400 ◦C and based on IGZO, a popular metal–oxide semiconductor, for the construction of an ANN consisting of monolithically integrated capacitors as memory elements and parallel, DG TFTs as computing elements has been described. At least, a portion of the channel of such a TFT is sandwiched between its two gate electrodes. Based on this technology, a demonstration ANN has been constructed and trained to recognize a set of designated Tetris patterns. The technology can be readily applied to realize ANNs of higher complexity.

# ACKNOWLEDGMENT

Microfabrication was done at the Nanosystem Fabrication Facility of The Hong Kong University of Science and Technology, Hong Kong.

# REFERENCES

[1] M. Prezioso, F. Merrikh-Bayat, B. D. Hoskins, G. C. Adam, K. K. Likharev, and D. B. Strukov, “Training and operation of an integrated neuromorphic network based on metal-oxide memristors,” Nature, vol. 521, pp. 61–64, Dec. 2015, doi: 10.1038/nature14441.   
[2] Y. van de Burgt, A. Melianas, S. T. Keene, G. Malliaras, and A. Salleo, “Organic electronics for neuromorphic computing,” Nature Electron., vol. 1, no. 7, pp. 386–397, Jul. 2018, doi: 10.1038/s41928-018-0103-3.   
[3] Y. P. Lin et al., “Physical realization of a supervised learning system built with organic memristive synapses,” Sci. Rep., vol. 6, no. 1, pp. 1–12, Sep. 2016, doi: 10.1038/srep31932.   
[4] V. A. Demin et al., “Hardware elementary perceptron based on polyaniline memristive devices,” Organic Electron., vol. 25, pp. 16–20, Oct. 2015, doi: 10.1016/j.orgel.2015.06.015.   
[5] E. J. Fuller et al., “Parallel programming of an ionic floating-gate memory array for scalable neuromorphic computing,” Science, vol. 364, no. 6440, pp. 570–574, May 2019, doi: 10.1126/science.aaw5581.   
[6] X. Yang et al., “Mechanoplastic tribotronic floating-gate neuromorphic transistor,” Adv. Funct. Mater., vol. 30, no. 34, Jul. 2020, Art. no. 2002506, doi: 10.1002/adfm.202002506.   
[7] S. Ma et al., “An artificial neural network chip based on two-dimensional semiconductor,” Sci. Bull., vol. 67, no. 3, pp. 270–277, Feb. 2022, doi: 10.1016/j.scib.2021.10.005.   
[8] T. Lei, R. Shi, Y. Wang, Z. Xia, and M. Wong, “A comparative study on inverters built with dual-gate thin-film transistors based on depletion—Or enhancement-mode technologies,” IEEE Trans. Electron Devices, vol. 69, no. 6, pp. 3186–3191, Jun. 2022, doi: 10.1109/TED.2022.3167940.   
[9] H. W. Zan, W. T. Chen, C. C. Yeh, H. W. Hsueh, C. C. Tsai, and H. F. Meng, “Dual gate indium-gallium-zinc-oxide thin film transistor with an unisolated floating metal gate for threshold voltage modulation and mobility enhancement,” Appl. Phys. Lett., vol. 98, no. 15, Mar. 2011, Art. no. 153506, doi: 10.1063/1.3578403.   
[10] Y. Hu, Y. Wang, T. Lei, F. Wang, and M. Wong, “Neuromorphic implementation of logic functions based on parallel dual-gate thin-film transistors,” IEEE Electron Device Lett., vol. 43, no. 5, pp. 741–744, May 2022, doi: 10.1109/LED.2022.3164684.   
[11] Y. Wang, Z. Xia, and M. Wong, “Characterization of the off-state current of an elevated-metal-metal-oxide thin-film transistor,” in SID Symp. Dig. Tech. Papers, vol. 52, Feb. 2021, pp. 413–416, doi: 10.1002/sdtp.14505.   
[12] Y. Wang, Y. Li, Y. Song, and X. Rong, “The influence of the activation function in a convolution neural network model of facial expression recognition,” Appl. Sci., vol. 10, no. 5, p. 1897, Mar. 2020, doi: 10.3390/app10051897.   
[13] T. P. Lillicrap, A. Santoro, L. Marris, C. J. Akerman, and G. Hinton, “Backpropagation and the brain,” Nature Rev. Neurosci., vol. 21, pp. 335–346, Jun. 2020, doi: 10.1038/s41583-020-0277-3.   
[14] Y. Yao, L. Rosasco, and A. Caponnetto, “On early stopping in gradient descent learning,” Construct. Approx., vol. 26, no. 2, pp. 289–315, 2007, doi: 10.1007/s00365-006-0663-2.   
[15] V. Dwivedi and B. Srinivasan, “A normal equation-based extreme learning machine for solving linear partial differential equations,” J. Comput. Inf. Sci. Eng., vol. 22, no. 1, Feb. 2022, Art. no. 014502, doi: 10.1115/1.4051530.