import requests
import smtplib
from email.mime import multipart
from email.mime import text


def mmsg():
    #check rapidapi.com
    res = requests.get("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous&count=1",
    headers={
    "X-Mashape-Key": "",
    "Accept": "application/json"
    }
    )
    msg = format(res.json()[0]['quote'])
    aut = format(res.json()[0]['author'])
    final_msg = msg+'\n'+' '*(len(msg))+'-'+aut

    return final_msg

def sndmail():
    server = smtplib.SMTP_SSL('smtp.zoho.com',465)
    server.login("mailid", "password")
    receiver = {'Name':'mailid',}
    for key,value in receiver.items():
        final_msg1 = 'Dear'+'\t'+key+'\n Good Morning'+'\n\n'+mmsg()+'\n\n Have a Good Day'
        msg1 = multipart.MIMEMultipart()
        msg1['From'] = 'mailid'
        msg1['To'] = value
        msg1['Subject'] = 'Morning Quotes'
        msg1.attach(text.MIMEText(final_msg1))
        server.sendmail("mailid", value, msg1.as_string())
    server.quit()

if __name__ == "__main__":
    sndmail()