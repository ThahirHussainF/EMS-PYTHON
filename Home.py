import EMS.Validation
import EMS.Employee
class Home:
    employeeRecords={}
    @classmethod
    def home(self):
        while True:
            print("----------------------Welocome to Aspire systems----------------------\n","1.Register\n","2.Login\n","3.Exit")
            choice=int(input("Enter the choice: "))
            if choice==1:
                Home.register()
            elif choice==2:
                Home.login()
            elif choice==3:
                print("Thank you, We will call you back later!")
                break
            else:
               try:
                   raise Exception("Invalid choice!")
               except Exception as exception:
                   print(exception)
    @classmethod
    def login(self):
        empId = input("Enter your employee id: ")
        if empId in Home.employeeRecords.keys():
            password = input("enter your password: ")
            if password in Home.employeeRecords.get(empId).getPassword():
                print("login succeed!!")
            else:
                print("Incorrect password!!")
                Home.login()
        else:
           try:
             raise KeyError("There is no account")
           except KeyError as exception:
               print(exception)
    @classmethod
    def register(self):
        print("----------------------Register----------------------")
        name,emailId,password,phoneNumber="","","",""
        name,phoneNumber,passWord,emailId=EMS.Validation.Validation.validateDetails()
        employee = EMS.Employee.Employee(name,emailId,phoneNumber,passWord)
        Home.employeeRecords[employee.getEmployeeId()]=employee
        employee.showDetails()
        print("You had registered succesfully!")
