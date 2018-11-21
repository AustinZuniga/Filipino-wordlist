#!/usr/bin/python
import re


file = open("words.txt", "r")
finish = open("result.txt","w")
contents = file.read()
contents = contents.split('\n')

for word in contents:
    word = word.split(':')
    if word[0] == 'Word':
        check = map(str,word[1])
        if '1' or '2' in check:
            pass
        else:
            finish.write(word[1]+'\n')
    elif word[0] == 'Active Verb':
        finish.write(word[1]+'\n')
    elif word[0] == 'Passive Verb':
        finish.write(word[1]+'\n')
    else:
        pass
