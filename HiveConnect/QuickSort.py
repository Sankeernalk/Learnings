def quick_sort(list1,low,high):
    if low < high:
        piv = partition(list1,low,high)
        quick_sort(list1,low,piv-1)
        quick_sort(list1,piv+1,high)

def get_pivot(list1,low,high):
    mid = (high+low)/2
    if list1[low] < list1[mid]:
        if list1[mid] < list1[high]:
            p1 = mid
        elif list1[low] < list1[high]:
            p1 = list1[high]
    return p1


def partition(list1,low,high):
    pivindex = get_pivot(list1,high,low)
    pivvalue = list1[pivindex]
    list1[pivindex],list1[low] = list1[low],list1[pivindex]
    border = low
    for i in range(low,high+1):
        if list1[i] < pivvalue:
            border +=1
            list1[border],list1[i]=list1[i],list1[border]
    list1[low],list1[border]=list1[border],list1[low]
    return border


list1 = [17,41,5,22,54,6,29,3,13]
low = 0
high = len(list1)-1
print(quick_sort(list1,low,high))
