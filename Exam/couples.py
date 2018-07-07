def minSwapsCouples(row):
   n=len(row)
   p2p=[None]*n
   for i, person in enumerate(row):
       p2p[person]=i
   cpt=0
   for i in range(0,n,2):
       p, z=row[i:i+2]
       q=p-1 if p%2 else p+1
       if q!=z:
           j=p2p[q]
           row[j]= z
           p2p[z]=j
           cpt+=1
   return cpt 

print(minSwapsCouples([1,3,4,0,2,5]))
print(minSwapsCouples([3,2,0,1]))
print(minSwapsCouples([1,0]))
print(minSwapsCouples([0,2,1,3]))