

'''
1. Создайте класс Word.
2. Добавьте свойства text и part of speech.
3. Добавьте возможность создавать объект слово со значениями в скобках.
4. Создайте класс Sentence
5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
6. Добавьте метод show, составляющий предложение.
7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.
'''


class Word:

    # Инициализатор экземпляра класса (объекта)
    def __init__(self, text='', part_of_speech='существительное'):
        self.text = text
        self.part_of_speech = part_of_speech


class Sentence:

    def __init__(self, words_list, words_order):
        self.words_list = words_list
        self.words_order = words_order

    def show(self):
        sentence = ''
        for i in range(len(self.words_order)):
            sentence = sentence + self.words_list[self.words_order[i]].text + ' '
        return sentence.rstrip().capitalize() + '.'

    def show_parts(self):
        parts = []
        for i in range(len(self.words_order)):
            parts.append(self.words_list[self.words_order[i]].part_of_speech)
        return parts


# Получить значение 'part_of_speech' из класса
w1 = Word('гряда')
# Получить значение 'part_of_speech' из объекта
w2 = Word('летучая', 'прилагательное')
w3 = Word('облаков')
w4 = Word('редеет', 'глагол')

words_list = [w1, w2, w3, w4]
words_order = [3, 2, 1, 0]
s = Sentence(words_list, words_order)

print('show():', s.show())
print('show_parts():', s.show_parts())


# Результат:
#
# show(): Редеет облаков летучая гряда.
# show_parts(): ['глагол', 'существительное', 'прилагательное', 'существительное']
