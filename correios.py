from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

import telebot
TOKEN = "seu token"
bot = telebot.TeleBot(TOKEN)
options = webdriver.ChromeOptions()#executar hidden
options.add_argument("--headless")
driver = webdriver.Chrome(executable_path='caminho webdriver',chrome_options=options)

vazio=[]

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def process_rastreio(message):
    driver.get(f"https://www.linkcorreios.com.br/?id={message.text}")#NL262847644BR
    rows = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/main/div[4]/div/div/div[1]/div/div/ul/li[1]/b')
    rows2 = driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/main/div[4]/div/div/div[1]/div/div/ul/li[2]')
    if  rows != vazio:
        for row in rows:
            descricao=(row.text)
        for row in rows2:
            hora=(row.text)
        messageText = f'Status:{descricao}, {hora}'
        bot.send_message(message.chat.id, messageText)
    else:
        bot.send_message(message.chat.id, 'Rastreio não encontrado')

bot.polling()
