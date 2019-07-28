import sys
import os
from operator import add
import re

os.environ['SPARK_HOME'] = "C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7"
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python")
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python\lib\\py4j-0.10.4-src.zip")

def sepNum(lines):
    return re.findall('\d+|\D+',lines)

try:
    from pyspark import SparkContext
    from pyspark import SparkConf
    from pyspark.sql import SQLContext
    from pyspark.sql.functions import *
    from pyspark.sql.types import *
    config = SparkConf().setAll([('spark.num.executors','10'),('spark.ui.port','4050')])
    sc = SparkContext(conf=config)
    sqlContext = SQLContext(sc)
    #rdd1 = sc.textFile("C:\\Users\\611419222\\PycharmProjects\\HiveConnect\\sample.txt")
    #rdd2 = rdd1.map(lambda lines:(1,lines))
    #print(rdd2.getNumPartitions())
    #rdd3 = rdd2.repartition(10)
    print(sc.defaultParallelism)
    #print(rdd3.getNumPartitions())
    #print(sc.getConf().getAll())
    # rdd1_1 = sc.parallelize([1,2,3,4,5])
    # rdd1_2 = sc.parallelize([5,6,7,8,9])
    # rdd1_3 = rdd1_1.union(rdd1_2)
    # print(rdd1_3.collect())
    # print(rdd1_1.getNumPartitions())
    # print(rdd1_2.getNumPartitions())
    # print(rdd1_3.getNumPartitions())
    # rdd1_4 = rdd1_3.coalesce(1)
    # rdd1_4.saveAsTextFile(path='C:\\Users\\611419222\\PycharmProjects\\HiveConnect\\sample_out')
    #rdd = sc.parallelize([('a',1)])
    df = (sc.parallelize([(1,2,3),(2,1,2),(3,4,5)]).toDF(['a','b','c']))
    #print(df.agg(max(df.a)).first()[0])
    #print(df.select(max('a').alias('Max')).show())
    #print(df.select('a').describe().show())
    #print(df.select('a').rdd.max()[0])
    #df.registerTempTable('df_table')
    #sqlContext.sql('select max(a) as max_val from df_table').collect()[0]
    #df = sc.parallelize([('person1','[google,msn,yahooo]'),('person2','[fb.com,airbnb,wired.com]')]).toDF('Name','URL_Visited')
    df.show()
    print(df.describe())
    print(df.rdd.getNumPartitions())
    print(df.columns)
    sc.stop()
except ImportError as e:
    print ("Error importing Spark Modules", e)
    sys.exit(1)