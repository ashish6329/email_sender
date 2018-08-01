import smtplib
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.ehlo()
connection.starttls()
connection.login('ashishvarshney2k16@gmail.com','xxxxxxxxxxxxxxx')
connection.sendmail('ashishvarshney1996@rediffmail.com','ashishvarshney2k16@gmail.com','Subject:hello   \n\n  hi i am ashish')
connection.quit()