---
title: "Combinatorial optimization by weight annealing in memristive hopfeld networks"
authors:
  - "Z. Fahimi"
  - "M. R. Mahmoodi"
  - "H. Nili"
  - "Valentin Polishchuk"
  - "D. B. Strukov"
date: "2021-08-12"
year: "2021"
journal: "Scientific Reports"
abstract: "The Hopfield neural network is a powerful framework for solving combinatorial optimization\\"
abstract_cn: "Hopfield神经网络是解决组合优化问题的强大框架。我们提出了一种权重退火方法：初始将所有突触权重设为零使网络快速进入全局最小状态，然后逐渐引入权重使网络保持在基态附近。大量模拟表明权重退火在多个组合优化问题上平均能获得更好的解。作为概念验证，使用20x20\\"
keywords:
  - "[[Hopfield Network]]"
  - "[[Memristor]]"
  - "[[Combinatorial Optimization]]"
  - "[[Weight Annealing]]"
  - "[[忆阻器]]"
  - "[[组合优化]]"
cite: "Fahimi Z, Mahmoodi M R, Nili H, Polishchuk V, Strukov D B. Combinatorial Optimization\\"
aiSum: "本文提出权重退火方法用于忆阻器Hopfield网络的组合优化。初始权重为零使网络快速进入全局最小，逐渐引入权重保持基态。在TiO2 crossbar和eFlash阵列上实验验证了图划分和最大独立集问题。"
confidence: "medium"
wiki_concepts:
  - "[[Memristor]]"
---

OPEN

# Combinatorial optimization by weight annealing in memristive hopfeld networks

Z. Fahimi1,3*, M. R. Mahmoodi1,3*, H. Nili1 , Valentin Polishchuk2 & D. B. Strukov1

![](images/6657ba50ade556d27d55f4c6fb28beb3b807cdd2ee3c23e03b0ff2cc2f7f678d.jpg)

The increasing utility of specialized circuits and growing applications of optimization call for the development of efcient hardware accelerator for solving optimization problems. Hopfeld neural network is a promising approach for solving combinatorial optimization problems due to the recent demonstrations of efcient mixed-signal implementation based on emerging non-volatile memory devices. Such mixed-signal accelerators also enable very efcient implementation of various annealing techniques, which are essential for fnding optimal solutions. Here we propose a “weight annealing” approach, whose main idea is to ease convergence to the global minima by keeping the network close to its ground state. This is achieved by initially setting all synaptic weights to zero, thus ensuring a quick transition of the Hopfeld network to its trivial global minima state and then gradually introducing weights during the annealing process. The extensive numerical simulations show that our approach leads to a better, on average, solutions for several representative combinatorial problems compared to prior Hopfeld neural network solvers with chaotic or stochastic annealing. As a proof of concept, a 13-node graph partitioning problem and a 7-node maximum-weight independent set problem are solved experimentally using mixed-signal circuits based on, correspondingly, a 20× 20 analog-grade TiO2 memristive crossbar and a 12 × 10 eFlash memory array.

Combinational optimization is an essential subset of mathematical optimization methods with numerous applications in various !elds, including operation research, machine learning, and scienti!c computing1–3 . A typical goal of combinatorial optimization is to !nd an optimal solution within a !nite set of possible solutions. For example, graph partitioning, that is, the problem of minimizing the cutsize when partitioning a graph into two sections of nearly equal weight, !nds applications in distributed computing and digital VLSI design "ow.

For most combinatorial problems, the exhaustive brute-force search is o#en not practical, and developing e$cient heuristic and meta-heuristic methods is of utmost importance4,5 . %e enormous computational power required to solve large-scale optimization problems also poses a great challenge. %e problem is exacerbated by the sequential structure of general-purpose processors, which are very energy-demanding and ine$cient in running large-scale, massively parallel algorithms. Hence, hardware accelerators, e.g., based on superconductors6,7 , digital CMOS5,8,9 , nanomagnetic10, and photonic 11 technologies, are proposed to solve optimization problems using heuristic methods e$ciently.Hop!eld neural network (HNN)12–14 is also a heuristic method that extended the application of neural networks from classi!cation to optimization and associative memory. A particular class of recurrent HNNs is the discrete-time asynchronous model, which operates based on a single neuron update at a time mechanism. For a network featuring N binary neurons, a randomly-selected jth neuron is updated at time t + 1 using

$$
U _ {j} (t + 1) = f \left(\sum_ {i = 1} ^ {N} w _ {i j} (t) U _ {i} (t) + T _ {j} ^ {b}\right), \tag {1}
$$

where Uj(t) is the binary state of the jth neuron at time t, wij(t) is the synaptic strength between neurons i and j b at iteration t, T j is the bias strength of the jth neuron, and f(.) is the binary threshold function. %e key features of HNNs are their activation dynamics and energy function, which are proven to be monotonically descending during the runtime15 (see Supplementary Section 1 for more details). Hence, by mapping the cost function of the optimization problem into the energy of the network and the variables to neuron states, the recurrent dynamic of the network optimizes the cost function and solves the optimization problem in the runtime.

1 UC Santa Barbara, Santa Barbara, CA 93106-9560, USA. 2 Linkoping University, 60174 Norrköping, Sweden. 3These authors  contributed  equally:  M.  R.  Mahmoodi  and  Z.  Fahimi. *email:  z.fahimi@ucsb.edu;  mrmahmoodi@ ucsb.edu

![](images/b4f967007b9720f46d95ff8f04c5047c08cdfa3a0749d8eb8cbb1778d80a9af5.jpg)

![](images/585906f94e6b632b4131a05be993cf73eb260a76b65b9a61c87c085315c00c48.jpg)

![](images/b43ac678ba65622de353ca41a39314b06655f7d0cf86a3b8d3b44f1931179120.jpg)

![](images/a0fda9b15d7581356ddb7f08095505f0197b8125a851335d02321b974a1dcb14.jpg)

![](images/7ce06f9768888994e349a97a56b03175c1f97a6f4898ddbcc135da54e284af09.jpg)

![](images/983658bf20fb6bf85a91860961792bf7b56ed10659dc4a746d45df134a962136.jpg)

Figure 1. Neuro-optimization with the weight annealing: (a) %e 7-node weighted graph partitioning problem that is used to illustrate the mechanism of weight annealing. %e blue/green coloring shows the optimum solution (Supplementary Materials S3 includes the actual weights). (b) %e energy evolution of each state during weight annealing for 200 epochs and τ = 40. %e black spheres mark the transitory ground state of the system, which is also projected to the energy-epoch plane. %e magenta curve shows the average transitory energy over 128 runs, which shows that the proposed weight annealing tracks the transitory globally optimum state of the system. (c) %e average energy of the network annealed with di'erent techniques over 128 runs. (d) Top-1 and Top-5 success rates of varying annealing techniques versus problem size (B: baseline, i.e., the standard Hop!eld network without annealing, S: stochastic (temperature reduced from 100 to 0.01), C: chaotic (temperature reduced from 250 to 0.001), and E: exponential weight annealing). For each graph size, we consider 200 randomly weighted problems and provide the parameters in supplementary S4. Note that the best response is the global optimum, and Top-5 counts if the !nal response is among the best top-5 solutions. Panel (e) shows the distribution of the !nal average energy, o'set by a constant for clarity, for the same graphs used in panel (d). %e circles represent graph size. (f) %e boxplot of the average !nal energy vs. epoch size for 200 random con!gurations of 25-node graph partitioning problems.

Similar to the Ising model and other greedy and local search methods, the critical shortcoming of HNN is the presence of (many) local minima in their energy function. Simulated16,17 and chaotic18–20 annealing are two prominent techniques that tackle this issue by harnessing thermally controlled probabilistic jumps and embedded chaos in HNNs with nonzero self-feedback weights, respectively. %erefore, an e$cient HNN accelerator should perform the frequent dot-product operation in Eq. 1 very fast and support an annealing technique to rescue the network from trapping in local minima. %is paper introduces a weight annealing technique in HNNs and its e$cient implementation, which is more e'ective and scalable than simulated and chaotic annealing methods. Our approach dates back to methods like weight annealing21–24, noising25, space smoothing26,27, and !ne-tuned learning28, where the core idea is to change in the energy landscape by modifying weights in the formula for the energy. Here, the exact meaning of “weight” varies from method to method, as well as from problem to problem addressed—a weight may be associated with an input data point, a subproblem, etc.; similarly, a variety of ways to modify the weights (random perturbation, adversarial change, etc.) has been explored. %e common crux of the methods is that they modify the weights di'erently in every timestep and in di'erent areas of the solution space; this way, the search is guided by weight changes adapted to the current state and reuses insights gained from previous iterations. While the clever schemes for such adaptive weight modi!cations underpin the strengths of methods, mimicking this adaptivity within any hardware would likely be ine$cient since performing individual changes to the weights consumes signi!cant time and energy. Further, hardware implementation of the algorithms that act di'erently in di'erent parts of the solution space would require complicated circuitry, leading to e$ciency losses. Our proposed weight annealing circumvents both of the above: First, all weights are scaled together at every iteration. Second, the weight modi!cation is oblivious to the status of the solution space exploration—the annealing schedule is pre-set in advance and does not depend on the state of the system (in particular, the schedule does not depend on the value of the energy function—it is the hardware that takes care of the derivatives, convergence, escaping local optima with stochastic decisions, etc.). We numerically demonstrate the e'ectiveness of our approach on several benchmarks by solving graph partitioning, vertex cover, maximumweight independent set, and maximum-weight clique problems.

We also propose a very e$cient implementation of weight annealing in HNNs harnessing analog-grade non-volatile memories, which have become the mainstream devices for implementing fast, compact, and energye$cient dot-product engines29–32. %e potentials for performing high-speed physical-level computing are perhaps the most intriguing feature of these devices. Passive (0T1R) memristive devices are the most promising candidate for the next generation of analog computing systems in part due to their excellent scalability prospects and superior integration density33–36. Furthermore, recent breakthroughs in exploiting embedded eFlash memories have opened the doors towards building large-scale industrial-grade neurocomputing systems32,37 as well. %ese exciting opportunities have served as the motivations for several experimental proposals on Hop!eld networks, simulated annealing, and related concepts.

Reference38 uses discrete Pt/TiO2(x/Pt memristive devices to implement a small-scale 4-bit data converter with the Hop!eld model. Reference39 implements a 3-bit associative memory based on digital HfO memristors. In 2Ref.40, simulation results demonstrate the e'ectiveness of using the inherent chaos in sub-100 nm NbO2 memristors to implement simulated annealing within Hop!eld networks. Ref. 41 implements an 18-node restricted Boltzmann machine based on a versatile stochastic dot-product engine using TiO2 memristive crossbars42. In addition, Ref. 41 demonstrates hardware implementation of simulated, chaotic, and adjustable annealing within HNNs. Conceptually, the proposed weight annealing is similar to the adjustable technique as it relies on dynamic scaling of the energy during runtime. However, the proposed method has a more straightforward implementation as it does not require extra circuitry, is not limited to the dynamic range of devices, and can be generally applied to any HNN irrespective of the target optimization problem. Several works (e.g., see43–45) propose using the inherently random switching mechanism of memories to implement stochastic sigmoid neuron functionality and simulated annealing. However, this method su'ers from the limited switching endurance, cycle-to-cycle and device-to-device variations, and scalability issues. Finally, Ref. 46 uses Y-"ash memories to implement a 3-bit associative memory based on the Hop!eld model.

![](images/51b70d7a5819501d68d0a20a8a0f05ab4c23abeded59dca49121789981a7d0c6.jpg)

# Results

%e proposed idea is to slowly modulate the energy landscape of the HNN, starting from a funnel shape with a deep global optimum where the ground state is easily accessible. %e network traps in it in the early stages and tends to remain in ground states during the runtime. In our proposed method, we change the synaptic weights slowly by considering $w _ { i j } = T _ { i j } \Big ( 1 - e ^ { \frac { - t } { \tau } } \Big )$ where $\tau > 0$ is the annealing schedule, and T is the ultimate synaptic weight matrix. %e Lyapunov energy associated with a certain state of the network at t is given by

$$
E (t) = - \frac {1}{2} \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} w _ {i j} (t) U _ {i} (t) U _ {j} (t) - \sum_ {i = 1} ^ {N} T _ {j} ^ {\mathrm {b}} U _ {j} (t). \tag {2}
$$

At the beginning and while t<<) is very small, the !rst term [in Eq. (2) ] is negligible, and the total energy of the network $\begin{array} { r } { \mathrm { i } s - \sum _ { i = 1 } ^ { N } T _ { i } ^ { b } U _ { j } ( t ) } \end{array}$ . At this stage, the network !nds a straightforward solution a#er few updates. i  %e ground state, for example, is located at $\bar { U _ { j } } = 1$ for the jth neuron that has $T _ { i } ^ { \mathrm { b } } > 0$ . As the network evolves, wij(t) gradually moves toward $T _ { i j } ( t )$ and the !rst term in Eq. (2) becomes more signi!cant until the network stabilizes in the equilibrium state. During this runtime, the ground state of the network changes many times, but the network tends to capture it and closely follows the transitory ground state.

We consider graph partitioning problems (see Supplementary Section 2) that !nd applications, e.g., in graphbased electronic structure theory applied to quantum molecular dynamic simulations45. To demonstrate a clear visual representation of ground state evolution, we use a 7-node graph partitioning problem with randomly selected weights and edges, as shown in Fig. 1a (see Supplementary Sect. 3 for the actual vertex and edge weights). Figure 1b shows the semi-exponential energy change of all possible states during the annealing $( \tau = 4 0 )$ . %e energy associated with each state is exponentially increasing as expected. %e black sphere points (projected to the bottom plane for clarity) represent the ground state of the system during the annealing. %e global optimum is ( 389.5459 and locates at state 97 (decimal equivalent of $^ { \cdot \propto } \dot { 1 } , 1 0 0 , 0 0 1 ^ { \mathfrak { W } } )$ . %e transitory state of the system is speci!ed by listing the N values of U and represented by a binary word of N bits14 and its decimal version for simplicity. $\mathrm { A t } t = \dot { 0 } ;$ the global minimum is recognizable (state 118, $E = - 9 1 7 . 7 6 )$ ). While the network is steadily evolving, the ground state of the system increases, and its location changes several times. %e average transitory energy of the system (de!ned over the transitory synaptic weights) is also shown for 128 initialization schemes and 200 epochs $( N _ { \mathrm { E P } } = 2 0 0 )$ in magenta. %e network !nds the initial ground state very quickly (regardless of the initial state) owing to the annealing mechanism and tracks it during the evolution. Other simulation details, including wij evolution are provided in Supplementary Sect. 3.

Figure 1c shows the performance of the proposed annealing technique versus stochastic annealing with a probabilistic sigmoid neuron (the temperature is reduced exponentially from 100 to 0.01) and chaotic annealing (the self-feedback weights are decreased exponentially from 250 to 0.001). In this experiment and a#er 200 epochs, the success rate (the relative number of cases led to the global optima) is 57.8%, 59.37%, 94.53% for chaotic, stochastic, and weight annealing techniques, respectively, and it is 28.12% for the standard Hop!eld model (baseline). It is noteworthy that the stochastic annealed network converges to $\mathrm { E } = - 3 8 7 .$ .98 and scores a 98.6% success rate when 30 k epochs are used, and the temperature is scaled from 100 k to 0.01.

To further investigate the performance of the proposed approach, 200 randomly populated con!gurations of 5, 10, 15, 20, and 25-node graphs are considered. Supplementary Sect. 4 discusses the parameters used in the simulations. %e annealing schedule parameter is manually optimized for the !rst problem and used in all con!gurations. %e scalability of our approach is compared with simulated annealing on three scenarios: !rst, $N _ { \mathrm { E P } } = 3 0 0$ is assumed for all sizes, then it is exponentially increased for a !xed-size graph (N = 25), and then, NEP is exponentially increased with respect to the linear increase of the problem size.

%e success rate achieved by di'erent methods on various problem sizes for $N _ { \mathrm { E P } } = 3 0 0$ is shown in Fig. 1d. %e performance of weight annealing is on par with simulated annealing for $N = 5 ;$ however, the energy gap becomes signi!cantly wider for larger problem sizes. More interestingly, for $N = 1 5 ,$ , among the 200 con!gurations, the 20 percentiles success rate of weight annealing is better than the 80 percentiles of all other methods. Note that due to the analog-grade behavior of our memristors, weighted graph problems are considered, and it would be unfair to compare our results (in terms of success rate) with previous implementations, which focus on sparse graphs with binary weights. Figure 1e shows the average !nal energy for the same graphs. %e gap between the solution quality (!nal energy) of exponential weight annealing and other methods becomes wider in more massive graphs. In Fig. 1f, the computational runtime (epoch number) is increased for 200 con!gurations of 25-node graphs. As expected, the performance of all annealing techniques, including weight annealing, improves by increasing the number of epochs (in part due to slower cooling, which allows the networks to search for better solutions). %e performance of weight annealing no longer improves for $N _ { \mathrm { E P } } { > } 3 2 0 0$ , while simulated annealing techniques, with noticeable inferior performance, bene!t from the longer computational time and slower annealing. %is is partly due to the inherent di'erences between the underlying mechanism of simulated and exponential weight annealing. Stochastic annealing requires more time to explore larger searching spaces. While for the weight annealing, it is simply not the case. %e accuracy saturation stems from the fact that the slower learning of weights no longer creates a more optimum path. Note that weight annealing achieves the same solution quality 10 × faster than simulated annealing techniques. Supplementary Sect. 4 extends the graph partitioning simulations. %ree other combinatorial optimization problems are considered in Supplementary Sect. 5, and the results signify the superiority of weight annealing, particularly in large scale problems.

![](images/76cd3e61b38d08d3b90e9d172fca4c8f0db99cb2d1a5b3d6cfa1488dd20c2ef9.jpg)  
Figure 2. %e current-mode recurrent circuit that implements the weight annealing of discrete-time Hop!eld networks with programmable analog memories. %e green circles show the bias weights $( T _ { i } ^ { \mathrm { b } } )$ while the black circles implement self-feedback weights $( T _ { i i } )$ i , and the rest of them denote the main synaptic weights $( T _ { i j , i \neq j } )$ . A constant ‘on’ voltage, which is the same as the tuning voltage, drives the bias column. We control the applied voltage to the rest of the devices during the runtime to adjust the synaptic weights (exponentially). Note tha $V _ { \mathrm { { c m } } }$ is only added to emphasize that the circuit operate on a single- $- V _ { \mathrm { d d } } .$ . Values $R , { \check { C } } ,$ and I depend on the problem size and technology, and determine the annealing schedule. Switch S resets the network to the initial condition. %e selected neuron is determined by the input address to the decoder, and the operation is synchronized with the sampling clock $( \varphi )$ in dynamic comparator. Note that we have omitted the tuning circuits in the !gure for clarity.

# Experimental results

%e proposed technique is demonstrated by addressing two optimization problems based on the most prospective analog-grade memory technologies. %e central merit of weight annealing lies in its very straightforward and compact implementation. Experimental results of hardware implementation are demonstrated by solving a 16-node graph partitioning problem using a 20 × 20 passively integrated analog-grade memristive crossbar and a 7-node maximum-weighted independent set on a $1 2 \times 1 0$ embedded array of eFlash memories.

Figure 2 shows the implementation of the weight annealing technique. %e corresponding hardware realization of Eq. (1) is discussed in the method section for both cases. %e main challenge in realizing the weight annealing is scaling the synaptic weights. Let us emphasize that direct modi!cation of (analog) states is impractical in part because of the limited endurance, device-to-device, and cycle-to-cycle variations. %is challenge can be resolved in resistive memories by using a simple control circuit (the pre-synaptic drivers), which scales all synaptic weights simultaneously (see Fig. 2). Here, V is exponentially increased toward $V _ { \mathrm { a p } }$ at which all devices are tuned. %e current neuron state determines which devices should be driven by $\underline { { V _ { \mathrm { c t r l } } } } .$ %e post-synaptic circuits include trivial circuits such as transimpedance ampli!ers (e.g., a bu'ered version of Ref.47) that senses currents and a dynamic voltage comparator (see, e.g.,48) that updates the selected neuron state. %ese circuit functionalities are emulated with Agilent characterization tools in the present demonstration.

In split-gate embedded Flash memories, the situation is more straightforward as we can bias the memories in the weak inversion regime, making their states (i.e., currents) semi-exponentially dependent on the select-gate voltage. %en, $V _ { \mathrm { c t r l } }$ is applied to the shared select-gates and linearly increased toward the $V _ { \mathrm { a p } } .$ .

In the !rst experiment, a 13-node graph partitioning problem is implemented using passively-integrated memristive crossbars. Note that, to the best of our knowledge, this work is the largest Hop!eld network implemented with passive memristors. Figure 3a shows the wire-bonded chip, crossbar TEM image, and an SEM image of a memristive device. %is crossbar has been previously used for the demonstration of a multilayer perceptron49, integrated spiking neural network for coincident detection29, and a hardware security primitive design50,51. %e method section includes a brief description of fabrication steps. More relevant details are also available in our previous work49.

In order to increase the demo size and without the loss of generality, we have ensured the weights and edges (of the graph) are selected such that $T _ { i j } < 0$ and $b _ { j } > 0$ (see Supplementary Sect. 6 for more details). %is facilitates a single-ended time-multiplexed dot-product of a $1 3 \times \left( 1 3 + 1 \right)$ network on our memristive crossbars. %e details of forming, tuning, and operation of the circuit, as well as the procedure of mapping the actual synaptic weights (from so#ware) to conductance values, are illustrated in the method section. A#er determining the desired conductance map, the devices are programmed individually using the write-verify algorithm54. Figure 3b,c show the desired weight map of the network and the corresponding conductance map obtained a#er tuning the crossbar, respectively. Most devices are tuned very close (within 5%) to the desired states, which is possible due to the tight distribution of switching thresholds in our analog-grade crossbar circuits. Figure 3d shows the distribution of pre-activation readout currents for the baseline case (the inset indicates no bias in neuron

![](images/b5fb96ad436b828afec288f11fb1c011702a1dbbbe32161be87693483f8bfbaa.jpg)

![](images/ebb9cfa34fc36690b8af199d31528a7ba06f73ea93598bbac11264ade1cb7492.jpg)

![](images/2f88347e3f23d5c8398c663b3a85b4bbbf99cabafc9ee484de2ed7cea5ad3f25.jpg)

![](images/1ee3ead1eabc4b9d0b8bf8106583ff9ad59aee5f52d34c05206191d75c837313.jpg)

![](images/e6cdc0c324585d8117150c5ccf2634861c10cd1c77b49c24237011ffabe65757.jpg)  
(b)

![](images/e3b3996de0f5ef590f0d553feeb72c6784c5ff76be20bd3b913e93c52b1b8cb4.jpg)  
(c

![](images/31b2c9d1c4df10f94868c8a1654d0802aadde6ae700cedc1010dd5cb27aab111.jpg)

![](images/565d538506d4eb7a52a4c5f343370e3a143a6a8fda549dbd8f68a21dbe782aa9.jpg)  
(e)

![](images/3c6b68034d21b6d83b309d3993eb2ba24c49176509861ebe65b18fbed6e093a0.jpg)  
(1)   
Figure 3. %e experimental demonstration with the integrated memristor crossbars. (a) %e fabricated $2 0 \times 2 0$ integrated memristor crossbar29. (b) %e desired ideal analog map for the 13-node graph partitioning problem, and (c) the resultant conductance map of the devices a#er tuning the crossbar. (d) Distribution of the readout current when solving the problem with the conventional (baseline) approach. %e inset shows the histogram of selected neurons (for updates) and indicates there is no bias in the neuron update. (e) %e evolution of the synaptic weights during the weight annealing. (f) %e experimental versus simulation results of the neurooptimization with di'erent techniques. %e inset shows the zoomed-in average energy in the last 100 epochs.

![](images/8b1706493fd7229eaba65dc9b72c2f4e0bb96f2d795bcad9572366d24d8931f5.jpg)

selection). %e input “on” voltage corresponding to binary input ‘1’ is $V _ { \mathrm { a p } } { = } 0 . 1 ~ \mathrm { V } .$ Note that we exponentially increase the “on” applied voltage from 0 to 0.1 V for the weight annealing. %e measured synaptic strength of each device during the weight annealing is shown in Fig. 3e. %e experimental and simulation results are compared in Fig. 3f. Speci!cally, the average energy over $1 0 ^ { 3 }$ cases for 200 epochs is shown for various methods. Here, the annealing schedule parameters are $1 0 ^ { 4 } , 1 0 ^ { 5 } ;$ , and 35 for chaotic, stochastic, and weight annealing, respectively. %e ground state locates $\begin{array} { r } { 1 1 - 3 7 9 6 , } \end{array}$ and weight annealing (on both experiment and simulation) performs better than other techniques and far better than the baseline.

In our second experimental demo, a 7-node maximum-weighted independent set is solved using an array of 12 × 10 redesigned embedded Flash memories fabricated in Global Foundries 55 nm LPe CMOS process (Fig. 4a). %e redesigned array structure enables< 1% analog programmability52 (see Fig. 6S). %e circuit diagram in Fig. 6Sd implements the weight annealing of Hop!eld networks with eFlash memories. Biasing conditions (imposed during programming) ensure the subthreshold operation of the devices at all operating conditions. Figure 4b shows the implemented weighted graph. Similar to the !rst demo, the weights and edges (of the graph) are chosen randomly but constrained by $T _ { i j } < \dot { 0 } \mathrm { a n d } T _ { i } ^ { \mathrm { b } } > 0 .$ . %e original weight matrix is shown in Supplementary Sect. 7. %e ground state of the energy function locates at -5.5755 that corresponds to the neural state “0010001”.

The devices are programmed with < 1% accuracy (see the method section). Figure 4c shows the resultant map of state currents under nominal biasing conditions, i.e., $( V _ { \mathrm { W L } } = \bar { 1 } . 5 \mathrm { V } , \ : V _ { \mathrm { C G } } = 2 . 5 \mathrm { V }$ , $V _ { \mathrm { B L } } = 1 \mathrm { V } , \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { V } _ { \mathrm { S L } } = 0 \mathrm { V }$ , and $V _ { \mathrm { E G } } = 0 \mathrm { V } )$ . %e experiments and simulations are performed over 128 initialization cases for 500 epochs and show the results in Fig. 4d. %e results are averaged over 100 runs in the simulations. %e annealing schedule is 10, 10, and 100, and the average probability of hitting the global optimum is 0.76, 0.92, 0.82, and 0.99 for stochastic, chaotic, and weight annealing, respectively (Fig. 4e). We drive the devices

![](images/d7ac81984ceb9830c9343834b857145ea48ec456b44da5baa41a70f9a51b9b8b.jpg)  
(a)

![](images/bbfa2b8cbdf3b74d5992fdaf41f6dcb51540d95e50fde4b7092c6047a00def5f.jpg)

![](images/19f40db2f3e9393696becd95775956dd2766e4136fed2edcd3694bae5d2efeb4.jpg)

![](images/3faf312fb135e951b35f45cb374b53c3df102ddb172a8b9b65d8e6fec8ed4922.jpg)  
(d)

![](images/c54e8b90fbe58380a14352de3d32c669a101e37d6e3bcea113160d219225fe55.jpg)  
(e)   
Figure 4. Neuro-optimization with embedded analog-grade eFlash memories. Panel (a) shows the fabricated 10 × 12 eFlash array chip in Global Foundries’ standard LPe CMOS process52. (b) A 7-node maximum-weighted independent set problem. (c) %e heat map of the synaptic weights for the devices that implement the neuronoptimization. (d) %e average energy versus epoch comparing experimental results with simulations over 100 runs. (e) %e success rate of di'erent annealing techniques on this problem over 100 runs.

corresponding to bias weights $( T _ { j } ^ { \mathrm { b } } )$ by constant gate-voltages $( V _ { \mathrm { W L } } = 1 . 5 \mathrm { V }$ and $V _ { \mathrm { C G } } = 2 . 5 \mathrm { V } )$ , while other rows (if their corresponding neuron is in the ’on’ state) are driven by $V _ { i } ( t )$ . %e impact of annealing schedule and exponential versus linear voltage scaling are also studied in Fig. 7S. For the former, a slower annealing schedule $( \tau _ { \mathrm { e x p } } = 6 0 )$ tackles the nonlinearities in the super-exponential dependency of synaptic current to voltage and closely match the trends in the simulations. For the latter case, the slowest annealing process $( \tau _ { \mathrm { e x p } } = N _ { \mathrm { E P } } \doteq 5 0 0 )$ leads to the best response.

# Discussion and summary

We have demonstrated weight annealing, a technique that improves the performance of asynchronous Hop!eld neuro-optimizer. %e weight annealing converges faster and to a better solution within studied runtime as compared to other considered annealing approaches. %e scalability of weight annealing (size and computational time) is investigated by solving several combinatorial problems, and its straightforward implementation is demonstrated the using two state-of-the-art analog-grade non-volatile memories.

%e passive integrated memristor technology o'ers the best scaling prospects and low fabrication cost. We have recently developed a 4 K fully CMOS-compatible 0T1R array with excellent switching characteristics36. %e measured analog characteristics are promising for the development of large-scale neuro-optimization systems. On the other hand, eFlash technology is much sparser, but it is currently commercially available and embedded in standard CMOS processes (down to 28 nm). Our preliminary estimations (see Supplementary Sect. 8 for more details) indicate impressive prospects of using metal-oxide memristors for the hardware implementation of Hop!eld networks and weight annealing. Future works focus on the CMOS-integrated design of a weight annealing optimizer, allowing us to perform a rigorous comparison with entirely fabricated annealing machines.

As opposed to most previous works43–45 that focus on switching statistics of memristors, our proposed solution o'ers very infrequent writes, which is justi!ed assuming long runtimes of computationally extensive problems. More importantly, our proposed neuro-optimizer o'ers analog (> 5 bits with memristive nanodevices and > 6 bits via eFlash technology) weights. %is feature is not demonstrated in most previous Ising machines. Unlike quantum computing machines that are susceptible to environmental noise, hard to scale, and must operate at cryogenic temperatures, the proposed circuit is more scalable, and can operate at room temperatures.

In summary, the proposed weight annealing boosts the performance of HNN in solving combinatorial optimization problems. Using extensive simulations on four representative problems, we numerically demonstrate that the proposed method outperforms the conventional Hop!eld network (baseline) and challenges the prominent stochastic and chaotic annealing techniques in computational time and accuracy. %en, an e$cient, scalable,

and fast circuit implementation and experimentally veri!ed based on two memory technologies. Large-scale integrated implementation is demonstrated of weight annealing is a near-term future work.

# Methods

In the !rst experiment, we demonstrate the weight annealing with a 20 × 20 array of passively integrated crossbars of 600-nm pitch memristive devices (200-nm lines separated by 400-nm gaps) fabricated in the University of California at Santa Barbara’s nanofabrication facility. %e fabrication and characterization details are discussed in 29,49. In summary, we deposit the active bilayer by low-temperature reactive sputtering, evaporate electrodes using oblique angle physical vapor deposition, pattern them by li#-o' technique, and then contact them to bonding pads. %e crossbar is wire-bonded in a dual in-line package and mounted on a custom-made printed circuit board, as shown in Supplementary Section 9.

%e devices are in pristine states upon fabrication and require electroforming to become programmable devices. An automated setup performs the current-controlled electroforming process device per device. A compliance voltage (1.5 V to begin with, but it is dynamically updated) prevents the memristors from burning. For every device, we sweep the applied current from 0 to 100 µA and monitor its resistance consistently. %e process continues until the device reaches an acceptable low resistance (typically 5 k+–150 k+). %e devices are formed individually and reset them a#er each forming success (to remove leakage for the rest of the crossbar). A dynamic leakage removal procedure is also employed to reset the devices when the algorithm struggles to form several devices in a row.

%e devices are tuned using an ex-situ approach meaning that weights $( T _ { i j } )$ and biases $( T _ { b } )$ are obtained from so#ware simulations and later transferred to the crossbar. Indeed, a#er forming the entire crossbar, i.e., the 400 devices (yield is typically > 99%), the memristors are tuned to the desired states individually using V/2 and write-verify schemes. %e automated algorithm progressively increases the pulse amplitude from 0.5 to 2 V (to increase the conductance) and from 0.5 to 2.2 V (to reduce it). %e pulse width is 1.1 ms during the programming. Each device typically needs ~ 50 pulses to reach within 2% of the targeted state. %e fabricated crossbar has a reasonably uniform and tightly distributed switching thresholds ranging from 0.6 to 1.5 V (for set) and ( 0.6 to ( 1.7 V (for reset), which provides us with the opportunity to harness the V/2 scheme and precisely tune the devices. %e devices have excellent retention characteristics, and accelerated retention tests report minor < 1% change in a#er the projected 10 years of operation at room temperature. Additional details are provided in Ref.22.

In order to increase our demo size (given our 20 × 20 crossbar size), we deliberately chose edges to be larger than weights (the values are selected randomly in all experiments and simulations) to force all non-diagonal synaptic weights $( T _ { i j } )$ to be negative and all biases to be positive. %is technique allows us to implement a relatively larger demo by assigning one device per weight (in comparison with the two-device per synapse needed for fully di'erential design) and perform each the vector-by-vector multiplication in two cycles. Indeed, the dot-product operation is implemented in a two-step time-multiplexed fashion; that is, in one cycle, we measure the total current $( \sum I ^ { - } )$ associated with the input vector multiplied by the synaptic weight vector (from the selected neuron), while the input bias voltage is zero. %en, we subtract it from the sensed current $( \sum I ^ { + } )$ from the same bitline, while the main inputs are zero and apply $V _ { \mathrm { a p } } { = } 0 . 1 ~ \mathrm { V }$ to the bias column. Besides, to increase the dynamic range, all bias conductances are divided by 5 and compensated by applying an extra gain of 5 at the neuron side. In other words, the !nal output is evaluated by hard thresholding $\left( 5 \sum I ^ { + } - \sum I ^ { - } \right)$ . (Note that we have previously fully-di'erential single-shot dot-product engines are already demonstrated using the same devices in our previous $\mathrm { { \dot { w o r k s } - s e e , e . g . \mathrm { { \dot { 2 } } ^ { 9 , 3 9 } ) } } }$ , and this simple trick is employed only to enlarge the problem size.

Owing to the single-ended design, we use $g _ { i j } = G _ { \operatorname* { m a x } } { \left( T _ { i j } / \operatorname* { m a x } { \left( | T _ { \operatorname* { m a x } } \right| ) } \right) }$ ", where max $( \bar { | T } _ { \operatorname* { m a x } } | )$ is the maximum absolute weight and $G _ { \mathrm { m a x } }$ is the maximum absolute conductance (40 µS in our experiment). We ground all bitlines (bottom electrode) except the one associated with the selected neuron, which is virtually grounded, and its current is sensed using a B1530A fast measurement unit and a B1500A parameter analyzer. We apply neuron voltages to the switch matrix, connected to both 20 rows and 20 columns of the crossbar. We link top electrodes to the input neurons and bottom electrodes to the output neurons through an E5250A switch matrix.

%e eFlash chip, fabricated in Global Foundries 55 nm LPe process, includes a $1 2 \times 1 0$ redesigned industry-grade split-gate memory array. %e packaged chip is previously used for developing a high-performance dot-product engine52. Agilent B1500A and B1530A tools are used for measurements and pulse generation. We have developed a custom-made switch matrix on a printed circuit board controlled via a lightweight microprocessor to interface Agilent tools with the chip. More details on the experimental setup, programming, eraser, redesigned layout structure, half-select disturbance immunity, retention, and endurance characteristics are available in Ref.52. All eFlash memories are programmed to their targeted states at $V _ { \mathrm { W L } } = 1 . 5 \mathrm { V } , V _ { \mathrm { C G } } = 2 . 5 \mathrm { V } , V _ { \mathrm { B L } } = 1 \mathrm { V } , V _ { \mathrm { S L } } = 0 \mathrm { V }$ , and $V _ { \mathrm { E G } } = 0 \mathrm { V }$ and operated at the same biasing condition. Further, the devices are tuned one at a time by progressively increasing voltage pulses and using the write-verify algorithm. We have discussed the details of pulse amplitudes and durations in the programming phase in Ref.52.

As discussed in the main text, weight annealing is implemented by increasing the VWL from 0.7 to 1.5 V linearly and exponentially, which would exponentially and superexponentially increase the synaptic weights, respectively, since devices are operated in weak inversion (see Supplementary Materials S.7). Similar to the memristor-based circuit, we use the single device per synapse topology and compute each update in two cycles.

%e weights are mapped from so#ware to hardware by using ITij = Imax Tij|Tmax| $I _ { i j } ^ { T } = I _ { \operatorname* { m a x } } \frac { T _ { i j } } { | T _ { \operatorname* { m a x } } | }$ and $\begin{array} { r } { I _ { j } ^ { \mathrm { b } } = I _ { \operatorname* { m a x } } \frac { T _ { j } ^ { b } } { | T _ { m a x } ^ { b } | } } \end{array}$ = Imax in which $I _ { \mathrm { m a x } } = 1 \mu A , T _ { \mathrm { m a x } } = 2$ is the maximum absolute synaptic weight, and $T _ { m a x } ^ { b } = 3 . 6 9 4$ max  is the maximum absolute bias.

# Data availability

%e data that support the plots within this paper and are available from the corresponding author upon reasonable request.

Received: 23 March 2020; Accepted: 17 November 2020

Published online: 12 August 2021

# References

1. Wen, U., Lan, K. & Shih, H. A review of Hop!eld neural networks for solving mathematical programming problems. Eur. J. Oper. Res. 198, 675–687 (2009).   
2. Cook, W., Lovász, L. & Seymour, P. D. (eds.) Combinatorial Optimization: Papers from the DIMACS Special Year, Vol. 20 (American Mathematical Society, 1995).   
3. Korte, B. H. et al. Combinatorial Optimization Vol. 1 (Springer, 2011).   
4. Horio, Y., Ikeguchi, T. & Aihara, K. A mixed analog/digital chaotic neuro-computer system for quadratic assignment problems. Neural Netw. 18, 505–513 (2005).   
5. Yamaoka, M. et al. A 20k-spin Ising chip to solve combinatorial optimization problems with CMOS annealing. IEEE J. Solid State Circuits 51, 303–309 (2015).   
6. Boixo, S. et al. Evidence for quantum annealing with more than one hundred qubits. Nat. Phys. 10, 218 (2014).   
7. Johnson, M. W. et al. Quantum annealing with manufactured spins. Nature 473, 194 (2011).   
8. Yamaoka, M., et al. 24.3 20k-spin Ising chip for combinational optimization problem with CMOS annealing. In Proceedings of ISSCC’15, (San Francisco, CA, 2015).   
9. Takemoto, T., et al. 2.6 A 2&×&30k-spin multichip scalable annealing processor based on a processing-in-memory approach for solving large-scale combinatorial optimization problems. In Proceedings of ISSCC’19 (San Francisco, CA, 2019).   
10. Sutton, B., Camsari, K. Y., Behin-Aein, B. & Datta, S. Intrinsic optimization using stochastic nanomagnets. Nat. Sci. Rep. 7, 44370 (2017).   
11. Inagaki, T. et al. Large-scale Ising spin network based on degenerate optical parametric oscillators. Nat. Photon. 10, 415 (2016).   
12. Hop!eld, J. J. Neurons with graded response have collective computational properties like those of two-state neurons. Proc. Natl. Acad. Sci. 81, 3088–3092 (1984).   
13. Tank, D. & Hop!eld, J. J. Simple ‘neural’ optimization networks: An A/D converter, signal decision circuit, and a linear programming circuit. IEEE Trans. Circuits Syst. 33, 533–541 (1986).   
14. Hop!eld, J. J. Neural networks and physical systems with emergent collective computational abilities. Proc. Natl. Acad. Sci. 79, 2554–2558 (1982).   
15. Joya, G. M., Atencia, M. A. & Sandoval, D. F. Hop!eld neural networks for optimization: Study of the di'erent dynamics. Neurocomputing 43, 219–237 (2002).   
16. Kirkpatrick, S. Optimization by simulated annealing: Quantitative studies. J. Stat. Phys. 34, 975–986 (1984).   
17. Kirkpatrick, S., Gelatt, C. D. & Vecchi, M. P. Optimization by simulated annealing. Science 220, 671–680 (1983).   
18. Chen, L. & Aihara, K. Chaotic simulated annealing by a neural network model with transient chaos. Neural Netw. 8, 915–930 (1995).   
19. Akiyama, Y., et al. Combinatorial optimization with Gaussian machines. In Proceedings IEEE International Joint Conference on Neural Networks, Vol. 1 (1989).   
20. Chen, L. & Aihara, K. Chaos and asymptotical stability in discrete-time neural networks. Phys. D 104, 286–325 (1997).   
21. Elidan, G., Ninio, M., Friedman, N. & Schuurmans, D. Data perturbation for escaping local maxima in learning. In AAAI/IAAI 132–139 (2002).   
22. Ninio, M. & Schneider, J. J. Weight annealing. Phys. A Stat. Mech. Appl. 349, 649–666 (2005).   
23. Loh, K., Golden, B. & Wasil, E. Solving the one-dimensional bin packing problem with a weight annealing heuristic. Comput. Oper. Res. 35   
24. Loh, K. H., Golden, B. & Wasil, E. A Weight Annealing Algorithm for Solving Two-dimensional Bin Packing Problems, Operations Research and Cyber-Infrastructure 121–146 (Springer, 2009).   
25. Charon, I. & Hudry, O. %e noising method: A new method for combinatorial optimization. Oper. Res. Lett. 14, 133–137 (1993).   
26. Coy, S. P., Golden, B. L. & Wasil, E. A. A computational study of smoothing heuristics for the traveling salesman problem. Eur. J. Oper. Res. 124, 15–27 (2000).   
27. Gu, J. & Huang, X. E$cient local search with search space smoothing: A case study of the traveling salesman problem (TSP). IEEE Trans. Syst. Man Cybern. 24, 728–735 (1994).   
28. Coy, S. P., Golden, B. L., Runger, G. C. & Wasil, E. A. Using experimental design to !nd e'ective parameter settings for heuristics. J. Heuristics 7, 77–97 (2001).   
29. Prezioso, M. et al. Spike-timing-dependent plasticity learning of coincidence detection with passively integrated memristive circuits.Nat. Commun.9,5311(2018).   
30. Bavandpour, M., et al. Mixed-signal neuromorphic inference accelerators: recent results and future prospects. In Proceedings of International Electron Devices Meeting (IEDM) (San Francisco, CA, 2018).   
31. Mahmoodi, M. R. & Strukov, D. B. An ultra-low energy internally analog, externally digital vector-matrix multiplier based on NOR "ash memory technology. In Proceedings of Design Automation Conference (DAC) (San Francisco, CA, 2018).   
32. Guo, X., et al. Fast, energy-e$cient, robust, and reproducible mixed-signal neuromorphic classi!er based on embedded NOR "ash memory technology. In Proceedings of International Electron Devices Meeting (IEDM) (San Francisco, CA, 2017).   
33. Rajendran, B. & Alibart, F. Neuromorphic computing based on emerging memory technologies. IEEE J. Emerg. Select. Top. Circ. Syst. 6, 198–211 (2016).   
34. Burr, G. W. et al. Neuromorphic computing using non-volatile memory. Adv. Phys. X 2, 89–124 (2017).   
35. Kuzum, D., Yu, S. & Wong, H. P. Synaptic electronics: Materials, devices and applications. Nat. Nanotechnol. 24, 3001 (2013).   
36. Kim, H., Nili, H., Mahmoodi, M. R. & Strukov, D. B. 4K-memristor analog-grade passive crossbar circuit. arXiv:1906.12045 (2019).   
37. Mahmoodi, M. R. & Strukov, D. B. An ultra-low energy internally analog, externally digital vector–matrix multiplier based on NOR "ash memory technology. In Proceedings of Design Automation Conference (DAC) (San Francisco, CA, 2018).   
38. Guo, X. et al. Modeling and experimental demonstration of a Hop!eld network analog-to-digital converter with hybrid CMOS/ memristor circuits. Front. Neurosci. 9, 488 (2015).   
39. Hu, S. G. et al. Associative memory realized by a recon!gurable memristive Hop!eld neural network. Nat. Commun. 6, 7522 (2015).   
40. Kumar, S., Strachan, J. P. & Williams, R. S. Chaotic dynamics in nanoscale NbO2 Mott memristors for analogue computing. Nature 548, 318 (2017).   
41. Mahmoodi, M. R., Prezioso, M. & Strukov, D. B. Versatile stochastic dot-product circuits based on non-volatile memories for high performance neurocomputing and neural optimization. Nat. Commun. 10, 5113 (2019).   
42. Mahmoodi, M. R., et al. An analog neuro-optimizer with adaptable annealing based on 64×64 0t1r crossbar circuit. In Proceedings of IEEE International Electron Devices Meeting (IEDM) 14.7.1–14.7.4 (San Francisco, CA, USA, 2019).

43. Borders, W. A. et al. Integer factorization using stochastic magnetic tunnel junctions. Nature 573, 390–393 (2019).   
44. Roy, K., Sengupta, A. & Shim, Y. Perspective: Stochastic magnetic devices for cognitive computing. J. Appl. Phys. 123, 210901 (2018).   
45. Fukami, S. & Ohno, H. Perspective: Spintronic synapse for arti!cial neural network. J. Appl. Phys. 124, 151904 (2018).   
46. Danial, L. et al. Two-terminal "oating-gate transistors with a low-power memristive operation mode for analogue neuromorphic computing. Nat. Electron. 2, 596–605 (2019).   
47. Assaad, R. S. & Silva-Martinez, J. %e recycling folded cascode: A general enhancement of the folded cascode ampli!er. IEEE J. Solid State Circ. 44, 2535–2542 (2009).   
48. Razavi, B. %e StrongARM latch [a circuit for all seasons]. IEEE Solid State Circuits Mag. 7, 12–17 (2015).   
49. Bayat, F. M. et al. Implementation of multilayer perceptron network with highly uniform passive memristive crossbar circuits. Nat. Commun. 9(1), 2331 (2018).   
50. Mahmoodi, M. R., Nili, H., & Strukov, D. B. RX-PUF: Low power, dense, reliable, and resilient physically unclonable functions based on analog passive RRAM crossbar arrays. In Proceedings of VLSITEC H’18 (Honolulu, HI, 2018).   
51. Nili, H. et al. Hardware-intrinsic security primitives enabled by analogue state and nonlinear conductance variations in integrated memristors. Nat. Electron. 1(3), 197 (2018).   
52. Guo, X., et al. Temperature-insensitive analog vector-by-matrix multiplier based on 55 nm NOR "ash memory cells. In Proceedings of CICC’17 (2017).   
53. Ushijima-Mwesigwa, H., Negre, C. & Mniszewski, S. M. Graph partitioning using quantum annealing on the d-wave system. In Proceedings of the Second International Workshop on Post Moores Era Supercomputing (ACM, 2017).   
54. Alibart, F. et al. High precision tuning of state for memristive devices by adaptable variation-tolerant algorithm. Nanotechnology 23, 075201 (2012).

# Acknowledgements

%is work was supported in part by a Semiconductor Research Corporation (SRC) funded JUMP CRISP center, NSF/SRC E2CDA grant 1740352, and partially supported by DENSO CORPORATION.

# Author contributions

M.R.M., Z. F., and D.B.S. conceived the original concept. M.R.M. developed the experiment and performed the measurements. Z.F. performed the simulations. H.N. fabricated the memristor crossbar. M.R.M. wrote the manuscript. All authors discussed the results.

# Competing interests

%e authors declare no competing interests.

# Additional information

Supplementary Information %e online version contains supplementary material available at https://doi.org/ 10.1038/s41598-020-78944-5.

Correspondence and requests for materials should be addressed to Z.F. or M.R.M.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional a$liations.

![](images/a063f2b4ea180c41890a052c64433230f5b3065d024f98a26827788330b44fb7.jpg)

Open Access %is article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or

format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. %e images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

%is is a U.S. Government work and not under copyright protection in the US; foreign copyright protection may apply 2020