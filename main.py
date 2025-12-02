import json
import os
from file_manager import File
from report import Report
from user import UserManager, User
from admin import Admin
from bank_operations import BankAccount

user_manager = UserManager()
bank_manager = BankAccount() 
current_user = None

while True:
    if current_user is None:  
        print("----------------------------------------")
        print("Welcome to Paradise Bank Online")
        print("----------------------------------------")
        print("-----------(1)--> User Login <----------")
        print("-----------(2)--> Register <------------")
        print("-----------(3)--> Produce Password <----")
        print("-----------(4)--> Forgot Password <-----")
        print("-----------(5)--> Support from AI <-----")
        print("----------------------------------------")
        menu_select = input("Select an option: ")
        
        if menu_select == "1":
            user_data = user_manager.login()
            if user_data:
                current_user = User(user_data['id'], user_data['email'], user_data['age'])
                print(f"\n✅ Welcome {user_data['email']}!")
                print(current_user)
        
        elif menu_select == "2":
            user_manager.register()
        
        elif menu_select == "3":
            user_manager.produce_password()
        
        elif menu_select == "4":
            user_manager.forgot_password()
        
        elif menu_select == "5":
            print("AI Support coming soon...")
        
        else:
            print("⚠️ Invalid option!")
    
    else: # Giriş
        print("\n========================================")
        print("Paradise Bank - Banking Services")
        print("========================================")
        print("-----------(1)--> Open Account <-------")
        print("-----------(2)--> Send Money <----------")
        print("-----------(3)--> Payments <------------")
        print("-----------(4)--> Foreign Exchange <----")
        print("-----------(5)--> Savings Tips <--------")
        print("-----------(6)--> Logout <--------------")
        print("========================================")
        banking_select = input("Select an option: ")
        
        if banking_select == "1":
            bank_manager.open_account(current_user.email)
        
        elif banking_select == "2":
            bank_manager.send_money(current_user.email)
        
        elif banking_select == "3":
            bank_manager.payments(current_user.email)
        
        elif banking_select == "4":
            bank_manager.foreign_currency(current_user.email)
        
        elif banking_select == "5":
            bank_manager.savings_tips()
        
        elif banking_select == "6":
            print(f"\n👋 Goodbye {current_user.email}!")
            current_user = None  # Logout
        
        else:
            print("⚠️ Invalid option!")