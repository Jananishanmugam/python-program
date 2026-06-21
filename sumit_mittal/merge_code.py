Q2: You're building a refined layer in your data lake using Apache Spark and Delta
Lake, where you need to maintain a historized view of customer records (e.g., current
active address) from an incremental stream of changes (inserts, updates, and
occasional deletes) originating from a CDC system. How would you implement this
efficiently and reliably, specifically handling updates and deletes?
Difficulty: Advanced
For handling inserts, updates, and deletes (CDC) in a refined layer using Delta Lake, the `MERGE
INTO` operation is the most robust and efficient solution. It allows for UPSERT (update or insert)
and DELETE operations based on a join condition.
1. **Source Data Format:** Ensure the incoming CDC data includes an operation type (e.g., 'I' for
insert, 'U' for update, 'D' for delete) and a primary key to identify records.
2. **Delta Lake Table:** The target table in Delta Lake should be partitioned appropriately (e.g., by
`customer_id` hash or `ingestion_date` if suitable) and ideally ordered/Z-ordered by the primary
key for better merge performance.
3. **Merge Logic:** Use `MERGE INTO` to apply changes from the incoming micro-batch to the
target Delta table.
* **WHEN MATCHED AND operation_type = 'U'**: UPDATE the existing row with new values.
* **WHEN MATCHED AND operation_type = 'D'**: DELETE the existing row.
* **WHEN NOT MATCHED AND operation_type = 'I'**: INSERT the new row.
This approach ensures atomicity (all changes in a batch succeed or fail together) and handles
schema evolution gracefully with Delta Lake's features.
Code Example:
```python
from pyspark.sql.functions import col
from delta.tables import DeltaTable
# Assume 'updates_df' is your DataFrame from the CDC stream
# It has columns: id, name, address, last_updated_at, operation_type ('I', 'U', 'D')
# Load the target Delta Lake table
delta_table_path = "s3://your-bucket/data/refined/customers"
deltaTable = DeltaTable.forPath(spark, delta_table_path)
# Perform the merge operation


deltaTable.alias("target") \
.merge(
source=updates_df.alias("source"),
condition=col("target.id") == col("source.id")
) \
.whenMatchedAnd(col("source.operation_type") == "U") \
.updateAll() \
.whenMatchedAnd(col("source.operation_type") == "D") \
.delete() \
.whenNotMatchedAnd(col("source.operation_type") == "I") \
.insertAll() \
.execute()
# Optional: Optimize the Delta table after merge
deltaTable.optimize().execute_compaction()
```



■ Real-World: Maintaining a near real-time customer master data set in a data lake, where customer
information (addresses, contact details) frequently changes in the source CRM system. Analysts need
the most up-to-date view for segmentation and personalization, and historical tracking might be needed
for audit trails or time-series analysis.
