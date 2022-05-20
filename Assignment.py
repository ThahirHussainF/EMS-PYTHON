
#Problem - 1

waterLevel=int(input("Enter the water level: "))

if waterLevel > 80:
    print("Turn off motor")
elif waterLevel >=20 and waterLevel <=80:
    print("Motor was idle state")
elif waterLevel<20:
    print("Turn on the motor")


#Problem - 2
"""
while True:
    password =int(input("Enter the password: "))
    if password==1234:
        fanStatus=int(input("Enter the fan status(1-turn on/0-turn off): "))
        if fanStatus==1:
            print("Turn the fan")
            break
        elif fanStatus==0:
            print("Turn off the fan")
            break
        else:
            print("You entered wrong choice")
            break
    else:
         print("You entered wrong password!.Try again")

"""

#Problem - 3

"""
count=0

for number in range(100,1,-1):
    if(number%3==0):
        print(number,end="\t")
        count+=1

print("\nCount of numbers which is divisible by 3: ",count)

"""

#Problem - 4

"""
def isEven(number):
    isEven=True
    
    for number in range(1,number+1):
        if isEven==True:
           isEven=False
        else:
            isEven=True
    return isEven        
             
            
evenNumber=[]
oddNumber=[]
for number in range(1,20):
    if(isEven(number)):
        evenNumber.append(number)
    else:
        oddNumber.append(number)


print(evenNumber)
print(oddNumber)

"""
#Problem - 5


      

            
    


    
