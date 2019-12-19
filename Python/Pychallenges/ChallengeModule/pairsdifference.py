def searchbinary(target, start, end, l):
    total_items = len(l)
    mid = start + int((end -1 - start) / 2)
    #print(start, end,mid)
    if mid < start or mid >= total_items:
        return 0
    else:
        if l[mid] == target:
            return 1
        elif l[mid] < target:
            return searchbinary(target, mid+1, end, l)
        else:
            return searchbinary(target, start, mid -1, l)


def pairs(k, arr):
    if len(arr) == 0:
        return 0
    copy_arr = arr[:]
    copy_arr.sort()
    ending = len(copy_arr)
    my_ret_list= list(map(lambda x: searchbinary(x-k,0, ending, copy_arr), copy_arr))
    result = sum(my_ret_list)
    return result
