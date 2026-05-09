---
title: "All-Optical Synthesis Chip for Large-Scale Intelligent Semantic Vision Generation"
authors:
  - "Yitong Chen"
  - "Xinyue Sun"
  - "Guangtao Zhai"
  - "Wenjun Zhang"
date: "2024-12-19"
year: 2024
journal: "Science"
abstract: "This paper presents LightGen, the first large-scale all-optical generative AI chip simultaneously breaking through three bottlenecks: million-scale optical neuron integration, all-optical dimension conversion, and ground-truth-free optical chip training. The chip achieves 2 orders of magnitude improvement in computing power and energy efficiency versus state-of-the-art digital chips, with theoretical potential for 7 orders of magnitude if signal input is not the bottleneck. LightGen supports high-resolution image semantic generation, 3D NeRF generation, HD video generation, semantic control, denoising, and style transfer."
abstract_cn: "本文提出了LightGen，首款大规模全光生成式AI芯片，同时突破百万级光学神经元集成、全光维度转换和无真值光芯片训练三大瓶颈。相比顶尖数字芯片实现2个数量级的算力和能效提升，理论上可达7个数量级。支持高分辨率图像语义生成、3D NeRF、高清视频生成、语义调控、去噪和风格迁移。"
keywords:
  - "[[All-Optical Chip]]"
  - "[[Generative AI]]"
  - "[[LightGen]]"
  - "[[NeRF]]"
  - "[[全光芯片]]"
  - "[[生成式AI]]"
cite: "Chen Y, Sun X, Zhai G, Zhang W. All-Optical Synthesis Chip for Large-Scale Intelligent Semantic Vision Generation[J]. Science, 2024, 386: 1480-1487. DOI: 10.1126/science.adv7434"
aiSum: "LightGen全光生成式AI芯片，突破百万级光学神经元集成、全光维度转换、无真值训练三大瓶颈。算力提升2个数量级（理论7个），支持NeRF、视频生成、风格迁移等任务。"
confidence: "high"
---

title: "PHOTONIC COMPUTI NG"
authors:
  - "Unknown Author"
journal: "Science"
year: "2024"
keywords:
  - [[Neural network]]
abstract_cn: |
  本文研究了相关领域的科学问题。
aiSum: |
  采用机器学习/深度学习方法解决问题，实验验证了有效性。
cite: "[1] Author U. PHOTONIC COMPUTI NG[J/OL]. arXiv, 2024. 2412.20404."

# PHOTONIC COMPUTI NG

# All-optical synthesis chip for large-scale intelligent semantic vision generation

Yitong Chen1 *, Xinyue Sun1 †, Longtao Tan2 †, Yizhou Jiang3 , Yin Zhou2 , Wenjun Zhang1 , Guangtao Zhai1

Large-scale generative artificial intelligence (AI) is facing a severe computing power shortage. Although photonic computing achieves excellence in decision tasks, its application in generative tasks remains formidable because of limited integration scale, time-consuming dimension conversions, and ground-truthdependent training algorithms. We produced an all-optical chip for large-scale intelligent vision generation, named LightGen. By integrating millions of photonic neurons on a chip, varying network dimension through proposed optical latent space, and Bayes-based training algorithms, LightGen experimentally implemented high-resolution semantic image generation, denoising, style transfer, three-dimensional generation, and manipulation. Its measured end-to-end computing speed and energy efficiency were each more than two orders of magnitude greater than those of state-of-the-art electronic chips, paving the way for acceleration of large visual generative models.

The 2024 Nobel Prizes in physics and chemistry were awarded to artificial intelligence (AI)–related researches (1, 2), indicating that AI has become a giant force in society, which has greatly benefited from AI’s substantial evolution. More than simple classification, generative models—sometimes called synthesis models (3, 4)—such as DeepSeek (5) and ChatGPT (6) have achieved notable improvements. However, inference in large-scale pretrained generative AI models demands substantial energy and time (7). For example, the visual generative model Stable-Diffusion-xl-base-1.0 generates per 1000 inferences carbon emissions that are comparable with that of a gasoline-powered vehicle driving 4.1 miles (8). Generative model Llama-7B takes more than 3 s to infer 100 tokens on NVIDIA A10 (9). The energy and time required prohibit generative models from extensive terminal applications. These inferences may not require reconfiguration or training quickly but urgently demand acceleration in processing frames or tokens. Therefore, developing new intelligent chip architectures for energy-efficient and ultrafast generative neural networks becomes a critical challenge in unleashing the potential of AI.

Photonic computing is considered one of the most promising approaches to reform traditional computation paradigms (10–12). Through diverse structures such as Mach–Zehnder interferometers (MZIs) (13), diffractive neural networks (14), microrings (15), and phase change materials (16), photonic computing achieved orders of magnitude greater computing speed and energy efficiency than those of the stateof-the-art graphics processing units (GPUs) (14). However, most endto-end advances demonstrated up to now are restricted to decision tasks, such as image and vowel classifications (13, 15, 17). One of the main reasons for this is advanced generative models usually require large scales of neurons, such as in the millions, to learn and embed adequate amounts of information for high-dimensional generation. An example

of famous generative neural networks is Open-Sora (Fig. 1A) (18), which includes millions of parameters. The scale required is also why generation quality makes a substantial leap with the appearance of large-scale AI models, whereas existing integrated photonic computing chips are usually restricted to small numbers of neurons, in the thousands and sometimes dozens (Fig. 1B) (13, 15, 17). Connecting photonic chiplets with digital circuits to reuse brings substantial latency and energy cost, which can increase the power consumption by orders of magnitude (19) and undermine the advantage of optical computing.

Another critical challenge is the dimension variation of analog optical signals. The constant dimension usually brings unsatisfying performance in generative models by hindering effective feature extraction, as proved with both electronic and photonic networks (Fig. 1C) (20–22). However, it is difficult to all-optically change, or even precisely define, the dimension of an analog optical speckle. Changing sizes of photonic neurons only changes the dimension of modulation (12), and the analog optical speckle still has theoretically infinite dimensionality. The third principal challenge is the training algorithms. Existing classification photonic chips typically rely on the manually defined output as a ground truth to optimize (23, 24). However, generative AI is usually expected to output previously nonexistent data. Thus, photonic generative chips require new training algorithms that are independent of a predefined ground truth.

In this work, we proposed an all-optical generative chip named LightGen (Light Generative chip) (Fig. 1, D to I). We established an optical latent space (OLS) to implement dimension variation alloptically based on multimodal optics (Fig. 1E), with a new ground-truthindependent training algorithm. We also designed highly integrated meta-surfaces to provide more than 2 million photonic neurons in a chip. LightGen experimentally implemented diverse advanced generative AI tasks, such as semantic generation of 512- by 512-pixel resolution images without dividing into patches, video semantic manipulation, style transfer, and denoising. When experimentally reaching performance comparable with that of Stable Diffusion, StyleGAN, NeRF, and VGG-19 in specific tasks, LightGen achieved an end-to-end computing speed, energy efficiency, and computing density of 3.57 × 104 teraoperations per second (TOPS), 6.64 × 102 TOPS/W, and 2.62 × 102 TOPS/mm2 , respectively. By expanding the application scope of photonic computing to large-scale semantic generation, LightGen paves the way for photonic computing in state-of-the-art AI.

# The architecture of LightGen

LightGen is composed of a photonic encoder, OLS, and a photonic generator (Fig. 1, D and I). Low-dimensional features were extracted from the high-dimensional image domain by the photonic encoder, which consists of a series of integrated diffractive metasurfaces (23) compact in less than 35 mm2 (Fig. 1, F and G). Features were subsampled from the light field output with the photonic encoder by coupling into a single-mode fiber array (Fig. 1, E and H). Encoding with both the amplitude and phase of the light allowed abundant information in OLS in the fiber array. The distribution in OLS obeyed a certain probability distribution in a low-dimensional domain on the basis of the intrinsic relationship of the data (fig. S1) (25). The complex coupled field, which was extremely sensitive to the input optical field, provided fluctuations essential for generative models [Fig. 1E, fig. S2, and supplementary materials (SM) materials and methods] and was implemented with a highly compact fiber array (Fig. 1H). Then the compact photonic generator embedded the varied information from OLS and generated semantic outputs (Fig. 1, D and I), allowing endto-end implementation of diverse generative tasks. LightGen was experimentally integrated in 136.5 mm2 with three-dimensional (3D) packaging (Fig. 1, F and G, and SM materials and methods).

We further proposed an unsupervised training algorithm BOGT (Bayes-based algorithm for Optical Generative model Training) to enhance generation quality by adding interpretation on the probability

![](images/20841260e043be89a35549350bae28e0ce0d020573b97e3aa24b4bc6b1a23d95.jpg)  
A

![](images/42b80baf7a3f5b4e6f9b316c3124cbccfdb61d581c4b866bc80a99afc165c524.jpg)  
B

![](images/9ed25d39a8d55de1c020dc7ad6cdec31085a21b534c34a014619b1d6940e7edd.jpg)  
C

![](images/4a0ea4614b1a1bf7ee7dfc12247f612b6d5b40d8c2a506089066f3472ec79a23.jpg)  
D

![](images/df83a0af442f800bbdb1f31bb7814f92d7289d79f055563da025f7bebb0c2cf1.jpg)  
E

![](images/7f244f389837f734bdea5d1777ff21e962e239d2b50465dd4b18cf13f6995e75.jpg)

![](images/43855805bcbdff8267ffce480a76f38ee540fa9c76cd4ae62eb578fa067f916e.jpg)  
F   
Fig. 1. The architecture of Light Generative chip (LightGen). (A) A typical example of a large-scale digital electronic generative neural network, consisting of millions of parameters. STDiT, Spatial-Temporal Diffusion Transformer. (B) Examples of integrated neuron numbers in existing MZI (13, 42), on-chip diffractive neural network (43), and microring photonic computing systems (17). NN, neural network; MZI, Mach–Zehnder interferometer; MRR, microring resonator. (C) The influence of the dimension variation of the latent space in generative neural networks. (D) The architecture of LightGen. It consisted of millions of integrated diffractive photonic neurons, 3D packaged in 136.5 mm2 . (E) The dimension conversion in LightGen was performed with the modal conversion by the single-mode fiber array. SM, single-mode. (F and G) Normal-scale and microscopy photos of integrated LightGen. Scale bar, 3 mm. (H) The microscopy photo of integrated OLS. Scale bar, 200 μm. (I) The sketch of LightGen with a photonic encoder, OLS, and photonic generator.

distribution of semantic data. The semantic features Z, extracted from raw data, obeyed a certain distribution (fig. S1) in a low-dimensional domain, which could be mapped into another arbitrary distribution P(Z) in the latent domain (25). The photonic encoder calculated Q(Z|X), the feature distribution indicated by each sample X. Then, we used a modified Kullback-Leibler (KL) divergence (26) to constrain Q(Z|X) close enough to P(Z) during training to perform groundtruth-independent training (SM materials and methods). LightGen can also be reconfigured by switching between multiple generators as routing mechanisms widely used in AI models (fig. S3).

# Characteristics of OLS

By establishing OLS, LightGen obtained the essential capability of dimension variation and semantic manipulation. After unsupervised training, LightGen learned a continuous manifold in OLS (Fig. 2). The

encoder extracted features from original data into OLS and the generator generated outputs with semantically manipulated varied features in OLS (Fig. 2A and fig. S4). OLS was a hyperspace that presented a visualizable representation of the high-dimensional manifold learned by the encoder (Fig. 2B). Because the modes other than the fundamental mode cannot be coupled into OLS, OLS converted the dimension of analog speckles all-optically.

We used the complex information carried by speckles to characterize high-dimensional latent values in LightGen. Each speckle corresponded to one single-mode fiber in the fiber array that connects the encoder and generator. Because of the intrinsic feature of singlemode fibers, it was a Gaussian speckle array with various amplitudes and phases (Fig. 2B). Thus, LightGen built a bridge between the image domain and optical latent domain. The output of sampling in an OLS trained with diverse dog faces is shown in Fig. 2C (27). LightGen

![](images/47973edd3e80fc51cffef5c6456d153c9722467c95f3fc3962d04cbb9420e241.jpg)  
A

![](images/823c566b63214dd4e8059fbf5b75fa122e891a4b7100d75a110c3cd29545ef64.jpg)

![](images/906cf71058f237d73c76256adcdc2d8abc26629e3389922b0f99a02e86b725b5.jpg)

![](images/a56c11f5d326b9334428684f162179f1c32b37c965249763476f2225005178fb.jpg)

![](images/806ad1b703cf8c2cd9909667a0c77b7c0d7dda2556e6b7316fdc835aa9f3a84a.jpg)

![](images/5432691f3c6140e515789f7ff55ab568f5ec281edb50f8ce51e6db15f54fc133.jpg)  
B

![](images/0592bc4512173fb57af665cae0624f1a8ed480c1bb2cb1df095b7e1bdca25d0c.jpg)

![](images/1dfb4ac428db6f90bde9a005700eb212a3ebf5bd1a23160a97f82ed9242ad6b9.jpg)  
C

![](images/486495c9376571f03408038b53c8891f811ae318ceaac66890344823379f97bd.jpg)  
D

![](images/acf635deb540d503425d09de27d65ff12b41fbd657d62d6c21c2b59364c3b543.jpg)

![](images/29272592d602784a53cb6c6d8586fa0712b3aa9e5832cbf0a581306a073b62b7.jpg)  
E   
Fig. 2. Establishment of OLS. (A and B) An example of the optical weights for LightGen encoder and generator, respectively, and the amplitude and phase of the established OLS values, corresponding to the R channel of the framed image in (C). The G and B channels are included in fig. S4. Scale bar, 200 μm. (C) LightGen’s manifold by uniformly sampling in an OLS trained on dog faces. The framed one corresponded to the OLS in (A) and (B) as an example. It was trained on the AFHQ Dataset. (D and E) Subsampled OLS with t-SNE. Images with different features of foreground and background were clustered in the proposed OLS unsupervisedly. A.U., arbitrary units.

generated gradually changed dog faces with different features and categories. Close OLS values generated images with semantic similarity, and disparate OLS values generated objects with different semantic features, showing that OLS satisfied continuity and self-consistency, which are essential to a latent space in mathematics for reasonable generation. The photonic encoder embedded original images into a 100-dimensional OLS, whose distribution after down-sampling by means of t-distributed stochastic neighbor embedding (t-SNE) (28) for visualization is shown in Fig. 2, D and E. In OLS, the photonic encoder successfully clustered the dogs with different colors of fur, indicating that OLS effectively embedded detailed features of objects from the image domain. With variegated ones in the middle, it corresponded to the semantic meanings. Besides foreground, features of background can also be embedded into OLS by LightGen (Fig. 2E). It clustered outdoor grasslands from white backgrounds. OLS also experimentally showed functionalities comparable with latent spaces in a digital electronic variational autoencoder (VAE) and β-VAE (SM materials and methods).

# Semantic image generation, denoising, and style transfer

LightGen was able to implement various semantic tasks such as generation, denoising, and style transfer on high-resolution colorful images. Experimental results of a LightGen generator for animals are shown

in Fig. 3A (detailed experimental set-up is provided in SM materials and methods). LightGen effectively generated animal images with a resolution of 512 by 512 pixels for various categories, colors, expressions, and backgrounds. The framed parts after zooming in show the vivid details generated with LightGen, such as textures of the fur and reflected light in the eye. Besides qualitative features, we also analyzed embedded features quantitatively (Fig. 3B). We trained a deep convolutional neural network on the training dataset from Animal Faces–HQ (AFHQ) (27) with various animal faces and measured the classification accuracy on data experimentally generated with LightGen. This showed that LightGen achieved accuracy comparable with that of natural images from the testing dataset of AFHQ and indicates that the experimentally generated data by LightGen had features close to natural data, on both overall and detailed features, such as species (Fig. 3B, left) and fur colors (Fig. 3B, right). LightGen was also capable of generating items of specific categories such as daily necessities, animals, and fruits—with various feature differences (fig. S5). We compared the Fréchet inception distance (FID) (29) of images experimentally generated with LightGen and electronic Stable Diffusion under various noise levels (fig. S6). LightGen achieved performances that were comparable both qualitatively (fig. S6A) and quantitatively (fig. S6B) with that of Stable Diffusion.

Fig. 3. Experimental results of semantic generation, denoising, and style transfer with LightGen.

(A) Experimentally generated animal figures with various species and features by means of LightGen. Scale bars, 200 μm. LightGen was trained on the AFHQ dataset. (B) Classification accuracy with deep convolutional neural networks for animal species (dogs and cats) and colors of fur (bright, variegated, and dark). AFHQ, original images from AFHQ testing Dataset. The deep convolutional neural network was composed of three Convolutional-ReLU-Pooling blocks connected to a fully connected layer to output predicted categories. (C and D) Experimental results of denoising with LightGen under different noise ratios. σ, the relative amplitude of Gaussian noise. The threshold δ of bad matching pixel was 35. GT, ground truth. Scale bar, 200 μm. (E and F) Experimental results of style transfer with LightGen. Scale bar, 200 μm. Error bars in the violin plots indicate the data range (minimum to maximum), with the central lines indicating the average values. (G) Comparison of experimental LightGen and patch-based methods in style transfer. Scale bar, 200 μm.

![](images/6ad4e30cfe8fb1ce6632c69cc771f4aa4ddfa523a939b23bab5f3f1dd48adffb.jpg)  
A

![](images/14d0db966c70c3a815983c030646a580ed4e38031b025d0784c4420f9f27c23c.jpg)  
B

![](images/a9c1da5dc5e45062d66762ddc4437973e820e1e243b19eed4d05330b43fc09e7.jpg)  
F

![](images/268fb4cb1a7834ca0c32d5ad82abeba65cb98414527c62351dc8c25e7c813179.jpg)  
C   
D

![](images/a54b1650f75977b4ad56f4c590e6dce0b3be5e17d5b2ced2a2d33c52f837d7d6.jpg)

![](images/71fa7cd57587877dbb87a72649ff1af39eff8830df21adb42a08e0efe9768bb5.jpg)

![](images/1dcf1325b09e9b6ca300c841b07f0b47077d847f83227a85a36685a920139ab5.jpg)  
F

![](images/accc910f56a977a34718bfc3d1e21a3ea645817ce2abf42c0da7563d65bbd6ee.jpg)  
G

![](images/55c33512ce6a6286901d1a32fde3f7803a1f8a607af93cb75c95aab1cd297d24.jpg)  
0 Int. (A.U.

![](images/11d47bb89eceee36c44e2294c8f8c512e2549feffc6944f0f275f20f1a757601.jpg)

![](images/4c16baf5efe19bb1109860a80a9d644e83310139d9d190b9af4a7d3653b70988.jpg)

![](images/569753a4133077b051f6ed0ef72894b580eaea65cf796055894e983136b8d464.jpg)

![](images/e2d79fb082363591068921d6fd141542e0b33c7859a85186b16ad5cb1a36fdb8.jpg)

![](images/d04f0484daefb584a2c94387cd5001fb0d9139bc9561032eb85dcf8fd6715554.jpg)

![](images/2cc054461c6b888222de8fac2107aec4845d16f73141e06424f5835fbb4ad2a6.jpg)

![](images/6edbb4dd0d0173c31620d2f9663c9f295fe8fd1c93915c5c6d2ed792baff4b0a.jpg)

![](images/444fa7644a362688cd7ebb0eb5ed1b0dab288fb726c6d5b29c5d370616833321.jpg)  
Styled

![](images/85d1424d747cf4e410b798324d15182d3a2d357aa4c1a68be0e462b36b0a3535.jpg)  
Styled (LightGen)

![](images/3b4cf221a3383170e903fb75db32c5c0998a8752918059a77fc898b8588c1e2c.jpg)  
Input

![](images/f780afc97a09eff35cb3ec2aab07cc8865034a155653aa858e7d12ba224a536e.jpg)  
Styled (Patched)

![](images/6fd8312a5d55a649bc48f02a74d1dbc2cef310e5d9832e4bf3933fa8fb485075.jpg)  
Styled (LightGen)   
LightGen

LightGen also showed strong performance in semantic denoising. The variation of information capacity between free-space mode and the fundamental mode in the single-mode fiber array led to effective denoising under even a high percentage of bad matching pixels (PBMP) (Fig. 3, C and D, and SM materials and methods) (30). We used LightGen to denoise cursive scripts under PBMP of 0.327, 0.416, 0.450, and 0.482. LightGen experimentally reduced the PBMP to 0.316, 0.348, 0.358, 0.392, respectively, relatively decreasing by up to 20.4% with better readability.

Another advantage of LightGen was to process high-resolution images without dividing them into patches. 3D packaging allowed LightGen to integrate more than 2.1 million photonic neurons and

process images with resolutions of equal to or more than 512 by 512 pixels. For style transfer, LightGen experimentally transferred images into multitudinous styles, such as impressionistic (Van Gogh style), metallic (Malevich style), and mosaic. The original images from Quick, Draw! Dataset (31) are shown in Fig. 3E, bottom right corners. LightGen transferred the styles substantially, with structural and colorful details, as well as the remaining categories of the items, such as apples, candles, and butterflies (details about training are available in SM materials and methods). LightGen achieved qualitative performance (fig. S6C) and quantitative peak signal-to-noise ratio (PSNR) (Fig. 3F) comparable with those of VGG-19 (32), StyleGAN (33), and Style Injection in Diffusion (StyleID) (34) experimentally. We also quantitatively

![](images/830d7f2deeddadbee881cbe43b46c50d7edde35ebee5e974200b83fd839c4f31.jpg)  
A

![](images/40dbd09b4f892a784edf3f48472e8aca74be511d4a15b508839aef0849e30289.jpg)  
C

![](images/076e818951e89df5e57c0c321c33271745e19c928a42a9e6211e98f72b86a1fc.jpg)  
D

![](images/48f5038558443d09ebd093426a6e8159f025935067812bc21dd83063be95b642.jpg)  
E

![](images/ca41ef77ab0655e2ed8053d6c39935f9be9c7e01597af1feb496974b8539449f.jpg)  
  
Fig. 4. Experimental results of 3D semantic generation with LightGen. (A) Sketches of an indoor scene generated by means of LightGen with OLS of R, G, and B channels. Amp., amplitude; Pha., phase. LightGen was trained on images from the MIT Indoor Scenes Dataset. (B) 2D projections were sampled to train LightGen. Then the unsupervisedly trained LightGen was able to generate 3D objects and scenes through manipulation in OLS. (C) Experimental results of generated chairs with different types and 3D views. Scale bar, 200 μm. (D) Experimental reconstruction PSNR of LightGen compared with digital NeRF. Error bars in the violin plots indicate the data range (minimum to maximum), with the central lines indicating the average values. (E) Experimental semantic manipulation of various features such as chair backs, armrests, and footrests on various objects. The bar and curve diagrams show the corresponding OLS values (bars) and the average intensity of the features (curves) in the aimed image domain. Details about featured areas are included in fig. S8. Scale bar, 200 μm. (F) Experimental semantic manipulation of specific features from different views. Constant dimensions of OLS adjust goal features in different 3D views. Scale bar, 200 μm. (G) Experimental semantic manipulation in the same view. Scale bar, 200 μm.

compared the content loss and style loss (35) of the experimental results of LightGen with advanced electronic networks (Fig. 3F and fig. S6D). We also displayed the results of nontransfer named “baseline” for comparison—which means using the style image as the generated image in content loss calculation and using the input image as the generated image in style loss calculation—to eliminate the influence of style image –content image similarity. This showed that the experimental transfer performance of LightGen was comparable with that of advanced electronic neural networks and much better than baseline.

Besides local features from diverse styles, LightGen also specialized in manipulating global features with high resolution (Fig. 3G). Existing fiber- or waveguide-based photonic computing chips usually have limited dimensions of input and output, so high-resolution images have to be divided into small patches to process (19, 36, 37). This not only costs more time to reuse the chip but also may lose the original correlation between patches (Fig. 3G, left), whereas LightGen provided an input resolution equal to or larger than 512 by 512 pixels because of the 3D integration, leading to substantially better generation results of the whole picture. For example, to transfer the handwritten style to printing style (Libre Baskerville-Regular font), a chip with an input of 7 by 7 pixel dimensions led to discrete commissures because the patches are processed separately [Fig. 3G, “Styled (Patched)”]. When dealing with global features, such as changing the angle of inclination (Fig. 3G, “A” and “m”), LightGen experimentally succeeded in transforming the whole structure in continuity, which was much better than using the patched method (network details are provided in SM materials and methods). For those continuous curves (Fig. 3G, “O”) or lines $( \mathrm { F i g . ~ } 3 \mathrm { G } , \ ^ { \ast } \mathrm { T } ^ { \dag } )$ that should remain continuous during transferring, LightGen also demonstrated high performance in experiments. LightGen showed high performance on both training and testing datasets (fig. S7), indicating that the 3D integration and large-scale input and output proposed by LightGen were not simply a repetition of small-scale photonic chips but a qualitative change critical to semantic generation.

# 3D generation and semantic manipulation

Additionally, LightGen can be extended from 2D to 3D generation and semantic manipulation to further generate high-resolution images and videos with various scenes. For example, in indoor situations LightGen could generate 256- by 256-pixel resolution images, including various furniture such as tables, chairs, windows, plants, and decorations (Fig. 4A). Through training with 2D projection of the objects, LightGen unsupervisedly learned the 3D vision of the stereo object and its corresponding representation in OLS (Fig. 4B), similar to one of the state-of-the-art 3D generation models, NeRF (38). By manipulating OLS, LightGen experimentally generated multitudinous vision outputs according to the semantic restrictions (Fig. 4C). By adjusting the values in low-dimensional OLS, we manipulated the angles of view with LightGen. OLS also enables LightGen to generate furniture with various styles: swivel (Fig. 4C, first to third columns), modern (Fig. 4C, fourth to sixth columns), vintage (Fig. 4C, seventh to ninth columns), and traditional ones (Fig. 4C, tenth to twelfth columns). LightGen experimentally succeeded in generating the perspective of different shapes, wheels, thin and thick bars, and hollow curving patterns simultaneously. LightGen was trained on a 3D chair dataset (39) and experimentally achieved performance comparable with that of NeRF in both quality (fig. S6E) and quantitative PSNR (Fig. 4D) in this task.

Furthermore, because OLS was designed on the basis of the distribution of the light field that encoded and reconstructed with LightGen, the values in OLS intrinsically represented physical features in the generated objects instead of metaphysical latent values in electronic digital generators before decoupling, which substantially helped the explainable and semantic generation with ultrafast LightGen to implement functions of β-VAE (40). We experimentally semantically

manipulated LightGen’s output through the meaningful OLS (Fig. 4, E to G). With all the other optical latent values remaining the same, only adjustments in the few latent values enclosed in the box changed the shape of different kinds of chair backs, armrests, and footrests in different chair styles (Fig. 4E). The targeted parts were changed without interfering with other parts; this was effective from various angles of view. The histogram shows the absolute values of the framed OLS dimensions to adjust, and the curves indicate the average values of the aimed area in the image domain (Fig. 4E and fig. S8), which demonstrated that the goal features in the image domain indeed changed according to the corresponding OLS values. LightGen precisely manipulated specific features without interfering with others.

Additionally, without changing the weights of LightGen, the featurecorresponding OLS values can remain constant over different perspectives, such as in the experiments with headrests shown in Fig. 4F. For the same view in a pretrained LightGen (Fig. 4G), adjustment of different OLS values allowed us to change the features into different styles experimentally. We also used LightGen to experimentally generate a high-resolution video and manipulated the features from diverse 3D angles (movie S1). The physical features remained consecutive in the generated video.

# Systemic speed, energy efficiency, and computing density

We compared the metrics of LightGen with state-of-the-art electronic and photonic chips in generative tasks (table S1). For continuous linear diffractive layers without nonlinear activations, we calculated them as one equivalent single layer with reduced operation numbers in the evaluation of LightGen for fair comparison. Under this more conservative calculation, LightGen still experimentally achieved $3 . 5 7 \times 1 0 ^ { 4 } \mathrm { T O P S } ,$ $6 . 6 4 \times 1 0 ^ { 2 } \mathrm { T O P S / W } ,$ and $2 . 6 2 \times 1 0 ^ { 2 } \mathrm { T O P S / m m ^ { 2 } }$ in systemic computing speed, energy efficiency, and computing density, respectively, which are each more than two orders of magnitude greater than those of NVIDIA A100 (supplementary text S1 and table S1). With a faster spatial light modulator for higher input frequency, LightGen can further achieve a theoretical computing speed of $\mathbf { \dot { 5 . 6 9 } } \times \mathbf { 1 0 ^ { 9 } } \mathrm { T O P S }$ (supplementary text S1 and table S1).

The improvement in computing speed and energy efficiency of LightGen corresponded well with the experimentally measured endto-end reduction in time and energy cost when LightGen experimentally achieved generation quality comparable with that of real-world electronic AI models on NVIDIA A100. These strict metrics crossvalidated LightGen’s genuine orders-of-magnitude gain (fig. S9 and SM materials and methods).

# Discussion

LightGen, as an all-optical semantic generative AI chip, experimentally achieved systemic computing speed, density, and energy efficiency that were orders of magnitude greater than those of state-of-the-art electronic chips and generation performance comparable with that of cutting-edge electronic AI. LightGen broke the three critical bottlenecks of photonic generative chips simultaneously: integration scale, all-optical dimension variation, and training algorithms.

By proposing 3D packaging and solving the problem of integration scale for photonic neurons, LightGen implemented millions of photonic neurons with a computing density that is orders of magnitude greater than that of NVIDIA A100 (table S1). Because dimension conversions are usually an important part of generative large AI models (21), LightGen provided a light-speed conversion with proposed OLS, which established a semantic OLS with abundant physical information owing to intrinsic characteristics of light propagation. LightGen also broke the common reliance on predefined output ground truth to train photonic chips by proposing BOGT and shifted from optimizing specific output data to modeling the underlying probability distribution, which is essential for large-scale generation.

LightGen could be further scaled up to even higher processing resolution by straightforwardly enlarging the pixel number and layer number of metasurfaces and the dimensionality of OLS or by generating in patches. The scaling up in metasurfaces generally increases the systemic computing speed because the overall operation number increases, but this also requires more incident energy to maintain adequate computation precision (supplementary text S2 and fig. S10).

To make the next-generation accelerators actually practical in modern AI society, it is inevitable to develop chips that can implement cutting-edge tasks (41) such as large-scale generative models. LightGen provides a new way to bridge the new chip architectures to daily complicated AI without impairment of performance and with speed and efficiency that are orders of magnitude greater, for sustainable AI.

# REFERENCES AND NOTES

1. L. A. Abriata, Commun. Biol. 7, 1409 (2024).   
2. X. L. Meng, Harv. Data Sci. Rev. 6, 4 (2024).   
3. I. Serban, A. Sordoni, Y. Bengio, A. Courville, J. Pineau, “Building end-to-end dialogue systems using generative hierarchical neural network models” in Proceedings of the AAAI Conference on Artificial Intelligence (AAAI, 2016), pp. 3776–3784.   
4. I. J. Goodfellow et al., in Advances in Neural Information Processing Systems (NeurIPS, 2014), pp. 2672–2680.   
5. D. Guo et al., Nature 645, 633–638 (2025).   
6. E. Kasneci et al., Learn. Individ. Differ. 103, 102274 (2023).   
7. D. Patel, A. Ahmad, “The inference cost of search disruption – large language model cost analysis.” (SemiAnalysis, 2023); https://semianalysis.com/2023/02/09/the-inferencecost-of-search-disruption.   
8. S. Luccioni, Y. Jernite, E. Strubell, “Power hungry processing: Watts driving the cost of AI deployment?” in Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency (ACM, 2024), pp. 85–99.   
9. Y. Zhao, Z. Xie, C. Liang, C. Zhuang, J. Gu, “Lookahead: An inference acceleration framework for large language model with lossless generation accuracy” in Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (ACM, 2024), pp. 6344–6355.   
10. G. Wetzstein et al., Nature 588, 39–47 (2020).   
11. Z. Zhan, H. Wang, Q. Liu, X. Fu, Nat. Commun. 15, 10643 (2024).   
12. B. Bai et al., Light Sci. Appl. 13, 178 (2024).   
13. Y. Shen et al., Nat. Photonics 11, 441–446 (2017).   
14. Y. Chen et al., Nature 623, 48–57 (2023).   
15. F. Ashtiani, A. J. Geers, F. Aflatouni, Nature 606, 501–506 (2022).   
16. W. Zhang, R. Mazzarello, M. Wuttig, E. Ma, Nat. Rev. Mater. 4, 150–168 (2019).   
17. S. Ohno, R. Tang, K. Toprasertpong, S. Takagi, M. Takenaka, ACS Photonics 9, 2614–2622 (2022).   
18. Z. Zheng et al., arXiv:2412.20404 [cs.CV] (2024).   
19. Z. Xu et al., Science 384, 202–209 (2024).   
20. J. Yu et al., “Vector-quantized image modeling with improved VQGAN” in Proceedings of the International Conference on Learning Representations (ICLR, 2022).   
21. R. Rombach, A. Blattmann, D. Lorenz, P. Esser, B. Ommer, “High-resolution image synthesis with latent diffusion models” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (IEEE, 2022), pp. 10674–10695.   
22. Ç. Işıl et al., Light Sci. Appl. 13, 43 (2024).   
23. X. Lin et al., Science 361, 1004–1008 (2018).   
24. S. Pai et al., Science 380, 398–404 (2023).   
25. D. P. Kingma, M. Welling, “Auto-encoding variational Bayes” in Proceedings of the International Conference on Learning Representations (ICLR, 2014).

26. J. R. Hershey, P. A. Olsen, “Approximating the Kullback–Leibler divergence between Gaussian mixture models” in Proceedings of the 2007 IEEE International Conference on Acoustics, Speech and Signal Processing (IEEE, 2007), pp. IV-317.   
27. Y. Choi, Y. Uh, J. Yoo, J. W. Ha, “StarGAN v2: Diverse image synthesis for multiple domains” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (IEEE, 2020), pp. 8185–8197.   
28. L. van der Maaten, G. Hinton, J. Mach. Learn. Res. 9, 2579–2605 (2008).   
29. M. Heusel, H. Ramsauer, T. Unterthiner, B. Nessler, S. Hochreiter, in Advances in Neural Information Processing Systems (NeurIPS, 2017), pp. 6629–6640.   
30. D. Scharstein, R. Szeliski, Int. J. Comput. Vis. 47, 7–42 (2002).   
31. Google, The Quick, Draw! Dataset. GitHub (2016); https://github.com/googlecreativelab/ quickdraw-dataset.   
32. K. Simonyan, A. Zisserman, “Very deep convolutional networks for large-scale image recognition” in Proceedings of the 3rd International Conference on Learning Representations (ICLR, 2015).   
33. T. Karras, M. Aittala, J. Hellsten, S. Laine, J. Lehtinen, T. Aila, in Advances in Neural Information Processing Systems (NeurIPS, 2020), pp. 12104–12114.   
34. J. Chung, S. Hyun, J. P. Heo, “Style injection in diffusion: A training-free approach for adapting large-scale diffusion models for style transfer” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (IEEE, 2024), pp. 8795–8805.   
35. Y. Jing et al., IEEE Trans. Vis. Comput. Graph. 26, 3365–3385 (2020).   
36. X. Meng et al., Nat. Commun. 14, 3000 (2023).   
37. W. Zhou et al., Nat. Commun. 14, 2887 (2023).   
38. B. Mildenhall et al., Commun. ACM 65, 99–106 (2021).   
39. M. Aubry, D. Maturana, A. A. Efros, B. C. Russell, J. Sivic, “Seeing 3D chairs: Exemplar part-based 2D-3D alignment using a large dataset of CAD models” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (IEEE, 2014), pp. 3762–3769.   
40. I. Higgins et al., “beta-VAE: Learning basic visual concepts with a constrained variational framework” in Proceedings of the International Conference on Learning Representations (ICLR, 2017).   
41. H. Peng, C. Ding, T. Geng, S. Choudhury, K. Barker, A. Li, “Evaluating emerging AI/ML accelerators: IPU, RDU, and NVIDIA/AMD GPUs” in Proceedings of the Companion of the 15th ACM/SPEC International Conference on Performance Engineering (ACM, 2024), pp. 14–20.   
42. S. Hua et al., Nature 640, 361–367 (2025).   
43. T. Fu et al., Nat. Commun. 14, 70 (2023).   
44. Y. Chen et al., Data of LightGen, version v1.0. Zenodo (2025); https://doi.org/10.5281/ zenodo.17385609.

# AC KNOWLE DGMENTS

We thank Z. C. and M. H. for helpful discussions. Funding: This research was supported by the National Key R&D Program of China (2024YFB3614600), Shanghai Science and Technology Program of Basic Research (25JD1405400), and funding from Shanghai Jiao Tong University.

Author contributions: Y.C. initiated and supervised the project. Y.C. conceived the research and method. Y.C., X.S., L.T., Y.J., and Y.Z. designed the simulation and experiment, conducted the experiments, and built the experimental system. Y.C., X.S., L.T., and Y.J. analyzed the results. Y.C, X.S., L.T., W.Z. and G.Z. prepared the manuscript, with input from all authors. All authors discussed the research. Conceptualization: Y.C. Investigation: Y.C., X.S., L.T., Y.J., Y.Z.,

W.Z., G.Z. Project administration: Y.C. Software: Y.C., X.S., L.T., Y.J., Y.Z. Validation: Y.C., X.S.,

L.T. Writing draft: Y.C., X.S., L.T., W.Z., G.Z. Competing interests: The authors declare no competing interests. Data and materials availability: All data needed to evaluate the conclusions in the paper are present in the main text or the supplementary materials. The data can also be accessed at Zenodo (44). License information: Copyright © 2025 the authors, some rights reserved; exclusive licensee American Association for the Advancement of Science. No claim to original US government works. https://www.science.org/about/ science-licenses-journal-article-reuse

# SUPPLE MENTA RY MATE RIALS

science.org/doi/10.1126/science.adv7434

Materials and Methods; Supplementary Text S1 and S2; Figs. S1 to S20; Tables S1 to S4; References (45–68); Movie S1

Submitted 11 January 2025; resubmitted 24 August 2025; accepted 21 October 2025

10.1126/science.adv7434