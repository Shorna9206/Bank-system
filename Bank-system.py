print("Welcome to our Bank")
amount=0;
deposit=0;
withdraw=0;
def account_holder():
    print("")
    print("Account Number : 171-15-9206")
    print("Account Name   : Rokeya Khatun Shorna")
    print("Balence        :",amount)
    print("Deposit        :",deposit)
    print("Withdraw       :",withdraw)
    print("")
account_holder()
i=6
while i!=0:
    print("")
    print("To Deposite      : Press 1")
    print("To Withdraw      : Press 2")
    print("To Check Amount  : Press 3")
    print("To Exit          : Press 0")
    print("")
    check =input("Enter Your Activity : ")
    condition=int(check)
    if(condition==1):
        depositAmount=input("Enter Deposit Amount : ")
        deposit=deposit+float(depositAmount)
        amount=amount+float(depositAmount)
        print("Deposit Successfull")

    elif(condition==2):
        if(amount>0):
            withdrawAmount=input("Enter Withdraw Amount : ")
            withdrawAmounts=float(withdrawAmount);
            if(withdrawAmounts<amount):
                withdraw=withdraw+withdrawAmounts
                amount = amount-withdraw
                print("Withdraw Successfull")
            else:
                print("")
                print("Balance is not sufficient")
                print("")
        else:
            print("")
            print("Balance is not sufficient")
            print("")
    elif(condition==3):
        account_holder()

    elif(condition==0):
        i=0
        break
    else:
        print("")
        print("Please Enter the Correct Number")
        print("")
print("")
print("Thank You for being with Us...")