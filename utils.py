## All functions used in main() for main.py and example_main.py

from graphspace_python.api.client import GraphSpace
from graphspace_python.graphs.classes.gsgraph import GSGraph
import time

################
## Reads in example graph edges
## Author: Ananke Krishnan and Aliya Ghassaei
## INPUTS: file name as a string if using example
## OUTPUTS:
## edge_list: a list of edges (as lists)
## node_list: a list of nodes (as strings)
## edge_dictionary: a dictionary with edges (keys) and edge weights as lists (values)

def read_in_example(filename='inputs/example_edges.txt'):
    
    # Open file, store contents in variable text, close file
    print('Opening example_edges.txt...')
    file = open(filename, 'r')      
    text = file.read()
    print('Reading file...')
    file.close()
    text = text.split()
    
    # Remove column headers from text
    if text[0] == '#Name' or text[0] == '#': del text[0:2]
           
    # Initialize edge list, node list        
    edge_list = [] 
    node_list = []                       
   
    # Loop through each line of file
    for i in range(0, len(text), 2):
        
        # Select both parts of an edge
        new_edge = [text[i], text[i+1]]
        
        # Check for duplicates
        if (new_edge not in edge_list) and ([new_edge[1], new_edge[0]] not in edge_list):
            edge_list.append(new_edge)

        # Add new nodes to node list
        node_list.append(new_edge[0]) 
        node_list.append(new_edge[1])
    
    # Remove duplicate nodes
    node_list = list(set(node_list))
    return node_list, edge_list

################
## Reads in flybase interactome graph
## Author: Ananke Krishnan and Aliya Ghassaei
## INPUTS: file name as a string if using example
## OUTPUTS:
## edge_list: a list of edges (as lists)
## node_list: a list of nodes (as strings)
## edge_dictionary: a dictionary with edges (keys) and edge weights as lists (values)

def read_ppi(filename='inputs/flybase-interactome.txt'):
    
    # Open file, store contents in variable text, close file
    print('Opening flybase-interactome.txt')
    file = open(filename, 'r')
    print('Reading file...')
    text = file.read()
    file.close()
    text = text.split()
    
    # Remove column headers from text 
    del text[0:8]
    
    # Initialize edge list, node list, edge dictionary               
    edge_list = []
    node_list = []                 
    edge_dictionary = {}      
     
    # Loop through each line of file
    for i in range(0, len(text), 8):
        # Select both parts of edge    
        new_edge = [text[i], text[i+1]]
        
        # Check for duplicates
        if (tuple(new_edge) not in edge_dictionary.keys()) and (tuple([new_edge[1], new_edge[0]]) not in edge_dictionary.keys()):
            edge_list.append(new_edge)
            edge_dictionary[tuple(new_edge)] = float(text[i+2])
        
        # Add new nodes to node list
        node_list.append(new_edge[0]) 
        node_list.append(new_edge[1])
   
    # Remove duplicates
    node_list = list(set(node_list))
    
    return node_list, edge_list, edge_dictionary

################
## Creates adjacency list from list of edges
## Author: Ananke Krishnan and Mikhail Ostrovsky
## INPUTS: list of edges
## OUTPUTS: adjacency list (dictionary with nodes as keys and values as neighbors)

def edge_to_adj(edge_list):
    print('Creating adjacency list...')
    
    # Initialize adjacency list
    adj_list = {}
    
    # Loop through every edge
    for i in edge_list:
        
        # Add first node if not in adjacency list
        if i[0] not in adj_list:
            adj_list[i[0]] = []
            adj_list[i[0]].append(i[1])
        
        # Otherwise, add second node to existing value mapped to first node
        else: 
            adj_list[i[0]].append(i[1])
            
        # Add second node if not in adjacency list
        if i[1] not in adj_list:
            adj_list[i[1]] = []
            adj_list[i[1]].append(i[0])
            
        # Otherwise, add first node to existing value mapped to second node
        else:
            adj_list[i[1]].append(i[0])

    return adj_list

def get_triangle_nodes(all_triangles):
    
    # Initialize list for nodes in triangles
    triangle_nodes = []
    
    # For every triangle
    for triangle in all_triangles:
        
        # Add each node
        triangle_nodes.append(triangle[0])
        triangle_nodes.append(triangle[1])
        triangle_nodes.append(triangle[2])
    
    # Get rid of duplicates     
    return list(set(triangle_nodes))

def trim_graph(all_triangles):
    
    # Initializing list with edges to feed to GraphSpace
    edges_to_post = []  
    
    # For every triangle
    for triangle in all_triangles:
        assert(len(triangle) == 3) # Check that it's a tuple of 3
        
        # Add all possible edges from the triangle if not already in edge list
        if [triangle[0], triangle[1]] not in edges_to_post and [triangle[1], triangle[0]] not in edges_to_post:
            edges_to_post += [[triangle[0], triangle[1]]]
        if [triangle[1], triangle[2]] not in edges_to_post and [triangle[2], triangle[1]] not in edges_to_post:
            edges_to_post += [[triangle[1], triangle[2]]]
        if [triangle[2], triangle[0]] not in edges_to_post and [triangle[0], triangle[2]] not in edges_to_post:
            edges_to_post += [[triangle[0], triangle[2]]]

    return edges_to_post

                        

################
## Author: Ingrid Zoll, modified by Aliya Ghassaei
## INPUTS: None
## OUTPUTS: 
def read_labeled_nodes_example():
    posneg_file = 'inputs/example_labels.txt'
    print("Reading "+posneg_file+'...')
    
    # Initializing dictionary and lists
    node_info = {}
    labeled_nodes = []
    pos_nodes = []
    neg_nodes = []

    with open(posneg_file) as fin:
        # For each line in file
        for line in fin:
            # Separate the two items
            n, pos_neg = line.strip().split()
            
            # If the line is not the header (in this case, the header starts with "#Name")
            if n != "#Name": 
                
                # If not a duplicate node, add it to the labeled node list and info dictionary
                if n not in labeled_nodes:
                    labeled_nodes.append(n)
                    node_info[n] = [pos_neg]
                    
                    # Add node to appropriate positive/negative node list
                    if pos_neg == "Positive": 
                        pos_nodes.append(n)
                    elif pos_neg == "Negative":
                        neg_nodes.append(n)

    return node_info, labeled_nodes, pos_nodes, neg_nodes

################
## Author: Ingrid Zoll
## INPUTS: None, labeled node file is hardcoded
## OUTPUTS:
## node_info: dictionary, with format {node: [id, pos_neg, annotation], etc}
## labeled_nodes: list of all nodes in the labeled-nodes file
## pos_nodes and neg_nodes: lists of positive and negative labeled nodes, respectively.
## fix notes about running as necessary, if i decide to put it in a folder
def read_labeled_nodes():
    print('Reading labeled-nodes.txt')
    posneg_file = 'inputs/labeled-nodes.txt'
    
    # Initialize dictionary and lists
    node_info = {}
    labeled_nodes = []
    pos_nodes = []
    neg_nodes = []
    
    # Open labeled nodes file
    with open(posneg_file) as fin:
        for line in fin: 
            
            # Separate the four items
            n, ID, pos_neg, annotation = line.strip().split()
            
            # If the line is not the header (in this case, the header starts with "#Name")
            if n != "#Name": 
                # Add node to node list and info to dictionary if it's not a duplicate
                if n not in labeled_nodes: 
                    labeled_nodes.append(n)
                    node_info[n] = [ID, pos_neg, annotation]
                    
                    # Add node to positive or negative node list
                    if pos_neg == "Positive":
                        pos_nodes.append(n)
                    elif pos_neg == "Negative":
                        neg_nodes.append(n)

    return node_info, labeled_nodes, pos_nodes, neg_nodes

################
## Finds all triangles a given node participates in
## Author: Aliya Ghassaei
## INPUTS: Node and adjacency list
## OUTPUTS: List of all triangles a node participates in (as tuples)
def get_triangles_for(node, adj_list):
    
    # Initialize triangle list
    nodes_triangles = []
    
    # For every neighbor u of the node
    for u in adj_list[node]:
        
        # For every neighbor v of the node
        for v in adj_list[node]:
            
            # If u and v are neighbors, then they are a triangle with node since both are neighbors of node
            if u in adj_list[v]:
                nodes_triangles += [(node, u, v)]

    return nodes_triangles

################
## Calls get_triangles_for() on all nodes in node list
## INPUTS: list of nodes, adjacency list
## OUTPUTS: list of all triangles present, as tuples
def get_all_triangles(node_list, adj_list):
    
    # Initialize list for all triangles to go
    all_triangles = []
    
    # Find triangles for every node and add to all_triangles
    for node in node_list:
        all_triangles += get_triangles_for(node, adj_list)
    return all_triangles

################
## Removes different permutations of the same combination of triangles
## in the list of all triangles
## INPUTS: list of all triangles as tuples
## OUTPUTS: list of all triangles with no duplicates
def remove_duplicates(all_triangles):
    
    # Initialize list for triangle tuples
    sorted_triangles = []
    
    # Sort every tuple, making tuples of same combination identical
    for triangle in all_triangles:
        sorted_triangles += [tuple(sorted(triangle))]
    
    # All duplicate combinations are the same, and will be removed when cast as set
    return list(set(sorted_triangles))

################
## Find the label of a node
## INPUTS: node, list of positive nodes, list of negative nodes
## OUTPUTS: string that denotes node label
def get_node_label(node, pos_nodes, neg_nodes):
    
    # If node is positive
    if node in pos_nodes:
        label = 'pos'
    
    # If node is negative
    elif node in neg_nodes:
        label = 'neg'
    
    # Node is unlabeled
    else:
        label = 'u'

    return label

################
## Standardizes the way that types of triangles are denoted in the rest of the program
## INPUTS: A tag (string) denoting the type of triangle
## OUTPUTS: A tag (string) that denotes type of triangle, but standardized
def get_key(tag):
    
    # If all nodes are positive
    if tag == 'pos_pos_pos_':
        return tag
    
    # If two positive, one negative
    elif tag == 'pos_pos_neg_' or tag == 'pos_neg_pos_' or tag == 'neg_pos_pos_':
        return 'pos_pos_neg_'
     
    # If one positive, two negative
    elif tag == 'pos_neg_neg_' or tag == 'neg_neg_pos_' or tag == 'neg_pos_neg_':
        return 'pos_neg_neg_'
    
    # If all negative
    elif tag == 'neg_neg_neg_':
        return tag
        
    # If two positive, one unlabeled
    elif tag == 'pos_pos_u_' or tag == 'pos_u_pos_' or tag == 'u_pos_pos_':
        return 'pos_pos_u_'
        
    # If one positive, two unlabeled
    elif tag in {'pos_u_u_', 'u_pos_u_', 'u_u_pos_'}: return 'pos_u_u_'
       
            
    # If two negative, one unlabeled
    elif tag == 'neg_neg_u_' or tag == 'neg_u_neg_' or tag == 'u_neg_neg_':
        return 'neg_neg_u_'
    
    # If one negative, two unlabeled
    elif tag == 'neg_u_u_' or tag == 'u_neg_u_' or tag == 'u_u_neg_':
        return 'neg_u_u_'
    
    # If all unlabeled
    elif tag == 'u_u_u_':
        return tag
    # If one of each
    elif tag == 'neg_pos_u_' or tag == 'neg_u_pos_' or tag == 'pos_u_neg_' or tag == 'pos_neg_u_' or tag == 'u_pos_neg_' or tag == 'u_neg_pos_':
        return 'neg_pos_u_'
    else:
        print("You didn't account for "+tag+" !")
        assert(False)

    return 0

################
## Get a tag and standardize it
## INPUTS: Triangle (tuple), list of positive nodes, list of negative nodes
## OUTPUTS: A string denoting the type of the triangle
def get_tag(triangle, pos_nodes, neg_nodes):
    
    # Initialize the tag
    tag = ''    
    
    # Add to the tag depending on the label of each node in the triangle
    for node in triangle:
        label = get_node_label(node, pos_nodes, neg_nodes)
        tag+= label +str('_')
    return get_key(tag)

################
## Makes a dictionary with types of triangles as keys and values as list of triangles (tuples)
## INPUTS: List of all triangles, list of all possible keys, list of positive nodes, list of negative nodes
## OUTPUTS: Dictionary of triangles organized by type
def get_triangle_dictionary(all_triangles, pos_nodes, neg_nodes, all_keys):
    
    # Initialize an empty dictionary with all possible combinations of labels
    triangles_dict = {}
    for key in all_keys:
        triangles_dict[key] = []
    assert(len(triangles_dict) == len(all_keys))
    
    # Organize each triangle into the dictionary
    for triangle in all_triangles:
        assert(len(triangle) == 3)
        key = get_tag(triangle, pos_nodes, neg_nodes)
        triangles_dict[key] += [triangle]
    return triangles_dict

################
## Finds edges that are part of triangles to highlight in the visualization
## For example graph only
## INPUTS: List of all triangles as tuples
## OUTPUTS: List of edges to highlight
def get_highlighted_edges(all_triangles):
    
    # Initialize list for edges
    highlighted_edges = []
    
    # Add all edges in each triangle
    for triangle in all_triangles:
        highlighted_edges += [[triangle[0], triangle[1]], 
                              [triangle[0], triangle[2]],
                              [triangle[1], triangle[2]]]

    return highlighted_edges

################
## Function to post graph to GraphSpace
## Author: Anna Ritz, modified by Aliya Ghassaei
## Posts the graph G to GraphSpace and shares it with the group.
## Prompts the user for graph name, email, and password.
## param G: GSGraph object
## param post_group: share with the group (default True).
##  (note: you can prevent sharing by specifying post_group=False)

def post_to_graphspace(G,post_group=True):
    print('Posting to GraphSpace...')
    ## Connect to the GraphSpace client.
    group='BIO331F21'
    graph_name = input('Enter Graph Name: ')
    G.set_name(graph_name)
    email = input('Enter Email: ')
    password = input('Enter Password: ')
    gs = GraphSpace(email,password)
    print('GraphSpace successfully connected.')

    try: ## If graph does not yet exist...
        graph = gs.post_graph(G)
        if post_group:
            gs.share_graph(graph=graph,group_name=group)
    except: ## Otherwise, graph exists.
        print('Graph exists! Removing and re-posting (takes a few seconds)...')
        graph = gs.get_graph(graph_name=graph_name)
        gs.delete_graph(graph=graph)
        time.sleep(1) # pause for 1 second
        graph = gs.post_graph(G)
        if post_group:
            gs.share_graph(graph=graph,group_name=group)
    print('Done!')
    return

#############
## Builds GraphSpace graph from example graph only
## Modified from Anna Ritz's viz_graph function
## INPUTS: node list, edges to highlight, edges, positive nodes, negative nodes
## RETURNS: None, just posts graph
def viz_graph_example(nodes, edges, highlighted_edges, pos_nodes, neg_nodes):
    print('Visualizing graph...')
    
    # Create a graph object with tag
    G = GSGraph()
    G.set_tags(['Final Project'])
    
    # Assign color to each node based on pos/neg/unknown label and post it
    for n in nodes:
        if n in set(pos_nodes): 
            color = '#ea00b5' 
        elif n in set(neg_nodes):
            color = '#00b5ea' 
        else:
            color = '#b5ea00'
        G.add_node(n,label=n)    
        G.add_node_style(n,color=color,shape='ellipse',height=40,width=40)

    # Post each edge, highlighting edges in triangles
    for edge in edges:
        if edge in highlighted_edges or [edge[1], edge[0]] in highlighted_edges:
            G.add_edge(edge[0], edge[1])
            G.add_edge_style(edge[0], edge[1],width=4)
        else:
            G.add_edge(edge[0], edge[1])
            G.add_edge_style(edge[0], edge[1],width=2)
    
    # Post graph
    post_to_graphspace(G)
    return

#############
# Builds GraphSpace graph from reduced set of nodes and edges
# Modified from Anna's viz_graph function in build-example.py
# INPUTS: pruned node list, pruned edge list, predctions as dictionary, zip/sqh
# RETURNS: None, just posts graph
def viz_graph(triangle_nodes, edges_to_post, pos_nodes, neg_nodes, special):
    print('Visualizing graph...')
    
    # Create a graph object and assign tags
    G = GSGraph()
    G.set_tags(['Final Project'])
    
    # Assign dimensions and color to nodes based on label and if they're in NMII
    for n in triangle_nodes:
        if n in pos_nodes: 
            if n not in special:
                color = '#ea00b5'
                height=60
                width=60
            else:
                color = '#9e007a'
                height = 60
                width = 60
        if n in neg_nodes:
            color = '#00b5ea'
            height=60
            width=60
        if n not in set(neg_nodes) and n not in set(pos_nodes):
            color = '#b5ea00'
            height=60
            width=60
        G.add_node(n,label=n)    
        G.add_node_style(n,color=color,shape='ellipse',height=height,width=width)

    # Post edges
    for edge in edges_to_post:
        G.add_edge(edge[0], edge[1])
        G.add_edge_style(edge[0], edge[1],width=2)
    
    # Post graph
    post_to_graphspace(G)
    return

#############
## Prints the results of the program
## INPUTS: Dictionary of triangles, list of all triangles
## OUTPUTS: None
def print_results(triangles_dict, all_triangles):
    print('RESULTS:')
    total = len(all_triangles)
    print('Total triangles connected to zip and sqh: '+str(total))
    for key in triangles_dict:
        count = len(triangles_dict[key])
        if count>0:
            percentage = 100*(len(triangles_dict[key])/total)
            print('Total triangles of type ' +key+': '+str(count)+' ('+str(percentage)+'%)')
        
    return None
    
    
    

