import heapq
from graphviz import Digraph

# Вузол дерева Хаффмана
class Node:
    def __init__(self, probability, symbol, left=None, right=None):
        self.probability = probability
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''

    def __lt__(self, other):
        return self.probability < other.probability

# Функція побудови дерева Хаффмана
def build_huffman_tree(probabilities):
    heap = [Node(prob, sym) for sym, prob in probabilities.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(node1.probability + node2.probability, None, node1, node2)
        heapq.heappush(heap, merged)

    return heap[0]

# Функція присвоєння кодів Хаффмана
def assign_codes(node, code='', codes={}):
    if node:
        if node.symbol is not None:
            codes[node.symbol] = code
        assign_codes(node.left, code + '0', codes)
        assign_codes(node.right, code + '1', codes)
    return codes

# Функція для малювання дерева Хаффмана
def draw_huffman_tree(node, dot=None, node_id=0):
    if dot is None:
        dot = Digraph()
        dot.node(name=str(node_id), label=f'{node.probability:.2f}')

    if node.left:
        left_id = node_id * 2 + 1
        dot.node(name=str(left_id), label=f'{node.left.probability:.2f}')
        dot.edge(str(node_id), str(left_id), '0')
        draw_huffman_tree(node.left, dot, left_id)

    if node.right:
        right_id = node_id * 2 + 2
        dot.node(name=str(right_id), label=f'{node.right.probability:.2f}')
        dot.edge(str(node_id), str(right_id), '1')
        draw_huffman_tree(node.right, dot, right_id)

    return dot

# Зчитування ймовірностей з таблиці
probabilities = {
    '1': 0.140350877,
    '2': 0.122807018,
    '3': 0.087719298,
    '4': 0.070175439,
    '5': 0.052631579,
    '6': 0.035087719,
    '7': 0.01754386,
    '8': 0.01754386
}

# Побудова дерева Хаффмана
huffman_tree = build_huffman_tree(probabilities)

# Присвоєння кодів Хаффмана
huffman_codes = assign_codes(huffman_tree)

# Малювання дерева Хаффмана
dot = draw_huffman_tree(huffman_tree)
dot.render('huffman_tree', format='png', cleanup=False)

# Вивід кодів Хаффмана
for symbol, code in huffman_codes.items():
    print(f'Symbol: {symbol}, Huffman Code: {code}')
