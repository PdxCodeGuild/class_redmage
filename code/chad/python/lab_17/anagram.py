word1_input = str(input('Give me a word? > '))
word2_input = str(input('Give Me a Second Word? > '))

def anagram_check(word1, word2):
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)
    evaluate = word1_sorted == word2_sorted
    return evaluate

print(f'You two words are an Anagram {anagram_check(word1_input,word2_input)}')