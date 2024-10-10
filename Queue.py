class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def is_empty(self):
        """Check if the queue is empty."""
        return not self.items

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return the front item of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        removed_item = self.items.pop(0)
        print(f"Dequeued: {removed_item}")
        return removed_item

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def front(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.items[0]

    def rear(self):
        """Return the rear item without removing it."""
        if self.is_empty():
            raise IndexError("Rear from empty queue")
        return self.items[-1]

    def __str__(self):
        """Return a string representation of the queue."""
        return "Queue: " + " <- ".join(map(str, self.items))


if __name__ == "__main__":
    q = Queue()

    # Enqueue elements
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    print(q)  # Output: Queue: 10 <- 20 <- 30 <- 40

    # Check size and front/rear elements
    print(f"Size: {q.size()}")
    print(f"Front: {q.front()}")
    print(f"Rear: {q.rear()}")

    # Dequeue elements
    q.dequeue()  # Removes 10
    q.dequeue()  # Removes 20
    print(q)      # Output: Queue: 30 <- 40
    print(f"Size: {q.size()}")

    # Dequeue remaining elements
    q.dequeue()  # Removes 30
    q.dequeue()  # Removes 40
    print(q)      # Output: Queue: 
    print(f"Size: {q.size()}")

    # dequeue from empty queue
    try:
        q.dequeue()
    except IndexError as e:
        print(f"Error: {e}")  # Output: Error: Dequeue from empty queue

    # access front/rear from empty queue
    try:
        q.front()
    except IndexError as e:
        print(f"Error: {e}")  # Error: Front from empty queue

    try:
        q.rear()
    except IndexError as e:
        print(f"Error: {e}")  # Error: Rear from empty queue

