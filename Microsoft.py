a=int(input())
l=[]
l1=[]
l2=[]
for i in range (a):
	b=int(input())
	l.append(b)

for i in range (a):
	for j in range(10):
		c=int((l[i]/10**j)%10)
		if c>0:
			l1.append(c)
		l2.append(l1)		

print (l2)
