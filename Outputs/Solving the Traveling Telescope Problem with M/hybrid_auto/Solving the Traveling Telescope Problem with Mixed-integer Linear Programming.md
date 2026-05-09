---
title: "Solving the Traveling Telescope Problem with Mixed-integer Linear Programming"
authors:
  - "Luke B. Handley"
  - "Erik A. Petigura"
  - "Velibor V. Mišić"
date: "2024-01-01"
year: 2024
journal: "The Astronomical Journal"
abstract: "The size and complexity of modern astronomical surveys has grown to the point where, in many cases, traditional human scheduling of observations are tedious at best and impractical at worst. Automated scheduling algorithms present an opportunity to save human effort and increase scientific productivity. A common scheduling challenge involves determining the optimal ordering of a set of targets over a night subject to timing constraints and time-dependent slew overheads. We present a solution to the traveling telescope problem that uses mixed-integer linear programming. This algorithm is fast enough to enable dynamic schedule generation in many astronomical contexts. It can determine the optimal solution for 100 observations within 10 minutes on a modern workstation, reducing slew overheads by a factor of 5 compared to random ordering. We also provide a heuristic method that can return a near-optimal solution at significantly reduced computational cost. As a case study, we explore our algorithm's suitability to automatic schedule generation for Doppler planet searches."
abstract_cn: “现代天文巡天的规模和复杂性已增长到传统人工观测调度繁琐甚至不可行的程度。本文提出使用混合整数线性规划求解旅行望远镜问题，算法可在现代工作站上10分钟内确定100次观测的最优解，相比随机排序将转动开销降低5倍。还提供一种启发式方法以显著降低的计算成本返回接近最优解，并以多普勒行星搜索为案例研究探讨了该算法在自动调度中的适用性。”
keywords:
  - "[[Mixed-integer linear programming]]"
  - "[[Telescope scheduling]]"
  - "[[Combinatorial optimization]]"
cite: "[1] Handley L B, Petigura E A, Mišić V V. Solving the traveling telescope problem"
aiSum: "混合整数线性规划求解旅行望远镜问题：10分钟内优化100次观测序列，转动开销降低5倍，适用于多普勒行星搜索等自动调度场景。"
confidence: "medium"
---

# Solving the Traveling Telescope Problem with Mixed-integer Linear Programming

Luke B. Handley1 , Erik A. Petigura1 , and Velibor V. Mišić2

1 Department of Physics & Astronomy, University of California Los Angeles, Los Angeles, CA 90095, USA

2 Decisions, Operations and Technology Management, Anderson School of Management, University of California Los Angeles, Los Angeles, CA 90095, USA

Received 2023 October 10; revised 2023 November 15; accepted 2023 November 16; published 2023 December 22

# Abstract

The size and complexity of modern astronomical surveys has grown to the point where, in many cases, traditional human scheduling of observations are tedious at best and impractical at worst. Automated scheduling algorithms present an opportunity to save human effort and increase scientific productivity. A common scheduling challenge involves determining the optimal ordering of a set of targets over a night subject to timing constraints and timedependent slew overheads. We present a solution to the “traveling telescope problem” that uses mixed-integer linear programming. This algorithm is fast enough to enable dynamic schedule generation in many astronomical contexts. It can determine the optimal solution for 100 observations within 10 minutes on a modern workstation, reducing slew overheads by a factor of 5 compared to random ordering. We also provide a heuristic method that can return a near-optimal solution at significantly reduced computational cost. As a case study, we explore our algorithm’s suitability to automatic schedule generation for Doppler planet searches.

Unified Astronomy Thesaurus concepts: Astronomical methods (1043); Observational astronomy (1145)

# 1. Introduction

Maximizing the scientific yield of expensive and often oversubscribed astronomical instrumentation requires meticulous planning of each night’s observations. However, determining the optimal (or even near-optimal) sequence of observations is a challenging and time-consuming task. Schedulers must incorporate temporal accessibility windows while factoring in slew and acquisition overheads that can themselves be time variable. In this paper, we refer to the task of determining the optimal ordering of a set of observations by a telescope as the “traveling telescope problem” (or TTP) given its similarities to the “traveling salesman problem” (or TSP).

The scientific benefits of intelligently sequenced observations can be significant, especially for programs with many targets spread over the entire sky. As an example, the Doppler planet searches at the Keck I telescope observe up to 100 targets per night (Howard et al. 2010). As we show below, a quasi-random sequence of 100 targets requires over 3 hr of slew during a 10 hr night, while an optimized sequence can reduce this to 0.5 hr.

Automated solutions to the TTP offer a number of opportunities. As is the case for the TSP, a skilled human scheduler can generate an observation sequence that significantly outperforms a random ordering. However, such script generation takes significant human effort that could be devoted elsewhere. In addition, a number of ongoing and forthcoming surveys are or will be scheduled automatically. The Zwicky Transient Facility (ZTF; Bellm et al. 2019b) and the Legacy Survey of Space and Time (Ivezić et al. 2019) are two prominent examples.

A common method to formulate these computationally intensive scheduling problems is through integer linear programming (ILP), which can solve combinatorial problems with thousands or millions of parameters. ILP has seen success

![](images/88282d3bb85b71d492f5c2f8d941a3322692782b05910cef93748a33298e4eef.jpg)  
distribution of of the work, jo

Original content from this work may be used under the terms of the Creative Commons Attribution 4.0 licence. Any further

this work must maintain attribution to the author(s) and the title urnal citation and DOI.

in scheduling systems in astronomy, notably its early use in the Las Cumbres Observatory Global Telescope network scheduler (Lampoudi et al. 2015) and the Atacama Large Millimeter/ submillimeter Array (Solar et al. 2016), which handled the unique scheduling constraint of multiresource allocation. Other modern scheduling systems have often made use of mixedinteger linear programming (MILP) models, where a subset of parameters are not restricted to integer values. Parazin et al. (2022) is one such formulation that expands on the ZTF scheduling algorithm (Bellm et al. 2019a) and deploys a continuous time-variable formulation for multimessenger follow-up of wide field surveys. ILP and MILP methods can make astronomical scheduling computationally tractable.

Automated solutions to the TTP are necessary for many types of automated surveys. While a rich literature exists on the TSP, standard solutions do not directly transfer to the TTP for several reasons. First, targets are often only accessible for a fraction of the night either due to their position on the sky or scientific need for time-critical observations. Thus, a large fraction of the N! target sequences are infeasible. Second, slew time between targets is itself a function of time. As an example, Figure 1 shows the trajectory of two targets above the Keck I telescope atop Maunakea. Two targets cross the meridian north and south of zenith, respectively. Like most large telescopes, Keck I moves in the altitude and azimuth (alt/az) directions, and target slews are dominated by differences in azimuth. Figure 1 shows the variation in slew time over the course of the night, which grows as the targets first approach the meridian and then straddle the telescope's cable-wrap limits.

Previous efforts have addressed the TTP under a number of simplifying assumptions. The ZTF scheduler divides the night into short intervals and solves a standard TSP while treating the set of accessible targets and target-to-target slew times as constant within the interval (Bellm et al. 2019a). The JWST’s scheduling architecture (Giuliano & Johnston 2008), which is built upon the Hubble Space Telescope’s SPIKE software (Johnston & Miller 1994), also treats target-to-target slew times as constant. At present, we are not aware of any global

![](images/0f47d8be71cbbd2dc61beab627e49b0b631bc2c83c978ed7cd16f906c36bc0bd.jpg)

![](images/67c35af655322f41a4380dce4b3b95b7f1d5c3250e120d24958ddc5cfbdad772.jpg)  
Figure 1. Time-dependent slew overheads at Keck Observatory. The left plot shows the motion of two targets in the alt/az frame across the accessible region at Keck Observatory (latitude $= 1 9 . 8 ^ { \circ } \mathrm { N } )$ . The top target sits at $\delta = 4 \dot { 3 } . 8 ^ { \circ }$ , the bottom at $\delta = 1 1 . 7 ^ { \circ }$ . As time progresses, the azimuthal separation dominates the slew and steadily increases to a maximum of over 5 minutes. Late in the night, the lower decl. target crosses azimuth = 270°, which corresponds to the assumed telescope cablewrap limit. At this time, a direct slew becomes available, and the slew time drops significantly. For any two arbitrary targets i and $j , \tau _ { \mathrm { i j m } } ^ { \mathrm { s l e w } }$ t approximates the pairwise slew time within the bounds of each time slot as dictated by M. The right plot shows the interpolated slew curve (gray) with the travel time tensor $\tau _ { \mathrm { i j m } } ^ { \mathrm { s l e w } }$ (black) overplotted for the full night with $M = 3$ . In this extreme case, $\tau _ { \mathrm { i j m } } ^ { \mathrm { s l e w } }$ often misrepresents the slew time by several minutes in the second and third time slots.

solutions to the TTP that capture both variable accessibility windows and slew overheads.

This paper is organized as follows. We describe the TTP in Section 2 and present a formulation using MILP that can be solved to global optimality for a range of problem sizes. In Section 3, we conduct a suite of numerical experiments to determine the performance and computational cost of our algorithm over various problem sizes. Section 4 discusses the limitations of our global approach and the potential of heuristic solutions. We conclude in Section 5.

# 2. Formulation of Traveling Telescope Problem

# 2.1. Problem Setup

For a given set of targets and an observing interval, we seek the tour that completes all exposures in the shortest possible time. Targets must be accessible for at least part of the observing duration. The slew time between any pair of targets must be computed in advance, but the slew time may itself be a function of time. The formulation presented below was inspired by Sun et al. (2018), who developed a framework to optimize the profitability of parcel pickup and delivery with variable time windows and travel times.

# 2.2. Slot Framework

Following the TSP literature, we refer to targets to be traversed in the TTP as nodes since that work emphasizes that the solution is a directed graph connecting all targets. With a list of N targets to be scheduled, we define the total set of nodes to be $\{ 0 , \ 1 , . . . , N , \ N + 1 \}$ . The nodes 0 and $N + 1$ are the anchoring start and end nodes; their location is arbitrary, i.e., not associated with a celestial source. Their purpose is explained in Section 2.4. Each node i has an associated exposure time tiexp $\tau _ { i } ^ { \mathrm { e x p } }$ and accessibility window $[ t _ { i } ^ { \mathrm { e } } , t _ { i } ^ { \ell } ]$ . The values $t _ { i } ^ { \mathrm { e } }$ and $t _ { i } ^ { \ell }$ are the earliest and latest times the tour can depart node i, i.e., the time the observation concludes (see

Figure 2). We summarize the symbols from the main body of this text in Appendix A.

Next, we break the scheduling interval into M subintervals, $\mathrm { o r } \ ^ { \mathrm { \bullet } } \mathrm { s l o t s } , \mathrm { \ " }$ within which travel time is treated as constant. M is a free parameter and impacts the computational load (see Section 3). The slots may have uneven durations if desired. The boundaries of the slots are $[ w _ { m } , w _ { m + 1 } ]$ , where m indexes each slot.

We then construct the slew tensor $\tau _ { \mathrm { i j m } } ^ { \mathrm { s l e w } }$ that specifies the travel time between any two nodes during every slot (see Figure 1). This depends on the telescope slew speed in altitude and azimuth directions as well as cable-wrap considerations. For a concrete example, $\tau _ { 4 , 6 , 2 } ^ { \mathrm { s l e w } }$ specifies the computed travel time between the i = 4 node and $j = 6$ node during the bounds of the slot $m = 2$ .

# 2.3. Decision Variables

Our MILP formulation involves both binary and continuous variables. The following variables trace the flow through the nodes and the times of node departures:

1. $X _ { i j m }$ is a binary variable equal to 1 if the tour traverses the arc from node i to node j during slot m and 0 otherwise.   
2. $Y _ { i }$ is a binary variable equal to 1 if the node i is entered at some point during the tour and 0 otherwise.   
3. $t _ { i }$ is a continuous variable denoting the departure time from node i.   
4. $t _ { i j m }$ is a continuous variable and equal to $t _ { i }$ if the tour departs the node i toward the node j during the time slot m, and 0 otherwise.

The nonzero elements of $X _ { i j m }$ describe the tour. The tensor dot product of $X _ { i j m }$ and $\tau _ { i j m } ^ { \mathrm { s l e w } }$ ,

$$
\sum_ {i, j = 1} ^ {N} \sum_ {m = 0} ^ {M - 1} \tau_ {i j m} ^ {\text {s l e w}} X _ {i j m}, \tag {1}
$$

is equal to the total travel time.

![](images/8917f3e906c3921875889c535ac5ffe897743a20d6155e38e372657b278b790e.jpg)

![](images/a1241ef5218e88719f35ce26e7b8cd1b4a20ced6ccd923a8be360fab3e60291a.jpg)  
Optimal Tour

![](images/041adea20ca8fb3d9a08b2a485db138f650e1dab0fecf08a8f0ceac0c0ecb66f.jpg)  
Figure 2. Schematic of suboptimal, optimal, and infeasible tours in the traveling telescope problem. The four polar plots on top show the sky above Keck Observatory (latitude = +19 deg) in alt/az coordinates. During a duration of 4 hr, targets A–E move across the sky as the Earth rotates. The shaded region shows an inaccessible region of alt/az (here, the Keck I Nasmyth platform). We have exaggerated slew times to clearly illustrate the differences between the three tours. In the top suboptimal tour, we include a horizontal timeline for targets A–D. The windows of accessibility are shown as vertical ticks. For example, the earliest the telescope can complete observations of target A is labeled with $\mathbf { t } _ { A } ^ { e } ,$ while $\mathbf { t } _ { A } ^ { l } ,$ denotes the latest time. Note that $\mathbf { t } _ { A } ^ { e }$ depends on both the rise time and exposure duration, and is the either the set time or the end of the observing interval, whichever comes first. This scheduler uses a greedy approach, i.e., once the observation of A is complete, the telescope immediately slews to the unobserved target with the shortest slew time. The tour is feasible, but the entire observing duration is required in this example. The middle optimal tour is scheduled with a global optimization. In our example, the slew between A and D is so long that it is advantageous for the telescope to wait until target B rises to observe it, before proceeding to D. This is the optimal tour to observe targets A–D. Finally, the bottom plot shows the inclusion of a fifth target, E, to illustrate an infeasible tour. There is not enough time to observe all targets.

# 2.4. Constraints

Next, we introduce the following constraints.

Constraint 1: Tour must depart the starting node. We require that flow be nonzero from 0 to some arbitrary target node j during some slot m in time to begin the tour:

$$
\sum_ {j = 1} ^ {N} \sum_ {m = 0} ^ {M - 1} X _ {0, j, m} = 1. \tag {2}
$$

Constraint 2: Tour must conclude at the ending node. Similarly, we anchor the end of the tour with the end node N + 1. We must traverse the arc (i, N + 1) from some arbitrary

target node i:

$$
\sum_ {i = 1} ^ {N} \sum_ {m = 0} ^ {M - 1} X _ {i, N + 1, m} = 1. \tag {3}
$$

Constraint 3: Y must indicate the visitation of a node. In the simplest possible case, we have a trivial solution traversing from 0 to N + 1, stopping at a single target node along the way. The objective (see Section 2.5) will reward the visitation of additional nodes between these two constrained anchors. This requires first defining the variable Y to track whether nodes are being visited. $Y _ { i }$ will be activated if the tour flows from the

node i during any slot in time, into any subsequent node $j \colon$

$$
\sum_ {j = 1} ^ {N + 1} \sum_ {m = 0} ^ {M - 1} X _ {i j m} = Y _ {i} \quad \forall i = 0, \dots , N. \tag {4}
$$

Constraint 4: A slew into any target node must be accompanied by a slew away from that node. Excluding the starting and ending nodes, we require that the slew into any target node k must be accompanied by a slew out of k:

$$
\sum_ {i = 0} ^ {N} \sum_ {m = 0} ^ {M - 1} X _ {i k m} - \sum_ {j = 1} ^ {N + 1} \sum_ {m = 0} ^ {M - 1} X _ {k j m} = 0 \quad \forall k = 1, \dots , N. \tag {5}
$$

If $X _ { i j m }$ is 1 for any arc $( i , k )$ in the sequence, it will also hold 1 for some $( k , j )$ arc at an arbitrary time. If the left term is 0 (the tour never enters node k) then the tour will never traverse a departing arc originating at k. The chronology of these events will next be enforced using the time variable t.

Constraint 5: Define the selection variable $t _ { i j m }$ . Now we enforce the proper constraints to define the selection time variable $t _ { i j m }$ relative to our generic time variable $t _ { i } .$ By summing over all potential destinations j and time slots $m ,$ we recover the value stored in $t _ { i } { \mathrm { : } }$

$$
t _ {i} = \sum_ {j = 1} ^ {N + 1} \sum_ {m = 0} ^ {M - 1} t _ {i j m} \quad \forall i = 0, \dots , N. \tag {6}
$$

The second time variable $t _ { i j m }$ is critical for the following two constraints. It behaves like the product of $t _ { i }$ and $X _ { i j m } .$ , but works within a linear program.

Constraint 6: Departure time from a node is greater than the departure from the previous node plus the slew and exposure time. Say we begin to traverse from one node to another on the arc $( i , j )$ within the bounds of the slot $m .$ Before the telescope may depart from the next node $j ,$ a minimum amount of time must pass, equal to the slew experienced on the journey from i to j plus the exposure time at the new node, i.e., $\tau _ { i j m } ^ { \mathrm { s l e w } } + \tau _ { j } ^ { \mathrm { e x p } }$ . The minimum time value of our departure from j is the time that the previous node i was departed $t _ { i j m }$ plus this minimum “passing time.” The inclusion of the variable $X _ { i j m }$ will ensure only the proper values of i and m are considered for the journey to the new node $j \colon$

$$
t _ {j} \geqslant \sum_ {i = 0} ^ {N} \sum_ {m = 0} ^ {M - 1} \left(t _ {i j m} + \left(\tau_ {i j m} ^ {\text {s l e w}} + \tau_ {j} ^ {\text {e x p}}\right) X _ {i j m}\right)
$$

$$
\forall j = 1, \dots , N + 1. \tag {7}
$$

Constraint 7: Ensure departure times are consistent with slot bounds. We must enforce constraints on the departure times $t _ { i j m }$ using bounds of the time windows defined in w. If we exit the node i during the time slot m, then the departure time must be within the bounds of the slot window:

$$
\begin{array}{l} w _ {m} X _ {i j m} \leqslant t _ {i j m} \leqslant w _ {m + 1} X _ {i j m} \\ \forall i = 0, \dots , N + 1 \\ \forall j = 0, \dots , N + 1 \\ \forall m = 0, \dots , M - 1. \tag {8} \\ \end{array}
$$

Constraint 8: Departure times must respect node accessibility. Finally, we enforce the time window constraints on the

departure times $t _ { i }$ for all the visited target nodes:

$$
t _ {i} ^ {\mathrm {e}} Y _ {i} \leqslant t _ {i} \leqslant t _ {i} ^ {\ell} Y _ {i} \quad \forall i = 1, \dots , N. \tag {9}
$$

# 2.5. Objective

We seek to maximize the the number of scheduled exposures while minimizing total slew time:

$$
\left. \operatorname {M a x} \left(\sum_ {i = 1} ^ {N} Y _ {i} - C \sum_ {i, j = 1} ^ {N} \sum_ {m = 0} ^ {M - 1} \tau_ {i j m} ^ {\text {s l e w}} X _ {i j m}\right)\right). \tag {10}
$$

Here, C is a small constant such that the slew penalization (second term) is always less than unity. Notice that our anchor nodes do not contribute to the total slews with this summation convention, and are therefore used only for constraining the flow of the tour (a physical location need not be set, and the values in the first row and column of $\tau _ { i j m } ^ { \mathrm { s l e w } }$ are set to 0).

The objective function does not require all nodes be visited. In similar TSP literature such as Sun et al. (2018), each target node may be assigned a scalar priority $p _ { j }$ included as a coefficient in the left summation term in Equation (10). In such a formulation, lowest-priority targets are preferentially excluded when total completion is infeasible. We note that global optimality becomes less intuitive when targets have different numerical priorities.

In the TTP, the optimization will work to remove the targets that contribute most to the total slews in every case. The objective is clear: To observe as many targets as possible as quickly as possible. We note that the formulation above describes a simple TTP where targets are observed once and no additional constraints are placed on the timing between observations. Appendix B describes small modifications to the algorithm presented above that can accommodate such constraints.

# 3. Performance

# 3.1. Numerical Experiments

We evaluated our algorithm’s ability to solve the TTP through a suite of simulated target lists. We explored problem complexity along the following three axes: number of targets N, number of time slots M, and duration of the scheduling interval D. We designed TTPs in the following manner:

1. We specified a random calendar night at Keck Observatory.   
2. We selected an observing duration D.   
3. We selected N stars from the California Legacy Survey (CLS; Rosenthal et al. 2021), a collection of 719 nearby stars that have been observed from Keck observatory for several decades as part of an extrasolar planet search. These stars comprise a good TTP test set because they are nearly uniformly distributed on the sky with decl. $\delta \gtrsim - 4 0$ deg and are thus observable for ${ \gtrsim } 7$ months per year. When sampling the targets, we required they be accessible for more than 50% of duration D. We removed a few close binaries that have negliable slew speeds.   
4. We modeled the slew rate of the Keck telescope as 1 deg per second in both altitude and azimuth directions.

![](images/6c0ed5f8c15d0d05b0d005fffc152a757c64cd593ca33b10e9fe7f3810e60d95.jpg)

![](images/4a317d790a25f6b99838740daa77805419386f07ab1e8272e133706477086782.jpg)

![](images/7b587fbb58e47284dbd4a4ec4d05f88c7c3f385531271f65bcf9dc5f979fbb92.jpg)

![](images/be312f075b1a994fb4e97893208a1463ed729e40f6113f4e38957614dde861b7.jpg)

![](images/36bf87b0b1f2a4f90ce53eab4ea8699536c1dad2c62c754a7f6c53ad4dae4eb9.jpg)

![](images/e61ea1fb44603aa926f1799cedbb4189828779f03866ffde10767e124eac2bc5.jpg)  
Figure 3. Comparison of a simple heuristic target ordering and a TTP-optimized tour of N = 50 targets during a simulated half night. The former routine orders the targets by their increasing set times. Top row: the azimuthal coordinate of the simulated telescope in each case. Middle row: the elevation angle of the simulated telescope. Bottom row: time spent exposing, slewing, or idle. The targets have randomized time windows, but are all accessible for at least half of the scheduling duration. The worst-case slew estimation from Equation (11) is 3.34 minutes per target. For the left (heuristic) column, the total slew time is 73 minutes, or an average of 91 s per slew, leaving 27 minutes idle. In the optimized (right) tour, the total time is a mere 13.8 minutes, or an average of 17.3 s per slew, resulting in 86 minutes idle (23 additional targets at the same pace).

5. We assigned uniform exposure times (in minutes) to all targets according to

$$
\tau_ {i} ^ {\exp} = (D - 2 N) / N \quad \forall i = 1, \dots , N. \tag {11}
$$

Setting the exposure times this way would completely fill the observing duration given a random ordering of targets with an average slew time of 120 s or 2 minutes. For our experiments, slews in azimuth (which ranges from 0 to 360 deg) dominate over those in altitude (which ranges from 0 to 90 deg). The average distance between two randomly selected values between 0 and 360 is 120. We expect all solutions to the TTP to be significantly more efficient. Thus, our experiments are feasible by construction and we report the improvement relative to this random ordering.

6. We selected M uniform slots within D.   
7. We calculated the distance tensor tijmslew $\tau _ { i j m } ^ { \mathrm { s l e w } }$ at the midpoint of each slot.

With the experiment specified, we solved the MILP described in Section 2 with one additional constraint.

Constraint 9: All target nodes must be visited.

$$
Y _ {i} = 1 \quad \forall i = 1, \dots , N. \tag {12}
$$

The problem generation process described above in general results in TTP instances in which it is possible to observe all N targets. Given this, we modify the objective function described in Equation (10) to focus on minimizing slews only, resulting in the following new objective function:

$$
\operatorname {M i n} \left(\sum_ {i, j = 1} ^ {N} \sum_ {m = 0} ^ {M - 1} \tau_ {i j m} ^ {\text {s l e w}} X _ {i j m}\right). \tag {13}
$$

In our results, in Section 3.2, we use TTP-Global to refer to the formulation defined in Section 2 with the objective function in Equation (13) and constraint (12).

Before describing our grid-based exploration of problem complexity, we show one example solution to the TTP in Figure 3. We compared it with a simple heuristic solution for a 50 target observing sequence conducted over a half night to emulate a human-generated script. In this heuristic, targets are observed in the order of their set times, i.e., the earliest setting target is observed first. Figure 3 shows graphically the slew overheads that TTP-Global eliminates through a more efficient ordering.

# 3.2. Computational Results

We test our formulation using different combinations of the number of targets N, the number of slots M, and the duration/ scheduling interval D. For the scheduling interval D, we consider quarter nights, half nights, and full nights. For quarter nights, we vary N in {5, 10, 25}; for half nights, we vary N in {5, 10, 25, 50}; and for full nights, we vary N in {5, 10, 25, 50, 100}. For each combination of D and N, we vary M in {1, 3, 10}.

For each combination of N and D, we consider 10 randomly generated sets of targets, and consider the three different values of M, giving rise to a total of $( 3 + 4 + 5 ) \times 3 \times 1 0 = 3 6 0$ problem instances. We solved TTP-Global using Gurobi v10.0.1, a stateof-the-art optimization suite that solves MILP problems using the branch-and-bound algorithm (Gurobi Optimization, LLC 2023). We used the Python programming language to generate the input data for TTP-Global and to formulate TTP-Global using the Gurobi Python API. We conducted our suite of numerical experiments on Amazon Elastic Compute Cloud (EC2), on a single instance of type m6a.48xlarge (AMD EPYC 7R13 processor, with 192 virtual CPUs and 768 GB of memory). For each experiment, we allocated eight virtual CPUs and limited computation time to 1800 s.

For a few points of reference, a TTP with N = 25 targets and $M = 1$ involved an MILP with 1643 rows (constraints) and

![](images/48777508beb68c39f145b504952f3ddcc1556922ac755c13e20cb274b6a36669.jpg)

![](images/8574b132a5927121631f536bb502f26d23b3ec9248cfca15099e41d1bc4aa608.jpg)

![](images/de4e62182e25d168c1f69caaa6cc3d2dbaac79a2936743309232035cd1071570.jpg)

![](images/1031a93ce36853fb71d8cee56d3912266033467807d2d3ad6a6a22cdd8eac454.jpg)

![](images/a56701b17aeff8dfdf50b7dd4a784d5be4b4bf5070057a84cbb9a901cfe002f8.jpg)

![](images/613ba16c9395d600cc88cc69e32ae5f6206f4d6449bd4dcadf8ac7812afa96e2.jpg)  
Figure 4. Top row: average value of Runtime for TTP-Global when scheduling each duration type D, with varying values of M. In the quarter-night case, TTP-Global can schedule all 25 observations for M < 10, but struggles to reach optimality at $M = 1 0 .$ In the half-night case, only the M = 1 model achieves optimality for $N = 5 0 .$ . For the full-night case, TTP-Global handles $N = \bar { 1 0 0 }$ far better than expected for the static case in comparison to $N = 5 0 .$ Bottom row: average relative improvement $\mathtt { R e l R e d } _ { \mathtt { r e a l } }$ for each value of D across the model types. For all D and the respective maximum values of N, TTP-Global can reliably reduce slews by around a factor of 5. For small N, there is some benefit to using $\dot { M ^ { \setminus 1 } }$ . For larger models, the risk of long slews in the $M = 1$ case has little impact on RelRedreal.

1513 columns (variables), and the $M = 1 0$ case had 14,765 rows and 14,635 columns. A TTP with $N = 1 0 0$ targets had 21,518 rows and 21,013 columns for $M = 1$ , and 208,790 rows and 208,285 columns for $M = 1 0 .$ .

For each experiment, we recorded the following information:

1. SlewTimeτ: total slew time of the final schedule obtained from Gurobi, calculated using the discretized tensor t ijmslew. $\tau _ { i j m } ^ { \mathrm { s l e w } }$   
2. RelRedτ: relative reduction in slew time of the final schedule compared to the randomly ordered value of 2N; mathematically, it is defined as

$$
\operatorname {RelRed} _ {\tau} = \frac {2 N - \operatorname {SlewTime} _ {\tau}}{2 N} \times 100 \% \tag{14}
$$

3. $\mathtt { S l e w T i m e } _ { \mathtt { r e a l } } \mathtt { i m e } _ { \mathtt { r e a l } } \mathtt { i m e } _ { \mathtt { r e a l } } .$ real slew time of the final schedule, calculated based on the $t _ { i }$ departure time values of the schedule.   
4. Rel $. { \mathrm { R e d } } _ { \tt c e a l } .$ the analog of $\mathtt { R e l R e d } _ { \mathtt { r e a l } }$ for the real slew time.   
5. Runtime: computation time.   
6. Whether a provably optimal solution was found.   
7. Whether a feasible solution was found.

Table 1 summarizes these statistics for the 10 experiments conducted at each combination of $N , M ,$ and D. We report the number of experiments where Gurobi found a feasible solution, NumFeas, and a provably optimal solution NumOptimal. For the feasible set, we report the average values of SlewTimeτ, RelRedτ, $\mathtt { S l e w T i m e } _ { \mathtt { r e a l } }$ , and $\mathtt { R e l R e d } _ { \mathtt { r e a l } }$

for each combination of N, M, and D, where the average is taken over the NumFeas instances for which a feasible solution was found. For example, for (Half, 50, 3), NumFeas is 8, indicating that Gurobi found a feasible schedule in only eight out of the 10 instances; consequently, the value of 12.7 for SlewTimeτ is the average slew time over those eight feasible schedules. We show the average Runtime and $\mathtt { R e l R e d } _ { \mathtt { r e a l } }$ values for different problem sizes in Figure 4.

# 4. Discussion

We may draw a number of conclusions about the suitability of TTP-Global for the TTP from Table 1 and Figure 4. Gurobi generally found a feasible schedule when the number of targets $N \leqslant 2 5$ . For $N \geqslant 5 0$ targets, our ability to find a feasible solution depended sensitively on the number of slots. Gurobi found a feasible schedule for all 10 instances when $M = 1$ , for some when $M = 3$ , and for none when $M = 1 0$ .

Not surprisingly, runtime was a strong function of N and M, as can be clearly seen in Figure 4. For example, Gurobi found an optimal solution for all $( \bar { D , } N , M ) = ( \mathrm { F u l l } , 2 \bar { 5 } ,$ 1) experiments with an average Runtime of 4.7 s. In contrast, the (Full, 25, 10) experiments found no optimal solutions in the 1800 s time limit. For the largest (Full, 100, 3) experiments, not even a feasible solution was found in the time limit. We find that the $M = 1$ case scales well into the realm of $N = 1 0 0$ , solving even faster than the $N = 5 0$ case. While this goes against our initial intuition, we suspect this behavior is the result of parameter tuning by Gurobi to accommodate larger models.

Table 1 Computational Results of TTP-Global for Different Values of D, N, and M   

<table><tr><td>D</td><td>N</td><td>M</td><td>NumFeas</td><td>NumOptimal</td><td>Runtime (s)</td><td>SlewTimeτ (min)</td><td>RelRedτ (%)</td><td>SlewTime real (min)</td><td>RelRed real (%)</td></tr><tr><td>Quarter</td><td>5</td><td>1</td><td>10</td><td>10</td><td>0.0</td><td>4.1</td><td>59.1</td><td>5.3</td><td>47.0</td></tr><tr><td>Quarter</td><td>5</td><td>3</td><td>10</td><td>10</td><td>0.0</td><td>3.7</td><td>63.3</td><td>5.3</td><td>47.0</td></tr><tr><td>Quarter</td><td>5</td><td>10</td><td>10</td><td>10</td><td>0.1</td><td>3.5</td><td>64.5</td><td>5.1</td><td>48.7</td></tr><tr><td>Quarter</td><td>10</td><td>1</td><td>10</td><td>10</td><td>0.0</td><td>5.8</td><td>70.9</td><td>8.2</td><td>58.8</td></tr><tr><td>Quarter</td><td>10</td><td>3</td><td>10</td><td>10</td><td>0.3</td><td>5.4</td><td>73.2</td><td>8.1</td><td>59.4</td></tr><tr><td>Quarter</td><td>10</td><td>10</td><td>10</td><td>10</td><td>2.1</td><td>5.3</td><td>73.7</td><td>7.7</td><td>61.4</td></tr><tr><td>Quarter</td><td>25</td><td>1</td><td>10</td><td>10</td><td>0.5</td><td>8.1</td><td>83.8</td><td>13.0</td><td>74.0</td></tr><tr><td>Quarter</td><td>25</td><td>3</td><td>10</td><td>9</td><td>217.7</td><td>7.8</td><td>84.4</td><td>11.3</td><td>77.5</td></tr><tr><td>Quarter</td><td>25</td><td>10</td><td>8</td><td>3</td><td>1625.2</td><td>9.6</td><td>80.8</td><td>13.7</td><td>72.7</td></tr><tr><td>Half</td><td>5</td><td>1</td><td>10</td><td>10</td><td>0.0</td><td>4.9</td><td>50.8</td><td>7.5</td><td>25.4</td></tr><tr><td>Half</td><td>5</td><td>3</td><td>10</td><td>10</td><td>0.0</td><td>4.7</td><td>53.2</td><td>6.3</td><td>36.8</td></tr><tr><td>Half</td><td>5</td><td>10</td><td>10</td><td>10</td><td>0.1</td><td>4.4</td><td>55.5</td><td>6.3</td><td>37.1</td></tr><tr><td>Half</td><td>10</td><td>1</td><td>10</td><td>10</td><td>0.1</td><td>6.5</td><td>67.3</td><td>12.5</td><td>37.6</td></tr><tr><td>Half</td><td>10</td><td>3</td><td>10</td><td>10</td><td>0.5</td><td>5.8</td><td>70.8</td><td>9.8</td><td>51.1</td></tr><tr><td>Half</td><td>10</td><td>10</td><td>10</td><td>10</td><td>3.5</td><td>5.5</td><td>72.4</td><td>8.5</td><td>57.4</td></tr><tr><td>Half</td><td>25</td><td>1</td><td>10</td><td>10</td><td>9.7</td><td>9.2</td><td>81.5</td><td>15.5</td><td>69.0</td></tr><tr><td>Half</td><td>25</td><td>3</td><td>10</td><td>8</td><td>776.8</td><td>8.5</td><td>83.0</td><td>15.2</td><td>69.6</td></tr><tr><td>Half</td><td>25</td><td>10</td><td>8</td><td>0</td><td>1800.0</td><td>12.7</td><td>74.6</td><td>20.5</td><td>59.1</td></tr><tr><td>Half</td><td>50</td><td>1</td><td>10</td><td>5</td><td>954.7</td><td>12.1</td><td>87.9</td><td>22.8</td><td>77.2</td></tr><tr><td>Half</td><td>50</td><td>3</td><td>8</td><td>0</td><td>1800.0</td><td>12.7</td><td>87.3</td><td>22.4</td><td>77.6</td></tr><tr><td>Half</td><td>50</td><td>10</td><td>0</td><td>0</td><td>1800.1</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Full</td><td>5</td><td>1</td><td>9</td><td>9</td><td>0.0</td><td>6.0</td><td>39.7</td><td>6.8</td><td>31.7</td></tr><tr><td>Full</td><td>5</td><td>3</td><td>9</td><td>9</td><td>0.0</td><td>5.3</td><td>47.0</td><td>7.3</td><td>27.0</td></tr><tr><td>Full</td><td>5</td><td>10</td><td>9</td><td>9</td><td>0.0</td><td>5.3</td><td>47.3</td><td>7.0</td><td>29.5</td></tr><tr><td>Full</td><td>10</td><td>1</td><td>9</td><td>9</td><td>0.1</td><td>8.3</td><td>58.6</td><td>13.1</td><td>34.6</td></tr><tr><td>Full</td><td>10</td><td>3</td><td>9</td><td>9</td><td>0.6</td><td>7.4</td><td>62.8</td><td>8.6</td><td>56.8</td></tr><tr><td>Full</td><td>10</td><td>10</td><td>9</td><td>9</td><td>1.6</td><td>6.5</td><td>67.6</td><td>8.9</td><td>55.3</td></tr><tr><td>Full</td><td>25</td><td>1</td><td>10</td><td>10</td><td>4.7</td><td>10.4</td><td>79.1</td><td>19.9</td><td>60.2</td></tr><tr><td>Full</td><td>25</td><td>3</td><td>10</td><td>5</td><td>1379.4</td><td>9.6</td><td>80.7</td><td>16.7</td><td>66.6</td></tr><tr><td>Full</td><td>25</td><td>10</td><td>10</td><td>0</td><td>1800.0</td><td>12.3</td><td>75.3</td><td>19.1</td><td>61.8</td></tr><tr><td>Full</td><td>50</td><td>1</td><td>10</td><td>7</td><td>1009.6</td><td>13.2</td><td>86.8</td><td>24.5</td><td>75.5</td></tr><tr><td>Full</td><td>50</td><td>3</td><td>3</td><td>0</td><td>1800.0</td><td>18.8</td><td>81.2</td><td>27.6</td><td>72.4</td></tr><tr><td>Full</td><td>50</td><td>10</td><td>0</td><td>0</td><td>1800.0</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Full</td><td>100</td><td>1</td><td>10</td><td>8</td><td>619.8</td><td>16.4</td><td>91.8</td><td>36.1</td><td>82.0</td></tr><tr><td>Full</td><td>100</td><td>3</td><td>0</td><td>0</td><td>1800.1</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Full</td><td>100</td><td>10</td><td>0</td><td>0</td><td>1800.0</td><td>—</td><td>—</td><td>—</td><td>—</td></tr></table>

Note. “–” indicates that the metric could not be calculated due to Gurobi not being able to obtain a feasible schedule for any of the 10 instances. For $D = \mathrm { F u l l } , N = 5$ and $D = \mathrm { F u l l } , N = 1 0$ , one instance was determined to be infeasible. The goal of our experiment is to devise target lists and exposure times that are feasible in the limit of large N, however for small N this is not strictly guaranteed.

When we do find a feasible schedule, it is significantly more efficient relative to the 2N baseline. For example, for the $( D , N ,$ $M ) = ( \mathrm { H a l f } , 5 0 , 3 )$ experiments, the average $\mathtt { S l e w T i m e } _ { \mathtt { r e a l } }$ is 22.4 minutes compared to the $2 N = 1 0 0$ minute benchmark, a reduction of $\mathrm { R e l R e d } _ { \mathrm { r e a l } } = 7 7 . 6 \%$ . For the (Full, 100, 1) set of instances, the average $\mathtt { S l e w T i m e } _ { \mathtt { r e a l } }$ is 36.1 minutes, which is a reduction of 82.0% relative to the $2 N = 2 0 0$ minute benchmark. We note that in all cases SlewTimeτ is less than $\mathsf { S 1 e w T i m e } _ { \mathtt { r e a l } } .$ For example, for the same $D = \mathrm { F u l l } .$ , N = 100, M = 1 set of instances, SlewTimeτ is a mere 16.4 minutes, which is a reduction of $\mathrm { R e l R e d } _ { \tau } { = } 9 1 . 8 \%$ relative to the 200 minutes worstcase value. The difference between $\mathtt { R e l R e d } _ { \mathtt { r e a l } }$ and RelRedτ stems from our piecewise slew approximation, i.e., the choice of M for each model.

In the quarter-night models, we find little improvement from using higher values of M, since the slews vary minimally with respect to time. For the longer durations, we see some benefit for higher M in the simpler $N < 2 5$ cases. For $N \geqslant 2 5 ,$ the higher-M models become too complex to be solved to optimality in the time limit (leaving better slews in question),

but the M = 1 models continue to demonstrate extremely efficient slews despite the higher expected variability.

In most cases, increasing the value of M did not demonstrate a significant advantage over the static models. For the high-N models, the optimizer was often not able to construct a feasible solution for $M > 1$ . For scheduling full nights of observations, the $M = 1$ case demonstrates dramatic improvement in slew times by up to a factor of 5, and increasing M provides more computational complexity than can be handled by our global algorithm in the time limit. For most cases, we would recommend M = 1 be the standard due to its exceptionally fast runtime.

In our numerical experiments we attempted to solve TTP-Global to a provably optimal solution by branch-and-bound algorithm. For large numbers of targets or finely discretized slew tensors this approach may not be computationally tractable. We note that many heuristic solutions to the TSP have been developed that achieve near-optimal solutions. We suspect that analogous high-quality heuristic solutions exist for the TTP, which may be equipped to solve the $M > 1$ models for much higher N. We develop one such procedure in the Appendix C for comparison with our global solution.

# 5. Conclusions

In this work, we addressed the challenge of determining the most efficient ordering of a set of exposures at a telescope. We formulated the TTP as an MILP, TTP-Global, and solved it using a standard commercial optimizer for problem sizes as large as 100 targets in ∼10 minutes using modest computational resources. The speed of TTP-Global means it can be run dynamically throughout the night and respond to real-time changes in target accessibility from weather. Further work is needed to develop algorithms that can solve the TTP for substantially larger sets of targets or substantially finer time resolution in slew overheads. Local searches initialized with an heuristic solution may prove fruitful. We hope that algorithms like the one described here can assist or automate scheduling, save human effort, and increase the scientific productivity of astronomical surveys.

# Acknowledgments

L.H. and E.A.P. acknowledge support from the following sources: the Heising-Simons Foundation grant No. 2022-3832. V.V.M. acknowledges support from the UCLA Anderson School of Management. We are grateful for enlightening conversations with Eric Bellm.

Software: astropy (Astropy Collaboration et al. 2013, 2018), numpy (Harris et al. 2020), pandas (pandas development team 2020), gurobi (Gurobi Optimization, LLC 2023), matplotlib (Hunter 2007).

# Appendix A Variables

Table 2 lists the variables used in all preceding sections of this paper, along with the location of their first usage.

Table 2   
Symbols Used   

<table><tr><td>Symbol</td><td>Definition</td><td>Section</td></tr><tr><td>C</td><td>Small normalization constant used in objective func-tion. Ensures the scheduling of additional observations is prioritized</td><td>2.5</td></tr><tr><td>i, j, k</td><td>Indices for arbitrary nodes</td><td>2.2</td></tr><tr><td>m</td><td>Index for an arbitrary time slot</td><td>2.2</td></tr><tr><td>M</td><td>The number of time slots where slews are assumed constant</td><td>2.2</td></tr><tr><td>N</td><td>The number of celestial targets assigned to the TTP</td><td>2.2</td></tr><tr><td>ti e</td><td>The earliest time value at which the node i can be departed based on observability constraints</td><td>2.2</td></tr><tr><td>ti l</td><td>The latest time value at which the node i can be departed based on observability constraints</td><td>2.2</td></tr><tr><td>ti</td><td>A continuous variable indicating the time value of the departure from node i</td><td>2.3</td></tr><tr><td>wm</td><td>The time value at which the slot m begins</td><td>2.2</td></tr><tr><td>Xijm</td><td>A binary decision variable indicating the flow state between nodes i, j during the time slot m.</td><td></td></tr><tr><td rowspan="2">Yi</td><td>Holds 1 if a slew takes place, and 0 otherwise</td><td>2.3</td></tr><tr><td>A binary decision variable that indicates the visitation of the node i. Holds 1 if the node is visited, and 0 otherwise</td><td>2.3</td></tr><tr><td>τi exp</td><td>The exposure duration of the target node i</td><td>2.2</td></tr><tr><td>τi slew</td><td>Travel time between the nodes i, j during the time slot m</td><td>2.2</td></tr><tr><td>τijm</td><td></td><td></td></tr></table>

# Appendix B Variants of the Traveling Telescope Problem

# B.1. Consecutive Targeting

One may require two exposures, i and i¢, be scheduled back to back, such as a science observation and a calibration observation. Such linked observations may be specified via two additional constraints:

$$
Y _ {i} + Y _ {i ^ {\prime}} = 2 \left(\sum_ {m = 0} ^ {M - 1} X _ {i i ^ {\prime} m} + \sum_ {m = 0} ^ {M - 1} X _ {i ^ {\prime} i m}\right), \tag {B1}
$$

$$
Y _ {i} = Y _ {i ^ {\prime}}. \tag {B2}
$$

The first constraint ensures that if both observations take place the directed tour must pass directly from i to $i ^ { \prime }$ or vice versa. The second constraint ensures both observations or neither observation occur.

# B.2. Intra-night Spacing Requirements

One may wish to enforce a minimum interval between two exposures. A common example occurs in time-series monitoring where multiple observations of the same target occur during the same night, subject to a minimum separation. We accomplish this by letting N correspond to the total number of exposures to be collected across all targets. For simplicity, let us assign exposure indices such that exposures of the same target occur consecutively in the total exposure list $\{ 1 , . . . , N \}$ . That is, if the target requires $n ^ { \exp }$ individual exposures, the node indices $\{ \kappa , { \bar { \kappa } } + 1 , { \bar { \ldots } } , \kappa + n ^ { \mathrm { e x p } } - 1 \}$ correspond to that target for some value κ.

With the repeat observations specified, we enforce a minimum interval via the following constraint:

$$
\sum_ {j = 1} ^ {N + 1} \sum_ {m = 0} ^ {M - 1} t _ {i j m} \geqslant \sum_ {j = 1} ^ {N + 1} \sum_ {m = 0} ^ {M - 1} t _ {i - 1, j, m} + Y _ {i} \tau^ {\text {s e p}},
$$

$$
\forall i = \kappa + 1, \dots , \kappa + n ^ {\exp} - 1. \tag {B3}
$$

Subsequent exposures of a given target must not end until at least $\tau ^ { \mathrm { s e p } }$ has passed since the previous exposure ended. For example, if the linked exposures of a target have index i = 5 and 6, exposure 6 may not end until at least $\tau ^ { \mathrm { s e p } }$ has passed since exposure 5 ended.

# Appendix C Local Search Heuristic

Here, we develop an alternative formulation to the TTP that uses a local search (LS) heuristic. We refer to this as TTP-LS to distinguish it from TTP-Global, which searches the global solution space.

# C.1. Algorithm Description

In the TTP, there are two sets of decisions that need to be made simultaneously. One is the sequence in which the targets will be visited. For example, with $N = 5 ,$ we have to choose between $5  1  4  2  3 , 1  3  2  4  5$ , and so on. The other set of decisions involves the timing slews. This involves deciding a (continuous) time ti within the observing duration D to slew and the corresponding slot m. Even with a fixed sequence of exposures, this is a nontrival task. As a result, making both sets of decisions under the umbrella of a single MILP formulation is computationally demanding.

This suggests an alternate approach to the TTP that decouples the sequence decision from the timing decision. Suppose that the sequence of targets is fixed. When should the telescope slew in order to minimize slew times? Let $\sigma$ denote the sequence of targets, which is a bijective function σ: $\{ 1 , . . . , N \} \longrightarrow \{ 1 , . . . , N \}$ , and let the minimum total slew time be denoted by the function $F ,$ so that $F ( \sigma )$ is the minimum total slew time that one would obtain from following the sequence σ. Let Σ denote the set of all such sequences. For example, for $N = 5$ targets and the sequence $5  1  4  2  3 \quad$ the corresponding σ is

$$
\begin{array}{l} \sigma (1) = 5 \\ \sigma (2) = 1 \\ \sigma (3) = 4 \\ \sigma (4) = 2 \\ \sigma (5) = 3. \\ \end{array}
$$

The TTP can then be abstractly formulated as

$$
\min_{\sigma \in \Sigma}F(\sigma),
$$

which is an optimization problem over sequences in Σ. $\mathbf { A } \mathbf { s }$ written, this is not a problem that can be readily provided to any commercial solver, but because of the discrete nature of $\Sigma ,$ it can potentially be solved using local search. Let $z \in \{ 1 , . . . , N \}$ and $z ^ { \prime } \in \{ 1 , . . . , z - 1 , z + 1 , . . . , N \}$ be positions in the sequence, and let $\sigma ^ { z  z ^ { \prime } }$ denote the sequence obtained by swapping the targets in positions z and $z ^ { \prime } { \mathrm { ; } }$ that is, $\sigma ^ { z  z ^ { \prime } }$ is the unique sequence such that

$$
\begin{array}{l} \sigma (z) = \sigma^ {z \leftrightarrow z ^ {\prime}} (z ^ {\prime}), \\ \sigma \left(z ^ {\prime}\right) = \sigma^ {z \leftrightarrow z ^ {\prime}} (z), \\ \sigma \left(z ^ {\prime \prime}\right) = \sigma^ {z \leftrightarrow z ^ {\prime}} \left(z ^ {\prime \prime}\right) \quad \forall z ^ {\prime \prime} \in \{1, \dots , N \} \backslash \left\{z, z ^ {\prime} \right\}. \\ \end{array}
$$

Let $\mathcal { N } _ { z } ( \sigma )$ denote the set of neighboring sequences of σ obtained by swapping the target at position z with a target at any other position:

$$
\mathcal {N} _ {z} (\sigma) = \left\{\sigma^ {\prime} \in \Sigma \left| \begin{array}{l} \sigma^ {\prime} = \sigma^ {z \leftrightarrow z ^ {\prime}} \\ \text {f o r s o m e} z ^ {\prime} \in \{1, \ldots , z - 1, z + 1, \ldots , N \} \end{array} \right. \right\}.
$$

With this definition, our local search algorithm can be formally described as Algorithm 1.

Algorithm 1. Pseudo-code of local search procedure.

Require: Initial sequence s Î S.

1: Set $\mathcal { U } \gets \{ 1 , . . . , N \} .$

2: while $| \mathcal { U } | > 0$ do

3: Select z Î ; set $\mathcal { U }  \mathcal { U } \backslash \{ z \}$

4: Set $\begin{array} { r } { \sigma ^ { * } \gets \operatorname * { a r g m i n } _ { \sigma ^ { \prime } \in \mathcal { N } _ { z } ( \sigma ) } F ( \sigma ^ { \prime } ) } \end{array}$

5: Set $\begin{array} { r } { F ^ { \prime } \gets \operatorname* { m i n } _ { \sigma ^ { \prime } \in \mathcal { N } _ { z } ( \sigma ) } F ( \sigma ^ { \prime } ) } \end{array}$

6: if $F ^ { \prime } < F ( \sigma )$ then

7: Set $\sigma \gets \sigma ^ { * }$

8: Set $\mathcal { U } \gets \{ 1 , . . . , z - 1 , z + 1 , . . . , N \}$

9: end if

10:end while

11: return Locally optimal sequence σ

In words, we begin from some initial sequence σ. We use  to denote the set of sequence positions which we have not yet tried to modify. As long as there is at least one sequence

position we have not tried to change, we pick a sequence position $z ,$ and calculate the best neighboring sequence $\sigma ^ { * }$ obtained by swapping the target at position z with the target at any other position. If the objective value $F ^ { \prime }$ of the best neighboring sequence improves on the current objective value $F ( \sigma )$ , we replace σ with $\sigma ^ { * }$ , and we reset  to be the set of all positions. Otherwise, if we do not make improvement in an iteration of the while loop, then  will be reduced by one member. If N such iterations occur, then $\boldsymbol { u }$ will be empty, and we will have ascertained that there is no neighboring sequence we can move to in order to reduce the objective value; in other words, σ is a locally optimal sequence. We note that this heuristic is similar to the 2-OPT heuristic (Croes 1958) for the classical TSP problem, which involves eliminating two edges in a TSP tour and reconnecting the tour so that the edges are swapped. The main difference comes from the function F, which calculates the minimum total slew time when one assigns the targets in the sequence to slots optimally.

Before this algorithm can be deployed, we must specify how to compute $F ( \sigma ) .$ . The function value $F ( \sigma )$ for a fixed sequence σ can be calculated by solving a MILP. While this MILP shares some similarities with the TTP problem described in Section $^ { 2 , }$ it is simpler because the target sequence is fixed and “baked in” to the optimization problem. This smaller MILP is a subroutine in Algorithm 1. We provide further details on this integer program in Section C.2.

We must also consider sequences of targets that are infeasible. In some cases, for a fixed sequence σ of targets, it may not be possible to make the timing decisions and the slot decisions in a way that respects the accessibility windows and slot bounds. In such cases, the MILP that defines the function F ( · ) will be infeasible. We can extend the definition of $F ( \cdot )$ so that $F ( \sigma ) = + \infty$ if the corresponding MILP is infeasible for sequence σ; since Algorithm 1 is always choosing the neighboring sequence with the lowest value of F, this ensures that Algorithm 1 will never replace the current sequence with one that is infeasible.

However, even with this fix, one problem that still remains is if the initial sequence σ and all neighboring sequences of that initial sequence are infeasible. In this case, Algorithm 1 will not return a feasible sequence, as it will simply terminate with the current sequence. This is a serious issue, because it is not straightforward to identify a sequence of targets for which the TTP problem constraints can be perfectly satisfied. In Section C.3, we present a feasibility heuristic for identifying such a sequence.

# C.2. Calculating Minimum Total Slew Time for a Fixed Sequence of Targets

As noted in the previous section, a key component of Algorithm 1 is the function F, which maps a sequence σ to a minimum slew time $F ( \sigma )$ . We use z to denote the index of a position in this sequence σ. For targets, z will range in {1, 2,K, $N \}$ . With a slight abuse of notation, we will use $z = 0$ to denote the start node of the telescope, and assume that σ $( 0 ) = 0 ;$ ; similarly, $\sigma ( N + 1 ) = N + 1$ at the final node. Thus, z can take any value in $\{ 0 , 1 , . . . , N + 1 \}$ .

Let $Y _ { z , m } ^ { \mathrm { a t } }$ be a binary decision va elescope $z \in \{ 0 , ~ 1 , . . . , N + 1 \}$ sequence in slot m, and 0 otherwise. Let $Y _ { z , m } ^ { \mathrm { b y } }$ be a binary

decision variable that is 1 if the telescope reaches slot m by position $z \in \{ 0 , 1 , . . . , N + 1 \}$ in the sequence and 0 otherwise. Let $t _ { z }$ denote the departure time of the telescope from the node at position $z .$ The function F is obtained by solving the following MILP:

$$
\text {m i n i m i z e} \quad \sum_ {z = 1} ^ {N} \sum_ {m = 0} ^ {M - 1} \tau_ {\sigma (z), \sigma (z + 1), m} ^ {\text {s l e w}} Y _ {z, m} ^ {\text {a t}} \tag {C4a}
$$

$$
\text {s u b j e c t} Y _ {0, 0} ^ {\text {b y}} = 1, \tag {C4b}
$$

$$
\begin{array}{l} Y _ {z, m} ^ {\mathrm {b y}} \leqslant Y _ {z + 1, m} ^ {\mathrm {b y}}, \quad \forall z \\ = 0, 1, \dots , N, m = 0, 1, \dots , M - 1, \tag {C4c} \\ \end{array}
$$

$$
\begin{array}{l} Y _ {z, m + 1} ^ {\mathrm {b y}} \leqslant Y _ {z, m} ^ {\mathrm {b y}}, \quad \forall z \\ = 0, 1, \dots , N + 1, m = 0, 1, \dots , M - 2, \tag {C4d} \\ \end{array}
$$

$$
\begin{array}{l} Y _ {z, m} ^ {\mathrm {a t}} = \quad Y _ {z, m} ^ {\mathrm {b y}} - Y _ {z, m + 1} ^ {\mathrm {b y}}, \quad \forall z \\ = 0, 1, \dots , N + 1, m = 0, 1, \dots , M - 2, \quad \left(\mathrm {C} 4 \mathrm {e}\right) \\ \end{array}
$$

$$
Y _ {z, M - 1} ^ {\mathrm {a t}} = Y _ {z, M - 1} ^ {\mathrm {b y}}, \quad \forall z = 0, 1, \dots , N + 1, \tag {C4f}
$$

$$
\begin{array}{l} t _ {z} \geqslant t _ {z - 1} + \sum_ {m = 0} ^ {M - 1} \tau_ {\sigma (z - 1), \sigma (z), m} ^ {\mathrm {s l e w}} \cdot Y _ {z - 1, m} ^ {\mathrm {a t}} \\ + \tau_ {\sigma (z)} ^ {\exp}, \quad \forall z = 1, 2, \dots , N + 1, \tag {C4g} \\ \end{array}
$$

$$
t _ {z} \geqslant \sum_ {m = 0} ^ {M - 1} w _ {m} \cdot Y _ {z, m} ^ {\mathrm {a t}}, \quad \forall z = 0, 1, \dots , N + 1, \tag {C4h}
$$

$$
t _ {z} \leqslant \sum_ {m = 0} ^ {M - 1} w _ {m + 1} \cdot Y _ {z, m} ^ {\mathrm {a t}}, \quad \forall z = 0, 1, \dots , N + 1, \tag {C4i}
$$

$$
t _ {z} \geqslant t _ {\sigma (z)} ^ {e}, \quad \forall z = 0, 1, \dots , N + 1, \tag {C4j}
$$

$$
t _ {z} \leqslant t _ {\sigma (z)} ^ {\ell}, \quad \forall z = 0, 1, \dots , N + 1, \tag {C4k}
$$

$$
Y _ {z, m} ^ {\mathrm {b y}} \in \{0, 1 \}, \quad \forall z = 0, 1, \dots , N + 1,
$$

$$
m = 0, 1, \dots , M - 1, \tag {C41}
$$

$$
Y _ {z, m} ^ {\mathrm {a t}} \in \{0, 1 \}, \quad \forall z = 0, 1, \dots , N + 1,
$$

$$
m = 0, 1, \dots , M - 1. \tag {C4m}
$$

In order of appearance, the constraints have the following meaning. Constraint (C4c) requires that if we have reached slot m by position $z ,$ then it must be the case that we have reached slot m by position $z + 1$ . Constraint (C4d) requires that if we have reached slot $m + 1$ by position z, then we must have reached slot m by position z. Constraints (C4e) and (C4f) link the $Y ^ { \mathrm { b y } }$ and $Y ^ { \mathrm { a t } }$ variables; constraint (C4e) means that we are in slot m at position z if and only if we have reached slot m by position $\bar { z } \ ( Y _ { z , m } ^ { \mathrm { b y } } = 1 )$ and have not reached slot $m + 1$ by position z (Y z m,by $z ( Y _ { z . m + 1 } ^ { \mathsf { b y } } = 0 )$ . Constraint (C4f) similarly requires that we are in slot $M - 1$ at position z if and only if we have reached slot M − 1 by position z. Constraint $\mathrm { ( C 4 g ) }$ requires that the departure time from the target in position z is at least the slew time that is realized departing from the target in slot $z - 1$ plus the exposure time of the target in position z. Constraints (C4h)

and (C4i) ensure that the departure time of each position z is within the lower and upper bounds of that position’s assigned slot, while constraints (C4j) and (C4k) ensure that the departure time from each position $z \in \{ 1 , . . . , N \}$ is within the rise and set times for the target in that position $( t _ { \sigma ( z ) } ^ { e }$ and $t _ { \sigma ( z ) } ^ { \ell }$ , respectively). ( ) The last two constraints enforce that the $Y ^ { \mathrm { a t } }$ ( ) and $Y ^ { \mathrm { b } \hat { \mathbf { y } } }$ variables are binary.

The MILP problem (C4) is essentially the TTP problem of Section 2, restricted to a particular sequence σ. Essentially, this formulation decides when each target’s departure time will be and to what slots the different positions in the sequence will be allocated. Importantly, the sequence of targets is not a decision variable as it is in the original TTP model; it is a fixed input that is provided by the user.

Many of the constraints are direct analogs of constraints that appear in the TTP-Global formulation. For example, (C4j) and (C4k) model the rise and set time constraints for each target in each position, mirroring constraint (9) of the TTP MILP. As another example, (C4i) and (C4h) model the lower and upper bounds of each slot, similarly to constraint (8). Note that because the sequence of targets is fixed, many of the constraints from the full TTP MILP can be simplified, and other decisions, such as the departure times and in which slot each target is being departed from, can be expressed more efficiently using different decision variables. Specifically, the decision of which slot each position is assigned to is captured by the $Y _ { z , m } ^ { \mathrm { b y } }$ decision variables. Here, we remark that these variables are an example of the incremental encoding technique in integer programming, which enhances the efficiency of branching in the branch-andbound algorithm, and which is the cornerstone of integer programming solvers. We refer interested readers to the review paper of Vielma (2015), and to Bertsimas et al. (2011, 2019) and Mišić (2020) for examples of applications of this technique in air traffic control, vehicle routing and optimization over trained machine-learning models.

As a result, problem (C4) is much easier to solve than the full TTP MILP. We found that that Gurobi could determine the exact optimal solution to this problem in under a second with a single thread.

# C.3. Feasibility Algorithm

The local search approach described above may fail if it initialized at an infeasible sequence whose neighbors are also all infeasible. In order for Algorithm 1 to return a sequence that can be implemented, the initial sequence must be one for which the minimum slew problem (C4) is feasible. Given the combinatorical complexity of the TTP, it is unlikely that one would randomly select a target sequence that would result in problem (C4) being feasible.

Thus motivated, we present in this section an algorithm that, starting from any sequence, seeks to return a feasible sequence. We note that this algorithm is a heuristic, and is not guaranteed to succeed. Nevertheless, our numerical results in Section C.4 indicate that this heuristic is generally very effective.

At a very high level, the algorithm we will propose resembles our local search procedure, Algorithm 1, in that it starts from a sequence $\sigma$ and makes moves to neighboring sequences. The key difference is the objective function that is used. Instead of using the function $F ,$ the feasibility algorithm first seeks to locally optimize a function $G _ { 1 } ,$ , followed by a function $G _ { 2 }$ . The function $G _ { 1 } ( \sigma )$ measures, for the sequence $\sigma ,$

the smallest violation of the slot window constraints (C4h) and (C4i) that can be attained when we choose the departure times and the slots to which each target is assigned to. This violation is a nonnegative quantity; a positive value implies that we are unable to satisfy all of the constraints, i.e., at least one constraint in constraint sets (C4h) and (C4i) is violated. A value of zero implies that all of the constraints in the two constraint sets are satisfied. The function $G _ { 2 } ( \sigma )$ similarly measures the smallest possible violation of the visibility constraints (C4j) and (C4k) when we choose the departure times and the slots. Again, a positive value implies that at least one constraint in the constraint sets (C4j) and (C4k) is violated, while a value of zero implies we can satisfy all of the constraints defined by (C4j) and (C4k).

$G _ { 1 }$ is defined by the following MILP:

$$
\text {m i n i m i z e} \quad \sum_ {z = 0} ^ {N + 1} \epsilon_ {z} ^ {\text {s l o t , e}} + \sum_ {z = 0} ^ {N + 1} \epsilon_ {z} ^ {\text {s l o t ,} \ell} \tag {C5a}
$$

$$
\text {s u b j e c t} Y _ {0, 0} ^ {\text {b y}} = 1, \tag {C5b}
$$

$$
\begin{array}{l} Y _ {z, m} ^ {\text {b y}} \leqslant Y _ {z + 1, m} ^ {\text {b y}}, \quad \forall z \\ = 0, 1, \dots , N, m = 0, 1, \dots , M - 1, \tag {C5c} \\ \end{array}
$$

$$
\begin{array}{l} Y _ {z, m + 1} ^ {\mathrm {b y}} \leqslant Y _ {z, m} ^ {\mathrm {b y}}, \forall z \\ = 0, 1, \dots , N + 1, m = 0, 1, \dots , M - 2, \tag {C5d} \\ \end{array}
$$

$$
Y _ {z, m} ^ {\mathrm {a t}} = Y _ {z, m} ^ {\mathrm {b y}} - Y _ {z, m + 1} ^ {\mathrm {b y}},
$$

$$
\forall z = 0, 1, \dots , N + 1, m = 0, 1, \dots , M - 2, \quad \left(\mathrm {C} 5 \mathrm {e}\right)
$$

$$
Y _ {z, M - 1} ^ {\mathrm {a t}} = Y _ {z, M - 1} ^ {\mathrm {b y}}, \quad \forall z = 0, 1, \dots , N + 1, \tag {C5f}
$$

$$
\begin{array}{l} t _ {z} \geqslant t _ {z - 1} + \sum_ {m = 0} ^ {M - 1} \tau_ {\sigma (z - 1), \sigma (z), m} ^ {\mathrm {s l e w}} \cdot Y _ {z - 1, m} ^ {\mathrm {a t}} + \tau_ {\sigma (z)} ^ {\mathrm {e x p}}, \\ \forall z = 1, 2, \dots , N + 1, \tag {C5g} \\ \end{array}
$$

$$
t _ {z} \geqslant \sum_ {m = 0} ^ {M - 1} w _ {m} \cdot Y _ {z, m} ^ {\mathrm {a t}} - \epsilon_ {z} ^ {\mathrm {s l o t , e}}, \quad \forall z = 0, 1, \dots , N + 1, \tag {C5h}
$$

$$
t _ {z} \leqslant \sum_ {m = 0} ^ {M - 1} w _ {m + 1} \cdot Y _ {z, m} ^ {\mathrm {a t}} + \epsilon_ {z} ^ {\mathrm {s l o t}, \ell}, \quad \forall z = 0, 1, \dots , N + 1, \tag {C5i}
$$

$$
t _ {z} \geqslant t _ {\sigma (z)} ^ {e} - \epsilon_ {z} ^ {\mathrm {e}}, \quad \forall z = 0, 1, \dots , N + 1, \tag {C5j}
$$

$$
t _ {z} \leqslant t _ {\sigma (z)} ^ {\ell} + \epsilon_ {z} ^ {\ell}, \quad \forall z = 0, 1, \dots , N + 1, \tag {C5k}
$$

$$
Y _ {z, m} ^ {\text {b y}} \in \{0, 1 \}, \forall z = 0, 1, \dots , N + 1, m = 0, 1, \dots , M - 1, \tag {C51}
$$

$$
Y _ {z, m} ^ {\mathrm {a t}} \in \{0, 1 \}, \forall z = 0, 1, \dots , N + 1, m = 0, 1, \dots , M - 1, \tag {C5m}
$$

$$
\begin{array}{l} \epsilon_ {z} ^ {\mathrm {e}}, \epsilon_ {z} ^ {\ell}, \epsilon_ {z} ^ {\text {s l o t}, \ell}, \epsilon_ {z} ^ {\text {s l o t}, \mathrm {e}} \geqslant 0, \quad \forall z = 0, 1, \dots , N + 1. \\ \end{array} \tag {C5n}
$$

Observe that this integer program is similar to the minimum slew problem (C4), except that we now allow for violations of the constraints (C4h), (C4i), (C4j), and (C4k). The main modifications are as follows. First, observe that in addition to the decision variables of problem (C4), problem (C5) includes the decision variables $\epsilon _ { z } ^ { \mathrm { e } } , \epsilon _ { z } ^ { \ell } , \epsilon _ { z } ^ { \mathrm { s 1 o t } , \ell } , \epsilon _ { z } ^ { \bar { \mathrm { s 1 o t } } , \mathrm { e } }$  z  ,  slot e, which measure z

how much the rise, set, slot upper bound, and slot lower bound constraints can be violated in time.

Second, observe that constraints (C5h)–(C5k) resemble constraints (C4h)–(C4k), except that the new $\epsilon _ { z } ^ { \mathrm { e } } , \epsilon _ { z } ^ { \ell } ,$ $\epsilon _ { z } ^ { \mathrm { s 1 o t } , \ell } , \epsilon _ { z } ^ { \mathrm { s 1 o t } , \mathrm { e } }$ E appear.These newdecision variables areounded from below by zero and unbounded from above, so they effectively allow the optimizer to choose to not satisfy these constraints. For example, in the constraint $t _ { z } \leqslant t _ { \sigma ( z ) } ^ { \ell } + \dot { \epsilon } _ { z } ^ { \ell } ,$ for whatever value of $t _ { z }$ we choose we can always make the constraint satisfied by setting $\epsilon _ { z } ^ { \ell }$ to be equal to any value greater than max $\{ 0 , t _ { z } - t _ { \sigma ( z ) } ^ { \ell } \} ;$ ; as a concrete example, if $t _ { z } ~ = ~ 1 2 0$ and $t _ { \sigma ( z ) } ^ { \ell } = 8 0$ , then any $\epsilon _ { z } ^ { \ell } \geqslant \operatorname* { m a x } \{ 1 2 0 - 8 0 , 0 \} = 4 0$ will satisfy the constraint.

Laof the fi $\epsilon _ { z } ^ { \mathsf { { s 1 0 t } , \ell } }$ serveand $\epsilon _ { z } ^ { \mathsf { s 1 0 t , e } }$ e objective function is equal to the sumvariables. Thus, the optimizer seeks to departure times so as to minimize how much the slot lower and upper bound constraints from problem (C4) are violated. Observe that if the optimal objective value of problem (C5) is zero, then we have found a partially feasible solution to problem (C4) that satisfies all of the constraints, and in particular constraints (C4h) and (C4i), with the possible exception of the rise and set time constraints (C4j) and (C4k). Importantly, note that no matter what sequence σ one chooses, problem (C5) is always feasible.

We now define the function $G _ { 2 } .$ . The function $G _ { 2 }$ is defined as the objective value of the following integer program, which is

$$
\text {m i n i m i z e} \quad \sum_ {z = 0} ^ {N + 1} \epsilon_ {z} ^ {\mathrm {e}} + \sum_ {z = 0} ^ {N + 1} \epsilon_ {z} ^ {\ell} \tag {C6a}
$$

$\mathrm { s u b j e c t ~ t o ~ c o n s t r a i n t s } ( \mathbf { C } 5 \mathbf { b } ) - \mathbf { ( C } 5 0 ) ,$ C6b  ( )

$$
\epsilon_ {z} ^ {\text {s l o t , e}} = 0, \quad \forall z = \{0, 1, \dots , N + 1 \}, \tag {C6c}
$$

$$
\epsilon_ {z} ^ {\text {s l o t}, \ell} = 0, \quad \forall z = \{0, 1, \dots , N + 1 \}. \tag {C6d}
$$

Problem (C6) has the same structure as problem (C5), except that we force the violation variables $\epsilon _ { z } ^ { \mathrm { s 1 o t , e } } \mathrm { a n d } \epsilon _ { z } ^ { \mathrm { s 1 o t , \ell } }$ to zero; thus, we no longer allow for violations of the slot bound constraints (C4h) and (C4i). We do still allow for violations of the rise and set time constraints (C4j) and (C4k). The objective function measures how much the rise and set time constraints are violated. Observe that if the objective value of problem (C6) is zero, then we have exactly verified that the minimum slew time MILP (C4) is feasible.

With problems (C5) and (C6) defined, we can now define the feasibility algorithm, which we provide in Algorithm 2. This algorithm works by first performing local search using the function $G _ { 1 }$ . If the local optimum is such that the value of $G _ { 1 }$ is positive, then the algorithm terminates and returns that the problem is infeasible. Otherwise, if the value of $G _ { 1 }$ is zero, then we continue to the next phase, in which we perform local search using the function $G _ { 2 }$ . If the local optimum of $G _ { 2 }$ is positive, then the algorithm again terminates and returns that the problem is infeasible. Otherwise, if the value of $G _ { 2 }$ is zero, then we have identified a feasible sequence. Note that Algorithm 2 is a heuristic and does not provably verify that problem (C4) is infeasible. If it returns “Problem is infeasible,” it may not be the case that the minimum slew problem is actually infeasible.

Algorithm 2. Pseudo-code of feasibility procedure.   
Require: Initial sequence $\sigma \in \Sigma$ 1: {Phase 1: Minimization of $G_{1}$ (violation of slot lower and upper bound constraints)}   
3: Set $\mathcal{U}\gets \{1,\dots ,N\}$ 3: while $|\mathcal{U}| > 0$ do   
4: Select $z\in \mathcal{U}$ ; set $\mathcal{U}\gets \mathcal{U}\backslash \{z\}$ 5: Calculate $\sigma^{*}\gets \mathrm{argmin}_{\sigma^{\prime}\in \mathcal{N}_{z}(\sigma)}G_{1}(\sigma^{\prime})$ 6: Calculate $G_{1}^{\prime}\gets \min_{\sigma^{\prime}\in \mathcal{N}_{z}(\sigma)}G_{1}(\sigma^{\prime})$ 7: if $G_{1}^{\prime} <   G_{1}(\sigma)$ then   
8: Set $\sigma \gets \sigma^{*}$ 9: Set $\mathcal{U}\gets \{1,\dots ,z - 1,z + 1,\dots ,N\}$ 10: end if 11:end while   
12: if $G_{1}(\sigma) > 0$ then   
13: return Problem is infeasible.   
14:else   
15:Phase 2: Minimization of $G_{2}$ (violation of rise and set time constraints)   
16: Set $\mathcal{U}\gets \{1,\dots ,N\}$ 17: while $|\mathcal{U}| > 0$ do   
18: Select $z\in \mathcal{U}$ ; set $\mathcal{U}\gets \mathcal{U}\backslash \{z\}$ 19: Calculate $\sigma^{*}\gets \mathrm{argmin}_{\sigma^{\prime}\in \mathcal{N}_{z}(\sigma)}G_{2}(\sigma^{\prime})$ 20: Calculate $G_{2}^{\prime}\gets \min_{\sigma^{\prime}\in \mathcal{N}_{z}(\sigma)}G_{2}(\sigma^{\prime})$ 21: if $G_{2}^{\prime} <   G_{2}(\sigma)$ then   
22: Set $\sigma \gets \sigma^{*}$ 23: Set $\mathcal{U}\gets \{1,\dots ,z - 1,z + 1,\dots ,N\}$ 24:end if   
25:end while   
26:if $G_{2}(\sigma) > 0$ then   
27:return Problem is infeasible.   
28:else   
29:return Feasible sequence $\sigma$ 30:end if   
31:end if

# C.4. Computational Results for Local Search Heuristic

We now present our results on our heuristic approach described above. We tested our approach on the same collection of 360 experiments described in Section 3.2, and compute the same result metrics. We tested two variants of our local search procedure:

1. TTP-LS-1: Here, we execute our overall algorithm from a single random starting point, which we obtain by drawing a sequence σ uniformly at random from all possible N! sequences.   
2. TTP-LS-10: In the second variant, we execute our overall algorithm from 10 randomly generating starting points, each of which is a uniformly randomly generated sequence, and retain the best solution obtained over the 10 repetitions.

With both TTP-LS-1 and TTP-LS-10, we impose a time limit of 600 s on the total runtime. In the most extreme case, TTP-LS-1 will require 600 s, while TTP-LS-10 will require 600 × 10 = 6000 s. In both variants, the functions $G _ { 1 }$ and $G _ { 2 }$ (see Appendix C.3) and F (see Appendix C.2) are computed by solving the corresponding MILPs using Gurobi with a single thread. We again implement our procedure in Python and run our experiments on the same Amazon EC2 instance described in Section 3.2.

Table 3 summarizes the results for TTP-LS-1 and Figure 5 shows runtime and slew efficiency for different problem sizes. TTP-LS-1 exhibits favorable performance in terms of

computation time; in most cases, TTP-LS-1 terminates with a locally optimal solution within 600 s. The only exception is the $( D , N , M ) = ( { \mathrm { F u l l } } , 1 0 0 ,$ 10) set of instances. Note that TTP-LS-1 resulted in a feasible schedule in all but seven of the 360 instances; importantly, TTP-LS-1 finds a feasible schedule in all of the instances for parameter combinations for which the TTP-Global MILP fails (e.g., for (Full, 100, 10), TTP-LS-1 produces a feasible schedule in all 10 instances in 600 s, whereas TTP-Global fails to find a feasible schedule in all 10 instances with 1800 s of computation). Of those seven instances in which TTP-LS-1 did not find a feasible schedule, six are the same instances which were determined to be infeasible by TTP-Global, and in one instance the feasibility procedure (Algorithm 2) failed to identify a feasible solution, despite the fact that the instance does admit a feasible solution based on running TTP-Global. Lastly, in terms of solution quality, the total slew time, as measured by SlewTimeτ and SlewTimereal, compares favorably to the worst-case bound of 2N.

In the most significant case, with N = 100 targets, TTP-LS-1 obtains schedules with total slew times that achieve a reduction of approximately 80% relative to the 2N bound.

Table 4 and Figure 5 present analogous results for TTP-LS-10.

We found that the TTP-LS-10 schedules were signficantly more efficient than the TTP-LS-1 schedules. For example, for (Full, 100, 1), SlewTimeτ is 32.6 minutes for TTP-LS-10, compared to 43.7 minutes for TTP-LS-1.

In cases where the TTP-Global returned an optimal schedule, this schedule was often much more efficient than TTP-LS-10 and TTP-LS-1. For example, for (Full, 50, 1), the TTP-Global MILP was solved to full optimality in seven out of 10 instances, and the average SlewTimeτ was 13.2 minutes, compared to 27.6 minutes for TTP-LS-1 and 19.9 minutes for TTP-LS-10. TTP-LS-10 and TTP-LS-1 do not guarantee a globally optimal solution, but the gap between local and global optima suggests additional work on heuristic solutions could prove fruitful.

On the other hand, in cases where the TTP-Global MILP does not terminate with an optimal solution, it is possible for the local search solution to perform better. For example, for the (D, N, M) = (Half, 25, 10) experiments, the TTP-LS-10 solution has an average SlewTimeτ of 10.8 minutes compared to 12.7 minutes for TTP-Global. Lastly, the computation time for TTP-LS-10 is roughly 10 times that of TTP-LS-1, as one would expect. However, we note that the 10 repetitions are independent, and could be carried out in parallel. This could be attractive from an implementation standpoint, as both TTP-LS-1 and TTP-LS-10 were executed with a single thread, so one could easily execute the local search procedure from multiple starting points in parallel within a multithreaded computing environment.

There are several key takeaways from Figure 5 when D = Full. Adopting static target-to-target slew overheads (M = 1), we find TTP-Global solves the schedule for N up to 100 in most runs. TTP-Global produces the highest $\mathtt { R e l R e d } _ { \mathtt { r e a l } }$ improvement of above 80% for the N = 100 case. For smaller cases of N, it sees some benefit from higher values of M, but cannot find feasible solutions in the time limit for large N. The local solvers TTP-LS-1 and TTP-LS-10 scale exponentially with N, and find local optima for all N in their expected time limits. $\mathtt { R e l R e d } _ { \mathtt { r e a l } }$ benefits

Table 3 Computational Results for TTP-LS-1 Procedure   

<table><tr><td>D</td><td>N</td><td>M</td><td>NumFeas</td><td>Runtime (s)</td><td>SlewTimeτ (min)</td><td>RelRedτ (%)</td><td>SlewTime real (min)</td><td>RelRed real (%)</td></tr><tr><td>Quarter</td><td>5</td><td>1</td><td>10</td><td>0.0</td><td>4.3</td><td>57.1</td><td>6.1</td><td>38.6</td></tr><tr><td>Quarter</td><td>5</td><td>3</td><td>10</td><td>0.0</td><td>4.4</td><td>56.3</td><td>5.9</td><td>40.7</td></tr><tr><td>Quarter</td><td>5</td><td>10</td><td>10</td><td>0.1</td><td>4.1</td><td>58.7</td><td>5.8</td><td>41.8</td></tr><tr><td>Quarter</td><td>10</td><td>1</td><td>10</td><td>0.1</td><td>7.7</td><td>61.3</td><td>11.1</td><td>44.6</td></tr><tr><td>Quarter</td><td>10</td><td>3</td><td>10</td><td>0.1</td><td>7.3</td><td>63.6</td><td>10.7</td><td>46.5</td></tr><tr><td>Quarter</td><td>10</td><td>10</td><td>10</td><td>0.6</td><td>7.1</td><td>64.7</td><td>10.7</td><td>46.6</td></tr><tr><td>Quarter</td><td>25</td><td>1</td><td>10</td><td>1.5</td><td>14.3</td><td>71.5</td><td>19.4</td><td>61.2</td></tr><tr><td>Quarter</td><td>25</td><td>3</td><td>10</td><td>3.5</td><td>13.7</td><td>72.5</td><td>20.8</td><td>58.4</td></tr><tr><td>Quarter</td><td>25</td><td>10</td><td>10</td><td>24.3</td><td>13.9</td><td>72.2</td><td>21.7</td><td>56.7</td></tr><tr><td>Half</td><td>5</td><td>1</td><td>10</td><td>0.0</td><td>5.4</td><td>45.9</td><td>6.8</td><td>32.4</td></tr><tr><td>Half</td><td>5</td><td>3</td><td>10</td><td>0.0</td><td>4.8</td><td>51.8</td><td>5.9</td><td>40.7</td></tr><tr><td>Half</td><td>5</td><td>10</td><td>10</td><td>0.1</td><td>4.6</td><td>53.6</td><td>6.0</td><td>40.4</td></tr><tr><td>Half</td><td>10</td><td>1</td><td>10</td><td>0.1</td><td>7.9</td><td>60.6</td><td>13.2</td><td>33.8</td></tr><tr><td>Half</td><td>10</td><td>3</td><td>10</td><td>0.1</td><td>7.7</td><td>61.5</td><td>11.8</td><td>40.8</td></tr><tr><td>Half</td><td>10</td><td>10</td><td>10</td><td>0.4</td><td>7.2</td><td>64.0</td><td>11.8</td><td>41.0</td></tr><tr><td>Half</td><td>25</td><td>1</td><td>10</td><td>1.1</td><td>15.9</td><td>68.3</td><td>22.6</td><td>54.9</td></tr><tr><td>Half</td><td>25</td><td>3</td><td>10</td><td>2.7</td><td>13.1</td><td>73.8</td><td>21.7</td><td>56.6</td></tr><tr><td>Half</td><td>25</td><td>10</td><td>10</td><td>11.1</td><td>13.4</td><td>73.2</td><td>20.8</td><td>58.4</td></tr><tr><td>Half</td><td>50</td><td>1</td><td>10</td><td>11.8</td><td>23.1</td><td>76.9</td><td>36.9</td><td>63.1</td></tr><tr><td>Half</td><td>50</td><td>3</td><td>10</td><td>30.4</td><td>20.3</td><td>79.7</td><td>35.5</td><td>64.5</td></tr><tr><td>Half</td><td>50</td><td>10</td><td>10</td><td>167.4</td><td>22.5</td><td>77.5</td><td>35.0</td><td>65.0</td></tr><tr><td>Full</td><td>5</td><td>1</td><td>9</td><td>0.0</td><td>6.2</td><td>37.6</td><td>6.6</td><td>34.4</td></tr><tr><td>Full</td><td>5</td><td>3</td><td>9</td><td>0.0</td><td>5.7</td><td>43.1</td><td>7.2</td><td>27.5</td></tr><tr><td>Full</td><td>5</td><td>10</td><td>9</td><td>0.0</td><td>5.5</td><td>44.6</td><td>7.0</td><td>30.0</td></tr><tr><td>Full</td><td>10</td><td>1</td><td>8</td><td>0.1</td><td>10.0</td><td>49.9</td><td>16.4</td><td>17.9</td></tr><tr><td>Full</td><td>10</td><td>3</td><td>9</td><td>0.1</td><td>9.5</td><td>52.6</td><td>11.7</td><td>41.5</td></tr><tr><td>Full</td><td>10</td><td>10</td><td>9</td><td>0.5</td><td>8.5</td><td>57.4</td><td>11.3</td><td>43.5</td></tr><tr><td>Full</td><td>25</td><td>1</td><td>10</td><td>1.2</td><td>17.5</td><td>65.0</td><td>27.7</td><td>44.7</td></tr><tr><td>Full</td><td>25</td><td>3</td><td>10</td><td>2.2</td><td>17.0</td><td>66.0</td><td>23.5</td><td>53.0</td></tr><tr><td>Full</td><td>25</td><td>10</td><td>10</td><td>6.8</td><td>14.4</td><td>71.2</td><td>20.3</td><td>59.5</td></tr><tr><td>Full</td><td>50</td><td>1</td><td>10</td><td>11.3</td><td>27.6</td><td>72.4</td><td>41.9</td><td>58.1</td></tr><tr><td>Full</td><td>50</td><td>3</td><td>10</td><td>23.1</td><td>23.2</td><td>76.8</td><td>34.7</td><td>65.3</td></tr><tr><td>Full</td><td>50</td><td>10</td><td>10</td><td>76.2</td><td>23.3</td><td>76.7</td><td>33.9</td><td>66.1</td></tr><tr><td>Full</td><td>100</td><td>1</td><td>10</td><td>98.7</td><td>43.7</td><td>78.2</td><td>63.6</td><td>68.2</td></tr><tr><td>Full</td><td>100</td><td>3</td><td>10</td><td>321.6</td><td>37.0</td><td>81.5</td><td>63.9</td><td>68.0</td></tr><tr><td>Full</td><td>100</td><td>10</td><td>10</td><td>602.0</td><td>38.7</td><td>80.6</td><td>62.6</td><td>68.7</td></tr></table>

from higher M for moderate values of N, but also has diminishing returns for N = 100 and a lower ceiling compared to the global solution. Local search is equipped to find

feasible solutions to larger models, but struggles to find solutions near the global optimum at high N, regardless of the value of M.

![](images/e27729bc20c0be274e32fddfa4d8ea0f125796d0cc09f405ab8f2042dda7e715.jpg)

![](images/665b42c69b19b8e464f5008f3162b8b8d18bbb21cb5c299723c8ff2a2b44a01c.jpg)

![](images/3c906b91ec1e8462e95fd1504cc40d89c78e14d13bb455a6343c14736d501601.jpg)

![](images/aecbe4db8074b592033151a3b53b68fadfba2dd567fa8f9bf69e17aeac4de645.jpg)

![](images/c8f2aab73c768b9c9e3051eed2f36ce20b273bdd2e6a5ec57c122b2dc9efd32d.jpg)

![](images/16b71c3d64b9d32f81efe51edfa0368e7495d5e3549c87566b649262d877dd50.jpg)

![](images/536dfc3f6b306af3dff7073030f58ea073c50da3660365bdd35c7f10ca34c66f.jpg)

![](images/96177cad5a7b6ac9701533468559476bbd108b797c14819a12b9681827f72b95.jpg)

![](images/52a33739b386b9a4cf223ddfa1e99641ceb58c05f9cda6e931eb440edb62b46c.jpg)

![](images/9fd378e570f5085f4ebbf3ebcd04c5822b139b34fb87cc855540fe0ad40d4ee8.jpg)

![](images/11b11b24bff889798989810d8561c7a4ce99e428112606f8ae7796d0efd27de0.jpg)

![](images/538d0129cad1cd6ece5ca65f5f969f0b35784a1cb70cc8bdbd845edfbf350867.jpg)

![](images/87d549a79b788326185e6f3aab7d11f4e536f6551f4fc3fdbac0f880d03cdb5f.jpg)

![](images/7b3943bb0cceda48a4a322f599589ae83fd52d39f679d41c792d69ddf052e3e3.jpg)

![](images/4f1898789fe981b144426f1870a65e68781019132a5e45d114e8836922e4f769.jpg)

![](images/ac2f239949a283c3652522383dffc97e54a8a15bbf9d2a77147cc0b6a98651e5.jpg)

![](images/778e199571f11bfa235432b2d93cb9dcca6d8d18c2999b3f4daba267822f45db.jpg)

![](images/468158a9b171170aa259acb6882b815049fcb603bf9a62d49e3e84bafd1a6ce6.jpg)  
Figure 5. Runtime and $\mathtt { R e l R e d } _ { \mathtt { r e a l } }$ for each duration type D, as found in Tables 1, 3, and 4. The first two rows summarize these statistics for the $D = { \mathrm { Q u a r t e r } }$ simulations, the next two for $D = { \mathrm { H a l f } } .$ , and the bottom two for $D = \mathrm { F u l l }$ . The top row in each pair shows the average Runtime (and optimal subset, for TTP-Global) across all runs for D with varying M as a function of N. The bottom row in each pair shows the average $\mathrm { R e 1 R e d _ { r e a l } }$ for the same values of D and M.

Table 4 Computational Results for TTP-LS-10 Procedure   

<table><tr><td>D</td><td>N</td><td>M</td><td>NumFeas</td><td>Runtime (s)</td><td>SlewTimeτ (min)</td><td>RelRedτ (%)</td><td>SlewTime real (min)</td><td>RelRed real (%)</td></tr><tr><td>Quarter</td><td>5</td><td>1</td><td>10</td><td>0.1</td><td>4.1</td><td>59.1</td><td>6.0</td><td>39.6</td></tr><tr><td>Quarter</td><td>5</td><td>3</td><td>10</td><td>0.2</td><td>3.7</td><td>63.3</td><td>5.3</td><td>47.2</td></tr><tr><td>Quarter</td><td>5</td><td>10</td><td>10</td><td>0.5</td><td>3.5</td><td>64.5</td><td>5.1</td><td>48.9</td></tr><tr><td>Quarter</td><td>10</td><td>1</td><td>10</td><td>0.8</td><td>5.8</td><td>70.9</td><td>9.3</td><td>53.7</td></tr><tr><td>Quarter</td><td>10</td><td>3</td><td>10</td><td>1.3</td><td>5.8</td><td>71.2</td><td>9.0</td><td>55.0</td></tr><tr><td>Quarter</td><td>10</td><td>10</td><td>10</td><td>5.2</td><td>5.5</td><td>72.6</td><td>8.8</td><td>55.9</td></tr><tr><td>Quarter</td><td>25</td><td>1</td><td>10</td><td>13.2</td><td>10.2</td><td>79.7</td><td>16.7</td><td>66.7</td></tr><tr><td>Quarter</td><td>25</td><td>3</td><td>10</td><td>36.1</td><td>9.9</td><td>80.2</td><td>16.3</td><td>67.5</td></tr><tr><td>Quarter</td><td>25</td><td>10</td><td>10</td><td>214.4</td><td>9.6</td><td>80.8</td><td>14.8</td><td>70.3</td></tr><tr><td>Half</td><td>5</td><td>1</td><td>10</td><td>0.1</td><td>4.9</td><td>50.8</td><td>7.4</td><td>25.8</td></tr><tr><td>Half</td><td>5</td><td>3</td><td>10</td><td>0.2</td><td>4.7</td><td>53.2</td><td>6.8</td><td>32.1</td></tr><tr><td>Half</td><td>5</td><td>10</td><td>10</td><td>0.5</td><td>4.4</td><td>55.5</td><td>6.3</td><td>37.1</td></tr><tr><td>Half</td><td>10</td><td>1</td><td>10</td><td>0.8</td><td>6.6</td><td>67.2</td><td>11.8</td><td>41.1</td></tr><tr><td>Half</td><td>10</td><td>3</td><td>10</td><td>1.3</td><td>6.0</td><td>70.1</td><td>9.5</td><td>52.6</td></tr><tr><td>Half</td><td>10</td><td>10</td><td>10</td><td>4.4</td><td>5.8</td><td>71.0</td><td>9.7</td><td>51.7</td></tr><tr><td>Half</td><td>25</td><td>1</td><td>10</td><td>12.1</td><td>11.2</td><td>77.7</td><td>19.8</td><td>60.3</td></tr><tr><td>Half</td><td>25</td><td>3</td><td>10</td><td>26.0</td><td>10.8</td><td>78.4</td><td>18.5</td><td>63.0</td></tr><tr><td>Half</td><td>25</td><td>10</td><td>10</td><td>118.6</td><td>10.8</td><td>78.5</td><td>18.8</td><td>62.4</td></tr><tr><td>Half</td><td>50</td><td>1</td><td>10</td><td>113.1</td><td>19.1</td><td>80.9</td><td>36.3</td><td>63.7</td></tr><tr><td>Half</td><td>50</td><td>3</td><td>10</td><td>330.3</td><td>16.7</td><td>83.3</td><td>30.0</td><td>70.0</td></tr><tr><td>Half</td><td>50</td><td>10</td><td>10</td><td>2003.9</td><td>17.0</td><td>83.0</td><td>26.8</td><td>73.2</td></tr><tr><td>Full</td><td>5</td><td>1</td><td>9</td><td>0.1</td><td>6.0</td><td>39.7</td><td>6.8</td><td>31.6</td></tr><tr><td>Full</td><td>5</td><td>3</td><td>9</td><td>0.2</td><td>5.3</td><td>47.0</td><td>7.3</td><td>27.1</td></tr><tr><td>Full</td><td>5</td><td>10</td><td>9</td><td>0.5</td><td>5.3</td><td>47.3</td><td>7.0</td><td>29.5</td></tr><tr><td>Full</td><td>10</td><td>1</td><td>9</td><td>0.9</td><td>8.8</td><td>56.2</td><td>13.3</td><td>33.3</td></tr><tr><td>Full</td><td>10</td><td>3</td><td>9</td><td>1.4</td><td>7.7</td><td>61.7</td><td>9.4</td><td>52.9</td></tr><tr><td>Full</td><td>10</td><td>10</td><td>9</td><td>4.5</td><td>6.5</td><td>67.5</td><td>9.5</td><td>52.4</td></tr><tr><td>Full</td><td>25</td><td>1</td><td>10</td><td>12.2</td><td>12.2</td><td>75.5</td><td>23.2</td><td>53.6</td></tr><tr><td>Full</td><td>25</td><td>3</td><td>10</td><td>22.3</td><td>12.1</td><td>75.9</td><td>20.0</td><td>60.1</td></tr><tr><td>Full</td><td>25</td><td>10</td><td>10</td><td>65.4</td><td>11.4</td><td>77.1</td><td>18.4</td><td>63.2</td></tr><tr><td>Full</td><td>50</td><td>1</td><td>10</td><td>109.2</td><td>19.9</td><td>80.1</td><td>33.0</td><td>67.0</td></tr><tr><td>Full</td><td>50</td><td>3</td><td>10</td><td>224.9</td><td>19.5</td><td>80.5</td><td>27.5</td><td>72.5</td></tr><tr><td>Full</td><td>50</td><td>10</td><td>10</td><td>842.0</td><td>17.9</td><td>82.1</td><td>26.8</td><td>73.2</td></tr><tr><td>Full</td><td>100</td><td>1</td><td>10</td><td>1052.1</td><td>32.6</td><td>83.7</td><td>58.8</td><td>70.6</td></tr><tr><td>Full</td><td>100</td><td>3</td><td>10</td><td>2852.0</td><td>29.8</td><td>85.1</td><td>54.1</td><td>72.9</td></tr><tr><td>Full</td><td>100</td><td>10</td><td>10</td><td>6025.6</td><td>32.3</td><td>83.8</td><td>55.3</td><td>72.4</td></tr></table>

# ORCID iDs

Luke B. Handley https://orcid.org/0000-0002-9305-5101

Erik A. Petigura https://orcid.org/0000-0003-0967-2893

Velibor V. Mišić https://orcid.org/0000-0002-8952-5617

# References

Astropy Collaboration, Price-Whelan, A. M., Sipőcz, B. M., et al. 2018, AJ, 156, 123   
Astropy Collaboration, Robitaille, T. P., Tollerud, E. J., et al. 2013, A&A, 558, A33   
Bellm, E. C., Kulkarni, S. R., Barlow, T., et al. 2019a, PASP, 131, 068003   
Bellm, E. C., Kulkarni, S. R., Graham, M. J., et al. 2019b, PASP, 131, 018002   
Bertsimas, D., Chang, A., Mišić, V. V., & Mundru, N. 2019, Transp. Sci., 53, 773   
Bertsimas, D., Lulli, G., & Odoni, A. 2011, OR, 59, 211   
Croes, G. A. 1958, OR, 6, 791   
Giuliano, M., & Johnston, M. 2008, ICAPS'08: Proc. Eighteenth Int. Conf.   
Automated Planning and Scheduling (New York: ACM), 107

Gurobi Optimization, LLC 2023, Gurobi Optimizer Reference Manual, https://www.gurobi.com   
Harris, C. R., Millman, K. J., van der Walt, S. J., et al. 2020, Natur, 585, 357   
Howard, A. W., Johnson, J. A., Marcy, G. W., et al. 2010, ApJ, 721, 1467 Hunter, J. D. 2007, CSE, 9, 90   
Ivezić, Ž., Kahn, S. M., Tyson, J. A., et al. 2019, ApJ, 873, 111   
Johnston, M. D., & Miller, G. E. 1994, Comput. Sci. Engin., 1994, 15640568   
Lampoudi, S., Saunders, E., & Eastman, J. 2015, arXiv:1503.07170   
Mišić, V. V. 2020, OR, 68, 1605   
pandas development team, T 2020, pandas-dev/pandas: Pandas, v1.4.1, Zenodo, doi:10.5281/zenodo.3509134   
Parazin, B., Coughlin, M. W., Singer, L. P., Gupta, V., & Anand, S. 2022, ApJ, 935, 87   
Rosenthal, L. J., Fulton, B. J., Hirsch, L. A., et al. 2021, ApJS, 255, 8   
Solar, M., Michelon, P., Avarias, J., & Garces, M. 2016, A&C, 15, 90   
Sun, P., Veelenturf, L., Hewitt, M., & Van Woensel, T. 2018, Transport. Res. B: Meth., 116, 1   
Vielma, J. P. 2015, SIAMR, 57, 3