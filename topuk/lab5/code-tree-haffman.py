import heapq
from collections import namedtuple
from graphviz import Digraph

# Define node structures for the Huffman Tree
class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc, graph=None, parent_id=None, edge_label=''):
        node_id = str(id(self))
        if graph is not None:
            graph.node(node_id, label="")
            if parent_id is not None:
                graph.edge(parent_id, node_id, label=edge_label)
        self.left.walk(code, acc + "0", graph, node_id, '0')
        self.right.walk(code, acc + "1", graph, node_id, '1')

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc, graph=None, parent_id=None, edge_label=''):
        code[self.char] = acc or "0"
        if graph is not None:
            node_id = str(id(self))
            graph.node(node_id, label=f'{self.char}\n{code[self.char]}')
            if parent_id is not None:
                graph.edge(parent_id, node_id, label=edge_label)

# Build the Huffman Tree
def huffman_tree(freqs):
    heap = []
    for char, freq in freqs.items():
        heap.append((freq, len(heap), Leaf(char)))
    heapq.heapify(heap)
    
    count = len(heap)
    while len(heap) > 1:
        freq1, _count1, left = heapq.heappop(heap)
        freq2, _count2, right = heapq.heappop(heap)
        heapq.heappush(heap, (freq1 + freq2, count, Node(left, right)))
        count += 1
    
    return heap[0][-1]

# Generate the Huffman Codes
def huffman_code(tree, graph=None):
    code = {}
    tree.walk(code, "", graph)
    return code

# Frequencies from the provided data
freqs = {
    'о': 0.101123596,
    'н': 0.076404494,
    'а': 0.071910112,
    'е': 0.065168539,
    'в': 0.058426966,
    'и': 0.056179775,
    'і': 0.056179775,
    'т': 0.053932584,
    'у': 0.042696629,
    'д': 0.040449438,
    'м': 0.038202247,
    'л': 0.035955056,
    'р': 0.035955056,
    'к': 0.033707865,
    'с': 0.033707865,
    'б': 0.029213483,
    'ч': 0.020224719,
    'п': 0.017977528,
    'ж': 0.015730337,
    'я': 0.015730337,
    'ц': 0.013483146,
    'щ': 0.013483146,
    'ь': 0.013483146,
    'х': 0.011235955,
    'з': 0.008988764,
    'й': 0.008988764,
    'ї': 0.008988764,
    'ш': 0.006741573,
    'ю': 0.006741573,
    'г': 0.004494382,
    'є': 0.004494382
}

# Build the Huffman Tree
tree = huffman_tree(freqs)

# Create a graphviz graph
graph = Digraph(format='png')
graph.attr('node', shape='circle')

# Generate Huffman Codes and visualize the tree
huffman_codes = huffman_code(tree, graph)

# Render the graph to a file
graph.render('/mnt/data/huffman_tree')

# Display Huffman Codes
huffman_codes
