# modules
import smtplib
from email.message import EmailMessage
import psutil
import time

# content
def mailat(ram,max_cpu):
    sender = "netcadmailtest@gmail.com"
    reciever = ["naciyilmaz05@gmail.com","receptopalak@gmail.com"]
    password = "ntc123**"
    msg_body = """Antalya Büyükşehir Belediyesi CPU %90 ı Geçti Çabuk Bak! CPU= """ +  str(max_cpu) +""" RAM=""" + str(ram)
    
    # action
    msg = EmailMessage()
    msg['subject'] = 'Antalya Büyükşehir Belediyesi CPU %90 ıGeçti Çabuk Bak!'   
    msg['from'] = sender
    msg['to'] = reciever
    msg.set_content(msg_body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender,password)
        smtp.send_message(msg)
        
while True:
    max_cpu = max(psutil.cpu_percent(interval=5, percpu=True))
    ram = psutil.virtual_memory().percent   
    if max_cpu > 90 :
        mailat(ram,max_cpu)
        print("mail atıldı")   
    time.sleep(3)
   


    
