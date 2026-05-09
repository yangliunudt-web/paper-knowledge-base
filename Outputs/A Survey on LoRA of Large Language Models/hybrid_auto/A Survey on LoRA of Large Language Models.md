---
title: "A Survey on LoRA of Large Language Models"
date: "2024-01-01"
year: 2024
journal: "Journal of Computer Science and Technology"
abstract: "Low-Rank Adaptation (LoRA), which updates the dense neural network layers with pluggable low-rank matrices, is one of the best performed parameter efficient fine-tuning paradigms. Furthermore, it has significant advantages in cross-task generalization and privacy-preserving. Hence, LoRA has gained much attention recently, and the number of related literature demonstrates exponential growth. It is necessary to conduct a comprehensive overview of the current progress on LoRA. This survey categorizes and reviews the progress from the perspectives of (1) downstream adaptation improving variants that improve LoRA's performance on downstream tasks; (2) cross-task generalization methods that mix multiple LoRA plugins to achieve cross-task generalization; (3) efficiency-improving methods that boost the computation-efficiency of LoRA; (4) data privacy-preserving methods that use LoRA in federated learning; (5) application. Besides, this survey also discusses the future directions in this field. At last, we provide a Github page for readers to check the updates and initiate discussions on this survey paper."
abstract_cn: "系统综述大语言模型低秩适配（LoRA）方法：从下游任务适配改进、跨任务泛化、计算效率提升、联邦学习隐私保护、应用五个方面梳理现有工作。LoRA 通过可插拔低秩矩阵更新稠密层，在参数量、计算效率、跨任务泛化和隐私保护方面具有显著优势，相关文献呈指数增长。本文提供完整分类和未来方向讨论。"
cite: "Mao Y R, Ge Y H, Fan Y J, et al. A Survey on LoRA of Large Language Models[J]. Journal of Computer Science and Technology, 2024, 39(1): 1-20."
aiSum: "LoRA 综述：下游适配改进（打破低秩瓶颈、动态秩分配）、跨任务泛化（混合 LoRA 模块）、计算效率提升（减少单模块成本、加速多模块服务）、联邦学习隐私保护、应用场景梳理。"
confidence: "high"
authors:
  - "Yuren MAO"
  - "Yuhang GE"
  - "Yijiang FAN"
  - "Wenyi XU"
  - "Yu MI"
  - "Zhonghao HU"
  - "Yunjun GAO"
keywords:
  - "[[Low-Rank Adaptation]]"
  - "[[LoRA]]"
  - "[[Large Language Models]]"
  - "[[LLMs]]"
---

# A Survey on LoRA of Large Language Models

Yuren MAO1, Yuhang GE1, Yijiang FAN1, Wenyi XU1, Yu MI1, Zhonghao HU1, Yunjun GAO(B)1

1 Zhejiang University, Hangzhou 310007, China

© Higher Education Press 2024

Abstract [[Low-Rank Adaptation]] ([[LoRA]]), which updates the dense neural network layers with pluggable low-rank matrices, is one of the best performed parameter efficient fine-tuning paradigms. Furthermore, it has significant advantages in crosstask generalization and privacy-preserving. Hence, [[LoRA]] has gained much attention recently, and the number of related literature demonstrates exponential growth. It is necessary to conduct a comprehensive overview of the current progress on [[LoRA]]. This survey categorizes and reviews the progress from the perspectives of (1) downstream adaptation improving variants that improve [[LoRA]]’s performance on downstream tasks; (2) cross-task generalization methods that mix multiple [[LoRA]] plugins to achieve cross-task generalization; (3) efficiencyimproving methods that boost the computationefficiency of [[LoRA]]; (4) data privacy-preserving methods that use [[LoRA]] in federated learning; (5) application. Besides, this survey also discusses the future directions in this field. At last, we provide a Github page 1 for readers to check the updates and initiate discussions on this survey paper.

Keywords [[Low-Rank Adaptation]], [[LoRA]], [[Large Language Models]], [[LLMs]]

# 1 Introduction

Rapidly increasing parameter scales of pre-training language models improves their generalization ability and brings emergent abilities. In the last few years, the parameter scales of pre-training languages models have increased by thousands of times (e.g., from 330M parameter BERT [1] to 540B parameter PaLM [2]). These pre-training language models having large parameter scales are termed [[Large Language Models]] ([[LLMs]]). Nevertheless, due to the knowledge boundaries of the [[LLMs]], their abilities on some downstream tasks are still limited. To expand the knowledge boundaries, it remains necessary to fine-tune [[LLMs]] on the downstream tasks.

However, fine-tuning the full parameters of an LLM, namely full fine-tuning, is extremely computationally expensive, for example, full fine-tuning

Received month dd, yyyy; accepted month dd, yyyy

of a LLaMA2-7B [3] model requires approximately 60GB of memory, which exceeds the capacity of common consumer GPUs [4]. To reduce the computational cost, various parameter-efficient fine-tuning (PEFT) methods have been proposed [5]. They adapt [[LLMs]] to downstream tasks by only fine-tuning a small number of (extra) model parameters. From the perspective of whether extra parameters are involved, PEFT methods can be divided into two categories: extra-parameter methods and intra-parameter methods. The extraparameter methods freeze all of the original parameters of an LLM and insert a set of learnable parameters to optimize the model input or model layers such as adapter tuning [6] and prompt tuning [7]. By contrast, intra-parameter methods freeze most of the original parameters of an LLM and only tune a small number of parameters of the LLM such as BitFit [8], LISA [4] and [[LoRA]] [9].

When we do not have access to modify the model architecture, intra-parameter methods are desirable. Among the intra-parameter methods, [[LoRA]] is the most widely used one, because it can achieve a comparable or better downstream adaptation performance to the full fine-tuning on a range of downstream tasks [9] and is easy to implement. Besides, there are many variants have been proposed to further improve the downstream adaptation ability of [[LoRA]] on more challenging downstream tasks.

[[LoRA]] achieves parameter efficiency by updating the dense neural network layers of an LLM with pluggable low-rank matrices. These matrices (a.k.a, [[LoRA]] plugins) are independent of the LLM, which can be stored and reused in other related downstream tasks. Furthermore, these [[LoRA]] plugins can be combined to achieve cross-task gener-

alization, which can facilitate multi-task learning, domain adaptation, and continual learning.

As the [[LoRA]] modules accumulate, the computation cost of managing [[LoRA]] modules is increasing. Although [[LoRA]] is computation-efficient, the computational cost of managing a larger number of [[LoRA]] modules is unignorable. It is necessary to further improve the computation efficiency of [[LoRA]]. The improvement can come from reducing the computation cost of single [[LoRA]] modules and accelerating the scalable serving of multiple modules. It can boost the application of [[LoRA]] in realworld use cases, such as Generative-as-a-Service (GaaS) cloud products.

In some cases, the training data are privately owned by multiple clients and cannot be centralized. To adapt [[LLMs]] with the distributed training data, we can adopt federated learning to protect the data privacy of each client. However, federated learning suffers expensive communication and computation costs. To reduce costs, [[LoRA]] is a natural choice. Its parameter-efficient nature helps to reduce the computation cost of each client and the communication cost of sharing parameters across clients. Furthermore, the pluggable feature of [[LoRA]], which supports the localization or encryption of personalized parameters, enhances privacy protection within federated learning. Therefore, [[LoRA]] has a great potential for privacy-preserving.

While some previous surveys have mentioned [[LoRA]] [5, 10, 11], they mainly focus on PEFT and only introduce a small number of [[LoRA]]-related works, lacking systematic treatment and comprehensive overview on [[LoRA]] and its variants. In this survey, we give a comprehensive overview of the current progress on [[LoRA]] for methods (1) improving downstream adaption performance of

[[LoRA]]; (2) mixing [[LoRA]] modules to achieve crosstask generalization; (3) boosting the computationefficiency of [[LoRA]]; (4) adopting [[LoRA]] in federated learning. Besides, the application of [[LoRA]] is briefly introduced. This taxonomy of [[LoRA]]related methods is illustrated in Figure 1. This survey is expected to give comprehensive background knowledge, research trends and technical insights for [[LoRA]].

The rest of this survey is organized as follows. Section 2 introduces the background knowledge of [[LoRA]], and Section 3 introduces the [[LoRA]]’s variants that aim to improve the downstream adaptation performance. In Section 4, we review the [[LoRA]] mixture methods that mix [[LoRA]] modules to achieve cross-task generalization. The [[LoRA]]driven federated learning methods are introduced in Section 6. Section 7 reports the applications of [[LoRA]]. We conclude this survey and discuss the future directions in Section 8.

# 2 [[Low-Rank Adaptation]] ([[LoRA]])

The Low-dimensional intrinsic dimensionality hypothesis [189] presents that over-parameterized models reside on a low intrinsic dimension, which demonstrates that we can achieve proper learning performance by only updating parameters related to the intrinsic rank. Based on this hypothesis, [[LoRA]] [9] proposes to update dense layers in a model with low-rank matrices. It can achieve both parameter- and computational- efficiency. In this section, we first introduce the details of [[LoRA]] and then introduce existing works that focus on the theoretical analysis of [[LoRA]]. Furthermore, we demonstrate [[LoRA]]’s efficiency in practice. At last, this section presents that [[LoRA]] can be used in other use cases except fine-tuning.

# 2.1 [[LoRA]]

Given a dense neural network layer parameterized by $W _ { 0 } \in \mathbb { R } ^ { d \times k }$ , to adapt it to a downstream task, we update it with $\Delta W \in \mathbb { R } ^ { d \times k }$ and obtain an updated layer parameterized by $W = W _ { 0 } + \Delta W$ . For full fine-tuning, ∆W is computed based on gradients of all the $d { \times } k$ parameters for the layer, which is computationally expensive and requires a large amount of GPU memory for [[LLMs]]. To improve the computational efficiency, [[LoRA]] decomposes ∆W into two small matrices $B \in \mathbb { R } ^ { d \times r }$ and $A \in \mathbb { R } ^ { r \times k }$ , i.e.,

$$
W = W _ {0} + \alpha B A \tag {1}
$$

where r ≪ min{d k}, B and A are initialized with a random Gaussian distribution and zero respectively,  represents the scaling factor that controls the strength of updates. The parameter number of [[LoRA]] is $r \times ( d + k )$ , which is significantly less than $d \times k .$ Figure 2 (a) and (b) compare the structures of full fine-tuning and [[LoRA]].

[[LoRA]] is highly parameter efficient for it updates only a small subset of model parameters, which reduces the memory and computational requirements for fine-tuning without increasing inference latency [190]. Furthermore, The parameter efficiency can be further improved by extending from the low-rank matrix to low-rank tensor [191] or combining with the Kronecker decomposition [192, 193]. Except for parameter efficiency, [[LoRA]] is also pluggable for the [[LoRA]] parameters that can be separated from the model after training. The pluggable character of [[LoRA]] enables it to be shared and reused by multiple users [98]. When we have [[LoRA]] modules for multiple tasks, we can combine these modules and expect a proper cross-task generalization perfor-

![](images/06463f8c95b8022ca2be8f707c47bbb51bfecb452b2efe34b9a3deed139989c6.jpg)  
[[Low-Rank Adaptation]] of [[Large Language Models]]   
Fig. 1 The taxonomy of this paper.

![](images/6500f9bdd1acbf863cbe92261dffe819a5a6826b82fa106b6e17501d0f5a0a37.jpg)  
(a) Full Fine-Tuning

![](images/e46476afcce73d57a54e4b852cb7ce73bebc1d026cc59d29bd48893e4db81d0b.jpg)  
(b) [[LoRA]]

![](images/6d98b533aa89f75e2887701a6f912732bf08fd65477f6c4f6e21779c5b6a623e.jpg)  
(c) Breaking the Low-rank Bottleneck

![](images/92c5f92aecf8f8ec70f314468f8bfe1b2d22564ad4f33de48260e520d07a3119.jpg)  
(d) Dynamic Rank Allocation   
Fig. 2 An illustration of full fine-tuning (a), [[LoRA]] (b) and its variants for improving downstream adaptation, which includes breaking the low-rank bottleneck (c) and dynamic rank allocation (d).

mance [60]. Besides, the low-rank mechanism of [[LoRA]] is compatible with other parameter-efficient methods, such as adapter [194, 195]. Besides, [[LoRA]] can achieve proper downstream adaptation performance on various downstream tasks. For example, on MMLU [196] benchmark, comparing with full fine-tuning, fine-tuning with [[LoRA]] can achieve comparable or even better performance across 57 tasks [4].

In practice, for a Transformer-based LLM, the dense layers typically consist of two types of weight matrices: the projection matrices in attention modules and feed-forward neural (FFN) modules. The experiments mentioned above are conducted based on the original [[LoRA]] settings, applying it to the query and value weight matrices in the attention modules. It is worth mentioning that subsequent work shows that applying it to the FFN layers can further improve model performance [197].

# 2.2 Theoretical Analysis

To understand why [[LoRA]] is effective and how [[LoRA]] can be more effective, several works have provided theoretical analyses from various aspects. To answer the question that why [[LoRA]] is effective, Malladi et al. [12] analyze the fine-tuning dynamics of [[LoRA]] from the kernel view and demon-

strate that in the lazy regime, [[LoRA]] fine-tuning is nearly equivalent to full fine-tuning. Besides, Zeng et al. [16] provides a theoretical analysis of the [[LoRA]]’s expressive power for both fully connected neural networks (FNNs) and Transformer networks (TFNs). They proved that [[LoRA]] can adapt any model f to accurately represent any smaller target model ¯f if [[LoRA]]-rank ≥ (width of $\begin{array} { r } { f ) \times \frac { d e p t h o f \bar { f } } { d e p t h o f f } } \end{array}$ under a mild assumption, where the depth and width are the number of layers and the number of neurons of the layer having the largest number of neurons, respectively. Moreover, they quantify the approximation error when the [[LoRA]]rank falls below this threshold. Regarding TFNs, they showed that any model can be adapted to a target model of equivalent size using a rank-$\left( { \frac { \mathrm { e m b e d d i n g ~ s i z e } } { 2 } } \right)$  embedding size  for [[LoRA]]. Additionally, Koubbi et al. [13] utilize the mathematical framework for Transformers established by [198–200] to investigate how variations in attention parameters and initial token values impact the structural dynamics of token clusters.

As to the question that how [[LoRA]] can be more effective, Jang et al. [14] analyze the finetuning of [[LoRA]] within the neural tangent kernel (NTK) [201] framework when N data points are available. They demonstrate that employing a rank

$r \ \gtrsim \ \sqrt { N }$ in [[LoRA]] helps to avoid spurious local minima and facilitates the discovery of lowrank solutions that exhibit good generalization. Besides, Zhu et al. [15] observe that the project-down matrix A is utilized for extracting features from the input, while the project-up matrix B employs these features to create the desired output. Based on this observation, they demonstrate that freezing the project-down matrix A while tuning only the project-up matrix B leads to better generalization compared to tuning both matrices, in addition to achieving a 2× reduction in parameters.

# 2.3 Efficiency in Practice

The computational efficiency of [[LoRA]] is significantly higher than that for full fine-tuning. Taking fine-tuning the dense weight matrix of the first FFN layer in LLaMA2-7B as an example, full fine-tuning needs to fine-tune $1 1 , 0 0 8 \times 4 , 0 9 6 \ : =$ 45 088 768 parameters while [[LoRA]] only needs to tune $( 1 1 , 0 0 8 \times 4 ) + ( 4 \times 4 , 0 9 6 ) = 6 0 .$ 416 parameters when r = 4. For this layer, [[LoRA]] only adjusts nearly one-thousandth of the parameters compared to full fine-tuning.

[[LoRA]] can significantly decrease the memory usage of fine-tuning an LLM, which can be divided into four parts: (1) Model Memory: the memory required to store the model weights; (2) Activation Memory: the memory occupied by intermediate activations during forward propagation. It mainly depends on factors such as batch size and sequence length; (3) Gradient Memory: the memory required to store gradients during backpropagation. The gradients are only calculated for trainable parameters; (4) Optimization Memory: the memory used to store optimizer states. For example, the Adam optimizer stores the “first moment” and

“second moment” of trainable parameters.

Pan et al. [4] provides a comprehensive empirical comparison between full fine-tuning and [[LoRA]] fine-tuning on an LLaMA2-7B model with batch size 1, utilizing a single NVIDIA RTX4090 (24GB) GPU. According to this study, full finetuning requires approximately 60GB of memory, which exceeds the capacity of an RTX4090 GPU; by contrast, [[LoRA]] fine-tuning only needs about 23GB of memory. [[LoRA]] significantly reduces memory usage and makes fine-tuning LLaMA2- 7B feasible on a single NVIDIA RTX4090 (24GB) GPU. Specifically, due to fewer trainable parameters, both optimization memory and gradient memory decrease significantly by approximately 25GB and 14GB respectively. On the other hand, while [[LoRA]] introduces additional “incremental parameters” resulting in slight increases in activation memory and weight memory (totaling about 2GB), this increase is negligible when considering the overall reduction in memory. Moreover, reducing memory brings an acceleration of forward propagation. [[LoRA]] is 1 9× times faster compared to full fine-tuning.

# 2.4 Beyond Fine-tuning

Besides fine-tuning, [[LoRA]] can be applied to other learning paradigms, such as pre-training [17, 19] and continual training [20]. For pre-training, Re[[LoRA]] [17] and MoRA [18] are proposed to use low-rank updates to train high-rank networks; moreover, LTE [19] is proposed to perform parallel training of multiple low-rank heads across computing nodes to minimize the need for frequent synchronization, which facilitates the utilization of [[LoRA]] in pre-training. As for continual training, there are several methods have been pro-

posed to address the catastrophic forgetting problem. Inf[[LoRA]] [20] addresses catastrophic forgetting by reparameterizing pre-trained weights with a minimal set of parameters in a subspace. GS-[[LoRA]] [21] uses group sparse regularization to automatically select specific [[LoRA]] groups while zeroing out others to mitigate catastrophic forgetting effects. I-[[LoRA]] [202] leverages dual-memory experience replay combined with [[LoRA]] parameter interpolation to combat catastrophic forgetting.

Furthermore, [[LoRA]] can be used to overcome the limited context size for [[LLMs]] [3,23]. For instance, Long[[LoRA]] [3] successfully computaitional efficiently extends the context window of LLaMA2- 7B [203] from 4k to 100k tokens by combining [[LoRA]] with shifted sparse attention. However, Long[[LoRA]] does not match the efficiency of vanilla attention due to chaotic attention head structures and unnecessary information exchange between token groups. To address these issues, Sink[[LoRA]] [23] introduces Sink Fixed Attention (SF-Attn) to proportionally returns cyclically shifted groups of attention heads to their un-shifted state and achieves proper performance.

# 3 Downstream Adaptation Improving

Although [[LoRA]] can achieve proper adaptation performance on some downstream tasks, there is still a performance gap between [[LoRA]] and full finetuning on many downstream tasks, such as mathematical reasoning [5, 204, 205]. To fill this gap, many methods are proposed to further improve the downstream adaptation performance of [[LoRA]]. Typically, existing methods improve the downstream adaptation performance from the following perspectives: (1) breaking the low-rank bottleneck, refer to Figure 2 (c); (2) adaptively allo-

cating the ranks of different [[LoRA]] modules, refer to Figure 2 (d); (3) optimizing the learning procedure of [[LoRA]]; (4) combining with other learning paradigms. In this section, we introduce these four types of methods respectively.

# 3.1 Breaking the Low-rank Bottleneck

The low-rank updates enable [[LoRA]] to be parameter efficient; however, it restricts [[LLMs]]’ ability to memorize downstream knowledge and generalization on downstream tasks [18, 204–207]. This low-rank limitation causes inferior performance of [[LoRA]] in knowledge- and skill-intensive domains comparing to full-fine tuning, such as code and math. Experimental study [205] demonstrates that the rank for full fine-tuning is significant (10- 100 ×) higher than that for [[LoRA]], and increasing the rank of [[LoRA]] updation can narrow the performance gap between [[LoRA]] and full finetuning. To increase the rank of [[LoRA]] and improve its performance, several methods have been proposed [17,24,27,208], which typically increase the rank through (1) stacking [[LoRA]]s along learning iterations; (2) updating as gradient compressors; (3) co-updating LLM and [[LoRA]] modules during finetuning.

# 3.1.1 Stacking [[LoRA]]s along Fine-tuning

Matrix rank is subadditive, i.e., $r a n k ( M _ { 1 } + M _ { 2 } ) \leq$ $r a n k ( M _ { 1 } ) + r a n k ( M _ { 2 } )$ for matrices $M _ { 1 }$ and $M _ { 2 }$ that have the same size. Based on the subadditivity, we can aggregate multiple [[LoRA]] modules together to increase the rank and break the low-rank bottleneck. Following this idea, Re[[LoRA]] [17] proposes a merge-and-reinit procedure for [[LoRA]], which periodically merges the [[LoRA]] modules to the LLM and then reinitializes the [[LoRA]] modules during fine-tuning. It equals stacking mul-

tiple [[LoRA]] modules along with fine-tuning and can increase the rank of the overall updates. Similarly, COLA [24] proposes another mergeand-reinit method based on Frank-Wolfe algorithm [209]. However, ME[[LoRA]] [25] points out that the merge-and-reinit procedure does not necessarily guarantee an increase in rank, because there can be overlap between the series of [[LoRA]] modules along fine-tuning. To solve this problem, ME[[LoRA]] proposes to decompose the [[LoRA]] modules into smaller mini [[LoRA]]s and then parallelly stack these mini [[LoRA]]s, whose effectiveness in increasing the rank is theoretically verified.

# 3.1.2 Updating as Gradient Compressor

The above methods break the low-rank bottleneck in the parameter space. As a supplement, F[[LoRA]] [26] finds that [[LoRA]] performs a fixed random projection to compress gradients and restricts the total weight matrix change to low-rank. To overcome this low-rank bottleneck in gradient space, F[[LoRA]] proposes to resample the random projection, which is demonstrated to largely recover the performance of full-matrix SGD.

# 3.1.3 Co-updating LLM and [[LoRA]]

The above two kinds of methods focus on improving the representation ability of [[LoRA]] itself. Different from them, Delta-[[LoRA]] [27] proposes to jointly update the LLM and [[LoRA]] modules, which directly updates the high-rank LLM and can gain better representation capable than updating [[LoRA]] independently. It updates the LLM based on the difference between two [[LoRA]] modules of two consecutive iterations, which enables it to update the LLM without any extra memory.

# 3.2 Dynamic Rank Allocation

For the rank of [[LoRA]], higher is not always better. The abundant [[LoRA]] ranks may cause degeneration in both performance and efficiency. Furthermore, the importance of weights can vary across different layers of a Transformer model during fine-tuning, requiring different ranks for each layer. [28, 31, 33, 35]. Therefore, assigning the same rank to [[LoRA]] modules of different layers is not the optimal choice. It is better to adaptively allocate ranks to [[LoRA]] modules of different layers. Existing methods adaptively allocate ranks for [[LoRA]] modules from the perspectives of (1) singular value decomposition (SVD); (2) single-rank decomposition (SRD); (3) rank sampling.

# 3.2.1 SVD-based Methods

Decomposing a matrix with singular value decomposition (SVD) and selectively truncating its singular values is an effective way to control the rank of the matrix. Inspire by SVD, we can decompose the [[LoRA]] parameter matrix BA into an SVD form, i.e, PΛQ where P and Q are orthogonal and Λ is a non-negative diagonal matrix. By controlling the elements in Λ, we can control the rank of BA and allocate ranks for [[LoRA]] modules. Following this idea, several rank allocation methods approximate the SVD decomposition for BA and allocate the ranks by filtering the diagonal matrix. For instance, Ada[[LoRA]] [28] approximates the SVD decomposition by regularizing the orthogonality of P and Q. Then, it drops unimportant singular values based on novel importance scoring methods. Similarly, Sa[[LoRA]] [29] also introduces an orthogonality regularization for P and Q; by contrast, it drops unimportant singular values based on the $L _ { 0 }$ norm. However, the above methods are not effi-

cient enough for they start with a high rank and then reduce the rank iteratively, which brings a predefined budget [30]. To solve this problem, Incre[[LoRA]] [30] proposes to start from a single rank and then automatically increase the rank based on a heuristic importance score, where the orthogonality regularization is also involved while the elements in Λ is not required to be non-negative.

# 3.2.2 SRD-based Methods

However, the orthogonality regularization brings unignorable computational costs for [[LoRA]] and degenerates its efficiency. To address this problem, several methods omit the orthogonality requirement of SVD and directly decompose BA into single-rank components. Then, they allocate the ranks by selecting the proper components.

# DoRA (Dynamic [[Low-Rank Adaptation]]) [31]

proposes to decompose the [[LoRA]] parameter matrix BA into single-rank components and prunes the components based on a heuristic importance score. Similarly, Auto[[LoRA]] [32] also decomposes the [[LoRA]] parameter matrix BA into single-rank components, but it prunes the components based on meta-learning. SoRA [33] eliminates the orthogonality regularization and filters columns and rows of P and Q (their combination can be regarded as single-rank components) by directly controlling the diagonal matrix. It controls the diagonal matrix by formulating them as a set of learnable gating units which are updated in the fine-tuning procedure. A[[LoRA]] [34] also filters the components by using gating units; by contrast, it learns the gating units based on neural architecture search [210].

# 3.2.3 Rank Sampling-based Methods

In the SVD parameterization- and component-wise decomposition-based methods, we need to spend

the extra computational costs to search proper ranks. To avoid the extra cost, Dy[[LoRA]] [35] points out that we can allocate ranks directly by random sampling. In each training step, it samples a value b from a pre-defined discrete distribution and allocates b as the rank. Then, the matrices A and B are truncated to rank-b. In the fine-tuning procedure, only the parameters on the b-th row of A and bth column of B are tunable while other parameters are frozen. Besides, the distribution can be defined based on users’ preferences.

# 3.3 Optimizing the Learning Procedure

In practice, [[LoRA]] converges more slowly than full fine-tuning. Moreover, it is also sensitive to hyperparameters and suffers from overfitting. These issues affect [[LoRA]]’s efficiency and hinder its downstream adaptation performance. To address these issues, researchers have developed several approaches to optimize the learning procedure of [[LoRA]], which can be categorized into the following three types: (1) Initialization Improvement; (2) Gradient Update Optimization; (3) Overfitting Mitigation.

# 3.3.1 Initialization Improvement

[[LoRA]] usually initializes its parameter matrices A and B using Gaussian noise and zeros respectively. There are two simple schemes: Init[A], which sets matrix B to zero and randomly initializes matrix A, and Init[B], which does the reverse. Literature [36] compares these two schemes and concludes that Init[A] is better through theoretical analysis. It reveals that Init[A] allows using a larger learning rate without causing instability, making the learning process more efficient. However, even with init[A], this random initialization method still results in small initial gradients, leading to slower

convergence. To solve this, PiSSA [37] initializes [[LoRA]] with the principal singular components of the pre-trained matrix. Since principal singular components represent the most significant directions in the matrix, aligning the initial weights with these components can accelerate convergence and improve performance. In contrast, Mi[[LoRA]] [38] initializes [[LoRA]] with the minor singular components. Given that random initialization of low-rank matrices can interfere with the important features learned in the pre-trained matrix, it reduces this interference to improve overall performance while adapting to new tasks.

# 3.3.2 Gradient Update Optimization

To further enhance the convergence and reliability of [[LoRA]], several studies have proposed improvements from the perspective of gradient updates. [39] introduces a scaled gradient method based on Riemannian optimization, which incorporates an r×r preconditioner item in the gradient update step to improve the convergence and hyperparameter robustness of [[LoRA]]. Through theoretical analysis, [[LoRA]]+ [40] discovered the necessity of setting a proportional learning rate for matrices A and B to achieve stable feature learning and accelerate convergence. Res[[LoRA]] [41] introduced residual connections into [[LoRA]] to optimize the gradient propagation path, speeding up training convergence and enhancing model performance. Similarly, SIBO [42] mitigate over-smoothing by injecting residual connections of initial token representations into [[LoRA]]’s input. Additionally, to further reduce computational resources, literature [43] employs gradient-free optimization methods such as CMA-ES and FWA to optimize [[LoRA]], demonstrating competitive performance in few-shot NLU tasks. Besides, DoRA (Weight-Decomposed Low-

Rank Adaptation) [44] constrains the gradient update, focusing on the directional change of the parameter. It decomposes pre-trained weight into two components, direction and magnitude, and applies [[LoRA]] only to the direction component to enhance training stability.

# 3.3.3 Overfitting Mitigation

Although [[LoRA]] effectively reduces the number of trainable parameters compared to full finetuning, some studies have shown that [[LoRA]] is also prone to overfitting [47], which contradicts previous views. To address this issue, Bi[[LoRA]] [45] adopts a bi-level optimization strategy. It alternately trains the singular vectors and singular values of the low-rank increment matrix on different subsets of the training data. This approach avoids the simultaneous optimization of parameters at different levels on a single dataset, thus mitigating overfitting. In addition, literature [46] applies dropout to [[LoRA]] parameters to reduce overfitting, while HiddenKey [47] employs columnwise dropout for attention layers and element-wise dropout for feedforward layers.

# 3.4 Combining with other Learning Paradigms

[[LoRA]] is compatible with other learning paradigms, such as Bayesian Learning, Incontext Learning and Active Learning. Combining [[LoRA]] with these learning paradigms can address several problems that hurt the downstream adaptation performance. For example, combining with Bayesian Learning, Laplace-[[LoRA]] [48] can relieve the overconfidence phenomenon that happened in downstream adaptation. Combining with In-context Learning, PILLOW [49] aims to solve the low-resource dilemmas existing in some downstream tasks. Combining with Active

Table 1 Performance of [[LoRA]] and its variants for RoBERTa-base model on the GLUE benchmark. We report Matthew’s correlation for CoLA, Pearson correlation for STS-B, and accuracy for the other datasets. The results are reported according to the results reported in literature [9, 32, 45, 89, 90].   

<table><tr><td>Method</td><td># Params</td><td>SST-2</td><td>MPRC</td><td>CoLA</td><td>QNLI</td><td>RTE</td><td>STS-B</td></tr><tr><td>Tied-[[LoRA]] [213]</td><td>0.043M</td><td>94.4</td><td>88.5</td><td>61.9</td><td>92.0</td><td>76.2</td><td>89.8</td></tr><tr><td>Auto[[LoRA]] [32]</td><td>0.3M</td><td>94.9</td><td>89.4</td><td>61.3</td><td>92.9</td><td>77.0</td><td>90.8</td></tr><tr><td>Dy[[LoRA]] [35]</td><td>0.3M</td><td>94.3</td><td>89.5</td><td>61.1</td><td>92.2</td><td>78.7</td><td>91.1</td></tr><tr><td>Ada[[LoRA]] [28]</td><td>0.3M</td><td>94.5</td><td>88.7</td><td>62.0</td><td>93.1</td><td>81.0</td><td>90.5</td></tr><tr><td>FourierFT [90]</td><td>0.024M</td><td>94.2</td><td>90.0</td><td>63.8</td><td>92.2</td><td>79.1</td><td>90.8</td></tr><tr><td>VeRA [88]</td><td>0.043M</td><td>94.6</td><td>89.5</td><td>65.6</td><td>91.8</td><td>78.7</td><td>90.7</td></tr><tr><td>Full Fine-tuning [9]</td><td>125M</td><td>94.8</td><td>90.2</td><td>63.6</td><td>92.8</td><td>78.7</td><td>91.2</td></tr><tr><td>[[LoRA]] [9]</td><td>0.3M</td><td>95.1</td><td>89.7</td><td>63.4</td><td>93.3</td><td>78.4</td><td>91.5</td></tr><tr><td>VB-[[LoRA]] [89]</td><td>0.023M</td><td>94.4</td><td>89.5</td><td>63.3</td><td>92.2</td><td>82.3</td><td>90.8</td></tr><tr><td>Bi[[LoRA]] [45]</td><td>0.3M</td><td>95.1</td><td>91.7</td><td>64.8</td><td>93.3</td><td>87.2</td><td>91.7</td></tr></table>

Learning, STAR [50] can effectively improve the data efficiency.

At last, to illustrate the performance difference between [[LoRA]] and some of its variants, we report their performance for RoBERTa-base [211] model on the GLUE benchmark [212] in Table 1. These results are derived from previous studies [9, 16, 32, 45, 90].

# 4 Cross-task Generalization

[[LoRA]]’s pluggable nature enables users to accumulate [[LoRA]] plugins for different tasks. For example, on Hugging Face platform, there are more than 20,000 [[LoRA]] plugins compatible with various [[LLMs]] for different tasks. These accumulated [[LoRA]] plugins can not only be utilized independently but also be mixed to achieve cross-task generalization [60]. Mixing multiple [[LoRA]] plugins together, namely [[LoRA]] mixture, has been widely applied in areas requiring cross-task generalization, such as multi-task learning, domain adaptation, and continual learning. Existing [[LoRA]] mixture methods can be categorized into (1) mixture with manually designed weights; (2) mixture with

learnt weights; (3) mixture of [[LoRA]] experts. This section introduces each category of methods respectively, as shown in Fig. 3.

# 4.1 Mixture with Manually Designed Weights

Early [[LoRA]] mixture methods attempt to linearly combine different [[LoRA]] modules with manually designed weights. Some research demonstrates that we can achieve proper cross-task generalization ability by simply averaging [[LoRA]] modules or their related outputs [51–53]. Furthermore, several methods have been proposed to further improve the performance of the [[LoRA]] mixture via adopting manually designed weights. For example, ControlPE [54], [55] and [56] set the weight factors as hyperparameters, and ControlPE uses hyperparameter search to determine the optimal combination of two [[LoRA]] modules. Additionally, Tokenlevel Adaptation [57] utilizes cosine similarity between the input feature and the adapter dataset center as weight factors, while BYOM [58] applies basic model fusion methods such as Task Arithmetic, Fisher-Merging, and RegMean.

Mixture with manually designed weights can quickly mix multiple [[LoRA]]s without extra train-

![](images/684127c1697345a99f027827cdecd596887038a6327b27340b0dccf3bceca110.jpg)  
(a) Mixture with Manually Designed Weights

![](images/60a16c7095deaf71efdca7b2914819a4a330f0fefff29fb0ab208313d5271b05.jpg)  
(b) Mixture with Learnt Weights

![](images/a8a5c05ecf82cb0de25519ae9c3c4eb7d2d00aa42add8d4e59222b6633f3abb8.jpg)  
(c) Mixture of [[LoRA]] Experts   
Fig. 3 An illustration of [[LoRA]] mixture methods.

ing, which demonstrates simplicity and computational efficiency. However, it often fails to find the optimal weights, leading to unstable performance and limited generalization. Subsequently, researchers have explored using learning-based methods to achieve more precise and adaptive mixtures.

# 4.2 Mixture with Learnt Weights

To learn the optimal mixture weights, several methods have been proposed at task level, instance level and token level to meet different needs. Task-level methods focus on enhancing task transferability, which can be either gradient-based, such as [59], or gradient-free, as seen in [[LoRA]]Hub [60]. Lo-RAHub employs a black-box algorithm named CMA-ES [214] to optimize weight factors for [[LoRA]] modules, simplifying the training process. Later, ComPEFT [61] and L-[[LoRA]] [62] use Lo-RAHub to mix quantized [[LoRA]] modules, further improving computational efficiency.

Compared to task-level methods, instance-level and token-level methods can provide flexibility and precision for complex inputs. For multimodal instruction tuning, Mix[[LoRA]] [63] dynamically

chooses appropriate low-rank decomposition vectors based on the input instance, which are then integrated into [[LoRA]] matrices for training. To conduct protein mechanics analysis and design tasks, X-[[LoRA]] [64] develops a dynamic gating mechanism to assign weights for [[LoRA]] modules at the token level and layer granularity. These approaches demonstrate better performance in specific tasks or application scenarios.

# 4.3 Mixture of [[LoRA]] Experts

When the [[LoRA]] modules are trainable, we can jointly learn the mixture weights and the [[LoRA]] modules, which can further improve the performance of the [[LoRA]] mixture. To jointly learn the mixture weights and [[LoRA]] modules, Mixture of [[LoRA]] Experts ([[LoRA]] MoE) is a natural choice, where each [[LoRA]] module acts as an expert, while a router network typically assigns the mixture weights. [[LoRA]] MoE has been proven to be effective in many tasks, such as continual learning [65, 66], vision-language tasks [67] and multitask medical applications [68].

Existing methods improve the performance of [[LoRA]] MoE from the perspectives of initialization,

task relationship management and efficiency. For initialization, Mixture-of-[[LoRA]]s [69] first trains multiple [[LoRA]]s separately as initialization and then optimizes the router and [[LoRA]]s jointly. Multi[[LoRA]] [70] proposes refining the initialization to reduce parameter dependency, which can yield more balanced unitary subspaces. As for task balance, MLoRE [71] adds a low-rank convolution path in the MoE structure to capture global task relationships. MT[[LoRA]] [72] adopts both taskagnostic and task-specific [[LoRA]] modules to address task conflicts. For efficiency, MoLA [73] adaptively allocates different numbers of [[LoRA]] experts to different layers of the Transformer model to save the number of [[LoRA]] modules. LLaVA-MoLE [74] and SiRA [75] leverage sparse computation to reduce computational cost. Additionally, Octavius [76] sparsely activates independent [[LoRA]] experts with instance-level instructions to mitigate task interference and improve efficiency. Fast [[LoRA]] [77] allows each sample in a minibatch to have its unique low-rank adapters, enabling efficient batching.

Besides, some methods are not explicitly based on MoE but follow MoE ideas. For example, I-[[LoRA]] [202] uses two [[LoRA]]s to manage long-term and short-term memory for continual learning, respectively.

# 5 Efficiency Improving

With the popularization of [[LLMs]], the demand for training and running [[LoRA]] modules increases rapidly. This increasing demand brings an unignorable computational burden; thus, for [[LoRA]], the smaller, the faster, the better. To meet this demand, existing methods improve the computational efficiency of [[LoRA]] from the perspectives of (1) pa-

rameter reduction; (2) parameter quantization; (3) parallel [[LoRA]] computing frameworks. This section introduces each category of methods, as illustrated in Fig. 4.

# 5.1 Parameter Reduction

[[LoRA]] significantly reduces the number of tunable parameters for fine-tuning [[LLMs]]. However, it still requires expensive activation memory to update low-rank matrices. To further reduce the memory cost, existing methods reduce the number of tunable parameters of [[LoRA]] via parameter freezing, parameter pruning, and parameter sharing.

# 5.1.1 Parameter Freezing

Parameter freezing methods reduce the number of tunable parameters for [[LoRA]] via freezing some of its parameters. They can be divided into two categories: intra-parameter methods and extraparameter methods.

The intra-parameter methods tune a subset of parameters of [[LoRA]] while freezing the others. [[LoRA]]-SP [79] randomly selects half of the [[LoRA]] parameters to freeze during fine-tuning. [[LoRA]]-FA [80]freezes the down-projection weights and updates the up-projection weights in each layer of [[LoRA]]. AF[[LoRA]] [81] constructs a low-rank trainable path and gradually freezes parameters during training [[LoRA]]. Additionally, DropBP [82] accelerates the training process by randomly dropping some [[LoRA]] gradient calculations during backpropagation.

By contrast, the extra-parameter methods introduce and tune a set of extra parameters while freezing the original parameters of [[LoRA]]. Most of them are proposed based on Singular Value Decomposition(SVD). [[LoRA]]-XS [83] adds a small

![](images/c40b7d9a615f2bb5b8ded21669093cbbe0e9adc4e9ed1c26a9693ed5437220b8.jpg)  
Fig. 4 An illustration of efficiency improving methods.

r × r weight matrix between frozen [[LoRA]] matrices, which are constructed using the SVD of the original weight matrix; then it tunes only the r × r weight matrices in fine-tuning. Similarly, BYOM-[[LoRA]] [58] adopts SVD to compress [[LoRA]] matrices for multi-task models.

# 5.1.2 Parameter Pruning

Parameter pruning methods aim to remove unimportant [[LoRA]] parameters during training and inference. They prune parameters by either pruning [[LoRA]] independently or jointly pruning [[LoRA]] and the LLM. [[LoRA]]-drop [84] uses the output of [[LoRA]] at each layer to evaluate the importance of parameters and prune the unimportant parameters. By contrast, [[LoRA]]Prune [85] jointly pruning [[LoRA]] matrices and the LLM parameters based on [[LoRA]]’s gradients. Besides, we can also use [[LoRA]] to support parameters pruning for [[LLMs]] [86, 87].

# 5.1.3 Parameter Sharing

Parameter-sharing methods reduce the number of parameters by sharing parameters across different layers or modules of [[LLMs]]. VeRA [88] and VB-[[LoRA]] [89] are two representative parametersharing methods for [[LoRA]]. Specifically, VeRA proposes to share a pair of frozen random matri-

ces across all layers and conduct layer-wise adaptation with “scaling vectors”. By contrast, VB-[[LoRA]] proposes a “divide-and-share” paradigm, which divides [[LoRA]]’s low-rank decomposition by a rankone decomposition and achieves global sharing based on an admixture model. Instead of sharing parameters in the original parameter space, FourierFT [90] converts the incremental matrix ∆W into the spatial domain using Fourier transform. It shares spectral entries across all layers and only learns its sparse spectral coefficients for each layer, thus reducing the number of trainable parameters.

# 5.2 Parameter Quantization

Quantization, which reduces the bit width of parameters (e.g., from 32-bit floats to 4-bit integers), can be used to reduce the memory and computational cost of [[LoRA]]. Existing quantization-aware [[LoRA]] methods consist of post-training quantization (PTQ)-based methods and quantization-aware training (QAT)-based methods [95].

# 5.2.1 PTQ-based methods

In PTQ-based methods, we first quantize an LLM and then fine-tune the quantized model, namely quantization and fine-tuning are sequentially conducted. Q[[LoRA]] [91] is the first PTQ-based

quantization-aware [[LoRA]] method. In the finetuning stage, it first quantizes an LLM to 4 bits and then fine-tunes a [[LoRA]] module on it with a higher precision, such as BFloat16 or Float16. In the inference stage, it dequantizes the LLM to the same precision as [[LoRA]] and then adds the [[LoRA]] updates to the LLM.

Although Q[[LoRA]] can significantly reduce memory cost for fine-tuning, it does not bring benefits for inference, because it requires dequantizing the LLM to high precision again. To solve this problem, QA-[[LoRA]] [92] is proposed to reduce memory cost for both the fine-tuning and inference stages. QA-[[LoRA]] uses group-wise operators to balance the degrees of freedom of the LLM quantization and fine-tuning, which enables it to obtain a [[LoRA]] module having identical precision with the quantized LLM. Thus, it can perform inference without dequantization.

# 5.2.2 QAT-based methods

In QAT-based methods, we jointly quantize and fine-tune an LLM, namely quantization and finetuning are simultaneously conducted. These methods can alleviate the quantization discrepancies observed in PTQ-based methods. To address the quantization discrepancy of Q[[LoRA]], LoftQ [93] alternatively applies quantization and low-rank approximation during fine-tuning to minimize the quantization error. However, ApiQ [94] points out that LoftQ ignores the error propagation across layers and proposes activation-preserved initialization to avoid error propagation. Besides, L4Q [95] is another QAT-based method that has an advanced layer design.

# 5.3 Parallel [[LoRA]] Computing Frameworks

[[LoRA]]’s parameter-efficient nature enables us to fine-tune or infer multiple modules on a single GPU or a GPU cluster, which can save computational resources and improve the efficiency of [[LoRA]]. This section introduces the parallel finetuning and parallel inference frameworks, respectively.

# 5.3.1 Parallel Fine-tuning

Parallelly fine-tuning multiple [[LoRA]] modules on a single GPU can reduce GPU memory usage and improve computation efficiency. ASPEN [96] proposes a high-throughput parallel finetuning framework for [[LoRA]], which consists of a BatchFusion approach and an adaptive job scheduling algorithm. Specifically, the BatchFusion approach supports parallelly fine-tuning multiple [[LoRA]] modules on a shared LLM by fusing multiple input batches into a single batch, while the adaptive job scheduling algorithm allocates computation resources to the fine-tuning jobs.

# 5.3.2 Parallel Inference

Parallel inference framework for [[LoRA]] can not only improve the computational efficiency but also support the needs of multi-tenant service. Punica [97] uses a new CUDA kernel design to batch GPU operations for different [[LoRA]] modules. Based on Punica, S-[[LoRA]] [98] further optimizes the parallel inference framework by introducing a unified paging mechanism and a new tensor parallelism strategy, which enables the service of thousands of concurrent [[LoRA]] modules. Then, based on Punica and S-[[LoRA]], CARASERVE [99] reduces the cold-start overhead and further improves the service efficiency and SLO (service-level ob-

jective) attainment rates by CPU-GPU cooperation and rank-aware scheduling.

# 6 [[LoRA]] for Federated Learning

When adapting [[LLMs]] to vertical domains such as medicine and finance, the available training data can be privately owned by multiple clients. In this scenario, the training data is not centralized, and we have to fine-tune [[LLMs]] while keeping the data localized, namely federated learning. In federated learning, the clients typically compute weight updates locally and then share these updates with others to globally update the LLM. It brings both communication and computation costs for the clients. Fortunately, [[LoRA]] is parameter efficient and pluggable, which can reduce communication costs and lower computational resource requirements. [[LoRA]] can enhance the overall efficiency and scalability of federated learning.

However, adopting [[LoRA]] in federated learning is not trivial for federated learning faces challenges such as data heterogeneity, device heterogeneity, and model heterogeneity. To address these issues, recent studies have designed various methods for [[LoRA]] to meet the diverse needs of federated learning, as shown in Fig. 5. Additionally, as a localized parameter component, [[LoRA]]’s pluggable nature allows it to support parameter privacy protection in federated learning.

# 6.1 Data Heterogeneity

Data heterogeneity refers to differences in data distribution across clients. In federated learning, different clients usually have different data distributions. The inconsistency in data distribution affects the overall performance of the model. Research

reveals that in federated learning, as user data becomes more diverse, the performance gap between [[LoRA]] and full fine-tuning widens [100]. To address this issue, researchers have proposed several improvement methods.

S[[LoRA]] [100] introduces a data-driven initialization method for [[LoRA]]. It first performs sparse federated fine-tuning before applying [[LoRA]] and then performs SVD to decompose the accumulated gradient updates into low-rank matrices for [[LoRA]] initialization. The goal is to enable the [[LoRA]] modules to better adapt to the data distribution of each client, thereby integrating these heterogeneous data characteristics into the global model more effectively. FeDeRA [101] uses a simpler initialization method. It directly applies SVD to pre-trained weights to initialize [[LoRA]]. Retaining the principal components of the pre-trained weights aligns the direction and magnitude of weight updates across different clients to handle data heterogeneity. Additionally, FFA-[[LoRA]] [102] freezes one low-rank matrix and fine-tunes only the other. This reduces inconsistency during server aggregation of [[LoRA]] gradients, alleviating the optimization instability caused by non-IID data.

# 6.2 Device Heterogeneity

Device heterogeneity refers to the differences in hardware capabilities, and network connectivity among clients participating in federated learning. Traditional federated learning methods often encounter the “buckets effect”, implying that the system’s overall performance is limited by the capability of the least powerful client. Specifically, these methods use the smallest [[LoRA]] rank to accommodate all clients, which prevents many resource-rich clients from fully utilizing their potential.

![](images/6eb1183ef30865fd1fe62daa6f18cc1de6469d1094576d732bb4b14353d59cc5.jpg)  
Fig. 5 An illustration of [[LoRA]] for federated learning.

To address this issue, a dynamic parameter allocation strategy can be adopted. FedMS [103] dynamically adjusts the number of activated [[LoRA]] matrices based on the real-time computational resources of clients. Flex[[LoRA]] [104] uses a dynamic parameter allocation strategy. It adjusts the [[LoRA]] rank and redistributes the SVD components of the global [[LoRA]] weights based on resource constraints. Similarly, HET[[LoRA]] [105] assigns different ranks for different clients. However, it performs weighted aggregation according to the sparsity of the updates from different clients, balancing update information better than simple aggregation.

# 6.3 Model Heterogeneity

Model heterogeneity indicates differences in model structures among clients. In traditional federated learning, clients use local models with the same architecture, allowing their parameters to be aggregated into a global model on the server. However, in practice, clients may prefer unique local model architectures due to personal needs and often do not want to disclose model details. Thus, it is necessary to transfer knowledge between heterogeneous models without sharing private data or revealing local model structures [215].

Previous work has used knowledge distillation, model ensembling, and mutual learning to ad-

dress model heterogeneity. However, these methods have limitations, such as reliance on public datasets, additional communication costs and poor local model performance. To avoid these limitations, pFed[[LoRA]] [106] uses [[LoRA]] as a carrier of both global and local knowledge. It adopts an iterative training strategy to facilitate knowledge transfer and integration, enabling knowledge sharing among heterogeneous models across different clients.

# 6.4 Parameter Privacy

In federated learning, protecting client-specific parameters is crucial because ensuring the privacy of these parameters also indirectly safeguards client data privacy. As a modular approach to adjusting personalized parameters, [[LoRA]] can be effectively integrated into federated learning systems to achieve parameter privacy protection.

Literature [107] proposes a secure distributed language model training framework based on model slicing. They deploy [[LoRA]] in a Trusted Execution Environment (TEE) and use OTP encryption to transmit features between the GPU and TEE, protecting model parameter privacy. Private[[LoRA]] [108] introduces a distributed system based on [[LoRA]]. It adds a square matrix M between low-rank matrices A and B. The non-trainable ma-

trices A and B, along with most of the pre-trained weights, are deployed on the global server to enhance computation. Meanwhile, the trainable matrix M is stored on the client as personalized parameters, thus ensuring parameter privacy protection.

Furthermore, recent works have integrated differential privacy (DP) techniques with [[LoRA]] in federated learning to enhance data privacy. DP-[[LoRA]] [216] ensures differential privacy by adding Gaussian noise to [[LoRA]]’s weight updates during the update process. This approach maintains privacy and improves communication efficiency. To solve the noise amplification when applying differential privacy in [[LoRA]], FFA-[[LoRA]] [102] fixes the matrix A, avoiding the local semi-quadratic structure and enhancing robustness and performance.

# 7 Applications of [[LoRA]]

In the rapidly evolving field of deep learning, [[LoRA]] has become widely used due to its unique advantages. Researchers utilize [[LoRA]] to finetune pre-trained models for various downstream tasks, reducing computational resource requirements while enhancing performance. [[LoRA]]’s strong adaptability and efficiency have significantly improved various applications. In this section, we will introduce [[LoRA]]’s applications in the following scenarios: (1) language tasks; (2) vision tasks; (3) multimodal tasks.

# 7.1 Language Tasks

Recently, the rapid development of pre-trained language models, especially [[LLMs]], is revolutionizing the approach to language tasks due to their outstanding performance. However, these pre-trained models are trained on a large amount of general

data and still require further fine-tuning on taskspecific data to adapt to downstream tasks. Therefore, it is natural to use [[LoRA]] to fine-tune these pre-trained language models, as it reduces computational resource requirements. We mainly focus on some representative downstream tasks, which include traditional NLP tasks, code tasks, model alignment and vertical domain tasks.

# 7.1.1 Traditional NLP Tasks

Given the strong instruction-following and contextual understanding abilities of [[LLMs]], some researches apply [[LoRA]] to fine-tune these models for traditional NLP tasks. For example, [[LoRA]] is widely adopted in LLaMA for various tasks, such as emotion recognition [109], text classification [110] and role recognition [111]. AutoRE [112] applies Q[[LoRA]] to three document-level relation extraction tasks, achieving great performance on different [[LLMs]]. Some studies [113–115] leverage [[LoRA]] from different perspectives to enhance the model’s capability in machine translation tasks. Additionally, [[LoRA]] can also improve the performance of models like BERT and T5 for text understanding tasks [116, 117].

# 7.1.2 Code Tasks

Some researchs apply [[LoRA]] to improve model performance in various code-related tasks. For example, BERT-style models fine-tuned with [[LoRA]] are suitable for code-change-related tasks, specifically in Just-In-Time defect prediction (JIT-DP) [118, 119]. Similarly, training CodeT5 and PLBART with [[LoRA]] can enhance their adaptability for code summarization and code clone detection [120]. As for the decoder-only model, RepairLLaMA [121] uses [[LoRA]] to fine-tune Llama for automated program repair (APR), while WizardCoder-15B is

fine-tuned with [[LoRA]] for Text-to-SQL task [122]. Additionally, SteloCoder [123], a fine-tuned version of StarCoder, is designed for multi-language to Python code translation.

# 7.1.3 Model Alignment Tasks

Model alignment tasks focus on adjusting a machine learning model to align with human values and intentions, often using techniques like Reinforcement Learning from Human Feedback (RLHF). To reduce memory requirements of RLHF, some studies use [[LoRA]] to fine-tune the reward model and policy model [124–126]. Furthermore, other works improve reward models by integrating multiple [[LoRA]] adapters. For example, DMoERM [127] combines MoE with [[LoRA]], routing model inputs to multiple [[LoRA]] experts while another work [128] proposes a [[LoRA]]-based ensemble method as well. The integration can also benefit the quantification of uncertainty in reward models [129]. Besides, literature [130] applies Laplace-[[LoRA]] [131] to train Bayesian reward models, which mitigates reward overoptimization in best-of-n sampling.

# 7.1.4 Vertical Domain Tasks

[[LLMs]] often perform suboptimally in vertical domains, requiring fine-tuning with domain-specific expertise. Some works apply [[LoRA]] to improve the performance of [[LLMs]] on domain-specific tasks. For example, some studies fine-tune [[LLMs]] on medical datasets with [[LoRA]] to adapt them to the medical domain [132–134]. Additionally, other studies improve medical tasks like clinical dialogue summarization [135], assertion detection [136] and medical QA tasks [137, 138]. Similarly, several studies fine-tune [[LLMs]] with [[LoRA]] on financial data to solve tasks such as financial news analytics

and sentiment classification [139–142]. Besides, [[LoRA]] can also be used to enhance the performance in database tasks like query rewrite and index tuning [143].

# 7.2 Vision Tasks

In vision tasks, [[LoRA]] is primarily applied to image generation and image segmentation, significantly improving training efficiency and optimizing model performance.

# 7.2.1 Image Generation

Image generation tasks hold significant importance in the field of computer vision. In recent years, diffusion model have demonstrated exceptional performance in image generation tasks. [[LoRA]] is widely used in diffusion models to address various image generation tasks while reducing computational resources. Some works use [[LoRA]] to fine-tune diffusion models for image style transfer [144–148], while others apply it to text-to-image generation [149–153].

Furthermore, researchers have designed several [[LoRA]]-based methods to improve image generation quality. For instance, Smooth Diffusion [154] uses [[LoRA]] to achieve smoothness in the latent space, leading to better performance in various image generation and editing tasks. ResAdapter [155] employs [[LoRA]] to learn resolution priors, adjusting the receptive fields of convolutional layers to dynamical resolution. Additionally, to specifically enhance text-to-image quality, STAMINA [156] uses [[LoRA]] to fine-tune diffusion models for longer concept sequences. Dream-Sync [157] and StyleAdapter [158] use [[LoRA]] to improve text fidelity and image quality. Mixof-Show [159] captures out-of-domain informa-

tion with [[LoRA]] weights to combine multiple customized concepts with high fidelity, reducing concept conflicts. Other studies combine [[LoRA]] with model distillation to accelerate image generation [160, 161]. Moreover, [[LoRA]] can also be applied to video generation [162–167] and 3D generation tasks [168–172].

# 7.2.2 Image Segmentation

Image segmentation is a significant challenge in computer vision, aiming to divide an image into multiple meaningful regions or objects. To address this, SAM has been proposed as a foundational model for image segmentation and demonstrated superior generalization ability. To further enhance its performance in specific vertical domains, many studies utilize [[LoRA]] to fine-tune it. For instance, in license plate detection, SamLP [173] utilizes [[LoRA]] to adapt SAM for efficient segmentation of license plates. In structural damage detection, literature [174] fine-tunes SAM’s encoder using [[LoRA]] for instance segmentation task. In the medical domain, many studies also apply [[LoRA]] to fine-tune SAM for a variety of tasks, including nuclei segmentation [175], OCTA image segmentation [176], brain tumor segmentation [177], organ segmentation [178], and surgical instrument segmentation [179]. Additionally, some studies use [[LoRA]] to fine-tune Vision Transformer (ViT) for visual tracking [180] and face forgery detection [181].

# 7.3 Multimodal Tasks

Multimodal [[Large Language Models]] (M[[LLMs]]) aim to integrate text with various modalities such as audio, image and video, which enable crossmodal understanding and reasoning through a unified embedding space. The success of [[LoRA]] in

both NLP and vision tasks has sparked considerable interest in applying them to M[[LLMs]].

In M[[LLMs]], [[LoRA]] can not only improve training efficiency but also facilitate effective modality alignment. In audio-text tasks, SALM [182] comprises [[LoRA]] layers, a frozen text-based LLM, an audio encoder and a modality adapter to handle speech inputs and corresponding task instructions. For image-text tasks, InternLM-XComposer2 [183] achieves modality alignment by applying [[LoRA]] to image tokens, mPLUG-Owl [184] freezes the visual module while jointly finetuning [[LoRA]] and abstractor of the text module, and CoLLaVO [185] employs Q[[LoRA]] to preserve object-level image understanding. In the realm of video-text tasks, VSP-LLM [186] fine-tunes the text module with Q[[LoRA]] for visual speech processing, MolCA [187] uses [[LoRA]] to understand 2D molecular graphs and text, while TPLLM [188] employs [[LoRA]] for efficient traffic prediction by integrating sequence and spatial features. These applications demonstrate the versatility and power of [[LoRA]] in M[[LLMs]] tasks.

# 8 Conclusion and Future Direction

In this survey, the recent progress of [[LoRA]] have been systematically reviewed from the perspective of downstream adaptation improving, crosstask generalization, efficiency improving, federated learning and applications. From this review, we can find that [[LoRA]] is parameter efficient, pluggable, compatible and easy to achieve cross-task generalization, which enables it to be one of the most important technology for [[LLMs]] applications. Recent progress further boosts the generalization and efficiency of [[LoRA]], and stimulate its potential to be used in more scenarios. Here, we list three future directions where [[LoRA]] will be indispensable.

# 8.1 [[LoRA]] for GaaS

In Generative-as-a-Service (GaaS), cloud-based platforms provide users with generative artificial intelligence (AGI) services. GaaS enables users enjoy AGI without deploying local computational resources. For the users’ needs are diverse, it is necessary to provides various functions for GaaS. To implement the various functions, we can construct a [[LoRA]] module for each function. The pramameter efficiency and plugability of [[LoRA]] can facilitate efficient functions’ construction and execution. Besides, the services on GaaS platforms can change rapidly alonging time. To follow the changes, we can train new [[LoRA]] modules that initialized by combination of previous [[LoRA]] modules. The cross-task generalization ability of [[LoRA]] can facilitate fast adaption to service updations.

# 8.2 [[LoRA]] for Continued Pre-training

In continued pre-training, a foundation model is continuely trained with unlabeled user data to adapt the model to specific domains. Typically, the selfsupervised training objective is same with that for pre-training, and the learning rate is much smaller than than for pre-training. Continued pre-training is a important stage for constructing vertical domain [[LLMs]]. However, it is highly computational expensive, which impedes the development of vertical domain [[LLMs]], especailly for the organizations with limited computational resources. Enhancing [[LoRA]] for continued pre-training and reducing its computational cost is worth to explored.

# 8.3 [[LoRA]] for Autonomous Agents

In LLM-based autonomous agents, the agents are assigned with specific roles. Based the roles and environment, agents make actions to response

users’ or other agents’ request. The actions can be made based on self-knowledge or tools that designed for domain-specific tasks. The request and the actions are stored in memory to support the future requests.

In the current agents, the roles are typically assigned by prompts; however, prompt may cannot give a comprehensive discription of the role when the role is complex and the number of related data is large. Assiging roles with [[LoRA]] modules training from data related to the roles can be a better choice. Furthermore, the tools for agent can be [[LoRA]] modules. Besides, the memory usually augments the agents with retrieval augmented generation (RAG); however, due to the input token limitation and the short-comings of in-context learning, the RAG-based support may be less effective. By contrast, we can use [[LoRA]]-based continual learning to construct memory modules, which can solve the problem of RAG. Therefore, [[LoRA]]driven agents are worth to explore.

Acknowledgements This work was supported in part by the NSFC under Grants No. (62025206, 62302436, U23A20296), Zhejiang Province’s ”Lingyan” R&D Project under Grant No. 2024C01259, and Ningbo Science and Technology Special Projects under Grant No. 2023Z212. Yunjun Gao is the corresponding author of this work.

# References

1. Devlin J, Chang M, Lee K, Toutanova K. BERT: pre-training of deep bidirectional transformers for language understanding. In: Proceedings of North American Chapter of the Association for Computational Linguistics: Human Language Technologies, NAACL-HLT. 2019, 4171–4186   
2. Chowdhery A, Narang S, Devlin J, Bosma M, Mishra G, Roberts A, Barham P, Chung H W, Sutton C, Gehrmann S, Schuh P, Shi K, Tsvyashchenko S, Maynez J, Rao A, Barnes P, Tay Y, Shazeer N, Prabhakaran V, Reif E, Du N, Hutchinson B, Pope R, Bradbury J, Austin J, Isard M, Gur-Ari G, Yin P, Duke T, Levskaya A, Ghemawat S, Dev S, Michalewski H,

Garcia X, Misra V, Robinson K, Fedus L, Zhou D, Ippolito D, Luan D, Lim H, Zoph B, Spiridonov A, Sepassi R, Dohan D, Agrawal S, Omernick M, Dai A M, Pillai T S, Pellat M, Lewkowycz A, Moreira E, Child R, Polozov O, Lee K, Zhou Z, Wang X, Saeta B, Diaz M, Firat O, Catasta M, Wei J, Meier-Hellstern K, Eck D, Dean J, Petrov S, Fiedel N. Palm: Scaling language modeling with pathways. J. Mach. Learn. Res., 2023, 24: 240:1–240:113   
3. Chen Y, Qian S, Tang H, Lai X, Liu Z, Han S, Jia J. Long[[LoRA]]: Efficient fine-tuning of long-context [[Large Language Models]]. arXiv preprint arXiv.2309.12307, 2023   
4. Pan R, Liu X, Diao S, Pi R, Zhang J, Han C, Zhang T. LISA: layerwise importance sampling for memoryefficient large language model fine-tuning. arXiv preprint arXiv.2403.17919, 2024   
5. Ding N, Qin Y, Yang G, Wei F, Yang Z, Su Y, Hu S, Chen Y, Chan C, Chen W, Yi J, Zhao W, Wang X, Liu Z, Zheng H, Chen J, Liu Y, Tang J, Li J, Sun M. Parameter-efficient fine-tuning of large-scale pretrained language models. Nat. Mac. Intell., 2023, 5(3): 220–235   
6. Houlsby N, Giurgiu A, Jastrzebski S, Morrone B, Laroussilhe d Q, Gesmundo A, Attariyan M, Gelly S. Parameter-efficient transfer learning for NLP. In: Proceedings of the 36th International Conference on Machine Learning. 2019, 2790–2799   
7. Lester B, Al-Rfou R, Constant N. The power of scale for parameter-efficient prompt tuning. In: Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing. 2021, 3045–3059   
8. Zaken E B, Goldberg Y, Ravfogel S. Bitfit: Simple parameter-efficient fine-tuning for transformer-based masked language-models. In: Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers). 2022, 1–9   
9. Hu E J, Shen Y, Wallis P, Allen-Zhu Z, Li Y, Wang S, Wang L, Chen W. [[LoRA]]: [[Low-Rank Adaptation]] of [[Large Language Models]]. In: The Tenth International Conference on Learning Representations. 2022   
10. Zhao W X, Zhou K, Li J, Tang T, Wang X, Hou Y, Min Y, Zhang B, Zhang J, Dong Z, others . A survey of [[Large Language Models]]. arXiv preprint arXiv:2303.18223, 2023   
11. Han Z, Gao C, Liu J, Zhang S Q, others . Parameterefficient fine-tuning for large models: A comprehensive survey. arXiv preprint arXiv:2403.14608, 2024   
12. Malladi S, Wettig A, Yu D, Chen D, Arora S. A kernelbased view of language model fine-tuning. In: International Conference on Machine Learning. 2023,

23610–23641   
13. Koubbi H, Boussard M, Hernandez L. The impact of [[LoRA]] on the emergence of clusters in transformers. arXiv preprint arXiv.2402.15415, 2024   
14. Jang U, Lee J D, Ryu E K. [[LoRA]] training in the NTK regime has no spurious local minima. arXiv preprint arXiv.2402.11867, 2024   
15. Zhu J, Greenewald K H, Nadjahi K, Ocariz Borde´ d H S, Gabrielsson R B, Choshen L, Ghassemi M, Yurochkin M, Solomon J. Asymmetry in lowrank adapters of foundation models. arXiv preprint arXiv.2402.16842, 2024   
16. Zeng Y, Lee K. The expressive power of [[Low-Rank Adaptation]]. arXiv preprint arXiv.2310.17513, 2023   
17. Lialin V, Muckatira S, Shivagunde N, Rumshisky A. Re[[LoRA]]: High-rank training through low-rank updates. In: The Twelfth International Conference on Learning Representations. 2023   
18. Jiang T, Huang S, Luo S, Zhang Z, Huang H, Wei F, Deng W, Sun F, Zhang Q, Wang D, others . Mora: High-rank updating for parameter-efficient fine-tuning. arXiv preprint arXiv:2405.12130, 2024   
19. Huh M, Cheung B, Bernstein J, Isola P, Agrawal P. Training neural networks from scratch with parallel low-rank adapters. arXiv preprint arXiv.2402.16828, 2024   
20. Liang Y, Li W. Inf[[LoRA]]: Interference-free [[Low-Rank Adaptation]] for continual learning. arXiv preprint arXiv.2404.00228, 2024   
21. Zhao H, Ni B, Wang H, Fan J, Zhu F, Wang Y, Chen Y, Meng G, Zhang Z. Continual forgetting for pre-trained vision models. arXiv preprint arXiv.2403.11530, 2024   
22. Ren W, Li X, Wang L, Zhao T, Qin W. Analyzing and reducing catastrophic forgetting in parameter efficient tuning. arXiv preprint arXiv:2402.18865, 2024   
23. Zhang H. Sink[[LoRA]]: Enhanced efficiency and chat capabilities for long-context [[Large Language Models]]. arXiv preprint arXiv.2406.05678, 2023   
24. Xia W, Qin C, Hazan E. Chain of [[LoRA]]: Efficient finetuning of language models via residual learning. arXiv preprint arXiv.2401.04151, 2024   
25. Ren P, Shi C, Wu S, Zhang M, Ren Z, Rijke d M, Chen Z, Pei J. Mini-ensemble low-rank adapters for parameter-efficient fine-tuning. arXiv preprint arXiv.2402.17263, 2024   
26. Hao Y, Cao Y, Mou L. F[[LoRA]]: Low-rank adapters are secretly gradient compressors. arXiv preprint arXiv.2402.03293, 2024   
27. Zi B, Qi X, Wang L, Wang J, Wong K, Zhang L. Delta-[[LoRA]]: Fine-tuning high-rank parameters with the delta of low-rank matrices. arXiv preprint

arXiv.2309.02411, 2023   
28. Zhang Q, Chen M, Bukharin A, He P, Cheng Y, Chen W, Zhao T. Adaptive budget allocation for parameterefficient fine-tuning. In: The Eleventh International Conference on Learning Representations. 2023   
29. Hu Y, Xie Y, Wang T, Chen M, Pan Z. Structureaware [[Low-Rank Adaptation]] for parameter-efficient fine-tuning. Mathematics, 2023, 11(20): 4317   
30. Zhang F, Li L, Chen J, Jiang Z, Wang B, Qian Y. Incre[[LoRA]]: Incremental parameter allocation method for parameter-efficient fine-tuning. arXiv preprint arXiv.2308.12043, 2023   
31. Mao Y, Huang K, Guan C, Bao G, Mo F, Xu J. Dora: Enhancing parameter-efficient finetuning with dynamic rank distribution. arXiv preprint arXiv:2405.17357, 2024   
32. Zhang R, Qiang R, Somayajula S A, Xie P. Auto[[LoRA]]: Automatically tuning matrix ranks in [[Low-Rank Adaptation]] based on meta learning. arXiv preprint arXiv.2403.09113, 2024   
33. Ding N, Lv X, Wang Q, Chen Y, Zhou B, Liu Z, Sun M. Sparse [[Low-Rank Adaptation]] of pre-trained language models. In: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing. 2023, 4133–4145   
34. Liu Z, Lyn J, Zhu W, Tian X, Graham Y. A[[LoRA]]: Allocating [[Low-Rank Adaptation]] for fine-tuning [[Large Language Models]]. arXiv preprint arXiv.2403.16187, 2024   
35. Valipour M, Rezagholizadeh M, Kobyzev I, Ghodsi A. Dy[[LoRA]]: Parameter efficient tuning of pre-trained models using dynamic search-free [[Low-Rank Adaptation]]. arXiv preprint arXiv:2210.07558, 2022   
36. Hayou S, Ghosh N, Yu B. The impact of initialization on [[LoRA]] finetuning dynamics. arXiv preprint arXiv:2406.08447, 2024   
37. Meng F, Wang Z, Zhang M. Pissa: Principal singular values and singular vectors adaptation of [[Large Language Models]]. arXiv preprint arXiv:2404.02948, 2024   
38. Wang H, Xiao Z, Li Y, Wang S, Chen G, Chen Y. Mi[[LoRA]]: Harnessing minor singular components for parameter-efficient llm finetuning. arXiv preprint arXiv:2406.09044, 2024   
39. Zhang F, Pilanci M. Riemannian preconditioned [[LoRA]] for fine-tuning foundation models. arXiv preprint arXiv:2402.02347, 2024   
40. Hayou S, Ghosh N, Yu B. [[LoRA]]+: Efficient low rank adaptation of large models. arXiv preprint arXiv:2402.12354, 2024   
41. Shi S, Huang S, Song M, Li Z, Zhang Z, Huang H, Wei F, Deng W, Sun F, Zhang Q. Res[[LoRA]]: Identity residual mapping in low-rank adaption. arXiv preprint

arXiv:2402.18039, 2024   
42. Wen Z, Zhang J, Fang Y. Sibo: A simple booster for parameter-efficient fine-tuning. arXiv preprint arXiv:2402.11896, 2024   
43. Jin F, Liu Y, Tan Y. Derivative-free optimization for [[Low-Rank Adaptation]] in [[Large Language Models]]. arXiv preprint arXiv:2403.01754, 2024   
44. Liu S Y, Wang C Y, Yin H, Molchanov P, Wang Y C F, Cheng K T, Chen M H. Dora: Weightdecomposed [[Low-Rank Adaptation]]. arXiv preprint arXiv:2402.09353, 2024   
45. Qiang R, Zhang R, Xie P. Bi[[LoRA]]: A bi-level optimization framework for overfitting-resilient [[Low-Rank Adaptation]] of large pre-trained models. arXiv preprint arXiv:2403.13037, 2024   
46. Lin Y, Ma X, Chu X, Jin Y, Yang Z, Wang Y, Mei H. [[LoRA]] dropout as a sparsity regularizer for overfitting control. arXiv preprint arXiv:2404.09610, 2024   
47. Wang S, Chen L, Jiang J, Xue B, Kong L, Wu C. [[LoRA]] meets dropout under a unified framework. arXiv preprint arXiv:2403.00812, 2024   
48. Yang A X, Robeyns M, Wang X, Aitchison L. Bayesian [[Low-Rank Adaptation]] for [[Large Language Models]]. arXiv preprint arXiv.2308.13111, 2023   
49. Qi Z, Tan X, Shi S, Qu C, Xu Y, Qi Y. PILLOW: enhancing efficient instruction fine-tuning via prompt matching. In: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track. 2023, 471–482   
50. Zhang L, Wu J, Zhou D, Xu G. STAR: constraint [[LoRA]] with dynamic active learning for data-efficient fine-tuning of [[Large Language Models]]. arXiv preprint arXiv.2403.01165, 2024   
51. Wang X, Aitchison L, Rudolph M. [[LoRA]] ensembles for large language model fine-tuning. arXiv preprint arXiv.2310.00035, 2023   
52. Zhao Z, Gan L, Wang G, Zhou W, Yang H, Kuang K, Wu F. [[LoRA]]retriever: Input-aware [[LoRA]] retrieval and composition for mixed tasks in the wild. arXiv preprint arXiv.2402.09997, 2024   
53. Smith J S, Cascante-Bonilla P, Arbelle A, Kim D, Panda R, Cox D D, Yang D, Kira Z, Feris R, Karlinsky L. Construct-vl: Data-free continual structured VL concepts learning. In: IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023, 14994–15004   
54. Sun Y, Li M, Cao Y, Wang K, Wang W, Zeng X, Zhao R. To be or not to be? an exp[[LoRA]]tion of continuously controllable prompt engineering. arXiv preprint arXiv:2311.09773, 2023   
55. Zhang J, Chen S, Liu J, He J. Composing parameter-

efficient modules with arithmetic operations. arXiv preprint arXiv.2306.14870, 2023   
56. Chitale R, Vaidya A, Kane A, Ghotkar A. Task arithmetic with [[LoRA]] for continual learning. arXiv preprint arXiv.2311.02428, 2023   
57. Belofsky J. Token-level adaptation of [[LoRA]] adapters for downstream task generalization. In: 6th Artificial Intelligence and Cloud Computing Conference. 2023, 168–172   
58. Jiang W, Lin B, Shi H, Zhang Y, Li Z, Kwok J T. Effective and parameter-efficient reusing fine-tuned models. arXiv preprint arXiv.2310.01886, 2023   
59. Asadi N, Beitollahi M, Khalil Y H, Li Y, Zhang G, Chen X. Does combining parameter-efficient modules improve few-shot transfer accuracy? arXiv preprint arXiv.2402.15414, 2024   
60. Huang C, Liu Q, Lin B Y, Pang T, Du C, Lin M. [[LoRA]]hub: Efficient cross-task generalization via dynamic [[LoRA]] composition. arXiv preprint arXiv.2307.13269, 2023   
61. Yadav P, Choshen L, Raffel C, Bansal M. Compeft: Compression for communicating parameter efficient updates via sparsification and quantization. arXiv preprint arXiv.2311.13171, 2023   
62. Tang A, Shen L, Luo Y, Zhan Y, Hu H, Du B, Chen Y, Tao D. Parameter efficient multi-task model fusion with partial linearization. arXiv preprint arXiv.2310.04742, 2023   
63. Shen Y, Xu Z, Wang Q, Cheng Y, Yin W, Huang L. Multimodal instruction tuning with conditional mixture of [[LoRA]]. arXiv preprint arXiv.2402.15896, 2024   
64. Buehler E L, Buehler M J. X-[[LoRA]]: Mixture of lowrank adapter experts, a flexible framework for [[Large Language Models]] with applications in protein mechanics and design. arXiv preprint arXiv.2402.07148, 2024   
65. Yang S, Ali M A, Wang C, Hu L, Wang D. Moral: Moe augmented [[LoRA]] for [[LLMs]]’ lifelong learning. arXiv preprint arXiv.2402.11260, 2024   
66. Dou S, Zhou E, Liu Y, Gao S, Zhao J, Shen W, Zhou Y, Xi Z, Wang X, Fan X, Pu S, Zhu J, Zheng R, Gui T, Zhang Q, Huang X. [[LoRA]]moe: Alleviate world knowledge forgetting in [[Large Language Models]] via moe-style plugin. arXiv preprint arXiv:2312.09979, 2023   
67. Gou Y, Liu Z, Chen K, Hong L, Xu H, Li A, Yeung D, Kwok J T, Zhang Y. Mixture of cluster-conditional [[LoRA]] experts for vision-language instruction tuning. arXiv preprint arXiv.2312.12379, 2023   
68. Liu Q, Wu X, Zhao X, Zhu Y, Xu D, Tian F, Zheng Y. Moe[[LoRA]]: An moe-based parameter efficient finetuning method for multi-task medical applications. arXiv preprint arXiv.2310.18339, 2023

69. Feng W, Hao C, Zhang Y, Han Y, Wang H. Mixture-of[[LoRA]]s: An efficient multitask tuning method for [[Large Language Models]]. In: Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation. 2024, 11371– 11380   
70. Wang Y, Lin Y, Zeng X, Zhang G. Multi[[LoRA]]: Democratizing [[LoRA]] for better multi-task learning. arXiv preprint arXiv.2311.11501, 2023   
71. Yang Y, Jiang P, Hou Q, Zhang H, Chen J, Li B. Multitask dense prediction via mixture of low-rank experts. arXiv preprint arXiv.2403.17749, 2024   
72. Agiza A R SN. M. Mt[[LoRA]]: [[Low-Rank Adaptation]] approach for efficient multi-task learning. In: CVPR. 2024   
73. Gao C, Chen K, Rao J, Sun B, Liu R, Peng D, Zhang Y, Guo X, Yang J, Subrahmanian V S. Higher layers need more [[LoRA]] experts. arXiv preprint arXiv.2402.08562, 2024   
74. Chen S, Jie Z, Ma L. Llava-mole: Sparse mixture of [[LoRA]] experts for mitigating data conflicts in instruction finetuning m[[LLMs]]. arXiv preprint arXiv.2401.16160, 2024   
75. Zhu Y, Wichers N, Lin C, Wang X, Chen T, Shu L, Lu H, Liu C, Luo L, Chen J, Meng L. Sira: Sparse mixture of low rank adaptation. arXiv preprint arXiv.2311.09179, 2023   
76. Chen Z, Wang Z, Wang Z, Liu H, Yin Z, Liu S, Sheng L, Ouyang W, Qiao Y, Shao J. Octavius: Mitigating task interference in m[[LLMs]] via moe. arXiv preprint arXiv.2311.02684, 2023   
77. Wen Y, Chaudhuri S. Batched [[Low-Rank Adaptation]] of foundation models. arXiv preprint arXiv.2312.05677, 2023   
78. Wu T, Wang J, Zhao Z, Wong N. Mixture-ofsubspaces in [[Low-Rank Adaptation]]. arXiv preprint arXiv:2406.11909, 2024   
79. Wu Y, Xiang Y, Huo S, Gong Y, Liang P. [[LoRA]]-sp: streamlined partial parameter adaptation for resource efficient fine-tuning of [[Large Language Models]]. In: Third International Conference on Algorithms, Microchips, and Network Applications. 2024, 488–496   
80. Zhang L, Zhang L, Shi S, Chu X, Li B. [[LoRA]]fa: Memory-efficient [[Low-Rank Adaptation]] for [[Large Language Models]] fine-tuning. arXiv preprint arXiv:2308.03303, 2023   
81. Liu Z, Kundu S, Li A, Wan J, Jiang L, Beerel P A. Af[[LoRA]]: Adaptive freezing of low rank adaptation in parameter efficient fine-tuning of large models. arXiv preprint arXiv:2403.13269, 2024   
82. Woo S, Park B, Kim B, Jo M, Kwon S, Jeon D, Lee

D. Dropbp: Accelerating fine-tuning of [[Large Language Models]] by dropping backward propagation. arXiv preprint arXiv:2402.17812, 2024   
83. Bałazy K, Banaei M, Aberer K, Tabor J. [[LoRA]]-xs: [[Low-Rank Adaptation]] with extremely small number of parameters. arXiv preprint arXiv:2405.17604, 2024   
84. Zhou H, Lu X, Xu W, Zhu C, Zhao T. [[LoRA]]-drop: Efficient [[LoRA]] parameter pruning based on output evaluation. arXiv preprint arXiv:2402.07721, 2024   
85. Zhang M, Chen H, Shen C, Yang Z, Ou L, Yu X, Zhuang B. [[LoRA]]prune: Pruning meets lowrank parameter-efficient fine-tuning. arXiv preprint arXiv:2305.18403, 2023   
86. Chen T, Ding T, Yadav B, Zharkov I, Liang L. [[LoRA]]shear: Efficient large language model structured pruning and knowledge recovery. arXiv preprint arXiv:2310.18356, 2023   
87. Zhu Y, Yang X, Wu Y, Zhang W. Parameterefficient fine-tuning with layer pruning on freetext sequence-to-sequence modeling. arXiv preprint arXiv:2305.08285, 2023   
88. Kopiczko D J, Blankevoort T, Asano Y M. Vera: Vector-based random matrix adaptation. arXiv preprint arXiv:2310.11454, 2023   
89. Li Y, Han S, Ji S. Vb-[[LoRA]]: Extreme parameter efficient fine-tuning with vector banks. arXiv preprint arXiv:2405.15179, 2024   
90. Gao Z, Wang Q, Chen A, Liu Z, Wu B, Chen L, Li J. Parameter-efficient fine-tuning with discrete fourier transform. arXiv preprint arXiv:2405.03003, 2024   
91. Dettmers T, Pagnoni A, Holtzman A, Zettlemoyer L. Q[[LoRA]]: Efficient finetuning of quantized [[LLMs]]. In: Advances in Neural Information Processing Systems. 2024   
92. Xu Y, Xie L, Gu X, Chen X, Chang H, Zhang H, Chen Z, Zhang X, Tian Q. Qa-[[LoRA]]: Quantization-aware [[Low-Rank Adaptation]] of [[Large Language Models]]. arXiv preprint arXiv:2309.14717, 2023   
93. Li Y, Yu Y, Liang C, He P, Karampatziakis N, Chen W, Zhao T. Loftq: [[LoRA]]-fine-tuning-aware quantization for [[Large Language Models]]. arXiv preprint arXiv:2310.08659, 2023   
94. Liao B, Monz C. Apiq: Finetuning of 2-bit quantized large language model. arXiv preprint arXiv:2402.05147, 2024   
95. Jeon H, Kim Y, Kim J j. L4q: Parameter efficient quantization-aware training on [[Large Language Models]] via [[LoRA]]-wise lsq. arXiv preprint arXiv:2402.04902, 2024   
96. Ye Z, Li D, Tian J, Lan T, Zuo J, Duan L, Lu H, Jiang Y, Sha J, Zhang K, Tang M. Aspen: High-throughput

[[LoRA]] fine-tuning of [[Large Language Models]] with a single gpu. arXiv preprint arXiv:2312.02515, 2023   
97. Chen L, Ye Z, Wu Y, Zhuo D, Ceze L, Krishnamurthy A. Punica: Multi-tenant [[LoRA]] serving. In: Proceedings of Machine Learning and Systems. 2024, 1–13   
98. Sheng Y, Cao S, Li D, Hooper C, Lee N, Yang S, Chou C, Zhu B, Zheng L, Keutzer K, others . S-[[LoRA]]: Serving thousands of concurrent [[LoRA]] adapters. arXiv preprint arXiv:2311.03285, 2023   
99. Li S, Lu H, Wu T, Yu M, Weng Q, Chen X, Shan Y, Yuan B, Wang W. Caraserve: Cpu-assisted and rankaware [[LoRA]] serving for generative llm inference. arXiv preprint arXiv:2401.11240, 2024   
100. Babakniya S, Elkordy A R, Ezzeldin Y H, Liu Q, Song K, El-Khamy M, Avestimehr S. S[[LoRA]]: Federated parameter efficient fine-tuning of language models. arXiv preprint arXiv:2308.06522, 2023   
101. Yan Y, Tang S, Shi Z, Yang Q. FeDeRA: Efficient fine-tuning of language models in federated learning leveraging weight decomposition. arXiv preprint arXiv:2404.18848, 2024   
102. Sun Y, Li Z, Li Y, Ding B. Improving [[LoRA]] in privacy-preserving federated learning. arXiv preprint arXiv:2403.12313, 2024   
103. Wu P, Li K, Wang T, Wang F. FedMS: Federated learning with mixture of sparsely activated foundations models. arXiv preprint arXiv:2312.15926, 2023   
104. Bai J, Chen D, Qian B, Yao L, Li Y. Federated finetuning of [[Large Language Models]] under heterogeneous language tasks and client resources. arXiv preprint arXiv:2402.11505, 2024   
105. Cho Y J, Liu L, Xu Z, Fahrezi A, Barnes M, Joshi G. Heterogeneous [[LoRA]] for federated fine-tuning of on-device foundation models. In: International Workshop on Federated Learning in the Age of Foundation Models in Conjunction with NeurIPS. 2023   
106. Yi L, Yu H, Wang G, Liu X, Li X. pFed[[LoRA]]: Model-Heterogeneous Personalized Federated Learning with [[LoRA]] Tuning. arXiv preprint arXiv:2310.13283, 2023   
107. Huang W, Wang Y, Cheng A, Zhou A, Yu C, Wang L. A fast, performant, secure distributed training framework for large language model. arXiv preprint arXiv:2401.09796, 2024   
108. Wang Y, Lin Y, Zeng X, Zhang G. Private[[LoRA]] for efficient privacy preserving LLM. arXiv preprint arXiv:2311.14030, 2023   
109. Zhang Y, Wang M, Wu Y, Tiwari P, Li Q, Wang B, Qin J. Dialoguellm: Context and emotion knowledgetuned [[Large Language Models]] for emotion recognition in conversations. arXiv preprint arXiv:2310.11374, 2024

110. Li Z, Li X, Liu Y, Xie H, Li J, Wang F L, Li Q, Zhong X. Label supervised llama finetuning. arXiv preprint arXiv:2310.01208, 2023   
111. Bornheim T, Grieger N, Blaneck P G, Bialonski S. Speaker attribution in german parliamentary debates with q[[LoRA]]-adapted [[Large Language Models]]. arXiv preprint arXiv:2309.09902, 2024   
112. Xue L, Zhang D, Dong Y, Tang J. Autore: Documentlevel relation extraction with [[Large Language Models]]. arXiv preprint arXiv:2403.14888, 2024   
113. Alves D M, Guerreiro N M, Alves J, Pombal J, Rei R, Souza d J G C, Colombo P, Martins A F T. Steering [[Large Language Models]] for machine translation with finetuning and in-context learning. In: Findings of the Association for Computational Linguistics. 2023, 11127–11148   
114. Zheng J, Hong H, Wang X, Su J, Liang Y, Wu S. Finetuning [[Large Language Models]] for domain-specific machine translation. arXiv preprint arXiv:2402.15061, 2024   
115. Mujadia V, Urlana A, Bhaskar Y, Pavani P A, Shravya K, Krishnamurthy P, Sharma D M. Assessing translation capabilities of [[Large Language Models]] involving english and indian languages. arXiv preprint arXiv:2311.09216, 2023   
116. Zhang Y, Wang J, Yu L, Xu D, Zhang X. Personalized [[LoRA]] for human-centered text understanding. In: Thirty-Eighth AAAI Conference on Artificial Intelligence. 2024, 19588–19596   
117. Liu Y, An C, Qiu X. Y-tuning: An efficient tuning paradigm for large-scale pre-trained models via label representation learning. Frontiers of Computer Science, 2024, 18(4): 184320   
118. Liu S, Keung J, Yang Z, Liu F, Zhou Q, Liao Y. Delving into parameter-efficient fine-tuning in code change learning: An empirical study. arXiv preprint arXiv:2402.06247, 2024   
119. Guo Y, Gao X, Jiang B. An empirical study on jit defect prediction based on bert-style model. arXiv preprint arXiv:2403.11158, 2024   
120. Ayupov S, Chirkova N. Parameter-efficient finetuning of transformers for source code. arXiv preprint arXiv:2212.05901, 2022   
121. Silva A, Fang S, Monperrus M. Repairllama: Efficient representations and fine-tuned adapters for program repair. arXiv preprint arXiv:2312.15698, 2023   
122. Roberson R, Kaki G, Trivedi A. Analyzing the effectiveness of [[Large Language Models]] on text-to-sql synthesis. arXiv preprint arXiv:2401.12379, 2024   
123. Pan J, Sade A, Kim J, Soriano E, Sole G, Fla-´ mant S. Stelocoder: a decoder-only LLM for multi-

language to python code translation. arXiv preprint arXiv:2310.15539, 2023   
124. Sidahmed H, Phatale S, Hutcheson A, Lin Z, Chen Z, Yu Z, Jin J, Komarytsia R, Ahlheim C, Zhu Y, Chaudhary S, Li B, Ganesh S, Byrne B, Hoffmann J, Mansoor H, Li W, Rastogi A, Dixon L. Perl:parameter efficient reinforcement learning from human feedback. arXiv preprint arXiv:2403.10704, 2024   
125. Santacroce M, Lu Y, Yu H, Li Y, Shen Y. Efficient RLHF: reducing the memory usage of PPO. arXiv preprint arXiv:2309.00754, 2023   
126. Sun S, Gupta D, Iyyer M. Exploring the impact of [[Low-Rank Adaptation]] on the performance, efficiency, and regularization of RLHF. arXiv preprint arXiv:2309.09055, 2023   
127. Quan S. Dmoerm: Recipes of mixture-of-experts for effective reward modeling. arXiv preprint arXiv:2403.01197, 2024   
128. Zhang S, Chen Z, Chen S, Shen Y, Sun Z, Gan C. Improving reinforcement learning from human feedback with efficient reward model ensemble. arXiv preprint arXiv:2401.16635, 2024   
129. Zhai Y, Zhang H, Lei Y, Yu Y, Xu K, Feng D, Ding B, Wang H. Uncertainty-penalized reinforcement learning from human feedback with diverse reward [[LoRA]] ensembles. arXiv preprint arXiv:2401.00243, 2024   
130. Yang A X, Robeyns M, Coste T, Wang J, Bou-Ammar H, Aitchison L. Bayesian reward models for LLM alignment. arXiv preprint arXiv:2402.13210, 2024   
131. Yang A X, Robeyns M, Wang X, Aitchison L. Bayesian [[Low-Rank Adaptation]] for [[Large Language Models]]. arXiv preprint arXiv:2308.13111, 2023   
132. Tran H, Yang Z, Yao Z, Yu H. Bioinstruct: Instruction tuning of [[Large Language Models]] for biomedical natural language processing. arXiv preprint arXiv:2310.19975, 2023   
133. Gema A P, Daines L, Minervini P, Alex B. Parameterefficient fine-tuning of llama for the clinical domain. arXiv preprint arXiv:2307.03042, 2023   
134. Toma A, Lawler P R, Ba J, Krishnan R G, Rubin B B, Wang B. Clinical camel: An open-source expert-level medical language model with dialogue-based knowledge encoding. arXiv preprint arXiv:2305.12031, 2023   
135. Suri K, Mishra P, Saha S, Singh A. Suryakiran at mediqa-sum 2023: Leveraging [[LoRA]] for clinical dialogue summarization. In: Working Notes of the Conference and Labs of the Evaluation Forum. 2023, 1720–1735   
136. Ji Y, Yu Z, Wang Y. Assertion detection large language model in-context learning [[LoRA]] fine-tuning. arXiv

preprint arXiv:2401.17602, 2024   
137. Wang R, Duan Y, Lam C, Chen J, Xu J, Chen H, Liu X, Pang P C, Tan T. Ivygpt: Interactive chinese pathway language model in medical domain. In: Artificial Intelligence - Third CAAI International Conference. 2023, 378–382   
138. Bhatti A, Parmar S, Lee S. SM70: A large language model for medical devices. arXiv preprint arXiv:2312.06974, 2023   
139. Konstantinidis T, Iacovides G, Xu M, Constantinides T G, Mandic D P. Finllama: Financial sentiment classification for algorithmic trading applications. arXiv preprint arXiv:2403.12285, 2024   
140. Pavlyshenko B M. Financial news analytics using fine-tuned llama 2 GPT model. arXiv preprint arXiv:2308.13032, 2023   
141. Liu X, Wang G, Zha D. Fingpt: Democratizing internet-scale data for financial [[Large Language Models]]. arXiv preprint arXiv:2307.10485, 2023   
142. Li J, Lei Y, Bian Y, Cheng D, Ding Z, Jiang C. Ra-cfgpt: Chinese financial assistant with retrievalaugmented large language model. Frontiers of Computer Science, 2024, 18(5): 185350   
143. Zhou X, Sun Z, Li G. Db-gpt: Large language model meets database. Data Science and Engineering, 2024, 9(1): 102–111   
144. Li S. Diffstyler: Diffusion-based localized image style transfer. arXiv preprint arXiv:2403.18461, 2024   
145. Frenkel Y, Vinker Y, Shamir A, Cohen-Or D. Implicit style-content separation using b-[[LoRA]]. arXiv preprint arXiv:2403.14572, 2024   
146. Liu Y, Yu C, Shang L, He Y, Wu Z, Wang X, Xu C, Xie H, Wang W, Zhao Y, Zhu L, Cheng C, Chen W, Yao Y, Zhou W, Xu J, Wang Q, Chen Y, Xie X, Sun B. Facechain: A playground for human-centric artificial intelligence generated content. arXiv preprint arXiv:2308.14256, 2023   
147. Liao Q, Xia G, Wang Z. Calliffusion: Chinese calligraphy generation and style transfer with diffusion modeling. arXiv preprint arXiv:2305.19124, 2023   
148. Shrestha S, Venkataramanan A, others . Style transfer to calvin and hobbes comics using stable diffusion. arXiv preprint arXiv:2312.03993, 2023   
149. Li L, Zeng H, Yang C, Jia H, Xu D. Block-wise [[LoRA]]: Revisiting fine-grained [[LoRA]] for effective personalization and stylization in text-to-image generation. arXiv preprint arXiv:2403.07500, 2024   
150. Kong Z, Zhang Y, Yang T, Wang T, Zhang K, Wu B, Chen G, Liu W, Luo W. OMG: occlusion-friendly personalized multi-concept generation in diffusion models. arXiv preprint arXiv:2403.10983, 2024

151. Shi J, Hua H. Space narrative: Generating images and 3d scenes of chinese garden from text using deep learning. In: xArch–creativity in the age of digital reproduction symposium. 2023, 236–243   
152. Jin Z, Song Z. Generating coherent comic with rich story using chatgpt and stable diffusion. arXiv preprint arXiv:2305.11067, 2023   
153. Wang H, Xiang X, Fan Y, Xue J. Customizing 360-degree panoramas through text-to-image diffusion models. In: Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision. 2024, 4933–4943   
154. Guo J, Xu X, Pu Y, Ni Z, Wang C, Vasu M, Song S, Huang G, Shi H. Smooth diffusion: Crafting smooth latent spaces in diffusion models. arXiv preprint arXiv:2312.04410, 2023   
155. Cheng J, Xie P, Xia X, Li J, Wu J, Ren Y, Li H, Xiao X, Zheng M, Fu L. Resadapter: Domain consistent resolution adapter for diffusion models. arXiv preprint arXiv:2403.02084, 2024   
156. Smith J S, Hsu Y C, Kira Z, Shen Y, Jin H. Continual diffusion with stamina: Stack-and-mask incremental adapters. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024, 1744–1754   
157. Sun J, Fu D, Hu Y, Wang S, Rassin R, Juan D C, Alon D, Herrmann C, Steenkiste v S, Krishna R, others . Dreamsync: Aligning text-to-image generation with image understanding feedback. In: Synthetic Data for Computer Vision Workshop@ CVPR 2024. 2023   
158. Wang Z, Wang X, Xie L, Qi Z, Shan Y, Wang W, Luo P. Styleadapter: A single-pass [[LoRA]]-free model for stylized image generation. arXiv preprint arXiv:2309.01770, 2023   
159. Gu Y, Wang X, Wu J Z, Shi Y, Chen Y, Fan Z, Xiao W, Zhao R, Chang S, Wu W, Ge Y, Shan Y, Shou M Z. Mix-of-show: Decentralized [[Low-Rank Adaptation]] for multi-concept customization of diffusion models. In: Advances in Neural Information Processing Systems. 2023   
160. Luo S, Tan Y, Patil S, Gu D, Platen v P, Passos A, Huang L, Li J, Zhao H. Lcm-[[LoRA]]: A universal stable-diffusion acceleration module. arXiv preprint arXiv:2311.05556, 2023   
161. Golnari P A. [[LoRA]]-enhanced distillation on guided diffusion models. arXiv preprint arXiv:2312.06899, 2023   
162. Ren Y, Zhou Y, Yang J, Shi J, Liu D, Liu F, Kwon M, Shrivastava A. Customize-a-video: One-shot motion customization of text-to-video diffusion models. arXiv preprint arXiv:2402.14780, 2024

163. Deng Y, Wang R, Zhang Y, Tai Y, Tang C. Dragvideo: Interactive drag-style video editing. arXiv preprint arXiv:2312.02216, 2023   
164. Yang S, Zhou Y, Liu Z, Loy C C. Rerender A video: Zero-shot text-guided video-to-video translation. In: SIGGRAPH Asia 2023 Conference Papers. 2023, 1– 11   
165. Khandelwal A. Infusion: Inject and attention fusion for multi concept zero-shot text-based video editing. In: Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023, 3017–3026   
166. Blattmann A, Dockhorn T, Kulal S, Mendelevitch D, Kilian M, Lorenz D, Levi Y, English Z, Voleti V, Letts A, others . Stable video diffusion: Scaling latent video diffusion models to large datasets. arXiv preprint arXiv:2311.15127, 2023   
167. Guo Y, Yang C, Rao A, Wang Y, Qiao Y, Lin D, Dai B. Animatediff: Animate your personalized text-toimage diffusion models without specific tuning. arXiv preprint arXiv:2307.04725, 2023   
168. Huang T, Zeng Y, Zhang Z, Xu W, Xu H, Xu S, Lau R W H, Zuo W. Dreamcontrol: Control-based textto-3d generation with 3d self-prior. arXiv preprint arXiv:2312.06439, 2023   
169. Ma Y, Fan Y, Ji J, Wang H, Sun X, Jiang G, Shu A, Ji R. X-dreamer: Creating high-quality 3d content by bridging the domain gap between text-to-2d and textto-3d generation. arXiv preprint arXiv:2312.00085, 2023   
170. Yu K, Liu J, Feng M, Cui M, Xie X. Boosting3d: High-fidelity image-to-3d by boosting 2d diffusion prior to 3d prior with progressive learning. arXiv preprint arXiv:2311.13617, 2023   
171. Yoo S, Kim K, Kim V G, Sung M. As-plausible-aspossible: Plausibility-aware mesh deformation using 2d diffusion priors. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024, 4315–4324   
172. Zhang Y, Xu Q, Zhang L. Dragtex: Generative pointbased texture editing on 3d mesh. arXiv preprint arXiv:2403.02217, 2024   
173. Ding H, Gao J, Yuan Y, Wang Q. Samlp: A customized segment anything model for license plate detection. arXiv preprint arXiv:2401.06374, 2024   
174. Ye Z, Lovell L, Faramarzi A, Ninic J. Sambased instance segmentation models for the automation of structural damage detection. arXiv preprint arXiv:2401.15266, 2024   
175. Na S, Guo Y, Jiang F, Ma H, Huang J. Segment any cell: A sam-based auto-prompting fine-tuning framework for nuclei segmentation. arXiv preprint

arXiv:2401.13220, 2024   
176. Chen X, Wang C, Ning H, Li S. SAM-OCTA: prompting segment-anything for OCTA image segmentation. arXiv preprint arXiv:2310.07183, 2023   
177. Feng W, Zhu L, Yu L. Cheap lunch for medical image segmentation by fine-tuning SAM on few exemplars. arXiv preprint arXiv:2308.14133, 2023   
178. Zhang K, Liu D. Customized segment anything model for medical image segmentation. arXiv preprint arXiv:2304.13785, 2023   
179. Wang A, Islam M, Xu M, Zhang Y, Ren H. SAM meets robotic surgery: An empirical study on generalization, robustness and adaptation. In: International Conference on Medical Image Computing and Computer-Assisted Intervention. 2023, 234–244   
180. Lin L, Fan H, Zhang Z, Wang Y, Xu Y, Ling H. Tracking meets [[LoRA]]: Faster training, larger model, stronger performance. arXiv preprint arXiv:2403.05231, 2024   
181. Kong C, Li H, Wang S. Enhancing general face forgery detection via vision transformer with [[Low-Rank Adaptation]]. In: 2023 IEEE 6th International Conference on Multimedia Information Processing and Retrieval. 2023, 102–107   
182. Chen Z, Huang H, Andrusenko A, Hrinchuk O, Puvvada K C, Li J, Ghosh S, Balam J, Ginsburg B. SALM: speech-augmented language model with incontext learning for speech recognition and translation. arXiv preprint arXiv:2310.09424, 2023   
183. Dong X, Zhang P, Zang Y, Cao Y, Wang B, Ouyang L, Wei X, Zhang S, Duan H, Cao M, Zhang W, Li Y, Yan H, Gao Y, Zhang X, Li W, Li J, Chen K, He C, Zhang X, Qiao Y, Lin D, Wang J. Internlm-xcomposer2: Mastering free-form text-image composition and comprehension in vision-language large model. arXiv preprint arXiv:2401.16420, 2024   
184. Ye Q, Xu H, Xu G, Ye J, Yan M, Zhou Y, Wang J, Hu A, Shi P, Shi Y, Li C, Xu Y, Chen H, Tian J, Qi Q, Zhang J, Huang F. mplug-owl: Modularization empowers [[Large Language Models]] with multimodality. arXiv preprint arXiv:2304.14178, 2023   
185. Lee B, Park B, Kim C W, Ro Y M. Collavo: Crayon large language and vision model. arXiv preprint arXiv:2402.11248, 2024   
186. Yeo J H, Han S, Kim M, Ro Y M. Where visual speech meets language: VSP-LLM framework for efficient and context-aware visual speech processing. arXiv preprint arXiv:2402.15151, 2024   
187. Liu Z, Li S, Luo Y, Fei H, Cao Y, Kawaguchi K, Wang X, Chua T. Molca: Molecular graph-language modeling with cross-modal projector and uni-modal adapter. In: Proceedings of the 2023 Conference on Empiri-

cal Methods in Natural Language Processing. 2023, 15623–15638   
188. Ren Y, Chen Y, Liu S, Wang B, Yu H, Cui Z. TPLLM: A traffic prediction framework based on pretrained [[Large Language Models]]. arXiv preprint arXiv:2403.02221, 2024   
189. Aghajanyan A, Gupta S, Zettlemoyer L. Intrinsic dimensionality explains the effectiveness of language model fine-tuning. In: Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing. 2021, 7319–7328   
190. Fomenko V, Yu H, Lee J, Hsieh S, Chen W. A note on [[LoRA]]. arXiv preprint arXiv:2404.05086, 2024   
191. Bershatsky D, Cherniuk D, Daulbaev T, Mikhalev A, Oseledets I V. Lotr: Low tensor rank weight adaptation. arXiv preprint arXiv.2402.01376, 2024   
192. Edalati A, Tahaei M S, Kobyzev I, Nia V P, Clark J J, Rezagholizadeh M. Krona: Parameter efficient tuning with kronecker adapter. arXiv preprint arXiv.2212.10650, 2022   
193. He X, Li C, Zhang P, Yang J, Wang X E. Parameterefficient model adaptation for vision transformers. In: Thirty-Seventh AAAI Conference on Artificial Intelligence. 2023, 817–825   
194. Mahabadi R K, Henderson J, Ruder S. Compacter: Efficient low-rank hypercomplex adapter layers. In: Advances in Neural Information Processing Systems. 2021, 1022–1035   
195. Liao B, Meng Y, Monz C. Parameter-efficient finetuning without introducing new latency. In: Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics. 2023, 4242–4260   
196. Hendrycks D, Burns C, Basart S, Zou A, Mazeika M, Song D, Steinhardt J. Measuring massive multitask language understanding. arXiv preprint arXiv:2009.03300, 2020   
197. He J, Zhou C, Ma X, Berg-Kirkpatrick T, Neubig G. Towards a unified view of parameter-efficient transfer learning. In: International Conference on Learning Representations. 2022   
198. Geshkovski B, Letrouit C, Polyanskiy Y, Rigollet P. A mathematical perspective on transformers. arXiv preprint arXiv.2312.10794, 2023   
199. Geshkovski B, Letrouit C, Polyanskiy Y, Rigollet P. The emergence of clusters in self-attention dynamics. In: Annual Conference on Neural Information Processing Systems. 2023   
200. Sander M E, Ablin P, Blondel M, Peyre G. Sinkform-´ ers: Transformers with doubly stochastic attention. In: International Conference on Artificial Intelligence and

Statistics. 2022, 3515–3530   
201. Jacot A, Hongler C, Gabriel F. Neural tangent kernel: Convergence and generalization in neural networks. In: Annual Conference on Neural Information Processing Systems. 2018, 8580–8589   
202. Ren W, Li X, Wang L, Zhao T, Qin W. Analyzing and reducing catastrophic forgetting in parameter efficient tuning. arXiv preprint arXiv.2402.18865, 2024   
203. Touvron H, Martin L, Stone K, Albert P, Almahairi A, Babaei Y, Bashlykov N, Batra S, Bhargava P, Bhosale S, Bikel D, Blecher L, Canton-Ferrer C, Chen M, Cucurull G, Esiobu D, Fernandes J, Fu J, Fu W, Fuller B, Gao C, Goswami V, Goyal N, Hartshorn A, Hosseini S, Hou R, Inan H, Kardas M, Kerkez V, Khabsa M, Kloumann I, Korenev A, Koura P S, Lachaux M, Lavril T, Lee J, Liskovich D, Lu Y, Mao Y, Martinet X, Mihaylov T, Mishra P, Molybog I, Nie Y, Poulton A, Reizenstein J, Rungta R, Saladi K, Schelten A, Silva R, Smith E M, Subramanian R, Tan X E, Tang B, Taylor R, Williams A, Kuan J X, Xu P, Yan Z, Zarov I, Zhang Y, Fan A, Kambadur M, Narang S, Rodriguez A, Stojnic R, Edunov S, Scialom T. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv.2307.09288, 2023   
204. Zhao J, Zhang Z, Chen B, Wang Z, Anandkumar A, Tian Y. Galore: Memory-efficient LLM training by gradient low-rank projection. arXiv preprint arXiv.2403.03507, 2024   
205. Biderman D, Ortiz J J G, Portes J, Paul M, Greengard P, Jennings C, King D, Havens S, Chiley V, Frankle J, Blakeney C, Cunningham J P. [[LoRA]] learns less and forgets less. arXiv preprint arXiv.2405.09673, 2024   
206. Han A, Li J, Huang W, Hong M, Takeda A, Jawanpuria P, Mishra B. Sltrain: a sparse plus low-rank approach for parameter and memory efficient pretraining. arXiv preprint arXiv:2406.02214, 2024   
207. Sui Y, Yin M, Gong Y, Xiao J, Phan H, Yuan B. ELRT: efficient low-rank training for compact convolutional neural networks. arXiv preprint arXiv.2401.10341, 2024   
208. Meng X, Dai D, Luo W, Yang Z, Wu S, Wang X, Wang P, Dong Q, Chen L, Sui Z. Periodic[[LoRA]]: Breaking the low-rank bottleneck in [[LoRA]] optimization. arXiv preprint arXiv.2402.16141, 2024   
209. Frank M, Wolfe P, others . An algorithm for quadratic programming. Naval research logistics quarterly, 1956, 3(1-2): 95–110   
210. Elsken T, Metzen J H, Hutter F. Neural architecture search: A survey. J. Mach. Learn. Res., 2019, 20: 55:1–55:21   
211. Liu Y, Ott M, Goyal N, Du J, Joshi M, Chen D, Levy

O, Lewis M, Zettlemoyer L, Stoyanov V. Roberta: A robustly optimized bert pretraining approach. arXiv preprint arXiv:1907.11692, 2019   
212. Wang A, Singh A, Michael J, Hill F, Levy O, Bowman S R. Glue: A multi-task benchmark and analysis platform for natural language understanding. arXiv preprint arXiv:1804.07461, 2018   
213. Renduchintala A, Konuk T, Kuchaiev O. Tied-[[LoRA]]: Enhancing parameter efficiency of [[LoRA]] with weight tying. In: Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies. 2024   
214. Hansen N, Ostermeier A. Adapting arbitrary normal mutation distributions in evolution strategies: The covariance matrix adaptation. In: Proceedings of IEEE international conference on evolutionary computation. 1996, 312–317   
215. Ye M, Fang X, Du B, Yuen P C, Tao D. Heterogeneous federated learning: State-of-the-art and research challenges. ACM Computing Surveys, 2024, 56(3): 79:1– 79:44   
216. Liu X Y, Zhu R, Zha D, Gao J, Zhong S, Qiu M. Differentially private [[Low-Rank Adaptation]] of large language model using federated learning. arXiv preprint arXiv:2312.17493, 2023

![](images/380883e427d8124e495b9c54c8506508727fc09c7388fcc6d2587bc1255bffc0.jpg)

Yuren Mao received his PhD degree under the supervision of Prof. Xuemin Lin in computer science from University of New South Wales, Australia in 2022. He is currently an assistant professor with the School of Software Tech-

nology, Zhejiang University, China. His current research interests include [[Large Language Models]] and its applications in Data Intelligence.

![](images/a37486145536da6cf02cbffea8114f5f0a1b43158a232c0f309c1149b366a285.jpg)

Yuhang Ge is currently working toward his PhD degree in the School of Software Technology at Zhejiang University, China. His research interests include [[Large Language Models]] and Data Management.

![](images/a44c425628b87776f3e495bc6df5bfd19726e20781629861c3557326e127d271.jpg)

Yijiang Fan is currently studying as a master’s student in the School of Software Technology at Zhejiang University, China. His research interests include [[Large Language Models]] and collaborative inference.

![](images/73af84056024245f4ab2af189e78ff60bcad57fadb3df2b90993251bd7b4e118.jpg)

Wenyi Xu is currently studying as a master’s student in the School of Software Technology at Zhejiang University, China. His research interests include Multimodal Large Models and RAG.

![](images/6d99d72aefc30e885101b41aab5b86e270aa8c6cf5b451a580c29885d757f801.jpg)

Yu Mi is currently studying as a master’s student in the School of Software Technology at Zhejiang University, China. Her research interests include [[Large Language Models]] and AI for science.

![](images/df101c89234a480b6cc226d173c19cb7a88ddaf6d4a218f825cf6d49d93bc7d8.jpg)

Zhonghao Hu is currently studying as a master’s student in the School of Software Technology at Zhejiang University, China. His research interests include [[Large Language Models]] and data discovery.

![](images/365cbef7c5d0b99088e9e9405d9c9eba964ce31c9ac4e74e7e18f0fcc5c78a85.jpg)

Yunjun Gao received the PhD degree in computer science from Zhejiang University, China, in 2008. He is currently a professor in the College of Computer Science and Technology, Zhejiang University, China. His research

interests include Database, Big Data Management and Analytics, and AI interaction with DB technology.