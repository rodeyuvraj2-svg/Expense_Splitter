import json

class member:
    def __init__(self):
            self.members = {}
            self.load_members()


    def add_member(self):
        try:
            number = int(input("\nEnter number of people: "))
        except ValueError:
                print("Please enter a valid number.")
                return

        for i in range(number):
            p = input(f"Enter name of person {i+1} : ")
            next_id = max(self.members.keys(), default=0) + 1
            self.members[next_id] = p
            print("Person added:", self.members[next_id])

        self.save_data()


    def show_member(self):
        if not self.members:
            print("\nNo members.")
            return

        print("\nAll members:")
        for i, j in self.members.items():
            print(i, " ", j)


    def delete_member(self):
        self.show_member()
        try:
            ch = int(input("Enter the number of person to kick out: "))
        except ValueError:
            print("Please enter a valid number.")
            return

        if ch in self.members:
            name = self.members.pop(ch)
            print(f"{name} is kicked out.")
            self.save_data()
        else:
            print("Failed to delete member.")


    def save_data(self):
        member = []
        for i in self.members.values():
            member.append(i)
        
        with open("storage/member.json", "w") as file:
            json.dump(member, file, indent=4)


    def load_members(self):
        with open("storage/member.json", "r") as file:
            data = json.load(file)
            for i in data:
                next_id = max(self.members, default = 0) + 1
                self.members[next_id] = i