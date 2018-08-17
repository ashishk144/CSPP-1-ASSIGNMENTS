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

def del_words(dicti, stopword):
    for word_s in stopword:
        if word_s in dicti:
            del dicti[word_s]
    return dicti

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    import math

    dict_1 = word_list(dict1)
    dict_2 = word_list(dict2)
    stop_words = load_stopwords('stopwords.txt')
    new_dict1 = del_words(dict_1, stop_words)
    new_dict2 = del_words(dict_2, stop_words)

    key_set = set(list(new_dict1.keys()) + list(new_dict2.keys()))
    freq_dict = {}
    for key_s in key_set:
        if key_s in new_dict1 and key_s in new_dict2:
            freq_dict[key_s] = [new_dict1[key_s], new_dict2[key_s]]
        elif key_s in new_dict1 and key_s not in new_dict2:
            freq_dict[key_s] = [new_dict1[key_s], 0]
        elif key_s in new_dict2 and key_s not in new_dict1:
            freq_dict[key_s] = [0, new_dict2[key_s]]
    numerator = 0
    deno_1 = 0
    deno_2 = 0
    for keys in freq_dict:
        numerator += freq_dict[keys][0] * freq_dict[keys][1]
        deno_1 += freq_dict[keys][0]**2
        deno_2 += freq_dict[keys][1]**2
    denominator = math.sqrt(deno_1) * math.sqrt(deno_2)
    similar = numerator/denominator
    return similar

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
