#main program
# make a new git, read in everything
## ajsdfhasdufalskdjfbalwubfiowbciqbapwejfbpwefbpjsdbLDSFJWLEOUFBpjB
from utils import*
def main():
    # Read in example
    node_list, edge_list= read_in('example_edges.txt')
    if verbose_read:
        print(node_list)
        print(edge_list)
    
    
    assert(len(edge_list) == num_edges)
    assert(len(node_list) == num_nodes)
    
    # Make adjacency list
    adj_list = edge_to_adj(edge_list)
    assert(len(adj_list) == num_nodes)
    if verbose_adj:
        print(adj_list)
    
    nodes_triangles = get_triangles_for('u0', adj_list)
    if verbose_tri:
        print(nodes_triangles)

    # make function that takes a single node and returns list of tuples with other
    # nodes in that triangle
    # make function that does this for all nodes
        # return that 
    return 0


   
num_edges = 13
num_nodes = 10
verbose_read = False
verbose_adj = False
verbose_tri = True

if __name__ == '__main__':
    main()
