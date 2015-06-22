
// Hacker Rank (www.hackerrank.com)
// Compare two linked lists
// author: Nurbek Sakiev

int CompareLists(Node headA, Node headB) {
    while((headA!=null) || (headB !=null)) {
        if((headA==null) || (headB == null)) {
            return 0;
        }
        
        if (headA.data != headB.data) {
            return 0;
        }
        else {
            headA = headA.next;
            headB = headB.next;
        }    
    }
    return 1;

}
