from models.expenses import Expense
from services.member import member
import json

class expense(member):
    def __init__(self):
        super().__init__()
        self.expense = {}
        self.load_expenses()

    def load_expenses(self):
        self.expense = {}
        with open("storage/expense.json", "r") as file:
            data = json.load(file)
            
            for exx in data:
                ex = Expense(
                    exx["name"],
                    exx["amount"],
                    exx["paidby"],
                    exx["split"]
                )

                ex.split_amount = exx.get("split_amount", [])
                next_id = max(self.expense, default = 0) + 1
                self.expense[next_id] = ex
        
    
    def save_data(self):
        ex = []
        for i in self.expense.values():
            ex.append(i.struct())
        with open("storage/expense.json", "w") as file:
            json.dump(ex, file, indent = 4)


    def add_expense(self):
        split = []
        split_amount = []
        name = input("\nEnter name of the expense : ")
        amount = int(input("Enter amount : "))

        self.show_member()
        py = int(input("Enter the number of person who paid : "))
        for i,j in self.members.items():
            if i == py:
                paidby = j

        for i,j in self.members.items():
            if i != py:
                split.append(j)
        
        avg = amount / (max(self.members) - 1)
        for i in split:
            split_amount.append(avg)
            
        ex = Expense(name, amount, paidby, split)
        ex.split_amount = split_amount
        next_id = max(self.expense, default=0) + 1
        self.expense[next_id] = ex
        self.save_data()
        

    def show_expense(self):
        if not self.expense:
            print("No Expenses.")
            return
        
        else:
            print("\nAll expenses are : ")
            for i,j in self.expense.items():
                print(f"{i}\nName : {j.name}\nAmount : {j.amount}\nPaidby : {j.paidby}\nSplit between : {j.split} ")


    def delete_expense(self):
        self.show_expense()

        delete = int(input("Enter the number of the expense to be deleted : "))
        if delete not in self.expense:
            print("Wrong expense number.")
            return

        expense_item = self.expense[delete]
        pending = False
        for amount in expense_item.split_amount:
            if amount != 0:
                pending = True
                break

        if pending:
            print("Debt is pending.")
            return

        self.expense.pop(delete)
        print("Expense deleted.")
        self.save_data()