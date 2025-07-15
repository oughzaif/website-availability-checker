import requests
import socket
from rich import print
url = "http://testphp.vulnweb.com"
domain = "testphp.vulnweb.com"
ip = socket.gethostbyname(domain)
try:
    respance=requests.get(url ,timeout=5) 
    if respance.status_code == 200 : 
        print("[bold green]good test[bold green/]",f"[italic blue]{respance.status_code}[/]")
        print(f"[red]{ip}")
except  requests.ConnectionError :
    print("no" , url, "down",respance.status_code)
    
