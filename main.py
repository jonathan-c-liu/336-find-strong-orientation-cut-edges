from dfs import run

file = open("./hw5_testset/test_12.in", "r")
data = file.read().splitlines()
for i in range(len(data)):
    line = data[i].split(" ")
    data[i] = [int(line[0]), int(line[1])]

n = data[0][0]
m = data[0][1]


# create adjacency lists
g = [[] for x in range(n)]
g_directed = [[] for x in range(n)]
dfs_tree = [[] for x in range(n)]

for edge in data[1:]:
    start = edge[0] - 1
    end = edge[1] - 1
    g[start].append(end)
    g[end].append(start)

for node_list in g:
    node_list.sort(reverse=True)


out = run(g, n)
text_file = open("test_ out", "w")
n = text_file.write(out)
text_file.close()
print(out)
