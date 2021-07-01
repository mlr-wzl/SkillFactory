# def censor(string):
#     filename="badwords.txt"
#     with open(filename, 'r', encoding='utf8') as f:
#         censored_list = [line.strip() for line in f.readlines()]
#         print(censored_list)
#     string_words = string.split()
#     for string_word in string_words:
#         string_word_lw=string_word.lower()
#         if string_word_lw in censored_list:
#             print(string_word_lw)
#             new_string = string.replace(string_word, '***')
#             print(new_string)
#             new_string = string.replace(string_word, '***')
#             return new_string
#         else:
#             return string
#
# censor("бала ыоувуциви")
#
