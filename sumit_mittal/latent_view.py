from pyspark.sql import SparkSession
from dataset_utils import create_class_dataframe, create_age_dataframe
from pyspark.sql.function import *
from pyspark.sql.StructType import *


 

spark = SparkSession.builder.appName("CodeInterview.io").getOrCreate()

 

# -------------------------------
# Step 1: Define data (as tuples)
# -------------------------------
#Header "order_id","user_id","restaurant_id","city","order_amount","order_time","delivery_time","rating"

 

data = [
    (1,"U1","R1","Chennai",250,"2026-06-01 10:00:00","2026-06-01 10:40:00",4.5),
    (2,"U2","R2","Chennai",300,"2026-06-01 11:00:00","2026-06-01 11:55:00",4.0),
    (3,"U3","R1","Bangalore",200,"2026-06-01 12:00:00","2026-06-01 12:30:00",3.5),
    (4,"U4","R3","Bangalore",500,"2026-06-01 13:00:00","2026-06-01 14:10:00",4.8),
    (5,"U2","R2","Chennai",150,"2026-06-01 14:00:00","2026-06-01 14:50:00",4.2),
    (6,"U5","R4","Bangalore",350,"2026-06-01 15:00:00","2026-06-01 16:00:00",3.9),
    (7,"U6","R3","Chennai",400,"2026-06-01 16:00:00","2026-06-01 17:10:00",4.6),
    (8,"U7","R5","Bangalore",600,"2026-06-01 17:00:00","2026-06-01 17:20:00",4.9)
]

 

# -------------------------------
# Step 2: Define schema (columns)
# -------------------------------

 schema = "order_id INT, user_id STRING, restaurant_id STRING, city STRING, order_amount INT, order_time TIMESTAMP, delivery_time TIMESTAMP, rating DOUBLE" 

schema = StructType([StructField("order_id", INTEGER),
StructField("user_id", STRING),
StructField("restaurant_id", STRING),
StructField("city", STRING),
StructField("order_amount",INTEGER),
StructField("order_time", TIMESTAMP),
StructField("delivery_time", TIMESTAMP),
StructField("rating",DOUBLE)])




# -------------------------------
# Step 3: Create DataFrame
# -------------------------------
df = spark.createDataframe(data,schema)

df_1 = df.groupBy(col('User_Id")).agg(count(col("order_id")).alias("Total_oders_per_user")
df_2 = df.select(col("user_id")).filter(max(col("order_amount")))

df_3 = df.select(col("restaurant_id")).filter(max(col("rating")))

df_t = df.withColumn("time_diff", datediff(col("delivery_time"),col("order_time")))
df_4 = df.filter(max(col("time_diff")), min(col("time_diff"))



 

#Get  
#Total Orders Per User
#Highest Spending User
#Highest Rated Restaurant
#Fastest Delivery and Slowest Delivery


link - https://codeinterview.io/
