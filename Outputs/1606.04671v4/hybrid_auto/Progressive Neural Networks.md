---


title: "Progressive Neural Networks"
authors:
  - "Andrei Neil"
  - "Guillaume Hubert"
  - "James Koray"
  - "Razvan Raia"
  - "Hadsell"
date: "2016‑06‑15"
year: 2016
journal: "arXiv"
doi: "arXiv:1606.04671v4"
abstract: "Learning to solve complex sequences of tasks—while both leveraging transfer"
abstract_cn: "学习解决复杂任务序列——同时利用迁移和避免灾难性遗忘——仍然是实现人类水平智能的关键障碍。渐进网络方法朝这个方向迈进了一步：它们不会遗忘，并能通过横向连接利用先前学到的特征。我们在多种强化学习任务（Atari"
cite: "[1] Rusu A A, Rabinowitz N C, Desjardins G, et al. Progressive neural networks[J]."
aiSum: "提出渐进网络架构：通过横向连接利用先前学到的特征，避免灾难性遗忘，在 Atari 和 3D 迷宫任务上优于预训练‑微调基线，证明迁移发生在感知和控制层。"
confidence: "low"
keywords:
  - "[[Catastrophic forgetting]]"
  - "[[Continual learning]]"
---

# Progressive Neural Networks

Andrei A. Rusu*, Neil C. Rabinowitz*, Guillaume Desjardins*, Hubert Soyer, James Kirkpatrick, Koray Kavukcuoglu, Razvan Pascanu, Raia Hadsell

* These authors contributed equally to this work

Google DeepMind

London, UK

{andreirusu, ncr, gdesjardins, soyer, kirkpatrick, korayk, razp, raia}@google.com

# Abstract

Learning to solve complex sequences of tasks—while both leveraging transfer and avoiding catastrophic forgetting—remains a key obstacle to achieving human-level intelligence. The progressive networks approach represents a step forward in this direction: they are immune to forgetting and can leverage prior knowledge via lateral connections to previously learned features. We evaluate this architecture extensively on a wide variety of reinforcement learning tasks (Atari and 3D maze games), and show that it outperforms common baselines based on pretraining and finetuning. Using a novel sensitivity measure, we demonstrate that transfer occurs at both low-level sensory and high-level control layers of the learned policy.

# 1 Introduction

Finetuning remains the method of choice for transfer learning with neural networks: a model is pretrained on a source domain (where data is often abundant), the output layers of the model are adapted to the target domain, and the network is finetuned via backpropagation. This approach was pioneered in [7] by transferring knowledge from a generative to a discriminative model, and has since been generalized with great success [11]. Unfortunately, the approach has drawbacks which make it unsuitable for transferring across multiple tasks: if we wish to leverage knowledge acquired over a sequence of experiences, which model should we use to initialize subsequent models? This seems to require not only a learning method that can support transfer learning without catastrophic forgetting, but also foreknowledge of task similarity. Furthermore, while finetuning may allow us to recover expert performance in the target domain, it is a destructive process which discards the previously learned function. One could copy each model before finetuning to explicitly remember all previous tasks, but the issue of selecting a proper initialization remains. While distillation [8] offers one potential solution to multitask learning [17], it requires a reservoir of persistent training data for all tasks, an assumption which may not always hold.

This paper introduces progressive networks, a novel model architecture with explicit support for transfer across sequences of tasks. While finetuning incorporates prior knowledge only at initialization, progressive networks retain a pool of pretrained models throughout training, and learn lateral connections from these to extract useful features for the new task. By combining previously learned features in this manner, progressive networks achieve a richer compositionality, in which prior knowledge is no longer transient and can be integrated at each layer of the feature hierarchy. Moreover, the addition of new capacity alongside pretrained networks gives these models the flexibility to both reuse old computations and learn new ones. As we will show, progressive networks naturally accumulate experiences and are immune to catastrophic forgetting by design, making them an ideal springboard for tackling long-standing problems of continual or lifelong learning.

The contributions of this paper are threefold. While many of the individual ingredients used in progressive nets can be found in the literature, their combination and use in solving complex sequences

of tasks is novel. Second, we extensively evaluate the model in complex reinforcement learning domains. In the process, we also evaluate alternative approaches to transfer (such as finetuning) within the RL domain. In particular, we show that progressive networks provide comparable (if not slightly better) transfer performance to traditional finetuning, but without the destructive consequences. Finally, we develop a novel analysis based on Fisher Information and perturbation which allows us to analyse in detail how and where transfer occurs across tasks.

# 2 Progressive Networks

Continual learning is a long-standing goal of machine learning, where agents not only learn (and remember) a series of tasks experienced in sequence, but also have the ability to transfer knowledge from previous tasks to improve convergence speed [20]. Progressive networks integrate these desiderata directly into the model architecture: catastrophic forgetting is prevented by instantiating a new neural network (a column) for each task being solved, while transfer is enabled via lateral connections to features of previously learned columns. The scalability of this approach is addressed at the end of this section.

A progressive network starts with a single column: a deep neural network having L layers with hidden activations $h _ { i } ^ { ( 1 ) } \in \mathbb { R } ^ { n _ { i } }$ , with $n _ { i }$ the number of units at layer $i \leq L$ , and parameters $\Theta ^ { ( 1 ) }$ trained to convergence. When switching to a second task, the parameters $\Theta ^ { ( 1 ) }$ are “frozen” and a new column with parameters $\Theta ^ { ( 2 ) }$ is instantiated (with random initialization), where layer ${ h } _ { i } ^ { ( 2 ) }$ receives input from both $h _ { i - 1 } ^ { ( 2 ) }$ and $h _ { i - 1 } ^ { ( 1 ) }$ via lateral connections. This generalizes to K tasks as follows: 1:

$$
h _ {i} ^ {(k)} = f \left(W _ {i} ^ {(k)} h _ {i - 1} ^ {(k)} + \sum_ {j <   k} U _ {i} ^ {(k: j)} h _ {i - 1} ^ {(j)}\right), \tag {1}
$$

where $W _ { i } ^ { ( k ) } \in \mathbb { R } ^ { n _ { i } \times n _ { i - 1 } }$ is the weight matrix of layer i of column $k , U _ { i } ^ { ( k : j ) } \in \mathbb { R } ^ { n _ { i } \times n _ { j } }$ are the lateral connections from layer i − 1 of column j, to layer i of column k and $h _ { 0 }$ is the network input. $f$ is an element-wise non-linearity: we use $f ( x ) = \mathrm { { \dot { m a x } } } ( 0 , x )$ for all intermediate layers. A progressive network with $K = 3$ is shown in Figure 1.

![](images/89279301dfd3dfdf90096f3dc343b08f1a1ea56d3cef56e4c02db37a3c0e82c9.jpg)  
Figure 1: Depiction of a three column progressive network. The first two columns on the left (dashed arrows) were trained on task 1 and 2 respectively. The grey box labelled a represent the adapter layers (see text). A third column is added for the final task having access to all previously learned features.

These modelling decisions are informed by our desire to: (1) solve K independent tasks at the end of training; (2) accelerate learning via transfer when possible; and (3) avoid catastrophic forgetting.

In the standard pretrain-and-finetune paradigm, there is often an implicit assumption of “overlap” between the tasks. Finetuning is efficient in this setting, as parameters need only be adjusted slightly to the target domain, and often only the top layer is retrained [23]. In contrast, we make no assumptions about the relationship between tasks, which may in practice be orthogonal or even adversarial. While the finetuning stage could potentially unlearn these features, this may prove difficult. Progressive networks side-step this issue by allocating a new column for each new task, whose weights are initialized randomly. Compared to the task-relevant initialization of pretraining,

columns in progressive networks are free to reuse, modify or ignore previously learned features via the lateral connections. As the lateral connections U (k:j)i $U _ { i } ^ { ( k : j ) }$ are only from column k to columns $j < k$ previous columns are not affected by the newly learned features in the forward pass. Because also the parameters $\{ \Theta ^ { ( j ) } ; j < k \}$ are kept frozen (i.e. are constants for the optimizer) when training $\Theta ^ { ( k ) }$ , there is no interference between tasks and hence no catastrophic forgetting.

Application to Reinforcement Learning. Although progressive networks are widely applicable, this paper focuses on their application to deep reinforcement learning. In this case, each column is trained to solve a particular Markov Decision Process (MDP): the k-th column thus defines a policy $\pi ^ { ( k ) } ( a \mid s )$ taking as input a state s given by the environment, and generating probabilities over actions $\pi ^ { ( k ) } ( a \mid s ) : = h _ { L } ^ { ( k ) } ( s )$ . At each time-step, an action is sampled from this distribution and taken in the environment, yielding the subsequent state. This policy implicitly defines a stationary distribution $\rho _ { \pi ^ { ( k ) } } ( s , a )$ over states and actions.

Adapters. In practice, we augment the progressive network layer of Equation 2 with non-linear lateral connections which we call adapters. They serve both to imprdimensionality reduction. Defining the vector of anterior features $h _ { i - 1 } ^ { ( < k ) } = [ h _ { i - 1 } ^ { ( 1 ) } \cdot \cdot \cdot h _ { i - 1 } ^ { ( \overline { { j } } ) } \cdot \cdot \cdot \cdot \hat { h } _ { i - 1 } ^ { ( k - 1 ) } ]$ [h(1)i−1 · · · h i − 1 ] of dimensionality n(<k)i−1 $n _ { i - 1 } ^ { ( < k ) }$ , in the case of dense layers, we replace the linear lateral connection with a single hidden layer MLP. Before feeding the lateral activations into the MLP, we multiply them by a learned scalar, initialized by a random small value. Its role is to adjust for the different scales of the different inputs. The hidden layer of the non-linear adapter is a projection onto an $n _ { i }$ dimensional subspace. As the index k grows, this ensures that the number of parameters stemming from the lateral connections is in the same order as $\left| \Theta ^ { ( 1 ) } \right|$ . Omitting bias terms, we get:

$$
h _ {i} ^ {(k)} = \sigma \left(W _ {i} ^ {(k)} h _ {i - 1} ^ {(k)} + U _ {i} ^ {(k: j)} \sigma \left(V _ {i} ^ {(k: j)} \alpha_ {i - 1} ^ {(<   k)} h _ {i - 1} ^ {(<   k)}\right)\right), \tag {2}
$$

where $V _ { i } ^ { ( k : j ) } \in \mathbb { R } ^ { n _ { i - 1 } \times n _ { i - 1 } ^ { ( < k ) } }$ is the projection matrix. For convolutional layers, dimensionality reduction is performed via $1 \times 1$ convolutions [10].

Limitations. Progressive networks are a stepping stone towards a full continual learning agent: they contain the necessary ingredients to learn multiple tasks, in sequence, while enabling transfer and being immune to catastrophic forgetting. A downside of the approach is the growth in number of parameters with the number of tasks. The analysis of Appendix 2 reveals that only a fraction of the new capacity is actually utilized, and that this trend increases with more columns. This suggests that growth can be addressed, e.g. by adding fewer layers or less capacity, by pruning [9], or by online compression [17] during learning. Furthermore, while progressive networks retain the ability to solve all $\dot { K }$ tasks at test time, choosing which column to use for inference requires knowledge of the task label. These issues are left as future work.

# 3 Transfer Analysis

Unlike finetuning, progressive nets do not destroy the features learned on prior tasks. This enables us to study in detail which features and at which depth transfer actually occurs. We explored two related methods: an intuitive, but slow method based on a perturbation analysis, and a faster analytical method derived from the Fisher Information [2].

Average Perturbation Sensitivity (APS). To evaluate the degree to which source columns contribute to the target task, we can inject Gaussian noise at isolated points in the architecture $\left( \mathrm { e . g . ~ a } \right.$ given layer of a single column) and measure the impact of this perturbation on performance. A significant drop in performance indicates that the final prediction is heavily reliant on the feature map or layer. We find that this method yields similar results to the faster Fisher-based method presented below. We thus relegate details and results of the perturbation analysis to the appendix.

Average Fisher Sensitivity (AFS). We can get a local approximation to the perturbation sensitivity by using the Fisher Information matrix [2]. While the Fisher matrix is typically computed with respect to the model parameters, we compute a modified diagonal Fisher $\hat { F }$ of the network policy π

with respect to the normalized activations 2 at each layer ${ \hat { h } } _ { i } ^ { ( k ) }$ . For convolutional layers, we define $\hat { F }$ to implicitly perform a summation over pixel locations. $\hat { F }$ can be interpreted as the sensitivity of the policy to small changes in the representation. We define the diagonal matrix ${ \hat { F } } ,$ , having elements $\hat { F } ( m , m )$ , and the derived Average Fisher Sensitivity (AFS) of feature m in layer i of column k as:

$$
\hat {F} _ {i} ^ {(k)} = \mathbb {E} _ {\rho (s, a)} \left[ \frac {\partial \log \pi}{\partial \hat {h} _ {i} ^ {(k)}} \frac {\partial \log \pi}{\partial \hat {h} _ {i} ^ {(k)}} ^ {T} \right] \qquad \mathrm {A F S} (i, k, m) \qquad = \frac {\hat {F} _ {i} ^ {(k)} (m , m)}{\sum_ {k} \hat {F} _ {i} ^ {(k)} (m , m)}
$$

where the expectation is over the joint state-action distribution $\rho ( s , a )$ induced by the progressive network trained on the target task. In practice, it is often useful to consider the AFS score per-layer $\begin{array} { r } { \mathrm { A F S } ( i , k ) = \sum _ { m } \mathrm { A F S } ( i , \breve { k } , m ) } \end{array}$ , i.e. summing over all features of layer i. The AFS and APS thus estimate how much the network relies on each feature or column in a layer to compute its output.

# 4 Related Literature

There exist many different paradigms for transfer and multi-task reinforcement learning, as these have long been recognized as critical challenges in AI research [15, 19, 20]. Many methods for transfer learning rely on linear and other simple models (e.g. [18]), which is a limiting factor to their applicability. Recently, there have been new methods proposed for multi-task or transfer learning with deep RL: [22, 17, 14]. In this work we present an architecture for deep reinforcement learning that in sequential task regimes that enables learning without forgetting while supporting individual feature transfer from previous learned tasks.

Pretraining and finetuning was proposed in [7] and applied to transfer learning in [4, 11], generally in unsupervised-to-supervised or supervised-to-supervised settings. The actor-mimic approach [14] applied these principles to reinforcement learning, by fine-tuning a DQN multi-task network on new Atari games and showing that some responded with faster learning, while others did not. Progressive networks differ from the finetuning direction substantially, since capacity is added as new tasks are learned.

Progressive nets are related to the incremental and constructive architectures proposed in neural network literature. The cascade-correlation architecture was designed to eliminate forgetting while incrementally adding and refining feature extractors [6]. Auto-encoders such as [24] use incremental feature augmentation to track concept drift, and deep architectures such as [16] have been designed that specifically support feature transfer. More recently, in [1], columns are separately trained on individual noise types, then linearly combined, and [5] use columns for image classification. The block-modular architecture of [21] has many similarities to our approach but focuses on a visual discrimination task. The progressive net approach, in contrast, uses lateral connections to access previously learned features for deep compositionality. It can be used in any sequential learning setting but is especially valuable in RL.

# 5 Experiments

We evaluate progressive networks across three different RL domains. First, we consider synthetic versions of Pong, altered to have visual or control-level similarities. Next, we experiment broadly with random sequences of Atari games and perform a feature-level transfer analysis. Lastly, we demonstrate performance on a set of 3D maze games. Fig. 2 shows examples from selected tasks.

# 5.1 Setup

We rely on the Async Advantage Actor-Critic (A3C) framework introduced in [13]. Compared to DQN [12], the model simultaneously learns a policy and a value function for predicting expected future rewards. A3C is trained on CPU using multiple threads and has been shown to converge faster than DQN on GPU. This made it a more natural fit for the large amount of sequential experiments required for this work.

![](images/2550dc9b47701d102d0a42e3d2caa9da962d5369a7fcf857f38301986ad11e24.jpg)

![](images/16a2f7a5324ab3fd3f467067e12b63a08f4ebdae8ffb1f893bcd46f350be03e5.jpg)  
(a) Pong variants

![](images/5e6cf6c436155fd68b3a340950512880c93c5f820def5c8fa2a08460876866da.jpg)  
(b) Labyrinth games

![](images/6996d03652ca18a45b093188c16f4e3601c3360517cd33034667e2dbd7f7660f.jpg)

![](images/99a53df8c633d4303532b919a0d7be2e89ace0d31555aa74455415565a51a63f.jpg)

![](images/94ff11ad3f7001b66f5c09bb97758dcb1d63b64548e4d9dfeba16c5cc573ad9a.jpg)  
(c) Atari games   
Figure 2: Samples from different task domains: (a) Pong variants include flipped, noisy, scaled, and recoloured transforms; (b) Labyrinth is a set of 3D maze games with diverse level maps and diverse positive and negative reward items; (c) Atari games offer a more challenging setting for transfer.

We report results by averaging the top 3 out of 25 jobs, each having different seeds and random hyper-parameter sampling. Performance is evaluated by measuring the area under the learning curve (average score per episode during training), rather than final score. The transfer score is then defined as the relative performance of an architecture compared with a single column baseline, trained only on the target task (baseline 1). We present transfer score curves for selected source-target games, and summarize all such pairs in transfer matrices. Models and baselines we consider are illustrated in Figure 3. Details of the experimental setup are provided in section 3 of the Appendix.

![](images/e3dddb3dabda11f3531b16d874e76b9e70ec86e8dc6b9f91aef937f9c83d2e88.jpg)

![](images/a97d88d2db9dd3f836f4d48b80f381a2b755944d62e9258feff8390f0f9575f3.jpg)

![](images/b15eb6fc0fbe43b66522e34179b6cea5b498b3fbfd0a24e7526a145db160eec6.jpg)

![](images/d43368910f4283bf6228e3a8c5fb5eae4dd072e56b39f329b4b9b915027de717.jpg)

![](images/01867fbf0c7afe5eecf14107c63560250833529d7e0cf742dab756ea0cd98bcd.jpg)

![](images/28840dcbcd1b5641bb255fb422ed49f8effbc4b6bb622cd0b32cd40e1cfb0dc7.jpg)

![](images/21deba13870464beff3d0c20aeeacac10214c74da64feb49796c86ffe018cb63.jpg)  
Figure 3: Illustration of different baselines and architectures. Baseline 1 is a single column trained on the target task; baseline 2 is a single column, pretrained on a source task and finetuned on the target task (output layer only); baseline 3 is the same as baseline 2 but the whole model is finetuned; and baseline 4 is a 2 column progressive architecture, with previous column(s) initialized randomly and frozen.

# 5.2 Pong Soup

The first evaluation domain is a set of synthetic variants of the Atari game of Pong ("Pong Soup") where the visuals and gameplay have been altered, thus providing a setting where we can be confident that there are transferable aspects of the tasks. The variants are Noisy (frozen Gaussian noise is added to the inputs); Black (black background); White (white background); Zoom (input is scaled by 75% and translated); V-flip, H-flip, and VH-flip (input is horizontally and/or vertically flipped). Example frames are shown in Fig. 2. The results of training two columns on the Pong variants, including all relevant baselines are shown in Figure 4. Transfer scores are summarized over all target tasks in Table 1.

![](images/cce7cbd16766d40e3a2d00e0c2ae1fd280d17a43b8c190dcc8debfcdf8cf2be1.jpg)  
(a)

![](images/5d4960dc582d56e32264dbf99df511db6bded5993d9d65b88193eb7a67ab6095.jpg)  
(b)

![](images/00ce8b83d57ceac5781c26d567568c5365f5c1df7b73eeaa14c6d4742d562f4e.jpg)  
Figure 4: (a) Transfer matrix. Colours indicate transfer scores (clipped at 2). For progressive nets, the first column is trained on Pong, Noisy, or H-flip (table rows); the second column is trained on each of the other pong variants (table columns). (b) Example learning curves.

We can make several observations from these results. Baseline 2 (single column, only output layer is finetuned; see Fig. 3) fails to learn the target task in most experiments and thus has negative transfer. This approach is quite standard in supervised learning settings, where features from ImageNet-trained nets are routinely repurposed for new domains. As expected, we observe high positive transfer with baseline 3 (single column, full finetuning), a well established paradigm for transfer. Progressive networks outperform this baseline however in terms of both median and mean score, with the difference being more pronounced for the latter. As the mean is more sensitive to outliers, this suggests that progressive networks are better able to exploit transfer when transfer is possible (i.e. when source and target domains are compatible). Fig. 4 (b) lends weight to this hypothesis, where progressive networks are shown to significantly outperform the baselines for particular game pairs. Progressive nets also compare favourably to baseline 4, confirming that progressive nets are indeed taking advantage of the features learned in previous columns.

# Detailed analysis

![](images/8e20aa79ef98bc972526bcfa1d67d4b7aa65e6fbbdaa0458fcf24c4834b47516.jpg)

![](images/aa166d3ca6440f32e65af4d1ad5460c960c0265cbd2c5999d54eff972fa748be.jpg)

![](images/65a773235e56bbc206cda6997edf5916d2b5ecc33f7d4609116a8ba577cc061f.jpg)

![](images/a31cf36a7768462814f4fb888a548b41f26e8e4060b0e1e783e1aa80de368674.jpg)  
(b)

![](images/d42b84190476aacda27b51629fb39922a06c14259757c11f1a1be82309f9e2c3.jpg)

![](images/08ccf76caa91e3dd403a3e79838f0f9f15b578d37a8ac4c152965f37c134d292.jpg)  
(c)

![](images/d5751839f02f08e27fb12900de79e90c31f400c14effb1f889c31e1813e1fda0.jpg)  
Figure 5: (a) Transfer analysis for 2-column nets on Pong variants. The relative sensitivity of the network’s outputs on the columns within each layer (the AFS) is indicated by the darkness of shading. (b) AFS values for the 8 feature maps of conv. 1 of a 1-column Pong net. Only one feature map is effectively used by the net; the same map is also used by the 2-column versions. Below: spatial filter components (red = positive, blue = negative). (c) Activation maps of the filter in (b) from example states of the four games.

We use the metric derived in Sec. 3 to analyse what features are being transferred between Pong variants. We see that when switching from Pong to H-Flip, the network reuses the same components of low and mid-level vision (the outputs of the two convolutional layers; Figure 5a). However, the fully connected layer must be largely re-learned, as the policy relevant features of the task (the relative locations/velocities of the paddle and ball) are now in a new location. When switching from Pong to Zoom, on the other hand, low-level vision is reused for the new task, but new mid-level vision features are learned. Interestingly, only one low-level feature appears to be reused: (see Fig. 5b): this is a spatio-temporal filter with a considerable temporal DC component. This appears sufficient for detecting both ball motion and paddle position in the original, flipped, and zoomed Pongs.

Finally, when switching from Pong to Noisy, some new low-level vision is relearned. This is likely because the first layer filter learned on the clean task is not sufficiently tolerant to the added noise. In contrast, this problem does not apply when moving from Noisy to Pong (Figure 5a, rightmost column), where all of vision transfers to the new task.

# 5.3 Atari Games

We next investigate feature transfer between randomly selected Atari games [3]. This is an interesting question, because the visuals of Atari games are quite different from each other, as are the controls and required strategy. Though games like Pong and Breakout are conceptually similar (both involve hitting a ball with a paddle), Pong is vertically aligned while Breakout is horizontal: a potentially insurmountable feature-level difference. Other Atari game pairs have no discernible overlap, even at a conceptual level.

To this end we start by training single columns on three source games (Pong, River Raid, and Seaquest) 3 and assess if the learned features transfer to a different subset of randomly selected target games (Alien, Asterix, Boxing, Centipede, Gopher, Hero, James Bond, Krull, Robotank, Road Runner, Star Gunner, and Wizard of Wor). We evaluate progressive networks with 2, 3 and 4 columns,

![](images/f8151925a15df6273145d9e6b5cf2db42eb0d4705af1f62b99cb813fc318bf5a.jpg)  
(b)

![](images/a999886c4f5c61b94b55942d19b5546c7d503b575b5aad3c0bf0f9fa302d6c5c.jpg)  
Figure 6: Transfer scores and example learning curves for Atari target games, as per Figure 4.

Table 1: Transfer percentages in three domains. Baselines are defined in Fig. 3.   

<table><tr><td></td><td colspan="2">Pong Soup</td><td colspan="2">Atari</td><td colspan="2">Labyrinth</td></tr><tr><td></td><td>Mean (%)</td><td>Median (%)</td><td>Mean (%)</td><td>Median (%)</td><td>Mean (%)</td><td>Median (%)</td></tr><tr><td>Baseline 1</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr><tr><td>Baseline 2</td><td>35</td><td>7</td><td>41</td><td>21</td><td>88</td><td>85</td></tr><tr><td>Baseline 3</td><td>181</td><td>160</td><td>133</td><td>110</td><td>235</td><td>112</td></tr><tr><td>Baseline 4</td><td>134</td><td>131</td><td>96</td><td>95</td><td>185</td><td>108</td></tr><tr><td>Progressive 2 col</td><td>209</td><td>169</td><td>132</td><td>112</td><td>491</td><td>115</td></tr><tr><td>Progressive 3 col</td><td>222</td><td>183</td><td>140</td><td>111</td><td>—</td><td>—</td></tr><tr><td>Progressive 4 col</td><td>—</td><td>—</td><td>141</td><td>116</td><td>—</td><td>—</td></tr></table>

comparing to the baselines of Figure 3). The transfer matrix and selected transfer curves are shown in Figure 6, and the results summarized in Table 1.

Across all games, we observe from Fig. 6, that progressive nets result in positive transfer in 8 out of 12 target tasks, with only two cases of negative transfer. This compares favourably to baseline 3, which yields positive transfer in only 5 of 12 games. This trend is reflected in Table 1, where progressive networks convincingly outperform baseline 3 when using additional columns. This is especially promising as we show in the Appendix that progressive network use a diminishing amount of capacity with each added column, pointing a clear path to online compression or pruning as a means to mitigate the growth in model size.

Now consider the specific sequence Seaquest-to-Gopher, an example of two dissimilar games. Here, the pretrain/finetune paradigm (baseline 3) exhibits negative transfer, unlike progressive networks (see Fig.6b, bottom), perhaps because they are more able to ignore the irrelevant features. For the sequence Seaquest[+River Raid][+Pong]-to-Boxing, using additional columns in the progressive networks can yield a significant increase in transfer (see Fig. 6b, top).

# Detailed Analysis

Figure 6 demonstrates that both positive and negative transfer is possible with progressive nets. To differentiate these cases, we consider the Average Fisher Sensitivity for the 3 column case (e.g., see Fig. 7a). A clear pattern emerges amongst these and other examples: the most negative transfer coincides with complete dependence on the convolutional layers of the previous columns, and no learning of new visual features in the new column. In contrast, the most positive transfer occurs when the features of the first two columns are augmented by new features. The statistics across all 3-column nets (Figure 7b) show that positive transfer in Atari occurs at a "sweet spot" between heavy reliance on features from the source task, and heavy reliance on all new features for the target task.

At first glance, this result appears unintuitive: if a progressive net finds a valuable feature set from a source task, shouldn’t we expect a high degree of transfer? We offer two hypotheses. First, this may simply reflect an optimization difficulty, where the source features offer fast convergence to a poor local minimum. This is a known challenge in transfer learning [20]: learned source tasks confer an inductive bias that can either help or hinder in different cases. Second, this may reflect a problem of

![](images/e20a41306dc046e350561f6178a5bbc48d0f5b76b5488eeaa90641b41f87e8fa.jpg)

![](images/30bced5872a130525012685d704df3c607758a6dafb3b589915c591192128768.jpg)  
Figure 7: (a) AFS scores for 3-column nets with lowest (left) and highest (right) transfer scores on the 12 target Atari games. (b) Transfer statistics across 72 three-column nets, as a function of the mean AFS across the three convolutional layers of the new column (i.e. how much new vision is learned).

exploration, where the transfered representation is "good enough" for a functional, but sub-optimal policy.

# 5.4 Labyrinth

The final experimental setting for progressive networks is Labyrinth, a 3D maze environment where the inputs are rendered images granting partial observability and the agent outputs discrete actions, including looking up, down, left, or right and moving forward, backwards, left, or right. The tasks as well as the level maps are diverse and involve getting positive scores for ‘eating’ good items (apples, strawberries) and negative scores for eating bad items (mushrooms, lemons). Details can be found in the appendix. While there is conceptual and visual overlap between the different tasks, the tasks present a challenging set of diverse game elements (Figure 2).

![](images/65f62fd9435d28138203b6c7d6b275a6b0b04bb427f5d9b764775af6b2685df1.jpg)

![](images/2288cae2521d06d8ca0802dcb6e4997b84b69442176305d10f2c9f44070e3f39.jpg)

![](images/2fbfb8a1d12d2af3dc2a0b773f1a79c8eff2414f5ecc7a3cbd4a27216b8cfc43.jpg)  
Figure 8: Transfer scores and example learning curves for Labyrinth tasks. Colours indicate transfer (clipped at 2). The learning curves show two examples of two-column progressive performance vs. baselines 1 and 3.

As in the other domains, the progressive approach yields more positive transfer than any of the baselines (see Fig. 8a and Table 1). We observe less transfer on the Seek Track levels, which have dense reward items throughout the maze and are easily learned. Note that even for these easy cases, baseline 2 shows negative transfer because it cannot learn new low-level visual features, which are important because the reward items change from task to task. The learning curves in Fig. 8b exemplify the typical results seen in this domain: on simpler games, such as Track 1 and 2, learning is rapid and stable by all agents. On more difficult games, with more complex game structure, the baselines struggle and progressive nets have an advantage.

# 6 Conclusion

Continual learning, the ability to accumulate and transfer knowledge to new domains, is a core characteristic of intelligent beings. Progressive neural networks are a stepping stone towards continual learning, and this work has demonstrated their potential through experiments and analysis across three RL domains, including Atari, which contains orthogonal or even adversarial tasks. We believe that we are the first to show positive transfer in deep RL agents within a continual learning framework. Moreover, we have shown that the progressive approach is able to effectively exploit transfer for compatible source and task domains; that the approach is robust to harmful features learned in incompatible tasks; and that positive transfer increases with the number of columns, thus corroborating the constructive, rather than destructive, nature of the progressive architecture.

# References

[1] Forest Agostinelli, Michael R Anderson, and Honglak Lee. Adaptive multi-column deep neural networks with application to robust image denoising. In Advances in Neural Information Processing Systems, 2013.   
[2] Shun-ichi Amari. Natural gradient works efficiently in learning. Neural Computation, 1998.   
[3] M. G. Bellemare, Y. Naddaf, J. Veness, and M. Bowling. The arcade learning environment: An evaluation platform for general agents. Journal of Artificial Intelligence Research (JAIR), 47:253–279, 2013.   
[4] Yoshua Bengio. Deep learning of representations for unsupervised and transfer learning. In JMLR: Workshop on Unsupervised and Transfer Learning, 2012.   
[5] Dan C. Ciresan, Ueli Meier, and Jürgen Schmidhuber. Multi-column deep neural networks for image classification. In Conf. on Computer Vision and Pattern Recognition, 2012.   
[6] Scott E. Fahlman and Christian Lebiere. The cascade-correlation learning architecture. In Advances in Neural Information Processing Systems, 1990.   
[7] G. E. Hinton and R. R. Salakhutdinov. Reducing the dimensionality of data with neural networks. Science, 313(5786):504–507, July 2006.   
[8] Goeff Hinton, Oriol Vinyals, and Jeff Dean. Distilling the knowledge in a neural network. CoRR, abs/1503.02531, 2015.   
[9] Yann LeCun, John S. Denker, and Sara A. Solla. Optimal brain damage. In Advances in Neural Information Processing Systems, 1990.   
[10] Min Lin, Qiang Chen, and Shuicheng Yan. Network in network. In Proc. of Int’l Conference on Learning Representations (ICLR), 2013.   
[11] G. Mesnil, Y. Dauphin, X. Glorot, S. Rifai, Y. Bengio, I. Goodfellow, E. Lavoie, X. Muller, G. Desjardins, D. Warde-Farley, P. Vincent, A. Courville, and J. Bergstra. Unsupervised and transfer learning challenge: a deep learning approach. In JMLR W& CP: Proc. of the Unsupervised and Transfer Learning challenge and workshop, volume 27, 2012.   
[12] V. Mnih, Kk Kavukcuoglu, D. Silver, A. Rusu, J. Veness, M. Bellemare, A. Graves, M. Riedmiller, A. Fidjeland, G. Ostrovski, S. Petersen, C. Beattie, A. Sadik, I. Antonoglou, H. King, D. Kumaran, D. Wierstra, S. Legg, and D. Hassabis. Human-level control through deep reinforcement learning. Nature, 518(7540):529–533, 2015.   
[13] Volodymyr Mnih, Adrià Puigdomènech Badia, Mehdi Mirza, Alex Graves, Timothy P. Lillicrap, Tim Harley, David Silver, and Koray Kavukcuoglu. Asynchronous methods for deep reinforcement learning. In Int’l Conf. on Machine Learning (ICML), 2016.   
[14] Emilio Parisotto, Lei Jimmy Ba, and Ruslan Salakhutdinov. Actor-mimic: Deep multitask and transfer reinforcement learning. In Proc. of Int’l Conference on Learning Representations (ICLR), 2016.   
[15] Mark B. Ring. Continual Learning in Reinforcement Environments. R. Oldenbourg Verlag, 1995.   
[16] Artem Rozantsev, Mathieu Salzmann, and Pascal Fua. Beyond sharing weights for deep domain adaptation. CoRR, abs/1603.06432, 2016.   
[17] A. Rusu, S. Colmenarejo, Ç. Gülçehre, G. Desjardins, J. Kirkpatrick, R. Pascanu, V. Mnih, K. Kavukcuoglu, and R. Hadsell. Policy distillation. abs/1511.06295, 2016.   
[18] Paul Ruvolo and Eric Eaton. Ella: An efficient lifelong learning algorithm. In Proceedings of the 30th International Conference on Machine Learning (ICML-13), June 2013.   
[19] Daniel L. Silver, Qiang Yang, and Lianghao Li. Lifelong machine learning systems: Beyond learning algorithms. In AAAI Spring Symposium: Lifelong Machine Learning, 2013.   
[20] Matthew E. Taylor and Peter Stone. An introduction to inter-task transfer for reinforcement learning. AI Magazine, 32(1):15–34, 2011.   
[21] Alexander V. Terekhov, Guglielmo Montone, and J. Kevin O’Regan. Knowledge Transfer in Deep Block-Modular Neural Networks, pages 268–279. Springer International Publishing, Cham, 2015.   
[22] C. Tessler, S. Givony, T. Zahavy, D. J. Mankowitz, and S. Mannor. A Deep Hierarchical Approach to Lifelong Learning in Minecraft. ArXiv e-prints, 2016.   
[23] Jason Yosinski, Jeff Clune, Yoshua Bengio, and Hod Lipson. How transferable are features in deep neural networks? In Advances in Neural Information Processing Systems, pages 3320–3328, 2014.   
[24] Guanyu Zhou, Kihyuk Sohn, and Honglak Lee. Online incremental feature learning with denoising autoencoders. In Proc. of Int’l Conf. on Artificial Intelligence and Statistics (AISTATS), pages 1453–1461, 2012.

# Supplementary Material

# A Perturbation Analysis

We explored two related methods for analysing transfer in progressive networks. One based on Fisher information yields the Average Fisher Sensitivity (AFS) and is described in Section 3 of the paper. We describe the second method based on perturbation analysis in this appendix, as it proved too slow to use at scale. Given its intuitive appeal however, we provide details of the method along with results on Pong Variants (see Section 5.2), as a means to corroborate the AFS score.

Our perturbation analysis aims to estimate which components of the source columns materially contribute to the performance of the final column on the target tasks. To this end, we injected Gaussian noise into each of the (post-ReLU) hidden representations, with a new sample on every forward pass, and calculated the average effect of these perturbations on the game score over 10 episodes. We did this at a coarse scale, by adding noise across all features of a given layer, though a fine scale analysis is also possible per feature (map). In order to be invariant to any arbitrary scale factors in the network weights, we scale the noise variance proportional to the variance of the activations in each feature map and fully-connected neuron. Scaling the variance in this manner is analogous to computing the Fisher w.r.t. normalized activations for the AFS score.

![](images/3b89cfd4f3f783bf012de06e46bbc8b4c6d4864b7f7c55cd5f76aa8eb90b754f.jpg)  
(a)

![](images/0597653fc6506439c5d9288811c5d186711b223ff67c84901b4cdb53f8e50722.jpg)

![](images/e6d6b2c3a28dc55375c154d0c414db1a4ca683ced4341106266ac42a05eaabc5.jpg)  
(c)   
Figure 9: (a) Perturbation analysis for the two second-layer convolutional representations in the two columns of the Pong/Pong-noise net. Blue: adding noise to second convolutional layer from column 1; green: from column 2. Grey line determines critical noise magnitude for each representation, $\sigma _ { i } ^ { 2 }$ . (b-c) Comparison of per-layer sensitivities obtained using the APS method (b) and the AFS method (c; as per main text). These are highly similar.

Define $\Lambda _ { i } ^ { ( k ) } = 1 / \sigma _ { i } ^ { 2 ( k ) }$ as the precision of the noise injected at layer i of column k, which results in a 50% drop in performance. The Average Perturbation Sensitivity (APS) for this layer is simply:

$$
\operatorname {A P S} (i, k) = \frac {\Lambda_ {i} ^ {(k)}}{\sum_ {k} \Lambda_ {i} ^ {(k)}} \tag {3}
$$

Note that this value is normalized across columns for a given layer. The APS score can thus be interpreted as the responsibility of each column in a given layer to final performance. The APS score of 2-column progressive networks trained on Pong Variants is shown in Fig9 (b). These clearly corroborate the AFS shown in (c).

# B Compressibility of Progressive Networks

As described in the main text, one of the limitations of progressive networks is the growth in the size of the network with added tasks. In the basic approach we pursue in the main text, the number of hidden units and feature maps grows linearly with the number of columns, and the number of parameters grows quadratically.

Here, we sought to determine the degree to which this full capacity is actually used by the network. We leveraged the Average Fisher Sensitivity measure to study how increasing the number of columns in the Atari task set changes the need for additional resources. In Figure 10a, we measure the average fractional use of existing

feature maps in a given layer (here, layer 2). We do this for each network by concatenating the per-feature-map AFS values from all source columns in this layer, sorting the values to produce a spectrum, and then averaging across networks. We find that as the number of columns increases, the average spectrum becomes sparser: the network relies on a smaller proportion of features from the source columns. Similar results were found for all layers.

Similarly, in Figure 10b, we measure the capacity required in the final added column as a function of the total number of columns. Again, we measure the spectrum of AFS values in an example layer, but here from only the final column. As the progressive network grows, the new column’s features are both less important overall (indicated by the declining area under the graph), and have a sparser AFS spectrum. Combined, these results suggest that significant pruning of lateral connections is possible, and the quadratic growth of parameters might be contained.

![](images/caa7e41741977805aab9c7546e322733fcf4242a4f65178c93018b8cc40942fc.jpg)  
(a)

![](images/d23349006c13a7c7d835a26106f8335ff609a7675347e86b5741d3142bca0a8e.jpg)  
(b)   
Figure 10: (a) Spectra of AFS values (for layer 2) across all feature maps from source columns, for the Atari dataset. The spectra show the range of AFS values, and are averaged across networks. While the 2 column / 3 column / 4 column nets all have different values of $N _ { m a p s }$ (here, 12, 24, and 36 respectively), these have been dilated to fit the same axis to show the proportional use of these maps. (b) Spectra of AFS values (for layer 2) for the feature maps from only the final column.

# C Setup Details

In our grid we sample hyper-parameters from categorical distributions:

• Learning rate was sampled from $\{ 1 0 ^ { - 3 } , 5 \cdot 1 0 ^ { - 4 } , 1 0 ^ { - 4 } \}$ .   
• Strength of the entropy regularization from $\{ 1 0 ^ { - 2 } , 1 0 ^ { - 3 } , 1 0 ^ { - 4 } \}$   
• Gradient clipping cut-off from {20, 40}   
• scalar multiplier on the lateral feature is initialized randomly to one from $\{ 1 , 1 0 ^ { - 1 } , 1 0 ^ { - 2 } \}$

For the Atari experiments we used a model with 3 convolutional layers followed by a fully connected layer and from which we predict the policy and value function. The convolutional layers are as follows. All have 12 feature maps. The first convolutional layer has a kernel of size 8x8 and a stride of 4x4. The second layer has a kernel of size 4 and a stride of 2. The last convolutional layer has size 3x4 with a stride of 1. The fully connected layer has 256 hidden units.

Learning follows closely the paradigm described in [13]. We use 16 workers and the same RMSProp algorithm without momentum or centring of the variance. The score for each point of a training curve is the average over all the episodes the model gets to finish in 25e4 environment steps.

The whole experiments are run for a maximum of 1.6e8 environment step. The agent has an action repeat of 4 as in [13], which means that for 4 consecutive steps the agent will use the same action picked at the beginning of the series. For this reason through out the paper we actually report results in terms of agent perceived steps rather than environment steps. That is, the maximal number of agent perceived step that we do for any particular run is 4e7.

# D Learning curves

Figure 11 shows training curves for all the target games in the Atari domain. We plot learning curves for two column, three column and four column progressive networks alongside Baseline 3 (gray dashed line), a model pretrained on Seaquest and then finetuned on the particular target game and Baseline 1 (gray dotted line), where a single column is trained on the source game Seaquest.

We can see that overall baseline 3 performs well. However there are situations when having features learned from more previous task actually helps with transfer (e.g. when target game is Boxing).

![](images/23efecea04903b00fb527b857c03bf0f319fd6809ef706ab295536311a1a11d6.jpg)

![](images/da12d04e2a46f5ec55f58501e5742c0d5ebb3d3e5f5008015c072bed70cd8e47.jpg)

![](images/a6cf6487af5fbbff1ecd46afdc24e3f415da8cc05fb42f0a20bb15a3aed12e67.jpg)

![](images/e4a71ba58c63202cbc505139bf9c6e55261c4c40f5d9f8306647d6ac245504c9.jpg)

![](images/b84bf50363bbaf15e33fd1826e2944b864d8a01f8ec55dfe1ee623affb24f7da.jpg)

![](images/c4c1b9b5530ab5e02c6daed7aeafc32dad2ce75ed0a5230c38ee8bdf29849661.jpg)

![](images/f866d93c3023051bfee5aa0976fa8e59e2153809ce505407b7622a49bb7ae992.jpg)

![](images/818915255b729b72ae105fa9139422770132ada0f78ef256f6456015cf2c4917.jpg)

![](images/a7dafdc94f6d0447bd8efbfa36cf30ad57c215cea8b23d18a8e4ba35101a8009.jpg)

![](images/f88fa7ac3d192a744456c25d1c47bc30dd056af87baab5dd039e1a8bbbea8fa0.jpg)

![](images/39136ac0ffd32637f76f52559164cb9e3906d0736a981ddd66c4d8971858cfc1.jpg)

![](images/2e2972f40c08f60f1336f76b9be0aaa598dafe2c70f5b348c1741e94228c1db2.jpg)  
Figure 11: Training curves for transferring to the target games after seeing first Seaquest followed by River Raid and lastly Pong. For the baselines, the source game used for pretraining is Seaquest.

Figure 12 shows how two-column progressive networks perform as compared to Baseline 3 (gray dashed line), a model pretrained on the source game, here standard Pong, and then finetuned on a particular target game, and Baseline 1 (black dotted line), where a single column is trained on standard Pong. Figure 13 shows two-column progressive networks and baselines on Labyrinth tasks; the source game was Maze Y.

# E Labyrinth

Section 5.4 evaluates progressive networks on foraging tasks in complex 3D maze environments. Positive rewards are given to the agent for collecting apples and strawberries, and negative rewards for mushrooms and lemons. Episodes terminate when either all (positive) rewards are collected, or after a fixed time interval.

Levels differ in their maze layout, the type of items present and the sparsity of the reward structure. The levels we employed can be characterized as follows:

• Seek Track 1: simple corridor with many apples   
• Seek Track 2: U-shaped corridor with many strawberries   
• Seek Track 3: Ω-shaped, with $9 0 ^ { o }$ turns, with few apples   
• Seek Track 4: Ω-shaped, with $4 5 ^ { o }$ turns, with few apples   
• Seek Avoid 1: large square room with apples and lemons   
• Seek Avoid 2: large square room with apples and mushrooms   
• Seek Maze M : M-shaped maze, with apples at dead-ends   
• Seek Maze Y : Y-shaped maze, with apples at dead-ends

![](images/b8f0d98df970086c4299bbdfd4343c829be389cf9d839e7e20f0a3a71c0209f4.jpg)  
Target: Pong

![](images/95c016b4cf510c965fbbab267f4e0be46f55644bcb3b8eb17448e2e6168d0018.jpg)  
Target: Black

![](images/ae51f8963a2a5feddcfdd2a729b12f40a8451a4cf28107e0a8c363d463d74fff.jpg)  
Target: H-flip

![](images/42e8bfc5bb0bfa0be64e9fe70b9c054a9fd7fb91176204fd9732966a93af4923.jpg)  
Target: HV-flip

![](images/2a179dd7762c584be5c175e6a914ffe346d7523affc5e1a736fe571869bade06.jpg)  
Target: Noisy

![](images/8648dd22d60db82b775b39e05e083a6a54327840b4d4d0f4a406df78d63739cb.jpg)  
Target: V-flip

![](images/67fabbc0d0158560a774d0aa546c662bbe79a01798e48e8a210297afab92c99c.jpg)  
Target: White

![](images/8dff5a20a0b3cec3bcb588cf7b5c8ce937b14a3b6ac080348a80d184d214cc11.jpg)  
Target: Zoom   
Figure 12: Training curves for transferring to 8 target games after learning standard Pong first.

![](images/ae976302288e5e5f79a12245cca61b9eb64d5e0efbeb23ad5f6b45c340967edf.jpg)  
Target: Track 1

![](images/b452a04ba3b1e9697ebdf87981b9def1eef7156e5a10e134f9f3d5f57bf77133.jpg)  
Target: Track 2

![](images/9f4dc29c78cc78db7b9ffe0b1522b85a8c34abe03bedbab83f442165523dfd6b.jpg)  
Target: Track 3

![](images/106e85219420a1a3ff7d5c5909a66c699c9d70c8d2a6487caea1bfd2565b7c54.jpg)  
Target: Track 4

![](images/da9d113a98f9a790312511c8eab0bf48ce679a18782fb1bc6361704911310141.jpg)  
Target: Avoid 1

![](images/a4c7e007289c225530282d8034a648d6ab192ddec34b31117670d5a32fea272b.jpg)  
Target: Avoid 2

![](images/23fd7cdb6fe53f47356238c6c86f999c10a6468ea1906e37d76e1fea49976078.jpg)  
Target: Maze Y

![](images/27cf1d258ef2102417c4f58caec62be28459435c8bf3f0cf213c405f206b8cb6.jpg)  
Target: Maze M   
Figure 13: Training curves for transferring to 8 target games after learning Maze Y first.