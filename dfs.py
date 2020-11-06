def run(g, n):
    parent = [None] * n
    frontier = [0]
    g_directed = ""
    cuts = ""
    cut_count = 0
    disc = [-1] * n
    low = [float('inf')] * n
    time = 0

    while len(frontier) != 0:
        u = frontier.pop()
        if disc[u] != -1:
            continue
        print(u)
        disc[u] = time
        low[u] = time
        time += 1
        for v in g[u]:
            if parent[u] == v:
                g_directed = g_directed + str(v + 1) + " " + str(u + 1) + "\n"
            elif disc[v] != -1:
                g_directed = g_directed + str(u + 1) + " " + str(v + 1) + "\n"
                low = update_low(v, u, low, parent)
            if disc[v] == -1:
                parent[v] = u
                frontier.append(v)

    visited = [False] * n
    frontier = [0]

    while len(frontier) != 0:
        u = frontier.pop()
        if visited[u]:
            continue
        visited[u] = True
        for v in g[u]:
            if low[v] > disc[u]:
                cuts = cuts + str(u + 1) + " " + str(v + 1) + "\n"
                cut_count += 1
            if not visited[v]:
                frontier.append(v)

    if cut_count > 0:
        return "NO\n" + str(cut_count) + "\n" + cuts
    else:
        return "YES\n" + g_directed


def update_low(v, z, low, parent):
    curr = z
    while curr != v:
        low[curr] = min(low[curr], low[v])
        curr = parent[curr]
    return low
