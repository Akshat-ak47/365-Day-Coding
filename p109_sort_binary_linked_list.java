// Sort Binary Linked List

// Problem Description
// Given a Linked List A consisting of N nodes.
// The Linked List is binary i.e data values in the linked list nodes consist of only 0's and 1's.
// You need to sort the linked list and return the new linked list.

// NOTE:
// Try to do it in constant space.

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; next = null; }
}

public class p109_sort_binary_linked_list {
    public ListNode solve(ListNode A) {
        int[] count = new int[2];
        ListNode current = A;
        while (current != null) {
            count[current.val]++;
            current = current.next;
        }
        current = A;
        for (int i = 0; i < 2; i++) {
            while (count[i] > 0) {
                current.val = i;
                current = current.next;
                count[i]--;
            }
        }
        return A;
    }

    // Utility function to print the linked list
    public static void printLinkedList(ListNode head) {
        ListNode current = head;
        while (current != null) {
            System.out.print(current.val + " ");
            current = current.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Creating a sample binary linked list: 1 -> 0 -> 1 -> 0 -> 1
        ListNode head = new ListNode(1);
        head.next = new ListNode(0);
        head.next.next = new ListNode(1);
        head.next.next.next = new ListNode(0);
        head.next.next.next.next = new ListNode(1);

        p109_sort_binary_linked_list solution = new p109_sort_binary_linked_list();

        System.out.println("Original Linked List:");
        printLinkedList(head);

        // Sorting the linked list
        ListNode sortedList = solution.solve(head);

        System.out.println("Sorted Linked List:");
        printLinkedList(sortedList);
    }
}
