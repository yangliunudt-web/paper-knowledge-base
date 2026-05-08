---
title: "Amorphous phase-change memory alloy with no resistance drift"
date: "2025-09-01"
year: 2025
journal: "Nature Materials"
doi: "10.1038/s41563-025-02361-0"
abstract: "Spontaneous structural relaxation is intrinsic to glassy materials due to"
abstract_cn: "自发结构弛豫是玻璃材料的固有特性，源于其亚稳态性质。对于相变材料，由此产生的电阻时间变化严重阻碍了神经形态计算应用。本文报道了一种从头算计算指导设计的非晶相变材料，由稳健的分子状基元组成，消除了引起弛豫和电阻漂移的关键结构成分。我们展示了非晶"
cite: "[1] Wang X, Wang R, Sun S, et al. Amorphous phase-change memory alloy with"
aiSum: "设计无电阻漂移的非晶 CrTe3 相变材料：从头算指导设计分子状基元，消除结构弛豫，在 ‑200°C 至 165°C 工作温度下无漂移，实现光电混合多级编码。"
confidence: "high"
---

# Amorphous phase-change memory alloy with no resistance drift
  - "[[Neuromorphic computing]]"

Received: 30 July 2024

Accepted: 1 September 2025

Published online: xx xx xxxx

![](images/a230a47fad89c0891b458b85790299005c6ce933382537863a573007de6ea941.jpg)

Check for updates

Xiaozhe Wang1,3, Ruobing Wang2,3, Suyang Sun1,3, Ding Xu1 , Chao Nie1 , Zhou Zhou1 , Chenyu Wen1 , Junying Zhang1 , Ruixuan Chu1 , Xueyang Shen1 , Wen Zhou1 , Zhitang Song  2 , Jiang-Jing Wang  1 , En Ma  1 & Wei Zhang  1

Spontaneous structural relaxation is intrinsic to glassy materials due to their metastable nature. For phase-change materials, the resultant temporal change in electrical resistance seriously hampers neuromorphic computing applications. Here we report an ab-initio-calculation-informed design of amorphous phase-change materials composed of robust ‘molecule-like’ motifs, depriving the amorphous alloy of critical structural ingredients responsible for relaxation and, hence, resistance drift. We demonstrate amorphous CrTe3 thin flms that display practically no resistance drift at any working temperature from −200 °C to 165 °C, and highlight the multilevel encoding ability via a hybrid opto-electronic approach. We further reveal that the same no-drift behaviour holds for melt-quenched amorphous CrTe3 in electronic devices. Moreover, the application potential of CrTe3 is testifed by its incorporation in a vehicle with an automatic path-tracking function. Our work provides an alternative route to achieve requisite properties for potential phase-change neuromorphic computing via the judicious design of disordered phase-change materials.

Data-intensive applications, such as artificial intelligence and the Internet of Things, are having a profound impact on nearly all aspects of life. The huge amount of data being generated at an ever-increasing rate poses formidable challenges to efficient data storage and processing. Neuromorphic computing or in-memory computing (IMC) based on resistive-switching non-volatile memory arrays, unifying storage with computing at the same location, can substantially improve the computing efficiency at a much lower energy cost1–4 . The key to high-storage-density neuromorphic computing is to obtain as many distinguishable resistance levels as possible in every memory/computing cell5 . Yet, high-precision IMC is facing a bottleneck problem associated with the intrinsic randomness of materials on programming6 , especially when operated at a working temperature (T) different from room temperature (RT). Continuous cooling is feasible at power farms,

but for the power-limited edge-computing platforms, temperature effects7–9 on accurate multilevel programming are much more critical.

Chalcogenide phase-change materials (PCMs), which utilize the large resistance contrast between their amorphous and crystalline states for data encoding10,11, are one of the leading candidates for non-volatile memories. The flagship $\mathbf { G e } _ { 2 } \mathbf { S } \mathbf { b } _ { 2 } \mathbf { T e } _ { 5 }$ (GST) alloys with moderate doping12 or heavy alloying13 have enabled the industrial production of high-density three-dimensional cross-point memory cards for computing servers and data centres with the operating temperature from ${ \bf \nabla } { \bf \cdot } 6 0 ^ { \circ } { \bf C } { \bf t o } 8 0 ^ { \circ } { \bf C }$ , as well as embedded memory units for automotive with a working temperature range from approximately −40 °C to 165 °C (ref. 14). Very recently, it has also been shown that crystalline PCMs and amorphous PCMs (a-PCMs) can survive the harsh space environment outside of the International Space Station15, where

![](images/61058f93ebbd888158b56ed0e5337b7ea6ad55dc8cb2f86d55650c50c2180fb6.jpg)  
a

![](images/5eb0c13251e7e310d240c25806c2af7b6a379cf4c1f71a6fed61e55c86d7caf5.jpg)

![](images/830abe8e2b0f07106cf583503f04756f024eb8a1bae3186b9e1c3270ffbe88fc.jpg)  
c

![](images/472e3485342dac7f014b9f8f68e73d0b79e9c2c886861c9fa6df2e68f26f1c2f.jpg)

![](images/98c372ef405045aba4e4cb35b55b172f34da0ac7f904493c53f4c882563fd7a3.jpg)  
f

![](images/3f03ed012225bc94c2dec6488017ef7f325abceafb1db422ea3bd431d767260c.jpg)  
Fig. 1 | Materials design, synthesis and characterizations. a, Relaxed atomic structures of c- $\cdot \mathbf { C r T e } _ { 3 }$ and melt-quenched $\mathsf { i } – \mathsf { C r T e } _ { 3 } .$ The Cr and Te atoms are rendered with red and light blue spheres and the $\left[ \mathsf { C r T e } _ { 6 } \right]$ octahedra are highlighted by orange polyhedra. b, ALTBC plot of a-CrTe3 showing no Peierls distortion at ${ \sim } 2 5 ^ { \circ } \mathbb { C }$ and ~165 °C. The black circle indicates equal bonds in c-CrTe3 (~2.7 Å). c, Calculated DOS of c-CrTe3 and a-CrTe3. d, XRD patterns of the as-deposited thin film and the thin films heated to 260 °C, 270 °C, 280 °C and $3 5 0 ^ { \circ } \mathrm { C } .$ . e, Temperature dependence of the sheet resistance of a CrTe3 film heated

temperature can cycle between $- 1 2 0 ^ { \circ } \mathrm { C }$ and $1 2 0 { } ^ { \circ } \mathrm { C }$ sixteen times per day. Beyond the success in these binary storage applications, PCMs do show multilevel storage capacity. However, the spontaneous structural relaxation—aging—of a-PCM causes intolerable resistance drift16–18. This is a pressing problem threatening the device accuracy needed for neuromorphic computing applications19.

Massive research efforts have been devoted to overcoming the adverse impact of resistance drift. On the device side, several approaches using mixed-precision computing19, algorithm compensation20, metal liner confinement21 and multi-PCM units22 were developed to partially mitigate the drift problem. It remains unclear whether these workaround solutions can still function at elevated temperatures or on extreme temperature cycling, but in any case, they add complexities to high-density device manufacturing and accurate multilevel programming. Therefore, a fundamental solution on the materials side, that is, PCMs with intrinsically low drift, is sorely needed. Previous attempts using impurity doping, heterostructure confinement and downscaling the film thickness only managed to reduce the drift tendency at $\mathsf { R T } ^ { 2 3 - 2 \mathsf { S } }$ . However, there is so far no candidate PCM that can generate many robust resistance states to function across a wide range of operating temperatures for various application scenarios. In the following, we offer a materials solution to diminish relaxation/drift once and for all, via a paradigm shift towards ‘molecular-glass-like’ a-PCMs. This approach enabled us to discover an a-PCM that is intrinsically

![](images/f89779d77a8ddd6404e214f5ae4e91f2074d1762d98a3cc398729f7dbf78a6d1.jpg)

![](images/e453ac76a705901132dde9af4c9e2bd9fb781ce049d599a30a295e273b55595f.jpg)

![](images/615177cabc1ae8afb38767a1239e34135b603077b05ebc4cd3b58b7f20dd593d.jpg)  
d

![](images/b725073633c75bf82c813772576415bd479da7057cc089386f795093e5225d06.jpg)  
e

![](images/7eb88a1288370dd3de1a2cccab80718d123595f9bb7cfd9464df4d33cc43a660.jpg)  
g

![](images/bf24e47557146a09168e64b6b834a9cc78a7e4d40b664d1c0162ea7f7c08a97d.jpg)  
up to 350 °C at a heating rate of 10 °C min− 1, and was then cooled to RT. f, van der Paul measurement of 34 units on a four-inch wafer. The 0.5 × 0.5 cm2 CrTe3 area in the middle of the substrate is contacted by eight tungsten electrodes (marked in yellow), which were patterned at the edges of the $1 . 2 \times 1 . 2$ cm2 substrate. g,h, TEM bright-field image (g) and the atomic-scale elemental mapping (h) of the c-CrTe film that was heated to 350 °C. The positions of the Te and Cr columns are marked in blue and red, respectively. The thickness of the films was ~150 nm for structural characterizations and ~50 nm for electrical measurements.

invulnerable to resistance drift at all working temperatures practically encountered in IMC operations.

# Design of molecular-glass-like a-PCM

On aging, a-PCMs are prone to structural relaxation. Conventional a-PCMs experience a gradual (1) reinforcement of Peierls distortion of (defective) octahedral motifs30 and (2) disappearance with increasing time (t) of salient structural defects30–32, including ‘wrong’ bonds (for example, Ge−Ge homopolar bonds) and tetrahedral motifs. Both these factors result in resistance drift. Our key idea is then to find an a-PCM that intrinsically has no such tendencies during time- and temperature-induced relaxation (Supplementary Note 1 and Supplementary Fig. 1). Figure 1a shows relaxed crystalline CrTe3 (c-CrTe ) calculated via spin-polarized density functional theory (DFT). First, the directional bonds of c-CrTe show no obvious Peierls distortion; the bond lengths are nearly identical, and the maximum difference is as small as 0.03 Å, an order of magnitude smaller than that of rhombohedral GeTe (~0.4 Å). Second, the crystal shows a layered structure composed exclusively of corner- and edge-sharing $[ \mathsf { C r T e } _ { 6 } ]$ octahedra. It is, thus, possible that its amorphous phase (a-CrTe ) would also contain a very high density of non-defective [CrTe ] octahedra with little Peierls distortion. To see if this hypothesis is valid, we carried out DFT-based ab initio molecular dynamics (AIMD) calculations to obtain a-CrTe models of 200 atoms following a standard melt-quench approach.

![](images/f22a5fe87cdf3d8f935e6d026d75bbc545500a93e80777b16e526dbc1e957b84.jpg)

![](images/1e48da9c3ad94736694d9f65867990bd73132b0ff1a16da9c939154582b22e34.jpg)

![](images/58d049119f52233bd2d6efa29a2eda6bb451a60b91b2b96570565b4cfa04b0b8.jpg)

![](images/a444afb871d5a4d105c0d703ef59c1d49fe21afb2bafae0cac74fd8eaa442f7f.jpg)  
Time (s)

![](images/f3aa66dd3597ec7fde96f6e8b10873c05c499f8f45883f492e51c15cb747a99e.jpg)  
Fig. 2 | Minimal resistance drift. a, Resistance drift measurement of as-deposited a-CrTe3 films on heating over 1 h, each at a different holding temperatures. b, Two as-deposited a-CrTe3 films were measured a $2 5 ^ { \circ } \mathrm { C }$ and $1 5 0 ^ { \circ } \mathrm { C }$ over 10 h (first part, displayed on the left). After aging for 3 days at RT, they were measured at 25 °C and 150 °C over 10 h again (second part, on the right). c, Resistance of the a-CrTe3 film measured at $0 ^ { \circ } \mathbb { C }$ and below. d, The a-CrTe3 film was subjected to extreme temperature cycling between –120 °C and 120 °C over 16 times in 24 h, and   
subsequently, its sheet resistance was measured $\mathfrak { t } ^ { - 1 2 0 ^ { \circ } \mathbf { C } }$ and $1 2 0 ^ { \circ } \mathrm { C }$ over time. The distinctive resistance levels were due to the varied thermally excited carrier concentrations at different temperatures. e, Summary of the measured drift coefficient of various a-PCM films. The drift coefficient is highly temperature dependent for other PCMs, for example, ν of a-Sb can be enlarged from ~0.001 at RT to $. 0 . 1 \mathbf { a t } - 1 7 3 ^ { \circ } \mathbf { C } .$ .

We first used the computed crystalline density directly, and the obtained atomic structure is shown in Fig. 1a. As highlighted using coordination polyhedra, almost all Cr atoms indeed form $[ \mathsf { C r T e } _ { 6 } ]$ ] octahedra (48 out of 50 Cr atoms, and the remaining two Cr octahedra have only one missing neighbour). This observation is further confirmed by quantitative structural analyses (Supplementary Fig. 2a).

We next evaluated the degree of Peierls distortion in the amorphous counterpart, that is, the a-CrTe3 model, by calculating the angular-limited three-body correlation (ALTBC) at RT $( \sim 2 5 ^ { \circ } \mathrm { C } )$ over directionally bonded pairs (bond angle, $- 1 5 5 ^ { \circ } - 1 8 0 ^ { \circ } )$ . In stark contrast with conventional PCM with an extended wing shape30, a-CrTe displays a single primary peak around 2.72 Å in the ALTBC profile at RT (Fig. 1b), which matches that of the c-CrTe (black circle). We also calculated the ALTBC profiles of a- $\mathrm { C r T } \mathbf { e } _ { 3 }$ at other (lower and higher than RT) temperatures (Supplementary Fig. 2b), and they show a picture consistent with that at RT. Further optimization of the amorphous model at RT leads to a volume expansion by ~2.1%, but the structural features remain the same (Supplementary Fig. 2c). Four additional $\mathbf { a } { \cdot } \mathbf { C r } \mathbf { T } \mathbf { e } _ { 3 }$ models in both crystalline and amorphous densities were calculated, which confirm that $\mathbf { a } { \cdot } \mathbf { \mathrm { C r T } } \mathbf { e } _ { 3 }$ consists of $\mathrm { [ C r T e _ { 6 } ] }$ octahedra connected in a disordered fashion, without obvious Peierls distortion and structural defects. In fact, octahedra are the only local configuration observed, and these motifs can, hence, be deemed molecule-like (Supplementary Fig. 3).

With the desired structural features in hand, the next challenge is the requisite electronic properties. For IMC applications, it is imperative for the PCM to have a large contrast window in electrical resistance on switching. The computed electronic density of states (DOS) predicts a major difference in electronic structure between c-CrTe and $\mathbf { a } { \cdot } \mathbf { C r T e } _ { 3 }$ (Fig. 1c). The crystalline phase is a semiconductor stabilized by antiferromagnetic interactions33. For the amorphous phase, we considered a couple of magnetic configurations, and the bandgap is always filled. Figure 1c shows the DOS for the ferromagnetic state, and other magnetic configurations are included in Supplementary Fig. 4. The open versus filled bandgaps should result in a sizable difference in electrical resistivity between the two states, with the amorphous state being the lower-resistance state, which

was observed in a similar layered PCM, that is, $\mathrm { C r G e T e } _ { 3 }$ (refs. 34,35). Importantly, as noted in Supplementary Fig. 2, the same octahedral configuration (‘molecules’ as well as their number density) stays predominant even when the temperature is elevated to $1 6 5 ^ { \circ } \mathrm { C } _ { I }$ , suggesting that a-PCM should also have excellent thermal stability across a wide range of operating temperatures.

# Wafer-scale synthesis of high-quality $\mathbf { C r T e } _ { 3 }$ films

We deposited CrTe films of ~50−150 nm in thickness on fourinch-diameter $\mathsf { S i O } _ { 2 } / \mathsf { S i }$ substrates at RT, using a pure Cr target and a pure Te target via magnetron sputtering. For the as-deposited film and the one heated to $2 6 0 ^ { \circ } \mathrm { C }$ at a heating rate of $1 0 ^ { \circ } \mathrm { C }$ min−1, X-ray diffraction (XRD) patterns at RT (Fig. 1d) show no crystalline diffraction peaks, except for the silicon substrate. After heating to $2 7 0 ^ { \circ } \mathrm { C } , 2 8 0 ^ { \circ } \mathrm { C }$ and $3 5 0 ^ { \circ } \mathbf { C } ,$ the (100), (200) and (400) peaks of $\mathbf { c } { \cdot } \mathbf { C } \mathbf { r } \mathbf { T } \mathbf { e } _ { 3 }$ appeared, indicating an out-of-plane texture. The lattice parameters obtained by XRD are 11.53 Å, 11.19 Å and 7.79 Å, in good agreement with the DFT calculation—11.49 Å, 10.92 Å and 7.91 Å, respectively. As estimated from X-ray reflectometry, the mass densities of the as-deposited amorphous and crystallized films were ~6.12 g cm−3 and ~6.39 g cm−3, respectively (Extended Data Fig. 1). Hence, on crystallization, a smaller increase in density $( \Delta \rho / \rho _ { \mathrm { c r y s t a l } } )$ was observed for CrTe3 (~3.9%), compared with GST (~6.4%)36.

Next, we monitored the electrical resistance on the in situ heating of the as-deposited film to $3 5 0 ^ { \circ } \mathrm { C }$ at a heating rate of $1 0 ^ { \circ } \mathrm { C } \mathsf { m i n } ^ { - 1 }$ using the van der Pauw method in an argon-protected environment. In agreement with our DFT prediction, Fig. 1e shows an inverse resistance contrast on crystallization for $\mathrm { C r T e } _ { 3 } ,$ , opposite to GST. The sheet resistance of the as-deposited amorphous film was ~7 kΩ sq−1 at RT, slowly and gradually decreasing on heating. Only after ${ \bf - } 2 3 0 ^ { \circ } \bf C$ , the sheet resistance drops more quickly (Supplementary Fig. 5), reaching a minimum at $T _ { \mathrm { x } } { \approx } 2 7 0 ^ { \circ } \mathrm { C } _ { \mathrm { \iota } }$ , where crystallization started, which is consistent with the XRD data. The sheet resistance of the crystallized film was measured to be 100 kΩ sq−1 at RT. According to the Hall effect measurements, the carrier concentration and mobility of the as-deposited film were $5 . 1 \times 1 0 ^ { 2 0 } { \mathsf { c m } } ^ { - 3 }$ and $6 . 8 \times 1 0 ^ { - 1 } { \mathsf { c m } } ^ { 2 } { \mathsf { V } } ^ { - 1 } { \mathsf { s } } ^ { - 1 }$ , respectively, which

![](images/a18b1fd03f07035347daaed8482e12b6ec37e6ebd1ccfce1507a35377b7e4129.jpg)  
a

![](images/694b786f8da3a346a82791338e3f7ef3d40b12620f82b09da47d2657877b4789.jpg)

![](images/acebfe79a7d8147656e310d59607aa8189620c90bfe95bfcb6610384b2dc0b18.jpg)

![](images/bcaf562e52f341d2b64d372ff576ce244ec2164d8bd864638551079b1d49fdfc.jpg)

![](images/cf5b9f3bbd07296ae8315d7cab31eb64d4040d072f6efcb1ad3bc87a35de0a4e.jpg)  
  
f

![](images/3273ce83cb4e7ba3968d1730e9950f70c82054dcf0a7413c3f03cad2aeadee3f.jpg)  
Fig. 3 | Electrical measurements using confined CrTe devices. a, Sketch of the confined electronic device with $\mathsf { C r T e } _ { 3 }$ being the functional PCM layer. b, A single electrical pulse was applied to fully RESET a confined memory cell, after which its resistance was monitored immediately at RT. c, Subsequent cross-  
sectional TEM characterizations of the RESET state, proving that the cell turned fully amorphous (see halos in the fast Fourier transform pattern). d, Electrically switched cycling test of a second confined cell. e,f, Drift measurement at RT of a full RESET state (e) and a full SET state (f) after cycling.

were reduced to $6 . 6 \times 1 0 ^ { 1 9 } \mathrm { c m } ^ { - 3 }$ and $2 . 8 \times 1 0 ^ { - 1 } { \mathsf { c m } } ^ { 2 } { \mathsf { V } } ^ { - 1 } { \mathsf { s } } ^ { - 1 }$ , respectively, in the crystallized film. To assess the reproducibility, we fabricated 34 tungsten-electrode-based test cells, each containing eight electrodes, and measured the sheet resistances of the as-deposited amorphous phase and the fully crystallized phase at $3 5 0 ^ { \circ } \mathrm { C }$ . All 34 test cells gave highly consistent resistance values (Fig. 1f).

For the completely crystallized phase, the cross-sectional transmission electron microscopy (TEM) image in Fig. 1g looks homogeneous with limited intensity contrast, and no grain boundary can be observed at this magnification. The fast Fourier transform pattern confirms the crystal orientation of the ${ \tt c r T e } _ { 3 }$ film to be [001]. The atomic-scale elemental mapping images clearly show an arrangement of slabs of CrTe trilayers sandwiching van der Waals gaps (Fig. 1h). Additional TEM analyses confirmed the highly textured large grains across the four-inch $\mathbf { c } { \cdot } \mathbf { C } \mathbf { r } \mathbf { T } \mathbf { e } _ { 3 }$ film, and the electron-transparent region in the TEM foil (lateral dimension, >5 μm) of the 50-nm c-CrTe film was nearly a single grain (Extended Data Fig. 1). This structural uniformity leads to highly consistent resistance values across the whole silicon wafer (Fig. 1f).

# Suppressed resistance drift at extreme temperatures

The resistance drift behaviour of a-PCMs is usually characterized using $R ( t ) = R _ { 0 } ( t / t _ { 0 } ) ^ { \nu } ( \sigma ( t ) = \sigma _ { 0 } ( t / t _ { 0 } ) ^ { - \nu } )$ , where $R _ { 0 } ( \sigma _ { 0 } )$ is the resistance (conductance) measured at time $t _ { 0 } ,$ and ν is the drift coefficient over time t. To avoid potential aging effects due to sample storage, we measured the resistance of a-CrTe thin films immediately after their sputter preparation. We tested different film thicknesses from 50 nm to 150 nm, which showed an ultralow drift with $\pmb { \nu } { \approx } 0 . 0 0 1$ at RT. With a drift coefficient at this level, resistance drift would have little impact on practical multilevel programming. Figure 2a displays the as-deposited a- $\mathrm { C r T } \mathbf { e } _ { 3 }$ film (50 nm thick) heated to increasingly elevated temperatures, and at

each temperature, the holding time was 1 h. The a-CrTe3 film showed a consistently low ν of 0.001−0.002 between RT and $1 5 0 ^ { \circ } \mathrm { C } . \mathrm { A t } 1 6 5 ^ { \circ } \mathrm { C }$ , its ν slightly increased to ~0.004. These values are far smaller than that of $\mathbf { a } { \cdot } \mathbf { G S T } { \cdot } { \nu } { \approx } 0 { . } 1 1$ between RT and $1 0 0 ^ { \circ } \mathrm { C }$ (Supplementary Fig. 6). Another issue of a-GST is that it crystallizes quickly at higher temperatures (for example, when approaching $1 5 0 ^ { \circ } \mathrm { C } )$ , making it unsuitable for embedded memory applications. Additional drift measurements were performed for a-GeTe, a-CrGeTe3 and $\mathbf { a } { \cdot } \mathbf { S } \mathbf { b } _ { 2 } \mathbf { S } \mathbf { e } _ { 3 }$ thin films (Supplementary Fig. 6), which showed notable resistance drift.

The ultralow drift behaviour of a- ${ \bf \cdot C r T e } _ { 3 }$ was found to be robust over much longer times. We took two other freshly as-deposited films, and recorded their sheet resistance a $\mathbf { t } 2 5 ^ { \circ } \mathbf { C }$ and $1 5 0 ^ { \circ } \mathrm { C }$ over 10 h. Then, the two films were stored for 3 days in air without argon protection at RT. Subsequently, the two films were measured again at $2 5 ^ { \circ } \mathrm { C }$ and $1 5 0 ^ { \circ } \mathrm { C }$ over another 10 h. Both sets of a- $\mathrm { C r T } \mathbf { e } _ { 3 }$ films showed ν ≈ 0.001 (Fig. 2b). We also recorded the resistance of $\mathbf { a } { \cdot } \mathbf { C r } \mathbf { T e } _ { 3 } \mathbf { a t } 0 ^ { \circ } \mathbf { C a n d } { - } 2 5 ^ { \circ } \mathbf { C }$ , using our custom-made setup, and at even lower temperatures using a physical property measurement system with liquid-helium refrigeration. As shown in Fig. 2c, our a-CrTe film again displayed very steady resistance with little drift, $\nu { \approx } 0 . 0 0 1$ , when held at any temperature from $0 ^ { \circ } \mathrm { C }$ down $\mathrm { t } 0 ^ { - 2 0 0 ^ { \circ } C }$ . We also confirmed that such minimal drift can be sustained on extreme temperature cycling (Fig. 2d).

Figure 2e summarizes the drift coefficient ν of a-CrTe (red stars) together with various a-PCMs23–29,37–39 $\mathsf { a } { \mathsf { - P C M S } } ^ { 2 3 - 2 9 , 3 7 - 3 9 }$ , plotted versus the holding temperature. Previous drift measurements of a-PCMs, including the best-so-far $\mathrm { T i T e } _ { 2 } / \mathsf { S b } _ { 2 } \mathrm { T e } _ { 3 }$ heterostructure26, were mostly conducted at RT. The holding temperature was limited $\mathbf { t o - 1 0 0 } ^ { \circ } \mathbf { C }$ , due to their relatively low T . Doping and alloying can increase the thermal stability of the amorphous phase, which, however, can also result in resistance drift in the crystalline phase, with ν reaching ~0.01 or even higher39. By contrast, for our $\mathbf { c } { \cdot } \mathbf { C } \mathbf { r } \mathbf { T } \mathbf { e } _ { 3 }$ (Extended Data Fig. 2), the sheet resistance showed a consistently low $\nu { \approx } 0 . 0 0 1$ at all the holding temperatures

![](images/451ea3308eebded1db2f395d54294a40ca31af23f6954e494c3d8fa530a6c3fd.jpg)  
a   
b

![](images/d3acf41fce44a694a30cd2bde9bc9804cba475151b1529702475c317315082b5.jpg)

![](images/c25bf42a85fa3ebe1e180b583622a625d2b5535a33ce0133fd78e8d4f3de0866.jpg)  
c

![](images/4abd4504aa132a04c4f9c573b21a130228b475649080b7d0dabe982f41940564.jpg)

![](images/f890b53c8cc254571cfeac99bf686517dc0f63060f939003277d2e04c035a5ef.jpg)  
Fig. 4 | CrTe3-based path-tracking vehicle. a, Image of a CrTe3-based path-tracking vehicle. b, Schematic of the control system with $\mathbf { a } 2 \times 2 \mathbf { C r } \mathbf { T e } _ { 3 }$ device array. c, Pathtracking function was preserved after heating. Supplementary Video 2 shows the entire test process.

used for $\mathbf { a } { \cdot } \mathbf { C r T e } _ { 3 }$ . We also note that $\mathrm { G e T e } / { \mathsf { S } } { \mathsf { b } } _ { 2 } \mathrm { T e } _ { 3 }$ and ${ \bf S } { \bf b } _ { 2 } \mathrm { T e } _ { 3 } / { \bf G } \mathrm { e } { \cdot } { \bf S } { \bf b }$ -Te superlattices may display a relatively low drift of $\nu { \approx } 0 . 0 0 2 { \mathrm { - } } 0 . 0 0 9$ (refs. 40–42). Nevertheless, their RESET states may be in a partly crystalline state. As shown in Fig. 2e, our $\mathsf { C r T e } _ { 3 }$ is the only PCM that is immune to resistance drift at all practical operating temperatures for IMC applications.

# Electrical measurement of $\bf \dot { C } F T e _ { 3 }$ devices

To ascertain that the melt-quenched a-CrTe displays the same no-drift behaviour, we carried out electrical measurements on a series of confined memory devices, inside which a $\mathrm { C r T e } _ { 3 }$ film of ~100 nm is confined by the electrodes (tungsten) and the dielectric layers $( \mathrm { { S i O } } _ { 2 } ;$ Fig. 3a). Further details about the device structure can be found in Supplementary Fig. 7. First, the $\mathsf { C r T e } _ { 3 }$ cell was thermally annealed at $3 5 0 ^ { \circ } \mathrm { C }$ to form a full crystalline state, and was programmed to a full amorphous state using a single electrical RESET pulse (Fig. 3b). The drift coefficient $( \nu { \approx } 0 . 0 0 1 )$ determined from the data acquired immediately after the electrical melt-quench process (Supplementary Video 1) is consistent with the behaviour of the as-deposited amorphous phase. The subsequent cross-sectional TEM characterizations confirmed that the electrical switching rendered the cell fully amorphous (Fig. 3c). We also performed cycling measurements and found the same no-drift behaviour of the RESET state of a ${ \bf - C r T e } _ { 3 }$ after ${ \bf \cdot } 2 \times 1 0 ^ { 5 }$ cycles (Fig. 3d,e). The same electrical measurements were repeated for several additional cells, and the drift coefficient values of the initial RESET and final RESET states are consistently close to 0.001 (Extended Data Fig. 3). Meanwhile, the SET state (that is, $\mathbf { c } { \cdot } \mathbf { C r } \mathbf { T e } _ { 3 } )$ showed constant electrical resistance over time, too (Fig. 3f). Further results are documented in Supplementary Fig. 8. Note that the programming noise of the $\mathsf { C r T e } _ { 3 }$ device can also be suppressed by increasing the pulsing width to reduce the crystallization randomness (Supplementary Fig. 9). Besides, we confirmed that consistently high resistance drift would persist for GST devices after extended cycling (Supplementary Fig. 10).

The essence of multilevel programming in PCM devices is to generate a series of intermediate resistance states, each corresponding to a different ratio of amorphous-to-crystalline volume. However, fine-tuning the volume fraction of crystalline versus amorphous

regions using electrical pulses requires sophisticated device fabrication and control, and is subject to much uncertainty. We, therefore, developed a hybrid opto-electro-thermal scheme, which serves the purpose of assessing the multilevel capacity of $\mathsf { C r T e } _ { 3 }$ in a deterministic way. The precise volume control is achieved via step-wise SET, that is, generating crystalline domains of the same size, one by one in a regular pattern, via laser irradiation on an amorphous film. The actual image of the setup is displayed in Supplementary Fig. 11. Using a bridge-like device covered with an as-deposited a-CrTe film, we applied laser pulses in the middle part of the devices for sequential crystallization along the lateral direction (Supplementary $\mathsf { F i g . }$ 12 shows the optical images). After sending every two laser pulses, the electrical resistance was measured and monitored for over 1 h. During the whole process $( > 1 6 \mathrm { h } )$ , each of the three devices were held at $2 5 ^ { \circ } \mathrm { C } , 8 0 ^ { \circ } \mathrm { C }$ or ${ \bf 1 5 0 } ^ { \circ } { \bf C } .$ Each device displayed 16 well-separated resistance levels (Extended Data Fig. 4). The resistance levels can be well distinguished even at a holding temperature of $1 6 5 ^ { \circ } \mathrm { C }$ (Supplementary Fig. 13). Although the crystallization rate is not a top-priority parameter to optimize owing to the parallel programming ability of the $\mathsf { P C M a r r a y } ^ { 4 3 }$ , it is still desirable to have relatively fast crystallization to shorten the training time of the neural network (Supplementary Note 2 and Supplementary Fig. 14).

# Path-tracking function enabled by stable resistance levels

To highlight the importance of robust resistance levels without drift, we fabricated $1 2 \times 2$ array of $\mathsf { C r T e } _ { 3 }$ -based bridge-like devices, and integrated the array into a self-made vehicle (Fig. 4a) to realize a stable path-tracking function. As shown in Fig. 4b, the control system of this vehicle mainly composed of two greyscale sensors, a device array, amplifiers and a servomotor. The sensors are symmetrically installed in the front of the vehicle to detect greyscale changes, which provide distinct input voltage signals when detecting black and white. We programmed the four well-separated resistance values into the four devices via step-wise SET laser operations on the as-deposited a-CrTe thin films. The weight (conductance) values of the four devices were then mapped into a single-layer neural network (the $2 \times 2 \mathsf { a r r a y } )$ ) as

the basic neuromorphic computing unit, performing matrix vector multiplication through Ohm’s law and Kirchhoff’s law to enable automatic path tracking44. The output current signals from the array were then processed through the transimpedance amplifier and differential amplifier, and were converted into voltage signals again for the final steering and turning actions of the servomotor. The threshold for failure is set as tight as ‘any weight value changing by more than ±1%’. As shown in Fig. 4c and Supplementary Video 2, the vehicle appropriately tracked the black path, consistently turning the wheels back to the black path when detecting the white background. This $\mathrm { C r T } \mathbf { e } _ { 3 }$ -based path-tracking vehicle still functioned very well after being placed in air for over 1 month, and after heating the control board at 150 °C for over 1 h. In a control experiment, a GST device array was integrated into the same vehicle. The automatic path-tracking function was achieved initially, but was completely lost after only 10 min (Supplementary Fig. 15 and Supplementary Video 3) due to the resistance drift of a-GST.

# Outlook

We have designed an unconventional PCM without resistance drift at almost all practical IMC operating temperatures $( T { = } { - } 2 0 0 ^ { \circ } \mathbf { C } \mathbf { t o } 1 6 5 ^ { \circ } \mathbf { C } )$ from the start (immediately after the amorphous state was generated) to many hours of aging at each T. Resorting to a glass with molecule-like motifs opens a new avenue towards ultralow resistance drift (Supplementary Note 3). In contrast with conventional a-PCMs (or other glass categories) that tend to readily relax towards other adjacent sub-basins (variable motif configurations) across a fairly shallow megabasin in the potential energy landscape, the molecular-glass-like a-PCM we designed would stay put in a rather steep basin (Extended Data Fig. 5), with little motivation for relaxation and no other desirable motifs that can be accessed (at least up $\mathbf { t o } { \cdot } 2 0 0 ^ { \circ } \mathbf { C } )$ . The transformation between amorphous and crystalline $\mathrm { C r T e } _ { 3 }$ via the cooperation of compact and robust octahedra also resulted in a desirable combination of excellent amorphous stability and satisfactorily fast crystallization speed. Future work is anticipated to gain a deeper understanding of this alloy at temperatures approaching crystallization via in situ measurements45,46 and machine-learning-facilitated molecular dynamics47. Also, it is necessary to test the multilevel capacity in nanoscale PCM devices48, the endurance beyond million cycles, as well as the device variability of $\mathsf { C r T e } _ { 3 }$ in a large crossbar array, before the new PCM can be put into practical use. Nevertheless, we have demonstrated that $\mathsf { C r T e } _ { 3 }$ thin films can be produced with wafer-scale homogeneity via a standard sputtering approach, adding no complexity to mass production nor to the programming algorithm. Overall, our no-drift discovery achieves the first intrinsically robust a-PCM, offering a front-end materials solution that has the potential to meet the demanding requirements of high-precision multilevel programming at the operation temperatures for both data-centric and edge-computing platforms.

# Online content

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41563-025-02361-0.

# References

1. Lanza, M. et al. Memristive technologies for data storage, computation, encryption, and radio-frequency communication. Science 376, eabj9979 (2022).   
2. Ielmini, D. & Wong, H.-S. P. In-memory computing with resistive switching devices. Nat. Electron. 1, 333–343 (2018).   
3. Zhang, W. et al. Edge learning using a fully integrated neuro-inspired memristor chip. Science 381, 1205–1211 (2023).   
4. Ambrogio, S. et al. An analog-AI chip for energy-eficient speech recognition and transcription. Nature 620, 768–775 (2023).

5. Rao, M. et al. Thousands of conductance levels in memristors integrated on CMOS. Nature 615, 823–829 (2023).   
6. Wang, Z. et al. Resistive switching materials for information processing. Nat. Rev. Mater. 5, 173–195 (2020).   
7. Wang, M. et al. Robust memristors based on layered two-dimensional materials. Nat. Electron. 1, 130–136 (2018).   
8. Boybat, I. et al. Temperature sensitivity of analog in-memory computing using phase-change memory. In Proc. IEEE International Electron Devices Meeting 28.3.1–28.3.4 (IEEE, 2021).   
9. Jiang, H. et al. Sub-10 nm Ta channel responsible for superior performance of a HfO memristor. Sci. Rep. 6, 28525 (2016).   
10. Wuttig, M. & Yamada, N. Phase-change materials for rewriteable data storage. Nat. Mater. 6, 824–832 (2007).   
11. Zhang, W., Mazzarello, R., Wuttig, M. & Ma, E. Designing crystallization in phase-change materials for universal memory and neuro-inspired computing. Nat. Rev. Mater. 4, 150–168 (2019).   
12. Cheng, H. Y., Carta, F., Chien, W. C., Lung, H. L. & BrightSky, M. 3D cross-point phase-change memory for storage-class memory. J. Phys. D: Appl. Phys. 52, 473002 (2019).   
13. Song, Z. T. et al. High endurance phase change memory chip implemented based on carbon-doped Ge2Sb2Te5 in 40 nm node for embedded application. In Proc. IEEE International Electron Devices Meeting 27.5.1–27.5.4 (IEEE, 2018).   
14. Grossier, N. et al. ASIL-D automotive-grade microcontroller in 28 nm FD-SOI with full-OTA capable 21 MB embedded PCM memory and highly scalable power management. In Proc. IEEE Symposium on VLSI Technology 1–2 (IEEE, 2023).   
15. Kim, H. J. et al. Versatile spaceborne photonics with chalcogenide phase-change materials. npj Microgravity 10, 20 (2024).   
16. Pirovano, A. et al. Low-field amorphous state resistance and threshold voltage drift in chalcogenide materials. IEEE Trans. Electron Dev. 51, 714–719 (2004).   
17. Boniardi, M. et al. A physics-based model of electrical conduction decrease with time in amorphous ${ \mathsf { G e } } _ { 2 } { \mathsf { S b } } _ { 2 } { \mathsf { T e } } _ { 5 } .$ J. Appl. Phys. 105, 084506 (2009).   
18. Zhang, W. & Ma, E. Unveiling the structural origin to control resistance drift in phase-change memory materials. Mater. Today 41, 156–176 (2020).   
19. Le Gallo, M. et al. Mixed-precision in-memory computing. Nat. Electron. 1, 246–253 (2018).   
20. Le Gallo, M. et al. Precision of bit slicing with in-memory computing based on analog phase-change memory crossbars. Neuromorph. Comput. Eng. 2, 014009 (2022).   
21. Ghazi Sarwat, S. et al. Projected mushroom type phase-change memory. Adv. Funct. Mater. 31, 2106547 (2021).   
22. Ambrogio, S. et al. Equivalent-accuracy accelerated neural network training using analogue memory. Nature 558, 60–67 (2018).   
23. Li, C. et al. Understanding phase-change materials with unexpectedly low resistance drift for phase-change memories. J. Mater. Chem. C6, 3387–3394 (2018).   
24. Khan, R. S., Dirisaglik, F., Gokirmak, A. & Silva, H. Resistance drift in $\mathsf { G e } _ { 2 } \mathsf { S b } _ { 2 } \mathsf { T e } _ { 5 }$ phase change memory line cells at low temperatures and its response to photoexcitation. Appl. Phys. Lett. 116, 253501 (2020).   
25. Wang, Q. et al. Reliable $\mathsf { G e } _ { 2 } \mathsf { S b } _ { 2 } \mathsf { T e } _ { 5 }$ based phase-change electronic synapses using carbon doping and programmed pulses. J. Materiomics 8, 382–391 (2022).   
26. Ding, K. et al. Phase-change heterostructure enables ultralow noise and drift for memory operation. Science 366, 210–215 (2019).   
27. Liu, B. et al. Multi-level phase-change memory with ultralow power consumption and resistance drift. Sci. Bull. 66, 2217–2224 (2021).   
28. Hatayama, S., Song, Y.-H. & Sutou, Y. Low resistance-drift characteristics in $\mathsf { C r } _ { 2 } \mathsf { G e } _ { 2 } \mathsf { T e } _ { 6 } .$ -based phase change memory devices with a high-resistance crystalline phase. Mater. Sci. Semicond. Process. 133, 105961 (2021).

29. Chen, B. et al. Suppressing structural relaxation in nanoscale antimony to enable ultralow-drift phase-change memory applications. Adv. Sci. 10, 2301043 (2023).   
30. Raty, J.-Y. et al. Aging mechanisms of amorphous phase-change materials. Nat. Commun. 6, 7467 (2015).   
31. Gabardi, S., Caravati, S., Sosso, G. C., Behler, J. & Bernasconi, M. Microscopic origin of resistance drift in the amorphous state of the phase-change compound GeTe. Phys. Rev. B 92, 054201 (2015).   
32. Konstantinou, K., Mocanu, F. C., Lee, T. H. & Elliott, S. R. Revealing the intrinsic nature of the mid-gap defects in amorphous Ge Sb Te . Nat. Commun. 10, 3065 (2019).   
33. McGuire, M. A. et al. Antiferromagnetism in the van der Waals layered spin-lozenge semiconductor CrTe3. Phys. Rev. B 95, 144421 (2017).   
34. Hatayama, S. et al. Inverse resistance change Cr Ge Te -based PCRAM enabling ultralow-energy amorphization. ACS Appl. Mater. Interfaces 10, 2725–2734 (2018).   
35. Wang, X., et al. Spin glass behavior in amorphous Cr2Ge2Te6 phase-change alloy. Adv. Sci. 10, 2302444 (2023).   
36. Njoroge, W. K., Woeltgens, H.-W. & Wuttig, M. Density changes upon crystallization of Ge2Sb2.04Te4.74 films. J. Vac. Sci. Technol. A 20, 230–233 (2002).   
37. Salinga, M. et al. Monatomic phase change memory. Nat. Mater. 17, 681–685 (2018).   
38. Wimmer, M., Kaes, M., Dellen, C. & Salinga, M. Role of activation energy in resistance drift of amorphous phase change materials. Front. Phys. 2, 75 (2014).   
39. Navarro, G. et al. Trade-of between SET and data retention performance thanks to innovative materials for phase-change memory. In Proc. IEEE International Electron Devices Meeting 21.5.1–21.5.4 (IEEE, 2013).   
40. Zhou, L. et al. Resistance drift suppression utilizing GeTe/Sb2Te3 superlattice-like phase-change materials. Adv. Electron. Mater. 5, 1900781 (2019).   
41. Khan, A. I. et al. Ultralow–switching current density multilevel phase-change memory on a flexible substrate. Science 373, 1243–1247 (2021).   
42. Wu, X. et al. Novel nanocomposite-superlattices for low energy and high stability nanoscale phase-change memory. Nat. Commun. 15, 13 (2024).

43. Burr, G. W. et al. Large-scale neural networks implemented with non-volatile memory as the synaptic weight element: comparative performance analysis (accuracy, speed, and power). In Proc. IEEE International Electron Devices Meeting 4.4.1–4.4.4 (IEEE, 2015).   
44. Wang, C. et al. A Braitenberg vehicle based on memristive neuromorphic circuits. Adv. Intell. Syst. 2, 1900103 (2019).   
45. Zalden, P. et al. Femtosecond X-ray difraction reveals a liquid-liquid phase transition in phase-change materials. Science 364, 1062–1067 (2019).   
46. Jiang, T.-T. et al. In situ characterization of vacancy ordering in Ge-Sb-Te phase-change memory alloys. Fundam. Res. 4, 1235–1242 (2024).   
47. Zhou, Y., Zhang, W., Ma, E. & Deringer, V. L. Device-scale atomistic modelling of phase-change memory materials. Nat. Electron. 6, 746–754 (2023).   
48. Kim, W. et al. Confined PCM-based analog synaptic devices ofering low resistance-drift and 1000 programmable states for deep learning. In Proc. IEEE Symposium on VLSI Technology T66–T67 (IEEE, 2019).

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons. org/licenses/by/4.0/.

© The Author(s) 2025, modified publication 2025

# Methods

# Synthesis and structural characterizations

CrTe3 thin films of ~50−150 nm were deposited on four-inch $\mathsf { S i O } _ { 2 } / \mathsf { S i }$ substrates at RT with a pure Cr target and a pure Te target in a high vacuum via AJA ORION 8 (base pressure, less than $\mathbf { - 1 } \times \mathbf { 1 0 } ^ { - 5 } \mathbf { P a } )$ . An ~10-nm-thick ZnS–SiO2 capping layer was grown on top of the CrTe3 film inside the vacuum chamber to prevent oxidation and evaporation. The deposition rate was set to 9.5 nm min−1. The chemical composition of the sputtered films was determined to be approximately $\mathrm { C r } _ { 2 5 . 4 } \mathrm { T e } _ { 7 4 . 6 }$ by the energy-dispersive X-ray experiments. The structures of the as-deposited and post-annealed thin films were investigated by XRD with Cu Kα radiation (Bruker D8 ADVANCE). The TEM specimens were prepared by a dual-beam focused-ion-beam system (Helios NanoLab 600i, FEI) with a Ga ion beam operated at 30 kV. A Pt protective layer was deposited above the $\mathsf { C r T e } _ { 3 }$ thin film to mitigate potential damage from Ga ions during the focused-ion-beam lift-out and thinning processes. The TEM experiments were performed on a Talos-F200X device operated at 200 kV. The scanning transmission electron microscopy–high-angle annular dark field imaging and energy-dispersive X-ray mapping experiments were performed on a JEOL ARM200F STEM device with a probe aberration corrector, operated at 200 kV. Raman spectra were collected using Renishaw inVia Qontor with a solid-state 532-nm laser for excitation, where the laser power was set as 0.25 mW, and an exposure time of 2 s with 50 cycles was used.

# Fabrication of devices and the vehicle

The confined memory devices were fabricated using electron-beam lithography and reactive ion etching. The top and bottom electrodes were made of tungsten, and SiO2 was used for the dielectric layers. The thickness of the CrTe layer was ~100 nm. Two lithography processes were adopted for the fabrication of the bridge-like devices. The first lithography process was applied to pattern the layer of a metal electrode on a $\mathrm { S i O } _ { 2 }$ wafer using an ultraviolet lithography machine (SUSS MJB4). The tungsten electrodes of 30-nm thickness were deposited on the patterned substrate via magnetron sputtering followed by a lift-out process. The second lithography process was applied to pattern the PCM layer. The deposited CrTe layer (~50 nm) was slightly thicker than that of the tungsten electrodes to ensure the connectivity of the device. $\mathsf { A Z n S  – S i O _ { 2 } }$ protective layer with a thickness of 20 nm was deposited on top of the surface. Both lithography processes were done using a negative photoresist (AZ5214E). The 2 × 2 CrTe3 device array was fabricated and integrated on a custom printed circuit board using a wire bonder (TPT HB10). The vehicle consisted of two greyscale sensors, a CrTe3 array, amplifiers and a motor system (including a servomotor and an engine), batteries and the vehicle body. The servomotor performed different steering actions directed by the CrTe -based control system.

# Electrical measurements

The custom-made electrical testing system was constructed by connecting a Keithley 2636B source meter and an Instec mK200 hot stage with a temperature accuracy of $0 . 0 0 1 ^ { \circ } \mathrm { C }$ . The sheet resistance of the CrTe films as a function of temperature was measured at a heating rate of 10 °C min−1 under argon protection. The probe electrodes were made of tungsten. For the electrical measurements of 34 units on the wafer, we first broke down these units from the wafer, and then repeated the sheet resistance measurement on each of them. The physical property measurement system instrument (Quantum Design DynaCool) was used for the Hall effect measurement at RT and the low-temperature resistance measurements between $- 5 0 ^ { \circ } \mathbf { C } \mathbf { t } \mathbf { 0 } - 2 0 0 ^ { \circ } \mathbf { C }$ . The electrical measurements of the confined memory devices were performed using the Keithley 2400C source meter (measuring cell resistance) and the Tektronix AWG5002B pulse generator (generating voltage pulse). Long voltage pules were used in the cycling experiments to guarantee the devices to form full RESET (2.5 V, 300 ns followed by a

40-ns falling edge) and SET (1.5 V, 500 ns followed by an 80-ns falling edge) states for the subsequent resistance drift measurements. The self-built opto-electro-thermal platform was equipped with Stradus 488–25 lasers, arbitrary function generator (AFG 31000 SERIES), optical path system, Keithley 2636B source meter, Instec mK200 hot stage and a computer. The wavelength, pulse duration and power of the applied laser were set as 488 nm, 100 ns and 90 mW, respectively, for the step-wise crystallization of bridge-like devices. The source meter records the resistance values continuously so that any change in resistance can be monitored in real time on multilevel programming. Slight numerical difference in the electrical resistance value of the amorphous (or crystalline) state is expected for different device setups, in which the film thickness, length, type of electrodes, amorphous-to-crystal ratio and orientation of the crystal can lead to some resistance variations.

# Ab initio calculations

We carried out DFT-based AIMD simulations using the second-generation Car–Parrinello molecular dynamics scheme49 implemented using the CP2K package50. The Kohn–Sham orbitals were expanded by a double- and triple-zeta plus polarization Gaussian-type basis set for Cr and Te, and the charge density was expanded in plane waves with a cut-off of 300 Ry. The Goedecker–Teter–Hutter pseudopotentials51 and Perdew–Burke–Ernzerhof functional52 with van der Waals correction based on the Grimme’s D3 method53 were applied, and spin polarization was considered using α and β orbitals without spin restriction. The AIMD calculations were carried out using the canonical (NVT) ensemble with a time step of 2 fs. To generate a-CrTe3, 50 Cr atoms and 150 Te atoms were randomly arranged in a cubic cell. The model was heated above 3,000 K to remove all possible crystalline orders, and were then quenched down to ~1,200 K in 10 ps. After an AIMD run at ~1,200 K for 30 ps, the model was then quenched down to 0 K at a cooling rate of $1 2 . 5 \mathsf { K p s } ^ { - 1 }$ . To collect structural data at different holding temperatures, the corresponding snapshots within the cooling process were picked out for a separate 50-ps AIMD run at the respective holding temperature. Three amorphous models with independent thermal history were calculated in both crystalline and amorphous densities, respectively. The structural relaxation and further spin-polarized DOS analyses at 0 K were conducted using the Vienna ab initio simulation package code54 with the Perdew–Burke–Ernzerhof functional, van der Waals D3 correction and the projector-augmented wave pseudopotentials55. The energy cut-off was set as 450 eV. Each amorphous model contained 50 Cr atoms and 150 Te atoms, and its Brillouin zone was sampled using the Γ point. For c-CrTe , the unit cell contained 8 Cr atoms and 24 Te atoms, and its Brillouin zone was sampled using a $2 \times 2 \times 4 k$ -point mesh.

# Data availability

All data needed to evaluate the conclusions in this paper are included in the Article or the Supplementary Information.

# Code availability

The Vienna ab initio simulation package and CP2K software packages are commercially available at https://www.vasp.at and https://www. cp2k.org (open source), respectively.

# References

49. Kühne, T., Krack, M., Mohamed, F. & Parrinello, M. Eficient and accurate car-parrinello-like approach to Born-Oppenheimer molecular dynamics. Phys. Rev. Lett. 98, 066401 (2007).   
50. Kühne, T. D. et al. CP2K: an electronic structure and molecular dynamics software package—quickstep: eficient and accurate electronic structure calculations. J. Chem. Phys. 152, 194103 (2020).   
51. Goedecker, S., Teter, M. & Hutter, J. Separable dual-space Gaussian pseudopotentials. Phys. Rev. B 54, 1703 (1996).

52. Perdew, J. P., Burke, K. & Ernzerhof, M. Generalized gradient approximation made simple. Phys. Rev. Lett. 77, 3865–3868 (1996).   
53. Grimme, S., Antony, J., Ehrlich, S. & Krieg, H. A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-P. J. Chem. Phys. 132, 154104 (2010).   
54. Kresse, G. & Furthmüller, J. Eficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. Phys. Rev. B 54, 11169 (1996).   
55. Blöchl, P. E. Projector augmented-wave method. Phys. Rev. B 50, 17953–17979 (1994).

# Acknowledgements

W. Zhang and J.-J.W. acknowledge support from the National Key Research and Development Program of China (2023YFB4404500). W. Zhang acknowledges support from the National Natural Science Foundation of China (62374131). J.-J.W. acknowledges support from the National Natural Science Foundation of China (62204201). We acknowledge X. Li for useful discussions, C. Li and C. Ma for their help with the TEM characterizations, S. Yang for technical support on bridge-like device fabrication, W. Liu for assistance with the integration of the path-tracking vehicle; the high-performance computing platform of XJTU and the Computing Center in Xi’an for providing computational resources; XJTU for hosting their work at CAID; and the International Joint Laboratory for Micro/Nano Manufacturing and Measurement Technologies of XJTU.

# Author contributions

W. Zhang, X.W. and E.M. conceived the idea and designed the experiments and simulations. X.W., J.-J.W. and R.W. carried out most

of the experiments with the help of D.X., C.N., Z.Z., C.W., J.Z., W. Zhou and Z.S. S.S. performed the DFT calculations with the help of R.C. and X.S. D.X. and J.-J.W. performed the image recognition simulations and vehicle testing. W. Zhang, X.W. and E.M. wrote the paper with input from J.-J.W. and S.S. All authors discussed the results and approved the submission of the paper.

# Competing interests

Several patents (PCT/CN2024/123713, CN 202411271055.6, CN 202411271061.1) on no-drift PCM are under examination. W. Zhang, X.W., J.-J.W. and W. Zhou are listed on the patent applications, and they are all from China. The other authors declare no competing interests.

# Additional information

Extended data is available for this paper at https://doi.org/10.1038/s41563-025-02361-0.

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41563-025-02361-0.

Correspondence and requests for materials should be addressed to Jiang-Jing Wang, En Ma or Wei Zhang.

Peer review information Nature Materials thanks Alan Greer and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permissions information is available at www.nature.com/reprints.

![](images/d522a1ecb7d70783050c581aafeb1f8ee3897883a0ec8ce1b9cd3acd827393b8.jpg)

![](images/712279a05dfe548cdf78a4c5a8e97924873418aa7aaeadfb78e0dfa9dcb3b991.jpg)

![](images/d989e61fc646b52e013f22b7fde46935839f7946b977382d4300c1dc33dcc676.jpg)

![](images/b71a17323fb0bc522bec6910a300d6ae87d5ed79ef75f218c0de3382762deec3.jpg)

![](images/b646c1b91fca21fac215f5f13ae2b79ff09452fbcaf69a54530279cf3005b7f9.jpg)

![](images/4a9226e63313b63b3321e179b1c970eca622dadac721ae67b8c189cb67a3062b.jpg)

![](images/a751e53cb1b032dcbfa83caff451e2f79bb0831037281096443a8b2f791a7f78.jpg)

![](images/a20f1798808ed3ac1ba45a11abc9b65981197266889e70606e0f7b0482053c6e.jpg)

![](images/7d210c4de49672ec3f020e7147725119b5c8bc25059a8f070f947419d160f5ee.jpg)

![](images/4b1bcdbb6874d1338af7ebd1932057f0972385f60577f99ff5e8a1babd3901c6.jpg)

![](images/d81615ace66a127820eedf241d00d6b5804fae843aa2f15256854ee6d6bf2eca.jpg)

![](images/61bb62dd12e086498ba75577c0b9d412f39456acd58c088aca1f0b65c412202d.jpg)  
Extended Data Fig. 1 | Structural characterizations of CrTe thin films. The samples were heated to 350 °C to obtain a completely crystallized state. (a) The XRR spectrum of as-deposited amorphous films and crystallized CrTe3 films of ~150 nm. (b) The TEM images near top Pt protective layer and the Si substrate of crystallized CrTe film of ~150 nm. The zoom-in TEM images taken at locations from the top to the bottom of the film consistently show well-aligned (001) lattice planes parallel to the substrate surface, consistent with the XRD results, indicating epitaxial-growth-like crystal quality even though no seeding layer was used in the deposition. (c) The atomic-scale HAADF image of crystalline   
CrTe viewed in the [001] direction and its corresponding EDX mapping of Cr and Te. The intensity of spots in the HAADF image is approximately proportional to the square of the averaged atomic number Z of each column along the view direction, therefore, the Te (Z = 54) columns look brighter than the Cr (Z = 24) columns. (d) The measured XRD patterns over 34 locations on the 4-inch wafer. (e) The TEM images recorded at different locations of crystallized CrTe film of ~50 nm. No clear grain boundary can be observed over >5 μm lateral direction. The film thickness along the beam incidence direction was ~80 nm for all TEM specimens we prepared.

![](images/10edfa610d5a100bf9d101e4cda354e2f58d7d6f0da817616ab456d476ecab34.jpg)  
a

![](images/38fe9cb89c486375fdfe85d38969f2da2544eb16ec09889cf4820543afa48ca3.jpg)

Extended Data Fig. 2 | Electrical measurements of the crystallized thin films. The resistance drift measurements of the crystallized CrTe thin films, each conducted at a different holding temperature (a) at or above RT, and (b) at 0 °C or below.

![](images/3bb7b1b2b53a7780df7d110950fed42881cd3791652a9308bc0f8f5886556979.jpg)

![](images/2cf54545cd54459069b2e3af40c1827f1c8874227932db5271a13a7122e24adb.jpg)

![](images/2175232d1fcec090755b017fde2097a3aa0c712b8e29b87c35055bf28c82a691.jpg)

![](images/a2a0c69562aaebf220f513a3d76ffaf58755eaac3b966a9a60f0a303df9d2d7d.jpg)

![](images/10dab5b30751fb7774efef094745bf0e703f893083c589c42134b1486451d2ef.jpg)

![](images/245363e346c7f065c5fa5511f44ce1876bb77d6045fd81d998297c0e0033e09c.jpg)  
Extended Data Fig. 3 | Additional drift measurements. The drift measurements after the initial electrical melt-quench RESET operation in electronic device, the cycling endurance test itself, and the drift measurements of the full RESET state   
after cycling at RT. Electrical measurements of four additional confined memory cells confirmed the no-drift behavior of the RESET state. See Supplementary Fig. 9 for the effect of pulse width in suppressing programming noise.

![](images/aebc395d0a982286a17f1c50ec26a4b373f793ef0a2f5856a60ce2bb7e8310d3.jpg)

![](images/000f5170e722b1dce7e6e0411c1fb79b748f4430b67591baa80e795f9ebc5d75.jpg)

![](images/e6257afeecc658174c93206043de38b3526e353c2e1b697c38183ed1e9562439.jpg)

![](images/267de5daee77048e72c119be1d16493a948472f94b31e94e60cfc848c5b1742b.jpg)

![](images/ad0b83629b9eb8872dff520146eb416c2909103c9afc3dfc72a894fb276bda88.jpg)  
Extended Data Fig. 4 | Deterministic multilevel programming. (a) The scheme of optical programming and electrical measurement on a bridge-like CrTe3 device. (b) The hybrid opto-electro-thermal setup consisted of a nanosecond laser beam with 1 μm spot size (controlled using an arbitrary functional generator, AFG), a source measure unit (SMU) for electrical measurements, and   
a temperature controller stage (TCS). The bottom-right inset shows the photo of the self-made CrTe3 device. (c) Using a bridge-like device of 10×20 μm2 , 16 robust resistance states were obtained at 25, 80 and 150 °C via step-wise SET operations. Each resistance level was measured after sending two laser pulses.

![](images/5ce2757be769327646e22f2be6f586c9af342e0cfcb6d97f8366de87952b9b03.jpg)  
Reaction coordinate

![](images/a2dee04445f94d371387d07ccb9d0d2e342a448515cb5aa41effb73202ebd3b8.jpg)  
Reaction coordinate   
Extended Data Fig. 5 | Schematic of the potential energy landscape. A substantial difference is expected for conventional PCMs (left panel, where upon ageing the glass can relax towards a number of possible lower-energy basins) and our new molecule-like PCMs (right panel, in which the glass sits at the   
bottom of a rather deep basin, while comparable/competing metastable basins are either non-existent, or all out of the picture because they are inaccessible due to high barriers for the glass aged in this study at temperatures below ~200 °C). See text for additional explanation.