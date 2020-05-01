# graph traversal
def has_path(graph, v_start,v_end, path_len=0):
    '''graph has path from v_start to v_end'''

    # traverse each vertex only once
    if path_len >= len(graph):
        return False

    #direct path from v_start to v_end?
    if graph[v_start][v_end]:
        return True

    # indeirect path via neighbor v_nbor?
    for v_nbor, edge in enumerate(graph[v_start]):
        if edge: #between v_start and v_nbor
            if has_path(graph, v_nbor, v_end, 
                path_len + 1):
                return True


    return False



# the graph represented as this matrix
G = [[1,1,0,0,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,1,1,1,0],
    [0,0,0,1,1]]

print(has_path(graph= G, v_start = 3, v_end = 0))