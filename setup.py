
import subprocess

print("███████╗░█████╗░███╗░░██╗██████╗░░█████╗░███╗░░██╗░██████╗░░█████╗░")
print("██╔════╝██╔══██╗████╗░██║██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗")
print("█████╗░░███████║██╔██╗██║██║░░██║███████║██╔██╗██║██║░░██╗░██║░░██║")
print("██╔══╝░░██╔══██║██║╚████║██║░░██║██╔══██║██║╚████║██║░░╚██╗██║░░██║")
print("██║░░░░░██║░░██║██║░╚███║██████╔╝██║░░██║██║░╚███║╚██████╔╝╚█████╔╝")
print("╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░░╚════╝░")
print("")
print("Setup Tool")
print("")
print("[+] Initiating one time setup... ")

def pip_install(): 
    subprocess.call("pip3 install netifaces",shell=True)
    subprocess.call("pip3 install Twisted==15.5.0",shell=True)
    subprocess.call("pip3 install pyhunter",shell=True)
    subprocess.call("sudo apt-get install gnome-terminal",shell=True)
    subprocess.call("pip3 install pyhunter",shell=True)
    subprocess.call("pip3 install pyperclip",shell=True)
    subprocess.call("pip3 install colorama",shell=True)
    subprocess.call("pip3 install googlesearch-python",shell=True)
    subprocess.call("pip3 install getmac",shell=True)

def install(): 
    #installing xerosploit
    subprocess.call("sudo apt-get install nmap",shell=True)
    subprocess.call("sudo apt-get install hping3",shell=True)
    subprocess.call("sudo apt-get install build-essential",shell=True)
    subprocess.call("sudo apt-get install ruby-dev",shell=True)
    subprocess.call("sudo apt-get install libpcap-dev",shell=True)
    subprocess.call("sudo apt-get install libgmp3-dev",shell=True)
    subprocess.call("sudo apt-get install bettercap",shell=True)
    subprocess.call("sudo pip install tabulate",shell=True)
    subprocess.call("sudo pip install terminaltables",shell=True)
    print("Allow xettercap to execute in xerosploit/tools/bettercap/bin/xettercap! Input anything to continue")
    input()
    subprocess.call("sudo python2 xerosploit/install.py",shell=True)

pip_install()
install()
