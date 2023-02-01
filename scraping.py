
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service('C:\Program Files\Google\Chrome\Application\chrome.exe')

def get_web_scraping():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AtomationControlled")
    options.add_experimental_option("Exclude-Switches", ["enable-automation"])

    driver = webdriver.Chrome(service = service, options=options)
    driver.get(url="http://automated.pythonanywhere.com/")
    return driver

def main():
    driver = get_web_scraping()
    element = driver.find_element(by= "xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text

print(main())

