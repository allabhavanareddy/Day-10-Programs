'''arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.'''

def peak(l,si,li):
    while si<=li:
        mid=(si+li)//2
        if l[mid]>l[mid-1] and l[mid]>l[mid+1]:
           return mid
        elif l[mid-1]>l[mid]:
             li=mid
        else:
            si=mid+1
l=list(map(int,input().split()))
print( peak(l,0,len(l)-1))





