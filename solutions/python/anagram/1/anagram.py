def find_anagrams(word, candidates):
    """ Given a word, search through a list of candidate words to see if any of them is an anagram.

    Args:
        word (str): The word to be checked.
        candidates (list(str)): The list of words to be checked for anagrams.

    Returns:
        list(str): The list of candidates for an anagram.
    """
    w_lower = word.lower()
    w_sorted = sorted(w_lower)
    anagrams = []
    for cand in candidates:
        cand_lower = cand.lower()
        # ignore the same word
        if cand_lower == w_lower:
            continue
        # check if it is an anagram
        if w_sorted == sorted(cand_lower):
            anagrams.append(cand)
    return anagrams