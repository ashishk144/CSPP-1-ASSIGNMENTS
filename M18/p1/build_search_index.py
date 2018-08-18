'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re

# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    #print(text)
    list_1 = []
    for eachline in text:
        reg = re.compile('[^a-z ]')
        list_1.append([reg.sub('', eachword.strip()) for eachword in eachline.lower().split(' ')])
    # print(list_1)
    return list_1

def remove_words(list_ofwords):
    '''removing all the stopwords'''
    stop_word = load_stopwords('stopwords.txt')
    for each_word in stop_word:
        for each_list in list_ofwords:
            while each_word in each_list:
                each_list.remove(each_word)
    return list_ofwords

def word_freq(list_word, ind, doc_id, diction):
    '''finding the word frequency'''
    for each_wrd in list_word:
        if each_wrd != '':
            if each_wrd not in diction:
                # print(each_wrd)
                diction[each_wrd] = [(doc_id, each_wrd.count(list_word))]
            # diction[each_wrd][ind][1] += 1
    return diction

def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
    search_index = {}
    list_ofdoc = remove_words(word_list(docs))
    for i, j in enumerate(list_ofdoc):
        k = 0
        search_index = search_index.update(word_freq(j, k, i, search_index))
        k += 1
    return search_index
# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1
    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
