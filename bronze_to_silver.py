# Databricks notebook source
dbutils.fs.ls("/mnt/bronze/SalesLT/")

# COMMAND ----------

# MAGIC %md
# MAGIC Doing transformation for all atbles

# COMMAND ----------

table_name = []

for i in dbutils.fs.ls("/mnt/bronze/SalesLT/"):
    table_name.append(i.name.split('/')[0])

# COMMAND ----------

table_name

# COMMAND ----------

from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType

for i in table_name:
    path = '/mnt/bronze/SalesLT/' + i + '/' + i + '.parquet'
    df = spark.read.format('parquet').load(path)
    column = df.columns

    for col in column:
        if "Date" in col or "date" in  col:
            df = df.withColumn("ModifiedDate", date_format(from_utc_timestamp(df["ModifiedDate"].cast(TimestampType()), "UTC"), "yyyy-MM-DD"))

    output_path = '/mnt/silver/SalesLT/' + i + '/'
    df.write.format('delta').mode('overwrite').save(output_path)

# COMMAND ----------

display(df)

# COMMAND ----------


