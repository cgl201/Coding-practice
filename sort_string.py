# -*- coding: utf-8 -*-
# Time: 5/17/2019 8:40 PM
# Author: Guanlin Chen


a = ' In reality, the president is trying to rewrite history.'

def reverse_string(data):
    index = len(data) - 1
    temp_word = ''
    result = ''
    while index >= 0:
        if data[index].isalpha():
            temp_word = data[index] + temp_word

        else:
            result = result + temp_word + data[index]
            temp_word = ''
        index -= 1

    result = result + temp_word
    return result


print(reverse_string(a))

