# modules
import smtplib
from email.message import EmailMessage
import psutil
import time

# content
def mailat(ram,max_cpu):
    sender = "Gönderen mail"
    reciever = ["alıcı1","alıcı2"]
    password = "mail şifresi"
    msg_body = """CPU= """ +  str(max_cpu) +""" RAM=""" + str(ram)
    
    # action
    msg = EmailMessage()
    msg['subject'] = 'Bilgilendirme kısmı'   
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
   


    
