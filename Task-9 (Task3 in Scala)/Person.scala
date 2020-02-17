class Person (name:String,id:Int){
  var oName:String = name
  var oId:Int = id

   def getNameGetID(): String ={
    return oName+"\t" +id.toString()
   }

}
