#main program
# remove duplicates in all triangles, figure this out
# use a dictionary

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
    if verbose_adj: print('ADJ_LIST = '+str(adj_list))
    
    #get pruned adj list
    
    
    # Get node labels
    node_info, labeled_nodes, pos_nodes, neg_nodes = read_labeled_nodes_example()
    
    all_triangles = remove_duplicates(get_all_triangles(node_list, adj_list))
    if verbose_tri: print('all triangles:\n'+str(all_triangles)+'\n')    
    
    triangles_dict = get_triangle_dictionary(all_triangles, pos_nodes, neg_nodes, all_keys)
    #assert(len(triangle_dict.keys() == ?))
    if verbose_tri_dict: print('triangles_dict = \n'+str(triangles_dict) +'\n')
    return 0


   
num_edges = 13
num_nodes = 10
verbose_read = False
verbose_adj = True
verbose_tri = True
verbose_tri_dict = True

all_keys = ['pos_pos_pos_', 'pos_pos_neg_', 'pos_neg_neg_', 'neg_neg_neg_',
            'pos_pos_u_', 'pos_u_u_', 'neg_neg_u_', 'neg_u_u_', 'u_u_u_', 'neg_pos_u_']

if __name__ == '__main__':
    main()
