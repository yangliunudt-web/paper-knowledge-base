---
title: "Hybrid neural networks for continual learning inspired by corticohippocampal circuits"
authors:
  - "Qianqian Shi"
  - "Faqiang Liu"
  - "Hongyi Li"
  - "Guangyu Li"
  - "Luping Shi"
  - "Rong Zhao"
date: "2025-02-02"
year: "2025"
journal: "Nature Communications"
abstract: "Current artificial systems suffer from catastrophic forgetting during continual learning, a limitation absent in biological systems. Biological mechanisms leverage the dual representation of specific and generalized memories within corticohippocampal circuits to facilitate lifelong learning. Inspired by this, we develop a corticohippocampal circuits-based hybrid neural network (CH-HNN) that emulates these dual representations, significantly mitigating catastrophic forgetting in both task-incremental and class-incremental learning scenarios. Our CH-HNNs incorporate artificial neural networks and spiking neural networks, leveraging prior knowledge to facilitate new concept learning through episode inference, and offering insights into the neural functions of both feedforward and feedback loops within corticohippocampal circuits. Crucially, CH-HNN operates as a task-agnostic system without increasing memory demands, demonstrating adaptability and robustness in real-world applications. Coupled with the low power consumption inherent to SNNs, our model represents the potential for energy-efficient, continual learning in dynamic environments."
abstract_cn: "持续学习仍然是人工神经网络面临的根本挑战。本文开发了一种基于皮质-海马回路启发的混合神经网络（CH-HNN），模拟大脑中特定记忆和泛化记忆的双重表征。ANN模拟mPFC-CA1回路在跨事件抽象规律中的作用，而SNN模拟DG-CA3回路编码特定事件记忆。该模型在多个数据集上的任务增量和类别增量学习场景中均展示了强大性能。它结合元可塑性机制，随着知识积累动态调节突触学习率。SNN组件实现低功耗，适用于神经形态硬件部署。"
keywords:
  - "[[Continual Learning]]"
  - "[[Corticohippocampal Circuits]]"
  - "[[Metaplasticity]]"
  - "[[Hybrid Neural Network]]"
  - "[[SNN]]"
  - "[[持续学习]]"
  - "[[元可塑性]]"
  - "[[混合神经网络]]"
cite: "[1] Shi et al. Hybrid neural networks for continual learning inspired by corticohippocampal circuits[J]. Nature Communications, 2025."
aiSum: "CH-HNN混合神经网络模型，模拟皮质-海马回路的双重记忆表征。ANN+SNN混合架构，结合元可塑性机制动态调节学习率。在任务增量和类别增量学习场景中表现优异，SNN组件支持低功耗神经形态硬件部署。"
confidence: "high"
wiki_concepts:
  - "[[Continual learning]]"
  - "[[Neural network]]"
---

# Hybrid neural networks for continual learning inspired by corticohippocampal circuits

Received: 30 April 2024

Accepted: 16 January 2025

Published online: 02 February 2025

Check for updates

Qianqian Shi $^{1,2,3,4,5,6}$ , Faqiang Liu $^{1,2,3,4,5,6}$ , Hongyi Li $^{1,2,3,4,5}$ , Guangyu Li $^{1}$ , Luping Shi $^{1,2,3,4,5}$ & Rong Zhao $^{1,2,3,4,5}$

Current artificial systems suffer from catastrophic forgetting during continual learning, a limitation absent in biological systems. Biological mechanisms leverage the dual representation of specific and generalized memories within corticohippocampal circuits to facilitate lifelong learning. Inspired by this, we develop a corticohippocampal circuits-based hybrid neural network (CH-HNN) that emulates these dual representations, significantly mitigating catastrophic forgetting in both task-incremental and class-incremental learning scenarios. Our CH-HNNs incorporate artificial neural networks and spiking neural networks, leveraging prior knowledge to facilitate new concept learning through episode inference, and offering insights into the neural functions of both feedforward and feedback loops within corticohippocampal circuits. Crucially, CH-HNN operates as a task-agnostic system without increasing memory demands, demonstrating adaptability and robustness in real-world applications. Coupled with the low power consumption inherent to SNNs, our model represents the potential for energy-efficient, continual learning in dynamic environments.

In recent years, artificial intelligence (AI) has achieved remarkable advances, becoming integral to our daily lives, especially with the development of the generative pre-trained transformer<sup>1</sup>. However, current AI systems still rely on training with entire datasets at once, lacking the ability to incrementally add new data without disrupting the existing model. This limitation presents challenges of catastrophic forgetting in environments that require incremental learning from temporally ordered data. To mitigate this issue, adaptive learning strategies known as continual learning or lifelong learning have garnered increasing attention in research. Despite significant advancements, current methods face persistent challenges, including the need for explicit task identification during inference and the increasing memory demands associated with storing samples or features from previous tasks or classes. These limitations significantly hinder the

practical application of continual learning in dynamic, real-world environments. Consequently, the development of task-agnostic approaches to enhance the practical implementation of continual learning in real-world scenarios remains a critical area of research.

In contrast, biological systems demonstrate exceptional efficiency in incremental learning with low energy consumption, underscoring the potential for brain-inspired algorithms to enhance the continual learning capabilities of AI by emulating the neural mechanisms underlying lifelong learning.

Neuroscientific research has revealed that corticohippocampal circuits play a critical role in the efficacy of episodic learning and generalization, which are fundamental for lifelong learning. Specifically, the medial prefrontal cortex $(\mathrm{mPFC})^2$ and the $\mathrm{CA1}^3$ region of the hippocampus (HPC) are thought to represent regularities across

<sup>1</sup>Center for Brain-Inspired Computing Research (CBICR), Tsinghua University, Beijing, China. <sup>2</sup>Department of Precision Instruments, Tsinghua University, Beijing, China. <sup>3</sup>IDG/McGovern Institute for Brain Research, Tsinghua University, Beijing, China. <sup>4</sup>Tsinghua University- China Electronics Technology HK Group Co. Joint Research Center for Brian-inspired Computing, Tsinghua University, Beijing, China. <sup>5</sup>Optical Memory National Engineering Research Center, Tsinghua University, Beijing, China. <sup>6</sup>These authors contributed equally: Qianqian Shi, Faqiang Liu. <sup>e</sup>e-mail: r_zhao@mail.tsinghua.edu.cn

related episodes, responding to correlated episodes encountered previously. While regions like the dentate gyrus (DG) and CA3 within the HPC are believed to encode specific memories, selectively responding to particular episodes. Together, these interconnected brain regions form a recurrent loop between the mPFC and HPC, hypothesized to drive the integration of episodic information, facilitating both generalization across episodes and the learning of new concepts.

Within this loop, the mPFC-CA1 circuits transmit high-order information derived from prior episodes to modulate novel learning in the DG-CA3 circuits, which subsequently relays newly formed associative memories back to the mPFC-CA1 circuits, thus enhancing the encoding of episode-related regularities<sup>4</sup>, as depicted in Fig. 1.

In this study, we emulate the dual representation of cortico-hippocampal recurrent loops and develop a hybrid neural network, termed CH-HNN, for artificial systems. CH-HNN provides a task-agnostic approach to reduce memory overhead and enhance the practical application of continual learning in real-world scenarios. By integrating artificial neural networks (ANNs) and spiking neural networks (SNNs), we replicate the complementary roles of specific and generalized memory representations within these circuits. ANNs, extensively developed in computer vision, excel at processing high spatial complexity and abstracting image regularities<sup>5,6</sup>, analogous to the role of mPFC-CA1 circuits that integrate regularities across episodes. In contrast, SNNs, with sparse firing rates and consequently low power consumption<sup>7</sup>, are used to incrementally encode new concepts, simulating the function of DG-CA1 circuits in specific episode memory formation, as illustrated in Fig. 2a. The regularities abstracted by the ANNs are designed to guide the SNNs to incrementally learn novel concepts via episode inference. CH-HNN overcomes traditional challenge of integrating these distinct network types and reveals new insights into their synergistic potential.

Additionally, we incorporate metaplasticity mechanisms $^{8,9}$ into the CH-HNN to simulate the dynamic changes in synaptic learning ability as knowledge accumulates. Specifically, episode-related

regularities are believed to have side effects, which could increase the incidence of false alarms when recognizing highly similar episodes in the brain $^{10}$ . To mitigate this, the interaction between the lateral parietal cortex (LPC) and DG-CA3 circuits, which encode specific memories, is thought to play a crucial role in reducing such errors $^{11}$ . Inspired by this, our model hypothesizes that the LPC modulates the metaplasticity of DG-CA3 circuits by preserving synaptic weights across similar episodes.

To evaluate the effectiveness of CH-HNN in continual learning, we applied it to the split MNIST (sMNIST), permuted MNIST (pMNIST) $^{12}$ , and split CIFAR-100 $^{13}$ (sCIFAR-100) in task-incremental scenarios, as well as the sMNIST, sCIFAR-100, split Tiny-ImageNet $^{14}$ (sTiny-ImageNet), and split DVS Gesture datasets $^{15}$ in class-incremental scenarios. Compared to alternative methods, CH-HNN demonstrates superior performance and achieves a more favorable balance between plasticity (the capacity to learn new information) and stability (the ability to retain previously acquired knowledge), a critical duality in the field of continual learning $^{16}$ . Furthermore, CH-HNN demonstrates the ability to transfer related-episode information across various datasets, highlighting its capacity for effective knowledge transfer in diverse scenarios.

To investigate the role of the feedback loop from DG-CA3 to mPFC-CA1 in facilitating the encoding of episode-related information, we implemented an incremental learning framework for the ANN within CH-HNN instead of an offline learning approach. The results indicate that as the ANN incrementally accumulates knowledge over time, its proficiency in encoding related-episode regularities significantly improves. These findings suggest that this feedback loop plays a crucial role in promoting episodic generalization by relaying novel embedding.

Aligned with our goal of enhancing continual learning in real-world scenarios, CH-HNN demonstrates strong adaptability and robustness across diverse applications. When implemented on neuromorphic hardware, the integration of SNNs significantly reduces power consumption, highlighting the model's potential for energy-efficient deployment in dynamic environments.

![](images/0c9c84dc19d58cf13cb0db7d68520d245f4330aade9e53eaf24265e245cc2b98.jpg)  
a   
Fig. 1 | Widespread corticohippocampal circuits: facilitating and characterizing dual representation for episode learning and generalization. a schematic diagrams illustrating the brain areas involved in episode learning and generalization. The mPFC interact with CA1 or the anterior hippocampus to represent episode-related regularities, as indicated by the area enclosed by a pink dashed

![](images/5f5e8ac46dbf4c31a161bb83dbbf057d6ace096258b13349581c3c87dcdf9091.jpg)  
b   
line. The interaction between DG and CA3 within hippocampus represents the specific memories, highlighted by an area enclosed by a green dashed line. b A concise schematic depicting the relationship between the DG-CA3 circuits and mPFC-CA1 circuits.

![](images/7345e0345e165124757e10d681cb0d8db17ff2ea56e52ad8e1df3038285ed7f1.jpg)  
a   
Fig. 2 | Hybrid neural networks based on corticohippocampus circuits and metaplasticity mechanisms. a The hybrid neural network comprises an ANN (depicted in pink) and a SNN (depicted in green). The ANN is trained on the similarities among image samples to generate episode-related regularities for each task, which modulate the SNN. The SNN is tailored to learn sequential specific tasks, thereby generating specific memories. b The learning process within the SNN is modulated by metaplasticity mechanism. Large synaptic spines, depicted in green,

In summary, the CH-HNN, inspired by corticohippocampal recurrent loops in the brain, effectively mitigates catastrophic forgetting in both task-incremental and class-incremental scenarios. It demonstrates robustness in real-world applications and shows potential for future implementation into neuromorphic hardware. Furthermore, our study provides evidence that enhances the understanding of the neural mechanisms underlying corticohippocampal functions, contributing to a deeper understanding of lifelong learning from a computational neuroscience perspective.

# Results

# Corticohippocampal recurrent loops for episode learning and generalization

Recent research increasingly supports the view that the brain does not represent concepts solely through individual engrams during continuous episodic learning $^{3,4,17}$ . Instead, the brain processes episodic information at multiple levels of specificity, enabling the formation of both generalized knowledge across related episodes and the retention of specific episodic details $^{18}$ . The complementary learning systems theory offers an explanation for the distinct yet complementary roles of the cortex and hippocampus in memory processing $^{19}$ . In this framework, the cortex, particularly the mPFC $^{18,20}$ and the enhorital cortex (EC) $^{21}$ , is implicated in representing generalized regularities across related experiences—a process referred to as memory integration. This generalized information is subsequently conveyed through the medial temporal lobe (MTL) $^{2,22}$ to the hippocampus. Within the hippocampus,

have stored substantial amounts of memory and learn at a slower rate in subsequent learning. Small synaptic spines, colored in pink, store less memories and are capable of learning additional knowledge. The size of synaptic spines varies across different episodes. c The impact of metaplasticity mechanism on learning dynamics across different spine sizes, illustrating the decline in learning capability as the absolute value of neural weights increases.

the CA1 region is thought to mediate interactions between these cortical areas and hippocampal subregions responsible for specific memory representations, such as the DG and CA3. These neural pathways are believed to facilitate the transfer of generalized information, thereby enhancing the learning of new, related concepts[23].

To streamline the process of memory integration and specific memory learning, we simplify the neural pathways representing generalized episodic information—likely involving the mPFC, MTL, EC, and CA1 regions—into a direct mPFC-CA1 pathway (depicted in pink in Fig. 1b). Concurrently, the circuits associated with specific memory representations within the hippocampus are refined to focus on the DG-CA3 pathways (shown in green in Fig. 1b). This refinement results in a recurrent loop, wherein the mPFC-CA1 pathway facilitates the efficient acquisition of novel, specific memories in the DG-CA3 pathways. In turn, the DG-CA3 circuits transfer these newly embedded memories back to the mPFC-CA1 circuits, thereby promoting the integration of related memories<sup>4</sup>. We anticipate that these simplified neural mechanisms underlying continual memory learning could inspire novel computational strategies to enhance continual learning in artificial systems.

# Hybrid neural networks designed to emulate corticohippocampal recurrent loop

Based on the corticohippocampal recurrent loop, we designed a hybrid model to simulate the bidirectional facilitation between the mPFC-CA1 and DG-CA3 circuits.

To emulate the function of memory integration in the mPFC-CA1 circuits, we leveraged the ANN's proficiency in processing high spatial complexity[6,7,24] and developed an ANN that learns the similarities among different episodes or concepts, generating a modulation signal aimed at facilitating the learning of new episodes or concepts. Specifically, the modulation signals generated by the ANN are constrained to reflect the similarity between coarse-grained input features from different tasks or classes, with the goal of guiding new concept learning.

To simulate the function of novel learning in the DG-CA3 circuits, we utilize SNNs due to their sparse firing rates and consequently lower power consumption $^{7,24}$ , enabling them to learn new concepts associated with tasks or classes.

During the learning process, ANNs generate modulation signals in response to each visual input. These modulation signals serve as masks, selectively activating neurons in the hidden layers of the SNNs and thereby altering the neural synchrony state across different episodes, as illustrated in Fig. 2a. Therefore, the modulation signals vary significantly with dissimilar inputs, enabling the automatic partitioning of SNNs into distinct sub-networks under the guidance of the ANNs. As a result, the ANNs take on the role of episode inference, assisting the SNNs in selecting episode-related neurons for each task or class. This design enhances resource utilization within the SNNs, reduces interference between different episodes, and thereby improves overall learning efficiency.

Notably, the ANNs within CH-HNN can be trained offline or over longer time scales than SNNs, aligning with the neural mechanisms underlying the slower formation of regularities in the mPFC-CA1 circuits during processes such as sleep or gradual learning[25,26].

# Introduce metaplasticity mechanism to CH-HNN

In the corticohippocampal loops, research indicates that the modulation signals from the mPFC-CA1 circuit may lead to an increase in false alarms among episodes with high similarity $^{10,27,28}$ , potentially due to the highly similar neural synchrony in downstream circuits. To counteract this hypothesis and enhance the performance of our hybrid neural networks, we introduce a metaplasticity mechanism $^{8}$ , which allows synapses to exhibit variable learning capabilities. Typically, metaplasticity at each synapse is modulated by chemical neuromodulatory signals, such as dopamine and serotonin $^{9}$ , which can manifest as changes in the size of synaptic spines, as illustrated in Fig. 2b. In this study, we propose that the LPC $^{11}$ , particularly the angular gyrus (ANG), and the lateral prefrontal cortex (IPFC) $^{29}$ , which are involved in representing recalled content-specific memories, may play a role in modulating synaptic metaplasticity in the DG-CA3 circuit (Fig. 1a).

To implement the metaplasticity mechanism in SNNs, we adopt an exponential meta-function, as proposed in $^{30}$ , to simulate plasticity dynamics of biological synapses. As synaptic weights increase in magnitude, the meta-function output decreases from 1 to 0, as illustrated in Fig. 2c. Integrating the meta-function into the optimization process during SNN training gradually diminishes each synapse's learning capacity as knowledge accumulates (details in Methods). This approach has proven effective in alleviating catastrophic forgetting in binary neural networks $^{31}$ and SNNs $^{9,30}$ .

Thus far, we have outlined the development of the CH-HNN framework. Moving forward, we will assess its performance and adaptability across both task-incremental and class-incremental learning scenarios using a range of datasets.

# CH-HNN demonstrates superior performance in task-incremental learning scenarios

In the task-incremental learning scenario, tasks with different classes are learned sequentially, requiring the model to identify each task after learning multiple tasks, as illustrated in Fig. 3a. To evaluate our model's performance, we conducted task-incremental learning experiments using various datasets, including sMNIST, pMNIST, and sCIFAR-100.

We compared our approach against several established methods on both ANNs and SNNs, including elastic weight consolidation (EWC) $^{32}$ , synaptic intelligence (SI) $^{33}$ , and context-dependent gating (XdG) $^{34}$ . Additionally, we utilized finely-tuned SNN and ANN models as baselines for comparison.

In the CH-HNN model, the ANN is optimized by ensuring consistency between the similarity of the generated modulation signals and the similarity of corresponding samples in the prior knowledge, rather than relying on direct supervised labels for the output modulation signals. This approach addresses the challenge of constructing labels in training datasets for ANN and enhances the model's adaptability to different tasks.

For the pMNIST dataset, which consists of 784! (the factorial of $28 \times 28$ ) permutations, we randomly selected 40 permutations to serve as tasks that are learned incrementally. The remaining permutations were used as prior knowledge to train the ANN to generate task-related modulation signals. To establish similarities between tasks, we grouped the permutations into clusters, with each cluster comprising four similar permutations, enabling the ANN to learn the relationships among tasks through the training samples. For the sMNIST, and sCIFAR-100 datasets, which lack natural task relationships, we manually specified task similarities, assigning a value of 1 within the same task and 0 between different tasks. This setup allows the ANN to perform episode inference based on the input samples from the test dataset.

To assess the effectiveness of the ANN-generated modulation signals in capturing relationships between various tasks, we computed correlation matrices among these signals, which were generated from visual samples in a test dataset. Using the pMNIST dataset as an example—where 40 tasks are grouped into clusters, with each cluster comprising four similar permutations—the correlation matrix (Fig. 3h) closely mirrors the patterns observed among visual samples of the permutations (Fig. 3b). This alignment suggests that ANNs can effectively generate task-related regularities in response to novel stimuli, thereby enabling dynamic episode inference.

With the architecture remaining unchanged in the continual learning framework, all algorithms were finely tuned. The experimental results indicate that, as the number of tasks increases, the CHHNN model exhibits a progressively greater performance advantage compared to other methods, as demonstrated in Fig. 3c-e.

At the final incremental stage, the CH-HNN model demonstrates a significant performance advantage over EWC, SI, and the fine-tuned baseline. On both the pMNIST and sCIFAR-100 datasets, CH-HNN substantially outperforms the XdG method. Moreover, CH-HNN maintains consistent performance across tasks, achieving the lowest inter-episode disparity—defined as the difference between the highest and lowest accuracy at the final stage. For example, on the sCIFAR-100 dataset, CH-HNN achieves an inter-episode disparity of $17.32\%$ , markedly lower than XdG's $48.76\%$ . These results highlight CH-HNN's superior balance between stability and plasticity, a key metric in continual learning, as illustrated in Fig. 3f, g (with further details in Supplementary Table 3).

Additionally, although the XdG method performs comparably to CH-HNN on the sMNIST dataset, it requires explicit task identification (ID) during both the training and inference phases, which constrains its applicability in real-world scenarios, the task-agnostic CH-HNN method not only achieves strong performance across diverse datasets in task-incremental settings but also eliminates the need for task ID, indicating its potential for real-world implementation.

# CH-HNN demonstrates superior performance in class-incremental learning scenarios

To explore more complex applications, we extended our investigation to class-incremental learning using the sMNIST, sCIFAR-100, and sTiny-ImageNet datasets. In these scenarios, the model incrementally

![](images/4228dc059851cf252a2b06bd1b912f14fbcb05e250fed4f60e7f5c7d29d27088.jpg)  
a

![](images/ad75a66d85f88e037851d20f9dd82b52c48b2d96563a9911b5af5409e7e8c568.jpg)  
b

![](images/81251c1e8560f8c27cf8d97eb09d612ec93d1369e08a708649ab9aeda4852e40.jpg)  
C

![](images/31c1aa30bddcf17be705933d4ac560748c1664423e759de08bf9725faf9abe75.jpg)  
d

![](images/f09b4e611b7ebdd0d1e20708aa8f92b0d33d5dc5d373c9a503a6f5bcf9f3c51e.jpg)  
e

![](images/0a153a90305f34887699c51ec8cd4a811dd90db6cddb22d19ba81a9325002318.jpg)

![](images/5216465c9cf7c69f1704a00a3f82c983ee9e5aa3f012c9af5869672c0e791135.jpg)  
f

![](images/c091af83127e693555410df97a58f126847d3ccd23bd1006f222d3880a7c3bbf.jpg)  
g

![](images/e948c2ce56ba33ed57efc4d649f0c02538dfc8c5cb29bc95f9b9de8376f6bd4c.jpg)  
h   
Fig. 3 | CH-HNN improves the performance of task-incremental learning across multiple datasets. a Schematic of the training protocol for task-incremental learning scenarios. b Correlation matrix of visual samples across the 40 tasks in the pMNIST dataset. Average test accuracy for incrementally learned tasks on c sMNIST, d pMNIST, and e sCIFAR-100 datasets. The results are presented as means over five random seeds, with shaded areas representing $\pm$ SEM. fViolin plot showing the distribution of test accuracy scores for each task after learning all   
tasks in the pMNIST dataset, with width representing probability density and overlaid scatter points indicating individual data points. g Test accuracy for individual task after completing all tasks in the sCIFAR-100 dataset, with results presented as means over five random seeds and shaded areas indicating $\pm$ SEM. h Correlation matrix illustrating the modulation signals generated by the ANN across 40 tasks in the pMNIST dataset.

learns multiple classes and must ultimately recognize all previously learned classes, as illustrated in Fig. 4a.

To facilitate this process, we employed a masking method that selectively activates output neurons corresponding to the current classes while suppressing those of other classes, ensuring efficient learning and minimizing interference among classes. Unlike task-incremental scenarios, which require constructing relationships among tasks that encompass various classes, the challenge here lies in

training the ANN to develop relationships among individual classes that have natural similarities. To address this, we used cosine similarity to compute the similarity between the statistics of feature maps from different categories during ANN training (see details in Methods). This approach enables the ANN to automatically generate modulation signals in response to each visual sample. Take the sTiny-ImageNet dataset as an example, we demonstrate the successful construction of an ANN capable of generating related-episode information across

![](images/ad7504c2b7b741638920ef93d7b1dedf4cfe955fb239e350de97bcf9a170f942.jpg)  
a

![](images/813ab3d72d7b8cc739d127afd5eab7884bcf7a9f1de0fa555ca621f0a3d762d5.jpg)  
b

![](images/b863bca6a0b5187cc8379201792c269e780af29834feb3a42a9beab8011bb51d.jpg)

![](images/20b332b7975e48f9442325d96b7ddff7453f902105db155e8b91b6d798d96488.jpg)

![](images/e327cde9fb8c81a284c771b1efd699973a373db4813e144006ba62d93c054215.jpg)  
CH-HNN (EIF) CH-HNN (IF) XdG (LIF) XdG (EIF) ANN-SI iCaRL Finetune-SNN ANN-EWC CH-HNN (LIF) XdG (ANN) Metaplasticity (LIF) Metaplasticity (EIF) FOSTER Finetune-ANN

![](images/39f1dabbe92b5de495cf974054ce010a5c83c1c0a13ab0976918d299a6902262.jpg)

![](images/a5c205f584dae9d4ae6c9b8bf5da85b75ae9e9824420c012cb3ca2db3c887ae3.jpg)  
h

![](images/6dc01c46f0156acb9ffb54d5fcc2c6bea4e64758c715c98e5c92fe8379a45d47.jpg)  
Fig. 4 | CH-HNN enhances the performance of class-incremental learning on various datasets. a Training protocol diagram for class-incremental learning scenarios. b Correlation matrix of visual samples across 200 classes of the sTinyImageNet dataset. Average test accuracy for incrementally learned classes on c sMNIST, d sTinyImageNet, and e sCIFAR-100 datasets, presented as means over five random seeds with shaded areas indicating $\pm$ SEM. f Test accuracy for each set   
of five classes after completing all classes of the sTiny-ImageNet dataset. g Violin plot showing the distribution of test accuracy scores for each set of five classes after learning all tasks in the sCIFAR-100 dataset, with overlaid scatter points highlighting individual data points. h Correlation matrix of the modulation signals generated by ANN across 200 classes in the sTiny-ImageNet dataset.

different classes by comparing the correlation matrix between modulation signals (Fig. 4h) with the correlation matrix between visual samples within a class (Fig. 4b).

In addition to the EWC, SI, XdG, and baseline methods employed in task-incremental learning, we further incorporate state-of-the-art methods such as iCaRL $^{35}$ and FOSTER $^{36}$ for class-incremental scenarios.

These methods, widely regarded as benchmarks in recent years, are better suited for class-incremental learning compared to EWC and SI, enabling a more comprehensive evaluation of CH-HNN.

For the experiments with iCaRL and FOSTER, we follow the parameter settings and utilized ResNet32 as specified in their respective publications. The experiments with EWC and SI are conducted using ANNs, which align more closely with their methodologies. For CH-HNN and XdG, we evaluate various spiking neuron models, including exponential integrate-and-fire (EIF) $^{37}$ , leaky integrate-and-fire (LIF) $^{38}$ , and integrate-and-fire (IF) $^{39}$ models, applied within SNNs to assess their performance.

With the architecture unchanged in the continual learning framework, all algorithms are optimally tuned. The experimental results show that both EWC and SI perform poorly in class-incremental learning, consistent with previous findings[40]. Our CH-HNN model, regardless of the neuron model used, outperforms all other state-of-the-art task-agnostic methods, including iCaRL and FOSTER, as well as metaplasticity approaches (Fig. 4c, d, e). Interestingly, as the complexity of the neuron models increases, CH-HNN demonstrates progressively better performance, likely attributed to the enhanced nonlinearity of the spiking models.

Notably, while XdG with the LIF neuron model performs comparably in the sMNIST dataset and even exceeds the performance of CHHNN in the sCIFAR-100 dataset, its performance declines in the sTinyImageNet dataset as the number of tasks increases. This decline may result from increased neuron overlap across tasks due to XdG's random neuron allocation strategy. Additionally, at the final stage of incremental learning, the inter-episode disparity of CHHNN is $44.34\%$ in the sTinyImageNet dataset and $21.47\%$ in the sCIFAR-100 dataset, both of which are lower than or comparable to those of other methods (see Supplementary Table 5 for further details), as illustrated in Fig. 4f, g.

Furthermore, CH-HNN dynamically generates episode-related regularities based on visual input during both training and testing phases, enabling task-agnostic learning. In contrast,XdG relies on explicit task identification during both training and inference, highlighting CH-HNN's superior adaptability and suitability for real-world applications.

# Knowledge transfer from prior knowledge to new concept learning

With the hypothesis that the mPFC-CA1 circuits learn regularities that summarize related information from prior knowledge, it is crucial to explore whether the ANNs in our CH-HNN model can effectively transfer related-episode knowledge across different datasets, as illustrated in Fig. 5a. Therefore, we conducted experiments where ANNs were pretrained on prior knowledge derived from the ImageNet dataset and then assessed their performance on the sCIFAR-100 and sTiny-ImageNet datasets. To ensure the priors were distinct, we followed the methodology of ref. 41 to exclude classes overlapping with CIFAR-100 and Tiny-ImageNet from ImageNet. These experiments utilized the EIF neuron model, which demonstrated the highest performance in class-incremental scenarios for both datasets within the CH-HNN framework.

By incorporating an ANN pre-trained on prior knowledge, the CHHNN model continues to significantly outperform other state-of-the-art methods on both sCIFAR-100 and sTiny-ImageNet, demonstrating its ability to transfer knowledge across datasets. This success stems from the ANN component, which effectively learns to extract regularities from prior experiences. The strong alignment between the correlation matrix of modulation signals and sample representations (see Supplementary Fig. 6c, d) further supports this capability.

# The evaluation of the feedback loop within the corticohippocampal circuits

In evaluating the efficacy of episode-related information in task-incremental and class-incremental learning, we have validated the role

of episode-related regularities in enhancing the learning of novel concepts, thus supporting the function of the feed-forward loop from mPFC-CA1 to DG-CA3 circuits. To further investigate the functional role of the feedback loop from DG-CA3 to mPFC-CA1 circuits, which is believed to transmit novel embeddings to promote generalization across related episodes $^4$ , we designed experiments where the ANN incrementally learns the classes in the sCIFAR-100 and sTiny-ImageNet datasets.

In the ANN's incremental learning process, we employed metaplasticity mechanism to mitigate forgetting of previously learned regularities. This approach enables the ANN to continuously learn new embeddings, enhancing its ability to extract episode-related regularities. As the ANN incrementally learns classes, CH-HNN demonstrates improved efficiency, as illustrated in Fig. 5e, f. The correlation matrix, which assesses the consistency of regularities with the sample representations, also demonstrated improvement after learning all classes, exemplified by the sTiny-ImageNet dataset in Supplementary Fig. 6e and 6f. These results indicate that as the ANN in CH-HNN accumulates prior knowledge, its ability to generalize across episodes improves.

Collectively, these findings validate the efficacy of the feedback loop (CA1-CA3 to mPFC-CA1) in transmitting novel embeddings to promote generalization across related episodes, contributing to a deeper understanding of the corticohippocampal neural mechanisms that support lifelong learning.

# Lesion experiments

To dissect the contributions of episode inference from ANN's modulation signals and metaplasticity mechanisms within our CH-HNN framework, we conducted a series of ablation studies targeting these core mechanisms.

For the pMNIST dataset, both mechanisms play a substantial role in enhancing continual learning. Metaplasticity, in particular, enhances stability by balancing the retention of old knowledge with the integration of new information, resulting in a lower inter-episode disparity $(12.53\%)$ compared to episode inference alone $(29.77\%)$ . Episode inference, meanwhile, enhances overall performance by improving average accuracy, reaching a mean of $70.41\%$ (Fig. 5g).

In class-incremental experiments on sTiny-ImageNet, metaplasticity has a limited effect, while episode inference plays a critical role in enhancing the CH-HNN model's performance, achieving $70.70\%$ , which is comparable to the full CH-HNN model's performance of $70.72\%$ . However, when ANN guidance is based on priors from less-relevant datasets—thus decreasing guidance accuracy—metaplasticity becomes particularly beneficial, increasing the average accuracy from $42.89\%$ to $47.23\%$ (see Fig. 5h, i, and Supplementary Table 6).

In summary, both episode inference and metaplasticity are essential to our CH-HNN model: episode inference provides the primary boost to overall performance, while metaplasticity offers crucial support under conditions of inaccurate guidance by balancing the retention of old and new knowledge through the preservation of synaptic weights from prior episodes.

# Applicability and robustness of CH-HNN in real-world implementation

Most high-performing continual learning algorithms, including XdG methods and the recently proposed channel-wise lightweight reprogramming methods $^{42}$ , rely on a perfect task oracle during the inference phase to accurately identify the task for each test image. This dependence complicates their deployment in dynamic real-world environments. In contrast, our CH-HNN model is designed for task-agnostic learning, enabling straightforward implementation across diverse real-world scenarios.

The applicability of CH-HNN is well-aligned with the growing adoption of hybrid ANN-SNN architectures in neuromorphic hardware $^{43,44}$ , such as PAICORE $^{45}$ and "Tianjic" chip $^{46}$ , which support

CH-HNN (ImageNet as priors) CH-HNN (ImageNet with overlapping classes removed as priors)   
CH-HNN (ImageNet with randomly removed classes as priors) iCaRL FOSTER   
ANN-EWC Metaplasticity Finetune-ANN Finetune-SNN ANN-SI

![](images/b4c48f60752a62ec8bb6728f2900d33a016cadddaec08c184ce4bfbabad878aa.jpg)  
a

![](images/6cffc5931b11624b024b1a355683816f564a89d23d97c3f4846a36d0cef06e67.jpg)  
b

![](images/2152f3f985d6b137a9d599b35d95d23a11227a6d353b000ca68fd4def727bdb8.jpg)  
C

![](images/fbb487428a91ba2081d671f2de497090e1c43069bd9353a94d1bc9d4d8bd1240.jpg)

![](images/cf4ab9489ccead4d7888c2928053b883ba25f593c49f02da8b7c9018bc482509.jpg)  
d

![](images/e0d191a7b0a3b291d791505cff875be7a8a657670b0ed9d59aa3df76806fb6a9.jpg)  
e

![](images/7ea0c698008ab3d380c24b6dce43156ac0a4b375e247c445a6785ce878b13161.jpg)  
f

![](images/2c1cd2b9786e664a20087f4e05fef4a2a7ed90d28dc2601d8535cde109dae913.jpg)  
g

![](images/8fc8e85196e352dd69257adcc75cf33acae30f5f527b3b62dc12b875656eb510.jpg)  
h

![](images/e433b057785d7b0c1ebe88c77ca213b7dfccee50cdacaa87518dc4fd4e7a62f1.jpg)  
i   
Fig. 5 | CH-HNN demonstrates the efficacy of the feedback loop. a Diagram illustrating knowledge transfer for episode-related information. Average test accuracy for incrementally learned classes on b sTiny-ImageNet and c sCIFAR-100 datasets. d Diagram depicting feedback loops within corticohippocampal circuits. Average test accuracy for incrementally learned classes with different ANN training designs on e sTiny-ImageNet and f sCIFAR-100 datasets. g Average test accuracy in   
lesion experiments on the pMNIST dataset. Results are presented as means over five random seeds, with shaded areas indicating $\pm$ SEM. Violin plots showing the distribution of test accuracy scores for each set of five classes after learning all tasks in h the sTiny-ImageNet dataset and i the ImageNet-as-Priors condition in sTinyImageNet dataset.

![](images/36f48f3d8b93f2fc805e1d4acfb5d674865a6ee6005b35ba7e5a4dc5666cc50d.jpg)

![](images/4523f6628fcb1b253f0026a5434da881d47912582d7b5250709c72615f04c4c1.jpg)

![](images/ba0d1bc22a28768c1b53c49142d766a33e2461065116d87a8a75c6252653cb35.jpg)

![](images/adb2fd62e2e0c331ea22de6b374b1757757075b8ceb0aba177b5f5e71acf8d59.jpg)

![](images/81d38b688e2c49d2a6a87cfcf00b8a3059efaeb85411964c2c096ba64b0e4cd3.jpg)  
Fig. 6 | CH-HNN demonstrates adaptiveness and robustness in real-world applications. a The quadruped robot performs actions guided by MNIST code recognition using CH-HNN. b The robotic arm identifies and grasps a specific object (apple) based on CH-HNN's decision-making. c Average accuracy of various methods in real-world applications with different object positions and angles. The box plot displays the interquartile range (IQR) with Q3 (upper quartile) and Q1   
(lower quartile), and outliers are shown as individual points. d Performance comparison under varying Gaussian noise (GN) levels for class-incremental learning on the sCIFAR-100 dataset. Results represent the distribution across five random seeds. e Power consumption analysis, comparing contributions from fully-connected layers (FC-L1 or L2), hybrid layers (Mask-L1 or L2), the output layer, and total consumption.

configurable cores capable of operating as either ANN or SNN components. Considering the precision constraints of most neuromorphic hardware, we reduce the CH-HNN model's precision from float32 to int8, observing minimal performance loss (Supplementary Fig. 4c). Furthermore, simulation results from a cycle

accurate simulator, validated by refs. 47,48, show that SNNs offer a significant advantage in reducing power consumption by $60.82\%$ compared to ANNs in new concept learning (Fig. 6e). These findings underscore the suitability of CH-HNN for low-power neuromorphic hardware applications.

To validate the robustness of our CH-HNN model in real-world applications, we implemented it in two practical settings. First, we applied CH-HNN to a pMNIST recognition task using a quadruped robot equipped with a real-time camera. The robot uses OpenCV $^{49}$ to crop MNIST images, which are processed by the ANNs within CH-HNN to generate modulation signals for episode inference, guiding the SNNs for accurate recognition. Recognized images trigger actions such as nodding or looking upwards (Fig. 6a, Supplementary Movie 1).

Second, we applied CH-HNN, trained in a class-incremental manner on sCIFAR-100 data, to an object grasping task using YOLO detection. CH-HNN identified objects (e.g., distinguishing "Apple" and "Not Apple") within the camera's field of view, enabling precise robotic arm grasping (Fig. 6b, Supplementary Movie 2). In a robustness evaluation involving sCIFAR-100 objects under varied positions and angles, CH-HNN achieved an average accuracy of $82\%$ ( $\pm 7.25\%$ ) over 30 trials, demonstrating its robustness under diverse conditions. The experiment included objects from both early and late learning stages, with CH-HNN outperforming methods like EWC in addressing the stability-plasticity dilemma (Fig. 6c, and Supplementary Fig. 4a). Additionally, CH-HNN shows resilience under Gaussian noise, maintaining acceptable performance despite some degradation (Fig. 6d).

Consequently, our CH-HNN method demonstrates both applicability and robustness in realistic scenarios. Furthermore, with integrated spiking unit structures, CH-HNN offers the added advantage of low power consumption.

# Discussion

The challenge of catastrophic forgetting in artificial systems during continual learning has garnered increasing attention. Incorporating brain-inspired learning mechanisms into artificial algorithms has shown promise in addressing this issue. For instance, generative replay<sup>40</sup> emulates the complementary roles of the cortices and hippocampus in managing long-term and short-term memories by storing generative features of old tasks and reusing them during new task learning. Additionally, metaplasticity methods introduce a global modulation mechanism that adjusts synaptic plasticity, offering another brain-inspired strategy to mitigate catastrophic forgetting<sup>9,31</sup>.

Despite success in specific contexts, continual learning faces challenges, particularly in real-world applications. Methods such as generative replay encounter growing memory demands as tasks accumulate. Additionally, metaplasticity-based approaches, while effective on simpler datasets like MNIST, tend to perform relatively poorly on more complex, real-world data. Furthermore, methods like XdG, which are not task-agnostic, rely on a task oracle, limiting their applicability in real-world scenarios.

To address these limitations, we develop a novel method termed CH-HNN, which integrates ANNs and SNNs into a hybrid neural network inspired by recurrent corticohippocampal loops. CH-HNN eliminates the need for a task oracle, exhibiting strong performance and power efficiency in real-world applications. While CH-HNN supports diverse neuron models, selecting the appropriate model involves trade-offs. Complex neuron models like the EIF model enhance biological realism and accuracy but demand more computational resources compared to simpler models like LIF and IF. Although the exponential term in the EIF model can be efficiently managed using a look-up table and results in only a modest power overhead of $8.35\%$ to $8.58\%$ on the "Tianjic" chip, real-world applications must still consider trade-offs among performance, memory cost, biological plausibility, and hardware compatibility to meet specific demands.

From the perspective of neural mechanisms in corticohippocampal circuits, CH-HNN provides indirect evidence for potential neural mechanisms. First, modulation of the feedforward loop from mPFC-CA1 to DG-CA3 can be achieved by resetting the neural synchrony state, offering complementary insights to generative replay methods $^{40}$ , which propose direct transfer of old knowledge from the

cortices to the hippocampus. Second, novel embedding transfers from feedback loops potentially enhance the generalization of related memories. Third, certain regions of the brain, such as the lateral posterior cortex and lateral prefrontal cortex, can modulate metaplasticity in the DG-CA3 circuits through chemical neuromodulatory signals.

Furthermore, there is ongoing debate regarding how the brain represents concepts—whether through distinct engrams or episode inference. The success of our CH-HNN method suggests that episodes are not encoded by discrete engrams but are instead processed through guidance based on episode-related information. Although our model simplifies the recurrent loop as mPFC-CA1 and DG-CA3, other research emphasizes the role of the EC in episode-related representations[21]. Furthermore, evidence indicates different functions for the anterior and posterior hippocampus. The anterior hippocampus interacts primarily with regions of the brain associated with generalized knowledge, whereas the posterior hippocampus is involved in specific memory representations. These findings further elucidate an interpretable neural mechanism underlying lifelong learning.

While current continual learning algorithms, including our CH-HNN model, effectively leverage prior knowledge to achieve high performance $^{41,51}$ , comparing models with prior knowledge to those without dedicated prior-learning mechanisms may seem imbalanced. Nevertheless, it is important to highlight that our approach offers an indirect method of prioritizing prior knowledge to facilitate new concept learning, potentially reflecting a neural mechanism for lifelong learning in the brain. Given that humans can sequentially acquire new concepts from only a few examples, therefore, integrating few-shot learning $^{52}$ with continual learning could be a promising avenue for future research. This integration may enhance the adaptability and efficiency of online continual learning in dynamic environments. Additionally, our model may encounter challenges in contexts where task correlations are limited, as it relies on the presence of natural or designed correlations among incremental episodes.

In conclusion, our study introduces a model that simplifies the simulation of corticohippocampal recurrent circuits, improving the performance and adaptability of continual learning in real-world applications, while emphasizing the potential of integrating neuroscientific insights into artificial intelligence systems.

# Methods

# Dataset process protocols

For the pMNIST dataset, each $28 \times 28$ image is randomly permuted to create a diverse set of image permutations. We have two subsets with these permutations, one containing 700 permutations and another with 40 permutations, the latter organized into ten groups. Each group contains four permutations with intra-group similarity to construct cross-task relationships.

For the sMNIST dataset, the 10 classes of MNIST are divided into 5 episodes, each containing 2 classes.

Similarly, the CIFAR-100 and Tiny-ImageNet datasets are divided into 20 and 40 episodes, respectively, with each episode comprising 5 classes. This results in the sCIFAR-100 and sTiny-ImageNet datasets. Prior to experiments, the $32 \times 32$ RGB image samples from these datasets are processed through the CLIP foundation model[53] to generate feature maps with 768 channels.

For the DVS Gesture dataset, we divide the data into 4 episodes, containing 3, 3, 3, and 2 classes, respectively.

# Structures of CH-HNNs

The architecture of the CH-HNN comprises several key designs, including:

(1) design of ANNs that generate episode-related modulation signals according to the similarity across various episodes;

(2) design of SNNs equipped with various neuron models that incrementally learn various episodes under the guidance of the modulation signals;   
(3) design of metaplasticity mechanisms that modulate the weight updating process in the SNNs and continual ANNs.

# Design and training methods for ANNs within CH-HNN

In principle, structures such as convolutional networks and transformers can be used to construct the ANNs within CH-HNN model. In this paper, the ANN is built with a fully connected network consisting of three linear layers, each layer encompassing 64 or 256 neurons. At the end of the network, each linear decoder produces a binary modulated signal vector, which is then normalized using a Softmax operation. The processing of the ANN is described by the following equation:

$$
\mathbf {R} = \mathbf {A} (\mathbf {x}; \theta_ {\mathrm {A}}) \tag {1}
$$

where $\mathbf{x}$ and $\mathbf{R}$ represent the input sample and the output modulated signal of the ANN, respectively. $\mathbf{R}$ is a binary matrix of size $n \times c$ , where the number of columns equals the number of hidden layer neurons $c$ in the SNN to be modulated. Each row in the matrix represents a modulated signal, denoted as $\mathbf{R}_i$ , with a total of $n$ such signals.

The training of the ANN is accomplished by optimizing the following objective function:

$$
\min  _ {\theta_ {\mathrm {A}}} \mathrm {E} _ {\mathbf {x}, \widetilde {\mathbf {x}} \sim D} \sum_ {i = 1} ^ {n} \left[ \left| \frac {\mathbf {R} _ {i} \widetilde {\mathbf {R}} _ {i}}{| \mathbf {R} _ {i} | | \widetilde {\mathbf {R}} _ {i} |} - \operatorname {s i m} (\mathbf {x}, \widetilde {\mathbf {x}}) \right| ^ {p} + \beta | \| \mathbf {R} _ {i} \| _ {1} - \rho c |\right) \tag {2}
$$

where $D$ is the dataset. The objective function is divided into two parts: the first term constrains the similarity between the modulated signals $\mathbf{R}_i$ and $\widetilde{\mathbf{R}}_i$ generated by the ANN to be consistent with the similarity of the $\mathbf{x}$ and $\widetilde{\mathbf{x}}$ . The second term constrains the sparsity of the generated modulated signals. $\beta$ is the coefficient that balances the two terms. $\rho$ is the desired sparsity, which is generally set to $\frac{1}{n}$ . During actual training, the mini-batch Adam optimization method is used for optimization.

The similarity of the corresponding samples $\mathrm{sim}(\mathbf{x},\widetilde{\mathbf{x}})$ in CH-HNN model can be defined in two ways. First, for task-incremental scenarios of the pMNIST dataset and all class-incremental learning scenarios where inherent correlations exist across episodes, similarity is automatically computed using cosine similarity:

$$
\operatorname {s i m} (\mathbf {x}, \widetilde {\mathbf {x}}) = \frac {\mathbf {x} _ {*} \widetilde {\mathbf {x}} _ {*}}{| \mathbf {x} _ {*} | | \widetilde {\mathbf {x}} _ {*} |} \tag {3}
$$

where $\mathbf{x}$ and $\widetilde{\mathbf{x}}$ represent statistics of the sampled instances from different episodes after dimension reduction via principal component analysis. For the sCIFAR-100 and sTiny-ImageNet datasets, $\mathbf{x}$ represents the feature maps extracted by the CLIP foundation model. For the sMNIST, pMNIST, and DVS Gesture datasets, $\mathbf{x}$ is the flattened vector of the original images. Second, for the task-incremental learning on sMNIST, sCIFAR-100, and sTiny-ImageNet datasets, without inherent or natural correlations across tasks, we manually specified the task similarities to clearly define their relationships. Specifically, we set the similarity within the same task to 1, and between different tasks to 0.

In the comparison experiments among models, all training dataset that will be continually learned in SNNs are involved in the ANN's offline training, except for the task-incremental learning dataset on pMNIST dataset. The other 700 permutation are as prior knowledge added part (0, 10, 20) of 40 permutations for SNNs incremental learning are involved in the ANN's offline training.

In the knowledge transfer evaluation experiments, we used three different configurations of the ImageNet dataset as priors. First, we selected classes with more than 500 samples in the training dataset, resulting in 950 classes, which we refer to as 'ImageNet as priors' in the legends. Second, following $^{41}$ , we removed classes from these 950 that

overlapped with CIFAR-100 or TinyImageNet, yielding 550 classes. This configuration is labeled as 'ImageNet with overlapping classes removed as priors'. Lastly, to examine the role of overlapping classes, we randomly removed 400 classes from the original 950, resulting in 550 classes, referred to 'ImageNet with randomly removed classes as priors'.

In the experiments of ANN's continual learning, the metaplasticity is included in its optimization process, which will be demonstrated more details in next section. In the sCIFAR-100 and sTiny-ImageNet dataset, the ANN need to incrementally learn the first half classes, respectively, and then remaining classes.

The correlation matrices generated by ANN are derived from randomly selected samples from the test dataset.

# Design and training methods for SNNs within CH-HNN model

The SNN contains three layers in all experiments in our study, and the first two layers consist of batch normalization (BN) following the fully connected layer:

$$
\operatorname {o u t} = \mathbf {W} _ {3} \left(\prod_ {l = 1} ^ {2} \underline {{\mathbf {R} _ {l}}} \theta^ {l} (\mathrm {B N} \left(\mathbf {W} _ {l} \mathbf {x}\right)) \right. \tag {4}
$$

where $\mathbf{x}$ is a visual input to the SNN, $\mathbf{W}_l$ represents the weights of each fully connected layer, followed by BN Layer. $\theta^l$ represents neuron models which we employ as the basic units in SNNs. The underlined $\mathbf{R}_l = \mathbf{A}_l(\mathbf{x};\theta_{\mathrm{A}})$ is generated by a well-trained ANN using the same visual input, selectively activating neurons in each layer $l$ using a mask method. In this study, we utilize the surrogate gradient methods for training efficiently, with the cross entropy (CE) loss function.

To compare the performance of different neuron models, we implement the EIF, LIF and IF neuron models.

For the EIF neuron model, the neuron dynamic is shown as below:

$$
\left\{ \begin{array}{c} \tau \frac {d V (t)}{d t} = - \left(V (t) - V _ {\text {r e s e t}}\right) + \Delta_ {T} \cdot \exp \left(\frac {V (t) - V _ {\text {t h}}}{\Delta_ {T}}\right) + R I (t) \\ \text {i f} V (t) > V _ {\text {t h}}, V (t) \leftarrow V _ {\text {r e s e t}}, \text {s p i k e} (t) \leftarrow 1 \end{array} \right. \tag {5}
$$

where the $V_{\mathrm{th}}$ is the spike threshold, $\Delta_T$ is the sharpness of the exponential term, $V_{\mathrm{reset}}$ is the reset voltage, and $R$ is the resistance of membrane.

For the LIF neuron, the equation describing its membrane potential dynamics is as follows:

$$
\tau \frac {d V (t)}{d t} = - (V (t) - V _ {\text {r e s e t}}) + R I (t) \tag {6}
$$

The process of spike generation is the same as that of EIF.

For the IF neuron model, the computation of spike is also not changed, with:

$$
\tau \frac {d V (t)}{d t} = R I (t) \tag {7}
$$

For numerical simulation, these equations were discretized in time using the Euler method. For example, the following is the discrete iterative formula for the LIF neuron:

$$
\left\{ \begin{array}{l} V _ {i + 1} = V _ {i} \lambda \left(\mathbf {1} - o _ {i}\right) + \mathbf {w} ^ {*} \mathbf {s} _ {i + 1}, \\ o _ {i} = \mathcal {H} \left(V _ {i} - V _ {\text {t h}}\right), \\ \lambda = \mathrm {e} ^ {- \frac {T _ {\mathrm {d}}}{\tau}}. \end{array} \right. \tag {8}
$$

where $V_{i}, o_{i}$ , and $\mathbf{s}_i$ represent the membrane potential, spike output, and spike input of the neuron at the $i$ -th time step, respectively. $\mathcal{H}$ is the unit step function, and $\lambda$ is the decay coefficient of the membrane potential. $T_{\mathrm{d}}$ is the discretization time interval.

The firing rate of the spiking neurons are encoded by rate coding, and then be decoded by fully connected layers in the output layer.

Metaplasticity Mechanisms introduced to both SNNs and ANNs The metaplasticity mechanisms are used in the optimization process of SNN's or ANN's incrementally learning process, with the modulation of the local synaptic plasticity by modifying the optimization process:

$$
\mathbf {W} _ {i + 1} = \mathbf {W} _ {i} - \alpha f (m, \mathbf {W} _ {i}), \quad i = 1, \dots , T \tag {9}
$$

$$
f (m, \mathbf {W} _ {i}) = e ^ {- | m \mathbf {W} _ {i} |} \tag {10}
$$

where $\mathbf{W}_i$ represents hidden weights within SNNs or ANNs, and $\alpha$ represents the learning rate. $f(m, \mathbf{W}_i)$ is set as exponential function, such that can decrease learning rate of local synapse with the neural weights accumulate, from 0 to 1 (see Supplementary Fig. 2a).

While the ANN within our CH-HNN model which is responsible for generate modulation signal is incrementally learned, the meta value $m$ is set as 15 in sCIFAR-100 dataset, and set as 10 in sTiny-ImageNet dataset.

# Pseudo-code for CH-HNN model

Algorithm 1. ANN within CH-HNN model

1: Input: $\theta_{\mathrm{A}}$ , D, sim, $N$ , $p$ , $\lambda$ , $B$ , $\rho$ , $c$ , $\eta$   
2: for $i \gets 1$ to $N$ do   
3: $\Delta \theta_{\mathrm{A}}\gets 0$ $\triangleright$ Initialize gradients   
4: $\mathbf{for}j\gets 1$ toBdo   
5: $\mathbf{x},\tilde{\mathbf{x}}\sim \mathbf{D}$ $\triangleright$ Sample two samples from dataset   
6: $\mathbf{R} \gets \mathbf{A}(\mathbf{x}; \theta_{\mathbf{A}}), \tilde{\mathbf{R}} \gets A(\tilde{\mathbf{x}}; \theta_{\mathbf{A}}) \triangleright$ Calculate modulation signals   
7: $\Delta \theta_{\mathrm{A}}\gets \Delta \theta_{A} + \nabla_{\theta_{A}}\sum_{k = 1}^{n}\left|\left|\frac{\mathbf{R}_{k}\mathbf{R}_{k}}{\left|\mathbf{R}_{k}\right|\left|\mathbf{R}_{k}\right|} -\operatorname {sim}(\mathbf{x},\tilde{\mathbf{x}})\right|^{p} + \lambda \right|\left|\left|\mathbf{R}_{k}\right|\right|_{1} - \rho c\left|\right|$

$\triangleright$ Update gradients

8: end for   
9: $\theta_{\mathrm{A}}\leftarrow \theta_{\mathrm{A}} - \eta \Delta \theta_{\mathrm{A}} / B\triangleright$ Update parameters   
10: end for

Algorithm 2. SNN within CH-HNN model

1: Input: $\mathbf{W_h}$ , $\theta_{\mathrm{S}}$ , $\theta_{\mathrm{BN}}$ , A, $\theta_{\mathrm{A}}$ , $(\mathbf{x}, \mathbf{y})$ , $\delta$ , m.   
2: $\mathbf{R} \gets \mathbf{A}(\mathbf{x}; \theta_{\mathbf{A}}) \quad \triangleright$ Generate modulation signals through ANN   
3: $\hat{\mathbf{y}}\gets$ Forward(S(x; $\theta_{\mathrm{S}})^{*}\mathbf{R},\mathbf{W}_{\mathbf{h}},\theta_{\mathrm{BN}})$ $\triangleright$ Perform inference   
4: C $\leftarrow$ CE(y,y) $\triangleright$ Compute mean loss over the batch   
5: for $\mathbf{W}_l$ in $\mathbf{W}_h\mathbf{d}\mathbf{o}$   
6: $\mathbf{W}_l \gets \mathbf{W}_l - \delta f(m, \mathbf{W}_l) \mathbf{W}_l \quad \triangleright$ Metaplasticity mechanisms   
7: end for   
8: $\theta_{\mathrm{BN}}\gets \theta_{\mathrm{BN}} - \delta \theta_{\mathrm{BN}}$   
9: return $\mathbf{W}_h$ , $\theta_{\mathrm{BN}}$

# Evaluation metrics

In incremental learning, we use several evaluation metrics to compare the performance of different methods.

(1) Average accuracy of the learned tasks or classes at the end of the incremental learning stage, which is given by:

$$
\frac {1}{N} \frac {1}{T} \sum_ {i = 1} ^ {T} \sum_ {j = 1} ^ {N} A _ {i j} \tag {11}
$$

where $T$ is the total number of tasks or classes, $N$ is the number of random seeds, and $A_{ij}$ is the accuracy on task $i$ using random seed $j$ .

(2) Average accuracy across random seeds for each task or class when the final stage of learning is completed, defined as:

$$
\frac {1}{N} \sum_ {j = 1} ^ {N} A _ {i j} \tag {12}
$$

where $N$ is the number of random seeds, and $A_{ij}$ is the accuracy on task $i$ using random seed $j$ .

(3) Inter-episode disparity calculated as the absolute difference between the highest and lowest test accuracy across all tasks or classes after the learning process:

$$
\frac {1}{N} \sum_ {j = 1} ^ {N} \left| \max  \left(A _ {1}, A _ {2}, \dots , A _ {T}\right) - \min  \left(A _ {1}, A _ {2}, \dots , A _ {T}\right) \right| \tag {13}
$$

where $A_{i}$ is the test accuracy on task $i$ .

# Implementation details

In all implementation experiments, the system performs inference tasks using models pre-trained in an incremental learning manner. For pMNIST recognition on robotic dogs, an Intel RealSense D435i RGB-D camera is mounted on a Unitree GO1 quadruped robot for real-time detection. The pMNIST images are displayed on a screen, and OpenCV $^{49}$ is employed to detect edges and crop the images. These images are then processed by the ANNs within the CH-HNN, which generate modulation signals for episode inference, guiding the SNN to predict a label (0 to 9) from the dataset. UDP communication with the Unitree GO1 robot is established via the Unitree SDK, enabling the robot to perform predefined actions such as nodding or looking up based on the recognition results.

For robotic arm experiments involving objects from the sCIFAR-100 dataset, objects within the camera's field of view are detected and cropped using the YOLO algorithm $^{50}$ . The recognition model, trained on sCIFAR-100, predicts labels from 0 to 99. If the predicted label matches a predefined target, such as an apple, the robotic arm is instructed to perform a grasp operation; otherwise, it refrains from grasping. The YOLO algorithm provides X and Y coordinates, while an RGB-D camera supplies depth data to determine the X-Y-Z spatial coordinates of the target. This information is transmitted to the robot, enabling the Unitree Z1 robotic arm to execute precise grasping of the object.

To evaluate the robustness of different models in real-world applications, five objects were selected from dataset indices 0 to 99: apple (index 0), bottle (index 9), orange (index 53), rose (index 70), and wolf (index 97). A RealSense camera was used to capture images for testing, and thirty recognition tests were conducted for each object with the camera in a fixed position. The objects were placed in three locations relative to the camera frame-left, center, and right--each tested ten times. Additionally, angular rotations were applied to the objects to introduce various perspectives during the tests.

# Data availability

All data used in this paper are publicly available and can be accessed at http://yann.lecun.com/exdb/mnist/for MNIST dataset, https://www.cs.toronto.edu/~kriz/cifar.htmlfor CIFAR-100 dataset, http://cs231n.stanford.edu/tiny-imagenet-200.zipfor Tiny-ImageNet dataset, and https://tonic.readthedocs.io/en/latest/generated/tonic.datasets.

DVSGesture.htmlfor DVS Gesture dataset.

# Code availability

The codes are available on Zenodo $^{54}$ (https://doi.org/10.5281/zenodo.14406003) and can also be accessed on GitHub (https://github.com/qqish/CH-HNN).

# References

1. Achiam, J. et al. GPT-4 technical report. Preprint at https://arxiv.org/abs/2303.08774 (2023).   
2. Hannula, D. E. & Duff, M. C. The Hippocampus from Cells to Systems: Structure, Connectivity, and Functional Contributions to Memory and Flexible Cognition (Springer, 2017).

3. Zeithamova, D. & Bowman, C. R. Generalization and the hippocampus: more than one story? Neurobiol. Learn. Mem. 175, 107317 (2020).   
4. Koster, R. et al. Big-loop recurrence within the hippocampal system supports integration of information across episodes. Neuron 99, 1342-1354 (2018).   
5. Zhou, Q., Du, C. & He, H. Exploring the brain-like properties of deep neural networks: a neural encoding perspective. Mach. Intell. Res. 19, 439-455 (2022).   
6. Wu, Y. et al. Efficient visual recognition: a survey on recent advances and brain-inspired methodologies. Mach. Intell. Res. 19, 366-411 (2021).   
7. Zhao, R. et al. A framework for the general design and computation of hybrid neural networks. Nat. Commun. 13, 3427 (2022).   
8. Mongillo, G., Rumpel, S. & Loewenstein, Y. Intrinsic volatility of synaptic connections—a challenge to the synaptic trace theory of memory. Curr. Opin. Neurobiol. 46, 7-13 (2017).   
9. Zhang, T. et al. A brain-inspired algorithm that mitigates catastrophic forgetting of artificial and spiking neural networks with low computational cost. Sci. Adv. 9, eadi2947 (2023).   
10. Bowman, C. R. & Zeithamova, D. Training set coherence and set size effects on concept generalization and recognition. J. Exp. Psychol. Learn. Mem. Cogn. 46, 1442 (2020).   
11. Kuhl, B. A. & Chun, M. M. Successful remembering elicits event-specific activity patterns in lateral parietal cortex. J. Neurosci. 34, 8051-8060 (2014).   
12. LeCun, Y., Bottou, L., Bengio, Y. & Haffner, P. Gradient-based learning applied to document recognition. Proc. IEEE 86, 2278-2324 (1998).   
13. Krizhevsky, A. Learning multiple layers of features from tiny images. Tech. Rep. TR-2009, Univ. Toronto (2009).   
14. Le, Y. & Yang, X. Tiny ImageNet visual recognition challenge. CS 231N 7, 3 (2015).   
15. Amir, A. et al. A low power, fully event-based gesture recognition system. Proc. IEEE Conf. Comput. Vis. Pattern Recognit. 7388-7397 (IEEE, 2017).   
16. Wang, L., Zhang, X., Su, H. & Zhu, J. A comprehensive survey of continual learning: Theory, method and application. IEEE Trans. Pattern Anal. Mach. Intell. 46, 5362-5383 (2024).   
17. Hintzman, D. L. & Ludlam, G. Differential forgetting of prototypes and old instances: simulation by an exemplar-based classification model. Mem. Cogn. 8, 378-382 (1980).   
18. Bowman, C. R. & Zeithamova, D. Abstract memory representations in the ventromedial prefrontal cortex and hippocampus support concept generalization. J. Neurosci. 38, 2605-2614 (2018).   
19. McClelland, J. L., McNaughton, B. L. & O'Reilly, R. C. Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory. Psychol. Rev. 102, 419 (1995).   
20. Baldassano, C., Hasson, U. & Norman, K. A. Representation of real-world event schemas during narrative perception. J. Neurosci. 38, 9689-9699 (2018).   
21. Schapiro, A. C., Turk-Browne, N. B., Botvinick, M. M. & Norman, K. A. Complementary learning systems within the hippocampus: a neural network modelling approach to reconciling episodic memory with statistical learning. Philos. Trans. R. Soc. B 372, 20160049 (2017).   
22. Cavada, C., Company, T., Tejedor, J., Cruz-Rizzolo, R. J. & Reinoso-Suárez, F. The anatomical connections of the macaque monkey orbitofrontal cortex: a review. Cereb. Cortex 10, 220-242 (2000).   
23. Clelland, C. D. et al. A functional role for adult hippocampal neurogenesis in spatial pattern separation. Science 325, 210-213 (2009).   
24. Pei, J. et al. Towards artificial general intelligence with hybrid Tianjin chip architecture. Nature 572, 106-111 (2019).

25. Wilson, M. A. & McNaughton, B. L. Reactivation of hippocampal ensemble memories during sleep. Science 265, 676-679 (1994).   
26. Deuker, L. et al. Memory consolidation by replay of stimulus-specific neural activity. J. Neurosci. 33, 19373-19383 (2013).   
27. Varga, N. L., Gaugler, T. & Talarico, J. Are mnemonic failures and benefits two sides of the same coin? Investigating the real-world consequences of individual differences in memory integration. Mem. Cognit. 47, 496-510 (2019).   
28. Gershman, S. J., Schapiro, A. C., Hupbach, A. & Norman, K. A. Neural context reinstatement predicts memory misattribution. J. Neurosci. 33, 8590-8595 (2013).   
29. Mack, M. L., Preston, A. R. & Love, B. C. Decoding the brain's algorithm for categorization from its neural implementation. Curr. Biol. 23, 2023-2027 (2013).   
30. Soures, N., Helfer, P., Daram, A., Pandit, T. & Kudithipudi, D. TACOS: Task agnostic continual learning in spiking neural networks. Preprint at https://arxiv.org/abs/2409.00021 (2024).   
31. Laborieux, A., Arnoult, M., Hirtzlin, T. & Querlioz, D. Synaptic metaplasticity in binarized neural networks. Nat. Commun. 12, 2549 (2021).   
32. Kirkpatrick, J. et al. Overcoming catastrophic forgetting in neural networks. Proc. Natl. Acad. Sci. USA 114, 3521-3526 (2017).   
33. Zenke, F., Poole, B. & Ganguli, S. Continual learning through synaptic intelligence. In Proc. International Conference on Machine Learning, 3987-3995 (PMLR, 2017).   
34. Masse, N. Y., Grant, G. D. & Freedman, D. J. Alleviating catastrophic forgetting using context-dependent gating and synaptic stabilization. Proc. Natl. Acad. Sci. USA 115, E10467-E10475 (2018).   
35. Rebuffi, S.-A., Kolesnikov, A., Sperl, G. & Lampert, C. H. iCaRL: Incremental classifier and representation learning. Proc. IEEE Conf. Comput. Vis. Pattern Recognit. 5533-5542 (IEEE, 2017).   
36. Wang, F.-Y., Zhou, D.-W., Ye, H.-J. & Zhan, D.-C. FOSTER: Feature boosting and compression for class-incremental learning. In Proc. European Conference on Computer Vision, 398-414 (Springer, 2022).   
37. Ostoic, S. & Brunel, N. From spiking neuron models to linear-nonlinear models. PLoS Comput. Biol. 7, e1001056 (2011).   
38. Hunsberger, E. & Eliasmith, C. Spiking deep networks with LIF neurons. Preprint at https://arxiv.org/abs/1510.08829 (2015).   
39. Abbott, L. F. Lapicque's introduction of the integrate-and-fire model neuron (1907). Brain Res. Bull. 50, 303-304 (1999).   
40. Van de Ven, G. M., Siegelmann, H. T. & Tolias, A. S. Brain-inspired replay for continual learning with artificial neural networks. Nat. Commun. 11, 4069 (2020).   
41. Kim, G., Liu, B. & Ke, Z. A multi-head model for continual learning via out-of-distribution replay. Proceedings of the Conference on Life-long Learning Agents, 548-563 (PMLR, 2022).   
42. Ge, Y., Li, Y., Ni, S., Zhao, J., Yang, M.-H. & Itti, L. CLR: Channel-wise lightweight reprogramming for continual learning. Proc. IEEE/CVF Int. Conf. Comput. Vis. 18752-18762 (IEEE, 2023).   
43. Gonzalez, H. A. et al. SpiNNaker2: A large-scale neuromorphic system for event-based and asynchronous machine learning. Preprint at https://arxiv.org/abs/2401.04491 (2024).   
44. Orchard, G. et al. Efficient neuromorphic signal processing with Loihi 2. Proc. IEEE Workshop Signal Process. Syst. 254-259 (IEEE, 2021).   
45. Zhong, Y. et al. PAICORE: a 1.9-million-neuron 5.181-TSOPS/W digital neuromorphic processor with unified SNN-ANN and on-chip learning paradigm. IEEE J. Solid-State Circuits https://doi.org/10.1109/JSSC.2024.3426319 (2024).   
46. Deng, L. et al. Tianjic: a unified and scalable chip bridging spike-based and continuous neural computation. IEEE J. Solid-State Circuits 55, 2228-2246 (2020).   
47. Deng, L. et al. SemiMap: a semi-folded convolution mapping for speed-overhead balance on crossbars. IEEE Trans. Comput.-Aided Des. Integr. Circuits Syst. 39, 117-130 (2020).

48. Xu, M. et al. Adaptive synaptic scaling in spiking networks for continual learning and enhanced robustness. IEEE Trans. Neural Netw. Learn. Syst. https://doi.org/10.1109/TNNLS.2024.3373599 (2024).   
49. Zelinsky, A. Learning OpenCV—Computer vision with the OpenCV library. IEEE Robot. Autom. Mag. 16, 100-100 (2009).   
50. Redmon, J., Divvala, S., Girshick, R. & Farhadi, A. You only look once: Unified, real-time object detection. Proc. IEEE Conf. Comput. Vis. Pattern Recognit. 779-788 (IEEE, 2016).   
51. Wang, L., Xie, J., Zhang, X., Su, H. & Zhu, J. HIDe-PET: continual learning via hierarchical decomposition of parameter-efficient tuning. Preprint at https://arxiv.org/abs/2407.05229 (2024).   
52. Xu, X., Xu, D. & Qin, F. A new diagnosis method with few-shot learning based on a class-rebalance strategy for scarce faults in industrial processes. Mach. Intell. Res. 20, 583-594 (2023).   
53. Fang, A. et al. Data determines distributional robustness in contrastive language image pre-training (CLIP). Proc. Int. Conf. Mach. Learn. (PMLR, 2022).   
54. Shi, Q. et al. Hybrid neural networks for continual learning inspired by corticohippocampal circuits. Zenodo (2024).

# Acknowledgements

This work was partly supported by the National Key Research and Development Program of China (No.2021ZD0200300) and National Nature Science Foundation of China (No. 62088102). We would like to thank Fangwen Yu, Shangqi Guo, Hao Zheng, Lukai Li, Liyuan Wang, and Zhenkun Zhang for valuable discussion.

# Author contributions

Q.S. and F.L. conceived the study, performed the experiments, and analyzed the results. G.L. and H.L. conducted the hardware implementation. Under the leadership of R.Z., all authors participated in discussions on model and experiment design. Q.S., R.Z., and F.L. contributed to the writing of this paper. R.Z. and L.S. supervised the whole project.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-025-56405-9.

Correspondence and requests for materials should be addressed to Rong Zhao.

Peer review information Nature Communications thanks the anonymous, reviewer(s) for their contribution to the peer review of this work. A peer review file is available.

Reprints and permissions information is available at

http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

© The Author(s) 2025