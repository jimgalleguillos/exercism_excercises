DECODER_VALUE = ord("a")+ord("z") # "a" and "z" sum values in alphabet ascii (96 + 123) -> 219

def encode(plain_text):
    """Encodes a plain text string using the Atbash cipher.

    Args:
        plain_text(str): The original text message to be encrypted.

    Returns:
        str: The encrypted text in lowercase, formatted into 5-character groups.

    """
    if not plain_text:
        return plain_text
    text = plain_text.lower()
    count = 0
    result = ""
    for letter in text:
        if letter.isdigit():
            result+=letter
            count+=1
        if letter.islower():
            result+= chr(DECODER_VALUE - ord(letter))
            count+=1
        if count >= 5:
            count = 0
            result+=" "
    return result.strip()

def decode(ciphered_text):
    """
    Decodes an Atbash cipher encrypted string back to plain text.
    
    Args:
        ciphered_text (str): The encrypted text grouped in blocks of 5 characters.

    Returns:
        str: The decrypted original text.
    """
    if not ciphered_text:
        return ciphered_text
    text = ciphered_text.lower().split()
    result = []
    for letter_group in text:
        for letter in letter_group:
            if letter.isdigit():
                result.append(letter)
            else:
                result.append(chr(DECODER_VALUE - ord(letter)))
    return "".join(result)