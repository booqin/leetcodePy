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
        前序遍历
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

    def levelOrder(self, root):
        """
        层次遍历（广度优先算法）
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        listQueue = []
        result = []
        next = [root]
        while next:
            listQueue = []
            currentList = []
            for index in range(len(next)):
                current = next[index]
                if current:
                    currentList.append(current.val)
                    listQueue.append(current.left)
                    listQueue.append(current.right)
            if currentList:
                result.append(currentList)
            next = listQueue

        return result

    def maxDepth(self, root):
        """
        最大深度，自低向上
        :type root: TreeNode
        :rtype: int
        """
        return self.bottom_up(root)

    def bottom_up(self, root):
        if not root:
            return 0
        left = self.bottom_up(root.left)
        right = self.bottom_up(root.right)

        return self.maxV(left, right) + 1

    def maxV(self, a, b):
        return a if a > b else b

if __name__ == '__main__':
    root = TreeNode(1)
    rootRight = TreeNode(2)
    rootRight.left = TreeNode(3)
    root.right = rootRight

    solution = Solution()

    print(solution.preorderTraversal(root))
