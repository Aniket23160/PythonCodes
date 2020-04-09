a=int(input())
l1=[]
c=[]
k=0
for i in range(a):
	b=int(input())
	l1.append(b)

for j in range(a):
	for i in range(100):
		c=(l1[j]/(10**(i))%10)
		if c==4:
			k=k+1
	print (k)		