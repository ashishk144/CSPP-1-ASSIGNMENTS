# Assignment-3
'''
At this point, we have written code to generate a random hand and display that hand to the user.
We can also ask the user for a word (Python's input) and score the word (using your getWordScore).
However, at this point we have not written any code to verify that a word given by a player
obeys the rules of the game.
A valid word is in the word list; and it is composed entirely of letters from the current hand.
Implement the is_validword function.

Testing: Make sure the test_isValidWord tests pass.
In addition, you will want to test your implementation by calling it multiple times on the same hand
what should the correct behavior be? Additionally, the empty string ('') is not a valid word -
if you code this function correctly, you shouldn't need an additional check for this condition.

Fill in the code for is_validword in ps4a.py and be sure you've passed the appropriate tests in
test_ps4a.py before pasting your function definition here.
'''

def is_validword(word_input, hand_let, word_list):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    count = 0
    for ch_ar in word_input:
        if ch_ar in hand_let:
            count += 1
    if count == len(word_input):
        if word_input in word_list:
            return True
    return False

def main():
    '''input function'''
    word_inp = input()
    hand_len = int(input())
    a_dict = {}
    for _ in range(hand_len):
        inp_ut = input()
        l_1 = inp_ut.split()
        a_dict[l_1[0]] = int(l_1[1])
    l_2 = input().split()
    print(is_validword(word_inp, a_dict, l_2))

if __name__ == "__main__":
    main()
