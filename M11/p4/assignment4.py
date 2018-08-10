"""Exercise: Assignment-4
We are now ready to begin writing the code that interacts with the player.
We'll be implementing the playHand function. This function allows the user to play out a single
hand. First, though, you'll need to implement the helper calculate_handlen function,
which can be done in under five lines of code.
"""

def calculate_handlen(hand_dict):
    """ 
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    return len(hand_dict.values())


def main():
	num_ber = input()
	a_dict = {}
	for _ in range(int(num_ber)):
		data_input = input()
		l_1 = data_input.split()
		a_dict[l_1[0]] = int(l_1[1])
	print(calculate_handlen(a_dict))

if __name__ == "__main__":
	main()
