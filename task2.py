import threading

# Shared counter variable
counter = 0
# Lock for synchronizing access to the counter
lock = threading.Lock()

# Function for incrementing the counter
def increment_counter():
    global counter
    for _ in range(100):
        with lock:  # Synchronize access to the shared counter
            counter += 1

# Create threads
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)
thread3 = threading.Thread(target=increment_counter)

# Start threads
thread1.start()
thread2.start()
thread3.start()

# Wait for all threads to finish
thread1.join()
thread2.join()
thread3.join()

# Final value of the counter
print(f"Final value of counter: {counter}")
