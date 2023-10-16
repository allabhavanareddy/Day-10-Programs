def bs_floor(l,target,si,li,floor):
    if si<=li:
       mid=(si+li)//2
       if l[mid]==target:
           return l[mid]
       elif l[mid]<target:
          floor=l[mid]
          return bs_floor(l,target,mid+1,li,floor)
          
       else:
           #floor=l[mid]
           return bs_floor(l,target,si,mid-1,floor)
    return floor
           
            
l=list(map(int,input().split()))
target=int(input())
print(bs_floor(l,target,0,len(l)-1,-1))
