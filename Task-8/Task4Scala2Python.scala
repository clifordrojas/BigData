import java.io.{BufferedWriter, FileWriter}

import scala.io.Source
import scala.util.control.Breaks

object Task4Scala2Python {
  def main(args: Array[String]): Unit = {
    var dict: Map[String, Int] = Map()

    val bufferedSource = Source.fromFile("shakeSpear.txt")
    for (line <- bufferedSource.getLines) {
      var lineArr = line.split(" +")
      for (words <- 0 to lineArr.length - 1) {
        dict += (stripAll(lineArr(words), ",?.!@#$%^&*()_+").toLowerCase() -> 1)
      }
    }
    var mDict = collection.mutable.Map(dict.toSeq: _*)
    val bufferedSource2 = Source.fromFile("shakeSpear.txt")
    for (line <- bufferedSource2.getLines) {
      var lineArr2 = line.split(" +")
      for (words <- 0 to lineArr2.length - 1) {
        mDict(stripAll(lineArr2(words), ",?.!@#$%^&*()_+").toLowerCase()) += 1
      }
      //      println((0).toString)
    }
    println(dict)
    println(mDict)
    val outputFile = new BufferedWriter(new FileWriter("shakeSpear.csv"))
    outputFile.write("Word , Count \n")

    for (word <- mDict) {
      outputFile.write("%s,%s\n".format(word._1,word._2))

      println("%s\t%s\n".format(word._1,word._2))
    }
  }

    //


//    Breaks.break()
//    bufferedSource.close

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

}
