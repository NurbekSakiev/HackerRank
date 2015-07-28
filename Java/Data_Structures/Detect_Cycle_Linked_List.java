// Hacker Rank (www.hackerrank.com)
// Detect Cycle
// author: Nurbek Sakiev

int HasCycle(Node head) {
    if(head == null) {
        return 0;
    }
    Node slow, fast;
    slow =fast = head;
    
    while(true) {
        slow = slow.next;
        if(fast.next !=null) {
            fast = fast.next.next;
        }
        else
            return 0;
        if (slow == null || fast == null) {
            return 0;
        }
        if (slow == fast) {
            return 1;
        }
    }
}
