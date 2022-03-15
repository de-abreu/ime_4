from unidecode import unidecode


def normalize(str):
    """Remove from the string whitespaces, accents, punctuation, and make it lowercase only."""

    normalized = ""
    for c in str:
        if c.isalnum():
            normalized += unidecode(c.lower())
    return normalized


def buildDict(str):
    d = dict()

    for c in str:
        d[c] = d.get(c, 0) + 1
    return d


def areAnagrams(s1, s2):
    n1 = normalize(s1)
    n2 = normalize(s2)

    if len(n1) != len(n2) or buildDict(n1) != buildDict(n2):
        return False
    return True


def main():
    print("This program evaluates if a given string is an anagram of a second string.")

    s1 = input("Type the first string: ")
    if areAnagrams(s1, input("Type the second string: ")):
        print("These are anagrams")
    else:
        print("These are not anagrams")


main()
