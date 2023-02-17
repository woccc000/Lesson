def bin_sea(list,item): 
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)/2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > mid:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1,2,4,5,7,9]

print (bin_sea(my_list,3))
print (bin_sea(my_list,-1))
