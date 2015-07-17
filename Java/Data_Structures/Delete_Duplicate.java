// Hacker Rank (www.hackerrank.com)
// Delete duplicate-value nodes from a sorted linked list
// author: Nurbek Sakiev

Node RemoveDuplicates(Node head) {
  // This is a "method-only" submission. 
  // You only need to complete this method. 
    Node temp = head;
    while(head.next != null) {
        if(head.data == head.next.data) {
            head.next = head.next.next;
        }
        else {
            head = head.next;    
        }
        
    }
    return temp;

}
