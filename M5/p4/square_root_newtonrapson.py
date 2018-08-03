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
    s_s = float(input())
    eps_ilon = 0.01
    gu_es = s_s/2.0
    while gu_es <= s_s:
        if abs(gu_es**2-s_s) >= eps_ilon:
            gu_es = gu_es-(gu_es**2 - s_s)/(2*gu_es)
        else:
            break
    if abs(gu_es**2-s_s) >= eps_ilon:
        print("Failed")
    else:
        print(gu_es)

if __name__ == "__main__":
    main()
