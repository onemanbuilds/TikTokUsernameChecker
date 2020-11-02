from colorama import init,Fore,Style
from os import name,system
from sys import stdout
from random import choice
from threading import Thread,Lock,active_count
from fake_useragent import UserAgent
from string import ascii_letters,digits
from time import sleep
from bs4 import BeautifulSoup
import requests
import json

class Main:
    def clear(self):
        if name == 'posix':
            system('clear')
        elif name in ('ce', 'nt', 'dos'):
            system('cls')
        else:
            print("\n") * 120

    def SetTitle(self,title_name:str):
        if name in ('ce', 'nt', 'dos'):
            system("title {0}".format(title_name))
        else:
            stdout.write("\x1b]2;{0}\x07".format(title_name))

    def __init__(self):
        init(convert=True)
        self.clear()
        self.SetTitle('One Man Builds TikTok Username Checker ^& Generator')
        self.title = Style.BRIGHT+Fore.RED+"""                                        
                 _____ ___ _  _______ ___  _  __  _   _ ____  _____ ____  _   _    _    __  __ _____ 
                |_   _|_ _| |/ /_   _/ _ \| |/ / | | | / ___|| ____|  _ \| \ | |  / \  |  \/  | ____|
                  | |  | || ' /  | || | | | ' /  | | | \___ \|  _| | |_) |  \| | / _ \ | |\/| |  _|  
                  | |  | || . \  | || |_| | . \  | |_| |___) | |___|  _ <| |\  |/ ___ \| |  | | |___ 
                  |_| |___|_|\_\ |_| \___/|_|\_\  \___/|____/|_____|_| \_\_| \_/_/   \_\_|  |_|_____|
                                  ____ _   _ _____ ____ _  _______ ____                                              
                                 / ___| | | | ____/ ___| |/ / ____|  _ \                                             
                                | |   | |_| |  _|| |   | ' /|  _| | |_) |                                            
                                | |___|  _  | |__| |___| . \| |___|  _ <                                             
                                 \____|_| |_|_____\____|_|\_\_____|_| \_\                                            


        """
        print(self.title)
        self.availables = 0
        self.takens = 0
        self.retries = 0
        self.ua = UserAgent()
        self.lock = Lock()
        self.use_proxy = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] ['+Fore.RED+'1'+Fore.CYAN+']Proxy ['+Fore.RED+'0'+Fore.CYAN+']Proxyless: '))

        if self.use_proxy == 1:
            self.proxy_type = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] ['+Fore.RED+'1'+Fore.CYAN+']Https ['+Fore.RED+'2'+Fore.CYAN+']Socks4 ['+Fore.RED+'3'+Fore.CYAN+']Socks5: '))
        
        self.method = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] ['+Fore.RED+'1'+Fore.CYAN+']Brute ['+Fore.RED+'0'+Fore.CYAN+']From Usernames.txt: '))
        self.enable_webhook = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] ['+Fore.RED+'1'+Fore.CYAN+']Enable Webhook ['+Fore.RED+'0'+Fore.CYAN+']No Webhook: '))
        self.threads_num = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Threads: '))
        
        if self.enable_webhook == 1:
            self.webhook_url = str(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Webhook URL: '))

        print('')

    def PrintText(self,bracket_color:Fore,text_in_bracket_color:Fore,text_in_bracket,text):
        self.lock.acquire()
        stdout.flush()
        text = text.encode('ascii','replace').decode()
        stdout.write(Style.BRIGHT+bracket_color+'['+text_in_bracket_color+text_in_bracket+bracket_color+'] '+bracket_color+text+'\n')
        self.lock.release()

    def ReadFile(self,filename,method):
        with open(filename,method) as f:
            content = [line.strip('\n') for line in f]
            return content

    def GetRandomProxy(self):
        proxies_file = self.ReadFile('proxies.txt','r')
        proxies = {}
        if self.proxy_type == 1:
            proxies = {
                "http":"http://{0}".format(choice(proxies_file)),
                "https":"https://{0}".format(choice(proxies_file))
            }
        elif self.proxy_type == 2:
            proxies = {
                "http":"socks4://{0}".format(choice(proxies_file)),
                "https":"socks4://{0}".format(choice(proxies_file))
            }
        else:
            proxies = {
                "http":"socks5://{0}".format(choice(proxies_file)),
                "https":"socks5://{0}".format(choice(proxies_file))
            }
        return proxies

    def TitleUpdate(self):
        while True:
            try:
                self.SetTitle('One Man Builds TikTok Username Checker & Generator | AVAILABLES: {0} | TAKENS: {1} | RETRIES: {2} | THREADS: {3}'.format(self.availables,self.takens,self.retries,active_count()-1))
            except:
                self.SetTitle('One Man Builds TikTok Username Checker ^& Generator ^| AVAILABLES: {0} ^| TAKENS: {1} ^| RETRIES: {2} ^| THREADS: {3}'.format(self.availables,self.takens,self.retries,active_count()-1))
            
            sleep(0.1)

    def Start(self):
        Thread(target=self.TitleUpdate).start()
        if self.method == 1:
            username_length = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Length: '))
            include_digits = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Include Digits ['+Fore.RED+'1'+Fore.CYAN+']yes ['+Fore.RED+'0'+Fore.CYAN+']no: '))
            prefix = str(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Prefix (leave it blank if you dont want to use): '))
            suffix = str(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Suffix (leave it blank if you dont want to use): '))
            print('')
            Run = True
            while Run:
                if active_count()<=self.threads_num:
                    name = self.GenName(username_length,include_digits,prefix,suffix)
                    Thread(target=self.TikTokUsernameCheck,args=(name,)).start()
        else:
            usernames = self.ReadFile('usernames.txt','r')
            for username in usernames:
                Run = True

                if active_count()<=self.threads_num:
                    Thread(target=self.TikTokUsernameCheck,args=(username,)).start()
                    Run = False

    def GenName(self,length,include_digits,prefix,suffix):
        if include_digits == 1:
            name = prefix+''.join(choice(ascii_letters+digits) for num in range(length))+suffix
        else:
            name = prefix+''.join(choice(ascii_letters) for num in range(length))+suffix
        return name

    def SendWebhook(self,message,proxy):
        try:
            if 'https://discord.com/api/webhooks/' in self.webhook_url:
                message_to_send = {'content':message}

                headers = {
                    'User-Agent':self.ua.random,
                    'Pragma':'no-cache',
                    'Accept':'*/*',
                    'Content-Type':'application/json'
                }

                payload = json.dumps(message_to_send)

                if self.use_proxy == 1:
                    response = requests.post(self.webhook_url,data=payload,headers=headers,proxies=proxy)
                else:
                    response = requests.post(self.webhook_url,data=payload,headers=headers)

                if response.text == "":
                    self.PrintText(Fore.CYAN,Fore.RED,'WEBHOOK','MESSAGE {0} SENT'.format(message))
                elif "You are being rate limited." in response.text:
                    self.PrintText(Fore.RED,Fore.CYAN,'WEBHOOK','YOU ARE RATELIMITED')
                else:
                    self.PrintText(Fore.RED,Fore.CYAN,'WEBHOOK','SOMETHING WENT WRONG RETRY')
                    self.SendWebhook(message)
        except:
            self.SendWebhook(message)

    def TikTokUsernameCheck(self,name):
        try:
            session = requests.session()

            link = 'https://www.tiktok.com/@{0}/'.format(name)

            headers = {
                'User-Agent':self.ua.random,
            }

            response = ''

            proxy = self.GetRandomProxy()

            if self.use_proxy == 1:
                response = session.get(link,headers=headers,proxies=proxy)
            else:
                response = session.get(link,headers=headers)

            soup = BeautifulSoup(response.text,'html.parser')
            
            if soup.find('p',{'class':'jsx-4111167561 title'}).text == "Couldn't find this account":
                self.availables = self.availables+1
                self.PrintText(Fore.CYAN,Fore.RED,'AVAILABLE',name)
                with open('availables.txt','a',encoding='utf8') as f:
                    f.write(name+'\n')

                if self.enable_webhook == 1:
                    self.SendWebhook('[AVAILABLE] {0}'.format(name),proxy)

            elif soup.find('meta',{'property':'twitter:creator'})['content'] == name:
                self.takens = self.takens+1
                self.PrintText(Fore.RED,Fore.CYAN,'TAKEN',name)
                with open('takens.txt','a',encoding='utf8') as f:
                    f.write(name+'\n')
            else:
                self.retries = self.retries+1
                self.TikTokUsernameCheck(name)
        except:
            self.retries = self.retries+1
            self.TikTokUsernameCheck(name)

if __name__ == '__main__':
    main = Main()
    main.Start()
