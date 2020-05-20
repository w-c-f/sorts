from random import randint, seed


# creates the list using the seed provided by the user
def getList():
    # seed(theseed)
    mylist = []
    for i in range(0, 5):
        mylist.append(randint(1, 100))
    return mylist


def opt_bub_sort(list_):
    # end is the final index, the position last item in list (one less, since i'm using < for that loop)
    # max_passes is the total number of times to traverse the list, left to right. (one less since im using <=)
    end = max_passes = len(list_)-1
    did_sort = True
    x = 1
    # restarts the comparisons, left to right, total num of passes = length - 1
    while x <= max_passes and did_sort is True:   # number of passes is one less than the total number of elements. so 4 passes for 5n list
        print("pass number {}".format(x))
        did_sort = False
        x = x + 1
        i = 0
        # do comparisons and swap if needed
        while i < end:
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
                did_sort = True
            i = i + 1
            print(list_)
        end = end - 1   # reduce the "last index to search" by 1, so it doesn't search sorted region
    print("final:{}".format(list_))


alist = getList()
#alist = [19, 67, 34, 20, 49, 50, 48, 46, 27]
print(alist)
opt_bub_sort(alist)
