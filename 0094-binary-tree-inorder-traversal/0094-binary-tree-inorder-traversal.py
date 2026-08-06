# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = [] #for the answer

        def inorder(node): #create the function
            if node is None: #if nothing then return nothing
                return
            inorder(node.left) #first check left
            ans.append(node.val) #then check root
            inorder(node.right) #then check right

        inorder(root) #call the main function

        return ans