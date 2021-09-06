from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"

# oldal betöltése
driver.get(URL)
time.sleep(1)

all_color_list = ["IndianRed", "Pink", "HotPink", "Coral", "OrangeRed", "DarkOrange", "Yellow", "DarkKhaki", "Violet",
                  "MediumOrchid", "DarkMagenta", "Chartreuse", "MediumSpringGreen", "DarkGreen", "DarkCyan",
                  "Turquoise", "RoyalBlue", "NavajoWhite", "SaddleBrown", "Gray", "Black", "AliceBlue", "OldLace",
                  "Chocolate"]
random_color = driver.find_element_by_id("randomColor")
test_color = driver.find_element_by_id("testColor")
# Helyesen jelenik meg az applikáció betöltéskor:
#  Alapból egy random kiválasztott szín jelenik meg az == bal oldalanán. A jobb oldalon csak a [ ] szimbólum látszik. <szín neve> [ ] == [ ]
# assert random_color.get_attribute("values") in all_color_list


def test_tc01():
    for color in all_color_list:
        assert color in all_color_list

# El lehet indítani a játékot a start gommbal.

#     Ha elindult a játék akkor a stop gombbal le lehet állítani.
start_button = driver.find_element_by_id("start")
stop_button = driver.find_element_by_id("stop")
result = driver.find_element_by_id("result")


def test_tc02():
    assert start_button.is_enabled()
    assert stop_button.is_enabled()


# Eltaláltam, vagy nem találtam el.

#     Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le amikor a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a Correct! felirat jelenik meg. ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az Incorrect! felirat kell megjelenjen.

def test_tc03():
    start_button.click()
    stop_button.click()
    time.sleep(1)
    if random_color == test_color:
        assert result.text == "Correct"
    else:
        assert result.text == "Incorrect!"

    driver.quit()
