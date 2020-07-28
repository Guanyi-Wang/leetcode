"""
     3
   /    \
  9    20
 / \   /  \
 1 10 15   7
inorder = [1,9,10,3,15,20,7]  (left, root, right)
postorder = [1,10,9,15,7,20,3] (left, right, root)
root always postorder[-1] -> 3
left subtree: inorder[:root] -> [1,9,10] root of subtree: postorder[-1]:[1,10,9][-1] = 9, left:1, right:10
right subtree: inorder[root+1:] ->[15,20,7] root of subtree: [15,7,20][-1]=9, left=15,right=7

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # recursive function to build subtree with length l
        def build(i, p, l):
            """
            i: start index in inorder list for subtree
            p: start index in postorder list for subtree
            l: length of subtree
            """
            print(i, p, l)
            if l <= 0:
                return None
            # build root of this subtree
            root = TreeNode(postorder[p + l - 1])  # root is the last in postorder list
            if l == 1:
                return root
            # separate left and right subtree in inorder list using root
            j = i
            while inorder[j] != root.val:  # find root index in inorder list
                j = j + 1
            l_left = j - i  # length of left subtree
            root.left = build(i, p, l_left)
            l_right = (p + l - 1) - (p + l_left - 1) - 1  # calculated in postorder list: root-last_left-1
            root.right = build(j + 1, p + l_left, l_right)
            return root

        return build(0, 0, len(inorder))


"""
     3
   /    \
  9    20
 / \   /  \
 1 10 15   7
inorder = [1,9,10,3,15,20,7]  (left, root, right)
postorder = [1,10,9,15,7,20,3] (left, right, root)
root always postorder[-1] -> 3
left subtree: inorder[:root] -> [1,9,10] root of subtree: postorder[-1]:[1,10,9][-1] = 9, left:1, right:10
right subtree: inorder[root+1:] ->[15,20,7] root of subtree: [15,7,20][-1]=9, left=15,right=7

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # use a dict to store value: index pairs of inorder to reduce look up time
        in_dict = {}
        for i, v in enumerate(inorder):
            in_dict[v] = i
        p_index = -1  # index of root in postorder
        # recursive function to build subtree
        def build(start, end):
            """
            start: start index in inorder list for subtree
            end: end index in inorder list for subtree
            """
            nonlocal p_index # use nonlocal instead of global because p_index is defined in enclosure function
            if end < start:
                return None
            # build root of this subtree
            root = TreeNode(postorder[p_index]) # root is the last in postorder list of subtree
            p_index -= 1
            if start == end:
                return root
            # seperate left and right subtree in inorder list using root
            r = in_dict[root.val] #find root index in inorder list
            # build right subtree first because of the order postorder[-1] is root of right subtree
            root.right = build(r+1, end)
            root.left = build(start, r-1)
            return root
        return build(0,len(inorder)-1)
