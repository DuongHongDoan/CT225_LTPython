import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
sender = 'doanb2013527@student.ctu.edu.vn'
passwd = 'xxxxxx' #nhap mat khau email cua ban, day la mat khau xac minh 2 buoc trong gmail!!!
receiver = 'duonghongdoan.hp2020@gmail.com'

msg = MIMEMultipart()
msg['Subject'] = 'Python Email Test'
msg['To'] = 'duonghongdoan.hp2020@gmail.com'
msg['From'] = 'doanb2013527@student.ctu.edu.vn'
string = ''
while True:
    body = input()
    if body.strip() == '.':
        break
    string += body + '\n'
msg.attach(MIMEText(string, 'plain'))
smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
smtp.login(sender,passwd)
print("Login success")
smtp.sendmail(sender, receiver, msg.as_string())
print("Email sented.")
smtp.quit()