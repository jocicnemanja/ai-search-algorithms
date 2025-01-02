from queue import PriorityQueue 


graph_simple = {
'A' : (9, ['B','C']),
'B' : (6, ['D', 'E']),
'C' : (7, ['F', 'G']),
'D' : (4, ['H']),
'E' : (8, ['G', 'I']),
'F' : (3, ['J']),
'G' : (4, ['J']),
'H' : (4, []),
'I' : (3, ['J']),
'J' : (0, [])
}



def best_first_search(graph, start, end):
  if start == end:
    
    path = list()
    path = append(start)
    return path
  
  priority_queue = PriorityQueue()
  visited = set()
  prev_nodes = dict()
  
  priority_queue.put((graph[start][0], start))
  visited.add(start)
  prev_nodes[start] = None
  isFound = False
  
  while (not isFound) and (not priority_queue.empty()):
    node = priority_queue.get();
    for dest in graph[node[1]][1]:
      if dest not in visited:
        prev_nodes[dest] = node[1]
        if dest is end:
          isFound = True
          break
        visited.add(dest)
        priority_queue.put((graph[dest][0], dest))
  
  path = list()
  
  if isFound:
    path.append(end)
    prev = prev_nodes[end]
    while prev is not None:
      path.append(prev)
      prev = prev_nodes[prev]
      path.reverse()
    return path


print("TEST", best_first_search(graph_simple,'A','J'));
