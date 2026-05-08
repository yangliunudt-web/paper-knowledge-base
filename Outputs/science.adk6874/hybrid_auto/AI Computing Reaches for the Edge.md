---
title: "AI Computing Reaches for the Edge"
date: "'2023-08-24'"
year: 2023
journal: "Science"
doi: "10.1126/science.adk6874"
abstract: "These findings have important implications for understanding neurodegenerative"
abstract_cn: "Science 视角文章讨论 IBM NorthPole 芯片，一种用于边缘 AI 计算的数字类脑架构。NorthPole 具有 256"
cite: "'Dharmendra S. Modha. AI Computing Reaches for the Edge[J]. Science, 2023. DOI:"
aiSum: "NorthPole 边缘 AI 芯片：256 核心，224MB 片上存储，>1000 帧/焦耳能效，数字类脑架构。"
confidence: high
---

that rats could form a long-term associative memory in the absence of theta and replay sequences; this suggests that the expression of cell assemblies and their later reactivation during rest periods may be sufficient for core component processes of episodic memory.

These findings have important implications for understanding neurodegenerative and neurodevelopmental disorders that affect episodic memory, including Alzheimer’s disease and autism spectrum disorder. Finding that associative memory and predictive capabilities may be supported by dissociable neuronal codes could mean that these specific facets of episodic memory are differentially affected in these disorders and/or are affected at different stages of a progressive disorder, such as Alzheimer’s disease. Hopefully, future research will investigate associative and predictive capabilities in neurological conditions.

Additionally, the findings by Liu et al. raise questions about whether the putative hippocampal predictive code holds for other tasks that draw on predictive capabilities. One interpretation of the result is that the predictive code (expressed through sequential hippocampal activity) was required for the spatial navigation task because of its sequential nature. Perhaps future studies can assess whether the hippocampal predictive code is also involved in more generic prediction learning. For example, does it help guide navigation when barriers are introduced into a familiar environment?

Investigating the role of the predictive code in inferential reasoning (inferring a relationship between two different events) is also an important research avenue. The ability to use spatiotemporal information to make inferences is central to predictive capabilities, as noted by Liu et al. and others (2, 4). Does the described hippocampal predictive code guide learning when, for example, an animal needs to find reward in a previously unseen environment that is similar to a familiar environment? Identifying the neuronal coding scheme supporting such inferential reasoning represents an exciting research frontier. j

# REFERENCES AND NOTES

10.1126/science.adk4642

# COMPUTER SCIENCE

# AI computing reaches for the edge

A chip design integrates computation and memory to efficiently process data at low energy cost

# By Subramanian S. Iyer and Vwani Roychowdhury

rtificial intelligence (AI)—the ability of computers to perform human cognitive functions in real-world scenarios—requires substantial computation power, energy, and vast datasets. Once trained, AI models are deployed to make predictions (inferences) for new situations. In the traditional paradigm, inference is supported by centralized, high-performance computational platforms and high-bandwidth network connections. However, in real-time

mission-critical applications such as facial recognition, object detection tracking, and behavior monitoring, an “edge” computing system is desirable, for fast and accurate inference and, hence, fast response times. Edge computing requires moving the large AI model from a centralized location to a position closer to the source of data (hence, working at the edge). On page

329 of this issue, Modha et al. (1) describe a computing platform called “NorthPole” that facilitates high inference speed and prediction accuracy but with a moderate energy requirement. This is a promising step toward chip designs that support lowpower edge AI inference.

Learning integrates immense sets of experiential data that are located in large, centralized data centers. It is an energy-, computing-, memory-, and time-intensive set of operations that results in a trained network with learned parameters (such as a weight value of input data). The trained model often comprises billions of parameters. Thus, the inference task is computationally demanding and primarily consists of matrix-vector multiplication operations, referred to as multiply and accumulate computations (MACs). Devices “at the

Electrical and Computer Engineering Department, Samueli School of Engineering, University of California, Los Angeles, CA, USA.Email: s.s.iyer@ucla.edu; vwani@ucla.edu

edge” that monitor and track in real time, for example, must communicate with powerful centralized AI models and then bring information back to the edge. This route is fraught with bandwidth limitations, latency problems, and potential disruption to networks. The objective of edge computing is to bring the large AI model to the edge, to accelerate inference. However, this requires a system at the edge that supports computation while simultaneously accessing data—much like the human brain.

Modha et al. designed a brain-inspired computer chip architecture that focuses on efficiently performing inference tasks

“…a promising step toward chip designs that support low-power edge AI inference.”

with technological, algorithmic, and software innovations. The platform uses a two-dimensional array of cores (computing units or, simply, compute units) and associated memory blocks that store weights of AI models. The MACs required for inferencing are assigned to different compute cores, each facilitating the multiplication of the weights of an AI

model against input data. This requires that necessary weights be routed to the appropriate cores on demand, a high energy-consuming task. One innovation of NorthPole is the ability to share compute and memory (weights) across the chip with no or minimal hierarchy. This means that a core compute unit can access memory that is both spatially close as well as far across the chip with almost equal ease. Another notable achievement by Modha et al. is that the chip, architecture, and software are co-optimized for edge inference and adapted to standard semiconductor technology for manufacturing integrated circuits. Because NorthPole is a digital system, it also has the advantage of being resistant to device noise and systemic biases and drifts that afflict analog systems. The primary source of inference error, however, is the use of limited-precision (number of bits) arithmetic operations for MACs. Nevertheless, NorthPole’s 256 cores and 224 MB of on-chip memory can operate

at a frequency range of 25 to 425 MHz, with an energy consumption of >1000 frames per joule, making it suitable for applications that include a self-driving car.

A limitation of Modha et al.’s approach is its relatively high power requirements when scaled to large AI models. This is partly due to the data architecture (how data are collected, stored, and flowed through the system) that permits lowlatency inference by making data transfers possible from memory located both near and far across the chip. Increased power and size demands also arise from elabo-

rate peripheral chips (such as field-programmable gate arrays coprocessors) and memory that are needed to power up the compute-memory integrated chip from a cold start. From this perspective, an edge device using NorthPole must have access to a reasonably high-power source and incur any associated increase in its size. Several applications of AI inference chips,

however, include functioning within sufficiently powerful machines such as automobiles, aircraft, and military vehicles, which would benefit from the chip design of Modha et al.

In the quest for lower-power AI edge inference accelerators, a somewhat different architecture called compute-in-memory (CIM) has been explored (2). CIM brings memory (weights) and compute (multipliers) units physically close together, at the level of the multiplier units used in MACs (recall that MACs are the primary operations required for inference). CIM can be either digital or analog. In digital CIMs, the weights are stored as bits using static random-access memory (which retains data as long as power is being supplied) and the multiplication is finite precision binary arithmetic, similar to the operation used by Modha et al. An analog CIM is more elegant in that it directly uses Ohm’s law to perform multiplication and uses a capacitor as an adder. It has potentially much lower power needs compared to digital MACs. The weights are stored as the conductance of a conductive element, and current flowing through the element is proportional to the product of input (applied voltage) and the conductance (weights). The currents through several such elements are added to provide the primary inference functionality. In principle, this MAC operation is very fast, and the power for inference is attractively low.

The challenge, especially in the analog CIM approach, lies in the choice of the

conductive element and the resolution of its conductance, which determines the resolution of the weights. In one example, a combination of several phase-change memory elements is used to store the weights (3). However, such analog CIM systems require the integration of new materials, which necessitates the addition of specialized steps to the industry-standard manufacturing process for complementary metal oxide semiconductors. An approach that addresses this obstacle requires instead a standard semiconductor device that traps charge (called the charge trap

transistor) and uses it to tune its resistance and achieve an estimated 8 equivalent bits of resolution in the resulting weights (4).

A disadvantage of analog techniques is that programming the weights is cumbersome, time consuming, and energy intensive. Thus, more suitable for edge applications would be AI models that are updated only occasionally. In

both analog CIM and digital approaches, precision of the weights and computations play a key role in accelerating inference. Thus, more work is necessary on designing training algorithms to yield AI models that are robust to both reduction in precision and systemic biases in analog devices. Recent progress reported for analog (2) and digital (5) platforms is encouraging.

Innovative chip architecture and digital approaches such as those reported by Modha et al. will play an important role in the near-term development of edgebased inference with moderate-size platforms. However, analog approaches may ultimately bring real-time AI to hand-held edge devices, especially as the enabling technologies become more mainstream and easily manufacturable. j

# REFERENCES AND NOTES

10.1126/science.adk6874

# PHOTONICS

# Tracking lightinduced charge transport

P recise charge dynamics could help to improve the operation of solar cells and sensors

By Rachel E. Bangle and Maiken H. Mikkelsen

ey to developing photocatalytic and solar cells is understanding charge dynamics. Light absorption in metals can initiate charge transport by exciting electrons to form high-energy “hot” charges, but this energy is rapidly lost as heat (1). To capture the extra energy that hot charges (or carriers) possess before they decay and use it to generate an electrical current, the carriers must be transported across an interface called a transport junction. The movement of hot charges determines the efficiency of these junctions. However, hot-carrier dynamics are notoriously difficult to measure owing to their ultrashort lifetimes (2–4). On page 299 of this issue, Taghinejad et al. (5) show that ejection of hot carriers at a transport junction produce terahertz (THz, 1012 Hz) radiation that provides information exclusively on hot-carrier dynamics. This could provide a reliable way to characterize hot carriers and thereby aid the design of sensors and solar cells.

Hot carriers are formed when collectively oscillating electrons, called plasmons, transfer energy within the metal to form excited electron and hole (positive charge) states on timescales of <100 fs (1 fs = 10-15 s). This initial state is very energetic and thus outside of the usual thermal equilibrium of electrons in metal. However, nonequilibrium carriers rapidly (<1 ps, 1 ps = 10-12 s) spread that energy among a larger electron population through scattering collisions. This raises the average electron temperature, and the electrons quickly (<100 ps) dissipate the excess energy to the metal lattice as heat. Hot-carrier extraction can occur during

Department of Electrical and Computer

Engineering, Duke University, Durham, NC, USA.

Email: m.mikkelsen@duke.edu
