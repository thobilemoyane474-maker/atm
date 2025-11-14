class ATM:
    def atm(self):
        self.pin="1234"
        self.balance= 1000
        self.attempts= 0
        self.max_attempts= 3

    def authenticate(self):
        while self.attempts < self.max_attempts:
            pin= input("Enter your PIN:")
            if pin== self.pin:
                print("login successful!")
                return True
            else:
                self.attempts += 1
                print(f"incorect PIN. you have {self.max_attempts - self.attempts}attempts left." ) 
        print("maximum attempts reached.Account locked.")
        return False
    def check_balance(self):
        print(f"your current balance is: ${self.balance}")

    def withdraw_money(self):
        try:
            amount= float(input("Enter the amount to withdraw: $"))
            if amount > self.balance:
                print("insufficient balance,")
            elif amount <= 0:
                print("invalid amount. please enter a positive number")
            else:
                self.balance -= amount
                print(f"withdrawal successful. your new balance is: ${self.balance:.2f}")
        except ValueError:
            print("invalid input. please enter a vlid amount.")

    def run(self):
        if self.authenticate():
            while True:
                print("\nATM Menu:")
                print("1. check balance")
                print("2. withdraw money")
                print("3. deposit money")
                print("4. Exit")
                choice= input("Enter your choice:")
                if choice== "1":
                    self.check_balance() 
                elif choice== "2":
                    self.withdraw_money()
                elif choice=="3":
                    self.deposit_money()
                elif choice=="4":
                    print("Thank you for using our ATM. Goodbye!")
                    return
                else:
                    print("invalid choice. please try again.")

    atm()                                                                      