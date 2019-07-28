import sys
import os

os.environ['SPARK_HOME'] = "C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7"
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python")
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python\lib\\py4j-0.10.4-src.zip")

def moving_avg(lines):
    counter = 0
    k = 3
    list_temp =[]
    list_sum = []
    list_tar = []
    for i in lines:
        list_temp.append(i)
    for i in list_temp:
        list_sum = list_temp[counter:k + counter]
        if len(list_sum) == 3:
            sum_temp = sum(list_sum) / k
            list_tar.append(round(sum_temp, 2))
        counter += 1
    return list_tar

try:
    from pyspark import SparkContext,SparkConf
    from pyspark.sql import SQLContext
    import pyspark.sql.functions as F
    config = SparkConf().setAll([('spark.num.executors','10'),('spark.ui.port','4050')])
    sc = SparkContext(conf=config)
    sqlContext = SQLContext(sc)
    rdd = sc.textFile("C:\\Users\\611419222\\PycharmProjects\\HiveConnect\\sample.txt",3)
    rdd = rdd.flatMap(lambda x:x.split(' ')).map(lambda x:int(x))
    rdd1 = rdd.mapPartitions(moving_avg)
    print(rdd1.collect())
    sc.stop()
except ImportError as e:
    print("Error importing modules",e)
    sys.exit(1)