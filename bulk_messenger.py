from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os
import pyautogui
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--log-level=3")  # apenas erros fatais

service = Service(log_path="NUL")  # Windows
# service = Service(log_path="/dev/null")  # Linux / macOS

driver = webdriver.Chrome(service=service, options=options)  # Ensure you have chromedriver installed

numbers = pd.read_csv('form.csv')
numbers = numbers['Whatsapp'].to_list()
message = """📢 *Convite especial para a sociedade civil e empresas locais!* 🌱🏙️%0A
%0A
Um convite muito especial mesmo!%0A
%0A
É especial hein....%0A
%0A
💡 *APARECE PORQUE É ESPECIAL*%0A
%0A
📅 *Dia 08/09/2029, 14h*%0A
📍 Sala Florense | Bloco M - UCS Campus-Sede%0A
📌 *TRAGA PRESENTES*%0A
🎤 Música top hein hahahaha %0A
%0A
📄 Confira a programação completa da semana no nosso site: https://www.citylivinglab.com/eventos%0A
"""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
image_path = os.path.join(BASE_DIR, 'convite-de-aniversario-digital-ben-10-ben.webp')

driver.get("https://web.whatsapp.com/")
input("Press enter when Whatsapp has loaded") #Espera confirmação de que se conectou no whatsapp web

for number in numbers:
    attempts = 0
    while attempts < 3:
        attempts+=1
        try:
            url = f"https://web.whatsapp.com/send/?phone={number}&text=&type=phone_number&app_absent=0"
            driver.get(url)

            time.sleep(5)

            # # Click the attachment button (clip icon)
            attachment_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[3]/div/div[5]/div/footer/div[1]/div/span/div/div/div/div[1]/div/span/button')
            attachment_button.click()
            time.sleep(2)

            image_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[4]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]')
            image_button.click()
            time.sleep(2)

            # # Locate the file input element and upload the image
            # file_input = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[3]/div/div[5]/div/footer/input')
            # file_input.send_keys(image_path)
            # time.sleep(5)

            pyautogui.write(image_path, interval=0.02)
            pyautogui.press("enter")
            time.sleep(3)

            text_input = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[3]/div/div[3]/div[2]/div/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div/div[1]/div[1]')
            text_input.send_keys("Exemplo de Imagem")
            time.sleep(1)

            send_image_button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div/div[3]/div/div[3]/div[2]/div/span/div/div/div/div[2]/div/div[2]/div[2]/span')
            send_image_button.click()
            time.sleep(2)

            url = f"https://web.whatsapp.com/send/?phone={number}&text={message}&type=phone_number&app_absent=0"
            driver.get(url)
            time.sleep(7)
            send_button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div/div[3]/div/div[5]/div/footer/div[1]/div/span/div/div/div/div[4]/div/span/button')
            send_button.click()
            time.sleep(2)  # Allow message to send
            break
        except Exception as e:
            print(f'{number} got an error. This was attempt number {attempts}.\n{e}')

print("Success!")
driver.quit()