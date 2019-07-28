import os
import sys
import pyspark.sql.functions as F
import pyspark.sql.types as T


os.environ['SPARK_HOME'] = "C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7"
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python")
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python\lib\\py4j-0.10.4-src.zip")

try:
    from pyspark import SparkContext
    from pyspark import SparkConf
    from pyspark.sql import SQLContext
    from pyspark.sql.types import *
    config = SparkConf().setAll([('spark.num.executors','10'),('spark.ui.port','4050')])
    sc = SparkContext(conf=config)
    sqlContext = SQLContext(sc)
    rdd = sc.textFile("C:\\Users\\611419222\\PycharmProjects\\HiveConnect\\sample.txt")
    rdd = rdd.map(lambda x:x.split(',')).map(lambda x:(x[0],int(x[1])))
    rdd = rdd.reduceByKey(lambda x,y:x+y).map(lambda x:(x[0].upper(),x[1]))
    print(rdd.collect())
    sc.stop()
except ImportError as e:
    print(e)