// Hacker Rank (www.hackerrank.com)
// Insert a node at the head of a linked list
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
// This is a "method-only" submission. 
// You only need to complete this method. 

Node Insert(Node head,int x) {
    Node newHead = new Node();
    newHead.data = x;
    newHead.next = null;
    
    newHead.next = head;
    head = newHead;
    return head;
}
