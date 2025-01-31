class Solution {
    public ListNode removeElements(ListNode head, int val) {
        if (head == null || (head.val == val && head.next == null)) {
            return new ListNode();
        }

        ListNode newHead = head;
        ListNode previous = head;
        head = head.next;

        while (head != null) {
            if (head.val == val) {
                previous.next = head.next;
                previous = previous.next;
            } else {
                previous = head;
                head = head.next;
            }
        }
        
        return newHead;
    }
}