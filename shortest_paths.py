
###################################
### Built w/ Python 3.9         ###
### Should Run in Python +3.6.x ###
###################################

from collections import deque


""" Inputs & Test Cases
"""
start_and_finish = ["A", "E"]
start_nodes =       ["A", "B", "B", "C", "D"]
connection_nodes =  ["B", "C", "D", "D", "E"]
# start_nodes =       ["A", "B", "B", "C", "C"]
# connection_nodes =  ["B", "C", "D", "D", "E"]
# start_nodes =       ["A", "A", "A", "B", "C", "D"]
# connection_nodes =  ["B", "C", "D", "E", "E", "E"]

"""
        A - B - C        A - B - C - E            A 
            |  /             |  /               / | \
            D                D                 B  C  D    
            |                                   \ | /
            E                                     E
"""

# Build the Graph
def build_graph(start_nodes, connection_nodes):

    graph = {}
    for i in range(len(start_nodes)):

        if start_nodes[i] not in graph.keys():     # If Starting Node not already in Dictionary, add it & it's connecttion
            graph[start_nodes[i]] = [connection_nodes[i]]

        else:                               # If Starting Node already in Dictionary, update it's connections
            current_node_list = graph[start_nodes[i]]
            current_node_list.append(connection_nodes[i])
            graph[start_nodes[i]] = current_node_list

    return graph


# Find the Shortest Path from Start to Finish
def define_shortest_paths(start_and_finish, graph, connection_nodes):

    shortest_paths = {}
    queue = deque()

    if start_and_finish[0] in graph:                        # Base Case // Only Start if Starting Node is in Graph
        shortest_paths[start_and_finish[0]] = [start_and_finish[0]]

        for child in graph[start_and_finish[0]]:            # Base Case // Add the Starting Node & Start forming Queue
            queue.append(child)
            shortest_paths[child] = shortest_paths[start_and_finish[0]] + [child]   # Shortest Path Child = Shortest Path to Parent + Child

        if start_and_finish[1] not in connection_nodes:     # Base Case // If Finish Node not connected in Graph, Return -1
            return -1

    while queue:

        node = queue.popleft()

        if node == start_and_finish[1]:             # End Case // If Current Node == Final Node as denoted by Input

            print(f"   Shortest Paths: {shortest_paths}\n")

            ''' HERE - I would search for alternative paths, finding all equally short paths via recursively visiting the parent
                        nodes, adding them to a list, comparing the length of the list to the "shortest_path[node]" (chosen & returned below)
                        and incrementing a counter each time said list matches the length of the currently decided "shortest_path[node]"
            '''

            # Returned here is the first, shortest_path to the Final Node & the Number of Steps to get from Start to Final Node
            return shortest_paths[node], len(shortest_paths[node])-1


        for child in graph[node]:
            if child not in shortest_paths:           # Set shortest_path to Child

                queue.append(child)
                shortest_paths[child] = shortest_paths[node] + [child]   # Shortest Path Child = Shortest Path to Parent + Child


if __name__ == "__main__":
    graph = build_graph(start_nodes, connection_nodes)
    print(f"\n   Graph: {graph}\n")
    shortest_path, num_of_steps = define_shortest_paths(start_and_finish, graph, connection_nodes)
    print(f"   FINISH - Shortest Path to {shortest_path[-1]}: {shortest_path}, Num of Steps: {num_of_steps}\n")