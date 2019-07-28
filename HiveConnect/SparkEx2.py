import sys
import os
from operator import add
import re
import pyspark.sql.functions as F

os.environ['SPARK_HOME'] = "C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7"
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python")
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python\lib\\py4j-0.10.4-src.zip")

def sepNum(lines):
    return re.findall('\d+|\D+',lines)

def myConcat(*cols):
    concat_columns = []
    for c in cols:
        concat_columns.append(F.coalesce(c,F.lit('*')))
        concat_columns.append(F.lit(' '))
    #concat_columns.append(F.coalesce(cols[-1],F.lit('*')))
    return F.concat(*concat_columns)

try:
    from pyspark import SparkContext
    from pyspark import SparkConf
    from pyspark.sql import SQLContext
    from pyspark.sql.functions import *
    from pyspark.sql.types import *
    config = SparkConf().setAll([('spark.num.executors','10'),('spark.ui.port','4050')])
    sc = SparkContext(conf=config)
    sqlContext = SQLContext(sc)
    test_rdd = sc.parallelize([(1,2),(0,5),(2,4)])
    test_rdd1 = test_rdd.cache()
    #print(test_rdd.max(key= lambda x: x[0]))
    print(test_rdd.max())
    sc.stop()
except ImportError as e:
    print ("Error importing Spark Modules", e)
    sys.exit(1)