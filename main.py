from robot import DolarRobot

if __name__ == '__main__':
    smtp_server = 'smtp.office365.com'
    port = 587
    sender = 'sender@email.com'
    sender_password = 'password_email_sender'
    receiver = 'email@email.com'
    robot = DolarRobot(url='https://melhorcambio.com/dolar-hoje', element='//*[@id="comercial"]')
    robot.execute_robot()
    robot.sent_mail(sender, receiver, sender_password, smtp_server, port)
