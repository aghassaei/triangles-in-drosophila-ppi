## All utilities
# utilities for the thing
# make all the names consistient
### CHANGE PASSWORD IN GRAPHSAPCE FUNC!!!
# print to console thing

from graphspace_python.api.client import GraphSpace
from graphspace_python.graphs.classes.gsgraph import GSGraph
import time
import csv

################
## Author: Ananke Krishnan and Aliya Ghassaei
## INPUTS: file name as a string if using example
## OUTPUTS:
## edge_list: a list of edges (as lists)
## node_list: a list of nodes (as strings)
## edge_dictionary: a dictionary with edges (keys) and edge weights as lists (values)

def read_in_example(filename='flybase-interactome.txt'):
    print('Reading .txt file...')
    # Open file, store contents in variable text, close file
    print('Opening file...')
    file = open(filename, 'r')      
    text = file.read()
    file.close()
    text = text.split()
    
    # Remove column headers from text
    print('removing column headers')
    print('text[0] = '+str(text[0]))
    print('text[1] = '+str(text[1]))
    if text[0] == '#Name' or text[0] == '#' or text[0] == '#symbol1':
        del text[0:2]
    print('text[0] = '+str(text[0]))
    print('text[1] = '+str(text[1]))
           
    # Initialize edge list, node list        
    edge_list = [] 
    node_list = []                       
   
    # Loop through each line of file
    print('going through each line of the file')
    for i in range(0, len(text), 2):
        # Select both parts of an edge
        new_edge = [text[i], text[i+1]]
        print(new_edge)
        
        # Check for duplicates
        if (new_edge not in edge_list) and ([new_edge[1], new_edge[0]] not in edge_list):
            edge_list.append(new_edge)
            

        # Add new nodes to node list
        node_list.append(new_edge[0]) 
        node_list.append(new_edge[1])
    
    print('removing duplicate nodes')
    # Remove duplicate nodes
    node_list = list(set(node_list))
    print('done')
    return node_list, edge_list


## author: Ananke
## NOTE: Edited from Aliya's read_ppi function above!
################
## INPUTS: file name as a string 
## To test: use '../../inputs/test-fly-interactome.txt'
## To run: use '../../inputs/flybase-interactome.txt'
## must call this from within your own directory
## RETURNS:
## edge_list: a list of edges (as lists)
## node_list: a list of nodes (as strings)
## edge_dictionary: a dictionary with edges (keys) and edge weights as lists (values)

## Edited to try and decrease runtime
# It seems to be working on the flybase_interactome file and I was able to verify its accuracy using the test file

################

def read_ppi(filename='flybase-interactome.txt'):
    print('Opening flybase-interactome.txt')
    file = open(filename, 'r')      #open file, store contents in variable text, close file
    
    print('Reading file')
    text = file.read()
    file.close()
    text = text.split()
    
    del text[0:8] #removes column headers from text
    print(text[0])
                   
    edge_list = [] #initialize edge list, node list, and edge_dictionary
    node_list = []                 
    edge_dictionary = {}      
     
    print('for loop')  
    for i in range(0, len(text), 8): #loops through each line of file
        new_edge = [text[i], text[i+1]] #selects both parts of edge
        
        #check for duplicates
        if (tuple(new_edge) not in edge_dictionary.keys()) and (tuple([new_edge[1], new_edge[0]]) not in edge_dictionary.keys()):
            edge_list.append(new_edge)
            edge_dictionary[tuple(new_edge)] = float(text[i+2])
        
        #add new nodes to node list
        node_list.append(new_edge[0]) 
        node_list.append(new_edge[1])
   
    node_list = list(set(node_list)) #remove duplicate nodes
    
    return node_list, edge_list, edge_dictionary

################
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
    print('get_triangle_nodes()')
    triangle_nodes = []
    for triangle in all_triangles:
        triangle_nodes.append(triangle[0])
        triangle_nodes.append(triangle[1])
        triangle_nodes.append(triangle[2])
    # Get rid of duplicates   
    assert('zip' in triangle_nodes)       
    return list(set(triangle_nodes))

def trim_graph(all_triangles):
    print('running trim graph')
    #print(len(triangle_nodes))
    #print('Preparing data to post...')
    #adj_to_post = {}
    edges_to_post = []  
    #print('looping through nodes')
    #for node in triangle_nodes:
     #   adj_to_post[node] = []
      #  for neighbor in adj_list[node]:
       #     if neighbor in triangle_nodes:
        #        adj_to_post[node] += [neighbor]
    print('looping through all triangles')
    for triangle in all_triangles:
        print('current triangle in trim graph = '+str(triangle))
        assert(len(triangle) == 3)
        if [triangle[0], triangle[1]] not in edges_to_post and [triangle[1], triangle[0]] not in edges_to_post:
            edges_to_post += [[triangle[0], triangle[1]]]
        if [triangle[1], triangle[2]] not in edges_to_post and [triangle[2], triangle[1]] not in edges_to_post:
            edges_to_post += [[triangle[1], triangle[2]]]
        if [triangle[2], triangle[0]] not in edges_to_post and [triangle[0], triangle[2]] not in edges_to_post:
            edges_to_post += [[triangle[0], triangle[2]]]
            #for edge in edge_list:
     #   if edge[0] in triangle_nodes and edge[1] in triangle_nodes:
      #      edges_to_post += [edge]
    return edges_to_post #adj_to_post, edges_to_post

                        

################
## Author: Ingrid Zoll, modified by Aliya Ghassaei
##
def read_labeled_nodes_example():
    print('Reading in .txt file...')
    posneg_file = 'example_labels.txt'
    # initializing dictionary and lists
    node_info = {}
    labeled_nodes = []
    pos_nodes = []
    neg_nodes = []

    with open(posneg_file) as fin:
        for line in fin: # for each line
            n, pos_neg = line.strip().split() # separate the two items
            if n != "#Name": # if the line is not the header (in this case, the header starts with "#Name")
                if n not in labeled_nodes: # if the node is not a duplicate
                    labeled_nodes.append(n) # add it to the full node list
                    node_info[n] = [pos_neg] # add info to full node dictionary
                    if pos_neg == "Positive": # if the node is positive, add to positive list
                        pos_nodes.append(n)
                    elif pos_neg == "Negative": # if node is negative, add to negative list
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
    posneg_file = 'labeled-nodes.txt'
    
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


#make sets to make easier[[[][[\]]]
def get_triangles_for(node, adj_list):
    print('get_triangles_for')
    nodes_triangles = []
    for u in adj_list[node]:
        #print('u = '+str(u))
        for v in adj_list[node]:
            #print('v = '+str(v))
            if u in adj_list[v]:# and (v, u) not in nodes_triangles:
                #print(u, v)
                #print('\n')
                nodes_triangles += [(node, u, v)]

    return nodes_triangles

#######
def get_all_triangles(node_list, adj_list):
    print('get all triangles')
    all_triangles = []
    for node in node_list:
        all_triangles += get_triangles_for(node, adj_list)
    return all_triangles

######
def remove_duplicates(all_triangles):
    print('remove duplicates')
    sorted_triangles = []
    for triangle in all_triangles:
        assert(len(triangle) == 3)
        #print('sorted triangle' +str(sorted(triangle)))
        sorted_triangles += [tuple(sorted(triangle))]
    return list(set(sorted_triangles))

def get_node_label(node, pos_nodes, neg_nodes):
    
    if node in pos_nodes:
        label = 'pos'
    elif node in neg_nodes:
        label = 'neg'
    else:
        label = 'u'

    return label
def get_key(tag):
    assert(len(tag) == 12 or len(tag) == 10 or len(tag) == 8 or len(tag) == 6)
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
    else: print('exception = ' +tag)

    return 0

######
def get_tag(triangle, pos_nodes, neg_nodes):
    print('getting tag for '+str(triangle))
    assert(len(triangle) == 3)
    tag = ''    
    for node in triangle:
        label = get_node_label(node, pos_nodes, neg_nodes)
        tag+= label +str('_')
    return get_key(tag)


### get master triangle dictionary
# uses all the triangles

def get_triangle_dictionary(all_triangles, pos_nodes, neg_nodes, all_keys):
    
    # Initialize an empty dictionary with all possible combinations of labels
    triangles_dict = {}
    for key in all_keys:
        #print('Initializing keys, key = '+str(key)+' len = '+str(len(key)))
        assert(len(key) == 12 or len(key) == 10 or len(key) == 8 or len(key) == 6)
        triangles_dict[key] = []
    #print(triangles_dict)
    #print('\n')
    #print('len triangles_dict = '+str(len(triangles_dict)))
    #print('len all keys = '+str(len(all_keys)))
    assert(len(triangles_dict) == len(all_keys))
    for triangle in all_triangles:
        #print('current triangle in get_triangle_dict = '+str(triangle))
        assert(len(triangle) == 3)
        key = get_tag(triangle, pos_nodes, neg_nodes)
        
        triangles_dict[key] += [triangle]
    return triangles_dict
        
def get_highlighted_edges(all_triangles):
    print('get highlighted edges')
    highlighted_edges = []
    for triangle in all_triangles:
        highlighted_edges += [[triangle[0], triangle[1]], 
                              [triangle[0], triangle[2]],
                              [triangle[1], triangle[2]]]
    # Set them so that they're easier to look up in viz_graph
    return highlighted_edges

## author: Anna Ritz, modified by aliya  ghassaei
## Posts the graph G to GraphSpace and shares it with the group.
## Prompts the user for graph name, email, and password.
## param G: GSGraph object
## param post_group: share with the group (default True).
##  (note: you can prevent sharing by specifying post_group=False)

# how to make public?

def post_to_graphspace(G,post_group=True):
    ## connect to the GraphSpace client.
    group='BIO331F21' #fix this?
    graph_name = input('Enter Graph Name:')
    G.set_name(graph_name)
    #email = input('Enter Email:')
    #password = input('Enter Password:')
    #gs = GraphSpace(email,password)
    gs = GraphSpace('aghassaei@reed.edu', 'contrasenajaja24')
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
    #print('Done!')
    return

#############
# Builds GraphSpace graph from reduced set of nodes and edges
# Modified from Anna's viz_graph function in build-example.py
# INPUTS: pruned node list, pruned edge list, predctions as dictionary, zip/sqh
# RETURNS: None, just posts graph
###akdjfaksdf cgeck spelling on nmii
#############
def viz_graph_example(nodes, edges, highlighted_edges, pos_nodes, neg_nodes, special):
    print('Visualizing graph...')
    G = GSGraph() # Create a graph object
    G.set_tags(['HW4']) ## tags help you organize your graphs
    counter = 0
    for n in nodes:
        #print(n)
        if n in set(pos_nodes) and n not in special: 
            #print('first condition')
            color = '#ea00b5' 
        elif n in set(neg_nodes):
            #print('second condition')
            color = '#00b5ea' 
        elif n in special:
            #print('special!')
            color = '#9e007a'
        #random color, if unlabeled
        else:
            #print('else')
            color = '#b5ea00'
        G.add_node(n,label=n)    
        G.add_node_style(n,color=color,shape='ellipse',height=40,width=40)
        # popup?
        counter+=1
    assert(counter == len(nodes))
    for edge in edges:
        if edge in highlighted_edges or [edge[1], edge[0]] in highlighted_edges:
            G.add_edge(edge[0], edge[1])
            G.add_edge_style(edge[0], edge[1],width=4)
        else:
            G.add_edge(edge[0], edge[1])
            G.add_edge_style(edge[0], edge[1],width=2)
    post_to_graphspace(G)
    return

#############
# Builds GraphSpace graph from reduced set of nodes and edges
# Modified from Anna's viz_graph function in build-example.py
# INPUTS: pruned node list, pruned edge list, predctions as dictionary, zip/sqh
# RETURNS: None, just posts graph
###akdjfaksdf cgeck spelling on nmii
#############s
def viz_graph(triangle_nodes, edges_to_post, pos_nodes, neg_nodes, special):
    assert('zip' in pos_nodes)
    assert('zip' in special)
    assert('sqh' in pos_nodes)
    assert('sqh' in special)
    assert('zip' in triangle_nodes)
    assert('sqh' in triangle_nodes)
    print('Visualizing graph...')
    G = GSGraph() # Create a graph object
    
    ##### change graph tags
    G.set_tags(['HW4']) ## tags help you organize your graphs
    counter = 0
    print('going through the nodes in viz graph')
    for n in triangle_nodes:
        #print('n = ' +str(n))
        if n in pos_nodes: 
            if n not in special:#print('in pos')
                color = '#ea00b5'
                height=40
                width=40
            else:
                print('special')
                color = '#9e007a'
                height = 50
                width = 50
        if n in neg_nodes:
            #print('in neg')
            color = '#00b5ea'
            height=40
            width=40
        if n not in set(neg_nodes) and n not in set(pos_nodes):
        #random color, if unlabeled
        
            #print('unlabeled')
            color = '#b5ea00'
            height=40
            width=40
        G.add_node(n,label=n)    
        G.add_node_style(n,color=color,shape='ellipse',height=height,width=width)
        # popup?
        counter+=1
    assert(counter == len(triangle_nodes))
    print('going through edges in viz graph')
    for edge in edges_to_post:
        if edge[0] not in triangle_nodes:
            print(edge[0])
        if edge[1] not in triangle_nodes:
            print(edge[1])
        #print(edge)
        G.add_edge(edge[0], edge[1])
        G.add_edge_style(edge[0], edge[1],width=2)
    post_to_graphspace(G)
    return

def print_results(triangles_dict, all_triangles):
    print('RESULTS')
    total = len(all_triangles)
    total_per = 0
    print('there were '+str(total)+' connected to zip and s')
    for key in triangles_dict:
        count = len(triangles_dict[key])
        percentage = 100*(len(triangles_dict[key])/total)
        total_per += percentage
        print('there were '+str(count)+' triangles of type '
              +str(key)+', which made up '+str(percentage)+' of the triangles')
    print('total = '+str(total_per))
    
    return None
    
    
    

