from colorama import init, Fore
import os
import sys
import platform
import datetime
system = sys.platform
command = input(Fore.GREEN + system + Fore.BLUE + "> ")
if command == "terminal --help":
    print(Fore.GREEN + "./var: view files in var folder")
    print(Fore.GREEN + "./bin: view files in bin folder")
    print(Fore.GREEN + "./sh: refresh terminal")
    print(Fore.GREEN + "make .c: make c file")
    print(Fore.GREEN + "make .cpp: make cpp file")
    print(Fore.GREEN + "make .py: make python file")
    print(Fore.GREEN + "system: get system name")
    print(Fore.GREEN + "processor: processor data")
    print(Fore.GREEN + "datetime: current date and time")
    print(Fore.GREEN + "ls: view dir")
elif command == "./var":
    print(Fore.RED + "var folder is empty")
elif command == "./bin":
    print(Fore.RED + "bin is empty")
elif command == "./sh":
    print(Fore.GREEN + "Refreshed")
elif command == "make .c":
    namec = input(Fore.GREEN + "Enter File Name:")
    os.system("code " + namec + ".c")

elif command == "make .cpp":
    namecpp = input(Fore.GREEN + "Enter File Name:")
    os.system("code " + namecpp + ".cpp")
elif command == "make .py":
    namepy = input(Fore.GREEN + "Enter File Name:")
    os.system("code " + namepy + ".py")
elif command == "system":
    print(f"{system}")
elif command == "processor":
    print(platform.processr())
elif command == "datetime":
    from datetime import datetime

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")

    print("Current Time:", current_time)
    print("Current Date:", current_date)
elif command == "cls":
    os.system("cls")
elif command == "clear":
    os.system("clear")
elif command == "ls":
    print(Fore.GREEN + "var")
    print(Fore.GREEN + "bin")
else:
    print(Fore.RED + f"{command}: not found")
while command != "end":
    system = sys.platform
    command = input(Fore.GREEN + system + Fore.BLUE + "> ")
    if command == "terminal --help":
        print(Fore.GREEN + "./var: view files in var folder")
        print(Fore.GREEN + "./bin: view files in bin folder")
        print(Fore.GREEN + "./sh: refresh terminal")
        print(Fore.GREEN + "make .c: make c file")
        print(Fore.GREEN + "make .cpp: make cpp file")
        print(Fore.GREEN + "make .py: make python file")
        print(Fore.GREEN + "system: get system name")
        print(Fore.GREEN + "processor: processor data")
        print(Fore.GREEN + "datetime: current date and time")
        print(Fore.GREEN + "ls: view dir")
    elif command == "./var":
        print(Fore.RED + "var folder is empty")
    elif command == "./bin":
        print(Fore.RED + "bin is empty")
    elif command == "./sh":
        print(Fore.GREEN + "Refreshed")
    elif command == "make .c":
        namec = input(Fore.GREEN + "Enter File Name:")
        os.system("code " + namec + ".c")
    elif command == "make .cpp":
        namecpp = input(Fore.GREEN + "Enter File Name:")
        os.system("code " + namecpp + ".cpp")
    elif command == "make .py":
        namepy = input(Fore.GREEN + "Enter File Name:")
        os.system("code " + namepy + ".py")
    elif command == "system":
        print(f"{system}")
    elif command == "processor":
        print(platform.processor())
    elif command == "datetime":
        from datetime import datetime

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%Y-%m-%d")

        print("Current Time:", current_time)
        print("Current Date:", current_date)
    elif command == "cls":
        os.system("cls")
    elif command == "clear":
        os.system("clear")
    elif command == "ls":
        print(Fore.GREEN + "var")
        print(Fore.GREEN + "bin")
    else:
        print(Fore.RED + f"{command}: command not found")
