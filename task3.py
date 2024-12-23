import threading
import time
import random
from collections import deque

class ThreadSafeList:
    def __init__(self):
        self.data = deque()
        self.lock = threading.Lock()
        
    def read(self):
        with self.lock:
            # Simulate reading the data
            return list(self.data)
        
    def write(self, value):
        with self.lock:
            # Simulate writing to the data
            self.data.append(value)

def reader(shared_list, read_limit):
    read_count = 0
    while read_count < read_limit:
        time.sleep(random.uniform(0.1, 0.5))  # Random sleep time
        data = shared_list.read()
        print(f"Reader read: {data}")
        read_count += 1

def writer(shared_list, write_limit):
    write_count = 0
    while write_count < write_limit:
        time.sleep(random.uniform(0.1, 0.5))  # Random sleep time
        value = random.randint(1, 100)  # Generate a random value
        shared_list.write(value)
        print(f"Writer wrote: {value}")
        write_count += 1

def main():
    shared_list = ThreadSafeList()
    
    # Start 5 reader threads with a limit of 5 reads
    reader_threads = []
    for _ in range(5):
        t = threading.Thread(target=reader, args=(shared_list, 5))
        t.start()
        reader_threads.append(t)
    
    # Start 2 writer threads with a limit of 5 writes
    writer_threads = []
    for _ in range(2):
        t = threading.Thread(target=writer, args=(shared_list, 5))
        t.start()
        writer_threads.append(t)
    
    # Let the threads run until they finish their operations
    for t in reader_threads + writer_threads:
        t.join()

if __name__ == "__main__":
    main()
