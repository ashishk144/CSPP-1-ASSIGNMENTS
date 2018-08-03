"""Write a python program to find if the given number is a perfect cube or not
using guess and check algorithm

testcase 1
Input: 24389
Output: 24389 is a perfect cube

testcase 2
Input: 21950
Output: 21950 is not a perfect cube"""

def main():
    """input is captured in s_s"""
    s_s = int(input())
    gu_es = 0
    while gu_es**3 < s_s:
        gu_es += 1
    if gu_es**3 == s_s:
        print(str(s_s)+" is a perfect cube")
    else:
        print(str(s_s)+" is not a perfect cube")
if __name__ == "__main__":
    main()
