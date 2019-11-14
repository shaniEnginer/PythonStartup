#  To Mark A Class abstract ABC class in PYthon 
from abc import ABC , abstractmethod

class PayrollSystem:
    def calculate_payroll(self , employees):
        for employe in employees:
            print(' calculating Payroll ')
            print('======================')
            print(f'Payroll for {employe.id}-{employe.name}')
            print(f'Amount  {employe.calculate_payroll()}')
            print(' ')


class Employ(ABC):
    def __init__(self, id ,name):
        self.id=id;
        self.name=name;


class SalaryEmploye(Employ):
    def __init__(self, id, name , weekly_salary):
        super().__init__(id, name)
        self.weekly_salary=weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employ):
    def __init__(self , id , name , hours_work, hours_rate):
        super().__init__(id, name)
        self.hours_rate=hours_rate
        self.hours_work=hours_work


    def calculate_payroll(self):
        return self.hours_rate*self.hours_work



class CommissionEmployee(SalaryEmploye):
    def __init__(self , id , name , weekly_salary, commission):
        super().__init__(id ,name ,weekly_salary)
        self.commission=commission

    def calculate_payroll(self):

        fixed=super().calculate_payroll()
        return fixed+self.commission


