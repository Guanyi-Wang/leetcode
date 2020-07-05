"""
DP: bottom up
since n> n-1, node n can only be root of subtree n-1 or right most child in each level.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []
        res = []
        root = TreeNode(1)
        res.append(root)
        if n == 1:
            return res
        # add one node each time
        for i in range(2, n + 1):
            pre = res
            res = []
            for node in pre:
                # previous tree as left child
                res.append(TreeNode(i, left=node))
                # new node as right most child in each possible level
                for j in range(i + 1):  # at most i levels
                    root = copy.deepcopy(node)  # copy in each time
                    cur = root
                    for k in range(j):  # find right child in kth level
                        if cur:
                            cur = cur.right
                        else:
                            break
                    if not cur:
                        break
                    # if cur has right child, right child become left child of newnode
                    if cur.right:
                        temp = cur.right
                        new_node = TreeNode(i, left=temp)
                        cur.right = new_node
                    else:
                        cur.right = TreeNode(i)
                    res.append(root)
        return res



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []
        def gT(l,r):
            nodes = []
            for i in range(l, r+1):
                for left in gT(l,i-1) or [None]:
                    for right in gT(i+1,r) or [None]:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        nodes.append(root)
            return nodes
        return gT(1,n)

