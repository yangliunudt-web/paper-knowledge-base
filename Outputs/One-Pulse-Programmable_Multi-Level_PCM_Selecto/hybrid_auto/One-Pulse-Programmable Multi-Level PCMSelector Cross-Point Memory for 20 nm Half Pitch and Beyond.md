---
title: "One-Pulse-Programmable Multi-Level PCM/Selector Cross-Point Memory for 20 nm Half\\\"
authors:
  - "Yuya Matsuzawa"
  - "Yuki Ohnishi"
  - "Kazuhiro Katono"
  - "Yusuke Muto"
  - "Takayuki Tsukagoshi"
  - "Hiroki Tokuhira"
  - "Kei Sakamoto"
  - "Hisakazu Matsumori"
  - "Hiroyuki Ode"
  - "Shosuke Fujii"
  - "Hide Tanaka"
  - "Takeshi Fujimaki"
date: "2024-01-01"
year: "2024"
journal: "Nature Electronics"
abstract: "We demonstrated, for the first time, a multi-level phase change memory/selector cell\\\"
abstract_cn: "我们首次展示了无需初始化或迭代验证即可操作的多级相变存储器/选择器单元，显示了未来高密度和低延迟均至关重要的成本效益存储级内存应用的潜力。我们发现优化的热设计和成分设计能够形成独特的中间电阻态，其中晶态和非晶态共存并置于设计位置。多级编程通过单一脉冲实现，无需任何额外操作，并且在超过10^7次循环中保持稳定，具有足够的存储窗口。此外，我们制造并演示了半间距为20\\\"
keywords:
  - "[[[[Cross-point array]]]]"
  - "[[[[In-memory computing]]]]"
  - "[[[[Non-volatile memory]]]]"
  - "[[[[Phase change memory]]]]"
  - "[[selector]]"
wiki_concepts:
  - "[[selector]]"
---

# One-Pulse-Programmable Multi-Level PCM/Selector Cross-Point Memory for 20 nm Half Pitch and Beyond

Yuya Matsuzawa, Yuki Ohnishi, Kazuhiro Katono, Yusuke Muto, Takayuki Tsukagoshi, Hiroki Tokuhira, Kei Sakamoto, Hisakazu Matsumori, Hiroyuki Ode, Shosuke Fujii, Hide Tanaka, and Takeshi Fujimaki

Institute of Memory Technology R&D, Kioxia Corporation, Yokkaichi, Japan, e-mail: yuya1.matsuzawa@kioxia.com

Abstract—We demonstrated, for the first time, a multi-level phase change memory/selector cell which can be operated without initialization or iterative verify, showing the potential for future cost-effective storage-class memory applications where both high density and low latency are essential. We found optimal thermal and composition design enabled to form distinct middle resistance state, in which crystalline and amorphous co-exist and were placed at designed positions. Multi-level programming was achieved by one single pulse without any additional operation, and it was stable over >107 cycles with sufficient memory window. Furthermore, we fabricated and demonstrated PCM/selector cross-point memory array with half-pitch of 20 nm. Thermal simulation showed the one-pulse multi-level operation is feasible in cross-point array with 20 nm half-pitch and beyond.

Keywords—PCM, phase change memory, selector, 1S1R, crosspoint

# I. INTRODUCTION

Cross-point memory array architecture is suitable for achieving both high density and low latency memory array for storage-class memory applications. Several memory cell candidates have been reported so far [1-4], and a high density memory cell with 22.5 nm half-pitch was successfully demonstrated [3]. Phase change material (PCM)/selector stacked cell is considered as a promising cell technology [4]. Further increase in bit density has been demonstrated by stacking memory deck [5]. However, low thermal stability nature of the PCM and selector requires complicated process integration technique, making further memory stacking more challenging and expensive. To reduce the process integration difficulties, exploration of new material engineering has been conducted in recent years [6-8].

Multi-level cell (MLC) is another way to increase bit density without increasing bit cost. However, current MLC technique requires iterative programming and control transistors to ensure tight distribution of the memory states, which is not suitable for storage-class memory application where low latency operation is essential. Recent study demonstrated the possibility of noverify MLC operation scheme with the PCM/selector cell [9], although initialization operation before re-programming was still needed. Therefore, novel memory cell engineering and/or operation scheme is demanded for future cost-effective storageclass memory application.

Fig.2(right): (a) IV curves for LRS and HRS. (b) Thermal simulation shows that heat is generated in selector and propagated to PCM.

In this work, we demonstrate, for the first time, that a stable and distinct middle resistance state (MRS) can be formed in a PCM/selector cell with sophisticated thermal design and PCM composition optimization. The stable MRS realizes multi-level programming by one single pulse without any additional operation, showing a feasible path to higher density cross-point memory array with keeping low latency.

# II. CELL THREMAL DESIGN

Fig.1 shows a TEM image of isolated pillar-type PCM /selector cell with a relaxed cell diameter. The cell stack consists of bottom electrode (BE), selector layer, middle electrode (ME), PCM layer, top electrode (TE), and insulator on sidewall of the pillar (liner). Fig.2(a) shows typical I-V curves for low resistance state (LRS) and high resistance state (HRS). The threshold voltage (Vth) at which an abrupt increase in the cell current occurs was changed in accordance with PCM memory state. Thermal simulation for the PCM/selector cell during voltage application was conducted as shown in Fig.2(b), where simulation parameters such as thermal and electrical conductivity for each component are determined by experimental data. It is revealed that most of the heat, which is the driving-force for PCM switching, is generated in the selector rather than self-heating within the PCM layer. In other words, the selector acts as a heater. This simulation result indicates that

efficient heat transfer from the selector to the PCM layer, and its confinement by electrodes and sidewall are key for effective PCM switching.

To further investigate the effects of the TE and ME on the heat transfer and confinement, we fabricated the PCM/selector cells with different combination of the TE and ME thicknesses, as shown in Fig.3(a). The normalized reset current (Ireset) for each cell are compared in Fig.3(b). The Ireset decreased with increasing the TE thickness (ABC), indicating that the heat dissipation proceeded mainly from the TE, and thicker TE effectively confined the heat transferred from the selector. On the other hand, there was no apparent change in the Ireset with changing ME thickness (C, D). This could be due to the tradeoff between heat transfer and heat generation in the ME; thinner ME can transfer the generated heat more effectively, but its amount is smaller due to lower ME resistivity. For the PCM/selector cell, therefore, optimization of the TE thickness is crucial to control the PCM switching.

Fig.4 shows endurance characteristics of the cells with different thermal property liners. As shown in Fig.4(a), we found atoms constituting selector were diffused to PCM layer through the liner after 107 cycles in the case of liner-A, which is the cause of Vth shift by cycling stress. The Vth for liner-A shifted downward and, as a result, there was no memory window

remained after 107 cycles. On the other hand, the device with optimized liner-B showed stable Vth and memory window unchanged over >107 cycles (Fig.4(b)) owing to suppressed atom diffusion. This stable endurance property ensures reliable multi-level operation since Vth shift during cycling degrades memory window available for multi-level operation.

# III. MULTI-LEVEL PCM/SELECTOR CELL

Design concept of multi-level PCM/selector cell is shown in Fig.5. We optimized heat transfer inside the cell and PCM composition to stabilize the MRS in which crystalline and amorphous co-exist and were placed at designed positions. The MRS acts as a distinct third state besides LRS (crystalline state) and HRS (amorphous state). Vertical temperature gradient inside the PCM layer during reset operation is enhanced by thinning the TE, making upper part of the PCM layer difficult to melt. Thermal simulation in Fig.6 showed that the cell with optimized TE thickness can form the MRS over a wide range of programming voltage (Vp), whereas the cell with conventional TE gave narrow MRS region due to strong heat confinement. Moreover, it should be noted that phase change from crystalline to amorphous in the PCM layer proceeds vertically from bottom to top. This trend is different from that in conventional mushroom-type cell structure, where phase change is known to

proceed radially. This unique feature for the pillar-type structure is attributed to the comparable diameter of the heater (selector) and the PCM. Bottom surface of the PCM layer is heated almost uniformly as illustrated in Fig.6, and hence horizontal temperature gradient in the PCM is small. This can also be confirmed by thermal simulation result shown in Fig.2(b).

Since the phase change proceeds mainly in vertical direction, it could be possible to control the vertical position of the boundary between crystalline and amorphous states in the MRS by simply stacking the PCM layers having different melting point. We designed the PCM composition in the upper part to be Te-rich (Sb-poor) as evidenced by EDS spectrum in Fig.5. This increases the melting point of the upper PCM layer [10], preventing the amorphous state from expanding to upper layer. Optimization of heat dissipation and PCM composition makes upper part of the PCM layer difficult to be amorphous.

Fig.7 shows Vth evolution as a function of Vp for the optimized cell. The MRS is formed stably between the LRS and HRS. It is found that the Vth change to the MRS is abrupt (not gradual change), and the Vth value for the MRS is almost constant irrespective of Vp. This stable MRS implies that the boundary of amorphous and crystalline states in the MRS is pinned due to higher melting point in the upper PCM layer. The TEM image shown in Fig.7 confirmed that the MRS has

crystalline and amorphous phase in the upper and lower PCM layer, respectively. The invariability of Vth for the MRS over Vp is beneficial for achieving reliable multi-level operation in the cross-point array where the actual programming voltage could be dependent on the cell location due to wire resistance.

Next, we performed reprogramming experiments shown in Fig.8. Three kinds of programming pulse with different voltage amplitude were used for multi-level operation. We were able to freely reprogram the memory states to desired state regardless of their initial state by simply controlling the program voltage with the same pulse width. The abrupt switching and stable Vth for LRS, MRS and HRS realized reliable multi-level operation with just one single pulse. Our multi-level cell does not degrade program latency since it requires just one single pulse and there is no need to identify previous memory state for determining voltage amplitude, in contrast to the other MLC technologies [9,11]. We also note here that the minimum voltage amplitude used for our MLC operation is x0.75, meaning that it is compatible with conventional Vp/2 scheme which is widely employed for cross-point memory array operation. Fig. 9 shows endurance properties for the optimized cell. The MRS has good endurance properties owing to the optimized liner process, and the Vth window available for multi-level operation remains unchanged over 107 cycles.

# IV. DEMONSTRATION OF DENCE CROSS-POINT ARRAY

We fabricated a cross-point array with HP 20 nm using conventional cell structure. Fig.10(a) shows bird’s-eye SEM image for the one-deck 20 nm PCM/selector array with CMOS circuitry underneath. The TEM image for the 20 nm cell array is shown in Fig.10(b). Thickness of each component in the cell, such as PCM, selector, and TE, was set to be the same as that in conventional isolated cell in order to preserve the vertical thermal design. Programming characteristics are shown in Fig.10(c). We confirmed that the conventional cell showed binary LRS / HRS switching as expected and, moreover, the Vth window between LRS and HRS was almost the same as the isolated cell, indicating our vertical thermal design is valid even in the scaled array.

Thermal simulation for the cell array with HP 20 nm is shown in Fig. 11. It is found that the stable MRS can be formed by thinning the TE thickness, indicating heat dissipation mainly proceeds from TE for the scaled cell. Furthermore, the boundary of amorphous and crystalline states is flat owing to scaled horizontal dimension. This could further facilitate the formation of distinct MRS with the assist of PCM composition optimization in vertical direction. We also confirmed our thermal design is effective in the HP 14nm array. These results demonstrate our one-pulse programmable MLC cell design is feasible in the scaled array.

# V. CONCLUSION

We demonstrated multi-level PCM/selector cell by optimizing PCM composition and heat transfer inside the cell. We found via thermal simulation that the selector acts as heater, and the TE thickness optimization is critical for controlling PCM switching. It was further revealed that the PCM bottom surface

is heated uniformly due to comparable diameter of PCM and selector, showing the possibility to control vertical position of crystalline/amorphous boundary in the MRS by PCM composition design. Stable and distinct MRS with crystalline/amorphous at designed position was formed by one single pulse, requiring no verify or initialization. We also showed successful operation of dense PCM/selector cross-point memory array with HP 20 nm, and cell design space for onepulse multi-level operation, making it a promising future costeffective low latency and high density cross-point memory technology.

# REFERENCES
