---
title: "Few-Shot Graph Learning with Robust and Energy-Efficient Memory-Augmented GNN"
authors:
  - "Chen Sun"
  - "Zhiran Wang"
  - "Dashan Shang"
date: "2022-01-01"
year: "2022"
journal: "IEEE J-EDS"
abstract: "Learning graph structured data from limited examples on-the-fly is a key challenge to smart edge devices. Here, we present the first chip-level demonstration of few-shot graph learning which homogeneously implements both the controller and associative memory of a memory-augmented graph neural network using a 1T1R resistive random-access memory ([[RRAM]]). Leveraging the [[in-memory computing]] paradigm, we validated the high end-to-end accuracy of 78% (GPU baseline 80%) and robustness on node classification of CORA dataset, while achieved 70-fold reduction in latency and 60-fold reduction in energy consumption compared with conventional digital systems."
keywords:
  - "[[Graph neural network]]"
  - "[[Few-shot learning]]"
  - "[[Memory-augmented]]"
  - "[[RRAM]]"
abstract_cn: "从有限样本中动态学习图结构数据是智能边缘设备面临的关键挑战。本文首次展示了少样本图学习的芯片级演示，使用1T1R阻变随机存取存储器（RRAM）同构实现记忆增强图神经网络的控制器和关联存储器。利用存内计算范式，我们在CORA数据集的节点分类上验证了78%的端到端高精度（GPU基线80%）和鲁棒性，同时与传统数字系统相比实现了70倍延迟降低和60倍能耗降低。"
cite: "[1] Sun et al. Few-Shot Graph Learning with Robust and Energy-Efficient Memory-Augmented GNN[J]. IEEE J-EDS, 2022."
aiSum: "少样本图学习 MAGNN：256 Kb 1T1R RRAM、CORA 78% 准确率、70 倍延迟降低、60 倍能耗降低、中科院+香港大学。"
confidence: "medium"
wiki_concepts:
  - "[[RRAM]]"
---

Abstract-Learning graph structured data from limited examples on-the-fly is a key challenge to smart edge devices. Here, we present the first chip-level demonstration of few-shot graph learning which homogeneously implements both the controller and associative memory of a memory-augmented graph neural network using a 1T1R resistive random-access memory ([[RRAM]]). Leveraging the [[in-memory computing]] paradigm, we validated the high end-to-end accuracy of 78% (GPU baseline 80%) and robustness on node classification of CORA dataset, while achieved 70-fold reduction in latency and 60-fold reduction in energy consumption compared with conventional digital systems.

# I. Introduction

Few-shot graph learning has received increasing attention in applications such as recommending systems of social networks, thanks to its capability to adapt to unseen data (Fig. 1). One promising approach for few-shot graph learning is memory augmented neural network (MANN) [1], where features are first extracted from a neural network followed by being stored and retrieved from an explicit associative memory (AM). Implementation of MANN with conventional digital hardware suffers from frequent and massive data shuttling between computing unit (CPU or GPU) and AM (e.g., DRAM) to calculate similarities or distance norms [2], incurring large energy dissipation and time latency. To avoid the tedious data transfer, non-volatile memory (NVM) technologies such as RRAM and [[FeFET]] have been exploited to implement various AMs with in-memory computing capability [2-7]. However, it remains elusive to apply in-memory few-shot learning to graph structured data, which encode the inherent dependency between nodes and make the meta-training more complicated and expensive. To address the aforementioned issue, in this work, we present a robust and energy-efficient few-shot graph learning framework, called memory augmented graph neural network (MAGNN), and implement it on a monolithically integrated 256 Kb 1T1R RRAM chip.

# II. MAGNN based on homogeneous RRAM chip

The proposed MAGNN consists of three essential components, an echo state graph neural network (ESGNN) controller, a binary neural network (BNN) encoder, and an AM, all implemented on the same 256 Kb TaOx RRAM chip fabricated using 40 nm standard CMOS technology (Fig. 2). The ESGNN is used for graph feature extraction [8]. The BNN is optimized by meta-training to map feature vectors to bipolar signatures (-1/+1) which, together with the corresponding labels, are stored in the AM. As a result, one can search in parallel for the supporting class that is closest to a given query. The hardware ESGNN, BNN, and AM seamlessly interface each other through a printed circuit board with analogue-digital conversion circuitry and a ZYNQ SoC (Fig. 3a). The distribution of the high and low resistance states of the RRAM with mean μ and standard deviation σ and the switching endurance are shown in Fig. 3b and ${ 3 \mathrm { c } } ,$ respectively. The experimental set and read speeds of RRAMs are 50 ns and 10 ns, respectively, as shown in Fig. 3d and 3e.

# III. Few-Shot learning and inference experiments

We demonstrate few-shot graph learning and inference on the widely used CORA dataset [9], consisting of 2708 nodes. Each node represents a scientific publication and belongs to one of the seven research disciplines. First, an RRAM sub-

array (156 Kb), termed fixed RRAM array, underwent SET processes to generate a random resistance matrix thanks to the stochastic ion motions. The obtained fixed RRAM array is divided into two sub-arrays to represent two weight matrices, the input matrix $W _ { \mathrm { i n } }$ and the recursive matrix $W _ { \mathrm { h } , }$ of the ESGNN (Fig.4a). Fig. 4b depicts the node embedding procedure [8]. The internal state of each node at the next time step is co-determined by the sum of neighboring contributions and input projection. Fig. 4c shows the evolution of measured node embeddings along iterations.

Next, the other part of the RRAM array, called programmable resistor array, was divided into two sub-arrays (40 Kb and 1 Kb) to represent the weight matrices $( W _ { \mathrm { o u t } } )$ of the BNN and AM, respectively. The 200 dimensional real-valued graph feature vectors extracted by ESGNN are quantized into 100-bit bipolar vectors (+1/-1) by the BNN, before being stored into the AM. During meta-training, new feature vectors from support set are embedded into AM through bit line (BL) (Fig. 5a). During inference, the comparison of the query vector with each of the support vectors stored in AM is performed by inmemory dot-products. Fig. 5b shows the measured conductance of the programmable RRAM array for AM that contains six 100-bit feature vectors after 2-way 3-shot learning. The similarities between inference samples are calculated according to the measured summation currents (Fig. 6). For meta-training, the weights in BNN can be updated by calculating the loss between the prediction and true label (Fig. $^ { 7 ) , }$ making the feature vectors associated with the same class of similar bipolar signatures. With increasing meta-training episodes, the loss (accuracy) gradually reduced (increased) (Fig. 8). The ESGNN effectively minimized the meta-training cost due to its fixed weights (Fig. 9). The node classification accuracies of RRAM-based MAGNN were in par with those obtained from software (Fig. 10). We also performed simulations for 3-way 3-shot learning using AMs of varying size, achieving software-equivalent accuracy and immunity to RRAM variations as the AM size increased (Fig. 11). End-toend benchmark against GPU backed by DRAM revealed that the RRAM-based MAGNN featured 70-fold search latency, 250-fold update latency, and 60-fold inference energy consumption improvements (Fig. 12).

# IV. Conclusion

We present the chip-level demonstration of few-shot graph learning using a monolithic 256 Kb 1T1R RRAM chip, where the same hardware can implement both the controller and AM. Excellent node classification accuracy of 78% (2-way 3-shot) and robustness on the CORA dataset were demonstrated. This work provides a promising solution to the future energyefficient autonomous systems at the edge.

Acknowledgements: This work was supported by the National Key R&D Program of China (Grant Nos. 2018YFA0701500), the NSFC (Grant No. 61874138, 62122004, 61888102, 61834009, 62025406), the Strategic Priority Research Program of the CAS (Grant No. XDB44000000), and the HK RGC-ECS (Grant No. 27206321).

References: [1] A. Santoro, et al., Pro. Machine Learning Res. 48, 1842, 2016; [2] K. Ni. et al., Nat. Electronics 2, 521, 2019; [3] C. C. Lin, et al., ISSCC 2016; [4] H. Li, VLSI 2021; [5] S. Dutta, et al., IEDM 2021; [6] Y. Li, et al., IEDM 2021; [7] C. Sun, et al., VLSI 2021; [8] S. C. Wang, et al., arXiv: 2112.15270; [9] P. Sen, et al., AI Mag. 29, 93, 2008.

![](images/18ea7f39c59c42b6a49016963b31cb576d09c29429b5b45a451ad863ee0f388e.jpg)

![](images/2b2d3d50a7f69daef88b65a674acbe145e9691d63c12d35e9bb1799c0b0f7ff6.jpg)  
Fig. 1 Graph structured data encode inherent dependency between nodes, posing a significant challenge to the conventional memory-augmented neural networks (MANNs) when unseen classes are encountered.

![](images/facb6114cd17db3510f45188b5a80cfb282bd4bc5f06cb807f2209c51eeb3bb6.jpg)

![](images/a3d47cd9b8b023db61efa2928cb0c7485854b252ba0e00e5c171840f194b445a.jpg)  
Fig. 2 The memory-augmented graph neural network (MAGNN) is composed of a controller, an encoder and an associative memory (AM). The graph features are extracted by echo state graph neural network (ESGNN), and then converted to bipolar vectors by binary neural network (BNN) and stored/searched in AM. The MAGNN is implemented homogeneously on a single RRAM chip.

# III. RRAM-Based Hardware System and RRAM Device Performance

![](images/0765d605bb49f6ef900ba9210cab8caeacec3ed94b7265b046b0af223d1406f9.jpg)  
Fig. 3 (a) RRAM-based in-memory computing hardware. The 256 Kb RRAM array was fabricated by 40 nm standard CMOS technology. (b) and (c) show the conductance distributions and switching endurance, respectively. (d) and (e) show the 50 ns programming speed and 10 ns read, respectively.

# IV. Graph Feature Extraction and Storage

![](images/480874fd904ed5e4169cdef9c8e5d0b5176754e9ec3d77db8e4c172a8747d9ee.jpg)

![](images/118b7178c06ca4a1446a1ba397813875cef7ee7bba59495e6325b1c59049988e.jpg)

![](images/a3034c7441c65af0c0f5abb2f069a782a0bcdf5a5bc1665d2984af58e6c59a22.jpg)

![](images/d15556baaff66cbf8817bd8b6aea03dc0521bba00f4706a115f63236e80e6552.jpg)  
Fig. 5 (a) Schematic of dot-product operations in AM (i.e., programmable RRAM Fig. 4 (a) The measured conductance of the fixed RRAM array, which is partitioned into two sub-arrays to represent the input weight matrix $( W _ { \mathrm { i n } } )$ array). The signed weights are realized using differential pairs (e.g., green box), proportional to conductance differences between adjacent RRAM cells. The support and hidden weight matrix (Wh) of the ESGNN. (b) Graph node embedding vectors are stored in the AM along the BL. Dot product is performed by applying procedure. The node state at the next iteration step is co-determined by the voltages (input query vectors) to the RRAM (stored vectors). (b) The measured AM neighboring contributions and input projection. (c) The evolution of graph conductance representing six 100-bit feature vectors after 2-way 3-shot learning.embedding vectors (50 of 200 dimensions are shown) along iteration steps.

# V. Experimental Deomonstration of Few-Shot Learning and Inference

![](images/2bd14f6bafbafc3a7a69b9db744b5f1af4e212cf206a4b3460eea5810aebce6c.jpg)

![](images/a54b0dcec08dc4e15d21be47cf32698b9e43b69cb8ef9016136a580b2dedae52.jpg)

![](images/d5648487c382084bc31b50228eaff332ff82785c9e8bcd6c0e0533af9c16f701.jpg)

![](images/0a5cb9d96c61c00662bfebb72bf7d43f8af215e5d0c0c27c754532859b1e1c2f.jpg)

![](images/e57e99ce01526b3227ab6d7eb0331fed6983a444d3773f158eed61c9f1dab6ae.jpg)  
Fig. 6 The calculated similarities between  Fig. 7 BNN weight distribution query vectors and stored support vectors in a  (200´100) before (top) and 2-way 3-shot task. The class prediction of the  after (middle) meta-training, queries according to maximum similarities and the corresponding weight consistent with the labels. changes (bottom).

![](images/fd1536f3a7b67cc9a721e75f01c71d6800cfd4db3c946659f932be1e32a33203.jpg)

![](images/d44f0316d8a7537ce3b265dd1a9adeddfae804ad4a00543a693e2a32381b5e01.jpg)  
Fig. 8 The loss and accuracy along meta-training.   
Fig. 9 Meta-training energy of an episode, showing 40- fold reduction compared to graph convolutional network (GCN) with GPU.

![](images/f1b53b34b646f406466009194b4b437b677cc9e6374d9f829ae1b51a1db9d617.jpg)  
Fig. 10 The measured (RRAM) and simulated (GPU) classification accuracy for different few-shot learning tasks.

# VI. Influence of AM Size on Accuracy

![](images/a5cfcba8c33b71b08d6dd6329b62b976019413cb1ef15a778e3cb4e028d76acd.jpg)

![](images/747829b923289b62bf95392936868b07b20847fd7f7ab8ce20b99dbee1f6eabe.jpg)  
Fig. 11 (a) Classification accuracies with increasing AM size (i.e., feature vector dimension) and (b) accuracies with increasing RRAM variations () in encoder and AM for 3-way 3-shot meta-learning task.

# VII. Benchmarking of Energy and Latency

![](images/d13ae8cb1057d149d34096396c4dccafc719c550d597f7e1283f7068f4ae794c.jpg)

![](images/3c79cc31cd9524240f2cf9c2d244ee6b19ac1d562beaa65454d7f53e761c7e25.jpg)

![](images/1995c43cb80fa7139183cee907052eaf4e841732baac4e52cae85605c5a32c79.jpg)

![](images/8848a0ab00cabf4cfd6cf78fb20dec8afbf9e1f9077819eb481bc6139ab9cd82.jpg)  
Fig. 12 The RRAM-based AM shows (a) 70-fold reduction in search latency, (b) 250-fold reduction in update latency compared to that on a GPU backed by conventional DRAM. (c) The RRAMbased MAGNN shows a 60-fold reduction of end-to-end inference energy consumption compared to that on a GPU backed by conventional DRAM. (d) The inference energy decomposition of (c).