ALPHABET = set("abcdefghijklmnopqrstuvwxyz") # all the letter in the English alphabet.
def is_pangram(sentence):
    """This funtion check if a sentence is a Pangram or not.
    
    Input:
    - sentence(string): string to be checked.

    Output:
    - boolean: True if it is a pangram, False otherwise.
    """
    if_pangram = set()
    
    for letter in sentence.lower():
        if letter in ALPHABET and letter not in if_pangram:
            if_pangram.add(letter)
    return len(if_pangram) == 26
            
