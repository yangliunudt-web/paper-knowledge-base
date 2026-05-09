---
title: "Class-Incremental Learning: A Survey"
authors:
  - "Da-Wei Zhou"
  - "Qi-Wei Wang"
  - "Zhi-Hong Qi"
  - "Han-Jia Ye"
  - "De-Chuan Zhan"
  - "Ziwei Liu"
date: "2024-01-01"
year: "2024"
journal: "IEEE TPAMI"
doi: "10.1109/TPAMI.2024.3369262"
abstract: "Deep models, e.g., CNNs and Vision Transformers, have achieved impressive achievements in many vision tasks in the closed world. However, novel classes emerge from time to time in our ever-changing world, requiring a learning system to acquire new knowledge continually. Class-Incremental Learning (CIL) enables the learner to incorporate the knowledge of new classes incrementally and build a universal classifier among all seen classes. Correspondingly, when directly training the model with new class instances, a fatal problem occurs — the model tends to catastrophically forget the characteristics of former ones, and its performance drastically degrades. There have been numerous efforts to tackle catastrophic forgetting in the machine learning community. In this paper, we survey comprehensively recent advances in class-incremental learning and summarize these methods from several aspects. We also provide a rigorous and unified evaluation of 17 methods in benchmark image classification tasks to find out the characteristics of different algorithms empirically. Furthermore, we notice that the current comparison protocol ignores the influence of memory budget in model storage, which may result in unfair comparison and biased results. Hence, we advocate fair comparison by aligning the memory budget in evaluation, as well as several memory-agnostic performance measures. The source code is available at https://github.com/zhoudw-zdw/CIL_Survey/. Index Terms—Class-Incremental Learning, Continual Learning, Lifelong Learning, Catastrophic Forgetting"
keywords:
  - "[[Class-Incremental Learning]]"
  - "[[Continual Learning]]"
  - "[[Catastrophic Forgetting]]"
  - "[[Lifelong Learning]]"
cite: "[1] Zhou et al. Class-Incremental Learning: A Survey[J]. IEEE TPAMI, 2024."
aiSum: "类增量学习综述：全面总结 CIL 方法，对 17 种方法进行基准评估，倡导基于内存预算的公平比较和内存无关的性能度量。"
confidence: "medium"
wiki_concepts:
  - "[[Catastrophic forgetting]]"
  - "[[Continual learning]]"
---

# Class-Incremental Learning: A Survey

Da-Wei Zhou, Qi-Wei Wang, Zhi-Hong Qi, Han-Jia Ye, De-Chuan Zhan, Ziwei Liu

Abstract—Deep models, e.g., CNNs and Vision Transformers, have achieved impressive achievements in many vision tasks in the closed world. However, novel classes emerge from time to time in our ever-changing world, requiring a learning system to acquire new knowledge continually. Class-Incremental Learning (CIL) enables the learner to incorporate the knowledge of new classes incrementally and build a universal classifier among all seen classes. Correspondingly, when directly training the model with new class instances, a fatal problem occurs — the model tends to catastrophically forget the characteristics of former ones, and its performance drastically degrades. There have been numerous efforts to tackle catastrophic forgetting in the machine learning community. In this paper, we survey comprehensively recent advances in class-incremental learning and summarize these methods from several aspects. We also provide a rigorous and unified evaluation of 17 methods in benchmark image classification tasks to find out the characteristics of different algorithms empirically. Furthermore, we notice that the current comparison protocol ignores the influence of memory budget in model storage, which may result in unfair comparison and biased results. Hence, we advocate fair comparison by aligning the memory budget in evaluation, as well as several memory-agnostic performance measures. The source code is available at https://github.com/zhoudw-zdw/CIL_Survey/.

Index Terms—Class-Incremental Learning, Continual Learning, Lifelong Learning, Catastrophic Forgetting

# 1 INTRODUCTION

R ECENT years have witnessed the rapid progress of deeplearning, where neural networks have achieved or even learning,where neural networks have achieved or even surpassed human-level performances in many fields [1], [2], [3]. The typical training process of a deep network requires precollected datasets in advance, e.g., large-scale images or texts — the network undergoes the training process of the pre-collected dataset multiple epochs. However, training data is often with stream format in the open world [4]. These streaming data cannot be held for long due to storage constraints [5] or privacy issues [6], requiring the model to be updated incrementally with only new class instances. Such requirements trigger the prosperity of the Class-Incremental Learning (CIL) field, aiming to continually build a holistic classifier among all seen classes. The fatal problem in CIL is called catastrophic forgetting, i.e., directly optimizing the network with new classes will erase the knowledge of former ones and result in irreversible performance degradation. Hence, how to effectively resist catastrophic forgetting becomes the core problem in building CIL models.

Figure 1 depicts the typical setting of CIL. Training data emerge sequentially in the stream format. In each timestamp, we can get a new training dataset (denoted as ‘task’ in the figure) and need to update the model with the new classes. For example, the model learns ‘birds’ and ‘dogs’ in the first task, ‘tigers’ and ‘fish’ in the second task, ‘monkeys’ and ‘sheep’ in the third task, etc. Afterward,

This work is partially supported by National Science and Technology Major Project (2022ZD0114805), Fundamental Research Funds for the Central Universities (2024300373), NSFC (62376118, 62006112, 62250069, 61921006), Collaborative Innovation Center of Novel Software Technology and Industrialization, China Scholarship Council, Ministry of Education, Singapore, under its MOE AcRF Tier 2 (MOET2EP20221- 0012), NTU NAP, and under the RIE2020 Industry Alignment Fund – Industry Collaboration Projects (IAF-ICP) Funding Initiative. (Corresponding authors: H.-J. Ye and Z. Liu.)   
D.-W. Zhou, Q.-W. Wang, Z.-H. Qi, H.-J. Ye, and D.-C. Zhan are with School of Artificial Intelligence, Nanjing University, and National Key Laboratory for Novel Software Technology, Nanjing University, Nanjing, 210023, China; E-mail: {zhoudw, wangqiwei, qizh, yehj, zhandc}@lamda.nju.edu.cn   
Work done when D.-W. Zhou was a visiting scholar at NTU.   
Z. Liu is with S-Lab, College of Computing and Data Science, Nanyang Technological University, Singapore, 639798. E-mail: ziwei.liu@ntu.edu.sg

![](images/114573d8cce4c0e2f7b29760809c61ef27362595796236a7adb2751e7531cb6b.jpg)  
Figure 1: The setting of CIL. Non-overlapping classes arrive sequentially, and the model needs to learn to classify all the classes incrementally. After learning each task, the model is evaluated among all seen classes. An ideal model should perform well in the newly learned classes and remember the former without forgetting.

the model is tested among all seen classes to evaluate whether it has discrimination for them. A good model should strike a balance between depicting the characteristics of new classes and preserving the pattern of formerly learned old classes. This trade-off is also known as the ‘stability-plasticity dilemma’ in neural system [7], where stability denotes the ability to maintain former knowledge and plasticity represents the ability to adapt to new patterns.

Since the data stream comes continually and requires training a lifelong time, incremental learning is also known as ‘continual learning’ [6] or ‘lifelong learning’ [9]. We interchangeably use these concepts in this paper. Apart from class-incremental learning, there are other fine-grained settings addressing the incremental learning problem, e.g., Task-Incremental Learning (TIL) and Domain-Incremental Learning (DIL) [8]. We show these three protocols in Figure 2. TIL is a similar setting to CIL, and both of them observe incoming new classes in new tasks. However, the difference lies in the inference stage, where CIL requires the model to differentiate among all classes. By contrast, TIL only requires classifying the instance among the corresponding task space. In other words, it does not require cross-task discrimination

![](images/c921749b232691760a6d51d117807e0aabf6c0a8be364b7736cee8fbfa65a966.jpg)  
Bird or Dog or Tiger or Fish?

![](images/52b8560facc2a98ffe5f9506f4871e78efb5f626ae438b31a411864e7243944e.jpg)  
Bird or Dog ? Tiger or Fish ?

![](images/607b7bb2466d183f631616f0f7f48fd643f780223efba72760931a2ea79cc65a.jpg)  
Bird or Dog ?   
Figure 2: The setting of Class-Incremental Learning (CIL), Task-Incremental Learning (TIL), and Domain-Incremental Learning (DIL). CIL and TIL share the same training protocol, while TIL is much easier during inference, i.e., only requiring classifying among corresponding label spaces. DIL refers to the data stream with distribution change, where new tasks contain the same classes from different domains, e.g., cartoon and clip-art. The distinction of these scenarios is proposed by [8].

ability. Hence, TIL is easier than CIL, which can be seen as a particular case of CIL. On the other hand, DIL concentrates on the scenario with concept drift or distribution change [10], where new tasks contain instances from different domains but with the same label space. In this case, new domains correspond to the images in clip-art format. In this paper, we concentrate on the CIL setting, which is a more challenging scenario in the open world.

There is also research about CIL before the prosperity of deep learning [11]. Typical methods try to solve the catastrophic forgetting problem with traditional machine learning models. However, most of them address the incremental learning within two tasks, i.e., the model is only updated with a single new stage [12], [13]. Furthermore, the rapid development of data collection and processing requires the model to grasp long-term and massivescale data streams that traditional machine learning models cannot handle. Correspondingly, deep neural networks with powerful representation ability well suit these requirements. As a result, deep learning-based CIL is becoming a hot topic in the machine learning and computer vision community.

There are several related surveys discussing the incremental learning problem. For example, [6] focuses on the task-incremental learning problem and provides a comprehensive survey. [14] is a related survey on the class-incremental learning field, while it only discusses and evaluates the methods till 2020. However, with the rapid development of the CIL field, many great works are emerging day by day, which substantially boost the performance of benchmark settings [15], [16], [17], [18]. On the other hand, with the prosperity of Vision Transformer (ViT) [19] and pre-trained models, a heated discussion about ViT in CIL is attracting the attention of the community. Other surveys either focus on the specific field [20], [21] or lack the performance evolution among state-of-the-arts [8], [22], [23]. Hence, it is urgent to provide an up-to-date survey containing popular methods to speed up the development of the CIL field.

In this paper, we aim for a comprehensive review of classincremental learning methods and divide them into seven categories. We also provide a holistic comparison among different kinds of methods over benchmark datasets, i.e., CIFAR100 [24] and ImageNet100/1000 [25]. On the other hand, we highlight an important factor in CIL model evaluation, i.e., memory budget, and advocate fair comparison among different methods with an aligned budget. Correspondingly, we holistically evaluate the extensibility of CIL models with budget-agnostic measures.

In general, the contribution of this survey can be summarized as follows: 1): We provide a comprehensive survey of CIL, including problem definitions, benchmark datasets, and different families of CIL methods. We organize these algorithms taxonomically (Table 1)

and chronologically (Figure 3) to give a holistic overview of stateof-the-art. 2): We provide a rigorous and unified comparison among different methods on several publicly available datasets, including traditional CNN-backed and modern ViT-backed methods. We also discuss the insights and summarize the common rules to inspire future research. 3): To boost real-world applications, CIL models should be deployed not only on high-performance computers but also on edge devices. Therefore, we advocate evaluating different methods holistically by emphasizing the effect of memory budgets. Correspondingly, we provide a comprehensive evaluation of different methods given specific budgets as well as several new performance measures.

# 2 PRELIMINARIES

# 2.1 Problem Formulation

Definition 1. Class-Incremental Learning aims to learn from an evolutive stream with new classes. Assume there is a sequence of B training task $s ^ { 1 } \left\{ \mathcal { D } ^ { 1 } , \mathcal { D } ^ { 2 } , \cdots , \mathcal { D } ^ { B } \right\}$ without overlapping classes, where $\mathbf { \check { \mathcal { D } } } ^ { b } = \mathbf { \check { \{ } } ( \check { x }  _ { i } ^ { b } , y _ { i } ^ { b } ) \mathbf  \dot { \} } _ { i = 1 } ^ { n _ { b } }$ 1 is the b-th incremental step with $n _ { b }$ training instances. $\mathbf { x } _ { i } ^ { b } \in \mathbb { R } ^ { D }$ is an instance of class $y _ { i } ^ { b } \in Y _ { b } , Y _ { b }$ is the label space of task b, where $Y _ { b } \cap Y _ { b ^ { \prime } } = \emptyset f o r b \neq b ^ { \prime }$ . We can only access data from $\mathcal { D } ^ { b }$ when training task b. The ultimate goal of CIL is to continually build a classification model for all classes. In other words, the model should not only acquire the knowledge from the current task $\mathcal { D } ^ { b }$ but also preserve the knowledge from former tasks. After each task, the trained model is evaluated over all seen classes $\mathcal { V } _ { b } = Y _ { 1 } \cup \cdot \cdot \cdot Y _ { b }$ . Formally, CIL aims to fit a model $f ( \mathbf { x } ) : X \to \mathcal { V } _ { b }$ , which minimizes the expected risk:

$$
f ^ {*} = \underset {f \in \mathcal {H}} {\operatorname {a r g m i n}} \mathbb {E} _ {(\mathbf {x}, y) \sim \mathcal {D} _ {t} ^ {1} \cup \dots \mathcal {D} _ {t} ^ {b}} \mathbb {I} (y \neq f (\mathbf {x})), \tag {1}
$$

where H is the hypothesis space, I(·) is the indicator function which outputs 1 if the expression holds and 0 otherwise. Dbt denotes the data distribution of task b. A good CIL model satisfying Eq. 1 has discriminability among all classes, which not only works well on new classes but also preserves the knowledge of former ones.

Class Overlapping: Typical CIL setting assumes $Y _ { b } \cap Y _ { b ^ { \prime } } = \emptyset$ for $b \neq b ^ { \prime } , i . e .$ , there are no overlapping classes in different tasks. However, in the real world, it is common to observe the old classes emerging in new tasks. When $Y _ { b } \cap Y _ { b ^ { \prime } } \neq \emptyset$ , the setting is called blurry class-incremental learning (Blurry CIL) [26]. It enables the model to revisit former instances in the later stage, which weakens the learning difficulty.

Number of Instances: Typical CIL setting assumes the training data of each class is balanced and many-shot (e.g., hundreds or

thousands). However, the data collection may face challenges in the real world, $e . g .$ , we can only collect a limited number of training instances for rare birds. When the training instances of new classes are limited $( e . g .$ , 5-shot per class), the setting is called Few-Shot Class-Incremental Learning (FSCIL) [27]. When the training instances are highly imbalanced and long-tailed, the setting is called Long-Tailed Class-Incremental Learning (LTCIL) [28]

Online CIL: Although data comes with stream format, the model can conduct multi-epoch training with each task, $i . e . ,$ , offline training within each task. There are some works addressing fully online (one-pass) CIL, where each batch can be processed once and then dropped [29]. It is a specific case of the current setting, and we concentrate on the generalized CIL setting in this paper.

In the following discussions, we decompose the CIL model into the embedding module and linear layers, $\bar { i . e . , f ( \mathbf { x } ) } = W ^ { \top } \phi ( \mathbf { x } ) . \big \rbrace \big .$ where $\phi ( \cdot ) : \mathbf { \bar { \mathbb { R } } } ^ { D } \to \mathbb { R } ^ { d } , W \in \dot { \mathbb { R } } ^ { d \times | \mathcal { V } _ { b } | }$ . The linear layer can be further decomposed into the combination of classifiers: $W =$ $[ { \pmb w } _ { 1 } , { \pmb w } _ { 2 } , \cdots , { \pmb w } _ { | { \mathcal { V } } _ { b } | } ]$ , where $\boldsymbol { w } _ { k } \in \mathbb { R } ^ { d } , | \cdot |$ | denotes the size of the set. The logits are then passed to the Softmax activation for further optimization, i.e., the output probability on class k is denoted as:

$$
\mathcal {S} _ {k} (f (\mathbf {x})) = \frac {\exp \mathbf {w} _ {k} ^ {\top} \phi (\mathbf {x}) / \tau}{\sum_ {j = 1} ^ {| \mathcal {Y} _ {b} |} \exp \mathbf {w} _ {j} ^ {\top} \phi (\mathbf {x}) / \tau}, \tag {2}
$$

where $\tau$ is the temperature parameter.

Backbones: As defined in Eq. 2, the predictions are derived by feeding instance x into the embedding function and linear layer. The embedding function is designed to project input instances into the embedding space to reflect its semantic information. Hence, ideal CIL algorithms should work for any type of backbones, e.g., multi-layer perceptron (MLP) [30], convolutional neural network (CNN) [31], and Vision Transformer (ViT) [19]. Specifically, we often treat the whole image as the input of MLP and CNN and utilize the final product as the embedding. By contrast, ViT transforms the image into a sequence of patches for patch features. These patches are then fed forward to the self-attention modules [32] and MLP layer to get the contextualized information. Typical ViT appends an extra token $( i . e .$ , [CLS] token) to the set of patches and utilizes the final representation of [CLS] token as the embedding. Since ViT relies on the self-attention mechanism to relate and adjust patch-wise features, it is intuitive to influence the embedding context by adding task-specific tokens as the input. The basic difference between these backbones triggers different tuning algorithms in CIL, which will be further discussed in Section 3.3. Baseline in CIL: In CIL, the typical baseline is sequential finetuning the model with the current dataset $\mathcal { D } ^ { b }$ (denoted as ‘Finetune’), whose loss function can be denoted as:

$$
\mathcal {L} = \sum_ {(\mathbf {x}, y) \in \mathcal {D} ^ {b}} \ell (f (\mathbf {x}), y), \tag {3}
$$

where $\ell ( \cdot , \cdot )$ measures the discrepancy between inputs, e.g., crossentropy loss. Finetune is known as the baseline method for CIL since it only concentrates on learning the new concepts in the current task. Consequently, it suffers severe forgetting since the model pays no attention to former ones.

# 2.2 Exemplars and Exemplar Set

As defined in Definition 1, in each incremental task, the model can only access the current dataset $\mathcal { D } ^ { b }$ . This helps to preserve user privacy and release the storage burden. However, this restriction is

2. We omit the bias term for ease of discussions.

relaxed in some cases, and the model can keep a relatively small set, namely exemplar set, to reserve the representative instances from former tasks.

Definition 2. Exemplar $\mathbf { S e } \ P $ is an extra collection of instances from former tasks $\mathcal { E } = \{ ( \mathbf { x } _ { j } , \overline { { \boldsymbol { y } _ { j } } } ) \} _ { j = 1 } ^ { M } , \boldsymbol { y } _ { j } \in \mathcal { V } _ { b - 1 }$ . With the help of the exemplar set, the model can utilize $\mathcal { E } \cup \mathcal { D } ^ { b }$ for the update within each task. The model manages the exemplar set after the training process of each task.

Exemplar Set Management: Since the data stream is evolving, there are two main strategies to manage the exemplar set in CIL [89]. The first way is to keep a fixed number of exemplars per class, e.g., R per class. Under such circumstances, the size of the exemplar set will grow as the data stream evolves — the model keeps $R | \mathcal { V } _ { b } |$ after the b-th task. This will result in a linearly growing memory budget, which is inapplicable in real-world learning systems. To this end, another strategy advocates saving a fixed number of exemplars, e.g., M . The model keeps $[ \frac { M } { | \mathcal { V } _ { b } | } ]$ instances per class, where $[ \cdot ]$ denotes floor function. It helps to keep a fixed size of exemplars in the memory and release the storage burden. In this paper, we use the second strategy to organize the exemplar set. Exemplar Selection: Exemplars are representative instances of each class, which need to be selected from the entire training set. An intuitive way to choose the exemplars is random sampling, which results in diverse instances. By contrast, a commonly used strategy is called herding [82], [124], aiming to select the most representative ones of each class. Given the instance set $X = \{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \cdot \cdot \cdot , \mathbf { x } _ { n } \}$ from class $y ,$ herding first calculates the class center with current embedding ω(·): $\textstyle \mu _ { y } \gets { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } \phi ( \mathbf { x } _ { i } )$ Afterward, it iteratively appends instances into the exemplar set:

$$
\boldsymbol {p} _ {k} \leftarrow \underset {\mathbf {x} \in X} {\operatorname {a r g m i n}} \left\| \boldsymbol {\mu} _ {y} - \frac {1}{k} \left[ \phi (\mathbf {x}) + \sum_ {j = 1} ^ {k - 1} \phi \left(\boldsymbol {p} _ {j}\right) \right] \right\|, \tag {4}
$$

until k reaches the memory bound of each class $( \left[ \frac { M } { | \mathcal { V } _ { b } | } \right] )$ . The exemplar set of class y is the concatenation of $\{ p _ { 1 } , p _ { 2 } , \cdot \cdot \cdot p _ { [ \frac { M } { | \mathcal { V } _ { h } | } ] } \}$ bEq. 4 ensures that the average feature vector over all exemplars selected thus far is closest to the class mean. Since the class center can be seen as the most representative pattern of each class, selecting exemplars near the center also enhances the representativeness. Herding is now a commonly used strategy to select exemplars in CIL, and we also adopt it in this paper.

# 3 CLASS-INCREMENTAL LEARNING: TAXONOMY

There are numerous works addressing CIL in recent years, raising a heated discussion among machine learning and computer vision society. We organize these methods taxonomically from seven aspects, as shown in Table 1. Specifically, data replay and data regularization concentrate on solving CIL with exemplars, either by revisiting former instances or using them as indicators to regularize model updating. Dynamic networks expand the network structure for stronger representation ability, while parameter regularizationbased methods regularize the model parameters to prevent them from drifting away to resist forgetting. Moreover, knowledge distillation builds the mapping between incremental models to resist forgetting, and model rectification aims to reduce the biased prediction of incremental learners. Template-based classification aims to transform inference into query-template matching. We list the representative methods chronologically in Figure 3 to show the research focus of different periods.

3. Also known as the ‘replay buffer’ and ‘memory buffer.’

Table 1: The taxonomy of CIL. The shade color in the last column denotes the subcategory, which is consistent with Figure 3.   

<table><tr><td colspan="2">Algorithm Category</td><td>Reference</td></tr><tr><td rowspan="2">§3.1
Data Replay</td><td>Direct Replay</td><td>[26, 33, 34, 35, 36, 37, 38, 39, 40]</td></tr><tr><td>Generative Replay</td><td>[41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]</td></tr><tr><td colspan="2">§3.2 Data Regularization</td><td>[34, 53, 54, 55, 56, 57, 58]</td></tr><tr><td rowspan="3">§3.3
Dynamic Networks</td><td>Neuron Expansion</td><td>[45, 59, 60, 61]</td></tr><tr><td>Backbone Expansion</td><td>[15, 16, 17, 62, 63, 64, 65, 66, 67, 68]</td></tr><tr><td>Prompt Expansion</td><td>[18, 69, 70, 71, 72]</td></tr><tr><td colspan="2">§3.4 Parameter Regularization</td><td>[33, 73, 74, 75, 76, 77, 78, 79, 80]</td></tr><tr><td rowspan="3">§3.5
Knowledge Distillation</td><td>Logit Distillation</td><td>[81, 82, 83, 84, 85, 86, 87, 88]</td></tr><tr><td>Feature Distillation</td><td>[89, 90, 91, 92, 93, 94, 95, 96, 97, 98]</td></tr><tr><td>Relational Distillation</td><td>[27, 99, 100, 101, 102, 103]</td></tr><tr><td rowspan="3">§3.6
Model Rectify</td><td>Feature Rectify</td><td>[104, 105, 106, 107, 108, 109]</td></tr><tr><td>Logit Rectify</td><td>[83, 89, 110, 111]</td></tr><tr><td>Weight Rectify</td><td>[112, 113, 114]</td></tr><tr><td colspan="2">§3.7 Template-Based Classification</td><td>[37, 82, 104, 115, 116, 117, 118, 119, 120, 121, 122, 123]</td></tr></table>

Note that the classification rules of these categories are based on the ‘key point’ (or the special focus) of each algorithm. With the rapid development of class-incremental learning, some techniques are becoming the well-acknowledged baseline to be shared among a variety of algorithms. Hence, these seven categories are not mutually exclusive, and there is no strict boundary between them. We organize them into several categories to enhance a holistic understanding of CIL from a specific perspective. In the following sections, we will discuss CIL methods from these aspects.

# 3.1 Data Replay

‘Replay’ is important in human cognition system [125], [126], [127] — a student facing final exams shall go over the textbooks to recall former memory and knowledge. This phenomenon can also be extended to the network training process, where a network can overcome catastrophic forgetting by revisiting former exemplars. Correspondingly, an intuitive way [82], [128] is to save an extra exemplar set E (as defined in Definition 2) and include it into the model updating process:

$$
\mathcal {L} = \sum_ {(\mathbf {x}, y) \in \left(\mathcal {D} ^ {b} \cup \mathcal {E}\right)} \ell (f (\mathbf {x}), y). \tag {5}
$$

Comparing Eq. 5 to Eq. 3, we can find that exemplars are concatenated to the training set for updating, enabling the retrospective review of former knowledge when learning new concepts.

Hot to construct the exemplar set? Utilizing the exemplar set for rehearsal is simple yet effective, which leads to numerous following works. The exemplar sampling process is also similar to the active learning protocol, and some works propose corresponding sampling measures to select the informative ones. For example, [33] suggests sampling exemplars with high prediction entropy and near the decision boundary. The model will achieve higher generalization ability by replaying these ‘hard’ exemplars. [26] proposes estimating exemplars’ uncertainty via data augmentation. They choose instances with large prediction diversity by aggregating the predictions of multiple augmented instances. Similarly, [34] proposes to sample exemplars with a greedy strategy in online incremental learning. It proves that exemplar selection is equivalent to maximizing the diversity of exemplars with parameters gradient as the feature. Without explicit task boundaries, [35]

explores the reservoir sampling process to ensure the exemplars are i.i.d. sampled. [36] formulates the replay process into a bilevel optimization and keeps intact predictions on some anchor points of past tasks. [37] introduces data replay in prototypical network [129], and utilizes the exemplars as pseudo-prototypes for embedding evaluation. Mnemonics [40] proposes a way to parameterize exemplars and optimize them in a meta-learning manner. The framework is trained through bi-level optimizations, i.e., model-level and exemplar-level, which can be combined with various CIL algorithms.

Memory-efficient memory: Since exemplars are raw images, directly saving a set of instances may consume enormous memory costs. To this end, several works are proposed to build a memoryefficient replay buffer [17]. [38] argues that extracted features have lower dimensions than raw images and proposes saving features in the exemplar set to release the burden. Similarly, [39] proposes keeping low-fidelity images instead of raw ones. However, since the distributions of extracted features and low-fidelity images may differ from the raw images, an extra adaptation process is needed for these methods, adding to the algorithm’s complexity.

Generative replay: The above-mentioned methods achieve competitive performance by replaying former instances in the memory. Apart from directly saving instances in the exemplar set, generative models show the potential to model the distribution and generate instances [153], [154], which have also been applied to classincremental learning. We denote the aforementioned methods directly saving instances for replay as ‘direct replay,’ and the methods utilizing generative models as ‘generative replay.’

There often exist two models in generative replay-based CIL, i.e., the generative model for data generation and the classification model for prediction. GR [41] firstly proposes to utilize the generative adversarial network (GAN) [153] in CIL. In each updating process, it utilizes the GAN to generate the instances from former classes and then updates GAN and classification model with both old and new classes. ESGR [42] extends GR by saving extra exemplars. It also proposes to train a separate GAN for each incremental task, which does not require updating GAN incrementally. [43] extends GR by introducing the dynamic parameter generator for model adaptation at test time. FearNet [44]

![](images/d1f4385fc4203f343bbdbd85aad6bbd67b9de8ed762449f7d98e49cb24b1c13f.jpg)  
Figure 3: The roadmap of class-incremental learning. We organize representative methods chronologically to show the concentration at different stages. Different colors of these methods denote the sub-categories in Table 1. Knowledge distillation and data replay dominated the research before 2021, while model rectify and dynamic networks became popular after 2021.

explores brain-inspired CIL and uses a dual-memory system in which new memories are consolidated from a network for recent memories. Recently, [45], [46], [47] explore the application of conditional GAN [155] in CIL, and [48] adopts variational autoencoders (VAE) [154] to model data distribution. Similarly, [49], [50] model each class into a Gaussian distribution and sample instances directly from the class center. With the prosperity of diffusion models [156], recent works also consider using diffusion models as the data generator for high-quality samples. Correspondingly, SDDR [51] studies the use of a pre-trained diffusion model as a complementary source of data. Similarly, DDGR [52] adopts a diffusion model as the generator and calculates an instruction operator through the classifier to instruct the generation of samples. There are also works [157], [158] on solving the catastrophic forgetting of these diffusion models.

Discussions: Direct replay is a simple yet effective strategy, which has been widely applied to camera localization [159], semantic segmentation [160], video classification [161], and action recognition [91]. Since it directly optimizes the loss over old exemplars, it is found to help continual learners stay in the lowloss region of prior tasks during the optimization strategy [162] However, since the exemplar set only saves a tiny portion of the training set, data replay may suffer the overfitting problem and weaken the generalizability [53], [162]. Considering repeated optimization on a small pool of data inevitably leads to tight and unstable decision boundaries, several works tackle this problem by constraining the model’s layer-wise Lipschitz constants with regard to exemplars [163] or enlarging representational variations to alleviate representation collapse [164]. Besides, the data-imbalance problem [165] also occurs due to the gap between the few-shot exemplars and the many-shot training set. Iteratively optimizing the imbalanced training set introduces extra bias in the classifier, and several works address this problem with balanced sampling [16], [110]. Finally, since direct replay requires saving exemplars of former classes, it will face privacy issues when the raw data contains face images or resource deficiency when the raw data contains images of rare animals [27]. Under such circumstances, algorithms should be designed to learn without exemplars [49] or

using privacy-friendly strategies like feature replay [50].

On the other hand, the performance of generative replay methods relies on the quality of generated data. They are found to work well on simple datasets [166], [167] while failing in complex, largescale inputs [168]. To tackle this problem, some works find generating features is much easier than generating raw images in terms of computational complexity and semantic information. Hence, they either utilize conditional GAN to generate features [169] or VAE to model the internal representations [166]. Additionally, recent advances in diffusion models reveal a promising way to generate instances with pre-trained diffusion models [51], while utilizing pre-trained models leads to an unfair comparison to other methods without extra information. Furthermore, when sequentially updating the generative model, the catastrophic forgetting phenomena can also be observed on these generative models [157], [158]. As a result, algorithms should be designed to address catastrophic forgetting in two aspects (i.e., classifier aspect and generative model aspect) when using generative replay.

# 3.2 Data Regularization

Apart from directly replaying former data, another group of works tries to regularize the model with former data and control the optimization direction. Since learning new classes will result in the catastrophic forgetting of old ones, the intuitive idea is to ensure that optimizing the model for new classes will not hurt former ones. GEM [53] aims to find the model that satisfies:

$$
f ^ {*} = \underset {f \in \mathcal {H}} {\operatorname {a r g m i n}} \sum_ {(\mathbf {x}, y) \in \mathcal {D} ^ {b}} \ell (f (\mathbf {x}), y) \tag {6}
$$

$$
\text {s . t .} \sum_ {(\mathbf {x} _ {j}, y _ {j}) \in \mathcal {E}} \ell \left(f (\mathbf {x} _ {j}), y _ {j}\right) \leq \sum_ {(\mathbf {x} _ {j}, y _ {j}) \in \mathcal {E}} \ell \left(f ^ {b - 1} (\mathbf {x} _ {j}), y _ {j}\right),
$$

where $f ^ { b - 1 }$ stands for the incremental model after training the last task $\dot { \mathcal Ḋ D Ḍ } ^ { b - 1 }$ . Eq. 6 optimizes the model with a restriction, which requires the loss calculated with the exemplar set not to exceed the former model. Since exemplars are representative instances from former classes, GEM strikes a balance between learning

new classes and preserving former knowledge. Furthermore, it transforms the constraints in Eq. 6 into:

$$
\langle g, g _ {o l d} \rangle := \left\langle \frac {\partial \ell (f (\mathbf {x}) , y)}{\partial \theta}, \frac {\partial \ell (f , \mathcal {E})}{\partial \theta} \right\rangle \geq 0, \tag {7}
$$

where $g , g _ { o l d }$ denotes the gradients of the current updating step and exemplar set, respectively. Eq. 7 requires the angle between gradients to be acute. If all the inequality constraints are satisfied, then the proposed parameter update is unlikely to increase the loss of previous tasks. However, if violations occur, GEM proposes to project the gradients g to the closest gradient g˜ satisfying the constraints. GEM further transforms the optimization into a Quadratic Program (QP) problem. However, since the regularization in Eq. 7 is defined among all exemplars, it requires calculating loss among exemplar sets and solving the QP problem in each optimization step. Hence, optimizing GEM is very time-consuming. To this end, A-GEM [54] is proposed to speed up the optimization by relaxing the constraints in Eq. 7 into a random batch. A similar idea is also adopted in [34].

There are other methods to address the regularization problem with exemplars. For example, Adam-NSCL [55] proposes to sequentially optimize network parameters by projecting the candidate parameter update into the approximate null space of all previous tasks. OWM [56] only allows weight modification in the direction orthogonal to the subspace spanned by all previously learned inputs. LOGD [57] further decomposes the gradients into shared and taskspecific ones. In model updating, the gradient should be close to the gradient of the new task, consistent with the gradients shared by all old tasks, and orthogonal to the space spanned by the gradients specific to the old tasks.

Discussions: Data regularization methods utilize the exemplar set in another manner, i.e., treating the loss of them as the indicator of forgetting. They assume that the loss on exemplars is consistent with the prior tasks and align the parameter updates with the direction of the exemplar set. Hence, previous knowledge can be preserved for these exemplars due to the aligned gradient direction. However, these assumptions may not stand in some cases [54], which results in poor performance. To this end, [170] gets rid of the requirement of exemplars and manually projects the gradient direction to be orthogonal with previous ones. On the other hand, some works assume the updating rule can be metalearned [171], [172] from a series of related tasks. MER [58] regularizes the objective of data replay so that gradients on incoming examples are more likely to have transferability and less likely to have interference with respect to past examples. iTAML [173] separates the generic feature extraction module from the task-specific classifier, thereby minimizing interference and promoting a shared feature space among tasks. [174] extends data replay with adversarial attack and meta-learns an adaptive fusion module to help allocate capacity to the knowledge of different difficulties.

Moreover, since data regularization and data replay both need to save previous data in the memory, similar problems will also occur in data regularization-based methods, e.g., overfitting, generalization issues [53], [162], and privacy concerns [149] Consequently, it would be interesting to design privacy-friendly algorithms to build the regularization term with intermediate products for real-world applications.

![](images/5f88dbdd4621482a732b1e94d06ce1be6213016316163236f47ab32e43ad1508.jpg)  
Figure 4: Illustration of network structure evolving in backbone expansion. Left: DER expands a new backbone per incremental task. Middle: FOSTER adds an extra model compression stage, which maintains limited model storage. Right: MEMO decouples the network structure and only expands specialized blocks.

# 3.3 Dynamic Networks

Deep neural networks are proven to produce task-specific features [175]. For example, when the training dataset contains ‘cars,’ the model tends to depict the wheels and windows. However, if the model is updated with new classes containing ‘cats,’ the features would be adapted for beards and stripes. Since the capacity of a model is limited, adapting to new features will result in the overwriting of old ones and forgetting [59]. Hence, utilizing the extracted features for beards and strides is inefficient for recognizing a car. To this end, dynamic networks are designed to dynamically adjust the model’s representation ability to fit the evolving data stream. There are several ways to expand representation ability, and we divide them into three sub-groups, i.e., neuron expansion, backbone expansion, and prompt expansion.

# 3.3.1 Neuron Expansion

Early works focus on neuron expansion adding neurons when the representation ability is insufficient to capture new classes. DEN [59] formulates the adjusting process into selection, expansion, duplication, and elimination. Facing a new incremental task, the model first selectively retrains the neurons that are relevant to this task. If the retrained loss is still above some threshold, DEN considers expanding new neurons top-down and eliminating the useless ones with group-sparsity regularization. Afterward, it calculates the neuron-wise drift and duplicates neurons that drift too much from the original values. Apart from heuristically expanding and shrinking the network structure, RCL [60] formulates the network expansion process into a reinforcement learning problem and searches for the best neural architecture for each incoming task. Similarly, Neural Architecture Search (NAS) [176] is also adopted to find the optimal structure for each of the sequential tasks [61].

# 3.3.2 Backbone Expansion

Expanding neurons shows competitive results with expandable representation. Correspondingly, several works try to duplicate the backbone network for stronger representation ability. PNN [62] proposes learning a new backbone for each new task and fixing the former in incremental learning. It also adds layer-wise connections between old and new models to reuse former features. Expert Gate [63] also expands the backbone per incremental task while it requires learning an extra gate to map the instance to the most suitable pathway during inference. To release the expansion cost, P&C [64] suggests a progression-compression protocol — it first expands the network to learn representative representations. Afterward, a compression process is conducted to control the total budget. AANets [66] partially expands stable and plastic blocks and aggregates their predictions to enhance model’s representation

ability. [65], [67] maintain a dual-branch network for classincremental learning, one for fast adaptation and one for slow adaption. Recently, DER [15] has been proposed to address the CIL problem. Similar to PNN, it expands a new backbone when facing new tasks and aggregates the features with a larger FC layer. Take the second incremental task for an example, where the model output is aggregated as:

$$
f (\mathbf {x}) = W _ {n e w} ^ {\top} \left[ \phi_ {o l d} (\mathbf {x}), \phi_ {n e w} (\mathbf {x}) \right], \tag {8}
$$

where $\phi _ { o l d }$ is the former backbone, and $\phi _ { n e w }$ is the newly initialized backbone. $[ \cdot , \cdot ]$ denotes feature aggregation, and $W _ { n e w } \in$ $\mathbb { R } ^ { 2 d \times | \mathcal { V } _ { b } | }$ is the newly initialized FC layer. In the model updating process, the old backbone is frozen to maintain former knowledge:

$$
\mathcal {L} = \sum_ {k = 1} ^ {| \mathcal {Y} _ {b} |} - \mathbb {I} (y = k) \log \mathcal {S} _ {k} \left(W _ {n e w} ^ {\top} \left[ \bar {\phi} _ {o l d} (\mathbf {x}), \phi_ {n e w} (\mathbf {x}) \right]\right), \tag {9}
$$

where $\bar { \phi } _ { o l d } ( \mathbf { x } )$ denotes the old backbone is frozen. DER also adopts an auxiliary loss to differentiate between old and new classes. Eq. 9 depicts a way to continually expand the model with new features. Under such circumstances, if the old backbone is optimized with ‘cars,’ the features extracted by $\phi _ { o l d }$ are then representative of wheels and windows. The new backbone trained with ‘cats’ is responsible for extracting beards and stripes. Since the old backbone is frozen in later stages, learning new classes will not overwrite the features of old ones, and forgetting is alleviated. Figure 4 (left) depicts the model evolution of DER.

However, saving a backbone per task requires numerous memory size in DER, and many works are proposed to obtain expandable features with a limited memory budget. FOSTER [16] formulates the learning process in Eq. 9 as a feature-boosting [177] problem. It argues that not all expanded features are needed for incremental learning and need to be integrated to reduce redundancy. For example, suppose old classes contain ‘tigers,’ and new classes contain ‘zebras.’ In that case, the stripe will be a useful feature that both old and new backbones could extract. Under such circumstances, forcing the new backbone to extract the same features is less effective for recognition. Hence, FOSTER adds an extra model compression process by knowledge distillation [178]:

$$
\min  _ {f _ {s} (\mathbf {x})} \operatorname {K L} \left(\mathcal {S} \left(f _ {t} (\mathbf {x})\right) \| \mathcal {S} \left(f _ {s} (\mathbf {x})\right)\right). \tag {10}
$$

Eq. 10 aims to find the student model $f _ { s }$ that has the same discrimination ability as the teacher model $f _ { t }$ by minimizing the discrepancy between them. The teacher is the frozen expanded model with two backbones: $f _ { t } ( \mathbf { x } ) = W _ { n e w } ^ { \top } [ \phi _ { o l d } ( \mathbf { x } ) , \phi _ { n e w } ( \mathbf { x } ) ]$ and the student is the newly initialized model $f _ { s } ( \mathbf { x } ) = W ^ { \top } \phi ( \mathbf { x } )$ . Hence, the number of backbones is consistently limited to a single one, and the memory budget will not suffer catastrophic expansion. Figure 4 (middle) depicts the model evolution of FOSTER.

MEMO [17] addresses the memory problem in CIL, aiming to enable model expansion with the least budget cost. It finds that in CIL, shallow layers of different models are similar, while deep layers are diverse. In other words, shallow layers are more generalizable, while deep layers are specific to the task, making expanding shallow layers less memory-efficient for CIL. Hence, MEMO proposes to decouple the backbone at middle layers: $\phi ( \mathbf { x } ) = \phi _ { s } ( \phi _ { g } ( \mathbf { x } ) )$ ), where specialized block $\phi _ { s }$ corresponds to the deep layers in the network, while generalized block $\phi _ { g }$ corresponds

to the rest shallow layers. Compared to DER, MEMO only expands specialized blocks $\phi _ { s } ,$ , and transforms Eq. 9 into:

$$
\sum_ {k = 1} ^ {| \mathcal {Y} _ {b} |} - \mathbb {I} (y = k) \log \mathcal {S} _ {k} (W _ {n e w} ^ {\top} [ \phi_ {s o l d} (\phi_ {g} (\mathbf {x})), \phi_ {s n e w} (\phi_ {g} (\mathbf {x})) ]),
$$

which indicates that task-specific deep layers can be built for each task upon the shared shallow layers $\phi _ { g } ( \mathbf { x } )$ . Figure 4 (right) depicts the model evolution of MEMO.

# 3.3.3 Prompt Expansion

Recently, Vision Transformer (ViT) [19] has attracted the attention of the computer vision community, and many works tend to design CIL learners using ViT as the backbone. DyTox [18] is the first work to explore ViT in CIL, which finds that model expansion in ViT is much easier than in convolutional networks. In DyTox, only task tokens are expanded for each new task, which requires much less memory than saving the whole backbone. Similarly, L2P [69] and DualPrompt [70] explore how to build CIL learners with pre-trained ViT. They borrow ideas from Visual Prompt Tuning (VPT) [179] to incrementally finetune the model with prompts. In L2P, the pre-trained ViT is frozen during the learning process, and the model only optimizes the prompts to fit new patterns. The prompt pool is defined as: $\mathbf { P } = \{ P _ { 1 } , P _ { 2 } , \cdots , P _ { M } \}$ , where M is the total number of prompts, $P _ { i } \in \bar { \mathbb { R } } ^ { L _ { p } \times d }$ is a single prompt with token length $L _ { p }$ and the same embedding size d as the instance embedding $\phi ( \mathbf { x } )$ . The prompts are organized as key-value pairs — each instance selects the most similar prompts in the prompt pool via KNN search. It obtains instance-specific predictions by adapting the input embeddings as: $\begin{array} { r } { \mathbf { x } _ { p } = \left[ P _ { s _ { 1 } } ; \cdot \cdot \cdot ; P _ { s _ { N } } ; \phi ( \mathbf { x } ) \right] , \quad 1 \leq N \leq M } \end{array}$ , where $P _ { s _ { i } }$ are the selected instance-specific prompts. The adapted embeddings are then fed into the self-attention layers [32] to obtain instancespecific representations. CODA-Prompt [71] extends the prompt search with the attention mechanism. Apart from pre-trained ViT, S-Prompt [72] utilizes the pre-trained language-vision model CLIP [180] for CIL, which simultaneously learns language prompts and visual prompts to boost representative embeddings. Apart from expanding prompts, other lightweight modules can also be dynamically expanded in CIL [181], [182], [183]

Discussions: Learning dynamic networks, especially backbone expansion methods, has achieved state-of-the-art performance in recent years [15], [16], [17], [68]. However, it often requires expandable memory budgets, which is unsuitable for incremental learning on edge devices. To tackle this problem, further model compression [16], decoupling [17], and pruning can be adopted to alleviate the memory budget. Additionally, training DER requires an individual backbone for each task and aggregates all historical backbones as the feature extractor. It implicitly results in an unfair comparison to other methods with a single backbone [17]. In this paper, we systematically investigate the fair comparison protocol between these dynamic networks and others in Section 4.4, 4.5. Additionally, expanding backbones ignores the semantic information across tasks, e.g., when the old task contains ‘tigers’ and the new task contains ‘zebras,’ features like ‘stripes’ will be extracted by multiple backbones, resulting in feature redundancy. Hence, analyzing the semantic relationship across tasks [88] can help detect the feature redundancy, and contrastive learning [184] can be adopted for generalizable features.

On the other hand, most prompt expansion methods rely on the pre-trained models as initialization. Without such generalizable backbones, lightweight model updating with prompts often

fails [185]. However, a pre-trained model is not always available for some specific downstream tasks, $e . g .$ , face recognition and speech recognition. Therefore, how to get rid of the dependence on pre-trained models is essential for these methods in realworld applications. Additionally, these prompt expansion-based methods tend to select instance-specific prompts based on a batch of instances. This requirement also needs to be satisfied during inference for accurate prompt retrieval [69], which implicitly results in an unfair comparison. Since a batch of instances is utilized to get the prompt, the context among instances becomes available, which is against the common sense of i.i.d. testing in machine learning.

Apart from these groups, there are works addressing network masks to divide a large network into sub-networks for each task [132], [135], [136]. However, deciding the activation of a specific sub-network requires the task identifier or learning extra task classifiers. On the other hand, several works [152], [186] propose to design specific modules for incremental new tasks, $e . g .$ , adapters [187]. However, manually handcrafting these modules requires heuristic designs or task-specific priors.

# 3.4 Parameter Regularization

Dynamic networks seek to adjust model capacity with data evolves. However, if the model structure is fixed and unchangeable, how can we adjust the plasticity to resist catastrophic forgetting? Parameter regularization methods consider that the contribution of each parameter to the task is not equal. Hence, they seek to evaluate each parameter’s importance to the network and keep the important ones static to maintain former knowledge.

Typical works estimate a distribution over the model parameters and use it as the prior when learning new tasks. Due to the large amounts of parameters, the estimation process often assumes them to be independent. EWC [73] is the first work addressing parameter regularization. It maintains an importance matrix with the same scale of the network, i.e., !. Denote the k-th model parameters as $\theta _ { k } ,$ , the importance of $\theta _ { k }$ is represented by $\Omega _ { k } \geq 0$ (the larger $\Omega _ { k }$ indicates $\theta _ { k }$ is more important). Apart from the training loss in Eq. 3 to learn new classes, EWC builds an additional regularization term to remember old ones:

$$
\mathcal {L} = \ell (f (\mathbf {x}), y) + \frac {1}{2} \lambda \sum_ {k} \Omega_ {k} \left(\theta_ {k} ^ {b - 1} - \theta_ {k}\right) ^ {2}. \tag {11}
$$

The parameter-wise regularization term is calculated based on two parts. $\theta _ { k } ^ { b - 1 }$ denotes the k-th parameter after learning last task $\mathcal { D } ^ { b - 1 }$ . Hence , (ϱb⇐1 $( \theta _ { k } ^ { b - 1 } - \theta _ { k } ) ^ { 2 }$ represents the parameter drift from k the last stage, and $\Omega _ { k }$ weighs it to ensure important parameters do not shift away from the last stage. Since the model at the last stage represents the ‘old’ knowledge, consolidating important parameters can prevent the knowledge from being forgotten.

Eq. 11 depicts a way to penalize essential parameters, and there are different ways to calculate the importance matrix !. In EWC, Fisher information matrix [188] is adopted to estimate !. However, the importance calculation in EWC is conducted at the end of each task, which ignores the optimization dynamics along the model training trajectory. To this end, SI [74] proposes to estimate ! in an online manner and weigh the importance via its contribution to loss decay. RWalk [33] combines these importance estimation techniques. [75], [76] resort to an extra unlabeled dataset for online evaluation. IMM [77] finds a maximum of the mixture of Gaussian posteriors with the estimated Fisher information matrix. IADM [78] and CE-IDM [79] analyze the

capacity and sustainability of different layers and find that different layers have different characteristics in CIL. In detail, shallow layers converge faster but have limited representation ability. By contrast, deep layers converge slowly while having powerful discrimination abilities. Hence, IADM augments EWC with an ensemble of different layers and learns layer-wise importance matrix in an online manner. K-FAC [80] extends the Fisher information matrix approximation with the Kronecker factorization technique.

Discussions: Although parameter and data regularization (Section 3.2) both exert regularization terms to resist forgetting, their basic idea differs substantially. Specifically, data regularization relies on the exemplar set to direct the optimization direction, while parameter regularization is based on the parameter-wise importance to construct the regularization term.

As shown in Figure 3, parameter regularization methods have attracted the attention of the community in the early years. [189] shows that despite stemming from very different motivations, both SI [74] and MAS [75] approximate the square root of the Fisher Information, with the Fisher being the theoretically justified basis of EWC. However, estimating parameter importance requires saving the matrix with the same scale as the backbone. It faces the same risk as dynamic networks in that the memory budget is linearly increasing when learning more and more tasks.

On the other hand, the importance matrix may conflict at different incremental stages [88], making it hard to optimize the model and achieve poor performance on new tasks. Hence, although these works achieve competitive results in task-incremental learning, many works [8] find that parameter regularization-based methods perform poorly in the class-incremental learning scenario. To this end, some works try to alleviate the intransigence by learning a new backbone and consolidating them into a single one [64], [77]. In that case, the learning of new tasks will not be affected by the regularization term, and the parameter importance will only be considered during the consolidation process, enabling the model to be fully fitted to new tasks.

# 3.5 Knowledge Distillation

Training data is evolving in the learning process, requiring tuning the model sequentially. We can denote the model after the previous stage $f ^ { b - 1 }$ as the ‘old model’ and the current updating model $f$ a s the ‘new model.’ Assuming the old model is a good classifier for all the seen classes in ${ \mathcal { D } } _ { b - 1 }$ , how can we utilize it to resist forgetting in the new model? To enable the old model to assist the new model, an intuitive way utilizes the concept proposed in [178], i.e., knowledge distillation (KD). KD enables the knowledge transfer from a teacher model to the student model, with which we can teach the new model not to forget. There are several ways to build the distillation relationship, and we divide these KD-based methods into three subgroups, i.e., logit distillation, feature distillation, and relational distillation.

LwF [81] is the first success to apply knowledge distillation into CIL. Similar to Eq. 11, it builds the regularization term via knowledge distillation to resist forgetting:

$$
\mathcal {L} = \underbrace {\ell \left(f (\mathbf {x}) , y\right)} _ {\text {L e a n i n g N e w C l a s s e s}} + \underbrace {\sum_ {k = 1} ^ {\left| \mathcal {Y} _ {b - 1} \right|} - \mathcal {S} _ {k} \left(f ^ {b - 1} (\mathbf {x})\right) \log \mathcal {S} _ {k} \left(f (\mathbf {x})\right)} _ {\text {R e m e m b e r i n g O l d C l a s s e s}}, \tag {12}
$$

where the old model $f ^ { b - 1 }$ is frozen during updating. The regularization term builds the mapping between the old and new models by forcing the predicted probability among old classes to be the

![](images/d87108a99c017fde23c2069d484a2ce8b789e143e26713463a859486ca7d1be8.jpg)  
Figure 5: Illustration of knowledge distillation in CIL. Left: Logit distillation aligns the model outputs to make the old and new models share the same semantic relationship. Middle: Feature distillation aligns the features produced by the old and new models to ensure the new model does not forget old features. Right: Relational distillation resorts to structural inputs, $e . g .$ , triples, and aligns the input relationship of the old and new model.

same. Given a specific input x, the output probability of the kth class reveals the semantic similarity of the input to this class. Hence, Eq. 12 forces the semantic relationship of the old and new models to be the same and resists forgetting. iCaRL [82] extends LwF with the exemplar set, which helps to further recall former knowledge during incremental learning. Additionally, it drops the fully-connected layers and follows [190] to utilize nearest-mean-ofexemplars during inference. $\operatorname { E q . }$ 12 strikes a trade-off between old and new classes, where the former part aims to learn new classes and the latter one maintains old knowledge. Since the number of old and new classes may differ in different incremental stages, BiC [83] extends Eq 12 by introducing a dynamic trade-off term:

$$
\mathcal {L} = (1 - \lambda) \ell (f (\mathbf {x}), y) + \lambda \sum_ {k = 1} ^ {| \mathcal {Y} _ {b - 1} |} - \mathcal {S} _ {k} (f ^ {b - 1} (\mathbf {x})) \log \mathcal {S} _ {k} (f (\mathbf {x})),
$$

where ς = $\begin{array} { r } { \lambda = \frac { | \mathcal { V } _ { b - 1 } | } { | \mathcal { V } _ { b } | } } \end{array}$ denotes the proportion of old classes among all classes. It increases as incremental tasks evolve, indicating that the model pays more attention to old ones.

LwF inspires the community to build the mapping between models, making knowledge distillation a useful tool in CIL. D+R [84] suggests changing the first part in Eq. 12 into a distillation loss by training an extra expert model. GD [85] proposes to select wild data for model distillation and designs a confidence-based sampling method to effectively leverage external data. Similarly, DMC [86] proposes to train a new model in each incremental stage and then compress them into a single model via an extra unlabeled dataset. Finally, if no additional data is available for knowledge distillation, ABD [87] proposes distilling synthetic data for incremental learning. These methods only concentrate on utilizing the old model to help resist forgetting in the new model. However, COIL [88] suggests conducting bidirectional distillation with co-transport, where semantic relationships between old and new models are both utilized.

Apart from distilling the logits, some works propose to distill the intermediate product of deep models, e.g., extracted features. UCIR [89] replaces the regularization term in Eq. 12 into:

$$
\mathcal {L} = \ell (f (\mathbf {x}), y) + (1 - \left\langle \frac {\phi^ {b - 1} (\mathbf {x})}{\| \phi^ {b - 1} (\mathbf {x}) \|}, \frac {\phi (\mathbf {x})}{\| \phi (\mathbf {x}) \|} \right\rangle). \tag {13}
$$

Eq. 13 forces the features extracted by the new embedding module to be the same as the old one, which is a stronger regularization than Eq. 12. Several works follow it to utilize feature distillation in CIL [90], [91], [97], [98], while others address distilling

other products. LwM [92] suggests penalizing the changes in classifiers’ attention maps to resist forgetting. AFC [93] conducts the distillation considering the importance of different feature maps. PODNet [94] minimizes the difference of the pooled intermediate features in the height and width directions instead of performing element-wise distillations. CVIC [191] decouples the distillation term into spatial and temporal features for video classification. DDE [95] distills the causal effect from the old training to preserve the old knowledge. GeoDL [96] conducts distillation based on the projection of two sets of features from old and new models.

However, both logit and feature distillation address the instancewise mapping between old and new models. To reveal the structural information in model distillation, several works suggest conducting relational knowledge distillation [192]. The differences between these groups of knowledge distillation are shown in Figure 5.

To conduct relational distillation, a group of instances needs to be extracted, $e . g .$ , triplets. We denote the extracted triplets as $\{ \mathbf { x } _ { i } , \mathbf { x } _ { j } , \mathbf { x } _ { k } \}$ , where $\mathbf { x } _ { i }$ is called the anchor. In a triplet, the target neighbor $\mathbf { x } _ { j }$ is similar to the anchor $\mathbf { x } _ { i }$ with the same class, while the impostor $\mathbf { x } _ { k }$ is dissimilar to $\mathbf { x } _ { i }$ (usually from different classes). R-DFCIL [99] suggests mapping the angle among triplets:

$$
\sum_ {\left\{\mathbf {x} _ {i}, \mathbf {x} _ {j}, \mathbf {x} _ {k} \right\} \in \mathcal {D} ^ {b}} \left\| \cos \angle \mathbf {t} _ {i} \mathbf {t} _ {j} \mathbf {t} _ {k} - \cos \angle \mathbf {s} _ {i} \mathbf {s} _ {j} \mathbf {s} _ {k} \right\|, \tag {14}
$$

where $\mathbf { t } _ { m } = \phi ^ { b - 1 } ( \mathbf { x } _ { m } )$ is the representation in the old model’s embedding space, and $\mathbf { s } _ { m } = \phi ( \mathbf { x } _ { m } )$ denotes the representation in the current model. The cosine value is calculated in the corresponding embedding space. Eq. 14 provides a way to encode the old model’s structural information into the new model and align the feature space softly. ERL [100] extends this regularization into few-shot CIL scenarios. TPCIL [101] models the relationship with the elastic Hebbian graph and penalizes the changing of the topological relations between vertices. TOPIC [27] further explores neural gas network to model the class-wise relationship. Apart from the triplet relationship, MBP [102] extends the regularization to the instance neighborhood, requiring the old and new models to have the same distance ranking in the neighborhood.

Discussions: Knowledge distillation is a general idea to build the mapping between a set of methods, which has been widely adopted in class-incremental learning with many formats $( e . g .$ ., logits, features, relationships). Due to their flexibility, knowledge distillation-based methods have also been widely applied to various incremental learning tasks, e.g., semantic segmentation [193], person re-identification [194], human action recognition [91], and federated learning [149]. Since a set of models exists in CIL, it is intuitive to build the student-teacher mapping in CIL, making knowledge distillation an essential solution for most works.

However, since the knowledge distillation term aims to strike a balance between learning the new and remembering the old, it is hard to control the precise trade-off term between plasticity and stability. Specifically, giving more importance to the knowledge distillation term will harm the plasticity of learning new tasks, while giving lower importance will cause catastrophic forgetting or feature overwriting. Compared to dynamic networks, knowledge distillation-based methods lack the ability to learn more informative features as data evolves. [17] compares knowledge distillation-based and dynamic network-based methods and finds that knowledge distillation-based methods and dynamic networks have their advantages given different memory budgets. Specifically, knowledge distillation methods show stronger performance given

limited memory, while dynamic networks require an adequate memory budget to perform competitively. Besides, feature/relational distillation only regularizes the extracted features to be similar, thus regularizing the embedding function to resist forgetting. However, due to the data characteristics of CIL, the classifier layer also gets biased and forgets former knowledge and knowledge distillationbased methods cannot handle such challenges.

# 3.6 Model Rectify

Assuming we can get all the training datasets at once and shuffle them for training with multiple epochs, the model will not suffer any forgetting and will perform well among all classes. Such a protocol is known as the upper bound of class-incremental learning, denoted as ‘Oracle.’ However, since the models trained with incremental data suffer catastrophic forgetting, several methods try to find the abnormal behaviors in CIL models and rectify them like the oracle model. These abnormal behaviors include the output logits, classifier weights, and feature embedding.

The first method addressing the bias of the CIL model is UCIR [89]. It finds that the weight norm of new classes is significantly larger than old ones, and the model tends to predict instances as the new classes with larger weights. Hence, UCIR proposes to utilize a cosine classifier to avoid the influence of biased classifiers: $\begin{array} { r } { f ( \mathbf { x } ) = \frac { W \mathbf { \theta } ^ { \top } } { \| W \| \mathbf { \theta } } \frac { \phi ( \mathbf { x } ) } { \| \phi ( \mathbf { x } ) \| } } \end{array}$ . Thus, the weight norm will not influence model predictions in incremental learning. WA [112] further normalizes the weight after every optimization step. It also introduces weight clipping to ensure the predicted probability is proportionate to classifier weights. SS-IL [113] explains the reason for weight drifting, which is caused by the imbalance phenomena between old and new instances. Since the number of new class instances is much more than that of old ones, optimizing the model with cross-entropy loss will increase the weight of new classes and decrease old ones. Hence, SS-IL suggests separated softmax operation and task-wise knowledge distillation to alleviate the influence of imbalanced data. RPC [114] claims that the classifiers of all classes can be pre-allocated and fixed. This makes it impossible for classifiers to be biased toward new classes.

On the other hand, several works find that the predicted logits of new classes are much larger than old ones. E2E [110] proposes to finetune the fully-connected layers with a balanced dataset after each stage. Furthermore, BiC [83] proposes to attach an extra rectification layer to adjust the predictions. The extra layer only have two parameters, i.e., re-scale parameter φ and bias parameter $\beta ,$ and the rectified output for the k-th class is denoted as:

$$
\hat {f} (\mathbf {x}) _ {k} = \left\{ \begin{array}{l l} \alpha \boldsymbol {w} _ {k} ^ {\top} \phi (\mathbf {x}) + \beta , & k \in Y _ {b} \\ \boldsymbol {w} _ {k} ^ {\top} \phi (\mathbf {x}), & \text {o t h e r w i s e} \end{array} \right.. \tag {15}
$$

Only the logits for new classes $( k \in Y _ { b } )$ are rectified after each incremental task. BiC separates an extra validation set from the exemplar set, $i . e . , \mathcal { E } = \mathcal { E } _ { t r a i n } \cup \mathcal { E } _ { v a l } .$ , and uses the validation set to tune the rectification layer. On the other hand, IL2M [111] suggests re-scaling the outputs with historical statistics. Suppose an instance is predicted as a new class. In that case, the logits will be re-scaled to ensure the predictions of old and new classes follow the same distribution.

Lastly, since the embedding module is sequentially updated in CIL, some works try to rectify the biased representations of incremental models. For example, SDC [105] utilizes a nearestmean-of-exemplars classifier, which calculates the class centers and assigns instances to the nearest class center. However, since the

embedding is incrementally updated, the class centers calculated in the former stage may suffer a drift in the next stage, making the classification results unreliable. Since old class instances are not available in the current stage, SDC aims to calibrate the class centers of old classes with the drift of new classes. CwD [106] analyzes the differences of embeddings among the CIL model and the oracle model and finds that the embeddings of the oracle model scatter more uniformly. It aims to make the CIL model similar to the oracle by enforcing the eigenvalues to be close. ConFiT [107] relieves the feature drift from the middle layers. MRFA [195] finds the all-layer margin of replay samples shrinks as data evolves. Other works address the model weight rectification. CCLL [108] aims to calibrate the activation maps of old models during incremental learning. RKR [109] proposes to rectify the convolutional weights of old models when learning new tasks. FACT [104] depicts a new training paradigm for CIL, namely forward compatible training. Since the embedding space is endlessly adjusted for new classes, FACT proposes to pre-assign the embedding space for new classes to relieve the burden of embedding tuning.

Discussions: Model rectify-based methods aim to reduce the inductive bias in the CIL model and align it to the oracle model. This line of work helps to understand the inherent factor of catastrophic forgetting. Apart from the rectification methods listed in this section, [113] addresses that the bias of the CIL model is from the imbalanced data stream. [184] finds that the embedding trained with contrastive loss suffers less forgetting than crossentropy loss. [196] finds that the batch normalization layers [197] are biased in CIL and proposes re-normalizing the layer outputs. [198] finds that vision transformers gradually lose the locality information when incrementally updated and proposes to insert the prior information about locality into the self-attention process. These works often treat the oracle model as the example, and design training techniques to reflect oracle model’s characteristics.

Apart from mimicking the oracle model, there are also works addressing the forward compatibility [104] and flat loss landscape. Since the ultimate goal of CIL is to find a flat minimum in loss landscape among all tasks, several works aim to achieve this goal during the first stage [199], [200]. It is worth exploring other factors in catastrophic forgetting and corresponding solutions in the future. On the other hand, the oracle model is obtained via joint training of all data via supervised loss. Other task-agnostic features could also help build a holistic classifier, e.g., via contrastive learning [184], which the oracle model does not possess.

# 3.7 Template-Based Classification

Lastly, we discuss template-based classification, which is widely adopted in CIL. If we can build a ‘template’ for each class, the classification can be done by matching the query instance to the most similar template. A popular approach is to utilize class prototypes [129] as the template, which is rooted in cognitive science [201]. The prototype in deep neural networks is often defined as the average vector in the embedding space. For example, we can utilize the current embedding function ω( ) to extract the prototype of the i-th class:

$$
\boldsymbol {p} _ {i} = \frac {1}{N} \sum_ {j = 1} ^ {| \mathcal {D} ^ {b} |} \mathbb {I} \left(y _ {j} = i\right) \phi \left(\mathbf {x} _ {j}\right), \tag {16}
$$

where N is the instance number of class i. In Eq. 16, the class prototype is calculated via the class center in the embedding

space. Hence, we can make inference without relying on the fully connected layer by matching an instance to the nearest prototype:

$$
y ^ {*} = \underset {y = 1, \dots , \left| \mathcal {Y} _ {b} \right|} {\operatorname {a r g m i n}} \left\| \phi (\mathbf {x}) - \boldsymbol {p} _ {y} \right\|. \tag {17}
$$

As discussed in model rectification-based methods, sequentially updating the incremental model will result in bias in the fullyconnected layer. Correspondingly, iCaRL [82] suggests conducting inferences via $\operatorname { E q . }$ 17, which is also known as nearest-classmean classifier [190]. Since inference is conducted by instanceprototype matching in the same embedding space, the bias among different stages can be alleviated. However, utilizing prototypebased inference also faces another challenge, i.e., the embedding mismatch between stages. Since the embedding function keeps changing among different stages, the prototypes of former stages may be incompatible with the query embedding of later stages. This phenomenon is also known as the semantic drift [105]. To fill in this gap, a naive solution is to utilize the set of exemplars and re-calculate class prototypes after each stage [37], [82]. Since the exemplar set $\mathcal { E }$ contains instances of former classes, re-calculating all class prototypes after each incremental stage ensures the compatibility between prototypes and the latest embedding function. However, when exemplars are unavailable, specific algorithms need to be designed to compensate for the semantic drift.

Prototype-based Inference without Exemplars: When exemplars are unavailable, there are two main solutions to maintain a prototype classifier. A naive solution is to freeze the embedding function after the first incremental stage [104], [116], which forces the prototypes of different stages to be compatible. Such a learning process assumes the embedding function trained with first-stage data is generalizable enough for future tasks, relying on the vast number of training instances in $\mathcal { D } ^ { 1 }$ . As a result, researchers tend to design suitable training techniques with $\mathcal { D } ^ { 1 }$ to obtain a generalizable feature space for future tasks. [49], [120] draw inspiration from contrastive learning and design pre-text tasks to enhance the representation learned by the first stage. CEC [115] meta-learns a graph model to adjust new class prototypes with known ones, which propagates context information between classifiers for adaptation. LIMIT [121] finds that using prototypes extracted by the first stage backbone tends to predict instances into classes of the first stage. It proposes calibrating the prediction logits by meta-learning a transformer block between old and new classes. TEEN [119] systematically analyzes the performance gap between old and new classes and finds that the prototypical network forces the model to predict new classes into the most similar old class. Hence, it suggests pushing the prototypes of new classes to old classes for a calibrated decision boundary. Moreover, [104] aims to enhance the model’s forward compatibility by reserving the embedding space for new classes so that new classes can be inserted into the embedding space without harming existing ones. It allocates ‘virtual prototypes’ for new classes and explicitly reserves the embedding space for them using a bimodal target label and manifold mixup [202] to generate new class instances.

When we have a pre-trained embedding function as initialization, ADAM [116] finds that using a prototype-based classifier easily beats the state-of-the-art prompt-based methods [69], [70]. However, although the pre-trained model possesses generalizable features, it still lacks task-specific information on incremental datasets. Hence, it designs the ‘adapt and merge’ protocol to unify the generalizability of the pre-trained model and the adaptivity of downstream tasks. With the pre-trained embedding, it finetunes

it with the first stage dataset $\mathcal { D } ^ { 1 }$ , and concatenates the pretrained and adapted embeddings for prototype extraction. Based on ADAM, RanPAC [117] designs random projection to project the concatenated features into a high-dimensional space, within which classes are separated more clearly. It also incrementally updates a Mahalanobis distance-based classifier, which shows stronger performance than cosine distance between prototypes and query embedding. FeCAM [118] also finds the inadequacy of the cosine classifier and proposes using a Bayesian classifier instead.

Apart from freezing the embedding, some works try to compensate for the semantic drift among different stages. Since prototypes will drift with the ever-changing embedding functions, they aim to estimate such drift to estimate the prototypes in the latest embedding space. SDC [105] aims to measure the prototype drift between different stages and utilizes the weighted combination of current stage data for reference. ZSTCI [122] achieves this goal by mapping prototypes of different stages into the same embedding space and designing a prototype alignment loss across stages.

Finally, another line of work considers generative classification [123]. Different from estimating the class prototype as a template, the template for each class is a generative model. Hence, the inference process can be measured via the likelihood of the query instance under such a generative model. However, it requires more calculation budgets for generative templates during inference than prototype-based methods.

Discussions: There are two advantages of template-based classification. Firstly, when the exemplar set is available, using template-based classification enables query-prototype matching in the embedding space. Since the classifier will be biased after incremental learning, utilizing such a matching target alleviates the inductive bias during inference [82]. Secondly, when the pre-trained model (or model trained with large base classes) is available as initialization, the feature representations are generalizable and can be transferred to downstream tasks. Hence, freezing the embedding and using template-based classification can take full use of the generalizable features, and such a non-incremental learner will not suffer forgetting due to the frozen backbone [116], [117], [118].

However, there are also some drawbacks. When the exemplar set is not available, re-calculating the prototypes is impossible, and it requires a complex adjusting process to overcome the semantic drift [105], [122]. Secondly, when freezing the backbone and taking a template-based classifier, the model sacrifices its adaptivity for downstream tasks. When there are significant domain gaps between the pre-trained model and the downstream data [203], [204], template-based classification shall fail due to the incapability to extract generalizable features. In that case, continually adjusting the backbone could be more suitable to extract task-specific features. Finally, we can use an energy-based model [205] to compute for each class an energy value rather than a likelihood [206] to alleviate the high cost of the generative model.

# 4 EXPERIMENTAL EVALUATION

In this section, we conduct comprehensive experiments to evaluate the performance of different kinds of CIL methods with benchmark datasets. We first introduce the benchmark experimental setting, dataset split, evaluation protocol, and implementation details. Afterward, we aim to compare these methods from three aspects:

How do these methods perform on benchmark datasets?   
• Are they fairly compared? How to fairly compare them?   
• How to evaluate them with memory-agnostic measure?

Table 2: Average and last accuracy performance comparison on CIFAR100. ‘#P’ represents the number of parameters (million).   

<table><tr><td rowspan="2">Method</td><td colspan="3">Base0 Inc5</td><td colspan="3">Base0 Inc10</td></tr><tr><td>#P</td><td>\(\bar{A}\)</td><td>\(A_B\)</td><td>#P</td><td>\(\bar{A}\)</td><td>\(A_B\)</td></tr><tr><td>Finetune</td><td>0.46</td><td>17.59</td><td>4.83</td><td>0.46</td><td>26.25</td><td>9.09</td></tr><tr><td>EWC</td><td>0.46</td><td>18.42</td><td>5.58</td><td>0.46</td><td>29.73</td><td>12.44</td></tr><tr><td>LwF</td><td>0.46</td><td>30.93</td><td>12.60</td><td>0.46</td><td>43.56</td><td>23.25</td></tr><tr><td>GEM</td><td>0.46</td><td>31.73</td><td>19.48</td><td>0.46</td><td>40.18</td><td>23.03</td></tr><tr><td>Replay</td><td>0.46</td><td>58.20</td><td>38.69</td><td>0.46</td><td>59.31</td><td>41.01</td></tr><tr><td>RMM</td><td>0.46</td><td>65.72</td><td>51.10</td><td>0.46</td><td>68.54</td><td>56.64</td></tr><tr><td>iCaRL</td><td>0.46</td><td>63.51</td><td>45.12</td><td>0.46</td><td>64.42</td><td>49.52</td></tr><tr><td>PODNet</td><td>0.46</td><td>47.88</td><td>27.99</td><td>0.46</td><td>55.22</td><td>36.78</td></tr><tr><td>Coil</td><td>0.46</td><td>57.68</td><td>34.33</td><td>0.46</td><td>60.27</td><td>39.85</td></tr><tr><td>WA</td><td>0.46</td><td>64.65</td><td>48.46</td><td>0.46</td><td>67.09</td><td>52.30</td></tr><tr><td>BiC</td><td>0.46</td><td>62.38</td><td>43.08</td><td>0.46</td><td>65.08</td><td>50.79</td></tr><tr><td>FOSTER</td><td>0.46</td><td>63.38</td><td>49.42</td><td>0.46</td><td>66.49</td><td>53.21</td></tr><tr><td>AANets</td><td>0.99</td><td>59.34</td><td>42.42</td><td>0.99</td><td>61.73</td><td>45.53</td></tr><tr><td>DER</td><td>9.27</td><td>67.99</td><td>53.95</td><td>4.60</td><td>69.74</td><td>58.59</td></tr><tr><td>MEMO</td><td>7.14</td><td>68.10</td><td>54.23</td><td>3.62</td><td>70.20</td><td>58.49</td></tr><tr><td>DyTox</td><td>10.7</td><td>68.06</td><td>52.23</td><td>10.7</td><td>71.07</td><td>58.72</td></tr><tr><td>L2P</td><td>85.7</td><td>84.00</td><td>78.96</td><td>85.7</td><td>89.35</td><td>83.39</td></tr></table>

Specifically, Sections 4.2 and 4.3 answer the first question, and Section 4.4 answers the second question. We provide the holistic performance measures in Section 4.5 to answer the third question and summarize the results in Section 4.6. We report more results, measures, and visualizations in the supplementary material.

# 4.1 Experimental Settings

# 4.1.1 Benchmark Datasets

iCaRL [82] firstly formulates the comparison protocol of classincremental learning, which was widely followed and compared in other works. It suggests using CIFAR100 [24] and ImageNet100/1000 [207] for evaluation. CIFAR100 contains 100 classes with 60,000 images, in which 50,000 are training instances, and 10,000 are testing ones, with 100 images per class. Each image is represented by 32 32 pixels. ImageNet1000 is a large-scale dataset with 1,000 classes, with about 1.28 million images for training and 50,000 for validation. ImageNet100 is the subset of ImageNet1000 containing 100 classes [82]. These classes are selected from the first 100 classes after a random shuffle. Some works [27], [72], [73], [113] utilize MNIST [208], CUB200 [209] and miniImageNet [207] for evaluation, while the aforementioned datasets are the most widely adopted in the current CIL community, and we choose them for model evaluation.

Dataset Split: Following the protocol defined in [82], all classes are first shuffled by Numpy random seed 1993. Afterward, there are two different ways to split the classes into incremental stages:

• Train from scratch (TFS): splits all classes equally into each incremental stage. For example, if there are B stages and C classes in total, each incremental task contains $C / B$ classes for training.   
Train from half (TFH): splits half of the total classes as the first incremental task and equally assigns the rest classes into the following stages. Specifically, it assigns $C / 2$ classes to the first task and $C / 2 ( B - 1 )$ classes to the rest tasks.

Both of these settings are widely adopted in the current CIL community [83], [89]. Hence, we unify these settings as ‘Base-m, Inc-n’, where m stands for the number of classes in the first stage, and n stands for the number of classes in each incremental task. $m = 0$ stands for the TFS protocol. We use the same training splits for every compared method for a fair comparison. The testing set is the same as the original one for holistic evaluation.

# 4.1.2 Evaluation Metrics

There are several metrics to evaluate the CIL model. We denote the Top-1 accuracy after the b-th task as ${ \mathcal { A } } _ { b } ,$ and higher $\mathcal { A } _ { b }$ indicates a better prediction accuracy. Since the CIL model is continually updated, the accuracy often decays with more tasks incorporated. Hence, the accuracy after the last stage $( A _ { B } )$ is a proper metric for measuring the overall accuracy among all classes.

However, only comparing the final accuracy ignores the performance evolution along the learning trajectory. Hence, another metric denoted as ‘average accuracy’ considers the performance of all incremental stages: $\begin{array} { r } { \bar { \mathcal { A } } = \frac { 1 } { B } \mathbf { \dot { Z } } _ { b = 1 } ^ { B } \mathcal { A } _ { b } } \end{array}$ . A higher average accuracy denotes a stronger performance along the incremental stages. Apart from these measures, we also consider forgetting and intransigence [33] measures in the supplementary.

# 4.1.3 Implementation Details

Selected methods: In the comparison, we aim to contain all kinds of methods in Table 1. We systematically choose 17 methods, including: Replay [128], RMM [144] (data replay), GEM [53] (data regularization), EWC [73] (parameter regularization), AANets [66], FOSTER [16], MEMO [17], DER [15], DyTox [18], L2P [69] (dynamic networks), LwF [81], iCaRL [82], PODNET [94], Coil [88] (knowledge distillation), WA [112], BiC [83] (model rectify). We also report the baseline method ‘Finetune,’ which updates the model with Eq. 3.

The choice of these methods follows the development timeline of CIL, which is also the way we introduce these works. Additionally, it not only contains all seven aspects of CIL algorithms in our taxonomy but also includes early works (e.g., EWC, LwF, iCaRL) and recent state-of-the-art (DER, MEMO, L2P). The choice also gives consideration to CNN-based methods, ViT-based methods (DyTox), and even pre-trained ViT-based methods (L2P). Specifically, RMM is a specific technique to efficiently organize the memory budget, which can be orthogonally combined with other methods, and we combine it with FOSTER, denoted as FOSTER+RMM. Similarly, we combine AANets with LUCIR [89], denoted as LUCIR+AANets. L2P requires pre-trained ViT as the backbone model, while others are trained from scratch.

Training details: We implement the above methods with Py-Torch [210] and PyCIL [211]. Specifically, we use the same network backbone for all CNN-based compared methods, $i . e .$ , ResNet32 [212] for CIFAR100 and ResNet18 for ImageNet. We use SGD with an initial learning rate of 0.1 and momentum of 0.9. The training epoch is set to 170 for all datasets with a batch size of 128. The learning rate suffers a decay of 0.1 at 80 and 120 epochs. For ViT-based methods like DyTox and L2P, we follow the original implementation and use ConViT [213] for DyTox and pretrained ViT-B/16 [19] for L2P. The optimization parameters of them are set according to the original paper since ViT has a different optimization preference to CNN. We follow the original paper to set the algorithm-specific parameters, $e . g .$ , splitting 10% exemplars from the exemplar set as validation for BiC, setting the temperature ε to 5 and using a 10 epochs warm-up for DER, using $\ell _ { 2 }$ norm to normalize the fully-connected layers in WA. For EWC, the ς parameter is done via a grid search among $\{ 1 , 1 0 ^ { 1 } , 1 0 ^ { 2 } , 1 0 ^ { 3 } , 1 0 ^ { 4 } \}$ , and we find $1 0 ^ { 3 }$ leads to its best performance.

Research has shown that a good starting point $( i . e .$ , the first stage accuracy $\boldsymbol { \mathcal { A } } _ { 1 } )$ implies better transferability and will suffer less forgetting [110]. It must be noted that the performance gap of the first stage should be eliminated so as not to affect the forgetting evaluation. Hence, to make the methods share the same starting

![](images/79b1599cc95fdefac5cab3c0c58adaf4e65a8e24f78d9ed0d4be4841e4a99d90.jpg)

![](images/41baeb2bf84f3d1b266fe6ce1e741ba7aa84b4b694bf7622e1c3cc304f355241.jpg)

![](images/4c1413c308b74aed99f29e1a625907f6aa41efaba2b970eceaac424bb32db268.jpg)

![](images/87fec77e9ee91331facce8e313e342f3cf0803313ea5a2bc8f71f5e7077df1f8.jpg)

![](images/05f0a917fd58d542957041229b7e1e9921b134f571a8423acde5458888bdbba0.jpg)

![](images/a6b1454fb422adae45f5cb041578cf83dd9ab43214a3e147cfce824b137f41c5.jpg)

![](images/0f5e0c244c5e3a1f5170e6a10d3c1954c12041ade43a9a94420fedaa32513864.jpg)

![](images/db8faf2bf82b785268542dd30a5b30d52fd479176d2b5e9a1275ef6ab0ab44ec.jpg)

![](images/4f8a1c6b70c887ecc4c2fa0d476c3c9c79289b39928a04ca63f854d670027328.jpg)  
(g) ImageNet1000 Base0 Inc100   
(h) ImageNet1000 Base500 Inc100

(e) ImageNet100 Base0 Inc5

(f) ImageNet100 Base50 Inc10

![](images/6518208585e8b4fa95a8609b4f9e81f51e2b6e7f3b838ddf4ffa097b04f7e26d.jpg)  
Figure 6: Incremental performance of different methods on CIFAR100 (a-d), ImageNet100 (e-f), and ImageNet1000 (g-h). Legends are shown at the top of this figure, and we report the results of more settings in the supplementary.   
(a) CIFAR100 Base0 Inc5

![](images/54fef456fd090f90d96bbb2c87922ec9bf4e9be7935236a14419dc2afbf564c5.jpg)  
(b) CIFAR100 Base0 Inc10

![](images/7d2b447facbbc722dcd964a6869eb2dcc92c1a67ef789213673280ffdf20c754.jpg)  
(c) ImageNet100 Base50 Inc5

![](images/acef04e1c19f4763af3f5e29f6492b80903effdd3dc9ef501ca417c6635bed9c.jpg)  
(d) ImageNet100 Base0 Inc10   
Figure 7: Incremental accuracy of different methods with aligned memory cost. Legends are shown in (a) and (d).

point, we utilize the same training strategy, data augmentation, and hyperparameters. We use basic data augmentation, e.g., random crop, horizontal flip, and color jitter for CIFAR100 and ImageNet.

It must be noted that Finetune, EWC, LwF, and L2P are exemplar-free methods, and we do not use any exemplar set for them. For other methods, we follow the benchmark setting to set the number of exemplars to 2,000 for CIFAR100 and ImageNet100 and 20,000 for ImageNet1000. These exemplars are equally sampled from each seen class via the herding [124] algorithm in Definition 2.

# 4.2 Comparison on Small-Scale Datasets

This section includes the comparison on the small-scale dataset, i.e., CIFAR100. We compare these methods under TFS and TFH settings with four data splits and report the incremental performance in Figure 6 (top). We summarize the average and final performance, the number of parameters in Table 2.

As we can infer from these figures, finetune shows the worst performance among all settings, verifying the fact that the model will suffer forgetting when sequentially learning new concepts. Regularizing the parameters, i.e., EWC, shows a negligible improvement over finetune. By contrast, LwF adds knowledge distillation loss to resist forgetting, which substantially improves the performance. When the exemplar set is available, directly replaying them during model updating can further enhance the performance by a substantial margin. Coil and iCaRL combine the exemplar

replay and knowledge distillation and further obtain a performance boost than the vanilla replay. Model rectify methods, i.e., BiC and WA, rectify the bias in iCaRL and further improve the accuracy. However, recent methods based on dynamic networks (i.e., DER, FOSTER, MEMO, and DyTox) show competitive results with the help of multiple backbones. It indicates that saving more backbones can substantially help the model overcome forgetting. When it comes to pre-trained models, L2P obtains the best performance among all methods. However, other methods are trained from scratch, while L2P relies on the ViT pre-trained on ImageNet-21K, making it unfair to directly compare these two lines of methods.

On the other hand, we can infer from different settings that TFH requires more stability than TFS. Since the evaluation is based on the accuracy among all classes, remembering old classes becomes more critical when there is a large group of base classes.

# 4.3 Comparison on Large-Scale Datasets

In this section, we evaluate different methods on the largescale dataset, i.e., ImageNet100 and ImageNet1000. We compare these methods under the TFS and TFH settings and report the incremental performance (top-1 accuracy) of different methods in Figure 6 (bottom). We report the top-5 accuracy and summarize the average and final performance, the number of parameters in the supplementary. Since GEM requires saving a large-scale matrix for solving the QP problem, it cannot be conducted with the

![](images/25c0860049273dac7a59cffcf64fdb4269a4dbb4b304848a73b2550bf9000aad.jpg)  
(a) Memory size of Figure 6(b)

![](images/37acc8737b765dfde8655ae72eb36eb4fcb7add29bae0329e0af314c6b0b2b60.jpg)  
(b) Memory size of Figure 7(b)   
Figure 8: Memory size of different comparison protocols. Dark bars denote the budget for exemplars, and red bars represent the budget for keeping the model. Different methods should be aligned to the same budget for a fair comparison, as shown in (b).

Table 3: Performance comparison on CIFAR100 with aligned memory cost. ‘#P’ represents the number of parameters (million). ‘# ’ denotes the number of exemplars, and ‘MS’ denotes the memory size (MB).   

<table><tr><td rowspan="2">Method</td><td colspan="5">CIFAR100 Base0 Inc10</td></tr><tr><td>#P</td><td>#E</td><td>MS</td><td>A</td><td>AB</td></tr><tr><td>GEM</td><td>0.46</td><td>7431</td><td>23.5</td><td>27.03</td><td>10.72</td></tr><tr><td>Replay</td><td>0.46</td><td>7431</td><td>23.5</td><td>69.97</td><td>55.61</td></tr><tr><td>iCaRL</td><td>0.46</td><td>7431</td><td>23.5</td><td>70.94</td><td>58.52</td></tr><tr><td>PODNet</td><td>0.46</td><td>7431</td><td>23.5</td><td>60.80</td><td>45.38</td></tr><tr><td>Coil</td><td>0.46</td><td>7431</td><td>23.5</td><td>70.69</td><td>54.40</td></tr><tr><td>WA</td><td>0.46</td><td>7431</td><td>23.5</td><td>69.55</td><td>59.26</td></tr><tr><td>BiC</td><td>0.46</td><td>7431</td><td>23.5</td><td>70.69</td><td>59.60</td></tr><tr><td>FOSTER</td><td>0.46</td><td>7431</td><td>23.5</td><td>72.28</td><td>59.39</td></tr><tr><td>DER</td><td>4.60</td><td>2000</td><td>23.5</td><td>71.47</td><td>60.26</td></tr><tr><td>MEMO</td><td>3.62</td><td>3312</td><td>23.5</td><td>72.37</td><td>61.98</td></tr></table>

ImageNet dataset. On the other hand, since the ViT in L2P is pretrained on ImageNet-21K, incrementally training it on ImageNet is meaningless, and we do not report its results.

As we can infer from these figures, most methods share the same trend as CIFAR100. Replay acts as a strong baseline in both small-scale and large-scale inputs, verifying the effectiveness of exemplars in incremental learning. Dynamic networks consistently show the best performance among all settings, outperforming other methods by a substantial margin in the benchmark comparison.

# 4.4 Memory-Aligned Comparison

Former experimental evaluations indicate dynamic networks show the best performance among all methods. However, are these methods fairly compared? We argue that these dynamic networks implicitly introduce an extra memory budget, namely model buffer for keeping old models. The additional buffer results in an unfair comparison to those methods without storing models. Taking Table 2 for an example, the number of parameters in DER is ten times that of iCaRL in the CIFAR100 Base0 Inc10 setting. We visualize the memory cost of different methods in Figure 8(a) and find that dynamic networks obtain better performance at the expense of more memory budgets. It makes directly comparing different kinds of methods unfair.

In this section, we follow [17] for a fair comparison among different methods with different memory budgets. For those methods with different memory costs, we need to align the performance measure at the same memory scale for a fair comparison. For example, a ResNet32 model costs 463, 504 parameters (float), while a CIFAR image requires $3 \times 3 2 \times 3 2$ integer numbers (int). Hence, the budget for saving a backbone is equal to saving 463, 504 floats ↖4 bytes/float $\div ( 3 \times 3 2 \times 3 2 )$ bytes/image ↙ 603 instances

Table 4: Memory-agnostic performance measures for CIL. AUC depicts the dynamic ability with the change of memory size.   

<table><tr><td rowspan="2">Method</td><td>CIFAR100</td><td>Base0</td><td>Inc10</td><td>ImageNet100</td><td>Base50</td><td>Inc5</td></tr><tr><td>AUC-A</td><td>AUC-L</td><td>AUC-A</td><td>AUC-A</td><td>AUC-L</td><td></td></tr><tr><td>GEM</td><td>4.31</td><td>1.70</td><td>-</td><td>-</td><td></td><td></td></tr><tr><td>Replay</td><td>10.49</td><td>8.02</td><td>553.6</td><td>470.1</td><td></td><td></td></tr><tr><td>iCaRL</td><td>10.81</td><td>8.64</td><td>607.1</td><td>527.5</td><td></td><td></td></tr><tr><td>PODNet</td><td>9.42</td><td>6.80</td><td>701.8</td><td>624.9</td><td></td><td></td></tr><tr><td>Coil</td><td>10.60</td><td>7.82</td><td>601.9</td><td>486.5</td><td></td><td></td></tr><tr><td>WA</td><td>10.80</td><td>8.92</td><td>666.0</td><td>581.7</td><td></td><td></td></tr><tr><td>BiC</td><td>10.73</td><td>8.30</td><td>592.7</td><td>474.2</td><td></td><td></td></tr><tr><td>FOSTER</td><td>11.12</td><td>9.03</td><td>638.7</td><td>566.3</td><td></td><td></td></tr><tr><td>DER</td><td>10.74</td><td>8.95</td><td>699.0</td><td>639.1</td><td></td><td></td></tr><tr><td>MEMO</td><td>10.85</td><td>9.03</td><td>713.0</td><td>654.6</td><td></td><td></td></tr></table>

![](images/34a38c09eb5f077c24597b86aa6c6998b2a967cbc5dcc5e59c868dd56a520898.jpg)  
(a) CIFAR100 Base0 Inc10

![](images/12c464c3fb50f964492170b1af4000856a9b49fc9fdb41163e1023cf96cb9cc8.jpg)  
(b) ImageNet100 Base50 Inc5   
Figure 9: Average performance-memory curve of different methods with different datasets. Dynamic networks perform better with large budgets, while other methods dominate small ones.

for CIFAR. A fair comparison between different methods can be made by equipping the other methods with more exemplars. Since DER requires saving all the backbones from history, we align the memory cost of other methods to DER with extra exemplars. We visualize the memory budget of different methods under the current protocol in Figure 8(b), where the total budgets of different methods are aligned to the same scale.

We report the results under the current protocol in Figure 7 and the detailed performance in Table 3. Since Finetune, LwF, and EWC cannot be combined with the exemplar set, we do not report the results of these methods. Similarly, DyTox and L2P utilize different kinds of backbones, and we do not report their results. As we can infer from these results, the gap between dynamic networks and other methods is no longer large under fair comparison. For example, DER outperforms iCaRL by 9.07% in terms of the final accuracy in the benchmark comparison of CIFAR100 Base0 Inc10, while the gap decreases to 1.74% under the current protocol.

# 4.5 Memory-Agnostic Measure

Section 4.4 enables fair comparison among different methods by aligning the memory cost. However, the comparison is made by aligning the memory cost of other methods to DER. In contrast, open-world applications require conducting class-incremental learning in various scenarios, i.e., high-performance computers and edge devices are both essential. Hence, it requires a memoryagnostic measure for CIL to measure the model’s extendability given any memory budget.

To this end, we can set several ‘comparison budgets’ and align the memory cost of different methods to them. The budget list starts from a small value and incrementally enlarges, containing the requirement of different scale models. In this setting, we set the budget of the start point to a single backbone and gradually increase it to the budget cost of DER. For those algorithms without

extra model storage, we equip more exemplars to meet the selected budget. However, when the selected budget is smaller than the required size, dynamic networks (i.e., DER and MEMO) cannot be deployed with the benchmark backbone. Therefore, we choose smaller backbones with fewer parameters for alignment. Hence, we can measure the performance of different methods at different memory scales and draw the performance-memory curve, as shown in Figure 9. The X-coordinate corresponds to the memory cost, and the Y-coordinate indicates the average performance A¯ (or last performance $\boldsymbol { A } _ { B } )$ . We suggest the area under the performancememory curve (AUC) since the curve of each method indicates the dynamic ability with the change of model size. We calculate AUC-A and AUC-L, standing for the AUC under the average performance-memory and last performance-memory curves.

As we can infer from Table 4, there are two main conclusions. Firstly, there exists an intersection between dynamic networks and other methods, where other methods perform better given a small memory size. In contrast, dynamic networks perform better given a large memory size. In other words, there is no free lunch in CIL, and different kinds of methods have their dominant domains. Secondly, the AUC measure provides a holistic way to measure the extendability of different methods given various memory budgets. FOSTER and MEMO show competitive results regarding the AUC-A/L measure, implying their stronger extendability. It would be interesting to introduce it as the performance measure and design CIL methods for real-world applications. We report implementation details and the performance of each budget point in the supplementary.

# 4.6 Discussions about the Comparison

With the above experimental evaluations from three aspects, we have the following conclusions: 1) Equipping the model with exemplars is a simple and effective way to resist forgetting in CIL models. 2) Knowledge distillation performs better than parameter regularization in resisting forgetting with the same cost. 3) Model rectification can further boost the performance of other CIL models in a plug-and-play manner. 4) Pre-trained models can ease the burden of incremental learning and show very strong performance. However, since the features of pre-trained models are already available and do not need to be incrementally learned, comparing pre-trained models to other methods may be unfair. 5) Dynamic networks show the best performance in the evaluation at the cost of extra memory budgets. However, when changing the extra budgets into equal size of exemplars, the performance gap becomes smaller. 6) AUC-A and AUC-L provide a way to evaluate different CIL methods in a memory-agnostic manner, which can help select the method with extendability given any budget.

# 5 FUTURE DIRECTIONS

In this section, we discuss the possible future directions of the class-incremental learning field.

CIL with Complex Inputs: In the real world, data is often with complex format, e.g., few-shot [27], imbalanced [28], weak supervised [184], [214], multi modal [180], [183], concept drift [10], novel classes [215] etc. CIL methods should be able to handle these real-world scenarios for better generalizability. Specifically, [27], [104], [115], [121], [216] address the few-shot CIL problem, where the model is required to be adapted to incoming few-shot classes. [28], [141] propose to tackle the long-tailed CIL problem, where the head classes are easy to collect with adequate instances

while tail classes are scarce. Recently, with the prosperity of CLIP [180], incrementally training the language vision models to handle multi-modal data streams [217] is becoming popular. Since the labeling cost is always expensive in the real world, there are some works addressing training CIL models in a semi-supervised or unsupervised manner [184]. [148] proposes a unified framework to handle CIL with concept drift. If the test dataset contains instances from unknown classes, open-set recognition [215] and novel class discovery [218] can equip the model with the detection ability, which refers to the open-world recognition problem [219]. Lastly, real-world data may emerge hierarchically, and the labels could evolve from coarse-grained to fine-grained. CIL with refined concepts [220] is also vital to building real-world learning systems. CIL with General Data Stream: Current CIL methods have a set of restrictions on the data stream, e.g., saving exemplars for rehearsal, undergoing multi-epoch offline training within an incremental task, etc. Future CIL algorithms should be able to conduct fully online training [221] without requiring the task boundaries [222]. On the other hand, saving exemplars from the history may violate user privacy in some cases. To this end, exemplar-free CIL [50], [150] [223] [224], [225] should be conducted to enable the model to be adapted without the help of exemplars. Lastly, most CIL methods rely on the number of base classes to define hyper-parameters in model optimization, where more base classes require larger stability and fewer base classes require larger plasticity. Therefore, designing the algorithm to handle CIL problems given any base classes [226] is also essential to the real world.

CIL with Any Memory/Computational Budgets: Dynamic networks have obtained impressive performance in recent years [16] However, most of them require an extra memory budget to save the external backbones. In the real world, a good CIL algorithm should handle different budget restrictions. For example, an algorithm should be able to learn with high-performance computers or with edge devices (e.g., smartphones), and both scenarios are essential. Hence, deploying and comparing CIL models in the real world should take the memory budgets into consideration. The performance measures of AUC-A/L [17] are proper solutions to holistically compare different methods given any memory budgets. On the other hand, future CIL methods are also encouraged to handle specific learning scenarios, e.g., [227] addresses training CIL systems under resource-limited scenarios. Another important characteristic is the computational budget [228]. For realistic scenarios with high-throughput streams, computational bottlenecks impose implicit constraints on learning from past samples that can be too many to be revisited during training. In that case, we can only update the model with limited iterations and cannot tackle all the data. Hence, designing computational-efficient algorithms in real-world applications remains a promising direction for relating CIL to realistic scenarios.

CIL with Pre-trained Models: Recently, pre-trained models have shown to work competitively with their strong transferability, especially for ViT-based methods [69], [70], [71], [72]. The pretrained models provide generalizable features for the downstream tasks, enabling the incremental model to adjust with minimal cost [179]. CIL with pre-trained models is a proper way to handle real-world incremental applications from an excellent starting point. However, since the final target for incremental learning is to build a generalizable feature continually, some will argue that pre-trained models weaken the difficulty of incremental learning. From this perspective, designing proper algorithms to train the CIL model

from scratch is more challenging. On the other hand, pre-trained language-vision models [180] have shown powerful generalizability in recent years, and exploring the ensemble of various pre-trained models is also an exciting topic.

CIL with Bidirectional Compatibility: Compatibility is a design characteristic in software engineering community [229], [230], [231], [232], which was introduced to the machine learning community in [233], [234]. Backward compatibility allows for interoperability with an older legacy system. In contrast, forward compatibility allows a system to accept input intended for a later version of itself. In the incremental learning field, compatibility is also a core problem, where the new model is required to understand the features produced by the old model to classify old classes. Most methods aim to enhance backward compatibility by making the new model similar to the old one. However, FACT [104] addresses the forward compatibility in CIL, where the model should be prepared for future updates, acting like the pre-assigned interface. Furthermore, it will be interesting to address bidirectional compatibility [88] in the future.

Analyzing the Reason Behind Catastrophic Forgetting: Model rectification-based methods aim to reduce the inductive bias in the CIL model. Recently, more works have tried to analyze the reason for forgetting in CIL. [196] suggests that batch normalization layers are biased when sequentially trained, which triggers the different activation of old and new classes. [223] finds that representations with large eigenvalues transfer better and suffer less forgetting, and [221] shows that eigenvalues can be enlarged by maximizing the mutual information between old and new features. [235] theoretically decomposes the CIL problem into within-task and taskid predictions. It further proves that good within-task and task-id predictions are necessary and sufficient for good CIL performances. [236] finds that applying data replay causes the newly added classes’ representations to overlap significantly with the previous classes, leading to highly disruptive parameter updates. [200] empirically shows that the amount of forgetting correlates with the geometrical properties of the convergent points. It would be interesting to explore more reasons for catastrophic forgetting theoretically and empirically in the future.

# 6 CONCLUSION

Real-world applications often face streaming data, with which the model should be incrementally updated without catastrophic forgetting. In this paper, we provide a comprehensive survey about class-incremental learning by dividing them into seven categories taxonomically and chronologically. Additionally, we provide a holistic comparison among different methods on several publicly available datasets. With these results, we discuss the insights and summarize the common rules to inspire future research. Finally, we highlight an important factor in CIL comparison, namely memory budget, and advocate evaluating different methods holistically by emphasizing the effect of memory budgets. We provide a comprehensive evaluation of different methods given specific budgets as well as some new performance measures. We expect this survey to provide an effective way to understand current stateof-the-art and speed up the development of the CIL field.

# REFERENCES

[1] David Silver, Aja Huang, Chris J Maddison, Arthur Guez, Laurent Sifre, George Van Den Driessche, Julian Schrittwieser, Ioannis Antonoglou, Veda Panneershelvam, Marc Lanctot, et al. Mastering the game of go

with deep neural networks and tree search. Nature, 529(7587):484–489, 2016.   
[2] John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ronneberger, Kathryn Tunyasuvunakool, Russ Bates, Augustin !ídek, Anna Potapenko, et al. Highly accurate protein structure prediction with alphafold. Nature, 596(7873):583–589, 2021.   
[3] Quan Feng and Songcan Chen. Learning multi-tasks with inconsistent labels by using auxiliary big task. Frontiers of Computer Science, 17(5):175342, 2023.   
[4] Heitor Murilo Gomes, Jean Paul Barddal, Fabrício Enembreck, and Albert Bifet. A survey on ensemble learning for data stream classification. ACM Computing Surveys, 50(2):1–36, 2017.   
[5] Georg Krempl, Indre !liobaite, Dariusz Brzezinski, Eyke Hüllermeier, ´ Mark Last, Vincent Lemaire, Tino Noack, Ammar Shaker, Sonja Sievi, Myra Spiliopoulou, et al. Open challenges for data stream mining research. KDD, 16(1):1–10, 2014.   
[6] Matthias De Lange, Rahaf Aljundi, Marc Masana, Sarah Parisot, Xu Jia, Ale" Leonardis, Gregory Slabaugh, and Tinne Tuytelaars. A continual learning survey: Defying forgetting in classification tasks. IEEE transactions on pattern analysis and machine intelligence, 44(7):3366– 3385, 2021.   
[7] Stephen T Grossberg. Studies of mind and brain: Neural principles of learning, perception, development, cognition, and motor control, volume 70. Springer Science & Business Media, 2012.   
[8] Gido M van de Ven, Tinne Tuytelaars, and Andreas S Tolias. Three types of incremental learning. Nature Machine Intelligence, pages 1–13, 2022.   
[9] Zhiyuan Chen and Bing Liu. Lifelong machine learning. Synthesis Lectures on Artificial Intelligence and Machine Learning, 12(3):1–207, 2018.   
[10] Jie Lu, Anjin Liu, Fan Dong, Feng Gu, Joao Gama, and Guangquan Zhang. Learning under concept drift: A review. IEEE Transactions on Knowledge and Data Engineering, 31(12):2346–2363, 2018.   
[11] Zhi-Hua Zhou, Jianxin Wu, and Wei Tang. Ensembling neural networks: many could be better than all. Artificial intelligence, 137(1-2):239–263, 2002.   
[12] Ilja Kuzborskij, Francesco Orabona, and Barbara Caputo. From n to n+ 1: Multiclass transfer incremental learning. In CVPR, pages 3358–3365, 2013.   
[13] Qing Da, Yang Yu, and Zhi-Hua Zhou. Learning with augmented class by exploiting unlabeled data. In AAAI, pages 1760–1766, 2014.   
[14] Marc Masana, Xialei Liu, Bart#omiej Twardowski, Mikel Menta, Andrew D Bagdanov, and Joost Van De Weijer. Class-incremental learning: survey and performance evaluation on image classification. IEEE Transactions on Pattern Analysis and Machine Intelligence, 45(5):5513– 5533, 2022.   
[15] Shipeng Yan, Jiangwei Xie, and Xuming He. Der: Dynamically expandable representation for class incremental learning. In CVPR, pages 3014–3023, 2021.   
[16] Fu-Yun Wang, Da-Wei Zhou, Han-Jia Ye, and De-Chuan Zhan. Foster: Feature boosting and compression for class-incremental learning. In ECCV, pages 398–414, 2022.   
[17] Da-Wei Zhou, Qi-Wei Wang, Han-Jia Ye, and De-Chuan Zhan. A model or 603 exemplars: Towards memory-efficient class-incremental learning. In ICLR, 2023.   
[18] Arthur Douillard, Alexandre Ramé, Guillaume Couairon, and Matthieu Cord. Dytox: Transformers for continual learning with dynamic token expansion. In CVPR, pages 9285–9295, 2022.   
[19] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, et al. An image is worth 16x16 words: Transformers for image recognition at scale. In ICLR, 2020.   
[20] Zheda Mai, Ruiwen Li, Jihwan Jeong, David Quispe, Hyunwoo Kim, and Scott Sanner. Online continual learning in image classification: An empirical survey. Neurocomputing, 469:28–51, 2022.   
[21] Magdalena Marta Biesialska, Katarzyna Biesialska, and Marta Ruiz Costa-Jussà. Continual lifelong learning in natural language processing: a survey. In COLING, pages 6523–6541, 2020.   
[22] German I Parisi, Ronald Kemker, Jose L Part, Christopher Kanan, and Stefan Wermter. Continual lifelong learning with neural networks: A review. Neural Networks, 113:54–71, 2019.   
[23] Eden Belouadah, Adrian Popescu, and Ioannis Kanellos. A comprehensive study of class incremental learning algorithms for visual tasks. Neural Networks, 135:38–54, 2021.   
[24] Alex Krizhevsky, Geoffrey Hinton, et al. Learning multiple layers of features from tiny images. Technical report, 2009.

[25] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. Imagenet: A large-scale hierarchical image database. In CVPR, pages 248–255, 2009.   
[26] Jihwan Bang, Heesu Kim, YoungJoon Yoo, Jung-Woo Ha, and Jonghyun Choi. Rainbow memory: Continual learning with a memory of diverse samples. In CVPR, pages 8218–8227, 2021.   
[27] Xiaoyu Tao, Xiaopeng Hong, Xinyuan Chang, Songlin Dong, Xing Wei, and Yihong Gong. Few-shot class-incremental learning. In CVPR, pages 12183–12192, 2020.   
[28] Xialei Liu, Yu-Song Hu, Xu-Sheng Cao, Andrew D Bagdanov, Ke Li, and Ming-Ming Cheng. Long-tailed class incremental learning. In ECCV, pages 495–512, 2022.   
[29] Zheda Mai, Ruiwen Li, Hyunwoo Kim, and Scott Sanner. Supervised contrastive replay: Revisiting the nearest class mean classifier in online class-incremental continual learning. In CVPR, pages 3589–3599, 2021.   
[30] Rudolf Kruse, Sanaz Mostaghim, Christian Borgelt, Christian Braune, and Matthias Steinbrecher. Multi-layer perceptrons. In Computational intelligence: a methodological introduction, pages 53–124. 2022.   
[31] Yann LeCun, Koray Kavukcuoglu, and Clément Farabet. Convolutional networks and applications in vision. In ISCAS, pages 253–256, 2010.   
[32] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, $ukasz Kaiser, and Illia Polosukhin. Attention is all you need. In NIPS, pages 5998–6008, 2017.   
[33] Arslan Chaudhry, Puneet K Dokania, Thalaiyasingam Ajanthan, and Philip HS Torr. Riemannian walk for incremental learning: Understanding forgetting and intransigence. In ECCV, pages 532–547, 2018.   
[34] Rahaf Aljundi, Min Lin, Baptiste Goujaud, and Yoshua Bengio. Gradient based sample selection for online continual learning. In NeurIPS, pages 11816–11825, 2019.   
[35] David Isele and Akansel Cosgun. Selective experience replay for lifelong learning. In AAAI, pages 3302–3309, 2018.   
[36] Arslan Chaudhry, Albert Gordo, Puneet Kumar Dokania, Philip Torr, and David Lopez-Paz. Using hindsight to anchor past knowledge in continual learning. In AAAI, pages 6993–7001, 2020.   
[37] Matthias De Lange and Tinne Tuytelaars. Continual prototype evolution: Learning online from non-stationary data streams. In ICCV, pages 8250–8259, 2021.   
[38] Ahmet Iscen, Jeffrey Zhang, Svetlana Lazebnik, and Cordelia Schmid. Memory-efficient incremental learning through feature adaptation. In ECCV, pages 699–715, 2020.   
[39] Hanbin Zhao, Hui Wang, Yongjian Fu, Fei Wu, and Xi Li. Memoryefficient class-incremental learning for image classification. IEEE Transactions on Neural Networks and Learning Systems, 33(10):5966– 5977, 2021.   
[40] Yaoyao Liu, Yuting Su, An-An Liu, Bernt Schiele, and Qianru Sun. Mnemonics training: Multi-class incremental learning without forgetting. In CVPR, pages 12245–12254, 2020.   
[41] Hanul Shin, Jung Kwon Lee, Jaehong Kim, and Jiwon Kim. Continual learning with deep generative replay. In NIPS, pages 2990–2999, 2017.   
[42] Chen He, Ruiping Wang, Shiguang Shan, and Xilin Chen. Exemplarsupported generative reproduction for class incremental learning. In BMVC, page 98, 2018.   
[43] Wenpeng Hu, Zhou Lin, Bing Liu, Chongyang Tao, Zhengwei Tao, Jinwen Ma, Dongyan Zhao, and Rui Yan. Overcoming catastrophic forgetting for continual learning via model adaptation. In ICLR, 2019.   
[44] Ronald Kemker and Christopher Kanan. Fearnet: Brain-inspired model for incremental learning. In ICLR, 2018.   
[45] Oleksiy Ostapenko, Mihai Puscas, Tassilo Klein, Patrick Jahnichen, and Moin Nabi. Learning to remember: A synaptic plasticity driven framework for continual learning. In CVPR, pages 11321–11329, 2019.   
[46] Ye Xiang, Ying Fu, Pan Ji, and Hua Huang. Incremental learning using conditional adversarial networks. In ICCV, pages 6619–6628, 2019.   
[47] Liyuan Wang, Kuo Yang, Chongxuan Li, Lanqing Hong, Zhenguo Li, and Jun Zhu. Ordisco: Effective and efficient usage of incremental unlabeled data for semi-supervised continual learning. In CVPR, pages 5383–5392, 2021.   
[48] Jian Jiang, Edoardo Cetin, and Oya Celiktutan. Ib-drr-incremental learning with information-back discrete representation replay. In CVPRW, pages 3533–3542, 2021.   
[49] Fei Zhu, Xu-Yao Zhang, Chuang Wang, Fei Yin, and Cheng-Lin Liu. Prototype augmentation and self-supervision for incremental learning. In CVPR, pages 5871–5880, 2021.   
[50] Grégoire Petit, Adrian Popescu, Hugo Schindler, David Picard, and Bertrand Delezoide. Fetril: Feature translation for exemplar-free classincremental learning. In WACV, pages 3911–3920, 2023.

[51] Quentin Jodelet, Xin Liu, Yin Jun Phua, and Tsuyoshi Murata. Classincremental learning using diffusion model for distillation and replay. In ICCVW, pages 3425–3433, 2023.   
[52] Rui Gao and Weiwei Liu. Ddgr: continual learning with deep diffusionbased generative replay. In ICML, pages 10744–10763, 2023.   
[53] David Lopez-Paz and Marc’Aurelio Ranzato. Gradient episodic memory for continual learning. In NeurIPS, pages 6467–6476, 2017.   
[54] Arslan Chaudhry, Marc’Aurelio Ranzato, Marcus Rohrbach, and Mohamed Elhoseiny. Efficient lifelong learning with a-gem. In ICLR, 2018.   
[55] Shipeng Wang, Xiaorong Li, Jian Sun, and Zongben Xu. Training networks in null space of feature covariance for continual learning. In CVPR, pages 184–193, 2021.   
[56] Guanxiong Zeng, Yang Chen, Bo Cui, and Shan Yu. Continual learning of context-dependent processing in neural networks. Nature Machine Intelligence, 1(8):364–372, 2019.   
[57] Shixiang Tang, Dapeng Chen, Jinguo Zhu, Shijie Yu, and Wanli Ouyang. Layerwise optimization by gradient decomposition for continual learning. In CVPR, pages 9634–9643, 2021.   
[58] Matthew Riemer, Ignacio Cases, Robert Ajemian, Miao Liu, Irina Rish, Yuhai Tu, and Gerald Tesauro. Learning to learn without forgetting by maximizing transfer and minimizing interference. In ICLR, 2018.   
[59] Jaehong Yoon, Eunho Yang, Jeongtae Lee, and Sung Ju Hwang. Lifelong learning with dynamically expandable networks. In ICLR, 2018.   
[60] Ju Xu and Zhanxing Zhu. Reinforced continual learning. In NeurIPS, pages 899–908, 2018.   
[61] Xilai Li, Yingbo Zhou, Tianfu Wu, Richard Socher, and Caiming Xiong. Learn to grow: A continual structure learning framework for overcoming catastrophic forgetting. In ICML, pages 3925–3934, 2019.   
[62] Andrei A Rusu, Neil C Rabinowitz, Guillaume Desjardins, Hubert Soyer, James Kirkpatrick, Koray Kavukcuoglu, Razvan Pascanu, and Raia Hadsell. Progressive neural networks. arXiv preprint arXiv:1606.04671, 2016.   
[63] Rahaf Aljundi, Punarjay Chakravarty, and Tinne Tuytelaars. Expert gate: Lifelong learning with a network of experts. In CVPR, pages 3366–3375, 2017.   
[64] Jonathan Schwarz, Wojciech Czarnecki, Jelena Luketina, Agnieszka Grabska-Barwinska, Yee Whye Teh, Razvan Pascanu, and Raia Hadsell. Progress & compress: A scalable framework for continual learning. In ICML, pages 4528–4537, 2018.   
[65] Hanbin Zhao, Yongjian Fu, Mintong Kang, Qi Tian, Fei Wu, and Xi Li. Mgsvf: Multi-grained slow vs. fast framework for few-shot class-incremental learning. IEEE Transactions on Pattern Analysis and Machine Intelligence, 46(3):1576–1588, 2024.   
[66] Yaoyao Liu, Bernt Schiele, and Qianru Sun. Adaptive aggregation networks for class-incremental learning. In CVPR, pages 2544–2553, 2021.   
[67] Quang Pham, Chenghao Liu, and Steven Hoi. Dualnet: Continual learning, fast and slow. NeurIPS, 34:16131–16144, 2021.   
[68] Fu-Yun Wang, Da-Wei Zhou, Liu Liu, Han-Jia Ye, Yatao Bian, De-Chuan Zhan, and Peilin Zhao. Beef: Bi-compatible class-incremental learning via energy-based expansion and fusion. In ICLR, 2023.   
[69] Zifeng Wang, Zizhao Zhang, Chen-Yu Lee, Han Zhang, Ruoxi Sun, Xiaoqi Ren, Guolong Su, Vincent Perot, Jennifer Dy, and Tomas Pfister. Learning to prompt for continual learning. In CVPR, pages 139–149, 2022.   
[70] Zifeng Wang, Zizhao Zhang, Sayna Ebrahimi, Ruoxi Sun, Han Zhang, Chen-Yu Lee, Xiaoqi Ren, Guolong Su, Vincent Perot, Jennifer Dy, et al. Dualprompt: Complementary prompting for rehearsal-free continual learning. In ECCV, pages 631–648, 2022.   
[71] James Seale Smith, Leonid Karlinsky, Vyshnavi Gutta, Paola Cascante-Bonilla, Donghyun Kim, Assaf Arbelle, Rameswar Panda, Rogerio Feris, and Zsolt Kira. Coda-prompt: Continual decomposed attention-based prompting for rehearsal-free continual learning. In CVPR, pages 11909– 11919, 2023.   
[72] Yabin Wang, Zhiwu Huang, and Xiaopeng Hong. S-prompts learning with pre-trained transformers: An occam’s razor for domain incremental learning. NeurIPS, pages 5682–5695, 2022.   
[73] James Kirkpatrick, Razvan Pascanu, Neil Rabinowitz, Joel Veness, Guillaume Desjardins, Andrei A Rusu, Kieran Milan, John Quan, Tiago Ramalho, Agnieszka Grabska-Barwinska, et al. Overcoming catastrophic forgetting in neural networks. Proceedings of the national academy of sciences, 114(13):3521–3526, 2017.   
[74] Friedemann Zenke, Ben Poole, and Surya Ganguli. Continual learning through synaptic intelligence. In ICML, pages 3987–3995, 2017.

[75] Rahaf Aljundi, Francesca Babiloni, Mohamed Elhoseiny, Marcus Rohrbach, and Tinne Tuytelaars. Memory aware synapses: Learning what (not) to forget. In ECCV, pages 139–154, 2018.   
[76] Rahaf Aljundi, Klaas Kelchtermans, and Tinne Tuytelaars. Task-free continual learning. In CVPR, pages 11254–11263, 2019.   
[77] Sang-Woo Lee, Jin-Hwa Kim, Jaehyun Jun, Jung-Woo Ha, and Byoung-Tak Zhang. Overcoming catastrophic forgetting by incremental moment matching. In NIPS, pages 4652–4662, 2017.   
[78] Yang Yang, Da-Wei Zhou, De-Chuan Zhan, Hui Xiong, and Yuan Jiang. Adaptive deep models for incremental learning: Considering capacity scalability and sustainability. In KDD, pages 74–82, 2019.   
[79] Yang Yang, Da-Wei Zhou, De-Chuan Zhan, Hui Xiong, Yuan Jiang, and Jian Yang. Cost-effective incremental deep model: Matching model capacity with the least sampling. IEEE Transactions on Knowledge and Data Engineering, 35(4):3575–3588, 2021.   
[80] Janghyeon Lee, Hyeong Gwon Hong, Donggyu Joo, and Junmo Kim. Continual learning with extended kronecker-factored approximate curvature. In CVPR, pages 9001–9010, 2020.   
[81] Zhizhong Li and Derek Hoiem. Learning without forgetting. In ECCV, pages 614–629, 2016.   
[82] Sylvestre-Alvise Rebuffi, Alexander Kolesnikov, Georg Sperl, and Christoph H Lampert. icarl: Incremental classifier and representation learning. In CVPR, pages 2001–2010, 2017.   
[83] Yue Wu, Yinpeng Chen, Lijuan Wang, Yuancheng Ye, Zicheng Liu, Yandong Guo, and Yun Fu. Large scale incremental learning. In CVPR, pages 374–382, 2019.   
[84] Saihui Hou, Xinyu Pan, Chen Change Loy, Zilei Wang, and Dahua Lin. Lifelong learning via progressive distillation and retrospection. In ECCV, pages 437–452, 2018.   
[85] Kibok Lee, Kimin Lee, Jinwoo Shin, and Honglak Lee. Overcoming catastrophic forgetting with unlabeled data in the wild. In ICCV, pages 312–321, 2019.   
[86] Junting Zhang, Jie Zhang, Shalini Ghosh, Dawei Li, Serafettin Tasci, Larry Heck, Heming Zhang, and C-C Jay Kuo. Class-incremental learning via deep model consolidation. In WACV, pages 1131–1140, 2020.   
[87] James Smith, Yen-Chang Hsu, Jonathan Balloch, Yilin Shen, Hongxia Jin, and Zsolt Kira. Always be dreaming: A new approach for data-free class-incremental learning. In ICCV, pages 9374–9384, 2021.   
[88] Da-Wei Zhou, Han-Jia Ye, and De-Chuan Zhan. Co-transport for classincremental learning. In ACM MM, pages 1645–1654, 2021.   
[89] Saihui Hou, Xinyu Pan, Chen Change Loy, Zilei Wang, and Dahua Lin. Learning a unified classifier incrementally via rebalancing. In CVPR, pages 831–839, 2019.   
[90] Yichen Lu, Mei Wang, and Weihong Deng. Augmented geometric distillation for data-free incremental person reid. In CVPR, pages 7329– 7338, 2022.   
[91] Jaeyoo Park, Minsoo Kang, and Bohyung Han. Class-incremental learning for action recognition in videos. In ICCV, pages 13698–13707, 2021.   
[92] Prithviraj Dhar, Rajat Vikram Singh, Kuan-Chuan Peng, Ziyan Wu, and Rama Chellappa. Learning without memorizing. In CVPR, pages 5138–5146, 2019.   
[93] Minsoo Kang, Jaeyoo Park, and Bohyung Han. Class-incremental learning by knowledge distillation with adaptive feature consolidation. In CVPR, pages 16071–16080, 2022.   
[94] Arthur Douillard, Matthieu Cord, Charles Ollion, Thomas Robert, and Eduardo Valle. Podnet: Pooled outputs distillation for small-tasks incremental learning. In ECCV, pages 86–102, 2020.   
[95] Xinting Hu, Kaihua Tang, Chunyan Miao, Xian-Sheng Hua, and Hanwang Zhang. Distilling causal effect of data in class-incremental learning. In CVPR, pages 3957–3966, 2021.   
[96] Christian Simon, Piotr Koniusz, and Mehrtash Harandi. On learning the geodesic path for incremental learning. In CVPR, pages 1591–1600, 2021.   
[97] Heechul Jung, Jeongwoo Ju, Minju Jung, and Junmo Kim. Less-forgetful learning for domain expansion in deep neural networks. In AAAI, pages 3358–3365, 2018.   
[98] Dawei Li, Serafettin Tasci, Shalini Ghosh, Jingwen Zhu, Junting Zhang, and Larry Heck. Rilod: Near real-time incremental learning for object detection at the edge. In Proceedings of the 4th ACM/IEEE Symposium on Edge Computing, pages 113–126, 2019.   
[99] Qiankun Gao, Chen Zhao, Bernard Ghanem, and Jian Zhang. R-DFCIL: relation-guided representation learning for data-free class incremental learning. In ECCV, pages 423–439, 2022.

[100] Songlin Dong, Xiaopeng Hong, Xiaoyu Tao, Xinyuan Chang, Xing Wei, and Yihong Gong. Few-shot class-incremental learning via relation knowledge distillation. In AAAI, pages 1255–1263, 2021.   
[101] Xiaoyu Tao, Xinyuan Chang, Xiaopeng Hong, Xing Wei, and Yihong Gong. Topology-preserving class-incremental learning. In ECCV, pages 254–270, 2020.   
[102] Yu Liu, Xiaopeng Hong, Xiaoyu Tao, Songlin Dong, Jingang Shi, and Yihong Gong. Model behavior preserving for class-incremental learning. IEEE Transactions on Neural Networks and Learning Systems, 34(10):7529–7540, 2023.   
[103] Nader Asadi, MohammadReza Davari, Sudhir Mudur, Rahaf Aljundi, and Eugene Belilovsky. Prototype-sample relation distillation: towards replay-free continual learning. In ICML, pages 1093–1106, 2023.   
[104] Da-Wei Zhou, Fu-Yun Wang, Han-Jia Ye, Liang Ma, Shiliang Pu, and De-Chuan Zhan. Forward compatible few-shot class-incremental learning. In CVPR, pages 9046–9056, 2022.   
[105] Lu Yu, Bartlomiej Twardowski, Xialei Liu, Luis Herranz, Kai Wang, Yongmei Cheng, Shangling Jui, and Joost van de Weijer. Semantic drift compensation for class-incremental learning. In CVPR, pages 6982–6991, 2020.   
[106] Yujun Shi, Kuangqi Zhou, Jian Liang, Zihang Jiang, Jiashi Feng, Philip HS Torr, Song Bai, and Vincent YF Tan. Mimicking the oracle: An initial phase decorrelation approach for class incremental learning. In CVPR, pages 16722–16731, 2022.   
[107] Shibo Jie, Zhi-Hong Deng, and Ziheng Li. Alleviating representational shift for continual fine-tuning. In CVPRW, pages 3810–3819, 2022.   
[108] Pravendra Singh, Vinay Kumar Verma, Pratik Mazumder, Lawrence Carin, and Piyush Rai. Calibrating cnns for lifelong learning. In NeurIPS, pages 15579–15590, 2020.   
[109] Pravendra Singh, Pratik Mazumder, Piyush Rai, and Vinay P Namboodiri. Rectification-based knowledge retention for continual learning. In CVPR, pages 15282–15291, 2021.   
[110] Francisco M Castro, Manuel J Marín-Jiménez, Nicolás Guil, Cordelia Schmid, and Karteek Alahari. End-to-end incremental learning. In ECCV, pages 233–248, 2018.   
[111] Eden Belouadah and Adrian Popescu. Il2m: Class incremental learning with dual memory. In ICCV, pages 583–592, 2019.   
[112] Bowen Zhao, Xi Xiao, Guojun Gan, Bin Zhang, and Shu-Tao Xia. Maintaining discrimination and fairness in class incremental learning. In CVPR, pages 13208–13217, 2020.   
[113] Hongjoon Ahn, Jihwan Kwak, Subin Lim, Hyeonsu Bang, Hyojun Kim, and Taesup Moon. Ss-il: Separated softmax for incremental learning. In ICCV, pages 844–853, 2021.   
[114] Federico Pernici, Matteo Bruni, Claudio Baecchi, Francesco Turchini, and Alberto Del Bimbo. Class-incremental learning with pre-allocated fixed classifiers. In ICPR, pages 6259–6266, 2021.   
[115] Chi Zhang, Nan Song, Guosheng Lin, Yun Zheng, Pan Pan, and Yinghui Xu. Few-shot incremental learning with continually evolved classifiers. In CVPR, pages 12455–12464, 2021.   
[116] Da-Wei Zhou, Han-Jia Ye, De-Chuan Zhan, and Ziwei Liu. Revisiting class-incremental learning with pre-trained models: Generalizability and adaptivity are all you need. arXiv preprint arXiv:2303.07338, 2023.   
[117] Mark D McDonnell, Dong Gong, Amin Parveneh, Ehsan Abbasnejad, and Anton van den Hengel. Ranpac: Random projections and pre-trained models for continual learning. In NeurIPS, 2023.   
[118] Dipam Goswami, Yuyang Liu, Bart#omiej Twardowski, and Joost van de Weijer. Fecam: Exploiting the heterogeneity of class distributions in exemplar-free continual learning. In NeurIPS, 2023.   
[119] Qi-Wei Wang, Da-Wei Zhou, Yi-Kai Zhang, De-Chuan Zhan, and Han-Jia Ye. Few-shot class-incremental learning via training-free prototype calibration. In NeurIPS, 2023.   
[120] Wuxuan Shi and Mang Ye. Prototype reminiscence and augmented asymmetric knowledge aggregation for non-exemplar class-incremental learning. In ICCV, pages 1772–1781, 2023.   
[121] Da-Wei Zhou, Han-Jia Ye, Liang Ma, Di Xie, Shiliang Pu, and De-Chuan Zhan. Few-shot class-incremental learning by sampling multi-phase tasks. IEEE Transactions on Pattern Analysis and Machine Intelligence, 45(11):12816–12831, 2023.   
[122] Kun Wei, Cheng Deng, Xu Yang, and Maosen Li. Incremental embedding learning via zero-shot translation. In AAAI, pages 10254–10262, 2021.   
[123] Gido M Van De Ven, Zhe Li, and Andreas S Tolias. Class-incremental learning with generative classifiers. In CVPRW, pages 3611–3620, 2021.   
[124] Max Welling. Herding dynamical weights to learn. In ICML, pages 1121–1128, 2009.   
[125] Matthew A Wilson and Bruce L McNaughton. Reactivation of hippocampal ensemble memories during sleep. Science, 265(5172):676– 679, 1994.

[126] Arielle Tambini and Lila Davachi. Persistence of hippocampal multivoxel patterns into postencoding rest is related to memory. Proceedings of the National Academy of Sciences, 110(48):19591–19596, 2013.   
[127] Daniel N Barry and Bradley C Love. A neural network account of memory replay and knowledge consolidation. Cerebral Cortex, 33(1):83– 95, 2023.   
[128] Roger Ratcliff. Connectionist models of recognition memory: constraints imposed by learning and forgetting functions. Psychological review, 97(2):285, 1990.   
[129] Jake Snell, Kevin Swersky, and Richard Zemel. Prototypical networks for few-shot learning. In NIPS, pages 4080–4090, 2017.   
[130] Amal Rannen, Rahaf Aljundi, Matthew B Blaschko, and Tinne Tuytelaars. Encoder based lifelong learning. In ICCV, pages 1320–1328, 2017.   
[131] Arun Mallya and Svetlana Lazebnik. Packnet: Adding multiple tasks to a single network by iterative pruning. In CVPR, pages 7765–7773, 2018.   
[132] Jathushan Rajasegaran, Munawar Hayat, Salman Khan, Fahad Shahbaz Khan, and Ling Shao. Random path selection for incremental learning. In NeurIPS, pages 12669–12679, 2019.   
[133] Dongmin Park, Seokil Hong, Bohyung Han, and Kyoung Mu Lee. Continual learning by asymmetric loss approximation with single-side overestimation. In ICCV, pages 3335–3344, 2019.   
[134] Mohammad Rostami, Soheil Kolouri, and Praveen K Pilly. Complementary learning for overcoming catastrophic forgetting using experience replay. In IJCAI, pages 3339–3345, 2019.   
[135] Ching-Yi Hung, Cheng-Hao Tu, Cheng-En Wu, Chien-Hung Chen, Yi-Ming Chan, and Chu-Song Chen. Compacting, picking and growing for unforgetting continual learning. NeurIPS, 32:13669–13679, 2019.   
[136] Davide Abati, Jakub Tomczak, Tijmen Blankevoort, Simone Calderara, Rita Cucchiara, and Babak Ehteshami Bejnordi. Conditional channel gated networks for task-aware continual learning. In CVPR, pages 3931–3940, 2020.   
[137] KJ Joseph, Jathushan Rajasegaran, Salman Khan, Fahad Shahbaz Khan, and Vineeth N Balasubramanian. Incremental object detection via meta-learning. IEEE Transactions on Pattern Analysis and Machine Intelligence, 44(12):9209–9216, 2021.   
[138] Jiangpeng He, Runyu Mao, Zeman Shao, and Fengqing Zhu. Incremental learning in online scenario. In CVPR, pages 13926–13935, 2020.   
[139] Pietro Buzzega, Matteo Boschini, Angelo Porrello, Davide Abati, and Simone Calderara. Dark experience for general continual learning: a strong, simple baseline. NeurIPS, 33:15920–15930, 2020.   
[140] Ameya Prabhu, Philip HS Torr, and Puneet K Dokania. Gdumb: A simple approach that questions our progress in continual learning. In ECCV, pages 524–540, 2020.   
[141] Chris Dongjoo Kim, Jinseo Jeong, and Gunhee Kim. Imbalanced continual learning with partitioning reservoir sampling. In ECCV, pages 411–428, 2020.   
[142] Tyler L Hayes and Christopher Kanan. Lifelong machine learning with deep streaming linear discriminant analysis. In CVPRW, pages 220–221, 2020.   
[143] Yu Liu, Sarah Parisot, Gregory Slabaugh, Xu Jia, Ales Leonardis, and Tinne Tuytelaars. More classifiers, less forgetting: A generic multiclassifier paradigm for incremental learning. In ECCV, pages 699–716, 2020.   
[144] Yaoyao Liu, Bernt Schiele, and Qianru Sun. Rmm: Reinforced memory management for class-incremental learning. NeurIPS, 34:3478–3490, 2021.   
[145] Haiyan Yin, Ping Li, et al. Mitigating forgetting in online continual learning with neuron calibration. NeurIPS, 34:10260–10272, 2021.   
[146] Rishabh Tiwari, Krishnateja Killamsetty, Rishabh Iyer, and Pradeep Shenoy. Gcr: Gradient coreset based replay buffer selection for continual learning. In CVPR, pages 99–108, 2022.   
[147] KJ Joseph, Salman Khan, Fahad Shahbaz Khan, Rao Muhammad Anwer, and Vineeth N Balasubramanian. Energy-based latent aligner for incremental learning. In CVPR, pages 7452–7461, 2022.   
[148] Jiangwei Xie, Shipeng Yan, and Xuming He. General incremental learning with domain-aware categorical representations. In CVPR, pages 14351–14360, 2022.   
[149] Jiahua Dong, Lixu Wang, Zhen Fang, Gan Sun, Shichao Xu, Xiao Wang, and Qi Zhu. Federated class-incremental learning. In CVPR, pages 10164–10173, 2022.   
[150] Kai Zhu, Wei Zhai, Yang Cao, Jiebo Luo, and Zheng-Jun Zha. Selfsustaining representation expansion for non-exemplar class-incremental learning. In CVPR, pages 9296–9305, 2022.   
[151] Tz-Ying Wu, Gurumurthy Swaminathan, Zhizhong Li, Avinash Ravichandran, Nuno Vasconcelos, Rahul Bhotika, and Stefano Soatto. Classincremental learning with strong pre-trained models. In CVPR, pages 9601–9610, 2022.

[152] Beyza Ermis, Giovanni Zappella, Martin Wistuba, Aditya Rawal, and Cedric Archambeau. Memory efficient continual learning with transformers. NeurIPS, pages 10629–10642, 2022.   
[153] Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, and Yoshua Bengio. Generative adversarial nets. In NIPS, pages 2672–2680, 2014.   
[154] Diederik P Kingma and Max Welling. Auto-encoding variational bayes. In ICLR, 2014.   
[155] Mehdi Mirza and Simon Osindero. Conditional generative adversarial nets. arXiv preprint arXiv:1411.1784, 2014.   
[156] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. NeurIPS, 33:6840–6851, 2020.   
[157] Micha# Zaj ˛ac, Kamil Deja, Anna Kuzina, Jakub M Tomczak, Tomasz Trzcinski, Florian Shkurti, and Piotr Mi ´ #os. Exploring continual learning ´ of diffusion models. arXiv preprint arXiv:2303.15342, 2023.   
[158] James Seale Smith, Yen-Chang Hsu, Lingyu Zhang, Ting Hua, Zsolt Kira, Yilin Shen, and Hongxia Jin. Continual diffusion: Continual customization of text-to-image diffusion with c-lora. arXiv preprint arXiv:2304.06027, 2023.   
[159] Lukasz Korycki and Bartosz Krawczyk. Class-incremental experience replay for continual learning under concept drift. In CVPR, pages 3649–3658, 2021.   
[160] Andrea Maracani, Umberto Michieli, Marco Toldo, and Pietro Zanuttigh. Recall: Replay-based continual learning in semantic segmentation. In ICCV, pages 7026–7035, 2021.   
[161] Andrés Villa, Kumail Alhamoud, Victor Escorcia, Fabian Caba, Juan León Alcázar, and Bernard Ghanem. vclimb: A novel video class incremental learning benchmark. In CVPR, pages 19035–19044, 2022.   
[162] Eli Verwimp, Matthias De Lange, and Tinne Tuytelaars. Rehearsal revealed: The limits and merits of revisiting samples in continual learning. In ICCV, pages 9385–9394, 2021.   
[163] Lorenzo Bonicelli, Matteo Boschini, Angelo Porrello, Concetto Spampinato, and Simone Calderara. On the effectiveness of lipschitz-driven rehearsal in continual learning. NeurIPS, pages 31886–31901, 2022.   
[164] Longhui Yu, Tianyang Hu, Lanqing Hong, Zhen Liu, Adrian Weller, and Weiyang Liu. Continual learning by modeling intra-class variation. arXiv preprint arXiv:2210.05398, 2022.   
[165] Yifan Zhang, Bingyi Kang, Bryan Hooi, Shuicheng Yan, and Jiashi Feng. Deep long-tailed learning: A survey. IEEE Transactions on Pattern Analysis and Machine Intelligence, 45(9):10795–10816, 2023.   
[166] Gido M Van de Ven, Hava T Siegelmann, and Andreas S Tolias. Braininspired replay for continual learning with artificial neural networks. Nature communications, 11(1):4069, 2020.   
[167] Liyuan Wang, Bo Lei, Qian Li, Hang Su, Jun Zhu, and Yi Zhong. Triplememory networks: A brain-inspired method for continual learning. IEEE Transactions on Neural Networks and Learning Systems, 33(5):1925– 1934, 2021.   
[168] Ryota Yoshihashi, Wen Shao, Rei Kawakami, Shaodi You, Makoto Iida, and Takeshi Naemura. Classification-reconstruction learning for open-set recognition. In CVPR, pages 4016–4025, 2019.   
[169] Xialei Liu, Chenshen Wu, Mikel Menta, Luis Herranz, Bogdan Raducanu, Andrew D Bagdanov, Shangling Jui, and Joost van de Weijer. Generative feature replay for class-incremental learning. In CVPRW, pages 226–227, 2020.   
[170] Yiduo Guo, Wenpeng Hu, Dongyan Zhao, and Bing Liu. Adaptive orthogonal projection for batch and online continual learning. In AAAI, pages 6783–6791, 2022.   
[171] Chelsea Finn, Pieter Abbeel, and Sergey Levine. Model-agnostic metalearning for fast adaptation of deep networks. In ICML, pages 1126–1135, 2017.   
[172] Wei-Lun Chao, Han-Jia Ye, De-Chuan Zhan, Mark Campbell, and Kilian Q Weinberger. Revisiting meta-learning as supervised learning. arXiv preprint arXiv:2002.00573, 2020.   
[173] Jathushan Rajasegaran, Salman Khan, Munawar Hayat, Fahad Shahbaz Khan, and Mubarak Shah. itaml: An incremental task-agnostic metalearning approach. In CVPR, pages 13588–13597, 2020.   
[174] Runqi Wang, Yuxiang Bao, Baochang Zhang, Jianzhuang Liu, Wentao Zhu, and Guodong Guo. Anti-retroactive interference for lifelong learning. In ECCV, pages 163–178, 2022.   
[175] Ian Goodfellow, Yoshua Bengio, and Aaron Courville. Deep learning. MIT press, 2016.   
[176] Thomas Elsken, Jan Hendrik Metzen, and Frank Hutter. Neural architecture search: A survey. The Journal of Machine Learning Research, 20(1):1997–2017, 2019.   
[177] Zhi-Hua Zhou. Ensemble methods: foundations and algorithms. CRC press, 2012.

[178] Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. Distilling the knowledge in a neural network. arXiv preprint arXiv:1503.02531, 2015.   
[179] Menglin Jia, Luming Tang, Bor-Chun Chen, Claire Cardie, Serge J. Belongie, Bharath Hariharan, and Ser-Nam Lim. Visual prompt tuning. In ECCV, pages 709–727, 2022.   
[180] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning transferable visual models from natural language supervision. In ICML, pages 8748–8763, 2021.   
[181] Da-Wei Zhou, Hai-Long Sun, Jingyi Ning, Han-Jia Ye, and De-Chuan Zhan. Continual learning with pre-trained models: A survey. In IJCAI, 2024.   
[182] Da-Wei Zhou, Hai-Long Sun, Han-Jia Ye, and De-Chuan Zhan. Expandable subspace ensemble for pre-trained model-based class-incremental learning. In CVPR, pages 23554–23564, 2024.   
[183] Da-Wei Zhou, Yuanhan Zhang, Jingyi Ning, Han-Jia Ye, De-Chuan Zhan, and Ziwei Liu. Learning without forgetting for vision-language models. arXiv preprint arXiv:2305.19270, 2023.   
[184] Hyuntak Cha, Jaeho Lee, and Jinwoo Shin. Co2l: Contrastive continual learning. In ICCV, pages 9516–9525, 2021.   
[185] Yu-Ming Tang, Yi-Xing Peng, and Wei-Shi Zheng. When prompt-based incremental learning does not meet strong pretraining. In ICCV, pages 1706–1716, 2023.   
[186] Oleksiy Ostapenko, Pau Rodriguez, Massimo Caccia, and Laurent Charlin. Continual learning via local module composition. NeurIPS, 34:30298–30312, 2021.   
[187] Sylvestre-Alvise Rebuffi, Hakan Bilen, and Andrea Vedaldi. Learning multiple visual domains with residual adapters. In NIPS, pages 506–516, 2017.   
[188] Lucien Le Cam. Asymptotic methods in statistical decision theory. Springer Science & Business Media, 2012.   
[189] Frederik Benzing. Unifying importance based regularisation methods for continual learning. In AISTATS, pages 2372–2396, 2022.   
[190] Thomas Mensink, Jakob Verbeek, Florent Perronnin, and Gabriela Csurka. Distance-based image classification: Generalizing to new classes at near-zero cost. IEEE Transactions on Pattern Analysis and Machine Intelligence, 35(11):2624–2637, 2013.   
[191] Hanbin Zhao, Xin Qin, Shihao Su, Yongjian Fu, Zibo Lin, and Xi Li. When video classification meets incremental classes. In ACM MM, pages 880–889, 2021.   
[192] Wonpyo Park, Dongju Kim, Yan Lu, and Minsu Cho. Relational knowledge distillation. In CVPR, pages 3967–3976, 2019.   
[193] Guanglei Yang, Enrico Fini, Dan Xu, Paolo Rota, Mingli Ding, Moin Nabi, Xavier Alameda-Pineda, and Elisa Ricci. Uncertainty-aware contrastive distillation for incremental semantic segmentation. IEEE Transactions on Pattern Analysis and Machine Intelligence, 45(2):2567– 2581, 2023.   
[194] Nan Pu, Wei Chen, Yu Liu, Erwin M Bakker, and Michael S Lew. Lifelong person re-identification via adaptive knowledge accumulation. In CVPR, pages 7901–7910, 2021.   
[195] Bowen Zheng, Da-Wei Zhou, Han-Jia Ye, and De-Chuan Zhan. Multilayer rehearsal feature augmentation for class-incremental learning. In ICML, 2024.   
[196] Quang Pham, Chenghao Liu, and HOI Steven. Continual normalization: Rethinking batch normalization for online continual learning. In ICLR, 2022.   
[197] Sergey Ioffe and Christian Szegedy. Batch normalization: Accelerating deep network training by reducing internal covariate shift. In ICML, pages 448–456, 2015.   
[198] Bowen Zheng, Da-Wei Zhou, Han-Jia Ye, and De-Chuan Zhan. Preserving locality in vision transformers for class incremental learning. In ICME, pages 1157–1162, 2023.   
[199] Guangyuan Shi, Jiaxin Chen, Wenlong Zhang, Li-Ming Zhan, and Xiao-Ming Wu. Overcoming catastrophic forgetting in incremental few-shot learning by finding flat minima. In NeurIPS, pages 6747–6761, 2021.   
[200] Seyed Iman Mirzadeh, Mehrdad Farajtabar, Razvan Pascanu, and Hassan Ghasemzadeh. Understanding the role of training regimes in continual learning. NeurIPS, 33:7308–7320, 2020.   
[201] Robert M Nosofsky. Attention, similarity, and the identification– categorization relationship. Journal of experimental psychology: General, 115(1):39, 1986.   
[202] Vikas Verma, Alex Lamb, Christopher Beckham, Amir Najafi, Ioannis Mitliagkas, David Lopez-Paz, and Yoshua Bengio. Manifold mixup: Better representations by interpolating hidden states. In ICML, pages 6438–6447, 2019.

[203] Dan Hendrycks, Kevin Zhao, Steven Basart, Jacob Steinhardt, and Dawn Song. Natural adversarial examples. In CVPR, pages 15262–15271, 2021.   
[204] Amit Alfassy, Assaf Arbelle, Oshri Halimi, Sivan Harary, Roei Herzig, Eli Schwartz, Rameswar Panda, Michele Dolfi, Christoph Auer, Peter Staar, et al. Feta: Towards specializing foundational models for expert task applications. In NeurIPS, pages 29873–29888, 2022.   
[205] Yann LeCun, Sumit Chopra, Raia Hadsell, M Ranzato, and Fujie Huang. A tutorial on energy-based learning. Predicting structured data, 1(0), 2006.   
[206] Shuang Li, Yilun Du, Gido van de Ven, and Igor Mordatch. Energy-based models for continual learning. In CoLLAs, pages 1–22, 2022.   
[207] Olga Russakovsky, Jia Deng, Hao Su, Jonathan Krause, Sanjeev Satheesh, Sean Ma, Zhiheng Huang, Andrej Karpathy, Aditya Khosla, Michael Bernstein, et al. Imagenet large scale visual recognition challenge. IJCV, 115(3):211–252, 2015.   
[208] Yann LeCun, Corinna Cortes, and CJ Burges. Mnist handwritten digit database. AT&T Labs [Online]. Available: http://yann. lecun. com/exdb/mnist, 2:18, 2010.   
[209] C. Wah, S. Branson, P. Welinder, P. Perona, and S. Belongie. The Caltech-UCSD Birds-200-2011 Dataset. Technical Report CNS-TR-2011-001, California Institute of Technology, 2011.   
[210] Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, et al. Pytorch: An imperative style, high-performance deep learning library. In NeurIPS, pages 8026–8037, 2019.   
[211] Da-Wei Zhou, Fu-Yun Wang, Han-Jia Ye, and De-Chuan Zhan. Pycil: a python toolbox for class-incremental learning. SCIENCE CHINA Information Sciences, 66(9):197101, 2023.   
[212] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In CVPR, pages 770–778, 2015.   
[213] Stéphane d’Ascoli, Hugo Touvron, Matthew L Leavitt, Ari S Morcos, Giulio Biroli, and Levent Sagun. Convit: Improving vision transformers with soft convolutional inductive biases. In ICML, pages 2286–2296, 2021.   
[214] Yi Zhong, Jia-Hui Pan, Haoxin Li, and Wei-Shi Zheng. Weakly supervised action anticipation without object annotations. Frontiers of Computer Science, 17(2):172313, 2023.   
[215] Da-Wei Zhou, Han-Jia Ye, and De-Chuan Zhan. Learning placeholders for open-set recognition. In CVPR, pages 4401–4410, 2021.   
[216] Huiping Zhuang, Zhenyu Weng, Run He, Zhiping Lin, and Ziqian Zeng. GKEAL: Gaussian kernel embedded analytic learning for few-shot class incremental task. In CVPR, pages 7746–7755, 2023.   
[217] Shipeng Yan, Lanqing Hong, Hang Xu, Jianhua Han, Tinne Tuytelaars, Zhenguo Li, and Xuming He. Generative negative text replay for continual vision-language pretraining. In ECCV, pages 22–38, 2022.   
[218] Amanda Rios, Nilesh Ahuja, Ibrahima Ndiour, Utku Genc, Laurent Itti, and Omesh Tickoo. incdfm: Incremental deep feature modeling for continual novelty detection. In ECCV, pages 588–604, 2022.   
[219] Abhijit Bendale and Terrance Boult. Towards open world recognition. In CVPR, pages 1893–1902, 2015.   
[220] Mohamed Abdelsalam, Mojtaba Faramarzi, Shagun Sodhani, and Sarath Chandar. Iirc: Incremental implicitly-refined classification. In CVPR, pages 11038–11047, 2021.   
[221] Yiduo Guo, Bing Liu, and Dongyan Zhao. Online continual learning through mutual information maximization. In ICML, pages 8109–8126, 2022.   
[222] Julien Pourcel, Ngoc-Son Vu, and Robert M French. Online task-free continual learning with dynamic sparse distributed memory. In ECCV, pages 739–756, 2022.   
[223] Fei Zhu, Zhen Cheng, Xu-yao Zhang, and Cheng-lin Liu. Classincremental learning via dual augmentation. NeurIPS, pages 14306– 14318, 2021.   
[224] Huiping Zhuang, Zhenyu Weng, Hongxin Wei, Renchunzi Xie, Kar-Ann Toh, and Zhiping Lin. ACIL: Analytic class-incremental learning with absolute memorization and privacy protection. In NeurIPS, pages 11602–11614, 2022.   
[225] Huiping Zhuang, Run He, Kai Tong, Ziqian Zeng, Cen Chen, and Zhiping Lin. DS-AL: A dual-stream analytic learning for exemplar-free class-incremental learning. In AAAI, pages 17237–17244, 2024.   
[226] Yaoyao Liu, Yingying Li, Bernt Schiele, and Qianru Sun. Online hyperparameter optimization for class-incremental learning. In AAAI, pages 8906–8913, 2023.   
[227] Zifeng Wang, Zheng Zhan, Yifan Gong, Geng Yuan, Wei Niu, Tong Jian, Bin Ren, Stratis Ioannidis, Yanzhi Wang, and Jennifer Dy. Sparcl: Sparse continual learning on the edge. NeurIPS, pages 20366–20380, 2022.

[228] Ameya Prabhu, Hasan Abed Al Kader Hammoud, Puneet K Dokania, Philip HS Torr, Ser-Nam Lim, Bernard Ghanem, and Adel Bibi. Computationally budgeted continual learning: What does matter? In CVPR, pages 3698–3707, 2023.   
[229] Ovidiu Gheorghioiu, Alexandru Salcianu, and Martin Rinard. Interprocedural compatibility analysis for static object preallocation. In POPL, pages 273–284, 2003.   
[230] Santosh Nagarakatte, Jianzhou Zhao, Milo MK Martin, and Steve Zdancewic. Softbound: Highly compatible and complete spatial memory safety for c. In PLDI, pages 245–258, 2009.   
[231] Pradeep Varma, Rudrapatna K Shyamasundar, and Harshit J Shah. Backward-compatible constant-time exception-protected memory. In FSE/ESEC, pages 71–80, 2009.   
[232] Wei Xu, Daniel C DuVarney, and R Sekar. An efficient and backwardscompatible transformation to ensure memory safety of c programs. In FSE, pages 117–126, 2004.   
[233] Gagan Bansal, Besmira Nushi, Ece Kamar, Daniel S Weld, Walter S Lasecki, and Eric Horvitz. Updates in human-ai teams: Understanding and addressing the performance/compatibility tradeoff. In AAAI, pages 2429–2437, 2019.   
[234] Megha Srivastava, Besmira Nushi, Ece Kamar, Shital Shah, and Eric Horvitz. An empirical analysis of backward compatibility in machine learning systems. In KDD, pages 3272–3280, 2020.   
[235] Gyuhak Kim, Changnan Xiao, Tatsuya Konishi, Zixuan Ke, and Bing Liu. A theoretical study on solving continual learning. NeurIPS, pages 5065–5079, 2022.   
[236] Lucas Caccia, Rahaf Aljundi, Nader Asadi, Tinne Tuytelaars, Joelle Pineau, and Eugene Belilovsky. New insights on reducing abrupt representation change in online continual learning. In ICLR, 2022.   
[237] Martin Arjovsky, Soumith Chintala, and Léon Bottou. Wasserstein gan. arxiv 2017. arXiv preprint arXiv:1701.07875, 30(4), 2017.   
[238] Youngmin Oh, Donghyeon Baek, and Bumsub Ham. Alife: Adaptive logit regularizer and feature replay for incremental semantic segmentation. In NeurIPS, 2022.   
[239] Fabio Cermelli, Dario Fontanel, Antonio Tavera, Marco Ciccone, and Barbara Caputo. Incremental learning in semantic segmentation from image labels. In CVPR, pages 4371–4381, 2022.   
[240] Chang-Bin Zhang, Jia-Wen Xiao, Xialei Liu, Ying-Cong Chen, and Ming-Ming Cheng. Representation compensation networks for continual semantic segmentation. In CVPR, pages 7053–7064, 2022.   
[241] Fabio Cermelli, Massimiliano Mancini, Samuel Rota Bulo, Elisa Ricci, and Barbara Caputo. Modeling the background for incremental learning in semantic segmentation. In CVPR, pages 9233–9242, 2020.   
[242] Juan-Manuel Perez-Rua, Xiatian Zhu, Timothy M Hospedales, and Tao Xiang. Incremental few-shot object detection. In CVPR, pages 13846– 13855, 2020.   
[243] Konstantin Shmelkov, Cordelia Schmid, and Karteek Alahari. Incremental learning of object detectors without catastrophic forgetting. In ICCV, pages 3400–3409, 2017.   
[244] KJ Joseph, Salman Khan, Fahad Shahbaz Khan, and Vineeth N Balasubramanian. Towards open world object detection. In CVPR, pages 5830–5840, 2021.   
[245] Jianren Wang, Xin Wang, Yue Shang-Guan, and Abhinav Gupta. Wanderlust: Online continual object detection in the real world. In ICCV, pages 10829–10838, 2021.   
[246] Na Dong, Yongqiang Zhang, Mingli Ding, and Gim Hee Lee. Bridging non co-occurrence with unlabeled in-the-wild data for incremental object detection. NeurIPS, 34:30492–30503, 2021.   
[247] Tao Feng, Mang Wang, and Hangjie Yuan. Overcoming catastrophic forgetting in incremental object detection via elastic response distillation. In CVPR, pages 9427–9436, 2022.   
[248] Minh H Vu, Gabriella Norman, Tufve Nyholm, and Tommy Löfstedt. A data-adaptive loss function for incomplete data and incremental learning in semantic image segmentation. IEEE Transactions on Medical Imaging, 41(6):1320–1330, 2021.   
[249] Mengya Xu, Mobarakol Islam, Chwee Ming Lim, and Hongliang Ren. Class-incremental domain adaptation with smoothing and calibration for surgical report generation. In MICCAI, pages 269–278. Springer, 2021.   
[250] Tongtong Wu, Massimo Caccia, Zhuang Li, Yuan-Fang Li, Guilin Qi, and Gholamreza Haffari. Pretrained language model in continual learning: A comparative study. In ICLR, 2022.   
[251] Joel Jang, Seonghyeon Ye, Sohee Yang, Joongbo Shin, Janghoon Han, KIM Gyeonghun, Stanley Jungkyu Choi, and Minjoon Seo. Towards continual knowledge learning of language models. In ICLR, 2022.   
[252] Chengwei Qin and Shafiq Joty. Lfpt5: A unified framework for lifelong few-shot language learning based on prompt tuning of t5. In ICLR, 2022.

[253] Tomasz Korbak, Hady Elsahar, Germán Kruszewski, and Marc Dymetman. On reinforcement learning and distribution matching for finetuning language models with no catastrophic forgetting. arXiv preprint arXiv:2206.00761, 2022.   
[254] Tejas Srinivasan, Ting-Yun Chang, Leticia Pinto Alva, Georgios Chochlakis, Mohammad Rostami, and Jesse Thomason. Climb: A continual learning benchmark for vision-and-language tasks. In NeurIPS, pages 29440–29453, 2022.   
[255] Ross Girshick. Fast r-cnn. In ICCV, pages 1440–1448, 2015.   
[256] Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun. Faster r-cnn: Towards real-time object detection with region proposal networks. In NIPS, pages 91–99, 2015.   
[257] Xiang Li, Wenhai Wang, Lijun Wu, Shuo Chen, Xiaolin Hu, Jun Li, Jinhui Tang, and Jian Yang. Generalized focal loss: Learning qualified and distributed bounding boxes for dense object detection. NeurIPS, 33:21002–21012, 2020.   
[258] Tsung-Yi Lin, Priya Goyal, Ross Girshick, Kaiming He, and Piotr Dollár. Focal loss for dense object detection. In ICCV, pages 2980–2988, 2017.   
[259] Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas Usunier, Alexander Kirillov, and Sergey Zagoruyko. End-to-end object detection with transformers. In ECCV, pages 213–229, 2020.   
[260] Xingyi Zhou, Dequan Wang, and Philipp Krähenbühl. Objects as points. arXiv preprint arXiv:1904.07850, 2019.   
[261] Dongbao Yang, Yu Zhou, Aoting Zhang, Xurui Sun, Dayan Wu, Weiping Wang, and Qixiang Ye. Multi-view correlation distillation for incremental object detection. Pattern Recognition, 131:108863, 2022.   
[262] Wang Zhou, Shiyu Chang, Norma Sosa, Hendrik Hamann, and David Cox. Lifelong object detection. arXiv preprint arXiv:2009.01129, 2020.   
[263] Li Chen, Chunyan Yu, and Lvcai Chen. A new knowledge distillation for incremental object detection. In IJCNN, pages 1–7, 2019.   
[264] Yu Hao, Yanwei Fu, Yu-Gang Jiang, and Qi Tian. An end-to-end architecture for class-incremental object detection with knowledge distillation. In ICME, pages 1–6, 2019.   
[265] Can Peng, Kun Zhao, and Brian C Lovell. Faster ilod: Incremental learning for object detectors based on faster rcnn. Pattern recognition letters, 140:109–115, 2020.   
[266] Xialei Liu, Hao Yang, Avinash Ravichandran, Rahul Bhotika, and Stefano Soatto. Multi-task incremental learning for object detection. arXiv preprint arXiv:2002.05347, 2020.   
[267] Yaoyao Liu, Bernt Schiele, Andrea Vedaldi, and Christian Rupprecht. Continual detection transformer for incremental object detection. In CVPR, pages 23799–23808, 2023.   
[268] Xizhou Zhu, Weijie Su, Lewei Lu, Bin Li, Xiaogang Wang, and Jifeng Dai. Deformable detr: Deformable transformers for end-to-end object detection. arXiv preprint arXiv:2010.04159, 2020.   
[269] Zhigang Dai, Bolun Cai, Yugeng Lin, and Junying Chen. Up-detr: Unsupervised pre-training for object detection with transformers. In CVPR, pages 1601–1610, 2021.   
[270] Li Yin, Juan M Perez-Rua, and Kevin J Liang. Sylph: A hypernetwork framework for incremental few-shot object detection. In CVPR, pages 9035–9045, 2022.   
[271] Meng Cheng, Hanli Wang, and Yu Long. Meta-learning-based incremental few-shot object detection. IEEE Transactions on Circuits and Systems for Video Technology, 32(4):2158–2169, 2021.   
[272] Pengyang Li, Yanan Li, Han Cui, and Donghui Wang. Class-incremental few-shot object detection. arXiv preprint arXiv:2105.07637, 2021.   
[273] Na Zhao and Gim Hee Lee. Static-dynamic co-teaching for classincremental 3d object detection. In AAAI, pages 3436–3445, 2022.   
[274] Umberto Michieli and Pietro Zanuttigh. Incremental learning techniques for semantic segmentation. In ICCV Workshop, pages 3205–3212, 2019.   
[275] Arthur Douillard, Yifu Chen, Arnaud Dapogny, and Matthieu Cord. Plop: Learning without forgetting for continual semantic segmentation. In CVPR, pages 4040–4050, 2021.   
[276] Umberto Michieli and Pietro Zanuttigh. Continual semantic segmentation via repulsion-attraction of sparse and disentangled latent representations. In CVPR, pages 1114–1124, 2021.   
[277] Sungmin Cha, YoungJoon Yoo, Taesup Moon, et al. Ssul: Semantic segmentation with unknown label for exemplar-based class-incremental learning. NeurIPS, 34:10919–10930, 2021.   
[278] Shipeng Yan, Jiale Zhou, Jiangwei Xie, Songyang Zhang, and Xuming He. An em framework for online incremental learning of semantic segmentation. In ACM MM, pages 3052–3060, 2021.   
[279] Lanyun Zhu, Tianrun Chen, Jianxiong Yin, Simon See, and Jun Liu. Continual semantic segmentation with automatic memory sample selection. In CVPR, pages 3082–3092, 2023.

[280] Lu Yu, Xialei Liu, and Joost Van de Weijer. Self-training for classincremental semantic segmentation. IEEE Trans. Neural Networks Learn. Syst., 34(11):9116–9127, 2023.   
[281] Jia-Wen Xiao, Chang-Bin Zhang, Jiekang Feng, Xialei Liu, Joost van de Weijer, and Ming-Ming Cheng. Endpoints weight fusion for class incremental semantic segmentation. In CVPR, pages 7204–7213, 2023.   
[282] Zihan Lin, Zilei Wang, and Yixin Zhang. Preparing the future for continual semantic segmentation. In ICCV, pages 11910–11920, 2023.   
[283] Fabio Cermelli, Massimiliano Mancini, Yongqin Xian, Zeynep Akata, and Barbara Caputo. Prototype-based incremental few-shot semantic segmentation. arXiv preprint arXiv:2012.01415, 2020.   
[284] Guangchen Shi, Yirui Wu, Jun Liu, Shaohua Wan, Wenhai Wang, and Tong Lu. Incremental few-shot semantic segmentation via embedding adaptive-update and hyper-class representation. In ACM MM, pages 5547–5556, 2022.   
[285] Tobias Kalb and Jürgen Beyerer. Principles of forgetting in domainincremental semantic segmentation in adverse weather conditions. In CVPR, pages 19508–19518, 2023.   
[286] Serban Stan and Mohammad Rostami. Unsupervised model adaptation for continual semantic segmentation. In AAAI, pages 2593–2601, 2021.   
[287] Yanan Gu, Cheng Deng, and Kun Wei. Class-incremental instance segmentation via multi-teacher networks. In AAAI, pages 1478–1486, 2021.   
[288] Dan Andrei Ganea, Bas Boom, and Ronald Poppe. Incremental few-shot instance segmentation. In CVPR, pages 1185–1194, 2021.   
[289] Chaohui Yu, Qiang Zhou, Jingliang Li, Jianlong Yuan, Zhibin Wang, and Fan Wang. Foundation model drives weakly incremental learning for semantic segmentation. In CVPR, pages 23685–23694, 2023.

# Supplementary Material

The supplementary material mainly contains additional experiments that cannot be reported due to page limit, which is organized as follows:

• Section A provides extra results in benchmark comparison, including detailed results on CIFAR100, ImageNet100, and Top-5 accuracy on ImageNet.   
• Section B provides visualization results on the confusion matrix and weight norm.   
• Section C provides extra results on other settings in the memory-aligned comparison.   
• Section D reports the detailed implementations of the AUC-A/L measure, including the per-point setting of memory, backbone, and incremental performance.   
• Section E reports the incremental learning performance (per-stage accuracy) of different methods in the benchmark comparison.   
• Section F reports the extra evaluation measures, i.e., forgetting and intransigence among all compared methods.   
• Section G conducts experiments on the type of replay strategies, including direct replay, feature replay, and generative replay.   
• Section H gives a detailed introduction about selected compared methods in the main paper.   
• Section I discusses the taxonomy in the main paper and introduces the related topics about incremental object detection and semantic segmentation.   
• Section J explores further analysis in class-incremental learning, including the influence of exemplars and computational efficiency.

# APPENDIX A

# SUPPLIED RESULTS IN BENCHMARK COMPARISON

In this section, we report the full results of the benchmark comparison. With a bit of redundancy, we list the incremental performance of all dataset splits. Specifically, we first report the

detailed results of CIFAR100 and ImageNet100 and then report the top-5 accuracy of the ImageNet comparison.

# A.1 Detailed Results of CIFAR100

We first report the results of CIFAR100 where we select six dataset splits (i.e., Base0 Inc5, Base0 Inc10, Base0 Inc20, Base50 Inc50, Base50 Inc10, Base50 Inc25). The results are shown in Figure 10, and we list the number of parameters, the average accuracy, and the last accuracy in Table 5.

As we can infer from these figures, L2P consistently obtains the best performance among all settings. However, it must be noted that L2P relies on the ImageNet-21K pre-trained Vision Transformer with 85M parameters. At the same time, typical methods train ResNet32 with 0.46M parameters from scratch. Hence, comparing pre-trained model-based methods to typical methods is unfair. We also notice that dynamic networks, e.g., DER and MEMO obtain better performance at the cost of more parameters. Therefore, we report Table 5 to point out that parameter cost is sometimes ignored in the benchmark comparison, which shall lead to unfair results. These comparison details also motivate us to design fair comparison protocols for class-incremental learning.

# A.2 Detailed Results of ImageNet100

We report the results of ImageNet100 where we select six dataset splits (i.e., Base0 Inc5, Base0 Inc10, Base0 Inc20, Base50 Inc50, Base50 Inc10, Base50 Inc25). The results are shown in Figure 11, and we list the number of parameters, the average accuracy, and the last accuracy in Table 6. The conclusions are consistent with former small-scale datasets, and dynamic networks perform better at the cost of more memory budget.

It must be noted that there are two methods not included in the ImageNet comparison, i.e., GEM and L2P. GEM requires solving the QP problem and saving a large-scale matrix, which cannot be deployed with ImageNet. Besides, L2P utilizes an ImageNet-21K pre-trained backbone for class-incremental learning [69], which overlaps with the dataset to be learned. Hence, these two methods are not included in the comparison.

# A.3 ImageNet Top-5 Results

In this section, we report the top-5 accuracy of different methods in the ImageNet100 comparison. As shown in Figure 12, the ranking of different methods remains the same as in the top-1 accuracy comparison. We also report the top-5 accuracy in the ImageNet1000 comparison in Figure 13.

# APPENDIX B

# VISUALIZATION RESULTS

In this section, we report the full visualization results in the CIFAR100 comparison. Specifically, we first show the confusion matrix of 15 methods in Figure 14. As we can infer from these figures, Finetune and EWC forget most knowledge from former classes, while LwF shows less forgetting with knowledge distillation. When comparing LwF to EWC, we find that knowledge distillation is a more suitable solution to resist catastrophic forgetting than parameter regularization without saving exemplars. When equipping the model with exemplars, the diagonal elements become brighter, implying that forgetting is alleviated. The performance of Replay shows more steady improvement than finetune, indicating

![](images/d44779bcd88ea63241331dd59189f9f78d7a42e219890bb4b3b8ff1504ab02d1.jpg)  
(a) CIFAR100 Base0 Inc5

![](images/81c848e0fcbccc459dc4181c7c2d333eb9c4a735dbf1bbc51309bd09ac344058.jpg)  
(b) CIFAR100 Base0 Inc10

(c) CIFAR100 Base0 Inc20   
![](images/9e22f3a5cc6a5227031c9a2cdaafd52d1ee8035af225bdfca21d684b0ec6bd40.jpg)  
→ Finetune ←RMM →EWC →DER -L2P →MEMO →iCaRL →Coil - WA Replay * GEM ←AANets -DyTox FOSTER → LwF → PODNet +·BiC →CNN-Oracle

![](images/bc3010c208ee23a2889284ed07b33daab3ffbb80ee5ee04756e6ddb23503ce44.jpg)  
(d) CIFAR100 Base50 Inc50

![](images/46bd12bfc04822747c8ca746bba17913f7e79f99e4ec60d6541a2d95bb7fb4fb.jpg)  
(e) CIFAR100 Base50 Inc10

![](images/4ae2b7ad80c4686316f76d0d06dfab9dd2286662fb40920b908adb7b9c5d8318.jpg)  
(f) CIFAR100 Base50 Inc25   
Figure 10: Incremental accuracy of different methods on CIFAR100.

the critical role of exemplars in CIL. However, when comparing iCaRL to GEM, we can find that data regularization shows inferior performance than knowledge distillation in the efficiency of using exemplars. Moreover, BiC and WA improve the performance of iCaRL by rectifying the bias in the model, indicating that these methods can be orthogonally equipped to other CIL methods for rectification. Lastly, dynamic networks (i.e., DER, FOSTER, MEMO, and DyTox) still show the most competitive performance in these visualizations, indicating that the former backbones help the model retrieve old features and resist forgetting.

Additionally, we visualize the weight norm of the fullyconnected layers in Figure 15 to show the bias introduced by incremental learning. As we can infer from these figures, when sequentially finetuning the model, the weight norm of new classes will dominate the learning process due to data imbalance. As shown in Figure 15(a), the weight norm of finetune has a stair-step shape. Since the features are passed through the ReLU layer to avoid negative ones, the larger weight norm of new classes will result in an imbalance in the prediction results. These results are consistent with the confusion matrix in Figure 14, and we find that most CIL methods can relieve the imbalance in the fully connected layers.

# APPENDIX C

# SUPPLIED RESULTS IN MEMORY-ALIGNED COMPAR-ISON

In the main paper, we report the incremental performance curve with aligned memory to DER. In this section, we report the detailed setting of those figures, including the number of exemplars, the

number of parameters, the total memory size, and the detailed performance in Table 7. Specifically, since DER and MEMO require an extra model budget compared to other methods, we equip more exemplars to other methods to make sure the total memory size is aligned to the same scale.

As we can infer from the table, the gap between different methods becomes smaller when the total budget is aligned to the same scale. Specifically, the typical baseline method iCaRL shows the best average accuracy in the CIFAR100 Base0 Inc5 setting. In other words, saving exemplars can be more memory-efficient than saving backbones when fairly compared.

# APPENDIX D

# DETAILS ABOUT THE AUC-A/L MEASURE

In this section, we report the details in the memory-agnostic measure, i.e., AUC-A/L for class-incremental learning. We first highlight the importance of this measure and then give the implementation details of the curve, including the per-node performance and memory alignment details. We will start with CIFAR100 [24] and then discuss ImageNet100 [25].

# D.1 Necessity of AUC in CIL

We report the full performance-memory curve in Figure 16, including the average and last accuracy-memory curves. In each figure, the X-coordinate indicates the memory budget of the specific model, and the Y-coordinate represents the corresponding performance of the model. To highlight the importance of the AUC measure, we begin with a simple question:

Table 5: Average and last accuracy performance comparison on CIFAR100. ‘#P’ represents the number of parameters (million).   

<table><tr><td rowspan="2">Method</td><td colspan="3">Base0 Inc5</td><td colspan="3">Base0 Inc10</td><td colspan="3">Base0 Inc20</td><td colspan="3">Base50 Inc10</td></tr><tr><td>#P</td><td>A</td><td>AB</td><td>#P</td><td>A</td><td>AB</td><td>#P</td><td>A</td><td>AB</td><td>#P</td><td>A</td><td>AB</td></tr><tr><td>Finetune</td><td>0.46</td><td>17.59</td><td>4.83</td><td>0.46</td><td>26.25</td><td>9.09</td><td>0.46</td><td>37.90</td><td>17.07</td><td>0.46</td><td>22.79</td><td>9.09</td></tr><tr><td>EWC</td><td>0.46</td><td>18.42</td><td>5.58</td><td>0.46</td><td>29.73</td><td>12.44</td><td>0.46</td><td>39.19</td><td>19.87</td><td>0.46</td><td>25.77</td><td>11.47</td></tr><tr><td>LwF</td><td>0.46</td><td>30.93</td><td>12.60</td><td>0.46</td><td>43.56</td><td>23.25</td><td>0.46</td><td>48.96</td><td>30.00</td><td>0.46</td><td>41.12</td><td>25.06</td></tr><tr><td>GEM</td><td>0.46</td><td>31.73</td><td>19.48</td><td>0.46</td><td>40.18</td><td>23.03</td><td>0.46</td><td>50.33</td><td>34.09</td><td>0.46</td><td>33.28</td><td>21.33</td></tr><tr><td>Replay</td><td>0.46</td><td>58.20</td><td>38.69</td><td>0.46</td><td>59.31</td><td>41.01</td><td>0.46</td><td>60.03</td><td>43.08</td><td>0.46</td><td>52.37</td><td>41.26</td></tr><tr><td>RMM</td><td>0.46</td><td>65.72</td><td>51.10</td><td>0.46</td><td>68.54</td><td>56.64</td><td>0.46</td><td>70.64</td><td>61.81</td><td>0.46</td><td>67.53</td><td>59.75</td></tr><tr><td>iCaRL</td><td>0.46</td><td>63.51</td><td>45.12</td><td>0.46</td><td>64.42</td><td>49.52</td><td>0.46</td><td>67.00</td><td>54.23</td><td>0.46</td><td>61.29</td><td>52.04</td></tr><tr><td>PODNet</td><td>0.46</td><td>47.88</td><td>27.99</td><td>0.46</td><td>55.22</td><td>36.78</td><td>0.46</td><td>62.96</td><td>49.08</td><td>0.46</td><td>64.45</td><td>55.21</td></tr><tr><td>Coil</td><td>0.46</td><td>57.68</td><td>34.33</td><td>0.46</td><td>60.27</td><td>39.85</td><td>0.46</td><td>63.33</td><td>45.54</td><td>0.46</td><td>55.71</td><td>41.24</td></tr><tr><td>WA</td><td>0.46</td><td>64.65</td><td>48.46</td><td>0.46</td><td>67.09</td><td>52.30</td><td>0.46</td><td>68.51</td><td>57.97</td><td>0.46</td><td>64.32</td><td>55.85</td></tr><tr><td>BiC</td><td>0.46</td><td>62.38</td><td>43.08</td><td>0.46</td><td>65.08</td><td>50.79</td><td>0.46</td><td>67.03</td><td>56.22</td><td>0.46</td><td>61.01</td><td>49.19</td></tr><tr><td>FOSTER</td><td>0.46</td><td>63.38</td><td>49.42</td><td>0.46</td><td>66.49</td><td>53.21</td><td>0.46</td><td>68.60</td><td>58.67</td><td>0.46</td><td>65.73</td><td>57.82</td></tr><tr><td>DER</td><td>9.27</td><td>67.99</td><td>53.95</td><td>4.60</td><td>69.74</td><td>58.59</td><td>2.30</td><td>70.82</td><td>62.40</td><td>2.76</td><td>68.24</td><td>61.94</td></tr><tr><td>MEMO</td><td>7.14</td><td>68.10</td><td>54.23</td><td>3.62</td><td>70.20</td><td>58.49</td><td>1.87</td><td>70.43</td><td>61.39</td><td>2.22</td><td>69.39</td><td>62.83</td></tr><tr><td>DyTox</td><td>10.7</td><td>68.06</td><td>52.23</td><td>10.7</td><td>71.07</td><td>58.72</td><td>10.7</td><td>73.05</td><td>64.22</td><td>10.7</td><td>69.07</td><td>60.35</td></tr><tr><td>L2P</td><td>85.7</td><td>84.00</td><td>78.96</td><td>85.7</td><td>89.35</td><td>83.39</td><td>85.7</td><td>90.17</td><td>86.91</td><td>85.7</td><td>85.21</td><td>79.34</td></tr></table>

Table 6: Average and last top-1 accuracy performance comparison on ImageNet100. ‘#P’ represents the number of parameters (million).   

<table><tr><td rowspan="2">Method</td><td colspan="3">Base0 Inc5</td><td colspan="3">Base0 Inc10</td><td colspan="3">Base0 Inc20</td><td colspan="3">Base50 Inc10</td></tr><tr><td>#P</td><td>A</td><td>AB</td><td>#P</td><td>A</td><td>AB</td><td>#P</td><td>A</td><td>AB</td><td>#P</td><td>A</td><td>AB</td></tr><tr><td>Finetune</td><td>11.17</td><td>17.06</td><td>4.70</td><td>11.17</td><td>26.19</td><td>9.30</td><td>11.17</td><td>40.20</td><td>17.86</td><td>11.17</td><td>24.12</td><td>9.26</td></tr><tr><td>EWC</td><td>11.17</td><td>18.78</td><td>6.14</td><td>11.17</td><td>27.78</td><td>11.10</td><td>11.17</td><td>41.54</td><td>18.98</td><td>11.17</td><td>26.21</td><td>11.54</td></tr><tr><td>LwF</td><td>11.17</td><td>41.76</td><td>17.74</td><td>11.17</td><td>55.50</td><td>33.10</td><td>11.17</td><td>68.43</td><td>53.00</td><td>11.17</td><td>46.24</td><td>31.42</td></tr><tr><td>Replay</td><td>11.17</td><td>56.37</td><td>37.32</td><td>11.17</td><td>59.21</td><td>41.00</td><td>11.17</td><td>64.53</td><td>48.76</td><td>11.17</td><td>55.73</td><td>43.38</td></tr><tr><td>RMM</td><td>11.17</td><td>69.70</td><td>57.16</td><td>11.17</td><td>74.07</td><td>65.66</td><td>11.17</td><td>80.08</td><td>73.96</td><td>11.17</td><td>73.02</td><td>66.52</td></tr><tr><td>iCaRL</td><td>11.17</td><td>62.36</td><td>44.10</td><td>11.17</td><td>67.11</td><td>50.98</td><td>11.17</td><td>73.57</td><td>61.50</td><td>11.17</td><td>62.56</td><td>53.68</td></tr><tr><td>PODNet</td><td>11.17</td><td>53.70</td><td>33.34</td><td>11.17</td><td>64.03</td><td>45.40</td><td>11.17</td><td>71.99</td><td>58.04</td><td>11.17</td><td>73.83</td><td>62.94</td></tr><tr><td>Coil</td><td>11.17</td><td>56.21</td><td>34.00</td><td>11.17</td><td>61.91</td><td>41.50</td><td>11.17</td><td>69.49</td><td>53.54</td><td>11.17</td><td>59.80</td><td>43.40</td></tr><tr><td>WA</td><td>11.17</td><td>62.96</td><td>46.06</td><td>11.17</td><td>68.60</td><td>55.04</td><td>11.17</td><td>74.44</td><td>64.84</td><td>11.17</td><td>65.81</td><td>56.64</td></tr><tr><td>BiC</td><td>11.17</td><td>58.03</td><td>34.56</td><td>11.17</td><td>65.13</td><td>42.40</td><td>11.17</td><td>76.29</td><td>66.92</td><td>11.17</td><td>66.36</td><td>49.90</td></tr><tr><td>FOSTER</td><td>11.17</td><td>64.45</td><td>53.18</td><td>11.17</td><td>69.36</td><td>60.58</td><td>11.17</td><td>75.27</td><td>68.88</td><td>11.17</td><td>69.85</td><td>63.12</td></tr><tr><td>DER</td><td>223.4</td><td>73.79</td><td>63.66</td><td>111.7</td><td>77.08</td><td>66.84</td><td>55.85</td><td>78.56</td><td>72.10</td><td>67.02</td><td>77.57</td><td>71.10</td></tr><tr><td>MEMO</td><td>170.6</td><td>68.19</td><td>56.10</td><td>86.72</td><td>71.00</td><td>60.96</td><td>44.75</td><td>76.59</td><td>68.64</td><td>53.14</td><td>76.66</td><td>70.22</td></tr><tr><td>DyTox</td><td>11.00</td><td>69.57</td><td>53.82</td><td>11.00</td><td>73.40</td><td>61.78</td><td>11.00</td><td>76.81</td><td>68.78</td><td>11.00</td><td>74.65</td><td>65.76</td></tr></table>

Given the same memory budget, which algorithm should I choose for class-incremental learning? iCaRL or DER?

It is a simple question that aims to explore a better algorithm with the same memory budget. However, when we compare the performance of iCaRL and DER in Figure 16(a), we find an intersection among these methods. Specifically, we find iCaRL has better accuracy when the memory size is 7.4 MB, while DER works better when the memory size is 23.5 MB. This results in a contradictory conclusion, and we cannot find a model that suits all memory budgets.

To this end, calculating AUC does not rely on the specific budget, and we can tell from the AUC table that DER has a better AUC performance, which means it has better expandability. In other words, accuracy can only measure the performance given a specific X-coordinate. In contrast, AUC measures the area under the incremental performance curve holistically.

# D.2 Implementation Details

We give the implementation details in plotting the performancememory curve in this section. In the following discussions, we use  to represent the exemplar set. # denotes the number of exemplars, and $S ( \mathcal { E } )$ represents the memory size (in MB) that saving these exemplars consume. Following the benchmark implementation in the main paper, 2,000 exemplars are saved

for every method for CIFAR100 and ImageNet100. Hence, the exemplar size of each method is denoted as $\begin{array} { r } { \bar { { \# } } \mathcal { E } = 2 0 0 0 + E , } \end{array}$ , where E corresponds to the extra exemplars exchanged from the model size, as discussed in the main paper. We use $\mathcal { \bullet } \mathrm { { P } } ^ { \bullet }$ to represent the number of parameters and ‘MS’ to represent the memory budget (in MB) it costs to save this model in memory. The total memory size (i.e., numbers on the X coordinate) is the summation of exemplars and the models:

$$
\text {M e m o r y S i z e} = \text {M o d e l S i z e} + \text {E x a m p l a r S i z e}, \tag {18}
$$

which should be aligned for fair comparison as we advocated.

Specifically, we can divide the selected methods into two groups. The first group contains GEM [53], iCaRL [82], Replay [128] WA [112], PODNet [94], Coil [88], BiC [83] and FOSTER [16], whose use a single backbone for incremental learning in the inference stage. Hence, they use the same network backbone with the same model size and equal memory sizes, and we denote them as SingleNet. The second group contains DER [15] and MEMO [17], which require more memory budget to save the extra model during inference. Specifically, DER sacrifices the memory size to store the backbone from history, which consumes the largest model size. On the other hand, compared to DER, MEMO does not keep the duplicated generalized blocks from history and saves much memory size to change into exemplars.

![](images/da19548e532a2171adf9ed30ff292c87617e220558301d4cab3ae1b5bc43cd05.jpg)  
(a) ImageNet100 Base0 Inc5

![](images/8723e9e8c081a0d60611603a559eef7799b137cf5bced9bf8db826f5a03aeb2f.jpg)  
(b) ImageNet100 Base0 Inc10

![](images/5556bd44f1e00f4f50ca68fcb3f7103a27e6cfac1d214a1068856bcc7fcfbd58.jpg)  
(c) ImageNet100 Base0 Inc20

![](images/5da8c230759ae808fae84524dca955a9e0832d3129fe0518c57b2241defe1be9.jpg)

![](images/9c2335e2ca125d743fada291ca88cb00e6883dd14f3ea4465c5b6265675d022a.jpg)  
(d) ImageNet100 Base50 Inc50

![](images/3288a2b02c1af976f22486bef99e27f26408446cc894f8232cc8a4f91026fdb6.jpg)  
(e) ImageNet100 Base50 Inc10

![](images/a598f73f13fbdc8e0f6e441894f6bc858ed55021a9bae6ef40bd8a349261e649.jpg)  
(f) ImageNet100 Base50 Inc25   
Figure 11: Incremental top-1 accuracy of different methods on ImageNet100.

Table 7: Average and last accuracy performance comparison with aligned memory cost. ‘#P’ represents the number of parameters (million). ‘# ’ denotes the number of exemplars, and ‘MS’ denotes the memory size (MB).   

<table><tr><td rowspan="2">Method</td><td colspan="4">CIFAR100 Base0 Inc5</td><td colspan="5">CIFAR100 Base0 Inc10</td><td colspan="5">ImageNet100 Base0 Inc10</td><td></td></tr><tr><td>#P</td><td>#E</td><td>MS</td><td>A</td><td>AB</td><td>#P</td><td>#E</td><td>MS</td><td>A</td><td>AB</td><td>#P</td><td>#E</td><td>MS</td><td>A</td><td>AB</td></tr><tr><td>GEM</td><td>0.46</td><td>13466</td><td>41.22</td><td>20.30</td><td>7.99</td><td>0.46</td><td>7431</td><td>23.5</td><td>27.03</td><td>10.72</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Replay</td><td>0.46</td><td>13466</td><td>41.22</td><td>74.25</td><td>61.09</td><td>0.46</td><td>7431</td><td>23.5</td><td>69.97</td><td>55.61</td><td>11.17</td><td>4671</td><td>713.2</td><td>67.46</td><td>53.72</td></tr><tr><td>iCaRL</td><td>0.46</td><td>13466</td><td>41.22</td><td>75.17</td><td>61.88</td><td>0.46</td><td>7431</td><td>23.5</td><td>70.94</td><td>58.52</td><td>11.17</td><td>4671</td><td>713.2</td><td>67.16</td><td>51.58</td></tr><tr><td>PODNet</td><td>0.46</td><td>13466</td><td>41.22</td><td>59.03</td><td>42.98</td><td>0.46</td><td>7431</td><td>23.5</td><td>60.80</td><td>45.38</td><td>11.17</td><td>4671</td><td>713.2</td><td>68.43</td><td>53.44</td></tr><tr><td>Coil</td><td>0.46</td><td>13466</td><td>41.22</td><td>74.39</td><td>60.78</td><td>0.46</td><td>7431</td><td>23.5</td><td>70.69</td><td>54.40</td><td>11.17</td><td>4671</td><td>713.2</td><td>69.97</td><td>54.24</td></tr><tr><td>WA</td><td>0.46</td><td>13466</td><td>41.22</td><td>74.07</td><td>63.18</td><td>0.46</td><td>7431</td><td>23.5</td><td>69.55</td><td>59.26</td><td>11.17</td><td>4671</td><td>713.2</td><td>72.62</td><td>62.12</td></tr><tr><td>BiC</td><td>0.46</td><td>13466</td><td>41.22</td><td>71.27</td><td>60.98</td><td>0.46</td><td>7431</td><td>23.5</td><td>70.69</td><td>59.60</td><td>11.17</td><td>4671</td><td>713.2</td><td>72.83</td><td>61.98</td></tr><tr><td>FOSTER</td><td>0.46</td><td>13466</td><td>41.22</td><td>75.06</td><td>62.82</td><td>0.46</td><td>7431</td><td>23.5</td><td>72.28</td><td>59.39</td><td>11.17</td><td>4671</td><td>713.2</td><td>71.55</td><td>59.86</td></tr><tr><td>DER</td><td>9.27</td><td>2000</td><td>41.22</td><td>70.41</td><td>57.85</td><td>4.60</td><td>2000</td><td>23.5</td><td>71.47</td><td>60.26</td><td>111.7</td><td>2000</td><td>713.2</td><td>75.70</td><td>67.14</td></tr><tr><td>MEMO</td><td>7.14</td><td>4771</td><td>41.22</td><td>73.57</td><td>62.97</td><td>3.62</td><td>3312</td><td>23.5</td><td>72.37</td><td>61.98</td><td>86.72</td><td>2652</td><td>713.2</td><td>72.55</td><td>64.08</td></tr></table>

Discussion about selected methods: In this part, we choose ten methods for the comparison, i.e., Finetune, EWC, LwF, RMM, DyTox, and L2P are not included in the evaluation. Firstly, nonexemplar-based methods (Finetune, EWC, LwF) are unsuitable for the evaluation since the extendability relies on adding extra exemplars. Secondly, RMM advocates another evaluation protocol in terms of the memory, which is incompatible with ours. Lastly, DyTox and L2P rely on the vision transformer as the backbone, which has a much larger memory scale than benchmark backbones. Directly comparing ResNet to ViT may be unfair since these backbones have different characteristics in model optimization.

How to choose the budget list? As we can infer from Figure 16, there are several selected memory sizes in the figures, which formulate the X-coordinate. Firstly, the start point corresponds to

the memory size of the first group, i.e., a single backbone with 2, 000 exemplars. It is a relatively small budget, which can be seen as the budget for edge devices. Correspondingly, since DER has the largest model size among all compared methods, we set the endpoint to the memory size of DER. After selecting the start and end points, we choose several intermediate budgets to formulate the budget list. The intermediate budgets are set according to the parameter size of DER and MEMO, as shown below.

How to set the exemplar and model size? For SingleNet, we can easily extend them by adding the number of exemplars. Since the model size is fixed for them, adding exemplars enables these methods to extend to a larger scale. However, we cannot use the same backbone as SingleNet for DER and MEMO when the memory size is small. Hence, we divide the model parameters

![](images/5879e81d2a393cd7af42bc1acc1af1ccdb4e3b45151509516b700a4fcc050ede.jpg)  
(a) ImageNet100 B0 Inc5

![](images/a610ba5888a80b0aec87e20dbf3440e074d9bae1d7e02fd865c2765da238aa95.jpg)  
(b) ImageNet100 B0 Inc10

![](images/1dddc5f7a796a6211c85b57c68e19a7dd724436e85d9f936f31b575dde73b0a9.jpg)  
(c) ImageNet100 B0 Inc20

![](images/301ee79738bc9e162f816976b2efb84ecbfb837c7ce69339c4d51b96392a7fba.jpg)

![](images/f17d036d6612a110afaef4f8c5869bc69d4420687b2b2c0d1283261c461af421.jpg)  
(d) ImageNet100 B50 Inc50

![](images/c64a6f98b88879bc9bb4d36c97de15dfc6ddcdb38ecdcc6e9c99622102ae7586.jpg)  
(e) ImageNet100 B50 Inc10

![](images/e81e72497b75ac7a8d11a9e351ec5fc74de5d131cccf84186af992fbce67006b.jpg)  
(f) ImageNet100 B50 Inc25   
Figure 12: Incremental top-5 accuracy of different methods on ImageNet100.

into ten equal parts (since there are ten incremental tasks in the CIFAR100 Base0 Inc10 setting) and look for a backbone with similar parameter numbers. For example, we separately use ConvNet, ResNet14, ResNet20, and ResNet26 as the backbone for these methods to match different memory scales. Specifically, we use the same backbone for DER and MEMO and another same backbone for SingleNet to keep the total memory budget at the same scale. We annotate the backbone type in the figures of configurations, e.g., ‘ResNet32/ResNet14’ means we use ResNet32 for SingleNet and ResNet14 for DER and MEMO.

In the following discussions, we give the memory figures and tables to illustrate the implementation of different methods and report their incremental performance. We start with CIFAR100 and then discuss ImageNet100.

![](images/3e45da05054c533fd1e6b6807421e40a0b47bfaf0b7c13bc318f267fda950c33.jpg)  
(a) Memory Usage

![](images/9fffe3d3e928056cf2d306dee4525e0c419be26d97f0202120a800186b2de032.jpg)  
(b) Performance Curve   
Figure 17: Implementation details and performance curve of CIFAR100 when memory size=7.6 MB.

Table 8: Numerical details when memory size=7.6 MB.   

<table><tr><td>7.6MB</td><td>#E</td><td>S(E)</td><td>Model Type</td><td>#P</td><td>Model Size</td></tr><tr><td>SingleNet</td><td>2000</td><td>5.85MB</td><td>ResNet32</td><td>0.46M</td><td>1.76MB</td></tr><tr><td>DER</td><td>2096</td><td>6.14MB</td><td>ConvNet2</td><td>0.38M</td><td>1.48MB</td></tr><tr><td>MEMO</td><td>2118</td><td>6.20MB</td><td>ConvNet2</td><td>0.37M</td><td>1.42MB</td></tr></table>

# D.2.1 CIFAR100 Implementations

There are five X coordinates in the curve of CIFAR100, e.g., 7.6, 12.4, 16.0, 19.8, and 23.5 MB. Following, we show the detailed implementation of different methods at these scales.

CIFAR100 with 7.6 MB Memory Size: The implementations are shown in Figure 17, and the memory size (7.6 MB) is relatively small. Since we need to align the total budget of these methods, we are only able to use small backbones for DER and MEMO. These small backbones, i.e., ConvNet with two convolutional layers, have

![](images/413bc129605bfc2f47a95926dd62e774e8cccab6630e8dad28a38e1bf9e95c2d.jpg)

![](images/7065eda413430a13c982241b78002bb0b3eaa0be6ab93da43e0c5c8e38654be7.jpg)

![](images/c0f9399fa598a702d13ed1aded304f9d4563720b0ec716909c1fc43ed00545b3.jpg)  
(a) ImageNet1000 B0 Inc100

![](images/d19d210c35409d2a192b2fda72d35d93506dc727d8a242c96e82dd54441a3e72.jpg)  
(b) ImageNet1000 B500 Inc100   
Figure 13: Incremental top-5 accuracy of different methods on ImageNet1000.

much fewer parameters than ResNet32 and saving 10 ConvNets matches the memory size of a single ResNet32 (1.48MB versus 1.76MB). We can infer that DER and MEMO are restricted by the learning ability of these small backbones, which perform poorly in the base session. These results are consistent with the conclusions in Figure 16 that dynamic networks are inferior to SingleNet given a small memory budget.

We report the implementation details, including the number of exemplars, size of exemplars, type of backbones, number of parameters, and size of models in Table 8. The total memory budget, i.e., 7.6MB, is the summation of the exemplar size and model size.

![](images/4f3471d28892ec2f4bc9eb03bd0f40b565b49e1d5dd2ec6bab111f1a6891c89e.jpg)  
(a) Memory Usage

![](images/0bc552ed1935774873737ed8ca562bebe5187413cc06a0db28675154bbf9974d.jpg)  
(b) Performance Curve   
Figure 18: Implementation details and performance curve of CIFAR100 when memory size=12.4 MB.

Table 9: Numerical details when memory size=12.4 MB.   

<table><tr><td>12.4MB</td><td>#E</td><td>S(E)</td><td>Model Type</td><td>#P</td><td>Model Size</td></tr><tr><td>SingleNet</td><td>3634</td><td>10.64MB</td><td>ResNet32</td><td>0.46M</td><td>1.76MB</td></tr><tr><td>DER</td><td>2000</td><td>5.85MB</td><td>ResNet14</td><td>1.70M</td><td>6.55MB</td></tr><tr><td>MEMO</td><td>2495</td><td>7.32MB</td><td>ResNet14</td><td>1.33M</td><td>5.10MB</td></tr></table>

CIFAR100 with 12.4 MB Memory Size: The implementations are shown in Figure 18. By raising the total memory cost to 12.4

MB, SingleNet can utilize the extra memory size to exchange 1634 exemplars. At the same time, dynamic networks can switch to more powerful backbones, i.e., ResNet14, to get better representation ability. We can infer that DER and MEMO show competitive results with stronger backbones and outperform other methods in this setting. These results are consistent with the conclusions in Figure 16 that the intersection between these two groups of methods exists near the start point.

![](images/f944457f082572d352e2b674bfdd94b2a2fd4abf23130e5f0fd696b5b9747d07.jpg)  
(a) Memory Usage

![](images/ce6c48c5d7e704af996e4649480a9e5266802cb2d86ce5dd37616445f7e4c045.jpg)  
(b) Performance Curve   
Figure 19: Implementation details and performance curve of CIFAR100 when memory size=16.0 MB.

Table 10: Numerical details when memory size=16.0 MB.   

<table><tr><td>16.0MB</td><td>#E</td><td>S(E)</td><td>Model Type</td><td>#P</td><td>Model Size</td></tr><tr><td>SingleNet</td><td>4900</td><td>14.3MB</td><td>ResNet32</td><td>0.46M</td><td>1.76MB</td></tr><tr><td>DER</td><td>2000</td><td>5.85MB</td><td>ResNet20</td><td>2.69M</td><td>10.2MB</td></tr><tr><td>MEMO</td><td>2768</td><td>8.10MB</td><td>ResNet20</td><td>2.1M</td><td>8.01MB</td></tr></table>

CIFAR100 with 16.0 MB Memory Size: The implementations are shown in Figure 19. By raising the total memory cost to 16.0 MB, SingleNet can utilize the extra memory size to exchange 2900 exemplars, and dynamic networks can switch to larger backbones to get better representation ability. We use ResNet20 for DER and

![](images/57773d786d8531033cd7162d258b2e5a41a4873bd299e7323bd48b8c0ce766ff.jpg)  
(a) Finetune

![](images/3cb06081781473abe0b853e5349cf8b6d990839dc681105074ceec7557214062.jpg)  
(b) EWC

![](images/e196112dc08710f7e71909d03a9f4d886d324bc699fe9c57d9f606369923a0b2.jpg)  
(c) LwF

![](images/2d526d5c0c7f544f6cd400e92cb468fcf5e01fb9f368290ca0e272f862cdf354.jpg)  
(d) Replay

![](images/ce877fb274c9c56612f5cca8b8d093c081e309408ca9b20e4716b5862f057ad6.jpg)  
(e) GEM

![](images/05678c80588ca145443b614ce3ee550a1eb9a78ad5b1add0219128de55e9fc5f.jpg)  
(f) iCaRL

![](images/efeea7ad526de526f113f816bfe341933d86e037d820fb11c69d58c6cb29b89e.jpg)  
(g) BiC

![](images/3f10cf527872a66686fa1e0849a96af676cf8293487b29c05750bb6a8da37e58.jpg)  
(h) WA

![](images/c3636d5fd2b19096c84b2f49155361cca2b5498f235d19ac65eb47a2911f966e.jpg)  
(i) PODNet

![](images/b355bb62d1d37e913e288fff55b4d931b70473350e64adf1e3a6f0744da0ef4c.jpg)  
(j) DER

![](images/a5400b4be0d3aea605f16c474ceb0c5f852a1b31ee62acfbaa0f84c07115d65f.jpg)  
(k) RMM+FOSTER

![](images/22e06a82adb66b2b79138f3f12bac65ea3ac0fbd72d9da94aee0f0aaa16cdbdb.jpg)  
(l) Coil

![](images/3e0c3c551c068db7844f01118db26ef4a7f525291cdd76cd217b3bffefe9ec67.jpg)  
(m) FOSTER

![](images/441c4e790970dd26bc1343023e732eed7d04ea4e913342a3ab1165c13aaa69c3.jpg)  
(n) MEMO

![](images/e02e49e5d9bc1f6937adedc367cb46001e8a1c6eaa3a62cdbc7d8e63b7b0fbd7.jpg)  
(o) Dytox   
Figure 14: Confusion matrix of different methods on CIFAR100 Base0 Inc20 setting after the last incremental stage.

MEMO in this setting. The results are consistent with the former setting, where we can see that DER and MEMO show competitive results with stronger backbones and outperform other methods.

![](images/9269bddc73c3bec10841a99dc91631d20957d8ecbcc45557a3a1f6c2cbf3fa4e.jpg)  
(a) Memory Usage

![](images/6dc881516455086068c11cc11b7bd7ec473974a8990f192d50c4689a460e0f9b.jpg)  
(b) Performance Curve   
Figure 20: Implementation details and performance curve of CIFAR100 when memory size=19.8 MB.

Table 11: Numerical details when memory size=19.8 MB.   

<table><tr><td>19.8MB</td><td>#E</td><td>S(E)</td><td>Model Type</td><td>#P</td><td>Model Size</td></tr><tr><td>SingleNet</td><td>6165</td><td>18.06MB</td><td>ResNet32</td><td>0.46M</td><td>1.76MB</td></tr><tr><td>DER</td><td>2000</td><td>5.85MB</td><td>ResNet26</td><td>3.60M</td><td>13.9MB</td></tr><tr><td>MEMO</td><td>3040</td><td>8.91MB</td><td>ResNet26</td><td>2.86M</td><td>10.92MB</td></tr></table>

CIFAR100 with 19.8 MB Memory Size: The implementations are shown in Figure 20. By raising the total memory cost to 19.8

MB, SingleNet can utilize the extra memory size to exchange 4165 exemplars, and dynamic networks can switch to larger backbones to get better representation ability. We use ResNet26 for DER and MEMO in this setting. The results are consistent with the former setting, where we can infer that dynamic networks show competitive results with stronger backbones and outperform other methods.

![](images/e8cef04d18e061e01fc905a1467f280cff77f1520dc89dee8e995a1c08f95af1.jpg)  
(a) Memory Usage

![](images/04ce0ae0c578d6ecefdc083f9494197b640894fa2ed791fa43834dc7c54539fc.jpg)  
(b) Performance Curve   
Figure 21: Implementation details and performance curve of CIFAR100 when memory size=23.5 MB.

Table 12: Numerical details when memory size=23.5 MB.   

<table><tr><td>23.5MB</td><td>#E</td><td>S(E)</td><td>Model Type</td><td>#P</td><td>Model Size</td></tr><tr><td>SingleNet</td><td>7431</td><td>21.76MB</td><td>ResNet32</td><td>0.46M</td><td>1.75MB</td></tr><tr><td>DER</td><td>2000</td><td>5.86MB</td><td>ResNet32</td><td>4.63M</td><td>17.68MB</td></tr><tr><td>MEMO</td><td>3312</td><td>9.7MB</td><td>ResNet32</td><td>3.62M</td><td>13.83MB</td></tr></table>

![](images/7991ccc1d88d3c27d13cb88b67e9fd52baca8e1f60513b418ef3c3f7901f4f38.jpg)  
(a) Finetune

![](images/8d9f3ad238e5112fd5bca0f06f19fdfe1f13217dd32b2a44d51f32d4164a49b3.jpg)  
(b) EWC

![](images/6923d41389823b8800937e465c9c61e1a415840d8a579c2fba66c074628d472f.jpg)  
(c) LwF

![](images/9cc312fcbb98d4e33fa07634624a606dcfb30c009c3f797fce05b852e5825ef6.jpg)  
(d) Replay

![](images/6ef66d51f9f466bcee98554e34abe265df99885c28d727a248255f6a2014bc90.jpg)  
(e) GEM

![](images/b11322add2b9ef67d34bea221c2ee0cf75078d9ce058082c2a1fdb41dd8f3a95.jpg)  
(f) iCaRL

![](images/2424708b9954d3f19ad5f7e502577ac8192f340fa8b69c0a4e38872cfe25988a.jpg)  
(g) BiC

![](images/b633b2bc4bbd63fa9f8b74edee2b3124ed82d7eb87ab6c98c8a4fa26eee83040.jpg)

![](images/56f431dd37f279bf457fb791294f623dbf0e38ce46a0ce6f69ac0e749e20a417.jpg)  
(i) PODNet

![](images/5b0d28f73af499c3ec49d69abd91e3401fb5008f4654f945ef018fe98dff9543.jpg)  
(j) DER

![](images/713e7069efca30fcb5aebf34f20eaa67790f11d50c2511fbe13190c93a824061.jpg)  
(k) RMM+FOSTER

![](images/f63c4bac5d34b17a0744b527f4e16e27b6f8b2e1ea4a254429966be67cc60b59.jpg)  
(l) Coil

![](images/139bc25305488cdf478d9777efd981e25e57ad8210e10016997de1cb1bfc00cd.jpg)  
(m) FOSTER

![](images/03175e03a02f7522c5dc1bbffa28049801175a0a4b1c5a1c479334d96bb0030e.jpg)  
(n) MEMO

![](images/cf7264e7e07bc09ac5a6a786fc60afa325020562ca0bc905e66c06d16741285e.jpg)  
(o) Dytox   
Figure 15: Weight norm of different methods on CIFAR100 Base0 Inc20 setting. We visualize the norm after the last incremental stage.

CIFAR100 with 23.5 MB Memory Size: The implementations are shown in Figure 21. By raising the total memory cost to 23.5 MB, SingleNet can utilize the extra memory size to exchange 5431 exemplars. In addition, dynamic networks can switch to larger backbones, i.e., ResNet32, to get better representation ability.

![](images/63fda28aa9b56e7e1dba093f7f1cdf6f74f024e33146f69c7d631bebaaf454af.jpg)  
(a) Memory Usage

![](images/f750048a67921c9788906761adfdc5134e80e717ae1fc4e9f1f80d7332da4d19.jpg)  
(b) Performance Curve   
Figure 22: Implementation details and performance curve of ImageNet100 when memory size=329 MB.

# D.2.2 ImageNet100 Implementations

Similar to CIFAR100, we can conduct an exchange between the model and exemplars with the ImageNet100 dataset. For example, saving a ResNet18 model costs 11, 176, 512 parameters (float), while saving an ImageNet image costs 3 ↖ 224 ↖ 224 integer numbers (int). The budget for saving a backbone is equal to saving 11, 176, 512 floats ↖4 bytes/float $\div ( 3 \times 2 2 4 \times 2 2 4 )$ bytes/image 297 images for ImageNet. We conduct the experiment with the ImageNet100 Base50 Inc5 setting, as discussed in the main paper.

There are six X coordinates in the curve of ImageNet100, e.g., 329, 493, 755, 872, 1180 and 1273 MB. Following, we show the detailed implementation of different methods at these scales.

Table 13: Numerical details when memory size=329 MB.   

<table><tr><td>329MB</td><td>#E</td><td>S(E)</td><td>Model Type</td><td>#P</td><td>Model Size</td></tr><tr><td>SingleNet</td><td>2000</td><td>287MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>DER</td><td>2032</td><td>291MB</td><td>ConvNet4</td><td>9.96M</td><td>38.0MB</td></tr><tr><td>MEMO</td><td>2115</td><td>303MB</td><td>ConvNet4</td><td>6.81M</td><td>26.0MB</td></tr></table>

ImageNet100 with 329 MB Memory Size: The implementations are shown in Figure 22. 329 MB is a relatively small memory size. Since we need to align the total budget of these methods, we are only able to use small backbones for DER and MEMO. These small backbones, i.e., ConvNet with four convolutional layers, have much fewer parameters than ResNet18, and saving 10 ConvNets matches the memory size of a single ResNet18. We can infer from the figure that DER and MEMO are restricted by the learning

![](images/5bf041e1f63fe42dc5853922e9808e72261fb0b1a37fb2f650b53d84858befbc.jpg)  
(a) Average accuracy curve of CIFAR100 Base0 Inc10

![](images/3fc9b9755e3c0fb260fd0c20ce7bbf22bd82373e42a794eae5a5b5e7fa6dc35f.jpg)  
(b) Average accuracy curve of ImageNet100 Base50 Inc5

![](images/3bf9f3920c61eafee231bce7f96d2862c7f27a0bb290fdbbb90f8ae15513b1bc.jpg)  
(c) Last accuracy curve of CIFAR100 Base0 Inc10

![](images/4facd3efa61b11d5b841b20ebe4b9ddb8cf0549227bd25716392fc6a1a19849f.jpg)  
(d) Last accuracy curve of ImageNet100 Base50 Inc5   
Figure 16: Performance-memory curve of different methods with different datasets.

ability of the inferior backbones, which perform poorly in the base task.

![](images/2a6695d11865615b443882856dd121a49f7aac4d7ceaf0f8817eff09b1640586.jpg)  
(a) Memory Usage

![](images/5098a7dcaed2eb0d6213ca6daabe6e39c814fea9580fc472cf4c67d4b4cc5edc.jpg)  
(b) Performance Curve   
Figure 23: Implementation details and performance curve ImageNet100 when memory size=493 MB.

Table 14: Numerical details when memory size=493 MB.   

<table><tr><td>493MB</td><td>#E</td><td>S(E)</td><td>Model Type</td><td>#P</td><td>Model Size</td></tr><tr><td>SingleNet</td><td>3136</td><td>450MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>DER</td><td>2000</td><td>287MB</td><td>ResNet10</td><td>53.96M</td><td>205MB</td></tr><tr><td>MEMO</td><td>2327</td><td>334MB</td><td>ResNet10</td><td>41.63M</td><td>158MB</td></tr></table>

ImageNet100 with 493 MB Memory Size: The implementations are shown in Figure 23. By raising the total memory cost to 493 MB, SingleNet can utilize the extra memory size to exchange 1136 exemplars. In addition, dynamic networks can switch to larger backbones, i.e., ResNet10, to get better representation ability. We can infer from the figure that dynamic networks show competitive results with stronger backbones and outperform other methods in this setting.

![](images/fda1bee335ba70f61c7ff8b06affeda0668ef0b668265d668f5479c67e027386.jpg)  
(a) Memory Usage

![](images/5bdb82402e9e4c393cbf0554ca3c2c2fe6b7257266af33e9b0ff9a1913600e4e.jpg)  
(b) Performance Curve   
Figure 24: Implementation details and performance curve ImageNet100 when memory size=755 MB.

Table 15: Numerical details when memory size=755 MB.   

<table><tr><td>755MB</td><td>#E</td><td>S(E)</td><td>Model Type</td><td>#P</td><td>Model Size</td></tr><tr><td>SingleNet</td><td>4970</td><td>713MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>DER</td><td>2000</td><td>287MB</td><td>ResNet18</td><td>122.9M</td><td>468MB</td></tr><tr><td>MEMO</td><td>2739</td><td>393MB</td><td>ResNet18</td><td>95.11M</td><td>362MB</td></tr></table>

ImageNet100 with 755 MB Memory Size: The implementations are shown in Figure 24. By raising the total memory cost to 755 MB, SingleNet can utilize the extra memory size to exchange 2970 exemplars. At the same time, dynamic networks can switch to larger backbones, i.e., ResNet18, to get better representation ability.

![](images/d148dc5515f8327e03e48f322d393074ec94151b17c9e4c9d4197f5557ced729.jpg)  
(a) Memory Usage

![](images/a87162f85ede3a783f93f709e461b7b57dc9d3e6c9880d967138fcabfdffa41c.jpg)  
(b) Performance Curve   
Figure 25: Implementation details and performance curve ImageNet100 when memory size=872 MB.

Table 16: Numerical details when memory size=872 MB.   

<table><tr><td>872MB</td><td>#E</td><td>S(E)</td><td>Model Type</td><td>#P</td><td>Model Size</td></tr><tr><td>SingleNet</td><td>5779</td><td>829MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>DER</td><td>2000</td><td>287MB</td><td>ResNet26</td><td>153.4M</td><td>585.2MB</td></tr><tr><td>MEMO</td><td>2915</td><td>417MB</td><td>ResNet26</td><td>119.0M</td><td>453MB</td></tr></table>

ImageNet100 with 872 MB Memory Size: The implementations are shown in Figure 25. By raising the total memory cost to 872 MB, SingleNet can utilize the extra memory size to exchange 3779 exemplars. In addition, dynamic networks can switch to larger backbones, i.e., ResNet26 for better representation ability.

![](images/399c5066fbcd7f1bcdd40e973289b7ea8dfd3c5477ec4cf1838cabee5e6a6f21.jpg)  
(a) Memory Usage

![](images/ebb666f04fc3bba8982812ce24d8f0923fa30ca171708c8e9a7677be526f14c8.jpg)  
(b) Performance Curve   
Figure 26: Implementation details and performance curve ImageNet100 when memory size=1180 MB.

Table 17: Numerical details when memory size=1180 MB.   

<table><tr><td>1180MB</td><td>#E</td><td>S(E)</td><td>Model Type</td><td>#P</td><td>Model Size</td></tr><tr><td>SingleNet</td><td>7924</td><td>1137MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>DER</td><td>2000</td><td>287MB</td><td>ResNet34</td><td>234.1M</td><td>893MB</td></tr><tr><td>MEMO</td><td>4170</td><td>598MB</td><td>ResNet34</td><td>152.4M</td><td>581MB</td></tr></table>

ImageNet100 with 1180 MB Memory Size: The implementations are shown in Figure 26. By raising the total memory cost to 1180 MB, non-dynamic networks can utilize the extra memory size to exchange 5924 exemplars. At the same time, dynamic networks can switch to larger backbones, i.e., ResNet34, to get better representation ability.

![](images/ab952abacbcc29ae395bfa5ced83901aa02e40ec69d87613a35d57b5a1e10f88.jpg)  
(a) Memory Usage

![](images/a8ec115503a388242b2a07e1c2b2206becd0cee77293cb550ad4e5fcbf8589ac.jpg)  
(b) Performance Curve   
Figure 27: Implementation details and performance curve ImageNet100 when memory size = 1273 MB.

Table 18: Numerical details when memory size=1273 MB.   

<table><tr><td>1273MB</td><td>#E</td><td>S(E)</td><td>Model Type</td><td>#P</td><td>Model Size</td></tr><tr><td>SingleNet</td><td>8574</td><td>1230MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>DER</td><td>2000</td><td>287MB</td><td>ResNet50</td><td>258.6M</td><td>986MB</td></tr><tr><td>MEMO</td><td>4270</td><td>612MB</td><td>ResNet50</td><td>173.2M</td><td>660MB</td></tr></table>

ImageNet100 with 1273 MB Memory Size: The implementations are shown in Figure 27. By raising the total memory cost to 1273 MB, SingleNet can utilize the extra memory size to exchange 6574 exemplars, and dynamic networks can switch to larger backbones to get better representation ability. We use ResNet50 for DER and MEMO in this setting.

Discussion about Backbones: It should be noted that ResNet18 is the benchmark backbone for ImageNet, and DER consumes about

755 MB memory budget under the benchmark setting. Hence, the last three points in the X-coordinate, i.e., 872, 1180, and 1273 MB, are larger than the benchmark setting. There are two main reasons for the budget list design. First, handling large-scale image inputs requires more convolutional layers, and it is hard to find typical models with small memory budgets. Second, we would like to investigate the performance when the model is large enough to see whether the improvement of stronger backbones will converge. The empirical results successfully verify our assumptions.

# APPENDIX E

# DETAILED INCREMENTAL PERFORMANCE

In this section, we report the detailed incremental performance of the main paper to facilitate a comparison of future works. Specifically, we report the performance on CIFAR100 and ImageNet100 in Table 19, 20, 21, 22, 23, 24, 25, 26.

# APPENDIX F

# FORGETTING AND INTRANSIGENCE MEASURE

In the main paper, we mainly utilize accuracy as the performance measure. Moreover, [33] proposes two metrics for evaluating continual learners, i.e., forgetting (F ) and intransigence (I). Specifically, we use $a _ { k , j }$ to represent model’s performance on task $j ^ { \flat } \boldsymbol { \mathrm { s } }$ testing set after learning task k. Hence, the forgetting of a single task is defined as:

$$
f _ {j, k} = \max  _ {l \in \{1, \dots , k - 1 \}} a _ {l, j} - a _ {k, j}, \quad \forall j <   k. \tag {19}
$$

$f _ { j , k }$ denotes the gap between the best performance $( a _ { l , j } )$ and the final performance $( a _ { k , j } )$ on the j-th task. Moreover, we can measure the gap between all tasks via the average forgetting of all tasks at the last stage:

$$
\mathcal {F} = \frac {1}{B - 1} \sum_ {j = 1} ^ {B - 1} f _ {j, B}, \tag {20}
$$

where B is the number of all tasks in the learning process. Note that the last task will not suffer forgetting, and there are only $B - 1$ terms in Eq. 20. Since the model often forgets former tasks during the learning process, the forgetting is usually larger than 0.

Apart from forgetting, we also have the intransigence measure to reflect the inability of a model to learn new tasks. The intransigence of task k is defined as:

$$
I _ {k} = a _ {k} ^ {*} - a _ {k, k}, \tag {21}
$$

where $a _ { k } ^ { * }$ represents the performance on the k-th task of a joint training model. ‘Joint training’ denotes a randomly initialized model optimized with all seen tasks $( { \mathcal { D } } ^ { 1 } \cup \cdot \cdot \cdot { \mathcal { D } } ^ { k } )$ . Hence, $I _ { k }$ measures the gap between the best performance it can achieve $( a _ { k } ^ { * } )$ and the incrementally learned performance $( a _ { k , k } )$ . In [33], the intransigence is originally defined on a single task, and we follow the definition of forgetting and average it on all tasks:

$$
\mathcal {I} = \frac {1}{B - 1} \sum_ {j = 2} ^ {B} I _ {j}. \tag {22}
$$

Note that there is no gap between joint and incremental training for the first task, and Eq. 22 averages B ≃ 1 following tasks.

As defined in Eq. 20 and 22, we report these new performance measures during the learning process. Specifically, we calculate

these performance measures for settings in Figure 6 in the main paper, and report the results in Table 27, 28. We can summarize two conclusions from the table:

• Generally, we find methods with higher last performance A¯ show better performance on the forgetting measure, i.e., lower F. The main reason is that the last performance accounts for the second term in the forgetting calculation, indicating the inherent relationship between these metrics.   
• Additionally, we find methods with less regularization tend to perform better on the intransigence measure, i.e., finetune shows the best performance. Since intransigence represents the gap between the algorithm’s performance and joint training’s performance on new tasks, regularization terms will harm the model’s plasticity and result in poor intransigence measure.

# APPENDIX G

# EXPERIMENT ON REPLAY STRATEGIES

There are several kinds of data replay to help the model recover former knowledge, i.e., image [82], [128], feature [38], [50] and generative replay [41], [42]. Facing a new task $\mathcal { D } ^ { \delta } .$ , all of them utilize the concatenation of exemplars and the newest training set $( i . e . , \mathcal { E } \cup \mathcal { D } ^ { b } )$ to update the model. However, the difference lies in the configuration of exemplars. Specifically, image replay directly saves raw images to construct $\boldsymbol { \mathcal { E } } , i . e . , \boldsymbol { \mathcal { E } } = \left\{ ( \mathbf { x } _ { j } , y _ { j } ) \right\} _ { j = 1 } ^ { M } ,$ $y _ { j } ~ \in ~ \mathcal { V } _ { b - 1 }$ . Using raw images enables the model to quickly recover former knowledge while having two main drawbacks — raw images consume large memory budget and saving them may violate privacy issues. To tackle this problem, feature replay is proposed by saving a set of features instead of raw images, i.e., $\pmb { \mathcal { E } } = \{ ( \phi ( \mathbf { x } _ { j } ) , y _ { j } ) \} _ { j = 1 } ^ { M } , y _ { j } \in \mathcal { V } _ { b - 1 }$ . Comparing to raw images with many pixels, features $\phi ( \mathbf { x } )$ are encoded in the embedding space with fewer dimensions, which helps to reduce the cost for memory budget. For example, saving a raw image of CIFAR costs $3 \times 3 2 \times 3 2$ integer numbers (int), while saving a feature by ResNet32 only costs 64 float numbers. Hence, the budget of saving a feature is equal to saving 64 floats ↖4 bytes/float $\div ( 3 \times 3 2 \times 3 2 )$ bytes/image $= \textstyle { \frac { 1 } { 1 2 } }$ image of CIFAR. Additionally, since features are irreversible representations of raw images, privacy issues can be alleviated by saving these features. However, the fatal problem of feature replay lies in the format of $\phi ( \mathbf { x } )$ . Since the embedding function is changing throughout the learning process, the features extracted at former stages will not be compatible with latter stages. Hence, it requires further alignment or mapping stage to transform features into the same embedding space. Finally, there is also a typical line of work on generative replay, i.e., utilizing generative models to model the distribution of former classes and generate exemplars when needed. A typical line of work using GAN [153] to memorize the distribution of former tasks and then replay them when learning new tasks [41], [42]. Specifically, GR [41] considers saving an extra GAN model as the generator and incrementally updates it when new data arrives. The classification model is optimized jointly with $\mathcal { D } ^ { b } \cup \mathcal { E }$ , where E stands for the generated dataset from the former distribution. However, incrementally updating a single GAN model will also incur catastrophic forgetting. It also requires a larger budget to save the GAN model than saving exemplars.

We supply an empirical study on these three kinds of replay strategies, and choose image replay [128] (IR), feature replay [38] (FR) and generative replay [41] (GR) for comparison on CIFAR100 B0 Inc10 and CIFAR100 B50 Inc10 settings. We reimplement [38]

Table 19: Incremental accuracy comparison of different methods under CIFAR100 Base0 Inc5 setting.   
Table 20: Incremental accuracy comparison of different methods under CIFAR100 Base0 Inc10 setting.   

<table><tr><td rowspan="2">Method</td><td colspan="20">Accuracy in each session (%) ↑</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td></tr><tr><td>Finetune</td><td>97.00</td><td>47.10</td><td>31.80</td><td>23.20</td><td>19.72</td><td>17.50</td><td>13.80</td><td>13.12</td><td>11.09</td><td>11.30</td><td>9.27</td><td>7.40</td><td>7.66</td><td>7.24</td><td>6.35</td><td>6.60</td><td>5.96</td><td>5.78</td><td>5.07</td><td>4.83</td></tr><tr><td>EWC</td><td>97.00</td><td>45.90</td><td>32.07</td><td>25.05</td><td>20.68</td><td>20.57</td><td>14.00</td><td>14.28</td><td>12.02</td><td>13.34</td><td>11.78</td><td>7.87</td><td>8.62</td><td>8.19</td><td>6.75</td><td>6.88</td><td>7.07</td><td>6.09</td><td>4.57</td><td>5.58</td></tr><tr><td>LwF</td><td>97.00</td><td>77.30</td><td>58.33</td><td>47.30</td><td>35.00</td><td>29.17</td><td>26.10</td><td>26.13</td><td>24.84</td><td>21.11</td><td>18.68</td><td>17.85</td><td>17.44</td><td>15.36</td><td>13.69</td><td>14.32</td><td>13.78</td><td>12.85</td><td>12.60</td><td></td></tr><tr><td>GEM</td><td>97.00</td><td>62.60</td><td>46.00</td><td>39.05</td><td>36.92</td><td>34.43</td><td>28.54</td><td>27.45</td><td>26.69</td><td>26.68</td><td>25.45</td><td>20.80</td><td>20.97</td><td>22.19</td><td>21.32</td><td>21.99</td><td>21.38</td><td>17.87</td><td>17.40</td><td>19.48</td></tr><tr><td>Replay</td><td>97.00</td><td>89.30</td><td>79.93</td><td>73.55</td><td>71.56</td><td>67.27</td><td>63.03</td><td>57.92</td><td>57.58</td><td>55.54</td><td>52.60</td><td>51.78</td><td>48.65</td><td>48.17</td><td>45.83</td><td>42.71</td><td>42.80</td><td>40.40</td><td>39.61</td><td>38.69</td></tr><tr><td>RMM</td><td>97.00</td><td>87.70</td><td>82.20</td><td>76.05</td><td>74.12</td><td>70.57</td><td>69.43</td><td>66.80</td><td>65.27</td><td>63.50</td><td>62.35</td><td>60.83</td><td>58.58</td><td>58.46</td><td>56.80</td><td>55.35</td><td>54.07</td><td>53.30</td><td>51.57</td><td>51.10</td></tr><tr><td>iCaRL</td><td>97.00</td><td>89.80</td><td>81.93</td><td>75.45</td><td>73.80</td><td>72.37</td><td>68.63</td><td>64.50</td><td>63.04</td><td>61.44</td><td>58.98</td><td>58.18</td><td>56.49</td><td>54.20</td><td>52.55</td><td>50.92</td><td>49.25</td><td>48.57</td><td>47.57</td><td>45.12</td></tr><tr><td>PODNet</td><td>97.20</td><td>84.90</td><td>73.27</td><td>62.40</td><td>59.08</td><td>54.60</td><td>50.31</td><td>46.40</td><td>44.76</td><td>43.28</td><td>40.73</td><td>39.35</td><td>37.74</td><td>36.73</td><td>34.97</td><td>32.99</td><td>31.84</td><td>30.62</td><td>28.35</td><td>27.99</td></tr><tr><td>Coil</td><td>97.00</td><td>89.90</td><td>82.33</td><td>75.35</td><td>73.88</td><td>69.40</td><td>65.86</td><td>60.65</td><td>58.82</td><td>56.38</td><td>52.89</td><td>50.57</td><td>48.37</td><td>45.51</td><td>42.92</td><td>39.25</td><td>38.09</td><td>36.57</td><td>35.34</td><td>34.33</td></tr><tr><td>WA</td><td>97.60</td><td>89.20</td><td>80.47</td><td>75.30</td><td>73.24</td><td>70.93</td><td>68.77</td><td>64.88</td><td>64.07</td><td>63.64</td><td>61.36</td><td>59.23</td><td>57.82</td><td>57.07</td><td>55.24</td><td>53.30</td><td>51.55</td><td>50.73</td><td>50.09</td><td>48.46</td></tr><tr><td>BiC</td><td>97.40</td><td>89.20</td><td>79.60</td><td>73.50</td><td>72.24</td><td>69.03</td><td>66.63</td><td>63.95</td><td>63.93</td><td>62.06</td><td>60.05</td><td>56.92</td><td>55.18</td><td>53.07</td><td>51.59</td><td>50.06</td><td>48.38</td><td>46.87</td><td>44.83</td><td>43.08</td></tr><tr><td>FOSTER</td><td>96.40</td><td>90.90</td><td>82.67</td><td>75.35</td><td>72.68</td><td>69.50</td><td>66.06</td><td>62.12</td><td>60.73</td><td>58.80</td><td>57.58</td><td>57.07</td><td>55.40</td><td>55.01</td><td>53.72</td><td>51.42</td><td>51.85</td><td>50.76</td><td>50.11</td><td>49.42</td></tr><tr><td>DER</td><td>97.00</td><td>89.40</td><td>81.40</td><td>76.85</td><td>75.60</td><td>74.20</td><td>72.11</td><td>68.72</td><td>67.40</td><td>66.04</td><td>64.24</td><td>63.37</td><td>62.03</td><td>61.69</td><td>60.19</td><td>58.59</td><td>56.93</td><td>55.48</td><td>54.57</td><td>53.95</td></tr><tr><td>MEMO</td><td>97.00</td><td>89.80</td><td>82.53</td><td>77.20</td><td>75.48</td><td>74.37</td><td>71.43</td><td>68.42</td><td>68.00</td><td>66.92</td><td>64.49</td><td>63.63</td><td>62.51</td><td>61.57</td><td>60.56</td><td>58.29</td><td>57.16</td><td>54.74</td><td>54.84</td><td>54.23</td></tr><tr><td>AANets</td><td>96.40</td><td>86.10</td><td>78.47</td><td>71.50</td><td>68.84</td><td>67.53</td><td>64.37</td><td>59.83</td><td>58.62</td><td>56.96</td><td>54.09</td><td>53.02</td><td>50.95</td><td>50.56</td><td>48.57</td><td>46.23</td><td>45.22</td><td>43.76</td><td>43.35</td><td>42.42</td></tr><tr><td>DyTox</td><td>94.60</td><td>90.20</td><td>83.13</td><td>79.40</td><td>77.28</td><td>75.73</td><td>73.31</td><td>71.53</td><td>69.13</td><td>67.80</td><td>66.24</td><td>63.63</td><td>62.05</td><td>60.83</td><td>58.45</td><td>55.23</td><td>53.33</td><td>54.06</td><td>52.97</td><td>52.23</td></tr><tr><td>L2P</td><td>97.80</td><td>96.90</td><td>90.67</td><td>88.75</td><td>88.32</td><td>86.67</td><td>87.20</td><td>85.12</td><td>84.44</td><td>83.76</td><td>80.67</td><td>80.28</td><td>77.77</td><td>79.40</td><td>77.52</td><td>78.72</td><td>78.33</td><td>79.27</td><td>79.46</td><td>78.96</td></tr></table>

<table><tr><td rowspan="2">Method</td><td colspan="10">Accuracy in each session (%)↑</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>Finetune</td><td>90.80</td><td>40.75</td><td>30.63</td><td>22.48</td><td>18.56</td><td>15.08</td><td>13.47</td><td>11.24</td><td>10.41</td><td>9.09</td></tr><tr><td>EWC</td><td>90.80</td><td>42.00</td><td>33.77</td><td>24.48</td><td>24.24</td><td>19.58</td><td>18.90</td><td>16.35</td><td>15.17</td><td>12.44</td></tr><tr><td>LwF</td><td>90.80</td><td>69.70</td><td>57.17</td><td>43.38</td><td>39.30</td><td>31.88</td><td>30.09</td><td>25.36</td><td>24.70</td><td>23.25</td></tr><tr><td>GEM</td><td>90.80</td><td>54.75</td><td>47.93</td><td>38.58</td><td>34.96</td><td>30.67</td><td>28.40</td><td>27.91</td><td>25.37</td><td>23.03</td></tr><tr><td>Replay</td><td>90.80</td><td>78.65</td><td>71.40</td><td>62.98</td><td>57.86</td><td>52.53</td><td>50.83</td><td>45.15</td><td>41.89</td><td>41.01</td></tr><tr><td>RMM</td><td>89.40</td><td>77.60</td><td>75.50</td><td>70.62</td><td>68.00</td><td>64.67</td><td>63.49</td><td>60.80</td><td>58.67</td><td>56.64</td></tr><tr><td>iCaRL</td><td>90.80</td><td>78.35</td><td>73.97</td><td>67.65</td><td>63.94</td><td>59.88</td><td>57.77</td><td>52.80</td><td>51.04</td><td>49.52</td></tr><tr><td>PODNet</td><td>89.70</td><td>72.10</td><td>65.57</td><td>57.45</td><td>53.48</td><td>49.57</td><td>46.00</td><td>42.10</td><td>39.44</td><td>36.78</td></tr><tr><td>Coil</td><td>90.60</td><td>79.25</td><td>73.00</td><td>65.00</td><td>59.82</td><td>55.40</td><td>52.31</td><td>45.76</td><td>41.73</td><td>39.85</td></tr><tr><td>WA</td><td>90.80</td><td>79.50</td><td>75.10</td><td>69.95</td><td>67.50</td><td>63.38</td><td>61.44</td><td>57.08</td><td>53.81</td><td>52.30</td></tr><tr><td>BiC</td><td>88.80</td><td>76.45</td><td>72.77</td><td>67.88</td><td>64.36</td><td>61.90</td><td>59.17</td><td>55.98</td><td>52.70</td><td>50.79</td></tr><tr><td>FOSTER</td><td>89.40</td><td>80.30</td><td>75.63</td><td>68.75</td><td>64.48</td><td>61.52</td><td>59.63</td><td>56.88</td><td>55.09</td><td>53.21</td></tr><tr><td>DER</td><td>90.80</td><td>78.80</td><td>75.97</td><td>71.72</td><td>69.22</td><td>66.58</td><td>64.99</td><td>61.75</td><td>60.21</td><td>58.59</td></tr><tr><td>MEMO</td><td>89.60</td><td>79.30</td><td>77.17</td><td>72.58</td><td>69.76</td><td>67.23</td><td>65.47</td><td>62.15</td><td>60.28</td><td>58.49</td></tr><tr><td>AANets</td><td>91.00</td><td>74.70</td><td>71.30</td><td>65.25</td><td>60.36</td><td>57.25</td><td>53.77</td><td>50.31</td><td>47.83</td><td>45.53</td></tr><tr><td>DyTox</td><td>91.60</td><td>80.00</td><td>77.30</td><td>74.35</td><td>72.16</td><td>67.68</td><td>65.89</td><td>62.63</td><td>60.40</td><td>58.72</td></tr><tr><td>L2P</td><td>98.50</td><td>95.15</td><td>93.47</td><td>91.00</td><td>89.84</td><td>86.32</td><td>85.71</td><td>85.17</td><td>84.97</td><td>83.39</td></tr></table>

Table 21: Incremental accuracy comparison of different methods under CIFAR100 Base50 Inc10 setting.   

<table><tr><td rowspan="2">Method</td><td colspan="6">Accuracy in each session (%) ↑</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Finetune</td><td>76.52</td><td>15.18</td><td>13.47</td><td>11.62</td><td>10.86</td><td>9.09</td></tr><tr><td>EWC</td><td>76.52</td><td>20.53</td><td>17.47</td><td>14.51</td><td>14.10</td><td>11.47</td></tr><tr><td>LwF</td><td>76.52</td><td>48.50</td><td>39.63</td><td>30.45</td><td>26.54</td><td>25.06</td></tr><tr><td>GEM</td><td>76.52</td><td>27.43</td><td>25.69</td><td>25.92</td><td>23.42</td><td>21.33</td></tr><tr><td>Replay</td><td>76.52</td><td>54.70</td><td>51.26</td><td>46.41</td><td>44.02</td><td>41.26</td></tr><tr><td>RMM</td><td>76.42</td><td>73.32</td><td>68.71</td><td>64.39</td><td>62.59</td><td>59.75</td></tr><tr><td>iCaRL</td><td>76.52</td><td>66.05</td><td>62.97</td><td>56.90</td><td>53.86</td><td>52.04</td></tr><tr><td>PODNet</td><td>76.60</td><td>70.13</td><td>66.00</td><td>61.05</td><td>57.73</td><td>55.21</td></tr><tr><td>Coil</td><td>76.52</td><td>63.12</td><td>57.10</td><td>50.06</td><td>45.53</td><td>41.24</td></tr><tr><td>WA</td><td>76.54</td><td>68.65</td><td>66.43</td><td>60.74</td><td>57.68</td><td>55.85</td></tr><tr><td>BiC</td><td>74.14</td><td>68.62</td><td>62.06</td><td>58.29</td><td>53.77</td><td>49.19</td></tr><tr><td>FOSTER</td><td>76.44</td><td>72.02</td><td>65.77</td><td>62.25</td><td>60.09</td><td>57.82</td></tr><tr><td>DER</td><td>76.52</td><td>72.05</td><td>69.79</td><td>65.69</td><td>63.33</td><td>61.94</td></tr><tr><td>MEMO</td><td>76.52</td><td>73.28</td><td>70.90</td><td>67.58</td><td>64.50</td><td>62.83</td></tr><tr><td>AANets</td><td>76.64</td><td>72.38</td><td>69.33</td><td>64.66</td><td>61.14</td><td>59.36</td></tr><tr><td>DyTox</td><td>79.96</td><td>74.62</td><td>71.16</td><td>65.58</td><td>62.73</td><td>60.35</td></tr><tr><td>L2P</td><td>92.56</td><td>88.05</td><td>85.96</td><td>83.76</td><td>81.60</td><td>79.34</td></tr></table>

Table 22: Incremental accuracy comparison of different methods under CIFAR100 Base50 Inc25 setting.   

<table><tr><td rowspan="2">Method</td><td colspan="3">Accuracy in each session (%) ↑</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>Finetune</td><td>76.52</td><td>27.29</td><td>20.88</td></tr><tr><td>EWC</td><td>76.52</td><td>30.72</td><td>23.85</td></tr><tr><td>LwF</td><td>76.52</td><td>48.48</td><td>37.31</td></tr><tr><td>GEM</td><td>76.52</td><td>41.80</td><td>37.29</td></tr><tr><td>Replay</td><td>76.52</td><td>52.85</td><td>44.07</td></tr><tr><td>RMM</td><td>76.42</td><td>70.51</td><td>64.63</td></tr><tr><td>iCaRL</td><td>76.52</td><td>64.88</td><td>57.59</td></tr><tr><td>PODNet</td><td>76.60</td><td>66.83</td><td>59.10</td></tr><tr><td>Coil</td><td>76.52</td><td>62.89</td><td>51.08</td></tr><tr><td>WA</td><td>76.54</td><td>66.57</td><td>61.49</td></tr><tr><td>BiC</td><td>74.68</td><td>65.91</td><td>59.77</td></tr><tr><td>FOSTER</td><td>76.44</td><td>70.01</td><td>62.38</td></tr><tr><td>DER</td><td>76.52</td><td>70.79</td><td>65.10</td></tr><tr><td>MEMO</td><td>76.52</td><td>71.36</td><td>66.06</td></tr><tr><td>AANets</td><td>76.56</td><td>69.79</td><td>61.85</td></tr><tr><td>DyTox</td><td>79.92</td><td>71.89</td><td>66.49</td></tr><tr><td>L2P</td><td>92.56</td><td>88.24</td><td>86.29</td></tr></table>

and [41] following the main paper. We use WGAN [237] as the generative model and implement it with four transposed convolutional layers. The optimization details (rounds, learning

rate, optimizer) are set according to the original paper. Specifically, training an extra GAN model requires much more parameters than saving exemplars/features, and we follow the comparison protocol

Table 23: Incremental accuracy comparison of different methods under ImageNet100 Base0 Inc5 setting.   
Table 24: Incremental accuracy comparison of different methods under ImageNet100 Base0 Inc10 setting.   

<table><tr><td rowspan="2">Method</td><td colspan="20">Accuracy in each session (%) ↑</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td></tr><tr><td>Finetune</td><td>94.40</td><td>42.20</td><td>30.13</td><td>26.90</td><td>19.76</td><td>16.33</td><td>13.83</td><td>12.30</td><td>10.40</td><td>9.80</td><td>9.42</td><td>8.27</td><td>7.51</td><td>7.23</td><td>6.72</td><td>6.05</td><td>5.79</td><td>5.11</td><td>5.20</td><td>4.70</td></tr><tr><td>EWC</td><td>94.40</td><td>41.80</td><td>32.93</td><td>28.60</td><td>23.84</td><td>19.87</td><td>15.89</td><td>15.75</td><td>12.49</td><td>10.68</td><td>10.00</td><td>9.60</td><td>8.80</td><td>9.06</td><td>8.00</td><td>7.30</td><td>7.25</td><td>6.29</td><td>6.19</td><td>6.14</td></tr><tr><td>LwF</td><td>94.40</td><td>78.20</td><td>63.87</td><td>59.60</td><td>56.56</td><td>55.33</td><td>51.20</td><td>44.40</td><td>42.00</td><td>36.08</td><td>31.45</td><td>29.10</td><td>29.20</td><td>27.80</td><td>27.95</td><td>27.20</td><td>22.99</td><td>20.24</td><td>20.32</td><td>17.74</td></tr><tr><td>Replay</td><td>94.80</td><td>83.80</td><td>73.33</td><td>74.30</td><td>66.16</td><td>65.27</td><td>61.71</td><td>59.85</td><td>54.27</td><td>54.36</td><td>52.84</td><td>49.57</td><td>46.95</td><td>42.69</td><td>43.73</td><td>41.92</td><td>43.13</td><td>42.18</td><td>39.31</td><td>37.32</td></tr><tr><td>RMM</td><td>94.40</td><td>83.60</td><td>80.67</td><td>80.30</td><td>76.72</td><td>74.33</td><td>72.86</td><td>71.15</td><td>69.73</td><td>69.60</td><td>68.87</td><td>66.80</td><td>64.22</td><td>62.69</td><td>61.36</td><td>61.28</td><td>60.19</td><td>59.40</td><td>58.74</td><td>57.16</td></tr><tr><td>iCaRL</td><td>94.40</td><td>86.80</td><td>80.67</td><td>78.90</td><td>73.44</td><td>70.80</td><td>66.06</td><td>63.45</td><td>62.76</td><td>59.76</td><td>58.40</td><td>55.20</td><td>53.94</td><td>51.80</td><td>50.61</td><td>50.85</td><td>48.38</td><td>47.78</td><td>47.98</td><td>44.10</td></tr><tr><td>PODNet</td><td>96.00</td><td>84.20</td><td>75.87</td><td>72.20</td><td>66.32</td><td>63.47</td><td>60.46</td><td>56.15</td><td>52.36</td><td>50.04</td><td>49.20</td><td>44.97</td><td>43.91</td><td>39.03</td><td>38.93</td><td>37.55</td><td>37.62</td><td>37.24</td><td>35.07</td><td>33.34</td></tr><tr><td>Coil</td><td>94.40</td><td>86.60</td><td>79.07</td><td>76.30</td><td>70.16</td><td>67.40</td><td>64.11</td><td>60.00</td><td>56.53</td><td>54.96</td><td>53.75</td><td>48.60</td><td>45.08</td><td>40.46</td><td>40.69</td><td>37.50</td><td>38.35</td><td>37.82</td><td>36.44</td><td>34.00</td></tr><tr><td>WA</td><td>94.80</td><td>84.20</td><td>78.27</td><td>78.30</td><td>73.12</td><td>71.67</td><td>69.14</td><td>65.30</td><td>64.27</td><td>62.04</td><td>61.42</td><td>57.30</td><td>54.31</td><td>51.46</td><td>49.79</td><td>50.25</td><td>49.95</td><td>49.36</td><td>48.17</td><td>46.06</td></tr><tr><td>BiC</td><td>94.80</td><td>84.60</td><td>78.67</td><td>76.40</td><td>72.08</td><td>70.40</td><td>66.51</td><td>64.15</td><td>59.60</td><td>55.84</td><td>54.95</td><td>50.93</td><td>49.94</td><td>46.49</td><td>44.24</td><td>41.75</td><td>40.02</td><td>38.36</td><td>36.38</td><td>34.56</td></tr><tr><td>FOSTER</td><td>94.40</td><td>87.00</td><td>77.60</td><td>75.50</td><td>71.36</td><td>67.87</td><td>65.54</td><td>63.05</td><td>61.42</td><td>61.72</td><td>61.71</td><td>59.60</td><td>56.25</td><td>55.23</td><td>56.05</td><td>56.02</td><td>55.91</td><td>54.84</td><td>54.84</td><td>53.18</td></tr><tr><td>DER</td><td>94.40</td><td>87.20</td><td>81.20</td><td>80.30</td><td>78.48</td><td>77.47</td><td>76.40</td><td>75.65</td><td>72.62</td><td>73.16</td><td>73.42</td><td>72.53</td><td>70.40</td><td>68.60</td><td>67.84</td><td>66.82</td><td>66.68</td><td>64.02</td><td>64.61</td><td>63.66</td></tr><tr><td>MEMO</td><td>94.40</td><td>84.80</td><td>77.47</td><td>78.10</td><td>72.96</td><td>72.93</td><td>71.20</td><td>68.90</td><td>67.64</td><td>66.68</td><td>67.38</td><td>64.87</td><td>63.20</td><td>62.23</td><td>60.37</td><td>59.42</td><td>59.67</td><td>58.07</td><td>57.41</td><td>56.10</td></tr><tr><td>AANets</td><td>96.80</td><td>85.00</td><td>76.93</td><td>74.20</td><td>65.76</td><td>62.00</td><td>59.66</td><td>56.20</td><td>55.60</td><td>54.52</td><td>54.04</td><td>52.33</td><td>49.94</td><td>48.23</td><td>46.61</td><td>46.12</td><td>46.00</td><td>44.56</td><td>42.48</td><td>41.64</td></tr><tr><td>DyTox</td><td>86.80</td><td>85.60</td><td>84.40</td><td>80.80</td><td>77.20</td><td>77.67</td><td>76.23</td><td>73.95</td><td>70.84</td><td>68.36</td><td>68.76</td><td>66.40</td><td>63.45</td><td>62.91</td><td>62.99</td><td>61.48</td><td>58.33</td><td>56.56</td><td>54.82</td><td>53.82</td></tr></table>

<table><tr><td rowspan="2">Method</td><td colspan="10">Accuracy in each session (%) ↑</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>Finetune</td><td>85.80</td><td>43.80</td><td>30.47</td><td>23.25</td><td>18.32</td><td>15.57</td><td>13.43</td><td>11.80</td><td>10.13</td><td>9.30</td></tr><tr><td>EWC</td><td>85.80</td><td>45.00</td><td>34.47</td><td>25.20</td><td>19.88</td><td>16.63</td><td>15.71</td><td>12.92</td><td>11.09</td><td>11.10</td></tr><tr><td>LwF</td><td>85.80</td><td>72.90</td><td>68.13</td><td>62.15</td><td>57.12</td><td>48.87</td><td>45.86</td><td>43.02</td><td>36.49</td><td>33.10</td></tr><tr><td>Replay</td><td>85.80</td><td>78.50</td><td>68.87</td><td>63.50</td><td>60.44</td><td>54.10</td><td>48.66</td><td>47.00</td><td>44.02</td><td>41.00</td></tr><tr><td>RMM</td><td>85.80</td><td>81.20</td><td>78.93</td><td>76.95</td><td>74.16</td><td>71.90</td><td>70.03</td><td>69.25</td><td>66.84</td><td>65.66</td></tr><tr><td>iCARL</td><td>85.80</td><td>82.10</td><td>76.00</td><td>71.95</td><td>67.64</td><td>63.77</td><td>60.03</td><td>56.55</td><td>53.64</td><td>50.98</td></tr><tr><td>PODNet</td><td>91.00</td><td>83.40</td><td>74.80</td><td>68.25</td><td>63.28</td><td>58.83</td><td>55.14</td><td>52.50</td><td>47.69</td><td>45.40</td></tr><tr><td>Coil</td><td>85.80</td><td>81.00</td><td>73.73</td><td>65.55</td><td>62.72</td><td>59.07</td><td>53.00</td><td>49.22</td><td>45.13</td><td>41.50</td></tr><tr><td>WA</td><td>85.80</td><td>82.00</td><td>75.93</td><td>72.95</td><td>69.44</td><td>65.97</td><td>61.63</td><td>59.65</td><td>57.36</td><td>55.04</td></tr><tr><td>BiC</td><td>87.00</td><td>80.50</td><td>74.93</td><td>72.90</td><td>69.20</td><td>64.17</td><td>59.51</td><td>53.52</td><td>47.16</td><td>42.40</td></tr><tr><td>FOSTER</td><td>85.80</td><td>79.80</td><td>74.27</td><td>70.05</td><td>68.64</td><td>65.97</td><td>63.69</td><td>63.12</td><td>61.67</td><td>60.58</td></tr><tr><td>DER</td><td>88.40</td><td>84.90</td><td>80.87</td><td>80.10</td><td>78.32</td><td>76.07</td><td>73.09</td><td>72.25</td><td>69.91</td><td>66.84</td></tr><tr><td>MEMO</td><td>85.80</td><td>79.60</td><td>75.93</td><td>73.35</td><td>70.52</td><td>69.77</td><td>65.66</td><td>65.05</td><td>63.40</td><td>60.96</td></tr><tr><td>AANets</td><td>86.40</td><td>78.80</td><td>72.60</td><td>66.35</td><td>62.84</td><td>59.23</td><td>53.66</td><td>52.38</td><td>49.64</td><td>46.60</td></tr><tr><td>DyTox</td><td>87.20</td><td>84.10</td><td>80.60</td><td>77.00</td><td>72.40</td><td>70.23</td><td>68.66</td><td>67.95</td><td>64.11</td><td>61.78</td></tr></table>

Table 25: Incremental accuracy comparison of different methods under ImageNet100 Base50 Inc10 setting.   

<table><tr><td rowspan="2">Method</td><td colspan="6">Accuracy in each session (%) ↑</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Finetune</td><td>84.40</td><td>15.63</td><td>13.57</td><td>11.68</td><td>10.20</td><td>9.26</td></tr><tr><td>EWC</td><td>84.40</td><td>15.97</td><td>17.51</td><td>15.08</td><td>12.98</td><td>11.54</td></tr><tr><td>LwF</td><td>84.40</td><td>47.13</td><td>41.60</td><td>38.48</td><td>34.42</td><td>31.42</td></tr><tr><td>Replay</td><td>84.40</td><td>57.20</td><td>51.49</td><td>50.30</td><td>47.58</td><td>43.38</td></tr><tr><td>RMM</td><td>83.40</td><td>79.23</td><td>70.97</td><td>70.20</td><td>67.78</td><td>66.52</td></tr><tr><td>iCaRL</td><td>84.40</td><td>64.57</td><td>59.94</td><td>58.22</td><td>54.89</td><td>53.68</td></tr><tr><td>PODNet</td><td>85.32</td><td>80.83</td><td>75.54</td><td>71.82</td><td>66.56</td><td>62.94</td></tr><tr><td>Coil</td><td>84.40</td><td>69.13</td><td>58.14</td><td>54.00</td><td>49.64</td><td>43.40</td></tr><tr><td>WA</td><td>84.40</td><td>67.70</td><td>63.66</td><td>62.92</td><td>59.56</td><td>56.64</td></tr><tr><td>BiC</td><td>84.60</td><td>77.10</td><td>67.17</td><td>63.55</td><td>55.82</td><td>49.90</td></tr><tr><td>FOSTER</td><td>84.40</td><td>77.53</td><td>66.43</td><td>64.97</td><td>63.62</td><td>63.12</td></tr><tr><td>DER</td><td>84.40</td><td>80.67</td><td>78.34</td><td>76.18</td><td>73.80</td><td>71.10</td></tr><tr><td>MEMO</td><td>84.40</td><td>80.13</td><td>77.71</td><td>75.68</td><td>72.82</td><td>70.22</td></tr><tr><td>AANets</td><td>85.08</td><td>81.23</td><td>76.51</td><td>73.90</td><td>69.78</td><td>66.84</td></tr><tr><td>DyTox</td><td>83.20</td><td>79.13</td><td>76.00</td><td>74.10</td><td>69.71</td><td>65.76</td></tr></table>

Table 26: Incremental accuracy comparison of different methods under ImageNet100 Base50 Inc25 setting.   

<table><tr><td rowspan="2">Method</td><td colspan="3">Accuracy in each session (%) ↑</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>Finetune</td><td>84.40</td><td>29.97</td><td>22.14</td></tr><tr><td>EWC</td><td>84.40</td><td>30.88</td><td>23.90</td></tr><tr><td>LwF</td><td>84.40</td><td>62.48</td><td>51.36</td></tr><tr><td>Replay</td><td>84.40</td><td>56.85</td><td>50.92</td></tr><tr><td>RMM</td><td>83.40</td><td>78.77</td><td>76.38</td></tr><tr><td>iCaRL</td><td>84.40</td><td>69.68</td><td>63.72</td></tr><tr><td>PODNet</td><td>85.32</td><td>77.65</td><td>71.14</td></tr><tr><td>Coil</td><td>84.40</td><td>68.03</td><td>58.64</td></tr><tr><td>WA</td><td>84.40</td><td>73.17</td><td>68.88</td></tr><tr><td>BiC</td><td>85.00</td><td>77.20</td><td>71.80</td></tr><tr><td>FOSTER</td><td>84.40</td><td>74.88</td><td>68.50</td></tr><tr><td>DER</td><td>84.40</td><td>79.25</td><td>74.88</td></tr><tr><td>MEMO</td><td>84.40</td><td>77.25</td><td>72.96</td></tr><tr><td>AANets</td><td>84.64</td><td>76.80</td><td>71.32</td></tr><tr><td>DyTox</td><td>83.96</td><td>77.07</td><td>71.18</td></tr></table>

in the main paper to align the memory cost of all methods. The comparison details are shown in Table 29. Note that [38] also includes a variation namely FR-hybird that saves both images and features in the memory, and we also implement it by dividing the total budgets into two parts. We report the performance comparison in Figure 28.

As we can infer from these figures, there are three main

conclusions.

• Utilizing generative replay fails in this setting, indicating the generative model also suffers catastrophic forgetting.   
• Utilizing feature replay alone cannot achieve competitive performance. However, using the hybrid replay memory can achieve competitive performance than image replay.   
• When the memory size is limited, using image replay shows

Table 27: Forgetting (F) and intransigence (I) measure on CIFAR100.   

<table><tr><td rowspan="2">Method</td><td colspan="2">Base0 Inc5</td><td colspan="2">Base0 Inc10</td><td colspan="2">Base50 Inc10</td><td colspan="2">Base50 Inc25</td></tr><tr><td>F</td><td>I</td><td>F</td><td>I</td><td>F</td><td>I</td><td>F</td><td>I</td></tr><tr><td>Finetune</td><td>0.9114</td><td>-0.1380</td><td>0.8834</td><td>-0.1107</td><td>0.8653</td><td>-0.1333</td><td>0.7921</td><td>-0.0662</td></tr><tr><td>EWC</td><td>0.7483</td><td>0.0094</td><td>0.7287</td><td>-0.0049</td><td>0.7998</td><td>-0.1181</td><td>0.7038</td><td>-0.0452</td></tr><tr><td>LwF</td><td>0.6998</td><td>-0.0147</td><td>0.5978</td><td>0.0048</td><td>0.4443</td><td>-0.0280</td><td>0.4349</td><td>-0.0038</td></tr><tr><td>GEM</td><td>0.4892</td><td>0.1166</td><td>0.4990</td><td>0.0959</td><td>0.4992</td><td>0.0844</td><td>0.4407</td><td>0.0387</td></tr><tr><td>Replay</td><td>0.5174</td><td>-0.1023</td><td>0.5040</td><td>-0.0884</td><td>0.4645</td><td>-0.0995</td><td>0.4564</td><td>-0.0478</td></tr><tr><td>RMM</td><td>0.1719</td><td>0.1018</td><td>0.1459</td><td>0.0776</td><td>0.0981</td><td>0.0495</td><td>0.0673</td><td>0.0482</td></tr><tr><td>iCaRL</td><td>0.3539</td><td>-0.0113</td><td>0.3348</td><td>-0.0212</td><td>0.2243</td><td>-0.0031</td><td>0.1907</td><td>0.0152</td></tr><tr><td>PODNet</td><td>0.4271</td><td>0.0905</td><td>0.3400</td><td>0.1015</td><td>0.1218</td><td>0.1156</td><td>0.1284</td><td>0.0709</td></tr><tr><td>Coil</td><td>0.5482</td><td>-0.0880</td><td>0.4748</td><td>-0.0505</td><td>0.3880</td><td>-0.0143</td><td>0.3534</td><td>-0.0485</td></tr><tr><td>WA</td><td>0.2791</td><td>0.0264</td><td>0.2790</td><td>0.0012</td><td>0.1854</td><td>0.0230</td><td>0.1197</td><td>0.0422</td></tr><tr><td>BiC</td><td>0.1823</td><td>0.2388</td><td>0.1748</td><td>0.1401</td><td>0.0980</td><td>0.4973</td><td>0.1006</td><td>0.0801</td></tr><tr><td>FOSTER</td><td>0.3325</td><td>-0.0340</td><td>0.2879</td><td>-0.0159</td><td>0.1478</td><td>-0.0022</td><td>0.1085</td><td>0.0225</td></tr><tr><td>DER</td><td>0.1894</td><td>0.0567</td><td>0.1840</td><td>0.0238</td><td>0.1098</td><td>0.0125</td><td>0.1065</td><td>0.0078</td></tr><tr><td>MEMO</td><td>0.2627</td><td>-0.0158</td><td>0.2081</td><td>0.0031</td><td>0.1226</td><td>-0.0201</td><td>0.0804</td><td>0.0180</td></tr><tr><td>AANets</td><td>0.3257</td><td>0.0425</td><td>0.2904</td><td>0.0586</td><td>0.1848</td><td>0.0507</td><td>0.1494</td><td>0.0405</td></tr></table>

Table 28: Forgetting (F) and intransigence (I) measure on ImageNet100.   

<table><tr><td rowspan="2">Method</td><td colspan="2">Base0 Inc5</td><td colspan="2">Base0 Inc10</td><td colspan="2">Base50 Inc10</td><td colspan="2">Base50 Inc25</td></tr><tr><td>F</td><td>I</td><td>F</td><td>I</td><td>F</td><td>I</td><td>F</td><td>I</td></tr><tr><td>Finetune</td><td>0.9404</td><td>-0.0744</td><td>0.9138</td><td>-0.0562</td><td>0.9156</td><td>-0.0679</td><td>0.8716</td><td>-0.0333</td></tr><tr><td>EWC</td><td>0.8971</td><td>-0.0476</td><td>0.8771</td><td>-0.0412</td><td>0.8656</td><td>-0.0643</td><td>0.8506</td><td>-0.0428</td></tr><tr><td>LwF</td><td>0.6524</td><td>0.0688</td><td>0.5513</td><td>0.0320</td><td>0.4392</td><td>-0.0069</td><td>0.3804</td><td>-0.0195</td></tr><tr><td>Replay</td><td>0.5800</td><td>-0.0582</td><td>0.5489</td><td>-0.0448</td><td>0.4989</td><td>-0.0656</td><td>0.4664</td><td>-0.0323</td></tr><tr><td>RMM</td><td>0.2535</td><td>0.0536</td><td>0.1807</td><td>0.0400</td><td>0.1457</td><td>0.0017</td><td>0.0678</td><td>0.0175</td></tr><tr><td>iCaRL</td><td>0.4589</td><td>-0.0110</td><td>0.4024</td><td>-0.0128</td><td>0.2967</td><td>-0.0080</td><td>0.2484</td><td>-0.0095</td></tr><tr><td>PODNet</td><td>0.5131</td><td>0.0452</td><td>0.4024</td><td>0.0430</td><td>0.2513</td><td>0.0115</td><td>0.1472</td><td>0.0319</td></tr><tr><td>Coil</td><td>0.5956</td><td>-0.0398</td><td>0.5318</td><td>-0.0344</td><td>0.4588</td><td>-0.0528</td><td>0.3444</td><td>-0.0348</td></tr><tr><td>WA</td><td>0.4139</td><td>0.0122</td><td>0.3169</td><td>0.0236</td><td>0.2430</td><td>0.0317</td><td>0.1722</td><td>0.0101</td></tr><tr><td>BiC</td><td>0.1400</td><td>0.4522</td><td>0.1589</td><td>0.3590</td><td>-0.0454</td><td>0.5754</td><td>0.1358</td><td>0.0204</td></tr><tr><td>FOSTER</td><td>0.3733</td><td>-0.0204</td><td>0.2971</td><td>-0.0140</td><td>0.1605</td><td>-0.0139</td><td>0.1644</td><td>-0.0041</td></tr><tr><td>DER</td><td>0.0299</td><td>0.2010</td><td>0.0633</td><td>0.1338</td><td>-0.0894</td><td>0.2112</td><td>0.0320</td><td>0.0692</td></tr><tr><td>MEMO</td><td>0.2785</td><td>0.0404</td><td>0.2431</td><td>0.0308</td><td>0.0658</td><td>0.0527</td><td>0.0948</td><td>0.0308</td></tr><tr><td>AANets</td><td>0.3817</td><td>0.0870</td><td>0.3611</td><td>0.0682</td><td>0.1278</td><td>0.0889</td><td>0.1122</td><td>0.0592</td></tr></table>

Table 29: Implementation details for different kinds of replay. ‘# I’ stands for the number of images saved in exemplar set, and ‘# F’ stands for the number of features. ‘MS’ stands for the total memory size (including exemplars and models).   

<table><tr><td>Method</td><td># I</td><td># F</td><td>Model Type</td><td># Parameters</td><td>MS</td></tr><tr><td>GR</td><td>0</td><td>0</td><td>ResNet32 + WGAN</td><td>3.35 M</td><td>12.78 MB</td></tr><tr><td>IR</td><td>3759</td><td>0</td><td>ResNet32</td><td>0.46 M</td><td>12.78 MB</td></tr><tr><td>FR</td><td>0</td><td>45108</td><td>ResNet32</td><td>0.46 M</td><td>12.78 MB</td></tr><tr><td>FR-hybrid</td><td>2000</td><td>21108</td><td>ResNet32</td><td>0.46 M</td><td>12.78 MB</td></tr></table>

the best performance and do not require other tuning techniques. Hence, when there is no restriction on privacy issues, using image replay is a simple yet effective solution.

# APPENDIX H

# INTRODUCTION ABOUT COMPARED METHODS

In this section, we give the detailed introduction about selected compared methods in the main paper. In the comparison, we aim to contain all kinds of methods in our taxonomy. Hence, we systematically choose 17 methods, including: Replay [128], RMM [144] (data replay), GEM [53] (data regularization), EWC [73] (parameter regularization), AANets [66], FOSTER [16], MEMO [17], DER [15], DyTox [18], L2P [69] (dynamic networks), LwF [81], iCaRL [82], PODNET [94], Coil [88] (knowledge

distillation), WA [112], BiC [83] (model rectify). The detailed introduction is as follows.

• Finetune is a typical baseline in CIL, which only utilizes the cross-entropy loss in new tasks to update the model while ignoring former tasks. It suffers severe forgetting of former tasks.   
• Replay [128] (data replay) is the typical baseline of data replay, which concatenates the exemplar set with the current dataset to update the model.   
• RMM [144] (data replay) is a recent state-of-the-art algorithm in data replay, which meta-learns an exemplar set organization policy and utilizes it for future tasks.   
• GEM [53] (data regularization) is a representative data regularization-based method, which utilizes exemplars as indicators during updating.   
• EWC [73] (parameter regularization) is a representative parameter regularization-based method, which measures the parameter importance via Fisher information matrix and prevents important parameters from drifting away.   
• AANets [66] (dynamic networks) is a representative dynamic network-based method, which builds a dual-branch network to capture task-specific information and adaptively aggregates them to balance stability and plasticity.   
• DER [15] (dynamic networks) is a representative dynamic network-based method, which expands an individual network for a new task and aggregates all backbones for feature representation.

![](images/ede3f5f4e3cb0caae5a8290c06b14655e0f4e2d9c8cd072e1326a7d97782d1aa.jpg)  
(a) CIFAR100 B0 Inc10

![](images/b40a048a3f2cd102f2bcf5bfbf619a787485f7687a537f54288d380048ad044d.jpg)  
(b) CIFAR100 B50 Inc10   
Figure 28: Incremental performance of different replay strategies. We align the total memory budget for fair comparison.

• FOSTER [16] (dynamic networks) is a state-of-the-art dynamic network-based method, which compresses the feature representation of multiple backbones into a single one to control the total budget.   
• MEMO [17] (dynamic networks) is a state-of-the-art dynamic network-based method, which decouples the network structure into specialized and generalized blocks and only expands specialized blocks based on the shared generalized blocks.   
• DyTox [18] (dynamic networks) is a state-of-the-art dynamic network-based method for ViT. Instead of expanding backbones, it proposes to expand a task-specific token to enhance the model’s representation ability.   
• L2P [69] (dynamic networks) is a state-of-the-art dynamic network-based method with pre-trained ViT. It learns a prompt pool to encode task-specific information. During inference, it utilizes a key-value matching strategy to select instancespecific prompts for encoding.   
• LwF [81] (knowledge distillation) is a representative knowledge distillation-based method, which is the first to introduce knowledge distillation into CIL.   
• iCaRL [82] (knowledge distillation & template-based classification) is a popular method in CIL, which extends LwF with exemplar replay and template-based classification (NCM).   
• PODNET [94] (knowledge distillation) is a state-of-the-art knowledge distillation-based method, which distills diverse pooled features among a set of models to resist forgetting.   
• Coil [88] (knowledge distillation) is a representative knowledge distillation-based method, which addresses the crossmodal distillation to enhance bi-directional knowledge flow.   
• BiC [83] (model rectify) is a representative model rectificationbased method, which learns an extra bias correction layer to rectify the biased output of fully-connected layers.   
WA [112] (model rectify) is a representative model rectification-based method, which normalizes the fullyconnected layers to reduce its inductive bias to resist forgetting.

The choice of these methods follows the development timeline of CIL, which is also the way we introduce these works. Addition-

ally, it not only contains all seven aspects of CIL algorithms in our taxonomy but also includes early works (e.g., EWC, LwF, iCaRL) and recent state-of-the-art (DER, MEMO, L2P). The choice also gives consideration to CNN-based methods, ViT-based methods (DyTox), and even pre-trained ViT-based methods (L2P).

# APPENDIX I

# DISCUSSIONS ABOUT CLASSIFICATION CRITERION AND SCOPES OF THIS SURVEY

In the main paper, we divide current class-incremental learning methods into seven groups based on the ‘key point’ of these methods. For example, for the methods discussing how to save and utilize exemplars for better rehearsal, we divide them into data replay-based methods. Similarly, we denote the methods of designing model expansion techniques to fit the network structure as data evolves as dynamic network-based methods. It must be noted that these methods also learn from each other, and there is no strict boundary between them. For example, iCaRL [82] utilizes knowledge distillation, template-based classification, and exemplar replay, but we assign it to the knowledge distillation-based methods. In fact, data replay is becoming a standard protocol in the classincremental learning community, which is widely adopted in most methods. As shown in main paper Figure 3, dynamic networks and knowledge distillation methods have dominated publications in recent years. However, it does not indicate that traditional methods like data replay are no longer popular. By contrast, most of these methods rely on the exemplar set to get better performance.

On the other hand, in the discussion of this paper, we mainly focus on the development of class-incremental learning in the image classification field. The main reason is that most influential works about CIL address the image classification problem. Furthermore, it has shown the potential to apply the techniques in classification into other tasks, e.g., semantic segmentation [193], [238], [239] [240], [241], object detection [137], [242], [243] [244], [245], [246] [247], video understanding [91], [161], medical surgery [248] [249], language model [250], [251], [252], [253], language-vision model [217], [254], etc. Specifically, object detection and semantic segmentation are two popular vision tasks that may also face

the incremental learning scenario. Continually updating a detection/segmentation model will also suffer catastrophic forgetting, making incremental learning ability a core factor for these scenarios. We then discuss the application of former techniques in these two popular settings.

Incremental Object Detection: Object detection focuses on identifying and locating objects within an image or a video sequence. While typical works focus on training an object detection model with all training sets at once, real-world applications also require continually updating the detection model, i.e., incremental object detection (IOD) [243]. In IOD, training samples for different object categories are observed in phases, restricting the ability of the trainer to access past data. The final target is to locate and identify the objects belonging to all seen classes, which is similar to CIL. However, since images can contain multiple objects in IOD, only the new categories are annotated in any given training phase, making it more challenging.

Knowledge distillation and data replay have been found effective in IOD. [243] applies knowledge distillation to the output of Fast R-CNN [255]. Moreover, the distillation can also be applied to other detectors (e.g., Faster R-CNN [256], GFL [257], RetinaNet [258], DERT [259] and CenterNet [260]) via intermediate features, which is similar to different distillation levels in CIL. ERD [247] focuses on elastically learning responses from the classification head and the regression head. MVCD [261] designs correlation distillation losses from channel-wise, pointwise, and instance-wise views to regularize the learning of the incremental model. Similarly, [262] applies knowledge distillation on both the region proposal network and the region classification network. Other works also apply knowledge distillation on the region proposal networks [263], [264], [265]. Moreover, exemplars can also help resist forgetting in IOD. [244] utilizes a set of exemplars for replay after each incremental step. [266] also designs an adaptive exemplar selection strategy for efficient exemplar selection in IOD. Most of these works are based on conventional detectors, while CL-DERT [267] finds directly applying knowledge distillation or data replay works poorly on transformer-based detectors (e.g., Deformable DETR [268] and UP-DETR [269]). It further designs detector knowledge distillation loss, focusing on the most informative and reliable predictions from old versions of the model. Other recent works also address the specific settings like few-shot IOD [242], [270], [271], [272], open-world IOD [244] and 3D IOD [273].

Continual Semantic Segmentation: As another popular topic, semantic segmentation aims to simplify the representation of the image into something more meaningful by assigning a label to each pixel of an image. When deploying semantic segmentation with incremental new classes, the setting is called continual semantic segmentation (CSS) [241], [274]. Similar to object detection, the application of typical CIL algorithms (e.g., knowledge distillation, data replay, and dynamic networks) can also be applied to CSS.

MiB [241] points out a core problem in CSS, namely background shift. Since each training step provides annotation only for a subset of all possible classes, pixels of the background class (i.e., pixels that do not belong to any other classes) exhibit a semantic distribution shift. To tackle this problem, it combines the output space distillation with cross-entropy loss to enable model updating without forgetting. To distill high-level information, PLOT [275] proposes a multi-scale pooling distillation scheme that preserves long- and short-range spatial relationships at the feature level. SDR [276] combines knowledge distillation with contrastive loss,

enabling the model to distill latent representations. RCIL [240] designs a pooled cube knowledge distillation strategy on both spatial and channel dimensions to further enhance the plasticity and stability of the CSS model. The second group relies on data replay to revisit former knowledge when learning new. SSUL [277] and EM [278] explore the application of exemplar replay in CSS. AMSS [279] proposes a memory sample selection mechanism that selects informative samples for effective replay in a fully automatic way. Besides, works also investigate the application of generative replay [160] and auxiliary data [160], [280] for data replay. Additionally, RCIL [240] also explores the application of dynamic networks in CSS. It freezes the convolutional layers of the former stage and learns a representation compensation module to fit new tasks. During inference, the old and new modules are merged via structural reparameterization. EWF [281] utilizes model fusion among different stage backbones to strike a balance between old and new knowledge. PFCSS [282] considers representation learning from the forward compatible perspective [104] and utilizes contrastive loss to enhance future knowledge.

Recent works in CSS also involve incremental learning in more challenging scenarios, e.g., learning with few-shot annotations [283], [284], different domains [285], [286], continual instance segmentation [287] [288] and weakly semantic segmentation [289]. Moreover, with the prosperity of foundation models, there are also works [289] transferring knowledge from the complementary foundation models for better performance.

# APPENDIX J

# FURTHER ANALYSIS

# J.1 Influence of exemplar numbers

Using exemplar replay to recover former knowledge is a common technique in CIL, whose capability is bounded by the size of the exemplar set. Specifically, if we can save all historical instances as exemplars and replay them during training, we can get an offline model that does not suffer forgetting. Hence, it is common to observe performance improvement with more saved exemplars. In this section, we change the number of exemplars for several typical methods, e.g., Replay, BiC, WA, PODNet, and iCaRL. We experiment on the CIFAR100 B0 Inc10 setting, and the benchmark protocol uses 2000 exemplars in total. To explore the influence of exemplar number, we change it among {100, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 5000, 6000, 8000, 10000} to investigate its influence on the final accuracy. We plot the results in Figure 29. Firstly, with the increase of exemplars, all methods achieve better performance, indicating their benefit in the incremental learning process. However, we also find the slope of all methods is becoming lower as exemplars increase. It indicates the trade-off between accuracy and memory consumption, i.e., we observe the accuracy increasing rate is almost saturated for exemplars > 4000.

# J.2 Running time comparison:

A recent work [228] considers another aspect of efficiency in CIL, i.e., computational efficiency. It focuses on realistic scenarios that cope with high-throughput streams, where computational bottlenecks impose implicit constraints on learning from past samples that can be too many to be revisited during training. In this section, we also supply an empirical study on computational efficiency. We consider reporting the running time comparison of different methods, which reveals another aspect of computational

![](images/384b4cd47a4c85c5b7b867c6b617f670bbfa5fbc07f5c2ba2aa881040a75077d.jpg)  
(a) Average accuracy

![](images/fda52c3575b499b0e3446053c4f123ee9f16394baa32fd611b55c92fc747fa9c.jpg)  
(b) Last accuracy

![](images/907988b1a3581fc36f954b1c88c58da718500ffb1f3c653d8b866c647b2be930.jpg)  
Figure 29: Average and last accuracy of different methods on CIFAR100 Base0 Inc10 with the change of exemplar number.   
Figure 30: Running time comparison of different methods on CIFAR100 B0 Inc10. The non-shaded area stands for running time with 2000 exemplars, while the shaded area stands for the extra time with aligned exemplars to DER.

efficiency. All the running time is evaluated on a single NVIDIA 3090 GPU. In Figure 30, we report the running time of DER and other compared methods in our memory-agnostic comparison. Specifically, we report two running times of other methods, one for 2000 exemplars (with the non-shaded area) and the other (with the shaded area) for memory-aligned exemplars to DER. As we can infer from this figure, equipping these methods with more exemplars leads to better performance, while the running time also faces a drastic increase. When the computational budget is strictly bounded, i.e., with limited iterations or updating time, we need to design more computationally-efficient algorithms.