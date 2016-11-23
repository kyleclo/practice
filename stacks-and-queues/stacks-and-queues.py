"""

Relation between Stacks and Queues

"""

from collections import deque


class QueueUsingTwoStacks:
    def __init__(self):
        self.outbox = []
        self.inbox = []

    def dequeue(self):
        if len(self.outbox) == 0:
            while len(self.inbox) > 0:
                self.outbox.append(self.inbox.pop())

        return self.outbox.pop()

    def enqueue(self, value):
        self.inbox.append(value)


class StackUsingTwoQueues:
    def __init__(self):
        self.current = deque()
        self.other = deque()

    def pop(self):
        while len(self.current) > 1:
            self.other.appendleft(self.current.pop())

        self.current, self.other = self.other, self.current

        return self.other.pop()


    def push(self, value):
        self.current.appendleft(value)


if __name__ == '__main__':

    print 'Enqueue values 1, 2, 3 to queue.'
    queue = QueueUsingTwoStacks()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print 'Dequeue values 1, 2, 3 in that order.'
    for _ in range(3):
        print queue.dequeue()

    print 'Push values 1, 2, 3 to stack.'
    stack = StackUsingTwoQueues()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print 'Pop values 3, 2, 1 in that order.'
    for _ in range(3):
        print stack.pop()
