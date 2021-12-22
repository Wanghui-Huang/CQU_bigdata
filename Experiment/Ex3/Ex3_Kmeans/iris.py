#!/usr/bin/env python3
#coding: UTF-8
"""
@author: huangwanghui
@time: 2020/1/29 11:07
"""

from pyspark.sql import Row
from pyspark.ml.linalg import Vectors
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from kmeans import Kmeans

DATAPATH = 'hdfs://master:9000/ex/ex3dataset/iris.data'
SAVAPATH = '/home/hadoop/Experiment/Ex3/Ex3_Kmeans/results/'

conf = SparkConf().setAppName("ex3").setMaster("spark://master:7077")
sc = SparkContext(conf=conf)
sc.setLogLevel("WARN")   # 设置日志级别
spark = SparkSession(sc)


def getDF():
    """
    读取数据，并对数据进行过滤等操作
    :return: 返回DataFrame类型数据格式
    """

    # 读取数据
    # 利用filter操作过滤掉空数据,如：[['1'],['2'],['']] --> [['1'],['2']]
    # 现在你需要【完成以下编码】

    rawData = sc.textFile(DATAPATH).filter(lambda ele: )

    # 转换为DataFrame
    # 你应该依次利用SparkRDD操作完成：
    # 1.map 将RDD每一行数据以逗号‘，’分隔
    # 2.map RDD每一行转换为Row


    dataDF = rawData.map(lambda line: )\
                    .map(lambda p: )\
                    .toDF()
    return dataDF

def f(x):
    """
    将x转换为Vector
    :param x: 对应iris.data（RDD）每一行
    :return:
    """
    rel = {}
    rel['features'] = Vectors.dense(float(x[0]), float(x[1]), float(x[2]), float(x[3]))
    return rel


def main():
    # 1.读取数据
    dataDF = getDF()

    # 2.测试最佳K值，第一次出现明显拐角处便是最佳K值
    km = Kmeans()
    km.searchK(SAVAPATH,dataDF,2,12)    # 查看保存的图片，选择最佳K值

    # 3.打印聚类结果
    # km.printResults(dataDF,best_k=3)


if __name__ == "__main__":

    # run code
    main()
