# Alekseeva Elena


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
        Defining comparison between nodes for unit testing
        """
        if self.data == other.data and self.next_node == other.next_node:
            return True
        else:
            return False

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
        self._size = 0
        self.__current = self.head

    def __len__(self):
        """Length of LinkedList"""
        while self.__current:
            self._size += 1
            self.__current = self.__current.next_node
        return self._size

    def __iter__(self):
        """Create an iterator. Return itself.
        """
        while self.__current:
            current = self.__current
            self.__current = self.__current.next
            yield current
        self.__current = self.head

    def __next__(self):
        """
        Provides the next entry to the iterator
        """
        if not self.__current:
            self.__current = self.head
            raise StopIteration
        current = self.__current
        self.__current = self.__current.next_node
        return current

    def traverse_list(self):
        """Traverse LinkedList"""
        if self.head is None:
            raise KeyError("LinkedList has no element")
        else:
            while self.__current is not None:
                print(self.__current.data, " ")
                self.__current = self.__current.next_node
