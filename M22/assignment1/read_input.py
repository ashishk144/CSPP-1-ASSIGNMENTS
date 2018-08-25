'''
Write a python program to read multiple lines of text input and
store the input into a string.
'''

def main():
    '''Defining a function to read multiple lines and display them'''
    num_lines = int(input())
    line = []
    for _ in range(num_lines):
        line.append(input())

    for each_line in line:
        print(each_line)

if __name__ == '__main__':
    main()
