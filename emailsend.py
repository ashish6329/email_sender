import smtplib,webbrowser
def get_mail():
	servicesavailable=['hotmail','yahoo','outlook','gmail']
	while True:
		mail_id=input("E-mail :  ")
		if '@' in mail_id and '.com' in mail_id:
			symbol_pos=mail_id.find("@")
			dotcom_pos=mail_id.find("com")
			sp=mail_id[symbol_pos+1:dotcom_pos-1]
			#print(sp)
			if sp in servicesavailable:
				return mail_id,sp
				break
			else:
				print("we don't provide service for",sp)
				print("we provide service for gmail yahoo hotmail outlook")
				continue
	
		else:
			print("invalid email type again")
			continue
def set_smtp_domain(serviceprovider):
	if serviceprovider=='gmail':
		return 'smtp.gmail.com'
	elif serviceprovider=='hotmail' or serviceprovider=='outlook':
		return 'smtp-mail.outlook.com'
	elif serviceprovider=='yahoo':
		return 'smtp.mail.yahoo.com'


print("welcome you can send emaik through this programme")
print("please enter email and password")

email,serviceprovider=get_mail()
print("your service provider",serviceprovider)
password=getpass.getpass("password:")
while True:
	smtpdomain=set_smtp_domain(serviceprovider)
	connection=smtplib.SMTP(smtpdomain,587)
	connection.ehlo()
	connection.starttls()
	connection.login(email,password)
	
print("eneter reciever email address")
recieveradd,recieversp=get_mail()
print("now please eneter subject and ,message")
sub=input("subject")
mes=input("message")

connection.sendmail(email,recieveradd,("Subject",sub,"\n\n","message",mes))
print("email send successful")
connection.quit()