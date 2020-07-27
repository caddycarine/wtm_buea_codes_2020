def find_anagrams(word, candidates):
    wordLength = len(word)
    lowerWord = list(word.lower())
    anagrams = []
    for candidate in candidates:
        lowerCandidate = list(candidate.lower())
        if (wordLength != len(candidate) | (lowerCandidate == lowerWord)):
            continue
        
        #Given that candidate has same length as word, convert them to lists of letters and compare        
        wLetters, cLetters = sorted(lowerWord), sorted(lowerCandidate)
        if wLetters == cLetters:
            anagrams += [candidate]
    return anagrams
