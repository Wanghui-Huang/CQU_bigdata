#!/usr/bin/env python3
#coding: UTF-8
"""
@author: huangwanghui
@time: 2020/1/29 10:59
"""

from pyspark.ml.clustering import KMeans
import matplotlib.pyplot as plt

class Kmeans:

    def searchK(self, SAVAPATH, dataDF, k_min, k_max):
        """
        寻找最佳K值
        :param SAVAPATH: 保存结果路径
        :param dataDF: DataFrame类型数据
        :param k_min: 最小k值
        :param k_max: 最大k值
        :return:
        """

        # 计算不同k值对应损失
        k_range = range(k_min,k_max)  # 指定k寻找范围
        costs = []
        # 利用pyspark.ml.clustering.Kmeans类函数计算损失
        # 1.定义KmeansModel，对DataFrame类型数据进行整体化处理，生成带预测簇标签的数据集
        # 2.计算损失
        for k in k_range:
            kmeansModel = KMeans()\
                          .setK(k)\
                          .setFeaturesCol('features')\
                          .setPredictionCol('prediction')\
                          .fit(dataDF)
            # 【完成以下编码】计算损失
            # spark 3.x以上版本，需要使用ClusterEvaluator代替computeCost方法来进行模型评价
            # https://github.com/Wanghui-Huang/CQU_bigdata/issues/24
            costk =
            costs.append(costk)

        # 可视化损失结果
        fig, ax = plt.subplots(1, 1, figsize=(8, 6))
        ax.plot(k_range, costs)
        ax.set_xlabel('k')
        ax.set_ylabel('cost')
        # 保存k-cost结果
        if not os.path.exists(SAVAPATH):
            os.makedirs(SAVAPATH)
        plt.savefig(SAVAPATH + 'k_cost.png')

    def printResults(self, dataDF, best_k,end=50):
        """
        打印聚类结果
        :param dataDF: DataFrame类型数据
        :param best_k: 指定最佳K值
        :param end: 打印多少行
        :return:
        """
        kmeansModel = KMeans() \
                      .setK(best_k) \
                      .setFeaturesCol('features') \
                      .setPredictionCol('prediction') \
                      .fit(dataDF)
        # 获取聚类预测结果
        # 1.利用pyspark.ml.clustering.KMeans中transform方法得到聚类结果
        # 2.利用DataFrame中collect方法转换DateFrame --> python list
        # 【现在完成以下编码】

        resDF =
        resList =
        # 打印部分聚类结果
        for item in resList[:end]:
            print(str(item[0]) + ' is predcted as cluster' + str(item[1]))


