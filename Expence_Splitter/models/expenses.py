class Expense:
    def __init__(self,name,amount,paidby,split):
        self.name = name
        self.amount = amount
        self.paidby = paidby
        self.split = split
        self.split_amount = []

    def struct(self):
        return{
            "name" : self.name,
            "amount" : self.amount,
            "paidby" : self.paidby,
            "split" : self.split,
            "split_amount" : self.split_amount
        }