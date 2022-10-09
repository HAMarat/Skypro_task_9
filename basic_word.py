class Basic_word:
    def __init__(self, word, right_words):
        self.word = word
        self.right_words = right_words

    def __repr__(self):
        return 'Класс для проверки слов'

    def checking_word(self):
        """
        Проверяет слово введенное пользователем на наличие в списке правильных слов
        """
        return self.word in self.right_words

    def number_of_word(self):
        """
        Возвращает максимальное количество правильных слов
        """
        return len(self.right_words)
