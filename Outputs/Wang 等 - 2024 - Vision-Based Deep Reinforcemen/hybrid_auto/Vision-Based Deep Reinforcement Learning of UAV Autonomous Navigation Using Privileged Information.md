---
title: "Vision-Based Deep Reinforcement Learning of UAV Autonomous Navigation Using"
authors:
  - "Jian Wang"
  - "Xiaoyu Zhang"
  - "Yuan Xu"
  - "Xin Li"
  - "Feng Zhou"
date: "2024-06-15"
year: 2024
journal: "IEEE Transactions on Cybernetics"
abstract: "The capability of UAVs for efficient autonomous navigation and obstacle avoidance in complex environments is critical for practical applications. This work proposes a vision-based deep reinforcement learning approach using privileged information for UAV autonomous navigation. An asymmetric Actor-Critic architecture leverages privileged information during training to enhance perception. A multi-agent exploration strategy accelerates experience collection. Experiments demonstrate superiority over existing methods in flight efficiency, robustness, and success rate."
abstract_cn: "无人机在复杂环境中高效自主导航和避障的能力对其实际应用至关重要。本文提出一种基于视觉的深度强化学习方法，利用特权信息实现无人机自主导航。采用非对称Actor-Critic架构在训练期间利用特权信息增强感知能力，提出多智能体探索策略加速经验收集。实验表明该方法在飞行效率、鲁棒性和成功率方面优于现有方法。"
keywords:
  - "[[Reinforcement learning]]"
  - "[[UAV]]"
  - "[[Autonomous navigation]]"
  - "[[Privileged information]]"
  - "[[深度强化学习]]"
  - "[[无人机导航]]"
cite: "[1] Wang J., et al. Vision-Based Deep Reinforcement Learning of UAV Autonomous"
aiSum: "采用深度强化学习+特权学习的方法，解决无人机在复杂环境下的自主导航问题。提出了非对称Actor-Critic架构和多智能体探索策略。实验在多种仿真场景中验证，算法在成功率、效率和鲁棒性方面优于TD3和EGO-Planner-v2。"
confidence: "medium"
---

title: "Vision-Based Deep Reinforcement Learning of UAV Autonomous Navigation Using Privileged Information"
authors:
  - "Junqiao Wang"
  - "Zhongliang Yu"
  - "Dong Zhou"
  - "Jiaqi Shi"
  - "Runran Deng"
journal: "Unknown Journal"
year: "2024"
keywords:
  - [[Reinforcement learning]]
  - [[UAV]]
  - [[Navigation]]
  - [[Obstacle avoidance]]
abstract: |
  The capability of UAVs for efficient autonomous navigation and obstacle avoidance in complex and unknown environments is critical for applications in agricultural irrigation, disaster relief and logistics. In this paper, we propose the DPRL (Distributed Privileged Reinforcement Learning) navigation algorithm, an end-to-end policy designed to address the challenge of high-speed autonomous UAV navigation under partially observable environmental conditions. Our approach combines deep reinforcement learning with privileged learning to overcome the impact of observation data corruption caused by partial observability. We leverage an asymmetric Actor-Critic architecture to provide the agent with privileged information during training, which enhances the model’s perceptual capabilities. Additiona...
abstract_cn: |
  研究提出了DPRL（分布式特权强化学习）导航算法，这是一种端到端策略，用于解决部分可观测环境下的高速无人机自主导航挑战。该方法结合深度强化学习与特权学习，利用非对称Actor-Critic架构在训练期间提供特权信息，增强模型的感知能力。同时提出多智能体探索策略加速经验收集。实验表明，该算法在飞行效率、鲁棒性和成功率方面优于现有方法。
aiSum: |
  采用深度强化学习+特权学习的方法，解决无人机在复杂环境下的自主导航问题。提出了非对称Actor-Critic架构和多智能体探索策略。实验在多种仿真场景中验证，算法在成功率、效率和鲁棒性方面优于TD3和EGO-Planner-v2。
cite: "[1] Wang J., et al. Vision-Based Deep Reinforcement Learning of UAV Autonomous Navigation Using Privileged Information[J/OL]. arXiv, 2024. 2106.01016."

# Vision-Based Deep Reinforcement Learning of UAV Autonomous Navigation Using Privileged Information

Junqiao Wang

23S004019@stu.hit.edu.cn

Zhongliang Yu

zlyu@cqu.edu.cn

Dong Zhou

dongzhou@hit.edu.cn

Jiaqi Shi

22s104188@stu.hit.edu.cn

Runran Deng

deng_run_ran@126.com

# Abstract

The capability of UAVs for efficient autonomous navigation and obstacle avoidance in complex and unknown environments is critical for applications in agricultural irrigation, disaster relief and logistics. In this paper, we propose the DPRL (Distributed Privileged Reinforcement Learning) navigation algorithm, an end-to-end policy designed to address the challenge of high-speed autonomous UAV navigation under partially observable environmental conditions. Our approach combines deep reinforcement learning with privileged learning to overcome the impact of observation data corruption caused by partial observability. We leverage an asymmetric Actor-Critic architecture to provide the agent with privileged information during training, which enhances the model’s perceptual capabilities. Additionally, we present a multi-agent exploration strategy across diverse environments to accelerate experience collection, which in turn expedites model convergence. We conducted extensive simulations across various scenarios, benchmarking our DPRL algorithm against the state-of-the-art navigation algorithms. The results consistently demonstrate the superior performance of our algorithm in terms of flight efficiency, robustness and overall success rate.

# 1 Introduction

Drones, also known as unmanned aerial vehicles (UAVs), have rapidly evolved in recent years, playing a pivotal role in various industries due to their efficiency and versatility[1]. One of the key advantages of drones is their ability to efficiently operate in challenging or unpredictable environments without endangering human lives[2], making them well-suited for tasks such as monitoring large agricultural fields[3], navigating complex logistics routes[4], and conducting post-disaster search and relief operations[5]. As drones continue to demonstrate their value across various applications, the ability to autonomously navigate in unknown complex environments becomes increasingly critical and has gradually gained significant attention.[11, 40, 41, 42]

Current autonomous drone navigation systems rely on a variety of sensors, including LiDAR, cameras, radar, GPS, RTK, and inertial measurement units (IMUs), to perceive with their environment[9]. Among these sensors, cameras offer significant advantages due to their lightweight, low power consumption, and cost-effectiveness[10], yet they provide high-resolution information about the surrounding environment, such as color and texture, making them preferable to other sensors like LiDAR for small drones with limited payload capacity[39]. In recent years, numerous UAV visual navigation algorithms based on onboard cameras have emerged, utilizing visual information for obstacle detection and avoidance[43, 44], visual odometry[45, 46], Simultaneous Localization and Mapping (SLAM)[16, 15], motion planning[14, 47], and flight control[31, 48].

![](images/d2e217cf0f73d5d2731c0273798e643f8327660d75c39e2ee862c97a60ee719c.jpg)  
Figure 1: The DPRL Framework for UAV Navigation.

In visual navigation, traditional algorithms, though widely used, often rely on hand-crafted features and predefined models, making them less adaptable to highly dynamic and complex environments, especially in the presence of noisy sensory data[12, 38]. These methods generally require precise tuning and struggle with unforeseen obstacles or changing conditions, leading to decreased efficiency and safety. However, deep reinforcement learning (DRL) offers significant advantages for visual navigation by enabling systems to learn navigation policies directly from raw visual data through trial and error[14, 54]. This kind of method reduces the need for extensive feature engineering and allows drones to autonomously adapt to uncertainties in complex environments, such as dynamic obstacles[7] and varying lighting conditions[8], thereby enhancing robustness and flexibility.

Despite the recent advances made by deep reinforcement learning-based visual navigation algorithms, they often overlook the impact of partial observability in the environment, which can severely affect the decision-making effectiveness of these models[13] and significantly degrade their performance when transitioning to real-world environments. Additionally, existing deep reinforcement learning-based visual navigation methods often struggle with low efficiency in experience collection, particularly in complex environments where successful flights are challenging to achieve, leading to slow model convergence[37].

To address the above issues, we propose the DPRL algorithm for UAV visual navigation, the algorithm framework is shown in Figure 1. DPRL incorporates an asymmetric Actor-Critic network structure, where the Critic network receives accurate, noise-free privileged perception information during training, enabling the model to build resilience against the interference in perception data caused by partial observability in the environment. Additionally, we propose a multi-agent exploration strategy which facilitates asynchronous experience collection across multiple environments to accelerate model convergence. This algorithm enables high-speed obstacle avoidance for UAVs in complex and unknown environments, while taking into account the inaccuracy of observations. The main contributions are summarized as follows:

1. We integrate deep reinforcement learning with privileged learning by providing accurate perception information to the Critic network during training, which greatly enhances the model’s ability to handle environment uncertainties.   
2. We propose a multi-agent exploration strategy where multiple UAVs asynchronously operate in simulated environments to collect experiences, enhancing efficiency and accelerating convergence.

3. We validated the algorithm’s advantages in success rate, efficiency, and robustness over TD3 and EGO-Planner-v2, with ablation studies confirming its design effectiveness.

The rest of the paper is organized as follows: Section 2 discusses related work on autonomous UAV navigation and obstacle avoidance algorithms. Section 3 introduces the proposed algorithm in this study. Section 4 describes the experimental setup, results, and analysis. Section 5 provides a conclusion and outlines future work.

# 2 Related Work

# 2.1 Vision-based UAV Navigation

Traditional approaches achieve autonomous UAV navigation and obstacle avoidance by performing sequential, cascaded tasks, often using visual navigation frameworks that leverage depth images to construct point cloud maps[15, 16, 17], which are then used for path planning[18, 19, 20, 21, 22] and flight control[23, 24, 25, 26]. Fast-Planner developed by Shen et al.[49, 50, 51], follows this pattern, constructs a grid map by combining depth camera data with localization information, employs a hybrid $\mathbf { A } ^ { * }$ algorithm for global path planning, optimizes trajectories using B-splines with automatic time allocation adjustments, and designs a controller for trajectory tracking. Recently, Zhou et al.[6] enhanced this framework and introduced EGO-Planner-v2, which achieves precise localization through visual-inertial odometry (VIO) based on grayscale images and IMU data, constructs a probabilistic map using depth images and localization data, conducts spatiotemporal trajectory planning based on this map and designs a controller to track the planned trajectory, enabling UAVs to navigate autonomously in complex outdoor environments.

While the frameworks mentioned above offer high interpretability and precise navigation with accurate maps, their cascading task structure often fails to capture interactions between tasks, leading to error accumulation. Additionally, map building and storage require substantial resources, lowering frame rates and limiting responsiveness to dynamic environmental changes, which reduces obstacle avoidance efficiency[8]. Recent advancements in deep learning have led to end-to-end visual navigation frameworks based on supervised learning that directly map perception to control[27, 28, 48]. These models, though less interpretable, eliminate cumulative error and the need for map storage, saving computational resources and improving adaptability to dynamic environments.

While supervised approaches struggle with data labeling and often overfit, deep reinforcement learning methods require no prior knowledge, instead learning through environmental interaction to develop robust obstacle avoidance strategies. Kalidas et al.[1] considered dynamic obstacle avoidance and established three simulation environments using AirSim. In these simulated environments, they trained and compared the performance of three deep reinforcement learning algorithms: DQN, PPO, and SAC. Myoung et al.[30] incorporated the Hindsight Experience Replay (HER) algorithm into the SAC framework to address the issue where the maximum entropy optimization objective in SAC may reduce the optimality of policy. They compared the proposed SACHER algorithm with SAC and DDPG, demonstrating its superiority. He et al.[52] proposed a model explanation method based on feature attribution to analyze the mapping relationship between features and decisions in reinforcement learning policy networks during the learning process. This approach enables better adjustment of network structures to enhance model performance. Their algorithm was validated in both simulation and real-world environments.

# 2.2 Strategies to Accelerate DRL Convergence

One of the major challenges in deep reinforcement learning algorithms is the low efficiency of experience collection, which leads to slow model convergence. Researchers have proposed various methods to address this issue. To tackle the inefficiency of experience selection, Hu et al.[53] combined curriculum learning with an improved prioritized experience replay (PER) method by launching independent threads to assign sampling priorities based on the current curriculum difficulty and the TD error of the experiences. They further eliminated low-priority experiences to improve the efficiency of selecting valuable experiences for model updates. However, curriculum learning is often limited by the rationality of difficulty settings, and significant changes in the distribution of observed data after curriculum transitions can cause noticeable performance degradation in the model.

Given the challenges in ensuring the effectiveness of curriculum learning’s difficulty settings and transition mechanisms, many studies have shifted their focus toward learning from demonstration. He et al.[37] adopted imitation learning by using the 3DVHF* algorithm as an expert policy. They pre-trained the Actor and Critic networks of the reinforcement learning model in a supervised manner using expert-generated experiences before allowing the model to interact with the environment to further enhance its navigation and obstacle avoidance capabilities. However, the interaction experiences significantly impact the pre-trained weights, requiring partial layers of the decision model to be frozen to prevent large parameter changes.

Due to the problem of model performance degradation caused by significant changes in training scenarios and experience distributions, many studies have turned to refining action selection methods. Xie et al.[29] modified the action selection strategy by building on the ϵ-greedy method. They incorporated rewards and Q-value estimates to select actions, avoiding errors caused by inaccurate Q-value estimates during the early training stages. This ensures that UAVs maximize their movement in the early training phase to collect diverse environmental data. However, this strategy is only suitable for discrete action spaces. In cases with large or continuous action spaces, it becomes difficult to effectively evaluate all possible actions, leading to reduced efficiency.

To efficiently utilize incomplete and noisy perceptual information while ensuring accelerated model convergence and robust decision-making, many studies have explored the application of privileged learning. Kaufmann et al.[31] addressed the issue of estimation errors in VIO by employing privileged learning, where the Critic network is provided with accurate pose and velocity information during model training. This approach enables the effective use of inaccurate experiences, thereby accelerating convergence. However, in UAV visual navigation tasks where environmental information is only partially observable, providing accurate pose data alone is insufficient to mitigate the impact of perception noise. To address this, we employed an asymmetric Actor-Critic structure, supplying the Critic network with all accurate observational data, including noise-free depth images, as privileged information to counteract the effects of corrupted observations due to partial observability. Furthermore, we proposed a multi-agent exploration strategy in which multiple agents asynchronously collect experiences across various environments, populating a centralized experience replay buffer. This buffer is used to update a central model, significantly improving the efficiency of experience collection and accelerating model convergence.

# 3 Methodology

The framework of our proposed DPRL navigation algorithm is illustrated in Figure 1. In this framework, each UAV independently and asynchronously collects interaction experiences within its respective environment. Accurate state data are obtained through onboard sensors and subsequently perturbed with noise to simulate observations under partially observable environmental conditions. The accurate and inaccurate observation data are used as privileged information and normal sensory input, respectively, and are fed into the Critic and Actor networks. The Critic network evaluates the state-action pair’s value, while the Actor network generates action outputs based on the current observations to control each UAV’s flight in its designated environment.

# 3.1 Problem Formulation

In this section, we first model the autonomous navigation task of an unmanned aerial vehicle (UAV) as a Partially Observable Markov Decision Process (POMDP), following the modeling approach of Zhou et al. [55]. Building on this framework, we then discuss the key components of reinforcement learning (RL) that drive the UAV’s autonomous navigation.

A Partially Observable Markov Decision Process is characterized by a tuple $< s , o , a , r , p , \gamma >$ , representing states, observations, actions, transition probabilities, rewards, and discount factor, respectively. For the UAV navigation task, we define these elements as follows:

1. State(s): The state represents the current environment context and UAV status, which may include the UAV’s position, velocity, orientation, proximity to obstacles, and sensor readings.   
2. Observation(o):The Observation refers to the information gathered by an agent to infer the state of its environment. In partially observable environments, the UAV cannot directly

access the full state information. Instead, it depends on observations collected from its onboard sensors, which offer a noisy and incomplete representation of the surrounding environment.

3. Action(a): The action space consists of the possible control commands that the UAV can take at each time step. These actions may include altering the UAV’s speed, direction, or altitude.   
4. Transition Probability(p): The transition probability defines the likelihood of reaching a new state given the current state and an action. In the context of UAV autonomous navigation, the state transition is determined by the UAV’s dynamics, which is influenced by factors such as control inputs, environmental conditions, and system noise.   
5. Reward(r): The reward function evaluates the immediate performance of the UAV based on its action in a particular state. The objective is to design a reward function that encourages the UAV to navigate efficiently towards its destination while avoiding collisions.   
6. Discount Factor(γ): The discount factor determines the importance of future rewards relative to immediate rewards. A value close to 1 implies that future rewards are highly significant, which helps in encouraging long-term goal achievement.

The key components of reinforcement learning are the agent, policy, and environment. The agent refers to the entity that performs actions and interacts with the environment; in the context of UAV autonomous navigation, this is the UAV itself. The policy serves as the decision-making guideline, which enables the agent to select actions based on its observations of the environment. The environment encompasses all external factors that the UAV must navigate, including terrain, obstacles, and dynamic elements that influence the UAV’s state.

At each time step, the agent selects an action from a predefined action space, receives feedback in the form of a reward, and transitions to a new state based on the environment’s response. This cycle continues as the agent gathers experience to refine its policy, ultimately learning an optimal strategy for safe and efficient navigation in complex environments.

# 3.2 Privileged Reinforcement Learning

In this section, we present the core of the UAV autonomous navigation framework: the deep reinforcement learning policy network integrated with privileged learning. We begin by introducing the reward function design tailored to this study, which plays a critical role in guiding the UAV’s behavior. Next, we detail the integration of deep reinforcement learning with privileged learning, explaining how privileged information is utilized during training to enhance model performance, along with the policy update mechanism. Finally, we describe the specific network architecture designed to effectively implement the proposed framework and handle the challenges of partially observable environments.

# 3.2.1 Reward Function Design

In our work, We have designed a reward function that incorporates both continuous and sparse rewards. At the end of each training episode, the agent receives sparse rewards, including a goal-reaching reward, a collision penalty, and an out-of-bounds penalty. Specifically, when the drone enters the target zone (within 2 meters), it is awarded a positive reward of +10. Conversely, if the drone collides with obstacles or exceeds the environment boundaries, it incurs a negative reward of −5.

In addition, the agent is given continuous rewards at each time step. These consist of a distance differential reward, a distance error penalty, and a collision proximity penalty. The distance differential reward evaluates the reduction in distance between the agent and the target from the previous time step to the current one. The distance error penalty is computed based on the distance between the drone and the straight line connecting the starting point and the target at each time step. The collision proximity penalty is determined by the difference between the shortest distance from the drone to any obstacle and the predefined safety distance at each time step. The expression for the continuous reward is shown in equation 1.

$$
\left\{ \begin{array}{l} r _ {e} = \frac {d _ {t - 1} - d _ {t}}{d _ {g}} \\ p _ {p} = \left| \operatorname {c l i p} \left(\frac {d _ {l}}{1 0}, 0, 1\right) \right| + 2 \cdot \left| \operatorname {c l i p} \left(\frac {z - z _ {g}}{5}, - 1, 1\right) \right| \\ p _ {o} = \left\{ \begin{array}{l l} 1 - \operatorname {c l i p} \left(\frac {d _ {o} - d _ {c}}{d _ {s} - d _ {c}}, 0, 1\right) & \text {i f} d _ {o} <   d _ {s} \\ 0 & \text {i f} d _ {o} \geq d _ {s} \end{array} \right. \\ r = \operatorname {c l i p} \left(\eta_ {r} \cdot r _ {e} - \eta_ {p} \cdot p _ {p} - \eta_ {o} \cdot p _ {o}, - 1, 1\right) \end{array} \right. \tag {1}
$$

The term $d _ { g }$ represents the distance from the starting point to the target, while $d _ { t }$ and $d _ { t - 1 }$ refer to the drone’s current and previous distances from the target, respectively. The variables z and $z _ { g }$ represent the current and target coordinates of the drone along the z-axis, respectively, and $d _ { l }$ denotes the distance between the drone’s current position and the straight line connecting the starting point and the target. The function clip is a limiting function. $d _ { o }$ represents the drone’s closest distance to the surface of an obstacle, calculated from depth images when privileged learning is not applied. However, when privileged learning is applied, it is determined using the global obstacle map and the UAV’s current position, ensuring greater accuracy. $d _ { c }$ is the collision distance, and a collision is considered to occur if $d _ { o }$ is less than $d _ { c } , d _ { s }$ is the safety distance, and the drone is considered at risk of collision if $d _ { o }$ is smaller than $d _ { s } . \ \eta _ { r } , \eta _ { p } ,$ , and $\eta _ { o }$ are the scaling factors for the reward and the two penalty terms, respectively.

The design of this continuous reward function encourages the drone to navigate towards the target through positive reward terms, while the distance error penalty ensures that the drone follows the shortest straight-line path and improves the accuracy of final navigation. The collision proximity penalty helps prevent the drone from getting too close to obstacles, which is particularly important in dense obstacle environments. Normalizing the continuous reward can help avoid large biases and, at the same time, highlight the weight of the sparse reward, making it more effective in providing global guidance and balancing exploration with exploitation.

# 3.2.2 Policy Learning with Privileged Information

Privileged Learning[36] is a machine learning paradigm inspired by a common phenomenon in human learning: when learning new tasks, humans often benefit from additional information such as explanations, books, or demonstrations—resources that may not always be available during actual task execution. In machine learning, this additional information is known as "privileged information." Privileged Learning is often implemented using the Learning Using Privileged Information (LUPI) framework, where extra information is used during training to guide the model’s learning, resulting in improved performance even when this information is not available at test time.

In our work, to address the issue of inaccurate perception caused by partial observability, we provide the policy model with the following two types of privileged information during the training process:

1. Accurate Perception Information: This includes providing the agent with unnoised depth images, localization information, and self-state perception data.   
2. Obstacle Map: This means providing the agent with prior knowledge of the global positions of obstacles. Using this map information, the agent can calculate the UAV’s current closest distance to the obstacle surface to determine the collision proximity penalty in the reward function, thereby enabling more accurate obstacle avoidance guidance.

We constructed an asymmetric Actor-Critic network structure, where the Critic Network receives accurate state information and the Actor Network receives partially observable information, as shown in Figure 1. This approach allows the agent to gain accurate perception of the environment during training, leading to more precise value estimation of the action-state pairs. As a result, this helps accelerate model convergence and improves the success rate.

![](images/6d5157b4c25767a7193ab27ba1a1e508e4217e396e4d66d52afee23376f8bd82.jpg)  
(a)

![](images/211f7361bdff97c6797568568de017874db6b98258bcdedc94c1dacc228ff385.jpg)  
(b)

![](images/21d20e497c8943953adcd6ee562144fe9c0804f6e2f51f08f7ddcf707c8aa255.jpg)

![](images/f3645f9b1fa024618103d9e821af63c475ee3c3374800e1b8e7ad9a02db90659.jpg)  
(d)   
Figure 2: The effect of adding noise to visual perception data. (a) Depth image obtained from the camera in the simulation environment. (b) Salt-and-pepper noise added to the depth image. (c) Gaussian noise added to image (b). (d) Motion blur applied to image (c).

In the simulation environment, we simulate the partially observable phenomena commonly encountered in the real world using different types of noise. Specifically, Gaussian noise with a mean of $\mu _ { s }$ and a standard deviation of $\sigma _ { s }$ is added to each dimension of localization and other self-state information, simulating sensor inaccuracies or estimation errors from VIO algorithms. To ensure stability, the noise is clipped to limit excessive interference. Additionally, noise is sequentially applied to depth image perception data in the specified order below, and the impact of progressively adding these three types of noise is illustrated in Figure 2.

1. Salt-and-Pepper Noise: First, we introduce salt-and-pepper noise with a probability $p _ { s p } ,$ randomly selecting pixels and setting them to extreme values (either 0 or 255). This simulates sudden sensor errors, such as those caused by abrupt lighting changes, strong reflections, or signal loss, where certain pixels become overly bright or dark.   
2. Gaussian Noise: After adding salt-and-pepper noise, we apply Gaussian noise with a mean $\mu _ { g }$ and a standard deviation $\sigma _ { g } .$ , representing overall sensor error. This introduces random measurement deviations across the entire image. The Gaussian noise blends with the saltand-pepper noise, softening some of the extreme values and simulating a more realistic scenario where multiple types of noise coexist.   
3. Motion Blur: Lastly, we apply motion blur using a convolution operation with a kernel size $k _ { m b } .$ . This simulates the blurring effect caused by either camera or object movement. The blur is applied after the other noises to simulate how, in real-world scenarios, noise caused by sudden disturbances would be further exacerbated by motion blur due to the UAV’s high-speed movement or onboard camera jitter.

![](images/65dece7d0b7a14e4755380ab2d53c96c2e271339b6d64c335bcda9b151d77c73.jpg)  
Figure 3: TD3 Framework within the POMDP Model.

To ensure fast and stable model convergence, we perform network parameter updates based on the Twin Delayed Deep Deterministic Policy Gradient (TD3) algorithm[33], which is an advanced version of the Deep Deterministic Policy Gradient (DDPG) algorithm[32], specifically designed to address the instability issues inherent in DDPG. TD3 enhances the robustness of learning by implementing three significant improvements over DDPG, In the context of POMDPs, which include:

1. Clipped Double Q-learning: TD3 consists of six networks: the Actor Network with parameters θ, the Target Actor Network with parameter $\theta ^ { - }$ , two Critic Networks with patameters ω, and their corresponding Target Critic Networks with parameters $\omega ^ { - }$ , as shown in Figure 3. At each step, $a _ { i } ^ { \theta }$ represents the action selected by the Actor Network based on the current observation $o _ { i } ,$ while $a _ { i + 1 } ^ { \theta ^ { - } }$ is the action chosen by the Target Actor Network based on the next observation $o _ { i + 1 }$ . The accurate states corresponding to these observations, $s _ { i }$ and $s _ { i + 1 }$ , align with $o _ { i }$ and $o _ { i + 1 }$ at their respective time steps. To address the overestimation bias present in DDPG, TD3 utilizes the two Critic Networks $Q ( s _ { i } , a _ { i } ^ { \theta } ; \omega _ { 1 } )$ and $Q ( s _ { i } , a _ { i } ^ { \theta } ; \omega _ { 2 } )$ to estimate the expected reward for a given state-action pair $( s _ { i } , a _ { i } )$ . When calculating the TD target, the minimum value between the two Q-functions from the Target Critic Networks $Q ( s _ { i + 1 } , a _ { i + 1 } ^ { \theta ^ { - } } ; \omega _ { 1 } ^ { - } )$ and $Q ( s _ { i + 1 } , a _ { i + 1 } ^ { \theta ^ { - } } ; \omega _ { 2 } ^ { - } )$ is selected to avoid overestimation. The Critic Network loss function is given by:

$$
L (\omega) = \mathbb {E} \left[ \frac {1}{2} \left(R + \gamma \min  _ {j = 1, 2} Q \left(s _ {i + 1}, a _ {i + 1} ^ {\theta -}; \omega_ {j} ^ {-}\right) - Q \left(s _ {i}, a _ {i} ^ {\theta}; \omega\right)\right) ^ {2} \right] \tag {2}
$$

Here, R is the reward for the current step, γ is the discount factor, $\mathbb { E } [ \cdot ]$ denotes the expected TD error over a batch of replay data.

2. Delayed Policy Updates: TD3 employs a delayed update strategy for the Actor (Policy) Network. Unlike DDPG, where the policy and value networks are updated simultaneously, TD3 updates the Actor Network less frequently. This delay ensures that the Critic Network has had sufficient time to learn a more accurate Q-function before the policy is updated, preventing the Actor from being optimized using noisy or unstable value estimates. The policy loss function for the Actor Network is:

$$
L (\theta) = - \frac {1}{N} \sum \left(\min  _ {j = 1, 2} Q \left(s, a ^ {\theta}; \omega_ {j}\right)\right) \tag {3}
$$

Here, N is the batch size of replay data. This loss function maximizes the expected Q-value by selecting actions that result in higher rewards as predicted by the Critic Networks.

3. Target Policy Smoothing: When calculating the TD target, noise is added to the output of the Target Actor Network π $\left( o _ { i + 1 } ; \theta ^ { - } \right)$ to smooth the Q-values and prevent the policy from overfitting to sharp changes in the Q-function. The action from the Target Actor Network is

perturbed by adding clipped noise ε, ensuring smoother policy updates:

$$
a _ {i + 1} ^ {\prime} = \pi \left(o _ {i + 1}; \theta^ {-}\right) + \varepsilon \tag {4}
$$

$$
\varepsilon = \operatorname {c l i p} (\mathcal {N} (0, \sigma), - c, c)
$$

Here, ε is sampled from a normal distribution $\mathcal { N } ( 0 , \sigma )$ and clipped to the range $[ - c , c ]$ .

![](images/86a59b629fc4983a1711093cdee711b538ae56ece1dd489a0adbc196bdb4bd4d.jpg)  
DRL Policy

![](images/634bef5f8e49c345f0e8363dbb4b3c67b26d0b268f104a6a431a424f7fb973fe.jpg)  
Figure 4: Architecture of Actor and Critic Network.

# 3.2.3 Neural Network Architecture

In our work, the network architecture is shown in Figure 4. The state input utilizes multimodal information including visual perception information and UAV self-state variables. Specifically, the visual perception information is a depth image captured at a resolution of $2 4 0 \times 3 2 0$ and resized to $8 0 \times 1 0 0$ for storage and processing, followed by a feature extraction network that extracts features from the depth image and performs dimensionality reduction. The visual perception data $D \in \mathbb { R } ^ { 8 0 \times 1 0 0 }$ is compressed into $S _ { 1 } ^ { \mathbf { i } } \in \mathbb { R } ^ { 2 5 }$ , which forms part of the overall system state. Another part is the 8-dimensional UAV self-state information vector $S _ { 2 } \in \mathbb { R } ^ { 8 }$ consisting of the three-axis distances to the target point $[ d _ { x } , d _ { y } , d _ { z } ] \in \mathbb { R } ^ { 3 }$ , three-axis velocities $[ v _ { x } , v _ { y } , v _ { z } ] \in \mathbf { \bar { R } } ^ { 3 }$ , the yaw angle deviation between the flight direction and the target direction $\Delta \psi \in \mathbb { R } ^ { 1 }$ , and the current yaw angular velocity $\dot { \psi } \in \mathbb { R } ^ { 1 }$ . From the above, the overall state vector is $S = [ S _ { 1 } , S _ { 2 } ] \in \mathbb { R } ^ { 3 3 }$ .

It is worth noting that we use depth images as the visual perception data instead of RGB images. This decision is based on the fact that RGB images obtained in simulation environments often differ in color and texture from those in real-world settings. As a result, feature extraction networks trained in simulations may struggle to effectively extract features from real-world RGB images. In contrast, depth images provide only contour and distance information of obstacles within the field of view, which remains largely consistent between simulation and real environments. This consistency facilitates a smoother transition from simulation to reality and aids in obstacle avoidance through depth information.

Table 1: Network Architecture   

<table><tr><td>Operator</td><td>Input</td><td>Filters</td><td>Output</td></tr><tr><td>Conv2D</td><td>1 × 80 × 100</td><td>3 × 3, 8, stride 1</td><td>8 × 80 × 100</td></tr><tr><td>Max Pooling</td><td>8 × 80 × 100</td><td>2 × 2, stride 2</td><td>8 × 40 × 50</td></tr><tr><td>Conv2D</td><td>8 × 40 × 50</td><td>3 × 3, 16, stride 1</td><td>16 × 40 × 50</td></tr><tr><td>Max Pooling</td><td>16 × 40 × 50</td><td>2 × 2, stride 2</td><td>16 × 20 × 25</td></tr><tr><td>Conv2D</td><td>16 × 20 × 25</td><td>3 × 3, 25, stride 1</td><td>25 × 20 × 25</td></tr><tr><td>Max Pooling</td><td>25 × 20 × 25</td><td>2 × 2, stride 2</td><td>25 × 10 × 12</td></tr><tr><td>Global Avg Pooling</td><td>25 × 10 × 12</td><td>10 × 12</td><td>25 × 1 × 1</td></tr><tr><td>Squeeze</td><td>25 × 1 × 1</td><td>-</td><td>25</td></tr><tr><td>State Feature</td><td>-</td><td>-</td><td>8</td></tr><tr><td>Concatenate</td><td>-</td><td>-</td><td>33</td></tr><tr><td>Fully Connected</td><td>33</td><td>128</td><td>128</td></tr><tr><td>Fully Connected</td><td>128</td><td>128</td><td>128</td></tr><tr><td>Fully Connected</td><td>128</td><td>4</td><td>4</td></tr></table>

On the other hand, the design of the 8-dimensional self-state vector aligns well with the data available from sensors in real-world flight scenarios. For instance, the three-axis position differences and three-axis velocity can be obtained via RTK modules or visual-inertial odometry (VIO) algorithms, while the yaw angle error and yaw rate can be measured using the IMU. Therefore, this state vector design is highly suitable for transitioning from simulation to real-world applications, ensuring both practicality and sufficiency for navigation and obstacle avoidance tasks without introducing unnecessary complexity.

As shown in Figure 4 and Table 1, the policy network consists of two parts: a feature extraction network and a decision network. The feature extraction network is composed of CNN blocks that utilize CNN layers, BatchNorm and MaxPool, effectively extracting features from depth images, with ReLU serving as the activation function. The decision network is a two-layer MLP with 128 neurons per layer, which maps the state feature vectors to actions. Leaky ReLU is employed as the activation function to prevent issues with gradient vanishing that can occur with tanh activation in the TD3 algorithm, which may cause the Actor Network to continuously output boundary values.

The output of the network is a flight control command that belongs to the action space $A \in \mathbb { R } ^ { 4 }$ , which consists of control commands for velocity $[ v _ { x } , v _ { y } , v _ { z } ] \in \mathbb { R } ^ { 3 }$ and yaw rate $\dot { \psi } \in \mathbb { R } ^ { 1 }$ . These continuous actions are used to directly control the UAV’s motion, including adjusting speed and yaw rate.

This continuous action space design facilitates seamless integration with downstream low-level controllers, such as the differential flatness controller which could calculate the throttle and angular velocity control commands based on the velocity and yaw angle control commands[35], providing a practical way to implement control commands in real UAV systems.

# 3.3 Multi-agent Exploration Strategy

In this section, we outline the process of multi-agent experience collection. To improve the efficiency of experience gathering and accelerate model convergence, we implement an asynchronous collection strategy. In this setup, multiple environments run in parallel, each with a single UAV interacting with its respective environment, as shown in Figure 1. These UAVs operate independently, gathering experience through interaction with their respective environments.

By leveraging multiprocessing, we can simultaneously control several UAVs, significantly increasing the rate of experience collection. This enables us to train the model more rapidly, as a larger dataset is generated in a shorter amount of time, leading to faster convergence.

The collected experiences from all UAVs are aggregated to train a central model. This model, in turn, provides decision outputs for each UAV, ensuring consistent policy updates across all environments. By centralizing the learning process, we enable knowledge sharing among the UAVs, which enhances overall performance and improves the success rate of the model. The pseudocode of our proposed DPRL algorithm is shown in Algorithm 1.

Algorithm 1 DPRL: Distributed Privileged Reinforcement Learning

Initialize: Actor network $\pi _ { \theta } ,$ , Critic networks $\overline { { Q _ { \omega _ { 1 } } , Q _ { \omega _ { 2 } } } }$ , target networks $\overline { { \pi _ { \theta ^ { - } } , Q _ { \omega _ { 1 } ^ { - } } , Q _ { \omega _ { 2 } ^ { - } } } }$ , experience replay buffer D

Hyperparameters: exploration noise $\epsilon ,$ batch size B, discount factor $\gamma ,$ target smoothing coefficient τ , target smoothing noise ξ

1: for each episode do   
2: for each agent i in ith environment do   
3: Initialize state $s _ { i , 0 } ,$ , observation $o _ { i , 0 }$ for Critic network   
4: for each time step t do   
5: Select action $a _ { i , t } = \pi _ { \theta } ( o _ { i , t } ) + \epsilon$ (with exploration noise)   
6: Execute $a _ { i , t } ,$ get next state $s _ { i , t + 1 } ,$ next observation $o _ { i , t + 1 }$ and reward ${ \boldsymbol { r } } _ { i , t }$   
7: Store $\left( { { s _ { i , t } } , { o _ { i , t } } , { a _ { i , t } } , { r _ { i , t } } , { s _ { i , t + 1 } } , { o _ { i , t + 1 } } } \right)$ in D   
8: end for   
9: end for   
10: for each training step do   
11: Sample mini-batch of B experiences $( s , o , a , r , s ^ { \prime } , o ^ { \prime } )$ from D   
12: Compute target action with target policy: $a ^ { \prime } = \pi _ { \theta ^ { - } } ( \stackrel { \prime } { o ^ { \prime } } ) + \xi$ (with noise)   
13: Compute target $\begin{array} { r } { y = r + \gamma \operatorname* { m i n } _ { j = 1 , 2 } Q _ { \omega _ { i } ^ { - } } ( s ^ { \prime } , a ^ { \prime } ) } \end{array}$   
14: Update Critic networks by minimizing loss:

$$
L \left(\omega_ {j}\right) = \frac {1}{B} \sum_ {i = 1} ^ {B} \left(y - Q _ {\omega_ {j}} (s, a)\right) ^ {2}, \quad j = 1, 2
$$

15: if every d steps then   
16: Update Actor network by maximizing $Q _ { \omega _ { 1 } } ( s , \pi _ { \theta } ( o ) )$   
17: Soft update target networks:

$$
\theta^ {-} \leftarrow \tau \theta + (1 - \tau) \theta^ {-}, \quad \omega_ {j} ^ {-} \leftarrow \tau \omega_ {j} + (1 - \tau) \omega_ {j} ^ {-}, \quad j = 1, 2
$$

18: end if   
19: end for   
20: end for

# 4 Experiments and Results

In this section, extensive experiments were conducted to verify our proposed DPRL navigation algorithm’s advantages in terms of efficiency, success rate, and robustness. Our proposed algorithm was compared against TD3 algorithm and EGO-Planner-v2 framework across various environments. Additionally, we performed several ablation studies to validate the novelty of our approach and the rationale behind our choices of state and action spaces.

![](images/0524db38b734775c01a57240859bc529ff9db5af8651e3eb5f491ffce26bcf5c.jpg)

![](images/ba9fe368f2c61902e90e54864c61b20ec39b7e4f5893a24b7d11642d3cf7ebee.jpg)

![](images/d2865b4567919817f7d60003a2d03f328f98f80787253166d5d1e2ca7d419535.jpg)  
  
Figure 5: Simulation environment built using UE4 and AirSim. (a) Top-down view of the training environment. (b) Top-down view of a randomly generated environment. (c) View of the UAV flying within the environment.

# 4.1 Experiments Setup

We created a realistic simulation environment in UE4, using AirSim’s underlying dynamics model for accurate simulation[34]. To emulate a complex obstacle-laden environment, we generated the scene shown in Figure 5(a) for model training. This environment features 70 cylindrical obstacles with a radius of 2.5 m and a height of 15 m, arranged within a circular area of 60 m radius centered at the origin. The UAV’s flight altitude is limited to a maximum of 15 m, ensuring it must maneuver around obstacles for collision avoidance rather than flying over them, which would expend excessive energy.

Table 2: Simulation Parameter Settings   

<table><tr><td>Category</td><td>Parameter</td><td>Value</td></tr><tr><td rowspan="9">Environment</td><td>x range</td><td>[-85, 85] m</td></tr><tr><td>y range</td><td>[-85, 85] m</td></tr><tr><td>z range</td><td>[0.2, 15] m</td></tr><tr><td>Start position</td><td>[0, 0, 5] m</td></tr><tr><td>Goal distance</td><td>65 m</td></tr><tr><td>Goal height</td><td>5 m</td></tr><tr><td>Safe distance</td><td>4 m</td></tr><tr><td>Crash distance</td><td>1 m</td></tr><tr><td>Accept radius</td><td>2 m</td></tr><tr><td rowspan="5">Dynamics</td><td>Action execution duration</td><td>0.1 s</td></tr><tr><td>x-axis velocity range</td><td>[-3.0, 3.0] m/s</td></tr><tr><td>y-axis velocity range</td><td>[-3.0, 3.0] m/s</td></tr><tr><td>z-axis velocity range</td><td>[-2.0, 2.0] m/s</td></tr><tr><td>yaw velocity range</td><td>[-0.3, 0.3] rad/s</td></tr><tr><td rowspan="11">Training</td><td>Discount factor γ</td><td>0.99</td></tr><tr><td>Learning rate α</td><td>3e-4</td></tr><tr><td>Learning start</td><td>2000</td></tr><tr><td>Buffer size</td><td>50000</td></tr><tr><td>Batch size</td><td>128</td></tr><tr><td>Train frequency</td><td>1</td></tr><tr><td>Standard deviation of action noise</td><td>0.1</td></tr><tr><td>σa</td><td></td></tr><tr><td>Number of environments</td><td>3</td></tr><tr><td>Total timesteps</td><td>330000</td></tr><tr><td>Max episode steps</td><td>500</td></tr><tr><td rowspan="3">Reward</td><td>ηr</td><td>5.0</td></tr><tr><td>ηp</td><td>0.5</td></tr><tr><td>ηo</td><td>1.0</td></tr><tr><td rowspan="5">Noise</td><td>μg</td><td>0</td></tr><tr><td>σg</td><td>3</td></tr><tr><td>sp</td><td>0.005</td></tr><tr><td>μs</td><td>0</td></tr><tr><td>σs</td><td>0.016</td></tr></table>

Each training episode begins with the UAV taking off from the origin at an initial altitude of 5 meters, aiming for a target position randomly placed along a circumference with a radius of 65 meters. An episode is considered successful when the UAV reaches within 2 m of the target. Conversely, if the UAV comes within 1 m of an obstacle or exits the defined flight area, the episode is marked as a failure.

For each action, an execution duration of 0.1 s is set, ensuring smooth command continuity while avoiding excessive computational load on the simulation, thereby maintaining optimal training frame rates. The specific environmental configurations and dynamics model parameters are outlined in Table 2.

In our training process, we created three separate environments based on three different seeds to train the model and used an additional environment for model evaluation. UAVs in each environment collected experience independently, controlled by different processes. Training was conducted on a workstation equipped with an Intel i7-13700KF CPU and an NVIDIA 4070 Ti GPU, achieving an average model update frame rate of 20 frames per second. The specific parameters for training, reward function, and noise settings are provided in Table 2.

To evaluate the model, we used three metrics: Average Episode Reward (AER), Average Steps of Successful Episodes (ASSE), and Success Rate (SR). AER assesses the overall performance of the algorithm, including navigation accuracy, obstacle avoidance safety, and efficiency. A higher AER reflects better overall performance. ASSE measures the efficiency of the algorithm, where a smaller ASSE value indicates that the UAV completes tasks with fewer steps, demonstrating greater efficiency. SR evaluates the success rate of the algorithm, with a higher SR signifying enhanced safety and practicality.

# 4.2 Comparison Experiment

To validate the comprehensive performance of our UAV autonomous navigation framework, we conducted a comparative analysis of the proposed DPRL algorithm, TD3 algorithm, and EGO-Planner-v2 framework. For DPRL and TD3, we provided noisy visual perception, localization, and other self-state information. In contrast, EGO-Planner received LiDAR point cloud data along with noisy odometry information, with the noise characterized by a mean of 0 and a standard deviation of 0.016. This setup introduced controlled disturbances in the mapping process to simulate realworld conditions. The maximum speed for EGO-Planner was set to be consistent with the RL-based methods, capped at 3 m/s. A PD controller was used for EGO-Planner, which outputs flight commands for velocity and yaw angle. The specific experiments are detailed below.

![](images/752fd884c664d1c4f20314898ccf7d413d0b8c98d8d52e7703c57c7111511c17.jpg)  
(a)

![](images/2d0ca2fb7d415d11407643ca83353f9b6b5e335c2271a47695bcc0f043ebcda0.jpg)  
(d)   
Figure 6: The training curves of different UAV navigation algorithms. (a) Average success rate curve of Proposed DPRL and TD3. (b) Average episode reward curve of Proposed DPRL and TD3.

Figure 6(a) and (b) present the comparative training curves between DPRL and TD3 under four different seeds. As illustrated in Figure 6(a), DPRL demonstrates a notably faster convergence rate compared to TD3, reaching an average success rate exceeding 85% after just 220,000 training steps. The average episode reward curves during training, shown in Figure 6(b), align closely with the trends observed in the average success rate curves. DPRL exhibits rapid reward growth during the early and mid-stages of training, stabilizing at a high reward value after 240,000 steps. In contrast, TD3 shows consistently slower reward growth and fails to converge by the end of training.

We deployed the trained models of DPRL, TD3, and EGO-Planner-v2 in both the training and randomly generated environments(Figure 5(b)), plotting the flight trajectories over 30 episodes with unique target positions, as shown in Figure 7. It can be observed that DPRL maintains a high success rate in both the training and random environments. Although the success rate decreases somewhat in unfamiliar environments compared to the training environment, the model still demonstrates robustness against noise interference, underscoring its adaptability to new environments.

In contrast, TD3 exhibits the lowest success rate, performing poorly in both environments, with less smooth trajectories compared to DPRL. For EGO-Planner, both environments are unfamiliar, with

![](images/a63439f15e800263a7ca153efa3017d292cce296ae1dfa3e1e400e591e96bd47.jpg)  
(a)

![](images/c70fe18575fdffb4d4df6c6b44cbe2da73e58ee930d10a5530da2028d84cdb8e.jpg)  
(b)

![](images/6941c3d0fb631014e0604d128464eddb6725651e18c24135e11aa7f1f9c9b82e.jpg)  
(c)

![](images/925143d74eb749a9afae96bae7c1664b9ae59bfe361cf10052fdd4ec0f128fbe.jpg)  
(d)

![](images/a616625470d7db201dbbe75d594f1935b682cdee97499efdf7d88295697cdd84.jpg)  
(e)

![](images/18b49782192dd177be384e7e891c97f910a196cec189976e95cbacb5402334c9.jpg)  
(f)   
Figure 7: Comparison results of navigation and obstacle avoidance trajectories. Each figure represents the evaluation results of 30 episodes, where blue trajectories indicate successful completions, and red trajectories represent failures due to collisions. (a) Flight trajectories of DPRL in training environment. (b) Flight trajectories of TD3 in training environment. (c) Flight trajectories of EGO-Planner-v2 in training environment. (d) Flight trajectories of DPRL in random environment. (e) Flight trajectories of TD3 in random environment. (f) Flight trajectories of EGO-Planner-v2 in random environment.

the training environment containing a higher density of obstacles. Consequently, EGO-Planner’s performance is weaker in the training environment than in the random environment. EGO-Planner produces the smoothest trajectories and reaches target points with the highest accuracy, but its planning speed is the slowest among the three algorithms.

Table 3: Performance Comparison in Training and Random Environments   

<table><tr><td rowspan="2">Environment</td><td rowspan="2">Algorithm</td><td colspan="3">Metric</td></tr><tr><td>AER</td><td>ASSE</td><td>SR</td></tr><tr><td rowspan="3">Training Env</td><td>DPRL</td><td>33.685</td><td>191.0</td><td>86.667%</td></tr><tr><td>TD3</td><td>16.205</td><td>202.0</td><td>33.333%</td></tr><tr><td>EGO-Planner-v2</td><td>22.746</td><td>399.625</td><td>83.333%</td></tr><tr><td rowspan="3">Random Env</td><td>DPRL</td><td>31.617</td><td>190.391</td><td>76.667%</td></tr><tr><td>TD3</td><td>17.033</td><td>196.875</td><td>26.667%</td></tr><tr><td>EGO-Planner-v2</td><td>24.527</td><td>374.0</td><td>90.0%</td></tr></table>

Table 3 summarizes the average episode reward, average steps of successful episodes, and success rate of each algorithm. While DRPL achieves a success rate comparable to EGO-Planner, it attains higher rewards and shorter episode lengths, demonstrating superior obstacle-avoidance efficiency and best overall performance among the three methods.

![](images/1f6afb04484ba75f99dace3cc98a760cf3910dd2dd08ec316a87e64b5e8f7987.jpg)  
(a)

![](images/204784881113c7cf83dfa4e3095d3d6ea9c0191bdca73865a47ddcf159a39dd5.jpg)  
(b)   
Figure 8: Ablation experiment results for key components in DPRL during model training. (a) Average success rate curve of Proposed DPRL, Privileged RL and Distributed RL. (b) Average episode reward curve of Proposed DPRL, Privileged RL and Distributed RL.

# 4.3 Ablation Experiment

We first conducted ablation studies on the privileged learning and multi-agent exploration components of the proposed DPRL algorithm to validate their effects. The detailed experimental results are shown in Figures 8(a) and (b). In these studies, Privileged RL and Distributed RL were derived from DPRL by removing multi-agent exploration and privileged learning, respectively.

As shown in Figures 8(a), DPRL demonstrates superior convergence speed and a higher final average success rate during training compared to both Privileged RL and Distributed RL. Specifically, DPRL’s success rate stabilizes after 220,000 steps, while both Privileged RL and Distributed RL only converge after 300,000 steps. The average episode reward curves, shown in Figures 8(b), align closely with the average success rate trends. DPRL’s rewards stabilize above 30 after 240,000 steps, whereas Privileged RL requires over 300,000 steps to achieve similar rewards. In contrast, Distributed RL fails to exceed a reward of 30 even by the end of training.

Notably, the impact of privileged learning is greater than that of multi-agent exploration. Although Distributed RL shows slightly better convergence than Privileged RL at the beginning of training, Privileged RL begins to outperform after 200,000 training steps, ultimately achieving a higher average success rate and average episode reward. This highlights the significant advantage of privileged learning in handling partial observability in the environment and the effectiveness of multi-agent exploration in accelerating early convergence.

To compare the impact of different state and action space designs on the model, we then conducted the following experiment. We established an alternative state and action space similar to that used by He et al.[37], with modifications to the self-state vector’s positioning and velocity information. Specifically, the state now includes the distance to the target in the xy-plane, the z-axis distance, the velocity in the xy-plane, and the z-axis velocity. This adjustment reduces the total dimensionality of the state vector from 33 to 31. Correspondingly, the action space was reduced from 4 dimensions to 3. The original x and y velocity components were replaced by a single xy-plane velocity, which is split into x and y components based on the current yaw angle during execution. This setup ensures that the UAV always flies in the direction it is facing, keeping obstacles in its forward field of view. However, this also significantly compresses the UAV’s action space, reducing maneuverability.

The actual training and evaluation results are shown in Figures 9. It is evident that our proposed 4-dimensional action space, along with its corresponding state space, significantly outperforms the 3-dimensional action space and its associated state space. During training, the DPRL model with the 3-dimensional action space exhibited almost no successful flight episodes in the early stages and demonstrated very slow learning progress. By the end of training, it achieved only an average success rate of about 30%, performing even worse than TD3 with the 4-dimensional action space. This poor performance is further reflected in the average episode reward results. The DPRL model with the 3-dimensional action space showed minimal improvement in rewards throughout training and only reached an average reward of 10 by the end, highlighting the substantial negative impact of action space compression on the model’s ability to learn obstacle-avoidance navigation. These findings confirm the rationality and effectiveness of our proposed state and action space design.

![](images/82f38459cdecca445fa2a5bf8ed9c889050b9dfee0143acae218957d5a907ae3.jpg)  
(a)

![](images/f4acd65836f6033edf6b509bcc6f12f295409b7e5e88400b6f5a57f85797a4cf.jpg)  
(b)   
Figure 9: Ablation experiment results for state and action space design in DPRL during model training. (a) Average success rate curve of DPRL with 3D and 4D action space. (b) Average episode reward curve of DPRL with 3D and 4D action space.

# 5 Conclusions

In our work, we propose the DPRL algorithm for UAV autonomous navigation and obstacle avoidance in complex, unknown environments. Specifically, we implement privileged learning using an asymmetric Actor-Critic network structure to address perception and localization noise encountered in flight environments. Additionally, we utilize asynchronous multi-agent exploration across multiple environments to improve data efficiency and accelerate model convergence.

Experiments conducted in the AirSim simulation environment demonstrate the DPRL algorithm’s comprehensive optimal performance in terms of convergence speed, final flight success rate, robustness to environmental variations, and planning efficiency. The results also validate the effectiveness of our novelty and the designed state and action space. Moreover, our algorithm shows strong potential for transfer to real-world applications and is compatible with all off-policy deep reinforcement learning algorithms, ensuring broad generalizability.

In future work, we will further enhance the navigation and obstacle avoidance success rate of the DPRL algorithm across various complex environments and conduct outdoor flight experiments to validate the proposed algorithm more comprehensively.

# References

[1] Kalidas, A.P.; Joshua, C.J.; Md, A.Q.; Basheer, S.; Mohan, S.; Sakri, S. Deep reinforcement learning for vision-based navigation of UAVs in avoiding stationary and mobile obstacles. Drones 2023, 7, 245. MDPI. DOI: https://doi.org/10.3390/drones7040245.   
[2] Lyu, M.; Zhao, Y.; Huang, C.; Huang, H. Unmanned Aerial Vehicles for Search and Rescue: A Survey. Remote Sensing 2023, 15, 3266. DOI: https://doi.org/10.3390/rs15133266.   
[3] Su, J.; Zhu, X.; Li, S.; Chen, W.-H. AI meets UAVs: A survey on AI empowered UAV perception systems for precision agriculture. Neurocomputing 2023, 518, 242–270. DOI: https://doi.org/10.1016/j.neucom.2022.11.020.   
[4] Diao, Q.; Zhang, J.; Liu, M.; Yang, J. A Disaster Relief UAV Path Planning Based on APF-IRRT* Fusion Algorithm. Drones 2023, 7, 323. DOI: https://doi.org/10.3390/ drones7050323.   
[5] Li, X.; Tupayachi, J.; Sharmin, A.; Martinez Ferguson, M. Drone-Aided Delivery Methods, Challenge, and the Future: A Methodological Review. Drones 2023, 7, 191. DOI: https: //doi.org/10.3390/drones7030191.   
[6] Zhou, X.; Wen, X.; Wang, Z.; Gao, Y.; Li, H.; Wang, Q.; Yang, T.; Lu, H.; Cao, Y.; Xu, C.; et al. Swarm of micro flying robots in the wild. Science Robotics 2022, 7, eabm5954. American Association for the Advancement of Science. DOI: https://doi.org/10.1126/ scirobotics.abm5954

[7] Tong, G.; Jiang, N.; Li, B.; Zhu, X.; Wang, Y.; Du, W. UAV navigation in high dynamic environments: A deep reinforcement learning approach. Chinese Journal of Aeronautics 2021, 34, 479–489. Elsevier. DOI: https://doi.org/10.1016/j.cja.2020.05.011   
[8] Loquercio, A.; Kaufmann, E.; Ranftl, R.; Müller, M.; Koltun, V.; Scaramuzza, D. Learning high-speed flight in the wild. Science Robotics 2021, 6, eabg5810. American Association for the Advancement of Science. DOI: https://doi.org/10.1126/scirobotics.abg5810   
[9] Arafat, M.Y.; Alam, M.M.; Moh, S. Vision-based navigation techniques for unmanned aerial vehicles: Review and challenges. Drones 2023, 7, 89. MDPI. DOI: https://doi.org/10. 3390/drones7020089   
[10] Fei, W.; Xiaoping, Z.; Zhou, Z.; Tang, Y. Deep-reinforcement-learning-based UAV autonomous navigation and collision avoidance in unknown environments. Chinese Journal of Aeronautics 2024, 37, 237–257. Elsevier. DOI: https://doi.org/10.1016/j.cja.2023.09.033   
[11] Yin, Y.; Wang, Z.; Zheng, L.; Su, Q.; Guo, Y. Autonomous UAV navigation with adaptive control based on deep reinforcement learning. Electronics 2024, 13, 2432. MDPI. DOI: https://doi.org/10.3390/electronics13132432   
[12] Srivastava, A.; Prakash, J. Edge enhancement by noise suppression in HSI color model of UAV video with adaptive thresholding. Wireless Personal Communications 2022, 124, 163–186. Springer. DOI: https://doi.org/10.1007/s11277-021-09461-5   
[13] Joshi, B.; Kapur, D.; Kandath, H. Sim-to-real deep reinforcement learning based obstacle avoidance for UAVs under measurement uncertainty. In Proceedings of the 2024 10th International Conference on Automation, Robotics and Applications (ICARA); IEEE, 2024; pp. 278–284. DOI: 10.1109/ICARA60736.2024.10553074   
[14] Lu, J.; Tian, B.; Shen, H.; Zhang, X.; Hui, Y. LPNet: A reaction-based local planner for autonomous collision avoidance using imitation learning. IEEE Robotics and Automation Letters 2023. IEEE. DOI: 10.1109/LRA.2023.3314350   
[15] Sumikura, S.; Shibuya, M.; Sakurada, K. OpenVSLAM: A Versatile Visual SLAM Framework. In Proceedings of the 27th ACM International Conference on Multimedia, Nice, France, 21–25 October 2019; pp. 2292–2295. DOI: https://doi.org/10.1145/3343031.3350539.   
[16] Teed, Z.; Deng, J. DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras. Adv. Neural Inf. Process. Syst. 2021, 34, 16558–16569. DOI: https://doi.org/ 10.5555/3540261.3541527.   
[17] Sarlin, P.-E.; DeTone, D.; Malisiewicz, T.; Rabinovich, A. SuperGlue: Learning Feature Matching with Graph Neural Networks. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, Seattle, WA, USA, 14–19 June 2020; pp. 4938– 4947. DOI: https://doi.org/10.1109/CVPR42600.2020.00499.   
[18] Li, J.; Liao, C.; Zhang, W.; Fu, H.; Fu, S. UAV Path Planning Model Based on R5DOS Model Improved A-Star Algorithm. Appl. Sci. 2022, 12, 11338. DOI: https://doi.org/10.3390/ app122211338.   
[19] Guo, Y.; Liu, X.; Liu, X.; Yang, Y.; Zhang, W. FC-RRT*: An Improved Path Planning Algorithm for UAV in 3D Complex Environment. ISPRS Int. J. Geo-Inf. 2022, 11, 112. DOI: https://doi.org/10.3390/ijgi11020112.   
[20] Zhao, Y.; Liu, K.; Lu, G.; Hu, Y.; Yuan, S. Path Planning of UAV Delivery Based on Improved APF-RRT* Algorithm. In Proceedings of the Journal of Physics: Conference Series, Online, 20 November 2020; Volume 1624, p. 042004. DOI: https://doi.org/10.1088/1742-6596/ 1624/4/042004.   
[21] Ait-Saadi, A.; Meraihi, Y.; Soukane, A.; Ramdane-Cherif, A.; Gabis, A.B. A Novel Hybrid Chaotic Aquila Optimization Algorithm with Simulated Annealing for Unmanned Aerial Vehicles Path Planning. Comput. Electr. Eng. 2022, 104, 108461. DOI: https://doi.org/ 10.1016/j.compeleceng.2022.108461.   
[22] Huang, Q.; Sheng, Z.; Fang, Y.; Li, J. A Simulated Annealing-Particle Swarm Optimization Algorithm for UAV Multi-Target Path Planning. In Proceedings of the 2022 2nd International Conference on Consumer Electronics and Computer Engineering (ICCECE), Guangzhou, China, 14–16 January 2022; pp. 906–910. DOI: https://doi.org/10.1109/ICCECE54139.2022. 9730600.

[23] Lindqvist, B.; Mansouri, S.S.; Agha-mohammadi, A.; Nikolakopoulos, G. Nonlinear MPC for Collision Avoidance and Control of UAVs with Dynamic Obstacles. IEEE Robot. Autom. Lett. 2020, 5, 6001–6008. DOI: https://doi.org/10.1109/LRA.2020.3010077.   
[24] Mohammadi, A.; Ramezani, A. A Robust Model Predictive Control-Based Method for Fault Detection and Fault Tolerant Control of Quadrotor UAV. Trans. Inst. Meas. Control 2023, 45, 37–48. DOI: https://doi.org/10.1177/01423312221114071.   
[25] Li, Y.; Li, H.; Li, Z.; Fang, H.; Sanyal, A.K.; Wang, Y.; Qiu, Q. Fast and Accurate Trajectory Tracking for Unmanned Aerial Vehicles Based on Deep Reinforcement Learning. In Proceedings of the 2019 IEEE 25th International Conference on Embedded and Real-Time Computing Systems and Applications (RTCSA), Hangzhou, China, 18–21 August 2019; pp. 1–9. DOI: https://doi.org/10.1109/RTCSA.2019.8864571.   
[26] Wang, L.; Wang, K.; Pan, C.; Xu, W.; Aslam, N.; Nallanathan, A. Deep Reinforcement Learning Based Dynamic Trajectory Control for UAV-Assisted Mobile Edge Computing. IEEE Trans. Mob. Comput. 2022, 21, 3536–3550. DOI: https://doi.org/10.1109/TMC.2021. 3059691.   
[27] Loquercio, A.; Maqueda, A.I.; Del-Blanco, C.R.; Scaramuzza, D. Dronet: Learning to fly by driving. IEEE Robotics and Automation Letters 2018, 3, 1088–1095. IEEE. DOI: https://doi.org/10.1109/LRA.2018.2795643.   
[28] Gandhi, D.; Pinto, L.; Gupta, A. Learning to fly by crashing. In Proceedings of the 2017 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS); IEEE, 2017; pp. 3948–3955. DOI: https://doi.org/10.1109/IROS.2017.8206247.   
[29] Xie, R.; Meng, Z.; Wang, L.; Li, H.; Wang, K.; Wu, Z. Unmanned aerial vehicle path planning algorithm based on deep reinforcement learning in large-scale and dynamic environments. IEEE Access 2021, 9, 24884–24900. IEEE. DOI: https://doi.org/10.1109/ACCESS. 2021.3057485.   
[30] Lee, M.H.; Moon, J. Deep reinforcement learning-based UAV navigation and control: A soft actor-critic with hindsight experience replay approach. arXiv preprint arXiv:2106.01016, 2021. DOI: https://doi.org/10.48550/arXiv.2106.01016.   
[31] Kaufmann, E.; Bauersfeld, L.; Loquercio, A.; Müller, M.; Koltun, V.; Scaramuzza, D. Champion-level drone racing using deep reinforcement learning. Nature 2023, 620, 982–987. Nature Publishing Group, UK, London. DOI: https://doi.org/10.1038/ s41586-023-06419-4.   
[32] Lillicrap, T.P.; Hunt, J.J.; Pritzel, A.; Heess, N.; Erez, T.; Tassa, Y.; Silver, D.; Wierstra, D. Continuous control with deep reinforcement learning. arXiv preprint arXiv:1509.02971, 2015. DOI: https://doi.org/10.48550/arXiv.1509.02971.   
[33] Fujimoto, S.; van Hoof, H.; Meger, D. Addressing function approximation error in actor-critic methods. In Proceedings of the International Conference on Machine Learning; PMLR, 2018; pp. 1587–1596. DOI: https://doi.org/10.48550/arXiv.1802.09477.   
[34] Shah, S.; Dey, D.; Lovett, C.; Kapoor, A. AirSim: High-fidelity visual and physical simulation for autonomous vehicles. In Proceedings of the Field and Service Robotics: Results of the 11th International Conference; Springer, 2018; pp. 621–635. DOI: https://doi.org/10. 48550/arXiv.1705.05065.   
[35] Faessler, M.; Franchi, A.; Scaramuzza, D. Differential flatness of quadrotor dynamics subject to rotor drag for accurate tracking of high-speed trajectories. IEEE Robotics and Automation Letters 2017, 3, 620–626. IEEE. DOI: https://doi.org/10.1109/LRA.2017.2776353.   
[36] Vapnik, V.; Vashist, A. A new learning paradigm: Learning using privileged information. Neural Networks 2009, 22, 544–557. Elsevier. DOI: https://doi.org/10.1016/j.neunet. 2009.06.042.   
[37] He, L.; Aouf, N.; Whidborne, J.F.; Song, B. Deep reinforcement learning based local planner for UAV obstacle avoidance using demonstration data. arXiv preprint arXiv:2008.02521 2020. DOI: https://doi.org/10.48550/arXiv.2008.02521.   
[38] Niu, C.; Zauner, K.-P.; Tarapore, D. End-to-End Learning for Visual Navigation of Forest Environments. Forests 2023, 14, 268. DOI: https://doi.org/10.3390/f14020268.

[39] Al-Kaff, A.; Martín, D.; García, F.; de la Escalera, A.; Armingol, J.M. Survey of Computer Vision Algorithms and Applications for Unmanned Aerial Vehicles. Expert Syst. Appl. 2018, 92, 447–463. DOI: https://doi.org/10.1016/j.eswa.2017.09.033.   
[40] Song, Y.; Shi, K.; Penicka, R.; Scaramuzza, D. Learning Perception-Aware Agile Flight in Cluttered Environments. Proceedings of the 2023 IEEE International Conference on Robotics and Automation (ICRA), 2023, 1989–1995. DOI: https://doi.org/10.1109/ICRA48891. 2023.10160563.   
[41] Yue, P.; Xin, J.; Zhang, Y.; Lu, Y.; Shan, M. Semantic-Driven Autonomous Visual Navigation for Unmanned Aerial Vehicles. IEEE Transactions on Industrial Electronics, 2024, 71(11), 14853–14863. DOI: https://doi.org/10.1109/TIE.2024.3363761.   
[42] Boiteau, S.; Vanegas, F.; Gonzalez, F. Framework for Autonomous UAV Navigation and Target Detection in Global-Navigation-Satellite-System-Denied and Visually Degraded Environments. Remote Sensing, 2024, 16(3), 471. DOI: https://doi.org/10.3390/rs16030471.   
[43] Al-Kaff, A.; Meng, Q.; Martín, D.; de la Escalera, A.; Armingol, J.M. Monocular Vision-Based Obstacle Detection/Avoidance for Unmanned Aerial Vehicles. Proceedings of the 2016 IEEE Intelligent Vehicles Symposium (IV), 2016, 92–97. DOI: https://doi.org/10.1109/IVS. 2016.7535370.   
[44] Chen, H.-C. Monocular Vision-Based Obstacle Detection and Avoidance for a Multicopter. IEEE Access, 2019, 7, 167869–167883. DOI: https://doi.org/10.1109/ACCESS.2019. 2953954.   
[45] Duan, R.; Paudel, D.P.; Fu, C.; Lu, P. Stereo Orientation Prior for UAV Robust and Accurate Visual Odometry. IEEE/ASME Transactions on Mechatronics, 2022, 27(5), 3440–3450. DOI: https://doi.org/10.1109/TMECH.2022.3140923.   
[46] Teed, Z.; Lipson, L.; Deng, J. Deep Patch Visual Odometry. Advances in Neural Information Processing Systems, 2024, 36. DOI: https://doi.org/10.48550/arXiv.2208.04726   
[47] Zhang, Z.; Zhang, Y.; Cao, Y. Monocular Vision-Based Obstacle Avoidance Trajectory Planning for Unmanned Aerial Vehicles. Proceedings of the 2020 International Conference on Unmanned Aircraft Systems (ICUAS), 2020, 627–632. DOI: https://doi.org/10.1109/ ICUAS48674.2020.9213901.   
[48] Bhattacharya, A.; Rao, N.; Parikh, D.; Kunapuli, P.; Wu, Y.; Tao, Y.; Matni, N.; Kumar, V. Vision Transformers for End-to-End Vision-Based Quadrotor Obstacle Avoidance. arXiv preprint, arXiv:2405.10391, 2024. DOI: https://doi.org/10.48550/arXiv.2405.10391   
[49] Zhou, B.; Gao, F.; Wang, L.; Liu, C.; Shen, S. Robust and Efficient Quadrotor Trajectory Generation for Fast Autonomous Flight. IEEE Robotics and Automation Letters, 2019, 4(4), 3529–3536. DOI: https://doi.org/10.1109/LRA.2019.2927938.   
[50] Zhou, B.; Gao, F.; Pan, J.; Shen, S. Robust Real-time UAV Replanning Using Guided Gradientbased Optimization and Topological Paths. Proceedings of the 2020 IEEE International Conference on Robotics and Automation (ICRA), 2020, 1208–1214. DOI: https://doi. org/10.1109/ICRA40945.2020.9196996.   
[51] Zhou, B.; Pan, J.; Gao, F.; Shen, S. RAPTOR: Robust and Perception-Aware Trajectory Replanning for Quadrotor Fast Flight. IEEE Transactions on Robotics, 2021, 37(6), 1992–2009. DOI: https://doi.org/10.1109/TRO.2021.3071527.   
[52] He, L.; Aouf, N.; Song, B. Explainable Deep Reinforcement Learning for UAV Autonomous Path Planning. Aerospace Science and Technology, 2021, 118, 107052. DOI: https://doi. org/10.1016/j.ast.2021.107052.   
[53] Hu, Z.; Gao, X.; Wan, K.; Wang, Q.; Zhai, Y. Asynchronous Curriculum Experience Replay: A Deep Reinforcement Learning Approach for UAV Autonomous Motion Control in Unknown Dynamic Environments. IEEE Transactions on Vehicular Technology, 2023, 72(11), 13985–14001. DOI: https://doi.org/10.1109/TVT.2023.3285595.   
[54] Zhou, D.; Sun, G.; Lei, W.; Wu, L. Space Noncooperative Object Active Tracking With Deep Reinforcement Learning. IEEE Transactions on Aerospace and Electronic Systems, 2022, 58(6), 4902–4916. DOI: https://doi.org/10.1109/TAES.2022.3211246.   
[55] Zhou, D.; Sun, G.; Zhang, Z.; Wu, L. On Deep Recurrent Reinforcement Learning for Active Visual Tracking of Space Noncooperative Objects. IEEE Robotics and Automation Letters, 2023, 8(8), 4418–4425. DOI: https://doi.org/10.1109/LRA.2023.3282792.