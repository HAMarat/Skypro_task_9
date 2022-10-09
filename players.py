class Player:
    def __init__(self, name):
        self.name = name
        self.used_words = []

    def __repr__(self):
        return 'Класс Player собирает и обрабатывает информацию об игроке'

    def get_used_words(self):
        """
        Возвращает количество угаданных слов
        """
        return len(self.used_words)

    def append_used_word(self, used_word):
        """
        Добавляет угаданное слово в список угаданных слов
        """
        self.used_words.append(used_word)

    def already_used_word(self, used_word):
        """
        Проверяет, есть ли угаданное слово в списке уже угаданных слов
        """
        return used_word in self.used_words
