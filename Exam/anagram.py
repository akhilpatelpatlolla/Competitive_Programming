s=input()
t=input()
a=[]
b=[]
for i in s:
	if(i!=' '):
		a.append(i.lower())
for i in t:
	if(i!=' '):
		b.append(i.lower())
a.sort()
b.sort()
if(str(a)==str(b)):
	print("true")
else:
	print("false")
