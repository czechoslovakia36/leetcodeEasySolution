n,m = map(int,input().split())
N = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
#Union set A & B
C = A.union(B)
N = [i for i in N if i in C]

a2=[i for i in A if i in N]
b2=[i for i in B if i in N]

r=0
for item in a2:
    for index in range(len(N)):
        if N[index]==item:
            r=r+1
        else:
            pass
        
for item in b2:
    for index in range(len(N)):
        if N[index]==item:
            r=r-1
        else:
            pass
        
print(r)

