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

    def PrintText(self,info_name,text,info_color:Fore,text_color:Fore):
        lock = Lock()
        lock.acquire()
        sys.stdout.flush()
        text = text.encode('ascii','replace').decode()
        sys.stdout.write(f'[{info_color+info_name+Fore.RESET}] '+text_color+f'{text}\n')
        lock.release()

    def __init__(self):
        self.SetTitle('One Man Builds TikTok Username Checker Tool')
        self.clear()
        init()
        self.ua = UserAgent()
        
        self.option = int(input('[QUESTION] Would you like to [1]Generate Usernames [0]Check Usernames: '))

        print('')
        self.usernames = self.ReadFile('usernames.txt','r')

    def GetRandomProxy(self):
        proxies_file = self.ReadFile('proxies.txt','r')
        proxies = {
            "http":"http://{0}".format(random.choice(proxies_file)),
            "https":"https://{0}".format(random.choice(proxies_file))
            }
        return proxies

    def GenUsername(self,amount,length):
        for i in range(amount):
            name = ''.join(random.choice(string.ascii_letters+'0123456789') for num in range(length))
            count = i+1
            self.PrintText(str(count),name,Fore.GREEN,Fore.WHITE)
            with open('usernames.txt','a',encoding='utf8') as f:
                f.write(name+'\n')

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
                self.PrintText('AVAILABLE',usernames,Fore.GREEN,Fore.WHITE)
                with open('available_usernames.txt','a') as f:
                    f.write(usernames+"\n")
            else:
                self.PrintText('NOT AVAILABLE',usernames,Fore.RED,Fore.WHITE)
                with open('bad_usernames.txt','a') as f:
                    f.write(usernames+"\n")
        except:
            self.CheckUsernames(usernames)

    def Start(self):
        if self.option == 1:
            self.amount = int(input('[QUESTION] Enter the amount: '))
            self.length = int(input('[QUESTION] Enter the length: '))
            self.GenUsername(self.amount,self.length)
        else:
            self.use_proxy = int(input('[QUESTION] Would you like to use proxies [1] yes [0] no: '))
            pool = ThreadPool()
            results = pool.map(self.CheckUsernames,self.usernames)
            pool.close()
            pool.join()


if __name__ == "__main__":
    main = Main()
    main.Start()
    