def is_pangram(sentence):
    sentence = sentence.lower()
    ref = "abcdefghijklmnopqrstuvwxyz"
    for letter in ref:
       if (sentence.find(letter) == -1):
        return False
    return True
