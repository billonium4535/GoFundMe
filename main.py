import time
import pywhatkit
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://gofund.me/92e65599"
driver = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver.exe")
running = False
total_donations = 16
new_donator = False


def get_info():
    global running
    output_data = []

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(url)
    if not running:
        driver.implicitly_wait(5)
        accept_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_button.click()
        running = True

    driver.refresh()
    donations = driver.find_element(By.XPATH, "//div[@class='mb2x show-for-large text-stat text-stat-title']").text
    total = driver.find_element(By.XPATH, "//p[@class='m-progress-meter-heading']").text
    donator = driver.find_element(By.XPATH, "//div[@class='hrt-avatar-lockup-content']").text
    top_donator = driver.find_element(By.XPATH, "(//div[@class='hrt-avatar-lockup-content'])[2]").text

    output_data.append(donations.split(" ")[0])
    output_data.append(total.split(" ")[0])
    output_data.append(donator.split("\n")[0])
    output_data.append(top_donator.split("\n")[0])

    return output_data


while True:
    information = get_info()

    if total_donations != int(information[0]):
        new_donator = True
        total_donations = int(information[0])
    else:
        new_donator = False

    if new_donator:
        print("Total Donations: {}\nTotal: {}\nLast Donator: {}\nTop Donator: {}".format(information[0], information[1], information[2], information[3]))
        # pywhatkit.sendwhatmsg_to_group_instantly("CFwqufEtE4X6sDiV8A7spg", "New Donation! Power 10!\n\nTotal Donations: {}\nTotal: {}\nLast Donator: {}\nTop Donator: {}".format(information[0], information[1], information[2], information[3]))

    time.sleep(60)
