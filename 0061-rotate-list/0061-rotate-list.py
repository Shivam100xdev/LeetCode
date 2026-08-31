class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        count = 1
        last = head
        while last.next:
            last = last.next
            count += 1

        k %= count
        if k == 0:
            return head

        last.next = head
        current = head
        for _ in range(count - k - 1):
            current = current.next

        new_head = current.next
        current.next = None
        return new_head

