from datetime import datetime
import rpa
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class DolarRobot(object):
    date = datetime.today().strftime('%H:%M - %d/%m/%Y')

    def __new__(cls, *args, **kwargs) -> object:
        if not hasattr(cls, 'instance'):
            cls.instance = super(DolarRobot, cls).__new__(cls)
        return cls.instance

    def __init__(self: object, url: str, element: str) -> None:
        self.__url = url
        self.__element = element
        self.__rpa = rpa
        self.__email = 'Dolar Hoje: ${0} - {1}'
        self.__dolar = None
        self.__message = MIMEMultipart()

    def execute_robot(self) -> None:
        self.__rpa.init()
        self.__rpa.url(self.__url)
        self.__rpa.wait(2.5)
        self.__dolar = self.__rpa.read(self.__element)
        self.__rpa.wait(2.5)
        self.__rpa.close()

    @property
    def dolar_today(self) -> str:
        return self.__dolar

    def sent_mail(self, sender: str, receiver: str, password: str, smtp_server: str, port: int, /) -> None:
        """
        :param sender: Endereço de email do remente.
        :param receiver: Endereço de email do destinatário.
        :param password: Senha de email remetente.
        :param smtp_server: Servidor smtp. (default = outlook)
        :param port: Porta smtp. (default = 587)
        """
        self.__message['from'] = sender
        self.__message['To'] = receiver
        self.__message['Subject'] = 'Cotação do dolar.'
        self.__message.attach(MIMEText(self.__email.format(self.dolar_today, self.date)))
        session = smtplib.SMTP(smtp_server, port)
        session.starttls()
        session.login(sender, password)
        session.sendmail(sender, receiver, self.__message.as_string())
        session.quit()
