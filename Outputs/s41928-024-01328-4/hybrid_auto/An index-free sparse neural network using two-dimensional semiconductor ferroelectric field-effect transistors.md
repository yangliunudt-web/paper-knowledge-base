---

title: "An Index-Free Sparse Neural Network Using Two-Dimensional Semiconductor Ferroelectric\
  \ Field-Effect Transistors"
authors:
  - "Hongkai Ning"
  - "Hengdi Wen"
  - "Yuan Meng"
  - "Zhihao Yu"
  - "Yuxiang Fu"
  - "Xilu Zou"
  - "Yilin Shen"
  - "Xiai Luo"
  - "Qiyue Zhao"
  - "Tao Zhang"
  - "Lei Liu"
  - "Shitong Zhu"
  - "Taotao Li"
  - "Weisheng Zhao"
  - "Yue Hao"
  - "Xinran Wang"
  - "Yi Shi"
  - "Litao Sun"
  - "Peng Zhou"
date: "2024-12-01"
year: "2024"
journal: "Nature Electronics"
doi: ""
abstract: "An index-free sparse neural network using two-dimensional semiconductor ferroelectric\
  \ field-effect transistors as synaptic devices, enabling energy-efficient edge AI\
  \ processing."
abstract_cn: "利用二维半导体铁电场效应晶体管作为突触器件，实现无索引稀疏神经网络，支持高能效边缘AI处理。"
keywords:
  - "[[FeFET]]"
  - "[[Neural network]]"
  - "[[2D materials]]"
  - "[[ferroelectric]]"
  - "[[edge AI]]"
cite: "Ning H, Wen H, Meng Y, et al. An index-free sparse neural network using two-dimensional\
  \ semiconductor ferroelectric field-effect transistors[J]. Nature Electronics, 2024.\
  \ (待补充DOI)"
aiSum: "二维FeFET实现无索引稀疏神经网络，高能效边缘AI处理。"
confidence: "high"
wiki_concepts:
  - "[[Edge computing]]"
  - "[[FeFET]]"
  - "[[Ferroelectric]]"
  - "[[Neural network]]"
---

# An index-free sparse neural network using two-dimensional semiconductor ferroelectric field-effect transistors

Received: 2 February 2024

Accepted: 3 December 2024

Published online: 8 January 2025

Check for updates

Hongkai Ning  1,7, Hengdi Wen1,7, Yuan Meng  1,7, Zhihao Yu  2,3 , Yuxiang Fu  4,5 , Xilu Zou1 , Yilin Shen  1 , Xiai Luo1 , Qiyue Zhao4 , Tao Zhang1 , Lei Liu1 , Shitong Zhu1 , Taotao Li  3,4,5, Weisheng Li  1,3,4,5, Li Li1 , Li Gao  6 , Yi Shi  1 & Xinran Wang  1,3,4,5

The fne-grained dynamic sparsity in biological synapses is an important element in the energy efciency of the human brain. Emulating such sparsity in an artifcial system requires of-chip memory indexing, which has a considerable energy and latency overhead. Here, we report an in-memory sparsity architecture in which index memory is moved next to individual synapses, creating a sparse neural network without external memory indexing. We use a compact building block consisting of two non-volatile ferroelectric feld-efect transistors acting as a digital sparsity and an analogue weight. The network is formulated as the Hadamard product of the sparsity and weight matrices, and the hardware, which is comprised of 900 ferroelectric feld-efect transistors, is based on wafer-scale chemical-vapour-deposited molybdenum disulfde integrated through back-end-of-line processes. With the system, we demonstrate key synaptic processes—including pruning, weight update and regrowth—in an unstructured and fne-grained manner. We also develop a vectorial approximate update algorithm and optimize training scheduling. Through this software–hardware co-optimization, we achieve 98.4% accuracy in an EMNIST letter recognition task under 75% sparsity. Simulations on large neural networks show a tenfold reduction in latency and a ninefold reduction in energy consumption when compared with a dense network of the same performance.

The synaptic connections in the human brain—and in the cerebral cortex, specifically—are highly sparse and dynamic in nature1–5 . Neuroimaging techniques have also highlighted the evolution of the synaptic density across the human lifespan3 : it increases from birth into childhood, reaching a peak in middle childhood, then undergoes pruning and finally stabilizes at a relatively sparse level in adulthood (Fig. 1a). The synaptic connections in a typical adult brain constitute less than 5% of those in a fully connected (FC) dense network, and up to 40% of

synapses are modified daily through pruning and regrowth processes4 . Such dynamic sparsity allows energy efficiency to be maintained while performing complex neurofunctions5 .

Early neurological research established a classical neuron–synapse model, where the superior neuron extends a long axon and connects the dendrites of the subordinate neuron by forming synapses6 (Fig. 1b). This model has inspired the development of artificial neural networks (ANNs)7 . Modern neurocytology further reveals that the synapses

A full list of affiliations appears at the end of the paper.  e-mail: zhihao@njupt.edu.cn; yuxiangfu@nju.edu.cn; xrwang@nju.edu.cn

are dynamic and that the sparsification and regrowth processes are facilitated by an activity-dependent mechanism, involving astrocytes and microglial cells congregating around axons8 (Fig. 1c). These cells influence synaptic connectivity by modulating neurotrophic factors and immune signals. Synapses that are consistently active are strengthened, whereas those that are rarely used are weakened and eventually eliminated. These dynamic processes are completely in situ without external biological signals or auxiliary communications, which maximizes the energy efficiency of the brain.

ANNs are, in contrast, overparameterized with about 95% redundance9,10, and most ANNs—whether implemented on graphics processing units or in-memory computing (IMC) architectures—are deployed on dense hardware. Such densely structured design leads to substantial energy cost, which is likely to be unsustainable in the future11. Recently, brain-inspired sparsification has been used to compress large computer vision and language models12–18. Unlike astrocytes and microglial cells in biological systems, which manipulate synaptic weight locally without external communications, existing artificial intelligence (AI) hardware relies on off-chip memory indexing to prune and update the irregularly distributed sparse weights10,11 (Fig. 1e). During the indexing process, the sparsity information is loaded from off-chip memory to an on-chip buffer, refreshed and read out to compute the weight update.

There is considerable energy consumption and latency overhead associated with indexing, similar to the von Neumann bottleneck11. For instance, during the training of VGG-8 Net (around 13 million parameters) on the CIFAR-10 dataset, the sparsity can reach 89% but memory indexing accounts for 92% of energy consumption and 96% of latency (Fig. 1f; see Methods for details). Although reducing sparsity granularity to layer or block level could reduce the off-chip memory access, the accuracy is compromised and the damage is irreparable after pruning some critical synapses10,11,13,17,18 (Extended Data Fig. 1).

In this Article, we report in-memory sparsity, which places sparsity information as close as possible to the individual weight synapses. The approach means that only in situ adjustments to sparsity information are required to execute pruning and regrowth operations on the synapses or weights. The stored sparsity information can also be used directly in computations without external indexing. Similarly to IMC, in-memory sparsity reduces the need for frequent data exchanges between computational units and memory, but with the distinction that the accessed data are specifically optimized for the sparsity patterns within neural networks (NNs).

# Design and operation of index-free synaptic cell

When we encode the sparsity information locally, a sparse neural network (SPNN) can be mathematically formulated as the Hadamard product of

the sparsity matrix and the weight matrix (Fig. 2a). This was physically implemented by two non-volatile memories in each synaptic cell (in our case, ferroelectric field-effect transistors, FeFETs), one storing the sparsity data and the other the weight data (Fig. 2b). During in situ pruning, small weights were first set to zero and the corresponding sparsity FeFETs were set to the high-resistance state (‘0’), which effectively removes the cell from multiply–accumulate (MAC) operations. After excessive pruning, the cell could be regrown by setting the sparsity FeFET to the low-resistance state (‘1’), enabling weight update operations again (Fig. 2c).

The FeFET devices were fabricated using chemical-vapourdeposited (CVD) molybdenum disulfide (MoS ) as the channel and hafnium zirconium oxide, $\mathsf { H f } _ { x } Z \mathsf { r } _ { 1 - x } \mathsf { O } _ { 2 } ( \mathsf { H Z O } )$ , as the gate dielectric19–28. A three-dimensional (3D) schematic and an optical microscopic image

of the cell are shown in Fig. 2d,e, respectively. The use of MoS offers several potential advantages including scaled device size, low power and back-end 3D integration29–38. By adjusting the thickness of the ferroelectric layer and the ferroelectric-to-dielectric area ratio39, the memory characteristics of the sparsity and weight FeFETs were tuned (Fig. 2f and Extended Data Fig. 2). The sparsity FeFET was tuned to have a large memory window and long retention (more than 10 yr) for non-volatile storage of sparsity information. In contrast, the weight FeFET was designed as an analogue memory with a narrower memory window. This difference in memory windows is crucial to prevent erroneous operations during weight updates. In essence, we replaced the selector transistor in the conventional one-transistor–one-FeFET design21 with a binary, non-volatile FeFET.

An important feature of our design is that the indexing is encoded locally in each synaptic cell without the need for external indexing. During MAC operations in a matrix, when the sparsity FeFET was set to a high-resistance state, the corresponding cell expressed as a pruned synapse, ensuring that the conductance of the weight FeFET remains unchanged upon update pulses. When the sparsity FeFET was set to a low-resistance state, the corresponding cell expressed as an active synapse, allowing updates to the conductance levels of the weight FeFET (Fig. 2g). According to the inference energy $E = V _ { \mathrm { i n } } ^ { ~ 2 } G _ { \mathrm { w e i g h t } } t$ , where $V _ { \mathrm { i n } } , G _ { \mathrm { w e i g h } }$ and t stand for input voltage, weight conductance and inference time respectively, every inactive cell can save up to four orders of magnitude of energy.

For practical applications, large-area device yield and uniformity are critical29–33,37–43. We measured 450 weight FeFETs in a 25 × 18 array, whose electrical characteristics are summarized in Fig. 2h. All the devices showed switching with on/off ratio over 103 , and 99.11% of devices (446 out of 450) showed on/off ratio over 106 . The switching voltage showed a narrow and symmetrical distribution centred at ±4.3 V. Recent works suggest that the ferroelectric properties of HZO can be maintained at 1 nm thickness26. Therefore, the gate voltage could be further reduced by scaling the thickness of hafnium oxide (HfO2) and HZO. We further performed more stringent multibit tests. Statistical analysis on 100 weight FeFETs showed 16 well-separated conductance levels, and almost negligible conductance change over 100, only about 0.05 μS on average (Extended Data Fig. 2g–h). Additionally, both the sparsity and weight FeFETs show robust memory characteristics and thermal reliability at temperatures of 85 °C and 125 °C (Extended Data Fig. 3).

# Software–hardware co-optimizations

To implement an SPNN, we customized a mini SPNN termed MSNet, which is a simplified convolutional NN LeNet-5 (ref. 44), to perform handwritten letter recognition from the EMNIST dataset45 (Fig. 3a). Our MSNet consisted of two convolution layers with 5 × 5 kernels, a pooling layer and an FC layer with a total of 1,060 weights. To map MSNet onto hardware, we fabricated a 25 × 18 array in a pseudo-crossbar structure (Fig. 3b). The details of the array design and testing are given in Extended Data Fig. 4 and Methods.

System-level implementation requires not only underlying hardware but also co-optimizations with software algorithms and data deployment methodologies to achieve the highest accuracy, sparsity and energy efficiency. The conventional method of weight updating on a cell-by-cell basis poses a notable challenge when applied to large-scale hardware. Adhering to this strategy would necessitate a compromise between uniformly updating every cell regardless of sparseness, and selectively skipping pruned cells through an off-chip index. To fully realize the potential of our hardware design, we developed a vectorial approximate update (VAU) algorithm, where each operation was performed vectorially (by rows or columns, Fig. 3d,e, Extended Data Fig. 5 and Methods). For a matrix of M rows and N columns, VAU uses M + N vectorial gradients to approximate the traditional M × N cell-wise gradients (Fig. 3d). The VAU algorithm approximately solves the operation vector OP, such that the calculated weight update matrix ΔW′ = A · OP (where A is the auxiliary matrix) is as close as possible to the accurate weight update matrix ΔW obtained by backpropagation (Fig. 3e). During updating, each vectorial operation performed a row of Hadamard products without any indexing due to the pre-stored sparsity information in each cell.

In addition to reducing complexity, this algorithm also adapts naturally to the SPNN in other aspects. First, when compared with dense NNs, SPNNs inherently have a large fraction of zero weights, which results in ΔW′ being more closely aligned with ΔW. Our simulations have shown that an increase in sparsity from 52.3% to 74.2% leads to a reduction in the mean square error between ΔW′ and ΔW from 0.24 to 0.06 (Extended Data Fig. 5b); when compared with an accurate cell-by-cell

update, the accuracy loss introduced by VAU is negligible (Extended Data Fig. 5c). Second, the fitted approximation as a slight perturbation can effectively prevent training from being bound to the local minimum of loss and accelerate the training convergence7 . Finally, depending on the pseudo-crossbar design, the total number of operations can be further reduced to M + 1 or N + 1 (Extended Data Fig. 5a), which means that, when compared with the cell-by-cell update, the power consumption and latency of VAU can be reduced nearly M- or N-fold.

We further optimized the training scheduling. Existing hardware adopts one-time pruning after training to minimize indexing energy. In contrast, our design provides the possibility to develop progressive update scheduling (Fig. 3c and Methods), consistent with the lifelong dynamic pruning and regrowth in the human brain. This update scheduling performs multiple pruning, updating and regrowth iterations after pretraining. Unlike one-time pruning, progressive pruning can continuously release zero weights through subsequent training, and maximize sparsity while maintaining high accuracy10. However, a poorly adapted scheduling could also cause problems in training convergence. Therefore, holistic co-optimization spanning across several architectural levels from unit cell to training and scheduling is essential to realize a high-performance index-free SPNN (Fig. 3f).

# Index-free training of SPNN

We combined the innovations in hardware, algorithms and scheduling to implement our index-free SPNN training. The training consisted of four stages, namely pretraining, pruning, overpruning and regrowth (Fig. 4a and Extended Data Fig. 6). Following a random initiation of weights, the pretraining stage was performed on the computer for ten epochs, resulting in a Gaussian-like weight distribution (Fig. 4d). From epoch 11, the MSNet transitioned into the pruning stage, which included four pruning operations (52.3%, 63.7%, 66.8% and 74.2%, respectively, at epochs 11, 17, 23 and 26). During the pruning epochs, the absolute weights were sorted in descending order and pruned from the lower end to the predetermined percentage. Following each pruning, the MSNet underwent several training epochs using VAU. At the end of epoch 28, the accuracy reached 93.2% despite 74.2% sparsity in weights (Fig. 4a). The progressive increase in sparsity and trimming of less impactful weights is illustrated by the heatmap in Fig. 4b.

In addition to accuracy, loss is another crucial metric for assessing the quality of NN training. Typically, an NN begins with a relatively high loss, which then converges, decreases and stabilizes at a lower value as training progresses (Extended Data Fig. 8a). We did not observe the escalation of loss during the first four pruning stages, indicating that the pruning preserved the network stability. The two-dimensional loss landscape evolved into a deep and broad valley at epoch 28 (Fig. 4c), suggesting that, despite errors and perturbations, the network maintained good robustness at this stage. As most weights were pruned and did not require updates in every epoch, the SPNN demands far less endurance when compared with a dense NN. This feature is particularly advantageous in addressing one of the most important technical challenges for non-volatile memory matrices in NN computation— endurance—and could extend the operational lifespan and reliability of these memory technologies.

From epoch 29, we performed several additional pruning operations (up to 86.9%); however, in contrast to the second stage, we observed obvious drop in accuracy, indicating overpruning. Beyond a certain threshold even the smallest weight was crucial and accuracy could not be recovered by subsequent training without regrowth (light red curve in Fig. 4a). Concurrently, the loss function valley became steeper and more pronounced (epoch 37, Fig. 4c), indicating that the system was less robust to disturbances. To remedy the effect of overpruning, we adopted a regrowth strategy similar to synaptic restoration in the human brain. During the regrowth epoch (epoch 38), weights were arranged in descending order of gradients, selected and regrown using an algorithm (detailed in Methods). At the end of

epoch 57, an accuracy of 98.4% was achieved, even though the 75% sparsity was similar to the end of the pruning stage (red curve in Fig. 4a). This improvement was attributed to the correction of certain pruning mistakes and the formation of new, potentially more efficient synaptic connections (Fig. 4b). After regrowth, the loss function returned to a wider valley with a lower overall loss level (epoch 57, Fig. 4c). The details of array design and measurements are detailed in Extended Data Fig. 7 and Methods.

A comparison of weight histograms before and after SPNN training reveals that indeed most small weights were pruned and the remaining weights were narrowly and symmetrically distributed on both sides of zero (Fig. 4e). This agreed well with theories and our simulations10,12 (Extended Data Fig. 8c). The small 1,060-weight array demonstrated an experimental recognition accuracy of 98.4% for the letters ‘a–e–p–r–s’ (Fig. 4f, Extended Data Fig. 8), despite 75% of weights being zero, and this validates our index-free hardware, the VAU algorithm and training scheduling.

# Performance projection and benchmark

To evaluate the performance of our index-free SPNN at larger scale, we simulated the VGG8-Net using NeuroSim46. We developed a modified chip architecture, adopting an H-tree structure with three hierarchical levels: array, processing element (PE) and tile (Extended Data Fig. 9a,b). Each tile comprises four PEs with 16 64 × 64 synaptic arrays. An index buffer is integrated at each level to facilitate sparse training. The standard one-transistor–one-FeFET unit cell was modified to a two-FeFET unit cell in accordance with our design. We also introduced various granularities for sparse training: element-wise, vector-wise, block-wise and layer-wise (Extended Data Fig. 9c). To accommodate 13 million parameters in VGG8-Net, a total of 44 tiles were used.

Figure 5a,b shows the weight distributions of the trained SPNN and dense NN, the latter being trained on the same hardware but without pruning. The dense NN showed a Gaussian distribution centred around zero, while the SPNN displayed a distinctive, suspension-bridge-like distribution. The SPNN achieved 88.5% overall sparsity, translating into a compression ratio of 8.7. Figure 5b shows the sparsity across different layers in the SPNN. Deeper layers (such as Conv4–6) have higher sparsity because complex and abstract features detected by deeper layers are more specific and less frequently encountered in the input data when compared with simple features such as edges. Moreover, in deeper layers, each neuron has a larger receptive field, which is a delimited medium where some physiological stimuli can evoke a sensory neuronal response in specific organisms. Since complex features are less common than simple features, neurons with larger receptive fields are activated less often, leading to higher sparsity.

Finally, we benchmarked the accuracy, latency and energy consumption of the index-free SPNN against dense NN and SPNN with external indexing (Fig. 5c). The methodologies and simulation details are provided in Methods and Extended Data Fig. 9d. Here, we normalized all the metrics of the dense NN to 1. When element-wise sparsity was introduced, the latency and power consumption increased by 2.7-fold and 1.5-fold respectively, due to off-chip memory indexing to handle the sparsity information. This highlights the critical trade-off in current ANNs: the efforts to reduce redundancy inevitably led to increased complexity and resource demand. On the other hand, our index-free SPNN showed 27.5-fold (10.3-fold) latency reduction and 13.6-fold (9.2-fold) decrease in energy with minimal accuracy loss when compared with external indexing SPNN (dense NN). Note that these numbers increase to 31.4-fold and 13.8-fold when using differential pairs (Extended Data Fig. 10).

# Conclusions

Inspired by the human brain, we have developed an in-memory sparsity architecture and created an inherently fine-grained SPNN hardware without external memory indexing. Combining VAU algorithms and optimized scheduling, the SPNN achieved 98.4% accuracy in handwritten letter recognition under 75% sparsity. The underlying hardware is based on CVD-grown MoS2 with nearly 100% device yield. Our approach could be used to develop more sustainable AI. It can reduce the energy and latency in large-NN training, and could lead to more efficient hardware utilization when around 90% of weights are empty. The similarities between our SPNN hardware and the brain could also help in understanding fundamental neurological questions, such as the origin of biological intelligence.

# Methods

# Materials and device design

Single-crystalline monolayer MoS films were grown at 1,000 °C in a customized CVD furnace. We used a specially designed C/A-plane sapphire wafer as a substrate, and sulfur powder, 5 sccm ${ \bf O } _ { 2 }$ and Mo sheets (carried by 50 sccm Ar) as precursors.

The metal–ferroelectric–metal–insulator–semiconductor structure is used for the weight transistor and sparsity transistor design. For the weight device, a metal–ferroelectric–metal capacitor is connected to a back-gate MoS transistor, turning the previous back gate into a floating gate. The $C _ { \mathrm { F E } } / C _ { \mathrm { D E } }$ ratio of 0.026 is designed to balance the memory window, endurance and data retention, where the $\mathbf { C } _ { \mathrm { F E } }$ and $\mathsf { C } _ { \mathrm { D E } }$ are the capacitance of ferroelectric film and dielectric film in the gate stack, respectively. For the sparsity device, another capacitor with the same thickness is connected head to head to the back gate. Thus, the gate is on the same layer as a floating gate. The purpose of this design is to double the memory window of the sparsity transistor without adding processes. The $C _ { \mathrm { F E } } / C _ { \mathrm { D E } }$ ratio for the sparsity transistor is 0.0065.

# Fabrication of index-free array

The array has 450 unit cells with 18 rows and 25 columns. Each cell contains one weight transistor and one sparsity transistor organized in a pseudo-crossbar structure, surrounded by four lines for interconnect: bit line, sparsity line, data input line and data output line.

We used a silicon substrate with 275 nm $\mathrm { S i O } _ { 2 } .$ First, we define and evaporate the row-line metal (15 nm Ti/Pt) using electron-beam lithography (EBL) and an electron-beam evaporator (EBE), respectively. Second, a 20-nm-thick $\mathrm { S i O } _ { 2 }$ layer is deposited by plasma-enhanced atomic layer deposition with the precursor diisopropylaminosilane

(DIPAS). Third, we define and evaporate back-gate metal (12 nm Ti/Pt) with EBL and EBE again, followed by 10 nm ferroelectric HZO film ALD deposition with precursors tetrakis(dimethylamido) (TDMA)-Hf and TDMA-Zr. Then, the floating-gate metal (12 nm Pt) is defined with EBL and evaporated with EBE, and a rapid thermal annealing is performed on the chip in N2 atmosphere at 450 °C. Next, using plasma-enhanced atomic layer deposition, a 12 nm dielectric HfO2 film is deposited with precursor tetrakis(ethylmethylamido) (TEMA)-Hf. Next, we define using EBL and etch oxides with BCl3/Ar gas in a GSE C200 plasma etcher to form a via. After this, we transfer a CVD monolayer MoS2 to a 35-nm-thick flat Au film supported by polydimethylsiloxane (PDMS) and polymethylmethacrylate (PMMA), define with EBL, etch Au not in the channel region with 100% KI solution and etch MoS2 with SF6 and O2 plasma in a reactive ion etcher. To form S/D metal and column-line metal, we define them with EBL and evaporate 15 nm Ti/45 nm Pd/15 nm Ti with EBE. Here, S and D stand for source and drain terminal of a transistor, respectively. Then we directly etch Au above MoS in the channel region under the S/D metal mask with 100% KI solution. Finally, the chip is annealed at 200 °C in a 10−6 Pa vacuum.

# Measurement set-up

The single-device-level test is performed using a Keithley 4200 semiconductor characterization system with four source-measure units (SMUs) for the transfer curve test and 4,225 remote pulse modules for the multistate test. For array-level tests, we developed an automatic test system (Extended Data Fig. 4) based on a National Instruments PXI-4163 SMU, three PXI-2532B switch matrices, a home-made 128-line feedthrough, customized probe cards (86 lines) and a vacuum probe station. Probe cards were carefully attached to the original single-probe holder of the probe station, supporting movement in XYZ directions. A microscope with a CCD (charge-coupled device) was used for positioning while probing. We deployed three PXI-2532 switch matrix cards with 16 × 32 1-Wire topology, providing a total of 1,536 connections (16 inputs and 96 outputs). These 96 outputs were connected to 86 pads of the device under test (DUT), and 16 inputs led to 16 SMUs of 24 in the one PXI-4163 card. One of the 16 SMUs was fixed to the ground during the full test. Through checking, the resistance introduced by wires, contact and switch matrices is lower than 10 Ω, which is negligible when compared with the resistance of the DUT.

The hardware code for automatic test and data acquisition (Extended Data Fig. 4a) is developed on the nidcpower and niswitch library in the nimi-python interface. The routing of signals was set by two encoders. Encoder 1 mapped 16 SMUs to switches, and encoder 2 mapped the device under test positions to the order of switches. After encoding, the procedure proceeds with the core hardware operations for sparse training (cyan blocks in Extended Data Fig. 4b). The code activated sources to measure currents for inference or performed sets of pulses for training. All parameters here were carefully optimized for the fabricated array before the full test. Once the core operations finished, all switches were disconnected, data were uploaded to the cloud and the procedure went on to the next layer or the next epoch. Additionally, the software codes for pruning and training scheduling are developed on the basis of the PyTorch platform (other sections in Methods). The hardware and software codes are deployed on two personal computers and data are transferred between them in real time via the network.

# Definition of the pruning granularities in simulation

To investigate the impact of various pruning methods on model and chip performance, we defined and implemented three types of unstructured or structured pruning granularity by simulation: unstructured element-wise pruning, structured vector-wise pruning and block-wise pruning, ranging from fine grained to coarse grained.

Element-wise pruning is the finest-grained granularity, which allows irregular sparse patterns in the weight tensor. It achieves the

highest training accuracy among all evaluated granularities and may outperform the dense model in certain configurations10,11. However, the aforementioned index overhead obviously impedes the chip performance of element-wise pruning (Fig. 5c). In our simulation, we adopted a direct-indexing scheme, where a one-bit index is assigned to each weight to signify whether it is pruned or not. Furthermore, in an IMC accelerator, vector–matrix multiplication (VMM) operations are executed in parallel by summing up the current along each weight column. Hence, element-wise weight sparsity cannot bypass the VMM calculation generally, hindering the acceleration of the feedforward process. On the other hand, during backpropagation and weight update, unstructured weight sparsity reduces the data transfer of delta weights proportionately, thus accelerating the computation.

In structured pruning, the grain size of a one-dimensional vector and two-dimensional (2D) block in the mapped weight matrix is defined as vector-wise and block-wise sparsity, respectively. In IMC hardware, weights are flattened into 2D matrices and mapped to predefined synaptic arrays, typically composed by a crossbar array of non-volatile memory devices and its CMOS (complementary metal–oxide–semiconductor) peripheral circuits. By matching the size of a pruning group to the size of a synaptic array, we define the structured pruning granularities in an IMC-friendly pattern to optimize the chip performance: vector-wise sparsity involves pruning weight columns in the mapped weight matrix, with the length of a vector defined as equal to the number of rows in a synaptic array. Consequently, each pruned vector conserves the energy of calculating one vector–vector multiplication during feedforward by deactivating the corresponding analogue-to-digital converter (ADC) and shift-adder of that column in the array.

Similarly, for block-wise sparsity, the size of a pruning block is equal to that of a synaptic array. As a result, pruned arrays are simply shut down to conserve energy in the feedforward process. During the training process, a direct-indexing scheme is also adopted for structured pruning, except that the assignment of indices is reduced to 1 bit per vector/block rather than per element when compared with unstructured pruning.

# Design of MSNet, dataset and array-level data flows

MSNet contains two convolution (Conv) layers, one max-pooling layer and two FC layers. The layer Conv1 has four filters, each of which has one 5 × 5 kernel. The sliding stride of Conv1 is 2. Thus, the data after Conv1 become 8 × 8 with a depth of 4. Then, the layer Conv2 has eight filters, each of which has four 5 × 5 kernels corresponding to the four channels of streaming data. The sliding stride here is 1, so the data after Conv2 become 4 × 4 with a depth of 8. A ReLU (rectified linear unit) activation function is used after each convolutional layer. Next, these data are compressed to 2 × 2 with eight channels using a max-pooling layer, flattened and expanded as a vector of size 32 and imported to FC layers with a size of 32 × 5 and a softmax function to obtain the final five output probabilities. Finally, the classification result is given by the maximum of these five outputs. The input data are randomly chosen from five letters (a, e, r, p, s) in the EMNIST dataset, with 50 images for each class. To adapt to the compact scale of the array, these 250 images are first binarized and compressed from 28 × 28 to 20 × 20 before being imported into the MSNet. The test set has a total of 500 images and each class has 100 images.

The MSNet training was implemented by directly hardcoding the necessary parameters into the hardware array (Fig. 4). The array-level data flow during MSNet training is shown in Extended Data Fig. 7a. The process begins with six software–hardware hybrid functions that transform the original image data into a format that is compatible with our hardware architecture, strictly following the principles of matrix multiplication and convolution.

We facilitate a smooth transition from the input data and weights to the voltage sequences and conductance levels of the cells by using quantization and physical mapping techniques, ensuring that they fall within suitable ranges for both software and hardware processing.

We note that the weight updates through the VAU method, pruning weights, along with the matrix multiplications that constitute the inference process (MAC), were performed directly on the hardware (on chip), leveraging Kirchhoff’s laws. In contrast, nonlinear activation functions, max-pooling operations, gradient calculation and sorting, sparsity generations and regrowth are incompatible with matrix multiplication, hence they were carried out in software (off chip).

The step-by-step experimental procedure for VAU and inference is detailed in Extended Data Fig. 7b. For each layer and every epoch, we initiate a VAU and write–verify process to ensure that each conductance value is within an acceptable range, closely aligned with the target weight at the outset. Figure 4b shows examples of the sparsity and weight maps captured on the hardware during pivotal epochs.

Upon completion of the weight update loop, voltage sequences are fed into the array, marking the beginning of the inference phase. We have extracted 4,000 data points from the synchronous output current sequence waveforms across all channels and layers for epoch 57 (Extended Data Fig. 7b). Extended Data Fig. 7c shows the aggregate current outputs and demonstrates the efficacy of the hardware-executed inference, as evidenced by the clear correlation between the two sets of outputs.

# Pruning and regrowth algorithm

The pruning algorithm defines the criteria of pruning, that is, it defines which weights are unimportant and should be pruned. First, the pruning ratio was determined and optimized considering the network size and the application. Then, the weights of each layer were sorted on the basis of their magnitudes. Weights with smaller magnitudes have less impact on computation results and are considered less important. According to the pruning ratio, a certain number of the least important weights were pruned by resetting their magnitudes to zero so that they no longer participated in the network training.

During the process of network training, the significance of synapses evolves dynamically. A synapse (weight) that was considered unimportant previously might later gain importance, suggesting that the earlier pruning strategy may no longer be appropriate. Therefore, adjusting the distribution of pruned weights is necessary to achieve better performance. Weight regrowth is introduced to make some pruned synapses (weights) active and engage again during training.

Our decision algorithm determines which synapses should be selectively regrown. First, weight gradients of each epoch were recorded to calculate momentum as follows:

where grad represents computed gradients during backpropagation. t and t − 1 are the current and previous training epochs respectively. The momentum serves as the criterion and pruned synapses are sorted on the basis of their momentum. Considering that weights with the largest momentum may not always be the most important, the range of weight regrowth needs to expand. Hence, we defined an expansion factor to obtain a candidate list (equations (2)–(4)). The final synapses to be regrown are randomly chosen from this list.

where sort() represents the descending order sorting operation and total num is the number of synapses in the network. Consequently, those weights would regrow from zero and participate in the training and inference again.

# Scheduling of sparse training

We built an integer-weight training algorithm on the basis of previous works47,48, and adapted it to support pruning and regrowth methods. The scheduling includes four durations: pretraining, pruning, overpruned and regrowth. Before the on-chip training, we pretrained the MSNet off chip for ten epochs using eight-bit weights. This method is always used for low-precision network training. During pretraining, L regularization was applied, which added a regularization term in the loss function to push the weights closer to zero while training. In this way, more weights were concentrated around the zero, obtaining a greater sparsity. Then, the MSNet was deployed into the fabricated index-free array.

In the hardware demonstration, every weight in the array was quantized49 from eight bit to five bit (32 levels), composed of a differential pair of four-bit (16 levels) unit cells. A full-batch training strategy with the Adam optimizer was adopted to reduce the number of updates. We note that the core components of MSNet, two convolution layers, and the FC layer were run on the index-free array, while other associated functions (such as max pooling, ReLU and softmax) were completed in software.

During the pruning operation, we adopt the pruning and finetuning phases iteratively to gradually compress the model (Fig. 3c). To ensure the stability of training, the pruning rate decreased exponentially from the start. Generally, the shallower layers in NNs are more crucial because they extract the initial features. Hence, while pruning the Conv1 layer, a lower pruning rate was applied, while the Conv2 layer had a higher pruning rate. In detail, we prune and fine-tune four times, and the ultimate pruning rates for the Conv1, Conv2 and FC layers are 52%, 80% and 59%, respectively, with an overall pruning rate of 74.2%.

During the overpruned operation, an additional 12.7% of weights, including important ones, were pruned with the same pruning method. As a result, the network would experience a decrease in accuracy. The loss of accuracy cannot be recovered by fine-tuning, indicating that the former pruning duration succeeded and reached the limit of sparsity. Finally, in the regrowth duration, 12.5% of weights were regrown. Due to the inherent randomness of the regrowth algorithm, the distribution of newly regrown weights tends to vary from their previously overpruned counterparts. However, the accuracy always was seen to increase, suggesting slight pruning mistakes during the main pruning duration.

# The VAU

The VAU reforms the update principles to optimize the sparse training of the index-free hardware. Cell-by-cell update of weight is precise but requires a time and energy overhead. The vectorial methods are developed from the Manhattan rule50 and update weights by rows (columns), where the operations for one row (column) are identical. However, these methods suffer from either degradation of precision or too long training iterations. In an SPNN, the majority of weights are pruned and any training operations on them are physically screened by sparsity transistors. The SPNN can be fast and efficient, and can have nearly precise vectorial updating.

The mathematical principle of VAU is shown in Fig. 3d,e. For a weight map with M rows and N columns, a known weight-to-tune (ΔW) map was calculated from the backpropagation algorithm and contains M × N operators. Using vectorial update, this map could be achieved using M row-wise operators and N column-wise operators. These operators (OP) are the solution of the equation

where A is known as an auxiliary matrix to establish the equations. This matrix remains constant throughout the entire calculation process, and its dimensions are solely determined by the size of the

gradient matrix. Consequently, the primary role of matrix A is to facilitate the transformation of M + N operations into M × N incremental weight adjustments. Importantly, matrix A does not exert any influence on the performance of the VAU algorithm. This clarification emphasizes that, while matrix A is instrumental in the computational process, its impact on the efficiency or speed of the VAU algorithm is negligible.

With the least-squares method, the best solution could be found and we could carry out an approximate ΔW′ map.

where λ is the perturbation factor and I is the perturbation matrix, which are added to make matrix AT A reversible. After evaluating the mean square error of ΔW and ΔW′, the final solution of vectorial operators was confirmed. According to the hardware specifications, these vectorial operators were transferred to a specific number of voltage pulses with identical amplitudes and periods.

The operation of VAU on an M × N array has two steps (Extended Data Fig. 5a). The first step is training by columns with N column vectors. Each column vector contains M sets of identical operation pulses, which are imported from M bit lines in parallel. During training, the selected data output line and all M data input lines were grounded while unselected data output lines were compensated with a specific DC voltage to avoid crosstalk. This step needs N compute cycles. The second step is all-parallel training with row vectors. Because the unit cells on one row share a one-bit line and one set of pulses, only one compute cycle is needed. During training, all data input lines and data output lines were grounded. Of note, benefiting from index-free hardware, the sparsity information has been programmed into every unit cell, hence the sparsity line is floating in the whole process of training and no one position is indexed.

We evaluated the precision of VAU by calculating the mean square error of ΔW and ΔW′. The error introduced by VAU was smaller than one state of weight with sparsity over 50% (Extended Data Fig. 5b). For a typical sparsity (always up to 90% for commercial models), this error decreased to a negligible value.

We performed training simulation with VAU, a precise update as a baseline and scenarios including hardware non-idealities (such as parasitic effects and variation) (Extended Data Fig. 5c). The impact of all hardware non-idealities is reflected in the computational outcomes through the noise present in the input and output signals. Write noise arises from the fluctuations that occur during the weight updating process (training phase), which inherently includes contributions from parasitic effects. We utilized a premeasured variation of 0.04 μS per state (0.4 μS in total), equating to a 10% write noise level. Read noise is derived from the inconsistencies that occur during the matrix–vector multiplication process (inference phase). In this case, we employed a premeasured variation of 0.017 μS per state, which corresponds to a 4.25% read noise level. The result indicates that the training accuracy of VAU is at the same level as the precise baseline but is more adaptive for the SPNN.

# Plotting loss landscape

The visualization method in a previous work51 was used to calculate and draw the loss landscape of all epochs. The weight number of the MSNet is 1,060, so the weight vector (or parameter vector) is 1,060 dimensional. First, the calculated weight map at the end of one epoch is chosen as the centre point θ* in the loss graph. Then we initialized two 1,060-dimensional direction vectors, δ and η, which are always randomly generated and orthogonal. Therefore, the 2D plot of the loss landscape could be written as

where α and β are two scalar parameters to define the weight surface θ* + αδ + βη. As a result, we could visualize the loss landscape of one specific epoch or all epochs according to the related weight maps (Supplementary Video 2).

# Implementation of a pruning-capable IMC architecture

We performed a simulation of a pruning-capable IMC accelerator based on DNN+NeuroSim v.2.1 (ref. 46), a benchmarking framework for on-chip training that provides an evaluation of both model and chip performance. The IMC accelerator in NeuroSim is structured with four hierarchies: chip level, tile level, PE level and synaptic array level. Each layer in a DNN is mapped to at least one tile and further partitioned into PEs and synaptic arrays. For on-chip training applications, the training schedule consists of feedforward, error propagation, weight gradient computation and weight update. Except for weight gradient computation, which is executed in a specific static random-access memory (SRAM)-based weight gradient unit to avoid the notable overhead of rewriting memory, the other three training steps are performed in the same transposable IMC arrays.

The original IMC accelerator lacks support for SPNN implementation, so we optimized the data flow by taking into account the reduction in data transfer and array operation during the training process of an SPNN. For pruning index storage, we integrated hierarchical index buffers into the chip architecture.

During feedforward, structured vector-wise and block-wise pruning reduce energy and latency by deactivating ADCs or entire synaptic arrays when the corresponding weight vectors or blocks are pruned. Additionally, VMM results of these pruned weights circumvent the need to transfer back to off-chip dynamic random-access memory (DRAM), which mitigates data transfer overhead. To locate the pruned synaptic vectors or arrays, PE index buffers are introduced to store indices for the pruning groups within a PE. The buffer capacity depends on the predefined array size and the number of arrays in a PE. Element-wise pruning does not affect the data flow of the highly parallel feedforward process, so no index buffer is introduced at the PE level for this granularity.

For error propagation, the computational pattern is similar to that of the feedforward process, but VMM is executed in a transposed manner on the synaptic array. This is realized by implementing transposable synaptic arrays, allowing input vectors along both rows (for feedforward) and columns (for error propagation). Therefore, for vector-wise pruning, a pruned weight column no longer facilitates deactivating ADCs at the end of each column but conserves data entries of input vectors for it. Other chip modifications remain consistent with the feedforward process for all pruning granularities.

Weight gradient computation of layer i is a process of convolving the errors from layer i with the activations from layer i − 1 in a channel-to-channel scheme. As weight sparsity does not generate predictable sparsity in error or activation map, it merely affects the weight gradient computation process by saving data transfer of the pruned weight gradients. To achieve this, an index buffer is incorporated beside the weight gradient unit at the chip level, with a capacity equivalent to the number of pruning groups within the present layer.

During weight update, weight sparsity directly diminishes delta weight (ΔW) transfer and array operations. Hence, pruning indices are fetched alongside ΔW and loaded into a specific index buffer at the tile level. The capacity of this buffer is defined as the number of pruning groups within one PE (rather than the entire tile), to limit the buffer overhead for indexing.

# Benchmarking

The benchmark of the weight update process is divided into three sections: delta weight transfer, pruning index transfer and array operation. We assume that the delta weight has been computed on chip,

whereas the pruning index needs to be loaded from off-chip dynamic random-access memory into the index buffer of each tile. Array operation refers to the selection and updating of the FeFET cells, as well as the operation of the peripheral word-line/bit-line/source-line switch matrices. To benchmark our proposed index-free method, we adapt the IMC chip architecture to employ the two-ferroelectric-device structure and VAU scheme. The CMOS selector in a one-transistor– one-FeFET array is substituted by a ferroelectric transistor, inherently storing the pruning index in a two-FeFET array. As a result, index access during weight updates is no longer necessary. Given this, index buffers (such as those in the above conventional weight update scheme) are no longer needed in the proposed method, saving both energy and latency for index access.

# Training process for scalability evaluation

To validate the scalability of the purposed methods, we employed a VGG8-Net with six convolutional layers and two FC layers by simulation on DNN+NeuroSim (ref. 46). The model was tested on the CIFAR-10 dataset, which consists of colour images in ten classes, with 5,000 training images and 1,000 test images per class. We utilized the mini-batch gradient descent algorithm for training, with consideration of device non-ideality and quantization. The device nonlinearities are derived from measurements (‘Simulation with non-idealities’). In terms of quantization, we set the bit width of weights and gradients to eight bits, and ADC precision to five bits, which is adequate for achieving an accuracy exceeding 90% on a dense network. The size of one FeFET synaptic array is 64 × 64.

In all test scenes, regardless of the pruning method used, the network is trained for 45 epochs. The learning rate is tuned for convergence at the 35th and 40th epochs. For both structured and unstructured pruning, an overall pruning rate of 88.5% is reached after a three-step pruning process, with a descending proportion of weight pruned in each step. The layer-wise pruning rate is carefully adjusted to ensure that it can be precisely achieved by the coarse-grained granularities. We also employ a threshold of the current pruning rate to decide when to apply VAU on each layer, which avoids imprecise VAU operations on an insufficiently sparse NN.

# Simulation with non-idealities

In accordance with the article on DNN+NeuroSim v.2.1, we have introduced nonlinearity and variations into the device model. The parameters include potential/depression nonlinearity, cycle-to-cycle variation (c2cVari), and device-to-device variation (d2dVari). Below are the definitions and simulated values for each parameter.

Nonlinearity. In NeuroSim, the potential/depression curve of the FeFET device is modelled by the following expressions:

where $G _ { \mathrm { m i n } }$ and $G _ { \mathrm { m a x } }$ denote minimum and maximum conductance, respectively, and P is the number of pulses. Parameter B controls nonlinearity of the curve, and parameter D normalizes the conductance within $[ G _ { \mathrm { m i n } } , G _ { \mathrm { m a x } } ] .$ . For intuitiveness, parameter B is converted to $\alpha _ { \mathrm { P } }$ and $\alpha _ { \mathrm { D } }$ for potential/depression nonlinearity, where a higher absolute value indicates higher nonlinearity. On the basis of actual measurements, $\alpha _ { \mathrm { p } } { = } 0 . 5 2 3$ and $\alpha _ { \mathrm { { D } } } = - 0 . 1 4 5$ are used in the simulation.

Cycle-to-cycle variation (c2cVari). Cycle-to-cycle variation is described as the variation of delta weight (ΔW) during each update. A Gaussian noise with an s.d. of c2cVari is applied to each weight during network parameter updates, simulating random cycle-to-cycle variation. The distribution of measured c2cVari is shown in Extended Data Fig. 10b, and $\mathsf { c } 2 \mathsf { c V a r i } = 0 . 5 \times 1 0 ^ { - 3 } ( \mathsf { s } . \mathsf { d } . )$ ) is adopted as the simulated c2cVari value.

Device-to-device variation (d2dVari). Similar to c2cVari, d2dVari is defined as the s.d. of the nonlinearity parameter $( \alpha _ { \mathrm { p } } / \alpha _ { \mathrm { D } } )$ of each FeFET cell, directly reflecting the shape of each cell’s potential/depression curve. d2dVari is calculated by statistically measuring the conductance curve of 29 FeFETs and determining the s.d. of the nonlinearity parameter α. In accordance with Extended Data Fig. 10c, d2dVari = 0.24 is used in the NeuroSim simulation.

Simulation results with non-ideal properties. We simulated the network accuracy and latency/energy of the hardware system using NeuroSim, taking into account the non-ideal properties described above. The configuration of the VGG-8 Net is identical except for the inclusion of non-ideal parameters. With non-idealities applied, an overall decline of approximately 0.7% in accuracy is observed (Extended Data Fig. 10e). Hardware performance in latency and energy for the weight update stage was also simulated under the same configurations as before, incorporating non-ideal parameters to reflect actual devices (Extended Data Fig. 10d). There are subtle differences between ideal and non-ideal results since each individual value of weight and ΔW changes with non-ideal properties, but the disparity between ideal and non-ideal cases is negligible. This is expected, as nonlinearity and variation introduce noise into network training without obviously affecting the overall (average) value of network parameters (weights and ΔW). Incorporating non-idealities into the NeuroSim simulation only modestly impacts the absolute accuracy and hardware performance metrics, and the core conclusion remains unchanged.

# Design of differential pairs for NeuroSim platform

We have implemented a differential pair functionality within the NeuroSim simulations to align with the experimental FeFET array. To ensure a realistic and accurate representation, we applied the same non-ideal properties to the simulation of the differential pair (Extended Data Fig. 10a–c). Incorporating a differential pair effectively doubles the scale of the weight arrays, necessitating twice as many devices to map the network. This adjustment ensures that our simulation reflects the hardware’s capacity to handle both positive and negative weights. Since the on/off state of each differential pair is not stored on chip, we have added additional buffers for differential index storage. Before updating, indices are read into the on-chip buffers to control which cell in the differential pair should be updated. This introduces an index overhead for both sparse and dense NNs; however, it does not affect the operation of our index-free method.

The simulation results indicate that the use of differential pairs does not affect the cell-by-cell update method for both sparse and dense NNs, as each weight cell is individually updated. In contrast, our VAU method benefits from higher sparsity in the weight array, which improves the precision of least-square fitting and, consequently, network training accuracy. With differential pairs, the actual sparsity in a device array increases, as half of the total devices are always shut down. For instance, with a 60% sparsity rate, the effective sparsity of an array becomes 80%, enhancing the accuracy of VAU with differential weight pairs. Extended Data Fig. 10f shows the accuracy with and without differential pairs. While there are fluctuations in the element-wise and no-pruning methods, the accuracy of the VAU method (index free) improves by 0.46% with the introduction of differential pairs.

# Data availability

Source data are available at https://doi.org/10.6084/m9.figshare. 27284259.v1 (ref. 52).

# Code availability

The codes used for sparse training, scheduling and simulations are available from the corresponding authors upon reasonable request.

# References

# Acknowledgements

This work was supported by the National Key R&D Program of China (grant numbers 2022YFB4400100 (X.W.), 2023YFF1500500 (X.W.), 2021YFA1202904 (L.G.), 2022YFA1402500 (W.L.), 2021YFA0715600 (W.L.), 2023YFB2806802 (Y.F.), 2021YFB3600104 (Y.F.)), the Leading-edge Technology Program of Jiangsu Natural Science Foundation (grant numbers BK20232024 (X.W.), BK20232001 (Y.S.)), the National Natural Science Foundation of China (grant numbers T2221003 (X.W.), 61927808 (X.W.), T2322014 (Y.Z.), 62204124 (Y.Z.), 62322408 (T.L.), 62204113 (T.L.), 62104098 (Y.F.), U21B2032 (L.L), 62304101 (W.L.)), Jiangsu Funding Program for Excellent Postdoctoral Talent (grant number 20220ZB63 (W.L.)), the Natural Science Foundation of Jiangsu Province (grant number BK20220773 (T.L.), BK20230776 (W.L.), BK20210178 (Y.F.)), the Jiangsu Province Key R&D Program (BE2023009-3 (W.L.)), the Key Laboratory of Advanced Photonic and Electronic Materials, Collaborative Innovation Center of Solid-State Lighting and Energy-Saving Electronics, and the Fundamental Research Funds for the Central Universities, China. We express our gratitude to the Interdisciplinary Research Center for Future Intelligent Chips (Chip-X) and Yachen Foundation for their invaluable support. X.W. acknowledges the support by the New Cornerstone Science Foundation through the XPLORER PRIZE.

# Author contributions

Z.Y. and X.W. supervised the project. H.N., Z.Y. and X.W. conceived the idea and designed the experiments. H.W. fabricated the array with assistance from H.N., Z.Y., W.L., X.L. and L.G. H.N. designed the software and hardware measurement system. H.W. performed the array measurement with assistance from H.N. and X.L. Y.M., Y.F., Y.S., Q.Z. and L. Li carried out the training algorithm, simulation and benchmarks. X.Z., L. Liu, S.Z. and T.L. synthesized the CVD MoS . H.N., Z.Y. and X.W. co-wrote the manuscript with input from all authors. All authors contributed to the interpretation of data and discussion.

# Competing interests

The authors declare no competing interests.

# Additional information

Extended data is available for this paper at https://doi.org/10.1038/s41928-024-01328-4.

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41928-024-01328-4.

Correspondence and requests for materials should be addressed to Zhihao Yu, Yuxiang Fu or Xinran Wang.

Peer review information Nature Electronics thanks Hongsik Jeong and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permissions information is available at

www.nature.com/reprints.

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

© The Author(s), under exclusive licence to Springer Nature Limited 2025

1 National Laboratory of Solid State Microstructures, School of Electronic Science and Engineering and Collaborative Innovation Center of Advanced Microstructures, Nanjing University, Nanjing, China. 2 School of Integrated Circuit Science and Engineering, Nanjing University of Posts and Telecommunications, Nanjing, China. 3 Suzhou Laboratory, Suzhou, China. 4 School of Integrated Circuits, Nanjing University, Suzhou, China. 5 Interdisciplinary Research Center for Future Intelligent Chips (Chip-X), Nanjing University, Suzhou, China. 6 State Key Laboratory for Organic Electronics and Information Displays, School of Materials Science and Engineering, Institute of Advanced Materials, Nanjing University of Posts and Telecommunications, Nanjing, China. 7 These authors contributed equally: Hongkai Ning, Hengdi Wen, Yuan Meng.  e-mail: zhihao@njupt.edu.cn; yuxiangfu@nju.edu.cn; xrwang@nju.edu.cn

Extended Data Fig. 2 | Design and statistics of weight device and sparsity device. a-b, The 3D schematic of the structure of weight device (a) and sparsity device (b). c-f, Distribution and spatial heatmap of memory window (c, d) and Ion/Ioff ratio (e, f) for all 450 weight devices in the index-free IMC array. The red lines are fitted curves by the normal distribution. g, Statistics of 16-state characteristics from 100 weight devices. On each box, the central mark indicates

the median of conductance of these 100 devices on a certain weight, and the bottom and top edges of the box indicate the 25th and 75th percentiles, respectively. The whiskers extend to the most extreme data points not considered outliers. h, Collected 8-state retention curves in 100 s from 50 weight devices (The shadow are dense lines of raw data rather than any error bands).

d-f, 128 states with sparsity- FeFETs on or off under 25 °C (d), 85 °C (e) and 125 °C (f). g-i, output curves of potentiation process with sparsity- FeFETs on under 25 °C (g), 85 °C (h) and 125 °C (i).

a

# Vectorial Approximate Update (VAU)

Pruning

Pruning cycles

Updating

Updating cycles

Regrowth

Regrowth cycles

Sparse NN

curves of training process for five cases: No pruning, Block-wise, Vector-wise, Element-wise, and Index-free. e, Size, mapping and sparsity parameters of sparsified VGG-8 Net. Panel a adapted with permission from ref. 46, IEEE.

Extended Data Fig. 10 | See next page for caption.

Extended Data Fig. 10 | Simulation with non-idealities and differential pairs. a-c, Extraction of non-idealities for NeuroSim simulations including a typical multistate curve providing the nonlinearity (a), device to device variation of nonlinearity (b) and cycle to cycle variation of delta weight during updating (c). d, Training process with non-idealities for three cases: No pruning, Elementwise, and Index-free. e, Accuracy, latency and energy enhancement of index-free

hardware w/o and w/ non-idealities, compared with traditional SPNN. f, The mapping schematics of weight map and sparsity map, and the structure inside the unit cell when deploying differential pairs. g, Sparse training of VGG-8 Net based on single device w/o noise, w/ noise, and differential pair w/ noise. h, Accuracy, latency and energy enhancement of index-free hardware w/o and w/ differential pairs, compared with traditional SPNN.
