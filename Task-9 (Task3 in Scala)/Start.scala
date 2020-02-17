import scala.collection.mutable.ListBuffer

object Start {
/*
This program will Create a list with 30 random numbers.
Will create a method that returns name and id of object.
Find the smallest missing pos integer
Remove duplicates
 */

  def main(args: Array[String]): Unit = {
//  Creates the random numbers between
    val myList = new ListBuffer[Int]()
    val start = 0
    val end = 30
    val randomNumber = scala.util.Random
    for (x <- 0 to 29 ){
      myList.append(start + randomNumber.nextInt((end -start)+1))
    }
    println("The length of this list is: %s".format(myList.length))
    println("The values insdie the list are: ",myList)

//  Create person object and return name and id
    val person = new Person("Cliford":String,27: Int)
    println(person.getNameGetID())
//  Find the smallest missing pos int
    val missingNumList = new ListBuffer[Int]()
    for(x <-0 to 10 ){
      missingNumList.append(x)
    }
    missingNumList.remove(5)
    var counter = 0
    var missingNum = -1
    for (x <- 0 to missingNumList.length){
      if (missingNumList.indexOf(counter) >= 0){
        counter += 1
      }
      else{
        missingNum = counter
        counter += 1
      }
    }
    if (missingNum == -1){
      missingNum = missingNumList.last + 1
    }
    println("The missing number is: %s".format(missingNum))
    println("The list of numbers: %s".format(missingNumList))
//Remove duplicates strings in a list
    var weekDays = List("sun","mon","tue", "sun","mon","tue","wed","thu","fri","wed","thu","fri","sat")
    var rmDuplicates = new ListBuffer[String]()

    for (x <- 0 to weekDays.length-1){
      if (rmDuplicates.contains(weekDays(x))){
//        println("Already there")
      }else{
        rmDuplicates.append(weekDays(x))
//        println("Adding to the list: %s".format(weekDays(x)))
      }
    }
    println("After removing duplicate items are %s".format(rmDuplicates))
  }

//  def addOne(number: Int): Int ={
//
//    return number+1
//  }
//  def isImportant(size: Int): String = {
//    // Return true if size is greater than or equal to 10.
//    return size.toString
//  }



}
class Person (name:String,id:Int){
  var oName:String = name
  var oId:Int = id

   def getNameGetID(): String ={
    return oName+"\t" +id.toString()
   }

}
