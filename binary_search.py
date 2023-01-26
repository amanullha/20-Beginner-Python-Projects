def binary_search(ar,t):
    left,right=0,len(ar)
    while left<right:
        midIdx=(left+right)//2
        mid=ar[midIdx]
        if mid==t:
            return {
                "value":mid,
                "index":midIdx
            }
        if(mid<t):
            left=midIdx+1
        else:
            right=midIdx
    return "invalid target!"

ar=[1,5,6,14,18,19,20,44]

for i in ar:
    print(binary_search(ar,i-2),"\n\n")