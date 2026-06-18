def translate(text):
    vowels = {"a", "e", "i", "o", "u"}
    text_list = text.split(" ")
    text_solve = []
    for word in text_list:
        if word[0] in vowels or word.startswith("xr") or word.startswith("yt"):
            text_solve.append(word+"ay")
            continue
        letter_id = 0
        while word[letter_id] not in vowels and letter_id < len(word):
            if word[letter_id] in vowels:
                break
            if word[letter_id] == "y" and letter_id > 0:
                break
            if word[letter_id:].startswith("qu"):
                break
            letter_id+=1
        if word[letter_id:].startswith("qu"):
            cut_point = letter_id + 2
            initial = word[:cut_point]
            final = word[cut_point:]
            text_solve.append(final+initial+"ay")
            continue
        initial = word[:letter_id]
        final = word[letter_id:]
        text_solve.append(final+initial+"ay")
    return " ".join(text_solve)
    
