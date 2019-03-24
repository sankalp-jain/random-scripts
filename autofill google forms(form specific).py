from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint


driver = webdriver.Chrome()
driver.set_window_size(1024, 768)

from getpass import getpass
urls = ['https://docs.google.com/forms/d/e/1FAIpQLSc6Z0o47WvXbMS5A-w3-qmcxVttIyENtHjOmL2M2wUYstF9Tw/viewform']
driver.get(urls[0])

def genRandom(n):
    return randint(0, n - 1)


ques = {
	1 : ['  i5','  i8','  i11'],
	2 : ['  i18','  i21','  i24'],
	3 : ['  i31','  i34','  i37'],
	4 : ['  i44','  i47','  i50'],
	5 : ['  i57','  i60','  i63'],
	6 : ['  i70','  i73','  i76'],
	7 : ['  i83','  i86','  i89'],
	8 : ['  i96','  i99','  i102'],
	9 : ['  i109','  i112','  i115'],
	10 : ['  i122','  i125','  i128'],
	11 : ['  i135','  i138','  i141'],
	12 : ['  i148','  i151','  i154'],
	13 : ['  i161','  i164','  i167'],
	14 : ['  i174','  i177','  i180'],
	15 : ['  i187','  i190','  i193'],
	16 : ['  i200','  i203','  i206'],
	17 : ['  i213','  i216','  i219'],
	18 : ['  i226','  i229','  i232'],
	19 : ['  i239','  i242'],
	20 : ['  i249','  i252','  i255','  i258']
}

print(ques)
c = 0
while(c < 30):
    urls = ['https://docs.google.com/forms/d/e/1FAIpQLSc6Z0o47WvXbMS5A-w3-qmcxVttIyENtHjOmL2M2wUYstF9Tw/viewform']
    driver.get(urls[0])

    for i in range(len(ques)):
        n = genRandom(len(ques[i + 1]))
        print(n)
        sleep(2)
        driver.find_element_by_xpath("//div[@aria-describedby='" + ques[i + 1][n] + "']").click();

    driver.find_element_by_class_name("freebirdFormviewerViewNavigationSubmitButton").click();

    c += 1
    sleep(5)

