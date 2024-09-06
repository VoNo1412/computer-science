from queue import Queue

def reverse_k_elements(queue, k):
    if queue.qsize() < k or k == 0:
        return

    stack = []

    for _ in range(k):
        stack.append(queue.get())
    
    while stack:
        queue.put(stack.pop())
    
    size = queue.qsize()
    for _ in range(size - k):
        queue.put(queue.get())


q = Queue()
for i in [10, 20, 30, 40, 50]:
    q.put(i)

print(reverse_k_elements(q, 3))

queue_list = []
while not q.empty():
    queue_list.append(q.get())

print(queue_list)  # Output: [30, 20, 10, 40, 50]

