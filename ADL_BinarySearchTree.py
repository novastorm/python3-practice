from ADL_BinaryTree import *

class ADL_BinarySearchTree(ADL_BinaryTree):

    @property
    def isEmpty(self):
        raise NotImplementedError

    def insertValue(self, value):
        raise NotImplementedError


    def findValue(self):
        raise NotImplementedError


    def removeValue(self):
        raise NotImplementedError


    @staticmethod
    def isBinarySearchTree(tree):
        raise NotImplementedError


class ADL_BinarySearchTree_graph(ADL_BinarySearchTree):

    Node = ADL_BinaryTreeNode_Iterative

    def __init__(self):
        self._root = None

    def __len__(self):
        return len(self._root) if self._root else 0

    @property
    def breadthFirst(self):
        return self._root.breadthFirst if self._root else iter([])

    @property
    def preOrder(self):
        return self._root.preOrder if self._root else iter([])

    @property
    def inOrder(self):
        return self._root.inOrder if self._root else iter([])

    @property
    def outOrder(self):
        return self._root.outOrder if self._root else iter([])

    @property
    def postOrder(self):
        return self._root.postOrder if self._root else iter([])


    def insertValue(self, value):

        if self._root is None:
            self._root = self.Node(value)
            return

        self._insertNodeIterative(self._root, value)


    def _insertNodeRecursive(self, root, value):
        if root.value < value:
            if root.right is None:
                root.right = self.Node(value)
            else:
                self._insertNodeRecursive(root.right, value)
        else:
            if root.left is None:
                root.left = self.Node(value)
            else:
                self._insertNodeRecursive(root.left, value)


    def _insertNodeIterative(self, root, value):
        currNode = root
        while currNode:
            if currNode.value < value:
                if not currNode.right:
                    currNode.right = self.Node(value)
                    break
                currNode = currNode.right
            else:
                if not currNode.left:
                    currNode.left = self.Node(value)
                    break
                currNode = currNode.left


    def findValue(self, value):
        if not self._root:
            return False

        return self._findNodeIterative(self._root, value)


    def _findNodeRecursive(self, root, value):
        if not root:
            return False

        if root.value == value:
            return True

        if root.value < value:
            return self._findNodeRecursive(root.right, value)
        else:
            return self._findNodeRecursive(root.left, value)


    def _findNodeIterative(self, root, value):
        currNode = root

        while currNode:
            if currNode.value == value:
                return True

            if currNode.value < value:
                currNode = currNode.right
            else:
                currNode = currNode.left

        return False


    def removeValue(self, value):
        if not self.findValue(value):
            raise ValueError('value does not exist in collection')

        def promoteLeft():
            pass

        def promoteRight():
            pass

        deletionTargetParentNode = None # if none means self._root node
        isDeletionTargetParentNodeLeftChild = None
        deletionTargetNode = self._root

        replacementNodeParent = None
        replacementNode = None

        # find deletionTarget
        while deletionTargetNode:
            # print(currNode.value)
            if deletionTargetNode.value == value:
                break

            deletionTargetParentNode = deletionTargetNode
            if deletionTargetNode.value < value:
                isParentNodeLeft = False
                deletionTargetNode = deletionTargetNode.right
            else:
                isParentNodeLeft = True
                deletionTargetNode = deletionTargetNode.left

        if not deletionTargetNode.left and not deletionTargetNode.right:
            # print("No children")
            if deletionTargetParentNode is None:
                self._root = None
            elif isDeletionTargetParentNodeLeftChild:
                deletionTargetParentNode.left = None
            else:
                deletionTargetParentNode.right = None
        elif deletionTargetNode.left and not deletionTargetNode.right:
            # print("left child only")
            if deletionTargetParentNode is None:
                self._root = self._root.left
            elif isDeletionTargetParentNodeLeftChild:
                deletionTargetParentNode.left = deletionTargetNode.left
            else:
                deletionTargetParentNode.right = deletionTargetNode.left
        elif not deletionTargetNode.left and deletionTargetNode.right:
            # print("right child only")
            if deletionTargetParentNode is None:
                self._root = self._root.right
            elif isDeletionTargetParentNodeLeftChild:
                deletionTargetParentNode.left = deletionTargetNode.right
            else:
                deletionTargetParentNode.right = deletionTargetNode.right
        else:
            # in right node, find left most node
            # print("left and right child")
            replacementNode = deletionTargetNode.right
            if not replacementNode.left:
                # print("RN: ", replacementNode.value)
                if deletionTargetParentNode is None:
                    self._root.value = replacementNode.value
                    self._root.right = replacementNode.right
                else:
                    deletionTargetNode.value = deletionTargetNode.right.value
                    deletionTargetNode.right = deletionTargetNode.right.right
            else:
                replacementNodeParent = deletionTargetNode.right
                replacementNode = replacementNodeParent.left
                # print("RNP: ", replacementNodeParent.value, "RN: ", replacementNode.value)
                while replacementNode.left:
                    # print("RN: ", replacementNode, "RN-L: ", replacementNode.left)
                    replacementNodeParent = replacementNode
                    replacementNode = replacementNode.left

                if deletionTargetParentNode is None:
                    self._root.value = replacementNode.value
                else:
                    deletionTargetNode.value = replacementNode.value
                replacementNodeParent.left = replacementNode.right


class ADL_BinarySearchTree_list(ADL_BinarySearchTree):
    pass

