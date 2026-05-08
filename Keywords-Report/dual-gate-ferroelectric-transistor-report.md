# 关键词索引报告：双栅铁电晶体管 (Dual-Gate Ferroelectric Transistor)

**生成日期**: 2026-05-06
**搜索关键词**: dual-gate, double-gate, 双栅, DG FeFET, DG FeTFT, DG MPBTFT
**匹配策略**: 模糊匹配（全文内容 + 关键词字段 + YAML frontmatter）
**分析论文总数**: 11 篇相关论文
**文献库路径**: `/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/Outputs/`

---

## 摘要统计

- **直接相关论文（双栅铁电晶体管为核心主题）**: 4 篇
- **间接相关论文（综述或涉及双栅结构讨论）**: 6 篇
- **相关但非铁电双栅论文**: 1 篇
- **期刊覆盖**: Nature Communications, Advanced Materials (x3), Science Advances, IEEE TED, IEEE JETCAS, 电子与信息学报, IEEE EDL, APL Materials, Advanced Science
- **年份范围**: 2021 - 2026
- **语言**: 英文为主，含 1 篇中文综述
- **核心研究主题**:
  - 双栅 FeFET 作为易失性物理储备池（reservoir computing）
  - 双栅结构实现存储与逻辑功能的独立控制（MFMIS / 双栅架构）
  - 双栅 FeFET 用于 TCAM 和存算一体电路
  - 双栅氧化物 TFT 与 FeFET 单片 3D 集成

---

## 第一部分：直接相关论文（核心文献）

### 1. Analog Reservoir Computing via Ferroelectric Mixed Phase Boundary Transistors

**链接**: [[Analog Reservoir Computing via Ferroelectric Mixed Phase Boundary Transistors]]
**作者**: Jangsaeng Kim, Eun Chan Park, Wonjun Shin, Ryun-Han Koo, Chang-Hyeon Han, He Young Kang, Tae Gyu Yang, Youngin Goh, Kilho Lee, Daewon Ha, Suraj S. Cheema, Jae Kyeong Jeong, Daewoong Kwon
**期刊**: Nature Communications, **年份**: 2024
**DOI**: 10.1038/s41467-024-53000-0

**研究摘要**:
- **问题**: 模拟储备池计算（ARC）系统各组件功能差异大，硬件实现面临挑战。
- **方法**: 利用 HfZrOx 铁电-混相边界（MPB）材料的多功能性，在 IGZO TFT 上实现全集成 ARC 系统。
- **双栅结构**: 采用 **双栅（double-gate, DG）MPB TFT** 作为易失性物理储备池和泄露积分点火（LIF）神经元。双栅结构包含底栅（BG, MFMIS 铁电结构）和顶栅（TG, 常规 MIS 结构），提供对 MPBTFT 电学特性的灵活调控。
- **关键发现**: DG 配置增强 16 个储备池状态的区分度和状态扩展能力，同时处理兴奋性和抑制性脉冲。非易失性 FeTFT（MFMIS 结构）模拟突触行为用于读出网络。实现复杂时间序列预测，NRMSE 低至 0.28。
- **质量评价**: **高** - Nature Communications 顶刊，方法新颖（材料-器件协同优化），实验验证完整（全集成单片 wafer），引用了双栅 FeFET 关键文献（Mulaosmanovic 2021, Jeong 2023）。

**双栅相关性**: **核心** - 双栅是本文物理储备池的核心器件结构。

---

### 2. Ferroelectric Transistors: from Materials Innovation to Intelligent Electronic Systems

**链接**: [[Ferroelectric Transistors from Materials Innovation to Intelligent Electronic Systems]]
**作者**: Enlong Li, Wunan Wang, Yu Liu, Ruixue Wang, Chunlai Luo, Hongmiao Zhou, Shuo Chen, Shuxin Chen, Zhaoren Xie, Kaichen Zhu, Wenwu Li, Junhao Chu
**期刊**: Advanced Materials, **年份**: 2025
**DOI**: 10.1002/adma.202515480

**研究摘要**:
- **问题**: 后摩尔时代传统冯诺依曼架构面临存储墙瓶颈，FeFET 作为革命性平台可集成非易失存储、存内计算和多模态传感。
- **方法**: 全面综述铁电材料（钙钛矿、HfO2、有机、2D）和三端 FeFET 器件物理与工程。
- **双栅结构**: **第 3.1.1 节专门讨论双栅 FeFET**（Dual-Gated FeFETs），将其与 MFS、MFIS、MFMIS、FinFET、GAA 并列为主要 FeFET 架构。双栅 FeFET 在半导体层顶部和底部集成了两个栅电极：一个铁电栅用于非易失存储操作，一个常规栅用于逻辑或读取功能。这种结构实现编程和感知过程的独立控制，扩大存储窗口，减轻读取干扰，并支持单个晶体管内的逻辑-存储-神经形态多功能计算。
- **关键发现**: 双栅架构为多功能存内计算提供紧凑解决方案，通过调制读取栅电压可进一步加速编程速度和提高耐久性。
- **质量评价**: **高** - Advanced Materials 顶刊综述，系统全面，引用广泛。

**双栅相关性**: **综述覆盖** - 将双栅列为 FeFET 六大核心架构之一，提供系统性论述。

---

### 3. 基于铁电晶体管的存储与存算一体电路

**链接**: [[基于铁电晶体管的存储与存算一体电路]]
**作者**: 刘勇, 李泰昕, 祝希, 杨华中, 李学清
**期刊**: 电子与信息学报, **年份**: 2023
**DOI**: 10.11999/JEIT230370

**研究摘要**:
- **问题**: IoT 和 AI 对片上存储与智能计算的能效、密度和性能提出更高要求，FeFET 提供新机遇。
- **方法**: 系统回顾 FeFET 的发展历程、结构、特性和建模，以及 FeFET 存储器和存算一体电路设计。
- **双栅结构引用**: 文中引用 "Compact and high-performance TCAM based on scaled double-gate FeFETs"（Liu et al., arXiv 2023, 参考文献 [77]），表明双栅 FeFET 在三态内容可寻址存储器（TCAM）中的应用。双栅结构有助于实现紧凑和高性能的 TCAM 设计。
- **关键发现**: FeFET 具有非易失、高能效、高开关比，适合低功耗高密度场景；双栅 FeFET 是 TCAM 的重要实现方案。
- **质量评价**: **中-高** - 中文核心期刊，综述内容覆盖全面，但双栅仅为文中引用内容而非独立研究。

**双栅相关性**: **引用提及** - 引用双栅 FeFET TCAM 工作作为 FeFET 应用案例。

---

### 4. A Compute-in-Memory Hardware Accelerator Design With Back-End-of-Line (BEOL) Transistor Based Reconfigurable Interconnect

**链接**: [[A Compute-in-Memory Hardware Accelerator Design With Back-End-of-Line (BEOL) Transistor Based Reconfigurable Interconnect]]
**作者**: Yandong Luo, Sourav Dutta, Ankit Kaul, Sung Kyu Lim, Muhannad Bakir, Suman Datta, Shimeng Yu
**期刊**: IEEE Journal on Emerging and Selected Topics in Circuits and Systems, **年份**: 2022
**DOI**: 10.1109/JETCAS.2022.3177577

**研究摘要**:
- **问题**: FeFET CIM 加速器面临两个挑战：缺乏先进节点的逻辑电压兼容 FeFET（面积缩放停滞）以及缺乏对不同 DNN 模型的灵活性。
- **方法**: 系统-技术协同设计（STCO）单片 3D 可重构 CIM 加速器，利用 BEOL 兼容氧化物沟道 MOSFET 和 FeFET。
- **双栅结构**: 提出使用 **双栅（double-gated）IWO 晶体管** 和单栅 IWO FeFET 的混合方案。双栅 IWO NMOS 用于设计面积高效的 M3D 写入电路。双栅结构提供更好的栅极控制和更高的驱动电流。
- **关键发现**: M3D IWO FeFET 设计能效比 7nm 2D SRAM 高 3.1 倍，可重构互连方案降低延迟 9%-32%。
- **质量评价**: **高** - IEEE JETCAS 期刊，系统级评估完整，技术-系统协同设计方法新颖。双栅 IWO 是重要支撑技术。

**双栅相关性**: **技术支撑** - 双栅 IWO 晶体管是 M3D 写入电路的核心元件，与 FeFET 协同工作。

---

## 第二部分：间接相关论文（综述或包含双栅讨论）

### 5. Unlocking Large Memory Windows and 16-Level Data per Cell Memory Operations in Hafnia-Based Ferroelectric Transistors

**链接**: [[Unlocking Large Memory Windows and 16-Level Data per Cell Memory Operations in Hafnia-Based Ferroelectric Transistors]]
**作者**: Ik-Jyae Kim, Jang-Sik Lee
**期刊**: Science Advances, **年份**: 2024
**DOI**: 10.1126/sciadv.adn1345

**研究摘要**:
- **问题**: HfO2 基铁电晶体管面临存储窗口限制和缺乏多级单元（MLC）高效操作技术的挑战。
- **方法**: 提出栅极堆叠工程方法（MFMFS 结构），通过控制电容比实现 10V 存储窗口而无需增加面积；提出位移电流控制（DCC）方法实现一次性编程到目标状态。
- **双栅相关性**: 文中讨论与 3D 双栅结构的兼容性。双栅架构可实现更大存储窗口和更低的读取干扰。
- **质量评价**: **高** - Science Advances 顶刊，16 级 MLC 演示，DCC 编程方法效率优于 ISPP。

**双栅相关性**: **间接提及** - 讨论与 3D 双栅结构的兼容性。

---

### 6. Reconfigurable Ferroelectric Devices for Neuromorphic Computing

**链接**: [[Reconfigurable Ferroelectric Devices for Neuromorphic Computing]]
**作者**: Tae Hyun Yoon, Jin Yong An, Yeon Ho Kim et al.
**期刊**: Advanced Materials, **年份**: 2026
**DOI**: N/A

**研究摘要**:
- **问题**: 在紧凑器件结构中实现传感、计算和存储多功能集成是重大挑战。
- **方法**: 基于 α-In2Se3 铁电 2D 半导体的可重构垂直光电二极管（MFsM 结构），通过面外极化部分开关实现内置电场的渐变可逆调制。
- **双栅相关性**: 综述部分讨论了可重构铁电器件设计，涵盖双栅 FeFET 等架构。
- **质量评价**: **高** - Advanced Materials，基于 2D 铁电半导体的创新器件设计。

**双栅相关性**: **综述内容** - 讨论可重构铁电器件大类，包含双栅结构。

---

### 7. Ferroelectric Transistors for Memory and Neuromorphic Device Applications

**链接**: [[Ferroelectric Transistors for Memory and Neuromorphic Device Applications]]
**作者**: Ik-Jyae Kim, Jang-Sik Lee
**期刊**: Advanced Materials, **年份**: 2022
**DOI**: 10.1002/adma.202200083

**研究摘要**:
- **问题**: 综述 HfO2 基 FeFET 在下一代存储和神经形态计算中的最新进展。
- **方法**: 回顾 FeFET 器件类型、工作原理、存储特性、阵列实现和 3D FeNAND。
- **双栅相关性**: 综述不同 FeFET 器件结构，涵盖双栅 FeFET 的讨论。
- **质量评价**: **高** - Advanced Materials 顶刊综述，引用广泛。

**双栅相关性**: **综述内容** - 涵盖双栅 FeFET 结构。

---

### 8. Reconfigurable Ferroelectric Hafnium Oxide FeFET Fabricated in 28 nm CMOS Technology for mmWave Applications

**链接**: [[Reconfigurable ferroelectric hafnium oxide FeFET fabricated in 28 nm CMOS technology for mmWave applications]]
**作者**: Sukhrob Abdulazhanov, Quang Huy Le, Dang Khoa Huynh et al.
**期刊**: IEEE Electron Device Letters, **年份**: 2023

**研究摘要**:
- **问题**: 需要高速高能效数据交换的 5G/6G 和 IoT 应用对可重构 RF 器件的需求。
- **方法**: 在 28 nm CMOS 技术中制造可重构多指 FeFET，通过切换阈值电压实现 RF 可重构功能。
- **双栅相关性**: 文中提到双栅器件在完全耗尽 SOI 中已展示过后制造适配能力，用于对比参考。
- **质量评价**: **中-高** - IEEE EDL，f_T/f_MAX 分别为 113/230 GHz（可重构 RF FeFET 中最高），双栅仅为对比提及。

**双栅相关性**: **对比提及** - 在讨论中引用双栅器件作为参考。

---

### 9. Ferroelectric Field Effect Transistors: Progress and Perspective

**链接**: [[Ferroelectric Field Effect Transistors: Progress and Perspective]]
**作者**: Jae Young Kim, Min-Ju Choi, Ho Won Jang
**期刊**: APL Materials, **年份**: 2021
**DOI**: 10.1063/5.0035515

**研究摘要**:
- **问题**: FeFET 作为下一代非易失性存储器和神经形态计算候选器件的前景和挑战。
- **方法**: 综述 HfO2 基 FeFET 的器件物理、材料工程和集成挑战。
- **双栅相关性**: 综述不同 FeFET 架构，包含双栅结构的相关讨论。
- **质量评价**: **中** - APL Materials，综述覆盖全面，但深度不如 Advanced Materials 系列综述。

**双栅相关性**: **综述内容** - 涵盖 FeFET 各类架构包括双栅。

---

### 10. Emerging 2D Ferroelectric Semiconductors: From Fundamentals to Advanced Device Applications

**链接**: [[Emerging 2D Ferroelectric Semiconductors: From Fundamentals to Advanced Device Applications]]
**作者**: Mengshuang Chi, Xiang Zhang, JiTao Liu, YiFan Wang, Aifang Yu, Di Guo, Junyi Zhai
**期刊**: Advanced Science, **年份**: 2025
**DOI**: 10.1002/advs.202514185

**研究摘要**:
- **问题**: 综述二维铁电半导体从基础到先进器件应用的发展。
- **方法**: 讨论二维铁电性起源、本征/外延材料体系、在 FeS-FET、FTJ、光电探测器等中的应用。
- **双栅相关性**: 文中提到 MFMIS 架构（2021 年）的采用改善了保持特性和耐久性。MFMIS 本质上是双栅结构的一种形式（铁电电容与晶体管栅极堆叠串联）。
- **质量评价**: **高** - Advanced Science，系统全面的综述，涵盖最新 2D 铁电半导体进展。

**双栅相关性**: **间接提及** - MFMIS 架构与双栅 FeFET 密切相关。

---

## 第三部分：相关但非铁电双栅论文

### 11. An Artificial Neural Network Implemented Using Parallel Dual-Gate Thin-Film Transistors

**链接**: [[An Artificial Neural Network Implemented Using Parallel Dual-Gate Thin-Film Transistors]]
**作者**: Yushen Hu, Tengteng Lei, Yuqi Wang, Fei Wang, Man Wong
**期刊**: IEEE Transactions on Electron Devices, **年份**: 2022
**DOI**: 10.1109/TED.2022.3201836

**研究摘要**:
- **问题**: 实现基于存内计算的人工神经网络硬件。
- **方法**: 采用单栅和并行双栅（DG）TFT 单片集成在电容器阵列中，电容器和 DG TFT 分别作为存储和计算元件。
- **双栅结构**: DG TFT 提供放大弱输入信号和抑制强无关信号的能力，是神经网络计算的核心元件。
- **关键区别**: **本论文使用常规 TFT（非铁电）实现双栅结构**，用于 ANN 计算而非存储。DG TFT 不具备非易失性，依赖电容器准静态电荷存储。
- **质量评价**: **中-高** - IEEE TED，电路实现完整（4x6 阵列俄罗斯方块分类），但非铁电相关工作。

**双栅相关性**: **相关但非铁电** - 双栅 TFT 的 ANN 实现，不涉及铁电材料。_作为双栅器件背景参考纳入。_

---

## 第四部分：关键词分布与关联分析

### 关键词关联图

```
                  双栅 / Dual-Gate / Double-Gate
                          |
          ┌───────────────┼───────────────┐
          |               |               |
      FeFET / 铁电晶体管    MFMIS结构        DG TFT（非铁电）
          |               |               |
    ┌─────┼─────┐         |               |
    |     |     |         |               |
  存储  存内计算 神经形态   3D集成         ANN/存内计算
    |     |     |         |
  TCAM  CIM   储备池计算   BEOL兼容
```

### 关键词频率统计

| 关键词 | 直接相关论文中频率 | 总论文中频率 |
|--------|-------------------|-------------|
| dual-gate / double-gate / 双栅 | 4/4 | 11/11 |
| FeFET / ferroelectric transistor | 4/4 | 9/11 |
| MFMIS | 2/4 | 3/11 |
| Reservoir computing | 1/4 | 1/11 |
| In-memory computing / CiM | 2/4 | 4/11 |
| IGZO / IWO (oxide TFT) | 2/4 | 4/11 |
| BEOL / monolithic 3D | 2/4 | 3/11 |
| HZO / HfO2 | 3/4 | 7/11 |

### 研究主题聚类

**聚类 A: 双栅 FeFET 器件物理与结构**（论文 2, 5, 6, 7, 9, 10）
- 综述双栅 FeFET 作为独立架构的地位
- MFMIS 与双栅结构的关系与区别
- 双栅实现存储/逻辑功能的独立控制

**聚类 B: 双栅 FeFET 在神经形态计算中的应用**（论文 1, 6）
- 双栅 MPB TFT 作为物理储备池
- 双栅增强储备池状态区分度
- LIF 神经元实现

**聚类 C: 双栅 FeFET 在存储与存算一体中的应用**（论文 3, 4, 5）
- 双栅 FeFET TCAM
- 双栅 IWO 晶体管与 FeFET 3D 集成
- 多级存储单元

**聚类 D: 双栅 TFT（非铁电）**（论文 11）
- 双栅 TFT 用于 ANN 硬件
- 作为背景技术参考

---

## 第五部分：文献库中缺失的关键引用论文

以下双栅 FeFET 关键论文在现有文献中被引用但 **不在文献库中**，建议纳入：

1. **Mulaosmanovic H, et al.** "Ferroelectric transistors with asymmetric double gate for memory window exceeding 12 V and disturb-free read." *Nanoscale*, 2021. （被论文 1 引用为 Ref [57]）
   - 核心贡献: 非对称双栅 FeFET 实现 >12V 存储窗口和无干扰读取。

2. **Jeong S, et al.** "All-Sputter-Deposited Hf0.5Zr0.5O2 Double-Gate Ferroelectric Thin-Film Transistor with Amorphous Indium-Gallium-Zinc Oxide Channel." *IEEE Electron Device Letters*, 2023. （被论文 1 引用为 Ref [58]）
   - 核心贡献: 全溅射 HZO 双栅 FeTFT，IGZO 沟道。

3. **Liu L, Kumar S, Thomann S, et al.** "Compact and high-performance TCAM based on scaled double-gate FeFETs." *arXiv:2304.03868*, 2023. （被论文 3 引用为 Ref [77]）
   - 核心贡献: 基于缩放双栅 FeFET 的紧凑高性能 TCAM。

---

## 第六部分：研究趋势与建议

### 趋势分析

1. **双栅 FeFET 研究从概念走向系统集成**: 2021 年 Mulaosmanovic 提出非对称双栅 FeFET 器件后，2024 年 Kim 等人将其成功应用于全集成模拟储备池计算系统，体现了从器件到系统的跨越。

2. **MFMIS 架构与双栅的融合**: 多个论文显示 MFMIS 结构（铁电电容 + MOSFET 串联）与双栅架构存在紧密联系，本质上双栅 FeFET 可看作 MFMIS 的扩展形式。

3. **氧化物半导体（IGZO/IWO）沟道是双栅 FeFET 的主流选择**: 因低温工艺兼容 BEOL 和 3D 集成，IGZO/IWO 是最常见的双栅 FeFET 沟道材料。

4. **双栅 FeFET 的应用从存储扩展到计算**: 早期聚焦存储窗口（TCAM、MLC），近期扩展到神经形态计算（储备池计算、LIF 神经元）。

### 建议阅读路径

- **入门**: 论文 2（Li 2025, Advanced Materials 综述）-> 论文 9（Kim 2021, APL Materials 综述），了解双栅 FeFET 架构概览
- **器件物理**: 论文 5（Kim 2024, Science Advances），了解栅极堆叠工程
- **系统应用**: 论文 1（Kim 2024, Nature Communications），了解双栅 FeFET 在 ARC 中的完整系统实现
- **存算一体**: 论文 3（刘勇 2023）和论文 4（Luo 2022），了解双栅在 TCAM 和 CIM 中的应用
- **补充**: 补齐缺失的 3 篇关键引用论文

---

*本报告由 literature-keyword-indexer agent 自动生成*
*报告路径: `/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/Keywords-Report/dual-gate-ferroelectric-transistor-report.md`*
