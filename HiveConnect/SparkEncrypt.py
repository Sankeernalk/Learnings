import sys
import os
from operator import add
import re
import pyspark.sql.functions as F
import hashlib

os.environ['SPARK_HOME'] = "C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7"
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python")
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python\lib\\py4j-0.10.4-src.zip")

def encrypt_name(lines):
    result = hashlib.sha256(lines.encode())
    return result.hexdigest()


try:
    from pyspark import SparkContext
    from pyspark import SparkConf
    from pyspark.sql import SQLContext
    from pyspark.sql.functions import *
    from pyspark.sql.types import *
    config = SparkConf().setAll([('spark.num.executors','10'),('spark.ui.port','4050')])
    sc = SparkContext(conf=config)
    sqlContext = SQLContext(sc)
    rdd1 = sc.textFile("C:\\Users\\611419222\\PycharmProjects\\HiveConnect\\sample.txt")
    rdd2 = rdd1.map(lambda line: line.split(' ')[1])
    rdd_first = rdd1.map(lambda line: line.split(' ')[0])
    #print(rdd2.collect())
    rdd3 = rdd2.map(encrypt_name)
    print(rdd3.collect())
    print(rdd_first.collect())
    rdd_fin = rdd_first.zip(rdd3)
    rdd_fin.coalesce(1).saveAsTextFile('C:\\Users\\611419222\\PycharmProjects\\HiveConnect\\sample_out_1')
    print(rdd_fin.collect())
    sc.stop()
except ImportError as e:
    print ("Error importing Spark Modules", e)
    sys.exit(1)