# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。 
# 
#  如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。 
# 
#  您可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  示例： 
# 
#  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#  
#  Related Topics 链表 数学


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return ('%s, %s') % (self.val, self.next)


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        h = curr = l1
        over = 0

        while l1 or l2:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + over
            curr = l1 or l2
            curr.val = sum % 10
            over = int(sum / 10)
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
            curr.next = l1 or l2

        if over > 0:
            curr.next = ListNode(1)

        return h


# 解答失败: 测试用例:[1,8] [0] 测试结果:[8,1] 期望结果:[1,8] stdout:
# 解答失败: 测试用例:[9,8] [1] 测试结果:[8,0,1] 期望结果:[0,9] stdout:
# 解答失败: 测试用例:[2,4,3] [5,6,4] 测试结果:[8,0,7] 期望结果:[7,0,8] stdout: 1, 8, 0, None

# rst = Solution().addTwoNumbers(
#     ListNode(2, ListNode(4, ListNode(3, None))),
#     ListNode(5, ListNode(6, ListNode(4, None)))
# )
# rst = Solution().addTwoNumbers(
#     ListNode(2, ListNode(4, ListNode(3, None))),
#     ListNode(5, ListNode(6, None))
# )
# rst = Solution().addTwoNumbers(
#     ListNode(2, ListNode(4, ListNode(3, None))),
#     ListNode(9, None)
# )
# rst = Solution().addTwoNumbers(
#     ListNode(9, ListNode(8, None)),
#     ListNode(1, None)
# )
l1 = ListNode(1)
l2 = ListNode(9)
l2.next = ListNode(9)

rst = Solution().addTwoNumbers(l1, l2)

print(rst)

a = l1 or l2
print(a)
