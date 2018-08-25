'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    reg = re.compile("[^a-z]")
    token_dict ={}
    line = []
    for each_line in string:
    	line.append(reg.sub('', each_line))
    print(line)

def main():
    n = int(input())
    list_ofstrs = []
    for _ in range(n):
    	list_ofstrs.append(input())
    # print(list_ofstrs)
    tokenize(list_ofstrs)
if __name__ == '__main__':
    main()
