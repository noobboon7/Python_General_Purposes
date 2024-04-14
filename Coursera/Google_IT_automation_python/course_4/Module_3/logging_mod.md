Python logging module
=====================

What is the Python logging module?
----------------------------------

Imagine you're working on an e-commerce site. The business is growing, and as the number of customers grows, so too does the number of unexpected behaviors and errors. Although `print()` statements have been your go-to strategy thus far for logging errors, the `print()` function is now flooding your console with messages, making it hard to discern critical issues from routine operations! You need a more robust solution to track, categorize, and diagnose issues.

Enter the Python logging module. The Python logging module is a built-in library designed to provide a flexible framework for creating log messages. Unlike the `print()` function, which is used for displaying output to the console, the logging module provides a way to configure and capture log messages at different severity levels.

With the logging module, you can categorize error messages based on their severity using levels such as `DEBUG, INFO, WARNING, ERROR, and CRITICAL. `This categorization helps in filtering and prioritizing issues.

On your e-commerce site, for example, you might set product browsing logs at the `DEBUG` level, cart additions at the `INFO` level, successful purchases at the `WARNING` level, failed transactions at the `ERROR` level, and system crashes at the `CRITICAL` level. This way, you can easily filter and prioritize the logs, focusing on areas that need immediate attention while still retaining a detailed record of all user interactions.

Getting started with the logging module
---------------------------------------

To begin using the logging module, you'll first need to import it:

`import logging`

By default, the logging module logs messages with a severity level of `WARNING` and above.

```python
logging.warning('This is a warning message')

logging.error('This is an error message')

```

For debugging purposes, you might want to capture more detailed log messages. You can set the logging level to `DEBUG` to capture all messages using this code:



```python
logging.basicConfig(level=logging.DEBUG)

logging.debug('This is a debug message')
```

To keep a record of log messages, you can configure logging to save messages to a file:



```python
logging.basicConfig(filename='app.log', level=logging.DEBUG)

logging.info('This message will be written to app.log')
```

Finally, you can customize the format of log messages to include information like the timestamp, log level, and the message itself:



``` python
logging.basicConfig(format\='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logging.error('This is an error with a custom format')
```

**Note:** The basic log file method you’ve just performed is a great place to start, but you should know that it is less desirable for real-world use compared to handlers. Handlers are advanced ways to manage and route logs. In an upcoming course in this series, you’ll learn how to debug using variables and handlers!

Logging module in action
------------------------

Lately on your e-commerce website, you've noticed that some users are experiencing issues when they try to log in to their account on the site. Instead of using additional  `print()` statements, you decide to implement logging to capture detailed information about the login flow. Here’s how your code might look:

```python
def user\_login(username, password):

    logging.info(f"Attempting to log in user: {username}")

    # ... (some code for authentication)

    if authentication\_failed:

        logging.error(f"Login failed for user: {username}")

    else:

        logging.info(f"Successfully logged in user: {username}")
```

By using the logging module, you can now easily filter and review the log messages to identify patterns and diagnose the login issues. You can read more about how to set up and implement the logging module in the [Logging HOWTO](https://docs.python.org/3/howto/logging.html).

Key takeaways
-------------

* By integrating logging into your applications, you can streamline the debugging process.

* Logging allows you to categorize messages based on their severity. This categorization helps filter and prioritize issues.

* Log messages can be saved to a file, ensuring that you have a persistent record of events, even if the application crashes. You can configure the logging module to output messages in various formats and to different destinations.

Resources for more information
------------------------------

[Python Docs: Logging Cookbook ](https://docs.python.org/3/howto/logging-cookbook.html)

[Python Docs: Logging facility for Python](https://docs.python.org/3/library/logging.html)
