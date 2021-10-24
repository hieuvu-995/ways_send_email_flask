import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "send_email"  # the email where you sent the email
password = "password"
send_to_email = "recipient_email"  # for whom
subject = "Gmail"
message = "This is active email!"


msg = MIMEMultipart()
msg["From"] = email
msg["To"] = send_to_email
msg["Subject"] = subject

msg.attach(MIMEText(message, "plain"))
text = msg.as_string()

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, password)
server.sendmail(email, send_to_email, text)
server.quit()
