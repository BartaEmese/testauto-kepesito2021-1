from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"

# oldal betöltése
driver.get(URL)
time.sleep(1)


# Az applikáció helyesen megjelenik:

#     A bingo tábla 25 darab cellát tartalmaz
#     A számlista 75 számot tartalmaz
def test_tc01():
    bingo_table = driver.find_elements_by_id("bingo-table")
    number_list = driver.find_elements_by_id("numbers-list")
    assert len(bingo_table) == 25
    assert len(number_list) == 75


# Bingo számok ellenőzrzése:

#     Addig nyomjuk a play gobot amíg az első bingo felirat meg nem jelenik
#     Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről tényleg a már kihúzott számok közül kerültek-e ki

def test_tc02():
    button = driver.find_element_by_id("spin")
    button.click()


# Új játékot tudunk indítani

#     az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
#     új bingo szelvényt kapunk más számokkal.

