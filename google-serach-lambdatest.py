#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import time
import multiprocessing
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from browserstack.local import Local
import urllib3
import sys
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.options import Options

def call():
    platform = "desktop"
    
    if platform=="desktop":
        desired_cap = {
            "browserName":"Chrome",      #Chrome, MicrosoftEdge
            "console": True,
            "build": "Idle Timeout issue",
            "name" : "Test 1",
            "version":"latest",                   #88.0
            "enableNetworkThrottling":False,
            #"forceUpdate":True,
            "headless":False,
            "network": False,
            #"performance":False,
            "platform": "Windows 10",       #MacOS Big sur, Windows 10
            "platformName": "Windows 10",
            "resolution":"1024x768", 
            #"selenium_version":"4.0.0-beta-3",
            #"tunnel": True,
            #"tunnelIdentifier":"",
            #"fixedIP": "10.80.16.19",                          #"10.81.97.228"
            "video":True,
            'goog:chromeOptions': {'extensions': [], 'args': ['--log-level=3']},
            "visual":True,
            "w3c":True
        }
    #    desired_cap = {
    #         "acceptInsecureCerts":True,
    #         "acceptSslCerts":True,
    #         "browserName":"safari",
    #         "build":"React Wayforward App Smoke Tests Bundle Fixed IP",
    #         "console":"true",
    #         "enableNetworkThrottling":False,
    #         "extendedDebuging":True,
    #         "headless":False,
    #         "idleTimeout":"180",
    #         "loggingPrefs":{
    #             "browser":"ALL",
    #             "driver":"ALL",
    #             "server":"ALL"
    #         },
    #         "name":"React Wayforward App test_signup_wld_sso cascade",
    #         "network":True,
    #         "network.full.har":True,
    #         "network.har":True,
    #         "performance":False,
    #         "platform":"macos 11.0",
    #         "resolution":"1280x1024",
    #         "safari.cookies":True,
    #         #"tunnel":True,
    #         "version":"latest.0",
    #         "video":True,
    #         "visual":False,
    #         "w3c":True,
    #         "fixedIP": "10.242.32.62", #10.242.32.146, 10.242.32.152, 10.242.32.147, 10.242.32.62
    #     }
    elif platform=="mobile":
        desired_cap = { 
            "build" : "iOS device testing 14.5",
            "name" : "Test",    # 
            "platformName" : "iOS",
            "deviceName" : "iPhone 12", # 
            "platformVersion":"14.4",
            "fixedIP":"10.92.181.43",          #23.105.12.40(Android), (10.242.32.103)ios  (23.105.12.36)android prod
            "appiumVersion":"1.21.0",
            #"fixedPort":"8000",
            #"console": "warn",
            #"network": True,
            #"browserName" : "Chrome",
            #"tunnel": True,
            #'isRealMobile' : True,
            #"orientation": "",
            #"deviceOrientation": "",
            #"chromedriverArgs": "disable-web-security",
        }
    #STAGE 
    # url = "https://divyanks:i1dGEHcw7jov92lkSz1pajKv4XLFde4Jd6IgMiUGZFKoaRAq8r@stage-hub.lambdatest.com/wd/hub"
    #STAGE FREEMIUM
    #url = "https://divyank-1:pOR8MLXkVNJySDQFRgeGT3RoTMVSUcebv4MCmwAILnY7WQVKSO@stage-hub.lambdatest.com/wd/hub"
    #PRODUCTION
    url = "https://divyanks:XFSP1IqZMWTXUC1iwbVqFCClLX654vuFg8OZUMyCfwbfygavq1@hub.lambdatest.com/wd/hub"
    #url = "https://divyanks:XFSP1IqZMWTXUC1iwbVqFCClLX654vuFg8OZUMyCfwbfygavq1@hub-ohio.lambdatest.com/wd/hub"
    #PROD FREEMIUM
    #url = "https://divyank-1:24yC7K6WqX4oQztJJNQub5mJzMd3vg5qo9IC0Oe2t8wwZn5jFg@hub-ohio.lambdatest.com/wd/hub"
    #PROD BROWSERSTACK
    #url = "https://falconmagicleap_vci1oa:JxzszpGVzPndo6ySxp3r@hub-cloud.browserstack.com/wd/hub"
    #url = "https://divyank31:QAN5BKWJaP7zh5p5yalMBM5jRz4AA094G0osRrbShUGIvpnF4v@hub.lambdatest.com/wd/hub"
    #DEV ENV
    #url = "https://divyanks:i1dGEHcw7jov92lkSz1pajKv4XLFde4Jd6IgMiUGZFKoaRAq8r@hub.divyank-commandlogs.dev.lambdatest.io/wd/hub"
    #url = "https://divyanks:i1dGEHcw7jov92lkSz1pajKv4XLFde4Jd6IgMiUGZFKoaRAq8r@hub.divyank-14-sep.dev.lambdatest.io/wd/hub"
    
    #BrowserStack
    #url = "https://divyanksingh1:CNnn3B4jqfsEFKbcJYyp@hub-cloud.browserstack.com/wd/hub"   #LT
    #url = "https://divyanksingh_mwxB5t:37ZZgnXZksNUysXFSyYk@hub-cloud.browserstack.com/wd/hub"      #personal
    #webhook
    #url = "https://webhook.site/1c1fb21c-5fcb-4dcc-9ea5-920e8e28b852"

    # #creates an instance of Local
    # bs_local = Local()

    # bs_local_args = { "key": "37ZZgnXZksNUysXFSyYk" }

    # #starts the Local instance with the required arguments
    # bs_local.start(**bs_local_args)

    # #check if BrowserStack local instance is running
    # print(bs_local.isRunning())


    # print(url)
    # start_time = time.time()
    # print(desired_cap)

    
    # chrome_options = ChromeOptions()
    # # chrome_options.add_extension("/Users/applemd1011/Downloads/LambdaDemo/chrome.zip")
    # chrome_options.add_argument("--log-level=3")
    # create new Chrome driver object with Chrome extension
    # driver = webdriver.Chrome(chrome_options=chop)

    
    
    # desired_cap.update(chrome_options.to_capabilities())
    # print(desired_cap)
    driver=webdriver.Remote(desired_capabilities=desired_cap,command_executor=url)
    
    # print("setup time {0} secs".format((time.time() - start_time) % 60))
    #driver.get("http://localhost:3000/")
    #time.sleep(5)
    print(driver.session_id)
    driver.get("https://mylocation.org/")
    driver.get("https://www.whatismybrowser.com/")
    #time.sleep(10)
    print("=============1===========")
    driver.get("https://www.google.com/")
    #time.sleep(60)
    driver.get("https://www.halowaypoint.com/en-us/games/halo-infinite")
    print("=============2===========")
    #time.sleep(60)
    driver.get("https://www.serverless.com/blog/cors-api-gateway-survival-guide")
    # driver.implicitly_wait(20)
    try :
        driver.find_element_by_id("divyank")
    except :
        pass
    #time.sleep(30)
    driver.get("https://en.wikipedia.org/wiki/Halo_Infinite")
    print("=============3===========")
    #time.sleep(30)
    driver.get("https://www.thrillophilia.com/best-mountain-trek-in-india")
    #time.sleep(60)
    driver.get("https://indiahikes.com/")
    print("=============4===========")
    driver.get("https://google.com/")
    #time.sleep(150)
    #driver.delete_all_cookies()
    #driver.clear_session_storage()
    #Tunnel
    # driver.get("http://localhost:8888/")
    # driver.get("http://localhost:8888/Test Scripts/")
    # driver.get("http://localhost:8888/Test Scripts/hashing/")
    # driver.get("http://localhost:8888/Test Scripts/local/")
    # driver.get("http://localhost:8888/Test Scripts/local/kafka/")
    # driver.get("http://localhost:8888/Go-Projects/")
    # driver.get("http://localhost:8888/Go-Projects/logging/")


    #Web Sockets
    # driver.get("https://www.websocket.org/echo.html")
    # print("=============1===========")
    # driver.find_element_by_id("connect").send_keys(Keys.ENTER)
    # print("=============2===========")
    # driver.find_element_by_id("send").send_keys(Keys.ENTER)
    # print("=============3===========")
    # driver.find_element_by_id("sendMessage").send_keys("Testing Web Sockets!!!")
    # print("=============4===========")
    # driver.find_element_by_id("send").send_keys(Keys.ENTER)
    # print("=============5===========")

    #driver.find_element_by_id("send").send_keys(Keys.ENTER)

    # driver.get("https://www.python.org/")
    # #driver.findElement(By.id("copy_to_clip")).click();
    # element = driver.find_element_by_xpath("//*[@id=\"dive-into-python\"]/ul[2]/li[1]/div[2]/h1")
    # element.send_keys(Keys.CONTROL + "a")
    # driver.implicitly_wait(3)
    # element1 = driver.find_element_by_xpath("//*[@id=\"dive-into-python\"]/ul[2]/li[4]/div[1]/pre/code")
    # element1.send_keys(Keys.CONTROL + "c")
    # element2 = driver.find_element(By.name("q"))
    # element2.send_keys(Keys.CONTROL + "v")
    # driver.implicitly_wait(3)


    #driver.execute_script("lambda-status=failed")
    #time.sleep(60)
    # driver.get("https://www.trekbikes.com/in/en_IN/bikes/mountain-bikes/c/B300/")
    # #time.sleep(60)
    # driver.get("https://www.lonelyplanet.com/articles/best-treks-in-the-world")
    # #time.sleep(60)
    # driver.get("https://www.adventurenation.com/activity/trekking")
    # #time.sleep(60)
    # driver.get("https://www.intrepidtravel.com/adventures/trekking-training-guide-tips/")
    # time.sleep(60)
    # print(driver.execute_script("lambda-perform-keyboard-events:^p")) #for CTRL+P
    # time.sleep(5)
    # print(driver.execute_script("lambda-perform-keyboard-events:{ENTER}")) #pressing ENTER
    # time.sleep(2)
    # print(driver.execute_script("lambda-perform-keyboard-events:demo-testing-keystroke.pdf"))  #inserting charcters
    # time.sleep(2)
    # print(driver.execute_script("lambda-perform-keyboard-events:{ENTER}"))

    start_time = time.time()
    driver.quit()
    print("quit time {0} secs".format((time.time()-start_time) % 60))
    #stop the Local instance
    #bs_local.stop()

if __name__ == '__main__':
    jobs = []
    for i in range(1):
        p = multiprocessing.Process(target=call)
        jobs.append(p)
        p.start()

