#!/usr/bin/env python3

import random, sys

class Language:
    def __init__(self, enc_strings):
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'í', 'ó', 'é', 'æ', 'á']
        self.enc_strings = enc_strings

    def encode(self, s):
        length = len(s)
        newVowel = True
        snew = []
        for i in range(0, length):
            if s[i] not in self.vowels:
                newVowel = True
            if s[i] in self.vowels and newVowel:
                snew.append(self.enc_strings[random.randint(0, len(self.enc_strings)-1)] + s[i])
                newVowel = False
            else:
                snew.append(s[i])
        return "".join(snew)

    def decode(self, s):
        length = len(s)
        snew = []
        i = 0
        while i < length:
            foundEnc = False
            for j in self.enc_strings:
                if s[i:i+len(j)] == j:
                    i+=len(j)
                snew.append(s[i])
            i += 1
        return "".join(snew)

    def prompt(self):
        if len(sys.argv) != 2:
            print("Please choose enc/dec")
        else:
            if sys.argv[1] == "enc":
                print(self.encode(input()))
            elif sys.argv[1] == "dec":
                print(self.decode(input()))
            else:
                print("Invalid option")
