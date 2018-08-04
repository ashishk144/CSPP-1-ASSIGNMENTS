'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    p_d = 1
    if int_input == 0:
        print("0")
    else:
        if int_input < 0:
            int_input = int_input * -1
            p_d = -1
        else:
            pass
        while int_input > 0:
            p_d = p_d * (int_input%10)
            int_input = int_input//10
        print(p_d)
if __name__ == "__main__":
    main()
