from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

sbis_site1 = 'https://fix.sbis.ru/'
driver = webdriver.Chrome()
try:
    driver.get(sbis_site1)
    driver.maximize_window()
    sleep(5)
    assert driver.current_url == sbis_site1, 'Неверно открыт сайт'
    contacts = driver.find_element(By.CSS_SELECTOR, ".sbisru-Header__menu-item-1")
    assert contacts.text == 'Контакты'
    contacts.click()
    sleep(3)
    logo_tensor = driver.find_element(By.CSS_SELECTOR, '[class="sbisru-Contacts__logo-tensor mb-8"]')
    logo_tensor.click()

    driver.switch_to.window(driver.window_handles[1])
    sleep(5)
    our_news = driver.find_element(By.CSS_SELECTOR, '[class="s-Grid-col s-Grid-col--6 s-Grid-col--sm12"]')
    our_news.location_once_scrolled_into_view
    assert our_news.is_displayed()
    sleep(3)
    details = driver.find_element(By.CSS_SELECTOR, '[href="/about"][class="tensor_ru-link tensor_ru-Index__link"]')
    details.click()
    sleep(3)
    assert driver.current_url == "https://tensor.ru/about"
finally:
    driver.quit()