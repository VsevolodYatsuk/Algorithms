class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return item

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Пример использования
if __name__ == "__main__":
    queue = Queue()
    
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    
    print("Очередь после добавления элементов:")
    queue.display()
    
    removed_item = queue.dequeue()
    print(f"Удаленный элемент из очереди: {removed_item}")
    print("Очередь после удаления элемента:")
    queue.display() 
