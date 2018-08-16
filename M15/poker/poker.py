'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    set_list = set(new_list)
    # print(len(set_list), max(new_list)-min(new_list))
    return len(set_list) == 5 and (max(new_list) - min(new_list)) == 4
    # card_values = set(['--23456789TJQKA'.index(c) for c,s in hand])
    # print(card_values)
    # return len(card_values)==5 and (max(card_values)-min(card_values) == 4)
def get_frequency(hand):
    hand_dict = {}
    for each_card in hand:
        if each_card in hand_dict:
            hand_dict[each_card][0] += 1
        else:
            hand_dict[each_card] = 1
    return hand_dict

def four_ofakind(hand_inp):
    '''if 4 cards are of the same value'''
    key_dict = get_frequency(hand_inp)
    for each_key in hand_inp:
        if key_dict[each_key] == 4:
            return True
    return False

def is_three(hand_in):
    '''If there are 3 cards of the same type'''
    key_dic = get_frequency(hand_in)
    for each_card in hand_in:
        if key_dict[each_key] == 3:
            return True
    return False
def two_pair(hand):
    two_dict = get_frequency(hand)
    pair_count = 0
    for each_key in hand:
        if two_dict[each_key] == 2:
            pair_count += 1
    if pair_count == 2:
        return True
    return False
def one_pair(hand):
    pair_dict = get_frequency(hand)
    for each_key in hand:
        if two_dict[each_key] == 1:
            pair_count += 1
    if pair_count == 1:
        return True
    return False

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    suit_set = set()
    for each_card in hand:
        suit_set.add(each_card[1])
    # print(suit_set == 1)
    return len(suit_set) == 1

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    new_list = []
    face_value = '--23456789TJQKA'
    for c_l, _ in hand:
        new_list.append(face_value.index(c_l))
    print(new_list)
    temp_hand = sorted(new_list)
    if is_straight(temp_hand) and is_flush(temp_hand):
        return 9
    if four_ofakind(temp_hand):
        return 8
    if is_three(temp_hand) and one_pair(temp_hand):
        return 7
    if is_flush(temp_hand):
        return 6
    if is_straight(temp_hand):
        return 5
    if is_three(temp_hand):
        return 4
    if two_pair(temp_hand):
        return 3
    if one_pair(temp_hand):
        return 2
    #if high_hand()
    return 1

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    # print(HANDS)
    print(' '.join(poker(HANDS)))
