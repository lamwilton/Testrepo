from pyspark import SparkContext
import sys
print(sys.version)
sc = SparkContext(master="local[*]", appName="task1")
"Version 1.2.5"