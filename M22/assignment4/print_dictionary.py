'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    '''Sorting with respect to keys and printing the dictionary'''
    keys = list(dictionary.keys())
    # print(list(keys))
    keys.sort()
    # print(keys)
    for key in keys:
        print(str(key)+' - '+str(dictionary[key]))

def main():
    '''Taking input as a dictionary'''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
