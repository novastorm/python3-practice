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

    def find_kth_largest(self,root,k):
        # Return Element should be of type TreeNode

        class OutOrderIterator:
            def __init__(self, node):
                self.stack = []
                curr = node
                while curr:
                    self.stack.append(curr)
                    curr = curr.right_child

            def __iter__(self):
                return self

            def __next__(self):
                if not self.stack:
                    raise StopIteration

                next = self.stack.pop()
                curr = next.left_child

                while curr:
                    self.stack.append(curr)
                    curr = curr.right

                return next.data

        iter = OutOrderIterator(self)

        return iter[k]
