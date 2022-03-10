# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


#Вариант №16
#Написать программу, которая считывает текст из файла и выводит его на экран, после
#каждого предложения добавляя, сколько раз встретилось в нем введенное с клавиатуры
#слово.


if __name__ == "__main__":
    with open("text.txt", "r", encoding="utf-8") as f:
        sentences = f.readlines()

    counter = 0
    key = input("Введите слово: ")
    for sentence in sentences:
        words = sentence.split(' ')
        for word in words:
            if key == word:
                counter += 1
        print(sentence, counter)




















