import csv
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('templates'), #before running create a folder named templates
    autoescape=select_autoescape(['html', 'xml'])
)


template = env.get_template() #name of the html file


email_user="" #enter sender email
password="" #enter your password (if you have 2FA on read this https://support.google.com/accounts/answer/185833?hl=en)
subject="" #enter email subject

#download your progress report in csv format and save it inside the script folder named data.csv
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    for line in reader:
        #make a html file with your formatted message and custom styles or simply use a string with all the message content
        html = template.render(name=line[0], quests=line[6], skill_badges=line[7])
        email_send=line[1]
        msg=MIMEMultipart("alternative")
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject
        msg.attach(MIMEText(html, "html"))
            
                

        server=smtplib.SMTP_SSL("smtp.gmail.com",465)
                
        server.login(email_user,password)
        text = msg.as_string()
        server.sendmail(email_user,email_send,text)
        print(f"sent successfully")
        server.quit()