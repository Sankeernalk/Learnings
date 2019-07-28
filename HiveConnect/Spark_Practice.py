import os, sys
os.environ['SPARK_HOME'] = "C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7"
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python")
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python\lib\\py4j-0.10.4-src.zip")
import pyspark.sql.functions as F
from dateutil.relativedelta import relativedelta

def month_range(d1,d2):
    return [d1 + relativedelta(months=+x) for x in range((d2.year-d2.year)*12+d2.month-d1.month+1)]

try:
    from pyspark import SparkContext,SparkConf
    from pyspark.sql import SQLContext,HiveContext
    from pyspark.sql.functions import *
    from pyspark.sql.types import *
    config = SparkConf().setAll([('spark.num.executors',10),('spark.ui.port','4050')])
    sc = SparkContext(conf=config)
    sqlContext = SQLContext(sc)
    rdd = sc.textFile("C:\\Users\\611419222\\PycharmProjects\\HiveConnect\\empph.txt")
    header = rdd.first()
    header_mod = header.strip().split(' ')
    rdd = rdd.filter(lambda x:x != header)
    rdd = rdd.map(lambda x:x.strip().split(' '))
    #print(rdd.collect())
    df1 = rdd.toDF(header_mod)
    month_range_udf = udf(month_range,ArrayType(DateType()))
    df1 = df1.withColumn("Start_Date1",F.to_date("start_date")).withColumn("End_date1",F.to_date("end_date"))
    df1 = df1.select("Name","Company","Start_Date1","End_date1").withColumn("Date", explode(month_range_udf("Start_Date1", "End_date1")))
    df1 = df1.select("Name","Company",year("Date"),month("Date"))
    df1 = df1.filter(F.col("Name").like("%resh%"))
    df1.show()
    sc.stop()
except ImportError as e:
    print("error while importing modules "+e)
