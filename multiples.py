n=int(input())
m=int(input())
mul= dict(input().split() for _ in range(m))
a=[]

for i in range(n+1):
	a.append(i)

for key in mul:
	k=int(key)
	for j in range(k,n+1,k):
		try:
			a[j]+=mul[key]
		except:
			a[j]=mul[key]

for i in range(1,n+1):
	print(a[i])
		

	
