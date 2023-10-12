from selenium import webdriver
#from selenium.webdriver.chrome.options import Options #selenium < 4
from selenium.webdriver.chrome.service import Service as ChromeService #selenium >= 4
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
from random import randint
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
import os


#options = Options() #selenium < 4
options = webdriver.ChromeOptions() #>= 4
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
#options.add_argument("--user-data-dir=/home/iamelvri/Desktop/Projects/chrome_user_data")  #Linux
options.add_argument("--user-data-dir=D:\Projects\whatsapp-blast\chrome_user_data") #Windows

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.BLUE)
print("**********************************************************")
print("**********************************************************")
print("*****                                               ******")
print("*****               WHATSAPP BLAST by ELF           ******")
print("*****                                               ******")
print("*****                                               ******")
print("*****                                               ******")
print("**********************************************************")
print("**********************************************************")
print(style.RESET)

startelapse = datetime.now()

Title = 'Blast WA For sales 12 Oct 2023'
#FilePath = 'blablabla.xlsx'
FilePath = ''
#FilePathSummary = 'blablabla.jpg'
FilePathSummary = 'D:\Projects\whatsapp-blast\example.jpg'
f = open("message.txt", "r", encoding="utf8")
message = f.read()
f.close()


print(style.YELLOW + '\nThis is your message-')
print(style.GREEN + message)
print("\n" + style.RESET)
message = quote(message)


numbers = []
f = open("listofnumbers.txt", "r")
for line in f.read().splitlines():
	if line.strip() != "":
		numbers.append(line.strip())
f.close()
total_number=len(numbers)
print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)
delay = 30


failed_list = []
failed_list.append("\n"+"**********************************************************")
failed_list.append(Title+" "+startelapse.strftime('%Y-%m-%d %H:%M:%S.%f'))


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options) #selenium >= 4
#driver = webdriver.Chrome(ChromeDriverManager().install(), options=options) #selenium < 4
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)
for idx, number in enumerate(numbers):
	number = number.strip()
	if number == "":
		continue
	print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx+1), total_number, number) + style.RESET)
	try:
		url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
		sent = False
		for i in range(3):
			if not sent:
				driver.get(url)
				try:
					#click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']"))) #old version wa web
					click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']")))
				except Exception as e:
					
					#file_box = driver.find_element_by_xpath("//input[@accept='*']")
					print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/3)")
					print("Make sure your phone and computer is connected to the internet.")
					print("If there is an alert, please dismiss it." + str(e) + style.RESET)
					if (i+1)==3:
						failed_list.append(number) #failed number will be listed

					try:
						#div_elem = driver.find_element_by_xpath("//div[@data-testid='popup-contents']")  #selenium < 4
						div_elem = driver.find_element(By.XPATH,"//div[@data-testid='popup-contents']")  #selenium >= 4

						div_value = div_elem.text

						print(style.RED + div_value + style.RESET)
					except NoSuchElementException:
						print("Error: Could not find div element")

				else:
					sleep(1)
					click_btn.click()
					sent=True
					sleep(3)
					print(style.GREEN + 'Message sent to: ' + number + style.RESET)
					#To send attachments
					
					if FilePath != '':

						#click_btn1 = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='clip']")))  #old version wa web
						click_btn1 = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='attach-menu-plus']")))
						click_btn1.click()
						
						#file_box = driver.find_element_by_xpath("//input[@accept='*']") #selenium < 4
						file_box = driver.find_element(By.XPATH,"//input[@accept='*']") #selenium >= 4
						file_box.send_keys(FilePath)

						#click_btn2 = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='send']"))) #old version web wa
						click_btn2 = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']")))
						click_btn2.click()

						sleep(1)

						print(style.GREEN + 'Attachment sent to: ' + number + style.RESET)

					if FilePathSummary != '':
						
						#click_btnsum1 = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='clip']"))) #old version wa web
						click_btnsum1 = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='attach-menu-plus']")))
						click_btnsum1.click()
						
						#file_boxsum = driver.find_element_by_xpath("//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']") #selenium < 4
						file_boxsum = driver.find_element(By.XPATH,"//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']") #selenium >= 4
						file_boxsum.send_keys(FilePathSummary) 
						
						#click_btnsum2 = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='send']"))) #old version wa web
						click_btnsum2 = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']")))
						click_btnsum2.click()

						sleep(1)

						print(style.GREEN + 'Summary image sent to: ' + number + style.RESET)
					
	except Exception as e:
		print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)
	dly = randint(1,5)
	print("Sleep Time " + str(dly) + " s")
	sleep(dly)


elapsed_time = datetime.now() - startelapse
elapsed_days = elapsed_time.days
elapsed_seconds = elapsed_time.seconds
elapsed_microseconds = elapsed_time.microseconds
elapsed_milliseconds = elapsed_microseconds // 1000
elapsed_hours = elapsed_seconds // 3600
elapsed_minutes = (elapsed_seconds % 3600) // 60
elapsed_seconds = elapsed_seconds % 60


failed_list.append(f"Elapsed Time: {elapsed_days} days, {elapsed_hours} hours, {elapsed_minutes} minutes, {elapsed_seconds} seconds, {elapsed_milliseconds} milliseconds")

# Open the file in append mode
with open("failednumber.txt", "a") as file:
    # Iterate through the list and write each element to the file
    for item in failed_list:
        file.write(item + "\n")
	
driver.close()
