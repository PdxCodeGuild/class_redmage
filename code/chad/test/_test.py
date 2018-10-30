    for i in range(len(word_count)):
        for text in word_count[i]:
            if '\n' in text:
                word_count[i] = word_count[i].replace('\n', '')