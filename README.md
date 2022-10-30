<h1 align='center'>重庆大学计算机学院“大数据课程群”</h1>

<h5 align='center'> Design by W.H. Huang | Direct by Prof. Feng</h5>

## 引言

> :slightly_smiling_face: 指导设计 *@ Prof. Feng*  ;  具体设计 *@ W.H. Huang*

重庆大学计算机学院“大数据课程群”实验、PPT及优秀案例：

- 开源地址：[CQU_bigdata](https://github.com/Wanghui-Huang/CQU_bigdata)

- 当前版本：`Beta V1.0` --> `Beta V2.0`-->`Relase V1.6.1`-->`Relase V2.1`-->`Relase V2.2`

- 完成度：`95%` --> `100%` --> `持续开源完善`

- 版本管理：`git`

- 开发时间：`(Stage1)2020/01/20 -- 2020/05/07` ,  基本框架设计完成；

  ​                    `(Stage2)2020/05/07 -- 2020/08/17` ，更进一步细节完善；

  ​                    `(Stage3)2020/08/17 -- 至今` ，开源大家共同完善。

下面将进行简略介绍。

## 开源贡献

本门课至今已开设了三年，也很开心陪伴我度过了三年读研时光。至这门课开设以来，我们所有的资料都是开源的，**也非常鼓励大家参与开源建设**。

可以和大家分享的是，每一年优秀课设、高分获得者同学一大半都参与过我们的开源项目。**有个别实验来源就是改编于往届同学的优秀课设**。

在这里我们给出具体的鼓励开源细则，希望每一年选这门课同学都可以积极参与，获得优异成绩~

|                           贡献类型                           | （对应）实验加分 |                             细则                             |
| :----------------------------------------------------------: | :--------------: | :----------------------------------------------------------: |
|              issue：反馈实验bug、优化实验流程等              |      +5~+10      |   根据issue质量给分，请参考issue中助教点评过的高质量issue    |
|        文档：对实验设计不足的地方进行优化，并撰写文档        |     +10~+20      | 如，ex2@[leexinhao](https://github.com/leexinhao)同学建议加入远程开发，助教采纳后并完善其初稿文档。本次ex2实验成绩给予满分。 |
| 文档：每一年同学可根据自己的想法完成非常棒的课设，并提交案例文档，作为我们的实验补充 |   本门课程优秀   | 质量很重要，如果质量尚不足，只能给实验加分，不能算作总成绩优秀。 |

## 实验设计

> 实验所有相关步骤、代码等均在实际环境测试运行通过。

下表共涉及到`8`个实验，其中：

- 必做实验：ex1、ex2、ex5；
- 选做实验：ex0；
- 2选1实验：ex3 、ex4；

具体请看下表，包含**成绩计分说明**。

| 实验序号 |                            实验名                            |                           实验内容                           |  页数  |               :warning:成绩计分说明               |
| :------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----: | :-----------------------------------------------: |
|   ex0    | [HelloLinux](https://github.com/Wanghui-Huang/CQU_bigdata/blob/master/Experiment/Ex0_HelloLinux/ex0.md) |              掌握后续实验所需Linux相关操作/知识              |   19   | **不计分**，但**强烈建议**对Linux不熟悉的同学练习 |
|   ex1    | [SettingUpEnvironment](https://github.com/Wanghui-Huang/CQU_bigdata/blob/master/Experiment/Ex1_SettingUpEnvironment/ex1.md) |           搭建Spark/Hadoop分布式环境，四种方式可选           |   27   |           请查看对应实验文档说明，下同            |
|   ex2    | [WordCount](https://github.com/Wanghui-Huang/CQU_bigdata/blob/master/Experiment/Ex2_WordCount/ex2.md) | Spark单机版环境下基于相关数据集完成青年择偶观统计并进行可视化 |   10   |                                                   |
|   ex3    | [Ex3_CHN](https://github.com/Wanghui-Huang/CQU_bigdata/blob/master/Experiment/Ex3/Ex3_CHN/ex3.md) |      Spark分布式环境下使用Spark  MLlib完成手写数字识别       |   14   |                                                   |
|          | [Ex3_Kmeans](https://github.com/Wanghui-Huang/CQU_bigdata/blob/master/Experiment/Ex3/Ex3_Kmeans/ex3.md) | Spark分布式环境下基于`iris` 数据集完成K-Means聚类并进行可视化 |   10   |                                                   |
|   ex4    | [Ex4_FaceRecognition](https://github.com/Wanghui-Huang/CQU_bigdata/blob/master/Experiment/Ex4/Ex4_FaceRecognition/ex4.md) |    Spark分布式环境下基于多层感知机模型完成高精度人脸分类     | 建设中 |                                                   |
|          | [Ex4_CustomerForecast](https://github.com/Wanghui-Huang/CQU_bigdata/blob/master/Experiment/Ex4/Ex4_CustomerForecast/ex4.md) | Spark分布式环境下基于相关数据集完成淘宝回头客预测并进行可视化 |   9    |                                                   |
|   ex5    | [Ex5_KnowledgeGraph](https://github.com/Wanghui-Huang/CQU_bigdata/blob/master/Experiment/Ex5/Ex5_KnowledgeGraph/ex5.md) |                         华为特色实验                         |   10   |                                                   |

## PPT 设计

> PPT 设计尽量保证美观大方，素材来源广泛限于自身所学，可能有所错漏。

PPT 部分章节因为自身无法较好把握整体结构，最开始尚未完成设计，现在已基本完成。

- `2020/09/17更新`：每个实验也对应增加，**实验PPT介绍 & 录音讲解** ；
- `2021/12/20更新`：:warning: Git上（课件）已更新，**请以我们项目`CQU_bigdata/PPT`目录下课件为准**。

具体设计见下表：

| 序号 |            章节名             |                           PPT内容                            | 完成度 | 页数 | 备注 |
| :--: | :---------------------------: | :----------------------------------------------------------: | :----: | :--: | :--: |
|  1   |          大数据概述           |                 介绍大数据概念、来源、应用等                 |   √    |  51  |      |
|  2   | Hadoop平台（Hadoop概述+HDFS） |                   介绍Hadoop及HDFS相关知识                   |   √    |  38  |      |
|  3   | Hadoop平台（YARN+MapReduce）  |                   介绍Hadoop分布式相关知识                   |   √    |  57  |      |
|  4   |       分布式数据库Hbase       |                    介绍分布式数据库Hbase                     |   √    |  65  |      |
|  5   |           Spark系统           |                      介绍Spark相关知识                       |   √    |  59  |      |
|  6   |          大数据算法           |     介绍大数据相关算法，如：分类、聚类、关联规则、预测等     |   √    | 158  |      |
|  7   |          大数据应用           | 介绍大数据相关应用，如：推荐系统、地震大数据、交通大数据、环境大数据等 |   √    |  54  |      |
|  8   |        图计算与流计算         |               介绍大数据图计算、流计算相关知识               |   √    |  73  |      |

## 优秀案例

我们根据最近几年冯老师班大数据课程，择优选出了20+套优秀案例。每套案例组织格式如下：

- 案例正文：包含摘要、版权信息、背景、正文、参考文献等信息；
- 案例说明：案例教学指导手册；
- 案例PPT：PPT供教师讲解、学生分享等；
- 附件资源：包含案例完整的数据集、代码、说明等。

所有案例，您可在[CQU_bigdata/CaseShow](https://github.com/Wanghui-Huang/CQU_bigdata/tree/master/CaseShow) 目录下找到。

## 特别致谢

以下致谢名单不分先后：

- [YangYiming919](https://github.com/YangYiming919) ，2018级本科生
- [Rayquaza](https://github.com/marxoffice)，2018级本科生
- [white_windmills](https://github.com/leexinhao) ，2019级本科生
- [Hongcheng-Gao](https://github.com/Hongcheng-Gao)   ，2019级本科生
- [Tan Yong](https://github.com/a-fly-fly-bird) ，2019级本科生
- [Cquyxf](https://github.com/Cquyxf) ，2019级本科生
- [chen hongyu](https://github.com/hqcheng-cqu) ，2019级本科生
- [ZJY](https://github.com/Info4Rec) ，2020级研究生 |助教
- [trevery](https://github.com/trevery) ，2020级研究生
- [hqcheng-cqu](https://github.com/hqcheng-cqu) ，2021级研究生 |助教

## 阶段小结

- `2022/01/04` 

  1. 更新ex5
  2. 新增优秀案例20+套
  
- `2021/12/22` 

  - 实验修改
  
    1. ex0：新增虚拟机安装教程 | 完善文档
    2. ex1：新增虚拟机分布式教程 | 完善文档
    3. ex2：新增远程开发教程 | 完善文档
    4. ex3：新增Ex3_CHN实验 | 完善文档 
    5. ex4：新增EX4_FaceRecognition
  
  - Issue处理
  
    处理完issue所有反馈的问题，并修改完善了文档
  
  - 其它
  
    - 新增：扩展实验选择、成绩计分细则、致谢等
    - PPT修改
    - 文档整体结构修整
    - ...
  
- `2020/09/17` 

  - 课程PPT和实验已正式投入使用，所有参加该门课程的同学都可一起加入完善。

- ` 2020/08/17` 

  - 基本上PPT和实验已经全部按老师的指导完成，PPT一些算法细节可能要补充参数说明。

- `2020/05/07` 

  - 隔了几个月终于把最后一部分课件（`第二章：Hadoop&Spark简介`）做完了，感觉还是相当耗脑的，主要还是如何把握整体框架要花费较多时间思考，其次就是画图和表格也较为耗费时间。

- `2020/02/10` 

  - 距离具体正式开工设计正好过去了`20` 天，完成`Beta_V1.0` 版本。

  

