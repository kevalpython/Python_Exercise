class BankAccount:
    def __init__(self,name,account_number,balance,pin):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.pin = pin

    def __str__(self):
        return f"Account Holder Name: {self.name} \nAccount Number: {self.account_number}\nAccount Number: {self.balance}"

    def check_pin(self,user_pin):
        if user_pin != self.pin:
            return False
        return True
    
    def deposit(self,deposit_amount):
        self.balance+=deposit_amount
        return f"{deposit_amount} rupees are successfully added to your account."
        
    def withdraw(self,withdraw_amount):
        if withdraw_amount<=self.balance:
            self.balance-=withdraw_amount
            return f"{withdraw_amount} rupees has been withdrawn successfully"
        return f"Your account don't have sufficient balance"

b1 = BankAccount(name="Ram",account_number=12345, balance=1000, pin=3456)
flag = True
while flag:
    user_pin=input("Enter your pin : ")
    try:
        if b1.check_pin(int(user_pin)) == True:
            while True:
                print("A. Deposit amount \nB. Withdraw amount \nC. Exit")
                choice=input("Please enter your choice : ")
                try:
                    if choice=="A" or choice=="a":
                        check=True
                        while check:
                            deposit_amount=input("Please enter your deposit amount : ")
                            try:
                                deposit_success=b1.deposit(int(deposit_amount))
                                print(deposit_success)
                                check = False
                            except:
                                print("Please enter correct input")
                    if choice=="B" or choice=="b":
                        check=True
                        while check:
                            withdraw_amount=input("Please enter your withdraw amount : ")
                            try:
                                withdraw_success=b1.withdraw(int(withdraw_amount))
                                print(withdraw_success)
                                check = False
                            except:
                                print("Please enter correct input")
                    if choice=="C" or choice=="c":
                        break
                except:
                    print("Please enter correct choice")
        print("Please enter correct pin")
    except:
        print("Please enter correct input")
        flag = False
    
  