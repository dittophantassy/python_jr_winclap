def annograms(word):
    # Is a word an anagram of itself?
    words = [w.rstrip() for w in open('WORD.LST')]
    return [ana for ana in words
            if sorted(ana) == sorted(word)  # have the same letters
            and ana != word]  # are not the same word

if __name__ == "__main__":
    print(annograms("train"))
    print('--')
    print(annograms('drive'))
    print('--')
    print(annograms('python'))
