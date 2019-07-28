import sys
import os
from operator import add
import re
import pyspark.sql.functions as F
import pyspark.sql.types as t
import pyspark.sql.column as c

os.environ['SPARK_HOME'] = "C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7"
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python")
sys.path.append("C:\\opt\\spark\\spark-2.2.0-bin-hadoop2.7\\python\lib\\py4j-0.10.4-src.zip")

def recur_man(emp_id,lvl,list1):
    if (type(list1) == int):
        list1 = []
    with open("C:\\Users\\611419222\\Documents\\Python\\employee_1.txt") as f:
            for lines in f:
                if lines.split(',')[0] == emp_id:
                    if lines.split(',')[9] is None:
                        list1.append('NA')
                    else:
                        list1.append(lines.split(',')[9])
                    lvl-=1
                    if lvl!=0:
                        recur_man(lines.split(',')[9],lvl,list1)
    for i in range(3-len(list1)):
        list1.append('NA')
    return list1


try:
    from pyspark import SparkContext
    from pyspark import SparkConf
    from pyspark.sql import SQLContext
    from pyspark.sql.functions import *
    from pyspark.sql.types import *
    from pyspark.sql.window import Window
    from pyspark.sql import functions as Fun
    config = SparkConf().setAll([('spark.num.executors','10'),('spark.ui.port','4050')])
    sc = SparkContext(conf=config)
    sqlContext = SQLContext(sc)
    rdd = sc.textFile("C:\\Users\\611419222\\Documents\\Python\\employee_1.txt")
    header = rdd.first()
    header_mod = [x.encode("utf-8") for x in header.split(',')]
    rdd = rdd.filter(lambda line: line!=header)
    rdd = rdd.map(lambda line: line.split(','))
    df1 = rdd.toDF(header_mod)
    spark_recur_man = udf(lambda x,y,z: recur_man(x,y,z),t.ArrayType(t.StringType()))
    list1 = F.lit(0)
    #df1.select('EMPLOYEE_ID', spark_recur_man('EMPLOYEE_ID', F.lit(3), list1).alias('heirarchy')).show(truncate=False)
    df1_mod = df1.select('EMPLOYEE_ID',spark_recur_man('EMPLOYEE_ID',F.lit(3),list1).alias('heirarchy'))
    df1_mod.show(truncate=False)
    df1_mod1 = df1_mod.select('EMPLOYEE_ID',explode('heirarchy'))
    #df1_mod1.show()
    df_mod2 = df1_mod1.select('EMPLOYEE_ID','COL').withColumn('row_num',Fun.row_number().over(Window.partitionBy('EMPLOYEE_ID').orderBy('EMPLOYEE_ID')))
    df_mod2.groupby('EMPLOYEE_ID').pivot('row_num').agg(first('COL')).orderBy('EMPLOYEE_ID').fillna(0).show()
    sc.stop()
except ImportError as e:
    print ("Error importing Spark Modules", e)
    sys.exit(1)