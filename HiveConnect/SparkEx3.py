import sys
import os
from operator import add
import re
import pyspark.sql.functions as F

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
    rdd = sc.parallelize([(0,'A',223,'201603','PORT'),(0,'A',22,'201602','PORT'),(0,'A',422,'201601','DOCK'),(1,'B',3213,'201602','DOCK'),
                          (1,'B',3213,'201601','PORT'),(2,'C',2321,'201601','DOCK'),(2,'C',2321,'201601','SAN'),(2,'C',2321,'201601','SAN')])
    df_data = sqlContext.createDataFrame(rdd,['id','type','cost','date','ship'])
    #df_data.show()
    #print(df_data.columns)
    #df_data_pivot = df_data.groupBy(df_data.id,df_data.type).pivot('date').avg('cost')
    #df_data_pivot = df_data.groupBy(df_data.id,df_data.type).pivot('date').agg(first('ship'))
    df_data_pivot = df_data.groupBy('id','type','date','ship').count().groupBy('id','type').pivot('date').agg(max(struct('count','ship')))
    #df_data_pivot.explain()
    df_data_pivot.show()
    sc.stop()
except ImportError as e:
    print ("Error importing Spark Modules", e)
    sys.exit(1)