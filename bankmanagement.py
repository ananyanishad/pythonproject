import pymysql as db

while True:
    print('''Chose the operation to perfrom
    1.Open Account
    2.Deposit Amount
    3.Withdraw Amount
    4.Balance Enquiry
    5.Display Customer Details
    6.Close An Account
    ''')
    choice = int(input("Enter Task No: "))

    if choice==6:
        break
    elif choice==1:
        name = (input("Enter Name:"))
        account = input("Enter Account Number:")
        DOB = input("Enter Date of Birth:")
        address = input("Enter Address:")
        openbalance = int(input("Enter Opening Balance:"))
        feedback = (name,account,DOB,address,openbalance)
        print(feedback)
        print("Account created successfully")
    elif choice==2:
        amount = int(input("Enter Amount:"))
        account = input("Enter Account No:")
        feedback = (amount,account)
        print(feedback)
        print("Deposit Successful")
    elif choice==3:
        amount = input("Enter Amount:")
        account = input("Enter Account No:")
        feedback = (amount,account)
        print(feedback)
    elif choice==4:
        account = input("Enter Account No: ")
        data = (account)
        print("Balance for Account:",account,"is")
        print("Balance Enquary Sucessfully`")
    elif choice==5:
        account = input("Enter Account No:")
        data = (account)
        print(data)

