

graf = {
"A": (9, [("B", 4), ("C", 6)]),
"B": (6, [("D", 4), ("E", 2)]),
"C": (7, [("G", 4), ("F", 6)]),
"D": (4, [("H", 4)]),
"E": (8, [("G", 5), ("I", 5)]),
"F": (3, [("J", 4)]),
"G": (4, [("J", 5)]),
"H": (4, []),
"I": (3, [("J", 3)]),
"J": (0, [])
}


def a_star(graf, start, end):
  
  foundDest = False
  open_set = set(start)
  close_set = set();
  prev_nodes = {}
  prev_nodes[start] = None
  g={}
  g[start]=0
  
  while len(open_set) > 0 and (not foundDest):
    
    node = None
    
    for next_node in open_set:
      if node is None or g[next_node] + graf[next_node][0] < g[node] + graf[node][0]:
        node = next_node
        
    if node == end:
      foundDest = True
      break
    
    for (descendant, cost) in graf[node][1]:
      if descendant not in close_set and descendant not in open_set:
        open_set.add(descendant)
        prev_nodes[descendant]=node
        g[descendant] = g[node] + cost
        
      
      else:
        if g[descendant] > g[node] + cost:
          g[descendant] = g[node] + cost
          prev_nodes[descendant] = node
          # because of heruistics is not good and we have to process node againg
          if descendant in close_set:
            close_set.remove(descendant)
            open_set.add(descendant)
    open_set.remove(node)
    close_set.add(node)
  
  path = list()
  
  path = []
  if foundDest:
    prev = end
    while prev_nodes[prev] is not None:
      path.append(prev)
      prev = prev_nodes[prev]
    path.append(start)
    path.reverse()
  return path
      
      
      
    
    
print("Path:", a_star(graf, "A", "J"))
