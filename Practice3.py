n=int(input())
k=0
def fac(x):
	s=1
	for i in range(1,(x+1)):
		s=s*i
	return (s)

for i in range(1,n+1):
	k=k+(i/fac(i))
print(k)

