import sys
import os
from operator import add
import re
import pyspark.sql.functions as F
import pandas as pd
import string

os.environ['SPARK_HOME'] = "C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7"
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python")
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python\lib\\py4j-0.10.4-src.zip")

def square(x):
    return x**2

def square_list(x):
    return [float(val)**2 for val in x]

def convert_ascii(number):
    return [number,string.ascii_letters[number]]

try:
    from pyspark import SparkContext
    from pyspark import SparkConf
    from pyspark.sql import SQLContext
    from pyspark.sql.functions import *
    from pyspark.sql.types import *
    from pyspark.ml.linalg import Vectors, VectorUDT
    config = SparkConf().setAll([('spark.num.executors','10'),('spark.ui.port','4050')])
    sc = SparkContext(conf=config)
    sqlContext = SQLContext(sc)
    df = sc.parallelize([(1,2,3),(4,5,6),(7,8,9)]).toDF(['a','b','c'])
    df.select('a',when(df['a']==1,'One').when(df['a']==2,'Two').otherwise('Three')).show()
    sc.stop()
except ImportError as e:
    print ("Error importing Spark Modules", e)
    sys.exit(1)