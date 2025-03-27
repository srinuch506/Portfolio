import smtplib
from email.message import EmailMessage
def sendmail(From,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('srinivasaraoch506@gmail.com','lraz tzfd mmad rmmu')
    msg=EmailMessage()
    msg['From']=From
    msg['To']='srinivasaraoch506@gmail.com'
    msg['Subject']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()