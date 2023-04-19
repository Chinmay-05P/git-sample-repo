a = [7,8,1,3,4,5,6]
def NoOfRotations_Binary():
    low = mid = 0
    high = len(a)-1
    while(low <= high):
        mid = int((low + high)/2)
        if(mid>0 and a[mid]<a[mid-1]):
            return mid
        elif(a[mid] < a[high]):
            high = mid-1
        elif(a[mid] > a[high]):
            low = mid+1
    return 0  

print(NoOfRotations_Binary())