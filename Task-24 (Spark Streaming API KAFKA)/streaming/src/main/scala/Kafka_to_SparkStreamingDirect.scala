
import org.apache.kafka.common.serialization.StringDeserializer
import org.apache.spark.streaming.kafka010._
import org.apache.kafka.common.serialization.StringDeserializer
import org.apache.spark.streaming.kafka010.LocationStrategies.PreferConsistent
import org.apache.spark.streaming.kafka010.ConsumerStrategies.Subscribe
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.streaming.{Seconds, StreamingContext}
import org.apache.kafka.clients.consumer.ConsumerRecord
import kafka.serializer.StringDecoder
import kafka.serializer.DefaultDecoder
import org.apache.commons.codec.StringDecoder

object Kafka_to_SparkStreamingDirect {
  def main(args: Array[String]): Unit = {

    val conf = new SparkConf().setMaster("local[2]").setAppName("kafka")

    val ssc = new StreamingContext(conf, Seconds(10))

    val kafkaParams = Map[String, Object](
      "bootstrap.servers" -> "localhost:9092",
      "key.deserializer" -> "org.apache.kafka.common.serialization.StringDeserializer",
      "value.deserializer" -> "org.apache.kafka.common.serialization.StringDeserializer",
      "group.id" -> "kgroup",
      "auto.offset.reset" -> "latest"
    )

    val topics = "ChuckNorris".split(" ").map(_.trim).toSet
    val stream = KafkaUtils.createDirectStream[String, String](
      ssc,
      PreferConsistent,
      ConsumerStrategies.Subscribe[String, String](topics, kafkaParams))


    stream.foreachRDD { rdd =>
      rdd.coalesce(1).saveAsTextFile("hdfs://localhost:9000/output/T24_result")
    }
    ssc.start()
    ssc.awaitTermination()
  }
}
