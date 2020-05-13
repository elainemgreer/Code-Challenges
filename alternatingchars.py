def alternatingCharacters(s):

    deletes = 0
    

    for i in range(0, len(s)):
        try: 
            if s[i] == s[i+1]:
                deletes += 1
        except:
            break

    return deletes