"""
Q.  Create a class Employee with data members: name, department and salary. Create
    suitable methods for reading and printing employee information.
"""


class Employee:
    def setValue(self):
        self.name = input("Enter Name: ")
        self.department = input("Enter Department: ")
        self.salary = int(input("Enter Salary: "))

    def printValue(self):
        print("----------------------------\nEmployee Information: ")
        print("Name: ", self.name, "\nDepartment: ", self.department, "\nSalary: ", self.salary)


employee = Employee()
employee.setValue()
employee.printValue()
