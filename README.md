# Zen
This is a collection of webbots that crawl sites to look for COVID vaccine appointments.
Only Sutter Health is supported currently, but it can be extended easily to support other sites.

4/18/21 - added Washington state mass vaccination site support

# Installation
* Install python3 in your system.  
  * For MacOS, follow this link https://docs.python-guide.org/starting/install3/osx/
* create virtual environment in the cloned directory 
```
$ cd /path/to/<clonedDirectory>
$ python3 -m venv venv
```
* start the virtual environment
```
$ source venv/bin/activate
```
* install the required packages
```
$ pip3 install -r requirements.txt
```
* download ChromeDriver with the version that matches your Chrome browser version
  * follow this link https://chromedriver.chromium.org/downloads
  * For MacOS, remove quarantine for chromdriver
  ```
  xattr -d com.apple.quarantine /path/to/your/chromedriver
  ```
* prepare config.json
```
$ cp config.json.template config.json
```
* update your credential and the chromeDriver path in config.json
  * **sutter section** : provide your credential if you plan to use sutter vaccine registration
  * **Washington section**: update your zip code, and the distance (25, 50, 100)
  * **sms and gmail section**: currently only applied to Washington.  
    * For gmail app password, you can create one in google account.  
    * example of sms number: 1234567890@txt.att.net
```json
{
    "sutter": {
        "userid": "yourvalue",
        "password": "yourvalue"
    },
    "washington": {
        "zipcode": 12345,
        "distance": 50
    },
    "chromeDriverPath": "yourpathtochromedriver",
    "delay": 2,
    "sms": {
        "enabled": true,
        "number": "<yourPhoneNumber>@<yourTelcoMessageGateway"
    },
    "gmail": {
        "userid": "yourGmailAddress",
        "password": "yourGoogleAppPassword"
    }
}

```
# adjust the webbot script
Each script is highly customized to the latest state of the site page layout and the options provided.  XPath is used to identify the elements such as answers to your medical conditions to declare your elibility for a vaccine appointment.  You need to adjust the options by using `chrome > developer tool`, CTRL-F and type in the xpath element to locate the options picked and make adjustment for your own answer choice accordingly.  

# Run
## Sutter only
Execute the corresponding health provider site webbot script, it will show the appointments and pause for the delay time * N, where N is hardcoded in the script and you can adjust if needed.   During the pause time, 
1. if the page shows appointments that you like, press CTRL-C in the terminal that runs the script to terminate and directly make the appoinment in the browser.  Choose **Cancel** when the browser asks you to `cancel` or `Leave`.   Make sure to act fast terminating the python process as it will refresh the appointments once the timer hits.
2. if no appointment is shown or the appointments shown is not what you like, you can let the script to terminate the browser after the pause time expires and the whole process will start over again  infinitely.
3. You can terminate the infinite loop in 2) by CTRL-C in the terminal running the script.  Remember to close the browser opened by the script. 
```
$ python sutter.py
```
## Washington state only
Execute the corresponding script.  It will show vaccination sites and number of available appointments.  If there is no available appointments, it will wait and restart again after a brief delay.

Press CTRL-C to terminate the script anytime.

When you spot appointments of use, copy the Washington state vaccine locator displayed in the terminal to a browser and start registering and booking.


```
$ python washington.py
```
### Sample output with appointment available
```
=======================
***** 2021-04-18 11:46:19.116458 *****
Arlington Airport Covid-19 Vaccine Site on 04/19/2021
4226 188th St NE, Arlington WA, 98223
Clinic Hours : 09:00 am - 04:00 pm
Available Appointments: 5
=======================
<Full search site url will be shown here if there is appointment availability>
=======================
```

### Sample output with no appointment available
```
=======================
***** 2021-04-18 11:47:15.545097 *****
No appointments available. Retry in 3 seconds
=======================
```