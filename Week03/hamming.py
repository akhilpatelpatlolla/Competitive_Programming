def hamming(x,y):
	return bin(x^y).count('1')
x=int(input())
y=int(input())
print(hamming(x,y))