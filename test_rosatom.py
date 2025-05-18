from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    # Открываем веб-страницу
    driver.get("https://www.rosatom.ru/index.html")
    print("Открыта страница:", driver.current_url)

    # Проверяем, что заголовок содержит слово "Росатом Госкорпорация «Росатом» ядерные технологии атомная энергетика АЭС ядерная медицина"
    assert "Росатом Госкорпорация «Росатом» ядерные технологии атомная энергетика АЭС ядерная медицина" in driver.title
    print("Заголовок страницы корректен:", driver.title)

    # Находим и кликаем на кнопку меню, так как страница открывается в неполноразмерном масштабе
    menu_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "span.m-ico"))
    )
    menu_button.click()
    print("Открыли меню")
    time.sleep(1)

    # Находим и кликаем на пункт "О Росатоме"
    about_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/about/' and contains(text(), 'Росатоме')]"))
    )
    about_link.click()
    print("Кликнули на ссылку 'О Росатоме'")

    # Проверяем URL
    WebDriverWait(driver, 10).until(
        EC.url_contains("/about/")
    )
    print("Успешный переход на страницу:", driver.current_url)

except Exception as e:
    print("Произошла ошибка:", e)


finally:
    # Закрываем браузер
    driver.quit()
    print("Браузер закрыт")
