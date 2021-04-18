import time, json, re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


config = json.loads(open('config.json').read())
delay = config['delay']

options = Options()
options.add_argument('--headless')
while True:
    driver = webdriver.Chrome(config['chromeDriverPath'], options=options)  # Optional argument, if not specified will search path.
    # driver.set_window_size(1400, 800)
    driver.maximize_window()
    driver.get('https://prepmod.doh.wa.gov/clinic/search?location=98105&search_radius=50+miles&q%5Bvenue_search_name_or_venue_name_i_cont%5D=&clinic_date_eq%5Byear%5D=&clinic_date_eq%5Bmonth%5D=&clinic_date_eq%5Bday%5D=&q%5Bvaccinations_name_i_cont%5D=&commit=Search#search_results')
    time.sleep(3) # Let the user actually see something!
    sites = driver.find_elements_by_class_name('justify-between')
    m = re.compile('^Available Appointments: ([0-9]+)$')
    total_available = 0
    for eachSite in sites:
        p = eachSite.find_elements_by_tag_name('p')
        if len(p) == 0:
            continue
        _t = p[8].text
        g = m.match(_t)
        available_appointments = int(g[1])
        total_available = total_available + available_appointments
        if available_appointments > 0:
            print(f"***** {datetime.now()} *****")
            print(p[0].text)
            print(p[1].text)
            print(p[7].text)
            print(_t)
            print("=======================")
    if total_available == 0:
        print(f"***** {datetime.now()} *****")
        print(f"No appointments available. Retry in {delay} seconds")
        print("=======================")
        time.sleep(delay)
    driver.quit()
