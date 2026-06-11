from services.balance import balance
import json

class settlement(balance):
    def __init__(self):
        super().__init__()
    

    def pay_dept(self):
        self.show_balance()
        num = int(input("Enter the number of the expense : "))
        name = input("Enter the name of the person : ")
        Flag = False
        
        for i,j in self.expense.items():
            if i == num:
                for k in range(len(j.split)):
                    if j.split[k] == name:
                        Flag = True
                        if j.split_amount[k] > 0:
                            print("Your current dept : ",j.split_amount[k])
                            amount = int(input("Enter the amount : "))
                            if j.split_amount[k] >= amount:
                                j.split_amount[k] -= amount
                                print("Amount updated.")
                                print("Your current dept : ",j.split_amount[k])
                                self.save_data()
                                return
                            else:
                                print("Amount is bigger than dept.")
                        else:
                            print("Dept is ZERO.")
                            return
                if not Flag:
                    print("Wrong name of the person.")
            else:
                print("Wrong expense number.")


    def show_dept(self):
        self.show_balance()