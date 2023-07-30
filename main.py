from pathlib import Path
from robot import DolarRobot
import json

if __name__ == '__main__':
    url_t = 'https://melhorcambio.com/dolar-hoje'
    element_t = '//*[@id="comercial"]'
    sender = 'sender@email.com'
    sender_password = 'password_email_sender'
    receiver = 'email@email.com'
    robot = DolarRobot(url_t, element_t)
    robot.execute_robot()
    robot.sent_mail(sender, receiver, sender_password)
