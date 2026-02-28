import sys
from pyspark.sql import SparkSession

def run_spark_job():
    # Create a Spark session
    spark = SparkSession.builder \
        .appName("Desktop Spark Job") \
        .getOrCreate()

    # Sample DataFrame creation
    data = [("Alice", 34), ("Bob", 45), ("Catherine", 29), ("David", 36)]
    columns = ["Name", "Age"]

    # Create DataFrame from the sample data
    df = spark.createDataFrame(data, columns)

    # Show the DataFrame
    df.show()

    # Perform some basic transformations
    df.filter(df.Age > 30).show()

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    run_spark_job()
