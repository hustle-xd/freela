from telethon import events, Button
import requests
from .. import *
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.users import GetFullUserRequest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pickle

# Setup Chrome options to 
    #Disable the "enable-automation" flag.
    #Add the "no-sandbox" argument.
    #Add the "disable-infobars" argument.
    #Add the "disable-dev-shm-usage" argument.





def getlatlong(url):
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set the driver
    webdriver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    try:
        #navigate to login gmail
        driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&hl=en&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession")

        # Identify the user name text box and enter the value
        driver.find_element(By.ID, "identifierId").send_keys("pandeytanmay978@gmail.com")
        time.sleep(2)

        # Clicks on the 'Next' button and waits for 2 seconds.
        driver.find_element(By.XPATH, "//span[text()='Next']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, '//input[@name="Passwd"]').send_keys("#Techhackerz456")
        time.sleep(2)

        # Clicks on the 'Next' button again and waits for 2 seconds.
        driver.find_element(By.XPATH, "//span[text()='Next']").click()
        time.sleep(2)
    except:
        #navigate to login gmail
        driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&hl=en&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession")

        # Identify the user name text box and enter the value
        driver.find_element(By.ID, "identifierId").send_keys("pandeytanmay978@gmail.com")
        time.sleep(2)

        # Clicks on the 'Next' button and waits for 2 seconds.
        driver.find_element(By.XPATH, "//span[text()='Next']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, '//input[@name="Passwd"]').send_keys("#Techhackerz456")
        time.sleep(2)

        # Clicks on the 'Next' button again and waits for 2 seconds.
        driver.find_element(By.XPATH, "//span[text()='Next']").click()
        time.sleep(2)


    #Uncomment below code to close the browser  
    #driver.close()
    
    print(url)
    driver.get(url)
    time.sleep(10)  # Wait for the page to load
    
    current_url = driver.current_url
    print(f"Current URL: {current_url}")
    
    if '@' in current_url:
        lat_long = current_url.split('@')[1].split(',')[:2]  # Get the first two parts after '@'
        latitude = lat_long[0]
        longitude = lat_long[1]
        print(f"Latitude: {latitude}, Longitude: {longitude}")
    else:
        print("Latitude and longitude not found in the URL.")
    #Uncomment below code to close the browser  
    
    l = [latitude,longitude]
    return l

# getlatlong("https://maps.app.goo.gl/?link=https://www.google.com/maps/@/data%3D!4m5!7m4!1m2!1s111182088604195545388!2sEggHBiWhQToRNQ%253D%253D!2e2!13s110014786763043033193&apn=com.google.android.apps.maps&amv=949000000&ius=comgooglemapsurl&isi=585027354&ct=location-sharing-fdl&mt=8&pt=9008&ibi=com.google.Azimuth&ibi=com.google.Azimuth.MessagesExtension&ibi=com.google.Bzimuth&ibi=com.google.Bzimuth.MessagesExtension&ibi=com.google.Czimuth&ibi=com.google.Czimuth.MessagesExtension&ibi=com.google.Dzimuth&ibi=com.google.Dzimuth.MessagesExtension&ibi=com.google.Maps&ibi=com.google.Maps.MessagesExtension&ibi=com.google.Rzimuth&ibi=com.google.Rzimuth.MessagesExtension&afl=https://www.google.com/maps/@/data%3D!4m5!7m4!1m2!1s111182088604195545388!2sEggHBiWhQToRNQ%253D%253D!2e2!13s110014786763043033193&ifl=https://www.google.com/maps/@/data%3D!4m5!7m4!1m2!1s111182088604195545388!2sEggHBiWhQToRNQ%253D%253D!2e2!13s110014786763043033193")
    