Debugging with print
====================

The print statement helps you figure out what is going on with your code. You can use the print command to send messages to the screen as your program executes to help you find out how far it’s getting before it crashes. Or you can print out the value of certain variables as the program runs, which might help explain what is going wrong. If your code has a loop that doesn’t seem to be executing correctly, try adding a print statement at the top of the loop. Print out the loop invariant and any other local variables that might help you figure out what’s going on.

How to debug with the print statement
--------------------------------------

Let’s take a look at how `print ()` can help you debug your code. Here’s a simple function that divides two numbers:

```python
def divide(numerator, denominator):

  return numerator / denominator
```
What happens if you call this function but provide a value of zero for the denominator? Dividing by zero causes an error, specifically, a ZeroDivisionError. You could watch out for this condition by using a print statement:

```python
def divide(numerator, denominator):

  print(“dividing {} by {}”.format(numerator, denominator))

  return numerator / denominator

```
Now, if the program crashes with a ZeroDivisionError, you’ll see your printed output right before the error:

```python
>>> divide(3,0)

dividing 3 by 0

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

  File "<stdin>", line 3, in divide

ZeroDivisionError: division by zero
```

Let’s take a look at another example. Imagine you write a function to retrieve a web page and print its contents. It might look something like this:

```python
import urllib3

def get\_web\_page(url):

    http = urllib3.PoolManager()

    response = http.request("GET", url)

    print(response.data.decode("utf-8"))
```

What happens if the url parameter is incorrect or missing? What if the request causes an error? The error messages from the urllib3 library are not always clear. If the URL is missing, for example, you may see this message: `LocationValueError`. Therefore, you might want to use a `print` statement to see what the URL is before making the call:
```python
import urllib3

def get\_web\_page(url):

    http = urllib3.PoolManager()

    print("Retrieving URL:", url)

    response = http.request("GET", url)

    print("HTTP response code:", response.status, response.reason)

    print(response.data.decode("utf-8"))
```

Now you can try it again:

`HTTP response code: 200 OK`

When in doubt, add more print statements! You can always take them out when you’re finished debugging. The more output, the easier it is to find the cause of your error.

Key takeaways
-------------

You can use the print statement to help you figure out what is going on with your code. After you finish debugging, you can take the print statement out.
