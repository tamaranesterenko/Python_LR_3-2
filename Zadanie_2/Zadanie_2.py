
# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


#Вариант №16 (14)
#Перед публикацией текста или документа обычно принято удалять или изменять в них
#служебную информацию. В данном упражнении вам необходимо написать программу,
#которая будет заменять все служебные слова в тексте на символы звездочек (по количеству
#символов в словах). Вы должны осуществлять регистрозависимый поиск служебных слов в
#тексте, даже если эти слова входят в состав других слов. Список служебных слов должен
#храниться в отдельном файле. Сохраните отредактированную версию исходного файла в
#новом файле. Имена исходного файла, файла со служебными словами и нового файла
#должны быть введены пользователем. В качестве дополнительного задания расширьте
#свою программу таким образом, чтобы она выполняла замену служебных слов вне
#зависимости от того, какой регистр символов используется в тексте. Например, если в
#списке служебных слов будет присутствовать слово exam, то все следующие варианты слов
#должны быть заменены звездочками: exam, Exam, ExaM и EXAM.


if __name__ == "__main__":
    with open("text.txt", "r", encoding="utf-8") as f:
        text = f.read().lower()
        text = text.split()

    with open("service.txt", "r", encoding="utf-8") as t:
        service = t.read().lower()
        service = service.split()
    with open("new.txt", "r+", encoding="utf-8") as k:
        for word_ser in service:
            word_ser = word_ser.split()
            for word_text in text:
                word_text = word_text.split()
                if word_text == word_ser:
                    String = ''.join(word_text).lower()
                    long = len(String)
                    word_text = String.split()
                    while long != 0:
                        str2 = ''
                        for element in String:
                            element = '*'
                            str2 += element
                            long -= 1
                    k.write(' ')
                    k.write(str2)
                    k.write(' ')
                else:
                    word_text = ''.join(word_text)
                    k.write(word_text)
