from players import Player
from utils import load_random_word

# Получаем имя игрока
name_player = input('Введите имя игрока ')

# создаем элемент класса Player
player_1 = Player(name_player)

print('Привет', player_1.name)

# создаем элемент класса Basic_word со случайным словом из данных выложенных на сайте
basic_word_one = load_random_word('https://www.jsonkeeper.com/b/PZQ9')

# Выводим условия игры
print(f'Составьте {basic_word_one.number_of_word()} слов из слова {basic_word_one.word}\n'
      f'Слова должны быть не короче 3 букв\n'
      f'Чтобы закончить игру, угадайте все слова или напишите "stop"\n'
      f'Поехали, ваше первое слово?')

# пустая переменная для начального условия в цикле
enter_word = ''
# запускаем цикл для принятия слов от игрока
while player_1.get_used_words() < basic_word_one.number_of_word():
    enter_word = input().lower()
    if enter_word in ['stop', 'стоп']:  # выходим из игры если игрок хочет её завершить
        break
    if len(enter_word) < 3:
        print('слишком короткое слово')
        continue
    if enter_word not in basic_word_one.right_words:
        print('неверно')
        continue
    if player_1.already_used_word(enter_word):
        print('уже использовано')
        continue
    print('верно')
    player_1.append_used_word(enter_word)  # добавляем правильно угаданное слово в список элемента класса Player

print(f'Игра завершена, вы угадали {len(player_1.used_words)} слов!')
