// Hacker Rank (www.hackerrank.com)
// Delete a Node
// author: Nurbek Sakiev

Node Delete(Node head, int position) {
    Node temp = head;
    if (position == 0) {
        head = head.next;
    }
    else if (position == 1) {
        head.next = head.next.next;
    }
    else {
        for (int i = 1; i<position; i++) {
            temp = temp.next;
        }
        temp.next = temp.next.next;
    }
    
    return head;
}

