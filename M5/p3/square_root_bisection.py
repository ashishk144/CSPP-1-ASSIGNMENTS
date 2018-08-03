"""Write a python program to find the square root of the given number
using approximation method

testcase 1
input: 25
output: 4.999999999999998

testcase 2
input: 49
output: 6.999999999999991"""

def main():
    """Defining main"""
    s_s = int(input())
    eps_ilon = 0.01
    l_o = 0
    h_i = s_s
    gu_es = (l_o+h_i)/2
    while abs(gu_es**2-s_s) >= eps_ilon:
        if gu_es**2 > s_s:
            h_i = gu_es
        else:
            l_o = gu_es
        gu_es = (l_o+h_i)/2
    if (gu_es**2-s_s) >= eps_ilon:
        print("Failed")
    else:
        print(gu_es)
if __name__ == "__main__":
    main()
