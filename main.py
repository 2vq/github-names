import os
import time
import random
import string
import requests
from colorama import Fore

os.system('cls')

def check():
        os.system(f'cls & title Github Name Checker')
        amount = input(f'{Fore.LIGHTBLACK_EX}>{Fore.BLUE} Amount{Fore.LIGHTBLACK_EX}: {Fore.LIGHTBLUE_EX}')
        Letter = input(f'{Fore.LIGHTBLACK_EX}>{Fore.BLUE} Letters{Fore.LIGHTBLACK_EX}: {Fore.LIGHTBLUE_EX}')
        for i in range(int(amount)):
            try:
                code = ''.join(random.choices(string.ascii_letters + string.digits, k = (int(Letter))))
                r = requests.get(f'https://github.com/{code}')
                if r.status_code == 404:
                    with open('github-names.txt', 'a') as f:
                        f.writelines(f'https://github.com/{code}\n')
                        print(f'{Fore.LIGHTBLACK_EX}>{Fore.BLUE} Non Taken Name{Fore.LIGHTBLACK_EX}: {Fore.LIGHTBLUE_EX}{code}')
                elif r.status_code == 200:
                    print(f'{Fore.LIGHTBLACK_EX}>{Fore.RED} Taken Name{Fore.LIGHTBLACK_EX}: {Fore.LIGHTRED_EX}{code}')
                else:
                    pass
            except:
                pass

if __name__ == '__main__':
    check()
