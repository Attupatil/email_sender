# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage
from string import Template
from pathlib import Path #os.path

html =Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = '' #Your name
email['to'] = '@gmail.com' #reciptantsemail@gmail.com
email['subject'] = ' blah blah blah' #subject

email.set_content(html.substitute({'name':'nameofsender'}),'html')#write the name to whom you are sending

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('<youremailaddress@gmail.com>','<your password>') #write your emailaddress along with password
	smtp.send_message(email)
	print('all good boss!!') #defines program exicuted successfully

