class Employee:
    raise_amounts = 1.5
    
    def __init__(self, name, hourly_wage, hour_worked):
        self.__name = name
        self.__hourly_wage = hourly_wage
        self.__hour_worked = hour_worked
        
    @property
    def name(self):
        return self.__name

    @property
    def hourly_wage(self):
        return self.__hourly_wage

    @property
    def hour_worked(self):
        return self.__hour_worked

    @name.setter
    def name(self, value):
        self.__name = value

    @hourly_wage.setter
    def hourly_wage(self, value):
        self.__hourly_wage = value

    @hour_worked.setter
    def hour_worked(self, value):
        self.__hour_worked = value


    def gross_pay(self):
        if self.hour_worked > 40 :
            print(self.name +'의 주당 급여는 %d입니다' %(self.hourly_wage * 40 + 1.5 * self.hourly_wage * (self.hour_worked - 40)))
        else:
            print(self.name +'의 주당 급여는 %d입니다' %(self.hourly_wage * self.hour_worked))
            
def main():
    a1 = Employee('이주원', 8250, 42)
    a2 = Employee('김하준', 7600, 48)
    a3 = Employee('박민준', 11000, 32)
    a4 = Employee('이하윤', 8500, 14)
    a5 = Employee('최수아', 9250, 48)
    a6 = Employee('김민서', 50000, 55)
    
    employee_list = [a1, a2, a3, a4, a5, a6]
    
    for employee in employee_list:
        employee.gross_pay()
        
main()