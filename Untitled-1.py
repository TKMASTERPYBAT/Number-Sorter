import os
from colorama import Fore, init
import time

def main():
    while True:
        print(Fore.RED + "[+] Your List Will Have Ten Number's In It.")
        time.sleep(1)
        print("")
        print(Fore.RED + "[+] Your Will Pick Each One At A Time To Sort.")
        time.sleep(2)
        os.system('cls')
        print(Fore.RED + "[+] Pick Your Number's")
        time.sleep(1)
        print("")
        n1 = input("Enter Number ONE: ")
        n2 = input("Enter Number TWO: ")
        n3 = input("Enter Number THREE: ")
        n4 = input("Enter Number FOUR: ")
        n5 = input("Enter Number FIVE: ")
        n6 = input("Enter Number SIX: ")
        n7 = input("Enter Number SEVEN: ")
        n8 = input("Enter Number EIGHT: ")
        n9 = input("Enter Number NINE: ")
        n0 = input("Enter Number TEN: ")
        os.system('cls')

        if n1 == n1 and n2 == n2 and n3 == n3 and n4 == n4 and n5 == n5 and n6 == n6 and n7 == n7 and n8 == n8 and n9 == n9 and n0 == n0:
            list = [f'{n1}', f'{n2}', f'{n3}', f'{n4}', f'{n5}', f'{n6}', f'{n7}', f'{n8}', f'{n9}', f'{n0}']
            print(Fore.GREEN + f"[+] ORGINAL = {list}")

            sorted = list.sort()
            print("")
            print(Fore.GREEN + f"[+] NEW = {list}")
            print("")
            input("PRESS ANY KEY TO CONTINUE...")

if __name__ == "__main__":
    main()