"""Write a python program to find the square root of the given number
using approximation method

testcase 1
input: 25
output: 4.999999999999998

testcase 2
input: 49
output: 6.999999999999991"""

def main():
    """epsilon and step are initialized
    don't change these values"""
    s_s = int(input())
    eps_ilon = 0.01
    st_ep = 0.1
    gu_es = 0
    while abs(gu_es**2 - s_s) >= eps_ilon:
        gu_es += st_ep
    if (gu_es**2 - s_s) >= eps_ilon:
        print("failed")
    else:
        print(gu_es)
if __name__ == "__main__":
    main()
