import time, json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

config = json.loads(open('config.json').read())
delay = config['delay']
while True:
    driver = webdriver.Chrome(config['chromeDriverPath'])  # Optional argument, if not specified will search path.
    # driver.set_window_size(1400, 800)
    driver.maximize_window()
    driver.get('https://mho.sutterhealth.org/');
    time.sleep(1) # Let the user actually see something!
    online_id = driver.find_element_by_id('online-id-form')
    online_id.send_keys(config['sutter']['userid'])
    password = driver.find_element_by_id('password-form')
    password.send_keys(config['sutter']['password'])
    signin_btn = driver.find_element_by_class_name('cta--form-submit.teal.js-dashboard-sign-in')
    signin_btn.click()

    time.sleep(delay * 2) # it seems this page sometimes need more time.  increase the delay.
    driver.find_element_by_xpath('//*[@id="links"]/a[2]').click()

    time.sleep(delay)
    driver.find_element_by_xpath('//*[@id="LQL_svU0KbYdMl9OVZBvT+uFDA==_1"]').click()
    driver.find_element_by_xpath('//*[@id="LQL_EExHV2uxeb5PW7nmL1JnGg==_5"]').click()
    driver.find_element_by_xpath('//*[@id="next-step"]').click() # proceed to next page

    time.sleep(delay)
    # driver.find_element_by_xpath('//*[@id="LQL_g9n4TlB7VSMvVVmuCi5r/w==_10"]').click()
    driver.find_element_by_xpath('//*[@id="LQL_g9n4TlB7VSMvVVmuCi5r/w==_1"]').click()
    driver.find_element_by_xpath('//*[@id="LQL_0D02j4T9UiZWAcD6abv9YQ==_1"]').click()
    driver.find_element_by_xpath('//*[@id="next-step"]').click() # proceed to next page

    # skip following due to previous page choices
    #time.sleep(delay)
    #driver.find_element_by_xpath('//*[@id="LQL_uxCOQHNIY+IXYANPoxHhJw==_1"]').click()
    #driver.find_element_by_xpath('//*[@id="questionform"]/div[2]/input').click() # proceed to next page

    time.sleep(delay)
    driver.find_element_by_xpath('//*[@id="LQL_RgEm6XD4rMEAB2wDsVz8xA==_1"]').click()
    driver.find_element_by_xpath('//*[@id="LQL_J6kVWdN36hEAidaOkPL2Ig==_1"]').click()
    driver.find_element_by_xpath('//*[@id="LQL_PSXl9st+MlbPZMBG1tZNDQ==_1"]').click()
    driver.find_element_by_xpath('//*[@id="LQL_rK/N8sMtygk/NV80AYYURw==_1"]').click()
    driver.find_element_by_xpath('//*[@id="LQL_x77HwN5T4VHjd2TBcEwIgw==_1"]').click()
    driver.find_element_by_xpath('//*[@id="LQL_ReDtqQRDiSbT6KOrItAOMw==_1"]').click()
    driver.find_element_by_xpath('//*[@id="LQL_2rfUQXcgyTiA05NnsuYWzg==_1"]').click()
    driver.find_element_by_xpath('//*[@id="next-step"]').click()

    time.sleep(delay)
    driver.find_element_by_xpath('//*[@id="LQL_vulxIKNBu33Jr/Z/0utMAQ==_1"]').click()
    driver.find_element_by_xpath('//*[@id="next-step"]').click()

    time.sleep(delay)
    driver.find_element_by_xpath('//*[@id="scheduling-workflow"]/div[7]/div[1]/div/div[2]/div/a[1]').click()
    driver.find_element_by_xpath('//*[@id="scheduling-continue"]').click()

    # it should now show the appointment availability page
    time.sleep(delay * 10) # Change the factor here to allow enough time for appointments to load
    driver.quit()
