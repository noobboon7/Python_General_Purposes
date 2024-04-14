Debugging with assert
=====================

A developer’s worst nightmare is to spend hours and hours developing and writing code for a program, and right before they deploy it, the developer discovers multiple bugs and errors. Instead of waiting until the last minute to check the correctness of your code, you should test it and check it throughout the development and writing process.

In this reading, you will learn more about debugging your code with `assert`.

What are assertions?
--------------------

Assertions are logical tests that developers use as a sanity check when writing code. In Python, you use an `assert` statement to write these sanity checks. When you write an `assert` statement, it is important to write it with one thing in mind: The condition you include with the `assert` statement should always be true. If the condition is false, you can use this information as a main indicator that the program has a bug. If the assert statement is false, it will automatically terminate the execution of the program and will display an error message. At this point, you can correct or fix the bug before continuing to write code to ensure you don’t introduce any additional bugs. Let’s look at an example where the condition is true and therefore no error message is displayed:

```python
a = 3 + 4

assert a == 7
```

Here, the `assert` statement says the sum of three and four should equal seven—and it does! Because the condition is true, no error message is raised to the developer.

Now let’s look at an example where some code uses an `assert` statement, and the condition is false. The code below takes a filename as an argument and then reads the file. If your function is called with an empty string instead of a filename, it will return a `FileNotFoundError` message.

```python
def read\_file\_and\_do\_something(filename):

  assert filename != “”

  with open(filename, “r”) as fp:

    …
```

Notice that in the second line of code, the ass`ert statement produces nothing and is blank.

What are the benefits of assertions?
------------------------------------

Assertions are not only beneficial to programmers to help catch bugs in their code, but they also prevent code from continuing to execute when additional input would cause further errors. In addition, you can use assert statements to create error messages that are easy to understand and user-friendly. Let’s look at an example:

```python
def read\_file\_and\_do\_something(filename):

  assert filename != “”

  with open(filename, “r”) as fp:

    …
```

Remember this code? If someone calls this function without a filename, the `assert` statement produces nothing, which can be confusing. This is because you don’t know exactly what the issue is. But what if we replace the message so that we can see exactly what is wrong with the code? We could use something like this:

```python
def read\_file\_and\_do\_something(filename):

  assert filename != “”, “You must specify a filename!”

  with open(filename, “r”) as fp:

    …
```

Look at the `assert` statement now. It produces `“You must specify a filename!”`, an error message that is clear and easy to understand.

Key takeaways
-------------

Using `assert` statements in your code enables you to check that your code works properly, detects bugs, and keeps your sanity as a developer. Use `assert` statements throughout your code to create robust and reliable code, saving you from extra debugging and code rewrites.
