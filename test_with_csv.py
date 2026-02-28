import sys
from pyspark.sql import SparkSession

def run_spark_job():

    try:
    # Create a Spark session
        spark = SparkSession.builder \
        .appName("CSV job") \
        .getOrCreate()

    # Path to the CSV file (ensure the path is correct)
        csv_file_path = "file:///home/chanya/Downloads/customers-100.csv"

    # Load the CSV into a DataFrame
        df = spark.read.csv(csv_file_path, header=True, inferSchema=True)

    # Show the first 5 rows of the DataFrame
        df.show(5)

    # Optionally, print the first 5 rows using the head method (returns a list of Row objects)
        print(df.head(5))
    except Exception as e:
        print(f"Error: {e}")
    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    run_spark_job()
