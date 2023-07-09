# Скрипт который определяет удаленное подключения и информирует в телеграм предоставляя информацию о имени пользователя, который подключился, ip адрес с которого было совершено подключение и по какому порту. Вписать TOKEN и chat_id
import psutil
import telebot
import time

# Впишите токен вашего бота (в правильном формате)
TOKEN = 'Токен_Вашего_Бота'

# Список портов, которые будем прослушивать
PORTS = [20, 21, 22, 23, 5900, 5901]

bot = telebot.TeleBot(TOKEN)

# Получаем имя пользователя и IP адрес с которого идет удаленное подключение
username = ''
remote_ip = ''
users = psutil.users()
if users: # Проверяем, что список users не пустой
    username = users[0].name
for conn in psutil.net_connections(kind='inet'):
    if conn.status == 'ESTABLISHED' and conn.laddr.port in PORTS:
        remote_ip = conn.raddr.ip

def check_connections():
    """Проверяем текущие соединения"""
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'ESTABLISHED' and conn.laddr.port in PORTS:
            # Отправляем сообщение в Telegram
            message = f"Внимание! \nПроизошло удаленное подключение!\nПользователь: {username}\nIP адрес: {remote_ip}\nПорт: {conn.laddr.port}"
            bot.send_message(chat_id='ID Чата', text=message)

while True:
    check_connections()
    time.sleep(60) # Время запуска в секундах




