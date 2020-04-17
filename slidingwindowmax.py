def largest_window(num_list, window_size, large_window):
 
    length = len(num_list)
    #checks if there are still at least the window_size amount of numbers in list
    if length >= window_size:

    # set window chunk to slice of num list
        window = num_list[:window_size]
        largest = max(window)
        large_window.append(largest)
        # call function again recursively excluding first number so our list will get smaller each time
        largest_window(num_list[1::], window_size, large_window)

    return large_window