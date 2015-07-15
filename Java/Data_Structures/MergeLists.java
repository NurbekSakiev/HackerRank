// Hacker Rank (www.hackerrank.com)
// Merge two sorted linked lists
// author: Nurbek Sakiev

Node MergeLists(Node list1, Node list2) {
   
     // This is a "method-only" submission. 
     // You only need to complete this method 
    Node result = null;
    if(list1 == null) {
        return list2;
    }
    else if(list2 == null) {
        return list1;
    }
    if(list1.data <=list2.data) {
        result = list1;
        result.next = MergeLists(list1.next,list2);
    }
    else {
        result = list2;
        result.next = MergeLists(list2.next,list1);
    }
    return result;
}
