import com.esotericsoftware.minlog.Log.Logger
import org.apache.spark.rdd.RDD
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.sql.{DataFrame, Dataset, ForeachWriter, Row, SQLContext, SparkSession}
import org.apache.log4j.{Level, Logger}
object Task31 {
import org.apache.spark



  def main(args: Array[String]): Unit = {

//  val spark = SparkSession
//    .builder()
//    .appName("dataframe")
//    .master("local")
//    .getOrCreate()

    val conf = new SparkConf().setAppName("rdd").setMaster("local")
    val sc  = new SparkContext(conf)
    val sqlContext = new SQLContext(sc)
    val spark = sqlContext.sparkSession
    sc.setLogLevel("OFF")

    sc.setCheckpointDir("/home/desktop/Desktop/RddCP")

    // For implicit conversions like converting RDDs to DataFrames
    import spark.implicits._
    val csv_rdd = sc.textFile("/home/desktop/Desktop/csv_file.csv")

    //Broadcast the large file
    val broacast_var = sc.broadcast(csv_rdd.collect())

    val csv_map = csv_rdd.flatMap(line => line.split(","))
    val csv_map2 = csv_map.map(line => (line(0), line(2)))
    //Cache the RDD to memory
    val csv_partition = csv_map2.repartition(200).cache()
    //Persist the rdd
    val csv_make_small = csv_partition.coalesce(4).persist()

    //Accumulate the finished executors
    val accum = sc.doubleAccumulator



    //Create RDD CheckPoint
    csv_make_small.checkpoint()
    // After usage stop persisting - Avoid unnecessary data usage
    csv_make_small.unpersist()
    //Show RDD Lineage
    println(csv_make_small.toDebugString)

    //Use implicits to create dataframe
    val rdd_toDF = csv_map.toDF()
    rdd_toDF.show(10)
//    val csv_file = spark.read.csv("/home/desktop/Desktop/csv_file.csv")
//    val new_column = csv_file.withColumn("new_id",$"_c0"+1)
//
//    new_column.show(10)






  }



}
