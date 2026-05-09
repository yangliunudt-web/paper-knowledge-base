---
title: "Leveraging [[ferroelectric]] Stochasticity and [[in-memory computing]] for DNN IP Obfuscation"
authors:
  - "Likhitha Mankali"
  - "Nikhil Rangarajan"
  - "Swetaki Chatterjee"
  - "Shubham Kumar"
  - "Yogesh Singh Chauhan"
  - "Ozgur Sinanoglu"
  - "Hussam Amrouch"
date: "2022-10-25"
year: "2022"
journal: "IEEE Journal on Exploratory Solid-State Computational Devices and Circuits"
doi: "10.1109/JXCDC.2022.3217043"
keywords:
  - "[[FeFET]]"
  - "[[Hardware security]]"
  - "[[DNN]]"
  - "[[PUF]]"
  - "[[In-memory computing]]"
cite: "[1] Mankali et al. Leveraging [[ferroelectric]] Stochasticity and [[in-memory computing]] for DNN IP Obfuscation[J]. IEEE Journal on Exploratory Solid-State Computational Devices and Circuits, 2022."
aiSum: "提出基于 FeFET PUF 的 DNN 模型保护方案，利用铁电畴随机性在对抗攻击时破坏权重，保护图神经网络 IP 安全。"
confidence: "medium"
wiki_concepts:
  - "[[FeFET]]"
  - "[[In-memory computing]]"
  - "[[Neural network]]"
---

Digital Object Identifier 10.1109/JXCDC.2022.3217043

# Leveraging [[ferroelectric]] Stochasticity and [[in-memory computing]] for DNN IP Obfuscation

LIKHITHA MANKALI 1 (Student Member, IEEE), NIKHIL RANGARAJAN 2 (Member, IEEE), SWETAKI CHATTERJEE 3 (Graduate Student Member, IEEE), SHUBHAM KUMAR 3 (Graduate Student Member, IEEE), YOGESH SINGH CHAUHAN 3 (Fellow, IEEE), OZGUR SINANOGLU 2 (Senior Member, IEEE), and HUSSAM AMROUCH 4 (Member, IEEE)

1Department of Electrical and Computer Engineering, New York University Tandon School of Engineering, Brooklyn, NY 11201 USA

2Division of Engineering, New York University Abu Dhabi, Abu Dhabi, United Arab Emirates

3Department of Electrical Engineering, Indian Institute of Technology Kanpur, Kanpur 208016, India

4Department of Computer Science, University of Stuttgart, 70049 Stuttgart, Germany

CORRESPONDING AUTHOR: L. MANKALI (lm4344@nyu.edu)

This work was supported in part by the Center for Cyber Security (CCS) at New York University Abu Dhabi (NYUAD).

This article has supplementary downloadable material available at https://doi.org/10.1109/JXCDC.2022.3217043, provided by the authors.

ABSTRACT With the emergence of the Internet of Things (IoT), deep neural networks (DNNs) are widely used in different domains, such as computer vision, healthcare, social media, and defense. The hardware-level architecture of a DNN can be built using an in-memory computing-based design, which is loaded with the weights of a well-trained DNN model. However, such hardware-based DNN systems are vulnerable to model stealing attacks where an attacker reverse-engineers (REs) and extracts the weights of the DNN model. In this work, we propose an energy-efficient defense technique that combines a ferroelectric field effect transistor ([[FeFET]])-based reconfigurable physically unclonable function (PUF) with an in-memory FeFET XNOR to thwart model stealing attacks. We leverage the inherent stochasticity in the FE domains to build a PUF that helps to corrupt the neural network’s (NN) weights when an adversarial attack is detected. We showcase the efficacy of the proposed defense scheme by performing experiments on graph-NNs ([[GNN]]s), a particular type of DNN. The proposed defense scheme is a first of its kind that evaluates the security of GNNs. We investigate the effect of corrupting the weights on different layers of the GNN on the accuracy degradation of the graph classification application for two specific error models of corrupting the FeFET-based PUFs and five different bioinformatics datasets. We demonstrate that our approach successfully degrades the inference accuracy of the graph classification by corrupting any layer of the GNN after a small rewrite pulse.

INDEX TERMS Deep neural networks (DNNs), ferroelectric field effect transistor (FeFET), [[Graph neural network]]s (GNNs), hardware security, model stealing attacks.

# I. INTRODUCTION

HE demand for artificial intelligence (AI) and machinelearning (ML) hardware for the edge computing paradigm has burgeoned in recent times with the growth of the Internet of Things (IoT). Deep neural networks (DNNs) are at the forefront of this revolution with applications in various domains, including computer vision, big data, natural language processing [1], [2], and so on. However, constructing and setting up a DNN incurs significant hardware costs and large-scale training data, requiring considerable monetary and logistical resources. Owing to this, cloud-based DNN applications and ML-as-a-service (MLaaS) have become

popular commercial models, catering to a wide range of businesses [3], [4]. Though performing complex DNN operations is computationally expensive, in certain scenarios like remotely deployed IoT devices or security-critical military applications, it is preferable to have an onboard hardware DNN processing system. Hence, from both commercial and military standpoints, the security of the deployed DNN hardware is of paramount importance, the piracy of which can cause monetary loss or result in the leaking of sensitive information.

In particular, graph neural network (GNN) is a class of DNNs specifically designed to process data relationships that

![](images/57c6e752f42a74ff31b1138127db0ae86a7c140a851fc8a46612778c7d87d775.jpg)  
FIGURE 1. Setup and training of hardware NNs, either for a cloud-based MLaaS model or for an ON-chip neural core implementation, is a resource-intensive and time-consuming process. This incentivizes NN IP stealing attacks. Here, the legitimate use cases are shown in green, whereas the malicious attack is highlighted in red.

can be expressed as graphs, for example, datasets pertaining to molecular chemistry and biology, social networks, and data mining, among others [5]. GNNs are typically utilized in applications involving non-Euclidean graph structures of various types, including cyclic, acyclic, directed, and undirected graphs [6]. They have recently gained traction because many relationships in the natural world occur in graph data, and neural networks (NNs) like convolutional NNs (CNNs) cannot process such graph data accurately. CNNs process the input data, such as images represented as tensors, and consider them as ordered data. The change in the order of elements in a tensor leads to a change in the output of the CNN. This change in the output with the representation order does not apply to graphs. A graph representation does not require a fixed order; thus, the tensor-based representation is unsuitable for graphs. GNNs can process graph data irrespective of the order and are capable of learning the structural features of the overall graph.

# A. HARDWARE SECURITY OF NEURAL NETWORKS

Various attacks have been proposed against the confidentiality of NN systems. These attacks aim to reverse-engineer (RE) the hardware of NNs by stealing the underlying model’s vital information, that is, its weight mapping. In such attacks, an attacker queries the NN with various inputs and collects the corresponding output responses. Furthermore, using the input–output responses, an attacker can RE the weights of the target network. Such attacks have been proposed against different types of DNNs. In [7], [8], and [9], researchers have proposed an attack on black-box DNNs wherein they craft the inputs, that is, images to be queried in such a way that the output predictions reveal the internal attributes of the underlying network. There are different types of adversarial attacks that aim to affect the confidentiality of GNNs. Such attacks either aim to retrieve the important information of the training dataset or steal the GNN model itself. The attacks proposed in [10] and [11] target membership inference which aims to find valid data samples that are used for training, thus affecting the confidentiality of the training dataset. In [12], a link stealing attack has been proposed that aims to predict the existence of links between two nodes in the training graph, thus leaking the training dataset. In [13] and [14], property inference attacks have been proposed against GNNs,

which aim to infer the properties of training datasets such as subgraphs, graph density, and so on. In [15], [16], and [17], model extraction attacks have been proposed against GNNs that aim to build a surrogate model with an accuracy similar to the original GNN model that is under attack. In [16], researchers have proposed different model extractions considering different attack scenarios, such as complete, partial, or no knowledge about the training dataset. However, this attack also extracts the model of GNN using input and output (I/O) queries. In [15], researchers have proposed a model extraction attack that targets inductive GNNs in an adversarial setting where they do not tamper with the training process. The attack proposed here queries the GNN considering two scenarios—with and without the structural information of the query graphs. In this work, we focus on such model stealing or extraction attacks on GNNs. All these attacks target the software implementation of the NN and aim to generate adversarial examples using the knowledge of the extracted model.

Several approaches have been proposed to defend against the model extraction/stealing attacks, especially for DNNs. These techniques defend the NN architecture at the hardwarelevel. In [19], researchers have demonstrated a technique that defends memristor-based NN architectures by leveraging the memristor’s obsolescence effect. The continuous application of voltage causes an increase in memristance, which causes the obsolescence effect in memristors. This solution thwarts the attacker from querying the NN architecture to obtain enough input–output pairs to replicate the target network model. But this defense can be circumvented by controlling the obsolescence effect through input voltage amplitude scaling. Later, in [20], researchers proposed a superparamagnetic magnetic tunnel junction (s-MTJs)-based defense mechanism that leverages the thermally induced telegraphic switching property of s-MTJs to corrupt the weights. This defense is unlike [19], wherein the attacker cannot control the corruption of weights. However, the small retention time of s-MTJs warrants frequent refresh operations, leading to higher energy costs.

# B. KEY CONTRIBUTIONS OF THIS WORK

In this work, we leverage two particular properties of emerging ferroelectric field effect transistor (FeFET) devices to secure NN systems, namely: 1) the inherent stochasticity in the spatial distribution of the ferroelectric (FE) domains to corrupt the NN weights [21] and 2) the in-memory computation capability of FeFET to perform efficient and compact XNOR-based logic-in-memory [22]. We design a weight encryption scheme for protecting the confidentiality of hardware NNs by combining these two effects. Specifically, we choose GNNs as the model network to be protected, although the proposed scheme can be applied to any DNN structure without loss of generality. Next, we describe the threat model assumed for the target GNN.

Threat model: Here, we outline the resources and capabilities of the attacker considered in this work.

(a) An attacker has (only) black-box access to the hardware GNN intellectual property (IP) that is either a part of the cloud-based infrastructure or a part of an onchip core. They do not have physical access to the individual internal weights, to probe and find the programed weights at any given instant.

(b) The attacker can apply any number of I/O queries to the GNN IP.   
(c) The attacker has access to the dataset that is part of the original training dataset or is similar to the training dataset of GNN IP.

Our contributions to this work are as follows.

(1) We exploit the randomness in FeFET devices to augment the security of NN systems by amalgamating it with the in-memory computation capabilities of FeFET XNOR gates.   
(2) We present a comprehensive analysis and modeling of the randomness in FE domains and highlight the construction of a reconfigurable physically unclonable function (PUF) using this inherent randomness. This FeFET-based reconfigurable PUF is pivotal to the weight corruption mechanism.   
(3) To the best of our knowledge, this is the first work to demonstrate a defense against model piracy attacks specifically targeting GNNs.   
(4) We explore the system-level implications of the GNN weight corruption on the accuracy of classification tasks and show how model piracy attacks can be foiled.

# II. IMPLEMENTATION

The background on GNNs and FeFET device construction and characteristics is described in the Supplementary information.

# A. MODELING THE INHERENT RANDOMNESS IN FeFET

It is noteworthy that not all the domains within the FE layer switch at the same time [23]. Therefore, positive and negative domains coexist in the FE layer when a ‘‘weak’’ write voltage (WV) pulse (i.e., a WV pulse with a smaller amplitude and/or smaller width than what is needed to completely switch all FE domains) is applied. Thus, depending on the percentage of domains polarized up or down $( \% P _ { \mathrm { F E + } } )$ , the FeFET can be set into intermediate V states by controlling the WV amplitude or pulsewidth. The high $V _ { \mathrm { T H } }$ state corresponds to 0%, where all the domains are polarized upward and vice versa for the low $V _ { \mathrm { T H } }$ state (100%), where all the domains are polarized downward. For a sufficiently long-channel FeFET, where the domain size is much smaller than the channel dimensions, a gradual switching of the FeFET is observed and there can be many intermediate states of polarization [21].

For intermediate $V _ { \mathrm { T H } }$ states, the polarized domains can exist in any spatial orientation throughout the channel [25]. Also, due to the stochastic switching time of the FeFET, it cannot be predicted the exact domains that might be switched even for the same pulse. This provides an additional source of variation in the distribution of the polarized domains along the channel. Thus, even for a fixed $\% P _ { \mathrm { F E + } }$ , we can have a different spatial distribution of the FE domains and thus variability in the underlying channel electron density. This can cause variability in the electrical characteristics of the FeFET at a given intermediate state. Also, conventional sources of variability in the underlying transistor, such as random dopant fluctuations, metal gate work function variation, and line edge roughness, can cause additional variation in the electrical properties of the intermediate state.

To model the variability and randomness (inherent stochasticity) inside FeFET, we employ our in-house TCAD-based

framework as in [21] and [25]. It enables us to directly evaluate the impact of random spatial fluctuation of the polarization through emulating the polarization charges $( P _ { \mathrm { F E } } )$ with fixed charges $( Q _ { \mathrm { F I X } } )$ at the $\mathrm { \bar { { H f O } } } _ { 2 } { - } \mathrm { S i O } _ { 2 }$ interface. In practice, each domain is assigned a particular $Q _ { \mathrm { F I X } }$ depending on the polarization. The value of $Q _ { \mathrm { F I X } }$ can be calculated by measuring the residual $P _ { \mathrm { F E } }$ in the FE layer as

$$
Q _ {\mathrm {F I X}} = \frac {P _ {\mathrm {F E}}}{1 . 6 \times 1 0 ^ {- 1 9}}. \tag {1}
$$

Here, QFIX represents the interface charge concentration (measured in $\mathrm { c m } ^ { - 2 } )$ at the FE layer–interfacial layer interface. The sign of QFIX determines the type of charge and thus the direction of the polarization of the domain.

For a given $\% P _ { \mathrm { F E + } }$ , the total number of domains with QFIX+ (or $Q _ { \mathrm { F I X - } } )$ is fixed and is randomly distributed in space to generate a random distribution of the channel electron density [21]. Next, Monte-Carlo simulations are performed to determine the effect of the random distribution of the domains on the electrical characteristics of FeFET. Additionally, variations due to the conventional sources of variability are simulated and combined with the inherent variations from the multidomain FeFET. The corresponding $V _ { \mathrm { T H } }$ distributions of the FeFET for 0%–100% is discussed in supplementary information. The maximum variation is observed at 50%, where there is an equal number of up and down polarized domains and thus maximum spatial variability. This variation in $V _ { \mathrm { T H } }$ also causes a variation in IDS at a particular $\% P _ { \mathrm { F E + } }$ .

![](images/c514c5e8fc091124f5ea2bae0fd48a857637e7e3cfe891d620cc80d9977130f6.jpg)  
FIGURE 2. (a) Change of $V _ { \mathsf { T H } }$ with $\% P _ { F E } .$ + and (b) plot of $\% P F E +$ against applied WV for a pulse duration of $\sum \mu \ S$ to set it into different $V _ { \mathsf { T H } }$ values and hence different stored states.

Fig. 2(a) plots the mean-VTH for each intermediate state with corresponding $\% P _ { \mathrm { F E + } }$ . In order to set the FeFET at a particular $\% P _ { \mathrm { F E + } }$ , we need to know the relationship between WV and $\% P _ { \mathrm { F E + } }$ . This relationship can be established by measuring the residual polarization after a write pulse. Once this value is known, it can be normalized between the minimum and maximum $P _ { \mathrm { F E } }$ and converted to $\% P _ { \mathrm { F E + } }$ . Our fixedcharge-based modeling framework also measures the same maximum and minimum $P _ { \mathrm { F E } } .$ , converts it into fixed charges, and distributes it among the domains according to a given $\% P _ { \mathrm { F E + } }$ . This allows us to link our fixed-charge-based TCAD model with the already known Preisach model and determine the write pulse magnitude and duration to set it into a particular $\% P _ { \mathrm { F E + } }$ . Fig. 2(b) shows the relationship between $\% P _ { \mathrm { F E + } }$ and WV for a fixed pulsewidth.

# B. FeFET-BASED RECONFIGURABLE PUF

As discussed in Section III-A, FeFET shows variation in $V _ { \mathrm { T H } }$ and correspondingly, the current flowing through it even

TABLE 1. Reconfigure pulse magnitude and time to set into different $\% P F E +$ .   

<table><tr><td>% PFE+</td><td>Voltage (V)</td><td>Time (ns)</td></tr><tr><td>45</td><td>-0.7</td><td>325</td></tr><tr><td>48</td><td>-0.7</td><td>145</td></tr><tr><td>49</td><td>-0.7</td><td>5</td></tr><tr><td>50</td><td>0</td><td>0</td></tr><tr><td>51</td><td>2.8</td><td>5</td></tr><tr><td>52</td><td>2.8</td><td>190</td></tr><tr><td>55</td><td>2.8</td><td>no change</td></tr></table>

for a fixed polarization strength. This forms the basis for FeFET to be used as a PUF. The structure of our designed PUF is similar to the recently proposed 1 FeFET per cell reconfigurable PUF [26]. The $\mathrm { \dot { P } U \dot { F } }$ is programed in three steps. First, all the transistors are set to an initial high-VTH or $\mathrm { l o w } { - } V _ { \mathrm { T H } }$ state by setting all the domains in an upward or downward direction. This is done by applying a high positive or negative pulse. In the next step, we apply a voltage pulse of lower magnitude to set it in an intermediate $V _ { \mathrm { T H } }$ state. The third and final step is to generate the output bits from the PUF. Because of the inherent stochasticity and randomness that arises from the multidomain FeFET, there exists variability in the FeFET. Owing to this variability, when the FeFET is read using a particular $V _ { \mathrm { R E A D } }$ , there exists variability in $I _ { \mathrm { D S } }$ . This gives us a distribution of $I _ { \mathrm { D S } }$ . The mean of the distribution is chosen as a reference $( I _ { \mathrm { R E F } } )$ and compared with $I _ { \mathrm { D S } }$ after reading to generate the bits. For a device with $I _ { \mathrm { D S } } > I _ { \mathrm { R E F } }$ , the output is $^ { \bullet \bullet } 0 , ^ { \bullet \bullet }$ else $^ { 6 6 } 1 . ^ { , 9 }$ . Thus, we can have equiprobable $0 \mathrm { { s } }$ and $1 \mathrm { { ' s } } ~ ( \mathrm { P ( 0 ) } = \mathrm { { P ( 1 ) } } = 0 . 5 )$ . To reconfigure the PUF, a positive or negative voltage pulse can be applied. This sets the constituent FeFETs into different intermediate $V _ { \mathrm { T H } }$ states such that the current distribution completely changes. This consequently alters the probability of 0’s and 1’s.

In order to simulate the PUF, we set the polarization in the FE layer for each FeFET to 50% because the maximum variation is observed here. This can be done by applying a WV of a suitable magnitude of about 2.2 V determined from Fig. 2(b). We use our variability modeling framework to run Monte-Carlo simulations at 50% for FeFET to generate the current distribution. Finally, we can read the drain–source current $\left( I _ { \mathrm { D S } } \right)$ from the bitline by applying a $V _ { \mathrm { R E A D } }$ at the gate terminal for a very short duration (0.5 ns) to not disturb the polarization state. When an m-bit challenge in the form of the address of the individual cells is input to the FeFET, an n-bit output is generated depending on the particular FeFET returning either ${ } ^ {  } 1 { } ^ { \ ' } \mathrm { o r } ^ { \cdots } 0 .$ ’

In the case of any attack by the attacker, the PUF can be reconfigured (reprogrammed) by applying a reconfiguration pulse at the word-line for each FeFET parallelly. This sets the FeFETs in the PUF array to a different state of polarization. Table 1 shows the magnitude and duration of the reconfigure pulse required to change into nearby states of polarization from 50% $P _ { \mathrm { F E + } }$ . These values are also calculated in the same way as described in Section II-A. The corresponding change in the distribution curves can be generated using our fixedcharge-based variability modeling framework (see Fig. 3). I does not change with the change in $\% P _ { \mathrm { F E ^ { + } } }$ and thus we no more have equiprobable 0’s and 1’s. If the $\% P _ { \mathrm { F E + } }$ increases, the distribution shifts right, and the probability of getting $\textrm { a } ^ { \ast } 0 ^ { \ast } \ ( \mathrm { P } ( 0 ) )$ increases. Conversely, for the decrease

![](images/36f9ecd26eba712b668b164d07d381a266466aafbf4ae75507147624c0912531.jpg)  
FIGURE 3. Domain configuration and the distribution of IDS before and after reconfiguring pulse. The tiles show the channel configuration and the random distribution of the domains for a particular $\% P _ { F E + } \cdot I _ { \sf D S }$ distribution for the corresponding state shows the variability due to the random distribution of domains.

![](images/36420d9d395b7e540d418ea09afe8425adea8762cb64ab554242d05327606470.jpg)  
FIGURE 4. Shift in the distribution curves for changing $\boldsymbol { \circ } / _ { \boldsymbol { \circ } } \boldsymbol { P } _ { \mathsf { F E } + }$ + from 50% by a small value. Increase in $\boldsymbol { \circ } / \boldsymbol { \circ } \boldsymbol { P } _ { \mathsf { F E } + }$ + shifts the entire distribution right and vice versa for decreasing $\boldsymbol { \circ } / _ { \mathsf { o } } \pmb { P } _ { \mathsf { F E } + }$ .

in $\% P _ { \mathrm { F E + } } , \mathrm { P } ( 1 )$ increases. Therefore, on applying the reconfiguration pulse, the existing output bit probability from the PUF changes. Fig. 4(b) shows the overlapping distribution of the $I _ { \mathrm { D S } }$ for two other polarization strengths compared to the golden standard case of 50%. As $I _ { \mathrm { R E F } }$ does not change, we have a probability for the output bits to flip from $^ { \bullet } 0 ^ { \prime \prime }  ^ { \bullet } 1 ^ { \prime \prime }$ $( P ( 1 _ { n } | \bar { 0 _ { p } } ) ) \mathrm { o r } ^ { * * } 1 ^ { , \bar { \cdot } }  ^ { * * } 0 ^ { , 9 } ( P ( 0 _ { n } | 1 _ { p } ) )$ . The suffix $\ " { \bf n } \ "$ and $\ " \mathrm { p } \ : \mathrm { . } \ :$ refers to the new state after reconfiguration and the previous state before reconfiguration respectively. The total P(error) is the sum of $P ( 1 _ { n } | 0 _ { p } )$ and $P ( 0 _ { n } | 1 _ { p } )$ .

Assuming that the nature of the distribution curve remains the same (i.e., points left and right of the mean continue to do so even on changing the $\% P _ { \mathrm { F E + } } )$ , we can easily calculate the error probability. If $\% P _ { \mathrm { F E + } }$ increases, $P ( 1 _ { n } | 0 _ { p } )$ remains zero because all of FeFETs which were originally producing an output $\cdot _ { 0 } \cdot \mathrm { \ }$ will continue to do so even after reconfigure. $\mathrm { P } ( \mathrm { e r r o r } ) = P ( 0 _ { n } | 1 _ { p } )$ for this case. Alternatively, $\mathrm { i f } \ \% P _ { \mathrm { F E + } }$ decreases, P(error) $\dot { = } P ( 1 _ { n } | 0 _ { p } )$ . To determine these probabilities, we use Bayes’ theorem as follows:

$$
P \left(1 _ {n} \mid 0 _ {p}\right) = \frac {P \left(1 _ {n}\right) \cdot P \left(0 _ {p} \mid 1 _ {n}\right)}{P \left(0 _ {p}\right)} \tag {2}
$$

$$
P \left(0 _ {n} \mid 1 _ {p}\right) = \frac {P \left(0 _ {n}\right) \cdot P \left(1 _ {p} \mid 0 _ {n}\right)}{P \left(1 _ {p}\right)}. \tag {3}
$$

From our previous discussion, we know $\begin{array} { r l } { P ( 0 _ { p } ) } & { { } = } \end{array}$ $P ( 1 _ { p } ) = 0 . 5 \mathrm { { . } } P ( 1 _ { n } )$ and $P ( 0 _ { n } )$ can be simply calculated as the probability for the new distribution curve to either lie left or right of the IREF. For calculation of $P ( 0 _ { p } | 1 _ { n } )$ and

TABLE 2. Error probability for bitflip for reconfiguring to different $\% P F _ { F E } .$ + at different $V _ { R E A D }$ .   

<table><tr><td rowspan="2">% PFE+</td><td colspan="3">Bitflip error probability (%)</td></tr><tr><td>VREAD = 0.1 V</td><td>VREAD = 0.5 V</td><td>VREAD = 1 V</td></tr><tr><td>45</td><td>83.696</td><td>88.535</td><td>98.598</td></tr><tr><td>48</td><td>20.900</td><td>37.057</td><td>58.215</td></tr><tr><td>49</td><td>3.585</td><td>11.401</td><td>20.745</td></tr><tr><td>50</td><td>0</td><td>0</td><td>0</td></tr><tr><td>51</td><td>22.113</td><td>31.764</td><td>47.192</td></tr><tr><td>52</td><td>42.797</td><td>58.793</td><td>58.557</td></tr><tr><td>55</td><td>83.611</td><td>98.071</td><td>99.903</td></tr></table>

$P ( 1 _ { p } | 0 _ { n } )$ , we calculate the probability for the new distribution curve to lie within $I _ { \mathrm { R E F } }$ and the mean of the new distribution since this defines the region that given it is $^ { 6 6 } 1 ^ { 9 } \ ( ^ { 6 6 } 0 ^ { 3 } )$ now, what is the probability that previously it was $^ { 6 6 } 0 ^ { 3 9 } ( ^ { 6 6 } 1 ^ { 5 } )$ . Table 2 demonstrates the P(error) for changing the $\% P _ { \mathrm { F E + } }$ for various $V _ { \mathrm { R E A D } }$ . Note that our model is able to capture only device-to-device variations and does not take into account cycle-to-cycle variations, which are present in real devices. However, the cycle-to-cycle variations will only add to the stochasticity of the FeFET device. Furthermore, we have considered an FeFET device with 100 domains and a very wide channel device. Thus, the cycle-to-cycle variations due to switching stochasticity will not play a huge role since the cycle-to-cycle variations are most prominent in highly-scaled devices with a very few domains [27].

# C. IN-MEMORY COMPUTATION WITH FeFET XNOR

The logic-in-memory realization of an FeFET-based XNOR Boolean function can be achieved through coupling two FeFETs together [28] in which a logic value is always stored inside in a complementary manner. The structure of a single FeFET XNOR cell is shown in Fig. 5. For instance, when logic ‘‘0’’ is stored, FeFET1 will be in the low $V _ { \mathrm { T H } }$ state and FeFET2 will be in the high $V _ { \mathrm { T H } }$ state. Correspondingly, the FeFETs are in opposite configurations for storing ‘‘1.’’

Depending on whether the value inputted to the FeFETbased XNOR matches the stored value or not, the XNOR output will be either $\mathbf { \ddot { \rho } } _ { 0 } , \mathbf { \vec { \rho } } _ { 0 }$ or ‘‘1.’’ In practice, a matchline (Mline) is first charged to high $V _ { \mathrm { d d } }$ . Then, when $A \ = B ,$ , both FeFETs will be OFF. Hence, no conducting path is formed and the gate output remains at high voltage. Therefore, the XNOR’s output provides a logic $^ { \overline { { \mathfrak { s } } } _ { 1 } , \mathfrak { s } }$ in such a case. Only when $A \ \ne \ B ,$ a conducting path is formed through the Ferroelectric FET (FeFET) that is in a low $V _ { \mathrm { T H } }$ state. Hence, the voltage rapidly drops and the output provides logic ‘‘0.’’ Concisely, if and only if $A \ \ne \ B$ , the output is logic ‘‘0.’’ Otherwise, it is logic ‘‘1,’’ which is a realization of the XNOR Boolean function. Further details on the FeFET-based inmemory XNOR is shown in [22].

# D. WEIGHT CORRUPTION SCHEME

Fig. 6 delineates the {FeFET PUF + in-memory XNOR}- based weight corruption architecture considered in this article.1 Initially, the PUF array is programed to a fixed random state and the internal states of the cells of the XNOR array are written accordingly, to obtain the desired final weight array $[ \omega _ { \mathrm { f i n a l } } ]$ that is required for the GNN task. In the

1Note that the weight corruption scheme is applicable for any standard FeFET-based [[crossbar]] without loss of generality.

![](images/bb93d38d23894b2d301ca93717ebc1b6d4bbd3ffc6a8a44960a0e4cc6a95522c.jpg)  
FeFET-based XNOR storing A = 0

![](images/fc942f8195fcb9692677cc1f6de85caf44a96ab44aef1ead7dbb283de09a3d9d.jpg)  
FeFET-based XNOR storing A = 1

FIGURE 5. FeFET-based in-memory XNOR gate construction and truth table.   

<table><tr><td>A</td><td>B</td><td>FeFinFET1</td><td>FeFinFET2</td><td>Output</td></tr><tr><td>0</td><td>0</td><td>OFF</td><td>OFF</td><td>1</td></tr><tr><td>0</td><td>1</td><td>ON</td><td>OFF</td><td>0</td></tr><tr><td>1</td><td>0</td><td>OFF</td><td>ON</td><td>0</td></tr><tr><td>1</td><td>1</td><td>OFF</td><td>OFF</td><td>1</td></tr></table>

![](images/0c4ea6df3fa3f2c8da3ef7fac55f289df02cb9da8f5bc6cd1e6069c6ee9982f4.jpg)  
FIGURE 6. FeFET-based reconfigurable PUF is used in conjunction with an in-memory XNOR array for implementing the weight corruption scheme.

case of no attack, the PUF is set once and device-to-device variations do not affect the functionality, that is, inference of GNN inference.

Once an attack is detected, the PUF array is reconfigured (rerolled) which changes the original n-bit response from PUF and hence, the final weights from the XNOR operation will be different from the original golden weights. This weight corruption ensures that the attacker is unable to steal the GNN IP (weight mapping).

We re-program the FeFET XNOR cell array and the FeFET PUF after an attack as follows. We first retrieve the golden weights ωf that are stored in a tamper-proof memory [29] and XNOR them with the rerolled PUF weight array, that is, ωPUF_new. This gives us the ωint_new values, which are then updated in the FeFET XNOR memory cells, by setting them in high or low $V _ { T H }$ . Now, by performing $\omega _ { \mathrm { i n t . } }$ _new ⊙ ωPUF_new, we can obtain the golden weights back.

# III. EXPERIMENTAL EVALUATION

In this section, first, we describe the experimental setup details and then evaluate the proposed work by conducting experiments on GNN.

# A. EXPERIMENTAL SETUP

The experiments have been performed on a single compute node with AMD EPYC CPU comprising 64 cores operating at 2.25 GHz, with 480 GB memory. We mimic the hardware-level corruption of weights at a software level by implementing the error distribution model of the proposed FeFET-based reconfigurable PUF. We perform experiments on five bioinformatics datasets, that is, PROTEINS, MUTAG, ENZYMES, NCI1, and D&D. These datasets are represented

as graphs, and the classification of these graphs is useful for various bioinformatics applications. We have obtained datasets for our experiments from [30]. Next, we describe the parameters of the GNN topology and error models of the FeFET-based PUF.

# 1) GNN TOPOLOGY

We perform the experiments on Deep Graph Convolution Neural Network (DGCNN) [18] as discussed in Supplementary information. We use default parameters of the DGCNN architecture [18]. The GNN consists of four GCN layers with output channel dimensions of 32, 32, 32, and 1, respectively. The m value of the SortPooling layer is set to 0.6. Furthermore, the 1-D convolutional layers have 16 and 32 output channels, respectively. Finally, the dense layer consists of 128 hidden units followed by a softmax layer as the output layer. Also, the GNN is trained to minimize the cross-entropy loss using an Adam optimizer.

# 2) ERROR MODEL

The probability for a particular bit to flip is described in detail in Section II-B. From there, we chose two error models for our experiments:

1) Error ModelA: This model corresponds to changing the state of polarization from 50% to 49 % $P _ { \mathrm { F E + } }$ for each FeFET in the PUF. $V _ { \mathrm { R E A D } }$ is chosen very low at 0.1 V. As the $\% P _ { \mathrm { F E + } }$ decreases in this case, the distribution shifts right and there exists a probability for the bits from PUF that were originally ‘‘0’’ changing to ‘‘1.’’ The corresponding P(error) for the output bits of PUF to flip is obtained from Table 2. Thus, for every bit in $[ \omega _ { \mathrm { f i n a l } } ]$ , if b == ‘‘0,’’ the bit is flipped with the probability of 3.58%.

2) Error ModelB: This model corresponds to changing the state of polarization from 50% to 51%. As with the other error model, the duration and magnitude of the reconfigure pulse can be obtained from Table 1 and $V _ { \mathrm { R E A D } } = 0 . 1$ V. As the $\% P _ { \mathrm { F E + } }$ increases, in this case, there exists a probability for the output bits from PUF to flip from ${ \bf \ddot { \tau } } ^ { * } 1 ^ { \bf \stackrel { , } { \tau } } { \bf \dot { t } } _ { 0 } \bf \ddot { \tau } ^ { * } 0 . \bf \stackrel { , } { \tau } ^ { , }$ The value for this can be again obtained from Table 2. Thus, for every bit in $[ \omega _ { \mathrm { f i n a l } } ] .$ , if b == ‘‘1,’’ the bit is flipped with the probability of 22.11%.

# B. EXPERIMENTAL RESULTS

Considering the probabilistic nature of the error model, we report an average reduction in the accuracy of GNNs over ten trials for all the results. Fig. 7 demonstrates the reduction in accuracy of the GNN for all the five datasets consid-

![](images/1735285229916b5ba731d94ef7154d4d4e87015fe228b2e7d5a385f65d5a430c.jpg)  
FIGURE 7. Reduction in the accuracy of GNN calculated over ten trials for all the considered bioinformatics datasets. The weights in all the GNN layers are XNORed with the proposed FeFET-based PUF’s error model.

ered above over ten trials when all the weights of the GNN are corrupted.2 The reduction in accuracy is the difference between the accuracy obtained upon weight corruption and the accuracy of the GNN with golden/original weights. It can be observed that the reduction in accuracy varies with the trial. This is observed because of the difference in the number of bit flips and corrupted weights. This observation is further justified by observing the effect of the GNN layer on accuracy degradation, which is discussed next.

# 1) EFFECT OF GNN LAYER

To observe the impact of the corruption of weights in each layer of the GNN, we corrupt the weights of each layer separately and obtain the corresponding accuracies. Fig. 8 demonstrates the accuracy reduction in the GNN output when weights of individual layers are corrupted one by one, across the eight layers of GNNs (four GCN layers, two 1-D convolutional layers, and two hidden layers) for the PROTEINS dataset. It can be observed that the accuracy degradation varies with the GNN layer, that is, the accuracy degradation due to the corruption in the second, third, and fourth GCN layers is low compared to corruption in other GNN layers. Thus, a defender need not corrupt all the weights of the GNN and can instead choose a particular layer to be corrupted, which lowers the power consumption.

![](images/cd9b9d4d46180f0d12875392c99143f62b9222967d45c2508b6290efb030eabc.jpg)  
FIGURE 8. Reduction in the accuracy of GNN (average of ten trials) for corruption of weights separately across GNN layers for the PROTEINS dataset.

# 2) EFFECT OF ERROR MODEL

As described above, we consider two error models for the bit flipping or corruption of weights. To observe the effect of the error model, we compare the accuracy degradation between the two error models for all the GNN layers in the ENZYMES dataset as shown in Fig. 9. There is a difference

2Note that all the results of accuracy degradation have been calculated over ten trials.

![](images/d533824ae82054e44e87185a2e80d67f97e7f2adbbb4e2e4a7a08c35f40c2351.jpg)  
FIGURE 9. Comparison in the reduction in accuracy (average over ten trials) for corruption of weights separately across GNN layers for the ENZYMES dataset for two error models.

![](images/6c409186ae0742b768676a6f623bef6873759621f3ba80cd28e955d5f0d04ef4.jpg)  
FIGURE 10. Reduction in accuracy (average over ten trials) for corruption of weights separately across GNN layers (first and second GCN layers, first 1-D convolutional layers, and second dense layer) for all the considered bioinformatics datasets for two error models.

in the accuracy reduction between the two error models for a considered layer. There is no particular trend observed between the error models. In some layers, Error ModelA has a higher accuracy reduction than Error ModelB, whereas it is the opposite for the remaining layers. Accuracy degradation depends on the weights’ value because the trend varies for the GNN layers between Error ModelA and Error ModelB.

# 3) EFFECT OF DATASET

Along with the difference in accuracy degradation with the GNN layer and error model, we also observe the variation in accuracy degradation with the dataset. Fig. 10 demonstrates the results of the accuracy degradation for the datasets— ENZYMES, PROTEINS, MUTAG, D&D, and NCI1 for the first and second GCN layers, first 1-D convolutional layers, and second dense layer. This variation is observed because of the change in weights of the GNN model with the dataset. Thus, a defender can choose an error model or the layer to be corrupted based on the dataset the GNN model is designed for.

The defender should consider the time taken to corrupt the weights along with accuracy degradation. The runtime of corruption is important since the defender has to ensure the weights are corrupted before an adversary collects a sufficient number of input–output pairs of GNNs. The time taken for the corruption of weights depends on the magnitude of reconfigure pulse of the proposed FeFET-based PUF. Thus, the magnitude of reconfigure pulse should be chosen in such a way that results in accuracy degradation and thwarts the attacker from collecting the inference of a sufficient number of queries. Furthermore, the magnitude of reconfigure pulse also determines the GNN layer to be corrupted. Next, we discuss the estimated runtime of the GNN model considered in this work. As mentioned above, we consider an in-memory compute architecture of GNNs, which is built using an array of multiply and accumulate (MAC) instances. Table 3 reports the runtime required for operations of each GNN layer. We consider a fixed size of MAC array, that is, 128 × 128, and runtime for the operations of a single cycle of MAC array as 1 ns. A defender can set the magnitude of rreconfiguredpulse of the PUF based on each layer’s runtime.

# C. DETECTING AND THWARTING PHYSICAL ATTACKS

Physical attacks can be detected in the proposed solution using resistance/capacitance sensor arrays [31] or

TABLE 3. Estimated runtime (ns) for all the GNN layers.   

<table><tr><td>GNN layer</td><td>Runtime (ns)</td></tr><tr><td>GCN Layer 1</td><td>2.5</td></tr><tr><td>GCN Layer 2</td><td>2.5</td></tr><tr><td>GCN Layer 3</td><td>2.5</td></tr><tr><td>GCN Layer 4</td><td>2.5</td></tr><tr><td>1-D Conv. Layer 1</td><td>14.5</td></tr><tr><td>1-D Conv. Layer 2</td><td>14.5</td></tr><tr><td>Dense Layer 1</td><td>6.5</td></tr><tr><td>Dense Layer 2</td><td>2.5</td></tr></table>

cryptographically secure mesh structures [32]. To deter an attacker from frequently querying the GNN, a mesh shield can be placed over the input—output terminals of the FeFET array. Any attempt to apply inputs through external leads will alter the data bit sequence through the mesh wires, thus detecting the incursion.

We note that physical incursions like cold-boot attacks are dependent on the delay between the logical turn-off of the memory cell and the time it takes to physically erase its remnant state [33]. Attackers can further increase this latency using cryogenic cooling to reduce the data entropy. In this scenario, the defender could try to erase all the IP information (stored weights) upon attack detection. However, data erasure incurs a write time penalty (O(µs)), which is much larger than the minuscule time taken to corrupt the FeFET PUF array in the proposed scheme (5 ns). Hence, attempting data erasure could still leave the attacker with ample time to obtain enough input–output data, whereas the FeFET PUF-based weight corruption will thwart such attacks.

# D. EVALUATION AGAINST MODEL EXTRACTION ATTACK

Here, we first discuss the methodology of the considered attack in [17] and evaluate the proposed obfuscation scheme against it. The steps of the attack in [17] are as follows.

1) The attacker chooses a random network and default weights/connections as the starting point.   
2) The attacker then repeatedly queries the golden GNN model to build an I/O dataset.   
3) After a sufficient number of I/O pairs are obtained, the random network is trained with them to be almost similar to the original network. However, the individual weights/connections inside this newly trained network will be vastly different than the original network, even though their I/O behavior is very similar.

![](images/30fdc6c31e7da6001d7f730f6317942727dc441a562165067575bfdefb57a73d.jpg)

![](images/5db3a0a3247e14178a15feb8294dac9b57090d00b18a55775d8be696eb123cc2.jpg)  
FIGURE 11. Accuracy (%) of recovered (surrogate) model for a GNN with no corruption and corruption in each individual layer with respect to I/O queries for error models A and B.

Here, we discuss the attack’s results on the GNN model with weight corruption. We launch the attack in [17] for the PubMed dataset. The original GNN model has three hidden layers with a dimension of 256. We consider four scenarios to compare the results, that is: 1) with no corruption in the original GNN model; 2) corruption in the weights of layer 1 of the original GNN model; 3) corruption in the weights of layer 2 of the original GNN model; and 4) corruption in the weights of layer 3 of the original GNN model. Fig. 11 demonstrates the accuracy of the recovered (surrogate) model for Error ModelA and ModelB with respect to the number of I/O queries. We observe that without corruption, the accuracy has increased with the increase in the number of I/O queries, whereas for the corrupted models, the accuracy of the recovered model remains the same, that is, in the range of ∼40%.

# IV. CONCLUSION

In this work, we propose a design-for-trust technique to protect the IP of NNs against model stealing or replication attacks that RE the weights of the NN model. In the proposed solution, an FeFET-based reconfigurable PUF is integrated with an in-memory FeFET XNOR array to corrupt the weights of the NN when an attack is detected. The corrupted weights result in accuracy degradation and thus, the attacker fails to obtain a sufficient number of input–output pairs for modelstealing attacks. We perform experiments on GNNs for the application of graph classification on different bioinformatics datasets. We are able to successfully corrupt the weights of the GNN model and degrade the accuracy of graph classification. Furthermore, we showcase an extensive analysis of the effect of layer-by-layer corruption of the GNN weights on its output accuracy. We also discuss various physical attack scenarios against the proposed defense scheme and explain how they are circumvented.

# ACKNOWLEDGMENT

The authors would like to thank Kai Ni from the Rochester Institute of Technology and Simon Thomann from the University of Stuttgart for their valuable help in FE modeling.

# REFERENCES

[1] K. He, X. Zhang, S. Ren, and J. Sun, ‘‘Deep residual learning for image recognition,’’ in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2016, pp. 770–778.   
[2] Y. Goldberg, ‘‘A primer on neural network models for natural language processing,’’ J. Artif. Intell. Res., vol. 57, pp. 345–420, Nov. 2016.   
[3] X. Zhang, C. Chen, Y. Xie, X. Chen, J. Zhang, and Y. Xiang, ‘‘A survey on privacy inference attacks and defenses in cloud-based deep neural network,’’ Comput. Standards Interfaces, vol. 83, Jan. 2023, Art. no. 103672.

[4] M. Xue et al., ‘‘DNN intellectual property protection: Taxonomy, attacks and evaluations,’’ in Proc. GLSVLSI, 2021, pp. 455–460.   
[5] F. Scarselli, M. Gori, A. Chung Tsoi, M. Hagenbuchner, and G. Monfardini, ‘‘The graph neural network model,’’ IEEE Trans. Neural Netw., vol. 20, no. 1, pp. 61–80, Jan. 2009.   
[6] J. Zhou et al., ‘‘Graph neural networks: A review of methods and applications,’’ AI Open, vol. 1, pp. 57–81, May 2020.   
[7] S. J. Oh et al., ‘‘Towards reverse-engineering black-box neural networks,’’ in Proc. ICLR, 2018, pp. 1–10.   
[8] M. Juuti, S. Szyller, S. Marchal, and N. Asokan, ‘‘PRADA: Protecting against DNN model stealing attacks,’’ in Proc. IEEE Eur. Symp. Secur. Privacy (EuroS&P), Jun. 2019, pp. 512–527.   
[9] N. Papernot, P. McDaniel, I. Goodfellow, S. Jha, Z. B. Celik, and A. Swami, ‘‘Practical black-box attacks against machine learning,’’ in Proc. ACM Asia Conf. Comput. Commun. Secur., Apr. 2017, pp. 506–519.   
[10] B. Wu, X. Yang, S. Pan, and X. Yuan, ‘‘Adapting membership inference attacks to GNN for graph classification: Approaches and implications,’’ in Proc. IEEE Int. Conf. Data Mining (ICDM), Dec. 2021, pp. 1421–1426.   
[11] X. He et al., ‘‘Node-level membership inference attacks against graph neural networks,’’ 2021, arXiv:2102.05429. [Online]. Available: https://arxiv.org/abs/2102.05429   
[12] X. He et al., ‘‘Stealing links from graph neural networks,’’ in Proc. USENIX Secur. Symp., 2021, pp. 2669–2686.   
[13] Z. Zhang et al., ‘‘Inference attacks against graph neural networks,’’ in Proc. USENIX Secur. Symp., 2022, pp. 4543–4560.   
[14] X. Wang and W. H. Wang, ‘‘Group property inference attacks against graph neural networks,’’ in Proc. ACM SIGSAC Conf. Comput. Commun. Secur. (CCS). Los Angeles, CA, USA: Association for Computing Machinery, 2022.   
[15] D. DeFazio and A. Ramesh, ‘‘Adversarial model extraction on graph neural networks,’’ 2019, arXiv:1912.07721. [Online]. Available: https://arxiv.org/abs/1912.07721   
[16] B. Wu, X. Yang, S. Pan, and X. Yuan, ‘‘Model extraction attacks on graph neural networks: Taxonomy and realisation,’’ in Proc. ACM Asia Conf. Comput. Commun. Secur., May 2022, pp. 337–350.   
[17] Y. Shen, X. He, Y. Han, and Y. Zhang, ‘‘Model stealing attacks against inductive graph neural networks,’’ in Proc. IEEE Symp. Secur. Privacy (SP), May 2022, pp. 1175–1192.   
[18] M. Zhang et al., ‘‘An end-to-end deep learning architecture for graph classification,’’ in Proc. AAAI, 2018, pp. 129–235.   
[19] C. Yang et al., ‘‘Thwarting replication attack against memristor-based [[neuromorphic]] computing system,’’ IEEE Trans. Comput.-Aided Design Integr. Circuits Syst., vol. 39, no. 10, pp. 2195–2205, Aug. 2019.   
[20] D. Rajasekharan et al., ‘‘SCANet: Securing the weights with superparamagnetic-MTJ crossbar array networks,’’ IEEE Trans. Neural Netw. Learn. Syst., early access, Dec. 15, 2021, doi: 10.1109/TNNLS.2021.3130884.   
[21] K. Ni et al., ‘‘On the channel percolation in ferroelectric FET towards proper analog states engineering,’’ in IEDM Tech. Dig., 2021, p. 15.   
[22] M. Yayla, S. Thomann, S. Buschjager, K. Morik, J.-J. Chen, and H. Amrouch, ‘‘Reliable binarized neural networks on unreliable beyond von-neumann architecture,’’ IEEE Trans. Circuits Syst. I, Reg. Papers, vol. 69, no. 6, pp. 2516–2528, Jun. 2022.   
[23] H. Mulaosmanovic, E. T. Breyer, S. Dünkel, S. Beyer, T. Mikolajick, and S. Slesazeck, ‘‘Ferroelectric field-effect transistors based on [[HfO2]]: A review,’’ Nanotechnology, vol. 32, no. 50, Sep. 2021, Art. no. 502002.   
[24] Q. Liu et al., ‘‘High performance UTBB FDSOI devices featuring 20 nm gate length for 14 nm node and beyond,’’ in IEDM Tech. Dig., 2013, p. 9.   
[25] S. Chatterjee et al., ‘‘Comprehensive variability analysis in dual-Port FeFET for reliable multi-level-cell storage,’’ IEEE Trans. Electron Devices, vol. 69, no. 9, pp. 5316–5323, Sep. 2022.   
[26] X. Guo et al., ‘‘Exploiting FeFET switching stochasticity for lowpower reconfigurable physical unclonable function,’’ in Proc. ESSCIRC, Sep. 2021, pp. 119–122.   
[27] H. Mulaosmanovic, T. Mikolajick, and S. Slesazeck, ‘‘Random number generation based on ferroelectric switching,’’ IEEE Electron Device Lett., vol. 39, no. 1, pp. 135–138, Jan. 2018, doi: 10.1109/LED.2017.2771818.   
[28] K. Ni et al., ‘‘Ferroelectric ternary content-addressable memory for oneshot learning,’’ Nature Electron., vol. 2, no. 11, pp. 521–529, 2019.   
[29] M. Yasin et al., ‘‘Provably-secure logic locking: From theory to practice,’’ in Proc. ACM SIGSAC Conf. Comput. Commun. Secur. (CCS). New York, NY, USA: Association for Computing Machinery, 2017, pp. 1601–1618.

[30] M. Zhang et al., ‘‘Deep graph convolutional neural network (DGCNN),’’ 2018. [Online]. Available: https://github.com/muhanzhang/DGCNN   
[31] P. Tuyls et al., ‘‘Read-proof hardware from protective coatings,’’ in Proc. Int. Workshop Cryptograph. Hardw. Embedded Syst. Cham, Switzerland: Springer, 2006, pp. 369–383.   
[32] J.-M. Cioranesco et al., ‘‘Cryptographically secure shields,’’ in Proc. IEEE Int. Symp. Hardw.-Oriented Secur. Trust (HOST), May 2014, pp. 25–31.   
[33] J. A. Halderman et al., ‘‘Lest we remember: Cold-boot attacks on encryption keys,’’ Commun. ACM, vol. 52, no. 5, pp. 91–98, 2009.

![](images/dfdbf5a6c317ed1b002dc05ac6d1a77aee817bb618795b32c1b0531091ceffe9.jpg)

SHUBHAM KUMAR (Graduate Student Member, IEEE) is currently pursuing the master’s and Ph.D. degrees with the Department of Electrical Engineering, Indian Institute of Technology Kanpur, Kanpur, Uttar Pradesh, India.

He is currently hosted at the Chair of Semiconductor Test and Reliability (STAR), University of Stuttgart, Stuttgart, Germany, as a Research Scholar. His current research interests include in-memory computing, hyperdimensional

computing, neuromorphic computing, and hardware security.

![](images/9036789a7d3ccc21240bed0b3e5ccadbfe3971080e7be6ed15523da427ee8081.jpg)

LIKHITHA MANKALI (Student Member, IEEE) is currently pursuing the Ph.D. degree with the Department of Electrical and Computer Engineering, Tandon School of Engineering, New York University, New York City, NY, USA.

She is a Global Ph.D. Fellow with New York University Abu Dhabi, Abu Dhabi, United Arab Emirates. Her research interests include hardware security, and using machine learning for enhancing and quantifying the security of IP protection techniques.

![](images/d1176986315cc7cae76b747f63dc41f761704f5a44b5faa9d63133acbc098f90.jpg)

YOGESH SINGH CHAUHAN (Fellow, IEEE) is a Chair Professor at the Indian Institute of Technology Kanpur, Kanpur, India. He has previously worked at IBM Bangalore, Bengaluru, India, the Tokyo Institute of Technology, Tokyo, Japan, the University of California at Berkeley, Berkeley, CA, USA, and ST Microelectronics. He is also the developer of several industry standard models, such as ASM GaN HEMT and BSIM models. His research interests include characterization, model-

ing, and simulation of semiconductor devices.

Dr. Chauhan received the Ramanujan Fellowship in 2012, the IBM Faculty Award in 2013, the P. K. Kelkar Fellowship in 2015, the CNR Rao Faculty Award, and the Humboldt Fellowship and Swarnajayanti Fellowship in 2018.

![](images/f849fa56f2756dd553977055887238339b8573fe4a35d8886f03bc3fcef690b1.jpg)

NIKHIL RANGARAJAN (Member, IEEE) received the M.S. and Ph.D. degrees in electrical engineering from New York University, New York City, NY, USA.

He is a Post-Doctoral Associate at the Division of Engineering, New York University Abu Dhabi, Abu Dhabi, United Arab Emirates. His research interests include spintronics, nanoelectronics, device physics, and hardware security. His current work aims to explore the security

implications of emerging devices-based logic and memory paradigms.

![](images/791bc17ec5ea06a36d2860e99a085ca7f06f65d1ea03d0bcaf48c94d24f63be3.jpg)

OZGUR SINANOGLU (Senior Member, IEEE) received the Ph.D. degree in computer science and engineering from the University of California at San Diego, La Jolla, CA, USA.

He is a Professor of electrical and computer engineering at New York University Abu Dhabi, Abu Dhabi, United Arab Emirates, where he is the Director of the Center for CyberSecurity. He has industry experience at TI, IBM, and Qualcomm. His current research is being funded by the U.S.

National Science Foundation, the U.S. Department of Defense, Semiconductor Research Corporation, Intel Corporation, and Mubadala Technology. His research interests include design-for-test, design-for-security, and designfor-trust for VLSI circuits.

Dr. Sinanoglu won the IBM Ph.D. Fellowship Award twice during his Ph.D. He was a recipient of the best paper awards at the IEEE VLSI Test Symposium in 2011 and the ACM Conference on Computer and Communication Security in 2013.

![](images/b0fc19a889cfc2184909af0599b4c6fe980be623e69141a1824838e0972fb793.jpg)

SWETAKI CHATTERJEE (Graduate Student Member, IEEE) is currently pursuing the master’s and Ph.D. degrees with the Department of Electrical Engineering, Indian Institute of Technology Kanpur, Kanpur, Uttar Pradesh, India.

He is currently hosted at the Chair of Semiconductor Test and Reliability (STAR), University of Stuttgart, Stuttgart, Germany, as a Research Scholar. His research focuses on emerging transistor technologies especially ferroelectric devices

for unconventional computing applications, such as hardware security, logicin-memory, and in-memory-computing.

![](images/8d1ab4159da499e64b25a63de10a15670827b0d76fe9fa11aff17593cb3c21ea.jpg)

HUSSAM AMROUCH (Member, IEEE) received the Ph.D. degree (summa cum laude) from the Karlsruhe Institute of Technology (KIT), Karlsruhe, Germany, in 2015.

He is a Jun.-Professor heading the Chair of Semiconductor Test and Reliability (STAR), University of Stuttgart, Stuttgart, Germany.

Dr. Amrouch has served as a reviewer in many top journals, such as Nature Electronics. He has around 190 publications (including 78 journals)

in multidisciplinary research areas across the entire computing stack. He currently serves as an Editor for the Nature Scientific Reports journal. His research in HW security and reliability have been funded by the German Research Foundation (DFG), Advantest Corporation, and the U.S. Office of Naval Research (ONR).