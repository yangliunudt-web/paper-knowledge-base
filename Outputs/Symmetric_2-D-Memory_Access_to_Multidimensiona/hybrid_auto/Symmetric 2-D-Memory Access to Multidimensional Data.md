---
title: "Symmetric 2-D-Memory Access to Multidimensional Data"
authors:
  - "Sumitha George"
  - "Xueqing Li"
  - "Minli Julie Liao"
  - "Kaisheng Ma"
  - "Srivatsa Srinivasa D"
  - "Karthik Mohan"
  - "Ahmedullah Aziz"
  - "John Sampson"
  - "Sumeet Kumar Gupta"
  - "Vijaykrishnan Narayanan"
date: "2018-02-23"
year: "2018"
journal: "IEEE Transactions on Computers"
abstract: "In this paper, we propose a novel memory architecture with the capability of single-cycle\"
abstract_cn: "本文提出一种具有单周期行/列访问能力的新型存储器架构。该架构非常适合在多维空间局部性特征的工作负载，这是许多矩阵和数组操作的典型特征。我们详细描述了实现所提出架构的电路设计技术，以及基于铁电晶体管的新兴存储器技术在此设计中的可行性。与标准一维访问的铁电晶体管存储器相比，所提出的二维读取存储器在32位列读写中实现了5%的能耗节省，二维读写存储器实现了93%的能耗节省。此外，二维读取存储器和二维读写存储器分别获得了约11%和95%的延迟节省。应用分析表明，在256×256矩阵操作中，二维读取存储器平均减少了约86%的行缓冲事务，且未增加阵列面积；二维读写存储器与一维铁电晶体管存储器相比，行缓冲事务减少87%，阵列面积增加28.5%。"
keywords:
  - "[[2‑D memory]]"
  - "[[Ferroelectric FET]]"
  - "[[Non‑volatile memory]]"
  - "[[Energy efficiency]]"
cite: "[1] George S, Li X, Liao M J, et al. Symmetric 2‑D‑memory access to multidimensional\"
aiSum: "基于铁电晶体管的新型二维存储器架构实现单周期行/列访问，在256×256矩阵操作中减少86%行缓冲事务，能耗降低5%~93%，延迟减少11%~95%。"
confidence: "medium"
wiki_concepts:
  - "[[FeFET]]"
---

# Symmetric 2-D-Memory Access to Multidimensional Data

Sumitha George , Student Member, IEEE, Xueqing Li , Member, IEEE, Minli Julie Liao, Kaisheng Ma, Srivatsa Srinivasa D , Student Member, IEEE, Karthik Mohan, Ahmedullah Aziz, Student Member, IEEE, John Sampson, Member, IEEE, Sumeet Kumar Gupta, Member, IEEE, and Vijaykrishnan Narayanan, Fellow, IEEE

Abstract— In this paper, we propose a novel memory architecture with the capability of single-cycle row-wise/column-wise accesses. Such an architecture is highly suitable for workloads featuring spatial locality in multiple dimensions, which is a characteristic of many matrix and array operations. We describe in detail the circuit design techniques enabling the proposed architectures, as well as the viability of emerging memory technologies based on ferroelectric transistors (FEFETs) for our design. Compared to FEFET memory with standard 1-D access, we achieve 5% energy savings for the proposed memory featuring 2-D read and 93% energy savings for memory with 2-D read and write, for 32 bit column read and write. In addition, we get around 11% and 95% delay savings for 2-D read-enabled memory and 2-D read-write memory, respectively. The application analysis shows that 2-D read-enabled memory achieves around 86% average decrease in row-buffer transactions in 256 × 256 size matrix operations without any array area increase. The 2-D read write memory offers 87% decrease in rowbuffer transactions with 28.5% increase in array area compared to the 1-D FEFET memory.

Index Terms— 2-D memories, big data analytics, ferroelectric FET (FEFET), nonvolatile memory (NVM), nonvolatility.

# I. INTRODUCTION

R ECENT developments in the field of science and tech-nology lend urgency to innovate in methods to tackle nology lend urgency to innovate in methods to tackle large amount of data and information. For example, it is now common to deal with an enormous amount of both raw and

Manuscript received July 18, 2017; revised December 15, 2017; accepted January 18, 2018. Date of publication February 23, 2018; date of current version May 22, 2018. This work was supported in part by GRC under Grant 2657.001; in part by the Center for Low Energy Systems Technology, one of the six SRC STARnet Centers, sponsored by MARCO and DARPA; and in part by the National Science Foundation Expeditions in Computing Program: Visual Cortex on Silicon CCF 1317560. The work of K. Ma was supported by NSF ASSIST. (Corresponding authors: Xueqing Li; Vijaykrishnan Narayanan.)

S. George, M. J. Liao, K. Ma, S. Srinivasa, K. Mohan, J. Sampson, and V. Narayanan are with the School of Electrical Engineering and Computer Science, Pennsylvania State University, State College, PA 16802 USA (e-mail: sug241@psu.edu; mjl5868@psu.edu; kxm505@psu.edu; sxr5403@psu.edu; kmm7041@psu.edu; sampson@cse.psu.edu; vijay@cse.psu.edu).

X. Li was with the School of Electrical Engineering and Computer Science, Pennsylvania State University, State College, PA 16802 USA. He is now with the Department of Electronic Engineering, Tsinghua University, Beijing 100084, China (e-mail: xueqingli@tsinghua.edu.cn).

A. Aziz and S. K. Gupta were with Pennsylvania State University, State College, PA 16802 USA. They are now with the School of Electrical and Computer Engineering, Purdue University, West Lafayette, IN 47907 USA (e-mail: aziz5@psu.edu; guptask@purdue.edu).

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/TVLSI.2018.2801302

structured data in the fields of autonomous navigation [1], video streaming, Internet of Things (IoT), machine learning, etc. The collective growth of these fields demands schemes for organizing and manipulating data faster and more effectively. Indeed, the field of big data analytics has arisen to deal specifically with challenges associated with rapid growth of data [2]. Rising demand has generated many industrial software platforms that aim to handle big data, and the growth of these software platforms puts pressure on the underlying hardware to deal with data in real time at line rate and offline in a manner that scales with collected data.

In addition to the quantity of memory used in these applications, the organization, both logical and physical, of data within the memory hierarchy plays a key role in determining the performance of a system. The impacts of physical placement are well studied due to the long-observed divergent technology-driven growth rates between the speed of processing elements and the latency of accessing memory elements [3]. However, logical organization of data can also play a key role in performance due to either enabling or impeding the application of various optimizations. One challenge in traditional memory organizations, like DRAMs, is that fetch is limited by row-adjacency for a single operation/cycle. This makes the overall data latency a function of access patterns and the locality of the data. In conventional systems, the best performance is obtained for access patterns with addresses located in row-contiguous memory locations. However, many applications, especially vision applications, frequently generate sequences of data requests that belong to different rows in the memory and are therefore less efficient. Existing approaches to mitigate pattern-based access inefficiency include prefetching [4] and incorporating scatter-gather mechanisms [5] using additional buffer registers and prediction techniques. Prefetching is limited by both prediction accuracy and the bandwidth impacts of over fetch, while scatter-gather logic is limited by the complexity of the required logic.

Prior approaches have considered modifying the fundamental memory cell designs in order to support more complicated access patterns. With additional transistors per cell [6], an SRAM array can be read in the vertical direction, but cannot be written. However, this further exacerbates the already limited density of SRAM. In contrast, a number of emerging nonvolatile memory (NVM) technologies, such as magnetic tunnel junctions (MTJs), resistive random-access memories (ReRAMs), and ferroelectric RAMs (FeRAMs),

![](images/ef87441ad48b3811d6caee878110459b7baa9bca2d600dda61c341683e4a343b.jpg)  
Fig. 1. (a) Horizontal rowwise data transfer in traditional memory array. (b) Vertical columnwise data transfer in memory array.

offer higher density, low leakage, and, if deployed as crosspoint arrays, synergize strongly with multidimensional access patterns. However, each has unique challenges for implanting efficient on-chip memories. Spin torque devices like MTJs [7], [8] offer a promising path for NVMs achieving high density and endurance, albeit with challenges associated with low distinguishability. ReRAMs have a larger, but still limited, resistance ratio and suffer from lower endurance [9]. Some of the other technologies, such as FERAM, have a destructive read process, forcing the need of a write back with every read [10].

We therefore propose a new memory architecture for onchip scratchpads built upon ferroelectric transistors (FEFETs) that can overcome the data transfer inefficiency of traditional row access memories by adding an additional direction of access to the memory bank. FEFET is an emerging memory technology having high distinguishability in the read, low operating voltages and nondestructive read [11] making it a good choice for our memory implementation. Fig. 1 shows our proposed architecture. We call the memory, which can provide single-cycle access to either a row [Fig. 1(a)] or a column [Fig. 1(b)] of data, a 2-D memory. Having two data access directions is beneficial for applications with spatial locality in both the row and column directions. This includes many scientific and streaming applications. For example, in the case of matrix multiplication, getting data in the columnwise direction from the multiplier matrix can effectively reduce the latency of performing each inner product operation, many scanning algorithms require columnwise data, and bookkeeping applications frequently feature both category and entryaligned access patterns. Augmenting the memory hardware with an additional access direction can reduce memory layout constraints, reduce fundamental operation latency on multialigned data, and reduce the bandwidth costs of over fetch, when the requested data is not equally dense in all dimensions. In our design, we get the flexibility of mapping the array elements to both row and column. In case of an N-dimensional array, we get the choice to map the fastest changing dimension to either row or column, compared to the traditional mapping where the mapping is restricted to either column major store or row major store across the design. Our contributions in this paper include the following:

1) proposal of a 2-D memory supporting both read and write in vertical and horizontal directions;   
2) identification and verification of an emerging technology (FEFET) suitable for building the 2-D memory;   
3) extensive analysis at the cell, layout, and array levels to quantify the benefits and trade-offs associated with the proposed design;   
4) identification of scenarios where the new memory scheme helps to boost the performance;   
5) evaluation of the impact of the proposed memory on algebraic applications showing improvements in a row-buffer activity.

The remainder of this paper is organized as follows. First, we discuss motivation and background briefly. Subsequent sections describe technology and implementation details of the proposed memory. The last section covers various performance and application analyses of the proposed memory organization and techniques.

# II. MOTIVATION AND BACKGROUND

In this section, we briefly discuss 2-D access memory and investigate the need for the same. Vision applications, database management and scientific applications, are some of the potential benefactors of such a system. For example, vision application kernels (e.g., Sobel edge detection) traverse in vertical and horizontal directions [15], which can speed up the target detection with 2-D memories. One of the major applications in bookkeeping is storing the details of the people according to categories. For example, in a class of 100 students, a record of each student is entered with that student’s name and the scores in various subjects. If we want to pick the scores of a student for all the subjects, we need rowwise fetch. If we want to fetch the scores of students according to a particular subject, we need the columnwise access. For such applications, 2-D memory gives the flexibility to pick the required data in a single cycle by either performing a row or column access. This in turn usually helps to reduce the memory access time, saving significant time and energy.

Furthermore, there are many applications that require column fetch at bit-level granularity. For example, in an application, which needs to fetch only the most significant bit (MSB) of all the words, traditional memory would access all the words rowwise and then only utilize the MSB from each. On the other hand, 2-D memory with columnwise data fetching capability will obviate the need for word-level transactions. Also, we need only one cycle of operation to fetch an entire column of MSBs. Such cases are very common in real-world applications where we need bits from certain positions of the word. Such examples include determination of the sign of the number (MSB needed), UNIX file permissions, error correction code manipulations, etc.

In order to utilize the concept of physical locality for two access directions, we have to ensure two conditions:

1) alignment of data in sync with logical row or column— which can be ensured by the memory controller;   
2) presence of columnwise vertical data transfer mechanism;

3) bit reorganization of words in the physical layout for facilitating single-cycle word accesses both in row and column directions.

In this paper, we discuss in detail about data transfer mechanisms along the vertical direction and investigate an emerging technology for potential designing of the same. In addition, we should consider that, with unique attributes and challenges in each emerging NVM technology, significant effort is directed toward improving the material, device, and circuit aspects of these technologies [12]. For example, the capability to introduce logic in memory can improve the overall performance of the system. Recently, Yin et al. [13] showed that the hysteresis properties of FEFET could be used to implement the logic in memory. Moving compute closer to memory implicates that the memory and logic technology should be process compatible. If we have a technology, which can be used both as memory and logic, it obviates the intricacies arising from compatibility issues. In this context, FEFET, an inherent steep slope transistor [14], can be changed to memory by changing the device parameters, thereby eliminating the compatibility issues for the co-existing memory and logic in the same chip. One other feature that is shared among several of the new memories is high degree of symmetry in the physical structure of rows and columns within memory mats. Interestingly, this feature can be utilized to improve the memory performance using the concept of 2-D memory. We show that physical symmetry in FEFET storage can translate to better gain in memory transfer efficiency. In addition, it is CMOS compatible making it a practical choice for integrating memories on-chip [16], [17]. The potential to build logic in memory using FEFET [13] in tandem with 2-D memory technologies opens up a huge exploration space in computing and memory, which compels us to look into details of FEFET technology. Also, it has to be noted that the proposed technique may be extended to other emerging technologies, especially crosspoint memory technologies with additional circuit tweaks. In order to understand the unique features of FEFET-based memories that enable a 2-D memory architecture, we provide a brief overview about FEFET operation in Section III.

# III. PROPOSED FEFET-BASED MEMORY ARCHITECTURES

Technology scaling has led to innovations to overcome the limits of traditional transistors. One of the leading efforts in that direction has led to the concept of Ferroelectric FETs. The uniqueness of this device arises from the presence of a ferroelectric (FE) layer in the gate-stack of the transistor. The FE layer acts as a voltage amplifier at the gate due to the negative capacitance of the FE, making the transistor a steep switching device suitable for ultralow power applications [14]. These transistors optimized toward a steep switching slope that can also be used for logic applications, known as negative capacitance FETs. These devices have been explored as suitable candidates for nonvolatile memory by utilizing the FE layer’s capability to retain polarization in the absence of voltage biases. The direction of polarization is used to denote logic high or low.

While the FEFET memory in [18] employs voltages of positive and negative polarities for write, with proper design,

![](images/6e1ec1827d1242fcc18667466cb1f4c651d4dfee3b1eb449554192315be64943.jpg)  
(a)

![](images/5584565f01f88b5c65ca1206d76ff23a32f4f8a9bcdba56c031bc10353058a85.jpg)  
(b)

![](images/e46620d1e8faba7183a783610e879f4a210ecdd1fafc497dbcf54ed4c98c6f7e.jpg)  
Fig. 2. (a) FEFET device. (b) Cross section of FEFET [11].   
(a)

![](images/dfdeaa28ae30d42c76235b2757bd5c445a46b1a2932c6931d87c76947e290ab7.jpg)  
(b)

![](images/a99297c035c91f4e7bd423356b6dc38ab609588f1c7babd5639ae59dc567f914.jpg)  
Fig. 3. Memory write of $\mathrm { ( a ) \ ^ { 6 } 1 ^ { 9 } }$ and $( \mathrm { b } ) \ ^ { 6 } 0 . ^ { 7 }$   
(a)

![](images/3387548574d441532dc78af74e26655e4904454293965c80bda8a0a541f0c404.jpg)  
  
Fig. 4. FeFET device feature. (a) $I _ { d } - V _ { g }$ of a typical FEFET sample. (b) Reading $I _ { d }$ of an FEFET.

the use of negative voltage can be averted in the array. In this paper, we focus on an array design requiring positive voltages only. Moreover, we exploit the structural symmetry of the FEFET in the proposed memory cell to make it suitable for 2-D memory access. To explain this more elaborately, we present the schematic of the FEFET in Fig. 2 [11]. Here, we see that, due to structural symmetry, the source and drain can interchange their roles. This attribute can be utilized for the 2-D memory design, as explained in subsequent sections.

In the proposed memory array, a bit $" 1 "$ is written into FEFET by applying a positive voltage at its gate and a complimentary zero write voltage at the source, as shown in Fig 3(a). This changes the direction of polarization in the positive direction. A bit $ { { } ^ { 6 } } 0 ^ { 9 }$ is stored by applying the positive pulse at source and zero write voltage at gate, thereby changing the polarization in the negative direction. The embedded MOSFET in an FEFET is either in an ON or OFF state due to its interaction with the FE layer polarization. This leads to differences in channel resistance. Drain current shows six orders of difference in magnitude between the positive and negative polarization states [14], [18], as shown in Fig. 4(a). As shown in Fig. 4(b), stored data of polarization state can thus be read by sensing the amount of drain–source current $I _ { \mathrm { r e a d } }$ or the impact of $I _ { \mathrm { r e a d } }$ (such as increased sense line voltage toward $V _ { \mathrm { R e a d } } )$ . The FEFET memory hysteresis window width

![](images/04b39581d39f65819fea96e298f73809d3ca6f97f87dfe0aabbf51df4822147e.jpg)  
(a)

![](images/06862811d5bfb514d7494102d8cca86c125596e1a4de332d80e021e7fdd450c0.jpg)

![](images/da199a2cadf5a839a346f346604009fb86febb18483e9745d28e69c5aff1c321.jpg)  
Fig. 5. Proposed 4T FEFET-based cell in read. (a) Rowwise. (b) Columnwise.   
Fig. 6. Proposed 4T FEFET-based memory array: the columnwise read.

could be increased by making the stacked ferroelectric layer thicker [14], [18], [19].

In this paper, we propose two types of memory arrays. One is built with 4T per cell, supporting rowwise write, and 2-D read. The other one is built with 5T per cell, supporting both write and read in 2-Ds. We will discuss about their operation mechanisms subsequently.

A. Proposed 4T Memory Array for 1-D Write and 2-D Read

At the single memory cell level, the 4T schematic is shown in Fig. 5, consisting of three vertical lines, three horizontal lines, and four transistors. While the biasing shown in Fig. 5 is only for read operations, the 4T scheme supports 1-D write and 2-D read. Read Select, Bit Line, and Sense Line are placed vertically, while Read line, Gate Select, and Sense Select are placed horizontally.

For the read access, the two MOSFET transistors connecting to FEFET drain and source ports are turned on, and the other MOSFET access transistor connecting to the FEFET gate is turned on to keep the FEFET gate at GND. As can be observed, neglecting the gate bias portion of the scheme, the other parts of FEFET drain and source access circuitry is fully symmetric, making the read access in the vertical and horizontal directions conceptually the same. In detailed implementations, a higher-than-zero read voltage, $V _ { \mathrm { R e a d } }$ , can be applied to Read line for rowwise read, or Sense Line for columnwise read. After the drain and source access transistors, S1and S3, are turned on, the Sense Line in Fig. 5(a) and the

TABLE I BIASING THE PROPOSED 4T ARRAY TO WRITE/READ ROW0 (ROW MODE)   

<table><tr><td>Name</td><td colspan="2">Read Select</td><td colspan="2">Gate Select</td><td colspan="2">Sense Select</td></tr><tr><td>Column Index</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td>Write “0”</td><td>GND</td><td>GND</td><td>VDD</td><td>GND</td><td>VDD</td><td>GND</td></tr><tr><td>Write “1”</td><td>GND</td><td>GND</td><td>VDD</td><td>GND</td><td>VDD</td><td>GND</td></tr><tr><td>Read</td><td>VDD</td><td>VDD</td><td>VDD</td><td>GND</td><td>VDD</td><td>GND</td></tr><tr><td>Hold row</td><td colspan="6">GND</td></tr><tr><td>Name</td><td colspan="2">Bit Line</td><td colspan="2">Sense Line</td><td colspan="2">Read Line</td></tr><tr><td>Column Index</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td>Write “0”</td><td>GND</td><td>GND</td><td>VDD</td><td>VDD</td><td colspan="2">GND</td></tr><tr><td>Write “1”</td><td>VDD</td><td>VDD</td><td>GND</td><td>GND</td><td colspan="2">GND</td></tr><tr><td>Read</td><td>GND</td><td>GND</td><td>Float ing</td><td>Floating</td><td colspan="2">VRad</td></tr><tr><td>Hold row</td><td colspan="6">GND</td></tr></table>

![](images/f7e366285df04e6973ff541bdf31688055ecfd072cbe9175a54917d3366c9fad.jpg)  
Fig. 7. Proposed fully symmetric 2-D read-write FEFET-based memory array in a 2 2 structure.

Read line in Fig. 5(b) can be pulled up toward $V _ { \mathrm { R e a d } }$ if the FEFET has a low resistance state, or stay as they are otherwise. Therefore, this enables voltage-mode read. Fig. 6 shows an example of columnwise read of the cells in the first column in a $2 \times 2$ array. If current-mode read is preferred in some scenarios, such as very big arrays, the current at the output line [Sense Line in Fig. 5(a) and Read line in Fig. 5(b)] can be sensed.

For the write access, only rowwise write is supported in the proposed 4T topology. In this rowwise write mode, all Read line and Read Select are grounded. Bit Line and Sense Line are set either low or high in voltage as needed to achieve the desired FEFET $V _ { \mathrm { G S } } { \mathrm { : } }$ VDD for positive polarization and –VDD for negative polarizations. For rows not to be accessed, Gate Select and Sense Select are grounded to isolate FEFET from Bit Line and Sense Line, respectively. For the accessed row,

![](images/5ab4199de53d66692384c9e28a5a6059f9e2aaebb171498fe08ad52da2fdd3af.jpg)  
(a)

![](images/1363cb91bbd0202ef74d6de93f61d3bc44f7ec848e1ba8b4a8e933a16c38fb74.jpg)  
(b)   
Fig. 8. (a) 2-D read-write memory transient waveforms; row mode read-write; polarization changes in the positive direction (storage of 1) by the application of $V _ { \mathrm { W r i t e } }$ at Bit Row Line and zero voltage in the sense line (during write 1 period in the figure), leading to high current I (Read) at sense line, when $V _ { \mathrm { R e a d } }$ is applied in Read line (Read 1 period in the figure). (b) Similarly, polarization changes in the negative direction with $V _ { \mathrm { W r i t e } }$ at sense line and zero voltage at Bit Row Line, leading to low current, when $V _ { \mathrm { R e a d } }$ is applied in Read line; column mode operation; polarization changes in the positive direction by the application of $V _ { \mathrm { W r i t e } }$ at Bit Col Line and zero voltage in the Read line (during write 1 period), leading to high current I (Read) at Read line, when $V _ { \mathrm { R e a d } }$ is applied in sense line (Read 1 period in the figure). Similarly, polarization changes in the negative direction with $V _ { \mathrm { W r i t e } }$ at Read line and zero voltage at Bit Col Line, leading to low current at Read line, when $V _ { \mathrm { R e a d } }$ is applied in sense line.

TABLE II BIASING THE PROPOSED 4T ARRAY TO READ COLUMN 0   

<table><tr><td>Name</td><td colspan="2">Read Select</td><td colspan="2">Gate Select</td><td colspan="2">Sense Select</td></tr><tr><td>Row Index</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td>Read</td><td>VDD</td><td>GND</td><td colspan="2">VDD</td><td colspan="2">VDD</td></tr><tr><td>Name</td><td colspan="2">Bit Line</td><td colspan="2">Sense Line</td><td colspan="2">Read Line</td></tr><tr><td>Row Index</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td>Read</td><td colspan="2">GND</td><td colspan="2">VRead</td><td>Floating</td><td>Floating</td></tr></table>

Gate Select and Sense Select are turned on to set the gate voltage and source voltage, respectively.

The biasing scheme for the idle state hold, reading from and writing to Row 0, is shown in Table I. Columnwise read biasing is shown in Table II.

# B. Proposed 5T Memory Array for 2-D Read and Write

As mentioned above, the symmetry of the read current flowing path makes it possible to reverse the direction of read current flowing to enable read in both columnwise and rowwise. This insight can be harnessed to add one extra access transistor to the FEFET gate, leading to a physically fully diagonally symmetric memory array. Fig. 7 shows an example array of $2 \times 2$ such cells, and Fig. 8 provides examples of transient simulation waveforms.

For read access in this array, a biasing scheme similar to the 4T topology can be adopted, while ensuring a single

![](images/c6f6f5f36f1d0d8812d0da310eeab0d306e1482dbf6b0abf0bcbdc4e1899d36b.jpg)  
Fig. 9. Basing conditions and activated metal lines to write to Row 0 (Row 0 shown in red dotted lines) of 2-D read-write array.

row/column FEFET gate access transistor is turned on. For write access, Figs. 9 and 10 show the signaling of rowwise write access and columnwise write access, respectively. Due to the physical symmetry, the biasing settings for rowwise and columnwise accesses are also symmetric. Table III shows the detailed biasing settings for read and write operations.

# IV. MEMORY ORGANIZATION AND PERIPHERAL CIRCUITRY

This section discusses the peripheral circuitry required to access the 2-D memory array for both read and write. We especially discuss the Bit Line read sensing scheme.

TABLE III BIASING CONDITIONS TO READ AND WRITE ROW 0/COLUMN 0 OF SYMMETRIC 2-D MEMORY   

<table><tr><td>Read/Write 
Row</td><td>Gate Sel 
R0</td><td>Gate Sel 
R1</td><td>Bit Row 
Line0/1</td><td>Sense 
Line0/1</td><td>Drain Sel 
0/1</td><td>Gate Sel C 
0/1</td><td>Bit Col Line 
0/1</td><td>Read 
Line0</td><td>Read Line1</td><td>Source 
Sel0</td><td>Source Sel1</td></tr><tr><td>Write 0</td><td>VDD</td><td>GND</td><td>GND</td><td>VDD</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>VDD</td><td>GND</td></tr><tr><td>Write 1</td><td>VDD</td><td>GND</td><td>VDD</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>VDD</td><td>GND</td></tr><tr><td>Read</td><td>VDD</td><td>GND</td><td>GND</td><td>Floating</td><td>VDD</td><td>GND</td><td>GND</td><td>VRead</td><td>GND</td><td>VDD</td><td>GND</td></tr><tr><td>Hold</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td></tr><tr><td>Read/Write 
Col</td><td>Gate Sel 
C0</td><td>Gate Sel 
C1</td><td>Bit Row 
Line0/1</td><td>Sense Line0</td><td>Sense Line1</td><td>Drain Sel0</td><td>Gate Sel R0/1</td><td>Drain 
Sel1</td><td>Bit Col 
Line0/1</td><td>Read Line 
0/1</td><td>Source 
Sel0/1</td></tr><tr><td>Write 0</td><td>VDD</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>VDD</td><td>GND</td><td>GND</td><td>GND</td><td>VDD</td><td>GND</td></tr><tr><td>Write 1</td><td>VDD</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>VDD</td><td>GND</td><td>GND</td><td>VDD</td><td>GND</td><td>GND</td></tr><tr><td>Read</td><td>VDD</td><td>GND</td><td>GND</td><td>VRead</td><td>GND</td><td>VDD</td><td>GND</td><td>GND</td><td>GND</td><td>Floating</td><td>VDD</td></tr><tr><td>Hold</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td><td>GND</td></tr></table>

![](images/7cc8638c91ffa13601c37e959fc146ffbe3f99b1e0d2d8df01b776e9d338ceb0.jpg)  
Fig. 10. Biasing conditions and activated metal lines for writing to column 0 in 2-D read-write memory array.

![](images/6fd0a312f575d0395067ebd89da004ef5af4c69080ee1892b542f68501b4e427.jpg)  
Fig. 11. 2-D-memory organization with peripheral circuitry.

Considering that the memory array is symmetric, the decoder and sensing circuitry are needed for columnwise and rowwise accesses.

Fig. 11 shows the read and write access scheme, where we have a second array of sensing, driving, and decoder. The switching block in Fig. 11 enables the array to sense the data in column/row mode. It receives the signal from the memory

![](images/d8ac28719fb6bee1165b04a3b7f6c302841e336f249b72b7194aec6e51a72cbf.jpg)  
Fig. 12. Bit arrangement of the 2-D memory.

controller and enables the multiplexers either to connect driver circuitry or sensor circuitry to the respective Read/Sense Line of the FEFET array in Fig. 11.

We get column-level access in bit-level granularity by the virtue of the device structure and arrangement mentioned in the previous sections. However, in order to achieve a column level word fetch in a single cycle, we need to have a bit plane arrangement of words. This arrangement can be done in multiple ways. For example, suppose we have eight words $( \operatorname { A } , \operatorname { B } , \operatorname { C } , \dots , \operatorname { G } , \operatorname { H } )$ , each having 8 bits (A: A0, A1, A2, . . . , A7, B: B0, B1, B2, . . . , B7, . . . , H: H0, H1, H2, . . . , H7). Without the bit plane arrangement, typical bit arrangement in a physical row is Row 1: A0, A1, A2, . . . , A7; B0, B1, $\mathrm { B } 2 , \ldots , \mathrm { \bf ~ B } 7 ; \ldots ; \mathrm { \bf ~ H 0 } ,$ , H1, H2, . . . , H7. In order to achieve a single-cycle row/column fetch, we rearrange bits to 8 bit groups consisting of (A0, B0, C0, . . . , H0), (A1, B1, C1, . . . , $\mathrm { H 1 ) , \ldots , \ ( A 7 , ~ B 7 , ~ C 7 , \ldots , ~ H 7 ) }$ and store in the physical row (in other words, store bits intermittently from each word) in the array such as Row 1: A0, B0, C0, . . . , H0; A1, B1, C1, . . . , H1; . . . ; A7, B7, C7, . . . , H7; We connect the output from each of the groups (A,B,..,H) to the vertical and horizontal buffers in the periphery maintaining the original order [(A0, A1, A2 . . . A7), (B0, B1, B2, . . . , B7), . . . , (H0, H1, H2. . .H7)] with the help of wires. This representation is shown in Fig.12.

Another possible arrangement is having eight different arrays for each of the 8 bit groups. In such a way, all the first bits of the words (MSBs) are in one array, and the second bit of the words will be in the second array, and so on. With proper buffer arrangement, parallel read and write operations

![](images/2b9e8d3581ce9e7ef159536de9f49029a21db85c8db6af5a4a866d61ee88bb22.jpg)  
(a)

![](images/28cb72979219bd5a245b0a5d91f122b421c9c087a2cb3ab184bf2b6061cf3b37.jpg)  
(b)   
Fig. 13. (a) Write voltage to write delay characteristics of FEFET cell having an FEFET layer thickness of 9.1 nm. (b) Write voltage to write energy trend.

TABLE IV SIMULATION PARAMETERS   

<table><tr><td>Technology node</td><td>10nm</td></tr><tr><td>Number of fins</td><td>1</td></tr><tr><td>α</td><td>-1.05e9 m/F</td></tr><tr><td>β</td><td>1e7 m5/F/coul2</td></tr><tr><td>γ</td><td>6e11 m9/F/coul4</td></tr><tr><td>ρ</td><td>0.1Ω·m</td></tr><tr><td>Write Voltage (Vwrite)</td><td>0.5V</td></tr><tr><td>Read Voltage (Vread)</td><td>0.3V</td></tr></table>

can be done so that all the bits of the same word are found written to or collected from the right location.

Memory controllers with traditional DRAM systems use a RowBankRankChannelColumn scheme to increase the parallelism by interleaving to reduce the memory latency. In our scheme, we use the ChannelRankBankRowColumn to constrain the column to be in the same physical bank. In addition, we did our evaluation with single channel and single rank to evaluate the merit of our system excluding the effect from interleaving. However, in order to increase the parallelism and to take advantage of the physical row column, the address scheme needs to be slightly changed. In this case, we need to make the basic unit for interleaving tiles with a certain number of rows and columns, so that within that tile we get single-cycle column or row access. Then, we interleave the tiles across BankRankChannel to increase the parallelism and thereby decreasing latency while making use of a single-cycle row–column access. The size of the tile and the optimum interleaving policy are the subject for future study.

# V. PERFORMANCE ANALYSIS

We analyze the performance of different circuit topologies described in Sections III-A–III-C using the model based on the time-dependent L-K equation coupled with 10-nm predictive technology Model [20] for FEFETs [19]. The parameters used for the analysis are given in Table IV. The array level analysis is done for 32 32 cells. We choose the array width to be 32 as it is common to have a 32-bit wide word size in the processors. The objective of our analysis is to get insights into situations, where the column access can save the energy and delay. For fixed circuit parameters, we have compared energy —delay for both read and write in the array and is given in Table V. The parameters are chosen based on the analysis given in Fig. 13. Fig. 13(a) shows the trend of voltage versus write delay for a fixed FEFET thickness of 9.1 nm, which is

![](images/fff217b7e4433e3dcc20f931d2c18a805db43ac4ac9aebdb6447442f7f413c12.jpg)  
Fig. 14. Write noise margin for different thicknesses of the ferroelectric layer (TFE) for a 4T FEFET cell. With an input write voltage of 0.5 V and a TFE of 9.1 nm, the write noise margin is around 0.2 V. The input voltage is applied to the Bit Line, and complimentary voltage is applied to sense line (Fig. 5) for this simulation.

sufficient to maintain the nonvolatility in the circuit. We see that if we decrease the voltage below 0.5 V, the write delay increases as it approaches the energy barrier for reversing the polarization. The trend in energy decrease with respect to decrease in voltage is gradual and is expected. Therefore, we chose our write voltage to be fixed at 0.5 V so that we get a reasonable delay and power. Then we fixed the read voltage, such that the read voltage will not upset the stored bits. The Select lines are given as boosted voltage for the entire write voltage to appear at the FEFET gate and source.

Also, we can further extend the device circuit design space by optimizing the ferroelectric layer thickness for nonvolatility and bias voltages for minimum energy and delay in the future work. For these emerging memories, write and read margin mainly depends on the technology and read write mechanisms. We define the write noise margin of a memory cell as the voltage difference between the minimum write voltage required to write to the cell (flip the polarization of the FE layer) and the write voltage we use in the design. In the FEFET memory, the amount of voltage needed to flip the bits depends on the FEFET polarization hysteresis width. The width of the hysteresis depends on the underlying thickness of the ferroelectric layer. In Fig. 14, we show the hysteresis characteristics when the input voltage is applied to the Bit Line and complimentary voltage to the Sense Line (Maximum sweep voltage—-applied voltage at Bit Line). In our design, with a write voltage of 0.5 V and the ferroelectric layer thickness of ∼ 9 nm, we get around 0.2 V as the write noise margin. In the case of read voltage, the margin can be defined as difference between the read voltage and the required amount of voltage to upset the bits. The chosen read voltage is 0.3 V. The read disturbance voltage at the read terminal (drain of FEFETs) should be at least 0.484 V to change the FEFET memory state, based on our experiments. This indicates a read noise margin around 0.184 V.

We observe from Table V that for the 2-D read memory (4T FEFET), the read energy is slightly more for column read compared to row read. This is due to the fact that while reading in the column mode, we need to turn on the multiple Gate Select lines that span across the column (in Fig. 6 Gate Select 1) to ensure the stability. However, the effect of column energy saving comes from the access pattern. For example,

TABLE V ENERGY-DELAY PERFORMANCE   

<table><tr><td></td><td>Proposed 4T Row-wise only</td><td>Proposed 4T Column-wise</td><td>Proposed 5T row- and column-wise</td></tr><tr><td>Write Energy(J)</td><td>1.58e-12</td><td>1.58e-12</td><td>1.76e-12</td></tr><tr><td>Write Delay(s)</td><td>1.81e-09</td><td>1.81e-09</td><td>2.93e-09</td></tr><tr><td>Read Energy(J)</td><td>8.59e-14</td><td>1.23e-13</td><td>1.76e-12</td></tr><tr><td>Read Delay(s)</td><td>240e-12</td><td>240e-12</td><td>380e-12</td></tr><tr><td>Transistor # /cell</td><td>4</td><td>4</td><td>5</td></tr></table>

if the access pattern requires reading a word in the column direction (32 bits), the read energy required by the traditional access would be $( 3 2 \times 8 . 5 9 \mathrm { e } ^ { - 1 4 } = 2 . 7 4 \mathrm { p J } )$ greater than singlecolumn access energy of the 4T 2-D read memory (0.12 pJ) saving around 95%. We could safely argue that the 4T column will be a win if the read accesses are skewed toward column.

For the 2-D read-write (5T) architecture, write and read energies are slightly greater than 2-D read (4T) architecture. We observe that if there are more accesses in the column direction, having full 2-D read-write memory is advantageous from timing and energy perspectives. For example, if we have two writes in the column direction, 1-D memory will consume $2 { * } 1 . 5 8 ~ \mathrm { p J } = 3 . 1 6 ~ \mathrm { p J }$ . For the same, 2-D memory needs only 1.76 pJ leading to 44 % savings in energy. Suppose we have 32 writes in the same column $( 3 2 * 1 . 5 8 \mathrm { p J } = 5 0 . 5 6 \mathrm { p J } )$ , then the energy savings are as high as 96% compared to 1-D memory writes. However, in the case we have only 16-bit column reads, the energy is 28% more (1.37 pJ) compared to 1-D 4T memory (1.76 pJ). For a 32-bit column read and 32-bit column write, we get around 5% energy savings for 2-D Read (4T) and 93% energy savings for 2-D read write (5T) compared to 1-D (53.3 pJ) memory in the array level. On the delay front in the array, we get around 11% savings for 2-D Read (4T) and 95% savings for 2-D read write (5T) compared to 1-D memory (65.6 ns). This opens up an exploration space for choosing optimum array configuration based on the application specific access pattern. In the standby mode, we can shut off the power supply to the memory as FEFET, a nonvolatile memory, can retain the stored state, eliminating the leakage power.

# VI. LAYOUT ANALYSIS

It is critical to evaluate the layout design and consider layout strategies to minimize the cell area and use minimal routing resources. The $2 \times 2$ layout array is depicted in Fig. 15. The vertical dimension of the layout is a function of the Metal 2 pitch, and the lateral dimension is a function of the poly pitch. In both the designs, select signals and Read line require four independent parallel routes running across the cell. The 1-D memory and 2-D memory layouts are optimized independently for the minimal optimum area with proper diffusion sharing. We have the FEFET sandwiched between C2 and C3 (Fig. 5) in both the designs, which is denoted by the dotted circle in Fig. 15. With the same number of horizontal tracks, Fig. 15(b) is larger to Fig. 15(a) only by an additional metal 2 pitch, which translates to 28.5% increase in the area in the bit-cell array.

![](images/42ab4f383da5d7e6efbf49d4bda5df5f715605e7db31b6f7f50f8e2ed5b465f0.jpg)

![](images/0aa73e7a762965e912a4a9d57de40af6231c297efd57815a5fea631107b17d59.jpg)  
(a)   
(b)   
Fig. 15. Layout of proposed FEFET-based memory arrays in a $. 2 \times 2$ structure. (a) Proposed 4T/cell design. (b) Proposed 5T/cell design.

We have shown the layouts of 1-D 4T FEFET cell $( 2 \times 2 )$ and the 2-D 5T FEFET $( 2 \times 2 )$ cell. The 28.5% area increase is due to the additional one transistor and two metal routings in the 2-D 5T cell compared to 1-D 4T cell. The percentage increase (28.5%) will remain unchanged even if we scale the array size from 32×32 to 256×256. The layout is drawn using the lambda-based design rules. A lambda is a half-minimum feature length. These rules are widely adopted in design rule checks [23]. The layout comparison assists in understanding the additional routing resources needed and the area penalty for read-write memory. In the case of peripheral circuitry, we encounter another 1% increase in the total area, as we need a second set of sense amplifiers and drivers in the columnwise. This area evaluation is based on the recently reported data that typical current sense amplifier area amounts less than 1% of the total macro area [22].

# VII. APPLICATION ANALYSIS

In many of the data analytics and IoT applications, we deal with a large amount of data. For example, accelerators in IoT devices are designed to handle high overload of data. While in a data analysis workload, 80% of data analysis is spent on the process of cleaning and preparing the data [21] in which matrix operations play a prominent role. Matrix operations are basic components of most scientific applications, and the matrix multiplication and transpose operations shown in our application set can contribute to general purpose computing [25] and many digital signal-processing applications [26].

In this section we analyze commonly used matrix operations to evaluate the impact of the proposed 2-D memory. The array

![](images/438457c303ac7645a2e89e2714d5af88f198fe630ad1af4b80b2130c848f53ad.jpg)  
Fig. 16. Normalized row/column buffer activations per application for 1-D/2-D read-enabled memory/2-D read-write memory. The maximum number of buffer accesses per application is also indicated.

operations contain multiple read write accesses. The rot 90, fliplrmat mux, and norm1 are MATLAB matrix operations. Rot 90 operation rotates a matrix counterclockwise by 90°. This involves reading the matrix in columnwise and writing the elements rowwise. Fliplr returns a matrix with column flipped about a vertical axis. The access pattern involves reading a matrix column and writing into a matrix columnwise. Matmux does matrix multiplication by taking a column from matrix A and taking a row from another matrix B. Norm1 computes the matrix column sum, and the access pattern involves reading the matrix columnwise [24]. Transpose is one of the very basic matrix operations used in multiple applications such as linear algebraic operations, fast Fourier transforms, etc. The transpose operation interchanges the contents of the memory locations by the row–column indices. The process is usually performed by accessing the contents of the array rowwise and storing the same in columnwise. In our proposed memory, this process becomes much easier as both the read and write operations can be completed in one cycle each. We can accommodate this process in one cycle for each of the row or column operation with the 2-D enabled read-only memory and also by choosing to read the data columnwise and writing the same in rowwise.

In Fig. 16, we calculate statistics of the row–column buffer openings. The memory access time can be obtained by multiplying the row/column access times with the number of buffer openings. Array energy consumption is also a function of buffer transactions as moving array elements to the peripheral circuits is an expensive operation. We observe from Fig. 16 that we get significant reduction (87%) in the number of buffer transactions. The access pattern and the statistics are obtained from the GEM5-NVMain [27] modeling of our system. We use 256 256 size matrices as inputs. We use the first-come first-serve memory controller on 1GB Memory for our simulations. For an open page row/column buffer policy, to access consecutive column elements, we need only one column access if the data are accessed in column mode from a 2-D memory due to the presence of separate column buffer. However, if we access a column of data from a 1-D memory, we need to open the row buffer multiple times. The number of row accesses required is the number of rows in the column as the physical mapping is same as that of the logical mapping.

We observe from Fig. 16 that, on average, for array operations such as transpose, rot90, filplr, matrix multiplications,

and norm1, the 4T 2-D read memory offers 86% improvement on buffer activations, whereas a full 2-D 5T memory offers 87% improvement in buffer operations over 1-D memory. The increase in savings for full 2-D memory over 2-D read-only memory can be attributed to the ability to write columnwise in some of the matrix operations. For example, the filplr application without any compiler modification requires to read and write the matrix in columnwise direction. As a result, it gives an edge to the 2-D read-write memory over 2-D enabled read-only memory as column write saves delay “N” folds where N is the column size of the matrix. Additionally, we need to note that, in fact, the proposed 2-D full read-write memory eliminates the need for a transpose operation in the conventional sense as the transposed application can directly access the memory locations by changing the row-column indices in the code.

Note that the 86% improvement in the 2-D read memory (4T) compared to 1-D memory is achieved without extra transistors in the array. However, one other set of peripheral circuitries is required as explained in Section IV. Nonetheless, typically the core area is much bigger than the peripheral circuit area, as a result of which the benefits of the proposed memory outweigh the need for extra peripheral circuits. The 87% improvement in buffer transactions for 2-D read-write memory (5T) over 1-D memory is achieved with a 28.5% area increase in the array area.

# VIII. CONCLUSION

We propose a memory array using the emerging FEFET technology, which is capable of performing read and write along the rows as well as columns. We discuss the design in detail at the bit-cell and array level. We choose ferroelectric layer thickness 9.1 nm to retain the nonvolatility in the memory and supply voltage 0.5 V to optimize the energy delay. The first design we propose (2-D read-enabled memory) has the capability to read data in both horizontal and vertical directions. The second design (2-D read- write memory) can read and write data in both vertical and horizontal directions. For a 32-bit column read and write, we achieve 5% energy savings with 2-D read-enabled memory and 93% energy savings with 2-D read-write memory, compared to FEFET memory with standard 1-D access in the array. In addition, we get around 11% delay savings for 2-D read-enabled and 95%delay savings for 2-D read-write memories. For 256×256 size matrix operation, on average, the 2-D read-enabled memory and 2-D read-write memory reduce row-buffer transactions by 86% and 87% respectively. The array area increase penalty of the 2-D read-write memory with respect to 1-D FEFET memory is 28.5%

# REFERENCES

[1] A. Ess, K. Schindler, B. Leibe, and L. Van Gool, “Object detection and tracking for autonomous navigation in dynamic environments,” Int. J. Robot. Res., vol. 29, no. 14, pp. 1707–1725, 2010.   
[2] X. Wu, X. Zhu, G.-Q. Wu, and W. Ding, “Data mining with big data,” IEEE Trans. Knowl. Data Eng., vol. 26, no. 1, pp. 97–107, Jan. 2014.   
[3] W. A. Wulf and S. A. McKee, “Hitting the memory wall: Implications of the obvious,” ACM SIGARCH Comput. Archit. News, vol. 23, no. 1, pp. 20–24, Mar. 1995.

[4] T. C. Mowry, M. S. Lam, and A. Gupta, “Design and evaluation of a compiler algorithm for prefetching,” ACM SIGPLAN Notices, vol. 27, no. 9, pp. 62–73, 1992.   
[5] How Does Scatter/Gather Work? Accessed: Feb. 9, 2018. [Online]. Available: https://www.eejournal.com/article/20170209-scatter-gather/   
[6] K. Bong, S. Choi, C. Kim, S. Kang, Y. Kim, and H.-J. Yoo, “A 0.62 mW ultra-low-power convolutional-neural-network face-recognition processor and a CIS integrated with always-on Haar-like face detector,” in Proc. ISSCC, 2017, pp. 248–249.   
[7] C. W. Smullen, V. Mohan, A. Nigam, S. Gurumurthi, and M. R. Stan, “Relaxing non-volatility for fast and energy-efficient STT-RAM caches,” in Proc. IEEE 17th Int. Symp. High Perform. Comput. Archit. (HPCA), Feb. 2011, pp. 50–61.   
[8] W. Xu, H. Sun, X. Wang, Y. Chen, and T. Zhang, “Design of lastlevel on-chip cache using spin-torque transfer RAM (STT RAM),” IEEE Trans. Very Large Scale Integr. (VLSI) Syst., vol. 19, no. 3, pp. 483–493, Mar. 2011.   
[9] M. F. Chang et al., “A high-speed 7.2-ns read-write random access 4-Mb embedded resistive RAM (ReRAM) macro using processvariation-tolerant current-mode read schemes,” IEEE J. Solid-State Circuits, vol. 48, no. 3, pp. 878–891, Mar. 2013.   
[10] R. Bez and A. Pirovano, “Non-volatile memory technologies: Emerging concepts and new materials,” Mater. Sci. Semicond. Process., vol. 7, nos. 4–6, pp. 349–355, 2004.   
[11] D. Wang, S. George, A. Aziz, S. Datta, V. Narayanan, and S. K. Gupta, “Ferroelectric transistor based non-volatile flip-flop,” in Proc. Int. Symp. Low Power Electron. Design, 2016, pp. 10–15.   
[12] J. S. Meena, S. M. Sze, U. Chand, and T.-Y. Tseng, “Overview of emerging nonvolatile memory technologies,” Nanosc. Res. Lett., vol. 9, no. 1, p. 526, 2014.   
[13] X. Yin et al., “Exploiting ferroelectric FETs for low-power non-volatile logic-in-memory circuits,” in Proc. IEEE/ACM Int. Conf. Comput.-Aided Design (ICCAD), Nov. 2016, pp. 1–8.   
[14] A. I. Khan, C. W. Yeung, C. Hu, and S. Salahuddin, “Ferroelectric negative capacitance MOSFET: Capacitance tuning & antiferroelectric operation,” in IEDM Tech. Dig., Dec. 2011, pp. 11.3.1–11.3.4.   
[15] K. Ogawa, Y. Ito, and K. Nakano, “Efficient Canny edge detection using a GPU,” in Proc. 1st Int. Conf. Netw. Comput. (ICNC), 2010, pp. 279–280.   
[16] M. H. Lee et al., “Steep slope and near non-hysteresis of FETs with antiferroelectric-like HfZrO for low-power electronics,” IEEE Electron Device Lett., vol. 36, no. 4, pp. 294–296, Apr. 2015.   
[17] K.-S. Li et al., “Sub-60 mV-swing negative-capacitance FinFET without hysteresis,” in IEDM Tech. Dig., Dec. 2015, pp. 22.6.1–22.6.4.   
[18] S. George et al., “Nonvolatile memory design based on ferroelectric FETs,” in Proc. 53rd ACM/EDAC/IEEE Design Autom. Conf., Jun. 2016, pp. 1–6.   
[19] A. Aziz, S. Ghosh, S. Dutta, and S. K. Gupta, “Physics-based circuitcompatible SPICE model for ferroelectric transistors,” IEEE Electron Device Lett., vol. 37, no. 6, pp. 805–808, Jun. 2016.   
[20] Predictive Technology Model (PTM). Accessed: Feb. 9, 2018. [Online]. Available: http://ptm.asu.edu/   
[21] H. Cherupalli, H. Duwe, W. Ye, R. Kumar, and J. Sartori, “Determining application-specific peak power and energy requirements for ultra-low power processors,” in Proc. 22nd Int. Conf. Archit. Support Program. Lang. Oper. Syst., 2017, pp. 3–16.   
[22] C.-P. Lo et al., “Embedded 2 Mb ReRAM macro with 2.6 ns read access time using dynamic-trip-point-mismatch sampling current-mode sense amplifier for IoE applications,” in Proc. Symp. VLSI Circuits, Jun. 2017, pp. C164–C165.   
[23] MOSIS Scalable CMOS (SCMOS). Accessed: Feb. 9, 2018. [Online]. Available: https://www.mosis.com/files/scmos/scmos.pdf   
[24] Matrix 1-Norm. Accessed: Feb. 9, 2018. [Online]. Available: https://www.mathworks.com/help/dsp/ref/matrix1norm.html   
[25] S. Huss-Lederman, E. M. Jacobson, J. R. Johnson, A. Tsao, and T. Turnbull, “Implementation of Strassen’s algorithm for matrix multiplication,” in Proc. ACM/IEEE Conf. Supercomput., Jan. 1996, p. 32.   
[26] R. Prasad and A. Mihovska, New Horizons in Mobile and Wireless Communications: Radio Interfaces, vol. 1. Norwood, MA, USA: Artech House, 2009, p. 105.   
[27] M. Poremba and Y. Xie, “NVMain: An architectural-level main memory simulator for emerging non-volatile memories,” in Proc. IEEE Comput. Soc. Annu. Symp. VLSI (ISVLSI), Aug. 2012, pp. 392–397.

![](images/64ff1e8568cf4f06958cef55b441c6170ce1469ad621a8f67863da8cc6864241.jpg)

Sumitha George (S’17) received the B.Tech. degree in electronics and communication from the University of Kerala, Kerala, India and the M.Tech. degree from IIT Delhi, New Delhi, India. She is currently working towards the Ph.D. degree in computer science and engineering at Pennsylvania State University, State College, PA, USA.

She was with the Systems and Technology Group, IBM, Bengaluru, India, where she was involved in microprocessor physical design. Her current research interests include device–circuit design and computer architecture.

![](images/a5424f36f1f16c443e2cda71fc3bff85bd1c462bcc19cdbf1244451d0448f186.jpg)

Xueqing Li (M’13) received the B.S. and Ph.D. degrees from Tsinghua University, Beijing, China.

He was a Postdoctoral Research Associate with the Department of Computer Science and Engineering, Pennsylvania State University, State College, PA, USA, from 2013 to 2017. He is currently an Assistant Professor with the Department of Electronic Engineering, Tsinghua University. He has authored or coauthored over 50 journal and conference papers. His current research interests include high-performance CMOS data converters

and emerging circuits and systems, including energy harvesting, low-voltage digital logic, nonvolatile memory and processing architectures using emerging devices, such as tunnel FETs, ferroelectric negative-capacitance FETs, and phase-transition FETs.

Dr. Li was a recipient of the 2015 HPCA Best Paper Award, the 2016 IEEE Micro Top Picks Award, the 2017 ASP-DAC Best Paper Award, the 2017 IEEE Transactions MSCS Best Paper Award, and the 2017 SRC/STARnet LEAST Center Best Publication Award.

![](images/97baf29678389910558c99afde273c64df07b57078dfef72f56a3b3a31d4dc43.jpg)

Minli Julie Liao received the B.S. degree in electronic information engineering from the Harbin Institute of Technology, Harbin, China. She is currently working toward the Ph.D. degree at the Department of Computer Science and Engineering, Pennsylvania State University, State College, PA, USA.

Her current research interests include computer architecture and power efficient systems.

![](images/fa7a55be5a2d494a57a18f5bcff675ec06df7f4db0f9b33bfe1871da6b3f697d.jpg)

Kaisheng Ma received the B.S. degree (honors) in electrical engineering from Hangzhou Electronic University, Zhejiang, China and the M.S. degree from the Institute of Microelectronic, Peking University, Beijing, China. He is currently working toward the Ph.D. degree at the Department of Computer Science and Engineering, Pennsylvania State University, State College, PA, USA.

His current research interests include nonvolatile processor architecture, machine learning, big data, neural networks, and neuromorphic computing.

![](images/574dc39b5f89bdcce07262083e4349700a7be449f76f2340bcf401fc6e234168.jpg)

Srivatsa Srinivasa (S’16) received the B.E. degree in electronics and communication engineering from Visvesvaraya Technological University, Belgaum, India. He is currently working toward the Ph.D. degree at the Department of Computer Science and Engineering, Pennsylvania State University, State College, PA, USA.

![](images/0f3af0c826bb3b522b53e9b4c96cc3586c21b48d1373e2c38f7daa6dc543da17.jpg)

Karthik Mohan received the B.E. degree in electronics and communication engineering from Anna University, Chennai, India and the M.S. degree in engineering in computer science and engineering from Pennsylvania State University, State College, PA, USA.

![](images/c7fbdf26c3188711bc61db9ac5f3bbcbd8781634897ca44516f7a3820b0ba6e2.jpg)

Ahmedullah Aziz (S’10) received the B.Sc. degree from Bangladesh University of Engineering and Technology, Dhaka, Bangladesh and the M.S. degree from Pennsylvania State University, State College, PA, USA. He is currently working toward the Ph.D. degree at the Department of Electrical and Computer Engineering, Purdue University, West Lafayette, IN, USA.

He was an Engineer with the Samsung R&D Institute, Dhaka, and Global Foundries, Malta, NY, USA. His current research interests include device–

circuit modeling and co-design with exploratory technologies.

![](images/840805dfeb86767c426276f77150fb3407c63bf2c520faf490d91b1fd3463ea7.jpg)

John Sampson (M’04) received the Ph.D. degree from the University of California at San Diego, San Diego, CA, USA.

He is currently an Assistant Professor with the Department of Computer Science and Engineering, Pennsylvania State University, State College, PA, USA. His current research interests include energy-efficient computing, architectural adaptations to exploit emerging technologies, and mitigating the impact of dark silicon.

![](images/6fbcdade063de2c402eb66ee326da4b3b5e2e54c3542c3f3efa6f4091d54fda9.jpg)

Sumeet Kumar Gupta (M’13) received the B.Tech. degree in electrical engineering from IIT Delhi, New Delhi, India, in 2006 and the M.S. and Ph.D. degrees in electrical and computer engineering from Purdue University, West Lafayette, IN, USA, in 2008 and 2012, respectively.

He was an Assistant Professor of Electrical Engineering with Pennsylvania State University, State College, PA, USA, and a Senior Engineer with Qualcomm, San Diego, CA, USA. He is currently an Assistant Professor of Electrical and Computer

Engineering with Purdue University, West Lafayette, IN, USA. His current research interests include low-power variation aware very large-scale integration circuit design, nanoelectronics and spintronics, device–circuit co-design, and nanoscale device modeling and simulations.

![](images/00ad129120d91ba6ea7f5efad725c172cdaafaa7a42a4a12256fad079b781c8e.jpg)

Vijaykrishnan Narayanan (F’11) received the B.S. degree from the University of Madras, Chennai, India, in 1993 and the Ph.D. degree in computer science and engineering from the University of South Florida, Tampa, FL, USA, in 1998.

He is currently a Distinguished Professor with Pennsylvania State University, State College, PA, USA. His current research interests include poweraware and reliable systems, embedded systems, nanoscale devices, and interactions with system architectures, reconfigurable systems, network-on-

chips, and domain-specific computing.

Prof. Narayanan was a recipient of several awards, including the Penn State Engineering Society Outstanding Research Award in 2006, the IEEE CAS VLSI Transactions Best Paper Award in 2002, the Penn State CSE Faculty Teaching Award in 2002, the ACM Special Interest Group on Design Automation Outstanding New Faculty Award in 2000, the Upsilon Pi Epsilon Award for Academic Excellence in 1997, the IEEE Computer Society Richard E. Merwin Award in 1996, and the University of Madras First Rank in Computer Science and Engineering in 1993. He was also a recipient of several certificates of appreciation for outstanding service from ACM and the IEEE Computer Society. He is currently the Editor-in-Chief of the IEEE TRANSACTIONS ON COMPUTER-AIDED DESIGN OF INTEGRATED CIRCUITS AND SYSTEMS.