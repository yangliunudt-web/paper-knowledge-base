---
title: "Two-dimensional fully ferroelectric-gated hybrid computing-in-memory hardware for\\"
authors:
  - "Tian Lu"
  - "Junying Xue"
  - "Penghui Shen"
  - "Houfang Liu"
  - "Xiaoyue Gao"
  - "Xiaomei Li"
  - "Jian Hao"
  - "Dapeng Huang"
  - "Ruiting Zhao"
  - "Jianlan Yan"
  - "Mingdong Yang"
  - "Bonan Yan"
  - "Peng Gao"
  - "Zhaoyang Lin"
  - "Yi Yang"
  - "Tian-Ling Ren"
date: "2024-09-04"
year: 2024
journal: "Science Advances"
doi: "10.1126/sciadv.adp0174"
abstract: "Computing in memory (CIM) breaks the conventional von Neumann bottleneck through\\"
abstract_cn: "存内计算（CIM）通过原位处理打破传统冯·诺依曼瓶颈。数字和模拟 CIM 硬件的单片集成可同时确保高精度和高能效，为日益复杂的人工智能应用提供可持续范式，但仍具挑战性。本文提出一种兼容\\"
cite: "Lu T, Xue J, Shen P, et al. Two-dimensional fully ferroelectric-gated hybrid computing-in-memory\\"
aiSum: "2D FeFET 混合 CIM：布尔逻辑+多级单元、96.36% 良率、>10^12 耐久性、用于动态跟踪。"
confidence: "high"
---

Lu et al., Sci. Adv. 10, eadp0174 (2024)     4 September 2024
S c i e n c e  A d va n c e s  | R e s e a r c h  A r t i c l e
2 of 10
hybrid CIM integration (8). However, conventional silicon-­based or 
other polycrystalline oxide–based FeFETs always face drifted or de-
graded electrical performance induced by undesired atomic diffu-
sion and charge trapping effects in the channel-­associated interfaces, 
leading to low endurance and large variations (15), which severely limits 
their large-­scale applications. To settle this matter, two-­dimensional 
(2D) transition metal dichalcogenides emerge as an appealing solution. 
They feature dangling bond–free passivated surfaces that minimize 
scattering effects, maintain robust mobility even at atomic-­level 
thicknesses, and offer van der Waals (vdW) layered interaction for 
processing compatibility (16).
In this study, we showcase a 2D fully ferroelectric-­gated hybrid 
CIM hardware platform that is compatible with complementary 
metal-­oxide semiconductor technology (Fig. 1A). Benefiting from 
the newly developed solution-­processable method, FeFETs are 
constructed with a vdW interface between high-­k hafnium oxide 
and 2D layer-­by-­layer MoS2 atomic-­thin channels. Serving as the 
fundamental units, they exhibit exceptional performance in terms 
of ultralong endurance cycles (>1012), extremely low cycle-­to-­cycle 
(CtC)/device-­to-­device (DtD) variations (~0.3%/~0.5%), and lowest 
power consumption of 0.03 fJ/bit with a 96.36% wafer-­scale yield. 
Taking the AI task of dynamic object tracking (DOT) as a demon-
stration, we further customize a 2D fully ferroelectric-­gated hybrid 
CIM system based on the monolithic integration of Boolean logic 
and trigger arrays for moving target detection as well as multilevel 
cell arrays for feature extraction. Last, this system successfully iden-
tifies pedestrians and tracks their motion paths with a high accuracy 
of 99.8% and a power efficiency of 26.3 TOPS/W. These results show 
the promising prospects of integrating fully ferroelectric-­gated hybrid 
CIM hardware as versatile blocks for the implementation of various 
AI applications.
RESULTS
2D fully ferroelectric-­gated platform
Here, we developed a solution-­processable method with 2D layer-­
by-­layer MoS2 atomic-­thin films for FeFETs and their integrated 
hardware (see Materials and Methods). The basic ferroelectric cells 
were constructed with a bottom-­gate (BG) metal-­ferroelectric-­
metal-­insulator-­semiconductor (MFMIS) structure as shown in 
Fig.  1B. First, a TiN/Hf0.5Zr0.5O2 (HZO)/TiN capacitor was pre-
pared and subjected to rapid thermal annealing (RTA) at 500°C. On 
the basis of the highly crystalized o-­phase domains (Fig. 1C), the 
ferroelectric capacitor exhibits a good hysterical behavior in the po-
larization–electric field (P-­EF) curve, with a coercive voltage (2Vc) 
of about 4.2 V and a high remnant polarization (2Pr) of 49.5 μC/
cm2 (fig. S1). Subsequently, a 15-­nm high-­k hafnium oxide dielec-
tric was stacked as the gate insulator, on which the 2D channel 
could be deposited. While, unlike other methods, e.g., chemical va-
por deposition (CVD), metal-­organic chemical vapor deposition 
(MOCVD), atomic layer deposition (ALD), and molecular beam 
epitaxy (MBE), that may involve the introduction of undesired im-
purities and stresses during additional transfer processes (15–18), a 
solution-­based process was adopted in this step. Through the 
A
B
C
D
E
F
G
Fig. 1. 2D fully ferroelectric-­gated hybrid platform. (A) Overview of the 2D hybrid fully ferroelectric-­gated CIM platform which includes the Boolean logic and triggers 
for digital processing in memory and multistage cell (MSC) arrays for analog in-­memory computing. (B) Schematic of the wafer-­scale fabrication of FeFETs with solution-­
processable 2D MoS2 channel. (C) Cross-­sectional high-­angle annular dark-­field scanning transmission electron microscopy (HAADF-­STEM) image of the ferroelectric ca-
pacitor with o-­phase HZO (fast Fourier transform shown in inset). (D) Cross-­sectional STEM image of the MoS2-­FeFET and corresponding energy-­dispersive spectroscopy. 
(E) Cross-­sectional STEM image of the layer-­by-­layer MoS2 atomic-­thin films as well as HfOx/MoS2 interface with a clear vdW gap. (F) Ultraviolet-­visible absorption spectra 
of the MoS2 inks with different concentrations which are denoted by Abs0.296, Abs0.406, Abs0.518, and Abs0.616, respectively. (G) A1g-­E1
2g map of the MoS2 films with 
selected deposition parameters (Abs × n) of 0.296 × 5 (a), 0.406 × 4 (b), 0.518 × 3 (c), and 0.616 × 3 (d), respectively. The value of A1g-­E1
2g indicates that the thickness of MoS2 
films is basically no more than four layers (marked number). Scale bar, 5 nm.
Downloaded from https://www.science.org at National University of Defense Technology on December 31, 2025

Lu et al., Sci. Adv. 10, eadp0174 (2024)     4 September 2024
S c i e n c e  A d va n c e s  | R e s e a r c h  A r t i c l e
3 of 10
intercalation agent and kinetic optimization in the preparation pro-
cess (19), the electron injecting into the host MoS2 crystal was 
greatly reduced to below the certain threshold of 0.29 electrons per 
MoS2 formula unit (20, 21), and thus pure semiconducting 2H-­
phase MoS2 ink was well prepared with minimal defects and phase 
transformation (fig. S2) (22). Benefiting from its low selectivity to 
the substrates, MoS2 ink was then directly spin-­coated onto the in-
sulator, where this aligns the flakes and ensures MoS2 film with op-
timized morphology. Last, Ti/Pd electrodes were evaporated as the 
source/drain (S/D). As shown in Fig. 1D, the cross-­sectional scan-
ning transmission electron microscopy (STEM) images of the Fe-
FET identify its multilayer gate stacks and illustrate clear elemental 
distributions, which is propitious to realize low leakage, long en-
durance, and large-­scale uniformity of FeFET units.
To ensure FeFETs with efficient gate control and a high on/off 
ratio (23), our method included a carefully designed scheme. This 
scheme allows for the deposition of ultrathin MoS2 films with con-
trollable thickness (Fig. 1E) by precisely coordinating the concen-
trations of the MoS2 ink with its spin-­coating times (denoted by 
Abs × n). Initially, the MoS2 ink was adjusted to specific concentra-
tions, guided by the optical ultraviolet-­visible (UV-­vis) absorption 
spectrum (Fig. 1F) and the Beer-­Lambert law (text S1). Alterna-
tively, different times of spin coating could be used to guarantee the 
continuity of the MoS2 film (fig. S3). Combining these two param-
eters, the prepared MoS2 films were analyzed by Raman spectros-
copy (fig. S4) and their thickness could be inferred by calculating 
the values of peak distance (A1g-­E1
2g ) (24). Following this, appropri-
ate combinations of Abs × n such as 0.296 × 5, 0.406 × 4, and 0.518 × 
3 were tried, and the deposited MoS2 films with no more than four 
layers were obtained (Fig. 1G). These results were well consistent 
with the atomic force microscopy measurements (fig. S5). To facili-
tate the reproduction of such a deposition process, we established 
an empirical formula linking A1g-­E1
2g value to Abs × n. This for-
mula shows that the thickness of MoS2 films correlates positively 
with the product of the solution concentration and the spin-­coating 
times (figs. S6 and S7), which provided a wide process window for 
the repeatable deposition of layer-­by-­layer MoS2 films with uni-
form and controllable atomic thickness. The STEM images of the 
MoS2 channel and corresponding electron energy-­loss spectrosco-
py (EELS) illustrate nearly atomically flat 2D interfaces along with 
a clear vdW gap (fig. S8), which intrinsically guarantees the effi-
cient charge transport with fewer carriers being injected and scat-
tered (25). Note that this preparation method is fully adaptive to 
MOSFETs only by selectively etching the deposited HZO layer in 
the second step, which offers a compatible method for building fer-
roelectric functional blocks.
Superior basic ferroelectric units
In addition to material and processes engineering, taking advantage of 
the plasticity of the MFMIS structure, we tuned the performance 
of the FeFETs in the initial batches by changing the area ratios (ARs) 
of their gate capacitors (fig. S9) (26). Basically, the obtained FeFETs 
exhibit a typical n-­type transfer curve (Id-­Vg) with high on/off ratios 
of over 107 and counterclockwise hysteresis under the double sweep-
ing of Vg (fig. S10). Through a full sampling test of the total 1292 
FeFETs in one batch, they exhibit an excellent wafer-­scale yield of 
96.36% ± 1.34% at a confidence level of 99% (fig. S11). On this basis, 
by increasing ARs of the FeFETs from 3.6 to 14.2, Vg dropping on 
the HZO layer can be preferably increased according to the princi-
ple of capacitive voltage division, which enables more effective po-
larization switching of ferroelectric domains (27), lastly leading to a 
maximum memory window (MW) of up to 4.7 V.
Subsequently, we developed a comprehensive testing methodol-
ogy to evaluate the performance of the fabricated FeFETs. First, we 
randomly selected 50 FeFETs with an AR of 14.2 and measured their 
transfer curves, 49 of which showed similar Id-­Vg curves (Fig. 2A). 
Meanwhile, these devices exhibited an average MW of 4.2 V with an 
SD (σ) of 0.8 V (fig. S12) as well as an average on/off ratio and a 
subthreshold swing (SS) of 3.7 × 107 and 144.7 mV/dec with corre-
sponding σ of 1.2 × 107 and 15.0 mV/dec, respectively. To test their 
stability, the FeFETs were normally preserved in the air at room 
temperature beforehand for 12 months. Owing to weak vdW inter-
facial interactions, these FeFET devices show stable electrical per-
formance (Fig. 2B) with Vth+/Vth− maintaining almost unchanged 
(fig. S13). Following this, cycling tests were conducted on one MoS2-­
FeFET along with a comparative experiment on an amorphous in-
dium gallium zinc oxide–based FeFET (Fig. 2C and fig. S14). It is 
clearly shown that the 2D MoS2–based FeFET is much more stable 
without any notable deviation in Id-­Vg curves, and its average MW 
and on/off ratio are 3.9 V and 1.8 × 107 with small σ of 0.09 V and 
7.5 × 106, respectively (fig. S15). These results imply that FeFETs 
with solution-­processable MoS2 atomic-­thin channels have excel-
lent electrical stability and consistency.
To further assess the reliability of MoS2-­FeFETs as NVMs, we 
characterized their retention and endurance properties. For reten-
tion testing, one Vg pulse of +4 V/−4 V was applied to the FeFET, 
followed by continuous Id measurements at Vg of 0 V. As shown in 
Fig. 2D, our device exhibits excellent characteristics of retention, 
which can maintain the programmed state (PRG)/erased state (ERS) 
at least 104 s with negligible current degradation, and the current 
loss after 10 years obtained by extrapolation is estimated at only 
about 7%. To measure endurance cycles, we repeatedly applied bi-
polar pulses of +4 V/−4 V with different pulse widths to the FeFET 
for cycling programming/erasure operations. Figure 2E shows that 
there is a trade-­off between the pulse width and endurance cycles. 
The obtained value of Id can maintain a high PRG/ERS ratio of 106 
for 107 cycles at a pulse width of 1 μs. When the pulse width is short-
ened to 100 ns, the PRG and ERS states exhibit a relatively low ratio 
of 105 but can be rewritable over 109 cycles without any prominent 
degradation to satisfy the requirements for edge training (28). When 
the pulse width is further reduced to 30 ns (Fig. 2F), the correspond-
ing PRG/ERS ratio drops to about 103 but is programmable up to 
1012 cycles, which also indicates an extremely low switching energy 
of 3 fJ (Fig. 2G and text S2) (29). On the whole, our basic ferroelec-
tric units exhibit overall improvements in the key figures of merit 
compared with previously reported FeFETs (Fig. 2H and table S1), 
which compensates for their deficiencies in large-­scale production, 
making the construction of fully ferroelectric-­gated hybrid blocks 
feasible (30–39).
Ferroelectric-­based digital processing in memory
Digital computing is indispensable for high-­performance computa-
tion (HPC) owing to its robustness to meet high precision require-
ments (40). By using the nonvolatile state of conductance as an 
input, ferroelectric digital units with compact areas and low power 
consumption emerge as a promising solution for HPC (41). In this 
section, we experimentally demonstrate reconfigurable ferroelectric 
Downloaded from https://www.science.org at National University of Defense Technology on December 31, 2025

Lu et al., Sci. Adv. 10, eadp0174 (2024)     4 September 2024
S c i e n c e  A d va n c e s  | R e s e a r c h  A r t i c l e
4 of 10
Boolean logic and trigger arrays for efficient digital processing 
(Fig. 3A).
When applied with a Vg pulse of 4 V/−4 V, the FeFET is prepro-
grammed to the PRG/ERS state, i.e., a logic value of 1/0 for input A, 
respectively. Subsequently, a gate voltage representing input B is 
applied to the FeFET, and then output current Id can be measured 
which depends on the value of both input A and B. By selecting a 
suitable voltage of input B, reconfigurable OR and AND logic gates 
can be achieved within a single FeFET. When 0.4 V/1.5 V is defined 
as the logical 0/1 for input B, respectively, the output Id is low (log-
ical 0) only if the inputs A and B are both logical 0, behaving as an 
OR logic gate. In addition, when the logical state of 0/1 of input B 
is set as −1 V/0.4 V, respectively, the output Id is high (logical 1) 
only when both of the inputs A and B are logical 1, behaving as an 
AND logic gate. On this basis, by connecting a pull-­up loaded 
transistor serially to the FeFET, such current outputs can be con-
verted to opposite voltage output, and thus NOR/NAND logic 
gates could be obtained. Moreover, when two AND-­mode FeFETs 
with always-­inverted inputs are connected in parallel, exclusive 
NOR/OR (XNOR/XOR) logic gates are realized with the current 
output. Similarly, by adding a loaded pseudo-­transistor to this unit 
as above, we obtain the corresponding voltage-­output XOR/XNOR 
logic gates. In this way, compound Boolean logic gates are implemented 
as shown in Fig. 3B which greatly reduce hardware cost as well as 
sum energy consumption to less than 6 fJ per operation.
By integrating logic into memory, ferroelectric Boolean logic 
presents a new paradigm in constructing complex processing cir-
cuits for meeting diverse computing needs (42). In our work, we 
proposed a reconfigurable compound gate and a one-­bit full-­adder 
(FA) emerged circuit (fig.  S16). The results based on Simulation 
Program with Integrated Circuit Emphasis (SPICE) show that this 
unit not only achieves 16 binary in/out logic functions (fig. S17) but 
also markedly reduces the area of the FA by 39.3% [from 28 MOS-
FETs (41) to 7 FeFETs and 10 MOSFETs], while consuming an ex-
tremely low average dynamic writing/reading energy of 7.02 fJ/1.13 fJ 
(fig. S18). In addition, we also developed a substitute circuit for the 
subtraction or difference operators. On the basis of the ferroelectric 
XNOR arrays, any dynamic changes of each pixel can be highlighted 
with an output of logic 0 (fig. S19), which eliminates the need for 
extensive subtraction and judgment operations (43).
In addition to combinatorial logic circuits, the ferroelectric units 
with memory characteristics are actually more similar to the se-
quential logic circuits. As an indispensable part of digital circuits, 
they provide more efficient and flexible computational methods for 
digital circuits. Schmitt triggers (STs), for example, having different 
threshold voltages are widely adopted to improve the noise margin 
Energy (pJ/state)
100
10−3
ZnOx
IGZO
CNT
WSe2
Si
1 pJ
45 pJ 35 pJ
7.5 pJ
30 fJ
Digital
Analog
This work
Si
80 pJ
103
26667×
1000×
3 fJ
0.03 fJ
−6
−3
0
3
6
10−14
10−9
10−4
Id (A)
Vg (V)
Cycles
Vds = 1 V
MW
−6
−3
0
3
6
10−14
10−9
10−4
Id (A)
Vg (V)
Vds=1 V
MW
Time
Initial
1 month
3 months
6 months
7 months
10 months
12 months
−6
−3
0
3
6
10−14
10−9
10−4
Id (A)
Vg (V)
 Devices
MW
Vds = 1 V
101
104
107
1010
1013
10−3
10−2
10−1
100
 This work      
BiT
HfO2-based 
PZT
P(VDF-TrFE)    
AlScN
Nor. MW(V nm−1)
Endurance
106
105
103
105
103~104
103~104
101~105
103~104
0.0
0.2
0.4
0.6
0.8
Id (A)
Time (s)
10−7
10−10
30 ns
+4 V
−4 V
30 ns
PRG
ERS
A
B
C
D
E
F
G
H
PRG/ERS ratio
102
104
106
108
10−13
10−9
10−5
Id (A)
Time (s)
PRG +4V 1 s
ERS −4V 1 s
Read @ 0 V, 300 K, air
10 years
100
103
106
109
1012
10−13
10−9
10−5
Pulse width
1 s
100 ns
30 ns
Id (A)
Cycle
PRG +4 V
ERS −4 V
Read @ 0 V, 300 K, air
Fig. 2. Electrical characteristics of the basic ferroelectric units. (A) Transfer curves of the different MoS2-­FeFETs. (B) Transfer curves of the MoS2-­FeFET which was pre-
served in the air at room temperature for a year. (C) Cycling test for the MoS2-­FeFET after being preserved in the air for a year. (D) Retention, (E) endurance, and (F) speed 
test for the MoS2-­FeFETs. (G) Benchmark of energy consumption for digital and analog computing based on the FeFETs. (H) Benchmark of endurance and Nor. MW with 
previously reported FeFETs. Nor. MW = MW/sweeping range of Vg. The high/low threshold voltage (Vth+/Vth−) is defined as the value of the positive/negative voltage 
corresponding to the Id of 1 nA in the transfer curve.
Downloaded from https://www.science.org at National University of Defense Technology on December 31, 2025

Lu et al., Sci. Adv. 10, eadp0174 (2024)     4 September 2024
S c i e n c e  A d va n c e s  | R e s e a r c h  A r t i c l e
5 of 10
of digital circuits, as well as pulse shaping and analog-­to-­digital 
converters (44). Conventional ST usually requires six transistors with 
complex circuit structures and low power efficiency (45). Here, a 
highly simple reconfigurable 2T ST with an ultralow operating volt-
age of 10 mV is realized by simply using the same cascade structure 
of the NOR/NAND gates mentioned above (fig. S20). With double-­
swept input voltage, this ST exhibits different Vth+ and Vth−. When 
the input signal surpasses Vth+, the output is pulled down to logic 0 
and is not reset until the signal falls below Vth−. On this basis, our 
ST implements rail-­to-­rail transitions in the triangular and sinusoi-
dal waveforms. In addition, it also realizes logic-­state transitions to 
ultrafast inputs with 30-­ns width (Fig. 3C). Not only that, we further 
explore its potential for array-­level filtering. Such STs experimen-
tally demonstrate strong noise reduction capabilities (fig. S21).
Ferroelectric-­based analog in-­memory computing
Beyond digital processing, the FeFET can also mimic the potentia-
tion/depression behavior of biological synapses owing to its oppo-
site conductance responses to the positive and negative pulses (46). 
On the basis of more precise control of the polarization switching of 
partial ferroelectric domains in the gate stacks to accumulate/deplete 
different numbers of carriers in the channel (33), the FeFET can be 
further programmed as a multistage cell (MSC). Through con-
structing a 4 × 4 ferroelectric MSC array, in this section, we ex-
plore efficient analog computing based on parallel vector-­matrix 
multiplication (VMM).
Figure 4A shows that the fabricated MSC array consists of four 
word lines (WL0 to WL3), four source lines (SL0 to SL3), and four 
drain lines (DL0 to DL3). The WLs and SLs are parallel to each other 
to control the MSCs in the rows and are vertical with respect to the 
DLs responsible for the columns. To ensure accurate computing, 
MSC (>6-­bit states) with symmetric and linear conductance re-
sponses are generally preferred (47). To this end, we systematically 
investigated the multistate storage capacity of a single FeFET by tun-
ing the steps, duration, and interval of the applied pulse sequences 
(fig. S22). Ultimately, when we adopted a 30-­ns pulse scheme with 
increasing amplitude, the ferroelectric MSC achieved a highly sym-
metric and linear conductance response with 90 states at a low noise 
level (fig. S23) (48). The determined pulses were then applied re-
peatedly for 100 cycles on one FeFET (18,000 pulses in total). As a 
result, hardly any fluctuation is observed in the overall range of the 
conductance responses (Fig. 4B), and all conductance states exhibit 
steep probability distribution without any overlap (fig. S24), which 
results in an extremely low CtC variation of about 0.3% (Fig. 4C). 
On the other hand, when the same pulse sequence was applied to 
different MSCs, they show similar conductance responses, which 
leads to a low DtD variation of about 0.5% (Fig. 4D and fig. S25).
Benefiting from these merits (table S2) (31, 47, 49–53), here, we 
demonstrate efficient VMM for image feature extraction by using 
the ferroelectric MSC arrays. First, to obtain a particular conduc-
tance matrix as shown in Fig. 4A, we adopt a selected/half-­selected/
unselected programming method to inhibit the disturbance when 
B
Boolean logic gates 
Schmitt triggers
C
A
Ferroelectric digital hardware
1FeFET
0
25
50
−6
0
6
0
1
2
3
4
0
25
50
Time (s)
0
6
0
25
50
−6
0
6
OUT (mV)
IN (V)
b
a
c
d
B
A
VDD
B
A
B
B
A
A
VDD
B
B
A
A
2FeFET
+1R
+1R
(0,0)   (0,1)   (1,0)    (1,1)  (0,0)   (0,1)    (1,0)   (1,1)
OUT (A or V)
10−9
10−6
(
10−6
10−9
0
0
1
1
OR
AND
NAND
NOR
XNOR
XOR
XNOR
XOR
IN (A, B)
a
b
c
d
Output
Output
Current output
Current output
Voltage output
Voltage output
−6
Fig. 3. Ferroelectric Boolean logic gates and triggers. (A) Optical images and circuit diagrams of the ferroelectric digital hardware of Boolean logic and Schmitt trigger 
(ST) array. (B) Output signals of the ferroelectric Boolean logic gates. (C) The transformation in triangular (in orange) and sine (in blue) waveforms and logic-­state transition 
(in green) based on ferroelectric STs.
Downloaded from https://www.science.org at National University of Defense Technology on December 31, 2025

Lu et al., Sci. Adv. 10, eadp0174 (2024)     4 September 2024
S c i e n c e  A d va n c e s  | R e s e a r c h  A r t i c l e
6 of 10
writing the weights into the MSC arrays row by row (figs. S26 and 
S27), and then a small input image of the letter “A” with a size of 
12 × 8 pixels is used as an example of input. This image is converted 
into a voltage matrix based on the intensity of each pixel, and then it 
is split into segmentation vectors of two bits each in length and ap-
plied segment by segment to the four WLs. To achieve parallel 
VMM, each MSC multiplies its conductance by the input voltage 
according to Ohm’s law and yields a corresponding output current, 
after which all currents in the same column are simultaneously ac-
cumulated by the DLs based on Kirchhoff’s law. Then, extra subtrac-
tion or addition operations are performed on the selected DLs to 
extract the key features of the image. For example, DL0 and DL1, 
which represent positive and negative weight columns, respectively, 
are connected to a subtraction circuit to capture the vertical edge of 
the letter A, and then the result is converted back into voltage signals 
by a 5 × 105–ohm load resistor. Last, the vertical edge of the letter 
A subsequently stands out with repeated convolution operations 
(fig. S28).
While maintaining the previously programmed weight distribu-
tion in Fig. 4A, a larger image containing 450 × 450 pixels is further 
used to verify the ability of this ferroelectric MSC array for fea-
ture extraction in different modes. Following the same principle, 
four convolution kernels of 
[ 1 1
1 1
]
 , 
[ 1 −1
1 −1
]
 , 
[ 1
1
−1 −1
]
 , and 
[ 1 0
0 −1
]
 
are constructed corresponding to extract four typical features of 
images—mean, vertical edge, horizontal edge, and edge, respectively 
(fig. S29). Figure 4E clearly illustrates four identified results of the 
images after a large number of repeated convolution operations by 
using different kernels. Note that the conductance states of each 
MSC can be further used for arbitrary weight distributions, making 
it feasible to extract more complex input features without being 
limited to the above four patterns. The weight matrix can then be 
continuously adjusted based on feedback by comparing the error 
between the processed results and the true values to achieve the op-
timal feature extraction in various NNs.
Fully ferroelectric-­gated hybrid CIM system for DOT
DOT technology nowadays has shown increasing importance in au-
tonomous driving, intelligent surveillance, and robot navigation 
(43). For autonomous driving systems, timely and accurate deter-
mination of pedestrian movements and other obstacles is critical 
because even a millisecond delay during high-­speed driving can 
jeopardize personal safety (54). Therefore, DOT requires the timely 
processing of massive amounts of sensor data as well as advanced 
software and hardware, for which we customize a hybrid CIM sys-
tem based on the digital and analog ferroelectric functional hard-
ware developed above.
To achieve DOT, the flowchart is divided into four steps (Fig. 5A). 
First, videos of the given scenarios are recorded by using cameras 
and other sensors, after which they are segmented into 30 frames 
per second and compressed into grayscale images. Second, digital 
circuits are established to clearly capture the moving objects. We use 
the ferroelectric XNOR, convolution kernels, and ST arrays to ac-
curately extract the size, position, and other key features of the dy-
namic targets (Fig. 5B). By performing XNOR operations on the 
pixels corresponding to two consecutive frames, we are easily able to 
0
90
180
0.0
0.5
1.0
1.5
Conductance ( S)
Pulse number
Max
Min
Median
75%
25%
Device-to-device variation
Increasing
Decreasing
~0.5%
0
90
180
0.0
0.5
1.0
1.5
Conductance ( S)
Pulse number
Max
Min
Median
75%
25%
Cycle-to-cycle variation
Increasing
Decreasing
~0.3%
Conductance ( S)
B
C
D
A
E
Mean
Vertical edge
Horizontal edge
Edge
Original
Analog in-memory computing
3 V
0 V
0
9000
0.0
0.5
1.0
1.5
Conductance ( S)
Pulse Number
4500
13,500
Total: 100 cycles
18,000
Fig. 4. Ferroelectric MSC array for analog in-­memory computing. (A) Optical image of the 4 × 4 ferroelectric MSC array and corresponding weight matrix after row-­by-­
row programming. (B) The cycling test for the obtained conductance response with 90 states (18,000 pulses in total). (C) CtC variation characteristics of 100 conductance 
increasing/decreasing cycles. (D) DtD variation characteristics of different MSCs. (E) Feature extraction of the input image of “windows” with the size of 450 × 450 pixels in 
four modes.
Downloaded from https://www.science.org at National University of Defense Technology on December 31, 2025

Lu et al., Sci. Adv. 10, eadp0174 (2024)     4 September 2024
S c i e n c e  A d va n c e s  | R e s e a r c h  A r t i c l e
7 of 10
detect the dynamic targets with clear contours, whereas the noise 
points in the extracted images are dispersed because of the low-­
speed noise generated by background objects. To tackle this issue, 
we use a smoothing convolution kernel to reduce the noise intensity 
and then filter it using a ferroelectric ST. This strategy effectively 
eliminates ambient noise while preserving the clarity and integrity 
of the dynamic object (fig. S30). Subsequently, each acquired frame 
is vertically compressed into 1D vectors. These vectors are then 
stacked in temporal order to form a 2D feature matrix. This method 
fuses the spatial and temporal features of the moving targets and 
reduces the amount of data by nearly 99.99%, thus reducing the 
computational burden on the subsequently used NNs. Our digital 
framework uses parallel computation, which guarantees a processing 
speed much higher than the frame interval of 0.033 s. During pro-
cessing, we reuse the ferroelectric hardware so that only 720 XNOR 
units are required for the differential frames of two 1920 × 720–pixel 
images, which significantly reduces the circuit area. Third, we con-
struct a highly compact convolutional NN with only three convolu-
tional layers (CLs) and one fully connected (FC) layer for accurately 
recognizing the trajectories of pedestrians (fig. S31). The CLs take 
the feature fusion maps as input and extract the valid information 
hidden in them, and then an FC layer is applied to combine the key 
features through nonlinear functions. Fourth, a Softmax function is 
used in the final stage to ascertain the probability distribution for 
predicting the direction of motion in the output layer. Figure 5C 
illustrates the entire computational process when using a feature 
10−3
10−2
10−1
100
101
102
Power efficiency (TOPS/W)
CPU
GPU
This work
0.0095
0.1
26.3
263×
2768×
Judgement
Convolution for feature extraction
Feature maps
X ij,1
X ij,2
STmn
XNORmn
Kernelmn
Digital
Analog
X ij,30
X ij,31
Analog
Computation
Digital
Computation
Video
Input
Path
Tracking
A
B
C
D
E
F
CL
CL
CL
FC layer
R
L
S
A
W
R
L
S
A
W
Dynamic detection
Smoothing
Filtering
Fig. 5. 2D hybrid CIM system for DOT. (A) Computing flowchart for path tracking based on the customized 2D fully ferroelectric-­gated hybrid CIM system. (B) Demon-
stration of the digital computation based on ferroelectric XNOR, smoothing convolution kernel, and ST arrays for pedestrian detection and noise filtering. (C) Demonstra-
tion of the analog computation in a four-­layer convolutional NN (CNN) based on ferroelectric MSC arrays for feature extraction and prediction. (D) The weight distributions 
of 590 ferroelectric MSCs in the highly compact CNN. (E) Power consumption comparison between traditional silicon-­based hybrid circuits (CPU and GPU) and our 2D 
fully ferroelectric-­gated hybrid CIM system. (F) Confusion matrix with an average accuracy of 99.8%.
Downloaded from https://www.science.org at National University of Defense Technology on December 31, 2025

Lu et al., Sci. Adv. 10, eadp0174 (2024)     4 September 2024
S c i e n c e  A d va n c e s  | R e s e a r c h  A r t i c l e
8 of 10
map of rightward motion as the input. Our system ultimately pro-
vides a moving direction recognition of the pedestrian based on the 
maximum output probability.
By integrating hybrid ferroelectric hardware, our system strikes a 
balance between digital and analog computing, which ensures a 
highly efficient CIM platform with both high accuracy and energy 
efficiency. On the one hand, deep NNs like the recurrent NN (RNN) 
or long short-­term memory (LSTM) network used for video pro-
cessing are generally based on traditional analog computing chips, 
which involve the deployment of tens of thousands or even millions 
of weight vectors, placing tremendous pressure on limited comput-
ing resources (55). In contrast, with parallel logical operations for 
accurate processing, our network uses only 590 weight-­related pa-
rameters, which greatly simplifies the architecture of the NN. On 
the other hand, although traditional silicon-­based computational 
approaches integrate digital preprocessing with analog NNs, the in-
dividual devices used in them lack nonvolatile data storage capabil-
ity which leads to the consumption of a large amount of energy for 
extensive data transfers and repeat write/read operations. Differ-
ently, our methodology separates the write and read operations, by 
which the weight distribution in our framework is written only once 
on the basis of the nonvolatile MSCs. As shown in Fig. 5D, the MSC 
arrays lastly exhibit a concentrated distribution of weights near zero 
(fig. S32) at which state the minimum programming energy of only 
0.03 fJ is consumed (56). As a result, our highly compact 2D ferro-
electric hybrid computational setup exhibits a 2768-­fold and a 263-­
fold improvement in energy efficiency compared to Intel 12th Gen 
i9-­12900K CPU and NVIDIA Tesla V100 GPU, respectively (Fig. 5E 
and text S3) (57–59). Moreover, on the basis of the self-­established 
test datasets, this proposed hybrid system lastly predicts the pedes-
trians’ motion paths with an extremely high overall accuracy of 
99.8% (Fig. 5F), corresponding to the five typical motion directions 
of going right (R), going left (L), stopping (T), approaching (A), and 
withdrawing (W), respectively. Note that this system can also imple-
ment constant path tracking with an impressive accuracy of 100%, 
which may pave the way for real-­time DOT (fig. S33).
DISCUSSION
We have developed a solution-­processable methodology facilitating 
the fabrication of MoS2-­FeFETs with a high on/off ratio (>107), supe-
rior endurance (>1012), long memory retention (>10 years), and low 
CtC/DtD variations (~0.3%/~0.5%) at a wafer-­scale yield of 96.36%. 
By using these remarkable FeFETs as fundamental units, we devel-
oped ferroelectric reconfigurable Boolean logic gates and triggers to 
form digital processing arrays that boast compact circuitry and ex-
ceptionally low power consumption, down to 3 fJ/bit. In addition, we 
have implemented parallel VMM based on ferroelectric MSC arrays. 
This technique allows the programming of ferroelectric MSCs with a 
highly symmetric and linear conductance response of up to 90 states, 
achieving a minimal power consumption of 0.03 fJ. Subsequently, we 
customized a 2D hybrid CIM system that integrates ferroelectric-­
gated digital processing units with analog computing hardware, 
demonstrating its applications in DOT. In comparison with analog 
computing chips and traditional silicon-­based hybrid computing 
hardware, this 2D fully ferroelectric-­gated hybrid CIM system offers 
significant advantages in terms of high accuracy, power efficiency, 
speed, and small circuitry, presenting a versatile strategy for a wide 
range of AI applications.
MATERIALS AND METHODS
Fabrication of 2D fully ferroelectric-­gated hybrid platform
We fabricated FeFETs with an MFMIS structure on SiO2/Si sub-
strates in six lithographic steps. First, 40-­nm TiN was sputtered 
(KJLC Lab18, K. J. Lesker) on a patterned double-­layer photoresis-
tor as the BG, followed by liftoff. Second, a 20-­nm HZO layer was 
deposited by using ALD based on tetrakis(ethylmethylamido)
hafnium [Hf(NCH3C2H5)4], tetrakis(ethylmethylamido)zirconium 
[Zr(NCH3CH5)4], and deionized water at 200°C. After this, it 
was patterned with inductively coupled plasma (ICP) etching (NE-­
550H, ULVAC) by using Cl2 and BCl3. Repeatedly, the gate stacks 
of TiN/HZO/TiN/HfOx were constructed in the first four steps, 
during which the TiN/HZO/TiN capacitor was sent to a furnace 
for RTA at 500°C for 30 s in an N2 atmosphere to induce the fer-
roelectricity of HZO at the third step. Fifth, MoS2 film was depos-
ited by using the two-­step spin-­coating method (1000 rpm, 3 s, and 
2000 rpm, 30 s). This was followed by annealing and ICP etching 
(GSE200S, NMC) of MoS2 by using SF6. Sixth, we deposited a 3-­nm 
adhesive Ti layer along with 50-­nm Pd electrodes as the S/D by us-
ing E-­beam evaporation. As for the CIM array, the four WLs were 
sputtered at first. Differently, after TiN/HZO/TiN/HfOx stacks, 
the four SLs were deposited parallel to the WLs before depositing 
an insulating layer of HfOx. Four patterned DLs were lastly sput-
tered following the deposition of the MoS2 films.
Characterizations
All the characteristics were measured at room temperature. The 
P-­EF characteristics of the TiN/HZO/TiN capacitors were mea-
sured with a ferroelectric analyzer (Multiferroic II, Radiant Tech). 
The electrical performance of the FeFETs and arrays was measured 
by using a semiconductor parameter analyzer (Agilent B1500A) 
and a waveform generator (DG4102, RIGOL). Optical images were 
captured with a microscope. The UV-­vis spectrum was obtained 
on a spectrophotometer (U-­3900, HITACHI), while the Raman 
spectra and PL spectroscopy were examined on a HORIBA Raman 
microscope with an excitation wavelength of 532 nm and a 50× 
objective. XRD was conducted with a Panalytical X’Pert Pro X-­ray 
Powder Diffractometer. STEM and EELS were carried out under 
an aberration-­corrected electron microscope (Thermo Fisher Scientific, 
Titan Cubed Themis G2) at 300 kV by using an electron gun with 
a high brightness (X-­FEG with monochromator).
Supplementary Materials
This PDF file includes:
Supplementary Text S1 to S3
Figs. S1 to S33
Tables S1 and S2
REFERENCES AND NOTES
	 1.	 W. A. Wulf, S. A. McKee, Hitting the memory wall: Implications of the obvious. ACM 
SIGARCH Comput. Archit. News 23, 20–24 (1995).
	 2.	 S. W. Keckler, W. J. Dally, B. Khailany, M. Garland, D. Glasco, GPUs and the future of parallel 
computing. IEEE Micro 31, 7–17 (2011).
	 3.	 Z. Sun, S. Kvatinsky, X. Si, A. Mehonic, Y. Cai, R. Huang, A full spectrum of computing-­in-­
memory technologies. Nat. Electron. 6, 823–835 (2023).
	 4.	 Y. Zhong, J. Tang, X. Li, X. Liang, Z. Liu, Y. Li, Y. Xi, P. Yao, Z. Hao, B. Gao, H. Qian, H. Wu, A 
memristor-­based analogue reservoir computing system for real-­time and power-­efficient 
signal processing. Nat. Electron. 5, 672–681 (2022).
	 5.	 S. Bhatti, R. Sbiaa, A. Hirohata, H. Ohno, S. Fukami, S. N. Piramanayagam,  
Spintronics based random access memory: A review. Mater. Today 20, 530–548 
(2017).
Downloaded from https://www.science.org at National University of Defense Technology on December 31, 2025

Lu et al., Sci. Adv. 10, eadp0174 (2024)     4 September 2024
S c i e n c e  A d va n c e s  | R e s e a r c h  A r t i c l e
9 of 10
	 6.	 R. Chen, Z. Fang, F. Miller, H. Rarick, J. E. Fröch, A. Majumdar, Opportunities and 
challenges for large-­scale phase-­change material integrated electro-­photonics. ACS 
Photonics 9, 3181–3195 (2022).
	 7.	 E. J. Fuller, S. T. Keene, A. Melianas, Z. Wang, S. Agarwal, Y. Li, Y. Tuchman, C. D. James,  
M. J. Marinella, J. J. Yang, A. Salleo, A. A. Talin, Parallel programming of an ionic 
floating-­gate memory array for scalable neuromorphic computing. Science 364, 570–574 
(2019).
	 8.	 H. Mulaosmanovic, E. T. Breyer, S. Dunkel, S. Beyer, T. Mikolajick, S. Slesazeck, Ferroelectric 
field-­effect transistors based on HfO2: A review. Nanotechnology 32, 502002 (2021).
	 9.	 A. Sebastian, M. Le Gallo, R. Khaddam-­Aljameh, E. Eleftheriou, Memory devices and 
applications for in-­memory computing. Nat. Nanotechnol. 15, 529–544 (2020).
	10.	 A. Momeni, B. Rahmani, M. Malléjac, P. del Hougne, R. Fleury, Backpropagation-­free 
training of deep physical neural networks. Science 382, 1297–1303 (2023).
	11.	 X. Geng, J. Gao, Y. Zhang, D. Xu, Complex hybrid weighted pruning method for 
accelerating convolutional neural networks. Sci. Rep. 14, 1–11 (2024).
	12.	 S. R. Kamalakara, A. Locatelli, B. Venkitesh, J. Ba, Y. Gal, A. N. Gomez, Exploring low rank 
training of deep neural networks. arXiv:2209.13569 (2022).
	13.	 C. Wu, F. Wu, L. Lyu, Y. Huang, X. Xie, Communication-­efficient federated learning via 
knowledge distillation. Nat. Commun. 13, 1–7 (2022).
	14.	 M. R. H. Rashed, S. K. Jha, R. Ewetz, Hybrid analog-­digital in-­memory computing, in 2021 
IEEE/ACM International Conference On Computer Aided Design (ICCAD) (IEEE, 2021),  
pp. 1–9.
	15.	 M. Seol, M. H. Lee, H. Kim, K. W. Shin, Y. Cho, I. Jeon, M. Jeong, H. I. Lee, J. Park, H. J. Shin, 
High-­throughput growth of wafer-­scale monolayer transition metal dichalcogenide via 
vertical ostwald ripening. Adv. Mater. 32, e2003542 (2020).
	16.	 P. C. Shen, Y. Lin, C. Su, C. McGahan, A. Y. Lu, X. Ji, X. Wang, H. Wang, N. Mao, Y. Guo,  
J. H. Park, Y. Wang, W. Tisdale, J. Li, X. Ling, K. E. Aidala, T. Palacios, J. Kong, Healing of 
donor defect states in monolayer molybdenum disulfide using oxygen-­incorporated 
chemical vapour deposition. Nat. Electron. 5, 28–36 (2022).
	17.	 H. Liu, L. Chen, H. Zhu, Q. Q. Sun, S. J. Ding, P. Zhou, D. W. Zhang, Atomic layer deposited 
2D MoS2 atomic crystals: From material to circuit. Nano Res. 13, 1644–1650 (2020).
	18.	 D. K. Singh, G. Gupta, van der Waals epitaxy of transition metal dichalcogenides via 
molecular beam epitaxy: Looking back and moving forward. Mater. Adv. 3, 6142–6156 
(2022).
	19.	 Z. Lin, Y. Liu, U. Halim, M. Ding, Y. Liu, Y. Wang, C. Jia, P. Chen, X. Duan, C. Wang, F. Song,  
M. Li, C. Wan, Y. Huang, X. Duan, Solution-­processable 2D semiconductors for 
high-­performance large-­area electronics. Nature 562, 254–258 (2018).
	20.	 Y. Li, K. A. N. Duerloo, K. Wauson, E. J. Reed, Structural semiconductor-­to-­semimetal phase 
transition in two-­dimensional materials induced by electrostatic gating. Nat. Commun. 7, 
1–8 (2016).
	21.	 Z. Zeng, Z. Yin, X. Huang, H. Li, Q. He, G. Lu, F. Boey, H. Zhang, Single-­layer 
semiconducting nanosheets: High-­yield preparation and device fabrication. Angew. 
Chem. Int. Ed. Engl. 50, 11093–11097 (2011).
	22.	 T. Carey, O. Cassidy, K. Synnatschke, E. Caffrey, J. Garcia, S. Liu, H. Kaur, A. G. Kelly,  
J. Munuera, C. Gabbett, D. O’Suilleabhain, J. N. Coleman, High-­mobility flexible transistors 
with low-­temperature solution-­processed tungsten dichalcogenides. ACS Nano 17, 
2912–2922 (2023).
	23.	 H. S. Lee, S. W. Min, M. K. Park, Y. T. Lee, P. J. Jeon, J. H. Kim, S. Ryu, S. Im, MoS2 nanosheets 
for top-­gate nonvolatile memory transistor channel. Small 8, 3111–3115 (2012).
	24.	 B. Tang, H. Veluri, Y. Li, Z. G. Yu, M. Waqar, J. F. Leong, M. Sivan, E. Zamburg, Y. W. Zhang,  
J. Wang, A. V. Y. Thean, Wafer-­scale solution-­processed 2D material analog resistive 
memory array for memory-­based computing. Nat. Commun. 13, 1–9 (2022).
	25.	 P. Luo, C. Liu, J. Lin, X. Duan, W. Zhang, C. Ma, Y. Lv, X. Zou, Y. Liu, F. Schwierz, W. Qin,  
L. Liao, J. He, X. Liu, Molybdenum disulfide transistors with enlarged van der Waals  
gaps at their dielectric interface via oxygen accumulation. Nat. Electron. 5, 849–858 
(2022).
	26.	 T. Lu, X. Zhao, H. Liu, Z. Yan, R. Zhao, M. Shao, J. Yan, M. Yang, Y. Yang, T.-­L. Ren, Optimal 
weight models for ferroelectric synapses toward neuromorphic computing. IEEE Trans. 
Electron Devices 1, 1–7 (2023).
	27.	 J. Sun, Y. Li, L. Cao, J. Liu, X. Shi, L. Tian, Effects of area ratio on the characteristics of 
metal-­ferroelectric-­metal-­insulator-­semiconductor field-­effect-­transistors (MFMIS FETs). 
Integr. Ferroelectr. 201, 183–191 (2019).
	28.	 A. Keshavarzi, K. Ni, W. Van Den Hoek, S. Datta, A. Raychowdhury, FerroElectronics for 
edge intelligence. IEEE Micro 40, 33–48 (2020).
	29.	 T. Paul, T. Ahmed, K. Kanhaiya Tiwari, C. Singh Thakur, A. Ghosh, A high-­performance 
MoS2 synaptic device with floating gate engineering for neuromorphic computing. 2D 
Mater. 6, 045008 (2019).
	30.	 K. H. Kim, S. Oh, M. M. A. Fiagbenu, J. Zheng, P. Musavigharavi, P. Kumar, N. Trainor,  
A. Aljarb, Y. Wan, H. M. Kim, K. Katti, S. Song, G. Kim, Z. Tang, J. H. Fu, M. Hakami, V. Tung,  
J. M. Redwing, E. A. Stach, R. H. Olsson, D. Jariwala, Scalable CMOS back-­end-­of-­line-­
compatible AlScN/two-­dimensional channel ferroelectric field-­effect transistors. Nat. 
Nanotechnol. 18, 1044–1050 (2023).
	31.	 M. Jerry, S. Dutta, A. Kazemi, K. Ni, J. Zhang, P. Y. Chen, P. Sharma, S. Yu, X. S. Hu,  
M. Niemier, S. Datta, A ferroelectric field effect transistor based synaptic weight cell.  
J. Phys. D Appl. Phys. 51, 434001 (2018).
	32.	 S. H. Tsai, Z. Fang, X. Wang, U. Chand, C. K. Chen, S. Hooda, M. Sivan, J. Pan, E. Zamburg,  
A. V. Y. Thean, Stress-­memorized HZO for high-­performance ferroelectric field-­effect 
memtransistor. ACS Appl. Electron. Mater. 4, 1642–1650 (2022).
	33.	 Y. Sun, N. He, Y. Wang, Q. Yuan, D. Wen, Multilevel memory and artificial synaptic  
plasticity in P(VDF-­TrFE)-­based ferroelectric field effect transistors. Nano Energy 98, 
107252 (2022).
	34.	 X.-­W. Zhang, D. Xie, J.-­L. Xu, Y.-­L. Sun, X. Li, C. Zhang, R.-­X. Dai, Y.-­F. Zhao, X.-­M. Li, X. Li, 
H.-­W. Zhu, MoS2 field-­effect transistors with lead zirconate-­titanate ferroelectric gating. 
IEEE Electron Device Lett. 35, 599–601 (2014).
	35.	 T. Kobayashi, N. Hori, T. Nakajima, T. Kawae, Electrical characteristics of MoS2 field-­effect 
transistor with ferroelectric vinylidene fluoride-­trifluoroethylene copolymer gate 
structure. Appl. Phys. Lett. 108, 132903 (2016).
	36.	 K. Huang, M. Zhai, X. Liu, B. Sun, H. Chang, J. Liu, C. Feng, H. Liu, Hf₀.₅Zr₀.₅O₂ ferroelectric 
embedded dual-­gate MoS₂ field effect transistors for memory merged logic applications. 
IEEE Electron Device Lett. 41, 1600–1603 (2020).
	37.	 S. Zhang, Y. Liu, J. Zhou, M. Ma, A. Gao, B. Zheng, L. Li, X. Su, G. Han, J. Zhang, Y. Shi,  
X. Wang, Y. Hao, Low voltage operating 2D MoS2 ferroelectric memory transistor with 
Hf1-­xZrxO2 gate structure. Nanoscale Res. Lett. 15, 1–9 (2020).
	38.	 J. Xiang, W. H. Chang, T. Saraya, T. Hiramoto, T. Irisawa, M. Kobayashi, Experimental 
demonstration of HfO2-­based ferroelectric FET with MoS2 channel for high-­density and 
low-­power memory application, in 2021 Silicon Nanoelectronics Workshop (IEEE, 2021),  
pp. S3–S2.
	39.	 X. Liu, D. Wang, K. H. Kim, K. Katti, J. Zheng, P. Musavigharavi, J. Miao, E. A. Stach,  
R. H. Olsson, D. Jariwala, Post-­CMOS compatible aluminum scandium nitride/2D channel 
ferroelectric field-­effect-­transistor memory. Nano Lett. 21, 3753–3761 (2021).
	40.	 M. Le Gallo, A. Sebastian, R. Mathis, M. Manica, H. Giefers, T. Tuma, C. Bekas, A. Curioni,  
E. Eleftheriou, Mixed-­precision in-­memory computing. Nat. Electron. 1, 246–253  
(2018).
	41.	 E. T. Breyer, H. Mulaosmanovic, J. Trommer, T. Melde, S. Dunkel, M. Trentzsch, S. Beyer,  
S. Slesazeck, T. Mikolajick, Compact FeFET circuit building blocks for fast and efficient 
nonvolatile logic-­in-­memory. IEEE J. Electron Devices Soc. 8, 748–756 (2020).
	42.	 C. Marchand, I. O’Connor, M. Cantan, E. T. Breyer, S. Slesazeck, T. Mikolajick, A FeFET-­based 
hybrid memory accessible by content and by address. IEEE J. Explor. Solid-­State Comput. 
Devices Circuits 8, 19–26 (2022).
	43.	 A. Brunetti, D. Buongiorno, G. F. Trotta, V. Bevilacqua, Computer vision and deep learning 
techniques for pedestrian detection and tracking: A survey. Neurocomputing 300, 17–33 
(2018).
	44.	 K. Cho, J. Park, T. W. Oh, S. O. Jung, One-­sided schmitt-­trigger-­based 9T SRAM cell for 
near-­threshold operation. IEEE Trans. Circuits Syst. I: Regul. Pap. 67, 1551–1561 (2020).
	45.	 P. Sharma, S. Gupta, K. Gupta, N. Pandey, A low power subthreshold Schmitt Trigger 
based 12T SRAM bit cell with process-­variation-­tolerant write-­ability. Microelectron. J. 97, 
104703 (2020).
	46.	 B. Wang, X. Wang, E. Wang, C. Li, R. Peng, Y. Wu, Z. Xin, Y. Sun, J. Guo, S. Fan, C. Wang,  
J. Tang, K. Liu, Monolayer MoS2 Synaptic transistors for high-­temperature neuromorphic 
applications. Nano Lett. 21, 10400–10408 (2021).
	47.	 M. K. Kim, J. S. Lee, Ferroelectric analog synaptic transistors. Nano Lett. 19, 2044–2050 
(2019).
	48.	 W. Shin, J. H. Bae, D. Kwon, R. H. Koo, B. G. Park, D. Kwon, J. H. Lee, Investigation of 
low-­frequency noise characteristics of ferroelectric tunnel junction: From conduction 
mechanism and scaling perspectives. IEEE Electron Device Lett. 43, 958–961 (2022).
	49.	 F. Xi, A. Grenmy, J. Zhang, Y. Han, J. H. Bae, D. Grutzmacher, Q. T. Zhao, Ferroelectric 
Schottky Barrier MOSFET as analog synapses for neuromorphic computing, in ESSCIRC 
2022-­ IEEE 48th European Solid State Circuits Conference (ESSCIRC) (IEEE, 2022),  
pp. 121–124.
	50.	 M. Si, A. K. Saha, S. Gao, G. Qiu, J. Qin, Y. Duan, J. Jian, C. Niu, H. Wang, W. Wu, S. K. Gupta,  
P. D. Ye, A novel scalable energy-­efficient synaptic device: Crossbar ferroelectric 
semiconductor junction, in 2019 International Electron Devices Meeting (IEEE, 2019),  
pp. 6.6.1–6.6.4.
	51.	 C. P. Chou, Y. X. Lin, Y. K. Huang, C. Y. Chan, Y. H. Wu, Junctionless poly-­GeSn ferroelectric 
thin-­film transistors with improved reliability by interface engineering for neuromorphic 
computing. ACS Appl. Mater. Interfaces 12, 1014–1023 (2020).
	52.	 D. Kim, Y. R. Jeon, B. Ku, C. Chung, T. H. Kim, S. Yang, U. Won, T. Jeong, C. Choi, Analog 
synaptic transistor with Al-­doped HfO2 ferroelectric thin film. ACS Appl. Mater. Interfaces 
13, 52743–52753 (2021).
	53.	 M. K. Kim, I. J. Kim, J. S. Lee, CMOS-­compatible compute-­in-­memory accelerators based 
on integrated ferroelectric synaptic arrays for convolution neural networks. Sci. Adv. 8, 
eabm8537 (2022).
	54.	 K. R. Jadav, A. R. Yadav, Dynamic shadow detection and removal for vehicle tracking 
system. Int. J. Image Graph. 22, 1–17 (2022).
Downloaded from https://www.science.org at National University of Defense Technology on December 31, 2025

Lu et al., Sci. Adv. 10, eadp0174 (2024)     4 September 2024
S c i e n c e  A d va n c e s  | R e s e a r c h  A r t i c l e
10 of 10
	55.	 S. Ahmed, M. N. Huda, S. Rajbhandari, C. Saha, M. Elshaw, S. Kanarachos, Pedestrian and 
cyclist detection and intent estimation for autonomous vehicles: A survey. Appl. Sci. 9, 
2335 (2019).
	56.	 H. Xiang, Y. C. Chien, L. Li, H. Zheng, S. Li, N. T. Duong, Y. Shi, K. W. Ang, Enhancing  
memory window efficiency of ferroelectric transistor for neuromorphic computing  
via two-­dimensional materials integration. Adv. Funct. Mater. 33, 202304657  
(2023).
	57.	 T. Gokmen, Y. Vlasov, Acceleration of deep neural network training with resistive 
cross-­point devices: Design considerations. Front. Neurosci. 10, 1–13 (2016).
	58.	 B. E. Jonsson, Area efficiency of ADC architectures, 2011 20th European Conference on 
Circuit Theory and Design (ECCTD) (IEEE, 2011), pp. 560–563.
	59.	 H. Zhao, Z. Liu, J. Tang, B. Gao, Q. Qin, J. Li, Y. Zhou, P. Yao, Y. Xi, Y. Lin, H. Qian, H. Wu, 
Energy-­efficient high-­fidelity image reconstruction with memristor arrays for medical 
diagnosis. Nat. Commun. 14, 2276 (2023).
Acknowledgments 
Funding: This work was supported in part by the National Natural Science Foundation of 
China (62274101, 61874065, 51861145202, 92364102, and 92264201) received by T.-­L.R. and 
H.L., in part by the National Key R&D Program of China (2021YFC3002200 and 
2020YFA0709800) received by T.-­L.R., in part by JCCDFSIT (2022CDF003) received by H.L., in 
part by QYJS-­2022-­1600-­B received by T.-­L.R., in part by the Beijing National Research Center 
Youth Innovation Foundation (BNR2024RC01002) received by H.L., in part by the Foundation 
of State Key Laboratory of High-­efficiency Utilization of Coal and Green Chemical Engineering 
(2022-­K81) received by J.X, in part by the National Natural Science Foundation of China 
(22275113) received by Z.L., and in part by Beijing Natural Science Foundation (Z240025) and 
Tsinghua University Dushi program received by Z.L. Author contributions: H.L., Y.Y., and T.-­L.R. 
conceived and supervised this project. J.X. and J.H. prepared MoS2 inks and finished related 
material characterizations with guidance from Z.L. X.G. and X.L. prepared the TEM samples and 
completed the analysis with guidance from P.G. T.L. fabricated the ferroelectric hybrid 
hardware and measured the electrical performance with assistance from R.Z., M.Y., and D.H. J.Y. 
finished the SPICE simulation. P.S. constructed the hybrid CIM system with guidance from B.Y. 
T.L., J.X., and P.S. wrote this manuscript. All the authors contributed to discussions. Competing 
interests: The authors declare that they have no competing interests. Data and materials 
availability: All data needed to evaluate the conclusions in the paper are present in the paper 
and/or the Supplementary Materials.
Submitted 21 March 2024 
Accepted 30 July 2024 
Published 4 September 2024 
10.1126/sciadv.adp0174
Downloaded from https://www.science.org at National University of Defense Technology on December 31, 2025

