import smtplib

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    #sender e-mail and password
    server.login("sender_email_id", "sender_email_id_password")
    server.sendmail("sender_email_id", to, content)
    server.close()

'''

elif "send email" in query:
try:
    speak("what should i say?")
    content = takeCommand()
    to = "receiver_email"
    sendmail(to, content)
    speak("Email send sucessfully")
except Exception as e:
    speak(e)
    speak("unable to send the email")

'''


#OR CREATE LIST OF SENDERS
'''
li = ["xxxxx@gmail.com", "yyyyy@gmail.com"]

for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("sender_email_id", "sender_email_id_password")
    message = "Message_you_need_to_send"
    s.sendmail("sender_email_id", dest, message)
    s.quit()
'''