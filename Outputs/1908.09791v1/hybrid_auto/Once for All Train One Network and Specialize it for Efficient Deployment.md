---
title: "'Once for All: Train One Network and Specialize it for Efficient Deployment'"
date: "'2019-08-01'"
year: 2019
journal: "arXiv preprint arXiv:1908.09791"
doi: "arXiv:1908.09791"
abstract: "Efficient deployment of deep learning models requires specialized neural"
abstract_cn: "提出 Once for All（OFA）方法：训练一个通用网络，支持不同深度、宽度、核大小和分辨率，无需重新训练即可派生 specialized"
cite: "'Cai H, Gan C, Han S. Once for All: Train One Network and Specialize it for"
aiSum: "OFA 通用网络：渐进收缩算法、支持 10^19 子网络、训练成本从 O(N) 降至 O(1)、比 NAS 快 14-1142 倍、多硬件平台部署。"
confidence: low
---

Number of Deployment Scenarios
  0        20        40        60        80       
14x~1142x 
reduction
direct deploy    (no retrain)
train a once-for-all network
specialized  sub-nets
59
63
66
70
73
77
15
35
55
75
95
115
135
Once for All
Once for All #25
Mnas
MobileNetV2
ProxylessNAS
FBNet
Samsung Note8 Latency (ms)
Top-1 ImageNet Acc (%)
60.3
65.4
69.8
72.0
69.0
71.1
74.3
75.3
cpu
F
P
G
A
Diﬀerent Hardware / Constraint
Design Cost
Previous: O(N) design cost
Ours: O(1) design cost
Need to Train

 Four Times
Train Once,

 Get Four
8.7%
Edge, 
Full battery
Edge, 
Low battery
Cloud
Figure 1: Left: a single once-for-all network is trained to support versatile architectural conﬁgurations
including depth, width, kernel size, and resolution. Given a deployment scenario, a specialized sub-
network is directly selected from the once-for-all network without training. Middle: this approach
reduces the cost of specialized deep learning deployment from O(N) to O(1). Right: once-for-all
network followed by model selection can derive many accuracy-latency trade-offs by training only
once, compared to conventional methods that require repeated training. See Table 2 for search cost
comparison and Figure 6 for results on more hardware platforms.
for efﬁcient deployment. However, designing specialized DNNs for every deployment scenario
is engineer-expensive and computationally expensive, either with human-based or AutoML-based
methods. Since such methods need to repeat the architecture design process and retrain the designed
network from scratch for each case. Their total cost grows linearly as the number of deployment
scenarios increases. It makes them unable to handle the vast amount of hardware devices (23.14
billion IoT devices till 20181) and highly dynamic deployment environments (different battery
conditions, varied workloads, different latency requirements, etc.). The NRE cost is high.
This paper introduces a new solution to tackle this challenge – designing a once-for-all network that
can be directly deployed under diverse architectural conﬁgurations. Inference can be performed by
selecting only part of the once-for-all network. It ﬂexibly supports different depths, widths, kernel
sizes, and resolutions without retraining. A simple example of Once for All (OFA) is illustrated in
Figure 1 (left). Speciﬁcally, we decouple the model training stage and model specialization stage. In
the model training stage, we train a single once-for-all network, from which various sub-networks with
different architectural conﬁgurations can be generated, and we focus on improving the accuracy of
each sub-network without interfering with each other. In the model specialization stage, we prebuild
the accuracy table and hardware efﬁciency (latency or energy) table for a subset of sub-networks. The
weights of the sub-networks are directly derived from the once-for-all network without retraining, so
this process is fast and computationally efﬁcient. Furthermore, since the accuracy table can be shared
among all hardware platforms, this cost is paid once. In the test time, given a deployment scenario,
we only need to query the accuracy table and hardware latency table to get a specialized sub-network,
and the cost is negligible. As such, we can reduce the cost of specialized neural network architecture
design from O(N) to O(1) (Figure 1 middle). However, training the once-for-all network is a non-
trivial task, since it requires joint optimization of the weights to maintain the accuracy of a large
number of sub-networks (more than 1019 in our experiments). It is computationally prohibitive to
enumerate all sub-networks and train each one individually. Even more challenging, sub-networks
share weights, but they shouldn’t interfere with each other. To address these issues, we propose
the progressive shrinking algorithm for training the once-for-all network. We ﬁrst train a neural
network with maximum depth, width, and kernel size, then progressively train the network to support
smaller sub-networks. This progressive shrinking scheme is crucial to prevent smaller sub-networks
from hurting the accuracy of larger sub-networks. Moreover, progressive shrinking also allows us
to provide good initialization and better supervision for small sub-networks with the help of large
sub-networks rather than training them from scratch.
We evaluate the effectiveness of our proposed framework on ImageNet with various hardware
platforms (Mobile/CPU/GPU) and efﬁciency constraints. Under all deployment scenarios, OFA
consistently achieves the same level (or better) ImageNet accuracy than state-of-the-art hardware-
1https://www.statista.com/statistics/471264/iot-number-of-connected-devices-worldwide/
2

aware NAS methods while being orders of magnitude more efﬁcient handling diverse deployment
scenarios.
2
Related Work
Efﬁcient Deep Learning.
Improving the efﬁciency of deep neural networks is crucial for deploying
deep learning algorithms on resource-constrained edge devices. Towards this goal, many efﬁcient
neural network architectures are proposed, such as SqueezeNet [14], MobileNets [11, 23], Shuf-
ﬂeNets [20,30], etc. Orthogonal to directly designing efﬁcient neural network architectures, model
compression [7] is another very effective technique for efﬁcient deep learning, which focuses on im-
proving the efﬁciency of a given neural network without affecting its accuracy. Speciﬁcally, network
pruning approaches achieve this by removing redundant units [8] or redundant channels [9,18] in a
neural network, while quantization approaches improve the efﬁciency by representing the weights
and activations of the neural network with low-bit representations [4,7,31].
Neural Architecture Search.
Manually designing neural network architectures requires tremen-
dous human effort, which is expensive and sub-optimal. Neural architecture search (NAS) focuses on
automating the architecture design process [1,16,22,32,33]. Early NAS methods [22,33] search for
high-accuracy neural network architectures without taking hardware efﬁciency into consideration.
Therefore, their searched architectures (e.g., NASNet, AmoebaNet) are not efﬁcient when deployed
on hardware platforms. Recent hardware-aware NAS methods [3,24,27] directly incorporate the
hardware feedback into the architecture search process as a part of the reward signal [3, 24] or a
loss regularization term [3,27] that makes latency differentiable. As such, they are able to design
specialized neural networks for different hardware platforms and efﬁciency constraints, showing
signiﬁcant improvements over non-specialized baselines (e.g., MobileNetV2). However, when a new
inference hardware platform appears, these methods need to repeat the architecture search process
and retrain the model. They are not scalable to a large number of deployment scenarios.
Dynamic Neural Networks.
The idea of training a single model to support different architectural
conﬁgurations is related to dynamic neural network approaches that focus on skipping part of an
existing model (e.g., ResNet50) based on input images. For example, [17,26,28] propose to learn
an additional controller or gating modules to adaptively drop blocks in a given neural network; [13]
introduces early-exit branches in the computation graph, allowing to exit in the middle based on the
current prediction conﬁdence; [15] proposes to adaptively prune channels based on the input feature
map at runtime; Slimmable Nets [29] train a model to support multiple width multipliers (speciﬁcally
4 different global width multipliers), building upon existing human-designed neural networks (e.g.,
MobileNetV2 0.35, 0.5, 0.75, 1.0). Such methods can save the computational cost while maintaining
the accuracy by skipping more when given easy input images and skipping less when given difﬁcult
input images. However, they inherit a pre-designed neural network, which limits their performances
on new deployment scenarios where the pre-designed neural network is not optimal. The degree of
ﬂexibility is also limited (e.g., only global width multiplier can adapt), and only a limited number of
architectural conﬁgurations are supported (e.g., 4).
3
Method
3.1
Problem Formalization
We start with formalizing the problem of training the once-for-all network that supports versatile
architectural conﬁgurations. We denote the weights of the once-for-all network as Wo and the
architectural conﬁgurations as {archi}. Then the problem can be formalized as
min
Wo
X
archi
Lval
 C(Wo, archi)

,
(1)
where C(Wo, archi) denotes a selection scheme that selects part of the model from the once-for-all
network Wo and forms a sub-network with architectural conﬁguration archi. For example, to get the
weights of a 3-layer sub-network from a 4-layer once-for-all network, one possible C(Wo, archi)
could be “taking the weights of the ﬁrst three layers”.
In this work, we explore four important dimensions of the convolutional neural network architectures,
i.e., depth, width, kernel size, and resolution. Other dimensions such as dilation and #groups can be
3

Once-
for-all
Network
K = 7
D = 4
W = 6
Train full 
network
Elastic Kernel Size
D = 4, W = 6
K !
 [7, 5, 3]
∈
Sample K at each layer
Generate kernel 
weights (Fig. 3)
Fine-tune weights & 
transformation matrix
Elastic Width
D !
 [4, 3, 2], K !
 [7, 5, 3]
∈
∈
Channel sorting 
Sample E at each 
Fine-tune weights
W !
 [6, 5, 4]
∈
W !
 [6, 5]
∈
Channel sorting 
(Fig. 5)
Sample W at each 
layer; sample K, D
Distill
Elastic Resolution
R !
 [128, 132, …, 224]
∈
Elastic Depth
W = 6, K !
 [7, 5, 3]
∈
Sample D at each 
Skip top (4-D) 
Fine-tune weights
D !
 [4, 3, 2]
∈
D !
 [4, 3]
∈
Sample D at each 
stage; sample K
Keep the ﬁrst D blocks 
at each stage (Fig. 4)
Fine-tune weights
Fine-tune weights
Distill
Distill
Figure 2: An example of the progressive shrinking process. We cover four important dimensions of
CNN architectures (depth D, width W, kernel size K and resolution R), resulting in a large space
comprising diverse sub-networks (> 1019).
7x7
Transformation  
Matrix: 25x25
5x5
Transformation  
Matrix: 9x9
3x3
Figure 3: Kernel transformation matrix for elastic kernel size. We support 7×7, 5×5, and 3×3
kernels. Weight sharing makes it more efﬁcient than independent settings.
naturally incorporated, and we leave them for future work. The overall objective is to train Wo to
make each supported sub-network achieving the same level of accuracy as independently training a
network with the same architectural conﬁguration.
3.2
Training the Once-for-all Network
Preliminary.
A convolutional neural network (CNN) typically consists of several stages. A stage
is a sequence of building blocks with the same resolution. In the network-level, we allow the model
to be executed under different input image sizes (i.e., elastic resolution). In the stage-level, we
allow each stage to skip different numbers of blocks (i.e., elastic depth). In the block-level, we
allow each block to use different numbers of channels (i.e., elastic width) and different kernel sizes
(i.e., elastic kernel size). Therefore, unlike previous methods that inherit a given neural network
architecture (e.g., ResNet, MobileNetV2) [9, 28, 29], we have a much more diverse architecture
space while allowing a signiﬁcantly larger number of architectural conﬁgurations (1019 v.s. 4 [29]) .
Thanks to the diversity and the large design space, we can derive new specialized neural networks
for many different deployment scenarios rather than working on top of existing pre-designed neural
networks. If a pre-designed neural network is inefﬁcient, the optimization headroom will be small
if directly working on top of it (Figure 6 and Figure 1 right). However, given such a large number
of sub-networks to support, it becomes challenging to train the once-for-all network to achieve this
ﬂexibility: the training cost should be affordable; different sub-networks shouldn’t interfere. In the
following section, we introduce an effective progressive shrinking approach to solve this problem.
A Progressive Shrinking Approach.
Instead of directly training the once-for-all network to sup-
port all sub-networks from scratch based on Eq. (1), which is difﬁcult to optimize, we propose to
decompose the optimization problem as a sequence of sub-tasks. An example of the progressive
shrinking process is provided in Figure 2. Speciﬁcally, we start with training a full neural network
with the maximum [width, depth, kernel size] under elastic resolution. Then we ﬁne-tune the neural
network to support both full [width, depth, kernel size] and partial [width, depth, kernel size] in a
progressive manner (from large sub-networks to small sub-networks).
This progressive shrinking scheme offers three unique advantages. First, it makes the once-for-all
network easier to optimize since each sub-task is much simpler than the full task. Second, small
models are easier to train with the help of large models. Progressive shrinking allows us to provide
4

stage i
stage i
train with full depth
stage i
progressively shrink the depth
progressively shrink the depth
O1
O2
O3
O1
O2
Figure 4: An overview of the training process for elastic depth. Instead of skipping each block
independently, we keep the ﬁrst D blocks and skip the last (4 −D) blocks. The weights of the blue
and green blocks are shared across D = 2, 3, 4; The orange block is shared across D = 3, 4.
train with full width
channel 
importance
0.02
0.15
0.85
0.63
channel 
sorting
progressively shrink the width
channel 
importance
0.82
0.11
0.46
reorg.
channel 
sorting
reorg.
progressively shrink the width
channel 
sorting
O1
O2
O3
O1
O2
O1
Figure 5: An overview of the progressive shrinking process for elastic width. In this example, we
progressively support 4-, 3-, and 2-channel settings. Smaller channel settings are initialized with the
most important channels (large L1 norm) after channel sorting.
good initialization for small sub-networks by keeping the most important weights of the large sub-
networks (Figure 5) and provide better supervision via knowledge distillation (Figure 2), which
is better than training small sub-networks from scratch. Third, the progressive shrinking gives an
ordering to the shared weights and prevents the smaller sub-networks from hurting the performances
of larger sub-networks. We describe the details of the training ﬂow as follows:
• Elastic Resolution (Figure 2). Theoretically, we can feed images with any resolution into a
trained CNN model, since the image size does not affect the weights of the CNN model. However,
practically, it will cause signiﬁcant accuracy drop if feeding images with resolutions that are never
seen during training. Therefore, to support the elastic resolution, we sample different image size
for each batch of training data when training our models. It is implemented by modifying the data
loader.
• Elastic Kernel Size (Figure 3). If trained properly, the center of a 7x7 convolution kernel can
also serve as a 5x5 convolution kernel, the center of which can also be a 3x3 convolution kernel.
Therefore, the kernel size becomes elastic. The challenge is that the centered sub-kernels (e.g.,
3x3 and 5x5) are shared and need to play multiple roles (independent kernel and part of a large
kernel). The weights of centered sub-kernels may need to have different distribution or magnitude
as different roles. Forcing them to be the same may degrade the performance of some sub-
networks. Therefore, we introduce kernel transformation matrices when sharing the kernel weights.
Concretely, we use separate kernel transformation matrices among different blocks. Within each
block, the kernel transformation matrices are shared among different channels. As such, we only
need 25 × 25 + 9 × 9 = 706 extra parameters to store the kernel transformation matrices in each
block, which is negligible.
• Elastic Depth (Figure 4). The elastic depth is supported in the stage-level, where a stage corre-
sponds to a sequence of building blocks that have the same output resolution. Each building block
consists of one depth-wise convolution and two point-wise convolutions. To derive a sub-network
that has D blocks in a stage that originally has N blocks, we keep the ﬁrst D blocks and skip the
last N −D blocks, rather than keeping any D blocks as done in current NAS methods [3,27]. As
such, one depth setting only corresponds to one combination of blocks. In the end, the weights of
the ﬁrst D blocks are shared between large and small models.
• Elastic Width (Figure 5). Width means the number of channels. We give each layer the ﬂexibility
to choose different channel expansion ratio. Following the progressive shrinking scheme, we ﬁrst
5

train a full-width neural network. Then we introduce a channel sorting operation to support partial
widths. It reorganizes the channels according to their importance, which is calculated based on
the L1 norm of a channel’s weight. Larger L1 norm means more important. For example, when
shrinking from a 4-channel-layer to a 3-channel-layer, we select the largest 3 channels; whose
weights are shared with the 4-channel-layer (Figure 5 left and middle). Thereby, the smaller
sub-networks are initialized with the most important channels on the once-for-all network which is
already well trained. Notably, this channel sorting operation does not hurt the performances of
larger sub-networks.
• Knowledge Distillation (Figure 2). We use both the hard labels given by the training data and the
soft labels [10] given by the trained full network when training the once-for-all network. These
two loss terms are combined with a scaling factor λ:
Loss = Losshard + λLosssoft.
(2)
3.3
Specialized Model Deployment with Once-for-all Network
Having trained a once-for-all network, the next stage is to derive the specialized sub-network for a
given deployment scenario. The goal is to search for a neural network that satisﬁes the efﬁciency
(e.g., latency, energy) constraints on the target hardware platform while optimizing the accuracy. The
“Once for All” methodology decouples model training from architecture search, thereby we do not
have any training cost in this stage.
Generally, OFA can be combined with any search algorithm, such as reinforcement learning [2,32],
evolutionary algorithms [22], gradient descent [16, 27], etc. However, these algorithms require
search cost in each deployment scenario, leading to linear growth of the total cost (Table 2). In this
work, we present a simple solution to eliminate the linear term. We randomly sample a subset of
sub-networks and build their accuracy table and latency table. As such, given a target hardware and
latency constraints, we can directly query the accuracy table and corresponding latency table to get
the best sub-networks within the table. The cost of querying tables is negligible, thereby avoiding the
linear growth of the total cost.
Speciﬁcally, we sample 16K sub-networks in our experiments and build the accuracy table on 10K
validation images (sampled from the original training set). Additionally, since we support the elastic
resolution, the same sub-network is measured under multiple input image sizes. Empirically, we ﬁnd
that the accuracy of a sub-network grows smoothly as the resolution increases. Therefore, to save the
cost, we measure the accuracy of sub-networks under a subset of resolutions with a stride 16 (e.g.,
160, 176, · · · ). For an unmeasured image size (e.g., 164), we predict its accuracy as follows:
Acci(164) = (Acci(176) −Acci(160)) × FLOPi(164) −FLOPi(160)
FLOPi(176) −FLOPi(160) + Acci(160),
(3)
where Acci(r) and FLOPi(r) denote the accuracy and FLOPs of archi under input image size r,
respectively. Since all sub-networks directly grab weights from the once-for-all network without
training, this process takes only 200 GPU hours to complete. More importantly, this cost is paid
once.
4
Experiments
In this section, we ﬁrst apply the progressive shrinking algorithm to train the once-for-all network on
ImageNet [5]. Then we demonstrate the effectiveness of our trained once-for-all network on various
hardware platforms (Samsung Note8, Google Pixel1, Pixel2, NVIDIA 1080Ti, 2080Ti, V100 GPUs,
and Intel Xeon CPU) with different latency constraints.
4.1
Training the Once-for-all Network on ImageNet
Training Details.
For a fair comparison, we use the same architecture space as ProxylessNAS [3],
without SE [12] and Swish activation function [21] that are orthogonal methods to boost the accuracy
[25]. We train a once-for-all network that supports elastic depth (the number of blocks in each stage
can be 2, 3 or 4), elastic width (expansion ratio in each block can be 4, 5 or 6) and elastic kernel size
(the kernel size of each depthwise-separable convolution layer can be 3, 5 or 7). Therefore, with 5
stages, we have roughly ((3 × 3)2 + (3 × 3)3 + (3 × 3)4)5 ≈2 × 1019 sub-networks. Additionally,
the input image size is also elastic, ranging from 128 to 224 with a stride 4.
6

D = 2
D = 4
Sub-networks
W = 4
W = 6
W = 4
W = 6
K = 3
K = 7
K = 3
K = 7
K = 3
K = 7
K = 3
K = 7
Parameters
2.8M
2.9M
3.3M
3.5M
3.7M
4.0M
4.7M
5.1M
FLOPs
191M
233M
266M
328M
329M
419M
473M
607M
Independent
68.7
70.5
70.9
72.6
72.8
74.3
74.6
75.4
W/o progressive shrink
-1.4
-0.7
-1.7
-1.3
-1.4
-1.6
-2.0
-1.9
Progressive shrink
0.0
+0.7
+0.1
+0.7
+0.5
+0.5
+0.2
+0.5
Table 1: ImageNet top1 accuracy (%) performances of sub-networks under resolution 224 × 224.
“(D = d, W = w, K = k)” denotes a sub-network with d blocks in each stage, and each block has
an width expansion ratio w and kernel size k. “Independent” indicates that the sub-networks are
trained independently. We report the accuracy differences between the sub-networks derived from
once-for-all network and independently trained sub-networks with the same architecture. Progressive
shrinking consistently achieves the same level (or better) ImageNet accuracy as independent training.
We use the standard stochastic gradient descent (SGD) optimizer with Nesterov momentum 0.9 and
weight decay 4e−5 to train models on ImageNet. The initial learning rate is 0.4, and we use the cosine
schedule [19] for learning rate decay. The independent models are trained for 150 epochs with batch
size 2048 on 32 GPUs. For training the once-for-all network, we use the same training setting with
larger training cost (roughly 8×), taking around 1,200 GPU hours on V100 GPUs. This is one-time
training cost which can be amortized by many deployment scenarios. Conventional models, even
trained longer, can not achieve the same accuracy (2nd row of Table 2).
Results.
The top1 accuracy of both independently trained models and the once-for-all networks
under the same architectural conﬁgurations are reported in Table 1. Due to space limits, we take 8
sub-networks for comparison, and each of them is denoted as “(D = d, W = w, K = k)”. It represents
a sub-network that has d blocks for all stages while the expansion ratio and kernel size are set to w
and k for all blocks. We also report the FLOPs and #parameters of these sub-networks for reference.
Compared to independently trained models, the once-for-all network trained by the progressive
shrinking (PS) algorithm can maintain the same level (or better) accuracy under all architectural
conﬁgurations. We hypothesize that knowledge is transferred from larger sub-networks to smaller
sub-networks through progressive shrinking and distillation, which enable them to learn better jointly.
In contrast, without PS (i.e., training the once-for-all network from scratch following Eq. 1), the
once-for-all network cannot maintain the accuracy of the sub-networks. The maximum top1 accuracy
drop reaches 2.0% on ImageNet. It shows the beneﬁts and effectiveness of the progressive shrinking
algorithm.
4.2
Specialized Sub-networks for Different Hardware Platforms and Constraints
We apply our trained once-for-all network to get specialized sub-networks for different hardware
platforms, aiming to optimize the trade-off between accuracy and latency. We use 7 different hardware
platforms . For the GPU platforms, the latency is measured with batch size 32 and 64 on NVIDIA
1080Ti, 2080Ti and V100 with Pytorch 1.0+cuDNN. The CPU latency is measured with batch size 1
on Intel Xeon E5-2690 v4. Additionally, we use the MKL-DNN2 library to speedup CPU inference.
To measure the mobile latency, we use Samsung Note8, Google Pixel1 and Pixel2 with TF-Lite with
batch size 1. On all hardware platforms, we fuse the batch normalization layers into the convolution
layers. No quantization is applied. In total, we have 40 deployment scenarios (Figure 6, Figure 1
right) in the experiments: eight hardware platforms, four latency requirements each.
Comparison with NAS on Mobile.
Table 2 reports the comparison between OFA and state-of-the-
art hardware-aware NAS methods on the mobile platform (Samsung Note8). OFA is much more
efﬁcient than NAS when handling multiple deployment scenarios, since the cost of OFA is constant
while others are linear to the number of deployment scenarios (N). With N = 40, the training time
of OFA is 14× faster than ProxylessNAS, 16× faster than FBNet, and 1,142× faster than MnasNet.
Without retraining, OFA achieves 75.0% top1 accuracy on ImageNet, which is 1.0% higher than
MnasNet, 0.4% higher than ProxylessNAS, and 0.1% higher than FBNet while maintaining similar
2https://github.com/intel/mkl-dnn
7

Model
ImageNet
FLOPs
Mobile
Search cost
Training cost
Total GPU hours
Top1 (%)
latency
(GPU hours)
(GPU hours)
N = 1/40/ · · ·
MobileNetV2 [23]
72.0
300M
106ms
0
150N
0.15K / 6K
MobileNetV2 #1200 [23]
73.5
300M
106ms
0
1200N
1.2K / 48K
NASNet-A [33]
74.0
564M
234ms
48, 000N
-
> 48K / 1,920K
DARTS [16]
73.1
595M
-
96N
250N
0.346K / 13.84K
MnasNet∗[24]
74.0
317M
108ms
40, 000N
-
> 40K / 1,600K
FBNet-C [27]
74.9
375M
129ms
216N
360N
0.576K / 23.04K
ProxylessNAS-Mobile [3]
74.6
320M
110ms
200N
300N
0.5K / 20K
SinglePathNAS [6]
74.7
328M
-
288 + 24N
384N
0.696K / 16.608K
Once for All w/o PS
72.9
321M
109ms
200
1200
1.4K / 1.4K
Once for All w/ PS
75.0
327M
112ms
200
1200
1.4K / 1.4K
Once for All w/ PS #25
75.3
327M
112ms
200
1200 + 25N
1.425K / 2.4K
Table 2: Comparison with state-of-the-art hardware-aware NAS methods on Samsung Note8. OFA
decouples model training from architecture search. The search cost and training cost both stay
constant as the number of deployment scenarios grows (N = 40 in our experiments). “#25” denotes
the specialized sub-networks are ﬁne-tuned for 25 epochs after grabbing weights from the once-for-all
network. ∗We cite the results of MnasNet without SE for a fair comparison of the search methodology.
(or lower) mobile latency. By ﬁne-tuning the specialized sub-network for 25 epochs, we can further
improve the accuracy to 75.3%. Besides, we also observe that OFA with progressive shrinking (PS)
can achieve 2.4% better accuracy than without PS, which shows the effectiveness of PS.
Model
Latency
Top1 (%)
MobileNetV2 0.35
28ms
60.3
MnasNet 0.35
27ms
62.4 (+2.1)
Once for All (ours)
31ms
66.3 (+6.0)
Once for All #25
31ms
69.0 (+8.7)
MobileNetV2 0.5
40ms
65.4
MnasNet 0.5
41ms
67.8 (+2.4)
ProxylessNAS 0.5
41ms
68.2 (+2.8)
Once for All (ours)
43ms
69.6 (+4.2)
Once for All #25
43ms
71.1 (+5.7)
MobileNetV2 0.75
77ms
69.8
MnasNet 0.75
75ms
71.5 (+1.7)
Once for All (ours)
79ms
73.7 (+3.9)
Once for All #25
79ms
74.3 (+4.5)
Table 3: ImageNet accuracy results on Sam-
sung Note8 under various latency constraints.
Results under Different Efﬁciency Constraints.
Table 3 summarizes the results on the mobile plat-
form under different latency constraints. Beneﬁting
from the OFA framework, we can design specialized
neural networks for all scenarios without additional
cost while previous methods typically rescale an ex-
isting model using a width multiplier to ﬁt different
latency constraints [3,23,24]. Therefore, as shown in
Table 3, we can achieve much higher improvements
over the baselines in such cases. Speciﬁcally, with
similar latency as MobileNetV2 0.35, we improve
the ImageNet top1 accuracy from the MobileNetV2
baseline 60.3% to 66.3% (+6.0%) without retraining,
and to 69.0% (+8.7%) after ﬁne-tuning for 25 epochs.
Results on More Hardware Platforms.
Figure 6
shows the detailed results on the other six hardware
platforms (GPUs have two rows for two different
batch sizes). OFA consistently improve the trade-off
between accuracy and latency by a signiﬁcant margin,
especially on CPU and GPUs, since previous work on compact model design emphasized the edge,
overlooking the cloud. OFA excels at both with low NRE cost. Speciﬁcally, with similar latency as
MobileNetV2 0.35, “OFA #25” improves the ImageNet top1 accuracy from MobileNetV2’s 60.3% to
70.9% (+10.6%) on Intel CPU and to 70.4+% (+10.1%) on NVIDIA GPUs. It reveals the insight that
using the same model for different deployment scenarios with only the width multiplier modiﬁed has
limited impact on efﬁciency improvement: the accuracy drops quickly as the latency constraint gets
tighter. We provide an efﬁcient way to specialize our models at the architectural level, decoupling
model training and architecture search, which offers a large design space and achieves better accuracy.
5
Conclusion
We proposed Once for All (OFA), a new methodology that decouples model training from architecture
search for efﬁcient deep learning deployment under a large number of deployment scenarios. Unlike
previous approaches that design and train a neural network for each deployment scenario, we designed
a once-for-all network that supports different architectural conﬁgurations, including elastic depth,
width, kernel size, and resolution. It greatly reduces the training cost (GPU hours) compared to
conventional methods. To prevent sub-networks of different sizes from interference, we proposed a
8

59
63
66
70
73
77
25
39
53
67
81
95
109 123
Pixel2 Latency (ms)
59
63
66
70
73
77
9
11
13
15
17
19
Intel Xeon CPU Latency (ms)
Top-1 ImageNet Acc (%)
59
63
66
70
73
77
15
25
35
45
55
65
75
85
Once for All #25
Once for All
MnasNet
MobileNetV2
Slimmable Nets
Pixel1 Latency (ms)
60.3
65.4
69.8
72.0
67.3
70.8
74.3
75.1
60.3
65.4
69.8
72.0
69.0
70.9
74.2
75.3
60.3
65.4
69.8
72.0
70.9
74.3
75.1
59
63
66
70
73
77
3
4
5
6
7
8
59
63
66
70
73
77
4.0
4.5
5.0
5.5
6.0
6.5
Top-1 ImageNet Acc (%)
59
63
66
70
73
77
6
8
10
12
14
16
1080Ti Latency (ms)
Batch Size = 32
2080Ti Latency (ms)
Batch Size = 32
V100 Latency (ms)
Batch Size = 32
60.3
65.4
69.8
72.0
60.3
65.4
69.8
72.0
60.3
65.4
69.8
72.0
72.1
73.0
74.5
75.2
71.4
72.6
74.3
75.3
74.2
74.5
75.2
59
63
66
70
73
77
5
7
9
11
13
15
59
63
66
70
73
77
4
6
8
10
12
Top-1 ImageNet Acc (%)
59
63
66
70
73
77
10
14
18
22
26
30
1080Ti Latency (ms)
Batch Size = 64
2080Ti Latency (ms)
Batch Size = 64
V100 Latency (ms)
Batch Size = 64
60.3
65.4
69.8
72.0
60.3
65.4
69.8
72.0
60.3
65.4
69.8
72.0
71.2
73.0
74.7
75.2
70.4
72.6
74.3
75.0
71.1
72.5
74.3
75.3
Figure 6: Specialized deployment results on mobile devices, Intel CPU and GPUs. On mobile,
we can achieve up to 8.7% higher ImageNet top1 accuracy (60.3% -> 69.0%, upper middle) than
MobileNetV2. On NVIDIA GPUs and Intel CPU, we can achieve up to 10+% higher ImageNet top1
accuracy than MobileNetV2. Specializing for a new hardware platform does not add the training cost.
progressive shrinking algorithm that enable each sub-network to achieve the same level of accuracy
compared to training them independently. Experiments on a diverse range of hardware platforms and
efﬁciency constraints demonstrated the effectiveness of our approach.
Acknowledgments
We thank MIT Quest for Intelligence, MIT-IBM Watson AI Lab, MIT-SenseTime Alliance, Samsung,
Intel, ARM, Xilinx, SONY, AWS Machine Learning Research Award, Google AR/VR Research
Award for supporting this research. We thank Samsung and Google for donating mobile phones.
References
[1] H. Cai, T. Chen, W. Zhang, Y. Yu, and J. Wang. Efﬁcient architecture search by network
transformation. In AAAI, 2018. 3
[2] H. Cai, J. Yang, W. Zhang, S. Han, and Y. Yu. Path-level network transformation for efﬁcient
architecture search. In ICML, 2018. 6
[3] H. Cai, L. Zhu, and S. Han. ProxylessNAS: Direct neural architecture search on target task and
hardware. In ICLR, 2019. 3, 5, 6, 8
9

[4] M. Courbariaux, Y. Bengio, and J.-P. David. Binaryconnect: Training deep neural networks
with binary weights during propagations. In NeurIPS, 2015. 3
[5] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei. Imagenet: A large-scale hierarchical
image database. In CVPR, 2009. 6
[6] Z. Guo, X. Zhang, H. Mu, W. Heng, Z. Liu, Y. Wei, and J. Sun. Single path one-shot neural
architecture search with uniform sampling. arXiv preprint arXiv:1904.00420, 2019. 8
[7] S. Han, H. Mao, and W. J. Dally. Deep compression: Compressing deep neural networks with
pruning, trained quantization and huffman coding. In ICLR, 2016. 3
[8] S. Han, J. Pool, J. Tran, and W. Dally. Learning both weights and connections for efﬁcient
neural network. In NeurIPS, 2015. 3
[9] Y. He, J. Lin, Z. Liu, H. Wang, L.-J. Li, and S. Han. Amc: Automl for model compression and
acceleration on mobile devices. In ECCV, 2018. 1, 3, 4
[10] G. Hinton, O. Vinyals, and J. Dean. Distilling the knowledge in a neural network. arXiv preprint
arXiv:1503.02531, 2015. 6
[11] A. G. Howard, M. Zhu, B. Chen, D. Kalenichenko, W. Wang, T. Weyand, M. Andreetto, and
H. Adam. Mobilenets: Efﬁcient convolutional neural networks for mobile vision applications.
arXiv preprint arXiv:1704.04861, 2017. 1, 3
[12] J. Hu, L. Shen, and G. Sun. Squeeze-and-excitation networks. In CVPR, 2018. 6
[13] G. Huang, D. Chen, T. Li, F. Wu, L. van der Maaten, and K. Q. Weinberger. Multi-scale dense
networks for resource efﬁcient image classiﬁcation. In ICLR, 2018. 3
[14] F. N. Iandola, S. Han, M. W. Moskewicz, K. Ashraf, W. J. Dally, and K. Keutzer. Squeezenet:
Alexnet-level accuracy with 50x fewer parameters and< 0.5 mb model size. arXiv preprint
arXiv:1602.07360, 2016. 3
[15] J. Lin, Y. Rao, J. Lu, and J. Zhou. Runtime neural pruning. In NeurIPS, 2017. 3
[16] H. Liu, K. Simonyan, and Y. Yang. Darts: Differentiable architecture search. In ICLR, 2019. 3,
6, 8
[17] L. Liu and J. Deng. Dynamic deep neural networks: Optimizing accuracy-efﬁciency trade-offs
by selective execution. In AAAI, 2018. 3
[18] Z. Liu, J. Li, Z. Shen, G. Huang, S. Yan, and C. Zhang. Learning efﬁcient convolutional
networks through network slimming. In ICCV, 2017. 3
[19] I. Loshchilov and F. Hutter. Sgdr: Stochastic gradient descent with warm restarts. arXiv preprint
arXiv:1608.03983, 2016. 7
[20] N. Ma, X. Zhang, H.-T. Zheng, and J. Sun. Shufﬂenet v2: Practical guidelines for efﬁcient cnn
architecture design. In ECCV, 2018. 3
[21] P. Ramachandran, B. Zoph, and Q. V. Le. Searching for activation functions. arXiv preprint
arXiv:1710.05941, 2017. 6
[22] E. Real, A. Aggarwal, Y. Huang, and Q. V. Le. Regularized evolution for image classiﬁer
architecture search. arXiv preprint arXiv:1802.01548, 2018. 3, 6
[23] M. Sandler, A. Howard, M. Zhu, A. Zhmoginov, and L.-C. Chen. Mobilenetv2: Inverted
residuals and linear bottlenecks. In CVPR, 2018. 1, 3, 8
[24] M. Tan, B. Chen, R. Pang, V. Vasudevan, and Q. V. Le. Mnasnet: Platform-aware neural
architecture search for mobile. arXiv preprint arXiv:1807.11626v1, 2018. 3, 8
[25] M. Tan and Q. Le. Efﬁcientnet: Rethinking model scaling for convolutional neural networks. In
ICML, 2019. 6
[26] X. Wang, F. Yu, Z.-Y. Dou, T. Darrell, and J. E. Gonzalez. Skipnet: Learning dynamic routing
in convolutional networks. In ECCV, 2018. 3
[27] B. Wu, X. Dai, P. Zhang, Y. Wang, F. Sun, Y. Wu, Y. Tian, P. Vajda, Y. Jia, and K. Keutzer.
Fbnet: Hardware-aware efﬁcient convnet design via differentiable neural architecture search. In
CVPR, 2019. 3, 5, 6, 8
[28] Z. Wu, T. Nagarajan, A. Kumar, S. Rennie, L. S. Davis, K. Grauman, and R. Feris. Blockdrop:
Dynamic inference paths in residual networks. In CVPR, 2018. 3, 4
10

[29] J. Yu, L. Yang, N. Xu, J. Yang, and T. Huang. Slimmable neural networks. In ICLR, 2019. 3, 4
[30] X. Zhang, X. Zhou, M. Lin, and J. Sun. Shufﬂenet: An extremely efﬁcient convolutional neural
network for mobile devices. In CVPR, 2018. 1, 3
[31] C. Zhu, S. Han, H. Mao, and W. J. Dally. Trained ternary quantization. In ICLR, 2017. 3
[32] B. Zoph and Q. V. Le. Neural architecture search with reinforcement learning. In ICLR, 2017.
3, 6
[33] B. Zoph, V. Vasudevan, J. Shlens, and Q. V. Le. Learning transferable architectures for scalable
image recognition. In CVPR, 2018. 3, 8
11
