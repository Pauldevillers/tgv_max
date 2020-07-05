import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import sys
from twilio.rest import Client
import subprocess

from selenium.webdriver.chrome.options import Options

#!/usr/bin/python

import sys




# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACe454db59a052ba8d013e3cd8d8fab74e'
auth_token = '70e36b2533087b3fd3177ab6220917f8'


class Person:
  def __init__(self, email, password,numero):
    self.email = email
    self.password = password
    self.numero=numero


  def login(self):
    time.sleep(2)
    driver.find_element_by_css_selector('a._i1uq3v3').click()
    time.sleep(2)
    name=driver.find_element_by_name('email')
    name.send_keys(self.email)
    time.sleep(2)
    password=driver.find_element_by_name('password')
    password.send_keys(self.password)
    driver.find_element_by_css_selector('button.jsx-3821812987').click()

    



    


class Voyages:
    def __init__(self,from_city,to_city,hours_departure,min_departure,day_departure,month_departure,Person):
        self.from_city=from_city
        self.to_city=to_city
        self.hours_departure=hours_departure
        self.min_departure=min_departure
        self.day_departure=day_departure
        self.month_departure=month_departure
        self.numero=Person.numero
    def choose_trip(self):
        
            wait = WebDriverWait(driver, 10)
            depart= wait.until(lambda driver: driver.find_element_by_id("from.text"))

           
            time.sleep(2)
            depart.send_keys(self.from_city)
            depart.send_keys(Keys.RETURN)

            arrive=driver.find_element_by_id('to.text')
            time.sleep(2)
            arrive.send_keys(self.to_city)
            arrive.send_keys(Keys.RETURN)
            time.sleep(2)
        
    def choose_calendar(self):
        driver.find_element_by_id('page.journeySearchForm.outbound.title').click()
        time.sleep(2)
        driver.find_element_by_id('page.journeySearchForm.outbound.title%s-%s'%(self.month_departure,self.day_departure)).click()
        time.sleep(2)
    def choose_time(self):
        select_hours = Select(driver.find_element_by_name('hours'))
        select_hours.select_by_visible_text(self.hours_departure)
        time.sleep(2)
        select_minutes = Select(driver.find_element_by_name('minutes'))
        select_minutes.select_by_visible_text(self.min_departure)
        time.sleep(5)
        driver.find_element_by_css_selector('button._h9fi920').click()
        time.sleep(2)

    def get_data(self):
        time.sleep(5)
        prix=driver.find_element_by_class_name('_tlvyrl')
        time.sleep(2)
        
        
        if prix.text=='$0.00':
            client = Client(account_sid, auth_token)

            client.messages \
                        .create(
                            body="TGV MAX AVAILABLE for trip  %s to %s on %s/%s"%(self.from_city,self.to_city,self.day_departure,self.month_departure),
                            from_='+12029335294',
                            to='%s'%(self.numero)
                        )
            #subprocess.check_output("crontab test.cron",shell=True)
            #subprocess.check_output('crontab -r | at now + 1 hour',shell=True)
            
        else:
            print('pas dispo')

subprocess.check_output('killcall chrome')
print('begin')  
#subprocess.check_output("kill -9 $(ps -x | grep chrome)",shell=True)
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

#driver = webdriver.Chrome('/Users/pauldevillers/Desktop/chromedriver')
time.sleep(2)
driver.get('https://www.thetrainline.com/')
time.sleep(2)
print('adding a person')
p1 = Person("", "","")
print('login')
p1.login()



new_trip=Voyages(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[5]),str(sys.argv[6]),str(sys.argv[3]),str(sys.argv[4]),p1)
print('searching for this trip..')
time.sleep(30)

new_trip.choose_trip()
print('adding dates..')
new_trip.choose_calendar()
print('adding time')
new_trip.choose_time()
print('getting the data ')
new_trip.get_data()




      














   
    




    
    


    












