# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head) -> bool:
        slow, fast = head, head
        while head:
            if not head.next or not head.next.next:
                return False

            slow = head.next
            fast = head.next.next

            if fast.val == slow.val:
                return True

            head = head.next

        return False


print(Solution().hasCycle(ListNode(3)))  # False
