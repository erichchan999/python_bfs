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

    while queue:
        n = queue.get()
        
        # Terminate and return the depth after the end is found
        if n == end:
            return level[n]
        
        for neighbour in graph[n]:
            if neighbour not in visited:
                visited[neighbour] = True
                queue.put(neighbour)
                level[neighbour] = level[n] + 1
    
        # end could not be found
        return -1

# Call function like this
bfs(visited, graph, 'A')
