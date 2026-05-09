---
title: "Benchmarking Test-Time DNN Adaptation at Edge with Compute-In-Memory"
authors:
  - "Zhenkun Fan"
  - "Zishen Wan"
  - "Che-Kai Liu"
  - "Anni Lu"
  - "Kshitij Bhardwaj"
  - "Arijit Raychowdhury"
date: "2024-07-01"
year: "2024"
journal: "ACM J. Auton. Transport. Syst."
abstract: "The prediction accuracy of deep neural networks (DNNs) deployed at the edge can deteriorate\\"
abstract_cn: "部署在边缘设备上的深度神经网络（DNN）的预测准确率会随着时间的推移因数据分布的变化而下降。为了提高鲁棒性，DNN需要不断改进和提高其预测能力。然而，在资源有限的边缘环境中进行适应面临以下挑战：（i）新的标记数据可能无法获得；（ii）由于云连接可能无法访问，必须在设备上进行适应；（iii）适应过程应优先考虑速度、内存效率和节能。存内计算（CIM）因其计算效率和优越的运行带宽而受到关注。此外，新兴的轻量级无监督DNN测试时适应技术在增强有噪数据模型准确度方面显示出良好的结果。本文首次对这些方法进行了全面的基准测试探索，评估了在边缘和自主系统中不同CIM架构下的性能和能效。我们的研究发现，提出的适应策略能够适应环境变化和固有的硬件噪声。通过进行跨层的算法-硬件-技术协同设计空间探索，我们强调了各种DNN适应技术和CIM配置在准确度、性能和能耗之间的重要权衡。"
keywords:
  - "[[Compute-In-Memory]]"
  - "[[DNN Adaptation]]"
  - "[[Edge Computing]]"
  - "[[Autonomous Systems]]"
  - "[[Test-Time Adaptation]]"
  - "[[存内计算]]"
  - "[[神经网络适应]]"
  - "[[边缘计算]]"
  - "[[自动驾驶系统]]"
  - "[[测试时适应]]"
cite: "Fan Z, Wan Z, Liu C K, Lu A, Bhardwaj K, Raychowdhury A. Benchmarking Test-Time DNN\\"
aiSum: "本研究提出了一个基准测试框架，用于评估在配备CIM硬件的受限边缘设备上测试时DNN适应技术。研究发现：（1）部分网络适应往往优于全网络适应；（2）CIM设备能效高但存在非理想性；（3）适应技术能有效处理环境数据偏移和硬件噪声；（4）在UAV自主导航中显著降低能耗和延迟。研究涵盖了监督和无监督方法，以及SRAM/RRAM混合CIM系统。"
confidence: "medium"
wiki_concepts:
  - "[[Edge computing]]"
  - "[[存内计算]]"
---

# Benchmarking Test-Time DNN Adaptation at Edge with Compute-In-Memory

ZHENKUN FAN, Georgia Institute of Technology, Atlanta, United States

ZISHEN WAN, Georgia Institute of Technology, Atlanta, United States

CHE-KAI LIU, Georgia Institute of Technology, Atlanta, United States

ANNI LU, Georgia Institute of Technology, Atlanta, United States

KSHITIJ BHARDWAJ, Lawrence Livermore National Laboratory, Livermore, United States

ARIJIT RAYCHOWDHURY, Georgia Institute of Technology, Atlanta, United States

The prediction accuracy of deep neural networks (DNNs) deployed at the edge can deteriorate over time due to shifts in the data distribution. For heightened robustness, it’s crucial for DNNs to continually refine and improve their predictive capabilities. However, adaptation in resource-limited edge environments is fraught with challenges: (i) new labeled data might be unavailable; (ii) on-device adaptation is a necessity as cloud connections may be inaccessible; and (iii) the adaptation procedure should prioritize speed, memory efficiency, and energy conservation. Compute-In-Memory (CIM) has recently garnered attention for its computational efficacy and superior operational bandwidth. Additionally, emerging lightweight unsupervised DNN adaptation techniques during test-time have showcased promising results in enhancing model accuracy for data with noise. This article pioneers a holistic benchmarking exploration of these methods, assessing their performance and energy efficacy across diverse CIM architectures in edge and autonomous systems. Our findings reveal that the proposed adaptation strategies can adapt to both environment shifts and inherent hardware noise. Engaging in a thorough cross-layer algorithm-hardware-technology co-design space exploration, we highlight pivotal trade-offs among accuracy, performance, and energy for various DNN adaptation techniques and CIM configurations.

CCS Concepts: • Hardware → Modeling and parameter extraction; Non-volatile memory; Emerging tools and methodologies; Memory and dense storage; • Computer systems organization → Neural networks;

Additional Key Words and Phrases: Adaptation, compute-in-memory, autonomous system, edge computing

Zhenkun Fan and Zishen Wan contributed equally to this research.

This work was supported in part by CoCoSys, one of seven centers in JUMP2.0, a Semiconductor Research Corporation (SRC) program sponsored by the Defense Advanced Research Projects Agency (DARPA). This work was performed under the auspices of the U.S. Department of Energy by Lawrence Livermore National Laboratory under Contract DE-AC52- 07NA27344.

Authors’ Contact Information: Zhenkun Fan, Georgia Institute of Technology, Atlanta, Georgia, United States; e-mail: zfan87@gatech.edu; Zishen Wan, Georgia Institute of Technology, Atlanta, Georgia, United States; e-mail: zishenwan@ gatech.edu; Che-Kai Liu, Georgia Institute of Technology, Atlanta, Georgia, United States; e-mail: che-kai@gatech.edu; Anni Lu, Georgia Institute of Technology, Atlanta, Georgia, United States; e-mail: alu75@gatech.edu; Kshitij Bhardwaj, Lawrence Livermore National Laboratory, Livermore, California, United States; e-mail: bhardwaj2@llnl.gov; Arijit Raychowdhury, Georgia Institute of Technology, Atlanta, Georgia, United States; e-mail: arijit.raychowdhury@ece.gatech.edu.

![](images/0347630522847a5cf19688fcce08fb957a67ecf554c3cefa9b497cb3e0f4423d.jpg)

This work is licensed under a Creative Commons Attribution International 4.0 License.

© 2024 Copyright held by the owner/author(s).

ACM 2833-0528/2024/07-ART16

https://doi.org/10.1145/3665898

# ACM Reference Format:

Zhenkun Fan, Zishen Wan, Che-Kai Liu, Anni Lu, Kshitij Bhardwaj, and Arijit Raychowdhury. 2024. Benchmarking Test-Time DNN Adaptation at Edge with Compute-In-Memory. ACM J. Auton. Transport. Syst. 1, 3, Article 16 (July 2024), 26 pages. https://doi.org/10.1145/3665898

# 1 INTRODUCTION

While deep neural networks (DNNs) undergo thorough training and validation using extensive datasets before their deployment on edge devices, they remain susceptible to degradation in prediction accuracy in real-world post-deployment scenarios. This degradation is primarily caused by shifts in the distribution of new input data samples, a phenomenon known as “dataset shifts” [12]. Such shifts often arise from sensor disturbances or environmental interferences [69]. To bolster the robustness of DNNs, various techniques, including data augmentation [29] and adversarial training [35], have been employed during offline training. However, these methods may not be adequate to handle the diverse range of data shifts that can occur after deployment. As a result, it is imperative to adapt neural networks to improve their prediction accuracy [22, 39, 49, 68].

Various transfer learning methodologies have been proposed to adapt neural networks on edge devices. One approach involves fine-tuning using a modest set of labeled target data. This strategy has proven effective in improving performance while outperforming domain generalization methods cost-effectively [39, 47, 56, 74]. It entails training a model on a large source dataset initially and then fine-tuning the pre-trained model on a smaller target dataset to adapt to distribution shifts. Another realm of application is when the labels for the new test data are not present, potentially domain-shifted, such as devices operating in remote places without human intervention [9, 18] or when the cost of annotating the new data with labels is too high and not feasible [27, 69]. Representative scenarios include (i) DNNs performing human action recognition on drones without labeled samples [18], (ii) techniques such as laser-induced breakdown spectroscopy in extreme environments (e.g., other planets) [8], or (iii) medical imaging where noise could be added due to scanners and the DNN for analysis needs to rapidly adapt without labeled data [27].

To ensure that deployed DNNs maintain or elevate their prediction accuracy while meeting stringent performance constraints in streaming applications, real-time on-device adaptation to new shifted test data is crucial. Relying on cloud-based adaptation may not always be practical due to stringent timing deadlines or devices being in connectivity-deficient regions. Predictiontime adaptation at the edge presents unique challenges, primarily concerning speed and efficiency. DNNs processing streaming data are frequently up against tight timelines, making rapid adaptation a necessity. Moreover, edge devices are often resource-constrained and may rely on battery power, making lightweight and energy-efficient adaptation imperative.

In the race to achieve efficient adaptation on resource-constrained edge platforms, Compute-In-Memory (CIM) systems have gained prominence. Such systems, including analog crossbar arrays, effectively combat the memory bottlenecks intrinsic to von Neumann architectures [59]. Analog crossbars harness various memristive devices, such as Resistive Random-Access Memories (RRAMs), Phase Change Memories (PCMs), and Ferroelectric Field-effect Transistors (FeFETs), which are extensively researched for their capability to perform low-precision DNN inference efficiently with high throughput [62]. Despite their advantages, CIM systems face unique challenges stemming from device-to-device variations, temporal conductance drift in memristive devices, and parasitic resistances in metallic interconnects within crossbar arrays [2, 13, 19, 32, 67]. These non-idealities might tamper with a DNN’s weights and lead to accuracy degradation in realworld applications.

This article introduces a benchmarking framework and conducts a comprehensive measurement study of prediction-time DNN adaptation techniques, encompassing both supervised and unsupervised approaches, on CIM hardware substrates at the edge. To the best of our knowledge, this study is the first to explore both supervised and unsupervised approaches for resource-constrained devices with CIM technology. Our study aims to address the following algorithm-hardware co-design questions: (i) For each CIM hardware configuration, what constitutes the optimal choice of a robust DNN and test-time adaptation algorithm in terms of three key objectives: prediction accuracy, adaptation time, and energy dissipated during adaptation? (ii) What bottlenecks are encountered when executing these algorithms on various CIM architectures? (iii) Can adaptation techniques effectively address both environmental data shifts and inherent hardware noise to improve accuracy? Built upon the benchmarking framework, we conduct a series of design space exploration analyses, revealing intriguing and, at times, non-obvious outcomes, and illustrating crucial tradeoffs between accuracy, performance, energy consumption, and memory utilization. Furthermore, our assessment extends to scenarios involving autonomous navigation by unmanned aerial vehicles (UAVs), where we showcase significant reductions in energy consumption and compute latency without compromising on performance, as gauged by the Mean Safe Flight (MSF) metric, i.e., the average flight distance before the crash.

This article, therefore, makes the following contributions:

— A benchmarking framework for evaluating DNN adaptation techniques, both supervised and unsupervised, on resource-constrained edge devices and UAV autonomous systems equipped with CIM hardware substrates.   
— A holistic evaluation of DNN adaptation techniques across diverse hardware configurations, showcasing their ability to adapt to both external environmental shifts and inherent hardware noise.   
— Insights from cross-stack algorithm-hardware-technology co-design space exploration, highlighting critical trade-offs between accuracy, performance, and energy efficiency concerning different DNN adaptation algorithms and CIM designs.

The rest of this article is organized as follows. Section 2 describes various techniques of DNN adaptation and CIM. Section 3 presents our proposed benchmarking suite for DNN adaptation with CIM at the edge. Section 4 conducts a cross-layer algorithm-hardware-technology evaluation of the adaptation with design space exploration. Section 5 further evaluates adaptation on UAV autonomous systems. Section 6 discusses pipelining partial adaptation. The article concludes with summaries in Section 7 of test-time DNN adaptation at edge with CIM. We have publicized the framework in github repo (https://github.com/SenFFF/CIM_Adaptation/).

# 2 BACKGROUND

In this section, we delve into techniques aimed at enhancing the robustness of DNNs during training. Additionally, we will explore adaptation techniques and recent developments in this field. Finally, we will introduce the concept of CIM with emerging non-volatile memory technologies.

# 2.1 Enhancing Robustness of DNNs During Training

Two widely adopted approaches for improving the robustness of DNNs are data augmentation and adversarial training, both of which are elaborated below.

2.1.1 Data Augmentation. Data augmentation is a strategy in which a neural network is trained using both the original “clean” samples (such as images in CIFAR-10) and their noisy counterparts [29]. This approach helps improve the generalization capability of the DNNs. Techniques such as Cutout, which removes sections of an image [21], CutMix, in which parts of one image

replace portions of another [73], and AugMix, which applies a variety of transformations (rotate, posterize, etc.) and then combines the modified images, have proven effective in enhancing DNN generalization capability [29].

2.1.2 Adversarial Training. Adversarial training is designed to make a neural network robust against adversarial attacks. Its training involves a min-max optimization problem, in which adversarial samples are generated from clean ones by introducing imperceptible perturbations. The network is then trained to both maximize prediction loss for these adversarial samples and minimize it for the clean ones [20, 24].

# 2.2 Adaptation

Recent advancements in the field of adaptation emphasize unsupervised domain adaptation, especially fine-tuning specific neural network layers during test-time. Techniques such as “Norm” adapt batch-normalization (BN) parameters by recomputing the mean and standard deviation statistics during test-time inference [49, 58], “Tent” [68] optimizes transformation parameters in addition to BN parameters but also performs a backpropagation pass at test-time to optimize the transformation parameters that apply channel-wise scales and shifts to the features, and “Surgical”fine-tunes different convolution layers based on the type of data corruption [39]. These works provide important insights into the overhead of running these algorithms on resource-constrained devices but only focus on adapting batch-norm parameters. Another recent work adapted batch-norm parameters to improve accuracy for lane detection applications in autonomous driving [9]. In our work, we focus on layers beyond batch-norm, such as convolutional and fully connected (FC) layers, and target not just corruptions but also noise due to analog operation inherent in in-memory computing architectures.

# 2.3 Compute-In-Memory

CIM has emerged as a promising architectural paradigm, facilitating operations across entire memory blocks by seamlessly integrating fundamental processing capabilities within the memory itself, thus effectively surmounting the memory wall challenge that existed in the Von Neumann machine [40]. With novel models leaning towards memory-intensive operation on smaller, resourceconstrained devices at the edge [19, 75], benchmark existing algorithms with edge devices become even more critical.

Specifically, the CIM paradigm is able to perform matrix-vector multiplication, the operation that is ubiquitous in today’s novel machine learning models [1, 16, 31], within one clock cycle, and CIM has been leveraged to accelerate several operation- and data-intensive workloads such as vector symbolic architecture [34, 43], recommendation systems [15], reinforcement learning [42], spiking neural networks [48, 57], deep neural networks [50], bioinformatics [4], and so on. These CIM designs leverage novel non-volatile memory (NVM) technologies such as RRAM [14], Fe-FET [61], and PCM [5] for inference and/or training for novel applications.

Recent works have been actively exploring CIM benchmarking. DNN+NeuroSim [51] is tailored for assessing CIM accelerators over a broad spectrum of device technologies and architectures. Reis et al. [55] concentrate on the modeling and benchmarking of CIM architectures, delving into design space exploration and the evaluation of various memory technologies. He et al. [25] investigate the design space and memory technology co-exploration for CIM-based machine learning accelerators, seeking to find the optimal mix of design variables and memory technologies to enhance performance and reduce power consumption and area. NVMExplorer [53] introduces a comprehensive framework for cross-stack comparisons of embedded NVM technologies.

Although benchmarking DNN with CIM has been widely implemented, DNN adaptation benchmarked against CIM has yet to be investigated. In addition, inspired by the fact that DNN

adaptation that is benchmarked against the state-of-the-art Von Neumann machine cannot satisfy the real-time and energy requirement at the edge [6, 7], in this work, we perform a thorough DNN adaptation benchmarking with CIM by truthfully integrating the existing CIM DNN benchmarking tool NeuroSim [50] for adaptation, enabling a different network wrapper to be integrated with the underlying circuit components.

# 3 BENCHMARKING DNN ADAPTATION WITH CIM AT THE EDGE

In this section, we focus on illustrating our test-time adaptation framework and its components for benchmarking adaptation on edge CIM macros. We first present the overview flow of our algorithm-hardware benchmarking study in test-time adaptation. We then elaborate on the experimental details, including algorithms (models, datasets, quantization schemes) and hardware (CIM architecture, memory devices, and inherent hardware noise features). Lastly, we discuss the evaluation metrics and design space exploration case study.

# 3.1 Adaptation Study Overview

Figure 1 shows an overview of our hardware-algorithm benchmark study for test-time DNN adaptation at the edge with CIM. We first train a model on a relatively large source dataset from metaenvironments and then fine-tune the pre-trained model on a small target dataset as a means of adapting to distribution shifts. In our work, we only adapt a part of the network model during the fine-tuning stage while freezing the other layers.

Typically, adaptation involves a set of more conservative hyper-parameters, for instance, a smaller learning rate. The object to be adapted is a model pre-trained on a given dataset on the cloud. The goal is to strengthen model robustness when encountering different input data distribution or when non-ideal factors such as device non-ideality deplete model resilience [54]. By denoting trainable parameters of an n-layer network as $( \theta _ { 1 } , \ldots \theta _ { n } )$ , pre-training can be formulated as the following:

$$
\operatorname *{arg  min}_{\theta_{i}}L(x,y),i\in [1,n].
$$

Here, x refers to input data and y the corresponding output. Contrary to conventional wisdom that one should fine-tune the whole model or the last few layers to reuse the learned features, we observe that fine-tuning only the part of layers of the network results in better performance for image corruption datasets and autonomous navigation scenarios, which is in line with [39]. This means that we judiciously choose parameters in certain layers, but not all of them, to perform backpropagation and weight updates, i.e.,

$$
\underset {\sum_ {\theta_ {i}}} {\arg \min } L (x _ {s h i f t}, y _ {s h i f t}), \sum_ {\theta_ {i}} \subseteq (\theta_ {0}, \ldots , \theta_ {n}),
$$

where $x _ { s h i f t }$ and $y _ { s h i f t }$ are the test data and their labels (in supervised learning scenarios) due to distribution shifted or inherent CIM noise during on-device adaptation.

# 3.2 Dataset and Model

Datasets. We conducted our experiments primarily on the CIFAR-10 dataset and its variants. To simulate the circumstances of data distribution shift, we applied CIFAR-10-Corruption (CIFAR-10-C) and CIFAR-Flip to represent the workload distribution encountered after network deployment [28]. Before deploying, we pre-trained the models with CIFAR-10 while testing and adaptation were both carried out on variant CIFAR datasets (CIFAR-10-C, CIFAR-Flip). Figure 2 gives an example of how the original image is distorted [63].

![](images/6aea2604f2503f9fd584508b70bd1eea0491bdcf159e72fb562acdc9e15f2a3f.jpg)  
Fig. 1. Overview of our hardware-algorithm benchmarking study of test-time adaptation at edge with CIM.

![](images/f339ac281d14bfa24e0f14cba2838bed740bd8c59f6e31e56bb04b69895c356d.jpg)  
Fig. 2. A demonstration of the dataset we used in this work to train the model and its variant to simulate data distribution shift.

Models. Since the CIFAR dataset is meant for image classification, we chose three imageprocessing neural network models as our candidate workload. VGG8 represents the so-called ‘shallower’ network. ResNet20 [26] and DenseNet40 [30] are selected as ‘deeper’ networks. Our evaluation results demonstrate that the number of layers (i.e., network depth) has impacts on the adaptation strategy, especially under quantization scenarios.

WAGE Quantization. Hardware that operates at the edge suffers from limited energy and area budgets. Energy and area consumption associated with floating-point (FP) operations are not advantageous for edge systems. In addition, the FP operation is not favorable when it comes to CIM-based implementations. Therefore, we applied WAGE as our quantization methodology [71].

WAGE quantizes four main operands (Weight, Activation, Gradient, Error) in backpropagation, rendering network deployment on edge possible. WAGE mainly covers linear and convolutional layers. Other layer types, such as maxpooling and batch norm, are omitted assuming they would be handled by other modules.

# 3.3 Compute-In-Memory Framework

Our adaptation benchmarking framework of this work is built based on NeuroSim [50–52], an end-to-end CIM macro-to-architecture simulation toolkit. NeuroSim is capable of evaluating both the algorithmic network model and CIM hardware performance during the training and inference phases. It has incorporated PyTorch and WAGE quantization in its Python-based shell wrapper and uses chip-validated data to calibrate the C++-based files for analytical hardware performancepower-area estimations [45]. We refer to the hardware evaluation module (aforementioned C++- based files) as “core” in the following text. The input feature map, layer weights, and gradient traces generated from training are recorded for detailed analysis for hardware evaluations.

NeuroSim has set up its own design principle to determine what would be the CIM macro’s architecture given some user-specified macro parameters, starting from NVM device characteristics to architecture-dependent parameters. To perform partial adaptation analysis, we intervene in trace communication between the Python shell and core by modifying weight and gradient traces during adaptation. In a similar manner, all sorts of CIM hardware non-ideality are simulated by blending mathematical models into the trace files. We refer to NeuroSim manuals for a detailed description of execution flow and non-ideality modeling [72]. A high-level workflow abstraction of the adaptation framework can be found in Figure 4.

Parameter settings. We use the default parameter settings in NeuroSim throughout the adaptation experimentation, except for the memory cell type and subarray size. The VGG8 network is evaluated with a 128×128 subarray whereas ResNet20 is evaluated with a 32×32 subarray. The array size is chosen to prevent violating the design principle set up by NeuroSim. The experiments are mainly conducted with Static Random Access Memory (SRAM) and RRAM with different technology nodes. We use a unified bit-width of 8 in WAGE quantization to support training. The batch size is set to 200 and the epoch is usually 3 to accommodate the endurance of eNVM cells. We use 1,000 images for CIFAR-10-C implementation, with an 8:2 split for training and testing. When tested on CIFAR-10-C, the numbers reported in Section 4 are obtained through averaging test set accuracy among 10 types of corruptions. The severity for CIFAR-C is set to 5 (which is the most severe) and images are shuffled every time when the test set is loaded.

Memory Cells. We evaluate both SRAM and RRAM with different technology nodes for testtime adaptation. RRAM is chosen as the representative NVM with its Complementary Metal-Oxide-Semiconductor (CMOS) compatibility, small cell area, low read latency and energy, and more. In addition to the difference in the memory technology, SRAM and RRAM necessitate different peripherals in their respective systems. For instance, CIM with RRAM requires the array to operate in the mixed signal realm whereas SRAM-based CIM indicates a pure digital configuration. At the circuit level, a level shifter for boosting the programming of RRAM and a calibrated sensing scheme [60] will be taken into consideration for the RRAM-based design. In addition to analyzing fully SRAM-based and RRAM-based adaptation systems, we explore the hybrid memory design paradigm by leveraging the unique characteristics of SRAM and RRAM. The adaptable layers are mapped onto SRAM due to its better write performance and endurance while the frozen layers are mapped onto RRAM due to its superior read performance and density.

Device Non-ideality. Traditional storage devices, such as Dynamic Random Access Memory (DRAM) and SRAM, rely on charge-based mechanisms. Additional peripherals and mechanisms are implemented to ensure the maintenance and correct operation of the bits within these

![](images/c3f9853b208d535dcfe95100971f5eb906585efec30b8675cc9557b0f468ec79.jpg)  
Fig. 3. Effect of WAGE quantization with ideal ON/OFF ratio and silicon-validated ON/OFF ratio. The red dotted line in the middle indicates the original evenly distributed data points.

![](images/5c3cae6900964f2fb30332fdc1906d3307a066b4b36b88fcb348241cf59a72eb.jpg)  
Fig. 4. The high-level abstraction of the proposed CIM adaptation estimation framework.

cells. In the case of SRAM, a group of transistors competes to maintain a stable state, whereas DRAM requires periodic refreshing to counteract charge leakage. These storage devices typically incorporate a larger noise margin to ensure the accuracy of the stored bit patterns. In contrast, resistive NVM cells store information using their resistance state. For instance, PCM exhibits varying cell resistance, thereby representing 0 or 1 states with different crystalline structures [23, 41]. RRAM forms or disrupts a conductive path to achieve its low-resistance state (LRS) and highresistance state (HRS) [33]. In the case of RRAM, as a cell undergoes numerous write operations, its physical structure gradually deteriorates, leading to a decrease in the on-off ratio (i.e., highstate resistance divided by low-state resistance). We model this on-off ratio as a linear scaling on the quantization axis, as illustrated in Figure 3. Furthermore, various types of inherent hardware noise, such as device-to-device variation, cycle-to-cycle variation, non-linearity introduced by retention issues, and quantization error introduced by the analog-to-digital interface, can all potentially damage the accuracy and hardware performance and power efficiency of the systems that employ NVM devices. We incorporate these device non-ideality factors into our adaptation benchmarking framework and investigate the effectiveness of test-time adaptation on both environmental data distribution shifts and inherent hardware noise. The non-ideality parameters have been validated against fabricated testchips [17, 46].

# 3.4 Evaluation Metrics and Design Space Exploration

Metrics. For DNN supervised and unsupervised adaptation (Section 4), we consider model testtime accuracy as the algorithmic metric for DNN performance, as well as compute latency and energy consumption as the CIM hardware metrics for DNN efficiency. For autonomous navigation system adaptation (Section 5), we consider the autonomous agent’s safe travel distance, compute latency, compute energy, and end-to-end task completion energy as the evaluation metrics.

Design Space Exploration (DSE). To establish a benchmarking framework enabling presilicon adaptation performance evaluation on CIM macros for designated workloads, we further conduct DSE analysis (Section 4.7) to identify the optimal algorithm-hardware configurations given the accuracy, latency, and power constraints of the deployment system.

# 4 ADAPTATION EVALUATION RESULTS

In this section, we elucidate the outcomes of our experiments on test-time DNN adaptation. Initially, we delve into the influence of various adaptation strategies on model performance in both supervised and unsupervised learning scenarios, considering different types of noise. Capitalizing on the complementary attributes of NVM devices, we then probe into the potential of hybrid CIM adaptation. Subsequently, we underscore the ability of test-time adaptation to manage both shifts in data distribution and inherent hardware noise. Finally, we venture into the adaptation design space tailored for distinct deployment contexts.

To provide clear insights, we employ varied configurations of our adaptation benchmarking platform to address the subsequent Research Questions (RQs):

RQ1: How effective is the DNN test-time adaptation with CIM in handling data distribution shifts?   
RQ2: What is the effectiveness of DNN test-time adaptation with CIM in addressing outputlevel shifts?   
RQ3: How does the DNN test-time adaptation with CIM perform for unsupervised learning tasks?   
RQ4: What constitutes the hardware overhead of NN test-time adaptation in CIM?   
RQ5: How does an SRAM/NVM hybrid–based CIM system benefit DNN test-time adaptation?   
RQ6: Is the DNN test-time adaptation capable of adjusting to both data distribution shifts and inherent CIM hardware noise?

# 4.1 DNN Adaptation for Data Distribution Shift

RQ1: Evaluating adaptation performance for various DNN models under data distribution shift. In this RQ, we investigate the impact of adaptation on three distinct DNN models. We elucidate that test-time adaptation with CIM effectively elevates task accuracy. Notably, the choice of adaptation strategy influences not just the model’s performance but also the hardware overhead stemming from the adaptation process.

In this work, we use adaptation to enhance the robustness of DNN models. It seems like a natural choice to tune all trainable parameters of the network with distribution-shifted data. Yet, it could be either energy-consuming or achieving non-optimal performance. Previous studies pointed out that adapting the whole network could potentially degrade some learned features in the network [39]. Tuning layers altogether could lead to modules deviating from their pre-trained optimal status. Addressing data distribution shifts while ignoring other noise sources, the optimal adaptation strategy appears to be context specific. For instance, deploying a pre-trained network on edge devices may result in low image quality, where adapting shallow layers could significantly enhance accuracy. This is because the initial layers, responsible for low-level feature extraction, may not be

![](images/9c29f3771fa2f61f2a8af80905fd61b72b71e62edf5eeadad4e2d585aaf70c81.jpg)  
(a)

![](images/7b279ee34942b2e3d6bd312a399b02269286fa5d0d33f72476cb4f3cd392850c.jpg)  
(b)

![](images/2850b4654fc0dccf9f7a241b0b7224844307c9803397edd45d86be4158a885c4.jpg)  
(c)   
Fig. 5. The relative accuracy gain of VGG8/ResNet20/DenseNet40 adaptation on input-level data distribution shift (CIFAR-10-C), with regard to inference accuracy before adaptation. The unsupervised adaptation adopts Shannon entropy [68] as the loss function.

well suited to processing noisy images. Adapting these layers can thus yield substantial improvements. Conversely, shifts in higher-level features may be best addressed by adapting middle layers, which bridge the gap between low-level features and more abstract representations. For example, adapting these layers can help the model recognize new shapes or patterns. Similarly, shifts at the output or label level, such as those exemplified by the CIFAR10-flip dataset, call for adaptations in the final mapping layers to correct mismatches between high-level features and labels.

We first train three DNN models, VGG8, ResNet20, and DenseNet40, on CIFAR-10 while quantizing them with WAGE regulation. We observe that all three models suffer accuracy loss when tested on CIFAR-10-C images. However, after test-time adaptation with CIM, the accuracy improves on CIFAR-10-C images. As adaptation is conducted in the granularity of blocks, we treat every two consecutive layers as one block in VGG8. For ResNet/DenseNet, we treat each basic block/Dense block as one block unit. The relative accuracy gain of test-time adaptation with CIM with regard to no adaptation is shown in Figure 5.

Figure 5 showcases that both full and partial model adaptations enhance accuracy compared with the original model. Intriguingly, adapting select blocks within DNN models often yields better results than full-model adjustments. Speaking in a quantitative manner, partial adaptation surpasses full adaptation in more than 80% of test cases throughput our experiments. Specifically, by fine-tuning a single parameter block while keeping others static, we achieve superior outcomes in addressing distribution shifts. Furthermore, optimal performance is observed when different blocks are tuned to cater to varied types of distribution shifts. For instance, adjusting the first block of VGG8 proves most effective for input-level shifts such as CIFAR-C (image corruption).

However, this observation isn’t universally valid, as evident from the results of ResNet20 and DenseNet40. We speculate that this discrepancy arises due to the quantization effect. To validate our assumption, we examine the mean of weight gradient across layers for the three networks. As depicted in Figure 6(a), deeper models such as ResNet20 and DenseNet40 have layers where the gradient is quantized to zero, meaning that the correction data of specific layers is neglected—a phenomenon absent in the comparatively shallower VGG8. Subsequent experiments revealed that, on average, 12.3% of trainable parameters in ResNet20 and 9.7% in DenseNet40 receive a zero weight gradient, whereas none receives a zero weight gradient in VGG8. Given that backpropagation processes deeper layers first followed by shallower ones, shallow layers accumulate more quantization errors. That is because gradient computation for shallow layers relies on deeper layers’ activation gradient. This leads to a reduced adaptation accuracy boost for shallow blocks compared with their floating-point counterparts. Such inefficiency could be further exacerbated by the

![](images/368a097b230c85282186909508c1c417cf9a5dae0d4c224c611bf2e54be75684.jpg)  
(a)

![](images/bb9a875a7be652c1cab997cc58bdadea0f9daf8d32e6532e28e80442ca05614e.jpg)  
(b)   
Fig. 6. (a) The mean value of the quantized weight gradient during adaptation. (b) The relative accuracy gain of adaptation on three DNN models upon CIFAR-Flip dataset.

minimal learning rate used for adaptation, which makes gradient values even more susceptible to quantization.

# Takeaway #1

We show that adaptation can boost model robustness against data corruption. Tuning only one block of parameters and freezing the remaining parameters can outperform full fine-tuning on a range of distribution shifts. Typically, fine-tuning the first block works best for input-level shifts such as CIFAR-C (image corruption). However, deeper networks may lose such attributes due to noises from quantization. Quantization deviates gradients and shallower layers suffer more gradient distortion.

# 4.2 DNN Adaptation for Output-Level Shift

RQ2: Adaptation performance under output-level shift for different DNN models. In this RQ, we study the effects of the adaptation CIFAR-Flip dataset on three different DNN models. The CIFAR-Flip dataset can be seen as an output-level shift because the only difference between CIFAR-10 and CIFAR-Flip is the flipped label (x → 9−x). Figure 6(b) presents the relative accuracy gain (i.e., blockwise adaptation accuracy — full adaptation accuracy) on the CIFAR-Flip dataset. We observe that fine-tuning partial blocks surpassed the full-tuning method regarding accuracy. Moreover, tuning the last layer works best for output-level shifts, and blocks closer to the loss function in the computation flow also suffer less from quantization error. The gap between last-block adaptation and other block fine-tuning will get smaller with more adaptation epochs. However, a higher number of adaptation epochs also indicates extra compute latency and energy overhead.

# 4.3 Unsupervised Partial Adaptation

RQ3: Adaptation performance under unsupervised learning tasks. A vast number of applications cannot enjoy the benefit of annotation and have to cope with a new working environment blindly, which prompts our experimentation on unsupervised adaptation on the distribution shift. We applied Shannon entropy as the unsupervised loss function [68]. Figure 5 demonstrates the performance of unsupervised adaptation on three DNN models. Interestingly, we found that for input-level shift, unsupervised adapting is effective and it even slightly surpassed supervised adaptation in more than 50% of our test cases. However, in output-level shifts, unsupervised adapting

![](images/66bdd6abbbc7ae8efb334effc87fadf12b04904a4e221bab071265ea8e32192e.jpg)  
Fig. 7. The computation flow of partial adaptation. The orange dashed line indicates the critical path during adapting, i.e., updating the block zero.

is hardly working. The testing accuracies are all below 20% under the same adaptation strategy. This is conceivable since Shannon entropy only depends on model prediction and possesses no knowledge of label shifting.

From the hardware perspective, unsupervised entropy minimization usually consists of exponential and logarithmic operations, whereas the adapted supervised loss function is the summed square error. The implementation of squaring and summation indicates that fewer resources are needed compared with the logarithmic and exponential unsupervised counterparts.

<table><tr><td>Takeaway #2</td></tr><tr><td>Unsupervised adaptation proved to be efficient when adapting to image corruption, which grants its feasibility for applications in which labels are impossible. In some cases, unsupervised adaptation even gains higher test accuracy compared with the supervised ones. As quantization error grows with backpropagation proceeding from deeper layers to shallow layers, it is conceivable that adapting deeper layers gives an optimal model when facing output-level shift.</td></tr></table>

# 4.4 Hardware Cost Estimation

RQ4: Hardware cost (compute latency and energy) under different adaptation strategies and DNN models. With the adaptation carried out on edge, compute latency and energy also play critical roles, together with task accuracy. Adapting different parts of the network would indicate different latency and energy costs. We conduct a hardware cost estimation corresponding to different adaptation strategies with our adaptation benchmarking framework.

In a single epoch, training — or adapting —can be segmented into three main sections: forward pass, backward pass, and weight update. One batch of training finishes as soon as all weights are updated. When adapting different blocks with different depths, the closer the block is to loss function in the computation flow, the less latency it will take. The flow is pictured in Figure 7. Since shallower layers show true dependency towards activation gradients from deeper layers, they will have to wait for deeper layers to have their activation gradient calculation finished, even if those layers are not meant to be adapted. Considering that adapting different blocks would give different accuracy gains, there is obviously a space for exploration to strike a balance between accuracy, latency, and energy consumption.

We demonstrate such trade-off with a quantized VGG8 network carried on CIM, as shown in Figure 9. The whole network is partitioned into four blocks, each consisting of two consecutive

![](images/8c1d916e8a15cace87b9e9297a1cab72f76f3a52ee529e25f4efac3df278f9cb.jpg)  
Fig. 8. Temporal operation distribution of a Layer 5 network that is partially adapting Layer 4 and Layer 2. As Layer 2 finishes the weight update later, $\tau _ { 2 }$ is deemed to be the adaptation latency.

![](images/6f94f6423207ae62a22d23aebf1fa2abbf7b8d9299748a0e12abe195cd586ebc.jpg)  
(a)

![](images/e998b863f339d85fcb914a07c18ad6a1245620833e6a57e26436bc7af3f29fad.jpg)  
(b)

![](images/1dab252a096b8bbea253efc3dc7455d11098d0fde1eaccda7b496cd3bd8c448d.jpg)  
(c)   
Fig. 9. (a) Latency estimation for different adaptation strategies (VGG8) utilizing different memory cells (SRAM/RRAM/Hybrid). (b) Energy cost regarding different adaptation strategies. (c) Energy breakdown and its relationship with weight sizes.

layers. Non-parameterized layers, such as maxpooling layers, are excluded. Given the number of layers as n, we derive the latency of partially adapting the $i ^ { t h }$ layer as (use τ as latency)

$$
\tau_ {\mathrm {a d a p t , i}} = \tau_ {\mathrm {F o r w a r d}} + \sum_ {t = i + 1} ^ {n} \tau_ {\mathrm {A c t i v a t i o n G r a d i e n t , t}} + \tau_ {\mathrm {w e i g h t g r a d i e n t , i}} + \tau_ {\mathrm {w e i g h t u p d a t e , i}}.
$$

If more than one layer is adapted, latency would be picked among the maximal adapt latency from all adapting layers. We provide the temporal graph of a 5-layer network adapting two layers to demonstrate latency definition (Figure 8). Here, we consider mostly dynamic energy since the summation of forward, weight gradient and activation gradient dynamic energy dominates energy consumption (>98%). The adaptation delay and energy consumption are given in Figure 9. Adapting the first block costs almost the same computational time as that of full adaptation, since the shallowest layer is very likely to be the critical path among all layers (if it is to be adapted). However, the bypassed weight gradient and weight update could save a large amount of dynamic energy as the calculation is omitted. In practice, a more energy-efficient system is possible through techniques such as applying power gating to the weight gradient unit while computing deeper layers’ activation gradient.

As the adapting block goes deeper, the latency decreases since less activation gradient is computed. Weight gradient computation is executed with an SRAM-based CIM module in the core. The gradient compute engine consists of multiple subarrays. It is initialized in a way that the subarray cluster can fit in the largest activation gradient across all layers. Such implementation has boosted weight gradient derivation. A large number of layers could be further accelerated through operand replication and parallel execution between subarrays. Consequently, weight gradient computation is hardly the critical path in adaptation. Energy consumption increases

![](images/ca117211738becb8b25b33d696b733ac6a66d18fe503265173ac354953262d7c.jpg)  
(a)

![](images/43ae17e745a3a19bd2aa3b51b9ab8d0b4688aed9830ebf6f4faf0235ea8adbb3.jpg)  
(b)   
Fig. 10. (a) Adaptation latency and energy of different adapting strategies on ResNet20 (RN20). (b) Energy breakdown and its relationship with weight parameter sizes.

with depth, which seems counterintuitive at first glance. A closer look into the energy breakdown provides clarity. Predominantly, the energy consumption stems from forward reading dynamic energy, activation gradient dynamic energy, and weight gradient dynamic energy. The trends in forward and activation dynamic energy consumption mirror those of latency, as their variations align precisely with the computation flow’s fluctuations. Yet, weight gradient dynamic energy relates directly to the number of weight parameters in the adapting layers. Essentially, layers with a larger set of trainable parameters demand more dynamic energy during weight gradient derivation. Figure 9(c) elucidates the correlation between the layer parameter size and weight gradient dynamic energy consumption. This observation underscores how pivotal the adaptation strategy is in determining the platform’s algorithmic efficiency, physical performance, and deployment factors. In scenarios in which accuracy is paramount, one might lean towards adapting shallower layers (subjected to input-level shifts), even if it implies a longer adaptation latency. Conversely, in situations in which minimizing latency is the priority, deeper layers may be chosen for adaptation. This choice, however, could come with the trade-offs of elevated energy consumption and diminished performance enhancements.

We also conduct a similar analysis on ResNet20, as shown in Figure 10. Latency declines when the adapting block goes deeper within the network. Energy consumption, however, is related to both block depth and the number of parameters in the adapting block. We chose the adapting unit of ResNet20 to be one basic block. The block with index 2 has the most weights whereas the last block (last FC layer) has the least. Though adapting the last block may not give the best accuracy recovery, it may still be an appealing option given the latency and energy benefit.

# Takeaway #3

Hardware adaptation cost (latency and energy) is related to adaptation strategy. Activation dynamic energy increases as the adapting block goes shallower, whereas weight gradient energy correlates to the size of trainable parameters. A balanced design should be struck based on network topology, CIM specification, and optimization budgets.

# 4.5 Hybrid Memory CIM Adaptation

RQ5: The effectiveness of adaptation based on SRAM/NVM hybrid–based CIM systems. This RQ prompts us to extend our adaptation benchmarking framework to encompass SRAM and NVM

hybrid–based CIM systems. The aim is to investigate the advantages of amalgamating various memory cells for enhancing system performance. NVMs generally show more compact area and superior reading characteristics while SRAM is better at writing. Additionally, SRAM is able to utilize more advanced tech nodes. NVMs, however, are typically a few generations behind, even if some of them are compatible with CMOS processes. From a dataflow perspective, SRAM-CIM is aligned with sequential readout, as the MAC operations are conducted in a row-wise manner. In contrast, mixed signal CIM, exemplified by RRAM, achieves high throughput by activating multiple word-lines simultaneously. This discrepancy in dataflow leads to the assembly of diversified peripherals within the array to support different workflows, resulting in varied performance estimation.

We first measured the latency and energy consumption of different adaptation schemes with full SRAM (14 nm) or RRAM configuration. The results are shown in Figure 9. An RRAM-based CIM macro is approximately 20.21% faster than an SRAM-based system. In addition, an SRAM-based CIM consumes 22.24% less energy than RRAM on average. Since only a portion of the network is adapted, we changed the adapting layers from an RRAM-based macro to an SRAM-based macro, forming a hybrid memory system. This means that only adapting layers are equipped with SRAM to boost writing. The full adaptation scheme is omitted since that would turn out to be a full SRAM-based system.

The performance of the hybrid system is shown in the histogram of Figure 9. Generally speaking, the hybrid CIM system shows intermediate latency and power consumption between pure RRAM and pure SRAM CIM systems. For example, if we use the hybrid memory system to adapt the block indexed 0, 21.2% of overall energy would be saved compared with a pure RRAM system. The energy saving comes at a price of a 24.6% latency increase (compared with full RRAM). For a design with more latency budget but tighter power constraints, swapping NVM with SRAM could be a potential solution. Moreover, as a charge-based system, SRAM is free from cell non-idealities of NVM cells. Concerns such as cells wearing out will never bother system performance. This could mean potentially higher accuracy gain in the long run.

From Figure 9, we can see that, when adapting the first or second block, the compute latency is even slightly better than that of a full RRAM system (0.96 s→0.95 s for 1st block, 0.81 s→0.78 s for 2nd block). This points to the fact that, even if latency is the only concerned parameter, there are still potential optimal points in the design space after introducing cell types as a new dimension.

One thing we noticed during our experiments is that, though we made assumptions for hybrid systems based on the writing properties of NVM/SRAM cells, weight update is not a dominant part concerning either latency or power consumption. This could be attributed to the workload picked as adaptation in which the learning rate is typically much smaller than training from scratch. A smaller learning rate results in smaller parameter gradients. With quantization, updates become even less critical since zero-quantized gradients imply omitted writing, as certain cells remain entirely untouched. In the core, the weight update cost is estimated by counting the amount of writing pulses applied to the subarrays, which is a number proportional to the amplitude of the weight gradient. As fine-tuning can imply a smaller number of write pulses compared with training, weight update is observed not to contribute the majority of adaptation overhead.

Another distinct advantage of NVMs is their compactness. In certain cases, an NVM cell might occupy an area smaller than $1 0 F ^ { 2 }$ , whereas a traditional SRAM cell can span nearly $1 5 0 F ^ { 2 }$ . Thus, a hybrid system could either opt for more NVM layers for compactness or SRAM for energy efficiency. We conducted area estimation upon the proposed hybrid system, shown in Figure 11. To summarize, when swapping the RRAM 1T1R crossbar array with the SRAM array to facilitate partial adaptation, the area overhead will be proportional to the number of tiles captured by the adapted block. Since block size expands as we proceed through shallow blocks to deeper blocks,

![](images/77b24bec82d40e42f3ba9a0a3678cb2fc647de309bfaa1595f1e0ae6023c0f68.jpg)  
Fig. 11. Hybrid CIM system area estimation under different adaptation schemes.

more SRAM tiles are required to carry weights, which leads to higher area overhead for the hybrid system.

<table><tr><td>Takeaway #4</td></tr><tr><td>Our proposed adaptation evaluation framework is adept at analyzing hybrid memory systems. We presented a hybrid CIM system, integrating RRAM and SRAM, achieving a balance in latency and energy. The hybrid CIM system introduces cell type as an additional layer-wise design variable.</td></tr></table>

# 4.6 Adapting NVM Non-ideality

RQ6: Adaptation on both environmental data shift and inherent hardware noise. In this RQ, we explore whether our proposed test-time DNN adaptation at edge with CIM is able to adapt the data distribution shift and inherent NVM device noise at the same time. Non-ideality associated with NVM devices, such as unpredictable cell-to-cell variation, IR-drop, and ON/OFF ratio degradation, have been a persistent issue for decades [10] and made models that are deployed on edge NVMbased systems suffer from algorithmic performance degradation.

With the proposed framework, for the first time, we find that such degradation caused by device imperfection could be amended by the test-time DNN adaptation along with the data distribution shift. As demonstrated in Figure 12, we evaluate the pre-trained models on the CIFAR-10-C dataset, and the endurance is simulated as a reduced on-off ratio, i.e., the ratio between the HRS and LRS [70]. We observe that with the on-off ratio being 80, the inference accuracy dropped roughly 3% for VGG8. When the on-off ratio further drops to 30, inference accuracy quickly goes down below 50%. Deeper networks appear to be more vulnerable to the damage of the on-off ratio as their inference accuracy drops severely to either of the on-off ratio values. In all cases, by applying 3 epochs of adaptation, we are able to adapt the network to a condition with better accuracy. Adaptation works for layers regardless of their depth. This shows that adaptation is not only capable of handling data corruption but also has model decay from non-ideality covered as well. Partial adaptation on VGG8, ResNet20, and DenseNet40 also consolidates this observation. Moreover, we observe that partial adaptation results in higher accuracy than full

![](images/cf9c7c882d16215659e7e134cb17a18a18b5cf3a036c7cdcb74c744eaf48c5e0.jpg)  
(a)

![](images/db6379b3f3c8f021e40071a8c2fcdd66a778b94574b2f075683359447bbc8a06.jpg)  
(b)   
Fig. 12. Accuracy for VGG8, ResNet20, and DenseNet40 with non-idealities (a) ON/OFF ratio = 30 and (b) ON/OFF ratio = 80.

adaptation. While training a hardware-aware model might seem advantageous, certain noise sources cannot be realistically accounted for during the training stage. However, our findings reveal that adapting a model aware of the on-off ratio on the CIFAR-10-C dataset results in an accuracy improvement of no more than 2% compared with a model unaware of the on-off ratio. This observation underscores the efficacy of test-time adaptation in simultaneously addressing both hardware and input noises. It suggests a potential inclination towards direct edge-based model adaptation, circumventing the need for additional training and pre-deployment profiling of CIM non-idealities. Considering that endurance could mean a reduced on-off ratio, adaptation may as well be a potential solution for defending against edge network conductance shift.

<table><tr><td>Takeaway #5</td></tr><tr><td>As device non-ideality exists with non-volatile CIM cells, it is destructive to model performance. For the first time, we demonstrate that test-time adaptation is beneficial to recovering model accuracy with the presence of non-ideality. Moreover, it is rather common that partial adaptation surpasses full adaptation in terms of test set accuracy.</td></tr></table>

# 4.7 Design Space Exploration

We conducted a set of experiments to show the discrepancy between different CIM macros carrying out different adaptation strategies. The result is demonstrated in Figure 13. We evaluate macros such as RRAM, SRAM based on 22-nm and 14-nm technologies, and a hybrid CIM system combining RRAM and 14-nm SRAM. These systems were analyzed during the adaptation of the VGG8 network on the CIFAR-10-C dataset over three epochs.

For the desired accuracy, we establish a threshold of at least 75%. Consequently, all adaptation schemes related to the 3rd block were eliminated. We further limit the timing constraint to under 2.85 s and set the energy consumption cap at 850 mJ. This filtering process narrowed down our options, leaving only a few viable candidates concentrated in the bottom-left quadrant of the figure.

As previously discussed in this section, the deeper the adapting block, the more likely the trend is towards reduced latency, increased energy consumption, and diminished accuracy gains. Hence, systems primarily concerned with latency tend to favor deeper adapting layers. Conversely, those

![](images/4b9258575849f12cbb8e8b0c3aeb4c30c4e68f6645b4dc6e6afb8a029925e043.jpg)  
Fig. 13. Design space exploration with different memories. Different shapes demonstrated different memory technologies. Colors to the right indicate full-tune, 0th block, 1st block, 2nd block, to 3rd block. Blue dashed lines indicate targeted performance. The dashed line elucidates the possible targeted performance constrained by energy and latency. The hollow shapes correspond to configurations with insufficient accuracy.

with energy efficiency as a priority typically lean towards adapting more superficial layers. For tasks that weigh both latency and energy as significant factors, a few configurations emerge as suitable. These include the RRAM adapting the 1st and 2nd blocks, the 14nm SRAM adapting the 3rd block, and the hybrid system adapting the 1st and 2nd blocks. These configurations are projected to be proficient for the task at hand.

# 5 ADAPTATION ON AUTONOMOUS SYSTEMS

In this section, we evaluate the proposed test-time adaptation with more complex UAV navigation problems in three-dimensional (3D) realistic environments and demonstrate the effectiveness of adaptation for real-time resource-constrained applications.

# 5.1 On-Device Adaptation in Autonomous Navigation Systems

Autonomous systems are becoming prevalent for Position-Navigation-Timing (PNT) applications [44]. To facilitate fully autonomous PNT, state-of-the-art UAVs are expected to run complex reinforcement learning (RL) models onboard with little-to-no offloading computation support [37, 66]. These UAVs often face constraints related to size, weight, and power (SWaP), making it crucial to balance energy efficiency with robustness and safety. A common strategy involves offline training of autonomy models in simulated environments followed by deployment for inference on edge devices. However, this can lead to performance issues due to differences between simulated training environments and actual deployment scenarios, necessitating on-device adaptations to enhance real-world performance within strict resource and latency limits.

Our approach champions a two-phase autonomous system learning paradigm that combines offline and online learning using fine-tuning adaptation. The key methodology is that if we train a model for an autonomous navigation task in a variety of environments collectively, we can leverage

![](images/9003d9eafdb1f94bac31e337b92752d4538770420856f688e8bd498830172474.jpg)  
Fig. 14. 3D realistic environments and their floor plans used in UAV autonomous navigation scenarios.

this knowledge using adaptation while training a smaller part of model for similar applications in a similar (but different/unseen) test environment.

In the offline phase, we train one autonomy network on a set of meta-environments using deep reinforcement learning [3]. These meta-environments serve as a library of environments for the underlying autonomous navigation problems. This offline training phase is carried out on highend workstations where we assume no strict restriction on the compute engine. Once we have effectively trained a network on the meta-environments collectively, we use these meta-weights as initialization during the online adaptation phase. In the online adaptation phase, a different test environment is used for adaptation (fine-tuning). The adaptation computations need to be carried out in the edge nodes with CIM architectures. In this phase, the adaptation is carried out on only a part of the network. The network is divided into non-adaptable and adaptable parts and only the weights of the adaptable parts are updated. The segmentation of the network is a compromise between the performance (obstacle avoidance) and the number of training computations.

# 5.2 Autonomous Navigation System Evaluation Results

Experimental Platform. We employ PEDRA [3], an open-source UAV simulation infrastructure, to test our adaptation methodology in autonomous systems. Powered by Unreal Engine, PEDRA creates realistic 3D environments. It uses AirSim to simulate the UAV’s dynamics and kinematics, and incorporates learning-based algorithms that generate real-time flight commands.

Task and Policy Model. In our experiments, the UAV starts at a predetermined point and is required to navigate through the hallways. There is no goal position and the UAV is required to fly avoiding the obstacles as long as it can [64]. The UAV captures RGB monocular images from its front-facing camera to determine its actions, which are processed through a reinforcement learning algorithm. Our model employs a perception-based probabilistic action space consisting of 25 possible actions [65]. A depth-based reward system encourages the UAV to avoid obstacles. The neural network, designed to predict action probabilities from sensory inputs, consists of three convolutional layers and two FC layers, shown in Figure 14. This network was trained across four diverse meta-environments: indoor-long, indoor-techno, outdoor-town, and outdoor-forest (Figure 15). During deployment, we assess the policy’s effectiveness by measuring the Mean Safe Flight (MSF), which is the average distance the UAV travels before encountering an obstacle, with longer distances indicating better performance.

Adaptation Performance. Adapting partial layers of the network improves the performance of UAV autonomous navigation tasks. As shown in Figure 16(a), after adaptation, the MSF achieved by the UAV surpasses the case achieved by the network initialized with meta-weights. Adapting Layer 1 achieves the highest MSF and it is observed that the performance of adapting partial layers surpasses the full fine-tuning.

![](images/d127621e1368969d02b08fb8e440abbbc8db639d31140ca2e810e3fa617a4877.jpg)  
Fig. 15. The five-layer autonomy neural network policy used to map environmental states to UAV action probabilities.

![](images/4e3749e99082e6ba8f0e95d383e0e43bb018f28958e5bba87ad726abeb8ac4a4.jpg)  
(a)

![](images/d28f35fe374b7a3302871406c2e3c6e4cc8969baba044e6260eb7e140d2fc697.jpg)  
(b)

![](images/662c0330dbb4721b154415f915395bb4c11434178daa211395e2739138da071a.jpg)  
  
Fig. 16. The UAV mean safe flight (MSF) distance, compute latency, and energy under various adaptation strategies.

Different adaptation strategies also present computational latency and energy trade-offs. As illustrated in Figure 16(b) and Figure 16(c), adapting Layer 2 to Layer 5 exhibits lower compute latency and energy compared with full model fine-tuning. Such computational efficiency directly influences the UAV’s safe flight speed and, by extension, its overall performance. Given a specific UAV speed, and accounting for the interval between successive frames and the UAV’s obstacle distance threshold, we can deduce the minimum Frames per Second (FPS) requisite for collision prevention. A swifter UAV mandates processing more frames within a fixed time span (demanding higher FPS). This pace is feasible only if the core computational system can handle the required FPS. Consequently, the system’s latency restricts the UAV’s maximum safe flight speed [36, 38]. Hence, the latency advancements from partial adaptation versus full fine-tuning in Figure 16 directly corresponds to an improvement of a maximum supported theoretical speed of about 1.73× from full fine-tuning to partial adaptation. For the same autonomous navigation task, the increased flight velocity results in faster task completion time (i.e., lower flight time), therefore consuming lower end-to-end flight energy since the majority of energy is consumed in rotors [11].

# 6 DISCUSSION

# 6.1 Pipelining Partial Adaptation

For pipelining to be effectively implemented, certain prerequisites must be met. Firstly, the process should be divisible into independent modules, akin to how neural networks are organized

![](images/4006ff5abbe46d772dc170f09c46acfaf5d4c828f13370b04deb33bafa4f295d.jpg)  
Fig. 17. Full adaptation is not compatible with pipelining due to read-after-write hazard. (FW: forward inference; BP: Backpropagation; Lx: Layer x)

![](images/f31d23e17b4484b82a9508327948a74aec2684587abee3f8e133301f3d4324dd.jpg)  
Fig. 18. Adaptation on last layer envision pipelining opportunities.

into layers. Secondly, operations on different inputs must remain independent to ensure accurate outcomes and prevent operational hazards. This setup aligns well with inference phases, in which network parameters are fixed following training, meeting the criteria for pipelining.

However, the situation shifts when it comes to training or tuning DNNs. Full parameter finetuning challenges the feasibility of pipelining, as initiating the next batch’s forward inference is contingent on completing the current batch’s weight updates, creating a read-after-write hazard. The possibility of pipelining during DNN tuning hinges on the specific tuning strategy employed. For example, tuning the initial block of a three-layer network closely resembles a full-tuning scenario, where pipelining is hindered due to direct data dependencies. Assuming that both forward and backward passes of a layer require a set time to complete, such processes, illustrated in Figure 17, show constraints indicated by arrows. If one forward and either a complete or partial backward propagation is considered a single instruction, with ‘time step’ equated to ‘cycle,’ the cycle-per-instruction (CPI) would be 6.

Adapting deeper layers presents a different scenario, suggesting that the initial layers remain unchanged during the adaptation. In a case in which only the last layer is tuned, the inference for the first two layers of the subsequent batch can commence before updating the third layer. This approach effectively masks the latency of the initial layers behind the latency of the previous batch’s forward-to-backward process.

With a sufficiently large batch size, the effective CPI could approximate 2. As tuning focuses on progressively shallower layers, the effective CPI trends towards 2L, with L representing the count of layers in reverse order from the last to the shallowest layer being tuned.

In summary, pipelining during partial network adaptations holds promise for enhancing efficiency. Nevertheless, the extent of throughput improvement achievable through pipelining is intricately linked to the selected tuning strategy, especially in managing the memory overhead for storing activations. Visualizations for three scenarios—highlighting whether the adapted layers are at the beginning or end of a three-layer network—demonstrate that pipelining is most beneficial in the latter case.

# 6.2 Future Work

We anticipate that future research can expand upon our work in four key dimensions, as follows.

— Algorithm level: The development and evaluation of additional models and test-time adaptation methods that demonstrate resilience against both environmental and model noise (the latter stemming from inherent hardware characteristics) represent a significant area for

![](images/23ba3a07896d91abf5cdd85c3c531a97cfa41ce86b6a181264632fbfbf649f91.jpg)  
Fig. 19. Comparing full adaptation, partial adaptation on the last layer, and partial adaptation on the last layer with pipelining. The latency and throughput benefits are visualized.

advancement. Our framework can act as a pivotal platform for assessing these algorithmic models’ efficacy and robustness.

— Architecture level: There is a compelling need to design efficient and reconfigurable CIM architectures that incorporate support for on-device test-time adaptation. Such architectures will be fundamental in enhancing the flexibility and performance of future CIM systems.   
— System level: The development of rapid and interpretable design space exploration strategies is critical for navigating the vast design possibilities. In conjunction with these strategies, constructing analytical models for adaptive CIM systems will facilitate swift, early-phase modeling. These endeavors are crucial for optimizing system design and ensuring that adaptive strategies are both effective and practical.   
— Technology level: Exploring and leveraging the performance and reliability characteristics of various memory technologies to create systems that deliver optimal end-to-end performance for specific applications is another essential avenue. This involves identifying and utilizing the strengths of different memory types to enhance overall system efficiency and reliability.

# 7 CONCLUSION

In this article, a cross-stack benchmarking framework is built and evaluated for test-time supervised and unsupervised DNN adaptation with CIM as the computing substrate. By adopting a software–hardware co-design scheme, this article presents a comprehensive analysis of the following. (i) with different combinations of memory technologies, the trade-off and bottleneck between algorithmic accuracy and hardware performance and efficiency; (ii) the impact of noise arising from the environment, including data shift and hardware such as intrinsic NVM noise; and (iii) the optimal hardware configuration under a given set of constraints. Our results conclude that adaptation is capable of recovering a CIM system from an environment overwhelmed with noise sources. The interaction between model topology, the essence of noise, adaptation choices, and the final hardware performance of the system are analyzed in detail. We also explored the possibility of adapting on autonomous systems with unsupervised adaptation. Finally, a CIM macro with multiple types of memory is evaluated and proved to be efficacious. In essence, this article showcases the robustness of our pre-silicon evaluation framework in the context of CIM adaptation.

# REFERENCES

[1] Tanner Andrulis, Joel S. Emer, and Vivienne Sze. 2024. CiMLoop: A flexible, accurate, and fast compute-in-memory modeling tool. arXiv preprint arXiv:2405.07259 (2024).   
[2] Alessio Antolini, Carmine Paolino, Francesco Zavalloni, Andrea Lico, Eleonora Franchi Scarselli, Mauro Mangia, Fabio Pareschi, Gianluca Setti, Riccardo Rovatti, Mattia Luigi Torres, et al. 2023. Combined HW/SW drift and variability mitigation for PCM-based analog in-memory computing for neural network applications. IEEE Journal on Emerging and Selected Topics in Circuits and Systems 13, 1 (2023), 395–407.   
[3] Aqeel Anwar and Arijit Raychowdhury. 2020. Autonomous navigation via deep reinforcement learning for resource constraint edge nodes using transfer learning. IEEE Access 8 (2020), 26549–26560.   
[4] Hamza Errahmouni Barkam, Sanggeon Yun, Paul R. Genssler, Zhuowen Zou, Che-Kai Liu, Hussam Amrouch, and Mohsen Imani. 2023. HDGIM: Hyperdimensional genome sequence matching on unreliable highly scaled FeFET. In 2023 Design, Automation & Test in Europe Conference & Exhibition (DATE). IEEE, 1–6.   
[5] Marco Bertuletti, Irene Muñoz-Martín, Stefano Bianchi, Andrea G. Bonfanti, and Daniele Ielmini. 2023. A multilayer neural accelerator with binary activations based on phase-change memory. IEEE Transactions on Electron Devices 70, 3 (2023), 986–992.   
[6] Kshitij Bhardwaj, James Diffenderfer, Bhavya Kailkhura, and Maya Gokhale. 2022. Benchmarking test-time unsupervised deep neural network adaptation on edge devices. In 2022 IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS). IEEE, 236–238.   
[7] Kshitij Bhardwaj, James Diffenderfer, Bhavya Kailkhura, and Maya Gokhale. 2022. Unsupervised test-time adaptation of deep neural networks at the edge: A case study. In 2022 Design, Automation & Test in Europe Conference & Exhibition (DATE). IEEE, 412–417.   
[8] Kshitij Bhardwaj and Maya Gokhale. 2021. Semi-supervised on-device neural network adaptation for remote and portable laser-induced breakdown spectroscopy. On-device Intelligence Workshop (MLSys Conference) (2021).   
[9] Kshitij Bhardwaj, Zishen Wan, Arijit Raychowdhury, and Ryan Goldhahn. 2023. Real-time fully unsupervised domain adaptation for lane detection in autonomous driving. In 2023 Design, Automation & Test in Europe Conference & Exhibition (DATE). IEEE, 1–2.   
[10] Abhiroop Bhattacharjee, Youngeun Kim, Abhishek Moitra, and Priyadarshini Panda. 2022. Examining the robustness of spiking neural networks on non-ideal memristive crossbars. In ISLPED: Proceedings of the ACM/IEEE International Symposium on Low Power Electronics and Design.   
[11] Behzad Boroujerdian, Hasan Genc, Srivatsan Krishnan, Bardienus Pieter Duisterhof, Brian Plancher, Kayvan Mansoorshahi, Marcelino Almeida, Wenzhi Cui, Aleksandra Faust, and Vijay Janapa Reddi. 2022. The role of compute in autonomous micro aerial vehicles: Optimizing for mission time and energy efficiency. ACM Transactions on Computer Systems (TOCS) 39, 1–4 (2022), 1–44.   
[12] Saikiran Bulusu, Bhavya Kailkhura, Bo Li, Pramod K. Varshney, and Dawn Song. 2020. Anomalous example detection in deep learning: A survey. IEEE Access 8 (2020), 132330–132347.   
[13] Indranil Chakraborty, Mustafa Fayez Ali, Dong Eun Kim, Aayush Ankit, and Kaushik Roy. 2020. GENIEx: A generalized approach to emulating non-ideality in memristive xbars using neural networks. In 2020 57th ACM/IEEE Design Automation Conference (DAC). IEEE, 1–6.   
[14] Muya Chang, Ashwin Sanjay Lele, Samuel D. Spetalnick, Brian Crafton, Shota Konno, Zishen Wan, Ashwin Bhat, Win-San Khwa, Yu-Der Chih, Meng-Fan Chang, et al. 2023. A 73.53 TOPS/W 14.74 TOPS heterogeneous RRAM inmemory and SRAM near-memory SoC for hybrid frame and event-based target tracking. In 2023 IEEE International Solid-State Circuits Conference (ISSCC). IEEE, 426–428.   
[15] Muya Chang, Samuel D Spetalnick, Brian Crafton, Win-San Khwa, Yu-Der Chih, Meng-Fan Chang, and Arijit Raychowdhury. 2022. A 40nm 60.64 TOPS/W ECC-capable compute-in-memory/digital 2.25 MB/768KB RRAM/SRAM system with embedded cortex M3 microprocessor for edge recommendation systems. In 2022 IEEE International Solid-State Circuits Conference (ISSCC), Vol. 65. IEEE, 1–3.   
[16] Jiasi Chen and Xukan Ran. 2019. Deep learning with edge computing: A review. Proc. IEEE 107 (2019), 1655–1674.   
[17] Pai-Yu Chen, Xiaochen Peng, and Shimeng Yu. 2017. NeuroSim+: An integrated device-to-algorithm framework for benchmarking synaptic devices and array architectures. In 2017 IEEE International Electron Devices Meeting (IEDM). IEEE, 6–1.   
[18] Jinwoo Choi, Gaurav Sharma, Manmohan Chandraker, and Jia-Bin Huang. 2020. Unsupervised and semi-supervised domain adaptation for action recognition from drones. In Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision. 1717–1726.   
[19] Brian Crafton, Zishen Wan, Samuel Spetalnick, Jong-Hyeok Yoon, Wei Wu, Carlos Tokunaga, Vivek De, and Arijit Raychowdhury. 2022. Improving compute in-memory ECC reliability with successive correction. In Proceedings of the 59th ACM/IEEE Design Automation Conference. 745–750.

[20] Edoardo Debenedetti, Zishen Wan, Maksym Andriushchenko, Vikash Sehwag, Kshitij Bhardwaj, and Bhavya Kailkhura. 2023. Scaling compute is not all you need for adversarial robustness. arXiv preprint arXiv:2312.13131 (2023).   
[21] Terrance DeVries and Graham W. Taylor. 2017. Improved regularization of convolutional neural networks with cutout. arXiv preprint arXiv:1708.04552 (2017).   
[22] James Diffenderfer, Brian R. Bartoldson, Shreya Chaganti, Jize Zhang, and Bhavya Kailkhura. 2021. A winning hand: Compressing deep networks can improve out-of-distribution robustness. arXiv preprint arXiv:2106.09129 (2021).   
[23] Manuel Le Gallo and Abu Sebastian. 2020. An overview of phase-change memory device physics. Journal of Physics D: Applied Physics (2020).   
[24] Ian J. Goodfellow, Jonathon Shlens, and Christian Szegedy. 2014. Explaining and harnessing adversarial examples. arXiv preprint arXiv:1412.6572 (2014).   
[25] Kang He, Indranil Chakraborty, Cheng Wang, and Kaushik Roy. 2022. Design space and memory technology coexploration for in-memory computing based machine learning accelerators. In Proceedings of the 41st IEEE/ACM International Conference on Computer-Aided Design. 1–9.   
[26] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. 2016. Deep residual learning for image recognition. In 2016 IEEE Conference on Computer Vision and Pattern Recognition.   
[27] Yufan He, Aaron Carass, Lianrui Zuo, Blake E. Dewey, and Jerry L. Prince. 2021. Autoencoder based self-supervised test-time adaptation for medical image analysis. Medical Image Analysis (2021), 102136.   
[28] Dan Hendrycks and Thomas Dietterich. 2019. Benchmarking neural network robustness to common corruptions and perturbations. In 2019 International Conference on Learning Representations.   
[29] Dan Hendrycks, Norman Mu, Ekin D. Cubuk, Barret Zoph, Justin Gilmer, and Balaji Lakshminarayanan. 2019. AugMix: A simple data processing method to improve robustness and uncertainty. arXiv preprint arXiv:1912.02781 (2019).   
[30] Gao Huang, Zhuang Liu, Laurens Van Der Maaten, and Kilian Q. Weinberger. 2017. Densely connected convolutional networks. In 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR).   
[31] Daniele Ielmini. 2011. Modeling the universal set/reset characteristics of bipolar RRAM by field- and temperaturedriven filament growth. IEEE Transactions on Electron Devices (2011), 4309–4317.   
[32] Shubham Jain, Abhronil Sengupta, Kaushik Roy, and Anand Raghunathan. 2020. RxNN: A framework for evaluating deep neural networks on resistive crossbars. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems 40, 2 (2020), 326–338.   
[33] Zizhen Jiang, Yi Wu, Shimeng Yu, Lin Yang, Kay Song, Zia Karim, and H.-S. Philip Wong. 2016. A compact model for metal–oxide resistive random access memory with experiment verification. IEEE Transactions on Electron Devices 63, 5 (2016).   
[34] Geethan Karunaratne, Manuel Le Gallo, Giovanni Cherubini, Luca Benini, Abbas Rahimi, and Abu Sebastian. 2020. In-memory hyperdimensional computing. Nature Electronics 3, 6 (2020), 327–337.   
[35] Klim Kireev, Maksym Andriushchenko, and Nicolas Flammarion. 2022. On the effectiveness of adversarial training against common corruptions. In Uncertainty in Artificial Intelligence. PMLR, 1012–1021.   
[36] Srivatsan Krishnan, Zishen Wan, Kshitij Bhardwaj, Ninad Jadhav, Aleksandra Faust, and Vijay Janapa Reddi. 2022. Roofline model for UAVs: A bottleneck analysis tool for onboard compute characterization of autonomous unmanned aerial vehicles. In 2022 IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS). IEEE, 162–174.   
[37] Srivatsan Krishnan, Zishen Wan, Kshitij Bhardwaj, Paul Whatmough, Aleksandra Faust, Sabrina Neuman, Gu-Yeon Wei, David Brooks, and Vijay Janapa Reddi. 2022. Automatic domain-specific SoC design for autonomous unmanned aerial vehicles. In 2022 55th IEEE/ACM International Symposium on Microarchitecture (MICRO). IEEE, 300–317.   
[38] Srivatsan Krishnan, Zishen Wan, Kshitij Bhardwaj, Paul Whatmough, Aleksandra Faust, Gu-Yeon Wei, David Brooks, and Vijay Janapa Reddi. 2020. The sky is not the limit: A visual performance model for cyber-physical co-design in autonomous machines. IEEE Computer Architecture Letters 19, 1 (2020), 38–42.   
[39] Yoonho Lee, Annie S. Chen, Fahim Tajwar, Ananya Kumar, Huaxiu Yao, Percy Liang, and Chelsea Finn. 2023. Surgical fine-tuning improves adaptation to distribution shifts. International Conference on Learning Representations (ICLR) (2023).   
[40] Daniele Ielmini and Philip Wong. 2018. In-memory computing with resistive switching devices. Computing with Resistive Switching Devices (2018), 333–343.   
[41] Daniele Ielmini and Yuegang Zhang. 2007. Analytical model for subthreshold conduction and threshold switching in chalcogenide-based memory devices. Journal of Applied Physisc (2007).   
[42] Mengyuan Li, Arman Kazemi, Ann Franchesca Laguna, and X. Sharon Hu. 2022. Associative memory based experience replay for deep reinforcement learning. In Proceedings of the 41st IEEE/ACM International Conference on Computer-Aided Design. 1–9.   
[43] Che-Kai Liu, Haobang Chen, Mohsen Imani, Kai Ni, Arman Kazemi, Ann Franchesca Laguna, Michael Niemier, Xiaobo Sharon Hu, Liang Zhao, Cheng Zhuo, et al. 2022. COSIME: FeFED based associative memory for in-memory cosine similarity search. In Proceedings of the 41st IEEE/ACM International Conference on Computer-Aided Design. 1–9.

[44] Shaoshan Liu, Zishen Wan, Bo Yu, and Yu Wang. 2021. Robotic Computing on FPGAs. Springer.   
[45] Anni Lu, Xiaochen Peng, Wantong Li, Hongwu Jiang, and Shimeng Yu. 2021. NeuroSim validation with 40nm RRAM compute-in-memory macro. In 2021 IEEE 3rd International Conference on Artificial Intelligence Circuits and Systems (AICAS).   
[46] Anni Lu, Xiaochen Peng, Wantong Li, Hongwu Jiang, and Shimeng Yu. 2021. NeuroSim validation with 40nm RRAM compute-in-memory macro. In 2021 IEEE 3rd International Conference on Artificial Intelligence Circuits and Systems (AICAS). IEEE, 1–4.   
[47] Phil Meier, Kris Rohrmann, Marvin Sandner, and Marcus Prochaska. 2020. Transfer learning for neuronal networks deployed on the sensors edge. In 2020 IEEE Sensors. IEEE, 1–4.   
[48] Abhishek Moitra, Abhiroop Bhattacharjee, Runcong Kuang, Gokul Krishnan, Yu Cao, and Priyadarshini Panda. 2023. SpikeSim: An end-to-end compute-in-memory hardware evaluation tool for benchmarking spiking neural networks. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2023).   
[49] Zachary Nado, Shreyas Padhy, D. Sculley, Alexander D’Amour, Balaji Lakshminarayanan, and Jasper Snoek. 2020. Evaluating prediction-time batch normalization for robustness under covariate shift. arXiv preprint arXiv:2006.10963 (2020).   
[50] Xiaochen Peng, Shanshi Huang, Hongwu Jiang, Anni Lu, and Shimeng Yu. 2020. DNN+NeuroSim V2.0: An end-to-end benchmarking framework for compute-in-memory accelerators for on-chip training. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems 40, 11 (2020), 2306–2319.   
[51] Xiaochen Peng, Shanshi Huang, Yandong Luo, Xiaoyu Sun, and Shimeng Yu. 2019. DNN+NeuroSim: An end-to-end benchmarking framework for compute-in-memory accelerators with versatile device technologies. In 2019 IEEE International Electron Devices Meeting (IEDM). IEEE, 32–5.   
[52] Xiaochen Peng, Rui Liu, and Shimeng Yu. 2019. Optimizing weight mapping and data flow for convolutional neural networks on RRAM based processing-in-memory architecture. In 2019 IEEE International Symposium on Circuits and Systems (ISCAS).   
[53] Lillian Pentecost, Alexander Hankin, Marco Donato, Mark Hempstead, Gu-Yeon Wei, and David Brooks. 2021. NVMExplorer: A framework for cross-stack comparisons of embedded non-volatile memories. arXiv preprint arXiv:2109.01188 (2021).   
[54] Brandon Reagen, Udit Gupta, Lillian Pentecost, Paul Whatmough, Sae Kyu Lee, Niamh Mulholland, David Brooks, and Gu-Yeon Wei. 2018. Ares: A framework for quantifying the resilience of deep neural networks. In 2018 55th ACM/ESDA/IEEE Design Automation Conference (DAC).   
[55] Dayane Reis, Di Gao, Shaahin Angizi, Xunzhao Yin, Deliang Fan, Michael Niemier, Cheng Zhuo, and X. Sharon Hu. 2020. Modeling and benchmarking computing-in-memory for design space exploration. In Proceedings of the 2020 Great Lakes Symposium on VLSI. 39–44.   
[56] Elan Rosenfeld, Pradeep Ravikumar, and Andrej Risteski. 2022. Domain-adjusted regression or: ERM may already learn features sufficient for out-of-distribution generalization. arXiv preprint arXiv:2202.06856 (2022).   
[57] Kaushik Roy, Akhilesh Jaiswal, and Priyadarshini Panda. 2019. Towards spike-based machine intelligence with neuromorphic computing. Nature 575, 7784 (2019), 607–617.   
[58] Steffen Schneider, Evgenia Rusak, Luisa Eck, Oliver Bringmann, Wieland Brendel, and Matthias Bethge. 2020. Improving robustness against common corruptions by covariate shift adaptation. Advances in Neural Information Processing Systems 33 (2020).   
[59] Abu Sebastian, Manuel Le Gallo, Riduan Khaddam-Aljameh, and Evangelos Eleftheriou. 2020. Memory devices and applications for in-memory computing. Nature Nanotechnology 15, 7 (2020), 529–544.   
[60] Ali Shafiee, Anirban Nag, Naveen Muralimanohar, Rajeev Balasubramonian, John Paul Strachan, Miao Hu, R. Stanley Williams, and Vivek Srikumar. 2016. ISAAC: A convolutional neural network accelerator with in-situ analog arithmetic in crossbars. ACM SIGARCH Computer Architecture News 44, 3 (2016), 14–26.   
[61] Shengxi Shou, Che-Kai Liu, Sanggeon Yun, Zishen Wan, Kai Ni, Mohsen Imani, X. Sharon Hu, Jianyi Yang, Cheng Zhuo, and Xunzhao Yin. 2023. SEE-MCAM: Scalable multi-bit FeFET content addressable memories for energy efficient associative search. In 2023 IEEE/ACM International Conference on Computer Aided Design (ICCAD). IEEE, 1–9.   
[62] Samuel D. Spetalnick, Muya Chang, Brian Crafton, Win-San Khwa, Yu-Der Chih, Meng-Fan Chang, and Arijit Raychowdhury. 2022. A 40nm 64kb 26.56TOPS/W 2.37 Mb/mm2 RRAM binary/compute-in-memory macro with 4.23x improvement in density and  75% use of sensing dynamic range. In 2022 IEEE International Solid-State Circuits Con->ference (ISSCC), Vol. 65. IEEE, 1–3.   
[63] Nicola Strisciuglio, Manuel Lopez-Antequera, and Nicolai Petkov. 2020. Enhanced robustness of convolutional networks with a push–pull inhibition layer. Neural Computing and Applications 32 (2020), 17957–17971.   
[64] Zishen Wan, Aqeel Anwar, Yu-Shun Hsiao, Tianyu Jia, Vijay Janapa Reddi, and Arijit Raychowdhury. 2021. Analyzing and improving fault tolerance of learning-based navigation systems. In 2021 58th ACM/IEEE Design Automation Conference (DAC). IEEE, 841–846.

[65] Zishen Wan, Nandhini Chandramoorthy, Karthik Swaminathan, Pin-Yu Chen, Kshitij Bhardwaj, Vijay Janapa Reddi, and Arijit Raychowdhury. 2024. MulBERRY: Enabling bit-error robustness for energy-efficient multi-agent autonomous systems. In Proceedings of the 29th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 2. 746–762.   
[66] Zishen Wan, Nandhini Chandramoorthy, Karthik Swaminathan, Pin-Yu Chen, Vijay Janapa Reddi, and Arijit Raychowdhury. 2023. BERRY: Bit error robustness for energy-efficient reinforcement learning-based autonomous systems. In 2023 60th ACM/IEEE Design Automation Conference (DAC). IEEE, 1–6.   
[67] Zishen Wan, Brian Crafton, Samuel Spetalnick, Jong-Hyeok Yoon, and Arijit Raychowdhury. 2022. RRAM-ECC: Improving reliability of RRAM-based compute in-memory. In 13th Annual Non-Volatile Memories Workshop (NVMW).   
[68] Dequan Wang, Evan Shelhamer, Shaoteng Liu, Bruno Olshausen, and Trevor Darrell. 2021. Tent: Fully test-time adaptation by entropy minimization. In International Conference on Learning Representations (ICLR). https://openreview. net/forum?id=uXl3bZLkr3c   
[69] Garrett Wilson and Diane J. Cook. 2020. A survey of unsupervised deep domain adaptation. ACM Transactions on Intelligent Systems and Technology (TIST) 11, 5 (2020), 1–46.   
[70] H.-S. Philip Wong, Heng-Yuan Lee, Shimeng Yu, Yu-Sheng Chen, Yi Wu, Pang-Shiu Chen, Byoungil Lee, Frederick T. Chen, and Ming-Jinn Tsai. 2012. Metal–oxide RRAM. Proc. IEEE 100, 6 (2012), 1951–1970.   
[71] Shuang Wu, Guoqi Li, Feng Chen, and Luping Shi. 2018. Training and inference with integers in deep neural networks. International Conference on Learning Representations (2018).   
[72] Xiaochen Peng, Shanshi Huang. 2020. User Manual of DNN+NeuroSim framework 2.0. Retrieved from https://github. com/neurosim/DNN_NeuroSim_V2.1/blob/master/Documents/DNN%20NeuroSim%20V2.1%20User%20Manual.pdf   
[73] Sangdoo Yun, Dongyoon Han, Seong Joon Oh, Sanghyuk Chun, Junsuk Choe, and Youngjoon Yoo. 2019. CutMix: Regularization strategy to train strong classifiers with localizable features. In Proceedings of the IEEE/CVF International Conference on Computer Vision. 6023–6032.   
[74] Peiying Zhang, Hao Sun, Jingyi Situ, Chunxiao Jiang, and Dongliang Xie. 2021. Federated transfer learning for IIoT devices with low computing power based on blockchain and edge computing. IEEE Access (2021).   
[75] Zhuowen Zou, Hanning Chen, Prathyush Poduval, Yeseong Kim, Mahdi Imani, Elaheh Sadredini, Rosario Cammarota, and Mohsen Imani. 2022. BioHD: An efficient genome sequence search platform using hyperdimensional memorization. In Proceedings of the 49th Annual International Symposium on Computer Architecture. 656–669.

Received 24 September 2023; revised 29 March 2024; accepted 2 May 2024