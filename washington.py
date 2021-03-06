import time, json, re
import smtplib
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


config = json.loads(open('config.json').read())
delay = config['delay']
zipcode = str(config['washington']['zipcode'])
distance = config['washington']['distance']
sms_enabled = config['sms']['enabled']
if sms_enabled:
    sms_number = config['sms']['number']
gmail_userid = config['gmail']['userid']
gmail_password = config['gmail']['password']

options = Options()
options.add_argument('--headless')
server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login(gmail_userid, gmail_password)

while True:
    driver = webdriver.Chrome(config['chromeDriverPath'], options=options)  # Optional argument, if not specified will search path.
    # driver.set_window_size(1400, 800)
    driver.maximize_window()
    url = f'https://prepmod.doh.wa.gov/clinic/search?location={zipcode}&search_radius={distance}+miles&q%5Bvenue_search_name_or_venue_name_i_cont%5D=&clinic_date_eq%5Byear%5D=&clinic_date_eq%5Bmonth%5D=&clinic_date_eq%5Bday%5D=&q%5Bvaccinations_name_i_cont%5D=&commit=Search#search_results'
    driver.get(url)
    time.sleep(3) # Let the user actually see something!
    sites = driver.find_elements_by_class_name('justify-between')
    m = re.compile('^Available Appointments: ([0-9]+)$')
    total_available = 0
    msg = []
    for eachSite in sites:
        p = eachSite.find_elements_by_tag_name('p')
        if len(p) == 0:
            continue
        _t = p[8].text
        g = m.match(_t)
        try:
            available_appointments = int(g[1])
        except:
            print(f"ERROR : cannot parse {_t}")
        total_available = total_available + available_appointments
        if available_appointments > 0:
            _m = []
            _m.append(f"***** {datetime.now()} *****")
            _m.append(p[0].text)
            _m.append(p[1].text)
            _m.append(p[7].text)
            _m.append(_t)
            _m.append("=======================")
            print('\n'.join(_m))
            msg = msg + _m
    if total_available == 0:
        print(f"***** {datetime.now()} *****")
        print(f"No appointments available. Retry in {delay} seconds")
        print("=======================")
        time.sleep(delay)
    else:
        msg.append(url)
        if sms_enabled: 
            server.sendmail( 'VaccineFinder', sms_number, '\n'.join(msg) )
        print(url)
        print('text message sent!')
        print("=======================")

    driver.quit()
