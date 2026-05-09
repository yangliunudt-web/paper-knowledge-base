---
title: "Reservoir Computing Utilizing a Complementary Combination of n- and p-Channel FeFETs"
authors:
  - "Rikuo Suzuki"
  - "Kasidit Toprasertpong"
  - "Ryosho Nakane"
  - "Eishin Nako"
  - "Mitsuru Takenaka"
  - "Shinichi Takagi"
date: "2024-07-29"
year: "2024"
journal: "IEEE Electron Device Letters"
doi: "10.1109/LED.2024.3435422"
abstract: "We investigate the potential of physical reservoir computing utilizing a combination of n-channel FeFETs (n-FeFETs) and p-channel FeFETs (p-FeFETs). We first confirm that the reservoir computing performance of a single p-FeFET is similar to that of a single n-FeFET despite the smaller memory window. We demonstrate that combining both the reservoir states of n- and p-FeFETs enhances the performance of reservoir computing owing to the complementary behaviors of the two FeFETs: the p-FeFET is turned ON when the n-FeFET is turned OFF and vice versa, providing large current output for any gate voltage input. These complementary characteristics provide the reservoir states that exhibit clear nonlinear transformation of any given input. It is also found that additionally combining with techniques using inverted digital inputs can further enhance the performance. Index Terms— Ferroelectric FET (FeFET), $\\mathsf { H f } _ { 0 . 5 } \\mathsf { Z r } _ { 0 . 5 } \\mathsf { O } _ { 2 }$ p-channel FeFET, reservoir computing."
abstract_cn: "本研究探索了利用n沟道FeFET和p沟道FeFET组合的物理储备池计算潜力。首先确认了单个p‑FeFET的储备池计算性能与单个n‑FeFET相似，尽管其存储窗口较小。我们证明，由于两种FeFET的互补行为（p‑FeFET在n‑FeFET关断时导通，反之亦然），结合两者的储备池状态可以提升储备池计算的性能，从而为任意栅压输入提供大电流输出。这些互补特性使储备池状态能够对任意输入进行明显的非线性变换。同时发现，结合使用反转数字输入技术可以进一步提升性能。"
keywords:
  - "[[FeFET]]"
  - "[[Reservoir computing]]"
  - "[[Complementary devices]]"
  - "[[Nonlinear transformation]]"
cite: "[1] Suzuki et al. Reservoir Computing Utilizing a Complementary Combination of n- and p-Channel FeFETs[J]. IEEE Electron Device Letters, 2024."
aiSum: "n‑p FeFET互补组合实现储备池计算，利用器件互补特性提升非线性变换能力，结合反转数字输入可进一步优化性能。"
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
  - "[[Reservoir computing]]"
---

# Reservoir Computing Utilizing a Complementary Combination of n- and p-Channel FeFETs

Rikuo Suzuki , Kasidit Toprasertpong , Member, IEEE, Ryosho Nakane , Member, IEEE, Eishin Nako , Student Member, IEEE, Mitsuru Takenaka Member, IEEE, and Shinichi Takagi , Senior Member, IEEE

Abstract— We investigate the potential of physical reservoir computing utilizing a combination of n-channel FeFETs (n-FeFETs) and p-channel FeFETs (p-FeFETs). We first confirm that the reservoir computing performance of a single p-FeFET is similar to that of a single n-FeFET despite the smaller memory window. We demonstrate that combining both the reservoir states of n- and p-FeFETs enhances the performance of reservoir computing owing to the complementary behaviors of the two FeFETs: the p-FeFET is turned ON when the n-FeFET is turned OFF and vice versa, providing large current output for any gate voltage input. These complementary characteristics provide the reservoir states that exhibit clear nonlinear transformation of any given input. It is also found that additionally combining with techniques using inverted digital inputs can further enhance the performance.

Index Terms— Ferroelectric FET (FeFET), $\mathsf { H f } _ { 0 . 5 } \mathsf { Z r } _ { 0 . 5 } \mathsf { O } _ { 2 }$ p-channel FeFET, reservoir computing.

# I. INTRODUCTION

N RECENT years, the growing demand for edge AI I computing has created the necessity of high-speed and low-power AI computing. Reservoir computing [1], [2], a framework based on recurrent neural networks, is well-suited for processing time-series data with greater energy efficiency and speed than other architectures [3]. In particular, physical reservoir computing [4], [5], which is reservoir computing that utilizes physical phenomena as reservoirs to provide temporal memory and nonlinearity, has attracted attention because of lower computational cost and simpler hardware implementation. Previous works have studied a variety of physical reservoirs, such as ferroelectric devices [6], [7], [8], [9], memristors [10], [11], photonic systems [12], soft materials [13], spin torque oscillators [14], and spin waves [15].

We have proposed reservoir computing utilizing a CMOScompatible Hf0. ${ } _ { . 5 } Z \mathrm { r } _ { 0 . 5 } \mathrm { O } _ { 2 }$ (HZO)/Si n-channel ferroelectric

Manuscript received 10 June 2024; revised 9 July 2024; accepted 25 July 2024. Date of publication 29 July 2024; date of current version 27 September 2024. This work was supported in part by Japan Science and Technology Agency - Core Research for Evolutionary Science and Technology (JST-CREST), Japan, under Grant JPMJCR20C3; and in part by Japan Society for the Promotion of Science (JSPS) KAKENHI, Japan, under Grant 21H01359. The review of this letter was arranged by Editor K. J. Kuhn. (Corresponding author: Rikuo Suzuki.)

The authors are with the Department of Electrical Engineering and Information Systems, The University of Tokyo, Tokyo 113-8656, Japan (e-mail: rko_suzuki@mosfet.t.u-tokyo.ac.jp).

Color versions of one or more figures in this letter are available at https://doi.org/10.1109/LED.2024.3435422.

Digital Object Identifier 10.1109/LED.2024.3435422

field-effect transistor (FeFET) as a physical reservoir. The dynamics of polarization-charge are used for nonlinear mapping and are extracted by detecting the FeFET current waveforms. Experimental demonstrations of reservoir computing with FeFETs [6], [17], [18], [19] have shown promising results.

In reservoir computing based on n-FeFETs, the polarization-charge dynamics cannot be efficiently extracted from the FET current during negative input voltage because the FET channel is turned off. This leads to an imbalance in computing performance between positive and negative input gate voltages [20]. We propose a scheme that uses both n- and p-FeFETs for reservoir computing to address this problem. We utilize both n- FeFET and p-FeFET for reservoir computing. Since the n- and p-FeFETs operate complementarily, the unbalanced current response can be compensated, resulting in improved computing performance.

# II. DEVICE STRUCTURE AND ELECTRIC PROPERTIES

We used Si n- and p-FeFET devices with 5 µm gate length, 100 µm gate width and $\mathrm { T i N } / \mathrm { H f _ { 0 . 5 } Z r _ { 0 . 5 } O _ { 2 } } ( 1 0 \mathrm { n m } ) / \mathrm { S i O _ { 2 } }$ (0.7 nm) gate stacks. Fig. 1(a) shows the schematic diagram and process flow of FeFETs. Fig. 1(b) exhibits the static $I \ - V _ { g }$ characteristics of n- and p-FeFETs at 50 mV drain voltage. The hysteresis loops in the specific direction of ferroelectricity are observed in both the n- and p-FeFETs. The memory window difference between the n- and p-FeFETs is due to trap-assisted polarization switching [21]. In n-FeFET, electron trap accumulation increases the electric field across the ferroelectric film, while in p-FeFET, less charge trapping makes polarization switching more difficult.

# III. EXPERIMENTAL PROCEDURE

The flow of reservoir computing utilizing the combined FeFETs is shown in Fig. 2. We first converted random digital inputs u(n) with discrete time steps n $( = 1 , 2 , . . . , 1 0 0 0 )$ into time-series triangular voltages, where 0 and 1 correspond to negative and positive peaks, respectively. Triangular wave can efficiently induce the transient dynamics of FeFET and can be implemented using analog circuits. The center voltage of these pulses was set at 0 V, with positive and negative peak voltages fixed at 3.5 V and -3.5 V, respectively. The pulse width of each pulse was taken to be 4 µs. The drain was biased at 0.3 V, while the source and substrate were grounded. We applied $1 0 ^ { \overset { \cdot } { 6 } }$ pre-cycling pulses before the measurements, which is reported to improve the stability of FeFET-based reservoir computing in the long-term operation [22], [23]. Next, the voltage waveforms were sequentially applied to the

![](images/a00978b461d752d1cc51b9db08543e2a809180c92f4c91199f724c56246a30f2.jpg)  
Fig. 1. (a) Schematic images of the n- and p-FeFETs and the process flow of these devices. (b) $\breve { I } - V _ { \mathfrak { g } }$ characteristics of n- and p- FeFET. The horizontal arrows in these pictures show the memory windows of these devices.

gate electrodes of both the n- and p- FeFETs. Subsequently, we measured the drain currents of the n- and p-FeFETs with a constant sampling rate to obtain $x _ { n , j }$ and $x _ { n , j } ^ { \prime } ,$ respectively, where the subscripts n and $j _ { \mathrm { \ell } } ( = 1 , 2 , . . . , M _ { \mathrm { \ell } } \overset {  , } { = } 4 0 0 )$ represent the time step and the sequential number of the sampling point, respectively. We used $x _ { n , j }$ and $x _ { n , j } ^ { \prime }$ as virtual nodes that correspond to the output states of the FeFET reservoirs at n. We confirmed by comparing $I _ { d }$ and $I _ { s }$ that the gate-induced drain leakage current does not contribute to the performance of reservoir computing. In this study, we employed a scheme that combines virtual nodes of different FeFET reservoir subsystems. We combine virtual nodes of $n -$ and p-FeFETs to create a combined set of virtual nodes with $2 M = 8 0 0$ for each time step to be connected with 800 weights on a PC. Additionally, when we combine four FeFETs, we create a combined set of virtual nodes with $4 M \ = \ 1 6 0 0$ for each time step to be connected with 1600 weights on a computer software. We discarded $x _ { n , j }$ and $x _ { n , j } ^ { \prime }$ in the first 500 steps and obtained a dataset from those in the rest 500 steps. In this way, 10 datasets from 10 measurement batches were prepared. We trained the weights using 8 datasets (4000 steps) and tested the system using the rest 2 datasets (1000 steps). We performed 5-fold cross-validation to estimate the mean performance [17].

To assess the reservoir computing performance, we employed three tasks: the short-term memory (STM) task [24], evaluating the short-term memory function, the parity check (PC) task, evaluating both short-term memory and nonlinearity functions [25], and NARMA-2 task, evaluating both short-term memory and nonlinearity functions [26].

# IV. RESULTS AND DISCUSSIONS

Fig. 3 shows the drain current waveforms of n- and p-FeFETs. When a digital input 1 (positive voltage) is applied, a large current flows in the n-FeFETs while only a small current flows in the $p { \mathrm { - F e F E T s } } ,$ and the opposite happens when a digital input 0 (negative voltage) is applied. Furthermore, the behaviors of the drain currents are dependent not only on the present gate input but also on past inputs. The results indicate that the time-series drain currents have temporal memory and we can extract past histories from these currents. Single FeFET-based reservoir computing has a problem originating from the following characteristics. For n-FeFET, the computing performance tends to be high when a positive gate voltage is applied and a large current flows. The large current reflects the polarization-charge dynamics in FeFET and thus holds rich

![](images/4ef34fda0f8f414f7f273385de622b478149b0ca4afda91c368553c904a2a5c3.jpg)  
Fig. 2. Flow of reservoir computing utilizing the combined virtual nodes gained from n- FeFET and p- FeFET.

![](images/8e2013e30a02450b37204568d3a9f25872ca1b38d7c605bb1e254ebe36061623.jpg)  
Fig. 3. Drain current responses to digital input sequences (e.g. ’01’ corresponded to applying 1 input after 0 input) obtained from n- and p-FeFETs.

information. However, the computing performance tends to be low when a negative gate voltage is applied and a small current flows. That is because the polarization-charge dynamics cannot be read out through the channel current due to the lack of the inversion channel.

In this study, to address this problem, we combine the virtual nodes from current waveforms of n- and p-FeFETs to extract rich information on the polarization-charge dynamics, irrespective of input data, through complementary operations of n- and p-FeFETs. Figs. 4(a) and (b) show the forgetting curves for STM and PC tasks, respectively, in the reservoir utilizing n- or p-FeFET. The forgetting curves were calculated by the determination coefficient $( r ^ { 2 } )$ between the inference results and the target values of a specific task at a given $T _ { d e l a y } . \ T _ { d e l a y }$ corresponds to a pulse width of the input pulse (4µs). We evaluated fundamental capacities indispensable for reservoir computing, using memory and parity check tasks. Here, $\operatorname { C } _ { \operatorname { S T M } }$ and CPC are defined by summing the $r ^ { 2 }$ values over the time delay steps $T _ { d e l a y }$ (excluding 0 delay). The reservoir computing performance of p-FeFET is comparable to that of n-FeFET despite the smaller memory window in Fig. 1(b). This is because memory window is static characteristics, whereas reservoir computing is performed using dynamic characteristics of polarization. We have confirmed that the polarization switching dynamics is similar in p-FeFET and n-FeFET.

![](images/48e9cc39138bed62e209f5e13d2929c93acfa3b69d233376a53924a05f5e5061.jpg)  
Fig. 4. Results of reservoir computing utilizing n- and p- FeFETs (n&p), n- FeFET (n), and p-FeFET (p). Determination coefficient of (a) STM and (b) PC tasks. The determination coefficient of the PC task when present digital input is (c) 0 or (d) 1. (e) CSTM and CPC when present digital input is 0 or 1.

The target values for each task are determined according to the formula shown in Fig. 4. The impacts of a combination of the n- and p-FeFET reservoirs on the STM and PC performance are shown in Figs. 4(a) and (b), respectively. Compared with the performance by only n- or p-FeFET, the combination significantly enhances both CSTM and CPC. These results highlight improvements in short-term memory and nonlinearity.

We analyze the forgetting curve of the PC task in Fig. 4(b) by separately evaluating the determination coefficients $( r _ { 0 } ^ { 2 }$ and $r _ { 1 } ^ { 2 } )$ for digital inputs of 0 and 1, respectively, as shown in Figs. 4(c) and (d). Furthermore, Fig. 4(e) shows CPC determined by summing $r _ { 0 } ^ { 2 }$ and $r _ { 1 } ^ { 2 } .$ , for three cases. In the case of p-FeFET, the capacity for the input 0 is higher than that for the input 1 because the nonlinear polarization-charge dynamics can be extracted from the ON current of the p-FeFET with the negative gate voltage. In contrast, the n-FeFET has a higher capacity for the input 1 because the ON current flows in the n-FeFET with the positive gate voltage. On the other hand, when combining the n- and p-FeFETs, the capacity becomes higher for the inputs of both 0 and 1 than those of the single FeFET, and the difference in the capacity between the inputs of 0 and 1 disappears. These results show that the combination of the virtual nodes in the n-FeFET and p-FeFET can extract the polarization-charge dynamics in either FeFET to provide rich information for any inputs, resulting in such high reservoir computing performance.

To solve the imbalance problem of reservoir computing using a single n-FeFET, on the other hand, we previously took another approach using two n-FeFETs with different gate voltage waveforms: one from the regular digital input data and the other from the inverted digital input data [20]. In this way, either n-FeFET can have large current for both inputs 0 and 1. Besides combining an n-FeFET and a p-FeFET, here we use two n-FeFETs and two p-FeFETs with the normal and inverted input waveforms (a combination of four FeFETs). Fig. 5 (a) shows the forgetting curves for the STM and PC tasks when we utilize the single n-FeFET and four FeFETs. To gain a deeper understanding of the computational capabilities of the proposed scheme, we conducted the NARMA-2 task, which is a time series prediction task. NARMA-2 is a nonlinear autoregressive moving average model defined as (1) below. I (t) is a random input of 0 or 0.5, and y(t) represents the target value. Additionally, the accuracy of this time series prediction is evaluated by the normalized mean square error (NMSE). As the capacities of STM and PC improve, it is expected that

![](images/7552c63c4ed4cce6fb13997bc676ef5543ee69f6945a08fbec3c78bc6afde431.jpg)

![](images/29e23703da398e39cde619dab5317efd5f136797f5b44487bf5a7ee9040bce04.jpg)

![](images/5b22980e1d9cf39cecf426dc4970e10c239ab70fce9b688b38b7e57323389f12.jpg)

![](images/2305ae79999ad39bd578093b920bae884625cf9940e14e5d38ec0f7c9d815292.jpg)  
Fig. 5. (a) Forgetting curve of reservoir computing utilizing four FeFETs. (b) Capacity of STM and PC task, (c) NMSE of NARMA-2 task of reservoir computing utilizing n-FeFET (n), p-FeFET (p), and n- and p- FeFETs (n&p), and two n-FeFETs(n&n¯), two p-FeFETs (p&p¯), and two n- and p- FeFETs with normal input patterns and inverted input patterns (n&p&n¯&p¯), (d) Benchmark of NMSE of NARMA-2 task using RC with given number of devices connected in the system.

NMSE will decrease.

$$
y (\mathbf {t} + \mathbf {1}) = \mathbf {0}. 4 y (\mathbf {t}) + \mathbf {0}. 4 y (\mathbf {t}) y (\mathbf {t} - \mathbf {1}) + \mathbf {0}. 6 I (\mathbf {t}) ^ {3} + \mathbf {0}. 1 \tag {1}
$$

Figs.5(b) and 5(c) show the capacities for the STM and PC tasks or NMSE of NARMA-2 task with various combinations. According to these figures, as the capacities of STM and PC improve through the combination of complementary devices, the accuracy of time series prediction by reservoir systems increases, resulting in a decrease in NMSE for the NARMA-2 task as expected. Additionally, As shown in Fig.5 (d), it has been confirmed that the FeFET reservoir computing exhibits high performance when compared to other reservoir computing based on electronic devices, which is further enhanced by the proposed connection scheme. Furthermore, this advantage of FeFET reservoir computing was further enhanced by the proposed scheme in this letter.

Capacities of any combinations of two FeFETs are higher than those of a single FeFET. Furthermore, the highest performance is achieved when combining four FeFETs composed of n- and p-FeFETs with the normal and inverted input waveforms. Considering the further improvement from the combination of the two devices, the combination of the four devices yields positive effects more than those by the complementary current response. This indicates that the currents of the n-FeFETs and p-FeFETs give different nonlinear transformations, owing to the different polarization switching behaviors between n- and p-FeFETs [20], and such difference lead to richer information useful for computing.

# V. CONCLUSION

We experimentally demonstrated reservoir computing using a complementary combination of the n- and p-FeFETs. The high performance was obtained by utilizing both the n- and p-FeFETs, which behave in a complementary manner, and the resulting ON current with rich information for any inputs. Furthermore, the combination of four FeFETs (two n-FeFETs and two p-FeFETs) with normal and inverted gate input waveforms leads to further enhanced performance. This indicates that the integration of n- and p-FeFETs with normal and inverted gate input waveforms results in various nonlinear transformations, which are beneficial for reservoir computing.

# REFERENCES

[1] H. Jaeger, “The ‘echo state’ approach to analysing and training recurrent neural networks with an erratum note,” German Nat. Res. Center Inf. Technol., Bonn, Germany, GMD Tech. Rep. 148, 2001, pp. 1–47.   
[2] W. Maass, T. Natschläger, and H. Markram, “Real-time computing without stable states: A new framework for neural computation based on perturbations,” Neural Comput., vol. 14, no. 11, pp. 2531–2560, Nov. 2002, doi: 10.1162/089976602760407955.   
[3] P. R. Vlachas, J. Pathak, B. R. Hunt, T. P. Sapsis, M. Girvan, E. Ott, and P. Koumoutsakos, “Backpropagation algorithms and reservoir computing in recurrent neural networks for the forecasting of complex spatiotemporal dynamics,” Neural Netw., vol. 126, pp. 191–217, Jun. 2020, doi: 10.1016/j.neunet.2020.02.016.   
[4] G. Tanaka, T. Yamane, J. B. Héroux, R. Nakane, N. Kanazawa, S. Takeda, H. Numata, D. Nakano, and A. Hirose, “Recent advances in physical reservoir computing: A review,” Neural Netw., vol. 115, pp. 100–123, Jul. 2019, doi: 10.1016/j.neunet.2019.03.005.   
[5] K. Nakajima, “Physical reservoir computing—An introductory perspective,” Jpn. J. Appl. Phys., vol. 59, no. 6, Jun. 2020, Art. no. 060501, doi: 10.35848/1347-4065/ab8d4f.   
[6] E. Nako, K. Toprasertpong, R. Nakane, Z. Wang, Y. Miyatake, M. Takenaka, and S. Takagi, “Proposal and experimental demonstration of reservoir computing using Hf0.5Zr0.5O2/Si FeFETs for neuromorphic applications,” in Proc. IEEE Symp. VLSI Technol., Jun. 2020, pp. 1–2, doi: 10.1109/VLSITechnology18217.2020.9265110.   
[7] M. Tang, X. Zhan, S. Wu, M. Bai, Y. Feng, G. Zhao, J. Wu, J. Chai, H. Xu, X. Wang, and J. Chen, “A compact fully ferroelectric-FETs reservoir computing network with sub-100 ns operating speed,” IEEE Electron Device Lett., vol. 43, no. 9, pp. 1555–1558, Sep. 2022, doi: 10.1109/LED.2022.3188496.   
[8] J. Yu, Y. Li, W. Sun, W. Zhang, Z. Gao, D. Dong, Z. Yu, Y. Zhao, J. Lai, Q. Ding, Q. Luo, C. Dou, Q. Zuo, Y. Zhao, S. Chen, R. Zou, H. Chen, Q. Wang, H. Lv, X. Xu, D. Shang, and M. Liu, “Energy efficient and robust reservoir computing system using ultrathin (3.5 nm) ferroelectric tunneling junctions for temporal data learning,” in Proc. Symp. VLSI Technol., Kyoto, Japan, Jun. 2021, pp. 1–2.   
[9] G. Lee, C. Kang, S. Kim, Y. Park, E. J. Shin, and B. J. Cho, “Physical reservoir based on a leaky-FeFET using the temporal memory effect,” IEEE Electron Device Lett., vol. 45, no. 1, pp. 108–111, Jan. 2024, doi: 10.1109/LED.2023.3335142.   
[10] C. Du, F. Cai, M. A. Zidan, W. Ma, S. H. Lee, and W. D. Lu, “Reservoir computing using dynamic memristors for temporal information processing,” Nature Commun., vol. 8, no. 1, Dec. 2017, Art. no. 2204, doi: 10.1038/s41467-017-02337-y.   
[11] J. Moon, W. Ma, J. H. Shin, F. Cai, C. Du, S. H. Lee, and W. D. Lu, “Temporal data classification and forecasting using a memristor-based reservoir computing system,” Nature Electron., vol. 2, no. 10, pp. 480–487, Oct. 2019, doi: 10.1038/s41928-019-0313-3.   
[12] F. Duport, B. Schneider, A. Smerieri, M. Haelterman, and S. Massar, “All-optical reservoir computing,” Opt. Exp., vol. 20, no. 20, p. 22783, 2012, doi: 10.1364/oe.20.022783.   
[13] K. Nakajima, H. Hauser, T. Li, and R. Pfeifer, “Information processing via physical soft body,” Sci. Rep., vol. 5, no. 1, May 2015, Art. no. 10487, doi: 10.1038/srep10487.   
[14] J. Torrejon, M. Riou, F. A. Araujo, S. Tsunegi, G. Khalsa, D. Querlioz, P. Bortolotti, V. Cros, K. Yakushiji, A. Fukushima, H. Kubota, S. Yuasa, M. D. Stiles, and J. Grollier, “Neuromorphic computing with nanoscale spintronic oscillators,” Nature, vol. 547, no. 7664, pp. 428–431, Jul. 2017, doi: 10.1038/nature23011.   
[15] R. Nakane, A. Hirose, and G. Tanaka, “Spin waves propagating through a stripe magnetic domain structure and their applications to reservoir computing,” Phys. Rev. Res., vol. 3, no. 3, Sep. 2021, Art. no. 033243, doi: 10.1103/physrevresearch.3.033243.

[16] L. Appeltant, M. C. Soriano, G. Van der Sande, J. Danckaert, S. Massar, J. Dambre, B. Schrauwen, C. R. Mirasso, and I. Fischer, “Information processing using a single dynamical node as complex system,” Nature Commun., vol. 2, no. 1, pp. 1–6, Sep. 2011, doi: 10.1038/ncomms1476.   
[17] K. Toprasertpong, E. Nako, Z. Wang, R. Nakane, M. Takenaka, and S. Takagi, “Reservoir computing on a silicon platform with a ferroelectric field-effect transistor,” Commun. Eng., vol. 1, no. 1, Aug. 2022, Art. no. 21, doi: 10.1038/s44172-022-00021-8.   
[18] S. Takagi, K. Toprasertpong, K. Tahara, E. Nako, R. Nakane, Z. Wang, X. Luo, T.-E. Lee, and M. Takenaka, “(Invited) HfZrO-based ferroelectric devices for lower power AI and memory applications,” ECS Trans., vol. 104, no. 4, pp. 17–26, Oct. 2021, doi: 10.1149/10404.00 17ecst.   
[19] E. Nako, K. Toprasertpong, R. Nakane, M. Takenaka, and S. Takagi, “Reservoir computing system with HZO/Si FeFETs in parallel configuration: Experimental demonstration of speech classification,” IEEE Trans. Electron Devices, vol. 70, no. 11, pp. 5657–5664, Nov. 2023, doi: 10.1109/TED.2023.3318870.   
[20] Z. Wang, E. Nako, K. Toprasertpong, R. Nakane, M. Takenaka, and S. Takagi, “Improvement in computing capabilities of FeFET-based reservoir computing by using an inverted signal scheme,” in Proc. Extended Abstr. Int. Conf. Solid State Devices Mater., Japan, Sep. 2021, pp. 109–110, doi: 10.7567/ssdm.2021.b-3-04.   
[21] K. Toprasertpong, M. Takenaka, and S. Takagi, “On the strong coupling of polarization and charge trapping in HfO2/Si-based ferroelectric fieldeffect transistors: Overview of device operation and reliability,” Appl. Phys. A, Solids Surf., vol. 128, no. 12, Dec. 2022, Art. no. 1114, doi: 10.1007/s00339-022-06212-6.   
[22] E. Nako, K. Toprasertpong, R. Nakane, Z. Wang, M. Takenaka, and S. Takagi, “Impact of endurance characteristics of FeFETs on reservoir computing capabilities,” in Proc. Extended Abstr. Int. Conf. Solid State Devices Mater., Japan, Sep. 2021, pp. 129–130, doi: 10.7567/ssdm.2021.b-5-07.   
[23] K. Toprasertpong, E. Nako, S.-Y. Min, Z. Cai, S.-K. Cho, R. Suzuki, R. Nakane, M. Takenaka, and S. Takagi, “Robustness to device degradation in silicon FeFET-based reservoir computing (invited),” in Proc. IEEE Int. Rel. Phys. Symp. (IRPS), Grapevine, TX, USA, Apr. 2024, pp. 1–6.   
[24] H. Jaeger, “Short term memory in echo state networks,” German Nat. Res. Center Inf. Technol., Bonn, Germany, GMD Tech. Rep. 152, 2001, pp. 1–60, doi: 10.24406/publica-fhg-291107.   
[25] N. Bertschinger and T. Natschläger, “Real-time computation at the edge of chaos in recurrent neural networks,” Neural Comput., vol. 16, no. 7, pp. 1413–1436, Jul. 2004, doi: 10.1162/0899766043230 57443.   
[26] A. F. Atiya and A. G. Parlos, “New results on recurrent network training: Unifying the algorithms and accelerating convergence,” IEEE Trans. Neural Netw., vol. 11, no. 3, pp. 697–709, May 2000, doi: 10.1109/72.846741.   
[27] H. Liu, S. Duan, W. Jiang, J. Li, and L. Wang, “Nonlinear system identification using dynamic memristor-based reservoir computing system,” in Proc. IEEE 5th Int. Conf. Electron. Technol. (ICET), Chengdu, China, May 2022, pp. 885–889, doi: 10.1109/ICET55676.2022.98 24316.   
[28] K. Liu, J. Li, F. Li, Y. Lin, H. Liu, L. Liang, Z. Luo, W. Liu, M. Wang, F. Zhou, and Y. Liu, “A multi-terminal ion-controlled transistor with multifunctionality and wide temporal dynamics for reservoir computing,” Nano Res., vol. 17, no. 5, pp. 4444–4453, May 2024, doi: 10.1007/s12274-023-6343-1.   
[29] D. Nishioka, T. Tsuchiya, W. Namiki, M. Takayanagi, M. Imura, Y. Koide, T. Higuchi, and K. Terabe, “Edge-of-chaos learning achieved by ion-electron–coupled dynamics in an ion-gating reservoir,” Sci. Adv., vol. 8, no. 50, Dec. 2022, Art. no. eade1156, doi: 10.1126/sciadv.ade1156.