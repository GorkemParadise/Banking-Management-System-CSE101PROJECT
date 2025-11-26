import json
import os
from file_manager import File
from report import Report
from user import UserManager, User
from admin import Admin
from bank_operations import Bank

user_manager = UserManager()
current_user = None

while True:
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
    
    elif menu_select == "2":
        user_manager.register()
    
    elif menu_select == "3":
        user_manager.produce_password()
    
    elif menu_select == "4":
        user_manager.forgot_password()
    
    elif menu_select == "5":
        print("AI Support coming soon...")
    
    else:
        print("Invalid option!")
