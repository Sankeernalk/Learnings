import sys
import os
from operator import add
import re
import pyspark.sql.functions as F
import pyspark.sql.types as t
import pyspark.sql.column as c

os.environ['SPARK_HOME'] = "C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7"
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python")
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python\lib\\py4j-0.10.4-src.zip")

def comm_list(line):
    list1 = []
    list1.append(line.split(',')[0])
    list1.append(line.strip().split(',')[1::])
    return list1

try:
    from pyspark import SparkContext
    from pyspark import SparkConf
    from pyspark.sql import SQLContext
    from pyspark.sql.functions import *
    from pyspark.sql.types import *
    from pyspark.sql.window import Window
    from pyspark.sql import functions as Fun
    config = SparkConf().setAll([('spark.num.executors','10'),('spark.ui.port','4050')])
    sc = SparkContext(conf=config)
    sqlContext = SQLContext(sc)
    rdd = sc.textFile("C:\\Users\\611419222\\Documents\\Python\\skillset.txt")
    rdd = rdd.map(lambda x: [x.split(',')[0],x.split(',')[1::]])
    #print(rdd.collect())
    # rdd = rdd.map(comm_list)
    df1 = rdd.toDF(['skill','list_agg'])
    df1_mod = df1.select('skill',explode('list_agg'))
    df1_mod.groupby('col').agg(Fun.collect_set('skill')).orderBy('col').show(truncate=False)
    sc.stop()
except ImportError as e:
    print ("Error importing Spark Modules", e)
    sys.exit(1)