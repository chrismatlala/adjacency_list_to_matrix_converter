def adjacency_list_to_matrix(adj_list):
    # Determine the number of nodes
    n = len(adj_list)
    
    # Initialize an n x n matrix with zeros
    matrix = [[0] * n for _ in range(n)]
    
    # Fill in the matrix based on the adjacency list
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1
    
    # Print each row
    for row in matrix:
        print(row)
    
    # Return the adjacency matrix
    return matrix