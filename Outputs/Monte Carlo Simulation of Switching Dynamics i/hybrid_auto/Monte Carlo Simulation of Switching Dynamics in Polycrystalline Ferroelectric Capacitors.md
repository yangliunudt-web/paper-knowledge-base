---
title: "Monte Carlo Simulation of Switching Dynamics in Polycrystalline Ferroelectric Capacitors"
authors:
  - "Cristobal Alessandri"
  - "Pratyush Pandey"
  - "Angel Abusleme"
  - "Alan Seabaugh"
date: "2019-01-01"
year: "2019"
journal: "IEEE Transactions on Electron Devices"
doi: "10.1109/IEDM.2011.6131606"
abstract: "Ferroelectric (FE) materials are being studied for a variety of applications in memory,\\"
abstract_cn: "铁电材料正在被研究用于存储器、逻辑和神经形态计算等多种应用，其中铁电极化的预测模型至关重要。本文提出了一种蒙特卡洛模拟框架，能够预测铁电在任意输入波形下的动态、历史相关响应。该模拟通过推广基于物理的成核限制开关模型，用于多晶铁电中的极化反转。从制造的FE\\"
keywords:
  - "[[Monte Carlo method]]"
  - "[[Ferroelectric]]"
  - "[[HZO]]"
  - "[[Nucleation-limited switching]]"
cite: "[1] Alessandri C, Pandey P, Abusleme A, et al. Monte Carlo simulation of switching\\"
aiSum: "蒙特卡洛模拟多晶铁电器件开关动力学：基于成核限制开关模型，使用HZO电容器数据提取晶粒统计分布，预测任意波形下动态响应，分析铁电-电介质双层结构动态特性及器件变异导致的存储窗口缩减。"
confidence: "high"
wiki_concepts:
  - "[[Ferroelectric]]"
  - "[[HfO2]]"
---

# Monte Carlo Simulation of Switching Dynamics in Polycrystalline Ferroelectric Capacitors

Cristobal Alessandri , Student Member, IEEE, Pratyush Pandey, Student Member, IEEE, Angel Abusleme , Member, IEEE, and Alan Seabaugh, Fellow, IEEE

Abstract-Ferroelectric (FE) materials are being studied for a variety of applications in memory, logic, and neuromorphic computing, for which predictive models of FE polarization are essential. In this paper, we present a Monte Carlo simulation framework capable of predicting the dynamic, history-dependent response of an FE under arbitrary input waveforms. The simulation is developed by generalizing the physics-basednucleation-limitedswitching model for polarization reversal in a polycrystalline FE. Measured polarization reversal data from fabricated FE $\mathsf { H f } _ { 0 . 5 } \mathsf { Z r } _ { 0 . 5 } \mathsf { O } _ { 2 }$ capacitors are used to extract the statistical distribution of FE grains. After parameter extraction, the model is able to predict the dynamics of the FE capacitor without further calibration. Finally, the model is applied to characterize the dynamic response of FE–dielectric bilayer structures and quantify the reduction in memory window due to device variability.

Index Terms-Ferroelectric (FE)， hafnium zirconate (HZO), Monte Carlo, nucleation-limited switching (NLS).

# I. INTRODUCTION

T HE discovery of ferroelectricity in the CMOS-compatible HfO2 material system [1] has led to a variety of applications, including memory [2], [3], steep-slope transistors [4], [5], and neuromorphic computing [6], [7]. To design devices for these applications and further explore the use of ferroelectrics (FEs) in circuit design, reliable and predictive models of the FE polarization dynamics are needed. However, describing the switching behavior of thin-film polycrystalline FEs is complicated by the fact that they are composed of a multitude of grains having different switching thresholds, the distribution of which is highly dependent on the growth

Manuscript received March 29, 2019; revised May 3, 2019; accepted May 24, 2019. This work was supported in part by the Center for Low Energy Systems Technology (LEAST), one of six centers of STARnet, through the Semiconductor Research Corporation Program sponsored by MARCO and DARPA, and in part by the National Science Foundation under Grant ECCS/GOALI-1408425. The review of this paper was arranged by Editor S.-M. Hong. (Cristobal Alessandri and Pratyush Pandey contributed equally to this work.）(Corresponding author: Cristobai Alessandri.)

C. Alessandri is with the Department of Electrical Engineering, University of Notre Dame, Notre Dame, IN 46556 USA, and also with the Department of Electrical Engineering, Pontificia Universidad Catolica de Chile, Santiago 7820436, Chile (e-mail: calessan@nd.edu).

P. Pandey and A. Seabaugh are with the Department of Electrical Engineering, University of Notre Dame, Notre Dame, IN 46556 USA (e-mail: seabaugh.1@nd.edu).

A. Abusleme is with the Department of Electrical Engineering, Pontificia Universidad Catolica de Chile, Santiago 7820436, Chile.

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/TED.2019.2922268

conditions. Therefore, to predict the time evolution of an FE film, it is necessary to keep track of the configuration of switched grains. Moreover, it was recently shown that deep submicrometer FE FETs exhibit abrupt FE switching dependent on the history of accumulated pulses [8]. In this paper, we show a Monte Carlo simulation approach that accounts for the history-dependent switching observed in FE films.

Prior dynamic models based on the static Preisach model [9]–[11] approximate the multidomain polarization– voltage (P–V ) hysteresis loops by a hyperbolic tangent function, while the dynamic component is included by using equivalent circuits having either fixed or bias-dependent time constants [11]. Due to these approximations, such models do not keep track of the distributions of switching thresholds and resort to interpolation and scaling of parameters to replicate the history dependence of partially polarized FEs [9], [10].

On the other hand, nucleation-limited switching (NLS) models [12]–[14] provide an accurate description of the polarization reversal dynamics of FE thin films. The field-dependent NLS model characterizes the FE film as an ensemble of elementary regions that switch independently with a distribution of field-dependent time constants, effectively coupling the distribution of switching thresholds and the switching dynamics. These models have been experimentally validated in FE HfO2 [15], [16], lead zirconate titanate [12]–[14], [17], and other material systems [17]. However, NLS models are limited as they are polarization reversal models and can only describe the switching dynamics of an FE starting from a fully polarized state and under the application of a constant field.

The Monte Carlo simulation framework describes the dynamic, history-dependent switching of a multidomain FE. In this framework, the field-dependent NLS model is generalized for use with arbitrary input waveforms. After a parameter extraction from polarization reversal measurements, the model is able to accurately predict the dynamical behavior of FE hafnium zirconate (HZO) under various applied waveforms without further parameter tuning, showing the predictive capability of the model. This model was outlined in [18]. This expanded treatment provides a detailed derivation of the model with further discussion of its physical interpretation. This paper is organized as follows. In Section II, the field-dependent NLS model for polarization reversal is described. In Section III, the Monte Carlo simulation framework is introduced for FE polarization reversal and then generalized to arbitrary input waveforms. Model predictions

![](images/e2d80cfede152ec04fa9c45d4b10b1d298b2706a5cf046484b2f86a6aea93a57.jpg)  
(a)

![](images/3d35afe22cdbb362c57a40c7621ec9351c828ecd241ee7de32c61160ce809f9f.jpg)

![](images/15c1b603479e6878242a407605e2fe0e0b1169ff9dbea390f8774f0ca70cde73.jpg)  
  
Fig. 1. (a) Measurement protocol for parameter extraction [15]. The pulsewidth (tP) was swept from 200 ns to 1 ms in increments of $1 . 5 \times .$ , and then, the amplitude (VP) was stepped in increments of 100 mV. The conditioning and read amplitude $V _ { R }$ was set to 2.5 V. (b) Partial polarization data (dots) and fit NLS model (solid line). (c) Extracted distribution of effective activation field $g ( \dot { E } _ { a } )$

for FE–dielectric (FE–DE) stacks and device variability are analyzed in Section IV.

# II. FIELD-DEPENDENT NLS MODEL FOR POLARIZATION REVERSAL

In the NLS model, the FE film is characterized as an ensemble of elementary regions that switch independently with a distribution of time constants [12]. These regions correspond to the grains in a polycrystalline FE film, considering that domain wall motion stops at the grain boundary and does not propagate to an adjacent grain. It is assumed that the switching of a grain occurs once a domain of reversed polarization is nucleated, and the wait time for the first nucleation event is much larger than the time needed for a nucleated domain wall to expand and occupy the entire grain. The NLS theory presented in [12] originally assumed that nucleation events occur spontaneously at a constant rate $1 / \tau .$ , so the switching of a grain was modeled as a Poisson process, where the cumulative distribution function (cdf) of the switching time $t _ { S }$ is

$$
P \left(t _ {S} <   t \mid \tau\right) = 1 - \exp \left(- \frac {t}{\tau}\right). \tag {1}
$$

However, according to the classical nucleation theory, the nucleation rate is not constant [19]. Domain nucleation occurs in a series of stages, starting with an incubation period where small clusters with reversed FE polarization continuously form and decompose, the distribution of which evolves over time until a quasi-steady-state distribution is reached. During this period, the nucleation rate increases monotonically until it becomes almost constant [19]. The assumption of constant nucleation rate was originally introduced as a special case to model the polarization reversal in an infinite crystal [20], where multiple nucleation events occur until the FE volume has reversed its polarization. In this regime, the incubation period could be safely ignored, but it can be the dominant factor in a polycrystalline FE where the switching time is determined by the first nucleation event.

Based on experimental results, 1 was generalized to a stretched exponential with parameter β [13], [14], which can be interpreted as a Weibull process [21] where the cdf for the

switching time is given by

$$
P \left(t _ {S} <   t \mid \tau , \beta\right) = 1 - \exp \left[ - \left(\frac {t}{\tau}\right) ^ {\beta} \right]. \tag {2}
$$

This results in a time-dependent switching rate

$$
r (t) = \frac {\beta}{\tau} \left(\frac {t}{\tau}\right) ^ {\beta - 1} \tag {3}
$$

as opposed to a constant nucleation rate. Note that for $\beta = 1$ , this reduces to a Poisson process with constant rate $1 / \tau$ . With $\beta > 1$ , a monotonically increasing nucleation rate is obtained, which provides an approximation for the FE nucleation during the incubation period.

The distribution of time constants in 2 can be associated with variations in the local electric field in the FE film [13], [14]. Under this assumption, the time constant τ is a function of the local field E and an activation field $E _ { a } ,$ which can be expressed by the empirical relation [14], [22]

$$
\tau \left(E _ {a}, E\right) = \tau_ {\infty} \exp \left[ \left(\frac {E _ {a}}{E}\right) ^ {a} \right] \tag {4}
$$

where $\tau _ { \infty }$ is the time constant obtained for an infinite applied field and α is an empirical parameter. Assuming an inhomogeneous and field-independent dielectric permittivity, the local electric field is expressed as $E \ : = \ : \eta E _ { \mathrm { F E } }$ , where $E _ { \mathrm { F E } }$ is an applied constant field across the FE and η is a random variable with probability density function (pdf) $f ( \eta )$ and unity mean, defined in the interval [0, ∞) [14]. The polarization reversal from $- P _ { S } ~ \mathrm { t o } ~ { + } P _ { S }$ is computed as the expectation of (2) over the distribution of local field variations f (η)

$$
\begin{array}{l} P \left(E _ {\mathrm {F E}}, t\right) = - P _ {S} \\ + 2 P _ {S} \int_ {0} ^ {\infty} P \left(t _ {S} <   t \mid \tau \left(E _ {a}, \eta E _ {\mathrm {F E}}\right), \beta\right) f (\eta) d \eta . \tag {5} \\ \end{array}
$$

With this mathematical formulation, the FE film is characterized by the parameters $P _ { S } , E _ { a } , \beta , \alpha , \tau _ { \infty }$ , and the pdf $f ( \eta )$ . As shown in [15], $f ( \eta )$ is well described by a generalized beta distribution of type 2, whose pdf is

$$
G B 2 (\eta | a, b, p, q) = \frac {(| a | / b) (\eta / b) ^ {a p - 1}}{B (p , q) [ 1 + (\eta / b) ^ {a} ] ^ {p + q}} \tag {6}
$$

where $B ( p , q )$ is the beta function. Fig. 1 shows the measurements of polarization reversal and the fit field-dependent

TABLE I FE PARAMETERS EXTRACTED FROM POLARIZATION REVERSAL MEASUREMENTS   

<table><tr><td>Parameter</td><td>f(η)</td><td>g(Ea′)</td></tr><tr><td>Ea</td><td>1.77 MV/cm</td><td>-</td></tr><tr><td>a</td><td>12.1</td><td>12.1</td></tr><tr><td>b</td><td>0.99</td><td>1.79 MV/cm</td></tr><tr><td>p</td><td>0.633</td><td>0.691</td></tr><tr><td>q</td><td>0.691</td><td>0.633</td></tr><tr><td>PR</td><td colspan="2">22.9 μC/cm2</td></tr><tr><td>τ∞</td><td colspan="2">387 ns</td></tr><tr><td>α</td><td colspan="2">4.11</td></tr><tr><td>β</td><td colspan="2">2.07</td></tr></table>

NLS model for an HZO film with thickness $T _ { \mathrm { F E } } = 8 . 3$ nm (fabrication details available in [18]). The time constant of the measurement setup was estimated to be below 10 ns, as described in [15]. Therefore, programming pulses above 200 ns were applied to ensure that the measurements are not limited by RC delays. The extracted parameters are shown in Table I. The extracted minimum time constant is over 30× larger than the time constant of the experimental setup, which indicates that the speed limitation is intrinsic to this particular ferroelectric (FE) film.

Note that due to the form of (4), a distribution of local fields is mathematically equivalent to a distribution of effective activation fields $E _ { a } ^ { \prime } = E _ { a } / \eta$ with probability density

$$
g \left(E _ {a} ^ {\prime}\right) = \frac {\eta^ {2}}{E _ {a}} f (\eta). \tag {7}
$$

The resulting pdf is shown in Fig. 1(c), which is also a generalized beta distribution of type 2. The parameters obtained with this formulation are shown in Table I under $g ( E _ { a } ^ { \prime } )$ and are used in the subsequent simulations. An offset voltage of $V _ { \mathrm { O S } } ~ = ~ 8 0$ mV was measured from P–V loops, such that $V _ { \mathrm { F E } } = V _ { A } + V _ { O S }$ , where $V _ { A }$ is the applied voltage and $V _ { \mathrm { F E } }$ is the actual voltage across the FE. This offset was considered during parameter extraction and applied to all simulations. The field at the FE is computed as $E _ { \mathrm { F E } } = V _ { \mathrm { F E } } / T _ { \mathrm { F E } }$ .

# III. MONTE CARLO SIMULATION FRAMEWORK

For the Monte Carlo simulation, a set of N grains $g ^ { ( i ) } , i \in$ $( 1 , N )$ is initialized by sampling values of activation fields $E _ { a } ^ { ( i ) }$ from the distribution $g ( E _ { a } ^ { \prime } )$ . The parameters, $P _ { S } , \beta , \alpha ,$ , and $\tau _ { \infty } ,$ are common to all the FE grains. Each FE grain can have one of two possible orientations, corresponding to a positive or negative polarization state $( s ^ { ( i ) } = \pm 1 )$ , and the time evolution of each grain is governed by (2) and (4). The simulation is first introduced for the simple case of polarization reversal and then generalized to arbitrary input waveforms.

# A. Polarization Reversal Simulation

For a polarization reversal simulation from $- P s$ to $P _ { S } ,$ , all grains are initialized to the state $s ^ { ( i ) } = - 1$ . Under a constant applied field, a grain $g ^ { ( i ) }$ has a fixed time constant $\tau ^ { ( i ) }$ given by (4). The simulation is performed by dividing the time into discrete-time intervals and computing the probability of transition for each unswitched grain according to (2). This is

![](images/fb75dc04c1edb93e8fe8227e36230b12a8445a72b724115a3f1302aebaa38bf6.jpg)  
Fig. 2. Polarization reversal simulation with the NLS model (red dashed lines) and Monte Carlo simulation with 5000 grains (black lines) are indistinguishable. Monte Carlo simulations with 100 grains (gray lines) show variation around the mean value (10 repetitions).

expressed as the probability that the switching time tS is in the time interval $[ t , t + \Delta t ]$ , given that the grain has not switched until t

$$
P ^ {(i)} \left(t _ {S} <   t + \Delta t \mid t _ {S} > t\right) = 1 - \exp \left[ \left(\frac {t}{\tau^ {(i)}}\right) ^ {\beta} - \left(\frac {t + \Delta t}{\tau^ {(i)}}\right) ^ {\beta} \right]. \tag {8}
$$

For each grain, the switching probability is evaluated as a Bernoulli trial with probability $P ^ { ( i ) }$ , and the state $s ^ { ( i ) }$ is updated to 1 in case of success. The total polarization due to the orientation of the FE grains is computed as

$$
P _ {F E} (t) = \frac {P _ {S}}{N} \sum_ {i = 1} ^ {N} s ^ {(i)} (t). \tag {9}
$$

For simplicity, it is assumed that the FE grains have the same area, but this can be generalized to account for different areas [12]. The Monte Carlo simulation for polarization reversal is summarized in Algorithm 1.

# Algorithm 1 Monte Carlo Polarization Reversal

Instantiate FE:

Define parameters $\{ P _ { S } , \beta , \alpha , _ { z \infty } \}$

Sample N activation fields $E _ { a } ^ { ( i ) }$ ∞from $g ( E _ { a } ^ { \prime } )$

Initialization: for grains $g ^ { ( i ) } , i \in ( 1 , N )$

$$
s ^ {(i)} \leftarrow - 1
$$

$$
\tau^ {(i)} \leftarrow \tau_ {\infty} \exp \left[ \left(E _ {a} ^ {(i)} / E _ {F E}\right) ^ {\alpha} \right]
$$

Simulation: for timestep [t , t + t ] and grains $g ^ { ( i ) } , i \in ( 1 , N )$

$$
\text {i f} s ^ {(i)} = - 1
$$

$$
P ^ {(i)} \leftarrow 1 - \exp \left[ \left(t / \tau^ {(i)}\right) ^ {\beta} - \left(\left(t + \Delta t\right) / \tau^ {(i)}\right) ^ {\beta} \right]
$$

$$
i f \operatorname {B e r n o u l l i} \left(P ^ {(i)}\right) = 1
$$

$$
s ^ {(i)} \leftarrow 1
$$

$$
e n d i f
$$

$$
e n d i f
$$

Fig. 2 shows the Monte Carlo simulations of polarization reversal and the analytic polarization reversal computed with the NLS model with the same parameters (see Table I). A Monte Carlo simulation with 5000 grains is indistinguishable from the NLS model, whereas 10 runs with 100 grains show variability around the mean value.

Note that, as shown in 8, the switching probability has an accumulation effect over time, even for a constant

applied field. Therefore, the state of a grain is not only determined by its polarization $s ^ { ( i ) } = \pm 1$ but also depends on the accumulated stimuli $t / \tau$ .

# B. Generalization to Arbitrary Input Waveforms

For an arbitrary field at the FE $E _ { \mathrm { F E } } ( t )$ , the time constant $\tau ^ { ( i ) }$ is a function of time, so the accumulated stimuli $t / \tau$ is replaced by an auxiliary history parameter $h ^ { ( i ) } ( t )$ that is defined as

$$
h ^ {(i)} (t) = \int_ {t _ {o}} ^ {t} \frac {d t ^ {\prime}}{\tau \left(E _ {\mathrm {F E}} \left(t ^ {\prime}\right) , E _ {a} ^ {(i)}\right)} \tag {10}
$$

where $t _ { o }$ indicates the time at which the stimuli to switch the grain started. The switching rate is expressed as

$$
r ^ {(i)} (t) = \frac {\beta}{\tau^ {(i)} (t)} \left(h ^ {(i)} (t)\right) ^ {\beta - 1} \tag {11}
$$

which results in a switching probability

$$
\begin{array}{l} P ^ {(i)} \left(t _ {S} <   t + \Delta t \mid t _ {S} > t\right) \\ = 1 - \exp \left[ \left(h ^ {(i)} (t)\right) ^ {\beta} - \left(h ^ {(i)} (t + \Delta t)\right) ^ {\beta} \right]. \tag {12} \\ \end{array}
$$

The Monte Carlo simulation is performed, as shown in Algorithm 2. After instantiating an FE with N grains, the state of each grain is initialized by defining its polarization $s ^ { ( i ) } = \pm 1$ and setting the history parameter to 0. Note that only a scalar value $\boldsymbol { h } ^ { ( i ) }$ is stored for each grain and updated during the simulation. Given that the FE switching can occur in both directions (i.e., from 1 to 1 or from 1 to 1), it is first verified that a grain is not already aligned with the external field. For the grains that are not aligned with the external field, the history parameter is updated to compute the switching probability, which is evaluated as a Bernoulli trial and the state of the grain is updated in case of success. Finally, the history parameter is updated when a grain switches according to a given relaxation rule, which needs to be determined. For a first approximation, two possible cases are evaluated: reset $\boldsymbol { h } ^ { ( i ) }$ to 0 after a grain has switched or keep its current value.

The experimental protocol in Fig. 3(a) was applied to validate the Monte Carlo simulation and evaluate the relaxation condition for $\boldsymbol { h } ^ { ( i ) }$ . Starting with the FE fully polarized to the $+ P s$ state that has been resting for a minute, a double triangular waveform is applied. The first pulse completely polarizes the FE to the $- P s$ state, whereas the second pulse is used to measure and subtract the current due to the dielectric response and leakage. After a hold time $T _ { H } ,$ , a double triangular waveform of the opposite polarity is applied to polarize the FE to the $+ P _ { S }$ state. After another hold time $T _ { H }$ , the procedure is repeated. The measured polarization response is plotted over the applied voltage in Fig. 3(b) with a 10-s hold time between pulses, which shows that transitions 1 and 3 (from $+ P _ { S } ~ { \mathrm { t o } } ~ - P _ { S } )$ follow the same trajectories. Likewise, transitions 2 and 4 (from $- P s$ to $+ P s )$ also overlap. When the history parameter is reset after a grain switches $( \mathrm { i } . \mathrm { e } . , h ^ { ( i ) } = 0 )$ , the Monte Carlo simulation closely matches the experiment, shown with red lines in Fig. 3(b). When the hold time is reduced to 10 ms, a different behavior is observed. The first transition from $- P s$ to $P _ { S }$ follows the same path as the

# Algorithm 2 General Monte Carlo Simulation

# Instantiate FE:

Define parameters $\{ P _ { S } , \beta , \alpha , \tau _ { \infty } \}$

Sample N activation fields $E _ { a } ^ { ( i ) }$ ∞from $g ( E _ { a } ^ { \prime } )$

Initialization: for grains $g ^ { ( i ) } , i \in ( 1 , N )$

$$
\begin{array}{l} s ^ {(i)} \leftarrow 1 \text {o r} s ^ {(i)} \leftarrow - 1 \\ h ^ {(i)} \leftarrow 0 \\ \end{array}
$$

Simulation: for timestep [t , $t + \Delta t ]$ and grains $g ^ { ( i ) } , i \in ( 1 , N )$

$$
\text {i f} s ^ {(i)} E (t) <   0
$$

$$
\tau^ {(i)} \leftarrow \tau_ {\infty} \exp \left[ \left(E _ {a} ^ {(i)} / | E (t) |\right) ^ {\alpha} \right]
$$

$$
h _ {n e w} ^ {(i)} \leftarrow h ^ {(i)} + \Delta t / \tau^ {(i)}
$$

$$
P ^ {(i)} \leftarrow 1 - \exp \left[ \left(h ^ {(i)}\right) ^ {\beta} - \left(h _ {n e w} ^ {(i)}\right) ^ {\beta} \right]
$$

$$
h ^ {(i)} \leftarrow h _ {n e w} ^ {(i)}
$$

$$
\text {i f} \operatorname {B e r n o u l l i} \left(P ^ {(i)}\right) = 1
$$

$$
\text {U p d a t e} s ^ {(i)}
$$

$$
h ^ {(i)} \mathrm {r e l a x a t i o n}
$$

end if

end if

![](images/bf7dec04ab244a525ea39bd04d747819bb6d61476b4cded8e04470dcc9563f2c.jpg)  
Fig. 3. (a) Experimental protocol to measure P–V loops. A double triangular waveform $V _ { A }$ is applied. The first triangle produces a current due to the linear capacitance and the polarization reversal. The displacement current due to the linear capacitance alone is measured by the second triangle, where there is no polarization current. A hold time $\mathit { \Pi } _ { T _ { H } }$ is applied between polarization pulses. Measured and simulated $P - \dot { V }$ loops with (b) 10-s hold time and (c) 1-ms hold time.

case with a 10-s hold time, given that the initial condition is the same. However, the subsequent transitions occurs at a lower voltage (earlier in time), as shown in Fig. 3(c). This apparent speedup has been observed in similar experiments and could be related to the distribution of clusters after a

![](images/b3393810b05515ca7493d7b5a15ce33b44f14fced7cc748f1cae44e5f282db16.jpg)  
(a)

![](images/e2d2372c2e24b0868f37f3934c673ced139e89aa38c02f5f8f74082f2c0ed4fe.jpg)  
  
Fig. 4. Experimental validation of Monte Carlo simulation framework. (a) Measured and simulated polarization versus time for an 8.3-nm HZO capacitor with a triangular input waveform of varying amplitude. (b) Measured and simulated major and minor loops obtained from (a) with detail of the transition between minor loops and major loops.

grain switches [23]. A simulation performed for the extreme case, where $h ^ { ( i ) } ( t )$ is not reset between transitions, produces a similar behavior [red lines in Fig. 3(b)].

Having verified that the Monte Carlo model closely matches the measurements of saturated P–V loops, the model predictions were evaluated for minor loops. Fig 4(a) and (b) shows the experimental and simulated data taken with a triangular waveform of varying amplitude. Under these conditions, the dielectric response is not canceled, as shown in Fig. 3, so the total FE charge is modeled as

$$
Q _ {\mathrm {F E}} (t) = P _ {\mathrm {F E}} (t) + \epsilon_ {\mathrm {F E}} E (t) \tag {13}
$$

where $\epsilon _ { \mathrm { F E } }$ is the permittivity of the FE film. For this simulation, $h ^ { ( i ) } ( t )$ was not reset between transitions, as shown in Fig. 3(c). The Monte Carlo simulation accurately predicts the behavior of the FE as it enters and exits the minor loops, as well as the drifting of the minor loops with field cycling. Small differences between the measured and simulated characteristics occur in part due to the assumption of a constant FE capacitance, whereas the measured capacitance exhibits the well-known butterfly shape [15].

# C. Further Study of Accumulation and Relaxation of the History-Dependent Switching Rate

Based on the experimental results, it has been observed that resetting the history parameter when a grain switches works well when a long resting period is applied between the pulses. For shorter resting periods or for periodic stimuli, not resetting $h ( t )$ produces a close match with experimental measurements, although this extreme case results in a continuously increasing rate that will slowly depart from experiments. Therefore, a more general reset condition would be to set $\boldsymbol { h } ^ { ( i ) }$ to a certain reset value $h _ { S }$ , which may be a function of the history parameter before switching and the grain parameters. In addition, a relaxation rule for the history parameter could be incorporated when there is no applied field or when the grain is already aligned with the external field. Such effects could be incorporated into the simulation as shown in Algorithm 3, although its functional form remains to be determined.

![](images/28af9b8d31b283a245a9d8d4827a55b0624765df77e5aa54ddf5864313eb8783.jpg)  
Fig. 5. Measured (markers) and simulated (solid lines) polarization obtained by pulsewidth modulation (diamonds) and a train of pulses (dots) with equivalent accumulated time.

The measurement protocol in Fig. 5 was applied to better understand the timescale of the relaxation behavior (the conditioning and readout protocols are the same, as shown in Fig. 1). Starting with an FE fully polarized in the $- P s$ state, either a single pulse of varying width or a train of pulses with equivalent accumulated pulsed time are applied. The width-modulated pulse ranges from 1 to 20 $\mu \mathbf { S } .$ The train of pulses has a constant pulsewidth of 1 $\mu \mathbf { S } ,$ with off time between the pulses $t _ { O F F }$ of either 1 or 10 $\mu \mathbf { S } .$ Amplitudes of 1, 1.25, and 1.5 V are applied for both the width-modulated pulse and the train of pulses.

The Monte Carlo simulation was implemented according to Algorithm 3, by applying a simple relaxation rule during the off time between the pulses, which is defined as

$$
h ^ {(i)} \leftarrow h ^ {(i)} \times \gamma \left(t _ {\text {O F F}}\right). \tag {14}
$$

By setting $\gamma = 0 . 5 5$ for a 1-μs off time between the pulses and $\gamma = 0 . 3$ for $1 0 \mathrm { - } \mu \mathrm { s }$ off time, the simulation closely matches the experiment for the pulses of 1-, 1.25-, and 1.5-V amplitude.

![](images/5f3373f30a27b0cd304d2a023bbcae9462314bee343874815fdd6972d8076e47.jpg)  
(a)

![](images/6a5bc60f0134339d250a5df1e0897d26ecf8ab3b3e8bfbd80b81847c16eae249.jpg)  
(b)   
Fig. 6. (a) Simulation of FE–DE P–V loops with L-K model for single-grain FE and Monte Carlo simulation of polycrystalline FE. (b) Monte Carlo simulation of polarization versus time of an FE capacitor and FE–DE structures with different dielectric capacitances, programmed with square waveforms of amplitudes 3 and 4 V with 2- and 5-µs period.

<table><tr><td colspan="2">Algorithm 3 Monte Carlo Simulation With the Proposed Relaxation</td></tr><tr><td colspan="2">Instantiate FE:</td></tr><tr><td colspan="2">Define parameters {PS, β, α, τ∞}</td></tr><tr><td colspan="2">Sample N activation fields Ea(i) from g(Ea&#x27;)</td></tr><tr><td colspan="2">Initialization: for grains g(i), i ∈ (1, N)</td></tr><tr><td colspan="2">s(i)← 1 or s(i)← -1</td></tr><tr><td colspan="2">h(i)← 0</td></tr><tr><td colspan="2">Simulation: for timestep [t, t+Δt] and grains g(i), i ∈ (1, N)</td></tr><tr><td colspan="2">if s(i)E(t) &lt; 0</td></tr><tr><td colspan="2">τ(i)← τ∞exp[(Ea(i)/|E(t)|)α]</td></tr><tr><td colspan="2">h(new)(i)← h(i) + Δt/τ(i)</td></tr><tr><td colspan="2">P(i)←1-exp[(h(i))β-(h(new)i)β]</td></tr><tr><td colspan="2">h(i)← h(new)i</td></tr><tr><td colspan="2">if Bernoulli(P(i)) = 1</td></tr><tr><td colspan="2">Update s(i)</td></tr><tr><td colspan="2">h(i)← hS</td></tr><tr><td colspan="2">end if</td></tr><tr><td colspan="2">else</td></tr><tr><td colspan="2">Relax h(i) // when s(i)E(t) ≥ 0</td></tr><tr><td colspan="2">end if</td></tr></table>

It is proposed that further investigation of the dynamics of formation and decomposition of clusters in the incubation period will lead to a direct relation between the switching rate and the underlying distribution of clusters in order to define improved accumulation and relaxation equations.

# IV. MODEL PREDICTIONS

FE–DE stacks are integral to many proposed FE devices in both memory and logic [5]. The Monte Carlo simulation framework was applied to model these structures and understand the key differences between polycrystalline FE films and a single-grain FE. The single-grain FE is simulated by the single-domain Landau–Khalatnikov (L-K) model [11]. Although this is a simplified model for illustrative purposes, it produces a close resemblance to the behavior obtained with a multidomain analysis [24]. Fig. 6(a) shows the simulated P–V loops for an 8.3-nm HZO capacitor and an FE–DE stack

of an 8.3-nm HZO film and a series dielectric with different capacitance ratios $C _ { \mathrm { D E } } / C _ { \mathrm { F E } }$ . The P–V loops are simulated with a triangular waveform of 4-ms period and 3-V amplitude. According to the L-K model, adding a series capacitor results in a decreased switching voltage with an abrupt transition, suggesting that the programming voltage of an FE–DE stack can be lower than that of an FE capacitor. However, this behavior is not observed with a polycrystalline FE [18]. As shown in the Monte Carlo simulation in Fig. 6(a), the switching starts at a lower voltage due to the depolarizing field of the DE, but the transition is not abrupt. The depolarizing field of the DE aids switching only when the magnitude of FE polarization is decreasing (i.e., from $\pm P s$ to 0) but opposes the switching when its magnitude is increasing (i.e., from 0 to $\pm P s )$ . Therefore, as the DE capacitance decreases (DE thickness increases), fewer FE grains switch under the same programming conditions. Fig. 6(b) shows the Monte Carlo simulations of the polarization versus time for the same FE and FE–DE capacitors when a square programming waveform is applied, with 2- and $5 \mathrm { - } \mu \mathrm { s }$ period and amplitudes of 3 and 4 V. Irrespective of the pulse duration, the FE–DE starts switching earlier than the FE but takes a longer time to settle. As the DE capacitance decreases, the switched polarization is reduced due to the effect of the depolarizing field. Multidomain simulations of FE switching have also shown a reduction or inhibition of the voltage amplification predicted by the L-K model [25]–[28]. However, these simulations do not consider grain boundaries, which may be the dominant effect in a polycrystalline FE.

The Monte Carlo modeling approach also allows for the investigation of the effects of device-to-device variability due to the grains having a distribution of activation fields. Fig. 7(a) shows the simulated device-to-device variations of an 8.3-nm FE capacitor initialized with 500, 100, and 20 grains, programmed with a square waveform with 20-μs period. For each case, the simulation is repeated 200 times and plotted with black lines, whereas the red line shows the mean value of all simulations. With a 1.5-V programming amplitude, a $2 P _ { S }$ memory window is obtained for 500 grains, which is reduced by approximately 50% for 20 grains. For a 1.25-V programming voltage, the memory window collapses with 20 grains. Fig. 7(b) shows the device-to-device variations of

![](images/671c0771bea73efa8f6804224aeb9cc49e1cbe929d3c783215812e3ab36092b7.jpg)

![](images/4609f74305205165dde0789a0a74564f65c3d268c704601104dfde6dfc8c2184.jpg)  
  
Fig. 7. Simulated device-to-device variations of 200 devices (black line) with 500, 100, and 20 grains for (a) 8-nm-thick FE and (b) FE–DE capacitor with $C _ { \mathsf { D E } } = 5 C _ { \mathsf { F E } }$ . With 20 grains, the memory window of the FE is reduced by 50% with respect to the mean value (red line) for a 1.5-V programming voltage and is completely lost with 1.25 V. With the same number of grains, the FE–DE requires a programming voltage above 1.5 V to obtain a memory window.

![](images/d3c4fa9c770068755e6975c51ecf0f099c485d08de5372b3b9d8d431ccb4778a.jpg)  
Number of pulses   
Fig. 8. Switching simulations of a three-grain FE capacitor with the activation fields of 1, 1.8, and 2.6 MV/cm under a train of pulses with 2-V amplitude and 100-ns width. The simulation is repeated five times, represented by different colors. The switching events for each grain are plotted as a function of the number of pulses, showing the inherent variability of the FE response. The normalized polarization is computed, assuming that the grains contribute a 0.45, 0.35, and 0.2 fraction of the total area.

an FE–DE stack with $C _ { \mathrm { D E } } = 5 C _ { \mathrm { F E } }$ under the same conditions. In this case, a 1.5-V programming voltage produces a memory window close to $P _ { S }$ for 500 grains and close to 0 for 20 grains. The programming voltage needs to be increased to 2 V to obtain similar memory windows than an FE with 1.5-V programming voltage.

Finally, the model is applied to analyze the stochastic switching behavior and accumulation effect in an FE capacitor with only 3 grains, as shown in Fig. 8. The grains are

initialized with the activation fields of 1, 1.8, and 2.6 MV/cm, and it is assumed that the grains have the same polarization $P _ { S }$ , but different areas. The switching instants for five repetitions of a train of pulses show that grains with a higher activation field switch after a larger number of pulses, and the stochastic switching time is captured by the simulation. The resulting polarization shows a stair-like behavior, similar to what has been previously observed [29].

It is important to emphasize that this is a model for polycrystalline FE in a nucleation-limited regime. A fundamental assumption of nucleation-limited models is that the nucleation time dominates the polarization dynamics, whereas the transient of domain growth within a grain is negligible. This assumption does not necessarily hold for highly scaled FE, especially when there is a large series capacitance that stabilizes the domain wall expansion regime [24].

# V. CONCLUSION

A Monte Carlo simulation framework, which is capable of predicting the dynamic, history-dependent response of an FE under arbitrary input waveforms, is presented. After a parameter extraction procedure from polarization reversal measurements, the proposed model can predict the polarization response of an HZO FE capacitor under different experimental conditions with the same set of parameters. The model was applied to characterize the dynamic response of FE–DE bilayer structures, showing that the response of polycrystalline FE is significantly different than that of single-grain FE. With the proposed model, the reduction in memory window due to device variability can also be quantified, both for FE capacitors and FE–DE stacks. Finally, an accumulation effect that leads to grain switching was studied and modeled for the first time by a history parameter. This effect is in agreement with a classical nucleation theory, and further theoretical and experimental study is proposed as future work to establish a direct relation

between the history-dependent switching probability and the underlying distribution of clusters during the incubation period of domain nucleation.

# REFERENCES

[1] T. S. Böscke, J. Müller, D. Bräuhaus, U. Schröder, and U. Böttger, “Ferroelectricity in hafnium oxide: CMOS compatible ferroelectric field effect transistors,” in IEDM Tech. Dig., Dec. 2011, pp. 24.5.1–24.5.4. doi: 10.1109/IEDM.2011.6131606.   
[2] X. Li et al., “Advancing nonvolatile computing with nonvolatile NCFET latches and flip-flops,” IEEE Trans. Circuits Syst. I, Reg. Papers, vol. 64, no. 11, pp. 2907–2919, Nov. 2017. doi: 10.1109/TCSI.2017.2702741.   
[3] A. Sharma and K. Roy, “1T non-volatile memory design using sub-10nm ferroelectric FETs,” IEEE Electron Device Lett., vol. 39, no. 3, pp. 359–362, May 2018. doi: 10.1109/LED.2018.2797887.   
[4] D. Kwon et al., “Improved subthreshold swing and short channel effect in FDSOI n-channel negative capacitance field effect transistors,” IEEE Electron Device Lett., vol. 39, no. 2, pp. 300–303, Feb. 2018. doi: 10.1109/LED.2017.2787063.   
[5] A. Aziz et al., “Computing with ferroelectric FETs: Devices, models, systems, and applications,” in Proc. Design, Automat. Test Eur. Conf. Exhib., Mar. 2018, pp. 1289–1298. doi: 10.23919/DATE.2018.8342213.   
[6] E. W. Kinder, C. Alessandri, P. Pandey, G. Karbasian, S. Salahuddin, and A. Seabaugh, “Partial switching of ferroelectrics for synaptic weight storage,” in Proc. 75th Annu. Device Res. Conf. (DRC), Jun. 2017, pp. 1–2. doi: 10.1109/DRC.2017.7999427.   
[7] S. Oh et al., “HfZrOx -based ferroelectric synapse device with 32 levels of conductance states for neuromorphic applications,” IEEE Electron Device Lett., vol. 38, no. 6, pp. 732–735, Jun. 2017. doi: 10.1109/LED.2017.2698083.   
[8] H. Mulaosmanovic, T. Mikolajick, and S. Slesazeck, “Accumulative polarization reversal in nanoscale ferroelectric transistors,” ACS Appl. Mater. Interfaces, vol. 10, no. 28, pp. 23997–24002, Jun. 2018. doi: 10.1021/acsami.8b08967.   
[9] K. Ni, M. Jerry, J. A. Smith, and S. Datta, “A circuit compatible accurate compact model for ferroelectric-FETs,” in Proc. IEEE Symp. VLSI Technol., Jun. 2018, pp. 131–132. doi: 10.1109/VLSIT.2018.8510622.   
[10] B. Obradovic, T. Rakshit, R. Hatcher, J. A. Kittl, and M. S. Rodder, “Ferroelectric switching delay as cause of negative capacitance and the implications to NCFETs,” in Proc. IEEE Symp. VLSI Technol., Jun. 2018, pp. 51–52. doi: 10.1109/VLSIT.2018.8510628.   
[11] A. K. Saha, S. Datta, and S. K. Gupta, “‘Negative capacitance’ in resistor-ferroelectric and ferroelectric-dielectric networks: Apparent or intrinsic?” J. Appl. Phys., vol. 123, no. 10, Feb. 2018, Art. no. 105102. doi: 10.1063/1.5016152.   
[12] A. K. Tagantsev, I. Stolichnov, N. Setter, J. S. Cross, and M. Tsukada, “Non-Kolmogorov–Avrami switching kinetics in ferroelectric thin films,” Phys. Rev. B, Condens. Matter, vol. 66, no. 21, Dec. 2002, Art. no. 214109. doi: 10.1103/PhysRevB.66.214109.   
[13] J. Y. Jo, H. S. Han, J.-G. Yoon, T. K. Song, S.-H. Kim, and T. W. Noh, “Domain switching kinetics in disordered ferroelectric thin films,” Phys. Rev. Lett., vol. 99, no. 26, Dec. 2007, Art. no. 267602. doi: 10.1103/PhysRevLett.99.267602.

[14] S. Zhukov, Y. A. Genenko, O. Hirsch, J. Glaum, T. Granzow, and H. von Seggern, “Dynamics of polarization reversal in virgin and fatigued ferroelectric ceramics by inhomogeneous field mechanism,” Phys. Rev. B, Condens. Matter, vol. 82, no. 1, Jul. 2010, Art. no. 014109. doi: 10.1103/PhysRevB.82.014109.   
[15] C. Alessandri, P. Pandey, A. Abusleme, and A. Seabaugh, “Switching dynamics of ferroelectric Zr-Doped HfO2,” IEEE Electron Device Lett., vol. 39, no. 11, pp. 1780–1783, Nov. 2018. doi: 10.1109/LED.2018.2872124.   
[16] N. Gong, X. Sun, H. Jiang, K. S. Chang-Liao, Q. Xia, and T. P. Ma, “Nucleation limited switching (NLS) model for HfO2-based metal-ferroelectric-metal (MFM) capacitors: Switching kinetics and retention characteristics,” Appl. Phys. Lett., vol. 112, no. 26, Jun. 2018, Art. no. 262903. doi: 10.1063/1.5010207.   
[17] Y. A. Genenko et al., “Universal polarization switching behavior of disordered ferroelectrics,” Adv. Funct. Mater., vol. 22, no. 10, pp. 2058–2066, 2012. doi: 10.1002/adfm.201102841.   
[18] C. Alessandri, P. Pandey, and A. Seabaugh, “Experimentally validated, predictive monte carlo modeling of ferroelectric dynamics and variability,” in IEDM Tech. Dig., Dec. 2018, pp. 16.2.1–16.2.4. doi: 10.1109/IEDM.2018.8614607.   
[19] R. W. Balluffi, S. Allen, and W. C. Carter, Kinetics of Materials, 1st ed. Hoboken, NJ, USA: Wiley, 2005.   
[20] Y. Ishibashi and Y. Takagi, “Note on ferroelectric domain switching,” J. Phys. Soc. Jpn., vol. 31, no. 2, pp. 506–510, 1971. doi: 10.1143/JPSJ.31.506.   
[21] W. Lee et al., “Investigation of time–dependent resistive switching behaviors of unipolar nonvolatile organic memory devices,” Adv. Funct. Mater., vol. 28, no. 35, Aug. 2018, Art. no. 1801162. doi: 10.1002/adfm.201801162.   
[22] J. F. Scott et al., “Switching kinetics of lead zirconate titanate submicron thin-film memories,” J. Appl. Phys., vol. 64, no. 2, pp. 787–792, 1988. doi: 10.1063/1.341925.   
[23] Y. Arayashiki, T. Nakajima, Y. Takahashi, and T. Furukawa, “Accelerated and decelerated polarization reversal in thin vinylidene fluoride/trifluoroethylene copolymer films,” IEEE Trans. Dielectr. Elect. Insul., vol. 17, no. 4, pp. 1066–1073, Aug. 2010. doi: 10.1109/TDEI.2010.5539676.   
[24] A. K. Yadav et al., “Spatially resolved steady-state negative capacitance,” Nature, vol. 565, no. 7740, pp. 468–471, 2019. doi: 10.1038/s41586-018-0855-y.   
[25] A. Cano and D. Jiménez, “Multidomain ferroelectricity as a limiting factor for voltage amplification in ferroelectric field-effect transistors,” Appl. Phys. Lett., vol. 97, no. 13, Sep. 2010, Art. no. 133509. doi: 10.1063/1.3494533.   
[26] S. Smith, K. Chatterjee, and S. Salahuddin, “Multidomain phasefield modeling of negative capacitance switching transients,” IEEE Trans. Electron Devices, vol. 65, no. 1, pp. 295–298, Jan. 2018. doi: 10.1109/TED.2017.2772780.   
[27] M. Hoffmann et al.k, “Ferroelectric negative capacitance domain dynamics,” J. Appl. Phys., vol. 123, no. 18, Apr. 2018, Art. no. 184101. doi: 10.1063/1.5030072.   
[28] M. Hoffmann, M. Peši´c, S. Slesazeck, U. Schroeder, and T. Mikolajick, “On the stabilization of ferroelectric negative capacitance in nanoscale devices,” Nanoscale, vol. 10, no. 23, pp. 10891–10899, 2018. doi: 10.1039/C8NR02752H.   
[29] H. Mulaosmanovic et al., “Switching kinetics in nanoscale hafnium oxide based ferroelectric field-effect transistors,” ACS Appl. Mater. Interfaces, vol. 9, no. 4, pp. 3792–3798, 2017. doi: 10.1021/acsami.6b13866.