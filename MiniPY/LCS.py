x="LARGEST"
y="LONGEST"

def display(m):
    for row in m:
        print(*row)

m=[[[0] for _ in range(len(x)+1)] for _ in range(len(y)+1)]

"""
       L   O   N   G   E   S   T
    0  0   0   0   0   0   0   0
O   0  0   0   0   0   0   0   0
N   0  0   0   0   0   0   0   0
E   0  0   0   0   0   0   0   0

E N O
"""
for i in range(1,len(y)+1):
    for j in range(1,len(x)+1):
        if y[i-1]==x[j-1]:
            m[i][j]=[m[i-1][j-1][0]+1,"↖"]
        else:
            if m[i-1][j][0]>=m[i][j-1][0]:
                m[i][j]=[m[i-1][j][0],"↑"]
            else:
                m[i][j]=[m[i][j-1][0],"←"]

display(m)

i=len(y)
j=len(x)
lcs=list()
while len(m[i][j])!=1:
    if m[i][j][1]=="←":
        j-=1
    elif m[i][j][1]=="↑":
        i-=1
    else:
        lcs.append(y[i-1])
        i-=1
        j-=1

lcs.reverse()
print(*lcs)