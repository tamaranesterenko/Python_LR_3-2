# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


if __name__ == "__main__":
    with open("text.txt", "r", encoding="utf-8") as f:
        text = f.read().lower()
        text = text.split()

    with open("service.txt", "r", encoding="utf-8") as t:
        service = t.read().lower()
        service = service.split()
    k = open("new.txt", "w", encoding="utf-8")

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
    k.close()
