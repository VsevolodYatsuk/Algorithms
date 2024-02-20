class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next


if __name__ == "__main__":
    linked_list = LinkedList()
    
    linked_list.insert_at_beginning(3)
    linked_list.insert_at_beginning(2)
    linked_list.insert_at_beginning(1)
    
    linked_list.insert_at_end(4)
    linked_list.insert_at_end(5)
    
    print("Исходный список:")
    linked_list.display() 
    
    linked_list.delete_node(3)
    print("\nСписок после удаления узла со значением 3:")
    linked_list.display() 