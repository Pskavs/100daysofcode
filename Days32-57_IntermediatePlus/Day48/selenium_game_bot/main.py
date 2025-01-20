#Importing packages and setting up selenium.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

#Creating the cookie object to click for the game.
cookie = driver.find_element(By.ID, "cookie")
game = True
clock = 0

def check_store():
    """Checks the score against the amount of money and then buys the object."""
    store = driver.find_element(By.ID, "store")
    store= store.find_elements(By.CSS_SELECTOR,'b')
    player_money = driver.find_element(By.ID, "money")
    print(store[7].text)
    money = int(player_money.text)
    store_dictionary = {}
    for i in range(len(store)-1):
        store_key = ''.join(c for c in store[i].text if c.isalpha())
        store_cost = ''.join(m for m in store[i].text if m.isnumeric())
        store_dictionary.update({store_key: int(store_cost)})
    if money >= store_dictionary["Timemachine"]:
        store_buy = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]')
        store_buy.click()
    elif money >= store_dictionary["Portal"]:
        store_buy = driver.find_element(By.XPATH, '//*[@id="buyPortal"]')
        store_buy.click()
    elif money >= store_dictionary["Alchemylab"]:
        store_buy = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]')
        store_buy.click()
    elif money >= store_dictionary["Shipment"]:
        store_buy = driver.find_element(By.XPATH, '//*[@id="buyShipment"]')
        store_buy.click()
    elif money >= store_dictionary["Mine"]:
        store_buy = driver.find_element(By.XPATH, '//*[@id="buyMine"]')
        store_buy.click()
    elif money >= store_dictionary["Factory"]:
        store_buy = driver.find_element(By.XPATH, '//*[@id="buyFactory"]')
        store_buy.click()
    elif money >= store_dictionary["Grandma"]:
        store_buy = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]')
        store_buy.click()
    elif money >= store_dictionary["Cursor"]:
        store_buy = driver.find_element(By.XPATH,'// *[ @ id = "buyCursor"]')
        store_buy.click()
    else:
        print("Not enough money!")

    print(store_dictionary)

game_cycle = 0
while game:
    """Continuously clicks the cookie while keeping time. When the clock hits 100, or 10 seconds, it checks the store.
    At 5 minutes we end the game."""
    cookie.click()
    time.sleep(0.001)
    clock += 1
    if clock >= 100:
        if game_cycle <=27:
            #Doesn't check the store with 30 seconds left so the focus is gathering points for the last 30 seconds.
            check_store()
        clock = 0
        game_cycle+=1
        print(game_cycle)
        if game_cycle >= 30:
            game = False