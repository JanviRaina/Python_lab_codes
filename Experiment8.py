# As we know ATM performs multiple operations and those are:
# 1.Account Information
# 2.PIN Change
# 3.Balance Inquiry
# 4.Withdrawal
# 5. Deposit
# Now, What you need to do, You need to create a class of ATM and methods/functions is nothing but your operations that means your code will have 5 methods
# One More important note, as you know if you enter wrong pin for three time it get block , that means you need to write a program in this way if I give wrong pin three times, Your account should get blocked. If you have any doubts, drop a comment or just text me on whats-app.
# Do the same post your link in comment section

# Now, How you will store data/Account information
# store it in terms of dictionary or file as per your convenience.
# 1.If You are using dictionary:
# key will be your name
# value will be your - Acc. No, Mobile No., PIN
# e.g. D={"ABC":5212485411,123454562,4545, "DEF":4559845253,1234567895,8989}

# 2.If you are using files include following:
# Name:
# Account No.
# Mobile NO.
# Address:
# PIN


info={  "A":[123456789,'1234',5400],
        "B":[234567891,'5678',6000],
        "C":[345678912,'9101',8574], 
        "D":[456789123,'1121',6548],
        "E":[567891234,'3141',5469]}


class Atm:
    def __init__(self,name,acc_no,pin,balance):
        self.name=name
        self.acc_no=acc_no
        self.pin=pin
        self.balance=balance
            
    def pin_authentication(self):
        verifypin = input("Enter PIN ")
        flag=True
        c=1
        while(verifypin != self.pin):
            print("Incorrect Pin")
            verifypin = input("Enter PIN again")
            c=c+1
            if(c == 3 and verifypin != self.pin ):
                print("Account Blocked")
                flag=False
                break
        return flag
    
    def account_info(self):
        print("Name ",self.name,"Account No ",self.acc_no,"PIN ",self.pin,"Balance ",self.balance)

    def pin_change(self):
        is_verified=self.pin_authentication()
        if (is_verified):
            new_pin=int(input("Enter new 4-digit pin: "))
            info[self.name][2]= str(new_pin)
            print("PIN changed")
        else:
            print("You entered the wrong pin")
        return is_verified,new_pin
        
    def balance_inquiry(self):
        print( "Account balance is",self.balance)
    
    def withdrawal(self):
        withdrawl_amt=int(input("Enter the amount to be withdrawn "))
        if (withdrawl_amt < self.balance):
            self.balance=self.balance-withdrawl_amt
        else:
            print("Not enough cash")
        
    def deposit(self):
        deposit_amt=int(input("Enter amount you want to deposit"))
        self.balance=self.balance+deposit_amt
        print("Deposition done")

def choice(Atm):
    option=0
    name=input("Enter name ")
    
    person=Atm(name,info[name][0],info[name][1],info[name][2])

    verify=person.pin_authentication()

    if (verify):
        op_dict={1:"Account Information",2:"Pin Change",3:"Balance Inquiry",4:"Withdrawal",5:"Deposit",6:"Exit"}
        while(option != 6):
            for i in op_dict:
                print("{:<3}-{:<20}".format(i,op_dict[i]))
            option=int(input())
            if(option==1):
                person.account_info()
            elif(option==2):
                check,new=person.pin_change()
                if(check==1):
                    break 
                info[name][2]=new
                person=Atm(name,info[name][0],info[name][1],info[name][2])
            elif(option==3):
                person.balance_inquiry()
            elif(option==4):
                person.withdrawal()
            elif(option==5):
                person.deposit()
            elif(option==6):
                break

choice(Atm)
