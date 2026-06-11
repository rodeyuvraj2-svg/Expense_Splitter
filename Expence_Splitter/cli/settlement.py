from services.settlement import settlement

class Settlement(settlement):
    def service_settlement(self):
        while True:
            try:
                c = int(input("\n1. Pay dept\n2. See dept\n3. Exit\nEnter your choice : "))
            except ValueError:
                print("Enter only numbers.")

            if c == 1:
                self.pay_dept()
            elif c == 2:
                self.show_dept()
            elif c == 3:
                break
            else:
                print("Invalid choice.")