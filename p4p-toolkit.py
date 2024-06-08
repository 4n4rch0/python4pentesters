# @AUTHOR: 4N4NRCH0
# This toolkit contains any code of the mentioned THM room as fully automated python application.
# The code demonstrates the automation of python code snippets to make tasks and procedures more efficient.
# In a security engagement it can be a big advantage to prepare useful scripts all together in one toolkit.
# This application is a demonstration, based on the "Python for Pentesters" room.

import os
import sys
import pyfiglet
from colorama import init, Fore, Back

def banner(titel):
    init()
    print(Fore.RED+"*"*65+Fore.RESET)
    print(17*"-"+"\tCREATED BY 4N4RCH0\t"+"-"*17)
    print(Back.BLACK+Fore.RED+pyfiglet.figlet_format(titel, font="avatar")+Back.RESET+Fore.RESET)
    print(Fore.RED+"*"*65+Fore.RESET)

class Webattacks:
    
    def __init__(self):
        pass

    def subdir_enumerate(self):
        target_domain = input("[?] Enter target domain: ")
        os.system(f"python sub3num.py {target_domain}")

    def directory_enumerate(self):
        target_domain = input("[?] Enter target domain: ")
        os.system(f"python dir3num.py {target_domain}")

    def download_file(self):
        os.system(f"python downloader.py")

class Networkattacks:
    
    def __init__(self):
        pass
    
    def arp_scan(self):
        os.system("python 4rpsc4n.py")
    
    def port_scan(self):
        os.system("python p0rtsc4n.py")

class Passwordattacks:
    
    def __init__(self):
        pass
    
    def hash_crack(self):
        os.system("python h4shcr4ck.py")
    
    def ssh_brute_force(self):
        os.system("python ssh_cr4ck3r.py")

class Postexploitation:
    
    def __init__(self):
        pass
    
    def key_log(self):
        os.system("python k3yl0g.py")

class p4p_menu:
    
    def __init__(self):
        pass
    
    def user_menu(self):
        
        menu_sections = ["Webattacks", "Networkattacks", "Passwordattacks", "Postexploitation", "Exit"]
        
        for n in range(0, len(menu_sections)):

            print(f"[{str(n+1)}] {menu_sections[n]}")

        user_input = input("[ > ] ")

        tools_menu = menu_sections[int(user_input)-1]

        os.system("cls")

        banner(" P4P-Toolkit ")

        if tools_menu == "Webattacks":

            webattack_toolbelt = ["sub3num", "dir3num", "downloader"]

            for n in range(0, len(webattack_toolbelt)):

                print(f"[{str(n+1)}] {webattack_toolbelt[n]}")

            tool_input = input("[ > ] ")

            if tool_input == "1":
                os.system("cls")
                Webattacks().subdir_enumerate()
            if tool_input == "2":
                os.system("cls")
                Webattacks().directory_enumerate()
            if tool_input == "3":
                os.system("cls")
                Webattacks().download_file()

        if tools_menu == "Networkattacks":

            networkattack_toolbelt = ["4rpsc4n", "p0rtsc4n"]

            for n in range(0, len(networkattack_toolbelt)):

                print(f"[{str(n+1)}] {networkattack_toolbelt[n]}")

            tool_input = input("[ > ] ")

            if tool_input == "1":
                os.system("cls")
                Networkattacks().arp_scan()
            if tool_input == "2":
                os.system("cls")
                Networkattacks().port_scan()
        
        if tools_menu == "Passwordattacks":

            passwordattack_toolbelt = ["h4shcr4ck", "ssh_cr4ck3r"]

            for n in range(0, len(passwordattack_toolbelt)):

                print(f"[{str(n+1)}] {passwordattack_toolbelt[n]}")

            tool_input = input("[ > ] ")

            if tool_input == "1":
                os.system("cls")
                Passwordattacks().hash_crack()
            if tool_input == "2":
                os.system("cls")
                Passwordattacks().ssh_brute_force()

        if tools_menu == "Postexploitation":

            postexploit_toolbelt = ["k3yl0g"]

            for n in range(0, len(postexploit_toolbelt)):

                print(f"[{str(n+1)}] {postexploit_toolbelt[n]}")

            tool_input = input("[ > ] ")

            if tool_input == "1":
                os.system("cls")
                Postexploitation().key_log()

        if tools_menu == "Exit":
            sys.exit()

def main():
    
    os.system("cls")
    
    try:
        
        banner(" P4P-Toolkit ")

        p4p_menu().user_menu()

    except KeyboardInterrupt:
        sys.exit()

    except Exception as e:
        print(e)
        sys.exit()
    
if __name__ == '__main__':

    main()