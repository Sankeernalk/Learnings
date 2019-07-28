import sys
import os
from operator import add
import re
import pyspark.sql.functions as F
import hashlib

os.environ['SPARK_HOME'] = "C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7"
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python")
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python\lib\\py4j-0.10.4-src.zip")

@F.udf
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
    header = rdd1.first()
    rdd2 = rdd1.filter(lambda line:line!=header)
    rdd3 = rdd2.map(lambda line: line.split(','))
    header_mod = header.split(',')
    df = rdd3.toDF(header_mod)
    df_fin = df.withColumn('Encrypt_Name',F.lit(encrypt_name(df.Name))).select('Sl','Encrypt_Name')
    df_fin.coalesce(1).write.format("csv").option("header","true").mode("overwrite").save("sample_out")
    sc.stop()
except ImportError as e:
    print ("Error importing Spark Modules", e)
    sys.exit(1)