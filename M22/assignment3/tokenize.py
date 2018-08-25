'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    reg = re.compile("[^a-z,0-9]")
    return reg.sub('', string)
            
def main():
    n = int(input())
    list_1 = []
    for _ in range(n):
    	list_1.append(input().split())
    print(list_1)
if __name__ == '__main__':
    main()
