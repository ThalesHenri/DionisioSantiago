import smtplib
#informações de envio
class EmailSender:
    def __init__(self):
        self.emailSender = "usCabaDrinks@gmail.com"
        self.emailReceiver = "empresadoth@gmail.com"
    def startserver(self):
        print("iniciando servidor...")
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(self.emailSender,"yfek ropp mnwe socm ")
        print("servidor inicado e logado com sucesso!.....")
    
    def sendMensage(self, subject, message):
        mail  = f"Subject: {subject}\n\n{message}"
        print("Capturando mensagem....")
        #encodando mensagem
        encodedMail = mail.encode('utf-8')
        self.server.sendmail(self.emailSender, self.emailReceiver, encodedMail)
        print(f"mensagem enviada do email {self.emailSender} para {self.emailReceiver}")