'''
    Document Distance - A detailed description is given in the PDF
'''
def word_list(inp_1):
    new_dict = {}
    line_1 = inp_1
    line_1 = line_1.lower()
    line_1 = line_1.replace('.', '').replace(',', '').replace('?', '')
    line_1 = line_1.split(' ')
    # line_1 = line_1.split('\n')
    # print(line_1)
    # for line in line_1:
    #      print(line)
    #      words_list = line.strip()
    for char_s in line_1:
        if char_s not in new_dict:
            new_dict[char_s] = 1
        else:
            new_dict[char_s] += 1
    return line_1

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
        print(stopwords)
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
