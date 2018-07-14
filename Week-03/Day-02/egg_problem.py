def egg(n,k):

    # Write the body of your function here
    if(k==0 or k==1):
        return k
    if(n==1):
        return k
    min=100
    i=1
    res=k+1
    for i in range(k):
       res=max(egg(n-1,i-1),egg(n,k-i))
       if(res<min):
           min=res

    return min+1

# Run your function through some test cases here
# Remember: debugging is half the battle!
n=input()
k=input()
f=egg(n,k)
print(f)