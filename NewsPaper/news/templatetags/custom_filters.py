from django import template
import os

register = template.Library()

@register.filter(name='censor')
def censor(string):
    filename = 'news/templatetags/badwords.txt'
    with open(filename, 'r', encoding='utf8') as f:
        censored_list = [line.strip() for line in f.readlines()]
    string_words = string.split()
    for string_word in string_words:
        string_word_lw=string_word.lower()
        if string_word_lw in censored_list:
            string = string.replace(string_word, '***')
    return string


