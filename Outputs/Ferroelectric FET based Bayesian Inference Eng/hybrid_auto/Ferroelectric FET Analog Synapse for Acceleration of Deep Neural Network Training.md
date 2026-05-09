---

title: "Ferroelectric FET Analog Synapse for Acceleration of Deep Neural Network Training"
authors:
  - "Matthew Jerry"
  - "Pai-Yu Chen"
  - "Jianchi Zhang"
  - "Pankaj Sharma"
  - "Kai Ni"
  - "Shimeng Yu"
  - "Suman Datta"
date: "2018-01-01"
year: "2018"
journal: "IEEE Electron Device Letters"
abstract: "The memory requirement of at-scale deep neural networks (DNN) dictate that synaptic\\"
abstract_cn: "大规模深度神经网络的内存需求要求突触权重值在片外存储器（如DRAM）中存储和更新，限制了能效和训练时间。具有模拟非易失性存储器的单片交叉阵列/伪交叉阵列能够在芯片上存储和更新权重，为加速深度神经网络训练提供了可能。本文利用铁电场效应晶体管中电压控制部分极化切换的动力学特性，演示了这种模拟突触。我们开发了一个瞬态Presiach模型，能够准确预测任意脉冲宽度、电压和历史条件下的次要环轨迹和剩余极化电荷。我们实验演示了一个具有对称增强和抑制特性的5位铁电场效应晶体管突触，以及75ns更新脉冲下45倍的可调电导范围。使用电路宏模型评估和基准测试了铁电场效应晶体管突触核心的片上学习性能（面积、延迟、能量、精度），揭示了相比基于多态电阻随机存取存储器的模拟突触，在线学习延迟加速了10^3至10^6倍。"
keywords:
  - "[[FeFET]]"
  - "[[Analog synapse]]"
  - "[[Deep neural network]]"
  - "[[On-chip learning]]"
cite: "[1] Jerry M, Chen P Y, Zhang J, et al. Ferroelectric FET analog synapse for acceleration\\"
aiSum: "FeFET模拟突触：基于部分极化切换，实现5位对称增强/抑制特性，75ns更新脉冲，45倍电导可调范围，相比多态RRAM突触在线学习延迟加速10^3‑10^6倍。"
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
  - "[[Neural network]]"
---

# Ferroelectric FET Analog Synapse for Acceleration of Deep Neural Network Training

Matthew Jerry<sup>1</sup>, Pai-Yu Chen<sup>2</sup>, Jianchi Zhang<sup>1</sup>, Pankaj Sharma<sup>1</sup>, Kai Ni<sup>1</sup>, Shimeng Yu<sup>2</sup> and Suman Datta<sup>1</sup>  
<sup>1</sup>Department of Electrical Engineering, University of Notre Dame, Notre Dame, IN 46556, USA  
<sup>2</sup>School of Electrical, Computer, and Energy Engineering, Arizona State University, Tempe, AZ 85281, USA  
Phone: (574)-631-5480; Fax: (574)-631-4393; email: mjerry@nd.edu

Abstract—The memory requirement of at-scale deep neural networks (DNN) dictate that synaptic weight values be stored and updated in off-chip memory such as DRAM, limiting the energy efficiency and training time. Monolithic cross-bar / pseudo cross-bar arrays with analog non-volatile memories capable of storing and updating weights on-chip offer the possibility of accelerating DNN training. Here, we harness the dynamics of voltage controlled partial polarization switching in ferroelectric-FETs (FeFET) to demonstrate such an analog synapse. We develop a transient Presiach model that accurately predicts minor loop trajectories and remnant polarization charge $(\mathrm{P_r})$ for arbitrary pulse width, voltage, and history. We experimentally demonstrate a 5-bit FeFET synapse with symmetric potentiation and depression characteristics, and a 45x tunable range in conductance with 75ns update pulse. A circuit macro-model is used to evaluate and benchmark on-chip learning performance (area, latency, energy, accuracy) of FeFET synaptic core revealing a $10^{3}$ to $10^{6}$ acceleration in online learning latency over multi-state RRAM based analog synapses.

# I. INTRODUCTION

Deep neural networks have demonstrated success in cognitive tasks such as speech and image recognition (Fig. 1(a)). However, the energy consumption and training time of at-scale deep neural networks are limited by off-chip memory (DRAM) access bottleneck owing to the large memory requirements of the weight matrices. For a fully connected DNN, significant acceleration in training can be achieved by minimizing data movement by utilizing on-chip storage and performing weight updates at the same node, where all the nodes are all connected together in an array. The ability to expand on-chip SRAM cache sizes to accommodate training of larger networks is limited due to $150\mathrm{F}^2$ (F is the smallest patterned feature) cell size and motivates the development of an area efficient high speed analog synapse capable of on-chip learning. Device requirements for accelerating the training of DNNs include $\pm 1\mathrm{V}$ , 1 nanosecond potentiation and depression programming pulses, a symmetric and linear conductance response with $\geq 32$ conductance states ( $\geq 5$ -bit), and a $\mathrm{G}_{\mathrm{max}} / \mathrm{G}_{\mathrm{min}}$ ratio of $>10$ [1][8]. Emerging non-volatile memories such as resistive random access memory (RRAM) and phase change memory (PCM) are potential candidates owing to their small cell size ( $4\mathrm{F}^2$ ) and the ability to program the cells with multiple intermediate states. However, achieving symmetric potentiation and depression characteristics, with nanosecond pulse widths, and sufficient $\mathrm{G}_{\mathrm{max}} / \mathrm{G}_{\mathrm{min}}$ ratios in RRAM/PCM has not been realized (Fig. 2). In the case of filamentary

RRAM, the lack of symmetry in the characteristics [2] results in the utilization of fewer conductance states, and often quenching $\mathrm{G}_{\mathrm{max}} / \mathrm{G}_{\mathrm{min}} < 10$ in addition, which negatively impacts the system performance. While interfacial RRAM and RRAM exploiting multiple weak filaments [3]–[5] exhibit increased symmetry between potentiation and depression, the program pulse widths are as large as 10ms due to the slow diffusion process of oxygen vacancies during weak programming. Therefore, training with a modest 1M images from the MNIST database on such devices would take years ( $>5.6 \times 10^{7}$ s) on such devices (Fig. 17). In this work, we harness electric-field controlled partial polarization switching in ALD ferroelectric $\mathrm{Hf}_{0.5} \mathrm{Zr}_{0.5} \mathrm{O}_2$ (HZO) [6] to demonstrate a FeFET based analog synapse (Fig. 1(c)). The FeFET synapse exhibits, highly symmetric conductance values for potentiation and depression, in a pseudo-crossbar array, for 75ns pulses with progressive amplitude (Fig. 1(b)). Therefore, enabling high speed training of networks with high online learning accuracy (90%), in a scaled cell footprint.

# II. METAL-FERROELECTRIC-METAL CAPACITOR FABRICATION AND MODELING

The FeFET synapse utilizes multi-domain polarization switching dynamics in ferroelectric HZO thin films to gradually tune the threshold voltage $(\mathrm{V_T})$ of the underlying channel, and consequently its drain-to-source conductance, by the application of short voltage pulses to the gate. First, we measure and model the dynamics of the metal-ferroelectric-metal (MFM) capacitors (TiN/10nm HZO/TiN). The multidomain effects are modeled using a Presiach theory of hysteretic switching where the MFM capacitor response is assumed to be an aggregate response of a distribution of individual domains with discrete and deterministic coercive fields $(\mathrm{E_c}^+$ and $\mathrm{E_c}^-$ (Fig. 3). The dynamic response of each domain is then computed by rescaling the applied voltage amplitude with an experimentally calibrated transfer function, that is dependent on the applied pulse width. The scaled effective voltage $(\mathrm{V_{EFF}})$ is then applied to the static model to compute the net polarization (P) response from a write pulse of arbitrary duration and amplitude [7] (Fig. 3). Fig. 4(a-c) show that the model captures both the history and the memory wipeout of the minor loop trajectories of the MFM device.

We study the effect of multiple pulse schemes on the remnant polarization to optimize the number of accessible polarization states (Fig. 6(a)-(c)). The remnant polarization charge $(\mathrm{P_r})$ is calculated by integrating the transient current (Fig. 5). The experimental and simulation results are in excellent agreement as shown in Fig. 6(a)-(c). Pulse schemes

1 and 2 exhibit regions of near linear $\mathrm{P_r}$ change, but the number of available states is limited (6-12 states) (Fig. 6(a)-(b). While scheme 3 (Fig. 6(c)) accesses $>50$ stable intermediate polarization states as it directly samples from the assumed distribution (Fig. 3) of $\mathrm{E_c}^+$ and $\mathrm{E_c}^-$ . Therefore, scheme 3 results in symmetric and sigmoidal potentiation and depression characteristics. The simulated trajectory of the polarization $(1\rightarrow 2\rightarrow 3)$ in response to three example potentiation pulses from pulse schemes 2 and 3 are shown in Fig. 7(a)-(b), highlighting the enhanced control of $\Delta \mathrm{P_r}$ in scheme 3. Point 1 indicates the initial $\mathrm{P_r}$ state while Point 3 is the new stable $\mathrm{P_r}$ state. Next, we evaluate the channel conductance of a FeFET based on the polarization states of Scheme 3 (Fig. 6(c)). The FeFET characteristics are simulated by computing the surface potential $\psi_{s}$ based on charge sharing between the capacitors in an MFIS stack using the $\mathrm{Pr}$ values from Fig. 6(c) and experimentally extracted FET parameters. The $\mathrm{I_{DS} - V_{GS}}$ characteristics are shown in Fig. 8(a)-(b). The simulated channel conductance $(\mathrm{G_{ds}})$ as a function of pulse number for potentiation and depression results in a symmetric conductance response with $\mathrm{G_{max} / G_{min}}$ ratio of 69 (Fig. 9) highlighting the potential of the FeFET as an analog synapse candidate.

# III. FEFET ANALOG SYNAPSE FABRICATION, CHARACTERIZATION, AND ANALYSIS

Fig. 10 summarizes the fabrication process flow of n-channel FeFETs. The ferroelectric gate stack consists of 10nm thick ALD HZO deposited on p-Si with 0.8nm thick interfacial $\mathrm{SiO}_2$ layer (confirmed by TEM), capped by ALD TiN layer, followed by a $600^{\circ}\mathrm{C}$ anneal. This gives rise to multiple ferroelectric domains within a nanocrystalline structure of HZO. The conductance behavior in response to pulse schemes 1, 2, 3 are shown in Fig. 11(a)-(c). The shape of the measured FeFET channel conductance $(\mathrm{G_{ds}})$ vs pulse number curves mirrors that of the $\mathrm{P_r}$ vs pulse number response, as shown previously in Fig. 6(a)-(c). This confirms that the programming sequence is deterministically switching a fraction of the total FE domains with each pulse. Scheme 3 exhibits the highest number of programmed states, 32 (5-bit), as it encompasses a more uniform sampling from the domain coercive field $(\mathrm{E_c}^+$ and $\mathrm{E_c}^-$ distributions compared to schemes 1 and 2. Pulse widths are limited to 75ns currently constrained by the experimental FeFET dimensions and will scale with geometry. The $\mathrm{G_{max} / G_{min}}$ ratios are extracted for each scheme and are compared with other reported values in Fig. 12(a). The ratio directly correlates with the neural network accuracy, where $\mathrm{G_{max} / G_{min}} > 10$ is required to achieve accuracies of $>80\%$ [8]. FeFET achieves a ratio of $47\times$ near the ideal design target of $50\times$ [8]. Fig. 12(b) shows the extracted non-linearity (as described in [8]) and corresponding asymmetry parameters for each pulse scheme. The equal sign $(+)$ and near zero value of, $\alpha_{p} = 1.75\alpha_{d} = 1.46$ indicated the linearity, and lead to a near ideal asymmetry value of 0.29 (ideal asymmetry $= 0$ , implying perfectly symmetric characteristics) highlighting the symmetric behavior of the FeFET between potentiation and depression using scheme 3. The corresponding transient $\mathrm{I_{DS} - V_{GS}}$ characteristics for all 32 potentiation and depression states are shown in Fig. 13.

# IV. FEFET SYNAPTIC CORE MACRO MODEL & BENCHMARKING

We benchmark the experimental FeFET with SRAM and other analog RRAM synaptic devices using a 2-layer multilayer perceptron (MLP) neural network (Fig. 14(a)) with the support of a circuit-level macro model, NeuroSim [8], by estimating the chip area, latency, dynamic energy and leakage power. We develop the cell structure of FeFET in a pseudo-crossbar array to realize key operations such as vector-matrix product (weighted sum Fig. 14(b)) and weight update (Fig. 15). The FeFET synaptic core is simulated with the supporting peripheral circuits (Fig. 16). The benchmarking highlights the increased learning accuracy ( $>90\%$ ) and faster speed (75ns) of FeFET than reported RRAMs for a training cycle comprising of 1M images from MNIST database (Fig. 17). Further, FeFET synaptic cores achieve a $10\times$ reduction in area and $>30\times$ reduction of leakage power compared to a 6-bit SRAM cache with similar accuracy.

# V. CONCLUSION

In conclusion, we experimentally demonstrate a FeFET analog synapse based on partial polarization switching, for acceleration of on-chip learning in deep neural networks. A transient Presiach model quantitatively captures the dynamics of voltage controlled partial polarization switching in $10\mathrm{nm}$ HZO films. The fabricated FeFET synapse exhibits symmetric 5-bit potentiation and depression characteristics, resulting in $90\%$ accuracy for image recognition after training on the MNIST database. Further, the 75ns experimental programing pulse width improves training time on 1M images by $1000\times$ compared to demonstrated RRAM devices while maintaining a $10\times$ area advantage over SRAM.

# VI. ACKNOWLEDGEMENTS

This project was supported by the National Science Foundation under grant 1640081 and 1552687, and the Nanoelectronics Research Corporation (NERC), a wholly-owned subsidiary of the Semiconductor Research Corporation (SRC), through Extremely Energy Efficient Collective Electronics (EXCEL), an SRC-NRI Nanoelectronics Research Initiative under Research Task IDs 2698.001. The authors thank useful discussion with Wilfried Haensch of IBM Research, Yorktown Heights.

# VII. REFERENCES

[1] T. Gokmen, et al., "Acceleration of deep neural network training with resistive cross-point devices: Design considerations," Front. Neurosci., 10, 1-13, 2016.   
[2] J. Woo, et al., "Improved synaptic behavior under identical pulses using AlOx/HfO2 bilayer RRAM array for neuromorphic systems," IEEE Electron Device Lett., 37, 8, 994-997, 2016.   
[3] L. Gao, et al., “Fully parallel write/read in resistive synaptic array for accelerating on-chip learning,” Nanotechnology, 26, 45, 455204, 2015.   
[4] S. Park, et al., "Neuromorphic speech systems using advanced ReRAM-based synapse," International Electron Devices Meeting, 2013.   
[5] S. H. Jo, et al., "Nanoscale memristor device as synapse in neuromorphic systems," Nano Lett., 10, 4, 1297-1301, 2010.   
[6] S. Oh, et al., "HfZrOx -based Ferroelectric Synapse Device with 32 levels of Conductance States for Neuromorphic Applications," IEEE Electron Devices Lett., 99, 732-735, 2017.   
[7] J. Chow, et al., "A voltage-dependent switching-time (VDST) model of ferroelectric capacitors for low-voltage FeRAM circuits," Symp. VLSI Circuits. Dig. Tech. Pap., 2004.   
[8] S. Yu, et al., "Scaling-up resistive synaptic arrays for neuro-inspired architecture: Challenges and prospect," International Electron Devices Meeting, IEDM, 2016.

# Motivation: FeFET for Neuromorphic Hardware Accelerator

![](images/87b84723d4f3feb9dc18cb4d6dc18801c68213c88c642f54fae0a851407ac061.jpg)

![](images/c494291a31320bf0157d2a160bf6516148e623dacbf2a7d70a221dfbbe4e15da.jpg)

![](images/904ae944977deda3acb24c25560b4c5f8e9a5eda2a536640abfdf89dc4de4f6b.jpg)

![](images/51312563d5223a7eb52cf730b87366d948a89c6722df628c57816391ccc37ac6.jpg)  
Fig. 2: Comparison of analog synapses for on-chip learning. $\mathrm{Hf}_{0.5}\mathrm{Zr}_{0.5}\mathrm{O}_2$ (HZO) FeFET based analog synapse exhibits the desired characteristics of high speed electric-field controlled switching and symmetric potentiation and depression, allowing fast training of high accuracy neural networks.

Fig. 1: (a) Deep neural networks require dense memory and computation of inner-dot products. (b) Structure of FeFET psuedo-crossbar array. (c) Principle of analog synapse operation where partial polarization switching results in gradual programming of the channel conductance $(\mathrm{G_{ds}})$ .

<table><tr><td colspan="4">Analog Synapse Devices</td></tr><tr><td>Type</td><td>Filamentary RRAM</td><td>Interfacial RRAM</td><td>Ferroelectric</td></tr><tr><td>Mechanism</td><td>current + field assist</td><td>current + field assist</td><td>electric-field</td></tr><tr><td rowspan="3">Prototypical behavior</td><td>Identical pulses</td><td>Identical pulses</td><td>non-identical pulses</td></tr><tr><td>Conductance</td><td>Conductance</td><td>Conductance</td></tr><tr><td>Pulse # [2]</td><td>Pulse # [3] [4] [5]</td><td>Pulse # This Work</td></tr><tr><td>Symmetry</td><td>Low</td><td>High</td><td>High</td></tr><tr><td>Accuracy</td><td>Low</td><td>High</td><td>High</td></tr><tr><td>Speed</td><td>ns</td><td>ms</td><td>ns</td></tr></table>

# Preisach Modeling Framework of Multi-Domain Response in HZO

![](images/687371a162e1fe74a942e1290c7ae2a0c3c3e7b42010f44121781f77605f4088.jpg)

![](images/859d1b5c0206836115cd39d9a113ceb8eb249b85f0ef7a3c805476dc41e7a10d.jpg)

![](images/91e4724ea77246a6aaba518dffc35190d19e1a8837d66667356fb37ddd831a95.jpg)

![](images/35ec7ff85e303c5c40c4d6f27cb36dc26f7b6237cc166acad9455c7dfa20ac09.jpg)

![](images/7e80bd72d47c69f5f351fb662ae5b18a4760e5d9b64706393e95189b8e448332.jpg)  
Fig. 4: (a) MFM capacitor applied voltage transient used to measure history and memory wipeout of previous minor loop trajectories. This is observed in experiment by the reduction in the slope (dP/dV) of minor loops near $\mathrm{E_c}$ (b). (c) The simulated response of the ferroelectric accurately captures the history and trajectory of the minor loops.

Fig. 3: The multi-domain response of HZO is simulated using a dynamic Preisach model which accurately captures the transient trajectory and polarization of the ferroelectric for arbitrary voltage amplitudes and pulse widths as in [7].

![](images/26a35de19b296dca263d5cdee8cd1dc35133ec1dca800d7fd79486db98774641.jpg)  
Fig. 5: $\mathrm{P_r}$ is measured after the application of potentiation/depression pulses, where $\mathrm{P_r}$ is calculated by integrating the transient current according to the equation in the lower right.

![](images/b2312dc1d40f7ea6255ccfed5adbba2d8e452888f95a009e119bab4ceec1ad03.jpg)

![](images/3c931852f4133ed4712b820404fc1ab4c1cec4a220d28f82e4c855620a7ad0e9.jpg)

![](images/9ffafeeb8e4f8f13c5c93ccd643004e9e56d3fe9c1769195fe1a423d33d8e205.jpg)  
Fig. 6: Measured and simulated $\mathrm{P_r}$ vs. programming pulse number. (a) Scheme 1: results in a limited number of polarization states with asymmetric response. (b) Scheme 2: modulation of the pulse width improves upon the characteristics at the cost of increased latency. (c) Scheme 3: exhibits the greatest number of states with symmetric response due to optimal sampling of the $E_c^{\pm}$ distributions.

![](images/cbf8cb57087236676205476376b54a465b82e7d54b67f7c9b1a4b5bac31456d1.jpg)

![](images/378b25ae871a04d7afed723aef0a6f3bd6148966ab092757b6cfd22a2aa6132a.jpg)

![](images/772bf0c4cf16c072a13faf9fe4757c916531961cd429a492ddce854be24286b5.jpg)

![](images/8841488a06a27bcee2c334fa62929a0cd2b6bc0269664561bfa1938e41ec317f.jpg)

![](images/10714b791ae65d8e635783ab1c42eb0540b652017dc6af96df65d91da3b4b9d0.jpg)  
Fig. 8: Simulated FeFET $\mathrm{I_{DS} - V_{GS}}$ for Scheme 3 polarization values. (a) Potentiation shows gradual decrease in $\mathrm{V_T}$ (b) depression gradual increase in $\mathrm{V_T}$ . $\mathrm{Vds} = 50\mathrm{mV}$ .   
Fig. 9: FeFET channel conductance $(\mathrm{G_{ds}})$ vs. pulse number is symmetric and $\mathrm{G_{max} / G_{min} = 69}$ Vgs,read=1.2V.   
Fig. 7: Modeled minor loop trajectories $(1\rightarrow 2\rightarrow 3)$ for pulse (a) Scheme 2 and (b) Scheme 3. In scheme 2 the increase in $\mathrm{P_r}(1\rightarrow 3)$ is non-equal for each pulse number (P#). While scheme 3 each pulse increases $\mathrm{P_r}(1\rightarrow 3)$ similarly, creating a more linear response.

![](images/fac158ddbe6986779426db97ae99d11830356d829f27ea14ebf3e67de211c995.jpg)  
Synaptic FeFET Characterization

![](images/8a31ae11f416939dbfc2bbb41b530f32a790910e41e373d05c98ba36851ae96d.jpg)

![](images/9b23ff864e89ecdf793fad651c6a93c87805976afc4d75396484048086080657.jpg)

![](images/464b20291641ed9a0ec23ba68504a85ec572ef5bf3c081d1be27b7cf02494f3f.jpg)  
Fig. 11: Measured FeFET channel conductance $(\mathrm{G_{ds}})$ as a function of pulse number for pulse schemes 1-3. The results match the shape of the polarization response in Fig. 6. (a) Pulse schemes 1 and (b) 2 result in low $\mathrm{G_{max} / G_{min}}$ , high nonlinearity $(\alpha_{p,d})$ , and high asymmetry $\left(\left|\alpha_{p} - \alpha_{d}\right|\right)$ . (c) Scheme 3 exhibits $\mathrm{G_{max} / G_{min}} = 45$ and symmetric characteristics, ideally suited for on-chip learning. (d) Definitions of fitting equations for non-linearity $(\alpha_{p,d})$ , asymmetry extraction.

![](images/955c5761aa2606d73c1d32d73df71b404f2605ff8d465413c1c5498e93f39186.jpg)  
Fig. 10: (a) SEM of FeFET with $10\mathrm{nm}$ ALD $\mathrm{Hf}_{0.5}\mathrm{Zr}_{0.5}\mathrm{O}_2$ and $0.8\mathrm{nm}$ interfacial $\mathrm{SiO}_2$ gate stack. (b) Process flow.

![](images/209c054ce946a064013c424b0aa2eb69a31ff578ba033e8ba81205d7cd4bb309.jpg)

![](images/0dd7601cc2b38cd347dbfe2668bf247e4c9b17f78ab30ef76418df8d09c9d293.jpg)

![](images/1c07a6313f2ce9e8055c6fbd2191aef697a6603ea45f633758b52f7feff5d0bc.jpg)

![](images/5f28906b89c5ce364649f622d32de26669ae551a3f0ddecb5891274d2ee17da5.jpg)  
Fig. 13: Gradual shift of $\mathrm{I_{DS} - V_{GS}}$ characteristics to (a) lower $\mathrm{V_T}$ states with successive potentiation programming and (b) higher $\mathrm{V_T}$ states with successive depression programming. Charge trapping reduces the total $\mathrm{V_T}$ swing.

Fig. 12: (a) Comparison of $\mathrm{G}_{\mathrm{max}} / \mathrm{G}_{\mathrm{min}}$ ratios as a function of pulse scheme (target=50x) [8]. The non-linearity (ideal $\alpha_{p,d} = 0$ ) and asymmetry (ideal=0) of the potentiation and depression characteristics are shown in (b) and (c). FeFET scheme 3 achieves near ideal values of $\mathrm{G}_{\mathrm{max}} / \mathrm{G}_{\mathrm{min}} = 45$ , $\alpha_{p} = 1.75$ , $\alpha_{d} = 1.46$ , and asymmetry of 0.29.

![](images/e5959d7f30ee9e7d9ebada2e7eda022622e78f960710f99493ea92eb8ca56a25.jpg)  
Device and System Benchmarking

![](images/ef1806f98780764a933dbc2123f3f0931ca384fdc4ebcb8324c37c98c65d0ac9.jpg)  
Fig. 14: (a) MNIST dataset is trained on a fully connected multi-layer perceptron using NeuroSim [8]. (b) FeFET synapse read scheme where the pseudo-crossbar array calculates the product of the input vector $(\mathrm{V_n})$ and weight matrix $(\mathrm{G_{ds(n,m)}})$ .

![](images/b6ae370c004037b692900572491232148188e17b6bc5052e63273a172a3f927d.jpg)  
Pseudo-crossbar Ferroelectric Synaptic Core   
Fig. 16: Schematic of FeFET synaptic core macro including peripherals used to benchmark system performance of FeFET synapse against other reported analog RRAM synapses.

![](images/74dc45b030f543d596dedbb067975d473059c0ff006ea6a28052dce58ae23218.jpg)

![](images/8515bfb789713a5d9c52898c5db4edd794bf00ff9f5c80be64c8477fd5781375.jpg)  
Fig. 17: Benchmark of system level performance (including peripheral circuits) on 1M images from the MNIST database. FeFET based synapse achieves the highest network accuracy and training speed compared to other analog RRAM. 6-bit SRAM maintains a speed and accuracy advantage but increases chip area 10x compared to FeFET, creating difficulty to scale the network size with SRAM.

Fig. 15: Row-by-row weight update scheme used to potentiate (left) and depress (right) the FeFET conductance within a pseudo-crossbar array. Weight updates are calculated via stochastic gradient descent [8].

<table><tr><td>Analog eNVM type</td><td>\( {\mathrm{{TaO}}}_{x}/{\mathrm{{TiO}}}_{2}\left\lbrack  3\right\rbrack \)</td><td>PCMO [4]</td><td>Ag:α-Si [5]</td><td>\( {\mathrm{{AlO}}}_{x}/{\mathrm{{HfO}}}_{2}\left\lbrack  2\right\rbrack \)</td><td>FeFET (This Work)</td><td>6-bit SRAM</td></tr><tr><td># of conductance states</td><td>102</td><td>50</td><td>97</td><td>40</td><td>32</td><td>- -</td></tr><tr><td>Nonlinearity (weight increase/decrease)</td><td>0.66/-0.69</td><td>3.68/-6.76</td><td>2.4/-4.88</td><td>1.94/-0.61</td><td>1.75/1.46</td><td>- -</td></tr><tr><td>Asymmetry</td><td>1.35</td><td>10.44</td><td>7.28</td><td>2.55</td><td>0.29</td><td></td></tr><tr><td>\( {\mathrm{R}}_{\mathrm{{ON}}} \)</td><td>5 MΩ</td><td>23 MΩ</td><td>26 MΩ</td><td>16.9 kΩ</td><td>559.28 kΩ</td><td></td></tr><tr><td>ON/OFF ratio</td><td>2</td><td>6.84</td><td>12.5</td><td>4.43</td><td>45</td><td>- -</td></tr><tr><td>Weight increase pulse</td><td>3V/40ms</td><td>-2V/1ms</td><td>3.2V/300μs</td><td>0.9V/100μs</td><td>3.65V (avg.)/75ns</td><td>- -</td></tr><tr><td>Weight decrease pulse</td><td>-3V/10ms</td><td>2V/1ms</td><td>-2.8V/300μs</td><td>-1V/100μs</td><td>-2.95V (avg.)/75ns</td><td>- -</td></tr><tr><td>Weight update cycle-to- cycle variation (a)</td><td>&lt;1%</td><td>&lt;1%</td><td>3.5%</td><td>5%</td><td>&lt;0.5%</td><td>- -</td></tr><tr><td>Accuracy for online learning</td><td>~10%</td><td>~10%</td><td>~73%</td><td>~41%</td><td>~90%</td><td>~94%</td></tr><tr><td>Area</td><td>1,071.3 μ \( {\mathrm{m}}^{2} \)</td><td>1,071.3 μ \( {\mathrm{m}}^{2} \)</td><td>1,072.0 μ \( {\mathrm{m}}^{2} \)</td><td>3,657.2 μ \( {\mathrm{m}}^{2} \)</td><td>1,190.4 μ \( {\mathrm{m}}^{2} \)</td><td>10,311 μ \( {\mathrm{m}}^{2} \)</td></tr><tr><td>Latency for online learning (1M images)</td><td>1132 years (3.57x1010 s)</td><td>22.19 years (7.00x108 s)</td><td>13.3 years (4.20x108 s)</td><td>1.77 years (5.60x107 s)</td><td>9.33 hours (3.36E4 s)</td><td>7.76 s</td></tr><tr><td>Energy for online learning (1M images)</td><td>65.86 mJ</td><td>29.4 mJ</td><td>87.94 mJ</td><td>150 mJ</td><td>98.01 mJ</td><td>6.98 mJ</td></tr><tr><td>Leakage power</td><td>35.29 μW</td><td>35.29 μW</td><td>35.29 μW</td><td>35.29 μW</td><td>35.29 μW</td><td>1.1 mW</td></tr></table>