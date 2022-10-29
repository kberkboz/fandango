import subprocess

print("███████╗░█████╗░███╗░░██╗██████╗░░█████╗░███╗░░██╗░██████╗░░█████╗░")
print("██╔════╝██╔══██╗████╗░██║██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗")
print("█████╗░░███████║██╔██╗██║██║░░██║███████║██╔██╗██║██║░░██╗░██║░░██║")
print("██╔══╝░░██╔══██║██║╚████║██║░░██║██╔══██║██║╚████║██║░░╚██╗██║░░██║")
print("██║░░░░░██║░░██║██║░╚███║██████╔╝██║░░██║██║░╚███║╚██████╔╝╚█████╔╝")
print("╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░░╚════╝░")
print("")
print("Mac Changer")
print("")
print("[+] Attempting to change MAC adress...")
print("Enter interface (wlan0 for wireless and eth0 for wired connections most of the time) ")
iface= input("> ")


def change_mac(): 
    subprocess.call("sudo ifconfig "+iface+" down", shell=True)
    subprocess.call("sudo macchanger --random "+iface, shell=True)
    subprocess.call("sudo ifconfig "+iface+" up", shell=True)

change_mac()