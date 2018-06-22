#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 11:46:02 2018

@author: hm1584
"""

class Account:
    
    def __init__(self,deposit,withdrawcash):
        self.deposit = deposit
        self.withdrawcash = withdrawcash
        self.newaccount = 100
    
    
    def open_account(self):
        print("You account is opened with a new account baolance %d" %self.newaccount)
           
    def deposit_money(self):
        print("Your depositing money")
        
    def withdraw_money(self):
        print("You withdraw amount would be ")        
    
    def view_balances(self):
        print("Your available balance would be")

customer1 = Account("20", "30")
customer1.open_account()
customer1.deposit_money()
print(customer1.deposit)
customer1.newaccount = 120
customer1.view_balances()
print(customer1.newaccount)
customer1.withdraw_money()
print(customer1.withdrawcash)
customer1.view_balances()
customer1.newaccount = 90
print(customer1.newaccount)
