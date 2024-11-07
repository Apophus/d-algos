/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        let head = ListNode
        let curr = head
        let carry = 0
        while (l1 or l2 or carry){
            let val1 = l1.val || 0
            let val2 = l2.val || 0
            let sum = val1 + val2 + carry
            carry = Math.floor(sum/10)
            let val = sum%10
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1 ? l1.next : null;
            l2 = l2? l2.next : null;
        }
        return head.next

    }
}