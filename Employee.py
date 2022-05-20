
import datetime
import EMS.Organization as P
class Employee(P.Organization):
    eid=1
    def __init__(self,*empDetails):
        self.__employeeID="ASPIRE"+str(datetime.datetime.now().year)+str(Employee.eid)
        Employee.eid=Employee.eid+1;
        self.__employeeName=empDetails[0]
        self.__emailId=empDetails[1]
        self.__phoneNumber=empDetails[2]
        self.__password=empDetails[3]

    def getEmployeeId(self):
        return self.__employeeID

    def getEmployeeName(self):
        return self.__employeeName

    def getEmailId(self):
        return self.__emailId

    def getPhoneNumber(self):
        return self.__phoneNumber

    def getPassword(self):
        return self.__password

    def showDetails(self):
        print("Employee Id: "+self.__employeeID)
        print("Employee Name: "+self.__employeeName)
        print("Employee Email Id: "+self.__emailId)
        print("Employee Phone Number: "+self.__phoneNumber)
        print("Organization name: ",P.Organization.companyName)
        print("Organization Location: ",P.Organization.location)

