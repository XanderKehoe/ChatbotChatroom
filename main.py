import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Simple Program that logins into github provided username and password are correct
# then opens up cleverbot and enters a message

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/Xander/Downloads/chromedriver_win32/chromedriver.exe')
        self.driver.get("https://www.pandorabots.com/mitsuku/")
        self.driver.maximize_window()

        self.timeout = 10
        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/button'))
        WebDriverWait(self.driver, self.timeout).until(element_present)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/button').click()  # click login page button

    def getReponse(self):
        self.driver.implicitly_wait(10)
        message_box = self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[4]/div[2]/div')
        responses = message_box.find_elements_by_class_name('pb-bot-response')
        last_response = responses[len(responses) - 1]
        return last_response.text

    def sendNewResponse(self, message):
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/form/div[1]/input').send_keys(message + Keys.ENTER)


def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')



bot1 = Bot()
bot2 = Bot()

bot2.sendNewResponse("Which came first, the chick or the egg?")
time.sleep(10)
# print(bot2.getReponse())

bot1_response = ""
bot2_response = ""

while True:
    try:
        bot2_response = deEmojify(bot2.getReponse())
    except:
        bot2_response = bot1_response
    print("Bot 2: "+bot2_response)
    time.sleep(3)
    bot1.sendNewResponse(bot2_response)
    try:
        bot1_response = deEmojify(bot1.getReponse())
    except:
        bot1_response = bot2_response
    print("Bot 1: "+bot1_response)
    time.sleep(3)
    bot2.sendNewResponse(bot1_response)
