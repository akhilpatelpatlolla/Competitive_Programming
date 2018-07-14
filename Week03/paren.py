def getBrackets(n):
  if(n == 0):
    return [""]

  ret = []
  c=0

  for i in range(n):

    brackets1 = getBrackets(i)
    brackets2 = getBrackets(n-i-1)

    for b1 in brackets1:
      for b2 in brackets2:
        ret.append( "(" + b1 + ")" + b2)  
  return ret
x=getBrackets(2)
print(x," ",len(x))
y=getBrackets(3)
print(y," ",len(y))
z=getBrackets(5)
print(z," ",len(z))
a=getBrackets(4)
print(a," ",len(a))
b=getBrackets(6)
print(b," ",len(b))
