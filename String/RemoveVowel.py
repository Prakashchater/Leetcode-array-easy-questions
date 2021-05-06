def removeVowel(s):
    vowel = ['a', 'e', 'i', 'o', 'u']
    for letter in s.lower():
        if letter in vowel:
            s = s.replace(letter, "")
    return s

if __name__ == '__main__':
    s = "GeeksforGeeks - A Computer Science Portal for Geeks"
    print(removeVowel(s))
