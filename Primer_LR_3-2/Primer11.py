# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


if __name__ == "__main__":
    with open("test.txt", "w", encoding="utf-8") as fileptr:
        print(
            "UTF-8 is a variable-width character encoding used for electronic communication.",
            file=fileptr
        )
        print(
            "UTF-8 is capable of encoding all 1, 112, 064 valid character code points.",
            file=fileptr
        )
        print(
            "In unicode using one ti four one-byte (8-bit) code units.",
            file=fileptr
        )

        







