#bank
total=0
acNo=0
acName="null"
acType="Saving"

def createAccount():
    global acNo,acName,acType
    acNo=int(input("Enter A/C number: "))
    acName=input("Enter custumer name: ")
    acType=input("Saving or Current Accont: ")

def deposite(bal):
    global total
    total=total+bal
    print("Total amount after deposite mony is: ",total)

def withdrow(amount):
    global total
    total=total-amount
    print("Total amount after withdrow mony is: ",total)

def inquiry():
    print("A/C number is: ",acNo)
    print("custumer name is: ",acName)
    print("total balance in this account is: ",total)