class Morse(object):
    def mor(self, words):
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]

        s = {"".join(MORSE[ord(code) - ord('a')]
        	for code in word)for word in words}

        return len(s)
a=["gin", "zen", "gig", "msg"]
b=["a", "z", "g", "m"]
c= ["bhi", "vsv", "sgh", "vbi"]  
d=["a", "b", "c", "d"]
l=["hig", "sip", "pot"]  
z=Morse()
print(z.mor(a))
print(z.mor(b))
print(z.mor(c))
print(z.mor(d))
print(z.mor(l))
	