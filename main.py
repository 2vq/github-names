import os
import time
import random
import string
import requests
import threading
from slowprint.slowprint import slowprint as slowp
from colorama import Fore

os.system('cls')

slowp(f'NOTE: might get you ratelimited very fast!', 0.2)
threadcount = input(f'{Fore.LIGHTBLACK_EX}>{Fore.BLUE} Threads{Fore.LIGHTBLACK_EX}: {Fore.LIGHTBLUE_EX}')
amount = input(f'{Fore.LIGHTBLACK_EX}>{Fore.BLUE} Amount{Fore.LIGHTBLACK_EX}: {Fore.LIGHTBLUE_EX}')
Letter = input(f'{Fore.LIGHTBLACK_EX}>{Fore.BLUE} Letters{Fore.LIGHTBLACK_EX}: {Fore.LIGHTBLUE_EX}')

def check():
        for i in range(int(amount)):
            try:
                code = ''.join(random.choices(string.ascii_letters + string.digits, k = (int(Letter))))
                r = requests.get(f'https://github.com/{code}')
                if r.status_code == 404:
                    print(f'{Fore.LIGHTBLACK_EX}>{Fore.BLUE} Non Taken Name{Fore.LIGHTBLACK_EX}: {Fore.LIGHTBLUE_EX}{code}')
                    with open('github-names.txt', 'a', encoding = 'UTF-8') as f:
                        f.write(f'https://github.com/{code}\n')
                elif r.status_code == 200:
                    print(f'{Fore.LIGHTBLACK_EX}>{Fore.RED} Taken Name{Fore.LIGHTBLACK_EX}: {Fore.LIGHTRED_EX}{code}')
                else:
                    pass
            except:
                pass

def thread():
    for i in range(int(threadcount)):
        threading.Thread(target = check).start()
    
if __name__ == '__main__':
    thread()
