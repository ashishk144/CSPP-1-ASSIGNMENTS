'''Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2'''
def main():
    """the input string is in s
    remove pass and start your code here"""
    str_s = input()
    ch_str = 'bob'
    c_co = 0
    for i in range(len(str_s)):
        if ch_str == str_s[i:i+3]:
            c_co += 1
    print(c_co)
if __name__ == "__main__":
    main()
