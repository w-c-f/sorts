from random import randint, seed


# creates the list using the seed provided by the user
def getList():
    # seed(theseed)
    mylist = []
    for i in range(0, 5):
        mylist.append(randint(1, 100))
    return mylist


def sel_sort(list_):
    # max_passes is the total number of times to traverse the list, left to right. (one less since im using <=)
    max_passes = len(list_)-1
    x = 1
    # restarts the comparisons, left to right, total num of passes = length - 1
    while x <= max_passes:   # number of passes is one less than the total number of elements. so 4 passes for 5n list
        print("pass {}".format(x))
        # go through list left to right and find the minimum value (current_len-1 comparisons)
        i = x # sets i to the current loop number (as in 1 for loop 1, so comparison is done on pos 1, and so on
        compnum = 1
        current_min = list_[i - 1]  # defines current minimum value as the first unsorted value
        position = i - 1  # defines position (as in to be swapped with) as that of first unsorted position
        while i < len(list_):  # compare every value in unsorted list, get min
            print("comparison {}".format(compnum))
            print("comparing {} with {}".format(current_min, list_[i]))
            if current_min > list_[i]:
                current_min = list_[i]
                position = i
            compnum = compnum +1
            print(current_min)
            i = i + 1
            print(list_)
        # swaps first value (pass # - 1) with value of minimum in unsorted
        list_[x - 1], list_[position] = list_[position], list_[x - 1]
        print("list after swap{}".format(list_))
        # since x increments by 1, and starts at 1, "i" will equal the current pass number at the start of next subloop
        x = x + 1
    print("final:{}".format(list_))



alist = getList()
#alist = [7, 9, 3, 5, 1]
print(alist)
sel_sort(alist)
