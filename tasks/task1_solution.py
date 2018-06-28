#!/usr/bin/env python


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
      
    def open_account(self):
        self.accnt_balance += 100 # 10 += 100 is nothing but 100 + 10
        print("opening accoutn with minimum balance: {}".format(self.accnt_balance))

    def deposit_money(self, money):
        self.accnt_balance += money
        print("successfully deposited moeny")

    def withdraw_money(self, money):
        self.accnt_balance -= money
        print("successfully money withdrawn")

    def view_balance(self):
        print("your accoutn balance is : {}".format(self.accnt_balance))






krishnas_acnt = Account()
krishnas_acnt.open_account()
krishnas_acnt.deposit_money(20)
krishnas_acnt.view_balance()
krishnas_acnt.withdraw_money(30)
krishnas_acnt.view_balance()
print(type(krishnas_acnt.accnt_balance))

a = "10"
b = 10
print(int(a)+b)
