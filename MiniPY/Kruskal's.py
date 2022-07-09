#Kruskal's

cost=[
[0,28,0,0,0,0,0],
[28,0,16,0,0,0,14],
[0,16,0,12,0,0,0],
[0,0,12,0,22,0,18],
[0,0,0,22,0,25,24],
[10,0,0,0,25,0,0],
[0,14,0,18,24,0,0]]
n=7

visited=list()
edges=list()
check=list()
vertex=[i for i in range(1,n+1)]

for i in range(n):
    for j in range(n):
        if cost[i][j]!=0 and sorted([i+1,j+1]) not in check:
            edges.append([i+1,j+1,cost[i][j]])
            check.append(sorted([i+1,j+1]))
edges=sorted(edges, key=lambda x:x[2])
print(edges)


def cycle(vertex,source,dest):
    if vertex[source-1]==vertex[dest-1]:
        return True
    vertex[:] = [x if x != vertex[dest - 1] else vertex[source - 1] for x in vertex]

total_cost=0
for edge in edges:
    if not cycle(vertex,edge[0],edge[1]):
        total_cost+=edge[2]

print("The total cost is: ",total_cost)