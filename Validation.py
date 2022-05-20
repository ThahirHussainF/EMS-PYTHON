import re
class Validation():
    @classmethod
    def validateDetails(self):
        flag=True
        while flag:
            name = input("Enter your name: ")
            nameFormat = r'\b[A-Za-z\s]+\b'
            if re.fullmatch(nameFormat,name):
                flag=False
            else:
                print("Name is invalid")
        flag = True
        while flag:
            passWord = input("Enter your password: ")
            passwordFormat="^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
            validPassword = re.findall(passwordFormat, passWord)
            if(validPassword):
                flag=False
            else:
                print("password is invalid")

        flag=True
        while flag:
            emailId = input("Enter your emil Id: ")
            emailFormat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if (re.fullmatch(emailFormat, emailId )):
                flag=False
            else:
                print("email id is not valid!!")

        flag=True
        while flag:
            phoneNumber=input("Enter your phone number: ")
            if (len(phoneNumber) == 10 and phoneNumber[0]!= '0'):
                flag=False
            else:
                print("Invalid phone number")
        return name,phoneNumber,passWord,emailId