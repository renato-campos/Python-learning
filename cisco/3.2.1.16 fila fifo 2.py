class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.fila = []

    def put(self, elem):
        self.fila.append(elem)

    def get(self):
        elem = self.fila[0]
        del self.fila[0]
        return elem


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        return True if len(self.fila) == 0 else False


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
