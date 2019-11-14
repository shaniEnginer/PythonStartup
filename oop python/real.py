#  Defining a class in Python
#  Every Class in Python is inherted by Object Class
# class Test(object):
#     pass



# class ErrorClass:
#     pass


# raise ErrorClass()

#! Traceback (most recent call last):
# !  File "real.py", line 12, in <module>
# !    raise ErrorClass()
#! TypeError: exceptions must derive from BaseException


#  now this class is drived from base Exception class
class ErrorClass(Exception):
    pass


raise ErrorClass()



# class PayrollSystem():
#     def calculate_payroll(self, employe):
#         for empl in employe:
#             print(f' Pay roll for {employe.name}-{employe.id}')
