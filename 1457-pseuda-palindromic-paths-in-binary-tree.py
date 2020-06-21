from functools import reduce

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:    
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def checkFreqPseudoPalindrome(freq):
            return 1 if reduce(lambda cnt,x: cnt + (x % 2), freq.values(), 0) <=1 else 0

        def getResultForLeafs(node: TreeNode, freq):
            if node is None:
                return 0
            freq[node.val] = freq.get(node.val, 0) + 1
            res = checkFreqPseudoPalindrome(freq) if node.left is None and node.right is None else getResultForLeafs(node.left, freq) + getResultForLeafs(node.right, freq)
            freq[node.val] = freq.get(node.val, 0) - 1
            return res
                
        return getResultForLeafs(root, {})

def test(arr_tree):
    def constructNode(idx):
        return TreeNode(arr_tree[idx], constructNode(2*idx + 1), constructNode(2*idx + 2)) if idx < len(arr_tree) and arr_tree[idx] is not None else None    
    solution = Solution()
    return solution.pseudoPalindromicPaths(constructNode(0))

assert test([9]) == 1 
assert test([2,3,1,3,1,None,1]) == 2
assert test([2,1,1,1,3,None,None,None,None,None,1]) == 1

        