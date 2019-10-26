import binaryTree

from binaryTree import TreeNode

class BinaryTree(binaryTree.BinaryTree):

    def diameter(self, root):
        return self.diameter_1(root)

    def diameter_1(self,root):

        class Height:
            def __init__(self, h=0):
                self.h = h

        def helper(node, height):
            leftHeight = Height()
            rightHeight = Height()
            
            if not node:
                height.h = 0
                return 0
                
            leftHeight.h += 1
            rightHeight.h += 1
            
            leftDiameter = helper(node.left_child, leftHeight)
            rightDiameter = helper(node.right_child, rightHeight)
            
            height.h = max(leftHeight.h, rightHeight.h) + 1
            
            return max(
                leftHeight.h + rightHeight.h + 1,
                max(leftDiameter, rightDiameter)
                )
                
        return helper(root, Height())

    def diameter_2(self, node):

        def helper(node):
            if not node:
                return (0, 0)

            left_height, left_max_diameter = self.diameter_recursive(node.left_child)
            right_height, right_max_diameter = self.diameter_recursive(node.right_child)

            height = max(left_height, right_height) + 1
            max_diameter = max(left_height + right_height + 1, left_max_diameter, right_max_diameter)

            return (height, max_diameter)

        _, diameter = helper(node)
        return diameter

    def diameter_3(self, node):
        def helper(node):
            if node is None:
                return (0, 0)

            left = helper(node.left_child)
            right = helper(node.right_child)

            return (
                max( 1 + le)
            )
        