---
title: "Context-modulation of hippocampal dynamics and deep convolutional networks"
authors:
  - "James B. Aimone"
  - "William M. Severa"
date: "2017-11-28"
year: "2017"
journal: "arXiv"
doi: "arXiv:1711.09876"
abstract: "Complex architectures of biological neural circuits, such as parallel processing\"
abstract_cn: "生物神经回路的复杂架构（如并行处理通路）在许多认知研究中已被行为学证据所暗示。然而，回路复杂性对神经计算的理论影响仅在有限情况下被探索。本文引入一种机制，通过从皮层到海马体\"
keywords:
  - "[[Hippocampus]]"
  - "[[CA3]]"
  - "[[Context modulation]]"
  - "[[Deep learning]]"
cite: "[1] Aimone J B, Severa W M. Context-modulation of hippocampal dynamics and deep convolutional\"
aiSum: "受海马体 CA3 双通路（EC 直接投射和 EC→DG→CA3 间接投射）启发，提出上下文调制深度神经网络，通过上下文敏感偏置在 CIFAR-100 和 Fashion-MNIST\"
confidence: "low"
wiki_concepts:
  - "[[Neural network]]"
---

James B. Aimone

Center for Computing Research

Sandia National Laboratories

Albuquerque, NM 87185-1327

jbaimon@sandia.gov

William M. Severa

Center for Computing Research

Sandia National Laboratories

Albuquerque, NM 87185-1327

wmsever@sandia.gov

# Abstract

Complex architectures of biological neural circuits, such as parallel processing pathways, has been behaviorally implicated in many cognitive studies. However, the theoretical consequences of circuit complexity on neural computation have only been explored in limited cases. Here, we introduce a mechanism by which direct and indirect pathways from cortex to the CA3 region of the hippocampus can balance both contextual gating of memory formation and driving network activity. We implement this concept in a deep artificial neural network by enabling a context-sensitive bias. The motivation for this is to improve performance of a size-constrained network. Using direct knowledge of the superclass information in the CIFAR-100 and Fashion-MNIST datasets, we show a dramatic increase in performance without an increase in network size.

# 1 Introduction

Although much of the attention on leveraging biological complexity in machine learning has focused on spiking opposed to non-spiking neurons, the difference in circuit architecture complexity between artificial neural networks (ANNs) and neural circuits is equally striking. ANNs are typically feedforward or leverage local recurrence; however, outside of early sensory processing, most biological neural circuits are far more complex. While the Felleman and van Essen [3] circuit for the visual system may be the most famous, the brain is flush with examples of parallel pathways, extended loops, and consolidation of multiple inputs. In this short paper, we explore how parallel pathways could be useful for conveying information at multiple scales, in effect providing an efficient mechanism for conveying global context and local meaning simultaneously.

To examine the effect of multiple inputs on a neuron, specifically the unique case where a neural population receives both a direct and an indirect input from a common source, we specifically look at the effects of convergent population inputs onto neurons within the CA3 of the hippocampus, in which neurons receive direct input from the cortex and an indirect cortical input that passes through the dentate gyrus (DG). While the hippocampus is more commonly associated with memory formation at the circuit level, we consider it here simply for its well characterized and straightforward local structure. From this anatomy, we infer a unique function of separated synaptic inputs as it relates to conveying specific and coarse information.

# 2 Context modulation of Hippocampal neurons through dual pathways

First, to illustrate how the brain potentially uses parallel processing pathways, we consider a particular case within the hippocampus. While the hippocampus shares few similarities to modern artificial networks, it has a clear anatomical structure that makes it amenable to analysis, consisting of three

primary sub-regions (the DG, CA3, and CA1) that each receive cortical input from the entorhinal cortex (EC) and a well-understood connectivity (Figure 1a).

Here, we focus on the influence of the direct (EC) projection and the indirect (EC via DG) projection on the short-term dynamics of the CA3 network. We ignore for now the extensive forms of plasticity, including lifelong neurogenesis in the DG [1], recurrent synaptic plasticity in CA3 [8] and robust synaptic turnover in CA1 [2]. While the DG does receive some inputs aside from EC, for the most part the DG is thought to recode EC inputs, suggesting that the CA3 receives two versions of the same information, anatomically flanking the numerous recurrent connections from within the CA3 network (Figure 1b). The conjunction of two anatomically distinct yet informatically overlapping projections onto the recurrent CA3 network has been key to many influencial theoretical studies of hippocampus function [11], however here we consider whether this paradigm offers a general capability to artificial networks.

![](images/ea23cff5fa8e6a752b9131d735546dab6d8f4ee093ee8a0308e6b1747ed5fbb5.jpg)  
(a)

![](images/2c132acbc7610faf13a7671433c3d5d140b2f1b13e1185907502b743996f4486.jpg)  
(b)

![](images/1780167c37ac9189924b4d951dbf226242b4a59dd7f0043b6665dd402c4da382.jpg)  
(c)   
Figure 1: (a) Illustration of subregions of hippocampus circuit. (b) Detailed view of excitatory inputs onto CA3 pyramidal neuron. (c) Schematic of direct cortical inputs providing context bias for processing in the hippocampus.

First, we look at the anatomical structure of these inputs (Figure 1b). While there are only a few DG inputs on a CA3 pyramidal neuron, they are massive — often covering several dendritic spines. The proximity and strength of these synapses suggests that when they are active, they can “detonate” the downstream neuron highly efficiently [6]. On the other hand, the EC inputs, while numerous, are on the distal dendrites far away from the soma and, unlike the DG inputs, likely provide only a moderate current to the neuron. In between lie the recurrent connections, which are both numerous and efficacious, consistent with other models of hippocampal and cortical recurrent dynamics.

Second, we consider the nature of the external inputs’ representations. DG neurons are known to be very sparsely active—with only a small percentage active at a given time and highly decorrelated even within a spatial context[9]. Thus given the sparse input numbers, we should expect that generally the DG inputs are silent, interrupted by occasional bursts from a single DG neuron. In contrast, the EC inputs have a more distributed code, either as grid cells encoding space or other high level cortical representations [4]. Thus across the approximately 5,000 synaptic inputs as a whole, we should expect a fairly smooth transitions in combined input activity, particularly within a given environment.

Combined, these two observations suggest the model of CA3 neuron modulation shown in Figure 1c. While the dynamics of the CA3 network are likely dominated by the numerous and reasonably powerful recurrent connections, the cortex can use these two distinct inputs to control these dynamics. For one, the sparse and powerful indirect inputs through the DG are well-suited to instantaneously set the recurrent network in a desired state—a highly distinct state, per the DG’s presumed pattern separation function—which then quickly evolves per the recurrent connections. At the same time, the

slowly evolving and diffuse direct inputs are ideal for setting the context of these dynamics. These weaker inputs are not necessarily able to drive activity directly, but they can bias the recurrent activity in meaningful ways that can similarly influence computation, albeit at far broader time scales.

One can hypothesize several benefits for having context reflected this way in hippocampal memory encoding (Figure 1c). First, having relatively small subsets of neurons pre-selected by the EC would be well-suited for fast “one-shot”-like learning that minimizes interference with other learned representations. Such rapid learning may either occur within the recurrent CA3 connections [8] or may be better suited for the feed-forward Schaffer Collateral connection to CA1. Indeed, recent results showing rapid CA1 synaptic restructuring would be consistent with that region continually realigning itself to these relevant CA3 ensembles [2]. At the same time, as these context-selected subsets of neurons do not need to be independent, there are effectively a very large number of potential combinations available for any encoding. Thus while the memory capacity within the recurrent CA3 network may be relatively low for any particular context, the overall capacity may be quite high.

# 3 Impact of parallel pathways on context modulation of ANNs

Some ANNs, such as deep residual networks, already leverage parallel pathways to facilitate learning [5], although this use of parallel pathways was not necessarily biologically inspired. So we next sought to identify whether parallel inputs could provide context inputs that help constrain a network’s function in a manner comparable to how we hypothesized hippocampus function may be improved.

One key motivation for this development is the application of deep convolutional networks (DCNs) in memory-constrained environments. These include the growing segment of embedded processors available for internet of things (IoT) devices as well as drones and autonomous vehicles. One promising direction is neural network compression, however, the neuroscience inspiration explained above may enable more efficient models. The impact of context in the above CA3 study suggests that the correlation of EC input against a baseline sensitivity provides a bias of sorts to the overall CA3 dynamics. Setting aside the specific downstream dynamics of CA3, the consideration of context in the biological setting is not altogether different from the concept of biases in ANNs. In our thought experiment above, the net effect of shifting the EC input onto pyramidal neurons is comparable to shifting the threshold required for other inputs to drive it to fire (Figure 2a).

We explored our model of context switching on a simple DCN implementation. Inspired the EC “bias” above, our ANN model adds a parameter and expands bias to be context-dependent. For each input vector/image x, we assume there exist an accompanying context xˆ which we represent with a one-hot vector encoding. Formally, the output of a traditional ANN layer is computed as $o ( x ) = f ( A x + b )$ where A is a weight matrix, b is the bias and f is the activation function. For a context xˆ, instead of the classic bias, we use $o ( x ) = f ( A x + b _ { \hat { x } } )$ which represents the concept that the bias may depend on xˆ. Let $\delta _ { i } = 1$ if the context xˆ is i and $\delta _ { i } = 0$ otherwise. In this case, our layer can equivalently be written $\begin{array} { r } { o ( x ) = f ( A x + \sum _ { i } \delta _ { i } b _ { \hat { x } } ) = f ( A x + B \hat { x } ) } \end{array}$ where B is a matrix representing each of the biases under each context.

# 3.1 Using Context to Improve Classification

We illustrate this model on the CIFAR-100 dataset [7] and Fashion-MNIST [12](Figure 2b). In CIFAR-100, each image belongs to both a superclass (20, also called a ‘coarse’ class) and a standard class (100). For Fashion-MNIST, we created coarse superclasses ‘Tops’ (consisting of ‘T-shirt/top’, ‘Pullover’, ‘Coat’, ‘Shirt’), ‘Bottoms’ (‘Trouser’, ‘Dress’) and ‘Other’ (‘Sandal’, ‘Sneaker’, ‘Bag’, ‘Ankle boot’). We aim to classify the standard class by using the superclass as the context xˆ. We use VGG16 pre-trained on ImageNet for feature extraction [10]. After the convolutional layers, we employ two densely connected layers (256 exponential linear unit nodes, followed by a softmax layer). We introduce the context into these layers at just the first dense layer. Layers that received context used no bias. We use dropout (0.5), to mitigate overfitting, and the adadelta optimizer [13]. Tests were performed at a variety of context accuracy levels, wherein the superclass information was systematically degraded to simulate various superclass classifier performance.

The inclusion of superclass information improves the classification performance of our networks (Figure 2c). As the quality of the superclass labels decrease, the benefit of context is diminished. For Fashion-MNIST, any noise $> 1 5 \%$ in the context input offsets the benefit of the additional context.

![](images/48b07bac7482a98cb792a588f5625a9ca5290ca7501e6fb2c3e4b6712a16251c.jpg)  
(a)

![](images/4814956800e1432bcb9f121f6172c2e169b826b41b7a258473484e9c58b5a54d.jpg)  
(b)

![](images/f3edfbd1dbcfad22f64f06c3f9efcc178b30859e288756c67c9903a1c168c84e.jpg)  
  
Figure 2: (a) Schematic of direct superclass inputs providing context as bias inputs for VGG image processing. (b) Examples of how different classes fall into superclasses within CIFAR and Fashion-MNIST. (c) Results from adding context to VGG Networks on CIFAR-100 and Fashion-MNIST. The means over 10 trials is plotted with the shaded areas representing 95% confidence intervals.

However, context aids CIFAR performance even with noisy contextual input. While the relative information content of the superclass labels likely explains some of the difference in context efficacy between these two data sets, future work is needed to help discern the differences seen here.

# 4 Conclusions

Even though hippocampal role in memory is quite a different function to image processing by DCNs, the results from both studies highlights the potential importance of parallel information pathways in neural computation. The use of multiple pathways is commonly seen within neural circuits of the brain. It is not unreasonable that the function of dual inputs proposed for the hippocampus here — coarse information influences context while fine-grained information drives circuit behavior acutely — may be general to many cortical and cortex-affiliated regions.

Accordingly, the results here show that in artificial visual processing we can observe that a parallel introduction of coarse and fine-grained information can improve performance markedly. In our case providing superclass information to help guide the classification of images has a dramatic benefit on overall network performance. It is not surprising that additional information helps classification, however there is no reason that the approach shown here cannot be extended to have the full system trained to learn both levels of information. Further, as examples of adversarial limitations of deep networks continue to be introduced, it is worth considering that networks using parallel processing pathways to perform both coarse and fine classification may be more robust to dramatic sub-perceptual manipulation of low-level features.

# Acknowledgments

This work was funded by the DOE Advanced Simulation and Computing program and Laboratory-Directed Research and Development Program at Sandia National Laboratories. Sandia National Laboratories is a multiprogram laboratory managed and operated by National Technology and Engineering Solutions of Sandia, LLC, for the U.S. Department of Energy’s National Nuclear Security Administration under contract DE-NA0003525.

# References

[1] James B Aimone, Wei Deng, and Fred H Gage. Resolving new memories: a critical look at the dentate gyrus, adult neurogenesis, and pattern separation. Neuron, 70(4):589–596, 2011.   
[2] Alessio Attardo, James E Fitzgerald, and Mark J Schnitzer. Impermanence of dendritic spines in live adult ca1 hippocampus. Nature, 523(7562):592–596, 2015.   
[3] Daniel J Felleman and David C Van Essen. Distributed hierarchical processing in the primate cerebral cortex. Cerebral cortex, 1(1):1–47, 1991.   
[4] Ila R Fiete, Yoram Burak, and Ted Brookings. What grid cells convey about rat location. Journal of Neuroscience, 28(27):6858–6871, 2008.   
[5] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pages 770–778, 2016.   
[6] Darrell A Henze, Lucia Wittner, and György Buzsáki. Single granule cells reliably discharge targets in the hippocampal ca3 network in vivo. Nature neuroscience, 5(8):790, 2002.   
[7] Alex Krizhevsky and Geoffrey Hinton. Learning multiple layers of features from tiny images. 2009.   
[8] Nelson Rebola, Mario Carta, and Christophe Mulle. Operation and plasticity of hippocampal ca3 circuits: implications for memory encoding. Nature Reviews Neuroscience, 2017.   
[9] William Severa, Ojas Parekh, Conrad D James, and James B Aimone. A combinatorial model for dentate gyrus sparse coding. Neural Computation, 2016.   
[10] Karen Simonyan and Andrew Zisserman. Very deep convolutional networks for large-scale image recognition. arXiv preprint arXiv:1409.1556, 2014.   
[11] Alessandro Treves and Edmund T Rolls. Computational constraints suggest the need for two distinct input systems to the hippocampal ca3 network. Hippocampus, 2(2):189–199, 1992.   
[12] Han Xiao, Kashif Rasul, and Roland Vollgraf. Fashion-mnist: a novel image dataset for benchmarking machine learning algorithms, 2017.   
[13] Matthew D Zeiler. Adadelta: an adaptive learning rate method. arXiv preprint arXiv:1212.5701, 2012.