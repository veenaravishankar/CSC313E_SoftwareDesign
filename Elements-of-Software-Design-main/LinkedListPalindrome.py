class Node:
   """A simple node for a singly linked list."""
   def __init__(self, data=0, next_node=None):
       self.data = data
       self.next = next_node


class LinkedList:
   """A simple linked list class for demonstration purposes."""
   def __init__(self):
       self.head = None


   def append(self, data):
       """Appends a new node with the given data to the end of the list."""
       if not self.head:
           self.head = Node(data)
           return
       current = self.head
       while current.next:
           current = current.next
       current.next = Node(data)


   def print_list(self):
       """Prints the elements of the list."""
       nodes = []
       current = self.head
       while current:
           nodes.append(str(current.data))
           current = current.next
       print(" -> ".join(nodes))


def reverse_and_clone(node):
   """
   This function intends to reverse and clone a linked list.


   Args:
       node: The head node of the linked list to reverse and clone.


   Returns:
       The head node of the new, reversed linked list.

   COMPLETE THE FUNCTION
   """
   new_head = None

   while node is not None:
       #clone the node by creating a new one with same data
       n = Node(node.data) #B#E#V#O
       #prepend the new node to the reversed list
       n.next = new_head # O-->V-->E-->B-->None
       new_head = n

       #move to the next node in the original list
       node = node.next
   return new_head


def is_equal(one, two):
   """
   This function intends to compare two linked lists to see if they are identical.


   Args:
       one: The head node of the first linked list.
       two: The head node of the second linked list.


   Returns:
       True if the lists are equal, False otherwise.


   COMPLETE THIS FUNCTION
   """
   while one is not None and two is not None:
       #B-E-V-O #O-V-E-B
       #1-3-1 #1-3-1
       if one.data != two.data:
           return False
       one = one.next
       two = two.next
   #if both LL are now empty,they are of sme lt and are equal.
   #if one is empty and the other is not, they are not equal
   return one is None and two is None



def is_palindrome(head):
   reversed_head = reverse_and_clone(head)
   return is_equal(head, reversed_head)

ll = LinkedList()
for char in ['B', 'E', 'V', 'O']:
    ll.append(char)

print("Original list:")
ll.print_list()

# Check if it's a palindrome
print("\nIs Palindrome?")
print(is_palindrome(ll.head))

ll2 = LinkedList()
for char in ['E', 'O', 'E']:
    ll2.append(char)

print("Original list:")
ll2.print_list()

# Check if it's a palindrome
print("\nIs Palindrome?")
print(is_palindrome(ll2.head))