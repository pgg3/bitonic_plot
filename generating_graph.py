import networkx as nx
import matplotlib.pyplot as plt
import math

def add_comparator(G, u, v, stage, index):
    G.add_edge((u, stage), (v, stage), index=index)

def create_bitonic_sorting_network(n):
    G = nx.DiGraph()
    logn = int(math.log2(n))

    for i in range(logn):
        for j in range(n):
            index = (j // (2 ** i)) % 2
            partner = j ^ (2 ** i)
            if partner > j:
                if index == 0:
                    # Ascending
                    add_comparator(G, j, partner, i, j // (2 ** (i + 1)))
                else:
                    # Descending
                    add_comparator(G, partner, j, i, j // (2 ** (i + 1)))

    return G

if __name__ == '__main__':

    # Initialize a directed graph
    G = nx.DiGraph()

    # Assuming we have 8 elements to sort, we create 8 levels
    levels = 8

    # Create nodes, each level will have nodes equal to the number of elements to sort
    for level in range(levels):
        for i in range(levels):
            G.add_node((level, i), pos=(level, i))

    # Connect nodes to simulate comparisons and swaps
    # This is where you would implement the logic of your sorting network
    # For demonstration, this will just connect each node to the next level node
    for level in range(levels - 1):
        for i in range(levels):
            G.add_edge((level, i), (level + 1, i))

    # Extract positions
    pos = nx.get_node_attributes(G, 'pos')

    # Draw the graph using the positions we set for each node
    nx.draw(G, pos, with_labels=False, node_size=500, node_color="orange", arrows=True)

    # Show the plot
    plt.show()