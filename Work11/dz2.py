from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

sbis_site1 = 'https://fix-online.sbis.ru/'
driver = webdriver.Chrome()
try:
    driver.get(sbis_site1) #Переходим на сайт
    driver.maximize_window()
    sleep(5)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')  # нахожу поле логин
    login.send_keys('rihard', Keys.ENTER)  # ввожу логин, ну и вообще текст в поле
    sleep(5)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys('виноградов1234', Keys.ENTER) #Ввожу пароль
    sleep(10)
    driver.get('https://fix-online.sbis.ru/page/dialogs') # Переходим в контакты
    sleep(5)
    create_btn = driver.find_element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]')
    create_btn.click() #Нажимаю создать сообщение
    sleep(10)
    field_for_search = driver.find_element(By.CSS_SELECTOR,
                                 '.addressee-selector-popup__browser-searchWidth '
                                 '.controls-Search__nativeField_caretEmpty'
                                           )
    field_for_search.send_keys('Затонский Рихард') # Ввожу в поле для поиска контакта своё ФИО
    sleep(5)
    my_contact = driver.find_element(By.CSS_SELECTOR, '.msg-addressee-item')
    my_contact.click() #Выбираю свой контакт, чтобы отправить себе сообщение
    sleep(2)
    text_editor = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    message = 'Привет'
    text_editor.send_keys(message, Keys.CONTROL + Keys.ENTER) # Отправляю сообщение себе
    sleep(2)
    #Проверяю отправленное сообщение
    messages = driver.find_elements(By.CSS_SELECTOR, '.msg-entity-text')
    assert messages[0].text == message, 'Текст не найден'
    sleep(2)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(messages[0])
    action_chains.context_click(messages[0])
    action_chains.perform()
    sleep(2)
    delete_btn = driver.find_element(By.CSS_SELECTOR, '.controls-Menu__row [title="Перенести в удаленные"]')
    delete_btn.click() #удаляем сообщение
    sleep(2)
    assert driver.find_elements(By.CSS_SELECTOR, '.msg-entity-text')[0].text != message, 'Сообщение не удалили'
finally:
    driver.quit()