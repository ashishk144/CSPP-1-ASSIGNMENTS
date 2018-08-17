'''
    Document Distance - A detailed description is given in the PDF
'''
def word_list(inp_1):
    words_list = []
    for line in inp_1:
        line = line.lower()
        words_list = line.split('\n')
        return words_list

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    return word_list(dict1), word_list(dict2)

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
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
