---
title: "Mechanisms of memory-supporting neuronal dynamics in hippocampal area CA3"
authors:
  - "Yiding Li"
  - "John J. Briguglio"
  - "Sandro Romani"
  - "Jeffrey C. Magee"
date: "2024-09-26"
year: "2024"
journal: "Cell"
doi: "10.1016/j.cell.2024.09.041"
abstract: "Hippocampal CA3 is central to memory formation and retrieval. Using intracellular\
  \ recordings and optogenetic manipulations in behaving mice, we found that CA3 place-field\
  \ activity is produced by a symmetric form of behavioral timescale synaptic plasticity\
  \ (BTSP) at recurrent synapses among CA3 pyramidal neurons. Excitatory input from\
  \ the entorhinal cortex was required to update place cell activity based on the\
  \ animal’s movement. These data were captured by a computational model that used\
  \ BTSP and an external updating input to produce attractor dynamics under online\
  \ learning conditions."
abstract_cn: "海马 CA3 是记忆形成和提取的核心区域。通过在小鼠行为过程中进行膜电位记录和光遗传操作，发现 CA3 位置野活动由 CA3 锥体神经元之间循环突触上的对称性行为时间尺度突触可塑性\
  \ (BTSP) 产生，而非齿状回输入。内嗅皮层兴奋性输入负责根据动物运动更新位置细胞活动。计算模型用 BTSP 和外部更新输入实现了在线学习条件下的吸引子动力学。"
keywords:
  - "[[Hippocampus]]"
  - "[[CA3]]"
  - "[[Memory formation]]"
  - "[[Synaptic plasticity]]"
  - "[[Attractor dynamics]]"
cite: "[1] Li Y D, Briguglio J J, Romani S, et al. Mechanisms of memory-supporting neuronal\
  \ dynamics in hippocampal area CA3[J]. Cell, 2024, 187(19): 5265-5279. DOI: 10.1016/j.cell.2024.09.041."
aiSum: "通过膜电位记录和光遗传操作揭示 CA3 位置野活动由循环突触上的对称性 BTSP 产生，内嗅皮层输入负责更新位置细胞活动，计算模型实现吸引子动力学，理论分析表明网络具有优越的记忆存储容量。"
confidence: "high"
wiki_concepts:
  - "[[Hippocampus]]"
---

# Mechanisms of memory-supporting neuronal dynamics in hippocampal area CA3

![](images/a501321bc4e5c4882bbd1b1d6b72d299c6a99291677130494e2f6ec21ed05cb1.jpg)  
Graphical abstract

# Authors

Yiding Li, John J. Briguglio, Sandro Romani, Jeffrey C. Magee

# Correspondence

romanis@janelia.hhmi.org (S.R.), jcmagee@bcm.edu (J.C.M.)

# In brief

Evidence from behaving mice points to cellular and circuit mechanisms that underlie observed attractor dynamics in hippocampal area CA3.

# Highlights

d CA3 intracellular $\mathsf { v } _ { \mathsf { m } }$ recordings and optogenetic manipulations in behaving mice   
d Symmetric BTSP at CA3-CA3 recurrent synapses builds attractor dynamics within CA3   
d External EC inputs update the CA3 attractor dynamics in accordance with behavior   
d A neuronal network built by BTSP possesses superior memory storage capacity

# Article

# Mechanisms of memory-supporting neuronal dynamics in hippocampal area CA3

Yiding Li,1 John J. Briguglio,2 Sandro Romani,2,* and Jeffrey C. Magee1,3,*

1Howard Hughes Medical Institute, Baylor College of Medicine, Houston, TX 77030, USA

2Howard Hughes Medical Institute, Janelia Research Campus, Ashburn, VA 20147, USA

3Lead contact

*Correspondence: romanis@janelia.hhmi.org (S.R.), jcmagee@bcm.edu (J.C.M.)

https://doi.org/10.1016/j.cell.2024.09.041

# SUMMARY

Hippocampal CA3 is central to memory formation and retrieval. Although various network mechanisms have been proposed, direct evidence is lacking. Using intracellular $\mathsf { v } _ { \mathsf { m } }$ recordings and optogenetic manipulations in behaving mice, we found that CA3 place-field activity is produced by a symmetric form of behavioral timescale synaptic plasticity (BTSP) at recurrent synapses among CA3 pyramidal neurons but not at synapses from the dentate gyrus (DG). Additional manipulations revealed that excitatory input from the entorhinal cortex (EC) but not the DG was required to update place cell activity based on the animal’s movement. These data were captured by a computational model that used BTSP and an external updating input to produce attractor dynamics under online learning conditions. Theoretical analyses further highlight the superior memory storage capacity of such networks, especially when dealing with correlated input patterns. This evidence elucidates the cellular and circuit mechanisms of learning and memory formation in the hippocampus.

# INTRODUCTION

The mammalian hippocampus plays a crucial role in episodic memory formation and retrieval.1–4 One subregion, area CA3, is thought to be particularly important in this process as consistent, environmentally specific sequences of robust place cell (PC) activity originate here.5,6 The concept of attractors, which are the minimal set of states in a state space to which all nearby states eventually flow, currently represents an appealing theoretical mechanism for memory storage within brains.7,8 Attractor networks produce a complete output from only a partial set of inputs (pattern completion), have the potential to robustly store and accurately retrieve a very large number of activity patterns, and have been implicated in the creation of distinct output patterns even when presented with similar inputs (pattern separation).7–9 While various forms of attractor dynamics have been hypothesized to underlie the mnemonic functions of the hippocampus, whether and how they are implemented in CA3 remains unknown.6,8–18

Most relevant to hippocampal memory are networks whose activity dynamics are linked to or updated by the animal’s behavior (Figures S1C–S1F). Formation of place-related activity patterns in such networks requires specific adjustments of synaptic strengths to produce a set of neurons that become active together (an activity ‘‘bump’’; Figures S1E and S1F) and a separate mechanism to associate this neuronal activity with certain internal (movement velocity and path integration) and external (sensory environmental elements) features such that the dynamics of the activity bump is linked to behavior8–17 (red arrows

in Figures S1D and S1F). This updating or linking mechanism is frequently an additional appropriately tuned excitatory input. The specific adjustments mentioned above are mediated by learning rules that yield synaptic weight changes, usually at recurrent connections, that are symmetrical in network space8–20 (Figures S1B and S1F, blue arrows). Such rules produce stable network activity dynamics that can give rise to single neuron place-specific activity that persists within the same location in the absence of the additional updating mechanism. Asymmetric learning rules, on the other hand, cause unstable network dynamics where activity can change independently of any external linking inputs and is thus untethered to behavior21,22 (Figures S1G–S1K). While there are many theories about what learning rules and which pathways allow CA3 to produce the observed network dynamics,6–20,23,24 there is no relevant direct in vivo experimental evidence. We therefore sought to determine (1) what plasticity forms, (2) which synapses are responsible for individual CA3 place-field (PF) activity, (3) which input pathways, if any, act as an activity update mechanism, and (4) what are the theoretical capabilities of such an attractor network.

# RESULTS

# Characteristics of CA3 PFs

We began by using whole-cell intracellular membrane potential (V ) recordings from CA3 pyramidal neurons (n = 185) in headfixed mice running on a linear treadmill ( 180 cm) for a water reward25–28 (Figures 1A and 1B). Approximately one-quarter of the pyramidal neurons (46/185) fired action potentials (APs) in

![](images/23053ca7b20f7a38b4d4fdae3d3608f27772d2cfbdaee81eed905b98162622cb.jpg)

![](images/ec8f9e4d59027ccf93f5e7b31eebf15726cad33f9531e4448d74013423146b1d.jpg)

![](images/11cf48a2e38eadb606323416ec0758253cd797f1aef4fd9a08424ebbab3c7cdc.jpg)

![](images/a6952a69c085f7c166bdc42b0d2def9e0bdf865120a3bf80932a6f44d1c8d16c.jpg)

![](images/e03dd9c4b14d6e59bcc1df246d84e5f052e1f4371b9be31e1c6c51a7eb01b32b.jpg)

![](images/6a3b6b5b7210be8f14fb042ff0c5d5ca75147fb321e57ccd30b358621a604b50.jpg)

![](images/ca9016c4d0505164c99e861c371956ba9d9303f9a02b719999973180f3089844.jpg)

![](images/cb052f02bf64ce89d3a3807d124e693a792e7711713a9eda15c72b0d8090ee21.jpg)

![](images/dac6b97a3c3ff81ec0ffdb17deb64bdbd7847f175f122f007ae7ac99cf37d8da.jpg)

![](images/3ce269cbdf937cc3df88c2488c2867af6e96fa7f0bc342d7b1683925c036fd0a.jpg)

![](images/cced9a240e7744d26e3e7b26f86fad81708e370a0581ddd171195f9171a3532d.jpg)

![](images/7259582d07cc8eb3b01255d669c7e88bda86c994a0a7cb86b827c85094e22065.jpg)

![](images/a8e1de635c19f32b84dec4e0779fbcf6fee6501411c6f49f19d94e6f71df83d2.jpg)

![](images/54b09cb672f4a0cdd6d581411069a6efea0577ca78bca0f24eeedabe8cd0f0b5.jpg)

![](images/26e2d0faee12985012416c9214ea468c8620d0f86e2a4e7c42f4d0f45ae09a67.jpg)

![](images/b43221e72434867c5843944d7ed5d610c056c391210ac81a46dd6a7b85ea06e6.jpg)

![](images/479d8162b9a60f4fb11eaf259e518a816a6de9c570b5822d408ad7c6f5de9604.jpg)

![](images/6890a55dd0e1d88bfdc50c6e4ddbbfc862fd6adf89849d650a51a5ae8fbb231a.jpg)

![](images/b19a91316b431bdb10737014e9bdec5693a43b62aed9f67ea4076b17826623c1.jpg)

# Figure 1. Characteristics of CA3 PFs

(A) Histology (upper) shows electrode track of recording targeting hippocampal area CA3. Below is the recorded CA3 pyramidal neuron filled with biocytin, enlarged from the window of upper panel. Scale bar: 1 mm and 100 mm, respectively.   
(B) A typical CA3 PC with its field roughly in the middle of the track for six consecutive laps. (Black: membrane potentia $\mathsf { V } _ { \mathrm { m } } ;$ ; green: mouse position on track from 0 to 180 cm; yellow: mouse licking). $\mathsf { V } _ { \mathsf { m } }$ during prolonged standing between laps are removed (breaks).   
(C) Heat map of PF firing for all natural PCs sorted by the peak of PF.   
(D) Raw $\mathsf { V } _ { \mathsf { m } }$ traces of the $3 ^ { \mathsf { r d } }$ lap (upper) and the average AP rate in space (below; line and shadow indicate mean and SEM) for the same cell in (B), and the green dashed line indicates the peak location of $\mathsf { V } _ { \mathsf { m } }$ ramp in (E).   
(E and F) Same as (D), but the $\mathsf { V } _ { \mathsf { m } }$ ramp (remove APs from D) and $\mathsf { V } _ { \mathsf { m } }$ theta, respectively.   
(G) Upper shows the $\mathsf { V } _ { \mathsf { m } }$ expanded from the $5 ^ { \mathrm { t h } }$ lap in (B), showing plateau-associated burst firing with threshold for plateau (dashed line; red trace, removal of APs). Below is the histogram of in-field plateau duration for all natural PCs.   
(H) Upper is the average spatial profile for mouse running velocity from all mice during PC recordings. Below shows PC AP firing rate is strongly correlated with mouse running velocity $( \mathsf { R } ^ { 2 } = 0 . 9 0 ; p < 5 . 4 \times 1 0 ^ { - 3 6 } )$ .   
(I) Spatial profile of average AP rate for all natural PCs. Line and shadow indicate mean and SEM.   
(J and K) Same as (I), but the average $\mathsf { V } _ { \mathsf { m } }$ ramp and $\mathsf { V } _ { \mathsf { m } }$ theta amplitude, respectively.   
(L) Histogram of PF peak location for all natural PCs.

See also Figure S2.

spatially specific patterns during running periods (Figures 1B and 1C; see individual PCs in Figure S2A). This spatially localized firing was associated with a gradual increase in $\mathsf { V } _ { \mathsf { m } }$ depolarization $( \mathsf { V } _ { \mathsf { m } }$ ramp; Figure 1E) and a rise in the amplitude of intracellular theta frequency oscillations $( \mathsf { V } _ { \mathsf { m } }$ theta; Figure 1F), both peaking around the same spatial location as the AP rate (Figure 1D). In addition to standard AP firing, high-frequency burst firing associated with moderate-duration after-depolarizations (ADPs) was frequently observed within the PF (Figure 1G). Population averages of AP rate, $\mathsf { V } _ { \mathsf { m } }$ ramp, and $\mathsf { V } _ { \mathsf { m } }$ theta remained relatively flat across the track, except for a possible modulation

of AP rate by animal running speed $( \mathsf { R } ^ { 2 } = 0 . 9 0 ; p < 5 . 4 \times 1 0 ^ { - 3 6 } ;$ ; n = 100 spatial bins from average $\mathsf { A P }$ rate versus average velocity; Figures 1H–1K), suggesting that the spatial density of CA3 PCs is uniform across the environment. This uniformity was further supported by the even distribution of PF peak locations (Figure 1L). Together, these results indicate that, like CA1 PCs, CA3 PF firing is driven by a slow ramp of $\mathsf { V } _ { \mathsf { m } }$ depolarization and an increase in the amplitude of theta frequency $\mathsf { V } _ { \mathsf { m } }$ oscillations. However, unlike CA1,28–31 the spatial activity of CA3 PCs is uniformly distributed across the environment, creating a favorable condition for stable attractor dynamics.

![](images/2606bc6f51882fbb342306edbaa27d578db09ef07f83ae805ef37fc8d2a8abcc.jpg)  
A

![](images/1cd9cb85f93938244c8d3aeffd93c6a110e280c3e7eae6c1304d8d138a6a6527.jpg)

![](images/bfcd36e9634c3a04d5e70a85c98e4d86c08cdf23fd6820152525b5882a7774ca.jpg)

![](images/0eae38416b0053ab98fca127f76520ec24fa73e1ae4893a5a3da7f0f5e8456eb.jpg)

![](images/a89578277d86f38472ed755601d8ea9c7f4d5d30c914ad9809f764a99b2adf22.jpg)  
E

![](images/e35b4fa8186b271a0d7d01960d52b881855ca4a443ac115157b723c27b92810f.jpg)

![](images/4e0c0b79fe74a84f0dc184699875926986a9b5a089daacc192096d8dcabd81c1.jpg)  
F

![](images/55936741063f081caa91f56b1eecd508316cf5cecd338c3302bcd832d684ae60.jpg)

![](images/30ef47629ec21a1a05c255957034338c4c6ff62a59c7d8023a51ef096c6a770c.jpg)  
I

![](images/956fad54a6e83d9fdbc4674871dad705813397ac3a0f5407fe32f18cb2df63ee.jpg)

![](images/6918b1f0c0f5f304c08f535766d4634a0158c42a10388c246b847e7b74abb383.jpg)  
M

![](images/87c2291d32f7d1e7c28b59d24ae9df8cb3f756f1f0d536ced9d68d39d3bd91e5.jpg)

L   
Figure 2. Symmetric bidirectional BTSP underlies CA3 PFs   
![](images/0536612668328f856a3ca58cc8cc6b25ca8458fc9d921d46ef1079a866a80ca5.jpg)  
(A) $\mathsf { V } _ { \mathsf { m } }$ (black) and position (green, 0–180 cm) traces from CA3 neuron for multiple trials showing abrupt PF formation following naturally occurring plateau (labeled by red star).   
(B) Heat map of $\mathsf { A P }$ rate shows all the laps from the same cell in (A) with a spontaneous Ca plateau occurred at lap 19 (red arrow).   
(C) Average $\mathsf { V } _ { \mathsf { m } }$ ramp in space from those laps before (red, lap 1–18) and after (black, laps 20–50) the lap of plateau (lap 19) from the same cell in (A). Gray lines indicate the plateau location.   
(D) Same as $( \mathsf { C } ) ,$ but the difference of average $\mathsf { V } _ { \mathsf { m } }$ ramp $( \Delta \mathsf { V } _ { \mathsf { m } } \colon$ after – before in C) in time.   
(E) Same as (D), but the population average $\Delta \mathsf { V } _ { \mathsf { m } }$ ramp from all naturally occurring plateaus. Line and shadow indicate mean and SEM.   
(F–I) Same as (A)–(D), but a silent CA3 neuron with induced plateaus (labeled by red arrow).

# Synaptic mechanisms of CA3 PF formation

We next questioned how the above place-specific activity was produced. In a group of CA3 neurons, we observed the occurrence of distinctive, long-duration, dendritic plateau potentials during locomotion that were associated with the rapid formation of new PFs in previously silent cells or the shifting of PF location in existing PCs (Figures 2A and 2B; 14/185 cells; for individual spontaneous plateaus, see Figure S3C). These prolonged plateau potentials ( 6 times longer duration than the ADPs noted within PFs; Figures 1G and S3D) occurred as single events or even trains of such plateaus. The emergence of these long-duration plateaus (lap 19 in Figures 2A and 2B) led to an immediate change in the $\mathsf { V } _ { \mathsf { m } }$ depolarization profile of these cells across successive laps (laps 20–50 in Figures 2A and 2B). The $\mathsf { V } _ { \mathsf { m } }$ changes $( \Delta \mathsf { V } _ { \mathsf { m } } )$ were bidirectional with enhanced depolarization present at locations near the plateau $( \mathsf { V } _ { \mathsf { m } }$ _after $> \mathsf { V } _ { \mathsf { m } }$ _before; Figure 2C) and hyperpolarization at more distant locations $( \mathsf { V } _ { \mathsf { m } }$ _after $< ~ \mathsf { V } _ { \mathsf { m } }$ _ before). This rapid, bidirectional modulation of $\mathsf { V } _ { \mathsf { m } } ,$ unfolding on the seconds timescale (Figures 2D and 2E; see individuals in Figures S3A and S3B), is distinct from classical Hebbian plasticity and more reminiscent of the synaptic plasticity that underlies PF formation in hippocampal area CA1 (behavioral timescale synaptic plasticity, or BTSP).25–28,32–36 However, a notable distinction observed in CA3 neurons is that the $\mathsf { V } _ { \mathsf { m } }$ change produced appeared to be symmetric over time around the plateaus (Figure 2E), which contrasts with the pronounced asymmetric time course typically seen in CA1 BTSP.

To more thoroughly investigate this uniquely symmetric form of PF plasticity in CA3, we next experimentally induced plateaus under more controlled conditions. Large amplitude currents were injected into a group of neurons at particular track locations over multiple trials (1 nA for 500 ms; n = 80 inductions in 70 neurons; average 5.8 ± 0.1 induction trials; Figures 2F, 2G, and S4B– S4E) either in silent cells or outside the PFs of existing PCs (for details, see individual cells in Figure S4A). These induced plateaus again produced a bidirectional $\mathsf { V } _ { \mathsf { m } }$ change in the majority of neurons (peak $\Delta \mathsf { V } _ { \mathsf { m } } > 2$ mV in 60 of 70 neurons) with changes symmetrically spanning 10 s around the induced plateau (Figures 2H, 2I, and 2K–2M; for individual inductions, see Figure S4A). Within this time frame, two distinct phases were present with increased depolarization occurring near the plateau (± 2 s) and net hyperpolarization for several more seconds outside this phase. Accordingly, a linear relationship was observed between the resulting $\mathsf { V } _ { \mathsf { m } }$ ramp width in space, but not in time, and the animal’s running speed during plateau induction laps (Figures S4F and S4G) as would be expected from a plasticity rule spanning a fixed seconds-long temporal window.25,27 I n addition, the induced $\mathsf { V } _ { \mathsf { m } }$ changes were highly dependent on the initial $\mathsf { V } _ { \mathsf { m } }$ level present before the plateau initiation (Figure 2J). Together, these results suggest that plateau potentials drive a synaptic plasticity whose direction and magni-

tude are dependent on the time interval between the synaptic input and the plateau potential, as well as the current synaptic weight.27 Finally, the amplitude of the resultan $\mathsf { V } _ { \mathsf { m } }$ ramp depolarization was consistent for plateaus induced across different track locations (Figures S4H and S4I), indicating that individual CA3 neurons can form a PF at any location. Indeed, the synaptic plasticity form present in CA3 appears designed to produce a final $\mathsf { V } _ { \mathsf { m } }$ ramp with a common target shape that yields PFs at any location with the sole determinant being the position of the plateau potential.

To replicate the effects of naturally occurring long-duration plateau trains (Figure S3C), we next administered large amplitude currents to CA3 neurons at 3 separate track locations during 5 trials (1 nA for 500 ms at 30, 90, and 150 cm; n = 4; Figure S5A). The resulting bidirectional $\mathsf { V } _ { \mathsf { m } }$ change in these neurons closely mirrored the plasticity observed with single plateau induction, suggesting a similar process for synaptic modification (Figures S5B–S5F).

Finally, to examine the ability of high-frequency AP firing associated with plateaus to rapidly produce PFs, we used trains of short-duration current injections to evoke high-frequency APs without inducing plateaus (train of 50 APs at 100 Hz, 1 nA, 3-ms-duration pulses, 5 trials, $n = 7 ;$ Figure S5G). Contrary to plateau-inducing experiments, this approach did not yield any significant changes in either $\mathsf { V } _ { \mathsf { m } }$ ramp amplitude or the AP rate (Figures S5H–S5K), suggesting the high-frequency $\mathsf { A P }$ firing alone is insufficient for rapid PF formation in CA3 neurons. This highlights the pivotal role of dendritic plateau potentials in driving rapid PF formation and memory encoding in hippocampal CA3. Collectively, our findings indicate that a uniquely symmetric, bidirectional BTSP underlies rapid PF formation in CA3. If this form of BTSP-mediated weight adjustment is at work among the recurrent synapses between CA3 neurons, it could produce a directionally unbiased positive feedback that may contribute to stable attractor dynamics and memory formation (Figures S1B–S1F).

# Inputs involved in CA3 PF formation

The formation of PF in CA3 has been proposed to result from synaptic plasticity occurring selectively at the various excitatory inputs to CA3 pyramidal neurons, including grid cell input from EC, mossy fiber input from the DG, and the recurrent connections among CA3 pyramidal neurons.8–20,37–42 To determine which synaptic input is required for BTSP-induced PF formation in CA3, we independently inhibited each of the excitatory pathways to CA3 pyramidal neurons using optogenetic techniques. First, we inhibited CA3 itself by expressing ReaChR in PV+ interneurons and delivering excitation ‘‘light’’ bilaterally to CA3 via chronically implanted optical fibers targeting CA3 (Figure S6A). To test the role of CA3-CA3 recurrents, we briefly inhibited CA3 activity just before the position of the BTSP-inducing current injections (2.6 ± 0.5 s, 67.1 ± 1.8 cm, n = 7 cells from 7

animals; Figures 3A–3C). This inhibition caused an approximately 7 mV hyperpolarization during the light $( - 7 . 5 \pm 1 . 2$ mV) and dramatically impacted the shape of the resulting change in $\mathsf { V } _ { \mathsf { m } }$ compared with control animals (fiber implanted but lacking expression; Figure S6B) that were also given a similarly sized $\mathsf { V } _ { \mathsf { m } }$ hyperpolarization via current injection (7.8 ± 2.0 mV; n = 5 cells from 4 animals; Figure S7B). Inhibition of CA3 input significantly reduced the amount of BTSP-induced potentiation at the location of the manipulation (CA3 versus control; $0 . 9 9 \pm 0 . 4 9 \mathrm { m V } _ { \mathrm { ; } }$ $n = 7$ versus 4.57 ± 1.29 mV, $n = 5 ; p = 0 . 0 1$ , from Dunnett’s test; Figures 3D and 3E; see individual manipulations in Figure ${ \mathsf { S } } 7 { \mathsf { A } } ) ,$ and this caused a highly asymmetric-shaped BTSP-induced $\mathsf { V } _ { \mathsf { m } }$ change.

We employed a simplified model to explore the impact of reducing CA3 input on the resulting BTSP-induced changes in Vm ${ \mathsf { V } _ { \mathsf { m } } } ^ { 2 7 }$ (Figures 3F–3I; STAR Methods). This model features a single plateau potential (top row of Figure 3F, light green) and 1,000 spatially tuned synaptic inputs arriving as a sequence in time (Gaussian functions; $2 ^ { \mathsf { n d } }$ row of Figure 3F). Each of these signals is filtered (exponential function, tau = 0.67 s) to produce traces that recover the time course of the plasticity (plateau trace [PT], dark green, top row of Figure 3F; eligibility traces [ETs], $3 ^ { \mathsf { r d } }$ row). Synaptic weight adjustments $( 4 ^ { \mathrm { t h } }$ row) are calculated from the BTSP rule that largely depends on input-plateau interval and the current synaptic weight (STAR Methods). These adjustments are used to scale the inputs accordingly $( 5 ^ { \mathrm { t h } }$ row). Under standard conditions, this process produces a symmetric change in $\mathsf { V } _ { \mathsf { m } }$ since the two filters have the same time constant (Figures 3H, 3I, and S1B). However, when the number of CA3 inputs was reduced by 70% at a particular time to simulate the optogenetic manipulation $( 2 ^ { \mathsf { n d } }$ row of Figure 3G), both the ETs and their overlap with the PT diminished correspondently $( 3 ^ { \mathsf { r d } }$ row), leading to a decrease in synaptic weight adjustments. This reduction is visualized by the blue circles, indicating the disrupted 70% of CA3 inputs, and the blue line corresponds to the remaining 30% inputs $( 4 ^ { \mathrm { t h } }$ row). As a result, the weights of disrupted inputs remain unchanged while those of the uninterrupted inputs potentiate normally (arrow in the $5 ^ { \mathrm { t h } }$ row), culminating in an asymmetric $\mathsf { V } _ { \mathsf { m } }$ change (Figures 3H and 3I). This finding supports the notion that inputs must be active for their synaptic weights to be modified; hence, any intervention that reduces the number of active inputs will inevitably lead to a decrease in overall synaptic potentiation.25,27,43 The above experimental results strongly indicate that BTSP-driven alterations in the weights of the CA3-CA3 recurrent connections play an important role in CA3 PF formation.

We next examined the impact of inhibiting DG input on the shape of CA3 $\mathsf { V } _ { \mathsf { m } }$ change induced by BTSP (DG expression of archaerhodopsin with bilateral optical fibers targeted to CA3— one directed at the recording site; Figure S6C). This DG inhibition did not alter the profile of resultant $\mathsf { V } _ { \mathsf { m } }$ change, which remained symmetric around the induced plateau and was comparable to the control condition (average $\Delta \mathsf { V } _ { \mathsf { m } }$ during light; DG versus control; 4.17 ± 1.13 mV, n = 7 versus 4.57 ± 1.29 mV, n = 5; p = 0.95, from Dunnett’s test; Figures 3D and 3E; see individual manipulations in Figure S7E). We also administered appropriately sized hyperpolarizing current injections to compensate for the lack of observable $\mathsf { V } _ { \mathsf { m } }$ hyperpolarization during DG manipulations

$( - 1 0 . 4 \pm 1 . 2 \mathsf { m V } ; n = 7$ cells from 5 animals; Figure S7D). Given the lack of effect, we conducted direct intracellular recordings from DG granule cells under identical experimental conditions to validate the effectiveness of DG inhibition (Figure S6E). The light application significantly hyperpolarized the $\mathsf { V } _ { \mathsf { m } }$ and reduced AP firing in DG granule cells (Figures S6G–S6I), consistent with the impact on local field potentials recorded in CA3 (Figure S6F). These observations strongly suggest the absence of detectable changes in the shape of $\Delta \mathsf { V } _ { \mathsf { m } }$ induced by ${ \mathsf { B T S P } }$ cannot be ascribed to an ineffective DG inhibition under our behavioral conditions.

Finally, we explored the role of excitatory input from EC by implanting optical fibers targeting EC in mice expressing ReaChR in $\mathsf { P V } ^ { + }$ interneurons (ipsilateral inhibition only; $n = 1 3$ cells from 9 animals; Figure S6D). Unexpectedly, inhibiting EC essentially yielded the opposite effect on the shape of $\mathsf { V } _ { \mathsf { m } }$ change as that produced by CA3 inhibition. Specifically, the $\mathsf { V } _ { \mathsf { m } }$ potentiation during EC inhibition was unchanged (average $\Delta \mathsf { V } _ { \mathsf { m } }$ during light; EC versus control; $5 . 3 8 ~ \pm ~ 0 . 6 7$ mV, $n = 1 3$ versus $4 . 5 7 ~ \pm$ $1 . 2 9 \mathsf { m V } ; n = 5 ; p = 0 . 8 7$ , from Dunnett’s test), whereas the potentiation following the plateau was substantially diminished (Figures 4A–4D and 4H; see individual manipulations in Figure S7F). This produced an asymmetrical $\mathsf { V } _ { \mathsf { m } }$ change profile in the opposite direction to that seen with CA3 inhibition (Figures 4D, 4E, 3D, and 3E), suggesting a distinct role of EC input in modulating CA3 neuronal activity. To explain this observed asymmetry, we propose that EC input is responsible for linking the movement of the CA3 activity bump with the animal’s movement through the environment and that a reduction of EC input will lead CA3 activity to persist for longer than normal (red arrows in Figures S1C–S1F). We simulated this in our simplified model by holding the input activity at the same value during light $( 2 ^ { \mathsf { n d } }$ row of Figure 4G). The prolonged synaptic input elevated the amplitude of the associated ETs (arrow in $3 ^ { \mathsf { r d } }$ row), which in turn leads to enhanced potentiation of persistent inputs due to increased interaction (overlap) with the PT near the intervention $\mathsf { s i t e } ^ { 2 5 , 2 7 , 4 3 }$ (before the plateau location in the $4 ^ { \mathrm { t h } }$ and $5 ^ { \mathrm { t h } }$ rows of Figure 4G; STAR Methods). In addition, the prolonged activity during the manipulation also delayed the arrival of subsequent inputs (note position of middle input [black trace] in the $2 ^ { \mathsf { n d } }$ row of Figures 4G and 4F), reducing the overlap between PT and ETs and, consequently, the level of synaptic potentiation for those inputs following the manipulation (after plateau location in the $4 ^ { \mathrm { t h } }$ row of Figure 4G). Altogether, this manipulation leads to a leftward shift in the shape of $\mathsf { V } _ { \mathsf { m } }$ induced by BTSP (Figures 4H and 4I).

In summary, our findings demonstrate that only inhibition within CA3 leads to a reduction in BTSP-induced synaptic weight potentiation during the period of manipulation. By contrast, inhibition of other input pathways had either no observable effect or resulted in a shift of the $\mathsf { V } _ { \mathsf { m } }$ change induced by BTSP. We interpret these data to indicate that it is BTSP at CA3-CA3 recurrent synapses that are responsible for the PF firing of CA3 PCs. Thus, the formation of new PFs or modification of existing PFs during learning is through an adjustment of the synaptic weights of other currently active CA3 PCs. As mentioned above, this arrangement could contribute to stable attractor dynamics and memory formation in CA3.

![](images/ac5cf566f534ec49f11c5ac9e3fe07d572908e89602829d95cd394558ac2dac8.jpg)

![](images/dc32223eef710c08e1d02610147ad775baf2c0e340fa628a8b1f4219671706ed.jpg)

![](images/83d4aa8013b1cbfb7e11c04972347d2657e71c2bdec8cd3ad65c13a9f5804769.jpg)

![](images/d437fb6c562785016cf75268870d55ab7ec0db9b5a4afb6f3ecb52f307443890.jpg)

![](images/92253d86708aa039779922db64081c605de088f284546f237a1cfcdc38425a65.jpg)

![](images/314e21052fb9b50758d1ad85753f8474a838f6fb6cafbb7dd9ed047d0d08939d.jpg)

![](images/1e4b50182b0a8f6bf02a2b7dd115bcdb3ecbf4a0a2d2990a0f9281b42551180d.jpg)

![](images/299e04bbaa52eda89ef455a5666a8b6362f2b78e76a78c8918cbd5c137563f4d.jpg)

![](images/5f29fc26a0792b241384718050f90d84c944d21fcfa5adfddcb5a266c2838427.jpg)  
Figure 3. Involvement of CA3 and DG input pathways in PF formation

(A) Schematic of optogenetic inhibition (top) and $\mathsf { V } _ { \mathsf { m } }$ traces for laps before, during, and after plateau induction with CA3 inhibition. Yellow line indicates the light location and duration.

(B) Average $\mathsf { V } _ { \mathsf { m } }$ ramps for laps before (gray) and after (black) plateau induction in space from the cell in (A). Dashed line indicates plateau location.

(C) Same as (B), but the difference of average $\mathsf { V } _ { \mathsf { m } }$ ramp $( \Delta \mathsf { V } _ { \mathsf { m } } )$ ) in time.

(D) Population average $\Delta \mathsf { V } _ { \mathsf { m } }$ shows the impact of pathway silencing on BTSP induction profile. Yellow box indicates light activation time. Lines and shading indicate mean and SEM. All time bins with significant differences are shown (two-tailed unpaired Student’s t test, $p < 0 . 0 5 ;$ upper blue symbols, CA3 versus control; lower blue symbols, CA3 versus DG).

(E) Average change in $\mathsf { V } _ { \mathsf { m } }$ during manipulation period (2 $\mathrm { t o } - 0 . 5$ s) for each group (left). Average symmetry index for each group (right). For each plot, values from individual neurons shown. Symbols indicate significant differences (Dunnett’s test (left) and two-tailed unpaired Student’s t test (right), p < 0.01 for CA3 versus DG and CA3 versus control, and not significant for DG versus control).

(F) Control model signals, from top to bottom: plateau voltage (light green) and hypothetical biochemical filter of plateau potential (plateau trace, PT; dark green), synaptic input signals (inputs), hypothetical biochemical filter of synaptic input (eligibility traces, ETs), BTSP-induced weight distribution (weights), inputs scaled by weights (scaled inputs). Red signals are those associated with the centermost input. Green dashed line indicates the center of the plateau. Note every $1 0 ^ { \mathrm { t h } }$ signal is shown (STAR Methods).

(G) Same as (F), but signals for ‘‘CA3 manipulation’’ model (blue) that simulated a 70% reduction in input numbers for 1 s (thin to 0.3; yellow bar). Larger blue circles in the $4 ^ { \mathrm { t h } }$ row are weights affected by manipulation, while thin lines are weights unaffected by manipulation. Arrow in the $5 ^ { \mathrm { t h } }$ row indicate region where weights were changed/unchanged from initialization due to manipulation. Scaled inputs are control input sequences scaled by weights resulting from manipulation (note that 30% unaffected inputs scaled normally by the blue line in $4 ^ { \mathrm { t h } }$ row, while 70% affected inputs scaled by the blue circle in the $4 ^ { \mathrm { t h } }$ row). Black traces are signals associated with the centermost input.

(H) Same as (D), but peak scaled (normalized) $\Delta \mathsf { V } _ { \mathsf { m } } .$ Control and DG groups are combined (black). All time bins with significant differences are shown (two-tailed unpaired Student’s t test, $p < 0 . 0 5 )$ ).

(I) Simulated $\mathsf { V } _ { \mathsf { m } }$ ramps produced by summation of scaled inputs resulting from control (black) or CA3 manipulation (blue) conditions.

See also Figures S6 and S7.

![](images/c257f85b333eb1c7cff7402045dc9fddecb4b2330c317cb8373adf025b719602.jpg)

![](images/a002eec663d19759d0e713b1d655c5c57b31abb5800ee6f5310953767dbd189b.jpg)

![](images/874c907fbbb31f4fbf4f459ef465a6c2b4f81d12738520b0499456e84ead181e.jpg)

![](images/07988ba3ef8de4712d1e8e72c74b76613673d3619facfd68a24e31146ab6030d.jpg)

![](images/2e437da192352b643fe168f9ea3259f51cae99c50428f498b94b9ec73f7a5c78.jpg)

![](images/7575e98471d24de53298b861196c8d50ddf0e26ca8857dadc1fa310939e09084.jpg)

![](images/07b9a500017bdf22b856246c0f3319b7b15be5750955b3cba7c8bedaa6a3c7c2.jpg)

![](images/bcf3b9e1b11c3ed2cbc1f42688af4327d2feeb6121746aac385eb5a0c3f37246.jpg)

![](images/64e8fbded771eccd34b76d8cb3d76ab2101f1583001d82cdba0e29bc97c01d5e.jpg)  
Figure 4. Involvement of EC input pathway in PF formation

(A) Schematic of protocol for optogenetic silencing (top) and $\mathsf { V } _ { \mathsf { m } }$ traces for laps before, during, and after plateau induction for EC inhibition. Yellow line indicates the light location and duration.

(B) Average $\mathsf { V } _ { \mathsf { m } }$ ramps for laps before (gray) and after (black) plateau induction in space from the cell in (A). Dashed line indicates plateau location.

(C) Same as (B), but the difference of average $\mathsf { V } _ { \mathsf { m } }$ ramp $( \Delta \mathsf { V } _ { \mathsf { m } } )$ in time.

(D) Population average $\Delta \mathsf { V } _ { \mathsf { m } }$ shows the impact of pathway silencing on BTSP induction profile. Yellow box indicates light activation time. Lines and shading indicate mean and SEM. Note the data of DG and control are the same as $\mathsf { i n F i g u r e 3 D . A l l }$ time bins with significant differences are shown (two-tailed unpaired Student’s t test, $p \ < \ 0 . 0 5 ;$ ; upper red symbols, EC versus control; lower red symbols, EC versus DG).

(E) Average change in $\mathsf { V } _ { \mathsf { m } }$ during manipulation period $( - 2 \ : \mathrm { t o } \ : - 0 . 5 \ : \mathsf { s } )$ ) for each group (left; Dunnett’s test, not significant). Average symmetry index for each group (right). Symbols indicate significant differences (twotailed unpaired Student’s t test $p < 0 . 0 1$ for EC versus DG and EC versus control, and not significant for DG versus control). For each plot, values from individual neurons shown. Note the data of DG and control are the same as in $\mathsf { F i g u r e 3 E }$ .

(F) Same as Figure 3F.

(G) Same as (F), but signals for ‘‘EC manipulation’’ model (red), where all inputs were held at their current amplitude for 0.5 s to simulate a hold of activity bump (yellow bar). Black signals are those associated with the centermost input. Note the black signals were delayed by the manipulation compared with the red signals in control in (F). Dashed weights trace is from control in (F). Scaled inputs are control input sequences scaled by weights resulting from manipulation.

(H) Same as (D), but peak scaled (normalized) $\Delta \mathsf { V } _ { \mathsf { m } } .$ . Control and DG groups are combined (black). All time bins with significant differences are shown (two-tailed unpaired Student’s t test $p < 0 . 0 5 )$ .

(I) Simulated $\mathsf { V } _ { \mathsf { m } }$ ramps produced by summation of scaled inputs resulting from control (black) or EC manipulation (red) conditions.

See also Figures S6 and S7.

![](images/f1aac40b44cb3d8312308df4968f814093335d3604353a8329f9e6d7aa231f71.jpg)  
A

![](images/9e656808fb407b32aa885d23b94b4325750283ce6248da69076e565508b1f041.jpg)

![](images/510a38d19f24aa95890d114bea3f392d17d3521d3b9dbf7cd162b93f06028832.jpg)

![](images/17405003a01892618aac0c2a3f898b5e6e0612be9d5f3f430623fb1cc05df273.jpg)  
B

![](images/2e090ce0fd5410231df374840f0d780eba3214076938af3d1bf419e3d5ff043b.jpg)

![](images/482760c8597a1dd7d95ab051018206b3da55567edf120a0956e00abf64b7319e.jpg)

![](images/5acb03d842f67d338138a4c257074d4412b46189eb4684ceb13472b72f3054ea.jpg)  
C

![](images/0cbada31595bd0f480d8d6239f664be2cbfc6171f169f79e2422d4c0099f8802.jpg)

![](images/cec87a7ac5324050b4d3b0a1b3a887dd6f24345230ff9b899594793a968f5e06.jpg)

![](images/9d1ad3624ba4b8686ab6e3761b45c4683fa9aa37760c9e8ee60216ac13873a42.jpg)  
D

![](images/0e546a16577d348046078db2b60200b76ddac5ddfc83cac35dd8fda5b65b001c.jpg)

![](images/427dea431ef99dbe240dc708df5768286268822212b1561725ac5b8bc17d35bf.jpg)

![](images/3c6865c969b640e0f4b2c51d444e284cb06e42936671e76928a171a6c1bd1445.jpg)  
E

![](images/e72cc1266fb83566433df88a929b814b66d62982981803cbffcfbacf383b15d8.jpg)

![](images/aa6bd42b210d49b3acb6da4ce50bb35e982d837fcbe74f9c1ad93779e70fbb20.jpg)  
G

Figure 5. Involvement of different input pathways in PF activity   
![](images/f24342061ae8590f150eac5495eaec9cfe9c6c8b20de382a383333cb65e1af6d.jpg)  
(A) Heat maps show the spatial profile of $\mathsf { V } _ { \mathsf { m } }$ ramps for listed trials. Yellow box indicates which trials and approximately where within them light was active to inhibit either CA3, DG, or EC, from left to right. $\mathsf { V } _ { \mathsf { m } }$ ramps are baseline corrected by subtracting the mean value of 1st 5 bins.   
(B) Average $\mathsf { V } _ { \mathsf { m } }$ ramps in space for laps before, during, and after light activation for different groups shown in (A). Note the pause and subsequent shift in $\mathsf { V } _ { \mathsf { m } }$ ramp for EC inhibition. Yellow line indicates the light location and covered distance.   
(C) Average velocity traces in time for the same trial shown above. Yellow line indicates the light location and duration. Solid lines and shading indicate mean and SEM.

(legend continued on next page)

# Inputs involved in CA3 PC activity updating

We proposed above that EC input is required for updating CA3 PF activity in accordance with an animal’s running behavior. To further explore this, we examined how inhibition of the different input pathways affected the $\mathsf { V } _ { \mathsf { m } }$ of CA3 neurons already exhibiting PFs (either natural or experimentally induced). Optogenetic inhibition of CA3 activity transiently affected the $\mathsf { V } _ { \mathsf { m } }$ ramp, with $\mathsf { V } _ { \mathsf { m } }$ briefly hyperpolarizing during the light but promptly returning to control levels after light cessation (n = 12 cells from 10 animals; $1 ^ { \mathsf { s t } }$ column of Figures 5A–5D; for individual manipulations, see Figure S8E). On average, DG inhibition had no significant impact on the $\mathsf { V } _ { \mathsf { m } }$ ramp either before or after light illumination $( n = 1 7$ cells from 13 animals; $2 ^ { \mathsf { n d } }$ column of Figures 5A–5D; see individual manipulations in Figure S8E). By contrast, EC inhibition substantially impeded the normal progression of $\mathsf { V } _ { \mathsf { m } }$ during illumination (n = 19 cells with ipsilateral and 3 cells with bilateral inhibition from 20 animals; $3 ^ { \mathsf { r d } }$ column of Figures 5A–5D; for individual manipulations, see Figure S8E), resulting in a net hyperpolarization relative to control laps. Notably, the AP rate also remained fairly constant or progressed at a significantly slower rate under light inhibition in those cells with robust in-field firing (Figures S8A and S8B). Following light termination, the Vm gradually resumed its normal trajectory but with a delay that shifted the Vm ramp to positions further along the track $( 3 ^ { \mathsf { r d } }$ column of Figures 5A–5D, S8A, and S8B). The magnitude of this shift was correlated with the size of the light effect on $\mathsf { V } _ { \mathsf { m } } \left( \mathsf { V } _ { \mathsf { m } } \right.$ hyperpolarization compared with control laps; Figures 5E and 5G) but uncorrelated with any modest changes in running velocity (Figure 5H). We also simulated this manipulation with our simplified model and found that the CA3 manipulation primarily leads to a localized decrease in $\mathsf { V } _ { \mathsf { m } }$ ramp (Figure S8C), whereas EC intervention (Figure S8D) prevented the progress of normal activity and shifted the entire $\mathsf { V } _ { \mathsf { m } }$ ramp (Figures S8F and S8G). These results provide further evidence that EC input to CA3 is necessary for the CA3 activity bump to advance appropriately with an animal’s movement. Altogether, the above data and simulations suggest that a symmetric form of BTSP at CA3-CA3 synapses underlies the formation of neuronal attractors, whose dynamics is updated in accordance with the animal’s behavior through an external input from EC.

# Attractor network model and theoretical capabilities

We next tested this hypothesis in a recurrent network model where different subsets of neurons emitted plateau potentials uniformly across all locations of an environment during simulated navigation. A symmetric BTSP plasticity rule was used to potentiate synapses between neurons emitting plateaus close in time and depotentiate synapses between neurons whose plateaus

were farther apart. This rule produced a symmetric synaptic weight profile with spatially localized excitation (Figure 6A). In a network that included uniform inhibitory feedback, the bump of activity resulting from the network dynamics could be controlled by an external input. Indeed, once the external input was removed from the network, the attractor dynamics kept an activity bump stable at the last visited location, consistent with the above experimental observations (Figure 6B). Thus, the unique symmetric time course of BTSP observed in CA3 was able to produce continuous attractor dynamics that were effectively controlled by an external input similar to that provided by the EC.

Neuronal networks possessing attractor dynamics such as those observed in the above experiments and model are effective at storing memories and are found in many theories of hippocampal mnemonic function.8–15,44 The actual storage and retrieval capabilities of such attractor networks are shaped by the implemented synaptic learning rules.45–52 Therefore, we assessed the memory capacity of a network endowed with a symmetric form of BTSP by measuring its ability to retain previously stored input patterns as additional patterns were presented and stored. To test this, we used a discrete-time model with binary plateaus and activity patterns. We discretize into broad time windows of about 4 s and introduce binary signals for the neurons, which differ depending on whether the neuron is pre- or postsynaptic for a given synapse. We first take into account the necessity of a postsynaptic plateau; hence, the postsynaptic signal is non-zero only if the time bin contained a plateau. From the presynaptic perspective, both PF activity and spikes accompanying a plateau potential contribute to the signal. We then establish a rule for the potentiation and depotentiation of synapses, operating solely on events taking place in the current and previous time bins: (1) if the synapse weight is low and there are both pre- and postsynaptic signals in the same time bin, the synapse will be potentiated. (2) conversely, if the synapse weight is high and there is a postsynaptic signal at the current time bin with a presynaptic signal at the previous time bin or vice versa, the synapses will be depotentiated (Figures 6C, S9A, and S9B; STAR Methods; Methods S1). A few important properties emerge at the network level. First, upon initial exposure of a pattern, neurons with plateaus become reciprocally connected, creating a connectivity pattern capable of stabilizing an attractor state (Figures 6D and S9B). On the other hand, neurons with AP activity produce feedforward inputs onto the core group of attractor neurons, thus participating in the initialization of the attractor activity but not in its final stabilization. When a subsequent pattern was presented, the connections between neurons from overlapping attractor patterns are weakened, enhancing the separation of patterns by reducing the number of neurons shared between them (Figure 6D).

![](images/fcecfdd95870fe0ceb065884b5db7bcac75f4ecf423818a0bc7ff6b48b8eeb57.jpg)

![](images/8d6f47508fa1d00c56fa32373c14f7159c46a312ba86f60da26d71cb3cf8321f.jpg)

![](images/2039ee499ab53d66f84061dbe933621f7732af46f0557aaa0afb4bc55a9e42bd.jpg)

![](images/01dc860ecf3e9cdcc62cb2b686bcaef02e8bf715a2b5608bf636cf711410bc91.jpg)

![](images/2732d8be31b31d4fe99ead7d2c1493f4ec861f7269657d2fb73c9ca74a2b0fd8.jpg)

![](images/befb2ea976f4d96f0c250b2c5556b95179ae77c373dc1309e60e103e24299ae3.jpg)

![](images/53161f71a07822ae2dd33e8c9472fbeb22a15cf0d552c0a153ac382cdb439ca1.jpg)

(legend on next page)

Formally, the behavior of the synaptic states when the input patterns are random can be described as a Markov process (STAR Methods; Methods S1) with five states. These states include the depotentiated state, the newly potentiated state, the potentiated state, and two states that are primed for depotentiation. The dominant state transitions governing this process can be understood as follows: (1) An initial learning step potentiates the synapse (depotentiated to newly potentiated) with a probability proportional to the product of presynaptic and postsynaptic signal probabilities (Figure 6E, black arrow). (2) From here, the most likely outcome for a newly potentiated synapse in the case of uncorrelated signals is a transition to the potentiated state, which happens so long as there are no presynaptic or postsynaptic signals (Figure 6E, blue). (3) But if any presynaptic or postsynaptic signals occur in the next time bin immediately following potentiation, the initial potentiation may be reversed (newly potentiated to depotentiated; Figure 6E, pink). (4) Finally, depotentiation from the high weight state (potentiated to depotentiated) is a two-step process, involving presynaptic signal followed by a postsynaptic signal or vice versa (Figure 6E, green). Remarkably, the reversal transition (3) allows for an increased probability of depotentiation in the case of overlapping adjacent signals. These dynamics result in an exponential decay for the signal-to-noise ratio (SNR; STAR Methods) of the synaptic memory trace of a pattern as additional patterns are stored. We defined memory capacity as the number of patterns producing an SNR larger than a certain threshold (Figures S9F and S9G; STAR Methods).47 As we increased the size of the network, we observed an approximate quadratic scaling of memory capacity, which is optimal from an information-theoretic standpoint (Figure 6F; STAR Methods).45,47

We then investigated how this model would perform in the presence of temporal correlations in the stream of patterns, which is expected in realistic scenarios. These correlations might arise from similarities in the processed sensory inputs that any given neuron receives or from the dynamics of a recurrent network, where the weights store information about previously encountered patterns. This realistic scenario is notoriously challenging for standard Hebbian rules that depend on the co-occur-

rence of pre- and postsynaptic activity due to the interference between similar patterns at storage and retrieval (Figure 7B, Hebbian rule). Unlike in the traditional Hebbian rule, with BTSP, we observed a surprising increase in the number of attractors that can be stored in the network as temporal correlations in the activity patterns were increased (Figures 7A and 7B). In this case, the Markov process has additional states representing the activity (see Methods S1). The depotentiation component of the rule plays a crucial role in ensuring the network’s robustness to temporal correlations in the activity patterns. As the depotentiation process is triggered when there is a presynaptic signal followed by a postsynaptic signal or vice versa, it effectively decorrelates the signal across neighboring time bins (Figure 6D). This means that if a specific pattern of activity is correlated with the previous pattern, the depotentiation process helps to prevent the current pattern from interfering with or being influenced by the previously stored pattern. In the presence of temporal correlations, depotentiation events become targeted rather than random, which allows BTSP to store more attractors. This targeted depotentiation aids in reducing interference between similar patterns and enhances the network’s ability to store and retrieve information in realistic scenarios with correlated inputs (Figure S10). These results demonstrate the efficacy of BTSP in generating large numbers of attractor states within recurrent [[Neural networks]] and the advantage of BTSP compared with traditional Hebbian plasticity.

# DISCUSSION

Together, the above data, theory, and simulations support the idea that hippocampal area CA3 exhibits attractor dynamics and point to cellular and circuit mechanisms that effectively mediate this activity (Figure 7C). Several key observations contribute to this understanding: firstly, the density of CA3 PFs is relatively uniform across the environment, providing a generally flat energy landscape conducive to flexible and stable dynamics. Secondly, the synaptic plasticity underlying PF activity is a version of BTSP characterized by a symmetric time course, establishing balanced synaptic weights, irrespective

# Figure 6. Attractor dynamics in recurrent neural networks with BTSP

(A) Synaptic weights learned between plateau-emitting CA3 model units after ten simulated laps on the belt in the presence of ongoing BTSP.   
(B) A spatially localized input (red line) drives a bump of activity in the network. Upon input removal, the bump persists at the last visited location.   
(C) Time discretization and binarization of signals in the binary version of BTSP. Top left: both plateaus (red) and place-field activity (blue) contribute to the plasticity process in the presynaptic neuron. Bottom left: only plateaus generate plasticity signals in the postsynaptic neuron. Middle left: example synaptic dynamics. An initially depressed synapse (green, low weight) is potentiated (green, high weight) in the presence of presynaptic and postsynaptic plateaus in the same time bin and subsequently depressed when presynaptic activity is followed by a postsynaptic plateau. The simplified plasticity rule driving these synaptic changes is illustrated to the right, where potentiation occurs with simultaneous signals (right, top) approximating the continuous time changes. Depotentiation occurs with presynaptic and postsynaptic signals occurring in adjacent time bins (right bottom), approximating the continuous time plasticity rule.   
(D) A naive network with synapses governed by this simplified BTSP model first forms recurrent connections between neurons with postsynaptic signals that receive feedforward inputs from neurons with presynaptic-only signals (middle). Neurons that are active in the subsequent pattern have the synaptic connections to this original pattern pruned (right).   
(E) There are five states governing the binary synapse dynamics identified by ðW;Wqpreðt  1Þ;Wqpostðt  1ÞÞ. These states represent the depotentiated state with W = 0, the potentiated state with W = 1 and qpreðt  1Þ = qpostðt  1Þ = 0, and the states that are primed for depotentiation with W = 1 and at least one of qpreðt  1Þ = 1 or qpostðt  1Þ = 1. A newly potentiated synapse will always be in the state ð1; 1; 1Þ.   
(F) Optimal storage capacity scaling. Capacity is estimated from signal-to-noise ratio in networks of increasing size N, with sparse random uncorrelated pre- and postsynaptic activity and plateaus. The probability of having activity or plateaus in any given neuron at any given time is proportional to log(N)/N. The network’s memory span grows approximately quadratically with system size (N2 /log(N) 2 logarithmic scale plot in the inset). Parameters for (A), (B), and (F) are in STAR Methods.

See also Figures S9 and S10.

![](images/0bd10832521515eacd035bf764a8aff88fae3b98a5aeef64d7f7192b4951be65.jpg)

![](images/5698609fc8a1d55320f02b4ce893082b82730d46dc38c6e97ac2b9bc7a6d4edd.jpg)

![](images/626d18559e8d1730597a1da0d7d78d628cff0af91a485fadd654ef82929bb99e.jpg)

![](images/10817d46ac972bffbf531d3215c4e8c5c75bf1fd0e95f1d1b254e9e5eda70042.jpg)  
Figure 7. Temporal correlations in recurrent neural networks with BTSP

(A) Correlations in the input activity patterns lead to significant increases in the synaptic potentiation probability between adjacently stored patterns, represented by the probability of synaptic connection between the most recently stored patterns minus the average synaptic potentiation probability (see confusion matrix section in Methods S1) with $f _ { p } ~ = ~ f _ { a } ~ = ~ . 0 8 4 .$ .

(B) BTSP is robust against temporal correlations in activity, outperforming rules relying solely on simultaneous pre- and postsynaptic activity. Values plotted are capacity, where the probability of correct decoding drops to 0.75 (lower bar), 0.50 (data point), and 0.25 (upper bar). Parameters for (B) in STAR Methods.

(C) CA3 circuit schematic showing various excitatory synaptic input pathways and their approximate locations on a pair of CA3 pyramidal neurons comprising a single attractor. Numbered text is hypothesized roles for each input according to questions posed in the introduction and discussion. (D) Ring version53 of proposed attractor system where a symmetric BTSP rule among CA3-CA3 recurrent synapses (blue arrows; solid is potentiation and dashed depotentiation) combined with uniform inhibition (not shown) produces a bump of activity (black Gaussian at black circles) whose movement is determined by an updating mechanism linked to behavior (red arrows). This updating mechanism is thought to be provided by EC synaptic input. Shading of circles around bump indicates symmetric spread of synaptic current due to the symmetric plasticity rule. The role of DG input in this scheme remains unknown.

See also Figures S1, S9, and S10.

initiating a process that is largely selforganizing once set in motion.

# Limitations of the study

The observed impact of EC inhibition on CA3 activity (backward shift) limited our ability to directly measure the contribution of EC-CA3 synaptic weight changes to $\mathsf { V } _ { \mathsf { m } }$ ramp amplitude. Since the impact of CA3 inhibition was quite pronounced ( 75% reduction in $\mathsf { V } _ { \mathsf { m } }$ ramp amplitude), we sus-

of the direction of animal’s trajectory. In addition, the plasticity adjusts the synaptic weights within the CA3-CA3 recurrent pathway, allowing these synapses to generate a positive feedback required for stable, persistent activity among similarly tuned PCs. Finally, the stable activity bump within the attractor network requires an external input to associate the internal neuronal activity with the animal’s actual movement in the enviroment9,10,14,15,17 (Figure 7D). This crucial linkage appears to be mediated by direct excitatory input from the EC, highlighting the integral role of EC in hippocampal spatial representation. Thus, path integration-related activity in the EC may be involved in the selection of which attractors will become active,

pect this contribution should be relatively small. Nevertheless, some level of spatial selectivity would be beneficial in the EC updating mechanism, and this could come from EC input weight changes. The precise manner of synaptic weight adjustment between EC and CA3 remains a compelling question for further investigation. In addition, future experiments are needed to test the role of the various inputs to CA3 in plateau potential initiation and BTSP induction.

# EC inputs and CA3 attractors

The idea that synaptic plasticity among CA3 recurrent synapses could serve as a mechanism for hippocampal memory was first

sketched over five decades ago18 and has received varying degrees of experimental support over the years.12,13,19,20,54 Despite this, new discoveries such as grid cells in the EC and the demonstration of attractor dynamics within this area have prompted alternative hypotheses including new proposals that dynamical PC activity in CA3 might be directly inherited from EC.37,50,54–59 Yet, the evidence we presented here supports the notion that CA3 itself is capable of supporting attractor dynamics, emphasizing that learning a new environment and the stable storage of relevant information involves a reshaping of existing CA3 PC activity rather than a transformation of grid cell outputs into PC representations. Thus, new CA3 PFs will be formed using the tuned AP and plateau potential activity of other CA3 PCs via modification of the synaptic weights between them with, in this case, the direct EC input shaping how the CA3 PF population activity evolves during behavior. One prominent feature here is the formation of macroscopic neuronal assemblies that represent specific locations, anchored by core attractors consisting of neurons exhibiting plateaus during the learning process.

# Building CA3 attractors with BTSP

The prevailing theories of the 20th century and later all proposed that the primary mechanism of CA3 ensemble or attractor formation was Hebbian style synaptic plasticity, based on correlated AP activit y.6,7,10,11,15,18–20 However, we present evidence here that a different form of synaptic plasticity—BTSP—is actually involved. Furthermore, our theoretical analyses reveal that BTSP outperforms standard correlation-based forms of plasticity in online learning and memory formation within recurrent networks. The effectiveness of BTSP is attributable to several additional advantageous properties beyond the fact that it operates on the appropriate timescales (seconds versus milliseconds). For instance, the plateau potential is such a robust induction signal that only a single event is required to produce a fully formed PF,25,26 and the effectiveness of our BTSP model in recurrent networks is partly attributed to the presence of such sparse plateau activity.28,35,60 This sparsity, akin to the sparse coding hypothesis for neural activity,45,47,61,62 promotes efficient information representation and storage with minimal overlap between representations. Moreover, the bidirectional learning rule of BTSP featuring a directed depotentiation component,27 facilitates the transformation of similar input patterns into distinct output patterns, thus aiding pattern separation and minimizing interference between similar patterns at the synaptic level. The combination of sparsity and targeted depotentiation in BTSP significantly enhances the ability of hippocampal area CA3 to create unique representations, therefore increasing memory storage and retrieval capacity. An additional benefit of BTSP is that plateau potentials, as dendritic voltage signals, can be initiated by an external input distinct from those driving AP output. This could allow the strong excitatory input from DG, potentially interacting with direct EC input within the distal dendritic integrative compartment to serve as a ‘‘teaching signal’’ that directs BTSP induction and initial ensemble formation. Thus, BTSP could play a crucial role in orthogonalization6,18,63 and global remapping processes, where the hippocampus rapidly reorganizes its activity patterns in response to changes in the environ-

ment or task.64,65 Further experiments are essential to explore these hypotheses and their implications for hippocampal function.

The evidence presented here indicates that BTSP within the CA3 recurrent network near optimally forms unique neuronal representations with features associated with attractor dynamics, including the capability to update activity in alignment with the animal’s behavior via an external input from the EC. Similar plasticity rules and circuit mechanisms could also be beneficial in other recurrent networks, such as those found in the neocortex. Overall, the above observations advance our understanding of the mnemonic function of the hippocampus by providing evidence that unique instantiations of BTSP and activity updating circuit mechanisms within hippocampal area CA3, a brain region long associated with episodic memory, efficiently and effectively support a form of network dynamics that remains the most compelling framework for memory storage and retrieval in brains.

# RESOURCE AVAILABILITY

# Lead contact

Further information and requests for resources should be directed to and will be fulfilled by the lead contact, Jeffrey Magee (jcmagee@bcm.edu).

# Materials availability

This study did not generate new unique reagents. This study did not generate new mouse lines.

# Data and code availability

d All electrophysiological and behavioral data reported in this paper will be shared by the lead contact upon request.   
d All original code has been deposited at https://github.com/romani-lab/ Mechanisms-of-memory-supporting-neuronal-dynamics-inhippocampal-area-CA3-code/releases/tag/doi_final_revision_cell and is publicly available as of the date of publication. DOIs are listed in the key resources table.   
d Any additional information required to reanalyze the data reported in this paper is available from the lead contact upon request.

# ACKNOWLEDGMENTS

We thank R. Chitwood for technical support and G. Buzsa´ ki, N. Brunel, H. Inagaki, N. Li, and A. Roxin for useful comments on the manuscript. This work was funded by HHMI (J.C.M. and S.R.), the Cullen Foundation (J.C.M.), and HHMI via the Life Science Research Foundation (Y.L.). This article is subject to HHMI’s Open Access to Publications policy. HHMI lab heads have previously granted a nonexclusive CC BY 4.0 license to the public and a sublicensable license to HHMI in their research articles. Pursuant to those licenses, the author-accepted manuscript of this article can be made freely available under a CC BY 4.0 license immediately upon publication.

# AUTHOR CONTRIBUTIONS

Conceptualization, Y.L., J.J.B., S.R., and J.C.M.; physiological recordings, Y.L.; physiological data analysis, Y.L. and J.C.M.; computational modeling and theory, J.J.B. and S.R.; writing – review & editing, Y.L., J.J.B., S.R., and J.C.M.

# DECLARATION OF INTERESTS

The authors declare no competing interests.

# STAR+METHODS

Detailed methods are provided in the online version of this paper and include the following:

d KEY RESOURCES TABLE   
EXPERIMENTAL MODEL AND STUDY PARTICIPANT DETAILS   
B Animals and surgery   
d METHOD DETAILS   
B Behavior   
B In vivo intracellular electrophysiology   
B Data analysis   
B Optogenetic manipulations   
B Histology   
d QUANTIFICATION AND STATISTICAL ANALYSIS   
B Computational modeling

# SUPPLEMENTAL INFORMATION

Supplemental information can be found online at https://doi.org/10.1016/j.cell. 2024.09.041.

Received: March 12, 2024

Revised: August 27, 2024

Accepted: September 26, 2024

Published: October 24, 2024; Corrected online: January 16, 2025

# REFERENCES

1. Scoville, W.B., and Milner, B. (1957). Loss of recent memory after bilateral hippocampal lesions. J. Neurol. Neurosurg. Psychiatry 20, 11–21. https:// doi.org/10.1136/jnnp.20.1.11.   
2. Morris, R.G., Garrud, P., Rawlins, J.N., and O’Keefe, J. (1982). Place navigation impaired in rats with hippocampal lesions. Nature 297, 681–683. https://doi.org/10.1038/297681a0.   
3. Eichenbaum, H. (2016). Still searching for the engram. Learn. Behav. 44, 209–222. https://doi.org/10.3758/s13420-016-0218-1.   
4. Josselyn, S.A., and Tonegawa, S. (2020). Memory engrams: Recalling the past and imagining the future. Science 367, eaaw4325. https://doi.org/10. 1126/science.aaw4325.   
5. Nakazawa, K., McHugh, T.J., Wilson, M.A., and Tonegawa, S. (2004). NMDA receptors, place cells and hippocampal spatial memory. Nat. Rev. Neurosci. 5, 361–372. https://doi.org/10.1038/nrn1385.   
6. Kesner, R.P., and Rolls, E.T. (2015). A computational theory of hippocampal function, and tests of the theory: new developments. Neurosci. Biobehav. Rev. 48, 92–147. https://doi.org/10.1016/j.neubiorev.2014.11.009.   
7. Hopfield, J.J. (1982). Neural networks and physical systems with emergent collective computational abilities. Proc. Natl. Acad. Sci. USA 79, 2554–2558. https://doi.org/10.1073/pnas.79.8.2554.   
8. Khona, M., and Fiete, I.R. (2022). Attractor and integrator networks in the brain. Nat. Rev. Neurosci. 23, 744–766. https://doi.org/10.1038/s41583- 022-00642-0.   
9. Knierim, J.J., and Neunuebel, J.P. (2016). Tracking the flow of hippocampal computation: Pattern separation, pattern completion, and attractor dynamics. Neurobiol. Learn. Mem. 129, 38–49. https://doi.org/10.1016/j. nlm.2015.10.008.   
10. Ka´ li, S., and Dayan, P. (2000). The involvement of recurrent connections in area CA3 in establishing the properties of place fields: a model. J. Neurosci. 20, 7463–7477. https://doi.org/10.1523/JNEUROSCI.20-19- 07463.2000.   
11. McNaughton, B.L., Battaglia, F.P., Jensen, O., Moser, E.I., and Moser, M.- B. (2006). Path integration and the neural basis of the ’cognitive map’. Nat. Rev. Neurosci. 7, 663–678. https://doi.org/10.1038/nrn1932.   
12. Colgin, L.L., Leutgeb, S., Jezek, K., Leutgeb, J.K., Moser, E.I., McNaughton, B.L., and Moser, M.B. (2010). Attractor-map versus autoassociation

based attractor dynamics in the hippocampal network. J. Neurophysiol. 104, 35–50. https://doi.org/10.1152/jn.00202.2010.   
13. Wills, T.J., Lever, C., Cacucci, F., Burgess, N., and O’Keefe, J. (2005). Attractor dynamics in the hippocampal representation of the local environment. Science 308, 873–876. https://doi.org/10.1126/science.1108905.   
14. Knierim, J.J., and Zhang, K. (2012). Attractor dynamics of spatially correlated neural activity in the limbic system. Annu. Rev. Neurosci. 35, 267–285. https://doi.org/10.1146/annurev-neuro-062111-150351.   
15. Agmon, H., and Burak, Y. (2020). A theory of joint attractor dynamics in the hippocampus and the entorhinal cortex accounts for artificial remapping and grid cell field-to-field variability. eLife 9, e56894. https://doi.org/10. 7554/eLife.56894.   
16. Tsodyks, M., and Sejnowski, T. (1995). Associative memory and hippocampal place cells. International Journal of Neural Systems - IJNS 6, 81–86. https://doi.org/10.1142/9789814531962.   
17. Romani, S., and Tsodyks, M. (2015). Short-term plasticity based network model of place cells dynamics. Hippocampus 25, 94–105. https://doi.org/ 10.1002/hipo.22355.   
18. Marr, D., and Brindley, G.S. (1971). Simple memory: a theory for archicortex. Philos. Trans. R. Soc. Lond. B Biol. Sci. 262, 23–81. https://doi.org/10. 1098/rstb.1971.0078.   
19. Mishra, R.K., Kim, S., Guzman, S.J., and Jonas, P. (2016). Symmetric spike timing-dependent plasticity at CA3–CA3 synapses optimizes storage and recall in autoassociative networks. Nat. Commun. 7, 11552. https://doi.org/10.1038/ncomms11552.   
20. Guzman, S.J., Schlo¨ gl, A., Frotscher, M., and Jonas, P. (2016). Synaptic mechanisms of pattern completion in the hippocampal CA3 network. Science 353, 1117–1123. https://doi.org/10.1126/science.aaf1836.   
21. Kleinfeld, D. (1986). Sequential state generation by model neural networks. Proc. Natl. Acad. Sci. USA 83, 9469–9473. https://doi.org/10.1073/pnas. 83.24.9469.   
22. Sompolinsky, H., and Kanter, I.I. (1986). Temporal association in asymmetric neural networks. Phys. Rev. Lett. 57, 2861–2864. https://doi.org/ 10.1103/PhysRevLett.57.2861.   
23. Dragoi, G., and Tonegawa, S. (2011). Preplay of future place cell sequences by hippocampal cellular assemblies. Nature 469, 397–401. https://doi.org/10.1038/nature09633.   
24. Husza´ r, R., Zhang, Y., Blockus, H., and Buzsa´ ki, G. (2022). Preconfigured dynamics in the hippocampus are guided by embryonic birthdate and rate of neurogenesis. Nat. Neurosci. 25, 1201–1212. https://doi.org/10.1038/ s41593-022-01138-x.   
25. Bittner, K.C., Milstein, A.D., Grienberger, C., Romani, S., and Magee, J.C. (2017). Behavioral time scale synaptic plasticity underlies CA1 place fields. Science 357, 1033–1036. https://doi.org/10.1126/science.aan3846.   
26. Bittner, K.C., Grienberger, C., Vaidya, S.P., Milstein, A.D., Macklin, J.J., Suh, J., Tonegawa, S., and Magee, J.C. (2015). Conjunctive input processing drives feature selectivity in hippocampal CA1 neurons. Nat. Neurosci. 18, 1133–1142. https://doi.org/10.1038/nn.4062.   
27. Milstein, A.D., Li, Y., Bittner, K.C., Grienberger, C., Soltesz, I., Magee, J.C., and Romani, S. (2021). Bidirectional synaptic plasticity rapidly modifies hippocampal representations. eLife 10, e73046. https://doi.org/10.7554/ eLife.73046.   
28. Grienberger, C., and Magee, J.C. (2022). Entorhinal cortex directs learning-related changes in CA1 representations. Nature 611, 554–562. https://doi.org/10.1038/s41586-022-05378-6.   
29. Dupret, D., O’Neill, J., Pleydell-Bouverie, B., and Csicsvari, J. (2010). The reorganization and reactivation of hippocampal maps predict spatial memory performance. Nat. Neurosci. 13, 995–1002. https://doi.org/10. 1038/nn.2599.   
30. Hollup, S.A., Molden, S., Donnett, J.G., Moser, M.B., and Moser, E.I. (2001). Accumulation of Hippocampal Place Fields at the Goal Location in an Annular Watermaze Task. J. Neurosci. 21, 1635–1644. https://doi. org/10.1523/jneurosci.21-05-01635.2001.

31. Turi, G.F., Li, W.K., Chavlis, S., Pandi, I., O’Hare, J., Priestley, J.B., Grosmark, A.D., Liao, Z., Ladow, M., Zhang, J.F., et al. (2019). Vasoactive Intestinal Polypeptide-Expressing Interneurons in the Hippocampus Support Goal-Oriented Spatial Learning. Neuron 101, 1150–1165.e8. https://doi. org/10.1016/j.neuron.2019.01.009.   
32. Zhao, X., Wang, Y., Spruston, N., and Magee, J.C. (2020). Membrane potential dynamics underlying context-dependent sensory responses in the hippocampus. Nat. Neurosci. 23, 881–891. https://doi.org/10.1038/ s41593-020-0646-2.   
33. Zhao, X., Hsu, C.L., and Spruston, N. (2022). Rapid synaptic plasticity contributes to a learned conjunctive code of position and choice-related information in the hippocampus. Neuron 110, 96–108.e4. https://doi.org/10. 1016/j.neuron.2021.10.003.   
34. Fan, L.Z., Kim, D.K., Jennings, J.H., Tian, H., Wang, P.Y., Ramakrishnan, C., Randles, S., Sun, Y., Thadhani, E., Kim, Y.S., et al. (2023). All-optical physiology resolves a synaptic basis for behavioral timescale plasticity. Cell 186, 543–559.e19. https://doi.org/10.1016/j.cell.2022.12.035.   
35. Priestley, J.B., Bowler, J.C., Rolotti, S.V., Fusi, S., and Losonczy, A. (2022). Signatures of rapid plasticity in hippocampal CA1 representations during novel experiences. Neuron 110, 1978–1992.e6. https://doi.org/10.1016/j. neuron.2022.03.026.   
36. O’Hare, J.K., Gonzalez, K.C., Herrlinger, S.A., Hirabayashi, Y., Hewitt, V.L., Blockus, H., Szoboszlay, M., Rolotti, S.V., Geiller, T.C., Negrean, A., et al. (2022). Compartment-specific tuning of dendritic feature selectivity by intracellular Ca(2+) release. Science 375, eabm1670. https://doi. org/10.1126/science.abm1670.   
37. Cheng, S., and Frank, L.M. (2011). The structure of networks that produce the transformation from grid cells to place cells. Neuroscience 197, 293–306.   
38. Witter, M.P. (2007). Intrinsic and extrinsic wiring of CA3: indications for connectional heterogeneity. Learn. Mem. 14, 705–713. https://doi.org/ 10.1101/lm.725207.   
39. Li, X.G., Somogyi, P., Ylinen, A., and Buzsa´ ki, G. (1994). The hippocampal CA3 network: an in vivo intracellular labeling study. J. Comp. Neurol. 339, 181–208. https://doi.org/10.1002/cne.903390204.   
40. Buzsa´ ki, G. (1989). Two-stage model of memory trace formation: a role for "noisy" brain states. Neuroscience 31, 551–570. https://doi.org/10.1016/ 0306-4522(89)90423-5.   
41. Zucca, S., Griguoli, M., Male´ zieux, M., Grosjean, N., Carta, M., and Mulle, C. (2017). Control of Spike Transfer at Hippocampal Mossy Fiber Synapses In Vivo by GABAA and GABAB Receptor-Mediated Inhibition. J. Neurosci. 37, 587–598. https://doi.org/10.1523/jneurosci.2057- 16.2016.   
42. Henze, D.A., Wittner, L., and Buzsa´ ki, G. (2002). Single granule cells reliably discharge targets in the hippocampal CA3 network in vivo. Nat. Neurosci. 5, 790–795. https://doi.org/10.1038/nn887.   
43. Magee, J.C., and Grienberger, C. (2020). Synaptic Plasticity Forms and Functions. Annu. Rev. Neurosci. 43, 95–117. https://doi.org/10.1146/annurev-neuro-090919-022842.   
44. Li, P.Y., and Roxin, A. (2023). Rapid memory encoding in a recurrent network model with behavioral time scale synaptic plasticity. PLoS Comput. Biol. 19, e1011139. https://doi.org/10.1371/journal.pcbi.1011139.   
45. Willshaw, D.J., Buneman, O.P., and Longuet-Higgins, H.C. (1969). Nonholographic associative memory. Nature 222, 960–962. https://doi.org/ 10.1038/222960a0.   
46. Tsodyks, M.V. (1990). Associative memory in neural networks with binary synapses. Mod. Phys. Lett. B 04, 713–716. https://doi.org/10.1142/ S0217984990000891.   
47. Amit, D.J., and Fusi, S. (1994). Learning in Neural Networks with Material Synapses. Neural Comput. 6, 957–982. https://doi.org/10.1162/neco. 1994.6.5.957.

48. Fusi, S., Drew, P.J., and Abbott, L.F. (2005). Cascade models of synaptically stored memories. Neuron 45, 599–611. https://doi.org/10.1016/j. neuron.2005.02.001.   
49. Benna, M.K., and Fusi, S. (2016). Computational principles of synaptic memory consolidation. Nat. Neurosci. 19, 1697–1706. https://doi.org/10. 1038/nn.4401.   
50. Solstad, T., Moser, E.I., and Einevoll, G.T. (2006). From grid cells to place cells: a mathematical model. Hippocampus 16, 1026–1031. https://doi. org/10.1002/hipo.20244.   
51. Clopath, C., Nadal, J.P., and Brunel, N. (2012). Storage of correlated patterns in standard and bistable Purkinje cell models. PLoS Comput. Biol. 8, e1002448. https://doi.org/10.1371/journal.pcbi.1002448.   
52. Kaifosh, P., and Losonczy, A. (2016). Mnemonic Functions for Nonlinear Dendritic Integration in Hippocampal Pyramidal Circuits. Neuron 90, 622–634. https://doi.org/10.1016/j.neuron.2016.03.019.   
53. Campbell, M.G., Ocko, S.A., Mallory, C.S., Low, I.I.C., Ganguli, S., and Giocomo, L.M. (2018). Principles governing the integration of landmark and self-motion cues in entorhinal cortical codes for navigation. Nat. Neurosci. 21, 1096–1106. https://doi.org/10.1038/s41593-018-0189-y.   
54. Jezek, K., Henriksen, E.J., Treves, A., Moser, E.I., and Moser, M.-B. (2011). Theta-paced flickering between place-cell maps in the hippocampus. Nature 478, 246–249. https://doi.org/10.1038/nature10439.   
55. de Almeida, L., Idiart, M., and Lisman, J.E. (2009). The input-output transformation of the hippocampal granule cells: from grid cells to place fields. J. Neurosci. 29, 7504–7512. https://doi.org/10.1523/JNEUROSCI.6048- 08.2009.   
56. Monaco, J.D., and Abbott, L.F. (2011). Modular Realignment of Entorhinal Grid Cell Activity as a Basis for Hippocampal Remapping. J. Neurosci. 31, 9414–9425. https://doi.org/10.1523/jneurosci.1433-11.2011.   
57. Azizi, A.H., Schieferstein, N., and Cheng, S. (2014). The transformation from grid cells to place cells is robust to noise in the grid pattern. Hippocampus 24, 912–919. https://doi.org/10.1002/hipo.22306.   
58. Gardner, R.J., Hermansen, E., Pachitariu, M., Burak, Y., Baas, N.A., Dunn, B.A., Moser, M.B., and Moser, E.I. (2022). Toroidal topology of population activity in grid cells. Nature 602, 123–128. https://doi.org/10.1038/ s41586-021-04268-7.   
59. Chandra, S., Sharma, S., Chaudhuri, R., and Fiete, I. (2023). High-capacity flexible hippocampal associative and episodic memory enabled by prestructured ‘‘spatial’’ representations. Preprint at bioRxiv. https://doi.org/ 10.1101/2023.11.28.568960.   
60. Vaidya, S.P., Chitwood, R.A., and Magee, J.C. (2023). The formation of an expanding memory representation in the hippocampus. Preprint at bio-Rxiv. https://doi.org/10.1101/2023.02.01.526663.   
61. Tsodyks, M., and Feigel’man, M. (2007). The Enhanced Storage Capacity in Neural Networks with Low Activity Level. EPL (Europhys. Lett.) 6, 101–105. https://doi.org/10.1209/0295-5075/6/2/002.   
62. Romani, S., Pinkoviezky, I., Rubin, A., and Tsodyks, M. (2013). Scaling laws of associative memory retrieval. Neural Comput. 25, 2523–2544. https://doi.org/10.1162/NECO_a_00499.   
63. Hainmueller, T., and Bartos, M. (2020). Dentate gyrus circuits for encoding, retrieval and discrimination of episodic memories. Nat. Rev. Neurosci. 21, 153–168. https://doi.org/10.1038/s41583-019-0260-z.   
64. Bostock, E., Muller, R.U., and Kubie, J.L. (1991). Experience-dependent modifications of hippocampal place cell firing. Hippocampus 1, 193–205. https://doi.org/10.1002/hipo.450010207.   
65. Colgin, L.L., Moser, E.I., and Moser, M.-B. (2008). Understanding memory through hippocampal remapping. Trends Neurosci. 31, 469–477. https:// doi.org/10.1016/j.tins.2008.06.008.   
66. Li, N., Chen, S., Guo, Z.V., Chen, H., Huo, Y., Inagaki, H.K., Chen, G., Davis, C., Hansel, D., Guo, C., and Svoboda, K. (2019). Spatiotemporal constraints on optogenetic inactivation in cortical circuits. eLife 8, e48622. https://doi.org/10.7554/eLife.48622.

67. Ferna´ ndez-Ruiz, A., Oliva, A., Soula, M., Rocha-Almeida, F., Nagy, G.A., Martin-Vazquez, G., and Buzsa´ ki, G. (2021). Gamma rhythm communication between entorhinal cortex and dentate gyrus neuronal assemblies. Science 372, eabf3119. https://doi.org/10.1126/science.abf3119.   
68. Miao, C., Cao, Q., Ito, H.T., Yamahachi, H., Witter, M.P., Moser, M.B., and Moser, E.I. (2015). Hippocampal Remapping after Partial Inactivation of the Medial Entorhinal Cortex. Neuron 88, 590–603. https://doi.org/10. 1016/j.neuron.2015.09.051.   
69. Kanter, B.R., Lykken, C.M., Avesar, D., Weible, A., Dickinson, J., Dunn, B., Borgesius, N.Z., Roudi, Y., and Kentros, C.G. (2017). A Novel Mechanism for the Grid-to-Place Cell Transformation Revealed by Transgenic Depolarization of Medial Entorhinal Cortex Layer II. Neuron 93, 1480–1492.e6. https://doi.org/10.1016/j.neuron.2017.03.001.   
70. Rueckemann, J.W., DiMauro, A.J., Rangel, L.M., Han, X., Boyden, E.S., and Eichenbaum, H. (2016). Transient optogenetic inactivation of the

medial entorhinal cortex biases the active population of hippocampal neurons. Hippocampus 26, 246–260. https://doi.org/10.1002/hipo.22519.   
71. Robinson, N.T.M., Priestley, J.B., Rueckemann, J.W., Garcia, A.D., Smeglin, V.A., Marino, F.A., and Eichenbaum, H. (2017). Medial Entorhinal Cortex Selectively Supports Temporal Coding by Hippocampal Neurons. Neuron 94, 677–688.e6. https://doi.org/10.1016/j.neuron.2017.04.003.   
72. Zutshi, I., Valero, M., Ferna´ ndez-Ruiz, A., and Buzsa´ ki, G. (2022). Extrinsic control and intrinsic computation in the hippocampal CA1 circuit. Neuron 110, 658–673.e5. https://doi.org/10.1016/j.neuron.2021.11.015.   
73. Keinath, A.T., Nieto-Posadas, A., Robinson, J.C., and Brandon, M.P. (2020). DG-CA3 circuitry mediates hippocampal representations of latent information. Nat. Commun. 11, 3026. https://doi.org/10.1038/s41467- 020-16825-1.

# STAR+METHODS

# KEY RESOURCES TABLE

<table><tr><td>REAGENT or RESOURCE</td><td>SOURCE</td><td>IDENTIFIER</td></tr><tr><td>Antibodies</td><td></td><td></td></tr><tr><td>Streptavidin, Alexa Flour 488 Conjugate</td><td>Invitrogen</td><td>Ca#S32354</td></tr><tr><td>Streptavidin, Alexa Flour 595 Conjugate</td><td>Invitrogen</td><td>Ca#S32356</td></tr><tr><td>Deposited data and code</td><td></td><td></td></tr><tr><td>Raw and analyzed data, including electrophysiological and behavioral data</td><td>This paper</td><td>Available upon request</td></tr><tr><td>Code</td><td>This paper</td><td>DOI: https://doi.org/10.5281/zenodo.13381238</td></tr><tr><td>Experimental models: Organisms/strains</td><td></td><td></td></tr><tr><td>C57Bl/6J</td><td>Jackson Laboratory</td><td>RRID: IMSR_JAX: 000664</td></tr><tr><td>PV-IRES-Cre</td><td>Jackson Laboratory</td><td>RRID: IMSR_JAX: 017320</td></tr><tr><td>ReaChR-mCitrine</td><td>Jackson Laboratory</td><td>RRID: IMSR_JAX: 024846</td></tr><tr><td>Ai35D</td><td>Jackson Laboratory</td><td>RRID: IMSR_JAX: 012735</td></tr><tr><td>Rbp4-Cre</td><td>MMRRC</td><td>MMRRC: 031125-UCD</td></tr><tr><td>Software and algorithms</td><td></td><td></td></tr><tr><td>MATLAB</td><td>MathWorks</td><td>https://www.mathworks.com/</td></tr><tr><td>IGOR</td><td>WaveMetrics</td><td>https://www.wavemetrics.com/</td></tr><tr><td>WaveSurfer</td><td>HHMI Janelia</td><td>https://wavesurfer.janelia.org/</td></tr></table>

# EXPERIMENTAL MODEL AND STUDY PARTICIPANT DETAILS

# Animals and surgery

All experimental methods were approved by the Baylor College of Medicine Institutional Animal Care and Use Committees (Protocol 15–126). All experimental procedures in this study, including animal surgeries, behavioral training, treadmill and rig configuration, and intracellular recordings, were performed identically to previous detailed reports25–27 with the exception that area CA3 was targeted instead of CA1.

Wild type C57BL6 (WT; JAX #000664) male mice aged 10–14 weeks obtained from the Baylor College of Medicine Center for Comparative Medicine or Jackson Laboratory were used for all non-manipulation experiments. Different transgenic mice in 10– 18-week-old of either sex were used for different sets of optogenetic experiments: PV-Cre (JAX #017320) crossed with ReaChR (JAX #024846) was used for CA3 and EC silencing, non-crossed ReaChR was used as the control group and Rbp4-Cre (MMRRC: 031125-UCD) crossed with Ai35D (JAX #012735) were used for DG silencing.

Craniotomies above the dorsal hippocampus for simultaneous whole-cell recordings and local field potential (LFP) recordings, as well as affixation of head bar and optical fiber implants were performed under deep isoflurane anesthesia. The coordinates for hippocampal CA3 recording were (in mm): AP: 1.85, ML: 2.35. The optical fibers (200 um in diameter, 0.5 N.A., Thorlabs) were implanted bilaterally at 0.15 mm (AP), 3.0 mm (ML), 40 to the horizontal, 35 to the sagittal, and the depth is 1.9 mm along the axis of the fiber for CA3 and DG manipulations as well as control groups (Figures S6A–S6C). For the EC manipulations, the fibers were implanted ipsilaterally/bilaterally at 4.8 mm (AP), 3.4 mm (ML), 10 to the coronal and the depth is 1.1 mm along the axis of the fiber (Figure S6D). The animals are singly housed after surgery and addition of running wheels to their home cages. All mice were reared on a reversed 12/12 hr light/dark cycle.

# METHOD DETAILS

# Behavior

Following a week of recovery, animals were prepared for behavioral training with water restriction. From the second day of water restriction, animals were adapted and handled by the experimenter for typically five days (30 min per day). Once the training started, water was given only during the experiment and in the end of the day, and specific care was taken to keep the animal body weight above 80 % of the weight before water restriction. The animals were trained on the cue-enriched belt ( 180 cm long with three different feature zones distributed equally in space) for a 10 % sucrose reward delivered through a licking port ( 3.3 ml per drop).

The first training day lasted only 20 min, and the reward was initially delivered every 30 cm to encourage the animal to run. After every 10 trials, an incremental 30 cm was added until a total distance of 180 cm was reached, at which point the reward was fixed per lap. Typically, the reward would be fixed starting from the second training day and the training session extended to 40 min. From the third training day, the session was extended and fixed to 1 h. Animals typically took 7–10 days to run more than 150 laps in an 1-h training session, at which point they were ready for the recording.

A MATLAB GUI interfaced with a custom microprocessor-controlled system was used for position-dependent reward delivery, intracellular current injection and optogenetic light delivery. Animal running velocity was measured by an encoder attached to one of the wheel axles.

# In vivo intracellular electrophysiology

To locate the CA3 pyramidal layer, an extracellular LFP glass electrode (1.5–3 MU) filled with 0.9 % NaCl was lowered into the dorsal hippocampus using a micromanipulator (Luigs and Neumann) until prominent theta-modulated spiking and increased ripple amplitude was detected again after transiting the CA1 pyramidal layer, usually to a depth of 1.8–2.0 mm. The extracellular signal was monitored using an audio amplifer (Grass Technologies). Then a glass intracellular recording pipette (8–12 MU) was lowered into the cortex while applying positive pressure (9–11 psi). After the pipette reached to 50 mm above the CA3 pyramidal layer, the pressure was reduced to 0.2–0.3 psi for hunting. Cells were identified by reproducible increases in electrode resistance. The intracellular solution contained (in mM): 134 K-Gluconate, 6 KCl, 10 HEPES, 4 NaCl, 0.3 MgGTP, 4 MgATP, 14 Tris-phosphocreatine, and 0.2 % biocytin. Current-clamp recordings of intracellular membrane potential $( \mathsf { V } _ { \mathsf { m } } )$ were amplified by Cornerstone BVC-700A amplifier (Dagan), analog filtered at 1 kHz before digitized at 20 kHz using BNC-2090A digitizer (National Instruments) and acquired by WaveSurfer (https://wavesurfer.janelia.org/), without correction for liquid junction potential.

For plateau induction, a position-dependent step current (1 nA, 500 ms, usually 5 laps) was injected into the recorded cells. In a subset of cells where resting $\mathsf { V } _ { \mathsf { m } }$ was greater than  –65 mV an additional small DC current (< 50 pA) was also given to increase the probability of inducing plateaus. A 100 Hz current train (1 nA, 500 ms, 3-ms-duration pulse, 5 laps) instead of the step current was injected to induce APs in some experiments (Figures S5G–S5K).

# Data analysis

The cells with series resistance > 60 MU or the AP amplitude < 30 mV were excluded. The data were not filtered unless specified. The AP was firstly detected and the AP threshold was defined as the largest increase in the slope of voltage versus the derivative dVdt. Then $\mathsf { V } _ { \mathsf { m } }$ were corrected on a trial-by-trial basis by setting the average of the fifth percentile of most negative AP threshold at –50 mV. To analyze the $\mathsf { V } _ { \mathsf { m } }$ ramp, the $\mathsf { A P }$ were removed by deleting all the points 1.5 ms before and 3 ms after the AP peak and interpolated, or raw $\mathsf { V } _ { \mathsf { m } }$ traces were median filtered (40 points).

To analyze the spatial location of AP rate, the spatially binned AP rate was determined (AP#/time in bin) using 100 equally sized spatial bins ( 1.80 cm) for each trial and averaged over the duration of the recording. Place cells were determined to possess above chance spatial information from these AP rate plots28:

$$
S I = \sum_ {i} p _ {i} \cdot x _ {i} \cdot \log_ {2} \left(\operatorname {a b s} \left(x _ {i} / \bar {x}\right)\right)
$$

Where pi is the probability of occupancy for spatial bin i, xi is the smoothed mean AP rate while occupying bin $i , { \bar { x } }$ is the overall mean AP rate. The SI for each cell is then compared to 500 shuffles of the AP rate (each shuffle was generated by randomly assigning a bin location). If the observed spatial information exceeded the $9 5 ^ { \mathrm { t h } }$ percentile of the shuffled information values, its field was considered spatially modulated. To analyze $\mathsf { V } _ { \mathsf { m } }$ ramps, raw $\mathsf { V } _ { \mathsf { m } }$ traces were median filtered to remove $\mathsf { A P s } ,$ , baseline corrected by subtracting the difference in the recorded AP threshold and –50 mV and spatially binned and averaged as above. To analyze theta frequency $\mathsf { V } _ { \mathsf { m } }$ oscillations, the $\mathsf { V } _ { \mathsf { m } }$ ramp were first bandpass filtered (2–10 Hz) and then the amplitude of the theta-band oscillations was determined from a Hilbert Transform of these traces. In some cases (Figures 1D–1F), the average spatially-binned $\mathsf { A P }$ rates, $\mathsf { V } _ { \mathsf { m } }$ ramps and theta amplitude traces were further smoothed using a boxcar of 5 bins. The spatially-binned AP rates in the heat map shown in Figure 1C were smoothed with a gaussian (36 cm). Spontaneous naturally-occurring plateau duration was estimated as the full width at plateau detection threshold $\mathsf { V } _ { \mathsf { m } }$ value (–35 mV), as shown in Figures 1G and S3E.

To determine the plateau-induced $\mathsf { V } _ { \mathsf { m } }$ change 5–10 trials before the plateau trials were averaged as a ‘‘before’’ trace. 5–10 trials after the plateau were also averaged as an ‘‘after’’ trace and this was subtracted from the before trace to produce a difference $( \Delta \mathsf { V } _ { \mathsf { m } } )$ . For naturally occurring plateau the time base (in 100 spatial bins) was produced by determining the time required for the animal to run from a given track location to the location of the $\Delta \mathsf { V } _ { \mathsf { m } }$ peak on the trial where the natural plateaus occurred. For induced plateau the time base was determined as the minimum run time from the middle of the plateau-inducing current injection to a particular location (in 100 spatial bins) as calculated from all induction laps. For this a single composite position versus time trace that represented the shortest induction lap in time was constructed by taking the minimum time delay to plateau midpoint for each spatial position across all induction laps (Figure S4C).

$\mathsf { V } _ { \mathsf { m } }$ ramp half-width (Figures 2I, S4F, and S4G) was calculated from the $\Delta \mathsf { V } _ { \mathsf { m } }$ traces as the time (s) or distance (cm) between the plateau and the final return of $\Delta \mathsf { V } _ { \mathsf { m } }$ to 15 % of max). This value was halved if both sides of the $\Delta \mathsf { V } _ { \mathsf { m } }$ trace returned to the minimum

value, if only one side returned (because the end of the track was reached before) then this single value was used. The average velocity was calculated from the composite induction lap as the mean velocity of the mouse for the distance covered by the half-width measure (Figure S4C). The symmetry of the $\Delta \mathsf { V } _ { \mathsf { m } }$ trace in time was determined from the relative difference in the positive areas under the curve (AUC), (AUCpositive time side – AUCnegative time side) / AUCtotal (Figures 2M, 3E, and 4E).

# Optogenetic manipulations

Given the lack of EC layer 2 and CA3 specific reporter lines, we chose to use localized activation of PV inhibitory cells to inhibit EC and CA3 given its strong and potentially restricted inhibition.66 We chose not to use the PV strategy for the DG inactivation because it would be very difficult to limit the delivery of the light to only the DG (without also inhibiting CA3 directly) and because expression in the Rbp4-Cre line is restricted to the DG within the hippocampus.

Optical fibers were coupled to an external fiber using standard FC connectors via the mental sleeve and then connected to two 595 nm LEDs (Thorlabs). The maximum power (2.5 mW) was used in all the optogenetic experiments except the EC manipulation. For the EC manipulation, the power (0.8–2.5 mW) was adjusted accordingly so as to not affect the animal’s behavior. A 40 Hz sine wave light stimuli, generated by an arbitrary waveform generator (Tektronix), was given to activate the PV positive interneurons expressing ReaChR, and a constant step light stimuli was used to silent the granule cells expressing Arch. The light delivery (positiondependent onset, distance-/time-based duration) was controlled by the custom microprocessor-controlled system.

The optogenetic manipulations shown in Figures 3 and 4 were specifically designed to identify which of the various synaptic input weights were changed by BTSP (CA3, DG or EC). To examine this, we attempted to affect only the synaptic input and associated biochemical signal (ET) within a neuron without affecting either plateau potential initiation or any signal associated with the plateau. Our rationale here was that the best location to place the manipulation was before the plateau induction because this reduces the likelihood of altering elements other than synaptic input, since those elements that we did not want to alter are either coincident with the plateau potential or after it.

The level of $\mathsf { V } _ { \mathsf { m } }$ ramp shift produced by optogenetic manipulations was quantified as the amount of shift required to minimize the difference between the decay portion of the $\mathsf { V } _ { \mathsf { m } }$ ramp (from peak to end of track) for test and control traces. The delta velocity was determined as the difference in the mean velocities for the time period during the light activation for test and control laps (velocity traces referenced to the beginning of light activation; Figure 5C) and quantified as a fractional change (DVel/average Vel). For Figure 5G, the net effect of light on $\mathsf { V } _ { \mathsf { m } }$ was quantified as the difference in the average $\mathsf { V } _ { \mathsf { m } }$ during the light and $\mathsf { V } _ { \mathsf { m } }$ for the same spatial bins of control traces from spatially-binned $\mathsf { V } _ { \mathsf { m } }$ ramps. Negative values represent net $\mathsf { V } _ { \mathsf { m } }$ hyperpolarization (i.e. less depolarization) during the light.

Comparison of optogenetic manipulations with other studies is difficult due to different recording conditions, manipulation durations and behavior.67–73 Most studies have recorded in CA1 (but see68,69) while inhibiting EC or CA3. The most common effect of inhibiting EC is an induction of global remapping of PF activity. Since this is a population phenomenon and we are recording from single cells it is difficult to compare our results (i.e. a shift in PF activity) with these other studies. However, as far as we can surmise no other studies have reported observing such a shift in PF activity.

# Histology

After the end of recordings, a LFP glass pipette loaded with DiI (saturated in DMSO) was lowered to 200 um above the CA3 pyramidal layer and a positive pressure (2–4 psi) was given to fill the pipette track with DiI. Mice were perfused transcardially with PBS and then with 4 % PFA in PBS after deep anesthesia with ketamine/xylazine (50 mg/ml and 10 mg/ml). The brain was dissected out and further post-fixed in 4 % PFA overnight, and then stored in PBS at 4 C. The fixed brain was cut into 100 mm thick coronal/sagittal sections with a vibratome. Sections around the recording site/optical fiber (with DiI/fiber track) were harvested and then incubated with fluorophore-conjugated streptavidin (1:1000, Invitrogen) against biocytin for 2 h at room temperature. The fluorescence images were acquired using Leica SP8X confocal microscopy (Figure 1A) or Zeiss AXIO Zoom.V16 stereo microscopy (Figures S6A–S6D).

# QUANTIFICATION AND STATISTICAL ANALYSIS

Statistical details of experiments can be found in the figure legends. Unless otherwise specified, measured values and ranges reflect mean ± SEM. Significance was defined as p < 0.05. Sample sizes were not determined by statistical methods, but efforts were made to collect as many samples as was technically feasible. No data or subjects were further excluded from any analysis.

# Computational modeling

# Schematic BTSP model

Related to Figures 3 and 4. CA3 inputs are represented by a set of 1000 gaussian functions (ampl = 1; SD = 0.5 s) whose midpoints were 10 ms apart. These functions are meant to mimic a sequence of tuned inputs moving in time from 0 to 10 s. Eligibility traces (ET) are convolutions of each of the gaussian inputs with an exponential function (t = 0.67 s). These signals simulate a biochemic al filter of the input. Plateau traces (PT) are the convolution of the plateau voltage signal (300 ms step) with an exponential function (t = 0.67 s). This signal simulates a biochemical filter of the plateau. Symmetric BTSP is produced by using activity filters (ET and PT) with the same time constant. Each input can have a weight from 0 to 1 and are initialized to 0.1. To simulate learning via BTSP, weights

are changed according to a BTSP learning rule that only contained a potentiation component $\Delta \mathsf { W } = ( 1 - \mathsf { w } _ { 0 } ) \mathsf { q } _ { + } ( \mathsf { E T } \cdot \mathsf { P T } )$ , where $w _ { 0 }$ is the initialized weight, q+ was a sigmoid function (slope = 0.1; midpoint = 0.25). Inputs are then scaled by the weights and summed to simulate a $\mathsf { V } _ { \mathsf { m } }$ ramp.

To mimic the optogenetic inhibition of CA3 input during BTSP induction, two out of every three inputs were set to 0 either for the remaining duration of simulation if the inputs peaked during the manipulation or for the duration of the manipulation if they peaked after the manipulation (Figures 3G and S8C). The manipulation occurred just before the start of the plateau (3–4 s; plateau initiation at 4.25 s) during the simulation run used to calculate DW. The manipulated inputs generated ETs with reduced amplitudes and thus reduced weight changes. Standard input trains (i.e. without manipulation) were then scaled by the resulting weight distribution and summed (see Figure 3I). To mimic the inhibition of EC input, inputs were held that their current value for 0.5 s just before the plateau and then allowed to continue by altering the gaussian function accordingly (Figures S4G and S8D). These prolonged inputs produced elevate ETs that were used to calculate DW. The resulting weight distribution was then applied to normal input sequences and these inputs were summed. To simulate the effect of such input manipulations on already formed ‘‘PFs’’ the same manipulations we applied to the inputs and a standard weight distribution was used to scale each of the inputs. These inputs were then summed.

# Binary model

Related to Figure 6C. To gain a deeper understanding of the storage and retrieval capabilities of a network endowed with BTSP under general conditions, we sought to simplify the underlying rule governing synaptic plasticity while preserving the essential aspects of BTSP. We report a complete derivation and mathematical analysis of this rule in supplemental information, but we briefly describe the main concepts and features of the rule below.

We discretized time into broad windows (4 s) and introduced binary signals for the neurons, which differed depending on whether the neuron was pre- or post-synaptic for a given synapse (Figures S9A and S9B). The two most prominent synaptic changes in BTSP occur in the form of (1) potentiation in the presence of presynaptic activity/plateau and postsynaptic plateau occurring within 2 s of each other, and (2) depotentiation with temporally offset (from 2 s to 4 s) postsynaptic plateau and presynaptic activity/plateau. Further, by assuming that synapses are binary (being either in a potentiated or depotentiated state), we approximated BTSP as:

$$
W (t + 1) = W (t) + (1 - W (t)) q _ {p r e} (t) q _ {p o s t} (t) - W (t) \left(q _ {p r e} (t) q _ {p o s t} (t - 1) O R q _ {p r e} (t - 1) q _ {p o s t} (t)\right) \tag {Equation1}
$$

where W = 0; 1 represents whether the synapse is depotentiated or potentiated, respectively, $\mathsf { q } _ { \mathsf { p r e } } ( \mathsf { t } ) = 0 ,$ ; 1 represents whether activity or plateau occurred in the presynaptic neuron at time t and ${ \sf q } _ { \sf p o s t } ( { \sf t } ) = 0 ,$ ; 1 represents whether or not a plateau occurred in the postsynaptic neuron at time t.

We next sought to eliminate the dependency on ðt  1Þ from the dynamics in Equation 1, in order to allow an analysis of these dynamics in terms of a Markov chain. By introducing the variables $\alpha ( t ) = W ( t ) q _ { p r e } ( t - 1 ) , \beta ( t ) = W ( t ) q _ { p o s t } ( t - 1 )$ Þ, the dynamics in Equation 1 becomes:

$$
\left\{ \begin{array}{c} W (t + 1) = W (t) + (1 - W (t)) q _ {p r e} q _ {p o s t} - W (t) \left(\beta (t) q _ {p r e} + \alpha (t) q _ {p o s t} - \alpha (t) \beta (t) q _ {p r e} q _ {p o s t}\right) \\ \alpha (t + 1) = W (t) q _ {p r e} + (1 - W (t)) q _ {p r e} q _ {p o s t} - W (t) \left(\beta (t) q _ {p r e} + \alpha (t) q _ {p r e} q _ {p o s t} - \alpha (t) \beta (t) q _ {p r e} q _ {p o s t}\right) \\ \beta (t + 1) = W (t) q _ {p o s t} + (1 - W (t)) q _ {p r e} q _ {p o s t} - W (t) \left(\beta (t) q _ {p r e} q _ {p o s t} + \alpha (t) q _ {p o s t} - \alpha (t) \beta (t) q _ {p r e} q _ {p o s t}\right) \end{array} \right. \tag {Equation 2}
$$

This system exhibits an exponential memory decay (see Methods S1). When presynaptic and postsynaptic activity and plateaus are temporally uncorrelated, the memory span of the system (the time constant of the exponential decay) is given by

$$
\tau_ {u n c o r r} \approx \frac {1}{6 f _ {p r e f} f _ {p o s t}} \tag {Equation 3}
$$

up to logarithmic corrections, where $f _ { p r e }$ is the probability of having activity or plateau presynaptically at each time step, and $f _ { p o s t }$ is the probability of having postsynaptic plateau. When presynaptic activity is correlated in time, we find that the memory span becomes:

$$
\tau_ {c o r r} \approx \frac {1}{6 f _ {p} ^ {2} + 2 (3 - c - c ^ {2}) f _ {a} f _ {p}} \tag {Equation 4}
$$

with $f _ { p }$ representing the plateau probability, $f _ { a }$ representing the activity probability, and c represents the correlation of activity at adjacent timepoints. The capacity estimate based on the SNR from network simulations reported in Figure 6F had parameters $f _ { a } = f _ { p } =$ 10 log N=N and $c = 0 ,$ .

# Network dynamics for storage capacity

In Figure 7B we built an attractor network using the weights learned from a recurrently connected network with global inhibition and thresholded activity described by the dynamics:

$$
A _ {i} (t + 1) = \Theta \left(\sum_ {j} \left(W _ {i j} - \bar {W}\right) A _ {j} (t) - \theta\right) \tag {Equation 5}
$$

where $\vec { A }$ is the population activity, $W _ { i j }$ is the learned matrix, $\overline { W }$ is its average, Q is the Heaviside function (1 when its argument is greater than zero and zero when the argument is less than zero), and  is a threshold. The threshold was chosen to be m + 3:5s where m and s are the mean and standard deviation of the distribution of inputs to units which are inactive $\sum _ { j } W _ { i j } q _ { p r e } ^ { j } \big | q _ { p o s t } ^ { i } = 0$ . The attractor capacity was defined as the number of steady state activity patterns that the network can retrieve. To define successful retrieval, we built a decoder that chooses the pattern with maximal correlation to the steady-state attractor activity and compared this decoder’s output to the pattern that seeded the attractor activity. The attractor capacity is then the number of patterns correctly decoded before the probability of correct decoding drops below 0:5, with error bars denoting correct decoding crossing 0.75 and 0.25 in a sample of 400 trials. The results of varying c with N = 3000, $f _ { a } = f _ { p } = 1 0$ log $N / N$ are plotted in Figure 7B.

# Network dynamics for continuous attractors

For the results reported in Figures 6A, 6B, and S9C–S9E, we used the continuous version of the discrete BTSP model. To derive the model, we first compute the difference of each variable between time t + 1 and t from Equation 2. We then take the average across realizations of pre and postsynaptic signals In order to compute the average of the product $\alpha \beta ,$ , we have to introduce an additional variable $\gamma = \alpha \beta$ aband derive its dynamics. We finally approximate the finite difference with a time derivative. This results in the gdynamics:

$$
\left\{ \begin{array}{c} \dot {W} = (1 - W) q _ {p r e} q _ {p o s t} - \left(\beta q _ {p r e} + \alpha q _ {p o s t} - \gamma q _ {p r e} q _ {p o s t}\right) \\ \dot {\alpha} = - \alpha + W q _ {p r e} + (1 - W) q _ {p r e} q _ {p o s t} - \left(\beta q _ {p r e} + \alpha q _ {p r e} q _ {p o s t} - \gamma q _ {p r e} q _ {p o s t}\right) \\ \dot {\beta} = - \beta + W q _ {p o s t} + (1 - W) q _ {p r e} q _ {p o s t} - \left(\beta q _ {p r e} q _ {p o s t} + \alpha q _ {p o s t} - \gamma q _ {p r e} q _ {p o s t}\right) \\ \dot {\gamma} = - \gamma - q _ {p r e} q _ {p o s t} (\alpha + \beta - \gamma - 1) \end{array} \right. \tag {Equation 6}
$$

In Figure S9C we estimated the change in synaptic weight by simulating these synaptic dynamics in the presence of Gaussian pre and postsynaptic signals, mimicking a postsynaptic plateau centered around $t \ = \ 0 ,$ , and presynaptic plateaus at 50 equally spaced timing from 4 s to 4 s. We repeated this procedure for 50 different initial values of the initial weight.

The Gaussian profiles had a standard deviation $\sigma = 0 . 7 5 s$ . For Figure 6A we modeled one plateau for each unit i as baseline substracted firing rate profiles described by Von Mises functions:

$$
\frac {e ^ {\kappa \cos (\nu t - \theta_ {i})}}{2 \pi I _ {0} (\kappa)} \tag {Equation 7}
$$

where $v = 2 \pi$ is the velocity of the simulated animal in a circular environment (one lap in $2 s ) , \kappa = 4$ is the concentration parameter, and $I _ { 0 } ( \kappa )$ p kis the zero order modified Bessel function of the first kind. Each of the N = 16 (Figure 6A) or $N = 3 2$ (Figure S9D) units in the knetwork emitted a plateau around location $\theta _ { j } ,$ , which was uniformly spaced along the circular environment. The synaptic dynamics qwas simulated for ten laps, starting from a uniform initial condition for the weights, $w = 0 . 2 5$ . We then used the resulting weight matrix $W _ { i j }$ in a rate model dynamics

$$
\tau \dot {h} _ {i} = - h _ {i} + \frac {J}{N} \sum_ {j} \left(W _ {i j} - \bar {W}\right) \phi \left(h _ {j}\right) + I _ {0} + I _ {1} \cos \left(\theta_ {i} - x (t)\right) \tag {Equation 8}
$$

where $\tau = 1 0$ ms is the integration time constant of the individual units, $J = 1 5$ is a scaling factor for the weights, $\overline { W }$ is the average of the weight matrix across all elements, $\phi ( )$ is the threshold-linear function, $I _ { 0 } = 2$ is a constant uniform input, and the last term fdescribed a tuned external input around the location of the animal x t (red line in Figures 6B and S9E). $I _ { 1 } = . 2 5$ (Figure 6B) or I = 2:5 (Figure S9E) was the amplitude of the tuned external input. $I _ { 1 }$ was set to 0 to probe the existence of attractors in the network (Figures 6B and S9E time interval without the red line). Figures S9D and S9E show the effects of having a shifted plasticity profile, resulting in an asymmetry. This is equivalent to shifting the relative timing between pre- and postsynaptic signals, which was achieved in simulation by a relative shift of 30 ms.

# Supplemental figures

![](images/93cecd81c8bd70c4721f85b7579b708a4e9208ff7b9297ec88b645380c2eb041.jpg)  
A

![](images/b4dfa28c54fe2cc7918682acc6f976fc7dd163757f7d51a4f6a260fd00f8050d.jpg)

![](images/f957455cd29f352308eacf927aa5eb3e27537d098eba45b0bc85fd61d81206aa.jpg)

![](images/83d074cc2bd942273d098a4b19948679c7cfb1252feed2e670058652ddfc4f9f.jpg)  
C

![](images/75e0c299d46c408bd1f1f7c6ce020f81bfaf339a604e9ac3a2c0da0929321e49.jpg)  
H

![](images/b17ee6180567d0cbadca7d162313b445055248021e0658165180486d11fc6a6e.jpg)

![](images/b57782357fde2b7b80fe564a76115df1bce153ed245df8ad74df341afaa332bf.jpg)

![](images/0f585d72c350f774787a818f88336afde36f6ca129ec4d09fdfd7f578106a22f.jpg)  
F

![](images/0f8652640693fc0738aabb518ab4bc555029dcb94a2b254ade0e48b096cab5ab.jpg)  
K

# Figure S1. Possible attractor formation mechanisms in CA3, related to Figure 7

(A) CA3 circuit schematic showing various excitatory synaptic input pathways and their approximate locations on a pair of CA3 pyramidal neurons comprising a single attractor.   
(B) Upper, a bidirectional synaptic plasticity rule expressing a symmetric time course of potentiation (positive values) and depotentiation (negative values). Such a plasticity rule applied to recurrent synapses will build balanced weights among neighboring cells (as blue arrows in F), thus producing a stable activity pattern that persists at a given location. Middle, eligibility traces (ET; blue) produced by convolution of Gaussian inputs with an exponential (tau = 0.5 s) for inputs ±2 s around plateau (before, dashed line; after, solid line). Plateau trace (PT; black) produced by convolution of step function and exponential (tau = 0.5 s). Lower, the overlap area of the ETs and PT (same as the filled area in the middle panel) is similar for both the input before and after the plateau due to the symmetric plasticity rule (numbers indicate the area of overlap).   
(C) Behavior of an animal (solid and dashed figures are current and future locations, respectively).   
(D) An additional excitatory input is needed to update the activity in the attractor network in (E) based on the movement of the animal in (C).   
(E) A different set of neurons active at different locations that are linked to the animal’s behavior in (C) (solid dark red arrow in (D) is current active external input, solid black Gaussian is current activity; dark dashed arrow in (D) and Gaussian are signals at future active locations and light solid arrows and Gaussians are signals at intervening active locations).   
(F) Same as (E), but a ring version53 of this attractor system where a symmetric rule (blue arrows; solid is potentiation and dashed depotentiation, as in B) combined with uniform inhibition (not shown) produces a bump of activity (black Gaussian at black circles) whose movement is determined by an updating mechanism linked to behavior (red arrows). Solid red arrow and black Gaussian indicate the current active external inputs and activity bump, while dashed red arrow and black Gaussian indicate the activity at a future location. Shading of circles around bump indicates symmetric spread of synaptic current due to the symmetric plasticity rule in B).   
(G) Same as (B), but BTSP in CA1 with an asymmetric time course. Note the tau of eligible traces (ET; blue) is 1 s, and large difference in the overlap area resulting from the asymmetric plasticity rule.

![](images/27b7558f3261119dfbbf2212a6a794eede41940ce094749256bf004cee0527e8.jpg)  
A

![](images/dae2af1ec911bcc7f12dcaee67a94c5b6fea9139b91c7bc2c371e40b55498360.jpg)

![](images/d42a7920e53c3f73f099144aa3797d0bdf1b1d698a7d556725ea4f15d862479e.jpg)

![](images/8ef5da0ad5f628e48b5d4fd6eaa0ae0b7e37792915d3e78717068f7aec6c154a.jpg)

![](images/f2e9712122bf38d571b41fbd168266699a3283bddd05ab9658a76f7580d95d35.jpg)

![](images/28509d654a8429c35567e1b246726504c42124b42f1697c53b3c8aff36b62526.jpg)

![](images/7ad528d3ad12c2d2b20940fb861f646100dc889cdf4a98f00ad780c43dbc1743.jpg)  
B   
C

![](images/5c743b7f2af097a925c5aa0d166a453ab76e0e2d7cae46370cf85d46d3baea33.jpg)

![](images/4ff8500919e1bd9428cc9d0d85aaf8eecf705c4e494c1dfd92712278193a7b4b.jpg)  
D

![](images/08de950ecb161a6f1d6a340e161c348a2c1a4bdf20d36deb784493bc3efc4187.jpg)  
E

# Figure S2. Natural PC recorded from hippocampal area CA3, related to Figure 1

(A) Spatially binned (100 bins of 1.8 cm) unsmoothed average AP rate, V ramp, and $\mathsf { V } _ { \mathsf { m } }$ theta amplitude (averages from 5–48 trials) for all 46 PCs recorded from CA3. Recordings are sorted by peak AP rate location.   
(B) Average AP rate (shading is SEM) for all PFs aligned to the location of PF peak AP rate of individual natural place cells.   
(C and D) Same as (B), but the $\mathsf { V } _ { \mathsf { m } }$ ramp and the $\mathsf { V } _ { \mathsf { m } }$ theta amplitude, respectively.   
(E) Same as (C) in Figure 1, but the average of even and odd trials, respectively. r = 0.56, p < 10e–5.

![](images/18fa2f37e15496854efb122aa0ebce102e85c50ba3bc5fe802bf59b25f3a2486.jpg)  
A

![](images/4af4b95301afcd2e948d709ffa3b0e28418d451384e74b7a19ac39b2f7ef49e9.jpg)

![](images/d15238171d27e54e0b49165d4804e90a16893e0cb039bba4248b0614b9abdc94.jpg)

![](images/83920b8ca649bd9782e7c041fcd44684daa4743d83f5d31af067c6d53f8269a3.jpg)

![](images/8f2f1838719e8df705522dfe41e68eae5ec0ccb9259be2306c6b771266101c36.jpg)

# Figure S3. Naturally occurring long-duration plateaus in CA3 neurons, related to Figure 2

(A) Average of spatially binned $\mathsf { V } _ { \mathsf { m } }$ ramps (gray, laps before plateaus; black, laps after plateaus) from all 14 neurons exhibiting naturally occurring long-duration plateau potentials. Sorted by the location of the plateau.   
(B) Same as $( \mathsf { A } ) ,$ but changed $\mathsf { V } _ { \mathsf { m } }$ ramp in time from all 14 neurons.   
(C) Raw $\mathsf { V } _ { \mathsf { m } }$ traces of naturally occurring long-duration plateau potentials. Red asterisks denote location (time) of peak positive $\Delta \mathsf { V } _ { \mathsf { m } } .$   
(D) Histogram of ADP duration during naturally occurring plateau potentials.   
(E) Expanded $\mathsf { V } _ { \mathsf { m } }$ trace (black) from the uppermost trace in (C). The median filtered $\mathsf { V } _ { \mathsf { m } } ,$ to remove APs, is superimposed (red). Dashed gray line indicates threshold for plateau determination.

![](images/f881f949f5c9941d7f6735e7f021ba759cae1d2f8cd1d70269614b6f71823725.jpg)

![](images/815b0ff4465fd92896a92331f5052625f668d4241241a47d82f5751dd3fd8993.jpg)

![](images/219d564a5ec6e115045915c826be58c09f89d9f6ec0af97e1f0d20ea01b1fdca.jpg)

![](images/8c752722f874c556a085dc736342b891ae0f46541e8f7dba68dcf0d4cfc3b9ed.jpg)

![](images/539d197deaec92f7da74649616e64cc15eba68b205d3073ad4db1cc70921d69b.jpg)

![](images/9f328bbb41b9e33ac1bb4f6c50b5d27a94bbd41441f10e90d61d970857fcad0e.jpg)

![](images/7b42629108a262ca24f9b5897a46601903266a528707e131590dad576435ca13.jpg)

![](images/b8cddc0c1d38b42a4c0ebe8a9418b68f129def474358b3bfd1342081edb6156a.jpg)

Figure S4. Induced plateaus generate PFs in CA3 neurons, related to Figure 2   
![](images/320a8ac4c4d811c053898b142e1e87332350d2d162cc8e07026cbfd80b4ee976.jpg)  
(A) Average of spatially binned $\mathsf { V } _ { \mathsf { m } }$ ramp (gray, laps before induction; black. laps after induction) from all 70 recordings. And $\Delta \mathsf { V } _ { \mathsf { m } }$ ramp in time from plateau. Sorted by the location of the plateau.   
(B) Spatially binned change in $\mathsf { V } _ { \mathsf { m } }$ ramp caused by three trials of induced plateau. Red asterisks in (B)–(E) indicate location of plateau induction.

![](images/35ea128d64462424ccba3ec75b1ae7ad12bb3e2736ead7de883b981778e315d8.jpg)

![](images/20033224fd9657389f06a2cebb03f94bfba7b42fc6545eafbe7818f35cc198dc.jpg)

![](images/1b5c94c912267e36bde589cdf4736446b27402c88e6c25948cd228610c0237f6.jpg)

![](images/7edc27b35f2d153ecd84c81622932b4aa760640deb576e1a6cb58b2ea09277cc.jpg)

![](images/63cd69d7ab3570909354f9f8e1dd0239cab625a501d94d858f2318887a4e69f7.jpg)

![](images/68dcbcf56bad29c0e71a4f559116ee635ddcd618862b7bb5c622350ccf5d2a80.jpg)

![](images/99de0c7d032ad0760e8936265884c082bab0fad7be55d247728d0c3d8c1c6deb.jpg)

![](images/cff0bea8fcf692e10ca16b69e1720104665085cb3a3e780a771790996145ef44.jpg)

![](images/0df3079b79679ff92c3545fd02e6c2c163ec1c42957b4313a35558eda93af75b.jpg)

![](images/506c0c14819e60c40d010a04dc8b6fcb307263247c5b75ad09c3cfb8fda92c14.jpg)

![](images/8d98213dc0baff4aaaf42b01172e8870747eb312bd0021d95aa9ebb61f81a1fb.jpg)

![](images/fd69677ec78ff4c04f94c11a43ae65cb811002dcfbceb3ab41af63fa7690d19d.jpg)

Figure S5. Plateau trains and 100 Hz AP trains induction, related to Figure 2   
![](images/df9f6c122ff0e012ba9f56ae348730282653c80fc750f3705a8f7ced55fa03ce.jpg)  
(A) Five spatially binned induction trials $( \mathsf { V } _ { \mathsf { m } }$ with APs removed) showing induction currents that were injected at three different locations across the distance of the track within the same trials in a single neuron ( 30, 90, and 150 cm).   
(B) Spatially binned $\mathsf { V } _ { \mathsf { m } }$ ramps (gray, laps before induction; black, laps after induction) from the cell in (A).   
(C) Same as (A), but plotted versus time base showing that they are centered on the middle current injection.   
(D) Same as (B), but plotted versus time base.   
(E) Average spatially binned $\mathsf { V } _ { \mathsf { m } }$ ramps (gray, laps before inductions; black, laps after inductions) from population of four neurons receiving the same multiple induction protocol.   
(F) Same as (D), but shown four individual cells (gray) and the average (black). Note that the time course of the change is similar to that induced by a single current injection (Figure 2L). Induction protocols in (A)–(F) were used to mimic trains of plateaus in Figure S3C.   
(G) Membrane potential $( \mathsf { V } _ { \mathsf { m } } ;$ black) and mouse position (green, 0–180 cm) for laps before (7, 11, and 12) during (13) and after (18, 19, and 31) 100 Hz spike train induction (5 laps total).   
(H) Average firing rate before (gray) and after (black) 100 Hz spike train induction from the cell in (G).   
(I) Average $\mathsf { V } _ { \mathsf { m } }$ ramp in space for laps before (gray) and after (black) 100 Hz spike train induction from the cell in (G).   
(J) Same as (I), but the difference of $\mathsf { V } _ { \mathsf { m } }$ ramp in time.   
(K) Same as (J), but the population average. Solid lines and shading indicate mean and SEM.

![](images/b75bf76b8f8c7b2d13a2f272ab099c0e77ea80ed801d18e4d10d8f342661476a.jpg)  
A

![](images/27527fe5525b179141baf196df171221d2465ee486ac0051cf780fd1ff79dd30.jpg)  
B

![](images/7a03c1f196923464d7231b6a7fad2aeb8635eab25196eb6839e54fe0627ee5a3.jpg)  
C

![](images/fc561df04806164a4c32387bfadd8d170b50b06e37488a07902c87073694cde2.jpg)  
D

![](images/f5ad720f5da299c5d603b100a3ad8a6abe2a2f13db59e2ebde5c83f9a28d7621.jpg)  
E

![](images/c5418a5aef034555a20aa043c29731018ef20e168f2b0a2ec604d974fb38a69e.jpg)  
F   
inhibitory extracellular currents in CA3   
G

![](images/fbd1a2a0c82b5ef6355e3eb16ab02925f64769805f9866243fed35b435474d89.jpg)

![](images/ab66af14c9810484a2000e2405ce6aacc66a771a04f0ae1d6c1eea7389e62aba.jpg)

![](images/776c0ec49701b3f60877b3c5b80da93dbe001bb0653b2a6fc87ce3d92ffa473b.jpg)  
I

Figure S6. Expression of optogenetic actuators, implantation of optical fiber, and validation of DG manipulation, related to Figures 3, 4, and 5 (A) Histology shows the optical fiber and pipette tracks for CA3 silencing with PV-cre:: ReaChR mice. Arrows indicate the recording site in CA3 and optical fiber end on the hippocampal CA3. R and L indicate right and left hemispheres, respectively.

(B–D) Same as (A), but for control, DG silencing and ipsi-EC silencing with different transgenetic mouse lines, respectively. Scale bar, 1 mm.   
(E) Sketch of manipulation condition showing CA3 location of optical fiber, CA3 location of extracellular recording, and DG location of intracellular recording.   
(F) Optical activation (yellow) of archaerhodopsin in DG axons/terminals produces hyperpolarization related local field currents (sources) in CA3.   
(G) Repeated optical activation of archaerhodopsin in DG axons/terminals (yellow, middle) drives $\mathsf { V } _ { \mathsf { m } }$ hyper-polarizations in an example of DG granule cell. Intracellular $\mathsf { V } _ { \mathsf { m } }$ (black, top) and current injection (gray, bottom). Note positive current injection drives AP output that is blocked by archaerhodopsin activation.   
(H) Average $\mathsf { V } _ { \mathsf { m } }$ of baseline (left) and depolarized (right, after current injection) during light off (control) and on (light) from 9 granule cells (2 animals). Lines indicate the same cell. Outside solid dot indicates the mean. The statistic differences are shown (parried Student t test).   
(I) AP rate after current injection at light off (control) and on (light) from 9 granule cells (2 animals). Outside solid dot indicates the mean. The statistic difference is shown (paired Student t test).

![](images/ab5f1800eeac2c29f4deb13b0eec865f625be94ff3262e7463f92b6faa08960b.jpg)

![](images/169fb0d9e3b82de51e0491b104406b60e68f587757321f6cf0d4a4faef1941ed.jpg)

![](images/d2479242f486b17a0ede93f5b5170cfef623070e1c982ab6c80f244fdf3ff76c.jpg)

![](images/d2945d6100243b0739f449bcde9b3c0c1e14701d3368b1c1e002423ad0a1374f.jpg)

![](images/c873d6c8c6a4ba9f8f9ad86add474cd446966deb8d1b73cc45c2ccfd7594645b.jpg)

![](images/17c31f15167f2420a753ca30a7141e37374b972c64c9b58b4e36cfd2945f72b7.jpg)

![](images/3f124d7488d21b50cfdbf35f9c4de0c3826ad32a6848b7b9a62082b475d1e9ad.jpg)

Figure S7. Effect of optogenetic manipulations on BTSP induction, related to Figures 3 and 4   
![](images/5db49ee2d32ed8893c736ef4ef78dbd80aaa55bd314cccd40e3fb3c25f126be6.jpg)  
(A) All changes in $\mathsf { V } _ { \mathsf { m } }$ ramp for individual neurons from CA3 manipulation (blue).   
(B) (From top to bottom) sketch of protocol for optogenetic silencing in control group; $\mathsf { V } _ { \mathsf { m } }$ traces for laps before, during, and after induction; $\mathsf { V } _ { \mathsf { m } }$ ramps for laps before (gray) and after (black) plateau induction and difference between $\mathsf { V } _ { \mathsf { m } }$ ramp after and before plateau $( \Delta \mathsf { V } _ { \mathsf { m } } )$ ) for single neuron from control group. Yellow lines indicate the light location, duration, or covered distance.   
(C) Same as (A), but individual neurons from control (black).   
(D and E) Same as (B) and (C), but for DG manipulation group (green).   
(F) Same as (A), but individual neurons from EC manipulation (red).

![](images/f4375d8dd2e4c348b902d4db2c7d3a69b8bd64a5bb1942c9ca75cdd3f7191bef.jpg)

![](images/e9017d51975e681d74e3cf236c18fed6a5629652cb716663d715fc16b7090b2f.jpg)

![](images/dffa0eb3d6f5d352b1a04f70bf4529dafca84aa13d973c69462feec41118d3cc.jpg)

![](images/3a9e615f0b3805b83c4dccdab472b078e3de3426e1a8e5980ff9292af61daf02.jpg)

![](images/e01c641f0f24a8a695d8655a11ffc83358aa1193fd6105cf59c953a45f244037.jpg)

![](images/ede94337e1583d078d0f84366e6362825501262ca910aec4469eedcb8d33d3a3.jpg)

![](images/7d107b51a524f041a235fb68107c698d12dd4c4faa77db40a7b9edb78dec605f.jpg)

Figure S8. Effect of optogenetic manipulations on CA3 PC activity, related to Figure 5   
![](images/1df9db2b24008a64d3eb8ea9f7d232ba77d5110f269e722bdd6e06ae9f3ba8ed.jpg)  
(A) Mean spatially binned AP rate for control (black) and intervention (red) trials for EC manipulation in population where light was far from PF peak (> 20 cm; left) or near to PF peak (< 20 cm; right). Only neurons that showed AP firing at the position of the light were included (* in E indicates neurons excluded due to no APs). Symbols indicate significant differences (two-tailed unpaired Student’s t test, p < 0.05). Solid lines and shading indicate mean and SEM. Yellow lines indicate the light-covered distance.

![](images/ca6bfdde66e9e39b322e31758bd4da01d6537ec752af3c00ee2c2b92f542eab6.jpg)  
A

![](images/62f58463bc9d29869ad5b32690b7bdbcbc0d49395d39564ffb34f552e616a3ef.jpg)  
B

![](images/54be389de72d1ff6f7183b15c49b58869a74fd12cbb43b49ae7c19bb67a83b73.jpg)  
C

![](images/4fa2772b438b14ee845bbbc12a3a95baa37fdc287ee3593c6de157edcf59ccc1.jpg)  
D

![](images/2a1f095927a36f0b4c7a67b60153df8455d06c77cb4e9aacc5bd4ade888e02b7.jpg)  
E

![](images/ee293167f2b3db7b1fffde5de5937b5a5024717d7ced748579244d417a89080a.jpg)  
F

![](images/00be834c20727e37fe2ea7e85b6f39b8b897a2102739370adc1b47d296abf14e.jpg)  
G

![](images/01e6f3ef220becf2f972686a988b2e275434c446c2a6d2b26f84923933c1d1e1.jpg)  
H

![](images/3467f445d953d2e7be10d0cabd71f951c8afcd7148743872c499c6152878e826.jpg)  
I

![](images/175391d5b4aa4781cdf94829159d0f7043859f366ea06e1d2c6b9592faa437f3.jpg)  
  
BTSP confusion matrix

![](images/9a9e9df95029a66cd16949a80f5af6b8ff1926d1f27055ab546eef290767aa4c.jpg)  
K   
Hebbian rule confusion matrix

# Figure S9. BTSP model, related to Figures 6 and 7

(A) Complete binary BTSP rule. Left: A depressed synapse (blue) is potentiated (yellow) in the presence of presynaptic (plateau or activity, left/right) and postsynaptic (plateau only) signals at the same time. Right: a potentiated synapse undergoes depression if a postsynaptic signal (plateau or activity) follows or precedes a presynaptic signal.   
(B) Left: synaptic patterns learned in the network after the presentation of a single pattern. Potentiated synapses (thick edges) form a self-reinforcing assembly among plateau-emitting neurons (black circles). The assembly receives feedforward input from active neurons (red circles) through potentiated synapses. Right: Subsequent transient reactivation of the units will drive persistent activity in the assembly.   
(C) Continuous time and continuous weight version of BTSP (Equation 6 in STAR Methods). Change in synaptic weight (color coded), as a function of the time interval between single Gaussian pulses for presynaptic and postsynaptic signals (x axis) and initial weight (y axis). Black curve denotes combination of pre-post timing and initial weight resulting in no weight change.   
(D) Asymmetric weight matrix representing connections between neurons with uniformly spaced plateau potentials and a temporally asymmetric form of BTSP (reminiscent of BTSP observed in CA1).   
(E) Neural activity from network with weight matrix from (F) as the virtual animal moves through the environment exhibits a moving bump of activity that tracks the animal’s location during externally driven input (red lines), but the bump exhibits rapid movement in the absence of external input.   
(F) Signal-to-noise ratio estimated from simulations of independent synapses undergoing BTSP (Equation 13 in Methods S1, black circles) and from the approximation based on the second leading eigenvalue of the transition matrix from the corresponding Markovian description of BTSP (Equation 16 in Methods S1, red dots). The age of the patterns increases from left to right, from the most recently stored to the most remote.   
(G) Same as (C), but with correlated activity across time bins and including the full theoretical solution (yellow line/dots).   
(H) Confusion matrix for a network that learns with BTSP describing the inputs one plateau pattern receives of the input-plateau pattern showing that jumping from one attractor state happens less often than chance (white represents chance).   
(I) Confusion matrix for a network that learns with a same-time learning rule, demonstrating that performance is limited by attractor states confusing adjacent patterns for one another (white represents chance).   
(J) Pdf of confusion matrix entries for BTSP in the presence of temporally correlated activity (Equation 20 in Methods S1) for the last 100 patterns learned by the network color coded by time difference between the input pattern and plateau pattern. The theoretical predictions are plotted against the simulated values (inset).   
(K) Same as (J), for the same-time rule. Note how adjacent patterns may be confused more easily for the same pattern than random patterns, unlike in BTSP. Parameters for all panels are in STAR Methods and supplemental information.

Figure S10. Pattern separation of correlated patterns with BTSP, related to Figure 6   
![](images/7442a5b64316849896a469658bf92a77b8440cdbc348509baa275751c1c03d92.jpg)  
Evolution of network structure in the presence of BTSP. Top: left: for simplicity, the network is initialized with depotentiated synapses (thin edges). Middle: upon presentation of the first pattern (black: plateaus, red: activity), the subset of units with plateaus forms a mutually reinforcing group (thick edges) that receives feedforward input from active units. Right: upon presentation of a second pattern, weights among the overlapping plateau and active units across the two patterns are depotentiated, effectively reducing the interference between the first and second pattern (right). Bottom matrices: weights among units with plateaus are symmetric, forming an assembly of self-reinforcing activity (2nd row). Weights from active units provide feedforward activity to the assembly $( 3 ^ { \mathsf { r d } }$ row) but do nost participate in the assembly $( 4 ^ { \mathfrak { t h } }$ row).