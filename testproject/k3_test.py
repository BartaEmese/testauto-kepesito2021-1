from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"

# oldal betöltése
driver.get(URL)
time.sleep(1)

title_data = ["abcd1234", "teszt233 @", "abcd"]
error_active = driver.find_element_by_xpath("//span")


def email_validation(a):
    title = driver.find_element_by_xpath("//input")
    title.clear()
    title.send_keys(a)


# Helyes kitöltés esete:

#     title: abcd1234
#     Nincs validációs hibazüzenet
def test_tc01():
    email_validation(title_data[0])
    assert error_active.text == ""


# Illegális karakterek esete:

#     title: teszt233@
#     Only a-z and 0-9 characters allewed.
def test_tc02():
    email_validation(title_data[1])
    time.sleep(2)
    assert error_active.text == "Only a-z and 0-9 characters allewed"


# Tul rövid bemenet esete:

#     title: abcd
#     Title should be at least 8 characters; you entered 4.
def test_tc03():
    email_validation(title_data[2])
    time.sleep(2)
    assert error_active.text == "Title should be at least 8 characters; you entered 4."

    driver.quit()
