---
title: "A Model or 603 Exemplars: Towards Memory-Efficient Exemplar-Free Continual"
authors:
  - "Kiwon Wang"
  - "Wei Wang"
  - "Mingyi Guo"
  - "Yongming Chen"
  - "Tianyu Liu"
  - "Hang Su"
date: "2022-05-26"
year: 2022
journal: "arXiv"
doi: "arXiv:2205.13218"
abstract: "Real-world applications require the classification model to adapt to new classes without forgetting old ones. Correspondingly, Class-Incremental Learning (CIL) aims to train a model with limited memory size to meet this requirement. Typical CIL methods tend to save representative exemplars from former classes to resist forgetting, while recent works find that storing models from history can substantially boost the performance. However, the stored models are not counted into the memory budget, which implicitly results in unfair comparisons. We find that when counting the model size into the total budget and comparing methods with aligned memory size, saving models do not consistently work, especially for the case with limited memory budgets. As a result, we need to holistically evaluate different CIL methods at different memory scales and simultaneously consider accuracy and memory size for measurement. On the other hand, we dive deeply into the construction of the memory buffer for memory efficiency. By analyzing the effect of different layers in the network, we find that shallow and deep layers have different characteristics in CIL. Motivated by this, we propose a simple yet effective baseline, denoted as MEMO for Memory-efficient Expandable MOdel. MEMO extends specialized layers based on the shared generalized representations, efficiently extracting diverse representations with modest cost and maintaining representative exemplars. Extensive experiments on benchmark datasets validate MEMO’s competitive performance. Code is available at: https://github.com/wangkiw/ICLR23-MEMO"
abstract_cn: "现实应用要求分类模型能够适应新类别而不遗忘旧类别。类增量学习（CIL）旨在训练一个内存受限的模型以满足这一需求。典型的CIL方法倾向于保存旧类别的代表性样本来抵抗遗忘，而最近的研究发现存储历史模型可以显著提升性能。然而，存储的模型未被计入内存预算，这导致不公平的比较。我们发现，当将模型大小计入总预算并按对齐的内存大小比较方法时，保存模型并不总是有效，特别是在内存预算有限的情况下。因此，我们需要全面评估不同内存规模下的CIL方法，并同时考虑准确率和内存大小进行度量。另一方面，我们深入研究了内存缓冲区的构建以实现内存效率。通过分析网络中不同层的作用，我们发现浅层和深层在CIL中具有不同的特征。受此启发，我们提出了一个简单而有效的基线，称为MEMO（内存高效可扩展模型）。MEMO基于共享的通用表示扩展专用层，以适中的成本高效提取多样化的表示并保持代表性样本。在基准数据集上的大量实验验证了MEMO的竞争性能。"
keywords:
  - "[[Continual learning]]"
cite: "[1] Zhou D W, Wang Q W, Ye H J, et al. A Model or 603 Exemplars: Towards Memory-Efficient Exemplar-Free Continual Learning[C]. ICLR, 2023."
aiSum: "无样本持续学习内存优化：单一模型替代样本存储，竞争性能+低内存占用。"
confidence: "low"
wiki_concepts:
  - "[[Continual learning]]"
---

Da-Wei Zhou, Qi-Wei Wang, Han-Jia Ye∗, De-Chuan Zhan

State Key Laboratory for Novel Software Technology, Nanjing University {zhoudw, wangqiwei, yehj, zhandc}@lamda.nju.edu.cn

# ABSTRACT

Real-world applications require the classification model to adapt to new classes without forgetting old ones. Correspondingly, Class-Incremental Learning (CIL) aims to train a model with limited memory size to meet this requirement. Typical CIL methods tend to save representative exemplars from former classes to resist forgetting, while recent works find that storing models from history can substantially boost the performance. However, the stored models are not counted into the memory budget, which implicitly results in unfair comparisons. We find that when counting the model size into the total budget and comparing methods with aligned memory size, saving models do not consistently work, especially for the case with limited memory budgets. As a result, we need to holistically evaluate different CIL methods at different memory scales and simultaneously consider accuracy and memory size for measurement. On the other hand, we dive deeply into the construction of the memory buffer for memory efficiency. By analyzing the effect of different layers in the network, we find that shallow and deep layers have different characteristics in CIL. Motivated by this, we propose a simple yet effective baseline, denoted as MEMO for Memory-efficient Expandable MOdel. MEMO extends specialized layers based on the shared generalized representations, efficiently extracting diverse representations with modest cost and maintaining representative exemplars. Extensive experiments on benchmark datasets validate MEMO’s competitive performance. Code is available at: https://github.com/wangkiw/ICLR23-MEMO

# 1 INTRODUCTION

In the open world, training data is often collected in stream format with new classes appearing (Gomes et al., 2017; Geng et al., 2020). Due to storage constraints (Krempl et al., 2014; Gaber, 2012) or privacy issues (Chamikara et al., 2018; Ning et al., 2021), a practical Class-Incremental Learning (CIL) (Rebuffi et al., 2017) model requires the ability to update with incoming instances from new classes without revisiting former data. The absence of previous training data results in catastrophic forgetting (French, 1999) in CIL — fitting the pattern of new classes will erase that of old ones and result in a performance decline. The research about CIL has attracted much interest (Zhou et al., 2021b; 2022a;b; Liu et al., 2021b; 2023; Zhao et al., 2021a;b) in the machine learning field.

Saving all the streaming data for offline training is known as the performance upper bound of CIL algorithms, while it requires an unlimited memory budget for storage. Hence, in the early years, CIL algorithms are designed in a strict setting without retaining any instances from the former classes (Li & Hoiem, 2017; Kirkpatrick et al., 2017; Aljundi et al., 2017; Lee et al., 2017). It only keeps a classification model in the memory, which helps save the memory budget and meanwhile preserves privacy in the deployment. Afterward, some works noticed that saving limited exemplars from former classes can boost the performance of CIL models (Rebuffi et al., 2017; Chaudhry et al., 2019). Various exemplar-based methodologies have been proposed, aiming to prevent forgetting by revisiting the old during new class learning, which improves the performance of CIL tasks steadily (Rolnick et al., 2019; Castro et al., 2018; Wu et al., 2019; Isele & Cosgun, 2018). The utilization of exemplars has drawn the attention of the community from the strict setting to update the model with restricted memory

![](images/505391fe72e6922561817ad5900e7932c1285d8310e1c9e294176ff546d61e9a.jpg)  
(a) CIFAR100, Base0 Inc10

![](images/b7c17fa5db3b2c4f00a2421841a66c0125a1eb8377459388db15abcbc948f109.jpg)  
(b) ImageNet100, Base50 Inc5   
Figure 1: The average accuracy of different methods by varying memory size from small to large. The start point corresponds to the memory size of exemplar-based methods with benchmark backbone (WA (Zhao et al., 2020), iCaRL (Rebuffi et al., 2017), Replay (Chaudhry et al., 2019)), and the endpoint corresponds to the memory cost of model-based methods with benchmark backbone (DER (Yan et al., 2021) and MEMO (our proposed method)). We align the memory cost by using the small model for model-based methods or adding exemplars for exemplar-based methods. ‘Base’ stands for the number of classes in the first task, and ‘Inc’ represents the number of classes in each incremental new task. See Section 4.1 and 4.2 for more details.

size (Castro et al., 2018; Rebuffi et al., 2017). Rather than storing exemplars, recent works (Yan et al., 2021; Wang et al., 2022; Li et al., 2021; Douillard et al., 2021) find that saving backbones from the history pushes the performance by one step towards the upper bound. These model-based methods propose to train multiple backbones continually and aggregate their representations as the feature representation for final prediction. Treating the backbones from history as ‘unforgettable checkpoints,’ this line of work suffers less forgetting with the help of these diverse representations.

Model-based CIL methods push the performance towards the upper bound, but does that mean catastrophic forgetting is solved? Taking a close look at these methods, we find that they implicitly introduce an extra memory budget, namely model buffer for keeping old models. The additional buffer implicitly results in an unfair comparison to those methods without storing models. Take CIFAR100 (Krizhevsky et al., 2009) for an example; if we exchange the model buffer of ResNet32 (He et al., 2015) into exemplars of equal size and append them to iCaRL (Rebuffi et al., 2017) (a baseline without retaining models), the average accuracy drastically improves from 62% to 70%. How to fairly measure the performance of these methods remains a long-standing problem since saving exemplars or models will both consume the memory budget. In this paper, we introduce an extra dimension to evaluate CIL methods by considering both incremental performance and memory cost. For those methods with different memory costs, we need to align the performance measure at the same memory scale for a fair comparison.

How to fairly compare different methods? There are two primary sources of memory cost in CIL, i.e., exemplar and model buffer. We can align the memory cost by switching the size of extra backbones into extra exemplars for a fair comparison. For example, a ResNet32 model has the same memory size with 603 images for CIFAR100, and 297 ImageNet (Deng et al., 2009) images have the same memory size with a ResNet18 backbone. Figure 1 shows the fair comparison on benchmark datasets, e.g., CIFAR100 and ImageNet100. We report the average accuracy of different models by varying the memory size from small to large. The memory size of the start point corresponds to the cost of an exemplar-based method with a single backbone, and the endpoint denotes the cost of a model-based method with multiple backbones. As we can infer from these figures, there is an intersection between these methods — saving models is less effective when the total budget is limited while more effective when the total budget is ample.

In this paper, we dive deeply into the empirical evaluations of different CIL methods considering the incremental performance and memory budget. Towards a fair comparison between different approaches, we propose several new measures that simultaneously consider performance and memory size, e.g., area under the performance-memory curve and accuracy per model size. On the other hand, how to organize the memory buffer efficiently so that we can save more exemplars and meanwhile maintain diverse representations? We analyze the effect of different layers of the network by counting the gradients and shifting range in incremental learning, and find that shallow layers tend to learn generalized features. By contrast, deep layers fit specialized features for corresponding tasks and yield very different characteristics from task to task. As a result, sharing the shallow layers and only creating deep layers for new tasks helps save the memory budget in CIL.

Furthermore, the spared space can be exchanged for an equal number of exemplars to further boost the performance. Intuitively, we propose a simple yet effective baseline MEMO to simultaneously consider extending diverse features with the most modest memory cost. MEMO shows competitive results against state-of-the-art methods under the fair comparison on vast benchmark datasets and various settings, which obtains the best performance in most cases of Figure 1.

# 2 RELATED WORK

We roughly divide current CIL methods into two groups, i.e., exemplar-based and model-based methods. The former group seeks to rehearse former knowledge when learning new, and the latter saves extra model components to assist incremental learning. Obviously, some methods do not fall into these two groups (Kirkpatrick et al., 2017; Li & Hoiem, 2017; Jin et al., 2021; Smith et al., 2021), and we refer the readers to (Zhou et al., 2023) for a holistic review.

Exemplar-Based Methods: Exemplars are representative instances from former classes (Welling, 2009), and CIL models can selectively save a relatively small amount of exemplars for rehearsal during updating (Isele & Cosgun, 2018). Like natural cognitive systems, rehearsal helps revisit former tasks to resist catastrophic forgetting (Parisi et al., 2019). Apart from direct replay, there are other methods addressing utilizing exemplars in CIL. iCaRL (Rebuffi et al., 2017) builds knowledge distillation (Zhou et al., 2003; Zhou & Jiang, 2004; Hinton et al., 2015) regularization with exemplars to align the predictions of old and new models. On the other hand, (Lopez-Paz & Ranzato, 2017) treats the loss on the exemplar set as an indicator of former tasks’ performance and solves the quadratic program problem as regularization. (Wu et al., 2019; Castro et al., 2018) utilize exemplars for balanced finetuning or bias correction. Note that exemplars can be directly saved or be generated with extra generative models (Shin et al., 2017b; He et al., 2018), which indicates the equivalency between models and exemplars. Consistent with our intuition, there has been much research addressing that saving more exemplars will improve the performance of CIL models correspondingly (Iscen et al., 2020; Ahn et al., 2021).

Model-Based Methods: There are some methods that consider increasing model components incrementally to meet the requirements of new classes. (Liu et al., 2021a) adds residual blocks as mask layers to balance stability and plasticity. (Ostapenko et al., 2021) expands dynamic modules with dynamic routing to generalize to related tasks. (Yoon et al., 2018) creates new neurons to depict the features for new classes when needed, and (Xu & Zhu, 2018) formulates it as a reinforcement learning problem. Instead of expanding the neurons, some works (Serra et al., 2018; Rajasegaran et al., 2019; Abati et al., 2020) propose to learn masks and optimize the task-specific sub-network. These methods increase a modest amount of parameters to be optimized. Recently, (Yan et al., 2021) addresses that aggregating the features by training a single backbone for each incremental task can substantially improve the performance. Since there could be numerous incremental tasks in CIL, saving a backbone per task implicitly shifts the burden of storing exemplars into retaining models.

Memory-Efficient CIL: Memory cost is an important factor when deploying models into real-world applications. (Iscen et al., 2020) addresses saving extracted features instead of raw images can help model learning. Similarly, (Zhao et al., 2021c) proposes to save low-fidelity exemplars to reduce the memory cost. (Smith et al., 2021; Choi et al., 2021) release the burden of exemplars by data-free knowledge distillation (Lopes et al., 2017). To our knowledge, we are the first to address the memory-efficient problem in CIL from the model buffer perspective.

# 3 PRELIMINARIES

# 3.1 PROBLEM DEFINITION

Class-incremental learning was proposed to learn a stream of data continually with new classes (Reoverlapping classes, where buffi et al., 2017). Assume there are a sequence of B training tasks $\mathbf { \mathcal { D } ^ { b } } = \left\{ \left( \mathbf { x } _ { i } ^ { b } , y _ { i } ^ { b } \right) \right\} _ { i = 1 } ^ { n _ { b } }$ is the b-th incremental step with $\left\{ \mathcal { D } ^ { 1 } , \mathbf { \dot { \mathcal { D } } } ^ { 2 } , \cdots , \mathcal { D } ^ { B } \right\}$ $n _ { b }$ instances. without $\mathbf { x } _ { i } ^ { b } \in \mathbb { R } ^ { D }$ is a training instance of class $y _ { i } \in Y _ { b } , Y _ { b }$ is the label space of task b, where $Y _ { b } \cap Y _ { b ^ { \prime } } = \emptyset$ for $b \neq b ^ { \prime }$ . A fixed number of representative instances from the former classes are selected as exemplar set ${ \mathcal { E } } , | { \mathcal { E } } | = K$ is the fixed exemplar size. During the training process of task $b ,$ we can only access data from $\mathcal { D } ^ { b }$ and E. The aim of CIL at each step is not only to acquire the knowledge from the current task $\mathcal { D } ^ { b }$ but also to preserve the knowledge from former tasks. After each task, the trained

model is evaluated over all seen classes $\mathcal { V } _ { b } = Y _ { 1 } \cup \cdot \cdot \cdot Y _ { b }$ . The incremental model is unaware of the task id, $i . e . , b ,$ during inference. We decompose the model into the embedding module and linear layers, i.e., $f ( \mathbf { x } ) = W ^ { \top } \phi ( \mathbf { x } )$ , where $\phi ( \cdot ) : \bar { \mathbb { R } } ^ { D }  \mathbb { R } ^ { d } , W \in \mathbb { R } ^ { d \times | \mathcal { V } _ { b } | }$ .

# 3.2 OVERCOME FORGETTING IN CLASS-INCREMENTAL LEARNING

In this section, we separately introduce two baseline methods in CIL. The former baseline belongs to the exemplar-based method, while the latter belongs to the model-based approach.

Knowledge Distillation: To make the updated model still capable of classifying the old class instances, a common approach in CIL combines cross-entropy loss and knowledge distillation loss (Zhou et al., 2003; Zhou & Jiang, 2004; Hinton et al., 2015). It builds a mapping between the former and the current model:

$$
\mathcal {L} (\mathbf {x}, y) = (1 - \lambda) \underbrace {\sum_ {k = 1} ^ {| \mathcal {Y} _ {b} |} - \mathbb {I} (y = k) \log \mathcal {S} _ {k} \left(W ^ {\top} \phi (\mathbf {x})\right)} _ {\text {C r o s s E n t r o p y}} + \lambda \underbrace {\sum_ {k = 1} ^ {| \mathcal {Y} _ {b - 1} |} - \mathcal {S} _ {k} \left(\bar {W} ^ {\top} \bar {\phi} (\mathbf {x})\right) \log \mathcal {S} _ {k} \left(W ^ {\top} \phi (\mathbf {x})\right)} _ {\text {K n o w l e d g e D i s t i l l a t i o n}}, \tag {1}
$$

where $\mathcal { V } _ { b - 1 } = Y _ { 1 } \cup \cdot \cdot \cdot Y _ { b - 1 }$ denotes the set of old classes, λ is trade-off parameter, and $S _ { k } ( \cdot )$ denotes the k-th class probability after softmax operation. W¯ and $\bar { \phi }$ correspond to frozen classifier and embedding before learning $\mathring { \mathcal { D } } ^ { b }$ . Aligning the output of the old and current models helps maintain discriminability and resist forgetting. The model optimizes Eq. 1 over the current dataset and exemplar set $\mathcal { D } ^ { b } \cup \mathcal { E }$ . It depicts a simple way to simultaneously consider learning new class and preserving old class knowledge, which is widely adopted in exemplar-based methods (Rebuffi et al., 2017; Wu et al., 2019; Zhao et al., 2020).

Feature Aggregation: Restricted by the representation ability, methods with a single backbone cannot depict the dynamic features of new classes. For example, if the first task contains ‘tigers,’ the CIL model will pay attention to the features to trace the beards and stripes. If the next task contains ‘birds,’ the features will then be adjusted for beaks and feathers. Since a single backbone can depict a limited number of features, learning and overwriting new features will undoubtedly trigger the forgetting of old ones. To this end, DER (Yan et al., 2021) proposes to add a backbone to depict the new features for new tasks. For example, in the second stage, it initializes a new feature embedding $\phi _ { n e w } : \mathbb { R } ^ { D }  \mathbb { R } ^ { d }$ and freezes the old embedding $\phi _ { o l d }$ . It also initializes a new linear layer $W _ { n e w } \in \mathbb { R } ^ { 2 d \times | y _ { b } | }$ inherited from the linear layer $W _ { o l d }$ of the last stage, and optimizes the model with typical cross-entropy loss:

$$
\mathcal {L} (\mathbf {x}, y) = \sum_ {k = 1} ^ {| \mathcal {Y} _ {b} |} - \mathbb {I} (y = k) \log \mathcal {S} _ {k} \left(W _ {n e w} ^ {\top} \left[ \bar {\phi} _ {o l d} (\mathbf {x}), \phi_ {n e w} (\mathbf {x}) \right]\right). \tag {2}
$$

Similar to Eq. 1, the loss is optimized over $\mathcal { D } ^ { b } \cup \mathcal { E }$ , aiming to learn new classes and remember old ones. It also includes an auxiliary loss to differentiate the embeddings of old and new backbones, which will be discussed in the supplementary. Eq. 2 sequentially optimizes the newest added backbone $\phi _ { n e w }$ and fixes old ones. It can be seen as fitting the residual term to obtain diverse feature representations among all seen classes. Take the aforementioned scenario for an example. The model will first fit the features for beards and strides to capture tigers in the first task with $\phi _ { o l d }$ . Afterward, it optimizes the features for beaks and feathers to recognize birds in the second task with $\phi _ { n e w } $ . Training the new features will not harm the performance of old ones, and the model can obtain diverse feature representations as time goes by. However, since it creates a new backbone per new task, it requires saving all the embeddings during inference and consumes a much larger memory cost compared to exemplar-based methods.

# 4 ANALYSIS

# 4.1 EXPERIMENTAL SETUP

As our paper is heavily driven by empirical observations, we first introduce the three main datasets we experiment on, the neural network architectures we use, and the implementation details.

Dataset: Following the benchmark setting (Rebuffi et al., 2017; Wu et al., 2019), we evaluate the performance on CIFAR100 (Krizhevsky et al., 2009), and ImageNet100/1000 (Deng et al., 2009). CIFAR100 contains 50,000 training and 10,000 testing images, with a total of 100 classes. Each image is represented by 32 × 32 pixels. ImageNet is a large-scale dataset with 1,000 classes, with about 1.28 million images for training and 50,000 for validation. We also sample a subset of 100 classes according to (Wu et al., 2019), denoted as ImageNet100.

Dataset Split: According to the common setting in CIL (Rebuffi et al., 2017), the class order of training classes is shuffled with random seed 1993. There are two typical class splits in CIL. The former (Rebuffi et al., 2017) equally divides all the classes into B stages. The latter (Hou et al., 2019; Yu et al., 2020) treats half of the total classes in the first stage (denoted as base classes) and equally divides the rest classes into the incremental stages. Without loss of generality, we use Base-x, Inc-y to represent the setting that treats x classes as base classes and learns y new classes per task. $x = 0$ denotes the former setting.

Implementation Details: All models are deployed with PyTorch (Paszke et al., 2019) and Py-CIL (Zhou et al., 2021a) on NVIDIA 3090. If not specified otherwise, we use the same network backbone (Rebuffi et al., 2017) for all compared methods, i.e., ResNet32 (He et al., 2015) for CI-FAR100 and ResNet18 for ImageNet. The model is trained with a batch size of 128 for 170 epochs, and we use SGD with momentum for optimization. The learning rate starts from 0.1 and decays by 0.1 at 80 and 150 epochs. The source code of MEMO will be made publicly available upon acceptance. We use the herding (Welling, 2009) algorithm to select exemplars from each class.

# 4.2 HOW TO FAIRLY COMPARE CIL METHODS?

As discussed in Section 3.2, exemplar-based methods and model-based methods consume different memory sizes when learning CIL tasks. Aiming for a fair comparison, we argue that these methods should be aligned to the same memory cost when comparing the results. Hence, we vary the total memory cost from small to large and compare different methods at these selected points. Figure 1 shows corresponding results, which indicates the performance given different memory budget. Take Figure 1(a) for an example; we first introduce how to set the start point and endpoint. The memory size of the start point corresponds to a benchmark backbone, i.e., ResNet32. The memory size of the endpoint corresponds to the model size of model-based methods using the same backbone, i.e., saving 10 ResNet32 backbones in this setting. For other points of the X-axis, we can easily extend exemplar-based methods to these memory sizes by adding exemplars of equal size. For example, saving a ResNet32 model costs 463, 504 parameters (float), while saving a CIFAR image costs 3 × 32 × 32 integer numbers (int). The budget of saving a backbone is equal to saving 463, 504 floats ×4 bytes/float $\div ( 3 \times 3 2 \times 3 2 )$ bytes/image ≈ 603 instances for CIFAR. We cannot use the same backbone as the exemplar-based methods for model-based ones when the memory size is small. Hence, we divide the model parameters into ten equal parts (since there are ten incremental tasks in this setting) and look for a backbone with similar parameter numbers. For example, we separately use ConvNet, ResNet14, ResNet20, and ResNet26 as the backbone for these methods to match different memory scales. Please refer to supplementary for more details.

Given these curves, there are two questions. First, what is a good performance measure considering memory cost? We argue that a good CIL method with extendability should work for any memory cost. As a result, it is intuitive to measure the area under the curve (AUC) for these methods for a holistic overview. Observing that model-based methods work at large memory costs while failing at small costs in Fig-

![](images/92b14a72bac1e075035c4625f6ab8327ff73a76d122ef08be45dda0b0ede1c96.jpg)  
$\mathrm { ( a ) \ M e m o r y { S i z e } = 1 2 . 4 M B }$

![](images/4a7b91dd69d6a0ae081c392f9edc446e66aaa92b3a86ce72b86834402cd3518a.jpg)  
(b) Memory Size = 23.5MB   
Figure 2: Performance of different methods when fixing the total budget and varying the ratio of model size to total memory size on CIFAR100.

ure 1, we argue that measuring performance at the start point and endpoint can also be representative measures. Secondly, given a specific memory cost, should we use a larger model or more exemplars? Denote the ratio of model size as ρ = Size(Model)/Size(Total). We vary this ratio

![](images/5f376a9790587417570dd306944b1874c46c535ead62f16e6992025efdd645b1.jpg)  
(a) Gradient norm (log scale)

![](images/1a1ce55c61cd55cd5c880857c14964932e96bfa962197e17e51e98e49f5c7822.jpg)  
(b) Shift of different blocks

![](images/150348bcf0b50e4116af2d0dcacfa91c8b0fc78e2e8f0db5b65bd14454747668.jpg)  
(c) CKA between backbones   
Figure 3: Left: gradient norm of different residual blocks when optimizing Eq. 1. Deeper layers have larger gradients, while shallow layers have small gradients. Middle: Shift between the first and last epoch of different residual blocks. Deeper layers change more, while shallow layers change less. Right: feature similarity (CKA) of different backbones learned by Eq. 2. The lower triangular matrix denotes the similarity between deeper layers; the upper triangular matrix denotes the similarity between shallow layers.

for exemplar-based methods at two different memory scales in Figure 2. We switch ResNet32 to ResNet44/56/110 to enlarge ρ. Results indicate that the benefit from exemplars shall converge when the budget is large enough (i.e., Figure 2(b)), where switching to a larger model is more memoryefficient. However, this trend does not hold when the total memory budget is limited, i.e., Figure 2(a), and there is no consistent rule in these figures. As a result, we report results with the same benchmark backbone in Figure 1 for consistency.

# 4.3 DO WE NEED A NEW BACKBONE PER TASK?

Aggregating the features from multiple stages can obtain diverse representations while sacrificing the memory size for storing backbones. From the memory-efficient perspective, we wonder if all layers are equal in CIL — if the storage of some layers is unnecessary, switching them for exemplars will be more memory-efficient for the final performance. In detail, we analyze from three aspects, i.e., block-wise gradient, shift, and similarity on CIFAR100 with ResNet32. Experiments with other backbones (e.g., ViT) and datasets (e.g., NLP) can be found in Section C.10.

Block-Wise Gradient: We first conduct experiments to analyze the gradient of different residual blocks when optimizing Eq. 1. We show the gradient norm of different layers in a single task in Figure 3(a). A larger block index corresponds to deeper layers. It indicates that the gradients of shallow layers are much smaller than deep layers. As a result, deeper layers shall face stronger adjustment within new tasks, while shallow layers tend to stay unchanged during CIL.

Block-Wise Shift: To quantitatively measure the adjustment of different layers, we calculate the mean square error (MSE) per block between the first and last epoch for every incremental stage in Figure 3(b). It shows that the shift of deeper layers is much higher than shallow layers, indicating that deeper layers change more while shallow layers change less. It should be noted that MSE in the first task D1 is calculated for the randomly initialized network, which shows different trends than others. These results are consistent with the observations of gradients in Figure 3(a).

Feature Similarity: Observations above imply the differences between shallow and deep layers in CIL. We also train a model with Eq. 2 for 10 incremental stages, resulting in 10 backbones. We use centered kernel alignment (CKA) (Kornblith et al., 2019), an effective tool to measure the similarity of network representations to evaluate the relationships between these backbones. We can get corresponding feature maps by feeding the same batch of instances into these backbones. Afterward, CKA is applied to measure the similarity between these feature maps. We separately calculate the similarity for deep (i.e., residual block 15) and shallow features (i.e., residual block 5) and report the similarity matrix in Figure 3(c). The similarities between deep features are shown in the lower triangular matrix, and the similarities between shallow features are shown in the upper triangular matrix. Results indicate that the features of shallow layers among all backbones are highly similar, while diverse for deeper layers.

To summarize, we empirically find that not all layers are equal in CIL, where shallow layers yield higher similarities than deeper layers. A possible reason is that shallow layers tend to provide general-purpose representations, whereas later layers specialize (Maennel et al., 2020; Ansuini et al., 2019; Arpit et al., 2017; Yosinski et al., 2014; Zhang et al., 2019). Hence, expanding general layers would be less effective since they are highly similar. On the other hand, expanding and saving the specialized features is essential, which helps extract diverse representations continually.

![](images/9010b778007c6f58d227dd29847afc0314c4c47075e13e0eb023061e83b3836a.jpg)  
Figure 4: An overview of three typical methods. Left: Exemplar-based methods train a single model. Middle: Model-based methods train a new model per new task. Right: MEMO trains a new specialized block per new task. When aligning the memory cost of these methods, exemplar-based methods can save the most exemplars, while model-based methods have the least. MEMO strikes a trade-off between exemplar and model buffer.

# 4.4 MEMO: MEMORY-EFFICIENT EXPANDABLE MODEL

Motivated by the observations above, we seek to simultaneously consider saving exemplars and model extension in a memory-efficient manner. We ask:

Given the same memory budget, if we share the generalized blocks and only extend specialized blocks for new tasks, can we further improve the performance?

Concretely, we redefine the model structure in Eq. 2 by decomposing the embedding module into specialized and generalized blocks, i.e., $\phi ( \mathbf { x } ) = \phi _ { s } \overline { { ( \phi _ { g } ( \mathbf { x } ) ) } } .$ 1 Specialized block $\phi _ { s } ( \cdot )$ corresponds to the deep layers in the network (the last basic layer in our setting, see Section B.1 for details), while generalized block $\phi _ { g } ( \cdot )$ corresponds to the rest shallow layers. We argue that the features of shallow layers can be shared across different incremental stages, i.e., there is no need to create an extra $\phi _ { g } ( \cdot )$ for every new task. To this end, we can extend the feature representation by only creating specialized blocks $\phi _ { s }$ based on shared generalized representations. We can modify the loss function in Eq. 2 into:

$$
\mathcal {L} (\mathbf {x}, y) = \sum_ {k = 1} ^ {| \mathcal {Y} _ {b} |} - \mathbb {I} (y = k) \log \mathcal {S} _ {k} \left(W _ {n e w} ^ {\top} \left[ \phi_ {s _ {o l d}} \left(\phi_ {g} (\mathbf {x})\right), \phi_ {s _ {n e w}} \left(\phi_ {g} (\mathbf {x})\right) \right]\right). \tag {3}
$$

Effect of block sharing: We illustrate the framework of MEMO in Figure 4. There are two advantages of MEMO. Firstly, it enables a model to extract new features by adding specialized blocks continually. Hence, we can get a holistic view of the instances from various perspectives, which in turn facilitates classification. Secondly, it saves the total memory budget by sharing the generalized blocks compared to Eq. 2. It is less effective to sacrifice an extra memory budget to extract similar feature maps of these homogeneous features. Since only the last basic block is created for new tasks, we can exchange the saved budget of generalized blocks for an equal size of exemplars. In other words, these extra exemplars will facilitate model training more than creating those generalized blocks.

Which Block Should be Frozen? By comparing Eq. 2 to Eq. 3, we can find that the network structure is decomposed, and only the specialized blocks are extended. It should be noted that the old backbone is fixed when learning new tasks in Eq. 2. However, since the generalized blocks are shared during the learning stages, should they be fixed as in Eq. 2 or be dynamic to learn new classes? We conduct corresponding experiments on CIFAR100 and report the

![](images/36007c0ffa705b8a702463a83aa42b604ad62827de513e3d3069b33bc10e3ac5.jpg)  
(a) CIFAR100 Base0 Inc10

![](images/9eb1f9f43ef20fc21cc5e7e4fc5b788e476be191e291f13f9f5cba1acdc0d64f.jpg)  
(b) CIFAR100 Base50 Inc10   
Figure 5: Experiments about specialized and generalized blocks. Specialized blocks should be fixed; while fixing or not generalized blocks depends on the number of classes in the base stage. Block with φ¯ means frozen, while without a bar means trainable.

incremental performance by changing the learnable blocks in Figure 5. In detail, we fix/unfix the specialized and generalized blocks in Eq. 3 when learning new tasks, which yields four combinations. We separately evaluate the results in two settings by changing the number of base classes. As shown in Figure 5, there are two core observations. Firstly, by comparing the results of whether freezing the

![](images/fd10f92b76a1c6f3a1611bde2052f05c80ae7ab898417859a3eae8c6df62219a.jpg)  
(a) CIFAR100 Base0 Inc5

![](images/7cbe19937ee18eb34c6ea6cf45b7a1b86e42721b05c195d48582e89f5c34b715.jpg)  
(b) CIFAR100 Base0 Inc10

![](images/caeadd72c55f1732b09fdb778055e4f45395fe1e56f87d2069bbc79858eeff38.jpg)  
(c) CIFAR100 Base50 Inc5

![](images/914dac613c9e4a09066c5492385919b5da0c1b5e5dd379547995a179c6e93790.jpg)  
(d) CIFAR100 Base50 Inc10

![](images/d94d65d4d4ef68e04fc80cbac4d210487fc9d1bf748ff613098443272e964976.jpg)  
(e) ImageNet100 Base50 Inc5

![](images/6d90ec46e7bed1ffa2719659d1b399dbb3c7663bf4676e6bfad8cf3ca0e4138c.jpg)  
(f) ImageNet1000 Base0 Inc100   
Figure 6: Top-1 accuracy along incremental stages. All methods are compared under the same memory budget as denoted in the image (aligned with DER). We report the performance gap after the last task of MEMO and the runner-up method at the end of the line. We list the last accuracy of each method in the legend, and report the incremental accuracy and configurations in Section A.3.

Table 1: Memory-aware performance measures for CIL. AUC depicts the dynamic ability with the change of memory size, and APM depicts the capacity at some specific memory cost.   

<table><tr><td>CIFAR100</td><td>AUC-A</td><td>AUC-L</td><td>APM-S</td><td>APM-E</td></tr><tr><td>Replay</td><td>10.49</td><td>8.02</td><td>7.68</td><td>2.97</td></tr><tr><td>iCaRL</td><td>10.81</td><td>8.64</td><td>8.32</td><td>3.00</td></tr><tr><td>WA</td><td>10.80</td><td>8.92</td><td>8.57</td><td>2.95</td></tr><tr><td>DER</td><td>10.74</td><td>8.95</td><td>7.05</td><td>2.97</td></tr><tr><td>MEMO</td><td>10.85</td><td>9.03</td><td>7.18</td><td>3.06</td></tr></table>

<table><tr><td>ImageNet100</td><td>AUC-A</td><td>AUC-L</td><td>APM-S</td><td>APM-E</td></tr><tr><td>Replay</td><td>553.6</td><td>470.1</td><td>0.137</td><td>5.2e-2</td></tr><tr><td>iCaRL</td><td>607.1</td><td>527.5</td><td>0.164</td><td>5.4e-2</td></tr><tr><td>WA</td><td>666.0</td><td>581.7</td><td>0.195</td><td>5.8e-2</td></tr><tr><td>DER</td><td>699.0</td><td>639.1</td><td>0.192</td><td>5.8e-2</td></tr><tr><td>MEMO</td><td>713.0</td><td>654.6</td><td>0.196</td><td>6.1e-2</td></tr></table>

specialized blocks, we can tell that methods freezing the specialized blocks of former tasks have stronger performance than those do not freeze specialized blocks. It indicates that the specialized blocks of former tasks should be frozen to obtain diverse feature representations. Secondly, when the base classes are limited (e.g., 10 classes), the generalized blocks are not generalizable and transferable enough to capture the feature representations, which need to be incrementally updated. By contrast, vast base classes (e.g., 50 classes) can build transferable generalized blocks, and freezing them can get better performance under such a setting. See Section C.2 for more results.

# 5 EXPERIMENT

# 5.1 REVISITING BENCHMARK COMPARISON FOR CIL

Former works evaluate the performance with the accuracy trend along incremental stages, which lack consideration of the memory budget and compare models at different X coordinates. As a result, in this section, we strike a balance between different methods by aligning the memory cost of different methods to the endpoint in Figure 1 (which is also the memory cost of DER). We show 6 typical results in Figure 6, containing different settings discussed in Section 4.1 on three benchmark datasets. We summarize two main conclusions from these figures. Firstly, the improvement of DER over other methods is not so much as reported in the original paper, which outperforms others substantially by 10% or more. In our observation, the improvement of DER than others under the fair comparison is much less, indicating that saving models shows slightly greater potential than saving exemplars when the memory budget is large. Secondly, MEMO outperforms DER by a substantial margin in most

![](images/73c6d51c295dd806efe0b94693aa8c6c7554d8b1b0ca5463bf33c2c040235671.jpg)  
(a) $\phi _ { s 1 } ( \phi _ { g } ( \mathbf { x } ) )$

![](images/266efdebaa5eec403e263380845308906893d01980b26e7ae946a96a19fac9a7.jpg)  
(b) $\phi _ { s 2 } ( \phi _ { g } ( \mathbf { x } ) )$

![](images/ee50ca1cf2e231736388a8c104bdd48458f842ff7a4535fdddabc1d72a9accc1.jpg)  
(c) $[ \phi _ { s 1 } ( \phi _ { g } ( \mathbf { x } ) ) , \phi _ { s 2 } ( \phi _ { g } ( \mathbf { x } ) ) ]$   
Figure 7: t-SNE visualizations on CIFAR100 of different specialized blocks learned by MEMO. Classes 1-5 are shown in dots, and classes 6-10 are shown in triangles.

cases, indicating ours is a simple yet effective way to organize CIL models with memory efficiency. These conclusions are consistent with our observations in Figure 2 and 3.

# 5.2 HOW TO MEASURE THE PERFORMANCE OF CIL MODELS HOLISTICALLY?

As discussed in Section 4.2, a suitable CIL model should be able to handle the task with any memory budget. Changing the model size from small to large enables us to evaluate different methods holistically. We observe that all the methods benefit from the increased memory size and perform better as it becomes larger in Figure 1. Hence, new performance measures should be proposed considering the model capacity. We first suggest the area under the performance-memory curve (AUC) since the curve of each method indicates the dynamic ability with the change of model size. We calculate AUC-A and AUC-L, standing for the AUC under the average performance-memory curve and last performance-memory curve. Similarly, we find that the intersection usually emerges near the start point of Figure 1. As a result, we can also calculate the accuracy per model size at the start point and endpoint, denoted as APM-S and APM-E separately. They represent the performance of the algorithm at different memory scales. It should be noted that these measures are not normalized into the centesimal scale, and the ranking among different methods is more important than the relative values. We report these measures in Table 1, where MEMO obtains the best performance in most cases (7 out of 8). Since all the methods are compared under the same budget, MEMO achieves the performance improvement for free, verifying its memory efficiency.

# 5.3 WHAT IS LEARNED BY SPECIALIZED BLOCKS?

Adding the specialized blocks helps extract diverse feature representations of a single instance. In this section, we train our model on CIFAR100 between two incremental stages; each contains five classes. We use t-SNE (Van der Maaten & Hinton, 2008) to visualize the property of these blocks. Classes from the first task are shown in dots, and classes from the second task are shown in triangles. We visualize the learned embedding of these separate specialized blocks in Figure 7(a) and 7(b). We can infer that the specialized blocks are optimized to discriminate the corresponding task, $i . e . , \phi _ { s 1 } ( \phi _ { g } ( \mathbf { x } ) )$ can recognize classes 1∼5 clearly, and $\phi _ { s 2 } ( \phi _ { g } ( \mathbf { x } ) )$ ) can tackle classes 6∼10 easily. When we aggregate the embeddings from these two backbones, i.e., $[ \phi _ { s 1 } ( \phi _ { g } ( \mathbf { x } ) ) , \phi _ { s 2 } ( \phi _ { g } ( \mathbf { x } ) ) ]$ ], the concatenated features are able to capture all the classes seen before. Results indicate that specialized blocks, which are fixed after learning the corresponding task, act as ‘unforgettable checkpoints.’ They will not lose discrimination as data evolves. Hence, we can aggregate diverse feature representations in the aggregated high dimension and divide decision boundaries easily.

# 6 CONCLUSION

Class-incremental learning ability is of great importance to real-world learning systems, requiring a model to learn new classes without forgetting old ones. In this paper, we answer two questions in CIL. Firstly, we fairly compare different methods by aligning the memory size at the same scale. Secondly, we find that not all layers are needed to be created and stored for new tasks, and propose a simple yet effective baseline, obtaining state-of-the-art performance for free in the fair comparison. Experiments verify the memory efficiency of our proposed method.

Limitations: CIL methods can also be divided by whether using extra memory. Apart from the methods discussed in this paper, there are other methods that do not save exemplars or models. We only concentrate on the methods with extra memory and select several typical methods for evaluation.

# ACKNOWLEDGMENT

This work is partially supported by NSFC (61921006, 62006112, 62250069), NSF of Jiangsu Province (BK20200313), Collaborative Innovation Center of Novel Software Technology and Industrialization, China Scholarship Council (CSC202206190134).

# REFERENCES

Davide Abati, Jakub Tomczak, Tijmen Blankevoort, Simone Calderara, Rita Cucchiara, and Babak Ehteshami Bejnordi. Conditional channel gated networks for task-aware [[Continual learning]]. In CVPR, pp. 3931–3940, 2020.   
Hongjoon Ahn, Jihwan Kwak, Subin Lim, Hyeonsu Bang, Hyojun Kim, and Taesup Moon. Ss-il: Separated softmax for incremental learning. In ICCV, pp. 844–853, 2021.   
Rahaf Aljundi, Punarjay Chakravarty, and Tinne Tuytelaars. Expert gate: Lifelong learning with a network of experts. In CVPR, pp. 3366–3375, 2017.   
Alessio Ansuini, Alessandro Laio, Jakob H Macke, and Davide Zoccolan. Intrinsic dimension of data representations in deep neural networks. NeurIPS, 32, 2019.   
Martin Arjovsky, Soumith Chintala, and Léon Bottou. Wasserstein gan. arXiv preprint arXiv:1701.07875, 2017.   
Devansh Arpit, Stanisław Jastrz˛ebski, Nicolas Ballas, David Krueger, Emmanuel Bengio, Maxinder S Kanwal, Tegan Maharaj, Asja Fischer, Aaron Courville, Yoshua Bengio, et al. A closer look at memorization in deep networks. In ICML, pp. 233–242. PMLR, 2017.   
Francisco M Castro, Manuel J Marín-Jiménez, Nicolás Guil, Cordelia Schmid, and Karteek Alahari. End-to-end incremental learning. In ECCV, pp. 233–248, 2018.   
Mahawaga Arachchige Pathum Chamikara, Peter Bertók, Dongxi Liu, Seyit Camtepe, and Ibrahim Khalil. Efficient data perturbation for privacy preserving and accurate data stream mining. Pervasive and Mobile Computing, 48:1–19, 2018.   
Arslan Chaudhry, Marcus Rohrbach, Mohamed Elhoseiny, Thalaiyasingam Ajanthan, Puneet K Dokania, Philip HS Torr, and M Ranzato. Continual learning with tiny episodic memories. 2019.   
Yoojin Choi, Mostafa El-Khamy, and Jungwon Lee. Dual-teacher class-incremental learning with data-free generative replay. In CVPR, pp. 3543–3552, 2021.   
Yulai Cong, Miaoyun Zhao, Jianqiao Li, Sijia Wang, and Lawrence Carin. Gan memory with no forgetting. NeurIPS, 33:16481–16494, 2020.   
Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. Imagenet: A large-scale hierarchical image database. In CVPR, pp. 248–255, 2009.   
Lei Deng, Guoqi Li, Song Han, Luping Shi, and Yuan Xie. Model compression and hardware acceleration for neural networks: A comprehensive survey. Proceedings of the IEEE, 108(4): 485–532, 2020.   
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805, 2018.   
Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, et al. An image is worth 16x16 words: Transformers for image recognition at scale. In ICLR, 2020.   
Arthur Douillard, Alexandre Ramé, Guillaume Couairon, and Matthieu Cord. Dytox: Transformers for continual learning with dynamic token expansion. arXiv preprint arXiv:2111.11326, 2021.   
Robert M French. Catastrophic forgetting in connectionist networks. Trends in cognitive sciences, 3 (4):128–135, 1999.

Mohamed Medhat Gaber. Advances in data stream mining. Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 2(1):79–85, 2012.   
Chuanxing Geng, Sheng-jun Huang, and Songcan Chen. Recent advances in open set recognition: A survey. TPAMI, pp. in press, 2020.   
Heitor Murilo Gomes, Jean Paul Barddal, Fabrício Enembreck, and Albert Bifet. A survey on ensemble learning for data stream classification. CSUR, 50(2):1–36, 2017.   
Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, and Yoshua Bengio. Generative adversarial nets. NIPS, 27, 2014.   
Stephen T Grossberg. Studies of mind and brain: Neural principles of learning, perception, development, cognition, and motor control, volume 70. Springer Science & Business Media, 2012.   
Chen He, Ruiping Wang, Shiguang Shan, and Xilin Chen. Exemplar-supported generative reproduction for class incremental learning. In BMVC, pp. 98, 2018.   
Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In CVPR, pp. 770–778, 2015.   
Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. Distilling the knowledge in a neural network. arXiv preprint arXiv:1503.02531, 2015.   
Saihui Hou, Xinyu Pan, Chen Change Loy, Zilei Wang, and Dahua Lin. Learning a unified classifier incrementally via rebalancing. In CVPR, pp. 831–839, 2019.   
Ahmet Iscen, Jeffrey Zhang, Svetlana Lazebnik, and Cordelia Schmid. Memory-efficient incremental learning through feature adaptation. In ECCV, pp. 699–715, 2020.   
David Isele and Akansel Cosgun. Selective experience replay for lifelong learning. In AAAI, 2018.   
Xisen Jin, Arka Sadhu, Junyi Du, and Xiang Ren. Gradient-based editing of memory examples for online task-free continual learning. NeurIPS, 34, 2021.   
Zixuan Ke, Hu Xu, and Bing Liu. Adapting bert for continual learning of a sequence of aspect sentiment classification tasks. In NAACL, pp. 4746–4755, 2021.   
Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola, Aaron Maschinot, Ce Liu, and Dilip Krishnan. Supervised contrastive learning. NeurIPS, 33:18661– 18673, 2020.   
James Kirkpatrick, Razvan Pascanu, Neil Rabinowitz, Joel Veness, Guillaume Desjardins, Andrei A Rusu, Kieran Milan, John Quan, Tiago Ramalho, Agnieszka Grabska-Barwinska, et al. Overcoming catastrophic forgetting in neural networks. PNAS, 114(13):3521–3526, 2017.   
Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. Similarity of neural network representations revisited. In ICML, pp. 3519–3529. PMLR, 2019.   
Georg Krempl, Indre Žliobaite, Dariusz Brzezinski, Eyke Hüllermeier, Mark Last, Vincent Lemaire, ´ Tino Noack, Ammar Shaker, Sonja Sievi, Myra Spiliopoulou, et al. Open challenges for data stream mining research. KDD, 16(1):1–10, 2014.   
Alex Krizhevsky, Geoffrey Hinton, et al. Learning multiple layers of features from tiny images. Technical report, 2009.   
Sang-Woo Lee, Jin-Hwa Kim, Jaehyun Jun, Jung-Woo Ha, and Byoung-Tak Zhang. Overcoming catastrophic forgetting by incremental moment matching. NIPS, 30:4652–4662, 2017.   
Zhizhong Li and Derek Hoiem. Learning without forgetting. TPAMI, 40(12):2935–2947, 2017.   
Zhuoyun Li, Changhong Zhong, Sijia Liu, Ruixuan Wang, and Wei-Shi Zheng. Preserving earlier knowledge in continual learning with the help of all previous feature extractors. arXiv preprint arXiv:2104.13614, 2021.

Yaoyao Liu, Yuting Su, An-An Liu, Bernt Schiele, and Qianru Sun. Mnemonics training: Multi-class incremental learning without forgetting. In CVPR, pp. 12245–12254, 2020.   
Yaoyao Liu, Bernt Schiele, and Qianru Sun. Adaptive aggregation networks for class-incremental learning. In CVPR, pp. 2544–2553, 2021a.   
Yaoyao Liu, Bernt Schiele, and Qianru Sun. Rmm: Reinforced memory management for classincremental learning. NeurIPS, 34, 2021b.   
Yaoyao Liu, Yingying Li, Bernt Schiele, and Qianru Sun. Online hyperparameter optimization for class-incremental learning. arXiv preprint arXiv:2301.05032, 2023.   
Raphael Gontijo Lopes, Stefano Fenu, and Thad Starner. Data-free knowledge distillation for deep neural networks. arXiv preprint arXiv:1710.07535, 2017.   
David Lopez-Paz and Marc’Aurelio Ranzato. Gradient episodic memory for continual learning. In NeurIPS, pp. 6467–6476, 2017.   
Hartmut Maennel, Ibrahim M Alabdulmohsin, Ilya O Tolstikhin, Robert Baldock, Olivier Bousquet, Sylvain Gelly, and Daniel Keysers. What do neural networks learn when trained with random labels? NeurIPS, 33:19693–19704, 2020.   
Jingyi Ning, Lei Xie, Chuyu Wang, Yanling Bu, Fengyuan Xu, Da-Wei Zhou, Sanglu Lu, and Baoliu Ye. Rf-badge: Vital sign-based authentication via rfid tag array on badges. IEEE Transactions on Mobile Computing, 2021.   
Oleksiy Ostapenko, Pau Rodriguez, Massimo Caccia, and Laurent Charlin. Continual learning via local module composition. NeurIPS, 34:30298–30312, 2021.   
German I Parisi, Ronald Kemker, Jose L Part, Christopher Kanan, and Stefan Wermter. Continual lifelong learning with neural networks: A review. Neural Networks, 113:54–71, 2019.   
Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, et al. Pytorch: An imperative style, high-performance deep learning library. In NeurIPS, pp. 8026–8037, 2019.   
Mozhgan PourKeshavarzi, Guoying Zhao, and Mohammad Sabokrou. Looking back on learned experiences for class/task incremental learning. In ICLR, 2022.   
Jathushan Rajasegaran, Munawar Hayat, Salman Khan, Fahad Shahbaz Khan, and Ling Shao. Random path selection for incremental learning. NeurIPS, 3, 2019.   
Sylvestre-Alvise Rebuffi, Alexander Kolesnikov, Georg Sperl, and Christoph H Lampert. icarl: Incremental classifier and representation learning. In CVPR, pp. 2001–2010, 2017.   
David Rolnick, Arun Ahuja, Jonathan Schwarz, Timothy P Lillicrap, and Greg Wayne. Experience replay for continual learning. In NeurIPS, pp. 350–360, 2019.   
Andrei A Rusu, Neil C Rabinowitz, Guillaume Desjardins, Hubert Soyer, James Kirkpatrick, Koray Kavukcuoglu, Razvan Pascanu, and Raia Hadsell. Progressive neural networks. arXiv preprint arXiv:1606.04671, 2016.   
Tara N Sainath, Brian Kingsbury, Vikas Sindhwani, Ebru Arisoy, and Bhuvana Ramabhadran. Lowrank matrix factorization for deep neural network training with high-dimensional output targets. In ICASSP, pp. 6655–6659. IEEE, 2013.   
Joan Serra, Didac Suris, Marius Miron, and Alexandros Karatzoglou. Overcoming catastrophic forgetting with hard attention to the task. In ICML, pp. 4548–4557. PMLR, 2018.   
Hanul Shin, Jung Kwon Lee, Jaehong Kim, and Jiwon Kim. Continual learning with deep generative replay. In NeurIPS, pp. 2990–2999, 2017a.   
Hanul Shin, Jung Kwon Lee, Jaehong Kim, and Jiwon Kim. Continual learning with deep generative replay. NIPS, 30, 2017b.

Karen Simonyan and Andrew Zisserman. Very deep convolutional networks for large-scale image recognition. arXiv preprint arXiv:1409.1556, 2014.   
James Smith, Yen-Chang Hsu, Jonathan Balloch, Yilin Shen, Hongxia Jin, and Zsolt Kira. Always be dreaming: A new approach for data-free class-incremental learning. In ICCV, pp. 9374–9384, 2021.   
Qianru Sun, Yaoyao Liu, Tat-Seng Chua, and Bernt Schiele. Meta-transfer learning for few-shot learning. In CVPR, pp. 403–412, 2019.   
Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jon Shlens, and Zbigniew Wojna. Rethinking the inception architecture for computer vision. In CVPR, pp. 2818–2826, 2016.   
Laurens Van der Maaten and Geoffrey Hinton. Visualizing data using t-sne. JMLR, 9(11), 2008.   
Fu-Yun Wang, Da-Wei Zhou, Han-Jia Ye, and De-Chuan Zhan. Foster: Feature boosting and compression for class-incremental learning. arXiv preprint arXiv:2204.04662, 2022.   
Jian Wang, Feng Zhou, Shilei Wen, Xiao Liu, and Yuanqing Lin. Deep metric learning with angular loss. In ICCV, pp. 2593–2601, 2017.   
Max Welling. Herding dynamical weights to learn. In ICML, pp. 1121–1128, 2009.   
Tz-Ying Wu, Gurumurthy Swaminathan, Zhizhong Li, Avinash Ravichandran, Nuno Vasconcelos, Rahul Bhotika, and Stefano Soatto. Class-incremental learning with strong pre-trained models. In CVPR, pp. 9601–9610, 2022.   
Yue Wu, Yinpeng Chen, Lijuan Wang, Yuancheng Ye, Zicheng Liu, Yandong Guo, and Yun Fu. Large scale incremental learning. In CVPR, pp. 374–382, 2019.   
Ju Xu and Zhanxing Zhu. Reinforced continual learning. In NeurIPS, pp. 899–908, 2018.   
Shipeng Yan, Jiangwei Xie, and Xuming He. Der: Dynamically expandable representation for class incremental learning. In CVPR, pp. 3014–3023, 2021.   
Jiwei Yang, Xu Shen, Jun Xing, Xinmei Tian, Houqiang Li, Bing Deng, Jianqiang Huang, and Xian-sheng Hua. Quantization networks. In CVPR, pp. 7308–7316, 2019.   
Jaehong Yoon, Eunho Yang, Jeongtae Lee, and Sung Ju Hwang. Lifelong learning with dynamically expandable networks. In ICLR, 2018.   
Jason Yosinski, Jeff Clune, Yoshua Bengio, and Hod Lipson. How transferable are features in deep neural networks? NIPS, 27, 2014.   
Lu Yu, Bartlomiej Twardowski, Xialei Liu, Luis Herranz, Kai Wang, Yongmei Cheng, Shangling Jui, and Joost van de Weijer. Semantic drift compensation for class-incremental learning. In CVPR, pp. 6982–6991, 2020.   
Qing Yu and Kiyoharu Aizawa. Unsupervised out-of-distribution detection by maximum classifier discrepancy. In ICCV, pp. 9518–9526, 2019.   
Chiyuan Zhang, Samy Bengio, and Yoram Singer. Are all layers created equal? arXiv preprint arXiv:1902.01996, 2019.   
Bowen Zhao, Xi Xiao, Guojun Gan, Bin Zhang, and Shu-Tao Xia. Maintaining discrimination and fairness in class incremental learning. In CVPR, pp. 13208–13217, 2020.   
Hanbin Zhao, Yongjian Fu, Mintong Kang, Qi Tian, Fei Wu, and Xi Li. Mgsvf: Multi-grained slow vs. fast framework for few-shot class-incremental learning. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2021a.   
Hanbin Zhao, Xin Qin, Shihao Su, Yongjian Fu, Zibo Lin, and Xi Li. When video classification meets incremental classes. In ACM MM, pp. 880–889, 2021b.

Hanbin Zhao, Hui Wang, Yongjian Fu, Fei Wu, and Xi Li. Memory efficient class-incremental learning for image classification. IEEE Transactions on Neural Networks and Learning Systems, 2021c.   
Da-Wei Zhou, Fu-Yun Wang, Han-Jia Ye, and De-Chuan Zhan. Pycil: A python toolbox for classincremental learning. arXiv preprint arXiv:2112.12533, 2021a.   
Da-Wei Zhou, Han-Jia Ye, and De-Chuan Zhan. Co-transport for class-incremental learning. In ACM MM, pp. 1645–1654, 2021b.   
Da-Wei Zhou, Fu-Yun Wang, Han-Jia Ye, Liang Ma, Shiliang Pu, and De-Chuan Zhan. Forward compatible few-shot class-incremental learning. In CVPR, pp. 9046–9056, 2022a.   
Da-Wei Zhou, Han-Jia Ye, Liang Ma, Di Xie, Shiliang Pu, and De-Chuan Zhan. Few-shot classincremental learning by sampling multi-phase tasks. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2022b.   
Da-Wei Zhou, Qi-Wei Wang, Zhi-Hong Qi, Han-Jia Ye, De-Chuan Zhan, and Ziwei Liu. Deep class-incremental learning: A survey. arXiv preprint arXiv:2302.03648, 2023.   
Zhi-Hua Zhou and Yuan Jiang. Nec4. 5: neural ensemble based c4. 5. IEEE Transactions on knowledge and data engineering, 16(6):770–773, 2004.   
Zhi-Hua Zhou, Yuan Jiang, and Shi-Fu Chen. Extracting symbolic rules from trained neural network ensembles. Ai Communications, 16(1):3–15, 2003.

# Supplementary Material

Class-incremental learning (CIL) is of great importance to the machine learning community. In the main paper, we answer two questions in CIL. The first is about how to fairly compare different methods, and we achieve this goal by aligning the memory cost. The second is about organizing the model with memory efficiency, and our proposed MEMO maintains the diverse feature representations with a modest memory cost. In the supplementary, we report more details about the experimental results mentioned in the main paper. We also provide more empirical evaluations and discussions. The supplementary material is organized according to the two questions above — we first supply details to fairly compare different methods and then discuss how to manage the model in a memory-efficient manner. Afterward, we give the additional experimental and implementation details.

• Section A reports the implementation details of the models and exemplars in the performancememory curve of the main paper, and numerical results in the benchmark comparison;   
• Section B discusses the variations of MEMO, including the definition of specialized and generalized blocks and other deep network structures;   
• Section C provides extra illustrative experimental evaluations that cannot be included in the main paper due to page limit, including the last accuracy-memory curve, gradient norms for all tasks, CKA visualizations of different blocks, the ablations about which layer to freeze, running time comparison, and CIL performance with multiple runs;   
• Section D holistically discusses the implementations of related work and ours, the choice of compared methods, and broader impacts.

# A IMPLEMENTATION DETAILS OF PERFORMANCE-MEMORY CURVE

We give the performance-memory curve in the main paper as one main contribution to fairly comparing different CIL methods. In this section, we give the detailed implementations of each point on the X coordinate. We will start with CIFAR100 (Krizhevsky et al., 2009), and then discuss ImageNet100 (Deng et al., 2009).

In the following discussions, we use E to represent the exemplar set. |E| denotes the number of exemplars, and S(E) represents the memory size (in MB) that saving these exemplars consume. Following the benchmark implementation (Rebuffi et al., 2017), 2,000 exemplars are saved for every method for CIFAR100 and ImageNet100. Hence, the exemplar size of each method is denoted as |E| = 2000 + E, where E corresponds to the extra exemplars exchanged from the model size, as discussed in the main paper. We use ‘# Parameters’ to represent the number of parameters and ‘Model Size’ to represent the memory budget (in MB) it costs to save this model in memory. The total memory size (i.e., numbers on the X coordinate) is the sum of exemplars and the models.

Since iCaRL (Rebuffi et al., 2017), Replay (Chaudhry et al., 2019) and WA (Zhao et al., 2020) are typical exemplar-based methods, they use the same network backbone with the same model size. Hence, they have equal memory sizes. DER (Yan et al., 2021) sacrifices the memory size to store the backbone from history, and it has the least exemplars. Compared to DER, MEMO does not keep the duplicated generalized blocks from history and saves much memory size to change into exemplars.

In the following discussions, we first give the tables to illustrate the implementation of different methods and report their incremental performance with figures. We report the improvement of MEMO against the runner-up method at the end of each line in the figures and analyze the empirical evaluations after the tables and figures.

# A.1 IMPLEMENTATIONS OF CIFAR100

There are five X coordinates in the curve of CIFAR100, e.g., 7.6, 12.4, 16.0, 19.8, and 23.5 MB. Following, we show the detailed implementation of different methods at these scales.

Table 2: Implementation details when memory size= 7.6 MB   

<table><tr><td>7.6MB</td><td>|E|</td><td>S(E)</td><td>Model Type #</td><td>Parameters</td><td>Model Size</td></tr><tr><td>Replay</td><td>2000</td><td>5.85MB</td><td>ResNet32</td><td>0.46M</td><td>1.76MB</td></tr><tr><td>iCaRL</td><td>2000</td><td>5.85MB</td><td>ResNet32</td><td>0.46M</td><td>1.76MB</td></tr><tr><td>WA</td><td>2000</td><td>5.85MB</td><td>ResNet32</td><td>0.46M</td><td>1.76MB</td></tr><tr><td>DER</td><td>2096</td><td>6.14MB</td><td>ConvNet2</td><td>0.38M</td><td>1.48MB</td></tr><tr><td>MEMO</td><td>2118</td><td>6.20MB</td><td>ConvNet2</td><td>0.37M</td><td>1.42MB</td></tr></table>

![](images/88cf21e8c9d43d7645b631e4c427ec23e0848a1586c668a6d30dfe5ee26eb222.jpg)  
Figure 8: CIL performance

CIFAR100 with 7.6 MB Memory Size: The implementations are shown in Table 2 and Figure 8. 7.6 MB is a relatively small memory size. Since we need to align the total budget of these methods, we are only able to use small backbones for DER and MEMO. These small backbones, i.e., ConvNet with two convolutional layers, has much fewer parameters than ResNet32, and saving 10 ConvNets matches the memory size of a single ResNet32 (1.48MB versus 1.76MB). We can infer from the table that DER and MEMO are restricted by the learning ability of the inferior backbones, which perform poorly in the base session. These results are consistent with the conclusions in the main paper that model-based methods are inferior to exemplar-based methods with a small memory budget.

Table 3: Implementation details when memory size= 12.4 MB   

<table><tr><td>12.4MB</td><td>|E|</td><td>S(E)</td><td>Model Type #</td><td>Parameters</td><td>Model Size</td></tr><tr><td>Replay</td><td>3634</td><td>10.64MB</td><td>ResNet32</td><td>0.46M</td><td>1.76MB</td></tr><tr><td>iCaRL</td><td>3634</td><td>10.64MB</td><td>ResNet32</td><td>0.46M</td><td>1.76MB</td></tr><tr><td>WA</td><td>3634</td><td>10.64MB</td><td>ResNet32</td><td>0.46M</td><td>1.76MB</td></tr><tr><td>DER</td><td>2000</td><td>5.85MB</td><td>ResNet14</td><td>1.70M</td><td>6.55MB</td></tr><tr><td>MEMO</td><td>2495</td><td>7.32MB</td><td>ResNet14</td><td>1.33M</td><td>5.10MB</td></tr></table>

![](images/dfd9e125db0dc41f2eff7d512a86440e4ce715c8663db41c730d5454987e44f2.jpg)  
Figure 9: CIL performance

CIFAR100 with 12.4 MB Memory Size: The implementations are shown in Table 3 and Figure 9. By raising the total memory cost to 12.4 MB, exemplar-based methods can utilize the extra memory size to exchange 1634 exemplars, and model-based methods can switch to more powerful backbones to get better representation ability. We use ResNet14 for DER and MEMO in this setting. We can infer that model-based methods show competitive results with stronger backbones and outperform exemplar-based methods in this setting. These results are consistent with the conclusions in the main paper that the intersection between these two groups of methods exists near the start point.

Table 4: Implementation details when memory size= 16.0 MB   

<table><tr><td>16.0MB</td><td>|E|</td><td>S(E)</td><td>Model Type #</td><td>Parameters</td><td>Model Size</td></tr><tr><td>Replay</td><td>4900</td><td>14.3MB</td><td>ResNet32</td><td>0.46M</td><td>1.76MB</td></tr><tr><td>iCaRL</td><td>4900</td><td>14.3MB</td><td>ResNet32</td><td>0.46M</td><td>1.76MB</td></tr><tr><td>WA</td><td>4900</td><td>14.3MB</td><td>ResNet32</td><td>0.46M</td><td>1.76MB</td></tr><tr><td>DER</td><td>2000</td><td>5.85MB</td><td>ResNet20</td><td>2.69M</td><td>10.2MB</td></tr><tr><td>MEMO</td><td>2768</td><td>8.10MB</td><td>ResNet20</td><td>2.1M</td><td>8.01MB</td></tr></table>

![](images/1fb800fea6a4f719c56df6ad11f6faeee9871b30a8870737e7c24d3d95ffb04a.jpg)  
Figure 10: CIL performance

CIFAR100 with 16.0 MB Memory Size: The implementations are shown in Table 4 and Figure 10. By raising the total memory cost to 16.0 MB, exemplar-based methods can utilize the extra memory size to exchange 2900 exemplars, and model-based methods can switch to larger backbones to get better representation ability. We use ResNet20 for DER and MEMO in this setting. The results are consistent with the former setting, where we can infer that model-based methods show competitive results with stronger backbones and outperform exemplar-based methods.

Table 5: Implementation details when memory size= 19.8 MB   

<table><tr><td>19.8MB</td><td>|E|</td><td>S(E)</td><td>Model Type #</td><td>Parameters</td><td>Model Size</td></tr><tr><td>Replay</td><td>6165</td><td>18.06MB</td><td>ResNet32</td><td>0.46M</td><td>1.76MB</td></tr><tr><td>iCaRL</td><td>6165</td><td>18.06MB</td><td>ResNet32</td><td>0.46M</td><td>1.76MB</td></tr><tr><td>WA</td><td>6165</td><td>18.06MB</td><td>ResNet32</td><td>0.46M</td><td>1.76MB</td></tr><tr><td>DER</td><td>2000</td><td>5.85MB</td><td>ResNet26</td><td>3.60M</td><td>13.9MB</td></tr><tr><td>MEMO</td><td>3040</td><td>8.91MB</td><td>ResNet26</td><td>2.86M</td><td>10.92MB</td></tr></table>

![](images/0b5e1d5ef3bf70df19951929b327382f46de2e24f20b9ed86d73f689e83039b9.jpg)  
Figure 11: CIL performance

CIFAR100 with 19.8 MB Memory Size: The implementations are shown in Table 5 and Figure 11. By raising the total memory cost to 19.8 MB, exemplar-based methods can utilize the extra memory size to exchange 4165 exemplars, and model-based methods can switch to larger backbones to get better representation ability. We use ResNet26 for DER and MEMO in this setting. The results are consistent with the former setting, where we can infer that model-based methods show competitive results with stronger backbones and outperform exemplar-based methods.

Table 6: Implementation details when memory size= 23.5 MB   

<table><tr><td>23.5MB</td><td>|E|</td><td>S(E)</td><td>Model Type #</td><td>Parameters</td><td>Model Size</td></tr><tr><td>Replay</td><td>7431</td><td>21.76MB</td><td>ResNet32</td><td>0.46M</td><td>1.75MB</td></tr><tr><td>iCaRL</td><td>7431</td><td>21.76MB</td><td>ResNet32</td><td>0.46M</td><td>1.75MB</td></tr><tr><td>WA</td><td>7431</td><td>21.76MB</td><td>ResNet32</td><td>0.46M</td><td>1.75MB</td></tr><tr><td>DER</td><td>2000</td><td>5.86MB</td><td>ResNet32</td><td>4.63M</td><td>17.68MB</td></tr><tr><td>MEMO</td><td>3312</td><td>9.7MB</td><td>ResNet32</td><td>3.62M</td><td>13.83MB</td></tr></table>

![](images/f5076c08eca07898e4f44bc8d40b51ac5552b9545d91805bf7d209276311a40d.jpg)  
Figure 12: CIL performance

CIFAR100 with 23.5 MB Memory Size: The implementations are shown in Table 6 and Figure 12. By raising the total memory cost to 23.5 MB, exemplar-based methods can utilize the extra memory size to exchange 5431 exemplars, and model-based methods can switch to larger backbones to get better representation ability. We use ResNet32 for DER and MEMO in this setting. The results are consistent with the conclusions in Section 5.1. Model-based methods are better than exemplar-based methods with large memory sizes, but the performance gap is not so large as reported in (Yan et al., 2021) when fairly compared.

To summarize, we conduct fair comparisons for exemplar-based and model-based methods by varying the memory size from small to large. Results indicate that exemplar-based methods are competitive with small memory sizes, while model-based methods are competitive with large ones. Our proposed MEMO obtains the best performance in most cases in these settings.

# A.2 IMPLEMENTATIONS OF IMAGENET100

Similar to CIFAR100, we can conduct an exchange between the model and exemplars on ImageNet100. For example, saving a ResNet18 model costs 11, 176, 512 parameters (float), while saving an ImageNet image costs 3 × 224 × 224 integer numbers (int). The budget of saving a backbone is equal to saving 11, 176, 512 floats ×4 bytes/float $\div ( 3 \times 2 2 4 \times 2 2 4 )$ bytes/image ≈ 297 images for ImageNet. We conduct the experiment with ImageNet100, Base50 Inc5, as discussed in the main paper. There are six X coordinates in the curve of ImageNet100, e.g., 329, 493, 755, 872, 1180 and 1273 MB. Following, we show the detailed implementation of different methods at these scales.

Table 7: Implementation details when memory size=329MB   

<table><tr><td>329MB</td><td>|E|</td><td>S(E)</td><td>Model Type #</td><td>Parameters</td><td>Model Size</td></tr><tr><td>Replay</td><td>2000</td><td>287MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>iCaRL</td><td>2000</td><td>287MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>WA</td><td>2000</td><td>287MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>DER</td><td>2032</td><td>291MB</td><td>ConvNet4</td><td>9.96M</td><td>38.0MB</td></tr><tr><td>MEMO</td><td>2115</td><td>303MB</td><td>ConvNet4</td><td>6.81M</td><td>26.0MB</td></tr></table>

![](images/cd98c779c0d1ea54c5cb16ca79e8d420b6664e1303268d41a9901648e18c07e4.jpg)  
Figure 13: CIL performance

ImageNet100 with 329 MB Memory Size: The implementations are shown in Table 7 and Figure 13. 329 MB is a relatively small memory size. Since we need to align the total budget of these methods, we are only able to use small backbones for DER and MEMO. These small backbones, i.e., ConvNet with four convolutional layers, has much fewer parameters than ResNet18, and saving 10 ConvNets matches the memory size of a single ResNet18. We can infer from the table that DER and MEMO are restricted by the learning ability of the inferior backbones, which perform poorly in the base session. However, our proposed MEMO outperforms these better backbones by saving the ‘unforgettable checkpoints,’ which obtains the best last accuracy and average accuracy in this case.

Table 8: Implementation details when memory size=493MB   

<table><tr><td>493MB</td><td>|E|</td><td>S(E)</td><td>Model Type #</td><td>Parameters</td><td>Model Size</td></tr><tr><td>Replay</td><td>3136</td><td>450MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>iCaRL</td><td>3136</td><td>450MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>WA</td><td>3136</td><td>450MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>DER</td><td>2000</td><td>287MB</td><td>ResNet10</td><td>53.96M</td><td>205MB</td></tr><tr><td>MEMO</td><td>2327</td><td>334MB</td><td>ResNet10</td><td>41.63M</td><td>158MB</td></tr></table>

![](images/16de14db66b5bb5ad9720792b2bc22fcea0c25f0edb0e1cf15145359e51cd9a8.jpg)  
Figure 14: CIL performance

ImageNet100 with 493 MB Memory Size: The implementations are shown in Table 8 and Figure 14. By raising the total memory cost to 493 MB, exemplar-based methods can utilize the extra memory size to exchange 1136 exemplars, and model-based methods can switch to larger backbones to get better representation ability. We use ResNet10 for DER and MEMO in this setting. We can infer from the figure that model-based methods show competitive results with stronger backbones and outperform exemplar-based methods in this setting.

Table 9: Implementation details when memory size=755MB   

<table><tr><td>755MB</td><td>|E|</td><td>S(E)</td><td>Model Type #</td><td>Parameters</td><td>Model Size</td></tr><tr><td>Replay</td><td>4970</td><td>713.5MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>iCaRL</td><td>4970</td><td>713.5MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>WA</td><td>4970</td><td>713.5MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>DER</td><td>2000</td><td>287MB</td><td>ResNet18</td><td>122.9M</td><td>468MB</td></tr><tr><td>MEMO</td><td>2739</td><td>393.2MB</td><td>ResNet18</td><td>95.11M</td><td>362.8MB</td></tr></table>

![](images/e1a29eb1c035436d6271cebd61f88f9dc0a3e4736a44e1589ce0c0992a0a8abf.jpg)  
Figure 15: CIL performance

ImageNet100 with 755 MB Memory Size: The implementations are shown in Table 9 and Figure 15. By raising the total memory cost to 755 MB, exemplar-based methods can utilize the extra memory size to exchange 2970 exemplars, and model-based methods can switch to larger backbones to get better representation ability. We use ResNet18 for DER and MEMO in this setting. The results are consistent with the former setting, where we can infer that model-based methods show competitive results with stronger backbones and outperform exemplar-based methods.

Table 10: Implementation details when memory size=872MB   

<table><tr><td>872MB</td><td>|E|</td><td>S(E)</td><td>Model Type #</td><td>Parameters</td><td>Model Size</td></tr><tr><td>Replay</td><td>5779</td><td>829MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>iCaRL</td><td>5779</td><td>829MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>WA</td><td>5779</td><td>829MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>DER</td><td>2000</td><td>287MB</td><td>ResNet26</td><td>153.4M</td><td>585.2MB</td></tr><tr><td>MEMO</td><td>2915</td><td>417MB</td><td>ResNet26</td><td>119.0M</td><td>453MB</td></tr></table>

![](images/d65aebce65c7b516296cc759f72ddc70140ea9bd153eede52330240e1607c275.jpg)  
Figure 16: CIL performance

ImageNet100 with 872 MB Memory Size: The implementations are shown in Table 10 and Figure 16. By raising the total memory cost to 872 MB, exemplar-based methods can utilize the extra memory size to exchange 3779 exemplars, and model-based methods can switch to larger backbones for better representation ability. We use ResNet26 for DER and MEMO in this setting.

Table 11: Implementation details when memory size=1180MB   

<table><tr><td>1180MB</td><td>|E|</td><td>S(E)</td><td>Model Type #</td><td>Parameters</td><td>Model Size</td></tr><tr><td>Replay</td><td>7924</td><td>1137MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>iCaRL</td><td>7924</td><td>1137MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>WA</td><td>7924</td><td>1137MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>DER</td><td>2000</td><td>287MB</td><td>ResNet34</td><td>234.1M</td><td>893MB</td></tr><tr><td>MEMO</td><td>4170</td><td>598MB</td><td>ResNet34</td><td>152.4M</td><td>581MB</td></tr></table>

![](images/f9b585d134199185d0a03fc8ab80829258cc390128ceefc3c25a72d5db16c979.jpg)  
Figure 17: CIL performance

ImageNet100 with 1180 MB Memory Size: The implementations are shown in Table 11 and Figure 17. By raising the total memory cost to 1180 MB, exemplar-based methods can utilize the extra memory size to exchange 5924 exemplars, and model-based methods can switch to larger backbones to get better representation ability. We use ResNet34 for DER and MEMO in this setting.

Table 12: Implementation details when memory size=1273MB   

<table><tr><td>1273MB</td><td>|E|</td><td>S(E)</td><td>Model Type #</td><td>Parameters</td><td>Model Size</td></tr><tr><td>Replay</td><td>8574</td><td>1230MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>iCaRL</td><td>8574</td><td>1230MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>WA</td><td>8574</td><td>1230MB</td><td>ResNet18</td><td>11.17M</td><td>42.6MB</td></tr><tr><td>DER</td><td>2000</td><td>287MB</td><td>ResNet50</td><td>258.6M</td><td>986MB</td></tr><tr><td>MEMO</td><td>4270</td><td>612MB</td><td>ResNet50</td><td>173.2M</td><td>660MB</td></tr></table>

![](images/8d27170a9e40cebba1bf41b9f6b69e86248c1114d10879e3f9a886e875726667.jpg)  
Figure 18: CIL performance

ImageNet100 with 1273 MB Memory Size: The implementations are shown in Table 12 and Figure 18. By raising the total memory cost to 1273 MB, exemplar-based methods can utilize the extra memory size to exchange 6574 exemplars, and model-based methods can switch to larger backbones to get better representation ability. We use ResNet50 for DER and MEMO in this setting. The results are consistent with the conclusions in Section 5.1. Model-based methods are better than exemplar-based methods with large memory sizes, but the performance gap is not so large as reported in (Yan et al., 2021) when fairly compared.

Discussion about Backbones: It should be noted that ResNet18 is the benchmark backbone for ImageNet, and the memory size for 872, 1180, and 1273 MB are larger than the benchmark setting. We conduct these experiments for two reasons. First, handling large-scale image inputs require more convolutional layers, and it is hard to find typical models with small memory budgets. Second, we would like to investigate the performance when the model is large enough to see whether the improvement of stronger backbones will converge, and the results successfully verify our assumptions.

To summarize, we conduct fair comparisons for exemplar-based and model-based methods by varying the memory size from small to large. Results indicate that exemplar-based methods are competitive with small memory sizes, while model-based methods are competitive with large ones. Our proposed MEMO obtains the best performance in most cases in these settings.

# A.3 NUMERICAL RESULTS AND CONFIGURATIONS FOR SECTION 5.1

In this section, we give the numerical incremental performance of different methods and configurations in Section 5.1. We first list the incremental and average accuracy in Table 13, 14, 15, 16,17, 18, and give the setting in Table 19, 20, 21, 22, 23, 24.

As we discussed in the main paper, a fair comparison among different methods should be aligned to the same memory budget. Since DER (Yan et al., 2021) requires saving multiple backbones, training DER requires the largest memory budget. Hence, we align the budget of other methods to DER (as shown in Table 19, 20, 21, 22, 23, 24) by saving more exemplars for them.

Table 13: Incremental and average accuracy comparison of different methods under CIFAR100 Base0 Inc5 setting.   

<table><tr><td>Method</td><td colspan="16376">Accuracy in each session (%) ↑</td></tr></table>

Table 14: Incremental and average accuracy comparison of different methods under CIFAR100 Base0 Inc10 setting.   

<table><tr><td rowspan="2">Method</td><td colspan="11">Accuracy in each session (%)↑</td><td>Average</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td></td><td></td></tr><tr><td>Replay</td><td>90.40</td><td>79.90</td><td>79.20</td><td>74.08</td><td>70.32</td><td>67.03</td><td>64.76</td><td>60.31</td><td>58.14</td><td>55.61</td><td>69.98</td><td></td></tr><tr><td>iCaRL</td><td>90.40</td><td>80.25</td><td>78.00</td><td>72.80</td><td>70.88</td><td>68.88</td><td>66.37</td><td>62.82</td><td>60.51</td><td>58.52</td><td>70.94</td><td></td></tr><tr><td>WA</td><td>90.40</td><td>76.65</td><td>74.57</td><td>70.92</td><td>69.20</td><td>66.48</td><td>65.24</td><td>62.41</td><td>60.37</td><td>59.26</td><td>69.55</td><td></td></tr><tr><td>DER</td><td>90.40</td><td>80.55</td><td>77.37</td><td>73.47</td><td>70.78</td><td>68.38</td><td>67.43</td><td>64.22</td><td>61.93</td><td>60.26</td><td>71.47</td><td></td></tr><tr><td>MEMO</td><td>90.40</td><td>80.30</td><td>78.33</td><td>74.65</td><td>71.74</td><td>69.67</td><td>68.19</td><td>65.34</td><td>63.10</td><td>61.98</td><td>72.37</td><td></td></tr></table>

Table 15: Incremental and average accuracy comparison of different methods under CIFAR100 Base50 Inc5 setting.   

<table><tr><td rowspan="2">Method</td><td colspan="12">Accuracy in each session (%)↑</td><td>Average</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td></td><td></td></tr><tr><td>Replay</td><td>76.32</td><td>68.96</td><td>67.60</td><td>65.55</td><td>65.34</td><td>63.84</td><td>60.86</td><td>59.39</td><td>58.12</td><td>56.93</td><td>56.20</td><td>63.55</td><td></td></tr><tr><td>iCaRL</td><td>76.32</td><td>70.00</td><td>69.28</td><td>67.38</td><td>67.00</td><td>65.45</td><td>63.55</td><td>60.95</td><td>60.47</td><td>59.31</td><td>58.37</td><td>65.28</td><td></td></tr><tr><td>WA</td><td>76.32</td><td>70.09</td><td>68.58</td><td>67.54</td><td>67.04</td><td>65.52</td><td>64.24</td><td>62.49</td><td>62.00</td><td>61.21</td><td>60.49</td><td>65.95</td><td></td></tr><tr><td>DER</td><td>76.32</td><td>74.71</td><td>72.15</td><td>70.92</td><td>69.54</td><td>68.03</td><td>65.26</td><td>63.00</td><td>61.80</td><td>61.73</td><td>59.84</td><td>67.57</td><td></td></tr><tr><td>MEMO</td><td>76.32</td><td>74.05</td><td>72.77</td><td>71.28</td><td>70.93</td><td>69.29</td><td>67.38</td><td>65.88</td><td>64.36</td><td>64.29</td><td>63.36</td><td>69.08</td><td></td></tr></table>

Table 16: Incremental and average accuracy comparison of different methods under CIFAR100 Base50 Inc10 setting.   

<table><tr><td rowspan="2">Method</td><td colspan="6">Accuracy in each session (%)↑</td><td rowspan="2">Average</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Replay</td><td>76.32</td><td>64.57</td><td>61.43</td><td>56.91</td><td>54.72</td><td>53.23</td><td>61.19</td></tr><tr><td>iCaRL</td><td>76.32</td><td>68.43</td><td>66.83</td><td>63.52</td><td>59.89</td><td>57.92</td><td>65.48</td></tr><tr><td>WA</td><td>76.32</td><td>71.25</td><td>69.30</td><td>64.79</td><td>62.37</td><td>60.62</td><td>67.44</td></tr><tr><td>DER</td><td>76.32</td><td>73.17</td><td>70.99</td><td>67.51</td><td>64.49</td><td>62.48</td><td>69.16</td></tr><tr><td>MEMO</td><td>76.32</td><td>74.37</td><td>71.87</td><td>68.50</td><td>65.81</td><td>63.66</td><td>70.09</td></tr></table>

Table 17: Incremental and average accuracy comparison of different methods under ImageNet100 Base50 Inc5 setting.   

<table><tr><td rowspan="2">Method</td><td colspan="12">Accuracy in each session (%)↑</td><td>Average</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td></td><td></td></tr><tr><td>Replay</td><td>84.44</td><td>66.76</td><td>64.10</td><td>61.26</td><td>59.00</td><td>58.67</td><td>58.40</td><td>56.56</td><td>56.67</td><td>54.36</td><td>51.30</td><td>61.04</td><td></td></tr><tr><td>iCaRL</td><td>84.44</td><td>73.27</td><td>69.70</td><td>67.29</td><td>65.46</td><td>62.80</td><td>63.55</td><td>61.53</td><td>60.36</td><td>59.26</td><td>57.30</td><td>65.90</td><td></td></tr><tr><td>WA</td><td>84.44</td><td>68.65</td><td>67.73</td><td>65.38</td><td>64.71</td><td>63.63</td><td>63.52</td><td>61.60</td><td>60.02</td><td>59.09</td><td>57.96</td><td>65.15</td><td></td></tr><tr><td>DER</td><td>84.44</td><td>82.22</td><td>81.30</td><td>78.22</td><td>77.03</td><td>75.23</td><td>74.10</td><td>74.14</td><td>72.11</td><td>71.07</td><td>70.26</td><td>76.37</td><td></td></tr><tr><td>MEMO</td><td>84.44</td><td>83.71</td><td>81.60</td><td>78.68</td><td>77.43</td><td>76.53</td><td>75.42</td><td>74.49</td><td>73.56</td><td>72.63</td><td>71.54</td><td>77.27</td><td></td></tr></table>

Table 18: Incremental and average accuracy comparison of different methods under ImageNet1000 Base0 Inc100 setting.   
Table 19: Configurations of different methods under CIFAR100 Base0 Inc5 setting.   

<table><tr><td rowspan="2">Method</td><td colspan="11">Accuracy in each session (%) ↑</td><td>Average</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td></td><td></td></tr><tr><td>Replay</td><td>83.16</td><td>73.47</td><td>64.72</td><td>59.93</td><td>54.05</td><td>50.78</td><td>46.91</td><td>44.24</td><td>41.22</td><td>39.40</td><td>55.78</td><td></td></tr><tr><td>iCaRL</td><td>81.16</td><td>74.56</td><td>67.63</td><td>61.98</td><td>57.03</td><td>53.15</td><td>49.72</td><td>47.07</td><td>43.88</td><td>41.30</td><td>57.94</td><td></td></tr><tr><td>WA</td><td>81.16</td><td>76.87</td><td>70.09</td><td>64.84</td><td>59.38</td><td>55.75</td><td>51.22</td><td>48.37</td><td>45.72</td><td>43.23</td><td>59.86</td><td></td></tr><tr><td>DER</td><td>83.16</td><td>78.64</td><td>74.21</td><td>71.44</td><td>68.13</td><td>65.80</td><td>62.9</td><td>61.21</td><td>59.84</td><td>58.30</td><td>68.36</td><td></td></tr><tr><td>MEMO</td><td>83.16</td><td>78.47</td><td>73.72</td><td>70.93</td><td>68.05</td><td>65.78</td><td>62.91</td><td>61.24</td><td>59.22</td><td>57.40</td><td>68.09</td><td></td></tr></table>

Table 20: Configurations of different methods under CIFAR100 Base0 Inc10 setting.   

<table><tr><td>41.22MB</td><td>|E|</td><td>S(E)</td><td>Model Type #</td><td>Parameters</td><td>Model Size</td></tr><tr><td>Replay</td><td>13466</td><td>39.47MB</td><td>ResNet32</td><td>0.46M</td><td>1.75MB</td></tr><tr><td>iCaRL</td><td>13466</td><td>39.47MB</td><td>ResNet32</td><td>0.46M</td><td>1.75MB</td></tr><tr><td>WA</td><td>13466</td><td>39.47MB</td><td>ResNet32</td><td>0.46M</td><td>1.75MB</td></tr><tr><td>DER</td><td>2000</td><td>5.86MB</td><td>ResNet32</td><td>9.27M</td><td>35.36MB</td></tr><tr><td>MEMO</td><td>4771</td><td>13.98MB</td><td>ResNet32</td><td>7.14M</td><td>27.24MB</td></tr></table>

Table 21: Configurations of different methods under CIFAR100 Base50 Inc5 setting.   

<table><tr><td>23.5MB</td><td>|E|</td><td>S(E)</td><td>Model Type #</td><td>Parameters</td><td>Model Size</td></tr><tr><td>Replay</td><td>7431</td><td>21.76MB</td><td>ResNet32</td><td>0.46M</td><td>1.75MB</td></tr><tr><td>iCaRL</td><td>7431</td><td>21.76MB</td><td>ResNet32</td><td>0.46M</td><td>1.75MB</td></tr><tr><td>WA</td><td>7431</td><td>21.76MB</td><td>ResNet32</td><td>0.46M</td><td>1.75MB</td></tr><tr><td>DER</td><td>2000</td><td>5.86MB</td><td>ResNet32</td><td>4.63M</td><td>17.68MB</td></tr><tr><td>MEMO</td><td>3312</td><td>9.7MB</td><td>ResNet32</td><td>3.62M</td><td>13.83MB</td></tr></table>

<table><tr><td>25.3MB</td><td>|E|</td><td>S(E)</td><td>Model Type #</td><td>Parameters</td><td>Model Size</td></tr><tr><td>Replay</td><td>8035</td><td>23.53MB</td><td>ResNet32</td><td>0.46M</td><td>1.75MB</td></tr><tr><td>iCaRL</td><td>8035</td><td>23.53MB</td><td>ResNet32</td><td>0.46M</td><td>1.75MB</td></tr><tr><td>WA</td><td>8035</td><td>23.53MB</td><td>ResNet32</td><td>0.46M</td><td>1.75MB</td></tr><tr><td>DER</td><td>2000</td><td>5.86MB</td><td>ResNet32</td><td>5.1M</td><td>19.45MB</td></tr><tr><td>MEMO</td><td>3458</td><td>10.13MB</td><td>ResNet32</td><td>3.98M</td><td>15.17MB</td></tr></table>

Table 22: Configurations of different methods under CIFAR100 Base50 Inc10 setting.   
Table 23: Configurations of different methods under ImageNet100 Base50 Inc5 setting.   

<table><tr><td>16.45MB</td><td>|E|</td><td>S(E)</td><td>Model Type #</td><td>Parameters</td><td>Model Size</td></tr><tr><td>Replay</td><td>5017</td><td>14.7MB</td><td>ResNet32</td><td>0.46M</td><td>1.75MB</td></tr><tr><td>iCaRL</td><td>5017</td><td>14.7MB</td><td>ResNet32</td><td>0.46M</td><td>1.75MB</td></tr><tr><td>WA</td><td>5017</td><td>14.7MB</td><td>ResNet32</td><td>0.46M</td><td>1.75MB</td></tr><tr><td>DER</td><td>2000</td><td>5.86MB</td><td>ResNet32</td><td>2.78M</td><td>10.61MB</td></tr><tr><td>MEMO</td><td>2729</td><td>8.0MB</td><td>ResNet32</td><td>2.22M</td><td>8.45MB</td></tr></table>

Table 24: Configurations of different methods under ImageNet1000 Base0 Inc100 setting.   

<table><tr><td>756.1MB</td><td>|E|</td><td>S(E)</td><td>Model Type #</td><td>Parameters</td><td>Model Size</td></tr><tr><td>Replay</td><td>4970</td><td>713.47MB</td><td>ResNet18</td><td>11.17M</td><td>42.63MB</td></tr><tr><td>iCaRL</td><td>4970</td><td>713.47MB</td><td>ResNet18</td><td>11.17M</td><td>42.63MB</td></tr><tr><td>WA</td><td>4970</td><td>713.47MB</td><td>ResNet18</td><td>11.17M</td><td>42.63MB</td></tr><tr><td>DER</td><td>2000</td><td>287.1MB</td><td>ResNet18</td><td>122.94M</td><td>468.99MB</td></tr><tr><td>MEMO</td><td>2739</td><td>393.2MB</td><td>ResNet18</td><td>95.11M</td><td>362.83MB</td></tr></table>

<table><tr><td>3297MB</td><td>|E|</td><td>S(E)</td><td>Model Type #</td><td>Parameters</td><td>Model Size</td></tr><tr><td>Replay</td><td>22672</td><td>3254.67MB</td><td>ResNet18</td><td>11.17M</td><td>42.63MB</td></tr><tr><td>iCaRL</td><td>22672</td><td>3254.67MB</td><td>ResNet18</td><td>11.17M</td><td>42.63MB</td></tr><tr><td>WA</td><td>22672</td><td>3254.67MB</td><td>ResNet18</td><td>11.17M</td><td>42.63MB</td></tr><tr><td>DER</td><td>20000</td><td>2871MB</td><td>ResNet18</td><td>111.76M</td><td>426.35MB</td></tr><tr><td>MEMO</td><td>20666</td><td>2967MB</td><td>ResNet18</td><td>86.72M</td><td>330.81MB</td></tr></table>

# B VARIATIONS OF MEMO

In this section, we discuss the variations of MEMO , including the choice of specialized blocks and implementation with other backbones.

# B.1 HOW TO DEFINE THE SPECIALIZE AND GENERALIZE BLOCKS?

In the main paper, we observe the differences between shallow and deep layers in terms of gradient, MSE, and similarity. Hence, we decouple the network structure into deep and shallow layers and treat the deep layers as specialized blocks and the others as generalized ones. It is worth exploring how to decompose the model into specialized and generalized blocks. In this section, we conduct vast experiments to give the rule of thumb for defining the specialized and generalized blocks.

We first take ResNet32 as an example. There are three groups of residual blocks in ResNet32,2, i.e., residual blocks 1 ∼ 5 are encapsulated as group 1; residual blocks 6 ∼ 10 are encapsulated as group 2 and 11 ∼ 15 as group 3. We treat these groups as the minimal unit when decoupling the network.

Since there are only three groups of blocks in ResNet32, there are only two ways to decouple the network structure (cutoff after group 1 or 2). Therefore, we conduct experiments to compare the performance when treating the last group as the specialized block (as discussed in the main paper) and the last two groups as specialized blocks (denoted as MEMO-2). MEMO-2 extends two groups of

![](images/2c08b9adb2b9b236cd400b0734c6f65741d528b0c4de7cc83f80ce31a7816a0f.jpg)  
(a) ResNet32

![](images/cab854a5c13016ea593e01a11f100cdb5ee37e0c24dc02b271f4da53bc58c3bf.jpg)  
(b) ResNet18

![](images/5410249e982241a023cb577d3da44da7fcac5ec4226980917bf83c4c63487a44.jpg)  
(c) VGG8

![](images/845db6f8dd3e8ff0f7510a4800938b076a33ecf903f1483422cf88434ebf0fcb.jpg)  
(d) ResNet32, fine-grained decouple   
Figure 19: Experiments about the choice of specialized and generalized blocks. The digit after model name denotes the number of exemplars used during model training. Choosing the last block groups as specialized blocks is more memory-efficient.

residual blocks at a time, which consumes more memory budget than MEMO. We follow the same evaluation protocol as Section 5.1 in the main paper to compare under the CIFAR100 Base0 Inc10 setting, and report the results in Figure 19(a).

There are three lines in Figure 19(a), and the number of exemplars is shown in the legend. It is obvious that MEMO-2 uses more memory size than MEMO with the same exemplar size. Hence, we follow the description in the main paper and align the memory cost of MEMO to MEMO-2, and denote the method with aligned exemplars as MEMO, 3033. There are two main conclusions in this figure. Firstly, MEMO-2 has a little better performance than MEMO with the same exemplar size, which means extending more generalized blocks can improve the performance, although they are highly similar. But it should be noted that these methods are not fairly compared since MEMO-2 uses more model size than MEMO. Secondly, when aligning the memory cost of MEMO, 3033 to MEMO-2, we can infer that MEMO has better performance than MEMO-2, verifying that treating the last layer as specialized blocks is more memory-efficient. In other words, saving the generalized blocks per task is less efficient than saving exemplars of equal size.

We also explore the strategy with ResNet18 under the ImageNet100 Base50 Inc5 setting and report the results in Figure 19(b). Since there are four layers in ResNet18, we choose to decouple the network after the first, second, and third layers, resulting in MEMO-3, MEMO-2, and MEMO, respectively. Furthermore, we align the memory budget of different methods to MEMO-3 since it costs the largest budget. The ranking of different variations is the same as Figure 19(a), and we find treating the

![](images/c191bdf55e7c3b063c751502f5dcbd1bfb54a2ab1def46046d780e4ce2fb15e8.jpg)  
(a) VGG8

![](images/e57211a629903d05ca0742d63c47d9d034924048864bdfd58b01e864908151c6.jpg)  
(b) Inception-V3   
Figure 20: Experiments when varying the network structure. We evaluate MEMO and DER with VGG8 and Inception-V3 on ImageNet100. MEMO consistently outperforms DER with different network structures.

last group of blocks as the generalized block is more memory-efficient, which consistently shows the best performance. We also verify this conclusion regarding other backbone structures, i.e., VGGNet (Simonyan & Zisserman, 2014). There are five layers in it, and we follow the same protocol to conduct the experiments and show the results in Figure 19(c). Observing the results with different network structures and datasets, we empirically find that choosing the last layer as the specialized block is more memory-efficient.

Since the groups are combined with residual blocks, we can also decouple the network from the middle of the layers. Taking ResNet32 as an example, we can decouple the network after residual block 11, after residual block 12, etc. We also experiment following the former settings, and the results are shown in Figure 19(d). We denote the variation which decouples the network after the n-th residual block as MEMO-Bn. It implies that decoupling from the middle of the group is not a good choice. A probable reason is that the decoupling harms the inner characteristics of the residual groups, resulting in inferior performance. Hence, we do not conduct fine-grained model decoupling and treat the residual groups as the minimal unit in model decoupling.

To summarize, we suggest treating the last residual group in the network as specialized blocks when decoupling the layers, which is proven to be most memory-efficient among different network structures and datasets. This rule is consistent with the observations in Figure 3 that the last layer shifts more than others.

# B.2 MEMO WITH OTHER BACKBONES

As discussed in the main paper, our implementation is based on ResNet, but the concept of MEMO can be applied to any other deep network structure that relies on deep and shallow features. In this section, we conduct experiments with VGGNet (Simonyan & Zisserman, 2014) and Inception (Szegedy et al., 2016) on ImageNet100, and compare MEMO with DER with the same backbone. Results are shown in Figure 20. Other settings are the same as in the main paper.

We use VGG8 and Inception-V3 for implementation. VGG8 is a relatively small backbone, and we can exchange the extra model size of DER into 412 exemplars for MEMO. Inception V3 is much larger, and the additional number of exemplars is 2512 for Inception-V3. We can infer from these figures that MEMO shows consistent improvement over DER on these different network backbones, verifying that MEMO is a generalized protocol and can be applied to various kinds of CIL tasks with various network structures.

# C EXTRA EXPERIMENTAL EVALUATIONS

In this section, we give the extra experimental evaluations, including the last accuracy-memory curve, the gradient norm of all tasks, CKA visualization of different layers, multiple runs, and running time. We also conduct experiments on ImageNet to discuss which layer should be frozen in MEMO.

# C.1 LAST ACCURACY-MEMORY CURVE

There are two commonly used pertest accuracy after the b-th stage as $\boldsymbol { \mathcal { A } } _ { b } .$ ance measures for cla, the average accuracy $\begin{array} { r } { \bar { \mathcal { A } } = \frac { 1 } { B } \sum _ { i = 1 } ^ { B } \mathcal { A } _ { i } } \end{array}$ arning. Denote therepresents model’s average performance with streaming data. The last accuracy $\mathcal { A } _ { B }$ denotes the performance after the last learning stage. These two accuracy measures are commonly used to measure the CIL performance in former works (Rebuffi et al., 2017; Zhao et al., 2020; Yu & Aizawa, 2019; Wu et al., 2019). We provide the performance-memory curve with average accuracy in the main paper and report the curve with the last accuracy in Figure 21.

We can infer from these figures that the observations in the main paper still hold, e.g., we observe the intersection between exemplar-based methods and model-based methods in CIFAR100. We do not observe the intersection on ImageNet100, but the performances of DER and WA are relatively close at the start point. The main reason is that the performance of the 4-layer ConvNet with a million parameters is enough to obtain diverse feature representations (as discussed in Figure 13). We can infer from Figure 21(b) that the intersection will be observed given a smaller memory size. Besides, the rankings between methods are not changed between these methods, and MEMO outperforms others by a substantial margin in most cases.

![](images/ff3989fda2c599c2fb8220b6f0397dfd7e9cc8dc0c53b0c08147796c4a38e1b9.jpg)  
(a) CIFAR100

![](images/610f54a55811a1709fc85f064731116d6715bdb9bd62a40433566105c559104b.jpg)  
(b) ImageNet100   
Figure 21: Last accuracy-memory curve for CIFAR100 and ImageNet100. Other settings are the same as the main paper. The order between these methods still holds.

# C.2 WHICH LAYER SHOULD BE FROZEN?

In the main paper, we discuss the choice of fixing/unfixing the specialized and generalized blocks with empirical evaluations on CIFAR100. We report similar observations on ImageNet100 in Figure 22.

The main conclusions of these datasets are consistent with the former ones. Firstly, specialized blocks should be frozen. This conclusion is observed by comparing the results that $\bar { \phi } _ { s } ( \phi _ { g } ( \mathbf { x } ) )$ has better performance than $\phi _ { s } ( \phi _ { g } ( \mathbf { x } ) )$ , and $\bar { \phi } _ { s } ( \bar { \phi } _ { g } ( \mathbf { x } ) )$ has better performance than $\phi _ { s } \big ( \bar { \phi } _ { g } \big ( \mathbf { x } \big ) \big )$ . Secondly, by comparing the best strategy in the different settings, we can infer that fixing or not the generalized block depends on the number of classes in the first incremental task. It can be seen that $\bar { \phi } _ { s } ( \phi _ { g } ( \mathbf { x } ) )$ has the best performance with 10 base classes, while $\bar { \phi } _ { s } ( \bar { \phi } _ { g } ( \mathbf { x } ) )$ has the best performance with 50 base classes. The main reason behind these phenomena is the definition of a ‘good’ generalized block. When the base classes are large enough, training these classes can obtain diverse and transferable generalized representations. By contrast, if the base classes are small with few classes, training these

![](images/95a79c275d955305c0f9be18890615da5ffeaceedb7e62632873ebb545c41907.jpg)  
(a) ImageNet100, Base0 Inc10

![](images/3789eb4dc9af13ad968617128ca9132dcc8a760de5cddca9854d42f13f589b17.jpg)  
(b) ImageNet100, Base50 Inc10

![](images/10e082a8362d9d23e5315d90b81000b0fc1144065cc8ed265321d90b2edf4a77.jpg)  
Figure 22: Experiments about specialized and generalized blocks. Specialized blocks should be fixed, while fixing or not generalized blocks depends on the number of classes in the base stage.   
(a) Base5 Inc5

![](images/4f4a4a634d56cd16f35b63f46d180aa5f0a3a4c2bfb22ef1cd7964254dea8d76.jpg)  
(b) Base10 Inc5

![](images/83b8f1584edac3cadec3049813f087cdfc2fcff7c99860a3a59c4ce2fe10f4a5.jpg)  
(c) Base20 Inc5

![](images/b91f6b5cda369db37598d8d2334bb7c71b136b16005979e36edc2023e69176a0.jpg)  
(d) Base25 Inc5

![](images/df525ee4a7144961f3d8ccbf9ed8c70ef60a07ca073fdf612e7f526de5efff39.jpg)  
(e) Base30 Inc5

![](images/5397ff070ee44af5e1f2446711682ff29ec39b903ae5cee1ece1733381cb96a1.jpg)  
(f) Base35 Inc5

![](images/f910bac622d14e32c4ef845754290852d0e0d4c67c40c4efb0d88107b02512d7.jpg)  
(g) Base40 Inc5

![](images/4bc76152e354394928b8f50b1006a49c1d2fa554286d13b95506d93bb333d9be.jpg)  
(h) Base50 Inc5   
Figure 23: Comparison of $\bar { \phi } _ { s } ( \phi _ { g } ( \mathbf { x } ) )$ and $\bar { \phi } _ { s } ( \bar { \phi } _ { g } ( \mathbf { x } ) )$ ) given differnt base classes on CIFAR100 dataset. We annotate the gap of the last accuracy between $\bar { \phi } _ { s } ( \phi _ { g } ( \mathbf { x } ) )$ and $\bar { \phi } _ { s } ( \bar { \phi } _ { g } ( \mathbf { x } ) )$ at the end of each line. Fewer base classes prefer trainable generalized blocks, while more base classes prefer frozen generalized blocks. The intersection among them emerges around 20 base classes.

classes cannot obtain diverse and transferable generalized representations, and fixing the generalized block will harm the representation ability of the model and the final performance.

In real-world applications, we may not know the incremental learning implementations in advance. Hence, it requires the model to design a suitable strategy to automatically choose the frozen layers. In Figure 23, we show a preliminary experiment by changing the number of base classes in CIFAR100. Specifically, we vary the number of base classes among {5, 10, 20, 25, 30, 35, 40, 50} and show the incremental performance. In the former experiments, we already know that specialized blocks should be frozen. Hence, we only compare $\bar { \phi } _ { s } ( \phi _ { g } ( \mathbf { x } ) )$ and $\bar { \phi } _ { s } \big ( \bar { \phi } _ { g } ( \mathbf { x } ) \big )$ in these figures.

As we can infer from these figures, $\bar { \phi } _ { s } ( \phi _ { g } ( \mathbf { x } ) )$ (i.e., do not freeze the generalized blocks) shows better performance when the base classes are limited, e.g., fewer than 20. The gap between these strategies becomes smaller as the number of base classes increases. When the base class number reaches 20, the intersection among them emerges. After that, $\bar { \phi } _ { s } \big ( \bar { \phi } _ { g } ( \mathbf { x } ) \big )$ (i.e., freezing the generalized blocks) shows better performance. Hence, we can treat 20 as an empirical threshold to define the learning protocol.

![](images/9501d7bdcc792157b3fbc7621d3ce21f5513ce89f4310709f7a83e5c73ffbafd.jpg)  
(a) CIFAR100 B50 Inc5. Base class accuracy

![](images/ccd46ad6bcf84d1522621c8ac063e352f1e93b6b4bb31afc0e04cbcfd1168f0b.jpg)  
(b) CIFAR100 B50 Inc5. New class accuracy

![](images/d06e6038bdcf9326b4f13c4e03ab6fbf2e0ee67fa46453ab96c32588eeec7a12.jpg)  
(c) CIFAR100 B0 Inc10. Base class accuracy

![](images/afabb07ec7724409ba499822867ec69fefc50f32d5de08f6ab3171ff33135374.jpg)  
(d) CIFAR100 B0 Inc10, New class accuracy   
Figure 24: Base and new class accuracy of different strategies. Freezing the generalized blocks helps to overcome catastrophic forgetting, while changing generalized blocks helps to adapt to new classes efficiently.

It must be noted that these figures only correspond to a specific case of the CIFAR100 dataset, which may be different in other learning scenarios. Designing proper metrics to measure the generalizability of the shallow layers is interesting future work, and a possible solution is to utilize the hold-out or wild data for evaluation. On the other hand, it would be interesting to explore how to strengthen the generalization ability of shallow layers, e.g., via meta-learning (Sun et al., 2019), self-supervised learning (Khosla et al., 2020) and deep metric-learning (Wang et al., 2017).

# C.3 INFLUENCE OF FREEZING GENERALIZED BLOCKS

In Section C.2, we empirically verify that the strategy to freeze or not the generalized blocks is related to the number of base classes. In this section, we explore the influence when freezing the generalized blocks. Specifically, we run the experiment under CIFAR100 B0 Inc10 and CIFAR100 B50 Inc5 setting and report the results in Figure 24.

In these figures, we separately record the accuracy of the ‘Base’ and ‘New’ classes along incremental stages. ‘Base’ classes denote the classes in the first incremental stage, i.e., in D0, while ‘New’ classes represent the classes in the latest incremental stage, i.e., in $\mathcal { D } ^ { b } .$ . As a result, the accuracy of base classes represents the ability to resist catastrophic forgetting, while the accuracy of new classes implies the ability of the model to adapt to new classes. These abilities are also known as ‘stability-plasticity

dilemma’ (Grossberg, 2012). It should be noted that incremental performance jointly considers the performance among all seen classes, and both abilities are essential in incremental learning.

As we can infer from these figures, freezing generalized blocks shows better performance on the base classes, which means it can better resist catastrophic forgetting. However, when it comes to new classes, dynamic generalized blocks show to have better performance. The reason is intuitive that freezing the generalized blocks restricts the model from adapting to new patterns of new classes. In other words, the general layers are trained with the current task, which is not generalizable enough for new tasks if the current class data is insufficient. Under such circumstances, freezing these layers harms the learning ability of the model to adapt to new classes. On the other hand, since the model keeps an exemplar set of old class instances, jointly optimizing the general layers with exemplars and the current dataset helps to rectify it, making it generalize to all classes and enhancing the model’s ability. It must be noted that the joint learning process can resist forgetting by rehearsing former instances.

To summarize, CIL requires the model to perform well among all seen classes. Hence, if the benefits of learning new classes surpass the loss of old classes, we should enable the model to adapt to new classes and not freeze the generalized blocks. By contrast, if there are numerous base classes and forgetting them shall significantly damage the performance, freezing the generalized blocks is a better solution. These results are consistent with Section C.2.

![](images/ade0369b5b5dfde9623290a021de3785bfb73bf05edb4be59b6eca8c459d487e.jpg)  
(a) Multiple runs

![](images/0d05838a522f37bc793dbaeaccfeea05facfc4e34ba70686b3d0ae3a532584c9.jpg)  
(b) Incremental performance   
Figure 25: Left: The average and last accuracy of different methods. Error bars denote the standard deviation. Right: Average incremental performance among five runs. The standard deviation is shown in the shadow region. The ranking of these methods is the same with different class orders.

# C.4 INCREMENTAL LEARNING WITH MULTIPLE RUNS

A typical setting of CIL defines the comparison protocol (Rebuffi et al., 2017; Hou et al., 2019; Wu et al., 2019; Liu et al., 2020; Yu et al., 2020; Zhao et al., 2020; Yan et al., 2021; Douillard et al., 2021) to shuffle the class order with random seed 1993, and we follow this protocol to conduct the benchmark comparison in the main paper. In this section, we run the experiment multiple times with different random seeds and report the results in Figure 25(a). We choose random seeds from {10, 20, 30, 40, 50} and run the experiments five times with CIFAR100, Base50 Inc5. We also show the incremental performance of each method in Figure 25(b). We plot the average performance and standard deviation (shown in the shadow region) of each method among five runs. As we can infer from the figure, the results are consistent with the conclusions in the main paper, and the order of different classes remains the same with the change of random seeds.

# C.5 RUNNING TIME COMPARISON

Exemplar-based methods rely on revisiting former instances during new class learning, i.e., the model optimizes the loss term over $\mathcal { D } ^ { b }$ ∪ E in every incremental stage. Hence, adding exemplar size will

![](images/3c2f83a8a3de8f2ba4c0ff90612d82c779d19333c4a32c4b8722b81bde8947a5.jpg)  
Figure 26: Running time comparison of different methods on CIFAR100. The running time of MEMO is at the same scale as other methods.

correspondingly increase the running time of these methods. On the other hand, model-based methods save the old backbones, which requires forwarding the same batch of instances multiple times with different backbones. These methods will increase the running time of class-incremental models, and we empirically analyze the running time of these methods on CIFAR100, Base0 Inc10 in this section. We report the running time in Figure 26.

As we can infer from the figure, simply replaying with exemplars consume the least running time, while it gets the worst performance among all methods. Adding the knowledge distillation can relieve catastrophic forgetting while substantially increasing the running time. On the other hand, expanding the models and saving old backbones obtains better performance. At the same time, it also increases the running time since a single instance should be forwarded by multiple backbones in the learning process. To summarize, we find that exemplar-based and model-based methods have the same scale running time. In other words, our MEMO achieves the best performance with the competitive running time, which is more efficient for developing CIL models in real-world applications.

# C.6 GRADIENT NORM OF ALL INCREMENTAL TASKS

In the main paper, we provide the gradient norm analysis for a single incremental task due to the page limit. We give the full gradients of all incremental tasks in this section, as shown in Figure 27. We can infer from these figures that the trend of gradient norm still holds for other incremental tasks. To be specific, the gradients of deeper layers are larger than shallow layers for all incremental tasks.

# C.7 CKA VISUALIZATION OF DIFFERENT LAYERS

In the main paper, we use CKA (Kornblith et al., 2019) to measure the similarity between different backbones learned during the incremental stages with ResNet32. We calculate the pair-wise feature similarities between the shallow layers (i.e., after residual block 5) and deep layers (i.e., after residual block 15) in the main paper. In this section, we provide the full CKA visualization of these residual blocks in Figure 28. As we can infer from these figures, the features of different backbones at the same depth yield different similarities. The features are highly similar for the shallow layers, i.e., after residual block 5 and residual block 10. In contrast, the similarity is diverse for deeper layers, i.e., after residual block 15. These results are consistent with the choice of generalized and specialized blocks discussed in the main paper and the empirical evaluations in Figure 19.

# C.8 COMPARISON WITH GAN-BASED METHODS

Generative models are capable of capturing the distribution of the data and generating instances. A typical line of work using GAN (Goodfellow et al., 2014) to memorize the distribution of former tasks and then replay them when learning new tasks (He et al., 2018; Shin et al., 2017a). Specifically, (Shin et al., 2017a) considers saving an extra GAN model as the generator and incrementally updates it when new data arrives. The classification model is optimized jointly with Dnew ∪ Dgen, where

![](images/5079613a0522fb69df75e7e63840fef2580d6d9b566b8d8653053048b25a6f30.jpg)  
(a) Task 1

![](images/36311713c0719e1c7d1e413b4be5cfe2978fa16e130c09b076ebfdd7a118271f.jpg)  
(b) Task 2

![](images/4abf9e1e3fb8e822c3d06eec8126d8380ccc744e9f99a0d4c04d8cbae802369b.jpg)  
(c) Task 3

![](images/1829180a9655265159fea16bdd7db1d1a141e1906d995b8eb489af6cd3f58242.jpg)  
(d) Task 4

![](images/3bce9000206d32476c7b0375b011274ff145094173b642ad5b273c00206cb05d.jpg)  
(e) Task 5

![](images/13843d001ab025d2463af5586657c9aea5817abd2f730a629cd596f43290fefa.jpg)  
(f) Task 6

![](images/026aeff60a74436359b4fe56ef1191e70482ee8cb080d622f30c26f812a20b35.jpg)  
(g) Task 7

![](images/4ae6a566dc50abdd8e0c464edef4a298e66d3c1b9a179d3ac4a7b534b7b51abb.jpg)  
(h) Task 8

![](images/c1a40055375f86bb2e9e3679bc87a7b46c6188402218dc2c7731936746590daf.jpg)  
(i) Task 9

![](images/03202bd08f06ada495072d921b9f31e584c9bf0dd004b9cd8ce304f520bd3eee.jpg)  
Figure 27: Gradient norm of different tasks. The numbers are reported in log scale. Deeper layers have larger gradients while shallow layers have smaller ones.   
(a) Residual Block 5

![](images/a189ce21aa1c298bcd30f66e6385a071ffb46bd3a2998dd1e93685ef769dda9a.jpg)  
(b) Residual Block 10

![](images/64e6eea4fb387e7524df2c3da7c18e98b800222990f64a7b2139f78c92658145.jpg)  
(c) Residual Block 15   
Figure 28: CKA visualization of different layers. The larger block index indicates deeper layers. The features extracted by deeper layers of different backbones are dissimilar, while that of shallow layers are similar.

$\mathcal { D } ^ { n e w }$ stands for the incoming dataset and $\boldsymbol { \mathcal { D } ^ { g e n } }$ stands for the generated dataset from the former distribution. However, incrementally updating a single GAN model will also incur catastrophic

forgetting. Hence, (He et al., 2018) considers training a new GAN per incremental class to resist the forgetting phenomena in GAN updating. It requires saving multiple generative models in the memory, which costs more memory as the data stream evolves. Apart from saving GANs, (He et al., 2018) finds it useful to save exemplars from the former distribution, and optimizes the model with $\mathcal { D } ^ { n e w } \cup \mathcal { D } ^ { g e n } \cup \mathcal { E }$ .

In this section, we re-implement GR (Shin et al., 2017a) and ESGR (He et al., 2018) and compare them to our proposed MEMO with CIFAR100 dataset. We follow the implementations in the main paper to organize a ‘Base 0 Inc 10’ setting. ESGR requires saving multiple GANs, which costs a much higher memory budget, and we do not align the cost of it to the others. We follow the original paper to use WGAN (Arjovsky et al., 2017) as the generative model and implement it with four transposed convolutional layers. The optimization details (rounds, learning rate, optimizer) are set according to the original paper. We report the results in Table 25 and Figure 29.

We can infer from these results that training a GAN costs a large number of parameters, which is also hard to optimize for complex image inputs. Our proposed MEMO outperforms these methods by a substantial margin, even with a much fewer memory budget. As a result, we do not compare MEMO to these GAN-based methods in the main paper.

Table 25: Implementation details when comparing to GAN-based methods.   

<table><tr><td>Method</td><td>|E|</td><td>S(E)</td><td>Model Type</td><td># Parameters</td><td>Model Size</td></tr><tr><td>GR</td><td>3658</td><td>10.71MB</td><td>ResNet32 + WGAN</td><td>3.35M</td><td>12.78MB</td></tr><tr><td>ESGR</td><td>3300</td><td>9.66MB</td><td>ResNet32 + 100*WGAN</td><td>166.39M</td><td>634.75MB</td></tr><tr><td>MEMO</td><td>3300</td><td>9.66MB</td><td>ResNet32</td><td>3.62M</td><td>13.83MB</td></tr></table>

![](images/c80aa7c4992285ac14d7c85b24fdab9e20f4cafd1800a795063e9c9772861958.jpg)  
Figure 29: CIL performance

![](images/b8075f7dc29d53c8002f3c6ab019d01b082da2698970981159485bfee01ac227.jpg)  
(a) CIFAR100 Base0 Inc5

![](images/88578184fcc594ccb8dabd5020cce7121ca120dbb42911611f64e2581561c934.jpg)  
(b) CIFAR100 Base0 Inc10

![](images/8abfae386fe71a5feebe63a7e227326f42c0390522e89455385e7dbb4bacfe05.jpg)  
(c) CIFAR100 Base0 Inc20

![](images/aef15de22c21be23597d07e324d9066566067facf8f58f8b60218bc18b697e72.jpg)  
(d) CIFAR100 Base50 Inc10

![](images/0e37878673380a1845f9d1582aad3f2577d4970517453d6f158426fbc8ca3703.jpg)  
(e) CIFAR100 Base80 Inc10

![](images/cfa26948574d3fb4767ad35ebfebfbf74fb61f5a667a405053eb54e26f21f99f.jpg)  
(f) CIFAR100 Base80 Inc5   
Figure 30: Experiments when comparing our proposed method to SPM. MEMO consistently outperforms SPM with different benchmark settings.

# C.9 COMPARISON WITH MULTI-BRANCH MODEL

A recent work SPM (Wu et al., 2022) also considers the multi-branch model for class-incremental learning. It should be noted that SPM is designed for CIL with vast base classes, e.g., with 500 or 800 classes in the first stage. However, there are not so many base classes in the benchmark CIL setting,

and we re-implement SPM under the benchmark setting for comparison. In the implementation, we train a model from scratch with the base dataset for incremental learning.

Since SPM also decouples the backbone network into two parts, we follow the implementation in the original paper (Wu et al., 2022) to decouple the representation, i.e., before the last convolutional block. Hence, the way of expansion in SPM is the same as MEMO, making the model size almost the same (the only difference lies in the fully connected layers, which is negligible).

Following the comparison protocol defined in the main paper, we can compare these methods fairly with the same exemplar size. Since the model size and memory size of SPM and MEMO is equal, the comparison is fair for them. The results are reported in Figure 30. We can infer from these figures that MEMO consistently outperforms SPM on these benchmark settings. The comparison to the contemporaneous multi-branch method verifies the effectiveness of our proposed method.

![](images/ccd86f5bcead510227d46c0b21443eb7b331aabc147bb8f1e88cb9f163d9324b.jpg)  
$\mathrm { ( a ) } \ \mathrm { L a y e r – w i s e \ s h i f t } \ ( \mathrm { V i T } , W _ { Q } , W _ { K } , W _ { V } , \mathrm { M L P } )$

![](images/ba6bfe39f4e26c292a33d04ee1f50acf2558d20df694dd85563aa4ebb4e55a17.jpg)  
$\mathbf { \eta } ^ { \left( \mathrm { b } \right) } \mathrm { L a y e r – w i s e s h i f t } ( \mathrm { V i T } , W _ { Q } , W _ { K } , W _ { V } )$

![](images/b78537d7b1b7ec13ca7ef52c4fc8c0d62600060b5b0342119bb8849874d50da9.jpg)  
(c) Layer-wise shift (Bert, $W _ { Q } , W _ { K } , W _ { V } , \mathbf { M L P } )$

![](images/4854ce00c4696508d0ec947d7660443a76572040536373df88e697d6b62f4523.jpg)  
$\mathrm { ( d ) ~ L a y e r – w i s e ~ s h i f t } \left( \mathrm { V i T } , W _ { Q } , W _ { K } , W _ { V } \right)$   
Figure 31: Layer-wise shift of ViT and Bert. The observations in residual networks still hold for these network structures and NLP datasets.

# C.10 DIFFERENT BACKBONES AND DATASETS

In the main paper, we explore the network behavior with ResNet (He et al., 2015) on image datasets, and find shallow layers stay unchanged while deep layers change more in class-incremental learning. In this section, we verify this conclusion with different network structures and different incremental datasets.

Specifically, we first explore the behaviors of Vision Transformer (Dosovitskiy et al., 2020) in incremental tasks. We directly run the experiments on CIFAR100 Base0 Inc10 with a 6-layer ViT.

Following the experiments in the main paper, we trace the weights in each Transformer encoder (including the weights of multi-head attention and MLP) and show the trends in Figure 31(a), 31(b). In Figure 31(a), we can observe that the layer-wise shift of deeper layers is more obvious than shallow ones. We also trace the shift of multi-head attention blocks, i.e., $W _ { Q } , W _ { K } , W _ { V }$ in Figure 31(b), and find the trend is consistent.

Additionally, we explore the behaviors of the network in NLP tasks. We follow (Ke et al., 2021) to use Bert (Devlin et al., 2018) for ASC dataset (Ke et al., 2021) (the aspect sentiment classification dataset containing 19 products), which is a benchmark NLP task. We keep the other settings the same and trace the shift of Transformer layers in Bert and draw the trends in Figure 31(c), 31(d). These results show the same trend as ViT.

As we can infer from these figures, the layer-wise change shows that shallow layers change less while deep layers change more, sharing the same trend as in residual networks. Hence, we can summarize that in various settings, shallow layers stay unchanged while deep layers change more in class-incremental learning.

# D IMPLEMENTATIONS

# D.1 DISCUSSIONS ABOUT RELATED WORK

Class-incremental learning is now a hot topic in the machine learning field, where new methodologies emerge frequently. We discuss CIL methods by dividing them into two groups, e.g., exemplar-based and model-based. These groups either save exemplars or models to boost their performance.

However, there are other methods that do not fall into these groups, e.g., (Kirkpatrick et al., 2017; Li & Hoiem, 2017; Jin et al., 2021; PourKeshavarzi et al., 2022). Since they are designed to conduct incremental learning without an extra memory budget, these methods often perform inferior to those discussed in the main paper, even equipped with additional exemplars. On the other hand, there are methods that address memory-efficiency from other aspects. For example, (Iscen et al., 2020) addresses memory-efficient CIL by saving the embeddings instead of raw images, (Zhao et al., 2021c) suggests saving low-fidelity exemplars, and (He et al., 2018; Shin et al., 2017a) address the problem by generating exemplars with generative models. It should be noted that saving embeddings will suffer the embedding drift phenomenon (Yu et al., 2020) and requires an extra finetuning process to fix such drift. The bias of the embedding adaptation process will accumulate, which works poorly in incremental learning with multiple stages. We re-implement (Iscen et al., 2020) and find it shows inferior performance than saving exemplars. Generating exemplars with generative models will consume the memory budget to save generative models, which also suffer catastrophic forgetting (Cong et al., 2020) and fail for large-scale images (Iscen et al., 2020) (See Section C.8). There are other methods designing multi-branch network structures, $e . g .$ , AANets (Liu et al., 2021a), PNN (Rusu et al., 2016) and SPM (Wu et al., 2022). The extra branch is designed to re-scale the network outputs (Liu et al., 2021a) or get multi-head predictions (Wu et al., 2022), which requires an extra tuning process or routing design. By contrast, our proposed method does not require the extra model tuning and shows stronger performance (See Section C.9). As a result, we mainly concentrate on the discussions about typical CIL methods that rely on extra memory from the efficiency and model complexity perspective. Below are the introductions to compared methods in this paper.

• Replay (Chaudhry et al., 2019) is an exemplar-based baseline that simply optimizes the cross-entropy loss with $\mathcal { D } ^ { b } \cup \mathcal { E }$ in every incremental stage;   
• iCaRL (Rebuffi et al., 2017) builds knowledge distillation (Zhou et al., 2003; Zhou & Jiang, 2004; Hinton et al., 2015) regularization term to regularize former classes from being forgotten. The loss (cross-entropy and knowledge distillation) is optimized with $\mathcal { D } ^ { b } \cup \mathcal { E }$ in every incremental stage;   
• WA (Zhao et al., 2020) extends iCaRL with weight aligning, which normalizes the linear layers to reduce the negative bias;   
• DER (Yan et al., 2021) is a model-based method that saves backbones to resist catastrophic forgetting. Apart from the loss term discussed in the main paper, it also introduces an auxiliary loss to encourage diverse representations and a sparse loss to conduct network pruning.

In this paper, we implement DER with two modifications to the original implementation. Firstly, the original DER utilizes different backbone networks than other methods, $e . g .$ , modified ResNet18 for CIFAR100, while other methods utilize ResNet32 as the benchmark backbone. In this paper, we report the benchmark comparison when using the same backbones for DER and other exemplar-based methods (in Section 5.1 of the main paper). Secondly, DER claims to use a pruning algorithm to reduce the parameter number. But it shows that the pruning has little effect on the total parameters and harms the final performance. On the other hand, the pruning code is not open-sourced yet.3 As a result, we re-implement DER without the pruning loss to report the results in this paper.

Recently, SPM (Wu et al., 2022) finds that fixing the generalized block is effective for classincremental learning with vast base classes and proposes a multi-branch method for CIL with strong pre-trained models. The findings in SPM only correspond to a tiny portion of ours, and we list the differences below:

• Different Settings: SPM concentrates on the incremental learning scenario with a strong pre-trained model, which requires 500 or 800 base classes in their setting. However, we are focusing on the typical class-incremental learning setting, where the model should be trained from scratch with few classes (say, 5 or 10). Our analysis in Section 4.3 is also irrelevant to the strong pre-trained models.   
• Different Observations: The observation in SPM is highly driven by their setting, i.e., they focus on how to design incremental models with vast base classes and find freezing the generalized block can facilitate model learning. However, the findings in SPM are only a tiny portion of our conclusions in Figure 5. Apart from the aforementioned findings, we also summarize that if the base classes are insufficient, fixing the generalized block will lead to inferior performance. Besides, we also find that the specialized blocks of former tasks should be frozen in all cases, which is also not discussed in SPM.   
• Different Network Behaviors: It should be noted that none of the conclusions in Section 4.3 can be found in SPM, where we analyze from the aspect of network behaviors (gradient norm, shift between blocks, and CKA between backbones). As a result, the conclusions in SPM only correspond to a tiny portion of ours and should not weaken our novelty.   
• Different Methodologies: Although our MEMO and SPM both adopt the multi-branch structure; the core difference is that SPM adds a new specialized block and fully-connected layer for each new task. It requires calibration between old and new classes, while ours will not face this problem since we update a larger fully-connected layer as Eq. 2 after each incremental stage. Besides, facilitated by the simple and effective training protocol, our method does not need any hyper-parameter to control the trade-off between loss terms.

We give the comparison of our proposed method to SPM in Section C.9, where we verify that our proposed method is more suitable for the benchmark class-incremental learning scenario.

# D.2 IMPLEMENTATION DETAILS OF MEMO

Similar to DER, there are two loss terms in MEMO. Apart from the cross-entropy loss discussed in the main paper, the auxiliary loss aims to differentiate between old and new classes. Denote the b-th incremental stage dataset $\mathcal { D } ^ { b }$ contains $| Y _ { b } |$ classes, we create an extra classifier $W _ { A } \in \mathbb { R } ^ { d \times | Y _ { b } | + 1 }$ . The auxiliary loss is represented by:

$$
\mathcal {L} _ {A} (\mathbf {x}, \hat {y}) = \sum_ {k = 1} ^ {| Y _ {b} | + 1} - \mathbb {I} (\hat {y} = k) \log \mathcal {S} _ {k} \left(W _ {A} ^ {\top} \phi_ {b} (\mathbf {x})\right), \tag {4}
$$

where $\phi _ { b }$ is the b-th embedding created for $\mathcal { D } ^ { b } , \hat { y }$ reassigns the ground-truth label into $| Y _ { b } | + 1$ classes, and treat $y \notin Y _ { b }$ as class $\left| Y _ { b } \right| + 1$ . Eq. 4 helps to acquire diverse feature representations for each embedding backbone, and the auxiliary classifier $W _ { A }$ is dropped after each task training. The final optimization of MEMO combines the cross-entropy loss discussed in the main paper and the auxiliary loss in Eq. 4. We also use weight normalization to eliminate the bias in the classifier layer.

# D.3 EXEMPLAR SELECTION

As discussed in the main paper, we follow (Rebuffi et al., 2017) to select the exemplars in the exemplar set E with the herding algorithm (Welling, 2009). It aims to select the most representative instances per class by the distance to the class center. Denote the current embedding as φ(·). Given the instance set $X = \{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \cdots , \mathbf { x } _ { n } \}$ from class y, the target is to select m representative instances from X. We first calculate the class mean via: $\textstyle \mu \stackrel { \cdot } {  } \frac { 1 } { n } \sum _ { i = 1 } ^ { n ^ { - } } \phi ( \mathbf { x } _ { i } )$ . We then calculate and rank the distance of each instance to the class center $\left| \left| \mu - \phi ( \mathbf { x } _ { i } ) \right| \right|$ k in ascending order. The exemplar set E is the collection of the top-m instances with the least distance.

# D.4 MODEL COMPRESSION

This paper mainly discusses how to allocate the memory budget for class-incremental models, i.e., investigating a memory-efficient way to allocate the model and exemplar given a specific memory budget. We do not aim to design extra model compression algorithms or post tuning methods to reduce the total parameters. By contrast, we concentrate on which part of the model should be saved/dropped. Given the fact that there are many methods to conduct model compression (Deng et al., 2020), e.g., knowledge distillation (Wang et al., 2022), pruning (Yan et al., 2021), low-rank factorization (Sainath et al., 2013) and quantization (Yang et al., 2019), we believe they can be combined with our method orthogonally as interesting future work.

# D.5 BROADER IMPACT

In this work, we study the class-incremental learning problem, a fundamental problem in machine learning. Specifically, we first address the fair comparison among different methods by aligning the memory budget and propose several performance measures for a holistic evaluation. We then observe the differences between different layers in the class-incremental learning process and propose a simple yet effective baseline method to efficiently organize the memory budget. Our work will give instructions for applications with difficulties managing the memory size for CIL models. At the same time, there is still much room for exploration in this work. We hope our work can inspire more discussions about class-incremental learning in real-world applications and drive more research to build practical and memory-efficient CIL models.

Meanwhile, we are aware that the abuse of this technology can pose ethical issues. In particular, we note that people expect that learning systems will not save any personal information for future rehearsal. While there are risks with this kind of AI research, we believe that developing and demonstrating such techniques is essential for understanding valuable and potentially troubling applications of the technology. We hope to stimulate discussion about best practices and controls on these methods around responsible technology uses.