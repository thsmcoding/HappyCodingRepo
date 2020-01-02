from copy import copy


#sorting one array in place
def sortingarray(A):
    total = len(A)
    if total == 0 or total == 1:
        return
    mid_A = total//2
    i = 0
    j = mid_A+1
    aux=[]
    A.sort()
    A[0:j].sort()
    A[j:len(A)].sort()
    aux.extend( A[0:j])
    aux.extend(A[j:len(A)])
    for k in range(0,total):
        if i>mid_A:
            A[k] = aux[j]
            j=j+1
        elif j>total:
            A[k] = aux[i]
            i=i+1
        elif aux[j] <aux[i]:
            A[k] = aux[j]
            j=j+1
        else:
            A[k] = aux[i]
            i = i + 1


def mergesortarrays(A, B, ll):
    #A and B are not necessarily sorted
    A_copy = copy(A)
    B_copy = copy(B)
    mid_A = len(A)//2
    mid_B = len(B)//2
    A_copy[0:mid_A+1].sort()
    A_copy[mid_A+1:].sort()
    a=[]
    mergesortedarrays(A_copy[0:mid_A+1], A_copy[mid_A+1:],a)
    B_copy[0:mid_B + 1].sort()
    B_copy[mid_B + 1:].sort()
    b=[]
    mergesortedarrays(B_copy[0:mid_B+1], B_copy[mid_B+1:],b)
    mergesortedarrays(a,b,ll)


#merging arrays A and B which already sorted
def mergesortedarrays(A, B, l):
    if len(A) == 0 and len(B) >0:
        l.extend(B)
        return
    elif len(A)> 0 and len(B) == 0:
        l.extend(A)
        return
    else:
        i,u = 0,0
        if A[i] <= B[u]:
            l.append(A[i])
            mergesortedarrays(A[i+1:], B,l)
        else:
            l.append(B[u])
            mergesortedarrays(A, B[u+1:],l)


def median(l):
    total = len(l)
    if total == 0:
        return
    elif total % 2 ==0:
        return (l[(total-1)//2] + l[total//2])/2
    else:
        return l[total//2]


def Kisvalid(k,A,B):
    if len(A) +len(B)>=k:
        return True
    return False


#returning the Kth element in an array
def Kthsinglearray(k,A):
    if len(A) >=k:
        return A[k-1]
    return


def findKelement(k, A, B):
    if len(A) ==0 and len(B) ==0:
        return
    elif len(A) == 0 and len(B) > 0:
        return Kthsinglearray(k,B)
    elif len(B) == 0 and len(A) > 0:
        return Kthsinglearray(k,A)
    else:
        if len(A) == 1 and len(B) == 0:
            return A[0]
        elif len(B) == 1 and len(A) == 0:
            return B[0]
        elif k == 1:
            return min(A[0], B[0])
        elif k == len(A) + len(B):
            return max( A[len(A)-1], B[len(B)-1])
        else:
            mid_A = len(A) // 2
            mid_B = len(B) // 2
            if A[mid_A] <= B[mid_B]:
                smaller_set = 1+mid_A + mid_B
                if smaller_set == k-1:
                    return B[mid_B]
                else:
                    if smaller_set > k-1:
                        B_cut = B[:mid_B]
                    else:
                        B_cut = B[mid_B+1:]
                return findKelement(k,A, B_cut)
            else:
                smaller_set = 1+ mid_A + mid_B
                if smaller_set == k-1:
                    return A[mid_A]
                else:
                    if smaller_set > k - 1:
                        A_cut = A[:mid_A]
                    else:
                        A_cut = A[mid_A + 1:]
                return findKelement(k,A_cut,B)



#Take the first (k+1) elements of a sorted array
def partitionarray(A, k):
    total = len(A)
    if total < k:
        return A
    return A[:(k+1)]


#finding the median of two sorted arrays
def computemediantwoarrays(A,B):
    if len(A) + len(B) ==0:
        return None
    elif len(A) == 0 and len(B)>0:
        return median(B)
    elif len(B) == 0 and len(A)>0:
        return median(A)
    else:
        total = len(A) + len(B)
        midpoint = total//2
        A_cut_1 = partitionarray(A, midpoint)
        B_cut_1 = partitionarray(B, midpoint)
        if total%2 == 0:
            A_cut_2 = partitionarray(A,midpoint+1)
            B_cut_2 = partitionarray(B,midpoint+1)
            elt_1 = findKelement(midpoint+1, A_cut_1,B_cut_1)
            elt_2 = findKelement(midpoint,A_cut_2,B_cut_2)
            return float((elt_1+elt_2)/2)
        else:
            median_odd = findKelement(midpoint,A_cut_1,B_cut_1)
            return float(median_odd)


