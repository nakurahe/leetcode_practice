/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode newHead = new ListNode(-1, head);
        ListNode previous = newHead;

        while (head != null) {
            if (head.val == val) {
                previous.next = head.next;
            } else {
                previous = previous.next;
            }
            head = head.next;
        }

        return newHead.next;
    }


    public static void main(String[] args) {
        Solution solution = new Solution();
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(6, new ListNode(3, new ListNode(4, new ListNode(5, new ListNode(6)))))));
        int val = 6;
        ListNode result = solution.removeElements(head, val);
        while (result != null) {
            System.out.println(result.val);
            result = result.next;
        }
    }
}