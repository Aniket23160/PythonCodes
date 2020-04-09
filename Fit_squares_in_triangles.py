a=int(input())
l=[]
for i in range(a):
	b=int(input())
	l.append(b)
for i in range(a):
	if (l[i]-2)>=0:
		print (int((l[i]-1)*(l[i]-3)/2))
	else:
		print (0)	