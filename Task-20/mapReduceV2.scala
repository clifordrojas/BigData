import java.io.{BufferedWriter, FileWriter}

import scala.collection.mutable
import scala.collection.mutable._
import scala.io.{BufferedSource, Source}
import scala.util.control.Breaks
import sys.process
import scala.sys.process.{Process, ProcessBuilder}
object Task4Scala2Python {
  def stripAll(s: String, bad: String): String = {

    @scala.annotation.tailrec def start(n: Int): String =
      if (n == s.length) ""
      else if (bad.indexOf(s.charAt(n)) < 0) end(n, s.length)
      else start(1 + n)

    @scala.annotation.tailrec def end(a: Int, n: Int): String =
      if (n <= a) s.substring(a, n)
      else if (bad.indexOf(s.charAt(n - 1)) < 0) s.substring(a, n)
      else end(a, n - 1)

    start(0)
  }
    def mapper(bufferedSource:BufferedSource): ListBuffer[(String,Int)] ={
    val tupleList:ListBuffer[(String,Int)] = ListBuffer()

    for (line <- bufferedSource.getLines) {
      val lineArr = line.split(" +")
      for (words <- lineArr) {
        val hello = (stripAll(words, ",?.!@#$%^&*()_+".toLowerCase()), 1)
        tupleList.addOne(hello)
      }
    }
    tupleList
  }
    def reducer(tupleList:ListBuffer[(String,Int)]): mutable.Map[String,Int]={
      val map = mutable.Map[String,Int]()
      val addOne = 1
      for (tuple <- tupleList){
        if (map.contains(tuple._1)){
          map(tuple._1) += 1
        }else{
          map.addOne(tuple)
        }
      }
    map
    }



  def main(args: Array[String]): Unit = {

    val bufferedSource = Source.fromFile("shakeSpear.txt")
    val tupleList = mapper(bufferedSource)
    val reduced = reducer(tupleList)

    val outputFile = new BufferedWriter(new FileWriter("shakeSpear.csv"))

    outputFile.write("Word , Count \n")

    for (word <- reduced) {
      outputFile.write("%s,%s\n".format(word._1,word._2))
      println("%s\t%s\n".format(word._1,word._2))
    }

    outputFile.close()
    println(reduced)
        "hadoop fs -copyFromLocal shakeSpear.csv /data" !

  }


}
