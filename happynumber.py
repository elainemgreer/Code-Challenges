def isHappy(n):


    def square_sum(n):

        num_list = []
        num_sum = 0

        num = str(n)
        for char in num:
            char = int(char)
            squared = char * char
            num_list.append(squared)
            num_sum = sum(num_list)
        return num_sum

    past = set()

    while n != 1:
        if n in past:
            return False
        past.add(n)
        n = square_sum(n)
        
    return True