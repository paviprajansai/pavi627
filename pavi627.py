p=0
r,k=map(int,input().split())
for i in range(r,k+1):
	for j in range(1,i+1):
		if j**2==i:
			p=p+1
print(p)
