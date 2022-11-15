class Employee:
    emp_id_start = 10
   
    def __init__(self,name, salary, address, department="", subjects=[]):
        self.emp_id = self.emp_id_start
        Employee.emp_id_start += 1
        self.name = name
        self.salary = salary
        self.address = address
        self.department = department
        self.subjects = subjects
        
        print(key, val, sep=" : ")

    def display(self):
        print("Name: ", self.name)
        print("EMP ID: ", self.emp_id)
        print("Salary: ", self.salary)
        print("Address: ", self.address)
        print("Department: ", self.department)
        print("Subjects: ", self.subjects)
        print()

class Teacher(Employee):
    def __init__(self,name, salary, address, department, subjects):
        self.department = department
        self.subjects = subjects
        super().__init__(name, salary, address, department, subjects)



emp = Employee("Aksa", 4500, "Trivandrum")
teacher = Teacher("Nelwin", 7000, "Trivandrum", "MCA", ["Python", "S.E"])

emp.display()
teacher.display() #
