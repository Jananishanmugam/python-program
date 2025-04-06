class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BT:
    def inorder_traversal(self,root):
        if root is None:
            return []
        return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)
    def preorder_traversal(self,root):
        if root is None:
            return []
        return [root.val] + self.preorder_traversal(root.left) + self.preorder_traversal(root.right)
    def postorder_traversal(self,root):
        if root is None:
            return []
        return self.postorder_traversal(root.left) + self.postorder_traversal(root.right) + [root.val]
    
    def sort_array(self,node):
        inorder_list = self.inorder_traversal(node)
        inorder_list.sort()
        # print(inorder_list)
        return inorder_list
    
    def replace_values(self,node,sorted_values,index):
        if node:
            index = self.replace_values(node.left,sorted_values,index)
            node.val = sorted_values[index]
            index+=1
            index = self.replace_values(node.right,sorted_values,index)
        return index    
    
    def BT_to_BST(self,root):
        sorted_values = self.sort_array(root)
        self.replace_values(root,sorted_values,0)
        return root


# Example usage
# Constructing the tree:
#       1
#    /    \
#   4      2
#  / \       \
# 5   6       7

root = TreeNode(1)
root.left = TreeNode(4)
left_child = root.left
left_child.left = TreeNode(5)
left_child.right = TreeNode(6)
root.right = TreeNode(2)
right_child = root.right
right_child.right = TreeNode(7)


#convert BT to BST
bt = BT()
print(bt.inorder_traversal(root))
bt.BT_to_BST(root)
print(bt.inorder_traversal(root))
