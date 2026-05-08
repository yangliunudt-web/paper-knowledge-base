---
title: "Supplementary Materials for Edge Learning Using Neuro-Inspired Memristor Chip"
authors:
  - "Corresponding Bin"
  - "Huaqiang"
date: "2023-09-15"
year: 2023
journal: "Science"
doi: "10.1126/science.ade3483"
abstract: "[Summarized] Abstract not available for supplementary material."
abstract_cn: "使用全集成神经启发忆阻器芯片 (STELLAR) 进行边缘学习的补充材料。包含器件制造细节、芯片架构、STDP 学习规则方程和实验数据。相比 HNPU 系统实现\
  \ 35 倍能耗降低。"
cite: "待补充. Supplementary Materials for Edge Learning Using Neuro-Inspired Memristor Chip[J].\
  \ Science, 2023. DOI: 10.1126/science.ade3483."
aiSum: "STELLAR 边缘学习芯片补充材料：器件制备、STDP 规则、35x 能耗降低。"
confidence: "high"
---

Corresponding authors: Bin Gao, gaob1@tsinghua.edu.cn; Huaqiang Wu, wuhq@tsinghua.edu.cn

Science 381, 1205 (2023)

DOI: 10.1126/science.ade3483

The PDF file includes:

Materials and Methods

Figs. S1 to S11

Tables S1 to S3

References

Other Supplementary Material for this manuscript includes the following:

Movies S1 to S3

# Materials and Methods

# 1. Algorithm for the STELLAR architecture

The STELLAR algorithm was developed to enable on-chip learning with memristors. It employs sign-based weight update calculations and utilizes a reconfigurable threshold in calculating the signs of errors. The STELLAR algorithm was designed as a generic approach to facilitate the implementation of on-chip learning with memristors for various neural networks. Considering that the manufactured memristor chip was designed to implement a two-layer neural network, the following explanation of the algorithm is based on this network. The details of the algorithm for other neural networks can be inferred from the following description.

A two-layer neural network with dimensions of $7 8 4 \times 1 0 0 \times 1 0$ was constructed; it employed a rectified linear unit (ReLU) as an activation function for low-cost hardware implementation. Each weight value was represented as the differential conductance of a pair of memristors. The on-chip learning consisted of two stages: the forward and weight update stages (fig. S1B). The forward inference was conducted using the memristor crossbar arrays (Fig. 2A):

$$
\boldsymbol {Y _ {1}} = R e L U (\boldsymbol {W _ {1} ^ {\bar {T}}} \cdot \boldsymbol {X})
$$

$$
\boldsymbol {Z} = \boldsymbol {W} _ {2} ^ {T} \cdot \boldsymbol {Y}
$$

$$
\mathbf {Y} _ {2} = R e L U (\mathbf {Z}) \text {(T h i s s t e p c o u l d b e s k i p p e d)}
$$

where X is the input vector, $Y _ { I }$ is the 1st-layer output vector, Z is the $2 ^ { \mathrm { n d } }$ -layer weighted-sum vector, $Y _ { 2 }$ is the $2 ^ { \mathrm { n d } }$ -layer output vector (for the output layer, this step could be omitted according to the algorithmic configurations), and $W _ { I }$ and $W _ { 2 }$ are the conductance weight matrices of the $1 ^ { \mathrm { s t } }$ and $2 ^ { \mathrm { n d } }$ layer, respectively. The weight update was performed for each input vector. The learning algorithm aimed to update the conductance optimally to minimize the loss function of the network output and target. The square loss function was used in this work; thus, the error vector was calculated as:

$$
\boldsymbol {E} = \boldsymbol {T} - \boldsymbol {Y} _ {2} \text {o r}
$$

$$
\boldsymbol {E} = \boldsymbol {T} - \boldsymbol {Z} (\mathrm {W} / \mathrm {O} \text {t h e R e L U a t t h e o u t p u t l a r})
$$

where T is the target vector, and E is the error vector. The signs of the errors were extracted to determine the weight update direction instead of the accurate values:

$$
\Delta W _ {2} = \boldsymbol {S} \boldsymbol {Y} _ {1} \cdot \left(\boldsymbol {S} \boldsymbol {Y} _ {2} ^ {T} \odot \boldsymbol {S} \boldsymbol {E} ^ {T}\right) \text {o r}
$$

$$
\Delta W _ {2} = S Y _ {1} \cdot S E ^ {T} (\mathrm {W} / \mathrm {O} \text {t h e R e L U a t t h e o u t p u t l a r}
$$

where $s Y _ { I }$ is the sign vector of the 1st-layer output, $s Y _ { 2 }$ is the sign vector of the $2 ^ { \mathrm { n d } } .$ -layer output, and SE is the ternary sign vector of the error. The elements sy1, sy2, and se in the sign vectors $s Y _ { I }$ , SY2, and SE were defined as follows:

$$
s y _ {1} = \left\{ \begin{array}{l l} 1, & y _ {1} \geq C _ {1} \\ 0, & y _ {1} <   C _ {1} \end{array} \right.
$$

$$
s y _ {2} = \left\{ \begin{array}{l l} 1, & y _ {2} \geq C _ {2} \\ 0, & y _ {2} <   C _ {2} \end{array} \right.
$$

$$
s e = \left\{ \begin{array}{c c} + 1, & e \geq T h \\ - 1, & e \leq - T h \\ 0, & e l s e \end{array} \right.
$$

where $y _ { I } , y _ { 2 } .$ , and e are the elements of vectors $Y _ { I } , Y _ { 2 } ,$ and E, respectively. The $C _ { I }$ and $C _ { 2 }$ could be flexibly reconfigured. If the ReLU activation function was applied for the weighted-sum output $\boldsymbol { Z }$ vector, the $C _ { I }$ value was typically the maximum among the 1st-layer outputs multiplied

by 0.4, and the C2 value was typically set as zero. Meanwhile, if the ReLU function was omitted for the output layer, there would be no C2, and the C1 value typically amounted to zero. The threshold Th filtered out the small error values, i.e., |se|<Th, which prevented weight updates that were extremely sensitive and improved the convergence of the