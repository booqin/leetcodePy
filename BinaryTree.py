# Definition for a binary tree node.
# 前序遍历


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        resultList = []
        self.setList(resultList, root)
        return resultList

    def setList(self, resultList, node):
        if node:
            resultList.append(node.val)
            self.setList(resultList, node.left)
            self.setList(resultList, node.right)

if __name__ == '__main__':
    root = TreeNode(1)
    rootRight = TreeNode(2)
    rootRight.left = TreeNode(3)
    root.right = rootRight

    solution = Solution()

    print(solution.preorderTraversal(root))
