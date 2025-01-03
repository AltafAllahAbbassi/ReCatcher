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
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = word.lower()
    if len(word) == 1:
        return ''
    if len(word) == 2:
        if word[0] in vowels:
            return word[1]
        else:
            return word[0]
    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels:
            if word[i-1] in vowels:
                return ''
            else:
                return word[i]
    return ''