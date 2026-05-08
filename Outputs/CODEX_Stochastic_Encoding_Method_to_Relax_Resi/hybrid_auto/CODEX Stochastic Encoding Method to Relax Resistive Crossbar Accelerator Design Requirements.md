---
title: "CODEX: Stochastic Encoding Method to Relax Resistive Crossbar Accelerator Design\\"
authors:
  - "Tony Liu"
  - "Amirali Amirsoleimani"
  - "Jianxiong Xu"
  - "Fabien Alibart"
  - "Yann Beilliard"
  - "Serge Ecoffey"
  - "Dominique Drouin"
  - "Roman Genov"
date: "2022‑03‑08"
year: 2022
journal: "IEEE Transactions on Circuits and Systems II: Express Briefs"
doi: "10.1109/TCSII.2022.3157789"
abstract: "A stochastic input encoding scheme (CODEX) is presented that aims to relax the analog‑to‑digital\\"
abstract_cn: "提出一种随机输入编码方案 CODEX，旨在降低忆阻器交叉阵列系统中模数转换器的设计需求。CODEX 通过使用伯努利统计对输入比特进行编码，使位线电流分布变为窄高斯分布，从而减小\\"
keywords:
  - "[[CODEX]]"
  - "[[Stochastic encoding]]"
  - "[[Memristor crossbar]]"
  - "[[Analog‑to‑digital converter]]"
  - "[[In‑situ training]]"
cite: "[1] Liu T, Amirsoleimani A, Xu J, et al. CODEX: stochastic encoding method to relax\\"
aiSum: "提出随机输入编码方案 CODEX，通过伯努利统计编码将位线电流分布压缩为窄高斯分布，降低 ADC 输入范围，实现 ADC 功耗降低 68.5%、面积降低 35.5%、原位训练周期数降低\\"
confidence: medium
---

# CODEX: Stochastic Encoding Method to Relax Resistive Crossbar Accelerator Design Requirements

Tony Liu , Amirali Amirsoleimani , Member, IEEE, Jianxiong Xu, Graduate Student Member, IEEE, Fabien Alibart, Yann Beilliard, Serge Ecoffey , Member, IEEE, Dominique Drouin , Member, IEEE, and Roman Genov , Senior Member, IEEE

Abstract—A stochastic input encoding scheme (CODEX) is presented that aims to relax the analog-to-digital converter (ADC) design requirements in memristor crossbar systems. CODEX reduces the ADC input range by encoding the input bits using Bernoulli statistics so that the bit-line current distribution becomes a narrow Gaussian. By reducing ADC input range, CODEX can be used to reduce ADC power and area or increase ADC resolution to reduce the number of epochs required for in-situ training. Besides input data encoding, CODEX includes probability thresholding for sparse input data as well as a random re-sampling method for dealing with ADC overflow. CODEX is evaluated on CIFAR-10 dataset image classification and reconstruction, sentiment classification, and audio classification. The results show an averaged 68.5% reduction in ADC power, 35.5% reduction in ADC area, and 25.8% reduction in training epochs required for in-situ training when applied to the state-of-the-art ISAAC and PUMA accelerators.

Index Terms—Memristor, analog-to-digital converter, vectormatrix multiplication, inference, deep neural network.

# I. INTRODUCTION

R ESISTIVE crossbars based on non-volatile memo-ries have garnered increased attention as low-power and high-speed approximate computing accelerators for a variety of computationally-intensive applications including deep neural networks (DNNs) [1]–[5] and neuromorphic computing [6]–[9]. Memristor crossbars perform vectormatrix multiplication (VMM) by mapping a N × M matrix onto the memristors’ conductance range, applying an input voltage vector to the rows, and then sensing the current from the columns. Although, memristor crossbars can significantly

Manuscript received 25 August 2021; revised 17 October 2021; accepted 1 March 2022. Date of publication 8 March 2022; date of current version 1 August 2022. This work was supported in part by NSERC HIDATA Project and in part by ERC-CoG IONOS under Grant 773228. This brief was recommended by Associate Editor E. Vianello. (Corresponding authors: Amirali Amirsoleimani; Roman Genov.)

Tony Liu, Amirali Amirsoleimani, Jianxiong Xu, and Roman Genov are with the Edward S. Rogers Sr. Department of Electrical and Computer Engineering, University of Toronto, Toronto, ON M5S 1A1, Canada (e-mail: amirali.amirsoleimani@utoronto.ca; roman.genov@utoronto.ca).

Fabien Alibart, Yann Beilliard, Serge Ecoffey, and Dominique Drouin are with the Department of Electrical and Computer Engineering, University of Sherbrooke, Sherbrooke, QC J1K 2R1, Canada.

Color versions of one or more figures in this article are available at https://doi.org/10.1109/TCSII.2022.3157789.

Digital Object Identifier 10.1109/TCSII.2022.3157789

increase energy, storage and area efficiency, peripheral input and output circuits will impose a considerable cost [10], [11].

Normally, peripheral circuits consume most of the total power (> 90%) with analog-to-digital converters (ADCs) in particular making up over 57% of peripheral circuit power in such platforms [12]. Such ADCs consume higher energy and area in comparison with resistive array and finding appropriate techniques to reduce their design costs will be critical to improve the resistive VMM platform performance metrics. One common method to relieve ADC design constraints include bit-slicing of weights [13] where a single high-resolution weight is split and mapped onto multiple lower-resolution memristors. Lowering the bit-resolution of the memristors decreases the number of possible output current quantized levels, which allows for the usage of lower resolution ADCs without hurting the computational accuracy. While effective in reducing ADC resolution requirements, bit-slicing results in severe area overhead. The work in [14] utilizes a quantization algorithm that compresses DNNs to relax ADC resolution constraints in ML applications. In [15], [16] input encoding methods to reduce the input range of the ADC has been presented. However, the encoded inputs in [15], [16] have log (N/2) additional bits where N is the number of rows of the crossbar. These extra input bits can entail a heavy cost in terms of system speed and throughput when used on larger crossbars.

# II. BIT-SERIAL VMM AND ADC CHARACTERISTICS

In order to perform VMM on a memristor crossbar system, the input data must be converted into a series of voltage signals (Fig. 1(a)). Typically, the most significant bits (MSBs) which hold most of the information will be heavily correlated as shown in Fig. 1(b) while the least significant bits (LSBs) are usually mostly independent as shown in Fig. 1(c). Similarly, the distribution of memristor resistances on the crossbar can vary greatly as can be seen in a small sample of 20 low resistance memristors in Fig. 1(a). The typical sensing circuit for the memristor array usually consists of trans-impedance amplifier (TIA) and ADC [11], in which the TIA converts the memristor array output current to voltage that is digitized by ADC . To discern all possible output states, J bit ADCs are required where $J = I + W + l o g _ { 2 } ( N + 1 )$ . Here, I and W represent the bit-resolution of the input voltage signals and the memristors, respectively, while N is the number of rows.

![](images/7a01ec587bed041b65529dd543255444b560c4ea108bcd44d990da3265f3c683.jpg)  
（c）

![](images/553fc1e7e75463380cce207876a05677c68356ef06d4470d6a9bdd75ce0d47e9.jpg)

![](images/5f6f090cbb8f1307ae5f6f1a550616b48c2ed31fc637cedb1b7ebb9f7e75b69a.jpg)  
(d)   
Fig. 1. (a) Memristor crossbar vector-matrix multiplication (VMM) input pipeline. (b) Sample correlation heat map of the most significant input bit. (c) The memristor crossbar array classification accuracy on the MNIST dataset for a given ADC resolution. (d) The relationship among the ADC resolution, memristor cell per ADC and memristor accuracy.

However, most typical ML applications do not need to discern between all possible output states and only require a moderateto-high (8-10 bit) ADC resolution in order to achieve good accuracy as shown in Fig. 1(c). Fig. 1(d) shows the relationship between the required ADC ENOB and the number of memristors per ADC where RS is defined as resistive state. The required resolution of the ADC is linearly proportional to the product of the number of memristors per ADC and the memristor resolution.

# III. METHODOLOGY

# A. Stochastic Input Modulation

Fig. 2(a) introduces CODEX, which stochastically modulates the input data by adding a randomly-generated binary input vector to each in order to decorrelate the input bits from each other. After CODEX is applied, the decoupled encoded input bits can be modelled as independent, non-identical random Bernoulli variables. As such, the output currents for each column are represented as a weighted sum of N bernoulli variables: $\begin{array} { r } { I _ { j } = \sum _ { i } ^ { \tilde { N } } w _ { i , j } b _ { i } ( p ) } \end{array}$ where N is the number of rows on the crossbar. Here, $I _ { j }$ is a random variable that represents the current in the j-th column, $w _ { i , j }$ is the conductance of the i-th row, j-th column memristor, and the i-th row input. The mea $b _ { i } ( p )$ $I _ { j }$ is the bernois given as $\begin{array} { r } { \mu _ { j } = \sum _ { i } ^ { N } p _ { i } w _ { i , j } } \end{array}$ with variance $\begin{array} { r } { \bar { \sigma } _ { j } ^ { 2 } = \sum _ { i } ^ { N } p _ { i } ( 1 - p _ { i } ) \bar { w } _ { i , j } ^ { 2 } } \end{array}$ where $p _ { i }$ i is the probability of $b _ { i } ( p )$ being 1. As $N \to \infty$ , the Lyapunov Central Limit Theorem (CLT) can be applied because Lyapunov’s condition is satisfied by $I _ { j }$ for $\delta = 1$ . Here, $s _ { n } ^ { 2 } = \dot { \sum _ { i } ^ { N } \sigma _ { i } ^ { 2 } }$ and $b _ { i } ( p )$ is defined as the bernoulli variable for the i-th row input. As a result, $I _ { j } \sim \mathcal N ( \mu _ { j } , \sigma _ { i } ^ { 2 } )$ as $N \to \infty$ .

Without CODEX, the input features will likely be correlated with each other and fail to satisfy the conditions of the CLT and as such, a normal output distribution is not guaranteed. As a result, practical memristor crossbar applications will have to consider a much larger bit-line current range than with CODEX where a normal output distribution can be assumed safely. The general flowchart of using CODEX in in-situ and ex-situ applications is shown in Fig. 2(b). The binary input matrix $\bar { \textbf { X } } \in \mathbb { R } ^ { N \times k }$ is modulated by adding random binary

matrix $\mathbf { U } \in \mathbb { R } ^ { N \times k }$ such that $\mathbf { X } ^ { \prime } = \mathbf { X } + \mathbf { U }$ where $\mathbf { X } ^ { \prime } \in \mathbb { R } ^ { N \times ( k + 1 ) }$ . The random encoding matrix U is sampled from a Bernoulli distribution with $P ( \mathbf { U } _ { i j } = 1 ) = 0 . 5$ as illustrated in Fig. 2(c). The modulated input $\mathbf { X ^ { \prime } }$ is then fed into the memristor crossbar as voltage pulses and the output current is recorded by the ADCs. The intended output current for the m-th bit, $X _ { m } \mathbf { G } ,$ , can be recovered by subtracting $U _ { m } \mathbf { G }$ from the recorded output current: $X _ { m } \mathbf { G } \ = \ I _ { m } - U _ { m } \mathbf { G }$ where $I _ { m }$ is the output current of the m-th column and G is a matrix that represents the conductances of the memristor crossbar.

We found in testing that randomly generating ten fixed U matrices beforehand is sufficient to produce a roughly normal output current distribution for practical applications and allows for UG to be calculated for every $\mathbf { U } \in U ^ { * }$ beforehand with negligible overhead. During in-situ training, UG will need to be recalculated at each update step. Assuming a typical batch size of 128, this would result in under 7.8% time overhead. To reduce this overhead, CODEX can use a smaller pool of encoding matrices, larger batch size, and/or recompute UG every several update steps instead of every update step.

# B. Sparse Input Optimization and ADC Overflow

Each element $x _ { i j }$ in the X input matrix has a probability $p _ { i j }$ of being one. Ignoring carry-over from previous bit columns, the probability of modulated input X’ being one can be formulated as:

$$
P \left(x _ {i j} ^ {\prime} = 1\right) = \left\{ \begin{array}{l l} p _ {i j}, & \text {i f} u _ {i j} = 0 \\ 1 - p _ {i j}, & \text {i f} u _ {i j} = 1 \end{array} \right. \tag {1}
$$

To estimate $p _ { i j } .$ a random sample of the input can be taken and the relative frequency of ones can be used to approximate $p _ { i j } .$ To keep crossbar power low, we want to reduce the frequency of non-zero input voltage pulses. In others words, we would like to keep minimize $P ( x _ { i j } ^ { \prime } = 1 ) = p _ { i j } ^ { \prime }$ for all i and $j .$ To address this issue, we propose a probability threshold illustrated in Fig. 2(d) where if $p _ { i j }$ is less than the threshold $^ { t h , }$ then $u _ { i j } = 0$ . This probability threshold prevents low $p _ { i j }$ from being randomly flipped into high $p _ { i j } .$ , thus, preventing any significant increase in average bit-line current. In addition,

![](images/50065e0e9503dcbf4140ebc901ad5f5e03b20363c9d26572a493f90057ee8660.jpg)

![](images/2e2ed0135250c27d8bd86625068313c0cf4a7a69e82e7c44105c9df499a11b26.jpg)

![](images/8128ded65e67c34b87b6987b8b99b7b08d19471e844b7a55437f4710fc823ce7.jpg)

![](images/ef3b35ee55113a543ed92336a065b5e4c3354fb196fd6b4dcfa29fa0fc2f3e8a.jpg)

![](images/f0d0faf2404a29ca7da46447c771431ca89413f72d28758cf5b8062019b63f55.jpg)  
Fig. 2. (a) CODEX encodes inputs randomly to normalize output distribution and reduce ADC input range. (b) CODEX in-situ and ex-situ usage flowchart. (c) Stochastic encoding matrix U is sampled from a Bernoulli distribution with an even probability distribution. (d) Threshold inputs by only randomizing non-sparse input bits to reduce average output current. (e) Prepare multiple spare CODEX encoding matrices to minimize ADC overflow probability.

![](images/f38c82d624282944f29fe1297b6ed82ec5c3363b056467782cdfedd36d2c447d.jpg)

![](images/b4b918fbb6ddaed1d757d2184f6f5524621deb862210e0c761c2c65510e03faf.jpg)  
Fig. 3. (a) CODEX is applied sequentially to the inputs of each layer of a DNN. (b) In-situ training accuracy curves with the total number of training steps compared between CODEX and baseline. (c) CODEX output current distributions with varying probability thresholds.

U remains random above th, keeping the output current distribution roughly normal. Assuming a normal output current distribution, there is a 4.55% chance that the output current falls outside 2σ of the mean and a 0.27% chance for the output to fall outside three σ .

A solution to this problem is to prepare multiple spare random encoding matrices to substitute in the case of an overflow. Let’s denote these random matrices as $\begin{array} { r l } { U ^ { * } } & { { } = } \end{array}$ $\{ \mathbf { U } _ { 1 } , \mathbf { U } _ { 2 } , \dots , \mathbf { U } _ { N } \}$ . Given an input matrix X, the output distribution for the k-th bit is $\begin{array} { r } { I _ { k } \ = \ \sum _ { i } ^ { N } ( X _ { i } + b ( 0 . 5 ) ) \cdot G _ { i j } } \end{array}$ . Assuming the probability that $I _ { k }$ falls outside the ADC input range is $p _ { o \nu e r } ,$ then the probability of every independent matrix $\mathbf { U } _ { i } ~ \in ~ U ^ { * }$ causing an ADC overflow is $( p _ { o v e r } ) ^ { N }$ as shown in Fig. 2(e). With a pool of 10 encoding matrices and a narrow sensing range of 2σ , the probability

of overflow for all ten encoding matrices is negligible $( 3 . 8 \times 1 0 ^ { - 1 2 } \% )$ .

# IV. RESULTS AND DISCUSSION

# A. CODEX Application and Performance Analysis

Fig. 3(a) shows CODEX is applied to a multi-layered neural network. Every layer in the network has a randomly assigned encoding matrix $\mathbf { U } _ { i }$ which is used to encode the input to the layer $( \mathbf { { X } } ^ { \backprime } { } _ { i } = \mathbf { { X } } _ { i } + \mathbf { { U } } _ { i } )$ and decode the subsequent output of the layer $( \mathbf { Y } ^ { \ast } { } _ { i } = \mathbf { Y } _ { i } - \mathbf { U } _ { i } \mathbf { G } _ { i } )$ . There are two main ways that crossbar systems can benefit from a reduction in ADC input range. First, the required bit resolution of the ADC can be reduced while maintaining the same distance between each ADC quantization level, which allows for the usage of lower

power and/or smaller area ADCs without hurting computational accuracy. Second, ADC resolution can be increased by using the same resolution ADC over the smaller input range. Fig. 3(b) shows an accuracy curve for a simple 2-layer neural network training on the MNIST digit classification task [17].

We can observe that CODEX reaches an acceptable accuracy of 90% after 96000 training images which is 30.2% faster than the baseline model. CODEX has a main parameter that need to be tuned before being applied to a crossbar system. First, we must consider the probability threshold when dealing with sparse input bits. Fig. 3(c) highlights the probability threshold’s effect on the output current distribution for the previously described 2-layer neural network on the MNIST dataset. Increasing the probability threshold decreases the average output current as intended with the most significant decrease occurring from th = 0 to th = 0.1 where the average current decreases by 0.63 mA.

# B. Results

In this brief, all simulations are performed using our extended 1T1R memristor crossbar simulation model [18] that includes the following memristor non-idealities: limited memristor programming precision, high and low conductance state noise for device-to-device variation, stuck-on and stuck-off memristors, and line resistances. In addition, CODEX is tuned to use a probability threshold of 0.35 and 2σ ADC sensing range around the mean output current for all applications.

To evaluate CODEX performance on existing crossbar systems, we apply it to the state-of-the-art ISAAC [19] and PUMA [20] accelerators. Both PUMA and ISAAC systems are complete crossbar architectures include a core VMM processing unit, where the memristor crossbar, DACs and ADCs reside in addition to a variety of other peripheral units In addition, PUMA and ISAAC have a variety of other peripheral units for data transfer, non-linear processing, and other tasks. PUMA adopts a similar core VMM processing units from ISAAC, but has slightly more VMM units than ISAAC resulting in slightly higher ADC power and area.

CODEX is tested on three datasets across four different applications: CIFAR-10 [21] for image classification and reconstruction, sentiment classification dataset [22], and Freesound dataset for audio classification [23]. Fig. 4(a-c,j) show the output current histograms across the four tasks for CODEX and the baseline system. While the baseline output distribution varies across the different tasks, the CODEX output distribution maintains a relatively consistent truncated normal distribution due to the ADC input range cutoff. On average, CODEX caused a 3.3× reduction in the range of output current CODEX with a max and minimum reduction of 2.37× and 4.16× for the sentiment analysis and CIFAR image reconstruction tasks, respectively. Fig. 4(d-f,l) examines the case where CODEX is used to reduce the number of epochs required for in-situ training to achieve high accuracy by increasing ADC resolution. After 100000 training images, the baseline model reaches an average validation accuracy 81.3% across the classification tasks. CODEX surpasses the final accuracy of the baseline model with 25.8% less training

![](images/476e20a37e759350023802da988966f49f3d607f85e5698f7da25082fb8c9c60.jpg)  
Fig. 4. (a-c,k) Baseline vs CODEX output histograms on (a) CIFAR image classification, (b) audio classification , (c) sentiment classification , and (j) CIFAR image reconstruction. (d-f) In-situ sample output predictions and training accuracy across tasks (a-c). (g-i,k) Improvements in energy metrics, area metrics, and max Signal to noise distortion ratio (SNDR) over baseline implementations [19], [20]. (l) In-situ cross entropy loss curve with sample output images.

images on average and was most effective for the CIFAR classification task where CODEX reaches the final baseline accuracy 33.6% faster after only 66400 training images. In Fig. 4(j), the CODEX and baseline loss curves follow roughly with CODEX having roughly 0.01 less binary cross entropy (BCE) error at all times. A look at the sample test outputs shown shows that CODEX consistently reconstructs noticeably clearer images than the baseline model. Fig. 4(g-i,k) shows the benefits to power, area, and Signal to noise distortion ratio (SNDR) when CODEX is used to reduce ADC design requirements when applied to the ISAAC and PUMA chip architectures.

Despite using the same ADC technology, ADC area and power consumption take up a different proportion of total area and power for ISAAC and PUMA which results in differences in total area and power improvement percentage despite using the same ADC technology. This effect is shown in Fig. 4(gi,k) where the ADC area and power improvement of ISAAC and PUMA are the same but the total area and power improvement percentage are different. When comparing energy (EE), storage (SE) and computational (CE) efficiency, we use 16-bit operations consistent with [20]. With lower ADC bit resolution, CODEX can be tuned between using an ADC with the same area as the baseline and lower power (CODEX-P), or an ADC with the same power as the baseline and lower area (CODEX-A). In both cases, the max SNDR is reduced because it is directly a function of ADC ENOB. From Table I, CODEX provides a 50.0% (PUMA-C) and 63.1% (ISAAC-C) increase in EE over the two baseline accelerators. PUMA-C

TABLE I COMPARISON OF CODEX WITH PREVIOUS WORKS   

<table><tr><td>Methods</td><td>PUMA</td><td>PUMA-C</td><td>ISAAC</td><td>ISAAC-C</td></tr><tr><td>ADC Power (W)</td><td>35.3</td><td>11.1</td><td>32.3</td><td>10.2</td></tr><tr><td>ADC Area (mm2)</td><td>21.2</td><td>13.7</td><td>19.4</td><td>12.5</td></tr><tr><td>Total Power (W)</td><td>62.5</td><td>38.3</td><td>65.8</td><td>43.7</td></tr><tr><td>Total Area (mm2)</td><td>90.6</td><td>83.1</td><td>85.4</td><td>78.6</td></tr><tr><td>EE (TOPS/W)</td><td>0.84</td><td>1.37</td><td>1.06</td><td>1.59</td></tr><tr><td>SE (MB/mm2)</td><td>0.76</td><td>0.83</td><td>0.74</td><td>0.80</td></tr><tr><td>CE (TOPS/mm2)</td><td>0.58</td><td>0.63</td><td>0.81</td><td>0.88</td></tr></table>

and ISAAC-C refer to the application of CODEX on the PUMA and ISAAC accelerators respectively. CODEX provides a smaller 8.62% and 8.64% improvement in CE over PUMA and ISAAC because there is a smaller reduction in ADC area than power. In addition, ADCs take a smaller proportion of total chip area than chip power in the ISAAC and PUMA architectures.

CODEX considers a co software-hardware system where VMM operations would be done on the crossbar and other operations such as activation functions as well as CODEX encoding and decoding would use software processing. The encoding of inputs and outputs where all inputs can be done as a single prepossessing step resulting in negligible processing time overhead. Similarly, there is negligible software area overhead because the linear CODEX encoding and decoding operations can be done using existing software units in the ISAAC and PUMA architectures.

CODEX can be applied to any general ADC technology, so the trade-off between area and power reduction between CODEX-P and CODEX-A is fully controllable through ADC design choices. Power and area calculations use the 8-Bit SAR ADC technology from PUMA and ISAAC with 16 mW power and 0.0096 mm area per ADC as a baseline. For Table I, PUMA-C and ISAAC-C improvements are evaluated based on the average sensing range reduction across the three applications of Fig. 4. The ADC technology and chip configurations of ISAAC and PUMA are used as a baseline and then the ENOB of the ADC is adjusted based on the reduction of ADC sensing range for an application. The power and area improvements provided by CODEX are then calculated based on the ENOB reduction using Eqns. (8-11) from [11]. These equations are derived from analysis of various ADC technologies/architectures and as such, similar power and area reduction behavior could be expected in case of using CODEX for any VMM platform including other ADC architectures.

# V. CONCLUSION

In this brief, we propose a stochastic input encoding method called CODEX to reduce the ADC input range in memristor crossbar systems. By taking advantage of Bernoulli statistics to normalize the output range, CODEX can be applied to any general crossbar system and is shown to be effective across a wide range of applications from sentiment classification to image reconstruction. When applied to the state-of-the-art ISAAC and PUMA accelerators, CODEX decreases in-situ training epochs on average by 25.8% and provide an average 56.6% and 8.63% increase in EE and CE, respectively.

# REFERENCES

[1] P. Yao et al., “Fully hardware-implemented memristor convolutional neural network,” Nature, vol. 577, no. 7792, pp. 641–646, 2020.   
[2] C. Li et al., “Long short-term memory networks in memristor crossbar arrays,” Nat. Mach. Intell., vol. 1, no. 1 pp. 49–57, 2019.   
[3] Z. Wang et al., “Reinforcement learning with analogue memristor arrays,” Nat. Electron., vol. 2, no. 3, pp. 115–124, 2019.   
[4] Z. Wang et al., “In situ training of feed-forward and recurrent convolutional memristor networks,” Nat. Mach. Intell., vol. 1, no. 9, pp. 434–442, 2019.   
[5] F. Cai et al., “A fully integrated reprogrammable memristor–CMOS system for efficient multiply–accumulate operations,” Nat. Electron., vol. 2, no. 7, pp. 290–299, 2019.   
[6] A. Mehonic, A. Sebastian, B. Rajendran, O. Simeone, E. Vasilaki, and A. J. Kenyon, “Memristors—From in-memory computing, deep learning acceleration, and spiking neural networks to the future of neuromorphic and bio-inspired computing,” Adv. Intell. Syst., vol. 2, no. 11, 2020, Art. no. 2000085.   
[7] A. Serb, J. Bill, A. Khiat, R. Berdan, R. Legenstein, and T. Prodromakis, “Unsupervised learning in probabilistic neural networks with multi-state metal-oxide memristive synapses,” Nat. Commun., vol. 7, no. 1, pp. 1–9, 2019.   
[8] H.-M. Huang et al., “Implementation of dropout neuronal units based on stochastic memristive devices in neural networks with high classification accuracy,” Adv. Sci., vol. 7, no. 18, 2020, Art. no. 2001842.   
[9] M. R. Azghadi et al., “Complementary metal–oxide semiconductor and memristive hardware for neuromorphic computing,” Adv. Intell. Syst., vol. 2, no. 5, 2020, Art. no. 1900189.   
[10] A. Sebastian, M. L. Gallo, R. Khaddam-Aljameh, and E. Eleftheriou, “Memory devices and applications for in-memory computing,” Nat. Nanotechnol., vol. 15, no. 7 pp. 529–544, 2020.   
[11] A. Amirsoleimani et al., “In-memory vector-matrix multiplication in monolithic complementary metal–oxide–semiconductor–memristor integrated circuits: Design choices, challenges, and perspectives,” Adv. Intell. Syst., vol. 2, no. 11, 2020, Art. no. 2000115.   
[12] I. Chakraborty et al., “Resistive crossbars as approximate hardware building blocks for machine learning: Opportunities and challenges,” Proc. IEEE, vol. 108, no. 12, pp. 2276–2310, Dec. 2020.   
[13] P. Narayanan et al., “Toward on-chip acceleration of the backpropagation algorithm using nonvolatile memory,” IBM J. Res. Develop., vol. 61, nos. 4–5, pp. 1–11, Jul.–Sep. 2017.   
[14] W.-C. Wei et al., “A relaxed quantization training method for hardware limitations of resistive random access memory (ReRAM)-based computing-in-memory,” IEEE J. Explor. Solid-State Comput., vol. 6, no. 1, pp. 45–52, Jun. 2020.   
[15] R. Genov and G. Cauwenberghs, “Stochastic mixed-signal VLSI architecture for high-dimensional kernel machines,” in Proc. Conf. Adv. Neural Inf. Process. Syst., 2001, pp. 1099–1105.   
[16] R. Karakiewicz, R. Genov, and G. Cauwenberghs, “1.1 TMACS/mW fine-grained stochastic resonant charge-recycling array processor,” IEEE Sensors J., vol. 12, no. 4, pp. 785–792, Apr. 2012.   
[17] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner, “Gradient-based learning applied to document recognition,” Proc. IEEE, vol. 86, no. 11, pp. 2278–2324, Nov. 1998.   
[18] T. Liu, A. Amirsoleimani, F. Alibart, S. Ecoffey, D. Drouin, and R. Genov, “AIDX: Adaptive inference scheme to mitigate state-drift in memristive VMM accelerators,” IEEE Trans. Circuits Syst. II, Exp. Briefs, vol. 68, no. 4, pp. 1128–1132, Apr. 2021, doi: 10.1109/TCSII.2020.3026642, 2020.   
[19] A. Shafiee et al., “ISAAC: A convolutional neural network accelerator with in-situ analog arithmetic in crossbars,” in Proc. ACM/IEEE 43rd Annu. Int. Symp. Comput. Archit. (ISCA), Seoul, South Korea, 2016, pp. 14–26.   
[20] A. Ankit et al., “PUMA: A programmable ultra-efficient memristorbased accelerator for machine learning inference,” in Proc. 24th Int. Conf. Arch. Support Program. Lang. Oper. Syst., 2019, pp. 715–731.   
[21] A. Krizhevsky and G. Hinton, “Learning multiple layers of features from tiny images,” Dept. Comput. Sci., Univ. Toronto, Toronto, ON, Canada, Rep. TR-2009, 2009.   
[22] B. Pang and L. Lee, “A sentimental education,” in Proc. 42nd Annu. Meeting Assoc. Comput. Lingust., 2004, p. 271.   
[23] E. Fonseca et al., “Freesound datasets: A platform for the creation of open audio datasets,” in Proc. 18th Int. Soc. Music Inf. Retrieval Conf., 2017, pp. 486–493.