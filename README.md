# Multi-Threaded Priority Message Queue Implementation

This Python script demonstrates a multi-threaded priority message queue implementation. It allows multiple threads to send messages to each other with varying priorities and performs a simple action upon receiving a message using a thread pool.

## Components

1. **PriorityMessageQueue**: Implements a priority message queue data structure supporting enqueue, dequeue, peek, and empty check operations. It ensures thread safety using locks and condition variables.

2. **ThreadPool**: Manages a group of worker threads, allowing concurrent execution of tasks. It provides methods to submit tasks and wait for their completion.

3. **Simple Action Function**: Defines a simple action to perform upon receiving a message. It's used to demonstrate message processing using the thread pool.

4. **send_message Function**: Facilitates message sending between threads, utilizing the priority message queue.

## Usage

1. Run the script using Python 3:

    ```
    python3 priority_message_queue.py
    ```

2. The script will demonstrate sending messages between threads with different priorities and processing them concurrently using a thread pool.

## File Structure

- `priority_message_queue.py`: Contains the implementation of the priority message queue, thread pool, and main function.
- `README.md`: This file providing an overview of the script and instructions for usage.
