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
    config = SparkConf().setAll([('spark.num.executors','10'),('spark.ui.port','4050')])
    sc = SparkContext(conf=config)
    sqlContext = SQLContext(sc)
    from pyspark.sql.types import IntegerType
    df_pd = pd.DataFrame(data={'integers':[1,2,3],'floats':[-1.0,0.5,2.7],'integer_arrays':[[1,2],[3,4,5],[6,7,8,9]]})
    df = sqlContext.createDataFrame(df_pd)
    df.show()
    square_udf_int = udf(lambda z: square(z),IntegerType())
    square_udf_float = udf(lambda z: square(z),FloatType())
    square_list_udf = udf(lambda y: square_list(y),ArrayType(FloatType()))
    array_schema = StructType([StructField('number',IntegerType(),nullable=False),StructField('letters',StringType(),nullable=False)])
    spark_convert_ascii = udf(lambda z: convert_ascii(z),array_schema)
    df.select('integers','floats',square_udf_int('integers').alias('int_squared'),square_udf_float('floats').alias('float_squared')).show()
    df.select('integer_arrays',square_list_udf('integer_arrays')).show()
    df.select('integers',spark_convert_ascii('integers').alias('ascii_map')).show()
    sc.stop()
except ImportError as e:
    print ("Error importing Spark Modules", e)
    sys.exit(1)