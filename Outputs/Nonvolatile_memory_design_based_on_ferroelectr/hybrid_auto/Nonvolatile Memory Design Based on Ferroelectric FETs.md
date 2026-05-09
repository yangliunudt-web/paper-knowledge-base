---
title: "Nonvolatile Memory Design Based on Ferroelectric FETs"
authors:
  - "Sumitha George"
  - "Kaisheng Ma"
  - "Xueqing Li"
  - "Ahmedullah Aziz"
  - "Sayeef Salahuddin"
  - "John Sampson"
  - "Sumeet Kumar Gupta"
  - "Vijaykrishnan Narayanan"
date: "2016-06-05"
year: "2016"
journal: "Proceedings of the ACM/IEEE Design Automation Conference"
doi: "10.1145/2897937.2898050"
abstract: "Ferroelectric FETs (FEFETs) offer intriguing possibilities for the design"
abstract_cn: "铁电场效应晶体管凭借其三端结构以及铁电材料在无电场下保持极化的能力，为低功耗非易失性存储器的设计提供了引人注目的可能性。利用铁电场效应晶体管的独特特性，我们提出了一种基于2晶体管铁电场效应晶体管的非易失性存储器，具有分离的读取和写入路径。通过在器件、单元和阵列级别的协同设计，所提出的设计实现了非破坏性读取，并在相同写入速度下相比标准铁电随机存取存储器具有更低的写入功耗。此外，基于铁电场效应晶体管的存储器表现出高区分度，两种状态对应的读取电流相差六个数量级。基于实验校准模型的比较分析显示访问能量延迟有显著改善。例如，在固定写入时间550ps下，写入电压和能量分别比铁电随机存取存储器低58.5%和67.7%。这些优势以2.4倍的面积开销实现。在能量收集非易失性处理器中进一步探索所提出的铁电场效应晶体管存储器显示，相比铁电随机存取存储器，平均前向进度提高了27%。"
keywords:
  - "[[Ferroelectric]]"
cite: "[1] George S, Ma K, Aziz A, et al. Nonvolatile memory design based on ferroelectric"
aiSum: "2T FeFET非易失存储器：利用三端结构实现分离读/写路径，非破坏性读取，相比FeRAM写入电压降低58.5%、能量降低67.7%，区分度10^6倍，能量收集非易失处理器前向进度提升27%。"
confidence: "medium"
wiki_concepts:
  - "[[Ferroelectric]]"
---

# Nonvolatile Memory Design Based on Ferroelectric FETs

Sumitha George<sup>1</sup>, Kaisheng Ma<sup>1</sup>, Ahmedullah Aziz<sup>1</sup>, Xueqing Li<sup>1</sup>, Asif Khan<sup>4</sup>, Sayeef Salahuddin<sup>4</sup>, Meng-Fan Chang<sup>2</sup>, Suman Datta<sup>3</sup>, John Sampson<sup>1</sup>, Sumeet Gupta<sup>1</sup>, Vijaykrishnan Narayanan<sup>1</sup>

$^{1}$ Pennsylvania State University, University Park, PA 16802, $^{2}$ National Tsing Hua University, Taiwan 30013

<sup>3</sup>University of Notre Dame, Notre Dame, IN 46556, <sup>4</sup>University of California, Berkeley, CA 94720

sug241@psu.edu,kxm505@psu.edu,afa5191@psu.edu,lixueq@cse.psu.edu

# ABSTRACT

Ferroelectric FETs (FEFETs) offer intriguing possibilities for the design of low power nonvolatile memories by virtue of their three-terminal structure coupled with the ability of the ferroelectric (FE) material to retain its polarization in the absence of an electric field. Utilizing the distinct features of FEFETs, we propose a 2-transistor (2T) FEFET-based nonvolatile memory with separate read and write paths. With proper co-design at the device, cell and array levels, the proposed design achieves non-destructive read and lower write power at iso-write speed compared to standard FERAM. In addition, the FEFET-based memory exhibits high distinguishability with six orders of magnitude difference in the read currents corresponding to the two states. Comparative analysis based on experimentally calibrated models shows significant improvement of access energy-delay. For example, at a fixed write time of 550ps, the write voltage and energy are $58.5\%$ and $67.7\%$ lower than FERAM, respectively. These benefits are achieved with 2.4 times the area overhead. Further exploration of the proposed FEFET memory in energy harvesting nonvolatile processors shows an average improvement of $27\%$ in forward progress over FERAM.

# Keywords

Ferroelectric FET (FEFET); NCFET; hysteresis; non-volatility; nonvolatile memory (NVM); nonvolatile processor (NVP);

# 1. INTRODUCTION

Nonvolatile memories (NVM) are being actively explored with the objectives to achieve zero stand-by leakage and high integration density, and thereby attain a large boost in the energy efficiency and storage capacity of on-chip caches for embedded applications and energy autonomous systems [1-5]. Moreover, non-volatility in storage can be useful for the design of nonvolatile processors in terms of boosting the forward progress of computation by storing the state of the system in the event of a power failure [1][4][6]. Recent research in the co-operation of NVM and architecture policies has revealed more optimization potential. Such promising attributes have led to the exploration of several nonvolatile memory technologies. However, so far, no single technology has been able to meet all the requirements needed for a robust low power memory array. Spin-based memories based on magnetic tunnel junctions [7] look promising in most aspects; however, poor distinguishability yields low sense margins. Resistive RAMs [5][19] and phase change memories [5] have high distinguishability but poor

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from Permissions@acm.org.

DAC '16, June 05-09, 2016, Austin, TX, USA

© 2016 ACM. ISBN 978-1-4503-4236-0/16/06$15.00

DOI: http://dx.doi.org/10.1145/2897937.2898050

endurance. Ferroelectric capacitor memories (FERAMs) offer high endurance, but low read stability and a destructive read operation exacerbates the read-write conflict [8]. Therefore, there is a pressing need for novel nonvolatile memory solutions to counter the limitations associated with the existing techniques.

Ferroelectric transistors (FEFETs) offer opportunities to alleviate the aforementioned problems by virtue of their distinct properties such as (a) polarization retention in the ferroelectric (FE) layer at zero electric field, (b) control of the drain current by the FE polarization and (c) low voltage switching of polarization on the application of suitable electric fields on the gate. Such unique properties allow separation of read and write paths of the memory, thereby mitigating the design conflicts. However, to exploit the benefits of FEFETs, proper device-circuit-array co-design is required. In this paper, we explore the cross-layer design of 2-transistor (2-T) FEFET memory with the objectives to (a) achieve stable and nonvolatile memory states with an enormous difference in their resistances via appropriate device optimization, (b) ensure disturb-free read operation, (c) maximize the energy efficiency by judicious cell design and (d) minimize the area penalty due to separation of read-write paths by innovative array organization.

It is important to mention that several previous works [5][9] have employed structures with separate read-write paths to optimize nonvolatile memory devices and bit-cells. For example, several multi-port spin-memories [15] offer low voltage write operation. However, in spite of read-write path separation, their distinguishability (maximum resistant ratio $\sim 7\mathrm{X}$ [15]) is not comparable to the proposed design (resistance ratio $\sim 10^6$ ). The metal ferroelectric insulator semiconductor (MFIS) transistors and FETRAM, discussed in [9][10] use the polarization stored in the gate of the transistor to overcome the destructive read issue. However, these transistors require high voltages up to $7\mathrm{V}$ for the write operation [10]. In our work the proposed FEFETs leverage the negative capacitance mechanism discussed in [11] to achieve low voltage operation. Distinct from prior work that has focused on the circuit-level implementation of a single-bit cell using FEFETs [9], this paper shows that device-circuit-array co-design is necessary to achieve optimized power-performance-area trade-offs. Note that the proposed FEFET memory is different from [10] which is designed for page-level access using a different ferroelectric device with much higher operation voltage (up to $7\mathrm{V}$ ), whereas this work supports bit-level access using supply voltages lower than $1\mathrm{V}$ . Our contributions in this paper are summarized as follows.

- We propose FEFET 2T memory with high distinguishability read disturb free operation and low read/write energy.   
- We investigate a novel array design for the proposed memory to mitigate the area penalty compared to FERAMs.   
- Based on experimentally calibrated circuit compatible models, we perform extensive analysis at the device, cell, layout and array levels to quantify the benefits and trade-offs associated with the proposed design.

We evaluate the impact of replacing FERAMs with FEFET based memories in a nonvolatile processor (NVP), and show $27\%$ forward progress improvement in low power scenarios.

# 2. BACKGROUND

![](images/7d1943751c4148b2ca3db003ff11b2c528165a50b635d8a954518247ea8bc4a8.jpg)

![](images/b5f817d6409b32a3cf6708a95bcd8cccf5694aeb43e10b02a1a07d4beb9fdcfc.jpg)

![](images/581a69dde9ef2944435fdc6345df62c33ae60f838b656b59fda2c7f4330a8d01.jpg)  
Figure 1. (a) FEFET structure; (b) transistor capacitance model; (c) PE loop of ferroelectric capacitor [12].

In this section, we briefly discuss the fundamentals of FEFETs to lay the groundwork for the rest of the paper. FEFETs are designed by adding a ferroelectric (FE) layer in the gate stack of MOSFETs as shown in Fig. 1(a) [11-12]. The unconventional charge-voltage relationship of FE materials leads to the unique device operation of FEFETs, featuring steep-switching behavior, hysteretic characteristics and non-volatility [11]. Each of these distinct properties is attainable by properly designing the devices, as discussed later. To explain the FEFET operation, let us consider a simple model shown in Fig. 1(b) with the capacitance associated with FE in series with that of the underlying MOSFET [11]. The behavior of FE is captured with time $(t)$ dependent $LK$ equation given below [12] and is illustrated in Fig. 1(c).

$$
\mathrm {E} = \alpha \mathrm {P} + \beta \mathrm {P} ^ {3} + \gamma \mathrm {P} ^ {5} + \rho \mathrm {d P} / \mathrm {d t}. \tag {1}
$$

Here, P is the polarization, E is the electric field, $\alpha$ , $\beta$ , $\gamma$ and $\rho$ are the coefficients [12][13]. It can be observed from Fig. 1(c) that there is a portion in the P-E curve where the change in polarization with respect to the electric field is negative, which leads to negative capacitance $(C_{FE} < 0)$ . Stabilizing the operation of the FE in the negative capacitance region with a positive series capacitance of the MOSFET $(C_{MOSFET})$ , achieves a voltage step-up action, which reduces the sub-threshold swing. Lowering $|C_{FE}|$ , for example, by increasing the FE thickness $(T_{FE})$ increases the voltage step-up leading to the sharper switching characteristics. At the same time, increasing $T_{FE}$ beyond a certain value introduces a hysteresis in the device characteristics, which increases as $T_{FE}$ is further increased [11]. When hysteresis spans over the positive and negative gate-to-source voltages $(V_{GS})$ , non-volatility is introduced in the device, which is the result of polarization retention in FE. While non

![](images/d05ba8811ee5021f358d0198bf1aee5b84688fe8bf1f11e9e4986e1bd53ed904.jpg)

![](images/5098a5cd5b37ecbfba2a4d4f3b157c4a3e1d13a8a323fccac9a632db6a60d2b8.jpg)  
Figure 2. 65nm N-type FEFET with 2.25nm ferroelectric layer thickness: (a) hysteresis; (b) non-volatility.

![](images/c7c908b1184ed27e8078dcd8c38978c120ff0d88edf4c4815485c3c5158dca00.jpg)

![](images/4d1a84df32206d3740811372f58ac4a6d925d264ab3c7dc6ae066ea345dee0d6.jpg)  
Figure 3. 65nm N-type FEFET with 1.90nm ferroelectric layer thickness: (a) hysteresis; (b) no non-volatility.

hysteretic FEFET operation is a subject of active research for ultra-low power logic applications [11-12][16], this paper targets FEFET operation in the nonvolatile hysteretic regime via appropriate device design, as described in the next section. To realize a robust low power nonvolatile memory array, device design must be tightly coupled with cell and array designs, as described in the subsequent sections.

# 3. NONVOLATILE FEFETS: DEVICE DESIGN AND ANALYSIS

The key to introducing non-volatility in FEFETs is to optimize the ratio of the capacitances of FE and the underlying MOSFET $(\mathrm{C_{FE} / C_{MOS}})$ to achieve the following operation. The application of positive gate-to-source voltage $(V_{GS})$ beyond a threshold must switch the polarization of FE in the positive direction and the subsequent withdrawal of $V_{GS}$ must retain the positive polarization. Similarly, negative $V_{GS}$ must switch the polarization in the negative direction, which must be retained once $V_{GS}$ is reduced to zero. This translates to the hysteresis spanning over the positive and negative $(V_{GS})$ in the transfer characteristics of FEFETs (Fig. 2(a)). Such characteristics lead to two solutions for the drain current $(I_{DS})$ at $V_{GS} = 0$ , denoted by points A and B in Fig. 2(a). We can interpret points A and B as two resistance states of the FEFET at zero $V_{GS}$ , which are the results of positive and negative polarizations of the FE layer in the gate stack. It is important to note that FEFET retains the polarization in the ferroelectric layer in the absence of $V_{GS}$ as well as drain voltage $(V_{DS})$ , which is a necessary condition for nonvolatility. Fig. 2 shows the DC and transient behavior of an FEFET with ferroelectric layer thickness of $2.25\mathrm{nm}$ and width of $65\mathrm{nm}$ . Fig. 2(a) shows the hysteresis behavior in the $I_{DS} - V_{GS}$ and Fig. 2(b) shows the polarization retention of the FEFET with time. The application of positive and negative gate voltage changes the direction of the stored polarization as shown in Fig. 2(b). The high resistance point A and low resistance point B in Fig. 2(a) are identified as logic bit 0 and logic bit 1 respectively. The stored logic state is identified by the magnitude of the $I_{DS}$ . Due to the inherent gain of the underlying transistor, the ratio of the currents corresponding to the two logic states can be as large as $10^{6}$ [16], which translates to enormous distinguishability at the cell level.

![](images/a8dcbc36ed8a9e30f8213fdb1c0d6191e3c8c185910b031d045383c8f6f56a41.jpg)

![](images/751d9448b4e8c67fd7c40a2d411bee8024cae29921e103b1330110db3c38c2f0.jpg)  
Figure 4. (a) Load line analysis with different $\mathrm{T_{FE}}$ . (b) Polarization switching voltage comparisons.

The position of the hysteresis is a crucial factor in the design of FEFETs as a nonvolatile element. For example, if we have the hysteresis only in the positive $\mathrm{V}_{\mathrm{GS}}$ region as shown in Fig. 3(a), non-volatility cannot be achieved, as the polarization falls back to zero with the removal of gate voltage. This implies that device parameters need to be designed carefully to maintain the nonvolatile functionality. In particular, the ratio $\mathrm{C}_{\mathrm{FE}} / \mathrm{C}_{\mathrm{MOS}}$ needs to be properly tuned [11] to regulate the hysteresis. We optimize the FE thickness $\mathrm{(T_{FE})}$ of FEFETs to introduce non-volatility.

![](images/5d60b8d5c6aa129a6b7ced5ce4aa64a35a90a482ec882e3b8d9370580bd5bb02.jpg)

![](images/451ab4262691305d4ad7b543b84de93bcc7dc24cf7d91975fccfdbb8550d7825.jpg)  
Figure 5. FEFET memory cell: (a) write; (b) read.

To explain the device design, we illustrate the load-line analysis in Fig. 4(a), which shows charge versus voltage for FE and the underlying MOSFET. Hysteresis is introduced in the device characteristics when there are two different points of intersection in the load line plot [12]. The hysteretic jumps in the $I_{DS} - V_{GS}$ characteristics (Fig. 2(a)) occur when the magnitudes of the positive MOSFET capacitance and negative ferroelectric capacitance become equal. With the device design corresponding to $\mathrm{T_{FE}} = 1\mathrm{nm}$ in Fig 4(a), it can be deduced that the FEFET does not exhibit hysteresis as there is only one intersection point. On the other hand, by increasing the thickness of the FE layer (Fig. 4(a)), the FE capacitance is lowered due to which the two intersection points are obtained, resulting in hysteresis. We have changed the thickness of the ferroelectric layer to shift the hysteresis position shown in Fig.2 to Fig.3. Our analysis shows that $\mathrm{T_{FE}} > 1.9\mathrm{nm}$ is required to retain the polarization in FE.

The choice of $T_{FE}$ is also dictated by the stability and power requirements of the memory device. The hysteresis must be large enough to attain sufficient noise margins required for polarization retention. At the same time, the coercive voltage or the gate voltage required for switching the polarization (which increases with increasing hysteresis) must be optimized to enable low voltage operation and achieve power savings. In an FEFET, the series combination of negative FE capacitance with positive MOSFET capacitance reduces coercive voltage compared to a stand-alone ferroelectric capacitor, as illustrated in Fig. 4(b). For example, for the ferroelectric thickness of $2.5\mathrm{nm}$ , FEFET hysteresis loop lies within the $+/-1\mathrm{V}$ whereas for stand-alone FE capacitor, the hysteresis loop extends outside the $+/-2\mathrm{V}$ range. The thickness of the ferroelectric in the capacitor may be reduced to lower the coercive voltage, albeit at the cost of leakage increase. On the other hand, FEFETs offer much lower coercive voltage even with higher FE thickness, enhancing the design flexibility. For our design, we choose $T_{FE} = 2.25\mathrm{nm}$ , which yields a hysteresis around $500\mathrm{mV}$ , leading to a balance between stability and switching voltage.

# 4. FEFET BASED MEMORY

In this section we propose a 2-T memory cell based on FEFETs. We also describe the array design utilizing the distinct features of the proposed cell. The appeal of FEFETs as memory elements relies on their polarization retention capability, high current ratio for the two states and low voltage operation, as described in the previous sections. Our memory architecture aims to exploit these advantages to improve the overall memory characteristics. The proposed 2-T cell is shown in Fig.5 and Fig.7. By virtue of the three terminal structure of FEFETs, the cell is designed to have separate read, write paths, which facilitates simultaneous optimization of the read, and write operations. The write path has a standard MOSFET as an access transistor, which is controlled by write select-line enabling selective write operation of the cells in an array. The write bit-line is shared amongst the cells in the same column. The read path consists of the FEFET with the read select connected to the drain and sense line tied to the source. The read select line is shared amongst the cells in the same row, while the sense line runs along

the column; thus, the need for a separate read access transistor is eliminated. In addition, the read select also functions as the read supply, reducing metal routing congestion. The read and write schemes are described subsequently.

# 4.1 Write

To perform the write operation, write-select line is asserted and appropriate bi-polar voltages are applied on the write bit-line to switch the FE polarization and write logics '0' and '1'. Positive write bit-line voltage $(V_{write})$ increases $V_{GS}$ of FEFET, which induces positive polarization in the FE. To reverse the polarization direction, negative bit-line voltage $(-V_{write})$ is applied. In order to order to apply sufficiently large voltage on the gate of FEFET, we boost the select line voltage. The unaccessed rows (Row 1 in Fig.7) are kept isolated by driving the corresponding write select line to negative $V_{DD}$ , which is necessary to ensure that the gate-to-source voltage of the write access transistors belonging to the unaccessed cells remain less than or equal to 0 at all times during the write operation. The read select line is driven to ground during the entire write operation. The proposed bias conditions for the write operation are summarized in Table.1.

Table 1. Bias conditions of the memory array   

<table><tr><td colspan="2"></td><td>Read select</td><td>Write select</td><td>Bit line</td><td>Sense Line</td></tr><tr><td>Accessed Row</td><td rowspan="2">Write</td><td>0</td><td>V_DD</td><td>V_write</td><td>0</td></tr><tr><td>Unaccessed Row</td><td>0</td><td>-V_DD</td><td>V_write</td><td>0</td></tr><tr><td>Accessed Row</td><td rowspan="2">Read</td><td>V_read</td><td>V_DD</td><td>0</td><td>0</td></tr><tr><td>Unaccessed Row</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>All</td><td>Hold</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

# 4.2 Read

The bit information is stored in the gate stack of an n-type FEFET. In order to tap the high magnitude difference in the drain currents corresponding to the two logic state, we have chosen current sensing for read. Note, application of fixed read voltage for current sensing also leads to the elimination of sneak current paths in the unaccessed cells of the proposed architecture. The read operation is illustrated in Fig. 5(b). The write select line is asserted and the write-bitline is driven to 0V to ensure that the gate of the FEFETs is biased in 0 volts for proper read operation. Following this, the read select voltage is asserted on the drain terminal to query the stored bits. The resulting drain current in FEFETs, the magnitude of which depends on the stored polarization, is used to sense the memory state. In order to ensure that the unaccessed cells are properly disconnected during read, the proposed scheme biases the sense line at virtual ground. This averts the development of a positive potential in the source terminal of the unaccessed FEFETs, thereby preventing the reverse current flow into the unassessed cells. Virtual ground on the sense line is achieved employing the sensing scheme which is described in Section 5. The bias voltages for the read operation are summarized in Table 1. The transient waveforms for memory read and write operations of a cell are illustrated in Fig. 6. All control lines are kept zero during the hold mode to achieve zero stand-by leakage. As read operation is based on current sensing, the read performance is strongly dependent on the sensing circuitry which we describe in the next section.

# 5. CURRENT-BASED SENSING CIRCUITS

Fig. 8(a) shows the schematic of the sensing circuit for the proposed memory, consisting of a clamping driver, a pre-charge driver, and a current sense amplifier, all enabled by the read enable signal EN. The clamping driver is used to clamp the sense line voltage, $V_{BL}$ , to a virtual ground voltage level. The pre-charge driver is used to pre-charge the sensing node voltage, $\mathrm{V}_{\mathrm{SENSE}}$ , from VSS to a predefined voltage $\mathrm{V}_{\mathrm{PRE}}$ . The current sense amplifier is used to sense the input current and generate the digitized output bit. Pre-charging and current-mode sensing with clamping drivers have been widely used

![](images/48b7a67c2b750b791c60af7158b2501d28a5dd42394a96c35f17baf79e1cbe8c.jpg)  
Figure 6. 2-T FEFET memory cell transient waveforms.

![](images/7ea12b683f7a33af8a7c24166eaaba4900af902fce88d253b7a8d16c2b1c39ef.jpg)  
Figure 7. A 2x3 FEFET memory array.

![](images/b540d5290065dfaed0920e516e96b3f7a7230792631261f25c744fbfef0d487f.jpg)

![](images/539fe525fcaab6814e3b391c1beeea4ca04324af5b8a32dd6a8c237ef055a146.jpg)  
Figure 8. FEFET memory: (a) read scheme; (b) waveforms. in nonvolatile memory read [19 -23]. Fig. 8(b) shows the read timing diagram and transient waveforms to better understand the read scheme. When read is enabled at time to, VDD is applied to the drain of the ferroelectric memory cell, and EN becomes effective and enables the clamping driver, pre-charge driver, and the current sense amplifier. The sense line voltage, $V_{BL}$ , was grounded before the onset of read, and remains at 0 volts during the read operation with the clamping driver. The instant the pre-charge driver is activated, a short and large current pulse generated by the pre-charge driver quickly charges the node between the clamping driver and the current sense amplifier, leading to a faster increasing $V_{SENSE}$ . At $t_1$ , $V_{SENSE}$ reaches the predefined voltage $V_{PRE}$ and the pre-charging pulse is disabled. The increase or decrease of $V_{SENSE}$ now depends on the current provided by the memory cell. If the cell stores logic "0", its low sensed current leads to a quick reduction of $V_{SENSE}$ , and accordingly, an output of "0" at the sense amplifier output node, $V_{SA}$ ; otherwise, logic "1" provides higher current and continues to increase $V_{SENSE}$ beyond the threshold voltage of sense amplifier, which then provides $V_{SA}$ equal to VDD. If a fast pre-charge circuit is not used, the large parasitic capacitance at the

charging node due to large-size transistors (M1 and M2 in Fig. 8(a), for less variation) will result in large charging time. Based on this read scheme, read time $t_{\text{read}}$ could be obtained:

$$
t _ {\text {r e a d}} = \max  \left\{t _ {\text {p r e}}, t _ {\text {d e c}} \right\} + t _ {s a} + t _ {\text {b u f f e r}}, \tag {2}
$$

where $t_{pre}$ , $t_{dec}$ , $t_{sa}$ , and $t_{buffer}$ represent the time required for pre-charging, decoder, sense amplifier and final output buffer to generate their output, respectively. The decoding of the read address and the pre-charging could be activated at the same time. Here, $t_{pre}$ , $t_{dec}$ , $t_{sa}$ , and $t_{buffer}$ are estimated as $0.50\mathrm{nS}$ , $0.50\mathrm{nS}$ , $1.5\mathrm{nS}$ , and $0.50\mathrm{nS}$ , respectively, leading to a total read time of $3.0\mathrm{nS}$ .

# 6. PARAMETER ANALYSIS AND COMPARISON WITH FERAM

In this section, we perform an extensive analysis of the proposed cell in terms of stability, area, retention, performance and power and draw comparison with the standard FERAMs (based on FE capacitor to store the data in terms of its polarization). In order to understand the difference between these two types of memories we briefly describe the operation of FERAM in the following section.

# 6.1 FERAM

The standard structure of an FERAM is shown in Fig.9. It contains one transistor and a ferroelectric capacitor attached to the drain of the transistor. A '1' is written into the FERAM by applying a positive voltage to the bit-line and keeping the plate line at 0V. A zero is written by applying positive voltage through the plate-line and keeping the bit line at 0V [18]. The read operation is performed by sensing the capacitive difference of the ferroelectric (FE) cap that results from positive or negative polarizations of the FE [8]. One of the possible implementations of FERAM is depicted in Fig. 9(b), in which the FE capacitor is placed in a back-end layer to reduce the cell area [8].

![](images/99d64bf75d7c78868a85a5c11162ff7edb506d8b72a621d8455da1c9bb37764b.jpg)

![](images/8d8261cbc9c75aa8f4ad10bf804b9ff7b9e07a62310811f766a02b07864a4ebe.jpg)  
Figure 9. FERAM scheme in (a) and structure in (b)[8].

# 6.2 Performance analysis

The analysis is based on time-dependent $LK$ equation for the FE calibrated to two different sets of experiments. The FE model is coupled with $45\mathrm{nm}$ high performance transistor model [14]. The simulation parameters are summarized in Table 2.

# 6.2.1 Read Stability and Performance

The proposed cell exhibits read-disturb free operation since the read and the write paths are decoupled, and the bias scheme is carefully chosen. The application of zero volts on the gate of the FEFETs and the biasing of the sense line to virtual ground during read (as explained in the previous sections) ensures that the FE polarization is not disturbed. The read current flow is isolated from the FE polarization in the gate stack of FEFET, as a result of which the memory state is not affected by the read current. The biasing of the sense lines at virtual ground also ensures that FE polarization of the unaccessed cells is not disturbed and that there is no current flow in the unaccessed cells. In contrast, read operation in FERAMs is destructive and therefore, requires write-back, which incurs performance and power overheads. The sensing circuits, described in the previous section, mainly determine the read speed of the proposed cell with current based sensing. The optimized design can achieve read speeds as high as 3.0ns at $V_{DD} = 0.68\mathrm{V}$ , by virtue of the large distinguishability (current ratio $\sim 10^6$ ) between the two logic

Table 2. Simulation parameters   

<table><tr><td>Technology node</td><td>45nm</td></tr><tr><td>Width of the transistors</td><td>65nm</td></tr><tr><td>α</td><td>-7e9 m/F</td></tr><tr><td>β</td><td>3.3e10 m5/F/coul2</td></tr><tr><td>γ</td><td>-0.2e10 m9/F/coul4</td></tr><tr><td>Metal Capacitance</td><td>0.2fF/um</td></tr><tr><td>Write Voltage (Vwrite)</td><td>0.68V</td></tr><tr><td>Read Voltage (Vread)</td><td>0.4V</td></tr></table>

states. On the other hand, FERAMs employ voltage-based sensing, the speed of which is limited by the bit-line/plate-line capacitance as well as poor capacitance difference between the logic states.

# 6.2.2 Write time and power

The operating voltage is an important consideration in memories for low power operation. Although both FERAM and FEFET store data in the form of polarization in the ferroelectric layer, the operating voltage is lower for FEFET (Fig. 4(b)), as described previously in Section 3. For the comparison in this section, we optimize the thickness of FE separately for FERAMs and the proposed FEFET-based cell. For FERAMs, the FE thickness of $1\mathrm{nm}$ leads to optimal write voltage and power. For FEFETs, FE thickness is chosen to be $2.25\mathrm{nm}$ to obtain appropriate hysteresis, considering a balance between stability and write power (see Section 3). In spite of larger FE thickness, FEFETs exhibit lower write voltage compared to FERAMs. The write access time of the FERAM and FEFET are shown in Fig. 10(a). Decreasing the voltage lower than $1.5\mathrm{V}$ for FERAM and $0.5\mathrm{V}$ for FEFET results in write failures. An iso-write time comparison of the write energy of the proposed memory with FERAM is shown in Table 3. FEFET-based cell expends $67.9\%$ lower energy compared to FERAM due to the lower write voltage. Table 3 shows the metrics of the FERAM and FEFET for the write bit cell delay around550ps. FEFET bit line voltage is $0.68\mathrm{V}$ while FERAMs need to employ much higher voltage ( $\sim 1.64\mathrm{V}$ ). Since the proposed array employs negative bit-line voltage for writing logic $^{10}$ , the voltage swing doubles. However, the total voltage swing ( $=2\mathrm{x}0.68\mathrm{V}$ ) is still less than that for FERAMs (1.64V). It is also important to note that negative select-line voltage as well as select-line boost proposed in the FEFET-based array contributes to increase in the write power, which is considered in the results above. However, in spite of such overheads, the overall write power is significantly less than that of FERAMs.

# 6.2.3 Area

The proposed FEFET memory cell use two transistors to store a single bit. As a result, the FEFET memory cells exhibits $2.4\mathrm{x}$ area, compared to IT-IC FERAM (Fig. 11), Note that there are different flavors of FERAMs showing different cell areas [8]. We have performed a worst-case area comparison for the proposed cell by comparing against the FERAM implementation with the minimum area. The proposed cell-array co-design minimizes the area overhead by (a) employing a unique architecture which eliminates the need for read access transistors and limits the number of transistors in a cell to two and (b) sharing the metal line for selecting the cell and applying the read voltage, which averts routing congestion. Although the proposed cell shows an area penalty, other design metrics show a significant improvement compared to FERAMs, alleviating the current limitations of FE-based technology. This can have important implications in system design.

# 6.2.4 Retention

For FE based memories, the retention time is expected to be exponentially proportional to the product of coercive voltage,

![](images/4b8da953842e155ca9e57292a142819f6cfa07fd4e66d674e4b907d5740abea6.jpg)

![](images/2dd6cf15e36df90f56409c3170635fcfaeb4b9114d28f0a742b5ff855d5cf903.jpg)

![](images/cf83148a0bef29cdc6e5f94b0e413b5cf22bec706f8a9276ebce94515a0fb3e6.jpg)  
Figure 10. One single 65nm FEFET and FERAM cell comparisons: (a) write access time; (b) energy

![](images/02ad137f0275782b8868650b205554c39a66f4449d8c26e677849fe3068c0e07.jpg)  
Figure 11. 2x2 memory cell layout: (a) FEFET; (b) FERAM.

remnant polarization, and area of the ferroelectric capacitor within single domain approximation. The retention time of current FEFET design (FE layer thickness $2.25\mathrm{nm}$ , width $65\mathrm{nm}$ ) is lesser than the FERAM design (FE layer thickness $1\mathrm{nm}$ , width $65\mathrm{nm}$ ) as the coercive voltage is higher for FERAMs. Our targeted applications like nonvolatile processor system [4] do not require long retention time. Larger FE layer thickness or FE layer area could be adopted for more retention time, required in other applications, at the cost of more write energy and area. For example, increasing the width of the FEFET to $112.5\mathrm{nm}$ achieve similar retention time as that of FERAM. Meanwhile, for current FERAM systems, reducing the retention for low voltage operation is difficult, as the coercive voltage is as high as $1.26\mathrm{V}$ even with smaller ferroelectric layer thickness of $1\mathrm{nm}$ . Furthermore, with new materials, the tradeoff study for the optimum retention, performance, area can be explored in future. In the next section, we analyze the impact of the proposed FEFET-based memory at the system level by analyzing its effects on the energy efficiency of a nonvolatile processor.

# 7. NVP ANALYSIS

Nonvolatile memories such as resistive RAMs [20] and FERAMs [17] are being actively explored to design nonvolatile processors by utilizing nonvolatile elements to retain the state of the system in the event of a power failure, thereby enhancing forward progress guarantees. However, the current technologies under consideration are all subject to limitations in endurance, energy efficiency, destructive reads, or high write power. The proposed memory cell offers appealing features for the design of nonvolatile processors. We performed an extensive analysis of the system-level implications by simulating the replacement of FERAMs in an existing nonvolatile processor with the proposed FEFET-based memories using the calibrated simulator developed in [4]. Fig. 12. shows the non-pipelined (NP) on-demand all-backup (ODAB) NVP architecture [4]. When a power outage is detected, the nonvolatile controller backs up volatile data of the program counter (PC) and register files to the NVM backup block to save the computation state during the power failure. Once the power is

retrieved, the backup data will be written back to PC and register files to recover the NVP computation state. With significant power consumed in backup operations, especially when the amount of memory is large, it is essential to reduce the read and write memory energy consumption in NVP design. In the evaluations, the parameters for the NVM backup block implemented in FEFET or FERAM are shown in Table 3.

Table 3. FERAM and FEFET memory parameters in NVP   

<table><tr><td colspan="4">FEFET</td><td colspan="4">FERAM</td></tr><tr><td>Bit line voltage</td><td>Write time</td><td>Write energy</td><td>Read energy</td><td>Bit line voltage</td><td>Write time</td><td>Write energy</td><td>Read energy</td></tr><tr><td>0.68V</td><td>0.55nS</td><td>4.82pJ</td><td>0.28pJ</td><td>1.64V</td><td>0.55nS</td><td>15.0pJ</td><td>15.5pJ</td></tr></table>

![](images/eb9077edcec6b2fe46d2b1695b934b7ae5ecb5ea60b5ac06b76da7aa72d3733a.jpg)  
Figure 12. NVP architecture with backup control.

![](images/4b374c8a302893191b015b655b31aff3dccd736edeef89d69886d4cc41304f32.jpg)  
Figure 13. Computation forward progress comparisons.

To compare the computation forward progress (FP) in typical applications (MiBench in [24] as the testbench) with a Wi-Fi energy harvester [4] as the supply, Fig. 13 compares the simulated FP. Using FEFET memory provides $22\% - 38\%$ more FP than using FERAM. Such significant system-level improvement confirms the advantage of using FEFET as nonvolatile memory. In particular, the gains form the replacement of FERAMs with FEFET memories are the largest for the lowest power and most frequently interrupted power traces, showing that FEFETs enable the deployment of NVPs into new, even lower-power scenarios than were previously viable with FERAMs.

# 8. CONCLUSION

We proposed a memory design technique based on FEFETs, utilizing the polarization retention capability of FE coupled with the three terminal structure of the transistor to implement low power robust nonvolatile memory cells and arrays with separate read and write paths. We discussed the device design and the optimization of the ferroelectric thickness to introduce nonvolatility in FEFETs. With proper device design, we showed that the coercive voltage of FEFETs can be reduced in comparison to FE capacitors, leading to write power savings. We also discussed other appealing features of an FEFET-based memory device, including six orders of magnitude difference in the currents corresponding to logic 0 and 1. Based on such intriguing device properties, we proposed a 2-T cell with non-destructive read, high distinguishability and decoupling of the read-write paths. We showed that the proposed cell exhibits $67\%$ lower write power at iso-write time compared to FERAMs. We proposed an array design technique, which limits the number of transistors in the cell to two and avoids metal routing congestion to minimize the area-penalty.

Moreover, the proposed biasing scheme for the unaccessed cells and the sensing circuit eliminates the sneak current paths and stability issues in the unaccessed cells. Deployment of the FEFET-based nonvolatile memory macro in a nonvolatile processor showed $27\%$ higher forward progress compared to an FERAM.

# Acknowledgement

This work was supported in part by the Center for Low Energy Systems Technology (LEAST) sponsored by MARCO and DARPA, SRC-GRC and in part by the NSF awards 1160483 (ASSIST), 1205618, 1213052, 1461698, and 1500848.

# REFERENCES

[1] Y. Liu, et al. Ambient energy harvesting nonvolatile processors: from circuit to system. In DAC, ACM, 2015.   
[2] C. W. Smullen, et al. Relaxing non-volatility for fast and energy-efficient STT-RAM caches. In HPCA, pages 50-61, 2011.   
[3] X. Li, et al. RF-powered systems using steep-slope devices, In NEWCAS, pages 73-76, 2014.   
[4] K. Ma, et al. Architecture exploration for ambient energy harvesting nonvolatile processors. In HPCA, pages 526-537, 2015.   
[5] A. Chen. Emerging nonvolatile memory (NVM) technologies. In ESSDERC, pages 109-113, 2015.   
[6] Y. Wang, et al. A 3us Wake-up Time Nonvolatile Processor Based on Ferroelectric Flip-Flops. In ESSCIRC, 2012.   
[7] K. L. Wang, et al. 2013. Low-power nonvolatile spintronic memory: STT-RAM and beyond. Journal of Physics D: Applied Physics, 46(7), 074003.   
[8] A. Sheikholeslami and P. G. Gulak. A survey of circuit innovations in ferroelectric random-access memories. Proceedings of the IEEE, 88(5): 667-689, 2000.   
[9] S. Das and J. Appenzeller. FETRAM. An organic ferroelectric material based novel random access memory cell. Nano letters 11(9): 4003-4007, 2011.   
[10] T. Hatanaka, et al. Ferroelectric (Fe)-NAND flash memory with batch write algorithm and smart data store to the nonvolatile page buffer for data center application high-speed and highly reliable enterprise solid-state drives. JSSC, 45(10): 2156-2164, 2010.   
[11] A.I. Khan, et al. Ferroelectric negative capacitance MOSFET: Capacitance tuning & antiferroelectric operation. In IEDM, pages 11.3.1-11.3.4, 2011.   
[12] S. Salahuddin and S. Datta. Use of negative capacitance to provide voltage amplification for low power nanoscale devices. Nano letters, 8(2): 405-410, 2008.   
[13] K. Karda, et al. An anti-ferroelectric gated Landau transistor to achieve sub-60 mV/dec switching at low voltage and high speed. Applied Physics Letters, 106(16), 163501, 2015.   
[14] http://ptm.asu.edu/   
[15] Y. Kim, S. H. Choday, et al. DSH-MRAM: Differential spin Hall MRAM for on-chip memories. In IEEE Electron Device Letters, 34(10), pages 1259-1261, 2013.   
[16] C.W. Yeung, et al, Low power negative capacitance FETs for future quantum-well body technology, In VLSI-TSA, pages 1-2, 2013.   
[17] M. Qazi, et al. A low-voltage 1 Mb FRAM in 0.13 m CMOS featuring time-to-digital sensing for expanded operating margin. Solid-State Circuits, IEEE Journal of 47(1), pages 141-150, 2012.   
[18] FRAM Guide book,Fujitsu Semiconductor manual,2005   
[19] M. F. Chang, et al. Challenges and Circuit Techniques for Energy-Efficient On-Chip Nonvolatile Memory Using Memristive Devices. IEEE Journal on Emerging and Selected Topics in Circuits and Systems, 5(2), pages 183-193, 2015.   
[20] S. S. Sheu and M. F. Chang. A 4Mb embedded SLC Resistive-RAM macro with 7.2ns read-write random access time and 160ns MLC-access capability. In ISSCC, pages 200-201, Feb 2011   
[21] M. F. Chang, et al. Area-Efficient Embedded Resistive RAM (ReRAM) Macros Using Logic-Process Vertical-Parasitic-BJT (VPBJT) Switches and Read-Disturb-Free Temperature-Aware Current-Mode Read Scheme. IEEE JSSC, 49(4), pages 908-916, 2014.   
[22] M. F. Chang, et al. A 0.5V 4Mb Logic-Process Compatible Embedded Resistive RAM (ReRAM) in 65nm CMOS Using Low Voltage Current-Mode Sensing Scheme with 45ns Random Read Time. In ISSCC), pages 434-435, 2012.   
[23] M. F. Chang, et al., An offset tolerant current-sampling-based sense amplifier for sub-100nA-cell-current nonvolatile memory. IEEE ISSCC, pages. 206-207, Feb 2011.   
[24] M. R. Guthaus, et al. Mibench: A free, commercially representative embedded benchmark suite. In Workload Characterization, IEEE International Workshop on, pages 3-14, 2001.