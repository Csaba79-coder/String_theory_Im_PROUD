def is_palindrome(text):
    """
    >>> is_palindrome('Mr. Owl ate my metal worm')
    True
    >>> is_palindrome('Eva, can I see bees in a cave?')
    True
    """
    text = text.casefold()
    text_list = []
    # print(text)
    for letters in text:
        if (letters.isalpha()) == True:
            text_list.append(letters)
    new_text_list = ("".join(text_list))
    if new_text_list == new_text_list[::-1]:
        return True
    else:
        return False
print("Palindrome:")
print(is_palindrome('Mr. Owl ate my metal worm'))
print(is_palindrome('Eva, can I see bees in a cave?'))
print(is_palindrome('Csaba'))


def is_isogram(text):
    """
    >>> is_isogram('uncopyrightables')
    True
    """
    text = text.casefold()
    text_list = []
    for letters in text:
        if (letters.isalpha()) == True:
            text_list.append(letters)
    new_text_list = ("".join(text_list))
    for items in new_text_list:
        if new_text_list.count(items) > 1:
            return False
    return True
print("Isogram:")
print(is_isogram('uncopyrightables'))
print(is_isogram('Csaba'))


def is_pangram(text):
    """
    >>> is_pangram('The quick brown fox jumps over the lazy dog')
    True
    """
    text = text.casefold()
    text_list = []
    for letters in text:
        if (letters.isalpha()) == True:
            text_list.append(letters)
    new_text_list = ("".join(text_list))
    new_text = set(new_text_list)
    sorted_new_text = sorted(new_text)
    sorted_alphabet_text = sorted("abcdefghijklmnopqrstuvwxyz")
    if sorted_new_text== sorted_alphabet_text:
        return True
    return False
print("Pangram:")
print(is_pangram('The quick brown fox jumps over the lazy dog'))
print(is_pangram('Csaba'))


def is_anagram(text1, text2):
    """
    >>> is_anagram('Justin Timberlake', "I'm a jerk but listen")
    True
    """
    text1 = text1.casefold()
    text1_list = []
    for letters in text1:
        if (letters.isalpha()) == True:
            text1_list.append(letters)
    new_text1_list = ("".join(text1_list))
    new_text1 = sorted(new_text1_list)
    text2 = text2.casefold()
    text2_list = []
    for letters in text2:
        if (letters.isalpha()) == True:
            text2_list.append(letters)
    new_text2_list = ("".join(text2_list))
    new_text2 = sorted(new_text2_list)
    if new_text1 == new_text2:
        return True
    return False
print("Anagram:")
print(is_anagram('Justin Timberlake', "I'm a jerk but listen"))
print(is_anagram("Csaba", "Zsolti"))


def is_blanagram(text1, text2):
    """
    >>> is_blanagram('Justin Timberlake', "I'm a berk but listen")
    True
    """
    text1 = text1.casefold()
    text1_list = []
    for letters in text1:
        if (letters.isalpha()) == True:
            text1_list.append(letters)
    new_text1_list = ("".join(text1_list))
    new_text1 = sorted(new_text1_list)
    text2 = text2.casefold()
    text2_list = []
    for letters in text2:
        if (letters.isalpha()) == True:
            text2_list.append(letters)
    new_text2_list = ("".join(text2_list))
    new_text2 = sorted(new_text2_list)
    counter = 0
    for char in new_text1:
        if char not in new_text2:
            counter += 1
    if counter == 1:
        return True
    return False
print("Blanagram:")
print(is_blanagram('Justin Timberlake', "I'm a berk but listen"))
print(is_blanagram("Anagram", "Managua"))
print(is_blanagram("Csaba", "Zsolti"))