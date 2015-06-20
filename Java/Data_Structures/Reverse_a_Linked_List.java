// Hacker Rank (www.hackerrank.com)
// Reverse a linked list
// author: Nurbek Sakiev

Node head;

Node Reverse(Node p) {

	if (p.next == null) {
		head = p;
		return head;
	}
	Reverse(p.next);

	Node q = p.next;
	q.next = p;
	p.next = null;

	return head;
}