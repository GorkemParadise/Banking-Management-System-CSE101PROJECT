from re import S
from file_manager import File
from report import Report
from user import User
from admin import Admin
from bank_operations import Bank

#print("Hello Worlds")

#file_user_data = open("user_data.json")
#contents = file_user_data.read()
#print(contents)

#with open("history.json") as file:
#    history2 = file.read()
#    print (history2)

#with open("history.json", mode="w") as histt5:
#    histt5.write("\nNew text.")

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
    menu_select = input("")