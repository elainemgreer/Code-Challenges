
def groupAnagrams(self, words):

    
    word_dict = {}
    anagrams = []

    for word in words:
    
        sorted_word = "".join(sorted(word))
        
        if sorted_word not in word_dict:
            word_dict[sorted_word] = [word]
            
        else:
            word_dict[sorted_word].append(word)

    for val in word_dict.values():
        anagrams.append(val)
    
    return anagrams