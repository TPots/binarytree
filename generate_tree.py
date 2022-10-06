from BinaryTree import BinaryTree
from typing import Optional, TypeVar
import graphviz, uuid, random

def make_node(dot, node) -> str:
    id = uuid.uuid1().__str__()
    dot.node(id, str(node.value))
    
    child_id_left = None
    child_id_right = None
    
    if node.left is not None:
        child_id_left = make_node(dot, node.left)
        
    if node.right is not None:
        child_id_right = make_node(dot, node.right)
    
    if child_id_left is not None:
        dot.edge(id, child_id_left) 

    if child_id_right is not None:
        dot.edge(id, child_id_right)
 
    return id

def main() -> None:
    
    l = random.sample(range(0,999),50)
    tree = BinaryTree(l.pop())
    for value in l:
        tree.add(value)
    dot = graphviz.Digraph(comment='Binary Tree')
    make_node(dot, tree)
    
    dot.render('tree.gv', view = True)
    
    return None

if __name__ == '__main__':
    main()
