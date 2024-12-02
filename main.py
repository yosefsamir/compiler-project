from Lexer import *
from parser import *
from binarytree import *

def build_binary_tree(tree):
    if isinstance(tree, list):
        root = Node(tree[1])  # Middle element is the operator
        root.left = build_binary_tree(tree[0])
        root.right = build_binary_tree(tree[2])
        return root
    else:
        return Node(tree)  # Leaf node

# Read and process the input code
code = Lexer.read_code('code.j')
lexer = Lexer(code)
tokens = lexer.tokenize()
parser = Parser(tokens)
trees = parser.parse()

# Write the output to a file
with open('output.txt', 'w') as file:
    for tree in trees:
        root = build_binary_tree(tree)
        file.write(str(root) + '\n')  
