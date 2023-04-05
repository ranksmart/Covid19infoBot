import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
import os


# class GMailClient:
def sendEmail(contacts):
    EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

    msg = EmailMessage()
    msg['Subject'] = 'Detailed Covid-19 Report!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = contacts[2]
    name=contacts[2].split('@')
    name=name[0]

    values = contacts[3]
    msg.set_content(f"""Hello {name}, \n\nHere are Covid 19 Cases Details of {contacts[4].upper()} Country:

    Total_Cases------->{str(values.get('total'))}
    New_Cases------->{str(values.get('new'))}
    Active_Cases------->{str(values.get('active'))}
    Critical_Cases------->{str(values.get('critical'))}
    Recovered_Cases------->{str(values.get('recovered'))}
    
    
    STAY SAFE FROM COVID VIRUS AND WEAR MASK!! """)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

# sendEmail(['rakesh','954333333','rakeshsinghsis123@gmail.com',[1,2,3,4,5],'india'])
