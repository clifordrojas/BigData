import com.esotericsoftware.minlog.Log.Logger
import org.apache.spark.rdd.RDD
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.sql.{DataFrame, Dataset, ForeachWriter, Row, SQLContext, SparkSession}
import org.apache.log4j.{Level, Logger}

object SparkStreaming {

  def main(args: Array[String]): Unit = {

    val spark = SparkSession
      .builder()
      .appName("dataframe")
      .master("local")
      .getOrCreate()

    import spark.implicits._

    // Create DataFrame representing the stream of input lines from connection to localhost:9999
    val lines = spark.readStream
      .format("socket")
      .option("host", "localhost")
      .option("port", 9999)
      .load()

    // Split the lines into words
    val words = lines.as[String].flatMap(_.split(" "))

    // Generate running word count
    val wordCounts = words.groupBy("value").count()

    val query = wordCounts.writeStream
      .outputMode("complete")
      .format("console")
      .start()

    query.awaitTermination()



  }

}
