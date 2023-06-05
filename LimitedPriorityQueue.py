from queue import PriorityQueue


def limit_priority_queue(pq, k):
    new_pq = PriorityQueue()
    for i in range(k):
        if pq.empty():
            break
        new_pq.put(pq.get())
    pq.queue = new_pq.queue
