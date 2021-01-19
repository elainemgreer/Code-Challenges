def find_word(words, string):


    def word_checker(word, string):

        for char in word:
            if char not in string:
                return False

        return True


    for word in words:
        check = word_checker(word)
        print(word)
        if check == True:
            return word
        if check == False:
            continue

    return None


find_words(['cat', 'dog', 'ax', 'baby', 'bird'], "tcabnihjs")