---
title: "Isolation and Impartial Aggregation: A Paradigm of Incremental Learning without Interference"
authors:
  - "Yabin Wang"
  - "Zhiheng Ma"
  - "Zhiwu Huang"
  - "Yaowei Wang"
  - "Zhou Su"
  - "Xiaopeng Hong"
date: "2022-01-01"
year: 2022
journal: "IEEE Transactions on Pattern Analysis and Machine Intelligence"
abstract: "This paper focuses on the prevalent performance imbalance in continual learning.\\"
abstract_cn: "本文聚焦于持续学习中的性能不平衡问题。提出一种基于阶段隔离的增量学习框架，通过一系列阶段隔离分类器避免相互干扰。引入基于锚点的能量自归一化策略，确保各阶段分类器在同一能量水平下工作，通过投票增强实现鲁棒推理。该方法任务无关，在四个大型基准数据集上取得了最先进的整体性能。"
keywords:
  - "[[Continual learning]]"
  - "[[Incremental learning]]"
  - "[[Catastrophic forgetting]]"
  - "[[Neural network]]"
cite: "Wang Y, Ma Z, Huang Z, et al. Isolation and impartial aggregation: A paradigm of\\"
aiSum: "阶段隔离增量学习框架+能量自归一化策略，避免灾难性遗忘，四个基准数据集SOTA。"
confidence: medium
---

Yabin Wang1, 3†, Zhiheng Ma2 †, Zhiwu Huang3, Yaowei Wang4, Zhou Su1, Xiaopeng Hong5, 4, 1‡

1School of Cyber Science and Engineering, Xi’an Jiaotong University, 2Shenzhen Institute of Advanced Technology, Chinese Academy of Science, 3Singapore Management University, Singapore, 4Peng Cheng Laboratory, 5Harbin Institute of Technology

iamwangyabin@stu.xjtu.edu.cn, zh.ma@siat.ac.cn, zzhiwu.huang@gmail.com

wangyw@pcl.ac.cn, {zhousu, hongxiaopeng}@ieee.org

![](images/9e3f390a3cfa97e8b6afaa78667cbab9ef086e8ecfa2020852b141268f6db3c0.jpg)

# Abstract
  - "[[Catastrophic forgetting]]"
  - "[[Continual learning]]"
  - "[[Neural network]]"

This paper focuses on the prevalent performance imbalance in the stages of incremental learning. To avoid obvious stage learning bottlenecks, we propose a brand-new stage-isolation based incremental learning framework, which leverages a series of stage-isolated classifiers to perform the learning task of each stage without the interference of others. To be concrete, to aggregate multiple stage classifiers as a uniform one impartially, we firstly introduce a temperature-controlled energy metric for indicating the confidence score levels of the stage classifiers. We then propose an anchor-based energy self-normalization strategy to ensure the stage classifiers work in the same energy level. Finally we design a voting based inference augmentation strategy for robust inference. The proposed method is rehearsal free and can work for almost all continual learning scenarios. We evaluate the proposed method on four large benchmarks. Extensive results demonstrate the superiority of the proposed method in setting up new state-of-the-art overall performance. Code is available at https://github.com/iamwangyabin/ESN.

# Introduction

Incremental learning (a.k.a, continuous learning or lifelong learning) is a paradigm that continually evolves machine models on a data stream. It is a longstanding research topic and might offer a path toward more human-like AI. The stability-plasticity dilemma is central to incremental learning (Mai et al. 2022; De Lange et al. 2021), which requires the models to be plastic to acquire new knowledge and stable to consolidate existing knowledge continuously.

Most previous works struggle to keep a fragile balance between stability and plasticity and also achieve pretty good

*This is the accepted version of (Wang et al. 2023), the Proceedings of the 37th AAAI Conference on Artificial Intelligence (AAAI23), Feburary 7–14, 2023, Washington DC, USA. Please cite the final published version.   
† Yabin Wang and Zhiheng Ma are co-first authors.   
‡ Xiaopeng Hong is the corresponding author.

results in terms of average accuracy, which, however, results in tremendous performance gaps of different learning stages (a.k.a. sessions or tasks). This is a well-known phenomenon named class imbalance (Mai et al. 2022; De Lange et al. 2021). The source of this problem is twofold: firstly, the imbalance in the number of samples between the new incoming data and the historical data; secondly and more importantly, using a uniform model to portray a heterogeneous data stream may result in a zero-sum game (Riemer et al. 2018; Knoblauch, Husain, and Diethe 2020), where one party gains mean another loses, as shown in Fig. 1 (a). This imbalance results in the breakdowns in recognizing certain classes, which creates a bottleneck in the final performance and limits the application of the model in real-world scenarios. A few methods use a rehearsal buffer to alleviate such imbalance problems (Hou et al. 2019). However, saving previous training data is memory expensive and has a privacy issue.

To address these issues, in this paper, we study how to create win-win solutions for all-stage learning. We challenge the traditional unified paradigm and suggest a stage-isolation scheme for learning stage classifiers (in Fig. 1 (b)). Stage isolation is targeted at learning multiple high confidence and low bias stage-specific classifiers for every stage in isolation, so that the classifier in each stage can be shielded from the interference of other stages, to satisfy the performance requirements of each stage adequately.

Nevertheless, the main difficulty of this paradigm lies in how to aggregate in an impartial way multiple isolated learners trained on different stages, as the learners trained on different stages of various incoming data stream separately may have diverse class-wise confidence distributions. For example, as shown by Fig. 3(b), the output scores of the classifiers of two stages can be clearly different. A straightforward aggregation like finding the class with the highest confidence still has a tendency to stage imbalance.

We contend that the key to solving this problem lies in

![](images/052b746c23f676967c287d54cf5348f84afaf4c906ce0e115e75cccb2c93ec34.jpg)  
Figure 1: Comparison of the proposed ESN against traditional methods. (a) Existing methods usually use a uniform model to portray a heterogeneous data stream, which may cause performance imbalance and interference among the learning stages. (b) In contrast, the proposed ESN uses a stage-isolation scheme for learning stage classifiers upon a fixed pre-trained backbone, resulting in much less forgetting and interference.

the regularization of the stage classifier outputs. Specifically, there are three criterions to meet. Criterion 1: the stage classifier should have higher output confidence scores for the data within the stage it belongs to (i.e., in-stage data) than others (i.e., out-stage data); Criterion 2: the confidence scores for in-stage data should be consistent across all stages; Criterion 3: the right stage classifier for the instage data shall have the highest confidence score among all classifiers. Unfortunately, they are challenging to be satisfied in the incremental learning scenarios. The reasons are two-fold. First, optimizing the stage learners only using the current data (the only one accessible) will result in a serious bias. Second, it is impossible to make full regularization as the classifiers to be learnt in future can not be considered at current stage.

Dealing with such a backward-compatible regularization dilemma, inspired by the Helmholtz free energy theory (Le-Cun et al. 2006), we introduce a temperature controlled energy metric to reflect the confidence score levels of stage classifiers. On this basis, we provide a rehearsal-free incremental learning paradigm, which regularize the stage classifiers for aggregating them impartially as a uniform classifier. Specifically, we first use the pre-trained ViT (Dosovitskiy et al. 2021) backbone as a frozen strong prior before the stage-specific classifiers to assure higher confidence scores for the in-stage data than the out-stage data as far as possible, which has been proved in (Fort, Ren, and Lakshminarayanan 2021) (for Criterion 1). Second, we design an anchor-based energy self-normalization loss, which restricts the energy metrics of stage classifiers tightly around the energy anchor, to ensure all stage classifiers lay in the same energy level when facing in-stage data of their own (for Criterion 2). Furthermore, though the ‘so far’ best control parameter for the current stage can be found by a design method, it works only in a backward-compatible manner. To avoid overfitting

to any specific stage, we maintain the ‘so far’ best parameters for all stages met and use a voting scheme to produce reliable inference outputs, by which Criterion 3 can be better approached by stages1.

To summarize, we propose a brand-new rehearsal-free general incremental learning paradigm to tackle the performance imbalance and the zero-sum game problems, called Energy Self-Normalization (ESN), which can handle almost all scenarios, including class-incremental learning (CIL) (De Lange et al. 2021), domain-incremental learning (DIL) (Wang, Huang, and Hong 2022), and cross-domain class incremental learning (Xie, Yan, and He 2022). The contributions can be further detailed as follows:

• We propose the anchor-based energy self-normalization (ESN) so that stage-classifiers can produce high and consistent confidence scores for in-stage data.   
• We design a control parameter (temperature) finding method to obtain stage-cumulative best parameters for progressively ensuring ‘right’ classifiers with the highest scores. On this basis, we propose a voting based inference augmentation strategy for robust inference.   
• The proposed ESN sets up new state-of-the-art performance, as shown by extensive experiments on four largescale benchmarks. A challenging benchmark for crossdomain class incremental learning is built as well.

# Related works

# Incremental Learning

There are three main types of incremental learning methods (De Lange et al. 2021).

Rehearsal-based methods tackle catastrophic forgetting either by keep a small set of old training examples in memory (Tao et al. 2020; Dong et al. 2021; Liu et al. 2022) or using synthesized data produced by generative models (Shin et al. 2017). By using rehearsal buffer for knowledge distillation and regularization, rehearsal-based methods have achieved state-of-the-art results on various benchmarks (Douillard et al. 2022; Joseph et al. 2022; Zhang et al. 2022). However, the performance of rehearsal-based methods generally deteriorates with smaller buffer size (Mai et al. 2022). What’s more, it is often more desired that the exemplars of old tasks are not stored for the data security and privacy reasons (Wang, Huang, and Hong 2022).

Regularization-based methods design knowledge distillation strategies (Li and Hoiem 2017) or parameter regularization terms (Kirkpatrick et al. 2017) to mitigate catastrophic forgetting.

Network-based methods modify networks’ architecture during incremental learning to mitigate catastrophic forgetting. Some works expand network parameters to learn new tasks and get state-of-the-art performances (Yan, Xie, and He 2021; Wang et al. 2022b; Xu and Zhang 2020; Douillard et al. 2022). Also some methods use the parameter isolation strategy to keep each task independent (Serra et al. 2018; Li et al. 2019). Recently, L2P (Wang et al. 2022b) uses

prompt tuning and pre-trained models for incremental learning tasks. Parameter efficient fine-tuning, like prompt tuning, offers a promising way for incremental learning problems. However, L2P is still a unified-structure model, and it requires a fixed query function to find prompts, which is time-consuming and less efficient in complicated situations.

# Energy-based Models

Energy-based Models (EBMs) (LeCun et al. 2006) capture dependencies of variables by associating a scalar energy to each configuration of the variables. EBMs have been used for generative modeling (Du and Mordatch 2019), out-ofdistribution detection (Liu et al. 2020), and open-set classification (Al Rahhal et al. 2022). Despite being successful across various tasks, EBMs have limited applications in incremental learning. ELI (Joseph et al. 2022) proposes to learn an energy manifold to counter the representational shift that happens during incremental learning. It uses EBMs to portray changes of the model and then try to compensate the updated model to the original one, which is still a tug of war. What’s more, it assumes the energy between different stages is distinguishable, which is a too strong assumption in application scenarios. EA (Zhao et al. 2022) also uses energy-based model to add the calculated shift scalars onto the output logits to mitigate class imbalance. The calculation of compensation scalars is based on the samples of all classes, which suggests that it relies on rehearsal buffer. Both works still struggle to alleviate the imbalance problem in a uniform model. Moreover, they are both rehearsal-based and can only handle CIL problems, which are far from general and robust solutions for incremental learning.

# Proposed Method

# Problem Definition

Incremental learning refers to training the model in a data stream, while the model can only access part of the training data at a time. Let $\zeta = \{ 1 , 2 , \mathrm { { } } \mathrm { { } } 3 , . . . , S \}$ denote the Stage-ID set, where S is the current maximum stage number. The incoming data of the s-th stage is denoted as $\mathcal { D } ^ { s }$ = $\left\{ x _ { i } , y _ { i } \right\} _ { i = 1 } ^ { N ^ { s } }$ , where $N ^ { s }$ is the total samples number of this stage. $( x , y ) \sim p _ { d a t a } ^ { s }$ represents the data distribution of the s-th stage. For class incremental learning, different stages have different categories to learn, and there is no category overlap, $\ y ^ { i } \cap \mathcal { y } ^ { j } \doteq \emptyset$ , where $\mathcal { V } ^ { s }$ is the label set of the s-th stage. For domain incremental learning, the categories maintains the same for all stages, $\mathcal { V } ^ { i } = \mathcal { V } ^ { \bar { j } }$ , but data distribution of each stage is different or even highly heterogeneous.

Our proposed ESN can handle these two challenging scenarios at the same time and even more challenging crossdomain class incremental learning, in which different stages have different categories from different domains.

# Overall Framework

Previous incremental learning methods need to find a fragile balance between stability and plasticity. Using a uniform model to portray a heterogeneous data stream may result in a zero-sum game and be seriously biased toward newer classes (De Lange et al. 2021; Mai et al. 2022).

![](images/cd0fe1383209a0093571cebf9d76818b7cbcea583021a9e580841fc1b33e0e37.jpg)  
Energy of Previous/Current Classifier   
Figure 2: Overview of the proposed anchor-based energy self-normalization for stage classifiers. The classifiers of the current and the previous stages, $f _ { \eta _ { s } }$ and $f _ { \eta _ { s - 1 } }$ , are aligned sequentially to restrict their energies around the anchor.

In this paper, we proposed a brand-new rehearsal-free general incremental learning paradigm to tackle the imbalance and the zero-sum game problems. Specifically, we train multiple isolated stage-specific classifiers upon a frozen pretrained backbone for each stage. In the inference phase, we first select the most confident classifier (Eq. 1), and then use it to predict the final result (Eq. 2).

$$
s ^ {*} = \underset {s \in \zeta} {\operatorname {a r g m a x}} H ^ {s} (x), \tag {1}
$$

$$
y ^ {*} = \underset {y \in \mathcal {Y} ^ {s ^ {*}}} {\operatorname {a r g m a x}} P ^ {s ^ {*}} (y | x), \tag {2}
$$

where $P ^ { s } ( y | x )$ is the classifier of the s-th stage, and its confidence score function is denoted as $H ^ { s } ( x )$ . As shown, comparability between different stages’ confidence scores is the guarantee of impartial aggregation.

As shown in $\mathrm { F i g } .$ . 1, given a pre-trained backbone $f _ { \theta } ,$ , each stage we initialize a specific classifier $f _ { \eta _ { s } }$ . During training at stage $s ,$ we freeze the pre-trained backbone $f _ { \theta }$ and only update parameters of the classifier $\eta _ { s } , \theta$ and $\eta$ are parameters of backbone and classifier respectively. For simplicity, we use the ViT-B/16 pre-trained on ImageNet as freeze backbone, and use the class-attention block (CAB) (Touvron et al. 2021) with a linear projection as the classifier. Our proposed strategy is also suitable for other parameter isolation methods (Jia et al. 2022), which we will show later in the experiments. The stage isolated classifier can shield the interference of each other.

In the following sections, we first detail the training method based on the self-normalization strategy, which ensures the impartial aggregation of all stages’ classifiers. Then we introduce the stage-cumulative control parameter optimization method with voting-based inference augmentation to further promote the performance.

# Stage Classifier Self-Normalization

The most commonly used training criterion in training deep neural networks is the softmax cross-entropy loss. However, previous works (Tang et al. 2021; Liu et al. 2020) show that directly training with this loss results in overconfidence issues, where the maximum softmax activation value always approaches one in despite of the data is from training data distribution or not. Previous works have shown that other criteria such as the Helmholtz free energy (Liu et al. 2020) or

the maximum logit value (Hendrycks et al. 2019) are better confidence scores than the maximum softmax value. However, none of the above works discuss how to align confidence scores between different classifies learned from data steam.

Next, we first briefly review the relationship between the softmax cross-entropy loss and the energy-based model (Grathwohl et al. 2019; Liu et al. 2020; LeCun et al. 2006), then propose the anchor-based energy selfnormalization objective function, which makes energy for in-stage data consistent across stages.

Let’s define the energy function for a given input-label pair $( x , y )$ as follows:

$$
E ^ {s} (x, y) = - h ^ {s} (x) [ y ], \tag {3}
$$

where $h ^ { s } ( x ) = f _ { \eta _ { s } } ( f _ { \theta } ( x ) )$ is the logits of the s-th classifier, and $h ^ { s } ( x ) [ y ]$ is the logit value of $y \in \mathcal { V } ^ { s }$ , then softmax activation can be considered as a special case of discrete Gibbs distribution when the temperature parameter $T$ equals to 1:

$$
P _ {T} ^ {s} (y | x) = \frac {\exp \left(- E ^ {s} (x , y) / T\right)}{\exp \left(- \mathcal {F} _ {T} ^ {s} (x) / T\right)}, \tag {4}
$$

where $\mathcal { F } _ { T } ^ { s } ( x )$ is the Helmholtz free energy, which can be expressed as the negative log partition function:

$$
\mathcal {F} _ {T} ^ {s} (x) = - T \log \sum_ {y \in \mathcal {Y} ^ {s}} \exp \left(- E ^ {s} (x, y) / T\right). \tag {5}
$$

Thus, the softmax cross-entropy loss can be rewritten as Eq. 6.

$$
\begin{array}{l} \mathcal {L} _ {c e} ^ {s} = \mathbb {E} _ {(x, y) \sim p _ {d a t a} ^ {s}} \left(- \log P _ {T} ^ {s} (y | x)\right) \\ = \frac {1}{T} \mathbb {E} _ {(x, y) \sim p _ {d a t a} ^ {s}} \left(E ^ {s} (y, x) - \mathcal {F} _ {T} ^ {s} (x)\right). \tag {6} \\ \end{array}
$$

As can be seen, the softmax cross-entropy loss will decrease the energy between the input data and the groundtruth label while increasing the overall Helmholtz free energy. However, when $\bar { E ^ { s } ( y , x ) }$ and $\mathcal { F } _ { T } ^ { s } ( x )$ are added with the same scalar, the loss value remains unchanged, which makes it meaningless to directly compare the free energy between different classifiers trained independently using softmax cross-entropy loss. To fix this issue, we propose a simple but effective energy self-normalization loss $\mathcal { L } _ { a l } ^ { s } ,$ which constrains the free energy of each classifier with a fixed anchor $\Delta ,$ as Eq. 7.

$$
\mathcal {L} _ {a l} ^ {s} = \mathbb {E} _ {x \sim p _ {d a t a} ^ {s}} \left(\mathcal {F} _ {T} ^ {s} (x) - \Delta\right) ^ {2}, \tag {7}
$$

where   is a preset hyper-parameter, and the experimental results show that ESN is insensitive to its value. The total loss trained for every individual classifiers is given by Eq. 8.

$$
\mathcal {L} _ {\text {t o t a l}} ^ {s} = \mathbb {E} _ {\left(x ^ {s}, y ^ {s}\right) \sim \mathcal {P} _ {\text {d a t a}} ^ {s}} \left(\mathcal {L} _ {\text {c e}} ^ {s} + \lambda \mathcal {L} _ {\text {a l}} ^ {s}\right), \tag {8}
$$

where   is a hyper-parameter to balance $\mathcal { L } _ { a l } ^ { s }$ term. And we choose a representative temperature $T = \mathrm { ^ { w } 1 }$ during training. Our complete training algorithm is introduced in Alg. 1. Fig. 3 visualizes the free energy distribution with and without the self-normalization, which illustrates the effectiveness of ESN.

![](images/fd00502d58ab192a5f9fab5ad1e87c18de8b5a0b63ac52db96e7354927aed1dd.jpg)  
(a) Confidence Score Distribution w/ ESN

![](images/0e68a19cf95ae2da813829e5e4bca897fc9084b9cf065ee8ff249ea6f1877d19.jpg)  
(b) Confidence Score Distribution w/o ESN   
Figure 3: Distribution shift. We extract 2 stages’ training data from Split CIFAR-100 and show their confidence scores trained with and without using our proposed anchor-based energy self-normalization. The y-axis is the count of image, and the x-axis is the confidence score.

# Algorithm 1: Model Training

0: Given components: Pre-trained backbone $f _ { \theta } ,$ stage classifier $f _ { \eta } ,$ total stage number S, training iterations for each stage ${ \dot { M } } ,$ energy anchor $\Delta ,$ , training data $\mathcal { D } ,$ learning rate ✏, temperature pool ⌦, candidate temperature pool $\Psi ;$

1: for $s = 1 , \cdots , S$ do   
2: Initialize classifier $f _ { \eta _ { s } }$ for the stage $s ;$   
3: for $m = 1 , \cdots , M$ do   
4: Draw a mini-batch training data B from $\mathcal { D } _ { s } \dot { , }$   
5: Calculate logits $h ^ { s } ( x ) = \overline { { f } } _ { \eta _ { s } } ( f _ { \theta } ( x ) ) ;$   
6: $\mathcal { L } _ { t o t a l } ^ { s }$   
7: Update $\eta _ { s } \mathrm { b y } \eta _ { s } \gets \eta _ { s } - \epsilon \rVert \eta _ { s } \mathcal { L } _ { t o t a l } ^ { s } ;$

#

9: if $s > 1$ then

10: for t  do   
11: Extract Helmholtz free energy $- \mathcal { F } _ { T } ^ { s } ( x )$ by $\operatorname { E q . 9 ; }$   
12: Calculate stage identification by s⇤ $\begin{array} { r l } { s ^ { * } } & { { } = } \end{array}$ $\mathrm { a r g m a x } _ { s \in \zeta } ( - \bar { \mathcal { F } } _ { T } ^ { s } ( x ) ) ;$ ;   
13: Calculate stage identification accuracy $A C C _ { t }$ of temperature t by $\sum ( s ^ { * } = = s )$ ;   
14: end for   
15: $\Omega  \mathrm { a r g m a x } _ { t \in \Psi } A C C _ { t } ;$   
16: end if   
17: Return the model parameters $\eta _ { s }$   
18: end for

# Voting with Stage-Cumulative Temperatures

As we have already normalized the Helmholtz free energy with the fixed anchor (Eq. 7), taking the negative Helmholtz free energy as the confidence score is a natural choice:

$$
H ^ {s} (x) = - \mathcal {F} _ {T} ^ {s} (x) = T \log \sum_ {y \in \mathcal {Y} ^ {s}} \exp \left(h ^ {s} (x) [ y ] / T\right), \tag {9}
$$

which is the logsumexp of the logits with the control temperature parameter T . Previous energy-based out-ofdistribution detection methods (Wang et al. 2022a; Liu et al. 2020) have shown that the in-distribution data usually has a lower free energy (higher confidence scores) than the outof-distribution data for a certain classifier. Further aided by the energy self-normalization objective function, we can approximately derive that the right stage classifier for the instage data shall have the highest confidence score among all classifiers (Eq. 1). The derivation can be briefly expressed

# Algorithm 2: Inference

0: Given components: Pre-trained backbone $f _ { \theta } ,$ stage classifiers $\{ \bar { f } _ { \eta _ { s } } \} _ { s = 1 } ^ { S }$ ✓, temperature pool ⌦, total stage number $S ;$   
1: Input: Test example $x ;$   
2: Calculate image feature $l ( x ) = f _ { \theta } ( x ) ;$   
3: for $s = 1 , \cdots , S$ do   
4: Generate s-th logits $h ^ { s } ( x ) = f _ { \eta _ { s } } ( l ( x ) ) \colon$   
5: for $t \in \Omega$ do   
6: Calculate scaled energy $- \mathcal { F } _ { T } ^ { s } ( x )$ by Eq. 9;   
7: end for   
8: end for   
9: Voting for stage identification $s ^ { * }$ by Eq.10;   
10: Return final prediction $y ^ { * }$ by Eq. 2.

as $H ^ { i } ( x ^ { i } ) ~ = ~ H ^ { j } ( x ^ { j } ) , H ^ { j } ( x ^ { j } ) ~ > ~ H ^ { j } ( x ^ { i } ) ~  ~ H ^ { i } ( x ^ { i } ) ~ >$ $H ^ { j } ( x ^ { i } )$ , where $x ^ { i }$ is the in-stage data of the i-th stage but the out-stage data of the j-th stage. However, this derivation only approximately hold, we further propose a stagecumulative temperature calibration strategy with a voting inference augmentation to further optimize the maximum confidence criterion (Eq. 1) without overfitting the newest stage’s data.

As shown in Eq. (5), we can adjust the free energy by changing the temperature parameter T . Theoretically, we can find out the optimal temperature T for each classifier by optimizing the stage-ID prediction accuracy with all stages’ data, which is not possible in rehearsal-free incremental learning. As we can only access the current stage’s data, we propose a stage-cumulative strategy to avoid overfitting.

Firstly, we find out the optimal temperature only with the current stage’s training data by traversing the candidate temperatures and choosing the one with the best stage-ID prediction accuracy of the current stage. Secondly, we add this temperature to the final temperature pool denoted as ⌦. Finally, we can traverse temperatures in the temperature pool ⌦, and then aggregate stage-ID predictions under different temperatures by voting. To keep the fairness and the comparability between different classifiers, we simultaneously change the temperature for all classifiers, and do voting as Eq. 10.

$$
s ^ {*} = \operatorname {M O D E} \left( \right.\left\{ \right.\underset {s \in \zeta} {\operatorname {a r g m a x}} - \mathcal {F} _ {T} ^ {s} (x) \left. \right| \text {F o r} T \in \Omega \left. \right\}\left. \right), \tag {10}
$$

where MODE(·) is the mode operator to find the most frequent element in a collection. This voting-based inference augmentation strategy only increases negligible computation overhead. After the logits predicted by the model by once, we only need to recalculate Eq. (9) under different T .

Our augmented inference algorithm is introduced in Alg. 2, and the stage-cumulative temparature calibration is already introduced in Alg. 1.

# Experiments

# Benchmarks and implementation

We conduct extensive experiments to evaluate the proposed ESN. We consider two main incremental learning scenar-

ios: (1) class-incremental learning where classes are generally from the same domain ; (2) domain-incremental learning where classes are the same but from different domains. Moreover, we consider a more general scenario: the crossdomain class incremental learning, where different classes from diverse domains. And build a benchmark, named as Split DomainNet, for this scenario.

We evaluate ESN on CIFAR-100 (Krizhevsky, Hinton et al. 2009), Split DomainNet, 5-datasets (Ebrahimi et al. 2020) and CORe50 (Lomonaco and Maltoni 2017).

Split DomainNet Benchmark We build the cross-domain incremental learning benchmark, Split DomainNet, based on DomainNet (Peng et al. 2019). The Split DomainNet is the scenerio that incoming data of each stage contains images of new categories from different domains. We construct this dataset as a benchmark for the cross-domain class incremental learning, which we believe is a more challenging and practical scenario. DomainNet collects images of 345 common objects from 6 diverse domains including Clipart, Real, Sketch, Infograph, Painting and Quickdraw. Because some domains and categories in DomainNet contain few instances (even without a single instance), we select the top 200 categories with the most images. We split the 200 classes randomly into ten stages with 20 classes per stage. Instances of each stage come from a randomly selected domain.

Split-CIFAR100 Benchmark CIFAR-100 (Krizhevsky, Hinton et al. 2009) is a widely used benchmark for classincremental learning. Split CIFAR-100 splits the origin CIFAR-100 into 10 sessions and each session has 10 classes.

5-Datasets Benchmark 5-Datasets (Ebrahimi et al. 2020) is a benchmark for class incremental learning. Although each dataset in 5-Datasets is not difficult, it is still a challenging benchmark for pre-trained models, because there are slight similarity between them.

CORe50 Benchmark CORe50 (Lomonaco and Maltoni 2017) is a large benchmark for continual object recognition. This dataset collects images of 50 different objects from 11 distinct domains (8 indoor and 3 outdoor). Three domains (3, 7, and 10) are selected as test set, and the remaining 8 domains are used for incremental learning. CORe50 is a benchmark for domain-incremental learning.

Evaluation Metrics. We use the Final Average Accuracy (FAA) and Final Forgetting (FF) as evaluation metrics for class-incremental learning and cross-domain task incremental learning, which are widely used in previous works (Mai et al. 2022). There is no distinct task boundary for Domainincremental learning, and we use the Final Average Accuracy (FAA).

Comparison Methods. We compare ESN against the state-of-the-art CIL and DIL methods. Though we are a rehearsal-free incremental learning method, we also consider rehearsal-based methods that need the buffer to store exemplars for a more fair comparison. Comparison methods are EWC (Kirkpatrick et al. 2017), LwF (Li and Hoiem 2017) ER (Chaudhry et al. 2019), GDumb (Prabhu, Torr, and Dokania 2020), BiC (Wu et al. 2019), DER++ (Buzzega et al. 2020) and Co2L (Cha, Lee, and Shin 2021), as well as the recently published transformer-based methods L2P (Wang et al. 2022b) and DyTox (Douillard et al. 2022).

<table><tr><td>Method</td><td>Buffer size</td><td>FAA (↑)</td><td>FF (↓)</td></tr><tr><td>ER</td><td></td><td>67.87±0.57</td><td>33.33±1.28</td></tr><tr><td>BiC</td><td></td><td>66.11±1.76</td><td>35.24±1.64</td></tr><tr><td>GDumb</td><td>1000</td><td>67.14±0.37</td><td>-</td></tr><tr><td>DER++</td><td></td><td>61.06±0.87</td><td>39.87±0.99</td></tr><tr><td>Co2L</td><td></td><td>72.15±1.32</td><td>28.55±1.56</td></tr><tr><td>DyTox</td><td></td><td>77.61±0.92</td><td>8.26±0.38</td></tr><tr><td>ER</td><td></td><td>82.53±0.17</td><td>16.46±0.25</td></tr><tr><td>BiC</td><td></td><td>81.42±0.85</td><td>17.31±1.02</td></tr><tr><td>GDumb</td><td>5000</td><td>81.67±0.02</td><td>-</td></tr><tr><td>DER++</td><td></td><td>83.94±0.34</td><td>14.55±0.73</td></tr><tr><td>Co2L</td><td></td><td>82.49±0.89</td><td>17.48±1.80</td></tr><tr><td>DyTox</td><td></td><td>88.15±0.28</td><td>3.64±0.19</td></tr><tr><td>FT-seq</td><td></td><td>33.61±0.85</td><td>86.87±0.20</td></tr><tr><td>EWC</td><td></td><td>47.01±0.29</td><td>33.27±1.17</td></tr><tr><td>LwF</td><td>0</td><td>60.69±0.63</td><td>27.77±2.17</td></tr><tr><td>L2P</td><td></td><td>83.86±0.28</td><td>7.35±0.38</td></tr><tr><td>ESN</td><td></td><td>86.34±0.52</td><td>4.76±0.14</td></tr><tr><td>Upper-bound</td><td>-</td><td>91.27±0.18</td><td>-</td></tr></table>

Table 1: Results on Split CIFAR-100 for class-incremental learning. Bold: best rehearsal-free results. All results except ESN, DyTox, and Upper-bound are copied from (Wang et al. 2022b).

To compare fairly, we use the same ViT models pre-trained on ImageNet (i.e., ViT-B/16 (Dosovitskiy et al. 2021)) for all the competitors as well as ESN. We use the joint training result as the upper-bound for ESN on all benchmarks.

Implementation details. We implement our method in Py-Torch with two NVIDIA RTX 3090 GPUs. The proposed ESN is insensitive to hyper-parameters. We use the SGD optimizer and the cosine annealing learning rate scheduler with a initial learning rate of 0.01 all benchmarks. We use 30 epochs for Split CIFAR-100 and Split DomainNet, 10 epochs for 5-Datasets and Core50. We set the batch size of 128 for all experiments. Momentum and weight decay parameters are set to 0.9 and 0.0005, respectively. We use the ViT-B/16 pre-trained on ImageNet as backbone and the classifier is a class-attention block (CAB) (Touvron et al. 2021) with a linear projection. The hyper-parameters of CAB is the same as ViT-B/16 except the MLP ratio is 0.5, which has the parameters 3M. Due to the fact raw features extracted from pre-trained ViT are not suitable for all downstream tasks, we also add parameters (10 ⇥ 768) to the input, like (Jia et al. 2022). The candidate temperature set is from a range of numbers from 0.001 to 1.0 with step of 0.001. We set the energy anchor   =  10 and balance hyper-parameter   = 0.1 for all benchmarks. Code will be available soon.

# Comparison Results

We compare the proposed ESN with the state-of-the-arts on Split CIFAR-100, Split DomainNet, 5-Datasets and CORe50. We run ESN for 5 times with different random seeds and report the average results. For fair comparison, all methods start from the same ImageNet pre-trained ViT-B/16.

Results on Class-incremental learning benchmarks. Table 1 and Table 2 summarize the results on Split CIFAR-

<table><tr><td>Method</td><td>Buffer size</td><td>FAA (↑)</td><td>FF (↓)</td></tr><tr><td>ER</td><td></td><td>80.32±0.55</td><td>15.69±0.89</td></tr><tr><td>BiC</td><td></td><td>78.74±1.41</td><td>21.15±1.00</td></tr><tr><td>DER++</td><td>250</td><td>80.81±0.07</td><td>14.38±0.35</td></tr><tr><td>Co2L</td><td></td><td>82.25±1.17</td><td>17.52±1.35</td></tr><tr><td>ER</td><td></td><td>84.26±0.84</td><td>12.85±0.62</td></tr><tr><td>BiC</td><td></td><td>85.53±2.06</td><td>10.27±1.32</td></tr><tr><td>DER++</td><td>500</td><td>84.88±0.57</td><td>10.46±1.02</td></tr><tr><td>Co2L</td><td></td><td>86.05±1.03</td><td>12.28±1.44</td></tr><tr><td>FT-seq</td><td></td><td>20.12±0.42</td><td>94.63±0.68</td></tr><tr><td>EWC</td><td></td><td>50.93±0.09</td><td>34.94±0.07</td></tr><tr><td>LwF</td><td>0</td><td>47.91±0.33</td><td>38.01±0.28</td></tr><tr><td>L2P</td><td></td><td>81.14±0.93</td><td>4.64±0.52</td></tr><tr><td>ESN</td><td></td><td>85.71±1.47</td><td>2.85±0.61</td></tr><tr><td>Upper-bound</td><td>-</td><td>94.39±0.21</td><td>-</td></tr></table>

Table 2: Results on 5-Datasets for class-incremental learning. Bold: best rehearsal-free results. All results except ESN and Upper-bound are copied from (Wang et al. 2022b).

<table><tr><td>Method</td><td>Buffer size</td><td>FAA (↑)</td></tr><tr><td>ER</td><td></td><td>80.10±0.56</td></tr><tr><td>GDumb</td><td></td><td>74.92±0.25</td></tr><tr><td>BiC</td><td rowspan="2">50/class</td><td>79.28±0.30</td></tr><tr><td>DER++</td><td>79.70±0.44</td></tr><tr><td>Co2L</td><td></td><td>79.75±0.84</td></tr><tr><td>DyTox</td><td></td><td>79.21±0.10</td></tr><tr><td>L2P</td><td></td><td>81.07±0.13</td></tr><tr><td>EWC</td><td></td><td>74.82±0.60</td></tr><tr><td>LwF</td><td rowspan="2">0</td><td>75.45±0.40</td></tr><tr><td>L2P</td><td>78.33±0.06</td></tr><tr><td>ESN</td><td></td><td>91.80±0.31</td></tr><tr><td>Upper-bound</td><td>-</td><td>92.50±0.11</td></tr></table>

Table 3: Results on CORe50 for domain-incremental learning, in terms of final test accuracy. Bold: best rehearsal-free results. All results except ESN, DyTox, and Upper-bound are copied from (Wang et al. 2022b).

100 and 5-Datasets benchmarks respectively. ESN achieves state-of-the-art performance without any rehearsal buffer in terms of average accuracy and forgetting. We compute that ESN obtains a considerable relative improvement (an average of roughly 3.5%) over the best rehearsal-free methods. We can see that most rehearsal-based methods significantly improve by storing more data. That shows that rehearsalbased methods’ performances highly depend on buffer size. The outstanding performance of ESN indicates that the proposed anchor-based energy self-normalization can successfully aggregate all stage classifiers impartially. And thus can get outstanding performance even without rehearsal buffer.

Results on Domain-incremental learning benchmarks. Table 3 summarizes the results on the CORe50 benchmark. CORe50 is a challenging DIL benchmark that uses 8 domains as train set and 3 domains as test set. That means test images do not belong to any training domains, and this benchmark mainly tests the generalization ability after incremental learning. ESN achieves the best performance compared with other methods (about 17% improvements over

Table 4: Results on Split DomainNet for cross-domain classincremental learning. Bold: best rehearsal-free results.   

<table><tr><td>Method</td><td>Buffer size</td><td>FAA (↑)</td><td>FF (↓)</td></tr><tr><td>ER</td><td></td><td>64.54±1.06</td><td>28.21±0.45</td></tr><tr><td>BiC</td><td>250</td><td>66.99±1.27</td><td>19.91±0.23</td></tr><tr><td>DER++</td><td></td><td>70.18±0.37</td><td>21.31±0.55</td></tr><tr><td>DyTox</td><td></td><td>77.16±0.72</td><td>6.88±0.31</td></tr><tr><td>ER</td><td></td><td>70.90±1.35</td><td>21.49±0.61</td></tr><tr><td>BiC</td><td>500</td><td>68.19±1.22</td><td>21.76±0.39</td></tr><tr><td>DER++</td><td></td><td>74.61±0.27</td><td>16.65±0.94</td></tr><tr><td>DyTox</td><td></td><td>79.6±0.91</td><td>5.87±0.20</td></tr><tr><td>Finetune</td><td></td><td>35.66±2.73</td><td>59.89±2.05</td></tr><tr><td>EWC</td><td></td><td>22.35±1.86</td><td>76.11±1.28</td></tr><tr><td>LwF</td><td>0</td><td>28.86±1.92</td><td>64.91±1.01</td></tr><tr><td>L2P</td><td></td><td>45.65±0.82</td><td>15.26±0.51</td></tr><tr><td>ESN</td><td></td><td>68.76±0.12</td><td>5.75±0.23</td></tr><tr><td>Upper-bound</td><td>-</td><td>82.53±0.44</td><td>-</td></tr></table>

L2P) with the same ViT-B/16 pre-trained backbone. Since there is no correct stage-ID for test images (no domain overlap), the accuracy of ESN comes from the ensemble voting strategy.

Results on Cross-Domain Class-incremental learning benchmark. Cross-Domain Class-incremental learning is a more challenging scenario than traditional CIL settings. As shown in Table 4, ESN out-performs all other rehearsalfree methods a large margin (about 50% improvement). We can see that most class incremental learning algorithms fail to prevent catastrophic forgetting in the cross-domain setting to a great extent, as indicated by high final forgetting (FF) shown in Table 4. Specially, some regularization-based methods, LwF and EWC, even perform worse than simply finetuning. That is probably due to some regularization are not robust to large domain shift. Our stage isolation learning strategy can preserve old knowledge successfully. And the proposed anchor-based energy self-normalization strategy is robust to handle this challenging scenario.

# Ablation Study

The effect of related components. To further study the effectiveness of ESN, we study the effect of our main components in Table 5. Table 5 (row 1) removes the proposed anchor-based energy self-normalization strategy $\bar { \mathcal { L } } _ { a l } ^ { s } ,$ , and keeps the other parts the same. The performance has a significant drop, suggesting that aligning all isolated classifiers to the same energy plane is the key issue in aggregating them impartially for final prediction. Table 5 (row 2) removes our proposed temperature selection strategy, and just using the default temperature 1 without voting for prediction. The results is slightly lower than ESN. The decrease suggests that using the proposed temperature calibration can further boost the performance. Table 5 (row 3) shares the same classattention block (CAB) across tasks. As the result shows, parameter isolation is important in tackling catastrophic forgetting and maintaining performance.

The effect of different  .   is the main hyper-parameter of our proposed energy self-normalization loss, and we conduct an ablation study to investigate its effect. Table 6 shows

Table 5: Ablation studies of the effect of related components. The experiments are performed on Split CIFAR-100.   

<table><tr><td>Ablated components</td><td>FAA (↑)</td><td>FF (↓)</td></tr><tr><td>w/o energy self-normalization</td><td>80.21</td><td>9.35</td></tr><tr><td>w/o temperature calibration</td><td>85.73</td><td>4.88</td></tr><tr><td>w/o parameter isolation</td><td>83.94</td><td>6.42</td></tr><tr><td>None</td><td>86.34</td><td>4.76</td></tr></table>

Table 6: The effect of the energy anchor  . The experiments are performed on Split CIFAR-100.   

<table><tr><td>Energy Anchor Δ</td><td>0</td><td>-1</td><td>-3</td><td>-5</td><td>-10</td><td>-15</td></tr><tr><td>FAA (↑)</td><td>85.96</td><td>85.60</td><td>85.59</td><td>86.20</td><td>86.34</td><td>86.25</td></tr><tr><td>FF (↓)</td><td>5.08</td><td>5.21</td><td>5.56</td><td>4.59</td><td>4.76</td><td>4.98</td></tr></table>

the final results (FAA and FF) is insensitive to the value of  . That is probably because the most important thing is to normalize all classifiers to the same energy plane.

The effect of different network architectures. In the main experiments, we mainly attach a class-attention block as a decoder to the pre-trained backbone. We point out that other network architectures can also use our proposed energy selfnormalization method. Table 7 summarizes the results of using different architectures. Here, we add two parameter isolation methods to demonstrate our idea: VPT (Jia et al. 2022) and DER (Yan, Xie, and He 2021). VPT uses a small amount of task-specific learnable parameters into the input while freezing the other parts of the model to tune a pre-trained model to downstream tasks. DER expands a new network for each new coming task. The network can be any type, and we use both ResNet50 and ViT-B/16 for experiments. We report the amount of expansion parameters for a single incremental stage in the Table 7. Though the amount of expansion parameters of VPT is significantly less than CAB, VPT needs almost ten times inference time than CAB. That is because CAB works as a stage-specific decoder and uses a shared backbone to extract image features, which can decrease the computational expense. DER-like methods have the same inference speed problem and perform worse than VPT and CAB. The worse performance of DER-like methods is probably because training large models on a small subset of a dataset has severe over-fitting.

Table 7: Ablation studies of different network architectures. The experiments are performed on Split CIFAR-100.   

<table><tr><td rowspan="2">Method</td><td colspan="2">Expansion Parameters</td><td rowspan="2">FAA (↑)</td><td rowspan="2">FF (↓)</td></tr><tr><td>M</td><td>Relative increase (%)</td></tr><tr><td>DER-ViT</td><td>86.6</td><td>100</td><td>83.43</td><td>5.52</td></tr><tr><td>DER-ResNet50</td><td>25.3</td><td>100</td><td>80.37</td><td>9.2</td></tr><tr><td>VPT</td><td>0.2</td><td>0.2</td><td>85.55</td><td>4.98</td></tr><tr><td>CAB</td><td>3.0</td><td>3.4</td><td>86.34</td><td>4.76</td></tr></table>

# Conclusion

This paper proposes a novel a rehearsal-free stage-isolation based general incremental learning framework. The proposed ESN learns stage-isolation classifiers for each stage, and uses then anchor-based energy self-normalization strategy to aggregate multiple isolated classifiers in an impartial way. Furthermore, we propose a control parameter (temperature) finding method and propose a voting based inference augmentation strategy for robust inference. Our experiments show that our method outperforms the current state-of-theart on four large benchmarks by a large margin and can handle general incremental learning scenarios.

# Acknowledgements

This work is funded by the National Key Research and Development Project of China (2019YFB1312000), the National Natural Science Foundation of China (62076195, 62206271, and U20B2052), the Fundamental Research Funds for the Central Universities (AUGA5710011522), and the Guangdong Basic and Applied Basic Research Foundation (2020B1515130004). This work is also supported by the Singapore Ministry of Education (MOE) Academic Research Fund (AcRF) Tier 1 grant (MSS21C002).

# References

Al Rahhal, M. M.; Bazi, Y.; Al-Dayil, R.; Alwadei, B. M.; Ammour, N.; and Alajlan, N. 2022. Energy-based learning for open-set classification in remote sensing imagery. International Journal of Remote Sensing, 1–11. 3   
Buzzega, P.; Boschini, M.; Porrello, A.; Abati, D.; and Calderara, S. 2020. Dark experience for general continual learning: a strong, simple baseline. NeurIPS. 5   
Cha, H.; Lee, J.; and Shin, J. 2021. Co2l: Contrastive continual learning. In ICCV. 5   
Chaudhry, A.; Rohrbach, M.; Elhoseiny, M.; Ajanthan, T.; Dokania, P. K.; Torr, P. H.; and Ranzato, M. 2019. On tiny episodic memories in continual learning. arXiv preprint arXiv:1902.10486. 5   
De Lange, M.; Aljundi, R.; Masana, M.; Parisot, S.; Jia, X.; Leonardis, A.; Slabaugh, G.; and Tuytelaars, T. 2021. A continual learning survey: Defying forgetting in classification tasks. IEEE transactions on pattern analysis and machine intelligence, 44(7): 3366–3385. 1, 2, 3   
Dong, S.; Hong, X.; Tao, X.; Chang, X.; Wei, X.; and Gong, Y. 2021. Few-shot class-incremental learning via relation knowledge distillation. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 35, 1255–1263. 2   
Dosovitskiy, A.; Beyer, L.; Kolesnikov, A.; Weissenborn, D.; Zhai, X.; Unterthiner, T.; Dehghani, M.; Minderer, M.; Heigold, G.; Gelly, S.; Uszkoreit, J.; and Houlsby, N. 2021. An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale. ICLR. 2, 6   
Douillard, A.; Rame, A.; Couairon, G.; and Cord, M. 2022. ´ Dytox: Transformers for continual learning with dynamic

token expansion. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 9285– 9295. 2, 5   
Du, Y.; and Mordatch, I. 2019. Implicit generation and modeling with energy based models. Advances in Neural Information Processing Systems, 32. 3   
Ebrahimi, S.; Meier, F.; Calandra, R.; Darrell, T.; and Rohrbach, M. 2020. Adversarial continual learning. In European Conference on Computer Vision, 386–402. Springer. 5   
Fort, S.; Ren, J.; and Lakshminarayanan, B. 2021. Exploring the limits of out-of-distribution detection. Advances in Neural Information Processing Systems, 34: 7068–7081. 2   
Grathwohl, W.; Wang, K.-C.; Jacobsen, J.-H.; Duvenaud, D.; Norouzi, M.; and Swersky, K. 2019. Your classifier is secretly an energy based model and you should treat it like one. arXiv preprint arXiv:1912.03263. 4   
Hendrycks, D.; Basart, S.; Mazeika, M.; Mostajabi, M.; Steinhardt, J.; and Song, D. 2019. Scaling out-ofdistribution detection for real-world settings. arXiv preprint arXiv:1911.11132. 4   
Hou, S.; Pan, X.; Loy, C. C.; Wang, Z.; and Lin, D. 2019. Learning a unified classifier incrementally via rebalancing. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 831–839. 1   
Jia, M.; Tang, L.; Chen, B.-C.; Cardie, C.; Belongie, S.; Hariharan, B.; and Lim, S.-N. 2022. Visual Prompt Tuning. In European Conference on Computer Vision (ECCV). 3, 6, 7   
Joseph, K.; Khan, S.; Khan, F. S.; Anwer, R. M.; and Balasubramanian, V. N. 2022. Energy-based Latent Aligner for Incremental Learning. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 7452–7461. 2, 3   
Kirkpatrick, J.; Pascanu, R.; Rabinowitz, N.; Veness, J.; Desjardins, G.; Rusu, A. A.; Milan, K.; Quan, J.; Ramalho, T.; Grabska-Barwinska, A.; et al. 2017. Overcoming catastrophic forgetting in neural networks. Proceedings of the national academy of sciences, 114(13): 3521–3526. 2, 5   
Knoblauch, J.; Husain, H.; and Diethe, T. 2020. Optimal continual learning has perfect memory and is np-hard. In ICML. 1   
Krizhevsky, A.; Hinton, G.; et al. 2009. Learning multiple layers of features from tiny images. 5   
LeCun, Y.; Chopra, S.; Hadsell, R.; Ranzato, M.; and Huang, F. 2006. A tutorial on energy-based learning. Predicting structured data, 1(0). 2, 3, 4   
Li, X.; Zhou, Y.; Wu, T.; Socher, R.; and Xiong, C. 2019. Learn to grow: A continual structure learning framework for overcoming catastrophic forgetting. In International Conference on Machine Learning, 3925–3934. PMLR. 2   
Li, Z.; and Hoiem, D. 2017. Learning without forgetting. IEEE transactions on pattern analysis and machine intelligence, 40(12): 2935–2947. 2, 5   
Liu, W.; Wang, X.; Owens, J.; and Li, Y. 2020. Energy-based out-of-distribution detection. Advances in Neural Information Processing Systems, 33: 21464–21475. 3, 4

Liu, Y.; Hong, X.; Tao, X.; Dong, S.; Shi, J.; and Gong, Y. 2022. Model Behavior Preserving for Class-Incremental Learning. IEEE Transactions on Neural Networks and Learning Systems. 2   
Lomonaco, V.; and Maltoni, D. 2017. Core50: a new dataset and benchmark for continuous object recognition. In Conference on Robot Learning, 17–26. PMLR. 5   
Mai, Z.; Li, R.; Jeong, J.; Quispe, D.; Kim, H.; and Sanner, S. 2022. Online continual learning in image classification: An empirical survey. Neurocomputing, 469: 28–51. 1, 2, 3, 5   
Peng, X.; Bai, Q.; Xia, X.; Huang, Z.; Saenko, K.; and Wang, B. 2019. Moment matching for multi-source domain adaptation. In Proceedings of the IEEE International Conference on Computer Vision, 1406–1415. 5   
Prabhu, A.; Torr, P. H.; and Dokania, P. K. 2020. Gdumb: A simple approach that questions our progress in continual learning. In ECCV. 5   
Riemer, M.; Cases, I.; Ajemian, R.; Liu, M.; Rish, I.; Tu, Y.; and Tesauro, G. 2018. Learning to Learn without Forgetting by Maximizing Transfer and Minimizing Interference. In ICLR. 1   
Serra, J.; Suris, D.; Miron, M.; and Karatzoglou, A. 2018. Overcoming catastrophic forgetting with hard attention to the task. In International Conference on Machine Learning, 4548–4557. PMLR. 2   
Shin, H.; Lee, J. K.; Kim, J.; and Kim, J. 2017. Continual learning with deep generative replay. Advances in neural information processing systems, 30. 2   
Tang, K.; Miao, D.; Peng, W.; Wu, J.; Shi, Y.; Gu, Z.; Tian, Z.; and Wang, W. 2021. CODEs: Chamfer Out-of-Distribution Examples against Overconfidence Issue. In Proceedings of the IEEE/CVF International Conference on Computer Vision, 1153–1162. 3   
Tao, X.; Chang, X.; Hong, X.; Wei, X.; and Gong, Y. 2020. Topology-preserving class-incremental learning. In European Conference on Computer Vision, 254–270. Springer. 2   
Touvron, H.; Cord, M.; Sablayrolles, A.; Synnaeve, G.; and Jegou, H. 2021. Going deeper with image transformers. In ´ Proceedings of the IEEE/CVF International Conference on Computer Vision, 32–42. 3, 6   
Wang, H.; Li, Z.; Feng, L.; and Zhang, W. 2022a. ViM: Out-Of-Distribution with Virtual-logit Matching. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 4921–4930. 4   
Wang, Y.; Huang, Z.; and Hong, X. 2022. S-Prompts Learning with Pre-trained Transformers: An Occam’s Razor for Domain Incremental Learning. In Conference on Neural Information Processing Systems (NeurIPS). 2   
Wang, Y.; Ma, Z.; Huang, Z.; Wang, Y.; Su, Z.; and Hong, X. 2023. Isolation and Impartial Aggregation: A Paradigm of Incremental Learning without Interference. In the Proceedings of the 37th AAAI Conference on Artificial Intelligence (AAAI 2023). 1

Wang, Z.; Zhang, Z.; Lee, C.-Y.; Zhang, H.; Sun, R.; Ren, X.; Su, G.; Perot, V.; Dy, J.; and Pfister, T. 2022b. Learning To Prompt for Continual Learning. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 139–149. 2, 5, 6   
Wu, Y.; Chen, Y.; Wang, L.; Ye, Y.; Liu, Z.; Guo, Y.; and Fu, Y. 2019. Large scale incremental learning. In CVPR. 5   
Xie, J.; Yan, S.; and He, X. 2022. General Incremental Learning with Domain-aware Categorical Representations. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 14351–14360. 2   
Xu, H.; and Zhang, J. 2020. Aanet: Adaptive aggregation network for efficient stereo matching. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 1959–1968. 2   
Yan, S.; Xie, J.; and He, X. 2021. Der: Dynamically expandable representation for class incremental learning. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 3014–3023. 2, 7   
Zhang, X.; Dong, S.; Chen, J.; Tian, Q.; Gong, Y.; and Hong, X. 2022. Deep Class-Incremental Learning From Decentralized Data. IEEE Transactions on Neural Networks and Learning Systems, 1–14. 2   
Zhao, B.; Chen, C.; Xiao, X.; Ju, Q.; and Xia, S. 2022. Energy Alignment for Bias Rectification in Class Incremental Learning. In ICASSP 2022-2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 3513–3517. IEEE. 3