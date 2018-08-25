'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''

import re

def clean_string(string):
    '''Function to clean the string'''
    reg = re.compile("[^a-z 0-9]")
    return reg.sub('', string)

def main():
    '''Main function to take input'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
