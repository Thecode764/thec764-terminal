from colorama import init, Fore
import os
import sys
system = sys.platform
command = input(Fore.GREEN + system + Fore.BLUE + "> ")
if command == "cd":
    print(Fore.RED + "cd is not defind try ./ and folder name")
elif command == "ls":
    print(Fore.RED + "ls and cd is not defind")
elif command == "system":
    print(sys.platform)
elif command == "./":
    print(Fore.CYAN + "var")
    print(Fore.CYAN + "bin")
    print(Fore.CYAN + "sh")
    print(Fore.CYAN + "./root")
elif command == "./var":
    print(Fore.GREEN + "Chnaged To var")
    print(Fore.RED + "var is empty and lock")
elif command == "./bin":
    print(Fore.RED + "bin is lock")
elif command == "./sh":
    print(Fore.GREN + "sh file is tm.py")
elif command == "./root":
    os.system("python3 rt.py")
elif command == "//python":
    os.system("python3")
elif command == "clear":
    os.system("clear")
while command != "end":
    from colorama import init, Fore
    import os
    import sys
    system = sys.platform
    command = input(Fore.GREEN + system + Fore.BLUE + "> ")
    if command == "cd":
        print(Fore.RED + "cd is not defind try ./ and folder name")
    elif command == "ls":
        print(Fore.RED + "ls and cd is not defind")
    elif command == "system":
        print(sys.platform)
    elif command == "./":
        print(Fore.CYAN + "var")
        print(Fore.CYAN + "bin")
        print(Fore.CYAN + "sh")
        print(Fore.CYAN + "./root")
    elif command == "./var":
        print(Fore.GREEN + "Chnaged To var")
        print(Fore.RED + "var is empty and lock")
    elif command == "./bin":
        print(Fore.RED + "bin is lock")
    elif command == "./sh":
        print(Fore.GREN + "sh file is tm.py")
    elif command == "./root":
        os.system("python3 rt.py")
    elif command == "//python":
        os.system("python3")
    elif command == "clear":
        os.system("clear")