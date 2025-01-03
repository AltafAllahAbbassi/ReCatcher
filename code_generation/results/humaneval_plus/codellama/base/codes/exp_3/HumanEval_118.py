def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    vowels = "AEIOU"
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    word = word.upper()
    if len(word) == 1:
        return ""
    if word[0] in vowels:
        word = word[1:]
    if word[-1] in vowels:
        word = word[:-1]
    for i in range(len(word)):
        if word[i] in consonants and word[i+1] in vowels:
            return word[i+1]
    return ""