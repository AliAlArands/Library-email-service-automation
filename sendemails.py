from email.message import EmailMessage
import ssl
import smtplib
import csv

# Enter the email you want to send from
email_sender = 'your email'


with open('contacts.csv', mode='r') as file:

    csvFile = csv.reader(file)

    for line in csvFile:
        emial_receiver = line[3]
        if '@' in emial_receiver:
            print(emial_receiver)
    
            message = EmailMessage()
            message['From'] = email_sender
            message['To'] = emial_receiver

            message["subject"] = "Invitation Letter for Book Exhibition"

            #Edit the message
            body = f"""Dear {line[0]} {line[1]},
            We are organizing a Book Fair Exhibition named as (Exhibition Name) where young talented [Writers and Poets] will put their books/ book stalls for two days. 
            we are also giving stalls to (Name and place name) for special children (Write specific category) where they will show their creations to the general public and sell it out.
            Kindly let us know if you are interested in a great opportunity.

            Date
            Address…

            Elon Smith        
            Company or Institute name…
            """
            message.set_content(body)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                #Enter Your Application Password!
                smtp.login(email_sender,'your_password')
                smtp.sendmail(email_sender, emial_receiver, message.as_string())