class Employee():
    def __init__(self, name: str, position: str, salary: int):
        self.name = name
        self.position = position
        self.salary = salary
    
    def setName(self, name: str) -> None:
        self.name = name
    
    def setPosition(self, position: str) -> None:
        self.position = position

    def setSalary(self, salary: int) -> None:
        self.salary = salary

    def getName(self) -> str:
        return self.name
    
    def getPosition(self) -> str:
        return self.position
    
    def getSalary(self) -> int:
        return self.salary 

class EmployeePrinter():
    def __init__(self) -> None:
        pass

    def printEmployeeDetails(self, employee: Employee) -> None:
        print(employee.getName())
        print(employee.getPosition())
        print(employee.getSalary())

    def printEmployeeSalary(self, salary: int) -> int:
        print(salary)

class SalaryCalculator():
    def __init__(self) -> None:
        pass

    def calculateAnnualSalary(self, employee: Employee) -> int:
        return employee.getSalary() * 12


if __name__ == "__main__":
    employee = Employee("Jorge Angel Zepeda Navarrete", "Desarrollador de software Jr", salary=1000)

    employeePrinter = EmployeePrinter();
    salaryCalculator = SalaryCalculator();

    employeePrinter.printEmployeeDetails(employee)
    employeePrinter.printEmployeeSalary(salaryCalculator.calculateAnnualSalary(employee))
