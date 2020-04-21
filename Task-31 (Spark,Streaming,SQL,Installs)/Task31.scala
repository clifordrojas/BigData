import com.esotericsoftware.minlog.Log.Logger
import org.apache.spark.rdd.RDD
import org.apache.spark.{SparkConf, SparkContext }
import org.apache.spark.sql.{DataFrame, Dataset, ForeachWriter, Row, SparkSession}

import org.apache.log4j.{Level, Logger}
object Task31 {
import org.apache.spark



  def main(args: Array[String]): Unit = {
//    Logger.getLogger("org").setLevel(Level.OFF)
//  val spark = SparkSession
//    .builder()
//    .appName("dataframe")
//    .master("local")
//    .getOrCreate()

    val conf = new SparkConf().setAppName("rdd").setMaster("local")
    val sc  = new SparkContext(conf)

    // For implicit conversions like converting RDDs to DataFrames
//    import spark.implicits._
    val csv_rdd = sc.textFile("/home/desktop/Desktop/csv_file.csv")
    val csv_map = csv_rdd.flatMap(line => line.split(","))
    val csv_map2 = csv_map.map(line => (line(0), line(2)))
    val csv_partition = csv_map2.repartition(200)
    val csv_make_small = csv_partition.coalesce(4)
    println(csv_make_small.toDebugString)



//    val csv_file = spark.read.csv("/home/desktop/Desktop/csv_file.csv")
//    val new_column = csv_file.withColumn("new_id",$"_c0"+1)
//
//    new_column.show(10)






  }



}
