import smtplib as s 

k=s.SMTP("smtp.gmail.com",587)
k.ehlo()
k.starttls()
k.login("krishchudasma07@gmail.com","krish@1640")
subject="test python"
body="i love python"
massage="subject:{}\n\n{}".format(subject,body)
listadd=["krishchudasma111@gmail.com"]
k.sendmail("krishchudasma07@mail.com",listadd,massage)
print("send mail")
k.quit()