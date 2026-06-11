from cli.member import Member
from cli.expense import Expense
from cli.balance import Balance
from cli.settlement import Settlement
m = Member()
e = Expense()
b = Balance()
s = Settlement()

while True:
    print("------- Expense Splitter -------")
    try:
        ch = int(input("\n1. Add member\n2. Add Expense\n3. Balance\n4. Settlement\n5. Exit\nEnter your choice : "))
    except ValueError:
        print("Enter only number.")
        break

    if ch == 1:
        m.service()       

    elif ch == 2:
        e.service_expense()

    elif ch == 3:
        b.service_balance()

    elif ch == 4:
        s.service_settlement()

    elif ch == 5:
        print("Thank you for visiting.")
        break

    else:
        print("\nInvalid option.")