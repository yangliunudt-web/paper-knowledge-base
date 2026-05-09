---
title: "FUEL: Fast UAV Exploration Using Incremental Frontier Structure"
date: "2021-02-01"
year: 2021
journal: "IEEE Robotics and Automation Letters"
doi: "10.1109/LRA.2020.3047374"
abstract: "Autonomous exploration is a fundamental problem for various applications of unmanned aerial vehicles(UAVs). Existing methods, however, were demonstrated to insufficient exploration rate, due to the lack of efficient global coverage, conservative motion plans and low decision frequencies. In this paper, we propose FUEL, a hierarchical framework that can support Fast UAV ExpLoration in complex unknown environments. We maintain crucial information in the entire space required by exploration planning by a frontier information structure (FIS), which can be updated incrementally when the space is explored. Supported by the FIS, a hierarchical planner plans exploration motions in three steps, which find efficient global coverage paths, refine a local set of viewpoints and generate minimum-time trajectories in sequence. We present extensive benchmark and real-world tests, in which our method completes the exploration tasks with unprecedented efficiency (3-8 times faster) compared to state-of-the-art approaches."
abstract_cn: "自主探索是无人机各类应用的基础问题。然而现有方法探索效率不足，原因是缺乏高效的全局覆盖、保守的运动规划和低决策频率。本文提出 FUEL，一个可在复杂未知环境中支持快速无人机探索的分层框架。通过前沿信息结构（FIS）维护探索规划所需的整个空间的关键信息，该结构在空间被探索时可增量更新。在 FIS 支持下，分层规划器分三步规划探索运动：找到高效的全局覆盖路径、细化局部视点集、顺序生成最小时间轨迹。"
cite: "Zhou B, Zhang Y, Chen X, et al. FUEL: Fast UAV exploration using incremental frontier structure[J]. IEEE Robotics and Automation Letters, 2021, 6(2): 777-784. DOI: 10.1109/LRA.2020.3047374."
aiSum: "FUEL 无人机探索：前沿信息结构（FIS）增量更新、分层规划、3-8 倍速度提升、香港科技大学。"
confidence: "medium"
authors:
  - "Boyu Zhou"
  - "Yichen Zhang"
  - "Xinyi Chen"
  - "Shaojie Shen"
keywords:
  - "[[UAV]]"
  - "[[Autonomous exploration]]"
  - "[[Frontier information structure]]"
  - "[[Motion planning]]"
wiki_concepts:
  - "[[Robotics]]"
---

Abstract—Autonomous exploration is a fundamental problem for various applications of unmanned aerial vehicles(UAVs). Existing methods, however, were demonstrated to insufficient exploration rate, due to the lack of efficient global coverage, conservative motion plans and low decision frequencies. In this paper, we propose FUEL, a hierarchical framework that can support Fast UAV ExpLoration in complex unknown environments. We maintain crucial information in the entire space required by exploration planning by a frontier information structure (FIS), which can be updated incrementally when the space is explored. Supported by the FIS, a hierarchical planner plans exploration motions in three steps, which find efficient global coverage paths, refine a local set of viewpoints and generate minimum-time trajectories in sequence. We present extensive benchmark and real-world tests, in which our method completes the exploration tasks with unprecedented efficiency (3-8 times faster) compared to state-of-the-art approaches. Our method will be made open source to benefit the community1 .

Index Terms—Aerial Systems: Applications; Aerial Systems: Perception and Autonomy; Motion and Path Planning

# I. INTRODUCTION

U NMANNED aerial vehicles, especially quadrotors havegained widespread popularity in various applications, gained widespread popularity in various applications, such as inspection, precision agriculture, and search and rescue. Among the tasks, autonomous exploration, in which the vehicle explores and maps the unknown environment to gather information, is a fundamental component.

Various exploration planning methods have been proposed in recent years, with some real-world experiments presented [1]–[4]. However, most of them demonstrate a low/medium exploration rate, which is unsatisfactory for many large-scale real-world applications. First of all, many existing planners plan exploring motions in greedy manners, such as maximizing the immediate information gain, or navigating to the closest unknown region. The greedy strategies ignore global optimality and therefore result in low overall efficiency. Besides, most methods generate rather conservative motions in order to guarantee information gain and safety simultaneously in previously unknown environments. Low-speed exploration,

Manuscript received: October, 15, 2020; Accepted December, 13, 2020. This paper was recommended for publication by Editor Pauline Pounds upon evaluation of the Associate Editor and Reviewers’ comments. This work was supported by Research Grants Council (RGC) project no.16213717, ITC project no.ITT/027/19GP, HDJI lab. All authors are with the Department of Electronic and Computer Engineering, Hong Kong University of Science and Technology, Hong Kong, China. {bzhouai, yzhangec, xchencq, eeshaojie}@connect.ust.hk. Digital Object Identifier (DOI): see top of this page.

1To be released at https://github.com/HKUST-Aerial-Robotics/FUEL

![](images/1a9e69dc069d24cea0da8428b18e282ffe30512f8d0f708bccfe32edb02f5185.jpg)  
(a) A cluttered environment for the exploration tests.

![](images/908b1afb8ae79872b46b4e18162eda000e0f47dd2b85aed4e365d3037751c2db.jpg)  
(b) The online built map and executed trajectory.   
Fig. 1. A quadrotor autonomous exploration test conducted in a complex indoor scene. Video of the experiments is available at: https://www.youtube. com/watch?v= dGgZUrWk-8.

however, disallows quadrotors to fully exploit their dynamic capability to fulfill the missions. Last but not least, many methods suffer from high computational overhead and can not respond quickly and frequently to environmental changes. However, to enable faster exploration, it is desirable to replan new motions immediately whenever new information of the environment is available.

Motivated by the above facts, this paper proposes FUEL, a hierarchical framework that can support Fast UAV ExpLoration in complex environments. We introduce a frontier information structure (FIS), which contains essential information in the entire space required by exploration planning. The structure can be updated efficiently and incrementally when new information is collected, so it is capable of supporting high-frequency planning. Based on the FIS, a hierarchical planner generates exploring motion in three coarse-to-fine steps. It starts by finding a global exploration tour that is optimal in the context of accumulated environment information.

Then, viewpoints on a local segment of the tour are refined, further improving the exploration rate. Finally, a safe, dynam-

ically feasible and minimum-time trajectory is generated. The planner produces not only efficient global coverage paths, but also safe and agile local maneuvers. Moreover, the planner is triggered whenever unvisited regions are explored, so that the quadrotor always responds promptly to any environmental changes, leading to consistently fast exploration.

We compare our method with classic and state-of-the-art methods in simulation. Results show that in all cases our method achieves complete exploration in much shorter time (3-8 times faster). What’s more, we conduct fully onboard realworld exploration in various challenging environments. Both the simulation and real-world tests demonstrate an unprecedented performance of our method compared to state-of-theart ones. To benefit the community, we will make the source code public. The contributions of this paper are summarized as follows:

1) An incrementally updated FIS, which captures essential information of the entire explored space and facilitates exploration planning in high frequency.   
2) A hierarchical planning method, which generates efficient global coverage paths, and safe and agile local maneuvers for high-speed exploration.   
3) Extensive simulation and real-word tests that validate the proposed method. The source code of our system will be made public.

# II. RELATED WORK

# A. Exploration Path Planning

Robotic exploration, which uses mobile robots to map unknown environments, has been studied for years. Some of the works focus on exploring the space quickly [1, 5], as this paper does. Meanwhile, other methods place more emphasis on accurate reconstruction [2, 6]. Among the various proposed methods, the frontier-based approaches are one type of classic approaches. The methods are first introduced in [7] and evaluated more comprehensively afterwards in [8]. To detect frontiers in 3D space, a stochastic differential equationbased method is proposed in [9]. In the original method [7], the closest frontier is selected as the next target. [1] presented a different scheme. In every decision, it selects the frontier within the FOV that minimizes the velocity change to maintain a consistently high flight speed. This scheme is shown to outperform the classic method [7]. In [10], a differentiable measure of information gain based on frontiers is introduced, allowing paths to be optimized with gradient information.

Sampling-based exploration, as another type of major approaches, generate viewpoints randomly to explore the space. These methods are closely related to the concept of next best view (NBV) [11], which computes covering views repeatedly to obtain a complete model of a scene. [12] first used NBV in 3D exploration, in which it expands RRTs with accessible space and executes the edge with the highest information gain in a receding horizon fashion. The method was extended to consider uncertainty of localization [13], visual importance of different objects [14] and inspection tasks [15] later. To avoid discarding the expanded trees directly, roadmaps are constructed in [16, 17] to reuse previous knowledge. [2] maintains and refines a single tree continuously using a rewiring

![](images/378090cf42f897befc8229287576bd283ad9feb9f86765ba457637d3e3a532ee.jpg)  
Fig. 2. An overview of the proposed exploration framework.

scheme inspired by RRT*. To achieve faster flight, [5] samples safe and dynamically feasible motion primitives directly and execute the most informative one.

There are also methods combining the advantages of frontier-based and sampling-based approaches. [4, 18] plan global paths toward frontiers and sample paths locally. [18] also presented a gradient-based method to optimize the local path. [3] samples viewpoints around frontiers and finds the global shortest tour passing through them. [6] generates inspection paths that cover the frontier completely using a sampling-based algorithm.

Most of existing methods make decision greedily and does not account for the dynamics of the quadrotor, which leads to inefficient global tours and conservative maneuvers. In contrast, we plan tours that efficiently cover the entire environment and generate dynamically feasible minimum-time trajectories to enable agile flight.

# B. Quadrotor Trajectory Planning

Trajectory planning for quadrotor has been widely studied, which can be categorized into the hard-constrained and softconstrained approaches in major. The former is pioneered by minimum-snap trajectory [19], whose closed-form solution was presented [20] later. Based on [19], [21]–[23] extract convex safe regions for safe trajectory generation. To obtain a more reasonable time allocation, fast marching [22], kinodynamic search [23] and mixed integer-based methods [24] are proposed. [22] also introduced an efficient Bezier curve-based´ method to guarantee feasibility.

Soft-constrained methods typically formulate a non-linear optimization trading off several objectives. Recently [25]– [30] applied them to local replanning, demonstrating their attractive performance. The methods were revived by [31] and extended to continuous-time trajectories [25] later. To relieve the issue of local minima, [26] initializes the optimization with collision-free paths. [27] introduces uniform B-splines for replanning. More recently, [28] further exploited B-splines and demonstrated fast flight in field tests. [28] is further improved with topological guiding paths and perception-awareness in [29, 30].

In this paper, we base our trajectory planning on [28] but extend it to optimize all parameters of B-splines. In this way, the total trajectory time can be minimized so that the unknown space is explored with a higher navigation speed.

![](images/25279a54c8c26d46f71d3fe8d93d138a947a6b28bd020ce17d36cd2d450b97dc.jpg)

![](images/3b1b7224936c509fccba2402d23957339acf003b6ceabadec9dadcebd0a130c1.jpg)

![](images/f1d2bc48e22875d8e8ab0be4463f709365089433cf1686213c25541a81688a4b.jpg)

Fig. 3. Incremental frontier detection and clustering. Top: detecting and removing outdated frontiers. Bottom: new frontier is detected (left) and PCA is performed, the large cluster is split into two smaller ones (right).   
![](images/cbda58cd0e8cc5265a8639da78d9170ebd33d7cfde13d0d315b5cb86137c40c3.jpg)  
FreeOccupiedUnknown Frontiers   
Bm C1ET1 Bt Principal components

# III. SYSTEM OVERVIEW

The proposed framework operates upon a voxel grid map. As illustrated in Fig.2, it is composed of an incremental update of the FIS (Sect.IV) and a hierarchical exploration planning approach (Sect.V). Whenever the map is updated using sensor measurements, it is examined whether any frontier clusters are influenced. If so, FISs of influenced clusters are removed while new frontiers along with their FISs are extracted (Sect.IV). After that, the exploration planning is triggered, which finds global exploration tour, refines local viewpoints, and generates trajectory to a selected viewpoint successively (Sect.V). The exploration is considered finished if no frontier exists.

# IV. INCREMENTAL FRONTIER INFORMATION STRUCTURE

As presented in classic frontier-based exploration [7], frontiers are defined as known-free voxels right adjacent to unknown voxels, which are grouped into clusters to guide the navigation. Traditionally, the extracted information is too coarse to do fine-grained decision making. Besides, frontiers are retrieved by processing the entire map, which is not scalable for large scenes and high planning frequencies. In this work, we extract richer information from frontiers to enable more elaborate planning, and develop an incremental approach to detect frontiers within the locally updated map.

# A. Frontier Information Structure

A frontier information structure $F I _ { i }$ is computed when a new frontier cluster $F _ { i }$ is created. It stores all cells $C _ { i }$ belonging to the cluster and the average position $\mathbf { p } _ { \mathrm { a v g } , i }$ of $C _ { i }$ . The axis-aligned bounding box (AABB) $B _ { i }$ of the cluster is also computed, in order to accelerate the detection of frontier changes (Sect.IV-B). To serve the exploration planning (Sect.V), candidate viewpoints $V P _ { i }$ are generated around the cluster. Besides, a doubly linked list $L _ { \mathrm { c o s t } , i }$ containing connection costs between $F _ { i }$ and all other clusters is computed. Data stored by a FIS is listed in Tab.I.

![](images/92e117a8f9710accfa107de254e327afd3d0ac1115ab6ab1e992b6d60d49c32c.jpg)  
Fig. 4. Generating candidate viewpoints for a frontier cluster. Within the cylindrical coordinate system centered at the average position of the cluster, points are sampled uniformly.

TABLE I DATA CONTAINED BY A FIS F Ii OF CLUSTER Fi.   

<table><tr><td>Data</td><td>Explanation</td></tr><tr><td>Ci</td><td>Frontier cells that belong to the cluster</td></tr><tr><td>pavg,i</td><td>Average position of Ci</td></tr><tr><td>Bi</td><td>Axis-aligned bounding box of Ci</td></tr><tr><td>VPi</td><td>Viewpoints covering the cluster</td></tr><tr><td>Lcost,i</td><td>Doubly linked list of connection costs to all other clusters</td></tr></table>

# B. Incremental Frontier Detection and Clustering

As depicted in Fig.3, every time the map is updated by sensor measurements, the AABB of the updated region $B _ { m }$ is also recorded, within which outdated frontier clusters are removed and new ones are searched. It starts with going through all clusters and returning only those whose AABBs $( B _ { i } )$ intersect with $B _ { m } .$ Then, precise checks are conducted for the returned clusters, among which the ones containing cells that are no longer frontier are removed. These two processes are inspired by the broad/narrow phase collision detection algorithms [32], which eliminate most unaffected clusters in a fast way and significantly reduce the number of expensive precise checks.

After the removal, new frontiers are searched and clustered into groups by the region growing algorithm, similar to the classic frontier-based method. Among the groups, the ones with a small number of cells typically resulting from noisy sensor observations are ignored. The remaining groups, however, may contain large-size clusters which are not conducive to distinguishing distinctive unknown regions and making elaborate decisions. Therefore, we perform Principal Component Analysis (PCA) for each cluster and split it into two uniform ones along the first principal axis, if the largest eigenvalue exceeds a threshold. The split is conducted recursively so that all large clusters are divided into small ones.

# C. Viewpoint Generation and Cost Update

Intuitively, a frontier cluster implies a potential destination to explore the space. However, unlike previous approaches which simply navigate to the center of a cluster, we desire more elaborate decision making. To this end, when a cluster $F _ { i }$ is created, we generate a rich set of viewpoints $V P _ { i } =$

$\{ \mathbf { x } _ { i , 1 } , \mathbf { x } _ { i , 2 } , \cdot \cdot \cdot , \mathbf { x } _ { i , n _ { i } } \}$ covering it, where $\mathbf { x } _ { i , j } = ( \mathbf { p } _ { i , j } , \xi _ { i , j } )$ . $V P _ { i }$ are found by uniformly sampling points in the cylindrical coordinate system whose origin locates at the cluster’s center, as displayed in Fig.4. For each of the sampled points p lying within the free space, the yaw angle ⇠ is determined as the one maximizing sensor coverage to the cluster, by using a yaw optimization method similar to [16]. The coverage is evaluated as the number of frontier cells that comply with the sensor model and are not occluded by occupied voxels. Then, viewpoints with coverage higher than a threshold are reserved and sorted in descending order of coverage. We reserve at most $N _ { \mathrm { v i e w } }$ viewpoints in $V P _ { i } \ ( n _ { i } \leq N _ { \mathrm { v i e w } } )$ to make the local viewpoint refinement (Sect.V) tractable.

To perform global planning of exploration tour (Sect.V), a connection cost between each pair of clusters $( F _ { k _ { 1 } } , F _ { k _ { 2 } } )$ is required. Let $t _ { \mathrm { I b } } \big ( \mathbf { x } _ { k _ { 1 } , j _ { 1 } } , \mathbf { x } _ { k _ { 2 } , j _ { 2 } } \big )$ denotes a time lower bound when moving between two viewpoints $\mathbf { x } _ { k _ { 1 } , j _ { 1 } }$ and $\mathbf { x } _ { k _ { 2 } , j _ { 2 } }$ , it is computed by:

$$
t _ {\mathrm {l b}} \left(\mathbf {x} _ {k _ {1}, j _ {1}}, \mathbf {x} _ {k _ {2}, j _ {1}}\right) = \max  \left\{\frac {\text {l e n g t h} \left(P \left(\mathbf {p} _ {k _ {1} , j _ {1}} , \mathbf {p} _ {k _ {2} , j _ {2}}\right)\right)}{v _ {\max }} \right., \tag {1}
$$

$$
\left. \frac {\operatorname* {m i n} \left(\left| \xi_ {k _ {1} , j _ {1}} - \xi_ {k _ {2} , j _ {2}} \right| , 2 \pi - \left| \xi_ {k _ {1} , j _ {1}} - \xi_ {k _ {2} , j _ {2}} \right|\right)}{\dot {\xi} _ {\operatorname* {m a x}}} \right\}
$$

where $P \left( \mathbf { p } _ { k _ { 1 } , j _ { 1 } } , \mathbf { p } _ { k _ { 2 } , j _ { 2 } } \right)$ denote a collision-free path between $\mathbf { p } _ { k _ { 1 } , j _ { 1 } }$ and $\mathbf { p } _ { k _ { 2 } , j _ { 2 } }$ found by a path searching algorithm, $v _ { \mathrm { m a x } }$ and $\xi _ { \mathrm { m a x } }$ are the limits of velocity and angular rate of yaw. For each pair $( F _ { k _ { 1 } } , F _ { k _ { 2 } } )$ , we select the viewpoints with highest coverage and estimate the cost as $t _ { \mathrm { l b } } \big ( \mathbf { x } _ { k _ { 1 } , 1 } , \mathbf { x } _ { k _ { 2 } , 1 } \big )$ , in which $P \left( \mathbf { p } _ { k _ { 1 } , 1 } , \mathbf { p } _ { k _ { 2 } , 1 } \right)$ is searched on the voxel grid map using the $\mathbf { A } ^ { * }$ algorithm.

Note that computing connection costs between all pairs of $N _ { \mathrm { c l s } }$ clusters from scratch requires $O ( N _ { \mathrm { c l s } } ^ { 2 } ) ~ \mathrm { A ^ { * } }$ searching, which is considerably expensive. Fortunately, the costs can also be computed in an incremental manner. When any outdated clusters are removed (Sect.IV-B), associated cost items in $L _ { \mathrm { c o s t } , i }$ of all remaining FISs are erased. After that, connection costs from each new cluster to all other clusters are computed and inserted into $L _ { \mathrm { c o s t } , i }$ . Suppose there are $k _ { \mathrm { n e w } }$ new clusters in each frontier detection, the above update scheme takes $O ( k _ { \mathrm { n e w } } \cdot N _ { \mathrm { c l s } } )$ time. Practically, $k _ { \mathrm { n e w } }$ is small and can be regarded as a constant factor, resulting in a linear time update of connection costs.

# V. HIERARCHICAL EXPLORATION PLANNING

Instead of adopting greedy exploration strategies or generating conservative maneuvers, we produce global paths to cover the frontiers efficiently and plan safe and agile motions for faster flight. Our planner takes inspiration from the recent hierarchical quadrotor planning paradigm [21, 22, 28], and makes decisi three phases, as shown in Fig.5.

![](images/c14af4897e699c08743e545525a08a88782486f1541247efcd912b87db52d77d.jpg)

# A. Global Exploration Tour Planning

Our exploration planning begins with finding a global tour to cover existent frontier clusters efficiently. Inspired by [3], we formulate it as a variant of the Traveling Salesman Problem (TSP), which computes an open-loop tour starting from the

![](images/1d8dcde2f15dda1aa0c6d47cbfd9eea1692a8bc8f52afd1503ec4740932949c9.jpg)  
Fig. 5. Generating exploration motion in three coarse-to-fine steps: (1) the shortest tour covering frontier clusters in the entire environment is found. (2) a local segment of the global tour is refined. (3) a safe minimum-time trajectory is generated to the first viewpoint on the refined tour.

current viewpoint and passing viewpoints at all clusters. We reduce this variant to a standard Asymmetric TSP (ATSP) that can be solved quickly by available algorithms, by properly designing the engaged cost matrix $\mathbf { M } _ { \mathrm { t s p } }$ .

Assume there are $N _ { \mathrm { c l s } }$ clusters totally, $\mathbf { M } _ { \mathrm { t s p } }$ corresponds to a $N _ { \mathrm { c l s } } + 1$ dimensions square matrix. The major part is the $N _ { \mathrm { c l s } } \times N _ { \mathrm { c l s } }$ block composed of the connection cost between each pair of frontier clusters, which is computed as:

$$
\begin{array}{l} \mathbf {M} _ {\mathrm {t s p}} \left(k _ {1}, k _ {2}\right) = \mathbf {M} _ {\mathrm {t s p}} \left(k _ {2}, k _ {1}\right) \tag {2} \\ = t _ {\mathrm {l b}} \left(\mathbf {x} _ {k _ {1}, 1}, \mathbf {x} _ {k _ {2}, 1}\right), k _ {1}, k _ {2} \in \{1, 2, \dots , N _ {\mathrm {c l s}} \} \\ \end{array}
$$

As mentioned in Sect.IV-C, this information is maintained when frontiers are detected. Thus, the $N _ { \mathrm { c l s } } \times N _ { \mathrm { c l s } }$ block can be filled without extra overhead.

The first row and column of $\mathbf { M } _ { \mathrm { t s p } }$ are associated with the current viewpoint $\mathbf { x } _ { 0 } ~ = ~ ( \mathbf { p } _ { 0 } , \xi _ { 0 } )$ and $N _ { \mathrm { c l s } }$ clusters. Starting from $\mathbf { x } _ { 0 } ,$ the cost to the k-th cluster is evaluated by:

$$
\begin{array}{l} \mathbf {M} _ {\mathrm {t s p}} (0, k) = t _ {\mathrm {l b}} \left(\mathbf {x} _ {0}, \mathbf {x} _ {k, 1}\right) + w _ {\mathrm {c}} \cdot c _ {\mathrm {c}} \left(\mathbf {x} _ {k, 1}\right), \tag {3} \\ k \in \{1, 2, \dots , N _ {\mathrm {c l s}} \} \\ \end{array}
$$

here a motion consistency cost $c _ { \mathrm { c } } ( \mathbf x _ { k , 1 } )$ is introduced, which is generally computed as:

$$
c _ {\mathrm {c}} \left(\mathbf {x} _ {k, j}\right) = \cos^ {- 1} \frac {\left(\mathbf {p} _ {k , j} - \mathbf {p} _ {0}\right) \cdot \mathbf {v} _ {0}}{\left\| \mathbf {p} _ {k , j} - \mathbf {p} _ {0} \right\| \left\| \mathbf {v} _ {0} \right\|} \tag {4}
$$

where $\mathbf { v } _ { 0 }$ is the current velocity. In some cases, multiple tours have comparable time lower bound, so back-and-forth maneuvers may be generated in successive planning steps and slow down the progress. We eliminate this inconsistency with $c _ { \mathrm { c } } ( \mathbf x _ { k , 1 } )$ , which penalizes large changes in flight direction.

Our problem is different from standard TSP whose solution is a closed-loop tour. However, we can reduce it to an ATSP by assigning zero connection costs from other clusters to the current viewpoint:

$$
\mathbf {M} _ {\mathrm {t s p}} (k, 0) = 0, k \in \{0, 1, 2, \dots , N _ {\mathrm {c l s}} \} \tag {5}
$$

In this way, going back to the current viewpoint in any closedloop tours contributes no extra cost, so each closed-loop tour always contains an open-loop one with an identical cost. As a result, we can obtain the optimal open-loop tour by finding the optimal closed-loop one and retrieving its equal-cost openloop tour.

![](images/ae1e5d59521cce9dd756b2e5a6804af93cc6dee03a84e1ae8dd530495e8ceea1.jpg)  
Fig. 6. Refining viewpoints locally using the graph search approach. Along a truncated segment of the global tour, multiple viewpoints of each visited cluster are considered to select the optimal set of viewpoints.

# B. Local Viewpoint Refinement

The global tour planning finds a promising order to visit all clusters. Nonetheless, it involves only a single viewpoint of each cluster, which are not necessarily the best combination among all viewpoints.

To this end, a richer set of viewpoints on a truncated segment of the global tour are considered to further improve the exploration rate, by using a graph search approach, as depicted in Fig.6. We found consecutive clusters whose viewpoints on the global tour are closer than $R _ { \mathrm { r f } }$ to the current position. To simplify the notation, suppose that $F _ { i } , 1 ~ \le ~ i ~ \le ~ N _ { \mathrm { r f } }$ are the considered clusters. We create graph nodes for their viewpoints $V P _ { i }$ and the current viewpoint $\mathbf { x } _ { 0 } .$ . Then each node is connected to other nodes associated with the next cluster with a directed edge, which compose a directed acyclic graph capturing possible variation of the truncated tour. We utilize the Dijkstra algorithm to search for the optimal local tour $\Xi = \left\{ \mathbf { x } _ { 1 , j _ { 1 } } , \mathbf { x } _ { 2 , j _ { 2 } } , \cdot \cdot \cdot , \mathbf { x } _ { N _ { \mathrm { f } } , j _ { N _ { \mathrm { f } } } } \right\}$ that minimizes the cost:

$$
\begin{array}{l} c _ {\mathrm {r f}} (\Xi) = t _ {\mathrm {l b}} \left(\mathbf {x} _ {0}, \mathbf {x} _ {1, j _ {1}}\right) + w _ {\mathrm {c}} \cdot c _ {\mathrm {c}} \left(\mathbf {x} _ {1, j _ {1}}\right) \tag {6} \\ + t _ {\mathrm {l b}} \left(\mathbf {x} _ {N _ {\mathrm {r f}}, j _ {N _ {\mathrm {r f}}}}, \mathbf {x} _ {N _ {\mathrm {r f}} + 1, 1}\right) + \sum_ {k = 1} ^ {N _ {\mathrm {r f}} - 1} t _ {\mathrm {l b}} \left(\mathbf {x} _ {k, j _ {k}}, \mathbf {x} _ {k + 1, j _ {k + 1}}\right) \\ \end{array}
$$

which also consists of time lower bounds and motion consistency. Note that it is straight forward to incorporate information gain [4, 12] to Equ.6, however, evaluating information gain for numerous viewpoints is expensive. Practically, we find that simply adopting viewpoints based on their coverages is much faster and leads to consistently satisfactory results.

# C. Minimum-time B-spline Trajectory

Given the discrete viewpoints, continuous trajectories are required for smooth navigation. Our quadrotor trajectory planning is based on a method [28] that generates smooth, safe and dynamically feasible B-spline trajectories. We go one step further to optimize all parameters of B-splines, so that the total trajectory time is minimized to enable the quadrotor to fully utilize its dynamic capability.

As the quadrotor dynamics are differentially flat [19], we plan trajectories for the flat outputs $\mathbf { x } \in ( x , y , z , \xi )$ . Let $\mathbf { X } _ { \mathrm { c b } } = \mathbf { \rho }$ $\left\{ \mathbf { x } _ { \mathrm { c } , 0 } , \mathbf { x } _ { \mathrm { c } , 1 } , \cdots , \mathbf { x } _ { \mathrm { c } , N _ { b } } \right\}$ where $\mathbf { x } _ { \mathrm { c } , i } = ( \mathbf { p } _ { \mathrm { c } , i } , \xi _ { \mathrm { c } , i } )$ be the $N _ { b } + 1$ control points of a $p _ { b }$ degree uniform B-spline, and $\Delta t _ { b }$ be the knot span. We find the B-spline that trades-off smoothness and total trajectory time, and satisfies safety, dynamic feasibility

and boundary state constraints. It can be formulated as an following optimization problem:

$$
\underset {\mathbf {X} _ {c, b}, \Delta t _ {b}} {\arg \min } f _ {\mathrm {s}} + w _ {\mathrm {t}} T + \lambda_ {\mathrm {c}} f _ {c} + \lambda_ {\mathrm {d}} \left(f _ {\mathrm {v}} + f _ {\mathrm {a}}\right) + \lambda_ {\mathrm {b s}} f _ {\mathrm {b s}} \tag {7}
$$

Similar to [28], $f _ { \mathrm { s } }$ is the elastic band smoothness cost:

$$
f _ {\mathrm {s}} = \sum_ {i = 0} ^ {N _ {b} - 2} \mathbf {s} _ {i} ^ {\mathrm {T}} \mathbf {R} _ {\mathrm {s}} \mathbf {s} _ {i}, \mathbf {s} _ {i} = \mathbf {x} _ {\mathrm {c}, i + 2} - 2 \mathbf {x} _ {\mathrm {c}, i + 1} + \mathbf {x} _ {\mathrm {c}, i} \tag {8}
$$

in which $\mathbf { R } _ { \mathrm { s } }$ is the penalty matrix:

$$
\mathbf {R} _ {\mathrm {s}} = \left[ \begin{array}{c c} w _ {\mathrm {s}, \mathrm {p}} \mathbf {I} _ {3} & \mathbf {0} \\ \mathbf {0} ^ {\mathrm {T}} & w _ {\mathrm {s}, \xi} \end{array} \right] \tag {9}
$$

$T$ is the total trajectory time depending on $\Delta t _ { b }$ and the number of B-spline segments:

$$
T = \left(N _ {b} + 1 - p _ {b}\right) \cdot \Delta t _ {b} \tag {10}
$$

$f _ { \mathrm { c } } , \ f _ { \mathrm { v } }$ and $f _ { \mathrm { a } }$ are the penalties to ensure safety and dynamic feasibility. Given the following function:

$$
\mathcal {P} \left(\tau_ {1}, \tau_ {2}\right) = \left\{ \begin{array}{c c} \left(\tau_ {1} - \tau_ {2}\right) ^ {2} & \tau_ {1} \leq \tau_ {2} \\ 0 & \text {e l s e} \end{array} \right. \tag {11}
$$

$f _ { \mathrm { c } }$ is evaluated as:

$$
f _ {\mathrm {c}} = \sum_ {i = 0} ^ {N _ {b}} \mathcal {P} \left(d \left(\mathbf {p} _ {\mathrm {c}, i}\right), d _ {\min }\right) \tag {12}
$$

where $d ( \mathbf { p } _ { \mathbf { c } , i } )$ is the distance of point $\mathbf { p } _ { \mathrm { c } , i }$ to the nearest obstacle, which can be obtained from the Euclidean signed distance field (ESDF) maintained by the mapping module. Practically a clearance larger than our quadrotor’s radius (typically $d _ { \operatorname* { m i n } } \ge 0 . 5 ~ \mathrm { m } )$ ensures safety in complex scenes. $f _ { \mathrm { v } }$ and $f _ { \mathrm { a } }$ penalize infeasible velocity and acceleration:

$$
f _ {\mathrm {v}} = \sum_ {i = 0} ^ {N _ {b} - 1} \left\{\sum_ {\mu \in \{x, y, z \}} \mathcal {P} \left(v _ {\max }, \left| \dot {p} _ {\mathrm {c}, i, \mu} \right|\right) + \mathcal {P} \left(\dot {\xi} _ {\max }, \left| \dot {\xi} _ {\mathrm {c}, i} \right|\right) \right\} \tag {13}
$$

$$
f _ {\mathrm {a}} = \sum_ {i = 0} ^ {N _ {b} - 2} \left\{\sum_ {\mu \in \{x, y, z \}} \mathcal {P} \left(a _ {\max }, \left| \ddot {p} _ {\mathrm {c}, i, \mu} \right|\right) + \mathcal {P} \left(\ddot {\xi} _ {\max }, \left| \ddot {\xi} _ {\mathrm {c}, i} \right|\right) \right\} \tag {14}
$$

in which the control points of derivatives are utilized:

$$
\dot {\mathbf {x}} _ {\mathrm {c}, i} = \left[ \dot {p} _ {\mathrm {c}, i, x}, \dot {p} _ {\mathrm {c}, i, y}, \dot {p} _ {\mathrm {c}, i, z}, \dot {\xi} _ {\mathrm {c}, i} \right] ^ {\mathrm {T}} = \frac {\mathbf {x} _ {\mathrm {c} , i + 1} - \mathbf {x} _ {\mathrm {c} , i}}{\Delta t _ {b}} \tag {15}
$$

$$
\ddot {\mathbf {x}} _ {\mathrm {c}, i} = \left[ \ddot {p} _ {\mathrm {c}, i, x}, \ddot {p} _ {\mathrm {c}, i, y}, \ddot {p} _ {\mathrm {c}, i, z}, \ddot {\xi} _ {\mathrm {c}, i} \right] ^ {\mathrm {T}} = \frac {\mathbf {x} _ {\mathrm {c} , i + 2} - 2 \mathbf {x} _ {\mathrm {c} , i + 1} + \mathbf {x} _ {\mathrm {c} , i}}{\Delta t _ {b} ^ {2}} \tag {16}
$$

In Equ.12, 13 and $^ { 1 4 , }$ the convex hull property of B-spline is utilized to ensure the feasibility efficiently. For brevity we refer the reader to [28] for more details.

Lastly, we set the 0th to 2nd order derivatives at the start to the instantaneous state $\left( \mathbf { x } _ { 0 } , \dot { \mathbf { x } } _ { 0 } , \ddot { \mathbf { x } } _ { 0 } \right)$ for smooth motion. The 0-th order derivative at the end is also determined by the

![](images/0679b6afc7531a0b1d5c64d63ead82fb61f2b1dbc1be6df8773c78ec3bed9182.jpg)  
Fig. 7. Benchmark comparison of the proposed method, classic frontier method [7], rapid frontier method [1] and NBVP [12] in a 3D space containing a bridge. The overall exploration paths are shown as blue, red, green and pink respectively.

TABLE II EXPLORATION STATISTIC IN THE BRIDGE AND LARGE MAZE SCENARIOS.   

<table><tr><td rowspan="2">Scene</td><td rowspan="2">Method</td><td colspan="4">Exploration time (s)</td><td colspan="4">Flight distance (m)</td></tr><tr><td>Avg</td><td>Std</td><td>Max</td><td>Min</td><td>Avg</td><td>Std</td><td>Max</td><td>Min</td></tr><tr><td rowspan="4">Bridge</td><td>Classic [7]</td><td>575</td><td>53</td><td>643</td><td>511</td><td>250</td><td>42</td><td>285</td><td>190</td></tr><tr><td>Rapid [1]</td><td>288</td><td>15</td><td>305</td><td>264</td><td>286</td><td>13</td><td>303</td><td>269</td></tr><tr><td>NBVP [12]</td><td>857</td><td>117</td><td>1018</td><td>740</td><td>322</td><td>47</td><td>377</td><td>261</td></tr><tr><td>Proposed</td><td>104</td><td>1.5</td><td>105</td><td>102</td><td>165</td><td>3.8</td><td>170</td><td>161</td></tr><tr><td rowspan="4">Large Maze</td><td>Classic [7]</td><td>814</td><td>104</td><td>961</td><td>721</td><td>419</td><td>63</td><td>509</td><td>373</td></tr><tr><td>Rapid [1]</td><td>669</td><td>68</td><td>766</td><td>613</td><td>469</td><td>32</td><td>514</td><td>440</td></tr><tr><td>NBVP [12]</td><td>1037</td><td>152</td><td>1253</td><td>925</td><td>1539</td><td>262</td><td>1898</td><td>1279</td></tr><tr><td>Proposed</td><td>168</td><td>16</td><td>192</td><td>156</td><td>280</td><td>20</td><td>310</td><td>264</td></tr></table>

viewpoint $\mathbf { x } _ { \mathrm { n e x t } }$ to be visited. In implementation we use cubic B-splines, so the associated cost is:

$$
\begin{array}{l} f _ {\mathrm {b s}} = \left\| \frac {\mathbf {x} _ {\mathrm {c} , 0} + 4 \mathbf {x} _ {\mathrm {c} , 1} + \mathbf {x} _ {\mathrm {c} , 2}}{6} - \mathbf {x} _ {0} \right\| ^ {2} + \left\| \frac {\dot {\mathbf {x}} _ {\mathrm {c} , 0} + \dot {\mathbf {x}} _ {\mathrm {c} , 1}}{2} - \dot {\mathbf {x}} _ {0} \right\| ^ {2} \tag {17} \\ + \left\| \ddot {\mathbf {x}} _ {\mathrm {c}, 0} - \ddot {\mathbf {x}} _ {0} \right\| ^ {2} + \left\| \frac {\mathbf {x} _ {\mathrm {c} , N _ {b} - 2} + 4 \mathbf {x} _ {\mathrm {c} , N _ {b} - 1} + \mathbf {x} _ {\mathrm {c} , N _ {b}}}{6} - \mathbf {x} _ {\mathrm {n e x t}} \right\| ^ {2} \\ \end{array}
$$

# VI. RESULTS

# A. Implementation Details

We set $w _ { \mathrm { c } } = 1 . 5$ in Equ.3 and 6. In global tour planning, the ATSP is solved using a Lin-Kernighan-Helsgaun heuristic solver [33]. In local viewpoint refinement, we reserve at most $N _ { \mathrm { v i e w } } = 1 5$ viewpoints in each FIS and truncate the global tour within radius $R _ { \mathrm { r f } } = 5 . 0$ . For trajectory optimization, we use $w _ { \mathrm { s , p } } = 5 . 0 , w _ { \mathrm { s , \xi } } = 2 . 5 , w _ { \mathrm { t } } = 1 . 0 , \lambda _ { \mathrm { c } } = \lambda _ { \mathrm { b s } } = 1 0 . 0 , \lambda _ { \mathrm { d } } = 2 . 0$ and $d _ { \operatorname* { m i n } } = 0 . 4$ and solve the problem with a general nonlinear optimization solver $\mathrm { N L o p t } ^ { 2 }$ . Cubic B-spline $( p _ { b } = 3 )$ is used as the trajectory representation.

To achieve fast exploration, an efficient mapping framework is essential. In our work, we utilize a volumetric map [34], which has been successfully applied to fast autonomous flights [28, 30] in complex scenes. Similar to [35], which is widely applied in exploration, [34] builds an occupancy grid representation of the space. Meanwhile it also maintains an ESDF incrementally to facilitate the trajectory planning. For brevity we refer interested readers to [34] for more details about our mapping framework.

2https://nlopt.readthedocs.io/en/latest/

![](images/52b01b58780b0c70154cf7e71f56051de4e8d7c26fb2854cd4fd1b2b580518cb.jpg)

![](images/b18b16328c4b5aaafdd71c156dab49bdfdadd079ab2d25d653de3ebac4e6fa80.jpg)  
Fig. 8. The exploration progress of four methods in the bridge (top) and large maze (bottom) scenarios.

TABLE III AVERAGE COMPUTATION TIME OF EACH PROPOSED COMPONENT.   

<table><tr><td rowspan="3">Scene</td><td colspan="6">Average computation time (ms)</td></tr><tr><td>Frontier</td><td>View.+Cost</td><td>Global</td><td>Local</td><td>Traj.</td><td rowspan="2">Total</td></tr><tr><td>Sect.IV-B</td><td>Sect.IV-C</td><td>Sect.V-A</td><td>Sect.V-B</td><td>Sect.V-C</td></tr><tr><td>Bridge</td><td>4.69</td><td>4.86+5.16</td><td>1.12</td><td>4.10</td><td>4.23</td><td>24.17</td></tr><tr><td>Maze</td><td>5.21</td><td>6.06+10.97</td><td>3.53</td><td>4.98</td><td>5.47</td><td>36.23</td></tr></table>

In all field experiments, we localize the quadrotor by a visual-inertial state estimator [36]. We use a geometric controller [37] for tracking control of the $( x , y , z , \xi )$ trajectory. We equipped our customized quadrotor platform with an Intel RealSense Depth Camera D435i. All the above modules run on an Intel Core i7-8550U CPU.

# B. Benchmark and Analysis

We test our proposed framework in simulation. We benchmark it in a bridge scenario and a large maze scenario. Three methods are compared: the NBVP [12], the classic frontier method [7] and the rapid frontier method [1]. Note that no open source code is available for [1], so we use our implementation. In all tests the dynamic limits are set as $v _ { \mathrm { m a x } } ~ = ~ 2 . 0$ m/s and $\xi _ { \mathrm { m a x } } ^ { \cdot } \ = \ 0 . 9$ rad/s for all methods. The FOVs of the sensors are set as $[ 8 0 \times 6 0 ]$ deg with a maximum range of 4.5 m. In both scenarios each method is run for 3 times with the same initial configuration. Statistics and exploration progresses of the four methods are shown in Tab.II and 8 respectively. The computation time of each component of our method is listed in Tab.III.

1) Bridge Scenario: Firstly, we compare the four methods in a $1 0 \times 2 0 \times 5 ~ \mathrm { m ^ { 3 } }$ space containing a bridge, as shown in Fig.7. The result indicates that we achieve much shorter exploration time and smaller time variance. The overall exploration path of our method is significantly shorter, primarily because we plan tours globally. The executed path is smoother, since we refine motions locally and generate smooth trajectories. Also, we are able to navigate at a higher flight speed, owing to the minimum-time trajectory planning.

![](images/35317ac857a34f6726091bdfee3b8efa2f4c82292894801777683184e02fdb58.jpg)

![](images/e6db58dd02b75a55cda9893ba7dd8a23a3c642ede1048867a8b849743b69c857.jpg)  
Fig. 9. Path generated by the proposed method (blue), classic frontier method [7](red), rapid frontier method [1] (green) and NBVP [12](pink).

![](images/fdb91d9c45b925029c8390818d6a5f65e72b574ba37334a6f1ad51fb6ac42096.jpg)

![](images/f0e927620050229cfea243680f72eadf309b2fb0e634aa92c2d0c4abc230c771.jpg)

![](images/58add933557b80d3e23073b15c377e75eafe0a680c427ed3d2d4ded3aa0752cf.jpg)  
Fig. 10. Experiments in an indoor scene composed of two room: a small one with tables and chairs (top left), a large room cluttered with obstacles (top right).

2) Large Maze Scenario: We also compare the methods quantitatively in a large maze environment shown in Fig.9. The explored space is $\mathrm { 2 0 \times 8 0 \times 3 \ m ^ { 3 } }$ large. In this scenario, all the benchmarked methods take a long time to reach full coverage, due to the complexity of the scene. In contrast, our method completes the exploration 4+ times faster on average. Path executed by the four methods after completion are displayed in Fig.9. Noticeably, our method explores the maze in a more sensible order, without revisiting the same place frequently. In consequence, it produces a much shorter coverage path and an approximately linear exploration rate (Fig.8). This behavior is owing to the global plan, without which known regions may be revisited many times and slow down the progress, as the benchmarked methods do. Also note that the computation time in the large maze is longer, mostly due to the larger scene, which naturally involves a greater number of frontier clusters.

# C. Field Exploration Tests

To further validate the proposed method, we conduct extensive field experiments in both indoor and outdoor environ-

![](images/65c578feea2c71bf8f1461debe40cc4cd761e25027fd61e57e084d157793d333.jpg)

![](images/151d00b8ff8a01a83f1153bfbf8da8979cf961baca664ef8aa12c07542370f7a.jpg)  
Fig. 11. Exploration experiment conducted in a forest.

ments. In all tests we set the dynamics limits as $v _ { \mathrm { m a x } } = 1 . 5$ m/s, $a _ { \mathrm { m a x } } = 0 . 8$ m/s and $\dot { \xi } _ { \mathrm { m a x } } = 0 . 9$ rad/s. Note that we do not use any external device for localization and only rely on the onboard state estimator.

First, we present fast exploration tests in two indoor scenes. The first scene is shown in Fig.1, within which we deploy dozens of obstacles and the quadrotor should perform 3D maneuvers to map the unknown space and avoid obstacles simultaneously. We bound the space to be explored with a $\mathrm { 1 0 \times 6 \times 2 \ m ^ { 3 } }$ box. One sample map and the flight trajectory is presented in Fig.1. The second indoor scene is a larger environment including two rooms, where one room is similar to scene 1 and the other is a part of an office containing tables and chairs. The space is bounded by a $\mathrm { 1 5 \times 1 1 \times 2 \ m ^ { 3 } }$ box. The quadrotor starts by exploring the large room, after which it proceeds to the small one. The second scene, the online generated map and trajectory are shown in Fig.10. Note that in the two scenes the quadrotor starts out at a spot with low visibility, so it only maps a small region of the environment at the beginning. Finally, to validate our method in natural environments, we conduct exploration tests in a forest. The size of the area to explore is $1 1 \times 1 0 \times 2 ~ \mathrm { m ^ { 3 } }$ . The experiment environment and the associated results are displayed Fig.11.

The above experiments demonstrate the capability of our method in complex real-world scenarios. They also show the merits of our autonomous quadrotor system, among which the state estimation [36] and mapping modules [34] are also crucial to fullfil the real-world tasks. Video demonstration of all experiments is available (Fig.1), we refer the readers to it for more details.

# VII. CONCLUSIONS

In this paper, we propose a hierarchical framework for rapid autonomous quadrotor exploration. An incrementally maintained FIS is introduced to provide the exploration planning with essential information. Based on FIS, a hierarchical

planner plans exploration motions in three sequential steps, which finds efficient global tours, selects a local set of optimal viewpoints, and generates minimum-time local trajectories. The method makes decisions at high frequency to respond quickly to environmental changes. Both benchmark and realworld tests show the competence of our method.

One limitation of our method is assuming perfect state estimation, as most methods do. We evaluate our method in simulation with ground truth localization, while drifts in pose are not considered. However, error in state estimation exists generally and can not be ignored. In the future we plan to consider the state estimation uncertainty in our method and evaluate its performance under pose drifts.

# REFERENCES

[1] T. Cieslewski, E. Kaufmann, and D. Scaramuzza, “Rapid exploration with multi-rotors: A frontier selection method for high speed flight,” in Proc. of the IEEE/RSJ Intl. Conf. on Intell. Robots and Syst.(IROS). IEEE, 2017, pp. 2135–2142.   
[2] L. Schmid, M. Pantic, R. Khanna, L. Ott, R. Siegwart, and J. Nieto, “An efficient sampling-based method for online informative path planning in unknown environments,” IEEE Robotics and Automation Letters, vol. 5, no. 2, pp. 1500–1507, 2020.   
[3] Z. Meng, H. Qin, Z. Chen, X. Chen, H. Sun, F. Lin, and M. H. Ang Jr, “A two-stage optimized next-view planning framework for 3-d unknown environment exploration, and structural reconstruction,” IEEE Robotics and Automation Letters, vol. 2, no. 3, pp. 1680–1687, 2017.   
[4] M. Selin, M. Tiger, D. Duberg, F. Heintz, and P. Jensfelt, “Efficient autonomous exploration planning of large-scale 3-d environments,” IEEE Robotics and Automation Letters, vol. 4, no. 2, pp. 1699–1706, 2019.   
[5] M. Dharmadhikari, T. Dang, L. Solanka, J. Loje, H. Nguyen, N. Khedekar, and K. Alexis, “Motion primitives-based path planning for fast and agile exploration using aerial robots,” in Proc. of the IEEE Intl. Conf. on Robot. and Autom. (ICRA). IEEE, 2020, pp. 179–185.   
[6] S. Song and S. Jo, “Online inspection path planning for autonomous 3d modeling using a micro-aerial vehicle.” in Proc. of the IEEE Intl. Conf. on Robot. and Autom. (ICRA), 2017, pp. 6217–6224.   
[7] B. Yamauchi, “A frontier-based approach for autonomous exploration,” in Proceedings 1997 IEEE International Symposium on Computational Intelligence in Robotics and Automation CIRA’97.’Towards New Computational Principles for Robotics and Automation’. IEEE, 1997, pp. 146–151.   
[8] M. Julia, A. Gil, and O. Reinoso, “A comparison of path planning ´ strategies for autonomous exploration and mapping of unknown environments,” Auton. Robots, vol. 33, no. 4, pp. 427–444, 2012.   
[9] S. Shen, N. Michael, and V. Kumar, “Stochastic differential equationbased exploration algorithm for autonomous indoor 3d exploration with a micro-aerial vehicle,” Intl. J. Robot. Research (IJRR), vol. 31, no. 12, pp. 1431–1444, 2012.   
[10] D. Deng, R. Duan, J. Liu, K. Sheng, and K. Shimada, “Robotic exploration of unknown 2d environment using a frontier-based automaticdifferentiable information gain measure,” in 2020 IEEE/ASME International Conference on Advanced Intelligent Mechatronics (AIM). IEEE, 2020, pp. 1497–1503.   
[11] C. Connolly, “The determination of next best views,” in Proc. of the IEEE Intl. Conf. on Robot. and Autom. (ICRA), vol. 2. IEEE, 1985, pp. 432–435.   
[12] A. Bircher, M. Kamel, K. Alexis, H. Oleynikova, and R. Siegwart, “Receding horizon” next-best-view” planner for 3d exploration,” in Proc. of the IEEE Intl. Conf. on Robot. and Autom. (ICRA). IEEE, 2016, pp. 1462–1468.   
[13] C. Papachristos, S. Khattak, and K. Alexis, “Uncertainty-aware receding horizon exploration and mapping using aerial robots,” in 2017 IEEE international conference on robotics and automation (ICRA). IEEE, 2017, pp. 4568–4575.   
[14] T. Dang, C. Papachristos, and K. Alexis, “Visual saliency-aware receding horizon autonomous exploration with application to aerial robotics,” in 2018 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2018, pp. 2526–2533.

[15] A. Bircher, M. Kamel, K. Alexis, H. Oleynikova, and R. Siegwart, “Receding horizon path planning for 3d exploration and surface inspection,” Auton. Robots, vol. 42, no. 2, pp. 291–306, 2018.   
[16] C. Witting, M. Fehr, R. Bahnemann, H. Oleynikova, and R. Siegwart, ¨ “History-aware autonomous exploration in confined environments using mavs,” in 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). IEEE, 2018, pp. 1–9.   
[17] C. Wang, D. Zhu, T. Li, M. Q.-H. Meng, and C. W. de Silva, “Efficient autonomous robotic exploration with semantic road map in indoor environments,” IEEE Robotics and Automation Letters, vol. 4, no. 3, pp. 2989–2996, 2019.   
[18] B. Charrow, G. Kahn, S. Patil, S. Liu, K. Goldberg, P. Abbeel, N. Michael, and V. Kumar, “Information-theoretic planning with trajectory optimization for dense 3d mapping.” in Proc. of Robot.: Sci. and Syst. (RSS), vol. 11, 2015.   
[19] D. Mellinger and V. Kumar, “Minimum snap trajectory generation and control for quadrotors,” in Proc. of the IEEE Intl. Conf. on Robot. and Autom. (ICRA), Shanghai, China, May 2011, pp. 2520–2525.   
[20] C. Richter, A. Bry, and N. Roy, “Polynomial trajectory planning for aggressive quadrotor flight in dense indoor environments,” in Proc. of the Intl. Sym. of Robot. Research (ISRR), Dec. 2013, pp. 649–666.   
[21] J. Chen, T. Liu, and S. Shen, “Online generation of collision-free trajectories for quadrotor flight in unknown cluttered environments,” in Proc. of the IEEE Intl. Conf. on Robot. and Autom. (ICRA), Stockholm, Sweden, May 2016, pp. 1476–1483.   
[22] F. Gao, W. Wu, Y. Lin, and S. Shen, “Online safe trajectory generation for quadrotors using fast marching method and bernstein basis polynomial,” in Proc. of the IEEE Intl. Conf. on Robot. and Autom. (ICRA), Brisbane, Australia, May 2018.   
[23] W. Ding, W. Gao, K. Wang, and S. Shen, “An efficient b-spline-based kinodynamic replanning framework for quadrotors,” IEEE Transactions on Robotics, vol. 35, no. 6, pp. 1287–1306, 2019.   
[24] J. Tordesillas, B. T. Lopez, and J. P. How, “FASTER: Fast and safe trajectory planner for flights in unknown environments,” in Proc. of the IEEE/RSJ Intl. Conf. on Intell. Robots and Syst.(IROS). IEEE, 2019.   
[25] H. Oleynikova, M. Burri, Z. Taylor, J. Nieto, R. Siegwart, and E. Galceran, “Continuous-time trajectory optimization for online uav replanning,” in Proc. of the IEEE/RSJ Intl. Conf. on Intell. Robots and Syst.(IROS), Daejeon, Korea, Oct. 2016, pp. 5332–5339.   
[26] F. Gao, Y. Lin, and S. Shen, “Gradient-based online safe trajectory generation for quadrotor flight in complex environments,” in Proc. of the IEEE/RSJ Intl. Conf. on Intell. Robots and Syst.(IROS), Sept 2017, pp. 3681–3688.   
[27] V. Usenko, L. von Stumberg, A. Pangercic, and D. Cremers, “Realtime trajectory replanning for mavs using uniform b-splines and a 3d circular buffer,” in Proc. of the IEEE/RSJ Intl. Conf. on Intell. Robots and Syst.(IROS). IEEE, 2017, pp. 215–222.   
[28] B. Zhou, F. Gao, L. Wang, C. Liu, and S. Shen, “Robust and efficient quadrotor trajectory generation for fast autonomous flight,” IEEE Robotics and Automation Letters, vol. 4, no. 4, pp. 3529–3536, 2019.   
[29] B. Zhou, F. Gao, J. Pan, and S. Shen, “Robust real-time uav replanning using guided gradient-based optimization and topological paths,” in Proc. of the IEEE Intl. Conf. on Robot. and Autom. (ICRA). IEEE, 2020, pp. 1208–1214.   
[30] B. Zhou, J. Pan, F. Gao, and S. Shen, “Raptor: Robust and perceptionaware trajectory replanning for quadrotor fast flight,” arXiv preprint arXiv:2007.03465, 2020.   
[31] N. Ratliff, M. Zucker, J. A. Bagnell, and S. Srinivasa, “Chomp: Gradient optimization techniques for efficient motion planning,” in Proc. of the IEEE Intl. Conf. on Robot. and Autom. (ICRA), May 2009, pp. 489–494.   
[32] C. Ericson, Real-time collision detection. CRC Press, 2004.   
[33] K. Helsgaun, “An effective implementation of the lin–kernighan traveling salesman heuristic,” European Journal of Operational Research, vol. 126, no. 1, pp. 106–130, 2000.   
[34] L. Han, F. Gao, B. Zhou, and S. Shen, “Fiesta: Fast incremental euclidean distance fields for online motion planning of aerial robots,” arXiv preprint arXiv:1903.02144, 2019.   
[35] K. M. Wurm, A. Hornung, M. Bennewitz, C. Stachniss, and W. Burgard, “Octomap: A probabilistic, flexible, and compact 3d map representation for robotic systems,” in Proc. of the IEEE Intl. Conf. on Robot. and Autom. (ICRA), vol. 2, Anchorage, AK, US, May 2010.   
[36] T. Qin, P. Li, and S. Shen, “Vins-mono: A robust and versatile monocular visual-inertial state estimator,” IEEE Trans. Robot. (TRO), vol. 34, no. 4, pp. 1004–1020, 2018.   
[37] T. Lee, M. Leoky, and N. H. McClamroch, “Geometric tracking control of a quadrotor uav on se (3),” in Proc. of the IEEE Control and Decision Conf. (CDC), Atlanta, GA, Dec. 2010, pp. 5420–5425.