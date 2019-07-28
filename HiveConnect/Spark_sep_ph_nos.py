import sys
import os
from operator import add
import re
import pyspark.sql.functions as F

os.environ['SPARK_HOME'] = "C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7"
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python")
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python\lib\\py4j-0.10.4-src.zip")

def digletseg(lines):
    return re.findall('\D+',lines),re.findall('\d+',lines)

try:
    from pyspark import SparkContext,SparkConf
    from pyspark.sql import SQLContext
    from pyspark.sql import Row
    from pyspark.sql.functions import *
    from pyspark.sql.types import ArrayType,StructType,StructField,IntegerType,StringType
    config = SparkConf().setAll([('spark.num.executors','10'),('spark.ui.port','4050')])
    sc = SparkContext(conf=config)
    sqlContext = SQLContext(sc)
    rdd = sc.textFile("C:\\Users\\611419222\\PycharmProjects\\HiveConnect\\empph.txt")
    rdd = rdd.map(digletseg)
    #rdd_mod = rdd.map(lambda x:[(a,b) for a,b in zip(x.a,x.b)])
    print(rdd.collect())
    rdd_mod = rdd.map(lambda x:zip(x[0],x[1]))
    print(rdd_mod.collect())
    df1 = rdd.toDF(['a','b'])
    df1.show()
    #print(rdd.collect())
    # df1 = rdd.toDF(['Name','Phone'])
    # _zip = udf(lambda x,y: list(zip(x,y)),ArrayType(StructType([StructField("first",StringType()),StructField("second",StringType())])))
    # df1.withColumn("tmp",_zip('Name','Phone')).withColumn("tmp1",explode("tmp")).select("tmp1.first","tmp1.second").show()
    # #df1.show(truncate=False)
    sc.stop()
except ImportError as e:
    print("Error importing "+e)
    sys.exit(1)