from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    firefox_options = Options()
    firefox_options.add_argument("--headless")  # Uncomment to hide the browser
    firefox_options.add_argument("--disable-gpu")
    firefox_options.add_argument("--no-sandbox")
    driver = webdriver.Firefox(options=firefox_options)
    return driver

def get_paragraphs(driver):
    main_content = driver.find_element(By.ID, "mw-content-text")
    return [p.text for p in main_content.find_elements(By.TAG_NAME, "p") if p.text.strip()]

def get_links(driver):
    main_content = driver.find_element(By.ID, "mw-content-text")
    all_links = main_content.find_elements(By.TAG_NAME, "a")
    return [
        (link.text, link.get_attribute("href"))
        for link in all_links
        if link.get_attribute("href") and "/wiki/" in link.get_attribute("href")
    ]

def handle_page(driver, current_url):
    driver.get(current_url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mw-content-text"))
    )

    while True:
        print("\n" + "="*50)
        print(f"Текущая страница: {driver.title}")
        print("Выберите действие:")
        print("1. Читать параграфы статьи")
        print("2. Перейти на связанную страницу")
        print("3. Выйти из программы")

        choice = input("Ваш выбор (1-3): ").strip()

        if choice == "1":
            paragraphs = get_paragraphs(driver)
            for i, p in enumerate(paragraphs, 1):
                print(f"\nПараграф {i}:")
                print(p)
                if i % 3 == 0:
                    input("\nНажмите Enter для продолжения...")

        elif choice == "2":
            links = get_links(driver)
            if not links:
                print("Нет доступных связанных страниц!")
                continue

            print("\nДоступные связанные страницы:")
            for i, (text, href) in enumerate(links[:10], 1):  # Показываем первые 10 ссылок
                print(f"{i}. {text}")

            link_choice = input("Выберите номер ссылки (или 0 для отмены): ").strip()
            if link_choice.isdigit() and 0 < int(link_choice) <= len(links):
                return links[int(link_choice)-1][1]  # Возвращаем новый URL

        elif choice == "3":
            return None

        else:
            print("Некорректный ввод!")

def wikipedia_search():
    driver = setup_driver()

    try:
        # Начальный запрос
        search_term = input("Введите поисковый запрос для Википедии: ").strip()
        current_url = f"https://ru.wikipedia.org/wiki/{search_term.replace(' ', '_')}"

        while True:
            new_url = handle_page(driver, current_url)
            if not new_url:
                break
            current_url = new_url

    finally:
        driver.quit()
        print("\nПрограмма завершена. До свидания!")

if __name__ == "__main__":
    wikipedia_search()
