

import org.apache.log4j.{Level, Logger}
import org.apache.spark.sql.{DataFrame, Dataset, ForeachWriter, Row, SparkSession}

object Kafka_to_structurestreaming {

  def main(args: Array[String]): Unit = {
    Logger.getLogger("org").setLevel(Level.OFF)
    val spark = SparkSession.builder
        .master("local[2]")
        .appName("kafka1")
        .getOrCreate()

    import spark.implicits._

    //Create DataFrame representing the stream of input lines from connection to localhost:9092
    val lines = spark
      .readStream
      .format("kafka")
      .option("kafka.bootstrap.servers","localhost:9092")
      .option("subscribe","ChuckNorris")
      .load()



    //Split the lines into words
    val words = lines.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
      .as[(String, String)]

//    val words = lines
    //Generate running word count
//    val wordCounts = words.groupBy("value").count()

    words.writeStream
      .option( "path", "structureKafka" )
      .option( "checkpointLocation", "checkpoint" )
      .option( "starting.offsets", "earliest" )
      .queryName( "api" )
      .format( "json")
      .start()
      .awaitTermination()
//    //Start running the query that prints the running counts to the console
//    val query = wordCounts.writeStream
//      .outputMode("complete")
//      .format("console")
//      .start()


//    query.awaitTermination()


  }

}
