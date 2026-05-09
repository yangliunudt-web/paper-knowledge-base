---
title: "Unsupervised Domain Adaptation by Backpropagation"
authors:
  - "Yaroslav Ganin"
  - "Victor Lempitsky"
date: "2015-07-06"
year: "2015"
journal: "ICML"
doi: "arXiv:1409.7495"
abstract: "Top-performing deep architectures are trained on massive amounts of labeled data. In the absence of labeled data for a certain task, domain adaptation often provides an attractive option given that labeled data of similar nature but from a different domain (e.g. synthetic images) are available. Here, we propose a new approach to domain adaptation in deep architectures that can be trained on large amount of labeled data from the source domain and large amount of unlabeled data from the target domain (no labeled target-domain data is necessary). As the training progresses, the approach promotes the emergence of “deep” features that are (i) discriminative for the main learning task on the source domain and (ii) invariant with respect to the shift between the domains. We show that this adaptation behaviour can be achieved in almost any feed-forward model by augmenting it with few standard layers and a simple new gradient reversal layer. The resulting augmented architecture can be trained using standard backpropagation. Overall the whole approach can be implemented with little effort using any of the deep-learning packages."
abstract_cn: "顶级深度架构需要大量标注数据训练。当特定任务缺乏标注数据时，域适应提供了一种有吸引力的选择，前提是可获得类似性质但来自不同域的标注数据（如合成图像）。本文提出一种新的深度架构域适应方法，可在源域大量标注数据和目标域大量无标注数据上训练（不需要目标域标注数据）。随着训练进行，该方法促进出现既对源域主学习任务具有判别性又对域间偏移具有不变性的深度特征。通过增加少量标准层和一个简单的梯度反转层，这种适应行为几乎可以在任何前馈模型中实现，增强后的架构可用标准反向传播训练。"
keywords:
  - "[[Domain adaptation]]"
  - "[[Deep learning]]"
  - "[[Adversarial learning]]"
  - "[[Gradient reversal]]"
cite: "[1] Ganin Y, Lempitsky V. Unsupervised Domain Adaptation by Backpropagation[C]. ICML, 2015."
aiSum: "提出 DANN 域对抗神经网络，通过梯度反转层实现域不变特征学习，在 MNIST→SVHN 等域适应任务上取得优异性能，开创深度域适应领域。"
confidence: "medium"
wiki_concepts:
  - "[[Neural network]]"
---

Yaroslav Ganin

Victor Lempitsky

Skolkovo Institute of Science and Technology (Skoltech)

{ganin,lempitsky}@skoltech.ru

# Abstract

Top-performing deep architectures are trained on massive amounts of labeled data. In the absence of labeled data for a certain task, domain adaptation often provides an attractive option given that labeled data of similar nature but from a different domain (e.g. synthetic images) are available. Here, we propose a new approach to domain adaptation in deep architectures that can be trained on large amount of labeled data from the source domain and large amount of unlabeled data from the target domain (no labeled target-domain data is necessary).

As the training progresses, the approach promotes the emergence of “deep” features that are (i) discriminative for the main learning task on the source domain and (ii) invariant with respect to the shift between the domains. We show that this adaptation behaviour can be achieved in almost any feed-forward model by augmenting it with few standard layers and a simple new gradient reversal layer. The resulting augmented architecture can be trained using standard backpropagation. Overall the whole approach can be implemented with little effort using any of the deep-learning packages.

# 1. Introduction

Deep feed-forward architectures have brought impressive advances to the state-of-the-art across a wide variety tasks within computer vision and beyond. At the moment, however, these leaps in performance emerge only when a large amount of labeled training data is available. At the same time, for problems lacking labeled data, it may be still possible to obtain training sets that are big enough for training large-scale deep models, but that suffer from the shift in data distribution from the actual data encountered at “test time”. One particularly important example is synthetic or semi-synthetic imagery, which may come in abundance and fully labeled, but which inevitably look different from real data [13, 20, 23, 21].

Learning a discriminative classifier or other predictor in

the presence of a shift between training and testing distributions is known as domain adaptation (DA). A number of approaches to domain adaptation has been suggested in the context of shallow learning, e.g. in the situation when data representation/features are given and fixed. The proposed approaches then build the mappings between the source (training-time) and the target (test-time) domains, so that the classifier learned for the source domain can also be applied to the target domain, when composed with the learned mapping between domains. The appeal of the domain adaptation approaches is the ability to learn a mapping between domains in the situation when the target domain data are either fully unlabeled (unsupervised domain annotation) or have few labeled samples (semi-supervised domain adaptation). Below, we focus on the harder unsupervised case, although the proposed approach can be generalized to the semi-supervised case rather straightforwardly.

Unlike most papers previous papers on domain adaptation that worked with fixed feature representations, we focus on combining domain adaptation and deep feature learning within one training process (deep domain adaptation). Our goal is to embed domain adaptation into the process of learning representation, so that the final classification decisions are made based on features that are both discriminative and invariant to the change of domains, i.e. have the same or very similar distributions in the source and the target domains. In this way, the obtained feed-forward network can be applicable to the target domain without being hindered by the shift between the two domains.

We thus focus on learning features that combine (i) discriminativeness and (ii) domain-invariance. This is achieved by jointly optimizing the underlying features as well as two discriminative classifiers operating on these features: (i) the label predictor that predicts class labels and is used at test time and (ii) the domain classifier that discriminates between the source and the target domains during training. While the parameters of the classifiers are optimized in order to minimize their error on the training set, the parameters of the underlying deep feature mapping are optimized in order to minimize the loss of the label classifier and to maximize the loss of the domain classifier. The

latter encourages domain-invariant features to emerge in the course of the optimization.

Crucially, we show that all three training processes can be embedded into an appropriately composed deep feedforward network (Figure 1) that uses standard layers and loss functions, and can be trained using standard backpropagation algorithms based on stochastic gradient descent or its modifications (e.g. momentum). Our approach is generic as it can be used to add domain adaptation to any existing feed-forward architecture that is trainable by backpropagation. In practice, the only non-standard component of the proposed architecture is a rather trivial gradient reversal layer that leaves the input unchanged during forward propagation and reverses the gradient by multiplying it by a negative scalar during the backpropagation.

Below, we detail the proposed approach to domain adaptation in deep architectures, and present prelimenary results on traditional deep learning datasets (such as MNIST [12] and SVHN [14]) that clearly demonstrate the unsupervised domain adaptation ability of the proposed method.

# 2. Related work

A large number of domain adaptation methods have been proposed over the recent years, and here we focus on the most related ones. Multiple methods perform unsupervised domain adaptation by matching the feature distributions in the source and the target domains. Some approaches perform this by reweighing or selecting samples from the source domain [3, 11, 7], while others seek an explicit feature space transformation that would map source distribution into the target ones [16, 10, 2]. An important aspect of the distribution matching approach is the way the (dis)similarity between distributions is measured. Here, one popular choice is matching the distribution means in the kernel-reproducing Hilbert space [3, 11], whereas [8, 5] map the principal axes associated with each of the distributions. Our approach also attempts to match feature space distributions, however this is accomplished by modifying the feature representation itself rather than by reweighing or geometric transformation. Also, our method uses (implicitly) a rather different way to measure the disparity between distributions based on their separability by a deep discriminatively-trained classifier.

Several approaches perform gradual transition from the source to the target domain [10, 8] by a gradual change of the training distribution. Among these methods, [17] does this in a “deep” way by the layerwise training of a sequence of deep autoencoders, while gradually replacing source-domain samples with target-domain samples. This improves over a similar approach of [6] that simply trains a single deep autoencoder for both domains. In both approaches, the actual classifier/predictor is learned in a separate step using the feature representation learned by au-

toencoder(s). In contrast to [6, 17], our approach performs feature learning, domain adaptation and classifier learning jointly, in a unified architecture, and using a single learning algorithm (backpropagation). We therefore argue that our approach is much simpler (both conceptually and in terms of its implementation).

While the above approaches perform unsupervised domain adaptation, there are approaches that perform supervised domain adaptation by exploiting labeled data from the target domain. In the context of deep feed-forward architectures, such data can be used to “fine-tune” the network trained on the source domain [24, 15, 1]. Our approach does not require labeled target-domain data. At the same time, it can easily incorporate such data when they are available.

The work that is most related to ours is the recent (and concurrent) technical report [9] on adversarial networks. While their goal is quite different (building generative deep networks that can synthesize samples), the way they measure and minimize the discrepancy between the distribution of the training data and the distribution of the synthesized data is very similar to the way our architecture measures and minimizes the discrepancy between feature distributions for the two domains.

# 3. Deep Domain Adaptation

# 3.1. The model

We now detail the proposed model for the domain adaptation. We assume that the model works with input samples $\mathbf { x } \in X$ , where X is some input space (e.g. images of a certain size) and certain labels (output) y from the label space Y . Below, we assume classification problems where $Y$ is a finite set $( Y = \{ 1 , 2 , \dots L \} ,$ ), however our approach is generic and can handle any output label space that other deep feed-forward models can handle. We further assume that there exist two distributions $ { \boldsymbol { S } } (  { \boldsymbol { { x } } } ,  { \boldsymbol { y } } )$ and $\tau ( x , y )$ on $X \otimes Y ,$ , which will be referred to as the source distribution and the target distribution (or the source domain and the target domain). Both distributions are assumed complex and unknown, and furthermore similar but different (in other words, S is “shifted” from T by some domain shift).

Our ultimate goal is to be able to predict labels y given the input x for the target distribution. At training time, we have an access to a large set of training samples $\left\{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { N } \right\}$ from both the source and the target domains distributed according to the marginal distributions $\scriptstyle { S ( \mathbf { x } ) }$ and $\tau ( \mathbf { x } )$ . We denote with $d _ { i }$ the binary variable (domain label) for the ith example, which indicates whether $x _ { i }$ come from the source distribution $( \mathbf { x } _ { i } { \sim } { \mathcal { S } } ( \mathbf { x } )$ if $d _ { i } { = } 0 )$ or from the target distribution $( \mathbf { x } _ { i } \sim T ( \mathbf { x } )$ if $d _ { i } { = } 1 )$ . For the examples from the source distribution $( d _ { i } { = } 0 )$ the corresponding labels $y _ { i } \in Y$ are known at training time. For the examples from the target domains, we do not know the labels

![](images/960eb08511afbbe90c395ab615dcefc5cd862459991beeb2b195c1e9f68255bc.jpg)  
Figure 1. The proposed architecture includes a deep feature extractor (green) and a deep label predictor (blue), which together form a standard feed-forward architecture. Unsupervised domain adaptation is achieved by adding a domain classifier (red) connected to the feature extractor via a gradient reversal layer that multiplies the gradient by a certain negative constant during the backpropagation-based training. Otherwise, the training proceeds in a standard way and minimizes the label prediction loss (for source examples) and the domain classification loss (for all samples). Gradient reversal ensures that the feature distributions over the two domains are made similar (as indistinguishable as possible for the domain classifier), thus resulting in the domain-invariant features.

at training time, and we want to predict such labels at test time.

We now define a deep feed-forward architecture that for each input x predicts its label $y \in Y$ and its domain label $d \in \{ 0 , 1 \}$ }. We decompose such mapping into three parts. We assume that the input x is first mapped by a mapping $G _ { f }$ (a feature extractor) to a D-dimensional feature vector $\textbf { f } \in \mathbb { R } ^ { D }$ . The feature mapping may also include several feed-forward layers and we denote the vector of parameters of all layers in this mapping as $\theta _ { f }$ , i.e. $\mathbf { f } = G _ { f } ( \mathbf { x } ; \theta _ { f } )$ . Then, the feature vector f is mapped by a mapping $G _ { y }$ (label predictor) to the label $y ,$ and we denote the parameters of this mapping with $\theta _ { y }$ . Finally, the same feature vector f is mapped to the domain label d by a mapping $G _ { d }$ (domain classifier) with the parameters $\theta _ { d }$ (Figure 1).

During the learning stage, we aim to minimize the label prediction loss on the annotated part (i.e. the source part) of the training set, and the parameters of both the feature extractor and the label predictor are thus optimized in order to minimize the empirical loss for the source domain samples. This ensures the discriminativeness of the features f and the overall good prediction performance of the combination of the feature extractor and the label predictor on the source domain.

At the same time, we want to make the features f domain-invariant. That is, we want to make the distributions $\begin{array} { r } { { \cal S } ( { \bf f } ) ~ = ~ \{ G _ { f } ( { \bf x } ; \theta _ { f } ) | { \bf x } { \sim } { \cal S } ( { \bf x } ) \} } \end{array}$ and $T ( \mathbf { f } ) \ =$ $\{ G _ { f } ( \mathbf { x } ; \theta _ { f } ) | \mathbf { x } { \sim } T ( \mathbf { x } ) \}$ to be similar. Under the covariate shift assumption, this would make the label prediction ac-

curacy on the target domain to be the same as on the source domain [18]. Measuring the dissimilarity of the distributions S(f ) and $T ( \mathbf { f } )$ is however non-trivial, given that f is high-dimensional, and that the distributions themselves are constantly changing as learning progresses. One way to estimate the dissimilarity is to look at the loss of the domain classifier $G _ { d } ,$ provided that the parameters $\theta _ { d }$ of the domain classifier have been trained to discriminate between the two feature distributions in an optimal way.

This leads us to our idea. At training time, in order to obtain domain-invariant features, we seek the parameters $\theta _ { f }$ of the feature mapping that maximize the loss of the domain classifier (by making the two feature distributions as similar as possible), while simultaneously seeking the parameters $\theta _ { d }$ of the domain classifier that minimize the loss of the domain classifier. In addition, we seek to minimize the loss of the label predictor.

More formally, we consider the functional:

$$
\begin{array}{l} E(\theta_{f},\theta_{y},\theta_{d}) = \sum_{\substack{i = 1..N\\ d_{i} = 0}}L_{y}\left(G_{y}(G_{f}(\mathbf{x}_{i};\theta_{f});\theta_{y}),y_{i}\right) - \\ \lambda \sum_ {i = 1.. N} L _ {d} \left(G _ {d} \left(G _ {f} \left(\mathbf {x} _ {i}; \theta_ {f}\right); \theta_ {d}\right), y _ {i}\right) = \\ = \sum_ {\substack {i = 1.. N \\ d _ {i} = 0}} L _ {y} ^ {i} \left(\theta_ {f}, \theta_ {y}\right) - \lambda \sum_ {i = 1.. N} L _ {d} ^ {i} \left(\theta_ {f}, \theta_ {d}\right) \tag{1} \\ \end{array}
$$

Here, $L _ { y } ( \cdot , \cdot )$ is the loss for label prediction (e.g. multinomial), $L _ { d } ( \cdot , \cdot )$ is the loss for the domain classification (e.g.

logistic), while $L _ { y } ^ { i }$ and $L _ { d } ^ { i }$ denote the corresponding loss functions evaluated at the ith training example.

Based on our idea, we are seeking the parameters $\hat { \theta } _ { f } , \hat { \theta } _ { y } , \hat { \theta } _ { d }$ that deliver a saddle point of the functional (1):

$$
\left(\hat {\theta} _ {f}, \hat {\theta} _ {y}\right) = \arg \min  _ {\theta_ {f}, \theta_ {y}} E \left(\theta_ {f}, \theta_ {y}, \hat {\theta} _ {d}\right) \tag {2}
$$

$$
\hat {\theta} _ {d} = \arg \max  _ {\theta_ {d}} E \left(\hat {\theta} _ {f}, \hat {\theta} _ {y}, \theta_ {d}\right). \tag {3}
$$

At the saddle point, the parameters $\theta _ { d }$ of the domain classifier $\theta _ { d }$ minimize the domain classification loss (since it enters into (1) with the minus sign) while the parameters $\theta _ { y }$ of the label predictor minimize the label prediction loss. The feature mapping parameters $\theta _ { f }$ minimize the label prediction loss (i.e. the features are discriminative), while maximizing the domain classification loss (i.e. the features are domain-invariant). The parameter λ controls the trade-off between the two objectives that shape the features during learning.

Below, we demonstrate that standard stochastic gradient solvers (SGD) can be adapted for the search of the saddle point (2)-(3).

# 3.2. Optimization with backpropagation

A saddle point (2)-(3) can be found as a stationary point of the following stochastic updates:

$$
\theta_ {f} \quad \leftarrow \quad \theta_ {f} - \mu \left(\frac {\partial L _ {y} ^ {i}}{\partial \theta_ {f}} - \lambda \frac {\partial L _ {d} ^ {i}}{\partial \theta_ {f}}\right) \tag {4}
$$

$$
\theta_ {y} \quad \leftarrow \quad \theta_ {y} - \mu \frac {\partial L _ {y} ^ {i}}{\partial \theta_ {y}} \tag {5}
$$

$$
\theta_ {d} \quad \longleftarrow \quad \theta_ {d} - \mu \frac {\partial L _ {d} ^ {i}}{\partial \theta_ {d}} \tag {6}
$$

where $\mu$ is the learning rate (which can vary over time).

The updates (4)-(6) are very similar to stochastic gradient descent (SGD) updates for a feed-forward deep model that comprises feature extractor fed into the label predictor and into the domain classifier. The difference is the −λ factor in (4) (the difference is important, as without such factor, stochastic gradient descent would try to make features dissimilar across domains in order to minimize the domain classification loss). Although direct implementation of (4)- (6) as SGD is not possible, it is highly desirable to reduce the updates (4)-(6) to some form of SGD, since SGD (and its variants) is the main learning algorithm implemented in most packages for deep learning.

Fortunately, such reduction can be accomplished by introducing a special gradient reversal layer (GRL) defined as follows. The gradient reversal layer has no parameters associated with it (apart from the meta-parameter λ, which

is not updated by backpropagation). During the forward propagation, GRL acts as an identity transform. During the backpropagation though, GRL takes the gradient from the subsequent level, multiplies it by −λ and passes it to the preceding layer. Implementing such layer using existing object-oriented packages for deep learning is thus as simple as defining a new layer can be, as defining procedures for forwardprop (identity transform), backprop (multiplying by a constant), and parameter update (nothing) is trivial.

The GRL as defined above is inserted between the feature extractor and the domain classifier, resulting in the architecture depicted in Figure 1. As the backpropagation process passes through the GRL, the partial derivatives of the loss that is downstream the GRL (i.e. $L _ { d } )$ w.r.t. the layer parameters that are upstream the GRL $( \mathrm { i } . \mathrm { e } . \ \theta _ { f } )$ get multiplied by −λ, i.e. ∂θf ∂Ld $\frac { \partial L _ { d } } { \partial \theta _ { f } }$ is effectively replaced with $- \lambda \frac { \partial L _ { d } } { \partial \theta _ { f } }$ ∂θf . Therefore, running SGD in the resulting model implements the updates (4)-(6) and converges to a saddle point of (1).

Mathematically, we can formally treat the gradient reversal layer as a “pseudo-function” $R _ { \lambda } ( \mathbf { x } )$ defined by two (incompatible) equations describing its forward- and backpropagation behaviour:

$$
R _ {\lambda} (\mathbf {x}) = \mathbf {x} \tag {7}
$$

$$
\frac {d R _ {\lambda}}{d \mathbf {x}} = - \lambda \mathbf {I} \tag {8}
$$

where I is an identity matrix. We can then define the objective “pseudo-function” of $( \theta _ { f } , \theta _ { y } , \theta _ { d } )$ that is being optimized by the stochastic gradient descent within our method:

$$
\begin{array}{l} \tilde{E} (\theta_{f},\theta_{y},\theta_{d}) = \sum_{\substack{i = 1..N\\ d_{i} = 0}}L_{y}\left(G_{y}(G_{f}(\mathbf{x}_{i};\theta_{f});\theta_{y}),y_{i}\right) + \\ \sum_ {i = 1.. N} L _ {d} \left(G _ {d} \left(R _ {\lambda} \left(G _ {f} \left(\mathbf {x} _ {i}; \theta_ {f}\right)\right); \theta_ {d}\right), y _ {i}\right) \tag {9} \\ \end{array}
$$

Running SGD for (9) thus leads to the emergence of features that are domain-invariant and discriminative at the same time. After the learning, the label predictor $y ( \mathbf { x } ) =$ $G _ { y } ( G _ { f } ( \mathbf { x } ; \theta _ { f } ) ; \theta _ { y } )$ can be used to predict labels for samples from the target domain (as well as from the source domain).

The simple learning procedure outlined above can be rederived/generalized along the lines suggested in [9] (see Appendix).

# 4. Experiments

# Datasets

In this report, we validate our approach within a set experiments on digit image classification. In each case, we train on the source dataset and test on a different target domain dataset, with considerable shifts between domains (see Figure 2). Overall, we have six datasets involved into the experiments that are described below.

![](images/26f4fbb67dbcd5b599c1063ada0ed5f5cfbff8215b71dd98b1257c8e2997308e.jpg)  
Figure 2. Random samples from the datasets used in the experiments. See Section 4 for details.

Table 1. Classification accuracies for digit image classifications for different source and target domains. In the case of MNIST, four different versions of the dataset were used: the original one, its dilated version (D), max-blended numbers over background (max, BG) and difference-blended numbers over background (|∆|, BG). The first row corresponds to the lower performance bound (i.e. if no adaptation is performed). The last row corresponds to training on the target domain data with known class labels (upper bound on the DA performance). For each of the two DA methods (ours and [5]) we show how much of the gap between the lower and the upper bounds was covered (in brackets). For all five cases, our approach outperforms [5] considerably, and covers a big portion of the gap.   

<table><tr><td>METHOD</td><td>SOURCE
TARGET</td><td>MNIST
MNIST (D)</td><td>MNIST
MNIST (max, BG)</td><td>MNIST
MNIST (|Δ|, BG)</td><td>SYN NUMBERS
SVHN</td><td>SVHN
MNIST</td></tr><tr><td colspan="2">SOURCE ONLY</td><td>.9678</td><td>.9173</td><td>.5749</td><td>.8665</td><td>.5919</td></tr><tr><td colspan="2">SA [5]</td><td>.9702 (12.3%)</td><td>.9197 (3.5%)</td><td>.6078 (7.9%)</td><td>.8672 (1.3%)</td><td>.6157 (5.9%)</td></tr><tr><td colspan="2">PROPOSED APPROACH</td><td>.9830 (75.8%)</td><td>.9476 (44.8%)</td><td>.8149 (57.9%)</td><td>.9048 (66.1%)</td><td>.7107 (29.3%)</td></tr><tr><td colspan="2">TRAIN ON TARGET (ORACLE)</td><td>.9878</td><td>.9848</td><td>.9891</td><td>.9244</td><td>.9951</td></tr></table>

The first four datasets are the well-known MNIST dataset [12] and its modifications. The modifications include:

• MNIST (D): Binary dilation with a 3×3 all-ones structuring element. This operation makes strokes thicker and may fill small holes thereby introducing additional challenge to the classification task.   
• MNIST (max, BG): Blending white digits over the patches randomly extracted from photos (BSDS500). While leaving meaningful pixels as they are, this modification adds strong background clutter.   
• MNIST (|∆|, BG): Difference-blending digits over the patches randomly extracted from photos (BSDS500). This operation is formally defined for two images I 1 , I 2 as ${ \cal I } _ { i j k } ^ { o u t } = | { \cal I } _ { i j k } ^ { 1 } - { \cal I } _ { i j k } ^ { 2 } |$ , where i, j are the coordinates of a pixel and k is a channel index. In other words, an output sample is produced by taking a patch

from a photo and inverting its pixels at positions corresponding to the pixels of a digit. For a human the classification task becomes only slightly harder compared to the original dataset (the digits are still clearly distinguishable) whereas for a CNN trained on MNIST this domain is quite distinct: the background and the strokes are no longer constant.

The last two datasets is the well-known Street View House Number (SVHN) dataset [14] and a new synthetic dataset Syn. Numbers of 500,000 images generated by ourselves from Windows fonts by varying the text (that includes different one-, two-, and three-digit numbers), positioning, orientation, background and stroke colors, and the amount of blur. The degrees of variation were chosen manually to simulate SVHN, however the two datasets are still rather distinct, the biggest difference being the structured clutter in the background of SVHN images.

# Baselines

In each experiment, we compare the results of our approach with the two natural baselines, i.e. training on the source domain without adaptation (a lower bound on any reasonable DA method) and training on the target domain while exploiting target domain labels (an upper bound on DA methods, assuming that target data are abundant and the shift between the domains is considerable).

In addition, we compare our approach against the recently proposed unsupervised DA method based on subspace alignment (SA) [5]. We detail the protocol for the use of SA further below.

The SA algorithm has one important free parameter, namely the number of principal components. In each of the experiments, we give this baseline an advantage by picking this value from the range {2, . . . , 60}, so that the performance on the target domain is maximized.

# CNN architectures.

Two different architectures were used in our experiments (Figure 3). We employ the smaller one if the source domain is MNIST and the bigger one otherwise. The chosen architectures are fairly standard for these datasets in terms of feature extractor and label predictor parts: the “MNIST” design is inspired by the classical LeNet-5 [12], while the second CNN is adopted from [19]. The domain classifier branch in both cases is somewhat arbitrary – the effect of changing its design is yet to be analyzed.

As for the loss functions, we set $L _ { y }$ and $L _ { d }$ to be logistic regression cost and binomial cross-entropy respectively.

# Training procedure.

The model is trained on 128-element batches of $3 2 ~ \times$ 32 color patches (we replicate channels for the original MNIST). No preprocessing is done except for the overall mean subtraction. A half of each batch is populated by the samples from the source domain (with known labels), the rest is comprised of the target domain (with unknown labels).

We use stochastic gradient descent with 0.9 momentum and the learning rate annealing described by the following formula:

$$
\mu_ {p} = \frac {\mu_ {0}}{(1 + \alpha \cdot p) ^ {\beta}}, \tag {10}
$$

where p is the training progress linearly changing from 0 to 1, µ0 = 0.01, α = 10 and β = 0.75 (the schedule was optimized to promote convergence and low error on the source domain).

In order to suppress noisy signal from the domain classifier at the early stages of the training procedure instead of

fixing the adaptation factor λ, we gradually change it from 0 to 1 using the following schedule:

$$
\lambda_ {p} = \frac {2}{1 + \exp (- \gamma \cdot p)} - 1, \tag {11}
$$

where γ was set to 10 in all experiments (the schedule was not optimized/tweaked).

Following [19] we also use dropout and `2-norm restriction when we train the SVHN architecture.

For the SA baseline, we consider the activations of the last hidden layer in the label predictor (before the final linear classifier) as descriptors/features, and learn the mapping between the source and the target domains [5].

Since the SA baseline requires to train a new classifier after adapting the features, and in order to put all the compared methods on an equal footing, we retrain the last layer of the label predictor using a standard linear SVM [4] for all four compared methods (including ours; the performance on the target domain remains approximately the same after the retraining).

# Visualizations.

We use t-SNE [22] projection to visualize feature distributions at different points of the network, while color-coding the domains (Figure 4). Overall, we observe quite strong correlation between the success of the adaptation in terms of the classification accuracy for the target domain, and the amount of discrepancy between the domain distributions in our visualizations.

# 4.1. Results.

We test our approach as well as the baselines for six different domain pairs. The results obtained by the composition of the feature extractor and the label predictor for the three baseline methods and our approach are summarized in Table 1 and are discussed below.

# MNIST → its variations

In the first three experiments, we deal with the MNIST dataset: a classifier is trained on the original dataset while being adapted to perform well on a particular modification of the source domain. The three target domains can be ordered in terms of the similarity to the source domain (which can be judged based on the performance of the classifier trained on the source domain and applied to the target domain). As expected, domain adaptation is easiest for the target domain that is closest to the source (MNIST (D)), and our method is able to cover three quarters of the performance gap between the source-trained and target-trained classifiers (i.e. lower and upper bounds).

![](images/03557c5f2bd4a280fbedb848c8d3ad78ad4e9edcd194df25d18f6e17c3d427af.jpg)  
(a) MNIST architecture

![](images/c8fa3dc492d5057bd52a48f19bf15a246f78be56dd1df5a602c9a5113303f8cf.jpg)  
(b) SVHN architecture   
Figure 3. CNN architectures used in the experiments. Boxes correspond to transformations applied to the data. Color-coding is the same as in Figure 1. See Section 4 for details.

The adaptation task is harder in the case of digits blended over the color background. Although samples from these domains have significant background clutter, our approach succeeded at intermixing the features (Figure 4), which led to very successful adaptation results (considering that the adaptation is unsupervised). The performance of the unsupervised DA method [5] for all three datasets is much more modest, thus highlighting the difficulty of the adaptation task.

# Synthetic numbers → SVHN

To address a common scenario of training on synthetic images and testing on challenging real images, we use SVHN as a target domain and synthetic digits as a source. The proposed backpropagation-based technique works well covering two thirds of the gap between training with source data only and training on target domain data with known target labels. In contrast, [5] does not result in any significant improvement in the classification accuracy, thus highlighting that the adaptation task is even more challenging than in the case of MNIST experiments.

# MNIST ↔ SVHN

Finally, we test our approach on the two most distinct domains, namely, MNIST and SVHN. Training on SVHN even without adaptation is challenging — classification error stays high during the first 150 epochs. In order to avoid ending up in a poor local minimum we, therefore, do not use learning rate annealing here. Obviously, the two directions (MNIST-to-SVHN and SVHN-to-MNIST) are not equally difficult. As SVHN is more diverse, a model trained on

SVHN is expected to be more generic and to perform reasonably on the MNIST dataset. This, indeed, turns out to be the case and is supported by the appearance of the feature distributions. We observe a quite strong separation between the domains when we feed them into the CNN trained solely on MNIST, whereas for the SVHN-trained network the features are much more intermixed. This difference probably explains why our method succeeded in improving the performance by adaptation in the SVHN → MNIST scenario (see Table 1) but not in the opposite direction (SA is not able to perform adaptation in this case either). Unsupervised adaptation from MNIST to SVHN thus remains a challenge to be addressed in the future work.

# 5. Discussion

We have proposed a new approach to unsupervised domain adaptation of deep feed-forward architectures, which allows large-scale training based on large amount of annotated data in the source domain and large amount of unannotated data in the target domain. Similarly to many previous shallow and deep DA techniques, the adaptation is achieved through aligning the distributions of features across the two domains. However, unlike previous approaches, the alignment is accomplished through standard backpropagation training. The approach is therefore rather scalable, and can be implemented using any deep learning package.

In the experiments with digit image classification, the approach demonstrated its efficiency, significantly outperforming a state-of-the-art unsupervised DA method. Further evaluation on larger-scale tasks constitutes the immediate future work. It is also interesting whether the approach can benefit from a good initialization of the feature extrac-

![](images/5ac060f2b8c8b25e170aee347c0cb954b8f8193448661fd7ad13e69bf03bebde.jpg)  
(a) Non-adapted

![](images/dca76e469debe79fdd8f6e35f8259c08350702838d39bc45e7c659e361c5f307.jpg)  
(b) Adapted

![](images/57b41b69294f987ba29e8c7ce1163a69111f1c38a6d758ff764dd4dc2efdf090.jpg)  
MNIST → MNIST (|∆|, BG): top feature extractor layer   
(a) Non-adapted

![](images/2bc7fa3bb390f8608d9f867fbe6f94f59c0050be7574fbbabe9f217353195632.jpg)  
(b) Adapted

![](images/2f9cb733f369276f7f536b166aec346ab655b7748fe81549abdcbee883ecdaf9.jpg)  
SYN NUMBERS → SVHN: last hidden layer of the label predictor   
(a) Non-adapted

![](images/74c78039161f5bb187f382d61caeed917b64d8d03a8174434e29aee0da8ad808.jpg)  
(b) Adapted   
Figure 4. The effect of adaptation on the distribution of the extracted features. The figure shows t-SNE [22] visualizations of the CNN’s activations (a) in case when no adaptation was performed and (b) in case when our adaptation procedure was incorporated into training. Blue points correspond to the source domain examples, while red ones correspond to the target domain. In all cases, the adaptation in our method makes the two distributions of features much closer.

tor. For this, a natural choice would be to use deep autoencoder/deconvolution network trained on both domains (or on the target domain) in a similar vein to [6, 17], effectively using [6, 17] as an initialization to our method.

# References

[1] A. Babenko, A. Slesarev, A. Chigorin, and V. S. Lempitsky. Neural codes for image retrieval. ECCV, pp. 584–599, 2014. 2   
[2] M. Baktashmotlagh, M. T. Harandi, B. C. Lovell, and M. Salzmann. Unsupervised domain adaptation by domain invariant projection. ICCV, pp. 769–776, 2013. 2   
[3] K. M. Borgwardt, A. Gretton, M. J. Rasch, H. Kriegel, B. Scholkopf, and A. J. Smola. Integrating structured ¨ biological data by kernel maximum mean discrepancy. ISMB, pp. 49–57, 2006. 2   
[4] R.-E. Fan, K.-W. Chang, C.-J. Hsieh, X.-R. Wang, and C.-J. Lin. LIBLINEAR: A library for large linear classification. Journal of Machine Learning Research, 9:1871–1874, 2008. 6   
[5] B. Fernando, A. Habrard, M. Sebban, and T. Tuytelaars. Unsupervised visual domain adaptation using subspace alignment. ICCV, 2013. 2, 5, 6, 7   
[6] X. Glorot, A. Bordes, and Y. Bengio. Domain adaptation for large-scale sentiment classification: A deep learning approach. ICML, pp. 513–520, 2011. 2, 9   
[7] B. Gong, K. Grauman, and F. Sha. Connecting the dots with landmarks: Discriminatively learning domaininvariant features for unsupervised domain adaptation. ICML, pp. 222–230, 2013. 2   
[8] B. Gong, Y. Shi, F. Sha, and K. Grauman. Geodesic flow kernel for unsupervised domain adaptation. CVPR, pp. 2066–2073, 2012. 2   
[9] I. J. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. C. Courville, and Y. Bengio. Generative adversarial networks. CoRR, abs/1406.2661, 2014. 2, 4, 9, 10   
[10] R. Gopalan, R. Li, and R. Chellappa. Domain adaptation for object recognition: An unsupervised approach. ICCV, pp. 999–1006, 2011. 2   
[11] J. Huang, A. J. Smola, A. Gretton, K. M. Borgwardt, and B. Scholkopf. Correcting sample selection bias by ¨ unlabeled data. NIPS, pp. 601–608, 2006. 2   
[12] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner. Gradient-based learning applied to document recognition. Proceedings of the IEEE, 86(11):2278–2324, 1998. 2, 5, 6   
[13] J. Liebelt and C. Schmid. Multi-view object class detection with a 3d geometric model. CVPR, 2010. 1

[14] Y. Netzer, T. Wang, A. Coates, A. Bissacco, B. Wu, and A. Y. Ng. Reading digits in natural images with unsupervised feature learning. NIPS Workshop on Deep Learning and Unsupervised Feature Learning 2011, 2011. 2, 5   
[15] M. Oquab, L. Bottou, I. Laptev, and J. Sivic. Learning and transferring mid-level image representations using convolutional neural networks. CVPR, 2014. 2   
[16] S. J. Pan, I. W. Tsang, J. T. Kwok, and Q. Yang. Domain adaptation via transfer component analysis. IEEE Transactions on Neural Networks, 22(2):199– 210, 2011. 2   
[17] S. B. S. Chopra and R. Gopalan. Dlid: Deep learning for domain adaptation by interpolating between domains. ICML Workshop on Challenges in Representation Learning, 2013. 2, 9   
[18] H. Shimodaira. Improving predictive inference under covariate shift by weighting the log-likelihood function. Journal of Statistical Planning and Inference, 90(2):227–244, 2000. 3   
[19] N. Srivastava. Improving neural networks with dropout. PhD thesis, University of Toronto, 2013. 6   
[20] M. Stark, M. Goesele, and B. Schiele. Back to the future: Learning shape models from 3d CAD data. BMVC, pp. 1–11, 2010. 1   
[21] B. Sun and K. Saenko. From virtual to reality: Fast adaptation of virtual object detectors to real domains. BMVC, 2014. 1   
[22] L. van der Maaten. Barnes-hut-sne. CoRR, abs/1301.3342, 2013. 6, 8   
[23] D. Vazquez, A. M. L ´ opez, J. Mar ´ ´ın, D. Ponsa, and D. G. Gomez. Virtual and real world adaptationfor pedestrian detection. IEEE Trans. Pattern Anal. Mach. Intell., 36(4):797–809, 2014. 1   
[24] M. D. Zeiler and R. Fergus. Visualizing and understanding convolutional networks. CoRR, abs/1311.2901, 2013. 2

# Appendix: An alternative optimization approach

There exists an alternative construction (inspired by [9]) that leads to the same updates (4)-(6). Rather than using the gradient reversal layer, the construction introduces two different loss functions for the domain classifier. Minimization of the first domain loss $( L _ { d + } )$ should lead to a better domain discrimination, while the second domain loss $( L _ { d - } )$ is minimized when the domains are distinct. Stochastic updates

for $\theta _ { f }$ and $\theta _ { d }$ are then defined as:

$$
\theta_ {f} \quad \leftarrow \quad \theta_ {f} - \mu \left(\frac {\partial L _ {y} ^ {i}}{\partial \theta_ {f}} + \frac {\partial L _ {d -} ^ {i}}{\partial \theta_ {f}}\right) \tag {12}
$$

$$
\theta_ {d} \quad \leftarrow \quad \theta_ {d} - \mu \frac {\partial L _ {d +} ^ {i}}{\partial \theta_ {d}}, \tag {13}
$$

Thus, different parameters participate in the optimization of different losses

In this framework, the gradient reversal layer constitutes a special case, corresponding to the pair of domain losses $( L _ { d } , - \lambda L _ { d } )$ . However, other pairs of loss functions can be used. One example would be the binomial cross-entropy [9]:

$$
L _ {d +} (q, d) = \sum_ {i = 1.. N} d _ {i} \log \left(q _ {i}\right) + \left(1 - d _ {i}\right) \log \left(1 - q _ {i}\right), \tag {14}
$$

where d indicates domain indices and $q$ is an output of the predictor. In that case “adversarial” loss is easily obtained by swapping domain labels, i.e. $L _ { d - } ( q , d ) = L _ { d + } ( q , 1 - d )$ .

This particular pair has a potential advantage of producing stronger gradients at early learning stages if the domains are quite dissimilar. In our experiments, however, we did not observe any significant improvement resulting from this choice of losses.