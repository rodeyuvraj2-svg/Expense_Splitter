from services.expense import expense
import math

class balance(expense):
    def __init__(self):
        super().__init__()


    def show_balance(self):
        self.load_members()
        self.load_expenses()

        if not self.expense:
            print("No Expenses.")
            return
        
        else:
            print("\nBalance as per Expense : ")
            mem = max(self.members)
            pd = mem - 1
            am = 0
            for i in self.expense.values():
                for j in i.split_amount:
                    am += j

            for i,j in self.expense.items():
                print(f"{i}\nName : {j.name}\nAmount : {j.amount}\nPaidby : {j.paidby}\nSplit between : {j.split} ")
                
                print(f"\n{j.paidby} should recieve {am}")
                l = len(j.split)
                for k in range(l):
                    print(f"{j.split[k]} owes {j.split_amount[k]}")
                print()