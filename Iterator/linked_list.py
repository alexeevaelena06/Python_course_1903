#  Alekseeva Elena


class Node:
    """Class for node of Singly Linked List
    Singly linked lists contain nodes which have a data field
    as well as 'next' field,
    which points to the next node in line of nodes"""

    def __init__(self, data=None, next_node=None):
        """Constructor to initiate this object"""
        self.data = data
        self.next_node = next_node

    def __eq__(self, other):
        """
        Define comparison between nodes for unit testing
        """
        return self.data == other.data and self.next_node == other.next_node

    def get_data(self):
        """Get data of Node"""
        return self.data

    def get_next(self):
        """Get next node"""
        return self.next_node

    def set_next(self, new_next):
        """Set data for next node"""
        self.next_node = new_next


class LinkedList:
    """Class for Singly linked list
    Definition: A linked list is a sequence of data elements, which are connected together via links.
    Each data element contains a connection to another data element in form of a pointer
    """

    def __init__(self, head=None):
        """Constructor to initiate this object"""
        self.head = head

    def __len__(self):
        """Length of LinkedList"""
        size = 0
        for _ in self:
            size += 1
        return size

    def __iter__(self):
        """Create an iterator. Return itself.
        """
        current = self.head
        while current:
            node = self.current
            self.current = self.current.next_node
            yield node

    def __repr__(self):
        """Traverse LinkedList"""
        if self.head is None:
            raise KeyError("LinkedList has no element")
        return ", ".join(node.data for node in self)
