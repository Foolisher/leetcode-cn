# 给定一个二叉树，返回它的中序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 
# 输出: [1,3,2] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return '%s %s, %s' % (self.val, self.left or '', self.right or '')


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        rst = []
        if not root: return rst
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            top = stack.pop()
            rst.append(top.val)
            root = top.right

        return rst


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

rst = Solution().inorderTraversal(root)
print(rst)
