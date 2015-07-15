// Hacker Rank (www.hackerrank.com)
// Get Node Value
// author: Nurbek Sakiev

int GetNode(Node head,int n) {
     // This is a "method-only" submission. 
     // You only need to complete this method. 
    if (head == null) {
        return 0;
    }
    Node temp = head;
    int count = 0;
    while (temp.next != null) {
        count++;
        temp = temp.next;
    }
    int rem = count-n;
   
    while (rem !=0) {
        head = head.next;
        rem--;
    }
    
    return head.data;
   
}
