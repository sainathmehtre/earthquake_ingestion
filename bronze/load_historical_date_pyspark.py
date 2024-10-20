from pyspark.sql import SparkSession
import argparse
import requests

if __name__ == '__main__':

    # Define Spark Session
    spark = SparkSession.builder.appName("Earthquake_Project").master("local[*]").getOrCreate()

    print(spark)