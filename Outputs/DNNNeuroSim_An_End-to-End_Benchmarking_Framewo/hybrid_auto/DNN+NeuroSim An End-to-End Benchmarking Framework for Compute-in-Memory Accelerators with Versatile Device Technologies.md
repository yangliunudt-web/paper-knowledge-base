---
title: "DNN+NeuroSim: An End-to-End Benchmarking Framework for Compute-in-Memory Accelerators with Versatile Device Technologies"
authors:
  - "Xiaochen Peng"
  - "Shanshi Huang"
  - "Yandong Luo"
  - "Xiaoyu Sun"
  - "Shimeng Yu"
date: "2021-01-01"
year: "2021"
journal: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
abstract: "DNN+NeuroSim is an integrated framework to benchmark compute-in-memory (CIM) accelerators for deep neural networks, with hierarchical design options from devicelevel, to circuit-level and up to algorithm-level. A python wrapper is developed to interface NeuroSim with popular machine learning platforms such as Pytorch and Tensorflow. The framework supports automatic algorithm to hardware mapping, and evaluates both chip-level performance and inference accuracy with hardware constraints. In this work, we analyze the impact of reliability in “analog” synaptic devices, and analog-to-digital converter (ADC) quantization effects on the inference accuracy. Then we benchmark CIM accelerators based on SRAM and versatile emerging devices including RRAM, PCM, FeFET and ECRAM, from VGG to ResNet, and from CIFAR to ImageNet dataset, revealing the benefits of high on-state resistance, e.g. by using three-terminal synapses. The open-source code of DNN+NeuroSim is available at https://github.com/neurosim/DNN_NeuroSim_V1.0."
keywords:
  - "[[In-memory computing]]"
  - "[[Benchmarking framework]]"
  - "[[NeuroSim]]"
  - "[[Deep neural networks]]"
cite: "[1] Peng et al. DNN+NeuroSim: An End-to-End Benchmarking Framework for Compute-in-Memory Accelerators with Versatile Device Technologies[J]. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, 2021."
aiSum: "DNN+NeuroSim基准测试框架：支持SRAM/RRAM/PCM/FeFET/ECRAM等器件，评估存内计算加速器的芯片面积、延迟、能效、推理精度，开源代码提供VGG/ResNet在CIFAR/ImageNet上的硬件约束性能分析。"
confidence: "medium"
wiki_concepts:
  - "[[In-memory computing]]"
---

# DNN+NeuroSim: An End-to-End Benchmarking Framework for Compute-in-Memory Accelerators with Versatile Device Technologies

Xiaochen Peng, Shanshi Huang, Yandong Luo, Xiaoyu Sun and Shimeng Yu School of Electrical and Computer Engineering, Georgia Institute of Technology, Atlanta, GA Email: shimeng.yu@ece.gatech.edu

Abstract—DNN+NeuroSim is an integrated framework to benchmark compute-in-memory (CIM) accelerators for deep neural networks, with hierarchical design options from devicelevel, to circuit-level and up to algorithm-level. A python wrapper is developed to interface NeuroSim with popular machine learning platforms such as Pytorch and Tensorflow. The framework supports automatic algorithm to hardware mapping, and evaluates both chip-level performance and inference accuracy with hardware constraints. In this work, we analyze the impact of reliability in “analog” synaptic devices, and analog-to-digital converter (ADC) quantization effects on the inference accuracy. Then we benchmark CIM accelerators based on SRAM and versatile emerging devices including RRAM, PCM, FeFET and ECRAM, from VGG to ResNet, and from CIFAR to ImageNet dataset, revealing the benefits of high on-state resistance, e.g. by using three-terminal synapses. The open-source code of DNN+NeuroSim is available at https://github.com/neurosim/DNN_NeuroSim_V1.0.

# I. INTRODUCTION

To solve the bottleneck of extensive data transfer in the conventional von Neumann architectures, compute-in-memory (CIM) has emerged as a promising paradigm for designing the machine learning hardware accelerator. Recently, the device community has been engineering “analog” synaptic devices for representing the weights in the deep neural network (DNN). These candidates include RRAM [1], PCM [2], FeFET [3] and ECRAM [4], etc. Till today, it still lacks a holistic methodology to evaluate these emerging device properties from the CIM system’s perspective. The prior work in IEDM 2017 [5] reported a benchmarking framework named MLP+NeuroSim that could evaluate the impact of device non-ideal properties. However, the prior work was limited to a 2-layer fully connected network for MNIST dataset only, with a focus on the synaptic-array level estimation, while the chip-level peripheries (such as buffers and interconnects) are missing. To enable the machine learning accelerator design to accommodate flexible neural network topologies and support large-scale datasets such as CIFAR and ImageNet, it is crucial to develop a new simulator with comprehensive hierarchical design options from device-level, to circuit-level and up to algorithm-level.

In this work, we propose an end-to-end benchmarking framework for the inference engine with offline training. Our approach is to build a python wrapper to interface NeuroSim, a hardware macro model, with popular machine learning

platforms such as Pytorch and Tensorflow. This approach could enable the exploration of CIM accelerator designs for flexible network topologies such as VGG-8 [6] for CIFAR-10, and ResNet-18 [7] for ImageNet, as well as versatile device technologies from CMOS (e.g. SRAM) to beyond-CMOS (two-terminal and three-terminal non-volatile memories).

# II. INTEGRATED FRAMEWORK PRINCIPLES

# A. Framework Structure

Fig. 1 shows the framework structure of DNN+NeuroSim. Flexible DNN topologies are setup in python wrapper (Pytorch and Tensorflow based on low precision training method WAGE [8]), while the weight precision (limited by device multilevel states) and partial sum quantization (limited by ADC precision) are introduced during the software offline training phase, and device retention degradation model [9] is introduced during the hardware inference phase. Fig. 1 (c) shows the simulator taking network topology as input to automatically design the chip floorplan (considering layer by layer computation), while weight-duplication [10] is introduced to maximize memory utilization (defined as percentage of the used memory over the total memory). This is a feature needed for convolutional layer where the unrolled kernel size is smaller than the memory subarray size, in order to speed up DNN processing. Fig. 1 (d) shows during inference in python wrapper, the traces of synaptic weights and neural activations are unrolled, saved and sent to NeuroSim core, then partitioned and assigned to different locations of the chip according to the automatic floor planning rule. The top-down hierarchy of the CIM system is defined as chip, tile, processing element (PE) and synaptic array. The framework outputs include the hardware-constrained inference accuracy (from python wrapper), and hardware metrics such as chip area, latency, dynamic energy, leakage power, as well as energy efficiency and throughput (from NeuroSim core) for layer-by-layer computation mode. The modular circuit component estimation are all calibrated by SPICE simulations across technology nodes with PTM models.

# B. Architecture of CIM Accelerators

Fig. 2 shows the detailed system architecture from chip level down to synaptic-array level. In different levels, peripheries are introduced, including buffers, interconnects (based on H-tree routing), neural-functional units (such as pooling, accumulation and activation). The synaptic array could be implemented by SRAM, two-terminal devices such as RRAM, PCM and STT-MRAM, or three-terminal devices such as FeFET and ECRAM,

while both sequential (row-by-row) and parallel read-out schemes are available for each of these device technologies.

# III. BEHCMARK RESULTS

In CIM inference engine, data retention and ADC quantization are the key factors for inference accuracy degradation. Here we evaluate their impacts and benchmark across technologies on an accelerator design based on VGG-8, for CIFAR10 dataset, with 8-bit weight and 8-bit activation precision.

# A. Data Retention

As the analog intermediate state retention still needs more experimental characterization, we consider four representative scenarios of conductance drift [9], which are drifting to maximum, minimum or intermediate states, and random drift. Fig. 3 (b-d) show the inference accuracy as a function of time, while the conductance are assumed to drift towards different final states (from -1 to 1, according to the algorithm weight range), or randomly drift, based on three various drift rates, which are equivalent to conductance drift by 2%, 6% and 10 % over 10 years, respectively. The results show that, in scenarios with fixed drift directions, drifting to maximum or minimal states degrade the accuracy faster than drifting to the middle states, while the random drift is the best scenario for maintaining inference accuracy even for 10 years (assuming the equivalent conductance drift by 2%).

# B. ADC Quantization

Typical weight matrix size is larger than the memory sub-array size (if unrolling the 4D kernels into 2D arrays in convolutional layers), therefore, partial sum going through ADC needs to be accumulated from multiple sub-arrays. Here we assume practical array sizes from 64×64 up to 256×256, with three kinds of memory cell precision (1-bit/cell, 2-bit/cell and 4- bit/cell), and sweep the ADC precision from 3-bit to 5-bit (with nonlinear quantization), to find the optimal design option considering the trade-offs between inference accuracy and hardware overhead. Fig. 4 shows with 1-bit cell precision, 4-bit ADC is sufficient to guarantee ~89% accuracy for 64×64 and 128×128 synaptic array, while 5-bit ADC is necessary to avoid significant accuracy loss in multi-bit cell precisions. Fig. 5 shows the trade-offs when increasing the array size. Increasing array size results in smaller chip area but worse throughput and energy efficiency, due to large column currents and parasitic loading capacitance. The radar plot shows that the design based on 128×128 array size with 5-bit ADC achieves relatively balanced trade-offs among accuracy, energy efficiency, throughput, area and memory utilization. Fig. 6 shows the impact of ADC and memory cell precisions on hardware performance. Higher ADC precision is detrimental to the area and energy efficiency, while higher memory cell precision is beneficial because the peripheral circuitry could be saved.

# C. Benchmark Across Device Technologies

Table 1 shows the benchmarking results across state-of-the-art device technologies, where the sequential and parallel read-out SRAM-based accelerators are evaluated at both 7nm and 32nm, and the parallel read-out NVM-based accelerators at 32nm. The

reason for choosing 32nm for NVMs is because state-of-the-art RRAM is at 22nm [11], PCM is at 40nm [12], and FeFET is at 28nm [3]. Consider the read-noise and on/off ratio, 4-bit/cell is assumed for [1, 2, 3, 4]. The benchmark results show that, large on-state resistance $R _ { o n }$ is the key factor to achieve better hardware performance. To avoid large voltage drop, the transistors in 1T1R or peripheral mux have to be sized up for small $R _ { o n } \mathrm { . }$ , yielding significant area overhead. As a result, it takes longer time to activate the synaptic arrays (due to the increased capacitance loading), adversely increasing latency and lowering throughput. Thus, the conventional RRAM [11] or PCM [2] with a couple kΩ to tens of kΩ is not competitive, even with multi-bit per cell. Overall, the “analog” synaptic device based designs with large $R _ { o n } \left( > 1 0 0 \mathrm { k } \Omega \right)$ (e.g. interfaceengineered analog RRAM [1] or three-terminal FeFET [3] and ECRAM [4]) at 32nm could achieve superior energy efficiency (in TOPS/W) than parallel SRAM-based design at 7nm, plus the benefits of non-volatility for instant-on applications.

# IV. FRAMEWORK PERFORMANCE

To explore the framework’s performance to large-scale system, we extend a FeFET [3] based inference engine benchmarking with a deeper DNN, i.e. ResNet-18 for ImageNet, comparing the results and run-time for different simulation methods. The real-traced simulation is the default method in the framework (all the traces are transferred and accessed hierarchically). In pseudo-traced simulation, the traces are only accessed once to generate the activity parameters of weight and activations (percentage of non-zero values in traces) for each layer, which are passed hierarchically as inputs instead of the large traces (to save simulation run-time). Similarly, but without trace accessing, the average simulation only passes user-assumed activity parameters (e.g. 50%). Fig. 7 shows that with reasonable run-time, the real-traced framework achieves most accurate results, while the other two methods underestimate the performance (due to inaccurate column-current estimation).

# V. CONCLUSION

In this work, we develop an end-to-end framework to benchmark CIM-based inference engine, which integrates NeuroSim with Pytorch and Tensorflow. With introduced device retention model and ADC quantization effects, it is efficient to investigate the trade-offs among inference accuracy, energy efficiency, throughput, area and memory utilization. With parallel read-out scheme and large $R _ { o n }$ , the “analog” synaptic device based accelerators show promises. An improved version of DNN+NeuroSim with on-chip training capability is under development for future release.

# ACKNOWLEDGMENT

This work is supported by ASCENT, one of the SRC/DARPA JUMP centers, NSF/SRC E2CDA program, and NSF-CCF-1903951.

# REFERENCE

[1] W. Wu et al. VLSI 2018.P. [2] W. Kim et al. VLSI 2019. [3] K. Ni et al. IEDM 2018. [4] J. Tang et al. IEDM 2018. [5] P.-Y. Chen et al. IEDM 2017. [6] K. Simonyan et al. ICLR 2015. [7] K. He et al. CVPR 2015. [8] S. Wu et al. ICLR 2018. [9] P.-Y. Chen et al. IRPS 2018. [10] X. Peng et al. ISCAS 2019. [11] Jain et al. ISSCC 2019. [12] J.Y. Wu et al. IEDM 2018.

![](images/9569e3ebe007e76c47a35f537165ec6b944ad3b84a097909972dfb8650fdc04f.jpg)  
Python Wrapper   
(a)

![](images/8081531f02594040ed2dfb9e338a3574d740de6051767fdc8c2a62803de9a715.jpg)  
(b)

![](images/87debba6c471fb33b67a19c359cc21c33a912aefbacfd8df448b6e9721afc0e7.jpg)

![](images/e0d1139884b9b1ff7ac3e56486e5fadd6f3e4e126573cbe6fa6844d57acbe8b7.jpg)

![](images/aaa786b72871a0cd919a1dc99e3810c50ab72ae468174492d61764dfe41be211.jpg)

![](images/ee100ea007fdab33dd297e001580a186e1006c80aef1b209e2ce35e58fb16d6a.jpg)  
Synaptic Weight & Neural Activations

![](images/ecb9f44826d694ad027f6236566ec8c49b07b2d24cb2bae0799c24c59b8f1bad.jpg)  
(e)   
Fig. 1. Framework structure of DNN+NeuroSim. (a) DNN setup in python wrapper, software training with hardware constraints such as weight precision and partial sum quantization; (b) introduction of retention model and ADC quantization effects to inference accuracy; (c) pre-defined network structure is loaded as input to NeuroSim core, for automatic floor planning which weight-duplication to maximize memory utilization; (d) loading real trace (synaptic weights and neural activations) into NeuroSim, mapping data to conductance and digital voltage input cycles, which are to be partitioned and assigned to different locations of the CIM system; (e) hierarchical simulation from chip to tile, and from processing element (PE) to synaptic array.

![](images/7c6870518fab1427e0735eab4d6eb066d01dd6cdb2edba379f939f89261ec7b1.jpg)

![](images/205760d4e084d708a00068c62136116391db3c2d8d0a7830ccca5250a07d51ad.jpg)  
Tile Level

![](images/8fdaeb210985b2d7ef2a5ecbd32ee13ca9a6c32585cec9094e1031f951167b4b.jpg)  
PE Level

![](images/918b5601b5247f94a75bc6216d011489e0ce6983bb7dc0f0fa19648f781dbf6e.jpg)

![](images/c85376f9e12c933835f04c703912cc1e3f340a4adfeeef436ce421f10697ddc1.jpg)

![](images/4a242d52d130b300ae73de0698c73699a9ed0b656b662f055a6acd5b7736318a.jpg)  
Fig. 2 (a) Architecture structure defined in the simulator, the top level of chip contains tiles, global buffer and neural-functional peripheries (including pooling, accumulation and activations). Inside a tile, it is further portioned into multiple processing elements (PEs), while each PE consists of several synaptic arrays, along with adder trees and local buffers. H-tree routing is used for interconnect. (b) Parallel read-out synaptic arrays based on SRAM, two-terminal NVMs (RRAM, PCM and STT-MRAM), and three-terminal NVMs (FeFET and ECRAM). Sequential (row-by-row) read-out modes also available. The circuit modules are all calibrated by SPICE simulations across technology nodes with PTM model.

![](images/3dbb9d8562681fef5ac75d6ec0d3d53d0979917743c816aaad5f7bae59e83a2e.jpg)  
(a) Drift Scenarios

![](images/c12ec2fa2693070b9d88fe11e2c47f92f7f078af2085daca52bcce1bd38bb05c.jpg)  
(b) 10% G Drift @ 10 years

![](images/d76d28906e2f60dd86815252df87294a363fb24cf5adfbc1b5d512a67d86678b.jpg)  
(c) 6% G Drift @ 10 years

![](images/028a790a4726b91ad614538970f10ca462d808be9f1b1a955eda124c822ae204.jpg)  
(d) 2% G Drift @ 10 years   
Fig. 3. (a) Different scenarios of conductance drift. Inference accuracy as a function of time for equivalent conductance drift by (b) 10%; (c) 6%; (d) 2% at 10 years, with different conductance uni-directional drifting targets (maximum 1 or minimum -1 or other intermediate states) or random drift of each weights.

Table 1. Benchmark results of DNN accelerators on VGG-8 for CIFAR10, based on SRAM (both sequential and parallel read-out at 7nm and 32nm), and reported “analog” synaptic devices (assumed at 32nm technology). Green bold values shows the devices with good performance.   

<table><tr><td colspan="10">VGG-8 (8-bit activation; 8-bit weight) on CIFAR10, with Novel Weight Mapping and Dataflow [9]</td></tr><tr><td>Technology node (LSTP)</td><td colspan="2">7 nm</td><td colspan="7">32 nm</td></tr><tr><td>Device</td><td colspan="2">SRAM</td><td>SRAM</td><td>RRAM (Intel) [11]</td><td>TaOx/HfOx (TsingHua) [1]</td><td>GST PCM (IBM) [2]</td><td>HZO FeFET (NotreDame) [3]</td><td colspan="2">ECRAM (IBM) [4]</td></tr><tr><td>ADC precision</td><td>Sequential</td><td>4-bit</td><td>Sequential</td><td>4-bit</td><td>5-bit</td><td>5-bit</td><td>5-bit</td><td>5-bit</td><td>5-bit</td></tr><tr><td>Cell Precision</td><td colspan="2">1-bit</td><td>1-bit</td><td>2-bit</td><td>4-bit</td><td>4-bit</td><td>4-bit</td><td>4-bit</td><td>4-bit</td></tr><tr><td>Ron (Ω)</td><td>\</td><td>\</td><td>\</td><td>\</td><td>6k</td><td>100k</td><td>40k</td><td>500k</td><td>500M</td></tr><tr><td>On/Off Ratio</td><td>\</td><td>\</td><td>\</td><td>\</td><td>17</td><td>10</td><td>12.5</td><td>100</td><td>40</td></tr><tr><td>Inference Accuracy (%)</td><td colspan="2">92%</td><td colspan="2">92%</td><td colspan="5">91%</td></tr><tr><td>Area (mm2)</td><td>4.65</td><td>4.28</td><td>97.83</td><td>87.47</td><td>86.07</td><td>20.45</td><td>22.63</td><td>19.71</td><td>19.71</td></tr><tr><td>Memory Utilization (%)</td><td>99.29%</td><td>99.29%</td><td>99.29%</td><td>99.29%</td><td>98.69%</td><td>97.05%</td><td>97.05%</td><td>97.05%</td><td>97.05%</td></tr><tr><td>L-by-L Latency (ms)</td><td>0.85</td><td>0.15</td><td>1.61</td><td>0.33</td><td>19.92</td><td>1.16</td><td>2.65</td><td>0.38</td><td>0.28</td></tr><tr><td>L-by-L DynamicEnergy (uJ)</td><td>13.25</td><td>10.63</td><td>162.79</td><td>76.82</td><td>285.96</td><td>32.17</td><td>38.41</td><td>27.69</td><td>28.57</td></tr><tr><td>L-by-L Leakage power (mW)</td><td>104.85</td><td>101.69</td><td>1.41</td><td>1.33</td><td>0.22</td><td>0.11</td><td>0.11</td><td>0.11</td><td>0.11</td></tr><tr><td>Energy Efficiency (TOPS/W)</td><td>3.95</td><td>14.95</td><td>3.70</td><td>7.92</td><td>2.10</td><td>18.97</td><td>15.76</td><td>22.17</td><td>21.51</td></tr><tr><td>Throughput (FPS)</td><td>1171.15</td><td>6875.94</td><td>619.53</td><td>3001.13</td><td>50.16</td><td>859.75</td><td>378.03</td><td>2617.24</td><td>3623.67</td></tr></table>

![](images/61be63a4b3f5e0552ce1b5bb68bd54d3515623e7ea1e97488cdcc06d10e7453d.jpg)

![](images/e94ec78b917685ee87415a128c6cf4d3488314e583e68ba908de31f93d8f08aa.jpg)

![](images/98b5a92b9729ccb390e93c5fda18fa46f9a53e23049fbc4c65d9d03a5bcdb9c7.jpg)

![](images/f59d49c3dfdec9492f10d92ea2324ce8802ae5b6e2754fba0bcd6dbf64092a14.jpg)  
Fig. 4. Inference accuracy for VGG-8 for CIFAR10 as a function of ADC precision with different memory cell precision, at array size of (a) 64×64; (b) 128×128 and (c) 256×256, based on interface-engineered TaOx/HfOx RRAM [1]. 5-bit ADC is necessary for multi-bit per cell to maintain accuracy.

![](images/49c6eed6fabc17accf1e4bfe637f8e6c5d4b3f9db296d8129becc64004ae3e10.jpg)

![](images/de26960cecb1b345dbd2975f3d8055334b7070cb44c2e1ceba2b6c015578a121.jpg)  
Fig. 5. Comparison of inference accuracy, memory utilization, area, energy efficiency and throughput, across different synaptic array sizes with 4-bit cell precision for VGG-8 for CIFAR10, based on interface-engineered TaOx/HfOx RRAM [1]. 128×128 array size with 5-bit ADC is chosen as a balanced design option.

![](images/1cb5126c19e163d28a6d838f7bd707a326208a814c4142debd803b99b1cdb217.jpg)  
Fig. 6. Impact of ADC precision and cell precision on area and hardware performance, with 128×128 array size based on interface-engineered TaOx/HfOx RRAM [1].

Fig. 7. Benchmark results of FeFET-based [3] DNN accelerators on ResNet-18 for ImageNet, with three different estimation methods (real trace, pseudo-trace and average). Green bold values shows real-traced method achieves more accurate estimation as other two methods underestimate the CIM performance, though real-traced method runs slower in a workstation (Intel Xeon Gold-6136 24-core 3.0GHz with 256GB DDR4).   
![](images/d79edf1af91e53ba04a0fff9b208c639765a80ab1d5d558de7fdf7f52cff1442.jpg)  
* Storage & Logic: bufers, digital logic modules (e.g. decoder, switch matrix, mux), interconnect   
* Accumulation: adders, shift+adders, adder trees, accumulation units

<table><tr><td>Latency (ms)</td><td>Real-traced</td><td>Pseudo-traced</td><td>Average</td></tr><tr><td>Area (mm2)</td><td colspan="3">20.08</td></tr><tr><td>TOPS/W</td><td>11.6</td><td>6.14</td><td>5.93</td></tr><tr><td>FPS</td><td>330</td><td>326</td><td>326</td></tr><tr><td>Run Time (s)</td><td>460</td><td>86</td><td>2</td></tr></table>