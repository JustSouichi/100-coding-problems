def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

