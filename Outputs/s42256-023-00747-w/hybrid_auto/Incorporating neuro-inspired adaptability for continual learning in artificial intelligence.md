---
title: "Incorporating neuro-inspired adaptability for continual learning in artificial intelligence"
authors:
  - "Liyuan Wang"
  - "Xingxing Zhang"
  - "Qian Li"
  - "Mingtian Zhang"
  - "Hang Su"
  - "Jun Zhu"
  - "Yi Zhong"
date: "2022-01-01"
year: "2022"
journal: "Nature Machine Intelligence"
abstract: "Continual learning aims to empower artificial intelligence with strong adaptability\\"
abstract_cn: "持续学习旨在赋予人工智能对现实世界变化的强适应性，同时避免灾难性遗忘。生物学习系统通过主动遗忘与稳定性保护等机制实现强适应性。本文分析了生物持续学习的关键功能因素，提出基于元可塑性与参数隔离的方法，在多种持续学习场景中取得最先进的整体性能，展现出优异通用性。"
keywords:
  - "[[Continual learning]]"
  - "[[Catastrophic forgetting]]"
  - "[[Meta-plasticity]]"
  - "[[Neural network]]"
  - "[[Adaptability]]"
cite: "Wang L Y, Zhang X X, Li Q, et al. Incorporating neuro-inspired adaptability for continual\\"
aiSum: "元可塑性+参数隔离方法，解决持续学习灾难性遗忘，多场景SOTA整体性能。"
confidence: "high"
wiki_concepts:
  - "[[Catastrophic forgetting]]"
  - "[[Continual learning]]"
  - "[[Neural network]]"
---

Received: 3 October 2022

Accepted: 26 September 2023

Published online: 16 November 2023

![](images/331effc6af3fdfc24ce261342a3cee144bc67bd8466d287e74e929cffce51b41.jpg)

Check for updates

Liyuan Wang  1,2,3,5, Xingxing Zhang1,5, Qian Li2,3, Mingtian Zhang4 , Hang Su1 , Jun Zhu  1 & Yi Zhong  2,3

Continual learning aims to empower artifcial intelligence with strong adaptability to the real world. For this purpose, a desirable solution should properly balance memory stability with learning plasticity, and acquire sufcient compatibility to capture the observed distributions. Existing advances mainly focus on preserving memory stability to overcome catastrophic forgetting, but it remains difcult to fexibly accommodate incremental changes as biological intelligence does. Here, by modelling a robust Drosophila learning system that actively regulates forgetting with multiple learning modules, we propose a generic approach that appropriately attenuates old memories in parameter distributions to improve learning plasticity, and accordingly coordinates a multi-learner architecture to ensure solution compatibility. Through extensive theoretical and empirical validation, our approach not only enhances the performance of continual learning, especially over synaptic regularization methods in task-incremental settings, but also potentially advances the understanding of neurological adaptive mechanisms.

Continual learning, also known as lifelong learning, provides the foundation for artificial intelligence (AI) systems to accommodate real-world changes. As the external environment tends to be highly dynamic and unpredictable, an intelligent agent needs to learn and remember throughout its lifetime1–3 . Numerous efforts have been devoted to preserving memory stability to mitigate catastrophic forgetting in artificial neural networks, where parameter changes for effective learning of a new task usually result in a dramatic performance drop of the old tasks4–6 . Representative strategies include selectively stabilizing parameters7–11, recovering old data distributions12–14, allocating dedicated parameter subspaces15,16 and so on. However, they usually achieve only modest improvements in specific scenarios, with effectiveness varying widely across experimental settings (such as differences in task type and similarity, input size, number of training samples and so on)2,3,17. As a result, there remains a huge gap between existing advances and realistic applications.

To overcome this limitation, we theoretically analyse the key factors on which continual learning performance depends, suggesting a broader objective beyond the current focus. Specifically, to perform well on all tasks ever seen, a desirable solution should properly balance memory stability of old tasks with learning plasticity of new tasks, while being adequately compatible to capture their distributions (see Methods for details). For example, if you want to accommodate a sequence of cakes (that is, incremental tasks) into a bag (that is, a solution), you should optimize the efficiency of space allocation for each cake as well as the total space of the bag, rather than simply freezing the old cakes.

As biological learning systems are natural continual learners that show strong adaptability to real-world changes2,3,18, we argue that they have been equipped with effective strategies to address the above challenges. In particular, the γ subset of the Drosophila mushroom body (γMB) is a biological learning system that is essential for coping with different tasks in succession and enjoys relatively

1 Department of Computer Science and Technology, Institute for AI, BNRist Center, Tsinghua-Bosch Joint ML Center, THBI Lab, Tsinghua University, Beijing, China. 2 School of Life Sciences, IDG/McGovern Institute for Brain Research, Tsinghua University, Beijing, China. 3 Tsinghua-Peking Center for Life Sciences, Beijing, China. 4 Centre for Artificial Intelligence, University College London, London, UK. 5 These authors contributed equally: Liyuan Wang, Xingxing Zhang.  e-mail: dcszj@tsinghua.edu.cn; zhongyithu@tsinghua.edu.cn

![](images/3f6168e672babf9173595ff3b54ca7438772d854b57896b9927a5e93bb85e404.jpg)

![](images/2d83ce412c165dbf434bc21cfc4dd95ed589c3783b3639658d2d02821fb9f7fb.jpg)

![](images/d201701ec3e134cefba46ef5a68302f04b4bdbec6bf55a817b10e6a29a4e80e5.jpg)  
Adaptation and survival in real-world changes   
Fig. 1 | Continual learning with reference to a biological learning system. a, The Drosophila γMB system has evolved adaptive mechanisms to cope with different tasks in succession, such as selective stabilization of synaptic changes, active regulation of memory decay (that is, active forgetting) and dynamic coordination of multiple parallel compartments (that is, γ1–γ5). KCs, Kenyon cells; DANs, dopaminergic neurons; MBONs, mushroom body output neurons. b, Inspired by such biological strategies, we propose to incorporate active   
forgetting together with stability protection for a better trade-off between new and old tasks, and accordingly coordinate multiple parallel continual learners to ensure solution compatibility. L –L , five continual learners corresponding to the five compartments. The dashed areas on the lower right denote the target distributions of L –L , and the small hollow circles represent the optimal solution for each incremental task (tasks A, B and C are coloured, and other tasks are grey). The schematic under panels a and b represents the connection between AI and BI.

clear and in-depth understanding at both functional and anatomical levels19–26 (Fig. 1a), which emerges as an excellent source for inspiring continual learning in AI.

As a key functional advantage, the γMB system can regulate memories in distinct ways to optimize memory-guided behaviours in changing environments19,25,27–31. First, old memories are actively protected from new disruption by strengthening the previously learned synaptic changes29,31. This idea of selectively stabilizing parameters has been widely used to alleviate catastrophic forgetting in continual learning7–10. Besides, old memories can be actively forgotten for better adapting to a new memory19,25,28,32. There are specialized molecular signals to regulate the speed of memory decay30,33, whose activation reduces the persistence of outdated information, while inhibition shows the opposite effect19,25,28,32. However, the benefits of active forgetting for continual learning remain to be explored3 . Here we propose a functional strategy that incorporates active forgetting together with stability protection for a better trade-off between new and old tasks, where the active forgetting part is formulated as appropriately attenuating old memories in parameter distributions and optimized by a synaptic expansion-renormalization process. Without compromising old tasks, our proposal can greatly enhance the performance of new tasks by eliminating the past conflicting information.

We further explore the organizing principles of the γMB system that support its function, which employs five compartments (γ1–γ5) with dynamic modulations to perform continual learning in parallel20–24. As shown in Fig. 1a, the sensory information is incrementally input from Kenyon cells, while the valence is conveyed by dopaminergic neurons21,34,35. The outputs of these compartments are carried by distinct MB output neurons and integrated in a weighted-sum fashion to guide adaptive behaviours22,34,35. In particular, the dopaminergic neurons allow for distinct learning rules and forgetting rates in each compartment, where the latter has been shown important for processing sequential conflicting experiences24,36–39. Inspired by this, we design a specialized architecture of multiple parallel learning modules, which can ensure solution compatibility for incremental changes by coordinating the diversity of learners’ expertise. Interestingly, adaptive implementations of the proposed functional strategy can naturally

serve this purpose through adjusting the target distribution of each learner, suggesting that the neurological adaptive mechanisms are highly synergistic rather than operating in isolation.

Through satisfying the identified criteria, our approach shows superior generality across various continual learning benchmarks and achieves strong performance gains. We further cross-validate the computational model with biological findings, to better understand the underpinnings of real-world adaptability for both AI and biological intelligence (BI).

# Results

# Active forgetting with stability protection

A central challenge of continual learning is to resolve the mutual interference between new and old tasks due to their distribution differences. The functional advantages of the γMB system suggest that stability protection and active forgetting are both important19,25,27–31 (Fig. 1b), although current efforts mainly focus on the former to prevent catastrophic forgetting4,5 . Here we formulate this process with the framework of Bayesian learning, which has been hypothesized to well model biological synaptic plasticity by tracking the probability distribution of synaptic weights under dynamic sensory inputs40,41. We briefly describe a simple case of two tasks (Fig. 2a) and leave the full details to Methods.

Let’s consider a neural network with parameters θ continually learning tasks A and B from their training data $D _ { \mathsf { A } }$ and $D _ { \mathrm { { B } } }$ to perform well on their test data, which is called a ‘continual learner’. From a Bayesian perspective, the learner first places a prior distribution p(θ) on θ. After learning task A, the learner updates the belief of the parameters, resulting in a posterior distribution $p ( \theta | D _ { \mathrm { A } } ) \propto p ( D _ { \mathrm { A } } | \theta ) p ( \theta )$ ) that incorporates the knowledge of task A. Then, task A can be performed successfully by finding a mode of the posterior: $\theta _ { \mathrm { A } } ^ { * } = \arg \operatorname* { m a x } _ { \theta } \log p ( \theta | D _ { \mathrm { A } } )$ . For learning task B, $p ( \theta | D _ { \mathsf { A } } )$ becomes the prior and the posterior $p ( \theta | D _ { \mathrm { A } } , D _ { \mathrm { B } } ) \propto p ( D _ { \mathrm { B } } | \theta ) p ( \theta | D _ { \mathrm { A } } )$ will further incorporate the knowledge of task B. Similarly, the learner needs to find $\theta _ { \mathrm { A , B } } ^ { * } = { \arg \operatorname* { m a x } } _ { \theta } \log p ( \theta | D _ { \mathrm { A } } , D _ { \mathrm { B } } )$ , corresponding to maximizing A,B both log $p ( D _ { \mathsf { B } } | \theta )$ for learning task B and log $\mathbf { \nabla } _ { p ( \theta | D _ { A } ) }$ for remembering task A.

![](images/01699e90f3cc4d4e365dc190f3d982e8ce8288354c961d590ed5acfccc8f7d4a.jpg)

![](images/8105d29e1b24f47148fae399b9e8ab16615635d38ed7b8e17a466354c1ff4c8a.jpg)

![](images/df4700a2faee1a8bb1478af8b0a65cce0264c7f599e5a80798c840d88a1a05c8.jpg)

![](images/728cb8f56af51ca7ade1a670974caabf30eb840638465351e3edc81235c39b6e.jpg)  
Fig. 2 | Implementation of active forgetting in a continual learning model. a, Formulating active forgetting together with stability protection through a Bayesian learning framework. b, The proposed functional strategy can be optimized in two equivalent ways of synaptic expansion-renormalization (AF-1 and AF-2), where the network parameters θ need to be selectively renormalized with both $\theta _ { \mathrm { A } } ^ { * }$ and $\theta _ { \mathrm { e } }$ to balance new and old tasks mutually in a shared solution. c, Experimental results. The evaluation metrics include average accuracy for   
overall performance (top), forward transfer for learning plasticity (middle) and backward transfer for memory stability (bottom). Because of different construction principles, the overall knowledge transfer ranges from more negative to more positive across S-CIFAR-100, R-CIFAR-100 and R-CIFAR-10/100. All results are averaged over five runs with different random seeds and task orders. The error bars represent the standard error of the mean. d, Visualization of the latest task predictions on S-CIFAR-100 with Grad-CAM75.

However, due to the differences in data distribution, remembering old tasks precisely can increase the difficulty of learning each new task well. Inspired by the biological active forgetting, we introduce a forgetting rate β and replace $p ( \theta | D _ { \mathsf { A } } )$ with

$$
\hat {p} (\theta | D _ {\mathrm {A}}, \beta) = \frac {p (\theta | D _ {\mathrm {A}}) ^ {(1 - \beta)} p (\theta) ^ {\beta}}{Z}, \tag {1}
$$

where $p ( \theta )$ is a non-informative prior without incorporating old knowledge42. Z is $1 \beta \cdot$ dependent normalizer that keeps p a normalized ̂ probability distribution (Supplementary Section 1.1). p tends to forget ̂ task A when $\beta \to 1 ,$ , while be dominated by $p ( \theta | D _ { \mathsf { A } } )$ with full old knowledge when $\beta \to 0$ . For the new target $p ( \theta | D _ { \mathrm { A } } , D _ { \mathrm { B } } , \beta ) \propto p ( D _ { \mathrm { B } } | \theta ) \hat { p } ( \theta | D _ { \mathrm { A } } , \beta )$ , we derive the loss function

$$
\mathcal {L} _ {\mathrm {R e g}} ^ {\mathrm {A F}} (\theta) = \mathcal {L} _ {\mathrm {B}} (\theta) + \underbrace {\frac {\lambda_ {\mathrm {S P}}}{2} \sum_ {m} F _ {\mathrm {A} , m} \left(\theta_ {m} - \theta_ {\mathrm {A} , m} ^ {*}\right) ^ {2}} _ {\text {s t a b i l i t y p r o t e c t i o n}} + \underbrace {\frac {\lambda_ {\mathrm {A F}}}{2} \sum_ {m} I _ {\mathrm {e} , m} \left(\theta_ {m} - \theta_ {\mathrm {e} , m}\right) ^ {2}} _ {\text {a c t i v e f o r g e t t i n g}}. \tag {2}
$$

$\mathcal { L } _ { \mathrm { B } } ( \boldsymbol { \theta } )$ is the loss function of learning task B, and m denotes the index of parameters. $\lambda _ { \mathsf { S P } }$ and $\lambda _ { \mathrm { A F } }$ are hyperparameters that control the strengths of two regularizers responsible for stability protection and active forgetting, respectively. The stability protection part is to selectively penalize the deviance of each parameter $\theta _ { m }$ from $\theta _ { \mathbf { A } , m } ^ { * }$ depending on its ‘importance’ for old task(s), estimated by the A,mFisher information $F _ { \mathrm { A } , m } .$ .

The optimization of active forgetting can be achieved in two equivalent ways, that is, AF-1 and AF-2 (Fig. 2b). They both encourage the network parameters θ to renormalize with an ‘expanded’ set of

parameters $\theta _ { \epsilon }$ when learning task B. For $\mathbf { A F } { \cdot } 1 , \theta _ { \mathrm { e } , m } { = } 0$ is ‘empty’ with equal selectivity $\cdot I _ { \mathrm { e } , m } = 1$ 1 for renormalization, where the active-forgetting term becomes the L2 norm of θ. The hyperparameters $\lambda _ { \mathrm { A F } } \propto \beta$ and $\lambda _ { \mathtt { S P } } \propto 1 - \beta ,$ , indicating that the old memories are directly affected. For $\mathsf { A F } { \cdot } 2 , \theta _ { \mathrm { e } , m } = \theta _ { \mathrm { B } , m } ^ { * }$ is the optimal solution for task B only, obtained from optimizing $\mathcal { L } _ { \mathrm { B } } ( \boldsymbol { \theta } _ { \mathrm { e } } )$ , and $I _ { \mathrm { e } , m } = F _ { \mathrm { B } , m }$ is the Fisher information. The forgetting rate is fully integrated into $\lambda _ { \mathrm { A F } } \propto \beta / ( 1 - \beta )$ and is independent of $\dot { \lambda } _ { \mathsf { S P } } .$ In the absence of active forgetting $( \beta = 0 )$ , the loss function in equation (2) is left with only $\mathcal { L } _ { \mathrm { B } } ( \boldsymbol { \theta } )$ and the stability protection term, which is (approximately43) equivalent to regular synaptic regularization methods such as elastic weight consolidation (EWC7 ). In particular, as the loss functions of these methods7–10 typically have a similar form and differ only in the metric for estimating the parameter importance43 (equation (11) in Methods), our proposal can be naturally combined with them by plugging in the active-forgetting term.

For biological neural networks, active forgetting is able to remove outdated information and provide flexibility for adapting to a new memory19,27,28. This strategy is essential for Drosophila to cope with the interference of previous tasks19,28,29,44. Here we theoretically analyse how this benefit is achieved in our computational model. First, an appropriate forgetting rate β is able to improve the probability of learning each new task well through attenuating old memories in θ (equation (5) in Methods), which can be empirically determined by a grid search $\mathbf { o f } \lambda _ { \scriptscriptstyle \mathrm { A F } } \mathbf { a n d } / \mathbf { o r } \lambda _ { \scriptscriptstyle \mathrm { S P } } .$ Second, when θ moves to the neighbourhood of an empirical optimal solution, the active-forgetting term in equation (2) can minimize the upper bound of generalization errors for continual learning, especially for new tasks (Proposition 2 in Methods).

Now we evaluate the efficacy of active forgetting on three continual learning benchmarks for visual classification tasks. They are all

![](images/1a2a8052fa64159814cd1e73ee4e94cf2f77e890fc67d51eabd39dcb68562d50.jpg)

![](images/9795be9cd616dbe6a23cde7c2bcc2f35c249100087b12a6e56a0fb30f8a1ac6d.jpg)

![](images/5cd3a458c9a49212ea4e59d16176cd44ed9eb87aedd4554b8fbc29dd11b0df5f.jpg)

![](images/9954da28fa902250dc8aa4499c6c3555f3d422e6d77ba6c6dc479069a2c36355.jpg)

![](images/2a76fd32a21509ed76ecd9c5d7779273214604839b1af17778c64f91af1dca4c.jpg)

![](images/288abd955c74e0fef7b441f2ed0e4a6a12e85ee8bbfd71350bbc3d5c72bdc547.jpg)

![](images/434282783bee0711732a61ce1460f164920b1758dc7dddf3a2a24d420c50af6a.jpg)

![](images/b453fa5704800f009dd4d77dfa90531c33c537028c0b96a671ec8d4df482cf89.jpg)

![](images/a365469a69ee7affb3f7fd27a7b4c2fc7bc9499a8bca26742008811592389e64.jpg)  
Fig. 3 | The γMB-like architecture of MCL with adaptive modulations. a, Inspired by the organizing principles of the γMB system, we design a specialized architecture consisting of multiple parallel continual learners ${ \bf L } _ { 1 } \mathrm { - } { \bf L } _ { K } . { \bf b } .$ , Learner differences can be modulated by the forgetting rate β. Here we present an example with the target distribution $p ( \theta | D _ { \mathrm { A } } , D _ { \mathrm { B } } , \beta )$ when p(θ) = ? μ, σ2) and p(θ|DA) = ? μ + a, σ2) in p(̂ θ|DA, β) = p(θ|DA) (1−β) p(θ) β . I $\begin{array} { r } { p ( \theta ) = \mathcal { N } ( \mu , \sigma ^ { 2 } ) \mathrm { a n d } p ( \theta | D _ { \mathrm { A } } ) = \mathcal { N } ( \mu + a , \sigma ^ { 2 } ) \mathrm { i n } \hat { p } ( \theta | D _ { \mathrm { A } } , \beta ) = \frac { p ( \theta | D _ { \mathrm { A } } ) ^ { ( 1 - \beta ) } p ( \theta ) ^ { \beta } } { Z } . } \end{array}$ n Z this case, $p ( \theta | D _ { \mathrm { A } } , D _ { \mathrm { B } } , \beta )$ is also a Gaussian (Supplementary Section 1.1) and the vertical dashed line denotes its mode. c, A conceptual diagram of continual learning. A, B and C are three incremental tasks with different similarities. ${ \bf L } _ { 1 } { - \bf L } _ { 5 }$ are five learners with appropriate diversity in parameter space. The coloured   
hollow circles indicate the optimal solution for each task. d, Learners' expertise across tasks. After continual learning of all tasks, we evaluate the relative accuracy of each learner across tasks, calculated as the performance of each learner minus the average performance of all learners. e,f, The two adaptive modulations (AF-1 and AF-S) can improve the performance of MCL to a large extent through coordinating the diversity of learners' expertise, as measured by the average cosine or Euclidean distance of their predictions. e and f represent the results of MCL with the original width and the narrowed width, respectively, averaged over ten runs with different random seeds and task orders. The error bars represent the standard error of the mean. All experiments are performed on R-CIFAR-100 with EWC7 as the baseline approach.

constructed from the CIFAR-100 dataset45 of 100-class coloured images but with different degrees of overall knowledge transfer42. As shown in Fig. 2c, the proposed active forgetting can largely enhance the average accuracy of all tasks, using EWC7 as a baseline for preserving memory stability. Then we analyse the benefits of active forgetting on learning plasticity and memory stability with the metrics of forward transfer and backward transfer, respectively, where the former is clearly dominant. Similar results are observed when plugging the active-forgetting term in other synaptic regularization methods that preserve only memory stability (Supplementary Fig. 1). In contrast, active forgetting fails to improve the joint training performance (Supplementary Fig. 4a), suggesting that its benefits are specific to continual learning. From visual interpretation of the latest task predictions in Fig. 2d, active forgetting can indeed eliminate the past conflicting information, leading to better recognition of the object itself.

# Coordination of multiple continual learners

After demonstrating the benefits of active forgetting together with stability protection for a single continual learner (SCL), we turn to investigate the organizing principles of the γMB system where new memory forms and active forgetting happens19–22,25,36,38,39,46. Specifically, there are five compartments that process sequential experiences in parallel. The outputs of these compartments are integrated in a weighted-sum fashion to guide adaptive behaviours. Inspired by this, we design a γMB-like architecture consisting of multiple parallel continual learners (Fig. 3a). Each learner employs a parameter space to learn all tasks, but its dedicated output head is removed and the weighted sum of the previous layer’s output is fed into a shared output head, where the output weights of each learner are incrementally updated.

In such a γMB-like architecture, the relationship between learners is critical to the performance of continual learning. When the diversity

![](images/06fbd618fdd5dc2bc094d67c0b679113e7e6cd999ef55d5c15fc0db408a27437.jpg)

![](images/eafeb70aac8f591e77404c74ad012eeb5326b1ccae927c5e68265427b4a0c9cb.jpg)

![](images/931af7b7c75483a5ba5d4b11f01ae80126ff797e5765b2a8c1a95c5749785caf.jpg)

![](images/52380f357564fad6e878355ef16318e5a5fc60363a7f0142696d0a5ece6039e4.jpg)

![](images/9e2f00d5bc86ba42d4d854051d1b38d8b1fdf675ebe81a549f3da5083d6045d9.jpg)

![](images/af75234e2707b55d8b8a834faa94be8f2b20cfe53d2d14e65b3a41909ca29ad4.jpg)

![](images/7d2f3f09a7564122b1cde26e964b2baaf1de14843f22604e26108e3ab0e38712.jpg)

![](images/8231c902f8d7bc71f16f36546d2e31de2e3f45a4d375a212f96414e0e1c9d29d.jpg)

![](images/2f203458f91b423042f07289db311ca3e9a9d0cc154b7576fbe58988eae24d77.jpg)

![](images/6ec673ecc662a1acf09e2ada0e4725250175537d7c4b9988f04b530b863f2e25.jpg)

![](images/faebe9dd79fd41e3b01eee0f13cb092e5c2484bcc69b79570bf3d49fdca040c3.jpg)

![](images/ae25d78747ee938b9da235a01d6f3e8e0eb3d1b614dc9e088b87ecadf0367ff1.jpg)

![](images/71da26ea2c0f4132a6e03bd2d9fdadf55738ac4cb87a993f8c41273a54b4086b.jpg)

![](images/ddd28f96750f0dd09bd5588609df324404bfaf1fec6fd3f5ab03de165b8a44b2.jpg)

![](images/114ee38353e709cfa8e98347e9eb02a28a56cc9738cffcd1f4442c1b4a0db034.jpg)  
Fig. 4 | Exploration of underlying mechanisms that improve continual learning. We build the MCL with a narrowed width to keep the total amount of parameters similar to that of the SCL, and adopt the high-diversity background as a sub-optimal implementation. All experiments are performed with EWC7 as the baseline approach. a–c, We empirically approximate the discrepancy of task distributions in feature space by training a simple discriminator to distinguish whether the feature of an input image belongs to a task or not, and measure the average discrimination error on test sets via binary cross-entropy, where   
a larger discrimination error indicates a smaller difference50,51. The error bars represent the standard error of the mean over five runs. d–f, Curvature of loss landscape around the obtained solution after continual learning of all tasks. After disturbing the network parameters with random values, we evaluate the training error with cross-entropy67, where each line is a different direction of disturbance. g–i, Total parameter changes and average accuracy of all tasks. Each point represents a run. a,d,g, The results of S-CIFAR-100. b,e,h, The results of R-CIFAR-100. c,f,i, The results of R-CIFAR-10/100.

of their expertise is properly coordinated, the obtained solution can provide a high degree of compatibility with both new and old tasks. Here we present a conceptual illustration via performing tasks A, B and C with different similarities (Fig. 3c). As it is difficult to find a shared optimal solution for all tasks, the SCL has to converge to a higherror region for tasks A and C. In contrast, the multiple continual learners (MCL) with appropriate diversity allow for division of labour to address task discrepancy and complement their functions as parameter changes. Then, the output weights can integrate the respective expertise of each learner into the final prediction.

In general, each learner’s expertise is directly modulated by its target distribution, where the proposed functional strategy can naturally serve this purpose. With the formulation of active forgetting, the target distribution $p ( \theta | D _ { \mathrm { A } } , D _ { \mathrm { B } } , \beta ) \propto p ( D _ { \mathrm { B } } | \theta ) \hat { p } ( \theta | D _ { \mathrm { A } } , \beta )$ tends to be different for learners with different forgetting rates β, and vice versa (Fig. 3b). Therefore, we implement the forgetting rates adaptively for these learners to coordinate their relationship. As the target distribution also depends on $\scriptstyle \upsilon ( D _ { \mathrm { B } } | \theta )$ , we further propose a supplementary modulation that constrains explicitly the differences in predictions between learners, corresponding to adjusting the learning rules for each new task. We refer to the γMB-like architecture with these two modulations as collaborative continual learners with active forgetting (CAF), and provide a formal definition in equation (12) in Methods.

For multiple learners with identical network architectures and similar forms of learning objectives, the priority is to obtain adequate

differentiation of their expertise. In this case, the forgetting rates serve to diversify these learners, similar to the neurological strategy of decaying old memories differentially in each compartment24,36–39. In practice, the differences of learners can also arise from their innate randomness, such as the use of dropout and different random initializations, leading to sub-optimal solutions with moderate performance. This potentially corresponds to the anatomical randomness of Kenyon cells receiving olfactory signals in Drosophila47–49. At this point, the modulations of forgetting rates and learning rules can provide finer adjustments, for example, by constraining excessive differences.

Given the same network width for each learner, using more learners (that is, more parameters) generally results in better performance. However, there is an intuitive trade-off between learner number and width under a limited parameter budget. We verify that this tradeoff is independent of training data distributions (Supplementary Section 1.3) and is relatively insensitive over a wide range (Supplementary Table 5). Therefore, we simply choose five learners (K = 5) corresponding to the five biological compartments, which employs approximately 5× parameters, and then reduce the network width accordingly to keep the total amount of parameters similar to that of the SCL. To evaluate the effect of innate diversity, we construct a low-diversity background by removing the dropout and using the same random initialization for each learner, and a high-diversity background by maintaining these randomness factors, where the overall diversity of expertise is evaluated by the average cosine or Euclidean distance between learners’ predictions.

![](images/d71050a3cf507872a9eb9af46f201d50874cbcfffd83f292e333ef39f32795ec.jpg)

![](images/4207b1d181df4b8fcf168fee4577bac47ef0836320c88fa60ba8606e67f340aa.jpg)

![](images/a38159182853707d1bcfb201886c626f41d823c813689bc105a3be0f952de149.jpg)

![](images/61a51aee8da21a2ce2970b40951252046d66653e50adf77c01b5c2fa86724e02.jpg)

![](images/dbcb04d995771fe5fb8f5881a4d1757c2335981da41b9f3efae2cb323d8cf187.jpg)

![](images/66c83a4e2ad42e6dac6285850a4d0a166944db8daf7b2cc0ee738c26271608e7.jpg)

![](images/36d824ad82a572572155dfc204c9ebcc6b2c2624103d64841234539f66ab4cdb.jpg)

![](images/c61c4196ceda84c00f64d930e15a4dc1901f1c27c43a1006a0c867a7228c9845.jpg)  
Fig. 5 | Performance evaluation for visual classification tasks. We consider multiple visual classification benchmarks to evaluate different aspects of continual learning, such as overall knowledge transfer, input size, number of training samples, length of task sequence, smoothly changed observations and so on. The bottom-left panel shows a demo of these benchmarks. CAF (ours)   
and CPR56 are plug-and-play for synaptic regularization methods such as EWC7 and MAS8 . Under similar parameter budgets, all results are averaged over five runs with different random seeds and task orders. The error bars represent the standard error of the mean.

As shown in Fig. 3e,f, adaptive implementations of either active forgetting (AF-1) or its supplementary modulation (AF-S) can greatly enhance the performance of MCL, where the degree of improvements varies with the effectiveness of increasing inadequate diversity or reducing excessive diversity in the two backgrounds, respectively. In response to different degrees of innate diversity, the respective advantages of AF-1 and AF-S are combined to achieve consistently better performance. Such modulations enable the multiple learners to effectively divide and cooperate in continual learning (Fig. 3d and Supplementary Figs. 4b,c and 5). They show a clear diversity of task expertise with several experts collaborating on each task, validating the conceptual model in Fig. 3c. Accordingly, the performance of CAF is largely superior to that of the SCL, averaging the predictions

of five independently trained continual learners, or using a separate learner for each task (Supplementary Fig. 6a,b). In particular, CAF can improve the SCL by a similar magnitude under different parameter budgets, indicating its outstanding scalability (Supplementary Figs. 6c and 7a).

According to our theoretical analysis in Proposition 1 in Methods, the performance of a shared solution for new and old tasks depends on the discrepancy of task distributions and the flatness of loss landscape around it. With respect to these two aspects, we delve more deeply into the benefits of our approach. As for the former, we evaluate the discrepancy of task distributions in feature space via the difficulty of distinguishing them after continual learning50,51 (Fig. 4a–c). The large increase in discrimination error suggests that our approach can

![](images/9f60b2453ebcbd026b9b5bf751cbf80c72d9cfccde76a357b30807e13d414481.jpg)  
a

![](images/39584d6ec543824e9c0a00350346035903b924b2019b21d77a1fb93e3a261be3.jpg)

![](images/7faee92b051208875f3cc8c25822659bb917b38c7a20ec271a2ef02f4c5425e8.jpg)  
b

![](images/d7de30d630ee1a3a3737afbf22bb3824807a025029de18433a71e42a2ec20b75.jpg)

![](images/19e38820afe29e4dfee2b16278e62e2d0ea5718682ab893afc130bfe0155e544.jpg)  
Fig. 6 | Performance evaluation for Atari reinforcement tasks. a, An agent attempts to acquire more rewards from learning a sequence of Atari games. b, The NAR in continual learning. The performance of simply fine-tuning on the task sequence is used to normalize the reward obtained for each task.   
c–e, After continual learning of all Atari games, we evaluate the overall performance (c), learning plasticity (d) and memory stability (e). Under similar parameter budgets, all results are averaged over five runs with different random seeds. The error bars represent the standard error of the mean.

successfully reconcile this discrepancy. As for the latter, the solution obtained by ours enjoys a clearly flatter loss landscape (Fig. 4d–f), indicating that it is more robust to modest parameter changes in response to dynamic data distributions. Therefore, CAF can update parameters more flexibly than the SCL (Fig. 4g–i), with the performance of new and old tasks simultaneously improved (Supplementary Fig. 7b,c).

Finally, we evaluate CAF under the setting of task-incremental learning52 and compare it with a range of representative methods7–9,53–56. We first consider visual classification tasks with different particular challenges. Besides the overall knowledge transfer, we additionally use four benchmark datasets such as Omniglot57 for long task sequence with imbalanced class numbers, CUB-200-201158 and Tiny-ImageNet17 for larger-scale images, and CORe5059 for smoothly changed observations. As shown in Fig. 5, the performance of all baselines varies widely across experimental settings, while CAF achieves consistently the strongest performance in a plug-and-play manner. We further experiment with Atari reinforcement tasks, where an agent incrementally learns to play several Atari games (Fig. 6a). The overall performance is evaluated by the normalized accumulated reward (NAR)42,55,56, where the rewards obtained for all tasks ever seen are normalized with the maximum reward of fine-tuning on each task, and then accumulated.

Likewise, CAF can greatly enhance the performance of baseline approaches (Fig. 6b,c) through improving both learning plasticity and memory stability (Fig. 6d,e).

# Discussion

Whether for animals, robots or other intelligent agents, the ability of continual learning is critical for successfully adapting to the real world. In this work, we draw inspirations from the adaptive mechanisms equipped in a robust biological learning system, and present a generic approach for continual learning in artificial neural networks. Our preliminary versions of some individual components have been presented at top conferences in AI42,51, while the current version enjoys substantial extensions in terms of technical robustness, synergistic cooperation and biological plausibility (Supplementary Section 3). The superior performance and generality of our approach can facilitate realistic applications, such as smartphones, robotics and autonomous driving, to flexibly accommodate user needs and environmental changes. Meanwhile, the deployment of continual learning avoids retraining all previous data each time the model is updated, which provides an energy-efficient and eco-friendly path for developing AI systems.

To bridge the gap between AI and BI, we carefully avoid involving specific implementations or overly strong assumptions in both theoretical analysis and computational modelling. This consideration not only allows for an adequate exploitation of biological advantages but also facilitates the emergence of interdisciplinary insights. Computationally, our approach is proven to satisfy the key factors on which continual learning performance depends, such as stability, plasticity and compatibility, with active forgetting playing an important role. This potentially extends the previous focus of preventing catastrophic forgetting in continual learning. Starting with this idea, below we discuss more broadly the connections between AI and BI in adaptability.

In a biological sense, active forgetting allows flexibility to accommodate external changes by removing outdated information27,30,60. This perspective is well supported by extensive theoretical and empirical evidence in our computational model. Recent work in neurobiology is deeply dissecting its underlying mechanisms from molecular to synaptic structural levels, where activation of the molecular signalling that mediates active forgetting initially leads to rapid growth of synaptic structures, but prolonged activation instead leads to their shrinkage19,30,42,60–64. In our computational model, active forgetting of old memories in parameter distributions can derive two equivalent synaptic expansion-renormalization processes. These two processes and their linear combinations cover a wide range of possible forms, including whether old memories are directly affected and whether expanded parameters encode new memories, which can serve as testable hypotheses for further research. As for the five compartments of the γMB system, the modulated forgetting rates have been shown to be important for coping with conflicting memories in succession24,36–39. Correspondingly, adaptive implementations of active forgetting help the γMB-like architecture to better accommodate incremental changes. Besides, we identify the necessity of regularizing learners’ predictions of new tasks, suggesting that the adaptation of learning rules may also contribute to continual learning in a more general context.

AI and BI share the common goal of adaptation and survival in the real world. These two fields have great potential to inspire each other and progress together. This requires generalized theories and methodologies to integrate their advances, as suggested by our work in continual learning. Subsequent work could further explore the ‘natural algorithms’ responsible for other advantages of the biological brain, thereby evolving progressively the current AI systems.

# Methods

# Synaptic expansion-renormalization

For the case of two tasks, the learner needs to find a mode of the posterior distribution that incorporates the knowledge of tasks A and B:

$$
\begin{array}{l} \theta_ {\mathrm {A}, \mathrm {B}} ^ {*} = \arg \max  _ {\theta} \log p (\theta | D _ {\mathrm {A}}, D _ {\mathrm {B}}) \\ = \arg \max  _ {\theta} \log p \left(D _ {\mathrm {B}} \mid \theta\right) + \log p \left(\theta \mid D _ {\mathrm {A}}\right) - \underbrace {\log p \left(D _ {\mathrm {B}}\right)} _ {\text {c o n s t a n t}}, \tag {3} \\ \end{array}
$$

where $p ( D _ { \mathsf { B } } | \theta )$ is the loss for task B. Although $p ( \theta | D _ { \mathsf { A } } )$ is generally intractable, we can locally approximate it with a second-order Taylor expansion around $\theta _ { \mathrm { A } } ^ { * } = \arg \operatorname* { m a x } _ { \theta } \log p ( \theta | D _ { \mathrm { A } } ) .$ , resulting in a Gaussian distribution whose mean is $\theta _ { \mathbf { A } } ^ { * }$ and precision matrix is the Hessian of Athe negative log posterior7,11,65. To simplify the computation, the Hessian is approximated by the diagonal of the Fisher information matrix:

$$
F _ {\mathrm {A}} = \mathbb {E} \left[ \left(\frac {\partial \log p (\theta \mid D _ {\mathrm {A}})}{\partial \theta}\right) \left(\frac {\partial \log p (\theta \mid D _ {\mathrm {A}})}{\partial \theta}\right) ^ {\top} \mid_ {\theta_ {\mathrm {A}} ^ {*}} \right]. \tag {4}
$$

To improve learning plasticity, we introduce a forgetting rate $\beta ,$ and replace p(θ∣DA) in equation (3) with p(̂ θ|DA, β) = p(θ|DA) (1−β) p(θ) β $p ( \theta | D _ { \mathsf { A } } )$ $\begin{array} { r } { \hat { p } ( \theta | D _ { \mathrm { A } } , \beta ) = \frac { \bar { p ( \theta | D _ { \mathrm { A } } ) } ^ { ( 1 - \overline { { \beta } } ) } p ( \theta ) ^ { \beta } } { Z } } \end{array}$ as Z equation (1), where $\beta \in [ 0 , 1 ]$ ] is deterministic and Z is a β-dependent normalizer. Correspondingly, the target distribution $p ( \theta | D _ { \mathrm { A } } , D _ { \mathrm { B } } )$

becomes p(θ $| D _ { \mathsf { A } } , D _ { \mathsf { B } } , \beta ) .$ . p has a nice property that it follows a Gaussian̂ distribution i ${ \dot { p } } ( \theta | D _ { \mathrm { A } } )$ and $p ( \theta )$ are both Gaussian (Supplementary Section 1.1), so we can compute p in a similar way to how we compute ̂ $p ( \theta | D _ { \mathsf { A } } )$ . A certain value of β can maximize the probability of learning each new task well through forgetting the old memories, validating the motivation of introducing the non-informative prior in equation (1):

$$
\beta^ {*} = \arg \max  _ {\beta} p \left(D _ {\mathrm {B}} \mid D _ {\mathrm {A}}, \beta\right) = \arg \max  _ {\beta} \int p \left(D _ {\mathrm {B}} \mid \theta\right) \hat {p} \left(\theta \mid D _ {\mathrm {A}}, \beta\right) \mathrm {d} \theta . \tag {5}
$$

With the implementation of active forgetting, the learner needs to find

$$
\begin{array}{l} \theta_ {\mathrm {A}, \mathrm {B}} ^ {*} = \arg \max  _ {\theta} \log p (\theta | D _ {\mathrm {A}}, D _ {\mathrm {B}}, \beta) \\ = \arg \max  _ {\theta} \log p \left(D _ {\mathrm {B}} \mid \theta\right) + \log \dot {p} \left(\theta \mid D _ {\mathrm {A}}, \beta\right) - \underbrace {\log p \left(D _ {\mathrm {B}}\right)} _ {\text {c o n s t a n t}} \\ = \arg \max  _ {\theta} \log p \left(D _ {\mathrm {B}} \mid \theta\right) + (1 - \beta) \log p (\theta \mid D _ {\mathrm {A}}) + \beta \log p (\theta) \\ = \arg \max  _ {\theta} (1 - \beta) \log p \left(D _ {\mathrm {B}} \mid \theta\right) + (1 - \beta) \log p \left(\theta \mid D _ {\mathrm {A}}\right) + \beta \log p \left(\theta \mid D _ {\mathrm {B}}\right), \tag {6} \\ \end{array}
$$

which can be optimized in two equivalent ways, that is, AF-1 and AF-2. Correspondingly, we derive the loss function in equation (2).

For continual learning of more than two tasks, for example, t tasks for any t > 2, the learner needs to find

$$
\theta_ {1: t} ^ {*} = \arg \max  _ {\theta} \log p \left(D _ {t} \mid \theta\right) + \log p \left(\theta \mid D _ {1: t - 1}, \beta_ {1: t - 1}\right) - \underbrace {\log p \left(D _ {t}\right)} _ {\text {c o n s t a n t}}, \tag {7}
$$

where $D _ { 1 : t - 1 } = \bigcup _ { i = 1 } ^ { t - 1 } D _ { i }$ denotes the training data of previous task(s) and $\beta _ { 1 : t - 1 } = \left\{ \beta _ { i } \right\} _ { i = 1 } ^ { t - 1 }$ denotes the previously used forgetting rate(s). Similarly, we replace the posterior $p ( \theta | D _ { 1 : t - 1 } , \beta _ { 1 : t - 1 } )$ that absorbs all information of $D _ { 1 : t - 1 }$ with

$$
\hat {p} \left(\theta \mid D _ {1: t - 1}, \beta_ {1: t - 1}, \beta_ {t}\right) = \frac {p \left(\theta \mid D _ {1 : t - 1} , \beta_ {1 : t - 1}\right) ^ {\left(1 - \beta_ {t}\right)} p \left(\theta\right) ^ {\beta_ {t}}}{Z _ {t}}, \tag {8}
$$

where $Z _ { t }$ is a β -dependent normalizer that keeps p a normalized̂ probability distribution. To simplify the hyperparameter tuning, we adopt an identical forgetting rate in continual learning, that is, $\beta _ { i } { = } \beta$ for $\dot { \iota } = 1 , . . . , t .$ Then we obtain the loss function:

$$
\mathcal {L} _ {\text {R e g}} ^ {\mathrm {A F}} (\theta) = \mathcal {L} _ {t} (\theta) + \underbrace {\frac {\lambda_ {\mathrm {S P}}}{2} \sum_ {m} F _ {1 : t - 1 , m} \left(\theta_ {m} - \theta_ {1 : t - 1 , m} ^ {*}\right) ^ {2}} _ {\text {s t a b i l i t y p r o t e c t i o n}} + \underbrace {\frac {\lambda_ {\mathrm {A F}}}{2} \sum_ {m} I _ {\mathrm {e} , m} \left(\theta_ {m} - \theta_ {\mathrm {e} , m}\right) ^ {2}} _ {\text {a c t i v e f o r g e t t i n g}}. \tag {9}
$$

$\theta _ { 1 : t - 1 } ^ { * }$ is the obtained solution for previous tasks, that is, the old network parameters. For AF-1, $\theta _ { \mathrm { e } , m } = 0 , I _ { \mathrm { e } , m } = 1 , \lambda _ { \mathrm { A F } } \propto \beta$ and $\lambda _ { \mathtt { S P } } \propto ( 1 - \beta )$ . For AF-2, $\theta _ { \mathrm { e } , m } = \theta _ { t , m } ^ { * } , I _ { \mathrm { e } , m } = F _ { t , m } , \lambda _ { \mathrm { A F } } \propto \beta / ( 1 - \beta )$ and $\lambda _ { \mathsf { S P } } \propto 1 . F _ { 1 : t - 1 }$ is recursively updated by

$$
F _ {1: t - 1} = F _ {1: t - 2} + F _ {t - 1}. \tag {10}
$$

When $\beta = 0 ,$ , the loss function in equation (9) degenerates to a similar form as regular synaptic regularization methods that preserve only memory stability7–10:

$$
\mathcal {L} _ {\text {R e g}} (\theta) = \mathcal {L} _ {t} (\theta) + \underbrace {\frac {\lambda_ {\mathrm {S P}}}{2} \sum_ {m} \xi_ {1 : t - 1 , m} \left(\theta_ {m} - \theta_ {1 : t - 1 , m} ^ {*}\right) ^ {2}} _ {\text {s t a b i l i t y p r o t e c t i o n}}. \tag {11}
$$

As these methods differ mainly in the metric $\xi _ { 1 : t - 1 }$ of estimating the importance of parameters for performing old tasks43, the

active-forgetting term can be naturally combined with them. We discuss in more depth the motivation and implementation of active forgetting in Supplementary Section 1.2, including the choice of an appropriate $\beta ,$ the connections of two equivalent versions and the technical details of derivation.

# Multiple parallel continual learners

The γMB-like architecture of MCL adopts K identically structured neural networks $f _ { \phi _ { i } } ( \cdot ) , i = 1 , \ldots , K ,$ , corresponding to K continual learners $\mathsf { L } _ { i } , i = 1 , . . . ,$ K with their own parameter sets ϕi. We remove the dedicated output head of each learner, and feed the weighted sum of the previous layer’s output into a shared output head $h _ { \varphi } ( \cdot )$ to make predictions, where the output weights of each learner ${ \displaystyle g _ { i } , i = 1 , . . . , }$ K are updated incrementally. Then, the final prediction becomes $\begin{array} { r } { \tilde { p } ( \cdot ) = h _ { \varphi } ( \sum _ { i = 1 } ^ { K } g _ { i } f _ { \phi _ { i } } ( \cdot ) ) , } \end{array}$ , where φ denotes the parameter set of prediction function and the optimizable MCL parameters $\theta _ { \mathrm { { \scriptscriptstyle M C l } } }$ L include $\textstyle | \bigcup _ { i = 1 } ^ { K } \phi _ { i } , \bigcup _ { i = 1 } ^ { K } g _ { i }$ and φ. The proposed MCL is applicable to a wide range of loss functions for continual learning. By default, here we focus on the synaptic regularization methods7–10 as defined in equation (11). To coordinate the diversity of learners’ expertise, we implement the proposed active forgetting in each learner. We further regularize differences in their predictive distributions, quantified by the widely used Kullback–Leibler divergence. Therefore, the loss function for the full version of our approach is defined as:

$$
\begin{array}{l} \mathcal {L} _ {\mathrm {C A F}} \left(\theta_ {\mathrm {M C L}}\right) = \mathcal {L} _ {t} \left(\theta_ {\mathrm {M C L}}\right) + \underbrace {\frac {\lambda_ {\mathrm {S P}}}{2} \sum_ {i = 1} ^ {K} \sum_ {m = 1} ^ {M _ {i}} \xi_ {1 : t - 1 , i , m} \left(\theta_ {i , m} - \theta_ {1 : t - 1 , i , m} ^ {*}\right) ^ {2}} _ {\text {s t a b i l i t y p r o t e c t i o n}} \tag {12} \\ + \underbrace {\sum_ {i = 1} ^ {K} \frac {\lambda_ {\mathrm {A F} , i}}{2} \sum_ {m = 1} ^ {M _ {i}} \left(\theta_ {i , m}\right) ^ {2}} _ {\mathrm {A F} - 1} + \underbrace {\sum_ {i = 1 , j \neq i} ^ {K} \frac {\gamma_ {i , j}}{N _ {t}} \sum_ {n = 1} ^ {N _ {t}} \tilde {p} _ {i} \left(x _ {t , n}\right) \log \frac {\bar {p} _ {i} \left(x _ {t , n}\right)}{\bar {p} _ {j} \left(x _ {t , n}\right)}} _ {\mathrm {A F} - S}, \\ \end{array}
$$

where $M _ { i }$ denotes the amount of parameters $\theta _ { i } = \{ \phi _ { i } , g _ { i } \}$ for learner i. n denotes the index of training samples in each task. The current task has $N _ { t }$ training samples, and $\tilde { p } _ { i } ( x _ { t , n } )$ is the prediction of learner i for $x _ { t , n } .$ . We mainly consider AF-1 instead of $\mathsf { A F } ^ { 2 }$ for computational efficiency, while keeping $\lambda _ { \mathtt { S P } }$ identical to each learner for ease of implementation. We then discuss the implementation of $\dot { \lambda } _ { \mathrm { A F } , i }$ and $\gamma _ { i , j }$ . If we consider CAF as an overall continual learning model, active forgetting can be implemented similarly to equations (1) and (2), setting a uniform forgetting rate $\lambda _ { \mathrm { A F , } }$ i as well as a uniform learning rule $\gamma _ { i , j }$ j to each learner. This implementation is indeed effective under strong innate randomness to reduce excessive diversity. In a more general context, the proposed MCL provides a spatial degree of freedom to modulate the diversity of learner’s expertise. This idea can be implemented by constraining the average of $\{ \lambda _ { \mathrm { A F } , i } \} _ { i = 1 } ^ { K }$ to be a deterministic hyperparamete $\lambda _ { \mathrm { A F } }$ , that is $\begin{array} { r } { , \frac { 1 } { K } \sum _ { i = 1 } ^ { K } \lambda _ { \mathrm { A F } , i } = \lambda _ { \mathrm { A F } } } \end{array}$ F where $\lambda _ { \mathrm { A F } , i } { = } \alpha _ { i } K \lambda _ { \mathrm { A } }$ F and $\textstyle \sum _ { i = 1 } ^ { K } \alpha _ { i } = 1$ , but allowing their relative strength αi as well as $\theta _ { \mathrm { { M C l } } }$ L to be optimized with gradients of the same loss function. Specifically, we perform softmax of a few optimizable parameters to ensure the constraint $\textstyle \sum _ { i = 1 } ^ { K } \alpha _ { i } = 1$ 1 and obtain $\alpha _ { i }$ for each learning module. $\gamma _ { i , j }$ can be implemented in a similar way by constraining their average $\begin{array} { r } { \frac { 1 } { K ( K - 1 ) } \sum _ { i = 1 , j \neq i } ^ { K } \gamma _ { i , j } = \gamma , } \end{array}$ K , to enjoy the spatial degree of freedom.

# Theoretical analysis of generalization ability

Continual learning aims to find a solution θ that can generalize well over a new distribution $\mathbb { D } _ { \iota }$ t and a set of old distributions $\mathbb { D } _ { 1 : t - 1 } : = \left\{ \mathbb { D } _ { k } \right\} _ { k = 1 } ^ { t - 1 }$ Let $\mathcal { E } _ { \mathbb { D } _ { t } } ( \theta )$ and $\mathcal { E } _ { \mathbb { D } _ { 1 : t - 1 } } ( \theta )$ denote the generalization errors. The training set and test set of each task follow the same distribution $\mathbb { D } _ { k }$ $( k = 1 , 2 , . . . , t )$ , where the training set $D _ { k } = \{ ( x _ { k , n } , y _ { k , n } ) \} _ { n = 1 } ^ { N _ { k } }$ 1 includes $N _ { k }$ data-label pairs. Then we define ${ \mathcal E } _ { \mathbb { D } _ { t } } ( \theta ) = \mathbb { E } _ { ( x , y ) \sim \mathbb { D } _ { t } } [ { \mathcal L } _ { t } ( \theta ; x , y ) ]$ and $\begin{array} { r } { \mathcal { E } _ { \mathbb { D } _ { 1 : t - 1 } } ( \theta ) = \frac { 1 } { t _ { - 1 } } \sum _ { k = 1 } ^ { t - 1 } \mathbb { E } _ { ( x , y ) \sim \mathbb { D } _ { k } } [ \mathcal { L } _ { k } ( \theta ; x , y ) ] } \end{array}$ ?t, where ${ \mathcal { L } } _ { k } ( \theta )$ x,y)∼?t t can be generalized t−1   for any bounded loss function of task k. To minimize $\mathcal { E } _ { \mathbb { D } _ { t } } ( \theta )$ and

$\mathcal { E } _ { \mathbb { D } _ { 1 : t - 1 } } ( \theta )$ without the use of old training samples $D _ { 1 : t - 1 } : = \left\{ D _ { k } \right\} _ { k = 1 } ^ { t - 1 }$ , a continual learning model can only minimize an empirical risk over the current training samples $D _ { t }$ in a parameter space Θ applicable to old tasks51,66, denoted as $\mathsf { m i n } _ { \theta \in \Theta } \hat { \mathcal { E } } _ { D _ { t } } ( \theta )$ where $\begin{array} { r } { \hat { \mathcal { E } } _ { D _ { t } } ( \theta ) = \frac { 1 } { N _ { t } } \sum _ { n = 1 } ^ { N _ { t } } \mathcal { L } _ { t } ( \theta ; x _ { t , n } , y _ { t , n } ) } \end{array}$ 1 ∑Ntn=1 ℒt (θ; xt,n , yt,n ). In practice, sequential learning of each task by mi $\scriptstyle \mathsf { \Lambda } _ { \theta \in \Theta } \hat { \mathcal { E } } _ { D _ { t } } ( \theta )$ can find multiple solutions with different generalizability for $\mathcal { E } _ { \mathbb { D } _ { r } } ( \theta )$ and $\mathcal { E } _ { \mathbb { D } _ { 1 : t - 1 } } ( \theta ) ,$ where a solution with flatter loss landscape typically acquires better generalizability and is therefore more robust to catastrophic forgetting56,67,68.

Accordingly, we define a robust empirical risk for the current task as $\begin{array} { r } { \hat { \mathcal { E } } _ { D _ { t } } ^ { b } ( \theta ) : = \operatorname* { m a x } _ { \| \varDelta \| \leq b } \hat { \mathcal { E } } _ { D _ { t } } ( \theta + \varDelta ) } \end{array}$ by the worst case of parameter perturbations Δ, where ∥⋅∥ denotes the L2 norm and b is the radius of perturbations around θ. Likewise, a robust empirical risk for the old tasks is $\begin{array} { r } { \hat { \mathcal { E } } _ { D _ { 1 : t - 1 } } ^ { b } ( \theta ) : = \operatorname* { m a x } _ { \| \varDelta \| \leq b } \hat { \mathcal { E } } _ { D _ { 1 : t - 1 } } ( \theta + \varDelta ) } \end{array}$ . Then, $\mathfrak { m i n } _ { \theta \in \Theta } \hat { \mathcal { E } } _ { D _ { r } } ^ { b } ( \theta )$ can find a flat minima over the current task. However, parameter changes that are much larger than the ‘radius’ of the old minima can interfere with the performance of old tasks, while staying around the old minima can interfere with the performance of new tasks. Therefore, it is necessary to find a solution that can properly balance memory stability with learning plasticity, while being adequately compatible with the observed distributions. Formally, we analyse the generalization errors of a certain solution for continual learning with PAC-Bayes theory69, to provide the objective for computational modelling of neurological adaptive mechanisms. We leave technical details to Supplementary Section 1.3 and present the main results below.

Proposition 1. Let $\{ \boldsymbol { \Theta } _ { i } \in \mathbb { R } ^ { M _ { i } } \} _ { i = } ^ { K }$ 1 be a set of parameter spaces $( K \geq 1$ in general), $d _ { i }$ be a Vapnik–Chervonenkis (VC) dimension of $\mathcal { O } _ { i } , \Theta = \cup _ { i = 1 } ^ { K } \Theta _ { i }$ with VC dimension d, and $\begin{array} { r } { M = \sum _ { i = 1 } ^ { K } M _ { i } } \end{array}$ as a given parameter budget. Let $\hat { \theta } _ { 1 : } ^ { b }$ denote the optimal solution of the continually learned 1:t tasks by robust empirical risk minimization over the current task, that is, $\begin{array} { r } { \hat { \theta } _ { 1 : t } ^ { b } = \arg \operatorname* { m i n } _ { \theta \in \Theta } \hat { \mathcal { E } } _ { D _ { t } } ^ { b } ( \theta ) } \end{array}$ . Then for any $\delta \in ( 0 , 1 )$ , with probability at least $1 - \delta \colon$

$$
\begin{array}{l} \underbrace {\mathcal {E} _ {\mathbb {D} _ {t}} \left(\hat {\theta} _ {1 : t} ^ {b}\right) - \min  _ {\theta \in \Theta} \mathcal {E} _ {\mathbb {D} _ {t}} (\theta)} _ {\text {l e a n i n g p l a s t i c i t y}} \leq \underbrace {\min  _ {\theta \in \Theta} \hat {\mathcal {E}} _ {D _ {1 : t - 1}} ^ {b} (\theta) - \min  _ {\theta \in \Theta} \hat {\mathcal {E}} _ {D _ {1 : t - 1}} (\theta)} _ {\text {l o s s f l a t n e s s}} \\ + \underbrace {\frac {1}{t - 1} \sum_ {k = 1} ^ {t - 1} \operatorname {D i v} \left(\mathbb {D} _ {k} , \mathbb {D} _ {t}\right)} _ {\text {t a s k d i s c r e p a n c y}} + C _ {1}, \tag {13} \\ \underbrace {\mathcal {E} _ {\mathbb {D} _ {1 : t - 1}} \left(\hat {\theta} _ {1 : t} ^ {b}\right) - \min  _ {\theta \in \Theta} \mathcal {E} _ {\mathbb {D} _ {1 : t - 1}} (\theta)} _ {\text {m e m o r y s t a b i l i t y}} \leq \underbrace {\min  _ {\theta \in \Theta} \hat {\mathcal {E}} _ {D _ {t}} ^ {b} (\theta) - \min  _ {\theta \in \Theta} \hat {\mathcal {E}} _ {D _ {t}} (\theta)} _ {\text {l o s s f l a t n e s s}} \\ + \underbrace {\frac {1}{t - 1} \sum_ {k = 1} ^ {t - 1} \operatorname {D i v} (\mathbb {D} _ {t} , \mathbb {D} _ {k})} _ {\text {t a s k d i s c r e p a n c y}} + C _ {2}, \\ \end{array}
$$

where C1 = maxi∈[1,K] $\begin{array} { r } { C _ { 1 } = \mathfrak { m a x } _ { i \in [ 1 , K ] } \sqrt { \frac { d _ { i } \ln ( N _ { 1 : t - 1 } / d _ { i } ) + \ln ( 2 K / \delta ) } { N _ { 1 : t - 1 } } } + \sqrt { \frac { d \ln ( N _ { 1 : t - 1 } / d ) + \ln ( 2 / \delta ) } { N _ { 1 : t - 1 } } } } \end{array}$ + and

$\begin{array} { r } { C _ { 2 } = \operatorname* { m a x } _ { i \in [ 1 , K ] } \sqrt { \frac { d _ { i } \ln ( N _ { t } / d _ { i } ) + \ln ( 2 K / \delta ) } { N _ { t } } } + \sqrt { \frac { d \ln ( N _ { t } / d ) + \ln ( 2 / \delta ) } { N _ { t } } } } \end{array}$ C2 = maxi∈[1,K] represent the cover of parameter space. $\mathrm { D i v } ( \mathbb { D } _ { i } , \mathbb { D } _ { j } ) : = 2 \operatorname* { s u p } _ { b , - \tau } | \mathcal { P } _ { \mathbb { D } _ { i } } ( I ( h ) ) - \mathcal { P } _ { \mathbb { D } _ { j } } I \left( h \right) ) |$ is the ℋ h∈H divergence of $\mathbb { D } _ { i }$ and $\mathbb { D } _ { j } ,$ , where $I ( h )$ is the characteristic function. $\begin{array} { r } { N _ { 1 : t - 1 } = \sum _ { k = 1 } ^ { t - 1 } N _ { k } } \end{array}$ is the total number of training samples over all old tasks, where $N _ { k }$ is the number of training samples over task k.

From Proposition 1, the generalization gaps over new and old tasks, corresponding to learning plasticity and memory stability, are uniformly constrained by the loss flatness and task discrepancy, which further depend on the cover of parameter space, that is, $C _ { 1 }$ and $C _ { 2 } .$ . In particular, we have $\begin{array} { r } { C _ { 1 } = 2 \sqrt { \frac { d \ln ( N _ { 1 : t - 1 } / d ) + \ln ( 2 / \delta ) } { N _ { 1 : t - 1 } } } } \end{array}$ and $\begin{array} { r } { C _ { 2 } = 2 \sqrt { \frac { d \ln ( N _ { t } / d ) + \ln ( 2 / \delta ) } { N _ { t } } } } \end{array}$ for K = 1. When $\begin{array} { r } { K > 1 , C _ { 1 } < 2 \sqrt { \frac { d \ln ( N _ { 1 : t - 1 } / d ) + \ln ( 2 / \delta ) } { N _ { 1 : t - 1 } } } } \end{array}$ and $\begin{array} { r } { C _ { 2 } < 2 \sqrt { \frac { d \ln ( N _ { t } / d ) + \ln ( 2 / \delta ) } { N _ { t } } } } \end{array}$ due to $d _ { i } < d { \sf f o r } i \in [ 1 , K ]$ . This means that employing MCL (that is, K > 1)

compared with an SCL (that is, K = 1) can tighten the generalization bounds and thus benefit the performance of continual learning. Likewise, the benefits of active forgetting can be explained from a similar perspective.

Proposition 2. Let {ϴi ∈ ℝMi } Ki=1 $\{ \boldsymbol { \Theta } _ { i } \in \mathbb { R } ^ { M _ { i } } \} _ { i = 1 } ^ { K }$ be a set of parameter spaces $( K \ge 1$ in general), di be a VC dimension of $\theta _ { i } , \Theta = \cup _ { i = 1 } ^ { K } \Theta _ { i }$ with VC dimension d, and $\begin{array} { r } { M = \sum _ { i = 1 } ^ { K } M _ { i } } \end{array}$ as a given parameter budget. Based on Proposition 1, for $\begin{array} { r } { \hat { \theta } _ { 1 : t } ^ { b } = \mathrm { a r g } \operatorname* { m i n } _ { \theta \in \Theta } \hat { \mathcal { E } } _ { D _ { t } } ^ { b } ( \theta ) } \end{array}$ , the upper bound of generalization gap is further externalized with $C _ { 1 } = r _ { 1 } ( \parallel \hat { \theta } _ { 1 : t } ^ { b } \parallel _ { 2 } ^ { 2 } / b ^ { 2 } )$ and $C _ { 2 } = r _ { 2 } ( \parallel \hat { \theta } _ { 1 : t } ^ { b } \parallel _ { 2 } ^ { 2 } / b ^ { 2 } )$ , where $r _ { 1 } : \mathbb { R } _ { + } \to \mathbb { R } .$ and $r _ { 2 } : \mathbb { R } _ { + } \to \mathbb { R } _ { + }$ are two strictly increasing functions under some technical conditions on $\mathcal { E } _ { \mathbb { D } _ { t } } ( \theta )$ and $\mathcal { E } _ { \mathbb { D } _ { 1 : t - 1 } } ( \theta )$ , respectively.

Proposition 2 externalizes the two generalization bounds in Proposition 1 by defining the VC dimension with L2 norm for parameters under some technical assumptions. Notably, the claim in Proposition 1 regarding the benefits of using multiple continual learners still holds in such a tightened version. In particular, optimization of the active-forgetting term in equations (2) and (12), which takes the form of minimizing a weighted L2 norm regarding all parameters, can contribute to tightening the two generalization bounds in Proposition 2, especially through optimizing $C _ { 1 }$ and $C _ { 2 }$ . Besides, $N _ { { \mathrm { 1 } } ; t - 1 }$ 1 becomes larger as t increases, while $N _ { t }$ remains constant in general. This means that $C _ { 1 }$ will decrease more rapidly around the empirical optimal solution $\begin{array} { r } { \hat { \theta } _ { 1 : t } ^ { b } = \arg \operatorname* { m i n } _ { \theta \in \Theta } \hat { \mathcal { E } } _ { D _ { t } } ^ { b } ( \theta ) } \end{array}$ as more tasks are introduced, resulting in more pronounced improvements in learning plasticity.

# Implementation

We mainly consider the setting of task-incremental learning52 to perform continual learning experiments, with task identities provided in both training and testing. We split representative benchmark datasets for visual classification tasks. The CIFAR-100 dataset 45 includes 100-class coloured images of size 32 × 32. We split it based on different principles to evaluate the effect of overall knowledge transfer. Specifically, R-CIFAR-100 and S-CIFAR-100 are constructed by splitting CIFAR-100 into 20 tasks, depending on random order or superclasses defined by semantic similarity, respectively. R-CIFAR-10/100 includes 2 tasks randomly split from the CIFAR-10 dataset 45 of 10-class coloured images, followed by the 20 tasks of R-CIFAR-100. The Omniglot data-$\mathsf { s e t } ^ { 5 \bar { 7 } }$ includes 50 alphabets for a total of 1,623 classes of characters, where each class contains 20 hand-written digits of size 28 × 28. We split each alphabet as a task consisting of a different number of classes. The CUB-200-2011 dataset58 includes 200-class bird images of size 224 × 224, and the Tiny-ImageNet dataset17 includes 200-class natural images of size 64 × 64, both split randomly into 10 tasks. The CORe50 dataset59 includes 50 handheld objects with smoothly changed observations of size 128 × 128, randomly split into 10 tasks70. We construct a sequence of Atari reinforcement tasks for continual learning, that is, DemonAttack - Robotank - Boxing - NameThisGame - StarGunner - Gopher - VideoPinball - Crazyclimber, using the same PPO algorithm71 to learn each task. The network architecture and training regime are described in Supplementary Sections 2.1 and 2.2, respectively.

# Baseline approach

To ensure generality in realistic applications, we restrict the old training samples to be unavailable in continual learning, and compare with representative methods that follow this restriction. Specifically, EWC7 , memory aware synapses (MAS8 ) and synaptic intelligence (SI9 ) are synaptic regularization methods that selectively penalized parameter changes to preserve memory stability; adaptive group sparsity based continual learning (AGS-CL55) took advantages of parameter isolation and synaptic regularization to prevent catastrophic forgetting; progress & compress $( \mathsf { P } \& \mathsf { C } ^ { 5 4 } )$ adopted an additional active column on the basis of EWC7 to improve learning plasticity; classifier-projection regularization (CPR56) encouraged convergence to a flat loss landscape,

which can be combined with other baseline approaches. The hyperparameters for continual learning are determined with a comprehensive grid search. We construct a different task sequence (that is, different class splits, data shuffling, task orders and random seeds) from the actual experiments and run it once. Then we use the best combinations of hyperparameters to perform the actual experiments for multiple runs, as described in Supplementary Section 2.3.

# Evaluation metric

We consider three evaluation metrics for visual classification tasks, that is, average accuracy (AAC), forward transfer (FWT) and backward transfer $( \mathsf { B W T } ) ^ { 6 , 7 2 } .$ :

$$
\mathrm {A A C} = \frac {1}{T} \sum_ {i = 1} ^ {T} A _ {T, i}, \tag {14}
$$

$$
\mathrm {F W T} = \frac {1}{T - 1} \sum_ {i = 2} ^ {T} A _ {i - 1, i} - \tilde {a} _ {i}, \tag {15}
$$

$$
\mathrm {B W T} = \frac {1}{T - 1} \sum_ {i = 1} ^ {T - 1} A _ {T, i} - A _ {i, i}, \tag {16}
$$

where $A _ { t , i }$ i is the test accuracy of task i after continual learning of task t, and $\tilde { a } _ { i }$ is the test accuracy of each task i learned from random initialization. ACC is the average performance of all tasks ever seen, which evaluates the overall performance of continual learning. FWT evaluates the average influence of remembering old tasks to new tasks for learning plasticity. BWT evaluates the average influence of learning new tasks to old tasks for memory stability.

The diversity of learners’ predictions is quantified by the average cosine (Cos) or Euclidean (Euc) distance:

$$
\cos = 1 - \frac {1}{K (K - 1)} \sum_ {i = 1, j \neq i} ^ {K} \frac {\left. p _ {i} \cdot p _ {j} \right.}{\left.\left.\left.\left. p _ {i} \right.\right.\right.\right.\left.\left.\left.\left. p _ {j} \right.\right.\right.\right.\left. \right.}, \tag {17}
$$

$$
\operatorname {E u c} = \frac {1}{K (K - 1)} \sum_ {i = 1, j \neq i} ^ {K} \| p _ {i} - p _ {j} \|, \tag {18}
$$

where pi and pj denote the predictions of learners i and j, respectively.

The discrepancy of task distributions in feature space is evaluated by the difficulty of distinguishing them, which is an empirical approximation of the ℋ divergence50,51 in Proposition 1. We train a simple discriminator consisting of a fully connected layer and use binary cross-entropy to measure the average discrimination error on test sets.

The performance of Atari reinforcement tasks is evaluated by the NAR, normalized plasticity (NP) and normalized stability (NS), corresponding to the overall performance, learning plasticity and memory stability, respectively:

$$
\mathrm {N A R} = \sum_ {i = 1} ^ {T} R _ {T, i} / r _ {i}, \tag {19}
$$

$$
\mathrm {N P} = \frac {1}{T - 1} \sum_ {i = 2} ^ {T} R _ {i, i} / r _ {i}, \tag {20}
$$

$$
\mathrm {N S} = \frac {1}{T - 1} \sum_ {i = 1} ^ {T - 1} R _ {T, i} / R _ {i, i}, \tag {21}
$$

where $R _ { t , i }$ is the reward for task i obtained in the test step after learning task t, and ri is the maximum reward for task i obtained in each test step of fine-tuning on the task sequence.

# Reporting summary

Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article.

# Data availability

All benchmark datasets used in this paper are publicly available, including CIFAR-10/10045 (https://www.cs.toronto.edu/~kriz/cifar.html), Omniglot57 (https://www.omniglot.com), CUB-200-201158 (https:// www.vision.caltech.edu/datasets/cub_200_2011/), Tiny-ImageNet17 (https://www.image-net.org/download.php), CORe5059 (https://vlomonaco.github.io/core50/) and Atari games73 (https://github.com/ openai/baselines).

# Code availability

The implementation code is available via Zenodo https://doi. org/10.5281/zenodo.8293564 ref. 74.

# References

1. Chen, Z. & Liu, B. Lifelong machine learning. (San Rafael: Morgan & Claypool Publishers, 2018).   
2. Parisi, G. I., Kemker, R., Part, J. L., Kanan, C. & Wermter, S. Continual lifelong learning with neural networks: a review. Neural Netw. 113, 54–71 (2019).   
3. Kudithipudi, D. et al. Biological underpinnings for lifelong learning machines. Nat. Mach. Intell. 4, 196–210 (2022).   
4. McCloskey, M. & Cohen, N. J. Catastrophic interference in connectionist networks: the sequential learning problem. Psychol. Learn. Motiv. 24, 109–165 (1989).   
5. McClelland, J. L., McNaughton, B. L. & O’Reilly, R. C. Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory. Psychol. Rev. 102, 419 (1995).   
6. Wang, L., Zhang, X., Su, H. & Zhu, J. A comprehensive survey of continual learning: theory, method and application. Preprint at https://arxiv.org/abs/2302.00487 (2023).   
7. Kirkpatrick, J. et al. Overcoming catastrophic forgetting in neural networks. Proc. Natl Acad. Sci. USA 114, 3521–3526 (2017).   
8. Aljundi, R., Babiloni, F., Elhoseiny, M., Rohrbach, M. & Tuytelaars, T. Memory aware synapses: learning what (not) to forget. In Proc. European Conference on Computer Vision 139–154 (Springer, 2018).   
9. Zenke, F., Poole, B. & Ganguli, S. Continual learning through synaptic intelligence. In Proc. International Conference on Machine Learning 3987–3995 (PMLR, 2017).   
10. Chaudhry, A., Dokania, P. K., Ajanthan, T. & Torr, P. H. Riemannian walk for incremental learning: understanding forgetting and intransigence. In Proc. European Conference on Computer Vision 532–547 (Springer, 2018).   
11. Ritter, H., Botev, A. & Barber, D. Online structured laplace approximations for overcoming catastrophic forgetting. Adv. Neural Inf. Process. Syst. 31, 3742–3752 (2018).   
12. Rebufi, S.-A., Kolesnikov, A., Sperl, G. & Lampert, C. H. iCaRL: incremental classifier and representation learning. In Proc. IEEE Conference on Computer Vision and Pattern Recognition 2001–2010 (IEEE, 2017).   
13. Shin, H., Lee, J. K., Kim, J. & Kim, J. Continual learning with deep generative replay. Adv. Neural Inf. Process. Syst. 30, 2990–2999 (2017).   
14. Wang, L. et al. Memory replay with data compression for continual learning. In International Conference on Learning Representations (2021).   
15. Serra, J., Suris, D., Miron, M. & Karatzoglou, A. Overcoming catastrophic forgetting with hard attention to the task. In Proc. International Conference on Machine Learning 4548–4557 (PMLR, 2018).

16. Fernando, C. et al. PathNet: evolution channels gradient descent in super neural networks. Preprint at https://arxiv.org/abs/1701.08734 (2017).   
17. Delange, M. et al. A continual learning survey: defying forgetting in classification tasks. IEEE Trans. Pattern Anal. Mach. Intell. (2021).   
18. Hadsell, R., Rao, D., Rusu, A. A. & Pascanu, R. Embracing change: continual learning in deep neural networks. Trends Cogn. Sci. 24, 1028–1040 (2020).   
19. Shuai, Y. et al. Forgetting is regulated through Rac activity in Drosophila. Cell 140, 579–589 (2010).   
20. Cohn, R., Morantte, I. & Ruta, V. Coordinated and compartmentalized neuromodulation shapes sensory processing in Drosophila. Cell 163, 1742–1755 (2015).   
21. Waddell, S. Neural plasticity: dopamine tunes the mushroom body output network. Curr. Biol. 26, R109–R112 (2016).   
22. Modi, M. N., Shuai, Y. & Turner, G. C. The Drosophila mushroom body: from architecture to algorithm in a learning circuit. Annu. Rev. Neurosci. 43, 465–484 (2020).   
23. Aso, Y. et al. Mushroom body output neurons encode valence and guide memory-based action selection in Drosophila. eLife 3, e04580 (2014).   
24. Aso, Y. & Rubin, G. M. Dopaminergic neurons write and update memories with cell-type-specific rules. eLife 5, e16135 (2016).   
25. Gao, Y. et al. Genetic dissection of active forgetting in labile and consolidated memories in Drosophila. Proc. Natl Acad. Sci. USA 116, 21191–21197 (2019).   
26. Zhao, J. et al. Genetic dissection of mutual interference between two consecutive learning tasks in Drosophila. eLife 12, e83516 (2023).   
27. Richards, B. A. & Frankland, P. W. The persistence and transience of memory. Neuron 94, 1071–1084 (2017).   
28. Dong, T. et al. Inability to activate Rac1-dependent forgetting contributes to behavioral inflexibility in mutants of multiple autism-risk genes. Proc. Natl Acad. Sci. USA 113, 7644–7649 (2016).   
29. Zhang, X., Li, Q., Wang, L., Liu, Z.-J. & Zhong, Y. Active protection: learning-activated Raf/MAPK activity protects labile memory from Rac1-independent forgetting. Neuron 98, 142–155 (2018).   
30. Davis, R. L. & Zhong, Y. The biology of forgetting—a perspective. Neuron 95, 490–503 (2017).   
31. Mo, H. et al. Age-related memory vulnerability to interfering stimuli is caused by gradual loss of MAPK-dependent protection in Drosophila. Aging Cell 21, e13628 (2022).   
32. Cervantes-Sandoval, I., Chakraborty, M., MacMullen, C. & Davis, R. L. Scribble scafolds a signalosome for active forgetting. Neuron 90, 1230–1242 (2016).   
33. Noyes, N. C., Phan, A. & Davis, R. L. Memory suppressor genes: modulating acquisition, consolidation, and forgetting. Neuron 109, 3211–3227 (2021).   
34. Cognigni, P., Felsenberg, J. & Waddell, S. Do the right thing: neural network mechanisms of memory formation, expression and update in Drosophila. Curr. Opin. Neurobiol. 49, 51–58 (2018).   
35. Amin, H. & Lin, A. C. Neuronal mechanisms underlying innate and learned olfactory processing in Drosophila. Curr. Opin. Insect Sci. 36, 9–17 (2019).   
36. Handler, A. et al. Distinct dopamine receptor pathways underlie the temporal sensitivity of associative learning. Cell 178, 60–75 (2019).   
37. McCurdy, L. Y., Sareen, P., Davoudian, P. A. & Nitabach, M. N. Dopaminergic mechanism underlying reward-encoding of punishment omission during reversal learning in Drosophila. Nat. Commun. 12, 1115 (2021).   
38. Berry, J. A., Cervantes-Sandoval, I., Nicholas, E. P. & Davis, R. L. Dopamine is required for learning and forgetting in Drosophila. Neuron 74, 530–542 (2012).

39. Berry, J. A., Phan, A. & Davis, R. L. Dopamine neurons mediate learning and forgetting through bidirectional modulation of a memory trace. Cell Rep. 25, 651–662 (2018).   
40. Aitchison, L. et al. Synaptic plasticity as bayesian inference. Nat. Neurosci. 24, 565–571 (2021).   
41. Schug, S., Benzing, F. & Steger, A. Presynaptic stochasticity improves energy eficiency and helps alleviate the stability– plasticity dilemma. eLife 10, e69884 (2021).   
42. Wang, L. et al. AFEC: active forgetting of negative transfer in continual learning. Adv. Neural Inf. Process. Syst. 34, 22379–22391 (2021).   
43. Benzing, F. Unifying importance based regularisation methods for continual learning. In Proc. International Conference on Artificial Intelligence and Statistics 2372–2396 (PMLR, 2022).   
44. Bouton, M. E. Context, time, and memory retrieval in the interference paradigms of pavlovian learning. Psychol. Bull. 114, 80 (1993).   
45. Krizhevsky, A. et al. Learning multiple layers of features from tiny images. Technical Report, Citeseer (2009).   
46. Shuai, Y. et al. Dissecting neural pathways for forgetting in Drosophila olfactory aversive memory. Proc. Natl Acad. Sci. USA 112, E6663–E6672 (2015).   
47. Chen, L. et al. AI of brain and cognitive sciences: from the perspective of first principles. Preprint at https://arxiv.org/ abs/2301.08382 (2023).   
48. Caron, S. J., Ruta, V., Abbott, L. F. & Axel, R. Random convergence of olfactory inputs in the Drosophila mushroom body. Nature 497, 113–117 (2013).   
49. Endo, K., Tsuchimoto, Y. & Kazama, H. Synthesis of conserved odor object representations in a random, divergent-convergent network. Neuron 108, 367–381 (2020).   
50. Long, M., Cao, Y., Wang, J. & Jordan, M. Learning transferable features with deep adaptation networks. In Proc. International Conference on Machine Learning 97–105 (PMLR, 2015).   
51. Wang, L., Zhang, X., Li, Q., Zhu, J. & Zhong, Y. CoSCL: cooperation of small continual learners is stronger than a big one. In Proc. European Conference on Computer Vision 254–271 (Springer, 2022).   
52. van de Ven, G. M., Tuytelaars, T. & Tolias, A. S. Three types of incremental learning. Nat. Mach. Intell. 4, 1185–1197 (2022).   
53. Riemer, M. et al. Learning to learn without forgetting by maximizing transfer and minimizing interference. In International Conference on Learning Representations (2018).   
54. Schwarz, J. et al. Progress & compress: a scalable framework for continual learning. In Proc. International Conference on Machine Learning 4528–4537 (PMLR, 2018).   
55. Jung, S., Ahn, H., Cha, S. & Moon, T. Continual learning with node-importance based adaptive group sparse regularization. Adv. Neural Inf. Process. Syst. 33, 3647–3658 (2020).   
56. Cha, S., Hsu, H., Hwang, T., Calmon, F. & Moon, T. CPR: classifier-projection regularization for continual learning. In International Conference on Learning Representations (2020).   
57. Lake, B. M., Salakhutdinov, R. & Tenenbaum, J. B. Human-level concept learning through probabilistic program induction. Science 350, 1332–1338 (2015).   
58. Wah, C., Branson, S., Welinder, P., Perona, P. & Belongie, S. The Caltech-UCSD birds-200-2011 dataset. (2011). http://www.vision. caltech.edu/datasets/   
59. Lomonaco, V. & Maltoni, D. Core50: a new dataset and benchmark for continuous object recognition. In Conference on Robot Learning 17–26 (PMLR, 2017).   
60. Ryan, T. J. & Frankland, P. W. Forgetting as a form of adaptive engram cell plasticity. Nat. Rev. Neurosci. 23, 173–186 (2022).   
61. Luo, L. et al. Diferential efects of the Rac GTPase on Purkinje cell axons and dendritic trunks and spines. Nature 379, 837–840 (1996).

62. Tashiro, A., Minden, A. & Yuste, R. Regulation of dendritic spine morphology by the rho family of small gtpases: antagonistic roles of Rac and Rho. Cerebral Cortex 10, 927–938 (2000).   
63. Hayashi-Takagi, A. et al. Disrupted-in-Schizophrenia 1 (DISC1) regulates spines of the glutamate synapse via Rac1. Nat. Neurosci. 13, 327–332 (2010).   
64. Hayashi-Takagi, A. et al. Labelling and optical erasure of synaptic memory traces in the motor cortex. Nature 525, 333–338 (2015).   
65. Martens, J. & Grosse, R. Optimizing neural networks with kronecker-factored approximate curvature. In Proc. International Conference on Machine Learning 2408–2417 (PMLR, 2015).   
66. Knoblauch, J., Husain, H. & Diethe, T. Optimal continual learning has perfect memory and is NP-hard. In Proc. International Conference on Machine Learning 5327–5337 (PMLR, 2020).   
67. Deng, D., Chen, G., Hao, J., Wang, Q. & Heng, P.-A. Flattening sharpness for dynamic gradient projection memory benefits continual learning. Adv. Neural Inf. Process. Syst. 34, 18710–18721 (2021).   
68. Mirzadeh, S. I., Farajtabar, M., Pascanu, R. & Ghasemzadeh, H. Understanding the role of training regimes in continual learning. Adv. Neural Inf. Process. Syst. 33, 7308–7320 (2020).   
69. McAllester, D. A. PAC-Bayesian model averaging. In Proc. Twelfth Annual Conference on Computational Learning Theory 164–170 (ACM, 1999).   
70. Pham, Q., Liu, C., Sahoo, D. & Steven, H. Contextual transformation networks for online continual learning. In International Conference on Learning Representations (2021).   
71. Schulman, J., Wolski, F., Dhariwal, P., Radford, A. & Klimov, O. Proximal policy optimization algorithms. Preprint at https://arxiv. org/abs/1707.06347 (2017).   
72. Lopez-Paz, D. et al. Gradient episodic memory for continual learning. Adv. Neural Inf. Process. Syst. 30, 6467–6476 (2017).   
73. Mnih, V. et al. Playing Atari with deep reinforcement learning. Preprint at https://arxiv.org/abs/1312.5602 (2013).   
74. Wang, L. & Zhang, X. lywang3081/CAF: CAF paper. Zenodo https://doi.org/10.5281/zenodo.8293564 (2023).   
75. Selvaraju, R. R. et al. Grad-CAM: visual explanations from deep networks via gradient-based localization. In Proc. IEEE Conference on Computer Vision and Pattern Recognition 618–626 (IEEE, 2017).

# Acknowledgements

This work was supported by the National Key Research and Development Program of China (2020AAA0106302, to J.Z.), the STI2030-Major Projects (2022ZD0204900, to Y.Z.), the National Natural Science Foundation of China (nos 62061136001 and 92248303, to J.Z., 32021002, to Y.Z., U19A2081, to H.S.), the Tsinghua-Peking Center for Life Sciences, the Tsinghua Institute for Guo Qiang, and the High Performance Computing Center, Tsinghua University. L.W. was also supported by the Shuimu Tsinghua Scholar. J.Z. was also supported by the New Cornerstone Science Foundation through the XPLORER PRIZE.

# Author contributions

L.W., X.Z., J.Z. and Y.Z. conceived the project. L.W., X.Z., Q.L. and M.Z. designed the computational model. X.Z. performed the theoretical analysis, assisted by L.W. L.W. performed all experiments and analysed the data. L.W., X.Z. and Q.L. wrote the paper. L.W., X.Z., Q.L., M.Z., H.S., J.Z. and Y.Z. revised the paper. J.Z. and Y.Z. supervised the project.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s42256-023-00747-w.

Correspondence and requests for materials should be addressed to Jun Zhu or Yi Zhong.

Peer review information Nature Machine Intelligence thanks Gido van de Ven and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permissions information is available at

www.nature.com/reprints.

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

© The Author(s), under exclusive licence to Springer Nature Limited 2023

# Reporting Summary

NaturePortfolioishstmprovetheeproducibitoftheorkthatwepublish.isformprovidesstructureforconsistencyandtrasparency inreporting.Forfurtherinformationon NaturePortfoliopolicies,seeour EditorialPoliciesandtheEditorialPolicyChecklist.

# Statistics

Foraltatisticalaalysofithatefolowingitemsareprsetintfgurelegend,tableegend,aintextorethdsctio

n/a|Confirmed

□ The exactsample size(n)for each experimentalgroup/condition,given asadiscrete number and unit of measurement   
□区Astatement on whether measurements weretaken from distinct samples or whether thesame sample was measuredrepeatedly   
Only common tests should be described solely byname;describemorecomplextechniques in the Methodssection.   
A description of all ovariates tested   
区Adescription ofanyassumptions orcorrections,such as tests of normalityand adjustment formultiplecomparisons   
Afuldescriptiofthestatisticalparametersincdingcetraltendency(eg.means)orotherbasicestimates(e.regresiocoficient) ANDariatiteatoorsdtitatintinras   
区 r   
区For Bayesian analysis,information on the choiceof priors and Markovchain Monte Carlo settings   
区For hierarchicalandcomplexdesigns,identificationoftheappropriate levelfortestsandfullreporting ofoutcomes   
区 Estimates of effect sizes (e.g. Cohen's d,Pearson's r), indicating how they were calculated

# Software and code

Policy information about availability of computer code

Data collection

Allexperimetsreerfditbcaseh-1-0glotageetB1t Please refer to our data availability statement.

Data analysis

Weperformdataanalysiswithbothcustomcode(includedinsuplementarymaterials,pleaserefertoourcodeavailabilitystatement)and Excel,and create all content figures with Prism 8.

# Data

Policy information about availability of data

Allmanuscriptsmustincludeadataavailabilitystatement.Tistatementshouldprovidethefollwinginformation,wherealicable:

- Accession codes,unique identifiers,or web links for publicly available datasets   
- A description of any restrictions on data availability   
- For clinical datasets or third party data,please ensure that the statement adheres to our policy

All datasets used in this paperarepubliclyavailable.We include necessrydownloadtoolsand instructionsin our code.

Policy information about studies involving human research participants and Sex and Gender in Research.

<table><tr><td>Reporting on sex and gender</td><td>N/A</td></tr><tr><td>Population characteristics</td><td>N/A</td></tr><tr><td>Recruitment</td><td>N/A</td></tr><tr><td>Ethics oversight</td><td>N/A</td></tr></table>

# Field-specific reporting

Pleaseselectheoebelowtatisthebestfitforyourresearch.Ifyouarenotsurereadtheappropratesectionsbeforemaingyourelection.

Life sciences

Behavioural & social sciences

Ecological,evolutionary & environmental sciences

Fora reference copy of the document with allsections,see nature.com/documents/nr-reporting-summary-flat.pdf

# Life sciences study design

<table><tr><td>Sample size</td><td>To obtain reliable results, all experiments are performed by more than 5 runs with different random seeds and task orders. This is a common choice following previous works in this field.</td></tr><tr><td>Data exclusions</td><td>No data were excluded in our analysis.</td></tr><tr><td>Replication</td><td>All results can be successfully replicated.</td></tr><tr><td>Randomization</td><td>N/A</td></tr><tr><td>Blinding</td><td>N/A</td></tr></table>

# Reporting for specific materials, systems and methods

Materials & experimental systems   

<table><tr><td>n/a</td><td>Involved in the study</td></tr><tr><td>×</td><td>Antibodies</td></tr><tr><td>×</td><td>Eukaryotic cell lines</td></tr><tr><td>×</td><td>Palaeontology and archaeology</td></tr><tr><td>×</td><td>Animals and other organisms</td></tr><tr><td>×</td><td>Clinical data</td></tr><tr><td>×</td><td>Dual use research of concern</td></tr></table>

Methods   

<table><tr><td>n/a</td><td>Involved in the study</td></tr><tr><td>×</td><td>□ ChIP-seq</td></tr><tr><td>×</td><td>□ Flow cytometry</td></tr><tr><td>×</td><td>□ MRI-based neuroimaging</td></tr></table>