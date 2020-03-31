# Alekseeva Elena


class Node(object):
    """Class for node of Singly Linked List
    Singly linked lists contain nodes which have a data field
    as well as 'next' field,
    which points to the next node in line of nodes"""

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    """Class for Singly linked list
    Definition: A linked list is a sequence of data elements, which are connected together via links.
    Each data element contains a connection to another data element in form of a pointer
    """

    def __init__(self, head=None):
        self.head = head

    def traverse_list(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data, " ")
                n = n.next_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def insert_at_end(self, data):
        """Equal to append()"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next_node is not None:
            n = n.next_node
        n.next_node = new_node

    def insert_after_item(self, x, data):
        n = self.head
        print(n.next_node)
        while n is not None:
            if n.data == x:
                break
            n = n.next_node
        if n is None:
            print("Data not in the list")
        else:
            new_node = Node(data)
            new_node.next_node = n.next_node
            n.next_node = new_node

    def insert_before_item(self, x, data):
        if self.head is None:
            print("List has no element")
            return

        if x == self.head.data:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node
            return

        n = self.head
        print(n.next_node)
        while n.next_node is not None:
            if n.next_node.data == x:
                break
            n = n.next_node
        if n.next_node is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.next_node = n.next_node
            n.next_node = new_node

    def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node
        i = 1
        n = self.head
        while i < index - 1 and n is not None:
            n = n.next_node
            i = i + 1
        if n is None:
            print("Index out of bound")
        else:
            new_node = Node(data)
            new_node.next_node = n.next_node
            n.next_node = new_node

    def get_count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete_at_start(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        self.head = self.head.next_node

    def delete_at_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        n = self.head
        while n.next_node.next_node is not None:
            n = n.next_node
        n.next_node = None

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def reverse_llist(self):
        previous = None
        current = self.head
        while current is not None:
            following = current.next_node
            current.next_node = previous
            previous = current
            current = following
        self.head = previous

    def make_new_list(self):
        nums = int(input("How many nodes do you want to create: "))
        if nums == 0:
            return
        for i in range(nums):
            value = int(input("Enter the value for the node:"))
            self.insert_at_end(value)

# Test


new_linked_list = LinkedList()

new_linked_list.make_new_list()

new_linked_list.insert_at_end(1)
new_linked_list.traverse_list()
new_linked_list.insert_at_end(2)
new_linked_list.traverse_list()
new_linked_list.insert_at_end(3)
new_linked_list.insert_at_start(0)
new_linked_list.insert_after_item(3, 5)
new_linked_list.insert_before_item(5, 4)
new_linked_list.insert_at_index(7, 6)
new_linked_list.traverse_list()
print(f"After action: {new_linked_list.get_count()}")
new_linked_list.delete(0)
new_linked_list.traverse_list()
print(f"After action: {new_linked_list.get_count()}")
new_linked_list.search(1)
new_linked_list.traverse_list()
print(f"After action: {new_linked_list.get_count()}")
