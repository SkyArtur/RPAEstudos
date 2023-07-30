from pathlib import Path
from robot import DolarRobot
import json

if __name__ == '__main__':
    file_password = Path(__file__).resolve().parent.joinpath('files/user_data.json')
    url_t = 'https://melhorcambio.com/dolar-hoje'
    element_t = '//*[@id="comercial"]'
    with open(file_password, encoding='utf8') as file:
        data_user = json.load(file)
    receiver = 'email@email.com'
    robot = DolarRobot(url_t, element_t)
    robot.execute_robot()
    robot.sent_mail(data_user['email'], receiver, data_user['password'])
