---
title: "Disturb-Free Operations of Multilevel Cell Ferroelectric FETs for Nand Applications"
authors:
  - "Chengji Jin"
  - "Jiacheng Xu"
  - "Jiani Gu"
  - "Jiayi Zhao"
  - "Xiaole Jia"
  - "Jiajia Chen"
  - "Huan Liu"
  - "Miaomiao Zhang"
  - "Yue Peng"
  - "Bing Chen"
  - "Ran Cheng"
  - "Yan Liu"
  - "Xiao Yu"
  - "Genquan Han"
date: "2023-02-13"
year: "2023"
journal: "IEEE Transactions on Electron Devices"
doi: "10.1109/TED.2023.3242922"
abstract: "We have experimentally investigated disturb-free operations of multilevel cell (MLC)\\"
abstract_cn: "我们通过实验研究了NAND阵列中多级单元铁电场效应晶体管的无干扰操作。系统表征了制备的FeFET单元，并研究了将FeFET单元写入高稳定性多状态的优化方案。提出了实现FeFET\\"
keywords:
  - "[[FeFET]]"
  - "[[Multilevel cell]]"
  - "[[NAND array]]"
  - "[[Disturb-free operation]]"
cite: "[1] Jin C, Xu J, Gu J, et al. Disturb‑free operations of multilevel cell ferroelectric\\"
aiSum: "MLC FeFET NAND阵列无干扰操作：实验研究编程/读取干扰，提出稳定多级写入/读取方案，确定抑制电压与通过电压容限。"
confidence: "high"
wiki_concepts:
  - "[[FeFET]]"
---

Chengji Jin , Jiacheng Xu, Jiani Gu , Jiayi Zhao, Xiaole Jia, Jiajia Chen, Huan Liu, Miaomiao Zhang, Yue Peng, Member, IEEE, Bing Chen , Ran Cheng , Yan Liu , Xiao Yu , and Genquan Han

Abstract— We have experimentally investigated disturb-free operations of multilevel cell (MLC) ferroelectric field-effect transistors (FeFETs) in a NAND array. The fabricated FeFET cells are systematically characterized, and optimized schemes to write FeFET cells into multiple states with high stability are investigated. Write and read schemes to achieve stable MLC operations of FeFET NAND arrays are proposed. For the realization of disturb-free MLC operations, both program and read disturbs are systematically characterized at the array level. In addition, margins of program inhibition voltage $( V _ { \mathrm { i n h i b } } )$ and pass voltage $( V _ { p a s s } )$ are determined from the measurement results. This work provides a fundamental understanding of disturb-free MLC FeFET operations for NAND applications.

Index Terms— Disturb, ferroelectric field-effect transistors (FeFETs), multilevel cell (MLC), NAND.

# I. INTRODUCTION

F ERROELECTRIC field-effect transistors (FeFETs) haveemerged as one of the most promising nonvolatile memory technologies since the discovery of CMOS-compatible ferroelectric $\mathrm { H f O } _ { 2 }$ [1], [2], [3]. Currently, 3-D NAND flash is
  - "[[FeFET]]"

Manuscript received 9 January 2023; revised 31 January 2023; accepted 2 February 2023. Date of publication 13 February 2023; date of current version 24 March 2023. This work was supported in part by the National Natural Science Foundation of China under Grant 62204228, Grant 62204229, Grant 62204226, Grant 62025402, Grant 62090033, and Grant 91964202; in part by the Scientific Research Project of Zhejiang Lab under Grant 2021MD0AC01; in part by the Zhejiang Province Key Research and Development Programs under Grant 2022C01232 and Grant 2021C05004; and in part by the Zhejiang Provincial Natural Science Foundation under Grant LQ21E070002. The review of this article was arranged by Editor R. Wang. (Chengji Jin and Jiacheng Xu contributed equally to this work.) (Corresponding authors: Xiao Yu; Yan Liu.)

Chengji Jin, Jiacheng Xu, Jiani Gu, Jiajia Chen, Huan Liu, Miaomiao Zhang, and Xiao Yu are with the Research Center for Intelligent Chips and Devices, Zhejiang Lab, Hangzhou 311121, China (e-mail: yuxiao@zhejianglab.com).

Jiayi Zhao, Bing Chen, and Ran Cheng are with the School of Micro-Nano Electronics, Zhejiang University, Hangzhou 310058, China.

Xiaole Jia, Yue Peng, and Yan Liu are with the School of Microelectronics, Xidian University, Xi’an 710071, China (e-mail: xdliuyan@xidian.edu.cn).

Genquan Han is with the School of Microelectronics, Xidian University, Xi’an 710071, China, and also with the Research Center for Intelligent Chips and Devices, Zhejiang Lab, Hangzhou 311121, China.

Color versions of one or more figures in this article are available at https://doi.org/10.1109/TED.2023.3242922.

Digital Object Identifier 10.1109/TED.2023.3242922

![](images/be8144e5f7a8f6cff7b6daeec2cc6d2682872b9020bc9ef9bfc2955a0fdcf932.jpg)

![](images/8ceb0ecd4b680f42bdea770dfbcb7777fa0587c236719dd5650c23ba5bc6abbf.jpg)

![](images/862278875b0275a2857af8ed38a1bcb8e5a5c8f87e87031f563845d152d29461.jpg)  
Fig. 1. Motivation of this work. Directly characterize disturb in a FeFETbased NAND array and determine optimized write and read schemes for disturb-free MLC operations.

the main-stream storage class memory because of its mature fabrication process, high performance, and high storage density. 3-D vertical FeFET NAND can be considered as one of the possible alternatives to improve write latency and energy efficiency by simply introducing ferroelectric HfO2 [4], [5], [6], [7]. However, to compete with the 3-D NAND flash from the view of storage density, multilevel cell (MLC) operations with sufficient margins are essential. From the device level, gate-stack engineering, such as adopting multiple ferroelectric layers and inserting dielectric layers, is utilized for reliable MLC operations [8], [9], [10], [11]. However, there is a lack of array-level study on FeFET operation by far despite its importance, especially in MLC cases. Proper write and read schemes should be well considered for disturb-free MLC operations in a NAND array (see Fig. 1).

In this work, we systematically characterized FeFET devices and investigated the operation schemes to realize robust MLC operations of a FeFET cell. Then, the electrical characteristics are directly measured on a FeFET-based NAND array to verify MLC operations and perform disturb analysis at the array level.

# II. DEVICE FABRICATION

Fig. 2(a) illustrates the structure of fabricated FeFET by using the gate last process [see Fig. 2(b)]. Fabrication started from a p-type Si substrate. After active area (AA) patterning, shallow trench isolation (STI) was performed. Then, a dummy gate was formed by thermal oxidation of Si and chemical vapor deposition (CVD) poly-Si. After the $\mathrm { S i } _ { 3 } \mathrm { N } _ { 4 }$ spacer and lightly doped drain (LDD) formation, arsenic ions with 40-keV energy and $4 \times 1 0 ^ { 1 5 } \ \mathrm { c m } ^ { - 2 }$ dose were implanted for

![](images/e42d133d1b11591bcb85962ad33e96188f7d072f6e059e3fa87bd6c1a323e418.jpg)

![](images/8f7b676e7aaea8435814c965e011d57d7119a10c5bcd0b013e8f45663c11f657.jpg)

![](images/c74437606c22a1245103ef373e6c27af7861b1ae400a32ac1605d92aaef7661f.jpg)

![](images/3619c04cddadba7b89a47b02fa7382a070148283e33c603ac15e7077d96b950a.jpg)  
Fig. 2. (a) Schematic illustration of the fabricated device. (b) Key process flow. (c) Cross-sectional TEM image of W/TiN/HZO/SiO2/Si gate-stack.

![](images/58cd4f6eaabe8b50a567c1559c5ae2fcf5d3a9c73f5d0cf69e4cc0e53fb5ae6f.jpg)

![](images/aac9995b9e49ee6d9e53ec82483c64a5805796e107dee7b6e9997388a64900b5.jpg)

![](images/50c33db0985a4d68fc69069edfc7a68f3962c3cfe69c3b4cc17441e8db2ed2e0.jpg)  
Fig. 3. (a) Layout of a 16 × 16 FeFET array connected in parallel for P–V measurement. (b) Measurement setup. (c) Measured $\dot { P } - V$ curves with various voltage amplitudes of triangular waves.

source/drain (S/D). Dopant activation was performed by a spike annealing at $1 0 5 0 ~ ^ { \circ } \mathrm { C } .$ . After dummy gate removal, SiO2 interfacial layer (IL) was grown by ozone oxidation. Next, 10-nm HfZrOx (HZO) was deposited by atomic layer deposition (ALD). A 20-nm TiN and 75-nm W were deposited by sputter and CVD, respectively. Then, rapid thermal annealing (RTA) was carried out in $\Nu _ { 2 }$ ambient at $5 5 0 ~ ^ { \circ } \mathrm { C }$ for 1 min to crystallize HZO.

Fig. 2(c) shows the cross-sectional transmission electron microscope (TEM) image of the $\mathrm { W } / \mathrm { T i N } / \mathrm { H Z O } / \mathrm { S i O } _ { 2 } / \mathrm { S i }$ gatestack. The poly-crystalline nature of HZO is confirmed. Finally, interconnects and contact pads were formed. In addition, FeFET-based NAND arrays were fabricated by using the same process to investigate disturb-free write and read operations. The gate width/length (W/L) of FeFET single cells as well as arrays characterized in this study is 8/0.5 µm.

# III. RESULTS AND DISCUSSION

# A. FeFETs With MLC Capability

To verify the ferroelectricity of HZO in the gate-stack, polarization–voltage (P–V ) measurement was implemented on a $1 6 \times 1 6$ FeFET array [see Fig. 3(a)] by the ferroelectric analyzer (aixACCT TF3000). The measurement setup is shown

![](images/be68d111a733103a4ac6f175c71def5261e1e1c7f9867981a8f647a56451800c.jpg)

![](images/0e466d8cec93aa198cdbdd073cbd1de49db85f2505e00acdf0e2872c79572ee1.jpg)  
Fig. 4. Measured $V _ { \mathrm { { f h } } }$ distributions with different pulse amplitudes and widths for (a) erase (ERS) and (b) program (PRG) operations, respectively.

in Fig. 3(b). Voltage is applied at the gate electrode, while S/D and the substrate are virtually grounded to capture both electrons and holes response in the Si channel [12], [13]. Fig. 3(c) plots the measured P–V curves with various voltage amplitudes at 1 kHz. Minor loops due to partial polarization switching are observed [14], [15], [16], which is responsible for the MLC capability of FeFETs.

To determine the optimized write schemes for various states of MLC FeFETs, write pulses with different pulse widths and amplitudes are applied. Fig. 4(a) and (b) summarizes the threshold voltage $( V _ { \mathrm { t h } } )$ distribution after erase (ERS, from low to high $V _ { \mathrm { t h } }$ states) and program (PRG, from high to low $V _ { \mathrm { t h } }$ states), respectively. $V _ { \mathrm { t h } }$ is defined as $V _ { g }$ at $I _ { d } \ =$ 10 nA. Note that the program operation is more stable than the erase, which can be judged by monotonically increased $V _ { \mathrm { t h } }$ as pulsewidth and amplitude increase [see Fig. 4(b)]. However, $V _ { \mathrm { t h } }$ after erase [see Fig. 4(a)] exhibits local maximum because of more prominent charge trapping at negative $V _ { g }$ pulses. Therefore, we program devices to different $V _ { \mathrm { t h } }$ states by positive pulses instead of negative pulses for reliable MLC operations. In addition, such write schemes are for the ease of block erase in NAND applications.

Based on the measurement results in Fig. 4(b), the optimized write pulse schemes to achieve four different $V _ { \mathrm { t h } }$ states $( \mathrm { i . e . , \ ^ { . . } 0 0 , ^ { 9 } \ ^ { 9 } 0 1 , ^ { 9 } \ ^ { 4 } 1 0 , ^ { 9 } }$ and “11,” 2 bits/cell) can be determined, and the mechanisms of MLC operations are illustrated in Fig. 5(a). Fig. 5(b) plots the corresponding read $I _ { d } - V _ { g }$ curves measured for ten cycles. Four $V _ { \mathrm { t h } }$ states are tightly distributed by different write pulses, as shown in the cumulative distribution [see Fig. 5(c)]. In addition, we have investigated deviceto-device variation, as shown in Fig. 5(d) and (e), which indicate robust MLC operations of our fabricated devices. Fig. 6(a) plots the retention of the four $V _ { \mathrm { t h } }$ states. $V _ { \mathrm { t h } }$ slightly shifts to negative due to ferroelectric imprint [17], [18]. The endurance of the fabricated FeFET is also characterized [see Fig. 6(b)]. Four $V _ { \mathrm { t h } }$ levels are still separated after $1 0 ^ { 4 }$ program/erase cycles.

# B. Write/Read Schemes of FeFET NAND Arrays

Fig. 7 illustrates the proposed write and read bias schemes of the FeFET-based NAND array in this study. Note that each memory cell has four terminals (gate, source, drain, and p-well), and all the memory cells in a block share the same p-well terminal that enabling erase operations with high efficiency. Different from the erase operation by selecting a

![](images/9589f3ef1f69e9b84819e2815af85786cbbba6f498fc9db4310732be814554de.jpg)  
(a)

![](images/771db99d9f7e44ff8ed2379543be96dbeeec6126382cbda5e86dddba8748a0f2.jpg)

![](images/11606cb2f64c69492a977303407fb585562cd349e80726884b724fb7b903a08e.jpg)

![](images/fdfee8c74bc6a0f69bcf3e877b875948ca25989bb0a720d984ca1d329ed4727c.jpg)

![](images/e18d4eebe5b8998153ff251d29732957afbd9723fd896b1e8765a28490165ef7.jpg)

![](images/60717d1744b1c6acc937a15294037a49589091b3dd63eea4de5e091e8cc58ac4.jpg)  
Fig. 5. Demonstration of FeFET with 2 bits/cell. (a) Corresponding write pulse schemes and mechanisms of MLC operations for four different states. (b) Measured ten cycles of read $I _ { d } - \dot { V } _ { g }$ curves for each state. (c) Cumulative $V _ { \mathrm { { f h } } }$ distribution for ten cycles. Four $V _ { \mathrm { { f h } } }$ states are tightly distributed by different write pulses. (d) Read $I _ { d } - \ddot { V } _ { g }$ curves. (e) $V _ { \mathrm { t h } }$ distribution for 20 devices.

![](images/190710c816ea57f247e0e9a08f9dc47001f56219012678d375685de1b62faaab.jpg)

![](images/77890fb98511506f5868b5a6bb2acd8ec9eae22221b26771e4d2a3e4fe8411a4.jpg)  
Fig. 6. (a) Retention of four different states at RT. Negligible $V _ { \mathrm { { f h } } }$ shift is observed for all the states. (b) Endurance of MLC FeFET. Four $V _ { \mathrm { { f h } } }$ states are still separated after $1 0 ^ { 4 }$ cycles.

single cell via a drain-erase scheme shown in the previous works [19], erase is performed in a block unit with the help of shared p-well terminal in this work, which is more suitable for memory arrays with large size. Erase operation is performed with all the wordlines (WLs) grounded, and all the bitlines (BLs) and source are floating (F) [see Fig. 7(a)]. In the meanwhile, a positive erase voltage pulse (VERS) is applied to the p-well of the block area, which induces ferroelectric polarization switching to a negative value for all the cells. For the program operation shown in Fig. 7(b), it is performed by applying a program voltage pulse (VPRG) to the WL of the selected page, while a pass voltage $( V _ { \mathrm { p a s s } } )$ is applied to WLs

![](images/ef9eec09f48657facb408e31bcd68c7c09d03bba3b8a445f7247f476f68208ff.jpg)

![](images/f5f29c69ef42e667a127276d57b31000ebaf0f3786720c81f65be0b9ac0802b1.jpg)

![](images/ecc0774092cb3c0e013479cd713500b649306dcc24d71d799b5a89cf4f81d604.jpg)  
Fig. 7. Schematic illustration of the proposed (a) erase, (b) program, and (c) read schemes for a FeFET-based NAND array. Erase is performed in a block unit. $V _ { p a s s }$ is applied to unselected WLs during the program and read operations. $V _ { \mathrm { i n h i b } }$ is applied to unselected strings when the program is performed.

![](images/76cdc663ad33d85dc8e8a6a4ae57b2ec255fe497ae52d3f753e8850d079db416.jpg)

![](images/944fc75ffcdd56e66007b67ceb941196cc2c826124f4f52bf8a0b397258b6b35.jpg)

![](images/62b2a30b15ccd91b4b0a69ad37d545dc3f82da4b5386aed5252cda5030be0165.jpg)  
Fig. 8. (a) Fabricated $2 \times 2$ FeFET-based NAND array for the proof of concept. (b) $2 \times 2$ FeFET test structure in a typical NAND array. (c) Measured device-to-device variation in $\mathsf { a } \mathsf { } 2 \times 2$ FeFET NAND array.

of unselected pages to access the selected cell. The BL of the selected NAND string is grounded. Here, to prevent program disturb of the WL half-selected cells, a program inhibition voltage $( V _ { \mathrm { i n h i b } } )$ is applied to the BLs of unselected NAND strings. Meanwhile, the source and p-well are grounded with two select-gate transistors SGD ON and SGS OFF. Note that during program operations, SGS is OFF. In this way, no current flows through the NAND strings, and only polarization switching and charging parasitic capacitances consume power during program operations. Furthermore, $V _ { \mathrm { i n h i b } }$ can be passed to both source and drain of WL half-selected cells, unlike [20] where a positive bias at the source is necessary for reliable program inhibition. Similar methods by using $V _ { \mathrm { D D } } / 2$ or $V _ { \mathrm { D D } } / 3$ bias schemes have been proposed to inhibit program disturb in an AND-type FeFET array and verified by characterizing a single device [21], [22]. In addition, a $V _ { \mathrm { D D } } / 2$ bias scheme was proposed to inhibit the unselected cells in a two FeFET ternary content addressable memories (TCAMs) array [23]. As shown in Fig. 7(c), the read operation is performed by applying 1 and 0.2 V to the WL of the selected page and BL of the selected string, respectively, while $V _ { \mathrm { p a s s } }$ is applied to the WLs of unselected pages. Note that $V _ { \mathrm { p a s s } }$ may result in a $V _ { \mathrm { t h } }$ shift of unselected cells due to accumulative polarization switching even though $V _ { \mathrm { p a s s } }$ is low [24].

# C. Disturb-Free Operations of MLC FeFET NAND Arrays

To verify the proposed operation schemes, a $2 \times 2$ FeFETbased NAND array [see Fig. 8(a)], which is a simplified test structure of the typical NAND array [see Fig. 8(b)], is investigated for the proof of concept. Device-to-device variation of the FeFET array is characterized by dc $I _ { d } - V _ { g }$ sweep, as shown

![](images/d75508bd737b70cd014b150e3855d217646d2e32cda03cc73b77bd671179903d.jpg)

![](images/9a095f0de7bd581d7e50aa7bd22b45a527671ab7d2a839d5ddaf3f8e75650fa0.jpg)  
(b)

![](images/62aa42c02ce8453ba378c2871a2b369d0aafb23b9ed95098e0129478aaf3caa3.jpg)

![](images/45c816d07f95c9a2452f5311de6d7284fab8322140a00e34a762a6c2023c31fa.jpg)  
  
Fig. 9. Measurement sequence to characterize (a) program disturb and (b) read disturb. (c) Schemes utilized to characterize the program disturb. (d) Schemes utilized to read out $T _ { 0 0 }$ .

![](images/89825be16cc0c9279e09f6c6877653f94ca8e1c3d01fae800f4f14e5b113a0fd.jpg)

![](images/9888686bdb1482646fd4efed601e4c20ecb677c9636446df1b2dbc28285dcbd8.jpg)

![](images/326d84a5107538e2f02643948c2528c849557443b7dac00ef2d62c85476c8c3e.jpg)

![](images/84300dbcf6a440cde9f4ea5ef9b2259c604218c8da989825933a7b72137fc855.jpg)  
Fig. 10. Measured $V _ { \mathrm { { f h } } }$ after (a) 2.5-, (b) 3-, and (c) 4-V program operations as a function of $V _ { \mathrm { i n h i b } }$ on BL0. Four $V _ { \mathrm { { f h } } }$ states are well separated at high Vinhib, indicating successful MLC program operations at the array level. (d) Cumulative distribution of minimum disturb-free $V _ { \mathrm { i n h i b } }$ in the worst case (WL half-selected cells in $" 0 0 "$ state under 4-V program voltage).

in Fig. 8(c). According to the operation schemes mentioned above, the program disturb as well as the read disturb also referred to as the $V _ { \mathrm { p a s s } }$ disturb should be considered [19].

We first investigate the program disturb in a FeFET-based NAND array. Proper $V _ { \mathrm { i n h i b } }$ is applied to the BL of unselected strings to prevent the $V _ { \mathrm { t h } }$ shift of the WL half-selected cells. This $V _ { \mathrm { i n h i b } }$ raises the channel potential of the WL half-selected cells through the pass transistors and thus suppresses polarization switching. Fig. 9(a) illustrates the detailed measurement sequence of program disturb for each target state. Considering a NAND string $( T _ { 0 0 }$ and $T _ { 1 0 } )$ in $\textbf { a } 2 \times 2$ FeFET test structure [Fig. 8(a)], block erase (3 V, 100 µs) is performed to write all the cells to the $\mathbf { \vec { \Sigma } } ^ { 6 } 0 0 ^ { 5 }$ state. Then, VPRG (2.5/3/4 V, 100 µs) is applied to WL0, while a sufficient large $V _ { \mathrm { p a s s } } \left( 2 \mathrm { ~ V ~ } \right)$ is applied to WL1, with BL0 grounded and SL0 floating. In this way, $T _ { 0 0 }$ is written to different initial states. Next, the previous step is repeated but with $V _ { \mathrm { i n h i b } }$ applied to BL0 to emulate the bias condition of unselected strings during the program [see Fig. 9(c)]. Finally, the state of $T _ { 0 0 }$ is read out by sweeping WL0 from −0.5 to 1.5 V through the pass transistor $T _ { 1 0 }$ [see Fig. 9(d)].

Fig. 10 summarizes the measurement results for different VPRG/target states. Four $V _ { \mathrm { t h } }$ states are well separated at high $V _ { \mathrm { i n h i b } }$ bias, which means that successful MLC program operations can be achieved at the array level by the proposed schemes. States $ { \mathbf { \tilde { \Delta } } } ^ { 6 6 } 1 0 ^ { 7 } $ and $^ { \ 6 \ } 1 1 ^ { \circ }$ show slight program disturb even at low $V _ { \mathrm { i n h i b } }$ . However, states $\mathbf { \vec { \Sigma } } ^ { 6 } 0 0 ^ { 5 }$ and “01” show prominent program disturb at low $V _ { \mathrm { i n h i b } }$ , especially for the case of 4 V $V _ { \mathrm { P R G } }$ [see Fig. 10(c)]. To study the impact of device-to-device variation on program disturb, Fig. 10(d) plots the cumulative distribution of minimum disturb-free $V _ { \mathrm { i n h i b } }$ in the worst case (WL half-selected cells in “00” state under 4-V program voltage). Here, disturb-free is defined as the cases that the reduction of $V _ { \mathrm { t h } }$ is less than 50 mV after

the program operation with the corresponding applied $V _ { \mathrm { i n h i b } }$ on BL. Considering device-to-device variation, $V _ { \mathrm { i n h i b } }$ higher than 2 V is necessary for disturb-free program operations according to our measurement results. Nonetheless, too high $V _ { \mathrm { i n h i b } }$ will lead to a positive $V _ { \mathrm { t h } }$ shift of the WL half-selected cells because of the large voltage drop between the drain and gate [20], [25]. However, we do not observe such kind of phenomenon in this study due to the large size of the measuring devices. Note that the upper limit of $V _ { \mathrm { i n h i b } }$ should be well considered for ultrascaled devices, where the gate to S/D coupling is strong.

Besides the program disturb, we have further studied the read disturb at the array level by considering a NAND string $( T _ { 0 0 }$ and $T _ { 1 0 } )$ in a $2 \times 2$ FeFET test structure [see Fig. 8(a)]. Fig. 9(b) illustrates the detailed measurement sequence of read disturb for different initial states. Block erase (3 V, 100 µs) is performed to write all the cells to the $\ " 0 0 ^ { \prime }$ state. Then, both $T _ { 0 0 }$ and $T _ { 1 0 }$ are programmed to the same initial state by using the corresponding write scheme. Next, $T _ { 0 0 }$ readout is performed through pass transistor $T _ { 1 0 }$ by a WL0 voltage sweep from $- 0 . 5$ to 1.5 V while $V _ { \mathrm { p a s s } }$ is applied to WL1, during which $T _ { 1 0 }$ suffers from $V _ { \mathrm { p a s s } }$ stress at the gate electrode. To investigate the state of $T _ { 1 0 }$ after $V _ { \mathrm { p a s s } }$ stress, $T _ { 1 0 }$ readout is performed through pass transistor $T _ { 0 0 }$ by a WL1 voltage sweep from −0.5 to $1 . 5 ~ \mathrm { V } ,$ while $V _ { \mathrm { p a s s } }$ is applied to WL0. Fig. 11(a) and (b) plots the readout $V _ { \mathrm { t h } }$ for T00 and $T _ { 1 0 } ,$ respectively. Note that the readout $V _ { \mathrm { t h } }$ of $T _ { 0 0 }$ [see Fig. 11(a)] can be regarded as a reference without read disturb, since the $T _ { 0 0 }$ readout was performed before $V _ { \mathrm { p a s s } }$ stress. As $V _ { \mathrm { p a s s } }$ increases, disturb becomes stronger for all the states. To study the impact of device-to-device variation on read disturb, Fig. 11(c) plots the cumulative distribution of maximum disturb-free $V _ { \mathrm { p a s s } }$ in the worst case $( T _ { 1 0 }$ in the “00” state). $V _ { \mathrm { p a s s } }$ should not be higher

![](images/cbc23e6be84b6dbc8208a61479c15378bae4cc30df6788f41b82e0b2dfc38a51.jpg)

![](images/7ca41a17b4b1d106eae0cc2c9341eb96017fa9464e0b7c2cfdc3da63faa3527d.jpg)

![](images/69243d6e4a81dd75701d697b756526fe768e9c48a9721eb203f8d7f9eb0fb9e7.jpg)

![](images/94e51a9a8b3be4e6de8532d29951c49888d0496bd4327f868b1d7197aaa44409.jpg)  
Fig. 11. Readout $V _ { \mathrm { { f h } } }$ for (a) $T _ { 0 0 }$ and (b) $T _ { 1 0 } ,$ , respectively. Note that the readout $V _ { \mathrm { { f h } } }$ of $T _ { 0 0 }$ can be regarded as a reference without read disturb. (c) Cumulative distribution of maximum disturb-free $V _ { \mathsf { p a s s } }$ in the worst case $( T _ { 1 0 }$ in $" 0 0 "$ state). (d) Cumulative effect of $V _ { p a s s }$ stress in read operations.

![](images/16a3ef34ee6de59307eaa23f36c5e149a84a1a4b76592f69cbfceee487a78916.jpg)

![](images/29241222f69143ee0b1f4202c0bfe21c20100594418641358574be67bcf74357.jpg)  
Fig. 12. Schematic illustration of (a) $V _ { \mathrm { i n h i b } }$ and (b) $V _ { \mathsf { p a s s } }$ margins determined in this work.

than 2 V for disturb-free read operations by taking device-todevice variation into account. Fig. 11(d) shows the cumulative effect of $V _ { \mathrm { p a s s } }$ stress in read operations. Considering deviceto-device variation, we chose $V _ { \mathrm { p a s s } } ~ = ~ 2 ~ \mathrm { V }$ to perform the cumulative read disturb measurement. Negligible $V _ { \mathrm { t h } }$ shift is observed for all the states after ten read cycles. In this measurement, a single read cycle corresponds to applying $V _ { \mathrm { p a s s } }$ stress for ${ \sim } 5 \ \mathrm { s } ,$ since readout is performed by dc $I _ { d } - V _ { g }$ sweep. Therefore, the total cumulative $V _ { \mathrm { p a s s } }$ stress time in the measurement is ${ \sim } 5 0 ~ \mathrm { s } .$ . Considering a typical read pulsewidth of $1 0 \ \mu \mathrm { s } ,$ , at least $5 \times 1 0 ^ { 6 }$ times read operations can be done without any $V _ { \mathrm { t h } }$ degradation.

Fig. 12 summarizes $V _ { \mathrm { i n h i b } }$ and $V _ { \mathrm { p a s s } }$ margins of MLC operations in FeFET-based NAND arrays. According to our measurement results, $V _ { \mathrm { i n h i b } }$ higher than 2 V should be satisfied to prevent program disturb. Meanwhile, $V _ { \mathrm { i n h i b } }$ should be lower than a certain level, or $V _ { \mathrm { t h } }$ shift by drain erase would happen. For the $V _ { \mathrm { p a s s } }$ margin, $V _ { \mathrm { p a s s } }$ no higher than 2 V is required for read disturb-free operations in this study, while a sufficiently large $V _ { \mathrm { p a s s } }$ should be applied to achieve low channel resistance of pass transistors. Channel mobility improvement is still important to increase the $V _ { \mathrm { p a s s } }$ margin.

Our measurement results show that no disturb issues when S/D to gate voltage is lower than ∼2 V $( V _ { \mathrm { P R G } } / 2 )$ . This phenomenon is easily understood since the polarization switches only when the voltage across ferroelectric is high enough. Moreover, the $V _ { \mathrm { t h } }$ variations of scaled devices would be larger because of the stochastic switching mechanism of the ferroelectric domain and the limited domain number in a scaled device [26]. We can expect that the margins for both $V _ { \mathrm { i n h i b } }$ and $V _ { \mathrm { p a s s } }$ will shrink as the device scales down to tens of nanometer level. Decreasing domain size by gate-stack engineering [27], [28] is critical for improving variation and thus the $V _ { \mathrm { i n h i b } }$ and $V _ { \mathrm { p a s s } }$ margins.

# IV. CONCLUSION

We have systematically investigated the MLC operation of FeFETs in a NAND array. Write and read schemes to achieve stable MLC operations of FeFET NAND arrays are proposed. To realize disturb-free operations, program and read disturbs are systematically characterized at the array level, and the margins of $V _ { \mathrm { i n h i b } }$ as well $V _ { \mathrm { p a s s } }$ are determined. These results provide the guideline for realizing disturb-free MLC operations in FeFET-based NAND arrays that the operation schemes should be carefully determined.

# REFERENCES

[1] M. Trentzsch et al., “A 28nm HKMG super low power embedded NVM technology based on ferroelectric FETs,” in IEDM Tech. Dig., Dec. 2016, p. 11, doi: 10.1109/IEDM.2016.7838397.   
[2] S. Dunkel et al., “A FeFET based super-low-power ultra-fast embedded NVM technology for 22nm FDSOI and beyond,” in IEDM Tech. Dig., Dec. 2017, p. 19, doi: 10.1109/IEDM.2017.8268425.   
[3] A. I. Khan, A. Keshavarzi, and S. Datta, “The future of ferroelectric field-effect transistor technology,” Nature Electron., vol. 3, no. 10, pp. 588–597, Oct. 2020, doi: 10.1038/s41928-020-00492-7.   
[4] K. Florent et al., “First demonstration of vertically stacked ferroelectric al doped HfO2 devices for NAND applications,” in Proc. Symp. VLSI Technol., Jun. 2017, pp. T158–T159, doi: 10.23919/VLSIT.2017.7998162.   
[5] K. Florent et al., “Vertical ferroelectric $\mathrm { H f O } _ { 2 }$ FET based on 3-D NAND architecture: Towards dense low-power memory,” in IEDM Tech. Dig., Dec. 2018, pp. 2.5.1–2.5.4, doi: 10.1109/IEDM.2018.8614710.   
[6] M. Pesic et al., “Variability and disturb sources in ferroelectric 3D NANDs and comparison to charge-trap equivalents,” in Proc. IEEE Int. Memory Workshop (IMW), May 2022, pp. 1–4, doi: 10.1109/ IMW52921.2022.9779245.   
[7] S. Yoon et al., “Highly stackable 3D ferroelectric NAND devices: Beyond the charge trap based memory,” in Proc. IEEE Int. Memory Workshop (IMW), May 2022, pp. 1–4, doi: 10.1109/IMW52921. 2022.9779278.   
[8] T. Ali et al., “A multilevel FeFET memory device based on laminated HSO and HZO ferroelectric layers for high-density storage,” in IEDM Tech. Dig., Dec. 2019, p. 28, doi: 10.1109/IEDM19573.2019.8993642.

[9] K. A. Aabrar et al., “BEOL compatible superlattice FerroFET-based high precision analog weight cell with superior linearity and symmetry,” in IEDM Tech. Dig., Dec. 2021, p. 19, doi: 10.1109/IEDM19574. 2021.9720713.   
[10] C.-Y. Liao et al., “Multibit ferroelectric FET based on nonidentical double HfZrO2 for high-density nonvolatile memory,” IEEE Electron Device Lett., vol. 42, no. 4, pp. 617–620, Apr. 2021, doi: 10.1109/LED.2021.3060589.   
[11] K. Seidel et al., “Gate stack optimization toward disturb-free operation of ferroelectric HSO based FeFET for NAND applications,” in Proc. 19th Non-Volatile Memory Technol. Symp. (NVMTS), Oct. 2019, pp. 1–4, doi: 10.1109/NVMTS47818.2019.8986166.   
[12] K. Toprasertpong, M. Takenaka, and S. Takagi, “Direct observation of interface charge behaviors in FeFET by quasi-static split C-V and Hall techniques: Revealing FeFET operation,” in IEDM Tech. Dig., Dec. 2019, p. 23, doi: 10.1109/IEDM19573.2019.8993664.   
[13] S.-H. Kuk, S.-M. Han, B. H. Kim, S.-H. Baek, J.-H. Han, and S.-H. Kim, “An investigation of HZO-based n/p-FeFET operation mechanism and improved device performance by the electron detrapping mode,” IEEE Trans. Electron Devices, vol. 69, no. 4, pp. 2080–2087, Apr. 2022, doi: 10.1109/TED.2022.3154687.   
[14] P. Wang et al., “Investigating ferroelectric minor loop dynamics and history effect—Part I: Device characterization,” IEEE Trans. Electron Devices, vol. 67, no. 9, pp. 3592–3597, Sep. 2020, doi: 10.1109/TED.2020.3009623.   
[15] C. Jin, T. Saraya, T. Hiramoto, and M. Kobayashi, “Physical mechanisms of reverse DIBL and NDR in FeFETs with steep subthreshold swing,” IEEE J. Electron Devices Soc., vol. 8, pp. 429–434, 2020, doi: 10.1109/JEDS.2020.2986345.   
[16] C. T. Tung, G. Pahwa, S. Salahuddin, and C. Hu, “A compact model of polycrystalline ferroelectric capacitor,” IEEE Trans. Electron Devices, vol. 68, no. 10, pp. 5311–5314, Oct. 2021, doi: 10.1109/TED.2021.3100814.   
[17] Y. Higashi et al., “Impact of charge trapping on imprint and its recovery in HfO2 based FeFET,” in IEDM Tech. Dig., Dec. 2019, p. 15, doi: 10.1109/IEDM19573.2019.8993472.   
[18] F. Mo, T. Saraya, T. Hiramoto, and M. Kobayashi, “Reliability characteristics of metal/ferroelectric-HfO2/IGZO/metal capacitor for nonvolatile memory application,” Appl. Phys. Exp., vol. 13, no. 7, Jun. 2020, Art. no. 074005, doi: 10.35848/1882-0786/ab9a92.

[19] G. Choe, W. Shim, P. Wang, J. Hur, A. I. Khan, and S. Yu, “Impact of random phase distribution in ferroelectric transistors-based 3-D NAND architecture on in-memory computing,” IEEE Trans. Electron Devices, vol. 68, no. 5, pp. 2543–2548, May 2021, doi: 10.1109/ TED.2021.3068086.   
[20] P. Wang et al., “Drain–erase scheme in ferroelectric field-effect transistor—Part I: Device characterization,” IEEE Trans. Electron Devices, vol. 67, no. 3, pp. 955–961, Mar. 2020, doi: 10.1109/TED.2020.2969401.   
[21] S. Mueller et al., “From MFM capacitors toward ferroelectric transistors: Endurance and disturb characteristics of HfO2-based FeFET devices,” IEEE Trans. Electron Devices, vol. 60, no. 12, pp. 4199–4205, Dec. 2013, doi: 10.1109/TED.2013.2283465.   
[22] K. Ni, X. Li, J. A. Smith, M. Jerry, and S. Datta, “Write disturb in ferroelectric FETs and its implication for 1T-FeFET AND memory arrays,” IEEE Electron Device Lett., vol. 39, no. 11, pp. 1656–1659, Nov. 2018, doi: 10.1109/LED.2018.2872347.   
[23] X. Yin, K. Ni, D. Reis, S. Datta, M. Niemier, and X. S. Hu, “An ultradense 2FeFET TCAM design based on a multi-domain FeFET model,” IEEE Trans. Circuits Syst. II, Exp. Briefs, vol. 66, no. 9, pp. 1577–1581, Sep. 2019, doi: 10.1109/TCSII.2018.2889225.   
[24] H. Mulaosmanovic et al., “Investigation of accumulative switching in ferroelectric FETs: Enabling universal modeling of the switching behavior,” IEEE Trans. Electron Devices, vol. 67, no. 12, pp. 5804–5809, Dec. 2020, doi: 10.1109/TED.2020.3031249.   
[25] P. Wang et al., “Drain-erase scheme in ferroelectric field effect transistor—Part II: 3-D-NAND architecture for in-memory computing,” IEEE Trans. Electron Devices, vol. 67, no. 3, pp. 962–967, Mar. 2020, doi: 10.1109/TED.2020.2969383.   
[26] S. Deng et al., “A comprehensive model for ferroelectric FET capturing the key behaviors: Scalability, variation, stochasticity, and accumulation,” in Proc. IEEE Symp. VLSI Technol., Jun. 2020, pp. 1–2, doi: 10.1109/VLSITechnology18217.2020.9265014.   
[27] H. J. Kim et al., “Grain size engineering for ferroelectric $\mathrm { H f } _ { 0 . 5 } \mathrm { Z r } _ { 0 . 5 } \mathrm { O } _ { 2 }$ films by an insertion of Al O interlayer,” Appl. Phys. Lett., vol. 105, no. 19, Nov. 2014, Art. no. 192903, doi: 10.1063/1.4902072.   
[28] S. F. Lombardo et al., “Local epitaxial-like templating effects and grain size distribution in atomic layer deposited Hf0.5Zr0.5O2 thin film ferroelectric capacitors,” Appl. Phys. Lett., vol. 119, no. 9, Aug. 2021, Art. no. 092901, doi: 10.1063/5.0057782.