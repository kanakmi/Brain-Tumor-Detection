import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_mail(to,typ,probability):
    message = Mail(
        from_email='result.tumor.detection@mail.com',
        to_emails=to,
        subject='Your Report',
        html_content='Our AI asses your report and found <strong>'+str(typ)+'</strong> with probability of '+str(probability))

    sg = SendGridAPIClient('SK7408a1a9c65e8f94ac82d0f0eef4075e')
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)
