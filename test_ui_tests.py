from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import allure 
import pytest

@pytest.fixture 
def browser(): 
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
    browser.maximize_window() 
    browser.implicitly_wait(4)
    yield browser 
    browser.quit()

    # Перейти на сайт «Читай-город» и добавить куки
cookie = {"name": "cookie_policy", "value": "1"}

@allure.title("Согласие на добавление куки") 
@allure.description("Тест проверяет добавление куки, чтобы плашка не мешала обзору") 
@allure.severity("Major") 
def test_opensite_and_addcookie(browser):
    browser.get("https://www.chitai-gorod.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    with allure.step("Добавление куки"):
        browser.add_cookie(cookie)
    sleep(5)

@allure.title("Поиск книги на русском языке") 
@allure.description("Тест проверяет поиск книги на русском языке") 
@allure.severity("blocker") 
def test_add_book(browser):
    browser.get("https://www.chitai-gorod.ru/")
    with allure.step("Добавлены ожидания и открытие окна"): 
        browser.implicitly_wait(10)
        browser.maximize_window()
    with allure.step("Выполнение поиска книги"): 
        browser.find_element(By.CSS_SELECTOR, ".header-search__input").send_keys("Мастер и Маргарита")
        browser.find_element(By.CSS_SELECTOR, ".header-search__button").click()  
    assert "Показываем результаты по запросу" in browser.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
    

    # Добавить все книги в корзину и посчитать
def add_book_and_count(browser):
    with allure.step("Добавить все книги"): 
        buy_buttons = browser.find_elements(
    By.CSS_SELECTOR, "button action-button blue")
    with allure.step("Посчитать все книги"):
        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter += 1

    # Перейти в корзину

    with allure.step("Перейти в корзину"): 
        browser.get("https://www.chitai-gorod.ru/cart")
    txt = browser.find_element_by_class_name("badge-notice header-cart__badge").text # чем отлич. от by css selector?
    with allure.step("Проверить счетчик товаров"): 
    # Проверить счетчик товаров
        assert counter == int(txt)
        browser.quit()

