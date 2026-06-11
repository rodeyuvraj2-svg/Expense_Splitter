from services.balance import balance

class Balance(balance):
    def service_balance(self):
        while True:
            try:
                c = int(input("\n1. Show balance (who owes who)\n2. Exit\nEnter your choice : "))
            except ValueError:
                print("Enter only numbers.")

            if c == 1:
                self.show_balance()
            elif c == 2:
                break
            else:
                print("Invalid choice.")