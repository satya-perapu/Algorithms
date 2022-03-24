#Seive algorithm to find the largest prime factor
s=0
N=int(input())
a=[i for i in range(N+1)]  #input
j=2
while j*j<=N+1:
    if a[j]==j:
       for k in range(j*j,N+1,j):#Replacing the multiplies of j with j 
            if a[k]!=k:
               continue  #Skipping the values when it is already replaced
            a[k]=j
    j=j+1       
while True:       #Finding the largest prime factor
    if a[N]==N: 
        break
    s=N//a[N]
    N=s
print(N)
