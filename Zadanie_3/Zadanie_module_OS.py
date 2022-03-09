# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import os


if __name__ == "__main__":
    os.rename("dog.png", "cat.png")
    os.remove("cat.png")
    path = os.getcwd()
    print(path)

























