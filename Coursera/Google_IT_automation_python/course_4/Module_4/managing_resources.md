More about managing resources
=============================

You’ve learned a lot about how to avoid memory leaks and manage your OS and network to achieve the best performance. Let’s look at a few more ways you can speed up your application processing and troubleshoot memory and system performance.

Using concurrency and threading
-------------------------------

Python has several tools to streamline the processing of code, including `threading`, `multiprocessing`, and a library called [asyncio](https://docs.python.org/3/library/asyncio.html).

With these, you can run things (threads, tasks, and processes) in an overlapping fashion, called _concurrency_. Similarly, you can use _asynchronous threading_, where you can tell the OS to prioritize certain threads over another. Although these are similar, they each have their own advantages.

You can also learn about concurrency and threading in the reading: [More about complex slow systems](https://www.coursera.org/learn/troubleshooting-debugging-techniques/supplement/aNk5Q/more-about-complex-slow-systems).

### Concurrency

Depending on your application’s resource needs, you may be able to use concurrency to help speed up things that are slowing down processing. Concurrency involves adding a bit of extra code to your programming to allow it to run multiple things in a sequence, but with overlapping time frames. For example, you could have hundreds of threads or requests, but you can set them to run on top of each other, instead of waiting for one to complete before the next starts.

In I/O-bound programming, where there is a lot of interfacing with networks or other hardware, using concurrency can help download network-based content faster and more efficiently. In CPU-bound programming, where the program is busy processing data, you can use concurrency to spread heavy CPU processes across multiple processors, essentially splitting the heavy load among workers.

Keep in mind, however, that adding concurrency to your code means … that’s right: more coding, and that introduces a greater risk of introducing hard-to-find errors into your program.

Learn all about concurrency, different forms of multitasking, ways to enable concurrency outside of `asyncio`, and much more in this in-depth and helpful [article](https://realpython.com/python-concurrency). And, for a good overview with clear examples of what concurrency is, read this [article](https://freecontent.manning.com/concurrency-vs-parallelism/#:~:text=Concurrency%20is%20about%20multiple%20tasks,resources%20like%20multi%2Dcore%20processor.).

### Asynchronous threading

Unlike concurrency, which involves processing things in a stacked order, we can also use _threading_—running multiple things at the same time—to increase efficiency.

For example, you might set up your threads like this:

```python
import threading

def thread_function(name):

print("Thread {} is running".format(name))

if _name_ == "__main__":

#  Create two threads

thread1 = threading.Thread(target=thread_function, args=("Thread-1",))

thread2 = threading.Thread(target=thread_function, args=("Thread-2",))

#  Start the threads

thread1.start()

thread2.start()

#  Wait for the threads to finish

thread1.join()

thread2.join()

print("All threads finished")
```

In this case, we see that the program starts, two threads are created, and each thread runs and prints out the thread name. Then the threads end and the program ends.

Using `asyncio`, we can even stage those processes to run in the order we choose.

With `asyncio`, we can use the `await` command inside of event loops to control processing for the utmost efficiency. This system is particularly useful for I/O-bound applications, where you may be waiting for a response from the network, and you want to use that time to process other tasks or threads.

You can read all about the various tricks for using `asyncio`, including scheduling, using different threads and loops, notifications, and more in this informative [article](https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32).

Checking memory usage
---------------------

Memory leaks can be a big problem when coding because they slow down the processing of your application and may create crashes. When you can evaluate programming to find issues, you can then streamline your code and/or processes to release code cleanly.

Although Python automatically manages memory as part of its language, there are several other tools you can use to look for memory leaks to ensure yours is running as efficiently as possible.

If you’re looking at a section of your code that you suspect may be slowing your application, there are packages, such as [memory-profiler](https://pypi.python.org/pypi/memory_profiler), that will evaluate a single function or code, line by line, to show detailed memory use. You can also use it to evaluate your application’s memory usage over time, helping identify memory that isn’t releasing as regularly as it should.

If you need to look at the application as a whole, try [guppy](https://zhuyifei1999.github.io/guppy3/), a library to view and evaluate memory use by different object types.

For more about memory-profiler and other tools, read [this article](https://www.pluralsight.com/blog/tutorials/how-to-profile-memory-usage-in-python).

Checking for network problems
------------------------------

If you’re not a network administrator or engineer, all those acronyms and their configurations can be a bit of a mystery: IP, SASE, IMAP, MAC, SSH, DHCP … If you’re a programmer facing network-connection issues, it can be overwhelming to sort out.

Lucky for you, you have some in-built tools to help you identify the source of the problem.

The first thing to try is to ping the server to see if it’s a server issue or an actual network issue. Sending a simple `telnet` command to the server and port you’re trying to reach can tell you if the server is having a timeout issue (or is completely down), or if there might be a problem accessing it for some other reason.

If you can’t get a response from the server, then you can probably assume there is something wrong with it or the network in between. Here’s where you detective skills come into play. First, you’ll need to test to see if it’s something on your end or on the receiving end.

Check your default gateway using the `ipconfig /all` command (in Windows) or `ifconfig -a` (in Linux). This will show you the IP addresses and DHCP connections. If you can’t see a DHCP, then you either need to renew its lease (the network connection between you and the IP address) or, in some cases, the DHCP server is down, which is a larger problem for the networking experts.

If you can see the DHCP, but the connection still isn’t working, you can try testing various devices to pinpoint the issue. In Linux, you can use the `#arp -n` command to see a list of MAC addresses for devices on the network. MAC addresses are like identifiers for individual computers instead of a network (the IP address). When you use `#arp -n`, then, you may be able to see if a device is missing a MAC address, which would tell you that it is down.

For more examples and details, check out this [article](https://www.linuxjournal.com/content/troubleshooting-network-problems). You’ll want to keep it bookmarked!

Key takeaways
-------------

Many things may cause performance issues in your programming, from memory leaks to network issues, to slow processing times. By knowing some simple tricks to code, scan, and troubleshoot, you can help your program run efficiently as possible.
