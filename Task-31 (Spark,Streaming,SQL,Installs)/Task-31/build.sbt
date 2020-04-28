name := "Task-31"

version := "0.1"

scalaVersion := "2.11.8"



// https://mvnrepository.com/artifact/org.apache.spark/spark-core
libraryDependencies += "org.apache.spark" %% "spark-core" % "2.4.5"
// https://mvnrepository.com/artifact/org.apache.kafka/kafka
libraryDependencies += "org.apache.kafka" %% "kafka" % "2.3.1"
libraryDependencies += "org.apache.spark" %% "spark-sql"  % "2.4.4"

libraryDependencies += "org.apache.spark" %% "spark-streaming" % "2.4.4"
libraryDependencies += "org.apache.spark" %% "spark-streaming-kafka" % "1.6.2"
libraryDependencies += "org.apache.spark" %% "spark-sql-kafka-0-10" % "2.4.4"
// https://mvnrepository.com/artifact/org.apache.spark/spark-streaming-kafka-0-10
libraryDependencies += "org.apache.spark" %% "spark-streaming-kafka-0-10" % "2.4.5"

libraryDependencies += "org.apache.spark" % "spark-streaming_2.11" % "2.2.0"