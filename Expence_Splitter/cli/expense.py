from services.expense import expense

class Expense(expense):
    def service_expense(self):
        while True:
            try:
                c = int(input("\n1. Add Expense\n2. Show Expense\n3. Delete Expense\n4. Exit\nEnter your choice : "))
            except ValueError:
                print("Enter only numbers.")

            if c == 1:
                self.add_expense()
            elif c == 2:
                self.show_expense()
            elif c == 3:
                self.delete_expense()
            elif c == 4:
                break
            else:
                print("Invalid choice.")