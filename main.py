import os
import requests
import json
import time
import random
import sys
import string
from colorama import init,Fore
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool
from threading import Thread, Lock
from fake_useragent import UserAgent

class Main:
    def clear(self):
        if os.name == 'posix':
            os.system('clear')
        elif os.name in ('ce', 'nt', 'dos'):
            os.system('cls')
        else:
            print("\n") * 120

    def SetTitle(self,title_name:str):
        os.system("title {0}".format(title_name))

    def ReadFile(self,filename,method):
        with open(filename,method) as f:
            content = [line.strip('\n') for line in f]
            return content

    def __init__(self):
        self.SetTitle('One Man Builds TikTok Username Checker Tool')
        self.clear()
        init(convert=True)
        title = Fore.YELLOW+"""
                        
               ___ _ _  _ ___ ____ _  _    _  _ ____ ____ ____ _  _ ____ _  _ ____ 
                |  | |_/   |  |  | |_/     |  | [__  |___ |__/ |\ | |__| |\/| |___ 
                |  | | \_  |  |__| | \_    |__| ___] |___ |  \ | \| |  | |  | |___ 
                                                                                    
                                ____ _  _ ____ ____ _  _ ____ ____                                  
                                |    |__| |___ |    |_/  |___ |__/                                  
                                |___ |  | |___ |___ | \_ |___ |  \                                  
                                                                                                    
                        
        """
        print(title)
        self.ua = UserAgent()
        
        self.option = int(input(Fore.YELLOW+'['+Fore.WHITE+'>'+Fore.YELLOW+'] Would you like to [1]Generate Usernames [0]Check Usernames: '))

        print('')
        self.usernames = self.ReadFile('usernames.txt','r')

    def GetRandomProxy(self):
        proxies_file = self.ReadFile('proxies.txt','r')
        proxies = {
            "http":"http://{0}".format(random.choice(proxies_file)),
            "https":"https://{0}".format(random.choice(proxies_file))
            }
        return proxies

    def UsernameGenRandomChars(self,amount,length,include_digits,prefix,suffix):
        counter = 0
        for i in range(amount):
            counter = i+1
            if include_digits == 1:
                username = prefix+''.join(random.choice(string.ascii_letters+'0123456789') for num in range(length))+suffix
            else:
                username = prefix+''.join(random.choice(string.ascii_letters) for num in range(length))+suffix
            print(Fore.GREEN+'['+Fore.WHITE+f'{counter}'+Fore.GREEN+f'] {username}')
            with open('usernames.txt','a',encoding='utf8') as f:
                f.write(username+'\n')

    def CheckUsernames(self,usernames):
        try:
            headers = {
                'User-Agent':self.ua.random
            }

            response = ''

            if self.use_proxy == 1:
                response = requests.get("https://www.tiktok.com/@{0}".format(usernames),headers=headers,proxies=self.GetRandomProxy()).text
            else:
                response = requests.get("https://www.tiktok.com/@{0}".format(usernames),headers=headers).text

            if 'jsx-4111167561 title' in response:
                print(Fore.GREEN+'['+Fore.WHITE+'!'+Fore.GREEN+'] AVAILABLE | {0}'.format(usernames))
                self.PrintText('AVAILABLE',usernames,Fore.GREEN,Fore.WHITE)
                with open('available_usernames.txt','a') as f:
                    f.write(usernames+"\n")
            else:
                print(Fore.RED+'['+Fore.WHITE+'!'+Fore.RED+'] NOT AVAILABLE | {0}'.format(usernames))
                with open('bad_usernames.txt','a') as f:
                    f.write(usernames+"\n")
        except:
            self.CheckUsernames(usernames)

    def Start(self):
        if self.option == 1:
            amount = int(input(Fore.YELLOW+'['+Fore.WHITE+'>'+Fore.YELLOW+'] Enter the amount: '))
            length = int(input(Fore.YELLOW+'['+Fore.WHITE+'>'+Fore.YELLOW+'] Enter the length: '))
            include_digits = int(input(Fore.YELLOW+'['+Fore.WHITE+'>'+Fore.YELLOW+'] Include digits [1]yes [2]no: '))
            prefix = str(input(Fore.YELLOW+'['+Fore.WHITE+'>'+Fore.YELLOW+'] Prefix (leave it empty if you dont want to use it): '))
            suffix = str(input(Fore.YELLOW+'['+Fore.WHITE+'>'+Fore.YELLOW+'] Suffix (leave it empty if you dont want to use it): '))
            self.UsernameGenRandomChars(amount,length,include_digits,prefix,suffix)
        else:
            self.use_proxy = int(input(Fore.YELLOW+'['+Fore.WHITE+'>'+Fore.YELLOW+'] Would you like to use proxies [1] yes [0] no: '))
            pool = ThreadPool()
            results = pool.map(self.CheckUsernames,self.usernames)
            pool.close()
            pool.join()

if __name__ == "__main__":
    main = Main()
    main.Start()
    