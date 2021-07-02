# Time: O(N)      Space:O(N)
def caesarCipher(letter, key):
    newLetter = []
    newKey = key % 26
    for i in letter:
        newLetter.append(getLetter(i, newKey))
    return "".join(newLetter)

def getLetter(i, key):
    newLetterCode = ord(i) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

if __name__ == '__main__':
    letter = "abc"
    key = 54
    print(caesarCipher(letter, key))