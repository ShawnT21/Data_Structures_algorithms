class Employee(object):
    numEmployee=0
    def __init__(self,name,rate):
        self.owed =0
        self.name=name
        self.rate=rate
        Employee.numEmployee += 1

    def de1 (self):
        Employee.numEmployee-=1

    def hours (self,numHours):
        self.owed += numHours*self.rate
        return ("%.2f hours worked" % numHours)

    def pay(self):
        self.owed=0
        return("payed %s" % self.name)


emp1=Employee("Jill", 18.50)

emp2=Employee("Jack", 15.50)

Employee.numEmployee

emp1.hours(20)

emp1.owed

emp1.pay()

class specialEmployee(Employee):
     def_init_(self,name,rate,bonus)
        Employee.__init__(self,name,rate)   #calls the base classes
        self.bonus=bonus


     def__hours__(self,numHours):
       self.owed += numHours*self.rate*2
       return("%.2f hours worked" % numHours)

#Example issubclass() to check wheter a class is a subclass of another class
#Example isinstance() to check if an object belongs to a class or not

print(issubclass(specialEmployee,Employee))
print(issubclass(Employee, specialEmployee))

d = Employee("packt", 20, 100)
b = Employee("packt", 20)
print(isinstance(b, specialEmployee))
print(isinstance(b, Employee))

#Special objects
class My_Class():
  def __init__(self,greet):
      self.greet=greet

  def __repr__(self):
     return 'a custom object (%r) ' % (self.greet)

a= My_Class('giday')

a
