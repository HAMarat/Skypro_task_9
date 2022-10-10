import random
import requests
from basic_word import BasicWord


def load_random_word(url_name):
    """
    Получает словари с сайта в формате json и возвращает случайный словарь в формате python
    @param url_name: Ссылка на данные в формате json
    @return: возвращает случайный словарь в формате python
    """
    words_dict = requests.get(url_name).json()
    one_word_dict = random.choice(words_dict)
    basic_word_1 = BasicWord(one_word_dict['word'], one_word_dict['subwords'])
    return basic_word_1
