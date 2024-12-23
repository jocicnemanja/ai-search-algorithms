
graph_simple = {
'A' : ['B','C'],
'B' : ['D', 'E'],
'C' : ['F', 'G'],
'D' : ['H'],
'E' : ['G', 'I'],
'F' : ['J'],
'G' : ['J'],
'H' : [],
'I' : ['J'],
'J' : []
}

import queue

def BFS(graph, start, end):
  if start is end:
    path=list()
    path.appen(start)
    return path
  
  queue_nodes = queue.Queue(len(graph))
  visited = set()
  prev_nodes = dict()
  
  queue_nodes.put(start)
  visited.add(start)
  prev_nodes[start] = None
  
  found_dest = False
  
  while (not found_dest) and (not queue_nodes.empty()):
    node = queue_nodes.get()
    for dest in graph[node]:
      if dest not in visited:
        prev_nodes[dest] = node
        if dest is end:
          found_dest = True
          break
        visited.add(dest)
        queue_nodes.put(dest)

  path = list()
  
  if found_dest:
    path.append(end)
    prev = prev_nodes[end]
  
  while prev is not None:
    path.append(prev)
    prev = prev_nodes[prev]

  path.reverse()
  
  return path
    
    
print(BFS(graph_simple,'A','J'))


        
    
    
    
