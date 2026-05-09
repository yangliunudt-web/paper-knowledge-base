---

title: "Memristor Spiking Neural Network for Shortest Path-Based Graph Learning"
authors:
  - "Ziting Peng"
  - "Xiaolong Zhao"
  - "Jiajun Xu"
  - "Yuan Fan"
  - "Shengbo Wang"
  - "Jialin Rong"
  - "Chenyue Sun"
  - "Yufei Kuang"
  - "Zhiyuan Wu"
  - "Jianmin Li"
  - "Ming Liu"
date: "2025-01-01"
year: 2025
journal: "Science Advances"
doi: "10.1126/sciadv.adv2312"
abstract: "Parallel and energy-efficient searching of the shortest paths on a large graph is\
  \ challenging. Conventional methods commonly used are sequential and computing intensive,\
  \ rendering them inadequate for addressing largescale and real-time situations.\
  \ Here, we propose a highly parallel, computation- and energy-efficient approach\
  \ to shortest path–based graph learning based on an emerging memristor spiking neural\
  \ network via algorithmdevice codesign. The shortest path is obtained parallelly\
  \ in nature using simultaneous spike traveling instead of arithmetic calculation,\
  \ achieving extremely low time and space complexity. A nonlinear weight mapping\
  \ approach is proposed to counterbalance the neuron intrinsic nonlinearity to guarantee\
  \ accuracy to support largescale graphs. The memristor hardware capability is experimentally\
  \ demonstrated in unsupervised and supervised classification tasks. The estimated\
  \ energy efficiency of 517.82 giga-traversal edges per second per watt outperforms\
  \ field programmable gate arrays by three to four orders of magnitude, providing\
  \ a pathway toward highly energy-efficient graph computing hardware."
abstract_cn: "大规模图上最短路径的并行高效搜索具有挑战性。传统方法通常是顺序且计算密集的，难以应对大规模和实时情况。本文提出一种基于忆阻器脉冲神经网络的高度并行、计算和能效高的最短路径图学习方法。最短路径通过同时脉冲传播而非算术计算自然并行获得，实现极低的时间和空间复杂度。提出非线性权重映射方法抵消神经元内在非线性以保证精度。实验证明该忆阻器硬件在无监督和有监督分类任务中的能力。估算能效\
  \ 517.82 GTEPS/W，超越 FPGA 三到四个数量级。"
cite: "Peng Z, Zhao X, Xu J, et al. Memristor spiking neural network for shortest path-based\
  \ graph learning[J]. Science Advances, 2025, 11(1): eadv2312. DOI: 10.1126/sciadv.adv2312."
aiSum: "忆阻器 SNN 图学习：最短路径并行计算、脉冲传播替代算术、517.82 GTEPS/W、超越 FPGA 3-4 个数量级。"
confidence: "high"
keywords:
  - "[[Memristor]]"
  - "[[Neural network]]"
---

# A P P L I E D S C I E N C E S A N D E N G I N E E R I N G

# Fully memristive spiking neural network for energy-efficient graph learning

Tuo Shi1 , Lili Gao1 , Ruixi Zhou1 , Yang Tian1 , Pei Chen2 , Yanting Ding2 , Shuangzhu Tang1 , Huiqin Ma1 , Jian Lu1 , Hui Zhang1 , Zhanfeng Wang3 , Bo Lyu1 , Xumeng Zhang2 , Xiaobing Yan3 *, Qi Liu2 *

Parallel and energy-efficient searching of the shortest paths on a large graph is challenging. Conventional methods commonly used are sequential and computing intensive, rendering them inadequate for addressing largescale and real-time situations. Here, we propose a highly parallel, computation- and energy-efficient approach to shortest path–based graph learning based on an emerging memristor spiking neural network via algorithmdevice codesign. The shortest path is obtained parallelly in nature using simultaneous spike traveling instead of arithmetic calculation, achieving extremely low time and space complexity. A nonlinear weight mapping approach is proposed to counterbalance the neuron intrinsic nonlinearity to guarantee accuracy to support largescale graphs. The memristor hardware capability is experimentally demonstrated in unsupervised and supervised classification tasks. The estimated energy efficiency of 517.82 giga-traversal edges per second per watt outperforms field programmable gate arrays by three to four orders of magnitude, providing a pathway toward highly energy-efficient graph computing hardware.

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

In the real world, data can be usually organized in a form of various relations among abundant entities, e.g., social network or biological network (1). This non-Euclidean data structure is naturally represented by a graph defined by vertex (entity) and edge (relation) (Fig. 1A) (2). As a critical and fundamental problem in graph learning, the shortest path problem (SPP) refers to finding the shortest path(s) between vertexes of a given graph (3). Natural or artificial processes, e.g., contagious spreading among humans (4) or information dissemination in a social network (5), take place along the shortest paths. Thus, SPP can be directly applied to various graph applications, e.g., biological network inference (6), chemical reaction prediction (7), and machine learning algorithm discovery (8), or indirectly applied as an essential element, e.g., message passing mechanism (9), attention mechanism (10), or graph kernel (11–13) in graph neural networks for various artificial intelligent tasks.

Traditional techniques for this problem, e.g., Dijkstra or Floyd-Warshall algorithm (14), use either sophisticated data structure or have high time and space complexity. Moreover, they are sequential, showing ineffectiveness in time and energy for large-scale and realtime applications. The SPP has also been addressed using the genetic algorithm and ant colony algorithm (15–17). However, it should be noted that these approaches do not guarantee an optimal solution but rather offer a probability of finding one. These algorithms are not suitable for solving large-scale problems because they require a large population to compete for solutions, leading to substantial computational requirements. Recently, there is a trend to use the learning capability of deep neural network to solve SPP (18– 20). Such an approach obtains only approximation solutions and

suffers from scalability and generalization issues. It only works well on small-scale graphs, and a minor change on graph requires retraining of the model. In contrary, autowave-based approaches, for example, pulse-coupled neural network, usually operate in an unsupervised manner (21–23). However, the network behaves as a system of nonlinear differential equations, which necessitates an enormous amount of computation to solve. For special scenarios, a hyperbolic mapping–based approach is proposed with the assumption of latentgeometric rules to solve SPP in incomplete graphs (24). Hence, a parallel and computation-efficient solution to SPP in large-scale and real-time applications is still challenging. A memristor is an emerging semiconductor device. Depending on its physical mechanism, a memristor can be categorized into nonvolatile ones, for example, resistive random-access memory (RRAM), phase change memory, and ferroelectric random-access memory, and volatile ones, for example, threshold switching memory (TSM) (25). The RRAM is typically used as synapses in memristor neural networks, while the TSM is used to construct neurons. A great advantage of a memristor is that it computes directly with physical laws (26), greatly reducing the computation complexity in comparison with traditional complementary metal-oxide semiconductor–based systems (27–37). Moreover, when organized in crossbar arrays, a memristor can realize massively parallel processing (38–40). Therefore, for SPP-based graph learning, a memristor has the potential to implement critical computations in an energy-efficient and parallel manner. However, this approach has not yet been exploited.

This study proposes a memristive spiking neural network (m-SNN) for shortest path–based graph learning. The network architecture incorporates $\mathrm { \hat { T i N } / T a O } _ { x } / \mathrm { H f \bar { O } } _ { x } \mathrm { \hat { / T i N } }$ (RRAM) synapse and codesigned Ti/ $\mathrm { N b O } _ { x } / \mathrm { N b O } _ { y } / \mathrm { P t }$ (TSM)–based neurons. We transform arithmetic operations in SPP into spike timing of SNN, eliminating time- and energy-intensive arithmetic operations in traditional and deep neural network–based methods. The acquisition of the shortest pathways is achieved through the temporal patterns of neural activity. The approach is unsupervised, minimizing the necessity for sample preparation and training. A nonlinear weight mapping strategy addresses the

nonlinear voltage-spiking time features of the neuron and maintains accuracy, enabling the approach to support large-scale graphs. The memristive hardware is experimentally tested in unsupervised graph search (drug screening) and supervised graph classification. In a weighted graph G(V, E), where V and E denotes the number of vertex and edge, respectively, our approach exhibits an extremely low time complexity of O(V·S) and space complexity of O(S), where S indicates the furthest length between vertexes. The estimated energy efficiency of the proposed hardware could outperform field programmable gate arrays (FPGAs) by three to four orders of magnitude and the TOP-1 machine in GreenGraph 500 (reported in June 2024) by ~23.4 times. This potential presents a disruptive solution to the fundamental problems in graph learning and enables highly parallel and efficient graph computing systems.

# RESULTS

# Schematic of the m-SNN for graph learning

In the human brain, each neuron connects with other neurons through synapses, forming a complex neural network (Fig. 1B). From the perspective of graph theory, the SNN can be seen as a biological graph (41), where the SPP refers to finding the shortest path of synapses between a pair of neurons (vertexes), and the synaptic weight can be used to represent the edge length.

A schematic of the m-SNN is shown in Fig. 1C. The vertex is implemented by a leaky integrate-and-fire (LIF) neuron circuit. The circuit is composed of a series resistance and a $\mathrm { T i } / \mathrm { N b } { \mathrm O _ { x } } / \mathrm { N b } { \mathrm O _ { y } } / \mathrm { P t }$ TSM device. The threshold switching behavior of the device is used to realize the leaky and fire behavior in the LIF neuron, while the

parasitic capacitance is for integration. The edge weight is realized with the conductance of a TiN/TaOx/HfOx/TiN RRAM device. For the SPP, the start neuron is first initiated by an externally applied voltage pulse. Afterward, the spike emitted by the start neuron spreads along all connected edges. The current through the RRAM synaptic device is converted by a transimpedance amplifier (TIA) to input the voltage of the LIF neuron. As a result, the path length from the start neuron to the current neuron is naturally reflected by the spike timing.

# Characterization of the artificial neuron and synapse

As elucidated in Fig. 1C, the fundamental principle underlying the m-SNN framework is the utilization of spike timing to encode path length. A crucial concern is that it is important to have a linear relationship between the path length, which is represented by the weight of the edges, and the timing of spikes. It is imperative to establish a linear relationship because of the nature of path length calculation, which involves the summation of subgroup path lengths. Deviating from this linear relationship would clearly contravene this fundamental concept, resulting in errors, as depicted in the left panel of Fig. 2A. Nevertheless, as discussed in the circuit model (outlined in Materials and Methods), the correlation between the input voltage and the spike timing is intrinsically nonlinear. The nonlinearity exhibited by neurons can be mitigated using two distinct approaches: hardware and software. The hardware technique is the preferred method for achieving high energy efficiency. One potential approach involves the implementation of additional nonlinearity within the synapse or peripheral circuit, such as a TIA, to counterbalance the neuron nonlinearity. While it is possible to construct a peripheral

circuit to achieve nonlinear conversion, its flexibility will be constrained. In contrast, the implementation of nonlinearity in the mapping from edge weight to device conductance can be premeditated and offer notable adaptability. Here, we propose a nonlinear mapping strategy to counterbalance the intrinsic nonlinearity, as illustrated in the right panel of Fig. 2A and described as follows (derivation of the mapping strategy and parameter declaration are discussed in Materials and Methods)

where

k is the parameter determining the ratio between the spike timing and the edge weight; it is determined according to the available conductance range of RRAM and the input voltage range of the TSM-based neuron. It should be noted that in the choice of the k value, the variability of RRAM and TSM devices should be considered. $\boldsymbol { I _ { \mathrm { o u t } } }$ is the current through the synaptic device. G is the device conductance, and W is the edge weight before mapping.

Another concern is that in large-scale graphs, the number of edges is numerous, resulting in a wide range of edge weights. In the calculation procedure of hardware, the edge weight of the graph is first nonlinearly mapped to the conductance of the RRAM device and then linearly represented by the input voltage of the neuron. To accurately represent weight information, it is necessary for the spike timing or input voltage of the neuron and the conductance of the synapse to have a broad range. This allows for the successful implementation of the calculated conductance after the weight nonlinear mapping and the subsequent input voltage of the neuron, which is directly proportional to the conductance, in physical devices. For the neuron, the input voltage range or voltage ratio $V _ { \mathrm { r a f i o } }$ (defined in Eq. 14 in Materials and Methods), in which neuron LIF behavior can occur, is finite and should be extended to increase the information coding capability of neurons to support large graphs. For the LIF behavior, the $V _ { \mathrm { r a t i o } }$ is influenced by threshold voltage $V _ { \mathrm { t } }$ and hold voltage $V _ { \mathrm { h } } .$ Meanwhile, for the integrate-and-fire behavior, the $V _ { \mathrm { r a t i o } }$ is influenced by the breakdown voltage $V _ { \mathrm { b r e a k d o w n } }$ and Vt (Eq. 15 in Materials and Methods). Because Vbreakdown is typically larger than $V _ { \mathrm { h } } ,$ the coding scheme is selected to be the time to the first spike (TTFS) (42) to enable a large $V _ { \mathrm { r a t i o } } .$ .

We codesigned a TSM device structure by analyzing its influence on $V _ { \mathrm { r a f i o } }$ from the aspect of finite-element simulation and experiment (see Supplementary Text). Then, we fabricated a TSM device with a structure of $\mathrm { T i } / \mathrm { N b } { \mathrm { O } _ { x } } / \mathrm { N b } { \mathrm { O } _ { y } } / \mathrm { P t }$ according to the process in Materials and Methods. The thicknesses of the $\mathrm { { N b O } } _ { x }$ and $\mathrm { N b O } _ { y }$ layers are 40 and 10 nm, respectively. The NbOx insertion layer is more oxygen deficient than the NbOy layer. The structure and element distribution of the device are studied via transmission electron microscopy in fig. S5, confirming the Ti/niobium oxide/Pt structure. Then, the valence states of the niobium oxide layer are further characterized by electron energy loss spectroscopy (fig. S6, A to C) and

x-ray photoelectron spectroscopy (fig. S6D). The analysis on valence states (detailed in Supplementary Text) suggests the existence of the $\mathrm { N b O } _ { x } / \mathrm { N b O } _ { y }$ structure.

A typical threshold switching behavior of the TSM device in the current-voltage (I-V) test is shown in Fig. 2B. The device is first electroformed at a voltage of 5 V under a compliance current $( I _ { \mathrm { C C } } )$ of $4 0 0 \mu \mathrm { A } .$ . Afterward, the threshold switching behavior is observed with a threshold voltage of 1.46 V and a hold voltage of 1.22 V $( I _ { \mathrm { C C } } = 3 0 0 \mu \mathrm { A } )$ . The LIF behavior of the TSM device with a 10-kilohm series resistance under a 3-V input voltage is shown in Fig. 2C. The spiking rates of the LIF behavior are measured with varying input voltage amplitudes at load resistances of 10, 20, 30, and 40 kilohms, as shown in Fig. 2D. It is suggested that neuron oscillation occurs in a restricted region. The TTFS is measured in Fig. 2E. With increasing input voltage, the TTFS decreases. The relation between the input voltage and the spike timing is highly nonlinear. Figure 2F shows the statistically calculated $V _ { \mathrm { r a t i o } }$ using the rate and TTFS encoding schemes based on experimental data. The $V _ { \mathrm { { b r e a k d o w n } } }$ used for calculation is obtained from 5 TSM devices, while the other parameters are measured from 40 TSM devices with each tested for 10 cycles. It is obvious that TTFS encoding enlarges the $V _ { \mathrm { r a t i o } }$ by ~5.23 times compared with the rate one. Figure 2G demonstrates experimental results of weight mapping of edge weight on the memristor hardware. The k values for the four types of neurons with 10-, 20-, 30-, and 40-kilohm load resistances are 0.13, 0.11, 0.11, and 0.12, respectively. The ꞵ value is ${ 1 0 } ^ { 6 }$ ohms, corresponding to a transimpedance gain of 120 dB·ohms of the TIA. A highly linear relation between edge weights and spike timing is obtained, verifying the feasibility of the proposed nonlinear mapping strategy. Figure 2H shows a typical resistive switching behavior of the one-transistor-one-resistor (1T1R) RRAM cell. The SET process is abrupt, while the RESET process is gradual. Therefore, in the programming of the cell, we use primarily the RESET process to tune finely the conductance (30). The obtained conductance of 2000 times tuning is shown in Fig. 2I, where a highly linear and symmetric conductance variation is observed. The conductance ON/OFF ratio of the RRAM device can be kept at ${ > } 1 0 ^ { 2 }$ in the tuning process. Following the nonlinear mapping, there is a linear relationship between the conductance of RRAM and the input voltage of the neuron. Given that the ON/OFF ratio of the RRAM is much greater than the $V _ { \mathrm { r a t i o } }$ of the TSM-based neuron, the extensive range of conductance in the RRAM device will not pose a limitation in encoding weight information. Therefore, it is crucial to optimize the $V _ { \mathrm { r a t i o } } ,$ as mentioned above.

# Solving SPP in an undirected weighted graph

The capability of the m-SNN is experimentally demonstrated in an undirected weighted graph based on a hardware system developed in cooperation with the College of Electronic Science and Technology, National University of Defense Technology (fig. S7). The experiment tends to find all-pair shortest paths in an undirected weighted graph G(8, 12) (Fig. 3A). The hardware architecture (detailed in Supplementary Text and fig. S10) is illustrated in Fig. 3B with the experimental flow shown in Fig. 3C. The neurons only fire once in the problem solving. During the execution, we track the activation state of each neuron to ensure that a neuron does not send a spike to a neuron that has already been activated. This mechanism ensures that neurons do not fire repeatedly, even in the presence of circular connections. The conductance of the 64 array cells after mapping is shown in Fig. 3D. The position information in the RRAM array of

conductance mapping in Fig. 3D is shown in fig. S11. Positions colored in light gray indicate no conductance mapping. The input voltage to the neurons (output signals from the TIAs) on the weighted graph G(8, 12), starting from neuron A, is shown in fig. S12. Each row in fig. S12 shows the input voltages received by that neuron from other neurons. Positions colored in light gray indicate no voltage transmission between the corresponding neurons. Then, a start neuron, e.g., neuron A, is selected and fired by applying an initial voltage pulse on it. Afterward, the remaining neurons fire accordingly with the spread of the spikes and their fire timing is recorded. Figure 3E illustrates the experimentally monitored spike timing of the neurons in the graph when neuron A is the start neuron. The process of finding the shortest path from neuron A is illustrated in Fig. 3F. The sequence is A-G-B-E-H-C-F-D. With the known neuron connectivity, the shortest paths from A to all the other vertexes are as follows: A-B, A-C-D, A-G-E-F, and A-G-H. For example, according to the calculated sequence, the shortest distance from A to B is considered as A-G-B. However, since G and B are not connected, G is removed and the shortest path is A-B. The all-pair shortest paths, i.e., the shortest graph distances between every pair of vertexes in the given graph, are obtained experimentally using above methods and shown in table S2. Here, route optimality represents the proportion of accurately identified shortest paths between a pair of vertexes to the total number of shortest paths. The effects of device noises are systematically analyzed via simulation (detailed in Supplementary Text), showing the high robustness of our approach against noise.

# Drug screening

We now apply the m-SNN to drug screening (43), which is an unsupervised learning task. The graph for drug screening is composed of disease genes and drug targets, as shown in Fig. 4A. The dataset and sub–protein-protein interaction (PPI) network construction are detailed in Supplementary Text. The drug screening task relies on the evaluation of the relationship between drugs and diseases in the interactome, which involves quantifying the proximity between drug targets and disease proteins. Here, we use shortest path–based methods to quantify the proximity with the path experimentally measured by the m-SNN hardware.

Figure 4B shows an illustrative graph in the sub-PPI network composed of four drug-disease associations between gliclazide (G), type 2 diabetes (T), daunorubicin (D), and acute myeloid leukemia (A). G and D are drugs, and T and A are diseases. The shortest paths between the targets and gene proteins on the graph are obtained experimentally by the m-SNN hardware (Supplementary Text). The conductance after weight mapping for the graph of drug-disease extracted from the PPI network is shown in fig. S13. A chord diagram (Fig. 4C) is used to represent the experimentally obtained shortest path length. Each vertex is represented by a fragment on the outer part of the circular layout. The size of the arc is proportional to the length of the shortest path.

Because a disease may have several associated proteins and a drug may have several target proteins, the distance between disease and drug is not straightforward and can be calculated according to

shortest distance $d _ { s } ,$ kernel distance dk, center distance $d _ { \mathrm { c c } } ,$ and separation distance $d _ { \mathrm { s s } }$ using the obtained shortest paths. Definitions of the four distance methods are presented in Supplementary Text. Afterward, we choose a relative proximity (z) to evaluate the relationship (43). This approach not only looks at direct interactions but also includes indirect pathways and network topology. The performance of the four methods is evaluated by the area under receiver operating characteristic curve (AUC, Supplementary Text), as shown in Fig. 4D. For the sub-PPI network, the shortest method reaches the best performance of 79.2%. As an example, the relative proximities of the four pairs in Fig. 4B are compared in Fig. 4E. The conclusions drawn from the hardware (marked with a suffix _exp) are consistent with that from software. For the four distance methods, only the shortest method obtains the correct conclusion: The G-T and D-A pairs are relevant, while the G-A and D-T ones are not. The results demonstrate that the proposed approach is effective in unsupervised graph learning tasks.

# Graph classification

To tackle a challenge that better reflects supervised learning on graphs, we further used the m-SNN to experimentally realize a graph kernel and a multilayer neural network for the purpose of graph classification. Figure 5A illustrates the flow chart of graph classification using the shortest path–based graph kernel. Details about the PPI dataset and the construction of the graph neural network are discussed in Supplementary Text.

Figure 5B shows the experimentally obtained shortest path length in 1 of the 86 graphs with 161 nodes (vertexes) and 667 edges. The path length is rounded so that it can be fit into the distance vector. The rounding method is detailed in Supplementary Text. Figure 5C demonstrates the similarity of each of the 86 graphs to the other graphs. The matrix contains 86 feature vectors for classification. The experimental test accuracy of the memristive classifier (detailed in Supplementary Text) after each training epoch is illustrated in Fig. 5D. The array weights before and after in situ training are shown in fig. S15. The experimental accuracy (83.33%) achieved by the hardware is equivalent to that of software training. Figure 5E shows a comparison of the shortest-path kernel with other kernel methods. The hardware demonstrates a greater level of test accuracy over the three software benchmark models, underscoring the suitability of our approach for graph learning tasks.

For situations with limited hardware resources, we adopt a strategy that simultaneously performs weight mapping and shortest path searching (detailed in Supplementary Text and fig. S16). This approach involves dividing connection weights into multiple subgroups and sequentially mapping them onto hardware, thereby using limited hardware resources more efficiently. However, this method also introduces additional time costs, including data transfer time, configuration time (e.g., weight mapping), and increased delays because of the serialization of operations. This method achieves a reduction in space requirements at the cost of an increase in processing time.

The proposed approach is evaluated from the aspects of computational complexity and energy efficiency. For the all-pair shortest path, the time complexity of our approach is O(V·S), and the space complexity is O(V) (detailed in Supplementary Text), demonstrating superior time and space efficiency over other contemporary methods (table S3). Its complexity is defined by the length of the shortest path but not the graph complexity or the number of paths inside. This strategy is nondeterministic, ensuring globally optimal solutions. The most

efficient way to find the shortest path from one source node to all other nodes is achieved by a single traversal of the network. Moreover, the energy efficiency of a fully integrated memristive graph learning hardware is evaluated in Materials and Methods using the physical parameters in table S4. Evaluated at the 180-nm technology node, the energy efficiency of the memristor hardware is 517.82 GTEPS (gigatraversal edges per second)/W, which is over three to four orders of magnitude higher than that of FPGA and ~23.4 times higher than that of the TOP-1 machine reported in GreenGraph 500 in June 2024 (listed in table S5). The throughput is estimated to be 12.1726 GTEPS by simulation in a large graph [R-MAT-21-91 (44); detailed in Materials and Methods], which is larger than that of FPGAs. As the graph size increases, the number of concurrently traversed edges increases proportionally, increasing throughput (fig. S17). This implies that our approach can dynamically adjust and accommodate very large graphs.

From the aspect of hardware implementation, the scalability of our approach can be achieved by various scale-up architectures (fig. S18) according to the requirements of practical application scenarios. The shared bus architecture exhibits minimal data transmission latency because of the direct connection between a source and a destination. Its simplicity makes it highly efficient in terms of power consumption and hardware area. Nevertheless, the scalability of the system is constrained by the sequential transfer of data. A crossbar architecture offers enhanced system performance and reduced communication time compared to a bus system because of its capability to establish multiple simultaneous connections between inputs and outputs. However, the addition of more ports results in a substantial rise in resource use. The increased hardware complexity and power consumption of a crossbar stem from the significant rise in demand for hardware resources. Although network-on-chips offer excellent system performance and scalability, they also have disadvantages including high power consumption, resource demands, and latency. The comparison of our hardware with state-of-the-art SNN hardware is shown in table S6. Estimated at the 180-nm technology node, our hardware can achieve a very low energy per synaptic operation (0.35 pJ) compared with state-of-the-art complementary metal-oxide semiconductor and memristor designs. The comparison of our hardware with state-ofthe-art memristor hardware and modern digital processors for graph tasks is shown in table S7. The energy per operation of our hardware is estimated to be 1.93 pJ at the 180-nm technology node, which is significantly lower than those of other memristor hardware (11.3 pJ, 40 nm) (45) and graphics processing unit (20.5 pJ, 7 nm) (46). The power consumption of our hardware is 0.193 mW, which is 37.3 times lower than that using a cross-wired memristive array (47).

# DISCUSSION

In summary, a highly parallel, energy-efficient solution to shortest path–based graph learning with ultralow time and space complexity is proposed and experimentally demonstrated on the basis of a fully m-SNN. Evaluated at the 180-nm technology node, the hardware system has the potential to achieve an energy efficiency ~23.4 times greater than that of the top one machine reported in GreenGraph 500 in June 2024. Since SPP is a fundamental problem in graph learning, our approach can be widely used in various graph applications, ranging from simple tasks, e.g., graph searching, matching, or link prediction, to complex tasks like clustering or classification. It is evidenced that the idea of substituting arithmetic operation with spike timing in bioplausible SNN can greatly reduce the time and

energy consumption, which may act as a valuable guidance for realizing future energy-efficient computing hardware, especially in an edge-computing scenario. Our work opens opportunities for solving fundamental graph problems using emerging memristors and may provide an intriguing way toward highly efficient graph learning hardware.

# MATERIALS AND METHODS

# Fabrication of memristor arrays

For the TSM device, initially, a layer of Pt (35 nm) was deposited on the $\mathrm { S i O } _ { 2 } / \mathrm { S i }$ substrate using the electron-beam evaporation technique to function as the bottom electrode. In addition, a 5-nm Ti layer was deposited between the Pt layer and the $\mathrm { S i O } _ { 2 }$ layer to enhance adhesion. Subsequently, a layer of amorphous $\mathrm { { N b O } } _ { x }$ was deposited using the process of sputtering a $\mathrm { N b } \bar { \mathrm { O } _ { 2 + x } }$ target at ambient temperature. Films of $\mathrm { \Delta N b O } _ { x }$ with different compositions were produced by manipulating the oxygen flux, which was measured in standard cubic centimeters per minute (SCCM), during the sputtering process. The oxygen flux for the single-layer (SL) device is measured to be 0.8 SCCM. In the DL device, the deposition of the insertion layer occurs at a flow rate of 0 SCCM, while the active layer is formed at a flow rate of 2.0 SCCM. Ultimately, the uppermost electrode, composed of a 10-nm Ti layer and a 20-nm Pt protective layer, was deposited by magnetron sputtering. Upon completion of the final liftoff procedure, the resultant device structure features a crossbar configuration. The Ti and Pt electrodes of the two type devices have thicknesses of 10 and 35 nm, respectively. The thickness of the $\mathrm { N b O } _ { x }$ layer of the SL device varies from 20 to 50 nm. The thickness of the $\mathrm { { N b O } } _ { x }$ layer of the double-layer (DL) device varies from 10 to 40 nm, while the thickness of the $\mathrm { N b O } _ { y }$ layer is kept at 10 nm, so that the total functional layer thickness of the DL device is the same as its SL counterpart.

The RRAM uses crossbar arrays consisting of 1T1R cells. The structure of each cell consists of a memristor composed of TiN/ $\mathrm { T a O } _ { x } / \mathrm { H f O } _ { x } / \mathrm { T i N }$ layers, which is placed on top of via 5 of metal layer 5. In addition, an n-type metal-oxide semiconductor transistor is included. The metal layers 1 to 4 of the arrays are fabricated using a commercially accessible conventional 180-nm technology, while the metal layers 5 to 6 are fabricated using a laboratory-specific 180-nm procedure.

# Measurement setup

A measuring system has been developed to electronically access and manipulate data on the 1T1R chip, as illustrated in fig. S7. The system comprises a mainboard and four auxiliary boards. The mainboard establishes a connection with an above computer using an ethernet port. Each auxiliary board is equipped with a socket that incorporates $1 2 8 + 6 4 + 6 4 \mathrm { - w a y }$ concurrent analog voltage inputs (ranging from $- 1 0 \mathrm { ~ t o ~ } { + } 1 0 \mathrm { ~ V } )$ with a minimum pulse width of about 2 ns. In addition, the auxiliary board has parallel current sensing capability. The individual row wires or gate wires within the 1T1R memristor array have the capability to be adjusted independently for voltage biasing, ground connection, or high-impedance state. The range of observable resistance is from 300 ohms to 10 megohms. The programming of the system is implemented using an operator library– based approach. This approach is further supplemented by low-level application programming interfaces and drivers.

To investigate the capacitance effect of the TSM devices, we used the Keithley 4200A-SCS parameter analyzer to conduct the experimental

measurements. The device equivalent circuit model consisted of a parallel combination of a resistor and a capacitor, which was then linked in series to another resistor. The rationale behind this observation is that the shell body of the thin film may be conceptualized as a resistor in parallel, and the top and bottom electrodes can be conceptualized as a second resistor in series. The proposed approach involves simplifying the equivalent circuit model by disregarding the resistor in series based on the predicted theoretical capacitance of the device under test. Consequently, the measurement was conducted using the parallel capacitance and conductance model $( C _ { \mathfrak { p } ^ { - } } G _ { \mathfrak { p } } )$ . It is important to acknowledge that the bias voltage is maintained at a level lower than $V _ { \mathrm { t } }$ (about 1.5 V) to ensure that the device under test remains under the same resistance condition throughout the duration of the experiment. The capacitance measurement was obtained using an input ac signal with a root mean square amplitude of 30 mV and a frequency of 100 kHz.

# LIF neuron circuit analysis

The energy consumption of the LIF neuron occurs only in the integration-and-fire process considering the TTFS information encoding method in this work. The LIF neuron circuit is shown in fig. S19A, with its equivalent circuit shown in fig. S19B. The state equations of the LIF neuron are as follows

where

$V _ { \mathbf { o } }$ is the actual voltage applied at the TSM device. $U _ { s }$ is the voltage potential of an equivalent voltage source for the neuron circuit. $R _ { \mathfrak { p } }$ is the equivalent resistance of the LIF circuit. $V _ { \mathrm { R } }$ and $I _ { \mathrm { R } }$ are the voltage and current on the equivalent resistance, respectively. $I _ { \mathrm { C } }$ is the current through the capacitor. $R _ { \mathrm { i n t } }$ and $R _ { \mathrm { o f f } }$ are the series load resistance and high resistance of the device, respectively. $V _ { \mathrm { i n } }$ is the input voltage.

The general solution to the state equations is

where

τ is the time constant. C is parasitic capacitance of the device. With the initial state of the circuit, i.e., zero potential on the device at time zero, we can obtain the integration time before the first spiking event

$t _ { 0 }$ is the integration time before the first spiking. $V _ { \mathrm { t } }$ is the threshold switching voltage of the device.

For the LIF behavior, it occurs only if the following conditions are both fulfilled

where $V _ { \mathrm { h } }$ is the hold voltage of the TSM device. As a result, the input voltage range in which LIF occurs is

The ratio of the high and low voltage limits is

Thus, for a very large $R _ { \mathrm { i n t } }$ the right term of the above approaches 1 and $V _ { \mathrm { r a t i o } }$ is determined by the product of $V _ { \mathrm { h } } / V _ { \mathrm { t } }$ and $R _ { \mathrm { o f f } } / R _ { \mathrm { o n } }$ . On the contrary, if $R _ { \mathrm { i n t } }$ is very small, then $V _ { \mathrm { r a t i o } }$ is determined solely by $V _ { \mathrm { h } } / V _ { \mathrm { t } }$ . Here, a trade-off between energy consumption and accuracy arises. For small $R _ { \mathrm { i n t } }$ the energy consumption is low, but the accuracy may drop because of limited information encoding capability (small $V _ { \mathrm { r a t i o } } )$ . Meanwhile, for large $R _ { \mathrm { i n t } }$ , the energy consumption is high, but the accuracy may be improved (large $V _ { \mathrm { r a t i o } } )$ .

However, if the TTFS coding scheme is used, only a single spike is enough for information transmission. In other words, integrateand-fire behavior but not the LIF one is obligatory. Thus, the upper limit becomes the device hard breakdown voltage instead of $V _ { \mathrm { h } } .$ The input voltage range is enlarged

# Nonlinear mapping strategy

We assume the mapping from graph edge weight to device conductance to be

where G is the device conductance, W is the edge weight, and f is the mapping function from W to G.

The current through the device is

where $V _ { \mathrm { r e a d } }$ is the read voltage applied on the device.

The current is fed into the neuron via a TIA that converts the current to voltage

where $R _ { \mathrm { T I A } }$ represents an equivalent resistance of the TIA. According to Eqs. 7 and 11 and the above three equations, the relation between G and $t _ { 0 }$ can be established

Assuming a linear relation between W and $t _ { 0 }$

where γ is the slope. Integrating Eq. 20 into Eq. 19, and using the definitions in Eqs. 2 and 3, we obtain

where

# Hardware benchmark

The performance of the m-SNN hardware is evaluated from the aspects of throughput [traversed edges per second (TEPS)] and energy efficiency (TEPS/W). For a single edge, it is implemented by a memristive synaptic device, a LIF neuron, and a TIA. In addition, two inverters and a transmission gate are used to catch and transmit the spiking signal, respectively. The energy consumption of the synapse $\bar { E } _ { \mathrm { s y n a p s e } }$ is calculated as follows

where $V _ { \mathrm { r e a d } }$ and $t _ { \mathrm { r e a d } }$ are the amplitude and width of read voltage pulse, respectively. R is the resistance of the synaptic device.

The energy consumption of the LIF neuron is calculated as

where

here, $P _ { \mathrm { n } }$ is the power consumption of the neuron. $I _ { \mathrm { i n } }$ is the input current.

The energy consumptions of the TIA, inverter, and transmission gate are

where $P _ { \mathrm { T I A } }$ and $P _ { \mathrm { i n v } }$ are the power consumptions of the TIA and inverter, respectively. $P _ { \mathrm { M a t r i x S w i t c h } }$ is the power consumption of Matrix Switch.

The energy efficiency is

Also, the throughput is

where N is the sum of outgoing or incoming neighbor list lengths of all visited vertexes, and T is the total run time. An edge is only counted once if it is visited more than once.

The throughput is calculated by simulation in a “RMAT-21-91” graph, representing a synthetic graph with $2 ^ { 2 1 }$ vertexes and $2 ^ { 2 1 } { \cdot } \mathrm { b y } .$ - 91 edges. The energy per synaptic operation (SOP) is calculated as follows

The energy per operation and power per operation are calculated as follows

# Supplementary Materials

This PDF file includes:

Supplementary Text

Figs. S1 to S19

Tables S1 to S7

References

# REFERENCES AND NOTES

# Acknowledgments

Funding: This work was supported by the National Key R&D Program of China under grant no. 2021YFB3601200 (to T.S.); the National Natural Science Foundation of China under grant nos. U22A6001 (to T.S.), 61888102 (to Q.L.), and 62306291 (to B.L.); the Strategic Priority Research Program of the CAS under grant XDB44000000 (to X.Y. and Q.L.); and Zhejiang Provincial Natural Science Foundation of China under grant no. LQ24F020029 (to T.S.). Author contributions: T.S., X.Z., X.Y., and Q.L. conceived the idea. T.S. and L.G. implemented neural network simulation. T.S., P.C., R.Z., Y.D., H.M., H.Z., and S.T. performed device test and characterization. Z.W., S.T., and J.L. set up the hardware and conducted the measurements. T.S. and Y.T. performed device modeling and simulation. T.S. and H.Z. benchmarked the system performance. T.S., L.G., Y.T., X.Z., H.M., H.Z., B.L., X.Y., and Q.L. performed the data analysis. T.S., L.G., S.T., Y.T., X.Z., B.L., X.Y., and Q.L. wrote the manuscript. X.Y. and Q.L. supervised the project. All authors discussed the results and implications and commented on the manuscript at all stages. Competing interests: The authors declare that they have no competing interests.

Data and materials availability: All data needed to evaluate the conclusions in this paper are present in the paper and/or the Supplementary Materials.

Submitted 10 December 2024

Accepted 1 April 2025

Published 7 May 2025

10.1126/sciadv.adv2312
