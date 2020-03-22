from typing import List

class Node:
    def __init__(self, k):
        self.key = k
        self.value = 1
        self.left = None
        self.right = None

class BST:
    # node.left.key < node.key < node.right.key

    # pass root when constructing a tree
    def __init__(self, k):
        self.root = Node(k)

    def add(self, k):
        node, parent = self.root, None

        while node is not None:
            if node.key > k:
                node = node.left

            if node.key < k:
                node = node.right

    def print(self, ):
        print(self.printNode(self.root))

    def printNode(self, node) -> str:
        return "["+node.key+" "+node.value + "(" + self.printNode(node.left) + "," + self.printNode(node.right) +")" if node.key is None else ""


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        return
        bst = BST()
        for i in range(len(nums)):
            bst.add(nums[i])

        bst.print()
        return 123


s = Solution()
#a = s.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)
#b = s.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2)
#c = s.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3)
#print(a,b,c)

bst = BST(2)
#bst.add(1)
#bst.add(3)
print(bst.root.key)
print(bst.root.left)
print(bst.root.right)