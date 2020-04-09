a=int(input())
l=[]
s=[]
for i in range(a):
	b=input()
	s=b.split()
	l.append(s)
for i in range(a):
	if l[i][0]>l[i][1]:
		print ('>')
	if l[i][0]<l[i][1]:
		print ('<')
	if l[i][0]==l[i][1]:
		print ('=')
