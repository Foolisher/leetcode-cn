# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。 
# 
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  
# 
#  示例: 
# 
#  给定 0-> 1->2->3->4, 你应该返回 2->1->4->3.
#  
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return head
        h = ListNode(0)
        h.next = head
        p = h
        curr = head

        while curr and curr.next:
            n = curr.next
            nn = n.next
            p.next = n
            n.next = curr
            curr.next = nn
            p = curr
            curr = nn

        return h.next


h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
rst = Solution().swapPairs(h)

# leetcode submit region end(Prohibit modification and deletion)
