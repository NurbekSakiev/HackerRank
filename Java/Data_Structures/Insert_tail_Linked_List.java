// Hacker Rank (www.hackerrank.com)
// Insert a node at the tail of a linked list
// author: Nurbek Sakiev

/*
  Insert Node at the end of a linked list 
  head pointer input could be NULL as well for empty list
  Node is defined as 
  class Node {
     int data;
     Node next;
  }
*/
Node Insert(Node head,int x) {
// This is a "method-only" submission. 
// You only need to complete this method. 
    Node tail = new Node();
    tail.data = x;
    tail.next = null;
    
    if (head == null) {
        head = tail;
    }
    else {
        Node temp = head;
        while(temp.next != null) {
            temp = temp.next;
        }
        temp.next = tail;
    }
   return head; 
}
