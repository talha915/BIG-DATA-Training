import findspark
findspark.init()

from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.master("local").appName("example").getOrCreate()

# Create a sample DataFrame
data = [("Alice", 34), ("Bob", 45), ("Cathy", 29), ("Lathy", 99)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Show the DataFrame
df.show()


