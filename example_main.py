## Main program that visualizes a toy graph

from utils import*
def main():
    
    # All possible combinations of triangle
    all_keys = ['pos_pos_pos_', 'pos_pos_neg_', 'pos_neg_neg_', 'neg_neg_neg_',
            'pos_pos_u_', 'pos_u_u_', 'neg_neg_u_', 'neg_u_u_', 'u_u_u_', 'neg_pos_u_']
    
    # Read in example edges
    node_list, edge_list= read_in_example()
    
    # Make adjacency list
    adj_list = edge_to_adj(edge_list)
    
    # Get node labels
    node_info, labeled_nodes, pos_nodes, neg_nodes = read_labeled_nodes_example()
    
    # Find all triangles in the graph
    all_triangles = remove_duplicates(get_all_triangles(node_list, adj_list)) 
    
    # Organize triangles into a dictionary
    triangles_dict = get_triangle_dictionary(all_triangles, pos_nodes, neg_nodes, all_keys)
    
    # Isolate edges that are part of a triangle to highlighted
    highlighted_edges = get_highlighted_edges(all_triangles)
   
    # Visualize results in GraphSpace
    viz_graph_example(node_list, edge_list, highlighted_edges, pos_nodes, neg_nodes)
    
    # Print results
    print_results(triangles_dict, all_triangles)
    
    return 0

if __name__ == '__main__':
    main()
