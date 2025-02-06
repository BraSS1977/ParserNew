import requests
from bs4 import BeautifulSoup
from googletrans import Translator


def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except Exception as e:
        print(f"Ошибка при получении слова: {e}")
        return None


def translate_to_russian(text):
    try:
        translator = Translator()
        translation = translator.translate(text, src='en', dest='ru')
        return translation.text
    except Exception as e:
        print(f"Ошибка перевода: {e}")
        return text  # Возвращаем оригинальный текст в случае ошибки перевода


def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_data = get_english_words()
        if not word_data:
            print("Не удалось получить слово. Попробуйте ещё раз.")
            continue

        # Переводим слово и определение
        russian_word = translate_to_russian(word_data["english_word"])
        russian_definition = translate_to_russian(word_data["word_definition"])

        print(f"\nЗначение слова - {russian_definition}")
        user_input = input("Что это за слово? ").strip()

        if user_input.lower() == russian_word.lower():
            print("Правильно! Вы угадали!")
        else:
            print(f"Неверно! Правильный ответ: {russian_word}")

        play_again = input("\nХотите сыграть ещё раз? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Спасибо за игру! До свидания!")
            break


if __name__ == "__main__":
    word_game()