def check_palindrome(word):
    length = len(word)
    for i in range(length):
        if word[i] != word[length -i -1]:
            return False
    return True

