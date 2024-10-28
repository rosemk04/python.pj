balance_amt=1000
while True:
    print("\n1.\tCheck Balance")
    print("2.\tDeposit Money")
    print("3.\tWithdraw Money")
    print("4.\tExit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print(f"The current balance${balance_amt}")
    elif choice==2:
        deposit_amt=float(input("Enter the amount"))
        balance_amt=balance_amt+deposit_amt
        print(f"The deposited amount${deposit_amt} and " f" The current balance${balance_amt}")
    elif choice==3:
        withdraw_amt=float(input("Enter the amount"))
        balance_amt=balance_amt-withdraw_amt
        print(f"The amount withdrawn from the account${withdraw_amt}and f The balance amount ${balance_amt}")
        if withdraw_amt>balance_amt:
            print("Insufficient Balance")
    elif choice==4:
            break
    else:
        print("Invalid Entry")



