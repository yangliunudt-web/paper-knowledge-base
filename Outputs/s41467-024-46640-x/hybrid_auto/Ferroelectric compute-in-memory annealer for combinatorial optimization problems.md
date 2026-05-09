---
title: "Ferroelectric compute-in-memory annealer for combinatorial optimization problems"
authors:
  - "Xunzhao Yin"
  - "Yu Qian"
  - "Alptekin Vardar"
  - "Marcel Guenther"
  - "Franz Mueller"
  - "Nellie Laleni"
  - "You Chu"
  - "Jiang Wu"
  - "Xiaotian Yao"
  - "Chang Liu"
  - "Zheng Li"
  - "Zhen Liu"
  - "Chen Yao"
  - "Frank Hoppensteadt"
  - "Catherine Mead"
  - "Qi Liu"
  - "Weisheng Li"
  - "Zhigang Su"
  - "Xiaotian Yao"
date: "2023-01-01"
year: "2023"
journal: "Nature Communications"
doi: "10.1038/s41467-023-46640-x"
abstract: "Computationally hard combinatorial optimization problems (COPs) are ubiquitous in many applications. Various digital annealers, dynamical Ising machines, and quantum/photonic systems have been developed for solving COPs, but they still suffer from the memory access issue, scalability, restricted applicability to certain types of COPs, and VLSI-incompatibility, respectively. Here we report a ferroelectric field effect transistor (FeFET) based compute-in-memory (CiM) annealer for solving larger-scale COPs efficiently. Our CiM annealer converts COPs into quadratic unconstrained binary optimization (QUBO) formulations, and uniquely accelerates in-situ the core vector-matrix-vector (VMV) multiplication operations of QUBO formulations in a single step. Specifically, the three-terminal FeFET structure allows for lossless compression of the stored QUBO matrix, achieving a remarkably 75% chip size saving when solving Max-Cut problems. A multi-epoch simulated annealing (MESA) algorithm is proposed for efficient annealing, achieving up to 27% better solution and ~2X speedup than conventional simulated annealing. Experimental validation is performed using the first integrated FeFET chip on 28nm HKMG CMOS technology, indicating great promise of FeFET CiM array in solving general COPs."
abstract_cn: "组合优化问题（Max-Cut、图着色、旅行商问题等）可映射为Ising/QUBO模型并通过模拟退火求解。本文展示了一种基于FeFET交叉开关阵列的铁电存算一体退火器，利用交叉架构的固有并行性实现组合优化问题的高能效硬件加速求解。"
keywords:
  - "[[FeFET]]"
  - "[[In-memory computing]]"
  - "[[Combinatorial optimization]]"
  - "[[Annealer]]"
  - "[[QUBO]]"
  - "[[Crossbar]]"
cite: "[1] Yin X, Qian Y, Vardar A, et al. Ferroelectric compute-in-memory annealer for combinatorial optimization problems[J]. Nature Communications, 2023."
aiSum: "FeFET交叉阵列退火器：组合优化→Ising/QUBO映射，硬件加速模拟退火，高能效COP求解。"
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
  - "[[In-memory computing]]"
  - "[[crossbar]]"
---

Received: 17 October 2023

Accepted: 5 March 2024

Published online: 18 March 2024

Check for updates

Xunzhao Yin 1,2,6, Yu Qian 1,6, Alptekin Vardar3 , Marcel Günther3 , Franz Müller 3 , Nellie Laleni3 , Zijian Zhao4 , Zhouhang Jiang4 , Zhiguo Shi1,2, Yiyu Shi 4 , Xiao Gong 5 , Cheng Zhuo 1,2,7 , Thomas Kämpfe 3,7 & Kai Ni 4,7

Computationally hard combinatorial optimization problems (COPs) are ubiquitous in many applications. Various digital annealers, dynamical Ising machines, and quantum/photonic systems have been developed for solving COPs, but they still suffer from the memory access issue, scalability, restricted applicability to certain types of COPs, and VLSI-incompatibility, respectively. Here we report a ferroelectric field effect transistor (FeFET) based compute-inmemory (CiM) annealer for solving larger-scale COPs efficiently. Our CiM annealer converts COPs into quadratic unconstrained binary optimization (QUBO) formulations, and uniquely accelerates in-situ the core vector-matrixvector (VMV) multiplication operations of QUBO formulations in a single step. Specifically, the three-terminal FeFET structure allows for lossless compression of the stored QUBO matrix, achieving a remarkably 75% chip size saving when solving Max-Cut problems. A multi-epoch simulated annealing (MESA) algorithm is proposed for efficient annealing, achieving up to 27% better solution and ~ 2X speedup than conventional simulated annealing. Experimental validation is performed using the first integrated FeFET chip on 28nm HKMG CMOS technology, indicating great promise of FeFET CiM array in solving general COPs.

Combinatorial optimization problems (COPs), as shown in Fig. 1a, are prevalent in diverse fields, including logistics, resource allocation, communication network design, finance, drug discovery, and transportation systems, etc.1–4 . Often, these problems belong to the class of non-deterministic polynomial-time-hard (NP-hard) problems, representing some of the most challenging computational tasks in the NP domain. Solving COPs using digital computers based on the von Neumann architecture poses difficulties, given the exponential growth in required resources regarding the computational power and latency as the problems scale up5–7 . Therefore, there is a pressing need to explore novel hardware design with alternative architectures and algorithms that can efficiently tackle COPs. This research frontier holds

crucial implications for real-world applications, with the potential to address complex and resource-intensive problems with greater effectiveness.

Many COPs, including graph coloring, Max-Cut, and traveling salesman problem, etc., can be mapped to the Ising spin glass model or often go by the name QUBO (i.e., quadratic unconstrained binary optimization)8 , which have emerged as a powerful framework for effectively modeling and solving a wide range of COPs9 . In this framework, the problem variables are elegantly represented as spins, and the interactions or constraints between variables are represented as spin-to-spin couplings. The objective function of the problem can then be mapped to the Hamiltonian energy function of the Ising model. The

1 Zhejiang University, Hangzhou, China. 2 Key Laboratory of CS&AUS of Zhejiang Province, Hangzhou, China. 3 Fraunhofer IPMS, Dresden, Germany. 4 University of Notre Dame, Notre Dame, USA. 5 National University of Singapore, Singapore, Singapore. 6 These authors contributed equally: Xunzhao Yin, Yu Qian. 7 These authors jointly supervised this work: Cheng Zhuo, Thomas Kämpfe, Kai Ni. e-mail: czhuo@zju.edu.cn; thomas.kaempfe@ipms.fraunhofer.de; kni@nd.edu

# aCombinatorial optimization problems

![](images/0299299ce4efe2daaa52e16bbbd3d0c71cae302b60f5cbf9cb9923a8013681a8.jpg)

![](images/71f830b2be8f2dbbec40d9042b0c8fa32aff44c77806242619a10c532b1170fe.jpg)  
Max Cut

![](images/77a5fd00f6d9b59c4f66d1ba5d5a61b8601b3e101c762ee50a91e75be18afe4c.jpg)  
Graph Coloring

![](images/26b625a74a45de5331aff2673e4418dae1533a2eed71d72846018b6964313c23.jpg)  
Prime ictorization

![](images/d5def4d78f01a16e8c8aca8109a5e60dc3caf2d60139195b2b5db3ced2f98b51.jpg)  
b Quadratic Unconstrained Binary Optimization

![](images/facdd0d04953bc0da88a5700d2ad1edc4d77b9a8d8e76b9ceef4d72c0230c59e.jpg)  
Q:a matrix, mapping a problem X: binary state vector

![](images/8cb1f3b51476e3c3b41d614162f861eca3a0c21ca068f579078d9e9e160954f8.jpg)  
C

![](images/953613a6e58094e73f570b01846194d97c8ebde0cf89c03564d91dd3fd51aed6.jpg)  
d

![](images/c3bda37f29e969ea79cfbcd30cfe057b07ccc4979e755e8d59fab851a9d14038.jpg)

![](images/0338a45efff2130cc2fae3392151d1cb103d69afa33302932af84654d980c92a.jpg)  
f QUBO formulation

![](images/e769aa7fd213f0842f6411832c3b4821212472f23c2d224e3503ddde8c2da0ca.jpg)  
FeFET crossbar array

$$
\operatorname {S i z e} \left(Q ^ {\prime}\right) \leq \operatorname {S i z e} (Q)
$$

![](images/b27c4861292c3c3f6f83a7eb4a7b6273f31eb4de54811a674f9bd6274c020dff.jpg)

Model compression via general QUBO form with asymmetric input vectors

![](images/01035cc7c54d55edc09c0c511b4d37b3e6424fca7645bc22844c9b0c7ee71496.jpg)  
QUBO with asymmetric input vectors   
g

$$
f = \mathbf {x} ^ {T} Q ^ {\prime} \mathbf {y} \propto \sum_ {i} I _ {i}
$$

$$
\mathbf {x} ^ {T} = \left(x _ {1} x _ {2} \dots x _ {K}\right) \mathbf {y} = \left(y _ {1} y _ {2} \dots y _ {M}\right) ^ {T} x _ {i}, y _ {i} \in \{0, 1 \}
$$

![](images/6b7769912f57064cb59d5e148cb6efa94e7aaa2d548e98c94f19431fdddc7879.jpg)  
Compressed crossbar array   
Fig. 1 | Acceleration of solving COPs with CiM array. a COPs (e.g., Max-Cut, graph coloring, prime factorization etc.) can be converted to b xT Qx QUBO formulation. Many hardware systems, including c digital annealing system, d dynamical system, and e CiM system are promising for solving COPs. f Due to the unique   
characteristics of FeFET-based CiM crossbar, it can implement typical xT Qx QUBO formulation with symmetrical input vectors. g The array can also accelerate a more general and compact xT Q0 y QUBO formulation with asymmetrical vectors, thus achieving high efficiency and low cost.

solution of a problem then corresponds to the combination of spins that minimizes the Ising Hamiltonian $H _ { \mathrm { P } } ,$ which can be formulated as follows:

$$
\min  H _ {P} = \sum_ {i, j = 1} ^ {N} J _ {i j} \sigma_ {i} \sigma_ {j} + \sum_ {i = 1} ^ {N} h _ {i} \sigma_ {i} \tag {1}
$$

where N denotes the number of spins, and $\sigma _ { i } \in \{ 1 , - 1 \}$ represents the state of spin $i . J _ { i j }$ and $h _ { i }$ stand for the coupling between spin i and j and the self-coupling of spin i, respectively. Through a simple variable change $\sigma _ { i } = 1 - 2 x _ { i } , \ x _ { i } \in \{ 0 , 1 \}$ , the Ising Hamiltonian (Eq. (1)) can be readily transformed into a QUBO matrix form10,11 as

$$
H _ {Q U B O} = \mathbf {x} ^ {T} Q \mathbf {x} \tag {2}
$$

where $\mathbf { x } = ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } )$ , and Q is a symmetric or an equivalent upper triangular n × n matrix12,13, as shown in Fig. 1b. For instance, consider a Max-Cut problem defined on an undirected graph G(V, E), where V represents the set of vertices, and E represents the set of edges12. The Max-Cut problem is mapped into the QUBO form by introducing a binary variable xi ∈ {0, 1} for each vertex i ∈ V, where xi takes the value 1 if vertex i is assigned to one set and 0 if it belongs to the other set. The objective function of the Max-Cut problem can then be formulated as follows:

$$
\min  \sum_ {(i, j) \in E} \left(2 x _ {i} x _ {j} - x _ {i} - x _ {j}\right) \tag {3}
$$

Considering the binary xi, such a form can be easily represented as the xT Qx QUBO form12,13. The conversion of other COPs, such as graph coloring problems and prime factorization problems, into the QUBO form is further elaborated in Sec. 1 of Supplementary Information.

To solve COPs efficiently, various alternative computing hardware are under active research. Figure 1c, d briefly summarizes different electronic implementations. One class of hardware are digital ASIC annealers, where various annealing algorithms are implemented in digital circuits14–17. Usually the spin coupling matrix is stored in memory and data need to be frequently transferred between memory and computing units for energy computation and annealing, which can be energy- and time-consuming as the problem scales up. An attractive alternative is dynamical system Ising machines, where the intrinsic system dynamics and tendency to settle at lowest energy state is exploited to solve the COPs, as shown in Fig. 1d. Once the spin coupling matrix are programmed within the hardware, these solvers naturally explore the solution space and ultimately find the spin combination that minimizes the Ising energy without explicitly executing annealing algorithms. Examples include the oscillator-based Ising machine (OIM)18–20, latch-based Ising machine21–23, and optical-based coherent ising machine (CoIM)24–28.

While the concept of such a system holds immense promise, there are several challenges that remain to be addressed. First, the dynamics and robustness of dynamical Ising solvers is highly sensitive to the coupling implementations between spins, as a slight deviation in coupling strength can lead to convergence disruption of the solution19,22. Therefore, it poses a significant challenge in precisely mapping the spin coupling matrix into hardware. Second, exploiting dynamical Ising solvers to their full potential requires mapping the entire problem onto a single solver. For large scale problems that are beyond the capacity of the solver, how to efficiently map the problems to multiple separate chips and implement chip-to-chip communication while maintaining system dynamics requires substantial work. Therefore, scaling of dynamical Ising solver is a critical challenge. Lastly, integration of self-interaction into these dynamical Ising solvers is not straightforward, thus allowing easy mapping of only a subclass of COPs without self-interaction terms, such as Max-Cut, Sherrington-

Kirkpatrick models, $\mathbf { e t c ^ { 1 8 , 2 9 } } .$ . Many COPs requiring self-interaction terms after mapping to the Ising model, including graph coloring, prime factorization, bin packing, etc., remain yet to be solved by dynamical Ising solvers. Other unconventional approaches, including quantum and photonic implementations, generally utilize their unique physical behavior to directly represent the Ising models. However, many of them are challenging to integrate into silicon VLSI technologies. For example, the D-Wave quantum annealers proposed in refs. 30–32 require expensive cryogenic cooling and exhibit limited connectivity between spins. Optical Ising machine consumes extremely long optic fiber to implement the solver, making its integration highly challenging25.

In this article, we perform a hardware-algorithm co-design of a compute-in-memory (CiM) based annealer to efficiently solve QUBO formulations, thus the COPs, as shown in Fig. 1e. The most well-known CiM hardware system is probably the crossbar array for acceleration of the vector-matrix multiplication (VMM), a core operation in neural networks33. In this scheme, the matrix is stored in memory, including volatile and nonvolatile memory (NVM), and the VMM computations are performed in CiM arrays without energy-consuming and slow data movement between memory and computing units, thus exhibiting superior energy efficiency. Drawing inspiration from this, and recognizing that the QUBO formulation is composed of a vector-matrixvector (VMV) multiplication as shown in Eq. (2), this article aims at expediting the in-situ VMV multiplication through CiM approach, thus accelerating solving COPs. Our CiM annealer could potentially address the aforementioned challenges faced by digital annealers and dynamical Ising solvers, offering several advantages: (i) our CiM approach stores the QUBO matrix in memory and directly performs VMV multiplication in memory, avoiding the data movement bottleneck seen in digital annealers; (ii) by programming multiple FeFET devices with binary states to represent a single matrix coefficient and performing the VMV multiplication in analog domain, CiM annealer is intrinsically robust against the noise and inaccuracy of the coupling matrix mapping. In contrast, Ising solvers can be vulnerable to these issues; (iii) Unlike dynamic Ising solvers, which rely on the overall system dynamics to solve COPs, our CiM-based approach easily handles larger-scale problems beyond the capacity of our chip by decomposing the corresponding QUBO formulation into smaller forms, then independently mapping and computing these forms across multiple CiM chips; (iv) Lastly, our CiM array can readily implement selfinteraction terms within the QUBO formulation by programming the diagonal matrix coefficient value onto the crossbar cells. In conclusion, CiM approach when seamlessly integrated with efficient annealing algorithms, could offer a powerful hardware platform for COPs.

Here we propose to develop an ferroelectric field effect transistor (FeFET) based CiM crossbar array to accelerate VMV multiplications of QUBO, as shown in Fig. 1f. FeFETs based on ferroelectric $\mathsf { H f O } _ { 2 }$ are a prime candidate technology platform to implement CiM system for insitu VMV multiplication. First, it is naturally a three-terminal nonvolatile device, ideal for VMV multiplication, where the coupling matrix element can be stored in the polarization state of the FeFET and the two inputs (not necessarily identical) can be applied on the gate and drain, respectively. On the contrary, other two-terminal NVM based CiM system would require an VMM operation to calculate the intermediate result, and then apply another dot multiplication in digital domain to complete the VMV multiplication. Second, HfO2 based FeFET exhibits superior energy efficiency with its electric field driven polarization switching mechanism and high ON/OFF ratio3 4,35 while current-driven memristor devices require additional access transistors and complex sensing circuitry, leading to much more energy consumption than FeFETs. Third, FeFETs stand out due to its CMOS compatibility and scalability34,35, while embedded flash struggles to scale beyond the 28nm node36. When performing VMV multiplication, a FeFET-based CiM array necessitates lower write/read

voltages $( V _ { w r i t e } / V _ { r e a d } { = } 4 / 1 V )$ and less write time ( ~ 10ns) compared to flash $( V _ { w r i t e } / V _ { r e a d } = 1 5 / 4 . 5 V , t _ { w r i t e } = 1 m s ) ^ { 3 7 }$ . This results in reduced energy consumption and execution time. Therefore, a compact single FeFET CiM array is developed in this work for the QUBO computations. Compared to memristor-based Max-Cut problem solver38,39, our work represents a significant advancement in CiM based annealers. The innovation of this work lies in: i) first proposal of a compact and effective 1FeFET1R CiM implementation for in-situ VMV multiplication by exploiting the three-terminal structure and nonvolatile storage of FeFETs. These voltage-driven devices feature with superior write energy and unique single-step 3-input multiplication capability; ii) proposing a lossless compression method for the QUBO formulation by capitalizing on the FeFET CiM array’s capability to accommodate insitu VMV multiplication with asymmetrical (non-identical) input vectors as shown in Fig. 1g, thus significantly reducing the array size of the crossbar and expanding the problem-solving capacity to larger scales; iii) introducing a multi-epoch simulated annealing (MESA) algorithm to enhance the annealing process and improve the solution quality, which can quickly find the optimal solution of COPs via iterative QUBO computations; iv) first experimental demonstration of a FeFET CiM array to showcase its efficacy in accelerating QUBO computations and highly competitive performance against other hardware alternatives in solving complex COPs. The overall working flow of our CiM based annealer is depicted in Sec. 2 of Supplementary Information and as follows: (i) A COP is initially converted into a QUBO formulation xT Qx as shown in Fig. 1f. (ii) This QUBO formulation is then losslessly compressed into a more general and compact form with asymmetric variable vectors $\mathbf { x } ^ { T } { \cal Q } \mathbf { y } ,$ , as shown in Fig. 1g. (iii) The QUBO matrix Q0 of the compressed formulation is mapped onto a FeFET-based crossbar array, which inherently performs single-step VMV multiplication. The summed current of the crossbar represents the value of the compressed QUBO objective function. (iv) The solving process utilizes a MESA algorithm. In each iteration of the annealing process, the FeFETbased array computes the QUBO formulation value, and the objective function value is determined. (v) After the MESA process, the variable vector configurations that correspond to the optimal objective function value are obtained and translated into the solution for the given COP.

# Results

# 1FeFET1R based CiM architecture

Considering the great promise of FeFET crossbar array in accelerating VMV multiplication with both symmetric and asymmetric input vectors for COPs in QUBO formulation, FeFET CiM array is designed and experimentally demonstrated. Figure 2 shows the cell and array design and experimental data illustrating the CiM hardware. The FeFET CiM chip is integrated onto an industrial 28nm high-κ metal gate FeFET technology platform40. The device features an approximately 8nm doped ${ \mathsf { H f O } } _ { 2 }$ as the ferroelectric layer, as shown in the schematic crosssection and transmission electron microscopy (TEM) cross-section in Fig. 2a. The structural similarity of FeFET to standard logic transistor, coupled with its CMOS compatibility and ultra-scalable nature of ferroelectric $\mathrm { H f } 0 _ { 2 } ,$ enables the integration of FeFETs with Si CMOS, which is leveraged in this work. For the demonstration, an 32 × 32 FeFET array is designed, where the chip layout is composed of array core, the word line (WL) driver, source line (SL)/data line (DL) driver, and the analogto-digital converter (ADC) is shown in Fig. 2b. The fabricated chip micrograph is shown in Fig. 2c.

As shown in Fig. 2d, our approach encodes the coupling matrix element q into the polarization states of the FeFET. By applying inputs x and y to the FeFET’s gate and drain, respectively, the resulting channel current $i _ { D L }$ corresponds to the scalar product of these three, i.e., $i _ { D L } = x \times q \times y$ . Consequently, the core computation within VMV multiplication can be implemented with minimal overhead. This sets our approach apart from other two-terminal NVM devices like

memristors, which are limited to singular multiplications between the input and the stored values41,42. Figure 2e further shows the relationship between cell current and gate voltage $( \mathrm { i } . \mathrm { e } . , V _ { \mathrm { w L } } )$ for two memory states across 60 distinct devices. The coupling matrix element is encoded as the polarization states, programmed via $+ 4 \mathsf { V } / \mathsf { - } 4 \mathsf { V } ,$ , 1μs gate pulses, which induce the polarization to orient towards the channel/ gate-metal, and hence set the threshold voltage $( V _ { \mathrm { T H } } )$ of FeFET into the low-VTH (i.e., q = 1)/high-VTH state $( \mathrm { i } . \mathrm { e } . , q = 0 )$ , respectively. By choosing an appropriate read gate bias (i.e., input x), the resultant cell current realizes the scalar product.

While the design is compact and elegant, a potential challenge arises from the need to manage FeFET variation, which can lead to compromised accuracy in VMV multiplications. Despite ongoing improvements in materials and processes43, FeFET variation remains a significant factor in CiM applications, as indicated in Fig. 2f. In this work, we employ an 1FeFET1R cell structure as depicted in Fig. 2g to effectively mitigate the device variations and enhance the accuracy of the VMV multiplication. By incorporating a series resistor, the cell’s ON current, regulated by the current limiter, becomes independent of the FeFET’s ON current44,45. Such structure ensures that the presence of variation in $V _ { \mathrm { T H } }$ does not manifest as variation in the cell’s ON current. As a proof of concept, each FeFET is connected with a series resistor for the same group of 60 devices. Figure 2h shows the 1FeFET1R cell I-V characteristics, which exhibits the same $V _ { \mathrm { T H } }$ distribution as that in Fig. 2e, while its ON current variation can be significantly suppressed, as illustrated in Fig. 2i. While there is a trade-off involving the reduction in the cell’s ON current, the ON/OFF ratio still exceeds 1000, ensuring that there should be no constraints on the practical array size. As a result, the 1FeFET1R CiM array is designed as illustrated in Fig. 2j, where the resistor is implemented with a fully integrated MOSFET. A more detailed description of our chip measurement can be referred to Fig. S3 in Sec. 3 of Supplementary Information. Additionally, to successfully program the array while suppressing the program disturb, a standard $V _ { \mathrm { W } } / 3$ is adopted46, as illustrated in Fig. S5a. Also the memory array error rate shown in Fig. S5b as a function of the write conditions clearly demonstrates that it is possible to reduce the write voltage if a long write latency can be tolerated47. Furthermore, the current within a column exhibits a linear relationship with the number of activated cells, corroborated across 20 different arrays as shown in Fig. 2k. Therefore, it validates the linearity and functionality of the crossbar array, and also demonstrates the tightly controlled distribution of the output current. Moreover, the CiM results are stable up to $1 0 ^ { 5 }$ seconds without noticeable degradation, as shown in Fig. S5c. These results lay a robust foundation for the acceleration of VMV multiplication in this work.

Lastly, we present the mapping of the generalized QUBO form, $\mathbf { x } ^ { T } \boldsymbol { Q } \mathbf { y }$ , onto the 1FeFET1R CiM array, as illustrated in Fig. 2l and m. The details of the general QUBO form are depicted in Fig. 2l. The input vectors, x and y, are mapped to the WL and SL inputs, respectively, as shown in Fig. 2m. This figure further shows the circuit implementation of the FeFET-based crossbar array along with its associated peripheral circuits. The QUBO matrix is mapped onto the FeFET crossbar by storing M-bit precision matrix elements within M 1FeFET1R cells. Each cell stores a single bit of the matrix element, therefore an n × n QUBO matrix corresponds to the implementation of n × N cells, where N is n × M. To perform the VMV multiplication, the WL driver activates all rows of the FeFET crossbar, and the SLs of the columns are activated per the input y (i.e., ‘1’ indicates ON, and ${ \bf \nabla } ^ { \prime } { \bf 0 ^ { \prime } }$ indicates OFF). The consecutive column outputs are directed to the column-shared analogdigital converters (ADCs), converted to digits, and further processed through Shift and Add units, generating the dot product between the stored multi-bit coupling vector and input vector x. The final value of QUBO xT Qy function is then accumulated as the output of the current iteration in the annealing process and stored in the output buffer. In this way, our proposed CiM crossbar realizes the VMV multiplication

![](images/234786454c4a2547ea396c07f5d3190452c3f15db254177188756fe8292e3699.jpg)

$$
i = x \times q \times y
$$

![](images/43ec88ad104bdced83bd31a99c45d643257a07c86f2ff294d2da6efb4c7960f8.jpg)  
d

![](images/28e94fe58acdc8d820a245b72799f36e5516371f8c63dbcefc813965ec60aff7.jpg)

![](images/b4b7dd41eb3146ecfccb36b4fa7857325257c189f4dd2817bb838910e91b4f30.jpg)

![](images/166b3a7ff5cd414982385285fcf686cbc057b26caff26181ea50595580d38ac4.jpg)

![](images/92aec2e50535316663216cc30c4d71dfd25f8dc898b21e520c4fda2c51ee442f.jpg)

![](images/d447c0175c1f2070085c51e1329f2fa058e60a8032fffaeebfd6c087fa7f8f8c.jpg)

![](images/4a9b6d4b357ebee9553c49b7fb132995bbb5b341f1ba784a54c9109403be3ea2.jpg)  
j

$$
\sum_ {k = 1} ^ {N} i _ {D L k} = \mathbf {x} ^ {T} Q \mathbf {y}
$$

![](images/4ec0b497da0f55c82cee0194a3f0992f9be004b927d3f8ab56c40c63cb6e8344.jpg)  
k

IGeneral QUBO form: $f = \mathbf { x } ^ { T } Q \mathbf { y }$

$$
Q = \left( \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \ldots & a _ {1 n} \\ 0 & a _ {2 2} & \ldots & a _ {2 n} \\ 0 & 0 & \ddots & \vdots \\ 0 & 0 & \ldots & \boxed {a _ {n n}} \end{array} \right) = (\boxed {A _ {1}} \ldots \boxed {A _ {n}})
$$

Each matrix element has M bits andmapped to M1FeFET1R cells

Array size: n x N

$$
N = n \times M
$$

![](images/253a1ebadd8fe5a3bb3cb555c4d960333ffe3cf998846e6ee7a0331049ad707f.jpg)  
Fig. 2 | FeFET-based CiM array for QUBO acceleration. a FeFET schematic and TEM cross section, featuring an 8nm doped $\mathsf { H f O } _ { 2 } \mathsf { s }$ the ferroelectric. b Layout of an 32 × 32 FeFET array composed of core and peripherals. c Micro-graph of the fabricated chip, where bond pads are visible. d The current of a FeFET $i _ { D L }$ corresponds to the scalar product of stored value q (i.e., threshold voltage $V _ { \mathrm { T H } } )$ , and inputs x and y, applied at the gate and drain, respectively. e The $I _ { \mathrm { D L } } \mathbf { \cdot } V _ { \mathrm { W L } }$ characteristics of 60 FeFETs for the two memory states. f Significant ON current variation of FeFETs will result in compromised accuracy in VMV multiplications. g An 1FeFET1R cell   
structure can suppress the $I _ { \mathrm { O N } }$ variability. h $I _ { \mathrm { D L } } \mathbf { - } V _ { \mathrm { W L } }$ of 60 1FeFET1R cells with 1MΩ resistor. i A significantly narrower $I _ { \mathrm { O N } }$ distribution for the 1FeFET1R cells, thus substantially enlarging the practical CiM array size. j As a result, the 1FeFET1R CiM array implementing a general QUBO formulation is proposed. k Measured column current shows a good linearity with respect to the number of activated cells in the column, thus promising for VMV multiplication. l QUBO formulation mapping to m FeFET-based CiM array architecture.

![](images/a53975ee31d50a56085efd59f05522b599b70146d708d214870b081e60bcbda4.jpg)

![](images/c06157acc85a7b873597db4bfc7cbfe57197f9334142888542b8ae3c44bb1ced.jpg)

![](images/d58c5b7deade63d47bd09cd0a882ee00e800b991ac4839622674fb39f064b309.jpg)

![](images/d92d0c3ab55b990834f1832cd30cfedce26842d5892f8c96f31827446c3e53d9.jpg)

![](images/866ee98965b5b49e23969bfae5ee7fb64558a769c7bbfe9ffb4e055af4085a1b.jpg)

![](images/ee984d190871e9e33eb34a33f9ab80995f8d8dec6b8059abd3f7cb927dc0bb1b.jpg)  
Fig. 3 | Proposed lossless compression of the QUBO matrix. Conventional xT Qx QUBO formulation for many COPs like a graph coloring and b Max-Cut is highly sparse. When directly mapped to a CiM array, significant portion of hardware could be wasted. c A lossless compression method is proposed to convert a large scale xT Qx formulation to a more compact and dense ${ \bf x _ { h } } ^ { T } Q ^ { \prime } { \bf x _ { v } }$ formulation by   
leveraging the three-terminal FeFET-based CiM array, where x = x ∪ x . d The conceptual flow of xT Qx compression leveraging the symmetry of the Q matrix. Chip size savings after compression for e graph coloring and f. Max-Cut problems, are presented in (a) and (b), respectively.

directly by simply applying two input vectors within each iteration, and ultimately solves the QUBO formulation in Eq. (2), synergizing with the efficient annealing algorithms.

# QUBO matrix lossless compression

Mapping the QUBO formulation directly onto the FeFET crossbar CiM array with two identical or symmetrical input vectors applied on the WLs and SLs, respectively, has revealed a challenge in terms of low chip utilization. This issue stems from the inherent sparsity often observed in QUBO matrix converted from COPs. Figure 3a, b show the sparsity of QUBO matrix for graph coloring problems48 and Max-Cut problems49, respectively, across varying problem instances with different node counts. Remarkably, the majority of the matrix elements (typically exceeding 85%) assume zero values. Therefore, when directly mapping

the QUBO matrix onto the FeFET crossbar array, a large portion of FeFET cells witin the array are programmed to state $\mathrm { { ' } } 0 ^ { \prime } \mathrm { { ( i . e . , h i g h . } } V _ { \mathrm { { T H } } }$ state). Although these ‘OFF’ cells do not actively participate in the VMV multiplication during QUBO computation, they still incur additional hardware area overhead and contribute to leakage power consumption. With the expansion problem complexity and scale, the hardware size essential for accommodating the converted QUBO matrix exhibits quadratic growth with the node count, thus leading to substantial hardware resources waste. Such low hardware utilization therefore introduces formidable obstacles to CiM annealers in solving largerscale COPs efficiently.

To minimize the hardware inefficiencies stemming from sparse matrix mapping, a lossless compression technique is proposed here, as illustrated in Fig. 3c. This approach entails pruning the sparse and

symmetric QUBO matrix, originally of size n × n within the $\mathbf { x } ^ { T } Q \mathbf { x }$ formulation, into a more compact dense matrix of size $p \times q$ within the ${ \bf x _ { h } } ^ { T } { Q } ^ { \prime } { \bf x _ { v } }$ formulation, where $\mathbf { x _ { h } } \cup \mathbf { x _ { v } } = \mathbf { x }$ and $p , q \leq n$ . This innovative technique achieves substantial chip size reduction by capitalizing on the distinctive attributes of the three-terminal FeFET crossbar CiM array, particularly when implementing the xT Qy formulation, where x and y need not be symmetrical. Figure 3d illustrates the methodology of QUBO matrix compression, elucidated through a concrete example, which consists of 4 steps:

Step 1. The input vectors are organized in order of the corresponding node degrees. Node degree represents the significance of the associated input variable in QUBO formulation computation, gauging the extent of its involvement in nonzero scalar multiplications. Pruning is initiated from nodes with fewer connections.

Step 2. Row compression of Q matrix is carried out in the order of sorted input vector list obtained in STEP 1. For each selected input variable $x _ { i }$ from the list, if the respective row in matrix Q is compressible, every nonzero element within the row is added to the element at its corresponding diagonal position, capitalizing on the symmetrical nature of xT Qx formulation. Subsequently, the elements in the compressed row are set to zero, with rows containing the updated diagonal elements marked as incompressible to ensure lossless compression.

Step 3. Column compression mirrors the operation conducted in STEP 2, with nonzero elements within the compressed column added to the their respective diagonal elements, then set to zero. Columns containing updated diagonal elements are labeled as incompressible.

Step 4. The QUBO matrix’s compressed rows and columns, along with their corresponding variables in the input vectors, are eliminated, yielding the compressed QUBO matrix along with the compressed input vectors.

A detailed description of the compression methodology is featured in Fig. S6 in Sec. 4 of Supplementary Information. As a result, redundant rows and columns of QUBO matrix are removed, reducing crossbar array size required to implement the xT Qx QUBO formulation without sacrificing accuracy. The compressed QUBO matrix is mapped onto the FeFET crossbar for the iterative annealing of QUBO formalized COPs. The binary variable vectors $\pmb { \mathrm { x } } _ { \mathbf { h } }$ and $\mathbf { x _ { v } }$ associated with the compressed QUBO formulation are applied to the WLs and SLs of the FeFET CiM array, respectively. In this way, the proposed compression approach enhances the scalability of CiM hardware, thereby scaling up the capacity for solving larger-scale COPs.

The efficacy of the proposed compression technique has been evaluated. For the same problem instances of graph coloring and Max-Cut COPs, as analyzed in Fig. 3a, b, respectively, the corresponding chip size reduction percentages are elucidated in Fig. 3e, f. These results demonstrate that the compression method yields substantial savings in chip size compared to the implementations without compression38,39. Note that the extent of chip size reduction does not necessarily correlates with the node count in a problem. This is because that the distribution of nonzero elements within the QUBO matrix significantly affects the impact of the compression method. For instance, if all nonzero elements aggregate within a single row, the QUBO matrix could be compressed to just one row, yielding high chip size savings. Conversely, if each row contains only one nonzero element, and these nonzero elements are at different columns, compression of the QUBO matrix might not be feasible, even if it is sparse.

# Solving COPs with multi-epoch simulated annealing

Previously developed FeFET CiM array demonstrates its capability to accelerate the computation of the QUBO formulation, which matches with annealing algorithms for solving COPs. That is, the configurations

or solutions corresponding to the minimal QUBO energy are sought via an iterative annealing procedure. Simulated annealing (SA) algorithms were introduced to address the problem of local minimum trapping during the annealing process. The energy of the objective function, as computed by the configurations in current iteration, is compared with the energy state corresponding to current solution. If the computed energy is lower, the solution configurations are updated with the corresponding variable configurations. Conversely, if the energy is higher, the update retains a probability proportional to the temperature. Such annealing process has been adopted in prior NVM based annealers38,39. Nonetheless, conventional SA has demonstrated suboptimal performance in handling large-scale $\boldsymbol { \mathrm { C O P s ^ { 4 2 } } }$ . To accelerate the SA process while still ensuring high probability of finding optimal solutions, a multi-epoch simulated annealing (MESA) algorithm is herein proposed.

Figure 4a illustrates the detail of the MESA process. For each epoch, an optimal solution $( \mathbf { x } _ { h o p t } , \mathbf { x } _ { v o p t } )$ and its associated QUBO energy $E _ { o p t }$ are defined and sustained throughout the epoch. This records the lowest energy state attainable by the system, given the input configuration and the energy initialized to the optimal solution from the previous epoch. The QUBO energy, $E _ { n e w } ,$ is calculated using the CiM hardware, as previously detailed. If $E _ { n e w }$ is lower than the energy $E _ { o }$ of the last iteration, indicating a progression toward a lower energy landscape, this QUBO energy and its associated variable solution $( \mathbf { x _ { h } } , \mathbf { x _ { v } } )$ are accepted. The optimal solution $( \mathbf { x } _ { h o p t } , \mathbf { x } _ { v o p t } )$ along with its energy value $E _ { o p t }$ within this epoch are either updated or maintained, depending on the comparison between $E _ { n e w }$ and the optimal solution. Should $E _ { n e w }$ closely approximate $E _ { o } ,$ indicating that the system is trapped at a local minimum, the energy and its corresponding variable solution remain unaltered, and the trap count is updated. If $E _ { n e w }$ is notably larger than the energy $E _ { o } ,$ the system has a probability closely related to the temperature T to accept the variable solution, allowing a chance to escape from local minimum. Subsequently, the system introduces random perturbations by flipping a few bits in the input vectors, and proceeds to the next iteration. When the system is trapped at a local minimum, where the energy trajectory remains stagnant for a predefined period $C o u n t _ { m a x } ,$ the epoch concludes, the temperature resets, and a fresh epoch commences. As a result, the length of each epoch is dynamically adjusted according to the system’s advancement. The input configuration and its corresponding energy at the beginning of a new SA epoch are initialized based on the optimal solution and the energy recorded during the last epoch. Such initialization ensures the continuous convergence of MESA toward lower energy states.

Figure 4b shows the COP solving capability of MESA over that of conventional SA in identifying optimal solutions for prevalent Max-Cut problems. It can be seen that MESA outperforms the conventional SA across all Max-Cut problems, ranging in size from 800 to 3000 nodes, encompassing a search space spanning 2800 to 23000. As the node count increases, i.e., the problem complexity grows, MESA yields superior solutions to SA, boasting an improvement of up to 27% in cut value when addressing 3000-node problems. With the dataset tested, Fig. S7 shows that MESA consistently outperforms conventional SA in terms of success rate and time-to-solution, achieving nearly double the speedup compared to conventional SA. The improvements of MESA over conventional SA result from the multi-epoch annealing process, where each annealing epoch begins with the optimal input configuration from the previous one. This greedy initialization enhances the convergence of the objective function towards the global optimum. Moreover, MESA includes an adaptive annealing termination scheme within each epoch to prevent the algorithm from trapping at a local minimum for an extended number of iterations, thus reducing unnecessary time and resource consumption. Leveraging both software advancements (introduction of MESA) and hardware improvements, particularly notable enhancements in hardware resource utilization,

![](images/fbf174ba633c50378621bd162ef0c6af10325691526f09699a51a86f20757ac5.jpg)

![](images/3b7c58196c2cad0e5e30c2b92100a806c1f13178ed25d8cebda0a1814c06c8b0.jpg)

![](images/a8ac877cfeccd20a106eef27db2fbc0a6c0cb6f56c92c757e407b99e0eb8668b.jpg)

![](images/e75b09a4fb66d8708ef729384d8d10faa7c015787143b7dcffd19532dc484200.jpg)

![](images/4c1e7f318c16258b9e024d344e445fa2d8c040e9509a3c2c8771b025a723480e.jpg)

![](images/2aa3fdf6d47f50d28d8cdc2c39d00908463ae982a274d04a13b96cc9711b3a53.jpg)

![](images/733d9b87f8177d291cab094c0b65161f707c5b45d7a08d719e7aa1e3f71140a6.jpg)

![](images/40872c50c6001a300749c059be2fbece87d4b36395e842de5ef170c45f89b15e.jpg)

![](images/8b3ea06e30a76de5a99cac73e5ada2debe3fe02c96ec59538d27db01b9c72c89.jpg)

time efficiency, and energy efficiency associated with QUBO computations within each annealing iteration (Fig. 3e, f), our approach markedly achieves significant improvements across various aspects, including problem-solving scale, time efficiency, and solution quality. Yet, the capability of all the CiM SA solver relies not only on the algorithm, but also the precision of the hardware especially when

mapping the QUBO matrix. Figure S8 demonstrates the impact of the QUBO matrix precision in solving the prime factorization problem (PFP), as an example. A single MESA epoch of solving the PFP is studied. As expected, the higher the precision of QUBO matrix, the higher the success rates of MESA in finding the solution. This is because higher mapping precision yields a more accurate representation of the

Fig. 4 | Demonstration of a new simulated annealing algorithm and its hardware acceleration using FeFET CiM array. a Proposed multi-epoch simulated annealing (MESA) algorithm for solving complex COPs. b Results of 30 Max-Cut problems demonstrate that MESA outperforms conventional SA in the quality of solution. c A toy example of graph coloring for hardware implementation, which consists of 7 nodes and 3 colors to paint. After compression, it requires a ternary CiM array of 16 × 15 to map. d When mapped to a FeFET CiM array, the measured array current is linearly proportional to the theoretical xT Qy value, demonstrating

the feasibility of performing MESA in hardware. e The ternary matrix Q corresponding to the toy graph coloring problem in (c). f Using 2 FeFETs to represent each ternary Q matrix element, the programmed FeFET $V _ { \mathrm { T H } }$ map of the corresponding 32 × 15 array. g The corresponding cell current. h The theoretical energy as a function of annealing iteration. i Experimentally measured energy as a function of annealing iteration, showing successful operation of the hardware in implementing the annealing algorithm.

Table 1 | Summary of QUBO Solvers   

<table><tr><td>Reference</td><td>41</td><td>50</td><td>51</td><td>52</td><td>42</td><td>This work</td></tr><tr><td>Problem</td><td>Max-Cut</td><td>Max-Cut</td><td>Spin Glass</td><td>Graph Partion</td><td>Traveling Salesman</td><td>Graph Coloring/Max-Cut/Prime Factorization</td></tr><tr><td>QUBO matrix compression</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>method</td><td>SA</td><td>Chaotic SA</td><td>SA</td><td>SA</td><td>Multi-step SA</td><td>MESA</td></tr><tr><td>Hardware implementation</td><td>memristor based crossbar</td><td>memristor based crossbar</td><td>RRAM based crossbar</td><td>RRAM based crossbar</td><td>RRAM based crossbar</td><td>FeFET based crossbar*</td></tr><tr><td>Hardware acceleration*</td><td>VM</td><td>VM</td><td>VM</td><td>VM</td><td>VM</td><td>VMV</td></tr><tr><td>Hardware size</td><td>60×60</td><td>2×2</td><td>11×3</td><td>64×64</td><td>1024×1152</td><td>32×32</td></tr><tr><td>Problem size</td><td>60 node</td><td>5 node</td><td>15 node</td><td>6 node</td><td>100 node</td><td>21 node</td></tr></table>

⋆: VM denotes vector-matrix multiplication, VMV denots vector-matrix-vector multiplication.   
† : The first one known to us.

energy landscape, as shown in Fig. S9, which however incurs more hardware costs in terms of analog-digital-converter and array size.

To demonstrate the capability of developed FeFET CiM array in accelerating COPs, a toy example of graph coloring, as shown in Fig. 4c, is evaluated. To fit the problem into the developed 32 × 32 FeFET array, the example consists 7 nodes and 3 colors to be assigned. The initial QUBO formulation prior to compression necessitates an 21 × 21 array (i.e., each node can be any of the three color, thus total 21 input variables, per the QUBO conversion described in Sec. 1 of Supplementary Information), whereas the compressed formulation can be implemented on an 16 × 15 array, resulting in a notable 1.84 × reduction in chip size. In this example, the matrix Q is ternary (i.e., has value of 0, 1, 2). For experimental demonstration, 2 FeFETs are used to represent each matrix element. Three FeFET CiM array dies (see Fig. 2c for the chip photo) have been employed to evaluate the QUBO formulation. The capability of the chip in realizing the intended xT Qy computation is demonstrated in Fig. 4d, where the measured array total current shows a linear dependence on the theoretical xT Qy value. Building upon this capability, MESA is performed on the chip. Figure 4e shows the ternary Q matrix corresponding to the graph coloring problem in Fig. 4c. The corresponding 32 × 15 FeFET array is then programmed. Figure 4f, g show the $V _ { \mathrm { T H } }$ and measured cell current, respectively, demonstrating successful mapping of the matrix Q.

Figure 4h and i show the theoretical energy and experimentally measured energy evolution with annealing iterations. The experimental measurements are conducted on 3 separate dies. Figure 4i shows 9 separate measurements on one of the die, where for each measurement, the FeFET CiM array is erased and programmed again with the same QUBO matrix, and MESA is executed. All of the measured curves consistently align with the theoretical curve, validating the capability and robustness of the proposed FeFET CiM systems in performing MESA to solve COPs. More experimental measurement results can be found in Fig. S10. Figure S11 showcases the graph coloring configurations during annealing, highlighted at different iteration steps shown in Fig. 4i, i.e., the beginning (A), midpoint (B), and end (C) of the evolution process. Initially, errors such as multiple colors attributed to a single node, identical colors assigned to adjacent nodes, or uncolored nodes could occur, which correspond to high QUBO energy states like point A and B. In these cases, the algorithm is

still exploring the solution space with the constraints loosely enforced. As annealing proceeds, the proposed approach can ultimately find the optimal solution with all the constraints satisfied.

# Discussion

We proposed a comprehensive hardware-algorithm co-design framework for solving the complex COPs efficiently. The proposed approach comprises a FeFET-based CiM array that accelerates the critical in-situ VMV multiplications within the QUBO formulation. Additionally, the proposed QUBO matrix compression technique significantly improves the chip utilization, thereby enhancing the problem solving capability of the hardware when addressing larger COPs. Complementing this, our multi-epoch based SA algorithm optimizes the proposed solver’s ability to converge and reach optimal solutions within a shorter time period. Both the simulation and experimental measurements on fabricated prototypes validate the problem-solving capability of the proposed approach. The solver summary in Table 1 demonstrates that the proposed framework can outperform solvers for COPs commonly showcased in prior works by leveraging the VMV acceleration and QUBO compression techniques. Remarkably, the proposed framework showcases robust COP-solving capability and exhibits wide applicability to a broad spectrum of COPS that can be transformed to QUBO formulation. Importantly, our framework has the potential for broad adoption across various NVM based crossbars beyond FeFET devices. Moreover, our framework can accommodate various types of COPs with even larger scales than the size of FeFET CiM chip, as illustrated in Sec. 1 and Sec. 8 of Supplementary Information. This adaptability positions our approach as a universal and highly efficient method for QUBO computation and solving COPs using three-terminal voltage-driven structures.

# Methods

# FeFET chip integration

Testing chip is designed with FeFETs integrated on 28nm high-κ metal gate (HKMG) platform. The fabricated ferroelectric field effect transistor (FeFET) features a poly-crystalline Si/TiN (2 nm)/doped $\mathsf { H f O } _ { 2 }$ (8 nm)/SiO2 (1 nm)/p-Si gate stack. The ferroelectric gate stack process module starts with growth of a thin $\mathrm { S i O } _ { 2 }$ based interfacial layer, followed by the deposition of an 8 nm thick doped HfO2. A TiN metal gate electrode was deposited using physical vapor deposition (PVD), on top

of which the poly-Si gate electrode is deposited. The source and drain n+ regions were obtained by phosphorous ion implantation, which were then activated by a rapid thermal annealing (RTA) at approximately 1000∘ C. This step also results in the formation of the ferroelectric orthorhombic phase within the doped HfO2.

# FeFET chip electrical characterization

The measurements primarily utilize a PXIe measurement system provided by National Instruments. A padring comprising 28 individual analog and digital pads establishes connections between the 1kb (32 × 32) FeFET macro and a serial peripheral interface (SPI). The adapter board interfaces with specific pads on the wafer using a probecard within a wafer probe system. The setup includes distinct NI PXIe-4143 source measure units (SMU) and an NI PXIe-6570 pattern generator. Notably, the output pins of the latter device can function as a Pin Parametric Measurement Unit (PPMU). This configuration facilitates the generation of necessary supply, bias voltages, and digital signals. Moreover, the pattern generator plays a crucial role in configuring the scan chain for the proper addressing of wordlines and sourceline/drainline.

# Data availability

The data that support the findings of this study are available in Zenodo with the https://doi.org/10.5281/zenodo.10697395. [https://doi.org/10. 5281/zenodo.10697394]. Other data related to this study are available from the corresponding author.

# Code availability

The code that support the findings of this study are available in Zenodo with the https://doi.org/10.5281/zenodo.10697395. [https://doi.org/10. 5281/zenodo.10697394].

# References

1. Yu, G. Industrial applications of combinatorial optimization, vol. 16 (Springer Science & Business Media, 2013).   
2. Paschos, V. T. Applications of combinatorial optimization, vol. 3 (John Wiley & Sons, 2014).   
3. Naseri, G. & Koffas, M. A. Application of combinatorial optimization strategies in synthetic biology. Nat. Commun. 11, 2446 (2020).   
4. Barahona, F., Grötschel, M., Jünger, M. & Reinelt, G. An application of combinatorial optimization to statistical physics and circuit layout design. Oper. Res. 36, 493–513 (1988).   
5. Markov, I. L. Limits on fundamental limits to computation. Nature 512, 147–154 (2014).   
6. Markov, I. L. Know your limits (review of” limits to parallel computation: p-completeness theory”; greenlaw, r., et al. 1995) [book review]. IEEE Des. Test. 30, 78–83 (2013).   
7. Greenlaw, R., Hoover, H. J. & Ruzzo, W. L. Limits to parallel computation: P-completeness theory (Oxford University Press on Demand, 1995).   
8. Lucas, A. Ising formulations of many np problems. Front. Phys. 2, 5 (2014).   
9. Mohseni, N., McMahon, P. L. & Byrnes, T. Ising machines as hardware solvers of combinatorial optimization problems. Nat. Rev. Phys. 4, 363–379 (2022).   
10. Date, P., Arthur, D. & Pusey-Nazzaro, L. Qubo formulations for training machine learning models. Sci. Rep. 11, 10029 (2021).   
11. Zaman, M., Tanahashi, K. & Tanaka, S. Pyqubo: Python library for mapping combinatorial optimization problems to qubo form. IEEE Trans. Computers 71, 838–850 (2021).   
12. Glover, F. et al. Quantum bridge analytics I: a tutorial on formulating and using QUBO models. Ann. Oper. Res. 314, 141–183 (2022).   
13. Glover, F., Kochenberger, G., Hennig, R. & Du, Y. Quantum bridge analytics i: a tutorial on formulating and using qubo models. Ann. Oper. Res. 314, 141–183 (2022).

14. Yamamoto, K. et al. STATICA: A 512-Spin 0.25M-Weight Annealing Processor With an All-Spin-Updates-at-Once Architecture for Combinatorial Optimization With Complete Spin–Spin Interactions. In IEEE Journal of Solid-State Circuits. 56, 165–178 (2021).   
15. Katsuki, K., Shin, D., Onizawa, N. & Hanyu, T. Fast solving complete 2000-node optimization using stochastic-computing simulated annealing. In 2022 29th IEEE International Conference on Electronics, Circuits and Systems (ICECS), 1–4 (IEEE, 2022).   
16. Onizawa, N., Kuroki, K., Shin D., & Hanyu, T. Local Energy Distribution Based Hyperparameter Determination for Stochastic Simulated Annealing. In IEEE Open Journal of Signal Processing 4, 452–461 (2023).   
17. Takemoto, T. et al. A 144kb annealing system composed of 9 × 16kb annealing processor chips with scalable chip-to-chip connections for large-scale combinatorial optimization problems. In 2021 IEEE International Solid-State Circuits Conference (ISSCC), vol. 64, 64–66 (IEEE, 2021).   
18. Moy, W. et al. A 1968-node coupled ring oscillator circuit for combinatorial optimization problem solving. Nat. Electron. 5, 310–317 (2022).   
19. Ahmed, I., Chiu, P.-W., Moy, W. & Kim, C. H. A probabilistic compute fabric based on coupled ring oscillators for solving combinatorial optimization problems. IEEE J. Solid-State Circuits 56, 2870–2880 (2021).   
20. Dutta, S. et al. An ising hamiltonian solver based on coupled stochastic phase-transition nano-oscillators. Nat. Electron. 4, 502–512 (2021).   
21. Roychowdhury, J. Bistable latch ising machines. In Unconventional Computation and Natural Computation: 19th International Conference, UCNC 2021, Espoo, Finland, October 18–22, 2021, Proceedings 19, Vol. 12984, 131–148 (Springer, 2021).   
22. Mallick, A. et al. Cmos-compatible ising machines built using bistable latches coupled through ferroelectric transistor arrays. Sci. Rep. 13, 1515 (2023).   
23. Afoakwa, R., Zhang, Y., Vengalam, U. K. R., Ignjatovic, Z. & Huang, M. Brim: bistable resistively-coupled ising machine. In 2021 IEEE International Symposium on High-Performance Computer Architecture (HPCA), 749–760 (IEEE, 2021).   
24. Pierangeli, D., Marcucci, G. & Conti, C. Large-scale photonic ising machine by spatial light modulation. Phys. Rev. Lett. 122, 213902 (2019).   
25. Honjo, T. et al. 100,000-spin coherent ising machine. Sci. Adv. 7, eabh0952 (2021).   
26. Yamamoto, Y., Leleu, T., Ganguli, S. & Mabuchi, H. Coherent ising machines—quantum optics and neural network perspectives. Appl. Phys. Lett. 117, 160501 (2020).   
27. McMahon, P. L. et al. A fully programmable 100-spin coherent ising machine with all-to-all connections. Science 354, 614–617 (2016).   
28. Böhm, F., Verschaffelt, G. & Van der Sande, G. A poor man’s coherent ising machine based on opto-electronic feedback systems for solving optimization problems. Nat. Commun. 10, 3538 (2019).   
29. Hamerly, R. et al. Experimental investigation of performance differences between coherent ising machines and a quantum annealer. Sci. Adv. 5, eaau0823 (2019).   
30. Albash, T. & Lidar, D. A. Demonstration of a scaling advantage for a quantum annealer over simulated annealing. Phys. Rev. X 8, 031016 (2018).   
31. Denchev, V. S. et al. What is the computational value of finite-range tunneling? Phys. Rev. X 6, 031015 (2016).   
32. Boixo, S. et al. Computational multiqubit tunnelling in programmable quantum annealers. Nat. Commun. 7, 10327 (2016).   
33. Sebastian, A., Le Gallo, M., Khaddam-Aljameh, R. & Eleftheriou, E. Memory devices and applications for in-memory computing. Nat. Nanotechnol. 15, 529–544 (2020).

34. Schroeder, U., Park, M. H., Mikolajick, T. & Hwang, C. S. The fundamentals and applications of ferroelectric hfo2. Nat. Rev. Mater. 7, 653–669 (2022).   
35. Salahuddin, S., Ni, K. & Datta, S. The era of hyper-scaling in electronics. Nat. Electron. 1, 442–450 (2018).   
36. Nebashi, R. et al. A 171k-lut nonvolatile fpga using cu atom-switch technology in 28nm cmos. In 2020 30th International Conference on Field-Programmable Logic and Applications (FPL), 323–327 (IEEE, 2020).   
37. Banerjee, W. Challenges and applications of emerging nonvolatile memory devices. Electronics 9, 1029 (2020).   
38. Taoka, K., Misawa, N., Koshino, S., Matsui, C. & Takeuchi, K. Simulated annealing algorithm & reram device co-optimization for computation-in-memory. In 2021 IEEE International Memory Workshop (IMW), 1–4 (IEEE, 2021).   
39. Misawa, N., Taoka, K., Matsui, C. & Takeuchi, K. Domain specific reram computation-in-memory design considering bit precision and memory errors for simulated annealing. In 2022 IEEE International Symposium on Circuits and Systems (ISCAS), 3289–3293 (IEEE, 2022).   
40. Trentzsch, M. et al. A 28nm hkmg super low power embedded nvm technology based on ferroelectric fets. In 2016 IEEE International Electron Devices Meeting (IEDM), 11.5.1–11.5.4 (IEEE, 2016).   
41. Cai, F. et al. Power-efficient combinatorial optimization using intrinsic noise in memristor hopfield neural networks. Nat. Electron. 3, 409–418 (2020).   
42. Hong, M.-C. et al. In-memory annealing unit (imau): Energy-efficient (2000 tops/w) combinatorial optimizer for solving travelling salesman problem. In 2021 IEEE International Electron Devices Meeting (IEDM), 21.3.1–21.3.4 (IEEE, 2021).   
43. Beyer, S. et al. Fefet: A versatile cmos compatible device with game-changing potential. In 2020 IEEE International Memory Workshop (IMW), 1–4 (IEEE, 2020).   
44. Soliman, T. et al. Ultra-low power flexible precision fefet based analog in-memory computing. In 2020 IEEE International Electron Devices Meeting (IEDM), 29.2.1–29.2.4 (IEEE, 2020).   
45. Saito, D. et al. Analog in-memory computing in fefet-based 1t1r array for edge ai applications. In 2021 Symposium on VLSI Technology, 1–2 (IEEE, 2021).   
46. Ni, K., Li, X., Smith, J. A., Jerry, M. & Datta, S. Write disturb in ferroelectric fets and its implication for 1t-fefet and memory arrays. IEEE Electron Device Lett. 39, 1656–1659 (2018).   
47. Mulaosmanovic, H. et al. Switching kinetics in nanoscale hafnium oxide based ferroelectric field-effect transistors. ACS Appl. Mater. interfaces 9, 3792–3798 (2017).   
48. CMU graph coloring dataset. https://mat.tepper.cmu.edu/COLOR/ instances.html.   
49. Stanford Max-Cut dataset. https://web.stanford.edu/~yyye/yyye/ Gset/.   
50. Yang, K. et al. Transiently chaotic simulated annealing based on intrinsic nonlinearity of memristors for efficient solution of optimization problems. Sci. Adv. 6, eaba9901 (2020).   
51. Shin, J. H., Jeong, Y. J., Zidan, M. A., Wang, Q. & Lu, W. D. Hardware acceleration of simulated annealing of spin glass by rram crossbar

array. In 2018 IEEE International Electron Devices Meeting (IEDM), 3.3.1–3.3.4 (IEEE, 2018).   
52. Mahmoodi, M. et al. An analog neuro-optimizer with adaptable annealing based on 64 × 64 0t1r crossbar circuit. In 2019 IEEE International Electron Devices Meeting (IEDM), 14.7.1–14.7.4 (IEEE, 2019).

# Acknowledgements

No external funding is received to support this research.

# Author contributions

X.Y., T.K. and K.N. proposed and supervised the project. M.G., A.V., F.M., N.L. and T.K. designed the chip and performed the experimental verification of the proposed design. Y.Q., Z.S. and C.Z. conducted SPICE simulations and verification. Z.Z., Z.J., Y.S. and X.G. helped with data analysis. All authors contributed to write up of the manuscript.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-024-46640-x.

Correspondence and requests for materials should be addressed to Cheng Zhuo, Thomas Kämpfe or Kai Ni.

Peer review information Nature Communications thanks Xueqing Li, and the other, anonymous, reviewer for their contribution to the peer review of this work. A peer review file is available.

Reprints and permissions information is available at http://www.nature.com/reprints

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/ licenses/by/4.0/.

© The Author(s) 2024