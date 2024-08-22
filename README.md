In this Project , We have one on premise database , Microsoft Sql Server. We have some datasets in this database. Here we are moving all of this data to cloud using tools like Azure Data Factory,Azure Databricks,
Azure Data Lake Gen2.
Azure Data Factory helps to copy all the data from our on premise database to cloud. We are storing it in Azure Data Lake Gen 2 on cloud.
Once the data is moved to Azure Data Lake then we are using Azure Databricks to make the data more cleaner & better. 

Azure Databricks helps us change the raw data into something more useful. It's like polishing raw material into something shiny and valuable.
We have used Lake House Architecture in this project means , We are organizing the data into different layers named bronze,silver,gold.

Bronze layer is the first step where we are storing data same as our on premise database without changing anything. It is like the photo of the data as it is. This is helpful because if something goes wrong later,we
can always come back to this bronze layer and can see how the original Data looks like.

Then while sending the data from bronze layer to silver layer we are using Azure Databricks to make somemeaningful updates in the bronze layer data. These updates involves tasks like renaming columns or adjusting
data types which fit better on the cloud.It is like making minor adjustments to improve data quality.

Finally In Gold layer data we are making more significant changes. This is where the data is in cleanest and most useful form.It's like getting the final polished version of the data ready to be used for important tasks.
