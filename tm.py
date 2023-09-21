from colorama import init, Fore
import os
import sys
import platform
import datetime

system = sys.platform
os.mkdir("var")
os.mkdir("bin")
command = input(Fore.GREEN + system + Fore.BLUE + "> ")
if command == "terminal --help":
    print(Fore.GREEN + "./var: view files in var folder")
    print(Fore.GREEN + "./bin: view files in bin folder (Dont Show New Files)")
    print(Fore.GREEN + "./sh: refresh terminal")
    print(Fore.GREEN + "make .c: make c file")
    print(Fore.GREEN + "make .cpp: make cpp file")
    print(Fore.GREEN + "make .py: make python file")
    print(Fore.GREEN + "system: get system name")
    print(Fore.GREEN + "processor: processor data")
    print(Fore.GREEN + "datetime: current date and time")
    print(Fore.GREEN + "ls: view dir")
    print(Fore.GREEN + "python: run python")
    print(Fore.GREEN + "python --version: python version")
    print(Fore.GREEN + "python -i: install python modules")
    print(Fore.GREEN + "AMD: your computer AMD")
    print(Fore.GREEN + "edition: windows editions")
    print(Fore.GREEN + "exit(): exit this terminal")
    print(Fore.GREEN + "mkdir: make folder")
    print(Fore.GREEN + "mkfile: make file")
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
elif command == "python":
    os.systen("python3")
elif command == "python --version":
    print(Fore.GREEN + "VERSION: " + platform.python_version())
elif command == "python -i":
    pip = input(Fore.RED + "Enter Python Package Name:")
    os.system("pip install " + pip)
elif command == "AMD":
    print(platform.machine())
elif command == "edition":
    if system == "win32":
        print(Fore.GREEN + platform.win32_edition())
    else:
        print(Fore.RED + "this command not supported in your device")
elif command == "exit()":
    sys.exit()
elif command == "mkdir":
    os.chdir("bin")
    namefolder = input(Fore.RED + "Enter Folder Name:")
    os.mkdir(namefolder)
elif command == "mkfile":
    dir = input("Enter Dir Name:")
    os.chdir(dir)
    namefile = input("Enter File Name:")
    os.system("code " + namefile)
else:
    print(Fore.RED + f"{command}: command not found")
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
        print(Fore.GREEN + "python: run python")
        print(Fore.GREEN + "python --version: python version")
        print(Fore.GREEN + "python -i: install python modules")
        print(Fore.GREEN + "AMD: your computer AMD")
        print(Fore.GREEN + "edition: windows editions")
        print(Fore.GREEN + "exit(): exit this terminal")
        print(Fore.GREEN + "mkdir: make folder")
        print(Fore.GREEN + "mkfile: make file")
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
    elif command == "python":
        os.system("python3")
    elif command == "python --version":
        print(Fore.GREEN + "VERSION: " + platform.python_version())
    elif command == "python -i":
        pip = input(Fore.RED + "Enter Python Package Name:")
        os.system("pip install " + pip)
    elif command == "AMD":
        print(platform.machine())
    elif command == "edition":
        if system == "win32":
            print(Fore.GREEN + platform.win32_edition())
        else:
            print(Fore.RED + "this command not supported in your device")
    elif command == "exit()":
        sys.exit()
    elif command == "mkdir":
        os.chdir("bin")
        namefolder = input(Fore.RED + "Enter Folder Name:")
        os.mkdir(namefolder)
    elif command == "mkfile":
        dir = input("Enter Dir Name:")
        os.chdir(dir)
        namefile = input("Enter File Name:")
        os.system("code " + namefile)
    else:
        print(Fore.RED + f"{command}: command not found")
