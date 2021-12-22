#!/usr/bin/env python3
#coding: UTF-8
"""
@author: huangwanghui
@time: 2020/2/1 11:50
"""

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.classification import SVMWithSGD

conf = SparkConf().setAppName("ex4").setMaster("spark://master:7077")
sc = SparkContext(conf=conf)
sc.setLogLevel("WARN")   # 设置日志级别
spark = SparkSession(sc)

TRAINDATAPATH = "/ex4/dataset/train_after.csv"
TESTDATAPATH = "/ex4/dataset/test_after.csv"

def GetParts(line):
    """
    将读取的数据集 train_after.csv、test_after.csv 转换为标准lable-feature形式，例如:
    ['1','2','3','4','0']  --> LabeledPoint(0, [2.0,3.0,4.0])
    :param line:  读取的字符串
    :return:
    """
    parts = line.split(',')
    return LabeledPoint(float(parts[4]),Vectors.dense(float(parts[1]),float(parts[2]),float(parts[3])))

def Getpoint(model,point):
    """
    预测并返回结果(元组)
    :param model: 训练集构建的SVMWithSGD模型
    :param point: 测试集数据，标准LabeledPoint类型数据
    :return:(测试集预测得分，原始标签)
    """
    score = model.predict(point.features)
    return (score,point.label)

def predict(Iterations=1000,threshold=-90000):
    """
    SVMWithSGD 预测淘宝回头客整体流程
    :return:
    """

    # 【完成下面代码缺失处】

    # 1.读取数据

    train_data = sc.textFile( )
    test_data = sc.textFile( )

    # 2.数据标准化

    train = train_data.map(lambda line: )
    test = test_data.map(lambda line: )

    # 3.构建模型

    model =   # 默认迭代1000次

    # 4.评估模型
    model.setThreshold(threshold)  # 默认阈值 -90000

    scoreAndLabels = test.map(lambda point:  )
    # 计算精度

    accuracy = scoreAndLabels.filter(lambda l:  ).count() / test.count()

    return accuracy

if __name__ == "__main__" :

    accuracy = predict()
    print("accuracy: "+ str(predict()*100) + "%")