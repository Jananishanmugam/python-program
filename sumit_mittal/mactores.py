Q1:
df1 => col 1, 2 ,3 
df2 => 1,2,3, 4 (100), 5(1*2)    => add column 4 and 5

answer:
df2 = df1.withColumn("col4", lit(100)).withColumn("col5", col("col1") * col("col2"))


Q2:
dataframe column has a struct based defined how would you restruct and make that single column into separate column (say that struct has 50 columns in it, 
I want to destruct and select only 25 columns from that )
col3 => complex struct (100)

list["a","b",...]

struct
{
id int,
name string
...
100
}

tried answering : 
list = []
for i in struct:
if i in list:
df3.withRenameColumn("col3","1")


Q3: map vs shuffle difference?

Q4: What is this function?
array_insert()

how do you check this function in spark documentation 3.5.4


Q5: How do you update the records in a dataframe using spark api or sql query?
1 2 3
key

delete table_name
where key = ""

Insert into table_name


Q6: Improve the performance of long running query?
long running -> performing (5)  

Q7: Optimization in RDS, Redshift, S3?

Q8: how to copy from S3 to Redshift vs snowflake?



