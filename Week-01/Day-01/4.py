from operator import itemgetter
m=((0, 1), (3, 5), (4, 8), (10, 12), (9, 10))
if len(m) <= 1:
    print("Invalid")
m= sorted(m,key=itemgetter(0))
pd = [m[0]]
m = m[1:]
for (s1,e1) in m:
    (s,e) = pd[-1]        
    if e>=s1:
        if e<=e1:
            e = e1
        pd[-1] = (s,e)
    else:
        pd.append((s1,e1))
print(pd)