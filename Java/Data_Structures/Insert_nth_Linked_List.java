// Hacker Rank (www.hackerrank.com)
// Insert a node at a specific position in a linked list
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

Node InsertNth(Node head, int data, int position) {
    Node newNode = new Node();
    newNode.data = data;
    newNode.next = null;
    
    Node temp = head;
    if (position == 0) {
        newNode.next = head;
        head = newNode;
    }
    else {
        for(int i = 1; i<position;i++) {
            temp = temp.next;
        }
        newNode.next = temp.next;
        temp.next = newNode;
    }
    
    return head;
}
