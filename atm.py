Deposit=0
Withdraw=0
balance=100.0
print("   WELCOME TO ATM    ")
pin = int(input("Enter the four digit pin\n"))
if pin == 1234:
    print('WELCOME SIR',"abc")
else:
    print()
    exit()
n = 'Y'
while n == 'Y':
    print('what would you like to do')
    print( '1)Balance\n''2)Withdraw\n''3)Deposit\n''4)Quit\n')
    Option=int(input("Enter Option: "))
    if Option==1:
        if balance+Deposit-Withdraw > 5000:
            print("Balance  ₹",balance+Deposit-Withdraw,'\ni am the richest'.upper())
        else:
            print("Balance  ₹",balance+Deposit-Withdraw)
    if Option==2:
        print("Balance ₹",balance+Deposit-Withdraw)
        Withdraw=float(input("Enter Withdraw amount ₹ "))
        if Withdraw == 0:
            print("None withdraw made")
        elif Withdraw>balance+Deposit:
            print("Withdraw exceeds balance")
        elif Withdraw<balance+Deposit:
            forewardbalance=(balance+Deposit-Withdraw)
            print("Foreward Balance  ₹",forewardbalance)
    if Option==3:
        print("Balance  ₹",balance+Deposit-Withdraw)
        Deposit=float(input("Enter deposit amount ₹"))
        if Deposit>0:
            forewardbalance=(balance+Deposit-Withdraw)
            print("Forewardbalance  ₹",forewardbalance)
        else:
            print("None deposit made")
    if Option==4:
        exit()
    n=input('if you want to continue press Y\n'.upper())
    if n != 'Y':
        break
