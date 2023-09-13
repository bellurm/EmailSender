import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_email = "CHANGE ME" # bir gönderici var
receiver_email = "CHANGE ME" # bir alıcı var

message = MIMEMultipart("")
message["Subject"] = "CHANGE ME"
message["From"] = sender_email
message["To"] = receiver_email

text = """
CHANGE ME
"""

part1 = MIMEText(text, "plain")
message.attach(part1)

filepath = "CHANGE"
part2 = MIMEBase('application', "octet-stream")
part2.set_payload(open(filepath, "rb").read())
encoders.encode_base64(part2)

part2.add_header('Content-Disposition', 'attachment; filename = "CHANGE"')
message.attach(part2)

context = ssl.create_default_context()
server = smtplib.SMTP("CHANGE ME (an email server)", 587)
server.starttls()
server.ehlo_or_helo_if_needed()
server.sendmail(sender_email, receiver_email, message.as_string())
