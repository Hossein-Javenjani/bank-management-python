from account import Account
from bank import Bank

bank = Bank()
while True:
    print(
        f"=====Bank Management=====\n1.Create\n2.Deposit\n3.Withdraw\n4.Transfer\n5.Show Account\n6.Search Account\n7.save\n8.load\n9.exit"
    )
    try :
        choosed = int(input("choose : \n"))
    except ValueError :
        choosed = int(input("you must choose a number : "))
    if choosed == 1:
        print(f'{"=" * 10} Create Account {"=" * 10}')
        bank.create()
    elif choosed == 2:
        print(f'{"=" * 10} Deposit {"=" * 10}')
        bank.deposit()
    elif choosed == 3:
        print(f'{"=" * 10} Withdraw {"=" * 10}')
        bank.withdraw()
    elif choosed == 4:
        print(f'{"=" * 10} Transfer {"=" * 10}')
        bank.transfer()
    elif choosed == 5:
        print(f'{"=" * 10} Show Account {"=" * 10}')
        bank.show_account()
    elif choosed == 6:
        print(f'{"=" * 10} Search Account {"=" * 10}')
        bank.search_account()
    elif choosed == 7:
        print(f'{"=" * 10} save Account information {"=" * 10}')
        bank.save()
    elif choosed == 8:
        print(f'{"=" * 10} load Account information {"=" * 10}')
        bank.load()
    elif choosed == 9:
        print("Goodbye!")
        break
    else:
        input("select true option 1_9!")
