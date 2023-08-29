from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from fake_useragent import UserAgent
import json


options = Options()
options.add_argument("window-size=1920,1080")
ua = UserAgent()
user_agent = ua.random
print(user_agent)
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=options)

full_info = []
try:
    driver.get(url="https://www.imdb.com/chart/top/?ref_=nv_mv_250")

    time.sleep(2)
    for i in range(1, 251):
        film_info = {}
        film_name = driver.find_element(By.CSS_SELECTOR, f"#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child({i}) > div.ipc-metadata-list-summary-item__c > div > div > div.ipc-title.ipc-title--base.ipc-title--title.ipc-title-link-no-icon.ipc-title--on-textPrimary.sc-b85248f1-7.lhgKeb.cli-title > a > h3")
        film_year = driver.find_element(By.CSS_SELECTOR, f"#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child({i}) > div.ipc-metadata-list-summary-item__c > div > div > div.sc-b85248f1-5.kZGNjY.cli-title-metadata > span:nth-child(1)")
        film_h = driver.find_element(By.CSS_SELECTOR, f"#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child({i}) > div.ipc-metadata-list-summary-item__c > div > div > div.sc-b85248f1-5.kZGNjY.cli-title-metadata > span:nth-child(2)")
        film_r = driver.find_element(By.CSS_SELECTOR, f"#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child({i}) > div.ipc-metadata-list-summary-item__c > div > div > span > div > span")
        film_info[film_name.text] = [film_year.text, film_h.text, film_r.text]
        full_info.append(film_info)
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, '#imdbHeader-navDrawerOpen').click()
    time.sleep(3)
    json_name = driver.find_element(By.CSS_SELECTOR, "#imdbHeader-navDrawer > div > div.drawer__panelContent > div > div:nth-child(1) > span > div > div > ul > a:nth-child(2) > span")

except Exception as ex:
    print(ex.__class__.__name__)
finally:
    with open(f'{json_name.text}.json', 'w') as file:
        json.dump(full_info, file, indent=2)
    print('------------------ OPEN THE FILE -----------------------')        
    driver.close()
    driver.quit()

