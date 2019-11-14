class Test:
      vars=['first' , 'Second' , 'third']
      
      def __init__(self):
            self.test="test in String "
            self.Var="the Var In string"
            self.mytuple = ("apple", "banana", "cherry")
            self.myit = iter(self.mytuple)

            print(next(self.myit))
            print(next(self.myit))
            print(next(self.myit))

      def user(self):
            self.nes_list=[]
            for listing in self.vars:
                  self.nes_list.append(listing)
            print(self.nes_list)



#  creating The Object In Python 
var =Test()
# print(f' the first {var.test} and {var.Var}')
var.user()


# # _ spacified protected in Python
# #  __ spacified private in Python

# class Person:
#     # name
#     # age
#   __age="test"
#   def __init__(self, mname, mage):
#     self.mname = mname
#     self.mage = mage

# p1 = Person("John", 36)

# # print(p1.name)
# print(p1.age)
# # if The age var Was private 
# # print(p1._Person__age)