from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
URL = " https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"

# oldal betöltése
driver.get(URL)
time.sleep(1)

# Helyesen betöltődik az applikáció:

#    Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
#        !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~

def test_tc01():
    flex_child = driver.find_element_by_xpath('//div[@class="flex-child"]/p[3]')
    flex_child2 = flex_child.replace('"', "").split(", ")
    print(flex_child2)
    time.sleep(1)
    assert flex_child.text == "!"# $%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

# Megjelenik egy érvényes művelet:

#     chr megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
#     op mező vagy + vagy - karaktert tartlamaz
#     num mező egy egész számot tartalamaz





