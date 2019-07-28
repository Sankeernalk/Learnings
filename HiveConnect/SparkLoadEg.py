from __future__ import print_function
from pyspark.sql.types import StringType
from pyspark.sql.functions import udf
from pyspark import SparkContext
from pyspark import SparkConf,SparkContext,SQLContext,Row,HiveContext
import pyspark.sql.functions as func
from pyspark.sql.functions import *
from datetime import datetime
from functools import reduce
from pyspark.sql import DataFrame
from pyspark.sql.types import *
from pyspark.sql import Row,functions as F
from pyspark.sql.window import Window
from pyspark.sql.functions import broadcast
from datetime import timedelta
import hashlib
import sys

if __name__ == '__main__':
    if len(sys.argv) < 6:
        print('Input Parameter missing',file=sys.stderr)
        exit(-1)
    sc = SparkContext(appName='SCD'+sys.argv[3])
    sqlContext = HiveContext(sc)
    tgt_schema = sys.argv[1]
    tgt_tbl_nm = sys.argv[2]
    src_schema = sys.argv[1]
    src_tbl_nm = sys.argv[3]
    load_dt = sys.argv[4]
    hist_delta = sys.argv[5]
    src_schema_tbl = src_schema+'.'+src_tbl_nm
    tgt_schema_tbl = tgt_schema+'.'+tgt_tbl_nm
    tgt_schema_stg_tbl = tgt_schema+'.'+tgt_tbl_nm+'_tgt'

    sqlContext.setConf("hive.exec.dynamic.partition","true")
    sqlContext.setConf("hive.exec.dynamic.partition.mode","nonstrict")
    sqlContext.setConf("hive.execution.engine","spark")
    sqlContext.setConf("hive.vectorized.execution.enabled","true")
    sqlContext.setConf("hive.vectorized.execution.reduce.enabled","true")

    delta_columns = ["delta_acct_nbr","delta_account_sk_id","delta_zip_code","delta_primary_state","delta_eff_start_date","delta_eff_end_date",
                     "delta_load_tm","delta_hash_key","delta_eff_flag"]
    hist_columns = ["acct_nbr","account_sk_id","zip_code","primary_state","eff_start_date","eff_end_date","load_tm","hash_key","eff_flag"]

    eff_close_dt = "3099-12-31"
    eff_flag_curr = "Y"
    eff_flag_non_curr = "N"
    eff_start_date_hist = "Today"
    eff_start_date_delta = "Tomorrow"
    hash_udf = func.udf(lambda x:hashlib.sha256(str(x)).hexdigest().upper())
    dt = datetime.now()
    load_tm = dt.strftime('%Y-%m-%d %H:%M:%S')



