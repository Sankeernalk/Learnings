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


try:
    from pyspark import SparkContext
    from pyspark import SparkConf
    from pyspark.sql import SQLContext
    from pyspark.sql.functions import *
    from pyspark.sql.types import *
    config = SparkConf().setAll([('spark.num.executors','10'),('spark.ui.port','4050')])
    sc = SparkContext(conf=config)
    sqlContext = SQLContext(sc)
    from pyspark.sql.types import IntegerType
    rdd = sc.textFile("C:\\Users\\611419222\\Documents\\hadoop\\ritu_proj\\spark\\temp_test.txt")
    header = rdd.first()
    header_mod = [x.encode("utf-8") for x in header.split('|')]
    rdd = rdd.filter(lambda line: line!=header)
    rdd = rdd.map(lambda line:line.split('|'))
    df1 = rdd.toDF(header_mod)
    df1.show()
    sc.stop()
except ImportError as e:
    print ("Error importing Spark Modules", e)
    sys.exit(1)