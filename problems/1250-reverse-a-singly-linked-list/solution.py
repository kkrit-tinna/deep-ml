class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# 1. itrerative approach: Flip each node's next pointer to point backward, one node at a time
def iterative_reverse(head):
    prev = None
    curr = head
    while curr:
        # save copy of the current next
        nxt = curr.next
        # flip it backward
        curr.next = prev
        # move prev & curr forward
        prev = curr
        curr = nxt

    return prev

# 2. recursive approach: # Reverse everything after head, then hook head onto the end.
def recursive_reverse(head):
    # base case: no node or no next node
    if head is None or head.next is None:
        return head
    # recurse the rest
    new_head = recursive_reverse(head.next)
    # point the next pointer of the next node back to head
    head.next.next = head
    # cut curr head link to next
    head.next = None

    return new_head

def reverse_linked_list(values, method="iterative"):
    # values: list of node values in head-to-tail order
    # method: 'iterative' or 'recursive'
    # return: list of node values after reversal

    # step 1: build the linked list from python list
    ll = Node(None)
    tail = ll
    for v in values:
        # attach new node after the current tail
        tail.next = Node(v)
        # move tail towards the end
        tail = tail.next

    # real head (None if values is empty)
    head = ll.next        

    # step 2: reverse the ll based on chosen method
    if method == 'iterative':
        new_head = iterative_reverse(head)
    elif method == 'recursive':
        new_head = recursive_reverse(head)
    else:
        raise ValueError("method must be ierative or recursive")

    # step 3: convert ll to python list
    res = []
    curr = new_head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res