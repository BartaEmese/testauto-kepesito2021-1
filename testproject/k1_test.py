from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"

# oldal betöltése
driver.get(URL)
time.sleep(1)

# teszt adatok
a_test_value = ["2", ""]
b_test_value = ["3", ""]
result_value = ["10", "NaN"]

# elemak kikeresése
a_field = driver.find_element_by_id("a")
b_field = driver.find_element_by_id("b")
submit = driver.find_element_by_id("submit")
result = driver.find_element_by_id("result")


# pitagoras függvény
def pitagotas(a, b, ):
    a_field.clear()
    a_field.send_keys(a)
    b_field.clear()
    b_field.send_keys(b)
    submit.click()
    time.sleep(1)


# Helyesen jelenik meg az applikáció betöltéskor:

#     a: <üres>
#     b: <üres>
#     c: <nem látszik>
def test_tc01():
    assert a_field.is_displayed()
    assert b_field.is_displayed()
    assert not result.is_displayed()


# Számítás helyes, megfelelő bemenettel

#     a: 2
#     b: 3
#     c: 10
def test_tc02():
    pitagotas(a_test_value[0], b_test_value[0])
    assert result.text == result_value[0]


# Üres kitöltés:

#     a: <üres>
#     b: <üres>
#     c: NaN
def test_tc03():
    pitagotas(a_test_value[1], b_test_value[1])
    assert result.text == result_value[1]

    driver.quit()
