---
title: "Task-Specific Parameter Decoupling for Class Incremental Learning"
authors:
  - "Runhang Chen"
  - "Xiao-Yuan Jing"
  - "Fei Wu"
  - "Wei Zheng"
  - "Yaru Hao"
date: "2023-01-01"
year: 2023
journal: "Pattern Recognition"
abstract: "Class incremental learning (CIL) enables deep networks to progressively"
abstract_cn: "类增量学习使深度网络能够逐步学习新任务，同时记住先前学到的知识。一种流行的类增量学习设计是应用共享特征提取器来学习旧类和新类。然而，这种设计可能导致表示干扰，即从不同任务获得的知识相互干扰。这限制了维持先前任务特征信息的能力，特别是在无法访问先前任务训练数据的情况下。为了克服这一限制，我们提出了一种新颖的类增量学习方法，称为任务特定模型参数解耦，包括参数解耦框架和动态参数融合策略。参数解耦框架将每个任务的知识压缩到一组紧凑的任务特定模型参数中。在这种情况下，与不同任务相关的紧凑模型参数之间的相互作用被消除，以减少表示干扰。此外，我们采用动态参数融合策略来自适应地融合较大模型的参数。随着学习任务的进行，动态参数融合策略增强了模型的适应性和稳定性。在包括CIFAR100和TinyImageNet在内的基准数据集上的大量实验证明了我们的方法相对于最先进方法的性能提升。"
keywords:
  - "[[Class incremental learning]]"
cite: "[1] Chen R, Jing X Y, Wu F, et al. Task‑specific parameter decoupling for class"
aiSum: "类增量学习参数解耦方法：PD框架将任务知识压缩至任务特定参数，DPF策略自适应融合参数，消除表示干扰，在CIFAR100/TinyImageNet上优于SOTA方法。"
confidence: "medium"
---

# Task-specific parameter decoupling for class incremental learning

![](images/124b307f676bd240774d172775f118e0bf270be9ee8f7c9c3421ef812030858f.jpg)

Runhang Chen a, Xiao-Yuan Jing a,c,d,∗, Fei Wu b, Wei Zheng a, Yaru Hao a

a School of Computer Science, Wuhan University, Wuhan, 430072, China   
b College of Automation and College of Artificial Intelligence, Nanjing University of Posts and Telecommunications, NanJing, 210003, China   
c Guangdong Provincial Key Laboratory of Petrochemical Equipment Fault Diagnosis and School of Computer, Guangdong University of Petrochemical Technology, Maoming, 525000, China   
d State Key Laboratory for Novel Software Technology, Nanjing University, Nanjing, 210008, China

# A R T I C L E I N F O

Keywords:

Class incremental learning

Model parameter decoupling

Dynamic parameter fusion

![](images/935555d512f3c8f7f44307420047d32a5cdc04eb5c8b2f0e0e2ba928f0313271.jpg)

# A B S T R A C T

Class incremental learning (CIL) enables deep networks to progressively learn new tasks while remembering previously learned knowledge. A popular design for CIL involves applying a shared feature extractor to learn old and new classes. However, this design can lead to representation interference, a phenomenon in which knowledge acquired from different tasks interferes with each other. This limits the ability to maintain feature information from previous tasks, especially without access to training data from previous tasks. To overcome this limitation, we present a novel CIL approach called task-specific model parameter decoupling, which includes a parameter decoupling (PD) framework and a dynamic-parameter-fusion (DPF) strategy. The PD framework compresses the knowledge of each task into a compact set of task-specific model parameters. In this situation, interactions between compact model parameters related to different tasks are eliminated to reduce representation interference. In addition, we adopt a DPF strategy to adaptively fuse the parameters of the larger model. As the learning task progresses, the DPF strategy enhances the model’s adaptability and stability. Extensive experiments on benchmark datasets, including CIFAR100 and TinyImageNet, demonstrate the performance improvement of our approach over state-of-the-art methods.

# 1. Introduction

Many real-world applications [1–4], such as recommendation systems [1], operate in dynamic environments where new data are often encountered. To remain robust and effective in these non-stationary settings, the machine learning (ML) models for these applications must be capable of lifelong adaptation to novel information. However, retraining the models from scratch using growing data is prohibitive [5]. A straightforward solution is to incrementally fine-tune the model using only the new data. Unfortunately, this approach often leads to catastrophic forgetting [6], where the model performance drastically deteriorates for previously learned tasks.

Catastrophic forgetting is a fundamental problem in ML models [7,8]. Incremental learning methods [9–12] offer a potential solution to this issue. Depending on the research objectives [13,14], incremental learning can be categorized into three main settings: 1) domain incremental learning (DIL), which concentrates on continuous learning and integrating different sample spaces; 2) task

![](images/1586517b4e84224d0cb6242f16d99b6c6fbcb3d818e36a8d6073df8e45cd3e33.jpg)

![](images/8771c28cbf476d3f792bd84214bce956152617dc84e6aa302b8212953a080cff.jpg)  
Fig. 1. The motivation of learning task-specific filters. In standard CNNs applied to CIL, each filter responds to multiple tasks. However, this can cause representation interference, where the features of different tasks overlap and interfere with one another (representation interference). In contrast, we mitigate the representation interference by isolating task-specific parameters, forcing each filter to respond to one task.

incremental learning (TIL), which concentrates on recognizing different classes within each task; and 3) class incremental learning (CIL), which attaches importance to the discrimination of all classes. In DIL, the learning model only focuses on samples of the same class from different domains [9,12]. TIL [13] employs a learning strategy that continuously learns new tasks involving new classes, allowing learning models to access the task identity (task ID) at inference time. Notably, missing task IDs would render the model unusable. In contrast, CIL provides a new option for incremental learning because it does not depend on the task ID [8,15].

From a data preservation perspective, CIL methods include rehearsal and non-rehearsal methods. Rehearsal methods store representative samples [8,16] or generate pseudo-samples [17,18] of past classes to train the model alongside the training samples of new classes. For example, iCaRL [8] chooses or saves typical samples of past tasks for joint training with subsequent tasks. However, storing samples from previous classes is not recommended owing to memory constraints or privacy concerns [14,19]. In addition, generating pseudo-samples using generative networks is not an ideal choice because of the challenges of low efficiency and complicated training processes. Conversely, non-rehearsal methods only require data from the current task to train continually closer to the actual demand.

According to mainstream classification, non-rehearsal methods can be classified into three paradigms: regularization, activation, and structure-based methods. Regularization-based methods focus on penalizing and estimating critical parameters in a model while learning a new task. A classic method is the elastic weight consolidation (EWC) [12], which calculates a Fisher information matrix to capture and constrain the crucial parameters of the learning model. The activation-based method is a principal branch of CIL that employs knowledge distillation (KD) [20] to maintain the representations of previous data while learning new tasks. For example, Learning without Forgetting (LwF) [19] uses the previous model’s outputs to retain the knowledge of prior tasks via KD loss. Regularization and activation-based methods accumulate new knowledge within a shared model, this can cause representation interference [21,22], as shown in Fig. 1.

Structure-based methods [23,24] aim to prevent interference with previous task representations by freezing the network parameters for old classes and adding additional components (such as filters for convolutional neural networks [CNNs] or neurons for Multi-layer perceptrons [MLPs]) to each layer for new classes. An intuitive idea is to dynamically expand the network capacity and freeze the network parameters for old classes while learning new tasks. This causes the model to grow incrementally as the number of tasks increases. Researchers have proposed another potential solution using model compression techniques [25]. The solution is to remove unimportant parameters and assign sparse connections to each task in a small sub-network. However, this solution requires additional masks to indicate the trainable parameters during model training, which increases the cost of maintaining and distributing masks during training. In addition, pruning unimportant parameters, especially removing numerous parameters, can affect impact model training and damage model performance [26,27].

Motivated by the above discussion, we propose a novel structure-based approach for non-rehearsal CIL consisting of a decoupling framework and a parameter fusion strategy. The parameter decoupling framework separates the model parameters of each layer in the model into task-specific model parameters (called compact models). Unlike previous methods, our decoupling framework assigns filters in each network layer to different tasks in an orderly manner; thereby, eliminating the need to allocate and maintain masks during training. Moreover, we introduce a parameter fusion strategy to compress large parameters into compact model parameters instead of discarding unimportant parameters. In this situation, our parameter strategy enhances the model’s adaptability and stability in incremental learning tasks.

We summarize the contributions of our work as follows:

• We propose a novel structure-based approach for non-rehearsal class incremental learning, including a parameter decoupling framework and a dynamic parameter fusion strategy. The proposed approach uses the limited capacity of the model to improve the model performance by isolating the task-specific parameter.   
• The parameter decoupling framework is designed to address the issue of representation interference between parameters and tasks in incremental learning. Our parameter decoupling framework eliminates the need to maintain masks for sparse connections between different tasks during training. This makes implementation easier and reduces the maintenance cost of binary masks.

• We also introduce a dynamic parameter fusion strategy that fuses network parameters to compress the model. Our parameter fusion strategy maintains performance by fusing all parameters rather than removing unimportant parameters, which helps maintain model stability during training.   
• Experiment results verify the efficiency and the effectiveness of our approach, compared to other state-of-the-art methods. Quantitatively, the average accuracy of our approach on CIFAR-100 and TinyImageNet improves by 0.87% and 0.67%, respectively. Compared to structure-based methods, our approach improves the average accuracy by at least 2.27% and 4.12% on CIFAR-100 and TinyImageNet, respectively.

# 2. Related work

To assist the readers in understanding the proposed approach, we summarize incremental learning from the perspective of background and recent advancements. Considering that model compression techniques inspire structure-based methods, we also review recent work on model compression.

# 2.1. Class incremental learning

Class incremental learning (CIL) methods can be categorized into two types based on whether the data information of past classes is accessible: rehearsal-based methods and non-rehearsal-based methods. Rehearsal-based methods store a portion of representative instances or generate pseudo-samples from each class and rehearse them when learning new ones. For example, iCaRL [8] and MneM [17] concentrate on the way for selecting or storing representative instances. CAN [28] uses class-conditional image synthesis networks to reconstruct the sample distributions from the previous tasks. However, rehearsal-based methods have some unavoidable issues in CIL. One issue is that selecting or storing representative instances may not always be feasible owing to storage overhead and individual privacy protection. Another issue is that generating pseudo-samples is not always available because generative networks can be unstable during training. Quite differently, non-rehearsal methods have gradually attracted more attention because of their universality and not limited to the above two issues.

Non-rehearsal-based methods can be classified into three categories: regularization-based, activation-based, and structure-based methods. Regularization-based methods [12,29] introduce a penalty term that prevents updating important weights of previous tasks when learning new tasks. The importance of parameters is usually determined by different evaluation strategies after each task has been learned. Activation-based methods [15,30] distill knowledge from previous snapshots of the model while new tasks are being learned. These methods balance old and new classes based on distillation loss terms [5]. However, regularization and activationbased methods utilize a single shared model to sequentially learn new classes, which can cause representation interference between old and new classes. In contrast, structure-based methods isolate parameters among tasks to mitigate representation interference.

# 2.2. Model compression

Structure-based continual learning (CIL) methods rely on model compression techniques to mitigate the forgetting problem. Before introducing the structure-based CIL methods, we briefly review three compression techniques: knowledge distillation (KD), weight pruning, and filter pruning. KD techniques transfer knowledge from large neural networks to smaller ones, first proposed by Bucilua et al. [31] and later known as knowledge distillation [20]. Numerous variants and extensions of KD [32,33] have been proposed to improve the performance of smaller models. Weight pruning techniques [34,35] compress the model by resetting unimportant weights. For instance, DNWP [34] reduces network complexity by dynamically pruning network connections. Weight pruning techniques typically require binary masks to indicate which weights are pruned or retained. However, binary masks introduce additional memory and computation overhead, which may limit the benefits of pruning. Filter pruning techniques [36–38] reduce the number of model parameters at the filter or channel level. For example, CPA [36] prunes the network based on a LASSO regression channel selection and the least square reconstruction. RC [38] determines the channel configuration of the pruned models by random search. By removing only part of the channels to implement filter pruning, the model may lose information about the filter’s spatial or frequency characteristics. Different from previous methods, we fuse all filters into a compact set in a dynamic manner.

# 2.3. Structure-based incremental learning method

Structure-based incremental learning (IL) methods alter the network structure by expanding or pruning parameters, providing parameters for new tasks. For instance, when new tasks arrive, Dynamically Expandable Representation (DEN) [39] selectively retrains the old network and dynamically expands its model size if necessary. CPG [18] employs a mechanism that selectively shares weights between model components while alternating between pruning and expanding the architecture. Despite the efficacy of structure-based IL methods, this requirement for task identity (task ID) during inference restricts their applicability.

Several methods for class incremental learning (CIL) have been proposed to overcome the reliance on task ID [23,24]. For example, CCGN [23], incorporates task-specific gating modules into each convolutional layer, and uses task predictors to select a gating module during inference. SpaceNet [25] allocates sparse connections for each task using adaptive training. The literature [25] has also explored modifications to DEN [39] for CIL. Specifically, each task-specific model generates class probability on the test data. The final predicted label for the test data is the class with the highest probability among all models. Recent CIL methods

![](images/4e147ad46465c6588a36ce2be3be8102c771cb71e55f6b586ce122c4bc4c58d7.jpg)  
Fig. 2. The overview framework of our approach.

integrate rehearsal-based and structure-based CIL methods. For example, DER [24] introduces a channel-level mask-based pruning strategy to expand the representation by using partial data from old tasks and new incoming data.

We propose a novel structure-based CIL approach that improves model performance with restricted parameter sizes. Our approach differs from existing structure-based CIL methods in two main aspects.

• Most structure-based CIL methods rely on binary masks to selectively update parameters during training, thus requiring additional storage and computation. In contrast, our approach sequentially assigns parameter connections to each task, which makes implementation simple.   
• Most structure-based CIL methods employ a pruning strategy that discards redundant parameters. However, this can lead to the loss of valuable information from the pruned parameters. In contrast, our approach fuses the intrinsic information among all parameters in each layer during training.

# 3. Method

In this section, we propose a new structure-based non-rehearsal CIL approach, called task-specific parameter decoupling. The proposed approach enhances the model’s capability for CIL under limited model parameters, as illustrated in Fig. 2. We first present the formulation of the CIL problem in Section 3.1. Then, we describe the parameter decoupling framework in Section 3.2 and the dynamic parameter fusion strategy in Section 3.3, respectively.

# 3.1. Problem formulation

In class incremental learning (CIL), a model must learn from a sequence of $T + 1$ tasks {0, 1, 2, ..., ? }, where task 0 is the base task. Let $D _ { t r a i n } ^ { b }$ be the training data corresponding to the ?-th task, containing $N ^ { b }$ image-label pairs $( \mathbf { x } _ { i } ^ { b } , y _ { i } ^ { b } ) . \mathbf { x } _ { i } ^ { b }$ is an instance from class $y _ { i } ^ { b } \in \dot { Y } ^ { b }$ ̃?? , and $Y ^ { b }$ is the label space of the ?-th task, where $Y ^ { b }$ has $c ^ { b }$ classes and $Y ^ { b } \cap Y ^ { s } = \emptyset ( b \neq s )$ ? ? ? . For task $\mathbf { b } ,$ the model learns only ? from $D _ { t r a i n } ^ { b }$ Db while minimizing the forgetting of previous knowledge. After learning each task, the model is evaluated on all classes

# 3.1.1. Problem analysis

Suppose a continuous model ${ \pmb { M } } _ { \Theta } ( \mathbf { x } )$ consists of a feature extractor and a classifier, 𝐱 is the input data and . are the model parameters. The network parameters are $\Theta = \{ \theta , \Phi \}$ , where . represents the parameters of the feature extractor and ℂ are those of the classifier. The network is then implemented as:

$$
\begin{array}{l} \boldsymbol {h} = \boldsymbol {f} _ {\theta} (\mathbf {x}), \\ \boldsymbol {M} _ {\Theta} (\mathbf {x}) = \mathbb {C} _ {\phi} (\boldsymbol {h}) \tag {1} \\ \end{array}
$$

where 𝐱 is input data, $f _ { \theta }$ is the feature extractor of the continuous model with parameters .. ℂ is the classifier. 𝒉 is the feature vector obtained from the feature extractor. $M _ { \Theta } ( \cdot )$ is the output of the model with parameters %.

In non-rehearsal CIL, the model does not access previous data. For training samples $\mathbf { x } ^ { t }$ in task $t ,$ there is a loss function $\mathcal { L } _ { n e w }$ to learn the current task and a regularization term 𝕃 to prevent the forgetting of old tasks.

$$
L = \alpha \mathcal {L} _ {\text {n e w}} \left(\mathbf {x} ^ {t}\right) + \beta \mathbb {L} \left(\mathbf {x} ^ {t}\right), \tag {2}
$$

where 𝛼 and 𝛽 are the coefficients. $\mathcal { L } _ { n e w }$ and 𝕃 update the model parameters % by the gradient.

$$
\frac {\partial L}{\partial \Theta} = \alpha \frac {\partial \mathcal {L} _ {\text {n e w}}}{\partial \Theta} + \beta \frac {\partial \mathbb {L}}{\partial \Theta}. \tag {3}
$$

If an inner product $\begin{array} { r } { \left. \frac { \partial L _ { n e w } } { \partial \Theta } , \frac { \partial \mathbb { L } } { \partial \Theta } \right. < 0 . } \end{array}$ ⟨ 𝜕𝐿?𝑒𝑤 , the gradients $\partial L _ { n e w }$ and 𝕃 in Eq. (3) may conflict with each other [40]. This may require complex operators to optimize the loss 𝐿 in $\mathsf { E q . } \left( 2 \right) \left[ 5 , 4 1 \right]$ .

Parameter Isolation Strategy: To avoid the above problems, structure-based non-rehearsal CIL methods of the unrehearsed class freeze the parameters of previous tasks and expand the network for new tasks. The task-specific parameters for each task will be integrated into % after the training is completed. The entire network can be written as:

$$
\boldsymbol {h} ^ {b} = f _ {\theta^ {b}} ^ {b} (\mathbf {x}),
$$

$$
\boldsymbol {h} = \boldsymbol {h} ^ {1} \oplus \boldsymbol {h} ^ {2} \oplus \dots \boldsymbol {h} ^ {b} \dots \oplus \boldsymbol {h} ^ {t}, \tag {4}
$$

$$
\phi = \left\{\phi^ {1}, \phi^ {2}, \dots , \phi^ {b}, \dots , \phi^ {t} \right\}
$$

$$
\boldsymbol {M} _ {\Theta} (\mathbf {x}) = \mathbb {C} _ {\phi} (\boldsymbol {h})
$$

where 𝐱 is input data and ⊕ represents the concatenation operation. $\theta ^ { b }$ and $\phi ^ { b }$ denote the parameters of the feature extractor and the classifier corresponding to task $^ { b , }$ respectively. ℂ is the classifier with the parameters φ. $\pmb { h } ^ { b }$ represents the feature vector of the ?-th task. Notably, existing structure-based CIL methods for the learning of task-specific parameters generally have two strategies. One strategy involves allocating new components for each incoming task while preserving existing ones. Another strategy (uses) sparse connections and pruning techniques to assign task-specific weights using binary masks. However, these methods involve trade-offs: new components increase the model’s size and complexity, whereas sparse connections incur additional overhead to maintain the network structure with binary masks.

# 3.2. Parameters decoupling framework for class incremental learning

In this study, we design a new structure-based CIL approach to exploit limited parameter sizes and eliminate the potential overhead associated with binary masks. To achieve this, we assign a fixed number of parameters (task-specific parameters) to each network layer for each task in an orderly manner. These task-specific parameters receive only inputs related to their respective tasks. The parameter decoupling (PD) framework pre-allocates task-specific parameters within a continuous model for distinct tasks. During the training stage, we create a compact model for each task by replicating the corresponding parameters of the continuous model. Subsequently, knowledge distillation (KD) [20] techniques are employed to train the compact model for each task. Finally, the compact model parameters for each task are copied back to the corresponding task-specific parameters of the continuous model. In Section 3.2.1, we first present the implementation of the parameter allocation and replication (as shown in Fig. 3). Then, we explain how to train a compact model for each task in Section 3.2.2.

# 3.2.1. Parameter allocation and replication

The PD framework pre-assigns task-specific parameters within a continuous model to different tasks. The task-specific parameters for each task can be trained independently and reintegrated into the continuous model without interfering with other tasks. Let $\Theta = \{ \theta , \Phi \} = \{ \theta _ { 1 } , \theta _ { 2 } , \cdots , \theta _ { l } , \cdots , \theta _ { L } , \Phi \}$ denote the model parameters of the continuous model, where $\theta _ { l }$ represents the parameters of the 𝑙-th convolutional layer and 𝜙 represents the parameters of the classifier. We pre-assign % to $T$ task-specific parameters $\Theta =$ $\{ \Theta ^ { 0 } \cup \Theta ^ { 1 } \cup \dots \cup \Theta ^ { b } \cup \dots \cup \Theta ^ { T } \}$ for ? tasks, where $\Theta ^ { b } = \{ \theta ^ { b } , \Phi ^ { b } \}$ . Then, we build a compact model by copying $\Theta ^ { b }$ from the continuous model for each task ?. After training the compact model for task $^ { b , }$ its parameters can be reintegrated into the corresponding taskspecific parameters of the continuous model. Formally, the parameters of the 𝑙-th layer of the compact model for task ? can be copied back to the corresponding task-specific parameters of the continuous model as follows:

$$
\theta^ {b} = \theta_ {l, r _ {l} ^ {b}: r _ {l} ^ {b} + \bar {c} h _ {l, i n} ^ {b}, r _ {l} ^ {b}: r _ {l} ^ {b} + \bar {c} h _ {l, o u t} ^ {b}} = \bar {\theta} _ {l, 1: \bar {c} h _ {l, i n} ^ {b}, 1: \bar {c} h _ {l, o u t} ^ {b}} ^ {b} \tag {5}
$$

$$
\phi^ {b} = \phi_ {r _ {l} ^ {b}: r _ {l} ^ {b} + \bar {c} h _ {l, i n} ^ {b}, r _ {l} ^ {b}: r _ {l} ^ {b} + \bar {c} h _ {l, o u t} ^ {b}} = \bar {\phi} _ {1: \bar {c} h _ {l, i n} ^ {b}, 1: \bar {c} h _ {l, o u t} ^ {b}} ^ {b},
$$

where $r _ { l } ^ { b }$ denotes the starting index of the task-specific parameters of task ? in layer 𝑙 in the continuous model. $\hat { c h } _ { l , i n } ^ { b }$ and $\hat { c h } _ { l , o u t } ^ { b }$ denote the input and output channels of the compact model for the 𝑙-th layer, respectively. $\bar { \theta } _ { l , 1 : \bar { c h } _ { l , i n } ^ { b } , 1 : \bar { c h } _ { l , o u t } ^ { b } } ^ { b }$ represents the parameters of the .𝑙,1∶ ̄,ℎ? ,1∶ ̄,ℎ? 𝑙-th convolutional layer of the compact model for task $b . ~ \boldsymbol { \Phi } _ { 1 : c \bar { h } _ { l , i n } ^ { b } , 1 : c \bar { h } _ { l , o u t } ^ { b } } ^ { b }$ represents the classifier’s parameters of the compact model for task ?. In this study, the classifier contains only a single fully connected layer. Before replicating the parameters, the task-specific parameters for task ? in the continuous model are initialized to zero. After performing the parameter replication according to Eq. (5), the parameters $\theta _ { l } ^ { b }$ in the 𝑙-th layer of the continuous model will receive only the output features of the corresponding task from layer $l - 1$ .

![](images/b13b96b4ecc6362d7ef941276b4409ca6f96b5505f7d2744fcb506a0ef1481b3.jpg)  
Fig. 3. Illustration of the proposed parameter decoupling framework. 𝒇 ? is the feature extractor of the ?-th task.

# 3.2.2. Training compact models for learning tasks

In this subsection, we describe the training process used to obtain a compact model for each task. We assign a designated number of filters to each task and use these filters to construct compact models corresponding to the respective tasks for independent training. Specifically, we first create a compact model by copying the pre-assigned parameters of the continuous model corresponding to the current task. Then, we train the compact model using a KD strategy.

During training, we first use a cross-entropy loss function to optimize the compact model for each task, ensuring that the model’s output probabilities are consistent with the labels of each training instance. The cross-entropy loss is defined as follows:

$$
\mathcal {L} _ {\mathrm {c e}} \left(\mathbf {x} _ {i} ^ {b}, y _ {i} ^ {b}\right) = \sum_ {k = C ^ {b - 1}} ^ {C ^ {b}} \mathbb {I} \left(k = y _ {i} ^ {b}\right) \log \mathbf {S} _ {k} \left(\bar {\mathbf {M}} _ {t} \left(\mathbf {x} _ {i} ^ {b}\right) / \tau\right), \tag {6}
$$

where 𝕀(⋅) is an indicator function, 𝜏 is the coefficient. $\mathbf { S } _ { k } ( \cdot )$ is the 𝑘-th output of softmax function. $\mathbf { x } _ { i } ^ { b }$ is the ?-th image of the task $b . \ y _ { i } ^ { b }$ is the label of image $\mathbf { x } _ { i } ^ { b } . \mathcal { C } ^ { b }$ is the number of classes for 1 to the task ?. $\bar { \mathbf { M } } ^ { b } ( \mathbf { x } _ { i } ^ { b } )$ is the output vector of the compact model corresponding to task ?.

Insufficient model parameters and poor designs can lead to underfitting when training small models from scratch [42]. To alleviate this issue, we use KD loss to guide a compact model to learn a new task. The distillation loss can transfer knowledge from the teacher model to the student model in which the target is the output probability of the teacher model. Li et al. [19] was the first to incorporate the KD loss into TIL using a training set for the current task. Knowledge loss is commonly used in activation-based methods owing to its effectiveness. Unlike activation-based methods, we do not intend to extend the strategies (activation-based methods). In this study, we only use the KD loss to match the output vector from a larger model (teacher model). The original KD loss [31] is defined as:

$$
\mathcal {L} _ {k d} \left(\mathbf {x} _ {i} ^ {b}\right) = \frac {1}{\mathcal {C} ^ {b} - \mathcal {C} ^ {b - 1}} \sum_ {k = \mathcal {C} ^ {b - 1}} ^ {\mathcal {C} ^ {b}} \left(\tilde {\boldsymbol {M}} _ {k} ^ {b} \left(\mathbf {x} _ {i} ^ {b}\right) - \tilde {\boldsymbol {M}} _ {k} ^ {b} \left(\mathbf {x} _ {i} ^ {b}\right)\right) ^ {2}, \tag {7}
$$

where $\bar { \pmb { M } } ^ { b }$ represents the output vector of the compact model of task $b . \tilde { { \pmb M } } ^ { b } ( \cdot )$ is the output vector of a teacher model, which has the same parameter size as the continuous model. $c ^ { b }$ is the number of classes from 1 to the task ?. The loss in Eq. (7) forces the compact model of task ? to yield the same output probability as that of the teacher model. Consequently, the matched probabilities cause the compact model of the old classes to have the same discriminant ability as the continuous model; thereby, improving the compact model’s learning ability. Thus, the training loss can be written as:

![](images/d82c18b2b11a78ab806333d77baf7a2421e874241f3e430a95866057aa03a4f8.jpg)  
Fig. 4. The illustration of dynamic parameter fusion.

$$
\mathcal {L} \left(\mathbf {x} _ {i} ^ {b}, y _ {i} ^ {b}\right) = \mathcal {L} _ {\mathrm {c e}} \left(\mathbf {x} _ {i} ^ {b}, y _ {i} ^ {b}\right) + \lambda \mathcal {L} _ {k d} \left(\mathbf {x} _ {i} ^ {b}\right), \tag {8}
$$

where 𝜆 is a coefficient. While KD has been shown to transfer knowledge from a larger teacher model to a smaller student model in Section 3.2.2. However, KD may not always result in significant performance improvements, particularly when applied to compact student models [43].

# 3.3. Dynamic parameter fusion strategy

Previous studies have verified that pruning techniques and distillation learning can yield more compact models [44]. Inspired by these findings, we intend to use larger models, such as ResNet, to derive compact models using filter pruning techniques. We present a dynamic parameter fusion (DPF) strategy to improve the learning ability of the task-specific model parameters (see Fig. 4). This strategy monitors the filter importance of the larger model and fuses the information into compact model parameters based on the filter importance in each convolutional layer during training.

We introduce a probability distribution $\mathbf { P } _ { l } = ( p _ { l , 1 } , p _ { l , 2 } , . . . , p _ { l , c h _ { l , o u t } } )$ to measure the relative importance of filters $\mathbf { W } _ { l }$ in the 𝑙-th layer of the continuous model, where $c h _ { l , o u t }$ 𝑙,𝑜<?is the number of filters. The summation of the distribution probability ${ \bf P } _ { l }$ is one, i.e., $\textstyle \sum _ { j = 1 } ^ { c h _ { l , o u t } } p ^ { l , j } = 1$ 𝑗=1 . A high value for $p _ { l , j }$ indicates that the filter $\mathbf { W } _ { l , j }$ has higher importance (called high-score filter) in the model. Conversely, a low value of $p _ { l , j }$ indicates the filter $\mathbf { W } _ { l , j }$ is less representative (called low-score filter). The relative importance of filter $\mathbf { W } _ { l , j } ,$ reflected in $p _ { l , j } ,$ should be dynamically updated as the filter weights $\mathbf { W } _ { l , j }$ change during training. To achieve this, we employ a differentiable fully connected weight $\mathbf { a } _ { l } = ( a _ { l , 1 } , a _ { l , 2 } , . . . , a _ { l , c h _ { l , o u t } } )$ ) to describe ${ \bf { P } } _ { l } \colon$

$$
p _ {l, i} = \frac {e ^ {a _ {l , i}}}{\sum_ {j} e ^ {a _ {l , j}}}, \quad k = 1, 2, \dots , c h _ {l, \text {o u t}}, \tag {9}
$$

where $a _ { l , i } \in \mathbf { a } _ { l }$ . We update the original filter $\mathbf { W } _ { l }$ and the distribution weight via the chain rule of the backpropagation. After network training, we will obtain the distribution probability ${ \bf P } _ { l }$ for filters in each CNN layer.

Unlike most pruning techniques that only retain the high-score filters of a model and discard the low-score ones, we fuse the information from all the filters in the larger model into a compact model. We argue that the low-score filters may also contain valuable information for the model, and directly removing them may degrade the network performance. Hence, our approach applies greater weight to high-score filters while retaining information from low-scoring filters. We first define a set of probability distributions $\{ \mathbf { P } ^ { 1 } , \mathbf { P } ^ { 2 } , \cdots , \mathbf { P } ^ { \tilde { c h } _ { l , o u t } } \}$ } for each CNN layer in the compact model, where each distribution corresponds to a specific filter in the model. Then the compact filters are refined as follows:

$$
\tilde {\mathbf {W}} _ {l, k} = \mathbf {P} _ {l} ^ {k} \cdot \mathbf {W} _ {l}, \quad k = 1, 2, \dots , \tilde {c h} _ {l, o u t}, \tag {10}
$$

where ⋅ denotes the dot product operation. $\mathbf { P } _ { I } ^ { k }$ denotes the distribution probability at the 𝑙-th CNN layer of a larger model, which is used to generate the 𝑘-th filter at the 𝑙-th CNN layer of the compact model. In Eq. (10), each filter $\bar { \mathbf { W } } _ { l }$ of the compact model for each task is a linear weighted average of the filters $\mathbf { W } _ { l }$ and distribution $\mathbf { P } _ { l } ^ { k }$ .

# 3.4. Discussion

Our approach aims to obtain compact task-specific models that can be incrementally combined to recognize learned classes. We applied a parameter decoupling (PD) framework to isolate the parameters for different tasks and prevent interference among tasks. Furthermore, to reduce the size of the task-specific models, we employ knowledge distillation to transfer knowledge from a larger model to a smaller one.

During distillation, the model is replicated and trained to produce outputs that closely match those of the original larger model. By distilling this knowledge, highly compact task-specific models can be obtained. Research has shown that pruning techniques and distillation learning can yield more compact models [44]. The dynamic parameter fusion strategy is proposed to address the challenge of training a compact model. This strategy involves measuring the importance of filters in larger models and assigning a corresponding weight to each convolutional layer during training. As new tasks emerge, our approach could learn robust task-specific models. These task-specific models can be modularly combined.

# 4. Experiments

To verify the effectiveness of our approach., we compare our method with structured-based and activation-based CIL methods.

# 4.1. Experimental setup

Dataset: To evaluate the proposed approach, we conducted experiments on two datasets: CIFAR-100 and TinyImageNet. CIFAR-100 consists of 50,000 images from 100 classes, with 500 training images and 100 test images per class. TinyImageNet contains 100,000 images from 200 classes, with 500 training images and 100 test images per class. We use the validation set as the test set for TinyImageNet because the test labels are not available. We follow the same task division settings as in [45]. For CIFAR-100, we use 50 classes for the initial task and split the remaining classes equally into five or ten incremental tasks (? = 5 and ? = 10). For TinyImageNet, we use half of the classes for the initial task and split the remaining classes equally into five or ten incremental tasks (? = 5 and ? = 10). We applied data augmentation techniques such as AutoAugment [46] and Mixup [47].

Compared methods: To evaluate the effectiveness of our structure-based approach, we compare it to several existing structure-based non-rehearsal CIL methods, such as SpaceNet [25], and CCGN [23]. We also compared our approach to DEN [39], with reference to the modification of DEN for CIL described in the literature [25]. Regularization-based non-rehearsal CIL methods and structure-based non-rehearsal CIL methods have the same objectives, even though they have different principles and implementations. Accordingly, we include some regularization-based non-rehearsal CIL methods in our comparison, such as PASS [45], SSRE [41], and FeTrIL [48]. Although rehearsal CIL methods are widely considered superior in terms of accuracy, we would like to explore whether our approach can achieve similar performance without storing data. To demonstrate the potential of our approach, we compare it to a structure-based rehearsal CIL method, i.e., DER [24]. Meanwhile, to obtain a more comprehensive evaluation, we also compare our approach with some widely used rehearsal CIL methods, such as iCaRL (iCaRL-CNN, iCaRL-NCM) [8], EEIL [49] and UCIR [50]. We use the official code for PASS, SSRE, FeTrIL, and the widely used code for iCaRL-CNN, iCaRL-NCM, EEIL, and UCIR.

Training details: In this study, we use ResNet-18 as the base model for all datasets. We use stochastic gradient descent (SGD) as the optimizer and set its momentum value to 0.9. We initialize the learning rate to 0.1 and use the cosine annealing function to adjust the learning rate during the training process. Each incremental stage consists of 200 epochs with a mini-batch size of 128. For methods with unreleased codes, we report the results based on our implementation.

Evaluation metrics: In this subsection, we introduce two metrics to evaluate the performance of our approach: average accuracy (AA) and average forgetting rate (AF). The average accuracy evaluates the performance in terms of average accuracy for all previously learned tasks. Let $A c c _ { t , i }$ be the accuracy of task ? after learning task ?. The definition of AA is as follows:

$$
\mathbf {A} \mathbf {A} _ {t} = \frac {1}{t} \sum_ {i = 0} ^ {t} A c c _ {t, i}, \tag {11}
$$

where ? represents the number of tasks. However, AA only measures the model performance on the current task. Thus, we also use the average forgetting rate [45] as the evaluation metric.

$$
\mathbf {A} \mathbf {F} _ {t} = \frac {1}{t - 1} \sum_ {j = 0} ^ {t - 1} f _ {t, j}, \tag {12}
$$

where $f _ { t , j }$ denotes the forgetting rate of task 𝑗 after training task $t ,$ i.e., $\begin{array} { r } { f _ { t , j } = \operatorname* { m a x } _ { i \in \{ 0 , \ldots , t - 1 \} } \left( A c c _ { i , j } - A c c _ { t , j } \right) , \forall j < t . } \end{array}$ . The average forgetting rate quantifies the extent to which previously learned knowledge is forgotten when new information is acquired.

# 4.2. Benchmark comparison

Table 1 shows the average accuracy of all stages for all methods on CIFAR-100, TinyImageNet. It can be seen that our approach achieves better performance than the competing methods. On CIFAR-100 (five incremental tasks), our approach outperforms the second-best method (FeTrIl) by 1.04% (67.32% ( 66.28%) in terms of average accuracy. For CIFAR-100 (ten incremental tasks), our approach outperforms the second-best method (FeTrIl) by 0.69% (65.88% ( 65.19%) in terms of average accuracy. On TinyImageNet (five incremental tasks), our approach outperforms the second-best method (FeTrIl) by 0.95% (55.71% ( 54.76%) in terms of average accuracy. For TinyImageNet (ten incremental tasks), our approach outperforms the second-best method (FeTrIl) by 0.38% (53.43% (

Table 1 Comparisons of the average accuracy (%) with other methods on CIFAR-100 and TinyImageNet. ? is the number of incremental tasks, and 𝐸 represents the number of exemplars. Methods with an asterisk ∗ represent the structure-based method.   

<table><tr><td rowspan="2" colspan="2">Methods</td><td colspan="2">CIFAR-100</td><td colspan="2">TinyImageNet</td></tr><tr><td>T=5</td><td>T=10</td><td>T=5</td><td>T=10</td></tr><tr><td rowspan="6">(1) E=20</td><td>iCaRL-CNN</td><td>51.07</td><td>48.66</td><td>34.64</td><td>31.15</td></tr><tr><td>iCaRL-NCM</td><td>58.56</td><td>54.19</td><td>45.86</td><td>43.29</td></tr><tr><td>EEIL</td><td>60.37</td><td>56.05</td><td>47.12</td><td>45.01</td></tr><tr><td>UCIR</td><td>63.78</td><td>62.39</td><td>49.15</td><td>48.52</td></tr><tr><td>CCGN*</td><td>63.90</td><td>61.83</td><td>50.98</td><td>49.01</td></tr><tr><td>DER*</td><td>65.34</td><td>63.32</td><td>51.48</td><td>49.42</td></tr><tr><td rowspan="8">(2) E=0</td><td>LwFMC</td><td>45.93</td><td>27.43</td><td>29.12</td><td>23.10</td></tr><tr><td>MUC</td><td>49.42</td><td>30.19</td><td>32.58</td><td>26.61</td></tr><tr><td>DEN*</td><td>63.01</td><td>61.02</td><td>49.04</td><td>46.78</td></tr><tr><td>SpaceNet*</td><td>62.96</td><td>61.71</td><td>49.90</td><td>46.99</td></tr><tr><td>PASS</td><td>63.47</td><td>61.84</td><td>49.55</td><td>47.29</td></tr><tr><td>SSRE</td><td>65.88</td><td>65.04</td><td>50.39</td><td>48.93</td></tr><tr><td>FeTrIL</td><td>66.28</td><td>65.19</td><td>54.76</td><td>53.05</td></tr><tr><td>Ours</td><td>67.32</td><td>65.88</td><td>55.71</td><td>53.43</td></tr></table>

Table 2 Comparisons of the average forgetting (%) with other methods on CIFAR-100 and TinyImageNet. is the number of incremental tasks. Methods with an asterisk ∗ represent the structure-based method.   

<table><tr><td rowspan="2">Method</td><td colspan="2">CIFAR-100</td><td colspan="2">TinyImageNet</td></tr><tr><td>T=5</td><td>T=10</td><td>T=5</td><td>T=10</td></tr><tr><td>iCaRL-CNN</td><td>42.13</td><td>45.69</td><td>36.89</td><td>36.70</td></tr><tr><td>iCaRL-NCM</td><td>24.90</td><td>28.32</td><td>27.15</td><td>28.89</td></tr><tr><td>EEIL</td><td>23.36</td><td>26.65</td><td>25.56</td><td>25.91</td></tr><tr><td>UCIR</td><td>21.00</td><td>25.12</td><td>20.61</td><td>22.25</td></tr><tr><td>CCGN*</td><td>21.23</td><td>25.96</td><td>20.35</td><td>19.87</td></tr><tr><td>DER*</td><td>19.61</td><td>24.28</td><td>18.72</td><td>19.33</td></tr><tr><td>LwFMC</td><td>44.23</td><td>50.47</td><td>54.26</td><td>54.37</td></tr><tr><td>MUC</td><td>40.28</td><td>47.56</td><td>51.46</td><td>50.21</td></tr><tr><td>DEN*</td><td>22.92</td><td>31.13</td><td>21.06</td><td>24.49</td></tr><tr><td>SpaceNet*</td><td>26.11</td><td>30.37</td><td>17.82</td><td>24.03</td></tr><tr><td>PASS</td><td>25.20</td><td>30.25</td><td>18.04</td><td>23.11</td></tr><tr><td>SSRE</td><td>18.37</td><td>19.48</td><td>9.17</td><td>14.06</td></tr><tr><td>FeTrIL</td><td>18.22</td><td>19.31</td><td>9.21</td><td>13.98</td></tr><tr><td>Ours</td><td>18.05</td><td>19.22</td><td>9.01</td><td>13.85</td></tr></table>

53.05%) in terms of average accuracy. Furthermore, our approach improves the average accuracy of the two task settings by at least 0.87% ((1.04% + 0.69%))2) and 0.67% ((0.95% + 0.38%))2) for CIFAR-100 and TinyImageNet, respectively.

Compared to structure-based methods, our approach improves the average accuracy on CIFAR-100 (five incremental tasks) by at least 1.98% (67.32% ( 65.34%) and on CIFAR-100 (ten incremental tasks) by at least 2.56% (65.88% ( 63.32%). Similarly, our approach achieves at least 4.23% (55.71% ( 51.48%) average accuracy improvement on TinyImageNet (five incremental tasks) and at least 4.01% (53.43% ( 49.42%) average accuracy improvement on TinyImageNet (ten incremental tasks). Overall, our approach outperforms the structure-based methods by at least 2.27% ((1.98% + 2.56%))2) and 4.12% ((4.23% + 4.01%))2) on CIFAR-100 and TinyImageNet, respectively.

Note that FeTrIL and SSRE achieve accuracy performance second only to that of our proposed approach. These methods require complex balancing mechanisms to mitigate catastrophic forgetting and improve the model CIL performance, as all learning tasks share the same feature extractor. In contrast, our approach isolates parameters for each task, resulting in competitive performance compared to activation-based methods, while avoiding sophisticated balance mechanisms between old and new classes. In addition, our approach demonstrates remarkable improvements compared to other structure-based methods. This observation emphasizes the importance of efficient parameter utilization for improving the model.

To better understand the behavior of the different methods, we compare their average forgetting of all phases. As shown in Table 2, our approach achieves lower average forgetting. For the average forgetting rate across five incremental tasks, our approach achieves 0.17% (18.22% ( 18.05%) and 0.16% (9.17% ( 9.01%) reductions on CIFAR100 and TinyImageNet, respectively, compared to the bestcompeting method. For the average forgetting rate across ten incremental tasks, our approach achieves 0.09% (19.31% ( 19.22%) and 0.13% (13.98% ( 13.85%) reductions on CIFAR100 and TinyImageNet, respectively, compared to the best-second method.

![](images/79de997ccfd6104b8d455487f006cd4bae6c42803d408ab2e2122418fb1db5d3.jpg)  
(a) 5 sequential tasks.

![](images/93973f64e038bb3e6ee7948aa0cc13509bc2a92944424e39348da0cda985f29e.jpg)  
(b) 10 sequential tasks.

![](images/17852003847f0c41ac8359cd13d8dd32e971da001dc514b307823e9bae7b1fd9.jpg)  
Fig. 5. Classification accuracy for various incremental/sequential task (5, 10) (%) on CIFAR-100 dataset.   
(a) 5 sequential tasks.

![](images/976f804d3cccfcca45f42de2d1977657306462c14ff61e64cdebdd91c0719871.jpg)  
(b) 10 sequential tasks.   
Fig. 6. Classification accuracy for various incremental/sequential tasks (5, 10) on TinyImageNet dataset.

Experimental results indicate that our approach achieves a lower average forgetting rate than most competing methods, as shown in Table 2. These results support our hypothesis because our approach isolates parameters for each task, thereby avoiding the interference of different tasks during training. We also observe that FeTrIL and SSRE achieve acceptable performance on average forgetting. One reason may be that the two methods preferentially retain the knowledge of previous tasks through complex balancing mechanisms. In contrast, our approach does not require complex balancing mechanisms to achieve competitive results.

# 4.3. Detailed view of accuracy

To better understand the evolution of accuracy for different methods, Fig. 5 and Fig. 6 present the detailed accuracy for different incremental stages to complement the average accuracy. Note that the learning difficulty increases with the number of incremental phases. However, these results indicate that the proposed approach is superior. Our approach outperforms the best-second method (FeTrIL) in most stages, especially in the first few tasks. Note that our approach exhibits a slight performance drop than the other methods (FeTrIL and SSRE) as the number of tasks increases enough, which is a common challenge in CIL methods. Nonetheless, the synthetic results highlight the potential of our approach to overcome the limitations of existing methods.

# 5. Ablation study and analysis

In this section, we perform ablation experiments to understand the impact of the components of our approach on the overall performance. In addition, we compare the basic pruning strategies with our parameter fusion strategy. To evaluate the efficiency of our approach, we compare the calculations of competing methods.

Table 3 Accuracy (%) of each component of our approach on CIFAR-100 and TinyImageNet datasets (10 incremental tasks). Ours denotes our parameter decoupling framework.   

<table><tr><td rowspan="2">Method</td><td colspan="11">Number of incremental tasks</td><td rowspan="2">Average accuracy</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td colspan="13">CIFAR-100</td></tr><tr><td>Baseline</td><td>74.21</td><td>66.65</td><td>63.63</td><td>61.32</td><td>58.77</td><td>56.23</td><td>55.11</td><td>53.56</td><td>52.33</td><td>50.82</td><td>48.10</td><td>58.25</td></tr><tr><td>Ours</td><td>78.36</td><td>72.81</td><td>68.22</td><td>62.35</td><td>60.56</td><td>59.13</td><td>59.10</td><td>58.13</td><td>57.78</td><td>56.13</td><td>53.22</td><td>62.34</td></tr><tr><td>Ours</td><td>81.68</td><td>75.24</td><td>71.87</td><td>70.02</td><td>67.26</td><td>63.53</td><td>62.05</td><td>61.35</td><td>60.16</td><td>57.21</td><td>54.26</td><td>65.88</td></tr><tr><td colspan="13">TinyImageNet</td></tr><tr><td>Baseline</td><td>58.21</td><td>53.13</td><td>46.38</td><td>45.44</td><td>44.77</td><td>43.21</td><td>41.25</td><td>36.89</td><td>35.27</td><td>34.05</td><td>32.56</td><td>42.83</td></tr><tr><td>Ours</td><td>60.23</td><td>54.38</td><td>49.68</td><td>48.77</td><td>47.90</td><td>44.64</td><td>43.28</td><td>39.77</td><td>39.21</td><td>38.66</td><td>38.32</td><td>45.89</td></tr><tr><td>Ours</td><td>64.34</td><td>62.67</td><td>59.93</td><td>57.66</td><td>54.31</td><td>52.57</td><td>49.63</td><td>48.82</td><td>47.92</td><td>45.51</td><td>44.33</td><td>53.43</td></tr></table>

Table 4 Accuracy (%) of each component of our approach on CIFAR-100 and TinyImageNet datasets (5 incremental tasks). Ours denotes our parameter decoupling framework.   

<table><tr><td rowspan="2">Method</td><td colspan="6">Number of incremental tasks</td><td rowspan="2">Average accuracy</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td colspan="8">CIFAR-100</td></tr><tr><td>Baseline</td><td>74.21</td><td>62.71</td><td>62.22</td><td>57.35</td><td>52.16</td><td>44.33</td><td>58.83</td></tr><tr><td>Ours</td><td>78.36</td><td>70.17</td><td>65.01</td><td>60.38</td><td>52.24</td><td>47.15</td><td>62.22</td></tr><tr><td>Ours</td><td>81.38</td><td>73.75</td><td>67.63</td><td>63.65</td><td>59.87</td><td>57.63</td><td>67.32</td></tr><tr><td colspan="8">TinyImageNet</td></tr><tr><td>Baseline</td><td>58.21</td><td>53.32</td><td>46.20</td><td>42.39</td><td>40.21</td><td>36.63</td><td>46.16</td></tr><tr><td>Ours</td><td>60.63</td><td>55.43</td><td>49.15</td><td>44.81</td><td>41.26</td><td>39.77</td><td>48.51</td></tr><tr><td>Ours</td><td>64.34</td><td>62.53</td><td>58.21</td><td>53.71</td><td>49.83</td><td>45.66</td><td>55.71</td></tr></table>

# 5.1. Effectiveness of parameters decoupling framework and parameters fusion strategy

To understand our approach, we evaluated the contribution of each components. We began with the parameter decoupling (PD) framework without distillation loss as the backbone. We gradually incorporated other components, including KD loss and dynamic parameter fusion (DPF). The following are the three variations used in the ablation study:

• Baseline (PD): Our PD framework removes the corresponding distillation loss term $\left( \operatorname { E q . } \left( 7 \right) \right)$ .   
• $\mathrm { O u r s } _ { * }$ (PD+KD): This is a complete PD framework that combines a backbone and a distillation loss term.   
• Ours (PD+KD+DPF): This is our complete approach that combines PD framework with DPF.

We compared these with average accuracy and average forgetting on CIFAR-100 and TinyImageNet datasets. We keep other settings unchanged and present the results in Table 3 and Table 4. The results of the Baseline and $\mathrm { O u r } _ { \star }$ show that combining KD loss can improve the performance of the model in terms of average accuracy. The reason can be attributed to the KD loss enhancing the performance of the compact models, and parameter isolation reduces the representation interference among models corresponding to different tasks. Furthermore, the results of ${ \mathrm { O u r } } _ { \star }$ and Ours demonstrate that DPF benefits our PD framework, leading to better performance in CIL. These results imply that we effectively combine and compress the information of all parameters, thereby improving the model’s performance in CIL.

# 5.2. Effect of the different parameter pruning strategies

In this subsection, we compare the performance of elementary filter pruning with that of the improved filter pruning on CIFAR-100 and TinyImageNet. We construct the following experiments.

• Ours♣ (KDCE+PD): Our CIL approach with a PD framework and without a pruning strategy.   
• DuP: Another pruning strategy equips our PD framework by discarding unimportant parameters.   
• Ours (KDCE+PD+DPF): Our approach combines a PD framework and a DPF strategy.

Note that the difference between DuP and Ours is how to prune parameters.

Table 5, Figs. 7 and 8 illustrate the results of the parameter pruning, where ? is the number of incremental tasks. Compared to the elementary parameter pruning, the improved filter pruning (DPF) can improve the continuous model performance for $T = 5$ and $T = 1 0$ on CIFAR-100. The experiments indicate that the DPF strategy is more effective in maintaining and improving the model’s performance on CIL. Although the accuracy of Ours is similar to that of the DuP in most stages for $T = 1 0$ on CIFAR-100, Ours still has the advantage of comprehensive performance in terms of the average accuracy and average forgetting rate for all tasks. This can

Table 5 Ablation study on CIFAR-100 and TinyImageNet (Average forgetting rate (%)). ? is the number of incremental tasks.   

<table><tr><td rowspan="2">Method</td><td colspan="2">CIFAR-100</td><td colspan="2">TinyImageNet</td></tr><tr><td>T=5</td><td>T=10</td><td>T=5</td><td>T=10</td></tr><tr><td>Baseline</td><td>43.23</td><td>25.12</td><td>28.23</td><td>21.66</td></tr><tr><td>Ours</td><td>29.13</td><td>23.79</td><td>26.90</td><td>19.72</td></tr><tr><td>DuP</td><td>21.51</td><td>21.32</td><td>12.29</td><td>16.73</td></tr><tr><td>Ours</td><td>18.05</td><td>19.22</td><td>9.01</td><td>13.85</td></tr></table>

![](images/4439cddf5fb094b92c8246852c729d0f7d3b1b5d74b3cf13a74141e8dbfcaf91.jpg)  
(a)5 sequential tasks.

![](images/52d5039e10895b69b8d3b5f512dff23ebb9b950074a7e547efbdc36ae737eb8e.jpg)  
(b) 10 sequential tasks.

![](images/ec2d769d8cf132acf483dd6827e7a63a068625deccd1c3d1cade2b6a47dc168c.jpg)  
Fig. 7. Classification accuracy (%) of different parameter pruning strategies on CIFAR-100 dataset (5 and 10 incremental/sequential tasks).   
(a) 5 sequential tasks.

![](images/649a26c72a00d713955c4e57190c913cac0c0a32c27db7d78a57d7c613cfb328.jpg)  
(b) 10 sequential tasks.   
Fig. 8. Classification accuracy (%) of different parameter pruning strategies on TinyImageNet dataset (5 and 10 incremental/sequential tasks).

be because that the parameter fusion strategy makes the model more robust by exploiting the intrinsic relationship between all the parameters of each layer and fusing them. In conclusion, the experimental results demonstrate the potential of our parameter fusion strategy for addressing the limitations of other methods.

Table 6 Comparison of parameters and calculations.   

<table><tr><td></td><td>PASS</td><td>SSRE</td><td>FeTrIL</td><td>DEN</td><td>SpaceNet</td><td>CCGN</td><td>DER</td><td>Ours</td></tr><tr><td>Params(M)</td><td>11.374</td><td>11.215</td><td>11.216</td><td>22.683</td><td>11.173</td><td>11.175</td><td>56.151</td><td>11.169</td></tr><tr><td>MACs(M)</td><td>558.080</td><td>555.469</td><td>557.926</td><td>699.717</td><td>557.881</td><td>558.963</td><td>2789.683</td><td>557.875</td></tr></table>

# 5.3. Comparison of parameters and computation

In this section, we compare the parameters and computations of structure-based and activation-based CIL methods (see Table 6). After learning ten tasks, the results were obtained using the PyTorch-OpCounter (THOP) tool of the ResNet-18 network architecture used on the CIFAR-100 dataset. Note that our approach has fewer parameters than the other structure-based methods (DEN, CCGN, and DER). Although the structure-based approach SpaceNet has similar parameters and computations to our approach, ours approach simplifies implementation by eliminating the need for masks during training. Unlike activation-based methods that share a feature extractor across tasks, our approach isolates the parameters for each incremental task. Nonetheless, the results show little difference in parameters between our approach and representative activation-based methods (PASS, SSRE, FeTrIL). A reason can be attributed to the excellent parameter utilization in our approach. We conclude that the performance of our approach was improved not by incorporating more parameters but by designing compact models for each task.

# 6. Conclusion

In this study, we presented a new structure-based approach for non-rehearsal CIL, called task-specific parameter decoupling. The proposed approach includes a parameter decoupling (PD) framework and a dynamic parameter fusion (DPF) strategy. Under the PD framework, the knowledge of each task is compressed into a compact number of task-specific model parameters, which can eliminate the feature overlap of these tasks. In addition, the DPF strategy exploits the intrinsic relationships among all parameters within each layer, rather than discarding redundant parameter units during incremental training, thereby promoting parameter utilization. Compared with the state-of-the-art method (FeTrIL), the experimental results on representative datasets (CIFAR-100 and TinyImageNet) show the effectiveness of our approach, with average accuracy improvements of 0.87% and 0.67%, respectively. Compared to structure-based methods, our approach achieves at least 2.27% and 4.12% average accuracy improvements on CIFAR-100 and TinyImageNet, respectively.

However, our approach has some limitations that should be addressed in future studies. One limitation is the necessity of extending the continuous model when it lacks alternate filters for subsequent tasks. Another limitation is the reliance on tracking the filter importance in the DPF strategy, which might not accurately capture the importance scores of additional filters. Future studies should investigate alternative parameter separation methods or non-linear fusion strategies to address these limitations. In addition, our approach primarily assesses specific learning scenarios and domains. Future research on CIL should explore other learning environments and cross-domain learning.

# CRediT authorship contribution statement

Runhang Chen: Conceptualization, Methodology, Software, Visualization, Writing – original draft. Xiao-Yuan Jing: Funding acquisition, Investigation, Supervision. Fei Wu: Writing – review & editing. Wei Zheng: Writing – review & editing. Yaru Hao: Validation.

# Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

# Data availability

Data will be made available on request.

# Acknowledgements

This work was supported by the NSFC Project under Grant (No. 62176069 and 61933013), the Natural Science Foundation of Guangdong Province under Grant No. 2023A1515012653, the Innovation Group of Guangdong Education Department under Grant No. 2020KCXTD014, and the 2019 Key Discipline project of Guangdong Province.

# References

[1] Z. Cui, X. Sun, L. Pan, S. Liu, G. Xu, Event-based incremental recommendation via factors mixed Hawkes process, Inf. Sci. 639 (2023) 119007.

[2] D.F. Leite, I. Skrjanc, S. Blazic, A. Zdesar, F.A.C. Gomide, Interval incremental learning of interval data streams and application to vehicle tracking, Inf. Sci. 630 (2023) 1–22.   
[3] R. Ranjbarzadeh, S. Dorosti, S. Jafarzadeh Ghoushchi, A. Caputo, E.B. Tirkolaee, S.S. Ali, Z. Arshadi, M. Bendechache, Breast tumor localization and segmentation using machine learning techniques: overview of datasets, findings, and methods, Comput. Biol. Med. (2023) 106443.   
[4] R. Ranjbarzadeh, A. Caputo, E.B. Tirkolaee, S. Jafarzadeh Ghoushchi, M. Bendechache, Brain tumor segmentation of mri images: a comprehensive review on the application of artificial intelligence tools, Comput. Biol. Med. 152 (2023) 106405.   
[5] M. Masana, X. Liu, B. Twardowski, M. Menta, A.D. Bagdanov, J. van de Weijer, Class-incremental learning: survey and performance evaluation on image classification, IEEE Trans. Pattern Anal. Mach. Intell. 45 (5) (2023) 5513–5533.   
[6] I.J. Goodfellow, M. Mirza, X. Da, A.C. Courville, Y. Bengio, An empirical investigation of catastrophic forgetting in gradient-based neural networks, in: ICLR, 2014, pp. 1–9.   
[7] Z. Mai, R. Li, J. Jeong, D. Quispe, H. Kim, S. Sanner, Online continual learning in image classification: an empirical survey, Neurocomputing 469 (2022) 28–51.   
[8] S. Rebuffi, A. Kolesnikov, G. Sperl, C.H. Lampert, Icarl: incremental classifier and representation learning, in: CVPR, 2017, pp. 5533–5542.   
[9] M. De Lange, R. Aljundi, M. Masana, S. Parisot, X. Jia, A. Leonardis, G. Slabaugh, T. Tuytelaars, A continual learning survey: defying forgetting in classification tasks, IEEE Trans. Pattern Anal. Mach. Intell. 44 (7) (2022) 3366–3385.   
[10] J. Bang, H. Kim, Y. Yoo, J.-W. Ha, J. Choi, Rainbow memory: continual learning with a memory of diverse samples, in: CVPR, 2021, pp. 8218–8227.   
[11] H. Ahn, J. Kwak, S. Lim, H. Bang, H. Kim, T. Moon, Ss-il: separated softmax for incremental learning, in: ICCV, 2021, pp. 844–853.   
[12] J. Kirkpatrick, R. Pascanu, N. Rabinowitz, J. Veness, G. Desjardins, A.A. Rusu, K. Milan, J. Quan, T. Ramalho, A. Grabska-Barwinska, et al., Overcoming catastrophic forgetting in neural networks, Proc. Natl. Acad. Sci. 114 (13) (2017) 3521–3526.   
[13] J. Jiang, O. Çeliktutan, Neural weight search for scalable task incremental learning, in: WACV, 2023, pp. 1390–1399.   
[14] G.M. van de Ven, T. Tuytelaars, A.S. Tolias, Three types of incremental learning, Nat. Mach. Intell. 4 (12) (2022) 1185–1197.   
[15] P. Dhar, R.V. Singh, K. Peng, Z. Wu, R. Chellappa, Learning without memorizing, in: CVPR, 2019, pp. 5138–5146.   
[16] Y. Wu, Y. Chen, L. Wang, Y. Ye, Z. Liu, Y. Guo, Y. Fu, Large scale incremental learning, in: CVPR, 2019, pp. 374–382.   
[17] Y. Liu, Y. Su, A. Liu, B. Schiele, Q. Sun, Mnemonics training: multi-class incremental learning without forgetting, in: CVPR, 2020, pp. 12242–12251.   
[18] S.C.Y. Hung, C. Tu, C. Wu, C. Chen, Y. Chan, C. Chen, Compacting, picking and growing for unforgetting continual learning, in: NeurIPS, 2019, pp. 13647–13657.   
[19] Z. Li, D. Hoiem, Learning without forgetting, IEEE Trans. Pattern Anal. Mach. Intell. 40 (12) (2018) 2935–2947.   
[20] G.E. Hinton, O. Vinyals, J. Dean, Distilling the knowledge in a neural network, arXiv preprint arXiv:1503.02531.   
[21] X. Zhao, H. Li, X. Shen, X. Liang, Y. Wu, A modulation module for multi-task learning with applications in image retrieval, in: ECCV, 2018, pp. 415–432.   
[22] M. Riemer, I. Cases, R. Ajemian, M. Liu, I. Rish, Y. Tu, G. Tesauro, Learning to learn without forgetting by maximizing transfer and minimizing interference, in: ICLR, 2019, pp. 1–31.   
[23] D. Abati, J. Tomczak, T. Blankevoort, S. Calderara, R. Cucchiara, B.E. Bejnordi, Conditional channel gated networks for task-aware continual learning, in: CVPR, 2020, pp. 3930–3939.   
[24] S. Yan, J. Xie, X. Der He, Dynamically expandable representation for class incremental learning, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2021, pp. 3014–3023.   
[25] G. Sokar, D.C. Mocanu, M. Pechenizkiy, Spacenet: make free space for continual learning, Neurocomputing 439 (2021) 1–11.   
[26] R. Humble, M. Shen, J.A. Latorre, E. Darve, J.M. Alvarez, Soft masking for cost-constrained channel pruning, in: ECCV, 2022, pp. 641–657.   
[27] Y. He, G. Kang, X. Dong, Y. Fu, Y. Yang, Soft filter pruning for accelerating deep convolutional neural networks, in: IJCAI, 2018, pp. 2234–2240.   
[28] Y. Xiang, Y. Fu, P. Ji, H. Huang, Incremental learning using conditional adversarial networks, in: ICCV, 2019, pp. 6618–6627.   
[29] F. Zenke, B. Poole, S. Ganguli, Continual learning through synaptic intelligence, in: ICML, 2017, pp. 3987–3995.   
[30] Y. Liu, S. Parisot, G.G. Slabaugh, X. Jia, A. Leonardis, T. Tuytelaars, More classifiers, less forgetting: a generic multi-classifier paradigm for incremental learning, in: ECCV, vol. 12371, 2020, pp. 699–716.   
[31] J. Ba, R. Caruana, Do deep nets really need to be deep?, in: NeurIPS, 2014, pp. 2654–2662.   
[32] Z. Shen, E.P. Xing, A fast knowledge distillation framework for visual recognition, in: ECCV, 2022, pp. 673–690.   
[33] J. Liang, L. Li, Z. Bing, B. Zhao, Y. Tang, B. Lin, H. Fan, Efficient one pass self-distillation with Zipf’s label smoothing, in: ECCV, 2022, pp. 104–119.   
[34] Y. Guo, A. Yao, Y. Chen, Dynamic network surgery for efficient dnns, in: NeurIP, 2016, pp. 1379–1387.   
[35] D. Kim, M. Kim, H. Shim, J. Lee, Your lottery ticket is damaged: towards all-alive pruning for extremely sparse networks, Inf. Sci. 634 (2023) 608–620.   
[36] Y. He, X. Zhang, J. Sun, Channel pruning for accelerating very deep neural networks, in: ICCV, 2017, pp. 1398–1406.   
[37] Z. You, K. Yan, J. Ye, M. Ma, P. Wang, Gate decorator: global filter pruning method for accelerating deep convolutional neural networks, in: NeurIPS, 2019, pp. 2130–2141.   
[38] Y. Li, K. Adamczewski, W. Li, S. Gu, R. Timofte, L. Van Gool, Revisiting random channel pruning for neural network compression, in: CVPR, 2022, pp. 191–201.   
[39] J. Yoon, E. Yang, J. Lee, S.J. Hwang, Lifelong learning with dynamically expandable networks, in: ICLR, 2018, pp. 1–11.   
[40] B. Liu, X. Liu, X. Jin, P. Stone, Q. Liu, Conflict-averse gradient descent for multi-task learning, in: NeurIPS, 2021, pp. 18878–18890.   
[41] K. Zhu, W. Zhai, Y. Cao, J. Luo, Z. Zha, Self-sustaining representation expansion for non-exemplar class-incremental learning, in: CVPR, IEEE, 2022, pp. 9286–9295.   
[42] H. Cai, C. Gan, J. Lin, S. Han, Network augmentation for tiny deep learning, arXiv preprint arXiv:2110.08890.   
[43] N. Aghli, E. Ribeiro, Combining weight pruning and knowledge distillation for CNN compression, in: CVPR, 2021, pp. 3191–3198.   
[44] H. Wang, J. Liu, X. Ma, Y. Yong, Z. Chai, J. Wu, Compressing models with few samples: mimicking then replacing, in: CVPR, 2022, pp. 691–700.   
[45] F. Zhu, X. Zhang, C. Wang, F. Yin, C. Liu, Prototype augmentation and self-supervision for incremental learning, in: CVPR, 2021, pp. 5871–5880.   
[46] E.D. Cubuk, B. Zoph, D. Mané, V. Vasudevan, Q.V. Le, Autoaugment: learning augmentation strategies from data, in: CVPR, 2019, pp. 113–123.   
[47] H. Zhang, M. Cissé, Y.N. Dauphin, D. Lopez-Paz, mixup: beyond empirical risk minimization, in: ICLR, 2018, pp. 1–13.   
[48] G. Petit, A. Popescu, H. Schindler, D. Picard, B. Delezoide, Fetril: feature translation for exemplar-free class-incremental learning, in: WACV, 2023, pp. 3900–3909.   
[49] F.M. Castro, M.J. Marín-Jiménez, N. Guil, C. Schmid, K. Alahari, End-to-end incremental learning, in: ECCV, vol. 11216, 2018, pp. 241–257.   
[50] S. Hou, X. Pan, C.C. Loy, Z. Wang, D. Lin, Learning a unified classifier incrementally via rebalancing, in: CVPR, 2019, pp. 831–839.