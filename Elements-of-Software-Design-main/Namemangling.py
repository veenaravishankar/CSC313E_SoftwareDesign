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
a = MyA()
b = MyB()
print(a._variable1, b._variable1)

#print(a.__variable2) # gives you error!

print(a.getvariable2(), b.getvariable2())

#print(b.getvariable2_B())# gives you error!
