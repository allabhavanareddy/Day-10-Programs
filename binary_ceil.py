def bs_ceil(l,target,si,li,ceil):
    if si<=li:
       mid=(si+li)//2
       if l[mid]==target:
           return l[mid]
       elif l[mid]<target:
          
           return bs_ceil(l,target,mid+1,li,ceil)
       else:
           ceil=l[mid]
           return bs_ceil(l,target,si,mid-1,ceil)
    return ceil
           
            
l=list(map(int,input().split()))
target=int(input())
print(bs_ceil(l,target,0,len(l)-1,0))



