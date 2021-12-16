# Main program that visualizes a portion of the triangles in the 
# fly interactome that have zip and/or sqh as one or nore of their 
# verticies

from utils import*
def main():
    # List of NMII proteins
    NMII = ['sqh', 'zip']
    
    # List of all possible triangle combinations    
    all_keys = ['pos_pos_pos_', 'pos_pos_neg_', 'pos_neg_neg_', 'neg_neg_neg_',
            'pos_pos_u_', 'pos_u_u_', 'neg_neg_u_', 'neg_u_u_', 'u_u_u_', 'neg_pos_u_']
    
    # Read in ppi
    node_list, edge_list, ignore= read_ppi()
    
    # Make adjacency list
    adj_list = edge_to_adj(edge_list)
    
    # Get node labels
    ignore, labeled_nodes, pos_nodes, neg_nodes = read_labeled_nodes()  
    
    # Find all triangles in the graph that have zip and/or sqh as a vertex
    all_triangles = remove_duplicates(get_triangles_for(NMII[0], adj_list) + get_triangles_for(NMII[1], adj_list))
    
    # Isolate the nodes that are in triangles
    triangle_nodes = get_triangle_nodes(all_triangles)
    
    # Organize triangles into a dictionary based on type of triangle
    triangles_dict = get_triangle_dictionary(all_triangles, pos_nodes, neg_nodes, all_keys)
   
    # Compile a sample of the triangles to post
    sample_triangles = all_triangles[:25]
    sample_edges = trim_graph(sample_triangles)
    sample_triangle_nodes = get_triangle_nodes(sample_triangles)

    # Visualize results in GraphSpace
    viz_graph(sample_triangle_nodes, sample_edges, pos_nodes, neg_nodes, NMII)
    
    # Print the results
    print_results(triangles_dict, all_triangles)  
    
    return 0

if __name__ == '__main__':
    main()
