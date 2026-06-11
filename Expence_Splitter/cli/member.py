from services.member import member

class Member(member):
    def service(self):
        while True:
            try:
                c = int(input("\n1. Add member\n2. Show members\n3. Delete member\n4. Exit\nEnter your choice : "))
            except ValueError:
                print("Enter only numbers.")

            if c == 1:
                self.add_member()
            elif c == 2:
                self.show_member()
            elif c == 3:
                self.delete_member()
            elif c == 4:
                break
            else:
                print("Invalid choice.")