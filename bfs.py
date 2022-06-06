graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

import queue as que

visited = {}            # Dictionary(hashmap) to keep track of visited nodes.
queue = que.Queue()     #Initialize a queue
level = {}              # Dictionary(hashmap) to keep track of level

def bfs(visited, graph, start, end):
    visited[start] = True
    queue.put(start)
    level[start] = 0

    cur_level = -1
    while queue:
        n = queue.get()
        cur_level = level[n]
        
        for neighbour in graph[n]:
            if neighbour not in visited:
                level[n] = cur_level + 1
                visited[neighbour] = True
                queue.put(neighbour)

# Driver Code
bfs(visited, graph, 'A')
