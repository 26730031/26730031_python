N=int(input())
lst=[]

for i in range(N):
    temp=int(input())
    lst.append(temp)

print(int(sum(lst)/N))

'''total=0
for i in lst:
    total+=i

print(int(total/N))'''
