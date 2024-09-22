class MyA:
     def __init__(self):
         self._variable1 = "variable1"
         self.__variable2 = "variable2"
     def getvariable1(self):
         return self._variable1
     def getvariable2(self):
         return self.__variable2
 
class MyB(MyA):
     def getvariable1_B(self):
         return self._variable1
     def getvariable2_B(self):
         return self.__variable2

###access variables to understand name mangling!
