# Find the heighest sum of 3 no. in a sequence
# In sliding window, we process the element which is in window frame of given size by repeatedly 
# removing the first element of that window frame and append new element

def slidung_window(array, window_size):
    total = sum(array[:window_size])
    best_total = total

    for i in range(window_size, len(array)):
        old = array[i - window_size]
        new = array[i]

        total = total - old + new

        if total>best_total:
            best_total = total
            window_frame = window = array[i - window_size + 1: i + 1]
        
        # for visual show on each iteration
        # i - window_size + 1 inversely proportional to the i + 1, so it keep winodw sliding by removing 
        # the first/old num and adding new num

        window = array[i - window_size + 1: i + 1]
        print(f"window frame : {array[i - window_size]}, {window}")

    return best_total, window_frame

array = [2,5,1,7,3,8,4,9,6]
heighest, window_frame = slidung_window(array, 3)
print("Hieghest Total: ", heighest)
print("Windws frame which hase hieghest total: ", window_frame)


