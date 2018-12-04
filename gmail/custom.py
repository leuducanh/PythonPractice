import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "leuaction@gmail.com"
password = "Leu1261995"
tolist = ["leuaction@gmail.com"]
fromName = username

email_conn = smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username,password)
email_conn.sendmail(fromName,tolist,"Hello")
email_conn.quit()

the_msg = MIMEMultipart("alternative")
the_msg["Subject"] = "Hello there!"
the_msg["From"] = username
the_msg["To"] = tolist



