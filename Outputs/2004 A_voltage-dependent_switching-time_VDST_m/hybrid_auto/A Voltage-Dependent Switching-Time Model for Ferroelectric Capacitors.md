---
title: "A Voltage-Dependent Switching-Time Model for Ferroelectric Capacitors"
authors:
  - "Jeffrey S. Cross"
  - "Ali Sheikholeslami"
  - "Gordon H. Charn"
  - "Shahriar Mirabbasi"
date: "2004-01-01"
year: "2004"
journal: "IEEE International Symposium on Circuits and Systems"
abstract: "The time required to switch a ferroelectric capacitor from one binary state"
abstract_cn: "铁电电容从一个二进制状态切换到另一个状态所需的时间与施加电压的大小密切相关，特别是在远低于电源电压的电压下。本文提出一种 Verilog-A"
keywords:
  - "[[Ferroelectric]]"
cite: "Cross J S, Sheikholeslami A, Charn G H, et al. A voltage-dependent switching-time"
aiSum: "FeRAM 开关时间模型：Verilog-A、电压依赖动态、0.35μm CMOS/PZT、Spectre 仿真验证。"
confidence: "medium"
wiki_concepts:
  - "[[Ferroelectric]]"
---

# Abstract

The time required to switch a ferroelectric capacitor from one binary state to the other is strongly related to the magnitude of the applied voltage, especially at voltages well below the power supply. This paper presents a Verilog-A model that accurately predicts the voltage-dependent switching dynamics of various FeRAM technologies. Spectre simulations of low-voltage FeRAM circuits implemented in a $0.35\mu \mathrm{m}$ CMOS/PZT testchip are in full agreement with our measurement results.

# Introduction

As circuit innovations in ferroelectric random-access memories (FeRAM) target low voltages and low access-times, the switching time of ferroelectric (FE) capacitors becomes all the more critical. Traditionally, circuit simulation models have neglected the switching time [1] [2] in favor of the RC time constant of the circuits involved. This assumption is still valid for voltages near the power supply $(V_{dd})$ , where switching completes in the sub-nanosecond time regime, but becomes invalid for smaller applied voltages (less than $V_{dd} / 2$ ) where switching can take up to one second.

To demonstrate the effect of voltage-dependent switching, we apply a 1.8V step to the plateline (PL) of a 1T-1C cell that uses $V_{dd} = 3\mathrm{V}$ , as shown in Fig. 1. The bitline (BL) voltage rises to its final value in less than 50ns if a zero-switching time is assumed, but remains substantially below the final value if the switching time is taken into account.

Previous attempts at incorporating the switching time either target a particular technology [3] or target FE capacitors as stand-alone elements [4]. This paper presents a dynamic model that is adaptable to various technologies and applicable to FE capacitors in any circuit topology. We demonstrate the model's accuracy through the comparison of simulations and measurements obtained from a $0.35\mu \mathrm{m}$ CMOS/PZT FeRAM testchip and successfully apply the model to the analysis of low-voltage FeRAM circuits.

# Voltage-Dependent Switching Time (VDST) Model

The VDST model is composed of a dynamic and static portion as depicted in Fig. 2. The dynamic portion models the switching delay of the FE capacitor by delaying $V_{in}$ through a set of time constants $(\tau_{i})$ to produce a corresponding set of $V_{eff_{i}}$ . A weighted sum of $V_{eff_{i}}$ is then applied to the static portion [1] to determine the charge, $Q(V_{eff})$ . Mathematically,

$$
V _ {e f f} (t) = \mu_ {l} V _ {e f f l} (t) + \mu_ {2} V _ {e f f 2} (t) + \dots + \mu_ {n} V _ {e f f n} (t) \tag {1}
$$

where $\mu_{l} + \mu_{2} + \ldots + \mu_{n} = 1$ , and each $V_{\text{eff}_i}$ is governed by

$$
d V _ {\text {e f f i}} (t) / d t = \left(V _ {\text {i n}} (t) - V _ {\text {e f f i}} (t)\right) / \tau_ {i} \tag {2}
$$

$$
\tau_ {i} \left(V _ {\text {p u l s e} i}\right) = \tau_ {\infty} \exp \left(\left(V _ {o _ {i}} / V _ {\text {p u l s e} i}\right) ^ {m}\right) \tag {3}
$$

$$
V _ {\text {p u l s e} i} \left(V _ {\text {e f f} i}\right) = V _ {i n} - c _ {i} - k _ {i} \left(V _ {\text {e f f} i} - c _ {i}\right) ^ {x} \tag {4}
$$

where $i = \{1,2,\dots,n\}$ , $k_{i} = (V_{in} - c_{i})^{-(x - 1)}$ and $c_{i}$ is $V_{effi}$ at the last change of $V_{in}$ such that the boundary conditions $V_{pulse_i}(c_i) = V_{in} - c_i$ and $V_{pulse_i}(V_{in}) = 0$ are met. Eq. (1)-(4) are implemented in Verilog-A and integrated into Spectre [5]. The implementation using Verilog-A achieves the same accuracy as an implementation using circuit elements, but

with a 20-fold reduction in simulation time.

Fig. 3 shows a depiction of (3) and (4) and the role of $x$ in characterizing the switching behavior of various FeRAM technologies. $V_{\text{eff}_i}$ is initially at $V_{\text{eff}_i@t_0}$ , which corresponds to a small switching time constant $(\tau_i@t_0)$ . As $V_{\text{eff}_i}$ increases with time and approaches $V_{\text{in}}$ , $\tau_i$ dynamically increases to mimic the switching delay of the FE capacitor.

The parameter $x$ controls the rate of increase of $\tau_{i}$ and can be calibrated to match the switching dynamics of a particular technology. For $x = 1$ , $V_{\text{pulse}_i} = V_{in} - V_{\text{eff}_i}$ , and the model degenerates to [3]. As $V_{\text{eff}_i}$ approaches $V_{in}$ , $V_{\text{pulse}_i}$ decreases linearly, thus increasing $\tau_{i}$ exponentially. This results in a slow switching characteristic consistent with a $0.5\mu \text{m}$ PZT technology. For $x = 2$ , $V_{\text{pulse}_i}$ decreases at a slower rate, thus holding $\tau_{i}$ at a smaller value. This results in a faster switching characteristic resembling that of a $0.35\mu \text{m}$ PZT technology.

To verify this analysis, the circuit in Fig. 4(a) is used to generate the switching curves (switching charge vs. time) of a FE capacitor for applied voltage steps of 1.5V, 2V, and 3V [4]. P1 defines the initial state of the capacitor, P2 reverses the polarization for various $t_2$ and $\nu_2$ , and P3 measures the result. Fig. 4(b) and 4(c) show the measured switching curves of a $0.5\mu \mathrm{m}$ $(V_{dd} = 5\mathrm{V})$ and $0.35\mu \mathrm{m}$ $(V_{dd} - 3\mathrm{V})$ PZT FE capacitor [6] and simulated results for $x = 1$ and $x = 2$ , respectively. The results are in close agreement and confirm the VDST model's adaptability to various FeRAM technologies.

Fig. 5 shows the $0.35\mu \mathrm{m}$ CMOS/PZT FeRAM testchip layout [7] used for simulation and measurement purposes, which utilizes a supply voltage of $3\mathrm{V}$ . To exaggerate the effect of voltage-dependent switching, we reduce $V_{dd}$ to $1.8\mathrm{V}$ and observe the simulated BL voltage development with time for a conventional step-sensing read scheme [8]. Fig. 6 shows the expected gradual increase of $V_{BL0}$ and $V_{BL1}$ due to the large switching time of the FE capacitor at small applied voltages, a trend consistent with our measurement results.

# Application to Low-Voltage FeRAM Circuits

FeRAM circuits experience smaller applied voltages due to supply-voltage scaling and voltage division in circuits containing FE capacitors in series. An example of the latter is the reference generation circuit proposed in [7] that uses four FE capacitors to provide an equivalent capacitance of $C_{\text{ref}} = (C_0 + C_1) / 2$ , where $C_0$ and $C_1$ are the nominal capacitances of a stored '0' and stored '1', respectively, as shown in Fig. 7. Due to the series combination of FE capacitors, each capacitor experiences only half of the reference BL voltage $(V_{BLref})$ instead of the full voltage, causing these capacitors to switch slower than the cell capacitor. Simulations using a model that neglects the switching time predict correct functionality of the reference capacitor [7]. The measurement results, however, indicate that the testchip always outputs a '1' regardless of the stored data. Simulations using the VDST model, calibrated to the $0.35\mu \text{m}$ discrete PZT sample in Fig. 4(c), successfully reproduce this behavior by showing that $V_{BLref}$ is larger than both $V_{BL0}$ and $V_{BL1}$ , as shown in Fig. 8.

# Conclusion

The VDST model successfully incorporates the voltage-dependent switching of FE capacitors for circuit simulations of low-voltage FeRAM circuits. The model accurately predicts measurement results obtained from a $0.35\mu \mathrm{m}$ CMOS/PZT FeRAM testchip.

# Acknowledgments

The authors thank S. Kawashima of Fujitsu Labs, Y. Eslami of the University of Toronto, and I. Stolichnov of EPFL for their insightful comments, and A. Itoh of Fujitsu Labs for his contributions to data measurement. The authors also thank Fujitsu Labs of Japan and NSERC of Canada for their generous funding.

# References

[1] B. Jiang et al., Symp. VLSI Technology, pp. 141-142, June 1997.   
[2] A. Shcikholeslami et al., IEEE Trans. UFFC, pp. 784-791, July 2000.   
[3] C. Kuhn et al., Symp. Appl. Ferroelectrics, pp. 695-698, Aug. 2000.   
[4] A. Tagantsev et al., Phys. Rev. B, vol. 66, pp. 214109-1-6, Dec. 2002.   
[5] Affirma Spectre Circuit Simulator Reference, Dec. 1999.   
[6] I. Stolichnov et al., Appl. Phys. Lett., vol. 83, pp. 3362-3364, Oct. 2003.   
[7] Y. Eslami et al., Symp. VLSI Circuits, pp. 298-301, June 2002.   
[8] A. Sheikholcslami et al., Proc. of IEEE, pp. 667-689, May 2000.

![](images/bce3b35f906d0da70b77dc23bbfefe56476a97bd802463def04e3243bc863dc5.jpg)  
Fig. 1: Assuming zero switching time (i.e. solely relying on the RC time constant of the circuit) erroneously reveals a fast-rising bitline.

![](images/623b225eaad04cd992508df1ce41376ad64771465e83cb9dac3b3fc1d0c5b349.jpg)  
Fig. 2: $V_{\mathrm{in}}$ is delayed through a set of time constants $(\tau_{\mathrm{j}})$ to model the switching delay of the FE capacitor. The resulting effective voltage $(V_{\mathrm{eff}})$ is applied to a static model to determine the charge.

![](images/c3b8eb939ca23883033c434abc4a7d823de6378433eb121e4c121614ef73f2f2.jpg)  
Fig. 3: Switching time $(\tau_{\mathrm{j}})$ dynamically increases with time as $V_{\mathrm{eff}}$ approaches $V_{\mathrm{in}}$ . The rate of increase is controlled by $x$ in (4).

![](images/cba5730886d7d6c8d49bacfc39101ce37e610180363839ece2b9d6fa93584575.jpg)

![](images/07fa837dbcd04bac6464fdc02e3d1e3fc7eaf0779b6cc9e8b51daff42d8b39ed.jpg)

![](images/128f8ace5effffb0fb4e11082493b0fed346c83de38b835e2c7e5e12e87300a2.jpg)

![](images/e23b16a0b0f0068b6fadf68354fda8d97182de6c1596c8b5562722b129d041e3.jpg)  
Fig. 4: (a) P1 sets the initial state of the capacitor, P2 switches the polarization, and P3 measures the result. Measured data points [6] vs. simulated switching curves for (b) $0.5\mu \mathrm{m}$ and (c) $0.35\mu \mathrm{m}$ P2T capacitors.

![](images/3576ee45b0d9cde04e1afb6d25fc80e6e642b6d759f123f2be593b4f7a0c886b.jpg)  
Fig. 5: Differential Capacitance Read Scheme (DCRS) testchip [7] is used to collect measurement data.

![](images/1c4b57943a1e41a9aed44d8ae7f609f8b305faacb9af0a5af89a4b817937737a.jpg)  
Fig. 6: Simulated bitline voltages for a step-sensing read scheme [8] at a reduced supply voltage of 1.8V.

![](images/d96f551f34025e6e9d2a1fad0db587615cad4a8ba06c4f5a6ce748c52ebd7d81.jpg)  
Fig. 7: Reference capacitor for DCRS $(C_{\text{ref}})$ [7] is theoretically the average of $C_0$ and $C_1$ . However, the actual $C_{\text{ref}}$ is much smaller. See Fig. 8.

![](images/1d45d7df52b198d6b726d875369ba15a610d407e558f96866f632724249a6f72.jpg)

![](images/f3bbf67d7782df5f98f2d4709271040658b12a740e589639aaa0f38f0e4a13e7.jpg)  
Fig. 8: (a) Simulation and (b) measurement results of DCRS circuit of Fig. 7. The VDST model accurately predicts that $V_{BLref}$ is larger than both $V_{BL0}$ and $V_{BL1}$ .