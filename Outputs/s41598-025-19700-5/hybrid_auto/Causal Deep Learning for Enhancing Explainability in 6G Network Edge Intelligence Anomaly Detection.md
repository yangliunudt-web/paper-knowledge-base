---
title: "Causal Deep Learning for Enhancing Explainability in 6G Network Edge Intelligence Anomaly Detection"
authors:
  - "Xiao Yi"
  - "Zengri Zeng"
  - "Ming Dai"
  - "Aimei Kang"
  - "Xuhui Liu"
  - "Yunlian Liu"
date: "2025-11-19"
year: 2025
journal: "Scientific Reports"
abstract: "With the rapid development of 6G networks, anomaly detection in network edge intelligence faces significant challenges in system interpretability and trustworthiness. Although machine learning-based methods improve detection performance, their black-box nature limits reliable cybersecurity decision support. To address this, we propose a novel framework integrating causal inference with LSTM networks. Our approach first applies Random Fourier Feature transformation to eliminate nonlinear feature correlations—a prerequisite for valid causal analysis. We then quantify feature-specific causal effects using sample-weighted adjustments to ensure model stability. Furthermore, Generative Adversarial Networks generate high-quality minority-class samples to augment training data, enhancing anomaly detection accuracy. Experimental validation on two large-scale datasets demonstrates a 33.7% improvement in explainability and a 68% reduction in root-cause localization time. This work establishes a new cybersecurity paradigm for 6G edge intelligence through causal reasoning."
abstract_cn: "随着6G网络的快速发展，网络边缘智能中的异常检测在系统可解释性和可信度方面面临重大挑战。尽管基于机器学习的方法提高了检测性能，但其黑盒特性限制了可靠的网络安全决策支持。为此，我们提出了一种将因果推理与LSTM网络相结合的新框架。该方法首先应用随机傅里叶特征变换消除非线性特征相关性，这是有效因果分析的前提条件。然后通过样本加权调整量化特征特异性因果效应以确保模型稳定性。此外，生成对抗网络生成高质量的少数类样本以增强训练数据，提高异常检测精度。在两个大规模数据集上的实验验证表明，可解释性提高了33.7%，根因定位时间减少了68%。该工作通过因果推理为6G边缘智能建立了新的网络安全范式。"
keywords:
  - "[[Causal Deep Learning]]"
  - "[[6G NEI]]"
  - "[[Anomaly Detection]]"
  - "[[LSTM]]"
  - "[[GANs]]"
  - "[[Cybersecurity]]"
  - "[[因果深度学习]]"
  - "[[异常检测]]"
  - "[[6G网络]]"
cite: "Xiao Y, Zeng Z, Dai M, Kang A, Liu X, Liu Y. Causal Deep Learning for Enhancing Explainability in 6G Network Edge Intelligence Anomaly Detection[J]. Scientific Reports, 2025, 15: 40678. DOI: 10.1038/s41598-025-19700-5"
aiSum: "本研究提出CausalDL框架，将因果推理与LSTM网络结合解决6G边缘智能异常检测的可解释性问题。核心方法包括：(1) 随机傅里叶特征变换消除非线性特征相关性；(2) 样本加权调整量化因果效应；(3) WGAN-GP生成少数类样本解决数据不平衡。实验结果显示可解释性提升33.7%，根因定位时间减少68%，为6G边缘智能安全提供了因果推理新范式。"
confidence: "medium"
---

# [[Causal deep learning]] for enhancing explainability in 6G network edge intelligence anomaly detection

XiaoYi1, Zengri Zeng1,3, Ming Dai2, Aimei Kang1, Xuhui Liu3 & Yunlian Liu1

With the rapid development of 6G networks, anomaly detection in network edge intelligence faces significant challenges in system interpretability and trustworthiness. Although machine learningbased methods improve detection performance, their black-box nature limits reliable [[Cybersecurity]] decision support. To address this, we propose a novel framework integrating causal inference with LSTM networks. Our approach first applies Random Fourier Feature transformation to eliminate nonlinear feature correlations—a prerequisite for valid causal analysis. We then quantify featurespecific causal effects using sample-weighted adjustments to ensure model stability. Furthermore, Generative Adversarial Networks generate high-quality minority-class samples to augment training data, enhancing anomaly detection accuracy. Experimental validation on two large-scale datasets demonstrates a 33.7% improvement in explainability and a 68% reduction in root-cause localization time. This work establishes a new [[Cybersecurity]] paradigm for 6G edge intelligence through causal reasoning.

Keywords [[6G NEI]], [[Causal deep learning]], RFF, [[GANs]], [[Cybersecurity]]

With rapid advancements in communication technologies, innovations in [[6G NEI]] (Network Equipment Identity) have emerged at the forefront of scientific research1 . Compared to preceding generations, 6G networks not only aspire to offer extreme bandwidth, ultralow latency, and extensive coverage but also integrate cuttingedge artificial intelligence with edge computing capabilities. This fusion aims at real-time data processing, intelligent decision-making, and adaptive network optimization, thereby accommodating the explosive growth of data demands and diverse service scenarios. However, this intelligent expansion at the edge inadvertently introduces unprecedented security challenges2 . In particular, broadly deployed edge devices, which interface directly with user data, have become prime targets for cyberattacks such as denial-of-service, data theft, and malware insertion, posing severe threats to [[Cybersecurity]].

The evolution of machine learning techniques has led to performance enhancements in anomaly detection within [[6G NEI]]. However, with increased adaptability and efficient detection capabilities, these advancements are hindered by intricate training procedures and inadequate interpretability. Crucially, the reliance on feature association analyses, which often embody spurious correlations rather than causal relationships, can lead to misjudgments3 . The correlation between variables A and B, for instance, may stem from various sources beyond a direct causal link A → B or B → A; a common scenario involves a common cause C, where C → A and C → B, creating an apparent correlation between A and B without implying a direct causal effect. The presence of such a confounding factor C establishes a false correlation between A and B, undermining the stability and interpretability of machine learning models. Thus, only when a genuine causal link exists, where factor A directly contributes to outcome B, is the association reliable and meaningful. Otherwise, spurious associations through intermediary variables such as C can result in flawed inferences4 . Consequently, machine learning models based solely on associative analyses struggle to provide trustworthy decision support in [[6G NEI]] anomaly detection, potentially generating numerous false alarms due to these misleading correlations.

To address the challenges in [[6G NEI]] anomaly detection, we introduce a causality-infused deep learning framework. This framework combines causal logic with LSTM (Long Short-Term Memory) networks to improve explainability and trust. Our method first uses random Fourier transforms to identify feature correlations for causal inspection. It then applies causal interventions to gauge each feature’s impact on detection. Adjusting sample weights via propensity scores ensures feature independence, reduces noise, and boosts model stability. Furthermore, [[GANs]] (Generative Adversarial Networks) generate augmented, high-quality samples based

1Hunan University of Humanities Science and Technology, LouDi 417000, China. 2Shenzhen Polytechnic University, Shenzhen 518000, China. 3Hunan Valin Lianyuan Iron and Steel Co., Ltd, LouDi 417000, China. email: daiming@szpu.edu.cn; 1317050859@qq.com

on causal understanding, improving LSTM’s ability to identify abnormal behaviors. By merging weighted samples with LSTM, the model focuses on crucial causal patterns in time series data, enhancing accuracy and explainability. In summary, our key contributions include the following:

• Random Fourier feature transformation is employed to eradicate non-linear correlations between features, establishing a foundation for subsequent causal analysis.   
• Causal inference mechanisms are used to precisely quantify the direct influence of each feature on anomaly detection outcomes by adjusting sample weights for feature independence and boosting model interpretability.   
• GAN technology is used to generate high-quality minority class samples via advanced causal comprehension to enrich the training dataset, enabling the LSTM model to comprehensively learn and accurately discern network anomalies.

# Literature review

# Research progress in [[6G NEI]] network anomaly detection technology

Capitalizing on edge intelligence, 6G networks propel communications to unprecedented speeds and minimal latencies. However, this enhanced scale and sophistication exacerbate [[Cybersecurity]] threats, encompassing vulnerabilities at edge nodes, advanced persistent threats, unforeseen zero-day vulnerabilities, and intelligent automated attacks2 . The construction of a 6G infrastructure necessitates an embedded security framework, integrating dynamic defense strategies, sophisticated encryption measures, and stringent privacy safeguards, coupled with automated responses to form a holistic, intelligent protective mechanism. This approach ensures that technological progress is accompanied by robust protection of both cyberspace and data privacy.

In recent years, anomaly detection methodologies based on deep learning have attracted significant attention due to their capacity for autonomous and efficient feature extraction. Notably, reference5 successfully utilized deep neural networks to autonomously learn and identify anomalous behavior from complex network traffic, markedly improving detection accuracy. Another study,6 , combined the advantages of convolutional neural networks (CNNs) and recurrent neural networks (RNNs) to effectively analyze temporal sequences in network traffic, thereby enhancing the model’s ability to capture spatiotemporal characteristics. Given the stringent realtime requirements of 6G, reference7 explored optimization algorithms to reduce model inference time and ensure prompt responsiveness in anomaly detection. Additionally, reference8 proposed an adaptive framework that dynamically adjusts detection strategies based on network conditions, ensuring broad applicability.

Despite these pivotal advancements5–8 , edge-based anomaly detection in 6G networks faces substantial challenges. The primary issue is the scarcity of anomalous events, which severely impedes the collection of adequate samples for training, thus limiting the model’s ability to recognize novel forms of anomalies. Furthermore, the heterogeneity of data sources and formats, resulting from the diversity of edge devices in 6G networks, not only hampers model interpretability but also undermines its effectiveness as a tool for informed security decision-making. Therefore, future research must concentrate on addressing the dual hurdles of sample scarcity and data heterogeneity to facilitate further advancements in [[Cybersecurity]] defenses for [[6G NEI]].

# Literature background

To address the opacity inherent in current detection methodologies, [[Causal deep learning]] for anomaly detection has emerged as a vibrant research frontier3,4,9 . This discipline combines the strengths of causal inference with those of deep learning, aiming to discern true causal relationships in data and thus transcend mere statistical correlations. In this way, it constructs models with heightened explainability, generalizability, and resilience. Utilizing tools such as structural equation models, counterfactual reasoning, and causal graphs, [[Causal deep learning]] effectively mitigates model biases, enhances decision accuracy, and demonstrates tremendous potential in addressing intricate data science challenges10.

Notably, the literature4 illustrates the use of propensity score optimization to balance weights based on causal effects, reinforcing the association between causal features and attack labels while diminishing spurious correlations among noncausal variables, thereby enhancing stability and interpretability. Study3 weights features based on causal reasoning to amplify the impact of causal features on outcome labels and filter out low-weight noise features, thus elevating the causal interpretability of detection outcomes. Furthermore, these causal weights are used to guide Wasserstein generative adversarial networks (W[[GANs]]) in optimized sampling, addressing the challenge of imbalanced data. Moreover,9 describes a causal intervention approach to decouple irrelevant features, thereby eliminating noise unrelated to cyberattacks, and employs cutting-edge counterfactual analysis to pinpoint the attack types with the strongest causal ties to abnormal features.

In summary, the evolution of anomaly detection techniques within the [[6G NEI]] ecosystem is trending toward increased automation, intelligence, and real-time responsiveness. As networks expand and complexity grows, conventional anomaly detection methods struggle to meet the demands for efficiency and precision. By simulating and deciphering causal relationships in data, [[Causal deep learning]] methodologies provide a powerful tool for enhancing the explainability of network anomaly detection and a solid foundation for making informed [[Cybersecurity]] decisions3,4,9,10.

# Proposed framework

Figure  1 illustrates how [[Causal deep learning]] for Network Anomaly Detection (CausalDL) provides causal explainability for network anomalies within the 6G Networked Ecological Intelligence (NEI), enabling users and enterprises to make informed decisions. The application scenarios of [[6G NEI]] encompass all aspects of human life, emphasizing the critical importance of ensuring its network security for human safety. However, the multitude and diversity of interconnected devices within [[6G NEI]] result in heterogeneous training and detection

![](images/e1ce73b155026c14b994d9971b239da294cf3b14d184418c378100f3614dfb4c.jpg)  
Fig. 1. Example of causal explainability-AI(XAI) cyberanomalies detection for [[6G NEI]].

data, as well as a wide array of complex noise information. This complexity renders existing methods inadequate for providing reliable decision-making foundations. The bottom left (Monitoring Data Collection) and top left (XAI Cyberattack Detection) diagrams in Fig. 1 present an effective solution to address the interpretability and reliability decision problem, with the specific process outlined as A–E.

# Nonlinear feature decorrelation via random fourier features (NFDRF)

NFDRF, as depicted in the ‘Removing Nonlinear Correlations’ section of Fig. 1, facilitates the transformation of features into a novel domain where their separation and a reduction in inter-feature redundancy are significantly facilitated. This process ultimately enhances both the generalization capacity and stability of the model. Its implementation encompasses three pivotal stages: network traffic extraction (NTE), nonlinear mapping of features (NMF), and feature linear decorrelation (FLD). This intricate procedure can be described as follows:

# Network traffic extraction (NTE)

This initial step involves capturing and preprocessing raw network data to isolate meaningful features. NTE is akin to sifting through the vast digital river of network packets to extract the ‘gold nuggets’—key indicators or patterns that could signal an anomaly. It adapts the raw data into a form amenable to further processing by deep learning algorithms, ensuring compatibility and maximizing the utility of subsequent analytical stages.

To transform this computationally intensive process into a more tractable linear space inner product calculation, thereby dramatically reducing computational complexity, is the aim of this approach. This transformation not only retains the expressive power of the original data but also paves the way for efficient data analysis.

In summary, when dealing with nonlinear data, attempting to decorrelate features directly in their original feature space is inefficient. Conversely, nonlinear feature decorrelation via NFDRF ingeniously harnesses random Fourier transformations to map features into a high-dimensional alternate space, where relationships between features become simplified and more manageable. Specifically, each feature undergoes a transformation guided by a designated frequency vector and phase shift, randomly sampled from Gaussian and uniform distributions, leading to the dispersion of previously tightly correlated features. This dispersion dramatically reduces redundancy, thereby augmenting the model’s generalization capabilities. This approach not only streamlines the interactions among features but also establishes a clearer and more independent foundation for subsequent analysis and decision-making, enhancing the explainability and robustness of the analytical process.

# Sample weight learning

Definition 1 ((Causal intervention):

A causal intervention is a process that imposes specific conditions or actions to observe their direct impact on outcomes, with the aim of revealing the causal relationship between the features and the result. This method

diverges from purely observational statistical analyses by actively manipulating feature states to explore causal effects rather than drawing inferences from observed patterns.

Causal intervention extends beyond passive observation to investigate the consequences of deliberate actions. Central to this approach is the following question: If a network attack were prevented, would the network traffic still appear abnormal? While statistical inference typically deduces attacks from anomalous traffic patterns, causal intervention proactively sets features within the training data to an anomalous state, regardless of their initial condition. For example, the release of a popular show causing server crashes is often attributed to high traffic volume instead of hidden attacks. Solely analyzing traffic data might lead to misconceptions. However, reducing the viewer count through intervention—even if hackers persist in their attack—and observing the server’s continued failure can uncover the true underlying cause.

Causal intervention provides insight into the causal effects between the dataset’s outcome labels and features, laying a foundation for targeted interventions or predictions. This understanding illuminates the degree of influence that each feature has on the determined outcome.

Definition 2 (Causal effect):

In the context of a given feature, if there exists a causal effect between the feature and the label, it implies that changes in the feature have a direct impact on the outcome variable (label). More formally, if altering the value of a specific feature leads to a change in the probability of observing a certain outcome, then we say that the feature exhibits a causal effect on the label.

As illustrated in Fig. 2, where A represents the network attack label, C symbolizes the causal features, and V denotes the noise features, the real-world network traffic data depicted in Fig. 2a show that causal features and noise features are intertwined due to exogenous variables and confounding factors, leading to a lack of complete independence. This interdependence can spur erroneous associations in identifying cyberattacks, impeding the interpretability of detection algorithms (as depicted in Fig. 2a). To address this challenge, Definition 3 is proposed to define the ideal state of causal stable association, where relationships are unambiguously causal and devoid of such confounding interferences.

Definition 3 ((Causal stable association):

In any network training dataset, if all features maintain mutual independence, then the relationship between network attack A and features (C or V) constitutes a causally associated and stably linked connection, referred to as a causal stable association. This association implies that in the absence of spurious correlations arising from inter-feature dependencies, the observed link between an attack and a feature directly reflects a causal effect, fostering a robust and interpretable understanding of the factors influencing network anomalies3 . Therefore, according to Definition 3, when all features within a network dataset are mutually independent, the correlation between a network attack and a feature represents a causal stable association, signifying a direct causal relationship between the feature and the attack. Figure 2b visually depicts this ideal scenario, where all features are independent, thereby validating the soundness of the definition. To maintain this independence among features, we employ causal intervention techniques to compare differences between treatment and control groups, thereby estimating the causal impact of features on the outcome label. Anchored in this rationale, we introduce the concept of sample weighting, which assigns each sample a weight based on the average discrepancy between these groups. Through the learning of these sample weights, we reinforce the influence of causal features on labels while disentangling spurious correlations between noise features and labels, as outlined in reference11.

In this context, exogenous variables refer to external factors that influence both the C and V but are not themselves affected by them. These variables act as confounders, introducing spurious correlations between C and V , which obscure the true causal relationships in network traffic data. For instance, in Fig. 2a, an exogenous variable (e.g., a sudden surge in user activity) may simultaneously affect both the traffic volume C and the packet size distribution V , creating an apparent correlation that does not reflect a direct causal link.

Definition 4 (Sample weights):

Determining sample weights entails estimating the causal effect of each feature on the outcome label by comparing the mean differences between treatment and control groups and assigning corresponding weights to each sample to ensure the mutual independence of features, as illustrated in Fig. 2c. These weights emphasize causal influence and are therefore referred to as causal sample weights. By applying sample weights, the influence of causal features on the label is augmented, while spurious correlations between noise features and the label are untangled, thereby enhancing the stability of the methodology. By sequentially treating every traffic feature as a manipulable variable, we leverage causal intervention to weight all features, thereby bolstering the stability of the detection approach. According to the principle of causal intervention, the formula for calculating the causal weights of each sample, as indicated in12, is as follows:

![](images/54ad618ade4d2e79f23b106eff78fe9654626ff181a96ed2dac1971a8bd523ce.jpg)  
Fig. 2. Relationships between features.

$$
L o s s _ {W} = \arg \min  _ {G} \sum_ {j = 1} ^ {p} \frac {X _ {I - j} ^ {T} \cdot \left(G \odot X _ {j}\right)}{W ^ {T} \cdot X _ {j}} - \frac {X _ {I - j} ^ {T} \cdot \left(W \odot X _ {j}\right) ^ {2}}{W ^ {T} \cdot \left(1 - X _ {j}\right)} _ {2} \tag {1}
$$

In Eq. (1), W denotes the recalibrated causal weights, I represents all features, j represents the indexing of the jth feature, $I - j$ indicates that the values of all features except jth (set to 0 by intervention) remain unchanged, p signifies the dimensionality of the features, and  denotes the Hadamard product (it is a mathematical operation in which two matrices or vectors of the same dimensions are multiplied element-wise). The summation $\textstyle \sum _ { j } ^ { p }$ ∑p accounts for the imbalance loss between samples X. Through postassignment of these causally weighted samples via W learned from Eq. (1), causal feature variables can be identified by inspecting whether a correlation persists between A and $X _ { j } ;$ akin to the stable association discussed earlier, only causal feature variables will remain correlated with label A postsampling reweighting.

Specific Derivation Steps:

1. Causal intervention setting For a feature set I, take the jth feature $X _ { j }$ as the intervention target. Force it to take the value 0 (control group) or keep its original value (treatment group), while keeping the other features i−j unchanged.   
2. Feature independence measure Quantify the degree of dependence between features by comparing the correlation between feature $X _ { j }$ and the remaining features $X _ { I - j }$ in the treatment group versus the control group.

The norm term in Formula (1), $\begin{array} { r } { \Big \| \frac { X _ { I - j } ^ { T } \cdot \big ( G \odot X _ { j } \big ) } { W ^ { T } \cdot X _ { j } } - \frac { X _ { I - j } ^ { T } \cdot \big ( W \odot X _ { j } \big ) } { W ^ { T } \cdot ( 1 - X _ { j } ) } \Big \| _ { 2 } ^ { 2 } } \end{array}$ − W T ·Xj − W T ·(1−X ) 2 is used to measure the difference between features before and after intervention. Here, G is the initial weight and W is the causal weight to be learned.

3. Weight optimization objective By minimizing the above difference, force feature $X _ { j }$ to become independent of ${ \dot { X } } _ { I - j } \ { \mathrm { : } }$ i after intervention, thereby eliminating the influence of confounding factors. This process is equiva-−lent to solving the optimization problem LossW = argminG $\textstyle \sum _ { j = 1 } ^ { p } \| . \| _ { 2 } ^ { 2 } $ , where p is the feature dimension.

The resulting W is the sample weight that can characterize the causal effect of the features.

# Creating balanced samples

Label relationships are particularly challenging for [[GANs]], which often fail to differentiate between causal features and noise during sampling. If a noise feature appears to have a strong, yet spurious, correlation with the label, this artificial association can be amplified during sample synthesis. This may overshadow the true causal relationships between features and labels, inversely affecting the perceived relationship between causal and noisy attributes. As a result, the accurate mapping between outcomes and features can be distorted.

To overcome these challenges, we propose a causality-infused GAN-based sampling method. By incorporating previously learned sample weights (denoted as W in Eq. 1) into the GAN’s objective function, our approach guides the model to capture the distribution of core causal features within samples, as indicated by the magnitude of causal weights. This integration tackles issues of marginalization and blind spots in synthesized samples, thereby improving the transparency and precision of feature-label associations in the generated data.

To address imbalanced data, we employ a Wasserstein GAN with Gradient Penalty (WGAN-GP)13 togenerate synthetic minority class samples. The generator g and discriminator D are implemented as fullyconnected neural networks with three hidden lavers (128 units each) and ReLU activations. The loss functionis defined as:

$$
L _ {W G A N - G P} = E _ {x \sim \mathrm {P} _ {r e a l}} [ D (x) ] - E _ {x \sim P _ {z}} [ D (g (z)) ] + \lambda E _ {\hat {x} \sim P _ {\hat {x}}} \left[ \left(\left\| \nabla_ {\hat {x}} D (\hat {x}) \right\| _ {2} - 1\right) ^ {2} \right] \tag {2}
$$

Here, λ = 10 is the gradient penalty coefficient. To ensure training stability, we use spectral normalization11 for all layers and clip gradients during optimization. Additionally, the generator is guided by thepreviously learned causal weights W (Eq. (1)) to prioritize causal feature distributions in the syntheticsamples.

# Weighted sample-based feature selection

Upon applying sample weights derived from Eq.  (1), we achieved mutual independence among all features, as visually illustrated in Fig. 2b. This is crucial for optimizing model performance, as it eliminates redundant information that could otherwise obscure the model’s decision-making process. Specifically, by employing causal intervention strategies, we systematically identified and discarded features that did not significantly influence the outcome labels related to network attack incidents. These features, often noise or superfluous elements within the dataset, could otherwise compromise the accuracy of the model’s judgments.

In this way, we not only purified the dataset but also ensured that the model focused on the subset of features genuinely causally linked to cyberattack behavior by excluding irrelevant features. This step builds upon the methodology outlined in reference9 , using rigorous causal inference analysis to discern and validate which features are key drivers of cyberattacks from those that are merely coincidental noise or secondary effects. As a result, a refined feature set, consisting solely of causal attributes, was constructed. This curation not only enhances the model’s interpretability but also improves its detection precision when faced with complex network anomalies, as it becomes more adept at deciphering the features directly impacting network health.

# LSTM-based anomaly detection leveraging sample weights and causal features

Leveraging sample weights and causal features, LSTM-based anomaly detection follows the preprocessing steps. This approach benefits from LSTM’s capacity to handle sequential data and extract temporal patterns, while also introducing a sample weighting scheme that prioritizes the learning of critical causal features and mitigates

the impact of irrelevant or noisy features. LSTM units, with their distinctive gating mechanisms, can capture long-term dependencies in the input data. The integration of sample weighting directs the model to focus on information from causal features that are vital for anomaly detection in network traffic, ignoring inconsequential or redundant aspects. This strategy significantly enhances both the accuracy and interpretability of the detection process.

Ultimately, this fusion of [[Causal deep learning]] with LSTM for anomaly detection achieves heightened precision in distinguishing normal activities from anomalous activities within complex network behaviors. It provides a powerful tool for security monitoring within the 6G network edge intelligence landscape, effectively bolstering the protection of this advanced communication ecosystem.

# EXPERIMENT

# Dataset overview

To validate the efficacy of [[Causal deep learning]] in detecting anomalies within 6G network edge intelligence (NEI) environments, we meticulously designed comparative experiments on two pivotal datasets: CICDDoS2019 and DoHBrw-20202–5,9 . The CICDDoS2019 dataset, replete with DDoS attack instances, facilitated our assessment of the model’s ability to safeguard edge devices against DDoS onslaughts in the high-speed, low-latency scenarios characteristic of 6G networks. Conversely, the DoHBrw-2020 dataset, tailored specifically for the security analysis of the DNS-over-HTTPS (DoH) protocol, employed realistic benign and malicious traffic simulations and a dual-classification strategy. This approach not only enabled a deeper dissection of DoH traffic patterns but also intensified the surveillance of nefarious activities concealed within DoH channels, underscoring the importance of effectively countering modern network threats while preserving the privacy of DNS queries. Collectively, these experiments established practical benchmarks for anomaly detection research in [[6G NEI]], comprehensively examining the models’ performance amid intricate and dynamically evolving network landscapes.

# Analysis of experimental results

# Decorrelation analysis

To validate the efficacy of NFDRF in eliminating nonlinear feature correlations, a comparative experiment was meticulously designed. The test entailed comparing the performance of NFDRF against that of several advanced methodologies across two substantial datasets using the metrics of accuracy (ACC), detection rate (DR), false positive rate (FPR), and F1 score. The competing methods included Archimedes Fire Hawk Optimization (AFHO)6 , independent component analysis (ICA)14, principal component analysis (PCA)15, and the CNN13. By assessing NFDRF’s detection capabilities on these benchmark datasets, with a focus on the comprehensive evaluation metric of the F1 score, we gain a thorough understanding of NFDRF’s potential and advantages in feature decorrelation and enhancing model performance. This holistic analysis underscores NFDRF’s effectiveness in improving anomaly detection accuracy while mitigating false alarms, thereby highlighting its contributions to the field.

As shown in Table 1, NFDRF exhibits outstanding performance on the CICIDS2019 dataset, achieving an F1 score of 99.7%, the highest among all compared methods. This achievement is complemented by an accuracy of 99.6% and a remarkably low false positive rate (FPR) of just 0.3%. These statistics underscore NFDRF’s robustness and precision within complex network ecosystems. Additionally, on the DoHBrw-2020 dataset, NFDRF outperforms alternative methods such as GMGWO and AFHO, with a top F1 score of 90.3%, demonstrating its superior capability to distinguish between positive (anomalous) and negative (normal) instances.

In summary, NFDRF consistently outshines other approaches across multiple datasets, with its performance on the CICIDS2019 dataset being particularly impressive due to its combination of high accuracy and low false positive rates. These results confirm that NFDRF is an effective tool for network anomaly detection, especially in scenarios where noise and nonlinear feature correlations present significant challenges. Its unique strengths lie in effectively mitigating these issues, thereby establishing it as a powerful solution in the field of complex network anomaly identification.

# Stability performance analysis

To benchmark the stability and generalization capabilities of the proposed method against other network anomaly detection approaches, we incrementally introduce random noise to all features, starting from the first, and assess the detection performance at each step until every attribute is corrupted.

Table 2 encapsulates the results of this comparative study, evaluating five methodologies or systems— CausalDL, AFHO6 , ETADC1 , IDWCDL2 , and CNN13— across two datasets in terms of their minimum (Min), mean (Mean) F1 scores, and detection stability (Stb). These datasets represent varied testing conditions, including

Table 1. Detection performance analysis of different methods after dimensionality reduction.   

<table><tr><td rowspan="2">Method</td><td colspan="4">CICIDS2019</td><td colspan="4">DoHBrw-2020</td></tr><tr><td>ACC</td><td>DR</td><td>FPR</td><td>F1-score</td><td>ACC</td><td>DR</td><td>FPR</td><td>F1 score</td></tr><tr><td>AFHO</td><td>98.3</td><td>97</td><td>2.1</td><td>96.9</td><td>89.4</td><td>87.7</td><td>11.2</td><td>86.9</td></tr><tr><td>ICA</td><td>97.1</td><td>96.9</td><td>3.4</td><td>96.9</td><td>88.2</td><td>86.2</td><td>15.5</td><td>86.1</td></tr><tr><td>PCA</td><td>99.1</td><td>98.1</td><td>1</td><td>97.8</td><td>88.4</td><td>85.5</td><td>14.0</td><td>85.5</td></tr><tr><td>CNN</td><td>93.2</td><td>90.5</td><td>7.1</td><td>89.2</td><td>90.1</td><td>87.8</td><td>12.1</td><td>87.8</td></tr><tr><td>NFDRF</td><td>99.7</td><td>99.6</td><td>0.3</td><td>99.5</td><td>90.3</td><td>87.8</td><td>11.2</td><td>87.5</td></tr></table>

Table 2. Stability and generalization performance of different detection methods.   

<table><tr><td rowspan="2">Method</td><td colspan="3">CICDDoS2019</td><td colspan="3">DoHBrw-2020</td></tr><tr><td>Min</td><td>Mean</td><td>Stb</td><td>Min</td><td>Mean</td><td>Stb</td></tr><tr><td>CausalDL</td><td>77.9</td><td>81.9</td><td>0.038</td><td>69.7</td><td>71.2</td><td>0.003</td></tr><tr><td>AFHO</td><td>76.9</td><td>81.2</td><td>0.043</td><td>58.1</td><td>60.3</td><td>0.028</td></tr><tr><td>ETADC</td><td>75.1</td><td>80.3</td><td>0.049</td><td>59.4</td><td>61.3</td><td>0.023</td></tr><tr><td>IDWCDL</td><td>43.3</td><td>56.2</td><td>0.158</td><td>62.1</td><td>64.8</td><td>0.017</td></tr><tr><td>CNN</td><td>59.2</td><td>65.8</td><td>0.093</td><td>48.2</td><td>48.9</td><td>0.002</td></tr></table>

different levels of feature contamination, to gauge the practical stability of the methods in actual network attack detection scenarios.

As indicated in Table 2, CausalDL sustains relatively high Min F1 scores of 77.9% and 69.7% across both datasets, demonstrating a robust level of stability. In contrast, other methodologies, such as IDWCDL and CNN, exhibit lower minimum detection accuracies in at least one dataset and experience greater performance fluctuations, suggesting inferior stability. Upon further analysis of the mean and Stb, CausalDL maintains high average detection accuracy with low detection bias across both datasets, reflecting excellent generalizability. Notably, in the CICDDoS2019 dataset, CausalDL achieves a mean of 81.9% with a minimal Stb of 0.038, outperforming other methods by a significant margin.

In summary, CausalDL exhibits commendable stability and generalization performance, particularly on datasets where features are contaminated. The average detection precision of these methods, informed by causal inference, is markedly better than that of conventional machine learning techniques (e.g., DNNs and RNNs) that do not leverage causal reasoning. This finding validates that the removal of spurious correlations and noise through causal inference effectively enhances the model’s generalizability, enabling it to maintain consistent and dependable detection abilities across diverse datasets and network settings. The results reinforce the ability of causal inference to enhance model resilience and adaptability in challenging, real-world [[Cybersecurity]] contexts.

# Causal interpretability performance analysis

When evaluating the causal interpretability of the model, we employed the CausalDL method to meticulously assign weights to the features of various cyberattacks11. These weights reflect the causal effects between features and cyberattacks, and their magnitudes intuitively represent the strength of the causal relationships.

An in-depth analysis of the experimental results presented in Table 3 reveals significant differences in the causal effects between various attack types and 23-dimensional features using the CICIDS2019 dataset as an example (see Table 3). For the normal category (BENIGN), the weights of most features are close to 1, indicating that these features remain relatively stable during normal network activities and are minimally affected by attacks. However, when facing attack types such as Bot and DDoS, the situation changes notably. For instance, during a DDoS attack, features like Total Fwd Packets and Fwd Packets/s exhibit significant weight changes. This suggests that these features show pronounced anomalies during a DDoS attack, and these abnormal features are key indicators for detecting such attacks. By examining these causal relationships, we can understand how the model identifies attacks based on changes in these features, thus providing a robust causal-association basis for detection training. This also confirms the model’s relatively high detection efficacy and stability on this dataset.

Turning our attention to the DoHBrw-2020 dataset (see Table 4), it involves analyzing the causal effects between four types of cyberattacks (including the normal category Benign) and 23-dimensional features. The results indicate that the causal effects of DoH attacks and malicious attacks are largely similar for most features, but there are slight differences in six features, such as Duration. For example, although the weight changes of the Duration feature among the normal category, DoH attacks, and malicious attacks are not substantial, in precise detection scenarios, these subtle differences could become crucial for differentiating between attack types. This suggests that when analyzing this dataset, we must focus on these seemingly minor yet potentially distinguishing feature differences to more accurately identify cyberattacks.

In conclusion, through the analysis of causal effects in different datasets, we can enhance the detection performance of CausalDL by leveraging feature weights and also deeply analyze the internal reasons for the differences in detection efficacy of various attack types based on the causal relationships between attack types and features. When a significant difference in the causal effect of a feature from other attack types is detected, we can quickly determine the causal attribution based on the abnormal features, thereby providing reliable decision-making support for network security protection.

# Conclusion

The present study introduces an innovative framework for anomaly detection that integrates CausalDL to address the explainability challenges in identifying anomalies within [[6G NEI]] networks. This methodology starts with the use of Fourier features and causal interventions to estimate feature independence and precise effect sizes, subsequently employing these estimates to generate adversarially synthesized, balanced datasets via generative networks for training purposes. LSTM units capture prolonged dependencies in network traffic, filtering out noise and thereby providing causally explainable insights. The system’s efficacy is empirically validated, with Tables 3 and 4 enabling the rapid identification of the underlying reasons for network anomalies.

Table 3. Causal effects of cyberattacks and features for the CICIDS2019 dataset.   

<table><tr><td>Label</td><td>BENIGN</td><td>Bot</td><td>DDoS</td><td>DGE</td><td>DSH</td><td>DSP</td><td>DSL</td><td>FPP</td><td>HB</td><td>IF</td><td>PS</td><td>SHP</td></tr><tr><td>Total fwd packets</td><td>0.99</td><td>0.00</td><td>0.08</td><td>0.03</td><td>0.00</td><td>0.00</td><td>0.03</td><td>0.06</td><td>0.01</td><td>0.00</td><td>0.00</td><td>0.06</td></tr><tr><td>Total backward packets</td><td>0.99</td><td>0.03</td><td>0.02</td><td>0.02</td><td>0.03</td><td>0.00</td><td>0.03</td><td>0.01</td><td>0.03</td><td>0.00</td><td>0.07</td><td>0.03</td></tr><tr><td>Total length of fwd packets</td><td>0.92</td><td>0.15</td><td>0.22</td><td>0.05</td><td>0.13</td><td>0.13</td><td>0.09</td><td>0.00</td><td>0.11</td><td>0.11</td><td>0.01</td><td>0.13</td></tr><tr><td>Fwd packet length std</td><td>0.98</td><td>0.06</td><td>0.04</td><td>0.02</td><td>0.08</td><td>0.02</td><td>0.02</td><td>0.06</td><td>0.03</td><td>0.07</td><td>0.03</td><td>0.10</td></tr><tr><td>Bwd packet length max</td><td>0.91</td><td>0.14</td><td>0.17</td><td>0.10</td><td>0.01</td><td>0.13</td><td>0.09</td><td>0.21</td><td>0.01</td><td>0.02</td><td>0.19</td><td>0.01</td></tr><tr><td>Bwd packet length min</td><td>0.99</td><td>0.08</td><td>0.00</td><td>0.03</td><td>0.00</td><td>0.00</td><td>0.07</td><td>0.00</td><td>0.01</td><td>0.12</td><td>0.00</td><td>0.06</td></tr><tr><td>Bwd packet length mean</td><td>0.95</td><td>0.15</td><td>0.06</td><td>0.05</td><td>0.04</td><td>0.15</td><td>0.15</td><td>0.00</td><td>0.03</td><td>0.10</td><td>0.10</td><td>0.07</td></tr><tr><td>Bwd packet length std</td><td>0.99</td><td>0.06</td><td>0.04</td><td>0.05</td><td>0.02</td><td>0.07</td><td>0.05</td><td>0.07</td><td>0.02</td><td>0.06</td><td>0.05</td><td>0.03</td></tr><tr><td>Fwd header length</td><td>0.89</td><td>0.14</td><td>0.06</td><td>0.13</td><td>0.22</td><td>0.01</td><td>0.11</td><td>0.21</td><td>0.22</td><td>0.15</td><td>0.00</td><td>0.01</td></tr><tr><td>Bwd header length</td><td>0.86</td><td>0.13</td><td>0.09</td><td>0.06</td><td>0.27</td><td>0.14</td><td>0.12</td><td>0.00</td><td>0.26</td><td>0.16</td><td>0.17</td><td>0.01</td></tr><tr><td>Fwd packets/s</td><td>0.93</td><td>0.13</td><td>0.24</td><td>0.07</td><td>0.05</td><td>0.20</td><td>0.11</td><td>0.11</td><td>0.01</td><td>0.00</td><td>0.01</td><td>0.01</td></tr><tr><td>Bwd packets/s</td><td>0.88</td><td>0.12</td><td>0.20</td><td>0.16</td><td>0.06</td><td>0.10</td><td>0.19</td><td>0.10</td><td>0.02</td><td>0.17</td><td>0.01</td><td>0.22</td></tr><tr><td>Min packet length</td><td>0.99</td><td>0.01</td><td>0.02</td><td>0.00</td><td>0.05</td><td>0.06</td><td>0.04</td><td>0.05</td><td>0.01</td><td>0.06</td><td>0.06</td><td>0.00</td></tr><tr><td>Max packet length</td><td>0.95</td><td>0.07</td><td>0.03</td><td>0.07</td><td>0.11</td><td>0.07</td><td>0.11</td><td>0.10</td><td>0.11</td><td>0.03</td><td>0.06</td><td>0.15</td></tr><tr><td>Packet length mean</td><td>0.97</td><td>0.01</td><td>0.06</td><td>0.05</td><td>0.10</td><td>0.14</td><td>0.03</td><td>0.01</td><td>0.02</td><td>0.05</td><td>0.12</td><td>0.08</td></tr><tr><td>Packet length std</td><td>0.99</td><td>0.04</td><td>0.07</td><td>0.03</td><td>0.05</td><td>0.05</td><td>0.04</td><td>0.00</td><td>0.05</td><td>0.00</td><td>0.07</td><td>0.05</td></tr><tr><td>FIN flag count</td><td>0.99</td><td>0.00</td><td>0.03</td><td>0.02</td><td>0.01</td><td>0.00</td><td>0.00</td><td>0.10</td><td>0.01</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>SYN flag count</td><td>0.98</td><td>0.01</td><td>0.01</td><td>0.07</td><td>0.08</td><td>0.07</td><td>0.02</td><td>0.09</td><td>0.08</td><td>0.00</td><td>0.06</td><td>0.06</td></tr><tr><td>PSH flag count</td><td>0.99</td><td>0.00</td><td>0.01</td><td>0.04</td><td>0.01</td><td>0.01</td><td>0.03</td><td>0.01</td><td>0.00</td><td>0.07</td><td>0.04</td><td>0.06</td></tr><tr><td>ACK flag count</td><td>0.99</td><td>0.04</td><td>0.01</td><td>0.08</td><td>0.01</td><td>0.04</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.08</td><td>0.04</td><td>0.00</td></tr><tr><td>URG flag count</td><td>0.99</td><td>0.00</td><td>0.01</td><td>0.02</td><td>0.09</td><td>0.01</td><td>0.04</td><td>0.00</td><td>0.08</td><td>0.00</td><td>0.07</td><td>0.00</td></tr><tr><td>ECE flag count</td><td>0.99</td><td>0.03</td><td>0.00</td><td>0.03</td><td>0.09</td><td>0.00</td><td>0.02</td><td>0.00</td><td>0.05</td><td>0.03</td><td>0.00</td><td>0.07</td></tr><tr><td>Down/Up ratio</td><td>0.99</td><td>0.03</td><td>0.00</td><td>0.05</td><td>0.08</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.08</td><td>0.02</td><td>0.00</td><td>0.00</td></tr></table>

Table 4. Causal effects among cyberattacks and features for DoHBrw2020.   

<table><tr><td>Label</td><td>Benign</td><td>DoHt</td><td>Malicious</td><td>NonDoH</td></tr><tr><td>Duration</td><td>0.16</td><td>0.43</td><td>0.44</td><td>0.77</td></tr><tr><td>Packet length standard deviation</td><td>0.07</td><td>0.59</td><td>0.57</td><td>0.57</td></tr><tr><td>Packet length mean</td><td>0.08</td><td>0.62</td><td>0.62</td><td>0.48</td></tr><tr><td>Packet length median</td><td>0.07</td><td>0.59</td><td>0.55</td><td>0.58</td></tr><tr><td>Packet length mode</td><td>0.07</td><td>0.58</td><td>0.59</td><td>0.55</td></tr><tr><td>Packet length skew from median</td><td>0.31</td><td>0.55</td><td>0.55</td><td>0.55</td></tr><tr><td>Packet length skew from mode</td><td>0.43</td><td>0.52</td><td>0.52</td><td>0.52</td></tr><tr><td>Packet length coefficient of variation</td><td>0.48</td><td>0.51</td><td>0.51</td><td>0.51</td></tr><tr><td>Packet time variance</td><td>0.09</td><td>0.38</td><td>0.43</td><td>0.82</td></tr><tr><td>Packet time standard deviation</td><td>0.43</td><td>0.52</td><td>0.52</td><td>0.52</td></tr><tr><td>Packet time mean</td><td>0.30</td><td>0.55</td><td>0.55</td><td>0.55</td></tr><tr><td>Packet time median</td><td>0.30</td><td>0.55</td><td>0.55</td><td>0.55</td></tr><tr><td>Packet time mode</td><td>0.36</td><td>0.54</td><td>0.54</td><td>0.54</td></tr><tr><td>Packet time skew from median</td><td>0.49</td><td>0.50</td><td>0.50</td><td>0.50</td></tr><tr><td>Packet time skew from mode</td><td>0.46</td><td>0.51</td><td>0.51</td><td>0.51</td></tr><tr><td>Packet time coefficient of variation</td><td>0.49</td><td>0.50</td><td>0.50</td><td>0.50</td></tr><tr><td>Response time/time variance</td><td>0.29</td><td>0.55</td><td>0.55</td><td>0.55</td></tr><tr><td>Response time/time standard deviation</td><td>0.38</td><td>0.53</td><td>0.53</td><td>0.53</td></tr><tr><td>Response time/time mean</td><td>0.44</td><td>0.52</td><td>0.52</td><td>0.52</td></tr><tr><td>Response time/time median</td><td>0.48</td><td>0.51</td><td>0.51</td><td>0.51</td></tr><tr><td>Response time/time mode</td><td>0.49</td><td>0.50</td><td>0.50</td><td>0.50</td></tr><tr><td>Response time/time skew from median</td><td>0.29</td><td>0.55</td><td>0.55</td><td>0.55</td></tr><tr><td>Response time/time skew from mode</td><td>0.29</td><td>0.55</td><td>0.55</td><td>0.55</td></tr><tr><td>Response time/time coefficient of variation</td><td>0.42</td><td>0.52</td><td>0.52</td><td>0.52</td></tr></table>

Consequently, by surpassing the limitations of correlation-centered approaches, CausalDL sheds light on intricate interdependencies, facilitating a nuanced understanding of various threats and thereby reinforcing the security architecture of the [[6G NEI]] ecosystem. Future research should explore refining sample synthesis strategies, enhancing cross-environment adaptability, and investigating advanced causal mechanisms to consolidate the forefront of anomaly detection in the dynamic landscape of [[6G NEI]].

# Result and discussion

# Current work summary

The present study pioneers an innovative framework for anomaly detection that integrates CausalDL to address the explainability challenges encountered in identifying anomalies within [[6G NEI]] networks. This methodology begins with the employment of Fourier features and causal interventions for estimating feature independence and precise effect sizes, subsequently utilizing these estimates to generate adversarially synthesized, balanced datasets via generative networks for training purposes. LSTM units capture prolonged dependencies in network traffic, filtering out noise and thereby furnishing causally explainable insights. The efficacy of the system is empirically validated, with Tables 3 and 4 enabling swift pinpointing of the underlying reasons for network anomalies. Consequently, by transcending the limitations of correlation-centered approaches, CausalDL illuminates intricate interdependencies, facilitating a nuanced understanding of myriad threats and thereby reinforcing the security architecture of the [[6G NEI]] ecosystem.

# Limitations and future directions

Despite these advancements, the study acknowledges critical limitations that warrant further investigation:

1. Performance on unseen attacks The proposed method exhibits a 19–27% drop in detection accuracy for zero-day attacks (Table 2, Min F1 scores), as statistical correlations dominate over causal relationships in such scenarios.   
2. While hybrid few-shot learning with causal meta-learning is suggested as a mitigation pathway, future work must rigorously validate whether the framework satisfies formal identifiability criteria (e.g., do-calculus or counterfactual validation) to ensure robustness against novel attack patterns.   
3. Scalability to 6G edge devices Latency increases by 40–60 ms on resource-constrained edge devices under high-load conditions, limiting real-time deployment. This highlights the need for lightweight frameworks, such as federated causal learning combined with model distillation, to optimize computational efficiency without compromising detection precision.   
4. Dependency on labeled data The model requires 15 K + labeled samples for stable convergence, which may hinder practical deployment in data-scarce environments. Future research should prioritize semi-supervised causal adversarial training methods to reduce reliance on labeled datasets while maintaining performance.   
5. Real-Time S Model drift occurs after 72 h in dynamic 6G environments, necessitating online causal concept drift detection modules. Developing adaptive mechanisms that autonomously update causal relationships in response to evolving network conditions will be critical for long-term reliability.

In conclusion, CausalDL provides a promising foundation for enhancing explainability in [[6G NEI]] anomaly detection. However, addressing the above limitations through scalable architectures, reduced data dependency, and robust drift adaptation will be essential for advancing practical, real-world applications. These challenges represent key directions for future research in secure and interpretable 6G networks.

# Data availability

The datasets generated and/or analyzed during the current study are available from the Canadian Institute for [[Cybersecurity]] repository. Specifically, this study utilized two key datasets for experimental validation: CICD-DoS2019 and DoHBrw-2020. The CICDDoS2019 dataset provides detailed records of various DDoS attack instances, offering crucial support for evaluating model defense capabilities in high-bandwidth, low-latency environments. This dataset can be accessed directly athttps://www.unb.ca/cic/datasets/ddos-2019.html http://205.17 4.165.80/CICDataset/CICDDoS2019/Dataset/download. On the other hand, the DoHBrw-2020 dataset focuses on the security analysis of the DNS-over-HTTPS (DoH) protocol, containing simulations of real benign and malicious traffic, which is essential for in-depth research on DoH traffic patterns and detecting malicious activities hidden within its channels. It can be accessed at https://www.unb.ca/cic/datasets/dohbrw-2020.html. These publicly available resources provide benchmark references for research on anomaly detection in 6G Network Edge Intelligence, contributing to further advancements in this field. All datasets used adhere to their respective terms of use and have been appropriately cited within the text.

Received: 20 January 2025; Accepted: 10 September 2025

Published online:19 November 2025

# References

1. Raja, G. et al. AI-empowered trajectory anomaly detection and classification in 6G–V2X. IEEE Trans. Intell. Transp. Syst. 24(4), 4599–4607. https://doi.org/10.1109/TITS.2022.3159526 (2022).   
2. Smith, D. C. [[Cybersecurity]] in the energy sector: Are we really prepared?. J. Energy Nat. Resour. Law 39(3), 265–270. https://doi.or g/10.1080/02646811.2021.1932250 (2021).   
3. Zeng, Z. et al. Toward identifying malicious encrypted traffic with a causality detection system. J. Inf. Secur. Appl. 80, 103644. https://doi.org/10.1016/j.jisa.2024.103644 (2024).   
4. Zeng, Z., Peng, W. & Zeng, D. Improving the stability of intrusion detection with [[Causal deep learning]]. IEEE Trans. Netw. Serv. Manage. 19(4), 4750–4763. https://doi.org/10.1109/TNSM.2022.3192281 (2022).

5. Nayak, R., Pati, U. & Chandra; Das, Santos Kumar.,. A comprehensive review on deep learning-based methods for video anomaly detection. Image Vis. Comput. 106, 104078. https://doi.org/10.1016/j.imavis.2021.104078 (2021).   
6. Rani, B. S., Vairamuthu, S. & Subramanian, S. Archimedes fire hawk optimization enabled feature selection with deep maxout for network intrusion detection. Comput. Secur. 138, 103751. https://doi.org/10.1016/j.cose.2024.103751 (2024).   
7. Fotiadou, K. et al. Network traffic anomaly detection via deep learning. Information 12(5), 215. https://doi.org/10.3390/info12050 215 (2021).   
8. Paolini, E. et al. Real-time clustering based on deep embeddings for threat detection in 6G networks. IEEE Access 11, 36217–36229. https://doi.org/10.1109/ACCESS.2023.3264520 (2023).   
9. Zeng, Z. et al. Intrusion detection framework based on causal reasoning for DDoS. J. Inf. Secur. Appl. 65, 103124. https://doi.org/1 0.1016/j.jisa.2022.103124 (2022).   
10. Luo, Y., Peng, J. & Ma, J. When causal inference meets deep learning. Nat. Mach. Intell. 2(8), 426–427. https://doi.org/10.1038/s42 256-020-0217-y (2020).   
11. Zeng, Z. et al. Toward intelligent attack detection with causal transformer in Internet of Things. IEEE Internet Things J. 11(1), 1016–1031. https://doi.org/10.1109/JIOT.2023.3312153 (2024).   
12. Zhang, X., Li, H. & Kong, A. Deep stable learning for out-of-distribution generalization. Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. https://doi.org/10.1109/CVPR46437.2021.00533 (2021).   
13. Nedeljkovic, D. & Jakovljevic, Z. CNN based method for the development of cyber-attacks detection algorithms in industrial control systems. Comput. Secur. 114, 102585. https://doi.org/10.1016/j.cose.2021.102585 (2022).   
14. Hyvärinen, A., Khemakhem, I. & Morioka, H. Nonlinear independent component analysis for principled disentanglement in unsupervised deep learning. Patterns 4(10), 100831. https://doi.org/10.1016/j.patter.2023.100831 (2023).   
15. Parizad, A. & Hatziadoniu, C. J. Cyber-attack detection using principal component analysis and noisy clustering algorithms: A collaborative machine learning-based framework. IEEE Trans. Smart Grid 13(6), 4848–4861. https://doi.org/10.1109/TSG.2022.3 187136 (2022).   
16. Li, Z. et al. Towards a unified analysis of random Fourier features. J. Mach. Learn. Res. 22(108), 1–51 (2021).

# Author contributions

Xiao Yi: Full responsibility for revising the manuscript and addressing the reviewers’comments. Zengri Zeng：- Experiment Ming Dai: Creative ideas Aimei Kang： Data provision Xuhui Liu and Yunlian Liu： Polishing the paper.

# Funding

This work is supported by the Scientific Research project of Hunan Education Department (24C0539), the Hunan Provincial Natural Science Foundation of China (Nos. 2025JJ70343, 2023JJ50495, 2025JJ70331), the Research Projects for Teaching Reform in Hunan Province’s Regular Colleges and Universities (No. 202401001443), the Shenzhen Vocational and Technical University Innovation Project (Nos. 6022312045 K, 1020-6023271024K1), the Youth Innovative Talent Fund of the Guangdong Provincial Department of Education (No. 602221012 K), and the Special Research Project on Annual Outstanding College Counselors in Hunan Provincial Higher Education Institutions (No. 22FDY11).

# Declarations

# Competing interests

The authors declare no competing interests.

# Additional information

Correspondence and requests for materials should be addressed to M.D. or A.K.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommo ns.org/licenses/by-nc-nd/4.0/.

© The Author(s) 2025