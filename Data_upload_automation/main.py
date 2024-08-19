from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import json
data = json.load(open('out2.json', encoding='utf8'))['questions']

driver  = webdriver.Chrome()

driver.get()

driver.maximize_window()
time.sleep(1)


driver.find_element(By.XPATH, '//*[@id="form2Example1"]').send_keys('goylerov04@gmail.com')
driver.find_element(By.XPATH, '//*[@id="form2Example2"]').send_keys('pX87\'Q!5=Z,u')
driver.find_element(By.XPATH, '/html/body/div/main/div/div/div/form/button').click()
time.sleep(3.6)


###############################################################################################################################################
uzunluq = len(data)
p = 15
while p < uzunluq:
    print(p)
    driver.find_element(By.XPATH, '//*[@id="question_add_btn"]').click()
    time.sleep(2)
    dropdown = driver.find_element(By.XPATH , '//*[@id="categories"]/select')
    x = Select(dropdown).select_by_visible_text("Development")
    time.sleep(1)

    dropdown = driver.find_element(By.XPATH , '//*[@id="subcategories"]/select')
    x = Select(dropdown).select_by_value("4cac6efd-17e0-4942-b354-4513874186ed")
    time.sleep(1)

    dropdown = driver.find_element(By.XPATH , '/html/body/div[1]/main/div/div[3]/div/div[1]/div[1]/div[3]/div[1]/select')
    x = Select(dropdown).select_by_value("f7eb6641-445c-430c-bf7b-c479dae7b4c4")
    time.sleep(1)


    dropdown = driver.find_element(By.XPATH , '//*[@id="levels"]/select')
    x = Select(dropdown).select_by_visible_text(data[p]["level"])
    time.sleep(1)

    driver.find_element(By.XPATH ,'/html/body/div[1]/main/div/div[3]/div/div[1]/div[2]/textarea[1]').send_keys(data[p]["question_text"])
    time.sleep(1)

    for cavab in data[p]["answers"]:
        if cavab["is_correct"] == 'true':
            driver.find_element(By.XPATH ,'/html/body/div[1]/main/div/div[3]/div/div[1]/div[2]/textarea[2]').send_keys(cavab["answer_description"])
            time.sleep(1)
            break

        

    l = len(data[p]["answers"])
    z = 0
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")    
    time.sleep(1)
    add_opt = driver.find_element(By.XPATH ,'/html/body/div[1]/main/div/div[3]/div/div[1]/div[2]/button')
    while z<l:
        
        
        add_opt.click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")    
        time.sleep(1)

        driver.find_element(By.XPATH ,f'/html/body/div[1]/main/div/div[3]/div/div[1]/div[2]/div[{z + 1}]/div[2]/textarea[1]').send_keys(data[p]["answers"][z]["answer_text"])
        # time.sleep(1)

        driver.find_element(By.XPATH ,f'/html/body/div[1]/main/div/div[3]/div/div[1]/div[2]/div[{z + 1}]/div[2]/textarea[2]').send_keys(data[p]["answers"][z]["answer_description"])
        time.sleep(1)

        if (data[p]["answers"][z]["is_correct"]) == 'true':
            driver.find_element(By.XPATH ,f'/html/body/div[1]/main/div/div[3]/div/div[1]/div[2]/div[{z + 1}]/div[2]/input').click()
            time.sleep(1)    
        
        z = z + 1
    driver.find_element(By.XPATH ,'/html/body/div[1]/main/div/div[3]/div/div[2]/button[2]').click()
    time.sleep(3)
    
    p = p + 1
driver.quit()