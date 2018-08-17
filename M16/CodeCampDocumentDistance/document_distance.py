'''
    Document Distance - A detailed description is given in the PDF
'''
def word_list(inp_1):
    new_dict = {}
    line_1 = inp_1
    line_1 = line_1.lower()
    line_1 = line_1.replace('.', '').replace(',', '').replace('?', '')\
    .replace('0', '').replace('1', '').replace('2', '')\
    .replace('3', '').replace('4', '').replace('5', '')\
    .replace('6', '').replace('7', '').replace('8', '')\
    .replace('9', '')
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
    return new_dict

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    new_dict1 = word_list(dict1)
    new_dict2 = word_list(dict2)
    stop_words = load_stopwords(stopwords.txt)
    for word_s in stop_words:
        if word_s in new_dict1:
            del new_dict1[word_s]
    
    for word_s in stop_words:
        if word_s in new_dict2:
            del new_dict2[word_s]
    print(new_dict1, new_dict2)

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
