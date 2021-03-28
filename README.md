# Zen
This is a collection of webbots that crawl sites to look for COVID vaccine appointments.
Only Sutter Health is supported currently, but it can be extended easily to support other sites.

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
* prepare config.json
```
$ cp config.json.template config.json
```
* update your credential and the chromeDriver path in config.json
  * sutter health is the only supported site for now
```json
{
    "sutter": {
        "userid": "yourvalue",
        "password": "yourvalue"
    },
    "chromeDriverPath": "yourpathtochromedriver",
    "delay": 2
}

```
* adjust the webbot script
Each script is highly customized to the latest state of the site page layout and the options provided.  XPath is used to identify the elements such as answers to your medical conditions to declare your elibility for a vaccine appointment.  You need to adjust the options by using `chrome > developer tool`, CTRL-F and type in the xpath element to locate the options picked and make adjustment for your own answer choice accordingly.  

# Run
Execute the corresponding health provider site webbot script, it will show the appointments and pause for the delay time * 10.   During the pause time, 
1. if the page shows appointments that you like, press CTRL-C in the terminal that runs the script to terminate and directly make the appoinment in the browser.
2. if no appointment is shown or the appointments shown is not what you like, you can let the script to terminate the browser after the pause time expires and the whole process will start over again  infinitely.
3. You can terminate the infinite loop in 2) by CTRL-C in the terminal running the script.  Remember to close the browser opened by the script. 
```
$ python sutter.py
```