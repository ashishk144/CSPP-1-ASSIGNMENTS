'''
    Document Distance - A detailed description is given in the PDF
'''
import re

import math

def string_opr(inp_str):
    '''string operations'''
    inp_str = inp_str.lower()
    regex = re.compile('[^a-z ]')
    inp_str = regex.sub('', inp_str)
    list_ofwords = inp_str.split(' ')
    for index in range(len(list_ofwords)):
        list_ofwords[index] = list_ofwords[index].strip()
    # print(list_ofwords)
    return list_ofwords
    # regex = re.compile('[^a-z ]')
    # return [regex.sub('', eachword.strip()) for eachword in inp_str.lower().split(' ')]

def remove_stopword(word_list):
    '''removing stopwords'''
    # print(word_list)
    stop_words = load_stopwords('stopwords.txt')
    for each_word in stop_words:
        while each_word in word_list:
            word_list.remove(each_word)
    # print(word_list)
    return word_list

def word_freq(word_list, ind, diction):
    '''finding the word frequency'''
    for each_wrd in word_list:
        if each_wrd != '':
            if each_wrd not in diction:
                diction[each_wrd] = [0, 0]
            diction[each_wrd][ind] += 1
    return diction

# def print_dic(d):
#     for i in d:
#         print(i,":",d[i])

def computation(dictionary):
    '''computing the similarity value'''
    numerator = sum(value[0]*value[1] for value in dictionary.values())
    denom_1 = math.sqrt(sum(value[0]**2 for value in dictionary.values()))
    denom_2 = math.sqrt(sum(value[1]**2 for value in dictionary.values()))
    # print(numerator, denom_2, denom_1)
    return numerator/(denom_1*denom_2)

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    input_1 = string_opr(dict1)
    input_2 = string_opr(dict2)

    # print(input_2, input_1)

    input_1 = remove_stopword(input_1)
    input_2 = remove_stopword(input_2)

    dictionary = {}
    dictionary = word_freq(input_1, 0, dictionary)
    dictionary = word_freq(input_2, 1, dictionary)
    # print_dic(dictionary)
    return computation(dictionary)

def load_stopwords(file_name):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(file_name, 'r') as file_name:
        for line in file_name:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
