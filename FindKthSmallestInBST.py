class BinaryTree:
    
    def __init__(self, root_node = None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node
    
    # Helper Method    
    def size(self,root):
        if root == None:
            return 0
        else:
            return (self.size(root.left_child) + 1 + self.size(root.right_child)) 
        
    def find_kth_smallest(self, root, k):
        return self.find_kth_smallest_iteratively(root, k)

    def find_kth_smallest_iteratively(self,root,k):
        if not root:
            return None
        # Return element should be of Type TreeNode
        stack = []
        curr = root
        while curr:
            stack.append(curr)
            curr = curr.left_child
            
        while stack:
            node = stack.pop()
            
            curr = node.right_child
            while curr:
                stack.append(curr)
                curr = curr.left_child
                
            k -= 1
            
            if k <= 0:
                return node
                
        return None


###############################################################################

import unittest

class Test_BST_find_kth_smallest(unittest.TestCase):

    def setUp(self):
        pass

    def test_find_kth_smallest(self):
        pass

if __name__ == '__main__':
    unittest.main()
    