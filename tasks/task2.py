#!/usr/bin/env python2
import sys


#naming convention

#camel case: WithdrawCash
#lower camel case: withdrawCash

#iMoney
#sName
#name_list


class Account:
    def __init__(self):
        print("Welcome to BOFA")
        self.accnt_balance = 0
        self.show_menu_and_process_request()

    def show_menu_and_process_request(self):
        choice = input( '''
        1.Open Account
        2.Money Deposit
        3.Money withdrawal
        4.View Balance
        5.Request Loan

        Please enter your choice: ''')
        
        if choice == "1":
            new_account = int(input("Please enter the minimum balance 150 to open your account :"))
            if new_account >= 150:
                krishnas_acnt.open_account()
            else:
                print("No sufficient Your application is declined")
        elif choice == "2":
            self.deposit_money(20)
        elif choice == "3":
            self.withdraw_money(30)
        elif choice == "4":
            self.view_balance()
        elif choice == "5":
            loan = int(input("Please enter the balance in your account :"))
            if loan >= 500:
                print("We considered your application and it will be processed")
            else:
                print("No sufficient funds,  we cannot process your application for Loan")
        else:
            print("Please select the correct choice from above")



    def open_account(self):
        self.accnt_balance += 150 # 10 += 100 is nothing but 100 + 10
        print("your account opened with minimum balance: {}".format(self.accnt_balance))

    def deposit_money(self, money):
        self.accnt_balance += money
        print("successfully deposited moeny")

    def withdraw_money(self, money):
        self.accnt_balance -= money
        print("successfully money withdrawn")

    def view_balance(self):
        print("your accoutn balance is : {}".format(self.accnt_balance))



#krishnas_acnt = Account()


#for loop
#while loop

I = True
'''while I:
    choice = int(input("please enter some number: "))
    if choice != 2:
        print("hello")
    else:
        #break
        I = False'''


''' open account 100
    open account 200
    view balance it should show me 200
    deposit money 4000
    view balance 4200
    withdrw blacne 200
    view balance 4000
    loan loan approved 
    6  Exit 
