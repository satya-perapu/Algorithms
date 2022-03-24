#sieves algorithm to count primes
n=int(input())
i=0
a=[True for i in range(n+1)]
a[0]=False
a[1]=False
if n==0 or n==1:
    print(0)
j=2
k=0
while j*j<=n+1:
    if a[j]:
        for k in range(j*j,n+1,j):
            a[k]=False
    j=j+1
c=0
for i in range(n):
    if a[i]:
        c=c+1
print(c)    
