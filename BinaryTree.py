from typing import Optional, TypeVar

T = TypeVar('T', int, float)

class BinaryTree:
    value: T = None
    
    left: 'Optional[BinaryTree]' = None
    right: 'Optional[BinaryTree]' = None
    
    def __init__(self, value: T = None) -> None:
        self.value = value
        return None
        
    def add(self, value: T) -> None:
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.add(value)
        else:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.add(value)
        
        return
            
    def find(self, value: T) -> T:
        if value == self.value:
            return self.value
        elif value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.find(value)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(value)
            
def main() -> None:
    tree = BinaryTree()
    return None
    
if __name__ == '__main__':
    main()