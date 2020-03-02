package capstonePipeline

import org.apache.log4j.{Level, Logger}
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types.DoubleType
import org.apache.spark.sql.{DataFrame, SQLContext, SaveMode, SparkSession}
import org.apache.spark.{SparkConf, SparkContext}


object apiMain {


  def readJsonFile(str: String,sc:SparkContext,sqlContext: SQLContext) = {
    val weedJSON = sc.wholeTextFiles("neobi_api_weed.json").map(tuple => tuple._2.replace("\n", "").trim)
    val weed_df = sqlContext.read.json(weedJSON)
    weed_df
  }

  def dropColumnDF(weedDF: DataFrame) =  {
    val droppedColumns = weedDF.select("name", "ccc", "type", "thc", "price", "eqWeight", "brand", "producer")
    droppedColumns

  }

  def addProducerColumn(dropCDF: DataFrame) = {

    val withProducer = dropCDF.withColumn("producer_name", col("producer")("name")).withColumn("producer_phone",col("producer")("phone"))
    withProducer
  }

  def removeProduceArrayWeed(weedWithProducer: DataFrame) = {
    val droppedColumn = weedWithProducer.select("name", "ccc", "type", "thc", "price", "eqWeight", "brand", "producer_name","producer_phone")
    droppedColumn
  }

  def fixPrice(sorted_weed: DataFrame) = {
    val fixing = sorted_weed.withColumn("price",regexp_replace(sorted_weed.col("price"), "[!@#$%^&*()]", "").cast(DoubleType))

//    val fixing2 = sorted_weed.withColumn("price_new",col(fixing))

      fixing
  }

  def main(args: Array[String]): Unit = {

    Logger.getLogger("org").setLevel(Level.OFF)
    Logger.getLogger("akka").setLevel(Level.OFF)

    val sparkConf = new SparkConf()
      .set("spark.sql.catalogImplementation","hive")
      .set("spark.sql.warehouse.dir","hdfs://localhost:50501/user/hive/warehouse/")
      .setAppName("My Context")
      .setMaster("local[*]")
    val sc = new SparkContext(sparkConf)
    sc.setLogLevel("OFF")




    val spark = SparkSession
      .builder()
      .enableHiveSupport()
      .getOrCreate()

    val weedDF = readJsonFile("neobi_api_weed.json",sc,spark.sqlContext)

    val dropCDF = dropColumnDF(weedDF)

    val weedWithProducer = addProducerColumn(dropCDF)

    val removedColumnsWeed = removeProduceArrayWeed(weedWithProducer)


    val sortedWeed = fixPrice(removedColumnsWeed)

    val sorted_weed = sortedWeed.orderBy(desc("price"))

    sorted_weed.write.mode(SaveMode.Overwrite).saveAsTable("df_hive")
    spark.sql("describe formatted df_hive")






  }

}
