'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re

def tokenize(string):
    '''Converting given strings to a dictionary with frequencies of each word'''
    reg = re.compile("[^a-z A-Z 0-9]")
    token_dict = {}
    line = []
    for each_line in string:
        line.append(reg.sub('', each_line).split())

    for each_str in line:
        for each_word in each_str:
            token_dict[each_word] = token_dict.get(each_word, 0) + 1
    return token_dict

def main():
    '''Taking inputs and displaying outputs'''
    num_lines = int(input())
    list_ofstrs = []
    for _ in range(num_lines):
        list_ofstrs.append(input())
    # print(list_ofstrs)
    print(tokenize(list_ofstrs))
if __name__ == '__main__':
    main()
 