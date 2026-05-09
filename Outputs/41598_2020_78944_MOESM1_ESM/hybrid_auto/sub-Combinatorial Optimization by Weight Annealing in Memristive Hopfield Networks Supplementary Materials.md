---


title: "sub-Combinatorial Optimization by Weight Annealing in Memristive Hopfield Networks"
date: "2020-01-01"
year: 2020
journal: "Scientific Reports"
abstract: "Supplementary materials for the main paper on combinatorial optimization"
abstract_cn: "忆阻器 Hopfield 网络权重退火组合优化主论文的补充材料。包含离散时间 Hopfield 网络与退火技术、优化问题公式化、图划分示例及额外仿真结果详情。"
cite: "待补充. sub-Combinatorial Optimization by Weight Annealing in Memristive Hopfield Networks[J].\
  \ Scientific Reports, 2020."
aiSum: "忆阻器 Hopfield 网络权重退火组合优化论文补充材料：Hopfield 网络与退火技术、优化问题公式、图划分示例及仿真结果。"
confidence: "medium"
parent:
  - "[[sub-Combinatorial Optimization by Weight Annealing in Memristive Hopfield Networks Supplementary Materials (Copy)]]"
authors:
  - "Z. Fahimi"
  - "M. R. Mahmoodi"
  - "H. Nili"
  - "Valentin Polishchuk"
  - "D. B. Strukov"
---

# Combinatorial Optimization by Weight Annealing in Memristive Hopfield Networks Supplementary Materials

Z. Fahimi1*#, M. R. Mahmoodi1*#, H. Nili1 , Valentin Polishchuk2 , D. B. Strukov1

1 UC Santa Barbara, Santa Barbara, CA 93106-9560, U.S.A. 2 Linkoping University, 60174 Norrkoping, Sweden

* Equal Contribution #{z.fahimi,mrmahmoodi}@ucsb.edu

# Overview

Here, we provide supplementary details in support of the main paper. Section 1 briefly discusses the discretetime Hopfield networks and annealing techniques. Section 2 formulates the optimization problems considered in this study. Section 3 expands upon the details of the 7-node graph partitioning problem. Section 4 and 5 are devoted to the additional graph partitioning, vertex cover, maximum clique, and maximum-independent set simulation results. Sections 6 and 7 include the relevant details of experiments performed with the two representative memory technologies. Section 8 and 9 discuss the performance prospects and the experimental setups, respectively.

# 1. Hopfield Neural Networks and Annealing Techniques

The focus of this paper is on discrete-time Hopfield neural networks (HNNs) [1,2]. The following Lyapunov energy function describes the dynamics of the network described by the update rule in Eq. 1 of the main text:

$$
E = \frac {- 1}{2} \sum_ {j = 1} ^ {N} \sum_ {i = 1, \neq j} ^ {N} T _ {i j} U _ {i} (t) U _ {j} (t) - \sum_ {j = 1} ^ {N} T _ {j} ^ {b} U _ {j} (t). \tag {S1}
$$

In the case of symmetric connections $( T _ { i j } = T _ { j i } )$ , zero self-feedback weights $( T _ { i i } = 0 )$ , and single neuron update at a time, the network always converges to a stable equilibrium point due to its gradient decedent dynamics. The change in the state of $\dot { \boldsymbol { \jmath } } ^ { \mathrm { t h } }$ neuron at epoch t+1 results in ∆? given by

$$
\Delta E = - \left(\sum_ {i = 1, \neq j} ^ {N} T _ {i j} U _ {i} (t) + T _ {j} ^ {\mathrm {b}}\right) \Delta U _ {j}. \tag {S2}
$$

Since $\Delta U _ { j }$ and $\begin{array} { r } { \sum _ { i = 1 , \neq j } ^ { N } T _ { i j } U _ { i } ( t ) + T _ { j } ^ { b } } \end{array}$ have similar signs, $\Delta E \le 0$ , and since ? is bounded, the equilibrium is a stable point. The search space is the interior of the N-dimensional hypercube, with minima located in the corners of it [3,4]. The most critical shortcoming of Hopfield networks (similar to the Ising model and other greedy and local search methods) is the presence of (many) local minima in their energy function. Although Eq. S2 guarantees the monotonic descendence of Lyapunov energy function, a local minima state may easily

trap the network. Therefore, these models, in general, may not find the global optimum solution. However, in many applications, finding an approximately "good" (and sometimes more energy efficient) solution in a reasonable time is preferred to finding the best solution slowly.

# 2. Combinatorial Optimization with Hopfield Networks

To implement a typical problem within the Hopfield model, we define an (intuitive) energy function, which its minima locate at the same points as the minima of the cost function (of the problem), and map the solution to the neuron states. The energy function is then compared with the generic Lyapunov function of HNN to find the synaptic weights. The inference involves initializing the neuron states or solution and then allowing the recurrent network to converge to a stable state that is interpreted as the ultimate solution. Several wellknown combinatorial optimization problems are considered in our study as follows:

# 2a. Graph Partitioning

Graph bisection, the problem of minimizing the cutsize when partitioning a graph into two sections of nearly equal weight, finds applications in distributed computing and digital VLSI design flow. We define it over an n-vertex undirected graph $G = ( V , E )$ in which $w _ { i }$ and $e _ { i j } ( 1 \leq i , j \leq n )$ are the weights of the $i ^ { \mathrm { t h } }$ vertex and the edge between adjacent nodes $i ^ { \mathrm { t h } }$ and $j ^ { \mathrm { t h } }$ , respectively. The objective is to bisect the graph such that the sum of weight vertices assigned to each partition is equal while the sum of the disconnected edge weights is minimum. A single neuron $( U _ { j } )$ is attributed to each vertex $( V _ { j } )$ ). $U _ { j } = 1$ determines that $V _ { j }$ belongs to partition 1 and $U _ { j } = 0$ is otherwise. The cost function consists of two terms and is given by

$$
E = \alpha \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} e _ {i j} (U _ {i} + U _ {j} - 2 U _ {i} U _ {j}) + \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} w _ {i} w _ {j} (1 - U _ {i} - U _ {j} + 2 U _ {i} U _ {j})
$$

in which $a = 0 . 5$ is a constant representing the relative importance of these two terms [5]. The first term is considered to minimize the weighted sum of the edges (which belong to each cut), and the second one to balance the sum of the node weights in two partitions. Rearranging and dropping the constant terms leads to

$$
E = - \frac {1}{2} \sum_ {i = 1} ^ {n} \sum_ {j = 1, \neq i} ^ {n} \left(2 e _ {i j} - 4 w _ {i} w _ {j}\right) U _ {i} U _ {j} - \sum_ {i = 1} ^ {n} U _ {i} (2 w _ {i} \sum_ {j = 1} ^ {n} w _ {j} - 2 w _ {i} ^ {2} - \sum_ {j = 1} ^ {n} e _ {i j})
$$

which is very similar to the general energy function of Hopfield networks $( \mathrm { E q . S 1 } )$ that is exploited to derive the weights as follows:

$$
T _ {i j} = 2 e _ {i j} - 4 w _ {i} w _ {j}, \qquad T _ {i} ^ {\mathrm {b}} = 2 w _ {i} \sum_ {j = 1} ^ {n} w _ {j} - 2 w _ {i} ^ {2} - \sum_ {j = 1} ^ {n} e _ {i j}.
$$

Note that $- 2 w _ { i } { } ^ { 2 }$ term in bias weights is missing in Ref. [5].

# 2b. Minimum Weighted Vertex Cover Problem

The vertex cover is a fixed-parameter tractable and a central problem in parameterized complexity theory and one of 21 NP-complete problems in Karp's seminal work [6]. The adjacency matrix of $\mathrm { G } , A = \left[ a _ { n \times n } \right]$ , is defined by $a _ { i j } = 1$ if there is an edge between $i ^ { \mathrm { t h } }$ and $j ^ { \mathrm { t h } }$ nodes of graph G, otherwise, $a _ { i j } = 0$ . The vertex cover C is a subset of G if all the edges of G are adjacent to at least one vertex in the set C. In minimum weighted vertex cover problems, the goal is to find the vertex cover with minimum cardinality (or size) whose total weight is also minimum [7]. Similar to the graph partitioning, one neuron is assigned per vertex. $U _ { i } = 1$ determines that $V _ { j }$ is a part of the vertex cover. The cost function is defined by

$$
E = \alpha \sum_ {i = 1} ^ {n} w _ {i} U _ {i} + \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} a _ {i j} (1 - U _ {i}) (1 - U _ {j})
$$

in which α is a constant representing the relative importance of these two terms. The first term is used to minimize the cardinality and total weight, and the second term ensures full coverage of the solution by penalizing the energy whenever there is an edge with endpoints not included in the cover. By dropping the constant terms and comparing them with the generalized energy function, we obtain the weights as

$$
T _ {i j} = - 2 a _ {i j}, \qquad T _ {i} ^ {\mathrm {b}} = 2 \sum_ {j = 1} ^ {n} a _ {i j} - \alpha w _ {i}.
$$

# 2c. Maximum Weight Independent Set Problem

In this problem, we are interested in finding the independent subset C of G with maximum total weight, which neither of its nodes is adjacent. The energy function is formulated by

$$
E = - \alpha \sum_ {i = 1} ^ {n} w _ {i} U _ {i} + \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} a _ {i j} U _ {i} U _ {j},
$$

and all the parameters have the same meaning as before. The first term favors larger sets with larger weights and the second term penalizes the energy if there are adjacent nodes in C. Comparing it with the generic energy function leads to

$$
T _ {i j} = - 2 a _ {i j}, \qquad T _ {i} ^ {\mathrm {b}} = \alpha w _ {i}.
$$

# 2d. Maximum-Weight Clique Problem

A clique is a subset of G in which all nodes are adjacent to each other, and finding a clique with maximum cardinality and the maximum total weight is an NP-compete problem [6]. It finds many applications, e.g., in bioinformatics and analysis of random processes. We consider $U _ { i } = 1$ when $i ^ { \mathrm { t h } }$ node is a part of the maximum clique solution, and use the intuitive energy function

$$
E = - \alpha \sum_ {i = 1} ^ {n} w _ {i} U _ {i} + \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} (1 - a _ {i j}) U _ {i} U _ {j}
$$

in which the first term ensures that the larger the sum of weights in the maximum clique, the lower the energy, and the second term penalizes the energy when the solution includes non-adjacent nodes. We compare it with the general Lyapunov energy function of the Hopfield model to find the weights:

$$
T _ {i j} = 2 (a _ {i j} - 1), \qquad T _ {i} ^ {\mathrm {b}} = \alpha w _ {i}.
$$

# 3. 7-node graph partitioning problem parameters

An arbitrary graph $G { = } ( V , E )$ with the following elements are used (all numbers are rounded to 2 decimal points for clarity):

$$
V = \left( \begin{array}{c c c c c c c} 0 & 8 4. 1 7 & 3. 8 8 & 5 0. 6 4 & 2 7. 5 3 & 3 0. 8 6 & 1 3. 2 1 \\ 8 4. 1 7 & 0 & 1 6. 3 1 & 8 1. 0 4 & 6 5. 8 4 & 4 5. 6 5 & 1 4. 2 1 \\ 3. 8 8 & 1 6. 3 1 & 0 & 9 4. 1 0 & 9 2. 1 8 & 6 1. 6 7 & 9. 0 9 \\ 5 0. 6 4 & 8 1. 0 4 & 9 4. 1 0 & 0 & 4 7. 6 9 & 6 9. 2 3 & 6 5. 5 1 \\ 2 7. 5 3 & 6 5. 8 4 & 9 2. 1 8 & 4 7. 6 9 & 0 & 3 8. 2 4 & 2 8. 1 2 \\ 3 0. 8 6 & 4 5. 6 5 & 6 1. 6 7 & 6 9. 2 3 & 3 8. 2 4 & 0 & 8 2. 1 8 \\ 1 3. 2 1 & 1 4. 2 1 & 9. 0 9 & 6 5. 5 1 & 2 8. 1 2 & 8 2. 1 8 & 0 \end{array} \right), E = \left( \begin{array}{c} 5. 6 4 \\ 3. 8 0 \\ 4. 7 9 \\ 3. 4 2 \\ 8. 4 3 \\ 9. 6 5 \\ 5. 0 1 \end{array} \right)
$$

Then, we employ the energy equations to find the weight matrices:

$$
T = \left( \begin{array}{c c c c c c c} 0 & - 1 0 0. 3 3 & 2 3. 9 6 & - 1 0 0. 3 3 & - 1 3 5. 3 0 & - 1 5 6. 1 3 & - 8 6. 6 5 \\ 8 2. 5 8 & 0 & - 4 0. 1 9 & 1 1 0. 0 0 & 3. 4 4 & - 5 5. 4 4 & - 4 7. 7 4 \\ - 1 0 0. 3 3 & - 4 0. 1 9 & 0 & 1 2 2. 5 5 & 2 2. 7 1 & - 6 1. 6 3 & - 7 7. 8 3 \\ 2 3. 9 6 & 1 1 0. 0 0 & 1 2 2. 5 5 & 0 & - 2 0. 2 4 & 6. 1 5 & 6 2. 3 4 \\ - 1 3 5. 3 0 & 3. 4 4 & 2 2. 7 1 & - 2 0. 2 4 & 0 & - 2 4 9. 2 8 & - 1 1 2. 8 6 \\ - 1 5 6. 1 3 & - 5 5. 4 4 & - 6 1. 6 3 & 6. 1 5 & - 2 4 9. 2 8 & 0 & - 2 9. 1 5 \\ - 8 6. 6 5 & - 4 7. 7 4 & - 7 7. 8 3 & 6 2. 3 4 & - 1 1 2. 8 6 & - 2 9. 1 5 & 0 \end{array} \right), T ^ {\mathrm {b}} = \left( \begin{array}{c} 1 8 5. 9 3 \\ - 2 6. 3 2 \\ 6 7. 3 5 \\ - 1 5 2. 3 9 \\ 2 4 5. 7 6 \\ 2 7 2. 7 5 \\ 1 4 5. 9 5 \end{array} \right)
$$

The runtime change in synaptic weights is shown in Fig. S1a. The weights are slowly deformed, and the network tends to remain in the transitory ground state during the runtime. The results in Fig. 1Sb compare exponential weight annealing with the baseline on all possible runs. The annealing schedule is ? = 40.

![](images/9503355b211093a2666de0974085c796ee3a6d49e73b25f6df2b317ef3778b91.jpg)

![](images/43080e9ef779c981e954992aba92b7a5a247728379e7096596690bd2b40c05fe.jpg)  
Fig. 1S: (a) The change of synaptic weights for the weight annealing technique when solving the 7-node graph partitioning problem. (b) Comparison between the results obtained by exponential weight annealing versus baseline for all 128 runs.

# 4. Additional data on graph partitioning

We have conducted three sets of extensive simulations on weighted graph partitioning. For all configurations, the vertex and edge weights are selected randomly in the ranges of [2:N] and [0:20], respectively. The impact of scaling the problem size is studied for a fixed number of epochs in the main text (Fig. 1d). Here, the simulation results are provided for the case when we scale up the number of epochs with the problem size. NEP is exponentially increased with respect to the problem size in Fig. 2S. The solution quality of weight annealing

is better than simulated annealing for $N { > } 1 0 .$ , as shown in Fig. 2S. Table I shows the parameters used in Figs. 1d, 1e, and 1f (of the main text), and Fig. 2S of supplementary materials.

![](images/76f60b4ca2fd28012c899f92d9d60812e106ad5c1500755edc7535ece1bdae64.jpg)  
Fig. 2S: Extended graph partitioning simulations: The result of increasing the computational time $( N _ { \mathrm { E P } } )$ with respect to the graph size (N). Note that, in this figure, the average energy is added by a constant for better clarity.

Table I: The parameters used in the graph-partitioning simulations   

<table><tr><td rowspan="10">Fig.1d</td><td rowspan="2">N</td><td rowspan="2">Epoch Number</td><td rowspan="2">Case numbers</td><td colspan="3">Annealing Schedule</td></tr><tr><td>Stochastic</td><td>Chaotic</td><td>Exponential</td></tr><tr><td>5</td><td>300</td><td>32</td><td>50</td><td>50</td><td>60</td></tr><tr><td>10</td><td>300</td><td>1000</td><td>60</td><td>500</td><td>60</td></tr><tr><td>15</td><td>300</td><td>10000</td><td>70</td><td>1e3</td><td>60</td></tr><tr><td>20</td><td>300</td><td>10000</td><td>70</td><td>5e3</td><td>60</td></tr><tr><td>25</td><td>300</td><td>10000</td><td>100</td><td>9e3</td><td>60</td></tr><tr><td>30</td><td>300</td><td>10000</td><td>300</td><td>2e4</td><td>60</td></tr><tr><td>40</td><td>300</td><td>10000</td><td>500</td><td>1e5</td><td>60</td></tr><tr><td>50</td><td>300</td><td>10000</td><td>1000</td><td>2e5</td><td>60</td></tr><tr><td rowspan="8">Fig.1f</td><td>25</td><td>100</td><td>10000</td><td>150</td><td>1e3</td><td>20</td></tr><tr><td>25</td><td>200</td><td>10000</td><td>200</td><td>4e3</td><td>40</td></tr><tr><td>25</td><td>400</td><td>10000</td><td>1e3</td><td>1e4</td><td>80</td></tr><tr><td>25</td><td>800</td><td>10000</td><td>5e3</td><td>1e5</td><td>160</td></tr><tr><td>25</td><td>1600</td><td>10000</td><td>1e4</td><td>1e6</td><td>320</td></tr><tr><td>25</td><td>3200</td><td>10000</td><td>5e4</td><td>1e7</td><td>640</td></tr><tr><td>25</td><td>6400</td><td>10000</td><td>1e5</td><td>1e8</td><td>1280</td></tr><tr><td>25</td><td>12800</td><td>10000</td><td>1e6</td><td>1e9</td><td>2560</td></tr><tr><td rowspan="5">Fig.2S</td><td>5</td><td>100</td><td>32</td><td>30</td><td>30</td><td>20</td></tr><tr><td>10</td><td>200</td><td>1000</td><td>60</td><td>60</td><td>40</td></tr><tr><td>15</td><td>400</td><td>10000</td><td>90</td><td>3e3</td><td>80</td></tr><tr><td>20</td><td>800</td><td>10000</td><td>200</td><td>7e3</td><td>160</td></tr><tr><td>25</td><td>1600</td><td>10000</td><td>700</td><td>1e5</td><td>320</td></tr><tr><td rowspan="3"></td><td>30</td><td>3200</td><td>10000</td><td>2e3</td><td>1e6</td><td>640</td></tr><tr><td>40</td><td>6400</td><td>10000</td><td>1e4</td><td>1e7</td><td>1280</td></tr><tr><td>50</td><td>12800</td><td>10000</td><td>1e5</td><td>1e8</td><td>2560</td></tr></table>

# 5. Simulation results on minimum weighted vertex cover, maximum weighted clique, and maximum weighted independent set problems

Similar sets of simulations are performed for three other combinatorial optimization problems as well. Note that simulation parameters (N and NEP) are the same as those for the graph partitioning problem (Table. I), while the annealing schedule might be slightly different since they are manually optimized for each problem type/size. Figs. 3S, 4S, and 5S show the results of the maximum independent set, maximum clique, and minimum vertex cover problems. Similar trends are observed, and weight annealing outperforms other annealing techniques. For the vertex cover, we notice that the weight annealing fails to find the exact solution (i.e., the global optimum) for few large graph configurations. Note that weight annealing is still better or on par with chaotic annealing on average and outperforms simulated annealing in terms of response quality (Top-5 and average energy). We believe that some spurious states generated during the annealing are responsible for those rare underperforming cases.

![](images/b04e0b00e5b0c23df695b7ad6eeb299a9c3a212b8fdf52809c821642368e3465.jpg)  
Fig. 3S: Simulation results on 200 random configurations of the maximum weighted independent set problem with various sizes: (a) the success rate and (the average final energy in the inset) for different sizes and fixed computational time $( N _ { \mathrm { E P } } { = } 3 0 0 )$ , (b) the success rate and (the average final energy in the inset) for different sizes with a varying number of epochs. Note that, in each figure, the actual average energy is added by a constant for better clarity.

![](images/8d10c0d696208a4a99b0884d154dd061c52c499fe60cb2657eb30b703a96f473.jpg)

![](images/cfda0ce76922b8f28d57813aace995caaad92db9387f942e434413654e44906a.jpg)  
Fig. 4S: Simulation results on 200 random configurations of the maximum weighted clique problem with various sizes: (a) the success rate and (the average final energy in the inset) for different sizes and fixed computational time $( N _ { \mathrm { E P } } { = } 3 0 0 )$ , (b) the success rate and (the average final energy in the inset) for different sizes with a varying number of epochs. Note that, in each figure, the actual average energy is added by a constant for better clarity.

![](images/70a4c84073335d4791865d4999e02c1109650dc761164e3bab328dbb7addeeb9.jpg)  
Fig. 5S: Simulation results on 200 random configurations of the minimum weighted vertex cover with various sizes: (a) the success rate and (the average final energy in the inset) for different sizes and fixed computational time $( N _ { \mathrm { E P } } { = } 3 0 0 )$ , (b) the success rate and (the average final energy in the inset) for different sizes with a varying number of epochs. Note that, in each figure, the actual average energy is added by a constant for better clarity.

# 6. Additional details on the 13-node graph partitioning experiment

A random graph $G { = } ( V , E )$ with the following analog weights are used in the memristor-based hardware implementations of weight annealing:

$$
V = \left( \begin{array}{c c c c c c c c c c c c c c} 0 & 1 1 & 6 & 4 & 6 & 1 & 1 & 1 6 & 1 8 & 2 5 & 9 & 4 & 5 \\ 1 1 & 0 & 1 2 & 2 9 & 3 0 & 2 & 1 6 & 1 0 & 1 4 & 5 & 1 4 & 9 & 1 7 \\ 6 & 1 2 & 0 & 3 0 & 1 5 & 3 & 2 5 & 6 & 1 8 & 0 & 1 & 5 & 1 4 \\ 4 & 2 9 & 3 0 & 0 & 1 4 & 8 & 3 & 1 2 & 8 & 3 & 2 & 1 9 & 5 \\ 6 & 3 0 & 1 5 & 1 4 & 0 & 7 & 1 6 & 1 8 & 7 & 8 & 5 & 1 3 & 5 \\ 1 & 2 & 3 & 8 & 7 & 0 & 5 & 1 4 & 1 & 2 8 & 1 6 & 3 0 & 7 \\ 1 & 1 6 & 2 5 & 3 & 1 6 & 5 & 0 & 1 5 & 1 4 & 5 & 3 & 4 & 0 \\ 1 6 & 1 0 & 6 & 1 2 & 1 8 & 1 4 & 1 4 & 0 & 5 & 1 3 & 1 8 & 2 0 & 1 3 \\ 1 8 & 1 4 & 1 8 & 8 & 7 & 1 & 1 4 & 5 & 0 & 1 6 & 1 3 & 1 9 & 1 4 \\ 2 5 & 5 & 0 & 3 & 8 & 2 8 & 5 & 1 3 & 1 6 & 0 & 1 8 & 1 8 & 1 7 \\ 9 & 1 4 & 1 & 2 & 5 & 1 6 & 3 & 1 8 & 1 3 & 1 8 & 0 & 1 0 & 2 \\ 4 & 9 & 5 & 1 9 & 1 3 & 3 0 & 4 & 2 0 & 1 9 & 1 8 & 1 0 & 0 & 1 4 \\ 5 & 1 7 & 1 4 & 5 & 5 & 7 & 0 & 1 3 & 1 4 & 1 7 & 2 & 1 4 & 0 \end{array} \right), E = \left( \begin{array}{c} 1 0 \\ 5 \\ 4 \\ 6 \\ 3 \\ 6 \\ 5 \\ 1 3 \\ 5 \\ 1 4 \\ 1 0 \\ 5 \end{array} \right).
$$

Then, the procedure described in section 2 is utilized to find the synaptic weights and bias matrices of the HNN model:

$$
T = - \left( \begin{array}{c c c c c c c c c c c c c c} 0 & 1 7 8 & 1 4 8 & 1 9 2 & 2 2 8 & 1 1 8 & 2 3 8 & 1 6 8 & 4 8 4 & 1 5 0 & 5 4 2 & 3 9 2 & 1 9 0 \\ 1 7 8 & 0 & 5 6 & 4 2 & 4 2 & 5 6 & 8 8 & 8 0 & 2 3 2 & 9 0 & 2 5 2 & 1 8 2 & 6 6 \\ 1 4 8 & 5 6 & 0 & 2 0 & 2 0 & 4 2 & 4 6 & 6 8 & 1 7 2 & 8 0 & 2 2 2 & 1 5 0 & 5 2 \\ 1 9 2 & 4 2 & 2 0 & 0 & 9 2 & 4 4 & 1 1 4 & 7 6 & 2 4 4 & 9 4 & 2 7 6 & 1 6 2 & 9 0 \\ 2 2 8 & 6 0 & 6 6 & 9 2 & 0 & 5 8 & 1 1 2 & 8 4 & 2 9 8 & 1 0 4 & 3 2 6 & 2 1 4 & 1 1 0 \\ 1 1 8 & 5 6 & 4 2 & 4 4 & 5 8 & 0 & 6 2 & 3 2 & 1 5 4 & 4 & 1 3 6 & 6 0 & 4 6 \\ 2 3 8 & 8 8 & 4 6 & 1 1 4 & 1 1 2 & 6 2 & 0 & 9 0 & 2 8 4 & 1 1 0 & 3 3 0 & 2 3 2 & 1 2 0 \\ 1 6 8 & 8 0 & 6 8 & 7 6 & 8 4 & 3 2 & 9 0 & 0 & 2 5 0 & 7 4 & 2 4 4 & 1 6 0 & 7 4 \\ 4 8 4 & 2 3 2 & 1 7 2 & 2 4 4 & 2 9 8 & 1 5 4 & 2 8 4 & 2 5 0 & 0 & 2 2 8 & 7 0 2 & 4 8 2 & 2 3 2 \\ 1 5 0 & 9 0 & 8 0 & 9 4 & 1 0 4 & 4 & 1 1 0 & 7 4 & 2 2 8 & 0 & 2 4 4 & 1 6 4 & 6 6 \\ 5 4 2 & 2 5 2 & 2 2 2 & 2 7 6 & 3 2 6 & 1 3 6 & 3 3 0 & 2 4 4 & 7 0 2 & 2 4 4 & 0 & 5 4 0 & 2 7 6 \\ 3 9 2 & 1 8 2 & 1 5 0 & 1 6 2 & 2 1 4 & 6 0 & 2 3 2 & 1 6 0 & 4 8 2 & 1 6 4 & 5 4 0 & 0 & 1 7 2 \\ 1 9 0 & 6 6 & 5 2 & 9 0 & 1 1 0 & 4 6 & 1 2 0 & 7 4 & 2 3 2 & 6 6 & 2 7 6 & 1 7 2 & 0 \end{array} \right), T ^ {b} = \left( \begin{array}{c} 1 5 1 4 \\ 6 9 1 \\ 5 6 1 \\ 7 2 3 \\ 8 7 6 \\ 4 0 6 \\ 9 1 3 \\ 7 0 0 \\ 1 8 8 1 \\ 7 0 4 \\ 2 0 4 5 \\ 1 4 5 5 \\ 7 4 7 \end{array} \right).
$$

To realize weight annealing within our memristive crossbars, we encode the normalized weights $( T _ { i j } < 0$ and $T _ { j } ^ { b } > 0 )$ to device conductances by using $g _ { i j } = G _ { \mathrm { m a x } } ( T _ { i j } / | W ^ { \mathrm { m a x } } | )$ and $g _ { j } ^ { b } = G _ { \mathrm { m a x } } ( T _ { j } ^ { b } / | W ^ { \mathrm { m a x } } | )$ where $| W ^ { \mathrm { m a x } } | = \operatorname* { m a x } { \{ | T | , | T ^ { b } | \} }$ , where $G _ { \mathrm { m a x } }$ is a predetermined value. Memristive crossbars inherently implement the dot-product using Ohm and Kirchhoff's laws, i.e.,

$$
V (t + 1) = \mathrm {f} \left(\sum_ {i = 1} ^ {N} g _ {i j} V _ {i} (t) + g _ {j} ^ {b} V ^ {\mathrm {a p}}\right). \tag {S3}
$$

Note that $\operatorname { f } ( . )$ is the binary activation function realized by a comparator in peripheral circuits. In our experimental setup, straightforward peripheral functionalities such as current sensing and binary activation

function are emulated by Agilent characterization tools. In exponential weight annealing, $V _ { i } ( t ) = V _ { i } ^ { \mathrm { a p } } ( t ) ( 1 -$ $\mathbf { e } ^ { \frac { - t } { \tau } } )$ is the applied voltage to the $i ^ { \mathrm { t h } }$ input and $V _ { i } ^ { \mathrm { a p } } ( t )$ is either 0 or $V _ { \mathrm { a p } } ,$ based on the neuron state. Given that, we rewrite Eq. S3 as

$$
\begin{array}{l} V (t + 1) = \mathrm {f} \left(\frac {V ^ {\mathrm {a p}} G _ {\mathrm {m a x}}}{| W ^ {\mathrm {m a x}} |} \sum_ {i = 1} ^ {N} T _ {i j} (V _ {i} (t) / V ^ {\mathrm {a p}}) + T _ {j} ^ {\mathrm {b}}\right) \\ = \mathrm {f} \left(\frac {V ^ {\mathrm {a p}} G _ {\mathrm {m a x}}}{| W ^ {\mathrm {m a x}} |} \sum_ {i = 1} ^ {N} T _ {i j} (V _ {i} ^ {\mathrm {a p}} (t) (1 - e ^ {\frac {- t}{\tau}}) / V ^ {\mathrm {a p}}) + T _ {j} ^ {b}\right) \\ \end{array}
$$

![](images/0d759721bd7e6b65544e42bf4c33ea5b566baf35ed0bc9eaca43e67f52963259.jpg)

$$
= \mathrm {f} \left(\frac {V ^ {\mathrm {a p}} G _ {\operatorname* {m a x}}}{\left| W ^ {\operatorname* {m a x}} \right|} \sum_ {i = 1} ^ {N} w _ {i j} (t) \left(V _ {i} ^ {a p} (t) / V ^ {\mathrm {a p}}\right) + T _ {j} ^ {b}\right), \tag {S4}
$$

which is essentially the hardware implementation of Eq. 1 of the main text.

# 7. Additional details the 7-node maximum weight independent set experiment

For the eFlash-based experimental demonstration, a graph with the following adjacency matrix and nodal weights are assumed:

$$
A = \left( \begin{array}{l l l l l l l} 0 & 1 & 1 & 0 & 1 & 1 & 1 \\ 1 & 0 & 1 & 1 & 1 & 1 & 1 \\ 1 & 1 & 0 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 1 & 1 \\ 1 & 1 & 1 & 0 & 0 & 1 & 1 \\ 1 & 1 & 0 & 1 & 1 & 0 & 1 \\ 1 & 1 & 0 & 1 & 1 & 1 & 0 \end{array} \right), E = \left( \begin{array}{l} 6. 4 0 \\ 7. 3 8 \\ 5. 0 5 \\ 1. 2 1 \\ 3. 4 3 \\ 2. 0 2 \\ 6. 0 9 \end{array} \right)
$$

Section S2 discusses the equations for solving the 7-node maximum weight independent set problem. Accordingly, the synaptic weights are found by assuming $\alpha = 0 . 5$ :

$$
T = - \left( \begin{array}{l l l l l l l} 0 & 2 & 2 & 0 & 2 & 2 & 2 \\ 2 & 0 & 2 & 2 & 2 & 2 & 2 \\ 2 & 2 & 0 & 2 & 2 & 0 & 0 \\ 0 & 2 & 2 & 0 & 2 & 2 & 2 \\ 2 & 2 & 2 & 0 & 0 & 2 & 2 \\ 2 & 2 & 0 & 2 & 2 & 0 & 2 \\ 2 & 2 & 0 & 2 & 2 & 2 & 0 \end{array} \right), T ^ {b} = \left( \begin{array}{l} 3. 2 0 \\ 3. 6 9 \\ 2. 5 2 \\ 0. 6 0 \\ 1. 7 1 \\ 1. 0 1 \\ 3. 0 4 \end{array} \right)
$$

The embedded flash memory array consists of supercells (Fig. 6S), and we can tune each floating-gate cell to a desired current value at nominal biasing conditions. Neglecting the drain-source voltage, $I _ { \mathrm { D S } } \approx$

$I _ { 0 } e ^ { \frac { V _ { \mathrm { W L } } - V _ { \mathrm { t h } } } { n V _ { \mathrm { t h } } } } \approx \theta _ { 0 } I _ { 0 } e ^ { \frac { V _ { \mathrm { W L } } } { n V _ { \mathrm { t h } } } }$ ೇ౓ైషೇ౪౞ ೇ౓ై where $\theta _ { 0 }$ is the effective weight of the devices, and other parameters have their usual meaning. We define $I _ { i j } ( V _ { \mathrm { W L } } ) = \theta _ { i j } I _ { 0 } e ^ { \frac { V _ { W L } } { n V _ { \mathrm { t h } } } }$ ೇೈಽ and $I _ { j } ^ { b } = \theta _ { j } ^ { b } I _ { 0 } e ^ { \frac { V _ { \mathrm { a p } } } { n V _ { \mathrm { t h } } } }$ ೇ౗౦ . During tunning, we make sure that $I _ { i j } ( V ^ { \mathsf { a p } } ) = \frac { I _ { \mathsf { m a x } } T _ { i j } } { | W ^ { \mathsf { m a x } } | }$ and $\begin{array} { r } { I _ { j } ^ { b } = \frac { I _ { \mathrm { m a x } } T _ { j } ^ { b } } { | W ^ { \mathrm { m a x } } | } } \end{array}$ where $| W ^ { \mathrm { m a x } } | = \operatorname* { m a x } { \{ | T | , | T ^ { b } | \} }$ , and $I _ { \mathrm { m a x } }$ is a predetermined value. Hence,

$$
\theta_ {i j} = \frac {I _ {\mathrm {m a x}} T _ {i j}}{| W ^ {\mathrm {m a x}} | I _ {0}} e ^ {\frac {- V ^ {\mathrm {a p}}}{n V _ {\mathrm {t h}}}}, \qquad \theta_ {j} ^ {b} = \frac {I _ {\mathrm {m a x}} T _ {j} ^ {b}}{| W ^ {\mathrm {m a x}} | I _ {0}} e ^ {\frac {- V ^ {\mathrm {a p}}}{n V _ {\mathrm {t h}}}} \qquad \mathrm {(S 5)}
$$

The update rule for the $j ^ { \mathrm { t h } }$ neuron is given by

$$
V (t + 1) = \mathrm {f} \left(\sum_ {i = 1} ^ {N} I _ {i j} \left(V _ {i} (t)\right) + I _ {j} ^ {b}\right) \tag {S6}
$$

and $V _ { i } ( t )$ is the gate-applied voltage to the $i ^ { \mathrm { t h } }$ input terminal at iteration ?. It is effortless to show that S6 performs the dot-product of (two-state) input voltage vector and (analog) weights. Note that we apply the digital inputs $( V _ { \mathrm { W L } } = 0 ~ \mathrm { V }$ corresponds to ~0 synaptic current and $V _ { \mathrm { W L } } = V ^ { \mathrm { a p } } = 1 . 5 V$ corresponds to the 'on' current for the baseline operation) in the gate-line direction and read the summed currents from the bitlines, (e.g., using a transimpedance amplifier or a current conveyor) to $V _ { B L } = 1 V$ .

For the exponential weight annealing, we substitute $I _ { i j }$ and $I _ { j } ^ { \mathrm { b } }$ in S6 using S5 and obtain

$$
\begin{array}{l} V (t + 1) = \mathrm {f} \left(\sum_ {i = 1} ^ {N} \frac {I _ {\mathrm {m a x}} T _ {i j}}{| W ^ {\mathrm {m a x}} | I _ {0}} e ^ {\frac {- V ^ {\mathrm {a p}}}{n V _ {\mathrm {t h}}}} I _ {0} e ^ {\frac {V _ {i} (t)}{n V _ {\mathrm {t h}}}} + \frac {I _ {\mathrm {m a x}} T _ {j} ^ {\mathrm {b}}}{| W ^ {\mathrm {m a x}} | I _ {0}} e ^ {\frac {- V ^ {\mathrm {a p}}}{n V _ {\mathrm {t h}}}} I _ {0} e ^ {\frac {V _ {\mathrm {a p}}}{n V _ {\mathrm {t h}}}}\right) = \\ = f \left(\frac {I _ {\mathrm {m a x}}}{| W ^ {\mathrm {m a x}} |} \sum_ {i = 1} ^ {N} T _ {i j} e ^ {\frac {V _ {i} (t) - V ^ {\mathrm {a p}}}{n V _ {\mathrm {t h}}}} + T _ {j} ^ {\mathrm {b}}\right) \\ \end{array}
$$

and $\begin{array} { r } { V _ { i } ( t ) = \frac { V _ { i } ^ { \mathrm { a p } } ( t ) t } { \tau } \left( \tau \right. } \end{array}$ is the annealing schedule) for the semi-exponential learning (it is "semi" since the devices have nonlinearities in their I-V) and $V _ { i } ( t ) = V _ { i } ^ { \mathrm { a p } } ( t ) ( 1 - e ^ { \frac { - t } { \tau } } )$ for the super-exponential learning. Fig. 7Sa shows the weight change for the former case, i.e., linear voltage scaling with $\tau = 5 0 0$ , and the main synaptic weights grow semi-exponentially. Also, since the currents are extremely small for $V _ { W L } < 0 . 7$ , the

ground state of the system remains constant for a significant period. We prevent this by starting from $V _ { \mathrm { W L } , 0 } =$ 0.7 and govern the annealing by

$$
V _ {i} (t) = \frac {(V _ {i} ^ {a p} (t) - V _ {W L , 0}) t}{\tau} + V _ {W L, 0}.
$$

Fig. 7Sb shows the experimental results on the impact of the annealing schedule and linear versus exponential voltage scaling. We obtain a better solution with slower annealing, particularly with the linear scaling in which the trend is much more apparent. The slowest linear scaling annealing, i.e., when $\tau _ { \mathrm { l i n } } = 5 0 0$ leads to the best solution.

![](images/98528434d1356e035dc708f5087b96f6e5592222ae3bff6239ee3c33100e453c.jpg)

![](images/79e4892b9ea38c4f5b76c161d4ab553a99f4c5a31ee794fd67155f64c2f6cfd4.jpg)

![](images/166160ebf873c572746276c2b32843f78e6ea52f1027ab2d5ea379957e91bd18.jpg)

![](images/b7d77a3f07f7f773d260129ae6a4d29f5affd53ec6a60d58b60f87515569a5a4.jpg)

![](images/19a8a620968d8ce5777126abed1d864904c37fc0759fcf451800e159d22cc22a.jpg)  
Fig. 6S: (a) The schematic of SST's eFlash supercell consisting of 2 analog-grade floating-gate cells and (b) its TEM image. (c) The weak inversion I-V characteristics of a flash cell programmed with 1% accuracy. (d) The schematic of a single channel recurrent neuro-optimizer. For clarity, we show the feedback signal only from the first channel.

![](images/cac158b7d4c29ffe252d9f55a62ae72fac156629069d347531a05e0298eaa499.jpg)  
Fig. 7S: Extended experimental results of the 7-node maximum weighted independent set problem: (a) weight evolution during weight annealing (linear voltage scaling), (b) the impact of changing the annealing schedule (?) for both cases of linear and exponential voltage scaling.

# 8. The performance of the proposed circuit

We design the peripheral circuits (amplifiers, current reference, and dynamic comparator) in Global Foundries 55 nm CMOS technology to determine the power, area, and speed of the circuit. 3-stage recycling folded cascode amplifiers are considered for designing the transimpedance amplifiers in the presynaptic and postsynaptic circuits and use the strongARM latch to develop the dynamic comparator. Flash memories have a large output impedance in weak inversion. This allows us to use faster and more compact circuits, e.g., current conveyors, for designing the readout circuit (see [25]). We assume 130×64 arrays, which can implement a full-differential 64×64 Hopfield network. In our estimation, we also consider the area of tuning circuits, analog switches, and decoders and exclude clocking and IO circuits as they can be shared with other system-on-chip modules. The circuits are designed targeting 2 ns settling time in dot-product operation and 0.5 ns sampling time in the comparator (hence, ~2.5 ns/update) in the typical corner. Such design parameters lead to ~0.33 pJ/update, ${ \sim } 3 , 0 3 8 ~ \mu \mathrm { m } ^ { 2 }$ active area with $4 F ^ { 2 }$ memristors, assuming 1 μs annealing schedule (2,000 epochs per run). For the eFlash technology, we obtain 0.09 pJ/update and ${ \sim } 1 0 , 9 9 2 ~ { \mu } \mathrm { m } ^ { 2 }$ active area with ${ \sim } 1 1 0 F ^ { 2 }$ redesigned eFlash memories, assuming 1 μs annealing schedule. These preliminary data suggest that our approach could potentially be $1 0 ^ { 2 } \times$ faster and $1 0 ^ { 5 } \times$ more energy efficient as compared to the most efficient conventional methods based on graphics processor units on the same task.

# 9. Experimental Setups

![](images/3879d3b9b4842febdd828f535253d317937ff2c425c54ff8e8b6c4fa5d0af658.jpg)  
Fig. 8S: The Experimental setup for (a) the 13-node graph partitioning implemented with memristive devices and (b) the 7-node maximum weighted independent set realized with an eFlash memory array. The experimental setups comprise of a personal computer to control parameter analyzer B1500A, arbitrary waveform generator B1530A, and a switch matrix (a low-leakage Agilent E5250A in (a) and a custom circuit for (b)). Both memristive crossbar and flash array are mounted on custom host circuit board and connected to their corresponding switch matrices.

# References

[1] Hopfield, John J., and David W. Tank. ""Neural" computation of decisions in optimization problems." Biological cybernetics 52.3 (1985): 141-152.   
[2] Hopfield, John J. "Neural networks and physical systems with emergent collective computational abilities." Proceedings of the national academy of sciences 79.8 (1982): 2554-2558   
[3] Tank, Df, and J. J. Hopfield. "Simple' neural 'optimization networks: An A/D converter, signal decision circuit, and a linear programming circuit." IEEE transactions on circuits and systems 33.5 (1986): 533-541.   
[4] Joya, Gonzalo, M. A. Atencia, and Francisco Sandoval. "Hopfield neural networks for optimization: study of the different dynamics." Neurocomputing 43.1-4 (2002): 219-237.   
[5] J. Ramanujam and P. Sadayappan, "Mapping combinatorial optimization problems onto neural networks", Information Science, vol. 82, pp. 239-255, 1995.   
[6] R. M. Karp, "Reducibility among combinatorial problems", Complexity of computer computations, Springer, Boston, MA, pp. 85-103, 1972.   
[7] M. N. Syed, and P. M. Pardalos, "Neural network models in combinatorial optimization", Handbook of Combinatorial Optimization, pp. 2027-2093, 2013.   
[8] M. R. Mahmoodi, and D. Strukov. "An ultra-low energy internally analog, externally digital vector-matrix multiplier based on NOR flash memory technology." Proceedings of the 55th Annual Design Automation Conference. 2018.