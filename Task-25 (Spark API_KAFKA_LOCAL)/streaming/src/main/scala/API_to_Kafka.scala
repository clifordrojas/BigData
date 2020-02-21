import java.util.Properties

import org.apache.log4j.{Level, Logger}
import java.util.Properties

import org.apache.http.client.methods.HttpGet
import org.apache.http.impl.client.DefaultHttpClient
import org.apache.kafka.clients.producer.{KafkaProducer, ProducerRecord}
object API_to_Kafka {

  def message(topic:String, data:String)= {

    new ProducerRecord[String, String](topic, data)
  }

  def getRestContent(url:String): String = {
    val httpClient = new DefaultHttpClient()
    val httpResponse = httpClient.execute(new HttpGet(url))
    val entity = httpResponse.getEntity()
    var content = ""
    if (entity != null) {
      val inputStream = entity.getContent()
      content = scala.io.Source.fromInputStream(inputStream).getLines.mkString

      inputStream.close
    }
    httpClient.getConnectionManager().shutdown()
    return content
  }

  def main(args: Array[String]): Unit = {
      var URL ="https://api.chucknorris.io/jokes/random"
      val apiData = getRestContent(URL)
      println(apiData)


      val topics = "ChuckNorris"
      val api_message = message(topics, apiData)

      val  props = new Properties()
      props.put("bootstrap.servers", "localhost:9092")
      props.put("char.encoder", "utf-8")
      props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer")
      props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer")
  //
      val producer = new KafkaProducer[String, String](props)
      producer.send(api_message)
      producer.flush()
      producer.close()
  }



}
