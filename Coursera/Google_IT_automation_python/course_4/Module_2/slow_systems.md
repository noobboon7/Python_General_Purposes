More about complex slow systems
===============================

Concurrency and parallelism
---------------------------

In Python, you can use concurrency to allow multiple tasks to make progress at the same time, even if they don't actually run simultaneously. This is useful when you want to optimize how tasks are scheduled and resources are used, especially for I/O-bound tasks. Concurrency lets you efficiently manage these tasks, ensuring they can smoothly move forward without being held back by other tasks.

Parallelism, on the other hand, involves running multiple processors or CPU cores at the same time. This is great for tasks that are CPU intensive. By dividing the work among multiple cores, parallelism can speed up these tasks significantly and reduce processing time.

By combining concurrency and parallelism in your Python programs, you can double their power. This should make your programs run more efficiently and responsively.

Concurrency for I/O-bound tasks
-------------------------------

Python has two main approaches to implementing concurrency: threading and asyncio.

1.  Threading is an efficient method for overlapping waiting times. This makes it well-suited for tasks involving many I/O operations, such as file I/O or network operations that spend significant time waiting. There are however some limitations with threading in Python due to the Global Interpreter Lock (GIL), which can limit the utilization of multiple cores.
    
2.  Alternatively, asyncio is another powerful Python approach for concurrency that uses the event loop to manage task switching. Asyncio provides a higher degree of control, scalability, and power than threading for I/O-bound tasks. Any application that involves reading and writing data can benefit from it, since it speeds up I/O-based programs. Additionally, asyncio operates cooperatively and bypasses GIL limitations, enabling better performance for I/O-bound tasks.
    

Python supports concurrent execution through both threading and asyncio; however, asyncio is particularly beneficial for I/O-bound tasks, making it significantly faster for applications that read and write a lot of data.

Parallelism for CPU-bound tasks
-------------------------------

Parallelism is a powerful technique for programs that heavily rely on the CPU to process large volumes of data constantly. It's especially useful for CPU-bound tasks like calculations, simulations, and data processing.

Instead of interleaving and executing tasks concurrently, parallelism enables multiple tasks to run simultaneously on multiple CPU cores. This is crucial for applications that require significant CPU resources to handle intense computations in real-time.

Multiprocessing libraries in Python facilitate parallel execution by distributing tasks across multiple CPU cores. It ensures performance by giving each process its own Python interpreter and memory space. It allows CPU-bound Python programs  to process data more efficiently by giving each process its own Python interpreter and memory space; this eliminates conflicts and slowdowns caused by sharing resources. Having said that, you should also remember that when running multiple tasks simultaneously, you need to manage resources carefully.

Combining concurrency and parallelism
-------------------------------------

Combining concurrency and parallelism can improve performance. In certain complex applications with both I/O-bound and CPU-bound tasks, you can use asyncio for concurrency and multiprocessing for parallelism.

With asyncio, you make I/O-bound tasks more efficient as the program can do other things while waiting for file operations.

On the other hand, multiprocessing allows you to distribute CPU-bound computations, like heavy calculations, across multiple processors for faster execution.

By combining these techniques, you can create a well-optimized and responsive program. Your I/O-bound tasks benefit from concurrency, while CPU-bound tasks leverage parallelism.

Selecting the right approach
----------------------------

Before developing your program, it is essential to determine whether you want to incorporate concurrency, as it is generally easier to add it later than to remove it. In order to make this decision, you must understand the tasks your application needs to perform. Your approach will depend on whether your program is CPU-bound (processing) or I/O-bound (communicating).

When you need to wait for external resources, concurrency with asyncio or threading would be more appropriate. Taking advantage of idle time during I/O operations allows your program to handle multiple tasks concurrently.

On the other hand, if you're dealing with CPU-intensive tasks, such as compression, rendering high-definition videos, or running complex simulations, multiprocessing is a good choice. By doing so, you can ensure that your system performs well by taking advantage of the power of multiple processors. You can reduce processing time by distributing computational tasks across multiple cores.

To learn more about the differences between concurrency and parallelism and how to choose the appropriate approach based on your tasks,  read more [here](https://realpython.com/python-concurrency/).

Asyncio events and task loops
-----------------------------

Python's asyncio library enables concurrent execution of multiple tasks through asynchronous operations using event loops and coroutines. A coroutine can pause execution while waiting for a specific operation, such as reading or saving data. Event loops are essential for scheduling and managing tasks, allowing smooth execution and reducing completion times. Unlike threading, this lightweight approach keeps long-running tasks from blocking the main application.

With Asyncio, you can efficiently handle small tasks, like sending emails or notifications, without creating many threads, resulting in faster notification responses. When combined with aiohttp, asyncio effectively manages multiple API calls concurrently. Asyncio offers an efficient way to handle data input/output tasks, allowing developers to create high-performance applications through simultaneous task execution.

This tool optimizes Python programs, especially those that handle notifications, web requests, and data-related tasks. If you want to learn more about asyncio and its concurrent programming capabilities, read more [here](https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32).
