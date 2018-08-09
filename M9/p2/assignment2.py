'''
Exercise: Assignment-2
Next, implement the function getGuessedWord that takes in two parameters
a string, secret_word, and a list of letters, letters_guessed. This function
returns a string that is comprised of letters and underscores, based on what
letters in letters_guessed are in secret_word. This shouldn't be too different from isWordGuessed!
guessed_word = secret_word
for each_char in letters_guessed:
if each_char in guessed_word:
guessed_word = guessed_word.replace(each_char, "_")
# print(guessed_word)
for each_char in guessed_word:
if each_char != "_":
# print(secret_word)
secret_word = secret_word.replace(each_char, "_")
return secret_word
'''
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    compare_string = ['_']*len(secret_word)
    for [i, _] in enumerate(letters_guessed):
        for [j, _] in enumerate(secret_word):
            if letters_guessed[i] == secret_word[j]:
                compare_string[j] = secret_word[j]

    compare_string = ''.join(compare_string)
    return compare_string

def main():
    '''
    Main function for current assignment
    '''
    user_input = input()
    if user_input:
        data = user_input.split()
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j][0])
    print(get_guessed_word(secret_word, list1))

if __name__ == "__main__":
    main()
