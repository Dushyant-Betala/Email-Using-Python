import smtplib
from email.message import EmailMessage


email =EmailMessage()
email['from'] = 'Dushyant Betala'
email['to'] = "db1624@srmist.edu.in"
email['subject'] = 'Trial E-mail'

email.set_content('I am a Python Developer')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('r.dushyantbetala2611@gmail.com', 'DushyantBetalaRock$26')
    smtp.send_message(email)
    print("All done!")