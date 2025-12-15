from typing import List

def decrypt(word: str) -> str:
    decrypted = ""
    decrypted = decrypted + chr((ord(word[0]) - 1))
    prev_ascii = ord(word[0])

    for i in range(1, len(word)):
        curren_ascii = ord(word[i])
        difference = curren_ascii - prev_ascii

        while difference < 97:
            difference += 26

        decrypted += chr(difference)
        prev_ascii = curren_ascii

    return decrypted


