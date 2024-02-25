import threading
import queue
import time

class PriorityMessageQueue:
    def __init__(self):
        self.queue = queue.PriorityQueue()
        self.mutex = threading.Lock()
        self.empty_condition = threading.Condition(self.mutex)

    def enqueue_message(self, message, priority):
        with self.mutex:
            self.queue.put((priority, message))
            self.empty_condition.notify()

    def dequeue_message(self):
        with self.mutex:
            while self.queue.empty():
                self.empty_condition.wait()
            return self.queue.get()

    def peek_message(self):
        with self.mutex:
            while self.queue.empty():
                self.empty_condition.wait()
            return self.queue.queue[0]

    def is_empty(self):
        with self.mutex:
            return self.queue.empty()

class ThreadPool:
    def __init__(self, num_threads):
        self.tasks = queue.Queue()
        self.workers = []
        for _ in range(num_threads):
            worker = threading.Thread(target=self.worker)
            worker.daemon = True
            worker.start()
            self.workers.append(worker)

    def worker(self):
        while True:
            task = self.tasks.get()
            if task is None:
                break
            task()
            self.tasks.task_done()

    def submit_task(self, task):
        self.tasks.put(task)

    def wait_completion(self):
        self.tasks.join()

def simple_action(message):
    print("Processing message:", message)
    time.sleep(1)  

def send_message(sender, receiver, message, priority):
    print("Sending message:", message)
    receiver.enqueue_message(message, priority)

def main():
    message_queue = PriorityMessageQueue()
    thread_pool = ThreadPool(3) 

    def receive_and_process():
        while True:
            priority, message = message_queue.dequeue_message()
            thread_pool.submit_task(lambda: simple_action(message))

    receiver_thread = threading.Thread(target=receive_and_process)
    receiver_thread.start()

   
    send_message(None, message_queue, "Hello", 2)
    send_message(None, message_queue, "World", 1)
    send_message(None, message_queue, "Priority", 1)
    send_message(None, message_queue, "Queue", 3)

    # Wait for threads to finish
    thread_pool.wait_completion()
    receiver_thread.join()

if __name__ == "__main__":
    main()
