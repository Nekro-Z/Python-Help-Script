import os
import time
import random

while True:
    os.system("clear")
    print("Welcome to Terminal Helper\nVersion 1.00")
    menu = input("Select what do you want to do:\n1.Power controls     2.File control     3.Games       4.Calculator     5.Useless functions\nOption: ")
    if menu == "1":
        power_menu = input("Select your option:\n1.Reboot     2.Shut down     3.Suspend\nOption: ")
    elif menu == "2":
        file_menu = input("Select your option:\n1.Update system     2.Sudo without password\nOption: ")
        if file_menu == "1":
            print("Hi")
        elif file_menu == "2":
            print("remove # before the statement at the end containing NOPASSWD ALL")
            time.sleep(10)
            os.system("sudo visudo")
    elif menu == "3":
        game_menu = input("Select your option;\n1.smth\nOption: ")
    elif menu == "4":
        calculator_menu = input("Select what do you want to do:\n1.Calculator\n2.Generate numbers till ...\n3.Random number generator")
        if calculator_menu == "1":
            number_1 = input("Select first number: ")
            number_2 = input("Select second number: ")
            while True:
                calculator_sign = input("Enter sign of operation or write help")
                if calculator_sign.lower() in ["help", "h", "he", "hel"]:
                    print("Use + for addition\n- for subtruction\n/ for division\n* for multiplication\n** for power")
                    time.sleep(5)
                    continue
        elif calculator_menu == "2":
            print("Smth")
        elif calculator_menu == "3":
            print("😘️")
    elif menu == "5":
        useless_menu = input("Select what do you want to do:\n1.Linux shortcuts")
        if useless_menu == "1":
            print("Linux shortcuts:\nctrl + ; for emoji menu")
    else:
        print("Wrong input")
    restart = input("Do you want to exit: ")
    if restart.lower() in ["y", "ye", "yes", "yep"]:
        break
    else:
        continue