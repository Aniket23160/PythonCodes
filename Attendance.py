a=int(input())
s=[]
l=[]
k=0
for i in range(a):
	b=input()
	s=b.split()
	l.append(s)
for i in range(a):
	for j in range(a):
		if l[i][0]==l[j][0]:
			k=k+1
	if k>=2:		
		print (l[i][0]+' '+ l[i][1])
	else:
		print (l[i][0])	