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
    df = sqlContext.createDataFrame([('foo','bar'),('baz',None)],('a','b'))
    #df_text = df.withColumn("combined",myConcat(*df.columns)).select("combined")
    #df_text.show()
    #df_text.coalesce(1).write.format("text").option("header","true").mode("overwrite").save("sample_out")
    #df.show()
    df_par = df.select(concat_ws(',','a','b').alias('Combined'))
    df_par.coalesce(1).write.format("csv").option("header","true").mode("append").save("sample_out")
    sc.stop()
except ImportError as e:
    print ("Error importing Spark Modules", e)
    sys.exit(1)