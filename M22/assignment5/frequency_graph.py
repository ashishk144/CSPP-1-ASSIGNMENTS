'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    keys = list(dictionary.keys())
    keys.sort()
    for each_key in keys:
        print(str(each_key), '-', dictionary[each_key]*'#')

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
