#!/usr/bin/env python

#!/usr/bin/env python2
import sys,os
#os.system('cls' if os.name == 'nt' else 'clear')


class Account:
    def __init__(self):
        print("Welcome to BOFA")
        self.accnt_balance = 0
        self.option_six = ["6",  "Q", "q",  "quit", "Quit"]
        self.show_menu_and_process_request()

    def show_menu_and_process_request(self):
        while True:
            choice = input( '''
            1.Open Account
            2.Money Deposit
            3.Money withdrawal
            4.View Balance
            5.Request Loan
            6.Quit (q)

            Please enter your choice: ''')
            if choice == "1":
                new_account = int(input("Please enter the minimum balance 150 to open your account :"))
                if new_account >= 150:
                    self.accnt_balance = new_account
                    self.open_account()
                else:
                    print("Minimum Balance ($150) required to open an account,  Your application cannot be processed")
            elif choice == "2":
                money = int(input("Please enter the amount you would like to deposit:"))
                self.deposit_money(money)
            elif choice == "3":
                money = int(input("Please enter the amount you would like to withdraw from account:"))
                if self.accnt_balance >= money:
                    self.withdraw_money(money)
                else:
                    print("Your Account doesnt have sufficient Balance")
            elif choice == "4":
                self.view_balance()
            elif choice == "5":
                if self.accnt_balance >= 500:
                    print("We considered your Loan application and it will be processed")
                else:
                    print("No sufficient funds,  we cannot process your application for Loan")
            elif choice in self.option_six:
                break
            else:
                print("Sorry, You have made a wrong choice")


    def open_account(self):
        print("your account opened with minimum balance: {}".format(self.accnt_balance))

    def deposit_money(self, money):
        self.accnt_balance += money
        print("successfully deposited moeny")

    def withdraw_money(self, money):
        self.accnt_balance -= money
        print("successfully money withdrawn")

    def view_balance(self):
        print("your accoutn balance is : {}".format(self.accnt_balance))
    

krishnas_acnt = Account()




# Balance Validation 

#Clear menu option -- > 

#Value ( Any value) - come back to menu 

#Account opening  --> Do you want to overdraft ( deduct 12 balance) 
#         --> No options slected, overdraft not avaialble 

# Account opening - Another menu opton -- show transcations ( Option 8 or 9 or somethign) - date


#eg: 26062108: opend account with 30
